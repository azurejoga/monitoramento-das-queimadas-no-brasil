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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6d5f248-1f2e-3de8-ba86-cdffc1771565 | -9.14295 | -60.77733 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4637b6a8-aa69-3179-88e3-11589dc3cb02 | -11.32255 | -43.53907 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7373cfb-4b13-31aa-b777-806eefcd2537 | -14.36887 | -52.09137 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50706a37-5994-338d-9bf5-fa877ce51a98 | -9.57763 | -55.39008 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed793de6-ce7f-31fc-a529-4a0aa69dcf17 | -11.32949 | -43.53462 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af6e2c81-1384-3d2a-8a3c-a4a57f69192c | -14.34272 | -53.34472 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 169f9768-85e1-387d-b0e7-31947b426091 | -12.92967 | -46.33228 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26447970-b656-326e-9b34-f58903e70f5c | -14.27537 | -53.06499 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 6acf7fdd-6ca8-3d9e-89ba-09c876615eba | -11.54989 | -46.35996 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bcc609d-2f00-3522-9299-6dddecd7b4fc | -8.55996 | -62.64164 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ae8ddf8-56f7-39c2-a8e0-d3da002371b9 | -10.47099 | -57.93463 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08a823f0-60b3-382a-987b-a6ec63c8d021 | -9.40821 | -60.52964 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f39715b4-a831-39bd-bbde-bcf9bb995e32 | -13.61862 | -48.24022 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 56657988-3738-3311-bc22-9c2a21540a63 | -9.40259 | -60.51318 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aebfef8-a4e1-3ddc-89b5-c6f974bb8aeb | -9.17479 | -59.45251 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f2763cb-3e54-3fe1-be7e-6780a10c3f82 | -9.48597 | -62.38985 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2b6710b-790c-3047-8124-970236fd6d3b | -13.54594 | -46.89674 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94aaf969-06a8-327c-abda-7d8b55762ca9 | -12.77919 | -48.16975 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b7daeaf7-0705-3e7e-a9b0-3fb444adc230 | -12.89127 | -48.09374 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81e6e11a-a863-34e1-aca5-b5e41ecbf513 | -9.24904 | -64.41224 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 71b87113-29fa-31a0-ae76-5f232ca756b7 | -10.46361 | -57.95778 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| f9cd8296-33ab-368b-9882-41694e2c23cf | -13.48713 | -46.8509 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3398b0f-257a-3ffc-ad09-59800f071011 | -10.15742 | -64.24848 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 952d6e28-1b73-3a43-9fbd-26a50f789a85 | -12.11836 | -55.19312 | 2025-08-28 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 034b8bd2-3e68-308f-a2dc-c1cbd1696a34 | -10.80535 | -60.77771 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5d14df2-f02f-3946-a1ff-510248aced47 | -13.67262 | -46.90854 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 435a020a-357c-3086-9aa3-d5015de747f3 | -12.8208 | -48.14824 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 874be0c0-631b-347f-ac80-20cb2f6d8cc8 | -8.91864 | -60.7154 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac4cd2d2-357c-3b99-91b1-5ba32c967a2e | -9.48045 | -62.39394 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71a3941e-2bac-37b1-8cd5-ff767f70e5f7 | -13.63764 | -48.24007 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04c3ab3e-e40e-319d-a8dc-3f78e60f1d73 | -11.83143 | -46.80381 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 958e0c89-b315-346f-a526-0db2e17abc09 | -15.08471 | -48.51216 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e7ab634-75ed-30be-8484-182109047821 | -10.10953 | -55.16539 | 2025-08-28 04:59:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a6654bc-6e6c-38eb-84f2-e292452f206f | -8.96079 | -65.94754 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50ef5b52-79e6-3bea-938c-edb84bc15e51 | -12.94672 | -46.32786 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48adb292-6844-35da-8d19-0490617780f7 | -9.4643 | -60.30362 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96cd226a-a241-3108-93de-d75f8fb115ff | -11.23736 | -55.06298 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f20e08-72fa-3ce8-ba5d-eb3eee769b3f | -11.3776 | -54.3477 | 2025-08-28 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9355a4d4-7de9-3a6e-b47d-d7146e279aa5 | -14.33568 | -53.34447 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6dc3e57e-4b4c-3ee8-b759-a9560f7b04bf | -11.55852 | -46.33384 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a709d390-769a-3010-a118-2ff39e37a1ce | -10.46777 | -57.95441 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7eaec007-1336-332a-b768-61674d5b9adc | -8.95403 | -65.95082 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12902cfb-ec69-35e3-99fa-c5f5688ff9cd | -8.94213 | -65.94867 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e148668-3e5f-311c-bb20-d5998bcc94f3 | -8.94398 | -65.9563 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edae870a-d0d6-3866-9ecf-0e5e0ae5a42d | -14.31878 | -53.05713 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f237e19-9f3d-3cde-b7d9-8ad6d226e62d | -9.5106 | -62.78307 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b634190b-b713-3fa1-b2b1-eb71b5c944d0 | -13.43608 | -46.96513 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60df447c-8afd-361d-887c-7fc667bec95d | -11.57547 | -47.6237 | 2025-08-28 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb290c99-4dd6-3759-9753-da7f8dce354c | -11.24423 | -44.97868 | 2025-08-28 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a95e404a-acd1-37f0-83ac-4d0dbeb296a2 | -12.9343 | -46.33969 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bef93fad-0651-3850-ab5d-0d8d555df561 | -14.27336 | -53.06717 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 863f3aaa-2c85-3ee4-8036-3fc890c33577 | -9.5956 | -55.38582 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dfbc9e00-61da-35ed-b95d-62e57b3cbeaa | -15.11028 | -48.5855 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ea7a748-9818-3b5c-a567-5c09a8412e8c | -10.60322 | -55.40169 | 2025-08-28 04:59:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 745f9d9f-d749-32f6-b191-eb1eae366368 | -11.56688 | -46.39691 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a0a4caf-1c9f-3a96-ba3e-07579d7280a3 | -10.07755 | -62.89411 | 2025-08-28 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cf51a0d-39ad-346a-a507-72654808d793 | -12.22826 | -64.22775 | 2025-08-28 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f160208-8eb8-3874-88ae-9a897f752fff | -14.35276 | -53.35055 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d7ff14e-bb59-3370-bb76-338105ef2337 | -9.80026 | -64.27324 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47a83217-5426-3c5f-92f7-646f6da0fe46 | -13.6722 | -46.9099 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25740cf3-ef34-35cb-92a4-fbd7d507ee8f | -16.3681 | -43.79131 | 2025-08-28 04:59:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 137e3a95-f282-3cf2-8daa-344945562f77 | -12.79904 | -48.16651 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c17b26c5-9958-3e46-abef-819c9ecbcfdf | -9.5058 | -62.78223 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ef984b9-c814-3363-93d3-f2427cf66be4 | -13.43083 | -46.96458 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cef090cb-e6cc-3eea-ba06-c9991efe3ca7 | -8.95485 | -65.9464 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3cff1811-99a8-3de2-b10b-d3acbde4feaf | -9.47008 | -57.84105 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4161b2b-a827-3226-adee-4bb4f5bc0a14 | -15.07418 | -48.64365 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a4610a3-7bb2-3bbf-8e47-03aec5dcbaa1 | -12.79167 | -48.18675 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a8254fd-c162-3a14-bf5a-e466a34eb789 | -8.95334 | -65.97172 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4be310dc-e816-3edf-afc8-1063b48b96fc | -8.96266 | -65.97079 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c1b1b8b-ce5e-3b41-a980-22ad76dd771f | -11.17027 | -50.53691 | 2025-08-28 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 334cb7db-67ce-383d-8b7e-0403af6bd04a | -15.03258 | -57.18795 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04848003-49af-3dd7-8532-84ffa349a07e | -13.18594 | -45.28936 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 81fc085d-a8ff-3731-b620-51711b986a9d | -10.806 | -60.77398 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36dbc803-4349-35a7-bfb0-c082f8e8c518 | -9.41103 | -60.53783 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98c3b93b-69a7-32b7-a4bc-a26031523363 | -12.70593 | -48.17095 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e592f67b-c180-30f2-97ab-4abe8ed0fd3f | -8.88245 | -60.74974 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 225bf3e9-6aed-34fe-bc3d-f56db6778cc0 | -13.45155 | -46.96907 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87dd0a17-0ea3-3aa6-8c69-aa5434675265 | -9.12777 | -65.78255 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 187c1677-a994-3534-876b-5549679e69e7 | -9.46774 | -60.30791 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13b08134-9f1b-39bb-aad8-587c1807ad81 | -9.17866 | -59.45318 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc67f64a-0053-38f2-8775-5bc367b14b8a | -15.64435 | -52.76022 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a0ccd6a-409a-345b-b37c-fdb120f113ca | -10.47199 | -57.95427 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23973a64-d746-3c66-b6d4-f684292816d6 | -15.60612 | -52.72013 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce79102e-aca6-32d1-81c3-2783400b36f3 | -10.4601 | -57.95716 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f33b0f51-2613-3bc3-aab7-ec715b3d583a | -8.90956 | -60.71788 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4428ec04-9833-38d6-ba2d-10d2a9541beb | -14.27414 | -53.07349 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ecc8d08-ea81-35e2-960d-4557a847beca | -13.4219 | -46.99425 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| afa61627-76af-3197-b462-3d3832f53c8e | -13.99329 | -46.34782 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd17871a-667e-3ca4-9a26-1578f62c9343 | -11.35998 | -63.27769 | 2025-08-28 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 77229080-baec-3182-b805-49e154695e41 | -14.3613 | -52.09024 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 296c5393-57aa-3f2b-b862-36245efd8f3c | -9.14195 | -65.77176 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b28796-7888-3cdc-a2f2-670fb9ad39c6 | -12.43486 | -45.96156 | 2025-08-28 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b690ee3d-6a32-312d-9513-52bf3a23dc7f | -8.95587 | -65.95852 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bccf0c22-0d9a-3b26-9b95-706dd305456c | -13.34864 | -51.78933 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6eb7e69b-2300-399b-b7c6-f43826d85fad | -12.81118 | -48.14729 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 873cd8ba-4007-3d0c-a71c-779e747df450 | -14.51573 | -53.0928 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10482539-0afc-3d2b-8bb2-c27ea937e131 | -8.95417 | -65.96736 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8b40a242-351a-3e16-a4f2-1eaf7da7a1f9 | -9.40625 | -60.54088 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 658609fd-0280-3309-9e6c-c5f5bb939ceb | -12.43443 | -45.96519 | 2025-08-28 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README65.md)
