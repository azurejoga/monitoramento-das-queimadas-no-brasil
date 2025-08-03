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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cfd6da6-935e-3af1-869e-a1bbeaaaec88 | -12.3993 | -43.4869 | 2025-08-03 00:18:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca8f8a64-11ec-33ba-89e7-0449c06e4ae7 | -22.566601 | -46.372398 | 2025-08-03 00:18:00 | METOP-B | BUENO BRANDÃO | MINAS GERAIS | Brasil | 3109105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 755235f5-cc14-30f7-9363-f9fcda2f9201 | -6.5582 | -51.0989 | 2025-08-03 00:18:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04cd65b4-0a5c-3e9a-aec5-05ae8cb97832 | -4.539 | -44.197701 | 2025-08-03 00:18:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2fa474-a360-3032-bf83-0b7c66436a5a | -12.5978 | -44.488998 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cce6763-f948-350e-9950-7ec15fc7448c | -4.2891 | -48.107899 | 2025-08-03 00:18:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cefe3e77-53ff-36cf-87f5-f255951ba5fc | -12.6141 | -44.513901 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3f6afd-74ee-36f7-a821-711e3fedd21c | -13.6544 | -41.3624 | 2025-08-03 00:18:00 | METOP-B | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0cec6faf-1337-3984-adbe-d751554e0b69 | -21.6952 | -47.701099 | 2025-08-03 00:18:00 | METOP-B | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d12a3fe8-491a-35f0-9a67-2b70bf46d0de | -14.1579 | -45.459599 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee3594f-832f-39a3-967a-dafb272d290a | -20.0079 | -46.431702 | 2025-08-03 00:18:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 438b4d4d-2f0c-3e97-a3c4-1cb0596d82ec | -7.992 | -43.181099 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a09f39ab-4aa7-30a1-a6c6-f5cbe4592846 | -11.9254 | -44.964901 | 2025-08-03 00:18:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f945744f-c037-318b-942f-46119e04c428 | -8.9163 | -46.754101 | 2025-08-03 00:18:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06632360-deb8-3655-bb13-13225f8a04d8 | -7.9761 | -43.1581 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ba2a1ba-43f8-3ad2-8ea7-f98ea4d41ede | -6.5598 | -51.105999 | 2025-08-03 00:18:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7b94428-8f41-3d22-b861-923ff4b667c7 | -18.8262 | -46.4426 | 2025-08-03 00:18:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7b8a34d-fb7f-3ff9-a2e8-efebdb739867 | -11.0372 | -49.536301 | 2025-08-03 00:18:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31ce899b-c27d-3db6-849a-bd0fef819204 | -7.0948 | -43.476898 | 2025-08-03 00:18:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9796e59f-5a68-3c71-9ae0-5d08921acc42 | -8.0156 | -43.1082 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d8e36db-ce28-398b-aaa3-fe1fba1499b0 | -7.9828 | -43.1432 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67057da0-10ad-39e0-b404-1634bdde45a1 | -8.3147 | -46.917999 | 2025-08-03 00:18:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58d9547c-279e-3db0-8156-7cd6f573881c | -15.66 | -47.586601 | 2025-08-03 00:18:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| e5dc3201-9674-33dd-b786-5a8f292225f5 | -6.6246 | -59.090801 | 2025-08-03 00:18:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbf9accd-1fe1-3ffb-8637-ea4f8d18d620 | -4.5418 | -44.2099 | 2025-08-03 00:18:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69acba30-cc03-3ae9-a17f-932647b10664 | -9.3687 | -45.504101 | 2025-08-03 00:18:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c497fad0-fa95-3e1a-8051-3ad8122f5793 | -20.2215 | -40.244301 | 2025-08-03 00:18:00 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f8445c3-fee9-3ead-a72e-d7e740c17ff1 | -8.0254 | -43.1059 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 541d4bc3-7ab9-3a5b-b9fd-c5eccc80a4f3 | -14.3585 | -50.319099 | 2025-08-03 00:18:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5328aa5f-caad-39f4-a7d1-a65cf2438f60 | -10.3221 | -44.906898 | 2025-08-03 00:18:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 026814ce-4f88-3055-8255-3259c122b095 | -14.1426 | -45.438099 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12fb7cb1-545b-3243-9295-730c4b159ee9 | -22.019699 | -47.584801 | 2025-08-03 00:18:00 | METOP-B | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7330eea6-e0d6-3fd6-8be2-09d04db46e2b | -7.9895 | -43.128101 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7cf10584-e3bb-3839-bb90-7492ee2a621d | -4.5292 | -44.200001 | 2025-08-03 00:18:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb85499-531b-3cc7-b04d-8252dabe5a37 | -23.3675 | -47.5107 | 2025-08-03 00:18:00 | METOP-B | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa04a711-9692-3ed4-94ff-316a16d57c9e | -3.7906 | -42.546001 | 2025-08-03 00:18:00 | METOP-B | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad70a8c9-e585-380d-b6af-12d93b37c161 | -9.5347 | -47.880402 | 2025-08-03 00:18:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1123d3b8-4d66-3ded-9cf2-47e3e15fd591 | -6.6202 | -59.07 | 2025-08-03 00:18:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb645ad-64bc-3949-826c-dfb72217a525 | -22.267 | -52.108002 | 2025-08-03 00:18:00 | METOP-B | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30c7f580-53e3-3d68-aa25-07d4d2bed22d | -7.9992 | -43.125702 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89f3326b-28a5-3b0f-97c2-e66f6335ada8 | -14.156 | -45.451698 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d26959d-3291-3fef-acce-a3cf2aa8ed8a | -10.3242 | -44.9161 | 2025-08-03 00:18:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16e2f2d7-32d4-35ca-ae2c-c04330be443f | -7.0977 | -43.4893 | 2025-08-03 00:18:00 | METOP-B | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b77d9e8-2f57-3eab-b703-ff455b161b59 | -12.6173 | -44.4842 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4347496d-d071-36f9-b10e-14f2455815b6 | -4.5447 | -44.222 | 2025-08-03 00:18:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c503eebb-a607-3786-8e9e-3e5d8a0ed4c3 | -12.6369 | -44.479401 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 987c7f2f-d194-3d20-afd5-8ce027b82733 | -12.6336 | -44.509102 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98ce57cf-b4d4-3d16-945c-3e815a4f226d | -12.0214 | -44.020599 | 2025-08-03 00:18:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a49716d-29f7-369d-a207-fa84c4ccd097 | -11.0388 | -49.543301 | 2025-08-03 00:18:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4b53fd5-b004-32fd-8f6b-0ab16a9dc2be | -9.3785 | -45.501701 | 2025-08-03 00:18:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36babf3f-36f1-357d-b807-66bae423108a | -22.005199 | -47.564201 | 2025-08-03 00:18:00 | METOP-B | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 03597b26-eb2c-358b-ab20-3afadf11ad19 | -21.2491 | -48.374001 | 2025-08-03 00:18:00 | METOP-B | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 225d56ac-5923-3f46-8335-5e3f01d426bb | -12.6238 | -44.511501 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40cf3927-d1f4-37ad-a3f8-3f19c48defca | -12.0037 | -44.815201 | 2025-08-03 00:18:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 273047dd-8cdb-3d92-a384-8ce8ac62f62e | -8.012 | -43.136101 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dae24f6b-cea9-3ba5-813e-8babcfe0973d | -21.247499 | -48.3661 | 2025-08-03 00:18:00 | METOP-B | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ba82055b-cf7a-3fac-9b04-9e722898b98d | -12.6021 | -44.507198 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d49b821-f602-3a73-aeb1-7d9c0bbaaaee | -7.9451 | -45.107399 | 2025-08-03 00:18:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 14509bab-b7a8-3d44-a227-cea961ff0ad5 | -10.4397 | -50.2813 | 2025-08-03 00:18:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cb85ffa-9bd2-3af4-b1ab-264408f5e3a6 | -4.2972 | -48.098202 | 2025-08-03 00:18:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e05197fb-974b-3e6f-9891-c3b4b86980cb | -12.6379 | -44.527199 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8dab6bfb-8e09-320e-9a06-a4119981428c | -9.3368 | -50.737099 | 2025-08-03 00:18:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c775f545-cedb-31eb-bc12-6e84f05b7aa8 | -12.6487 | -44.486099 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ee5b97c-88dc-3b89-8c16-f3a179f9f541 | -8.0023 | -43.138401 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18eb9614-03c5-3297-99de-ecf5b4ce0268 | -19.976999 | -45.776001 | 2025-08-03 00:18:00 | METOP-B | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac514ddb-b663-3f8f-b7d1-c9851634d0e8 | -18.8148 | -46.437698 | 2025-08-03 00:18:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f0e18b90-8d7e-320f-babf-9b294f6e1976 | -12.6466 | -44.477001 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4774ce-a8ec-3fff-a108-f1d2d1f952c7 | -21.4373 | -55.0863 | 2025-08-03 00:18:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d193ea42-b3fd-3f2f-b092-4641dc3aafbb | -14.1542 | -45.443699 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23513556-d71e-346f-b9fe-fb460ed5186e | -6.1814 | -46.3405 | 2025-08-03 00:18:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1fa75643-b9d0-3d93-a763-287c598a0480 | -7.9859 | -43.1558 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 281d3768-0829-30c0-9087-557d48e98ed2 | -7.8589 | -45.530899 | 2025-08-03 00:18:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 61f9269e-d477-36a7-a980-3d6e76b3916b | -20.2183 | -40.231602 | 2025-08-03 00:18:00 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 719a6549-8ae7-356e-9033-7034a03606b5 | -18.827801 | -46.449799 | 2025-08-03 00:18:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4967f926-f339-3f36-9efa-a66ede7c1f85 | -9.3765 | -45.493 | 2025-08-03 00:18:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5485ebaa-ba97-3351-90b8-3ad18f314903 | -12.639 | -44.488499 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2bac2d8-fda8-389f-91ea-6b4f08e3abca | -12.662 | -48.0882 | 2025-08-03 00:18:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 686dbdaf-eef0-3527-bae3-b0b6d5454340 | -10.8006 | -50.476299 | 2025-08-03 00:18:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b28250f1-3ead-3adb-b8eb-ce6d4af6cdd1 | -10.8104 | -50.474098 | 2025-08-03 00:18:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c8bbd60-444b-32fc-a0ea-a56843556e87 | -7.9429 | -45.097801 | 2025-08-03 00:18:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 55cffc1b-8419-32a0-9bf4-d61ce54e40d9 | -7.9986 | -43.1661 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fa414832-5e68-393e-a303-da11aa48ef37 | -7.4919 | -49.7444 | 2025-08-03 00:18:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf26de70-5d1a-3c5a-a1a5-ccc212469d91 | -6.1834 | -46.349098 | 2025-08-03 00:18:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 698fab1e-53fe-380f-9d7e-2303a87c9cf9 | -12.0058 | -44.8241 | 2025-08-03 00:18:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c36952aa-0a96-39a6-a789-7ab033aaaa42 | -8.4083 | -47.4608 | 2025-08-03 00:18:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cede8fcd-02a1-3c26-8d71-180db3ff5495 | -7.9889 | -43.168499 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 10b69ebd-be3d-3dd6-a54c-7951bc727a38 | -12.6271 | -44.4818 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33b35c16-9898-3289-b0bb-ebc391f0d2c1 | -22.0165 | -47.5695 | 2025-08-03 00:18:00 | METOP-B | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d18dbedd-1428-34a4-a728-f6ef442d243a | -4.532 | -44.2122 | 2025-08-03 00:18:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea716879-071c-3ee1-8426-7c71adb29224 | -3.9654 | -47.998299 | 2025-08-03 00:18:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d84b3b0e-b872-3568-b213-4de0bbcc9aaf | -12.6476 | -44.524799 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70e6c929-b28f-38d5-b3e3-23eea1638423 | -6.7997 | -48.6357 | 2025-08-03 00:18:00 | METOP-B | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 66044919-0d72-3a70-8364-d8a3c229d9c9 | -10.8088 | -50.466702 | 2025-08-03 00:18:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd0b382-f1e8-36f5-ba11-ee51b7aee3f2 | -12.0093 | -44.0131 | 2025-08-03 00:18:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9ec55c1-2ab4-32ce-ac26-530cbfc0fe9f | -6.1854 | -46.3577 | 2025-08-03 00:18:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae1f6663-96e6-385f-9862-0838399cb077 | -4.7549 | -45.342499 | 2025-08-03 00:18:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bea81c8-6e2c-3bf6-94fb-dde58686080f | -7.9791 | -43.170799 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d77fde82-6a56-3789-97bd-07e619a81564 | -27.161699 | -53.390701 | 2025-08-03 00:18:00 | METOP-B | VICENTE DUTRA | RIO GRANDE DO SUL | Brasil | 4323101 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2c3ada8c-64a6-37b8-8e3d-c0fcd77db09c | -22.018101 | -47.577202 | 2025-08-03 00:18:00 | METOP-B | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 386dbd7e-27a6-3d3a-b7dc-b0fa99726d74 | -11.7743 | -44.936501 | 2025-08-03 00:18:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
