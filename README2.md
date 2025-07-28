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
| d0418085-83ca-3ce1-a6b3-053ad8118f63 | -18.12897 | -48.05328 | 2025-07-28 01:05:00 | TERRA_M-M | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1fa852cf-e3d6-372a-ab48-02ffe6014381 | -19.5082 | -48.48354 | 2025-07-28 01:05:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3a7ec09d-eeca-3d8e-969d-87732d00b897 | -10.75494 | -52.76638 | 2025-07-28 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8752c40a-ab7d-3b55-ac06-a1c699792da3 | -19.97157 | -48.42404 | 2025-07-28 01:05:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 72665f8d-9994-3fb3-9a9a-cdf730d47759 | -14.49329 | -48.6342 | 2025-07-28 01:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 6b4895db-315c-31ed-a56d-2bc36e319daa | -14.49099 | -46.54187 | 2025-07-28 01:05:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5e781708-5c19-31da-a863-9664f5e03ddf | -19.50564 | -48.46845 | 2025-07-28 01:05:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 405dad46-da1c-3853-af83-2ad16a435952 | -14.51113 | -48.66724 | 2025-07-28 01:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e5a842fa-4049-3327-8898-23307ffa7c27 | -10.54216 | -49.49117 | 2025-07-28 01:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 36eea57b-6062-380b-a7d1-58c2c3afb48e | -14.31079 | -54.14825 | 2025-07-28 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 1c0debc5-ed43-31cf-9716-b4138c5748da | -11.52276 | -54.68944 | 2025-07-28 01:05:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 635b155a-7689-3c2c-9820-0bf1ddbdfb81 | -13.52626 | -46.28884 | 2025-07-28 01:05:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ad7184f5-a2c7-35d2-a87b-f6486168a3f9 | -14.50827 | -48.64982 | 2025-07-28 01:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ac9d837f-ce8e-3957-9c3f-2a2771a0001d | -11.5215 | -54.68042 | 2025-07-28 01:05:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 13f31ab8-7db6-3f9d-ab95-ff0301a6b22a | -11.35249 | -51.25015 | 2025-07-28 01:05:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d9bf3477-66fd-355c-86ed-c14bbcec579f | -14.31207 | -54.15736 | 2025-07-28 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 43762160-4cab-333c-b82d-1ebf7e55e356 | -6.40457 | -53.35112 | 2025-07-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fb2a368a-981b-3147-8f91-f03ccc6476e1 | -4.31023 | -48.12238 | 2025-07-28 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| fe0cb5cc-c48c-3354-b237-f46cc8f61998 | -6.54799 | -56.19703 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5e3fdb63-c702-3343-a01e-c6eb0c29c5b4 | -6.54677 | -56.18819 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6496814a-7732-3301-8bce-642c542364a0 | -6.17771 | -58.07307 | 2025-07-28 01:07:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 30d2ad07-6fba-3736-b9c6-0a854d006671 | -6.49384 | -56.21109 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ecfb4604-2245-36b3-88a0-96cc79939328 | -10.31405 | -54.1574 | 2025-07-28 01:07:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c31daae5-f0aa-318f-9493-f0c4353d1b31 | -7.81221 | -50.78384 | 2025-07-28 01:07:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a686249c-ce44-32c4-bb5e-473f7d864865 | -9.02397 | -59.75911 | 2025-07-28 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bd02de17-22d5-3c5d-9873-37f433451347 | -6.39479 | -53.35257 | 2025-07-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 97bd4949-ff70-3dab-b286-9053e4d62033 | -6.49261 | -56.20224 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| b7f75522-3fc5-3854-8e94-a20bff1b18de | -9.25786 | -60.78402 | 2025-07-28 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f368e283-9d6b-3a3c-8b1c-c5dc7748b2f5 | -6.40614 | -53.3621 | 2025-07-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| da37d606-5703-3b48-9662-30ece482ece4 | -4.16278 | -46.82308 | 2025-07-28 01:07:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 210.7 |
| 9a090ea9-30f9-3b94-8a19-98f5f4bc6f70 | -9.45878 | -57.8564 | 2025-07-28 01:07:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c25873bd-a40c-3b27-9de3-20dc3dcf2c02 | -6.39636 | -53.36351 | 2025-07-28 01:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9d1e7e43-79cf-36c6-bf99-d36c8b58e0a3 | -4.16663 | -46.81711 | 2025-07-28 01:07:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 180.6 |
| 0014d348-d088-3ea9-8947-d94418df2f0c | -4.14983 | -46.81998 | 2025-07-28 01:07:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1be053fe-9852-3b22-b925-bebac530f084 | -6.50391 | -56.21867 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 6cfd855f-a008-3c7b-85a3-afff9e31ba53 | -6.50145 | -56.20098 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 34bd532e-b3a5-347a-9ce2-adb9b471938e | -6.50023 | -56.19214 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 15ea0a34-581b-30cf-a603-59675e373d20 | -6.50268 | -56.20983 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| fb98e750-8629-3fd3-9e0e-0cc9cbeb632a | -6.49506 | -56.21993 | 2025-07-28 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e02cf0a7-1213-3b85-bf3a-c358c0822dc0 | -4.30575 | -48.09299 | 2025-07-28 01:07:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f9474420-b93f-3f30-abad-bd52752d51ac | -9.03053 | -64.022 | 2025-07-28 01:07:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e782d164-f6af-331e-83bb-0cabb3c82286 | -6.489 | -56.1941 | 2025-07-28 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 75402cd0-e2f1-320b-8003-1db9899c85f5 | -17.3636 | -42.6532 | 2025-07-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 218.5 |
| dadb3bd9-a461-3b02-a43a-95e93512dcea | -7.2523 | -45.3943 | 2025-07-28 01:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 36a3b743-b00a-3067-8c46-a13abbb0772e | -4.1603 | -46.8101 | 2025-07-28 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 58b45967-d3b4-3a28-8b68-e8866e4f55ea | -14.4943 | -46.5387 | 2025-07-28 01:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e6f7ff55-5fe7-3c39-b1eb-bbaa413c51c2 | -17.3643 | -42.6284 | 2025-07-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 346.7 |
| 02d7c133-7bbb-3378-9d7f-15b4013fe225 | -17.3442 | -42.6333 | 2025-07-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 327a17c1-7f75-39b0-890b-19f740e3ee14 | -6.5074 | -56.213 | 2025-07-28 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| f8d7d078-762e-3d8f-a3f4-269226a17b3b | -4.1601 | -46.8322 | 2025-07-28 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a8ea4645-0322-31c3-a4f4-f21429c0eae1 | -6.5075 | -56.1932 | 2025-07-28 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c21eb587-330a-3fb5-b792-91ed7f3821c9 | -6.4889 | -56.2139 | 2025-07-28 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 17a8a3fa-ccb4-3ee0-8750-f16ec77a69be | -4.1601 | -46.8322 | 2025-07-28 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5f6a55ba-e8f0-3afb-b5fd-0c75b0db1554 | -17.3636 | -42.6532 | 2025-07-28 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 0463169a-44e3-336e-90d8-364481ed3586 | -6.4889 | -56.2139 | 2025-07-28 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ba617d73-dae6-3ecb-9286-46c5bd5ff422 | -4.1603 | -46.8101 | 2025-07-28 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| e18c1142-fdd4-3be2-863d-d466b104d32e | -17.3442 | -42.6333 | 2025-07-28 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d2ad859a-9187-30a4-baa0-8200803ffaab | -17.3643 | -42.6284 | 2025-07-28 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 255.5 |
| b6ab5969-b942-34ad-b504-7588adf53a98 | -6.5074 | -56.213 | 2025-07-28 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6f59893a-18ce-34a7-8df3-3c69a497cfa0 | -14.4943 | -46.5387 | 2025-07-28 01:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 37f3d911-96ea-3871-942f-9e12a9ca60d7 | -6.5075 | -56.1932 | 2025-07-28 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| bf51c5d1-6626-32be-b215-513a0004ab26 | -6.489 | -56.1941 | 2025-07-28 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b800ed09-47be-3c37-b813-b931d2c4e835 | -4.1601 | -46.8322 | 2025-07-28 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 20e23f7c-4935-36a6-a5f5-c49805a657f3 | -6.5074 | -56.213 | 2025-07-28 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f25e500b-046f-3bc1-96e9-4b80869da7a9 | -6.489 | -56.1941 | 2025-07-28 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 6f552045-3d1f-323c-bfe3-8f0d08332504 | -17.3442 | -42.6333 | 2025-07-28 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 311952a0-8f6a-38fb-afb9-5259adefba12 | -17.3636 | -42.6532 | 2025-07-28 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 054bb388-4324-3f00-8657-6aa66baa8a4c | -6.4889 | -56.2139 | 2025-07-28 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 367380f9-8de9-3774-8125-053ff1d54b49 | -6.5075 | -56.1932 | 2025-07-28 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 376abb44-683d-3a95-aca9-c55a1fdcdd2d | -17.3643 | -42.6284 | 2025-07-28 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 8507491d-0199-3c3e-a961-9de4ce323356 | -4.1603 | -46.8101 | 2025-07-28 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| b70f6713-8e85-3999-9c70-638849c4e487 | -21.0639 | -48.9124 | 2025-07-28 01:40:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| 3e37242a-fb56-3b26-a651-52fc596127c9 | -6.5074 | -56.213 | 2025-07-28 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f3a7836b-764c-3106-af9d-222471cd29ce | -4.1603 | -46.8101 | 2025-07-28 01:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| baa711db-38c7-32ab-8c6b-a4c90eed5c3e | -6.489 | -56.1941 | 2025-07-28 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2bdd5ef1-ce6d-3a78-9ad7-f4083f583994 | -17.3636 | -42.6532 | 2025-07-28 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 70c6daef-51b0-36dc-b658-14fffd0d8098 | -6.5075 | -56.1932 | 2025-07-28 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 0267f3d0-8ef8-3dd8-a3c9-5eb7ebc50148 | -6.4889 | -56.2139 | 2025-07-28 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ea24aa87-3d8c-3520-ad71-bd71486234d0 | -21.0633 | -48.9356 | 2025-07-28 01:40:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.2 |
| a688c8c9-cd12-3ee3-bced-72f243d0e236 | -17.3643 | -42.6284 | 2025-07-28 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 9a3bea83-f237-3688-84a2-c20be42a85e0 | -17.3636 | -42.6532 | 2025-07-28 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d6d89d25-5ccf-3acb-baff-2d6c6915e2e0 | -4.1603 | -46.8101 | 2025-07-28 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 22d3e096-869b-3756-9ad6-0c86f5b7b7f7 | -9.3626 | -40.328 | 2025-07-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 40d487e6-487c-3389-ad99-018220fe25ff | -6.5075 | -56.1932 | 2025-07-28 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 8a8b3b76-b692-3e1d-92d3-3bfed28178e3 | -9.3821 | -40.3004 | 2025-07-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 7104512b-38b6-3fd9-952d-f4350387e10a | -9.3817 | -40.3252 | 2025-07-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 1a9bb1ca-6e4e-3ebf-ba81-c96b5de09cdc | -9.363 | -40.3031 | 2025-07-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 42cf06ad-5b7c-325e-ade6-62c38ec4fe1e | -6.4889 | -56.2139 | 2025-07-28 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0b325787-bc43-3715-9468-b29dbaaefb56 | -6.489 | -56.1941 | 2025-07-28 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| b23f92a3-4644-3358-9127-d21ea9dc399b | -17.3643 | -42.6284 | 2025-07-28 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 18655ef3-f4f7-3d83-a576-68d002a182f5 | -6.5074 | -56.213 | 2025-07-28 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3d5d820a-47c1-3c1a-b174-4df78d087757 | -4.1601 | -46.8322 | 2025-07-28 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| e0354936-5e04-3442-9e83-93336a700a94 | -17.3636 | -42.6532 | 2025-07-28 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3937ba37-4946-3b30-86ed-6879048cedb7 | -17.3643 | -42.6284 | 2025-07-28 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 24743652-cf21-3b69-9e26-2fdba5d49712 | -23.3866 | -47.5138 | 2025-07-28 02:00:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| 34926ec5-8c3a-3920-9276-3c72003b592c | -6.5074 | -56.213 | 2025-07-28 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 710ffa32-4ae6-3c69-b4aa-7760d434a5a5 | -4.1603 | -46.8101 | 2025-07-28 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 8bae0d1d-6c32-374a-bc25-51d048cdea6e | -4.1601 | -46.8322 | 2025-07-28 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ad368777-83b9-3b28-be95-a7db8f37575c | -4.1789 | -46.8092 | 2025-07-28 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6ac4dbc1-6154-362c-bfab-3329ad867296 | -6.5075 | -56.1932 | 2025-07-28 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |


[Clique aqui para ver as próximas entradas](README3.md)
