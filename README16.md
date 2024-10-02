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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec608648-e08c-34b7-9121-31f2ea577546 | -16.7455 | -57.4674 | 2024-10-02 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| 9ae9c48d-f8b0-3d51-bd64-5d91f308f4ac | -16.7461 | -57.4265 | 2024-10-02 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 54cfbbb6-f944-3900-8ef8-22845990ebdf | -16.7647 | -57.4856 | 2024-10-02 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.6 |
| 0fad3953-e2dd-3486-a08d-fa04d82aff46 | -16.7663 | -57.3833 | 2024-10-02 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 39446d5e-2c7b-3b19-95f8-2743e3628296 | -16.7666 | -57.3628 | 2024-10-02 00:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 3f452286-7ef5-3e54-bfe7-e921875e0aba | -16.8184 | -57.8058 | 2024-10-02 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| 65c90c1f-94a2-3095-9252-395f44c8b163 | -16.8234 | -57.4789 | 2024-10-02 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| f4aa0460-ac39-32b1-934c-a18f55e4eccc | -16.8238 | -57.4584 | 2024-10-02 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 9b6b9302-93a0-379a-b197-abd5e8f6697e | -16.8386 | -57.7628 | 2024-10-02 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| c86f37b2-359e-33c9-8505-c7d7a99ff037 | -16.8695 | -55.848 | 2024-10-02 00:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| ef73a1fe-e324-338c-b59d-e4ff6b375601 | -17.0502 | -56.7551 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 64fd51d8-847b-3057-92a0-1a76bcde1dd7 | -17.0612 | -56.0931 | 2024-10-02 00:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| c96042bd-cebc-36b3-91f0-7b9246fc60aa | -17.0695 | -56.7733 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| d71bffd2-34fb-365c-b0f1-185fc79d30b4 | -17.0699 | -56.7527 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| c22b08b4-4d8d-3d1b-a884-7d732dd7c862 | -17.0705 | -56.7114 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| dcc238b8-005f-363c-b5b7-bcb652f254dc | -17.0892 | -56.7709 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 22974f7b-e178-3214-8a12-43cd5effcc82 | -17.0895 | -56.7503 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| e038be9f-8a7e-32b3-a32f-7f14bb044a55 | -17.0902 | -56.709 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 17c803f0-9680-36c2-8a06-612adbec43ea | -17.0905 | -56.6884 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 32912ffc-54dc-317f-8fb6-6159f8630beb | -17.1091 | -56.7479 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 081ceef2-d7f0-3cc0-8877-bb9f51ffad98 | -17.1101 | -56.686 | 2024-10-02 00:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| db642b4b-4a64-3955-89e7-a3b2c99ed37e | -17.1577 | -56.1844 | 2024-10-02 00:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 9aeb4b6f-a23f-3376-aa66-bd76ba300613 | -17.1581 | -56.1637 | 2024-10-02 00:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 37791abc-46d7-3526-acfe-347ab39db5e1 | -17.1971 | -56.1795 | 2024-10-02 00:46:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| e3fb391b-d205-3f25-a036-14861ae7422d | -17.196 | -56.2417 | 2024-10-02 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 0247c52b-d01b-30f7-85c0-0df38af3f26c | -17.1964 | -56.2209 | 2024-10-02 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 04dbd363-ad10-3263-865e-a86242093424 | -17.1967 | -56.2002 | 2024-10-02 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 1c66fd9d-21b6-3984-8770-14cf412f0592 | -17.216 | -56.2185 | 2024-10-02 00:46:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 0b8491f0-9650-3638-97da-a5f121ce3f08 | -19.2317 | -46.8687 | 2024-10-02 00:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 9f2bf82a-2d9b-354a-ae24-f0101ea0d50e | -19.2323 | -46.8452 | 2024-10-02 00:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e8ed63ed-3814-3205-86dc-48e470afa0a2 | -19.2519 | -46.8641 | 2024-10-02 00:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 165.0 |
| eaf974dd-310c-311b-97ce-82917500de0a | -19.2526 | -46.8406 | 2024-10-02 00:46:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 44cdd488-6b97-3729-9ef9-771b154228c2 | -21.2854 | -47.6277 | 2024-10-02 00:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6e9d0a06-8b7a-3fbf-b476-7c6ba7986b0c | -21.2861 | -47.604 | 2024-10-02 00:47:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 0a7fda73-4575-3f9a-8ad9-7cfe428747f1 | -21.6275 | -50.796 | 2024-10-02 00:47:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| 81b1abcb-ce22-3d99-a93a-790c5f4bf47f | -22.9277 | -43.7243 | 2024-10-02 00:47:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 100.7 |
| 54a9391f-c9c8-3bb1-857f-1b679cb563f8 | -22.9006 | -45.1029 | 2024-10-02 00:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 8d0809cc-3707-3f95-9bec-f84259292407 | -22.9014 | -45.0779 | 2024-10-02 00:47:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.2 |
| bb1b8d1f-2db3-3179-97b9-443a04b46c7a | -2.6496 | -54.6172 | 2024-10-02 00:55:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 323180ab-32a7-385f-a842-a56879324ff4 | -3.2136 | -46.7843 | 2024-10-02 00:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 42b165d4-b136-329a-8310-f6df9edd7a41 | -4.4657 | -42.8877 | 2024-10-02 00:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 39f1c0e6-8745-32fc-a820-7442d903d072 | -5.9786 | -45.3847 | 2024-10-02 00:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| df896451-401d-3bf2-8555-b61c7f266807 | -5.9788 | -45.3621 | 2024-10-02 00:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e81c1a61-ff2c-3ffc-836c-3c5110f5dc93 | -7.1796 | -46.9444 | 2024-10-02 00:55:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a9c56087-9e2d-31e0-b4d5-8900efc5b10f | -8.205 | -44.365 | 2024-10-02 00:55:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 3c39a541-7331-3bac-a14e-6881fa34986f | -8.2053 | -44.3419 | 2024-10-02 00:55:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| ecba2d8d-094c-309e-bc77-cbdb7d1ee631 | -8.2239 | -44.363 | 2024-10-02 00:55:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 25c0bf76-a7f6-33db-936e-c654df5ef300 | -8.4643 | -62.7124 | 2024-10-02 00:55:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9932852f-7217-3bca-827f-4f8b918c3e67 | -9.5398 | -62.8005 | 2024-10-02 00:56:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 2f26d3bb-b8cf-3114-ac2e-d33aed1b5a7d | -9.9367 | -64.9179 | 2024-10-02 00:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 205.8 |
| cb773c40-8103-3b6f-8723-7be55af215d3 | -9.9368 | -64.8991 | 2024-10-02 00:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 196.9 |
| fdb285fb-3193-348b-8b5f-828912f14e12 | -9.9553 | -64.9172 | 2024-10-02 00:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 5521b8cf-bffa-30c6-8554-e17a61bc2c5e | -9.9554 | -64.8984 | 2024-10-02 00:56:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 156.6 |
| ea7f8838-6cab-3397-9567-ddcd7339d618 | -10.3699 | -64.0904 | 2024-10-02 00:56:05 | GOES-16 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 96a8ab0d-0ed3-3934-9f80-f2b76ad6538f | -10.626 | -55.8752 | 2024-10-02 00:56:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 62be5297-8567-3efd-a328-9fe683d0cbea | -11.4822 | -56.7892 | 2024-10-02 00:56:11 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| fcbb41d3-284a-3a71-865e-8b51862d1a36 | -11.884 | -43.8142 | 2024-10-02 00:56:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 27c98131-1c47-3247-86bb-6cafabb85464 | -11.6554 | -65.018 | 2024-10-02 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5030fee1-94d6-3a30-9a7b-8142ced36c4f | -11.6555 | -64.9991 | 2024-10-02 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 813fcd0a-92b4-374a-9d31-20343d273ff4 | -11.6556 | -64.9802 | 2024-10-02 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b6bf549e-7b9f-3da3-a18e-d960ba110bf9 | -11.6743 | -64.9983 | 2024-10-02 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 3334789b-0c9c-3059-a66c-4f05a566d6cb | -11.6744 | -64.9793 | 2024-10-02 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 711f06b4-8071-3463-8cf8-c861a69f9d82 | -12.1597 | -50.0501 | 2024-10-02 00:56:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| fff6d1bb-6e3d-3641-ae39-3b8c08fc1419 | -12.4433 | -43.7242 | 2024-10-02 00:56:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 28cbc5e3-5f96-3c21-bbce-4fb598b5d3b0 | -12.2754 | -47.6473 | 2024-10-02 00:56:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 83a302b6-e584-3d25-9a3a-4a63c23810ce | -12.2946 | -47.6446 | 2024-10-02 00:56:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| b2576093-4dcc-3833-8c44-85f4e2559ef1 | -12.6484 | -63.1214 | 2024-10-02 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 7d7413ef-a223-36ae-9ef0-1b5180b22e21 | -12.6486 | -63.1022 | 2024-10-02 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d8a5bfc0-5541-359c-9b48-3b639d742955 | -12.7054 | -63.0798 | 2024-10-02 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a58d54de-1e59-3393-88d4-57153ddb8d1c | -12.8593 | -62.7826 | 2024-10-02 00:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 871ca1f8-fe6e-3886-b339-586c4e2bcded | -12.8782 | -62.7815 | 2024-10-02 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a8e9d5a0-7e3f-3201-a2ce-04c657b8f523 | -12.8784 | -62.7622 | 2024-10-02 00:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 117cfebd-83dc-3a96-9d3d-b8fbbcb1570e | -12.9167 | -62.7022 | 2024-10-02 00:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| db83249f-eed9-3d3b-8a57-74f2f236fbd4 | -13.055 | -51.4186 | 2024-10-02 00:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 5bf5dc04-9392-3425-9bc8-7865945709cf | -13.0553 | -51.3973 | 2024-10-02 00:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a8228b67-651c-35c6-847f-8e7ec17da1c0 | -12.9357 | -62.701 | 2024-10-02 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 172.7 |
| 68b8568b-5804-3a2f-a903-ca112397d5ca | -12.9358 | -62.6818 | 2024-10-02 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 7d7ee22c-fb9d-38f7-a3b4-095134da090f | -13.0742 | -51.4163 | 2024-10-02 00:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 9c86ef2f-a2b8-3dbd-b05c-f214eff7750d | -13.0745 | -51.3949 | 2024-10-02 00:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ccf79e43-f670-3c65-8ce9-8bb149cd434f | -12.9546 | -62.6999 | 2024-10-02 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 223.6 |
| 87e987ae-b347-35e3-b6a8-385a8f3a25e3 | -12.9548 | -62.6806 | 2024-10-02 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 340.2 |
| 6593d5fd-9845-3316-b755-b45657f1c595 | -12.9738 | -62.6795 | 2024-10-02 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3d2e9f87-7263-3d5e-bb86-f0503cea598d | -13.5965 | -51.1367 | 2024-10-02 00:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d03837e5-c8d0-34d9-9085-30378256ed3c | -14.83 | -58.6154 | 2024-10-02 00:56:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| fdd53956-7b58-3130-ae25-082c0f06dc4f | -15.1197 | -55.8307 | 2024-10-02 00:56:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 906f75f9-cb16-369a-8c76-3342052f4205 | -15.139 | -55.8285 | 2024-10-02 00:56:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 42e73f02-c7f9-3d1d-a6d9-e12c5448ffa1 | -15.1393 | -55.8079 | 2024-10-02 00:56:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 978db1c2-d767-3c97-bf3e-e6cfc87f6718 | -15.8933 | -57.1754 | 2024-10-02 00:56:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| ad2b54f6-699e-32ff-9d87-d028dcc7bfd7 | -16.6868 | -57.4741 | 2024-10-02 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 638c60fc-6733-3f07-860c-4d87aa6ed805 | -16.6884 | -57.3718 | 2024-10-02 00:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| 3c65aa87-0700-3108-a345-01479c4d27a7 | -16.6887 | -57.3513 | 2024-10-02 00:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.6 |
| 6ab7fc2d-4991-3c19-8a0a-b00c9c618ae6 | -16.7063 | -57.4718 | 2024-10-02 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.5 |
| e09a37a5-df5a-36a9-ab71-0c531386a9e8 | -16.7082 | -57.3491 | 2024-10-02 00:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 122356c9-5e9e-3c30-8ca2-96bb1aabd62c | -16.7265 | -57.4287 | 2024-10-02 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 1669cdb6-1110-3786-a85b-ac047e44a8f4 | -16.7269 | -57.4083 | 2024-10-02 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 9f61a207-424a-372e-9742-f04227e80a9d | -16.7452 | -57.4878 | 2024-10-02 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| b673d9f3-ac98-3961-848f-29215766e7c5 | -16.7455 | -57.4674 | 2024-10-02 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| e7d9d88f-78dc-36f4-a78b-93e65a7bd974 | -16.7461 | -57.4265 | 2024-10-02 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 6a059dc4-a3be-33fa-af1c-47b23ea6d0be | -16.7663 | -57.3833 | 2024-10-02 00:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| eafe9577-01e3-3f8a-8208-981bc38688c0 | -16.7666 | -57.3628 | 2024-10-02 00:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.3 |


[Clique aqui para ver as próximas entradas](README17.md)
