# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e697cb2-c6ae-3e32-83c7-8d197c0f0bc7 | -3.04792 | -54.15153 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc690109-fcf3-31d8-a1e2-e5934bc52bbc | -6.44534 | -55.02542 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97999e2e-b1cc-38c1-9235-47812f12f684 | -2.77048 | -54.10884 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| be5427b8-b494-3880-bd15-181278e54f46 | -3.29769 | -53.86392 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69bd2b33-2b6d-34f4-be55-263a43ae3003 | -3.51289 | -41.9433 | 2026-10-07 04:19:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8136b9ea-7788-3f92-b0b9-f91fb8167a3b | -3.99217 | -56.2647 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 096a2148-2f1b-3269-8a7e-b59ff2838951 | -3.47227 | -50.0821 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38a443be-6e68-35df-a8c6-a658db32e814 | -2.76143 | -54.08655 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| eb6a3f0f-ebbf-302d-a710-1a390857c3a6 | -3.00496 | -54.13891 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cfca857e-be26-3b1f-97d0-ae0de6a3ae46 | -6.59537 | -41.55242 | 2026-10-07 04:19:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fcd5d84d-5929-34f1-a135-c0ebeee30fda | -7.29931 | -47.26947 | 2026-10-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c6f4fd9-be5b-3019-aca5-2a9ecc1faec4 | -3.22455 | -53.88526 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a5fd2c5-8741-3938-ac81-5bfb28d494fc | -3.02248 | -53.89465 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 523b4f11-1cd6-3480-8aea-4337351f3bfe | -4.83615 | -45.79713 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6803660b-ac73-37ad-88f2-38f3c86abc49 | -3.35415 | -50.47315 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52d4bee7-3324-376c-afc4-929971d1d999 | -3.2131 | -53.87843 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 037b359d-78a3-3ca9-8bbb-9cb0301d3e46 | -2.71928 | -47.55985 | 2026-10-07 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 992202ef-20d2-3e34-b109-ef3036a31734 | -3.20302 | -42.95753 | 2026-10-07 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e14a38ac-0bbd-32cd-9543-c4370ba1177c | -3.23522 | -50.17773 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72a2f412-b49d-33d4-a33a-c3246b6a6bad | -4.35886 | -47.78254 | 2026-10-07 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6f94cde8-ba80-370e-8e63-c9774cca0d6a | -6.16012 | -47.37629 | 2026-10-07 04:19:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f919b891-cec9-3af7-9779-fec5a4b6322e | -5.97357 | -40.95593 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 126d0dd8-dc18-38fb-8fda-0c67ad99ba28 | -4.30563 | -50.78506 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75cc0475-ac0f-30af-a6e0-be7968a621a4 | -3.05914 | -54.14667 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba9ee731-f63d-3b60-a85a-804a0c2fa292 | -3.80971 | -51.04351 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc1bf648-9441-3e4b-be76-6b7a02e3d16b | -3.52516 | -54.64806 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2aabfbd0-8d7e-3b6c-8752-5216c34c8924 | -6.91955 | -47.65831 | 2026-10-07 04:19:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5801695-13e2-31b1-a867-46997ecf014a | -2.86944 | -54.15577 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cea6cbb-4109-3cb8-b60b-325864c2805d | -2.80504 | -52.09362 | 2026-10-07 04:19:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e26f586c-3b99-38a0-bc2c-2ba780bfd147 | -3.15829 | -50.44399 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2be45b10-9fd0-3ce6-9b73-12ce06506ff1 | -4.0453 | -50.98466 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 346c22e3-c6ed-3a64-b145-139fd7802459 | -3.08788 | -53.72837 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a93eacd6-6c02-3e2f-9055-dea65c10e5b4 | -3.08484 | -54.25908 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c139fe1-7c00-3615-826b-6ce54c0180aa | -3.51519 | -54.66151 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 808d36ca-50d1-359f-843c-f716f94c2406 | -2.86918 | -54.21384 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 846d8b49-2e23-37f1-9567-a8f642c4a30b | -3.16986 | -50.44734 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df6d749f-2855-3fb9-9868-dc660de61b74 | -3.28799 | -54.06241 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0865b91a-81cc-3d1a-b42b-ea5d39199977 | -5.73092 | -41.72512 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84d6916c-2610-3280-8b5d-d6bf0e17da9e | -1.27974 | -54.56644 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54a00375-b5fe-341d-ae91-7ad8be559ad1 | -6.35331 | -42.5418 | 2026-10-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74e909ee-9bc4-3b27-97b3-ab7a1747e755 | -6.99041 | -43.21897 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 114a7b98-0c37-3e74-8c1e-4bb493bf8b28 | -2.15091 | -51.98105 | 2026-10-07 04:19:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a77afb86-bc5d-3460-bc50-e8a468fadc72 | -3.04503 | -53.90525 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ddfe705-d482-30dc-a49f-61337b4642a2 | -3.52072 | -54.66785 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d5d2f901-7547-362f-b6b0-975a72bb6595 | -1.28627 | -54.56793 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa268902-a2ba-3f19-a833-30649917d04d | -3.2755 | -54.03191 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 30901c4e-7608-38e4-a9f3-8184f7ff4a2d | -3.28949 | -54.02458 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f852d598-aaec-3ee8-a844-96a424d1c05a | -7.12566 | -44.07901 | 2026-10-07 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7aa2ab65-632a-3a09-9fcb-3a384938048f | -2.87353 | -54.20715 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b34f5f80-8703-36c3-9b70-ef8e5c20dc98 | -5.22894 | -48.39673 | 2026-10-07 04:19:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 315cccc5-0443-364f-af7e-4373a348cae1 | -3.0978 | -54.18393 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99460d92-f2ac-314c-a3c0-5139b07bfcb7 | -7.18082 | -52.61353 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a83bdd1-0e4c-365f-8498-5477a39e1550 | -5.27553 | -43.3638 | 2026-10-07 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a73945fb-71ff-3d0b-877c-569b26412fb1 | -3.13966 | -51.02776 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5a93b7-2915-3f3b-b53a-3e2682a57754 | -6.14784 | -51.73431 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0236052e-9647-3d34-becd-6ecb6961351d | -6.93774 | -43.05798 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2c1b552-d0b6-33e2-9ac8-1024d5aa1828 | -3.28006 | -54.04264 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7908a193-b099-34e0-b85a-eb56b00f8320 | -3.50793 | -51.69261 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83d46952-48a5-386f-ae4e-b9e82e3c8465 | -2.20364 | -48.14962 | 2026-10-07 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e3bef1c-375e-3a44-a6f1-5e3ac9ed816b | -3.50036 | -54.63898 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3656a82d-b0b5-3756-826e-f225e9acd09d | -1.5686 | -47.73777 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb245cc7-d4b9-37f2-aa8a-0d3b1665115d | -3.72924 | -51.21275 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a297e320-83c8-33d9-a28c-0c16c6f2d0bd | -3.35682 | -50.76968 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c34f589-0492-3a09-868c-af6d6f5c3e7d | -7.60687 | -44.63604 | 2026-10-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1175dcef-3d68-3102-aa9d-fc3c5a3d8ec1 | -2.77691 | -54.08776 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 923ba47e-0739-3556-997c-de774460db84 | -3.47633 | -55.43377 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae39b4cf-13d4-30d4-aa8a-068d3ebaa74a | -2.96415 | -40.39407 | 2026-10-07 04:19:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 30a66b9e-a428-3726-8237-af0aa707d598 | -3.58565 | -54.30462 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99d8093a-f3e3-3c4b-acc1-7af68429a7a0 | -3.03723 | -53.91373 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38290cd4-bcfc-3640-b545-2e93e7f37986 | -3.27057 | -54.06097 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f14ade1-5ddb-3191-8ca3-36ebdd791ea7 | -4.47655 | -38.17448 | 2026-10-07 04:19:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65740a99-9280-36dc-960f-b99a903e6ff7 | -4.36574 | -43.91238 | 2026-10-07 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af1b9217-83c5-3b53-8709-ce5a2d4c82c5 | -3.96319 | -56.06193 | 2026-10-07 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b12f7a3-4c7b-3ac6-bfc7-27fe590c41eb | -3.0905 | -54.30166 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7f7aae54-1cda-316c-be9f-74abba3e3580 | -5.72662 | -45.15308 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ccbdfac8-d2a1-3dad-bc12-a1f44e41316c | -3.04131 | -53.88998 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c7eaa05-55cb-3d54-b8e0-730dc5e60d52 | -3.13059 | -54.37228 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eff2f5b0-168d-3458-b050-0f68987a2f60 | -2.98652 | -54.05953 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db8f6c83-6094-3c97-8eef-9ae54b626a64 | -4.11732 | -50.83137 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f598b6d9-8b52-3295-9599-a170f913927e | -5.17853 | -46.27106 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd42e629-d843-333b-815e-c2273f258403 | -5.72304 | -41.66511 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aadcb77b-845c-3591-87cd-b1491db7a382 | -4.3471 | -43.79784 | 2026-10-07 04:19:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc8de6de-3a6d-3c57-800d-a68240d084fe | -5.97423 | -40.9289 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 73cf90c7-89eb-33bb-bb65-fea2f8dfc488 | -4.92083 | -55.87498 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd580f57-9b33-3785-987e-26ff7e2951cd | -3.80622 | -47.4942 | 2026-10-07 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 506edaf1-4269-3853-9da6-54e0c99d7c29 | -6.86109 | -43.07075 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b9d4ef7-5b25-3f3e-8bb9-25d8b134a706 | -3.12558 | -53.76719 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3e5ed7b-336f-31b7-bf7a-3c4fc54e9dff | -4.91726 | -42.75217 | 2026-10-07 04:19:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 295f0dad-8a7d-33fe-8da2-11f167bb82aa | -7.70021 | -41.23944 | 2026-10-07 04:19:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b046cd1a-b46d-3507-a495-e6817c9a372a | -5.09857 | -45.83413 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb277aa6-2d7e-31b6-842c-b71cfc6a9a4a | -2.95952 | -51.05222 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e5ed653-c27b-3435-b8e4-08813d64f9ba | -3.07855 | -54.25796 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a16583c8-f9b1-37ea-9b1a-584850b746ed | -3.48485 | -50.0946 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e40d21b6-f002-3173-a9e8-c8f437660661 | -5.7248 | -45.16436 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e1584127-c9b6-3cde-b9d4-9d4dd05de147 | -4.10039 | -52.06986 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a785d84a-752d-3ce4-ac59-4e3db34e1530 | -2.76682 | -54.09267 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c8ba89fa-f4c2-31f3-97bb-feb504114654 | -5.97304 | -40.93651 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 87ae47c7-c113-3708-9ccb-54020807fcd5 | -3.41327 | -42.65904 | 2026-10-07 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15ebdf3b-6131-3a4e-bf31-5b9c0cc6633f | -5.68815 | -40.89426 | 2026-10-07 04:19:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9028d8c9-6b77-3e5c-b832-1c667db1f4e5 | -3.07422 | -54.26479 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README50.md)
