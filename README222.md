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

## Dados Diários - Página 222

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adb6891a-b170-3f95-b899-761f6c5a8ca7 | -12.59283 | -53.05779 | 2024-10-09 06:14:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 5a8d07e3-249f-32ff-8645-b3bb1de89de2 | -12.43184 | -63.02483 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| de5c4b41-7573-3c25-872a-e0cb45d25170 | -12.32546 | -59.16727 | 2024-10-09 06:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f484c93e-0fee-3850-ba85-171ee13f56c2 | -12.32412 | -59.17665 | 2024-10-09 06:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 8cf6627b-5ae1-3609-aad4-d8f6e6bb1297 | -12.31517 | -59.1783 | 2024-10-09 06:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b46fbd54-6bf6-383e-a963-fc9ed1d4f2a3 | -12.30479 | -59.18632 | 2024-10-09 06:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| caa59355-a259-393e-90f8-18ada58b0503 | -12.14362 | -63.35753 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 64d3b43f-2c38-3e0c-9a4a-34bae79ff10d | -12.14028 | -63.36279 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6519ad80-95a6-3e83-83cc-e170e6782b02 | -11.90874 | -63.27773 | 2024-10-09 06:14:00 | AQUA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 271713e1-4031-330c-96a4-cf5fbd1eef44 | -11.89895 | -63.27612 | 2024-10-09 06:14:00 | AQUA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9e19a1c9-5648-3c4d-b86a-d37e698f398a | -11.71941 | -64.99568 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c228d841-ffe8-31ec-b849-299caacaf23b | -11.71696 | -65.01025 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 33687792-6e3e-3542-9613-053db4099eed | -11.71322 | -64.9647 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| eb5898e4-5b82-36e8-ba8d-79bad9f2fb4b | -11.69805 | -64.00979 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9bb6e246-5d2c-37d6-9530-2b58e23d05c6 | -11.69598 | -64.02239 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| e36cbfbc-492e-3b8e-a342-c7a3be05f8fb | -11.69396 | -64.03473 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 18dee811-42be-3062-9df1-b892ef4386c3 | -11.68569 | -64.02048 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 24.6 |
| a2c638a4-1920-3700-8dd5-35f10da0210b | -11.68371 | -64.03249 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2bd838a5-67a4-3af5-bfb8-d3a30a3c4bb4 | -11.5827 | -58.95412 | 2024-10-09 06:14:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 78084adc-2343-3133-b61e-3bbc217aa796 | -11.5233 | -65.13237 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aa2d857b-ae13-3f2e-a132-c71066c031d7 | -11.5171 | -65.1004 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c71c42cd-6214-3178-97b5-21696edfc803 | -11.49752 | -61.97658 | 2024-10-09 06:14:00 | AQUA_M-M | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3bcd3b29-a19d-3940-b1d6-a606e908e80c | -11.44361 | -60.45275 | 2024-10-09 06:14:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ca3b8a41-7f87-376b-9450-b8193c7bf238 | -11.4136 | -60.41145 | 2024-10-09 06:14:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc8f1cdf-b8c1-32a7-b779-e81152129888 | -11.40475 | -60.41011 | 2024-10-09 06:14:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 722f4c1f-db43-334c-8e70-5b21310fed2c | -11.36258 | -60.56239 | 2024-10-09 06:14:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61da0fda-1c81-3350-9627-e7de603d84b6 | -11.36123 | -60.57138 | 2024-10-09 06:14:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fd32343e-2ecd-3f68-9145-34693fcc72cc | -11.30805 | -60.56324 | 2024-10-09 06:14:00 | AQUA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fc872744-24ec-3a03-8188-247da0d9db9b | -11.2421 | -61.17637 | 2024-10-09 06:14:00 | AQUA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d3d12d0f-c1bb-351a-8334-941f58bea33a | -10.99087 | -63.94505 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 02fa169c-e305-31c3-b916-7ae73b1c514f | -10.98875 | -63.95818 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| f54d9e0b-01c4-3173-8fec-65bf5cd4fae9 | -10.98663 | -63.97127 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 50af9096-1f56-3db7-a3f2-f8eb2a5e02b2 | -10.98455 | -63.98412 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 50362658-b763-38cc-bf0f-0333fa9c3ea7 | -10.93383 | -63.85301 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ce0e74f-207a-3dde-9599-0818e3ad03f1 | -10.93196 | -63.86463 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 691c44cc-43bb-3962-ac25-95ba950b4a69 | -10.91315 | -64.15672 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 384378d7-7ad5-3aa2-9e3b-d186dc798e09 | -10.89085 | -63.92158 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ef576a81-a537-3ed3-9457-4d223552abc5 | -10.8846 | -63.89455 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6a4a6230-be8f-318c-b3b8-92c51f9a7d66 | -10.88255 | -63.90706 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 27.3 |
| bc180319-6cd5-30db-bc09-cd4400240b07 | -10.8721 | -63.9058 | 2024-10-09 06:14:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c401c81f-9edd-3cea-b1e4-ae613c9129b6 | -10.8701 | -63.91796 | 2024-10-09 06:14:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7eac85fb-cbd9-394d-abb2-26ab5976b71e | -11.7117 | -65.0155 | 2024-10-09 06:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f305b592-ff70-3f30-85ca-48a0a9aff827 | -11.7119 | -64.9966 | 2024-10-09 06:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a244fb96-2840-34fe-a5a0-34e50a119192 | -9.99111 | -64.77699 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98482985-5bd3-3ddc-842e-edb67f145f5f | -9.99057 | -64.78133 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20dc0bde-4b3c-393d-9224-53a23640c8e5 | -9.98519 | -64.77615 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c12ad9c-1aa8-3bbd-9b59-e711221d910c | -9.98465 | -64.78051 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a428babf-c8c7-35de-9b09-699208ace714 | -9.95438 | -66.77259 | 2024-10-09 06:20:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d572e83d-83cd-3eb9-8722-851c748dc76e | -9.95398 | -66.77563 | 2024-10-09 06:20:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e377f86c-45e0-3457-9a30-0590fc32556e | -9.92268 | -65.0479 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6e0e3dc-6318-331b-a5b6-4be93a19d59f | -9.92204 | -65.04544 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df2e6cfa-a1df-3acf-8137-8684c0eb482e | -9.92154 | -65.04955 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afb47493-b914-3fdd-8754-5233035f90fe | -9.91616 | -64.77408 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 522009ea-9de6-39da-9c3c-2bc2fe05241a | -9.89731 | -64.92225 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37b1ccaa-a9a8-38b3-aa38-7b9f5be49bc6 | -9.89145 | -64.92142 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a56e6c-4196-3a13-b7d7-73a41627f48f | -9.89092 | -64.92561 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c474304a-1638-3c8f-a909-bd8a41cfe2f8 | -9.852 | -68.9964 | 2024-10-09 06:20:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d01c2e6f-78e3-3cf9-bd38-7cc0f83c0c40 | -9.80039 | -64.46191 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31c8509d-8a0e-390a-ace1-5dd35b0fede9 | -9.79983 | -64.46645 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90976e39-4fa7-3521-b7b0-9985084824c1 | -9.79897 | -64.46479 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f53fa538-572e-365f-9320-b4d156e40a2d | -9.79838 | -64.46935 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97275329-c105-3e94-9e2e-61710463a942 | -9.75126 | -62.37079 | 2024-10-09 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5cc98b0-626f-38b5-95e9-a7fd67afe2aa | -9.74054 | -65.87795 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd8568a3-16af-3700-9f37-aa37c0be6eda | -9.74007 | -65.88156 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0594c645-67f4-3e82-b9e8-dc7d139cb908 | -9.7305 | -64.89636 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06d6a538-2d41-359a-a1e1-71a617e9606a | -9.72996 | -64.90051 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4f8aa14-a1ee-36be-ba9c-d369f8224c01 | -9.72958 | -64.2332 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7a46357-b4e3-351e-a1c7-ac0e1adc0d1b | -9.72901 | -64.23788 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaebb55a-c834-30d1-897e-ad0c907ff51c | -9.72849 | -64.89793 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f30feab7-a0fd-3391-9e3f-4939fb587120 | -9.72291 | -64.23697 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f96a7336-5d2f-30ec-9413-11cc46b89a5d | -9.58582 | -65.24442 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f43cb7-7a34-3174-8708-aca8bc6e04de | -9.58417 | -65.2439 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf96d365-5385-3ef0-bbe2-d1fa57e310a4 | -9.58365 | -65.24785 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8e55417-f145-3d1f-b4e8-6aeac4131353 | -9.58313 | -65.25178 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 806b506f-d582-3a5b-ba6b-6f227fff808c | -9.5801 | -65.24361 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22923dfb-93da-3d16-a6ae-98049de23599 | -9.57961 | -65.24755 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b7e8ea3-1381-315f-ada8-c455788ff76b | -9.57912 | -65.2515 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3af3e431-d3d3-37a3-9dc3-6b841a80a632 | -9.57794 | -65.24706 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5df096cb-92c0-35a1-ab2b-5f29adbf6097 | -9.57741 | -65.251 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f72e0ee2-aca7-364b-89e3-00fdf89ad9c9 | -9.57689 | -65.25493 | 2024-10-09 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0344228-1835-389e-bb28-c694cec29a31 | -9.48733 | -67.15772 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d221d24-3cea-361a-880f-41d3121d1e04 | -9.4823 | -67.15709 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7347760d-e7a1-31fe-9f52-2a7ee537a6b8 | -9.47727 | -67.15644 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cee4733a-482c-3497-8afb-49d6847a9835 | -9.47225 | -67.1557 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d67a1e5f-e424-307f-a5a4-6f26eb18e37a | -9.44394 | -67.09837 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60abcde1-70d5-3d33-92dd-77bfccb302e2 | -9.44316 | -67.1043 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdd88917-c079-3975-a47a-774d7d0e6395 | -9.4404 | -67.09744 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 58fe10a7-630d-31e1-ae09-7f891889b504 | -9.43959 | -67.10335 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a163dcb-a821-3ff3-953d-441223eab34e | -9.43889 | -67.0977 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4eb63456-93d5-3d8e-b562-a9bad9a94fc1 | -9.43884 | -67.21558 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc8a0156-7515-31f9-bdc2-6540ee4f38de | -9.43879 | -67.10915 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 572a2f1f-040d-3a8a-ae80-86bdbd7abe5f | -9.43813 | -67.10361 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc62aef0-4715-3a08-9788-dacb31fe9513 | -9.43536 | -67.09677 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41be301b-fa7b-3778-8ee1-0acfaa493f72 | -9.43455 | -67.10265 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7005ed00-4edd-3f82-8ae3-69d5439d1759 | -9.43385 | -67.097 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1b91fee-6756-3c7a-93ba-c77d76045712 | -9.43376 | -67.10846 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d412d401-5e34-3ad0-a9ec-72f1e288edbc | -9.43309 | -67.1029 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f8947254-a56a-3edf-9a30-96d3c8a6cd05 | -9.40436 | -63.65668 | 2024-10-09 06:20:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a9a0afe-febd-3f65-9d38-b217a853803b | -9.40415 | -66.54482 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d178c6b8-7d4b-3c7d-9ad8-6b909ac61199 | -9.40402 | -66.54323 | 2024-10-09 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README223.md)
