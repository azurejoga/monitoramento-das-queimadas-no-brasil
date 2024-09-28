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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e2cfe0f-feff-3a6e-b40d-01aabbae1c54 | -21.40629 | -47.76819 | 2024-09-28 05:27:00 | AQUA_M-M | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 32bad4ac-c14f-37fd-abb9-d966777f9849 | -20.57506 | -46.25354 | 2024-09-28 05:27:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e7e124fe-5ab3-362a-a16f-8561b021eba1 | -20.5646 | -46.25197 | 2024-09-28 05:27:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f243fb37-19b4-3df5-a1b5-8208c5bba59e | -20.56284 | -46.26594 | 2024-09-28 05:27:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b85e1c0e-8901-3bc5-be3e-665eee5cfd49 | -20.55421 | -46.24986 | 2024-09-28 05:27:00 | AQUA_M-M | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b42cbad5-b4bf-374b-b0bf-34323ee30d2f | -20.14802 | -46.56413 | 2024-09-28 05:27:00 | AQUA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 951ccdc9-72e0-3414-b652-e52824f550d2 | -20.08503 | -47.66693 | 2024-09-28 05:27:00 | AQUA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| befd9db2-106a-3d32-b7c1-0babd0a6901d | -20.08356 | -47.6779 | 2024-09-28 05:27:00 | AQUA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 12a6aa53-ac63-36db-afdd-4d473d989e8d | -20.07834 | -42.01343 | 2024-09-28 05:27:00 | AQUA_M-M | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| bead3e6e-62b1-3b64-8d7e-b38909cbbfed | -19.63946 | -45.89685 | 2024-09-28 05:27:00 | AQUA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 10d3a29e-8680-34eb-ac23-76acc517f460 | -19.51962 | -44.10572 | 2024-09-28 05:27:00 | AQUA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e6cb62e4-7753-3df1-bbc5-af7bc9c534b2 | -19.50961 | -44.08562 | 2024-09-28 05:27:00 | AQUA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a0a15a92-11ed-3588-a4b6-4070b5786327 | -19.50751 | -44.10421 | 2024-09-28 05:27:00 | AQUA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 8aa49a7d-795e-3b1a-af34-e3333bc53550 | -19.46159 | -49.11072 | 2024-09-28 05:27:00 | AQUA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d0030ca6-d145-3622-bf83-9de96d4d2643 | -19.36609 | -42.56982 | 2024-09-28 05:27:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| a4408b22-f5e9-3638-be70-c8b0a74e3cb5 | -19.36327 | -42.59559 | 2024-09-28 05:27:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 0622f710-6b6d-3868-862d-e678c38f7efb | -18.78942 | -41.6097 | 2024-09-28 05:27:00 | AQUA_M-M | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| e8123970-f3c3-3ce4-97b9-5a7a44a41399 | -18.05068 | -44.38348 | 2024-09-28 05:27:00 | AQUA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f7a258a6-cf0e-3f60-af85-e85c54f6d270 | -17.85094 | -45.89053 | 2024-09-28 05:27:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 3520c7b2-3f99-33ab-9388-873d6d4839fd | -17.84931 | -45.90315 | 2024-09-28 05:27:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 152.6 |
| dd70ff75-1243-3b55-955f-d5464e5e88f1 | -17.84062 | -45.88911 | 2024-09-28 05:27:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 8e94e51e-e550-31f5-807e-138881c72d0f | -17.83901 | -45.90163 | 2024-09-28 05:27:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 36.3 |
| e012a517-c253-31ff-82d0-f622d7ea2edc | -17.72877 | -46.81878 | 2024-09-28 05:27:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8a00c8be-b4ea-3e2b-b758-0b9caf90e21b | -17.72726 | -46.82996 | 2024-09-28 05:27:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d8861fbc-eea8-3863-9adf-a052ac9d9869 | -17.11928 | -56.19324 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 3c4fdcdf-3b26-3ea0-846b-391b8e6e6282 | -17.11548 | -56.20855 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 8ff2ab9b-58c4-38cd-a6be-b657ec2c69dd | -17.10653 | -56.19073 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| f50e676f-0700-3840-8e52-c0fd508e033c | -17.10641 | -56.18558 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| fc0fa552-ffa8-38d1-b378-b38cd49c1dde | -17.10272 | -56.20599 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 85d20445-08b4-3894-8d4d-1af7741dfd64 | -17.1027 | -56.2111 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 4206a221-4e30-3553-8eae-aea950ff22e1 | -17.08997 | -56.20344 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| ee742187-6d76-323c-9df2-1660845f0a05 | -17.06295 | -56.13491 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| d5e3cb31-c153-32a7-8071-1cd99b86a340 | -17.01725 | -56.16787 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 60d5c568-fe98-3f08-8014-cd59902f5f7a | -16.73814 | -55.8127 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 5e2892fc-0618-379d-9dab-31f0b083d7f0 | -16.73785 | -55.81994 | 2024-09-28 05:27:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 124939d4-097d-3a40-bb0a-79ac51bb26fe | 3.12579 | -61.18164 | 2024-09-28 05:57:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d594cb0-bf0d-306a-8a0b-2215dd7454b8 | -9.95088 | -60.23932 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 665fae65-3399-360d-8985-65b26f094842 | -9.94547 | -60.23782 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a26c2a9-5d53-3090-adfc-c015be2ff2c4 | -9.94504 | -60.23852 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e81f370-4ed6-3de0-a9e6-ad239f90f320 | -9.92936 | -59.93754 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d595201-11ec-3ac8-be1b-67a97b3b3f9e | -9.9234 | -59.93673 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7708042-4a0f-3f06-a306-80b56c509101 | -9.92287 | -59.94109 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 34480d85-671d-3980-a6bc-98222016ef47 | -9.9207 | -59.9095 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5bb10106-ddea-381b-933a-484fc4bc949a | -9.92016 | -59.91387 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 53b84023-1999-3d30-a4db-e9f97a07573a | -9.90808 | -60.73085 | 2024-09-28 06:01:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 505446b0-e4bb-3048-a08e-e69c3d519d7a | -9.90242 | -60.73011 | 2024-09-28 06:01:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19a296ea-9920-3647-8393-dddd2f83df3c | -9.82133 | -60.4757 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20106c34-ed3c-336a-bde8-72ca47783830 | -9.82083 | -60.47976 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 515cd2e3-641a-3872-9eb7-9aa80bce7043 | -9.82008 | -60.47559 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb573cde-a359-333a-abde-4ae3940f4355 | -9.81955 | -60.47963 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 949c7c3e-456a-3a4b-b63d-bf4ccf00f31f | -9.8151 | -60.47886 | 2024-09-28 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae7a9fc7-ff09-3e26-be63-de4463e42057 | -9.69124 | -58.19236 | 2024-09-28 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1bae4e3-0964-34ba-a83a-a5f870faee47 | -9.60583 | -68.6207 | 2024-09-28 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6657edec-7c6a-37bd-a9ca-821eeaa6ed19 | -9.55099 | -68.26256 | 2024-09-28 06:01:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 623c0889-76ce-328a-bbb0-8e7093ce03a7 | -9.42057 | -63.42445 | 2024-09-28 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 604bc241-3924-3875-b71e-187d3d6a4310 | -9.41992 | -63.42942 | 2024-09-28 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80e892a8-7e93-3734-a38a-9ba4730f4d4a | -9.41777 | -63.42643 | 2024-09-28 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d200ca50-b887-33d8-b415-ea0b894807d1 | -9.41708 | -63.43138 | 2024-09-28 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 736edade-362b-3fa6-8fe7-e701570e5296 | -9.37306 | -62.33253 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 217eb615-3480-3aaa-bdf6-6a551f4ed03e | -9.3516 | -63.80135 | 2024-09-28 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39605e89-9ebf-3ee4-9d50-1ce1204fdd18 | -9.29413 | -57.16164 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7fc18dd5-bf36-3d58-aa94-2b3a36ab5d85 | -9.28387 | -62.31347 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc955c20-365a-33bf-a878-9779543db419 | -9.28349 | -62.31638 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b90c2a6-7dc3-3637-8406-aea1c628a004 | -9.2463 | -68.31001 | 2024-09-28 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7f4e96f3-1b25-3af8-afc8-d716c2ff8329 | -9.24283 | -68.30949 | 2024-09-28 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aa60943c-eef3-323b-bfa6-1f0d4cf0b3d2 | -9.23759 | -60.49516 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a86e0cf9-1cb9-3a9d-b506-b299fa1ad650 | -9.19195 | -68.29372 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d086ec45-9612-37ca-a348-8fc48e97667f | -9.19137 | -68.29758 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 377c4a2a-68a5-36af-8023-c15e0c0c136a | -9.18791 | -68.29704 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3f2d555-39a2-3e13-9eae-41dade010d27 | -9.15737 | -58.89897 | 2024-09-28 06:01:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0f997f0-ba96-328d-913e-b6c980aabc20 | -9.15594 | -68.16586 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fc62c34-85ed-333e-84f7-f5fb7c0ae28d | -9.15245 | -68.16531 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b126968-288f-3d13-bcd7-7dfa475cd55f | -9.1511 | -58.89786 | 2024-09-28 06:01:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64de16c0-0358-39d1-8462-e7f1bf77467a | -9.11832 | -67.88564 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e53e7bca-70d8-34d4-98b7-4d08310d6f50 | -9.11817 | -67.88903 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f441f7ff-47a6-3261-980c-fa1cd9f97d20 | -9.11771 | -67.88964 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 152e8018-23e6-32ee-9c60-6d1a216312a4 | -9.11758 | -67.89304 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66486cbe-c2ac-3291-8d30-b1b77d58dbfc | -9.11711 | -67.89365 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba6c191a-e474-345f-bcbf-5b8e7e35a671 | -9.11699 | -67.89705 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7c95808-2b18-30bd-aefe-d118a08b2303 | -9.1165 | -67.89764 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae3b43b1-dca5-35ea-be7f-7b859ed5f7a0 | -9.11522 | -67.88448 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14ac2279-961f-3b51-a3c8-405ce99b71c6 | -9.11479 | -67.8851 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8be7675-b6c3-38c0-9968-e9dd448c2c25 | -9.11464 | -67.88849 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa3a81c9-a0ff-33a1-aa1e-2d68a1454f6f | -9.11418 | -67.8891 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8724e7a-7dc2-37c5-8983-11c934ce2626 | -9.11405 | -67.89249 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54685b0f-0527-3e83-a726-42ff1d8f2cef | -9.11358 | -67.8931 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a8ff6e4-5e2c-3258-af19-7fed318a0467 | -9.11347 | -67.8965 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1434d4f-3c18-3395-b9bb-ce5e733cd7f0 | -9.11297 | -67.8971 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c41af160-52aa-37c6-8aed-e32ee987e718 | -9.11065 | -67.88857 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f7ccce0-3ae9-3a8a-bf8a-66624465cfb8 | -9.11005 | -67.89257 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa1a479a-12e1-3068-b8c2-6fe3693d3934 | -9.10945 | -67.89656 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6579eab1-1537-3ef8-aa2e-cbc9041cd158 | -9.10884 | -67.90057 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8b7049c-5db9-3b00-98b2-3e846221b2e0 | -9.10652 | -67.89203 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e75b08b3-e4ab-3936-b9f4-872cb02f17dc | -9.10592 | -67.89603 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49072f9a-cf8d-3f39-8009-8c750dd82f1e | -9.10532 | -67.90002 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44f1a0ef-b762-3630-a935-599d10c2112d | -9.10397 | -67.78884 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2ff5837-d45f-3613-a487-a4e175ba5440 | -9.10239 | -67.89548 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c342458-ef60-38b1-9548-e48ace60c0f7 | -9.09407 | -61.12929 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e083fece-f13d-3736-89c1-89b456064f4e | -9.09362 | -61.1328 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5b01203-d03b-39bb-98cb-260fd9ecee3b | -9.09227 | -61.13195 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README99.md)
