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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0be2ad2-a25b-30a0-b846-cb4a449cab33 | -6.98328 | -43.2191 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 86adbe60-143c-30e2-b893-3a4b2f1531db | -1.41664 | -48.03341 | 2026-10-07 16:03:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa59e262-eeb6-3a44-b68f-01390a84a349 | -1.21154 | -49.03571 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 94a73b51-7133-391d-945e-a7c5318aacf7 | -6.99949 | -45.12241 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b0264da9-3cc5-3ffb-ad3a-ceff4508f1f1 | -5.73946 | -41.72941 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ce550fca-00d6-3610-b807-e7b90a634698 | -7.77244 | -46.66339 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2bf3002-8f73-3728-96bd-ce1ba27963c6 | -7.04904 | -44.33106 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e9dd2b2f-b3c1-3625-b6a3-d484a55d1958 | -2.45425 | -46.02713 | 2026-10-07 16:03:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 97a025a0-85e1-351b-bbe6-eae749890fb6 | -5.28194 | -42.75277 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 244da6d8-f915-350f-80f6-37b0cf8c3c56 | -3.94614 | -41.54635 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 285.4 |
| 43538e4f-d11c-3109-b62a-b2421fa80124 | -4.93179 | -45.10988 | 2026-10-07 16:03:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0f4913d-0e39-31e4-b8bc-9ed260e3b247 | -7.57233 | -46.72926 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7178ee4d-c226-365a-8b99-90da1e230ce1 | -4.24129 | -49.9808 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 223f9e35-dc92-316c-bcee-9a95ffd52ab4 | -5.96858 | -41.3554 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 876d21d5-3be9-3fbe-bfc6-97b1eeac0d58 | -7.76676 | -46.66079 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4ee1a1ad-983e-311a-a8cc-1426fdd24f2c | -5.96376 | -45.70351 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| b4bf5d4a-315e-3007-824a-c87e6a7b5366 | -6.62089 | -37.88109 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 2876a763-e477-31a4-bb77-4752b377fac6 | -6.70238 | -44.01177 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4641ecdc-235c-3f7f-9ec9-30a2919a3e8b | -4.62495 | -48.86093 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 16738a13-b326-37e4-add4-9785b83290c3 | -5.73036 | -41.74406 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 071e4b39-5982-376c-a822-07dec7a647f0 | -7.47895 | -45.77226 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d8de86c4-ede1-3b58-924c-56626c95cbed | -7.56061 | -47.78006 | 2026-10-07 16:03:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 0a834a17-f080-3abf-bb43-bda06e566352 | -1.87821 | -45.43162 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 33543ee0-2eba-33f9-85ce-fecdcd6fb202 | -3.89728 | -44.10703 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 203fb8da-78b0-3996-b8da-619c37cf509d | -3.19031 | -50.56348 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2143e85c-520e-32fe-ad85-ee2180c60082 | -3.77131 | -41.77973 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| d14e4ea8-b4f2-3300-bdfe-84db68cf2314 | -7.56276 | -46.69751 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a7f7111f-0d72-3884-b1c2-d120dd05634d | -5.94887 | -46.35705 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4c37b8e-5e21-3a71-a471-dd71f8d7e3aa | -3.05683 | -44.44933 | 2026-10-07 16:03:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f5779b9c-0807-3b4d-9947-945d7d438aeb | -7.56113 | -47.78385 | 2026-10-07 16:03:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 90fcdc44-27ee-3fbd-986f-9283b62ded50 | -5.21156 | -48.33979 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 4097c21e-8d08-3a90-b89a-0139ab37ee77 | -3.8876 | -44.12773 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| c0bd7839-612a-3f1a-8d2c-67268e843c35 | -7.39114 | -46.21429 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e6372523-1610-3c4f-9e9e-583a36e66645 | -4.97748 | -50.57081 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 2f1a499b-b2ce-3828-bd50-5d3fca885515 | -7.24082 | -43.75815 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e267683e-bc06-3647-a6be-a305131b8de2 | -3.75299 | -41.70647 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 951ef62a-11b0-3865-bf60-256f5ec32e03 | -6.93407 | -45.29275 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1e7ecf02-256e-3936-b864-11cf92a18378 | -6.68093 | -44.94797 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 43bcdf34-7845-39c5-8d5f-d87a285a9525 | -5.98149 | -40.95089 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| fdb14f46-a234-3b22-9ba9-dcf067069caa | -3.9491 | -41.54177 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 838039a0-2e12-3721-a1e1-75c7c9517bbb | -3.23301 | -42.79013 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf4b5456-a565-3f25-a3ba-e2c26f624074 | -3.64965 | -39.44093 | 2026-10-07 16:03:00 | NOAA-21 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ef4c9511-0c73-3057-951d-d1a9104e93d6 | -3.49271 | -39.50446 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 0e2801f5-5f99-3953-a638-e35fd07971e6 | -4.27394 | -39.54784 | 2026-10-07 16:03:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 514cd1d9-f477-36ed-b6fc-9fa13eee5b02 | -3.20346 | -42.95454 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 7ca60add-f898-3b33-8706-d49f780a9f4f | -4.45107 | -49.14793 | 2026-10-07 16:03:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| efb1d36a-a68d-399e-8485-3bb77374d4a0 | -3.94625 | -44.70805 | 2026-10-07 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4185fe8-1263-3249-adff-85325ef623d0 | -5.99642 | -44.12664 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0130ba33-581c-3d5f-b9df-bddb6b04db95 | -3.37306 | -41.75167 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a22b4050-3cb9-3427-a767-12dce5cf6a3c | -4.82995 | -40.73146 | 2026-10-07 16:03:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 5361eda0-afae-3b0d-ad23-9431a6643ab2 | -3.54936 | -39.47461 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4aa39eea-8564-3ece-8e16-c3e7d12fc7df | -4.36831 | -38.80106 | 2026-10-07 16:03:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b02fd630-c3b4-3215-99d7-bc9524b2637d | -6.17572 | -35.42451 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a08d7874-7a08-3407-bed9-670d3dedae96 | -6.59222 | -47.40324 | 2026-10-07 16:03:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f46cb58c-725f-3ee1-af56-8e0462cefbc9 | -6.85647 | -43.88412 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| abd168de-8d2c-3f20-97ae-ac3668905749 | -5.97374 | -40.94784 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 98ec7fbf-4408-3f39-a748-9c9f471b8735 | -7.17347 | -47.79454 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a8f15453-f2d6-37ae-bd4e-c58b686f8839 | -3.41406 | -40.03844 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 05111c13-7395-3577-ac40-f139187f7013 | -7.45973 | -43.20494 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7a835c0d-dcf5-35f8-927c-0ea2d30d6adf | -7.54652 | -46.73606 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| caec83b8-718c-3d20-b0fd-4f85dc28cb68 | -2.42163 | -49.76004 | 2026-10-07 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f717a8d6-ec24-3f7d-b854-07a965898012 | -6.31947 | -43.4871 | 2026-10-07 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b10874e3-7746-350d-af8a-6732685d188e | -6.03495 | -44.37947 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e530ba59-2136-33ad-a203-87473e28852a | -7.55497 | -47.78078 | 2026-10-07 16:03:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 16d39e54-1569-33b9-9a10-614bfc9bf45d | -7.16966 | -47.7964 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4a81cf64-9ad4-3be8-8a4a-c19d5b380371 | -6.42231 | -44.83677 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f7906d43-a89c-300a-a48e-2d5789b74718 | -3.87511 | -44.12949 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fda59450-5c49-3edf-9a11-6e0f40b64619 | -7.38137 | -46.54853 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34671a25-df28-3465-98fd-3eea9004b563 | -1.09115 | -48.05418 | 2026-10-07 16:03:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b3375b67-0517-308e-b22e-6888f6c0ca35 | -7.29266 | -47.28919 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 7d747252-e32a-3830-ba0e-a2879e04423f | -8.03307 | -46.97628 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2014f922-75a7-3534-be9c-abdb003e9034 | -3.35552 | -39.85531 | 2026-10-07 16:03:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| d5c491fc-d185-3f38-b10c-9e33b4b62d87 | -5.23716 | -48.39957 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0d22816b-ab23-33d9-9a2f-a8b05b3faff6 | -3.27466 | -39.65649 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9ab73934-c3ed-3861-b048-f88d2efab82d | -7.69585 | -44.73697 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ce48758f-9887-3280-97ca-f27b9c405f51 | -7.27571 | -45.57198 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b00159b6-8234-3057-9794-0b0b7535556b | -7.03546 | -45.42509 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 70edf764-3a37-3366-b5f8-c229b5619925 | -3.8765 | -44.10999 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| cc7702f8-0400-3a46-82fc-c8b66f58eb7b | -2.41713 | -46.03239 | 2026-10-07 16:03:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 271b5f2b-1e7d-3a0e-8af1-6c9fb32b4a5b | -7.1733 | -43.71094 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ae25483-a02d-36c3-9c9a-c343336c5d1e | -4.74134 | -49.75286 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f7d4ccfd-94b2-38f2-8ff3-fa52acbd4427 | -3.70081 | -44.94187 | 2026-10-07 16:03:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3be24c23-680f-3d7b-a6d2-692a03f7e38e | -3.76972 | -44.35524 | 2026-10-07 16:03:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9f4186fb-a377-371e-a822-ab2beacee98d | -4.20645 | -44.61686 | 2026-10-07 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| aad6aa8e-11f8-3462-99ad-3b48b3bcb38e | -3.77842 | -41.87658 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| b2444768-b0a0-3b3d-b428-7134f5af1c41 | -5.0984 | -42.92587 | 2026-10-07 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d4963715-7bee-36f7-a54d-0893a2754bfb | -2.97392 | -41.41353 | 2026-10-07 16:03:00 | NOAA-21 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 68439bb8-32e8-3e2f-958b-45150faff8f4 | -4.63073 | -48.86053 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 926022ef-de5f-34fb-9353-70d9dd9b25fe | -4.62812 | -43.49992 | 2026-10-07 16:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ec9b4c43-db2b-36d9-a227-12e7247472fe | -6.89642 | -45.89626 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 78f67b1c-6743-3c23-9bb5-99e1c6ccb89e | -3.00792 | -43.83993 | 2026-10-07 16:03:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 423f4a8d-0ca5-360c-8cd6-fe7fffb8719d | -6.76474 | -50.96554 | 2026-10-07 16:03:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5d6f906f-b7d8-346c-8ea8-e4201c4244d4 | -7.16914 | -47.79272 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dd504acf-0a16-356a-98a0-7c4ddf57536c | -3.22817 | -40.02676 | 2026-10-07 16:03:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 4f8449c6-d3e8-32e8-a6c0-3c3d3db71bc4 | -7.83178 | -45.49958 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| deec048f-5e7d-3e51-be5c-624d17b3fb7a | -5.98327 | -40.93829 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 69c66a49-38d1-374b-968c-e22546bc6706 | -6.71146 | -45.77013 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0869f451-b9ec-392c-b5bb-4422ada46a0d | -5.96796 | -40.9324 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| f90c8e07-03ba-3199-a1cd-6f59186c697c | -3.66697 | -41.44614 | 2026-10-07 16:03:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 0cd8b18b-d92b-335a-b400-183937aa9c12 | -3.50656 | -41.93973 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |


[Clique aqui para ver as próximas entradas](README169.md)
