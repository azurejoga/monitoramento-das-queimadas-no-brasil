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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa4e83fb-9b42-3b29-aacd-56853536711c | -5.88118 | -44.35344 | 2025-06-14 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a80ee89f-eafa-3e38-8348-21882eaa3c84 | -8.5637 | -47.04672 | 2025-06-14 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24fa602c-fe1b-37d3-9841-b2a1d99ab015 | -7.22349 | -43.58719 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d08215f-a8a8-3c7e-b019-b9ef1f98f6ac | -6.21091 | -43.33014 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb9261ee-3ff2-36fb-bb83-9f08d9f772cc | -6.60035 | -43.89426 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 519b46f6-2103-32be-b82e-439b46d047c2 | -7.45185 | -45.50875 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f763efb-8f47-3c5d-a8bb-e771a9721450 | -3.77139 | -41.60706 | 2025-06-14 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 334e15a6-7c14-3df7-af8f-a3cb4987af49 | -7.19258 | -43.54676 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b659a450-c6f6-3b55-ba8c-a78064aecc99 | -7.45999 | -45.50229 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2eba9200-cb82-3abb-92fe-cbfb7904b3be | -8.42859 | -49.55956 | 2025-06-14 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 003fb648-f1f5-3284-9c5d-bb74066405b6 | -5.88791 | -44.35454 | 2025-06-14 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20393fe3-58ba-30bb-99a9-f372627fca7b | -8.42789 | -49.56365 | 2025-06-14 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 70c14d9e-5896-30fb-b73d-fdabb5ae6a38 | -6.94873 | -42.89455 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| c44dc86a-3849-31ad-873a-0fac1ebe5481 | -7.1713 | -43.52941 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c10c0aa-96a6-3515-b3f7-12f147f8ef29 | -6.60811 | -43.88834 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 15eb52a1-d0a9-386d-97ab-7f8653701651 | -7.4553 | -45.5093 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f9cb6cd-02b9-377f-947a-e63c47bc0089 | -6.607 | -43.89533 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8a6288e5-06c9-3e6d-b119-5dc1f33bd70c | -7.67899 | -43.64972 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95124856-cd42-3ceb-844b-29cbebb9b628 | -7.23844 | -43.10373 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 883973ee-7278-3aa2-bbcb-aec7b7041c83 | -6.60423 | -43.8913 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3cc09aaa-104e-337d-83e6-9ce3e1c9b743 | -4.57447 | -37.82467 | 2025-06-14 04:12:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4aaf0c91-4609-3bad-8231-816fccd4a47b | -7.22467 | -43.10511 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| aa326309-1188-3427-a252-1afe1e47e844 | -10.86409 | -54.30281 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32fae528-6f04-3c58-a5b4-800624cd4f66 | -12.27821 | -57.27049 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6fbb20aa-6608-3976-888c-ba9bd182be31 | -8.56082 | -50.0777 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f984dcd-171d-39fc-aeb0-6202a7dd36e4 | -11.56597 | -54.57081 | 2025-06-14 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d6d9199-038d-333b-b353-739e33f536ce | -10.93666 | -56.84094 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d1f7abf8-a902-3789-9f50-68bb4c1d07cc | -10.84986 | -53.79007 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14f65d18-28b1-3d06-8ce4-ef961ab099b9 | -9.38614 | -57.52262 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 56d6d480-fec9-352f-ad8e-3f0ba713158f | -9.71249 | -48.61414 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d926dee1-b6b6-3a90-8528-f32de0c74e9f | -11.56758 | -54.57509 | 2025-06-14 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75ed429c-c409-3ce5-9cd9-ceac36244ea1 | -10.79482 | -49.58882 | 2025-06-14 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7365f7ce-9cd7-396a-b8d2-5ad85cd4cdac | -10.85198 | -53.77909 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b41501a-f7a8-3dfc-8524-28d347af6f70 | -9.46901 | -57.85008 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a53042ff-e16d-3047-9297-3ece4817804f | -14.02607 | -55.12455 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da270157-ed51-39f9-8d47-23cd198d9478 | -10.23688 | -52.23705 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94b2da90-afd0-3b88-a4bd-7e394679707a | -10.75277 | -54.77898 | 2025-06-14 04:14:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f637cb0-537b-3970-98aa-115f629fa297 | -9.39937 | -48.41779 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8058a2f5-66e8-3109-9b20-0515c9ed764a | -13.47448 | -47.14007 | 2025-06-14 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3b4fbb1-5f0c-3ac7-a320-8d9732b9680f | -12.15995 | -56.54794 | 2025-06-14 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 482fbba7-3b67-34ca-b40b-bd5f409822dd | -9.40552 | -48.42919 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3eba871-5b8d-335e-8bd0-da0fa548c8af | -9.85867 | -48.20037 | 2025-06-14 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3221f5fc-a510-3ea2-a69a-90685393a14d | -13.87956 | -44.45516 | 2025-06-14 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 929e11ae-bde4-3fff-bd83-2c51d4345aef | -9.84361 | -44.69349 | 2025-06-14 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d9bc25-e343-33c0-8f78-70503644bbf0 | -8.92531 | -49.85023 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ee168a7-e7e0-337c-960b-45285a972a6d | -14.21746 | -57.40717 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de16cffe-eb4c-3a1e-aeb2-15e4452846af | -13.89106 | -54.61024 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9d24bd40-0cf8-3f8f-aacb-d4e59aef7b3b | -9.15079 | -48.99771 | 2025-06-14 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afddec2d-fc08-3dd4-b70e-ceb8785b22a9 | -14.02843 | -55.12498 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a277300-931f-3470-afb1-f7d86bced43e | -9.56066 | -50.77697 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbfb27de-9529-3ea6-a751-43c93ccdef66 | -12.27284 | -57.27281 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf87faa1-7f26-365a-8db7-9d8df5b2cea4 | -13.58572 | -54.28482 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b8b0e0c-1ea5-3aaa-9255-3c584d061431 | -11.5742 | -47.43495 | 2025-06-14 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64d64741-b25f-3360-ac33-1760e8d0b133 | -11.40099 | -55.08452 | 2025-06-14 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0560d094-fb88-3412-9f8c-b499a2de6042 | -9.12275 | -46.93362 | 2025-06-14 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b406ae1c-8d0e-3761-b9db-229c6b83a24a | -9.46048 | -57.85572 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bf45e792-bd6c-36b0-9925-2ca0f20c2891 | -9.71501 | -48.61632 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a991f7fe-a3b0-3cf2-937b-eca7e10d3b0d | -15.39847 | -47.86581 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7adb9294-f8d9-3219-8a51-d6f9a808db94 | -12.13215 | -43.7087 | 2025-06-14 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06b1b1c5-f584-3cc2-ad40-e0d1f3e3a1f6 | -10.94311 | -56.84277 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3645fee9-5b5a-389c-9ed8-8b42b60f93f6 | -11.798 | -57.3564 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 113f9c52-1c78-3242-801c-bf2ef3fc5149 | -8.91667 | -49.84856 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcbf67c5-4767-32ef-8efd-286b1434579b | -14.03491 | -55.13832 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f61a53b-878a-38ad-88ca-060e7e2b0b74 | -11.89701 | -47.45625 | 2025-06-14 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73cd3308-2661-3f29-a780-b589bb94b242 | -10.6215 | -52.58791 | 2025-06-14 04:14:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0c0c507-b078-3135-93f8-133786304c6b | -10.92051 | -54.78207 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a79e96b1-a609-311f-b8f4-fc94368b8203 | -16.68005 | -43.8822 | 2025-06-14 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c19f58b7-55b3-36a8-a322-03c78552e8d9 | -11.13811 | -53.91853 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8b4ddba-b87b-3f98-8b33-58ed57e9307a | -8.8426 | -49.24312 | 2025-06-14 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f5c2eef-d348-3385-ac08-b8f1a774e6e7 | -16.19502 | -46.46604 | 2025-06-14 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b5cea107-ea7a-3181-8f2d-edfe9b0acfa1 | -11.80705 | -57.34623 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d2d830fb-08ac-36d2-ad96-20129a9729e4 | -9.38968 | -57.52986 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92c92bd0-d437-3f37-b233-80fe4a2b2360 | -13.89579 | -54.61489 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 23adf4e4-5c47-3564-9480-62ef3c323cf6 | -10.95806 | -49.56742 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8558ebf6-298f-3bdf-9c17-8435dea0fc5f | -12.61066 | -57.88496 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3b9aca6-eab6-39b3-bba9-305d43d14cc8 | -10.91464 | -56.84846 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a86adf7d-dffd-32df-baa3-7d1bce2a9047 | -9.39767 | -48.42786 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f856dd3d-0aeb-3ad5-96f7-7ea74777b0c0 | -12.61107 | -57.89053 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ec3c846-cfa0-31a0-bc28-f19fd5d3016a | -14.68655 | -53.3698 | 2025-06-14 04:14:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01e489cc-3f5a-338e-8e87-5ba97fac376e | -12.16102 | -56.54278 | 2025-06-14 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cf9a0af-142c-3374-9bbf-444d99f21d9b | -10.56134 | -52.01773 | 2025-06-14 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6176932-938e-3193-8770-0a2ed2ab804b | -10.36452 | -57.23289 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbc01c14-075a-34c4-863d-0c0098224d30 | -11.9322 | -47.84429 | 2025-06-14 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 260f4429-99fe-3776-ba27-82826aaaeac5 | -11.40687 | -55.08558 | 2025-06-14 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 953df445-8d80-30c5-8fa5-722a5878504b | -9.3827 | -57.52837 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 770999a1-4192-31d0-b171-37d498f5f070 | -9.71105 | -48.61568 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c851d7a2-b5da-3caf-bb39-2fd36e4db217 | -9.39107 | -57.52295 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa9a26b1-bd66-384a-9301-baa25b4038c3 | -11.00623 | -55.08414 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 50ad2b8d-0c6e-3589-a530-e6d595214628 | -9.40804 | -48.41418 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 42f66cbe-ea7f-3d9d-9b9a-e6d929b66004 | -10.65211 | -44.48192 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6aab2da3-1b90-3b18-b668-3c9fcb50cc39 | -10.84182 | -53.77325 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f9e8c12-9749-3060-9f18-a00aaf0a4c3b | -9.40968 | -48.42717 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 770680fe-b137-3c3d-bab0-d3815869493e | -15.38461 | -47.86016 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c38334ed-2d7b-3bfe-a194-ca83189c817f | -11.02442 | -45.23639 | 2025-06-14 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03368108-3df1-354f-96be-35f894c3c852 | -13.89174 | -54.60677 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 999a9c0b-801a-365a-bf84-0bad93dc15e5 | -10.85056 | -53.78644 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a66fcb2f-05ad-39ca-833d-cc06a2f757a5 | -15.3942 | -47.8906 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b59f4c63-7d4b-3a7c-9e13-f0328e7d27b2 | -10.40945 | -46.68309 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72a3540c-a93e-30e6-ab6c-5c379391817f | -14.20586 | -57.3989 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb6d1a65-279d-3394-afc5-94a015ae9d21 | -11.13311 | -53.94415 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
