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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 204fc10d-803b-34d8-9975-2446fb29a25d | -11.1586 | -57.18116 | 2025-09-11 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f8c359-d429-3805-a3b7-db14eb4710b5 | -14.52001 | -53.92815 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a561f6b-1f70-3a42-99cb-fdb0fd3884ea | -12.38959 | -54.17132 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea56a1e-d0ca-3650-9fff-a562ef74816b | -15.09881 | -50.06486 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 450d8322-a0b1-32b0-b63f-5dc3aa03b861 | -12.84284 | -47.9694 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55d72fa0-4df3-346d-b523-66fa9e01bb94 | -14.93756 | -50.10396 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| de6cf673-9273-3cd4-8194-7aa6ec663cc9 | -12.46942 | -53.83163 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eefbd62-9e4a-37ac-a889-62834cb90141 | -13.15119 | -45.28501 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5e83743-f409-3e9c-b2db-590ccc777640 | -11.10923 | -51.94734 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc998c4-89f2-3185-9a78-3cb6005acdce | -11.48644 | -43.64341 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f9c429a-d70b-32a0-9c5f-14d7b9cb8112 | -9.79618 | -51.09377 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6855719-2073-3e9b-a3d5-d4dbb08fe680 | -12.10337 | -51.02625 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 911ceb13-f9e7-3951-abd4-280db7b38186 | -11.46126 | -43.59734 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61a75683-2d8f-3d2a-872e-fc6d82ca82d5 | -11.47858 | -43.62412 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 487f451d-dbcc-35ea-97dc-bb1116afc4fe | -16.06579 | -48.13273 | 2025-09-11 04:46:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c6f5495-11b9-3362-970a-d47c645b094e | -14.29966 | -45.02088 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e077e3a-a7fd-3684-aa15-1ff09aa0219d | -15.14387 | -48.60679 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f36346e-eaf2-3cbe-9076-b9a6e43368cb | -12.56591 | -44.6436 | 2025-09-11 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b4fcae44-dabd-368e-b18e-1c33fbde12f3 | -15.38774 | -52.91516 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d449fd9c-4952-3d38-8b88-c3a12f762db2 | -9.49252 | -48.30519 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abe12e81-9c06-3416-8708-df93859f8c04 | -11.18437 | -48.36492 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7aa65eab-7d29-3b3c-aae7-4fa9e00478a8 | -10.01505 | -51.71412 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13189906-d4da-30ea-b55e-a1862255fc2d | -15.79476 | -52.26296 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1d2b5fd-9f79-3a2d-9e8c-fb95e78ec03a | -10.54485 | -51.51908 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48bb8563-09e5-344c-8492-c9af869847a6 | -15.08339 | -50.07063 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 747084d4-4fd4-3bd3-aaee-6159f92bc34d | -8.92361 | -51.05376 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21fe6b1a-3490-35ec-95e7-4776f7a9d883 | -11.15064 | -52.05105 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04b47b68-0356-3a32-a855-f51bbb7843ce | -9.91071 | -49.90783 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2bcdea5-be21-358c-a288-b9b7e6f34147 | -8.57136 | -51.35138 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4110ab3f-7298-3883-9332-55f5e8442fc2 | -9.03588 | -49.76954 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 494f5b17-e469-3872-b080-b5da97a9e48f | -11.45182 | -43.58985 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fb826c4-78e9-3bb1-ac06-e752ebedfaae | -14.12272 | -44.31954 | 2025-09-11 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d0ea830-6503-37f8-a7fa-4d5518476e22 | -15.08638 | -50.07517 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34a05303-c83e-31a7-b868-ad37f24e3677 | -12.05501 | -50.94778 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3c8dff3-4a5b-3cc8-a0a2-b46880cadc7b | -12.37136 | -54.17583 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec7b42e9-ec95-3d8b-b723-03fef5d72e94 | -11.22866 | -55.00356 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 778f0530-a3d6-38cc-ad28-7c9482257f6e | -14.90026 | -55.87912 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f0a4381-04bd-3e9c-b949-35c278acdc05 | -12.94016 | -54.81054 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb31ebf9-15be-3ec8-a52e-d62a8ca850f9 | -9.68029 | -47.52657 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01340144-10fa-35c8-a10b-fe646ba9409e | -11.14788 | -52.02545 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e023f36e-8cf2-3604-829b-42ac80138f4b | -11.49438 | -43.64507 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 999380c7-4ae5-3993-9cc0-0558560678c4 | -12.5577 | -46.93436 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b905dc51-950a-38aa-9a92-6032480be7d0 | -15.56468 | -54.75168 | 2025-09-11 04:46:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecd8962f-7a9f-371c-8072-795947a85e15 | -11.64231 | -52.249 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9a8c65c-9a6a-3357-90c7-3e175fbfd539 | -9.8388 | -47.78536 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 195819c1-886b-3a0e-88f8-7e3bc8b930f3 | -10.06596 | -50.38143 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1df4ec1-d2d8-3789-86cf-61074a0da964 | -14.9194 | -55.83145 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9e7f0fe-dad9-3c4c-ac72-ac89140c602b | -9.29578 | -48.42286 | 2025-09-11 04:46:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5de77afe-6f8a-38cf-9bcb-aab64e244eab | -11.45497 | -43.60577 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a2c31d9c-5130-34d9-8d39-5b2181673c12 | -15.11786 | -52.4053 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27e13069-57c0-3800-adab-45218f3cee17 | -12.84327 | -52.94353 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 984e649a-b71d-3e28-949d-2f7f74c0630f | -11.79597 | -50.58113 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 02e13d48-a055-3d27-9a45-d70d6da694a1 | -11.13519 | -52.04137 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b331bf1-4dbf-3a65-bf4b-25749271e854 | -12.84653 | -52.96585 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db6b41d1-6cd4-3fff-b8e9-8d61681d3800 | -12.94293 | -54.75116 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed662ce6-827c-385c-9fc0-83b380edbf5e | -11.48777 | -43.65657 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 625aaf61-7c11-36ed-9293-46c595f5face | -15.48176 | -49.36045 | 2025-09-11 04:46:00 | NOAA-20 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73278dca-c17b-3c9c-a0af-280924f0ac73 | -9.30862 | -46.75756 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe107116-b22d-37a5-8611-a26bc953c0eb | -13.58293 | -47.70368 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c6d153a7-f506-3668-b54e-04872bf524ff | -8.07813 | -54.75243 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4033a200-e7ad-390c-b18e-08352bf45f7a | -9.07811 | -50.47358 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a31002fb-b609-32c8-a627-871fc606b60c | -13.667 | -44.22449 | 2025-09-11 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84b54b35-1449-3021-b3df-4f97b4b285b5 | -9.52978 | -48.30632 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 311644da-2838-3282-9e05-2e5a6bf2f632 | -15.16063 | -52.43467 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b068cd58-afc4-3741-b05e-ae95449bb2cf | -12.00124 | -47.58805 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f45389b-58fb-3a12-980c-03ed9db7cbda | -15.28682 | -53.78637 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f80ffbb-3276-3b4a-a941-f2dc8580117c | -10.56916 | -51.49411 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58233173-dd73-36b7-8190-f3fbcd80c34c | -12.01452 | -47.57952 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18129f4b-3dbc-3baa-9714-0738c33d319c | -11.14899 | -52.06157 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 248955d0-f9d3-3974-9e89-a658cd766ae6 | -12.05387 | -50.93266 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6c5b914-02f1-3904-a74f-5886d26d63ef | -9.83812 | -47.78997 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f50b40b2-5b78-3549-9dd4-af856f4be6fa | -16.05914 | -49.97545 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c6a9b2b-1b48-3c28-80d5-aa2caab263f8 | -12.84832 | -47.96249 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d312ba8-10f6-38e4-9781-da8d20bd2988 | -10.53956 | -49.88936 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6490db75-4acc-3532-89ec-f092bca97759 | -9.98029 | -51.69782 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1403fb8-727e-30dc-b976-c4667937655d | -10.89175 | -47.25724 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58c79564-44ac-3d76-a051-6f3395769a0b | -9.06137 | -50.49304 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57ce3efb-0e2c-3476-868a-9f6911f7be06 | -11.35525 | -46.50521 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e6dbf992-bb8e-3413-bf49-06abadf54e75 | -12.86261 | -52.95037 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be421269-bee7-324a-b64b-5517af8c018b | -11.32847 | -50.75431 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1be1d58e-fd91-3d0c-98ca-1d720bb4f314 | -11.48129 | -43.68262 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8359fd3c-c93d-3c06-83e4-d7c9e682238e | -8.86586 | -49.57556 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 850ad3f3-3388-3e58-9a7d-ab23f1251542 | -11.48836 | -43.66827 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d2802a6-61ca-33f0-85c3-d3ee2e7e0551 | -13.1869 | -51.7687 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41531c6c-beec-302e-b7e5-7f56a33aa4a2 | -15.12432 | -50.13992 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c010dc3e-3d42-36cf-aec2-356df81213c8 | -14.31222 | -54.74901 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af472ca7-9b65-399f-afe2-a0a6df8d50da | -14.31806 | -53.06695 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5432bf87-738d-32eb-ba3c-8d99a30172cc | -16.42921 | -45.69273 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76e0f73f-b6f5-381f-b923-6977c872a5c7 | -9.38675 | -46.76532 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa17752d-5b41-3729-8719-ce80b9c867ee | -11.26454 | -51.12493 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9913828-b193-3fbc-87ae-7abd1b0ef89d | -11.40717 | -43.55078 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b3e8d15-8af5-3c46-a303-4635f441ee18 | -9.59605 | -50.92192 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb36b7f5-4863-3afa-ba1b-3e3a8873c686 | -11.09323 | -48.43111 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 831e1fc6-39b0-3fa1-a7b0-4ab9bf7a5af6 | -12.03618 | -47.54071 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25b0b903-a27f-38a2-992e-0f1e2bd530d7 | -10.01065 | -51.72056 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e14a25cc-14ab-3d86-97c7-b6f4bdfbff26 | -15.11903 | -50.12638 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b49514d2-3d5c-377f-b542-9d8ea6a58227 | -14.88378 | -55.85204 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95c26b80-8dcb-3e16-b1fa-dd025d1854e6 | -11.73376 | -50.6245 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0cde0858-e28d-3d6c-931b-c564a0eee3fb | -11.16132 | -45.30703 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| df0bec0f-055d-3383-8ca1-01181ded8b2e | -11.02522 | -45.06304 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |


[Clique aqui para ver as próximas entradas](README108.md)
