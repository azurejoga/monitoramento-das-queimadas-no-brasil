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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4373568a-5d88-32ef-b168-fa38a9bbadf5 | -9.29157 | -48.50393 | 2025-09-28 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bc73acc-dd8b-33e4-8967-1b24fa3845a4 | -11.36067 | -44.94303 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 979130ba-1bd5-34eb-a9d4-80388c9ee0b0 | -5.84418 | -46.99926 | 2025-09-28 04:25:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66064a2c-5bc3-3e6b-bb81-d1f9c6224273 | -11.99642 | -47.89832 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f430ad7-c08b-39f5-bf31-5c2465c019bf | -5.43398 | -46.65461 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9099f0d-2226-3f1e-a85a-0b304be3ac31 | -10.29808 | -45.40482 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b89e5e7-c001-3c52-b131-f7a2434f91b4 | -7.81112 | -47.00166 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 050719d9-2313-3016-8b5c-73b0e2886401 | -7.37425 | -47.03556 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 361009bd-bc1d-33a6-9890-ad879034b8d1 | -6.71897 | -47.20378 | 2025-09-28 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b58e1ada-e7ba-31b7-8034-cd8ced0a68a8 | -7.38316 | -44.30035 | 2025-09-28 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22c9a45e-f132-31ab-8471-f98003b2030f | -9.4529 | -50.89782 | 2025-09-28 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc898c0-f9fc-3c65-a216-7a698abfcbd8 | -12.40893 | -47.5035 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f62035-4948-3e97-94b9-f8c545e507a5 | -5.91125 | -42.93166 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d140c12d-d9b1-32cf-b5c6-145ac20377df | -6.78176 | -44.04505 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a18e379-bdd8-335f-afad-27aca596d906 | -6.75975 | -45.5256 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b3c68af-0ff8-33d3-987d-57c24169821d | -7.4483 | -43.17703 | 2025-09-28 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8e7940b6-a686-35bf-b42a-fe05c9e60a51 | -10.41695 | -46.15168 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cff0d2e-88ee-32e9-a435-4023d951be76 | -7.39967 | -44.44497 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ed96b3e-2f9d-3d05-a4bf-c2483db0a342 | -6.19247 | -44.50601 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86ed0c01-e59e-35f9-8999-2e96161de307 | -11.40884 | -44.90635 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0580025d-b332-3cc6-97ec-85cba90b2794 | -7.87136 | -44.5649 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0f28725-ed5e-352c-9509-1a40657431cf | -8.02049 | -49.74166 | 2025-09-28 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23904654-ed4b-3bfc-85cb-e19d641c0afd | -8.17108 | -46.40035 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 93110fb7-d7d8-3e85-b06e-4bbdb52f3630 | -5.64299 | -46.38585 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9121c4c1-f1e2-3e1e-bf66-a59d84eb31d7 | -11.79424 | -44.91037 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a6f8275-96a1-3720-8fce-1f6a47d5b920 | -11.70131 | -44.4173 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4503caa8-2659-3ccd-938e-7ffb6b832774 | -5.88749 | -43.19861 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 81ad7b06-0c54-3fd4-8895-a632f116ddb4 | -11.39276 | -46.9683 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efe68051-3ce3-331f-94a3-da257d4d0602 | -11.44005 | -44.98332 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f139bc0-a3e7-30a9-a798-53a8b6eb7e54 | -5.83898 | -45.87538 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97372485-bb84-3031-8211-1b625041e437 | -6.1622 | -42.81046 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f1408a94-c570-3504-88d2-9e08582e3c4b | -12.01469 | -47.89044 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc5b27fb-b3c2-3e0e-81cf-e1c88823ce67 | -7.76097 | -45.72515 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abe0ab9f-f832-3c4a-bda1-3bbb0bace85e | -6.61705 | -43.77322 | 2025-09-28 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55196164-be96-30cc-aacb-15501b863d51 | -10.00867 | -46.70036 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0193d27c-d4a1-3728-9a18-bf74d00e4362 | -6.52943 | -43.49566 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7279fb1-8e86-390a-b1c0-0ab0aff378cb | -6.90247 | -44.76181 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 334576e2-c698-3806-9ab8-e7687e529d48 | -8.21752 | -47.03098 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52f2fc9b-aee6-3dee-883a-7f55957bf180 | -5.96421 | -43.26814 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 494229f6-e6d4-39d4-831b-e2c8f895ce5a | -7.22411 | -46.61214 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41b7e112-6230-3afe-a649-a44457f8ecb9 | -7.06206 | -40.38684 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc11f41e-8586-3f67-8eef-d1ba75598e22 | -5.82732 | -45.60418 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50aee639-cd9a-3361-81b6-76359f309e77 | -6.45594 | -44.02434 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a603448-3add-3e4e-85ec-9d3351cbc958 | -9.08656 | -45.8638 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e416ddf2-ea3c-32d8-ba8d-101eccb754b9 | -10.18238 | -52.57414 | 2025-09-28 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 851d1302-23e7-36d9-9d63-25b5c9a4e49a | -7.24562 | -44.76215 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a8a2921-a1eb-31b7-ad12-5175da0582ab | -7.65678 | -43.90341 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10ac2faa-f511-3e01-8c4e-a26b0063e922 | -10.90802 | -45.7412 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e39f8b89-a398-3eac-b021-82ba851f2c11 | -8.27945 | -45.46529 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15715536-d515-3bc1-9fb2-e6bd837e6012 | -12.01525 | -47.88692 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f4f6706-fe65-3807-afe7-67a615fcb318 | -9.04999 | -46.72914 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2cf1bdb2-3675-3af5-8ac4-c6cdf4d9cd2e | -6.72871 | -43.72978 | 2025-09-28 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 684fbaae-f6f3-39c0-a5b0-e0329d56e56c | -10.12756 | -45.33329 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd3ec44b-c653-39f1-9f94-f6961ab0ab4c | -11.50468 | -43.53659 | 2025-09-28 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffcff731-b669-396d-af50-a2263769f326 | -9.61348 | -46.68691 | 2025-09-28 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0909e4d6-0fff-36cb-850f-bebd8d0e8268 | -11.35781 | -44.96248 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08c40e8a-74f2-3a3c-a0a9-5afd3ddec39a | -8.97264 | -44.91691 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec17cdc8-c1e1-3fbe-9827-667bca288e4a | -10.90297 | -45.75158 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 955ce848-0d2f-3841-b8d0-2aae4ab4652b | -10.42713 | -45.13402 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c594529-b482-33de-9ed1-3d276d123d53 | -7.70552 | -41.29052 | 2025-09-28 04:25:00 | NOAA-20 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e78969d6-90ba-35ad-ad36-68f6a3853ed6 | -12.95407 | -45.15048 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dba66cb0-4746-3be9-834d-71a5db64941b | -7.16401 | -44.45181 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e19895fb-b7a4-3fe7-97f5-db343c37f93c | -11.41207 | -46.95339 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09b358ec-4ceb-39ad-86ee-edf05fc8cbea | -8.50246 | -47.01209 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e505849e-b0bd-35d9-a4ec-98cd2149e3ff | -11.94177 | -47.94386 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e111cd5-6d00-3cb9-a623-fbe15d380380 | -7.04078 | -44.77188 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a08cdca-e029-37ca-8d28-7ac4520befdc | -7.62934 | -43.79841 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 846d32a6-25b1-3f53-ab3f-e91dd541c5b3 | -7.79673 | -47.02797 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6fdd4a1a-bc90-336f-a8fa-7f38a3853bf7 | -5.63934 | -44.93756 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 182ff262-5797-3da0-b03b-ee58fe046d0d | -5.55555 | -46.27245 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b22e831-86e6-31f2-a971-0222f8dfdf93 | -10.75973 | -45.38762 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4cedf98-3d92-31f1-be9e-c8254671b04a | -10.91799 | -44.80369 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 384c002f-e89f-3eaf-9aae-5c468d5d1c79 | -11.97835 | -48.01129 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba053c2a-da15-39c1-a871-53ec9d3e4ddf | -11.69114 | -44.43687 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 124a1de7-8462-3350-98fa-6221e881b41b | -5.91244 | -45.84124 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1f76be8-f7f5-3d1d-84d6-9138863a2e53 | -8.1722 | -46.41476 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fc3b4521-9c05-3a6d-bec4-a7d23604441d | -11.35213 | -45.04903 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb0aad2b-f2f8-3475-a70f-f5777824b0da | -7.37924 | -47.02562 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3456d19f-71c2-3dcd-9840-983a24d4551d | -11.96982 | -48.0028 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| de80892e-9905-3cb5-9389-f245865cbfaa | -7.02668 | -44.77343 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 776e7151-5d25-3328-984c-b6238fbe84e9 | -8.27331 | -45.46067 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 915b85d7-708b-3cbe-965f-29c4fb9c2432 | -6.15251 | -42.80043 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 26198121-c3f9-3223-96b5-848d452c1dbb | -9.9791 | -43.61168 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eedb15d5-1d81-3750-ae19-ac7fc4bf584b | -11.9889 | -47.88278 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b3c2a14-290e-3a76-b521-d0cd11da1d4a | -10.96847 | -49.57001 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ff7d6a3-4516-396e-ae66-a69205c39c3a | -8.81884 | -46.21053 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eb393cc-3f9e-3415-be8b-d47e59c78726 | -6.69015 | -44.57327 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2acf5d59-ddd7-3d6d-9e0d-fac0968bab74 | -9.05583 | -45.56028 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13024a3c-0157-3196-91b5-7718fd28c465 | -11.9511 | -47.97073 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f044ae2d-07f2-3501-bb44-f8e510ed614c | -6.04823 | -43.92162 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9bbe1f07-5d1b-3657-945d-469c501495ad | -12.88903 | -47.10332 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4e6c193-5382-308f-be97-fe8598971edf | -6.09454 | -49.394 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f3298733-fdbd-3d44-8c59-5f2c77355c8e | -11.78622 | -47.61852 | 2025-09-28 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40ae1458-d3ff-397f-921f-fbc90ec7b10e | -7.86334 | -44.57155 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41c53951-6984-388a-99ed-ba7a027b35fd | -6.27579 | -45.05794 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e635486c-f703-3d12-9bd2-9e9b84d122fc | -11.52072 | -54.31556 | 2025-09-28 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef490cf7-cad6-3713-92af-037063a120e5 | -6.42904 | -43.51322 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5499d5b6-20fe-3f52-b244-37ec2eca5ec7 | -7.10687 | -44.23278 | 2025-09-28 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aca6362-d3de-3b91-820e-384ea9a273dc | -11.36762 | -44.94418 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36d774c3-baa7-3ead-acf0-b4f8b92f2cf2 | -7.16775 | -41.71826 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README62.md)
