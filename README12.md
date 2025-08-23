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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44cb20f4-51be-37b4-9b68-bc83497c8a22 | -17.5979 | -46.5715 | 2025-08-23 03:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9b918d66-1e0b-323a-937b-c004e2345601 | -14.6706 | -54.9142 | 2025-08-23 03:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 6c6a46f9-15e7-34ed-b0c7-19dca2b6e662 | -7.0352 | -44.6396 | 2025-08-23 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b5efd3c9-1c57-3404-9d5b-12ec4f234b94 | -9.9681 | -60.1743 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| e1bf972c-6dbb-3319-9b90-2a73a2db534d | -13.3777 | -46.2208 | 2025-08-23 03:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 9c02c349-9287-35f0-a5c2-9af2d165d397 | -17.5985 | -46.5481 | 2025-08-23 03:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3850aff2-438c-3555-87c9-4a8797221788 | -8.5944 | -62.6126 | 2025-08-23 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2e2f8189-36ef-366b-8f91-5336599f93a6 | -17.5785 | -46.5523 | 2025-08-23 03:00:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9fa4472d-8724-3f99-896b-ad00bf84e858 | -9.5179 | -60.5461 | 2025-08-23 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| da40dacb-a996-3689-990e-add761a1eb47 | -20.4042 | -45.592 | 2025-08-23 03:10:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 49c86180-eb27-38f2-8cf0-a1d7fd76f614 | -6.37 | -45.5356 | 2025-08-23 03:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| b9be5652-2ec4-3ebe-88a7-f10d357b02dc | -7.0352 | -44.6396 | 2025-08-23 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 9e59db20-28f8-36f0-93c9-7e71a5a6ed53 | -17.5785 | -46.5523 | 2025-08-23 03:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 71ae86b6-2fd4-3a3a-8b2d-e98fa62c0f56 | -12.9921 | -45.2252 | 2025-08-23 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f5321df1-4dd8-3bc1-8a40-9c59ccf3108a | -8.5943 | -62.6315 | 2025-08-23 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c73f0a50-6a30-3f6f-9f54-53e693b986e9 | -8.5944 | -62.6126 | 2025-08-23 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 81a06554-e379-35ae-8cbf-631d5726086e | -9.968 | -60.1937 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| ef1af6aa-6c1b-3654-b36e-64795bae1b65 | -9.9495 | -60.1754 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 648db8ba-e5fb-368a-8ca8-268912a3e481 | -9.518 | -60.5268 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 40ee5ae0-aa04-34d9-ad56-d8f41e8a6e62 | -7.0164 | -44.6413 | 2025-08-23 03:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| e72adc73-b7a6-3695-bc48-8068a57d31fd | -9.5179 | -60.5461 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a8eb898f-0ddb-3cef-9537-d7ffd891bd25 | -9.5181 | -60.5075 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f1fa91da-8061-37f4-ba26-d9aa7c5a76cc | -9.5177 | -60.5653 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 83989961-1e5c-3917-b794-62afefe5acc6 | -13.3777 | -46.2208 | 2025-08-23 03:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3e60f5e8-308b-3ee1-a6a9-59f076d09785 | -14.6706 | -54.9142 | 2025-08-23 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| df73acd4-c29e-3771-a77e-6cc58e8107a8 | -9.1897 | -59.6171 | 2025-08-23 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| fa67a783-42c4-3524-9b61-96fe3c3a39a5 | -14.2936 | -58.5249 | 2025-08-23 03:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d98b016a-2a5d-3770-b9ba-bdc0e15ad8ec | -9.9681 | -60.1743 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 315b11c3-6fc1-31fc-8ecc-d5fb74e3dd0f | -9.9493 | -60.1947 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 279.1 |
| 26766d6a-4e35-3aad-a959-7a6c92b9cd07 | -17.5985 | -46.5481 | 2025-08-23 03:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| db4b6784-fea0-3625-b224-2f13930dfef9 | -9.9492 | -60.2141 | 2025-08-23 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f07da0ed-4d93-3a80-a83b-edaca7382ab4 | -6.6044 | -44.5624 | 2025-08-23 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 98edf388-4265-39f6-8d84-218a28fe25e8 | -17.5979 | -46.5715 | 2025-08-23 03:10:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7310fb42-ebe7-322a-b9d0-43850d256f78 | -4.98038 | -38.59887 | 2025-08-23 03:10:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d5071d91-66ec-3663-81dd-29a5f90451c9 | -4.52659 | -38.23298 | 2025-08-23 03:10:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c758b259-8428-3484-bc64-189847eeb6d8 | -4.97953 | -38.60371 | 2025-08-23 03:10:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| aba6e52b-5aad-3027-8f43-8f936d162c9d | -4.5274 | -38.22831 | 2025-08-23 03:10:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c36e6ae7-b8ff-3769-a818-e1140118086a | -9.33073 | -37.98263 | 2025-08-23 03:13:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5ab77500-f44c-3651-888c-9e73aafa0d98 | -9.79284 | -41.78407 | 2025-08-23 03:13:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 899a30e4-8e5d-33dc-af8f-be6e1e0443f4 | -9.33174 | -37.98105 | 2025-08-23 03:13:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f141f554-5404-360a-ac03-0317fc831b6a | -9.33107 | -37.98473 | 2025-08-23 03:13:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc2827db-9d86-363b-aea1-55cb2ebccca0 | -6.95047 | -37.3903 | 2025-08-23 03:13:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 63f09459-5be2-32f1-a7bd-df76826e2324 | -6.42256 | -41.22669 | 2025-08-23 03:13:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3e7355c3-5711-3b8d-9331-d3e4ef051bac | -6.9544 | -37.39461 | 2025-08-23 03:13:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4be68ec3-205b-3e77-8a1f-4a88fa2f1a10 | -6.95508 | -37.39091 | 2025-08-23 03:13:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2e77f5fb-80fd-340f-b6d6-de37efee4bc2 | -6.41687 | -41.21809 | 2025-08-23 03:13:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 12e3ef73-2140-3292-8a70-cc264567fea2 | -6.94952 | -37.38997 | 2025-08-23 03:13:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9fc62023-b43a-3653-905d-6bbca913c3aa | -6.43091 | -41.22108 | 2025-08-23 03:13:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c3369cf4-4464-3730-8b47-c68abada6f55 | -6.4239 | -41.21956 | 2025-08-23 03:13:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 90d17673-ac22-3e48-88e2-b86a44474995 | -6.94884 | -37.39365 | 2025-08-23 03:13:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3d7a296f-e499-340a-af11-24299ecbba23 | -7.2463 | -39.27437 | 2025-08-23 03:13:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 283045f7-e788-321b-8e7e-1a80aa75f7a3 | -7.2441 | -39.27637 | 2025-08-23 03:13:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8807ecba-cf83-3653-b7bf-fe4e643472ae | -6.94982 | -37.39399 | 2025-08-23 03:13:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3027604d-e492-3823-816e-58b44aa0d286 | -6.42521 | -41.21253 | 2025-08-23 03:13:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6a849fb9-24d9-3419-b87e-c7cc38165ba9 | -7.24506 | -39.27131 | 2025-08-23 03:13:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 57f6c788-ac6a-385c-bd9a-2e526748c92a | -15.53059 | -41.69227 | 2025-08-23 03:15:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3806b306-af94-3440-bdb1-4f86f8d408f2 | -15.90721 | -42.3073 | 2025-08-23 03:15:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7fcbd643-7fda-3d5d-84e3-98f72335845e | -15.71225 | -41.93097 | 2025-08-23 03:15:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 305b378d-6095-3fc6-a44a-251dd4b8009e | -18.05044 | -42.95852 | 2025-08-23 03:15:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a39fe057-0875-3112-a66e-366f410c9e2b | -19.38175 | -41.44526 | 2025-08-23 03:15:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 25d9901b-ee85-3b80-bb5b-e5fa3ceea3e6 | -15.71337 | -41.92586 | 2025-08-23 03:15:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| c21e6f83-0f33-332d-85c1-87bf14b82f59 | -15.52957 | -41.68568 | 2025-08-23 03:15:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 97dd5cb5-7312-387b-9fe1-a82042eaa7af | -15.90685 | -42.30544 | 2025-08-23 03:15:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| c7784994-d072-3f85-814b-2050c16485ba | -15.55893 | -42.68746 | 2025-08-23 03:15:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| fa93ceba-18e9-3364-adc2-b774dba594ca | -19.38291 | -41.4443 | 2025-08-23 03:15:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7582b9bf-9145-3d74-ad1e-b504fed4c4d1 | -15.7071 | -41.92437 | 2025-08-23 03:15:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9c68814a-c4b6-3999-bb75-159117d2de47 | -15.90823 | -42.30276 | 2025-08-23 03:15:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e92890b7-dda3-3584-b81e-638bee19744d | -15.70599 | -41.92946 | 2025-08-23 03:15:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| bf2f5f79-6219-3857-bba8-91a896c62373 | -15.53467 | -41.69218 | 2025-08-23 03:15:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0536d6e6-2c95-3ad8-829e-38a75ad0e7a7 | -19.38389 | -41.43994 | 2025-08-23 03:15:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e73494b5-2f52-3b2c-9e62-ead8f5359cf9 | -18.05173 | -42.9528 | 2025-08-23 03:15:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 452c005f-fdab-3a94-8254-316d7c42b290 | -19.38269 | -41.4409 | 2025-08-23 03:15:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c460a902-09fb-31de-99af-1ce731a4b187 | -22.02898 | -44.09453 | 2025-08-23 03:17:00 | NOAA-21 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ead2acce-3b68-3a2d-a46d-9dcc3016bb1d | -22.47006 | -44.27933 | 2025-08-23 03:17:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d47295cb-af0b-304a-9680-d23df63f5db1 | -22.42179 | -44.50389 | 2025-08-23 03:17:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e81e85c5-9a58-338c-8792-b138fd8db187 | -22.16874 | -43.28691 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 141e50b5-349b-3225-b6e5-57728797310e | -21.96134 | -45.59193 | 2025-08-23 03:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 89ea25bd-8691-3ac1-9c40-7208cacbe74f | -22.1533 | -44.59822 | 2025-08-23 03:17:00 | NOAA-21 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ae2c4da7-c121-3508-b083-ac5b23922e7e | -22.53331 | -43.72836 | 2025-08-23 03:17:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 811bb961-7354-30d9-bdf5-544c8c7fc151 | -22.42322 | -44.4981 | 2025-08-23 03:17:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| cdb94044-b6cf-37b7-8fb6-73d1a54fbaf1 | -22.17233 | -43.27169 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cf8179e9-f120-3bdf-bb4c-356a35662dc7 | -20.44638 | -42.13047 | 2025-08-23 03:17:00 | NOAA-21 | SÃO JOÃO DO MANHUAÇU | MINAS GERAIS | Brasil | 3162559 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2ab86918-21cd-3c99-8a91-160e28f40fe7 | -22.12383 | -41.38053 | 2025-08-23 03:17:00 | NOAA-21 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed0b18a9-f159-36d9-b9a2-c91bbe351c40 | -22.19022 | -44.55715 | 2025-08-23 03:17:00 | NOAA-21 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| e8d039c3-d89a-3b6a-8051-62e66eb864f1 | -22.90467 | -46.39261 | 2025-08-23 03:17:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 700d7576-d7d2-384a-b8cb-2319b5fd71c7 | -22.47788 | -44.27473 | 2025-08-23 03:17:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 06f685d8-99ec-304d-9f33-a8770a8a4d7e | -20.39261 | -45.44639 | 2025-08-23 03:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b7ef52e9-d99a-3d0c-b5d6-0716c3e9c679 | -23.49416 | -46.00229 | 2025-08-23 03:17:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 927590e5-b5c3-332f-b4c2-ee9e74d9636c | -22.09425 | -45.03049 | 2025-08-23 03:17:00 | NOAA-21 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b739217f-86e9-3a8f-b27a-ec67d8532644 | -22.47651 | -44.28037 | 2025-08-23 03:17:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a32fa2ac-240e-341a-bec1-b03f1db0847f | -22.03069 | -44.09648 | 2025-08-23 03:17:00 | NOAA-21 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3b0c58bc-a2ad-3c24-a3e7-422788ad4ea6 | -22.46877 | -44.28463 | 2025-08-23 03:17:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| caa09b94-9f86-306a-ae71-3afa80dc7e5b | -20.39958 | -45.44818 | 2025-08-23 03:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b4e074d5-737f-3a11-bca9-8b463318bc53 | -21.96616 | -45.60168 | 2025-08-23 03:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bbf73dbe-572b-30c6-9e05-510161c33586 | -20.44218 | -42.12204 | 2025-08-23 03:17:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 655a340b-14f8-33a7-b65a-2dc0379ec917 | -22.17477 | -43.2883 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5c240ee4-1c0e-330d-8eea-8f91f72f4162 | -22.05664 | -46.04744 | 2025-08-23 03:17:00 | NOAA-21 | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8980c7c6-c818-3571-811d-8e762d08ac41 | -20.39526 | -45.44639 | 2025-08-23 03:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 39f9696c-8151-3f82-be15-677c146a02ae | -21.97795 | -44.94642 | 2025-08-23 03:17:00 | NOAA-21 | CAXAMBU | MINAS GERAIS | Brasil | 3115508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3838859a-65e6-3847-8b28-eb8d553b63b8 | -22.02782 | -44.09939 | 2025-08-23 03:17:00 | NOAA-21 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |


[Clique aqui para ver as próximas entradas](README13.md)
