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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71313173-481b-3152-9900-5de66cc193c6 | -1.40582 | -52.3467 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47434e34-c588-342e-84e7-9b4cadab6a6d | -2.22824 | -53.62385 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa99499c-bb7b-33c9-90aa-b728cbf1122e | -1.62154 | -53.89027 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1570d25e-2bbe-3323-ba7c-05c1d193e852 | -1.88336 | -52.661 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce2f78f2-58e8-3250-a40b-01d173b419b4 | -3.96679 | -46.73948 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23a62146-f36a-336c-bfcc-c082012f858a | -2.2316 | -53.62438 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f55e893d-e707-3283-a72a-15d06fecc318 | -2.63503 | -55.49328 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41aba5ad-9ed3-3043-b8a1-976c7148b2e3 | -2.79838 | -54.13004 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9592866b-c33f-3a08-8b45-2335cf8be8b3 | -2.91455 | -53.07479 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb9241f1-6792-38b8-98a9-57f971b349ce | -1.06435 | -53.22415 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 510af7b1-a1b8-3397-88da-9e73377a78e1 | -1.19996 | -51.74953 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9354f04a-eeda-3182-988a-ce4c1e5071ff | -1.56582 | -51.8597 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6e0ed14-ec97-3027-8e70-dda7743ceddd | -0.27198 | -51.62374 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 570e1f34-fbc5-36dd-86c1-0cadb0f25533 | -1.32448 | -51.66845 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58f91582-fd50-3fa7-9809-4c28b5e5b367 | -2.71689 | -53.17574 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9a6aed5-e0ad-3e80-80ec-cdaa8d97a726 | -2.82867 | -48.47039 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7052108f-8ec4-3812-bb5f-318297c688e7 | -3.00042 | -50.50985 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5683215f-180a-3bfb-a835-b94f85477cfc | -1.74811 | -52.65213 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 516e491f-219f-366c-8593-c516ba43f880 | -3.74854 | -49.93597 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd191431-7ef1-3ebb-af7e-c6a793baab51 | -2.03454 | -53.49994 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baf784f4-270e-3484-9045-d8ca6035f715 | -1.24835 | -54.54385 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd57299a-d535-3d05-a2bf-b3201cdf0e1f | -1.68148 | -46.77819 | 2024-11-30 05:01:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d2067f0e-539b-39d1-be16-03bc39491539 | -1.0622 | -53.3799 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64e8c220-b951-336f-bf56-01a94f254d50 | -1.91788 | -52.88303 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b51cf3ec-4bd2-3df3-8f10-295028d7dd11 | -1.13553 | -53.39491 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d56deaa5-2aec-3903-aafa-24de77ca3bc3 | -3.12307 | -53.27852 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70e408a3-b4be-338b-9c6a-3c485bcb4e80 | -1.08934 | -51.88439 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 685aad2d-1cb2-3188-9744-77de13a36960 | -1.15964 | -53.57895 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc2f7848-862e-35a7-b861-b18840621cad | -3.09907 | -50.36281 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20e5b8d7-4e65-39c1-9b62-4f70c528e974 | 0.99051 | -50.26665 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74876819-4f6f-3333-9e14-67641a382c89 | -3.22337 | -54.18166 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1df4ab6c-8439-398a-a1a4-f377fd75053e | -3.06884 | -53.91658 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b82ba11-a642-3375-ac0c-b664ecce8daa | -2.79841 | -51.01047 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| def7236b-f882-3b01-8c46-5a0053e9a7d9 | -2.75573 | -54.08424 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb24487-461f-3c4c-ace4-b6cbe120a046 | -2.88208 | -53.94572 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaba8cef-c7e6-3472-8ebe-c28176a7baea | -2.88607 | -54.0075 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9048730f-6dd9-3f89-9285-eda6ab7a1084 | -1.25231 | -52.71828 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8b85b55-ea7e-3aec-830a-48aaf607198b | -1.6259 | -53.86233 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdd169ce-c283-3d01-8414-c5f1c6594bcc | -2.73281 | -54.0341 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c4c4e6c-330d-34eb-83be-5fe256fd712f | -3.24669 | -53.62778 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f7f48f5-b5cf-3f8c-b44f-6eecc32e6893 | -3.53231 | -53.78806 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eae3e5df-05ce-3e06-97b1-7a190a56bc4a | -3.14932 | -53.83151 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c6c7ef2-f43f-325c-947d-05a07d3be33a | -1.22454 | -51.8025 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 686b2a7a-3cb0-32b6-b80a-ff3b2c60fa0b | -1.33398 | -54.62424 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 260b77d2-42fa-37b0-8853-2a2016e27335 | -1.5864 | -52.27953 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42d9057e-1a0f-3c23-ad06-a66b9a4afe1b | -1.36443 | -52.54139 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3147e424-4027-3b44-b0e8-c001538488a8 | -3.29569 | -53.82865 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd560d71-06e5-377a-9573-d93170b71d8e | -3.0152 | -54.10611 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31921130-5b4f-33a3-8fa8-b6cd8572024f | -2.33254 | -50.67474 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8a4be9c4-a39c-3614-9ae2-c1b3476f3778 | -1.36019 | -55.18686 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3393e79-5108-3413-a46b-3029d2a9aa43 | -2.63329 | -54.06462 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 979d1db5-9080-36ec-bc54-e8ed2d1b10aa | -2.84428 | -54.01177 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e93bdabd-abe5-3e31-a267-a46b34791ef7 | -3.32007 | -46.17125 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3c31504-bfe7-3dd2-b527-5f3a12b5ebf2 | -3.94136 | -49.76089 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 019c7826-2df0-3280-8e57-4e283db16541 | -3.02609 | -54.01446 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fe54675-4393-3a17-9555-43d608bc660c | 1.6802 | -50.6618 | 2024-11-30 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d70ae835-c01d-3ea0-b6c9-f57aef0fca7f | -2.26953 | -53.47003 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 193bb6a3-09b9-3c65-8427-d2cbfdcf886f | -3.05292 | -54.04018 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a03ce2b6-f38b-3d00-b4b2-a7f280ced98c | -3.45205 | -54.62291 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90550629-6cef-3150-a3c6-eeae6f134382 | -2.85986 | -53.99982 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdc9923d-21b8-3c13-b482-f949471152e0 | -3.05038 | -48.96253 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2a1e2ea5-8d91-3a61-84ba-d0147b2a983e | -2.60725 | -46.56584 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6729ddb7-db1f-3c70-985a-2a3e2204115e | -2.43162 | -53.88302 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc172278-bb60-3fe6-b875-f23a5b61360b | -5.58369 | -45.20383 | 2024-11-30 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6356125f-6ccd-3c3a-844c-6ca1dea453ba | -3.20228 | -51.41853 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca18276c-89f2-31f2-bd7a-b80b82a54e62 | -3.07097 | -50.5705 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9e20e02-4c2e-3034-bbb3-e76adef9133f | -1.91044 | -52.90826 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41b58d82-9ddf-37f4-a3ed-b95d68c75c76 | -3.21543 | -53.38252 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45aef9ce-541a-34f6-aec3-ac36cafefea5 | -3.09268 | -54.12934 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c721cf68-82c0-3701-9cf7-92509662eedc | -3.24438 | -53.42039 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e07b6b8-8669-34e8-b642-988d9974076b | -2.71504 | -48.60151 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf7d30ab-362a-30e4-8db4-772e03140d08 | -3.73356 | -54.22823 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0ab3580-8302-371f-82d7-b4ba5e21950c | -1.08659 | -53.63956 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f186867-75ec-36ac-ac3b-e20147dd0473 | -3.84459 | -46.52487 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cfb6fb57-c422-32f2-bd89-eaec1421c32e | -3.49919 | -53.80129 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 994a2130-55f6-3bf0-83ae-5dbc868e7b60 | -2.70769 | -51.99835 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e79e0080-b14b-344b-aa80-42375cd454e6 | -1.62486 | -52.37563 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85da9350-c7f8-3663-89c3-46dee91a0d6b | -3.34141 | -50.52306 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df237fea-97c4-3941-ad45-5d307398cad9 | -3.96391 | -50.18685 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a609882-1c8e-36b1-993f-b064a3f516b9 | -1.2 | -53.71406 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f08b0b31-05f7-34d6-a062-e1207b4be979 | -3.13879 | -55.0022 | 2024-11-30 05:01:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca56db99-2197-31f3-b9f6-460dc9928306 | -1.19853 | -53.8923 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab6aa177-bdc6-3b62-a78b-7e6a47693bb9 | -1.33759 | -54.98475 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b0b0645-9aa6-3403-9dd3-a781013a5306 | -4.04064 | -48.33311 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 790816fb-6038-3c17-97ba-073d6a91c5bf | -1.58241 | -52.25922 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b613714-a710-3612-aa9b-007e8f29f370 | -1.43853 | -54.51698 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cb85cb0-715e-3e0e-af8e-24250640aa33 | -1.35437 | -51.3778 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dd1cd78-f733-3efd-9439-dde4c41ad89d | -2.26233 | -51.23763 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03925f06-6126-3328-990e-4198d0a1cf40 | -2.27442 | -52.83777 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c888967-2f56-3a3f-9198-35206ee57ef4 | -1.73287 | -52.49963 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ac09031-e96f-3016-8aae-16cc97b2358f | 1.86958 | -55.73874 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 006e30d7-e18c-3ad2-9b1a-b69901f7a000 | -1.12392 | -54.19595 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e752454a-e53f-3f6e-b16e-ec3914ee0865 | -2.70787 | -51.97346 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c59f5aa1-8fc1-3b7b-8fad-9948ce3f60fa | -3.05172 | -53.24552 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ea925b7-f4c8-3ca6-8128-0c160263a748 | -2.3489 | -53.80926 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf64d44d-3ead-38fc-bd61-689f95f2aa9d | -1.0671 | -53.6329 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3587272-4f0e-3c14-81ca-87b9737517af | -2.58388 | -54.09623 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2abf454-e2d8-374f-9776-428f90598b86 | -1.34146 | -54.98182 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b32d4d0-9e06-3606-9a0f-206f0366cb41 | -1.15122 | -53.54521 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 124e4b13-b0fa-38e0-844b-d330506b7e38 | 1.18924 | -55.96224 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README78.md)
