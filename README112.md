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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 960f9058-cc9e-3fad-9d3e-baaa3d1f73f2 | -22.65897 | -53.09991 | 2025-09-12 05:23:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8991c25e-0de8-31f2-8935-95ae88adf27a | -23.19083 | -49.65135 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 500b2385-da78-3f81-9ae1-7498fe729daa | -22.65829 | -53.10712 | 2025-09-12 05:23:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a1d7cbfd-2c91-3a74-b56a-5ad7f1c52989 | -23.23664 | -49.42076 | 2025-09-12 05:23:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 40c1f73e-7533-35c0-9f9c-0f6ca5a2bcde | -24.12018 | -48.70706 | 2025-09-12 05:23:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0a593cd8-4c03-3072-bad5-3b3b2a767cb8 | -23.19326 | -49.64776 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 74712b46-8e1c-39d4-a0bd-c03c1a7e1391 | -23.19047 | -49.6567 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f4e8eff5-2b95-3550-8585-51047adfe302 | -20.83002 | -56.88293 | 2025-09-12 05:23:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e39915c0-25ed-328b-9efa-c1551627ec16 | -22.65863 | -53.10351 | 2025-09-12 05:23:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 930e8db2-b521-3c21-b4ac-2b2bd6ce3c29 | -21.61376 | -53.99458 | 2025-09-12 05:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d123af5-d7ce-3750-b460-898aee665004 | -22.65795 | -53.11074 | 2025-09-12 05:23:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18bf3ffa-0103-3ee0-b7a8-f1516271a47c | -21.45259 | -56.15611 | 2025-09-12 05:23:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e427d9e-eb89-3254-9426-cb87f4fc1c3a | -23.13937 | -49.65432 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4e1e8fbd-b8a5-35a0-be45-24de151e5574 | -23.23317 | -49.41812 | 2025-09-12 05:23:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 79e66651-2551-3d1d-bea1-157f9ccaf6e1 | -22.62712 | -53.09249 | 2025-09-12 05:23:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 80fdf5f4-4155-3ab8-be43-d8b9161dfcb8 | -21.63936 | -53.9919 | 2025-09-12 05:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 791e2579-db33-3e97-86ae-12637a89e5be | -20.89634 | -55.17707 | 2025-09-12 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db978329-a613-3d9f-9e8a-dab24eab9062 | -22.63249 | -53.09313 | 2025-09-12 05:23:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ab307db-54b0-300a-b40c-9ea3ef6e6eed | -21.61875 | -53.99526 | 2025-09-12 05:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f6b2541-a1b5-3690-936d-40259d6da5d5 | -23.19783 | -49.64662 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fcb9baa9-c161-39e8-a68c-e7216fe5dc38 | -21.64437 | -53.99248 | 2025-09-12 05:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a3b9826-d1ef-3bc5-a8bf-d08e47099d54 | -23.19285 | -49.6534 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0432a31b-6188-33aa-9077-1edb7508278e | -23.14587 | -49.65688 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a21d466f-ae14-3036-afa8-229e885408c4 | -22.65761 | -53.11435 | 2025-09-12 05:23:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c234b57b-62a7-3564-b307-5a46c44892a2 | -21.17971 | -54.97015 | 2025-09-12 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 654d8436-397f-3e3d-be80-81fec4894631 | -22.65361 | -53.09928 | 2025-09-12 05:23:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e738c983-c312-3c8d-9db9-1c58b459190a | -23.13885 | -49.66186 | 2025-09-12 05:23:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b15c8501-fba0-3757-a677-ca651882e508 | -21.1616 | -54.9627 | 2025-09-12 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38559941-6a0f-3d29-8cfb-bb1b78eab180 | -21.15692 | -54.96219 | 2025-09-12 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d24f72a1-de5c-3f2c-b680-9b6c59dcc213 | -22.63819 | -53.09016 | 2025-09-12 05:23:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f492007-cf53-3872-8497-2897d5a283aa | -9.3017 | -65.5959 | 2025-09-12 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ad1d66c5-67f1-3daf-8bd1-5925994f9056 | -12.9292 | -54.7538 | 2025-09-12 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e099eee7-f1ba-3be1-8360-029a35dde931 | -17.3942 | -52.9526 | 2025-09-12 05:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| a1c6d422-3380-36bb-8be9-bf8cfe3e201a | 2.50469 | -61.02911 | 2025-09-12 05:42:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d8914a44-e399-3931-899d-78042d69cb78 | 3.36645 | -61.22409 | 2025-09-12 05:42:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c0e7611-40da-3806-aad1-d93e2d2612fe | 2.50816 | -61.02857 | 2025-09-12 05:42:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b30484d7-0470-3944-a0df-2aabcff7fa1b | 4.11399 | -59.97733 | 2025-09-12 05:42:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d6f49c6-0d0a-37f8-bca7-4260f25079e1 | 4.31688 | -59.82652 | 2025-09-12 05:42:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0df9ece3-fb00-3618-b164-be8db8a5b62e | 4.11758 | -59.97682 | 2025-09-12 05:42:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c40883d4-f539-35ec-b9be-735b58bb0557 | 4.11335 | -59.97342 | 2025-09-12 05:42:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c617e3-0c61-3c08-9af4-cbcb84f0662d | 4.11693 | -59.97284 | 2025-09-12 05:42:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b9df230-720c-3e3c-a7f7-ce8f1d3e2dd0 | 4.11627 | -59.96884 | 2025-09-12 05:42:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69b3fb9b-d76f-3206-b155-4eb18bc191d9 | -6.82638 | -52.79898 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1c91625-29ea-3a4a-af5b-851afec34469 | -6.82046 | -52.79219 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cb8a558-43c6-356c-8a78-8174a4d206d1 | -6.81585 | -52.8061 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cdf3ba5-ad74-3d47-b241-060d7aaabfb8 | -4.93529 | -55.78513 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0d4cc71-48f3-3dce-a9cc-29bd9bea6312 | -7.35591 | -59.82251 | 2025-09-12 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75728296-3fd3-3138-9801-c8473af6c8a5 | -4.92839 | -55.78113 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ad6f473-68d5-3752-aa69-8bb5c37ba814 | -7.47867 | -61.58931 | 2025-09-12 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0551e8d8-28f4-39df-837c-4af87f7cbe1b | -7.39015 | -59.6981 | 2025-09-12 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eb8971d-9b28-3708-8b27-258e893f6b98 | -7.49401 | -54.94704 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48f958c9-60f4-302a-910a-f2312c402a59 | -4.93328 | -55.78525 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15c81632-9f8e-3ff5-a84e-42a3ef0396ff | -7.23021 | -55.06284 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b92ee228-5ab3-3cca-932a-1efcedbdd643 | -6.83071 | -52.79679 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0166691-aaf8-3927-8d91-a987905f0e3b | -6.82709 | -52.79347 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de2148d6-cadc-3220-8111-747f39743ae6 | -6.40243 | -58.20938 | 2025-09-12 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47feff2e-4b9b-32b0-8809-f7a128d9f6ce | -3.40607 | -60.3953 | 2025-09-12 05:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9c34d15-4b0c-3595-bfa5-a18254640f9a | -3.0433 | -59.19677 | 2025-09-12 05:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 174ee5d3-aa63-333d-8851-3b8188a90932 | -3.4006 | -60.39656 | 2025-09-12 05:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87c37ffd-42ce-3d45-81d6-d4620379f537 | -7.51298 | -55.01866 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99f1ef0f-d1b3-35bc-a3bf-f5c42eb1b2cf | -4.53418 | -55.68263 | 2025-09-12 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02e03a60-fd26-3e5f-9bfb-e686161498b0 | -4.53711 | -55.68733 | 2025-09-12 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7d05214-b49e-346b-915c-8a16815f62ec | -6.82403 | -52.79593 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0774634-8c61-31ec-b221-094129fceaee | -3.53695 | -59.57775 | 2025-09-12 05:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a56ae4c-df54-3ace-8f87-0a6f97cf70f8 | -3.53289 | -59.57715 | 2025-09-12 05:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c620104f-bea2-3101-8335-0d45c614bfd9 | -6.81971 | -52.79802 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de9dce3c-68e2-3782-bf68-d637dd7dfd7a | -4.5337 | -55.686 | 2025-09-12 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4794961-ab12-33f5-b80d-3495a14bc47c | -6.83312 | -52.79946 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2388d37c-6ad2-3692-a96a-b5e178d0fc2b | -7.51883 | -55.01964 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9e84c99-8642-3e7d-9a9f-4ca4238abef3 | -4.92992 | -55.78431 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cb821fd-1b84-381b-abc1-8757a9ac41df | -7.49248 | -54.94658 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0c6c4b7-9ed2-38a3-997f-d501d1de7d70 | -7.49193 | -54.95079 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bec14c3b-370a-3656-bc82-6be4dbd254e6 | -7.49343 | -54.95128 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed2de4bd-10f4-3546-ac1b-79dee44e8ed2 | -7.0957 | -59.53638 | 2025-09-12 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 754042d4-f8de-3c18-b4ef-5bbc7f92cc0f | -3.52883 | -59.57655 | 2025-09-12 05:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7139271-0705-3732-b0f8-60cf5556c366 | -4.53173 | -55.68651 | 2025-09-12 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb8fe96a-282a-3d34-9007-f265bb86fbc4 | -4.25984 | -53.51642 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54630ddf-1ade-3634-8aac-7542fa879729 | -7.4865 | -61.40535 | 2025-09-12 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c31b515e-9c37-3f00-b4c5-ac0886e66e61 | -7.38587 | -59.69755 | 2025-09-12 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8505bb93-3ed0-323e-9fd6-52a89d534dd2 | -6.82328 | -52.80144 | 2025-09-12 05:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfcf15d5-854b-35ee-8f4f-1cae7307dbfe | -3.8171 | -59.67012 | 2025-09-12 05:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eca92bf-cde4-3d06-b787-5bfe1e125f38 | -4.93039 | -55.78097 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75eebf3a-8616-3e15-a425-5015f7ba9782 | -3.40223 | -60.39469 | 2025-09-12 05:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd913290-63a0-3f27-bef2-b6cd37f94b60 | -4.16482 | -56.14233 | 2025-09-12 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b202c70-8cf9-3b42-af66-c4c986e70a62 | -3.75858 | -59.42217 | 2025-09-12 05:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa0d72b6-db15-315e-bd36-6936418983ea | -4.16527 | -56.13919 | 2025-09-12 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8fb99e9-314d-3d90-9878-ab32c1d5bc0b | -7.22493 | -55.05795 | 2025-09-12 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd79242-6d8f-36f0-ae5d-3ef65847352d | -4.93277 | -55.78865 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a237341-96a9-38a1-b650-872f8fe8f20e | -4.92945 | -55.78766 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf029d7-17ba-3418-876d-5847f2691318 | -4.93378 | -55.78188 | 2025-09-12 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05f4d340-d65b-349a-bd92-4b28c19842b8 | -14.94162 | -55.94999 | 2025-09-12 05:46:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc0fc8a4-bfb7-36fa-8422-9d40f102781d | -12.77041 | -61.44666 | 2025-09-12 05:46:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21e9ba50-bd66-3bbc-bb97-2ff7d8797a32 | -11.87714 | -58.82668 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10904526-7416-31ce-b8ea-9c84b15a446f | -8.63243 | -66.71678 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91b990b1-2f9c-332b-a3d7-dd05c79a3fee | -12.91744 | -54.76036 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 919a6d2a-40c3-3ced-9c05-eb2ee78dd0ea | -9.51632 | -54.63109 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 99759afb-11df-3741-ad5f-45d921e19f7d | -7.5604 | -61.3124 | 2025-09-12 05:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f8f1d53-5635-3ebe-9d18-8ededfa495c5 | -9.50283 | -65.58249 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 362792a8-a108-3b4e-886a-27ea615fdfd7 | -8.85801 | -64.23378 | 2025-09-12 05:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b6282e4-5569-3d41-8554-25c194c15739 | -12.919 | -54.75573 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README113.md)
