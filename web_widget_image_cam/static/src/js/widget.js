/** @odoo-module **/
console.log("@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!")
import { Dialog } from "@web/core/dialog/dialog";
import { ImageField } from "@web/views/fields/image/image_field";
import { useService } from "@web/core/utils/hooks";
const { Component, onMounted, useRef, onWillDestroy } = owl;
import { patch } from "@web/core/utils/patch";

class ImageCaptureDialog extends Component {
    setup() {
        super.setup();
        this.live_cam_img = useRef("live_cam_img");
        this.webcam_img = useRef("webcam_img");
        this.img_data = "";
        onMounted(() => {
            Webcam.set({
                width: 320,
                height: 240,
                dest_width: 320,
                dest_height: 240,
                image_format: "jpeg",
                jpeg_quality: 90,
                force_flash: false,
                fps: 45,
            });

            Webcam.attach(".live_cam_img");
            $(".save_close_btn").attr("disabled", "disabled");
            $(this.webcam_img.el).html(
                '<img src="/web/static/img/placeholder.png"/>'
            );
        });

        onWillDestroy(() => {
            Webcam.reset();
        });
    }

    _captureImage() {
        var self = this;
        Webcam.snap(function (data) {
            self.img_data = data;
            console.log("DATA", self);
            $(self.webcam_img.el).html(`<img src="${data}"/>`);
        });
        if (Webcam.live) {
            $(".save_close_btn").removeAttr("disabled");
        }
    }

    _saveClose() {
        console.log("savwe close", this);
        var img_data_base64 = this.img_data.split(",")[1];
        var info = { data: img_data_base64 };
        this.props.rec_to_update.onFileUploaded(info);
        this.props.close();
    }
}
ImageCaptureDialog.components = { Dialog };
ImageCaptureDialog.template = "web_widget_image_cam.CameraDialog";
patch(ImageField.prototype,{
    setup() {
        super.setup();
        this.dialog = useService("dialog");
    },

    onOpenCam() {
        console.log("Opening camera dialog", ImageCaptureDialog);
        this.dialog.add(ImageCaptureDialog, {
            rec_to_update: this,
        });
    },
});