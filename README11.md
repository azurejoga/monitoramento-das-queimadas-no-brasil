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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 679fbcdd-87f6-327f-aaaf-40902317f46e | -9.36954 | -48.41715 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58792cf3-8b73-3e51-9eed-a4475e142d70 | -11.88719 | -55.1342 | 2026-06-16 04:38:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43bdc2d8-0fd4-3b3c-b4c7-415d3abcb2a6 | -11.16688 | -49.25229 | 2026-06-16 04:38:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f7e79f3-64ef-337c-8b92-4e2fb9491036 | -13.4939 | -56.57165 | 2026-06-16 04:38:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b200a34-b4b2-370d-8ec0-bb5acac34246 | -9.74341 | -47.8746 | 2026-06-16 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e894f0cf-769f-3702-a018-2939f7e1a5a8 | -9.34185 | -45.47457 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d32eba0-d564-30a9-89da-9f777b39fd36 | -11.54491 | -52.78203 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 134188f4-9f20-3630-8987-97dfcbeb7e91 | -11.5463 | -52.79611 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 433822f9-540c-31a9-acc2-8337a2671a70 | -11.27491 | -44.52699 | 2026-06-16 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b06f4eba-0822-3bff-8a36-0dc8fee45d4c | -12.8471 | -44.37095 | 2026-06-16 04:38:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 444e4d74-b849-31fc-9251-3fffdff86924 | -11.48019 | -57.11676 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 314df519-46de-3f7d-a7a7-a79587410bf8 | -14.11291 | -59.45518 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfefa4cf-61f2-33d7-837b-75e3fe4f82e5 | -14.15389 | -41.95693 | 2026-06-16 04:38:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3d606ef7-092a-338e-8fb8-213cdfaaf072 | -12.68137 | -54.5818 | 2026-06-16 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e54260c1-2edc-3473-acaa-948d314c2b1d | -9.35815 | -46.48769 | 2026-06-16 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6467941-a6d6-31e4-ab72-7cbd23dd4667 | -9.40681 | -50.69743 | 2026-06-16 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84464dcb-09c4-3fdc-be6c-49e4cd744bdf | -13.56503 | -47.86744 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 487c637b-25c5-3b74-843d-4a88f76e7f51 | -10.82131 | -56.61029 | 2026-06-16 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63e502c3-1e2b-36a0-adc9-009a9aab8e9d | -12.1553 | -48.45223 | 2026-06-16 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 352477c8-1804-37f0-9262-7d43661b84c7 | -11.35407 | -51.38067 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 34525645-22df-3307-b577-14498276e907 | -12.59934 | -52.91408 | 2026-06-16 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 032b8c39-6e58-3949-882b-ae784b2df702 | -13.52034 | -54.30068 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 340fac14-2267-3b2e-9712-9b07eef93b03 | -10.87957 | -49.54031 | 2026-06-16 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c341160-9900-3acf-aec5-06fbc0fd10bd | -9.33405 | -45.47765 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bc57308-1a52-306d-b2b7-035705d7f5c4 | -10.49561 | -53.58097 | 2026-06-16 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29fb580f-059a-3aca-928d-7af030e259a1 | -9.22662 | -48.59113 | 2026-06-16 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cbd544a-438f-3c80-8829-7a87f68103b6 | -9.62788 | -49.01661 | 2026-06-16 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75b165b1-5846-3c3f-903b-1423ba98ccf7 | -14.85416 | -43.36919 | 2026-06-16 04:38:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3ff734ba-05b5-387a-9121-7fa6bc9b4255 | -14.09668 | -59.45171 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 461759d3-d66b-3519-bea8-8733b65a24bb | -11.35945 | -55.82196 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ad6d9ee3-1abf-3c3f-af8f-410d57144e2e | -10.81753 | -56.60413 | 2026-06-16 04:38:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1642bc5d-0849-3029-97c0-1f9217c1d628 | -14.11218 | -59.4588 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a85425c1-8854-3032-a67c-0bee082965c8 | -11.78857 | -57.0057 | 2026-06-16 04:38:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a3732a8-432c-3e1a-a1a0-21c6d0be4de9 | -8.98034 | -47.9765 | 2026-06-16 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46c97476-01a2-3212-8699-b4f40ede96f8 | -11.35754 | -51.38126 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c89a9a94-9dea-352e-8e73-cc69b47bba83 | -14.10748 | -59.45414 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ec93577-d81d-3d27-903d-a429bf75c707 | -9.22441 | -48.58364 | 2026-06-16 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cac0c505-e7eb-3a8a-8045-8c4faa56c510 | -10.54984 | -47.02691 | 2026-06-16 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0ad0822-a90d-3dc1-89cd-452fe15aaf7b | -10.36182 | -54.09867 | 2026-06-16 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47b27ba4-5150-3d69-9035-f22ea74d6f2c | -12.80278 | -54.86054 | 2026-06-16 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f9cd3c1-5179-3e3e-a91d-aac82f667460 | -11.53751 | -52.78078 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f56e81a8-b348-3790-a1b4-18d439bf416e | -13.5639 | -47.85196 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5699a48-9254-3edd-9947-ea44bf475a93 | -11.71898 | -54.49035 | 2026-06-16 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bcb3661-8484-31c4-afca-852922d01c3a | -11.25815 | -47.52005 | 2026-06-16 04:38:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e3cad3a-bf84-3880-9504-86c409c15eb0 | -10.71563 | -56.24712 | 2026-06-16 04:38:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7de69cbc-532c-3dbf-8a6e-6b2aa437585a | -11.20722 | -49.68084 | 2026-06-16 04:38:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d778acda-bcec-3737-9281-f5b54e29c56b | -10.71467 | -56.25236 | 2026-06-16 04:38:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2c0ab98d-378b-3d0e-9026-15d4a7a03020 | -10.25716 | -47.36163 | 2026-06-16 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61391f79-3359-3cd5-9860-447da5fdd8bc | -9.32265 | -45.4802 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37e14627-bb33-3cbf-994c-e5a1f8971e73 | -12.33425 | -50.00473 | 2026-06-16 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74fedc4f-075b-3619-87ee-ed7812d730c2 | -14.10601 | -59.46138 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90349dd0-afc2-33df-8daf-fb5a887b87d1 | -12.92585 | -54.22119 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dcc4747f-e077-3fab-87b2-6e1275539b5c | -14.09056 | -59.45406 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e39ce7d-08c1-379b-bb7b-b2e99dd493a5 | -13.81456 | -43.64892 | 2026-06-16 04:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d83de0da-77b4-3db2-98f8-258376982ab1 | -11.35495 | -55.82121 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fe160aba-e373-3aa5-ad9f-99da4ba59a65 | -13.5622 | -47.8632 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 216fda8b-0cb7-3823-ab05-b0c6d34cdc35 | -11.5953 | -55.33988 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6eb597e-5a99-3041-b99d-43e7cd68e5ef | -12.59568 | -52.91338 | 2026-06-16 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab784db0-eea1-3ffd-87c0-0c7c04cf0d6a | -12.71972 | -56.56654 | 2026-06-16 04:38:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa7c49f-d142-3814-be3b-71699c4b79b9 | -9.21232 | -47.3405 | 2026-06-16 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7010ab4-9b44-34ea-81e1-4d26e4b5e200 | -9.32624 | -45.48074 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb817088-2aa7-35e5-a267-326f3da227bb | -10.879 | -49.54383 | 2026-06-16 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac36daed-51f9-31d0-9abb-090449737ba2 | -10.58768 | -51.77489 | 2026-06-16 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 876da5ac-b015-3d33-b195-5754b6c159d1 | -12.15142 | -48.45525 | 2026-06-16 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 580170e2-8af6-3d9e-89cb-7c1a6223e301 | -9.33764 | -45.4782 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a9ba3c8-290d-32d0-bfd9-2cc0c0c6025c | -11.54198 | -52.77693 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0fe4537b-3457-3d15-8517-8fe1efcbafc6 | -11.54121 | -52.7814 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1f47711b-c7db-3fa6-b5cc-4c03ec460049 | -13.55091 | -47.84599 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bd16089-ebd5-3ab4-a176-431a3444be19 | -14.09986 | -59.46387 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bef63f0-89ae-37e3-9640-464d6a99d320 | -11.2735 | -44.5294 | 2026-06-16 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efcda0a3-e291-38bf-8d8b-57fe36b67ba0 | -9.34123 | -45.47874 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fdeb2cb8-ba07-3c07-b765-d3dea4b5dd42 | -9.34904 | -45.47565 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cde67853-ec38-347e-97e9-99aedebe61ec | -12.90917 | -54.22345 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c164b0f-07fc-31bb-9331-90ef007bcb6d | -13.49756 | -56.57721 | 2026-06-16 04:38:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 138aa9c8-0133-3cac-9135-6c99d88e9196 | -10.15296 | -56.60205 | 2026-06-16 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2e4328cf-5cfb-33c3-a957-df04c1b3f52e | -11.15674 | -48.26086 | 2026-06-16 04:38:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d3349e3-9c0b-3991-b3d4-0bd0e5969578 | -11.74095 | -54.78684 | 2026-06-16 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca012839-65ef-3800-8d9c-dfe48300415c | -10.89954 | -54.13198 | 2026-06-16 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 005cc1fa-6e9e-305b-9b0c-c4ec43d32fc5 | -10.71095 | -56.24629 | 2026-06-16 04:38:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba41bd4b-804c-33c9-af0f-e334672dc24e | -11.58591 | -55.34246 | 2026-06-16 04:38:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7431c415-38ea-3989-b0ce-c6bbfb3326f6 | -12.59857 | -52.91851 | 2026-06-16 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c1293aa-1b61-3133-8f26-684efa8c9068 | -8.97316 | -47.97894 | 2026-06-16 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a74438ae-970f-3788-ab77-67f29c281081 | -12.80141 | -54.86808 | 2026-06-16 04:38:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c784b353-543a-3ae0-95b5-d74a25f57f5b | -11.73611 | -54.78989 | 2026-06-16 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9cf2578-7bd6-3c54-9070-9ab15e5636fa | -12.15087 | -48.4588 | 2026-06-16 04:38:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48ac00b6-c246-32ca-abef-306721f80c1c | -9.45903 | -48.38897 | 2026-06-16 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9424f6a5-634a-3131-bcb9-333866ec109d | -9.62515 | -49.0126 | 2026-06-16 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 008b7879-ce00-379a-85df-65b839442c0d | -11.16751 | -45.37074 | 2026-06-16 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab6c824a-ee4c-34b3-a1f9-205077dbfa85 | -14.09595 | -59.45534 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd88d208-16ba-3e19-bfa2-b71e93ed648b | -9.33466 | -45.47349 | 2026-06-16 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86baa0ef-9256-3232-b462-a838b3b2602e | -13.54183 | -47.8601 | 2026-06-16 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d343adc0-cf67-36d6-8313-d00258fbab2e | -14.10822 | -59.45049 | 2026-06-16 04:38:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01fbc76d-d74c-3917-92fb-963708bde606 | -11.61895 | -55.18078 | 2026-06-16 04:38:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a93c244b-edb4-36ef-8668-854a265a3960 | -10.80368 | -54.17798 | 2026-06-16 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b07af5f-917e-3b41-8df7-44b81210a610 | -12.58833 | -54.16888 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7818500-3071-3e96-9703-80d69efe1559 | -11.11886 | -45.14064 | 2026-06-16 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed53f40e-3259-3479-ac82-07f08d5aeec0 | -11.54937 | -52.77821 | 2026-06-16 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 96bd51d3-ecf7-3188-bce2-df6cb503eced | -10.5487 | -47.03437 | 2026-06-16 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 95fc6141-c838-3263-be34-83ca3e454bec | -12.90523 | -54.22272 | 2026-06-16 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c36f420-b27b-34e7-8c1a-5855a2bb324c | -14.34012 | -56.84813 | 2026-06-16 04:38:00 | NOAA-20 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
