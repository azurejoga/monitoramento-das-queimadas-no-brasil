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
| 71ad7e13-d7e8-3ecc-b979-e78e03f0058a | -3.063 | -54.5009 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01145ed2-b5ba-32cc-9518-8e89282536e3 | -3.3016 | -53.669899 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0e29222-42a3-3426-86a9-347ad4195952 | -3.122 | -54.621799 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1ec229c-adbe-3285-820e-d4f04757e067 | 1.1318 | -60.515099 | 2024-12-04 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b6f67b6f-ea77-351d-84c8-a3fbf5985f9c | -2.0354 | -53.939201 | 2024-12-04 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4cdaee3-b49a-3394-a32e-3a1351608278 | -1.733 | -52.599998 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb516914-00e6-3626-af6c-1597ac3d5656 | -3.1034 | -54.056198 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb15267b-a4a9-3b58-9e20-5085fa60cbf5 | -2.4149 | -54.020599 | 2024-12-04 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2642eb3a-f090-3c1a-ae9f-953edb469dff | -3.0532 | -54.503201 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4faea18-e55f-3778-b1ab-a827e35d4fb4 | -3.124 | -54.630199 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2b7354-b848-39ae-b4e3-d22567299b7f | -3.2558 | -53.650398 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b90d5be-408c-379d-8403-7b2ac59b08a1 | -3.1298 | -54.611099 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 453862f4-6f53-3c08-9ff4-ed077ed32366 | -2.3441 | -54.380199 | 2024-12-04 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99c1856e-8727-3e8f-a519-5a733e0bb012 | -1.7385 | -52.6231 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4e88a75-a372-35e5-957c-22078be7a008 | -3.2709 | -53.6269 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61d35ed0-593a-3260-b091-a22301cbf5fb | -1.751 | -52.632401 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3b1296-b86a-3c37-985f-04b62a47cfd2 | -3.2536 | -53.6409 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70f252a9-4062-35af-8170-c89d5bc25dbc | -1.6676 | -52.759998 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24248d88-3b56-3c10-b830-df8030bc2d09 | -3.0617 | -53.262199 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b4ffb6a-dfc7-3326-8ab0-de1d8c9f0fe5 | -3.2461 | -54.1371 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83925442-8622-3a95-aa4c-a4ab910ccc17 | -3.6353 | -55.497799 | 2024-12-04 01:15:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a3f7d35-7d73-37df-be9d-42d75378eb71 | -2.9802 | -53.881699 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9001213-e31c-319f-94d2-7d4c1b4fcd37 | 1.6567 | -56.0182 | 2024-12-04 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 086ca02a-c8ab-3cf6-b804-c7c74cbe884d | 1.6586 | -56.010101 | 2024-12-04 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f98feef-285b-38b2-9a17-5b3806475fce | 1.6685 | -56.012299 | 2024-12-04 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9f3f7b1-2e8f-314c-9edb-16e85e14a281 | -3.2678 | -53.6577 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e00de2-310a-3745-84a1-678fef30c784 | -2.3462 | -54.389099 | 2024-12-04 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb258270-234e-379d-bb1f-153fa46209e2 | -3.2687 | -53.617401 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f335da6a-65df-344a-b0ea-afe8d81ef428 | 1.9684 | -60.914001 | 2024-12-04 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff7b225-689d-309a-872d-d65cb0e76d4f | -3.258 | -53.659901 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91b69718-a5ef-3dd3-a969-24dd03478426 | -3.2567 | -53.6101 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 337e8892-2ea2-3625-a218-924128faa6f6 | -3.064 | -53.272301 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9ba0f1-6ce2-30c1-ae91-e6fa5306fde5 | -1.6649 | -52.7486 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29a5ef03-6aed-3989-9d5b-ede18d24453b | -3.1161 | -54.5965 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90040045-439e-3c69-90fc-f64f4d4e8da7 | -1.7483 | -52.620899 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e85aa819-6ae2-38ea-9ecb-88a654e22f3c | -2.69 | -51.858398 | 2024-12-04 01:15:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f69d6c-e8a7-36f0-9b01-31d09b4a3d28 | -3.2909 | -53.712101 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4147930f-cd5f-3bf3-a655-9719400033e2 | 1.0503 | -59.522999 | 2024-12-04 01:15:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ef5ea656-853b-353a-b097-f6af83c01bde | -1.6552 | -52.7509 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccaf9fab-a87b-3aba-aa93-ab7d9294498e | -3.1338 | -54.627899 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7de70c-4147-33ca-9b92-6a6f65a30baa | 1.0876 | -55.984901 | 2024-12-04 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f431fc3c-0e53-3e71-9229-551aad08cc41 | 1.0613 | -60.597198 | 2024-12-04 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 43e4d1ef-ad84-3241-9f79-ce7bf5346280 | -1.4388 | -60.077999 | 2024-12-04 01:15:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b60a5c93-3d43-3393-92f6-e96b2d7415d8 | 1.9701 | -60.9067 | 2024-12-04 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 006217f5-9ac1-357d-abcf-557dd8550f83 | -2.7961 | -53.052502 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4aba17d-1c9f-3cce-a04a-9bedd2792d8a | -3.2611 | -53.6292 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d7401fd-f236-3236-8155-bf139a3b7b46 | -2.2351 | -53.691399 | 2024-12-04 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba5bb531-eab1-345c-abcf-3ae2ce7d2ca8 | -3.1122 | -54.624001 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9814d1-b973-32e3-a09f-a5656c14d209 | -3.072 | -54.053902 | 2024-12-04 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23213f01-7673-343c-a806-fc5a42a47483 | -3.1279 | -54.6026 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90410df6-dc65-3637-98cf-aca2757ea5b9 | -1.6485 | -52.3703 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fcc98c9-6289-3d16-b3c5-eaccd0ea4a14 | -1.7456 | -52.609299 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 024e297a-a481-3372-9140-ac852bd75f8e | -3.091 | -53.255501 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb75dd8f-c968-39c4-8cb6-1c2f95aebfef | -2.6929 | -51.870998 | 2024-12-04 01:15:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb22400-aa1b-389a-8296-8be75aecaf61 | -2.8182 | -53.058601 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723bbd7c-3427-380e-9dcb-ecbe7510a929 | -2.723 | -51.8242 | 2024-12-04 01:15:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e53ab2-7f5d-39b8-9bcd-d5ae59069bb6 | -2.9964 | -53.819099 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a38c647-fb29-3ff3-bfc1-4aea912d8fd0 | -3.2656 | -53.648201 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cb36813-7e9c-3c99-aa29-573d63877c40 | -3.2634 | -53.638699 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d93156-c61b-3551-a423-91ac880c8fac | -2.8059 | -53.050301 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0122abd-edec-3ea0-8818-30e885a04942 | -2.3512 | -54.499001 | 2024-12-04 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f3923a9-923d-3d1d-8e83-62687eff0d29 | -2.8255 | -53.045799 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc0fc83-939c-312e-ae29-a4d43bd0a94d | 1.4752 | -55.866199 | 2024-12-04 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c73fbf30-dbf8-361b-ba33-698f14944ad1 | -3.1083 | -54.607101 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cee9d62-8a54-36a9-b877-8861eb4fe192 | -3.2887 | -53.702702 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd87c23a-1e73-35c0-8abe-c59d1385f35e | -1.6542 | -52.394402 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5933bb1-ead6-32d1-b9eb-10725a342b99 | -3.1884 | -54.5084 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2770fe0f-1dd2-3073-9bf3-8ca52c36deef | -3.1775 | -54.329201 | 2024-12-04 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5721ec0b-fe56-3100-aa8e-9228ad55caac | -3.2589 | -53.619598 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8325d9af-5cd5-3639-a1b2-be063704c94d | -2.8035 | -53.039902 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df36e97-dee8-3925-9d68-cde1844d02ff | -3.1013 | -54.047199 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa279abd-85ee-3b28-9863-d1d8fb8c629b | -1.6513 | -52.382301 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b27f5a8-a1d6-3b7f-ab8d-c666d7f64ae0 | 0.4412 | -60.602901 | 2024-12-04 01:15:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 686506ad-dbe8-3970-845f-6b4944dd42f3 | -2.8157 | -53.0481 | 2024-12-04 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3631e236-755b-3013-a960-e1ed49906881 | -3.0622 | -54.056099 | 2024-12-04 01:15:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39cea78b-3cf5-3f26-bd5a-f687573fc08f | -3.2896 | -53.662701 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0907923-d6bf-382e-9129-c90b5142c9e0 | -3.0916 | -54.0494 | 2024-12-04 01:15:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52b75371-6be5-3c75-83cf-f7742c9d1cc6 | -1.6227 | -53.5378 | 2024-12-04 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e1c3f9-9d3d-3e97-b549-efd69c082d2f | -1.6967 | -52.620499 | 2024-12-04 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4c81db4-915a-3f4b-8c17-70ee094e4916 | -2.6242 | -45.7399 | 2024-12-04 01:20:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| eb157269-677f-32e4-9b5b-47b502bff91b | -1.6623 | -52.7599 | 2024-12-04 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 67ecaffd-c63a-3550-8c41-190e82d468c8 | -3.2153 | -50.6423 | 2024-12-04 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 33bef1a8-81dc-3c2c-bdb3-168e378fc52a | -2.8791 | -51.7932 | 2024-12-04 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1e197930-d194-37e3-8a7e-5840923f192a | -2.0682 | -45.4871 | 2024-12-04 01:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b0b79cfe-176a-3380-b6bd-ea6a40e6c1d8 | -2.6428 | -45.7394 | 2024-12-04 01:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 2ba569eb-8cd8-37bc-bd8d-f8d8cb01a1d4 | -1.7544 | -52.6363 | 2024-12-04 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c2fe8cd2-a5da-3923-8855-bade7b9ae5df | -1.7361 | -52.6162 | 2024-12-04 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0b5b30c5-185c-3fae-b9d7-52e36da12eb9 | -2.8975 | -51.8133 | 2024-12-04 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8773665f-963d-3f52-932c-c09fa727a000 | -3.2774 | -53.6585 | 2024-12-04 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 06232f12-ec9c-3400-8062-b39f27030d2e | -4.1223 | -43.9299 | 2024-12-04 01:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 709bbc3f-36ca-3f81-825a-8350bac7ac0e | -6.086 | -48.0557 | 2024-12-04 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b5a9f6b6-8f48-3d71-8c56-7881d682371f | -3.1086 | -54.6068 | 2024-12-04 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 0ddff3bb-bf6e-374d-8d46-0f96fb810a32 | -5.6281 | -44.8433 | 2024-12-04 01:20:00 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| d39515d0-2852-3551-aa05-d9a2ddae71fc | -3.058 | -53.28 | 2024-12-04 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f7919d11-bcf1-385b-8f4c-fe7cd05c7f0e | -3.1453 | -54.6259 | 2024-12-04 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 520493f6-8788-37eb-a42c-e64db613d962 | -3.586 | -50.3158 | 2024-12-04 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6a2b4f61-36b3-3e22-9769-ea6477835676 | -2.8197 | -53.0425 | 2024-12-04 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5a4957dd-c8bc-3f7a-8d18-a25fd62874fc | -3.0764 | -53.2796 | 2024-12-04 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5926691e-3ce0-3174-b2aa-30c30319e19f | -3.1454 | -54.6059 | 2024-12-04 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 5f5561c4-f8ac-3497-a2e0-99b055bf6bf6 | -3.1086 | -54.6268 | 2024-12-04 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 225.0 |


[Clique aqui para ver as próximas entradas](README16.md)
