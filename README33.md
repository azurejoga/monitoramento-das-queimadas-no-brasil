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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b56f2fea-ce53-3b8f-bf50-0a9256f2641b | -4.0052 | -44.76077 | 2024-12-01 04:21:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbc2701a-5d77-36a8-bdcd-b166a05e443a | -3.66013 | -50.71226 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30c7ceee-44f9-3d88-898b-6d487d7223ab | -3.26373 | -48.76926 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bfe57d2-acae-34b2-8d97-14463aef4209 | -4.44593 | -45.35626 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a56c41-3428-303b-944c-89a48ca98bd1 | -2.63644 | -46.88047 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10f872c7-7332-3860-b21b-a49a5c3763fb | -3.53982 | -50.17461 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b86aa97-b392-32f4-b6ff-29903457b451 | -2.75214 | -46.10683 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a869522-42d1-3089-a557-4c40d48164aa | -2.981 | -53.28887 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7ec73ec-9fe1-35b7-b9ab-8ad72627df13 | -3.11417 | -53.80975 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bd01a37-b6f9-3b1d-a054-3ee3856906a6 | -2.44877 | -53.61941 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 762aac11-ad91-3a99-b936-4e814ea085b7 | -2.62941 | -46.19516 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98193c5b-d20e-34f6-acab-90135bea3d69 | -0.74283 | -51.78301 | 2024-12-01 04:21:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54918eee-26fa-390c-9945-f94764a836be | -3.12286 | -45.98266 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 989d4a8e-8b93-3825-9849-e6aff0011b6b | -3.38501 | -50.11506 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d96f652-bc13-39d5-9742-d1c600e3fbd0 | -2.89771 | -51.58131 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 149f97cd-7c67-35fb-9567-4dd66e7b8a4f | 1.183 | -50.87637 | 2024-12-01 04:21:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23fcbf14-5503-376b-b81e-f29696f0ed05 | -2.6744 | -46.59637 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4916a8d-2377-3f0f-84e2-4fc738b585ed | -2.24326 | -45.43495 | 2024-12-01 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27031011-4b5c-3192-a45a-5684d5fd25bd | -3.52404 | -51.13803 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76366820-b3d3-3293-a9b4-ba6237329801 | -3.41653 | -50.1848 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 365297fa-e718-3974-af2f-f7d5bf372753 | -3.38687 | -49.85899 | 2024-12-01 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e162148d-3a29-3a21-91c5-513af7fef4c7 | -2.61153 | -49.12523 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1c65b66-e9ad-3bd5-83f2-3848d6a92907 | -4.44816 | -45.36378 | 2024-12-01 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d37e6e9-77ad-30c7-95f6-b5fe0db19d79 | -2.63178 | -54.22122 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2150308c-1a15-3e3b-a11a-82e1e4114b6f | -3.79743 | -46.69116 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48903e86-a840-3a3f-8f8a-60c190ed8d76 | -1.72122 | -52.62757 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0fc4148-1836-3ba4-8634-655060a6bfe6 | -3.85224 | -46.54018 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d449c4ca-449e-3648-98ce-77b4eae34451 | -3.09577 | -54.29751 | 2024-12-01 04:21:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f605a7c0-ddaf-323a-b7b0-14bb38e9adea | -1.07368 | -53.6263 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35743d7c-cb67-3c7b-bc4a-914ac1e868d4 | -1.14448 | -53.67509 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e004d742-1b47-3976-ab71-a8d621f9d125 | -3.76767 | -47.71252 | 2024-12-01 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e106b6d-a7c9-3413-b406-ae9a5bab955a | -3.0339 | -50.23851 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d265cfb-f633-39ef-9ffd-c38cb76e02f0 | -3.21789 | -53.13094 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ecda65c-f3f0-34e9-b56a-f7b485591578 | -4.09181 | -44.85912 | 2024-12-01 04:21:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55a6ac05-2fdf-3378-90ee-e312d4acbc28 | -2.9859 | -45.57945 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 552e6569-9da1-3994-8411-31adfcd9d086 | -4.03905 | -48.33202 | 2024-12-01 04:21:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ddc9ae4-8bcd-3866-8f09-5e7b39e4536d | -2.46895 | -46.56521 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c57de6-44ef-3094-a120-a46a77b1e6df | -3.12035 | -53.80662 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dc90f903-b589-3303-a1f8-6da845fb62dd | -3.06234 | -53.8134 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae81be3a-508c-3e19-8925-d96266ca1a37 | -3.11111 | -53.75679 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c751137d-342e-31cf-bd80-fb8a22046f3f | -2.60216 | -46.56983 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 957cfee4-0f4b-34c2-a729-a5216440caff | -2.76226 | -51.68959 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ff5b7c2-e6b3-3870-aecc-5e86cb3c26b0 | -2.75037 | -46.11799 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e899064-b675-396d-ba0c-4809b42943df | -1.60979 | -46.23457 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3502a00-b4a9-351b-819e-b4cdf776f1c4 | -3.68046 | -50.24603 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebd7feb5-cdb9-3777-9b15-03f782e2285f | -3.36751 | -51.54137 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fec1b00-3c6a-3595-ba37-3032d2a2ab25 | -3.65369 | -50.22164 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12f59ac1-1141-30a3-bdc7-50ca25675758 | -1.97237 | -48.79416 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f61ebf8-b2dc-3625-adc9-e30840de039e | -1.00788 | -51.73063 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28dd0c93-df3b-3c34-8a2d-9ae1f9393208 | -3.0385 | -41.63199 | 2024-12-01 04:21:00 | NOAA-21 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| af785d2b-9521-31e5-8b05-72265ebeeb9b | -3.56348 | -44.62798 | 2024-12-01 04:21:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99bf6dad-ff06-3185-b91e-9ad65b36a152 | -3.09572 | -54.02036 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db6a49d7-a508-3133-b70b-957ed1d88a3c | -2.7107 | -51.97709 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c7f2cd9-ec0b-3b47-a66e-f1f979b34fc6 | -1.60805 | -46.23446 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| befcc346-9a80-3a71-ace1-cf94577ccbd5 | -2.23371 | -46.39545 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cbd0b49-4fc5-3ad5-a847-43fb4fd5987f | -2.56042 | -46.40566 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1b63242-2267-3afe-a40f-d0c4530a6b2b | -2.14262 | -54.87432 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cadc416a-c626-30ee-9127-46532c527acf | -2.04058 | -51.20379 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0ba4d3c-bc31-3622-b395-841c817f78e7 | -3.26564 | -50.04706 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f4045580-50c5-304d-b751-b5d004d7eb53 | -4.06041 | -46.82166 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd0cbe10-6004-3a50-bf57-6fe3e2ec18a3 | -3.78231 | -46.69669 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a26ff6d-2b49-3c84-a511-485e565c979b | -3.26632 | -45.37593 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9cca938-0f3e-3893-a9ca-797c0e6a362b | -1.07594 | -53.63573 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6490483f-7c3e-3e80-bfc3-ff4416dfdfb1 | -3.35839 | -50.51368 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14b31bb0-961b-35f5-98ff-eab881f65604 | -3.68869 | -50.24252 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c89a570-77ef-39a4-aa4a-aab0cd190ba6 | -2.98253 | -45.57892 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2581b400-80dc-3325-9b88-377f0cef3d5b | -2.70537 | -47.74128 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2713f1b-7391-3677-ba64-a15029afb33d | -2.66875 | -46.25912 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36939953-6aa4-3c7a-a8d9-acfd47b1c5d8 | -3.02748 | -51.53661 | 2024-12-01 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e649aeb-8874-3a37-9eea-537b8a7f1ed5 | -4.00555 | -46.94028 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1987bd1-5433-3a0f-aa12-bdbafb5f6b8d | 0.93236 | -50.74612 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57cee89d-441a-32f9-8d68-9bbc78fa5abc | -3.12343 | -45.979 | 2024-12-01 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aeb0e3b-ff4a-3427-9901-a98c6abe42c0 | -0.76463 | -52.41336 | 2024-12-01 04:21:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf3eede4-9268-3fef-9d36-9dd1f7912869 | -2.65678 | -51.87892 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d2c61f83-d540-30fe-bdf0-5ceb257fa581 | -1.67358 | -52.09754 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c076f5a-ecf3-3c6e-a08e-e08d09ca4f8d | -3.73049 | -49.93972 | 2024-12-01 04:21:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d07fa897-54b8-3708-9c8b-5c982cc23cd1 | -3.38331 | -49.85445 | 2024-12-01 04:21:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06de3fbe-c83e-32de-a1a0-0bea89f1983b | -4.56276 | -43.95538 | 2024-12-01 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 849d08eb-f589-3134-bd94-20cc31ef5492 | -2.04138 | -51.19886 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4d34c06-5b60-3f6a-8c3a-39b623bc2d8c | 1.1657 | -55.9676 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a826cd0e-15bc-3d3c-8f07-8ac18f2e0206 | -4.06104 | -42.55568 | 2024-12-01 04:21:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd4cb443-7996-3a07-bb6a-9d30ec0e66de | -3.78926 | -46.69777 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f29fbbc0-682e-303f-a96e-936828653861 | -2.46483 | -46.56854 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 977e69a5-3bed-30e0-8e73-a290b6010853 | -2.11597 | -46.55178 | 2024-12-01 04:21:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0417cbe7-051d-3fac-a427-a91f49fbe4c8 | -2.97564 | -53.2882 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54592288-b168-3614-888c-37d7e5f23f46 | -3.32455 | -50.19189 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98329ee4-d6d8-35cb-aff3-3f9749f72197 | -2.68295 | -46.14599 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ad743c7-ac0c-3d08-a437-3d8386d639de | -1.52283 | -45.91159 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11db3e2d-622d-35c9-9695-fea39003c592 | -2.63616 | -54.22999 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 751d0afd-8269-3764-9fc4-7837fb1ba85b | -3.1725 | -46.31269 | 2024-12-01 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f920d228-8bfd-380f-961a-97be61da7a51 | -3.28949 | -50.63012 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6eca1f0-e189-3053-9ac4-e68b1b1816b4 | -1.72218 | -46.22405 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a160c950-06f2-3547-9ff1-6cbdb5c1b8dd | -3.97715 | -46.75036 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9c459504-eac9-3a43-812a-959c0b673d7d | -2.36295 | -53.86415 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa3fe65d-69b6-390a-a9b6-23aeb59df1e1 | -2.66068 | -46.13106 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0089c21-423b-38d3-a212-3f5976121b79 | -1.24389 | -51.79473 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65af1e9c-7c27-3f89-9b00-755cbeb1bd9d | -2.9211 | -54.26606 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47e954c4-0e5e-3b51-8acf-92bd933e039b | -3.11226 | -54.26826 | 2024-12-01 04:21:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c58a91ca-ab12-3f46-b175-488ab2d6e65f | -2.75962 | -47.90408 | 2024-12-01 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42487b67-568c-3642-ae41-180856e46774 | -2.6873 | -51.72594 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README34.md)
