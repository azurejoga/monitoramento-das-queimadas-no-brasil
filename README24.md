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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac992930-bc4e-3699-91dd-88da6d7a625d | -24.94699 | -53.8647 | 2025-11-26 04:25:00 | NOAA-20 | SÃO PEDRO DO IGUAÇU | PARANÁ | Brasil | 4125753 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0942ef55-d9eb-355c-b170-cfd2fd564d9f | -18.4673 | -46.72586 | 2025-11-26 04:25:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f3111bf-02cd-3a96-bcf6-856046137ace | -18.79322 | -48.55101 | 2025-11-26 04:25:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d044946-b0df-35a6-867d-fa65d8e1cd1b | -23.59894 | -48.34536 | 2025-11-26 04:25:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f4bd426-d1d6-33e9-8857-244c0a6690b8 | -26.1017 | -50.17573 | 2025-11-26 04:25:00 | NOAA-20 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ee23132a-e2a3-3c3f-949e-d9655480acbe | -19.95128 | -44.70576 | 2025-11-26 04:25:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a5fc7b1-66ec-3b77-8fad-1f4fd3556541 | -16.76149 | -51.35205 | 2025-11-26 04:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb14e176-650d-3535-8b07-139177a24802 | -25.19138 | -52.97189 | 2025-11-26 04:25:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 50cf4787-7a9e-38f2-94b8-833948e83b68 | -18.94223 | -49.30217 | 2025-11-26 04:25:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 183cee06-2133-3094-af20-34f9ad69ae51 | -29.95051 | -51.61774 | 2025-11-26 04:25:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| bab16960-cd97-3f24-bafd-12f18288201f | -19.15416 | -49.44201 | 2025-11-26 04:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1c119dc-84eb-3b01-8f32-a365826321a4 | -1.07987 | -49.19478 | 2025-11-26 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adfb6788-5c35-3851-9543-1dfac3a7fd72 | -1.58022 | -48.65059 | 2025-11-26 05:08:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba70a43c-a45e-3bb6-bd40-8ecf54e99b9e | 2.74295 | -60.72639 | 2025-11-26 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38d3ca9f-1e4f-3cf7-a04e-be76f6570248 | 4.2277 | -60.12685 | 2025-11-26 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17354a3c-a8ea-3aee-9eb7-814a03f6c962 | 3.10341 | -60.76586 | 2025-11-26 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7331c23-d61f-38dc-8d74-853cf885aa3d | -1.76199 | -47.09407 | 2025-11-26 05:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bc6ed41-6594-3945-9c17-3f87dc4d5cec | -1.76147 | -47.09743 | 2025-11-26 05:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 515fffd3-6744-334f-b3bf-029a4d441b60 | 3.09923 | -60.76647 | 2025-11-26 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 548c155b-39d7-33a5-94e1-1fb6ae336a24 | 3.87153 | -60.36469 | 2025-11-26 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60a916b9-1b06-32ff-99ea-e6d6bf81e427 | 4.23115 | -60.12223 | 2025-11-26 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6926bc11-26d8-3998-844a-b6218102681c | -1.07528 | -49.19406 | 2025-11-26 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8265de6f-8473-3633-b9f0-162f474053ed | 4.22713 | -60.12307 | 2025-11-26 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 177b2c24-9eea-3f7f-a915-fc6de7e8f971 | 4.0696 | -60.21189 | 2025-11-26 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce8f2e25-3e00-3e87-8464-4ed4503b4d52 | 4.15135 | -59.94873 | 2025-11-26 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a370a4-d135-347b-8e8d-7ae080bc8efa | 3.10399 | -60.76968 | 2025-11-26 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 43e0eda3-5d3e-3ff8-9cdb-7d5c0319687b | 3.09981 | -60.7703 | 2025-11-26 05:08:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6700ea07-7980-33ed-bf5e-c125d3f4f067 | -2.48338 | -47.82917 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afb42819-469f-32cd-9117-ba69902f8e27 | -3.09019 | -51.54472 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f92245-84cf-3c56-aeed-c6b81583f5a4 | -2.91775 | -51.30658 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 983eff26-66ad-357e-9b4f-2881bea26351 | -2.71423 | -45.69036 | 2025-11-26 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd62dd3f-e3fb-3746-8dc4-a7b3f7bb6c5d | -3.30719 | -50.27357 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 798c0b08-dbb3-3f97-94c9-6aa0f1138b7d | -7.74967 | -44.19758 | 2025-11-26 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68378876-813e-3ebb-a68f-d5c1b9414df1 | -4.17062 | -43.7436 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 602e2e3c-8467-34b9-8327-330060e78d82 | -3.30084 | -53.04673 | 2025-11-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56cbacfe-3c08-386e-b9ab-b66bbd8e9548 | -4.7263 | -46.46256 | 2025-11-26 05:10:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9a86a7e-a474-3a02-ae14-35a06aa7bda4 | -3.26208 | -51.17643 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f5e8b12f-7832-3cf2-ac32-023d95010256 | -2.48853 | -47.82996 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a3afe931-7b4d-3864-8183-7b1ffec04f0c | -4.16609 | -43.71896 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c758e1f1-4efa-3675-81ad-63c2b4a31b56 | -3.02216 | -51.03808 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 842b4c7d-ab95-32db-9fc2-7e03a5d1f478 | -3.69789 | -47.64768 | 2025-11-26 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1b7b1e8-c87f-3097-8666-fbed14a6e5cd | -3.92575 | -49.21875 | 2025-11-26 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fd1a505-0a6e-3be3-ae52-0bb341e8bb08 | -2.93896 | -49.35355 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 39b202b7-f663-33c1-88b3-019c0570b3bc | -2.7468 | -47.13414 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ff211a2-e956-3960-bc71-b6eac5feae9c | -3.18089 | -48.61856 | 2025-11-26 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b1356dc-283c-3464-a470-cfb506930aab | -3.30279 | -50.27287 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e18c89c-38a5-3732-8071-86928f56415b | -4.1809 | -43.71955 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 046e88f5-d891-3c2e-bbdb-3b1a2f7fbddf | -3.96141 | -49.03696 | 2025-11-26 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fef17cdb-59cf-358e-9335-d739d45cae5e | -5.27589 | -43.64159 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0e6e287a-cd0e-334d-9c58-6ab0e27e1ae2 | -3.23198 | -51.17943 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6030fc71-78ae-3a13-812d-7dc4a2c1a639 | -2.49415 | -47.82771 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bae198c3-471f-33b5-84dd-7be90ad878f8 | -3.37365 | -51.29515 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a7ea7fa-3c0c-313d-8e7d-392571ab0921 | -3.28981 | -51.27218 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6023bfce-52d7-3b87-a9b2-9185648a2ec3 | -3.42389 | -50.09361 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68833e75-f866-3275-82bd-79ed1bcad5cb | -4.67596 | -49.37866 | 2025-11-26 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c58e3bb-18ff-374e-8e89-59047f7846ef | -3.45983 | -50.54878 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 023f1645-2b14-338c-9f67-cae6c5459f34 | -3.92096 | -49.21804 | 2025-11-26 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9249ed30-78e9-30b3-b571-8d374d348153 | -2.71357 | -45.69474 | 2025-11-26 05:10:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f84934ce-591b-3118-9745-fff5eb63642a | -5.38908 | -50.49205 | 2025-11-26 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bbb911a-de64-314e-bb51-1e79096b3c68 | -4.28951 | -47.30625 | 2025-11-26 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6ce13c5-03ea-3a91-b573-5cae09ecb87a | -2.47777 | -47.83141 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9a1d52b-e4b7-34d6-b034-c2bce5197749 | -3.0989 | -50.55711 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cc85671-c534-33b2-9e72-1f584b5922c7 | -4.45508 | -44.3047 | 2025-11-26 05:10:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 600e9bae-b73c-32b8-bf06-14df11e8b742 | -4.1643 | -43.73151 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cdf61c1a-394b-307b-a6e8-f694f0bc7ae7 | -4.33356 | -50.48558 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10050f8f-4132-3c2a-8fa8-bcd525c07f7d | -3.3791 | -50.57224 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc491bd5-308a-38f6-a1df-32da6a271b07 | -2.47218 | -47.83353 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f319ffe2-2388-302c-853e-b0ec8f70b834 | -4.9301 | -49.15359 | 2025-11-26 05:10:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f4d7d7c-58b6-3cee-b89e-677bab8f16bf | -2.727 | -49.79088 | 2025-11-26 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bef17954-ae48-3e72-9f75-9d6f445b8dca | -6.76713 | -46.51248 | 2025-11-26 05:10:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 566b7fa5-8885-3cb6-922e-af52e24c651e | -3.237 | -50.59324 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 156aa219-5bb4-3a1d-9eb2-fde1c5c75801 | -4.81497 | -43.82376 | 2025-11-26 05:10:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd6a3bc1-24ce-3a08-a899-ebc57b92b298 | -4.74815 | -46.55853 | 2025-11-26 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3786939e-605d-37ab-92f4-ec76db06bb23 | -3.3015 | -53.04236 | 2025-11-26 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ff9144-637b-31fe-ab85-8c612908d3ca | -2.49977 | -47.82543 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d52bbf1b-159b-35b4-a814-ec7ed62c0382 | -2.4173 | -50.29053 | 2025-11-26 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f38ab8e-ba53-3240-b6ab-4d6cb431e352 | -4.17977 | -43.72133 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 22c25258-d480-30e1-aeb2-b8e7bd4d028d | -2.74492 | -47.13486 | 2025-11-26 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb4ee9c0-5c3e-3290-a875-ed9c0261db14 | -2.44905 | -49.02945 | 2025-11-26 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c760ea9d-ea8a-3c04-aec7-080790e5e38c | -4.28896 | -47.31006 | 2025-11-26 05:10:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68261952-0d69-3b83-afa3-0c1b55438529 | -2.93692 | -48.22063 | 2025-11-26 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69ea6676-69c6-3b65-80b9-1cd7d9d3019e | -3.1785 | -48.62324 | 2025-11-26 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9460c55e-cc06-30ed-9f9a-8ae54af8b0e3 | -2.49461 | -47.82465 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6673d013-d622-38de-b9a8-27a98d936fcd | -4.17581 | -43.70552 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6660a04-8785-37bd-bad3-44cb6f97d6d1 | -3.17935 | -48.61773 | 2025-11-26 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc005cc6-a2bf-36a0-a588-10d35a628666 | -3.0995 | -50.55299 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df5ab85-7dfe-3a41-a6b5-382e1d07e287 | -4.68077 | -49.37923 | 2025-11-26 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38ac0c98-550f-3247-b548-962077d84b10 | -5.27712 | -43.64088 | 2025-11-26 05:10:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10aa010a-7cc5-3622-a559-fddda290263e | -3.16656 | -50.60515 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 328c4b43-39d9-3b2e-ac9f-5d474c2fb941 | -1.38332 | -55.34339 | 2025-11-26 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a1fb40f-ff21-342e-afbb-4e64836bc235 | -3.9683 | -50.21876 | 2025-11-26 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae81c6f8-1a63-32b8-b66c-ab17e65f65fe | -2.48992 | -47.82072 | 2025-11-26 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2898a534-d9ca-3ced-a210-c4c0c10bfb0a | -3.02862 | -51.034 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08b95707-e072-3bf3-99d8-e24d933d712b | -4.9691 | -50.87388 | 2025-11-26 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227cc3e9-31a9-3e47-8332-fec2923e5bdf | -4.17201 | -43.72658 | 2025-11-26 05:10:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| bd0b4530-b414-3660-af86-c840096c75e7 | -3.98494 | -49.28193 | 2025-11-26 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4f96753-7cc7-391b-a65d-99a4b8bbb0e2 | -3.32994 | -49.71586 | 2025-11-26 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8edc26f1-1a45-3a89-bb56-0261f35659d7 | -3.44995 | -50.5556 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ceb53a75-90f9-330d-a09d-85aeedee621f | -4.74753 | -49.89862 | 2025-11-26 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 555f45a5-3d38-3430-8bf3-cca717216838 | -3.02275 | -51.03428 | 2025-11-26 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README25.md)
