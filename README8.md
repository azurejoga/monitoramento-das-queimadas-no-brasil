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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23c9f1c9-817c-3e9c-9418-b4cbd2a55e04 | -6.49774 | -42.22177 | 2026-07-11 11:45:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| c719a034-4ecc-3396-a98d-a4f3e57748bf | -9.34128 | -40.46181 | 2026-07-11 11:45:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 45170c37-2bb2-3349-b6ef-9f8a93188aeb | -7.01532 | -45.42124 | 2026-07-11 11:45:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 07a54feb-58d8-3084-bbe6-29e1dc1f456b | -6.49949 | -42.21633 | 2026-07-11 11:45:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 9159e86a-c3f4-3aa4-816e-f768cfd9cccb | -4.81796 | -45.23366 | 2026-07-11 11:45:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cb824bc6-a06f-3ffe-943f-3647a12b2c66 | -4.9706 | -37.9405 | 2026-07-11 11:45:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 2130ea85-6e0b-38cd-a276-4d13b5733b31 | -5.83246 | -43.47635 | 2026-07-11 11:45:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b1d6ebee-f823-33a4-884c-90aae07d4cd0 | -9.34344 | -40.44472 | 2026-07-11 11:45:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 33.4 |
| ecfbe83b-6dbe-3053-9b9e-25b9fd72cc8e | -6.99765 | -42.91076 | 2026-07-11 11:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 3714f469-8333-371a-a1a7-0fba7ec08403 | -13.95438 | -47.79894 | 2026-07-11 11:47:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92091afb-39f4-31a7-871d-8ea78e8cdc03 | -13.42569 | -40.26374 | 2026-07-11 11:47:00 | TERRA_M-M | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| db0ff32c-8623-3968-bb5c-a02f46740593 | -17.56068 | -54.0383 | 2026-07-11 11:47:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8e6b50d8-c52f-397a-89bc-ded3e9a79974 | -13.81579 | -42.39957 | 2026-07-11 11:47:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 87a818e1-1986-3c7b-ac24-ea74e20fc2a4 | -17.57298 | -54.0404 | 2026-07-11 11:47:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f13ce234-9f8c-3446-a4d0-0c0b3f9252ae | -15.98402 | -43.69343 | 2026-07-11 11:47:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 756bfe40-95a3-3743-8807-c26c9d82596e | -13.80485 | -42.39809 | 2026-07-11 11:47:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 7ca793fc-e4b9-36a9-b911-2f77fe44adb1 | -12.02504 | -42.76346 | 2026-07-11 11:47:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3ad201f5-6312-3839-9142-e94a96fba6b1 | -13.6252 | -43.71595 | 2026-07-11 11:47:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1376c353-3444-314f-93db-47aa466ec7f3 | -15.98559 | -43.68076 | 2026-07-11 11:47:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 507ea651-ff63-394e-a72c-dd3207c447c9 | -12.84773 | -44.36287 | 2026-07-11 11:47:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ab684cc7-818b-3b26-b506-c28fa7dbf7e1 | -13.72497 | -42.94267 | 2026-07-11 11:47:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 3854cb66-7395-33eb-b85b-1e8b27bb046e | -17.07039 | -45.40971 | 2026-07-11 11:47:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7453a0b3-4981-3e13-8949-8e029bfd9b7c | -13.54564 | -40.35128 | 2026-07-11 11:47:00 | TERRA_M-M | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 09bda37e-2fff-3c1e-b19b-2cbf39400424 | -13.4244 | -40.26987 | 2026-07-11 11:47:00 | TERRA_M-M | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 98597f7a-f03c-39a0-b86b-096a0974a735 | -21.80945 | -45.28348 | 2026-07-11 11:49:00 | TERRA_M-M | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| b0f6e9b3-1348-3da8-9c36-8fbd8a29aa6b | -19.72861 | -46.17089 | 2026-07-11 11:49:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b40bb666-6d23-3a0c-bcf5-5cea3aeaa7f8 | -20.14154 | -47.07582 | 2026-07-11 11:49:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 812c4d4d-eb94-31bc-b3ea-625d3b209563 | -22.48525 | -49.09196 | 2026-07-11 11:49:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a3d4f802-cc9d-31ea-abbc-6a2ca2055639 | -20.58311 | -44.30004 | 2026-07-11 11:49:00 | TERRA_M-M | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| 5f30595b-2857-30ab-8043-dd97205dd168 | -6.9979 | -42.9016 | 2026-07-11 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| db87b015-eaee-3d0e-904a-a7e76b2bf594 | -6.9979 | -42.9016 | 2026-07-11 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| bc5b96d9-382f-308e-af70-6c8cafa7c32b | -17.5703 | -54.0341 | 2026-07-11 13:40:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d7f05ce9-d636-3a7d-b546-44d375064769 | -6.9979 | -42.9016 | 2026-07-11 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| f9da8d7a-9118-39bd-8bc5-4e77d6948305 | -17.5703 | -54.0341 | 2026-07-11 13:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 223847b5-5c5f-37a9-aa98-3eb729678934 | -6.9979 | -42.9016 | 2026-07-11 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 327edeb4-0913-354f-be5e-68879af949d6 | -6.9979 | -42.9016 | 2026-07-11 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 9a07a2bd-bc59-3da4-9be7-50a08f51928d | -17.5703 | -54.0341 | 2026-07-11 14:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 2bbfe226-5fb2-3d6a-91d2-fd7f455eee7e | -6.9979 | -42.9016 | 2026-07-11 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 973c6d08-8030-3791-b2f3-6887a5f874af | -6.9979 | -42.9016 | 2026-07-11 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 736015ff-9bbe-39ae-b629-21be58944c84 | -6.9979 | -42.9016 | 2026-07-11 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 0f3439b4-a8ba-3fce-b92d-b2d33c6c2332 | -6.9979 | -42.9016 | 2026-07-11 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |


