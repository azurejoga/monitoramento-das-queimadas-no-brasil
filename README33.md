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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0910e2ad-0c1d-3554-b6d8-6b93a60662a6 | -12.30001 | -50.33198 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d9c0f95-d135-3e59-879c-4ab4be2d5947 | -10.23739 | -47.63945 | 2025-10-30 04:06:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 36c1b2f2-1e61-3a2d-9b23-c7afa25260bd | -10.49471 | -44.14007 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bec0a8a6-a47f-3a80-8e8d-b4a2c2154ae7 | -13.02751 | -48.81346 | 2025-10-30 04:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21de9b1d-9cd0-3ee7-99db-f2a1ae313e5c | -9.81623 | -47.57665 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c050b329-17f6-33e4-aa60-752ef2e32bf1 | -7.92807 | -46.01174 | 2025-10-30 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 834bca20-3d9b-33d9-8e66-617e0f7f3dd5 | -9.71384 | -47.7542 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcb6efee-1d4f-3664-8376-85641112e380 | -11.29231 | -47.54811 | 2025-10-30 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 007b57b4-83ed-308a-9e77-badf50574a59 | -13.14896 | -44.0108 | 2025-10-30 04:06:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8409e23e-a7e8-35fa-99bc-dbebc9e8a3b7 | -12.30062 | -50.32876 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56f8e9f6-61b7-34f1-9632-899f34d9fe61 | -14.28116 | -42.33497 | 2025-10-30 04:06:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2dbecf0-67c4-3563-89d8-24cc4a12bbdd | -13.19872 | -44.48459 | 2025-10-30 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46fe0025-5d4d-3dee-befd-f1c17dd4755f | -10.8586 | -47.86763 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4821f0ff-3ef3-3b46-8208-2d4eb67f2825 | -8.88664 | -49.79377 | 2025-10-30 04:06:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0745234-2460-323a-adc2-751b411e7dd1 | -13.30273 | -47.06264 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d223116-17e9-361a-b1bb-b0e7442e4fd3 | -7.95626 | -46.74852 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 015c5848-238f-3b9b-9116-5258a921d8a9 | -13.65181 | -48.43584 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81da8aaa-19bb-314e-ba97-28f20bee89b9 | -12.03282 | -44.80471 | 2025-10-30 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b9c0054-f258-3343-9e51-790788018457 | -9.89049 | -47.44916 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b6252d1-b900-368b-9689-a5d9116f28ac | -10.93678 | -47.79761 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e66399d1-0cd6-37ac-a33f-53c7ef694ce5 | -10.85096 | -50.1273 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 706c5a3b-bd3d-34a1-ab70-4fbcc24ac888 | -10.7421 | -44.74065 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 891534b2-a2e1-3945-af40-74c0630b6f18 | -13.42561 | -47.36362 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca974ff5-36bc-319b-8e50-67ffd1d7728a | -12.50822 | -50.56235 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ea818167-2be0-3111-afd8-7a65a17c552f | -11.86732 | -46.75217 | 2025-10-30 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2abc14f-6b8e-3c9f-be23-9b5b0a56fc93 | -10.97622 | -50.11444 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6994a85a-255c-3389-9ba8-0da874017d7d | -8.32269 | -47.9271 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4c916aa3-b5fd-31ab-9bda-9c33fce3c03f | -13.27761 | -47.7432 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 712daf0f-2eb0-3d58-a3dc-f9539df11974 | -13.22156 | -47.72758 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c5453c4-ab02-3426-8ab7-7cc7f41bee59 | -9.89128 | -47.44468 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e09eb6f8-36fb-3cf5-b767-9bffa25d0e07 | -13.55004 | -47.12918 | 2025-10-30 04:06:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac302431-49d2-34f5-9dfe-44fad3391f34 | -11.17648 | -47.61487 | 2025-10-30 04:06:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68687bdc-7593-3297-9ad3-47b620a4ef8e | -9.32131 | -43.09209 | 2025-10-30 04:06:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ddb49e8-4663-335d-940b-2e46c74ad8d1 | -10.93299 | -50.20505 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e474d69b-a1dc-3ea0-933d-3e198d540864 | -8.33586 | -46.15385 | 2025-10-30 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 540d7a81-4670-39d4-ae63-ea571983cc18 | -9.22008 | -45.60335 | 2025-10-30 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a19f79c-686e-3853-83cc-a1490bf427ee | -12.51392 | -50.57089 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66902d62-5e17-37f7-8e51-f79a900239be | -13.42281 | -44.06048 | 2025-10-30 04:06:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e02fee34-c493-34ae-a183-60d60cabde32 | -11.17517 | -45.21885 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61855ac8-376c-3586-99a2-05e197392e0e | -10.98488 | -50.21192 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20beafd7-4b96-3f44-91ba-9fd4d595d981 | -13.27267 | -47.72165 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f241c33-d2b4-35e4-a5e3-11b64c996c46 | -11.06574 | -50.32329 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd6136d7-6ad0-3bc6-9e94-76a786093564 | -10.85782 | -47.87208 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 803fd332-1245-3998-bddb-3fcf22fe5419 | -13.88494 | -43.93175 | 2025-10-30 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1239c84c-abf5-38f6-ad6d-2d2905657af5 | -13.21829 | -47.04718 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12f7d8b1-41c5-3524-b922-2c2e07ca2d0b | -11.38809 | -46.03893 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faa9cdf1-7bf2-3494-b3a2-fc4586ef54b7 | -12.70967 | -46.29779 | 2025-10-30 04:06:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e2021865-58e2-34ac-a993-cc8aaa447ada | -12.50757 | -50.56565 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83aa82e7-a180-3269-9c99-ee654ba4780b | -7.95489 | -46.73028 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51ff19a3-6653-3f42-b793-d57877b05403 | -10.43333 | -40.50431 | 2025-10-30 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e6e66bb3-b3dc-3ed7-a878-c1740fc98c12 | -12.91851 | -45.05039 | 2025-10-30 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a8dd07e-400d-388a-999b-32d8020aad81 | -9.81024 | -47.58307 | 2025-10-30 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b42c4ae-4312-3f2b-85e3-1c8cb9fa2774 | -13.28203 | -47.71926 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26857fd0-3552-38d5-a018-f65fc7bca1c9 | -12.18692 | -46.70888 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5408b666-488a-39bb-98a1-99cdd85b139f | -7.96233 | -46.7137 | 2025-10-30 04:06:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a18e5555-78dc-39d0-829b-ec75e6b77d10 | -13.17563 | -48.44222 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 910d32a8-273b-37c0-a519-8e84e41aa8d1 | -12.4785 | -50.58432 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f32dcadf-88d1-3ff3-a1f2-ad1327e4d594 | -11.87146 | -46.75296 | 2025-10-30 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e53552a-8723-3b9d-a811-faedfb9e8fb6 | -12.85642 | -48.62036 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d8c5df0-495b-32b1-b693-8e89096068b4 | -13.64818 | -48.43029 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2814690-bf8a-353d-b9cf-0d510ecd45c5 | -13.21895 | -47.04348 | 2025-10-30 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8357cfd-c98b-3388-80d2-b81f4d7a3b47 | -13.16239 | -48.46295 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25e62b84-9512-3eb4-a4e6-1307c44c77ed | -11.94638 | -44.32843 | 2025-10-30 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a73c06aa-d69c-3dc0-be59-6c2af8e13c6f | -10.86463 | -47.62357 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d14876f7-9d63-342e-8f0a-2123f93053c1 | -12.88132 | -48.64084 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f901417d-52ca-3d20-a246-54de9557f630 | -10.87624 | -48.00324 | 2025-10-30 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d1df7bf-e442-3848-8efd-582cd2e3967b | -10.86543 | -47.61903 | 2025-10-30 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9d97c76-0cb1-3bbd-9b72-2b16e9088a83 | -13.43394 | -47.36555 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94856499-75ea-32fc-90d1-491db6d926d0 | -11.16592 | -45.227 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05b7e7f1-a4d8-36e6-9907-a98473f15335 | -10.33687 | -47.0932 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a51f5fb7-2f46-3cd3-b34f-b7c592d9cd26 | -10.88312 | -45.07344 | 2025-10-30 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f0e63364-63c2-3599-b944-47a75204c88a | -13.9536 | -44.18978 | 2025-10-30 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f70812ec-88da-30d4-b32b-9c9e8b758c9f | -13.47829 | -48.00071 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9b358cd-6a0f-3c0f-9241-b6bfd61d0ca2 | -12.49222 | -50.56988 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d995fa3f-58f2-3486-ab84-e8bc94a2303e | -13.05939 | -48.46168 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae8b2303-0efa-3323-990f-5afcb9c1b683 | -11.0056 | -41.6777 | 2025-10-30 04:06:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b0e750d-77aa-3acd-bf52-736cd0c6fd75 | -12.6041 | -43.19893 | 2025-10-30 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cfa5025-a273-3bd7-a755-b489e94fafb8 | -10.74892 | -44.74852 | 2025-10-30 04:06:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80f599fd-d231-3e51-8c22-aa559ce0d1d8 | -13.34928 | -47.66746 | 2025-10-30 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 254b1367-7ba5-3dd7-86f6-4d427b7fe9a1 | -10.4501 | -44.3168 | 2025-10-30 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0da0564-0b16-3fe0-a511-8542e9b012dd | -13.39928 | -48.37865 | 2025-10-30 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66dcea9b-2aa8-3e01-841a-5ec09a4dc90a | -12.88227 | -48.63559 | 2025-10-30 04:06:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06386153-8ddc-321c-a9a4-a09a2378d51b | -13.43394 | -47.36557 | 2025-10-30 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc0e799c-9efa-31c7-8176-defe0da6f2dc | -10.9743 | -50.20984 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4665ff25-5d43-3282-b9d9-a0323fd39ce5 | -12.48568 | -50.57543 | 2025-10-30 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 74736059-2a23-3cca-a1f0-a488b147a0d9 | -10.98882 | -47.87626 | 2025-10-30 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aa4ba96-b9dd-3e1e-86f2-1d256c2b6bb3 | -8.33646 | -46.15513 | 2025-10-30 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 020ac076-e684-3c7e-89d9-6fc22dedc32c | -9.89314 | -44.93197 | 2025-10-30 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0f9de79-ae8d-3f49-8229-32df9aaad755 | -10.64928 | -48.79323 | 2025-10-30 04:06:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3c83ae8-aef0-3c22-a5d8-a67a19772e6a | -10.01001 | -48.22929 | 2025-10-30 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 335b0e99-c897-369c-b665-31bd1c33afac | -13.16339 | -48.45757 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71938ba5-1590-3161-8339-e9da797a537d | -9.33278 | -46.29592 | 2025-10-30 04:06:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4795a0d-b30c-3382-8b60-1bef8ba3e7c3 | -12.62105 | -44.25028 | 2025-10-30 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f678438d-15a3-337e-9369-1e6911e732a6 | -14.53462 | -43.78687 | 2025-10-30 04:06:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ced675f-0873-39f7-93cb-58f687d1d415 | -8.33219 | -47.92895 | 2025-10-30 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65f74103-deea-35ea-8233-0e3102ac8465 | -11.10119 | -44.70337 | 2025-10-30 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1b17ec0-0c83-383f-8663-03142331a536 | -13.80631 | -43.75149 | 2025-10-30 04:06:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8d4f6f6-d97a-3df9-8e33-bada69453311 | -10.97302 | -50.21649 | 2025-10-30 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d540d3fe-32de-3d94-a41a-bead6c4e817b | -13.07297 | -48.21383 | 2025-10-30 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1112de2c-06b8-3727-a4f9-0eec75a75bfe | -10.33308 | -47.09034 | 2025-10-30 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README34.md)
