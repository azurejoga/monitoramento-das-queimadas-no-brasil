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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42f54c17-8157-378b-90c2-701c14981b77 | -3.16462 | -48.43564 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f65ae60c-516e-35af-a465-4144b6692d7f | -2.82934 | -54.11677 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4aafe31e-b85f-344e-9f4f-4f88946ca9c8 | -3.22462 | -54.09007 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8281e0ca-fb7b-3ea8-bc10-0b90dcd0450d | -4.50425 | -46.60267 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be61e511-f818-3971-9b60-bace29bf43f0 | -3.70889 | -51.80417 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ab8c4fa-0b78-394c-982f-f16820203503 | -2.83731 | -46.83376 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8437a7a8-b565-3c88-928f-b4be2da16309 | -4.23619 | -48.64182 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 495cca0a-021c-303d-9c6b-62d67a06a0ee | -4.21609 | -50.90248 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff195fcb-476e-36d5-a103-5327a058e784 | -2.80251 | -52.90907 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90dec2bc-7c5b-3036-8332-ac6f67a17d73 | -3.2488 | -50.61605 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ede98b60-101f-3b70-92fa-67385189ce75 | -3.27823 | -48.76146 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01f34dae-41b9-33da-81ed-8542e46ae6da | -3.28384 | -50.75932 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a2af30c-5156-3a3f-87d3-0284033147fc | -3.05391 | -53.28137 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f824366-fecd-3b00-baf0-f518882f5ed0 | -3.41507 | -50.44498 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe48e11-5c68-3452-88b2-9bae22eeeb5a | -4.21798 | -46.45072 | 2024-11-27 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 193c2426-7a4a-38d1-8f5c-dac2a7c1aba6 | -3.101 | -53.73204 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b7b3dad4-ca7f-3f41-abc7-b29eb803cee8 | -2.44502 | -50.41235 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c79a35d-76e1-3104-ae0a-7ae7cc990508 | -3.31327 | -46.6623 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e39e944-b6d3-3ce4-bd27-3eb751ebac80 | -2.89783 | -54.17239 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2eb08bd7-1ed2-3eed-96c8-eeae122c5b5e | -0.84027 | -47.65587 | 2024-11-27 04:42:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61eff45d-c842-34ba-a8c0-988de0c00f21 | -2.17335 | -52.08442 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a60026e9-0dbb-3308-8253-2fcf1efb3225 | -4.24583 | -48.66972 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea25ee22-58dc-3d6c-bb4b-7959694113c3 | -3.10056 | -50.3704 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc81ef13-6fee-3454-b724-c64ca334b52b | -1.1924 | -51.77097 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6492ae95-2dda-3711-bb25-dba9f16ca4f3 | -2.99335 | -51.46188 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01b9152d-65ef-328f-bbe9-43d4eee5aae9 | -3.81028 | -46.61177 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53cfa503-adb1-3ab4-886c-14033ac32a70 | -2.64539 | -48.48418 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18aee52b-4190-38d6-8ee2-3454cb52c4c1 | -1.76439 | -53.6198 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5aac799f-96dd-385b-ad8c-16b3c002bed2 | -2.73176 | -48.64862 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2674b8d9-a0ac-37ab-82ff-b408237dc331 | -2.71863 | -46.28673 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d69f0049-9adf-33a8-881d-d7fd6da1a2eb | -2.56558 | -46.41825 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8c3b592-2ccb-3a55-baca-d282eba7f275 | -3.67275 | -53.55503 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82b8effa-2b46-3bfa-9a67-5108a9736266 | -2.93177 | -48.01694 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db4df9b8-3480-3a56-b244-4a9ef676d521 | -3.27235 | -50.5527 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50c98148-b2e8-3602-bdc4-eec5b9ed72e3 | -1.77606 | -46.95076 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca405c70-1101-3521-8675-581115946d04 | -2.18372 | -53.66479 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ae7ad41-abd5-3319-8a39-8d0912e4877e | -3.52433 | -50.24731 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a5b2700-4515-34d2-9d2d-a9d96b89036e | -1.96013 | -51.05451 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48c5a2c9-0628-3969-b5e8-d2ab48eab760 | -2.81912 | -46.83098 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8021b828-d8e8-3f6b-afbe-3113dc64d354 | -3.22845 | -54.16729 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c61a6e5b-0c60-3508-add5-60830489ca82 | -3.72375 | -49.95031 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a25fb54c-0852-3ade-945e-4bc935aac432 | -4.30172 | -48.2391 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcbb7534-0a8d-31ba-9913-654245257c77 | -4.38723 | -47.77569 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a44aa082-45ee-393a-9066-bbd91613702c | -3.18619 | -48.43145 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 296c8f52-6a25-3ee9-90f2-787ba7844c64 | -5.61836 | -43.95144 | 2024-11-27 04:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 59b587b8-7ce7-33bf-a7d0-950ef007050d | -3.09507 | -53.25425 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4c82f6b0-69c2-38df-b768-460c1a1d0225 | -3.96797 | -48.08435 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e3bdce9d-a73b-3d96-951a-c7eecc74077e | -2.24883 | -53.46481 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db756496-4314-30ba-aa1f-edc20b22dff3 | -2.09774 | -53.3564 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e26438b5-2633-3114-9c19-b9ff5aa774a3 | -3.2938 | -50.24251 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 383bd736-937d-3a1d-aacb-5203fabe896f | -2.17475 | -48.53801 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8b827428-2c33-3691-94e6-fbef424d77f4 | -5.97945 | -45.36685 | 2024-11-27 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa4a5b4-8ace-3f99-9398-0dd0e4acc56d | -3.16802 | -48.43617 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 25ed610d-aa6c-3030-a227-eb3d6540e281 | -3.7024 | -50.69072 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eecc6496-a443-3de4-8162-c75e394d86c8 | -3.78593 | -51.75383 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14d367a8-8029-3de9-8fbb-ebe921aa6857 | -3.24806 | -53.28831 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6caa0863-3b85-3437-ad43-0f7c3c69db2d | -1.81277 | -55.63176 | 2024-11-27 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d42116f-1491-3543-9a77-76935276dec0 | -3.18163 | -48.57273 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df9c5bb4-e62a-3cb4-9373-e22c0e7b4757 | -1.44917 | -52.72115 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94eb976e-2172-3657-9a71-0aef504f3b0b | -3.45933 | -49.96936 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ec6b38-2879-371c-9ac8-a4e15db58484 | -1.26641 | -52.16328 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea302a99-f805-3279-b866-607aa1c7eb18 | -2.96863 | -48.00713 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e42438f-4915-3673-94e8-c697aa2725f8 | -3.89245 | -46.09952 | 2024-11-27 04:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 731e8e71-8f77-38d7-bd88-e33601694d4c | -1.12596 | -51.68093 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e99e29ae-7bdb-3fa7-9ebf-86d0d83e9132 | -2.70843 | -53.18499 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e2bf2847-d69b-3a97-96d6-3ecc58579c02 | -4.29942 | -48.23106 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fcd9e70-743e-36ff-b63e-e46bb8ae677d | -4.38072 | -45.97532 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab1d95d0-756f-3186-967f-6faf7799c9c1 | -3.29105 | -50.54151 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39be3201-bd68-3a49-9600-7df5ec5b27df | -1.31585 | -51.74398 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82e2165f-ee16-3573-8803-f492878948e8 | -4.01479 | -46.439 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f903e598-2605-3689-b2fe-146357dcfaa7 | -2.88684 | -48.73786 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfe779d1-ba21-364a-a5f3-f9a269723743 | -1.71241 | -52.72651 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043745af-6203-3cc9-913c-6f628bb5a39a | -3.49858 | -53.82049 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0039ea99-0439-3cdb-bd0f-b9ba59083730 | -3.81556 | -47.47298 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca37fd23-9b90-30f1-b682-c120b05c14da | -2.90465 | -45.23693 | 2024-11-27 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a06ab49-b997-3d3d-ba73-01da99a6f9aa | -3.02191 | -51.36136 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 912b6d7f-0c20-3464-aa6a-635c81c9e84f | -1.77544 | -46.9548 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 252e3bb4-59b6-3013-bee9-baf095019c4c | -2.60481 | -52.94569 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9328bbe2-b235-3ccf-bf9e-25cf7d6dfb3c | -1.4598 | -52.291 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69f6c818-a04c-3e72-8fcb-a3eea74e82ae | -2.71471 | -46.25554 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a0d9099-988a-3b53-8650-4cc2a5ae04a2 | -3.4993 | -53.81612 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db100ca5-0e3b-3bb9-a0c9-b6a7ceb25d33 | -2.40737 | -53.84995 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a1dd036-0f0d-37e0-94e4-808154fe14ba | -3.79275 | -49.94343 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2a652b0-1856-39aa-a15b-f7b076523e0b | -2.77422 | -52.90452 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d8c9216-45c3-307e-9482-c905ee0e5da8 | -3.32746 | -53.72153 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc399d30-a5dc-347f-b7e6-74cbe6577d01 | -3.17824 | -48.43774 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 80e34f4a-d2c2-3196-8836-6581f88edd7e | -2.30828 | -53.61159 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0ed04be-b71d-30ff-9b16-5efb06001e8d | -1.63345 | -52.49317 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f3dcec-412b-3edb-a490-ac0168f3f54d | -3.17102 | -49.22801 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 120f9d88-fbef-36a0-b9ea-de8149bc8d69 | -3.15488 | -50.58717 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 488a1930-0dc8-3642-b2fd-35079899f52b | -3.08593 | -53.26542 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d953a327-5afd-3a9e-8537-f908eb01175b | -1.31813 | -51.75141 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af7ae9be-994f-31dd-8516-6a1a3d714498 | -4.29369 | -48.19903 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5413625f-f2b9-38c1-bd3a-85d6140e0cae | -3.07717 | -49.50244 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea628ca5-9a1d-3186-b378-e3ef67ef20ea | -5.02709 | -47.01246 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3fe5cb8-2ad2-3875-b9a3-3da73f45b4f4 | -2.93054 | -48.63422 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c748ba5-8bce-382e-8d4a-a6d7377db8ee | -2.9654 | -53.73481 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0250bd8-4a6e-3006-bdee-5e99b8442e23 | -4.21773 | -50.89213 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2cf6f7f3-deb2-3594-aa56-dc3a10316957 | -3.77578 | -46.68823 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be0f5f5a-6404-3f91-acb1-4bc9b9c14d3d | -3.97329 | -49.94 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README54.md)
