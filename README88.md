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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14728301-566d-3503-ad93-471008f2fe04 | -2.88757 | -53.99886 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 927a7a53-c05a-3289-959b-7c2ba1aa1e83 | -2.64582 | -54.28547 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b6f6a14-9661-3faa-90cc-7936b0e8a912 | -2.98087 | -53.28777 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| d0d46d5e-7fc8-3176-8fd0-72f7bd9535df | -3.11475 | -53.26143 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f8dc6d8-9bee-3aa2-b6c4-16b48b4d324b | -3.49704 | -50.46286 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a67eea4-7362-32d9-9bc2-ad3f31b15e57 | -2.84141 | -46.81496 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89385f5b-48a4-3c95-98ca-9f3ef43739ca | -4.28077 | -55.73896 | 2024-11-29 05:22:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e3cf256-5575-3378-b6ae-ccb40c16e55a | -3.53568 | -50.19505 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e579c2f4-27ca-367f-ba75-0177b54deaef | -4.26028 | -47.61544 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3d2f027-ba8b-3b61-934a-c8fdf36744d5 | -3.52517 | -50.38437 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 076627dc-cc2d-35fc-9e10-1a409f77df5d | -1.71442 | -52.63577 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b88a91b-861f-324b-aed5-dc3b5c4752eb | -2.02347 | -55.21043 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9560b556-f083-3a2e-b1b9-18d8e768f061 | -3.41761 | -50.15974 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ff673df-d7df-3de8-ad0f-a0bd66226fc4 | -1.65816 | -52.73019 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcb5d640-41aa-3b2c-a231-e7ac58268adb | -3.5043 | -53.82529 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c75fe363-d701-3c55-bb42-2bf8e156d84f | -3.19064 | -54.32647 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5d008ac-b484-3f14-96bb-f9fed6a91696 | -2.59914 | -53.96915 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3b06cdc-8622-379e-aeb4-cf0cffdcaf49 | -3.3303 | -50.22005 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78dc81d4-ae4b-3e22-b383-a78eaaff8b76 | -3.96303 | -48.08109 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cca8e473-427b-3489-8074-bfcefcd4f3ef | -3.27921 | -50.03809 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a9051a6-4206-35a6-9bc3-8893e92e0482 | -1.69694 | -52.44123 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86b1f7a5-7731-3d7e-bf5d-cf83521292ae | -3.53067 | -50.38512 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d8423d-ea4b-3b8f-9878-0fc04f859109 | -3.28473 | -48.76704 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 981a31ca-6600-31b2-9503-34c5ea35c7ce | -3.46423 | -50.52959 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55da69f1-e209-34cb-bd16-1ddbed8a126d | -2.61627 | -54.20033 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 533116cb-7403-3a45-b9c8-d538aec65653 | -2.86817 | -53.98387 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 402d4d81-ad98-3a37-b944-6a6fb77f790a | -4.26107 | -47.60989 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc7a0184-4163-3e96-87cd-84be42936fcd | -1.42823 | -54.30241 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e9f36ba-6a33-315d-94e4-b8fab790f223 | -1.662 | -52.73542 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fb5a234-80cc-3ff3-b2a9-c907c294371a | -1.69773 | -52.4772 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4feefb57-2f9c-3fd4-872d-de5381ef145e | -2.29261 | -51.9803 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb976e2b-1c97-34f5-a24d-de9fc441f752 | -3.49809 | -53.80798 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54d5432d-95b1-368e-bdef-1e74077d712a | -11.36185 | -56.21045 | 2024-11-29 05:22:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40aa34c5-bff9-3374-9be4-44af175bee89 | -1.60166 | -55.43598 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e7e1449-1ca6-3619-bd21-b744dd766007 | -2.6571 | -48.78188 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c916191-bcdc-3779-931c-1ff3b87b22f4 | -2.90269 | -54.18194 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47cf1e76-b48f-3a27-ae8b-bb94c571df3d | -3.68885 | -50.22855 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cfc65bb-692f-3f52-a954-b6c52b002d04 | -2.80041 | -54.06086 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53de5c99-dba1-3f38-9d73-e50b241e85c7 | -4.07536 | -47.03016 | 2024-11-29 05:22:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 372b7bf3-6daf-3933-84c7-68bbf62311bc | -4.15854 | -60.88712 | 2024-11-29 05:22:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21f48617-2f46-399a-bbb0-606d5fd31bc9 | -1.41741 | -55.25676 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f09727df-4c3c-35cc-99e1-d69d0d48165a | -3.47455 | -50.53469 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0c8a379-4a61-3766-8da2-8c96bbbc76e7 | -2.44532 | -53.62595 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 111686c8-064b-3c21-b2f1-3b02f85995d4 | -2.02151 | -55.20723 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cee8a44-6eef-346c-8dfd-9740f631ba19 | -4.51375 | -59.81267 | 2024-11-29 05:22:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb8e3e68-4dae-3ebb-850e-9224180db723 | -3.36497 | -50.40335 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a1814c9-0493-3dca-8a8d-4c54c85ef58b | -1.71964 | -52.47874 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c61b151e-4e9b-3a99-9e78-06174557aafc | -1.35901 | -54.6603 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1651e0d5-6438-31af-9bc9-2f4abb762141 | -3.5296 | -50.19787 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ba7a58-4770-3687-a519-24a4b82a7211 | -2.91295 | -51.71114 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 542cf7d0-2fb9-3a8a-980b-301ec4ff5753 | -2.25456 | -53.74207 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b948d60-0ea2-3acc-bebe-9ae1ef9b0614 | -2.97633 | -53.89011 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5375deeb-3595-33ac-a760-88a281c21675 | -1.62223 | -53.8793 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5774a80d-f091-387c-8cd6-eb2e4eaf6f96 | -3.41346 | -54.90524 | 2024-11-29 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e981acca-ae96-3f0a-994e-9a3e6e64f6ac | -1.70388 | -52.64359 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2805e9e6-0018-39f6-b37f-d7b0ca3798f8 | -3.33738 | -46.69917 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3efc73c9-56d2-34c3-92e8-259e4dcf4925 | -3.15808 | -54.48453 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 171474e3-21cb-3c91-b717-90bc7ebfd0c3 | -3.78686 | -50.12874 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba8c685b-fd9d-361b-ab81-ce07255a6d12 | -3.37049 | -50.82722 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74ed9e42-3526-3ee4-8821-16b7f256d9d3 | -2.23011 | -53.62505 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec52009-fd6d-39c6-afee-fba7999c14ee | -3.57797 | -50.33077 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e8ed5f8-f9a6-392b-9336-8215eedbe6e7 | -3.31628 | -54.18224 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b56de55d-a4c8-3941-b707-351654928604 | -2.6086 | -54.27974 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2d4e20d-7b91-39c2-9034-03db1a2a85fc | -1.35207 | -55.03173 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f5d8059-68f6-3899-a98a-05faf9319aae | -4.69084 | -46.66385 | 2024-11-29 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7182793e-0b70-3380-97b8-c5e095531fbe | -2.82628 | -54.08839 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a3217d0-3caa-3742-8d50-dcf956ac86f2 | -3.67543 | -52.1115 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 752f074f-880d-3e7a-90df-32fea6b4e899 | -2.972 | -53.28619 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 75c0e5db-f411-348a-b6bf-13f44d446b4c | -1.94178 | -52.95889 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f6f0eb9-b5f3-3fe1-b3ef-3718c440da12 | -3.11344 | -53.27012 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c77e7629-3b22-3fb4-b7f6-12f28d24c14c | -3.11286 | -54.47746 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 368910b7-428b-30b7-93ed-4e9d3b4d2bf6 | -3.4125 | -50.16202 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d0bbf37-5a6c-31e3-8663-f3c9cffb8d53 | -2.42414 | -54.0175 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7a4a953-75ba-3fff-b7f1-f399c90f9a3b | -2.77925 | -54.03001 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c6a5bac-699e-37c7-8f43-b2732014ac8d | -7.97787 | -55.30603 | 2024-11-29 05:22:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 520d51d0-e9e7-31eb-8afb-681971bb20f9 | -1.69611 | -52.45758 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 30831afe-50d2-3a20-b255-6b77590dc98e | -4.04465 | -50.32328 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e34935d0-e96e-377b-b8dc-2ac9515fb27f | -4.21389 | -54.76395 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd04fb32-81f2-3872-be1a-f214ace1f726 | -3.59061 | -51.14487 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d03bd067-7401-37cc-aad4-2156f731339f | -2.32064 | -51.95779 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd7fdf64-3d5b-39cd-95d5-f7a2f34b3641 | -2.39072 | -55.2953 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76e08d8a-86f0-3ed2-99df-f58287020225 | -3.95991 | -48.0901 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d32adf7-a903-3fd4-86ef-087c0a935add | -3.32425 | -50.22283 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 643d296d-2512-357d-95bd-6ea87dc89bd2 | -2.65665 | -48.79437 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| bcae9af3-59bc-3e71-b833-488d755939cc | -2.6277 | -54.06664 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b629005-d651-36c0-8f0c-34c6e795bc63 | -3.09813 | -53.80963 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0ac18c4-4312-37a0-9232-699255b6a4fe | -2.69735 | -51.68631 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e166432-10f3-3dbe-9794-1b8843fe352e | -1.35025 | -54.99248 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b72b550-6fba-30e1-a7e3-8b18f1c9c78d | -3.5752 | -54.5192 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ca94e72-2df0-33ba-aa17-22f88fb40c0c | -1.92257 | -52.89019 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b7c0d9a5-8063-3f36-8500-888daf7c301d | -1.68018 | -52.49865 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b2141b-4e98-3bae-a8c9-cb53ceb350aa | -1.34876 | -55.00203 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0de7f637-cf2b-3a9c-88b1-9ff2f8f4d4f4 | -2.8348 | -54.12101 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c41c97f-949a-3286-8266-d16e15d851b1 | -3.09752 | -53.81355 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0c3925d-a664-30c4-8d13-425b66b09fea | -3.6138 | -49.85384 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29a275d3-b8ce-3314-a701-1be250a4362e | -3.20197 | -46.57051 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 407cc593-dbd9-352e-98a2-bb0c95c28bc9 | -1.67496 | -52.52496 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 684eeccd-5ae7-353e-86d0-0e20246eabac | -3.69271 | -54.62321 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ccd8e35-ded5-3e31-9bf5-5de72ddb4e6a | -3.03019 | -54.02325 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1af731d7-a83a-3a3e-9a31-59b73d844180 | -2.88771 | -54.16801 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README89.md)
