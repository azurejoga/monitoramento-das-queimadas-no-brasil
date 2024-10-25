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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5db7a693-b77f-3b06-ab80-b15b57a99ada | -3.30927 | -43.51344 | 2024-10-25 15:35:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 398c6d31-f340-30f7-9928-af5e587c3ccd | -3.55088 | -44.00004 | 2024-10-25 15:35:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5e17aa8d-d82c-3716-b987-000a76455085 | -3.37659 | -44.3113 | 2024-10-25 15:35:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| be0c4c38-d5c0-308d-8da1-50d807b4558a | -3.16686 | -44.08691 | 2024-10-25 15:35:00 | NPP-375 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 29f97f6b-0564-3370-b876-e9544eb4c217 | -3.16638 | -44.08385 | 2024-10-25 15:35:00 | NPP-375 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| ae6beea1-196c-3ca3-82df-b2d3f1606704 | -3.61654 | -43.00048 | 2024-10-25 15:35:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67484bf4-75ac-3cf6-b940-8ad19bce0c2c | -3.61628 | -43.00204 | 2024-10-25 15:35:00 | NPP-375 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc0ffce9-908a-3986-9699-be56ea7d92bc | -3.09042 | -42.87506 | 2024-10-25 15:35:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 32ff4c6c-d204-3efb-abb8-ac41a14e12ea | -4.65832 | -43.75422 | 2024-10-25 15:35:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5bbb30ac-8808-33c9-8c4f-c837f9a6482c | -4.59575 | -43.54109 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0ce57d44-5f72-3161-b468-4c87ddbcc294 | -4.59503 | -43.53594 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 37715ffa-935b-3478-a944-fcd4f700fda9 | -4.5604 | -43.56691 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 45b564d1-2f26-361c-822b-657f794c7f54 | -4.5597 | -43.5618 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d79a12af-01ec-37f1-84eb-48a952d45b3a | -4.55955 | -43.5703 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 36faefbc-4544-3d83-a009-70b5bc0187f1 | -4.55882 | -43.56522 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 263c31de-ce6f-356e-b591-e3635ae999e2 | -4.55809 | -43.56013 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fefc1ef1-7ff8-379a-94ab-e10969d20f46 | -4.55046 | -43.58923 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4f0ac40f-3ef8-31d6-939f-12bf632d16d8 | -4.54977 | -43.58412 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 17d47751-f718-39ec-b169-daa6fc6da4e4 | -4.54902 | -43.58746 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 13b7d71c-5414-3798-8c24-867867673da4 | -4.5483 | -43.58239 | 2024-10-25 15:35:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e59de39f-47a2-3c58-ac82-e27b6409a4db | -4.29984 | -43.64249 | 2024-10-25 15:35:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 96855f90-5dd6-39c3-be84-eb367cfdc394 | -4.29913 | -43.63748 | 2024-10-25 15:35:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da45c690-8031-3e65-9af5-9ec77b7839ce | -4.01023 | -43.93306 | 2024-10-25 15:35:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db4ef44d-51de-365e-a44a-d3f9b200073e | -4.74781 | -44.10275 | 2024-10-25 15:35:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86bcce61-a621-3e16-8012-8ecb96ccf8de | -4.74619 | -44.10325 | 2024-10-25 15:35:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 55f926a9-0a1d-3875-87ea-f07c45cd0f10 | -4.13365 | -44.15127 | 2024-10-25 15:35:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88065e97-eedb-3580-9099-f378ca5266e1 | -4.34274 | -43.19972 | 2024-10-25 15:35:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a05493ff-d882-389e-b5e1-97476bf32f4f | -4.22292 | -43.27784 | 2024-10-25 15:35:00 | NPP-375 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ff16b6b1-aeb4-3263-81e0-271fa965eea7 | -3.01621 | -44.84677 | 2024-10-25 15:35:00 | NPP-375 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c3ff12e5-3716-3450-84a1-8fba6b1a1893 | -3.01538 | -44.84086 | 2024-10-25 15:35:00 | NPP-375 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 536a6cd6-bde1-3363-9c42-f4a73609bdd3 | -3.01393 | -44.84361 | 2024-10-25 15:35:00 | NPP-375 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| e1ab13f1-93ab-3dcc-83ee-a20488393d1b | -2.99802 | -44.87601 | 2024-10-25 15:35:00 | NPP-375 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| c5169760-3c0b-375e-9023-4a785ea07361 | -2.99715 | -44.87009 | 2024-10-25 15:35:00 | NPP-375 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 16b981ba-572b-3d5e-a65c-10f62621aaeb | -4.91518 | -45.68245 | 2024-10-25 15:35:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7de18ecc-79a1-3b93-828a-fe08c03e698c | -4.89106 | -45.33417 | 2024-10-25 15:35:00 | NPP-375 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b45f7afa-be8a-3fd2-bae4-7bf44c452998 | -4.85191 | -45.04054 | 2024-10-25 15:35:00 | NPP-375 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 20510ffa-b8a5-3577-a45c-d42445589445 | -3.80668 | -45.32738 | 2024-10-25 15:35:00 | NPP-375 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a7acfae7-30c8-3908-a255-c22e477e69f5 | -3.69239 | -45.06356 | 2024-10-25 15:35:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 34a2baa3-5d38-37fd-bdd3-b53d7845d495 | -3.69149 | -45.05733 | 2024-10-25 15:35:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e60afbfc-f1ed-31a7-bfe5-2fbd00c956d2 | -4.08854 | -39.96625 | 2024-10-25 15:35:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 73c93883-1ea6-3427-aa7f-95d38dfe4b3c | -3.69993 | -38.89218 | 2024-10-25 15:35:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 994ade26-9e2a-3a24-bcb2-6da7c833f3b1 | -3.37331 | -40.51719 | 2024-10-25 15:35:00 | NPP-375 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 845df0c6-1bbe-3c6a-aa27-2dcc2312ab72 | -3.31426 | -40.52497 | 2024-10-25 15:35:00 | NPP-375 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 59.9 |
| e22e0e29-05d3-3c26-983c-c4e1bf0f7032 | -3.43356 | -41.26928 | 2024-10-25 15:35:00 | NPP-375 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8704b612-9dcd-3f56-bf10-ec5bf862f20c | -4.18922 | -40.62967 | 2024-10-25 15:35:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1a78f870-467e-306a-aeb2-2c9bc8319109 | -4.18444 | -40.63358 | 2024-10-25 15:35:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 05d3a3ec-210b-36d9-a410-e30d83877c9f | -4.18399 | -40.63044 | 2024-10-25 15:35:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 78cdec90-c243-32f0-8a31-1c73464f3b46 | -4.18355 | -40.62731 | 2024-10-25 15:35:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 19e89d53-a663-3377-ad53-236a5df4349a | -4.17877 | -40.6312 | 2024-10-25 15:35:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 22026543-cea3-3486-9fa2-bb047e4bb914 | -4.17832 | -40.62808 | 2024-10-25 15:35:00 | NPP-375 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 72.6 |
| c3d512f5-3b69-342e-a5ce-b8cb9c69f141 | -4.02016 | -40.19471 | 2024-10-25 15:35:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 81a898ca-b1b2-3afd-a14f-bd241d0eabe5 | -4.01974 | -40.1918 | 2024-10-25 15:35:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 2ead7a2d-ba3d-3b39-93f1-a8d2e4925bef | -3.81981 | -40.28771 | 2024-10-25 15:35:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| fd9fcf60-5057-3b97-8de0-d2014dbba22c | -3.81939 | -40.2848 | 2024-10-25 15:35:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e32f2023-d753-332c-a2f5-9ef297320660 | -3.81474 | -40.28849 | 2024-10-25 15:35:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 57069cdd-53a7-35f4-b8c0-961fdfec832f | -3.81432 | -40.28556 | 2024-10-25 15:35:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 41463be1-aaac-30db-bc5f-55f3c4f39d7b | -3.79149 | -40.27083 | 2024-10-25 15:35:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 7949cfb0-df2e-35de-a130-e00e9a2a58ed | -3.79107 | -40.26792 | 2024-10-25 15:35:00 | NPP-375 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ec04f2d1-09bf-37c8-926e-5ab2ab8d057c | -3.34294 | -41.41487 | 2024-10-25 15:35:00 | NPP-375 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 55aa3995-c8ca-3543-9ce6-034002b5012f | -3.34244 | -41.41143 | 2024-10-25 15:35:00 | NPP-375 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 0f1879e2-8320-3ae8-b274-ad71ae912135 | -3.3049 | -41.53832 | 2024-10-25 15:35:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 442c58de-499d-30f7-9f2b-e7b4e827f70e | -3.30446 | -41.53923 | 2024-10-25 15:35:00 | NPP-375 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 0c3f8a12-7fe4-3bdc-8850-150caf1ba095 | -3.03894 | -41.4131 | 2024-10-25 15:35:00 | NPP-375 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c48f56a6-3c44-3240-b0cb-6c933a36fa68 | -2.90257 | -41.81813 | 2024-10-25 15:35:00 | NPP-375 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ff5fe1f-b74d-367e-9963-4ad88d1e31c8 | -2.87244 | -41.84473 | 2024-10-25 15:35:00 | NPP-375 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4f0e932-bf2f-3dc5-adea-a46779490e55 | -3.53054 | -42.46021 | 2024-10-25 15:35:00 | NPP-375 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| ef1d745d-34f2-3139-823a-046988bc689c | -3.52992 | -42.45601 | 2024-10-25 15:35:00 | NPP-375 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 3f823bae-f10a-3176-ab53-a4f2f1fd530f | -3.52929 | -42.46259 | 2024-10-25 15:35:00 | NPP-375 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| c8e502ac-7515-3966-84e0-9c6fefd975d3 | -3.52871 | -42.4584 | 2024-10-25 15:35:00 | NPP-375 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| c0397a4a-e5ae-371b-a915-2163e5e7a473 | -3.46215 | -42.39939 | 2024-10-25 15:35:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 7ae90076-08b9-3e80-afb7-1a9eeabdb45c | -3.30405 | -42.52873 | 2024-10-25 15:35:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 548be9bb-a04d-3e66-ac7f-59db00852468 | -3.30144 | -42.84531 | 2024-10-25 15:35:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 44c7564e-4d51-32f1-bc04-ed9e0e864acd | -3.23931 | -42.45022 | 2024-10-25 15:35:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 186371be-dd45-3111-b9e9-1ce1eec40435 | -3.23909 | -42.45032 | 2024-10-25 15:35:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 672029c9-513e-3659-92d1-a94c5489c61d | -3.22866 | -42.7015 | 2024-10-25 15:35:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 09388e00-dcf1-3cd1-ae99-4f8672806ad9 | -3.22805 | -42.69731 | 2024-10-25 15:35:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 677d0ec2-4660-3326-b5f1-156ed46dcbdd | -3.21744 | -42.70736 | 2024-10-25 15:35:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 91972daa-2dce-3c20-aafe-dfcc84798d68 | -3.21152 | -42.70819 | 2024-10-25 15:35:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 11518c30-fccb-3b97-93fa-9a5703e0674c | -2.95003 | -42.68622 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8472f2da-dfaf-38e0-bfc1-84f859c22c7b | -2.94979 | -42.72461 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ff7fd29-634e-3984-9912-d89ff50586f4 | -2.94959 | -42.69946 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6161bf6f-a63b-3208-8694-226f0d225f8c | -2.94916 | -42.72046 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0dd8c734-5132-397b-a64a-e8cf66c90fce | -2.94854 | -42.7163 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0b4cd21-213c-30e6-a5a8-28c7f39c4ea0 | -2.94792 | -42.71217 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89c45c8e-f9b3-3219-bff7-70d8b80a3cbc | -2.94729 | -42.708 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 768ac96d-2d4b-345b-a910-c6a07106be3a | -2.94549 | -42.71293 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d98ad1a7-e33d-324f-8735-5acf78109f3d | -2.9449 | -42.70875 | 2024-10-25 15:35:00 | NPP-375 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21a31c15-3740-332e-8f8a-ef93cd26191a | -4.00784 | -41.91455 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 204e8b7f-572e-3f6e-a9a1-8e4098a5adeb | -4.0073 | -41.9107 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d1d1fac0-a4b6-33da-b4c0-e690e544db66 | -4.00525 | -41.91311 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| effd0af7-1395-3d19-8208-25c2d9dc26e8 | -3.95473 | -41.8844 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ca53b503-1c53-3d67-865e-bc08a2e7dc68 | -3.9542 | -41.8807 | 2024-10-25 15:35:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 93692bd3-9f69-3d51-8d14-defc98c35e16 | -3.86223 | -41.70183 | 2024-10-25 15:35:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c1b15092-3dc6-382c-baea-0478532b0930 | -3.85982 | -41.70155 | 2024-10-25 15:35:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 06abfec3-3c30-32b0-9707-1e171426586a | -3.7989 | -41.95802 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| f8b4b25f-a85f-3adb-b328-423e4589a07c | -3.79833 | -41.95414 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 33d9f6d0-47d6-31d6-8eb9-677c98f9386d | -3.7956 | -41.9583 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 5c133527-aeb6-31b6-bdd4-e183943111c7 | -3.79505 | -41.95441 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| b098a805-9337-3931-a763-885b2ac88271 | -3.79321 | -41.95875 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 60b81630-5c34-3494-80ed-82a428c7a8b2 | -3.79264 | -41.95488 | 2024-10-25 15:35:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |


[Clique aqui para ver as próximas entradas](README128.md)
