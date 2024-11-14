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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84fda5af-df4c-3524-a8fb-4bf0367c4a3f | -1.99158 | -46.2602 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b9d267b5-a579-3b09-8fb7-80a4da1687b5 | -3.06027 | -45.5277 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 36ce53b5-6e04-3cb8-9336-1e20d1718dc1 | -4.18073 | -46.1025 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 15179731-26de-34af-b488-0592300e1696 | -3.38836 | -43.93507 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 373810af-7a1a-34ff-bf9c-27d45a1b5020 | -1.84663 | -46.28383 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b4650ab2-5c6d-3bbb-8ed1-b690efd55b0b | -2.3809 | -45.61858 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e1388dc3-76a8-376c-8bc1-f77590400cb5 | -1.95375 | -46.24758 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5c52ce67-a6bd-343a-84c3-382ab47c39ad | -4.21108 | -45.3209 | 2024-11-14 00:41:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0bf4686c-844b-3964-8fee-64dcfaa64128 | -3.27802 | -50.57996 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7ff428d2-7ab3-3621-9c1a-95182e79097b | -4.00499 | -45.56648 | 2024-11-14 00:41:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 308.0 |
| c31cb6be-eadf-37dd-ac0a-acbb5adfc634 | -5.0274 | -46.83085 | 2024-11-14 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 25333f05-b0a9-3c85-9cb6-50a77c961f89 | -5.1996 | -44.35899 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 166a2454-503a-3f8a-b7bf-53d07ccd8f47 | -2.05862 | -45.88622 | 2024-11-14 00:41:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a1c7ee19-2530-3889-a951-dc210bf14718 | -5.47457 | -47.00737 | 2024-11-14 00:41:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c95c4776-8ee4-318b-9b88-c25bd9bfd6d8 | -2.66869 | -46.81968 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| bf69b014-f632-3832-98ee-6214e4657f85 | -4.02867 | -44.68025 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| dcbec463-f1d8-35cb-bb4f-86c1bbefb1c3 | -3.08212 | -45.42551 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 633f3d80-efa6-3773-a409-67588c84cfd7 | -3.88176 | -52.2746 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 6a6e3a5a-1dcc-34b5-b7da-5fb9d22dbdeb | -2.03157 | -46.94865 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b1ee5d80-c4ce-34bf-850a-ab6680a6342c | -5.95044 | -39.66773 | 2024-11-14 00:41:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 8657fa3e-5582-3c08-806e-ddc93e560ffd | -2.58438 | -47.48021 | 2024-11-14 00:41:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f64b7146-dab1-3ad2-a723-357f3e04255c | -2.72303 | -53.20086 | 2024-11-14 00:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a145b0fd-8f44-3e8f-8323-026df62b675a | -2.88641 | -51.80123 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 9e2d68eb-a4a2-35c0-b1e5-2ede71e57d15 | -3.47128 | -50.31349 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 08cd2a36-ef30-329f-ad2f-0ae37704e50d | -3.35815 | -46.08423 | 2024-11-14 00:41:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 826a930e-8235-3ef3-87a5-05cf0c37499c | -4.05037 | -47.22599 | 2024-11-14 00:41:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 3549be47-b529-3fac-b221-136f84c14583 | -4.52793 | -46.4828 | 2024-11-14 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 71b399ab-5233-3a80-ac5a-77f4985a9e3d | -4.07171 | -50.00429 | 2024-11-14 00:41:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| dc4cdeaf-b6e7-3a57-bbba-9caad5c2c7e3 | -1.48554 | -45.80606 | 2024-11-14 00:41:00 | TERRA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e01892f-2b46-3b35-9034-2df07de1413b | -4.62442 | -44.53063 | 2024-11-14 00:41:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 64cdda71-150d-326c-b20d-6f93bf37082d | -3.24599 | -46.53746 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6f3390e7-8188-3f25-b74b-636a7eb3d834 | -2.88389 | -51.78318 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 69371dfb-e1ed-3485-b43d-f2c8ff506a77 | -2.90263 | -45.58923 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 458a46e1-e37c-329f-8249-44be84b37357 | -3.95562 | -46.407 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7f7d694e-0349-395a-9796-99b976143b88 | -2.87404 | -51.80289 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 9bfebb72-be76-3197-9a53-b5a8be412662 | -2.83044 | -46.65672 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| acd2bd81-0922-34a1-a539-bb2c619c9373 | -6.02162 | -48.04396 | 2024-11-14 00:41:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 868d23d4-cfe4-3563-b11e-80f551743b78 | -2.40801 | -45.34655 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2b62ab91-a0e9-333b-a65d-aea3d08cf41a | -2.25365 | -47.48396 | 2024-11-14 00:41:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 094dd756-f700-335b-9f04-6f224cfa0abd | -3.77717 | -41.60691 | 2024-11-14 00:41:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 64d056fb-fe43-3a22-9a63-4a13b2ebe8c6 | -3.27725 | -50.5737 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 0ebd0cd1-919d-3198-ba04-067248660f35 | -4.07359 | -50.01812 | 2024-11-14 00:41:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| a2845c3b-3e4f-327e-8a41-a05727e36f1c | -3.41309 | -50.3133 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7675a403-3385-3210-94bf-a836a4b6a657 | -4.43697 | -45.95795 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5d26406b-7956-327d-9382-8daebe8c7de5 | -2.54376 | -47.11739 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b60edd8d-dae6-3c8a-b01d-57ed9c5990d2 | -3.26543 | -46.27449 | 2024-11-14 00:41:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f3ad0b5-e09f-3a2b-acb3-92726f03c794 | -2.63971 | -46.1534 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df14f21c-43fc-3615-9383-64d9a77e8e3c | -4.15383 | -43.73659 | 2024-11-14 00:41:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4dcb55b2-5dac-3193-8c58-ce1033339cac | -4.92908 | -45.71644 | 2024-11-14 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29f249a3-9bbc-3d05-9e48-5957f39c1775 | -4.33675 | -45.43215 | 2024-11-14 00:41:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 31c30641-175f-3494-8112-a747548e1e6e | -1.3902 | -51.1194 | 2024-11-14 00:43:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e7364d8f-ce46-3dc2-a8f1-6ac6853db086 | -0.19284 | -51.49681 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1579e5a4-5647-3914-b807-7c0874e31a0f | -1.38418 | -51.56027 | 2024-11-14 00:43:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2040704a-125b-3f39-bc59-60199bd12e43 | -0.19211 | -51.5071 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 668d1628-1f28-35dd-aecc-8558bd48faee | -0.0336 | -50.77985 | 2024-11-14 00:43:00 | TERRA_M-M | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0c30b40a-18aa-3d43-a299-4b810ba15924 | -0.42044 | -51.57479 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 79696b94-ffeb-3b36-aee4-2e92a6a3228e | -0.20579 | -51.52105 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ba024075-e3ba-32ba-8984-a14a7de063a7 | -0.22669 | -51.50224 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 38.3 |
| c03148d5-5d7b-3485-bb74-b83cddc8d6f8 | -1.4016 | -51.11779 | 2024-11-14 00:43:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7319ce0f-df1e-3712-8f81-bc57e7e6ac1f | -0.19509 | -51.51232 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f65735db-c8b9-3630-b58c-5f0cbe11b53f | -1.5597 | -51.85097 | 2024-11-14 00:43:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d565dcec-f2f6-3dbe-8e0c-e3e34d04fdda | -0.90033 | -51.72494 | 2024-11-14 00:43:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b6b8d21e-d662-3113-821e-0c84fe13acea | -1.41146 | -52.38543 | 2024-11-14 00:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| f996f7bc-8aa4-3527-a810-e98b414cbfcf | -1.67011 | -52.55618 | 2024-11-14 00:43:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 70919bfc-f5ce-364d-8d75-f57d9abb1e34 | -1.05525 | -47.346 | 2024-11-14 00:43:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| b1d22b41-0dc7-3063-a0be-cae411926f8c | -0.34531 | -52.04523 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 39.8 |
| ffb75f1b-05d8-3a42-b95f-d8f05064b0d2 | -1.39232 | -51.13453 | 2024-11-14 00:43:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8beab94c-18f3-3dcf-b66c-ff760c1fd4d7 | -0.20364 | -51.50549 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 27.7 |
| a2ea98be-6497-3be0-847c-fc8e15017ce1 | -1.36518 | -52.33924 | 2024-11-14 00:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 727f62d4-5199-3c8d-a731-85f2fc96d0e9 | -1.05399 | -47.33693 | 2024-11-14 00:43:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 035a4a45-68a5-3109-b982-cd1aa468162c | -1.38311 | -52.37542 | 2024-11-14 00:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ecef8874-31be-370b-ae7b-a7f401cb8510 | -0.34298 | -52.02803 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c50ffa0b-c8b0-361f-868b-ce35f53e59f4 | -1.38044 | -52.35642 | 2024-11-14 00:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 48235c43-9c6a-31a6-95a5-1e66fec0e95c | -0.33828 | -52.035 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b3e111ab-fd89-39c8-aed2-646e727ed1c5 | -0.34075 | -52.05219 | 2024-11-14 00:43:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e3ce681c-f8f9-30dd-ab84-89529605cfc6 | -1.4111 | -52.39098 | 2024-11-14 00:43:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f2b5ce6c-ef08-37a4-aab2-bbd774dc8446 | -0.79483 | -49.49926 | 2024-11-14 00:43:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9fb18dbd-c17b-3d4c-94b7-1d58e009a921 | -0.93834 | -51.73663 | 2024-11-14 00:43:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3429d6d3-9201-37a3-ad80-513672d52476 | -3.7809 | -52.0952 | 2024-11-14 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f9c86b8a-77c4-3607-80f0-61c61cc0bcf5 | -4.0189 | -45.5719 | 2024-11-14 00:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 67122ecb-7e5e-382a-8261-2d7a960b42b7 | -17.5869 | -57.5533 | 2024-11-14 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.3 |
| bc017472-f86e-3ed2-9fca-2b1a4399ecc1 | -17.5672 | -57.5557 | 2024-11-14 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| b3f44507-d0e2-3673-8d41-ff11ccc2ad53 | -3.6217 | -50.587 | 2024-11-14 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| a7515023-8144-308a-bfc7-51d439b29fa8 | -4.0005 | -45.5503 | 2024-11-14 00:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| b2766385-c0d5-3735-83a2-f2fc21305d7b | -2.6564 | -47.0008 | 2024-11-14 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 1917c1de-01ad-3830-9a27-9c8548d53f3c | -1.3894 | -51.1197 | 2024-11-14 00:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b10d659f-d65c-3527-8f41-41c38498127f | 1.0674 | -59.2467 | 2024-11-14 00:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8c99367f-0060-3383-b49b-ef50963958b8 | -1.3874 | -52.3555 | 2024-11-14 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a284b225-1220-3bf6-8d0a-eedc523abe9c | -3.6401 | -50.6073 | 2024-11-14 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 7709ee85-ebe2-301d-a7cb-5b9d4c59a655 | -4.0003 | -45.5728 | 2024-11-14 00:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 89b60bf4-0977-35b1-b6b8-9ab9e6b3a520 | -1.4078 | -51.1195 | 2024-11-14 00:50:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 0718dfed-3a22-3fa0-b1d8-e115ca85ea7b | -2.675 | -47.0003 | 2024-11-14 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 3ab00692-90a5-3526-bf12-357783d266bd | 1.2852 | -60.4454 | 2024-11-14 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| a8dfe65b-e654-3c9d-ae68-4da9f8ea923f | -3.6587 | -50.5857 | 2024-11-14 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 366b0650-d1da-3136-a059-e33b7161e169 | 2.6703 | -61.169 | 2024-11-14 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c73de02f-e16d-3b50-8d41-5c39c1fb6b0f | 1.3034 | -60.4263 | 2024-11-14 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d192c68d-8105-38e0-95df-76de758a6b31 | -3.0522 | -45.5461 | 2024-11-14 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| f842264a-6358-35ff-a911-24ed4a54ac0c | -4.0191 | -45.5494 | 2024-11-14 00:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 2a3c4359-4324-315f-9ada-218cfc283867 | -4.0465 | -47.2109 | 2024-11-14 00:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c1183f87-c933-3a00-976a-fdb1bbd7f4c2 | -2.8791 | -51.7932 | 2024-11-14 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |


[Clique aqui para ver as próximas entradas](README13.md)
