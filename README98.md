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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b0e64c7-f4e9-3840-94a7-933e21ac8521 | -15.78445 | -43.64761 | 2025-10-17 04:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7b19e2f-f8ca-396e-ba3c-c34c33e0bfb4 | -14.71943 | -48.30033 | 2025-10-17 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0c87227-e20e-3288-b6f5-8981fcf3e069 | -10.28119 | -44.03189 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0267c16b-001a-3b0d-85b0-92b4ecd3067f | -10.57432 | -47.42019 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac1bc6d6-81eb-3c1b-8b15-36b1702583a2 | -11.57712 | -48.55641 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f33f4e76-1331-3e59-a135-2556aee42f93 | -12.06378 | -47.98573 | 2025-10-17 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6588477c-6e8f-38bb-8235-da3be89786c4 | -11.97243 | -46.55997 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c82b1d81-b1c6-3299-8e8f-9191d6005dad | -10.80826 | -47.93678 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf89b0a7-e6e8-322b-840a-dce27f7362fa | -13.93322 | -48.69231 | 2025-10-17 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 012fc50e-fae8-358c-805d-717e516a2055 | -8.4463 | -44.18219 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b93ff66b-0930-3391-af97-fcc8e3bafe0d | -10.81194 | -43.93233 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad2d594a-195c-3974-85dc-d0b23be20192 | -8.33669 | -49.07417 | 2025-10-17 04:51:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ed22783-8197-3d84-8c02-d65a97ebe049 | -9.27284 | -50.60926 | 2025-10-17 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f69b9d9-5bd9-3ddd-9928-f81d9a8b8808 | -11.97188 | -46.56391 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84002405-d4dc-3aa4-87a9-2c367ec6b0ee | -9.06498 | -48.84758 | 2025-10-17 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad4e88f6-79ca-3bac-b962-d687c8935b25 | -9.23512 | -45.27863 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24538723-9f77-303e-babc-f1ea741ab8bd | -10.50587 | -43.40041 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceb8fce5-d98c-3f5c-9598-267c2e627bf5 | -9.01968 | -46.6579 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c10c613-ba3d-3526-8da2-74d543a20c68 | -8.2586 | -44.06084 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1238a3cc-2461-372a-8895-7e5547f92d71 | -10.10984 | -44.56623 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31420c05-7c8b-39f2-8c7f-c239456155ca | -10.65389 | -45.2929 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07ca0ee8-3ef9-3a4d-b711-383bafc6eb11 | -14.35048 | -51.46973 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f06731b3-cd68-3fe4-9a22-638d4f5438c9 | -11.4767 | -44.28504 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04643843-a324-352b-828b-d60889cb7e6c | -8.19749 | -46.93427 | 2025-10-17 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6282e043-2a35-33d7-b50e-62616cdb5ec3 | -10.62887 | -53.89182 | 2025-10-17 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ea10bd-2a49-3b04-abf2-2bee5379fbee | -9.72059 | -48.91532 | 2025-10-17 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 30d10de6-f843-3323-9e78-8d92724a5656 | -9.97424 | -47.0044 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5c60e2d-cf4d-31f1-924c-d78e63f1216b | -9.28923 | -46.91026 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01a23d9c-36ff-374a-b85f-5ff2ba6e1bcf | -10.61502 | -45.2392 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25c9081a-0662-3b95-85b2-3ace9cfe0a2b | -11.41355 | -44.21883 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 963e3d8e-f13d-3f3e-a925-a8ab17bfbf05 | -9.28997 | -46.90511 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e43f463-9816-3c62-b1ee-78f534fd6918 | -10.85633 | -51.29158 | 2025-10-17 04:51:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b67cc3-ba0b-3332-8b90-29f45c6bf671 | -9.88649 | -47.67956 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eb9c0c8-11e3-3eee-a8b0-f0c1f6838a77 | -10.18238 | -49.50859 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eeded6c8-4e2b-32bd-b0d9-6f0630b5c11a | -10.6643 | -45.32557 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1e88ba9-3df3-3daf-87d3-a3523a2d6032 | -10.50707 | -43.39116 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 218ef224-ef2a-376e-9807-52449a3da2b9 | -10.27209 | -44.02471 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22f1c0fb-e051-3bd1-810d-4c7ad8aae719 | -14.33124 | -51.43623 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 291b8298-9173-3a46-a358-63af0ae99ca0 | -14.33747 | -51.46385 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b6166154-d85e-30e1-bf2c-299e323273e3 | -10.0584 | -43.87038 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6e928a5-76d4-37db-90c6-996f23e7d0d4 | -11.19104 | -51.75108 | 2025-10-17 04:51:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24fe39b1-1503-3653-8bef-fc937876337c | -14.32561 | -51.47334 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55151cac-70ec-3c9d-979d-c3d16db99f7d | -12.45364 | -54.48243 | 2025-10-17 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87ca6f24-861e-3ae4-b2de-c2230f9e54b6 | -9.13374 | -46.63939 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26dbd957-1c92-30f3-ae37-eaf8a632409b | -11.5775 | -48.55865 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87ad808c-3885-3784-b49a-efcac5198604 | -10.28472 | -44.04331 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9b4685bb-4765-3996-9b78-021464114c89 | -8.82103 | -50.05399 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a41cdb66-66c2-307f-a9f7-506141e9249b | -9.21695 | -46.89323 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b90c4a9e-8da4-3e62-ac42-234e7db228e6 | -9.45036 | -56.65538 | 2025-10-17 04:51:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 114568b8-c506-31cf-8cca-d89ece9ccca5 | -10.10675 | -44.62591 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f718df24-096e-3ea6-8b89-a40eac76547d | -10.01649 | -45.66255 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cecc57f-eecf-31fd-ad56-8db6e9dfbf1d | -8.45545 | -46.2444 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0efb99d6-9add-3960-aa0d-b7110e121676 | -8.24895 | -47.87104 | 2025-10-17 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab4778db-b5a7-3444-a3f0-f1a0ffe4b363 | -10.95605 | -49.77278 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f28e2844-4645-397f-b7bb-2d9979157903 | -10.52953 | -49.54644 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e21ffcf1-cbe1-3d87-88ab-75b4c1154e94 | -12.91332 | -41.82655 | 2025-10-17 04:51:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cdf1cd28-0016-3ae6-bb1d-685efa19668b | -15.03324 | -48.76746 | 2025-10-17 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ec7ec94-56f5-3772-bbba-917417b6d906 | -10.95315 | -49.76834 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| a79b3208-f97e-37f0-b761-89e8b055458e | -10.29597 | -44.03389 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d261f6a2-8e55-364e-981e-ab0c4feb689f | -10.15252 | -44.5359 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9946c0b8-5c98-3015-9d45-06e9494a1c35 | -10.53496 | -44.50665 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da8805d8-943a-367b-927b-d92cf9fb367e | -11.16616 | -46.12699 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e6b564e-f91c-3550-9d2f-28088c188e94 | -12.42197 | -51.31265 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e65ff75-32ff-3a9f-8218-37b52a53fcfc | -13.92945 | -45.61805 | 2025-10-17 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bfc1615-6d8b-39e3-8308-f35baa350954 | -9.34015 | -46.90866 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c64e8357-d2dc-3d5f-86cf-de2ec80ec008 | -10.97751 | -47.89098 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8450f34-10d2-3946-958b-9ca97abbf2ec | -11.57198 | -44.05606 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 72da7068-dfd1-31fa-befc-741e034471c9 | -10.27626 | -44.03129 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 907ca7fb-81d8-3056-9dc2-7813bd3034b6 | -14.30636 | -51.43986 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cf1fc21e-c00c-386f-afb8-9e49e705e921 | -8.4688 | -50.10109 | 2025-10-17 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0d6e99b-ecd3-3fd1-8bcd-6065f70165e0 | -12.16476 | -45.07637 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccdc4f11-d53b-399b-abff-8fb2ad76f4b2 | -9.25664 | -45.25522 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e4394e9-fbc5-392e-96d5-63c6ab76d968 | -13.50686 | -47.16836 | 2025-10-17 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d70b67a-ad33-3b27-af41-6d455649b554 | -14.08613 | -43.62285 | 2025-10-17 04:51:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9fccabf-fcde-38ef-94e7-7e414fda2aed | -9.24068 | -44.37529 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0a99e94-a4f2-3cee-ad3f-862f35e21ce1 | -9.94614 | -45.71477 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9654e067-995b-3f04-8256-b42b08c3ff62 | -8.49192 | -48.49531 | 2025-10-17 04:51:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dc64212-e205-340e-b46f-124fd0dc3328 | -9.28448 | -46.91494 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8ed548b-fdf8-3881-a84d-f77cc90cfc31 | -10.10895 | -44.56462 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aab73bf6-4884-3d06-b117-cf9e36ee97b5 | -11.73726 | -55.17976 | 2025-10-17 04:51:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddac8018-14e3-3122-83c7-d7afbb68f81c | -11.57686 | -48.56315 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fefe72b8-3230-39bf-94ff-9e50a206b6bf | -9.14411 | -46.59653 | 2025-10-17 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1c3b46f-5125-3581-b88f-d550ed371a93 | -10.28965 | -44.04393 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bceb538d-cee4-3c02-b992-409dfe191eb4 | -11.4101 | -44.20697 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dc14a35-6da5-3bb3-89a0-0248a3691123 | -10.10761 | -44.5742 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37516092-8c95-3d59-9170-af0cf7251b91 | -15.14695 | -47.95923 | 2025-10-17 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 362d5645-1690-35ca-92ea-2f5df091bcf1 | -14.23378 | -54.90142 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8dea86d6-2634-3e34-84fc-e5f142ea2464 | -10.27043 | -44.02966 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99f61959-fd90-39c7-a212-7d03dff20891 | -13.92688 | -45.61995 | 2025-10-17 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab46b1d5-3044-3dad-af8c-1f6f6e221bd5 | -13.73255 | -48.21322 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e43930d-9ed3-3006-9cd6-d9f8599e6223 | -13.23478 | -47.11724 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afffbdb3-9295-3f6a-b866-4c2aa075287a | -10.2706 | -44.03628 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dedaba98-d743-366e-82b1-68dc9c272add | -10.5026 | -43.42564 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 17c4043e-c99d-3d4e-a915-b08808ac284e | -10.504 | -43.41483 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 273909c6-971b-30c6-8c8e-f9ff9fd07a58 | -13.4196 | -48.57716 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72289da8-7d12-3956-98bf-17b662529945 | -10.29181 | -44.02737 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d2b834fb-317f-3494-84a4-1394d830f25b | -10.10287 | -44.57357 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e23cb54a-91cb-3303-b1b8-9d8c72ce0b32 | -13.41579 | -48.57656 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13ca264f-32fa-3ec1-bfff-d33ffa5bbcf1 | -11.44852 | -44.1835 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cdcbff4-621d-36b6-a14c-8e0179a276ac | -12.77555 | -44.88511 | 2025-10-17 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README99.md)
