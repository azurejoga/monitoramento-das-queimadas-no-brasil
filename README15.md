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
| 185e4f3c-8929-3192-902d-4958d5073c0d | -10.0516 | -59.1013 | 2026-06-29 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c11b37f0-998c-3940-a2cc-9633e0b504a8 | -17.4442 | -47.1582 | 2026-06-29 16:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 1bdf685e-4d30-3933-b170-a0651849be09 | -12.2222 | -56.5467 | 2026-06-29 16:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d3a2be78-e9aa-3c34-a6e8-ab6bf551e11f | -11.8906 | -57.415 | 2026-06-29 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 52ed459c-3306-303e-87aa-7d56ab6fdd79 | -11.2148 | -53.833 | 2026-06-29 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| e155143e-1763-3ab3-9b21-a49d0b98638d | -8.0926 | -50.9431 | 2026-06-29 16:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f232f26e-0899-3a48-87c4-ba77a97b3eaf | -11.9126 | -57.1339 | 2026-06-29 16:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 32dd8688-81ed-3f50-a5d8-823f9bded954 | -9.3142 | -58.0113 | 2026-06-29 16:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d6ed9af6-1b84-30f9-8b4a-17f7d154d191 | -11.9533 | -58.6192 | 2026-06-29 16:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 499709a0-e890-3357-8ff8-f0333045174a | -17.712 | -46.7798 | 2026-06-29 16:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 810ae5b7-fccc-3f38-ae57-6161041fe845 | -11.875 | -57.117 | 2026-06-29 16:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| fa296504-7090-3bea-a684-ccd9976b3874 | -10.0514 | -59.1208 | 2026-06-29 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f8eeffbd-1c54-3f32-a7c4-7c072e542dba | -11.06 | -55.7597 | 2026-06-29 16:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 350.9 |
| ffb08833-edc9-3326-a368-1d767c6ca9f4 | -10.9882 | -49.5618 | 2026-06-29 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| da32ca38-2823-3916-8508-ba819d574ac9 | -13.2198 | -54.4356 | 2026-06-29 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4bdad02f-0fbe-33c8-83e4-6d3a5d33d127 | -11.0414 | -55.7411 | 2026-06-29 16:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| a31c06a3-860f-3584-b801-fd010d36a264 | -11.9286 | -57.392 | 2026-06-29 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 5e30452b-c13e-3f3c-99b4-ce0f624c21fa | -11.5085 | -56.1251 | 2026-06-29 16:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d7edd3ee-6131-3863-ab8e-9fab3fcac905 | -7.7845 | -48.1883 | 2026-06-29 16:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d65fb790-4a17-30f3-851d-35133ddcc8e2 | -11.9441 | -57.7091 | 2026-06-29 16:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6a8632a3-994c-3a6e-83b6-68360831adc2 | -11.8937 | -57.1355 | 2026-06-29 16:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 80e54095-2df3-3628-af86-b3e38e768668 | -6.8952 | -43.6833 | 2026-06-29 16:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 01b28ca2-5fdd-3dfa-ab25-41fc739f34c4 | -11.8748 | -57.137 | 2026-06-29 16:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| fcf938e4-6f02-32c1-abfc-59a9d4e5d866 | -9.314 | -58.0309 | 2026-06-29 16:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 34f980e9-c2f5-309f-bc5a-cf55f58ebef6 | -9.6037 | -56.9276 | 2026-06-29 16:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 187.6 |
| b399e453-b87e-367f-9e2c-357e8f8960e4 | -11.875 | -57.117 | 2026-06-29 16:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 1d03704b-40ed-3f1d-ad13-22e2d119df7e | -17.4442 | -47.1582 | 2026-06-29 16:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 233.7 |
| d3262ce8-b58e-339e-b4f5-727e2768e20b | -11.9128 | -57.1139 | 2026-06-29 16:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| aa85f17d-9f21-3e22-a576-409de104b00d | -10.0514 | -59.1208 | 2026-06-29 16:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b7f10a0a-a883-315a-99ae-4e87d9bcd5cc | -10.0516 | -59.1013 | 2026-06-29 16:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5d3af9f4-f7e6-3a3e-82d7-c067410c7ae6 | -11.9441 | -57.7091 | 2026-06-29 16:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f258e7cc-df0a-3131-b56a-3117e5bf48b5 | -12.4656 | -58.4612 | 2026-06-29 16:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 3b04520a-528e-3324-963f-f4e4f3a06ac5 | -11.8937 | -57.1355 | 2026-06-29 16:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 180.1 |
| 547d294d-e0a2-30a1-94bd-2229ddf66bbf | -11.9126 | -57.1339 | 2026-06-29 16:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| be0d911a-c027-3e2b-b6a5-a4572be16b1e | -11.8748 | -57.137 | 2026-06-29 16:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 20be2692-1f98-3630-bcaa-23d29342011d | -11.06 | -55.7597 | 2026-06-29 16:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 365.5 |
| fc630b18-e39c-351f-9ab4-a8f3f5a52e74 | -11.8939 | -57.1155 | 2026-06-29 16:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 348a35cf-1541-343f-bfdb-e08882091d04 | -10.313 | -57.1169 | 2026-06-29 16:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c001fdcd-d779-3ed7-8de6-51c75d895587 | -10.9882 | -49.5618 | 2026-06-29 16:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 02117bdb-1d9e-3560-8322-afe925ca8a10 | -17.712 | -46.7798 | 2026-06-29 16:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b01d5692-b3de-343e-a640-167e683ebe2c | -9.3329 | -58.0102 | 2026-06-29 16:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 0f8f033d-f6a5-31c6-8148-9de27d7fe65a | -9.6037 | -56.9276 | 2026-06-29 16:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 2b6a8f73-6f68-3de2-b18e-be309afda3bd | -11.0414 | -55.7411 | 2026-06-29 16:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e6c73ab7-d3db-3d08-a097-0026deacd18c | -6.8952 | -43.6833 | 2026-06-29 16:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 15ea6139-53fe-365f-b191-ccae8b3f0428 | -6.497 | -42.238 | 2026-06-29 16:20:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 98ab8cc8-5e58-3b81-81c3-01676d8662dd | -11.2148 | -53.833 | 2026-06-29 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 085f06df-fc83-3386-ac0c-64d8ed7a8167 | -12.2222 | -56.5467 | 2026-06-29 16:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ca5ec01f-9787-3c6a-b48c-9fd53ac4b94b | -6.8952 | -43.6833 | 2026-06-29 16:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 32f3fa07-9c98-36ee-a275-854f80b74154 | -11.8748 | -57.137 | 2026-06-29 16:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1473dbac-f9b0-3770-8109-967c3cc5b272 | -12.5135 | -48.2802 | 2026-06-29 16:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c6c1d4bb-6d96-3ace-b42f-dd4ca1fd19f8 | -10.2942 | -57.1182 | 2026-06-29 16:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a41fb045-1793-3945-800b-fa2b733b0351 | -11.8939 | -57.1155 | 2026-06-29 16:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 328cf068-f9ab-3f1a-8f4a-052a4c99ea12 | -11.9126 | -57.1339 | 2026-06-29 16:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 17e0d76c-81f8-3ab6-b888-35d0a7cd735c | -17.712 | -46.7798 | 2026-06-29 16:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 117.0 |
| d31e0f7c-1206-3c01-9ae7-e940bb05a30d | -10.2941 | -57.138 | 2026-06-29 16:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 63e0561c-9d81-37df-abb5-8c4e0c4e1c2f | -11.0414 | -55.7411 | 2026-06-29 16:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| d0a0367e-fe57-3c04-9806-815029abeb12 | -12.4656 | -58.4612 | 2026-06-29 16:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 80913275-5c6b-3d3a-a6de-49353c93324d | -11.9128 | -57.1139 | 2026-06-29 16:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1b1a6625-c19f-358d-9968-8be758635022 | -11.9533 | -58.6192 | 2026-06-29 16:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| a6334c4b-f501-3d13-8844-7be9ffc0d41e | -11.9284 | -57.4119 | 2026-06-29 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 34d4a680-1cf1-3e89-9a1d-29bd6c55250f | -11.2148 | -53.833 | 2026-06-29 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c83c8588-21f0-30f4-8ce6-4dd09e7047e9 | -11.06 | -55.7597 | 2026-06-29 16:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 424.0 |
| 287c5cd0-f91c-37ed-a0d5-4b0676e2d52b | -6.914 | -43.6816 | 2026-06-29 16:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a87a952b-4488-3cf8-9a09-dd377bdb961f | -10.0514 | -59.1208 | 2026-06-29 16:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 26af5b6f-3dcf-384f-a2d9-dc19aad2350e | -9.6037 | -56.9276 | 2026-06-29 16:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 159.8 |
| fb239fe0-3bea-3191-bb7e-a427ee7f7032 | -11.9286 | -57.392 | 2026-06-29 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 180.4 |
| e58304ec-cfbd-31ff-8a51-f8deee7634d0 | -10.0516 | -59.1013 | 2026-06-29 16:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 72583e7f-8979-369e-86ed-1325153a3591 | -6.497 | -42.238 | 2026-06-29 16:40:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 613603e1-e9af-37c8-b6ae-892b8e7cb7f8 | -11.9284 | -57.4119 | 2026-06-29 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 5ca972b3-008f-3492-b562-283b53049db0 | -6.8952 | -43.6833 | 2026-06-29 16:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 8655af54-d322-3782-8930-2fa2f17b6467 | -11.9128 | -57.1139 | 2026-06-29 16:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 172940e0-47cb-3e8c-8c41-0f462777134a | -10.9882 | -49.5618 | 2026-06-29 16:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e196f0c7-eef7-339c-9a16-0ba21d7ebd0d | -11.06 | -55.7597 | 2026-06-29 16:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 297.6 |
| 8d921733-e68f-3c87-9b93-8a4e22d70645 | -10.0514 | -59.1208 | 2026-06-29 16:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a6dc79ad-d40b-3605-b76f-d5e65c04fc36 | -11.2148 | -53.833 | 2026-06-29 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 589c5fd8-4f68-3eaf-bb24-9dad02d6a53b | -13.2198 | -54.4356 | 2026-06-29 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e4f4957b-abb6-39b2-819a-d65accca4cf1 | -9.6037 | -56.9276 | 2026-06-29 16:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 189.3 |
| c26ff156-3152-3994-a427-502b5ffd7012 | -11.8748 | -57.137 | 2026-06-29 16:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d4bcf45d-ba7c-339f-9548-42c688c13308 | -10.9886 | -49.5402 | 2026-06-29 16:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 3995c2da-9a42-37fb-beba-71baf66ab25d | -9.3329 | -58.0102 | 2026-06-29 16:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 025eacbc-535f-3004-9bd0-8b0f5b575f58 | -6.914 | -43.6816 | 2026-06-29 16:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 75e1d49c-79fd-3f57-9a95-fd34362824c5 | -11.875 | -57.117 | 2026-06-29 16:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c15a4a5d-4763-36a5-89a8-e3b4a9772c08 | -17.712 | -46.7798 | 2026-06-29 16:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a16db374-da65-33b1-97c9-4d4d8900e1ab | -11.9441 | -57.7091 | 2026-06-29 16:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| dce308dd-e0c6-39cb-8406-499765c13579 | -11.9126 | -57.1339 | 2026-06-29 16:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| e2f429c0-c6ed-3eed-8a63-4bc66ac884b9 | -10.2941 | -57.138 | 2026-06-29 16:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| eef79e57-8f39-3860-8d5f-96ee43659cbd | -11.0414 | -55.7411 | 2026-06-29 16:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 96a8f507-041c-3555-ba32-77eb008322fc | -11.8939 | -57.1155 | 2026-06-29 16:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 76ef1654-5376-3ca3-ab3d-a39453b91ed8 | -11.9286 | -57.392 | 2026-06-29 16:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 223.0 |


