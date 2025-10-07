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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f526393-e932-38c7-bf60-1264de7ec65b | -13.28479 | -47.80644 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e212ede8-2bc6-34b5-8e11-924409d97446 | -13.34326 | -48.0289 | 2025-10-07 05:55:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c3314d6f-6f56-3e0f-a75c-d5d6e163e484 | -13.25911 | -47.79318 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 469aa0f6-a900-3d58-be6d-b9d36e864314 | -14.28527 | -45.84718 | 2025-10-07 05:55:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b1f651ee-0e47-383a-b99f-64fdf2d2ea1d | -14.73221 | -46.01154 | 2025-10-07 05:55:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 068c7929-4d23-3585-9a4f-cdcb04f46232 | -20.05768 | -49.5516 | 2025-10-07 05:55:00 | AQUA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| fc899f2f-e600-35ff-a9a5-fef8ae5e357c | -15.35925 | -47.30778 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77d2485d-8162-377a-9c07-11e9c077638a | -14.90466 | -51.43817 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 395a98ac-b678-394c-b6fa-2aead559256c | -21.77111 | -47.78236 | 2025-10-07 05:55:00 | AQUA_M-M | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7c9b0661-3ecc-3bc3-b5bd-8428c802afcc | -13.70462 | -48.08314 | 2025-10-07 05:55:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5037da87-55b4-3ccc-a73b-952c3018911a | -13.02072 | -51.03144 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2170f045-957e-3ac9-9048-c5d95863b68a | -14.92667 | -46.80258 | 2025-10-07 05:55:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 53c7de10-c756-3103-8d8b-336d23e644e6 | -15.50444 | -47.91973 | 2025-10-07 05:55:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f3659944-a9a4-375d-bfc2-e60440f71561 | -14.91812 | -51.42555 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a730b549-4df7-3d6e-a21b-f532e983e55e | -15.49857 | -46.82427 | 2025-10-07 05:55:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a03ae0b-891f-347b-91e2-9e13e9b386df | -20.07901 | -49.59193 | 2025-10-07 05:55:00 | AQUA_M-M | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| 4e3a060e-81ca-3280-be69-e58ee89945f5 | -13.09796 | -47.99676 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 669bc985-395d-3ea6-84ae-b2f0be068808 | -21.90761 | -44.87536 | 2025-10-07 05:55:00 | AQUA_M-M | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 98c760ac-93a9-3050-997f-ae30591183fa | -22.02067 | -49.71386 | 2025-10-07 05:55:00 | AQUA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 19cc2cfa-01d5-33de-ae13-34231cf4ef06 | -14.94495 | -46.82032 | 2025-10-07 05:55:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fbc52c17-c340-3fa8-b2da-1c71fb32386a | -18.96807 | -47.82224 | 2025-10-07 05:55:00 | AQUA_M-M | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| b1622a71-9a85-310f-a6f0-b01b552e9a1c | -16.28825 | -50.98098 | 2025-10-07 05:55:00 | AQUA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cfd54da7-bab5-33ed-8f0f-f5e41fabb297 | -15.38952 | -48.0098 | 2025-10-07 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4654a593-471c-3fa8-ae43-288725d51363 | -15.26995 | -48.06214 | 2025-10-07 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a7746a47-9600-325b-91b9-6cc52f12ed25 | -22.94667 | -49.29525 | 2025-10-07 05:55:00 | AQUA_M-M | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ef600fca-2031-37f8-b6f1-d42aee2f49da | -14.73971 | -46.02197 | 2025-10-07 05:55:00 | AQUA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| dcd71858-01ef-3e77-8bcb-8be33edc1d87 | -13.70615 | -48.07333 | 2025-10-07 05:55:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 82a46a2a-28a6-3b43-b66c-7decc499f097 | -13.28353 | -47.16148 | 2025-10-07 05:55:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 22ec6417-5596-305c-9d0a-9f8cf1521100 | -12.89452 | -54.72656 | 2025-10-07 05:55:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 5ae20426-b2df-3849-ac48-40ba9a6320a9 | -17.98433 | -44.98177 | 2025-10-07 05:55:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e5662cff-2675-3e47-a84a-2a563afd2f23 | -14.70081 | -48.38956 | 2025-10-07 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 604fcdab-d3a6-34d0-9783-a4df43fc45fc | -22.0027 | -49.7106 | 2025-10-07 05:55:00 | AQUA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 291e477c-48fa-30d2-96a6-66e96c32cc67 | -22.11564 | -45.00028 | 2025-10-07 05:55:00 | AQUA_M-M | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 277cb291-1c8d-3a74-94f2-137b9ecb7e08 | -13.33857 | -47.76262 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7897da38-f7b2-3f02-9e19-8690e05f16fe | -13.22904 | -47.80779 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7a69cd79-c8a8-3482-bec7-8e9d19415787 | -14.9291 | -51.42754 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 9e2569af-addd-37cc-a1ba-fd5612a6c600 | -20.05175 | -49.53017 | 2025-10-07 05:55:00 | AQUA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.2 |
| 692979a6-751c-37d0-b98f-d7c6d8cec5fb | -13.22872 | -48.45508 | 2025-10-07 05:55:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 784f512d-7da1-34c7-9448-44c3146f5cec | -14.92804 | -46.79356 | 2025-10-07 05:55:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 8afc3438-86d5-3025-8db4-821d50ca47d6 | -16.11228 | -48.93731 | 2025-10-07 05:55:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 478f5313-ff75-3163-b1d1-f51b20656e05 | -14.76623 | -46.02606 | 2025-10-07 05:55:00 | AQUA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 512ad6a9-6d8f-3e78-a67a-c6c4b150e7cf | -13.59047 | -48.68629 | 2025-10-07 05:55:00 | AQUA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8a969da4-35d8-390a-b603-9e5a0bc05c21 | -15.59966 | -52.55872 | 2025-10-07 05:55:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c12c576c-33c0-3648-b18e-2b352bd1fc1b | -22.00854 | -49.73196 | 2025-10-07 05:55:00 | AQUA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| a9702b39-7e65-3b23-b1fa-bcaf39ebac15 | -13.21848 | -47.81602 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5db8ff47-b733-3ad9-84e4-939031b15845 | -21.39491 | -45.05173 | 2025-10-07 05:55:00 | AQUA_M-M | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 9387a451-f3ca-3b1a-a442-a1df3faab4dd | -13.28625 | -47.79707 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a0c13e82-f1d2-30ff-a0fc-4ee396611201 | -20.11219 | -44.40611 | 2025-10-07 05:55:00 | AQUA_M-M | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 140b00b5-0454-3058-8c5e-d404f00cd35c | -15.39098 | -48.00039 | 2025-10-07 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb7d99b4-ae20-37df-9d44-0ed2e7ff8b19 | -13.08698 | -48.00926 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e6c80110-164c-3073-ae77-424b6f20e5c6 | -15.29496 | -46.32835 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7771888f-8e18-3ca8-b0cc-ac90cbc12133 | -14.90714 | -51.42356 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c4c0fae8-867d-3688-99e6-43c679173231 | -15.61152 | -52.56066 | 2025-10-07 05:55:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| fbec425e-f418-3f75-9cbb-4239105276f2 | -15.36666 | -47.31837 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 05b986a3-8d7c-3f34-8949-316f27b389f5 | -14.90362 | -46.83603 | 2025-10-07 05:55:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b873d68-6c53-3712-b822-c26b747e79cd | -13.09639 | -48.00659 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 55fefa9d-3644-3b73-b38a-4a04f196c8f8 | -17.25477 | -46.93084 | 2025-10-07 05:55:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0a992d7-514d-3789-a5e3-ad64ee759e09 | -22.02966 | -49.71545 | 2025-10-07 05:55:00 | AQUA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 34b26ef5-92b3-30fb-8826-4820dbc7e3a8 | -15.36062 | -47.2988 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 19f2c21a-f511-34fe-a903-dac4f6b0f3bf | -20.05926 | -49.54168 | 2025-10-07 05:55:00 | AQUA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.4 |
| 8f02a2a3-421d-3bc4-b321-4f5917337c0c | -18.97687 | -47.82369 | 2025-10-07 05:55:00 | AQUA_M-M | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6942c72b-d66f-3c70-b164-dd70d00ba1ed | -13.21997 | -47.8066 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| b9bfca28-47e5-394c-b089-608988378a1b | -15.07371 | -46.63442 | 2025-10-07 05:55:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cd305d43-ceba-3bba-a28f-923e72fd8b45 | -13.22759 | -47.81704 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2fb9667f-cde7-3723-90c7-19c52fd73fb0 | -13.36945 | -47.56543 | 2025-10-07 05:55:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea483da1-0849-312a-bb48-eac4f03cb84b | -14.73702 | -46.04019 | 2025-10-07 05:55:00 | AQUA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a571a37f-e4a5-3d8b-bbdf-f88e9e081173 | -20.0881 | -49.59357 | 2025-10-07 05:55:00 | AQUA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 26c2c259-b091-39f2-8a1c-d8424fd05222 | -14.93343 | -51.41928 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 28d08efd-0b4b-3042-9302-7a2eabc5f850 | -13.27466 | -47.16011 | 2025-10-07 05:55:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e21f508b-f75a-3f44-a6b6-8ff9fb907b20 | -13.09957 | -47.98666 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 793e450f-2b37-3dcc-8fb4-67087b3948c5 | -16.29032 | -50.96862 | 2025-10-07 05:55:00 | AQUA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bb5e4d0e-d533-3d08-bd59-3a8535c42bad | -13.25552 | -47.16648 | 2025-10-07 05:55:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1837a27-df78-3d1e-8cd9-db01ef77bffd | -17.0932 | -43.37912 | 2025-10-07 05:55:00 | AQUA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c544d12e-3b87-3a07-b02f-42a05941bc13 | -14.91565 | -51.44016 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 39298ec7-1d1b-30da-831c-350a1016dd69 | -15.27271 | -46.34623 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6f29371a-1dfb-39ab-89d1-8c7142f1c6d5 | -20.05017 | -49.54008 | 2025-10-07 05:55:00 | AQUA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 122.3 |
| ed0e5ab7-1cd9-3883-8e03-f3e67de3cbd8 | -15.02645 | -47.55428 | 2025-10-07 05:55:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79c680b8-0180-3815-bdb8-17e5846a9d4b | -14.6504 | -48.35587 | 2025-10-07 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d2fac702-e225-3d46-a81f-e596930cbd73 | -16.10306 | -48.93587 | 2025-10-07 05:55:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 981083be-fd4d-33d9-be6f-ada52b500b8d | -20.06083 | -49.53174 | 2025-10-07 05:55:00 | AQUA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.0 |
| 829700d7-36f1-312b-a8c0-904f2511653d | -21.18582 | -45.60912 | 2025-10-07 05:55:00 | AQUA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f318d97e-57c2-326f-b62e-fe75e88f2bd7 | -20.08971 | -49.58355 | 2025-10-07 05:55:00 | AQUA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 1868b124-98fe-36a1-9b52-f8ede4cbd316 | -17.3448 | -46.82871 | 2025-10-07 05:55:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2abe3e8f-e311-38b1-99e0-63705ddac177 | -22.00112 | -49.72049 | 2025-10-07 05:55:00 | AQUA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| df2c2950-f0d0-3848-b332-9f52ca9be56b | -18.77825 | -44.62027 | 2025-10-07 05:55:00 | AQUA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c195ddd3-c50e-300b-bc5f-ec4b394fa25f | -14.92305 | -51.39644 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 94d9c1dc-b06b-3752-a223-8424d56a5596 | -13.36049 | -47.56407 | 2025-10-07 05:55:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2ac2736c-18bf-3924-9ab0-caa47686c6fd | -13.02318 | -51.01682 | 2025-10-07 05:55:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ddf895ec-8333-389c-99ee-f96165d38f1c | -23.10276 | -46.18088 | 2025-10-07 05:55:00 | AQUA_M-M | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 251c8b3e-627c-3faa-a09f-2a7349398be2 | -18.97546 | -47.83294 | 2025-10-07 05:55:00 | AQUA_M-M | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9bea7a43-280d-39a3-88bf-d5f55f7e021a | -16.04391 | -50.95173 | 2025-10-07 05:55:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 586d227c-b17a-3d0e-b032-dbcba7205e43 | -16.10144 | -48.94593 | 2025-10-07 05:55:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c0a6efe0-59c9-3a43-9785-837cb365be4d | -15.11933 | -43.8647 | 2025-10-07 05:55:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a5b7f924-4f4f-3551-86bc-ca95cbfe89c5 | -13.08851 | -47.99939 | 2025-10-07 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 610a27c8-901c-3b75-b0f2-5aa4401ac830 | -6.74608 | -63.06148 | 2025-10-07 06:16:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fe192d8-a2aa-382a-bc64-cb1585b71134 | -6.74029 | -63.0607 | 2025-10-07 06:16:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91b608ff-bfda-363b-bc59-94f74a591b84 | -6.69871 | -62.84085 | 2025-10-07 06:16:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4136ed9-7365-34c4-b7c7-4a39e9865d62 | -8.90239 | -71.36833 | 2025-10-07 06:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e07742e2-e07b-3902-b3dc-1da163a66097 | -8.22515 | -61.18178 | 2025-10-07 06:18:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70a1f0de-6873-34ab-8497-575a76f1de57 | -9.19952 | -62.5988 | 2025-10-07 06:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README109.md)
