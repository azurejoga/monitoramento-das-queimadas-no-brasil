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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a1c12f9-f84e-3423-a5e1-397b710ed630 | -18.03049 | -51.15311 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c59526a7-d368-38ac-9a2d-f11c84d06400 | -13.60301 | -47.42836 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e686f15f-f454-366e-80d8-cdcd5ab24e4f | -13.03235 | -47.92162 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2283ae35-0bba-3b9c-9cbf-4e0cd45512c8 | -10.88191 | -56.06599 | 2025-10-08 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 126308d7-4a9f-35d5-8bcb-30cce82235cf | -11.14473 | -54.87805 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8baa7b14-fd68-3d79-924e-e722de8c3726 | -10.96587 | -54.14594 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c99e61b-1035-3d63-ab62-61ec9ad025c6 | -17.30103 | -58.06946 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b44ff173-e03a-303c-94fa-b39d2f382775 | -16.62152 | -45.42503 | 2025-10-08 04:40:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c4721b-0542-38bf-b0e2-4da772297044 | -11.34052 | -56.2024 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07d47299-d853-3040-b73a-4b9b9af618e5 | -11.94158 | -51.47451 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa186b0f-283d-346e-9c31-d01d6a03fce7 | -12.23429 | -43.7794 | 2025-10-08 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0eecbafa-5fa6-3a81-90fe-486aea11ab4a | -11.17643 | -54.88524 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 368cd023-7152-3c01-b0e4-8a80d67def6f | -14.79658 | -41.63641 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7a08d58-d06b-39fb-8681-ee3dcf1b97bf | -11.16783 | -54.88881 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6aaea53a-d332-3025-bbf3-6b4f93c0d2ea | -9.78909 | -59.97131 | 2025-10-08 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da6ae203-0c9f-3071-a225-267871a547fe | -12.18489 | -57.23391 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a315c0a0-cb68-31d0-8c0f-97a91f99fb7e | -14.91285 | -46.8129 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2016ce50-e1ee-36a1-9d08-e9e5085cdbf0 | -11.2973 | -54.88398 | 2025-10-08 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7690910a-9156-391c-88bc-c09d12ad5a26 | -11.1652 | -54.90388 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2607a14-167f-355a-936b-b5f3575461d9 | -15.70394 | -47.51126 | 2025-10-08 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5891fe41-f592-3132-91cc-076b538e732e | -14.7125 | -46.07921 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc9add71-7233-3782-9445-db6080a7d008 | -18.30351 | -42.22802 | 2025-10-08 04:40:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9bebce69-72ce-3b4d-8807-3164230ce5c8 | -13.07106 | -43.59383 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e58fda8-a1cc-3bd7-b8c8-52be7e841e1c | -15.88598 | -46.25596 | 2025-10-08 04:40:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d49bfe91-a644-3cb1-b92d-dc9badef198f | -11.70535 | -50.95602 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 567768c3-afa7-3bd4-8978-62551741f869 | -16.06159 | -47.77482 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eece809-c644-3396-88d0-064ec8692221 | -14.09822 | -44.30468 | 2025-10-08 04:40:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfa2b485-14a2-385f-a6eb-49017b10b201 | -14.24051 | -60.16871 | 2025-10-08 04:40:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05d6bd95-6a28-3ad0-ace3-0329ec6594b2 | -18.65584 | -43.90944 | 2025-10-08 04:40:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edb267af-d2fc-3079-95a7-a525998ce41e | -14.25579 | -45.86793 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6737aa0a-d3e2-325f-850e-34ec8e3d0f51 | -19.58105 | -44.65141 | 2025-10-08 04:40:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1477d4d3-f942-3ee5-8895-1ab951fbe548 | -15.37066 | -47.3011 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 7c631232-9066-3e4f-8079-67f60e9490e1 | -15.36749 | -47.32441 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9efe707-0237-30f6-b965-a39e6de77919 | -17.26507 | -58.11905 | 2025-10-08 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 101dd101-747a-3102-8cd6-8cecded41f1f | -13.73411 | -45.71331 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f006712b-a8ff-3361-8d44-58ac77580083 | -19.71763 | -43.9056 | 2025-10-08 04:40:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d81556da-66ac-35f7-b105-671ee5652b4a | -15.31775 | -46.17096 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3dcde636-8299-39ff-b35d-e48d4debe467 | -15.3143 | -46.15973 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bc1fa38e-cb57-334f-8053-937770d3d360 | -13.0228 | -47.91233 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0f468d4-7f8f-33c0-882f-403e594cb0c9 | -12.16523 | -50.96974 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d09d83f1-e4e6-325e-9bc7-36378706f21b | -15.29549 | -56.92475 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c06e68b8-6abb-37d4-a733-d7a5fa4392f0 | -14.65087 | -52.54491 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 745dc2d9-acb1-389b-8264-f09c7e0f183a | -14.71058 | -46.09357 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 28a8ae13-eae3-30ea-b6d6-7b101cd347eb | -15.25004 | -46.35993 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71630609-939e-3da9-b686-cb8c3cd9a19f | -17.274 | -42.65388 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 91a8f83c-5b3f-30a0-9463-dcd1bb563abe | -15.06452 | -49.48293 | 2025-10-08 04:40:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a21c9657-5fdf-3f0a-b818-0e1ceeeb6cd5 | -11.50112 | -51.48671 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7af83b88-0a6c-39e2-9cf9-b20b28d94670 | -14.65266 | -52.53392 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e6a222b-c8ce-399b-9db0-12c16424b8cb | -14.70093 | -46.01173 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d89adf49-9c3b-3684-a5b6-6525cf698db5 | -14.94553 | -46.80439 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 460ffbe1-bfc8-3173-8514-aacce00e0f69 | -13.06128 | -47.94746 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b8bd979-ad47-332f-b815-83d4dc56ee57 | -16.34249 | -47.04787 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8677b888-8900-3222-b390-4549e09f5cd9 | -11.18331 | -54.89169 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9381d0d-4811-3a68-819d-fa876da60c96 | -12.32316 | -50.26998 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7435543f-6a1e-39be-b967-367e1d4ba206 | -15.63411 | -52.56068 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4429c323-6787-36db-948d-da7f44871cb3 | -14.83376 | -48.41525 | 2025-10-08 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 485aa213-bb0c-3678-a6af-6f4d06fa3453 | -14.91804 | -46.80373 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5576546-b305-39b9-ace5-91b28312a98d | -12.92169 | -46.82567 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 693fb99d-09dc-33b0-8c1a-55d8a3fb7f96 | -14.79229 | -46.07196 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d684bf13-a0b1-347c-9981-b97b4dd8a5a9 | -13.28114 | -48.49285 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bfb24d94-2f4c-3d11-b4f2-39cae7c99dd3 | -13.80591 | -45.79364 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| edc8eb99-e2e9-308c-8901-56e6e3f45154 | -15.08317 | -46.61661 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9e3fce8-735a-3a87-9ff7-f19610299a23 | -15.49014 | -47.94792 | 2025-10-08 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e76225f-c69d-320f-a18e-db9c45b1795e | -13.39277 | -42.69958 | 2025-10-08 04:40:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 461291ec-e48d-3a2a-a6dc-1175d36cda08 | -15.37057 | -47.32679 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88844df8-e0e7-3069-bbb7-ca52bf25898b | -15.9532 | -42.60147 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b7f08518-1b2d-382e-bcb4-a644ddb8a864 | -14.70704 | -46.08942 | 2025-10-08 04:40:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ee0c6b4d-71d2-38b6-99f7-64f313d34b31 | -12.18931 | -57.2348 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74f05b92-7675-3f0f-9d52-9644d8e59a6c | -17.6904 | -54.21605 | 2025-10-08 04:40:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a6be3be-53ff-3775-845f-19e225cf7160 | -12.42752 | -45.62575 | 2025-10-08 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41a25278-46de-3d50-852b-ab2c1f9e1ca4 | -15.35481 | -47.32945 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb02a011-b225-34a0-a2f6-bb4a112c71e5 | -17.16161 | -56.60063 | 2025-10-08 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d9a112f4-18dc-37a1-8d2a-1af437fcaf9d | -18.50699 | -42.09871 | 2025-10-08 04:40:00 | NOAA-20 | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7a623c1d-da99-3b55-9c45-84b5f0a66a41 | -11.17383 | -54.90025 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1da41d4d-b143-32f1-ab5d-bd0ae24502d7 | -11.14757 | -54.89037 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d550f24-7756-34b4-a3cc-a793a0624be2 | -14.55972 | -47.00143 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55563ecc-7ec9-3de4-8c6c-e9f0d278754e | -12.99751 | -46.78136 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3b16d379-beef-33af-a987-3e4dcbc45cee | -11.68159 | -50.95573 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| ccdc2e87-c989-3014-9798-d08c8d5efd94 | -12.39286 | -51.14075 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbc6222b-1186-3011-9c3f-2f6009c8669d | -17.97256 | -44.97509 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9e8e920-8720-33d1-a9a0-d0d7f9d0fe88 | -11.74242 | -50.9368 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba2077bc-e7ac-3910-aab6-8166b3173d1d | -17.13787 | -43.46215 | 2025-10-08 04:40:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c87ee4c-93fc-3b64-af25-fdfaba037086 | -16.58867 | -46.55049 | 2025-10-08 04:40:00 | NOAA-20 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5557b44c-56e6-328d-92bd-f0d366e7c2c4 | -11.69541 | -50.95438 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fdb7c2a0-82b9-303b-833c-708f9ddf26b7 | -13.25235 | -47.79524 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f05ff005-b32e-332c-bd7b-256e67178f24 | -13.26709 | -48.04574 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7efa2b47-2c46-3281-86cc-08aa80df6033 | -13.00441 | -46.78705 | 2025-10-08 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8c7e12bb-13a3-374c-9b20-285c9c918be5 | -11.18503 | -54.88174 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b2325e7-3050-3bc1-bf52-872a128c7951 | -15.06736 | -49.48726 | 2025-10-08 04:40:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91dd6e51-9806-3aae-81a6-9200b58a7fe9 | -11.96053 | -51.4631 | 2025-10-08 04:40:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b8b6fbe-860d-3761-b801-7427c7755523 | -12.24317 | -43.78206 | 2025-10-08 04:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f397722-afa0-34e3-a37d-6f54191a0a50 | -11.7413 | -50.94384 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa2bee6d-d05e-332c-b2ab-730ce9b98e00 | -15.35021 | -52.81875 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ddddeef-9b6a-3949-b13e-3b91c1839478 | -17.13671 | -43.46191 | 2025-10-08 04:40:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23cc2e55-5a46-341d-add1-fa13acafe766 | -13.03647 | -47.89315 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1485e8-dbb3-3513-b9b6-e3036ccd45c1 | -14.39158 | -46.03059 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62b28d03-e55b-37bb-bd9f-2a6ec5ca0654 | -10.07733 | -56.75 | 2025-10-08 04:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4779f53e-d013-39bc-8aad-8993f46c490a | -17.28445 | -42.65547 | 2025-10-08 04:40:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64b6506d-12ed-3662-8e35-2a61ef7e1be3 | -11.15792 | -54.87691 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69d65fc8-5078-34d4-b991-d7411469227c | -14.62018 | -52.47906 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README75.md)
