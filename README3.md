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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b58290b-cd5c-3daa-8e32-94b7f26c8b39 | -4.57493 | -47.23529 | 2026-06-29 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85b7e69a-e6fa-3236-834e-4bf5b168d55b | -5.62383 | -47.09875 | 2026-06-29 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0214b10-8d89-33d8-85bb-495327d5ebc0 | -5.62325 | -47.10252 | 2026-06-29 04:38:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b1e8abd-f9d9-31e2-b73c-dbd06f7ebef2 | -4.76946 | -46.39163 | 2026-06-29 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5216db40-7bca-39d1-b153-ece35baf5dfd | -4.8457 | -42.92569 | 2026-06-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d6f7e39-f866-3ee7-8f54-6e36072aff39 | -4.8429 | -42.92738 | 2026-06-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4aab013-619b-3a6f-b50f-10d7c23213a2 | -4.3402 | -48.66664 | 2026-06-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab822562-755f-3933-b216-5f0c1ebcdee7 | -11.884 | -57.12404 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8bb3298-6680-3940-a5d8-75e3e45339df | -10.82566 | -49.13211 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c30cf1b-25ca-31c5-ac0b-431e00659ca9 | -11.32152 | -54.47129 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48aff71d-a53b-321e-8de7-6c1de3e9c70c | -12.51861 | -48.29432 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80a3a28b-294c-3847-b047-a30d46a89743 | -11.48283 | -47.41565 | 2026-06-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39e51aa7-aafe-341e-a6a5-783a604feb02 | -11.89204 | -57.12995 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25528840-b16a-3f23-9b4a-8a46249ec25f | -7.2812 | -49.68399 | 2026-06-29 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e2be41-d2d3-3213-b36f-a52c329eca74 | -11.88763 | -57.12915 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad19dffa-bc0b-3683-8e4e-c1afe1c82745 | -10.63163 | -50.17297 | 2026-06-29 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddba2918-e5ff-3d38-b923-a4c1f730b199 | -11.51807 | -56.12403 | 2026-06-29 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3b59427-e292-3300-abdc-e4ccab8d65e8 | -9.95351 | -52.19916 | 2026-06-29 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02ca070d-bc55-35bb-9a1c-65366b21d4ed | -11.89045 | -57.13879 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56845695-2aa5-39c5-8a2d-3616f29f2c99 | -11.21223 | -53.82046 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3fb5aa4a-1a17-3fe8-b427-94cd552d69d8 | -10.32525 | -50.17369 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7916ee95-cce4-3609-a5f1-85e4247f1040 | -9.31448 | -58.03043 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cd8e798-25b4-3e18-b1f3-b7daedb1d1fd | -12.2296 | -56.55704 | 2026-06-29 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87ee70ff-1094-3f61-ab52-534f6f210661 | -11.2173 | -53.83457 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1a22eb53-b59f-3a2c-9eb5-52915fe3ca49 | -10.8468 | -49.12812 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ace80211-9772-3b85-9f90-6d88edf6812f | -10.46213 | -46.58565 | 2026-06-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 329f1c09-1a05-3e2e-b036-e56f4e167b14 | -11.51937 | -54.79559 | 2026-06-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 00b3e052-ab00-3651-9819-8e85a6f95b4c | -11.88997 | -57.11614 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826c3207-7b14-348f-9484-691277a6f120 | -11.88964 | -57.14328 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8630001-2b5b-31e6-acba-718f78e9afec | -10.38866 | -56.76599 | 2026-06-29 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4917234-838c-3d4b-bba6-fdd7dcc5210c | -11.64233 | -48.53045 | 2026-06-29 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddeffbef-2eae-3ddb-adde-d4df73d6ebf2 | -10.50579 | -53.57317 | 2026-06-29 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15a579a0-c69b-3cef-8ca4-17544861c961 | -11.48464 | -47.4285 | 2026-06-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a43d2ba-96da-3e9a-8784-3bac2dcba687 | -7.63927 | -50.02801 | 2026-06-29 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56e7dee3-3a7b-3780-af54-994286e491b1 | -9.69116 | -47.69766 | 2026-06-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5742a960-4959-313e-a2b4-4f0d530f81d9 | -11.89405 | -57.14405 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50514786-2bd5-3f0e-a708-de5a7f93425e | -10.32308 | -50.18761 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0b561a7-ef8d-3f3a-9130-f73fd7f95506 | -11.49556 | -54.50173 | 2026-06-29 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a9e69e3-4d38-3735-ac22-2656dc197214 | -11.49932 | -54.50239 | 2026-06-29 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa643039-086f-347e-9655-3c7546cc6205 | -11.21392 | -54.30289 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f95a984-cc91-3d80-b603-3ae54203898b | -7.74956 | -44.17527 | 2026-06-29 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1360db95-0172-385a-a99f-7d4fe3d78b34 | -10.97844 | -49.55619 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c24ddd71-0e23-33f0-859b-6e2cbde027db | -10.32855 | -50.17421 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9dae5622-ebf0-38ff-80ef-93e3d504ad33 | -11.21493 | -53.82243 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2cb5ef36-17d4-379c-a9ab-ae220e91fcce | -11.527 | -54.79697 | 2026-06-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f551704d-0ffa-3d3a-9303-b16cb651395d | -11.21468 | -54.29837 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14303f12-66b1-3d92-a54b-1e738a288f88 | -9.32726 | -58.01562 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 046f7772-6c0f-3903-b97f-fa1d15e4534b | -12.45007 | -46.92213 | 2026-06-29 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22584392-e59b-3d6f-a717-0741a6107540 | -11.50385 | -54.49842 | 2026-06-29 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2abcec50-4f32-34c2-ab07-af500ed3e776 | -10.30459 | -57.12774 | 2026-06-29 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0a1c4d2e-2374-36d8-9320-a085002f1df6 | -12.10697 | -51.98963 | 2026-06-29 04:40:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4e1d823-1a31-3e36-ba85-01a08a7f677d | -10.51222 | -51.93808 | 2026-06-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15783235-147a-39bc-a93e-b6c921110df8 | -11.2115 | -53.82473 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23b38ea1-871c-3ea1-8161-ddd9fd04b6a6 | -10.29935 | -57.12402 | 2026-06-29 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 064a8ee8-19eb-3958-9058-bcdc952f741d | -10.46148 | -46.59017 | 2026-06-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0271050e-da3e-3b55-b87b-13815f9c8878 | -7.5523 | -43.76915 | 2026-06-29 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b37b2183-2c5e-36e2-84ef-b75e6f231ea9 | -11.21586 | -53.82105 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f421adc-afa2-3b38-9074-220a337c2deb | -6.86926 | -47.48873 | 2026-06-29 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a55750-0dd3-39c8-af0c-9385b665e237 | -11.52401 | -54.79151 | 2026-06-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ce41e19-d459-3396-a9a0-bdb1d5242fbf | -11.21659 | -53.81679 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09b2cdcd-243b-3da3-a885-467645fe6721 | -10.28836 | -47.59561 | 2026-06-29 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca859e0d-d695-3823-b9d4-8b097987af18 | -10.829 | -49.13264 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b0c5f07-224d-3615-b932-7d82657ec711 | -12.51717 | -48.29354 | 2026-06-29 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9d688d48-d9d8-35f4-8c12-9e9dd999d1b6 | -13.70778 | -47.85447 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ded800a-50db-38a0-9b41-d8db3215ff26 | -7.95155 | -46.82963 | 2026-06-29 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e902e323-8db6-385e-9504-66da0e39a255 | -11.88322 | -57.12837 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4a14f176-9c5f-39a3-8ead-b84f5233d044 | -11.52101 | -54.78608 | 2026-06-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bca9f7af-48e2-3026-896f-a7c828df6070 | -11.21765 | -54.30353 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2da9527-9353-3495-976d-78a9d2660beb | -12.23522 | -56.54985 | 2026-06-29 04:40:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd3a53c0-39fc-3d24-9ca7-24940038406c | -11.88604 | -57.138 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 574ec288-3d23-3776-9a35-eb3a91993c80 | -11.21564 | -53.81815 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4cafba9d-0160-33b6-9545-e7fc91ff7aa7 | -11.88883 | -57.14775 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b05ca6dd-a4e3-36c1-b5f4-263589c4a4ab | -11.9112 | -57.12451 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474ae238-c134-396d-9b5f-0f801e8db394 | -11.22093 | -53.83521 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e11e0b7-b60e-3585-89b9-c8b014e6cc3c | -9.06954 | -44.77805 | 2026-06-29 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef61c9eb-a328-3623-9cef-d1d49f20ff25 | -11.8936 | -57.12127 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3861e91a-a39e-3c5b-ac12-ef56e059525f | -11.22137 | -54.30418 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03da6770-ab5d-3572-83de-ad1e0fe80e1f | -12.03378 | -55.459 | 2026-06-29 04:40:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27c2ff89-28a2-3ce9-a9a5-5680ebca0860 | -10.33239 | -50.17125 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d2b32dd-357d-33ff-b923-fe99f8dfad3f | -12.37206 | -47.44251 | 2026-06-29 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 867b004e-b6ca-3d68-a282-e8b610ac43c6 | -11.5001 | -54.49776 | 2026-06-29 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bf44670-d240-3503-a032-e3441552770e | -12.20617 | -52.87129 | 2026-06-29 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a7a576-3b03-3c7d-82fa-2c34a1203457 | -10.48711 | -47.10553 | 2026-06-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7d38de6-d51f-3fa5-ba86-7398641d759e | -7.64257 | -50.02853 | 2026-06-29 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ddd7021-474b-3671-928f-c76653f4b808 | -11.50088 | -54.49316 | 2026-06-29 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d292aae3-3446-3bea-925b-1ba3acb16c24 | -11.48996 | -47.41696 | 2026-06-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78246894-f97b-3f5c-aa92-defd5b70092a | -11.5174 | -56.12785 | 2026-06-29 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b87c923e-9bac-32e7-939b-b989ec8ac08a | -10.32086 | -50.18013 | 2026-06-29 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2c2d34d8-bc5a-3b71-a865-dcb7b8a9088d | -9.60304 | -56.92596 | 2026-06-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b0fbe4d3-0c82-3a98-8fbe-a1241ab9a179 | -9.32036 | -58.02582 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3baed88b-caeb-3862-808b-9e91fae8a25e | -11.88919 | -57.12051 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e124eb0-ab7e-3368-9437-7f96522f245a | -10.9779 | -49.55972 | 2026-06-29 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8b053f5-7897-3498-9fbc-384d9795d2f0 | -11.31965 | -54.46396 | 2026-06-29 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfaf296a-dfee-3df1-bfbc-7d68c3e953e7 | -13.7084 | -47.85009 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 174855b9-b7d0-374b-9509-dbffb1d0fe19 | -7.3073 | -46.29068 | 2026-06-29 04:40:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c69e3589-26e7-3dde-a16a-4fc645d56af2 | -11.89565 | -57.13514 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69b60de8-53dc-3f83-b096-5aa336f2f175 | -13.5615 | -47.84758 | 2026-06-29 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8da9a066-d76f-31c8-9c99-5fa36b30c61f | -13.30728 | -48.25313 | 2026-06-29 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57b1d7c6-51a2-3a1d-aa71-eb812e927c2f | -11.88841 | -57.12483 | 2026-06-29 04:40:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9396fdfd-15d0-3df7-b857-8af6c36b61c1 | -9.31548 | -58.02488 | 2026-06-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README4.md)
