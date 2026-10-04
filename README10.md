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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31f676e2-9f16-3710-8e1d-3a222827feb2 | -6.0651 | -47.285801 | 2026-10-04 00:31:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57473d14-704f-36d8-8824-5096d2975234 | -3.8824 | -49.694302 | 2026-10-04 00:31:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad7c8b82-266c-364f-a9d5-7a32b071faec | -3.1199 | -53.7374 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32640362-9ad9-3ea4-b055-8cf70a0125d5 | -3.815 | -51.536201 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 106faa12-bbad-3d64-a2c1-668f6716ee30 | -2.8169 | -54.1194 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdd4ae0b-4527-326d-a4ef-ad6c38c4591f | -4.8085 | -49.875702 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cafc7539-9b7f-31f7-aff1-715fa759995c | -5.8708 | -43.599098 | 2026-10-04 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb201ac-b98e-3801-accc-e6b15cde28ad | -3.1045 | -53.7141 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a3e7be-2231-3255-acfa-2a8e9ce580d1 | -4.1541 | -47.541 | 2026-10-04 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d5f53f-e495-3e46-bdd5-5f944636629f | -4.2806 | -50.272099 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e5b1da5-86df-3578-8c50-6fd2083f10e2 | -1.4727 | -49.473099 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6acd1ac9-ae4e-3c9c-9724-69d1be389b7d | -3.4955 | -54.5924 | 2026-10-04 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273006f3-1d4f-33ce-a166-256480c8152e | -8.538 | -50.064301 | 2026-10-04 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6822355d-0544-30e7-9a28-75834c669202 | -4.4603 | -50.979401 | 2026-10-04 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0add3a16-ca42-3f10-9a93-c33dfbf12586 | -3.5053 | -54.590302 | 2026-10-04 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1380327b-0993-3f65-9ebc-50b761725d5f | -2.8101 | -54.134899 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0c6d9d-feda-36f9-943e-7d904c325c54 | -3.3649 | -43.382099 | 2026-10-04 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03bce577-af20-31cf-8230-57fe2614b9ec | -1.3826 | -46.478298 | 2026-10-04 00:31:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 444a4ebf-743b-3ce5-9329-d6de5ef23695 | -3.2954 | -53.834702 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee2b3f2c-4519-3baf-bf6c-7dd00a852ffd | -5.9957 | -53.519699 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf617e6d-ec64-3b40-818d-ba16737213aa | -2.2226 | -53.710098 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075e5e9c-f079-34b2-8de4-a787ac87ca59 | -3.2705 | -43.375099 | 2026-10-04 00:31:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3c0530f-46f3-3158-9d55-6c89f8b0be32 | -2.8108 | -54.092602 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c773582-8c0e-3f7c-bf07-136e2985ed66 | -6.0581 | -53.477798 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 018f5404-95df-3674-a030-8ad11012ddb1 | -4.3776 | -44.403599 | 2026-10-04 00:31:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f756d79-0294-382a-b09e-33926ad92760 | 1.769 | -55.654999 | 2026-10-04 00:31:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e31422-3e6d-345e-86be-375096e13179 | -4.818 | -49.2799 | 2026-10-04 00:31:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdee7ef7-b8a1-34e6-add9-c97e0176f4a8 | -0.4672 | -52.0508 | 2026-10-04 00:31:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1b5f3b9c-c8c9-3a1a-9e67-3c13ffee9af0 | -3.7596 | -49.561501 | 2026-10-04 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f4a790-d906-382f-b0c1-b82a6669c064 | -2.21 | -53.699902 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df189b7e-2fba-3d46-93a1-c96e25f5b17b | 2.1033 | -50.7346 | 2026-10-04 00:31:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfdf6d4-1fe9-3507-97a4-d1586e3e4878 | -6.2093 | -45.4011 | 2026-10-04 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8dbffde8-1d4c-3a7d-a5c0-dfdbb0215858 | -4.2658 | -49.9786 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b860dac-cdbf-3829-b167-daf00373272e | -2.7816 | -54.098999 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc348451-7d68-3a9d-8da5-eb1cc860e4c8 | -3.2885 | -53.849899 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48f9eedd-bfd6-38de-beb2-2741241bafcd | -0.3575 | -52.065701 | 2026-10-04 00:31:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bdcb6acd-02c3-327f-a9a1-b077d7778fe5 | -3.0733 | -49.532398 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1e9d08d-27ad-3df0-9ef4-f1d4e424298c | -3.1674 | -54.0853 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e54d03-5d4e-30c2-9466-dfbec96764b7 | -4.2047 | -53.461899 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f98507b-ae62-3aad-ba8e-2370b493c5d0 | -5.0527 | -45.6199 | 2026-10-04 00:31:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 891cc262-5620-379d-8acd-70e3a9df989d | -7.7433 | -49.2062 | 2026-10-04 00:31:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| abaf2d9d-fa3b-3045-9e45-9b903bef0ed0 | -2.2488 | -51.880402 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f00bfa81-619f-3837-8096-fc7bdeb75655 | -4.8165 | -49.8657 | 2026-10-04 00:31:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6e32bf4-2461-36a9-b43a-5587c0f2ad85 | -1.1539 | -49.251598 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e34543-df6d-3793-8bc0-2c6d4bcb7657 | -5.986 | -53.521702 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 425db179-7b95-3a91-bf5b-5d32870a9ebe | 1.7724 | -55.640499 | 2026-10-04 00:31:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 155050d9-9be9-310e-8d0d-fbe0b98175d7 | 2.0935 | -50.732399 | 2026-10-04 00:31:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 76a35369-d5be-369e-9fe9-bbeac4df6619 | -3.4709 | -50.104 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b377addc-6cc4-3b36-b118-520f542c2b7e | -5.2937 | -49.198601 | 2026-10-04 00:31:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ce4586-02a5-3701-952f-263894a1697a | -5.5584 | -45.264 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f6837bf-d0a2-37a4-af77-d318e08fcaec | -3.1741 | -54.069698 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb678111-5089-3be9-9be3-0b9756b072e7 | -3.0296 | -54.201 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34c0b55d-e58a-3421-aad5-5a3a537e3142 | -1.4743 | -49.434898 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5038215a-3567-3408-a5de-a98e2e48f916 | 0.8386 | -51.2547 | 2026-10-04 00:31:00 | METOP-C | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d0eefca8-c0e2-3060-a495-0f810cc2f6a8 | -2.7484 | -51.545502 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8302e6d8-8c39-3835-a4f4-aea4b3d09696 | -4.2686 | -46.378601 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31ac396a-b095-3d2e-935d-f0d465bc5e0e | -2.9144 | -54.098099 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0f448f2-3dc9-3104-8394-e112cc486c2b | -2.8198 | -50.500099 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8962b8aa-c5b0-3f5a-9fff-583d681ea4b2 | -2.208 | -48.227699 | 2026-10-04 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59914ce5-457e-3cf7-8a7d-d1379f5790a9 | -13.4753 | -42.471298 | 2026-10-04 00:31:00 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 18a09c2b-9591-374c-9129-1dc73d2d14e0 | -5.0719 | -45.168999 | 2026-10-04 00:31:00 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f724bb89-85e9-36c0-a743-9e9e9019f9a4 | -1.4825 | -49.470901 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98767bb5-0812-3add-819d-f0692927bfd2 | -3.1966 | -50.755199 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b9ad74-52ce-3dcc-8468-89581daec259 | -2.252 | -51.939499 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee37bb9-1900-3379-8984-88d82dc577b5 | -2.5771 | -51.8778 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec721b97-c4ea-3e67-9890-38193140dc42 | -3.8033 | -50.845901 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33cef308-4b17-3dcd-a57a-3372725f4887 | -5.7491 | -45.1521 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c087174-7a02-3c48-8e05-2fe785c16e44 | -9.1003 | -49.773998 | 2026-10-04 00:31:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e71e6337-3f6c-34b1-a575-1b6f79dd84de | -2.0373 | -56.862801 | 2026-10-04 00:31:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e15be1a9-fc48-361b-9936-5edb8f4c77f9 | -4.254 | -46.3601 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 931185b8-74a5-3291-9897-ec573b84b4dc | -6.3146 | -43.3368 | 2026-10-04 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7927d3e6-6da4-3f5f-9557-935ac5a85417 | -5.8597 | -55.713001 | 2026-10-04 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9051ff-4c84-3653-925d-083becd482c3 | -2.9759 | -54.098801 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 866abd9e-c755-3568-b13d-cb0908a92f17 | -2.8912 | -54.131401 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb97bdc-7745-3483-91f2-2fb46011a718 | -1.489 | -49.4543 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec34c1f-62ce-3b08-a42b-d2b6f9315b48 | -2.9998 | -50.477299 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b739f692-01be-3c83-a115-ade5c88b001c | -4.8201 | -49.881599 | 2026-10-04 00:31:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 903c234b-7d8a-3c13-9ca4-0cdc79d86a7d | -2.5673 | -51.880001 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56a49ab2-f4f4-3cb2-ac0c-17d3974e2350 | -6.196 | -52.798302 | 2026-10-04 00:31:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c563e07-8f14-3b58-9fa7-f14ffc09bb15 | -4.2556 | -46.367001 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad522222-fe4a-3442-a69d-a7019af71ec9 | 2.1016 | -50.742001 | 2026-10-04 00:31:00 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0e2a26-fd57-3443-b478-b54177c2f868 | -2.6766 | -54.632301 | 2026-10-04 00:31:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e122480-796f-3cdf-ae4d-3cc195245ad5 | -3.1142 | -53.712002 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff0d7d00-4234-3731-8427-e302a59d2ec0 | -4.9836 | -46.034599 | 2026-10-04 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bae0eeea-bd0c-3d81-a9e7-ba0eb59242fc | -4.4505 | -50.981499 | 2026-10-04 00:31:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b176919-44e2-3c23-9c13-c9cae5cd9726 | -4.2788 | -50.263901 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e8935b1-a1a9-395c-b626-5976f7bb29a5 | -4.2638 | -46.357899 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7575a1-3ce7-3456-a5b0-32525e362d30 | -4.805 | -48.2239 | 2026-10-04 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73adadac-508d-3a03-8865-aba0b0dde508 | -2.5782 | -51.837601 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee82ab3-c288-396a-8f2a-9f0d641b8bfa | -3.1074 | -53.726898 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18f3d5f2-2853-35b1-b5a2-5f4ddfe4d369 | -9.1022 | -49.782799 | 2026-10-04 00:31:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be98eefe-f5e5-30ed-bf49-f5b01b3827f2 | -3.1004 | -53.741699 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b51f14-436b-399c-bdc5-fcc25bdeff3c | -2.9602 | -54.074001 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5dfde92-1e40-3eb3-bb06-1d95317075ab | -4.2843 | -50.288502 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bde10a9d-6d69-3f44-8648-cbad3a7149f2 | -4.2769 | -50.255699 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5245e6e5-4a76-37a5-87b7-286db4c6f8d6 | -6.0649 | -53.462101 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01cf25c7-7a37-30de-9764-add87f8c9093 | -5.7474 | -45.144798 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf24fba-8446-34e8-8f18-3a8c4165e08d | -4.2886 | -50.261799 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b163e3-2980-3e17-9349-6093299e14ad | -3.8841 | -49.7019 | 2026-10-04 00:31:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc4852db-5413-3f1d-89d7-30e161331da2 | -13.3374 | -42.412498 | 2026-10-04 00:31:00 | METOP-C | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README11.md)
