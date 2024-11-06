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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24ed5190-ebcd-3b00-8dd9-f8a58d22798c | -0.39378 | -51.99261 | 2024-11-06 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 165ea831-b6c3-36cb-988f-a63c5878bc62 | 3.61391 | -51.30577 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 506c6e70-29cd-3b2b-a7aa-776d5f2febeb | 3.61442 | -51.30886 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4aa71848-6b95-3108-a7ea-618e31b685db | 0.17972 | -51.06726 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e207e1a6-908d-35fd-b290-17d3cfe86f58 | -3.55187 | -59.86771 | 2024-11-06 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f9758b1-8b8e-3354-aeb6-714e171bf1d9 | -1.28954 | -54.56471 | 2024-11-06 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 820f0343-bc14-35bf-850f-ec0a7d81c1bf | -4.73278 | -48.96885 | 2024-11-06 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4b9d1a6f-414d-31d2-a612-5449839b327e | 0.18581 | -51.07008 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 392d8171-a91f-3010-bbbd-219d06b1a6e1 | 0.18586 | -51.06998 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eaceb71-881f-36ed-a91b-cc06cfc9553a | 3.6098 | -51.31286 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e8125634-2c3e-301c-b1df-c2b3cfc71430 | -4.41356 | -59.52922 | 2024-11-06 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 277c080a-be73-341e-9211-3c0f59e97a64 | -0.39852 | -51.99661 | 2024-11-06 05:29:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52d0969b-2ef5-3298-8650-12ac7e302468 | -4.44713 | -50.69367 | 2024-11-06 05:29:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d84dbe-791e-30cb-bab0-4411f1b53221 | -4.21495 | -53.56663 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d37daa30-7897-324b-b73a-28f46665a12b | 1.03866 | -60.54184 | 2024-11-06 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f4cd4c5-47a8-3023-b014-f08cbf04338c | -0.85254 | -52.8376 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2328d492-d8be-3742-9b68-95d198bfffff | -4.73954 | -48.96981 | 2024-11-06 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bc370fc4-c6e7-3a78-bdf1-7947f8d7e077 | -0.8521 | -52.8405 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66a48133-776a-309b-b520-5f7ae6f95a7b | 3.34743 | -51.28885 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc5d1d00-268a-3ffd-a69f-60dc9a84428c | 0.17916 | -51.0636 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bd1f35e-790b-300e-a006-c5526632a2dc | 3.52208 | -51.2417 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f6d54d3-8cb0-352c-a639-4472d6fe327d | 0.97148 | -59.74262 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| badb38d4-a79b-37dd-9e56-cb9bf9fb9d26 | -1.06125 | -53.66114 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f5282f85-190b-3472-9f25-0792b65dedd1 | 0.17974 | -51.06716 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dcb1088-7eb8-32be-b104-f0f951dbfce0 | -5.11803 | -59.83005 | 2024-11-06 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f69b3ca2-678a-3430-b0d9-bfebdc02090e | -3.66262 | -58.58266 | 2024-11-06 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20cc82ad-2b4a-3819-94b7-230444e1ca4b | -1.39456 | -52.20206 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fc828a2-55d6-3cb3-86bd-a6844088dc00 | 3.60929 | -51.30978 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19ad1f24-80dd-32b9-889b-029a25c6664e | -0.96785 | -47.81049 | 2024-11-06 05:29:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 736ae182-1dee-37a5-8fa0-80d0f3cf8266 | 2.08115 | -60.83546 | 2024-11-06 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7b77d45-009c-3a40-b693-ab54289a01e7 | -4.73554 | -48.96548 | 2024-11-06 05:29:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9ce9b506-8c89-38ea-8493-41619c14b8a7 | 3.51174 | -51.2435 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcf4ffd1-67cb-31a8-ad14-d8f7692b5fdc | 1.05176 | -59.55932 | 2024-11-06 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d446cc5-448c-37b4-8a0a-b694fe89ef22 | -4.66588 | -50.9755 | 2024-11-06 05:29:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f559e540-d16f-30fa-913f-1974669007cf | -1.38932 | -52.20123 | 2024-11-06 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d926f745-37cd-33c2-be00-5ff93a16e015 | -4.2162 | -53.558 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7e248fa-4cfa-3085-8169-726fbc11fd79 | 3.51639 | -51.23948 | 2024-11-06 05:29:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6877970-5b95-353c-af25-90fa4f396438 | -4.22036 | -53.56446 | 2024-11-06 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c0bb441-a673-3129-bacf-d4005d978030 | -3.9213 | -59.62924 | 2024-11-06 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1bf5c3e-0118-3ec6-a888-f9b550b4c191 | 0.18409 | -51.05897 | 2024-11-06 05:29:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc200045-35c9-3250-a097-ca3874bbeb50 | -3.0396 | -53.2805 | 2024-11-06 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 18b8fe4f-7f76-3dd0-b91d-014a97c5003c | -3.0207 | -53.4227 | 2024-11-06 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 57a0758a-64cf-3f98-9b38-da64d42db3a0 | -3.0207 | -53.443 | 2024-11-06 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c25c3615-87f4-3894-8d87-a444b29464e7 | -3.2348 | -50.3904 | 2024-11-06 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ad934dd5-429a-30ec-9bbe-9ed231302357 | -3.967 | -48.15 | 2024-11-06 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 772214d5-d216-3220-a54f-7f08e5e1d465 | -3.5447 | -47.3636 | 2024-11-06 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 7424ec4a-f8ed-3cea-b40c-aba19b7084ea | -2.9186 | -51.047 | 2024-11-06 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 42279597-aa4f-3ff9-bf94-9728b5b43d51 | -2.8423 | -51.7735 | 2024-11-06 05:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 27c387da-e018-36c2-828e-cd030346ecb6 | -2.937 | -51.0673 | 2024-11-06 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3eacb93a-2fca-3941-a359-2e3f1650bef9 | -6.5094 | -44.6847 | 2024-11-06 05:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3917ad84-2f7f-3459-9172-c481bfe9d413 | -3.9669 | -48.1716 | 2024-11-06 05:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ad146015-e814-389f-850b-bde17212400f | -3.1616 | -50.2248 | 2024-11-06 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 77b9c1af-6521-302e-943e-73a134f62536 | -3.1617 | -50.2038 | 2024-11-06 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 9751b5e3-5163-3cef-a40b-b4d649f849c6 | -4.1432 | -43.5822 | 2024-11-06 05:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 42f7ab6a-5934-3c15-9ed9-c2d5f2f133ee | -3.0397 | -53.2603 | 2024-11-06 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 4235bc3c-8845-30ec-a5cf-236326c9b1a1 | -2.8506 | -49.4744 | 2024-11-06 05:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ebce0bb5-7e9e-3331-a753-fba766da2235 | -6.4906 | -44.6862 | 2024-11-06 05:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b7832128-b112-3abe-aed3-ffb26073cb05 | -4.1246 | -43.5833 | 2024-11-06 05:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 87892cd5-0dde-3bcd-ad22-46a0b7854bfd | -3.0023 | -53.4434 | 2024-11-06 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c5ab3332-3d72-31f2-a3c6-aeabcaa9f2f1 | -2.7243 | -54.1552 | 2024-11-06 05:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 0fb32e43-3084-3ff3-90f2-145134c1b189 | -2.8608 | -51.7731 | 2024-11-06 05:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 8d16216a-0dc4-398f-bc8a-5cc5262d3aac | -3.5446 | -47.3855 | 2024-11-06 05:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 1b086b3e-def2-31eb-badd-8d57dd68d2fe | -2.9371 | -51.0465 | 2024-11-06 05:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 50c5584e-2d11-3de2-bd53-8dcff82a6b78 | -6.5014 | -47.4813 | 2024-11-06 05:30:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8e8acafa-3d5a-3c2b-bf30-8dd48fa1ad40 | -3.71694 | -49.42928 | 2024-11-06 05:31:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62584766-d34a-35c2-93ec-6b1374b19986 | -2.82918 | -49.78124 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05998acb-d2ac-3f74-b5d0-bbfd3e8de750 | -2.87859 | -51.30711 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a1a5276-27df-3e73-bfee-b7d2626673d4 | -1.33182 | -54.60873 | 2024-11-06 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2922e7c7-8008-335e-bf73-9359855995a7 | -2.94002 | -51.05725 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 22039d55-2b6a-34b4-a620-75cb5f1adf13 | -2.97658 | -53.27517 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83c9f9bc-d19b-3075-996d-25c98ee7a4ad | -3.03357 | -53.26988 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e174403a-5598-3ce4-bcd9-d4822530b8f9 | -2.8248 | -52.9175 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c1562e52-e526-3e50-9185-fae8310cc7b0 | -3.53078 | -50.34759 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d301266c-6e54-323c-b29e-8dc6dc6d1d7c | -3.66004 | -50.2354 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5831990-8744-3bae-bda9-94853c4f66bc | -3.6669 | -50.23156 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c0055e3c-04a9-3a69-83d3-faf5f366911b | -2.82152 | -52.90445 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8e9ab167-363e-3eed-85be-69677b8bc902 | -9.30105 | -68.25909 | 2024-11-06 05:31:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d1ef1e1-5fdc-347b-a236-4a3b1af92603 | -3.21206 | -53.1025 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 556f9d14-74ba-3bcd-b0ca-2281e61ee3ea | -2.84598 | -49.47083 | 2024-11-06 05:31:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e51ae19f-f797-3c98-9ccb-676983759e19 | -3.97097 | -48.16424 | 2024-11-06 05:31:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f62fb895-b77a-3442-bc7d-99a4f7dbc7d1 | -2.90241 | -54.24141 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c74ea4c9-fdfc-3490-9707-5af7d1e4a734 | -2.80988 | -51.49683 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3cdd2956-ddaa-3510-b540-50af261bad21 | -3.11446 | -54.16705 | 2024-11-06 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6cb69bb-07c0-346c-9a64-4863eeb07b5e | -1.94287 | -59.98944 | 2024-11-06 05:31:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 115c912f-e08c-3b17-bcb5-9b9ba6914fd5 | -3.16585 | -54.46264 | 2024-11-06 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34bd5d72-669a-3c00-b32b-7adf3a3ed120 | -2.67528 | -51.83307 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4680d6e-d73b-3703-b537-d419afe0ae6a | -3.21905 | -50.38319 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 04ca63ac-9a4e-349a-8f11-5f74340e606f | -3.42298 | -51.5402 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61318331-3a55-33f0-ae65-a9fb56dde556 | -2.83263 | -52.90001 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 979ebde9-e45e-3147-b81c-0043ec2224f1 | -3.09777 | -53.70926 | 2024-11-06 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6de720bf-62c3-336d-a175-91a3b3a3a5fb | -3.18984 | -50.5911 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4cd4ced-7762-329d-b4f9-93494f0d9bc1 | -3.45834 | -50.37438 | 2024-11-06 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e22979a9-806a-38ab-beac-2003b79c41c6 | -3.04368 | -53.27191 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6357bf9a-a9dd-3d8c-90fa-bbb25cbbbd28 | -2.81104 | -51.48897 | 2024-11-06 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7ae1432-0165-3484-bb19-58effc359431 | -2.8588 | -51.77617 | 2024-11-06 05:31:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d05f3b2f-e5a4-3a62-8037-6d7a3d4e0ccc | -2.83756 | -51.34845 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ee24ca7-e5b7-30a6-a728-f92b7a4a8f82 | -3.16214 | -50.20885 | 2024-11-06 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 35641345-622e-3ea2-835a-7c3a59c519f5 | -3.20863 | -49.22683 | 2024-11-06 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c089d638-68f8-3466-b66c-b31cb308ee18 | -11.79203 | -64.84903 | 2024-11-06 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 225cae8d-7b83-385f-b2ad-787e1e820bca | -3.23034 | -53.39821 | 2024-11-06 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README61.md)
