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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f69413a-e65e-322f-a332-bed6e02ab0d7 | -10.9009 | -45.3509 | 2026-09-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| f84e6082-7587-3ad4-b03b-eea691c8a41f | -12.1516 | -47.0608 | 2026-09-02 02:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 5bd7db99-c301-3d3d-b260-755337911dd1 | -11.7906 | -50.5236 | 2026-09-02 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 71c1cd73-c0d7-39a0-9480-69677c7552ce | -10.3956 | -49.9918 | 2026-09-02 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| ebe503ad-3b89-3f00-9428-22a77ae5933d | -11.7719 | -50.5043 | 2026-09-02 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1d5cc97f-6d3e-3251-8760-fe7297d68209 | -10.9204 | -45.3253 | 2026-09-02 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 72afd20e-d2ad-3a11-a4e9-e0a17ae50df4 | -10.7965 | -44.7437 | 2026-09-02 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 716d05cf-8eaf-3c08-bc8f-03f1f39f680c | -11.791 | -50.5021 | 2026-09-02 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 670daa66-78a1-3403-a460-ee5e2aee0307 | -10.7161 | -46.1942 | 2026-09-02 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 10d6dd7b-047d-3ae6-84a5-db93424ea2d4 | -6.6948 | -58.7678 | 2026-09-02 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fde3f965-02a8-3a07-8a14-264f523bf493 | -3.2486 | -47.2438 | 2026-09-02 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 1d73cef3-fa61-3087-ab35-ebd6d8307264 | -11.3524 | -50.6159 | 2026-09-02 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 5e89d0ff-b410-379e-b677-86345a2c4266 | -11.7716 | -50.5258 | 2026-09-02 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6372a5dd-b8c1-39f7-95fb-ea527c5077cc | -11.3147 | -50.5987 | 2026-09-02 02:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 864b8ff4-8866-3d3d-a209-31b2928a06b9 | -10.7962 | -44.7669 | 2026-09-02 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| d53bc397-826c-320d-81e3-9ce225181b0d | -13.9855 | -58.672 | 2026-09-02 02:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c499aa59-31ec-3abb-8ec3-7915f2b6f318 | -10.7158 | -46.2169 | 2026-09-02 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ca0c0919-f02f-3859-86ee-a6ad0eff5167 | -10.777 | -44.7695 | 2026-09-02 02:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| d7158b7f-f0d1-3fdf-beb1-6edd30dcfa8c | -8.4669 | -54.7237 | 2026-09-02 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 6ac1594f-4bc9-3031-9df9-4cca6c18e182 | -10.7965 | -44.7437 | 2026-09-02 02:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| c3f3e852-b2eb-3535-92de-5adda06fcdf3 | -8.4483 | -54.725 | 2026-09-02 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 5e8f8e9f-e209-3431-8986-3dadf21e559c | -8.4485 | -54.7048 | 2026-09-02 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 867605ab-e71e-31f4-aeaa-6364f4def1d1 | -10.7962 | -44.7669 | 2026-09-02 02:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 25836ee2-e6d9-36a9-a658-8948616107be | -6.6948 | -58.7678 | 2026-09-02 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 06b4ad11-0ceb-32f0-9b44-2a2aadf00878 | -11.791 | -50.5021 | 2026-09-02 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 180.7 |
| bc828d5b-8dd4-38e6-b8ca-4f7f4649391f | -10.9013 | -45.3279 | 2026-09-02 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e984281b-d65c-3c6f-b47a-6824a7f7bb7f | -4.5008 | -45.9054 | 2026-09-02 02:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7ad92478-697a-371e-8c52-329693c6c911 | -11.7906 | -50.5236 | 2026-09-02 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 288b5888-828b-3575-ae54-e9d8e065f9c4 | -8.4671 | -54.7035 | 2026-09-02 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| c75ed2ea-ef17-3386-afc9-947638917f4a | -13.9853 | -58.6919 | 2026-09-02 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 11c004ac-6655-3cf6-9649-e11c9e1d95dc | -8.4669 | -54.7237 | 2026-09-02 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| bc4b62c9-188d-3aef-ae20-9bc44b16f1dd | -16.1926 | -47.491 | 2026-09-02 02:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 7d38b3c0-baa8-3f51-929c-a2bee4332a12 | -16.2123 | -47.4874 | 2026-09-02 02:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4979f737-4fe6-3969-974f-eea4fdb40815 | -10.9204 | -45.3253 | 2026-09-02 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 0cf4b302-c91c-3f86-b85a-27480824e609 | -7.2006 | -60.6706 | 2026-09-02 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| fd75d5eb-c42f-37e6-bdae-783b205380ed | -8.911 | -62.372 | 2026-09-02 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4282c013-a2b2-3768-a7b8-d37a8f47ccbb | -6.6764 | -58.7686 | 2026-09-02 02:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 43e9b703-45a4-3197-b1f3-e6ee479fa24d | -14.9672 | -48.1111 | 2026-09-02 02:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 3815b730-5a28-3113-975b-b0410155fa79 | -13.9855 | -58.672 | 2026-09-02 02:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 3baadf19-1425-3d87-924a-8ccaef7ea19e | -14.9867 | -48.1079 | 2026-09-02 02:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4c2d4887-ed59-36ef-94a6-1fd83ec696af | -11.7719 | -50.5043 | 2026-09-02 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 156e4397-5890-3b8c-98d5-7ca4fbe5e24f | -17.0878 | -56.8534 | 2026-09-02 02:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 57aff8e5-32fe-3f94-bb30-68c2dcf776b4 | -8.4298 | -54.706 | 2026-09-02 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 085d122d-65a9-342a-9ce4-5a501a83b691 | -12.1504 | -47.1283 | 2026-09-02 02:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 167fb7ad-bf4a-3a64-ba57-b95beef53748 | -11.7716 | -50.5258 | 2026-09-02 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bfaa027a-9621-3e1b-b02a-23ac5b7bb3f7 | -8.4483 | -54.725 | 2026-09-02 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| c85a5172-f987-3a57-b247-9ba15924dfc0 | -10.9013 | -45.3279 | 2026-09-02 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 27c904d2-0722-3145-8cbd-efa108de082b | -4.3587 | -47.7853 | 2026-09-02 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3d095bcd-2568-37ca-9fc2-9e31e17226e0 | -8.4298 | -54.706 | 2026-09-02 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f5f94e13-097e-3916-8f5f-be035c1d34be | -14.9867 | -48.1079 | 2026-09-02 03:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| a88650c6-2f79-375e-be9b-d796fe06265e | -8.4485 | -54.7048 | 2026-09-02 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 24bf91f0-9f9c-33c4-8819-728301d9c581 | -8.4669 | -54.7237 | 2026-09-02 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 4b90602f-c3f8-3472-a097-235a26598afb | -6.6764 | -58.7686 | 2026-09-02 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 3cc54a0f-c5d9-3956-8926-0664aa68eff8 | -10.9204 | -45.3253 | 2026-09-02 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| ac26f520-7287-38bc-a4ae-671ce12bbc08 | -7.2006 | -60.6706 | 2026-09-02 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 822cfadb-ede8-33eb-8d0d-115033904723 | -13.9853 | -58.6919 | 2026-09-02 03:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 3083181e-d456-38fb-9877-8a4f43850c53 | -14.9672 | -48.1111 | 2026-09-02 03:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| ac40604b-cd63-30da-b50a-95c637dad439 | -11.7719 | -50.5043 | 2026-09-02 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7bd8a1ce-6600-3b14-8c84-8eca1a067b81 | -11.791 | -50.5021 | 2026-09-02 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| c9492cb7-59c4-3fb6-85d4-10aa09ddaa6f | -8.4671 | -54.7035 | 2026-09-02 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 1e0c80ca-0b1b-3811-af1b-7919769edac2 | -12.1504 | -47.1283 | 2026-09-02 03:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 776e9a57-46c5-3b96-a504-37c783bb099b | -6.6948 | -58.7678 | 2026-09-02 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 018dd717-72c2-3507-9fa5-7f82846d37b8 | -10.9204 | -45.3253 | 2026-09-02 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 90cac866-27ad-3502-a3a2-f8067508f398 | -11.791 | -50.5021 | 2026-09-02 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 39045855-48d2-35a9-9839-aac54d17a095 | -10.7962 | -44.7669 | 2026-09-02 03:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 27064e2d-4940-355f-8ca5-f84039032fee | -8.4298 | -54.706 | 2026-09-02 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| c70b11af-346b-3d65-8dd4-1b305fa9e58e | -10.9013 | -45.3279 | 2026-09-02 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 9740f486-0c64-370d-8a51-d9cc80810ad4 | -6.6949 | -58.7485 | 2026-09-02 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 542d99aa-8821-31a9-8c52-f23706106271 | -8.4858 | -54.7023 | 2026-09-02 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 92150408-3d02-3bee-8c81-ca9028f50955 | -4.3772 | -47.7844 | 2026-09-02 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f9fb3199-6b7d-3294-91a0-e7031fd1ec72 | -8.4669 | -54.7237 | 2026-09-02 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 83ae6f78-e088-3048-a5ed-ea9d39b4ebb9 | -6.6948 | -58.7678 | 2026-09-02 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d6ac01ed-03c8-37b0-82ba-b736d289f213 | -11.7719 | -50.5043 | 2026-09-02 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e2769602-befd-39c3-a040-586c33454a31 | -8.4483 | -54.725 | 2026-09-02 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| add7b72c-1feb-3ae4-acd4-0399b39de9cf | -10.7965 | -44.7437 | 2026-09-02 03:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 1a19cd0e-e326-3a54-8736-d70db218c4a3 | -11.3048 | -45.1575 | 2026-09-02 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a8579e5e-a631-3ca9-9691-b5a163581caa | -3.2486 | -47.2438 | 2026-09-02 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b94478b3-eb27-3263-84b2-271087105448 | -8.4485 | -54.7048 | 2026-09-02 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 97ddded4-12e2-3397-b21b-9f0c44673b72 | -8.4671 | -54.7035 | 2026-09-02 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| bfdb9468-bfcc-3cf4-8009-e017dd017f4c | -12.1504 | -47.1283 | 2026-09-02 03:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d3ac1c41-6cb3-31bb-88ad-4ca050897053 | -11.34 | -50.64 | 2026-09-02 03:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19885195-34fb-3ad5-ba3b-96ac32b2e0d7 | -11.31 | -50.57 | 2026-09-02 03:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ececab6-9606-3a11-8569-2ecae2856c54 | -11.34 | -50.58 | 2026-09-02 03:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e6f68e2-2a18-3b2c-b6bc-d50136d601f8 | -11.31 | -50.63 | 2026-09-02 03:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08dc98b9-5b22-3f4b-9267-7264b06d9dbd | -4.99369 | -37.09763 | 2026-09-02 03:15:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74e8e838-4758-3afa-adf8-cfff49c04d32 | -4.99054 | -37.10128 | 2026-09-02 03:15:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7f61dec6-5cfc-3889-998c-b1e91fab0b7c | -4.99275 | -37.10277 | 2026-09-02 03:15:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e5c97231-55a8-3556-8323-a5ab11d4e691 | -12.46959 | -41.3175 | 2026-09-02 03:17:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37a48a08-9b5b-344c-a5b2-bd6628c0ec26 | -9.57526 | -40.34567 | 2026-09-02 03:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 57b37ae9-26d2-3204-b927-48849b6700d3 | -12.46262 | -41.31536 | 2026-09-02 03:17:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c0a19e0d-114c-3843-b8bb-acc39858ad4f | -12.46559 | -41.31358 | 2026-09-02 03:17:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d1bce09f-9b48-3b38-ba14-ed33a9b8bda2 | -9.57382 | -40.35258 | 2026-09-02 03:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7a4faadc-8a68-37e5-8ca5-6d392a2c5e9d | -9.57008 | -40.35123 | 2026-09-02 03:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 18f2992d-1274-3d7e-9c90-ce78c2a9e421 | -9.57147 | -40.34432 | 2026-09-02 03:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 4098e4c9-c29e-3d52-9a58-a134e01b61ee | -17.66141 | -40.25643 | 2026-09-02 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c6248721-9b11-336c-b61b-01c7ac0ee375 | -17.65673 | -40.25385 | 2026-09-02 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 70ae72fc-d6b8-3e83-9c3d-99f72a73fe04 | -17.79484 | -39.70719 | 2026-09-02 03:19:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6f53264b-b423-376f-9cf4-114c576d0fc0 | -17.66033 | -40.26117 | 2026-09-02 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1309a26c-1dcc-3ec7-b686-c436ffc2d6e6 | -17.676 | -40.13724 | 2026-09-02 03:19:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 6fbf7229-77be-3f8b-b781-ebdd2a190900 | -17.79122 | -39.70802 | 2026-09-02 03:19:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |


[Clique aqui para ver as próximas entradas](README14.md)
