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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee434b09-ff0b-38fc-a8fe-9f7e98fec92c | -2.7409 | -54.105 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec02e892-2ed0-3891-9e75-4c841cd67854 | -3.2906 | -53.847 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff37aac-b5ca-3609-8441-dd3e45b7375b | -3.5106 | -50.466999 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28820491-cc6f-3f1e-9a58-95f735cfa3ba | -1.2284 | -51.794201 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecda3f34-ca45-339a-9fc9-56671c4e36f6 | -1.5271 | -47.305302 | 2024-11-23 00:45:00 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e546f70-d420-3cf2-97da-ae8aff204667 | -3.5278 | -53.801498 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd8c6c02-7d90-3b03-8eb0-57495097f7a5 | -1.778 | -53.629398 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 215fe138-a1a0-3320-8f36-e7e1f4f2f62a | -3.8063 | -51.984001 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f67597-5058-33aa-9770-7d79640c9487 | -3.2731 | -53.815102 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2baff3a-72fb-3589-932a-13ad593e4e75 | -2.5552 | -53.9673 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43841620-d576-38b1-8927-a4c455e0e414 | -1.4328 | -53.378502 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08a19777-f35c-3e1b-bf34-6ca61a15c5be | -1.6342 | -53.311798 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f79a15d-9774-383b-b5eb-b24dad77e8af | -3.485 | -49.9081 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d548c366-06c8-3960-afc1-c83233830f58 | -3.2655 | -50.431198 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33a34901-71c8-3749-8e2a-7027766ee9f6 | -3.2559 | -54.2411 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c30d27d-12dc-36c2-9afa-6223e05df9ea | -3.1927 | -54.326599 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29ef08ce-63ae-3566-904d-8de1eaf3dbd1 | -3.2335 | -54.095901 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2776e4db-c413-3ba2-aa84-08aabd00a72c | -2.1575 | -50.449001 | 2024-11-23 00:45:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e94d60ca-b424-35f0-b759-6794c19c4c69 | -2.1595 | -50.458 | 2024-11-23 00:45:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf24556-1691-386f-9882-54b5042e5816 | -1.2131 | -51.953701 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a2610c-4b53-360a-8c41-58e17359bb8a | -1.1935 | -51.958099 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67ea8906-bb05-3443-8d9a-6e37d165d259 | -2.682 | -45.669998 | 2024-11-23 00:45:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9fca83e6-8741-3bb3-9345-a8a4e9cec3fd | -2.5783 | -54.0695 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b32240d-2994-3e6b-9662-589d928f715d | -2.8777 | -51.5728 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82e5fc17-149b-3fd6-908e-e3ff994ff051 | -1.2834 | -54.542198 | 2024-11-23 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0d57a1a-22c4-3b67-8a2c-71ef162e5671 | -2.7519 | -54.016701 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41628725-523f-3501-9574-0ecddb279cef | -1.4637 | -51.108101 | 2024-11-23 00:45:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4acf36-00d5-3653-a556-f4b2a067e176 | -4.6086 | -46.478 | 2024-11-23 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 3840c9d8-f222-3402-9462-95c975bdc2a5 | -4.6085 | -46.5002 | 2024-11-23 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 792afffd-ce7d-3c0a-a9b7-46f3ec786567 | -4.706 | -45.8493 | 2024-11-23 00:50:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| ef5432a4-3421-3d32-a6e4-716d2b85af32 | -2.8123 | -45.1725 | 2024-11-23 00:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 237.9 |
| dff9c644-efb8-3d7f-a9d8-99bd2d176394 | -3.1831 | -54.3247 | 2024-11-23 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5cc631e9-c47e-3933-a8ed-6697b5c78aca | -3.4663 | -48.2349 | 2024-11-23 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fd8cb86d-f22e-340e-9d48-f6158586f67d | -3.7187 | -46.033 | 2024-11-23 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 112.4 |
| facc4bec-0d1f-393c-a778-d047c6bd67e0 | -4.1133 | -42.4614 | 2024-11-23 00:50:00 | GOES-16 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 39e8db6f-022f-35bd-a8e2-db4f3540e916 | -3.7353 | -50.0158 | 2024-11-23 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| be63a324-b8cd-3db1-b646-05b8896efec6 | -1.7175 | -52.7184 | 2024-11-23 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 655a541d-7eb6-32f4-8143-cbdf44af1c42 | -2.8308 | -45.1719 | 2024-11-23 00:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 435.9 |
| ece10845-63c7-3e03-96ca-10796a71c939 | -3.0353 | -45.1644 | 2024-11-23 00:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9361d8fc-1f88-3b41-8cac-9d0cc6a5b2f0 | -2.8124 | -45.1499 | 2024-11-23 00:50:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 278.7 |
| eaeef942-d41c-3bcb-8548-cdfb972deb2b | -3.7372 | -46.0545 | 2024-11-23 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 206.2 |
| ac684303-4680-3e66-8333-1f1dcdcdfd3d | -2.7149 | -46.2713 | 2024-11-23 00:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0fab8ce6-a0f7-3018-b8c5-f0e28a2cc0a1 | -1.7359 | -52.7181 | 2024-11-23 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| e30137a9-3130-33bd-8235-5168e154051b | -4.5403 | -42.9066 | 2024-11-23 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| b8b12e36-daba-3145-a1fc-3651edc4a7ea | -3.2386 | -54.223 | 2024-11-23 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 4e19ee72-12d4-3b56-bdae-029a9663455d | -2.6963 | -46.2719 | 2024-11-23 00:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 45960e46-4064-37de-8508-bbc8d569c223 | -6.4867 | -47.0428 | 2024-11-23 00:50:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 080c94d0-e699-3f22-bd99-0727842538d6 | -3.7538 | -50.0152 | 2024-11-23 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| e702c61d-c491-3778-9951-d18045dffe42 | -2.8309 | -45.1493 | 2024-11-23 00:50:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 557.0 |
| f64bd732-5196-3b95-afbe-df3e192ef6ac | -3.4662 | -48.2565 | 2024-11-23 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 75e562ca-987e-3185-9959-d7716b8dde95 | -4.4196 | -44.1204 | 2024-11-23 00:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 14e23a2f-598c-34fe-b885-6ad9f7694a53 | -4.5402 | -42.93 | 2024-11-23 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0e2b9e28-2fb4-3447-9919-c671c860f3fc | -3.7373 | -46.0322 | 2024-11-23 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 292.6 |
| b6dfa1d0-a207-3716-b23b-97b82409e0f1 | -3.7539 | -49.9941 | 2024-11-23 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| db762562-66c1-3c71-93ba-98761d62e873 | -4.5215 | -42.9312 | 2024-11-23 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 993db8f0-2777-3fe3-838e-d74ffec0407d | -3.2569 | -54.2426 | 2024-11-23 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 281a96e1-72cf-3cbd-89e8-cc0678dde4aa | -6.5054 | -47.0414 | 2024-11-23 00:50:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a707fa83-4dc4-3173-8816-6ee84cc05b17 | -3.7186 | -46.0553 | 2024-11-23 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a0c00ab4-a0a9-32a2-be6f-b24c4dff3991 | -7.0224 | -39.225 | 2024-11-23 00:50:00 | GOES-16 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 09430daa-f399-3618-890e-a8717d05e880 | -3.2385 | -54.2431 | 2024-11-23 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 23e8223c-f611-3cca-b676-734b59e2decc | -3.0354 | -45.1419 | 2024-11-23 00:50:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 65d8413c-7625-3cd2-8a41-08a5f23ef566 | -3.2569 | -54.2226 | 2024-11-23 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 18df811f-8b47-3c74-a6ee-02e1f5fe947a | -4.5216 | -42.9078 | 2024-11-23 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| e0c4eec1-6146-3daf-99d1-338e84fa4feb | -4.67 | -45.6722 | 2024-11-23 00:50:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 8b19f07c-af62-32fa-99f9-b0a8b2ce2f08 | -6.5054 | -47.0414 | 2024-11-23 01:00:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e9bc364a-79cf-322a-a143-0060cbe86be7 | -2.8309 | -45.1493 | 2024-11-23 01:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 341.1 |
| 20b5e30c-f028-3174-a4b4-b6e5b155cad8 | -3.7373 | -46.0322 | 2024-11-23 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e5c0d8bd-d381-37e2-843a-bd7781a520c6 | -4.5215 | -42.9312 | 2024-11-23 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0c410cb1-aaba-31a5-bf22-7430a4df8bf9 | -4.5216 | -42.9078 | 2024-11-23 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7170dde9-b0d6-3026-8e32-34affa557fb4 | -4.6086 | -46.478 | 2024-11-23 01:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| b63929fe-3964-328c-ba71-29fba79bd0ae | -2.6963 | -46.2719 | 2024-11-23 01:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e4fef47c-d7b9-3d24-abb2-23d4c96da0e6 | -1.1287 | -53.3951 | 2024-11-23 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a5addefb-e26f-3ed8-9363-f4d8051428f0 | -4.5898 | -46.5012 | 2024-11-23 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 3112ee9e-03ba-34ee-b6eb-d7efa1cf0dc5 | -2.8308 | -45.1719 | 2024-11-23 01:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 283.4 |
| 8bd8ff66-605f-302d-8674-18bf34d4fc1f | -3.4662 | -48.2565 | 2024-11-23 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 4d21a74e-c99c-39fe-b08b-f9560f2ae601 | -2.6061 | -45.6287 | 2024-11-23 01:00:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 128e3c1f-9c4e-386b-bb65-fae18be15c22 | -4.5402 | -42.93 | 2024-11-23 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 56d3481a-5019-315d-8612-724490f26e03 | -6.4867 | -47.0428 | 2024-11-23 01:00:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| a6d0de5b-020c-3672-919c-3603da2c8b4c | -3.7538 | -50.0152 | 2024-11-23 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| d51cc8ea-4b5f-3447-bf3b-5c6c11ef1953 | -2.8123 | -45.1725 | 2024-11-23 01:00:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 302.3 |
| 9a240d96-48fc-363b-b5ca-0d2a2b696de8 | -1.7359 | -52.7181 | 2024-11-23 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 6aa80eaf-e2bc-3b10-b40f-29eb49f68b0e | -4.5403 | -42.9066 | 2024-11-23 01:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| d03a65d8-e9d3-33ae-a9bb-561f70827d65 | -3.7539 | -49.9941 | 2024-11-23 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e112aa89-8cd3-363f-964a-5be79284d820 | -3.5159 | -53.8132 | 2024-11-23 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| ba70c979-bf38-3116-ae88-c988224d8019 | -4.67 | -45.6722 | 2024-11-23 01:00:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c00aea83-b949-3e3c-8434-478b8f308b3b | -3.2386 | -54.223 | 2024-11-23 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 03409e40-b9a7-3d0c-9306-d76e89a01012 | -3.2569 | -54.2226 | 2024-11-23 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| bfdb401a-dd49-3fe5-92a2-822c1ea2c6f0 | -3.2569 | -54.2426 | 2024-11-23 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 89e405ae-986a-3448-8a00-54c51710688b | -3.2768 | -53.8199 | 2024-11-23 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 433c90d3-bed8-376a-bb91-c0643036f0b4 | -4.6085 | -46.5002 | 2024-11-23 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 164.7 |
| f56824d8-4346-33ce-90db-e2683e1d24f8 | -2.3283 | -45.4353 | 2024-11-23 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 860c8039-94f8-35d5-9e85-90f4b325708c | -4.706 | -45.8493 | 2024-11-23 01:00:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 506e5527-07c3-3675-9530-c70be3e24ccf | -3.2385 | -54.2431 | 2024-11-23 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| d9dc18dc-72f7-3cd3-a660-eb5a6369ef48 | -3.7187 | -46.033 | 2024-11-23 01:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e262b610-f2af-3d3d-b411-21f93ff779b4 | -3.4663 | -48.2349 | 2024-11-23 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 1370558c-1914-3279-b07a-2d85554638ec | -2.8124 | -45.1499 | 2024-11-23 01:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 370.3 |
| feb1a46f-8f40-3975-bc6c-308c9429d9ac | -2.82 | -45.14 | 2024-11-23 01:00:00 | MSG-03 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 905309e6-9b28-3c06-8095-081510026fc6 | -2.84 | -45.14 | 2024-11-23 01:00:00 | MSG-03 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2418b5-5eed-3f3a-ac41-531494e6ec6d | -4.52 | -42.92 | 2024-11-23 01:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 906412e7-3c5a-3b43-92e0-5c5356366f6a | -2.82 | -45.19 | 2024-11-23 01:00:00 | MSG-03 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
