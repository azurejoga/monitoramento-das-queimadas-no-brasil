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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dec810c7-eb6a-3bf5-86d2-de7a939ca1d7 | -15.74674 | -59.85267 | 2025-01-29 05:05:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35c58b3a-3694-3f1e-8bc9-002e354eb0a9 | -29.51326 | -51.72795 | 2025-01-29 05:08:00 | NOAA-20 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c008c743-5cc1-3c7b-b900-18e17e198a3e | -29.51296 | -51.73139 | 2025-01-29 05:08:00 | NOAA-20 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a55d1362-f24a-3b4f-8a08-fd82a4dd1507 | -29.51484 | -51.72856 | 2025-01-29 05:08:00 | NOAA-20 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 36801db8-a23c-35ee-bc90-540c8728afb8 | -22.15694 | -56.67822 | 2025-01-29 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 142587f4-4d1a-3721-86b5-6d89251a5bbf | -6.9344 | -43.5401 | 2025-01-29 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| cc71f91a-6ead-3d15-8b6b-fc61e9a3d0fb | -6.9532 | -43.5384 | 2025-01-29 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| e122ca1b-795f-3228-b0d7-c1512484f30f | -6.9344 | -43.5401 | 2025-01-29 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9a99884f-a697-341e-8ee5-7dc15476628d | -6.9346 | -43.5168 | 2025-01-29 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 58df6dba-6b96-39d2-8ba6-32d4be365dab | -6.9532 | -43.5384 | 2025-01-29 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 46a79628-8f69-3b89-b9f0-f6be00c201a2 | -6.9346 | -43.5168 | 2025-01-29 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 8daf7925-1d86-3154-850c-e1f01f11fbda | -6.9344 | -43.5401 | 2025-01-29 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f277ad55-6167-3550-8723-58132b6671bf | -6.9532 | -43.5384 | 2025-01-29 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| a1b92b8a-0ed9-34ad-9a6e-2c068b14d8ea | 3.5298 | -60.35131 | 2025-01-29 05:52:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4244f73-0ef8-3ae2-b4f9-6ea937cbab9d | -3.31716 | -54.91013 | 2025-01-29 05:54:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f7477f4-22f5-396f-851e-a5cdc9c43980 | -10.10043 | -62.08105 | 2025-01-29 05:57:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10fc3fd0-d3a1-370b-9a8f-8edcfbb8ce43 | -10.10008 | -62.07738 | 2025-01-29 05:57:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b84ec631-4c49-3b6c-9582-2ddbe89400fb | -9.23856 | -60.33551 | 2025-01-29 05:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ea46109-74ce-3257-9a3c-87086c93eeee | -9.82485 | -63.56081 | 2025-01-29 05:57:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5a24d66-6207-372f-9344-82cf8fb547e9 | -12.43898 | -64.08469 | 2025-01-29 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40664a45-485c-3f32-a34f-cd52bcda848b | -9.25879 | -60.31747 | 2025-01-29 05:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa314523-e51d-386c-b3ab-2ddf3ebd8b82 | -12.42349 | -64.13763 | 2025-01-29 05:57:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b8d5c2-31d2-3caf-a18f-f85a8a0b976b | -9.26253 | -60.31345 | 2025-01-29 05:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 934cc7c1-0727-3b0a-b67a-bc9799ccf4fa | -9.17264 | -62.38756 | 2025-01-29 05:57:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3aaf87c6-6302-3831-8bee-1e7b05a40476 | -11.25895 | -60.79396 | 2025-01-29 05:57:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cc1410e-f60c-32fc-a711-2777f86d2248 | -9.25919 | -60.31435 | 2025-01-29 05:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 313744e4-b369-3c09-aa88-6f3e589c2bcc | -9.17711 | -62.38819 | 2025-01-29 05:57:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 173c5a22-817a-367d-a571-96432b0b3428 | -11.25933 | -60.79087 | 2025-01-29 05:57:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30d2dc11-f503-332a-8b28-cd86a0ab5a3a | -9.2621 | -60.31659 | 2025-01-29 05:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a453d4e-2782-387d-96aa-35d7467b9a14 | -10.22696 | -64.22042 | 2025-01-29 05:57:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2ec4fa6-ece6-330c-a77b-647a87d964b5 | -6.9532 | -43.5384 | 2025-01-29 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 949f62d3-72d7-35f2-af6f-9ac2bed56193 | -6.9344 | -43.5401 | 2025-01-29 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 14e535d2-53bf-31e6-aa8d-12d4cb9fc2bf | -6.9346 | -43.5168 | 2025-01-29 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 38810d5b-1775-3dca-802c-7fe73c69ad2b | -6.9532 | -43.5384 | 2025-01-29 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 16928b2f-5697-397c-8d76-d39ded0efb1b | -6.9344 | -43.5401 | 2025-01-29 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 499f55f0-f83c-347e-88b2-add10b91bfa8 | -6.9346 | -43.5168 | 2025-01-29 06:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4016be90-8e52-37c5-8029-68e0702a8ffd | -15.83 | -43.46 | 2025-01-29 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c79d98f-1220-353b-8f5c-40264fa833a5 | -15.42 | -43.79 | 2025-01-29 12:00:00 | MSG-03 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f467b04-b00f-3451-a7da-1e85f96accbc | -3.58728 | -48.95662 | 2025-01-29 12:44:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 81a912fe-dd3b-33ac-9bec-27c4a52b2a95 | -3.5541 | -43.65585 | 2025-01-29 12:44:00 | TERRA_M-T | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2c0ea570-436d-30ea-a2c6-6aa4d8cfcbaf | -3.51917 | -43.65126 | 2025-01-29 12:44:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 81770601-05de-3baa-adf1-f8d9a0583571 | -3.66646 | -45.37845 | 2025-01-29 12:44:00 | TERRA_M-T | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b5be420a-8be1-3c1b-995d-d4f4f598e4db | -13.18971 | -45.22414 | 2025-01-29 12:46:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1df5cf0f-85b3-3756-942f-c9a6596f051c | -12.798 | -44.8941 | 2025-01-29 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 17b20fe1-66e7-3008-a8fe-6dcba6988aed | -12.74317 | -44.83185 | 2025-01-29 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 8742a705-ec18-3bd9-a486-b47dc40b4383 | -10.74288 | -52.77045 | 2025-01-29 12:46:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 50d65702-3837-3c27-b2c5-591df33fe7cb | -10.6778 | -47.20065 | 2025-01-29 12:46:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7e0b4a75-93c6-3e70-89c4-9ba47760323c | -11.06345 | -52.12566 | 2025-01-29 12:46:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6f09420b-e07d-37ea-a9e3-5847ed1b1143 | -12.7533 | -44.85171 | 2025-01-29 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b4263afb-811f-3042-96f9-c4220b3cbaf0 | -13.09198 | -45.27634 | 2025-01-29 12:46:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0849beaa-ffcd-3e58-8c35-f87a24ecc0df | -11.08095 | -53.82701 | 2025-01-29 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6d42ee6e-8644-3a47-b7a8-7f3a829709c7 | -11.14238 | -52.69837 | 2025-01-29 12:46:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 35d120f2-4015-3646-8ca2-af208fffc7ef | -13.09032 | -52.26704 | 2025-01-29 12:48:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d132efd6-0b44-34c4-a887-2848e8145ab4 | -13.59398 | -54.34323 | 2025-01-29 12:48:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7fe0ea23-ac54-3d96-af86-e0e710f68278 | -13.47077 | -54.92001 | 2025-01-29 12:48:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 858c2b6f-3b8d-3533-a00b-f9812269cec9 | -13.23542 | -55.0986 | 2025-01-29 12:48:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0d13c5ed-ae22-39c7-803e-06f99001d197 | -13.23441 | -52.53755 | 2025-01-29 12:48:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 74a22eb2-dc6d-3517-a152-11b61dc4f82d | -13.53307 | -48.22011 | 2025-01-29 12:48:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c1b7877a-d7c5-3831-be9b-cb4ffb2f5639 | -19.80653 | -53.79346 | 2025-01-29 12:50:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |


