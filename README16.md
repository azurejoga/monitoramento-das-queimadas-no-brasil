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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3d69c33-dc7a-3754-b460-5e204a734145 | -4.15037 | -49.16449 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf7745c-32d4-3c02-b73b-30906b82233a | -3.53457 | -53.25773 | 2025-11-26 04:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a55f0523-3263-3e1c-bcdd-8ff83c790c4a | -4.09892 | -49.06627 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 444f2a5e-8eac-32d1-b287-53a278109dcd | -4.1672 | -43.71506 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 99e40121-1e6b-310f-86e9-2e0a3924be16 | -5.33127 | -43.56919 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 54b631a5-1844-3140-a516-a4f5e5bd4e36 | -4.30865 | -50.74509 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62d3e51a-3c8d-3c31-80ca-65330ad6de01 | -5.32794 | -43.56867 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f9783b83-ba1e-3c0a-92ed-4c150c1cd8d5 | -5.32848 | -43.56517 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e21627a2-8ad1-3e5c-8419-f32ecf65b6c9 | -4.17383 | -43.71609 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 3dd4654b-d4f9-358a-a382-5abe20b0e536 | -5.209 | -42.90135 | 2025-11-26 04:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ae9d4ae-5248-39b3-8c94-332764985515 | -2.92862 | -48.22239 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 248df165-fe84-3ae7-9782-af13ed1b12c2 | -7.48155 | -42.75212 | 2025-11-26 04:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d6a497f-577c-3b17-b583-51dde8f960f1 | -6.30844 | -43.7929 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b240edcc-8267-3e56-bcb0-68203b76349d | -3.02356 | -51.03311 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c97fafa-85eb-3e89-983a-cd5c75a043b5 | -2.74291 | -49.86856 | 2025-11-26 04:21:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de39fd54-cf69-3d2f-9259-d5ba258cb6c9 | -2.8215 | -49.12676 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e610bce-6f01-3477-9320-130e0cae6f8c | -3.59333 | -40.98357 | 2025-11-26 04:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a25c18b3-f0f8-35b9-a95f-95c23bd04a85 | -4.82311 | -43.82156 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 531f78f4-20ce-37ff-92a2-beb2e7e49be6 | -5.3346 | -43.56969 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64596fed-c391-3814-b0e3-89afc7df91f9 | -4.18924 | -43.70438 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 070f879d-6b61-33c0-9e89-5546c808c3ed | -2.49555 | -47.82803 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0df56314-74b4-3b18-9ab1-078adbd632b0 | -3.69545 | -50.94601 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c16aa361-a6e0-30b1-9752-ccc841d09325 | -2.4835 | -47.83079 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dad522bf-8fca-38d5-b00b-c5728ff60bae | -3.29999 | -53.04482 | 2025-11-26 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e30f7a9f-cd37-315b-bd9e-186769105812 | -4.36249 | -48.29633 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae5fde24-b3fe-3126-aa38-09cd7917455b | -4.59721 | -44.41493 | 2025-11-26 04:21:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b916a017-8eea-3c90-ad68-ff1bfec45ad3 | -6.55765 | -39.02059 | 2025-11-26 04:21:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3758cbde-fdce-3776-869e-efe67362618d | -3.38886 | -47.19328 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012cf26f-e771-33e0-b5ab-697e907a2c34 | -5.25159 | -44.14422 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd7d1858-49bd-3811-9c87-cea819453a10 | -4.81539 | -43.82745 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2767dd36-3335-36a1-8f25-116aaf8ea87d | -4.65294 | -43.97556 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b629c563-1015-3707-9cd9-3d814658ac1f | -2.50309 | -47.82924 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 85682f70-eb19-3c72-ac30-318c6ea71114 | -4.14439 | -43.64421 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 278a6bcf-5340-3423-9a9f-f0057b01737d | -8.04956 | -43.11135 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 319638f3-1132-34f1-81ec-b91262fa3350 | -3.13073 | -49.40486 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da8793d8-22b1-3a23-a313-3cc988a2dc30 | -3.36114 | -49.50346 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fa46b60-e09b-3b43-9972-a1e2b0ccb61a | -3.59892 | -38.78007 | 2025-11-26 04:21:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 059f1a63-9e30-37b4-8470-72c3eada7ac0 | -8.06499 | -43.12523 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 547838ea-6e10-376b-adb9-8619414b59a1 | -8.06213 | -43.12096 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 0cf15a23-6b4a-393c-81f1-5ecdb42e5ab5 | -3.67413 | -43.56714 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8d5ddd1-3187-3772-a75a-338ea86643c4 | -3.94724 | -49.45978 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad853b44-f4b3-30bd-bd7f-2fabf7ca33bc | -4.94099 | -44.30308 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a38a6eac-5a50-38ae-b648-8a19bb02b348 | -2.60767 | -49.44582 | 2025-11-26 04:21:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f1f7f8a-6e0e-3dd0-8732-bf62104732e5 | -4.74653 | -46.555 | 2025-11-26 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57ac8de1-4608-3d94-8d71-fd9d780c59f5 | -5.75931 | -46.43443 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c31ed2c1-8087-3be9-9e1e-056b15b140d6 | -4.56792 | -43.80264 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bfc53120-d4b0-374f-a92d-83e147a2ec22 | -3.6675 | -43.56611 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6eee24d-369b-3e68-9691-c28b53127174 | -4.53257 | -48.94301 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ab969b2-ab17-37e3-9e11-6e5682772b75 | -4.15444 | -45.14951 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ca06e27-6793-302c-860a-44feb8fa313e | -3.03782 | -45.11745 | 2025-11-26 04:21:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ec38e4-010f-332c-bcaf-ee0f4c8b775f | -3.91077 | -46.74089 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a595fab7-0187-3a22-a455-ff9bee4a6cf7 | -2.90176 | -45.48357 | 2025-11-26 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b01fdba-cfc0-3131-81aa-85510efa7dc9 | -4.72267 | -43.33433 | 2025-11-26 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 93460711-dc4f-36c3-a617-e59a5ab8b8b4 | -6.57085 | -47.90407 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4db44be-58f2-3089-b26b-edf3d754dd09 | -5.2758 | -43.64275 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39dce333-2c75-3027-801f-f90ed1314bdb | -4.2818 | -47.29758 | 2025-11-26 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00668001-ce2a-39f3-9352-44136c76b689 | -4.28345 | -47.31025 | 2025-11-26 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ce5ea56-2dfa-3ef6-a6f5-868e61b3407f | -7.012 | -45.17276 | 2025-11-26 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9575e23a-4f53-3afd-b776-a26f8bd26c7f | -7.30277 | -45.43967 | 2025-11-26 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 909cd25a-f735-31fb-b23a-98e778f870ad | -3.04173 | -45.11445 | 2025-11-26 04:21:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 964d9ea4-b7b0-3884-90d0-2a8579e38eca | -4.22585 | -48.37042 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| afd1e26c-6439-36dd-8c1f-f12b1149d815 | -8.03927 | -43.10976 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c84cee31-2dda-3766-91fd-94f6e6b73cf6 | -4.22315 | -48.36768 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f111c6cd-c587-372e-9def-711e28eea522 | -3.13134 | -49.40112 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 99e1e37b-e146-382f-82dc-d3ab325606d8 | -4.9055 | -43.79512 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 746d9890-cd2c-3680-82e6-180b157bd3ad | -2.48498 | -47.82171 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d963c774-62e6-3196-8d58-85f1478ba822 | -4.81208 | -43.82693 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 643b7ee3-c420-3097-9245-34c53e7d1cc0 | -4.2589 | -45.13405 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a061460e-8231-3f55-b590-0e5aeebf6f10 | -4.25392 | -45.12252 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90f9ac80-ab34-3cc6-bfe2-cfd3ff630c5a | -4.83164 | -45.76371 | 2025-11-26 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e4864c1-7049-37fa-9c09-ce35209d9fe3 | -6.0585 | -43.25975 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2aaadc8-de8b-3b8a-8b24-42812d9834ce | -3.47554 | -43.4259 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc013f07-2899-34e8-8ccc-27342b3cdfce | -7.50955 | -45.71956 | 2025-11-26 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cd6d53b-7a9e-3bdd-a913-5d54da26a792 | -3.32536 | -49.72438 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 864daedd-c140-3cbb-9486-3385167228af | -4.83221 | -45.76016 | 2025-11-26 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69549087-8add-3b98-8a7c-b8bce5f33476 | -4.17165 | -43.72993 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 21b7f10a-146d-34a4-b408-ec310a612fd7 | -3.45795 | -50.54203 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eaf08a40-6eaf-3fe9-80b2-ba4b16c5591c | -4.30938 | -50.74075 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8ca6607-cda2-3fb6-9366-b86194b2fc32 | -3.33171 | -50.26916 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5bb85aa1-f9de-3ee2-833f-6cdd2135a933 | -4.94677 | -41.15814 | 2025-11-26 04:21:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f6fbdb7-9e43-3e2e-9ccf-c3ef22133c55 | -2.7425 | -47.13577 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d7335141-15c9-379c-b251-013aa7907549 | -6.04711 | -45.83578 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39bf30bf-2562-3145-b69c-aebd153e262a | -3.35817 | -50.4916 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 516bb546-58e5-3de1-a35a-41fce2701d4e | -2.91636 | -51.30734 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84f8ca5a-4e07-3859-9371-5ff019d3a535 | -3.40598 | -42.42007 | 2025-11-26 04:21:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca8529c7-da7b-3144-93b5-ed5326f828b4 | -4.17773 | -43.73441 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 399f17a7-447f-3fb5-bddc-4ed81e1bd822 | -4.53994 | -45.56812 | 2025-11-26 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d57f62ae-fdcd-3278-be4f-a87752ff439c | -5.43162 | -45.85512 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aefbde68-547f-3856-8327-85e7f7c36bb4 | -5.04378 | -40.22885 | 2025-11-26 04:21:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44f611de-eda9-3ba7-a502-10c933bea7bd | -3.53309 | -53.25509 | 2025-11-26 04:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 443c2a0d-70df-33e2-8b2c-3152bca69cce | -4.17056 | -43.73684 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e5fa8b7-cc8c-309a-a12c-af1202db63b4 | -8.06098 | -43.12845 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1cb01e82-706f-3443-b567-279ce1668176 | -5.23236 | -45.42406 | 2025-11-26 04:21:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711c354e-4a34-3138-9742-b6cb1213974c | -5.49823 | -42.37411 | 2025-11-26 04:21:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 813044ff-32b2-35ad-ae4d-170f6279ea88 | -3.17232 | -48.031 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db70a589-c1ba-3ebb-9b53-a55d655ef696 | -4.59215 | -45.70726 | 2025-11-26 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 483b1ba6-dc33-37d2-a248-6648fdaeabd3 | -2.74936 | -51.90701 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7a6c56-a738-3047-88b3-5f67d2f7f639 | -7.56249 | -45.87901 | 2025-11-26 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 476825e1-86da-3168-9129-607c5c1f86a5 | -3.21414 | -45.1455 | 2025-11-26 04:21:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 184c933f-a600-3e2e-ae7a-c9e47a99623e | -5.12403 | -43.02501 | 2025-11-26 04:21:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README17.md)
