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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ee2546b-d293-3dae-ad2f-a7db26e4b915 | -11.7561 | -44.513 | 2024-10-07 11:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b6f74de1-c71d-36fa-b339-645538378575 | -17.6675 | -53.1033 | 2024-10-07 11:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e37bd72f-d387-3d64-8e32-baf55be5a0f4 | -17.8125 | -53.7645 | 2024-10-07 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 161.8 |
| ad823045-0cba-3745-b2db-455c1bf16f7f | -17.7922 | -53.7889 | 2024-10-07 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 08f5b2c6-b550-3178-99e1-1875c80ac7a5 | -17.7926 | -53.7675 | 2024-10-07 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 327.6 |
| 25ddf0a9-3e1c-32ab-aad2-24bb4d6d0d78 | -17.7931 | -53.7462 | 2024-10-07 11:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 410.3 |
| ab3f3e84-954e-387c-8065-afda6c65336f | -18.4718 | -53.5134 | 2024-10-07 11:06:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 79e19151-8d08-391e-9b6e-3b101e839ac5 | -17.6675 | -53.1033 | 2024-10-07 11:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 213.7 |
| 8c96070b-5127-37e2-8ecd-3f4fc8df0e7d | -17.6873 | -53.1003 | 2024-10-07 11:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 9351c603-1a26-30c6-bffc-4a9faacd9720 | -17.6679 | -53.0819 | 2024-10-07 11:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 7c46ae0e-bc47-3de0-ae18-83f35038080a | -17.6877 | -53.0788 | 2024-10-07 11:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| dca8935b-858a-3956-86f0-3d9cbdcd7da3 | -17.7926 | -53.7675 | 2024-10-07 11:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 4239c8f0-3966-33e9-bdce-0a1c409d8c80 | -17.7931 | -53.7462 | 2024-10-07 11:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 714975a8-d772-3cf9-bcbf-6a157861e5c5 | -18.4518 | -53.5165 | 2024-10-07 11:16:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 7dad0298-f42d-3448-a8ed-e59a6ab414c1 | -18.4718 | -53.5134 | 2024-10-07 11:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 198.1 |
| afbf96d2-3dab-3f0f-a7ca-a70c87acdefe | -11.7566 | -44.4897 | 2024-10-07 11:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| e0f22cea-8369-3b04-bf9b-d7d4698078af | -11.7561 | -44.513 | 2024-10-07 11:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 38b0fc1b-b9af-313f-9db3-b189d9eeec74 | -13.8754 | -44.5858 | 2024-10-07 11:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| da8c6977-6110-357d-beb0-8bcdc349f92d | -14.1078 | -45.5241 | 2024-10-07 11:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 12fb4ee1-68a8-3499-a85a-ef66c8396dbc | -14.1273 | -45.5207 | 2024-10-07 11:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| d4e17c11-72be-3467-8c29-bea115681378 | -17.1437 | -51.6989 | 2024-10-07 11:26:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b121afbe-4e4f-395d-a170-d36f7ec8f43d | -17.6675 | -53.1033 | 2024-10-07 11:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| a7dc028b-daca-3271-932e-d4b73f25863c | -17.6877 | -53.0788 | 2024-10-07 11:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c94b98e0-ce6e-39ad-a9e3-a39e77be5e6a | -17.6679 | -53.0819 | 2024-10-07 11:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3bad8b2a-6d25-32a1-9c5b-81005deb8732 | -17.6873 | -53.1003 | 2024-10-07 11:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 5c1076d1-5e68-3404-8f4c-b97a8ca4ceb3 | -17.7931 | -53.7462 | 2024-10-07 11:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 21330327-ff47-3b52-bf1f-57a1e2e7982e | -17.7926 | -53.7675 | 2024-10-07 11:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 38fc791d-f8f5-34d6-915d-5dd4a41b392e | -18.4718 | -53.5134 | 2024-10-07 11:26:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3dee2281-9d94-3d09-a0af-2fec1a9c6ca8 | -18.8899 | -54.4947 | 2024-10-07 11:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 217.4 |
| c051d447-96af-3857-b51e-7db86866aec5 | -18.8903 | -54.4733 | 2024-10-07 11:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 6f4b7339-160e-3767-a88b-0cbd50f76330 | -18.8886 | -54.5587 | 2024-10-07 11:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a961d41d-b250-3070-8c4f-b02744f5c789 | -11.7566 | -44.4897 | 2024-10-07 11:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1bd1b2bd-1c7e-3615-8714-20b111442958 | -11.7561 | -44.513 | 2024-10-07 11:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| a89364d8-d619-3259-9604-60978a6316c6 | -13.8754 | -44.5858 | 2024-10-07 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 32e7a8f5-2503-3ba0-aad6-0d11759b8264 | -13.8948 | -44.5823 | 2024-10-07 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 4a7cb60e-f623-3384-b755-d0a60eef4ef1 | -13.8943 | -44.6058 | 2024-10-07 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 228e71cc-ed37-3c7d-a9f3-2ff99a22005b | -13.8749 | -44.6093 | 2024-10-07 11:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d16a8807-1926-302b-822c-1e09e96a5dbb | -14.1273 | -45.5207 | 2024-10-07 11:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| c003311d-2020-3fc6-af1e-e65f79e15b94 | -14.1268 | -45.5439 | 2024-10-07 11:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| fedebce9-f916-31ae-925e-8d6376a8cf87 | -16.8894 | -47.1763 | 2024-10-07 11:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 119.1 |
| cd2254c6-b34f-3523-bb2e-31eae8b9e4c6 | -17.1437 | -51.6989 | 2024-10-07 11:36:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| f56ddbc6-82c8-3a63-8b4c-230b19f529b3 | -17.6873 | -53.1003 | 2024-10-07 11:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 203.5 |
| da47a382-d735-3b99-a730-f0ad2805bf89 | -17.6679 | -53.0819 | 2024-10-07 11:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 646db7c7-f4e9-39e6-89b3-f5d0d763fe2c | -17.6877 | -53.0788 | 2024-10-07 11:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 265.1 |
| f6b0963f-414f-3162-a762-1aabcf558974 | -17.6675 | -53.1033 | 2024-10-07 11:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 129.7 |
| b39785c0-1b45-33db-8942-1c09a5b4e2c9 | -17.7926 | -53.7675 | 2024-10-07 11:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 09af2e5d-8791-3b0c-9c67-32b6b837be16 | -17.7931 | -53.7462 | 2024-10-07 11:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| d8f76051-bd2e-3743-8bd0-bf81c04d6b61 | -18.4718 | -53.5134 | 2024-10-07 11:36:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 446cb85e-2e15-33e6-a1f4-b28d9846b26a | -18.8899 | -54.4947 | 2024-10-07 11:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 7bcf15ff-7128-3261-80db-008011ad1c8f | -18.8903 | -54.4733 | 2024-10-07 11:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 205e1c4e-d4b3-3cf1-9c26-7f0092d5b160 | -18.8886 | -54.5587 | 2024-10-07 11:36:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e786c99d-a905-30a2-aca2-290205e4b080 | -11.7561 | -44.513 | 2024-10-07 11:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 4dc45fb3-057c-37df-8834-d635460e71b8 | -11.7566 | -44.4897 | 2024-10-07 11:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 17aa0e61-404a-3143-8d92-cb14bc2c2c07 | -13.8749 | -44.6093 | 2024-10-07 11:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 676c6f95-3956-3516-81d8-6f4392aa6ad0 | -13.8754 | -44.5858 | 2024-10-07 11:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 29f9bf1a-621a-3048-9639-69c5f28312bc | -13.8948 | -44.5823 | 2024-10-07 11:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 6ff5f074-5eef-3d83-a81f-3dd006452aae | -14.1258 | -45.5904 | 2024-10-07 11:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 5a509339-918b-380e-a0e2-d5c2580bd665 | -14.1268 | -45.5439 | 2024-10-07 11:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 3da39669-6345-3e04-a127-d1961b8b2e0f | -14.1273 | -45.5207 | 2024-10-07 11:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 6d9569c4-f41e-3f0c-82f1-be981bfcbc31 | -14.1078 | -45.5241 | 2024-10-07 11:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3f6b2326-3a20-382a-8d8e-974c4af5766d | -16.9092 | -47.1724 | 2024-10-07 11:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 5e4ef51f-03dd-388a-b6a9-9ec123016a5f | -16.8894 | -47.1763 | 2024-10-07 11:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 5503eea7-79a9-3009-a191-561a165b43c6 | -16.8899 | -47.1532 | 2024-10-07 11:46:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 101.1 |
| ba662cf7-56bd-36ce-a456-49c6d8e8899b | -17.6679 | -53.0819 | 2024-10-07 11:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 41db85c1-54fc-30b7-8455-118aa7570504 | -17.6882 | -53.0573 | 2024-10-07 11:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 05aa360d-0a0d-3f5b-927b-f39a0d31e550 | -17.6873 | -53.1003 | 2024-10-07 11:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 431.4 |
| d5415cf7-ad01-30eb-9e2f-f4ad49de3cd8 | -17.6675 | -53.1033 | 2024-10-07 11:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 0594bfb0-afc4-39f7-9f79-7ae723360ce4 | -17.6877 | -53.0788 | 2024-10-07 11:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 556.0 |
| 5d05beed-f243-358d-82d7-8cccbc1b91ab | -17.7662 | -53.1095 | 2024-10-07 11:46:46 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| ed06f13f-e320-38fe-8e0c-aaf1dc125ae8 | -18.4718 | -53.5134 | 2024-10-07 11:46:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a467f97e-a977-3dc3-89c2-40a3c32ff84d | -18.8899 | -54.4947 | 2024-10-07 11:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 7c6f2e06-e098-3be3-8730-6245d1d67e8a | -18.8903 | -54.4733 | 2024-10-07 11:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 136.6 |
| a25872e9-d7e9-3068-a636-c79b9c73a28f | -18.8886 | -54.5587 | 2024-10-07 11:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 8f4d466a-9ad3-3cf2-be7e-9843da8b197a | -9.325 | -46.74 | 2024-10-07 11:55:59 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 881d4482-93ce-3bf8-9895-295e38365b13 | -11.7566 | -44.4897 | 2024-10-07 11:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 963d78c7-972b-3ca1-a876-d492812b2619 | -11.7561 | -44.513 | 2024-10-07 11:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 74ea4969-ee33-34f3-9d25-c787d5561958 | -13.8754 | -44.5858 | 2024-10-07 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7b253540-b7ac-3cf0-bd0a-fd0eb0da5343 | -13.8549 | -44.6363 | 2024-10-07 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| f748e118-1c0b-3426-b393-b3e6520c5df4 | -13.8749 | -44.6093 | 2024-10-07 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 04657cde-9494-3419-b29d-16e4119ad227 | -13.8359 | -44.6162 | 2024-10-07 11:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 43cc20b6-dfb0-3e08-9a7e-1701071e40de | -14.1083 | -45.5008 | 2024-10-07 11:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| dc1fdb4d-9181-32f3-b3bd-b8215126d927 | -14.1078 | -45.5241 | 2024-10-07 11:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e860c458-4c77-37b1-9d54-24c9886aeb65 | -14.1273 | -45.5207 | 2024-10-07 11:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 273.4 |
| cc334665-761e-311a-829f-1dcf9745512a | -14.1268 | -45.5439 | 2024-10-07 11:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 8bbad521-f906-31a0-acc3-26809061d33d | -14.1258 | -45.5904 | 2024-10-07 11:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 68a5fe3b-160c-33a3-8572-304c9600f97c | -16.8894 | -47.1763 | 2024-10-07 11:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 1473b252-f5fc-3c0c-9862-2e6d1881b6cb | -16.9092 | -47.1724 | 2024-10-07 11:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| cf210827-e6b1-3369-b85b-392bd643e316 | -17.6675 | -53.1033 | 2024-10-07 11:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 673513c1-6210-39b3-9a23-c9cfb2341e38 | -17.6684 | -53.0604 | 2024-10-07 11:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 268ef97f-48cc-33d6-8775-0b8936ad6d67 | -17.6873 | -53.1003 | 2024-10-07 11:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 195.3 |
| ac60617e-fea4-3fd1-9a88-24aec6ab8457 | -17.6679 | -53.0819 | 2024-10-07 11:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 334.2 |
| 1b41658a-c527-3526-b0ad-5dd13e036b9d | -17.6877 | -53.0788 | 2024-10-07 11:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 281.3 |
| 2e7110a3-06fe-35d6-9f40-a3ada9ff0249 | -18.8899 | -54.4947 | 2024-10-07 11:56:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 26afbc5a-b7c1-3782-9038-5c67c3fba4e8 | -11.7566 | -44.4897 | 2024-10-07 12:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| b7e5d833-5c15-3fb9-a90e-ed9cbc33a6ef | -11.7561 | -44.513 | 2024-10-07 12:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 1084f6c3-3969-35bd-98bb-b754058b8edd | -13.8359 | -44.6162 | 2024-10-07 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6bfde9db-f297-3446-b901-98b4f465329b | -13.8549 | -44.6363 | 2024-10-07 12:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 10d11032-3dcb-3357-9b50-f4c97ed01fbe | -14.1083 | -45.5008 | 2024-10-07 12:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| f35d1239-a375-3d00-84ec-c1fc2c4a3e56 | -14.1078 | -45.5241 | 2024-10-07 12:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 260cc976-22ca-33de-96c0-22445d90f366 | -14.1273 | -45.5207 | 2024-10-07 12:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |


[Clique aqui para ver as próximas entradas](README148.md)
