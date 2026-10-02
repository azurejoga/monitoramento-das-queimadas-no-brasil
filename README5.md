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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abee57e8-7d01-3bdf-8359-ff34adb8f85e | -10.529 | -57.762001 | 2026-10-02 00:48:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b80bb52e-ba8f-3e5c-8d7e-d9313bac5c1b | -5.851 | -53.489201 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 797e3ecd-9280-3b13-9959-7e96f2a08044 | -7.7427 | -54.807999 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb4c904-4c2d-3985-ace8-45e0b47b05df | -6.171 | -57.699299 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20b3aea1-1b8b-33e2-bc57-bfc063634032 | -6.7092 | -55.5826 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b34b98d-2344-301a-a9a3-0972c3bb5cb9 | -10.8215 | -51.123402 | 2026-10-02 00:48:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7dfbda5f-8c42-3960-bb29-9ef6555ea9f9 | -10.7972 | -53.774101 | 2026-10-02 00:48:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddb26d8-321b-3bd0-be48-cf4300987959 | -7.5557 | -55.019199 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c49caba3-913a-3882-84e8-50526617edbb | -8.2338 | -54.7906 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28099803-574f-3dff-8da4-6db2e810de55 | -6.5402 | -56.2686 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250c9b89-d36a-3839-a2c0-6ad610e9f458 | -6.5423 | -56.277599 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70cf8b26-b7e4-350a-837f-3942e8271fe4 | -4.2592 | -50.763699 | 2026-10-02 00:48:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b20a4e64-98fd-387d-a8b9-b0eb766b9b27 | -5.01 | -56.2939 | 2026-10-02 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d86e9057-f864-3e33-a66b-1e0dea38b47e | -7.3993 | -55.229599 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eedf5abc-8494-342f-a22c-9ef91675c4a9 | -7.5434 | -56.147099 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d85dd56-6b0a-323a-903a-a05b2495549c | -5.8998 | -53.521301 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 123a5f21-32b2-34a3-be64-3a0d5bb364ef | -5.8641 | -53.500702 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99c6689-944d-3bea-94be-d42fda7709ed | -7.2788 | -55.5923 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c45f857-af80-336a-947e-0eb9da34a9f5 | -4.4482 | -54.905998 | 2026-10-02 00:48:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20f6e707-32bf-3f3e-b6e5-c4166ef635f1 | -7.5509 | -55.042198 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c19ea88e-6c8b-360e-bef7-ab37f75d3555 | -6.3402 | -55.3293 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79f43ba2-0867-3321-9df2-267d17966b1b | -6.0675 | -57.607899 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf9d086-30ed-39d4-a292-93045441873d | -10.7875 | -53.7766 | 2026-10-02 00:48:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 905287a9-9895-39e4-bddb-56e787d1af7f | -6.4332 | -55.811798 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb77803d-17c9-328a-b570-7432d089a857 | -7.0564 | -55.654999 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8e2742-d076-3958-ab69-615c78e8e54e | -8.0606 | -54.843201 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c14a16d-1600-3b53-a389-764527d77d79 | -6.0329 | -57.681801 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed770ec3-5fc2-3ff8-b47c-78e12581707c | -8.2581 | -54.7626 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcfbd6f3-6d85-3cad-9f52-5ac29cd10593 | -5.3776 | -56.058399 | 2026-10-02 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 281a95bf-f0ff-3b56-b8ae-f74a9aba449f | -8.2634 | -55.698601 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84989559-e4c1-3c3e-9448-cbaed7cc8649 | -4.2798 | -50.8064 | 2026-10-02 00:48:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0f593f4-baf0-349a-b500-c39ed2a5d81e | -6.4977 | -58.537701 | 2026-10-02 00:48:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9e21ec1-4f3e-33b1-a1dc-9687d139955e | -6.0882 | -57.832298 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c719ac-59a6-3a80-952e-3fcbe0619043 | -8.253 | -54.741501 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72e7bab6-c59a-38b3-9f8a-d9ec24efd3f3 | -6.0791 | -57.613499 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbfc90ea-f304-3799-bb23-6be3c4e208c4 | -7.8192 | -55.129501 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51da41ca-4396-3cd0-ad43-c0fdfe4f2ec2 | -7.6838 | -54.7771 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56830287-94b5-3367-a3c2-b5f57a3254eb | -7.7453 | -54.8186 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3cd6d6d-9221-3fb3-a638-7d59a70f9fd1 | -4.2688 | -50.761299 | 2026-10-02 00:48:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bcc0097-5e2a-350f-af43-9363eacdcd7d | -4.451 | -54.917599 | 2026-10-02 00:48:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43cf61f8-da84-3fa2-96cd-0fbeeddb29b1 | -12.7811 | -51.397301 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14b84794-f4da-3ece-b84a-5bcd1673e4f7 | -7.5728 | -55.134602 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b448ad64-5c6a-3225-b297-59a6c7353e67 | -7.269 | -55.594601 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820243f1-d500-3d9b-9c85-575e7da86adb | -8.3018 | -54.729698 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1cf122b-b083-3258-b0f3-7dc73ea07fc2 | -4.2991 | -50.801701 | 2026-10-02 00:48:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 490651e2-db3c-3f12-ae00-e265d4901cfe | -6.1612 | -57.7015 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecdf45a3-b6d2-3501-a409-8b833a9a0644 | -10.415 | -53.773899 | 2026-10-02 00:48:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2304c45-d007-3f4c-bdca-b868585be7ea | -7.3286 | -55.235699 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9020daa6-4669-3d6a-8b2a-e94f06f2246f | -7.733 | -54.810398 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d9fbb1-da95-30a9-9b7e-553edbc2953e | -7.3969 | -55.219501 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58609680-3ed6-3165-bbf4-4ab0aa402040 | -6.87 | -57.733501 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe8dacdd-aa30-3fd0-bece-870898df1d54 | -8.0631 | -54.853699 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91ac1eb4-34eb-350c-8250-693a5091570a | -12.8096 | -51.4687 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c97c06f-ba4e-3adf-bfa1-5afda79754fb | -12.7871 | -51.379902 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4b0f757-3df5-3e4e-9f80-5e17363e13b3 | -7.497 | -54.989201 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e85ca51-bbfa-3665-b628-29e71b64a855 | -5.7424 | -55.767799 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122d6c9f-b1a9-330d-9387-55fe21c0c200 | -6.3161 | -54.791599 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9236c09b-420b-344b-bd0d-5a2cd371c3dc | -6.6995 | -55.5849 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 097a368d-2cd8-31f2-ad97-d2b2e62222e1 | -6.1755 | -57.7635 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6456383-1055-38fb-8eab-b4dd568bbdd2 | -12.8267 | -51.495399 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba74e478-4e0a-3ffb-9a6a-624eaf8949e5 | -12.8304 | -51.509998 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd1a6965-934a-34dc-9187-f17b2ae57772 | -5.1249 | -56.035599 | 2026-10-02 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e98061-18a1-3107-a282-1fef2b17415b | -6.1063 | -55.6931 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4168dd7-6571-3566-8f1c-ca788359d544 | -5.3753 | -56.048801 | 2026-10-02 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de477de0-8d37-3785-9dda-ff60ae343aa2 | -8.2089 | -54.729698 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa31c7f3-d83b-3c99-aa5c-aef4dfe2088b | -12.8133 | -51.483299 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e7b3976-df83-3d3a-85cf-906662522ecf | -4.2949 | -50.826401 | 2026-10-02 00:48:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e3b3a6a-e9e3-3ffa-b626-4817114cd1d5 | -13.1147 | -51.244999 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73d0362a-5e8a-38bd-a862-91408a9919db | -12.8177 | -51.4193 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59fd16d3-314f-396c-afe3-f4121b03219c | -7.5413 | -56.138199 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c69e08-5df8-3d82-b4c6-60ba616d5a88 | -6.0693 | -57.615799 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 477b8008-72d4-3a4c-9537-03f8440ea6c0 | -9.782 | -53.846199 | 2026-10-02 00:48:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce0c6ee-9f68-37d1-a360-42d7a53e9abe | -5.9715 | -55.383301 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e5d664-20df-3f76-8b11-2276f29508b2 | -5.9095 | -53.518902 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceee705f-c938-398f-bb11-e91bcf06a970 | -8.3043 | -54.7402 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d31197c-6cf6-3566-a885-e61bf1744f8d | -8.2064 | -54.719101 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03018299-69d8-37a1-a59b-2198b17eb840 | -9.7792 | -53.834702 | 2026-10-02 00:48:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df9fd598-3c95-37e8-8301-db979feb1b1d | -7.331 | -55.2458 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58a72a1b-4a1e-33ab-8e93-7c1762abc84e | -13.1089 | -51.2626 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9b8a9fe-feff-389c-9362-e39e270f2105 | -13.1224 | -51.275002 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6fc0c45-4fed-3e9b-85a2-8e4f5ee207b9 | -13.1186 | -51.259998 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d26bfe53-5883-352b-8d2c-1433305436bd | -12.817 | -51.498001 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 914e0b25-c383-3917-b364-a5030148982d | -8.5325 | -54.5728 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a28f4d9c-ab1a-3e96-b5f1-030b231db539 | -7.2833 | -55.611599 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51fe13ad-b5ef-3a0f-8fbb-7761b2215010 | -10.2491 | -59.028702 | 2026-10-02 00:48:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd5cacab-f2f6-3115-8c3a-2447d480918f | -8.185 | -54.802299 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ee0b68d-a5c0-3e7d-be62-62c9fb4b49ce | -12.8438 | -51.522099 | 2026-10-02 00:48:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f253a179-935f-3c12-8291-2729f560e4ec | -7.0443 | -55.647701 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c7a93ca-c7ea-3864-add3-64e302a4990b | -7.5582 | -55.029499 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 487784fc-3ea3-3e83-9451-d295b5e5e779 | -5.8674 | -53.5145 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50e0a06-848b-3c29-b8c8-01026f105558 | -8.1875 | -54.812698 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c72ba49-fe07-3962-8c8b-bc42ec2fe0aa | -5.9838 | -55.391399 | 2026-10-02 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a31c5708-a663-3047-836d-bc2c71079938 | -7.3945 | -55.209301 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 019110d1-7639-31d0-8f5a-251275c8b6ff | -6.0865 | -57.8246 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3fb3b3-7045-36d6-99ff-4ae7cb41c7aa | -5.8543 | -53.502998 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dae886a-bac2-329f-b72d-9753e06ee089 | -7.0541 | -55.645401 | 2026-10-02 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2dc2cf5-5e71-3836-9203-a4bde563446b | -8.5423 | -54.5704 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d93e8c9-f543-3a7c-a7ba-db7c411239c0 | -6.2476 | -57.763302 | 2026-10-02 00:48:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f197169-24fd-3648-b221-fbea310f08c9 | -4.2647 | -50.786201 | 2026-10-02 00:48:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a365e38c-5442-329f-b1f1-03431c48e936 | -5.8965 | -53.5075 | 2026-10-02 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
