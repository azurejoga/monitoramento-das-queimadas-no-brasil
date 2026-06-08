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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecb8b5d5-1ce9-3ac4-890c-966185bd98de | -12.48298 | -46.26518 | 2026-06-08 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79d68c20-2518-34cc-9fd2-c85a9ae7852e | -12.48725 | -46.27206 | 2026-06-08 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebdc9b4f-6934-317a-a632-d00d4d06d16a | -12.04983 | -45.57093 | 2026-06-08 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aa81f56e-fa0e-3f9f-9f54-fbad5718d75f | -14.39775 | -43.80516 | 2026-06-08 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a104fb4-b548-3f63-ad34-daa2f2231592 | -18.90898 | -47.43495 | 2026-06-08 03:49:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1818c9e9-b8e2-327c-b529-ccce0468c8ad | -22.77938 | -43.37596 | 2026-06-08 03:49:00 | NOAA-20 | SÃO JOÃO DE MERITI | RIO DE JANEIRO | Brasil | 3305109 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e528466a-fb15-3208-b4c2-22e8f5a2ded1 | -14.3986 | -43.80062 | 2026-06-08 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5854588-b383-3020-b629-8edcdec41972 | -12.31947 | -46.0801 | 2026-06-08 03:49:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cf7be3a-726c-30d0-ab43-cccf785c2aaf | -20.32399 | -47.73184 | 2026-06-08 03:49:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a26d9b7-3b59-36d3-8c39-0552fcd30b07 | -12.06628 | -48.42984 | 2026-06-08 03:49:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cab857d4-bda2-3b2f-95ca-8b52ff623be0 | -20.54625 | -42.11986 | 2026-06-08 03:49:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f7402cb0-05a9-34ba-ae84-bf6d417899b2 | -6.98379 | -42.8824 | 2026-06-08 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f1d60206-e459-3b04-abf5-537ca93d0fba | -3.49611 | -48.03237 | 2026-06-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 68e8b604-e1d9-340e-a987-0382f0066efb | -3.49556 | -48.03585 | 2026-06-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 39333ee1-84c7-367c-92cc-b878259fde3d | -3.49889 | -48.03635 | 2026-06-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b8ed767b-95e2-3b6a-b6ff-8d9695efa344 | -6.98431 | -42.87886 | 2026-06-08 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 746bdbde-aa5a-3db2-8588-b0263631b0ea | -10.14393 | -47.64055 | 2026-06-08 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83bae910-dc54-3a49-9091-bf3d58475aa5 | -12.4922 | -46.26428 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f90d992-337e-3b47-81b7-0edba6ba3f68 | -11.55397 | -52.80707 | 2026-06-08 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc12bba4-80be-377c-9f77-79d32483dea1 | -9.09495 | -50.60817 | 2026-06-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b3d3ecd-4f1b-367f-b4e5-5ca9d116335b | -10.85243 | -53.74229 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e71cd926-cbf0-3eb8-94d0-99655474e674 | -9.30847 | -48.96707 | 2026-06-08 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 328a8a07-7208-364d-8e17-a3bc70003190 | -12.49055 | -46.27569 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| af0f0f6b-55a8-3d43-b5ae-f71337d562d9 | -10.85302 | -53.73883 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b657eb42-7173-3ffc-905f-f4faf5ceca87 | -11.79642 | -49.50691 | 2026-06-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c8c98d9-fd34-3872-bd15-7db2eb343739 | -10.47993 | -47.93196 | 2026-06-08 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dae4192a-9965-33c4-8116-48aff824047e | -11.30128 | -54.8834 | 2026-06-08 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d52598bf-3183-37fd-afe0-74781a2d6724 | -12.06753 | -43.84943 | 2026-06-08 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e4374a3-b689-3f06-b41a-ab645a63bfbe | -10.82533 | -56.60118 | 2026-06-08 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a9bd5c-2ddc-34e9-b7fc-1aeed67406e7 | -12.22777 | -51.34052 | 2026-06-08 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91a1db79-d5d6-30dc-bb3e-0d8e5dbdb271 | -12.05242 | -45.56873 | 2026-06-08 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0b65888d-33ab-35de-9b71-756ee99dab84 | -12.5177 | -48.27871 | 2026-06-08 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fab1edce-75d5-30fb-b6ba-98e41b4f4013 | -7.00156 | -43.86528 | 2026-06-08 04:34:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16f32d7d-f1e6-3a6e-ae81-dc35d3c457e7 | -10.84726 | -53.74858 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 713eacb9-c75b-3408-be45-1c04d34e56b6 | -12.32383 | -46.07742 | 2026-06-08 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 517a8241-a657-303a-b349-1b88a1ef1276 | -9.418 | -50.67564 | 2026-06-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f3e7270-35a7-3d54-b826-18ad8995f228 | -9.0915 | -50.60761 | 2026-06-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 104ad6da-7607-30db-8309-a0f35cab1291 | -6.85113 | -47.90656 | 2026-06-08 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3606df75-4139-3a18-8082-5f4d6db068a4 | -6.75351 | -45.0123 | 2026-06-08 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f955436-18e9-3176-9cae-bfa703979620 | -14.40167 | -43.80523 | 2026-06-08 04:34:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b93dc72-1fc7-354f-8218-f1dd9c69c1ad | -10.85642 | -53.74298 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff354fea-944e-3b63-b2e6-10d7b87fef2a | -12.51824 | -48.27514 | 2026-06-08 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb0d3809-c282-347b-a176-d91b98d2a488 | -11.60346 | -49.32795 | 2026-06-08 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fd98df5-f28b-3c04-95d1-9b0a8f918325 | -11.84322 | -52.51271 | 2026-06-08 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85acc8de-85a9-34ba-adbc-656a2f7e8837 | -7.15292 | -43.15088 | 2026-06-08 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3eaf9b1e-463a-3825-9c65-c6af2d5db02d | -10.85184 | -53.74576 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76badb8a-bd60-33b5-a35d-cfd61552f659 | -12.48757 | -46.27125 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34ab3c22-81e4-39a0-830f-a2766f38990c | -11.58604 | -58.50959 | 2026-06-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 661e4375-00e7-3352-91a9-1648f08cc5ce | -10.12298 | -57.75906 | 2026-06-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| debe5329-5433-3060-98e1-517ba0b1265e | -7.23892 | -49.67601 | 2026-06-08 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a26104c5-5233-394f-a710-c4a5d8ee7ca4 | -7.32362 | -46.96428 | 2026-06-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be1c7af7-e179-399f-9b17-fbc301ca8ac5 | -10.14725 | -47.64108 | 2026-06-08 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8295e47e-cbcf-3997-bf75-38bb357a0816 | -11.0354 | -44.32141 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c98ebc94-bb1a-34b6-993e-682bf9141e4e | -11.02642 | -44.31786 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa6b2c1d-5e40-3587-96eb-5bbedb9bba1d | -12.36894 | -47.89202 | 2026-06-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb0ea98e-d140-3dd5-bf1a-19ae84fee6aa | -9.78335 | -47.44282 | 2026-06-08 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b62f0bae-267f-386c-84e3-47979c95d940 | -10.12177 | -57.76567 | 2026-06-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad2a1f27-d372-3cfc-9840-04f838a84f9f | -9.25276 | -48.23825 | 2026-06-08 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28c304d3-6414-3956-ac29-3fd4c23d4519 | -11.03153 | -44.32084 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70c1a8d1-f430-3b46-a71b-b56ebdef574c | -11.03505 | -48.91645 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4307bed8-08ab-3786-8e11-fbf78f080e5b | -10.49817 | -49.27746 | 2026-06-08 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfef92c3-7675-38eb-8d79-4755764b68c5 | -10.12238 | -57.76234 | 2026-06-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fedd4033-83be-3e14-9885-7d938c0c0a10 | -14.40219 | -43.80126 | 2026-06-08 04:34:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 952bc33f-6719-3d55-83c4-5bc14fa2d532 | -12.49575 | -46.26476 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f128e6e0-d270-37a5-9ecb-8d36034c956b | -11.51251 | -56.12828 | 2026-06-08 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85d16670-f43d-3e87-9809-8e88cd1de8f7 | -11.79311 | -49.50637 | 2026-06-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24cb8281-1eb3-3b04-8010-c9dba01f5f78 | -9.30792 | -48.97057 | 2026-06-08 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22b475dd-27d9-3ec6-bcd3-3842c35c0dfe | -7.89852 | -47.09626 | 2026-06-08 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b475c82e-59e0-3551-8bb3-6d1fa5832bde | -10.84667 | -53.75206 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c87537be-f39a-3d50-a65e-1fd88d58d462 | -11.0876 | -48.26915 | 2026-06-08 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4267b683-30c9-3f0e-9491-91ab24fa66c1 | -9.78668 | -47.44334 | 2026-06-08 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8b41df7-5c63-3e6b-bc98-22a238aa2fb9 | -9.49296 | -40.38612 | 2026-06-08 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 66fe1da4-bb43-38e6-9284-d77c2e0ae347 | -12.49112 | -46.27175 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48cdeb13-f21e-3887-8881-d43c01ca05fb | -9.34448 | -49.14872 | 2026-06-08 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 123cb3a0-72cb-3145-ba53-4859dddf7c70 | -11.44224 | -46.67914 | 2026-06-08 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f80ae85a-1075-341a-b68f-cfc453a28759 | -6.46639 | -46.89954 | 2026-06-08 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1eb95dc9-7c4b-3f2b-a058-a36e21b83f7b | -11.63738 | -47.87735 | 2026-06-08 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ef315f0-2bf6-3814-8ce0-4deac1accbfa | -12.06979 | -48.42915 | 2026-06-08 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8064bb07-dd69-35cd-b98b-3bfadf180b1d | -9.03706 | -42.68812 | 2026-06-08 04:34:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 92643256-cdf5-3b00-82a7-2933ffd0a8de | -11.4365 | -46.67043 | 2026-06-08 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e0ae752-61fe-343b-82f0-c2ce3b48147a | -10.85911 | -53.74073 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a83f646-6f16-3fdd-91b3-2a6ac4f33130 | -12.48492 | -46.26464 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38d1b065-da9a-3b52-a52f-bdc697e7ed3d | -12.49166 | -46.26798 | 2026-06-08 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da07de46-6d7e-3e24-95fe-58b83db267cd | -10.90306 | -49.34317 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc36c953-1e18-3ced-9df6-357ab09c3cb0 | -8.81196 | -43.92951 | 2026-06-08 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 134eca61-124c-3741-8e25-b5b3d49e9b84 | -10.14671 | -47.64464 | 2026-06-08 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab10f4ec-60cb-3939-b88e-17a92ad12862 | -11.03416 | -44.31899 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a94ca988-a886-3db2-a898-8a2f173b17ab | -10.85452 | -53.7435 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b22a0f37-70db-366d-bc5c-e94251c42fa4 | -12.04816 | -45.57253 | 2026-06-08 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1cf4cb9-f04e-3718-8b55-fea1ee07f51e | -10.88188 | -49.54195 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56065f4b-88d4-33f9-8e45-bbb064b6ddc1 | -9.09235 | -50.60823 | 2026-06-08 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0d5ccc58-6f6e-3478-87ff-7ecd77e79d5f | -11.02765 | -44.32027 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75db34ad-0fb4-3602-a04a-af60ba24da41 | -12.06687 | -43.84937 | 2026-06-08 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 385ec3fa-6741-37aa-ae10-ae52c77c31c4 | -12.51214 | -48.27052 | 2026-06-08 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1da9521f-f575-3ff9-8a4d-86dc512b144d | -10.85513 | -53.74004 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f0cb208-c6a1-364d-8ad3-cabe529f947b | -10.88132 | -49.54549 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1f40e55-3930-3722-955e-25bab6f71cdd | -10.84785 | -53.74509 | 2026-06-08 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b049b90-b018-3dd3-8ac8-dcbe83cbe2fa | -11.79255 | -49.50989 | 2026-06-08 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32a041f4-b57b-3f64-bcf0-7e6f87a78bcb | -11.02833 | -44.31533 | 2026-06-08 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bbd1bf1-5029-3c22-88b9-431f037eee4c | -14.03122 | -47.38797 | 2026-06-08 04:34:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
