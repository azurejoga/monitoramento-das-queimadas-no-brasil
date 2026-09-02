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
| d44f1430-c49a-37ae-87fd-69e0fe823766 | 0.65051 | -59.57406 | 2026-09-02 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f73f959a-eeb4-310d-99a1-acaabbc31640 | -6.83116 | -41.68335 | 2026-09-02 04:55:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ff3e8cd-e4f5-3baa-aa57-0adf016dfc9a | -4.96784 | -55.84459 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61cbb4c5-3e15-35dd-b504-d28301720eed | -6.14009 | -44.45891 | 2026-09-02 04:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7c12bdf-607a-3c63-94c5-ce29726ec140 | -5.24967 | -55.8989 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3f6fb00-5c4e-3c0c-a236-1e9ce93c2dde | -2.84149 | -49.51358 | 2026-09-02 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e26210a1-1f00-34e7-8c02-a69c70a66312 | -4.49702 | -45.91326 | 2026-09-02 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 430c22e8-562a-32b8-b5b8-d301457befe5 | -5.75965 | -53.39977 | 2026-09-02 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d0fa14b9-1eb1-3494-99da-3213ee0fbbf6 | -1.01455 | -53.72104 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b6642c4-6cfe-3f28-94ce-ab439e24a044 | -7.23343 | -42.76716 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5214c5ad-9aad-30ce-924a-03212f2e0bfc | -4.91415 | -48.99071 | 2026-09-02 04:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a25a20-cc88-31f5-b267-c904d9e5f5aa | 0.97645 | -59.38698 | 2026-09-02 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc620363-0ccc-3dec-9db2-695f815d2896 | -5.25599 | -55.91093 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 007c2bbb-c39b-3529-a12b-7fc500aa5711 | -3.37358 | -52.79797 | 2026-09-02 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4cddbd2c-24c5-3fc8-acb1-384c1e4c95e8 | -3.18456 | -48.0253 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 182bce39-e1a8-3beb-bc7e-09be5f64e96c | -3.63522 | -60.55508 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a9019de-942d-38c2-8da2-fc41bf15c49d | -6.27923 | -47.35958 | 2026-09-02 04:55:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1890a0d-8de6-3e2d-b568-349d39947abb | -3.37419 | -52.79416 | 2026-09-02 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c30da11-549e-38f5-aab6-166e8d65fc3f | -4.11779 | -51.02716 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a634f0ab-b171-339e-a421-7497b4e225c8 | -6.93234 | -45.71525 | 2026-09-02 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67a4f3e5-aa79-3c24-b798-a04fb9a3856d | -5.74092 | -52.18005 | 2026-09-02 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 427df415-a3d4-3677-a21c-90de96049fe3 | -4.17887 | -49.40383 | 2026-09-02 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1df22b76-6360-3608-91bc-79aa9d215c1f | -3.07599 | -60.73817 | 2026-09-02 04:55:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b094f10-d72c-3cb8-bc5a-0fb58db60daf | -5.24443 | -55.90531 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d57cc91-11ae-3e25-97d2-22908547bd82 | -5.12283 | -57.03147 | 2026-09-02 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e21cee0-4860-325b-81d7-3c56b7acc80b | -6.618 | -47.63558 | 2026-09-02 04:55:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b17d82d3-85af-3954-835f-876402205d5e | -3.18517 | -48.02145 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 533bb019-b8be-3457-a01c-349b5564ff56 | -3.8471 | -44.06012 | 2026-09-02 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74d531b3-d328-3438-ade1-539fdc836e93 | -1.99724 | -47.25223 | 2026-09-02 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| faa4fad4-f830-3ded-8b87-fb53303b1d97 | -1.43127 | -54.23053 | 2026-09-02 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76ab754a-3367-3949-906e-9ae5cedcea3e | -7.22565 | -42.74709 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5429fd2c-3a59-3056-bcdc-869fad06786a | -6.91443 | -45.71364 | 2026-09-02 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcb1ea76-0840-3088-b52e-d8b762373d1a | -3.74638 | -59.32144 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9db86752-e8a2-3219-9ae8-2d67ab0f4b00 | -7.22407 | -42.74858 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b5cbb835-c187-352c-aaeb-38762fc1527c | -5.25489 | -55.89253 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faa1112c-2a09-3c33-bb72-70efe5f3531c | -5.25143 | -55.88834 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2ef30e8-a698-30fc-a7c6-c42848f44784 | -7.22609 | -42.7439 | 2026-09-02 04:55:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53ecbbeb-96d4-31b0-ae5a-1af04505c129 | -4.11723 | -51.03063 | 2026-09-02 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09b33ca5-64e7-3b55-9d02-840316efb01b | -7.22452 | -42.74544 | 2026-09-02 04:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 329ad192-89ef-3f1a-a9c3-b439febfd71f | -3.62254 | -60.56079 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48c11fff-b471-3060-b7fb-30ab5d87e2dc | -6.80842 | -46.1969 | 2026-09-02 04:55:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf7b9b30-8678-3891-945b-dbc70f6d498e | -2.16333 | -47.48002 | 2026-09-02 04:55:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd110d80-2608-368f-9190-0827e3f7b93c | -3.7446 | -55.9803 | 2026-09-02 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d70c2090-94df-3291-9756-13992e4e8e78 | -5.25254 | -55.90665 | 2026-09-02 04:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 346c5a4d-378b-3f00-8c8a-b413df3c8a5b | -5.39429 | -45.62844 | 2026-09-02 04:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8d9cebc1-bbd8-34c1-97d6-1caab7a06dd5 | -3.90587 | -59.65092 | 2026-09-02 04:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3ffb228-4cc2-3ee7-bf15-49c71504fcad | -0.78821 | -50.68072 | 2026-09-02 04:55:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffdb9f8b-60a8-37f8-a80c-10203814e613 | -7.17549 | -44.06964 | 2026-09-02 04:55:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b71b7cb8-5d25-3a4a-a9bf-95e4c31e819b | -6.93709 | -45.71194 | 2026-09-02 04:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddbf65f2-5cd6-36ca-8ca0-030e13e26029 | -3.86549 | -52.15045 | 2026-09-02 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7ac1eac-2762-39ca-a712-8ed3ab07959d | -3.63587 | -60.55121 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d10d3668-5d92-3bed-a218-b5eb7862e155 | -3.65882 | -58.91751 | 2026-09-02 04:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3192be65-bc48-3348-8af6-66f620573fcb | -3.24303 | -47.24968 | 2026-09-02 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4edc5602-6b52-3803-bce9-fe8bf6bc34fd | -3.61989 | -60.57637 | 2026-09-02 04:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2547aa35-45c8-3b3f-8f27-17b3a8a4c9a6 | -1.01832 | -53.72158 | 2026-09-02 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f6319d3-63d4-3b6b-a604-df965648c963 | -8.9041 | -62.34811 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 814d9b09-bfe1-3bcf-8e25-1d17ca9249c2 | -8.76732 | -46.43959 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adcda378-9034-3223-8efa-ec1d25dcbfb7 | -6.92696 | -59.64526 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba4b5971-f24f-3117-b33e-a935538bbde5 | -5.94766 | -57.6847 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1af71cb2-c41f-3b90-add0-b102a9c7b23f | -7.28918 | -49.82996 | 2026-09-02 04:57:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1a59215-3329-3033-9702-15503acdc2aa | -8.47627 | -54.7006 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1fea4da3-b784-3e1e-a18d-04ff04215f2f | -5.34036 | -60.15108 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 943e8d29-84e3-3491-ab13-6c1add11a86b | -11.33406 | -50.62303 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a585db5-ee2d-3e91-a2bf-1e814a751e4a | -11.75231 | -50.54819 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14ed6d21-56c5-3aac-9452-8c901a24c86a | -7.53982 | -60.72013 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 016a0b77-1387-3f00-9841-373e3679bbe6 | -8.12028 | -54.95526 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| ce9bac06-b23a-35e4-9212-9918b2d74e28 | -9.08907 | -65.37492 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b99ff71f-542f-32e9-97b9-82816d4e0b51 | -9.37542 | -60.31246 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06577fe1-656d-3e98-a98d-f1ab462847c1 | -7.18208 | -55.48285 | 2026-09-02 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16815bb8-95c0-36bf-8937-2bd243fa31d6 | -9.40062 | -51.57622 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 606dad81-4334-392c-b2e8-534b2f1ba425 | -5.90898 | -53.56738 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8de2953e-4262-3598-813e-a09757b1550f | -6.25509 | -55.43811 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cada89bb-4050-3790-b231-4acd55e4976e | -9.87643 | -64.98762 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbe673ca-eed3-38bf-b7d9-ff423b358695 | -8.47848 | -54.70961 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 925192b5-15ed-389b-ae2c-4cebd1e06d52 | -9.00863 | -50.77911 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5b10f21a-b658-3a24-83ab-1b5026fd6f63 | -11.33407 | -50.57749 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c97641ef-de27-3f5c-b234-760c1ea69ffe | -11.34659 | -45.41439 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f763c1da-1777-36ce-80e2-238b5df8c1f3 | -8.62302 | -54.85168 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c13ba52-56ee-3add-b1ba-b003a3cdde89 | -12.14469 | -47.06617 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72db33bf-f693-3aa6-9aa2-514be27a1f35 | -7.19471 | -60.68865 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4c13ae0-3e43-30f0-a4a7-8bfb73fbce92 | -10.78096 | -44.75623 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 9e5f09ce-8693-36be-92e3-3fa211518ae2 | -11.02076 | -48.38564 | 2026-09-02 04:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83dccea7-0c36-36fe-87f4-cb4c4776509b | -11.30063 | -45.16585 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5ed3786-6fa7-3b8c-8bdd-36f2e42b0b5b | -8.76418 | -62.58018 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c279d6a-ae8f-32b1-82a7-744bfae77041 | -9.01328 | -65.40691 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8eb52ec-820d-3031-802a-ba8753663daf | -9.53188 | -51.66895 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22d0249f-3e00-32d9-b815-4ac0b75b910d | -6.80735 | -59.10631 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e4ef566a-6c62-35f5-b8bf-50d98ca41014 | -6.16176 | -57.77775 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4c3ab3e-7c40-365a-9dd2-002ccb0571b7 | -8.47206 | -54.7258 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc23b8ac-1c45-3e99-afe4-f85ef73cae7d | -13.41384 | -43.87602 | 2026-09-02 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7713a924-5f3c-3564-b4d4-3fff43a9e588 | -7.5392 | -60.72355 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff9d9322-f75b-3345-a0af-e74ebb2c018e | -9.8325 | -59.47084 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bea2f42a-fd5e-3b76-bedb-b5ca22f37fe1 | -10.77693 | -44.75048 | 2026-09-02 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08220237-e7ed-3203-b5ff-70014849e3ad | -10.90549 | -45.33993 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8271178e-b098-3782-add5-dedf8791f5de | -13.40825 | -43.87851 | 2026-09-02 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1aa0120-5612-3374-93b9-8fc4351d0b85 | -12.13645 | -47.09535 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdcda93e-98f2-3f50-82c7-3772709e5920 | -7.66043 | -45.87885 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 070d7db4-5f7f-3c54-8724-63745734de73 | -6.88084 | -56.5088 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df05199b-805b-37c5-aadf-28757a0437cb | -8.72696 | -49.59571 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2868ca5d-6fe7-3bf2-a5c6-ab747527f2a8 | -11.66095 | -50.1849 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README33.md)
