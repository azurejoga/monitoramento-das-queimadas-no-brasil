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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 149ca7fa-0274-3728-a712-a5e2f20ca264 | -12.8452 | -47.9459 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 3cf5eaa8-8e5e-37a6-9ec4-ac0b8ec85c81 | -9.2656 | -59.4191 | 2025-09-13 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| aabc0916-716e-3123-82a4-656356aa1618 | -16.3422 | -51.5217 | 2025-09-13 12:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d83206e5-b5d6-382e-906f-47d07ee0ef30 | -13.8979 | -48.2804 | 2025-09-13 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 75659116-4349-3a7b-bcdf-4df1349da184 | -13.9172 | -48.2775 | 2025-09-13 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 66124e89-1596-3009-8700-db5b30df1b28 | -11.4119 | -50.4383 | 2025-09-13 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 176d8320-2a4e-33d2-9ee4-c3e36787c11f | -9.2658 | -59.3997 | 2025-09-13 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| d56057a5-ed8d-3243-94f5-3d9a48b8410e | -14.394 | -52.9245 | 2025-09-13 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 69a0640c-3550-3abe-83a4-1dd5129312bb | -11.8698 | -46.7627 | 2025-09-13 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 98667a65-cce5-3883-9e73-9cd283597337 | -12.9595 | -47.9963 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b601c184-2e48-32d8-9677-3d75082849e4 | -13.203 | -51.7406 | 2025-09-13 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 006f5fe9-db59-3337-93e4-cfcddad09776 | -16.4906 | -55.1276 | 2025-09-13 12:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| f683794d-f28c-3322-a25b-874bfe57f52f | -15.1169 | -52.4705 | 2025-09-13 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 35d55aaf-c539-3bf6-9612-b7bcf6870fdc | -12.9402 | -47.9991 | 2025-09-13 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 40d07e82-75d4-3144-8dee-abb4bcf0e8a0 | -11.9863 | -46.6564 | 2025-09-13 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 60a4b880-90d4-3db4-88ab-aeffd12ca1b7 | -17.4137 | -49.2744 | 2025-09-13 12:50:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 334d1609-d450-37a2-8c47-eb5b2cba106a | -13.2222 | -51.7382 | 2025-09-13 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 01c76d42-d0f6-3068-88b0-839a1cb10c39 | -14.4398 | -47.2979 | 2025-09-13 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 85b97f69-a324-39ab-8fa4-48a4845af4c4 | -8.5159 | -45.1349 | 2025-09-13 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 63784bd3-9cf8-3caf-90bd-1d200d56e045 | -16.5102 | -55.125 | 2025-09-13 12:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 476265c3-3415-3c3c-bbbe-18623c6034bf | -11.1066 | -51.9538 | 2025-09-13 12:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 94098384-6a13-3c32-8669-ba53e484450c | -12.5791 | -45.6821 | 2025-09-13 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| c87468c0-b799-36e0-b061-7def4edd66b7 | -9.5324 | -54.6277 | 2025-09-13 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 7468f82c-941d-39e6-a5ca-a890c737b48c | -12.5979 | -45.7021 | 2025-09-13 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 7e85e110-5c9b-397a-820f-c3dd7481c024 | -11.7826 | -47.402 | 2025-09-13 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 67bf0e8e-df3d-3619-8b4b-313376eb01c4 | -9.5137 | -54.6292 | 2025-09-13 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| e7573219-20d0-3a60-8c47-72ddbad9212b | -15.0858 | -48.0241 | 2025-09-13 12:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 874250ea-fac6-305f-ba00-5961a613b31a | -12.5787 | -45.7051 | 2025-09-13 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 853d91b9-9d3c-3e32-9a38-c7b3a0a36304 | -13.9185 | -48.2105 | 2025-09-13 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 3a84dcd7-d1a3-32a3-959a-9e0a367b710d | -10.3699 | -50.507 | 2025-09-13 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| befebd53-e01e-3fbe-930a-db12349876ed | -15.155 | -52.5078 | 2025-09-13 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 4ae21295-f422-38b4-93f4-97567a3e2617 | -16.0791 | -50.0151 | 2025-09-13 12:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 1cd4828c-ed2c-3ba6-9d19-fd33da079ecc | -11.1237 | -50.7049 | 2025-09-13 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ac23bb68-cefa-30cc-bf52-35defdbeda66 | -14.4394 | -47.3206 | 2025-09-13 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 768c9a34-3039-31df-bdb3-46c0b61b8f41 | -14.4204 | -47.3011 | 2025-09-13 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 130.5 |
| f4f7facc-f2d5-3542-8d05-c20bbbe315dc | -8.497 | -45.1369 | 2025-09-13 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 09423332-c7f1-36ac-a060-5fbb342039f3 | -7.2131 | -43.8396 | 2025-09-13 12:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 041c3656-3075-396f-9d9f-e6af51f0581c | -16.4903 | -55.1484 | 2025-09-13 12:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 7c7b45ac-0ac1-313a-9dcc-c0bcc00a5606 | -10.6579 | -46.2694 | 2025-09-13 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3c393a91-00b6-323b-aac4-6f1fd519b7bf | -13.203 | -51.7406 | 2025-09-13 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5fffaec5-3d30-34c9-a2bf-67d4617773d3 | -10.8976 | -45.5572 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 321.1 |
| 36ef8e48-6899-3daf-a54f-94cd8570b101 | -7.2131 | -43.8396 | 2025-09-13 13:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 5e243f4c-f748-3411-8855-ecefc03508a7 | -11.4832 | -43.7112 | 2025-09-13 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 88206f8e-44f7-3cbd-a20f-05ec1dd18009 | -12.5787 | -45.7051 | 2025-09-13 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 097ca77c-3a5a-3d6d-bafe-fb4ab194b04d | -13.9172 | -48.2775 | 2025-09-13 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4d6849bf-94b5-3708-ae1d-3ea68b72321f | -14.29 | -46.0924 | 2025-09-13 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 191.3 |
| f2970c1b-59c5-38f4-98d0-c2a2e3f27123 | -19.3417 | -45.1132 | 2025-09-13 13:00:00 | GOES-19 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 199d3940-6f8c-3286-928c-64258a1519ca | -15.0241 | -50.1367 | 2025-09-13 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 724851bd-e7ef-33b8-ad4e-f0f4fafa3565 | -11.1259 | -51.9309 | 2025-09-13 13:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 53acdd4e-2d8a-36a5-b184-06b12322c7df | -18.0065 | -46.9499 | 2025-09-13 13:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 673a31ca-5dc3-33ad-b361-bb06bf878ff5 | -10.8785 | -45.5597 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 368185a8-362d-3671-af40-112604e876a1 | -13.9379 | -48.2076 | 2025-09-13 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| a81a9fde-2369-39ab-a1b7-cf3af30259d9 | -14.2092 | -46.2439 | 2025-09-13 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 135.9 |
| ba287cda-e533-3d71-83dc-285ec0c5e9a7 | -12.104 | -47.6039 | 2025-09-13 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| e2d7a71f-3edc-329e-ae09-842b38e131c8 | -13.2222 | -51.7382 | 2025-09-13 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b9597803-076f-3a39-89df-6987e732cdc5 | -15.0432 | -50.1556 | 2025-09-13 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| d04d132c-5370-304f-9358-166f75330d09 | -17.4142 | -49.2519 | 2025-09-13 13:00:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 106.6 |
| ae125e04-10dc-307f-933f-54337ff66dd7 | -16.4903 | -55.1484 | 2025-09-13 13:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 6003dd59-6578-391c-8129-d09039305982 | -15.0436 | -50.1337 | 2025-09-13 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c3a4c64b-d5bc-356e-89f5-edefd958246c | -12.1232 | -47.6013 | 2025-09-13 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 528deca2-93b0-3bc7-95fb-1d7119887c28 | -13.8979 | -48.2804 | 2025-09-13 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| cb98b716-7f02-3714-8a34-984d06ccc92d | -12.9402 | -47.9991 | 2025-09-13 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 0d248f7a-5c5b-3dba-beaf-f8e722bdc663 | -16.0796 | -49.993 | 2025-09-13 13:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 46c9e407-d8d8-36d8-8ac1-6ea148cedaf3 | -9.5004 | -55.9788 | 2025-09-13 13:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 2fb361c6-6e4a-3518-81a5-0d69e189c258 | -10.8567 | -48.1827 | 2025-09-13 13:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ac3a047e-0911-362b-b73e-be33383e06a5 | -15.1169 | -52.4705 | 2025-09-13 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 98baaa4a-bee7-375a-b3fc-28f18a0b090b | -10.8781 | -45.5826 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| bc69f930-84ad-3bd8-a7f5-e7ca92d14f15 | -11.1152 | -51.3211 | 2025-09-13 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5d0093bd-053b-30b2-a5f2-5318b41eda59 | -11.8698 | -46.7627 | 2025-09-13 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c276fcc8-81c8-3e76-b1ad-9788db8edc25 | -10.8972 | -45.58 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| ab4fdf59-d6f6-3512-8031-5c35be1924b8 | -15.8648 | -47.2322 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b2da5975-7f19-3a54-aec8-94aec6ef220c | -16.5102 | -55.125 | 2025-09-13 13:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 96619d82-9659-3b00-92e3-5e71a109d0d4 | -14.1703 | -46.2505 | 2025-09-13 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| a162840a-6b68-39cd-9a4c-258c180cf3f9 | -10.6575 | -46.292 | 2025-09-13 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| dc09f1f5-fcbb-3a49-b02d-abf97aa0f12d | -13.2609 | -51.7122 | 2025-09-13 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.9 |
| cf6db7a6-d8fe-30f2-aae4-d7827d51ed0c | -14.3095 | -46.089 | 2025-09-13 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 345.8 |
| 342ab30f-d3df-3ea3-9ed2-90fa66473226 | -12.8263 | -47.9263 | 2025-09-13 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| e5ab9482-4f5b-3b11-b349-bca0e8b2f191 | -14.1694 | -46.2965 | 2025-09-13 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 034f5b6b-63d9-3f8e-9d56-792b669513cf | -13.9185 | -48.2105 | 2025-09-13 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 89c1220d-babd-37e7-83c1-60bda0d2bddd | -11.3835 | -47.3206 | 2025-09-13 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5f582290-9eb0-38cf-a6af-f3670cfd5b50 | -15.155 | -52.5078 | 2025-09-13 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 29598784-b1d1-3feb-a82e-46a9531c2cd8 | -8.5159 | -45.1349 | 2025-09-13 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| f7cab652-9883-3767-aa18-4bfbdb0242bb | -9.2656 | -59.4191 | 2025-09-13 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 939a39cf-f438-3bec-b9c1-9ca4764e1fd9 | -12.5979 | -45.7021 | 2025-09-13 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f9b132b6-d29b-3e6e-af4e-1e21606f3765 | -9.5006 | -55.9588 | 2025-09-13 13:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| e9be42d3-783d-34ee-bb33-516fe9b4ddff | -15.4708 | -47.3484 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 5dacc77d-54af-3b4b-a8a6-86e6a54e73a9 | -14.31 | -46.066 | 2025-09-13 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| da98239d-9a67-31fe-9ecc-b4b2d52f46b0 | -15.8845 | -47.2286 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 7fb269ff-04be-3428-80b4-0b131f1e4e87 | -11.7826 | -47.402 | 2025-09-13 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 163527f2-e5c1-3043-88d3-9f1b74a10d59 | -10.3699 | -50.507 | 2025-09-13 13:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ec94b1ef-c264-3d05-88bc-febc4f4e4c76 | -8.497 | -45.1369 | 2025-09-13 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 16cbf88d-9cca-34f2-b20e-60eab5832d9d | -15.4713 | -47.3256 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 196.2 |
| f5dfa2a5-e2cb-3862-916f-2d1f2faed16c | -15.1554 | -52.4865 | 2025-09-13 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 3ebb4526-dcfc-3e9a-b98c-00aa085daa93 | -12.8452 | -47.9459 | 2025-09-13 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0cfe8a55-4069-3357-a4fc-ec42ce2c71d3 | -15.4517 | -47.3291 | 2025-09-13 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ed7e6b0c-2d9f-3cc5-9fb9-81ffd50734c7 | -13.2801 | -51.7099 | 2025-09-13 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 52e183a0-8f4c-39c0-a10b-be33c3b72c7e | -16.0997 | -49.9677 | 2025-09-13 13:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| feae50e3-b29f-383b-bcd7-2e4a71289cc6 | -12.1236 | -47.579 | 2025-09-13 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 2b9f1a76-5f83-3a1a-9e79-b74a3e4a83d4 | -9.2658 | -59.3997 | 2025-09-13 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 3d2fd94d-e8e6-346d-a7d0-8cab46be2016 | -12.9398 | -48.0213 | 2025-09-13 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.7 |


[Clique aqui para ver as próximas entradas](README126.md)
