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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d1221a6-9c98-3bf6-aa33-97f9b24987a3 | -8.87903 | -46.19407 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15c2d9ae-b368-34d1-858f-2c6281c45d62 | -12.15482 | -50.40617 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc11b32c-bde3-36e6-9a25-70ad87a7d4ff | -9.78996 | -48.2002 | 2026-09-29 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47f22108-bffd-3c45-9bc8-dfdb6ac57b03 | -11.30658 | -43.54595 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b31c4cb0-2b0a-3ef5-a3ba-f9d93d814559 | -12.03766 | -46.50332 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68a55fdb-f7fe-32a5-bc2e-13420656fa22 | -13.57543 | -46.36209 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78800142-ebf7-3dbb-9fe9-02b4baec06d4 | -10.26643 | -44.63557 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b38f709-3093-3e51-a6f1-c66ba9fec39f | -10.41428 | -53.77977 | 2026-09-29 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ffc2f92-8151-3297-bec8-adbc0b9a43f3 | -12.7242 | -46.99189 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f43e3474-586f-34e3-8418-810b29837bbd | -16.35223 | -42.5789 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 818f171a-9ec7-34e5-944a-03e6faea1e24 | -9.77042 | -44.82467 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9125327d-938e-3893-ba3e-7ff68d943df7 | -21.06914 | -48.83871 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1ac164b9-5518-39b0-9196-c7a5b2a18216 | -11.99586 | -50.95376 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 450e595a-55bd-35c3-b697-a752ceb24356 | -10.42873 | -49.37543 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fc08274-1fe4-3d58-a54a-e29a93a42a70 | -15.13274 | -43.6194 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8848b7ab-1205-373e-b31a-678c821b4630 | -12.60886 | -47.27921 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94e18cd2-5d5c-31a5-a509-3847d92e8d0f | -12.69503 | -47.25718 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 2544b80a-59a2-3af2-8b78-8b2ef43b20ba | -11.38573 | -54.04484 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3222e088-bdbb-30ea-a775-be59aedc1b5c | -11.44307 | -43.45479 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87557787-762b-3a35-88e9-4abb6e8b9526 | -11.40752 | -43.44191 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b11e470-4ad7-3459-a643-40f3270ba95c | -15.22542 | -46.17746 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd4095c1-d300-35f7-8a61-8acb5b9cd803 | -10.81707 | -48.74125 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6d571d1-de42-386d-b741-4caa3a205bfe | -12.61302 | -47.27584 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 880b0e21-fda5-37f6-b7bb-0c684dc3087a | -10.81624 | -48.74601 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de91326c-d884-39d0-86dd-e7659db4012a | -11.13896 | -50.07309 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 415bdb24-e8d4-3da0-8f06-315c0cec693b | -13.10982 | -47.40681 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa4b7194-ccab-3976-8767-0bb420f910c9 | -11.37851 | -54.04354 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dceb873-317a-343b-830d-1a1985427119 | -9.7621 | -44.83418 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41a201db-a689-3f84-acaf-0e52feb8462b | -12.93557 | -46.66731 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67d4a424-8085-3485-aea9-adba8660f378 | -8.66195 | -48.88894 | 2026-09-29 04:17:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74c53357-0da4-328b-b157-4d77bbc2f9b4 | -13.3738 | -44.0074 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43c21411-dfb6-3573-9c61-f38b28f867c0 | -12.74221 | -47.28432 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aae18ae9-f001-3db8-b6c4-f48bb496ff63 | -11.178 | -44.79062 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdab35f7-dfae-3290-a24e-08b980c6008e | -13.33268 | -46.81849 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52c63a4d-c715-36d9-a715-8d9157b2e004 | -11.44645 | -43.47722 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccdbeb87-92f9-3c8a-9fc4-ebee0510f0cd | -13.1692 | -48.56103 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8617f58-0692-39ae-ba5d-ed3a3827af24 | -20.79289 | -45.35249 | 2026-09-29 04:17:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5c57f5c9-a4b4-35d6-b019-48801e7f5697 | -21.05621 | -48.87313 | 2026-09-29 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 80416f36-4e96-31a2-8a96-8436d3c7b8f4 | -12.17455 | -45.05042 | 2026-09-29 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc7e3449-4458-3426-a81a-57fcf41176db | -11.50951 | -47.39816 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 982bbac1-4820-3034-8b9a-14a745148a02 | -11.38296 | -43.4015 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1493e02d-4658-34ec-ad19-ec61b7b950bf | -15.15417 | -43.61516 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f518443a-a130-3266-9f77-36f2c5313420 | -10.21482 | -46.70774 | 2026-09-29 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c880a176-fd20-3c41-8eeb-7634dcf4216c | -11.86644 | -50.46201 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bd560e40-9ba2-3949-bdc2-e16f55f9ddcf | -14.08229 | -46.3194 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6a1331e-7ae2-3d55-bdae-b8b8ad860644 | -12.02687 | -50.98162 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70b4f7b4-7c4b-3506-9632-88dbbb543a7c | -12.05738 | -46.46795 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75effcc1-a894-3f23-b98b-53e15adbbe26 | -10.19887 | -49.99462 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e89701f-8ee1-37c0-acc9-f55235c20d09 | -14.52076 | -52.48018 | 2026-09-29 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b693c7ee-cb24-3f51-9edc-c64dbdf4b8c7 | -12.14153 | -45.00179 | 2026-09-29 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92e29629-555d-3cff-b08c-fc315cb40222 | -11.36828 | -47.44309 | 2026-09-29 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32d308cf-3242-3d8c-ad3c-219d87ce0358 | -13.33672 | -46.81526 | 2026-09-29 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90e27637-9cf9-3c62-89df-f636b9477ce2 | -11.17745 | -44.79412 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0dcdf50-4a1b-3cad-9770-413dbb2d5e77 | -10.20026 | -49.98672 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e7674267-a1e7-37d3-b12b-970bfa4e27d9 | -14.77432 | -47.15882 | 2026-09-29 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f07d30-ce06-32d1-9694-cabf6ebb4120 | -11.19145 | -45.13528 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3795aed1-92e2-380c-86c9-99bbf73ba01a | -11.44033 | -43.47261 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83186d09-617d-35cd-b2d0-51bacd5b22da | -11.83572 | -45.02029 | 2026-09-29 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee3fa80f-c8d8-37cb-a1f0-f0daf4620995 | -20.55309 | -45.86383 | 2026-09-29 04:17:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39c06c6b-2edf-3548-be25-d59dcce6b90e | -14.96098 | -47.53772 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2877d04f-c525-30c5-94c3-a1ebd766140a | -11.44699 | -43.47366 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 401f3591-4795-31e0-b548-b0b76b0e6a10 | -11.41866 | -43.45827 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| de6cb048-1f4e-3408-95ad-8cd0686aec21 | -9.96126 | -50.13256 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e2a32425-c26a-3708-8802-707546f4bae6 | -14.63297 | -52.13587 | 2026-09-29 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 212fdece-d1a9-3d37-84b8-9bd0c6d0257e | -11.8248 | -46.90049 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e6d50fd-e092-3e79-ac82-2c4ff8a495f4 | -9.80303 | -44.83347 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e219e8a3-ecb1-3e1a-983c-f2f5d165939a | -11.36026 | -54.05123 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 456d487e-75db-33dd-ab95-a6bbd485f994 | -14.11067 | -43.62943 | 2026-09-29 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a0b47b7-9a1b-3856-9cf9-3fd24df27243 | -21.05689 | -48.86913 | 2026-09-29 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| fce07ca3-da04-3075-b7db-c7b13b1c140f | -12.0071 | -50.99134 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 663b953d-923d-36eb-b099-7f559f9a836d | -12.00633 | -50.99566 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| bb6f2c26-c0b8-339f-a852-f8a014537532 | -13.14503 | -48.54705 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7fc81bd-f2a0-38e9-9581-a3124106625e | -10.28619 | -49.96965 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c58ed50f-e1a5-3ee6-af24-ab7bf268ff53 | -9.76986 | -44.82819 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df8d785e-70d3-346b-a712-2c7e7657a16e | -15.81471 | -42.57134 | 2026-09-29 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9e6ba50d-0ec7-3705-bae4-ae08f821ad39 | -11.1333 | -50.07298 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34e867cd-e774-3f64-afa2-dc17589b97f1 | -15.17103 | -46.13514 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fae7c3aa-f445-34b1-bbb7-c86725c1e55b | -11.65532 | -47.59569 | 2026-09-29 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcddc901-f292-3ed5-81fa-0f404041981a | -14.11493 | -46.28754 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3380526-c7e6-390e-bd09-a0396640d15e | -12.60404 | -47.28655 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 543bcf80-c910-3255-8afb-b3bd9d6d2c38 | -12.68805 | -47.25601 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d15450b3-4a8a-34f5-9107-a157d3114220 | -11.39256 | -43.45052 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f08a7fa-9a00-3bdf-9ae2-543bc00770cb | -11.12764 | -50.05597 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fbbb3a9-9aa3-3fb2-825a-938727d23c7b | -11.18075 | -44.79465 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29d0fc2b-5a26-35fc-87f8-e73f59ebc9a7 | -10.28129 | -44.62724 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc7f1363-94f0-35dd-bf01-79cccb738711 | -11.35327 | -43.3527 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cecd1aa4-2b7b-3d13-926b-4079b2ecae67 | -12.66609 | -46.97884 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7238d92a-826d-3592-92c8-a5f1b46354b9 | -11.62697 | -46.79978 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 121e7d13-eccb-3a9a-8e1d-6ccfefebad5c | -15.22153 | -46.18045 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00913270-a406-391a-a83a-b4f464e41b7d | -21.99492 | -48.17957 | 2026-09-29 04:17:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcfb48c0-f07e-3164-87e7-1706b96eedae | -12.87919 | -44.80876 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5f37de7-549c-37ff-a593-36c343f91cdd | -11.437 | -43.4721 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b9154fc-126b-3ade-821e-2f2ef2eaff27 | -9.82383 | -44.93851 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ca2fa95-7e30-3f37-a6de-dc7654203bc7 | -11.96494 | -50.92602 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0d1dabf-5245-3fd4-af72-8d991fa08e51 | -11.43422 | -43.46801 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fa049e38-2693-3335-b955-adec6a68b914 | -11.43362 | -43.44965 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a8c151a-aa56-387c-b5e9-435f667af4cf | -11.16529 | -50.04589 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40712d12-b303-3d52-b374-39da2070f82e | -12.00865 | -50.98272 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff3d81b7-fee1-345e-a7f1-8e85cee5058e | -11.30326 | -43.54543 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd5006a2-7e8e-3fd3-861a-ab3194798d88 | -11.50884 | -47.40218 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
