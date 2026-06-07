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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f175f172-dfac-3d17-b00f-97f1a8627f6d | -10.18775 | -52.65145 | 2026-06-07 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a85ccdd-ee92-3431-a146-89347f2a7b37 | -6.90738 | -51.05271 | 2026-06-07 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5c706ea-bc52-3f0d-9211-09dfaf7b9c5a | -9.27361 | -50.65759 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e36201de-37a8-363d-bc8c-7937a01a0db7 | -10.1916 | -52.64845 | 2026-06-07 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a44b52eb-aa5c-3fa0-9351-e1f3d0cc40f6 | -7.50941 | -55.00882 | 2026-06-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77eec21f-6a6b-30c7-be6d-77521a6b10ee | -7.15717 | -44.06179 | 2026-06-07 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4179b704-d0d5-36e3-94c5-d2132573424d | -7.18798 | -46.55058 | 2026-06-07 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 554bc4be-9da8-3ff6-bf38-b81f1165edaa | -8.93797 | -45.67654 | 2026-06-07 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e422efdf-97b5-32ab-b968-d8174f4bcb0a | -9.08877 | -50.60778 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5475934c-8578-3e96-9154-37a2e1205f69 | -5.80918 | -45.12115 | 2026-06-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81bb4879-afe4-38fe-bea6-593c928982c9 | -8.94337 | -45.67212 | 2026-06-07 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| afd6e64c-714a-3e94-8660-3f8f25668b79 | -5.93803 | -45.49866 | 2026-06-07 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 282b3f64-49d3-300b-a45e-9b6fd8517e3f | -6.99775 | -43.86298 | 2026-06-07 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0340f56a-d91f-3d71-88b3-58ba8fe21138 | -10.18444 | -52.65093 | 2026-06-07 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fbee0a6-be7c-3618-8788-4ff9dda25a3e | -7.00161 | -43.86511 | 2026-06-07 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09f55463-3d3c-3c1f-8402-16c655f58172 | -5.94649 | -45.50471 | 2026-06-07 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6192b306-a01a-3abe-9c3c-db381a8122ac | -7.15676 | -44.06475 | 2026-06-07 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec8b1d44-28cb-38ec-89e5-2474c4ef76fa | -9.62417 | -49.02391 | 2026-06-07 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50884c67-947e-3737-ab51-f27ff974a220 | -8.46884 | -50.22088 | 2026-06-07 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2acb9f29-2c78-3734-918f-c82398776822 | -9.07538 | -50.60175 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 886e9de2-65c5-34a5-b828-4c63d1354cf8 | -8.16975 | -46.822 | 2026-06-07 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50399930-7714-3ec2-a8ef-cd8866168034 | -9.09691 | -50.60098 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dae8c032-9377-3093-9520-a7b9bf47679e | -9.10579 | -49.64606 | 2026-06-07 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1071fe4-737e-320d-8322-7f3be6dfa726 | -7.87947 | -47.10123 | 2026-06-07 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 726f9f76-3033-3420-801a-e82e5ed96a9c | -9.08528 | -50.60725 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a41c0da-f78a-3dd6-a970-e84fc72dec02 | -9.07304 | -50.59337 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c949fea-3d40-3901-a8fb-fe111c3ee131 | -5.72322 | -45.03667 | 2026-06-07 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f90e9441-5248-32a0-9eac-95b775eec18d | -7.00206 | -43.86194 | 2026-06-07 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bbe8946-e090-3b19-ae61-9f8e479cc395 | -8.02992 | -46.05478 | 2026-06-07 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d43ba70d-23bd-3104-94aa-5ff7213c50a1 | -10.44024 | -46.4058 | 2026-06-07 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c122e23e-bcf7-31ae-9a5c-9c70712fee55 | -7.15635 | -44.06767 | 2026-06-07 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97d84e0c-915d-37c2-8597-edffed923d37 | -5.9426 | -45.49931 | 2026-06-07 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6cbe2691-c235-3b05-acc0-8ba4740f28d6 | -9.09342 | -50.60046 | 2026-06-07 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dd6eb03-519f-32a4-a5ce-4188927738bc | -10.19107 | -52.65197 | 2026-06-07 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8586de54-0117-31bb-8eb3-43fff07499f9 | -11.97837 | -47.36136 | 2026-06-07 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c104d581-0acb-35ec-a1e3-40688a835223 | -10.8308 | -60.7609 | 2026-06-07 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6cbbe3dc-5524-31ce-8ed4-ffd163e529af | -10.84993 | -53.75172 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93805d5c-1d5d-31e0-b692-739cf1087cb9 | -14.64366 | -54.51245 | 2026-06-07 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c9f0596-734f-343b-aaf2-8214dc7706e9 | -10.91962 | -54.11152 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca6c505c-a265-3430-b212-b647bbe877cc | -12.06323 | -48.07627 | 2026-06-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c5d3392-99ce-3c7d-aca4-904ff4eb67f4 | -12.5033 | -46.27132 | 2026-06-07 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ecee971-cca4-3e9b-a4bb-e03c670b1895 | -10.77455 | -54.10198 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d3c1b7a-c761-3d46-b248-2a2f48b02197 | -14.2358 | -47.97508 | 2026-06-07 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9116311e-2788-37be-9ecc-0ef603053c2f | -12.80886 | -54.86061 | 2026-06-07 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee2850a-02c6-3177-83cf-626d3f767ac0 | -14.63215 | -54.45612 | 2026-06-07 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef949818-be07-34bb-9846-fce1865aa7fd | -10.84003 | -53.75013 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc695189-30f0-3883-8169-dbe9314fd509 | -10.85926 | -53.73533 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 680ca71f-8438-38c7-a603-af90e5514cfb | -10.82903 | -60.77072 | 2026-06-07 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8edfdec7-4089-3206-9749-4b139e56acf2 | -14.24518 | -47.97101 | 2026-06-07 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cba323e-1455-3410-b2e9-74148dd77e64 | -11.30099 | -54.88056 | 2026-06-07 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8edc2d4f-c806-3d56-9ebe-4ac2b3ca3c42 | -16.50583 | -43.5062 | 2026-06-07 04:53:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b44bacf-7142-3af8-9849-0f5d3dd5577a | -14.28636 | -57.53415 | 2026-06-07 04:53:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e39a2a5c-37d0-3731-a9cd-1f22bb62468c | -11.56121 | -52.80583 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26a96fb2-f83d-361c-9b88-3a2a4d94c582 | -12.81161 | -54.86472 | 2026-06-07 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c230ed15-31a1-3e06-8a19-07af340ed23c | -11.55415 | -52.80854 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2af71313-fa1e-37bb-a86d-894719026216 | -13.36479 | -43.20119 | 2026-06-07 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 40523fbe-fb61-35da-901e-7c3469cd62ac | -11.05346 | -56.92819 | 2026-06-07 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 319078da-422d-3ebe-8f69-e1e261ff223d | -11.55083 | -52.80801 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69acb5f7-ee9d-32cd-8854-cdb24e32b231 | -14.55146 | -49.11481 | 2026-06-07 04:53:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3da0b2c-a194-32d8-ad0d-edb0e143093d | -10.92293 | -54.11206 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c09a34ce-d661-34a8-831e-37946533899c | -11.55688 | -52.7908 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 61390120-2e20-3579-9438-6e97e0c8a5b4 | -12.50508 | -46.25718 | 2026-06-07 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e52f43e-3c67-34e0-b7ca-5f0915aa1613 | -14.28849 | -57.54329 | 2026-06-07 04:53:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7c415ae-0c1f-3316-8efd-db58b1b67a40 | -16.50229 | -43.50317 | 2026-06-07 04:53:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 52edd1f7-e1ad-3d29-9533-cca1636b2e00 | -10.84333 | -53.75066 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7698010b-9f26-33ab-888b-4aa26b123694 | -11.63004 | -54.15873 | 2026-06-07 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 924de8e1-c2ff-3789-9d59-513c5824c57b | -13.49674 | -56.57272 | 2026-06-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 783a0418-e967-3e15-89ed-0d6e7b7eed62 | -10.85871 | -53.73882 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ea31849-71d2-31a0-849e-9010eeaf9749 | -13.36257 | -43.20584 | 2026-06-07 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 601154f9-2e3e-3c7f-9d58-c5c955ece978 | -12.0627 | -48.08022 | 2026-06-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 920a5625-b3b4-34a4-993a-3f0c4b40e2e0 | -10.83632 | -60.75679 | 2026-06-07 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0fbead0c-5faf-35bb-9762-7f50b6b09363 | -11.98276 | -47.36198 | 2026-06-07 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4709878-f02c-3a14-9ca2-7382803233a0 | -11.73302 | -51.13095 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e91b662-a4d1-3c82-85ba-a5cc23ded9bd | -10.85816 | -53.74231 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e313981-1721-3598-9909-8e61ecae88c1 | -10.85541 | -53.73829 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7ea9496-2c2e-3f2c-9b24-7cf2a04b7884 | -11.72445 | -56.84863 | 2026-06-07 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6c67ab3-d96f-3228-9b88-76a2d6cacb12 | -11.55356 | -52.79028 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 410437af-321e-3b78-9bd3-a7e829600be6 | -11.61759 | -55.18177 | 2026-06-07 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21dfad75-a632-3d80-a782-bc7411d9fa82 | -13.11597 | -53.53157 | 2026-06-07 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 976ae9f3-bb20-36d0-bfb8-0a3a498f96d1 | -10.59535 | -55.42133 | 2026-06-07 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f446f27c-50b0-3aca-9dad-0ffbc88dda97 | -14.1676 | -53.98787 | 2026-06-07 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6b69e7c-6e84-3c59-b3ff-567bd0345a05 | -11.46394 | -55.11561 | 2026-06-07 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ac9496c-0ba2-3973-97d6-0f39d23e2253 | -11.47414 | -47.34301 | 2026-06-07 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75ffe1c9-c6e7-3bef-ab8d-092e0f4f9383 | -11.56453 | -52.80635 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8332ff56-6ce6-3c37-a299-abf44553a9af | -12.3679 | -47.89231 | 2026-06-07 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a954a96e-f424-3067-a5c0-f92ddd5ca91b | -12.40902 | -47.49699 | 2026-06-07 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d3b7623-6f94-30fd-a67c-5074e7b84bfa | -10.57408 | -57.32354 | 2026-06-07 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0193ba2-6612-3453-8408-fdfcddb01be3 | -11.6339 | -54.15575 | 2026-06-07 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc09155f-aa8f-3796-b5a6-1c11c09810f9 | -15.36887 | -55.88054 | 2026-06-07 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30d2ef58-ee22-36f4-9e35-d441db5678eb | -11.47852 | -47.34349 | 2026-06-07 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19ec3f06-61b0-3e63-8e7e-0e4558568e9d | -16.49985 | -43.50513 | 2026-06-07 04:53:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed65ad7f-e3bb-3e06-a5f2-b58fe0efc815 | -10.59876 | -55.4219 | 2026-06-07 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bb8ebe8-a245-3e34-bdc6-4fd67fb61b77 | -11.79371 | -57.35435 | 2026-06-07 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f6221f0-e8cc-34e6-af0f-69a59731e48a | -10.83543 | -60.76172 | 2026-06-07 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 72eba0e6-a081-332e-a63d-10dbeca8046f | -12.49965 | -46.26176 | 2026-06-07 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ef0c11b-5de6-3034-bacc-e500d04e5951 | -11.55743 | -52.78725 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2abff7ab-658c-30ee-9cf6-a991f9973b2f | -11.6306 | -54.15521 | 2026-06-07 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 681c4911-2dfc-3731-9825-6bd458969001 | -11.54692 | -52.78923 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 69c6a92d-3ebd-3a63-9142-4a635bff3d06 | -11.55024 | -52.78975 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 360567b2-2771-3955-b22d-85b9ee52790f | -12.06974 | -48.43076 | 2026-06-07 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |


[Clique aqui para ver as próximas entradas](README6.md)
