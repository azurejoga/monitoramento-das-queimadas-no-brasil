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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9c22868-6da1-3e76-ba51-3a43d9fd2c5c | -16.8698 | -55.8272 | 2024-10-02 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| f3d3cf3a-28f8-37a6-8248-252aab92e368 | -17.0705 | -56.7114 | 2024-10-02 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 0eb63267-c76d-3aab-aeed-511bbacb836c | -17.0709 | -56.6908 | 2024-10-02 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 9dea2bc2-c157-3e8d-899b-f360f4a86915 | -17.0902 | -56.709 | 2024-10-02 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| e1ac4b60-8117-3d2b-897d-a4ad0a782587 | -17.0905 | -56.6884 | 2024-10-02 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| f2d04319-88af-3f21-97a5-02bdc7474bc2 | -17.1002 | -56.1089 | 2024-10-02 00:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| a69043a2-d175-3470-9ee2-2ac24eea919f | -17.1098 | -56.7066 | 2024-10-02 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| fbbeff1b-c3fd-39d6-adf9-37c5ca601d72 | -18.7769 | -46.5732 | 2024-10-02 00:06:50 | GOES-16 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 36b36de1-c8c0-3a37-a0d7-e9937dfd1340 | -19.2519 | -46.8641 | 2024-10-02 00:06:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 37b207b9-0b74-3fce-8235-be4137491ef9 | -19.7618 | -41.9953 | 2024-10-02 00:06:54 | GOES-16 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| eae1c3fa-ebb8-3fe8-a7a5-72162e6ccad9 | -19.7824 | -41.9894 | 2024-10-02 00:06:54 | GOES-16 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 132.7 |
| 602043d9-a990-3eda-b004-a868d1d58bb6 | -20.0238 | -42.7271 | 2024-10-02 00:06:56 | GOES-16 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| ab56f43d-9fbd-359e-8e42-d2fe4e52fb7b | -20.0246 | -42.7018 | 2024-10-02 00:06:56 | GOES-16 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| de790898-5956-3b84-8f69-8ca62f57d561 | -19.9921 | -55.4728 | 2024-10-02 00:06:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e57bc239-dc51-3f2b-8cb0-2f77a17d7035 | -20.5252 | -46.3263 | 2024-10-02 00:06:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 587ae1a5-e2dd-3df5-9c54-fe39a4dc39c4 | -20.5259 | -46.3023 | 2024-10-02 00:06:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 734b7051-d552-36ef-9103-4a4f7c6ef155 | -20.5266 | -46.2783 | 2024-10-02 00:06:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 55.2 |
| c5a3bd01-0770-3e87-995d-764963fa8768 | -21.4175 | -50.9759 | 2024-10-02 00:07:04 | GOES-16 | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| aed0b727-e81f-3c2e-9b06-c9498254e3f0 | -21.4381 | -50.9716 | 2024-10-02 00:07:04 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| 108b5acf-e60e-3696-bc19-ad3c248c2996 | -21.3456 | -55.6841 | 2024-10-02 00:07:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 54238cd1-2340-36ff-a226-465ab2048da0 | -21.6275 | -50.796 | 2024-10-02 00:07:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.1 |
| 796a960b-06b3-3a66-9bed-dd2a2cf4dcc3 | -22.6275 | -42.1643 | 2024-10-02 00:07:09 | GOES-16 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| e573a04b-8732-3f6c-8d1c-d8f3e9a885c9 | -22.9277 | -43.7243 | 2024-10-02 00:07:11 | GOES-16 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 89.8 |
| b26ed084-9514-3b2b-b1cc-99eb4e873fe4 | -22.8803 | -45.0842 | 2024-10-02 00:07:11 | GOES-16 | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| 70d652af-edb8-3d95-be53-f68ad7d1cf15 | -22.9006 | -45.1029 | 2024-10-02 00:07:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 195.5 |
| 1ae8b5f4-c461-379e-8a12-004d6e0e44d1 | -22.9014 | -45.0779 | 2024-10-02 00:07:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.6 |
| 7a177590-e753-368c-aa03-8ac50ebeabab | -22.9217 | -45.0966 | 2024-10-02 00:07:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| 9c24d80e-767b-30cb-9953-841e345e9496 | -22.9226 | -45.0717 | 2024-10-02 00:07:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 1688b4c5-8f5d-3560-86b7-c7a6d3df2e84 | -3.128 | -49.4235 | 2024-10-02 00:15:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c1adfd28-decb-3bd9-b730-ddadfd1d657c | -3.2136 | -46.7843 | 2024-10-02 00:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 13478d62-1534-3f74-b272-505e1e5b3239 | -3.386 | -54.1187 | 2024-10-02 00:15:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 35543f1f-207c-3d78-9b32-bce97fb73ed5 | -4.4468 | -42.9123 | 2024-10-02 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 3a11c1fe-3277-343c-8435-3930e21dc228 | -4.447 | -42.8889 | 2024-10-02 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7a330b9e-d3b3-3b7c-b025-b7db85d75daf | -4.4655 | -42.9112 | 2024-10-02 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| bf746e8d-845b-3c08-aaed-cf804ade0638 | -4.4657 | -42.8877 | 2024-10-02 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 222.3 |
| e836919b-3cee-346f-90e2-3a81ffd47977 | -4.4844 | -42.8866 | 2024-10-02 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4564aeca-993d-396a-a640-4a33f0d3240d | -4.4679 | -48.127 | 2024-10-02 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 7881b830-d508-3b10-95b2-672748ac9c4a | -4.4681 | -48.1054 | 2024-10-02 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2951ec37-a6d7-31ec-bf25-982c52ea2617 | -4.4865 | -48.1261 | 2024-10-02 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7ee3d9c6-f79f-325d-99f1-5784f93c0b4f | -4.4866 | -48.1045 | 2024-10-02 00:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8017febd-0f14-32c1-b310-ad8889874150 | -4.58 | -48.0132 | 2024-10-02 00:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 789975b1-3048-3a2d-9382-85a9f1eee8fa | -5.9036 | -45.4127 | 2024-10-02 00:15:39 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1de0cace-cafe-3113-9279-3001f6fb1c0a | -5.9038 | -45.3901 | 2024-10-02 00:15:39 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 6ad55fcc-9b11-33e9-8c32-ca64ae2353ba | -5.9788 | -45.3621 | 2024-10-02 00:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6b850288-e3f0-3407-88da-cfabdeae6c15 | -6.1371 | -46.4706 | 2024-10-02 00:15:41 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 865374fa-f08d-3eae-9b58-c9128a8d5ad3 | -6.1373 | -46.4484 | 2024-10-02 00:15:41 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8a9b2b34-89ba-3738-9f63-57e067cf4d37 | -6.9459 | -42.5048 | 2024-10-02 00:15:45 | GOES-16 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 31abb173-17f2-3df1-a70b-3675093abbce | -7.1796 | -46.9444 | 2024-10-02 00:15:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 78a5139b-8d30-3803-a231-9d8a8f3eadc7 | -7.651 | -67.2009 | 2024-10-02 00:15:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ac73bcd3-e34b-39a1-9ae8-3a8c61413647 | -8.205 | -44.365 | 2024-10-02 00:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 7cdbca68-f496-34d6-aa0c-9969ee40f883 | -8.2053 | -44.3419 | 2024-10-02 00:15:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 46d792d8-f414-3889-9d81-6ffd70d355d2 | -8.4642 | -62.7313 | 2024-10-02 00:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6eaf0f3d-2c42-3b2f-891d-f1eea6133f66 | -8.4643 | -62.7124 | 2024-10-02 00:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a21dc002-19c8-3d2e-8041-a0e86aae00eb | -8.6844 | -45.2309 | 2024-10-02 00:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| e8f65d8f-203b-37a9-ad28-289a6362baa1 | -8.7033 | -45.2289 | 2024-10-02 00:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b47261da-c994-3753-994e-15f4114b3957 | -9.5821 | -50.2011 | 2024-10-02 00:16:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 7b86d242-74cc-342d-8c08-2b5ee0b107d0 | -9.5397 | -62.8195 | 2024-10-02 00:16:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6564e2ba-2ccb-33ca-8bd0-a97c0627e590 | -9.5398 | -62.8005 | 2024-10-02 00:16:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 1c932528-f9b1-335a-a354-a8627f6cb7ac | -9.5583 | -62.8187 | 2024-10-02 00:16:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 68a37f5d-0505-3866-a51f-e534475239e0 | -9.5584 | -62.7997 | 2024-10-02 00:16:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 10c07c4c-585f-3e8e-9a99-08664501771a | -9.9367 | -64.9179 | 2024-10-02 00:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 265.9 |
| 8c78b705-2011-3ac6-84d1-60d97eda19a7 | -9.9368 | -64.8991 | 2024-10-02 00:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 243.3 |
| fe22186e-3d9d-3d2d-9e17-4617add1b7dd | -9.9553 | -64.9172 | 2024-10-02 00:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 275.5 |
| 31754d0f-6cc5-3b6e-92cd-ce16c17d8ec0 | -9.9554 | -64.8984 | 2024-10-02 00:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 293.6 |
| 32a99a08-895c-35a8-835d-f8860c0fbdc8 | -9.9747 | -64.7661 | 2024-10-02 00:16:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 446330f2-379f-3f57-adf5-038c00185b6d | -10.1089 | -67.8999 | 2024-10-02 00:16:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 59.9 |
| eff27b85-41eb-3f1d-98e9-e0d3d9ca470b | -10.109 | -67.8813 | 2024-10-02 00:16:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 62c75a14-1705-39aa-ab29-48d0a8779012 | -10.1275 | -67.8994 | 2024-10-02 00:16:04 | GOES-16 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 3a1f65d0-e591-379d-98b6-81076d00bcca | -10.626 | -55.8752 | 2024-10-02 00:16:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 3010e046-7829-38af-a875-c55757224917 | -10.9044 | -50.1304 | 2024-10-02 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b4b9a6de-91f9-3af5-a4ad-950127ef2eef | -10.9234 | -50.1284 | 2024-10-02 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 9e1727b0-32c6-3cd0-9f7d-8e2c363ca843 | -10.9237 | -50.1069 | 2024-10-02 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 87501201-5705-3901-b4a6-d6568462b830 | -11.4822 | -56.7892 | 2024-10-02 00:16:11 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 444d8ff1-cafd-31c6-a6e9-91dea7b8a8b3 | -11.884 | -43.8142 | 2024-10-02 00:16:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 60d85fb9-5350-3ee2-a347-acdcc993c7d8 | -11.6555 | -64.9991 | 2024-10-02 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| be9af6ae-ae0f-3b6c-800c-d079cc630966 | -11.6556 | -64.9802 | 2024-10-02 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| dfda683f-62ad-36d5-9244-0fe39db3cff1 | -11.6743 | -64.9983 | 2024-10-02 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f0c32a54-dad9-330f-9b79-eb34406b2a3e | -11.6744 | -64.9793 | 2024-10-02 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b11f5c44-3628-32c7-ab86-f1c676c4b6d6 | -12.1406 | -50.0524 | 2024-10-02 00:16:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 05b19a97-875a-3c85-a8b7-609d396526c9 | -12.1597 | -50.0501 | 2024-10-02 00:16:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| acea4cd7-d57f-333c-88c2-6857d6cdad63 | -12.4433 | -43.7242 | 2024-10-02 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 19826508-bf5f-3f98-8dfb-f8729104c2ec | -12.2754 | -47.6473 | 2024-10-02 00:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 739ba624-502c-3a1c-a947-da13b2239f69 | -12.2946 | -47.6446 | 2024-10-02 00:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 1215dd92-3927-3d5d-9e86-fb1df11ac3de | -12.6484 | -63.1214 | 2024-10-02 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 150.4 |
| f35987bc-ed82-359a-b9af-79cf3947f8b8 | -12.6486 | -63.1022 | 2024-10-02 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 40e7af6e-7353-3a43-8165-b5a4d7db30fe | -12.7054 | -63.0798 | 2024-10-02 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e34f2b29-11f7-3f81-8090-666e90075717 | -12.9574 | -51.5369 | 2024-10-02 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7477ab35-1a1a-31c5-ae7f-09cb1247d37b | -12.9578 | -51.5156 | 2024-10-02 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 253f66be-061f-36f9-8d87-3ffa0aeec3b9 | -12.8593 | -62.7826 | 2024-10-02 00:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0587fe1e-e1db-3c48-85f6-ffe577fc6af8 | -12.8782 | -62.7815 | 2024-10-02 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| d4002157-8ee7-3bc7-9ec8-e9c4d0f6fa13 | -12.8784 | -62.7622 | 2024-10-02 00:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ad905b04-74be-3ef9-ab33-143b1a28a002 | -13.2177 | -48.6019 | 2024-10-02 00:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b75b8b64-e90b-357f-b95e-33f00a675e87 | -12.9167 | -62.7022 | 2024-10-02 00:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0bc1922c-b262-3494-8f3f-5beba653dd55 | -12.9357 | -62.701 | 2024-10-02 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 63d8fe44-a709-3174-9804-9ac58264ee7e | -12.9358 | -62.6818 | 2024-10-02 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 170.4 |
| 78586d4c-376d-3390-a07d-88dddccebbd4 | -12.9546 | -62.6999 | 2024-10-02 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 96.0 |
| d45965fa-529b-3f17-a6e8-52724552a599 | -12.9548 | -62.6806 | 2024-10-02 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 191.6 |
| e3463e7b-b25f-32ca-ac49-3513d84e3c6e | -12.955 | -62.6613 | 2024-10-02 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5a229cc1-a468-3f6f-8c53-905bbcba227c | -14.7986 | -48.7628 | 2024-10-02 00:16:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 84b21fc8-d885-3afb-bf81-20f7c35acc5e | -15.139 | -55.8285 | 2024-10-02 00:16:31 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |


[Clique aqui para ver as próximas entradas](README3.md)
