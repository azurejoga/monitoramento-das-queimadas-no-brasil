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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e154baf-02ff-3425-a19f-a1ff0792e7e9 | -16.08621 | -51.07122 | 2025-10-04 05:33:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a175eeec-66f6-31d5-97f4-ba5b93e84fc5 | -9.71899 | -63.23203 | 2025-10-04 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbceec01-d1b7-3fd6-a43b-816850a31881 | -9.34045 | -54.52903 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a125ec65-b5b3-3528-b371-c161331209e5 | -11.96769 | -51.48074 | 2025-10-04 05:33:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42542ad0-c4f2-3cd0-983b-a23fd224ae36 | -7.8793 | -61.68327 | 2025-10-04 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e77e765f-00b7-320a-a3b1-b2e2fc6cbb8d | -14.57853 | -52.4787 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a77b9ef9-4a12-3f5d-95aa-8713bfec3fb9 | -11.12545 | -55.45543 | 2025-10-04 05:33:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92b73f67-fc09-3309-ae51-8bcb33e6446f | -9.63769 | -54.31295 | 2025-10-04 05:33:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 263ecc1b-8d73-3b9a-8edb-8359ade1ef28 | -10.12721 | -52.34866 | 2025-10-04 05:33:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ebf0967f-7782-3060-b33d-cb876db5432c | -12.36345 | -54.16978 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c86f912f-6eab-376d-84f1-067470f91046 | -15.22189 | -56.81747 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c6d7ca1-5b97-3dc2-a9fe-24c563c6f113 | -11.20517 | -54.08796 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9953dba3-7833-3463-a476-b45c5ddae8e4 | -14.58499 | -52.49615 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1308708d-afcf-3bd8-8bea-ae89d7a2a25d | -9.93347 | -50.89721 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d230848-b23a-3516-b863-814c961100e0 | -9.85725 | -60.27209 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffc4609c-de78-3387-ae64-f4b249277866 | -12.79219 | -56.96382 | 2025-10-04 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df64c6ad-02ac-319c-a56e-c473c0ef5e4b | -10.82901 | -57.20086 | 2025-10-04 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c4d5fdb-95de-3a2c-8c1b-e628d466784b | -12.9249 | -54.72848 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb545325-85db-3293-82c8-32809599ca22 | -10.63581 | -49.14657 | 2025-10-04 05:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf35e168-aa62-3009-80da-5b68ffb8f3cc | -9.33742 | -54.51356 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfa0c985-4753-3b3c-af9f-974d1000f40c | -8.54221 | -55.01801 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d8a8fc7-bbd0-3160-9a2b-99b3f4ba910f | -9.9239 | -60.19144 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b0164bd-e110-3cec-93ed-7a7bd9f8564c | -9.90615 | -63.58733 | 2025-10-04 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 989efb27-1045-3626-b988-fffd548eda8c | -8.53944 | -55.01685 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74124835-3f54-3c94-999d-49f408da6847 | -9.33621 | -54.52239 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51dcb2fd-1249-3633-84e1-123e6303c3c2 | -11.13034 | -55.45603 | 2025-10-04 05:33:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14f50b55-2195-3fb0-ad6f-2a531e26d717 | -8.61247 | -54.97387 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 500e4740-c530-376e-a888-12704ad349f3 | -13.33814 | -50.95579 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 834e5acc-7b11-3086-a72a-f2568a208b0f | -9.93202 | -50.20182 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78804667-443f-3af7-88ef-09033b17a732 | -12.38474 | -54.46081 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da934c95-d342-34be-b11f-b165056415f5 | -11.20784 | -54.08587 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f96f71a6-cc3a-3fff-880f-be7d84303afe | -11.74483 | -54.7256 | 2025-10-04 05:33:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e68d4d8-d7ad-3a60-bb1d-df7b218ecf22 | -9.90559 | -63.59086 | 2025-10-04 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee2fee4e-eb18-3254-8417-5067fa2cc4f9 | -9.083 | -59.01952 | 2025-10-04 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bdc1f69-0cf2-3e68-86c0-ebd62853b56c | -9.3453 | -54.5213 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2f6b681-2d3f-3163-b5d1-c93c83c150ba | -8.62969 | -54.9923 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc1dee78-7c7b-3303-b549-e65a605aa3db | -10.59569 | -54.34955 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 628e59fe-270e-3056-a7fd-f7c9aa890c4c | -8.6207 | -54.98584 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2189606-1c74-3aaf-8e2a-6d2c3d3286be | -9.30421 | -58.92696 | 2025-10-04 05:33:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bed316fc-f149-3e9e-a61b-874c4059be1d | -10.32887 | -50.33338 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80585594-1ab0-3741-aeba-f8385c196cb1 | -9.33196 | -54.51575 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f4612e1-5119-3913-9171-974949e0b4fb | -9.31132 | -61.84428 | 2025-10-04 05:33:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a294a202-6419-3e8e-a335-747606ab3fcb | -13.16966 | -50.89384 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f176cfab-5b59-3e1d-8f4a-ea3b5ee60e25 | -12.91964 | -54.72785 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d13290c0-a64f-34fc-859a-12d1878e1f2d | -10.60048 | -54.35355 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b0a062-6cb3-3536-81f8-10e265838ade | -12.39086 | -54.45492 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ee9430e-3cd5-3406-9d7d-9a80fec936a8 | -10.05342 | -63.32218 | 2025-10-04 05:33:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a7f441d-cc22-332c-9566-2366ab9ab622 | -13.18166 | -50.93777 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| ad496e3c-38dd-3a46-bf10-4db76a6cbaf0 | -9.92929 | -62.22124 | 2025-10-04 05:33:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2447947d-c4e7-351a-b2b1-24b31eeb162b | -9.9841 | -57.82034 | 2025-10-04 05:33:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72dbeb80-7cd1-30f5-aa03-ec1bd7cbee5d | -9.75208 | -62.2697 | 2025-10-04 05:33:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51cb8afe-cc8f-326f-a00c-a462d24e55c1 | -10.59486 | -54.3559 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5167d5d4-f98f-3642-a9cc-f9c8f6cd5ab9 | -8.50718 | -54.59991 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5310bc9-e27b-36a1-81da-9b71b9b31311 | -9.47127 | -60.37541 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c56b254c-6cd3-3449-a154-072b56c652b2 | -12.30089 | -55.13036 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61c395eb-7a3e-30ff-98d9-a262e4062926 | -15.57556 | -52.47338 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c24cac16-199e-3060-bee1-350f3186b43d | -9.57085 | -62.26334 | 2025-10-04 05:33:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bb81fc8-4470-3fc8-baf7-e72a647f2932 | -13.17704 | -50.88863 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dd59221-d9b4-353d-a03d-746f3e9d7b34 | -11.21272 | -54.98714 | 2025-10-04 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4233dbdd-670f-3956-b255-e516f80678d6 | -9.63932 | -55.13306 | 2025-10-04 05:33:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14b96086-61b7-3746-a3d0-d9a4d1081859 | -12.91357 | -54.7337 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f99c8a76-9f52-32a4-b052-1f428e268234 | -9.1449 | -62.37233 | 2025-10-04 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50226069-6c58-3fb0-bde1-112918f78fb7 | -9.34167 | -54.52016 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 65bd352b-3317-336b-921d-d2563e805d18 | -10.90001 | -56.19373 | 2025-10-04 05:33:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dff6f5c-22a9-3d3d-86a4-7e8d057b3abd | -10.12777 | -52.34431 | 2025-10-04 05:33:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8d64da0-debf-3233-844b-f417c9efd1c0 | -8.62337 | -55.00213 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8594c5c9-ba2e-3536-94d7-b7f8ad863023 | -14.75321 | -54.62883 | 2025-10-04 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2050177f-6166-3309-9fa4-cbc344ba708c | -8.62296 | -54.9697 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97fefa9c-184b-34fb-869f-2592dd0ad57c | -9.92684 | -60.19603 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eccf0d92-df52-31c9-8076-ccf5a0bf7847 | -13.17974 | -50.92515 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f6a3e962-ef3d-3bba-98cc-38103165af08 | -9.31431 | -54.53175 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bda765a-6828-3f61-a3ba-3327351192f5 | -11.2136 | -54.98659 | 2025-10-04 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 646a8ce3-f36e-39f5-a9d1-66b51526da77 | -14.74651 | -54.6389 | 2025-10-04 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbbbcfde-076e-3e4d-b7b2-538cd0c72fe7 | -9.34553 | -54.52963 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce0795be-20a6-3fe4-864d-09ebdc6c79b5 | -9.99971 | -60.01294 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbc8d2a6-cbf0-3268-b2e2-0c15f82a5000 | -9.33074 | -54.52469 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3fb544c-cafa-3da0-8a6a-f227786eb655 | -10.06101 | -59.35325 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29379e9-1fb4-3f10-9103-6f4b2627db0b | -9.32527 | -54.527 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83cab342-b0a7-3f93-93d7-fab739b435cf | -8.22085 | -55.20686 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00f4f1dc-440c-3bb7-9559-d18efcecac65 | -14.57887 | -52.49475 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2134a012-960a-3adc-a6f9-377b75e0e1ce | -12.27956 | -55.13618 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85d02746-db8f-35bf-8309-c50e2f502176 | -12.38556 | -54.45417 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a64bf1f3-fcf4-3e34-9bb9-60e81c89f6da | -14.04436 | -53.92458 | 2025-10-04 05:33:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4258169e-6d58-338e-8819-98aa257810db | -9.34673 | -54.52089 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0fb253e-036d-32a8-8425-81c495e3c7cd | -9.6363 | -63.24422 | 2025-10-04 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 933bc451-05ad-3baf-b2bc-b1f45b7d8d32 | -9.52802 | -59.38583 | 2025-10-04 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4896295-bf66-31a9-8f5c-78532ed168a0 | -15.60499 | -52.49532 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ccf44d4-d25a-3f5e-bae3-6e32ebaa3de8 | -9.45664 | -56.6571 | 2025-10-04 05:33:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1dec4f8-fc4f-3a4b-9930-09bfab378733 | -13.17622 | -50.92506 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ef46674a-9c7e-33a8-82e7-f1d35e0cd76e | -12.38433 | -54.46413 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34caa1ec-dabd-30b4-bb79-4c9781fc905f | -7.52971 | -61.48046 | 2025-10-04 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcbd5549-2fb2-3af3-844d-63b790dd20b9 | -9.92667 | -50.89715 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f7a32e6-c072-306c-9748-6cad1aff8156 | -9.92934 | -50.20143 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ca9bd7d-79b1-3fc1-ba4b-b02cd62bc9d7 | -10.33559 | -50.33424 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d6c3d83c-55e3-3664-8b51-e2e9f494f049 | -12.27992 | -55.13329 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccdfb992-f449-3c25-9f36-90b27f9f46f1 | -9.3202 | -54.52635 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de0e02a6-70d0-325c-9e7c-e313310514e7 | -9.63253 | -54.3122 | 2025-10-04 05:33:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ad0532-a095-3af7-9e2a-6a9f6a317ef2 | -15.22915 | -56.85076 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11169a87-7998-3300-bb03-25a19df53211 | -14.57939 | -52.49014 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afa52d5a-c571-3156-ba44-315a630504af | -11.1629 | -61.27878 | 2025-10-04 05:33:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README130.md)
