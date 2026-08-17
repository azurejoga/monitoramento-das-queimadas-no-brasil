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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24a25e17-0ae8-3fc1-8821-39057fffe89b | -11.91246 | -47.34829 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3492262f-b4bb-348d-8aae-88028d18ee57 | -8.52372 | -54.90596 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3cd20119-2a5f-3236-81a7-95c2b8b934ca | -8.58526 | -54.69312 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2a6a2be6-af75-35bb-ad62-082f6c848db7 | -13.26068 | -51.65622 | 2026-08-17 04:57:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee953ed9-9ebe-38a3-a837-183918b2ac7f | -6.59722 | -58.97079 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e5335b7d-9df6-3f49-8b8f-db1dd91bbcec | -8.2108 | -55.01154 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 514ad6e1-e4cd-3f3e-8168-ed5930f4af89 | -8.60544 | -54.70506 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa09db0a-553b-3464-ae1f-7c4e8708e9a2 | -11.20916 | -54.81392 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 909eaf40-9ade-3d92-a360-80014ed48ab2 | -14.47848 | -45.6836 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1be90c07-8f67-30c7-8459-5fdad7b44c96 | -8.52221 | -54.89276 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71c078e5-4084-34fd-9981-645e40e3a630 | -10.04495 | -62.45362 | 2026-08-17 04:57:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a7c2bd-bb54-3670-95c3-28f07c476fda | -10.1892 | -46.40738 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd43a301-8cb7-35d9-a09a-96ac8474e479 | -6.69092 | -59.06574 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b730b7d-8265-3979-baba-95294d7d5ac2 | -12.38294 | -46.44708 | 2026-08-17 04:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bd980d6-e64c-3647-bd9f-44ac100cad06 | -7.3847 | -55.49194 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63474b9a-ae7a-3915-82e0-2f132535bbe0 | -10.50609 | -50.00613 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aaba5b8-967c-311b-a3fc-fe653dd7a3dd | -8.90311 | -60.60089 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ce8df2b-f7eb-32f2-b52e-8603d51436d4 | -14.40744 | -53.00076 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97e102d8-eef0-36b8-91e7-f1e2713ef89f | -6.83123 | -56.45985 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53045421-a4f3-32bd-bf03-16bdde365cb9 | -10.50436 | -50.01756 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2c9d1173-f6aa-3e32-9e4b-6568213a1932 | -12.01895 | -46.49984 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a66a3f7-d1b3-3a0d-80a4-77e082e8e202 | -14.44358 | -51.83511 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 94d17804-96be-3dbf-a647-d2622f5aae8e | -11.39759 | -46.40038 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3428f948-ea9a-3545-bef7-fac074bd4a6b | -8.97227 | -60.51604 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea07f551-f8f8-3445-a0b1-431f6cfd176b | -11.24198 | -54.01496 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1101a3-cee7-3ddf-b3b7-94c03588a9b2 | -8.89842 | -60.56752 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 433aa824-9b34-323a-bc6b-b42cb5d91d14 | -12.90837 | -52.82973 | 2026-08-17 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9c898e1-fbca-3061-b31d-7296c9835176 | -7.06975 | -56.6511 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf01bf14-1892-310c-a68c-c0b57e63e6d5 | -14.52799 | -53.26154 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1245d1ce-017b-3fae-9229-3b4565d75702 | -8.67382 | -54.76603 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c90d9959-a7a8-323a-9255-11ddcf75e68d | -11.5377 | -46.22729 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7800329f-37eb-3318-af09-9493a7461c01 | -14.87394 | -46.64805 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ded764d2-582b-3711-9f04-88391a28a4da | -14.03267 | -53.62614 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 925fae1f-cb7d-3d9a-a912-a737113c5488 | -11.97851 | -46.44366 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4787b00-bc8b-3d80-95b6-57ad95f1ab2f | -11.70869 | -54.59354 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c41213-755a-33e8-99b9-e6f093b70b6f | -10.27595 | -48.28444 | 2026-08-17 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1adc44eb-1bfb-3767-b8d7-5913880994c8 | -8.97113 | -60.52227 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| feb99748-4166-3648-877b-6344e05c002b | -11.4959 | -46.58451 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b64d8bd5-39c7-3a24-bc9a-5260164378fa | -11.61759 | -47.79199 | 2026-08-17 04:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e84d0efd-b510-313f-9712-57432acc3712 | -10.05596 | -62.45806 | 2026-08-17 04:57:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1f392d1-69a9-31be-8cab-78e699450cb5 | -12.17851 | -45.15051 | 2026-08-17 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01a6da3a-5de9-37c9-97d7-2e310707fccc | -6.6147 | -58.97112 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35b7c274-7e5b-3624-a942-868a310c5665 | -8.96135 | -60.51725 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbd8bfb8-164c-3950-ae6c-f06dc130a70d | -12.75204 | -48.42519 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9dd2cf3-efdd-3c04-a9bf-db95f2c2bed4 | -6.98477 | -59.03334 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7115a07f-d1f4-3eb2-b373-51e15e67b35b | -6.72091 | -58.93929 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0346ca80-7631-3cca-b073-9aa72f4a6e13 | -12.13287 | -57.20886 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3054130c-a517-35bd-9877-3506cc49b549 | -10.79241 | -50.32692 | 2026-08-17 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0270718a-54de-3a2e-b11b-f8ccf8d10f3d | -14.41664 | -53.07173 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30895882-96c4-3a4a-8ab8-699135f54db5 | -14.27513 | -53.13189 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eaa88b0-5840-319d-b838-02755066a7f0 | -6.70739 | -58.93134 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32cbad4a-682a-32fe-8ad7-4699982050da | -11.44789 | -46.59002 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 053b75a8-c74f-3072-8298-ded9bfa97050 | -11.71869 | -54.61903 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae83c14e-9d6c-3bad-aa08-7cc9d241392f | -6.62957 | -59.07146 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e44cc5a-bc50-34bf-9047-c4e5e5840e72 | -12.33108 | -47.25119 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 515030a5-02b9-34b2-98cc-d4bb6a5712ca | -10.51989 | -45.30706 | 2026-08-17 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51f788f8-e622-3f94-853a-276e19acb0d8 | -6.82529 | -56.45221 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b97247e7-72e9-3325-8da1-d143e0b65b18 | -8.52727 | -54.88483 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 033d740d-6dde-3d8f-ad9e-ef0cb3027f81 | -7.56208 | -60.85765 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb6bdf73-a806-38fd-bb2e-0f2b609eef79 | -8.63982 | -54.72604 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9351d8a3-55d8-3c89-b0d3-9d4e513bcb79 | -12.67783 | -48.51766 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a5d73b9e-4f91-366e-b721-3f8c33548e9b | -6.97321 | -59.04234 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ddf2e4-7f25-3d1e-9e7c-4d12db07be55 | -6.59435 | -58.9732 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7b207ac2-def1-362b-ac57-daed64c2d194 | -6.96293 | -59.30413 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ef9569b-c504-35de-a926-cc979ae42789 | -6.65729 | -58.97045 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 34ba42d3-fe54-356a-bc65-c06bdec9a1a9 | -12.5507 | -47.86705 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43d43997-f14e-3fb0-b46b-73f05eb3f3ed | -6.9693 | -59.03614 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa392560-322c-3c2b-a792-3e07b599bfc5 | -12.68544 | -48.51878 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6be9542-d54f-3a57-adcb-f48dd65b4a01 | -14.03325 | -53.62255 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f0e936f-f956-35b7-9183-942cf2a71629 | -11.88126 | -50.22542 | 2026-08-17 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc34a1bd-49d5-37f3-b806-507f718064b6 | -13.51714 | -46.28488 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d5ac406-6dfc-3702-b385-80a0024a086b | -8.97515 | -60.52955 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0d5cf94-c796-3cff-9aee-aec2d938f27f | -8.98431 | -60.50861 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74cc4437-20d1-3267-9719-57d3992e4bf6 | -13.44264 | -43.84679 | 2026-08-17 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d47c4dc6-8733-32f5-839e-30ef18d53753 | -11.80975 | -51.77494 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5ec07bf-3ff1-377a-b205-c9659eef129c | -9.481 | -51.62981 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 645b4ca1-7abc-3edf-bc56-f77847e910b9 | -6.65824 | -58.96501 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 48cadfe5-3e95-37a0-9c3e-882d671c9028 | -8.63262 | -54.72489 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a6992a-50bf-3370-8c2e-778254e15385 | -10.47169 | -50.37043 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c2767d5-823f-377f-8c8b-8725ac9b412e | -6.70457 | -58.94701 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 34cdebc5-90a1-364e-919e-800085912e53 | -8.90367 | -60.59777 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 03b3c18e-6b78-3118-bc9b-f025540e9354 | -12.69821 | -48.51104 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5005f35d-ae8f-38bf-8100-6e74e6afb803 | -14.30897 | -47.19846 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 490b3415-bb26-3d68-a1ef-711cc4eb2794 | -8.89948 | -60.56121 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cdb268b7-bf53-396a-8f47-9b23a44d591d | -6.82305 | -56.45856 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94662c5f-4d3c-39c3-9ca4-c9e6a101acbe | -9.99631 | -51.47496 | 2026-08-17 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f64d57b8-f57d-33ab-999d-042a6cccfca3 | -12.7634 | -48.42786 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a62e2d06-60fb-3371-a39f-4850a76ab2b3 | -12.03827 | -46.48666 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 402bb0bd-d3b6-3e11-a5ce-ea14ea1c04dd | -10.38241 | -48.26631 | 2026-08-17 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed47afdd-8131-37ce-b570-286673bfe589 | -7.38392 | -55.49664 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 724f394d-d354-3fa8-b2a2-d0d2f42803e6 | -12.54208 | -47.87105 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4946e1d6-ff2f-37ac-8832-7d5dec5d7110 | -6.70073 | -58.9502 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf07bbcd-11e8-3f7a-8f21-d4de9a18dfc3 | -12.33005 | -47.25858 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4b4d3c6-9515-3edd-8114-d18686dc6a4b | -11.70264 | -54.60835 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 665cd672-928f-3ce4-8ea8-ddfb92c31355 | -10.50033 | -50.02084 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28f7a8ba-9d52-3a5c-862b-fd35f1520e15 | -8.95096 | -60.54465 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99aa598f-9997-3f65-b8b8-735903f4e8b7 | -13.50612 | -46.23061 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bd58c72b-d48c-3dbf-b750-6f2d9f80995e | -6.97508 | -59.03165 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2457587-c0e8-3eac-800e-e395d7ebcaee | -8.8979 | -60.59994 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 636453c8-9b64-3607-9960-21c46e1363f7 | -14.29942 | -47.20531 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README35.md)
