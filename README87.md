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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd30968-9e57-3aed-a55c-a5faf048a081 | -12.58172 | -49.09299 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd009536-0952-33ea-8eeb-7a64a466e1ef | -11.05934 | -49.77491 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74b9f77d-c1fc-3dc7-bbae-e70ad4d798a6 | -10.87962 | -54.06221 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 992878ad-35b7-37de-9685-93e95b148ede | -14.79279 | -48.55725 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d4eb786-b5b8-32e4-a8a2-0ac6b9114446 | -13.73684 | -48.79433 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37d35cde-24a1-3a1d-b7ba-9657fc53cb4c | -15.81994 | -53.11213 | 2026-09-19 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 649827c7-6a97-37af-bfa5-9ee987532cf7 | -13.74253 | -48.78376 | 2026-09-19 04:59:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b48ae76-1a35-33fc-bcdb-77bc1bd0b075 | -14.95224 | -49.93944 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2f25bff-ffe0-342d-a7e3-7ad66c6912db | -10.70609 | -60.73739 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91c9a9c7-13cd-3697-b04e-b29f1ead6a41 | -14.67204 | -46.66091 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 22052e49-8dc5-39a0-9e2d-c35b27404af9 | -13.73781 | -48.78704 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3f66597-9e07-348d-b56c-ee8ed2d22b9d | -16.88465 | -50.5814 | 2026-09-19 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a6b38db0-3560-3b30-a5cb-511c0ca1ba16 | -10.87597 | -56.21006 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b509cd9-1c0b-3af2-80cf-00c122226650 | -12.13053 | -46.98648 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c2a78d8c-0ca9-3731-b3a1-93446941f108 | -12.98061 | -46.98142 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22fc50dd-0fe8-32aa-ac63-a485eabfd1d1 | -11.06314 | -49.77548 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 612d0c24-f5ab-3c52-bd12-afcacc8804db | -15.67899 | -52.76685 | 2026-09-19 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a434893-dfaa-39f8-9d3a-fe96e24febbf | -12.33019 | -50.7259 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 102f8d16-43b3-3322-9c79-11e4fc1e5d5a | -12.59976 | -50.92476 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13fda992-7654-3642-887f-0058d5c91f50 | -12.12974 | -46.9833 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 88f106b1-9d41-37af-895d-6959393723d2 | -11.55765 | -46.90319 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b5564dd9-27db-3684-a0c8-bf06083ba24a | -12.27823 | -49.16236 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 47ab639c-bdb0-38b4-b8fb-d11c7606bd08 | -15.5586 | -46.43827 | 2026-09-19 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e086f46a-8bf4-3945-8175-cedd54bc5d41 | -13.02206 | -46.93548 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 553dbdf4-a406-30a5-b2d6-8f8995c2e46e | -13.33498 | -51.66961 | 2026-09-19 04:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e4c74da-8aee-3ae3-919e-a9c7669432d7 | -11.30338 | -51.72588 | 2026-09-19 04:59:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bba19c1b-9476-343d-a65a-c5cd9f86ac4c | -17.31341 | -46.626 | 2026-09-19 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a68cde12-9b59-3796-80f1-3da2d43f8d89 | -14.79869 | -48.57891 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6401aa6-8e31-3658-a802-ef255647e86a | -16.60013 | -46.99418 | 2026-09-19 04:59:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78442885-63b5-3288-910b-ef0c7bbd6b45 | -10.69701 | -60.73569 | 2026-09-19 04:59:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e049776-da75-3229-a846-e79b914e9a51 | -12.98758 | -46.94334 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 228b23ce-14cd-30c2-a849-670880825c24 | -13.23485 | -46.90966 | 2026-09-19 04:59:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a7d106d-33ca-31f8-a358-b4d5bbbcf5ae | -13.61701 | -46.97124 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a28b1b49-f793-3b76-a602-c48adc01016f | -16.88535 | -50.57627 | 2026-09-19 04:59:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f3e9eb26-3358-3959-93ea-c082f08b855e | -12.13822 | -46.99063 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce9385f2-bef1-3ba1-984d-a5feed7c190a | -10.92941 | -53.96262 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7d464d7-8d2b-3887-8b5e-28bd0214d0b3 | -12.33147 | -50.71719 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8493e476-3f23-35f6-8222-0d06360c06e3 | -11.99725 | -49.96268 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 370ee021-31f0-3067-bb1c-300310ab44f7 | -13.63603 | -46.93431 | 2026-09-19 04:59:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 293b8fde-5fc5-38b0-950e-fd13788f0e4d | -11.46947 | -47.64934 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c40a73b4-12ef-39cc-bfb9-80eb0410d239 | -12.13178 | -47.00401 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e52437c4-2f9c-3896-94db-7069e37315d7 | -16.30838 | -53.86054 | 2026-09-19 04:59:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65625327-5421-3222-90fe-d1b8304a7f32 | -12.13119 | -47.00853 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 13006a4b-4854-333f-9cfe-3227e6eeba5a | -12.19806 | -46.48769 | 2026-09-19 04:59:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8925b0a6-ef80-302e-96e1-71039777b46c | -13.0073 | -46.9761 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c137fd5d-6e7d-3e1f-a4fb-8b1871bb0a03 | -10.91283 | -53.98148 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29e05ef0-b1ef-38d3-81ad-c359ce747187 | -11.14082 | -54.02171 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 0134fd73-af49-30f6-9b48-f15bcb05b1eb | -15.02533 | -48.57123 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55cc1b37-7168-36ff-84ae-e0ecd7eeef71 | -11.967 | -45.77736 | 2026-09-19 04:59:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce21bb18-6094-3558-99ff-2d7770c7e920 | -11.47326 | -47.65421 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2cfad963-1557-3dec-bd70-9064278d63e7 | -11.87745 | -47.61556 | 2026-09-19 04:59:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb06a450-df71-366d-b747-85887451161a | -15.55829 | -46.44088 | 2026-09-19 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 019ba601-8507-3e1f-a1ef-4aacc4c2df02 | -10.62712 | -53.89894 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db55ccf6-714e-38c4-9cd0-3f64ec2fa1d4 | -14.78521 | -48.5811 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b5fe1b2-f1c2-3b4e-b74c-d19dca8b0088 | -12.01289 | -50.04185 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f010531-8a38-3e2b-98bc-6d3eea9bda19 | -12.58996 | -49.09797 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dae896de-bb98-3864-9011-0211ffb74c21 | -12.58542 | -49.10101 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ec1a99b6-6860-3a2a-a9b6-b27ae8311365 | -10.88847 | -54.04929 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368d0f2b-2e71-3ebe-9c15-39e79fb85cbf | -13.61106 | -48.31887 | 2026-09-19 04:59:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb61ff8a-bc4a-3f01-8259-7e74c0a1b6fa | -15.87978 | -49.89452 | 2026-09-19 04:59:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2da5123-5260-3f42-8d63-6c21d6bd5702 | -10.85708 | -56.19486 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 394f4f5d-e51a-33d4-9339-340f512d129f | -15.67321 | -52.7341 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4045c03-ce97-3a52-a9fa-11b3d8f78e0b | -13.38468 | -48.03485 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e39f1f6e-bc4c-3bde-a42f-18a7ecad92e6 | -10.40892 | -54.41358 | 2026-09-19 04:59:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c50755c8-e555-38af-bbb4-aa178547b5c7 | -12.69409 | -45.94509 | 2026-09-19 04:59:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4103c036-d505-3cef-9012-64495ee859f3 | -10.86575 | -54.10666 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3886e28b-3f5b-3e9a-b6dc-87e6149699cd | -15.61121 | -54.37398 | 2026-09-19 04:59:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3243400-eaa5-35c9-b3f1-214d3df1705c | -14.79382 | -48.5825 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db8fd1aa-898b-33ba-8b25-d4c26d9808d3 | -13.73591 | -48.80131 | 2026-09-19 04:59:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc3bb17f-6c63-305f-9187-e7d8f36493ac | -12.86161 | -46.33789 | 2026-09-19 04:59:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ff74c6ad-1238-362f-bf8e-39008396edcd | -10.86272 | -56.20381 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a84014bf-6cb5-3f6b-b77d-56aadcef1c5c | -14.66223 | -46.65962 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1d473b92-e74c-3b3f-b813-542a28f5b032 | -11.40816 | -51.41743 | 2026-09-19 04:59:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78112dc4-0e11-3c7c-acce-8dce48e7bdd1 | -16.05042 | -49.98485 | 2026-09-19 04:59:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 606ce4b5-916c-3c17-94c4-0d28a217579e | -12.59044 | -49.09436 | 2026-09-19 04:59:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0ba8ed8-c98f-3256-b31b-b4497ededcdf | -10.25186 | -55.25266 | 2026-09-19 04:59:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166d1097-9f52-317d-bc6b-0c971bcbb7fb | -12.34245 | -50.71884 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cbd3725-79b5-3487-bf18-7ab2a8592afc | -15.6738 | -52.73011 | 2026-09-19 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bec06f0-4b7f-3328-aeec-05c62ab36d58 | -12.33257 | -50.73516 | 2026-09-19 04:59:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f17626ff-03b1-3d72-a049-5d47c8729d78 | -10.89123 | -54.05333 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e167144d-237b-3626-9ad8-c8b2480aae41 | -13.23011 | -46.90913 | 2026-09-19 04:59:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a400390-402d-3372-9fb4-35dc24d42067 | -13.38417 | -48.03596 | 2026-09-19 04:59:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c5868fa6-dac1-39c3-8a9b-039be0d537db | -13.00198 | -46.98042 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4483a08c-07f3-3255-ae26-51c894e7a798 | -10.89077 | -53.99218 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c8111bb-1052-3c9f-aa25-bb7acefe3a39 | -11.25116 | -54.09745 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6adf4bb-988f-3b75-bf45-37ded36bee85 | -13.38989 | -49.4527 | 2026-09-19 04:59:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fe3c744-b119-3be1-8a3e-d5d04f46737b | -10.89454 | -54.05387 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ae308be-ad49-35f6-b290-878d6a6495d3 | -11.67716 | -54.45171 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7f85a8d-fa9b-3e37-8ebb-28dbf364354d | -12.15127 | -46.99894 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9b64165-a2d4-370e-b8a3-f68daca2f0ba | -11.67497 | -54.44412 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e40b9487-75a4-30c9-8eac-367b713633e4 | -11.68082 | -54.44862 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d91854bb-8847-3b45-9ee5-03530213b82e | -12.12512 | -46.98259 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c625230a-19d5-3f71-bfb8-7ddabfe50567 | -11.03417 | -54.15894 | 2026-09-19 04:59:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7c54f6b-79cd-3173-86b7-cb6a16f48b0f | -9.37033 | -60.32014 | 2026-09-19 04:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95a39a83-23f8-3d9d-af55-7ded97f27778 | -14.81829 | -48.56404 | 2026-09-19 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 437a6ddb-0770-37a6-a589-0f43047a4b23 | -12.12385 | -46.99247 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e1d7a3b-7bb6-3d79-aee1-6fee830e5fd5 | -12.15941 | -47.00871 | 2026-09-19 04:59:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fb65e58-b07e-364f-adb5-02bb017efb84 | -12.26895 | -57.18004 | 2026-09-19 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98163376-6ab0-3132-96e2-a1e3269f0c1d | -11.67772 | -54.44819 | 2026-09-19 04:59:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95d8e738-6552-3616-bcfb-9255c040b103 | -10.8599 | -56.19933 | 2026-09-19 04:59:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README88.md)
