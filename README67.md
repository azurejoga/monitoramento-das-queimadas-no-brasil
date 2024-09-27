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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81acc5fe-a272-3be5-86ce-d428074ef3a7 | -22.2042 | -48.6441 | 2024-09-27 03:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| e5b1447f-d19a-3b82-80b9-5a190d253808 | -22.2049 | -48.6206 | 2024-09-27 03:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.1 |
| c33ebbee-bd98-3902-8bcc-8bffc13e06d7 | -22.225 | -48.639 | 2024-09-27 03:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 203.0 |
| f00ca633-4086-3890-8591-899801b3049d | -22.2257 | -48.6155 | 2024-09-27 03:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 390.0 |
| 676dac89-06d4-3151-a6b5-a48398b9f3e6 | -22.2264 | -48.592 | 2024-09-27 03:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.9 |
| 9a317292-aa15-3ba1-9946-0b8026ed08ce | -22.2466 | -48.6104 | 2024-09-27 03:57:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| a9209814-df17-3682-bf82-c858562b976e | -22.3873 | -48.7627 | 2024-09-27 03:57:09 | GOES-16 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.8 |
| ae97dc87-489b-30e0-84db-318ceffcea24 | -22.4082 | -48.7576 | 2024-09-27 03:57:09 | GOES-16 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 02cee3b1-3c67-3d22-a27b-6cf39d5471a7 | -22.4089 | -48.7341 | 2024-09-27 03:57:09 | GOES-16 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| 23e11d41-ac73-377f-95f0-ba49b86f3784 | -22.7433 | -44.8035 | 2024-09-27 03:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.6 |
| 31452cb3-3f19-34e1-a6dc-3e1bf755a03f | -2.8795 | -51.6695 | 2024-09-27 04:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9e87a8b0-bdb8-35d4-a73b-7d12bbb9d425 | -3.0107 | -51.0652 | 2024-09-27 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| af81ad98-360c-3a89-b1eb-d06b95398f84 | -3.0292 | -51.0647 | 2024-09-27 04:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 68a64e6c-668a-3224-8ca9-83c245f300ed | -7.4605 | -60.4114 | 2024-09-27 04:05:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 64fda83e-4c38-32c8-85b8-077b11f3033c | -7.5682 | -49.2001 | 2024-09-27 04:05:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 95.4 |
| d65f436a-76e5-3d42-85c9-c349a0547538 | -7.5684 | -49.1786 | 2024-09-27 04:05:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f4d278a1-2151-3cb6-8b57-168d7e82c522 | -7.5703 | -60.5984 | 2024-09-27 04:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4dd7d9b7-87f0-38c5-ad5c-c4ccfe94ce09 | -7.5887 | -60.5976 | 2024-09-27 04:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| bdfeedf2-9bfd-3fef-ba23-386d572dc811 | -7.5888 | -60.5785 | 2024-09-27 04:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 18e72af4-2993-394a-96bd-0689b43615c6 | -7.7885 | -61.2008 | 2024-09-27 04:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| d7de9bb3-ba4d-34cd-8459-2fe8de31b956 | -7.77 | -61.2015 | 2024-09-27 04:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f01a3608-090e-37c8-bd13-70f36b9dd9b8 | -7.7701 | -61.1825 | 2024-09-27 04:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| f546236c-3158-3255-a15b-0b1726a8df2d | -7.8156 | -54.7252 | 2024-09-27 04:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 8bfc6b74-cd5e-3429-9ab8-6193cefbeaf8 | -7.7886 | -61.1817 | 2024-09-27 04:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 5ba3529b-9b9e-39bf-84da-2fc4dc7853a2 | -8.3215 | -56.4929 | 2024-09-27 04:05:54 | GOES-16 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| bd356dd0-669d-3348-a180-d37bb151bef2 | -8.6286 | -63.1219 | 2024-09-27 04:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8e926402-a3ee-3e3f-8a5c-a7f2661422e7 | -8.8117 | -67.6732 | 2024-09-27 04:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 583a18c6-0cdb-39d4-8d98-e7c39e01b827 | -9.1032 | -61.3343 | 2024-09-27 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2e530633-dc84-3996-b510-36e6eba753dc | -9.103 | -61.3534 | 2024-09-27 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 2cedc1df-f5f3-3578-aad7-9ff6512473ce | -9.1029 | -61.3726 | 2024-09-27 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 54455974-1501-30e5-89df-dc26cd4c22e6 | -9.0163 | -67.3719 | 2024-09-27 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9952ba4a-bf46-353e-b18a-01b41cb080c8 | -8.9978 | -67.3538 | 2024-09-27 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| aa94313e-57bf-3f07-afb2-4cad1520f7a0 | -8.9978 | -67.3724 | 2024-09-27 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 226.6 |
| f37eb1f7-84c0-39ac-b728-212eb7e29d7f | -8.9977 | -67.3909 | 2024-09-27 04:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| a95e60c2-2fd8-352f-aa17-614ec2112f74 | -9.1215 | -61.3717 | 2024-09-27 04:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 87503ce8-4fa1-3030-a21d-c57c1868026d | -9.1216 | -61.3526 | 2024-09-27 04:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e529b15f-350e-3cce-a3cf-7e535817e492 | -9.1217 | -61.3334 | 2024-09-27 04:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ee33907a-2819-3b5d-b768-21a19a3ca3b8 | -9.6018 | -50.1352 | 2024-09-27 04:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| da51a17b-cf28-34f8-8ec4-2c3b9475edf2 | -9.5829 | -50.137 | 2024-09-27 04:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 1c07e7ea-7032-32c6-ac92-44170f845124 | -9.949 | -60.2334 | 2024-09-27 04:06:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 87ec8935-f7d1-3605-aa65-7146fe73745a | -10.1312 | -49.9976 | 2024-09-27 04:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 48fc853f-860c-3b36-a2bf-393fc754f7e6 | -10.1309 | -50.019 | 2024-09-27 04:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 815e78ee-a915-34d9-b58d-b7c1547f7b96 | -10.3672 | -53.7858 | 2024-09-27 04:06:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 1637cbc2-8f24-38fe-914d-9ad87e8d53f7 | -10.6639 | -45.8838 | 2024-09-27 04:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 41770f2a-44bc-349a-89fd-6c89f40b028b | -10.7214 | -51.0657 | 2024-09-27 04:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 2766a44c-87c1-3169-aed8-399c4f467ade | -10.7211 | -51.0869 | 2024-09-27 04:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 9ea8295a-5bf1-3efd-a3e5-56297354b70c | -10.9453 | -54.2676 | 2024-09-27 04:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4ca6076d-ac6b-3524-acb9-3d4952dfe9e8 | -10.9267 | -54.2488 | 2024-09-27 04:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 491233de-1966-319b-a3de-7a380111d174 | -10.9264 | -54.2692 | 2024-09-27 04:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| cacec085-82ed-3814-b328-47cc34b83871 | -11.2223 | -54.7735 | 2024-09-27 04:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 57824379-a440-38be-8c0f-71959141bced | -11.2034 | -54.7752 | 2024-09-27 04:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8ef03236-c994-3392-b186-6c97548a1353 | -12.6829 | -54.6558 | 2024-09-27 04:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 0c821360-1309-3e14-96b4-5a19781150c0 | -12.6826 | -54.6763 | 2024-09-27 04:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 031277d9-27f4-3131-a8d3-51f0d9a93652 | -12.6824 | -54.6968 | 2024-09-27 04:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 7cd3dbca-a67c-36da-be2d-4764a8661999 | -12.6636 | -54.6782 | 2024-09-27 04:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b606191b-c003-3d35-be36-0fbc3275e570 | -12.6639 | -54.6577 | 2024-09-27 04:06:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 9be37b2a-6257-3c50-a613-07d3258bd4b1 | -14.9414 | -51.448 | 2024-09-27 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| d6cf716e-6cf5-301e-9a99-2271c02afa83 | -14.941 | -51.4695 | 2024-09-27 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 79399de1-5afe-38b0-a46b-13bf8297b58c | -14.8443 | -51.4616 | 2024-09-27 04:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 51a84621-33d6-3acc-b9f0-997693526230 | -16.0993 | -51.9465 | 2024-09-27 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 84936322-2e73-3fdf-9382-bf1ae5edb999 | -16.1185 | -51.9651 | 2024-09-27 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c19818ea-a5cb-3947-a7d0-388a15067c23 | -16.1189 | -51.9436 | 2024-09-27 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3d1d04a8-a13d-36fa-9320-89220e5f2385 | -16.0985 | -51.9896 | 2024-09-27 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| dd554434-6b8b-3400-a574-99df2d303bf2 | -16.0989 | -51.968 | 2024-09-27 04:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 217.1 |
| eb16d085-dea8-3f10-9240-fc2b73247969 | -16.7325 | -55.8445 | 2024-09-27 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 346f796a-52f7-36c1-af1b-0f2065887065 | -16.856 | -47.7539 | 2024-09-27 04:06:40 | GOES-16 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3f78e5d2-d50e-313e-90d6-dd2afb617557 | -16.7329 | -55.8237 | 2024-09-27 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| f0f50627-11b7-37a4-8eb3-22a3e9acd472 | -16.8933 | -58.0213 | 2024-09-27 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| 9b35e477-240a-3374-825b-cc1e00ac5d8c | -16.893 | -58.0417 | 2024-09-27 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 4c53fee6-5df0-32ec-bca1-951e54d59cca | -16.8737 | -58.0235 | 2024-09-27 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| f8c0f7ad-646e-34bc-8122-2fd612909906 | -19.6136 | -42.8159 | 2024-09-27 04:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.7 |
| 16394a5a-0b59-3dcd-ae2b-31b939d4f030 | -19.6342 | -42.8103 | 2024-09-27 04:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 45c0e67e-6156-3991-b484-a2b12bf4a750 | -20.5199 | -41.952 | 2024-09-27 04:06:59 | GOES-16 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 6fc91acc-b5ac-3763-9952-5c2d7e7d0494 | -21.9825 | -48.4413 | 2024-09-27 04:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 80.1 |
| eb4b28a7-8722-3bd3-b615-9deb3af54194 | -21.9617 | -48.4463 | 2024-09-27 04:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dc0ab4fb-780d-3351-9a24-444262f8752e | -21.9416 | -48.4279 | 2024-09-27 04:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 3cb4c022-502e-36f4-8838-b7aa237a0061 | -21.9409 | -48.4514 | 2024-09-27 04:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 56c48b32-23a5-3d7e-a4fd-84080285f60a | -22.2891 | -48.5766 | 2024-09-27 04:07:09 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 681b2655-0f22-3a50-a11e-4487d8811337 | -22.7433 | -44.8035 | 2024-09-27 04:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| 7e996bd4-3ce6-3856-81e1-5c68f45e0963 | -7.5682 | -49.2001 | 2024-09-27 04:15:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 9e8ff6ed-b099-3ea5-bd99-291c1b83e296 | -7.5684 | -49.1786 | 2024-09-27 04:15:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1005f9ac-2e2c-3780-ba4a-a2b07d9614ce | -7.5703 | -60.5984 | 2024-09-27 04:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c08ba73c-efb2-34b9-9130-9bedff4154fc | -7.5887 | -60.5976 | 2024-09-27 04:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 9f38795c-a6fc-3052-a140-f96010e44379 | -7.5888 | -60.5785 | 2024-09-27 04:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e3b664fb-0548-36c5-a2a2-cbfba91d0868 | -7.77 | -61.2015 | 2024-09-27 04:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| e122d29d-6c42-3456-abb3-beb5155a52b8 | -7.7701 | -61.1825 | 2024-09-27 04:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 5d148f58-0648-3269-93a5-a4db773f6a00 | -7.8156 | -54.7252 | 2024-09-27 04:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 2a5b7cd4-cf03-3430-b33a-3a7faf81647e | -7.7886 | -61.1817 | 2024-09-27 04:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 8355c5e0-70fe-380e-a935-5b2defc2ab77 | -7.9175 | -61.2718 | 2024-09-27 04:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5c68e3cf-a28e-3e29-bc56-8b9901ef8a2f | -7.936 | -61.271 | 2024-09-27 04:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f31aeb4d-4610-3c91-9051-33e33746b843 | -8.6286 | -63.1219 | 2024-09-27 04:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 75d92b6d-8f4d-3f21-9fea-094374888a7c | -8.8116 | -67.6917 | 2024-09-27 04:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 81732f88-c4f9-3787-b5ea-9a2a3de3b77f | -8.8117 | -67.6732 | 2024-09-27 04:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c7fd6446-2a83-30ae-81bd-acde55df93ac | -8.9977 | -67.3909 | 2024-09-27 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 9712d272-c80f-3f3f-b6ae-53880de3af2c | -8.9978 | -67.3724 | 2024-09-27 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 700bb68a-71b0-31bd-a50c-4189483d039b | -8.9978 | -67.3538 | 2024-09-27 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9dd0f54b-59f2-3549-a8a7-789b92b452d0 | -9.0163 | -67.3719 | 2024-09-27 04:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5b4e957b-dd0f-30a7-bfbd-a80a52727ad1 | -9.086 | -61.1245 | 2024-09-27 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5f63c5d1-db6e-394c-a9e2-67363f57f54a | -9.1029 | -61.3726 | 2024-09-27 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a932112f-0c93-307a-b4c3-d4ee85178846 | -9.103 | -61.3534 | 2024-09-27 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |


[Clique aqui para ver as próximas entradas](README68.md)
