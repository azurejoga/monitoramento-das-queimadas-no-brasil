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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc59c129-a476-300f-be79-4f53c4fe78a7 | -8.9875 | -65.4006 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6b0d757c-aa14-3eb6-bd70-49259f73809a | -9.006 | -65.4 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| cdc39cab-db3f-34e9-bb5c-3f65757526f3 | -9.1722 | -59.4629 | 2025-08-25 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ac0220e3-a7df-350f-a05d-b22e437f4da0 | -8.9874 | -65.4192 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 458e843a-4241-3b71-9c27-266167ff2fc3 | -8.8918 | -62.4677 | 2025-08-25 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| fef55ff2-1ea0-3441-99bb-014c9605b369 | -9.06 | -65.7344 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 0a2b572f-1326-3839-b6fd-2bf41edc79bf | -8.2128 | -61.393 | 2025-08-25 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 25e7abe4-52bf-3fa3-a6ae-551b4484df8d | -8.8733 | -62.4685 | 2025-08-25 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 124.8 |
| b58d4680-7864-3352-bf1b-16252797428e | -5.118 | -43.2198 | 2025-08-25 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 43b1d8f5-3551-3b92-883e-89c7ac66bd7b | -8.0493 | -49.6967 | 2025-08-25 04:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8ae42e4d-4ed6-3a47-8080-be0a4f5b4d11 | -8.0681 | -49.6951 | 2025-08-25 04:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9892592a-a883-3c99-a22b-2c45a4257a4b | -9.0415 | -65.7349 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 22e8cff3-b4e7-32ab-8324-81faeaa0d5ec | -8.9689 | -65.4198 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 55e17190-9455-3573-9c4f-0996c5061a74 | -5.3078 | -60.2008 | 2025-08-25 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 586263e2-64fc-3be5-a096-880c328a33e0 | -6.8229 | -58.956 | 2025-08-25 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 3d877d6f-fcff-3ed6-9dd7-95c1ca209bb2 | -9.0601 | -65.7157 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 6840bb90-e4ab-3a57-a85a-4d5599ff9e94 | -9.0971 | -65.7332 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| ab0f4bce-abda-3d6e-95da-784752853448 | -9.0416 | -65.7163 | 2025-08-25 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 3fdb10d1-df99-33b8-b2d2-7c503c14df41 | -8.8734 | -62.4495 | 2025-08-25 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 3ef44417-6a2f-3463-9517-c2d1d2fd0a6f | -8.8919 | -62.4487 | 2025-08-25 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.7 |
| dd2eb235-2069-3bd3-bdfd-ddba938d9be3 | -5.1181 | -43.1964 | 2025-08-25 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6c25c560-4cc9-304e-9426-32e63b363972 | -7.08972 | -44.62027 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d3eb02c-9d39-3964-b35a-c1aec0bcf881 | -9.52298 | -40.31823 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d796a961-e97a-3de4-938b-0981dc438fb7 | -5.74447 | -45.36206 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8555145c-4e31-3f95-a2e3-2dc756f33c46 | -6.02238 | -42.80004 | 2025-08-25 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca625cd3-3c0a-3d2a-aba5-357f10f8ef53 | -5.88448 | -43.37918 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fed1b69c-caaa-364f-92da-5b95078d7ffd | -8.38589 | -44.94468 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aa82282-2aa9-371a-b7ac-2b49d197856b | -7.47643 | -44.89077 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1db64aca-5499-370e-a249-62aa1dce6760 | -8.06181 | -49.67615 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19748b24-9e1b-3b29-b6dc-d0459160408f | -6.13951 | -44.39562 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c68b6e4-229b-37ca-b267-f386b32dbf4c | -6.82763 | -42.82749 | 2025-08-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca17c65d-645f-39da-8c6f-e780643d6bd8 | -6.6821 | -44.42384 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 301bfe80-0862-387e-adec-1b6555dd63e3 | -5.10883 | -43.20364 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 2d63a922-55eb-3dd3-975c-3b4ab2b52163 | -7.17478 | -39.40739 | 2025-08-25 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 85c1264f-756c-36a5-8f9f-372a71edc695 | -7.66482 | -42.66824 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b06cef0-941f-3e34-ac35-e89ebebc5558 | -7.89534 | -45.89492 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 525f9aef-65b6-3d15-9aad-97333af33eff | -3.44287 | -49.04434 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2808b66b-a03f-314d-9c36-ccd8b8f0afb8 | -6.38299 | -43.25705 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b072d472-bb0b-3b7b-a77a-e21efed1476d | -6.98354 | -44.13375 | 2025-08-25 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b328fbe2-840a-3e49-9a41-3a740372c98f | -5.49029 | -48.08884 | 2025-08-25 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68eb7003-e9dd-3114-bb70-9989e65e271e | -8.39202 | -44.94931 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6013279c-19fa-379a-a485-5bb694702fff | -6.6394 | -44.24377 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2b7dc2e-a8b3-3c54-aa77-664798fa2a27 | -3.98358 | -49.49825 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5435d289-d49a-3ca3-9381-ecb162fa9168 | -8.80305 | -47.31511 | 2025-08-25 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38a0ff8c-4bc6-3b16-a429-c93deb0261c9 | -6.03095 | -44.2193 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2784d791-e3f1-3c88-8398-f0a8df063281 | -7.25542 | -43.66116 | 2025-08-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 332c1f05-5c34-3e22-b226-765963abf84f | -5.86875 | -42.91403 | 2025-08-25 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2acb5d08-4b64-378b-9d0d-c40c8d5300bb | -6.78228 | -44.30964 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d440a995-3cd1-3e30-bbe4-d77699075ea3 | -3.45755 | -43.34307 | 2025-08-25 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3bd601e2-cc53-3e47-a8e2-41ebf588a3ff | -6.38192 | -43.26395 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b617ccc-33a6-3422-9ba7-e767ff5dfb7c | -7.17952 | -45.17102 | 2025-08-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a8a665a-f92a-346b-b522-b9a05ef8c8ce | -3.25687 | -46.90508 | 2025-08-25 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 853867c7-f191-3bed-abba-7840f5949780 | -7.47307 | -44.89026 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f12fabd6-bd7d-3f7d-99ea-98d5aedcb082 | -8.40935 | -39.83094 | 2025-08-25 04:14:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 002ad91d-22b7-38df-9c0e-9b2643cbdb4b | -6.16433 | -43.00322 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 125b2dbc-ba6f-3e46-bf18-60b09e51d72f | -8.54322 | -48.85759 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4009fb3d-d590-39b5-9734-eba72f3b8d25 | -8.59156 | -44.05571 | 2025-08-25 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7355ed90-ae85-3c6e-a790-35bf20fe9a42 | -2.29437 | -47.97961 | 2025-08-25 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5eb535f-bbe3-3cd9-8534-0bba67739bea | -6.9211 | -43.77467 | 2025-08-25 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 565fa18b-4e70-3258-aeb7-af096cc0026e | -7.29471 | -44.53281 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e239ea0-b912-3214-85ee-77b75b3a36fa | -6.23123 | -44.77752 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aeddb49-4b35-3e03-82fa-d1a8aa2fd538 | -8.06829 | -49.6899 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37a42377-1562-3643-9238-be04f55b52a6 | -7.90453 | -42.54674 | 2025-08-25 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f3941a6-e1fe-3efc-b66b-08dcfc8dd32a | -7.61169 | -45.23554 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8af2504b-ff37-33a7-ac1a-3f655e5482d2 | -5.39305 | -42.3642 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b22bc62a-1db1-3cd0-a7ac-448bbfaea365 | -8.11221 | -47.13322 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47b188d8-43ac-3a6b-aa64-5eb47c87a067 | -8.31966 | -47.26314 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb22e85b-b601-3823-9ee6-527250f53a94 | -5.46103 | -42.60598 | 2025-08-25 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 392d01b4-9e23-3119-af5e-aa829bf48d52 | -6.49833 | -49.90722 | 2025-08-25 04:14:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc2110b9-3e3a-3241-b01e-d1baa71967d2 | -5.95563 | -46.15239 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6f688f2-940f-348d-b6a8-c3d2d582d0da | -8.54502 | -48.84688 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d22e6f5-3cc2-329e-b2fd-669bfa71a88e | -3.19929 | -43.90055 | 2025-08-25 04:14:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd5dfbd5-369e-33be-b247-4989e531bc35 | -6.20623 | -44.14265 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b773c8e-23a4-3c6d-9cca-a73cad7779ec | -6.03284 | -42.79811 | 2025-08-25 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a5a3c8e-759a-3f92-a581-8e08ef06c8f8 | -6.80334 | -44.99504 | 2025-08-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc0c0410-6bed-3750-8060-095473a5ca8d | -6.43956 | -44.56347 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5650defc-774d-3748-9f6b-9dbe457cd2ca | -5.50341 | -41.41252 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9f2790ea-1514-36bf-a7c6-e9a38652b318 | -4.6313 | -41.40218 | 2025-08-25 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61b572bf-f69a-3139-ad6e-82512dc7162c | -6.89749 | -47.93163 | 2025-08-25 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80bb49b3-fdb4-3858-9596-94407c9a079d | -7.47166 | -45.01925 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28bf2974-c19a-3691-85db-473264999608 | -5.10721 | -43.21397 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 62f9d65b-2ccf-3501-b134-148d99bc1588 | -6.21788 | -44.11218 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8233a2de-e426-3a95-897c-2bcff9e75566 | -6.68043 | -44.41643 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a613cac2-5f1a-3e1b-a9bd-9cad69f66920 | -6.26192 | -42.87683 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05e02ec4-e80c-3585-8070-feb977fe6dec | -6.03762 | -44.1122 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da53a3c4-4030-342b-baee-27ef459267f1 | -7.09469 | -44.63207 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 858ff9ad-4985-313f-8dcc-15a00588877d | -4.63468 | -41.40267 | 2025-08-25 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 734f3551-e5eb-3cf9-8763-59e5c994eb24 | -5.63676 | -45.15551 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fe3bc86-bf54-33d9-8bac-60f68a862128 | -7.93602 | -45.92904 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11361820-8e66-32bc-90b9-52c04d606206 | -8.12463 | -47.12639 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76324110-3ce8-3d11-93b7-bc2b31f28f06 | -6.20011 | -44.13815 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28d40918-daa0-30cf-a05a-ed8ba9738b47 | -8.32039 | -47.25875 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac197475-5afb-3d98-ba6f-e7f921e776ef | -5.86821 | -42.91747 | 2025-08-25 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2f547d5-5519-34f1-915e-bfcf41d1f921 | -6.90293 | -44.405 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 373a66a4-8fc6-3770-83eb-095ab2957374 | -5.49238 | -37.26576 | 2025-08-25 04:14:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 90f6a2ee-a63c-38c6-9e8c-677e5cce85a9 | -6.06251 | -43.99762 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6ad8027-1bc5-3ea8-bec3-0c313663551d | -5.48929 | -41.4141 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15cbea54-c42f-3d14-80f9-ff62581f2847 | -7.09192 | -44.62796 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6783067e-6c4e-3400-b7d0-567ba356cfd6 | -8.38669 | -47.99638 | 2025-08-25 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10049dc1-5686-38c4-bb51-b207b8e70bbd | -6.14625 | -51.75279 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
