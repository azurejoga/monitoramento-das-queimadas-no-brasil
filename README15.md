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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b034d143-aca0-382a-a631-289ba55a0a3f | -9.59455 | -56.92802 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a33fac1-abea-30a6-87c8-23d5751928ea | -11.93145 | -57.71143 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d10bf45-c30f-3c81-be60-d6fbd6f6d2a4 | -9.32482 | -57.83222 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b6dff35-877b-3e85-a437-13d5e9711639 | -11.88218 | -57.12428 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93398a90-9028-3a8a-a80a-e64a83f30a83 | -14.2015 | -57.43299 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 882a1d40-8183-3707-9e0b-3d6665c89571 | -12.60899 | -57.89187 | 2026-06-30 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b555f70-d2e0-35f5-ae2d-c38eb729dab9 | -9.17194 | -58.0684 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21a17155-2be2-359d-977f-1738d33ca473 | -10.13354 | -52.40721 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e555dbfa-3e77-3ff3-8b51-f1148c8a918f | -11.21424 | -53.81797 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcc41e4e-1897-3a40-b55f-cf6df5064ca6 | -11.21889 | -53.83614 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1c50108-ac4e-3fce-9864-bcaf4dda6a92 | -11.88443 | -57.1095 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd06b3b1-ed69-34fd-9dc5-617687d5a036 | -9.59901 | -56.92137 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecc73ee1-243a-3ae2-8877-d7b30ee7db09 | -11.47707 | -47.41355 | 2026-06-30 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1a4c040-a90e-3e5c-a4d8-08e8586c8eff | -9.44879 | -50.83966 | 2026-06-30 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5e3fcf1-edd4-3179-be41-bcc2c58847fe | -11.88894 | -57.12535 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01ba35bc-8ddf-31dd-aa70-0ad809c9af88 | -10.78503 | -54.10562 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a361bc5c-590b-39c2-b1d7-571b4e583ae3 | -11.88274 | -57.12059 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93e663c3-41ef-3b68-8f6a-46a1c426d609 | -13.72293 | -47.86736 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3eff98be-7a8a-34d7-807b-96ff2bb2029f | -13.7088 | -47.87376 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac034d23-bedd-3049-b3c7-422a79cc23e0 | -12.14748 | -57.22522 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3205c14a-3d5f-38d9-a2e1-10d525d0b7e2 | -12.44842 | -58.4887 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb7f6e9f-f678-37b0-8996-383fee889188 | -10.37794 | -49.59298 | 2026-06-30 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5babbf6-e335-34c3-8373-a796e92b3480 | -11.89515 | -57.13012 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa5a75ff-d222-3207-aa82-1f5c44065100 | -12.45063 | -58.49629 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09d89753-6036-3b50-98f2-e99e77281163 | -13.2631 | -56.78738 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f0934e7-864a-31cd-a906-e4992c76966e | -11.92227 | -57.39234 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 851a2d55-69c0-3a2e-ac03-70f641c6d59e | -12.16842 | -59.75714 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 569a85cf-9927-3b79-8da2-3e9040e107a7 | -11.21959 | -53.83107 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30802ecd-642c-318c-acea-b6748dec000c | -11.89402 | -57.13749 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1be5c291-4891-33bb-8139-13eefed021c8 | -9.31848 | -58.0238 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f55bf5-75d5-398f-81c1-d356f67bce80 | -11.8991 | -57.12696 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07f018e2-eeaf-31ac-bcbd-1143f2b1e62a | -12.22018 | -56.55831 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03cf9139-a532-3dea-8048-ecc64e3f2e9c | -11.89628 | -57.12273 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11e70b7c-7057-38ba-b5c7-9833256520c1 | -10.37836 | -49.58984 | 2026-06-30 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 585b8599-0d5e-3b9c-91be-182e71c9338e | -9.32509 | -58.02486 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cf5d1e8-e813-3f59-b73c-aeb183c56813 | -13.26252 | -56.79127 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96239fab-a736-39dc-91d5-81f5c76098fb | -13.26422 | -56.80345 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b47542cf-6e4c-35cb-9985-62fb45daba1f | -12.50564 | -48.2739 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 244a779c-ce75-3542-b15f-e355be5f791a | -11.2225 | -54.3162 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fffea8d8-7cb5-3763-bd77-9534a6ab7af2 | -12.03421 | -55.45653 | 2026-06-30 05:16:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ace99976-6e1f-3835-befc-cabc59199aeb | -12.21731 | -56.55388 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d14ce52-8f7b-3827-8fd6-34d38e44dbf2 | -11.95655 | -58.61457 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8865459-2453-3994-ab64-9faf8138f798 | -13.26076 | -56.80293 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a58003c1-66d4-313a-9cad-05aff9eb33a6 | -12.45394 | -58.49682 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd82e6f7-ba5d-37ad-a7be-3e894714c779 | -10.91174 | -56.85561 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 437e42fa-c758-361e-8b36-f756f94dea24 | -11.8912 | -57.13327 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09bd301c-91c2-3d15-9590-1e97f803f87d | -12.50562 | -48.27306 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e93674d-57b5-3445-ac16-943f73b97bc0 | -13.25097 | -56.79743 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 695257c5-32b2-3878-9b34-fe0a30aa4b4d | -9.17249 | -58.06492 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c57349d-e7fb-3a67-a811-7d09e5dcff45 | -11.90377 | -57.37822 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a29a149-1ebd-3886-9bf9-421e9c33e520 | -10.04929 | -59.1104 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 656d80cc-1bf0-3d9b-83ba-13af0696974c | -12.45173 | -58.48925 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 531fee25-06d1-3296-8ac3-6fbf27dc06df | -12.52111 | -48.29224 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1944c2a-f8b5-38d8-b9fb-d7508ab05082 | -11.88443 | -57.1322 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71a4ae06-04d9-3415-a3ce-df278820b6fc | -11.21596 | -53.83393 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02c0ebbe-984e-3ba4-b764-1d85407066e7 | -9.19907 | -46.63174 | 2026-06-30 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 091d2153-90dd-3aa0-bd4a-1398ae75cea5 | -8.70463 | -50.71144 | 2026-06-30 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e564cabd-8b32-3738-9828-e489af5c605f | -9.60126 | -56.92907 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea1890f4-5d53-3377-986a-50ddcbd081be | -11.90079 | -57.13855 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bd5c566-e66d-3bd8-a336-d134334ee705 | -15.07181 | -55.80993 | 2026-06-30 05:16:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92446e16-2b74-38d7-afbe-c95c143e5a08 | -13.71485 | -47.8746 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58da7d3f-46e3-3ded-b31d-1598c2a90f7d | -10.71532 | -56.21018 | 2026-06-30 05:16:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f2cbaeb-18db-32a7-84df-bdc08372a8c0 | -11.21661 | -54.32993 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8b3b575-89f9-3944-9f00-50eff7d11f3c | -9.08544 | -59.39166 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af073631-5340-3dfd-89c8-8f56a6115b48 | -10.30086 | -57.13014 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48459bf-6e15-33b9-a813-0bb56655f283 | -12.61343 | -57.88524 | 2026-06-30 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d2e405c-1bb4-37e8-acfe-2d135f802c4f | -9.60517 | -56.92601 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2f8a2883-57ff-359f-ab33-45498e125b12 | -9.74662 | -49.0256 | 2026-06-30 05:16:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0f46651-3642-3607-b751-af6444ba4e31 | -11.9359 | -57.7048 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79108a4c-53b1-3c8b-8885-ac9f932558ac | -11.88782 | -57.13274 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 666e8e36-6668-3569-b403-b3ec2c9a947f | -13.7035 | -47.87629 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8aefb725-9d42-3657-90f5-8d0c3100389f | -10.38354 | -49.59055 | 2026-06-30 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c4cfa3b-8012-391c-83e7-a687b0468be7 | -13.25789 | -56.79852 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00e18385-cc77-3ef0-98b6-b3f3c2c68d43 | -9.60742 | -56.9337 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc8fbe06-e000-3530-8ba4-c4e4d9046a39 | -12.44676 | -58.49927 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f51f8af2-9e36-320f-b7c0-23b8ccede107 | -11.58116 | -47.92559 | 2026-06-30 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 357fb27c-2aae-34d8-969c-d53268c3d47f | -11.23015 | -54.31734 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37c60ae1-6ff8-3af6-b72e-eaa06f0b8bb0 | -13.25501 | -56.79408 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54a708a4-f998-3297-811a-3978fd8018c7 | -11.57979 | -47.92349 | 2026-06-30 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2e6450c-6431-37ef-adb7-4eb9117d5467 | -9.20326 | -63.52532 | 2026-06-30 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a21b970-bd98-3e12-81ed-565a25b2803d | -12.44732 | -58.49575 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62ac623f-a073-346e-ba9a-fc0a5a4ed318 | -10.13072 | -52.4039 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5076bc27-5701-345d-bf10-cab965bdb817 | -12.1999 | -52.86318 | 2026-06-30 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dfadfe03-d4c2-3241-a0c2-04484aa12868 | -11.79744 | -62.37578 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff125133-ee84-3a34-828b-3ca1e3076657 | -12.50616 | -48.26967 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86054d76-982f-30ca-bc6b-f7120adeeb59 | -10.90496 | -56.85456 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e189a5e-928b-3738-a0dd-713b5165a5aa | -11.90887 | -57.4125 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e7f70d6-973a-32cd-aca5-2e2e0749033d | -12.44456 | -58.49169 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba54049b-2891-35f6-ade6-be5e92c1f024 | -13.26018 | -56.8068 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ea55888-465b-3721-bac9-0c7230f94712 | -12.20786 | -52.86845 | 2026-06-30 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 797ec5d4-cbf2-3a4b-b7b8-69d25ac045fe | -11.47651 | -47.41829 | 2026-06-30 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dddb0281-100b-3bae-a6f7-694b796cef12 | -9.18611 | -58.06682 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27e32021-6675-3a3d-b725-1fc80418a02c | -11.11162 | -54.14463 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 999b7f6d-b0a9-37b6-b912-bc53bd1011f9 | -12.60286 | -57.88721 | 2026-06-30 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a79d2fc0-2062-367b-8e15-073f7353d33c | -9.19794 | -46.63089 | 2026-06-30 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84b3af5c-5dc8-303c-99e4-20214c0cf403 | -10.85359 | -56.66068 | 2026-06-30 05:16:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60dd5aaf-9693-339c-81bf-c98218270de8 | -11.9004 | -57.37768 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72eddd86-5191-3de3-9d71-ec6f1494a5c1 | -11.90496 | -57.41558 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c96d06c-cb22-33b0-b388-9313cb0e5497 | -13.94806 | -53.95084 | 2026-06-30 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 564ab89b-b659-32be-9279-f9c8b8851ec9 | -10.14261 | -52.40445 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README16.md)
