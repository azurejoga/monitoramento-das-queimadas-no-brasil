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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7391b24e-3b3f-3ae3-9a55-054d5e33d24a | -13.04467 | -53.7114 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04b7aa2f-a329-3ad2-8fa5-67edcc707a34 | -15.88587 | -43.46064 | 2025-05-05 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 25160988-654b-33bc-b009-e0cad0cd969f | -15.88351 | -48.34578 | 2025-05-05 04:42:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 729fcf03-2815-387a-a183-fe0969f119a7 | -15.89092 | -43.45956 | 2025-05-05 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 10059c0e-b76a-3b65-9cce-42de87903b67 | -13.04547 | -53.72823 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 86fd2d2a-97bd-334d-a686-73121de2d9d6 | -13.03839 | -53.72696 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aee7d565-fdc4-31f3-804f-878b127dd761 | -16.6807 | -43.88691 | 2025-05-05 04:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9c99c84-8ff1-38d9-bdee-9d357ff4cb96 | -13.03908 | -53.7229 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc7315e1-9a1e-3baf-82b6-29a1e7c9210e | -11.39539 | -52.94708 | 2025-05-05 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 001478c6-2e6e-3262-83f4-9981007efc16 | -15.56952 | -47.85337 | 2025-05-05 04:42:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36bd4853-d579-3e54-86d7-bd65209a1f80 | -15.89149 | -43.45561 | 2025-05-05 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2a8c1a14-17ef-34d7-acb4-21d5d36485f3 | -11.3919 | -52.94648 | 2025-05-05 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 81f4ebfa-e209-398e-8d2f-90ca7b5bb173 | -15.88666 | -43.45317 | 2025-05-05 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fce45a3e-6037-33d1-b9de-017d993aba19 | -15.88653 | -43.4549 | 2025-05-05 04:42:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 61136ec9-46e2-33ad-9cc7-fe051ee57dec | -13.04193 | -53.72758 | 2025-05-05 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9be2917-3e0a-3415-99bc-150ea61b0e25 | -19.04752 | -54.36242 | 2025-05-05 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 540f6961-e798-3330-86e5-54193b62a30e | -23.54951 | -51.49016 | 2025-05-05 04:44:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8d9dd9f-92f4-3284-bad1-264ecbcd7f86 | -20.31868 | -46.75205 | 2025-05-05 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2186508e-687e-3721-8adb-6b5339bf6e38 | -20.47595 | -53.67623 | 2025-05-05 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebb26260-c6c8-3a9e-a92e-c0448ba71cfa | -20.99517 | -51.79335 | 2025-05-05 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6007cf01-392a-344a-bc10-6be8334f4dfb | -23.33916 | -46.77204 | 2025-05-05 04:44:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11052f88-8109-3593-bcea-3f94f9b9abbd | -18.00896 | -49.39282 | 2025-05-05 04:44:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 569c6831-6313-300b-a9f5-27a3755b8a52 | -18.94068 | -48.06008 | 2025-05-05 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b8fcefa-f8db-3300-8208-49fb4ed8b09e | -18.58024 | -49.15874 | 2025-05-05 04:44:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8390229-5224-3666-b45c-4fd07609a3b6 | -20.31916 | -46.74802 | 2025-05-05 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b591c47-a079-3971-9bd6-715412055502 | -24.24304 | -50.74163 | 2025-05-05 04:44:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d4da86af-4c0d-357a-9846-f0f671624f38 | -27.19867 | -51.4431 | 2025-05-05 04:46:00 | NPP-375D | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 690ace10-0340-3935-8d67-8bc4fc599c27 | -27.19928 | -51.43867 | 2025-05-05 04:46:00 | NPP-375D | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75ff7e86-4440-3020-8582-69c3b805e4ce | -29.59725 | -50.5387 | 2025-05-05 04:46:00 | NPP-375D | ROLANTE | RIO GRANDE DO SUL | Brasil | 4316006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 70b96596-c369-30ad-a8c9-628d7fe3e305 | -27.63473 | -48.90543 | 2025-05-05 04:46:00 | NPP-375D | ÁGUAS MORNAS | SANTA CATARINA | Brasil | 4200606 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b84100d3-5a67-3f55-bc86-73b94a9de3ce | -25.19017 | -49.32542 | 2025-05-05 04:46:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 20b7d8e4-96ca-33b5-9157-e0b76dc8bd1c | -5.16273 | -45.10526 | 2025-05-05 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a6c2f37-f6d8-394b-b630-9a632730e14c | -6.30896 | -46.05828 | 2025-05-05 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48ced992-e11f-3f5f-92a7-280a53635151 | -6.30847 | -46.06179 | 2025-05-05 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 572d405e-0d8b-3196-9621-c83879595bbc | -9.19314 | -45.34354 | 2025-05-05 05:01:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3f6e4df-dbef-3569-adab-567a70a54122 | -5.16332 | -45.10113 | 2025-05-05 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3121107-6849-30c2-9620-72045dd357bc | -13.04139 | -53.72535 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b8ee81c-560f-3ba6-a6a0-c25fb13ae4c3 | -13.04569 | -53.72147 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 007252d5-b4fa-33d0-b7c5-8ea069a8e333 | -13.05062 | -53.71316 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5148ea41-5603-3803-9ec5-ff195cb30776 | -13.04694 | -53.71263 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19cdb615-a1a3-3301-a270-b7516938ac16 | -11.62829 | -54.94136 | 2025-05-05 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0542752-4489-3809-a645-5225b1d4f3eb | -13.04874 | -53.72641 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1450b33d-55dc-3efe-be68-145bd51f2aab | -11.39117 | -52.94567 | 2025-05-05 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5dbb3141-531f-3272-90f6-ef52f24a1c9b | -11.39493 | -52.94622 | 2025-05-05 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d7be2c9-dd11-3a62-b4d8-57c60654b758 | -13.04757 | -53.70819 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3dd6c39-e8b0-3f84-9017-f0aff92d9270 | -13.04444 | -53.73029 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a83e26f-1274-3646-87aa-af96f9b173e2 | -13.04076 | -53.72976 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ea1b867-9488-357f-a066-39bf90302105 | -13.04937 | -53.72199 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd5bd248-1048-39d5-bc65-3ac26a0c6634 | -13.05242 | -53.72692 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4c8e5dc-5190-3ec4-80c5-e79fc16bd2f0 | -13.04506 | -53.72588 | 2025-05-05 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 184b5882-0d50-34c1-91a2-06ad3a83e760 | -19.04876 | -54.36385 | 2025-05-05 05:06:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a03b82b3-8819-3420-ac4d-d4a1bdbe57bb | -20.47677 | -53.67412 | 2025-05-05 05:06:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6bc5c39-6d6e-3081-bb65-ea865093d03c | -15.8955 | -43.4523 | 2025-05-05 05:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 407500cb-993a-3895-871b-83fec40d7540 | -15.8955 | -43.4523 | 2025-05-05 05:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 7a793dae-15bd-3771-aa44-71abc7e18876 | -15.88236 | -43.46455 | 2025-05-05 05:31:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9ae46aec-d6ba-37f9-84ab-38d8c4fbae78 | -15.88384 | -43.45411 | 2025-05-05 05:31:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 2f18f874-7b11-32fb-bfe3-ab3a85b8f57d | -15.88935 | -43.45109 | 2025-05-05 05:31:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 47c8a6b1-b538-34cf-973a-67751e701555 | -15.88792 | -43.46154 | 2025-05-05 05:31:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| b2e31699-6f58-3e05-a684-8cfa792811ed | -20.94179 | -48.89259 | 2025-05-05 05:33:00 | AQUA_M-M | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 7dda4be7-dcdc-309d-92ad-1e6411e9601d | -6.9613 | -42.8108 | 2025-05-05 11:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| f054a87e-0e55-346d-9609-2412659f68cf | -6.9615 | -42.7872 | 2025-05-05 11:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| c6600549-4143-3895-a347-fbec91a6e41e | -6.9613 | -42.8108 | 2025-05-05 11:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 4704cce8-6c8f-3936-b035-ae8c0dff4f1a | -6.9615 | -42.7872 | 2025-05-05 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 114.1 |
| 8d57fb86-3571-3e2b-8de1-dff05de90b0a | -6.9613 | -42.8108 | 2025-05-05 11:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 44d832a7-dfc2-3cb5-a44a-57c6171a1da2 | -6.9613 | -42.8108 | 2025-05-05 11:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 2d4213af-4620-3493-aa4f-ab37371ded53 | -6.9615 | -42.7872 | 2025-05-05 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| d2cda809-dbf6-354c-bcf3-9d550831a5a5 | -6.9613 | -42.8108 | 2025-05-05 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 13896d46-4b6f-374e-9c20-21e5966687f7 | -6.9615 | -42.7872 | 2025-05-05 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 697bfdfd-9331-3e1e-8cd5-de68411366a2 | -6.9613 | -42.8108 | 2025-05-05 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.2 |
| ea2cecb9-1f03-386b-b2d1-65ba08abeac8 | -6.9613 | -42.8108 | 2025-05-05 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| ab8bf934-bf18-3075-aac6-08b4bfb43dc6 | -6.9615 | -42.7872 | 2025-05-05 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| a2966a05-e205-3479-9067-2d0abc9dd96c | -6.9613 | -42.8108 | 2025-05-05 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| d5e88d4f-d95d-3577-9aee-727f695a09bb | -6.9615 | -42.7872 | 2025-05-05 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| bf283ffa-e5a7-38b5-baba-424e515340b5 | -5.66254 | -43.27393 | 2025-05-05 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1041cf3d-ea1a-3b86-ab32-b2c00245d985 | -6.96408 | -42.80453 | 2025-05-05 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 46419691-1319-31d6-8d7d-cc9ac727769e | -6.61524 | -44.78296 | 2025-05-05 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1a3c6b94-087e-3937-b20a-98711c713fc3 | -7.39528 | -41.76653 | 2025-05-05 12:17:00 | TERRA_M-T | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 808fcf1a-e1d5-37f8-9557-f5957090d550 | -6.96672 | -42.78589 | 2025-05-05 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b8f0e99d-c9c4-37ab-9da3-8967c6557d69 | -8.16765 | -44.39336 | 2025-05-05 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f7e54948-84f2-3a87-bf47-1f110d409b26 | -6.61654 | -44.77399 | 2025-05-05 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 2c17fce2-cd70-3359-91de-344071880cfc | -6.97577 | -42.78714 | 2025-05-05 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 31fc925d-9ad9-3d99-bb41-6e833e706cc1 | -6.9654 | -42.79522 | 2025-05-05 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 6eff1b66-e5be-398a-b3b2-f6c07166746f | -6.97444 | -42.79647 | 2025-05-05 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 38.2 |
| ba7ec305-58ce-3eef-bdf3-d91f6de6be11 | -10.98972 | -44.44377 | 2025-05-05 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 45c3aec0-f801-336f-be92-268e70555827 | -10.99101 | -44.43475 | 2025-05-05 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6289b0ea-d95c-3c58-89df-dc6ca99ae4e2 | -18.50819 | -47.60055 | 2025-05-05 12:19:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b037c40a-b615-3f2d-bd74-676fe48608da | -17.48362 | -45.30005 | 2025-05-05 12:19:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db52da72-f50a-38ea-a14c-40326e605a70 | -11.06909 | -46.127 | 2025-05-05 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 478a08a3-cb99-3447-bc1e-cd22060d8055 | -10.98213 | -44.4335 | 2025-05-05 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a352d1c7-c421-3d05-9a85-d02a1c1224d8 | -16.43221 | -43.47551 | 2025-05-05 12:19:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b9c618d-bc9e-3531-b646-c16e5da0b4c7 | -10.07664 | -43.07819 | 2025-05-05 12:19:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 767c0f64-83c3-3403-8f1a-1452ecbe37fa | -8.71921 | -44.0131 | 2025-05-05 12:19:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| be1f26b4-a398-39b4-859e-fa191d4c3787 | -10.98084 | -44.44252 | 2025-05-05 12:19:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| f3085b14-5865-3f84-9eb8-473848305238 | -18.50066 | -47.58967 | 2025-05-05 12:19:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e896f644-c13c-3651-afc5-5049ce509fa5 | -12.86852 | -43.52628 | 2025-05-05 12:19:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a47b5cf2-c85b-3250-a515-1e4cba118e6b | -18.49925 | -47.5991 | 2025-05-05 12:19:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 1e9fda0b-61a1-3409-a20c-e076df7cc9c4 | -6.9615 | -42.7872 | 2025-05-05 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 170cacb8-3395-3010-a735-c23bd62f43e2 | -6.9613 | -42.8108 | 2025-05-05 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| d775f514-70bc-3f4e-8220-b3f34145932c | -21.55799 | -46.84995 | 2025-05-05 12:21:00 | TERRA_M-T | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ccda9537-ce80-36d0-a1f6-117dd877f5c1 | -27.87599 | -49.79555 | 2025-05-05 12:23:00 | TERRA_M-T | RIO RUFINO | SANTA CATARINA | Brasil | 4215059 | 42 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |


[Clique aqui para ver as próximas entradas](README3.md)
