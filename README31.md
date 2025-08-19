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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f868edfc-45bf-3289-a786-91ea3221c8e7 | -19.71471 | -47.93406 | 2025-08-19 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f7ca222-5b46-329c-8c9c-369319826c7c | -15.79683 | -48.22163 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 901e5f90-c8c5-3d24-a85a-5c6f42ad3a95 | -16.62572 | -51.36053 | 2025-08-19 04:29:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 174510ed-bbce-3af1-9504-afbd8fc551bf | -15.80921 | -48.27461 | 2025-08-19 04:29:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c103fbae-ec42-3a5c-89d3-f3f873aa8877 | -17.41251 | -46.71055 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5801718-b087-3756-8918-7a8f2a156afc | -18.87536 | -48.02879 | 2025-08-19 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 151162d4-1e07-34cd-95f8-6abfe23ee4e8 | -16.47656 | -45.09705 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e03c0805-0f0a-35c3-ac9a-518cb2108a93 | -19.95342 | -47.90495 | 2025-08-19 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f39430f1-3c39-3648-80f8-96d0ccf2a824 | -15.0384 | -54.81581 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 484b5e45-8ad9-3bae-a0f8-463537ede16f | -19.64804 | -44.65581 | 2025-08-19 04:29:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f64aec4b-afea-36b0-aff0-a7b4964a858b | -16.79353 | -50.09172 | 2025-08-19 04:29:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a5200bc-795b-32a2-a096-c34e94161c99 | -17.40558 | -46.70948 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12e0b007-21c8-3a16-a2f9-2d2fcf1bf7f0 | -17.40847 | -46.71397 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f01bde7e-a2ee-398b-aaf8-c5b380f29501 | -16.48034 | -45.07703 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 983db653-0295-37bb-8785-211f1a2f7911 | -21.23615 | -49.08326 | 2025-08-19 04:29:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1e6a083e-5af4-3950-8c56-f63b7223df0c | -17.5736 | -44.47913 | 2025-08-19 04:29:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71d7ca89-bc4d-3239-aff9-ef51190d1652 | -17.41193 | -46.71449 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15836545-8cd4-3fcc-b3dc-a9f7937981dd | -20.33184 | -51.70533 | 2025-08-19 04:29:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7689b17d-8240-3887-ad68-0ee210279e13 | -19.31881 | -44.87677 | 2025-08-19 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86703b91-8439-32f5-8090-154d1b2edcd5 | -19.0011 | -50.54243 | 2025-08-19 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fff0f732-2478-3c86-813f-d91834cc60fa | -15.08051 | -55.4198 | 2025-08-19 04:29:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25e9da91-634c-30df-a6eb-b887d2e34fd2 | -16.47901 | -45.07892 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2158c8a6-8dcb-3eb4-a9fa-2ac4ada5a472 | -21.40309 | -45.00788 | 2025-08-19 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 3cb433bb-7056-35ba-bfa9-186a89c97da6 | -17.33428 | -47.17202 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 233042eb-b7cb-33d9-a611-4c92abbe25d1 | -19.31731 | -46.05925 | 2025-08-19 04:29:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b17c746f-92cb-322f-a27f-7e3e89ce52ba | -21.39914 | -45.00737 | 2025-08-19 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 30168e07-4e1e-3e42-811d-e549c662f432 | -14.97605 | -54.8065 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f90c29d8-bb28-3272-888e-0fe4c471a268 | -16.47906 | -45.08608 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef7d5f66-22f2-3f89-8353-f1a119b87fe2 | -15.35983 | -47.25803 | 2025-08-19 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9db2ac4-a1fa-3754-b799-a332b274ce35 | -15.01735 | -54.80846 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 767814fb-422a-399b-97ef-9229d898cc25 | -16.30835 | -49.16885 | 2025-08-19 04:29:00 | NOAA-21 | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2259dd36-47a2-3e1e-9e10-aa4a132243e9 | -15.75022 | -46.61281 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24b6e4ad-78b4-3b05-81a4-d1c5eff7982a | -21.13331 | -47.0395 | 2025-08-19 04:29:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f50501ef-da15-3789-9809-de31246594a7 | -16.84181 | -48.91257 | 2025-08-19 04:29:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0e48591-8f95-31e4-97d0-1cec3d9df340 | -15.35592 | -47.26117 | 2025-08-19 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45dfb74b-abd9-3964-9c52-92ba79d5aecc | -14.98635 | -54.79923 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b6151ae-1616-32cb-882f-3731bbeab134 | -19.93948 | -45.06366 | 2025-08-19 04:29:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d7ed5bd-5a71-3f9a-85f8-50b3d3256826 | -16.50546 | -45.10603 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0eacf69-b0b3-3d21-9928-24550db63bad | -15.79929 | -48.22896 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27c9a810-d205-3481-bb45-e761391411ca | -14.64608 | -54.92341 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c55b017c-58c5-307c-b331-e60d3ca3d41b | -17.42001 | -46.70765 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb2a22bf-c905-3bd6-9d9b-cac7d39995df | -14.98986 | -54.80454 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| da90152d-f9c5-3e51-8780-42048abf5f92 | -14.98905 | -54.80898 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0f1c9f32-620d-3f55-bc8e-8d2ee6d387de | -15.35648 | -47.25744 | 2025-08-19 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34068c26-f619-3237-bbf3-e3a85ab815c2 | -16.81401 | -49.36909 | 2025-08-19 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24027dff-f02a-3eae-8c9f-99da6b219f6a | -19.64088 | -46.84538 | 2025-08-19 04:29:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b366629d-1689-3e2a-bf7a-1164d1b47d57 | -16.50976 | -45.10207 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6540e4ae-62f8-36c6-985e-7041e33686e5 | -14.97252 | -54.8013 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 133e4096-37f7-31e1-9578-2bb0274b9684 | -15.02526 | -54.81411 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56824eb8-bba3-3c47-8276-8a9dd242f0b4 | -16.48332 | -45.10268 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5063e941-183d-3510-a207-b1992cd33a08 | -17.34505 | -47.16985 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10c08d43-9362-3916-a2de-fdafb443fd73 | -14.62777 | -54.9241 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bafd5ae1-9f93-3247-a621-872cf933f2c6 | -20.50027 | -46.37918 | 2025-08-19 04:29:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7969efe-605a-3cbf-946d-b0424857e870 | -20.33119 | -51.70925 | 2025-08-19 04:29:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa6b2fb6-b96e-348b-ac1b-916ba308de7a | -16.48394 | -45.09815 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77090ad4-134a-32a4-a40e-945f350a2894 | -19.20012 | -46.8474 | 2025-08-19 04:29:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03e3d4e4-7546-33b3-bfd0-b5127e3daa1f | -15.75078 | -46.60895 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2223330f-f688-39b8-9352-55d517c3af23 | -16.67943 | -49.18766 | 2025-08-19 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ab070bf-782d-3769-bb1a-1174b06c2f2e | -16.84125 | -48.91616 | 2025-08-19 04:29:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e0c999a-7886-370c-a771-709831e4bc7c | -16.79688 | -50.09228 | 2025-08-19 04:29:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0804324-8afd-382b-8a42-97f666076a48 | -14.98662 | -49.56071 | 2025-08-19 04:29:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f541891-0a44-393f-81be-3e2ab9badec5 | -14.98313 | -54.81685 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a52214fc-2ae2-3c2d-9f53-e8c848bda19b | -20.4764 | -53.67554 | 2025-08-19 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06597ceb-21f1-35d9-a84a-ea60c6f92157 | -15.02701 | -54.80481 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 212d960c-51d3-3544-a588-2ebd13255c8b | -20.29823 | -50.95548 | 2025-08-19 04:29:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d678650-913d-3c10-8a0d-6ccb15aad1eb | -14.29957 | -53.35786 | 2025-08-19 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ec91da0-e1ab-38a2-adf4-ed10af2395b4 | -20.33461 | -51.70988 | 2025-08-19 04:29:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c95f3f97-7999-32c7-a8d2-455e7d4c2c41 | -19.29403 | -48.43282 | 2025-08-19 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ece1b90-2d66-3b03-a7cd-718e3faac0a2 | -16.71356 | -47.6235 | 2025-08-19 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12700f2f-3bd9-32f8-8aa6-dc9ecc69e567 | -15.15595 | -48.77686 | 2025-08-19 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a411847e-67f7-3687-b602-7ce351f335ff | -14.96899 | -54.79611 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b04bad50-afb6-33c6-97af-fb7b25ceefc8 | -16.70911 | -47.63027 | 2025-08-19 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cfa01d0b-ec23-3bfb-ac13-02dbd79a1b95 | -17.34564 | -47.16589 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56293a7d-298a-39aa-94ed-eb5a9ad62543 | -14.64331 | -54.91369 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6359781-e868-3aab-a55f-3afb4c5999d1 | -17.39176 | -46.7072 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2728be4f-f9a7-3af3-821c-349aabdf4fec | -16.19851 | -42.8796 | 2025-08-19 04:29:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f98ca542-991c-3b41-b2aa-d354431bcbc2 | -19.20419 | -46.84391 | 2025-08-19 04:29:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d37b41a7-1851-3f4a-8778-66b174eea62c | -17.91757 | -44.44641 | 2025-08-19 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3985fd6b-e140-34ba-8668-fa50c7fc93e7 | -16.49132 | -45.09927 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| befc4950-0ba0-3e4a-8243-eba6181b1d11 | -15.03757 | -54.82026 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b0810bd-b41d-3990-b20f-86baf9363735 | -15.8026 | -48.27353 | 2025-08-19 04:29:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32679fe9-3612-324c-a8f8-81df0e961595 | -15.03404 | -54.81519 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e902af01-379d-396a-92b8-fb268ecc39cd | -16.47717 | -45.09251 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90d2c27c-6890-3e2a-8091-4f75a8c0993a | -21.51533 | -45.44915 | 2025-08-19 04:29:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dec76613-8877-3cc7-809d-7c5476298c96 | -15.75135 | -46.60507 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2a771a9-bce9-336a-a487-6b60d54cddca | -14.30832 | -53.37801 | 2025-08-19 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d75f9ecc-7bd4-37e3-9f0c-49ad994133ac | -17.89183 | -48.60765 | 2025-08-19 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 648ff561-6965-31f2-8acd-d4fbe3c64412 | -16.4784 | -45.08345 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b17da43e-f66c-3ec7-b38e-ad64447f1c04 | -16.4907 | -45.10379 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9abc800-8c78-3b5b-aaca-bdb41278b8df | -15.79242 | -48.22822 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16ff345c-6a0e-3d2f-a525-e88b2d20210f | -15.74967 | -46.6166 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53ee6524-a0ed-3209-80eb-e5224d41fe89 | -19.64147 | -46.84127 | 2025-08-19 04:29:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dd1e8aa-f3f6-39d7-85a2-66ffdfb84783 | -21.32155 | -48.67299 | 2025-08-19 04:29:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bbd16d83-ce4a-36a1-b05f-fa84bb06b870 | -19.93785 | -45.06207 | 2025-08-19 04:29:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28752b67-d68b-3ca8-93ab-04dddb89552e | -17.49161 | -45.85285 | 2025-08-19 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be955f5e-c391-312f-bd37-0438e2213489 | -14.4517 | -53.02938 | 2025-08-19 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 402fd371-7571-34bb-aead-29ff92bb926b | -16.38409 | -48.8396 | 2025-08-19 04:29:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e365307-46ca-38c5-a321-9dcd55f5d0e3 | -16.61737 | -51.36734 | 2025-08-19 04:29:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 008bc58c-20b3-3418-ba4f-d7ab3119aef6 | -16.31166 | -49.1694 | 2025-08-19 04:29:00 | NOAA-21 | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c373b076-ead2-3891-a4c7-3fe11d972f45 | -17.98814 | -46.35264 | 2025-08-19 04:29:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
