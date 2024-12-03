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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a5e2064-61b4-31bd-aa2e-613d5973815c | -3.17799 | -54.33334 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38eae1e7-3e72-3962-b379-d365dabac907 | -2.76932 | -55.35769 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a156280e-9412-36fc-9680-a7f4eb54572d | -2.82836 | -51.83941 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5adaaa07-bf02-30bf-adc6-01e5d6f2f264 | -12.70765 | -58.20477 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab9910df-0a5e-3522-8632-14d03346da25 | -4.16542 | -48.19548 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a7a1b88a-2d6d-3091-9391-37423d3a8fd1 | -3.26507 | -53.65104 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ca9e3ba-4369-3bec-a7de-0df975a277a6 | -1.73125 | -52.77847 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0d0b176-2452-3a89-88ce-4020adf3f477 | -3.25542 | -53.65131 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aec1f1ef-cdd3-3ab9-870e-b97fdcfe616c | -2.89611 | -51.79689 | 2024-12-03 05:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dab0761-002d-3c0a-8bb7-34e78180cc1c | -9.66193 | -62.44377 | 2024-12-03 05:25:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c03a23e2-b011-3415-b0c7-ea83d8107f96 | -3.29407 | -53.66562 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff2de19d-792b-3946-96b9-49b4b69a8e19 | -3.55271 | -51.51739 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f09966b-a52c-37c8-9960-2a71552b2dbe | -3.41443 | -53.22876 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5efad78-2dff-3964-95dd-f9ff4a4d93b8 | -4.16563 | -48.18971 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c7e74291-f817-3686-aab4-46d5efc6c815 | -3.08219 | -53.37312 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0b64c963-f930-35cd-88db-65ad9cd37b15 | -3.26574 | -53.64666 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e09b4c4-42be-395f-b4a1-26057c10033d | -3.11388 | -53.75641 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f028e4f-da39-339b-85da-0e83306b5b4c | -2.56814 | -53.39965 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de36bec0-2073-3f1a-8dea-5469f94b8d8f | -3.25736 | -50.61328 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e666a27-c34b-3583-bf6d-40f9783382b3 | -12.57432 | -57.80619 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c2255cb6-0ccc-357f-af6b-5a476fa2ffc1 | -4.16291 | -48.58601 | 2024-12-03 05:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5d9cbf1-0ed6-32be-b5f2-9cddb6623ef4 | -8.80995 | -64.26792 | 2024-12-03 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cd68955-94a8-3976-b723-aab93e6bdc23 | -3.25444 | -53.63157 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a95d999e-1993-3404-bb83-f1693cd3ee24 | -3.10508 | -53.28394 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0be50a62-fbb2-3481-87be-6a08285d1c86 | -3.25035 | -50.62293 | 2024-12-03 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afd56a49-b1f4-3c04-aa7c-b38215cb40bc | -1.75976 | -52.80702 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1233233f-d534-3395-b1dd-05d654aec980 | -2.82532 | -52.58522 | 2024-12-03 05:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17b8624a-6e2c-3c89-8e69-c56a1b6988b9 | -1.10762 | -54.18623 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 489f028a-e0c5-3d78-a534-46a3b890b581 | -12.5691 | -57.8154 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf393e9c-59e5-3e88-962f-8e8541a3d215 | -3.25985 | -53.62067 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08243af5-b3cc-347e-ad59-9d75c7cc27bc | -4.05456 | -47.00056 | 2024-12-03 05:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ed0eec0-c7a6-3583-a39f-2fc8a4e9aa0f | -1.76194 | -52.79291 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4deeb59a-d04b-35dc-8352-bfeace5488c4 | -1.78771 | -52.74845 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e2e6ac1-58ec-3da2-b554-1e449e4ed357 | -2.56302 | -53.40341 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0d35b3e-fd4b-3f98-8710-7b7812049c87 | -3.25417 | -53.65999 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0cf371be-f8f8-32b1-a288-6c6b61339d57 | -12.70947 | -58.21925 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd7b0ad3-f60f-352e-a322-bab8147f4f1a | -2.44164 | -53.61545 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 562d3be8-219a-351f-93b2-8fbf9f499bfe | -2.20949 | -53.78038 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 17ed0a4d-9f77-3cfa-bed3-342571be1516 | -1.73197 | -52.77375 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b8ca2ea-d93e-382b-ae25-560354bf68e0 | -3.21424 | -54.23478 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9850a40b-a056-3805-8165-dd0c305b15b0 | -3.26301 | -53.63022 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e6b15df-4d8f-369a-9b51-9e355b0c9d5e | -8.96678 | -63.64064 | 2024-12-03 05:25:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c226a886-edf3-39e0-97d6-a40aff92278f | -2.60903 | -54.22964 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 204a2cde-4750-39a5-869a-0cc84a4a91b9 | -2.80727 | -53.05179 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9e211a8-74ad-36b0-a4bd-64b2b77c1317 | -3.0285 | -53.42426 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54d2b337-2b64-3daf-a4c9-b80f81b8321e | -2.39301 | -59.994 | 2024-12-03 05:25:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0167f970-12ce-35da-8558-87abfbc7aded | -9.8932 | -60.7913 | 2024-12-03 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6aa99ac-2b84-335a-892b-966605df7ad0 | -3.25605 | -53.64696 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00097e3d-ac57-348b-b057-78b284f6ee1c | -2.78886 | -55.36201 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c129b69-12bf-3d47-97b2-c7ae8b6cab7e | -12.43008 | -57.81207 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be847677-add8-38a8-bc35-09a958988498 | -2.26582 | -53.61447 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40f121e7-3f5a-369a-8956-421e74c6f341 | -1.8824 | -53.29367 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f84314f-3673-3a95-b801-34d96248e705 | -2.33875 | -53.81559 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84b950b5-26e5-3e3c-b455-7f98fe3f4875 | -2.30676 | -53.91019 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 222b8069-cd4b-39bb-883e-02d534c9e884 | -12.70387 | -58.20425 | 2024-12-03 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb90790c-9f09-3626-ad6a-130e269a3ce1 | -3.29915 | -53.66187 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 34790327-1e63-3234-b1e9-d2cbe8321820 | -1.74237 | -52.64345 | 2024-12-03 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a426701a-e90a-38b1-8c71-e3348914188f | -3.272 | -50.20534 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e82a5a4-69cc-36f4-88ab-52c4de438100 | -2.86022 | -54.05975 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a0a9fc5-403a-351f-b8c2-a42fec4a5f25 | -3.01823 | -54.03913 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19e86c14-d988-323e-91f9-e9bcda184d2d | -2.88369 | -54.21646 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fcb9987-09e5-3e1d-b653-96a82f81868a | -2.74332 | -54.17228 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fd1d464-1b68-3f04-be4c-b3f3012dbcbc | -3.10043 | -54.12508 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd40aba7-6ef0-3ddb-bc74-78281426b53d | -3.05406 | -54.49743 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80185296-16f9-3801-9f9f-07f094f52c5c | -4.17047 | -48.2018 | 2024-12-03 05:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c3722a2b-361b-330f-89e8-0f4891f0d7f6 | -3.18642 | -54.33477 | 2024-12-03 05:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 105ed0e9-9244-37ce-b473-ba28dbc22463 | -3.2602 | -53.62353 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc09f688-5d96-388d-8f16-1c150ad03ae3 | -2.7764 | -55.36386 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 264534b5-b4b4-370c-92be-61b1fd92111b | -9.5154 | -62.93805 | 2024-12-03 05:25:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03863acd-fdd1-38e0-8314-7d66a9a4f81e | -2.80269 | -53.05107 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b74e7561-d586-36ee-a654-9971f0f97809 | -3.10618 | -54.05611 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e818abf5-a8fc-3bff-a475-f0a8535e85ab | -3.0867 | -53.37373 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 61ccac78-e719-3509-aecf-17da4d9e7d1f | -2.54574 | -53.4067 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e2e8dad-1f90-364b-848f-b894d925bca2 | -2.80413 | -53.04168 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e63691ab-9aae-347d-8a86-42e8c66a7f66 | -2.74082 | -54.10356 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf4fbc8f-c601-37ff-8c12-2afbabcf917e | -3.25311 | -53.64035 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f29fa76-5e12-332b-b03d-552685b64edf | -2.76776 | -54.12315 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5a657be-55ef-3940-b2a7-ffc25fc38621 | -2.98485 | -53.89339 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a656966-fe48-3ccb-b1af-ae2f84458d53 | -2.36125 | -53.92678 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81ec6bf9-df17-3445-8a91-1fa9e4c8c8f6 | -2.9787 | -53.87542 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2492955a-8b70-330a-94ea-759fa3b3e4da | -2.58025 | -53.67984 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fd8bea8-096b-3056-963b-ebb549f29be9 | -1.10976 | -54.11815 | 2024-12-03 05:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ace816d-a481-3a3f-a3be-84841a9014cc | -2.34063 | -53.80331 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d565862-e4e6-3844-bae7-47ef5f7259d5 | -3.86436 | -50.8989 | 2024-12-03 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed772992-870f-3b5a-9be5-5df0b20ab04e | -3.08534 | -53.38263 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d9bc1741-b41e-3f8b-a087-a95c498ccb56 | -3.10511 | -53.75507 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 997cb070-7ee0-3eee-a5ee-5c5cdc134381 | -1.39868 | -60.1092 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6325b757-a32a-3469-9de4-a55606c5629b | -10.34936 | -57.25286 | 2024-12-03 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8606762e-dea9-38c0-a8c3-636ce391e3a6 | -1.5186 | -60.32266 | 2024-12-03 05:25:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 245ae69f-6bb1-33e6-b6d3-a3dc5284c5bd | -3.10449 | -53.22705 | 2024-12-03 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7dfa8d50-42fd-314f-bc87-e48aee6f97aa | -3.06864 | -51.26647 | 2024-12-03 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 877048b3-fad6-326f-a668-c0eaa8e9d894 | -3.2719 | -53.63142 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ad98125b-1922-3829-bd44-3cbd82fc1e8d | -0.70411 | -63.2169 | 2024-12-03 05:25:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d40fb30d-ace8-316e-96b5-a42ab71cba8c | -3.3301 | -53.5451 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d0ccd23-14f5-314b-bf90-cfea6caaf18e | -0.70196 | -63.22007 | 2024-12-03 05:25:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7febb4f7-347d-3081-b349-8a7159c08c3f | -2.26648 | -53.61018 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3bd120c-9247-31cd-883a-a1bce8cc3c68 | -3.26872 | -53.65331 | 2024-12-03 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dca63536-298c-31a9-ad3c-5ff66b573ee4 | -2.4196 | -53.93816 | 2024-12-03 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aee1dea9-5e35-3503-88f5-7a4941b99ce4 | -9.89778 | -63.18288 | 2024-12-03 05:25:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0381fd7-5f4a-316d-b41a-64fe0c3b0d78 | -2.63356 | -54.21149 | 2024-12-03 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README62.md)
