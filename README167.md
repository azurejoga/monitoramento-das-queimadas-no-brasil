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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a789cc58-abd6-3ad4-85fd-3f46f8e98cce | -7.04342 | -44.32316 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 85a9c1fb-e3d8-3589-ac2a-9e90be9e82a6 | -4.57496 | -43.88265 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ecfb873-4db9-320a-888f-e5df686de8a0 | -7.76681 | -43.81228 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| a4c82ae0-2c8d-3433-bdb5-053c9003e52a | -7.39153 | -46.21722 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4ba7c869-21e2-3058-8c42-53f874da7417 | -5.97081 | -40.95242 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 41.9 |
| a79ffd0f-4021-30ad-8e88-aee3f5e90928 | -4.51859 | -43.8042 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 98845bdb-96d9-363e-b82c-f06efa575125 | -5.73991 | -41.7072 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8f1507b1-c3f0-3ee6-a391-f87ad840fe33 | -3.76284 | -45.0556 | 2026-10-07 16:03:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 13b8644b-2b23-3603-aea0-4af596dee7cf | -3.66284 | -41.44267 | 2026-10-07 16:03:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 30f5faa5-9c77-3c28-a072-380f0a4a1250 | -3.0658 | -44.45197 | 2026-10-07 16:03:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| fdc40884-42ad-3fca-88aa-74e620a8c9b7 | -6.22546 | -44.83772 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2f7a4433-c601-3984-b310-97260f0deffd | -3.76208 | -40.76182 | 2026-10-07 16:03:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 62cee932-f452-3ac7-921b-7af02c5dbc2c | -6.31894 | -43.48349 | 2026-10-07 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3d3958f9-c020-3a46-95a1-18e40aab7853 | -7.18841 | -42.02341 | 2026-10-07 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 55cdbb08-be42-388f-baf5-f6450c6c785a | -7.29621 | -47.27403 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d9038c57-9c64-3856-ac3e-d86da15d7e67 | -3.86733 | -44.13443 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecc76573-bbfb-3770-8fd6-c2273087e669 | -3.95267 | -41.54125 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 117.4 |
| af64d5e0-094e-388c-bd86-4826934f641c | -7.46026 | -43.20862 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ec4bef29-ed3c-3ad5-819d-c2ca3f4c0292 | -5.73404 | -41.74352 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 25b6f6b8-60d3-3cc3-b2b8-ade497c2cdd4 | -6.43992 | -44.79699 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2fb85a14-ae62-3eb3-a147-c3549be02050 | -7.23767 | -43.7665 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f247673-b85f-3802-8efd-1df694a6e26d | -5.95248 | -46.38264 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1072b5aa-c44e-31e0-a07b-78ee3b82ec89 | -6.68812 | -48.20433 | 2026-10-07 16:03:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9947aa20-ad50-3e08-9565-a86e6a69843c | -7.55751 | -46.69821 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba0f2c77-70dc-364d-b3a0-03080df23a4c | -3.70221 | -40.83218 | 2026-10-07 16:03:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 255.1 |
| ce26ef95-5f7d-36f3-8c33-adb980f715a3 | -6.33821 | -43.82333 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e1c5382f-1469-3d64-8654-48ca6456afe6 | -7.87489 | -44.23064 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e5cc256f-bee4-3261-af9e-551c7ec5b2cb | -3.40196 | -43.99666 | 2026-10-07 16:03:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f380bf35-7597-3c9d-9d8f-ad9093cc757e | -5.94409 | -46.39567 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce2dc9f4-6447-304a-92df-f4172ddf8504 | -6.68685 | -44.9569 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b1c54247-74ca-38e4-a287-f159b6a42c61 | -7.28535 | -47.29029 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83f9e263-ecdf-3fcd-a651-e7d3479d1973 | -6.0271 | -51.72259 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8bad7242-2d9b-369b-8ece-4241885115ed | -3.94971 | -41.54583 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 285.4 |
| 9a46bb92-3f21-3816-b5a7-d78e9e374149 | -6.57915 | -46.11043 | 2026-10-07 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2f5df51d-5b2d-38f4-b7e6-681f7b12fa3b | -7.57841 | -46.19566 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c20aa386-6ba4-35f1-9368-15a751b1e01b | -2.78395 | -51.68455 | 2026-10-07 16:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e220110a-b6d9-3110-9858-352fd211f31c | -5.95833 | -46.38784 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fb49abdb-3902-3012-ac9c-8ef6ed9a58a8 | -3.94764 | -38.38438 | 2026-10-07 16:03:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d99b90dd-c564-3130-8a5c-f587cc912027 | -7.55445 | -47.77699 | 2026-10-07 16:03:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 422e977e-253d-3dcc-b87b-cd52c5bd0087 | -2.52739 | -47.44382 | 2026-10-07 16:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0aeb5ebd-c3f0-3427-b417-e6340d8426d8 | -5.27361 | -45.17062 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| aeeeb823-9962-34cc-95db-51a259dc6b33 | -6.94354 | -45.25671 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6be9a5ff-c7ed-31a2-9e70-3e9b821e371e | -4.26758 | -49.98738 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 45644394-ea19-3408-855c-e7627f207a6a | -4.11999 | -41.78593 | 2026-10-07 16:03:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 84007721-e747-37e5-8d19-dd13032cbdf5 | -3.00678 | -43.11465 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d5530769-9423-31ec-b1c4-b5774f4ce4b6 | -4.57136 | -43.88703 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d6876ce5-d5ad-38d1-bfb4-096ea66c808b | -3.19446 | -50.54736 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 59560f68-240b-38b2-95f7-d48c2876e6a9 | -2.94021 | -49.03607 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 569a7cb8-e2e1-3fcb-a3ee-b36a08ee653c | -3.54477 | -50.10286 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 557057cb-d82b-34f6-b92f-ad4fe108d965 | -6.98961 | -43.29375 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e5b7fe7f-bfd8-3eb3-8928-9ba07852b16a | -5.72107 | -41.73206 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 190.6 |
| 6ac57a77-4cd0-3c0a-b55d-cc7f72b11010 | -4.5689 | -40.72285 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 26a207a0-ff41-34c2-b8a6-f8bb9ceb465c | -5.72715 | -41.72237 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| e790f2a3-f8ed-32ea-a120-30b11da1c5d6 | -5.48439 | -41.40041 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 7152deee-54d4-3d78-9bde-f49da3780606 | -7.28223 | -46.16461 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d25483a4-cddd-3725-b301-2108325b0ba8 | -6.62142 | -37.88454 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 879f5723-f294-31ae-ae5f-e4f14a9fef2a | -3.7312 | -39.53116 | 2026-10-07 16:03:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 597d3b8b-2957-3c27-9111-71c1e999f90a | -5.7266 | -45.15734 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6988d137-33f0-3eae-90af-8388712a9692 | -7.27561 | -46.15355 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cecdc1aa-967e-3ee3-ba64-bad0c6a7820a | -3.28585 | -50.44238 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f6eb9df7-9d90-3d4e-bb83-d073e1342fc0 | -6.22038 | -44.15419 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fae02780-6f28-3829-ac13-2fe3ae14019c | -6.06823 | -51.65557 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dd393619-bb6c-34c9-ace5-7c9e2bdd7392 | -5.98153 | -40.92634 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 48595e28-384c-3dcd-987e-7089e516f36c | -7.35057 | -45.27203 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 57f6f4eb-4908-37bb-b962-f0ccac86fc7c | -3.26332 | -50.4197 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| acc954b3-7354-3179-9238-e254b613e839 | -6.67895 | -44.96751 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ce2006e3-ed30-3951-80ce-ce3de8d16e58 | -4.71484 | -47.93059 | 2026-10-07 16:03:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 50c68004-62e1-3d15-8036-894d0d200a35 | -3.56948 | -45.21455 | 2026-10-07 16:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bfc16bd7-d0bc-302c-8aa0-1da2476abc62 | -3.58402 | -39.14262 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 1ce3dea3-6523-33ad-a335-8ac8aebbf8ee | -6.94082 | -45.27185 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 1fd65100-9c8a-3896-af9f-6ac380f8a2bf | -6.14902 | -51.74027 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1e029c31-c62e-3c7c-88b4-04f28c5dbaa2 | -4.34251 | -43.79898 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| afc40556-106e-377a-93ad-a399cbe8a405 | -7.69653 | -44.74205 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 704b4a73-fc8a-3b0a-b5b5-415a12ac9917 | -3.94935 | -40.72579 | 2026-10-07 16:03:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 14.8 |
| ce98b924-761b-3c3e-a32b-166a5d002e8b | -7.25698 | -43.50734 | 2026-10-07 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| feee2c1c-bbc8-3a21-a317-6e81e9c22571 | -7.17386 | -43.71488 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9d2673a3-f325-3ba7-9bb3-f85f54f87902 | -3.29929 | -40.08881 | 2026-10-07 16:03:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5cfc11c4-e8f7-3a65-ba0b-021ab6f1ed5e | -5.2145 | -48.34032 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e05b3719-68d9-35bd-a06f-4376939caf22 | -3.51833 | -44.98732 | 2026-10-07 16:03:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3d23183f-0fc3-3de2-8a2b-af43d46970dc | -3.8912 | -44.12335 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| c70c2433-cd4b-3bcd-9b50-562a30690f9d | -7.28687 | -46.16101 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73c95a54-a662-3588-9ed6-6d44e1a633e5 | -5.73765 | -45.16781 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1e932db3-ddf8-343e-a362-b8f8ef043d7f | -6.33452 | -43.82766 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c72e8de2-a464-37cc-88a5-8ff73868e8fa | -6.79863 | -41.25064 | 2026-10-07 16:03:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 9907e688-4d5e-3406-93a8-07440f1ba4d2 | -5.47786 | -41.21761 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 1b4438c7-b11e-3548-a66b-46b9c6541a44 | -2.69095 | -49.04613 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 333d0506-054d-33df-a89f-6c2c8ae9246c | -5.10551 | -42.91977 | 2026-10-07 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e9d181ea-ad23-31da-b682-311b11085e2c | -4.32386 | -43.80981 | 2026-10-07 16:03:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 35ca5139-3b0c-3f16-b1b8-cde191567e19 | -3.73444 | -51.2092 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2e955dfc-db64-3859-bf37-f106142291dd | -7.21409 | -44.32473 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 359f6b4e-c906-3009-b09a-863bc1e97554 | -4.96524 | -37.96947 | 2026-10-07 16:03:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6c8dd674-64fd-3719-bd86-b014e2d4d886 | -6.95751 | -44.41439 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f0298a79-d64f-3d6c-a1e9-772d569b326b | -5.94749 | -46.3835 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 382cd9c3-3025-3c0b-a0bd-a91e24b17861 | -5.95874 | -46.39073 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 700080e7-6ebc-3225-8e5b-3c6baea9b36b | -7.76451 | -43.7961 | 2026-10-07 16:03:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 17eedcb2-80ec-31d7-bb1d-0b115b6fc31f | -6.48059 | -46.62002 | 2026-10-07 16:03:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9bed5a4c-edad-31ba-9ec5-e48bdf9ad79f | -4.11936 | -41.78175 | 2026-10-07 16:03:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 616b3c26-47f3-38b1-980c-096d20b18a47 | -5.96959 | -40.94434 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5319bb77-25d8-3138-9acd-780994e40898 | -3.94459 | -38.49753 | 2026-10-07 16:03:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 09981f87-3d71-389b-8614-8e1d4cce022f | -3.55981 | -39.13921 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 55.1 |


[Clique aqui para ver as próximas entradas](README168.md)
