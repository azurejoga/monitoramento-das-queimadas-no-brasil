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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6175e133-a61b-3672-be59-f09cb5802d0c | -14.43031 | -52.50621 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfd18320-e08c-37e0-9b42-eee736ea0deb | -15.02778 | -52.76763 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 993a8bf4-5ae6-36d2-a5cb-8a6251bcc454 | -14.39784 | -52.47873 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a187d3f1-b99b-3a79-8ec8-f0d87d0012ea | -15.83796 | -47.68563 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c72aac6b-f945-3a07-8fcf-ff6c41e33c0d | -14.26698 | -52.86223 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95c2cabc-0058-3882-ad04-364a62507847 | -17.13811 | -46.8374 | 2026-09-01 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 941af3c5-13f0-3db9-aada-2239a85e58c4 | -15.38101 | -52.81634 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb15a7ae-2fbc-3183-b2cb-c291328ee110 | -15.6388 | -50.10708 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56558a24-c814-3b55-ac12-423dc586cb0d | -13.62725 | -51.82686 | 2026-09-01 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8b2270f-9c70-3a77-9144-918fdbcd94f5 | -16.52945 | -49.42249 | 2026-09-01 04:42:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7993177-3eea-3e6e-b2e3-b09f7be73a1d | -16.93283 | -47.92133 | 2026-09-01 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54f8c0c7-2916-3de0-97a0-8836124a22b7 | -15.2399 | -53.84818 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8daa28b4-7054-3436-96c8-1bcf7541394e | -14.42915 | -52.51345 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6485782c-a98e-360e-b3e8-05f7947964c9 | -14.39597 | -52.51191 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1b15753-eb8d-32e0-b092-c79db59a8832 | -14.41178 | -52.47733 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1da68e1-3087-3c7b-89d9-3bbf07671d5f | -16.3599 | -51.01956 | 2026-09-01 04:42:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bcd33a58-d8d3-3622-b243-b7da3c47c0a4 | -15.87045 | -56.48076 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c8e1cb29-12a8-3e1b-84b5-b18ea4779983 | -15.64951 | -50.10499 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31ee120d-1716-3877-9fde-bfb6c381646a | -10.50588 | -59.61983 | 2026-09-01 04:42:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c87ed717-62ee-3fa0-9c99-35c339df0c9d | -15.0239 | -52.7562 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f2d3ee0-876a-3be1-be44-4c6c0ea75621 | -14.41728 | -53.14701 | 2026-09-01 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c0a89a4-ba1a-3053-bddd-f92c1e6a8f20 | -15.03507 | -52.76516 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46871d73-67b1-3a94-a85b-6aa0cc81a992 | -13.38304 | -51.75764 | 2026-09-01 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 235fda39-54fb-3f34-8ee5-3bf10b7d6e51 | -15.18436 | -46.24426 | 2026-09-01 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cf41464-4779-36cb-a8e2-950ca87a86a4 | -14.50764 | -52.23764 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fa77ba3-3180-3053-b57d-585b629ba0cd | -15.60377 | -46.58083 | 2026-09-01 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c6b66d7-a9aa-3829-b4c4-646dcb81863b | -13.5514 | -48.24183 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb3a485-e364-3a35-9443-68caf3653cf1 | -15.63542 | -50.10652 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c43149d-49fc-3f12-abf9-46207c3cad62 | -14.26239 | -52.86907 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e4df89c-d9a9-37bb-abef-734dc81996c8 | -15.65401 | -50.09808 | 2026-09-01 04:42:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f17f574f-3f95-3ca4-a6af-8a4bc3bf5059 | -15.60827 | -56.38752 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 871f2b99-6171-365a-a4f9-49acc351a923 | -14.46425 | -53.37234 | 2026-09-01 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d54a7e7c-fa62-316c-8173-98693cb18a9d | -15.40147 | -52.71088 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11cd287f-774b-328a-aab8-d26b6bf5a31f | -16.54426 | -49.56743 | 2026-09-01 04:42:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 77ae3479-2367-33df-a5b8-7611bf8f4616 | -10.41566 | -64.46059 | 2026-09-01 04:42:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5a8226a-0cfe-3b89-a975-044b2df0c36d | -14.40047 | -52.50522 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 72798e30-38fb-3765-982c-c2dc957ad00d | -16.18896 | -49.32097 | 2026-09-01 04:42:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d1b18fb-d61d-312e-aae8-59490827afd0 | -15.65646 | -48.70061 | 2026-09-01 04:42:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd633ed4-f63e-37ae-8a67-f82435e01a02 | -14.39655 | -52.50829 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1e65632-ec65-36fc-8e93-ee23383f8641 | -15.76483 | -56.08338 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 98a98cff-7469-3c91-a555-d4677cff59e5 | -14.0026 | -54.08111 | 2026-09-01 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c21110a-94fd-3a87-b931-abe20b6825f5 | -17.39113 | -42.35689 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9b693e6f-0200-3207-9c3d-d9dbe5f580d3 | -13.54783 | -48.24133 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 256d8d7f-7a8e-35ce-b26c-42bf0afbb621 | -13.09692 | -45.17675 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a13e7bb4-edd4-3175-b58b-616f5a2f1eb6 | -17.38501 | -42.36276 | 2026-09-01 04:42:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 982afa05-d05a-3ec4-ad03-30cf3ace5f8a | -14.13629 | -52.79445 | 2026-09-01 04:42:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6263de4f-c715-380e-9e60-1599691e60be | -10.50186 | -59.61229 | 2026-09-01 04:42:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5c7f172-aa42-3e7e-bdcc-ba9c7043bed3 | -15.26298 | -53.88042 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 408a2681-4175-3e68-a60c-bea6aa9c35fb | -16.37047 | -54.52034 | 2026-09-01 04:42:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cee8f64e-3d45-3970-b721-0fac47835c63 | -15.29837 | -53.85362 | 2026-09-01 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3bd61e10-4af2-3a36-9879-a261c69249c6 | -15.84862 | -47.69205 | 2026-09-01 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 891b0cd6-8f92-3655-a3d6-1921d3ef5260 | -16.47697 | -47.95141 | 2026-09-01 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 1e77930f-7cf1-380b-816e-e746d2f7f3fe | -13.27895 | -48.55099 | 2026-09-01 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c976dcbe-750c-3cbb-8981-4b3f3950bff9 | -15.63809 | -56.38034 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d456932a-b420-304b-a7e5-5d5b6e904afa | -17.20958 | -47.63693 | 2026-09-01 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba607acf-1e28-31e7-9304-f6479bd55621 | -14.51326 | -52.22382 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32df3a4a-55cd-30ea-a682-45ac24320a34 | -12.9127 | -45.82787 | 2026-09-01 04:42:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1be1decc-9e4e-3536-bf72-b84239d6585f | -15.21939 | -56.34982 | 2026-09-01 04:42:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9eedfc3-621c-31bc-bb33-bbfd63a3cb7d | -15.639 | -56.37525 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a05c5f54-7cff-34c4-8c50-e9cab2129e39 | -15.24163 | -53.88062 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 374da5d4-b059-3ab2-ad8c-b3d96697df79 | -14.44761 | -52.50538 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2b4c87d-d795-38d8-910f-d67e0e95b435 | -14.27624 | -52.89044 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5065adcd-30bf-34e2-a5f3-ac54b367f266 | -15.23112 | -56.35196 | 2026-09-01 04:42:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9736dbd-5655-3a91-ae8c-5644c0565cf6 | -15.26234 | -53.88433 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d6c08ee1-046f-3d3c-a045-a3389b572d13 | -18.25331 | -52.72829 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 083d7077-21ea-3d0e-a98a-0c4c1de77ab2 | -21.4546 | -43.91069 | 2026-09-01 04:44:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8121223e-a3ca-3a83-9405-526515471055 | -21.45976 | -43.91145 | 2026-09-01 04:44:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5464c3ef-86a0-3263-9d96-4098b9d4bd23 | -21.46009 | -43.90818 | 2026-09-01 04:44:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f86e9ac6-9501-35b3-97f7-adceba6924fc | -19.90662 | -47.90656 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bdd775c4-c8b0-30e8-8f9c-6414ca2245e9 | -20.37286 | -46.56729 | 2026-09-01 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f6058bd-2033-31c5-8fc8-6c5445890746 | -19.89944 | -47.9002 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d52b5185-25c4-3efb-a202-ebbf7f320096 | -19.8955 | -47.89973 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f95e9754-bc45-3623-9a02-0a43e6f23836 | -19.17864 | -57.31865 | 2026-09-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 100cf94c-d1f5-3812-8987-1e83008034f4 | -21.86852 | -42.03399 | 2026-09-01 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 987e3fcb-a212-3a8c-8634-809f43bc556a | -18.28794 | -52.65973 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a5a3af4-4346-369f-b510-ce26f93d5c25 | -21.87435 | -42.03497 | 2026-09-01 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cfe8839d-bcc4-3d1b-9338-e524eda0bdce | -17.94644 | -54.01916 | 2026-09-01 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88741c9c-bec4-3548-96cf-0039fcf1992e | -18.29456 | -52.66088 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05068fed-4791-3bfa-97bd-974e63f644ce | -19.89091 | -47.90444 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dbb3193-ea23-3a07-852e-35a477e794ca | -18.25071 | -52.70174 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73ecfc82-d063-3685-8293-36813d8d054c | -18.25128 | -52.69811 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2890672e-58c4-3073-acbe-2cac8b914acb | -21.24946 | -44.52335 | 2026-09-01 04:44:00 | NOAA-21 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 39306c16-9847-3acf-954d-884b8d67e9c8 | -18.25981 | -52.75177 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65d75f25-11be-35b2-9dec-b7e368eff86e | -19.90984 | -47.91259 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a3efec12-91e8-3dd5-8f1e-b1b294fbbf27 | -19.10632 | -57.40442 | 2026-09-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 57858746-a48d-37cb-9e71-7667af4e74d6 | -20.97454 | -45.57979 | 2026-09-01 04:44:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c8635c7-c6ef-30c7-981d-d78ea9baac64 | -19.57027 | -45.71693 | 2026-09-01 04:44:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c07bb8ea-424b-3fca-ba48-10e8485280b3 | -19.902 | -47.91142 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 03036e3d-f751-35ef-8a33-586c04ef123e | -19.10537 | -57.40965 | 2026-09-01 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 49128365-c96b-38b6-801e-0eb343197f96 | -18.25013 | -52.70537 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b029b521-47c5-397f-b390-fbc4a40d4f82 | -19.72354 | -49.39916 | 2026-09-01 04:44:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e0c47a7-8fc6-333f-b40a-b7f4d3b404e9 | -18.25821 | -52.74032 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 99409ac3-b9c8-32f4-b040-d23ca2e4d929 | -18.14197 | -51.54098 | 2026-09-01 04:44:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ec081d6-618a-36bb-819c-02321d523701 | -18.25433 | -52.74338 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12d3efda-3607-3e80-a113-b3a2798e7b66 | -19.91446 | -47.90773 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5e06efe9-7cbc-3543-b83a-66dec5d5cfb7 | -19.90592 | -47.91201 | 2026-09-01 04:44:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2aad4a8c-65ca-3fcb-9efb-34158da713b8 | -18.25185 | -52.69448 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b57132c-8f16-3ae8-9924-401f7d87e835 | -21.45493 | -43.9074 | 2026-09-01 04:44:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 55b7bd85-5862-3461-b8ee-de0cc1aa3cfd | -18.25274 | -52.73192 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5743ab08-9d53-3911-8618-73d4811fb04e | -18.25217 | -52.73555 | 2026-09-01 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README51.md)
