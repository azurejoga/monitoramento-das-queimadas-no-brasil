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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0284b5f-40d2-3879-a00a-76a1ef74991b | -16.8491 | -55.892 | 2024-10-02 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| fe307acb-61bf-343b-b3b7-c3a97d5e317b | -16.8695 | -55.848 | 2024-10-02 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| c321be6a-f677-3b3b-b997-1d27dd887e79 | -17.1577 | -56.1844 | 2024-10-02 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| f2ae6df5-81e1-3bb2-b9e8-5063b6ac00f1 | -17.1581 | -56.1637 | 2024-10-02 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 31989140-4add-3662-8815-e22173ef0791 | -17.0502 | -56.7551 | 2024-10-02 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| b0796180-f348-3791-b9e6-2f44caad4d58 | -17.0705 | -56.7114 | 2024-10-02 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 50a67c36-06c6-3f38-ad56-8e42c430cc9b | -17.0709 | -56.6908 | 2024-10-02 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 65f67f2f-ae5f-3699-889a-1b88eda97969 | -17.0892 | -56.7709 | 2024-10-02 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 9db24b90-6366-3fca-bfd3-4ce8e32c3fc9 | -17.0895 | -56.7503 | 2024-10-02 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| d8d814ca-fad7-3665-a750-a20d264644a9 | -17.1091 | -56.7479 | 2024-10-02 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 04b99e70-d221-3884-885d-4f4c4d689812 | -8.7597 | -66.606903 | 2024-10-02 01:26:42 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5d9ace0-d8da-3df1-b609-288a044c4c83 | -17.196 | -56.2417 | 2024-10-02 01:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| bad8a920-b394-3b2f-8a4b-1f3fc7b507ce | -17.1964 | -56.2209 | 2024-10-02 01:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 3df9b3fd-e8cf-3417-8660-4f87196e9c88 | -6.7098 | -59.123001 | 2024-10-02 01:26:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a46dcf0-743d-3ecd-8d4e-f4f35d7bded5 | -6.7114 | -59.130001 | 2024-10-02 01:26:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec801ce-ef9c-3e22-a0b8-fc4fe58a21cc | -19.2317 | -46.8687 | 2024-10-02 01:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 125.3 |
| cf132f6a-4999-3cb2-b32d-18cceeb8c959 | -19.2323 | -46.8452 | 2024-10-02 01:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1875a04f-6f8e-393d-8fed-3eda4eab6569 | -19.2519 | -46.8641 | 2024-10-02 01:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| e8f2a756-004a-3e6d-b34a-a48a0adb66b9 | -19.2526 | -46.8406 | 2024-10-02 01:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 624d29bf-9f6e-3268-878e-a473a5d34609 | -20.0424 | -55.9738 | 2024-10-02 01:26:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| c399a08d-a48c-39db-9513-b8d5c052ff46 | -20.6699 | -51.4641 | 2024-10-02 01:27:00 | GOES-16 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.8 |
| 498dd72c-7689-3fd2-91e5-8a94a1c37aba | -7.6372 | -67.193802 | 2024-10-02 01:27:02 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8b12da0-4fef-3ebf-821b-0423e198835e | -7.6329 | -67.172997 | 2024-10-02 01:27:02 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9719db6-d782-37eb-9a91-7566583fe489 | -21.3456 | -55.6841 | 2024-10-02 01:27:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 95.6 |
| bde49872-053c-38f2-8cab-6cf4936237a6 | -21.6275 | -50.796 | 2024-10-02 01:27:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| d15c3ff1-3306-3e5a-9236-93ac53a29d09 | -22.9006 | -45.1029 | 2024-10-02 01:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.0 |
| c59d737c-a589-314a-84bf-54d60081a8ce | -22.9014 | -45.0779 | 2024-10-02 01:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.6 |
| cbe49aaf-1b30-35ce-ac3d-a12711ae09e7 | -22.9277 | -43.7243 | 2024-10-02 01:27:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 92.2 |
| c40be905-1580-370b-9c15-88eb1416dd06 | -23.5226 | -47.213 | 2024-10-02 01:27:14 | GOES-16 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |
| 681783ee-8128-342f-8014-8bc9c0c56f6a | -8.48486 | -46.84983 | 2024-10-02 01:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 67fcb302-6568-3bb8-862f-b464a20ccf0d | -8.48396 | -46.87371 | 2024-10-02 01:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 53994eba-01b0-3fa9-89b5-7b6d1143f695 | -8.47899 | -46.84437 | 2024-10-02 01:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| eac48399-3e89-3728-99da-9a20af463a13 | -3.22146 | -46.78378 | 2024-10-02 01:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0bfa7a78-e489-33ad-9cf8-4a2b956c5bc1 | -7.1889 | -46.95556 | 2024-10-02 01:28:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d03c9137-759d-3794-aa97-96225779a7ea | -7.18708 | -46.98331 | 2024-10-02 01:28:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ebc3bbbd-df15-3c82-b82c-6100517ed8ff | -7.18157 | -46.9507 | 2024-10-02 01:28:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 2684706b-0f55-31ab-8cf6-6e65e1f42ac1 | -7.17302 | -46.95854 | 2024-10-02 01:28:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 07d10b43-22ed-31bd-aba8-17241d798fa7 | -4.58095 | -48.01779 | 2024-10-02 01:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 96993c27-1a10-39c1-9db6-e6d40e2d3232 | -4.49129 | -48.12925 | 2024-10-02 01:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 8b24626e-63d1-38cb-8b6f-53ddab873163 | -4.47599 | -48.13151 | 2024-10-02 01:28:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 55f1534e-19c3-36e1-8950-e62b38d9fe0e | -9.59653 | -50.2091 | 2024-10-02 01:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 07175565-001c-38d5-ad6f-ec44b47106ea | -9.59389 | -50.19247 | 2024-10-02 01:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d658ecdd-24f6-3f7c-96c3-baac3ac5f68f | -9.58209 | -50.19441 | 2024-10-02 01:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 72c46780-287e-3c17-8bac-dddb8f26d0ca | -9.56761 | -50.17966 | 2024-10-02 01:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1e64ebf2-c37b-3f67-91ca-aed4bcc4009e | -9.56145 | -50.18717 | 2024-10-02 01:28:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 36764484-7eb1-35b5-b17d-98def3329d52 | -9.06802 | -53.25628 | 2024-10-02 01:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7b4af4fa-7b1a-3959-9263-97ca9c3c09c0 | -8.96358 | -52.81937 | 2024-10-02 01:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 794b8b29-b016-38ca-82c8-4886ec62fc86 | -8.96191 | -52.80825 | 2024-10-02 01:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ed0fc07f-a71d-300f-8d4c-e7e6ab56c670 | -10.39303 | -52.92812 | 2024-10-02 01:28:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 529ce46d-d298-3416-8752-e0a42f25a11d | -6.58298 | -52.93177 | 2024-10-02 01:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 924971ac-87a6-3220-a920-9b6a3a2387cf | -6.58122 | -52.92001 | 2024-10-02 01:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d55f628a-9749-34f6-b9f4-f71861920098 | -6.57275 | -52.92718 | 2024-10-02 01:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 986ebe8c-b439-312a-bf42-1cc4a78f4311 | -10.61441 | -54.06562 | 2024-10-02 01:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8822e550-e02c-360e-bd7f-078e69d42d12 | -10.23533 | -54.2489 | 2024-10-02 01:28:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a9ab6c8-143e-3dd4-83c1-28f279274b95 | -10.63167 | -55.88555 | 2024-10-02 01:28:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4ec6bee-44e5-364e-b86f-59e03932ace2 | -10.63043 | -55.87656 | 2024-10-02 01:28:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 313a0eb8-c840-3709-9c07-7c5510e7722b | -10.62281 | -55.88685 | 2024-10-02 01:28:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| fd7a919e-e573-382a-80f3-9e2d53d646d3 | -10.62156 | -55.87785 | 2024-10-02 01:28:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 7ef38fc3-5a5b-3eb3-a8c1-97c2106e523a | -11.66024 | -65.01668 | 2024-10-02 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.9 |
| e04e80c8-ac5e-3a8a-bcca-51d68c5613ec | -11.66596 | -65.01125 | 2024-10-02 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c7641c54-a79a-3b52-8293-5dcd3d6ee5b5 | -9.93381 | -64.89292 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 279bb1af-d4aa-3a0b-bf19-7b3132c2b050 | -9.93769 | -64.92681 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 231.0 |
| 4f0450fe-d20f-35a8-92f6-6d73c0d49e3f | -9.94989 | -64.89101 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 8b6be0fe-98e6-3b3f-befe-08b6aadddf07 | -9.95382 | -64.92493 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 13111c37-c3f2-3081-b7dd-85649cdde1c3 | -10.99022 | -63.95812 | 2024-10-02 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 27d5bf5e-e5b6-3ed6-969b-dade90f0f5aa | -11.55079 | -63.82866 | 2024-10-02 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| bec72b85-381c-35ba-8bd0-1a2aa4170256 | -11.56259 | -63.79741 | 2024-10-02 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 789fe823-0ccd-3140-9bf2-eea46df95776 | -11.63232 | -64.02557 | 2024-10-02 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 57ac3d76-7a1a-35c3-9e23-99a6c4aa7b67 | -9.54195 | -62.80455 | 2024-10-02 01:28:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 403e444d-50f9-3a7e-84c9-dae961208255 | -9.5446 | -62.82742 | 2024-10-02 01:28:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 1cc81ae6-053e-3ffe-838a-71fa0e06fa2a | -9.54804 | -62.80921 | 2024-10-02 01:28:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 3f378a79-1603-3b6b-a44f-06c508c011ab | -9.55928 | -64.25838 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.9 |
| bc81729c-dda3-3905-84c6-97d474cc4db6 | -8.45599 | -62.72808 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 296f7736-5b0c-3b52-861a-c58bf9058dac | -8.46561 | -62.72129 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 34454718-a7f3-38fc-ab4b-6c0ab02ca57b | -8.46821 | -62.74271 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ceceb3b4-15f3-3c4b-be87-3e28586ad73b | -8.46924 | -62.72637 | 2024-10-02 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 6da2826f-690a-35da-99d9-7de4f7cf6618 | -10.63481 | -62.80994 | 2024-10-02 01:28:00 | TERRA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 193dee2a-604c-3562-91cd-db221c610682 | -10.64256 | -62.81449 | 2024-10-02 01:28:00 | TERRA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 1e035ddd-a163-3eb4-b199-f5fb0c3f20b9 | -11.24738 | -60.60713 | 2024-10-02 01:28:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f80214f1-411c-3472-a15b-afca69cdf5bd | -11.25894 | -60.6048 | 2024-10-02 01:28:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| afb42d03-0b28-384b-94f3-e1f338c39ef7 | -9.39142 | -61.0382 | 2024-10-02 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b5569cac-b49d-35ba-bf7c-837abd984f8d | -9.39348 | -61.05448 | 2024-10-02 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 11339ec3-5ae3-3702-94ea-047852566a30 | -9.92505 | -59.90538 | 2024-10-02 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 02410e2d-5d1d-3be8-959c-99b6988560bd | -9.92846 | -59.93288 | 2024-10-02 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 23d36a2d-9c3f-31e6-ba63-e5a1838fa699 | -6.71502 | -59.12218 | 2024-10-02 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ae97a0c0-6ef1-3806-9183-73e215edb79b | -6.71646 | -59.13313 | 2024-10-02 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| ee0c7822-75aa-368f-b1fb-ca5e595b3be7 | -10.71783 | -58.51433 | 2024-10-02 01:28:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dabeff20-f671-3b73-8798-8ab2f092fb07 | -10.71931 | -58.52567 | 2024-10-02 01:28:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 7c1e3677-c61e-3a22-bebb-bb761b7f08de | -9.19625 | -58.20005 | 2024-10-02 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b692f036-dc03-3907-8a5c-9dee49cda94c | -9.19763 | -58.21048 | 2024-10-02 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d23444a9-26f9-36a5-ae18-d5670437593e | -10.13454 | -56.76152 | 2024-10-02 01:28:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9903c6c7-f732-3684-8244-7b34f1f03483 | -10.32805 | -57.50883 | 2024-10-02 01:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3e722a23-9c0f-3985-881f-9fc152bad942 | -5.32226 | -56.00532 | 2024-10-02 01:28:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 77803cd0-97af-3389-aa6f-50fff0c4fcb3 | -2.65892 | -54.6228 | 2024-10-02 01:30:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ab1c9d15-b0ac-3262-8c95-d7fc3fd7cc00 | -2.8199 | -57.75872 | 2024-10-02 01:30:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb3b9f3f-c880-3770-8d60-e243bc11eb96 | -3.2136 | -46.7843 | 2024-10-02 01:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 9efb562c-39eb-3b59-af6e-583875ca9e98 | -4.4657 | -42.8877 | 2024-10-02 01:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b27817d7-7c41-3db8-a8c3-c21f9f2e2e55 | -7.1796 | -46.9444 | 2024-10-02 01:35:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 93491b4e-5e6a-39a4-9830-74cf5629b157 | -8.205 | -44.365 | 2024-10-02 01:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5f8e8fb9-af6d-38fa-91ab-dcdbf6fce8d5 | -8.4643 | -62.7124 | 2024-10-02 01:35:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |


[Clique aqui para ver as próximas entradas](README39.md)
