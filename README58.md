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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afd14621-843e-32e3-92a1-9a8181f0ee92 | -7.24463 | -43.37143 | 2026-09-29 05:10:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4e3e0237-2013-3d9e-8795-098539a347a0 | -6.67676 | -55.1091 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df02aced-85a0-3b18-8160-d3ec341fe876 | -6.31408 | -52.62916 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4697082d-8f50-378e-8d51-a85a230cd295 | -5.42967 | -43.45237 | 2026-09-29 05:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a681670-c6fe-347e-9f10-38d4d90be643 | -6.31453 | -43.61435 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8226d445-5182-32a8-9d4e-d49025dedfe1 | -3.21535 | -53.94646 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7836da31-7f3e-303d-8e47-af362b09babc | -5.48511 | -45.12379 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa11cd49-fe48-3fe2-9413-0cdd9734c4ef | -2.4869 | -54.73367 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ec34976-f950-37e8-826d-074c20718e90 | -7.83969 | -45.81958 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| faea1d62-c1e5-37c6-bc38-93a5fa8b276d | -6.15197 | -52.90237 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09ce6c87-7db1-3cc7-83b7-c25734fbfcf3 | -8.21765 | -45.45729 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f3f7b914-782c-3930-aeed-82f094a91ea2 | -2.90725 | -54.09408 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25d780fb-5d0a-38de-9a42-eaedce8ec6ec | -4.49707 | -42.5564 | 2026-09-29 05:10:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67cd234a-ba20-3e36-ace4-a7a0362b6574 | -6.31396 | -43.60883 | 2026-09-29 05:10:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21395174-bc02-36d5-85e9-d41dc629e981 | -6.88721 | -52.47485 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 581c05eb-a088-3844-aead-f6c5ad4b5f2d | -5.73214 | -43.28474 | 2026-09-29 05:10:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 043b992d-01d7-3978-a280-ac097c0af486 | -1.34567 | -55.4811 | 2026-09-29 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1d2f383e-5588-384d-a044-967679d169e5 | -3.15897 | -54.0937 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 395b0e8e-dcce-38fe-80b2-25f80ab9961f | -2.90949 | -54.12328 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34577ee3-e371-308b-8356-cdd76e422cf7 | -5.43042 | -43.44693 | 2026-09-29 05:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cc76a239-9ebe-3717-b78f-e29217da6376 | -5.18924 | -46.07839 | 2026-09-29 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7279e2dd-12ff-39c3-a1fb-a38b883eb15b | -5.01445 | -48.0474 | 2026-09-29 05:10:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f7a955a-8da1-3f6b-b6f3-e32219674a07 | -5.61072 | -45.00592 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a08c1183-3b1d-3fdd-88f0-0f29b9b5794a | -5.73126 | -45.05868 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5b4b4a6-82d6-38bf-92cc-122db803829f | -9.04568 | -49.63742 | 2026-09-29 05:12:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aaebb352-6787-3f27-8f35-9e04aad67e04 | -11.63208 | -54.99717 | 2026-09-29 05:12:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee7d2791-832c-3afb-af2d-568df4407828 | -9.72294 | -54.78257 | 2026-09-29 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b86090-4985-3177-804b-2a53c7815c92 | -12.00494 | -44.93237 | 2026-09-29 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| af93a087-60ad-31c5-bbc7-0f1f2e9d1463 | -12.00149 | -50.99604 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c4f86978-e420-38a8-8c6c-e2e0489abfa2 | -10.82174 | -48.72417 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ddbee51-576d-3bcb-834a-c8b16444d047 | -11.87356 | -47.08824 | 2026-09-29 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5562752-b8ac-3050-8c4d-dab0c5cc0aa1 | -12.01717 | -50.94597 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a6b179c-aea6-3e54-b5e8-4103a4573018 | -11.40381 | -43.42186 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 789f1b37-65da-31a1-bc6d-22a3c412b7d0 | -12.00462 | -50.93983 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f0ab200-d108-3bf3-b65e-cb589be6e785 | -11.17745 | -44.79272 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 759c3ed0-8bd6-34ad-9331-34cbcf65b3ea | -10.39485 | -61.24108 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8210e322-7813-35b5-8974-6b41daaec853 | -12.75104 | -47.29184 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 466446ba-6cc4-3e6f-a424-8872088325c2 | -10.26579 | -59.02839 | 2026-09-29 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 658744f0-2c9b-373b-83a3-48b7683cf06b | -12.00321 | -50.98325 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85fc8db6-87f4-36f4-bf46-01f1811bd068 | -13.16444 | -48.54304 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0bc3928d-7924-318e-a1be-7a9070157e03 | -12.04722 | -50.95454 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e286208-33f5-3277-863f-607bef8d0484 | -10.71785 | -44.44252 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8201dc44-47a5-3bfa-96c7-c99b54554c98 | -11.37692 | -54.04295 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f295e94-7b88-3c6c-bac0-1b13eb2f2abb | -10.70664 | -44.42431 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e52f68b8-4370-3d44-93bb-16ecc4bd68dc | -10.25624 | -44.60533 | 2026-09-29 05:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46049de5-bcda-3f78-be79-31c5607feac9 | -13.16679 | -48.56727 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33565d1a-75d6-38ca-bb37-d41d2b819b26 | -11.9559 | -50.93736 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21f245a6-cca9-36ab-acbd-2128d0f71851 | -13.22056 | -48.56242 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 806835e8-c049-391d-b1ec-21af04cf6ce4 | -9.72637 | -54.78309 | 2026-09-29 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfab3c08-a97a-3ed1-9d84-273d02bba140 | -10.80573 | -48.72958 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51de2635-0292-38d2-b1db-6f6014ae5f9a | -9.79052 | -48.19474 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2229652-72c6-3fa3-bfda-8f801c361fc3 | -14.1188 | -46.2903 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bac9c905-b10f-3eb1-ace1-19d3e95e760d | -11.39828 | -45.4124 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6dc51f75-e4e4-3fe7-a69c-c41022bdb8f1 | -10.39158 | -61.25987 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3330f18f-9f45-35bc-bf10-4c83b86bb307 | -12.90728 | -52.06694 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6320ad83-2c67-3ff1-a9a3-9ab5218df528 | -11.42193 | -43.45189 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f78063ee-8879-321b-aec4-9f5808ae6bda | -12.95299 | -46.64133 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afba67c9-4b0c-3d2a-b00f-4c082e55fed1 | -11.98539 | -50.95025 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 242c970a-e31d-3dee-a68b-13466ffa179c | -11.05462 | -54.19609 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecfb9ec5-3c58-3c93-bd0d-22b21d7bd916 | -14.7674 | -47.15627 | 2026-09-29 05:12:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 267a1b38-fe8f-32ee-b6d2-e2dbcf362e5b | -8.28615 | -54.7029 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f639a7c3-9851-3be5-a7b4-35ccf50c8bce | -12.01021 | -50.99726 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96493a91-5d22-3c2e-aac3-90f607427408 | -10.41261 | -53.82464 | 2026-09-29 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95ed4ebb-e051-3933-a92a-7b80fb00f309 | -11.39522 | -43.43501 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9763dd99-963a-3398-acb9-6042668e21e6 | -11.90139 | -50.61568 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98c74f9a-9a73-3b09-ab2c-2d67413ff8db | -10.81156 | -48.72405 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ea21420-dcc5-329d-8efe-31fe2fb98dbc | -12.05354 | -50.22081 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f74b5ed3-7cbf-329c-b419-4a3172fbe124 | -13.45312 | -48.5822 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9939a30-633b-3efd-95f8-c2b6f7f071ff | -10.80612 | -48.72662 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adeb3756-bcdc-3d5b-83df-a14a17b66c37 | -11.37333 | -54.0424 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e91e334a-85ae-3608-bc03-35cb949f8a72 | -11.44075 | -43.47494 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 985cbf9a-df45-3ccd-8e90-6587018eb2af | -12.95245 | -46.64606 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fad14b7c-fabe-31a7-920d-af66c9573c19 | -12.03788 | -50.9576 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d660c4b-99bf-3d28-8d63-803ff55c192f | -9.96386 | -50.13101 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e8bcb50-e029-3807-9414-0add11ab83e9 | -12.79665 | -54.01101 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a09c1126-b886-3bce-9d69-42080ce6c050 | -11.42969 | -43.46689 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4cf4bf82-5623-312c-b8a2-29e5d602492e | -9.06927 | -49.86749 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f88a910-8c17-3492-9592-f63e2597c94d | -11.35293 | -54.05624 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 189866b8-b16f-36c0-8721-9470dc867edf | -11.41333 | -43.46501 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29fbe8f1-737e-30da-ba2c-d852c6c29ec6 | -13.52338 | -46.90243 | 2026-09-29 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9116cd5-48f7-378f-a61d-0ff2a3dde0ee | -11.01204 | -54.16475 | 2026-09-29 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1a7903b-fd2f-364b-a49f-d0b8038f5b1b | -12.76238 | -47.2931 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b6941f1-d238-3141-bfb2-9b5ec5973c9d | -10.69936 | -44.42918 | 2026-09-29 05:12:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 668f5a6c-1780-3ae7-bbe4-c99aefbcef15 | -12.75321 | -54.05317 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c9e2ddc-a3e8-3077-957d-f0a0d7938eca | -7.49538 | -54.97096 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68c97e58-a6f9-30c9-bcef-1b7ebf3d3adb | -11.19058 | -45.13816 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a10cd03c-e6a0-3905-90d1-92c06bf69e2f | -11.99356 | -50.95576 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd7211fa-9e3c-3e14-8e85-9db2858c1255 | -10.70474 | -47.82127 | 2026-09-29 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93136332-4d23-3a55-8831-595b5614afbc | -12.75905 | -47.29842 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e02110ff-dfad-3246-9c4f-c930379906f7 | -11.36431 | -54.05373 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e86652f-a20d-33e5-bbc3-09a4f43bd1ab | -11.38112 | -54.03936 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b020123-3276-365e-92bd-06ad614a04bf | -11.4478 | -43.47569 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 071d6f53-288b-3fe3-b33d-b3e11f50c7a9 | -7.17678 | -69.89342 | 2026-09-29 05:12:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95e00148-bc21-3ec0-865f-f60ceb04f342 | -12.94067 | -46.64408 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91399ee2-9da5-323b-9595-91e8079a4adb | -12.24528 | -50.42858 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7404e43-ad50-33d7-860f-5fc687e8898b | -8.30145 | -54.71661 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6111a429-9f2e-32ef-8fbd-07e77e575f21 | -11.43998 | -43.48179 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5797cec-7e37-35c2-8956-8bab0e17bba2 | -12.0638 | -46.49742 | 2026-09-29 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1fb8cd6-7b72-30d8-b143-8a0fe0becd3d | -11.3919 | -54.04097 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea16a3d-316f-3a63-91b7-908f2760e470 | -11.50926 | -47.40714 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README59.md)
