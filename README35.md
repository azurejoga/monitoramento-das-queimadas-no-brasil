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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb88e376-1329-302c-a867-70ca40b9930f | -8.59336 | -54.73225 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 353a294b-2c48-3366-8eb2-b7d0d4a586ef | -7.15118 | -43.43794 | 2026-08-25 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66b9d945-d00a-34e4-b9d1-acd6249c5050 | -7.19426 | -42.74906 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e07e644c-74f2-3b7a-b1ab-9c9344958866 | -8.65913 | -47.32252 | 2026-08-25 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7da0733d-c298-3ed1-bff1-c897c048b05d | -9.96419 | -48.32128 | 2026-08-25 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44ec07f9-7faf-31b6-9cdc-1d310a308b02 | -6.18568 | -53.51806 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80c3ccf1-de96-3aaf-95a1-920c182dcbba | -8.07328 | -44.64872 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5d0ea6f-da6d-3f61-a539-6a0ac357759e | -10.37489 | -45.06242 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ca866e7e-514e-3d06-aa39-f1c6adc89678 | -3.97264 | -41.52018 | 2026-08-25 04:25:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 137f559e-d760-384b-880c-8c9cb958bf2c | -7.28742 | -45.36682 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e886be4-ffa7-3e12-8c1f-07faee1a50d0 | -7.25486 | -45.37937 | 2026-08-25 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a98378a-1e0c-3f04-8325-e53943da7a6a | -7.43545 | -43.1139 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 10fa5b8b-83a8-3e40-b10b-48e7433761f5 | -7.4805 | -46.09254 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83ffc281-53f0-3776-82c0-01d1baf380a7 | -8.09751 | -47.47645 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9255307-58af-3d0b-92ec-0b288901ea63 | -9.68836 | -46.05678 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ba33b51-80b3-3645-9dda-c00557bdbc9e | -5.81673 | -42.91681 | 2026-08-25 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1a9d6efe-1e92-37ef-af42-263b8bcee24e | -5.89151 | -46.91325 | 2026-08-25 04:25:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef7683cf-d636-387b-9bbe-d75b82a05417 | -7.15006 | -43.44523 | 2026-08-25 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1514df42-5a0d-33c7-a1de-49fc07c97d72 | -6.43382 | -54.97469 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26024624-fd14-36e2-9447-1039a72d18c1 | -8.08488 | -44.6398 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c357098-e2f0-38e3-8b17-917d8d7195f8 | -7.28246 | -44.0819 | 2026-08-25 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60079f76-2051-31f9-b99c-f3850df56123 | -6.83712 | -52.50714 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f90ffaa2-07e7-377b-bf6f-9470128fed77 | -7.13229 | -42.78275 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0dd32f77-3f5f-3125-88e0-58538d73c399 | -5.76933 | -57.55803 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40760223-a965-3103-9f88-137e604c5ce4 | -8.09787 | -47.49613 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9c6da6c-d4a4-3850-b88a-47bea74a6275 | -6.19542 | -53.52308 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f304faf3-3a91-34e7-84bf-f424cd96e697 | -7.48742 | -44.9409 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c77aec5e-c8d9-32e5-a95b-295f6078b2b8 | -5.95203 | -53.5901 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0794c0a-49c9-3b4f-ac56-593539da2c99 | -6.83887 | -52.49685 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e1165eef-2d43-3308-8479-d97afe2351e6 | -7.13171 | -42.78659 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e472dcb9-8b75-312a-aa5a-1a2450693ec8 | -7.28356 | -44.07483 | 2026-08-25 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6dde66b5-f433-3efa-ac9b-6aa813b63c84 | -7.31284 | -42.97616 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 987be31a-8d3a-322b-afd1-9f36b0eec93a | -8.21617 | -55.00011 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81280259-752a-3c25-ab36-c3aa62ce3770 | -10.526 | -46.32203 | 2026-08-25 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ce137b6-f7fe-3226-bdc8-290c6697ef4c | -6.17508 | -53.4876 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e70eb750-804e-35e2-b474-a9dc8aaab239 | -7.6577 | -47.11607 | 2026-08-25 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 422b8eeb-c5af-3297-897e-f410d6c3f3b9 | -7.24616 | -45.86011 | 2026-08-25 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1949efb9-7ebd-39eb-83cd-0e4e13feb7e8 | -7.24883 | -44.21009 | 2026-08-25 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f293058-9ad6-3a10-95b6-75ef26901a79 | -8.21509 | -54.97565 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48cfafff-8048-353e-95e2-e385d7195472 | -8.17028 | -54.97186 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f025e989-dc28-35fd-8c96-ad151a060b2f | -9.20551 | -50.10528 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4677b880-577a-353c-8f4d-ba5541a25cf0 | -7.41505 | -44.96813 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 607085d2-875a-3073-b069-e1a766a873f0 | -9.65231 | -48.32053 | 2026-08-25 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 54b5d56c-821f-31c1-822e-b2aa7b75f1d2 | -6.33872 | -54.74396 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f547b274-0c33-3c27-b74a-4f5da996fded | -7.15201 | -42.74638 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0112373a-4e82-3c25-b709-0df89568eeab | -7.65212 | -42.73324 | 2026-08-25 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c3c353c-c70c-3b13-8adf-e8e6559a5480 | -9.04583 | -50.80712 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bf15ff5-687a-35ec-9f47-6e2c87f9c730 | -9.04551 | -50.78444 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca5b8964-6f7b-3f50-a4e3-b15b0e60c40e | -9.44108 | -51.58678 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d8a5f0a-71c3-3967-928c-f36b93810ebd | -8.60121 | -50.01524 | 2026-08-25 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 523b82c0-7dd6-3811-8dc4-9f6de9392d73 | -6.97441 | -42.08319 | 2026-08-25 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 476d0f6d-9e32-3ea7-8547-943ba53b4199 | -6.35074 | -54.77295 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e66dfcee-bb5b-3cc4-8ec4-ac33f54de2ae | -9.03868 | -50.82425 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 476b0f9a-a4a0-332c-b11b-90dfb2cf3aea | -7.43602 | -43.11016 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d0a3a73-a2b8-3052-a7cf-56af59058196 | -9.05894 | -45.22686 | 2026-08-25 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe9852e2-6c9c-35e8-b19c-dc7a1232f23d | -9.38212 | -45.41772 | 2026-08-25 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bb191f4-d40e-39f5-b97b-c512579470fe | -5.90083 | -45.54057 | 2026-08-25 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a500fc7d-c2c4-358b-affd-02579e260b42 | -9.6983 | -46.05838 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d124ffa-c648-3df8-995e-8f2493f3cdb1 | -7.1879 | -42.74414 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09595af1-baa0-334c-9201-629185e26441 | -9.5343 | -49.27311 | 2026-08-25 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48c37656-1ab1-353c-97c9-7610fcd86a59 | -6.56877 | -44.34666 | 2026-08-25 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de27c4a9-ac63-3e20-adb6-b37de3701b13 | -8.2094 | -54.97471 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 415ecd42-1b1d-35c2-9487-4c871f4f99b7 | -9.03286 | -50.76027 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7059315a-01ca-3042-90f2-fa1a7d0dc1ad | -6.43378 | -43.86332 | 2026-08-25 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8769a05d-2ff1-3026-bbd5-cf81e2cdb3ac | -10.57132 | -46.31506 | 2026-08-25 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 348a6e5d-1f43-3bea-8f5c-0b3387242515 | -6.17467 | -43.7649 | 2026-08-25 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a916cde2-9fd9-396a-80bb-a9b4ac78da90 | -8.5723 | -54.84936 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5642dda5-31f7-3e18-9b83-c74a59edb560 | -7.63935 | -42.72335 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| faad3c0b-e603-3ef8-b2b1-28682f296994 | -8.66035 | -47.31504 | 2026-08-25 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 344d5a4e-98fe-3966-ae3c-30170d7098c5 | -2.78723 | -49.58239 | 2026-08-25 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f29d667-8605-3d5b-a284-3d0b35c7c1b5 | -9.7376 | -45.98228 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e3d0b0b-6521-356d-a94f-a7de34a4bc41 | -6.18481 | -53.49254 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32b117c0-69d8-33c0-9104-15eb165d783b | -7.15062 | -43.44159 | 2026-08-25 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8329f07e-3204-32d1-9d6b-a07cbaf547d8 | -6.97162 | -43.76482 | 2026-08-25 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a72edd6c-4278-3e42-82d8-15e00a066e3a | -8.54033 | -55.30542 | 2026-08-25 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f96baf8-8d91-3b76-9f1d-02679f1c1a1b | -5.78997 | -57.61138 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd6a815f-b727-312a-b2b0-0dde74c519d3 | -7.86857 | -46.11157 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 045b7365-336c-3462-b6e5-499f00591b8f | -7.48797 | -44.93744 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7945a15d-381b-337d-bf46-9f1d12561ea7 | -7.6632 | -46.91151 | 2026-08-25 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04c0ae0b-0e07-3347-bc7e-69e32ad09570 | -8.92559 | -45.72616 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ba16e8a-75b0-3818-993e-b9e44e6ea50b | -7.30652 | -42.97129 | 2026-08-25 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 59e9c5af-51cd-35a7-b2dd-f13f64f44dd1 | -7.1439 | -42.75302 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f2d5b784-21f4-3e58-81bc-642b3b171651 | -6.19082 | -53.51901 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e0d7e1c-6560-3ba8-9b2c-2d66814bd9d9 | -8.08377 | -47.51737 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa4b37cc-b170-3a02-81c6-8f50e6c57b39 | -6.11798 | -57.83229 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 666c91a4-dcf0-36da-a9e4-15f3f1bd15e5 | -4.47381 | -54.80517 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ab752fe6-6f05-3fed-a8ef-ef7c6a7af8f4 | -7.63875 | -42.72724 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7d990fa2-70e9-354c-8c4c-30524c6a51b4 | -8.65974 | -47.31878 | 2026-08-25 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 083effdf-9bea-386e-bad0-7bdbbd2e18a1 | -7.75808 | -46.14455 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45846b52-efe8-31e6-92ab-2a3d69437d85 | -3.53811 | -48.17921 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| fe50fd21-6de9-3094-9a0a-5f8a7ab55391 | -9.05618 | -45.22283 | 2026-08-25 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58541146-be1b-311a-a965-f14934d395b8 | -9.70329 | -46.0484 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abdf935c-9903-336f-8e64-4fe04da7ed94 | -6.81606 | -58.65625 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c8b2c76-3218-326b-b66a-6301b4561932 | -9.04839 | -50.79217 | 2026-08-25 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d39de69-17bc-35e7-a68f-cf1644ea386f | -7.14331 | -42.75688 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 269fe649-eae8-33d9-b14a-164e652c1318 | -6.63232 | -58.5092 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 27c62794-2c9f-310b-ba6a-eca106ab41de | -8.31183 | -47.59624 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 728e3040-04c7-3f97-9c13-cccf11c67f08 | -5.88015 | -52.126 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da253d7a-bd99-305e-ad32-c7e3562d0d04 | -10.04075 | -46.42337 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8519172e-026c-31bb-8767-5d7b6d4773bd | -6.97256 | -42.09531 | 2026-08-25 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
