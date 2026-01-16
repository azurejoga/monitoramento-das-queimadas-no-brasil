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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed2221e8-a7ba-3cd2-af62-7d383ffb6d00 | -18.82384 | -51.60682 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c86b1dec-09d5-392d-aa0a-e007468e4898 | -15.38592 | -47.27959 | 2026-01-16 04:18:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d18e8fda-3a81-39d5-b591-bc01fa431e06 | -15.43129 | -56.32584 | 2026-01-16 04:18:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 46aeebc4-5543-3858-94a9-53c5a5103087 | -13.69001 | -55.68043 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd49c21c-7d09-3d11-9d52-39290bddb623 | -15.44287 | -56.32847 | 2026-01-16 04:18:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc25e4b8-a19d-3c19-abee-fbc86dae9e7c | -13.69578 | -55.68159 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3fb0d9e-48c5-3301-9e29-586654d1b876 | -19.17347 | -57.54481 | 2026-01-16 04:18:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3513a023-16da-3c4c-88cb-c09dec86902d | -17.6189 | -46.65778 | 2026-01-16 04:18:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffa6fe9c-ad64-3f6c-9012-760c72b1ec6f | -16.65822 | -43.35404 | 2026-01-16 04:18:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9087c387-76de-3651-a771-afa9cc488c50 | -18.8136 | -51.6165 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8cca13c7-0624-3246-8ae4-a614f35545a2 | -16.11316 | -56.75425 | 2026-01-16 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d9841846-b2d3-3d54-8d40-392fe4e1a768 | -20.4499 | -45.17216 | 2026-01-16 04:18:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ce5c3cf9-5088-36fe-8c44-9c348ae9ac22 | -19.17442 | -57.54053 | 2026-01-16 04:18:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 16f3614d-7d36-3d9e-8112-b94f2803d5c1 | -15.77869 | -55.75296 | 2026-01-16 04:18:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 228f5217-9a9f-344c-992b-7659976e4326 | -15.442 | -56.33271 | 2026-01-16 04:18:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d21cb8b-3c0f-349f-ad8c-6d9c9cc37a2d | -17.61226 | -46.65662 | 2026-01-16 04:18:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dab099c9-8049-3a2f-9b46-b391f1b8b45d | -18.81503 | -51.60898 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b5b3ca10-90ab-301a-a6b6-fde1dda0b5e4 | -18.81574 | -51.60522 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 0889d22c-fe71-3fd5-b213-104189083249 | -17.70875 | -53.48396 | 2026-01-16 04:18:00 | NOAA-21 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc90c9e9-2406-3bd0-b515-caaf60acb142 | -18.90793 | -41.94256 | 2026-01-16 04:18:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dfde646e-3727-3fdd-8ca8-ff08f76fee23 | -16.10636 | -56.75735 | 2026-01-16 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58bc49a3-8632-315a-b052-f12e283760de | -13.69492 | -55.68578 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 16d32ad1-58a0-3b1e-ae78-f5ba801a4bf8 | -16.61896 | -40.70148 | 2026-01-16 04:18:00 | NOAA-21 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 02f9ca6a-5d40-350a-936f-abd80fe6050f | -15.71987 | -43.27994 | 2026-01-16 04:18:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09f0ca03-2bc1-37ad-add8-f7045e528aad | -15.01899 | -48.66034 | 2026-01-16 04:18:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cb760f8-2248-3989-9595-61479ea7ecee | -15.58764 | -57.34025 | 2026-01-16 04:18:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9b8b50c-8a9f-3d3a-affe-ab624823449c | -16.08791 | -45.17277 | 2026-01-16 04:18:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7876e80-2919-39c0-9749-fe3c84d22b0d | -13.68916 | -55.68459 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9aeb1584-3935-3868-ad33-32a9cebc7b53 | -17.61558 | -46.6572 | 2026-01-16 04:18:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e8e09b8-e8a9-3aa8-8f0f-f4c44fa7316b | -17.62222 | -46.65836 | 2026-01-16 04:18:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2490a1e3-5417-3e66-a8a9-f98a3297cc0f | -18.82911 | -51.62338 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0a40d2d-d9be-3916-9f86-b420ca754d99 | -16.13728 | -40.40622 | 2026-01-16 04:18:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f44da47-f786-3565-ae99-11bdd18d772b | -15.43042 | -56.33006 | 2026-01-16 04:18:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9c6f1339-c44c-3c15-9e07-e00ac6a0bf48 | -16.10539 | -56.76191 | 2026-01-16 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d0a83fc7-9dc6-30b0-a5c4-5af5739e86d8 | -16.09121 | -45.17331 | 2026-01-16 04:18:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f60badb7-cf98-31b8-a510-de71bf88f0da | -18.82647 | -51.61511 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0e30f12-9d1d-30a6-a490-bc7e7976fa3a | -13.69663 | -55.67742 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca70da41-d452-38a8-a48d-af89de7edb1e | -19.95492 | -41.21522 | 2026-01-16 04:18:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f7116eb-b476-3f84-a41c-794bc2dbfb18 | -18.82454 | -51.60311 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09e45ade-7568-39df-a2e6-04b86318d340 | -13.69086 | -55.67628 | 2026-01-16 04:18:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a45be8e2-1156-3858-baad-73c7a274cac7 | -18.81431 | -51.61275 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6e0331ed-2986-3291-b393-2f27b8b6ab98 | -17.62338 | -50.35641 | 2026-01-16 04:18:00 | NOAA-21 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1709c597-8e1b-379c-a062-f6f64658991b | -18.81097 | -51.60823 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14054858-d085-3799-9fab-21c22e636e91 | -16.21881 | -45.66006 | 2026-01-16 04:18:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 862fe3ab-6c44-33fb-8a33-ddca1075f6d5 | -15.59239 | -57.34314 | 2026-01-16 04:18:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c2885f3-78f1-38e0-872b-199ce0942bcd | -18.81168 | -51.60446 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6694824-8d06-3b38-9d63-26ec47c2d054 | -18.81908 | -51.60975 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d91431e6-816e-3314-913b-0198664fec29 | -16.10146 | -56.75142 | 2026-01-16 04:18:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14225fd3-7f98-333e-a739-dba770446fd6 | -18.82982 | -51.61965 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b062cb82-71b4-3496-b18d-f7e15c6c684b | -16.13329 | -40.40554 | 2026-01-16 04:18:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d956bf4f-8626-38ad-8d4f-f3aff7fa054c | -18.81767 | -51.61724 | 2026-01-16 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d219c575-6b46-36ad-953c-4d000a15895f | -20.01921 | -44.59689 | 2026-01-16 04:18:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0ce12dd-0946-3c24-86ef-8c357d2a4ba1 | -18.8124 | -51.5914 | 2026-01-16 04:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7516f97a-32b3-38c9-b7d5-8b70a7d62485 | -13.6993 | -55.6773 | 2026-01-16 04:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a70de07d-9987-341c-a9f4-f0e336399dfd | -18.832 | -51.6099 | 2026-01-16 04:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4da63dc8-a653-3d49-8810-44b46b0e01fc | -18.8119 | -51.6134 | 2026-01-16 04:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 71a4de6e-9461-3173-84bc-05e95f7fb046 | 2.7634 | -60.315 | 2026-01-16 04:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 46dfff00-b7ec-33c6-ab73-e1868e19a019 | -20.43562 | -57.86074 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6ec9cd95-4984-3743-b5bb-2bbedada733e | -20.43464 | -57.86511 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3a585384-46a0-3e5c-b05e-05ad4f6dd0c6 | -20.72697 | -55.16572 | 2026-01-16 04:21:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8af7dd66-51fd-3698-9abe-a1c8a6995260 | -20.72538 | -55.1638 | 2026-01-16 04:21:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1475e3b-582e-3cc1-9faa-f15f5bdf9335 | -20.43573 | -57.83315 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 770e3c54-491a-3f12-9ec3-601c9547ecea | -20.42986 | -57.85929 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6ebb0d96-4d81-348a-80cc-6b1dccfb61b5 | -20.73182 | -55.16696 | 2026-01-16 04:21:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa202f55-ca31-3dbc-b97e-48b63d2daeb8 | -22.84687 | -42.80938 | 2026-01-16 04:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02630365-499d-3d3e-b353-08a379a74e40 | -20.44041 | -57.86657 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e57332a1-bac2-30c0-8dcb-7268b94d13f6 | -20.72824 | -55.15976 | 2026-01-16 04:21:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f84a83e2-fc80-3c7d-8bb2-65dcca44ed17 | -22.70202 | -43.35492 | 2026-01-16 04:21:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea557037-dc84-3177-916b-d15b84affa89 | -22.57447 | -42.02485 | 2026-01-16 04:21:00 | NOAA-21 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1b4a8827-d599-382f-9d50-5746afc729c0 | -25.50485 | -50.96997 | 2026-01-16 04:21:00 | NOAA-21 | IRATI | PARANÁ | Brasil | 4110706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 80062e03-bacb-38ac-a3ee-6a61f95e4873 | -20.43084 | -57.85493 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c7e2a7eb-6584-36e6-890c-e89af90cf276 | -27.66917 | -51.24431 | 2026-01-16 04:21:00 | NOAA-21 | CELSO RAMOS | SANTA CATARINA | Brasil | 4204152 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 89a70676-2a99-303d-96da-5109cfcffba9 | -20.42617 | -57.82157 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 39de8f22-2f85-3b9a-92f3-6e7f506be3b7 | -20.44051 | -57.83894 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 8f4dacfb-559c-3082-bc48-bec57d8f9d06 | -27.07887 | -49.55632 | 2026-01-16 04:21:00 | NOAA-21 | IBIRAMA | SANTA CATARINA | Brasil | 4206900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 99405d89-615a-3692-9080-7b81a16a1d77 | -22.8537 | -42.90628 | 2026-01-16 04:21:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 88d5a2d8-8dd3-3a6c-a01c-abcb1177b24c | -24.95833 | -49.28947 | 2026-01-16 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bce3fcaf-252b-3a4d-b08c-17924ddba9cd | -20.44148 | -57.83459 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 4467b5a2-7777-3cea-8db1-a4862cdbf866 | -20.43095 | -57.82736 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5c633748-e377-3b93-a900-6845033d4162 | -20.73025 | -55.165 | 2026-01-16 04:21:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 84572a68-72ab-30ec-b398-f6dfd73c140c | -20.73147 | -55.15903 | 2026-01-16 04:21:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f8878b8-c749-3dd6-9713-d4419e7c3381 | -20.73309 | -55.16098 | 2026-01-16 04:21:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3231c537-f96f-3479-9e0d-73b4cd25bf12 | -20.4367 | -57.82881 | 2026-01-16 04:21:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5df3443a-7124-3342-b786-8c6391078796 | -24.9617 | -49.29008 | 2026-01-16 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08955051-d703-3fcf-adf8-bcd0dbc936c5 | -27.68742 | -48.75068 | 2026-01-16 04:21:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ba767391-1486-3b75-9495-ba11748e4229 | -29.95119 | -51.61619 | 2026-01-16 04:23:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 11a09c4d-3e56-3333-9faf-42cfc914763a | -30.31908 | -50.99871 | 2026-01-16 04:23:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| f28096dd-3837-304d-b18b-e2efc8646ac6 | -29.84131 | -50.98843 | 2026-01-16 04:23:00 | NOAA-21 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 62107cc6-adc3-3aa0-b870-2b9df105b2ac | -18.8119 | -51.6134 | 2026-01-16 04:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 9873888e-aedc-386d-b532-f98d0a0aa503 | -18.832 | -51.6099 | 2026-01-16 04:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f3f1d75a-2fec-3615-9fd9-83a96905168e | -13.6993 | -55.6773 | 2026-01-16 04:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 52481079-402f-3336-adbe-0256fd91dee0 | -18.8124 | -51.5914 | 2026-01-16 04:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 898fe80e-fff5-330c-b0f9-9b66b1957e22 | 2.7451 | -60.3153 | 2026-01-16 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 72d1d72c-14d2-322b-b11c-9fb99fb0ccff | 2.7634 | -60.315 | 2026-01-16 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7007db28-e9f5-3168-91fb-0d360986e728 | 2.76617 | -60.32924 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d00dc7ed-0591-30fb-b8d0-a067c4cfe6f5 | 4.24547 | -60.79272 | 2026-01-16 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bae3dcef-d145-322a-9231-a7192cc97c0e | 4.24855 | -60.79345 | 2026-01-16 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8924941d-9958-362f-b68f-355505deb4a7 | 2.75717 | -60.32386 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 086e4128-eb09-3c01-af33-6fa04e75153b | 3.06371 | -60.1053 | 2026-01-16 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cfd1c10-f591-37ce-8afb-cdf3607e47e2 | 4.24647 | -60.79969 | 2026-01-16 04:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README7.md)
