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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 837283f5-6471-3147-9f8f-50b3871a1468 | -14.2347 | -44.158298 | 2024-10-12 00:22:06 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3cf5358-cafc-309f-b9e0-708c8352046f | -13.4639 | -40.834801 | 2024-10-12 00:22:07 | METOP-B | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 17637fbb-99f0-344b-b6cc-372699828d7e | -13.4659 | -40.843498 | 2024-10-12 00:22:07 | METOP-B | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b06408fc-37b8-3852-9409-7bc65f3f1121 | -14.0793 | -43.690701 | 2024-10-12 00:22:07 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9e9149-c721-3472-a04e-92ce155b91cc | -13.8815 | -43.773899 | 2024-10-12 00:22:11 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a27f540-976c-32ee-a54d-d5beef12eb5b | -13.8831 | -43.780998 | 2024-10-12 00:22:11 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87aebeba-7fa9-3169-9a6f-2ce4fa4a0740 | -13.9396 | -44.034302 | 2024-10-12 00:22:11 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17a8fd8d-8078-327a-852c-8a983d67ae6f | -13.9411 | -44.041401 | 2024-10-12 00:22:11 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61cae4f4-96a4-3f5c-a0b9-f6f5b4823651 | -13.493 | -42.964699 | 2024-10-12 00:22:14 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 65e48a2e-9bf3-3bd8-8338-bd3d78540789 | -13.711 | -44.257 | 2024-10-12 00:22:15 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d4479d47-eae1-3691-8c61-12505efcbbef | -13.7125 | -44.264 | 2024-10-12 00:22:15 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a89b54af-c1ab-3110-aaa9-b70102ea8c71 | -13.2271 | -42.343102 | 2024-10-12 00:22:16 | METOP-B | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fe7f33af-31b9-3fe8-9714-87437cf4d754 | -13.2288 | -42.350601 | 2024-10-12 00:22:16 | METOP-B | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d9433b24-800b-35d5-aa3a-edaa0c73368c | -13.2173 | -42.345402 | 2024-10-12 00:22:16 | METOP-B | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cf39e213-bc25-38c0-9c9f-56c492631f82 | -13.1927 | -42.959202 | 2024-10-12 00:22:19 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3f5a986b-c58e-3c8c-81a1-60e64c4b7c71 | -13.1943 | -42.966499 | 2024-10-12 00:22:19 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 112af1d5-0a85-36db-b05c-57c9c0ed63fb | -13.196 | -42.973701 | 2024-10-12 00:22:19 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 713b6d58-fd7e-3e41-925b-0d84413987f2 | -13.5074 | -44.4072 | 2024-10-12 00:22:19 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74360f28-3ff8-3838-8b4e-eb49b76811a4 | -12.88 | -42.449799 | 2024-10-12 00:22:22 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 64ec808a-4cf7-315c-a6ac-87cb786107b5 | -12.735 | -42.492199 | 2024-10-12 00:22:25 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a89d99f6-503b-3eee-b4cb-98de28d62ff7 | -12.7834 | -43.291199 | 2024-10-12 00:22:27 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c3a5b21-6a55-33c7-81d8-9f008a8c22cc | -12.785 | -43.298302 | 2024-10-12 00:22:27 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8916dc0d-00e9-39ee-9246-9331cc789ed4 | -12.7866 | -43.3055 | 2024-10-12 00:22:27 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 70882204-3305-3ce1-b9c8-9b59157b697e | -12.7674 | -44.1357 | 2024-10-12 00:22:30 | METOP-B | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9035337f-f4ac-33e5-8560-4d2ec1977fb3 | -12.769 | -44.1427 | 2024-10-12 00:22:30 | METOP-B | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 830c448b-4964-376d-93bb-172f4f6f0ca2 | -12.8006 | -44.841599 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8dc2f67f-c792-361a-91f2-425051b15159 | -12.8022 | -44.848598 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9532e6c9-5beb-36b6-b217-859210eff522 | -12.8052 | -44.862598 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99bcb9a3-1473-3144-a198-3f28bef5012e | -12.8068 | -44.869701 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfe72ac7-d63a-3c51-be5a-b67d91f29177 | -12.7908 | -44.843899 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bac17271-ec89-325e-a48f-2e1de9cc942b | -12.7924 | -44.850899 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 807dbf92-daa8-3f4d-a1a1-3e3e59802fce | -12.797 | -44.872002 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 707e19b8-6739-343a-88cb-08f8bcf32bfc | -12.7985 | -44.879002 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86e8ad53-6e43-33cb-b03f-a1b8db0eb58e | -12.781 | -44.8461 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32874f10-4f6a-30d4-ba1a-670204ee077d | -12.7826 | -44.8531 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5037a2c0-3770-36f4-b3d0-a92b6b195fb6 | -12.7841 | -44.8601 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 088eaaa9-ce00-35cf-881f-85b21e67bdc1 | -12.7856 | -44.8671 | 2024-10-12 00:22:32 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dbf9f0b5-4505-32d3-b5d4-c4772eb6b362 | -12.3673 | -44.051102 | 2024-10-12 00:22:36 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50e7fe91-e41b-37bd-949b-040c53261786 | -12.2526 | -43.588001 | 2024-10-12 00:22:36 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57aa27a2-a322-3899-aabe-3412a4d30d53 | -12.2542 | -43.5951 | 2024-10-12 00:22:36 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 668a7f55-cbb5-35fc-bc25-d71b527af752 | -12.2955 | -43.8237 | 2024-10-12 00:22:37 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e59bd5de-ac11-3ef3-8833-2bb6f6aa0772 | -12.2971 | -43.830799 | 2024-10-12 00:22:37 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95d47fe4-ac46-38f1-aacd-6062c4ef5a1a | -12.0543 | -42.943001 | 2024-10-12 00:22:37 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 17698dc8-b3b9-3597-8d9e-d688378a5198 | -12.056 | -42.950298 | 2024-10-12 00:22:37 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2de4fd2b-69e5-3cf1-886b-45f86772d6b7 | -11.7986 | -42.058201 | 2024-10-12 00:22:38 | METOP-B | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3f3bee23-1ab4-37a6-a576-3dcc863d2b85 | -12.3108 | -44.351002 | 2024-10-12 00:22:38 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2165187-3e90-33f5-99f7-45936a013e44 | -12.0718 | -43.472599 | 2024-10-12 00:22:39 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66dd08f5-3ab8-3031-82f9-f864512f3b07 | -12.0637 | -43.481998 | 2024-10-12 00:22:39 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc719360-327a-3720-aa2f-55dd472936ed | -12.0653 | -43.489201 | 2024-10-12 00:22:39 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eef7f9c7-7eb0-30ce-a451-120271e30b9f | -11.9951 | -43.9081 | 2024-10-12 00:22:42 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a114898-a68c-304e-bc1f-3888c8b52af1 | -11.8907 | -44.637901 | 2024-10-12 00:22:46 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b50ac8a-b900-3493-9c4b-5cac2eeb7d77 | -13.2444 | -51.094898 | 2024-10-12 00:22:46 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 667490c2-f798-3b2a-abff-faa2d594fbb0 | -13.2347 | -51.096901 | 2024-10-12 00:22:46 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12f93722-0b19-3f53-bfba-a2903464182f | -13.2249 | -51.0989 | 2024-10-12 00:22:46 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 082f4bce-3bf9-3be4-9a50-7f078253507f | -12.5984 | -48.598701 | 2024-10-12 00:22:48 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9699c048-7d98-3368-8c88-1d5b34463748 | -12.6003 | -48.608101 | 2024-10-12 00:22:48 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29b43c69-99da-3e4e-9b2e-75df898f67f1 | -12.2241 | -47.110298 | 2024-10-12 00:22:49 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97c95ec1-84b7-314d-9e1b-67c52b015dde | -12.2258 | -47.118198 | 2024-10-12 00:22:49 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e4750e8-74fc-3875-8315-f02058fc4a8c | -11.4716 | -43.917999 | 2024-10-12 00:22:50 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9572b3e2-e2af-3bbe-845f-92d02f25f9ab | -11.4732 | -43.924999 | 2024-10-12 00:22:50 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6803121f-730c-3aa4-b4a5-c9173b5d4a40 | -11.4603 | -43.9132 | 2024-10-12 00:22:50 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e06fcb8c-773c-380c-ae44-6aa95c6aa08f | -11.4619 | -43.9202 | 2024-10-12 00:22:50 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7fde1647-e2d4-39e8-881a-e0e1fc92d528 | -11.5916 | -45.0061 | 2024-10-12 00:22:52 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b21f3d48-27ab-3674-8e52-54ec10659649 | -11.5931 | -45.013 | 2024-10-12 00:22:52 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de5f7fa6-ad84-302f-9e8a-912ee3825b69 | -10.8486 | -42.858898 | 2024-10-12 00:22:56 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 369ce55b-31ea-34f0-b11a-dac4f5924b6b | -11.1345 | -44.941601 | 2024-10-12 00:22:59 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7bdf246-bb93-3199-b0ec-959119ae7505 | -10.944 | -44.6418 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba38de6a-5a89-328b-8238-7169c04911ea | -10.9652 | -44.644299 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4f529a0-f4fb-3857-8260-ef69ad54f3f4 | -10.9667 | -44.651199 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9c22281-8783-3d99-9834-a57e83bd5e38 | -10.9683 | -44.658199 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27d41b7f-5dba-335e-81f6-67e86322ba44 | -10.9523 | -44.632599 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e583993-db15-3b14-a45d-f73bdc830e14 | -10.9538 | -44.639599 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e51ce2e3-edc3-3cde-abbc-e1c316c4b0fc | -10.9554 | -44.6465 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 934ef0fa-6b15-3702-b9a4-037a75367fc6 | -10.9569 | -44.6535 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65be1632-05df-366c-91cc-a5ea18ee8244 | -10.9425 | -44.634899 | 2024-10-12 00:23:01 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9a299843-ac56-3753-a58f-72504a9f3972 | -10.8435 | -44.423401 | 2024-10-12 00:23:02 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 432aa827-7155-3cb0-80c9-c22c974a0450 | -10.8451 | -44.430401 | 2024-10-12 00:23:02 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc2ca914-d438-38a6-b8d5-6778d9b4af0f | -10.8467 | -44.437401 | 2024-10-12 00:23:02 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ddce596e-a9cf-3f1d-a15a-02eee1375637 | -11.5074 | -47.307999 | 2024-10-12 00:23:02 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e105dde-5eb7-3322-977d-1fe83a32a6b7 | -10.8333 | -44.929699 | 2024-10-12 00:23:04 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03f19a3a-1769-3e7c-a6e9-34cbd096f0f3 | -10.8348 | -44.936699 | 2024-10-12 00:23:04 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3313d7cb-cb88-3719-8f17-e647a6640f2e | -11.3443 | -47.073898 | 2024-10-12 00:23:04 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d9fde74-7565-333f-8705-a327ad68606b | -11.3459 | -47.0816 | 2024-10-12 00:23:04 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c214ce19-1189-32b8-9d82-9b023fc61f50 | -10.8364 | -44.9436 | 2024-10-12 00:23:04 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7649d1b-2aa1-3a39-a4ef-f19667574f5e | -10.7382 | -44.688702 | 2024-10-12 00:23:05 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f69a1e3d-d72d-34f2-81e1-4e1848efb341 | -10.2157 | -42.442101 | 2024-10-12 00:23:05 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5819187e-1c6e-3907-8627-e862dc7fda5b | -9.6229 | -40.319302 | 2024-10-12 00:23:07 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 38724a54-c7b5-380a-b3e9-4098cbd36e3a | -9.6253 | -40.329498 | 2024-10-12 00:23:07 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1340fc9d-a91e-3f07-bb3c-521347f12333 | -9.6132 | -40.321602 | 2024-10-12 00:23:07 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8265d70d-fdc5-3a60-9606-695f90764c5d | -9.6156 | -40.331799 | 2024-10-12 00:23:07 | METOP-B | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b9eb0543-3218-38be-a40e-2e404b098981 | -10.6103 | -44.7616 | 2024-10-12 00:23:07 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90547078-ef5b-3593-9c53-dd4d518bffa3 | -10.6119 | -44.768501 | 2024-10-12 00:23:07 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 128bcf1f-e408-3c75-9ad8-dd5502d27aee | -11.2103 | -47.8377 | 2024-10-12 00:23:08 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdaeed03-01c9-3cde-9d0a-4ad1bd013727 | -10.2661 | -43.965801 | 2024-10-12 00:23:10 | METOP-B | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03c133ed-f799-366c-b73e-fad7b056841c | -9.6796 | -42.845501 | 2024-10-12 00:23:15 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88b3730e-aca4-31ab-9106-a186331521f1 | -9.6814 | -42.8531 | 2024-10-12 00:23:15 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 025d63d4-5c47-3a61-9451-3a95315f2c4e | -11.3228 | -50.885101 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 55e208cf-5d0f-3c3b-8fe9-5501ba73b1dc | -11.3254 | -50.897598 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7686f83-fbeb-31df-af78-39a60bef5739 | -11.3279 | -50.910099 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00b331ba-ca66-3e4c-b569-90989d32f7a8 | -11.313 | -50.8871 | 2024-10-12 00:23:17 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
