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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa6028fd-9194-3ad2-bdcb-2a6ff221c898 | -2.87085 | -50.46226 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| dd79b563-437b-36e2-b638-a303b5cc0633 | -2.86936 | -50.47241 | 2024-10-06 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 1899863a-fa93-3500-bf77-54048fe17777 | -2.83237 | -48.5996 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b1b391bb-b920-3e58-b9c5-cc1652d97062 | -2.83168 | -48.68145 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 15119fa7-35d2-3256-87c3-ef20ca51f308 | -2.82978 | -48.69471 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 29c07372-ecae-3185-b4b2-b15006312119 | -2.81907 | -48.69319 | 2024-10-06 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6e731f59-ef97-3a0d-8111-2c9726614e8a | -2.79645 | -53.20679 | 2024-10-06 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ee00bf8-80ca-3fdb-9fb2-ca9d7c84331f | -2.79513 | -53.2156 | 2024-10-06 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2406459f-58ff-39d3-9c8f-aa44b4f9ad9c | -2.70666 | -49.06308 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 13155647-736a-3123-9bb1-c10382355d72 | -2.70486 | -49.07547 | 2024-10-06 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a2b681da-2bda-314c-bdfc-93325047115c | -2.62127 | -54.54705 | 2024-10-06 05:48:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5636ed06-1235-33e9-8f6c-9139f4f74182 | -8.4044 | -46.29416 | 2024-10-06 05:48:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 456b5b20-051c-3424-a02f-480b1348393d | -11.91023 | -50.1089 | 2024-10-06 05:50:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4a2bfa92-8b30-3a52-ac81-6d1fad241f0d | -11.89909 | -50.10738 | 2024-10-06 05:50:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3ecffd47-4ce5-372e-b41e-3c6b98fee904 | -11.89834 | -50.10191 | 2024-10-06 05:50:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 183adce1-67a5-3d51-b6d6-94a020e12cfa | -11.25498 | -53.85668 | 2024-10-06 05:50:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d87e8cb9-d971-347a-a3aa-1a6d3f41e188 | -11.25364 | -53.86581 | 2024-10-06 05:50:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b78af0d-15f7-3195-ab2f-6f0056ff06aa | -11.24605 | -53.85537 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 225ed4f1-3255-3d1b-9d51-812402c09a64 | -11.12517 | -54.22967 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 92cf63ae-81d3-3743-baf6-8599bc048575 | -11.12383 | -54.23866 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac816611-7cff-3803-9fa8-33ada6381d51 | -11.1163 | -54.22835 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 09442f21-a662-3830-838f-578b216658a6 | -11.11496 | -54.23734 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 62cd7a1b-46df-3875-9c97-4b3a71ea2952 | -11.10125 | -54.0232 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6189dda8-b7e8-3f12-820e-df0ed1bd6d5d | -11.1008 | -54.77258 | 2024-10-06 05:50:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 755a6a1a-baa0-3cc3-aada-a14b63e7d853 | -11.09992 | -54.03224 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d2ab6e5d-d4f3-33e7-8c24-ee094185de2d | -11.09946 | -54.78153 | 2024-10-06 05:50:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 52fed418-e8c0-3e9a-9a15-66dbbab53b96 | -11.09103 | -54.03092 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 733acac8-3406-3e82-ae53-6092aa4cc23c | -10.99338 | -54.00977 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d20c2a4-0a8f-30e8-8014-856d47065fff | -10.99205 | -54.01881 | 2024-10-06 05:50:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd15c5d0-2f18-3618-82f6-bc0b5e33e386 | -10.92524 | -52.38457 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a23e51e2-c2d7-37e1-bba6-849c296baa4f | -10.91729 | -52.37303 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 8bc32598-b0ed-317c-9299-2e41176d09f8 | -10.91583 | -52.38321 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 392b2970-9de5-36c1-af12-c72c01ad99b0 | -10.90642 | -52.38188 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 43daebbd-81c8-3491-8c7a-1e31fdd036f3 | -10.89555 | -52.39075 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6db85de8-c663-3a39-8ceb-55ed7f11531f | -10.8941 | -52.40097 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 139292d3-003d-3520-bf89-52e146750cd3 | -10.88513 | -50.13145 | 2024-10-06 05:50:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 270b2942-284b-3428-9b6b-474601b96d98 | -10.87539 | -50.13692 | 2024-10-06 05:50:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c48f1bf9-b6b5-3d58-b18d-2ee3b99bf164 | -10.78178 | -52.47202 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 90ba2a52-1aa0-38e7-8ec6-b307a4d37bc2 | -10.71884 | -53.04147 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e00a624d-c9ef-3e64-9029-12e2c2ab6b67 | -10.70973 | -53.04011 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5f348989-aae7-3776-8254-4b316451fdb8 | -10.46686 | -50.69393 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 00620859-94c8-356f-ab04-f03b2b698cc7 | -10.46515 | -50.70655 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 300.0 |
| 450ee7b2-1f3b-348a-98c8-d313439b91e5 | -10.46342 | -50.71931 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| d52b8949-9308-3401-9df5-aa4eb62e52c7 | -10.45644 | -50.69251 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 227.7 |
| 97f419fb-b805-3402-9e6a-2293ba5fd2af | -10.45473 | -50.7052 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 893.3 |
| ef9211f7-a779-3389-a610-2e207ea70e92 | -10.45302 | -50.7179 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 224.3 |
| c682370e-a85b-34db-86ee-a223a9b7433b | -10.4513 | -50.73061 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 12e2bbf8-aa5a-3146-9962-c2381a2099db | -10.44602 | -50.69112 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5a3dff45-ff8b-3f50-9a18-4f8002008ca3 | -10.44455 | -50.78063 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a95b4edd-5660-3e1f-badc-24d5c747d412 | -10.44432 | -50.7038 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 518.3 |
| 86c71cdf-c09f-3d47-ae23-24a81907c4a7 | -10.44262 | -50.71644 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 436.9 |
| 681635d6-99c9-3b71-8b7e-127c0d9a02e5 | -10.44093 | -50.72906 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1a8d40b3-36e3-3410-a60d-880768131fc0 | -10.43885 | -50.69623 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 395d6a61-3a2b-34c0-a4d2-fb4cc3112d0d | -10.43707 | -50.70889 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 280.1 |
| 9e925f6b-fe15-30a4-aeca-c6e196315f25 | -10.4353 | -50.72149 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 254.0 |
| a5a491fd-167d-3cff-89cb-18558c21ea29 | -10.43391 | -50.70236 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 800609f3-15a2-3d53-be3a-909e14c74da1 | -10.43353 | -50.73407 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 795d4070-02df-39b1-a53f-d1878e2636bd | -10.43222 | -50.71503 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| d40422ea-77cc-3b00-b2dc-b67ee6d6b894 | -10.43054 | -50.72762 | 2024-10-06 05:50:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 12ba3d2c-e5b3-39b7-8cac-3d773e95333e | -10.2332 | -59.4072 | 2024-10-06 05:50:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| d4cbd46b-092b-3755-9fee-03820d48bdea | -10.23314 | -59.39851 | 2024-10-06 05:50:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| cecb39cc-eaf9-36af-95da-a00c9abf66d4 | -6.95858 | -59.06361 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b5dfd8d9-e1de-3c21-8c3a-1f5b6ba93bc5 | -9.8673 | -60.29831 | 2024-10-06 05:50:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 85990e41-bf35-3286-bc10-816894ee296d | -9.77061 | -53.15842 | 2024-10-06 05:50:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 46f351ad-2a2c-3652-8583-deb403f2e1c9 | -9.7591 | -50.64952 | 2024-10-06 05:50:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9ed90872-df74-3af5-89ee-5cc951137aec | -9.74853 | -53.1836 | 2024-10-06 05:50:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9bda84c7-4e54-3ad5-82de-a262b331f298 | -9.71265 | -64.60133 | 2024-10-06 05:50:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| e25ac97b-e203-3ac1-8aeb-3d76785e5a36 | -9.70567 | -64.64091 | 2024-10-06 05:50:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 1ff11277-438c-3b9c-9062-cb70a77d7d4a | -9.69628 | -64.60667 | 2024-10-06 05:50:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 21fdafe6-4394-3702-8df7-40fb7e7866bb | -9.68379 | -53.50171 | 2024-10-06 05:50:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f17f60cc-4d3a-39c4-843a-3a3c9937f0fc | -9.68075 | -53.58465 | 2024-10-06 05:50:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 349efabb-197b-39df-b8a1-7b947a006d51 | -9.67316 | -53.57428 | 2024-10-06 05:50:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 85ff6069-43a6-35b7-971c-bae82a30aa33 | -9.65438 | -53.57413 | 2024-10-06 05:50:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9137d3e1-6a48-3f74-b982-bba30c24b5f4 | -9.65411 | -51.77955 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1a466ba-00f3-354a-9763-a4239f9b8b99 | -9.58539 | -50.22892 | 2024-10-06 05:50:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a1be3266-aa06-3f92-b519-64db08668b00 | -9.39187 | -51.09057 | 2024-10-06 05:50:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aec057ee-dfee-3ecb-8deb-dfe6125a87eb | -9.38348 | -51.07765 | 2024-10-06 05:50:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 74ec2315-162e-30d2-93d6-335a2f0b1b60 | -9.18208 | -61.55203 | 2024-10-06 05:50:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e37c1669-ca07-37d3-9c1e-67f210096972 | -9.17812 | -61.57534 | 2024-10-06 05:50:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a9e22afa-8305-3ffe-816c-84672b9ba9da | -9.09244 | -53.25984 | 2024-10-06 05:50:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6b93b9f9-fb1c-3e7b-a314-652f7f88e3ce | -8.97691 | -52.78688 | 2024-10-06 05:50:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7cb12184-0d47-35b0-a4f0-00598fb01905 | -8.56946 | -51.77448 | 2024-10-06 05:50:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0d735d2-868c-30c6-83f5-0dd4df48b19e | -8.39287 | -51.65287 | 2024-10-06 05:50:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2aab1a05-e940-3866-b9cf-3934a95ad57b | -8.23017 | -61.20133 | 2024-10-06 05:50:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bc0ea9f0-53b0-3755-a195-7567e7595912 | -8.12903 | -55.30722 | 2024-10-06 05:50:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3d024728-3b67-3683-a66e-1d23e8bb181c | -7.99199 | -54.75299 | 2024-10-06 05:50:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5aacddd9-8677-3d4f-ad4a-a619fc3ac5d9 | -7.99063 | -54.76201 | 2024-10-06 05:50:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70b8b8aa-bda9-3770-8837-ce02a8f1338c | -7.98927 | -54.77103 | 2024-10-06 05:50:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0dd69e29-e529-3f22-a3bb-2051492992d0 | -7.88768 | -54.88896 | 2024-10-06 05:50:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7f98bcfd-0dbd-34d0-ba18-d949a36aaa40 | -7.1719 | -59.30224 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e6b4aa31-9dfe-3bcd-a44a-34fed64ca9a2 | -7.16002 | -59.30035 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 436f3ac8-3e26-32e3-b6e1-8224bc41d1ec | -6.97885 | -59.05752 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| bdb35322-530a-375a-a11b-812d241847b3 | -6.9762 | -59.07368 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 7afd5a20-98e8-390d-90f5-3400497ecd08 | -6.97279 | -59.0494 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 4f9cc683-3420-3b65-8c70-7ed97d6ecbe4 | -6.97028 | -59.06548 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 278863b0-5014-3099-837a-f4160e11afe6 | -6.96717 | -59.05564 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 44963d04-906a-3ab7-9d45-3630cf745600 | -6.9645 | -59.07184 | 2024-10-06 05:50:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 37e3d36d-d1a7-3fe9-9d55-53218ab1edde | -16.63238 | -55.92026 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| bb525398-078f-361e-bb30-635d93ad5ade | -16.61939 | -57.21131 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 8596284e-ddb1-3998-956c-a9ea25f28852 | -16.59566 | -55.9087 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |


[Clique aqui para ver as próximas entradas](README149.md)
