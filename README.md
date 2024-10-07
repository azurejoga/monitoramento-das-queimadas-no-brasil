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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd20091-0c78-3945-92d9-ff935f73468a | -21.56 | -47.77 | 2024-10-07 00:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0fecd3b1-36e0-3776-919b-c6a3d03d8ff8 | -17.65 | -53.11 | 2024-10-07 00:03:44 | MSG-03 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f3157939-d3cd-378a-a70a-fecd4129d963 | -17.77 | -53.81 | 2024-10-07 00:03:44 | MSG-03 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a04c300b-27de-303e-9131-d10e0f81f940 | -17.77 | -53.75 | 2024-10-07 00:03:44 | MSG-03 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac5acf6d-0aa2-32dd-949f-5a062af5eb48 | -17.81 | -53.83 | 2024-10-07 00:03:44 | MSG-03 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4739c967-62c4-3447-ada0-2b834385f7fa | -4.27 | -43.74 | 2024-10-07 00:05:03 | MSG-03 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdfe7918-7956-3d05-97fb-3dc55e10d2b4 | -2.87 | -52.95 | 2024-10-07 00:05:11 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d28851d9-a55f-3af9-bc4b-882420894ef3 | -2.87 | -52.89 | 2024-10-07 00:05:11 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62ebf836-e339-3e54-902d-657f2f8e88bd | -2.9 | -52.89 | 2024-10-07 00:05:11 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 364c0626-3904-37d1-892b-c6f3454d09bc | -1.0182 | -53.739 | 2024-10-07 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 9573d4b3-0fd2-3aab-a48f-fd52ae195871 | -1.0182 | -53.7189 | 2024-10-07 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a4b74e74-447e-3c78-9d90-a78d392707e5 | -1.0365 | -53.7389 | 2024-10-07 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 4afd8c91-83f0-3415-baa0-0735d7a8e49f | -1.0365 | -53.7187 | 2024-10-07 00:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| eda30ab6-d7bc-3c5c-be3f-8b2fd73c4705 | -2.2113 | -53.7029 | 2024-10-07 00:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 58848108-0f8f-3f85-844a-8d3a2aef315f | -2.2114 | -53.6828 | 2024-10-07 00:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| e92dce02-0bef-387e-a1a2-389496900079 | -2.2297 | -53.7026 | 2024-10-07 00:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 122aad7f-aa64-3c6c-9afb-3ef5fc163cd5 | -2.2297 | -53.6824 | 2024-10-07 00:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| d9cddfc1-75f2-319f-93e8-73c16e71585d | -2.8569 | -52.9197 | 2024-10-07 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 1de50891-db97-34e5-8eee-c3821c7bd89c | -2.857 | -52.8993 | 2024-10-07 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 196.5 |
| 298a507a-434d-3e5c-8298-3f99bbbfd131 | -2.8753 | -52.9192 | 2024-10-07 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 307.6 |
| f0d3ced6-a370-36e2-98b1-e929d1e73169 | -2.8754 | -52.8989 | 2024-10-07 00:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 391.0 |
| de01ac06-759c-32d6-b874-7d285a8dcfcb | -2.8937 | -52.9188 | 2024-10-07 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 1ac9a5aa-a668-3f08-b5a5-bdf892c46b2b | -2.8937 | -52.8984 | 2024-10-07 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| c21b911b-f149-3c7b-af97-f58c41f873b8 | -4.2728 | -43.7601 | 2024-10-07 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 9f5ebed5-f327-368a-adf3-24f43befb184 | -4.2729 | -43.737 | 2024-10-07 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 275.9 |
| 3decd31e-ab3a-38ec-878d-d50e47ee595b | -4.2914 | -43.7591 | 2024-10-07 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 280fb7f4-f07d-35d5-a1c6-c7e1fb0f21db | -4.2916 | -43.736 | 2024-10-07 00:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 2096809c-6c0f-32b6-86f1-563e812e9ce6 | -10.8754 | -63.9169 | 2024-10-07 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0b0332ec-a5d2-3e2c-bf2e-7ebb6ecb46bf | -10.8755 | -63.8979 | 2024-10-07 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2982e24d-74a5-3aa8-bf6e-3b3c393291ea | -10.8941 | -63.916 | 2024-10-07 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1139f161-14c6-30e2-ba18-82c637b5acbb | -10.8942 | -63.8971 | 2024-10-07 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6f51f59e-8bb4-3e1a-b905-937bb303849d | -11.2467 | -51.3918 | 2024-10-07 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 12590ee5-4e49-317b-9cef-92ac7c552e15 | -11.2654 | -51.411 | 2024-10-07 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 52461a98-663b-3d80-9e1f-7d3322d1f212 | -11.2657 | -51.3898 | 2024-10-07 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b234c055-2aac-391e-88bb-32796300afd1 | -11.266 | -51.3686 | 2024-10-07 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| eb6f81fb-a8b7-3381-aba1-cb98f2ff215c | -11.2847 | -51.3878 | 2024-10-07 00:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b59508fe-d783-39f6-8e1d-7628e7384e61 | -11.7369 | -44.5159 | 2024-10-07 00:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 635d2241-72e9-3b11-8ce5-007310f63d6c | -11.7373 | -44.4926 | 2024-10-07 00:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 82f9f2ab-836d-345a-8e61-2e6572509a6b | -11.7561 | -44.513 | 2024-10-07 00:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| e88120d1-3804-3d7f-9108-35f7a1cb3eb8 | -11.7566 | -44.4897 | 2024-10-07 00:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 254.7 |
| cd92ace0-2aae-3f03-b662-cf76603bb404 | -11.8737 | -59.019 | 2024-10-07 00:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 3f15d1f4-8455-3f56-a9bf-2f34401e2c49 | -12.0585 | -63.7841 | 2024-10-07 00:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7e19c883-d54d-30de-bbae-fa166f6f46f0 | -12.0587 | -63.765 | 2024-10-07 00:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 81b93618-493f-361b-9ae9-5aeaa5f97b8c | -12.4973 | -47.0118 | 2024-10-07 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4a1a5cd2-b7e7-3bcb-85ff-d9485b7c6b4e | -12.4977 | -46.9892 | 2024-10-07 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 6a979bd4-0528-30d0-a1dc-0db5e72f4151 | -12.4981 | -46.9666 | 2024-10-07 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 5be79bfc-b98a-3147-a9af-32e5ccd41c85 | -12.5165 | -47.009 | 2024-10-07 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 59b32983-885a-360c-909b-8d026b268278 | -12.5169 | -46.9864 | 2024-10-07 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 222a12b7-0d38-389b-b832-66e3ea8d1ac8 | -12.5173 | -46.9639 | 2024-10-07 00:06:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6f29f199-d815-36d6-b84a-39a1f7a326aa | -12.7089 | -40.2155 | 2024-10-07 00:06:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 3c76997a-603b-3beb-a62d-73ef68e30e4f | -12.7284 | -40.2117 | 2024-10-07 00:06:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 83.1 |
| d5e51054-6680-38c8-8778-085b14db3266 | -13.5719 | -50.3223 | 2024-10-07 00:06:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cf83572d-b507-3f29-b205-31367e3be85f | -13.5723 | -50.3006 | 2024-10-07 00:06:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 5ee4a3b9-ea65-3e69-9844-a6ef9164a588 | -13.8354 | -44.6398 | 2024-10-07 00:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| e795845f-0d97-3761-8df4-1f1d6bc356d6 | -13.8359 | -44.6162 | 2024-10-07 00:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| a44affc9-0896-3c9a-b09c-78793569f1ff | -13.7342 | -60.6471 | 2024-10-07 00:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 1f61db46-cd2e-33e4-937f-ba9e9ec7e434 | -15.0422 | -51.24 | 2024-10-07 00:06:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 17dd2144-c740-335e-a766-ad1132179787 | -16.4161 | -57.3211 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| cb3527ec-750b-3b0a-954f-1c85b04c07c9 | -16.4164 | -57.3006 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| d518d2f1-9ada-3995-9cae-8e6d270fcdd6 | -16.4356 | -57.3189 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| aa534272-5e75-382f-9d3b-e4f9f8aa3fde | -16.475 | -57.294 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| f2c7d554-ba3f-3089-a3a4-77637acaa0cc | -16.4753 | -57.2735 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 1294557d-fc05-38be-86dc-d28e0c6c5b63 | -16.4948 | -57.2713 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| ecd993d7-4b63-335b-a5df-12ccfe57faf6 | -16.5072 | -57.7387 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 123.3 |
| dd2070e9-a7f7-3e13-9cff-76d5f4aeca8e | -16.5267 | -57.7365 | 2024-10-07 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 169.9 |
| 1666a86c-1fce-3351-99ad-1391c5687c11 | -16.6199 | -55.5684 | 2024-10-07 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 48274cd1-9a1a-31ba-a549-087d68ad613d | -16.6731 | -55.8934 | 2024-10-07 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| a92f4843-dd10-3edb-bf14-3b4400045432 | -16.8178 | -57.8466 | 2024-10-07 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| e4e65b16-cc49-37e9-920c-3a95a4db4d75 | -16.8181 | -57.8262 | 2024-10-07 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| a15f677b-beab-30a1-a7aa-b88c889338ea | -16.8377 | -57.824 | 2024-10-07 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 7d31f964-b6b8-3e1a-8843-03c261e0700d | -16.838 | -57.8036 | 2024-10-07 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| a0d2f96b-008d-3516-9838-fc35cca4866c | -16.8547 | -56.7375 | 2024-10-07 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| fd53c369-4af8-3727-94d3-20249a806c65 | -16.9711 | -56.8058 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.1 |
| 72435caf-ba07-355e-add8-d86827f55f10 | -16.9714 | -56.7852 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 6984c2ce-21cc-3c76-8ec9-b6e017edb73d | -16.9717 | -56.7646 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| 960e9887-8cd0-3376-af00-88efb257c5e3 | -16.992 | -56.721 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| ba39843c-e783-3495-9853-2955fadafd54 | -16.9924 | -56.7003 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.3 |
| f56550c7-288f-30b0-8e80-3e7017546d34 | -17.0196 | -55.1 | 2024-10-07 00:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 131bd959-c4a2-38a7-b255-2ee4a2d56a0a | -17.02 | -55.0791 | 2024-10-07 00:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| d62b3091-7791-3852-8c3f-8ce4411109fb | -17.0116 | -56.7186 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 164.8 |
| fb0fdb15-838c-3c68-b119-02cad39a1e2c | -17.012 | -56.698 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.8 |
| ec696a14-dc47-30e8-834c-e9609d6d2aa8 | -17.0123 | -56.6773 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 7c068ccd-64ae-33ef-ab26-3fdb644325ee | -17.0319 | -56.6749 | 2024-10-07 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 341aa445-c440-3699-b093-011ab55e1959 | -17.1581 | -57.3582 | 2024-10-07 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.0 |
| b6ca7e1b-ddd6-300a-8bf9-24aec262bcea | -17.1584 | -57.3377 | 2024-10-07 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 476ab6a7-3136-3352-a1a3-210675d39cc8 | -17.3149 | -55.0603 | 2024-10-07 00:06:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 108.0 |
| fa2bda3e-7790-3588-b7eb-ae6a87661cdb | -17.3153 | -55.0393 | 2024-10-07 00:06:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| a990bad4-11b7-3f7f-abc1-6ff0bc5deca3 | -17.6283 | -53.088 | 2024-10-07 00:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d38b7eb9-cbd0-3a12-97e4-9f373918673b | -17.6481 | -53.0849 | 2024-10-07 00:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 260.4 |
| 99759041-acaf-3423-9da9-b451c18c359c | -17.6485 | -53.0634 | 2024-10-07 00:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 455c93fd-eab8-3f00-b3fa-d3e6b45771e9 | -17.6679 | -53.0819 | 2024-10-07 00:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 157.9 |
| a9bab54f-4bb5-3e4f-8db9-750fedbd1fa4 | -17.6684 | -53.0604 | 2024-10-07 00:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2c329465-d9d0-3401-ac6f-efc645e65bd0 | -18.0192 | -42.1166 | 2024-10-07 00:06:45 | GOES-16 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.9 |
| ec23824a-5568-3071-bd12-1439ce80dd32 | -17.7324 | -57.0833 | 2024-10-07 00:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 9c10173c-886c-36e1-a41f-93fc49f1c256 | -17.7724 | -53.7918 | 2024-10-07 00:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 521.7 |
| 143d164f-dd52-3db1-aa9c-efa38c9766b5 | -17.7728 | -53.7705 | 2024-10-07 00:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 311.4 |
| 036de30a-9b07-3af3-b391-62b0a0755140 | -17.7922 | -53.7889 | 2024-10-07 00:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 796.4 |
| f4f5cb4b-c7fc-331d-9239-7d3fb43886b7 | -17.7926 | -53.7675 | 2024-10-07 00:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 520.4 |
| faece27b-787d-3241-8716-4cf56de21959 | -17.8319 | -53.7829 | 2024-10-07 00:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1dbe7245-6468-34dc-b948-a09aa4a9419d | -18.6391 | -57.2578 | 2024-10-07 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.6 |


[Clique aqui para ver as próximas entradas](README2.md)
