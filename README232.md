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

## Dados Diários - Página 232

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2f1692a-56cb-3604-b272-d143969b2972 | -2.30537 | -57.08393 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ede74ab7-2bc5-3087-b4f3-7579056f41a1 | -3.2885 | -54.05685 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 13ff80d7-7131-355f-a57c-b56a702358c6 | -3.00034 | -43.84151 | 2026-10-07 16:39:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af3b2dc4-eb86-38f4-a9df-2e1c76e72225 | 1.07307 | -56.1994 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f06c8449-d576-3156-8307-4fb968dcb68c | -2.84184 | -54.07201 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 725b3f48-e61b-3c96-bdee-d782f837f261 | -3.16191 | -54.72934 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 7fb61707-ecf5-30ac-9690-b685d30f9788 | -1.47609 | -54.495 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 917514c0-3bcf-38c2-a4db-8c25f6c6c63c | -1.47349 | -54.77127 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 78958a47-f966-31f2-a8c1-f544a7966bf4 | -4.13014 | -54.25388 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 585c008d-72f3-35fd-ba0b-bfc7d6c34d15 | -2.50253 | -56.12556 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 0a1f49b4-d850-3ab7-aea5-377438bf42c2 | -2.45468 | -46.02107 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05a94c5f-edc3-39c5-9032-bfad87a55733 | -3.84147 | -55.98018 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ba026ae8-1708-3c98-8521-bd647d979db4 | -2.05785 | -45.97495 | 2026-10-07 16:39:00 | NPP-375 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7672fca0-5580-3de4-b521-090592de977a | -0.79994 | -49.17189 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4e571ecc-8c9d-31ff-a572-5e6a590634fb | -3.24116 | -50.17561 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9df60ef6-15fa-3ef9-9f6d-cdd76ace47aa | -2.27474 | -48.75224 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cc88cbb8-342d-3067-ac22-9da1356b407d | 3.22124 | -51.29305 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 127ff0b5-dbbb-3ba3-8e17-75caff5b9344 | -3.52413 | -54.66309 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c05933d1-445a-3cf9-8ca3-196eebf8e5c8 | -1.53625 | -46.29366 | 2026-10-07 16:39:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 4ae9351a-b9de-385c-8b88-277a39f5a199 | -2.93391 | -53.9312 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e804eae3-8da3-33ae-a722-800c99b1c1bd | -2.84674 | -54.06784 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2b18b11-8ecd-3987-804b-88739ec21e5b | -3.10759 | -54.16489 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 633fab0b-2575-3c43-9c02-2f64b22efc56 | -3.10126 | -53.76289 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 15bcca74-bffc-3aff-b858-b1e27327743a | -2.93489 | -54.16603 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5af66e4d-9dd6-373e-a935-82dc1d0319ec | -3.28451 | -54.02952 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bcf76dfd-b89c-38ce-9fdc-acfb3975e123 | -3.58417 | -54.3125 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e4fc2dc3-b60d-3936-9720-f88a368ad93a | -2.7899 | -51.68267 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2f339054-073e-393c-892d-4c71c83902cd | -2.70476 | -49.0436 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dec8f46-67c5-30e5-b01e-963ccacde0f2 | -2.98285 | -54.04042 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9d1695b4-1cea-3c80-9146-ba2462e91ddd | -1.37885 | -55.19365 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bba97934-6df0-36ce-83d6-30d7a82d0ce2 | -3.09612 | -57.64738 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fa747820-8570-3683-8835-8a96308b711a | -3.51846 | -54.6638 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 40861719-4de9-3045-9b55-409594fbfdfe | -3.2282 | -54.37185 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 29f29912-515c-306d-8cf9-43a2ab573feb | -3.40358 | -58.01611 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| facddb7a-79a4-3c55-b68b-4a5a9dc2d852 | -2.80325 | -54.08411 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 856272f5-58d4-353e-820c-a1ffda4a5d7c | -3.27716 | -54.05496 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e7963fac-f816-3252-9360-fa56626c5aa4 | -3.03734 | -53.91109 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abad2035-ea48-3287-96e7-287d99141e90 | -3.99706 | -56.26403 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f6f61c9d-38ac-338d-8716-dd8e7fe5e5ae | -3.30997 | -53.86727 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 73e991f4-396f-3e2c-b3b8-757a5131a053 | -4.14626 | -54.91386 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 49ac3cc9-d4a5-3d02-bd9c-02321641ef05 | -3.09982 | -53.71143 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6d3c7e1-9687-3fc8-8096-0108033166a1 | -3.11069 | -53.78286 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| fc90e8c0-1888-3123-a65f-57e76517d2e7 | -2.7812 | -54.08383 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| d85d732d-f7c1-35f4-9dcb-bbdfb9a6514d | -2.79197 | -54.0823 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 500.7 |
| 8e629b62-1232-3162-b3f1-f47e35487e0a | -2.96727 | -54.08424 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16c1a06a-0e06-3eba-bf26-357c41e5e35d | -3.10266 | -54.2833 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| df3e3057-9f54-3ef5-ba77-8bdd1c846b6a | -2.00663 | -45.08268 | 2026-10-07 16:39:00 | NPP-375 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dc95532-8688-3b53-a5dc-421be2759425 | -2.79705 | -57.66037 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 100586bd-013e-32f0-948e-374ba346d9b8 | -3.27121 | -54.66676 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7088992f-993d-3d97-a19b-902ab93a2764 | 2.23597 | -50.82866 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c129cdaa-bddf-3054-a349-e33a2dcb8fb4 | -2.58589 | -54.61908 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4826381a-4ed9-3fa6-9049-340288c2425e | -2.44624 | -56.55152 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 65ea5cc5-b95e-3ac4-b2b4-8936bd9512be | -2.94472 | -54.11905 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| aac976f0-f354-351c-b875-fdacaa41120b | -1.14946 | -46.57124 | 2026-10-07 16:39:00 | NPP-375 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f289c0d7-8a40-3c0b-8ad3-8f24918a6683 | -3.03392 | -53.92514 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7111a389-3ffd-3270-90f2-80995021e74a | -3.03831 | -53.91773 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5a70d874-d700-37c9-ae32-9b79df332056 | -3.18377 | -57.86175 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0e534428-1666-3526-ba81-87cecfce263e | -1.58878 | -57.64068 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4159ba9c-1ef3-312c-b266-d1abd7477000 | 1.20153 | -51.28487 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b3eacd4d-0a2a-3e4a-8be5-6a0b3d606b7a | -3.6542 | -50.94692 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b7cd1edd-5c96-3708-b7bf-9b959e769726 | -2.92445 | -54.10867 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d083e7ce-6a7c-314e-aba4-fc22fc48abe1 | -3.70453 | -50.6557 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 40edcab6-1b1e-32e1-b703-ba39583d9c63 | 1.70431 | -55.62806 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d5953353-5fdc-3671-8e1f-e07950540221 | -3.28158 | -54.04731 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1f6cd119-18c0-3e36-a0f7-7d137905b1c8 | -4.06757 | -55.32553 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 66bb56c5-0b34-3790-8441-13cad60e833a | -2.46582 | -46.02661 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 88f8f2be-f97c-3814-b813-4e888bc15036 | -1.79383 | -57.11563 | 2026-10-07 16:39:00 | NPP-375 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 8fbd413e-558c-3164-aebc-890c2e2b54b9 | -3.03296 | -53.9185 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| afcaf865-58b6-3b77-ba75-f86c1b4a149b | -1.42655 | -49.11039 | 2026-10-07 16:39:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f8ca50aa-a1f2-3c58-9da6-da624a39b1c9 | -3.9464 | -56.04929 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9ece1777-cb8c-3fe7-88b9-b0a41b16c469 | -2.76218 | -54.10403 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| e72c5a46-270b-34f4-a972-178e4530caed | -4.14107 | -54.91905 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2eb60cdd-6f7a-3817-97af-9ac9cf32c7c5 | -3.52476 | -54.62837 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d3124bbf-1ea2-3788-931a-f93b89431c3f | -3.0583 | -54.24726 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec04cf01-86a2-3f30-8350-1bd709768761 | -1.42138 | -52.84792 | 2026-10-07 16:39:00 | NPP-375 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4a1c3e03-df4d-3438-ba1c-c11899e2a45c | -4.54511 | -55.61794 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f1b3d5f7-2b1f-349e-b709-81fdb01f0e39 | 2.01277 | -55.84983 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 000e1a7c-e663-352d-b314-c44abbca2c5e | -3.17987 | -50.55061 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 23ac0495-3d15-3376-910b-659308133bb8 | -2.51555 | -56.25806 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 01a46fc8-1db8-32f8-bf21-95898cbc09bf | -2.7753 | -54.08118 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 069e1b0d-e4d1-388a-87a6-896b9e1b2ee1 | -3.27617 | -54.04812 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f36f3953-89a6-3a6b-a6fa-7e68b526fbf6 | -2.75443 | -57.66844 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c2721307-18fc-3443-8ce0-e16db838c722 | -2.98566 | -54.13421 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b09c0cec-07c5-3bf1-9a19-19a9b202937f | 3.22414 | -51.30075 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b225859-6723-33db-8e28-549238aa75d9 | -1.37828 | -55.18976 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 347f6d8c-ea20-30de-987d-77e029b71c89 | -3.19377 | -50.55659 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 0cb4b6d0-9584-3a59-8389-0d6ad5038c7c | -1.83744 | -54.94512 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 50c3cb65-1143-3def-82dd-14db307e7025 | -2.94204 | -54.15177 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 0f82a067-1893-3737-a0bd-faa421d5e74e | -3.30462 | -53.86805 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| df6e83e3-38c5-3c27-8eee-e41be1ab9a00 | -3.10939 | -53.7818 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 2f036001-e2cf-34c9-adf9-568b27544c36 | -3.80763 | -51.04407 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ee4f3c55-3f20-3144-af41-2818c190a6a1 | -2.45965 | -46.03114 | 2026-10-07 16:39:00 | NPP-375 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cf6aabf-c60a-3ef2-9166-4405a01446f9 | -3.94714 | -55.71445 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2c3d68fe-d4ab-3e28-bc82-341e5e2f18d1 | 1.64351 | -55.79053 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 28c437cd-754e-3a9a-90c0-10d916b2d309 | -3.08569 | -54.28216 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| fa540b9d-318b-3b87-9961-b97349fee09d | -3.15699 | -54.08738 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a787b42a-b8fa-301f-b361-80545c8e4048 | -3.29042 | -54.0322 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 70a9842a-a1ee-3677-9c5f-f963132084ea | -4.92786 | -55.85931 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 905ce61d-9fcc-3c75-a9ef-345856f63a73 | -3.22871 | -54.37534 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| da99cfd6-4116-3689-a9dd-314df985a11e | -1.88292 | -53.97617 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README233.md)
