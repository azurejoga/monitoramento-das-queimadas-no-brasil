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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53d66ef3-c67f-3647-b867-02ff3aba3065 | -5.71446 | -42.86784 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 094b0c10-3e6c-3b5f-bdd2-e6e5e47d513a | -11.67295 | -44.29381 | 2025-09-29 04:57:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1660fcd2-d948-38e1-84bd-45eb8e91e06d | -3.83927 | -48.9596 | 2025-09-29 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23bbb01d-2a74-3e5c-b423-2fdbb4ec7f85 | -8.30118 | -45.48908 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee3956eb-ee51-3adb-bd28-06613d711223 | -9.25972 | -54.57494 | 2025-09-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 565c54c7-0669-3afd-96fa-5bbbf724f3b3 | -7.90153 | -44.59977 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2272c8fc-6b32-367b-9c9c-49e38e11b5ba | -8.8315 | -50.66581 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4708e7e7-96f0-3529-bb23-5fc4538b5c06 | -4.33772 | -48.61255 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 794950a8-b579-3c6c-a84d-6603649b48aa | -11.21219 | -47.74738 | 2025-09-29 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 785a233b-ca6b-38fb-b001-ef774a2931e0 | -10.68574 | -46.75431 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe010652-1203-372b-ba78-5f4edc03b48d | -8.82287 | -49.23762 | 2025-09-29 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3dae2ddd-eff2-325c-bc09-2678e98429e1 | -10.04246 | -52.10058 | 2025-09-29 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe05c45d-f1bd-3708-a6de-6a76e2790175 | -5.90688 | -45.8548 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f37780b-4fb0-3f2d-8170-8eb3663fea2e | -10.80783 | -46.67816 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58f18ebf-0f2f-3ae2-b076-05c374d136b1 | -9.75788 | -47.78531 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cad6d473-d9a6-3361-940d-f4bac1d047c6 | -6.06822 | -42.60314 | 2025-09-29 04:57:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e79765b6-109a-3319-83bc-dc10c09b55d2 | -4.2287 | -50.38728 | 2025-09-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf958424-99df-3a65-bd81-2ebf19c2bcc5 | -7.58166 | -44.8045 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4beba128-56e6-3f12-a851-786c55ef9e0b | -10.81016 | -46.65974 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 734ca99e-b9ae-3508-b62a-11d5871ea91d | -8.14239 | -46.40795 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5b73fa38-a4d3-3b64-abd6-773a1e20bba8 | -9.30996 | -45.70718 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 215226c4-04bb-3d0d-91c2-04fcb68c00d7 | -5.88853 | -43.29718 | 2025-09-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51ace2ca-de4d-3c84-9948-5c097749fab6 | -9.39971 | -54.70034 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2abda4e9-dccc-39df-aef0-38de8fec0aec | -8.27208 | -45.50335 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 586416ea-ebbf-3a5e-986d-94fa2efaed96 | -11.36067 | -45.07215 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b512825b-ac2b-39df-8043-7c674aad792b | -8.65641 | -50.08968 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f57ab1eb-595b-3674-9484-ac874ba9fdfc | -5.15418 | -46.07951 | 2025-09-29 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e28a30d8-3016-31b0-b240-7f7cfe8b42e5 | -11.45374 | -44.99074 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebec5e5d-67cd-31e7-a591-09d3898ab9e3 | -6.83444 | -44.83075 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ab288b0-f457-390d-8012-2c999c035ca3 | -7.02974 | -45.18565 | 2025-09-29 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 893e98e5-df48-3842-9fb9-b8ba526c42f4 | -8.30468 | -45.50375 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a5918305-b1d7-3fb5-a079-b603a8889e4d | -9.41507 | -54.68853 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b954b2b8-3776-3007-adef-94739bc58084 | -6.19168 | -44.30186 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f920b6d-0b5c-3e35-997c-e046de5c090f | -10.685 | -46.76015 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7577f816-ed59-3f5d-8e3e-8c501c09c17b | -7.10627 | -45.53333 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e01771b4-6728-396b-82a7-123dde518d38 | -9.05352 | -46.7067 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b7029390-8304-30c4-8651-29253d4b8997 | -9.55138 | -47.76809 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d79b826-12f8-3e4b-a7cb-afe0e4068c52 | -8.76939 | -48.50747 | 2025-09-29 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2db74e31-783d-3ea7-ab9a-4bed80a2d601 | -10.81779 | -47.93495 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74b66406-371b-3d0f-be91-a3072232edaf | -4.29419 | -48.26724 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4bbb48c1-6a45-3dd4-917a-35dae215670e | -5.19086 | -43.76353 | 2025-09-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c4e98d38-b643-3953-8ab1-48121aa6375e | -7.82904 | -45.14137 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8eb43df7-5327-3c7e-9de9-b35ea1ec2ebb | -10.7551 | -45.38603 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72972e21-5ae2-33fa-9d50-4b644c7a16a2 | -10.41159 | -48.11601 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9df90e05-343c-343d-9ff1-3eea92066021 | -9.10536 | -45.8442 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9af3cb-0f57-3bda-a366-f3b58f4c8901 | -10.32439 | -48.20702 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 228c0d01-f50b-3b37-8682-5472c21b4ac3 | -6.89724 | -45.72473 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48960d66-6d77-3acc-a25d-568fff7c79cb | -6.89313 | -44.53217 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13303950-2b16-39fd-850e-a521fc2148cd | -9.40113 | -46.2415 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5562cb3-6c51-3f77-abd1-327f8ffb52ad | -9.41701 | -54.70297 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c43dbdc-2cfd-3081-83d1-456f09dd0169 | -6.62134 | -44.95595 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcfbcabc-1e46-3651-8720-1578d24bd9e3 | -4.97532 | -44.5053 | 2025-09-29 04:57:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a6b5ebd7-8ded-3161-be65-0284aff6d71c | -8.27862 | -45.49498 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 943a078c-ae31-34c3-9b59-a3a2c51350d4 | -9.78256 | -46.94137 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c31c8d9-be7d-3e0e-8739-2cbd38597de4 | -10.54432 | -52.30456 | 2025-09-29 04:57:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7877c86-747a-35d9-80cd-470e09d60b19 | -5.91233 | -45.85264 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec89216f-bed0-3119-b7f9-4fbc8f04d59b | -8.29355 | -45.5056 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2b59a758-f08a-3106-ab14-167a3e878d89 | -10.39798 | -48.14803 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42203ffa-8842-3a8d-bddf-eac02b39f69e | -10.31137 | -48.19996 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ffb92ae-583d-3ab4-8d8d-5e5aa1e9dff9 | -8.8683 | -46.59899 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35fe7312-c68d-3dc7-8d4e-7d74da8ea61d | -6.49967 | -44.12143 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d82d68-7cb4-3fac-9824-cc0ce813fe40 | -10.45666 | -50.85051 | 2025-09-29 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 416eda5f-4fa5-39b8-9db5-e1756a86b9a8 | -6.74476 | -44.75018 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e189192-e362-3a45-a1d2-e5ded20b7f67 | -7.89637 | -44.59536 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eac0c109-0659-3408-aa22-29ec2e2e12eb | -9.75968 | -47.78465 | 2025-09-29 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f805e2fa-fb0a-370c-9cbc-9afb76898b8b | -10.46108 | -48.20115 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c7334b5a-d555-395a-a173-ce0f82570212 | -8.86604 | -46.61621 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8016226a-75fa-3275-81c3-600af1e5534d | -5.722 | -42.8549 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9f725d58-40e3-30e6-a6ea-9731e8111573 | -10.19621 | -52.5591 | 2025-09-29 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc888ea6-32aa-3bee-bac1-219a2cc254af | -7.58695 | -44.80518 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd22c31b-1574-302e-b8a5-8ab50d45c890 | -9.41814 | -54.71738 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a0f9a5-0f50-3f9e-81e5-d29dd53bf0ca | -7.51435 | -44.30116 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee3094bb-8f6e-31b4-84d4-a438c1b6eb69 | -9.05731 | -46.70873 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a4bd973c-15a3-3303-80bd-a23fa77ec559 | -6.75657 | -45.6214 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67641094-2450-3750-aef1-93e864b077f7 | -8.26495 | -45.47451 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bf30750-27ff-3e60-a5df-d0efb373ad04 | -5.71511 | -42.86296 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d86d8454-9816-31a1-a830-9e4bff85f82d | -7.81869 | -47.00197 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a89782ef-9d6c-390a-a4e2-3f7e8af4d3b4 | -9.40576 | -54.70485 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 821c44b3-5b26-3e36-b725-0a1cf99a1de5 | -10.92178 | -45.7211 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aae7b2c3-2bd8-3bc2-b596-9170b0d21fa7 | -8.28341 | -45.49994 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fa2003bc-9659-3e3e-a18b-78b1c8d37f51 | -10.31534 | -48.20499 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7843575-d239-3b2a-bbec-9ea2684354b5 | -7.03019 | -45.18225 | 2025-09-29 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d85899bf-d2b4-314b-8000-a9da9cf999a5 | -7.86405 | -41.05714 | 2025-09-29 04:57:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 98d2a34f-d3f6-3628-aa56-ceb3b5ecec2c | -11.26267 | -47.19583 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7317a728-6601-3854-b97b-6bc0d659d4fe | -8.27908 | -45.49143 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 311cce76-015c-3e3f-8aed-80b4b6ca82f2 | -10.42487 | -46.15104 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfb0f1ff-3760-371a-855d-60d739baed83 | -10.82746 | -47.62736 | 2025-09-29 04:57:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a905e061-3979-3356-ae35-647d376f77c1 | -4.71009 | -41.9768 | 2025-09-29 04:57:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4146394b-e837-362e-a7f9-db48b3e8212c | -9.36052 | -51.4881 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cdb26a1-4f16-33a7-b9fb-31c4d7b65374 | -5.35514 | -43.6877 | 2025-09-29 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5155855e-bf71-3fce-8c60-40005a35eaee | -9.41128 | -54.71284 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5a644b6-2ba2-3987-a489-af4488c15232 | -10.60445 | -46.29305 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe2dea9a-7c49-37df-ad77-862ab10314d1 | -4.71503 | -41.98811 | 2025-09-29 04:57:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1ece441e-a80f-3cd5-b479-3ff17e2af47e | -9.77763 | -46.94056 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 48534a9a-e63b-390f-addd-6104d2469610 | -9.41868 | -54.71391 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1624af7-9fae-39ec-91af-1b67b2ae5b8d | -7.24724 | -43.01087 | 2025-09-29 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a2a7daf9-6aa3-3604-8384-a3e5df9e5ec6 | -9.28058 | -45.69722 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe21b5b0-2145-3bb0-95bf-1e6120e8df22 | -8.2998 | -45.49954 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 89ea64d6-2d45-3aa1-8d50-d5ed64cdf100 | -7.22551 | -44.77421 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b188c714-9e92-36e4-be4f-a34f37a6ee06 | -8.30262 | -45.47826 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README64.md)
