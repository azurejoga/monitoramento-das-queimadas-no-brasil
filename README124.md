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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f867e104-67f5-36b2-9297-495fc3ecd6f5 | -7.88189 | -40.00732 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2318287f-f4b3-35f7-ad8d-1cc237942e11 | -7.88147 | -40.00408 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 989aa97f-da08-3413-a480-5dc3d04921e1 | -7.85157 | -40.55086 | 2024-10-25 15:33:00 | NPP-375 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54cda863-ae1e-32cc-bccd-fc9cdb2042a4 | -7.80017 | -40.09961 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d8f14f41-0d8d-335c-ad54-b1ebf8fa3c24 | -7.79972 | -40.09634 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d19c8b8b-f904-3fe5-b5b9-98504b792bda | -7.79901 | -40.10192 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8d5c0bd4-f1ed-3d79-bb1c-0a01204ac418 | -7.79859 | -40.09864 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 5aac68fb-ffe2-377f-ab8d-6aa6ae018882 | -7.79483 | -40.10017 | 2024-10-25 15:33:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7657f120-e888-389b-a5b9-a3656a67387e | -7.69759 | -40.05992 | 2024-10-25 15:33:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 5ef6aadc-8727-3f03-8c95-564a27c2a7ef | -7.62384 | -40.06046 | 2024-10-25 15:33:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5fd30d76-3a79-3485-bc94-2dba1f59b891 | -7.58574 | -39.97575 | 2024-10-25 15:33:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 65ebd45b-526c-3b21-98c1-bcdd896a5e7a | -7.58531 | -39.97252 | 2024-10-25 15:33:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 29c8a2d6-cef4-37af-a748-128f2366b8d3 | -7.58048 | -39.97646 | 2024-10-25 15:33:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b6c5cfa3-fd04-3bf1-8a8c-69836d0b9b0f | -7.58006 | -39.97324 | 2024-10-25 15:33:00 | NPP-375 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c8dfd915-df65-3e96-b518-05655e80c90e | -7.55598 | -40.51853 | 2024-10-25 15:33:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43168cb4-ca31-344e-bd38-456f4711e792 | -7.39476 | -40.30688 | 2024-10-25 15:33:00 | NPP-375 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 14d543c8-79db-3e3a-ae46-417562a264ce | -7.24509 | -39.97752 | 2024-10-25 15:33:00 | NPP-375 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b71f9e3b-4fa6-3e49-8a5d-6ea38d7d1e45 | -7.85108 | -40.55157 | 2024-10-25 15:33:00 | NPP-375 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae50c4f3-43a9-3036-a687-abf80099f631 | -7.72412 | -40.31855 | 2024-10-25 15:33:00 | NPP-375 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4bb1e6b2-ed9c-312b-bb45-25bf5a50e660 | -7.7208 | -40.32111 | 2024-10-25 15:33:00 | NPP-375 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f1c69150-8219-3a05-972d-9926b1e5853e | -7.70724 | -40.34362 | 2024-10-25 15:33:00 | NPP-375 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 41e53d10-bee3-3bb6-a320-aec2f40a3a19 | -7.76184 | -40.59305 | 2024-10-25 15:33:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 5205bf8f-55be-304b-8056-69daa3f78d77 | -7.76148 | -40.59203 | 2024-10-25 15:33:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 29.4 |
| a6351867-6223-3ec3-8c21-913d83654e04 | -7.76136 | -40.58955 | 2024-10-25 15:33:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 2d9f4fbe-8521-3bb7-834b-efc8f118425d | -7.76103 | -40.58852 | 2024-10-25 15:33:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 33.2 |
| a487e95c-9764-395e-9925-7a0abc3a32c7 | -7.72036 | -40.31768 | 2024-10-25 15:33:00 | NPP-375 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 341fc979-421c-3842-8bb2-2ea4e388fa6a | -7.71872 | -40.31925 | 2024-10-25 15:33:00 | NPP-375 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3a8a2238-ce56-3f53-a21d-65183d7c151b | -7.68239 | -40.54166 | 2024-10-25 15:33:00 | NPP-375 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 7aff6ff6-b982-3ee9-9a5d-3a298a89cf15 | -8.5204 | -39.7193 | 2024-10-25 15:33:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5e49b353-3e02-39cf-90cc-b03e3c253aa4 | -8.44849 | -39.85766 | 2024-10-25 15:33:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 387b0830-6889-3bf0-b2b7-080026777069 | -8.96892 | -40.86168 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 683d9b2c-aed0-39db-98ad-d02834c660a2 | -8.91875 | -40.76108 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 60.0 |
| fe0719de-aa92-3b04-b809-353d60932e72 | -8.62722 | -40.70328 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 1b5cb92d-97b9-3d5a-b31c-01ac67d0f7ca | -8.62211 | -40.70769 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 80c49775-a5e7-3859-a169-17d5710648e7 | -9.17365 | -40.94439 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| cc84df78-5fd2-364c-abd5-fef195097a27 | -8.91261 | -40.75804 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 9b8fe5d0-575e-3cd9-9576-3d94eb15e751 | -8.90524 | -40.87942 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63ec81e5-02f9-3cf6-b193-ccf1ecf8c40f | -8.62519 | -40.70671 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 6c9d0381-df90-35cc-abb9-5052f66e3e32 | -8.10927 | -40.77308 | 2024-10-25 15:33:00 | NPP-375 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fdfe39a4-f246-360b-8e73-01cb3dfb932b | -8.12854 | -39.54074 | 2024-10-25 15:33:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 767b890a-6ee5-30fd-b794-ff685a8119b0 | -8.05316 | -39.32864 | 2024-10-25 15:33:00 | NPP-375 | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 98cad093-da7d-3ff4-abb5-0911a4e96ebe | -8.02461 | -39.83202 | 2024-10-25 15:33:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7915898e-969a-3004-bc58-492dc6adeaec | -9.17223 | -40.94436 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| c665c000-16f2-3082-9b6a-83effba59aa7 | -8.96636 | -40.86021 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bb1219d2-a847-3abf-9b26-ec9e99b5d757 | -8.62162 | -40.70404 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 7c04d08b-e8b4-3dc6-ba4d-64d789e594e5 | -9.16791 | -40.94509 | 2024-10-25 15:33:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e5fe1957-a2df-324b-8822-a18483c56a08 | -8.9131 | -40.76177 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 60.0 |
| cbaa779b-f800-33e0-896f-e98d841c0af8 | -8.62473 | -40.70306 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 36.3 |
| eac4d75a-0e1b-3ba6-960b-608e2e91bf60 | -8.46866 | -40.48417 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| af1a5198-34a5-3199-9dd8-ec28043b9e17 | -8.03257 | -40.44486 | 2024-10-25 15:33:00 | NPP-375 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 0c2ec3ac-9db6-36c8-8763-645397facf14 | -8.91485 | -40.43208 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| b864b572-c15c-3b8f-9c99-8c43de54ab4d | -8.5826 | -40.49654 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7d5a6038-0030-33f2-ad3d-f6d3f607dc2f | -8.21113 | -40.31394 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 834846b7-401f-33fd-be4c-50552ef369c8 | -7.9092 | -40.56439 | 2024-10-25 15:33:00 | NPP-375 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| ad123f3d-b742-344f-bf48-31e94c8b69f6 | -8.58211 | -40.4929 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 325052dd-9d15-3268-859c-f54aafa6aadf | -8.58164 | -40.49588 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 05a9c0af-a3df-3f18-b4ae-51b834bb6660 | -8.58118 | -40.49222 | 2024-10-25 15:33:00 | NPP-375 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 476733d8-a86b-3e76-b277-439b0d54c209 | -8.47897 | -40.25864 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5edb1497-915d-3c07-afc7-4717d98b6a0b | -8.21155 | -40.31712 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 41c74e87-d0b0-30e0-a5c4-780f08e4dd79 | -8.20612 | -40.31781 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 5267560c-eb27-3280-9b12-4e0f4a650532 | -8.07966 | -40.28784 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 92389a06-7bbf-388e-bc78-6804ac987093 | -8.07921 | -40.28441 | 2024-10-25 15:33:00 | NPP-375 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 62088449-d8d2-3cf4-8264-64e9074e9147 | -7.95164 | -40.54736 | 2024-10-25 15:33:00 | NPP-375 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 67de183d-9f68-312f-be30-b53422a3ce3a | -8.20473 | -39.86714 | 2024-10-25 15:33:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4d4c1a37-b705-35eb-9a39-256401c0e335 | -8.12812 | -39.53771 | 2024-10-25 15:33:00 | NPP-375 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2d26d7e2-748c-3fd8-a7fb-0725867ca057 | -8.64585 | -39.69889 | 2024-10-25 15:33:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 53c07333-7b16-35b6-a0d9-0c133a60c214 | -8.52082 | -39.72249 | 2024-10-25 15:33:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 93313e5c-2c27-3d70-9ff2-3b764b34f95e | -8.51558 | -39.7232 | 2024-10-25 15:33:00 | NPP-375 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| eb2f1520-7d8b-3ac1-b71d-cc12e2eaf234 | -8.91576 | -40.43933 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 7840ddfb-bb7b-3a58-b5ba-6f1df78348be | -8.91531 | -40.43571 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| a948be59-bd0d-3dc7-97ee-7960ed9c358e | -8.68888 | -39.41847 | 2024-10-25 15:33:00 | NPP-375 | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 085b3055-296f-3f45-b2ec-42bd3daeec14 | -8.05355 | -39.33159 | 2024-10-25 15:33:00 | NPP-375 | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2135c27e-daaa-3a2f-ae12-c2f6d599b126 | -7.95119 | -40.54659 | 2024-10-25 15:33:00 | NPP-375 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 790c380f-fac4-367c-9462-4d93fa22547d | -10.62238 | -39.88363 | 2024-10-25 15:33:00 | NPP-375 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ed77958f-0603-3b76-919a-7dc1ac746b9d | -10.62201 | -39.88464 | 2024-10-25 15:33:00 | NPP-375 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 19d500ac-b553-3fc1-927a-2d254dcb3f92 | -10.28748 | -39.93683 | 2024-10-25 15:33:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9f6dc038-a6d2-3c6c-b9e1-b29f956b3c52 | -10.2738 | -39.96011 | 2024-10-25 15:33:00 | NPP-375 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 30b1c3fd-0196-3da0-b184-576c8592d2fc | -10.65066 | -40.1198 | 2024-10-25 15:33:00 | NPP-375 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 165cce74-11de-376b-a534-0c2ff50332f6 | -10.64645 | -40.12101 | 2024-10-25 15:33:00 | NPP-375 | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1920d6ab-8983-33c0-b0db-45cb8f800c80 | -10.43232 | -40.42294 | 2024-10-25 15:33:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 8786a145-8d19-330e-83ff-48c6aa3304f8 | -10.36304 | -40.36984 | 2024-10-25 15:33:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d354dcda-52ea-332f-a105-94c81396da68 | -10.35141 | -41.00316 | 2024-10-25 15:33:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 883eb37a-e6fd-3fd6-a4ed-97a37ac14973 | -10.34947 | -40.99971 | 2024-10-25 15:33:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 0b68dc66-982b-34f1-9a1d-2f6b84fdb9b0 | -10.34482 | -40.30065 | 2024-10-25 15:33:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 07f0f182-5543-38e8-bb43-34bca4228068 | -9.46368 | -40.62963 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7d104ab3-b2d8-3349-9022-4c27cbde1195 | -9.46159 | -40.63225 | 2024-10-25 15:33:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 18bd8eb5-fe6b-36e2-824d-91940b1d5198 | -9.48224 | -40.79018 | 2024-10-25 15:33:00 | NPP-375 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 076c4fcd-73df-391c-980d-2b26237afb8c | -9.47799 | -40.79251 | 2024-10-25 15:33:00 | NPP-375 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f32529c2-a1d7-3e20-820e-5b1b1994b4aa | -9.47654 | -40.79091 | 2024-10-25 15:33:00 | NPP-375 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8821ef95-37f6-3d44-9a1e-4886013d01d4 | -11.41216 | -40.19032 | 2024-10-25 15:33:00 | NPP-375 | QUIXABEIRA | BAHIA | Brasil | 2925931 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b9c98f81-2790-398c-8cac-58c1ee115e34 | -11.40869 | -40.19091 | 2024-10-25 15:33:00 | NPP-375 | QUIXABEIRA | BAHIA | Brasil | 2925931 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c5519add-dd44-39cb-93e6-746a625ed25e | -11.40722 | -40.08808 | 2024-10-25 15:33:00 | NPP-375 | QUIXABEIRA | BAHIA | Brasil | 2925931 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5d13dc59-3695-3785-85cc-77d076b9f6ec | -11.2735 | -40.61432 | 2024-10-25 15:33:00 | NPP-375 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 10190335-0543-3674-82a3-7082db815c2e | -11.19584 | -41.43961 | 2024-10-25 15:33:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 11838903-8adb-3fc1-afab-b534a40efd54 | -5.07753 | -40.57056 | 2024-10-25 15:33:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82afbb07-3986-3948-a8f5-660c3b642556 | -4.96033 | -40.53292 | 2024-10-25 15:33:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85287c21-a96d-3bf2-b2ec-faffad7e4774 | -4.93701 | -40.5197 | 2024-10-25 15:33:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5d9427f7-de5c-3ee1-bfb9-5736784958fe | -4.77451 | -40.1696 | 2024-10-25 15:33:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| d715a695-bf5c-3c42-b347-7a2914e1acb4 | -4.77411 | -40.16682 | 2024-10-25 15:33:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 27.0 |
| f38c2704-feee-3b2a-8d41-d234931bd659 | -4.70221 | -40.13646 | 2024-10-25 15:33:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |


[Clique aqui para ver as próximas entradas](README125.md)
