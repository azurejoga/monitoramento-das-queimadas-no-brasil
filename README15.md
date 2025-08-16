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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3682eaf-01e7-30eb-ba7c-fba232adddbb | -12.5369 | -46.9385 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 47dcc991-c7c8-31d5-8553-729e7389309b | -12.5947 | -46.9301 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b8a72a0f-8670-3044-b3a1-031c9e170b39 | -9.1523 | -59.6384 | 2025-08-16 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 07fdff2e-2971-3abb-b3e5-3e90e1f850e7 | -8.9706 | -61.7224 | 2025-08-16 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ab1ae509-5a3d-3487-bdda-508899568787 | -12.5365 | -46.9611 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 91cdfac2-82bf-3367-8362-5275c50c8459 | -8.9708 | -61.7033 | 2025-08-16 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 130.4 |
| b9e70212-6c19-3264-83c8-6e2ead218fed | -9.5179 | -60.5461 | 2025-08-16 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 73e8b57f-a2ad-35e1-8b01-9eebf7e2fc4e | -8.9893 | -61.7024 | 2025-08-16 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3bdfcb0e-2ce3-397c-adbd-c0a21637177d | -9.1709 | -59.6374 | 2025-08-16 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 6018a15e-e192-398d-9601-c865beae9845 | -7.9333 | -61.7471 | 2025-08-16 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| afa17250-df07-3608-a8cb-438cf11f616c | -6.9486 | -59.549 | 2025-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 12a7180a-fbe5-3078-9f7f-abfc84543782 | -9.518 | -60.5268 | 2025-08-16 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e113f47f-3eaf-3de1-9dfa-6449da5dd385 | -12.5562 | -46.9357 | 2025-08-16 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 6c40c458-f8af-3015-8b9f-28be681501c0 | -8.971 | -61.6651 | 2025-08-16 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 582956e6-f9d8-3e02-a401-21b5b17c9f08 | -9.518 | -60.5268 | 2025-08-16 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 0b155abc-a94f-341e-82cb-a85627c304fe | -9.1708 | -59.6568 | 2025-08-16 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 7579c73c-8f7b-3f3c-b9c5-7cb337a2f0a8 | -14.9632 | -54.7143 | 2025-08-16 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 5fa32b33-ea04-3adf-8ffe-816ffd994f46 | -6.6327 | -60.0033 | 2025-08-16 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3fca9505-b92a-3de0-9f98-989ad4d113c1 | -14.9438 | -54.7166 | 2025-08-16 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 7cf26978-6583-3b08-a7db-06f635024b05 | -9.1523 | -59.6384 | 2025-08-16 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 287990c3-11fc-3bce-bad0-5747b029b55e | -9.4994 | -60.5278 | 2025-08-16 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1710084a-3871-3427-811d-6fb938ecce11 | -7.9149 | -61.7288 | 2025-08-16 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 4c7b265c-5dd7-34df-8c93-e2f13f23fa5c | -8.9893 | -61.7024 | 2025-08-16 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 48c1c522-10b0-326d-8b94-3448c1b04bf8 | -11.2599 | -50.4553 | 2025-08-16 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d68a6c6a-fee4-321c-b4b2-096c37617dc6 | -11.2596 | -50.4767 | 2025-08-16 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| b9b1c82d-e207-373b-a74f-af63d35ba30d | -9.4992 | -60.547 | 2025-08-16 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a6ffd1f9-2f4f-3277-954f-a77d2ead96eb | -9.1709 | -59.6374 | 2025-08-16 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| d8894459-8e65-3543-aa23-73adb887b835 | -14.9628 | -54.7351 | 2025-08-16 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 49c7d55e-9dc6-3402-877a-29002608f980 | -14.9441 | -54.6959 | 2025-08-16 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 1f2ca179-b97b-3ece-99f6-0cbdd3be5fab | -3.8209 | -47.7444 | 2025-08-16 01:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6fdb11e9-b49d-37e8-bd59-b325c916f6b0 | -9.5179 | -60.5461 | 2025-08-16 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c4291f77-defd-33c5-a44c-cd7648fab400 | -7.9148 | -61.7478 | 2025-08-16 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| c8adbc20-efba-3336-ba90-27ad4509aba3 | -8.9709 | -61.6842 | 2025-08-16 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 26eeb37a-06ae-3caa-b39c-fe63c0ee4281 | -8.9708 | -61.7033 | 2025-08-16 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3074aa54-1714-3b83-ae44-9a67bc74cebe | -7.0796 | -59.2351 | 2025-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d8d6718d-c23f-3493-8c42-2c92a6abba82 | -7.9334 | -61.7281 | 2025-08-16 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 47f3f54a-35ba-3421-bfa2-3e53b8e34872 | -8.971 | -61.6651 | 2025-08-16 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| dca2abfc-75d2-3ffc-9143-d3d4ec948918 | -14.9435 | -54.7374 | 2025-08-16 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b8438fa9-419b-31b6-95c3-6f3ebaf936b8 | -13.4294 | -43.6733 | 2025-08-16 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 89c901ab-10c7-3a8b-9638-4f984466770c | -7.9333 | -61.7471 | 2025-08-16 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e7849ac3-015f-3e3d-962b-51c05548c750 | -6.9486 | -59.549 | 2025-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a2d057ad-be08-3670-9f17-259e00d343a4 | -6.9487 | -59.5297 | 2025-08-16 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0b3fcf24-d3a0-3317-88c6-a332da581bb7 | -8.9892 | -61.7215 | 2025-08-16 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4f06e2ff-2c50-32a7-b6ea-41632be3cc21 | -8.9706 | -61.7224 | 2025-08-16 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 74204e10-3620-31da-aded-3bf5efb8db25 | -7.9334 | -61.7281 | 2025-08-16 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9f7e717d-c1f5-38f0-8b1d-2936efaae2f8 | -4.9305 | -43.2558 | 2025-08-16 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5404550f-6ff1-3e8f-bc67-5a182a1d8a22 | -14.9628 | -54.7351 | 2025-08-16 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6b4965cd-aeae-392f-afef-8330049dbef7 | -6.5641 | -43.0122 | 2025-08-16 02:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3a91d756-58cc-3851-addc-20ffd5ea56d0 | -8.9892 | -61.7215 | 2025-08-16 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0ee9408a-f2f6-3123-92ec-c43937a5255b | -8.9893 | -61.7024 | 2025-08-16 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f18a7dde-5410-3f88-8da2-14607fd71bab | -9.5179 | -60.5461 | 2025-08-16 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1efcd895-83bc-3ba2-88dd-1cfbdbc11054 | -8.971 | -61.6651 | 2025-08-16 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0df26b95-aedb-3dea-abda-c1466ad30ad4 | -8.9708 | -61.7033 | 2025-08-16 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 4d147725-3bd4-3bff-a522-551627ec3ab9 | -6.6327 | -60.0033 | 2025-08-16 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| be9ea99a-1a37-37f5-9118-153be943e7ea | -6.9302 | -59.5497 | 2025-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 60c2778e-770c-399c-bb95-2f5c3b6fcc91 | -14.5828 | -47.905 | 2025-08-16 02:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 247ea868-6e33-3a63-a570-fe80e32913c3 | -7.9149 | -61.7288 | 2025-08-16 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 0a745f87-23fd-31f2-9d8f-8df2645d38dd | -7.9333 | -61.7471 | 2025-08-16 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d096b417-8ec8-3787-a96d-29a87fd59594 | -14.9632 | -54.7143 | 2025-08-16 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| da850134-9f7b-3e2e-8bf4-6c42d03a0ac3 | -7.9148 | -61.7478 | 2025-08-16 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| bffe1711-5737-34e8-a520-c75b9c4e3247 | -9.4994 | -60.5278 | 2025-08-16 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bffebb6b-224a-3dfc-abaf-e1518e91edd4 | -14.9441 | -54.6959 | 2025-08-16 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| a27b9cf3-8743-3da4-a2aa-67b62f05bc12 | -6.5638 | -43.0357 | 2025-08-16 02:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 29781471-a163-327b-8809-0b34a134f753 | -7.0796 | -59.2351 | 2025-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 09a7d15d-3585-3398-ae24-d87d0e479133 | -11.3466 | -55.4326 | 2025-08-16 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ba15a686-befa-3dda-be06-52a6f395bf7f | -9.1708 | -59.6568 | 2025-08-16 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 4dc46eac-04a1-3729-9a7f-92da59953762 | -9.518 | -60.5268 | 2025-08-16 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1a53f1ad-48f1-32ae-9594-82c1f068d2ab | -14.9435 | -54.7374 | 2025-08-16 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 513b7336-9450-3664-8cee-53ca426f66b5 | -9.2082 | -59.6354 | 2025-08-16 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 70eb79d1-7586-3cc7-95c9-cd814bfb3873 | -9.1709 | -59.6374 | 2025-08-16 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 2aa9fa55-8abb-3f49-9473-34ce47906e5f | -9.1523 | -59.6384 | 2025-08-16 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 57dc243d-e2d0-3e3b-ba52-bf87fa2ffabb | -14.9438 | -54.7166 | 2025-08-16 02:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 200.1 |
| b8da3b3f-630c-30b8-945a-a292d1ecb1d0 | -9.4992 | -60.547 | 2025-08-16 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 98c3460e-2323-3713-b2f6-0371958cb25b | -6.9486 | -59.549 | 2025-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4e41afa2-1466-3b08-86aa-4630472173ec | -8.9709 | -61.6842 | 2025-08-16 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 6d693910-e8e7-3e48-b0a7-2b414f5f4f8b | -8.9706 | -61.7224 | 2025-08-16 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1d4c81ea-7f27-3f0e-8696-21a515004fcb | -4.9118 | -43.257 | 2025-08-16 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 9be2b9ff-e5ae-3b0c-894a-a0acd40706dc | -6.9487 | -59.5297 | 2025-08-16 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e36158f4-9311-3005-b040-8ab48560ccfe | -7.50005 | -63.81424 | 2025-08-16 02:06:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 690b1ee3-684f-353d-a744-929e981ff120 | -7.92514 | -61.75423 | 2025-08-16 02:06:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 23bd8846-6db9-39c2-843c-5dda6035d425 | -7.92096 | -61.76181 | 2025-08-16 02:06:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 72af514d-3e20-37bd-b073-5002d48d758b | -7.62083 | -63.33644 | 2025-08-16 02:06:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| f76af44d-a0bc-3209-98c0-cd5a8d6b9293 | -7.915 | -61.72465 | 2025-08-16 02:06:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 17012acb-d1da-3408-8bb4-aaf1ce6b59f8 | -8.46632 | -64.06078 | 2025-08-16 02:06:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 332a4789-1d02-348d-acbc-c74611da24dd | -8.47147 | -64.05334 | 2025-08-16 02:06:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 31cb5435-683b-308d-b8cf-e856682bebe0 | -9.04603 | -67.43741 | 2025-08-16 02:06:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e14a8b32-fc91-335f-8ae4-760a04628565 | -8.9716 | -61.6925 | 2025-08-16 02:06:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 191.9 |
| 6b8c0ee3-8946-33af-989e-4bab95dfe475 | -7.90842 | -61.75703 | 2025-08-16 02:06:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 60332bf6-53cc-3e0e-aaef-365fcfd0c905 | -8.97754 | -61.72842 | 2025-08-16 02:06:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 94b166f6-d983-3f50-bfa9-41ba72e7530b | -7.91978 | -70.22665 | 2025-08-16 02:06:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 33586a93-71ae-3e51-93e2-43fc592733a9 | -7.62191 | -63.3429 | 2025-08-16 02:06:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0e6ba9f4-9670-36d0-bf75-4b3d5c384526 | -7.68054 | -63.32648 | 2025-08-16 02:06:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 964bbe0f-502c-353f-a728-bbb455606da6 | -9.04411 | -67.42446 | 2025-08-16 02:06:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a3e45f95-11db-31ac-9361-694768723878 | -8.66802 | -62.46454 | 2025-08-16 02:06:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0cef4c6c-19f3-33b3-b873-963964901a96 | -8.97692 | -61.68462 | 2025-08-16 02:06:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 101.9 |
| b820bbe8-f5fe-3697-947b-55dccb5f21e7 | -8.1551 | -62.78099 | 2025-08-16 02:06:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 9d758e67-ff89-36e6-837b-0e680429cb7b | -7.91891 | -61.71695 | 2025-08-16 02:06:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 36d9b397-2b93-3240-b403-570a7e854d8f | -9.03358 | -67.4261 | 2025-08-16 02:06:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 48bc8dd0-5674-3dff-b9c9-739c354a668b | -7.50427 | -63.84022 | 2025-08-16 02:06:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 4cc8ade6-501a-3452-8254-ed3def5c349a | -7.49817 | -63.82128 | 2025-08-16 02:06:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |


[Clique aqui para ver as próximas entradas](README16.md)
