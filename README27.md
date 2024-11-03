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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf19f5fa-ceaf-38b0-a69a-5f085dacfb78 | -5.53416 | -39.17303 | 2024-11-03 03:53:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| adfd309a-6c08-36c0-8736-cf9a0866358c | -6.37794 | -39.25262 | 2024-11-03 03:53:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71c9d639-e028-39d9-b79d-298220073964 | -6.29179 | -39.5176 | 2024-11-03 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 81735bae-3697-31f0-bc85-e23bb464783a | -6.28844 | -39.51706 | 2024-11-03 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 42b9f4ec-ce50-362c-8965-63a5be546f57 | -6.77754 | -39.04796 | 2024-11-03 03:53:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11055467-bd51-3d87-a699-cde00176368f | -9.67192 | -40.5849 | 2024-11-03 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1a794fd8-3105-3604-8cd5-ef86c202378d | -10.74252 | -40.3567 | 2024-11-03 03:53:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| db348846-f162-36e2-bee9-37b01ba1abd4 | -11.54196 | -40.41391 | 2024-11-03 03:53:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 689f662a-125d-3150-a531-7cb1c049e687 | -11.53864 | -40.41337 | 2024-11-03 03:53:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1de59fe0-893c-321d-85e2-598710e17638 | -3.75975 | -41.03033 | 2024-11-03 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 31be6c1f-a1c2-36c4-b962-1b7fe6faf82e | -5.71911 | -41.54237 | 2024-11-03 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2f44e3fe-8eaf-38ef-b283-9b62d6742b42 | -5.70766 | -41.26306 | 2024-11-03 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e38e100-606f-37d2-a61e-4fed75586b56 | -6.31358 | -41.57208 | 2024-11-03 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 529a1b0d-4075-3f88-83c3-5b064197c1c8 | -6.236 | -41.63733 | 2024-11-03 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bc9169c5-5114-31a4-972f-117293100d8b | -6.53024 | -41.48463 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f11f80ab-d9c4-3efa-8166-e6b77d15c360 | -6.52957 | -41.48878 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77877a1b-0966-3f2a-b2e6-60759e88b56d | -6.5289 | -41.49292 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a03d00c-ba3d-3dde-8c47-6c226e949089 | -6.52664 | -41.48408 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 34847438-3961-3d6d-837a-4632530c8823 | -6.52597 | -41.48822 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| bd23cebe-6adb-3fd4-abf7-22596eb2dff0 | -6.5253 | -41.49236 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 0e3116ca-17b5-3024-84f7-c1bd4ad49aa1 | -6.52463 | -41.49649 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2c9b57a-ec89-31e4-b57b-1b923ad1fbcc | -6.52305 | -41.48352 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f77688ad-9c4a-3904-80b9-07eeee148cfd | -6.52238 | -41.48767 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 6dab39ca-1421-32ea-8619-737d3520b5e1 | -6.5217 | -41.49181 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 81771f84-5d9b-3e8b-8a27-795ff2b97f58 | -6.52103 | -41.49593 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0ac25e2-b096-36d9-8a6e-d7932bde8354 | -6.52037 | -41.50005 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c61a632-16a2-3fb8-94d5-f35c3bcfeb5b | -6.51945 | -41.48297 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 38530d19-e31d-3742-a72a-18c6cbf61f70 | -6.51878 | -41.48713 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 8a2ee13c-6d5b-358f-bd87-7d5088177b5e | -6.51811 | -41.49126 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 10596219-4aad-3487-9c40-f47ac32035d2 | -6.51744 | -41.49539 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f6674b0e-507e-340f-bdfe-af9449222624 | -6.51451 | -41.49071 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| e5ea0c82-cfb5-3224-bbe3-e19f7ff46443 | -6.51092 | -41.49014 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae8f2df3-c20c-3a47-ae9d-b802d047eab6 | -6.51024 | -41.49429 | 2024-11-03 03:53:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d26df7b8-aca5-30bf-bb02-59ed75cfa62e | -10.58191 | -41.4833 | 2024-11-03 03:53:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| bfd4f84e-d583-3311-aea0-f1d81672af53 | -11.70121 | -41.65448 | 2024-11-03 03:53:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6ea659d8-3ef7-3f22-ab4f-9c9a77f034a0 | -11.25306 | -41.90653 | 2024-11-03 03:53:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 01b65a3c-7a60-3253-8498-18a9e8a30f73 | -3.3926 | -41.65107 | 2024-11-03 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 364d1a94-fcea-3ae4-9a86-601953ab4da1 | -3.38883 | -41.65048 | 2024-11-03 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b7672df-7fb8-38a7-816a-70e36804e2be | -3.40179 | -42.50295 | 2024-11-03 03:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a7fb5ee-b72d-3744-bd3e-55a68080a7fe | -4.61963 | -42.79403 | 2024-11-03 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 57f4b105-006e-3fa3-a2a1-7225a3243f94 | -4.61877 | -42.79915 | 2024-11-03 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5bf8ed50-a6f2-3943-9b71-4115a4f16cb6 | -4.61682 | -42.79708 | 2024-11-03 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 761c2470-2c1e-3ff0-affe-095b6de9b215 | -4.61565 | -42.79338 | 2024-11-03 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6166e8a5-d78d-30cc-9700-4e64fa133bc9 | -4.6148 | -42.79851 | 2024-11-03 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b759344a-7041-327f-a3f8-3f404007fa15 | -4.5588 | -43.10844 | 2024-11-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0e419f3-7fa3-3834-b4ad-324ce7ba62fd | -4.55875 | -43.10876 | 2024-11-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d22d2c4f-055c-3270-ae3e-0f175dd5ad23 | -4.55817 | -43.11236 | 2024-11-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14235d95-8e87-326c-b93c-c64ef260c150 | -5.29402 | -43.07591 | 2024-11-03 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8fcf7e98-d465-3875-8361-dad1da980522 | -5.29346 | -43.0794 | 2024-11-03 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f7bbbcb-9e28-3f0b-9946-f700a752684a | -5.29001 | -43.07528 | 2024-11-03 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2e142956-5e05-38cd-902a-b9c09bb62cb5 | -5.15112 | -42.91231 | 2024-11-03 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63155394-a48a-3d3f-9c70-43f320016dfe | -7.65334 | -42.7587 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 78b4cc70-b01a-315a-a0bd-3036192b032b | -7.54624 | -42.86141 | 2024-11-03 03:55:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ffaf54a0-f4b6-3cc3-b4b4-e01c9462db77 | -6.85165 | -43.57697 | 2024-11-03 03:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ed99fbe-613e-3feb-b539-32c300f9d9e2 | -6.63965 | -43.47121 | 2024-11-03 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f7cfa97-9808-326b-b0b2-5f811873a5a0 | -6.63908 | -43.47469 | 2024-11-03 03:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5db33767-a596-3e94-b962-959c28dfc6c0 | -8.33896 | -43.57595 | 2024-11-03 03:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c31df3e4-9440-3203-86fb-f63af276f1da | -8.33723 | -43.58615 | 2024-11-03 03:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c11d0619-7ad8-3f12-8a00-ff22ba2ef8fd | -8.33501 | -43.57525 | 2024-11-03 03:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65682427-60f7-3ecb-892f-e76ae6789032 | -8.33415 | -43.58035 | 2024-11-03 03:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51f754a3-c9a8-3294-8b95-345053d0f39a | -8.3333 | -43.58538 | 2024-11-03 03:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2c252c2-2ecf-3065-8a22-2799997ce10b | -8.32714 | -43.57378 | 2024-11-03 03:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 623b389b-6cfe-3740-b6c2-86527edf8bd3 | -8.32627 | -43.57893 | 2024-11-03 03:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb143e25-c849-367f-a886-94c547a758dc | -13.39372 | -44.41969 | 2024-11-03 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70394a3b-8883-3c14-ba59-c6077e61812b | -13.07774 | -44.72831 | 2024-11-03 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03bedfdc-ff66-3450-b6c0-70741678ff16 | -12.85327 | -44.12757 | 2024-11-03 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c0542b1-0cb7-3393-975c-cb8de2dc4ba0 | -7.45137 | -44.73256 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a901868b-720b-384e-8917-8e9b7d08adfb | -7.44846 | -44.72373 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11932cd1-bdb7-3ba2-b558-c1dda065e748 | -7.44631 | -44.73605 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1282a756-0de7-3311-8c79-0a83209c44aa | -7.44559 | -44.7402 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2a69e24-b4e3-39dd-a737-4708a4cbdcfc | -7.44413 | -44.72303 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc5d6b1d-59e5-31da-9d1b-6d681f40e310 | -7.42778 | -44.72974 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25b9a15b-d48d-398f-81e1-aaf15a0e79a6 | -7.4254 | -44.72847 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc0fa3e8-9d19-33b3-8482-0c512b9b99a6 | -7.42346 | -44.72902 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 377a7c05-0d5b-3360-b8ac-7f649abc78d7 | -7.41914 | -44.72826 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92029a49-2f71-3f4b-ba77-410d898733c8 | -7.41843 | -44.73249 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3086b61e-ed9e-32c2-9db8-1f676beb5bdf | -7.41411 | -44.73175 | 2024-11-03 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d587ad13-064a-3ca3-beef-1fbf97fb350f | -7.18152 | -44.9606 | 2024-11-03 03:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02c7d358-0f63-3e7c-8952-ffce8b6a241d | -7.18063 | -44.96368 | 2024-11-03 03:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2103b5ff-f20b-3de2-83fe-6124f0fc2cdb | -6.90737 | -44.62854 | 2024-11-03 03:55:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5143452a-bb5f-3628-8792-27497a042f6b | -8.49961 | -45.48417 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0da9015-581d-3cdb-a825-b6d35a4cf971 | -8.49833 | -45.47698 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a60e8c53-7e6e-3788-9824-32dd3efd62a3 | -8.4967 | -45.47467 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a594699-b60c-3066-a7f4-03ca3ed43dae | -8.49597 | -45.47878 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3cc3fa5-fc39-3dd7-82a3-34f5dd663710 | -8.49387 | -45.47617 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 85b4c3ce-8d35-3f70-99fa-dfc62164eda0 | -8.49149 | -45.47805 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 336c7200-8786-3d64-8e7e-244607dcaec5 | -8.48996 | -45.48666 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e986edf6-6eae-3e69-a935-22713d561b90 | -8.48917 | -45.49107 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 45b5e556-3a7b-36d2-9bf2-4bd526c5268d | -8.48794 | -45.48393 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 08a0b5c6-dada-3a23-8cf2-c44c4b027ab3 | -8.48721 | -45.4882 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f48cf193-d62c-3682-8eb1-70babcb27d8f | -8.48645 | -45.49265 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5e17f68b-1e4f-3d06-9257-02364c54b7d2 | -8.48626 | -45.48156 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6df0cf8c-5aba-33e6-a45c-272060161407 | -8.48551 | -45.48579 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| daf45645-4707-306b-ba64-21b0a63dc574 | -8.48473 | -45.49015 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 706075fa-6614-3029-8afd-7421c2f92e7b | -8.48349 | -45.48307 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 419bb412-e694-3098-ba55-c4f4a8ddca6c | -8.48275 | -45.48738 | 2024-11-03 03:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51780705-0303-3f68-b07a-bfac09418f6b | -7.76501 | -48.24087 | 2024-11-03 03:55:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4bf91b9-9828-316c-ae7e-7aef4874ea83 | -7.76021 | -48.2363 | 2024-11-03 03:55:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a0b1650-0ee4-3173-8c1f-6afd1a00ad32 | -7.75957 | -48.23985 | 2024-11-03 03:55:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0010d940-c8ab-35c5-827b-9a38e5b6f942 | -7.75283 | -48.24614 | 2024-11-03 03:55:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README28.md)
