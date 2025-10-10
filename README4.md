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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0cd20ba-d18f-36f0-b3a6-62233591a569 | -13.46569 | -47.69783 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8fb98967-b94c-3742-98b1-120129faca75 | -15.91509 | -43.30803 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 55.6 |
| cb476792-ee33-3a92-ba8b-dffee4ff57fc | -15.00686 | -46.28179 | 2025-10-10 00:33:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 21867ba6-d52b-315a-b93c-b236ee7f010f | -17.04756 | -49.2254 | 2025-10-10 00:33:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5ade9231-1390-33fd-85f1-14943c7a0c43 | -12.7399 | -45.85872 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 82c0a91c-ae97-3f0f-b756-2021f478e2a2 | -14.43906 | -48.00824 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 28f10c50-6142-302e-907d-0fe1c55b0295 | -12.62874 | -45.05035 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 57afdfd5-8a5b-3a55-b272-423851b4e059 | -11.09849 | -41.0464 | 2025-10-10 00:33:00 | TERRA_M-M | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 81d33df2-b46d-353a-9f5f-7876302c7b83 | -13.31428 | -47.99904 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8e65ad5e-ce43-3949-afc1-edb39c0dc192 | -15.52974 | -47.96814 | 2025-10-10 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a40ca91-d423-35f7-bfd5-7f362315a944 | -13.30314 | -47.1339 | 2025-10-10 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 41aba5fb-9f9a-3790-badf-f038090e4513 | -9.43209 | -40.31141 | 2025-10-10 00:33:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| ec674cda-37ce-3dda-83dc-f2503bad838d | -15.00369 | -47.55714 | 2025-10-10 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3cbb123b-e785-30a1-88aa-1341b42dac64 | -9.43508 | -40.334 | 2025-10-10 00:33:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| aa180a94-53d1-3c8d-88c4-580ce379eb1b | -15.94516 | -48.1823 | 2025-10-10 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7b1efc26-576f-392d-9754-0e1b551bbe41 | -14.06512 | -51.15462 | 2025-10-10 00:33:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0d4e4aeb-db7c-311d-b499-74b326719f0d | -14.81136 | -44.90333 | 2025-10-10 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 091d33cb-81ac-35d3-97a3-bef0ac387ec0 | -13.32329 | -47.74031 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e3487279-f232-3e79-8cf3-0835f9c8d8c5 | -9.6662 | -43.8474 | 2025-10-10 00:33:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 9add717c-cc9b-3c5b-8311-fb1eb22e128c | -13.06383 | -43.09904 | 2025-10-10 00:33:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0eca9661-5bb0-392a-a5f4-915144e749a5 | -14.89448 | -48.23515 | 2025-10-10 00:33:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e7cea483-57f4-3d6f-ac54-0b495a3730c3 | -13.28778 | -48.01804 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d1aeefd-d4bd-39d8-be31-6ca73fb009b8 | -14.26658 | -45.8814 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 27c8d549-cadf-3e0b-aa42-6ef15587ee96 | -12.43172 | -45.77783 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 282a2eca-af8a-3121-a07c-a666e18270af | -14.86137 | -48.47113 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 78fcb7cf-72b3-3af0-ba37-2d368a5586c1 | -13.38351 | -42.71832 | 2025-10-10 00:33:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 1088f6f9-fce7-35df-9079-740ef03b19fd | -15.09009 | -46.60541 | 2025-10-10 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 49dc3457-41d1-3249-b274-e24fcb6deae1 | -14.85126 | -48.46335 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0344a4c5-3605-325d-b644-a5cd04367d9d | -10.61873 | -46.61964 | 2025-10-10 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b6d99e7a-ea38-3015-b30d-0b8f70e2400f | -11.68976 | -47.52362 | 2025-10-10 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 11eb717d-8047-310a-a87c-a22ff945f805 | -15.10691 | -49.56137 | 2025-10-10 00:33:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| af21fb23-43ab-3064-bcd6-075c200f71cb | -17.04156 | -49.23261 | 2025-10-10 00:33:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0f9fe567-fae9-36d0-9fd9-4a85a7397341 | -11.21022 | -48.04625 | 2025-10-10 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8cf47c83-846b-3f70-9796-63b790f9e0fc | -15.09142 | -46.61468 | 2025-10-10 00:33:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7e45ae07-b164-347c-a317-09a75a9dfd64 | -12.63858 | -45.04885 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1c9946b9-4c5f-3fe5-9858-64dd45b03b76 | -13.37123 | -47.74543 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 25e6f848-a34c-3aca-b1c3-920066457436 | -15.913 | -43.29513 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 681.0 |
| 4edd348c-1545-3e67-892f-a26a6b053528 | -14.04849 | -49.48703 | 2025-10-10 00:33:00 | TERRA_M-M | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6e1d9653-90eb-38dd-bd6d-7773914e2196 | -14.7114 | -47.44374 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f681db8d-966d-3f43-8b0f-31f3f2d1390d | -11.87552 | -45.49868 | 2025-10-10 00:33:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4467fa99-06a7-301d-a2b5-98703c72f1dc | -14.62394 | -48.1448 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9fbdc074-4ba6-3e36-8103-085a06ca92e2 | -13.27897 | -48.01934 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a0a7f3e4-b264-3bf8-a475-f12b1efe5ce9 | -16.28421 | -47.16579 | 2025-10-10 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 75ac5a81-5d52-3052-b080-2ee921962598 | -14.26948 | -45.90138 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8210b413-d35f-3b0d-a4d4-5f878270963c | -13.42034 | -47.64602 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| db1e706b-e356-3965-a969-28fde5f2a92f | -14.44414 | -47.97972 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 19b96b11-c0bf-3443-a9d0-dbdf9f5f0db9 | -13.33211 | -47.73899 | 2025-10-10 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 2d12511b-0ac4-3698-adfe-bbf95edbfefe | -13.39136 | -47.76079 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d1223082-7346-3834-a416-22f7bf694fcb | -16.29303 | -47.16443 | 2025-10-10 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2f3d7ae7-c336-3881-a790-744e80083e12 | -12.4475 | -45.75397 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 95fa94ec-dc5f-399e-a305-7641f4e132db | -13.87964 | -44.24718 | 2025-10-10 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a29f4bb2-ec16-3c89-a61b-8f4f33bd93de | -16.11935 | -47.90937 | 2025-10-10 00:33:00 | TERRA_M-M | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85122dba-1c91-3c6f-84ba-d5a26f8731f0 | -11.82249 | -47.09647 | 2025-10-10 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1777778a-2127-37cf-bf68-cc70f7a2620c | -15.82571 | -43.77044 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 48.7 |
| edb5646e-5f07-36ad-a75e-7da9c0f6e4d0 | -13.05569 | -43.83907 | 2025-10-10 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 1c3549f4-72d9-35c7-953e-6fd3e6df75c8 | -14.02447 | -48.14591 | 2025-10-10 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 98a8aa20-59f8-330a-8379-d4633e02267c | -14.84237 | -48.46471 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e5898c20-b6bc-3154-bf50-2b5c964c252b | -15.40765 | -48.02649 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 10acdf1b-81eb-3b7f-a63b-5c9b35fc8eee | -15.40006 | -48.03698 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 45.5 |
| ff6deade-9b7d-36b7-9a4d-ea53af6f2a4d | -9.00436 | -45.48445 | 2025-10-10 00:33:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b6e16486-429a-3c1b-90b1-539a16a39609 | -16.30057 | -47.15396 | 2025-10-10 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4dff2ece-d692-3b36-84ed-f3680c8ab692 | -11.21148 | -48.05522 | 2025-10-10 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a22663f4-a0c8-33d9-a3ff-61184b51b8b3 | -13.52443 | -48.12139 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5a001507-f23c-3abd-ad5b-3ccdb4f66fc4 | -10.15899 | -44.5801 | 2025-10-10 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c3b2af3b-53f8-38b8-999c-8acb7efbd790 | -13.84575 | -45.84977 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a920cbe-9d81-360e-9077-e45204a286d9 | -14.5577 | -43.51565 | 2025-10-10 00:33:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 857a91b3-51cc-373d-b334-ca8aa815e345 | -15.40891 | -48.03566 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| e0a298ec-50d9-36f8-a207-96961141b9c0 | -15.46658 | -48.52657 | 2025-10-10 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b8edf0a6-5efa-30e0-90a7-e7959a65bd0f | -14.67575 | -48.0626 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cee2c53a-10ae-3e4c-8580-299beef8b719 | -13.41027 | -47.63831 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b654f1f5-a8db-32fa-ba87-f5d80d7e1024 | -14.26803 | -45.89141 | 2025-10-10 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 109b7687-99bb-3741-82f9-56155903e7f7 | -14.93115 | -46.78413 | 2025-10-10 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 46b4c5db-00bb-369e-984e-cc6b92b28df3 | -13.07055 | -43.86412 | 2025-10-10 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 56fa3fee-a135-3732-8a83-3bded5006d06 | -15.74165 | -43.94921 | 2025-10-10 00:33:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8fe98510-7fb5-3234-bd33-63a34385607a | -13.46694 | -47.64242 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 82c81a87-3249-3489-8c6b-cd75aad5380f | -13.83319 | -45.89272 | 2025-10-10 00:33:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8f7cb2f2-d7c0-37bc-9bf8-d6340624e8b0 | -15.32593 | -43.1877 | 2025-10-10 00:33:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b33871a0-df58-3d3b-b975-e7e1a0452e3c | -12.63044 | -45.06164 | 2025-10-10 00:33:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e20047f6-64d2-359e-99fc-57e3067b0808 | -13.06843 | -43.85072 | 2025-10-10 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9538456d-c948-34a0-9c17-03c8efc053b6 | -13.05783 | -43.85252 | 2025-10-10 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 693cf9b3-c063-32ba-aaec-08d8c379ab39 | -13.46694 | -47.70682 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 04b16f10-348b-37bc-b619-86130f19568a | -10.99967 | -45.12325 | 2025-10-10 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 085a4211-7089-3148-b478-f54be53a1580 | -10.94061 | -42.85257 | 2025-10-10 00:33:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| ef6a25b3-4abb-34bd-a534-8fdf8d41e49e | -16.27539 | -47.16713 | 2025-10-10 00:33:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c83f011b-6b9d-35f9-8d19-830fd59ffb3c | -15.10364 | -43.46761 | 2025-10-10 00:33:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b4719849-900d-3654-a31f-8d81c69b18a6 | -14.63278 | -48.14349 | 2025-10-10 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff5db26e-bede-3ee9-af76-e1e0f0bad20a | -12.22896 | -43.79458 | 2025-10-10 00:33:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dc87ab7c-5048-35a6-b31f-4b243b7180d2 | -15.91087 | -43.28204 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 8ee3de4b-a1a5-340c-9730-1798741d3b5b | -12.48018 | -46.92547 | 2025-10-10 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ee4409a6-9aff-3671-b435-7470a797edac | -15.74916 | -48.98932 | 2025-10-10 00:33:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 980bf8eb-eb54-3423-a2bf-126dba4de14d | -8.60071 | -41.42041 | 2025-10-10 00:33:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| eaa20c14-c988-3f44-a50f-b8b0b186f7a6 | -13.41908 | -47.63702 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e42ac156-4dbe-3384-9cdb-95c3f957968a | -13.32309 | -47.99773 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 67242fb0-20ae-3625-b211-b9d41b2497c6 | -13.07507 | -43.09712 | 2025-10-10 00:33:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| c0a9ac9b-b289-361f-8a5f-90ecb142c260 | -12.9538 | -43.95045 | 2025-10-10 00:33:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 710f4906-14d1-3425-8aac-7229d95ed89a | -13.39011 | -47.75179 | 2025-10-10 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b7802c88-f7fc-3939-8c95-a78e9394683f | -15.74 | -43.94305 | 2025-10-10 00:33:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c8065399-9588-3c37-9340-96655fa76871 | -17.90744 | -57.5094 | 2025-10-10 00:33:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| a055e4d5-372b-3bf8-9e7d-d7d459c855eb | -15.91875 | -43.29994 | 2025-10-10 00:33:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 502eafff-53b8-3831-9158-954d6f198a3a | -11.21905 | -48.04495 | 2025-10-10 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README5.md)
