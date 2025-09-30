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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4b60c52-86db-3363-9e88-e9258e2aa9f4 | -10.19317 | -44.90102 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fcb2cfcb-ffb2-344c-aa47-ea44ea2cd0d1 | -11.86715 | -41.50343 | 2025-09-30 03:47:00 | NOAA-20 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80c9fdfc-85ad-35f0-a802-4089f1312916 | -5.27952 | -43.16764 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db8afc07-d533-3406-87b2-ea26c1e4059d | -9.03837 | -46.70136 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3a9f608-da61-3434-88ea-8a9b64fc2006 | -4.25758 | -48.55715 | 2025-09-30 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dab155b-a86a-339b-beb6-505490b5dc7a | -10.18762 | -44.90507 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| fa537499-528b-34fe-bd50-4b807027a164 | -10.95031 | -44.31954 | 2025-09-30 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24c235e5-7d87-3922-955a-afb7d1612971 | -9.44693 | -50.9076 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2e374be-9b49-3f93-9da6-6bf107b5fb5e | -8.66897 | -47.72009 | 2025-09-30 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 780628db-31f2-3ae3-8bbb-463b06a997a9 | -9.31669 | -50.63477 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fa7a6c7-75ed-3894-8027-455596d7ddf6 | -3.81386 | -47.57818 | 2025-09-30 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc19b8d6-4954-32dd-a6d0-1510b62f98fa | -10.83988 | -45.41784 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a14a3dc8-9125-359f-a80f-bf70242921e3 | -7.9247 | -48.18863 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81a218b6-9c9f-3b05-8b2c-4fe782f65e82 | -4.25658 | -48.56295 | 2025-09-30 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56f27975-e743-3f0c-9781-17d52844ce13 | -11.68089 | -44.30394 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17a7144f-5da8-3e04-a8e8-2fd7112a6eb5 | -9.27401 | -45.70031 | 2025-09-30 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea86e908-8fb5-311e-a153-d6955daf3171 | -9.30075 | -47.373 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5422b1e9-6b86-3519-bc9b-ddd6cccee028 | -5.10429 | -43.06963 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c256335-6e8a-350c-a01d-d6482b5982b0 | -8.54234 | -44.66493 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70fbd876-c7cf-33ea-98d0-728b77483fac | -11.51148 | -43.5407 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28989520-c818-3626-9dde-59bc2c3422e5 | -8.32751 | -46.21648 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1f1eb67-60b1-3f1b-aa3b-076ea312d583 | -8.26764 | -45.50767 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 643b5f80-dda4-3f16-841a-81c11bbf72c5 | -10.08778 | -46.07291 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fbe3ac7-e2c7-3618-9007-32fed6e05591 | -9.88588 | -45.95536 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 857d1da6-df58-3c3c-a879-08b94bf403c9 | -10.08571 | -50.21734 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b6b9089b-bf1c-39e3-b598-37dad67b5a6b | -11.46195 | -44.99401 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5967c440-27a3-3899-9b5f-708f2e560f87 | -9.984 | -45.41541 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32ca5fa5-9676-3f85-beb2-998363495eb4 | -8.5396 | -44.6803 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5483eb2-1b0d-3350-85f4-e15a6db7fcfe | -8.32689 | -46.21983 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ae90433-2d50-3aeb-bfc3-1ba7d7459473 | -8.14376 | -46.37026 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2022f49-5777-38e4-bb3e-692a0e6f908b | -9.75246 | -47.19983 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cc659d4-613f-388d-a1dd-b0ce4d03e13c | -10.8453 | -47.96616 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d0de5bb-0872-3384-9e5e-8910bafe147f | -8.00791 | -47.0542 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c0d6c9db-ac77-3e65-b18f-e1092896d9d5 | -10.1885 | -44.90007 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a88b89e7-30a1-3ba4-85cb-af7db96fd25a | -10.86988 | -41.61724 | 2025-09-30 03:47:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40912636-6bb7-3d77-8f94-b3b4a7eb8c70 | -11.67446 | -44.2893 | 2025-09-30 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7749b5a0-df89-3c7c-bad4-dc2e491e5090 | -3.42393 | -39.34391 | 2025-09-30 03:47:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9db831a1-a125-3380-ae6d-ff4318fe3f27 | -10.42745 | -46.15194 | 2025-09-30 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb2f73f4-9c92-32a0-9d74-e712c75f55db | -11.40452 | -44.89694 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0748b35-af03-308c-9648-c8a83eeb501b | -7.91041 | -44.62003 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 192d0de4-14b2-301c-b277-781be3b07bc8 | -7.75508 | -45.77295 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61e07975-8965-3e20-af94-ed19154928dd | -5.02355 | -42.98868 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4baa3e25-39ea-3806-a108-ddbcb86545b4 | -9.75862 | -47.19727 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97527a49-83d7-348a-8dbc-46a6adaeddf5 | -4.15472 | -39.13311 | 2025-09-30 03:47:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1f05ad4-456f-39c5-870b-39f601baa360 | -10.39447 | -49.04089 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8983debc-33a6-3bb9-8e1e-403714116652 | -7.91515 | -44.62108 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32860259-f9ee-3cc4-a4b7-0e717adc9849 | -10.18728 | -44.89218 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 029aa934-689a-34e1-b77b-f92666b29e47 | -7.50147 | -46.12737 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9613ce3c-66ea-3afb-8be6-1249484261e7 | -2.80438 | -41.79884 | 2025-09-30 03:47:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a67d66ec-5185-39b0-9e02-b8d5c911171f | -10.65439 | -48.55069 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e77c1099-28a0-3b01-8d18-429384aeebee | -11.45783 | -44.99533 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff22fc26-27dd-3ae5-839b-5ed6fcbbdf6e | -4.39509 | -44.08071 | 2025-09-30 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6e35f71a-8719-3298-9f39-08369669cf13 | -4.39248 | -44.39579 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f06e07-d9ae-311f-b7e7-778be71fff2c | -9.95337 | -43.58441 | 2025-09-30 03:47:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01a7ddae-b55a-3301-8cee-5cdf72265304 | -7.82513 | -47.00168 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b630e7f-ef18-3150-8d3a-26a37b8ce66a | -11.44651 | -44.97895 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3058b72c-e61b-3502-a52a-731b7ac0b844 | -8.14248 | -46.37737 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c8ea9dc-ab2b-3de5-8a47-104431a514db | -3.82415 | -40.47492 | 2025-09-30 03:47:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7487cdc2-d3d4-3d30-b024-672098d48d1e | -3.60579 | -41.37675 | 2025-09-30 03:47:00 | NOAA-20 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fdbcb116-b861-354e-91fd-59caeed56669 | -4.66726 | -45.69172 | 2025-09-30 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac21395d-9e9a-3af8-a13e-ed2e592f8244 | -7.83419 | -47.01569 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74ab4e7e-3585-3603-8b2b-856e069abf15 | -8.65403 | -43.98132 | 2025-09-30 03:47:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e0c299f-1861-3a7b-8688-736ac1b0ab46 | -7.91433 | -44.62578 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ff1a519-7162-338a-84ee-5de01be5193d | -9.32297 | -50.63419 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8f51f369-3165-3675-be2a-9f78994cf7aa | -11.43213 | -43.50188 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64e13ace-3b5f-36e7-bd5d-ce91389f6f13 | -4.79356 | -40.54461 | 2025-09-30 03:47:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 578889b9-56c2-3492-a0f4-afc1cbb12068 | -10.63847 | -48.5697 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cde44023-a525-3612-aa4f-a4d0fab053cb | -9.75237 | -47.20043 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fb1dfc3-a480-3abd-b918-137d388b88e6 | -9.98642 | -45.4169 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f509709-8eb3-305c-84ae-21c468131dfc | -8.70949 | -47.98319 | 2025-09-30 03:47:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21299d76-b30a-39ef-8599-9006500f40f1 | -7.47252 | -47.26879 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71c2f241-9868-3052-8f39-e9a788645418 | -10.83895 | -47.96863 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 438cdb8b-33e0-3485-a42c-a7e337cf947e | -5.49321 | -37.37748 | 2025-09-30 03:47:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66cfc5d1-f664-3a41-848a-4dcb059146b8 | -5.40446 | -37.70426 | 2025-09-30 03:47:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8d615b5a-9a1d-33ed-a924-a4eb425ee304 | -7.82654 | -46.9939 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bb64dab-9137-3e4f-9aaa-8e67e3782857 | -5.50221 | -42.74828 | 2025-09-30 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a5991545-adb9-3f57-8d9f-e2a264f33f9f | -4.39321 | -44.39148 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18109c18-0be2-34a7-bc58-c2c9b0f1cb1a | -3.86138 | -40.44121 | 2025-09-30 03:47:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d27dd1d-79e1-345a-ae5c-17937c7943a4 | -3.85358 | -48.98085 | 2025-09-30 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 96ae7600-12dc-3ff7-adef-12029168b2df | -8.96611 | -47.44858 | 2025-09-30 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbb2923b-4b51-38c2-9434-7be08d6bd53c | -9.93198 | -47.458 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72188073-cc36-3fec-8119-066c38577519 | -10.94959 | -46.48175 | 2025-09-30 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0247b0a-11da-3f4f-991b-7b6d1c33ff67 | -2.43981 | -47.33394 | 2025-09-30 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e79a97a-3816-33f7-8b17-82e7145bc86d | -10.63408 | -48.59232 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e37975e0-2362-3b12-b2cb-f96ccafd7b79 | -11.45108 | -45.05204 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2a250f5f-03e2-30ba-b4ee-e472b12cacbf | -4.35207 | -45.58138 | 2025-09-30 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8783e224-3328-3f31-82f8-89d5a65257d1 | -11.41837 | -44.89886 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7858db5e-ab97-32db-b545-71be61aa2e71 | -10.19284 | -44.88821 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2aeec042-c4ee-37eb-845f-761087a562b8 | -8.23175 | -45.50454 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8765c59a-fa04-3f04-8d05-aa3d79c825f2 | -10.87 | -41.61967 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 42eac6fd-3997-318a-89cb-85f82bfe46db | -7.86845 | -47.25976 | 2025-09-30 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c40c61d-7649-3ff6-aac7-4aea1250749a | -5.28035 | -43.17072 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 325f5c86-3dcc-37f5-aa7f-265db6930220 | -4.64185 | -47.95982 | 2025-09-30 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dda71b4-810e-3874-92e0-4c27bdd51154 | -11.45195 | -45.05463 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0310b124-7949-339e-9725-01c48fa4afa6 | -8.25025 | -45.54604 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 652a7a97-76a0-3b5c-8146-665c5f2f1222 | -7.51758 | -46.69402 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f6584f4-a177-385d-884b-97579ce01c86 | -10.18819 | -44.88725 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| af8b81ca-3b9f-3eb7-a05f-2e481fa45553 | -10.19012 | -44.90301 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| a5ca723c-9334-32a7-9789-c466e01aa596 | -10.17443 | -44.89767 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1ce1103-0edc-3c94-9bf6-d501d1bd33c8 | -4.86426 | -45.05437 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README27.md)
