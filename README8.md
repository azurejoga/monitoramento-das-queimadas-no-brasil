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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 443f5800-13af-3a7d-8f1b-571027de2389 | -12.88781 | -48.37357 | 2025-11-21 04:16:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26419c85-698b-36b1-906f-43c14ba8a970 | -12.55136 | -54.80851 | 2025-11-21 04:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad39932a-116f-38bb-a7e5-6c7951538907 | -17.82541 | -46.99213 | 2025-11-21 04:16:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83becb03-84ba-310f-8e32-ae00fb202fcc | -18.75947 | -45.285 | 2025-11-21 04:16:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 51800ab1-ec94-3d0a-8241-d94ee1675f15 | -13.70574 | -48.42405 | 2025-11-21 04:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1b6de99-9e7d-30b5-82ea-d07ba7bd4e12 | -13.7373 | -48.45481 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95a759bd-3c07-39e2-b242-51fff1a47a9d | -15.28829 | -53.04316 | 2025-11-21 04:16:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd184ba8-2969-3749-ae37-ececf615338d | -17.80899 | -44.30814 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7997728-8947-3a83-abbd-bb0d38532c25 | -17.07042 | -46.60029 | 2025-11-21 04:16:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e1057be-9e9f-317d-8159-4e0ab9098463 | -14.52701 | -49.34294 | 2025-11-21 04:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76a0f85c-dcc8-39c4-a9c9-0b43125287e2 | -14.04283 | -47.56597 | 2025-11-21 04:16:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae0ed293-3c85-3b04-bf7c-975d315056fd | -15.23701 | -50.2108 | 2025-11-21 04:16:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd6d4815-01e3-3378-af4e-38d05157f033 | -14.8484 | -53.67077 | 2025-11-21 04:16:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 427cd479-f5f2-3335-8b92-933de8a6a8c4 | -11.27334 | -53.96392 | 2025-11-21 04:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 544cce0d-1a17-36e1-84f5-c716aaf148f2 | -13.09445 | -49.05987 | 2025-11-21 04:16:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcaab504-fd07-3284-a45e-0b7c7cc8d951 | -13.705 | -48.4284 | 2025-11-21 04:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9752a76-1e30-39e0-bcb1-dcbff1835423 | -13.70424 | -48.43289 | 2025-11-21 04:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cda88b27-926a-3d71-9d85-38eeb0b27756 | -18.27445 | -42.37702 | 2025-11-21 04:16:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 240e3dcd-8c57-3ddd-97a4-6287a349637d | -17.61335 | -52.99809 | 2025-11-21 04:16:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6c6b533-14a5-35b7-a0fa-1c8e43825d6b | -13.78462 | -49.57877 | 2025-11-21 04:16:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 116e925b-56f5-35ca-bb1f-cd629cdc082b | -18.76279 | -45.28557 | 2025-11-21 04:16:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b187d715-f214-3dbf-9560-266b9445db79 | -12.86909 | -54.74398 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6cf4f03-d1d3-394a-83be-e502d3d74468 | -14.52402 | -49.3375 | 2025-11-21 04:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c117f58e-7bfa-3e8b-a0e7-23b855afeeb0 | -18.23977 | -44.16463 | 2025-11-21 04:16:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6220f1ca-5b84-3c14-8d35-cec7818a5b78 | -16.41473 | -43.12658 | 2025-11-21 04:16:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2c25f93-ae9f-3b7c-9309-40f35f74d303 | -14.77877 | -53.17652 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8322758-8d18-31f4-a0f4-4b5302e8d540 | -12.54362 | -54.80357 | 2025-11-21 04:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ec2c7bc-5ca3-3414-8112-00745aff9d69 | -14.40052 | -48.26557 | 2025-11-21 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dafbbab6-f037-33c3-9667-a448cc975d79 | -16.43374 | -51.64822 | 2025-11-21 04:16:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0af4e23-9cd1-3b67-a130-5ed2128fadfa | -17.43004 | -49.08161 | 2025-11-21 04:16:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9227ab7a-3c94-337f-a39a-49c2786f1b40 | -14.40172 | -48.26404 | 2025-11-21 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc61f600-e46a-3094-8824-c7dc8de53281 | -16.41127 | -43.12603 | 2025-11-21 04:16:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c31ccb01-826a-3bce-b1ad-cde4274d3630 | -14.52021 | -49.33677 | 2025-11-21 04:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17f7a37d-991c-3482-9d2a-ec9d1b92e3e9 | -16.63351 | -51.30498 | 2025-11-21 04:16:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e2b5142-a3af-3cda-b50b-cfe5370c68c2 | -13.73442 | -48.44958 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6523809-54aa-34c8-9a7d-decd932a4fd8 | -16.51685 | -43.54325 | 2025-11-21 04:16:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14ced872-203a-3de2-b50a-6758ae911a2d | -13.73808 | -48.45032 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51996b98-ed6a-34cf-b925-3c61e10c77b1 | -12.86505 | -54.74286 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13412770-8deb-33bc-a3b2-ac8f2e83921a | -17.83484 | -46.99757 | 2025-11-21 04:16:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ad8cdb7-5e84-3e3a-8c1c-537d53f0120f | -19.45 | -43.08005 | 2025-11-21 04:16:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 92131b88-457c-3242-aec3-58f5a5d16952 | -17.56449 | -48.00972 | 2025-11-21 04:16:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4b4935c-e89e-325f-b8f9-644c98c7d141 | -16.63142 | -43.47853 | 2025-11-21 04:16:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8dbbe4a-1b93-3c49-aef9-ab9d58033f60 | -19.4059 | -40.53671 | 2025-11-21 04:16:00 | NOAA-20 | MARILÂNDIA | ESPÍRITO SANTO | Brasil | 3203353 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d0f48cdd-e63e-3949-8d3e-00e245740923 | -13.90461 | -48.76539 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cff41f87-9705-3527-8c86-bdbf5dcffa7d | -12.87137 | -54.74009 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76db4496-6d9f-3212-8677-2638b6952806 | -16.29675 | -46.59002 | 2025-11-21 04:16:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f508e6b-d68a-3e00-9124-ace0fe052d33 | -17.50918 | -44.7869 | 2025-11-21 04:16:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a6ecde8-1fd8-3429-8f15-c791549bf32c | -15.53006 | -55.76916 | 2025-11-21 04:16:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d76998b3-8717-3ce5-be4f-d3af67001844 | -13.70057 | -48.43222 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a4c956-14bd-3b2f-bf3d-2bb6bf903495 | -14.51556 | -49.34083 | 2025-11-21 04:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc89a97d-5a7e-370f-9232-c26b5770d081 | -14.40534 | -48.26459 | 2025-11-21 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04136ec7-0a85-3a71-9646-a0e504e5e8e9 | -15.40334 | -48.93776 | 2025-11-21 04:16:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af9d5a7f-a5a2-3934-bd3d-580dda9d8def | -18.23636 | -44.1641 | 2025-11-21 04:16:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d68615bb-57cd-30dc-8ee9-f4e547083e5f | -12.87465 | -54.74507 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e2bdf45-88ad-3db5-93da-41f3f6ead04f | -14.41258 | -48.26578 | 2025-11-21 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ebd683-21d2-3f58-99d3-bfceb9e847fa | -13.70864 | -48.42925 | 2025-11-21 04:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d0963e9-6dcb-311c-859c-d464d22dd463 | -15.42098 | -48.06391 | 2025-11-21 04:16:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1e28242-132f-3f45-86d9-d86ff4d79b5f | -15.28936 | -53.03772 | 2025-11-21 04:16:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 932d6b0e-fed1-30a4-8d82-9eee25921f62 | -17.81181 | -44.3124 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bd911f8-6d04-395f-bbea-d685edcab631 | -17.64813 | -43.88556 | 2025-11-21 04:16:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a9b7f0f-b672-342f-b1d8-52d9f7df9bbf | -14.77394 | -53.17544 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| daa2d42c-d3fb-3c2b-b204-20ec228df659 | -19.4494 | -43.08424 | 2025-11-21 04:16:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8cb1f44e-8ad3-3d6a-9131-ac4f708efd22 | -16.42576 | -52.04731 | 2025-11-21 04:16:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a71f0552-116c-3af9-860e-be04e7c6de5b | -14.84781 | -53.67374 | 2025-11-21 04:16:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a1f8be2-6359-3ebf-bbf0-698c2a02b041 | -14.40896 | -48.26517 | 2025-11-21 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 433f0a41-7f10-3843-b237-0a93e891b9a8 | -15.23764 | -50.20726 | 2025-11-21 04:16:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 044bd1d2-33d1-3d42-9ced-e5b0fef27816 | -17.07375 | -46.60088 | 2025-11-21 04:16:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82bc624a-e933-3735-8e5e-59f77df478d9 | -16.73277 | -47.83948 | 2025-11-21 04:16:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73f8180e-076b-31e8-b3f7-5095e062744d | -17.80844 | -44.31185 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62d3b490-6d57-3738-8fe6-deb6059959cb | -17.57787 | -46.67673 | 2025-11-21 04:16:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b6df433-550c-3da3-a6e1-dbf2fc58bcfb | -17.41015 | -46.68122 | 2025-11-21 04:16:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf6e9596-ba2b-3cd1-b2d4-a2029852d768 | -17.39734 | -44.47893 | 2025-11-21 04:16:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed0fec10-ecc5-3f90-bb55-53227e21ed14 | -17.81293 | -44.35085 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9d0fa99-311e-3769-bd94-f71f330d965e | -14.97845 | -52.98442 | 2025-11-21 04:16:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45772dc2-085d-3ea7-862b-6e43d5ee05c8 | -14.77274 | -53.00026 | 2025-11-21 04:16:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 277c876e-b7af-3dd8-be50-bf71d72f9acf | -12.86753 | -54.75169 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dc3c2b8-8e2b-3982-8db1-c915e1e58df5 | -17.8135 | -44.3471 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e32ef4b5-4b65-3272-80c0-a413154e55f3 | -17.64415 | -43.88884 | 2025-11-21 04:16:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df689571-b0db-3c57-9116-ab9132154964 | -17.61789 | -52.99903 | 2025-11-21 04:16:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61c478b5-d522-33bf-9e5b-529e50e2ef7e | -12.54921 | -54.80484 | 2025-11-21 04:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1b62eb3-e9e0-302e-a0c4-2fae107e3152 | -14.84283 | -53.67259 | 2025-11-21 04:16:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb71bec3-1782-3ed3-8daa-4277f60c6c39 | -16.38775 | -44.06026 | 2025-11-21 04:16:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af39b49d-8f82-37fa-9b94-fe65d93a3a08 | -17.1579 | -50.84928 | 2025-11-21 04:16:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 827b1ba7-992e-3dd8-a8d2-c38d7e5bdea8 | -13.80666 | -50.64254 | 2025-11-21 04:16:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a5a5a20-a9bd-3f8c-bd50-d0f41dd60f8c | -17.5812 | -46.67731 | 2025-11-21 04:16:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8884aea9-d3db-37fd-9288-c5b397478631 | -12.8731 | -54.75276 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34ae6c07-953c-35ac-9ec1-11cb9c4eb4c4 | -17.72099 | -48.0776 | 2025-11-21 04:16:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d24b55d3-da23-3d7d-ba12-8c226211b2be | -14.84399 | -53.66676 | 2025-11-21 04:16:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4eaece19-0ad1-35db-b52a-0c4acc1e4519 | -17.95356 | -45.9874 | 2025-11-21 04:16:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56d15787-222b-3286-a963-74665c70ac76 | -12.86986 | -54.74784 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39fb8a05-2a7c-3b91-9b24-c04355db882a | -17.23779 | -48.11638 | 2025-11-21 04:16:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8de79381-98af-31d2-bd40-3ca9e900592d | -18.52464 | -44.6207 | 2025-11-21 04:16:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c69256-10df-30b6-be1f-a0f9dc616218 | -17.8163 | -44.35141 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9a72dc9-ddf8-39de-818b-d09fd953bde3 | -15.326 | -52.21071 | 2025-11-21 04:16:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dcf86934-97c0-3ce5-8c91-90dea8418009 | -17.80507 | -44.31131 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03ad46f9-4cff-3a98-9aed-819ac341e229 | -19.16254 | -45.33288 | 2025-11-21 04:16:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 397e598b-30e7-35c4-9284-b1e628e91837 | -12.55479 | -54.80611 | 2025-11-21 04:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6309c50f-ba8a-36a1-9e2d-e8ab755447fd | -13.73206 | -48.4631 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82e9463c-e001-3809-bb10-8c9839e52904 | -13.78853 | -49.57949 | 2025-11-21 04:16:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 213adca4-8f73-3fa9-8143-f2b96698dbed | -18.7023 | -48.03269 | 2025-11-21 04:16:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README9.md)
