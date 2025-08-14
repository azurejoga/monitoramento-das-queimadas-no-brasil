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
| 870c1be6-5b1a-32fb-b9a6-93301ab7bc56 | -15.68462 | -56.39654 | 2025-08-14 04:51:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a1bbeb9-bc40-3a7a-8898-1373928a6814 | -15.58119 | -47.32463 | 2025-08-14 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b9c80c6-dd0e-321e-bec5-e418a8ebfde2 | -16.31208 | -52.91434 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e6a05eb-7463-3576-8bf6-e3fdfccf3738 | -17.04617 | -51.79263 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74aa8720-1994-3206-a610-83294f6442ad | -18.5459 | -46.05755 | 2025-08-14 04:51:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f0706c56-ea65-3e92-bf1d-bc0393880884 | -16.30984 | -52.9287 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 213770fb-95b2-3d95-9f3e-92696d45d64c | -17.65424 | -46.68486 | 2025-08-14 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bbc7167-cd5d-37aa-94ed-4bab9aad8928 | -16.51772 | -49.02491 | 2025-08-14 04:51:00 | NPP-375D | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57578bf5-9132-339a-95d7-a3ac53e934bf | -13.70875 | -53.03356 | 2025-08-14 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 875eeb80-ba4a-3a36-a6ac-6d645c36979b | -13.12952 | -57.14743 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2747300-0eb5-36c7-a3f8-b2cfd93bd104 | -13.07122 | -57.1402 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cf73d4e-e1de-3555-a630-6820d9b03b58 | -13.27649 | -57.25126 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c23df70-f36b-3d93-8e78-7430326eaa68 | -17.04561 | -51.79551 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36965258-89d2-38e9-99d6-4e897f7da60a | -16.29822 | -52.9157 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3184e894-8c6e-3409-b2f0-a2da68784174 | -17.04675 | -51.78884 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28ee2e75-2114-329a-a7b8-35d2592336d4 | -17.04957 | -51.79228 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8aec9114-2285-304b-aadb-713d80254176 | -16.28768 | -52.91762 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5294a8fe-20cb-3720-8497-773057704420 | -16.31817 | -52.91906 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 675569fb-c04a-3897-95d3-ce1e74b25b0d | -18.61848 | -44.26247 | 2025-08-14 04:51:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c5bc931-eed9-3ec3-b61a-e9f07299e5b2 | -14.32419 | -48.63941 | 2025-08-14 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c9e3c0d-07b1-3c00-ad07-7146495dad26 | -21.19745 | -46.68423 | 2025-08-14 04:51:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e2f02262-f94f-3d5c-b8c2-267809307fcb | -18.24777 | -47.25833 | 2025-08-14 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a548b00-3cfc-3915-a41e-93873706f9f9 | -16.30431 | -52.9204 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 661cf2a7-2f0b-33b1-b735-949258c757b7 | -14.6124 | -51.33638 | 2025-08-14 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47236c83-43b6-383f-b942-3b844a85d05c | -18.24341 | -47.25768 | 2025-08-14 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17d7f43f-78d2-3826-9ab7-efa55bfe92da | -15.15171 | -53.51285 | 2025-08-14 04:51:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 176d4c77-348e-3789-b392-1ac8526605ca | -20.47631 | -53.67438 | 2025-08-14 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff51d379-2911-3ae0-95a0-c0080340361c | -19.25746 | -44.17017 | 2025-08-14 04:51:00 | NPP-375D | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d546dba8-75b1-3d67-b062-c5f7e5840d2e | -16.30211 | -52.91266 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ec541c1-3060-3e77-9df3-666c1b1c7b17 | -17.86743 | -52.195 | 2025-08-14 04:51:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74f6d2bc-3dcd-3008-b34e-2532027ff3f9 | -15.69689 | -56.41227 | 2025-08-14 04:51:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4388389c-98f4-341a-a299-3c3e19b4b8f5 | -14.46053 | -48.81714 | 2025-08-14 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aedeca60-2806-38ea-87c3-82ff4124c007 | -14.46118 | -48.81534 | 2025-08-14 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f005b4c7-160d-3cea-9ec4-712257db31c0 | -16.30708 | -52.92455 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c86aec1d-f4d9-34b3-8aba-afe5d70558e8 | -16.30652 | -52.92813 | 2025-08-14 04:51:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 265b1dd8-a605-32ad-80f7-4fbc4fd31449 | -18.63983 | -51.8505 | 2025-08-14 04:51:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17db1d5a-61bc-3b5e-95d9-58a520f1c22a | -20.03376 | -49.4064 | 2025-08-14 04:51:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5bf26e5-4968-31b2-95f6-0cefea7b2725 | -21.01125 | -48.92182 | 2025-08-14 04:51:00 | NPP-375D | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| d71ca84f-896f-35c1-8e0d-ab7868d03e34 | -19.25202 | -44.16958 | 2025-08-14 04:51:00 | NPP-375D | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e2c7b85-b4db-35f8-a93f-c945ab2fbf05 | -13.11833 | -57.14907 | 2025-08-14 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd1d4f3d-4fb7-38f4-8065-5544be8ecdbc | -20.48201 | -54.74915 | 2025-08-14 04:51:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 877516cc-4226-3117-a5fd-87ee5f015955 | -21.14105 | -46.62682 | 2025-08-14 04:51:00 | NPP-375D | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 43ce316f-b5aa-3916-ac44-d916925f24df | -14.37595 | -54.6537 | 2025-08-14 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b53c3e1f-a0f5-3b6a-b297-948ee348a46a | -20.34825 | -45.98721 | 2025-08-14 04:51:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf80af28-53a8-31c3-9598-6815ce845fd2 | -17.63838 | -44.49997 | 2025-08-14 04:51:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b18f9579-5ab2-3664-ab67-12f5ff2e6671 | -17.0524 | -51.7966 | 2025-08-14 04:51:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| faa3ef26-a89b-3cf2-b273-542279fc769f | -18.24287 | -47.26207 | 2025-08-14 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 743899d8-0134-36f1-bccc-9dccf3a867f8 | -16.26025 | -49.96613 | 2025-08-14 04:51:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f900333-7c38-3fee-bec0-76f1f7ca94a6 | -18.6181 | -44.26596 | 2025-08-14 04:51:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46819f88-a258-3db0-9b86-79c0431825e6 | -20.4802 | -54.74943 | 2025-08-14 04:51:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45048edf-60a2-3260-9543-b451e9fb36e2 | -14.797 | -42.72478 | 2025-08-14 04:51:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 038faa28-bf00-346e-8535-23c5f6b5d35a | -18.53702 | -46.05111 | 2025-08-14 04:51:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ad2103b-f847-338f-b7af-90eebf83041c | -22.67538 | -47.45591 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7d6c392f-799a-3745-b9d9-57eae222b8f6 | -23.19089 | -46.59419 | 2025-08-14 04:53:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7adf5086-b661-3a3b-a15b-78694a5f29a1 | -21.83109 | -46.4986 | 2025-08-14 04:53:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a173bc00-dbb5-38eb-949f-8ffd36faa81d | -26.1041 | -50.17726 | 2025-08-14 04:53:00 | NPP-375D | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4bf7936a-26f9-3a14-95d7-3993191095f5 | -23.34775 | -47.8153 | 2025-08-14 04:53:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1dbf8c7a-9c57-382a-88b6-006c559cd842 | -22.6269 | -47.39264 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 17229c61-e7ba-3191-af5b-452f5e3dbf85 | -22.59954 | -46.72281 | 2025-08-14 04:53:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2130f27-a085-30c7-a260-c8319797ecf5 | -22.62288 | -47.38687 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1eb073cc-b224-3c2e-94de-1ed3c61aae07 | -23.18836 | -46.59346 | 2025-08-14 04:53:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 933d8f5c-5378-333a-8690-cbfbfddb9bd3 | -22.67058 | -47.45889 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f5ccbac5-6569-3a89-a63c-1215172eae27 | -24.45643 | -51.81874 | 2025-08-14 04:53:00 | NPP-375D | MANOEL RIBAS | PARANÁ | Brasil | 4114500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd713db1-8956-33bc-b49b-175519033a24 | -22.71696 | -43.23334 | 2025-08-14 04:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 84a3837d-b2d3-392a-8a27-6534da9f1755 | -22.85519 | -49.22433 | 2025-08-14 04:53:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3c5d917a-ae5c-3e9f-b0d1-0c00db74d3ed | -22.71655 | -43.23804 | 2025-08-14 04:53:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bee5c94e-42a0-3f4a-be32-0c31363ed510 | -22.55596 | -49.77166 | 2025-08-14 04:53:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 15c5c5da-5110-375d-bd80-cae52fbe584e | -23.05442 | -48.85358 | 2025-08-14 04:53:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fab7fd80-462c-3ad9-b5f5-f1b4ce734748 | -24.48146 | -50.64512 | 2025-08-14 04:53:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2d944f8-8180-3cd6-aecb-6eb44ee07053 | -23.57693 | -47.24352 | 2025-08-14 04:53:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f29b1b3a-4b69-3c57-93ac-4f102c0f06c0 | -22.60433 | -46.72355 | 2025-08-14 04:53:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed13107a-04db-3acb-b476-c3b475c8824a | -20.61962 | -55.48635 | 2025-08-14 04:53:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7111a924-fecc-36ac-aebb-dce9a40c8f4a | -23.18601 | -46.59365 | 2025-08-14 04:53:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8045f344-f93d-31c5-b3d1-a7f85dfa6012 | -23.57224 | -47.24284 | 2025-08-14 04:53:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fa6d17aa-8fc4-39ba-8134-33dfaedee36d | -21.5399 | -54.16596 | 2025-08-14 04:53:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f95f2783-d8f9-3e0a-a3fb-dacb58ef7eff | -26.09313 | -49.45776 | 2025-08-14 04:53:00 | NPP-375D | PIÊN | PARANÁ | Brasil | 4119103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b5caed19-4f00-3b69-b1d7-2122c7d86b09 | -22.16274 | -56.65158 | 2025-08-14 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 417b13ff-2212-3a83-a648-37ac1e44e9e5 | -22.67116 | -47.45388 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2835033b-7f92-32cf-bc51-3ef26e5964da | -22.67079 | -47.45543 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 16660da8-308c-3f37-a11a-eece033890d2 | -22.21574 | -56.19363 | 2025-08-14 04:53:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1caf43c1-54f7-39d6-b548-ff526ddf55d6 | -22.67484 | -47.46092 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 4d4f6213-40a9-384a-91d0-30934cb4d3f5 | -22.6223 | -47.392 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ab6143b3-1253-30ad-8d8d-cd8400a4e3dd | -22.6183 | -47.3861 | 2025-08-14 04:53:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1d402f59-b01e-37d3-bd34-48bb68c8c2a6 | -22.59894 | -46.72839 | 2025-08-14 04:53:00 | NPP-375D | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cca17c49-2d3e-34ce-bdc2-b0e571cf7459 | -23.35226 | -47.81593 | 2025-08-14 04:53:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5e213556-9aa7-3355-931b-f880e98f54c0 | -6.8956 | -59.1462 | 2025-08-14 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 723c49e0-33e5-323d-8bf6-b116051f9be4 | -6.914 | -59.1455 | 2025-08-14 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 2bde1cbd-6060-3ab9-b001-2cfb59f3a146 | -6.8771 | -59.147 | 2025-08-14 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0aa4a0d9-9397-3de5-8e5f-e009a2df5bf2 | -6.8955 | -59.1655 | 2025-08-14 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8388c63b-3cfb-38ab-9473-02e8fac37c4b | -6.877 | -59.1663 | 2025-08-14 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| a431a2e6-e2ff-3f99-83e5-7fcf16014cad | -2.91058 | -48.2445 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08121ed7-3470-318e-b4aa-789346356445 | -2.90728 | -48.244 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12dcacb4-a363-3090-861a-f34081dd8fb0 | -4.22734 | -47.21459 | 2025-08-14 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8af07428-da0f-31aa-8230-46d90abf9419 | -4.22678 | -47.21835 | 2025-08-14 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d53e1677-5f27-3902-af19-017be11e86c5 | -2.90127 | -48.24915 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b6fc17b-5c20-3a60-a635-c8e46271fb10 | -2.3683 | -51.90844 | 2025-08-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cdec5365-7f2d-3b96-abdb-d42a0cdc05ee | -2.9547 | -51.66223 | 2025-08-14 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf4f9b61-9473-3849-9f8e-ed7f0d7e2a32 | -2.36906 | -51.90345 | 2025-08-14 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ccff2fb5-8c9d-362d-bce0-b001ba9c736e | -2.90461 | -48.24964 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66c5f6bf-2c98-3204-b0de-965cb11806c0 | -2.90505 | -48.24668 | 2025-08-14 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README26.md)
