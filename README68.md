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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d637e2d3-29ed-3a01-ba31-d8a686b65dc3 | -18.82547 | -48.24845 | 2026-09-19 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e349f53-1213-392f-82c0-dc183bbc9adb | -19.56216 | -47.66697 | 2026-09-19 04:42:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ff7ea0b-e84c-394e-89ca-80950208c85e | -19.56616 | -47.66368 | 2026-09-19 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f99ea8c-2bae-3b8e-a3a7-ddf7fe793977 | -20.90299 | -46.34494 | 2026-09-19 04:42:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 28dcba6a-a344-3fa4-9ab4-66cf8958560b | -19.0571 | -46.3559 | 2026-09-19 04:42:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31beed35-a8be-359b-8e69-b609a765b81e | -19.56499 | -47.6714 | 2026-09-19 04:42:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9dd9e9f1-4591-3e68-b22a-d7f74aaf5783 | -21.76985 | -48.48286 | 2026-09-19 04:42:00 | NPP-375D | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f2fd80e-b1bc-3489-8584-811f3b66c4ec | -20.85079 | -49.06733 | 2026-09-19 04:42:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 1c1dacb5-d11b-3d16-8730-f57c6b121659 | -19.56899 | -47.66811 | 2026-09-19 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbbf7687-a091-30c4-9b96-5a5ed545bf96 | -18.81206 | -48.24613 | 2026-09-19 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f622a1ed-017f-3751-8216-8622943f4c76 | -16.80211 | -46.98321 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c4029d0-d468-331a-af72-8b6a31230ccc | -18.0235 | -51.07557 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ac944e6-2d82-3849-8353-4205b33fabd4 | -18.82851 | -47.93521 | 2026-09-19 04:42:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0f3d3da7-f432-354c-bc17-23c70a2d86f1 | -18.02417 | -51.07164 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a2996166-24cd-3f4e-af5c-fcb18b5b42bc | -18.82882 | -48.24903 | 2026-09-19 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4090e348-0713-3ce1-be66-1b574d038168 | -16.11845 | -51.93893 | 2026-09-19 04:42:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50d7c6b8-df01-37fb-8d9f-f70db117e2c5 | -16.30843 | -53.85941 | 2026-09-19 04:42:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc50759c-07ec-3d9d-872b-afd5775c4d32 | -19.45914 | -45.65137 | 2026-09-19 04:42:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3962439e-b324-37c5-a096-4b0d391f7212 | -21.02455 | -47.2611 | 2026-09-19 04:42:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43af2f0f-99b1-3c5c-a603-aa445cfe3a79 | -18.87613 | -49.51046 | 2026-09-19 04:42:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 789b8260-f2a0-3e59-8b4f-1cb3fef47c33 | -19.44765 | -47.56886 | 2026-09-19 04:42:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c60eaadd-afdb-3592-9c82-7b6ebee0cff0 | -20.85137 | -49.06361 | 2026-09-19 04:42:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2e73cc02-1b7d-3c00-a6c7-cc6e67628023 | -16.79699 | -46.99406 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41aa66b0-5096-3d0f-8ab9-72031edd7c93 | -19.19571 | -46.84152 | 2026-09-19 04:42:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79f14c67-af43-3868-801d-15edb8349f98 | -18.8728 | -49.50987 | 2026-09-19 04:42:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1f009a2e-be41-33ed-b310-1f55fbc06002 | -18.33497 | -44.01365 | 2026-09-19 04:42:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0347d993-ba41-371a-9904-92d3ca0da7ff | -18.82907 | -47.93147 | 2026-09-19 04:42:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 29ec0c56-fbcf-3e1a-9e2e-db42839d58bd | -17.83387 | -44.84749 | 2026-09-19 04:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a8b202e-fb82-3733-b7f2-2c99ad37da8f | -16.31316 | -53.85648 | 2026-09-19 04:42:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2597ef8e-7fd8-3710-a270-b83d59e5e4bc | -19.56333 | -47.65924 | 2026-09-19 04:42:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b30d1ee4-fe9c-3740-864b-1e2a1badb227 | -18.01316 | -51.07368 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e877ff12-7115-32ea-84f6-9773d4559eac | -17.31539 | -46.6248 | 2026-09-19 04:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 491bd5d3-2753-378c-b408-f23812c8209f | -18.87555 | -49.51413 | 2026-09-19 04:42:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1410bcef-3963-38fe-9ade-fb4bad755019 | -18.0215 | -51.08743 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82522d15-02d7-3a3e-a457-9dba8398b5f1 | -18.92291 | -44.72587 | 2026-09-19 04:42:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 636e62a1-a1fa-3593-a8e8-c945f1a238e0 | -18.56684 | -45.8834 | 2026-09-19 04:42:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cb6095c-bb1b-33bf-99ab-359d0588acc7 | -17.95755 | -45.12357 | 2026-09-19 04:42:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 436ff2bf-3adf-39f9-a6be-b085671ca40e | -18.02072 | -51.071 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3915d8f8-83e0-37b1-b9b5-24ee394e96b0 | -17.95819 | -45.11895 | 2026-09-19 04:42:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60c94993-7ad9-312d-a535-f5dbe54f6e57 | -18.81819 | -48.25099 | 2026-09-19 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a7cd6b8-d0b8-3683-a0fa-167f8274b650 | -18.92221 | -44.73096 | 2026-09-19 04:42:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e723b8c0-affe-3d69-9da4-351698259a60 | -21.3122 | -45.47728 | 2026-09-19 04:42:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac4ca128-757c-3196-9d1a-6c5f6eeccf1c | -21.42125 | -48.4845 | 2026-09-19 04:42:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 365fc2bc-4aea-3577-8a81-9b567f5d01a2 | -18.86947 | -49.50928 | 2026-09-19 04:42:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c51f3dee-862a-3f2e-a59f-dfe76a726852 | -16.30912 | -53.85567 | 2026-09-19 04:42:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68431202-e2f3-3373-b915-337c987fd947 | -19.56557 | -47.66754 | 2026-09-19 04:42:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98f78750-3fe4-34e1-8cfa-8b72f9177eed | -19.56274 | -47.66311 | 2026-09-19 04:42:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ba721b8-0dec-3c19-bb8b-9a5be7b50550 | -18.01527 | -51.0822 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f11bf1d4-e640-32ec-bc34-92259aeff09e | -18.02695 | -51.07622 | 2026-09-19 04:42:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 566ba2b0-dbde-3444-84f7-4304deaea406 | -30.17512 | -55.01807 | 2026-09-19 04:46:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 15d7a263-4f50-3706-9e23-d4ef494a3107 | -30.15675 | -55.0184 | 2026-09-19 04:46:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 4.7 |
| afb0521b-a913-3686-97e6-df2fc33ab1d0 | -30.17241 | -55.01278 | 2026-09-19 04:46:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 92809e88-958c-34bc-affd-ba6c47224f22 | -30.15594 | -55.02289 | 2026-09-19 04:46:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| ab90b1e1-9e05-3795-a764-83625ddc6646 | -30.1716 | -55.01725 | 2026-09-19 04:46:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 28e93de1-fcf8-322f-8201-dc38a2aa5d7a | 1.25729 | -50.75219 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec47acaa-01ac-38b4-a5d4-5e15d4e7ebaa | 4.44391 | -60.4648 | 2026-09-19 04:55:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f49ea64-74c4-3aab-804c-dee468244584 | -1.83802 | -54.85431 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ac65f6-58c1-3ec0-be26-03c5df2d4b8b | -2.81546 | -50.47581 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91ed6ad9-4c01-3165-a528-e4869a24899a | -2.83407 | -50.46765 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d109b23a-b86a-36d5-995e-92b6a7856aa1 | -2.03327 | -48.77865 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1797167-3276-36ce-a9ec-eb27ca430f5e | -1.42444 | -49.42619 | 2026-09-19 04:55:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eee7af4-dbea-3b7c-8fcf-fd2d6bc355be | -2.82222 | -50.47686 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8875b2da-b9a0-3370-8230-36608aeb0c7c | 4.44022 | -60.46587 | 2026-09-19 04:55:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73eff231-3e65-3cc9-b75c-d2d9399c8ee7 | 4.19713 | -60.1004 | 2026-09-19 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6945432a-4b6a-34d8-9b78-8ee12848431c | 0.25282 | -51.36088 | 2026-09-19 04:55:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a8527f9-bd95-30aa-a463-911438ca9aa5 | -1.71079 | -54.89216 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6959875b-1e77-392a-aa31-6a64d8e87b2c | -1.58041 | -54.43243 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f59b10c6-53bf-3cc1-a99f-ad9dd7560735 | -3.03382 | -48.41603 | 2026-09-19 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ced78f1c-a931-3de6-b32a-57e2a0087256 | -1.09531 | -48.06038 | 2026-09-19 04:55:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d091a6c3-4128-31bb-87a0-828293e797e8 | -1.14757 | -54.16998 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b62af32b-0b4d-33d4-8bd4-6d2bdd666a3a | -1.65793 | -54.922 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63905043-c7a3-382c-9d16-a91ef340d7a4 | -0.85449 | -48.71956 | 2026-09-19 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45f2caec-5f8c-3767-aa5d-295193d2665e | -2.8224 | -51.33678 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16cc67e3-44fc-30fa-bb04-37a24b612e35 | -1.56966 | -50.06282 | 2026-09-19 04:55:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3b5a3df2-5397-3fdc-8eb6-60761d7ba5ad | -2.6028 | -49.50656 | 2026-09-19 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a991cac0-7e3b-3297-a762-a7808d69b1d3 | -1.60032 | -54.44379 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28d230ab-71be-33a4-a725-bca5487d8cac | -0.266 | -48.41084 | 2026-09-19 04:55:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9f9c34f-6864-3714-a08c-b929b355fd17 | -1.67535 | -54.92904 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae188d5c-a04a-35ca-9eac-ed778dc643c9 | -1.22668 | -55.73134 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd87eee6-b994-3f6c-bb8d-94b27ec21257 | -2.45392 | -50.37214 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b9526f-fd64-36c1-a933-9eccced5d49a | -3.23801 | -46.94316 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6136ca8-9c05-3a94-a90b-191529cafce9 | 2.51244 | -50.84666 | 2026-09-19 04:55:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 049ad484-f861-3a65-b8ae-039d02f68636 | 4.1977 | -60.1043 | 2026-09-19 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7a90bf4-9d11-3901-997c-f953453b83c5 | -1.49271 | -54.97413 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75f02ba3-4e8e-34bc-b2ef-2aa7357e45a2 | 0.24951 | -51.36139 | 2026-09-19 04:55:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67f5bd96-daf8-3dbb-b6d4-40198c35f346 | -3.23339 | -46.94616 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d187800-52d5-362e-80e1-afac3f26c60d | -0.85387 | -48.72357 | 2026-09-19 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ff6cea1-6d4c-35be-8979-f79d56ac534a | 1.26667 | -50.7472 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eeb2b3e6-6c7b-38be-9fff-35e2f9a69521 | -2.81773 | -50.46142 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b844098-abb5-30b7-b21d-46432493b580 | 1.22297 | -51.00752 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc83dc17-5831-3b71-bfd8-914d240c520f | -1.96616 | -54.69525 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14f2f878-694b-30d1-a8ac-431e202ce334 | -0.5235 | -49.14331 | 2026-09-19 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e636c92-c94b-3533-9824-aba092c96086 | 1.25398 | -50.7527 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a99b9cc0-b6a9-3115-bba8-0f6073c2bd7d | -2.82166 | -50.48045 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44b0d0f4-e0ee-392e-8784-c94a21ac49f2 | -2.02544 | -48.78164 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e22a409e-9644-3b22-ad60-ca8e5683ff0d | 1.21305 | -51.00907 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 21cf23a3-8939-3e6a-8839-f31896d80fe7 | -0.52168 | -49.15477 | 2026-09-19 04:55:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f77ec33-d2fb-374e-8448-ac9720814b09 | -3.24153 | -46.9474 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a448c344-5cba-3bf3-96c4-cf6dc1119e13 | -1.70292 | -54.89516 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d8a3277-0b9e-3c2f-aaba-c55ebbfa9552 | -1.2274 | -54.12591 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README69.md)
