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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc7ec3d9-d598-3d5d-a674-f5297b62ff8c | -15.72098 | -53.63851 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8868cc70-2019-3788-af6f-a67efae59add | -21.0875 | -45.45353 | 2025-09-03 03:57:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 304e973f-94ca-359e-9a88-60af9473ece3 | -17.29094 | -47.70384 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c538eeba-abd1-36ce-bdd7-710313880624 | -23.20917 | -49.41367 | 2025-09-03 03:57:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 110ee66e-be3d-358c-955b-be7a0a7f57c2 | -18.1453 | -51.74937 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cabba2b3-2a25-32e4-a9f1-f9fbaa688f89 | -20.40406 | -45.6914 | 2025-09-03 03:57:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6384f6e0-abfa-3d17-96cc-507788bd5442 | -16.84667 | -52.11838 | 2025-09-03 03:57:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8287dca-3d1a-30a8-8583-237684a69c61 | -18.68267 | -52.71423 | 2025-09-03 03:57:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 082d9295-6c50-3838-9ae5-2e9f90ce3470 | -19.36747 | -49.11457 | 2025-09-03 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 635b087d-5415-3992-9679-a045f25fd2d4 | -18.66886 | -49.0925 | 2025-09-03 03:57:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a966b815-fb4f-3293-a1c3-0aa8234945e2 | -18.03197 | -51.59214 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 040ca359-bc0e-301f-aa01-79bebd395090 | -17.53837 | -46.61807 | 2025-09-03 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a410d20-0e4d-3198-815e-42ba2ea8a55b | -17.52785 | -47.5842 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6b3b1408-9855-37ed-b91e-c45cce47f66e | -20.59618 | -45.1097 | 2025-09-03 03:57:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b1369267-c473-35c7-86e9-e100e13182fd | -20.59516 | -45.11114 | 2025-09-03 03:57:00 | NOAA-20 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c98db841-41ed-336a-94e1-ed57bc85a2ff | -18.06663 | -45.98819 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8967424c-6cd9-3314-85ce-c1b73b84a462 | -17.9156 | -47.20991 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10ea65c2-c3a2-3ad0-8bd8-50ee2aa812be | -21.34465 | -45.48537 | 2025-09-03 03:57:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce8849c7-19b1-35fc-9b20-636e2275d749 | -20.70789 | -46.30178 | 2025-09-03 03:57:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9c0301e-91ad-39ba-b7c2-25c8535959cd | -22.75737 | -47.27064 | 2025-09-03 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd338096-7a7f-3303-9640-e7974abd859e | -19.13175 | -47.70424 | 2025-09-03 03:57:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76107103-1682-3b69-b882-0cfdf3c16e7b | -19.74958 | -43.29325 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3bbbcdbe-8965-3240-8bf9-c9e80c1dceb2 | -16.39114 | -50.40942 | 2025-09-03 03:57:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eff27c9-b37c-3465-a09d-cdf214c8b87f | -22.17663 | -48.82097 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9610cb74-1a98-3992-b75f-ec31f67419d7 | -19.36175 | -49.11884 | 2025-09-03 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d52bb8b5-4aee-341c-9838-6f0ce8d099e8 | -18.92297 | -47.57491 | 2025-09-03 03:57:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd2fa910-7398-3fd2-b3dd-deb46f54f3c6 | -23.3917 | -45.96345 | 2025-09-03 03:57:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 82d9dd57-3b08-3ab2-9bcf-b8326e99f341 | -18.1935 | -48.12753 | 2025-09-03 03:57:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23e2e798-ff57-3624-8bf8-463e1bb9ad08 | -15.71729 | -53.64386 | 2025-09-03 03:57:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 889daa15-904e-337c-b78d-1cccbfe18951 | -18.06761 | -45.98289 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae11c6c1-29d0-3cc7-95a0-1ab60ca0e4b0 | -15.74752 | -53.69377 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7092e52b-dbb1-36d8-b189-2a96a427e0a1 | -17.53982 | -46.61035 | 2025-09-03 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 667090e2-c26d-3aaf-a157-f72564dc30be | -19.74214 | -43.29581 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d425b955-8a2b-35c5-a817-829b5d495a39 | -16.71567 | -49.07877 | 2025-09-03 03:57:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2248275b-df6b-3edb-a55c-8f77f696a679 | -17.94895 | -47.23638 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65250d07-d585-3b0b-a5b1-f329fbf2df74 | -17.92257 | -47.21308 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a07d48-16d7-30f4-8991-dfe2a768a89b | -18.65942 | -49.09052 | 2025-09-03 03:57:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 687e5cd1-f7de-3343-bf81-cc83c378267a | -15.73319 | -53.69598 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d4a175d-45fd-329d-8a8c-0a0f50887655 | -15.57617 | -54.32676 | 2025-09-03 03:57:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52652ed3-a075-3d04-8b05-a12cde3b3c2d | -17.92406 | -47.21181 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae220e5d-6cd4-3cf6-8d7e-019d01f61894 | -16.30829 | -52.9697 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb34c040-16ce-3409-a4b0-7a826d637fb4 | -22.18531 | -48.82288 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| bb6697ca-f272-3eb2-84fd-0099d6f43fd7 | -20.89124 | -50.10359 | 2025-09-03 03:57:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| db1ec0fb-87a8-3881-9e05-c1cbf48bbb78 | -22.75242 | -47.27522 | 2025-09-03 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 45cff0f9-09c6-33a2-8372-03ff38d4bc6b | -19.74281 | -43.29187 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6742ecda-50fa-315e-b4df-40be85f81c62 | -15.7396 | -53.66742 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85d3e0ca-8ad4-3a79-812b-1249c0ca6ead | -22.75346 | -47.26976 | 2025-09-03 03:57:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c42200ee-ca8c-30f2-89eb-9d199eaa1e03 | -16.302 | -52.96844 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df0ec8f5-e442-36aa-8480-df56bdc3aae0 | -23.32801 | -47.8437 | 2025-09-03 03:57:00 | NOAA-20 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f69ac963-39b9-39d9-bbc2-e65d3375f2a8 | -17.61866 | -46.7022 | 2025-09-03 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9db4b5cf-37f9-3767-951d-155ad2ab6bc8 | -17.93603 | -47.21188 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63945a45-b218-3020-8f20-03e1c637bf96 | -18.06859 | -45.9776 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b684e0e-b293-3951-a190-eb4ccdbdf20c | -17.53218 | -47.58533 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2b7b7af6-fc92-3b54-99cd-ba8a5bcb76f7 | -16.81971 | -52.14157 | 2025-09-03 03:57:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69cb9b23-e984-34be-8e56-0c1ee6465849 | -17.20828 | -50.36736 | 2025-09-03 03:57:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ae2eb01-2ac6-3ee0-93aa-d9359c1bf3f1 | -22.17485 | -48.83 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.7 |
| 1aa618e6-f27d-3704-b95f-8da7e0b91db4 | -16.29431 | -52.95955 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d863563-75e7-3005-b03a-a3c646c8a873 | -15.74627 | -53.66849 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 373930b8-6610-3b64-8d6e-7e2287c8b620 | -18.13967 | -51.74813 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dd5b35f5-33bd-30f2-b127-11aafc321ffa | -17.94818 | -47.24044 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ee58f7-ced3-30a8-91c9-b54c3b033dc4 | -19.74149 | -43.29969 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 037b232c-5f76-32f0-a931-95ffa861d12a | -19.36279 | -49.11364 | 2025-09-03 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55b03fe7-c347-3926-867a-bf6002831db1 | -20.75052 | -47.13408 | 2025-09-03 03:57:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4837f51-c751-30dd-8bea-9402011ae744 | -17.93524 | -47.21596 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 578c535e-52a5-3539-a248-729292eca95a | -19.13774 | -47.6964 | 2025-09-03 03:57:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb65c02a-5415-306c-9de3-9872ba336ae7 | -22.70548 | -47.03205 | 2025-09-03 03:57:00 | NOAA-20 | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 61786183-20f1-32bc-983b-670a03840b8a | -19.14959 | -47.59902 | 2025-09-03 03:57:00 | NOAA-20 | PEDRINÓPOLIS | MINAS GERAIS | Brasil | 3149200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39b8c220-5a80-376e-a2e3-ea15c4fa668d | -16.81727 | -52.13976 | 2025-09-03 03:57:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 584b18ed-5d18-3a78-a68d-0245b8682390 | -16.63668 | -49.29097 | 2025-09-03 03:57:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ac4fae5c-2fb4-3bf4-9969-7de3bf14e102 | -15.71606 | -53.6493 | 2025-09-03 03:57:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9f2028d-95b2-36e1-8f06-d15142f1b0f8 | -18.06958 | -45.99428 | 2025-09-03 03:57:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff20b921-87d4-36ed-868e-e6ed22a154ed | -16.30452 | -52.973 | 2025-09-03 03:57:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77af3303-ed02-37de-a159-9b1b7b0a23aa | -17.18835 | -46.06557 | 2025-09-03 03:57:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2a895f1-b042-3a55-bdaf-fb0151600e1f | -17.61792 | -46.70612 | 2025-09-03 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3a35413-7244-3d90-8a8b-8598ef2554c5 | -23.34636 | -47.15109 | 2025-09-03 03:57:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bd15f530-007b-359c-85aa-7124dda4ee32 | -15.72945 | -53.6945 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e480e82f-f2b8-3d59-aced-58b651d5fb0d | -19.74619 | -43.29256 | 2025-09-03 03:57:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb36da71-de7a-329e-95c2-6257311898c5 | -16.52938 | -49.41157 | 2025-09-03 03:57:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14e721bb-b3ca-3025-a73a-8b2a48e952ec | -15.7186 | -53.64936 | 2025-09-03 03:57:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e4beaaa6-ed99-30f7-b1c3-370432f1e4d7 | -23.65604 | -47.41763 | 2025-09-03 03:57:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7261fa82-ea75-34b8-a460-7c813555bb69 | -23.97609 | -46.47165 | 2025-09-03 03:57:00 | NOAA-20 | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c698f056-594a-33a2-9333-4fe2bd8c23ee | -17.92948 | -47.22297 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4436592e-f6cd-3e01-8a21-f376498bc625 | -16.39184 | -50.40598 | 2025-09-03 03:57:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68d49738-7dba-3f09-904e-77824bcdd6ac | -23.6019 | -49.00757 | 2025-09-03 03:57:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4eac486f-4ce9-3aae-a8d2-c43c4ba5d08e | -17.0489 | -49.6348 | 2025-09-03 03:57:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74178af7-0b17-32ca-ac74-8059cdb48294 | -22.17303 | -48.83923 | 2025-09-03 03:57:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| ff025724-0f8e-3968-9a33-973afe399225 | -17.95237 | -47.24157 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5caabf48-75c3-3ecc-885f-475d6e35ac44 | -18.2965 | -45.41466 | 2025-09-03 03:57:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0f7718d-1559-32ed-8716-67f32dac0cd9 | -19.9435 | -44.71762 | 2025-09-03 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e01ddcd3-df9b-3e2d-96ac-d2c63b15745f | -22.18523 | -48.82535 | 2025-09-03 03:57:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| d5b585d2-9abe-3ad5-829f-7c7fe621ee99 | -17.53302 | -47.58086 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 318a2b3f-8da1-35da-810b-b264b504adc5 | -17.52894 | -47.57836 | 2025-09-03 03:57:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aed56302-a779-3c5f-aee8-830017bed887 | -19.13451 | -47.70222 | 2025-09-03 03:57:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2ceb3dd-6644-3284-bf27-a48303d02e05 | -17.94288 | -47.22205 | 2025-09-03 03:57:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11852683-97fb-35c6-9f66-046d9623660c | -18.14138 | -51.74021 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fbdeaf27-8e5a-31d5-ab59-94acb79875e8 | -17.36293 | -49.18393 | 2025-09-03 03:57:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f476d208-7a4e-357f-aafa-fba642c1b4ee | -18.14444 | -51.75335 | 2025-09-03 03:57:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62ae9ccd-1e00-39a6-b2f8-091af0cbe633 | -15.74249 | -53.69811 | 2025-09-03 03:57:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92a508e9-fcb1-35b5-9c75-a1287fccb242 | -19.42503 | -45.56853 | 2025-09-03 03:57:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1321a849-d150-3ff3-b1af-cbfd16f681cc | -23.03932 | -45.54078 | 2025-09-03 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README47.md)
