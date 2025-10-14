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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9732b5e-615b-330a-a307-e0b1055f39a3 | -7.9631 | -44.113 | 2025-10-14 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f97cdcc0-e85b-339d-88bb-41f814169756 | -4.6883 | -43.1314 | 2025-10-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| b72745ed-9535-35e1-b1b9-62829aef867b | -7.9439 | -44.1381 | 2025-10-14 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| a60dd126-2ad0-32b5-9eed-4d118d93d131 | -3.0416 | -40.108 | 2025-10-14 01:30:00 | GOES-19 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 66.5 |
| b7e40ab8-b1bf-3827-b249-e6e5054eb156 | -4.6883 | -43.1314 | 2025-10-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 336984d8-2ce7-3ce6-9c23-bb5b706ae9d6 | -5.494 | -43.0526 | 2025-10-14 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9a1321e4-dd93-346b-ab84-597385bd5aef | -4.1233 | -50.0639 | 2025-10-14 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a71ccf53-a7e5-3b33-a494-acdb50ef8846 | -11.7406 | -43.269 | 2025-10-14 01:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 104.3 |
| c541e714-31f1-399c-a541-2534d15b18c7 | -11.7598 | -43.2659 | 2025-10-14 01:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 104.6 |
| 00aafa4d-8377-3567-9172-2267869d00e1 | -12.8181 | -50.6786 | 2025-10-14 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 49e50bca-3243-373d-9017-f9f49787f892 | -11.7401 | -43.2928 | 2025-10-14 01:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 153.6 |
| 92e341ee-b144-3fc6-91c5-66ab8007273c | -13.5145 | -50.3084 | 2025-10-14 01:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f0f9d716-c08a-348e-a754-284f0f2d3b0f | -4.6698 | -43.1092 | 2025-10-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 36e066bd-5fee-3cf5-94a5-e5c5c6ffd15b | -11.7594 | -43.2898 | 2025-10-14 01:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 150.1 |
| 10d80e72-aa18-38bf-b42a-dc6c751d2b15 | -5.0994 | -43.1977 | 2025-10-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0e06910c-b769-3246-b10b-9010be942104 | -4.1048 | -50.0647 | 2025-10-14 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| fac8cb98-e227-39ff-a179-ecee07248108 | -4.6319 | -45.7863 | 2025-10-14 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 48fb5004-a094-3a77-b85f-aeefe3c5f716 | -4.6694 | -43.1559 | 2025-10-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 8b40f2a3-6999-33b2-8f80-5f11d41586dd | -4.1235 | -50.0428 | 2025-10-14 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d5992304-40d1-3e4c-87be-d681b58b1059 | -7.0414 | -39.2229 | 2025-10-14 01:30:00 | GOES-19 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 0f3fbfb9-8a4f-353e-a79c-2655bed39126 | -12.8184 | -50.6571 | 2025-10-14 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 275b0bdf-a898-36da-8150-1a89e8e97237 | -5.4937 | -43.0761 | 2025-10-14 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1e43521b-9e6e-3123-aaa8-e52c8d0e1ca9 | -7.9442 | -44.115 | 2025-10-14 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 953298bc-7777-3b32-b9f0-8c5bb521b33f | -5.1181 | -43.1964 | 2025-10-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 152648c4-10b9-3fc5-aaf7-5bf7611de536 | -4.6321 | -45.7639 | 2025-10-14 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c6b85552-9722-3ea0-84bc-4f085881e22a | -4.105 | -50.0436 | 2025-10-14 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 186.0 |
| 97de56e3-d983-3174-9330-326f675e28ce | -4.6509 | -43.1337 | 2025-10-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| da262d90-a429-33d2-aa51-5ee88932fd0e | -7.9253 | -44.1169 | 2025-10-14 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 13a5360c-8d0d-3bac-8b32-4e29b999e022 | -4.6696 | -43.1326 | 2025-10-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| e0abfaab-7a10-348a-9379-02e5a27f94ce | -7.9251 | -44.1401 | 2025-10-14 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| cd94e277-047e-377a-b0ce-d8d2f5235872 | -10.38761 | -61.22886 | 2025-10-14 01:32:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 90fee6de-6bbd-3ea9-bb8e-bedcb85fb17d | -9.44969 | -56.65066 | 2025-10-14 01:32:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 00e99e34-3f7a-3d63-89ba-ba2ab20c7200 | -9.41506 | -62.29776 | 2025-10-14 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 29a79298-7570-37c5-b5d2-38214d610937 | -8.84418 | -62.3034 | 2025-10-14 01:32:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 69f93cd7-8e25-3f6f-86d8-f0708443f260 | -9.66995 | -62.14535 | 2025-10-14 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3b41f352-24b0-3b75-8955-bf0bc4033d44 | -9.01362 | -62.0017 | 2025-10-14 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e41843c-6c89-307b-bf7a-f0340d29037a | -8.98186 | -61.97664 | 2025-10-14 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 677e90f8-c285-3422-a53f-4ec969812a2b | -8.7279 | -63.37577 | 2025-10-14 01:32:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 14e6a729-dfaf-3900-b7f6-35f237adfc93 | -7.82486 | -61.69211 | 2025-10-14 01:32:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9298e75f-f18b-35ab-a928-2bbbae1679f2 | -8.97266 | -61.978 | 2025-10-14 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 84e50af3-0344-3dc2-89fd-754e55250220 | -8.38174 | -64.07155 | 2025-10-14 01:32:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| faf5bc40-afd7-313b-904e-1bd272466536 | -8.84282 | -62.29388 | 2025-10-14 01:32:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7bbfdf12-cef6-3a1d-b125-eed23fbf8143 | 1.77019 | -55.84106 | 2025-10-14 01:34:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| b7c5bc13-3834-3426-94bb-36271a06f042 | 1.77583 | -55.80081 | 2025-10-14 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 46ad8da0-0971-307b-8670-1f66d59c9b9d | 1.77685 | -55.80585 | 2025-10-14 01:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 98250126-30b8-3165-a945-356c2d62bfaf | 1.82173 | -56.02181 | 2025-10-14 01:34:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 0f133bed-9fe7-3ee4-a2e5-11a807b9d01e | -4.1048 | -50.0647 | 2025-10-14 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| e69a028d-d4b7-32ff-8c27-094a27ab407b | -12.8376 | -50.6547 | 2025-10-14 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 821265bb-b5cb-3b65-9978-9e5743150b5b | -7.9253 | -44.1169 | 2025-10-14 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 56b950b2-ab1e-34d3-a536-0d110cdbe0f6 | -4.6694 | -43.1559 | 2025-10-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 0f1a54d4-bb18-33ed-9d5d-4ea43bb85628 | 1.7667 | -55.8031 | 2025-10-14 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| abf4dc4b-a216-37de-aa68-3e5bcbbfc606 | -12.8373 | -50.6762 | 2025-10-14 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1b3744c0-34ae-31df-8766-5ddc57c5f1ce | -12.8181 | -50.6786 | 2025-10-14 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 40658538-0678-380d-8753-1e4aea020616 | -7.9442 | -44.115 | 2025-10-14 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 187.5 |
| b6bd684e-b469-31a8-981c-08ef0afe5f9c | -12.7993 | -50.6595 | 2025-10-14 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5c0a27aa-eb04-3006-8e6f-8cb8ca92d3c1 | 1.1135 | -50.9776 | 2025-10-14 01:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d93e8990-219c-3ca9-93e1-1b0567f3cf19 | -4.6319 | -45.7863 | 2025-10-14 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ad9f98cb-d47d-3504-8653-a52feeaf61f0 | -4.1233 | -50.0639 | 2025-10-14 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 2ef41f20-41b9-3824-a2a8-026777cb7ddb | -7.9628 | -44.1362 | 2025-10-14 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 1f85650c-c853-3e59-aa66-cc8db675be27 | -11.7406 | -43.269 | 2025-10-14 01:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 116.0 |
| d8de0b3b-4cd7-3dee-addf-61450fe9bf9a | -4.105 | -50.0436 | 2025-10-14 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 28a9aa1d-3a30-3687-b7b1-3ff2f7c4c2b8 | -11.7401 | -43.2928 | 2025-10-14 01:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 175.7 |
| b62572e9-9877-3373-8049-0f16c965cfa9 | -5.494 | -43.0526 | 2025-10-14 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 1d860ffb-80e7-3aac-853a-ced32667bbdd | -4.6883 | -43.1314 | 2025-10-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b02b85e0-c042-3c91-bf10-c6a514c468ae | -4.1235 | -50.0428 | 2025-10-14 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| e720af88-b833-3d56-b395-385909c4909c | -4.6321 | -45.7639 | 2025-10-14 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 5be14f46-70be-3278-91f1-d9924209673d | -7.9251 | -44.1401 | 2025-10-14 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4b2d9ab7-5003-37f1-a918-2ecb78d2bbec | -5.4937 | -43.0761 | 2025-10-14 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e36490a6-3198-3e05-b5f1-07859ae5464c | -7.9631 | -44.113 | 2025-10-14 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dbcb4371-254f-3b2f-b5c8-9da1d06a7846 | -4.6696 | -43.1326 | 2025-10-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 6d376efa-1e97-36bf-8561-d78029fc557f | -4.6134 | -45.765 | 2025-10-14 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c653ee8e-a16e-3ad1-bada-8e0e16bc1a0b | -4.6509 | -43.1337 | 2025-10-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 09a35269-1131-3893-bd6a-1f252c9509e5 | -7.9439 | -44.1381 | 2025-10-14 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 1609a22d-d88d-350e-92d5-4f8fba139dc8 | -12.8184 | -50.6571 | 2025-10-14 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| c9fcb0d1-9b7d-37f2-ab27-ec8c8f8d3e5f | -4.6133 | -45.7874 | 2025-10-14 01:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b4b96377-c154-32c4-b77b-3c5c5fa7b9e2 | -11.7594 | -43.2898 | 2025-10-14 01:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| d3036bb0-1159-34cc-b20d-110e741f84e8 | -4.6698 | -43.1092 | 2025-10-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 797e468a-0931-3dfd-866f-73a3d4b72d52 | -5.1181 | -43.1964 | 2025-10-14 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 9c262004-6904-342d-b33b-c2b6958920c0 | 1.8213 | -56.0191 | 2025-10-14 01:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c381c50e-c0c9-3d7b-bec7-15a55814d408 | -12.7993 | -50.6595 | 2025-10-14 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e84a8d20-ce02-3c4c-ac54-bcf94248fd06 | -5.0994 | -43.1977 | 2025-10-14 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f9491a28-12b8-3202-8526-0380ab962855 | -12.8184 | -50.6571 | 2025-10-14 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 03518f60-48e8-3ff7-a006-1f0787526171 | -7.9628 | -44.1362 | 2025-10-14 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 62a8b5f6-9eb7-34e3-9aa4-0dd799faa918 | -4.1233 | -50.0639 | 2025-10-14 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d453773f-548d-30dd-8a25-216c1ea22e2b | -4.6696 | -43.1326 | 2025-10-14 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 951d250e-11b1-3275-b0db-e9b30d14063a | -4.6509 | -43.1337 | 2025-10-14 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 08149e51-f280-3e34-b30d-b577119a9eff | -7.9439 | -44.1381 | 2025-10-14 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 6d7cb34d-a635-3d22-98f0-a3e3c1af487d | -4.6321 | -45.7639 | 2025-10-14 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 00538191-bcf2-31f9-acf3-8c8132388272 | -11.7594 | -43.2898 | 2025-10-14 01:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 126.8 |
| 70842db6-10c1-35c7-a586-45f4525fafff | -12.9188 | -47.0626 | 2025-10-14 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b001fef6-a2d8-347e-85fe-57aae6db26f5 | -3.0416 | -40.108 | 2025-10-14 01:50:00 | GOES-19 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 60.8 |
| b771c829-ae4e-3422-a3f9-6cd49ada0c93 | -4.105 | -50.0436 | 2025-10-14 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 5d63f212-a0fb-31f5-a146-e677dd188cba | -5.4937 | -43.0761 | 2025-10-14 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b6ad49c8-0a27-36be-b07e-54ef970cc1f3 | -4.6133 | -45.7874 | 2025-10-14 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4f3313b1-daf2-3f38-904e-7a48e3a12bd0 | -4.6694 | -43.1559 | 2025-10-14 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 6b99ee09-28b9-389e-9dfd-ea65a214e9ad | -12.9183 | -47.0852 | 2025-10-14 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 759e4ea3-7a49-3999-844b-117bcdb69124 | -7.9631 | -44.113 | 2025-10-14 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b584171e-2558-36e8-ac15-e4bb48e290d4 | -5.494 | -43.0526 | 2025-10-14 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 15e3d3b0-133c-3c27-90a0-03110e95f4e0 | -4.6319 | -45.7863 | 2025-10-14 01:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 8b63491c-98aa-3e8e-a64a-26d7a7aaa8b4 | -7.9442 | -44.115 | 2025-10-14 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 208.6 |


[Clique aqui para ver as próximas entradas](README4.md)
