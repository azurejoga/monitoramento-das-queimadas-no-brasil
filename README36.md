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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3016343-fd90-3c5a-b8f9-e715966359c1 | -12.03308 | -45.19197 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da7528f7-fb15-3ba9-b38d-e12a1fe4b980 | -14.88876 | -48.35236 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5865f58-2912-3091-9f96-f07bb7be6170 | -11.9096 | -46.35365 | 2025-10-04 03:53:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 907caa2f-5c9e-3189-a6d8-0281df033312 | -15.66585 | -48.14486 | 2025-10-04 03:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c467ac6-0096-30e9-9a33-65ccb922d4e1 | -13.68428 | -48.61449 | 2025-10-04 03:53:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 744f7513-3891-317d-bf66-e4cd97ce23c8 | -12.88684 | -47.16933 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da414843-85e4-3de4-b909-efaf3a67c677 | -13.66115 | -47.87205 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a65f298e-b802-3c6d-8585-8350f3bb15e1 | -11.78671 | -46.82346 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbf726aa-d809-3e09-b80a-b4333f364035 | -13.73442 | -47.9225 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57106d64-d0f3-3806-a903-68c75eb8a971 | -11.78414 | -46.8373 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59328607-f50e-3ce1-b0a1-6db62619fe42 | -13.74306 | -48.08851 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2e89cc4-5587-3ad4-8cac-7dfda92656d9 | -11.87552 | -44.97495 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 044cfc26-780b-3adb-8465-f28acc8f875f | -13.28583 | -46.98196 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5209aaf6-be5e-3b49-ae7f-f2f862d95193 | -13.10342 | -47.87878 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8f87cf7-99f3-31a9-863e-42cc67b5d580 | -14.44645 | -46.11889 | 2025-10-04 03:53:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e93e5ea1-82ba-3d4c-9646-646903a14fcf | -13.29418 | -47.59876 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e08fd17-33c2-3730-b053-12af59ed4111 | -14.85204 | -48.28562 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 425536ed-6927-3d0c-a7be-b268803a5e41 | -13.52459 | -47.30335 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cd7c9da-b6ee-36b6-a0f2-f828e3a749ab | -11.69915 | -47.51012 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 252fc948-dea6-3296-a930-4d990e2ae6f1 | -12.37391 | -46.51135 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 747ebd4b-da10-3bb3-b697-8ab7106e6135 | -14.9649 | -47.26963 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ad1bdb54-c0f0-3068-98b9-4305357da44c | -12.95395 | -42.42518 | 2025-10-04 03:53:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4abb5d20-557d-36f2-b03c-761999f22e7d | -11.87101 | -44.9739 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b6bab72-ef06-3fea-b433-447b2a0b663a | -14.69132 | -48.09464 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81a4292b-0e9d-3f3d-8c4c-d4e866fe4c84 | -13.32539 | -47.18829 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 601f3224-b7da-34ca-984c-682ed4904939 | -14.6555 | -48.244 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf79ca82-7571-38e3-a2c5-ada4218b09c5 | -14.98271 | -49.96783 | 2025-10-04 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d7b51d6-f6f3-33eb-9c47-88b76e6a4a6b | -12.81674 | -46.85759 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14a34601-1502-3799-88f0-b1a8db219f0b | -16.09038 | -51.06967 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee4be012-73ee-3ace-8908-1d715838c391 | -15.31134 | -46.27613 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e8fc978-581d-3a00-bf21-9351aae5646f | -13.74654 | -47.93124 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19e930e5-0af8-34ed-9436-395196ba25ed | -17.07669 | -43.36003 | 2025-10-04 03:53:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 245a743b-364e-304c-9f5c-307fd822093e | -15.76172 | -47.77523 | 2025-10-04 03:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 818d2339-a4a8-370f-8df6-526875a5b834 | -14.8895 | -48.34868 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8bf9bd6-8399-3cda-8160-26c7e377e148 | -12.37277 | -46.51179 | 2025-10-04 03:53:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21a82711-742f-3e4c-b90d-e4341ad4994b | -13.99873 | -48.20377 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45a8fcc1-8418-3c46-a3f4-b226f6342c21 | -12.19642 | -47.78154 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cb0a0d0-535f-33e4-8d2c-de64baaf56b7 | -13.74103 | -47.95875 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 440dea28-b8c7-3799-bc12-011e918a1ba7 | -13.31884 | -47.25063 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecd0ea63-1d80-3eac-94ac-afe1bed9d2f9 | -13.52509 | -47.27264 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb7a42d7-8684-36eb-a928-8fbd965bcdba | -14.93036 | -46.89535 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e8b67c93-df6d-3834-b0e6-f1d692795cc0 | -11.78159 | -46.8223 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c82495b7-d5ca-3f07-8985-17981792f194 | -13.32961 | -48.11034 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cf44e05-8976-32e7-ba11-4986b8841e6f | -13.39578 | -47.54953 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9572b2a-79bc-31e9-a354-cc0328500492 | -16.35281 | -43.41789 | 2025-10-04 03:53:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdfbe696-c8e5-3c81-b27c-23d15713d241 | -12.95477 | -42.42045 | 2025-10-04 03:53:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2ae8322d-8000-3f8d-8947-7e58cea55ec8 | -11.88294 | -44.98587 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a411309d-cd16-33ad-86ea-bd9dd21bd36b | -17.58048 | -44.49041 | 2025-10-04 03:53:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a5b6b9d-d3d7-3f12-853a-3dd180b75d71 | -11.53859 | -47.66453 | 2025-10-04 03:53:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 374bc44b-fe1a-33f9-9f68-76a9cec2d81c | -14.63133 | -48.24509 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be54dbf5-ac97-38ce-bb8d-d8bc688f86ad | -15.28296 | -47.14773 | 2025-10-04 03:53:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 741527f1-551f-3e8b-b47a-9157910a7707 | -13.58247 | -48.18068 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d8077d1-8aa8-36c5-95e3-d6d98c2fee0b | -12.72277 | -48.574 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6a59969-9461-32ff-afb9-a9e2913b5eed | -16.00977 | -50.92604 | 2025-10-04 03:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 704e8667-313e-3451-9ba6-8a706da05338 | -12.64258 | -46.98278 | 2025-10-04 03:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d1b4ad76-9c51-3752-9be7-71dfbef0b8ab | -14.66536 | -48.30574 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| aa92199d-639c-3249-a9f3-e1940e513e6f | -15.53374 | -46.83733 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a86f0f27-6bcf-38f3-a558-82571cfa8a15 | -13.33171 | -50.94534 | 2025-10-04 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1a4f525-010d-3dd4-a4bb-4a56507b87b1 | -15.3481 | -46.29762 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42130e6d-57f7-34d7-8eeb-3e3a868a155e | -13.74379 | -48.08485 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d696c1c-b3bc-3b15-8e33-627f33b0c9fa | -12.0322 | -45.19676 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f90a25fb-6328-3613-9393-ecb26f554135 | -15.31039 | -46.28108 | 2025-10-04 03:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d37784d-2500-3053-8da1-f057a9f23b26 | -17.27734 | -48.31229 | 2025-10-04 03:53:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 793949ab-48c2-3088-8e3d-086db3831c0b | -13.40577 | -43.68803 | 2025-10-04 03:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 914444c6-1471-35d4-8b52-8d6db190c35d | -12.0759 | -45.16571 | 2025-10-04 03:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea9e47c7-6463-3ada-afab-1083a92c02b7 | -11.85999 | -44.95702 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa1fc5cc-44ca-3fee-a9d6-021a9a5c294f | -15.5347 | -46.83237 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b171ecb2-bfe7-34d1-b24a-a4f5ceb90bb0 | -12.41098 | -45.15704 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcf74225-5c0b-3def-9dcc-2720fa4ab408 | -17.55393 | -46.76162 | 2025-10-04 03:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6a8e70d-ca97-32c9-b429-456081991b86 | -12.99331 | -47.77691 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71633778-d9a5-3284-8bd7-d91624fa8bea | -14.64335 | -48.30379 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86d399fc-8da4-3729-92de-7d5da6891631 | -13.52536 | -47.24343 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab0fa28d-e4a0-3b42-91a7-b005a9901bb9 | -13.28645 | -47.83563 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 706c0cd8-d7e9-3eed-8074-fc1fa1f04707 | -15.34648 | -47.8225 | 2025-10-04 03:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95380aa1-5d94-3946-b94d-17d00ef1c245 | -12.93037 | -45.06935 | 2025-10-04 03:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e978f2b-9d30-3f0e-ae69-9f106d75681a | -13.74446 | -48.08145 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac66042d-fce5-362c-a208-cbde63e0e4a4 | -13.34891 | -48.06963 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1919ed1-d92c-34c1-97df-c086e036fe1c | -17.07913 | -46.24548 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a377fbc2-534a-3bcf-997b-144e716614fe | -11.25405 | -47.7924 | 2025-10-04 03:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8cd491e-d194-34be-87cd-74cc7d14c537 | -14.93664 | -46.86337 | 2025-10-04 03:53:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eb306de7-8bb4-3bae-81f6-a23fa40d4c9a | -13.98805 | -48.2009 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58c2950d-1773-3f12-84ae-0c11d4f955ae | -14.66163 | -48.29644 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| edf2ed85-54e4-35d0-9cc7-b0c2badeafc4 | -11.88209 | -45.01662 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e95ec973-d410-3497-ac8e-4e9cdc8efad0 | -13.26294 | -47.20798 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb590c46-821a-3f36-adf0-10055376a462 | -13.5477 | -47.24467 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37d0de72-f48f-3388-b8c0-cc21bc25cc7a | -11.80676 | -45.04118 | 2025-10-04 03:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e0a9f25-3fb1-3cf9-8ef3-7847b56d748b | -13.12899 | -47.91932 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0838f3e-afcb-36b1-a55c-99ddd605da09 | -13.92788 | -48.16018 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 213eddba-3456-386a-a71e-073eea9792c9 | -16.08317 | -51.0728 | 2025-10-04 03:53:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 54d34ecf-979d-30b4-a33d-a85a65110063 | -14.60295 | -46.73109 | 2025-10-04 03:53:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d60a357-475d-3c21-8fcb-aac96c039252 | -13.10617 | -47.8931 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 803b356e-c418-31a5-9ec9-be569d5711f9 | -13.63829 | -48.6699 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63dbaaa0-e021-32c3-84f1-890772bdb80e | -11.7872 | -46.82821 | 2025-10-04 03:53:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f20e7096-5de5-334d-8f6a-6cdb4ff06cf1 | -13.1417 | -47.94031 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c57e8649-8e49-3845-9a96-608a30814763 | -12.71448 | -48.55627 | 2025-10-04 03:53:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b36d7931-f72a-3830-8169-a32f4a2b41cf | -13.31219 | -48.14119 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2dc805e-18a7-3e9c-9ba8-0a72562e1893 | -11.55361 | -47.6748 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aabd1b7a-3751-3716-b120-7e54e3964ee1 | -12.22147 | -43.7725 | 2025-10-04 03:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ef3628c-c0da-387e-a3fd-86b031315e83 | -16.35629 | -51.47632 | 2025-10-04 03:53:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d6a8304-fbc0-30da-a494-4e643943b277 | -15.71843 | -46.28799 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README37.md)
