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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| defda422-aab1-3a73-bfe1-b269be9c7fee | -12.6995 | -45.3764 | 2025-11-19 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb5f4fa7-4245-306b-917c-835608a0dd78 | -9.9975 | -44.077202 | 2025-11-19 00:35:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4ceaf71-37b0-32ad-aeed-06665efcc7ab | -12.6444 | -45.5434 | 2025-11-19 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64cf2377-6eae-3b24-a160-b4745d2f59da | -2.5406 | -45.3825 | 2025-11-19 00:35:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43cd1880-52b8-3349-983a-59c535cced27 | -11.6215 | -43.912201 | 2025-11-19 00:35:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 209748d4-5c58-3a68-95a0-2273c7da908d | -4.9846 | -44.756302 | 2025-11-19 00:35:00 | METOP-C | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb9d3ace-e519-3151-8a87-fde6783b056d | -4.5459 | -46.743 | 2025-11-19 00:35:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee45ffa-97c7-3d55-8318-24002ed67bca | -5.3426 | -43.026001 | 2025-11-19 00:35:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 1fe9a439-e470-3d57-9ca1-8c2e6cbf75d7 | -13.9737 | -44.220798 | 2025-11-19 00:35:00 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb62f92-1206-3be5-8b74-c3193c191661 | -12.1646 | -43.983601 | 2025-11-19 00:35:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d088a35f-448a-3dc2-ab7c-59f43d2c2e73 | -6.7179 | -42.126801 | 2025-11-19 00:35:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ac8724f-2e79-3def-8458-72ddf186450c | -11.9303 | -44.8041 | 2025-11-19 00:35:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c0958a3-7448-39b0-8049-fb25d053f453 | -2.5371 | -45.367401 | 2025-11-19 00:35:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee85e62-946f-3ef6-8a7f-c7180df8ce84 | -21.4282 | -47.682598 | 2025-11-19 00:35:00 | METOP-C | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bcdc0c66-edf3-3a3a-a36d-ed1ca04c29a3 | -6.1169 | -42.940701 | 2025-11-19 00:35:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 147bdb9c-fd5f-3642-af95-98d4079d5ed3 | -13.4728 | -43.037399 | 2025-11-19 00:35:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6df5f79c-1828-376d-80ca-3e012f035db5 | -9.6642 | -43.8881 | 2025-11-19 00:35:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c9caee4-7e72-38bc-8db9-174856d6d83c | -11.5119 | -45.004501 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c88ddfd-0eb3-32f1-ace6-a31ad3d1357a | -10.3509 | -48.893299 | 2025-11-19 00:35:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6b2152dc-6a02-3442-aee6-30989f4fec11 | -5.8401 | -44.930199 | 2025-11-19 00:35:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a841a354-23d5-3263-8982-a33283af0a0e | -6.2975 | -43.7953 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de20e6ec-55c2-3e1f-802a-4976a174f292 | -10.0608 | -47.898499 | 2025-11-19 00:35:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e6a378e-167f-38bf-b439-b78df91c1ec5 | -12.8786 | -50.141602 | 2025-11-19 00:35:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 777080fd-7940-3ef3-9456-d7c4ec38d4b9 | -3.2523 | -43.036598 | 2025-11-19 00:35:00 | METOP-C | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16b78b78-ff40-38bc-bde6-0923eed1bffa | -10.3544 | -48.909801 | 2025-11-19 00:35:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71f3b0e8-9bc6-3c43-8279-0cbebec7460a | -6.337 | -44.2281 | 2025-11-19 00:35:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9608a49-71d1-328c-8f96-462bef2a0140 | -4.5852 | -44.0616 | 2025-11-19 00:35:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 743530fc-02ed-391c-bbf9-2596b55aa346 | -13.4842 | -44.3811 | 2025-11-19 00:35:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f244b97-1560-3964-b9ea-4b0c9d130042 | -9.3864 | -48.428799 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a2e8ba0-bd9f-3d2f-ba57-ae5b1036f9c5 | -13.2868 | -44.375401 | 2025-11-19 00:35:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a95e79c-7412-3695-9eba-0586d803cec8 | -10.3429 | -48.903801 | 2025-11-19 00:35:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0038b4af-b81f-339a-b962-1fbb5cc4995c | -15.4825 | -43.1506 | 2025-11-19 00:35:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 6afd681f-7816-31f5-a6c8-e4a0a7863fd4 | -10.6969 | -44.7794 | 2025-11-19 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 600055bf-127b-3d5d-b396-2b2f505e5d07 | -4.1441 | -46.790001 | 2025-11-19 00:35:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 133bb251-93b1-3a3d-9669-1bc100b0ef50 | -3.5612 | -43.4753 | 2025-11-19 00:35:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65cccb4c-7209-3aa1-87d0-ff4845dd5014 | -10.6133 | -44.954498 | 2025-11-19 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 436f9372-7f40-3589-9a44-f840eac4adaf | -3.1534 | -51.678902 | 2025-11-19 00:35:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e8c5aa5-7b8e-33c2-aed6-bbc597b247d4 | -3.3495 | -43.495399 | 2025-11-19 00:35:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afc62e6a-c660-389b-bde7-00ccdf2a3944 | -10.7654 | -44.808102 | 2025-11-19 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 48628ea1-0bfe-35ce-8249-2b1249b33508 | -12.7643 | -45.435001 | 2025-11-19 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b512f479-09d8-32c6-a861-2576c9d939a5 | -3.9277 | -50.2785 | 2025-11-19 00:35:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a22b141f-8ed2-3644-831f-43688119acf0 | -5.0357 | -43.6063 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba4c03cc-8615-3b6d-8240-b203030086f0 | -10.8695 | -49.538502 | 2025-11-19 00:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb49fb4a-3e7e-34b8-9bbe-45e1a9c5b657 | -4.6687 | -43.2299 | 2025-11-19 00:35:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc8e0a09-2151-35b3-abc8-77e89d8b6b47 | -11.5271 | -44.890499 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab5e6a8-8239-38ab-a6d6-00b0b5f4cb7b | -11.6686 | -47.967499 | 2025-11-19 00:35:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab711c06-5b71-39e0-a1f0-74649d422a06 | -2.2248 | -44.819801 | 2025-11-19 00:35:00 | METOP-C | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2b05aa0-9ba7-3299-a564-a934c96d7fc1 | -8.8732 | -47.3246 | 2025-11-19 00:35:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc5c7c8c-2b6c-3d88-8a6c-c41ac09ac4db | -5.8384 | -44.922798 | 2025-11-19 00:35:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd8c0e5e-52ce-32a0-8533-dafb4789a2d6 | -15.7738 | -43.5191 | 2025-11-19 00:35:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ec3a7d9-e72f-3371-aea4-fe820f4486ea | -6.1211 | -42.958698 | 2025-11-19 00:35:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ee5200e-af17-332e-9cb8-935c67175fb8 | -10.5425 | -44.112202 | 2025-11-19 00:35:00 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57416645-f31d-3e6d-83f9-ce06619000a8 | -10.7391 | -44.917999 | 2025-11-19 00:35:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a2f4c48f-e109-36f7-9f20-a02fa17ad27c | -12.1485 | -45.173302 | 2025-11-19 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0829fcfa-e224-38e1-ab79-3f1f5cf8b93f | -3.5494 | -43.468601 | 2025-11-19 00:35:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34844e53-2a81-3515-8144-57d34217ce61 | -10.0641 | -47.913399 | 2025-11-19 00:35:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a671daa-07e7-399b-8fe2-51b01d957231 | -13.2008 | -48.316601 | 2025-11-19 00:35:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da8eda8d-8864-31eb-88b6-59f6617f9ad7 | -13.9721 | -44.213699 | 2025-11-19 00:35:00 | METOP-C | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7eac43c-4a09-3eed-943c-eaec6a892835 | -6.2956 | -43.787201 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07d107e3-d153-3923-b5c5-d999f1312ecc | -6.3351 | -44.220299 | 2025-11-19 00:35:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4db36cd1-b651-3098-a7bd-af3fa3acc1fc | -4.9127 | -48.169201 | 2025-11-19 00:35:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b0c0720-7a37-385e-9bce-32b2cfa3e400 | -13.4746 | -43.044998 | 2025-11-19 00:35:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 33bca7d6-896b-3a20-9c26-dfc06ba8f236 | -4.7853 | -40.257301 | 2025-11-19 00:35:00 | METOP-C | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9336d60d-913f-360e-9138-2b2f7f44d92d | -4.6743 | -43.209599 | 2025-11-19 00:35:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afde568a-058a-33a5-9151-ea0a9764c1d1 | -3.557 | -43.457298 | 2025-11-19 00:35:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d48fc40-4b06-3bc8-a21c-d2c4a45431fd | -3.4935 | -51.089901 | 2025-11-19 00:35:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e45ecd7-23bc-3e2b-a281-b47f4867a757 | -15.4957 | -43.162899 | 2025-11-19 00:35:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 7025f520-4a38-3a03-8ea7-a8565e23721c | -12.3492 | -43.978199 | 2025-11-19 00:35:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34d9cecf-9893-37c6-927b-969603c8d666 | -13.4186 | -43.026402 | 2025-11-19 00:35:00 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eaf0ed07-f236-3781-857b-7fb290d20c2b | -6.2493 | -43.6777 | 2025-11-19 00:35:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e2b6978-ca73-3606-846d-92a6fa2e94ac | -9.3847 | -48.421101 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0bad69e-f94e-3f5e-b8af-8d102ed12a15 | -4.3338 | -48.9781 | 2025-11-19 00:35:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf261808-28be-3508-843b-cabecdecb556 | -13.388 | -44.366501 | 2025-11-19 00:35:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50a31690-589a-3791-8220-7c8d4cd2330a | -12.8829 | -50.162399 | 2025-11-19 00:35:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74de2235-3fc6-3bdc-a458-f22bb356b664 | -12.3509 | -43.9855 | 2025-11-19 00:35:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87ba5681-bebe-3785-8b37-10295a517019 | -11.4195 | -43.312698 | 2025-11-19 00:35:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f2ca881-2aac-3a57-94fb-45ce5d619cd2 | -10.7473 | -44.908699 | 2025-11-19 00:35:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b0ec8dda-742d-3b43-b1df-4858542b7e98 | -11.7922 | -44.6064 | 2025-11-19 00:35:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a65e621-ba23-341f-8779-52d7a34a76f7 | -3.4915 | -51.0812 | 2025-11-19 00:35:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e64a8b0-ff3b-3384-ac68-3b4775dd310b | -11.0182 | -49.0383 | 2025-11-19 00:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d5b1279-df13-3cfd-b62d-6b414a5b0f95 | -6.3054 | -43.784901 | 2025-11-19 00:35:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d9b1dda-fa2d-3951-a0e9-34688e1d74f5 | -7.8319 | -42.167198 | 2025-11-19 00:35:00 | METOP-C | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a188cbb5-da3f-35dc-823c-116f3cef5cbf | -11.5255 | -44.883499 | 2025-11-19 00:35:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 805867fe-fb68-3b56-8732-3444aed5f96a | -4.1425 | -46.783199 | 2025-11-19 00:35:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3da514ad-2dbc-38aa-8b2c-35d1d4f35d4c | -9.3783 | -48.438599 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efd3790f-4b04-3e70-9ab1-f8e9cc174932 | -4.28 | -42.107101 | 2025-11-19 00:35:00 | METOP-C | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f79b0ca-858b-3b1a-a43d-bf92ef7f3dd8 | -12.6429 | -45.5364 | 2025-11-19 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69918f92-d641-3ae1-864a-1786bffc4b27 | -13.0724 | -42.1301 | 2025-11-19 00:35:00 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b0063909-4539-3267-888f-fb9b18a08e4d | -4.9225 | -48.167 | 2025-11-19 00:35:00 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e049bc80-d8d1-341a-b74f-ee0ed8555ff7 | -12.8139 | -49.3423 | 2025-11-19 00:35:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d55e1c7-58c5-3557-ac25-b129578a2530 | -3.3474 | -43.486401 | 2025-11-19 00:35:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e253a3b6-2bab-3073-a260-0980ba2817c1 | -9.3715 | -48.407902 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 044fc7af-2519-3d69-b93e-b4416f669be0 | -3.5591 | -43.466301 | 2025-11-19 00:35:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e676f3f-52f7-39db-94fe-bb257eddf859 | -10.8793 | -49.536301 | 2025-11-19 00:35:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2600e985-8b35-34e0-b05e-4359f04db9e4 | -12.1629 | -43.976398 | 2025-11-19 00:35:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed958103-5caa-38d9-92ed-37b82c0535cf | -1.3483 | -47.011902 | 2025-11-19 00:35:00 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cbbaed3-a74f-383e-82ef-535fd4c28d93 | -4.6645 | -43.211899 | 2025-11-19 00:35:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fef0dd9a-cbf8-34c9-9df5-93a0a153fe51 | -9.3766 | -48.430901 | 2025-11-19 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82a74268-8494-3c9c-905a-7657d8a331d5 | -1.3467 | -47.005001 | 2025-11-19 00:35:00 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 617df964-2cb5-38a5-8443-d58b339ed468 | -2.8179 | -45.4221 | 2025-11-19 00:35:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
