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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61f296a7-3709-3755-8893-b5d31492b205 | -19.73825 | -45.31971 | 2025-08-22 04:21:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0ca701d-b7ed-3621-b244-d1731bec7bf3 | -18.28875 | -45.53881 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbc37f68-d5cb-3bb7-bd89-8e3f5bc2ac8a | -13.01626 | -45.1756 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c53760a4-c043-3917-836d-368645d94cb3 | -15.03226 | -54.83753 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0834cf54-4763-3ce4-b4b7-81157792f568 | -13.63975 | -46.87876 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4893de7c-e220-3919-9012-59335d2006b8 | -12.98146 | -56.89142 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6c0dbbf-9fac-3c38-83d8-919f88731322 | -14.78568 | -59.65818 | 2025-08-22 04:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e604a043-c8cc-3f00-8692-6710ddfbf512 | -13.02409 | -45.19163 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f61239c-ec29-3ab3-84a0-1bfef45edc92 | -12.98874 | -56.88865 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84922095-284d-3a0e-b2d5-45dac8d44dce | -20.23693 | -46.61574 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f7051e38-45bf-35c2-9b46-ff1748a540e8 | -15.58353 | -43.80266 | 2025-08-22 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29eb7a6c-4450-3c73-ac3c-6a38063b8255 | -13.02742 | -46.3285 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33cc7c0f-fd2e-3fa2-8149-9334233e99d2 | -15.41339 | -41.64923 | 2025-08-22 04:21:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b744b177-8c6e-39f4-ac06-85ef91b45d1c | -14.83388 | -47.92803 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fa34f16-22d8-3ca7-99c8-1f118348a6b3 | -17.60386 | -46.09613 | 2025-08-22 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8da388ac-7256-3340-b9f2-f4fd3e2d527a | -20.43203 | -46.50659 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a7c99e0-f4d6-3f51-8952-e174ee94b096 | -12.95631 | -46.28431 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| adadacc5-507b-3783-b6c5-edec01a4e221 | -17.39926 | -44.24705 | 2025-08-22 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01f27f1f-12c3-3d16-8a74-a4f195992e2c | -13.64418 | -45.70563 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5cd4ec4-258e-3ef5-aa38-9d050eeb3af3 | -14.89838 | -48.05248 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfe90421-7c70-3cf5-9978-8c16af719361 | -13.6475 | -45.70617 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33d0f88b-52ee-3ea9-beb3-371ae06483b9 | -13.79975 | -52.86755 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44b22e13-8830-3b07-bd5a-3538343ada34 | -18.79345 | -41.45958 | 2025-08-22 04:21:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 10d52665-0c1b-3600-ae6f-0f0887810213 | -16.48388 | -45.09644 | 2025-08-22 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d669a28-552e-33d3-bc6a-1fd219821b0f | -19.97162 | -44.92361 | 2025-08-22 04:21:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9788c70f-9602-3014-b36b-b7274f57bf18 | -14.87888 | -47.93952 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47185751-f2d3-39d4-bfc8-132d3c82a195 | -15.65669 | -52.68858 | 2025-08-22 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63984507-5508-37f1-8d09-b086cd5db125 | -12.94638 | -46.28268 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ebf01a8-b687-391f-9acc-c8c96b8bebf6 | -14.60797 | -54.83922 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51aa2664-2ac1-3e7d-b52f-8986a9494b18 | -13.02356 | -46.33147 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 650bdc72-b0d9-3e1d-bd74-897df35c304d | -14.47978 | -48.35966 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27fdc91a-e267-3329-951f-92118e75d15a | -13.38024 | -46.22308 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac94fc15-9baa-3013-af51-56782a389afe | -20.35717 | -46.51446 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6144919-4b8f-330d-b5d4-66b4d0208732 | -14.76555 | -45.42831 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2810e261-a7c9-31be-a283-c9e730746cb8 | -13.38324 | -47.50535 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c783fe7-0976-37d7-9f92-049039ee51c0 | -12.98307 | -56.88325 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe83d507-6783-3d34-845c-1af6e2df3355 | -18.28988 | -45.50699 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4694f41-bcd7-3108-8a81-9ad0f000fd43 | -18.66474 | -46.98622 | 2025-08-22 04:21:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a3f73f2-6ff1-3006-9ed5-e6054eed9049 | -20.36505 | -46.50803 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f2c4a22-ec4f-332a-94cb-b390b2ac2168 | -12.98787 | -45.23414 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f18fd3fd-3c98-30a2-8120-e1376f6826f9 | -16.55817 | -49.2665 | 2025-08-22 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab8367ee-96f5-3389-9c43-e0c4aecee204 | -16.50733 | -46.73986 | 2025-08-22 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 498e9064-58ec-3cb6-a958-29131ce6730b | -13.46301 | -47.0508 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f36bbd96-2183-31c1-93d5-635ee6e7df12 | -18.27562 | -45.55666 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b422d1cb-2501-3775-be6d-20520fc207bd | -15.73307 | -43.24189 | 2025-08-22 04:21:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f22a967-2118-3b5d-872d-73c8d68c04ea | -13.023 | -46.335 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3857c908-4bd3-3a12-a957-845018f68135 | -13.4197 | -43.67812 | 2025-08-22 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e21d0bb3-3378-3185-bcea-f834cbd9133c | -18.73429 | -46.90795 | 2025-08-22 04:21:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66a183fe-0ae3-3218-b7e9-f5d5a3e3f59d | -12.9453 | -46.181 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76edf6de-ef2c-3469-9106-1ee93b6a6d40 | -14.47577 | -48.36278 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d3e110-a49a-34a2-9a89-5d35e86ff845 | -14.6453 | -54.91867 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0773f62f-76c6-31b1-994a-3284d8905bf2 | -16.78525 | -47.66747 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7f685ef-68d3-3e33-90bb-5adcd618dde5 | -12.49161 | -53.80957 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cef4406-2201-3fa3-b2a0-22322cd10959 | -18.33275 | -49.44637 | 2025-08-22 04:21:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b8e8010-ab6a-3812-9744-7dff84710c6a | -18.31391 | -48.86391 | 2025-08-22 04:21:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8fb6ac30-b869-331d-ab80-44d250f3c4d2 | -19.09848 | -46.6764 | 2025-08-22 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2be3c35c-8c36-37e0-8323-9774fdf1b24e | -15.08 | -47.09355 | 2025-08-22 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 348b5757-2402-3605-a453-082d395c0cd3 | -17.8851 | -45.92949 | 2025-08-22 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3016d0ed-68f7-3c4d-b75d-f3c472ae19a9 | -20.67542 | -41.42043 | 2025-08-22 04:21:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02f79676-8557-3eb5-989b-c8d3bfa7cac2 | -13.02574 | -45.18081 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64e93f78-e415-31bd-a290-04196fb7092a | -12.95963 | -46.28485 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a905f052-da2a-3ce7-8491-93f4ec800b76 | -15.65958 | -52.70062 | 2025-08-22 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24ff1d41-8d83-3757-9e26-94a5080aae5c | -20.27221 | -46.57434 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 688dcaf7-8302-3098-8c33-378c6b32d28c | -14.34165 | -53.12191 | 2025-08-22 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 729ae99e-3682-35ed-b703-5ccc26ce703b | -13.45855 | -47.05738 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b960f0e2-b9e1-3ffd-af65-49e90c2aaacd | -15.55392 | -51.70272 | 2025-08-22 04:21:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cc61b98-cabb-3203-80e3-8f9a582d17ee | -13.0263 | -45.1772 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c3e2a09-9924-3065-9df1-6ac42b3376ca | -11.31769 | -55.22767 | 2025-08-22 04:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a3284fb-1eb6-3025-bcf8-e662859a4dfa | -13.01905 | -45.17974 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cb21b3a-fc33-328c-9200-11d3e5ed599c | -14.76665 | -45.39848 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 277291e6-7d6f-317c-9ad2-e79521aaaf1e | -19.67492 | -48.98909 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| da53ef00-bcf3-3a55-ace3-8f3f851fecf0 | -12.99738 | -45.20955 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 824f39eb-8263-3cbd-a2b2-571d26d9795b | -13.435 | -57.1767 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0a08b49-fa50-36a3-9338-c42613f0a8cb | -14.8966 | -48.06337 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e13eb1d-2660-3743-8b99-1469c1500eb3 | -15.50419 | -48.48793 | 2025-08-22 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5421d7c9-c474-3071-9b45-fcfa079fb8cf | -16.154 | -44.15753 | 2025-08-22 04:21:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bfe1cad-2274-3737-8dbb-ea1b1be2e6da | -13.32278 | -54.40181 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2253199-4c8b-34a4-8d9f-d757efaf0f4c | -20.33802 | -46.55009 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb81f0b2-ed07-3698-8335-73adfd0f91a0 | -12.95745 | -46.25554 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36f785b6-5289-350b-9868-2474f56f318a | -14.88103 | -47.94745 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39757634-d87f-3d00-af10-071dea8b514d | -11.89497 | -55.89715 | 2025-08-22 04:21:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b55918e-7355-3c9e-bb68-24ad14f5092a | -11.90102 | -55.8962 | 2025-08-22 04:21:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12708472-5583-3483-b1f6-3cb250e47fc9 | -13.02912 | -45.20353 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca7a805d-65e6-380d-bc17-fa4258d0af07 | -15.55671 | -50.32767 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab97b1b5-366d-31de-ac99-53eca1643ce7 | -20.40747 | -40.84356 | 2025-08-22 04:21:00 | NOAA-20 | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9760cbfc-ce09-3c04-b417-64b483a1c341 | -14.75379 | -45.41517 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc3c58ba-b458-3915-80e4-dbcf6c68ee3a | -13.37437 | -47.4964 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0eb8b549-1af2-36fd-b953-950fd336d054 | -14.62603 | -54.80861 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e4225c9-5902-3e17-a54c-f70647062825 | -15.4129 | -41.65284 | 2025-08-22 04:21:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4586725b-e91c-31c2-9f50-f3cd29d8dacb | -18.73975 | -48.31847 | 2025-08-22 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0c8700d-c631-3f3c-93b5-7b6cdc51a907 | -17.60975 | -46.69918 | 2025-08-22 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71736d7b-e94a-36dd-891d-2d7a1e44b367 | -13.02909 | -45.18134 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c187f62-2e96-31e9-afa2-0a01d140a95b | -14.76385 | -45.39427 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c9e7dc8-eec2-3aca-ba03-ef70bed616b5 | -15.734 | -49.4464 | 2025-08-22 04:21:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 177c97e3-acf9-3bfd-a942-8c54b39b981f | -14.99259 | -54.86054 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4abeef16-1312-3ed6-b3c1-f41fa370fe0c | -12.98619 | -45.22282 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 011e92fe-053b-3bf6-99ca-a07350b59c0e | -17.91978 | -44.49152 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 443809af-0597-3064-af35-868b6ec36998 | -20.2375 | -46.61198 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ea510104-f62d-3ce9-aae0-12c6b70cbdd8 | -20.32744 | -44.24221 | 2025-08-22 04:21:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 90ccf416-c5a6-3c20-98d2-4868df797b70 | -20.27212 | -46.69111 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README35.md)
