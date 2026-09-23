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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49701f24-622d-3d20-9f1a-f065b6c2fee2 | -6.61841 | -43.74847 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 31dd1513-79b6-3c80-90da-6c858ab2afc1 | -4.28484 | -48.60743 | 2026-09-23 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 829f705c-0dd9-3d42-9fe5-17e580e89fb8 | -6.60547 | -43.73839 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 572f90ad-8cca-3bda-ba27-a4b2a47c738e | -2.95101 | -51.0409 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d19835d0-1ed4-3106-a849-b239bdace5d0 | -5.99468 | -45.23304 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c6939d4-185c-3f48-b93c-f21d599e2ed8 | -3.50354 | -53.20628 | 2026-09-23 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f2202c2c-9013-3312-bb8e-56a9034aff92 | -1.8289 | -55.71896 | 2026-09-23 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fadd5d7a-de5d-3c6d-9411-c048d5ab6df0 | -4.44899 | -55.07298 | 2026-09-23 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a48a66e0-3d2b-3082-8039-ed913b197ae9 | -2.8957 | -49.1665 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26973935-e844-34e8-8211-aeb7b66d0534 | -7.31825 | -42.2653 | 2026-09-23 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| af0d417a-8852-38df-a4d4-3fe9b2e00e36 | -7.32063 | -42.26402 | 2026-09-23 04:25:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b1f2717b-c62b-3d1a-9e77-7f1b22daef3c | -7.16143 | -43.02147 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c53871d2-c2f0-3b04-93c5-9b25956b9c35 | -5.77895 | -43.76525 | 2026-09-23 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bab21ac3-94fd-3cb5-a962-23469af81984 | -1.39523 | -49.05169 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e212ffa5-bc01-3fc9-a020-58023cc32e72 | -3.55768 | -43.46883 | 2026-09-23 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7ea609f-eeee-37e1-99d3-ea802c99006a | -3.00658 | -54.17411 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 418517ac-a8eb-3d86-9dc1-764ad74bcdbf | -7.08043 | -42.07399 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6d89dd32-f310-3506-a29e-004983c86409 | -2.8234 | -49.24547 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d66fc5f2-4592-3bbc-a34a-5d27c1cea851 | -3.28854 | -53.26204 | 2026-09-23 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbb3a6c8-267d-3c25-bb2c-90b08ccfe344 | -3.44613 | -50.61433 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a747bd62-5fd1-39f9-83a5-6e949798766c | -3.45935 | -43.36519 | 2026-09-23 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c328e568-e1a1-3a6f-bfa1-e1ef2f2c05be | -5.04567 | -49.22895 | 2026-09-23 04:25:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d6b6bc2-de94-3df0-8f47-479151642ebc | -6.8928 | -43.75375 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6561562a-1838-3d4c-b9c9-ec041c063758 | -6.10572 | -44.14717 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51276ea4-5598-30e2-b65f-433425212e93 | -4.29619 | -49.13011 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dee3e1b3-673e-37d0-99c8-a292772017f8 | -2.95847 | -54.08658 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a1ac9cc-2678-3ce6-a668-3052e74ccff7 | -6.61435 | -43.72743 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 075ecf15-da8b-30d5-ae5c-b6465462eca5 | -7.15961 | -42.08325 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6677d668-3f1d-3306-abdc-caabaf78d448 | -1.91931 | -58.26444 | 2026-09-23 04:25:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 887a6873-a6f1-34df-b08d-4fc5f1a9555f | -5.03163 | -42.47354 | 2026-09-23 04:25:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7cefc078-29fc-3f9f-8522-431706cd4db7 | -7.14401 | -42.08096 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7aa56330-9e91-3379-9b5b-b49419377b88 | -3.51876 | -51.6349 | 2026-09-23 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65d9ffe9-3069-36f2-8585-813dd8bc1493 | -6.1639 | -44.13688 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ddaee86-d3ef-3408-a2e7-a62f3ad784c7 | -2.88278 | -54.08083 | 2026-09-23 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe2aa285-663c-3e4c-ab65-c483c7ac81b9 | -1.38178 | -49.04057 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50f49b60-a160-3c36-8cec-a0f280b25938 | -4.30176 | -49.12977 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 749d3ae5-5dc9-3446-8503-06d35a679fba | -3.155 | -57.69431 | 2026-09-23 04:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aac44e10-7d48-367c-ba4d-1ec4d0eadbc8 | -3.16066 | -49.22313 | 2026-09-23 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 889da213-d684-30d3-97e8-f15d934a0460 | -5.61932 | -43.36476 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15333784-e81f-3ff8-a761-627d27c9d0cb | -5.76791 | -45.11518 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d04b7114-f6b4-33c4-9ad7-6e76282ffa4b | -6.57591 | -44.14692 | 2026-09-23 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7418ee9c-ce53-3eb0-9dd7-d8cf2d519889 | -5.34106 | -45.2802 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e28f96ff-8df4-3e94-8cfc-6035f9f11ee6 | -5.6235 | -43.36125 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46b73849-320e-3451-b9b0-15af1ef5733f | -6.88924 | -43.63409 | 2026-09-23 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0589a707-341d-3530-9a21-3202c346e65d | -6.10917 | -44.14774 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3e6254d-e04e-31be-90e0-e06dc9a1a4c7 | -3.28753 | -53.26482 | 2026-09-23 04:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86d58700-05cb-3760-a6ca-edb70708e74a | -5.6122 | -43.36366 | 2026-09-23 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e4b2613-3402-3e0d-8dd8-09e35047fd62 | -4.29816 | -49.12919 | 2026-09-23 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a1db38d5-665a-3db5-ac63-0b09423bccdc | -5.8734 | -51.9431 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81341043-448a-353f-baaf-4d4f40137988 | -6.84615 | -45.55246 | 2026-09-23 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57cdefca-f318-31bc-b06d-a9292dc91c08 | -6.00287 | -44.10907 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 779d8863-8c7b-3580-b80d-188d29bf5276 | -5.60586 | -44.02378 | 2026-09-23 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 155fc0a8-7687-3faf-bf91-42ead96bfd2e | -6.18638 | -43.34303 | 2026-09-23 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24c4013d-ca35-3a9a-8395-b3007ae56472 | -7.1266 | -43.07882 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0fda02b5-fe6b-302a-af92-e21adef3fa82 | -2.95065 | -54.07941 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16d8b013-990b-33c9-a280-554d11b1b657 | -6.32699 | -43.93155 | 2026-09-23 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b209a817-bb40-3633-bd0d-0997e5a943cf | -6.62021 | -43.7365 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| aa7bf70e-d9fe-32c3-a0b5-720e186730ae | -7.12835 | -43.09242 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd0b5a32-b3d6-3305-899c-8e06704871ae | -5.4644 | -44.32844 | 2026-09-23 04:25:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c58597a-fd63-3f34-9f88-6c9c920f7856 | -6.1377 | -43.84062 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b068981a-3d27-32f1-8266-d86d34cb3b50 | -5.03024 | -49.68043 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61384b8e-830b-3188-a67d-d6fc5aac4b19 | 0.28445 | -51.47687 | 2026-09-23 04:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92d80a14-514f-3080-8c94-c4ec54cdfc2b | -6.13887 | -43.85669 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d60b3b4-f380-3199-af02-1ec7c612e32d | -1.39894 | -49.05227 | 2026-09-23 04:25:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 95f75981-7260-3ec1-b77d-fcb6b0f29454 | -2.9534 | -54.08577 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0938fa74-b3ff-3dfa-8609-63f37e7f3342 | -1.82958 | -55.71492 | 2026-09-23 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d40991-a155-3a1c-8665-cf209ef7ce71 | -2.95524 | -54.08318 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b7317b0-094f-3c2d-a300-a58bf1a46686 | -5.76565 | -45.10759 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 32f0d559-0c43-3b0c-a456-fdac6037d01c | -7.13699 | -43.08477 | 2026-09-23 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f41b2522-380b-3b98-b441-ee235f337da0 | -2.97094 | -50.39357 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f9a17948-5586-3f8f-84d5-ffe856077b08 | -6.34236 | -43.36993 | 2026-09-23 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37bd3abd-8107-3a94-8813-4e8639096224 | -5.16701 | -45.43871 | 2026-09-23 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 454b9e23-dd67-3f1d-a535-d8c4393ddf1f | -1.32818 | -54.66267 | 2026-09-23 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 84624ece-d463-33cd-bc23-b5a0be088db1 | -5.34819 | -45.1694 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e213c66-9161-39cf-bce0-4b78537118a7 | -4.05171 | -56.31216 | 2026-09-23 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 729029c2-ed00-3cab-a631-64454fb68eff | -3.45781 | -43.36397 | 2026-09-23 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a868905-a411-378d-adfb-d2e399767df5 | -4.56581 | -49.5583 | 2026-09-23 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04b77214-5990-36d3-935c-c465f3294b81 | -2.94933 | -54.07906 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2b0de11-4565-3ed7-ad59-2e0ef9e233a9 | -3.93923 | -49.99168 | 2026-09-23 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcfcba81-ffc6-332d-8516-e11b080d48a0 | -5.35789 | -45.74217 | 2026-09-23 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a75477f7-245c-3c97-8b66-ad7b4ead94ce | -6.72154 | -44.15075 | 2026-09-23 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fc222017-5ebe-3171-a8a9-602ae18e71ac | -6.1086 | -44.15149 | 2026-09-23 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30aeba46-bd2d-3716-83ce-ba9310a04207 | -5.87216 | -46.26463 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65a455c2-3caa-3776-b3e3-45bb3622c9a9 | -6.44444 | -48.44018 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e62bb70c-8863-3cf0-8a20-20f672c49c01 | -3.45477 | -50.61131 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9eb4536b-d3b4-3b00-bdb4-dfef197a8a3a | -6.72097 | -44.15458 | 2026-09-23 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b3017301-2788-346b-9c21-0d35d6e64be5 | -3.06821 | -54.39261 | 2026-09-23 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98acba60-56c8-3680-ba24-3fe5a03c2485 | -6.0563 | -46.3498 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab546d0b-dec9-325b-b451-75188250c24b | -6.98074 | -42.59472 | 2026-09-23 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 010a4b1c-459e-3d61-b448-7736826e84b6 | -5.34929 | -45.16235 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fc90764-0293-3274-98ae-0192429ca351 | -6.62254 | -43.74501 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f92180a9-88f4-3136-b69d-8ad852755eeb | -5.31546 | -49.0569 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5f14285-03fb-3175-adc2-4b2710e402a8 | -3.52847 | -44.84178 | 2026-09-23 04:25:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48734013-39bc-36ae-82e8-15d06b3490fd | -2.94363 | -50.48838 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd1172ab-f4d2-3717-89e3-5f0aa2725311 | -3.03311 | -54.41215 | 2026-09-23 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f17b62a-235c-3c4c-ba55-2a92a728f7a9 | -5.60562 | -45.94389 | 2026-09-23 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea1aca95-6ae4-3f69-a9a7-34fa6ef6ed00 | -5.62164 | -45.24752 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5c5384fc-6cc5-3328-856c-e01fef05e96a | -6.27866 | -43.79316 | 2026-09-23 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be2e9616-cd00-3f5f-af12-154c5544918f | -5.40871 | -49.26662 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ab8e4ce-a37a-336a-8740-e3e53eadc7da | -3.85722 | -58.82225 | 2026-09-23 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |


[Clique aqui para ver as próximas entradas](README51.md)
