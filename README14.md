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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d815445-40d2-3baa-91f8-b60aaf50c5dc | -10.9506 | -44.630001 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62b97cf5-3d39-3e74-af11-b546a53d53b9 | -10.9533 | -44.641201 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 292ac65a-f4a5-3ccd-a054-5eecdf6f67e3 | -10.9436 | -44.6436 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 69ee2250-adf0-306f-84b9-1a6fd844c3ad | -10.9464 | -44.654701 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8431656d-c58c-31ea-b26d-6fdf06aa3fc8 | -10.9491 | -44.665798 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2e2633a-0fe6-3d07-9e11-dd0e9f15134c | -10.9338 | -44.646099 | 2024-10-13 00:57:35 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c79be27-d921-34fc-8fc0-2b027d4afbf7 | -10.9366 | -44.6572 | 2024-10-13 00:57:35 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f3ac019-1ded-38e7-bda4-38f00e2bda1b | -10.9393 | -44.668301 | 2024-10-13 00:57:35 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b71b726-c554-342e-b7cd-464a90e42790 | -10.9421 | -44.679401 | 2024-10-13 00:57:35 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9aacb72-c7b1-38e7-8ada-662f761b4073 | -10.9269 | -44.659599 | 2024-10-13 00:57:35 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7001766f-0039-3608-8421-7790ebc78aec | -10.9296 | -44.6707 | 2024-10-13 00:57:35 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d1c615c-6fcc-36af-82cc-a24ca48d5c4a | -10.9324 | -44.681801 | 2024-10-13 00:57:35 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7699abaf-2cf7-371c-9360-aec94f49ea29 | -11.7398 | -48.3573 | 2024-10-13 00:57:36 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb62f7ab-dd61-36f4-8225-cfbaeb0fb1ee | -11.7415 | -48.364601 | 2024-10-13 00:57:36 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88324be8-0a59-32c9-aaae-1274b7c6d87a | -11.7432 | -48.371899 | 2024-10-13 00:57:36 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e184260-fc49-38a6-b1f7-bd397fa1806c | -12.1811 | -50.703899 | 2024-10-13 00:57:37 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c3ee2c9-d399-3e0e-9681-3dbe605962f6 | -12.1827 | -50.710999 | 2024-10-13 00:57:37 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e806f36-0d35-35d8-8d8a-51579e4a918e | -10.7182 | -44.4842 | 2024-10-13 00:57:37 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97956b13-6324-3992-8b48-d763bc305d4f | -10.7057 | -44.475101 | 2024-10-13 00:57:38 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd54a3b-0913-3040-b622-dc97caaf001e | -10.7085 | -44.486599 | 2024-10-13 00:57:38 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7bfb0a43-93fa-371f-8c5b-636309ac4d0b | -11.6402 | -48.3731 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4aab14f-d6b4-36e0-9d9a-ea1334847606 | -11.6419 | -48.380402 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 753d9e2e-cd2b-3250-a12a-5366f7f7ffa3 | -11.627 | -48.360901 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee2f3748-0fde-330d-87a3-d879b8669310 | -11.6287 | -48.368198 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 481115da-c9c3-3e07-bd49-51dd36548851 | -11.6304 | -48.375401 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 781c0da3-9e66-362a-ae94-93a67f51bdca | -11.6321 | -48.382702 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1dbbad58-7e87-34c0-ad4e-4a34b9cae44a | -11.6338 | -48.389999 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b30551f5-2001-3571-b3fc-81f6d2caa852 | -11.6189 | -48.370499 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd3b593-ad1a-3442-a6a6-c5353afa721e | -11.6206 | -48.377701 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb77b9f-1a82-3bf1-8049-dd1fcd0386bf | -11.6223 | -48.384998 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2de21d56-0ea3-320d-98cb-33390ecc646c | -11.624 | -48.3923 | 2024-10-13 00:57:38 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d045308-3fc6-3126-9a11-c3096bc4af19 | -11.5919 | -48.476501 | 2024-10-13 00:57:39 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 503ef990-fed6-3763-8ef1-400830c977b8 | -11.5936 | -48.4837 | 2024-10-13 00:57:39 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f502f2c-9f5d-3491-b95b-603f4d200d0a | -11.5902 | -48.469299 | 2024-10-13 00:57:39 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca1d4bfd-ed37-3081-9e31-0c58b4b17f9e | -11.6634 | -49.054501 | 2024-10-13 00:57:40 | METOP-C | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a16d554-82fc-3e78-8813-b8a3e6c2bde8 | -11.665 | -49.061501 | 2024-10-13 00:57:40 | METOP-C | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3b42927-0042-3463-a657-cc077d02c337 | -11.4962 | -48.598 | 2024-10-13 00:57:41 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 972f31a4-a3f8-33c4-aee1-1ffac609b4cf | -11.4946 | -48.590801 | 2024-10-13 00:57:41 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e38d1b77-ed37-37f0-a6b9-0af9a517df80 | -12.0052 | -50.930599 | 2024-10-13 00:57:41 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d9d5663-a340-3df9-94ce-97cfbd672495 | -11.2062 | -47.8409 | 2024-10-13 00:57:43 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d835317-1484-3cc2-a52b-589e94aa9b68 | -11.208 | -47.848499 | 2024-10-13 00:57:43 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7db71d83-5f0e-3b88-9b02-cbb90d1ecf1a | -10.4486 | -44.942001 | 2024-10-13 00:57:44 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d2345ac8-bcc1-385d-84f9-a1ae27b04925 | -13.7256 | -60.563499 | 2024-10-13 00:57:45 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0619417-9207-3481-ad45-0bbeccbff17f | -13.716 | -60.5653 | 2024-10-13 00:57:45 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0458660-2734-3031-b551-cea289f141fa | -13.721 | -60.592701 | 2024-10-13 00:57:45 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7321265-5179-36ee-9923-1f085aa405f0 | -13.7113 | -60.594398 | 2024-10-13 00:57:45 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2f5540d-31dc-3825-8aab-b4d830ec51bd | -10.3317 | -44.971001 | 2024-10-13 00:57:46 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 412cb06e-1556-3474-8ff5-8aa9ca335977 | -10.3219 | -44.9734 | 2024-10-13 00:57:46 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7d756822-b8e7-39c0-9de2-4ed6d91704ee | -10.0618 | -44.1698 | 2024-10-13 00:57:47 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bdd022fb-8360-378d-a82c-4ef7f796bb90 | -10.6299 | -48.0256 | 2024-10-13 00:57:53 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2432893-12eb-3e8a-ad80-d0a62c40d034 | -10.6317 | -48.033199 | 2024-10-13 00:57:53 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e76453ed-e1b1-3b8b-b120-26c5a55f031e | -11.2611 | -50.778801 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26de59c5-1dcd-3002-b796-a4a1eadbe948 | -11.2627 | -50.785801 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1fb2f98-e816-3d79-84e5-93bfb461d413 | -11.2683 | -50.903 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edace839-7f8a-3e5c-bd13-54ee033d5f4f | -11.2699 | -50.910099 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc5dd44-8131-3592-92dc-6abe7e54e185 | -11.2715 | -50.917198 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d88b9975-1674-3d65-99c5-f162540e9a49 | -11.2778 | -50.945499 | 2024-10-13 00:57:53 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ab06d68-2b7d-3c47-a3ad-b2caa2d7ea5e | -11.257 | -50.898201 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b97aee09-a75b-3b2f-95c0-17daa31950d2 | -11.2585 | -50.9053 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0dfe9497-963e-3527-937c-23d897929967 | -11.2601 | -50.912399 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06b9bde4-7a78-350f-a4b1-42bdafd7f617 | -11.2617 | -50.919399 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22c57391-3a73-3bff-b190-5a4628ffee3c | -11.2681 | -50.947701 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1263f3af-762f-3fc9-b49f-61dc8fc52ef9 | -11.2519 | -50.9216 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8bef6ab-09f0-32d6-b710-b97353302b9d | -11.2535 | -50.928699 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 269454c0-7127-3378-b302-5af23295c81c | -11.2551 | -50.935799 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f102c9d7-3bad-32e1-a363-385d64a9e2f4 | -11.2567 | -50.942902 | 2024-10-13 00:57:53 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c95b0103-2813-3e8b-a74c-9286efdc7a94 | -10.6827 | -49.007099 | 2024-10-13 00:57:55 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7295da2-179b-3cfd-ab9c-9220816a1ab8 | -10.9167 | -49.8022 | 2024-10-13 00:57:55 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e9a42c6-cf60-31f7-a2b3-1239fc696919 | -13.3639 | -61.976398 | 2024-10-13 00:57:55 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 61b60f1f-de5e-3dea-9d9a-5dc372c5ce11 | -9.5658 | -44.460999 | 2024-10-13 00:57:56 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| acd5763d-ca01-3317-9a12-fc7ec2fb2907 | -9.5561 | -44.463402 | 2024-10-13 00:57:56 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46bfc3bd-b445-3765-b0cd-ad62cfec7204 | -9.5591 | -44.475399 | 2024-10-13 00:57:56 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36e884e5-3dee-3a41-bfba-c2a10569fb85 | -9.445 | -44.139 | 2024-10-13 00:57:57 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7fc96772-6a11-35e4-a678-4cacb3d598e0 | -9.4352 | -44.141399 | 2024-10-13 00:57:57 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df01518d-8bc2-3237-9b06-ceb0003be33b | -10.5196 | -49.1049 | 2024-10-13 00:57:58 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd36d1c8-fccf-3383-9be1-9ad99c987232 | -10.6374 | -49.888302 | 2024-10-13 00:57:59 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d3ce941-4db6-3e84-acdb-9398745f9bc5 | -10.1683 | -48.038799 | 2024-10-13 00:58:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21acdc36-d1df-3074-8414-ae79339dfa14 | -10.3245 | -48.7966 | 2024-10-13 00:58:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 247c212f-18f8-39c0-bbd7-d3c898777656 | -9.9452 | -47.267899 | 2024-10-13 00:58:01 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e446ca6e-c976-363b-a0cc-77272338b8ce | -9.9472 | -47.2761 | 2024-10-13 00:58:01 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3a037d-c5bc-31c3-b4cb-70b850eb57e6 | -10.5571 | -49.943298 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c7b73ae-e434-3fe8-abae-41f2041cfff7 | -10.5587 | -49.950199 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bef81e0-5296-3db1-b3b5-792c5781c9bd | -10.8151 | -51.131699 | 2024-10-13 00:58:01 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5b8c762-5aa5-332b-8a18-41d477733781 | -10.8167 | -51.138802 | 2024-10-13 00:58:01 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e59ede9-ff66-38b3-acf2-95631d82559f | -10.536 | -49.9408 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3afa022c-ddbc-30f9-a935-7d67c4414caa | -10.5375 | -49.9478 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7789b18c-754c-3f83-b27c-38a94dd04d00 | -10.5277 | -49.950001 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc110651-68e3-30d8-95b8-9d2b6636b285 | -10.5293 | -49.956902 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbd42e57-4774-3cbf-ad63-3104c450e589 | -10.5309 | -49.963902 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62bbf4ce-8381-3ead-83c1-89752bafe8d3 | -10.5356 | -49.984699 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bdec2d5f-b4ac-39a7-8be5-66ace3ad6b65 | -10.5372 | -49.9916 | 2024-10-13 00:58:01 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c97ac5d1-6c8c-33d9-a2cd-0b958ced38d4 | -9.827 | -46.9879 | 2024-10-13 00:58:02 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47803565-6f09-362b-9ad6-04c8452fbbe1 | -9.829 | -46.996399 | 2024-10-13 00:58:02 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bada057f-2a9c-377f-ba1c-88f3510154e5 | -10.5211 | -49.966099 | 2024-10-13 00:58:02 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de40e641-a465-32c1-bb8b-2cd2cdf474b4 | -10.5227 | -49.973099 | 2024-10-13 00:58:02 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df96932a-f10f-3895-a966-173166d56b91 | -10.5243 | -49.98 | 2024-10-13 00:58:02 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b722de70-89b0-371a-a62f-2f913e352649 | -10.4854 | -49.945099 | 2024-10-13 00:58:02 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90f62d99-5418-340e-ad24-7c1dca855034 | -10.487 | -49.952 | 2024-10-13 00:58:02 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f32a1ce9-9ff0-3992-80a1-93c6d24a3cb3 | -9.7327 | -46.938599 | 2024-10-13 00:58:03 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42adff4c-e13c-3fad-85ec-368ee27194db | -9.7347 | -46.947102 | 2024-10-13 00:58:03 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README15.md)
