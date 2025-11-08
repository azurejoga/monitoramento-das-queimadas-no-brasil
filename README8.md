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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2f0ff39-165b-3e42-a6e9-3898510b60f9 | -2.97201 | -44.58789 | 2025-11-08 04:06:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52223722-3a2c-3660-ba32-98f45fcf6409 | -2.52323 | -49.44544 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9f5fa41-e6fd-38e2-b3c2-caee229a40c2 | -2.4331 | -48.03959 | 2025-11-08 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bbf7fae2-d063-372e-87f1-3bb5ad58f709 | -1.18576 | -49.05433 | 2025-11-08 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f388c91-1f9f-33e9-9b16-8f3bc6cf5694 | -3.84068 | -40.72289 | 2025-11-08 04:06:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49ef7b3b-14b8-3818-8933-39632c097d58 | -3.2446 | -41.76358 | 2025-11-08 04:06:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 228486c6-c919-3556-8bcc-2ad675f0354e | -3.4438 | -43.1596 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f2487bbf-faff-3e46-8a18-4dd22b930e9e | -2.61353 | -49.22427 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb5842e8-4a66-394b-bad0-c29adfe6b0cd | -1.09758 | -47.51844 | 2025-11-08 04:06:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c244de55-f57d-3fa6-8943-cd26d276b5cc | -3.43844 | -43.17064 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91b49836-7ca4-3187-8477-74d460e1d862 | -4.0372 | -38.25066 | 2025-11-08 04:06:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f83e8bfd-3dbe-3a7c-8c43-ca8ae4cd3ce1 | -3.15698 | -45.49659 | 2025-11-08 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6265e34f-a9e5-3b56-bb04-43ce23ea2d9f | -3.06662 | -40.08058 | 2025-11-08 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6c41df64-cdd0-3562-980b-2c75079bf349 | -3.62936 | -43.65429 | 2025-11-08 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 85986d42-06c0-3221-8169-b0d86f2e6418 | -2.52377 | -49.44219 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98f23e6e-4422-345a-9961-348a8bd74dfd | -3.43782 | -43.17452 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0af67acd-891a-32c5-9fcd-d22aa9e86ffb | -2.4549 | -49.36927 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9cd019a-946b-3182-a1ad-603cf7278f28 | -2.69631 | -48.97364 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c62b58ee-600e-3547-b82e-8dbcdb6e7093 | -3.15642 | -45.50003 | 2025-11-08 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd35e13b-c70f-3225-afb1-ca2c9c702cd2 | -3.67079 | -42.37925 | 2025-11-08 04:06:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5e9a949-112d-3a96-a7aa-a7927552f88b | -2.46016 | -49.37011 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0af99dad-3b17-3237-a1ef-5f6995a4273f | -1.06855 | -48.09735 | 2025-11-08 04:06:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f77a689c-6ee6-3aa0-b084-005c3dd4bd2b | -2.66915 | -49.4432 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77a77bfb-3c6f-3110-8361-e6cb1b6d7f83 | -2.5285 | -49.44626 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6632fe05-0c13-32ee-9857-536c5a711198 | -2.7202 | -49.16604 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ad8b937-8982-3ac2-9201-438d6b819de2 | -3.1985 | -43.42089 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8486826-4006-311d-9eed-de3b484aaeba | -2.68372 | -49.55252 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea25a491-1ce8-3d86-be3c-aece7a155250 | -3.35497 | -45.29664 | 2025-11-08 04:06:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9092c9-fc49-36f9-b6ab-b8c7354ba40c | -2.09841 | -48.04551 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d2589c0b-ac7d-3122-b77f-d5753ce35370 | -3.43557 | -43.16622 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02f1321b-f209-3df2-b7e3-be2d1886252d | -2.45437 | -49.37248 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa8af7cd-4e8f-3eb6-8605-43a927ef5b1d | -2.62664 | -50.07502 | 2025-11-08 04:06:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b430ea36-3e97-31ba-877b-7f5d987e8f08 | -2.52214 | -49.45195 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d96a3d0c-b40a-3d7f-b44c-ba3542987484 | -3.44442 | -43.15572 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c4ad9a21-78ce-3f51-96fe-5b3287106b6d | -3.43906 | -43.16677 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9175c701-243f-35b5-9818-f40ceff6e94e | -3.87481 | -40.98522 | 2025-11-08 04:06:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 306c2af1-99b5-395f-870d-713ba73bab5f | -3.3597 | -45.29227 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 887cd181-fc8a-3bd7-bb38-538f42cbe9b2 | -3.9006 | -40.72866 | 2025-11-08 04:06:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c5f5dd5-da02-329a-ac12-6d786f977e49 | -2.62428 | -46.85416 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e53ea9d2-8f41-33e4-9f40-397af118b5b7 | -3.15426 | -45.49857 | 2025-11-08 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bad1ad5-c214-3b43-9fa1-5670381c2d8f | -2.71232 | -49.54365 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8f5eec8b-e0af-353b-8751-4d3ced4ee706 | -2.61301 | -49.22739 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a9d4fb5-ebb5-3c07-bf58-aa18dd756938 | -2.52904 | -49.44303 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8282db28-1022-3b81-981b-6f778a3c196c | -3.26149 | -45.98032 | 2025-11-08 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fe275f8-a9fe-3498-b88b-8e1251901460 | -3.29733 | -45.32869 | 2025-11-08 04:06:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8799c6e-7ab7-3cb4-aa28-0f3efd28a223 | -3.60446 | -43.51428 | 2025-11-08 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32918562-d911-3aed-91b3-38ed85034066 | -2.6125 | -49.23051 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 790aa43b-0235-3a09-8246-722abfca39a4 | -3.44193 | -43.1712 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bb7db2cc-3555-3126-9b94-1bceb06ac5b1 | -3.29736 | -45.33147 | 2025-11-08 04:06:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16ed43fa-2fc5-3f94-b6ca-ab1c81f32975 | -3.63228 | -43.65888 | 2025-11-08 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| aa404808-cc36-360b-ba8a-d3ee1edf24fc | -3.44317 | -43.16347 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c17d95b5-e8a9-31d1-b409-d2944c5599b2 | -4.0337 | -38.2501 | 2025-11-08 04:06:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27b00dad-f86b-3d3a-8a73-4a0bb04de7a2 | -3.62872 | -43.65831 | 2025-11-08 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 563cbf57-0fa9-3342-8cdd-c1c1b7ce8c9e | -2.7991 | -48.93958 | 2025-11-08 04:06:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85f73d96-573f-3711-8542-82810d011279 | -3.70031 | -42.78682 | 2025-11-08 04:06:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62f0168d-85dd-3055-8c18-a804f9d3ccac | -1.67188 | -47.40375 | 2025-11-08 04:06:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 715e52db-925d-3870-9985-8853f865c22d | -2.5089 | -48.26518 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a1e62e-e728-34b1-af2a-91521ee73517 | -3.80636 | -42.56087 | 2025-11-08 04:06:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd84c934-638d-37a4-939e-41bddc243064 | -3.6442 | -40.91023 | 2025-11-08 04:06:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53accda9-c853-33af-9e2b-54316e6dc75d | -3.76533 | -43.0442 | 2025-11-08 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9b8cf93-66a0-3f97-ac94-54beb9ab8587 | -3.33362 | -42.35672 | 2025-11-08 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cd48673-7152-3af5-959a-d1b79e8f2f98 | -2.42285 | -48.59491 | 2025-11-08 04:06:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35818ce0-7b4c-37f7-8108-c44d043dbc7e | -2.49278 | -48.15315 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a71005-1887-30ba-9f56-f79b14b17932 | -2.70755 | -49.53952 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39e17dc9-1338-37f2-b593-fe7b36eb3334 | -3.608 | -43.51483 | 2025-11-08 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a2df98c6-c40b-3d9a-981a-581f721af3da | -2.69978 | -48.97262 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ab402eb-d2b7-3cbd-bc84-3097d1273263 | -3.63357 | -43.6508 | 2025-11-08 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5c2981e-16ac-38c0-8fed-f5d50f23757c | -3.26208 | -45.97666 | 2025-11-08 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9453e88-bf0d-3b35-9bdd-4b78b6423af2 | -3.44255 | -43.16733 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 544ac844-19b5-3e68-a055-7230e701c93b | -3.63292 | -43.65485 | 2025-11-08 04:06:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| faf66fff-264d-371c-8fb8-5313dfbce900 | -2.96748 | -44.59189 | 2025-11-08 04:06:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b813f2b6-c39a-38aa-acb8-52e8c12958be | -2.96716 | -44.593 | 2025-11-08 04:06:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bda2586f-a356-3abc-a93b-8eac9926437e | -3.15243 | -45.49939 | 2025-11-08 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0374a965-0ff8-31e3-8c9a-718857bf8a36 | -2.52268 | -49.4487 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9cd0633-d319-3852-bcda-80e0b27e66ea | -3.23838 | -45.60192 | 2025-11-08 04:06:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b25eba4-043b-33b9-bb5d-bf16882c989e | -2.845 | -48.10685 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bc7c3e2-baeb-3fde-acae-3920c7e47710 | -3.6431 | -40.5938 | 2025-11-08 04:06:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 202464d3-4d7f-3e69-871f-18fe2aa8e427 | -2.09718 | -48.0486 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 578f6bd9-89cf-3ead-b899-3e924b76f4d7 | -0.92177 | -47.75494 | 2025-11-08 04:06:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60875f8f-e7d3-3111-bbde-aeecd0e762f8 | -3.84346 | -41.05009 | 2025-11-08 04:06:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0b50752-1c1d-32fe-b493-7ef13f6f1474 | -2.196 | -48.2253 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bdd3054-9b61-3ce1-97c1-f661ceeac9a5 | -3.69908 | -41.64455 | 2025-11-08 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 387ac04d-8986-35ea-8508-9077bb9b8baf | -2.96672 | -44.59649 | 2025-11-08 04:06:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72590837-7800-3301-8f0f-0418cd796434 | -3.35577 | -45.29165 | 2025-11-08 04:06:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18381791-f194-38a2-8299-07003b1775d0 | -2.45963 | -49.37332 | 2025-11-08 04:06:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c5a10c80-506b-3438-8215-83e66d0055e9 | -1.5058 | -47.15179 | 2025-11-08 04:06:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70930f7b-b673-30fd-9283-6be8f9964f67 | -1.191 | -49.05515 | 2025-11-08 04:06:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed598956-8c78-3f92-b43c-480566a99762 | -2.6199 | -46.85333 | 2025-11-08 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7d9abd1-0d57-3e00-a1b9-ad8384ccdab6 | -2.70702 | -49.5428 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 203e6f06-0ef3-3b04-999d-15f27eebcb4b | -2.49384 | -48.15158 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7155e02e-77cc-30dd-8f01-b0d499867f4c | -3.44504 | -43.15186 | 2025-11-08 04:06:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2f02d90a-e50e-3cbb-ab90-041cb721e165 | -3.4362 | -43.16235 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c383d5fb-fa4a-3f06-8bf1-af3c8632667e | -2.49299 | -49.13878 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6a26e29-0183-302e-9d4d-1a7c4ecb2144 | -3.76187 | -43.04366 | 2025-11-08 04:06:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83afa23e-9e6a-3116-9629-3173a859a8b1 | -2.97166 | -44.589 | 2025-11-08 04:06:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec3b4b3f-f563-3822-8457-97cde04390c1 | -2.71179 | -49.54694 | 2025-11-08 04:06:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 43cf0f0a-90f4-3561-84de-55291887cc3c | -3.16097 | -45.49723 | 2025-11-08 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5d8f7762-a989-345c-899e-ae5c4b0760f0 | -2.09757 | -48.0508 | 2025-11-08 04:06:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c3365850-781d-3fd5-9539-e6b859896136 | -2.6177 | -49.23132 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22d2085d-efc8-32d0-87b3-ecf649059ac3 | -3.09557 | -50.32439 | 2025-11-08 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README9.md)
