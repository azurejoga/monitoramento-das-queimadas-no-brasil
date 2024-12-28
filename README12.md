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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f6cefe2-8655-31ea-9bad-b8db866b985c | -10.55645 | -37.04006 | 2024-12-28 04:16:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3f983a51-a0b5-352c-8d81-4eac72a7fa00 | -11.75972 | -44.86556 | 2024-12-28 04:16:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f6190fe-5f0a-3a75-bb05-3d13520964c8 | -9.2749 | -43.26427 | 2024-12-28 04:16:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cfc80bbe-769e-3666-a9b8-20254f6c2185 | -9.44257 | -39.08514 | 2024-12-28 04:16:00 | NOAA-21 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a78356bc-cd42-314e-90ee-fa58feacc146 | -11.13425 | -43.30566 | 2024-12-28 04:16:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b468229a-6124-3802-bdee-feed2a90ede7 | -10.42899 | -44.89066 | 2024-12-28 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7973846-cb86-388b-9b3b-cecf014ff874 | -9.26004 | -40.95579 | 2024-12-28 04:16:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ed8011ca-7143-3f11-962f-b3d0f94c8273 | -13.37852 | -41.79327 | 2024-12-28 04:16:00 | NOAA-21 | ABAÍRA | BAHIA | Brasil | 2900108 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0493e5a4-585e-349e-ba81-7abd9f95a67d | -13.17141 | -39.77705 | 2024-12-28 04:16:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c653ddfe-66b1-3b1d-a52c-31dc531d9637 | -8.12457 | -43.14084 | 2024-12-28 04:16:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fb035376-33af-3573-b625-5caa5d2d81cf | -11.75641 | -44.86503 | 2024-12-28 04:16:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 490d167e-1eb8-3327-8913-a779e8776370 | -13.17497 | -39.78099 | 2024-12-28 04:16:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ffd5e6af-a79d-3293-a18b-fd457a8e235a | -19.02351 | -57.62439 | 2024-12-28 04:18:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 81534529-c28f-3e15-84fe-d77ccdcdc9a3 | -15.09477 | -59.62622 | 2024-12-28 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9add91ca-1f03-3191-9fab-a84ce81c31f6 | -15.5146 | -59.42206 | 2024-12-28 04:18:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a914227-ff6b-339b-bd34-aad40762b7c5 | -19.02445 | -57.62016 | 2024-12-28 04:18:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aba1c810-ccd7-30a5-bf00-744c392fcf42 | -16.09946 | -60.07922 | 2024-12-28 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1911f833-3f2d-34d3-bc2e-7a0373db4ed1 | -15.09734 | -59.63029 | 2024-12-28 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5f9c152d-8951-3304-8775-d8466a402fb6 | -15.09317 | -59.63327 | 2024-12-28 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c641d9ab-c10c-38f7-a74e-8677378ce968 | -16.34888 | -43.69612 | 2024-12-28 04:18:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e346917c-b21e-3fae-bfd1-21b5dd4f91e7 | -15.98408 | -43.29502 | 2024-12-28 04:18:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc0a6126-7a36-33a4-bce2-baa51a66ba5d | -15.09036 | -59.6284 | 2024-12-28 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 675e451b-bab8-314d-90dc-258404ec39e4 | -16.10122 | -60.07162 | 2024-12-28 04:18:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| eee7498a-217f-3b18-ac16-0636a74e149d | -15.52156 | -59.42341 | 2024-12-28 04:18:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2715ce17-63e3-3e40-acea-63f4da5be298 | -23.40686 | -46.55648 | 2024-12-28 04:21:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dddbbe8d-7500-3f24-bb50-4db853a7b32e | -23.59384 | -47.43848 | 2024-12-28 04:21:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 31645168-adee-31cb-acdf-fb2d4d9b19e7 | -24.24444 | -50.74082 | 2024-12-28 04:21:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d56fad63-24a9-3406-8b32-1447d23ede42 | -26.76695 | -53.64277 | 2024-12-28 04:21:00 | NOAA-21 | BANDEIRANTE | SANTA CATARINA | Brasil | 4202081 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 41b836f1-02fd-325e-a1da-ba3aceaa9c8b | -29.72219 | -50.55827 | 2024-12-28 04:23:00 | NOAA-21 | ROLANTE | RIO GRANDE DO SUL | Brasil | 4316006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2cd959f-a120-32ba-941f-dbd9b9de857f | -4.13101 | -46.68528 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7b9f927-b37c-3046-8952-ccca3d4c70ff | -3.8174 | -46.72975 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9e25270-f58e-3e0c-a955-19931c727a1d | -3.7383 | -47.34631 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b328fa-58e0-3096-81ad-a1c4f6e8caf4 | -3.77305 | -47.19003 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35b6d128-4c50-332c-8d01-8e5d05d51b16 | -2.70519 | -54.06148 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6f496b0-61be-3415-a500-9594e4e41461 | -3.95981 | -46.67512 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47d9e00d-3fe1-33ac-a8e9-9ed4bab400e4 | -5.09546 | -45.09921 | 2024-12-28 04:38:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e33bd70-193b-365b-a219-8267bce1d1be | -3.92729 | -46.62792 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2d65606-506c-3490-9c31-8ae3d5645426 | -1.42766 | -53.70266 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fae9e2d-7e09-3272-8d59-e2d06439c2c9 | -4.12751 | -46.68479 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 701cd86c-22d2-399c-86c8-d45774b2ec1f | -3.8851 | -46.69236 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b128cd5c-fd8b-3ea1-b1ad-560fd2c73a2f | -4.27756 | -46.83561 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fce376d-5b51-3451-ac1c-c3a648d3a819 | -3.19007 | -46.12692 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86c24cd0-8ac7-3b7c-9ac0-6d6f05c9930c | -5.90827 | -43.47945 | 2024-12-28 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c7c56fc-60e4-355c-9bfb-e1a958a59d85 | -3.91641 | -46.88004 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb95c72b-837d-35a0-b25f-313bee55ed5c | -3.19477 | -46.00051 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d14c28f2-719f-3297-8bb0-951a9fdd06d9 | -4.04066 | -46.70737 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c19e501-d341-3fb9-85c2-13c97db5b4f0 | -3.90237 | -46.98124 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ce49d36-38ed-33aa-88f3-e2ab0cb01a89 | -2.91244 | -54.01139 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02a1b1bd-0633-37df-aed7-5314733ae9f6 | -3.83793 | -46.68981 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23c80ad4-5830-3edc-ac85-b95231c333de | -5.7418 | -44.43088 | 2024-12-28 04:38:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90564702-22e4-3029-b2b7-26f1ed50e152 | -3.997 | -46.91855 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| befa6049-89eb-317f-ab9b-0212303cf8de | -3.81392 | -46.72923 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc6cf7e1-1934-385e-ab9b-f5efd00dc380 | -3.9162 | -46.93702 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9a1cac7-d21e-33ec-aaa2-7e48f5d1d96e | -3.84206 | -46.69359 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45fefe19-a826-3645-9a66-7dd7da73d71a | -3.93937 | -46.76224 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bd974f7-cb10-3578-b218-2131d3ae91e9 | -3.99235 | -46.69608 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9838438f-49db-3e37-9113-7fdfa4e78c2c | -3.89641 | -46.98492 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f923fb3-6ff8-309b-abdc-6b052f93ed61 | -5.57231 | -46.13082 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1e5c1b88-4e3b-38b1-b726-08c6e45e08b4 | -3.87812 | -46.69132 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9646281f-bd72-321d-ab6b-41fb79ea8d4e | -6.01082 | -39.27667 | 2024-12-28 04:38:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b0a010e6-b13e-32eb-acbc-1dcec8a577d8 | -3.99573 | -46.74358 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c8fed56-d9bd-3144-abfe-7ea9b895c83c | -3.9662 | -46.68011 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe139e86-1d9d-35da-bfb4-9737c6787a2b | -3.97237 | -46.33794 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38dfa0e8-8304-32f8-ba75-fd41471e0187 | -3.81962 | -46.62396 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 152fedc4-5269-31fa-bb8f-56c75e3057d3 | -3.89117 | -47.01838 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a815573e-5983-34db-afbd-c5a174dc51d6 | -3.86711 | -46.66994 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7257202-97b3-322b-9bb2-78662e975e6b | -3.53685 | -53.79881 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9c49a9e-067c-34b6-a0f8-ef01ec98497e | -3.9133 | -46.90969 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 529fbd6f-d421-391d-b965-6e56ae8f0622 | -5.5796 | -46.13199 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 530125b5-d796-3172-b4ff-1c6f00b51dc5 | -3.89724 | -47.01474 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6474c373-4796-30f5-abc2-27ac4355e8f9 | -3.89954 | -47.02274 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9213332-3895-3b2a-ba40-a73bc23c5cae | -4.5573 | -44.12481 | 2024-12-28 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13a8db6c-19d0-3d07-bb7a-1d7536c4ecfd | -2.70104 | -54.06091 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f4b7db5-2710-36be-8be7-10523a3358ef | -3.53572 | -53.80576 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d29ee010-6c96-36dd-bd83-bf2612886479 | -5.91258 | -43.48017 | 2024-12-28 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfb42b9f-509b-357c-959d-871f26e7f84c | -4.00794 | -46.57158 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66f21577-34f6-3f22-8dab-4c54f3d9d1a3 | -3.80013 | -46.86284 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a4daad3-5155-3ea6-b4a1-9bb731a06f80 | -3.8181 | -46.70247 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 718ad014-999b-3433-b8fa-6e1a460bbe47 | -3.97218 | -46.89572 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7353a51b-c6a5-3b3b-b7f5-3702b37a83cc | -3.90702 | -46.9173 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 085ea4be-f78a-3b25-8831-38cf8fd9ff73 | -3.94951 | -49.44305 | 2024-12-28 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26bde1d7-1855-3de3-b0f8-2516b50ba3f0 | -3.79667 | -46.86231 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 844b90c0-78f9-39ef-aec5-edbbad6d4eb0 | -4.04584 | -46.71994 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6948b0e6-696c-3411-b6bd-7bd53d56d70b | -3.93058 | -46.98163 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 00d32a18-2c02-306b-a76a-08f2b5213838 | -3.91841 | -46.66199 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f8dc6eb-fdca-3e10-95cc-14ac417e03ab | -3.20081 | -45.98486 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f429fe1f-9efe-31f3-ba59-3affdcf8f29a | -3.77184 | -46.60876 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25d61013-7de5-3506-a508-d7c7c43a2805 | -3.81767 | -46.0614 | 2024-12-28 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d9cd1e1-dfbd-3ef0-bda7-ae42210572f3 | -3.99927 | -46.72069 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2ef6046-a212-384a-87bb-071decd05462 | -6.39442 | -38.90742 | 2024-12-28 04:38:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 081c1c97-4420-30fe-8731-58dd08dcbdda | -3.89667 | -47.01846 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b42323-d9f9-3aac-9330-7bbd9caaebdf | -3.99582 | -46.92611 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02ef83a0-5980-36a4-b47f-6034e8588cc5 | -3.93576 | -46.99388 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70e11e44-214a-350b-8469-701e64eed404 | -3.84909 | -46.67095 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8180ec23-7163-3af1-a0da-e99ec1bbcda6 | -3.96911 | -46.68447 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d07f8547-4378-3917-8416-200761802167 | -1.42354 | -53.70201 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9cced75-0719-3769-8735-f546d144932e | -2.29205 | -45.57231 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65f2fe16-4437-3f24-b514-8635948eb180 | -3.03711 | -53.9089 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1a70117-fb43-3e1b-9882-5c9c919e3c34 | -3.90762 | -46.9135 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1a9abb8-93b8-36b6-849f-4c40d671ab73 | -3.99295 | -46.6922 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
