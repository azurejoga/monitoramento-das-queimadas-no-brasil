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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac0c0151-4c9c-3b9c-b455-4cd7707f7bf2 | -13.23285 | -51.36906 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 830e6ac9-1b60-3466-9262-63a64ec67587 | -10.76359 | -53.98949 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ded12dfa-fbba-31dc-ba1f-9f1e0f096fad | -15.14546 | -50.06258 | 2026-08-26 04:53:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbae6600-ee76-3a96-8a01-78dc317e7ae6 | -9.45545 | -60.53026 | 2026-08-26 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4800289d-8b43-392d-947d-5e04e8103fa0 | -9.9684 | -53.96472 | 2026-08-26 04:53:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 511d4312-f688-3254-b0e5-3840f58502a2 | -13.23044 | -51.51124 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01e04dd2-2323-38f0-9e16-42352cebd90c | -13.25048 | -51.52262 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| cd02f925-1f08-3596-838d-3093345369ea | -12.77103 | -44.26212 | 2026-08-26 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07f39e6f-f1f9-3046-95b1-e6285ed678b4 | -9.65957 | -55.14134 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39c3e4cb-dccd-3aab-9a89-a245557af50c | -9.48838 | -56.9211 | 2026-08-26 04:53:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91f63e66-6ef3-3819-9e41-10d7e180a165 | -11.31129 | -55.20753 | 2026-08-26 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12844114-4ac5-306f-8bd0-96c32563b7ba | -13.23522 | -51.37786 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1c9df471-59ad-3661-9416-70d3651a0731 | -8.81401 | -62.31507 | 2026-08-26 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22b988ab-138d-3550-857b-a62dab389f8b | -13.86119 | -54.02867 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd481ae3-088c-3208-8f3d-25306fa9eb7c | -13.65462 | -51.84736 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5c4eef75-b767-3b99-893c-0e7d7c3d7493 | -12.08672 | -64.23763 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3698684a-0801-303c-915c-470620bbf37d | -13.87306 | -54.08481 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55b69c4a-b27b-3dfb-96a1-d16b2097d28c | -10.76357 | -53.96797 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9df0d046-7b23-3753-84b0-c4eacaa4d8f7 | -10.61087 | -52.22225 | 2026-08-26 04:53:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f30411b8-91d2-34c1-9bfb-45300d4f08ed | -15.60209 | -53.11753 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 573d6bea-a144-3739-9e98-e5867e6aea66 | -12.68688 | -48.40819 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 45182071-7605-31a2-b7d0-ee57afa855be | -10.64994 | -57.24802 | 2026-08-26 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 682185dc-2f92-30bb-847b-2f25b22f2dc6 | -9.17933 | -59.38784 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdbcdf61-2a21-3a22-a5b7-3e066d85866f | -12.67439 | -48.40536 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f0056b9-1b5f-3ada-b4fa-18e8340c04af | -10.75367 | -54.00943 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52075cf8-42f2-3eb7-9d34-407161b5e398 | -13.28697 | -51.46824 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e87038-c028-3c42-8f7e-1e4774edd366 | -13.29879 | -51.46167 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| ced5f2fa-61a1-363e-badf-a95d930df2cd | -13.75311 | -51.99842 | 2026-08-26 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c8eb267-8357-3690-91b8-68242a2b820a | -14.38623 | -52.91199 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ff296ff-008c-34d8-9dab-e947194ced51 | -12.76744 | -46.44362 | 2026-08-26 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5091948c-4093-37ae-93f8-12a90f087ee1 | -10.7669 | -53.99002 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c05d888-7a50-3d8c-bd20-e10c1d1db986 | -11.76335 | -54.53013 | 2026-08-26 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c68a82c-3eed-3f2e-a161-137aba08ca84 | -9.39175 | -55.97466 | 2026-08-26 04:53:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb85e015-285a-3bf2-a22d-0dee509dafdc | -12.03571 | -46.02852 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9454fbeb-c05d-3417-8e15-2d4d6c82560f | -13.25815 | -51.51963 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9adbe488-1b7d-35d4-b45d-cbb9c0312fd1 | -13.24175 | -51.38307 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 069ddbaa-07c5-374b-b182-dc4a6fff580f | -14.79782 | -48.80444 | 2026-08-26 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e2b1157-d0c7-3fe7-9c35-8da5f6a9e296 | -13.23759 | -51.38665 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c6421ec3-ce99-3f43-a1f2-3495431caf4c | -12.7292 | -48.38101 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e219da5c-4f7f-3332-b517-d76d593d36cf | -13.87357 | -54.05944 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 147d3548-5d58-3b3d-9546-c92d7d2b60c7 | -12.74966 | -46.46766 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f1255e0f-5293-3e8e-8e95-cf4a73395b24 | -9.67058 | -55.09408 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bebafb5-2400-3050-8fac-fd12ca41c8d4 | -13.38856 | -48.22299 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f344328c-56cf-31d3-b51c-dc3a76482d8a | -12.43101 | -51.16947 | 2026-08-26 04:53:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4832e580-a40c-349b-a9b1-1936fbccedeb | -13.8645 | -54.02921 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d90ca5e-5dce-3544-a8e7-d78e6f64fa59 | -12.07769 | -64.2429 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3ff6dd2-f7f4-39f7-831a-138c9e21487a | -14.12751 | -52.36014 | 2026-08-26 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9136e5f-a11b-34f5-8227-7c940284ca10 | -13.33702 | -48.21514 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0ab15e45-104d-365a-bcd7-fc7c5c54c497 | -12.76542 | -46.45914 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16b473bc-5e64-3035-83eb-14058d1e7ced | -8.65092 | -62.89325 | 2026-08-26 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67dc4858-2fce-34ae-b30c-4e3c44a9f1f2 | -9.661 | -55.08878 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f83b7654-891b-360d-ae59-501cf60f63e3 | -14.38305 | -51.7611 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6114dde2-16db-354e-8fb8-4ef1e2a71a8f | -13.22985 | -51.51531 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6769c05-f8ed-3457-8d1d-54f1d8df52a5 | -12.68271 | -48.40733 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| da3458eb-5efe-3cbf-a0d2-77faa6c3dfa1 | -12.89691 | -59.92097 | 2026-08-26 04:53:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f936dfb-3412-35c1-9599-55b5829bf941 | -13.25402 | -51.52316 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 082873bf-c457-3307-8eaa-ffc517dd5d64 | -11.21196 | -55.0839 | 2026-08-26 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca9ae4c0-9764-3e9c-860c-42f6957e137d | -9.18002 | -59.38381 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61496932-43d6-372a-8401-0279b0e2e326 | -10.64627 | -57.24738 | 2026-08-26 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4425e053-2c35-305a-9864-2649809efc96 | -10.53297 | -50.77597 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d826ade-b33f-3708-93e9-eaba5b62aba9 | -10.75809 | -54.02449 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fc85f286-6a7d-31c3-b0bf-2196f181ce1f | -13.25107 | -51.51855 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d01f3560-2d6a-3e21-818c-5b10a00ec4a9 | -9.13435 | -57.56349 | 2026-08-26 04:53:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25d29cda-0ec4-3fc7-89d8-2b583fe3e975 | -10.83793 | -50.53751 | 2026-08-26 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05e07bed-5ebb-3f03-9460-3540f3ba0fb4 | -13.85623 | -54.03877 | 2026-08-26 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f468523e-0dc8-316a-8d4a-44a49998c997 | -9.09517 | -59.41528 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b1648c2-57d9-3815-968c-d0eae7e9ec28 | -9.20122 | -59.58304 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d771489-a4d8-394a-a73f-6822007b7805 | -12.03358 | -46.0452 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc7e1037-010a-3d65-b772-f548eeea3c73 | -13.34293 | -48.20351 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd1e5499-1aff-3af2-b9b9-45da96325020 | -12.08252 | -64.24789 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e423d06a-302b-3504-bd9a-456d99379743 | -13.17459 | -51.34925 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 608a86ce-48e3-3a8a-aa3e-63fa47304086 | -11.37546 | -45.16084 | 2026-08-26 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba3c1a16-9bfe-3176-8c91-b3ceb2bc7766 | -10.75588 | -54.01696 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ad14e10-a384-3607-a465-c8e8caaad27b | -15.60493 | -53.12184 | 2026-08-26 04:53:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c2a9f64-14f8-3729-b423-e17f23d32088 | -9.09659 | -59.40714 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4046f66b-6d20-3190-a11c-a5d639c9a786 | -14.29997 | -51.11479 | 2026-08-26 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebb3043a-7601-3b40-b282-5d894c0af64b | -10.77023 | -54.03362 | 2026-08-26 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 84b6580b-2f24-34e7-bd75-db64796eed44 | -12.07966 | -64.24415 | 2026-08-26 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e475da27-190f-3472-8e74-9a02492aa09c | -11.19716 | -55.07721 | 2026-08-26 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f6fdb5c-f787-324d-8986-44a98a436f1c | -12.69905 | -48.41335 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 29197d55-f36e-3708-9c2a-da90307bd0f7 | -14.38907 | -52.91626 | 2026-08-26 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62be6c93-9ffe-34b2-8045-9d6fd3eac3a9 | -10.39379 | -48.27221 | 2026-08-26 04:53:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3541037f-5372-37e3-ab3d-af5085603af3 | -12.75997 | -46.46349 | 2026-08-26 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42228566-501b-3027-afb1-8ae56e734024 | -11.49985 | -45.06414 | 2026-08-26 04:53:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 212c7448-1ebd-30a6-aa84-22f87f3b206a | -14.3624 | -51.75375 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63138c4b-f4b0-32ea-b5cd-070b8c0abe03 | -15.88217 | -48.3545 | 2026-08-26 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06f5fc79-2b78-34a8-943c-3cc04e7067df | -12.7124 | -48.3781 | 2026-08-26 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e0cb683-8f3c-3066-a223-b1be405b9490 | -13.33983 | -48.22715 | 2026-08-26 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a14a2774-4187-355b-b888-d610f1e06ddc | -12.035 | -46.03408 | 2026-08-26 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22270276-0dee-31c8-89e0-fd592aee370e | -13.61339 | -49.01524 | 2026-08-26 04:53:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0387dab-82f7-3ed1-8990-d2878d535ed1 | -13.23463 | -51.38198 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b06a73f4-3d27-3565-89ca-ea91b027dfb7 | -14.37951 | -51.76056 | 2026-08-26 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 925765fb-0b98-35f0-83a0-c2c87b3692c1 | -11.82248 | -47.65651 | 2026-08-26 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1f7e30f-66b0-36c4-a447-8c8deeb0028d | -13.1966 | -51.34243 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3354b6cb-3ef7-34c1-894a-4ebe19abcdc8 | -11.21138 | -55.08752 | 2026-08-26 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 741412f5-3864-3836-802e-e195126094b2 | -7.90244 | -63.68778 | 2026-08-26 04:53:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b643c9f-fad5-3c08-b28d-2d19619d9051 | -9.1014 | -60.90994 | 2026-08-26 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 768a12e7-9da5-3a76-954a-d1082acb5e44 | -9.6015 | -55.11303 | 2026-08-26 04:53:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 95f3d5f2-7562-3e61-83c1-adc9de18ae45 | -11.42054 | -62.09169 | 2026-08-26 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d529c99-8b7a-3d8b-b84f-b63c9cbb6736 | -13.24354 | -51.37069 | 2026-08-26 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |


[Clique aqui para ver as próximas entradas](README48.md)
