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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c7afb8a-803a-3458-9a65-9cd68138de70 | -16.18504 | -42.19758 | 2025-11-04 04:33:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0223b308-d52f-3d0f-b1d0-e0f99f5470e4 | -16.25831 | -45.5571 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d88a332e-744d-3269-9a77-9c083927347f | -13.43017 | -44.11285 | 2025-11-04 04:33:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ed1b526-6340-34f7-8e18-070bfce6b7ee | -16.26451 | -45.57999 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2dde9ad-37ca-367d-8528-91e217476226 | -16.26651 | -45.56496 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd1ae7db-a11a-306d-bc85-0cca07c17545 | -12.22416 | -41.49415 | 2025-11-04 04:33:00 | NOAA-20 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34eae137-8f98-33f6-b769-c163e952f8d2 | -11.28089 | -41.74471 | 2025-11-04 04:33:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1c6315a4-dca8-3d5d-a811-6bb527878268 | -16.26584 | -45.56997 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb00accc-ae2d-300c-b81f-ba27f7e82301 | -17.50232 | -44.49565 | 2025-11-04 04:33:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fec46ca-5589-3e44-96f9-0e8ff3ea43ce | -10.93951 | -44.19208 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb434c39-107b-39c3-95b9-e1c675eb48ca | -15.78826 | -41.47004 | 2025-11-04 04:33:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e3c0771-eb07-37c8-8f98-10c518658a02 | -16.0206 | -42.90282 | 2025-11-04 04:33:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fff0986-1498-3f29-afa8-f9bacca9d2cf | -13.43037 | -44.11288 | 2025-11-04 04:33:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b1a9189-de28-3b26-a936-9f2e6f3d4be8 | -10.93877 | -44.19712 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 798d6ed7-3335-320b-b716-be7882aa30c5 | -11.72709 | -44.75003 | 2025-11-04 04:33:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7965bf89-b4f5-396a-9965-857686152ba8 | -10.93559 | -44.19152 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e26d072-61b8-3aa1-b520-b471d25e4e50 | -12.44553 | -43.85651 | 2025-11-04 04:33:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f192a17-8a8e-3962-a16e-0314c2d74dc9 | -12.01516 | -43.84956 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d54dce4f-760f-3178-94f1-4c16157cdb75 | -16.42446 | -55.96001 | 2025-11-04 04:33:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9a287b03-7d8e-31ca-8fb0-082686571cd7 | -10.9324 | -44.18591 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dca0622d-74da-3ed3-8b1a-d2fdd164434e | -10.86822 | -44.40973 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7a7d927-c896-31d9-969d-9d0ebd5ddd05 | -10.93167 | -44.19096 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21d44982-9a49-30e8-a1c9-d3bd8b5aaa45 | -16.42522 | -55.95603 | 2025-11-04 04:33:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0485b7f8-e75d-3207-a92e-29e43a7435cd | -13.31647 | -42.41881 | 2025-11-04 04:33:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 10623b28-6cc1-3146-84ad-016f04a017e5 | -10.93911 | -44.19393 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fd65d475-9a11-329b-89fe-76397bcc2a78 | -16.27477 | -45.59167 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae996795-5a45-3407-a681-52cdea975fa4 | -12.01465 | -43.85322 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1910e2f5-b3f0-3957-881e-5b0319e7aae2 | -11.84143 | -43.72756 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e0bb0b6f-ac35-3e13-827d-ba722e5198cd | -15.78323 | -41.46935 | 2025-11-04 04:33:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c485a99-68ae-33f5-856f-5fc7780b2433 | -16.42426 | -55.95699 | 2025-11-04 04:33:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 16fb41e8-1083-3f3b-84aa-7975535358b2 | -12.44502 | -43.86021 | 2025-11-04 04:33:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8355d013-7321-3ccc-b63a-f4e9e8c442d3 | -16.26517 | -45.57498 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3f69288-8141-3e6f-b47f-ddac4e7ef837 | -10.93804 | -44.20214 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3d8b9b4-eabb-342c-a146-6b8cb1bc2d15 | -11.68354 | -41.12589 | 2025-11-04 04:33:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1d9fa25a-d098-31e7-bf9e-bd97208d5a39 | -13.32193 | -44.47993 | 2025-11-04 04:33:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b75f1e19-cf7e-3d67-b3a1-9c619ad1e5ba | -11.73092 | -44.75059 | 2025-11-04 04:33:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6553d3b1-1b62-37bb-91ef-03e1ba1a969f | -16.74787 | -41.69304 | 2025-11-04 04:33:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7e1d43e1-10d1-39b2-9602-9c0f20b31fa1 | -10.94196 | -44.2027 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aa9d6fb-5498-357c-9b3e-019ea368d841 | -10.86435 | -44.4092 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4884528-eaa1-3bda-bddb-c380f69bbba8 | -13.32043 | -42.42392 | 2025-11-04 04:33:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ef579526-686a-30fd-804a-97aec6f171d2 | -15.31867 | -42.04392 | 2025-11-04 04:33:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 37516117-ef1b-35f2-8017-6e985bb3d0dc | -12.01872 | -43.85382 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 589e656b-f182-3f2a-8040-4e76085d64d7 | -11.72984 | -44.74763 | 2025-11-04 04:33:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b8cc8f9-1f37-37fb-9816-2f07cc1000da | -13.31585 | -42.42344 | 2025-11-04 04:33:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 918e10eb-bf91-3427-b915-d076cd303a69 | -10.93519 | -44.19336 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d4877229-6ac4-305a-8af7-a0a805dac9cb | -10.93197 | -44.18774 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0e4353e-6da5-3171-aa29-e38e90bdc162 | -16.26148 | -45.56266 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e864bfa-63fa-3c29-89c5-f4099d413917 | -12.01923 | -43.85016 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2073cfd9-8b13-307b-ad24-eae36911cc23 | -15.30319 | -42.97894 | 2025-11-04 04:33:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4da95d45-aabf-3d23-b50a-5502674a2f46 | -10.94269 | -44.19768 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e19529d3-acc2-3530-9dea-e1bedb196bf3 | -10.93589 | -44.18832 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0c530a7-5714-3277-9e97-7febd9805a85 | -11.73326 | -43.84598 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b035e665-46a2-3645-a8c8-f042d85a9ad5 | -16.74752 | -41.69592 | 2025-11-04 04:33:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 78d65164-dd3d-37bf-ba63-4b1e2b24c149 | -14.74716 | -42.79548 | 2025-11-04 04:33:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c1b1082c-2961-3713-a1d0-fe8be1121ed1 | -16.26264 | -45.56438 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fd794c2-5615-38ac-a1ef-f46caa8ee08d | -11.84091 | -43.73125 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f690c313-2282-3778-b6d4-63c1af38a172 | -11.73378 | -43.84236 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b46bcdd-ee86-3d30-84f6-6edfd5acc26d | -15.31955 | -42.0426 | 2025-11-04 04:33:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24a47c06-f034-3090-9989-e8c2654cbafa | -11.11025 | -41.62582 | 2025-11-04 04:33:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 026f8361-5a85-3970-9806-4faeb0fbb008 | -10.94233 | -44.19954 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ecf0cfd-b6d8-3932-a96a-7f0afd66fff2 | -11.83735 | -43.72697 | 2025-11-04 04:33:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af7d63b1-f3bb-31d4-8206-2116c0cfbda7 | -16.26838 | -45.58055 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee147801-0c60-35a7-a1ef-8b7c1dea10d1 | -17.50283 | -44.49162 | 2025-11-04 04:33:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04f10b7a-f654-369e-8aa6-c84b7d06ca3d | -10.93127 | -44.19279 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c186611-340d-3ec1-8e8e-0e016d9e391a | -12.72649 | -43.44094 | 2025-11-04 04:33:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a574842-9012-33f1-b2d3-114dba168bda | -10.72857 | -44.01769 | 2025-11-04 04:33:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d4c1d41-c2c8-3477-82a2-d81c876d02ff | -13.32119 | -44.48525 | 2025-11-04 04:33:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 715de929-1a46-33e0-9cb9-8f08fc429f83 | -11.68232 | -41.12218 | 2025-11-04 04:33:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b2c8c48-791c-3f61-acd7-f5b21e28593d | -15.79246 | -42.02789 | 2025-11-04 04:33:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9552c1f3-a0bb-318f-a568-7243d30e4df4 | -11.14387 | -44.02201 | 2025-11-04 04:33:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbb33bb8-855b-3037-bbf2-3c297a3c926b | -13.60111 | -43.56667 | 2025-11-04 04:33:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d470770-8d70-38f0-8a78-07b096953002 | -10.93771 | -44.204 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f595748a-a17c-3730-85a4-b7e8c2a07b5e | -17.49812 | -44.49505 | 2025-11-04 04:33:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54eb5226-6e54-342c-865b-cdd57e6c8615 | -16.25944 | -45.5588 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6860fd41-f466-3bea-8507-769975e56814 | -10.93841 | -44.19897 | 2025-11-04 04:33:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff5a464a-1925-3c7f-a156-294e3bf29e30 | -16.26331 | -45.55936 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57a7c61b-ce63-3c0c-af2f-e9b2fe032413 | -16.26771 | -45.58555 | 2025-11-04 04:33:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 746942c3-3cb7-3377-b69c-ce7caf23675f | -18.76707 | -42.84244 | 2025-11-04 04:36:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ba738d4a-84d3-3205-9274-9f04f7cde683 | -20.17232 | -49.68209 | 2025-11-04 04:36:00 | NOAA-20 | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9302e7a1-f430-3542-b142-717f9839b9bd | -20.32771 | -54.36791 | 2025-11-04 04:36:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3982a758-343b-3ed3-a068-952ec4d28a94 | -20.09712 | -51.15662 | 2025-11-04 04:36:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f83f5e1-9cee-3869-ace6-782c3e756c93 | -19.17955 | -54.85374 | 2025-11-04 04:36:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02b2a532-dbfd-3ad5-a7b2-bba16d366d92 | -20.64312 | -52.87752 | 2025-11-04 04:36:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 299048f9-9c44-3948-a3f8-617daabb2896 | -20.32412 | -54.36723 | 2025-11-04 04:36:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 656f0819-9bca-3152-bc44-88ecce43ec65 | -19.97276 | -57.23441 | 2025-11-04 04:36:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b00d566a-df57-3c51-9110-90e2d62745a2 | -30.14982 | -55.85833 | 2025-11-04 04:38:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 04dc8ca9-e4cf-35e9-ab48-c6c59d7f9bfb | -29.72994 | -53.87439 | 2025-11-04 04:38:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 9e0283a1-d925-3a9a-8d6c-fd2eee61b7af | -27.69117 | -51.21952 | 2025-11-04 04:38:00 | NOAA-20 | CELSO RAMOS | SANTA CATARINA | Brasil | 4204152 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f828d8c6-1015-39a1-ba93-24d5312e2b5c | -3.4386 | -50.2368 | 2025-11-04 04:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5397de10-6ee7-3380-9c93-d8126b26ff15 | -3.9139 | -47.697 | 2025-11-04 04:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1fb1d12b-38f4-3539-bd47-13c14fa09fd2 | -3.4386 | -50.2368 | 2025-11-04 04:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| b8b8fb05-e46e-3094-bda7-1e982823cc07 | -3.9139 | -47.697 | 2025-11-04 04:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1ce39e3e-dc95-376b-903f-7010eee68afa | -3.9139 | -47.697 | 2025-11-04 05:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| a2bada39-ed34-3801-b7a1-ae538d2b6934 | -3.4386 | -50.2368 | 2025-11-04 05:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| fbd1f8c7-4618-3726-a588-ccb795223b64 | -3.9324 | -47.6962 | 2025-11-04 05:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 63050a60-fd01-3041-b94d-9bf94cae28c2 | -3.9139 | -47.697 | 2025-11-04 05:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 764c9545-dc4a-318d-81c4-43bca537e93d | -3.4386 | -50.2368 | 2025-11-04 05:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 16ce6050-ebbf-3604-85e4-3d402723661d | -3.9139 | -47.697 | 2025-11-04 05:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f7bdee34-5b68-3b49-bb4b-bcfa6d7a14df | -3.4386 | -50.2368 | 2025-11-04 05:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 48a664c9-3f33-3e37-94e1-268e93151f08 | 1.08638 | -60.31938 | 2025-11-04 05:20:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
