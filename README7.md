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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee09aca6-b523-335f-8519-c6f49c02d401 | -11.20642 | -54.03225 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 661a3c4a-4706-3e63-8d15-c1dec5d68af6 | -14.22597 | -48.51053 | 2026-08-10 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 254f2f9c-3f89-308c-b5d1-98068026042d | -11.21296 | -54.03379 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d390e693-cb67-3f64-bf70-7b1434a8b04d | -11.21813 | -54.03163 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dcf60db-3734-3d5b-80b4-6ffd300b9281 | -8.30777 | -46.41734 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b244aa3-ea41-3ecf-b211-5b6abdbeeaae | -12.10229 | -47.2021 | 2026-08-10 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b4da9cd-9868-3852-bea8-bd2a7bd130e5 | -15.04819 | -46.56844 | 2026-08-10 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a651d060-5617-3604-8641-dc9fdae01834 | -13.48455 | -40.30909 | 2026-08-10 04:08:00 | NOAA-20 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8e783eaf-0006-319c-96ff-593eccfbd099 | -13.63737 | -46.22884 | 2026-08-10 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f40265c4-6c1a-3408-b4df-09627e42d8ff | -13.85749 | -43.64857 | 2026-08-10 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e774927b-869e-3600-8fb8-5597ddd2568d | -13.64126 | -46.22931 | 2026-08-10 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8aad8c17-8a0c-37e0-b8c0-28c428c773c8 | -11.04035 | -49.77375 | 2026-08-10 04:08:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca5fc7ff-67f5-3b5d-8f0f-2561d2a6c40a | -9.62703 | -48.32601 | 2026-08-10 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 32981d7c-1f0c-3e4f-ad2e-ccdd33fc792d | -11.2116 | -54.03 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd1f16fb-cfdd-3876-92ca-95e68702bc3b | -15.04198 | -46.56871 | 2026-08-10 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27176663-fcae-3b84-bfbd-13ef205426f2 | -13.48118 | -40.30854 | 2026-08-10 04:08:00 | NOAA-20 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 68c7e626-e36a-3037-ad6a-d7945ec87acc | -13.86152 | -43.6454 | 2026-08-10 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed55c67b-cffe-3a53-89fb-9e6db6a1c4c2 | -9.63013 | -48.32971 | 2026-08-10 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0d3a9a6-9d41-3a9f-9fd3-0603877a67ac | -13.84121 | -53.89717 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75756d05-bf60-3f4b-8a99-9b1a79d4f76f | -8.31404 | -46.4062 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ee22e5a-186c-3001-9e90-44539de9599f | -11.04092 | -49.77072 | 2026-08-10 04:08:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8748134-4abf-35eb-9bce-0676e6b537b1 | -12.10239 | -47.19847 | 2026-08-10 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c9c2e15-abdf-3e28-9920-f660e321c00e | -13.84704 | -53.69524 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be34e4a8-bfd6-39b2-96df-eca060b3ec4b | -12.05105 | -45.5654 | 2026-08-10 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3185cb5d-c887-33d4-961e-4d39a4a44b33 | -15.0505 | -46.56553 | 2026-08-10 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5afac69e-1c06-3aea-93c1-5ad808a7a53d | -11.21179 | -54.0396 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b89a82d-929b-30b4-812e-380c9aca8ede | -13.8675 | -53.6587 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 428fcd46-136b-37d0-bbee-09aecc6a1e01 | -11.041 | -44.28573 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9008379c-af8b-3ef4-85b3-fe1236f847bf | -11.21949 | -54.03541 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a61f0f04-848d-3392-8ec9-60f8937b57ee | -8.58997 | -45.39569 | 2026-08-10 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25809345-9db5-3e11-a129-440562379d76 | -8.29925 | -46.41606 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5810c76a-9c46-36d7-a367-bebb268c2103 | -11.4717 | -50.55898 | 2026-08-10 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e475323-600d-35e5-9239-94586d653c46 | -12.04726 | -45.5647 | 2026-08-10 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25af1e27-0e6a-31bb-9b7e-e1dcef393a24 | -15.33247 | -42.90687 | 2026-08-10 04:08:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b1985ac-4e28-371c-b64c-5e0b32f71e19 | -11.26374 | -44.85415 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7be9327-c897-31e8-be72-8bd5db42ab60 | -11.62075 | -51.0961 | 2026-08-10 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 421af494-a85e-3586-9ac8-67f1e0673eaa | -10.24821 | -45.91408 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eda03acc-2410-340a-b71a-9c9da5157cc5 | -8.29499 | -46.41544 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaadabc7-cfc5-3ad6-b670-1c410c47ce33 | -15.04669 | -46.56463 | 2026-08-10 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a3fceab-e1de-30c2-9836-43fe8dbdafda | -10.47976 | -46.62126 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 740c4334-1177-373a-a6df-8bd9f991d867 | -11.03741 | -44.28511 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e55fb2db-0150-3c9f-bd46-a6a64f993566 | -15.04351 | -46.57249 | 2026-08-10 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed22957a-ff4d-3211-a3ce-fbbd9cecd341 | -8.32225 | -46.38362 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e90f2a1-6f72-382f-ba95-cac963293f3f | -12.35736 | -53.16166 | 2026-08-10 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38c99997-9d13-34f1-a9b8-955fb55388ea | -13.84593 | -53.70056 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01728bcd-1caa-3f86-af70-f79d8becf21b | -11.62146 | -51.09249 | 2026-08-10 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fe041b7d-49da-3aee-b246-fd4997ccddf7 | -8.9039 | -60.5769 | 2026-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 082accf8-f091-383b-a10b-6cee66dcd3c2 | -8.9598 | -60.555 | 2026-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1257da3d-6a05-3e45-84ec-58dd02b3a784 | -17.71642 | -54.18974 | 2026-08-10 04:10:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87745471-1fa7-3db5-84f0-d2812f621aa3 | -20.51951 | -42.30739 | 2026-08-10 04:10:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7fd80f9b-28b2-3612-998e-fc16199ae6da | -20.50146 | -43.64264 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f79fb7a7-e444-3914-bc42-3af04f7699d0 | -20.52285 | -42.30798 | 2026-08-10 04:10:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 036ca5f9-c3a4-3beb-9572-3332ba88d74d | -19.82527 | -43.30318 | 2026-08-10 04:10:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36613eaa-2266-3b53-af9f-6c81551cb2dc | -18.04345 | -44.36633 | 2026-08-10 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 333bcc98-2873-3747-b8c3-e3ce44b18326 | -14.14061 | -54.0124 | 2026-08-10 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| adda6011-ecaf-3d33-bcc3-6473e209b656 | -20.50574 | -43.6585 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e2f7c2c8-6f41-3164-b9ab-d94da28f8f28 | -18.61813 | -49.19125 | 2026-08-10 04:10:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a741be0-7db3-344d-a76b-da28bb8cfe73 | -20.54779 | -41.25094 | 2026-08-10 04:10:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 57611aab-ac1f-36f9-9ca4-93be788257ea | -16.76649 | -49.46686 | 2026-08-10 04:10:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da4011cd-8fec-399a-9019-7e363436ea5b | -21.11078 | -44.2298 | 2026-08-10 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 30bb0dfe-e4b4-3002-8ad4-487a1c7304d6 | -20.49932 | -43.63472 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 90fd2acd-7d60-3290-891b-0d7950cdf893 | -15.75996 | -47.76886 | 2026-08-10 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca333b71-ddb0-346b-b94e-c7d4fc51ca41 | -19.82915 | -43.3001 | 2026-08-10 04:10:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 31855cdb-db19-36ff-99d3-fdc664105d76 | -16.7152 | -46.4024 | 2026-08-10 04:10:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83dce975-d11d-3f35-adeb-528515a726fa | -16.77097 | -49.46775 | 2026-08-10 04:10:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc520d84-a474-313e-b9f9-4df85398f6bc | -18.81592 | -49.64426 | 2026-08-10 04:10:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 8d375df4-c963-387c-ac74-bde5c0d1301b | -21.47995 | -41.24676 | 2026-08-10 04:10:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c0c1bed4-575b-3c16-9e42-7838edf8ac52 | -16.09894 | -47.99294 | 2026-08-10 04:10:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50280bbc-1334-3229-949b-0fea2c657d93 | -22.22417 | -43.02465 | 2026-08-10 04:10:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d36db8a2-edd0-3c5f-b73c-e1631d32b493 | -18.04222 | -44.36633 | 2026-08-10 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9757256-9abf-35ee-bf1e-1ef5adfff128 | -20.50594 | -43.6359 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2c614fb0-8a91-35ec-a9f9-d62f58d0e87e | -19.49912 | -42.61235 | 2026-08-10 04:10:00 | NOAA-20 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4595f353-55b7-3449-a8b5-c63be0a52c2f | -19.50244 | -42.61292 | 2026-08-10 04:10:00 | NOAA-20 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| cc2cb852-fcb6-3fc8-96c0-89e06c8ab07d | -20.37265 | -42.90729 | 2026-08-10 04:10:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8cdcaf1b-7dca-37c4-8364-e7c8560f0bf3 | -20.49874 | -43.63839 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d2c15272-1588-34f8-acbc-3fe456c2ce8e | -15.0729 | -50.38023 | 2026-08-10 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 067f5687-3340-3cfb-b0b8-e955d3ed49df | -14.30552 | -54.93331 | 2026-08-10 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92f74375-b1eb-3a4c-bc4f-12767f4f7ff2 | -17.83151 | -41.96275 | 2026-08-10 04:10:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| db6d70f1-c6f3-34e6-af01-e69db52c0914 | -17.87764 | -44.43028 | 2026-08-10 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c93a1a49-23b5-34ed-aeb1-a33c6098f68c | -16.71792 | -46.40141 | 2026-08-10 04:10:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 129b98fd-a005-3ce5-9dd4-4857de5e5a84 | -20.36819 | -42.91407 | 2026-08-10 04:10:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5eed9571-b858-3aa1-baa3-090482006511 | -21.67793 | -41.86073 | 2026-08-10 04:10:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3ba2a3e8-62f9-35d0-ae41-6a7633797299 | -20.36877 | -42.91039 | 2026-08-10 04:10:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 57349bd3-b19f-369a-8d6b-d787423af9b8 | -22.20085 | -42.34501 | 2026-08-10 04:10:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1d7e7b85-5911-3188-8a85-696e38ed917e | -20.72378 | -45.36638 | 2026-08-10 04:10:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fc948fe-358f-36dd-8836-1115e009cc6b | -16.33135 | -46.89052 | 2026-08-10 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5cb6174c-5116-3491-b7fb-02c9fef81f6e | -19.90765 | -44.49313 | 2026-08-10 04:10:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9f0a561b-f98e-3799-a66f-498da24b108b | -20.42816 | -41.58856 | 2026-08-10 04:10:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a06ea025-b5cc-31c1-aaac-55b97eea736e | -20.04886 | -43.77448 | 2026-08-10 04:10:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a4a3185-f613-395b-8c24-d86ce54f6084 | -18.02534 | -44.36338 | 2026-08-10 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad4d8d89-2d80-3eb5-abf1-f00e77567c99 | -21.41417 | -43.88424 | 2026-08-10 04:10:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 25990231-fa28-3233-a93b-27e8f31b680b | -19.82196 | -43.30259 | 2026-08-10 04:10:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a345a47c-0dc0-396b-9aa8-df1a0f702fa8 | -17.71054 | -54.18822 | 2026-08-10 04:10:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 681975f5-187b-39ac-9b97-8322858c4d8c | -15.08245 | -52.69003 | 2026-08-10 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0d82f5d-23ec-3e89-9e36-244ac1382f7f | -21.29284 | -41.74653 | 2026-08-10 04:10:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1a15ea8-05ff-3ba1-833b-390435dec3c1 | -18.03946 | -44.36204 | 2026-08-10 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31898deb-3268-3a5a-bdbe-ce561569c0eb | -20.43275 | -42.84962 | 2026-08-10 04:10:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e28f6fbe-4a14-3b9b-ab10-f134afe70d42 | -22.27676 | -48.73822 | 2026-08-10 04:10:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 6b9c51eb-ec07-36fa-8a58-6829c1620e8a | -18.8088 | -42.16084 | 2026-08-10 04:10:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a617fc7e-02d3-3b98-8643-e917c6309903 | -19.44815 | -40.39428 | 2026-08-10 04:10:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
