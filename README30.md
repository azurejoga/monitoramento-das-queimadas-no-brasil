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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76fac650-a4a4-3418-ac41-ac4d11d39367 | -8.41752 | -45.68573 | 2025-07-30 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5e90fe5-8563-3aa4-82fe-09be9d32ae5c | -7.85643 | -46.73795 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f01ba332-c875-3573-a6d0-92be4cebcc20 | -9.74534 | -48.57515 | 2025-07-30 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71f58861-4a42-36f6-a835-b7eb9e32afc7 | -10.52713 | -42.55399 | 2025-07-30 04:51:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 80986bd1-793a-3547-a334-421c8564e9a2 | -8.94767 | -46.7365 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecb12a7d-a1d9-32ac-9fd1-3cd22d7e43d3 | -9.55247 | -40.32638 | 2025-07-30 04:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51b02657-f7c9-3431-b4c6-4e7cb12feb59 | -6.52371 | -56.2103 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a92378b4-e76c-3367-90ab-1a79dea8c8d2 | -9.45797 | -57.84928 | 2025-07-30 04:51:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b3348424-dc2b-31be-bcc4-d5d3673bf605 | -6.56165 | -56.18454 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0dc46db-ba8b-3a76-8de1-a65ce884ebd4 | -11.34074 | -51.25048 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d6080ac-952b-3fd5-93e8-4e3f1a65c637 | -11.9252 | -44.5439 | 2025-07-30 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d56e725f-d196-34ce-8c80-a1774527f2cd | -11.98068 | -46.95196 | 2025-07-30 04:51:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3971c02-6b8f-3c57-9da1-a4c0433344c2 | -8.02141 | -47.68464 | 2025-07-30 04:51:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a5d3645-4eed-3047-8c63-f4a8e9c053fe | -9.87588 | -44.69335 | 2025-07-30 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcd23628-8c9f-3d30-9a92-d005471deed5 | -11.46715 | -45.12029 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 99ad88b2-1f8a-3522-8711-acb204485222 | -6.52441 | -56.206 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a0a8409a-dce2-32a1-b16e-af3d3c46924c | -6.49235 | -56.21833 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36a30bf3-871f-3a76-9864-97ff3bf6bc68 | -8.51579 | -43.31108 | 2025-07-30 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 63286ded-78ee-3af9-9199-03219905837d | -10.9347 | -45.77849 | 2025-07-30 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cba4866-5ae2-3771-8deb-6ba02039cfb3 | -10.61671 | -45.24373 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6813402b-b3f2-37b1-91c8-5c7b4c4dd768 | -6.49601 | -56.21893 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d642129-6449-3fc9-92e2-b4460d6999e9 | -10.7004 | -48.86218 | 2025-07-30 04:51:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f447a404-02b5-38bd-bf52-ab54e5e2f094 | -13.06627 | -47.38928 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ed280b5-6201-3fa8-a2d3-03d3eee66212 | -10.60697 | -45.23925 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e7b6c6c-4889-3616-8f89-5d67e9d7c761 | -11.74227 | -58.34238 | 2025-07-30 04:51:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf5c3475-17e2-384d-99bd-836e5cc288ce | -6.52353 | -56.18825 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a0d25c7-4f9c-35a1-843a-bd55447656bd | -6.48878 | -56.01234 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ee569f3-83d7-3836-9059-ed783534dc86 | -9.23065 | -50.04665 | 2025-07-30 04:51:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0be0f8f2-11c9-3705-bf10-7be009a78fb1 | -8.5214 | -43.31184 | 2025-07-30 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b228caed-01a5-349f-a228-173d1faccf60 | -9.17754 | -48.84543 | 2025-07-30 04:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e738dbbb-dc50-3ead-8bbf-96b49cad0489 | -10.60658 | -45.24226 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7af8c5f-952a-3246-831c-c12779ea7df3 | -8.95661 | -46.7377 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f8cdfd8-0901-3419-8e0c-33a38fd6acc9 | -7.93511 | -44.092 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1950625b-69a8-365f-805f-ab674e37e494 | -8.67873 | -51.21171 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e0e5086-9793-3128-bf9a-6a25d7e9df7b | -6.56236 | -56.18027 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3bcc77a-77f6-3381-a787-635526ce55d9 | -14.46044 | -47.87158 | 2025-07-30 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f4c1a75-c628-3d83-a0cc-7897fcf386cd | -12.72918 | -47.00955 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f5294e0-7c9b-3bf9-bc48-aea399c3be41 | -11.98531 | -46.69777 | 2025-07-30 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ee73ab8-3927-3adc-aa36-0efd24a6eaf8 | -13.08098 | -47.32038 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cc14363-9683-3c51-ba07-d38db3d62ddb | -7.93617 | -44.08775 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b974b98f-8be5-3d6d-8bba-c9a016b321aa | -7.00071 | -52.88298 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5e05084-81e0-39f0-a20e-8cecfa8d5a22 | -8.94702 | -46.74105 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 495e75e5-6766-3de3-a4f3-2ac2ddda0c73 | -9.40017 | -45.49131 | 2025-07-30 04:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1bc5d309-fb28-3188-9441-6f3e86b99860 | -7.85705 | -46.73367 | 2025-07-30 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 879c80fc-90f8-3be3-9e00-f727c1631b4e | -8.32953 | -54.75605 | 2025-07-30 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78aee368-dc95-3ae4-8f33-6a5d02eff79e | -6.52649 | -56.19312 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cbf37d97-cb53-396f-9dc1-764839049193 | -14.50327 | -46.53046 | 2025-07-30 04:51:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c0bae0a-77ab-3451-a84b-f48e705f48e8 | -6.49305 | -56.21404 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51d8dc5c-1d66-3756-83d5-fcb50471f34b | -6.52075 | -56.20539 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2efdd209-2be4-3b83-9f99-4f53eb6abb19 | -6.50037 | -56.21524 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f6f17f5-cbca-32f7-ac23-e32e4fc5c275 | -9.87065 | -44.69273 | 2025-07-30 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5649dad-3af8-3949-97ee-331c5fd4c64f | -7.94128 | -44.08607 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c122deb4-a426-3f54-b19a-00e3910dc50b | -9.27275 | -40.55221 | 2025-07-30 04:51:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4807c783-f26b-3711-a6a4-20b09ca33b04 | -8.03361 | -46.91174 | 2025-07-30 04:51:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 599c382a-50f0-3471-b7bc-272cd8eb6159 | -13.41543 | -47.29274 | 2025-07-30 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f549f67c-fb88-3979-ad78-62feee79298b | -6.52144 | -56.2011 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80935a9c-351e-3905-8b25-7bc15334afd1 | -7.72861 | -51.12806 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 803182b3-3a5d-3963-9c3a-b8fa4b30f239 | -6.50682 | -56.19868 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c34b6fc3-4d6d-384a-b6bf-fb603154e725 | -7.74058 | -51.09565 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5774e704-ebc6-3e98-ab26-042ca3b0f61e | -6.52737 | -56.21092 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26fac7b8-b546-396d-83c2-3512fdcfcb04 | -13.08538 | -47.32224 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 892948ed-4c51-37d2-ae7e-4ea65ce4d206 | -9.74134 | -48.57458 | 2025-07-30 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73820abb-9557-3b62-8077-97790b0dbd74 | -14.09604 | -53.9838 | 2025-07-30 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffc3ad17-428b-379c-84ef-fd12d4908a65 | -9.87166 | -44.69008 | 2025-07-30 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26eb4d3a-b4ba-3207-b565-d406ff7e7b9b | -12.54421 | -44.73003 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11c517dc-6e43-30b6-b99f-eb3d6d0a0b8d | -6.55952 | -56.19738 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d89c28-793e-3929-8b98-f7b8080cd1e9 | -6.95654 | -56.38024 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 96560dd7-1750-38fb-a1a3-e452951e6171 | -6.49952 | -56.19743 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c018e836-fbc6-3a96-91b3-a2ed80f2544c | -13.08105 | -47.31403 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a95a5482-40b2-3e65-8d0a-fed123ea6c66 | -7.9357 | -44.0911 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b26ce73-bb19-3740-acfa-1e55404afb07 | -11.92231 | -44.54048 | 2025-07-30 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49d3aa48-4a22-3351-aadd-f0d612747075 | -6.5296 | -56.19676 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9230aeb9-15a4-376f-8f6b-943e1e5d6953 | -10.61242 | -45.2371 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 362d87e9-8e94-3905-8586-28f40aa07029 | -9.04308 | -45.07466 | 2025-07-30 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f56beab4-5e52-3a0e-a636-c1e8e5cb08d7 | -10.46447 | -46.73038 | 2025-07-30 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 530f8acb-7b5c-3bfe-8db9-44eebcf5c292 | -14.76384 | -47.54419 | 2025-07-30 04:51:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4619c99-77ea-389f-ad74-286869f89fc2 | -14.09272 | -53.98327 | 2025-07-30 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fd1d2e12-32d8-3533-88ba-95f9fc3400eb | -7.94657 | -44.08678 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33d7ee5b-202c-38be-863c-267fd84a8af8 | -8.95834 | -46.74493 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8f82ab8a-d8f4-3539-85e1-51d242a0541a | -7.03606 | -55.5052 | 2025-07-30 04:51:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1e387c6-bc5b-3c50-bc83-8a3d195bfd19 | -7.94611 | -44.09018 | 2025-07-30 04:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 225a489b-3aa3-3c31-989c-241c098ce607 | -10.61787 | -45.2349 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a61f013f-4623-316a-9424-00c518a2bf30 | -7.72975 | -51.09779 | 2025-07-30 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| adf0e5d9-7ed1-3783-be55-23d25150d5f1 | -13.09309 | -47.29823 | 2025-07-30 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 982f04c2-ecdc-3d0b-96c8-43c41a5069f9 | -6.53449 | -56.19002 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8387c9bf-c05f-359a-ac2b-c72987b99f29 | -11.27413 | -52.47226 | 2025-07-30 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff24273c-5c16-3f0a-9a20-27ab6326752f | -6.56459 | -56.18942 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6d25b33-068c-3ee1-bd56-38f297787b69 | -10.61165 | -45.24298 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f950a1a4-e302-36be-8398-c87a1dfc927d | -10.93886 | -45.785 | 2025-07-30 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38e5378c-3baa-3526-8b54-d844bd4fa78f | -12.81514 | -45.44313 | 2025-07-30 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11f20191-5c22-3465-82f6-79adcb2d460d | -11.98062 | -46.69715 | 2025-07-30 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 205d36eb-aa10-320e-b3da-7f8f9824e43a | -6.56601 | -56.18088 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44fdf8ba-6f62-3c58-8323-b529a9965714 | -6.55587 | -56.19676 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c5cb81f-2fae-3895-ac89-ce1cfb9e248d | -8.95326 | -46.74886 | 2025-07-30 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de1ba775-2cb9-3204-aa87-14224167edc4 | -6.50838 | -56.21218 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63e6dbdb-a9df-3572-bc52-45b7ed9b2441 | -9.04845 | -45.07281 | 2025-07-30 04:51:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1b87726-103e-3bdf-ba9d-9c74fbf75c85 | -7.09847 | -63.04734 | 2025-07-30 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d131aca5-9e0d-38b5-b0b9-6dcf0b2812cb | -6.49671 | -56.21463 | 2025-07-30 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dba49fd5-0b42-3b86-89a7-893ad3483ce5 | -7.10412 | -63.0484 | 2025-07-30 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 388c30c5-9f97-38b9-a625-ba7a0ec04b75 | -10.61826 | -45.23192 | 2025-07-30 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README31.md)
