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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c1f316c-ab57-3380-b950-c5894d4a6eb3 | -16.03632 | -43.7263 | 2025-07-11 03:47:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 572b1149-c145-3d93-aedc-be135cc04d61 | -11.32224 | -45.22 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fb94b42-a667-33ad-b5fc-f20e2d85fac5 | -13.36001 | -47.89074 | 2025-07-11 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eba11c34-e9dc-3209-a30f-2e7b31602ed2 | -9.90998 | -47.8397 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f7c8fbd3-8ed2-3d3f-8415-2899043dd2d5 | -12.40138 | -45.36114 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa318b56-36b1-3385-88a3-3dea626598b2 | -13.13426 | -47.29735 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7c3b633-bec4-3ee6-b617-e65af5f4d650 | -12.4002 | -45.36741 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a76a6d5-0a45-3dc8-acf6-1ec4dfee9d11 | -9.85712 | -47.87663 | 2025-07-11 03:47:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07878fbe-965a-38f6-8971-df61276b518c | -10.56872 | -49.1442 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5eb203db-8785-30e8-b4cc-2b31640e859b | -12.46562 | -44.49823 | 2025-07-11 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eec611f5-b2a2-32bb-9a19-4936c2f68276 | -10.64089 | -45.22889 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42371d35-a971-3ec5-90c2-aea533eade43 | -12.98517 | -44.85941 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c0df1d8-cae6-3c06-aecf-86dfefa39468 | -13.1326 | -47.30376 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78fdd1e5-6ead-3ea2-a5b8-11c303206ced | -9.91104 | -47.83416 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e73ed35d-7483-3b59-9b4d-197de430795c | -10.62327 | -45.23544 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b147eb8-5f39-3700-85b8-9f3d0761a8ac | -13.00758 | -44.87585 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18f0f836-dc3b-302a-8a56-4674c7d6770f | -12.99757 | -46.27949 | 2025-07-11 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6683ace6-9987-362d-ad44-83a91e65b410 | -12.41223 | -45.3602 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 338bf0bb-09bc-3030-ae8f-6f4a8780bbe4 | -10.85046 | -49.11687 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7dfb1d48-432c-3f15-a272-d36480d86c35 | -12.41164 | -45.36334 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35fd2935-a097-391b-a5cf-ccfcc983d6d7 | -13.15343 | -47.29135 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94fcbbf2-0202-3bb2-b5b9-3a351ad125e9 | -13.84608 | -45.85399 | 2025-07-11 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 914cffa2-b124-326f-9e58-29733bc4a0ae | -10.66856 | -49.49678 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| df95c007-a1ac-3a97-b5fa-8e8f43d8dbc5 | -16.03712 | -43.72204 | 2025-07-11 03:47:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cc23baf-85ed-3687-8666-af9fefc494f6 | -11.83682 | -47.50423 | 2025-07-11 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7c7b92c-7af4-303d-9524-45e030ebd992 | -22.90109 | -43.75266 | 2025-07-11 03:47:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3e0349b9-3152-3bcf-9efd-e1712167b8ed | -11.27061 | -44.89431 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6495a806-8823-3b33-a846-e57f8bb119f7 | -9.6118 | -49.01883 | 2025-07-11 03:47:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48e4b160-3292-3c14-9d0a-bb975b4c9884 | -11.44897 | -45.12124 | 2025-07-11 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d350884-5765-3be6-b2c6-72157760303b | -10.62451 | -45.22893 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a687f61a-1ac0-3535-876b-2ebfbf3d2f34 | -9.91727 | -47.83569 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| babc7212-23a4-317c-9702-c8d8b5f28f87 | -16.04144 | -43.72294 | 2025-07-11 03:47:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ee16df7-e639-39a7-ab0d-1fefdfe1edd1 | -9.91332 | -47.835 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| a0d8a26e-e158-34cd-9648-fa9eec847f8d | -11.26552 | -44.89328 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac6a65d2-b769-3fdd-9662-3e78d2dc45f7 | -21.68857 | -49.49798 | 2025-07-11 03:47:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 6ec7873e-c60d-3014-9fec-63e7fe600031 | -14.56133 | -48.14294 | 2025-07-11 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f819a6ef-8321-33b8-b970-e7f1ce1c0005 | -11.44442 | -45.11708 | 2025-07-11 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 821dd22c-e451-395f-8400-1b73c84a084b | -12.05472 | -48.55149 | 2025-07-11 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4170b707-cc03-37ab-9a23-a2b614048732 | -12.40592 | -45.36536 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f244f5d-29ea-38de-9bb7-937d4394abf8 | -12.98796 | -44.8715 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4613436d-1c0d-348e-bb15-0307e45bf20a | -10.62589 | -45.22969 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b561bd1-92a2-3276-ad61-c0a1323c14dd | -10.67786 | -49.48519 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| faf4909a-c5b8-3d13-b562-bf91662db408 | -21.53754 | -49.52976 | 2025-07-11 03:47:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 11eb0df9-81f3-3b89-bd6f-84ffbcfe8977 | -10.66979 | -49.48984 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 2de033fa-34b7-33af-9631-e66d0af1419d | -14.39634 | -43.77357 | 2025-07-11 03:47:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82172149-f5c3-3b28-9f2c-503076b547f3 | -12.41609 | -43.48599 | 2025-07-11 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df1408cf-5c67-3225-ae2c-712f47cbe906 | -21.68949 | -49.49389 | 2025-07-11 03:47:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| fc5e27b3-4b96-3f7c-a01b-bcdafdaff8ec | -10.57549 | -49.14527 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c5b0009e-2ccd-341a-b7d5-7c8512b730e7 | -9.91302 | -47.82381 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 66ebccc2-0337-3619-a6c0-8d3244444dda | -12.4071 | -45.35909 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54097c40-1de2-37aa-8d9c-efe307d4d4ab | -13.13908 | -47.3012 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a562f55a-90b2-306a-80e7-59fe93d70502 | -10.8454 | -49.12304 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6cd52798-8273-3120-a958-a289a61b98a5 | -9.91828 | -47.83037 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87406ca2-f510-3303-b66d-c56899923f8f | -13.35846 | -47.89828 | 2025-07-11 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c8e835d-f3ba-3861-92c1-4a7b0bcabbef | -10.62005 | -45.23183 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f9ffbd1-0264-3485-8e79-30807bbc583b | -10.67657 | -49.49144 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4a8af954-855a-38f8-ae29-9b646b133eaa | -18.68808 | -48.12209 | 2025-07-11 03:49:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58a6a56c-f1ba-3e4a-ac62-6845be0de264 | -19.44469 | -48.53484 | 2025-07-11 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acf6c8d4-349b-39ff-a99d-cbfc55e8247e | -19.45011 | -48.53648 | 2025-07-11 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1287e30f-0cbc-343d-bc65-3537ee988a93 | -19.43798 | -44.34083 | 2025-07-11 03:49:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4ab3978-6f2c-35ad-acef-6562d14544c7 | -19.44901 | -48.5342 | 2025-07-11 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 744ee835-2ee6-3626-be88-029d962cf189 | -19.44382 | -48.53885 | 2025-07-11 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6047af0-9a6b-3800-89c1-366cc2d0c2cf | -24.31551 | -50.85332 | 2025-07-11 03:49:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7fa2435-a5a1-3bbf-910c-86690b9da06f | -18.68727 | -48.12581 | 2025-07-11 03:49:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed755dd4-3c39-3c0b-966b-e3b93cfe6ffd | -19.44923 | -48.54059 | 2025-07-11 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4700849-dcd7-393d-9844-95286cd217d3 | -19.44813 | -48.53815 | 2025-07-11 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 041db04e-fcf7-327a-b56c-930f8ea56e07 | -24.3165 | -50.84915 | 2025-07-11 03:49:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74efccf1-df5f-3621-818a-b0876014a7fc | -5.5427 | -43.9096 | 2025-07-11 03:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| beb77fbb-2c33-398d-843c-18690539c2a7 | -5.5429 | -43.8864 | 2025-07-11 03:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3ac31099-1b04-39b5-9734-63bb8b83e985 | -10.6862 | -49.4874 | 2025-07-11 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| a0f875b0-cf74-310e-85ab-825ddcd89616 | -9.9148 | -47.8282 | 2025-07-11 03:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b2b3d957-42ac-35eb-b252-9c83391364c6 | -10.6672 | -49.4895 | 2025-07-11 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e8db2f78-c713-3521-9bdd-6b078295f68f | -10.6862 | -49.4874 | 2025-07-11 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 14727267-9cd0-33ef-bfa9-44bbf858332f | -22.2852 | -54.9409 | 2025-07-11 04:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 568d82a3-f4f7-3b8c-8174-9305ad89dd52 | -10.6672 | -49.4895 | 2025-07-11 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| d7525924-c6cf-3917-bd8c-a6a313555ae6 | -10.5776 | -49.1316 | 2025-07-11 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2885ecd7-c9d0-34ba-85f7-4f7ea380aed0 | -9.9148 | -47.8282 | 2025-07-11 04:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 194574fe-7567-309a-a5ed-ec8df29e8d24 | -4.59333 | -47.72201 | 2025-07-11 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c18b097-ae66-3abd-b856-ff9418df9008 | -7.18105 | -43.36414 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6697ed4e-bf47-39ba-9be0-a215e3097540 | -6.10579 | -44.81749 | 2025-07-11 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af99ca06-f56f-3b09-85b4-8288aaa939e8 | -6.84642 | -42.78331 | 2025-07-11 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 295d7ae8-d072-3b45-8583-d08036ca3b22 | -6.89363 | -44.05394 | 2025-07-11 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4b18c41-388d-31db-83be-b88b56c46736 | -4.78522 | -45.34529 | 2025-07-11 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 607d4c59-2fce-3fa4-befa-898cf0e807ae | -6.27664 | -42.37209 | 2025-07-11 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e5a56f8-1e5a-32ce-8eda-70fbce0a0018 | -6.72247 | -43.89888 | 2025-07-11 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6805d34c-9ab4-3c87-88f8-11dbbe2fb1b9 | -4.81787 | -47.32144 | 2025-07-11 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac481ad7-d475-3c86-b5ba-72a56cdc819e | -5.98032 | -43.75877 | 2025-07-11 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96878f69-b118-3ec0-9118-1b12f23fdb71 | -3.74715 | -47.11033 | 2025-07-11 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97824c24-fa08-357f-ade0-d1a2e0b5dae2 | -6.51098 | -43.33541 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74aaafae-c387-3e6c-8a5d-215ca1e3e708 | -6.7355 | -39.04348 | 2025-07-11 04:06:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12025788-1b7c-34c7-9565-7747ce957806 | -6.51494 | -43.33231 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f193019-97d0-3686-aee9-63d0d33ed3df | -4.22127 | -47.21199 | 2025-07-11 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbd82950-3f1b-39e9-b6b8-e6a1fe14e142 | -6.67213 | -46.30613 | 2025-07-11 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| baf1d0f6-7ea6-341d-a970-c0e1bd21bcc2 | -5.91482 | -37.39561 | 2025-07-11 04:06:00 | NOAA-20 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07f14185-93bc-33ef-ac24-baeed4cd65c6 | -6.87714 | -45.23255 | 2025-07-11 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a76a5c0-1e9d-3825-b57f-1f2a6befe14c | -5.54716 | -43.90387 | 2025-07-11 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceafe4a5-01e8-33af-8af4-20c7fad2350d | -7.18941 | -43.37666 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6b870c34-2e9c-34e0-aae8-1ceca6460529 | -6.65125 | -43.19061 | 2025-07-11 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0b7447ba-19cf-3b26-9e49-dc260ac17585 | -6.73686 | -43.89742 | 2025-07-11 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fca36b0-c633-3fd7-a371-327a9a1ab2ff | -7.19 | -43.37303 | 2025-07-11 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README10.md)
