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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a438c291-021c-331c-b5c9-0c4563b854b6 | -7.56175 | -43.33438 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a79ad8e-304f-3805-bc54-58656f233d91 | -8.29579 | -55.09902 | 2025-05-27 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 380cdedb-4889-3af5-8847-e33fc92fdcda | -6.2308 | -43.34681 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a48d45a9-636d-3b50-96e4-514c46e1ef53 | -9.15712 | -49.65334 | 2025-05-27 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 080af9fd-84ae-3dfa-bbf3-7c9d6a40caf4 | -6.22721 | -43.34627 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8e72249-1da9-332a-bf92-5d72caafc7a4 | -6.64825 | -43.20144 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa50d503-5ffe-3fc2-b145-7d3bd419c962 | -8.43147 | -46.65085 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98aea4ab-d4d3-3d4f-baf3-7a96b0d010a4 | -7.60078 | -43.39671 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c4296c8-ccd9-3fe4-a674-97feb1650e5e | -6.64761 | -43.20564 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a229ffc-7661-3860-adaa-b3abe7895468 | -8.4337 | -46.65836 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed8f3eac-73b6-3d73-a539-ff6a217375d0 | -7.60568 | -43.31526 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7da6c0e4-3ac1-331f-92e4-6ab85dbd67f8 | -7.56585 | -43.35679 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5b09250-1406-3195-bdaf-a51e371df901 | -8.01564 | -49.68782 | 2025-05-27 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5c8cf169-090a-327f-887b-faf2d501e60a | -7.23062 | -43.11041 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| c0c596ff-6b39-38cd-8053-65ae328bf47a | -8.42814 | -46.65033 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59ba3d38-ed20-3c9f-89fd-47be0e2c8542 | -12.2739 | -44.58646 | 2025-05-27 04:27:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 830a9440-7274-3456-9381-efcc2ece9074 | -11.56998 | -47.44403 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14057e92-f0e3-3625-a14b-0e8502a3bd8b | -6.16238 | -48.06176 | 2025-05-27 04:27:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea00af04-ebc0-3a77-b86f-be049d596047 | -11.56277 | -47.44647 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 363a087a-ad13-3655-ad34-059cd41c43b7 | -10.73323 | -49.29513 | 2025-05-27 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ea3de6c-8fc1-3a8a-937b-8a3b90b38666 | -10.35975 | -47.97574 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8ca60d6-2afc-38f7-870d-69f61fd81ace | -11.80366 | -44.27007 | 2025-05-27 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 829b3305-37b6-3214-9bbb-dde6f15cd476 | -7.57014 | -43.35305 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7ee401a-7d43-3ab6-b1e9-89fdc2269165 | -8.75092 | -49.75616 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8d6700c6-46c7-32a0-b5f3-9de8921a54a9 | -10.65436 | -44.49609 | 2025-05-27 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9815b547-9d6e-3c17-bb0d-b8988e4655eb | -8.59636 | -49.85863 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc9581f5-da05-3f7f-b86d-bf4925a7b7e3 | -8.29678 | -55.10126 | 2025-05-27 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14bfb46a-570a-3830-be37-ca471a553ce6 | -9.6068 | -49.02759 | 2025-05-27 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7afe36fc-bbbb-3270-b4ae-5ebae33e4c2c | -6.83257 | -42.79674 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e8c9a72-ac34-36f7-b12c-052eaa0d434d | -9.60336 | -49.027 | 2025-05-27 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5566eadb-afd4-3b19-b924-f58b8f1b9055 | -9.02706 | -47.73459 | 2025-05-27 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b69fea97-0fe9-3658-825f-09290d496395 | -10.23325 | -47.43048 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1db90fdd-deb0-3923-8f99-c3008859fb39 | -6.16641 | -48.05855 | 2025-05-27 04:27:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38842c19-ceab-3d6b-bcef-15494d99c877 | -8.36416 | -47.07654 | 2025-05-27 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e99076d8-51c1-3611-872e-ce52629d238d | -10.33855 | -47.9796 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a366599-8e49-3968-bc1a-8e1ef49ce7f0 | -10.94643 | -48.15495 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be1e8d21-b168-32eb-925f-fdf403e0d38a | -7.54409 | -43.18518 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b9ad9eb-5cbe-380e-82e9-a442f5169888 | -10.71474 | -49.62326 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8a6ee8a-5bd1-3439-ae23-068d59058ecd | -8.00202 | -46.15697 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 139278b0-4fff-33c2-abf1-1028ea19f28b | -8.04152 | -49.64899 | 2025-05-27 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdecbbf8-dfd9-3114-8a1b-10bdf0914568 | -8.38678 | -49.66074 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64e1eabd-3bd2-3645-b87a-f64fcc5498f5 | -11.5828 | -45.025 | 2025-05-27 04:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 613c21a0-ec39-3bc6-9854-f433177f25cb | -11.57544 | -47.62565 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a5f1072-8170-3d36-864a-2e21f75ea8a2 | -6.64334 | -43.2093 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 11b628ad-a5ec-3457-bf6c-80653d2acc6d | -11.5661 | -47.44701 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 244973c0-1a5a-3f97-8e40-2c60cefceb75 | -11.56665 | -47.44349 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 17379296-9cfe-32c9-b74d-e3870035cbe4 | -6.63608 | -43.20821 | 2025-05-27 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d2c5d00-1bfa-3b06-a006-2cd11125f75d | -9.38737 | -48.42194 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5142a21e-9158-3949-be27-e40372bdf5e9 | -5.41709 | -47.56955 | 2025-05-27 04:27:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 141d2cbb-adc1-3771-9e53-c758dec6fefc | -10.64302 | -48.08713 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46d19b46-6c64-3011-97bc-6116eec8b8a5 | -11.80426 | -44.26463 | 2025-05-27 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a94782e9-c626-3961-9eb3-0a9515756e0f | -7.59366 | -43.29586 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 704035a7-39e5-3607-943a-d66bb163ec1c | -11.55944 | -47.44593 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 338fa11b-ab94-3e12-8033-1c3f49a039b1 | -9.57462 | -49.1157 | 2025-05-27 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 572fd60e-4982-355e-bcf6-623c41becaa5 | -7.20127 | -43.11218 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 24ac50c0-7e7f-3aba-935a-bdbee8da3e8e | -10.3631 | -47.97628 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f2dbb92-5f9e-32b7-9371-5ca93ed4b980 | -8.75571 | -47.67995 | 2025-05-27 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7b7d07f-b5d4-3472-b01a-4b861e6151cc | -5.9636 | -36.09963 | 2025-05-27 04:27:00 | NPP-375D | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cf5f74d1-8f5c-30a9-9230-7b19d3644d1d | -9.39297 | -48.43034 | 2025-05-27 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f93d83f-c53f-3ff4-a4c8-2c47f1c93e51 | -7.47241 | -43.36193 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b620d30-b3e6-33e5-800b-d11553097bca | -6.50267 | -47.4875 | 2025-05-27 04:27:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8b3c3be-96b7-3143-b0ac-2ef503ce6232 | -7.36525 | -43.6837 | 2025-05-27 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1f0c401-f1dd-30c7-b4ad-c18cb6379374 | -7.15881 | -43.31874 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40e8e0e9-48f3-3172-be8c-b889c79a64b5 | -7.96974 | -49.69724 | 2025-05-27 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a080ccd2-b023-3da0-a5c8-2dfd9d51157e | -8.43479 | -46.65138 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff8d5486-e4fb-306e-aaab-70e546ca726b | -10.63543 | -48.80476 | 2025-05-27 04:27:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1ba2c54-a443-37ee-897e-bcb42cf38500 | -6.22362 | -43.34571 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b372a82-29ca-3f3a-b6cd-9fd9e48d76bd | -7.54664 | -43.1835 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e57856df-02d6-3c99-8baf-e6a43e2ae52c | -6.13146 | -44.03798 | 2025-05-27 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42cc3841-22ca-3b86-aa27-7a9498e572bb | -10.63632 | -48.08603 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1f42993-e9f9-3404-803e-ca5f68001c7e | -5.78108 | -43.61811 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 054daad2-e5eb-3ac3-8f8d-4f810b1d8813 | -7.22396 | -43.11128 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 48d8d7d0-84a4-3ea4-a4f8-09091491232f | -7.54776 | -43.18573 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d23f4b4-2fe5-353e-9e07-d5a01f03f9cc | -6.88133 | -46.35888 | 2025-05-27 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8bdbd9e1-1b8f-3dc5-969c-c25948f5c8c9 | -6.83695 | -42.79293 | 2025-05-27 04:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bee763f3-bc3f-3bb9-ac7f-e7be37b8076a | -8.02018 | -43.20377 | 2025-05-27 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b51c77f-c2d0-3287-a455-00516f8ab348 | -11.80065 | -44.26522 | 2025-05-27 04:27:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6eba2fce-3ecf-35bb-a58f-b5f9ae3454f2 | -7.5695 | -43.3573 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96d03e8d-3ce1-33b5-bb18-748fcc15777d | -8.43257 | -46.64387 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7583c0c-afee-35fc-a800-2ef0d9ab7b20 | -6.22657 | -43.35039 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 81aa2a46-04b0-3d80-bacb-97a7c1486337 | -10.72055 | -49.54459 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b7b75e9-0e70-3e09-8b72-c9b985b1795f | -6.64666 | -41.9959 | 2025-05-27 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b18fdde9-99cd-3e6d-a99d-d5df4abe6abb | -6.15955 | -48.05749 | 2025-05-27 04:27:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5da5b548-7a56-3a95-910d-08e491c3efe3 | -10.67651 | -41.79503 | 2025-05-27 04:27:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bfc21b66-3237-34ee-a05d-e7a53ffa2bbc | -7.47861 | -47.41403 | 2025-05-27 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 167ba9c9-db28-3cac-b444-ebfe7c3b3a0a | -11.56 | -47.44241 | 2025-05-27 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de82348c-02f7-3cb8-98a4-7214a8d09914 | -9.35136 | -50.23421 | 2025-05-27 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 274b44da-b4ed-3b85-8595-fe52b908675f | -10.7141 | -49.62716 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9907b23f-4455-36c1-bdb9-c7c6a0ce5f3e | -8.64956 | -49.40588 | 2025-05-27 04:27:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 195a218b-4812-3eb9-bf36-e7bb6563eb67 | -8.75226 | -49.74799 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 24c6d944-99b4-3e66-a3f5-af6bdf2e50a2 | -7.20192 | -43.10788 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a4b6498b-1dea-3271-87d5-daa16a4ccf4e | -7.20061 | -43.1165 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 770a453d-69b6-343b-be97-368b89086996 | -7.20494 | -43.11274 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 23a6c461-3003-37dc-80f6-ccab74034199 | -6.23206 | -43.34624 | 2025-05-27 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e5a8118-ad00-3fd6-bb2a-6ae35f2c65e8 | -7.22462 | -43.10698 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d1033a6-fb2a-37dc-8404-114f9f5b443d | -8.43534 | -46.64789 | 2025-05-27 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 376eb87a-a374-3b16-a294-cee677a99841 | -7.49916 | -43.35732 | 2025-05-27 04:27:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b0f108a-31fe-331e-8047-4274ac63b22c | -7.2313 | -43.11242 | 2025-05-27 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5f5e5334-c32c-322d-bcd0-c584608acfd1 | -10.95091 | -48.14838 | 2025-05-27 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9699fc51-f4cb-306a-9298-e8a5bdc7da5a | -8.75159 | -49.75208 | 2025-05-27 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README10.md)
