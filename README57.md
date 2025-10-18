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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bc1e097-13cf-3340-9b3f-49454f2ac7dc | -12.17402 | -45.05404 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 538fbebd-7c40-313f-8374-d790661ec783 | -13.60607 | -42.42378 | 2025-10-18 04:32:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3ee2919b-c1a6-3895-9fc4-c1a6558b0040 | -12.42783 | -47.79359 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 056ae428-0aad-3e8a-86e8-e64734d911b6 | -10.88351 | -47.46358 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccb95f4a-a003-3225-84fa-0824ef934fe9 | -12.20534 | -43.55853 | 2025-10-18 04:32:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0e20000d-c9c6-3338-b8b6-1f2041ff21a7 | -13.0408 | -48.19528 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7169907f-58a5-3398-a29c-2ee579518208 | -13.03648 | -46.95515 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66c50fe1-158d-3c86-aa8d-bbc378ad2f93 | -11.37167 | -49.37432 | 2025-10-18 04:32:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 365d0b34-d3b2-307a-bbd1-1062451cf2ef | -12.9135 | -48.58353 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 413dbbb4-f24a-37e8-b53d-67ea8b4b9724 | -17.49366 | -43.45875 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0edfde7c-57f5-32b1-86da-789ad1b80619 | -13.02938 | -47.27648 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baa2a169-1072-3ad0-a8ea-020abe4f36c9 | -13.77976 | -48.24484 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff863669-06c2-3c3e-b2d3-059041e779e9 | -13.44556 | -47.98526 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0f820b9-c7e5-3895-a41d-de8161b4a4ed | -12.24281 | -49.37134 | 2025-10-18 04:32:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee0b24b9-8289-3950-8de9-afdb535ec923 | -12.46771 | -45.47174 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 6ca022e8-a30b-35b0-b531-1171a0792af1 | -14.50557 | -45.607 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4cbb192-0b7c-3ab6-8bf0-8b9941d74fb6 | -10.98452 | -47.93128 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74323e4b-7716-3e0e-8676-0231188d76c6 | -13.03803 | -48.19117 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0db482d1-c395-3a1d-9694-b9dd3a234491 | -13.18601 | -46.43794 | 2025-10-18 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d42113ba-6fb0-3281-8762-3972b5153cf1 | -10.91035 | -47.9122 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d0600b3-79b3-3a39-98fa-376b276d01e0 | -13.7559 | -43.81058 | 2025-10-18 04:32:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 802d546b-9024-3627-9456-2af26b34ee5e | -10.97842 | -47.92663 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d0f10d4-c57d-35c5-a85c-0c4597230e82 | -10.91906 | -47.9862 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbbb7d6f-d7aa-375a-a4c3-74e54f66b9e8 | -16.07315 | -42.55183 | 2025-10-18 04:32:00 | NPP-375D | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7d86878-ad86-3f79-9393-d375884ce411 | -13.8351 | -42.63002 | 2025-10-18 04:32:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 935ccb38-c30f-351c-8fb8-6a045e6fe23d | -13.73542 | -44.22956 | 2025-10-18 04:32:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e25ef1b6-55f5-333b-ab9a-e9099d807c04 | -13.24579 | -48.55487 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fc8eb01-2668-38c7-80c4-57e22d501d19 | -13.73462 | -48.12064 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5d0fc83-a698-366c-b2be-c368154422f1 | -12.39106 | -47.20713 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 995c7896-64d8-32f5-a2a7-554bfc5d561c | -11.18879 | -51.96481 | 2025-10-18 04:32:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fd1f23-3e3d-33fc-a9b0-49c6fc4ebd89 | -13.77311 | -48.24372 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 01dece36-4baa-30d7-8577-0313429a33e7 | -17.76717 | -45.58846 | 2025-10-18 04:32:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0834508a-9c0d-3304-84b3-4b425f895f1d | -14.54843 | -49.27862 | 2025-10-18 04:32:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9516072d-957e-3441-bc76-62e5e5fa3d1d | -11.47431 | -49.81798 | 2025-10-18 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1ca94d6-e2cf-3da3-9626-5d3b73bd5bc8 | -11.61021 | -44.07823 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| faac320b-1fe2-3f39-8a75-c6ed9e78fb29 | -13.34842 | -47.26612 | 2025-10-18 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ef6697f-76f9-3ede-9968-20b12bdc7e9a | -11.49308 | -44.16901 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4bd697a-462c-3f0b-9a6b-8ac4f5a5adb5 | -12.48916 | -45.47115 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5abe2b8-a231-3a57-bfe7-126a44dc4df6 | -15.18067 | -43.09357 | 2025-10-18 04:32:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1e58b665-26f0-37bd-a514-a00ebb5760f6 | -10.93483 | -47.56556 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9df44fc3-f752-3466-9394-25bed3df7a6e | -10.90645 | -47.91518 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b6b069a-8de2-3861-8a61-656d01bf8e36 | -13.76036 | -48.23797 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da88e1fe-0346-3f8c-89dc-d6badfa79df6 | -12.65736 | -54.77246 | 2025-10-18 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e954bd4-47fa-3b05-8df1-4d387ff0067d | -13.72585 | -48.11943 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 212aa548-f007-3659-9c38-d939e4a70261 | -11.36388 | -47.29242 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60a6d0a1-e155-387f-bc27-153fea44fb58 | -15.04882 | -46.6091 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95d45b23-f2e8-3c55-bcd8-a8c39370a155 | -13.43919 | -48.11166 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d12d1bf-3f88-3efa-abe4-d8b4cfee580f | -13.25601 | -48.51264 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2acb18f-52e6-326b-8b29-ff9ac53090a2 | -11.60717 | -44.07332 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9a18d80e-e138-35ce-98db-6014e0b1dff8 | -10.91102 | -47.86517 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9410c483-1c13-37a5-80c4-95e0588ecf8b | -13.41041 | -47.97272 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07c95597-28ec-3949-b4de-576739e9d4b6 | -13.03983 | -46.95568 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 416e1ca1-772f-3928-87ec-4d8b41698643 | -13.03549 | -47.28114 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6de5059e-cbcd-36f0-9daa-d24849a49114 | -12.17337 | -45.08294 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee89905e-1192-31d8-932d-7da41a1b9a16 | -13.92239 | -50.25807 | 2025-10-18 04:32:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ebf2313-9b77-3a99-aaed-48adab0bf86e | -13.53396 | -48.00027 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d404dc8-0b5c-3474-b3f1-8e7b23f29cf0 | -11.61627 | -44.08805 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 12689e65-82a6-36c8-869b-1c49a1f7bbe2 | -14.9145 | -46.7225 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d687173f-d82b-3d8d-be18-d7f1d14009d4 | -13.08312 | -43.06126 | 2025-10-18 04:32:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a1ecdb8f-c9ec-314a-b29f-47cce43504b1 | -15.04205 | -46.6159 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 623fb7ce-aaaf-39e1-9188-b36004e361ba | -13.26917 | -46.44298 | 2025-10-18 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dff3a2c4-b643-35ec-98de-d0a9adc76f07 | -11.4945 | -44.23494 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8481c576-275b-387b-b26d-94c5974bb839 | -11.47432 | -44.01541 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb16f7a6-2fcc-3ea4-ac77-13a0d8f9edbf | -13.57064 | -44.44496 | 2025-10-18 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a25a7c85-1768-372e-a13e-184577f8e3df | -15.52979 | -45.70251 | 2025-10-18 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7847d730-5b40-306c-9011-f923bde740d4 | -14.44901 | -52.89695 | 2025-10-18 04:32:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bc8062c-5492-34c7-a160-0da9823aafc4 | -12.79074 | -48.62939 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ce81aea-fd77-3cd6-9456-f9b6968454b5 | -11.85118 | -45.45238 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cdc94d9-2f72-3538-bbde-5b17112e361b | -15.45595 | -45.93735 | 2025-10-18 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fd94602-7b66-399f-99a3-4870dbe3e0d4 | -12.78681 | -48.63241 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fca2760-bf15-33a0-9c72-0e4b04cf4b7f | -13.69267 | -47.72393 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fad7b0eb-3e89-372e-a311-8b245704ce20 | -11.61085 | -44.07387 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5e6674b5-c8cb-3bc5-8575-956a130df48f | -13.44456 | -47.92682 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53f0b49f-dc2c-369e-8017-3792925e0428 | -10.92541 | -47.56043 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41ae490d-2917-35e2-96a7-c4f483603e9e | -13.76178 | -48.12151 | 2025-10-18 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0b135ca-2afc-3186-8973-9f797f56dc00 | -13.4161 | -47.91544 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| feb61f4a-eedf-3af8-acf3-db52e6809471 | -18.51935 | -43.99928 | 2025-10-18 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c55dfae-4888-32c0-9253-83b375c0a146 | -11.8112 | -44.58673 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6cc132d-fff6-3bf5-a96c-bcced483d749 | -15.09002 | -42.12437 | 2025-10-18 04:32:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c34a6aca-d22e-3c2d-8657-11935e10318c | -13.71223 | -40.98655 | 2025-10-18 04:32:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b79e723d-20c3-3c33-83a1-3426c340b47b | -15.03923 | -46.61148 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6a061d8-336f-310f-a569-ee33c291e921 | -10.95134 | -49.769 | 2025-10-18 04:32:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b9ed9e2-3985-3902-9090-e5bf948228ad | -12.8689 | -44.82777 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19a8ee70-5074-3f61-909f-e6abc4914f90 | -14.13067 | -44.70907 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5400ed2-94bd-33bc-9937-ef3429077bdd | -13.77813 | -48.23362 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a2c6b06-a04e-34ad-bbc3-bd915f10b3ad | -14.90998 | -46.72937 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff8ea465-7a80-39bd-9fe7-f63f9ee777ec | -13.08101 | -43.05949 | 2025-10-18 04:32:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 03c5aee3-29c3-311b-ac72-77b73342a686 | -12.46482 | -45.46731 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1f4e9b13-ead2-388f-b122-40b596c68cf8 | -15.03583 | -46.61087 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c514adb-239b-37df-bc54-fe65e2a0f1b2 | -11.36384 | -44.18632 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7b7f48-04d8-31bf-9f91-6d2bd6ca1965 | -15.46632 | -43.20544 | 2025-10-18 04:32:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 781742e2-4cdc-3918-9185-6ef96855ecb8 | -10.81069 | -54.61411 | 2025-10-18 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ac6024f-3d53-345c-83a7-828d96ba6976 | -12.9096 | -48.58649 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a2efb73d-2ccf-336e-8d60-bd38d919cc50 | -13.2619 | -48.56128 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8f85561-81ae-3b2b-95b5-383c240877fe | -17.50092 | -43.46727 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abf0f8b7-8294-3935-81ae-24483da01e05 | -10.97508 | -47.92612 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f21b448-c87c-303d-9f64-a34427e46c55 | -12.16984 | -45.08244 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 341ba28c-0ca4-3b22-a7b8-8af1a3d38dc8 | -13.47466 | -48.12483 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2643d80-e682-3b35-8dec-4fdf0ad5ba7d | -13.45121 | -47.92791 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6127c023-acf0-3f8d-9538-d7360e9af698 | -13.03368 | -46.95102 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README58.md)
