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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67df2e61-ef4c-3af0-be60-5bf7f3036c68 | -6.1778 | -35.289 | 2024-10-04 01:15:40 | GOES-16 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| e6cb5d78-1981-399a-ae26-a54a3a672f72 | -5.9786 | -45.3847 | 2024-10-04 01:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b1946fa7-1564-3e34-9ca4-b87fa9d16507 | -7.8539 | -45.3611 | 2024-10-04 01:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e9f758fd-87db-3ec5-8f27-e975eea8d6ae | -7.8541 | -45.3384 | 2024-10-04 01:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b7ff1fcb-41d0-3ce9-b157-45772cda8185 | -8.3128 | -49.5679 | 2024-10-04 01:15:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a2e8c1c9-35d6-361c-b4d5-1b13b2f05482 | -8.6448 | -50.0518 | 2024-10-04 01:15:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 1c15cc67-f0f5-3a29-baad-5406fecac82a | -8.6492 | -66.621 | 2024-10-04 01:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 40db2f62-e8cc-3208-9900-7d03636da1c0 | -8.6677 | -66.6205 | 2024-10-04 01:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f5d22a23-b868-3d79-b678-a5d08c1f0aac | -9.1481 | -43.1611 | 2024-10-04 01:15:57 | GOES-16 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 30d2f1bc-5f1c-3b41-ae65-aefe3dec0b16 | -9.1158 | -51.5315 | 2024-10-04 01:15:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 71c3db14-3ee2-31f0-bd40-a45bb096e51c | -9.0162 | -67.3904 | 2024-10-04 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 954b06d9-4c6f-35dd-ba10-5adf2c50591f | -9.0347 | -67.39 | 2024-10-04 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b3b0375b-ba11-304a-a6f8-c151a601ed89 | -9.0898 | -67.4997 | 2024-10-04 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| df5d7bbc-4b73-3fa4-b5e1-5bdfd1245100 | -9.3115 | -50.8203 | 2024-10-04 01:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 217.0 |
| 99fb0344-d403-377a-9b71-a0ff09df5e50 | -9.3118 | -50.7991 | 2024-10-04 01:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 236.2 |
| 4391605e-4562-3693-82dd-11e14aca44bf | -9.312 | -50.7779 | 2024-10-04 01:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| dcb6825f-6fb7-3ed1-b2ab-84a7a8d5cf9b | -9.3303 | -50.8186 | 2024-10-04 01:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 026da0f4-bb78-3ee1-9a7f-84135e51a230 | -9.3306 | -50.7974 | 2024-10-04 01:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 751a5567-d82a-38a0-8f3d-ab1669172aa6 | -11.0532 | -46.5344 | 2024-10-04 01:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3bd3fb9d-cf23-3b11-a624-d4cedbf9144a | -11.0536 | -46.5118 | 2024-10-04 01:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 2897ca74-339a-31a1-97cb-5c74169fae3a | -11.0727 | -46.5093 | 2024-10-04 01:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 537567ca-e825-30b6-ab61-b8899f00eadc | -11.5425 | -65.0607 | 2024-10-04 01:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 977caaaa-078c-35b0-8cab-662cc2e0763b | -11.5991 | -65.0204 | 2024-10-04 01:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 64637c62-3614-3c27-bd1f-48bc793239fa | -11.5992 | -65.0015 | 2024-10-04 01:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f27d5836-3dc0-37b2-9f07-f753c22459aa | -11.6181 | -64.9818 | 2024-10-04 01:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4da24ce8-aebf-3d83-84cd-7c217abfce7e | -11.6369 | -64.981 | 2024-10-04 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ab303a50-3aae-36f5-b392-7d27d37c5979 | -11.6932 | -64.9785 | 2024-10-04 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 299e1f11-f5bb-30a7-83fc-d50d70c0f51e | -11.712 | -64.9777 | 2024-10-04 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 609274d8-2072-36f9-8d1e-75a5195efa9f | -11.8052 | -56.6024 | 2024-10-04 01:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| f5310b8a-cdcf-3f05-bd53-365c455080cc | -11.8242 | -56.6009 | 2024-10-04 01:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| a8cc90e0-36e8-35d8-a4b2-267830174771 | -11.8244 | -56.5808 | 2024-10-04 01:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 95ca1e74-223f-3edb-822c-3a75eaf9e20f | -11.9147 | -56.9539 | 2024-10-04 01:16:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 4e3268df-7a5b-310b-9c9d-2aee25144e78 | -12.5711 | -53.1171 | 2024-10-04 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 0b20b0b6-607d-3b36-b37b-d1cc16b7083a | -12.5898 | -53.1359 | 2024-10-04 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 167.4 |
| d51ffce5-851c-3a11-ab26-069abc01c6b2 | -12.5901 | -53.115 | 2024-10-04 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 269.9 |
| cfad5ebc-ee6d-300c-88d2-d92b3c8dbbc0 | -12.6092 | -53.1129 | 2024-10-04 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 233c2faf-3f9c-35eb-9e65-7e5b4c924f81 | -12.6295 | -63.1225 | 2024-10-04 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 9736c942-ef50-381d-ba23-92532ba97b1e | -12.6296 | -63.1033 | 2024-10-04 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 01cb337c-f89c-3e3c-ab7d-88ed3316c095 | -12.6484 | -63.1214 | 2024-10-04 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 71145d0b-2314-3f76-8c49-c8beb5afa2a2 | -12.6486 | -63.1022 | 2024-10-04 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| ee75f764-7fdf-30d1-906c-6e3d4c0f0c6f | -12.8049 | -62.497 | 2024-10-04 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 35e786df-420a-3d2f-b401-a8799a36106e | -12.8051 | -62.4777 | 2024-10-04 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 76f54976-76cd-3469-a022-2be47e6ef2cc | -12.8052 | -62.4585 | 2024-10-04 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 862cd143-8390-3b4d-baff-a54bfac40f1d | -12.8238 | -62.4959 | 2024-10-04 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5722a48b-253a-3f75-ac85-20d4e9e227cb | -12.824 | -62.4766 | 2024-10-04 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 269f98d1-9e6f-3a55-9705-1b2b90926882 | -12.8242 | -62.4573 | 2024-10-04 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 28e2eec8-e86e-3adb-b571-a8a552c69c22 | -12.881 | -62.4538 | 2024-10-04 01:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ec3f75fe-b800-33d1-b57a-baf08143ce70 | -13.1254 | -46.3063 | 2024-10-04 01:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 94a9251b-3b35-3d44-bcbc-db3121251e5b | -13.1447 | -46.3033 | 2024-10-04 01:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 65.7 |
| be606161-eda9-3019-9b1d-600477a245ae | -12.8999 | -62.4527 | 2024-10-04 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a7e7a1f6-3cd1-32b1-a5f4-f7f7ff16f2fd | -12.9186 | -62.4901 | 2024-10-04 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6c403d42-cb95-3704-80ab-ff89c2118dc5 | -12.9187 | -62.4708 | 2024-10-04 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c3fd436f-d633-35da-bbe5-815509e2b3bb | -13.0594 | -51.1409 | 2024-10-04 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 22e0d383-62e3-3571-81a9-d4da7d011209 | -13.0598 | -51.1195 | 2024-10-04 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| d4b01c86-9b99-3b81-9ef0-2404ad2b35a3 | -13.0786 | -51.1385 | 2024-10-04 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 0ff12f57-30a2-38b3-803f-61c264b851bd | -13.079 | -51.1171 | 2024-10-04 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3f960066-510a-371a-96a0-1328aa66f452 | -13.0975 | -51.1575 | 2024-10-04 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 501e8927-8385-3721-8361-bace2c973b98 | -13.1166 | -51.1551 | 2024-10-04 01:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 3be6c912-5f23-3416-b469-e04723d47775 | -14.004 | -44.0201 | 2024-10-04 01:16:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e464bd45-45a2-326a-a20f-8584788d2ebe | -14.7939 | -48.0275 | 2024-10-04 01:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 4b156b76-17ad-35b6-b6a9-6a1a2cfbade0 | -14.7944 | -48.005 | 2024-10-04 01:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| eb2ebbb5-8e6d-378d-b91e-7bf626994d95 | -16.0897 | -50.452 | 2024-10-04 01:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| b3680d42-ccbc-3520-ad06-2f7b879e5162 | -16.1094 | -50.4489 | 2024-10-04 01:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1e4e6faa-1796-3fbf-ad0e-06c06c6cc47a | -16.5783 | -58.198 | 2024-10-04 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 15d2f2fc-2ea0-3766-b576-c30cd5ec6d80 | -16.5925 | -57.2602 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 14d87af3-a1a7-3a52-b3e3-0058437a9a18 | -16.5928 | -57.2397 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| a3e4ec29-7327-33db-9d2a-cfab3d65cfc2 | -16.5935 | -57.1988 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 9c409ae8-a2f3-33fa-bf96-7b1414fcc491 | -16.5938 | -57.1783 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 52b76f28-fa24-34bf-92e2-53db02df1ac3 | -16.4148 | -57.4028 | 2024-10-04 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 539f7ac4-7af8-320e-a9f5-5313e9171dc7 | -16.4151 | -57.3823 | 2024-10-04 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| e8688e72-fb46-3ea1-8a2d-e0fbc089f61c | -16.4554 | -57.2962 | 2024-10-04 01:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| f3c3bc73-54d4-3b64-ab2b-144e30e9c0cc | -16.5537 | -57.2442 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| b017b629-04c3-36c8-8f78-7e09d95c2f41 | -16.573 | -57.2624 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 8a69e1b1-6009-3789-9d63-63effe7dbfbb | -16.5733 | -57.2419 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.5 |
| f6a12e32-2c73-3a49-8e48-355d8a0289ee | -16.5736 | -57.2215 | 2024-10-04 01:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| e72d10df-3231-3d05-a3d2-e3f92950964f | -16.613 | -57.1965 | 2024-10-04 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 55886602-1320-3f17-9b0e-50e46215c602 | -16.7411 | -57.7534 | 2024-10-04 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 29b05300-835b-3a2a-b9bd-4289264d6a4c | -16.7606 | -57.7512 | 2024-10-04 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| c2674a8c-61e7-3e08-a310-589a0b40eeb1 | -16.9296 | -47.1455 | 2024-10-04 01:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d58d2b46-eaf3-33df-973c-85409cba9a81 | -16.9302 | -47.1224 | 2024-10-04 01:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| c7e86457-0ad2-39d7-a317-c75a8a2264f7 | -16.6133 | -57.176 | 2024-10-04 01:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 4563decd-0cdc-3a3d-93cc-1f5a747df91b | -16.779 | -57.8306 | 2024-10-04 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 09200fb6-5b0f-3f10-bd47-e46f848eb358 | -16.7856 | -57.4015 | 2024-10-04 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 8ca7cd07-6e96-3311-8260-a6c719889c83 | -16.7859 | -57.3811 | 2024-10-04 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 157.3 |
| 32657062-a031-3a7f-a96e-900e4a18f91c | -16.7985 | -57.8284 | 2024-10-04 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| f8158d9e-8251-3386-a92a-08a5237328fe | -16.8051 | -57.3993 | 2024-10-04 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 7726afbb-ace6-36e5-8f9e-f30cc23fa63f | -16.8055 | -57.3788 | 2024-10-04 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| 8695f387-0bc2-317f-9938-adbf298f86b8 | -16.843 | -57.4767 | 2024-10-04 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 3de14f11-9819-364c-9b3d-e2ed0f3e3d6d | -16.9084 | -55.8638 | 2024-10-04 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 2397f6fe-49a3-3b82-b6a0-5782f1350a19 | -16.9087 | -55.843 | 2024-10-04 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 66d84ec5-1e5d-3f14-9975-14382afb05c2 | -16.9283 | -55.8405 | 2024-10-04 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 8753d543-4faa-3585-a698-318b50d9f635 | -16.9287 | -55.8197 | 2024-10-04 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 9597240a-14d3-35b0-9627-b130bc85d765 | -17.0616 | -56.0723 | 2024-10-04 01:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 441ec4b7-96b4-303a-a6ad-cea10f81a68f | -17.3643 | -42.6284 | 2024-10-04 01:16:42 | GOES-16 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 892f260f-fbd9-35c8-82e9-eb2a0083e26a | -17.3844 | -42.6235 | 2024-10-04 01:16:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 112.4 |
| d90e35c2-72e3-34d4-b630-1bc627c4364c | -18.0854 | -42.5976 | 2024-10-04 01:16:46 | GOES-16 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| efadb72d-98de-31af-aacb-12afb9fbcd6b | -18.8413 | -42.8985 | 2024-10-04 01:16:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.4 |
| 645f6f56-6516-36b8-9cb8-d875dacea97b | -18.8609 | -42.9182 | 2024-10-04 01:16:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| 59aff21f-fe63-3286-b4a5-51f98ebb1a8f | -18.8617 | -42.8932 | 2024-10-04 01:16:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.2 |
| f7e135b3-8c50-341c-ba77-cf91de9d78d2 | -18.8613 | -43.5837 | 2024-10-04 01:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |


[Clique aqui para ver as próximas entradas](README31.md)
