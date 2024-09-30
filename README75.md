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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 834830ee-313e-3314-b01c-fc45dad9ebeb | -12.07835 | -50.01514 | 2024-09-30 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1ad4c5a2-404f-3fb8-b6ed-3991886cd7bd | -12.03881 | -50.04842 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f9968ca9-ddb4-35f5-ac7f-82fbe7c852e1 | -11.95935 | -50.18785 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 45f4f990-737e-3288-828f-48b3c1e7debd | -11.9592 | -50.1777 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 127b93c5-623c-3c58-9d02-c885adc0f37b | -11.95661 | -50.19331 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c0d4c294-6db1-334d-985e-4dec0db3cb8c | -17.6403 | -53.1528 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| bc9ab95b-3288-3db9-8e8f-52bde8ee036b | -11.85309 | -49.62114 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f25f9592-cf02-3619-a6ac-6cdcd458e260 | -11.70217 | -49.92083 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7d2dc062-e356-312b-a725-70026f69bd80 | -11.69976 | -49.93593 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 76419067-58bb-35a6-9401-c481a9ae905c | -11.15873 | -49.71706 | 2024-09-30 12:34:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e263c01f-439d-3290-a567-448613a8a069 | -11.15634 | -49.73196 | 2024-09-30 12:34:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| caa4c0af-bf6d-3dd8-b95c-92f0ecbe8ba9 | -11.1107 | -49.58249 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 185907c2-5340-3840-9b41-5f2fdee8cd4b | -11.09959 | -49.5807 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 76272359-1ae0-3350-b3e6-ebce1cdc7963 | -13.6749 | -50.90393 | 2024-09-30 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 186.2 |
| b11be7ae-ed07-382f-867c-efb46be4572e | -13.67218 | -50.92057 | 2024-09-30 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 147.8 |
| b4cb9766-fce2-32fb-baeb-5fb8ccf84a81 | -13.57596 | -51.06015 | 2024-09-30 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2965ddf9-812c-3570-9ce9-bb38036e651d | -13.57306 | -51.07726 | 2024-09-30 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.2 |
| d016d8e1-ccc2-3777-9b7e-bc9c586b2b3e | -12.41623 | -50.97374 | 2024-09-30 12:34:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 869c054d-c671-342b-9de8-bff55798a048 | -12.28594 | -50.50358 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b7d48d62-bba3-3364-a56d-7243155710cf | -12.27427 | -50.50163 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e8526e22-ce3b-3352-a2ab-04a9d591cff2 | -12.22585 | -50.67479 | 2024-09-30 12:34:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 280a65e8-dbc6-3a0d-8efd-f9aa5b963799 | -13.69944 | -50.94828 | 2024-09-30 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 93a961cf-29dd-3d3c-8101-562464e15867 | -13.68157 | -50.91096 | 2024-09-30 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 251.3 |
| 9119bce7-0b32-3821-99b2-5919ab3b9b0a | -8.86973 | -51.02801 | 2024-09-30 12:34:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4a2e51e3-8817-30c7-8c22-b2295c688e1b | -10.50843 | -51.1325 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 271b2018-c72d-31b7-bc77-977c2eccc9a4 | -13.2165 | -51.22372 | 2024-09-30 12:34:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| a2faadb7-2fe8-3057-9ca0-c53885617d1f | -13.20436 | -51.22164 | 2024-09-30 12:34:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2d2b857d-e19d-3727-acc2-3d880989a307 | -17.71716 | -53.15839 | 2024-09-30 12:34:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 3621649b-56ca-30b0-8850-ea51961970b7 | -17.65456 | -53.14068 | 2024-09-30 12:34:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 5e4424b0-35ae-3529-a149-4cb6b17bd952 | -17.63783 | -53.15926 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 41.0 |
| f87414a0-3e06-3d5f-92fa-fa7095a03e6f | -11.06065 | -52.45959 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8c4c0554-6185-348e-9635-5fe7acf88de2 | -12.30169 | -54.11564 | 2024-09-30 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7912a0da-755f-39cc-aa7e-fa7dce675446 | -17.14272 | -56.20031 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 699e85f3-c02e-34e9-a849-faadad186a9f | -17.13246 | -56.20395 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 4dca5c04-c493-37b6-b445-a12bd30fc74f | -17.12645 | -56.19681 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| c47b2db9-db0c-334c-be27-a2def06551a8 | -17.02117 | -56.09243 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 146.0 |
| 9d190d20-1d3b-3d7e-92c1-79d6877bbc4b | -16.79592 | -55.95844 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.6 |
| ec3547fb-5659-3584-9b65-f0a145d95cd0 | -16.79322 | -55.84327 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 296.0 |
| 2e0145d6-e56c-3f5c-a732-ea1ad11553e1 | -16.78619 | -55.83446 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 439.3 |
| dd34f674-90b1-3712-ae87-99a51ed81a9e | -16.77969 | -55.8691 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.4 |
| 5a137bcf-32b6-3566-95fa-a2f8da172cdb | -16.77722 | -55.83995 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 601.6 |
| 4ba1646e-226f-315b-b650-3a549db74380 | -16.7702 | -55.83111 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 460.6 |
| 32215bcb-20e5-3224-b1ec-5547f575aae2 | -16.76366 | -55.86573 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 199.2 |
| f2781577-05c7-3ab3-b5cc-e7382245edfe | -16.76122 | -55.83662 | 2024-09-30 12:34:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 192.5 |
| c0c60f71-2943-3e07-9c8c-6dd8fff59fbf | -20.18013 | -43.51299 | 2024-09-30 12:36:00 | TERRA_M-T | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| ad020546-2503-3ed8-964d-b76ffcf526fa | -22.84978 | -43.70984 | 2024-09-30 12:36:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 00baabbf-d796-3de3-814a-e95e3013cfa3 | -22.84824 | -43.72285 | 2024-09-30 12:36:00 | TERRA_M-T | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c08adf0c-2fe9-3737-a1ae-d81e92851800 | -22.84118 | -43.71608 | 2024-09-30 12:36:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| e65a2629-580a-36b0-9cfb-6743c8d3f494 | -22.74387 | -43.76313 | 2024-09-30 12:36:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| fb1e758a-7116-38a3-994d-bd642d3f0335 | -22.44584 | -43.7835 | 2024-09-30 12:36:00 | TERRA_M-T | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| d37a8982-2a18-3874-b3a3-af1c964e05c5 | -20.34157 | -45.09185 | 2024-09-30 12:36:00 | TERRA_M-T | SÃO SEBASTIÃO DO OESTE | MINAS GERAIS | Brasil | 3164605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| ccee608d-7671-3743-aa33-db4e6737fd20 | -21.28399 | -45.24637 | 2024-09-30 12:36:00 | TERRA_M-T | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 24d45d70-5ee2-39d7-b43d-5d701a701410 | -21.71908 | -46.17858 | 2024-09-30 12:36:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e2968fdf-f1bc-31db-a265-098fd2525acc | -21.53064 | -45.87912 | 2024-09-30 12:36:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 0f861e88-9e7d-3acf-aff8-759cfbf68b20 | -21.37168 | -45.34967 | 2024-09-30 12:36:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 1ae2da05-4e34-3ed0-b4f4-20110ab7b9fe | -20.97159 | -46.3291 | 2024-09-30 12:36:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 964833a1-83c2-3efb-8e9e-330ced10f880 | -23.49587 | -47.22557 | 2024-09-30 12:36:00 | TERRA_M-T | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 40af1542-977a-31d4-890c-e9ca46ea4e86 | -23.19444 | -46.41597 | 2024-09-30 12:36:00 | TERRA_M-T | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 7b55d564-4215-3f22-8d0c-7c698486a1e1 | -25.90342 | -49.40118 | 2024-09-30 12:36:00 | TERRA_M-T | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 6a3f816e-d129-31f9-bdf1-8242be57021b | -20.5626 | -47.06987 | 2024-09-30 12:36:00 | TERRA_M-T | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 77d98da1-b4d2-3fff-898d-faa14f5b2067 | -20.31702 | -46.65891 | 2024-09-30 12:36:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| edc678ed-a0b1-3a88-8834-889443ffccc3 | -20.31569 | -46.66827 | 2024-09-30 12:36:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5c739e08-8181-35b0-9bac-08e2425d7435 | -20.27453 | -47.45922 | 2024-09-30 12:36:00 | TERRA_M-T | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 7505b179-f378-3ee7-bffa-f87a03d40ee0 | -20.27312 | -47.46872 | 2024-09-30 12:36:00 | TERRA_M-T | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dde02c86-fca9-3e61-84c7-fd8c802abbc8 | -20.26562 | -47.45778 | 2024-09-30 12:36:00 | TERRA_M-T | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 176e2879-edc8-3b47-9ba2-4ae09031942c | -20.26421 | -47.46726 | 2024-09-30 12:36:00 | TERRA_M-T | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1fd2ffe4-6377-37cb-9825-75ca2c487d36 | -20.17424 | -47.82433 | 2024-09-30 12:36:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f452555c-e2d5-32d6-ac9d-043a8f19f8b4 | -20.15704 | -47.81503 | 2024-09-30 12:36:00 | TERRA_M-T | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ce635896-32c2-3af0-abde-1ddb3d992a11 | -21.97104 | -48.01475 | 2024-09-30 12:36:00 | TERRA_M-T | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 91a73a71-95d6-31a8-8a05-fc9423288887 | -21.96961 | -48.0244 | 2024-09-30 12:36:00 | TERRA_M-T | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4f41975f-f6ab-3a32-82e8-de6cd42d453c | -21.96211 | -48.01323 | 2024-09-30 12:36:00 | TERRA_M-T | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7c59cfd9-89b0-3fd9-b058-aeae6174061a | -21.61552 | -47.8027 | 2024-09-30 12:36:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 3eb7c0e1-d530-33ee-92c8-68c6241ff240 | -21.6141 | -47.8123 | 2024-09-30 12:36:00 | TERRA_M-T | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 30dcdfb4-7130-30d5-8f9f-342c9aae3e31 | -21.10869 | -47.04375 | 2024-09-30 12:36:00 | TERRA_M-T | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 58fc7dba-d7d4-393b-94e1-1876dfd52113 | -21.0998 | -47.04233 | 2024-09-30 12:36:00 | TERRA_M-T | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 24338576-f381-31e2-ac07-0d99ac6b02c8 | -21.09844 | -47.05179 | 2024-09-30 12:36:00 | TERRA_M-T | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 987fb14f-77da-3e79-a4ce-2326182969a9 | -21.76081 | -48.49282 | 2024-09-30 12:36:00 | TERRA_M-T | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 51.0 |
| c4c8a5df-2659-3eeb-abf8-c8bae696b2a4 | -21.7593 | -48.50273 | 2024-09-30 12:36:00 | TERRA_M-T | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a3b8f816-6e10-3570-80e9-130fcf45dd36 | -23.61799 | -47.91058 | 2024-09-30 12:36:00 | TERRA_M-T | SARAPUÍ | SÃO PAULO | Brasil | 3551108 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 12685801-2c27-39d1-99ef-5150fd56c8ae | -24.00645 | -48.64758 | 2024-09-30 12:36:00 | TERRA_M-T | TAQUARIVAÍ | SÃO PAULO | Brasil | 3553856 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 519db3a7-c1b8-37bd-bf93-8fc7e422495d | -25.90188 | -49.41126 | 2024-09-30 12:36:00 | TERRA_M-T | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| bb5714dd-18ea-323b-91b0-c00ee99bcd52 | -20.29418 | -48.67479 | 2024-09-30 12:36:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 077bfca7-0b3d-3fa0-9ea9-afd2d116b606 | -20.29262 | -48.6849 | 2024-09-30 12:36:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 0fb72a86-64b6-3c05-bce7-e611da063755 | -20.28497 | -48.67326 | 2024-09-30 12:36:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 259.7 |
| b15889d4-4776-3fee-b2e6-bed0646d1e3a | -20.28341 | -48.68336 | 2024-09-30 12:36:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 451.8 |
| c46bf40f-4109-3ef6-99a7-7653e3809d34 | -20.28184 | -48.69356 | 2024-09-30 12:36:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 16ffa9e6-3a82-3aa0-b09e-699c3b93985f | -20.27578 | -48.67168 | 2024-09-30 12:36:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 87c56551-8fd6-3044-9e27-33d11ee9ec68 | -20.27421 | -48.68184 | 2024-09-30 12:36:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 1c459adf-9a3e-31cf-a1d2-979e36a879a1 | -19.66846 | -48.77098 | 2024-09-30 12:36:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5f1237d1-6483-39cc-851a-50447518d9a0 | -19.66685 | -48.78126 | 2024-09-30 12:36:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 4b7d0dad-598b-34f2-a5a9-b6f9a88f1c50 | -20.65002 | -48.76077 | 2024-09-30 12:36:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| a0c80375-5771-35b7-8603-aa3a282ff788 | -20.64238 | -48.74907 | 2024-09-30 12:36:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 5c2a6000-e000-345d-b4e1-d0f4adcf720d | -20.64082 | -48.75919 | 2024-09-30 12:36:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.1 |
| ff18e21b-9068-389f-99c9-fed77337d2a9 | -20.63318 | -48.74753 | 2024-09-30 12:36:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.0 |
| 89960861-89b1-3f09-bf8a-cc322b70d505 | -20.63161 | -48.75765 | 2024-09-30 12:36:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| 3e6214c0-a9f0-3c13-8e5f-5f83657c5e2a | -21.37324 | -48.49268 | 2024-09-30 12:36:00 | TERRA_M-T | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b83d6c2f-4308-381f-a37e-d19f9808bb18 | -21.37171 | -48.50262 | 2024-09-30 12:36:00 | TERRA_M-T | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 41e6a4c8-2652-3318-9129-56b4173be144 | -21.31654 | -49.22382 | 2024-09-30 12:36:00 | TERRA_M-T | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 281.1 |
| 8d1f0de7-5de0-3302-bcc6-5325ea7b0a75 | -21.31491 | -49.2343 | 2024-09-30 12:36:00 | TERRA_M-T | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.2 |
| a7506877-b750-3e07-8d03-c0b43fe93ca4 | -21.30887 | -49.21169 | 2024-09-30 12:36:00 | TERRA_M-T | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |


[Clique aqui para ver as próximas entradas](README76.md)
