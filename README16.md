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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b46c61bd-c515-37f6-a94e-d61f514e0535 | -1.80494 | -48.05969 | 2026-08-16 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6df1dce5-30d8-389b-b061-5c1bd0ef6df7 | -5.06104 | -42.91257 | 2026-08-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 609cef53-b481-3f0f-bdb3-44bf4b93f889 | -3.5578 | -49.20752 | 2026-08-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 305b3eed-4fbb-3992-bfa7-8b92c0a9b7bf | -2.5733 | -47.24709 | 2026-08-16 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eccb847a-03d1-3f22-a5e5-ae13778a06de | -4.10022 | -42.50155 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5ccac76-fac8-3efc-bd4e-48aa1989535f | -4.09067 | -42.50458 | 2026-08-16 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5e93e4be-ce4c-3d3f-89d6-2503913f8f8b | -4.10704 | -50.99342 | 2026-08-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d240f7ce-397a-3b9d-a06d-a72a6184b62a | -3.12822 | -51.70501 | 2026-08-16 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a69e322-ad3e-3a7a-81ff-372f10cb6fea | -2.76924 | -48.56955 | 2026-08-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69aa33b5-cb91-3ff5-b7ba-e7d1498b384b | -1.58633 | -50.43994 | 2026-08-16 04:38:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 549f3422-b36d-34a8-831c-670044f7eecc | -8.9415 | -60.5174 | 2026-08-16 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 50c27552-d910-3e1d-9e19-2fb8cbe86797 | -8.9785 | -60.5349 | 2026-08-16 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 553f4601-94c8-33c6-bc4c-c086fba27a48 | -6.8387 | -56.4344 | 2026-08-16 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9c3f2d48-2f8f-321c-9889-454b25f140c0 | -6.6194 | -59.0609 | 2026-08-16 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| eb93cd09-72be-3525-87ad-c8f2abb40148 | -8.9601 | -60.5165 | 2026-08-16 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 56720d56-1e6a-3e5e-bd91-4385d2f6807c | -8.4275 | -62.676 | 2026-08-16 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| e849e3c8-7d56-34d1-a64e-3fd19bd470bf | -8.96 | -60.5358 | 2026-08-16 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| a6ab6841-d499-3783-91d9-d46c8c927769 | -8.9787 | -60.5156 | 2026-08-16 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 733ecfcd-f78b-3a0b-a363-ff7df66f8bc9 | -6.7123 | -58.9412 | 2026-08-16 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| bd46028d-f4f8-313d-9233-5599ea244761 | -12.7017 | -48.4753 | 2026-08-16 04:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7f3b00e9-39c2-3925-a27d-4ccef2c1c0db | -6.6378 | -59.0602 | 2026-08-16 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 784e0338-46b6-3317-9388-4193beac6f3a | -6.3137 | -43.6178 | 2026-08-16 04:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8dd5292d-9f7c-3e1b-b4d6-b03f6a64041f | -6.82 | -56.4551 | 2026-08-16 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c7bce0e3-5c5b-37ec-93a1-3a319f366ea8 | -6.72138 | -58.9422 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9775d7d-c05a-3242-b046-ef6a8c94e3e7 | -8.42781 | -62.68065 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 1b85d471-4701-3019-8f0d-a81a8dca575b | -8.89772 | -60.55797 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5dd3f45f-a17d-3988-be28-b03c813a4af8 | -6.95556 | -59.29472 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8607ad53-0bd8-3bc0-aa92-0ea7f92f5cb5 | -6.86151 | -42.90039 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| eb273ab8-6ef0-3ac6-bee2-8674dc360ade | -11.51114 | -54.63638 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c09c7e7-2977-3ac6-911b-c62bd71caf44 | -8.44166 | -62.66953 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e2d876fa-747f-3ce9-9db0-b40eee2e5989 | -7.78653 | -56.29384 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 178f1e98-9132-344e-a8c7-933f61020e9e | -8.64145 | -54.695 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79a44333-966b-3646-b8f5-0139db67febe | -7.20603 | -43.15644 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 642c8549-9008-3c00-ab5b-7ac1ac7e47b2 | -6.21759 | -47.74691 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50608c09-8806-3036-87de-9aa3ce4c3ef3 | -8.95569 | -60.59776 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e22bd796-7961-3d6b-9c0a-29b157b89d89 | -7.46226 | -55.30822 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ad43163-9cb1-3e6b-a23c-8bb1eee77289 | -11.87288 | -51.95258 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 755777f5-305b-373e-a625-f2ed6e2db3b2 | -6.85045 | -58.96372 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3650a18-a0f0-3f3f-87bf-2229b12113be | -6.69159 | -59.06078 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc944874-424e-3d50-be49-3f7c2d8cef11 | -11.21517 | -54.8214 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3f8481e-cdca-37ba-b26b-985249a6a480 | -6.85399 | -56.4274 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca549eaf-21d4-343a-a0f4-8a2b3e2a2a61 | -7.55649 | -61.16978 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ee1f580-08df-358f-b395-5b7c4a61c62e | -9.29701 | -56.81778 | 2026-08-16 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c0f8eb2-7e76-3e58-93f3-d93cc1d394f7 | -6.70174 | -58.95965 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1cf9aa21-5899-3101-a4c7-461dbfcc16a0 | -6.42939 | -60.07235 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c42effb5-433a-33f5-b187-eabc55aff635 | -7.33879 | -59.59916 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59775915-4853-393e-96d5-9cd92ccecab0 | -6.6171 | -58.99839 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fc2263d-aadd-321e-8acb-ad85c239d0e3 | -9.06218 | -45.7856 | 2026-08-16 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b8cc0e9-53ae-3f75-93f6-7ec068e2c5c4 | -7.02319 | -45.91596 | 2026-08-16 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc2f0a6b-2ee4-3325-9472-79b51be7b112 | -6.8486 | -58.97407 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 267c1d78-f2f7-388f-849e-b722d6e941d8 | -7.26124 | -44.69789 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59b1e310-0934-3017-a60f-763ed4bec0c7 | -8.97855 | -60.53884 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b37b040-cc99-3e1a-8203-10f4d68d2a42 | -6.93139 | -43.63773 | 2026-08-16 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cc739ed-e6f4-3b89-8bac-d4144ad9ac8e | -7.61184 | -49.44255 | 2026-08-16 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7572b8ee-e5f0-37e9-acf7-94bfa933bd74 | -6.37564 | -58.31779 | 2026-08-16 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6360ba74-6194-394e-8c01-3c5d9026b223 | -10.72083 | -52.10747 | 2026-08-16 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59fbb320-5944-3ebc-b69c-338da2b226f1 | -7.34501 | -59.59638 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cc74050-0ff8-3e03-9700-dfa36d337110 | -8.64578 | -54.69281 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d39253-bb5e-36a8-8db1-297201492aac | -6.59671 | -58.98793 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01b2e978-f911-3fdf-bdf4-7bcf2bb85853 | -8.35246 | -45.98029 | 2026-08-16 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 22112c8d-1809-3e99-bc36-64bfed19d0ab | -8.9743 | -60.52983 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 00f05e19-1e41-31e3-8ea5-e9e7a3a03917 | -8.59967 | -54.70377 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efd680cf-3927-37b7-bc91-38585fbef4d3 | -6.05884 | -44.88335 | 2026-08-16 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be885820-0c8d-3937-bc50-455424138804 | -11.8723 | -51.95619 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 473b86fc-efad-3f1f-a434-dd8e491abdf7 | -6.82895 | -56.43752 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adc56ea2-b3df-361d-829b-da5c8310b72a | -10.25702 | -50.4263 | 2026-08-16 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 621dc0fd-1909-39b8-830f-0ccf95ea97ed | -9.4915 | -51.6496 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2d1b99c-04eb-3073-b33f-87104b2c0f3b | -6.697 | -58.955 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f6921ab0-e233-3990-b8e1-c467e8d9f728 | -8.66989 | -54.76436 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d59bd0a2-14a3-3c2e-870e-9a604f0bc612 | -8.94562 | -60.52467 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f74b64b8-db73-334a-a96a-12a55eea4f9f | -11.47761 | -46.59351 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5b26ea47-e318-3590-a710-c57873d946bc | -10.15382 | -48.08376 | 2026-08-16 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed533c8b-0752-3f8f-ac2e-69883a85874b | -7.34567 | -59.59262 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 34c56d5f-0fb6-3524-a854-25cf1d59c194 | -8.90271 | -60.56303 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7e673c4b-32f8-3fc8-b1cd-f4f3e23dc2d1 | -11.24977 | -44.89208 | 2026-08-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a24deb1a-cbc7-3837-9434-8ba5c6fb14be | -9.42682 | -60.3256 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bdd1210-18c5-37e7-885d-4a347a6c3c2c | -6.31236 | -43.61919 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 73ea64f1-e848-36e9-b500-dac1710cc8df | -6.62203 | -59.0644 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4507bb53-6aef-37e3-ae86-d76f4eb57244 | -6.83294 | -56.41471 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4bad4d5-ff48-38ab-9c46-33b19790525d | -11.96404 | -44.33506 | 2026-08-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 744a08d3-3578-39b5-b9db-8431ba9f98b6 | -11.08197 | -47.24919 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 121c7e11-4f1f-3d0f-ba20-65c082005e3b | -8.90013 | -60.6052 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cb6b4faa-07bf-3a1e-8690-ffcbe03f28fb | -6.29477 | -47.74768 | 2026-08-16 04:40:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7741d5b3-d4bf-3047-8cec-d92e6fe664d2 | -12.24091 | -47.01334 | 2026-08-16 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a8c27c9-5c43-35d1-8c9b-a380dd65e624 | -10.67937 | -49.00058 | 2026-08-16 04:40:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3a5d3c30-d3e3-3693-812c-0437c278ab65 | -6.61957 | -58.9846 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5947279-9fce-30ae-bc0a-78902119a4fa | -7.54951 | -61.17337 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d18c1a04-672c-3d1f-9125-477622176408 | -6.85582 | -58.96465 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8363858a-86e0-3de0-8bb7-5509b0fc0023 | -10.53897 | -44.85171 | 2026-08-16 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a2be530-2ceb-3ac7-a8f4-b843c1a8371c | -8.9479 | -60.51257 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 91bd0ca3-ed5f-31d3-be58-61391cedd2ad | -6.81849 | -56.46475 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| faae1f89-e735-38e7-970a-669f6e8bfc54 | -8.61173 | -54.6799 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 700f8285-7909-3c96-8789-3f77ab37dd23 | -12.46773 | -46.66964 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf667f33-632f-3443-b2a0-8fbc727551ce | -11.91205 | -49.33456 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f03000e3-1e08-3623-9e78-4030675db143 | -12.01406 | -46.42751 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4304bd70-1481-3c8c-b24c-a7d1dca221ef | -8.64405 | -54.70285 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eed173eb-d292-3bb0-9f5e-e59145fe65a4 | -6.84789 | -56.43576 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b87cbb4-da13-38e6-a64a-49ac744b308b | -6.6214 | -59.06789 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 997b77b5-9dd7-3faa-b85e-9903f1d118af | -6.78356 | -55.83654 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dff10b84-e63d-3890-a906-1f1917ee5868 | -11.45601 | -46.60973 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
