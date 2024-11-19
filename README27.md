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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c599dc32-2a88-38a4-9be6-736bd0cad60a | -2.68841 | -46.22317 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c987ddd-f322-3bc8-8191-00d753741d06 | -1.30783 | -51.74972 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3240838-84b7-3361-9a08-e7b7f9212f6a | -1.24688 | -52.05139 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49e4848e-08d3-3715-ae6e-41e3aa2f6e90 | -1.33326 | -51.86121 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03e6ef79-7bed-3790-817d-d896f17396b7 | -3.06706 | -53.27839 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6a4d4d3-148e-35f3-b657-031c68e2da9e | -4.86749 | -50.53911 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebc78563-c513-3484-bdce-944b5e9c6253 | -1.62448 | -55.14199 | 2024-11-19 04:46:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14541c4e-95e1-3df4-9cee-fc05a2e43a42 | -4.57566 | -48.01535 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9a08c42b-87fa-30b4-8e57-eeec2c934739 | -3.5127 | -53.79809 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee0d213f-bc8f-30de-b341-242364f5eb22 | -4.54728 | -48.01099 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8eb0249f-7a29-32ec-8603-54e5a50f7889 | -2.15523 | -50.70193 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf8f2a72-71b2-38e9-acf1-c5abad448f23 | -6.4163 | -46.18745 | 2024-11-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7603b2ec-b8ae-32a2-b3a9-b41eeba113ed | -1.86495 | -53.19559 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73725fc7-4da6-3dab-b416-260d20b2ed7b | -3.88477 | -52.22615 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d4dc833-1983-303f-a1c2-c061db77add8 | -0.85069 | -48.74572 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 822dfa10-2f6d-3afe-8f37-5820bfb257b4 | -3.09627 | -51.31691 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0d88903-989f-352b-833b-793a28e54e5b | -3.00875 | -51.44258 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f449376-1ad5-3df5-ba8d-e3c2ba43aeb3 | -1.61858 | -52.4802 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e210607d-36a3-3509-ba95-35aae467cc9a | -2.80414 | -54.18843 | 2024-11-19 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b9780b4-2830-3947-b91c-9d51bc8c878c | -2.75923 | -54.05168 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ac9d7e64-8f5c-379d-9540-28a760db5824 | -0.81136 | -51.48851 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7177830-a24d-39e6-97e7-07b52d543e67 | -0.96027 | -51.72966 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f81a0e5f-a586-330a-a32f-ee4b32f93d1e | -5.98339 | -45.36693 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88dd98b6-c4c2-3038-b3a2-99f3c6b2e3b1 | -0.12016 | -51.42327 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d39e3d24-3834-3649-9bc1-055957983f86 | -0.20505 | -49.39865 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8708190-eebf-3aa6-9d60-7ba2747c9b99 | -3.33521 | -51.13801 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3158013-6a32-3c1c-96ba-edce4300bbbc | -4.54313 | -48.01444 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1589d617-f674-39d5-b637-b660b41566b8 | -3.05533 | -54.4083 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 110e186a-2d5c-3e32-97ff-45bd902c0226 | -2.60133 | -48.33913 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58ad931a-00a9-38a4-a5fe-65ad47620e5e | -2.2587 | -48.42083 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4685960-6152-3902-890a-ce93a726e694 | -1.67341 | -53.10111 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf09d804-8a10-3247-ac66-20144d94ed9c | -1.0045 | -48.00122 | 2024-11-19 04:46:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90585360-6178-30b0-bb90-d317c42772fa | -4.58658 | -48.49348 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d56c9869-a136-3d51-b2b0-2e6a4ce81357 | -7.39806 | -42.76291 | 2024-11-19 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 11fc0775-907b-3aa1-bfd9-1fd1c23dcf7b | -3.05979 | -54.40443 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24612c5c-49b3-3079-93f4-fafe9a915354 | -3.34514 | -45.35885 | 2024-11-19 04:46:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a7c01465-c4bb-3048-954d-d405270cb686 | -1.113 | -51.92156 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e2fc0d1-3640-3b3d-8b84-b85fd04142dd | -2.64252 | -46.21628 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 402a9390-6365-3f39-b65b-71b4c14fc4d7 | -1.48004 | -51.97402 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c5fae24-4529-3f33-a960-e0051dfb400a | -3.69022 | -51.56384 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a100f10b-c774-31ab-9fbb-045a80067bef | -1.2208 | -51.74388 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08b8bf94-7e01-3bca-b23a-584098200f69 | -1.48443 | -52.10298 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b7222e5-c488-3b28-af82-70d7db7791bb | -3.3139 | -54.17164 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8b1b2258-2087-3cf0-857d-728d3ee5cea2 | -4.30636 | -46.74416 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4120a631-1ec6-3fe4-829a-53a20b269999 | -3.1587 | -45.32465 | 2024-11-19 04:46:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8854d75-b3d1-3d6c-b762-e651eb181456 | -1.20161 | -51.77808 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62ef9197-4103-34c5-8fa1-9f752b6e607a | -0.81168 | -51.60695 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4502682e-344d-36a7-914a-1d4a4e0f6219 | -2.66073 | -51.68398 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fad44bf9-b8f7-31ef-92da-aea2f725bb0a | -2.6834 | -46.17903 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa15400-f4ac-32f7-80a2-9d79b3e3c499 | -3.79584 | -50.03933 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 935e0b31-e332-3180-ad3f-4be69982ee9f | -0.85629 | -48.75384 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63f72c2f-84b4-36af-9cbd-8b4e01558d77 | -1.14014 | -51.68332 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8084a90-16f6-3b4c-966c-5577f9885636 | -2.96271 | -51.45343 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bce3b374-372f-3655-8eca-7abcb9e52a03 | -4.10593 | -51.06108 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4942716d-9371-34f8-9ee7-f362ef2376b8 | -3.08805 | -54.66621 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 199f54e9-138b-33ad-8db3-5e525bf5df97 | -1.43706 | -53.38113 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efc8a026-7519-38c2-82b0-a021e85f7c8d | -7.43096 | -47.86763 | 2024-11-19 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63960e27-1f73-3b5a-9983-2b701da221ae | -2.60644 | -51.79591 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c8659f1-2e39-3b36-bfae-570f5985338c | -4.48871 | -46.71685 | 2024-11-19 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5787e650-ef0f-37b7-b8a6-5eda5d680843 | -4.06324 | -50.00294 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8ee01a3-b573-3093-b952-1b39c823c61c | -2.7953 | -48.60326 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc788646-0d47-3256-a00b-1a137ffba83a | -3.11566 | -51.32344 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f738ef-68be-3dcf-9b57-a1e28ec2e8bc | -1.00107 | -48.00069 | 2024-11-19 04:46:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3495ea3-e632-3acb-9c35-9a08e450ec81 | -0.0418 | -50.81544 | 2024-11-19 04:46:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e3db3aa-ed56-37e1-bd0e-1b672e73548d | -1.61158 | -52.36661 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41f64f29-b18d-3831-b721-92652e825fee | -3.61076 | -54.21361 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 06c11c4a-d418-30d1-9f99-3bff212a5344 | -6.35261 | -47.30324 | 2024-11-19 04:46:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 679a213d-fcfe-3eda-8612-3aef11135d35 | -3.18557 | -54.32071 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ece64e9-3ada-3ca0-ac37-7a9391cb7b14 | -1.19522 | -51.97918 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e68aa96f-b9a6-3030-a73f-909d5999e9ab | -2.54464 | -50.66779 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50fa4780-719d-3fb8-a94f-61fbe0d07a4d | -6.29126 | -46.12696 | 2024-11-19 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 380c6c3d-94a3-300d-ad1d-d06b2207d642 | -2.72602 | -53.97591 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c1fef1b-0f21-3e47-b2bf-067752a08b0d | -3.66853 | -54.65272 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22e1b082-ccd3-3bbe-9363-7496b74db141 | -2.8721 | -51.78983 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b93d4628-3934-35dc-aefa-f7c95c764986 | -5.15434 | -48.18625 | 2024-11-19 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 944067d4-06cc-3ecb-8d2d-75579c63e11e | -5.97436 | -45.3695 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13fdb630-85f4-35c1-adcf-9447d5466845 | -3.7109 | -51.84121 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9755cd1-d5a1-3558-9746-9f0ca81c9faa | -7.8947 | -44.22089 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17189982-07fa-3ea2-8802-62159f6d9040 | -3.52773 | -50.25549 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58ad5469-7975-3b49-8746-7d173b2cde9d | -1.53726 | -60.33377 | 2024-11-19 04:46:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06abae96-7a60-3f09-a3ad-c240e899eb61 | 0.22493 | -51.10956 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4a02e9c-bdee-3974-b6c7-9dfa4f5ceff6 | -3.72251 | -52.44705 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b3a341b-e73d-357b-b551-723bf658993b | -4.00316 | -49.90773 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28719e77-7985-3b3f-a5a1-b0844c6adf32 | -1.63258 | -52.67493 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec26cd1d-f7a8-3b38-8ac8-c3a04193fd9a | -3.02671 | -51.47767 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8d5c60-22f5-3dd5-9dc6-b0763e039a8d | -3.81957 | -52.16827 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9b00709-8645-3c17-b828-21a71499bf3a | -2.16598 | -48.7275 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbe0fcd1-7975-3fe3-9137-347ee2c8f1af | -6.48599 | -47.50403 | 2024-11-19 04:46:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1522cec2-2ece-30f7-a490-09dd6e61089f | -2.90567 | -51.77317 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58bffee2-a892-305c-a0ee-9798d24a53f3 | -1.85824 | -55.27136 | 2024-11-19 04:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a95e031-830f-385a-8f6d-c57ee377e002 | -1.19805 | -51.98339 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4eeb36dd-15f9-3d72-ab9f-7e43d26b75b8 | -1.14295 | -51.68746 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e58e8307-3ec7-31e4-a381-cb0f3d11d6db | -2.02223 | -52.07549 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92bd85bb-7130-38c4-a824-f8a61a8fbb43 | -2.31448 | -50.63917 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ffcc1b6-8016-346e-9c48-7e7df5dd99eb | -3.09552 | -51.04009 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae76ed7c-cee2-33a6-9084-78491d4c1a95 | -3.5078 | -50.22771 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a9d58a0-d991-3ae4-8f5b-8c006ab824f1 | -2.90249 | -50.70619 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfc6e368-fea0-30a7-b4b2-f57fd8df332c | -2.69152 | -46.22847 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e129be9-de3c-353e-92eb-e6ce71841770 | -6.04445 | -46.60425 | 2024-11-19 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5e311ee7-21a5-3566-aee5-3ded826b9d05 | -1.1452 | -51.6952 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README28.md)
