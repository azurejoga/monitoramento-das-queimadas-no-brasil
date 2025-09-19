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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdbd99b3-8430-325d-b0ff-58688aa8df1d | -6.26375 | -43.90902 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8f9562f0-b102-3fed-bdd3-cc72ccc17a9b | -3.27647 | -49.15111 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 755a8d66-a15a-308b-a90e-7e0c9aa08fc2 | -1.45819 | -55.21794 | 2025-09-19 05:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b00464f6-026a-39e1-8edd-26df41f1c5cd | -4.20156 | -55.1298 | 2025-09-19 05:12:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 550c30e6-f3b2-392d-b0f3-c29ae868cd96 | -6.25772 | -43.92228 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 17c21d47-6cd1-3f1d-b6b6-97aca7f7f04b | -2.57321 | -54.65484 | 2025-09-19 05:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1897e457-75dc-3461-9f98-b0eef5d34e7f | -3.6961 | -49.57301 | 2025-09-19 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 822b586a-99f7-3cd4-8036-0a7e167703b3 | -4.94069 | -49.92236 | 2025-09-19 05:12:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db2b9d40-9d84-39e8-aef5-599b435c03c6 | -3.59558 | -55.30227 | 2025-09-19 05:12:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a665747-de65-3b00-a80b-2c88792931f9 | -3.69127 | -49.01904 | 2025-09-19 05:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99830c3e-b86b-314f-aa0a-e6a5441dab98 | -4.40945 | -47.59971 | 2025-09-19 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31cbfb35-93d0-3108-8fa7-6adeca6fb1ee | -6.26456 | -43.90282 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dcc550de-15d1-39e4-b7ac-c6ad34ebaafe | -3.59383 | -53.47252 | 2025-09-19 05:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9f7dae0-a111-35ba-810a-7a30681106c4 | -3.28203 | -49.14668 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f0ad24f-4c5d-3d79-a7f6-637e1b35e44f | -6.25589 | -43.91437 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d4d46bd6-b528-3a0e-95a2-89e54fa18a48 | -5.34274 | -46.14403 | 2025-09-19 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ff79434-bf2b-3c53-bcb0-6ae469f0c6e5 | -5.76199 | -43.39388 | 2025-09-19 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a42e25c-20c8-37ae-9017-aae0e0df0bb5 | -5.08938 | -47.51583 | 2025-09-19 05:12:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9371c8c-48f8-31da-b9f8-d1a3bdf1ef30 | -3.45382 | -53.82952 | 2025-09-19 05:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c7ac8de-03b0-32ac-9fad-588b9a97f097 | -5.46389 | -46.68238 | 2025-09-19 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 79d709c9-de15-3b16-bc1c-093c92f10692 | -6.25674 | -43.90786 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 90d8a92d-15fa-3da5-a6f6-92ba0f64593e | -4.47806 | -54.85181 | 2025-09-19 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b20d274c-9a35-3e0f-b4a1-62f61e9ed275 | -6.26562 | -43.91688 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1bb956d3-a060-3f76-a123-af82bdc9a920 | -5.34882 | -46.14478 | 2025-09-19 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 764e15d5-c10f-33c1-884e-ba55e8ed2c76 | -3.57815 | -55.54522 | 2025-09-19 05:12:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bde458d-729e-3e14-89cd-86507212f24b | -5.79991 | -45.36656 | 2025-09-19 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b068d7e-d5ec-396b-8c36-0819c1c5834a | -3.27723 | -49.14998 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21dd9fe6-04f3-332f-a8d9-ba4dfc639c2a | -5.77645 | -45.97707 | 2025-09-19 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a5151d-404a-3d92-916c-2a158fdf3ac6 | -5.63176 | -45.94802 | 2025-09-19 05:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d77ec488-6885-3559-98fe-555fb6d72f28 | -3.73855 | -49.0548 | 2025-09-19 05:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8177f033-c511-3235-b182-e93b240d71e1 | -6.26905 | -43.92311 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 40585cb0-995b-31f4-82be-cd6f8f64fef5 | -5.7942 | -45.36065 | 2025-09-19 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2cf608b-8d86-3973-a6ba-dc429dacbcac | -3.37258 | -52.79523 | 2025-09-19 05:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e707924d-b2a0-3c44-acb6-85c59e21d973 | -1.76211 | -48.05238 | 2025-09-19 05:12:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d0b913-5621-3b11-a95e-85618e357359 | -6.26292 | -43.91535 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 0e1a91c0-5997-3a40-a8fb-fbe72dc9d05c | -5.13375 | -47.82775 | 2025-09-19 05:12:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b6e4118-db91-31a7-b13c-3c4a2b83ed2f | -5.75481 | -43.39273 | 2025-09-19 05:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 631dbd00-4ea9-3afc-96a7-b71e98bb3918 | -1.75703 | -48.05165 | 2025-09-19 05:12:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a17f894-44f9-36a4-9175-0e2f9571bf9d | -3.28128 | -49.15184 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 232ea4e6-0536-38d6-9e4f-ca076598d9e5 | -5.46329 | -46.6865 | 2025-09-19 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1eeb7ca5-a41a-30cd-9308-d965bf2ce21b | -4.78955 | -50.78969 | 2025-09-19 05:12:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e09dc742-2eec-3f4b-ad7b-55df69755599 | -4.57169 | -56.25405 | 2025-09-19 05:12:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0899318-2c0c-36e6-98c4-811fe28b9add | -2.26254 | -47.88745 | 2025-09-19 05:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96dee628-9141-34fb-9d4b-8c2b68df18ff | -5.4616 | -46.68376 | 2025-09-19 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac958f01-092c-3794-a338-84c88a56c101 | -5.95962 | -47.09434 | 2025-09-19 05:12:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc15be59-1f68-3338-b9c8-40cc96b14c81 | -2.85325 | -54.89628 | 2025-09-19 05:12:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29af416c-7f05-339b-ad8d-88a6db37e26c | -6.25505 | -43.92077 | 2025-09-19 05:12:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 8b2fb471-9c72-3665-aa13-06887f76bab1 | -5.08886 | -47.51945 | 2025-09-19 05:12:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 528c1c2d-a6fb-3cef-963c-82cb589420f4 | -3.27723 | -49.14594 | 2025-09-19 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9562b18-01a3-35f2-a486-40d27021e248 | -9.17641 | -45.32265 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 089d8fa7-19b2-3e60-a6b7-88cffe463504 | -9.17045 | -45.31577 | 2025-09-19 05:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 941c3e76-617e-363c-a2cf-9e31c85807e5 | -8.03187 | -45.73875 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8601d70c-6ad7-3821-942a-eda276dc3850 | -5.54156 | -51.3723 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f400ba3-35dd-374d-b523-66d97e8198de | -10.29533 | -50.23633 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3aa0d82f-bec5-3078-aae2-2c832b3d0940 | -8.14592 | -46.78214 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03bac37d-863f-3a20-a387-3ded1e8e5e38 | -8.14043 | -46.77706 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a439181-1a5d-3848-b25a-6f99a21418b9 | -8.01634 | -45.70115 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74171ebc-1d57-3820-97e0-0dc1046126f3 | -7.87408 | -45.63435 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bd82fa8-2920-3962-bbdd-a62bfe5c698a | -12.0856 | -44.82479 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5e92991-128f-3c1d-ac51-bdd5403a97e9 | -8.0461 | -45.7301 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4617ab7-283d-3221-9d55-9435d57d7d60 | -8.13803 | -43.62888 | 2025-09-19 05:14:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89381612-a81d-3883-af13-6f5b1ed22fee | -8.68498 | -46.45465 | 2025-09-19 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bd7bb3c-c8ef-3ef3-9997-f89a56014b84 | -6.33794 | -56.18069 | 2025-09-19 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f4b5c89-6257-3068-ae49-102e01f29b0f | -7.19143 | -44.42011 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 472d5663-37e0-3a51-9210-43f30ebb5aa3 | -12.10104 | -44.84846 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 386ac61b-d52a-32b9-85b7-d8c161657e31 | -10.29687 | -50.2251 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6498d2f7-a91b-33fa-8ac3-c8a9b0f5ee0e | -12.09778 | -44.84633 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62fced2d-df38-31bf-89d2-d9c3e21bd91f | -7.33297 | -44.56957 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72dd5515-b3f1-3112-8d66-44a56674790a | -7.21704 | -44.37658 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a088103c-7dcf-343b-9a4c-85facb1f9f5c | -7.35893 | -44.58463 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 965adcb2-3788-3bce-81a3-7241baadb2ff | -10.2911 | -50.2323 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 75c5998a-cab0-390c-80d2-ced00439add6 | -8.02246 | -45.7095 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94606ed4-abc4-3efc-af92-2c913596f474 | -8.14527 | -43.63034 | 2025-09-19 05:14:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f7aa5fb-9f50-3f44-a95c-86d3eb7d267f | -8.13985 | -46.78149 | 2025-09-19 05:14:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee175a4a-845c-3da7-8701-26332ffd6487 | -8.01611 | -45.70774 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8792c004-cc65-384c-bc1f-48d3585b368a | -7.22406 | -44.3768 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ae344a6-c182-3f51-9fb9-a766c3ee97f4 | -8.37537 | -44.67653 | 2025-09-19 05:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ffb6ac83-8fc1-3206-b21b-32372a0f7f0e | -7.57653 | -45.48955 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d699470a-c444-350c-8df5-c8978d2f4201 | -10.96078 | -49.57174 | 2025-09-19 05:14:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 974da115-e135-3df8-b645-9c8b158caa5f | -7.84104 | -45.63518 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6d65a5c-82a1-31fa-b014-51f538ea56cb | -8.69186 | -46.45035 | 2025-09-19 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22b30f89-579c-39e0-8f66-e461d196dbb3 | -6.95813 | -44.76369 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4c3f433-b9a7-3358-a61c-da151bbc8978 | -10.28542 | -50.23723 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fccff9a2-2282-3b2f-bd42-d051e15733f5 | -9.94989 | -59.92479 | 2025-09-19 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7183b61-15ef-3789-9d94-4608125f062d | -6.93686 | -44.75627 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fbcb078-5b34-3df3-a0b0-43f4bfc3f674 | -6.91412 | -44.7725 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2cb08382-d537-3ba1-842d-71f1b2e3219d | -7.71913 | -61.51513 | 2025-09-19 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ab7e04d-45ab-3af3-8b18-fb8101852e4c | -6.89801 | -44.76993 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20cc4108-b391-3a31-aa7a-80716cacb1f3 | -10.28961 | -50.24126 | 2025-09-19 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 25bd2b16-054c-3ad4-8ce8-476cd98a3066 | -6.90734 | -44.77195 | 2025-09-19 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 7a8cc351-a9de-3c6a-b1f8-37dfe9e16eb4 | -7.57067 | -45.48373 | 2025-09-19 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 355b7129-f3e5-3fd2-a9f5-ed8dbc1b4793 | -8.03121 | -45.7373 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30556e7a-5aac-3e04-b0e9-a29fffb21974 | -8.37434 | -44.68324 | 2025-09-19 05:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59d376ad-086f-39c5-8592-d9062e67a029 | -7.8482 | -45.63068 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17669e65-daf7-3ae1-9ee5-a46974f91e89 | -8.03403 | -45.7163 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f879160-2026-3cd3-8d4b-9ef4a586a487 | -11.20767 | -49.63736 | 2025-09-19 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283f49e5-31e9-3a5a-a918-cc1695e3d0e5 | -8.02832 | -45.70994 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2232273e-3ab1-3aab-ab5d-b086486b2e58 | -12.08488 | -44.83158 | 2025-09-19 05:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1010b493-21db-34e4-a67b-0b82a936495d | -8.02308 | -45.7046 | 2025-09-19 05:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 399b7e7d-b16c-3b2c-9055-19ca82857155 | -7.33218 | -44.57574 | 2025-09-19 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README33.md)
