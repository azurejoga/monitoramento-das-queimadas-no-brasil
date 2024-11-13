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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 400ab41d-5b1f-35bf-8621-7eecabd7bf96 | -2.71241 | -57.3483 | 2024-11-13 05:46:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e56ae3e2-d69b-35e7-8021-dbb0fecc0eb7 | -3.33317 | -56.95625 | 2024-11-13 05:46:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ac6653a-379e-3e6d-8582-54f7d0eb754e | -2.98767 | -53.97991 | 2024-11-13 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7432a5d4-81d1-36ab-a5fb-2c07b4d2ba13 | -4.16354 | -59.91116 | 2024-11-13 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d52523b-dff8-36fc-aac9-a3f9a46d0021 | -3.61659 | -54.79468 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65438a93-1f3c-33f2-b112-962adc1d6be8 | -3.52438 | -54.48357 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43ccc51a-a9c9-3e55-b934-9933b3eaa826 | -2.76584 | -54.73868 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36122f70-3dae-3ce5-8a79-5e9aca30e4fd | -3.66214 | -54.6611 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f405c9e-4643-346d-b4cf-7a160a0a166c | -2.77331 | -54.73414 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27752584-edd3-36a8-9510-91fa031ad0ea | -2.24558 | -53.74648 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5c68bb4b-5dfb-3d13-9421-c8c5ef2bbaef | -3.25883 | -54.53656 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d191b0c8-69c2-3a5f-b1dd-7215e73c4359 | -3.14669 | -54.48669 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2cb363a2-87dd-3053-8106-19d677294e41 | -2.98704 | -53.98407 | 2024-11-13 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43780182-a74a-301a-8040-d73aad46a3f8 | -2.39951 | -53.73652 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98eb042e-9afa-39d5-9912-d135fd16dd48 | -2.39051 | -53.66911 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b9138b8-ae5a-3acf-a12e-b62a91b296dd | -1.50975 | -55.88195 | 2024-11-13 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c58ea1b4-1606-3385-b46f-990bb55cef52 | -2.62624 | -54.27773 | 2024-11-13 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2810d34f-d777-37c5-aa26-ec098e57378d | -3.62275 | -54.79597 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d203bcae-67a0-38ce-b2c4-b115c05efdf6 | -3.25955 | -54.53158 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4934d615-1437-34d1-8a96-a6eba8aa4f2b | -2.24393 | -53.75735 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1117d83c-3018-3f78-b239-81a2b5d44caa | -1.57598 | -53.73751 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 326b8f86-2173-3227-93ca-18802a73d968 | -3.14305 | -54.4893 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e212fef7-2034-3b69-ac09-16311385b84a | -3.73105 | -54.43529 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f532d92-563f-375c-8b6a-40842e7ca5de | -3.14934 | -54.49031 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aa2109c-d819-3cca-b464-84b2c4f2068e | -2.62698 | -54.27262 | 2024-11-13 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea7ad0e8-fd7d-3e25-bc78-e3509ba3bdfe | -3.10688 | -54.29823 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 519463e2-aa1d-380f-8087-d1f7394a92d9 | -3.5292 | -54.49476 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2657bd06-be8f-3639-a353-e72addf00e23 | -2.77255 | -54.73914 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f96c8fdd-7276-37a2-bc08-4863f4ea46ec | -1.88622 | -54.20255 | 2024-11-13 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d74a6bd-70a4-3df2-ac6f-1f73f50a31af | -2.39299 | -53.73541 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2652a210-5abc-3921-b3c4-7f343cfa2540 | -3.12644 | -59.01887 | 2024-11-13 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8846400f-5c46-3a30-9e81-4a2782f03016 | -3.14379 | -54.48442 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69634f1d-5c87-3202-8e8a-95dcdf7fd805 | -2.4 | -53.73818 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d403604-d9aa-3172-a30f-838808e2bc26 | -3.10614 | -54.30325 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84fbb72d-0f4f-3bc4-bc15-4cc8d3b66444 | -2.62379 | -54.27449 | 2024-11-13 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a24312fe-7b56-3a81-bb08-7f2e4a4b6b7b | -3.53551 | -54.49582 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 365b4fcc-5f5a-398d-b86e-cab3552800b9 | -3.2556 | -54.53296 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ea1b5bc-8648-31ec-a447-b452c04efc23 | -1.76522 | -55.61552 | 2024-11-13 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de69ddf5-d440-38b9-9dd6-32eada5bb7ab | -2.20655 | -53.74043 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bbaf52f-332f-3232-98dc-d4e72e214581 | -3.52363 | -54.48868 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db681a2d-9c84-35c4-b0a3-51721abc03dc | -3.62096 | -54.79864 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80a7ffe9-67d2-36c0-a521-ceaba75bb2e2 | -3.25485 | -54.5379 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15ff4582-051f-3bce-a76a-0c0ae287f438 | -2.76715 | -54.73315 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5730e103-3899-3d31-9a48-727d0f9f80a6 | -2.76639 | -54.73818 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52146651-306e-377e-851e-9c64850d35c6 | -1.88886 | -54.20652 | 2024-11-13 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5eaae30-a1c9-39f7-827c-ad1c21a63a60 | -1.88548 | -54.20754 | 2024-11-13 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb5291a6-fdbf-35a3-86e8-bbc6ccf82af9 | -3.25258 | -54.5354 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bafb1325-0b97-3a57-a375-83ff38621667 | -3.09829 | -54.31239 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07ace80f-c974-3b71-97d0-342f30f9a6b7 | -2.25126 | -53.7529 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bd50b8e-f99a-3d1e-97ee-394314e169b1 | -2.71287 | -57.34518 | 2024-11-13 05:46:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaa3b12d-226f-301d-946f-b970a83e7357 | -2.38957 | -53.66724 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 839dd95e-8e1e-3022-b6c8-6d2b26877f99 | -2.39349 | -53.73711 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 378046fb-c36a-38f4-9723-18daac3cc719 | -2.21148 | -53.75201 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee698773-ac73-3020-a131-4efb9eccce53 | -2.38968 | -53.67453 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffbb5bea-7ad8-38e1-a466-1e933724517e | -2.76656 | -54.73367 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 958b335b-a43a-3f18-9dca-320c9445dd93 | -2.98785 | -53.97869 | 2024-11-13 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 142cf38b-0e1d-354d-804d-c13bc812568b | -1.51033 | -55.87822 | 2024-11-13 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 783c076c-11af-3ddb-a7b6-1e99334f45cd | -3.58066 | -54.64858 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 327ebca7-d05b-3b85-878f-bd4d2200fbe1 | -1.65738 | -52.54787 | 2024-11-13 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e2f65f0-7743-383d-bbaf-a89555281de8 | -3.10051 | -54.29731 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3a2cbde-5b4c-3d11-aa82-319d8604ff17 | -3.25329 | -54.53045 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85d3c27b-730e-369d-b10f-8bc61c29e16a | -2.24476 | -53.7519 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2d840170-0062-3416-a562-e890a1ab6f23 | -2.20632 | -53.7445 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8322e09-dc60-34a9-a701-305e52c2b2a0 | -2.21228 | -53.74664 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 816d4079-e7c2-3cbf-9ba2-50ea2bf5d857 | -2.25043 | -53.75839 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd997f34-2d08-3e60-bc38-2922a3758b64 | -1.65837 | -52.54137 | 2024-11-13 05:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73343f1d-ba4e-3c3d-a7a5-46241985a6c0 | -2.62301 | -54.27957 | 2024-11-13 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cb15e40-9415-3715-8230-26ea4a212c8d | -2.20575 | -53.74578 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54857cfa-5498-3498-b27b-7cbc00e5dd5f | -2.23829 | -53.75069 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f91dc9cd-951e-3f32-8c96-ed130034945d | -3.20137 | -59.70025 | 2024-11-13 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e8d8861-d908-30e5-9e24-0b6ef61ce771 | -1.88256 | -54.20558 | 2024-11-13 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6750a7ce-b155-3918-942f-319bb1121236 | -2.9812 | -53.97887 | 2024-11-13 05:46:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52281069-36f7-310f-8861-d2823bde5a00 | -2.772 | -54.73969 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b3363b9-674a-36bb-8d0c-1d2f07e06a9e | -2.20548 | -53.74987 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43eab6f6-a989-30b9-b326-a96dd1726881 | -3.53626 | -54.49072 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 876d7f46-3b32-3030-9228-40977c4709c0 | -3.09976 | -54.30239 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68cc4f2c-d4c9-387b-ae9d-84371efa78e4 | -1.76585 | -55.61145 | 2024-11-13 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95024672-d58f-39af-a44e-f3e2dc0de56e | -4.16422 | -59.90672 | 2024-11-13 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 745906bc-fe47-3858-87d3-1b6fd2b3eca4 | -3.66003 | -54.65898 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a52d794-8d80-3452-b0ba-6e6098cfb324 | -2.38878 | -53.67266 | 2024-11-13 05:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a157110-d922-38ed-b303-5a07989240d0 | -3.1501 | -54.48532 | 2024-11-13 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3658610-549b-32cb-a9da-82a893d04c31 | -4.16274 | -59.90969 | 2024-11-13 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1cc68910-2f1b-3c70-a654-0eee25ef26d3 | -3.57437 | -54.64776 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e6583eb-df8b-3606-8aba-1b62790f4ff2 | -2.61991 | -54.27676 | 2024-11-13 05:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbb92fdf-cd98-3a36-bd41-c7cf1944e76e | -3.52994 | -54.48973 | 2024-11-13 05:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87aadd0b-df26-334b-88f6-159884f75e78 | -9.6055 | -63.22116 | 2024-11-13 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe7818dc-a3b1-3859-be7e-126b08b77adf | -3.0721 | -45.2532 | 2024-11-13 05:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0a81c60c-3332-3ef0-82ac-048c941ba3bf | -3.0535 | -45.2539 | 2024-11-13 05:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b71f4d92-2174-3842-9ff4-54afef06fa33 | -4.6767 | -47.4206 | 2024-11-13 05:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6aab1efd-2f8e-32c9-a7aa-5c22712ea099 | -3.072 | -45.2757 | 2024-11-13 05:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5a570bd9-23e4-3c3b-930f-b02d438edec9 | -4.6581 | -47.4216 | 2024-11-13 05:50:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| af88df42-04a4-3213-b8d3-7d87b82fb7a4 | -3.0504 | -50.3332 | 2024-11-13 05:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4a710815-3288-397a-924e-f488d7405a42 | -4.6581 | -47.4216 | 2024-11-13 06:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 94e57da4-2311-323a-8cfe-11814154ecc4 | -3.9483 | -48.1724 | 2024-11-13 06:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| aa326603-a7f6-32cc-887d-90209a243235 | -3.0689 | -50.3326 | 2024-11-13 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| af440f97-9376-3f5c-8302-8b4d4c6810c9 | -3.0535 | -45.2539 | 2024-11-13 06:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| df3e79f9-78f8-3919-9446-f4512f29f858 | -3.0504 | -50.3332 | 2024-11-13 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 753e69a5-484f-35a2-94ba-6a4ac3936be2 | -4.0913 | -49.1323 | 2024-11-13 06:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 62a2afd2-7df5-3e10-a5de-49f21488e93a | -3.0534 | -45.2764 | 2024-11-13 06:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 136bfb76-5d59-3255-a657-9d680c748ac2 | -4.6581 | -47.4216 | 2024-11-13 06:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |


[Clique aqui para ver as próximas entradas](README52.md)
