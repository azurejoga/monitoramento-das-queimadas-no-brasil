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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f9da147-889d-3bf0-9bd5-a5cc8398650a | -6.32208 | -43.36118 | 2025-01-29 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fea87b4-211b-3cb0-89e2-a7139fe9eaec | -7.95367 | -49.75556 | 2025-01-29 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44231cf3-eeae-3dbf-9280-be3ce2d08c74 | -6.9413 | -43.5331 | 2025-01-29 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 91962d1f-a78f-3435-923f-7f7db8e3864a | -6.49687 | -47.493 | 2025-01-29 04:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 259505bf-fb5e-3ee6-8700-a293c85c50c9 | -8.15514 | -49.13657 | 2025-01-29 04:40:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20722076-c2e8-37b9-b1bb-a235aa7df5d3 | -6.50904 | -47.59945 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f701ffa-bf9b-3c22-aff7-d671cea8bace | -10.21226 | -59.40707 | 2025-01-29 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c5a33c7-39e4-348a-85b8-d10a529efaef | -6.93753 | -43.52821 | 2025-01-29 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1f338f14-cc66-3f7a-8f83-647d68d8af6d | -5.83152 | -48.08173 | 2025-01-29 04:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe4501ab-b8c6-3a69-bcb7-6310a3fa74fb | -9.98633 | -48.07746 | 2025-01-29 04:40:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc917aa3-3db6-31aa-b15a-3d23ffb1a85f | -7.95312 | -49.75905 | 2025-01-29 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a370f436-bc6c-3369-97bb-3f0da486a783 | -6.63674 | -47.85957 | 2025-01-29 04:40:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 178451a5-0f75-363f-8f0b-f609764655cc | -10.21438 | -52.85531 | 2025-01-29 04:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 396a66de-5b51-3300-b375-9eeeea65a9b9 | -5.46793 | -42.92391 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3e5ca439-b1aa-3309-9268-ec2cf8c733e1 | -9.20096 | -49.47702 | 2025-01-29 04:40:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 622cecae-8a7e-3399-9660-22cc2a90465c | -8.84225 | -49.90679 | 2025-01-29 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1be4e317-4891-3bc9-9133-a42ddf19401c | -7.95203 | -49.76601 | 2025-01-29 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6198561a-0bd9-3615-911b-ef8b7d999a56 | -6.50554 | -47.48255 | 2025-01-29 04:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5973e6a4-47c4-3c19-8ae4-76d3c6f04c7b | -6.94191 | -43.5289 | 2025-01-29 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 99956e06-7181-36f8-87cb-85615effbd52 | -9.26243 | -60.3162 | 2025-01-29 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67787864-697d-36a3-bbff-5647a31df7cf | -5.4608 | -42.92382 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49f1670b-3373-38ae-8136-21e216f361da | -9.25681 | -60.31506 | 2025-01-29 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b266d8fc-81de-34d3-8ba3-60cccd16a062 | -11.39243 | -52.93828 | 2025-01-29 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5302cdb-bb4c-3f53-8f90-419a1419b5bd | -7.9487 | -49.76549 | 2025-01-29 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2001785-12d5-32f9-a6fb-2910505d0666 | -6.94568 | -43.53376 | 2025-01-29 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 26e9ecc0-da75-356e-908b-2c144301ff80 | -5.47304 | -42.92012 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0d091e8-0084-345d-8619-0237e5d96b47 | -6.66176 | -47.60659 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93fb46ce-c35e-3bdd-99a5-fdc00bf56a6d | -11.36314 | -53.93452 | 2025-01-29 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dfac70d-4a3f-3136-8f1d-0b1777fc47ba | -5.46346 | -42.92321 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 037b4f22-07bf-3870-987d-b68484784fcf | -10.68857 | -54.3533 | 2025-01-29 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c448c70-a201-33d1-86de-351f6eb58908 | -10.21373 | -52.85918 | 2025-01-29 04:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76a39573-3c00-36b4-9cf6-e1b847143d84 | -6.49962 | -47.48634 | 2025-01-29 04:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd05b4a2-8ddc-3f67-9f3e-a438647715df | -5.75165 | -43.40474 | 2025-01-29 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7726ca2-d753-315a-9a7a-c3c52c92bb0c | -8.32774 | -49.3736 | 2025-01-29 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 268aff6f-f9c4-3317-8859-0eca4501442d | -6.6583 | -47.60604 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecbe9f03-b47e-3ecf-88b6-30f27ac91c2f | -6.32646 | -43.36192 | 2025-01-29 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 651b18a7-3fc3-3a4f-b390-f16ab86743ac | -4.12825 | -54.89823 | 2025-01-29 04:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 048497b5-5def-3048-9acd-e93fb1d7a48e | -6.93692 | -43.53244 | 2025-01-29 04:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| babef153-c867-3271-baf7-3fe188b3669c | -11.80283 | -49.32244 | 2025-01-29 04:40:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfa3d1d8-84af-3eb2-869d-f2ca799c4959 | -11.38896 | -52.93769 | 2025-01-29 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7181ef6c-33a0-3982-ad77-437d3640f458 | -11.86306 | -46.94743 | 2025-01-29 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a75d6f6-7d9a-3cb2-886a-4e49e54432b3 | -6.64017 | -47.86008 | 2025-01-29 04:40:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2401f8f2-2b63-3c7c-8b2b-1519f91c8741 | -3.88398 | -54.21848 | 2025-01-29 04:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76805910-1b4e-338b-95bf-6a88fda0d3d7 | -8.71573 | -44.00417 | 2025-01-29 04:40:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 108b28bf-d9fe-3731-bd7f-4d85ac46b33e | -5.46409 | -42.91879 | 2025-01-29 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b133921c-9374-33f8-ab0e-a91c8b2afeb0 | -6.51249 | -47.60001 | 2025-01-29 04:40:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b547814-39b9-3525-bd80-03e078053014 | -6.63731 | -47.85586 | 2025-01-29 04:40:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dffea43e-f7e9-3e56-8292-91fcef771fd7 | -11.25878 | -60.7924 | 2025-01-29 04:42:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95231142-4083-3514-9f66-78406931e865 | -15.80281 | -58.51793 | 2025-01-29 04:42:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dd4d2d3b-4437-36f2-8a40-354664146423 | -12.90254 | -45.07262 | 2025-01-29 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69e27498-f47d-31ac-ab97-824abc3092e4 | -12.90042 | -45.05545 | 2025-01-29 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aecd0d6f-9461-3e08-98c7-70fdd352f716 | -14.31821 | -57.60844 | 2025-01-29 04:42:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c2abb16-2719-3259-9e55-e28f26d4e213 | -15.74687 | -59.85329 | 2025-01-29 04:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f40f9708-cf6d-36f4-a8f6-ad759f02d620 | -14.32174 | -57.61354 | 2025-01-29 04:42:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb6675b1-49bc-3637-bf3b-464cb4eecc90 | -12.89987 | -45.05959 | 2025-01-29 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e5b5021-bc7d-3282-b507-575a95695332 | -12.09821 | -51.22146 | 2025-01-29 04:42:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb401ee-a2af-336e-a4ea-5fe20ba485d6 | -11.25803 | -60.79622 | 2025-01-29 04:42:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd0caa8f-a7fd-39e6-85d4-25b70e70f5e8 | -16.28109 | -56.7873 | 2025-01-29 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e901155b-9e65-3666-a87b-d32fe7e920af | -13.41054 | -41.34325 | 2025-01-29 04:42:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d3779af-cf8b-3e8b-baa2-4e3310f20513 | -13.66605 | -50.6311 | 2025-01-29 04:42:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9f16a13-1634-3301-b692-bcea3676b316 | -16.23939 | -60.13564 | 2025-01-29 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da0cd96f-f661-31f2-8dea-a4dad9a0f221 | -15.08005 | -48.94419 | 2025-01-29 04:42:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c002bcd-3e54-3032-80e8-9c3efc31f2e4 | -12.90309 | -45.06849 | 2025-01-29 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74331f9f-a8a1-3da8-a679-fd7f43a40656 | -15.80724 | -58.51889 | 2025-01-29 04:42:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cab717cb-6e6a-358e-bbfa-bd7b4336d575 | -14.32252 | -57.60927 | 2025-01-29 04:42:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b8f7259-055a-3ab4-974f-56e64b78e7f8 | -15.80197 | -58.52246 | 2025-01-29 04:42:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f10a4be5-9096-3c9d-be63-94308805c0bb | -15.80406 | -58.5216 | 2025-01-29 04:42:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d1057d3e-8d57-3783-8d0a-fbf8f371db9f | -15.80493 | -58.51709 | 2025-01-29 04:42:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0a0a0e4c-3dad-30fe-b88d-8cf6068571a9 | -13.41095 | -41.33982 | 2025-01-29 04:42:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f602b46-c5c6-37b9-85ae-47fea3bd082c | -16.22142 | -58.60749 | 2025-01-29 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5550165f-0c3c-3ee4-b069-c2569c0c85c1 | -14.31744 | -57.61271 | 2025-01-29 04:42:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 596fd96b-4bd7-3781-abbe-d693594f5285 | -12.89878 | -45.06787 | 2025-01-29 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d93034cf-d4b6-33da-9ebe-f5eddbbc79fc | -22.32282 | -46.92505 | 2025-01-29 04:44:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d60e7088-783f-344e-a63b-cf755180871b | -20.90517 | -56.53646 | 2025-01-29 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ed712ad-b766-3670-ac99-5dd03382e7ef | -20.54512 | -55.84305 | 2025-01-29 04:44:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9854d62-a5e9-37b0-b0b7-90e95e3d1a0a | -21.07631 | -56.39439 | 2025-01-29 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fef29fa4-6a56-3724-9b5d-fa6197527a73 | -19.30216 | -48.38805 | 2025-01-29 04:44:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed20837b-e0ad-3b02-b45a-a882fc63dfaf | -20.90883 | -56.53715 | 2025-01-29 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b57eddfd-407b-3be0-8058-1038d9d9fea6 | -20.70044 | -55.42925 | 2025-01-29 04:44:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fba941c-e6a0-3f07-bb3a-c43ab9284829 | -19.80197 | -53.79389 | 2025-01-29 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52242a65-9378-36f7-83fb-0b9f298d7fa1 | -20.70114 | -55.42515 | 2025-01-29 04:44:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee594ac6-4be8-3518-a4d1-03ffd25dd184 | -19.79861 | -53.7933 | 2025-01-29 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64cd60b6-35a9-33de-bbff-29c6f9e3192a | -24.24379 | -50.73889 | 2025-01-29 04:44:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c67f2a99-0760-32a8-91fd-7a1cdcad4800 | -29.51124 | -51.72575 | 2025-01-29 04:46:00 | NPP-375D | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d4055ed1-cdab-30f8-9067-5e2e8ec151fc | -27.08399 | -50.51117 | 2025-01-29 04:46:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9b5a92c-a6bd-3400-b7e2-db0938663ee8 | -29.51489 | -51.72627 | 2025-01-29 04:46:00 | NPP-375D | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4e246dcc-c21f-3d38-844c-83913dd1c33b | -29.51064 | -51.73043 | 2025-01-29 04:46:00 | NPP-375D | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7293d23e-edbe-32e6-81c5-45822679cbd9 | 3.89215 | -60.17172 | 2025-01-29 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| feb76011-4c20-3f78-a9d9-d500a0f196d3 | 4.67443 | -60.82684 | 2025-01-29 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f284946-e0fa-3219-905c-1795bdb957b3 | -0.82461 | -47.58825 | 2025-01-29 04:59:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6161fe5c-988e-3631-9c83-de1f0ddd8647 | -0.82579 | -47.58618 | 2025-01-29 04:59:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74ce679b-0fea-3189-9024-5c7c246c6a10 | 4.67455 | -60.8254 | 2025-01-29 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1372bd6-4b15-380b-ad9f-e954b283bf39 | -0.82776 | -47.45388 | 2025-01-29 04:59:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 504d6893-ff6f-3365-97f7-0e0167621730 | -9.55409 | -38.28465 | 2025-01-29 05:01:00 | AQUA_M-M | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 040e3781-0aa9-3dc3-9b85-8b7aa164ee57 | -2.90753 | -54.28611 | 2025-01-29 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c592b40-0f1c-39ad-b88f-9d009ddeb7d3 | -6.93703 | -43.52239 | 2025-01-29 05:01:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ebacf54b-690f-3d44-bf90-33b2ebc8b884 | -3.16684 | -54.77641 | 2025-01-29 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c1c91b47-f0c5-3c38-a7fd-241cc7cc63e6 | -3.72078 | -53.75362 | 2025-01-29 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c7ff34a-0fe5-3fd9-b5c8-0487caa39a5d | -6.50559 | -47.48447 | 2025-01-29 05:01:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cb126ff-9312-3cbd-87c0-4d144b584b55 | -3.71959 | -53.69447 | 2025-01-29 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
