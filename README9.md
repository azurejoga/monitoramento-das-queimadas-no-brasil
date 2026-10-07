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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55da69f3-2b77-338d-9729-69672bee70df | -2.9425 | -54.142502 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd23c612-ffae-3bdf-a4ee-08a7b8b1e8de | -2.7551 | -57.6605 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4475d60c-b38e-3167-9b3e-2dd94a986aa4 | -2.7663 | -54.0923 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 834bada1-60ca-3dd4-abe4-97284835990b | 1.9778 | -60.606499 | 2026-10-07 00:47:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ec8590e-173e-3ab6-b6fe-ac33b559eec6 | -9.2989 | -63.739498 | 2026-10-07 00:47:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93127199-c0f4-3638-909f-c9d1bab31127 | -3.0268 | -53.886799 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bb34b76-9282-38ec-a82b-44a52694c9e3 | 0.7923 | -59.1922 | 2026-10-07 00:47:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| abb3ab4e-60be-3a39-ac16-bbba4b091da5 | -4.4434 | -54.9743 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6dee79b-dcde-33b5-aca1-4a6073e141b0 | -3.163 | -50.556499 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80b3284b-4b79-3a31-b2d4-38fa23a871ff | -3.5504 | -59.4785 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dad84eb4-2280-39be-96ba-006af41a121e | -3.2696 | -54.002201 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5369a2b1-3a14-33bf-a582-ed739a663a29 | -2.8472 | -59.105598 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcd6f4f2-8d05-32a7-abd0-6e6f0b7f9434 | -3.008 | -54.114498 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45e99255-52c5-31a2-b8f8-870293ea347e | -3.2684 | -54.041401 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 155ae20d-60e2-335e-8417-c0174e631bc6 | -3.4955 | -54.617901 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a02692a5-e901-3d7d-a2fe-bbfcd88a3070 | -9.1454 | -65.940399 | 2026-10-07 00:47:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae460131-288d-3af7-b076-747ad78c1b73 | -3.4755 | -59.466301 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14f3e7de-879e-349f-b2ab-48fab1a1fddd | -4.3695 | -55.452702 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 462a372c-4f3f-345c-9481-bd2b932e952e | -2.7104 | -57.464901 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3a8190c-b571-36fe-8709-2e2e726bb8a5 | -4.7539 | -55.643299 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96e337b7-ec9d-3ff3-af33-295d21acfab0 | -3.0933 | -54.260502 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 431bc131-843c-3dbb-8cdc-6477024f8cca | -3.8881 | -59.330898 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 110c502c-868f-33ef-956d-2878a214c597 | -3.5572 | -54.484901 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb895454-dcc1-35c8-8f06-9cbb3753bb1b | -3.059 | -59.903702 | 2026-10-07 00:47:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29a3f804-47a1-304c-9494-97158a2a7cbf | -3.0259 | -53.927101 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53954ddc-a991-3216-b9f4-c5bf64bf6173 | -3.4944 | -51.689201 | 2026-10-07 00:47:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1eac9b3-efc1-3ca0-afad-40b310c37f8b | -3.1778 | -50.5756 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79bf5648-0495-3fd8-9a6f-2767a5234f2a | -11.0455 | -45.810501 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55ed9dbc-8081-38d7-bae1-e807bab0d117 | -6.7794 | -56.239101 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09d0fb9-1956-31f2-8e65-b4aebe5d4cf6 | -3.539 | -59.473701 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b040bf37-dabb-3141-86a6-bc51a8924d56 | -3.0864 | -54.2747 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28b09c32-fdc0-36b3-8013-0d98552b8e3d | -3.001 | -54.129002 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf979cf-07f7-3d6c-8927-1bfc8587bc26 | -3.1696 | -57.534401 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d82ae2ea-ea5a-3cf5-9084-898ee5aec558 | -11.0942 | -45.688202 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb4b5c29-55c5-3ea6-9199-ab09127711f2 | -3.6677 | -59.631901 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dad770d-a12d-3e39-81e0-ce1911b7d226 | -3.2879 | -54.0369 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfdc974-0ab1-3fd0-a247-24410cd16329 | -3.0529 | -54.219299 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6bcc04f-ebdb-3a02-a47c-b13d2ebe9c35 | -4.1447 | -55.150902 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fc8cb1a-69b3-31a7-99ae-598a20e2099a | -2.9563 | -54.113499 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d33e81e-ad60-3616-a41a-c051c5eeee94 | -3.4902 | -51.671501 | 2026-10-07 00:47:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e78c34a-c74e-312b-80a0-6b09ef6a1edb | -3.4838 | -59.457298 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 814814ed-403d-36ba-a5b4-8e214e8050bb | 4.1528 | -61.247101 | 2026-10-07 00:47:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2257b1f0-169a-3c4f-a109-9235caf419e0 | -2.7595 | -54.106899 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f60d51a1-ff26-3ec1-9c58-5814194ee84b | -3.0555 | -54.1422 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf5df3c-1bd3-3bf8-8ebb-4b868dd026da | -3.1745 | -58.639999 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29e1dd75-6325-3385-a882-2bb50eca5e6e | -6.2099 | -52.8214 | 2026-10-07 00:47:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d52a73df-ea68-3df7-b42f-d3ef54ebc6ea | -3.5545 | -54.473598 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff8d95fb-1c3d-34ad-9978-376954d455be | -3.2615 | -54.055901 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b874430-f4ed-3e0a-87f2-2a2d508fc8d0 | -3.0424 | -53.909901 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6c31292-882b-35cf-89b4-096d05795b05 | -2.3237 | -57.983101 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7fa819f-a4f8-3b80-b340-8b7f3f0e92d9 | -2.9787 | -54.121201 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4287bd6-befb-3bac-a263-9dee51c679a8 | -2.9286 | -54.171398 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8a95ba5-4a12-394d-8a90-dd8d28f8d1a1 | -2.779 | -54.102402 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 113dab78-faa9-330d-a77d-d6d303c11c84 | -4.756 | -55.652599 | 2026-10-07 00:47:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46394a3c-4c2e-3957-9805-dcd1efbc14eb | 3.2284 | -61.049099 | 2026-10-07 00:47:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7b068e79-9d06-35be-b359-6596e57552ac | -2.8415 | -54.061901 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51a51a6b-1b2f-3f82-8795-d6b945c08ea5 | -1.792 | -57.0979 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 192203d9-6368-3b4a-9871-7d80dffe2fa4 | -2.7538 | -54.0821 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46be8495-23ad-3ab3-a0ec-e74c73d0cafa | -2.5248 | -58.096298 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 930d362f-6412-3f52-bf7c-cd7eca4413f4 | -3.2973 | -59.498901 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa45d94a-1ff9-318f-baca-8e43c886ede3 | -2.966 | -54.111301 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceb76ad2-edf9-3140-a355-cb16ac11c79a | -3.5104 | -54.638 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9bce52-a190-30af-916d-acef81779e1d | -3.4791 | -59.573502 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1a4c66e-ec11-3c5b-9ddc-6fd4d49fd938 | -3.068 | -54.152 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b354c2-de69-377b-baaf-8f56c747ab7b | -3.3918 | -59.506599 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1eef18d-a679-3164-b0c9-1498efcf8a0a | -2.0996 | -52.0714 | 2026-10-07 00:47:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7cf7e13-7b24-321a-b311-899a5470ed53 | -9.4627 | -64.324898 | 2026-10-07 00:47:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b9173c01-63b8-3821-b04c-730911fbd95b | -3.3934 | -59.5135 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 432ce449-5cb6-3e96-8bd0-8a5a3c283da4 | -3.8662 | -55.992599 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2172bba-7f67-3615-b2a4-a32d1e4449c8 | -3.0355 | -58.6637 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| afc72151-d91a-354c-b540-272b0dc61167 | -10.8406 | -50.650799 | 2026-10-07 00:47:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b42b2929-47f2-339c-88bf-44d44bbb698d | -3.6759 | -59.622898 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94fafb05-8856-3995-8d5f-1c7945e0dc1e | -3.5587 | -59.469398 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0491f0fe-44ce-39c9-aa26-233245908c22 | -3.53 | -54.6334 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1c155a-6559-30a9-9c7a-1bfb1b7af4ac | -3.4724 | -59.452599 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb9efc24-8631-3e29-9fd8-5742376d11dc | -8.2674 | -50.2533 | 2026-10-07 00:47:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b89e65a2-3017-383f-a77b-69b9b2918232 | -3.2656 | -54.029099 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c757be2-4572-3052-9f9f-db093034b63a | -3.1681 | -50.5779 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a00aa3-6c25-3740-8d73-bf44bd21a8a6 | -3.989 | -56.256302 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179ff160-7316-34d4-8a4a-4587d1a599f6 | -12.4772 | -51.284901 | 2026-10-07 00:47:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1457e5f6-8de7-3042-8281-e56368923039 | -3.7699 | -59.4006 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d428c6b-46d2-3714-a643-c99620b0e8cc | -3.987 | -56.247501 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1952feaa-30af-34cb-bb6d-02cc50dd65b1 | -3.4786 | -55.430801 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 565fcd3a-6a1e-31ec-a24d-0e2a00a95cff | -2.9173 | -54.122501 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ac13e2-6c5e-309c-9bd4-5f0c8e17ada8 | -3.0911 | -57.641602 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9806a98b-7d5c-3a39-ad55-7dcaba5b963e | -3.0961 | -54.183899 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56f23b2-afb4-343d-aa60-7f0665c410d8 | -3.3849 | -58.206001 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95052a9d-f273-38f6-a2ba-bd24688e25d0 | -6.4413 | -55.0116 | 2026-10-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd83191c-c8c1-310b-ae29-6f2dc0ed7d79 | -3.0356 | -53.924801 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6dafce6-86fa-326f-98a2-54dd490bff50 | -3.7285 | -55.976002 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b898fb-a2a4-3e93-9383-1f636fb7cb14 | -3.1676 | -50.532799 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8b8f4e-916e-386f-8f25-0ce2d8544631 | -9.1551 | -65.9384 | 2026-10-07 00:47:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba3071d-41f4-33bc-a794-67aa0bbe0d7c | -2.9368 | -54.118 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d3ac72b-ab42-3f4e-b3b8-b04203f91437 | -4.3702 | -54.748699 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0174cc0-8f0d-33fa-ba66-a4ef59e3388a | -3.0915 | -59.182598 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8093dc67-37d0-33f0-8d95-61c3f3a5a1f0 | -2.9907 | -54.0406 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18896bd0-9a40-31d3-b52d-cae9bcd2bd63 | -3.5853 | -54.561798 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 947c7693-0a9f-3305-996e-b4faabef10ce | -3.0141 | -53.8764 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31d71851-8a7b-323e-bcd8-aeb53877302f | -3.1242 | -53.688099 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e833d09-7813-3d7e-ab10-d02a01c9a818 | -3.4858 | -54.620201 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
