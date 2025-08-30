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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe425349-043a-391f-9803-f133c7b87f4f | -9.43833 | -60.53909 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4b723e0e-f168-3b25-b82a-1a7f87d2443e | -9.44341 | -62.32656 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6953364f-e985-3977-ad18-b1ec61022526 | -7.78021 | -45.46406 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a177a048-8f04-378c-9bfa-0de501d95d05 | -8.89609 | -62.10406 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98b0d89a-852f-3e6c-8f33-3a7a23354aaf | -6.00033 | -57.85381 | 2025-08-30 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3740be00-244c-386c-9542-8aeb4095a940 | -6.68678 | -49.77165 | 2025-08-30 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2885d376-67fe-3b76-8c7b-a6542da8bc83 | -8.67209 | -62.43223 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4566170d-b232-3272-b0a6-800898b07771 | -9.44008 | -62.32402 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82175920-5e13-3e22-890a-f7b0fd5b0866 | -7.58452 | -45.12864 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65cd4692-fe2a-3e9a-bbec-0af99eccc8ac | -7.16296 | -45.16368 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28f0c27a-826e-3b33-b0ad-dc4ad65d599d | -12.69806 | -46.80442 | 2025-08-30 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9acfa4a3-c44a-37b5-b9f2-f3bfe1ac785c | -11.85103 | -46.43987 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2de0f0a-1109-310f-aba6-2e975512469f | -8.44878 | -43.64413 | 2025-08-30 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c7f248a-fb06-3065-95e5-ce1a60aac28c | -9.21663 | -60.86537 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a519311f-0b1e-3b71-86b1-a1a2d4f7322d | -9.71147 | -61.30956 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 059e2d67-062a-37ae-a21c-b4ff54f92517 | -11.3157 | -43.64669 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a23e734-bf5b-30fa-bc23-332ae842c943 | -11.35669 | -43.54787 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f61eb93-9978-38df-909a-3b8b28505ab6 | -7.40956 | -42.05923 | 2025-08-30 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 98f55394-b6dc-387b-bce5-3f4a68a58aef | -11.15539 | -47.14579 | 2025-08-30 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| df03aa8e-e759-3075-93b5-400b03e9c024 | -7.95497 | -46.38747 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0ac8a7e-45bf-3ae3-b0a6-0976fcbf1f36 | -9.78203 | -64.25607 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f842697-f2b2-3b9c-b55a-7ede89b6d7d1 | -8.87291 | -60.73823 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49ccb5a0-4b7b-3877-9233-127fb3316f60 | -7.39831 | -45.92725 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 540d1eaf-cbb8-326c-b538-dcf19d11db0d | -7.15871 | -44.13704 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7892ff50-df62-3fa1-964b-0a8f7e58f5df | -8.8861 | -60.72678 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f19185b-6c68-3644-8c01-a2e639ce6df7 | -10.49427 | -51.62979 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c647206-25db-3dbf-ab54-f26f33125698 | -10.99525 | -46.84601 | 2025-08-30 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e2b1acc-24cc-3c4b-a3b3-08ee84cc62f6 | -11.84557 | -46.39276 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2d051a66-b449-38a2-8a0d-b34e750e9845 | -9.08439 | -59.48659 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6952e41-e94f-38e0-b15f-3f9b058c0cfd | -8.56425 | -63.02743 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| baceb37c-ef02-30d5-9d7c-772799453b3d | -8.55274 | -51.30603 | 2025-08-30 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fd90202-fe28-3511-9d52-c237647cd219 | -9.44593 | -62.32515 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8194936-2465-3ebe-9468-7dbe4dd3b335 | -11.87547 | -46.38684 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7b2f8fad-7a24-3d69-a43b-71f69985308b | -9.27599 | -60.4556 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0831348d-4399-3a66-8114-2110f37a7ba4 | -9.43774 | -62.33661 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| afb77498-e96c-39dc-90be-46e51972ca5c | -9.43927 | -60.56256 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 032a7878-d078-3208-8896-2b185fc97639 | -9.15185 | -59.56162 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ffe21a59-f2d3-39c7-888a-ad40aa0f5234 | -9.4452 | -62.34882 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9fd7e81c-ab95-3a17-978a-e374e7e1a3cc | -9.24079 | -59.77953 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 025133c0-f30c-39b4-b287-15622f55bad1 | -8.56003 | -63.0268 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 846934b4-b0b8-33e4-bda1-7e863557b7fe | -9.45093 | -60.55808 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4154bc37-17c9-3362-92ba-bc826aab5476 | -7.17156 | -44.46804 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a85143bc-1495-3b88-824c-bfda9f6262b7 | -7.16728 | -44.14305 | 2025-08-30 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1a3e4a6-7f95-31ac-9791-237b6b532d49 | -7.15808 | -45.16697 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d29b009-2d5a-399f-b4c7-7b857f04194b | -7.63782 | -46.556 | 2025-08-30 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb29f7ad-db76-34e0-a495-0ba763e69bc8 | -9.45214 | -60.55165 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a95a84ca-bf54-30a0-87ea-b26620779041 | -9.1122 | -65.76597 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fe27a565-67c2-3672-bcdf-c7153ac9b15a | -7.73778 | -50.29056 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33fc6f1c-92c3-3c97-a20d-ee907c3bea79 | -11.31025 | -43.6489 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c61c0618-d4f3-38e7-abf8-a5506789577b | -9.45371 | -60.5722 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85422088-db89-390f-92dd-72ff52add4f2 | -11.90044 | -46.71305 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eeca1c2-be12-3178-a792-fbb17e305ccb | -9.82612 | -63.86002 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f1b9b25-9565-32ec-9f8a-c7d24cbb02b9 | -11.07883 | -44.76824 | 2025-08-30 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed1a646-07b0-378c-ae15-772f10154b21 | -11.34307 | -43.59597 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90567322-6b25-3443-bda0-4739e8b02c19 | -6.87799 | -44.44128 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dce74b80-9d6d-35d5-9052-9d98f6b45baa | -9.11668 | -65.7438 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b12f2286-6c8f-3bbc-8c46-0ca8cbecff0a | -10.07964 | -54.93161 | 2025-08-30 04:49:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feba91cd-fa75-3104-a84a-c95323e6403e | -10.72453 | -47.00686 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7806861e-7a57-3b70-a8ae-248006d937cd | -11.30312 | -43.58412 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 714d881f-336b-3da4-b603-8098d78ab69f | -9.23543 | -59.78385 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d47538b4-221e-3562-a3bb-e4aa0f0eab9c | -9.58128 | -54.46981 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d403ef02-0742-3808-88a8-7fa19841f4b4 | -11.94097 | -46.69564 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ed2a62-042c-3f09-9b22-5c3806f59700 | -11.06996 | -52.05405 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c967d089-ac90-33d1-93ad-e0cb8005e3ee | -7.19963 | -43.70948 | 2025-08-30 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84edc5a4-6fdd-31c8-9082-ae9310a6e07b | -11.41008 | -48.9554 | 2025-08-30 04:49:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dcf8433-4ce4-3778-8f06-1afa695b18e9 | -9.44069 | -60.55597 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a034dd8f-06ab-307d-96d8-0d795821ff0c | -11.33132 | -43.60642 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4de2bf05-2fe1-386d-bdac-cabb1073629c | -10.37901 | -57.82553 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17202656-f758-398c-8b6b-0a769cf6695c | -8.82885 | -47.78237 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46006fce-041f-3d37-8d30-1180f3c6ea6b | -11.35835 | -43.57623 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78087589-e54e-3014-9fed-57664236415f | -9.4467 | -62.32104 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4810451c-ed86-3f64-a79a-e3678b7d7d84 | -11.32662 | -43.64228 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1da4cac-02b0-3ea6-9f05-56c3eaecf6a7 | -7.33559 | -59.64227 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6faa67d9-ab89-3970-8fbc-4e14140834ba | -11.3572 | -43.58543 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26a62169-20c9-3a3e-81c9-c26207f6dbce | -8.84532 | -47.80532 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7366df7-7321-307a-91b6-9f3a21c80910 | -9.43718 | -60.54548 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2be854d5-df9b-3ca1-ad1a-72a1a5781ab6 | -8.67039 | -62.4411 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47856cf1-c587-31b1-b660-5f7bc2ab7a3c | -8.56274 | -63.01218 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 905f766c-1cfa-31fe-942c-f21aed349cb8 | -10.07493 | -58.36371 | 2025-08-30 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 819f4f4e-bd6e-377c-895f-946072565483 | -11.84629 | -46.44309 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71c74391-7335-3869-aab3-a556f1c9d543 | -6.94813 | -44.30618 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eb2537c-a6da-3af1-9704-e34869d894f0 | -9.44691 | -60.55069 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bbd53580-d226-3f35-800b-3ed466dfe119 | -7.63111 | -42.66016 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fdf1eb1c-1e86-3558-b201-a633f559809a | -8.54763 | -63.0243 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fa6b1c9-57c2-396e-9620-68d9be452772 | -9.43836 | -60.5689 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66da43bd-4ee4-39bf-9e56-a454989b417a | -7.24573 | -45.45094 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fba88eb6-a3d7-3e16-9b7b-750648ddbbe8 | -7.71875 | -50.28049 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ce22615-f8a1-3d22-8fb5-93c9eddeebed | -7.0975 | -44.59934 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47c31f7f-b22b-311e-a77c-8a16b42b5b38 | -7.39801 | -60.59658 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7108aba-41a2-326c-9dd6-9fb6098f4f7f | -9.77771 | -64.24343 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9a8f6a6-c081-3e49-8c1a-2588967b6f9c | -10.38183 | -57.83446 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6365924-9e6e-3d32-b2df-0320ec83f797 | -11.40354 | -46.91063 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bc29dfd-3a9a-3767-ae38-39a0349e8266 | -7.73155 | -50.26435 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3eb1026-2aef-30fe-bb03-0e5b1b2e6125 | -7.77917 | -45.47143 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4a391048-570c-3503-9b2c-e00ece6a836d | -7.33613 | -59.63924 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31e6a09a-60d0-38fa-9733-ba7f65b573e7 | -10.67901 | -47.06948 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0d66051-1365-3ab2-97bd-d256c60e1b43 | -11.84728 | -46.43572 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 43c22fcb-7bb4-332d-ba73-0ac947f92a52 | -11.30987 | -43.61207 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3088fc1b-4d3a-321a-aca2-8ade32b8b1fd | -9.6026 | -55.38506 | 2025-08-30 04:49:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20a7ccf3-df43-3e06-bc8d-3004e1a7e621 | -9.4545 | -60.539 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README45.md)
