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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f216873-e32c-3d6b-81b9-ce81995ac3da | -13.59969 | -46.9007 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a1ccb27d-7085-3ca2-9b44-f1acb3304bb5 | -16.62846 | -51.38026 | 2025-08-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d2cd69-4c1a-3a4e-8455-68e3d2d7a10c | -17.4922 | -45.85329 | 2025-08-17 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 551fc917-4bca-3730-a5c1-cd180d07189c | -15.64526 | -48.13208 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a34c002a-6c2f-3c98-9387-e2322c622467 | -15.73188 | -48.40771 | 2025-08-17 04:17:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ea0fd91-af1a-3c9c-a300-f9d4c6d07f6a | -14.59088 | -47.94908 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3de13d0-e0a4-3a9f-af3a-757a64511e91 | -14.58777 | -47.94995 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b6eeed83-32c4-3342-895a-4f157b7c8164 | -19.3549 | -43.13897 | 2025-08-17 04:17:00 | NOAA-20 | PASSABÉM | MINAS GERAIS | Brasil | 3147501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 28462b74-181d-3e1d-b4f8-0f488855ffb0 | -15.17695 | -48.76977 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92931b08-ddc9-3227-8329-7608feee28c8 | -18.06387 | -46.35952 | 2025-08-17 04:17:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 537981c9-b8f4-3269-9146-8ca41943853a | -19.42586 | -43.72751 | 2025-08-17 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09027423-bee8-309b-b218-10af14d860d6 | -17.83524 | -46.51433 | 2025-08-17 04:17:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62f694b9-b59f-3342-800d-a5f22f4d9ea9 | -14.18906 | -45.32826 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c21d0827-6b7f-3397-aa63-876a70704bcf | -13.41967 | -57.03458 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 078bbc4c-4489-335e-b184-900471f380e3 | -17.88938 | -39.7671 | 2025-08-17 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ea782370-1292-3a4e-a1f0-ee1763e9dcda | -13.57467 | -46.98694 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd5795c8-46e4-340c-8c3a-71c71ef7ef11 | -21.16041 | -46.75128 | 2025-08-17 04:17:00 | NOAA-20 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 255be4c1-b521-3165-92c4-2fa3ae4ced11 | -14.97478 | -54.74895 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 98fa62c8-3ccf-3a19-b3e7-0f89f6121dcb | -13.60463 | -47.77688 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fd97e0b-737f-3041-a528-26b02b159f6f | -20.38689 | -45.32314 | 2025-08-17 04:17:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0d024c99-313b-3f34-b474-f0573fe748f7 | -19.98564 | -45.51315 | 2025-08-17 04:17:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 788e23b8-6a30-3349-b516-1ad33f0e6d3f | -16.62429 | -51.37945 | 2025-08-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92c51215-0013-3fcb-b095-38887c31d128 | -18.64334 | -43.62959 | 2025-08-17 04:17:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 61707734-e504-3852-9636-73f81f6d465a | -17.21781 | -49.60003 | 2025-08-17 04:17:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2cd299f-b31a-3bbf-851d-91a849299c5d | -14.19899 | -45.32992 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63c7b70a-ea48-392f-ac2e-bfb902dc5e99 | -17.90207 | -44.42308 | 2025-08-17 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b233fac-3253-3b51-89c7-3a305b11d55f | -15.52778 | -42.3374 | 2025-08-17 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e00f7e4d-5589-3e70-9997-709a8cb39dbf | -19.78096 | -46.04499 | 2025-08-17 04:17:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bf57e31a-dc58-3a21-a2bf-76c6b15253ec | -13.58293 | -46.97993 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c651983c-4780-3133-8c7e-dec4cf47b8e9 | -13.61942 | -47.75414 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be8beac8-10ce-3d0a-9349-d05c25958f48 | -20.56873 | -44.87715 | 2025-08-17 04:17:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9afd35d-4df0-36e8-8a27-9fd78bd64c1c | -13.60314 | -46.9012 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d000f6a0-9bf5-30aa-9102-c6fc091f0d47 | -14.54691 | -48.59169 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bebdb00-d037-32e4-96d0-7d5b190cbda4 | -20.7755 | -49.56374 | 2025-08-17 04:17:00 | NOAA-20 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c94d33d-1f8f-337b-bada-a69085763a26 | -14.96301 | -54.76572 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f8dd248-3cd7-3e60-9e07-a4c6ca8ad246 | -16.75732 | -45.06153 | 2025-08-17 04:17:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fffd8932-1f94-3de7-8adf-5c57e165d9cd | -13.59251 | -47.762 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1227f743-0549-39a5-9bf6-3c82b51b34c6 | -15.13986 | -48.7443 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4597556c-d9c0-3e73-a5b3-41858b833256 | -14.36145 | -47.04889 | 2025-08-17 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d90eefe4-bc5e-3a3d-a9da-bfd9fe958e2f | -13.61415 | -46.89865 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71b1af81-8785-3fa9-93c4-448e919989bc | -15.1806 | -48.77051 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 975b5607-d1c4-379f-85fe-7d4dc11cdd9f | -19.16679 | -46.58029 | 2025-08-17 04:17:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 545956f5-2405-394f-a76d-c0f10cd5dbb5 | -15.24344 | -43.85563 | 2025-08-17 04:17:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d403d2-2c56-331f-a6df-3c1ff93c1075 | -14.5937 | -47.95389 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90b63566-bbc5-3922-8f15-02bdb957467b | -16.73543 | -45.99886 | 2025-08-17 04:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca0a3467-abf3-3f1c-9c8a-452a9266021b | -16.03225 | -44.7465 | 2025-08-17 04:17:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c06cf2b0-d937-3e1a-8cee-f0873117d09d | -20.97556 | -44.04116 | 2025-08-17 04:17:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8fdc93be-65b3-3f60-833e-926fd9e56fbc | -18.64391 | -43.62566 | 2025-08-17 04:17:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83b74df6-9bc5-33bd-8882-58963c830c91 | -14.18962 | -45.32471 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05c7487c-5afa-3441-915b-6d4041767315 | -20.21022 | -49.1392 | 2025-08-17 04:17:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad7dab92-579c-3110-a051-630a69fe86be | -14.96853 | -54.75232 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb1ea20d-ff2a-3a2b-a18d-f1da9148bd28 | -14.95631 | -54.75763 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f573fc-68ed-3af5-a23a-cbadec921b69 | -14.19237 | -45.32882 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f52c8999-d025-3b75-a275-0ffc9fe83949 | -13.60244 | -47.74645 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cea8bec-6645-32d5-a89f-9156a11df58b | -14.36551 | -47.04566 | 2025-08-17 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1036c4a5-7440-3a31-883c-e42462b73be1 | -14.37649 | -46.59414 | 2025-08-17 04:17:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a6fb78a-5fcd-3888-9d11-e4a3ac7cbd57 | -15.68649 | -43.21167 | 2025-08-17 04:17:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d1642b6-737a-3b2e-91af-b2fab18f47ea | -13.60173 | -47.75068 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e19632cf-f7c7-3de0-822a-e59599cd12ba | -14.19293 | -45.32527 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cc92c71-7883-3bd3-8159-1eb0ef599776 | -14.18744 | -45.31707 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc35068a-de3c-35cf-ba90-52fa10bb1af5 | -14.58734 | -47.94845 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43e8ff34-e154-3378-818b-96434d4bd08a | -12.99447 | -56.85978 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6ed4b102-9a55-3f12-9da2-ca50c3215df6 | -16.73866 | -44.96199 | 2025-08-17 04:17:00 | NOAA-20 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5649669b-e0a3-3898-a38c-cae54a3e906e | -14.96699 | -54.75987 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b005bb53-225e-3917-8b82-4ec04d002ef8 | -13.65654 | -53.70497 | 2025-08-17 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 187a1d97-b762-35ec-9af4-3f1d40fc6024 | -17.21946 | -49.59065 | 2025-08-17 04:17:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe5dc24a-88db-37e6-92a0-7b9e2426086a | -13.42882 | -57.03429 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 647b776f-7bd5-37c2-b153-b3a510cd388a | -13.61165 | -47.7569 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67e5b97b-1f2b-3ff5-8999-03700050cdee | -15.61984 | -47.63259 | 2025-08-17 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf553682-c0ab-35a8-a799-6bf0fea949a0 | -20.62419 | -47.2568 | 2025-08-17 04:17:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 183b52f7-42f2-3dd5-b69e-3a0a3c7568be | -22.28042 | -55.95625 | 2025-08-17 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d45a45f0-f802-3454-97cf-5eb7fa4ba6a6 | -17.41391 | -48.10628 | 2025-08-17 04:17:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69e1bbff-825d-3b5f-bd2a-6dfc52cf1193 | -13.62876 | -46.91695 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63c931a8-0aef-3b7b-a146-e482f301f9d8 | -13.59238 | -46.96572 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1151d00-26a0-3752-b16d-51ea14ac0d18 | -14.95913 | -54.75714 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8eae49d-5601-3d38-8313-31808d7338a6 | -19.35036 | -46.10657 | 2025-08-17 04:17:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffd619a8-a724-3ed3-a76b-d4dcc2823e9c | -14.93941 | -47.057 | 2025-08-17 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e8f877b-9910-38b0-9576-f14dc3547893 | -17.06188 | -47.1496 | 2025-08-17 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b55bf59e-45d7-34bc-9969-fdd5c8ed6145 | -15.39042 | -47.61784 | 2025-08-17 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a05e928-6952-3fd8-beaf-0745a29575b3 | -20.29096 | -42.20668 | 2025-08-17 04:17:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 86017469-0843-31ce-ac99-b2229cad5de9 | -15.18482 | -53.838 | 2025-08-17 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4806cf55-823f-3ae2-b526-d57ea33646c9 | -17.11432 | -47.9684 | 2025-08-17 04:17:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 795cf571-dc38-33a2-9ed6-d8eb4656b167 | -14.96623 | -54.76358 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6eedade8-e6df-36be-844e-4674190ed5a4 | -15.1835 | -48.77562 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e728413-658e-3050-be35-784b0c71a5dc | -13.427 | -57.03093 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64024849-449d-342f-87c3-d95c3543ca38 | -14.93537 | -47.06021 | 2025-08-17 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89b23e53-5947-3571-96bf-0d8c678898e3 | -14.59647 | -47.95898 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e07fca4-25aa-397e-8ea0-ae7d22316619 | -22.16887 | -56.11551 | 2025-08-17 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1a4a8ae-f21f-38ea-bdef-d20e18248e82 | -14.54586 | -52.03195 | 2025-08-17 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2980710e-8470-39cd-b352-c478f61eb861 | -15.52838 | -42.33328 | 2025-08-17 04:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d47a1f3c-6f49-30e8-b227-336954c82cae | -21.1571 | -46.75069 | 2025-08-17 04:17:00 | NOAA-20 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b7f31eb7-a6d6-38d4-bba1-a7543fa7c4b4 | -19.35093 | -46.10293 | 2025-08-17 04:17:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b110d811-3388-35ab-8a1c-626653ac1fdc | -16.49122 | -45.11341 | 2025-08-17 04:17:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f91db71-2961-385f-a797-358383554bef | -17.27038 | -44.92215 | 2025-08-17 04:17:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2415ce1-9df6-336b-b876-8bd6588ef71a | -19.63076 | -45.27843 | 2025-08-17 04:17:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d81805c-2640-30af-8fb3-564df0cef4d4 | -13.59109 | -47.77039 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c1d2c089-ee53-3702-9f8e-8da234adf523 | -13.42803 | -57.02591 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 888817fe-4a8c-308b-a2b7-20dcd493dbf0 | -14.36209 | -47.04506 | 2025-08-17 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2033d0c3-8693-3f3c-9671-879806b1622f | -14.19019 | -45.32117 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29a6b791-f16a-350d-9086-8b8c6e935f85 | -13.87851 | -45.5511 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
