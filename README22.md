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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed5b28b5-5eca-3587-bb25-ceeeecbf3280 | -2.0664 | -54.6395 | 2024-10-05 01:11:44 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40cf664c-3128-3f75-9567-32ffdfdfff48 | -3.0935 | -59.3559 | 2024-10-05 01:11:45 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 512b18fe-d29f-3d18-b957-cb9e4cc685dc | -1.8193 | -55.180801 | 2024-10-05 01:11:50 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 104e64fe-8237-3f00-aa1e-d7bc4d168054 | -1.1942 | -46.5935 | 2024-10-05 01:15:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0a189da6-ec88-38fd-9a5d-6d657b29d8a7 | -2.8829 | -50.7147 | 2024-10-05 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c9f4b02d-1bd8-3727-9b7d-089cddecb28a | -2.9014 | -50.7142 | 2024-10-05 01:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 8d12a0d9-9893-3785-91c9-74d04ffda96d | -3.1432 | -50.2254 | 2024-10-05 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2c8d6d54-80da-377b-8255-69c1d8f69734 | -3.2349 | -50.3695 | 2024-10-05 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| defd7528-588a-3b27-99c0-927678dc9357 | -3.239 | -49.3986 | 2024-10-05 01:15:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 6c3249f2-072c-30a1-9a0e-7084252128b1 | -3.2534 | -50.3689 | 2024-10-05 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| dc178b27-5252-3fd3-a40b-70216c221c7d | -3.2575 | -49.398 | 2024-10-05 01:15:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d331c827-df71-3c7b-9e82-ff343a027b3c | -3.2899 | -50.4516 | 2024-10-05 01:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 353632b6-cf35-3193-a902-5217b2f73ffa | -3.3083 | -50.4719 | 2024-10-05 01:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| ab9cb61f-789d-3ff9-9f02-291ddc2dce85 | -3.3084 | -50.451 | 2024-10-05 01:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| e6159017-65d9-383c-87fc-bba2164470c1 | -3.3127 | -49.4599 | 2024-10-05 01:15:25 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 2106fec6-4f73-3268-98a0-54bc4f9f9c70 | -3.4566 | -50.3412 | 2024-10-05 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 4c0ad1be-2088-3365-b125-dfb3ee0683a8 | -3.618 | -47.5352 | 2024-10-05 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e6a336b3-d37e-38bd-9e94-b6496a484611 | -3.6181 | -47.5134 | 2024-10-05 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 4742f05e-e184-3001-99cc-3af46f847d12 | -4.0794 | -47.9502 | 2024-10-05 01:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| fdf5ca41-ab47-3c3c-b86f-7d2656772256 | -4.9451 | -43.7888 | 2024-10-05 01:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 30c37100-c2ea-3f6c-9dc6-d168e58772fe | -4.9452 | -43.7657 | 2024-10-05 01:15:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f2ba06c8-8f40-3f52-bf1d-65e4dbb3d5f8 | -5.8214 | -44.1426 | 2024-10-05 01:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 773f9a6a-a998-3ccc-816a-6b6920f0f2ee | -5.8216 | -44.1196 | 2024-10-05 01:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 180.7 |
| c7898fb0-1f94-3096-8fbc-ff46e85d203e | -6.1838 | -45.4371 | 2024-10-05 01:15:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 87db486b-aa99-3167-bc0b-0eff5acd0a7c | -6.3311 | -45.6963 | 2024-10-05 01:15:42 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| de8fa660-9762-3c61-b4bf-d59b3ee7fc52 | -7.1346 | -59.3099 | 2024-10-05 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 56017e39-fe48-39b2-a8c0-e065f03fe854 | -7.1347 | -59.2906 | 2024-10-05 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 832f5376-1bd1-3f65-bd8b-23b64bd6fb06 | -7.153 | -59.3092 | 2024-10-05 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d5a47cb5-cb4d-3dba-875b-6d413901472d | -7.7362 | -49.2297 | 2024-10-05 01:15:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d5b7a47b-72bb-3471-a060-02dd41d01a76 | -7.7364 | -49.2082 | 2024-10-05 01:15:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 110.4 |
| c80c94f8-d885-3adb-9c7d-60b4f2e88c72 | -7.7549 | -49.2282 | 2024-10-05 01:15:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 3011b802-8fcb-3802-8343-687f809aab8a | -7.7551 | -49.2067 | 2024-10-05 01:15:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 023ce9ac-7a7c-32f1-9bdd-3fa92859b2b5 | -8.6555 | -49.1083 | 2024-10-05 01:15:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 564771ba-388f-367c-bfd1-169a9f80a3c5 | -8.7772 | -49.955 | 2024-10-05 01:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 815058bf-82e8-3218-a157-7c39891044f2 | -8.7957 | -49.9747 | 2024-10-05 01:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7bdd4a34-4806-3223-8aa9-05617e31437b | -8.7959 | -49.9533 | 2024-10-05 01:15:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7aa1b164-2d62-3146-8ab0-4ab5a56cf946 | -10.3126 | -50.5554 | 2024-10-05 01:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4c2eaef4-e332-30a2-8723-a66e21aff491 | -10.3129 | -50.5341 | 2024-10-05 01:16:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f7fef635-4237-373b-a8b1-4f22e6d345a7 | -10.4424 | -50.7336 | 2024-10-05 01:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 98ff5b7c-3276-3651-89a9-938e64199802 | -10.5943 | -64.024 | 2024-10-05 01:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6d5c1f4d-a8ea-3ae4-a050-a2f1ee27c510 | -11.0966 | -54.2336 | 2024-10-05 01:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 51a0a0e5-a79e-3163-95e7-cd0df1310820 | -11.1155 | -54.2319 | 2024-10-05 01:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| bfb56743-51f9-347a-95a2-4ab119003ad3 | -11.1158 | -54.2114 | 2024-10-05 01:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6e7f97d7-b109-3f12-89e3-ea93a0a37be7 | -12.7623 | -50.5782 | 2024-10-05 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 0a17b964-89de-3769-b4bb-554ca8a28be0 | -12.7627 | -50.5567 | 2024-10-05 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 184.6 |
| fafde8cb-55e1-34b6-aa3e-e08f2add5033 | -12.7815 | -50.5758 | 2024-10-05 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 23243b66-40f3-3c71-a873-b628d40a3933 | -12.7819 | -50.5543 | 2024-10-05 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 196.4 |
| d756b2ff-93e2-398f-aca2-a0f70dd01c6d | -12.801 | -50.5519 | 2024-10-05 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 095fb160-89fc-372e-9c07-83b2bb830a9a | -12.8202 | -50.5495 | 2024-10-05 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 6f4b5d3e-6bcb-324c-813b-a61f8569487a | -13.1351 | -51.1955 | 2024-10-05 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 166.8 |
| a6d092fa-ee24-3689-82de-4640a86a12f6 | -13.1355 | -51.1741 | 2024-10-05 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| f5169f99-6cf2-3981-adf2-c2f612a9e3be | -13.154 | -51.2145 | 2024-10-05 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b6ec98aa-c0e9-3bc1-94bf-7b2d74e18ff4 | -13.1543 | -51.1931 | 2024-10-05 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 298.5 |
| 2fe2fa5b-42a6-3625-a174-7513f5619815 | -13.1547 | -51.1717 | 2024-10-05 01:16:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 1c4c8897-b6ea-3037-8948-592de66424c9 | -13.1735 | -51.1907 | 2024-10-05 01:16:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| db0963a3-3541-3ecf-a0e1-f7cc82d589bd | -15.5597 | -57.4553 | 2024-10-05 01:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0ea800f3-18ff-3154-807f-fb413b8bf102 | -15.5791 | -57.4532 | 2024-10-05 01:16:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 122aa6c7-73fe-3062-9cc2-3196d543eeb8 | -15.7151 | -57.4184 | 2024-10-05 01:16:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| ecb5cff6-6916-3d93-be15-863dfe10b4fa | -15.7346 | -57.4164 | 2024-10-05 01:16:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 04399248-747d-3ed7-8235-37acf5b9d6d0 | -16.4155 | -57.3619 | 2024-10-05 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.9 |
| 459e6c53-8878-3c24-91c1-ca67266634d6 | -16.5345 | -57.2259 | 2024-10-05 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| d57c43d8-b8a6-3699-ab77-0c8e801643ec | -16.554 | -57.2237 | 2024-10-05 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 163.9 |
| afe5658b-2331-3399-b1fe-737b5ff7fe56 | -16.5544 | -57.2032 | 2024-10-05 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 67e62c2b-2ccc-3739-b372-66596b23a035 | -16.5736 | -57.2215 | 2024-10-05 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| cb3074fb-8826-3e07-98de-bdf89d7d51a4 | -16.5742 | -57.1805 | 2024-10-05 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 269.2 |
| 83e48d16-c133-3642-9748-25199e0fcb5f | -16.5745 | -57.16 | 2024-10-05 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 273.1 |
| 309d1f52-748f-34a3-b004-8e3cf1ad06da | -16.5938 | -57.1783 | 2024-10-05 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 40e48c5b-34f5-3532-9870-89171864ad81 | -16.6871 | -57.4536 | 2024-10-05 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 42dd728b-6649-37b2-a52e-7a453d703812 | -16.7452 | -57.4878 | 2024-10-05 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 043cf942-7184-388a-84a2-1989f3a534ff | -16.7647 | -57.4856 | 2024-10-05 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.2 |
| 8cc3ca56-f0af-3198-8e04-212617ca770b | -16.7843 | -57.4834 | 2024-10-05 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| eb010ff5-40b4-36ea-a874-c36a0b36418a | -17.4067 | -40.4548 | 2024-10-05 01:16:42 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 127.1 |
| 3830f3d4-aa7d-3f35-a9d8-8b840bbe9188 | -17.0888 | -56.7915 | 2024-10-05 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| dc559e67-df96-3f77-a231-3e12af9ead6f | -17.0892 | -56.7709 | 2024-10-05 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 421b9754-df29-349c-8c9f-6367fa789643 | -17.1381 | -57.381 | 2024-10-05 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| 0c2b3877-260a-3557-a393-628ec98ae22f | -17.1178 | -57.4244 | 2024-10-05 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.1 |
| b2216fd9-4def-37ea-8b8f-394e1966111a | -17.1182 | -57.4039 | 2024-10-05 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 222.1 |
| 09311969-1eab-379e-81c4-cbe5fbc95f70 | -17.1185 | -57.3834 | 2024-10-05 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 67f1c8d3-fe4f-3519-8d29-4cd494a5653f | -17.1375 | -57.4221 | 2024-10-05 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.0 |
| a8bc4c5e-d948-3944-b835-03135d5aaede | -17.1378 | -57.4016 | 2024-10-05 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 214.5 |
| 43ae4806-469b-316e-9a91-dd0e19c18ba4 | -18.6582 | -57.2967 | 2024-10-05 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| ccea4c8c-a879-3e0d-894a-0992c81a6249 | -18.6586 | -57.2759 | 2024-10-05 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.9 |
| 24bee6e2-6963-3b3b-ac26-fe31ec3768b7 | -18.6782 | -57.2941 | 2024-10-05 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 9a81d40e-9696-32f5-a022-6d1cba7f878a | -18.6785 | -57.2734 | 2024-10-05 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.2 |
| 96591c17-fe09-330b-8e5b-86cdce1c14f2 | -18.6981 | -57.2915 | 2024-10-05 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 802d0500-ab6e-3036-ab8e-41dcbe9f93a8 | -19.0944 | -48.2415 | 2024-10-05 01:16:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 331feedb-98dd-3b08-82f4-f2199471f099 | -20.5699 | -51.3948 | 2024-10-05 01:17:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.5 |
| cae3731d-93e4-33e2-9633-3a3b0c909f61 | -20.5904 | -51.3907 | 2024-10-05 01:17:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 180.1 |
| addad3bb-7082-3826-8408-ddf508d803f2 | -1.0626 | -47.9269 | 2024-10-05 01:25:12 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 01352e67-f946-3ad0-8c63-e12098a14967 | -2.9014 | -50.7142 | 2024-10-05 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 2042bcdd-4a37-3b88-b109-e751ef27a315 | -3.2349 | -50.3695 | 2024-10-05 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 61316e03-8d85-32a6-b9ce-0ec020b26214 | -3.2534 | -50.3689 | 2024-10-05 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| ac805d3d-7dfb-32e9-aa45-c4734e35c93f | -3.2575 | -49.398 | 2024-10-05 01:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0e003db4-9690-3c19-a9ba-30e2c55b504e | -3.2899 | -50.4516 | 2024-10-05 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 78d5ecd9-303b-3667-9c1b-324c0861a16a | -3.3083 | -50.4719 | 2024-10-05 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 43ae3e3c-2c9b-3862-b96a-59f3c1b60700 | -3.3084 | -50.451 | 2024-10-05 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| a425fe32-a966-3b25-9375-c4b86829f61c | -3.3269 | -50.4504 | 2024-10-05 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ad638d9e-40da-33c8-8162-d8437d8ddc48 | -3.618 | -47.5352 | 2024-10-05 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 28742a62-1ff9-36be-965b-d998f0772c0c | -3.6181 | -47.5134 | 2024-10-05 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| dc9ee5ec-c809-3942-b2d6-a7138ab4f212 | -4.0794 | -47.9502 | 2024-10-05 01:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |


[Clique aqui para ver as próximas entradas](README23.md)
