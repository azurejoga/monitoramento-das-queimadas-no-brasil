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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07d62e00-730c-3bf2-a0c3-baffcfa6fd48 | -10.46606 | -47.9511 | 2025-06-02 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d1753e13-4f7b-3eb6-ae0c-8043a4182474 | -7.06878 | -44.92877 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a2f61c5-6442-3ee4-9939-52cc2fc46915 | -9.40146 | -48.43956 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eff4aa3a-b639-3130-a623-81d146aa1dac | -11.91666 | -54.8263 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcdc9337-b592-30a6-a4e8-a7333ef6d280 | -13.08243 | -45.26852 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4867eaab-b45c-370c-9e78-499e695a2620 | -19.52341 | -44.26238 | 2025-06-02 04:17:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ef4c8fb-9657-39ab-8869-ff9f2593085a | -12.62647 | -48.17052 | 2025-06-02 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf8c6e11-8361-382e-a715-1d0af074b7a1 | -7.21021 | -44.18258 | 2025-06-02 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9865b280-792a-3cd8-9e6c-f72190810e78 | -11.44498 | -55.00399 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46d4e4a1-b93b-3849-8a85-1912940c9d1e | -13.17189 | -46.95877 | 2025-06-02 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7424b35-7588-311d-b0bf-88739b6b8174 | -7.08348 | -46.55753 | 2025-06-02 04:17:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ef20467-6582-3ffa-9b18-2e352502ae17 | -10.82068 | -56.94767 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d935d09-b038-3af8-9fbf-108526c8aae1 | -10.82188 | -56.94186 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f577b35b-a3e6-3d61-94b8-f4f65a2b1ec2 | -18.6904 | -46.98548 | 2025-06-02 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efddbc24-ea04-324e-b55d-c6981942eb78 | -17.25558 | -42.66212 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3d00f0db-2b52-3ae7-ad64-26edb9f0403d | -16.67986 | -43.88235 | 2025-06-02 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 715a0757-c90e-3fa2-b814-b4f165323727 | -6.7325 | -42.8873 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 840c9156-3305-3a68-bfd7-bd728ce00ce5 | -11.91586 | -54.83043 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 027d2e22-b596-3b8a-a74e-172cae175656 | -10.47002 | -47.94861 | 2025-06-02 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f920889a-b17e-3196-b252-f7937ed8ef75 | -7.88449 | -46.2255 | 2025-06-02 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4a5bb3c-7fd0-37d8-9d5f-ecc5c6e166e3 | -13.08634 | -45.26551 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c0c6035-a865-36ba-94e7-5f162f9c2e3c | -13.10359 | -45.26472 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91336ee1-d702-3ef8-bb9f-2a4eaa5306b2 | -9.32516 | -48.94926 | 2025-06-02 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65f5401d-8a87-3186-bca2-4ffe9ac6eb1e | -18.22267 | -49.21353 | 2025-06-02 04:17:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77c3c6b9-39ff-3105-93bc-e967df54499a | -19.43885 | -44.34159 | 2025-06-02 04:17:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d82d56b1-b70b-32ec-bf4d-47c68d9969c7 | -10.46626 | -47.94796 | 2025-06-02 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e1d06be-0cef-3d98-8e4d-c4c66db21f67 | -18.68461 | -46.99977 | 2025-06-02 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9fb1736-acc1-34e2-8934-53146fc89065 | -7.27359 | -43.22935 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a34b45a7-a72f-32da-bce0-a2293e6c60ef | -9.39806 | -40.36338 | 2025-06-02 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f988d574-75f8-3de2-99d4-befd7ecadb36 | -16.68327 | -43.88291 | 2025-06-02 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26ac1840-ebc3-3a9c-94d2-bea54a0be1be | -13.09301 | -45.26663 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93c8de17-4313-3ad1-92d7-e91d9e07ec0b | -9.11848 | -47.64159 | 2025-06-02 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 465875d7-fe42-38c8-b231-8741d7f51963 | -11.91103 | -54.82735 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8ba402e-a046-368f-bd62-7fc8dc2f90ec | -7.00855 | -44.60669 | 2025-06-02 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d009b1b-4562-3b5a-962f-e815a2eb3462 | -11.44541 | -55.01063 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93146b84-19a9-34fe-9177-3ba0fd45f4d5 | -7.38301 | -43.13653 | 2025-06-02 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9800b17c-627e-3b03-938d-da4c472eedfa | -8.77634 | -47.23881 | 2025-06-02 04:17:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1859518-f38d-3e1c-87ca-9caf156149d1 | -7.27692 | -43.22988 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fcee63d9-c7c5-3ccf-bcbe-9bd96f667987 | -17.25916 | -42.66266 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d68b53d2-9dfb-3362-91bd-682d3ce3e5dc | -10.46926 | -47.95317 | 2025-06-02 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9babbac6-d3bd-389c-8d41-09b8a09c8027 | -6.73638 | -42.88434 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8796531b-014b-314f-b1dd-1e22b2b1ad19 | -7.01084 | -44.59233 | 2025-06-02 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 841f1e25-750c-3311-98e8-a29d5aee67c6 | -17.25841 | -42.65997 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d7c3dd4-5fdf-38f3-adf1-276d4fa7a699 | -6.64165 | -43.20427 | 2025-06-02 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fc6ae5f8-0b26-3f57-a8d3-d3aaabefc475 | -19.7822 | -42.09487 | 2025-06-02 04:17:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e6bb806-5903-3a62-a104-491458c19228 | -9.39869 | -40.35902 | 2025-06-02 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a19768bb-b5de-3235-97f7-b2aaf7b27085 | -13.083 | -45.26496 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a22f1930-e203-3bb8-81b9-ac64db328354 | -17.29026 | -42.65025 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 728af5fd-bbf2-30e3-8272-8576dd2dfef1 | -7.26365 | -43.24918 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6a99174-f2e2-30bb-9ca3-5831d7251212 | -11.91745 | -54.82217 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cbeadfe-9eec-38d3-8075-c3a124d44fb6 | -9.39763 | -48.42103 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 573c954c-655d-3d19-a711-15b8ed74fbc9 | -13.09358 | -45.26306 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 16f0ad87-1f21-35f9-ac71-c96fdb35d077 | -9.3285 | -48.94988 | 2025-06-02 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54a54909-4423-328b-9671-75497d7cd990 | -8.33134 | -47.09598 | 2025-06-02 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb12504d-2db2-318e-9ca8-de8938868310 | -9.39647 | -40.36075 | 2025-06-02 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b2098356-5199-36f4-aa6b-60274407a70e | -11.44038 | -55.00531 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f697b0f-a5c7-306b-9a0b-2cec367e9367 | -10.82407 | -56.94876 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbec7606-f813-3577-a02e-93882d50080d | -9.56445 | -40.77787 | 2025-06-02 04:17:00 | NPP-375D | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b76c27f9-bb69-3ace-9358-7cdd5a76441c | -9.11707 | -47.64813 | 2025-06-02 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e59b892b-92ee-336b-9b14-6b169e2745ff | -10.8284 | -56.96147 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19912802-cb70-319b-a9de-7c9a6f53e46f | -18.14647 | -47.80163 | 2025-06-02 04:17:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 644cd9d1-ec89-35e2-99a5-ebcb3cb816ea | -7.07984 | -46.55693 | 2025-06-02 04:17:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf62946e-4933-3f4d-8463-25c6f296dd69 | -7.07231 | -44.92942 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3875c852-120c-3b9b-8d59-3f549ca245bb | -6.63833 | -43.20374 | 2025-06-02 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2632f13e-7812-3d84-9ac2-e0d94190cd77 | -10.81088 | -56.94588 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ce4a8b2-6aa2-3b29-ab11-832fe82c9bca | -10.81746 | -56.94741 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9de1ea92-ce76-349e-a50f-8c1de8aea3c8 | -8.13015 | -49.58714 | 2025-06-02 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a1fad1a-0fb6-39b2-81fb-e786c0ea6c9c | -11.9159 | -54.83267 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4eff603b-9029-3d28-ab34-e85d6eeca58b | -13.08577 | -45.26908 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd74496c-decb-3b52-bd3f-cfabc87dcc7d | -7.0695 | -44.92522 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4ce06e8-8e58-31cb-bd43-8e11de65dc44 | -15.7773 | -49.30571 | 2025-06-02 04:17:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0c77a95-25ad-34a3-9caa-7af02b1ae915 | -9.56868 | -40.77423 | 2025-06-02 04:17:00 | NPP-375D | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e5a3cad-9b91-3aa7-a701-418b88f05613 | -7.00912 | -44.60308 | 2025-06-02 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8240740-18f3-3ea1-aa0a-82d666e4eb29 | -10.46684 | -47.94656 | 2025-06-02 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac35eb53-6e20-3081-8bf7-e514ad524146 | -7.09942 | -42.91671 | 2025-06-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3ceb1f7-eb9b-3b52-b074-0c77781dc389 | -7.07332 | -44.94468 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17aea3a8-f97e-3612-803a-25cc36395bfe | -9.3993 | -48.41113 | 2025-06-02 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2a0e135-e44d-34fd-9d4f-ed9596c03587 | -11.44999 | -55.00925 | 2025-06-02 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9042f78f-f960-3aa6-84b1-8a6fc575c011 | -17.27112 | -42.65588 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2de3cc7-2b11-30b5-ad56-04d5e36b7486 | -13.08691 | -45.26195 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4996648-dba2-334f-87d8-40c428b38e2d | -7.62869 | -46.11652 | 2025-06-02 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc84b8e9-0190-3697-8878-82527113e3f8 | -11.88595 | -46.722 | 2025-06-02 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b14948e4-47e6-3b2f-90b5-1f5e0f6938b0 | -7.27678 | -42.91235 | 2025-06-02 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e98ffe9-1eab-3e9d-867d-368cb1454b7a | -10.81207 | -56.93998 | 2025-06-02 04:17:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 407cc1da-22db-3ccd-b9a9-48796458f50b | -17.28966 | -42.65451 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 13c93b99-71bc-3942-9cdd-811effcdcbfd | -17.27411 | -42.66072 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eebe6a71-be29-32da-bb15-2f6324e0c30b | -11.2976 | -46.45866 | 2025-06-02 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6db28204-c36c-3321-8319-7cbd09ed02b3 | -7.06937 | -44.92509 | 2025-06-02 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4d5d06c-b06c-34ff-9fbe-0e38b0e5ab96 | -13.09025 | -45.2625 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee829d25-f0c4-31ea-b403-471861185b8d | -11.37327 | -50.06907 | 2025-06-02 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a80cf3b3-8204-3930-9fad-157ba254f254 | -17.28607 | -42.65396 | 2025-06-02 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b1f3ff6a-654a-3032-8994-068d042c9ba1 | -7.01422 | -44.59283 | 2025-06-02 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16eac89c-87f8-30e7-8f0d-d23f130e183e | -11.91507 | -54.83455 | 2025-06-02 04:17:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 083689e3-343b-3a79-8c25-1524ca5ef310 | -9.11785 | -47.64363 | 2025-06-02 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06e58892-e056-3517-bf05-39b9806fb364 | -9.07037 | -47.15999 | 2025-06-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6188454-9ab1-3aa0-868a-5e08fe1a5d54 | -9.07109 | -47.15561 | 2025-06-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f8737d7-f5a1-38af-863c-df0d7e489915 | -7.63137 | -46.11569 | 2025-06-02 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d7ff21f-d63e-3825-8c9d-b38dcc603819 | -13.0891 | -45.26964 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66c95062-36e0-3d78-906e-b0d8060ad454 | -8.32693 | -47.09981 | 2025-06-02 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbe4b9d1-e9f9-3503-968b-376a82bb025f | -13.10025 | -45.26417 | 2025-06-02 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README5.md)
