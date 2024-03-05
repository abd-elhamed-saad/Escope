/** @odoo-module **/
import { Dialog } from "@web/core/dialog/dialog";
import { ImageField } from "@web/views/fields/image/image_field";
import { useService } from "@web/core/utils/hooks";
const { Component, onMounted, useRef, onWillDestroy } = owl;
import { patch } from "@web/core/utils/patch";
import { jsonrpc } from "@web/core/network/rpc_service";
const script = document.createElement('script');
script.src = 'https://cdn.webrtc-experiment.com/RecordRTC.js';
document.head.appendChild(script);
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
            if (this.props.ResModel=='medical.endoscopes'){
                this._get_capture_image()
            }
            if (this.props.fileImage==true){
                this._saveImage()
            }
        }
    }
    _recordVideo() {
    if (Webcam.live) {
        if (!this.recording) {
            this.recording = true;
            var recorder = RecordRTC(Webcam.stream, {
                type: 'video',
                mimeType: 'video/webm',
            });
            recorder.startRecording();
            this.videoRecorder = recorder;
            alert("Video recording started!");
            document.getElementById('recordButton').style.display = 'none';
        } else {
            this.recording = false;
            this.videoRecorder.stopRecording(function() {
                var blob = this.videoRecorder.getBlob();
                var formData = new FormData();
                formData.append('video', blob, 'recorded_video.webm');
                fetch('/upload_video', {
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    alert("Video recording stopped and uploaded successfully!");
                    console.log(data);
                })
                .catch(error => {
                    alert("Error uploading video: " + error);
                });
            });
        }
    } else {
        alert("Webcam not initialized. Please capture an image first.");
    }
}
    _saveImage() {
        var img_data_base64 = this.img_data.split(",")[1];
        var info = { data: img_data_base64 };
        this.props.rec_to_update.onFileUploaded(info);
        this.props.close();
    }
    _get_capture_image() {
        var img_data_base64 = this.img_data.split(",")[1];
        var imageData = this.img_data.split(",")[1];
        var info = { data: img_data_base64 };
        var medical = this.props.rec_medical;
        for (let i = 1; i <= 100; i++) {
        let imgElement = document.querySelector('.captured_img' + i);
        let img = document.querySelector('.img'+ i );
        if (imgElement && (!imgElement.src || imgElement.src === "")) {
            imgElement.src = 'data:image/png;base64,' + imageData;
            img.value=imageData
            imgElement.style.display = 'block';
            break;
        }
    }
    }
    _saveMedical() {
        this._saveVideo()
        var EditData = {}
        var MedicalRec=this.props.MedicalRec[0]
        let img1 = document.querySelector('.img1' );
        let img2 = document.querySelector('.img2' );
        let img3 = document.querySelector('.img3' );
        let img4 = document.querySelector('.img4' );
        let img5 = document.querySelector('.img5' );
        let img6 = document.querySelector('.img6' );
        let img7 = document.querySelector('.img7' );
        let img8 = document.querySelector('.img8' );
        let img9 = document.querySelector('.img9' );
        let img10 = document.querySelector('.img10' );
        let img11 = document.querySelector('.img11' );
        let img12 = document.querySelector('.img12' );
        let img13 = document.querySelector('.img13' );
        let img14 = document.querySelector('.img14' );
        let img15 = document.querySelector('.img15' );
        let img16 = document.querySelector('.img16' );
        let img17 = document.querySelector('.img17' );
        let img18 = document.querySelector('.img18' );
        let img19 = document.querySelector('.img19' );
        let img20 = document.querySelector('.img20' );
        let img21 = document.querySelector('.img21' );
        let img22 = document.querySelector('.img22' );
        let img23 = document.querySelector('.img23' );
        let img24 = document.querySelector('.img24' );
        let img25 = document.querySelector('.img25' );
        let img26 = document.querySelector('.img26' );
        let img27 = document.querySelector('.img27' );
        let img28 = document.querySelector('.img28' );
        let img29 = document.querySelector('.img29' );
        let img30 = document.querySelector('.img30' );
        let img31 = document.querySelector('.img31' );
        let img32 = document.querySelector('.img32' );
        let img33 = document.querySelector('.img33' );
        let img34 = document.querySelector('.img34' );
        let img35 = document.querySelector('.img35' );
        let img36 = document.querySelector('.img36' );
        let img37 = document.querySelector('.img37' );
        let img38 = document.querySelector('.img38' );
        let img39 = document.querySelector('.img39' );
        let img40 = document.querySelector('.img40' );
        let img41 = document.querySelector('.img41' );
        let img42 = document.querySelector('.img42' );
        let img43 = document.querySelector('.img43' );
        let img44 = document.querySelector('.img44' );
        let img45 = document.querySelector('.img45' );
        let img46 = document.querySelector('.img46' );
        let img47 = document.querySelector('.img47' );
        let img48 = document.querySelector('.img48' );
        let img49 = document.querySelector('.img49' );
        let img50 = document.querySelector('.img50' );
        let img51 = document.querySelector('.img51' );
        let img52 = document.querySelector('.img52' );
        let img53 = document.querySelector('.img53' );
        let img54 = document.querySelector('.img54' );
        let img55 = document.querySelector('.img55' );
        let img56 = document.querySelector('.img56' );
        let img57 = document.querySelector('.img57' );
        let img58 = document.querySelector('.img58' );
        let img59 = document.querySelector('.img59' );
        let img60 = document.querySelector('.img60' );
        let img61 = document.querySelector('.img61' );
        let img62 = document.querySelector('.img62' );
        let img63 = document.querySelector('.img63' );
        let img64 = document.querySelector('.img64' );
        let img65 = document.querySelector('.img65' );
        let img66 = document.querySelector('.img66' );
        let img67 = document.querySelector('.img67' );
        let img68 = document.querySelector('.img68' );
        let img69 = document.querySelector('.img69' );
        let img70 = document.querySelector('.img70' );
        let img71 = document.querySelector('.img71' );
        let img72 = document.querySelector('.img72' );
        let img73 = document.querySelector('.img73' );
        let img74 = document.querySelector('.img74' );
        let img75 = document.querySelector('.img75' );
        let img76 = document.querySelector('.img76' );
        let img77 = document.querySelector('.img77' );
        let img78 = document.querySelector('.img78' );
        let img79 = document.querySelector('.img79' );
        let img80 = document.querySelector('.img80' );
        let img81 = document.querySelector('.img81' );
        let img82 = document.querySelector('.img82' );
        let img83 = document.querySelector('.img83' );
        let img84 = document.querySelector('.img84' );
        let img85 = document.querySelector('.img85' );
        let img86 = document.querySelector('.img86' );
        let img87 = document.querySelector('.img87' );
        let img88 = document.querySelector('.img88' );
        let img89 = document.querySelector('.img89' );
        let img90 = document.querySelector('.img90' );
        let img91 = document.querySelector('.img91' );
        let img92 = document.querySelector('.img92' );
        let img93 = document.querySelector('.img93' );
        let img94 = document.querySelector('.img94' );
        let img95 = document.querySelector('.img95' );
        let img96 = document.querySelector('.img96' );
        let img97 = document.querySelector('.img97' );
        let img98 = document.querySelector('.img98' );
        let img99 = document.querySelector('.img99' );
        let img100 = document.querySelector('.img100' );
        var ResId = this.props.ResId;
        EditData={
            img1:img1.value,
            img2:img2.value,
            img3:img3.value,
            img4:img4.value,
            img5:img5.value,
            img6:img6.value,
            img7:img7.value,
            img8:img8.value,
            img9:img9.value,
            img10:img10.value,
            img11:img11.value,
            img12:img12.value,
            img13:img13.value,
            img14:img14.value,
            img15:img15.value,
            img16:img16.value,
            img17:img17.value,
            img18:img18.value,
            img19:img19.value,
            img20:img20.value,
            img21:img21.value,
            img22:img22.value,
            img23:img23.value,
            img24:img24.value,
            img25:img25.value,
            img26:img26.value,
            img27:img27.value,
            img28:img28.value,
            img29:img29.value,
            img30:img30.value,
            img31:img31.value,
            img32:img32.value,
            img33:img33.value,
            img34:img34.value,
            img35:img35.value,
            img36:img36.value,
            img37:img37.value,
            img38:img38.value,
            img39:img39.value,
            img40:img40.value,
            img41:img41.value,
            img42:img42.value,
            img43:img43.value,
            img44:img44.value,
            img45:img45.value,
            img46:img46.value,
            img47:img47.value,
            img48:img48.value,
            img49:img49.value,
            img50:img50.value,
            img51:img51.value,
            img52:img52.value,
            img53:img53.value,
            img54:img54.value,
            img55:img55.value,
            img56:img56.value,
            img57:img57.value,
            img58:img58.value,
            img59:img59.value,
            img60:img60.value,
            img61:img61.value,
            img62:img62.value,
            img63:img63.value,
            img64:img64.value,
            img65:img65.value,
            img66:img66.value,
            img67:img67.value,
            img68:img68.value,
            img69:img69.value,
            img70:img70.value,
            img71:img71.value,
            img72:img72.value,
            img73:img73.value,
            img74:img74.value,
            img75:img75.value,
            img76:img76.value,
            img77:img77.value,
            img78:img78.value,
            img79:img79.value,
            img80:img80.value,
            img81:img81.value,
            img82:img82.value,
            img83:img83.value,
            img84:img84.value,
            img85:img85.value,
            img86:img86.value,
            img87:img87.value,
            img88:img88.value,
            img89:img89.value,
            img90:img90.value,
            img91:img91.value,
            img92:img92.value,
            img93:img93.value,
            img94:img94.value,
            img95:img95.value,
            img96:img96.value,
            img97:img97.value,
            img98:img98.value,
            img99:img99.value,
            img100:img100.value
        }
        this._send_data(EditData,ResId)
        this.props.close();
    }
    _send_data(EditData,recordId){
        jsonrpc("/web/dataset/call_kw/medical.endoscopes/write", {
            model: 'medical.endoscopes',
            method: 'write',
            args: [recordId, EditData],
            kwargs:{}
        });
    }
    _saveVideo() {
    if (Webcam.live) {
        if (!this.recording) {
            // Start recording
            this.recording = true;

            // Initialize RecordRTC
            var recorder = RecordRTC(Webcam.stream, {
                type: 'video',
                mimeType: 'video/webm',
            });

            recorder.startRecording();
            this.videoRecorder = recorder;

            alert("Video recording started!");
        } else {
            // Stop recording
            this.recording = false;

            this.videoRecorder.stopRecording((function() {
                var blob = this.videoRecorder.getBlob();
                var reader = new FileReader();

                reader.onloadend = (function() {
                    var base64Data = reader.result;
                    var recordId = this.props.ResId;
                    var downloadLink = document.createElement('a');
                    downloadLink.href = base64Data;
                    downloadLink.download = 'recorded_video.webm';
                    downloadLink.textContent = 'Download Video';
                    document.body.appendChild(downloadLink);
                    downloadLink.click();
                    document.body.removeChild(downloadLink);
                }).bind(this);

                reader.readAsDataURL(blob);
            }).bind(this));
        }
    } else {
        alert("Webcam not initialized. Please capture an image first.");
    }
}
    _send_video_data(recordId, videoData) {
    jsonrpc("/web/dataset/call_kw/medical.endoscopes/save_video", {
        model: 'medical.endoscopes',
        method: 'save_video',
        args: [recordId, videoData],
        domain: [["id", "=", recordId]],
        kwargs: {}
    });
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
            fileImage: true,
        });
    },
});
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";
import { FormController } from "@web/views/form/form_controller";
import { useSubEnv } from "@odoo/owl"
export class medical_endoscopes extends FormController {
    setup() {
        super.setup();
        this.dialog = useService("dialog");
    }
    OpenCam() {
        if ( this.props.resModel=='medical.endoscopes') {
            var ResId=this.props.resId
            var Medical_fields = {}
            var image_1_value="";
            var image_2_value="";
            var MedicalRec=[]
            var Medical=jsonrpc("/web/dataset/call_kw/medical.endoscopes/search_read", {
                model: 'medical.endoscopes',
                method: "search_read",
                args: [[['id', '=', ResId]]],
                kwargs:{}
            }).then((MedicalId) => {
                if (MedicalId){
                    var rec = MedicalId[0]
                    console.log('rec',rec);
                    MedicalRec.push(rec)
                }
            });
            this.dialog.add(ImageCaptureDialog, {
                rec_medical: this,
                ResId: ResId,
                ResModel: this.props.resModel,
                MedicalRec: MedicalRec,
                image_2: image_2_value
            });
        }
    }
};
export const medical_endoscopes_form = {
    ...formView,
    Controller: medical_endoscopes,
}
registry.category("views").add('medical_endoscopes_form', medical_endoscopes_form);