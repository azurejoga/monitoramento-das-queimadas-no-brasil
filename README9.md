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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cb6ce7e-32b9-3249-b95e-7fb78bc868ca | -9.4384 | -45.685101 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e75cac2f-72d4-3116-9ca6-a5cc7e68de6d | -7.5117 | -55.333599 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe61cdcf-618a-327a-b659-f8bc08b47f2e | -6.9001 | -55.708599 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc3b1c5-75a1-3e57-aa39-e77d1f416110 | -10.1519 | -45.736698 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 703feeed-59db-37b8-ace8-ae3075dba67f | -5.2551 | -55.9091 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 470921cc-aa81-32fb-97be-8c2d946d596a | -5.4822 | -57.151402 | 2026-08-31 00:35:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc2e81cd-4756-328b-b3f2-fd511800a0f6 | -7.9275 | -44.249599 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 345bb273-9533-3dcb-a779-d11a08f779f3 | -7.495 | -55.302299 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cecc88c-1a9f-36dd-a1af-822f0b1153b7 | -9.427 | -45.680199 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a844f35e-6e1b-35f4-bc07-36b9af7d7119 | -10.6274 | -48.6796 | 2026-08-31 00:35:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68bafd8c-f909-3006-8520-4fec1db7f645 | -4.3938 | -47.841599 | 2026-08-31 00:35:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa7f627-5a50-322c-9fab-e37368e8eaa3 | -6.9391 | -55.7005 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbb58af-06b7-3279-a408-f979dc012f05 | -3.5392 | -49.476398 | 2026-08-31 00:35:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 450c4d49-9f93-31eb-80c4-7b0c98e190ca | -5.2491 | -55.928001 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49768c8e-3abb-3573-b326-eb0911d8bdbb | -10.8394 | -45.360699 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfe09f14-eebc-33d4-9e54-eec807be6e26 | -14.7512 | -44.644001 | 2026-08-31 00:35:00 | METOP-C | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1812826-d27b-3a6e-b01a-39f5a706a31c | -14.5982 | -54.1157 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6202a42-26a0-3b18-b4a0-8f3cc4c9e43b | -6.278 | -53.332802 | 2026-08-31 00:35:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8def5a95-81a9-30dc-9bd8-7404e8724c75 | -7.2865 | -49.8437 | 2026-08-31 00:35:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1b7fb99-c4be-34d9-9b85-831a6ed84d3a | -5.2381 | -55.877499 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2183c39-2e82-324a-ac9a-291647c24d22 | -7.5251 | -55.348301 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31126368-d46d-3f47-b5c7-6688372fa8d9 | -11.9183 | -45.071201 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81d0036b-03ee-389f-890e-cad41173f577 | -7.9762 | -44.281101 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91468984-0e4e-3fc0-bf14-a3c62b9117c0 | -11.3617 | -45.2089 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b06debd-90cf-3c15-b160-00f5b247f59b | -7.6129 | -44.889801 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c7a7e92b-0b11-3994-a190-7bfa84f6d306 | -8.9344 | -50.189201 | 2026-08-31 00:35:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6b29f13-fc27-3cb4-8650-88f682bc1d3b | -14.201 | -44.585098 | 2026-08-31 00:35:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5c0c54e-7be4-3959-b237-573833100f64 | -7.2848 | -49.835999 | 2026-08-31 00:35:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 503f9169-2f1d-3bfa-9753-4cafd789f385 | -9.6693 | -50.883099 | 2026-08-31 00:35:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07fc1c6a-dd70-3839-abee-c759f0b3809c | -10.7316 | -54.0602 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33accafe-6c8e-35fe-b402-32591d7ead38 | -10.551 | -46.219002 | 2026-08-31 00:35:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26c6b7a7-d715-3d5b-9cfd-3033a30ad59a | -14.9059 | -46.904099 | 2026-08-31 00:35:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f6e76f7-4b50-365c-999d-009308e9cc63 | -13.1944 | -44.071999 | 2026-08-31 00:35:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6222d6e7-475d-3c62-88fd-ffec6bdcec0b | -12.9223 | -45.900398 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48b51945-2b04-39bf-a68d-b6e5ad803a2a | -12.0978 | -45.0443 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2a65aff-1bf0-31a4-bbb1-6f822bb9983f | -7.2882 | -49.851398 | 2026-08-31 00:35:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c300cd48-3403-3580-8b47-47a982541ff5 | -8.7471 | -46.448601 | 2026-08-31 00:35:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a78d2e4-c9b7-354f-8f31-74953dbc70d2 | -11.6786 | -47.6166 | 2026-08-31 00:35:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec6d7c2c-01f6-354c-a6f0-280ef557f064 | -14.1801 | -52.888599 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9613a4e-89d2-3e3a-b5f7-9709d8ce4b61 | -5.4506 | -47.547501 | 2026-08-31 00:35:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a002f646-fdb1-3b51-86f2-e4daacdb14ff | -11.2141 | -43.383701 | 2026-08-31 00:35:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 984d5795-ddda-343a-8630-d3556a0ae047 | -8.1368 | -45.500702 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2cf6171a-6275-3b9b-881b-84d3181f1fc9 | -12.1362 | -47.266701 | 2026-08-31 00:35:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 027d4358-9393-3842-8b9e-0b8d461aa40b | -3.4107 | -50.136299 | 2026-08-31 00:35:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3481524-11f4-36d0-adda-b27fac7010ef | -10.7503 | -44.8862 | 2026-08-31 00:35:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5921f0-0b25-3962-8e1c-fc319fb315c8 | -11.4967 | -46.938301 | 2026-08-31 00:35:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee48018-c12b-399f-8945-ed9e0ec4afbc | -8.4095 | -44.985802 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ad47895-e890-307f-abf5-578b68ddc4e7 | -8.0892 | -45.473301 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 623f131a-51bd-313d-bc6c-727dabf831c8 | -14.9938 | -48.170101 | 2026-08-31 00:35:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d3b5899f-e220-3c0e-b47e-fa3ecf22e75d | -8.4014 | -44.995499 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ffbce762-4b68-3fb8-b542-3244aa921b30 | -14.4399 | -52.557499 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97d32087-b1cc-36dd-a067-d706445f808d | -12.0927 | -44.9772 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3eaea8-4d27-3b86-b4cb-e9bdf597c3cb | -14.3954 | -52.537701 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d64719d4-c044-38d7-abb6-234508f3b071 | -8.329 | -45.662201 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f010221e-127a-3a41-be8a-450f0b2ad9e1 | -9.3225 | -40.230301 | 2026-08-31 00:35:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 93725c4b-a967-3dd8-bcbd-fa9eae286694 | -13.3683 | -46.928398 | 2026-08-31 00:35:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99f315da-392a-3949-983f-fdafc17c1096 | -18.310101 | -43.234402 | 2026-08-31 00:35:00 | METOP-C | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82dc4c0b-2e50-3d3a-9acd-15dee7d1a8e4 | -6.9038 | -55.726002 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bdf49e4-589f-35a3-9a64-9abb836652a7 | -8.9381 | -50.205898 | 2026-08-31 00:35:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 900852a6-defb-36fb-be89-104880f7e34f | -10.7808 | -50.861801 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe4469e9-0fd7-39e7-a4bb-f4c05a388f7d | -15.9023 | -56.2048 | 2026-08-31 00:35:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82216699-f42e-3c57-8f46-b96656603a94 | -11.2208 | -45.090401 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98c9d511-928f-33c8-8b7e-6ac5b4327fc7 | -5.2418 | -55.894299 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9172c1bc-e68f-37b0-b15b-26bb11cfcd2e | -3.5376 | -49.469398 | 2026-08-31 00:35:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48bc533d-9592-3054-ac90-fa5a9bfba808 | -10.7613 | -50.865898 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbe627d9-3f88-379f-9f93-2744a6eb9b08 | -11.2648 | -45.057301 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba4502e-82e1-379f-8028-70700fd3d4a9 | -7.6218 | -44.9282 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3d9b2fc2-beac-3a72-b0da-9e4adfe6fa13 | -12.1011 | -45.058601 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 946f1c85-96cb-3324-bbd8-a655df4b0b44 | -10.1438 | -45.745998 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1573b2b-08e7-3730-89be-3761a4203bdd | -7.9392 | -44.255402 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f5086ae-47f1-3770-af89-54578eef7e7e | -11.9247 | -45.0546 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 825c1a10-c789-360d-b8dd-2a2d3c2edc08 | -7.286 | -52.367199 | 2026-08-31 00:35:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e65798bb-443c-3fa7-9c83-ebb5cb369f27 | -16.285999 | -42.5798 | 2026-08-31 00:35:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1ead4f4-05bc-32ab-a898-71faae1f5089 | -15.4233 | -52.716999 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46a11e64-c2fd-3a63-8448-9f0e049906f0 | -12.9384 | -45.926102 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e468ed3a-7ff6-3c2c-8ead-c9559626c5e6 | -12.3879 | -46.456501 | 2026-08-31 00:35:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9c35f5c-1ce6-3981-9bd9-cd794171029e | -6.5989 | -58.6092 | 2026-08-31 00:35:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42be2363-5b79-346c-971d-36b3a07fe606 | -16.076599 | -45.723202 | 2026-08-31 00:35:00 | METOP-C | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3c089c2-74c4-353b-b8e6-a1a9825737a8 | -9.4221 | -45.658901 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79f28d8a-5044-3734-af5f-696a8da69f57 | -12.9529 | -45.944698 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e5d3a19-a401-3882-9c20-359bf1c8dda3 | -13.9317 | -54.431099 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a890891-fd57-3a5b-bba8-3b708c6f2c50 | -10.8015 | -50.670101 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e01dc4d6-76c6-3288-a24a-4a0ebe6dbb5b | -14.4274 | -52.545601 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 67a25803-ff72-352a-ad10-2a4d9e05079d | -11.8843 | -45.8241 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91732e42-98e1-3cd6-b860-0b22b3487567 | -5.2356 | -55.9132 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6fdf0ba-7cb1-3511-9812-f49f7fa07bfa | -6.4879 | -49.905998 | 2026-08-31 00:35:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6f6e547-eb97-33e2-bc46-327c166b692e | -10.7788 | -50.852299 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b5f4730-8bd6-3d2a-bfda-4d2316cde49a | -11.2258 | -45.112 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f9308a73-80be-37d9-b3e4-bfa765bb8aed | -10.1536 | -45.743698 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 68d35bff-4283-3e5f-a80f-902a71ba0292 | -12.9239 | -45.907398 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c91cbf50-6ae8-3157-b416-e63198ebd9f8 | -7.2837 | -52.5452 | 2026-08-31 00:35:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adf8ae04-b231-3c7c-9f26-2ddb72856d94 | -14.4345 | -52.5299 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47edd28c-fd16-36bd-8a51-824ddac4155f | -14.1944 | -46.568401 | 2026-08-31 00:35:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6bde0bbb-68cd-3a00-be5e-00ca8a33d48c | -11.1602 | -45.0513 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd56ba66-b3cb-3aa4-a284-0154606ecdb8 | -11.216 | -45.1143 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33366806-16d2-3382-9914-769e79d1c643 | -14.2027 | -44.5923 | 2026-08-31 00:35:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e565ed5-a50a-34a4-9c94-e962cfdc93be | -7.936 | -44.992001 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2dac131f-3214-33c8-8cb1-94a303c79402 | -14.5884 | -54.117599 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87e4c124-0d44-3ae7-9e78-943b160cb569 | -18.2934 | -52.667702 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c9826b1e-8cf5-3bf6-8d3d-f5b0a803b3be | -16.2763 | -42.582298 | 2026-08-31 00:35:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
