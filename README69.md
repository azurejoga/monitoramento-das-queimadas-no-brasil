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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f4d161c-17f0-3981-82b1-790c453311b3 | -2.8608 | -51.7731 | 2024-11-06 06:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| cc8fc527-a83e-32ff-8b14-74e79d8ce17e | -2.7243 | -54.1552 | 2024-11-06 06:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 68769a05-6489-339f-b314-fa40157f6857 | -2.9371 | -51.0465 | 2024-11-06 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| bf50eda0-071d-3d88-bfc5-60c7bda60c0c | -3.967 | -48.15 | 2024-11-06 06:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| c0b7f06d-0501-3dfd-8bf4-d31bfa9f03f5 | -3.0213 | -53.2607 | 2024-11-06 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 24cc3355-2574-31ff-8dae-b8cede84ab27 | -3.0397 | -53.2603 | 2024-11-06 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 940f0ad8-6c8e-3878-8288-9518a29c1845 | -2.8506 | -49.4744 | 2024-11-06 06:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a7004c78-4677-3cc9-a231-c4cbee7156e2 | -3.1617 | -50.2038 | 2024-11-06 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 75b94bca-2ab6-3734-bf5e-200a36fc45e2 | -4.1246 | -43.5833 | 2024-11-06 06:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 03d9c2e3-102a-308b-b4eb-1cd261985aa1 | -2.7244 | -54.1351 | 2024-11-06 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8d8a0d78-9293-3c0c-bc90-180ef0537528 | -2.9186 | -51.047 | 2024-11-06 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| a6ce2525-e8ff-3db3-ab7b-9e83a026b0e9 | -2.7243 | -54.1552 | 2024-11-06 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 531ad855-0c68-3e8b-b825-c8cf92dedf5d | -3.2163 | -50.391 | 2024-11-06 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| fb5b60e6-1ebb-334f-b8ca-f36ce6fdbbe2 | -3.0397 | -53.2603 | 2024-11-06 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4b6da5dc-614f-3785-bcaf-4f34020bc0f6 | -3.1617 | -50.2038 | 2024-11-06 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 849fcef4-519a-3e27-9807-b514b99c6dd2 | -3.0207 | -53.443 | 2024-11-06 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0a94e792-d5ce-3bd4-a70a-db75c31ae5cd | -2.8608 | -51.7731 | 2024-11-06 06:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 31c1a349-545c-381f-b74f-749bd0af5bc1 | -3.0396 | -53.2805 | 2024-11-06 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 06910d97-7583-36dd-b3c2-3138e22c8b8e | -2.8506 | -49.4744 | 2024-11-06 06:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| d7394494-0acd-3a7c-83f9-cc89f0200846 | -2.8423 | -51.7735 | 2024-11-06 06:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2e265488-14e5-394b-9b44-4e876a920643 | -2.9371 | -51.0465 | 2024-11-06 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| fa03e034-691c-3d8d-a376-e2764ae5c0a8 | -2.706 | -54.1556 | 2024-11-06 06:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6f8ddde4-8258-31be-8a31-ff1a0a7b8db2 | -2.4457 | -49.039 | 2024-11-06 06:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 87d5c2dd-f8e7-3140-955a-a47a71c4bf57 | -3.0207 | -53.4227 | 2024-11-06 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b74daaba-5083-35dc-b9c3-2a9297a717a2 | -2.7244 | -54.1351 | 2024-11-06 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a4265197-64bc-3a15-a013-cebbc7e54284 | -2.8608 | -51.7731 | 2024-11-06 06:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bd0d0ed8-0812-3f32-923b-322c0def2c42 | -2.9186 | -51.047 | 2024-11-06 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c34144b4-79a6-3200-abef-99fe7bb48eda | -2.8202 | -52.9002 | 2024-11-06 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fa476278-3f98-3d95-ad75-208a26114cd3 | -2.8384 | -52.9405 | 2024-11-06 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| fdc966c6-5463-3e5e-8260-cf7e93ce2cef | -2.8201 | -52.9206 | 2024-11-06 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 4ae13c35-9200-3dd6-a9a8-a69202cbe295 | -2.8385 | -52.9201 | 2024-11-06 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| af6d0a0d-77b7-35ef-87fd-5a31337c3461 | -2.7243 | -54.1552 | 2024-11-06 06:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 1ae19baf-39f8-3bc5-a3a2-6670a3998ea7 | -2.8506 | -49.4744 | 2024-11-06 06:50:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b24061dd-b8fa-3ff0-bbd6-cf6afe6dbffb | -2.8386 | -52.8998 | 2024-11-06 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 696f335f-6f21-344d-a747-0269d298872c | -2.82 | -52.9409 | 2024-11-06 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 6942a7cc-65df-3b6f-85b6-46da6dc074ed | -2.8423 | -51.7735 | 2024-11-06 06:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a493da99-7e3c-33ec-bc91-b79d953a2bce | -2.4457 | -49.039 | 2024-11-06 06:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| d4bd00d2-c49e-3358-9823-838cd3029437 | -2.9371 | -51.0465 | 2024-11-06 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c6cdb904-f22b-31c5-8fc3-433cce453c53 | -9.44736 | -68.52814 | 2024-11-06 06:52:00 | AQUA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83afb543-a546-3f1b-b4d5-10a49bd751e2 | -2.7243 | -54.1552 | 2024-11-06 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 8f59d9c6-9ae1-31ce-80c0-a8180fb4dee5 | -2.7244 | -54.1351 | 2024-11-06 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 86423512-9ef0-3eea-8da8-7ec74e601720 | -2.8506 | -49.4744 | 2024-11-06 07:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 32240055-f12f-3bc3-9495-0212e0dd9437 | -23.9306 | -54.0564 | 2024-11-06 08:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| 8adceac3-4594-3d25-93de-3db67982f3b9 | -23.93 | -54.0787 | 2024-11-06 08:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 9f6d4663-02cd-30cd-9cdc-8de7ea4a1cb3 | -6.12 | -43.95 | 2024-11-06 11:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5856af-d6f5-3f76-9f36-13f14da77dcf | -2.4458 | -49.0176 | 2024-11-06 11:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 01d383fc-2ff3-3fe0-bb85-5d01c4701b51 | -2.4457 | -49.039 | 2024-11-06 11:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 178.7 |
| f4a1cc33-94cd-39b1-9e8a-2e823d170906 | -2.4457 | -49.039 | 2024-11-06 12:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 204.9 |
| 5e0e25ff-dd06-393d-8f77-55a7f6ad1258 | -2.4458 | -49.0176 | 2024-11-06 12:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| fc9ddbbf-317d-3842-b6cc-a5b8976977bf | -2.4457 | -49.039 | 2024-11-06 12:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| dc92fff6-c975-39fe-bc79-91c4753c4576 | -2.4458 | -49.0176 | 2024-11-06 12:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 6530cd8f-8fe1-339b-ad9f-a8ffc83da85c | -2.4458 | -49.0176 | 2024-11-06 12:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 4481764e-aee1-3cfa-b3e7-1881307e0900 | -2.4457 | -49.039 | 2024-11-06 12:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 8523cc4a-a3e9-3c2e-83b7-5422171aadfc | -2.4458 | -49.0176 | 2024-11-06 12:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 3dbd2a60-194a-3096-955d-49a578f7cedf | -2.8385 | -52.9201 | 2024-11-06 12:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| e26060f4-893e-3550-a32f-c1238e8d3323 | -2.8202 | -52.9002 | 2024-11-06 12:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 4741cfbc-1824-3ab9-a2c0-780c6da04b5e | -2.8201 | -52.9206 | 2024-11-06 12:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 8e835888-3cf5-3d78-940d-756b5136146b | -2.8386 | -52.8998 | 2024-11-06 12:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 308.7 |
| 78dad25d-35e6-363d-8f3d-f83d97a69690 | -2.4457 | -49.039 | 2024-11-06 12:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| adb73913-72fe-3dd3-a333-440bdf48b3af | -2.82 | -52.9409 | 2024-11-06 12:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| b294c4ed-8507-3ffe-81f3-aa3c4af1861f | 3.6102 | -51.31629 | 2024-11-06 12:38:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 62372efd-fb22-326c-8287-3bdb4c130950 | 3.49553 | -51.24906 | 2024-11-06 12:38:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 0e454355-771a-32c9-a5e6-e5002340788c | -2.4458 | -49.0176 | 2024-11-06 12:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 210cc89d-bdd6-3fff-a68f-b3d19622b0df | -2.4457 | -49.039 | 2024-11-06 12:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 9e11bc05-ad83-30b7-8cb6-cc1a744181b9 | -2.8386 | -52.8998 | 2024-11-06 12:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 320.5 |
| 1d45d8b7-f360-3c2e-b994-f1f7bca0454b | -2.8385 | -52.9201 | 2024-11-06 12:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 59e4b62b-7671-3599-af75-4c9399903629 | -2.7243 | -54.1552 | 2024-11-06 12:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 195.7 |
| b8e5d22f-375f-307d-8afe-3395ee5af3bd | -2.6764 | -51.8189 | 2024-11-06 12:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| dd15d313-2eb2-3470-9ddf-9350f0d04cf5 | -2.8202 | -52.9002 | 2024-11-06 12:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| ccab9c73-8012-33d1-b642-91fa49604d8e | -2.82 | -52.9409 | 2024-11-06 12:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 5187f516-583e-37cd-9ef1-37a937bd72a9 | -2.8201 | -52.9206 | 2024-11-06 12:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 175.8 |
| bfc6dd89-07a3-33dd-a559-57a994bf0218 | -7.58798 | -37.91739 | 2024-11-06 12:40:00 | TERRA_M-T | TAVARES | PARAÍBA | Brasil | 2516607 | 25 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 7cb98b25-f8d5-39c3-b882-38e2564db437 | -2.92118 | -51.05088 | 2024-11-06 12:40:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2f0d415c-7a23-3e2f-b4b8-568bfb5cb7f8 | -4.19287 | -46.70096 | 2024-11-06 12:40:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 35678242-d845-31e6-a858-37a23e7639cc | -7.0929 | -41.82795 | 2024-11-06 12:40:00 | TERRA_M-T | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 9dba589a-2814-3f30-a0ad-a2fb15365741 | -8.26236 | -44.86308 | 2024-11-06 12:40:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0661e1e3-0cf1-304b-98ec-c01734f8ab99 | -3.30775 | -41.06419 | 2024-11-06 12:40:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 24941e20-8cb7-3578-bb4a-58d2834d6efc | -6.67439 | -43.38452 | 2024-11-06 12:40:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a94eae20-7979-32ca-b36e-f0f160aa58cd | -4.7337 | -48.97243 | 2024-11-06 12:40:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 9228b507-cbfe-3a79-9567-e9fcb0fd5675 | -4.53897 | -38.95589 | 2024-11-06 12:40:00 | TERRA_M-T | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 46.1 |
| f5ee32f2-dbf9-37c1-9a63-3059465f5eaf | -3.97086 | -48.16068 | 2024-11-06 12:40:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 883dad80-7d0b-3687-aea8-6ac14eecb80e | -3.8758 | -47.54924 | 2024-11-06 12:40:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d2fc1ba7-ce9c-34be-93d6-87cee9d8d55e | -3.76599 | -47.60499 | 2024-11-06 12:40:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4247d616-2d94-3a94-822a-43eef4cf9e0c | -2.50908 | -45.97566 | 2024-11-06 12:40:00 | TERRA_M-T | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 84e25b6f-e0a7-3ccb-86a1-20083b893a0d | -8.37638 | -43.63857 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c93eac99-89a7-3a3a-9c83-a7963a784508 | -3.87318 | -40.07729 | 2024-11-06 12:40:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 1600b85b-87f0-3c3c-a0b3-a9b68f890560 | -7.25188 | -48.42835 | 2024-11-06 12:40:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e40b2875-eeb0-3174-80ca-7c122214d5f3 | -2.95283 | -48.61346 | 2024-11-06 12:40:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 64e3a876-5d17-3f8e-a28c-9255fff29239 | -8.38642 | -43.6398 | 2024-11-06 12:40:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4cd76a67-edc7-3b43-9d4a-a32817aa150f | -2.32094 | -48.86823 | 2024-11-06 12:40:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 0d894a5f-4eb1-3e44-b85c-85fccefda178 | -3.80002 | -42.37514 | 2024-11-06 12:40:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 1e463caf-59f7-36ab-9e62-fbf174e37f1a | -7.49352 | -39.57357 | 2024-11-06 12:40:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 38.7 |
| bc968f8e-4485-3ca8-96bb-e79325f32bb2 | -4.85725 | -44.91011 | 2024-11-06 12:40:00 | TERRA_M-T | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c6647826-4c69-30f7-a0c0-ed3c71aa4520 | -8.09225 | -44.44126 | 2024-11-06 12:40:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6508491a-4667-3df1-9846-4688963d871f | -3.82442 | -44.1408 | 2024-11-06 12:40:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f0b70e1e-a271-32e7-a780-afea187f59fb | -4.78084 | -45.94965 | 2024-11-06 12:40:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 91b0e9c0-0aac-3df3-a6c2-b5973b51e173 | -3.17477 | -46.59859 | 2024-11-06 12:40:00 | TERRA_M-T | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| eb3cc95d-caa6-3f99-9f26-ca8628617212 | -4.4169 | -47.25541 | 2024-11-06 12:40:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 05498379-b863-3bec-82d9-b69cfc7ac94d | -3.54347 | -50.2874 | 2024-11-06 12:40:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4bed74f3-53a6-3300-9e18-97aafc8ef108 | -3.31081 | -43.35819 | 2024-11-06 12:40:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |


[Clique aqui para ver as próximas entradas](README70.md)
