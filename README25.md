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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 570923e2-b79e-3b46-bed7-3a7f7c686083 | -12.50021 | -55.73993 | 2025-07-18 04:55:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55229bd9-3369-39ea-8086-e566c9a7d962 | -20.04332 | -41.6611 | 2025-07-18 04:55:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 058820ab-9420-375e-8f94-57f3fcdd5126 | -12.57696 | -56.96931 | 2025-07-18 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d076785-794f-3d29-9ce8-87c7dab5c442 | -18.66076 | -55.73093 | 2025-07-18 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f0ce05dc-237f-30a7-8b52-47441d0795b7 | -14.15321 | -51.02592 | 2025-07-18 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bae2788-a0bc-3661-bb7a-3ea4d0e8f7b8 | -12.43663 | -63.70344 | 2025-07-18 04:55:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 339e26eb-c910-3f26-9dd2-8498346655b6 | -14.72799 | -45.10731 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f505a06-d546-3853-b5b2-ee8163b9f3bd | -12.37759 | -50.35396 | 2025-07-18 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c11f8d4-9724-37c3-ac2e-35ed851fd5ed | -18.6586 | -55.72306 | 2025-07-18 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4a1eaabd-44b4-3ea8-a087-282888a83b6c | -12.43009 | -50.01851 | 2025-07-18 04:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4031d8ea-7509-3a33-8ded-96ea962d0629 | -15.18698 | -43.53763 | 2025-07-18 04:55:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dda09aa4-d24a-31bc-9bd3-c4d9f4194e52 | -20.03621 | -41.6611 | 2025-07-18 04:55:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 66f48677-4f9f-3b1a-b453-6d4c81a27682 | -15.33809 | -49.42358 | 2025-07-18 04:55:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85775aa2-74e3-3e5a-ab1e-410b8f301372 | -14.72218 | -45.11026 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb7aa434-6b9f-317f-911e-5d89c4464c03 | -14.75866 | -48.27515 | 2025-07-18 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9d4cc65-7b05-3f46-a55b-adc335f866b6 | -12.57913 | -56.97819 | 2025-07-18 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9a9ad4c-58a3-34ea-9518-06b34509bea4 | -12.42631 | -50.01798 | 2025-07-18 04:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bee4b7b-3f89-3889-a058-ef8c0441f289 | -20.30664 | -43.97149 | 2025-07-18 04:55:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a7e199fa-ab37-3f02-90ba-c7cf67c5b96d | -18.65802 | -55.7267 | 2025-07-18 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| efbc503f-dd8a-31a6-8411-25574606b54a | -12.98724 | -46.9298 | 2025-07-18 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| befe4d71-fe12-380d-860d-3c85578bfac5 | -12.96573 | -46.926 | 2025-07-18 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1db4113d-b627-3bd2-8ede-968892424f77 | -14.73705 | -45.07626 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2df0a93c-621c-33c6-a4bc-6f4e17c9fe12 | -13.59914 | -51.80609 | 2025-07-18 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cef5586e-da68-3fee-94ec-f8bc22498d78 | -14.72165 | -45.06722 | 2025-07-18 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd9a1c3a-b783-3313-951d-5f64cdb6e757 | -18.58043 | -52.39545 | 2025-07-18 04:55:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 748d788b-432c-3254-b533-dd9336d1d685 | -20.99311 | -49.76581 | 2025-07-18 04:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 89a7aefe-d2dd-36aa-88fd-f76daa6ee7e3 | -22.88262 | -44.77231 | 2025-07-18 04:57:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ffb10f97-d48b-32f0-87a3-b647b98dcba5 | -24.7744 | -51.97618 | 2025-07-18 04:57:00 | NPP-375D | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| caa494a2-1592-3dab-9429-b5734307a2a6 | -21.04012 | -55.98468 | 2025-07-18 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a15c5893-058f-3afb-8c6f-f2bd105ff6aa | -21.22987 | -47.74811 | 2025-07-18 04:57:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93f90158-d87b-3118-8729-f84aa46acbae | -23.56029 | -46.17555 | 2025-07-18 04:57:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 68f8d8f8-08df-3c47-b769-f81a0f5c876d | -23.4746 | -47.16891 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 63ea7f91-9f7f-322d-b88c-7f800078831c | -21.48682 | -56.14978 | 2025-07-18 04:57:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59274a56-d2e3-3359-a98f-710117d4ef10 | -23.48041 | -47.17418 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a6f8247b-950e-3156-8dfa-88dfcef32a4b | -21.04286 | -55.98898 | 2025-07-18 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e8138f7-9204-325a-96f5-db7a05989897 | -20.93949 | -56.59489 | 2025-07-18 04:57:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f577c41b-b32e-3d08-b090-b66d69549498 | -23.4798 | -47.17007 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dc2dc201-f48e-3190-85af-77d77fc202e3 | -22.05038 | -49.96667 | 2025-07-18 04:57:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0ca9d3f8-b04a-393d-a6d4-e3843d21a801 | -23.4752 | -47.17317 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 397cfce8-7082-397f-9b3a-6f32e99ad449 | -21.03679 | -55.98409 | 2025-07-18 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38d8a509-ac66-3f01-b73c-6213e61e6db8 | -23.47064 | -47.16555 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2dcc9088-dc96-3a5a-84f3-db2061839baa | -22.70532 | -44.18193 | 2025-07-18 04:57:00 | NPP-375D | BANANAL | SÃO PAULO | Brasil | 3504909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37b8c719-8f84-3b75-aa3c-070239726c32 | -20.19229 | -50.4953 | 2025-07-18 04:57:00 | NPP-375D | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e5cb8c3-489b-393e-a8a9-0f82f85cc5cc | -23.4795 | -47.17329 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fe5bb962-2a1c-3ea5-a58d-f4bc946bfae2 | -23.47585 | -47.16661 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 151523f6-909d-31c9-a291-03d5ea16710b | -20.19587 | -50.49959 | 2025-07-18 04:57:00 | NPP-375D | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 7a4f7c20-5b8e-32f1-8663-2596d38d4507 | -22.70243 | -44.17846 | 2025-07-18 04:57:00 | NPP-375D | BANANAL | SÃO PAULO | Brasil | 3504909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 732f17d7-6319-3838-9e2f-45b420b22376 | -23.47491 | -47.16554 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bdecaaa1-c340-33a0-bd85-31c363b75eb9 | -23.00928 | -48.62565 | 2025-07-18 04:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd96ca2b-1c4c-3b6f-b06e-a4e3973751f8 | -22.2473 | -49.92051 | 2025-07-18 04:57:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 71b70919-6ed8-3129-8d77-df784c0f6c04 | -20.22523 | -56.31967 | 2025-07-18 04:57:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7841def2-67bb-33fc-83d0-fdf4e5b2d22f | -22.88294 | -44.76842 | 2025-07-18 04:57:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 03e28ce5-e3f9-31f6-b8a9-7575a0242f5c | -25.39001 | -49.67479 | 2025-07-18 04:57:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5785198a-de28-3db7-b4af-7c03cb4cc9a5 | -21.03954 | -55.98838 | 2025-07-18 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9acae8c-de5f-3c48-b011-f76ba1ac2b02 | -23.48073 | -47.17101 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b11ab516-ef7f-3c2d-881c-2d3ff6f48e4d | -22.41821 | -48.15413 | 2025-07-18 04:57:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4972d077-b06f-320e-ae70-9bab6fcb8dfc | -22.05089 | -49.9623 | 2025-07-18 04:57:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b60fe875-41b7-306a-b56f-42a35f97fe90 | -23.56348 | -46.17378 | 2025-07-18 04:57:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5dbb3e8a-2c4e-3e0a-a509-6b09f94f38ea | -20.9883 | -49.76954 | 2025-07-18 04:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 505e3ee4-08e4-3cd4-a973-3bf653881d58 | -23.00452 | -48.62513 | 2025-07-18 04:57:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b09b4a8a-c660-3572-84aa-fd033b738d22 | -21.10785 | -55.80575 | 2025-07-18 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e799f027-76a5-37a6-ab53-11b353ea413e | -20.20537 | -56.61354 | 2025-07-18 04:57:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7ca65643-27ae-3dcf-9329-ffdbd50f163f | -20.9926 | -49.77011 | 2025-07-18 04:57:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| fb2e7bc8-553b-322a-9a0f-b02e43edb2e0 | -20.19635 | -50.49586 | 2025-07-18 04:57:00 | NPP-375D | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 92b4fe56-ff6a-311c-a8e7-02425c3dcd2d | -21.86347 | -56.74087 | 2025-07-18 04:57:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a905bb55-754d-35df-99f7-34885b84f473 | -20.19181 | -50.49903 | 2025-07-18 04:57:00 | NPP-375D | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 44ebbf59-aa4c-3215-9ea5-de7b71b28674 | -21.34364 | -55.63717 | 2025-07-18 04:57:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3e30527-76fc-37da-9d5f-c45fca3cd17a | -22.64176 | -47.51888 | 2025-07-18 04:57:00 | NPP-375D | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 60e95d0a-c3f2-3549-bc88-1cd6874a36ef | -22.41613 | -48.15458 | 2025-07-18 04:57:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73a6ddc7-fbb3-3526-9515-535c82a7d1e2 | -20.20477 | -56.61726 | 2025-07-18 04:57:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5c4e80ed-2076-3254-b5f7-69324dca97c2 | -22.70571 | -44.17739 | 2025-07-18 04:57:00 | NPP-375D | BANANAL | SÃO PAULO | Brasil | 3504909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61c7b9da-a67b-3352-8474-8a916a027167 | -23.47429 | -47.17217 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 30f19b44-6ee8-3ea1-bd37-27e5b52ccf8b | -22.65427 | -53.37684 | 2025-07-18 04:57:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 732fa374-5bb0-3821-92a9-58455429fc3e | -23.15197 | -46.25672 | 2025-07-18 04:57:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 14e3dd14-5e0c-3c48-a17b-83049df45abc | -23.56063 | -46.17179 | 2025-07-18 04:57:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d272d473-81c7-3ce3-8e92-5bc3e714808b | -21.10727 | -55.80945 | 2025-07-18 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c9ba66b-a179-3fbe-91d5-28177238e8dd | -23.47552 | -47.16998 | 2025-07-18 04:57:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd4ad014-7ba5-3ac1-9f3c-a5a78b8cb512 | -5.6569 | -43.6929 | 2025-07-18 05:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 601c45ea-9e53-3082-800f-c229c25f77ae | -11.7508 | -48.1825 | 2025-07-18 05:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a091c6ab-6882-3bc9-956e-f56c3b2f5658 | -5.6567 | -43.7161 | 2025-07-18 05:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| d114bc9f-6606-3c80-8bce-664db525f0db | -3.3958 | -47.4785 | 2025-07-18 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 3a1d0873-a324-3ad0-b01e-11e6c2e94704 | -5.1934 | -45.4835 | 2025-07-18 05:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 1a7d1814-f006-3a54-8a1f-faacfa44e2a1 | -3.3957 | -47.5003 | 2025-07-18 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 36129dc9-a45f-38a2-9e56-f3759a6402d6 | -5.6567 | -43.7161 | 2025-07-18 05:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b10ca8a7-e7f7-3232-a65a-e121476c6fc7 | -11.7317 | -48.1849 | 2025-07-18 05:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 409da1dd-ee4d-3c2a-ac4b-7335d656ba0e | -5.1934 | -45.4835 | 2025-07-18 05:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 2102ca45-42cf-361e-9ae1-e8d8cb13efa8 | -11.7508 | -48.1825 | 2025-07-18 05:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| bd56fabf-59d6-3b52-bcc9-05e4caf62093 | -3.3958 | -47.4785 | 2025-07-18 05:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 10ee21c9-c7ae-30db-9490-3db38e87ccbb | -2.44247 | -47.32945 | 2025-07-18 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32966030-159f-311e-957e-cc1f8d6b5523 | -2.44 | -47.32784 | 2025-07-18 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea17405b-e7e7-3fd0-8fac-a2d374177a48 | -3.11616 | -47.00932 | 2025-07-18 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fd8f56af-e476-36f3-bd2e-f44f5e4c9a54 | -2.63232 | -47.3057 | 2025-07-18 05:14:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d2de087-e7e2-362e-a487-e1975869526e | -2.58647 | -51.92297 | 2025-07-18 05:14:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0701a00-514e-3b19-82dc-4c9b39274a73 | -3.12234 | -47.01022 | 2025-07-18 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 64c74090-b7f7-38f9-ad94-e53f962aed24 | -3.12132 | -47.01321 | 2025-07-18 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b2a008b7-72cf-33af-8285-87c882130af2 | -2.91236 | -48.24319 | 2025-07-18 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d25374e-9f99-3cfd-bed5-1df309889c1a | -2.6532 | -48.80798 | 2025-07-18 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d5eff1d-8f2c-3631-bea5-38d44fc1e136 | -2.65371 | -48.80451 | 2025-07-18 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63d3715d-70a2-35fd-a4b0-d036e3128267 | -2.44531 | -47.33318 | 2025-07-18 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3acbb310-3227-30ec-a07f-1eda1de2fe87 | -2.91178 | -48.24706 | 2025-07-18 05:14:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README26.md)
