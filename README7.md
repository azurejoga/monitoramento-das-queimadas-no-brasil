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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d82ee75-2923-3a81-a08d-4d376898c82e | -5.7725 | -45.0872 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19711f0b-4c9b-319a-9487-7b1270f12223 | -3.806 | -55.887699 | 2026-09-09 00:48:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca122e37-e1b3-3de0-8d48-fd4991f70297 | -6.3541 | -43.583801 | 2026-09-09 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 304d7d4f-93c4-3efe-b297-9b1265a034d0 | -5.8084 | -53.8139 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6643640-d681-3e6e-9073-cc50da7dcc11 | -3.9741 | -47.579601 | 2026-09-09 00:48:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7547d2c3-dcb1-3934-afe5-8e08c0907455 | -2.9532 | -48.593399 | 2026-09-09 00:48:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 628ebe1e-5cb8-3572-a5e8-951ad687d1a5 | -9.7803 | -43.5145 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9f073d6-4928-3699-a9fb-6cb69704d810 | -6.1602 | -44.645599 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dffd0a80-75c3-3582-a143-7747cf0f91f3 | -3.2679 | -50.084499 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9761fc53-10b6-3e50-9b99-63136ef50694 | -5.3645 | -56.018902 | 2026-09-09 00:48:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d465294-f741-3985-b704-983be89caf35 | -3.85 | -54.301701 | 2026-09-09 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6952c798-892a-3fbd-8574-b550094c1651 | -10.6531 | -58.757401 | 2026-09-09 00:48:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1638886f-c412-3cf9-bb82-bf1cfd029186 | -8.0998 | -45.6698 | 2026-09-09 00:48:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cbafd95-a908-3643-bf1d-f808ad80469a | -6.1699 | -44.643299 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66d370bb-2155-3db9-83e6-b7463291685f | -6.8706 | -46.008301 | 2026-09-09 00:48:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 002d5bce-7b88-317f-b1bc-34bddfec7bc9 | -9.2644 | -45.660301 | 2026-09-09 00:48:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 653c859f-9153-3957-bd60-fd8a3985e9ef | -6.3638 | -43.581402 | 2026-09-09 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44173a5b-f4a1-3c21-80a0-3a497c739356 | -8.0926 | -45.682499 | 2026-09-09 00:48:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d8a1546-555b-3012-8ccd-699412b95cf8 | -5.7347 | -43.281799 | 2026-09-09 00:48:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 935b2cee-0852-3e4b-8583-cbd9c75fbb7c | -4.3756 | -55.037102 | 2026-09-09 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70742e45-3edd-31a2-9f73-29b8892ac2b4 | -2.9416 | -50.4585 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8f27710-5c6e-3863-b8aa-c9c516626ed6 | -2.8003 | -54.757099 | 2026-09-09 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa3b92a4-c46e-358f-9b07-6b5663ebf8c4 | -2.7753 | -49.470901 | 2026-09-09 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8366aafd-68a3-3c90-b953-e79b2f7aea88 | -10.744 | -45.966999 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dbc0f251-2c9d-336e-847d-c3a39e051c3b | -5.8066 | -53.806099 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c70009b-56cc-3a0d-bbfd-efb6e275f8de | -10.513 | -47.075401 | 2026-09-09 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16775e8e-d645-3420-ad1c-fa2c4da4459c | -5.7628 | -45.0896 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfd8e0c2-d927-3198-a154-b33fc57bbda4 | -6.8608 | -46.010601 | 2026-09-09 00:48:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba6f449c-14a6-3350-aafd-bad2474f4dd8 | -10.511 | -47.0672 | 2026-09-09 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4b4aeef-1732-3337-9124-badcd8594aea | -6.7966 | -58.940701 | 2026-09-09 00:48:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5682c5e4-6617-3f3c-bd50-38eaf3cfa22c | 2.66561 | -60.1793 | 2026-09-09 00:48:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5b288162-09ff-30a1-b2e8-25ddc9bccf9f | -3.1462 | -60.6506 | 2026-09-09 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 87ff852e-4176-3791-a0a8-1e753f0c4bdd | -6.1726 | -44.6432 | 2026-09-09 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| cf7b2b33-1c92-3ab4-a459-625f657fdc34 | -10.7578 | -45.9624 | 2026-09-09 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e339eebd-f885-379e-a398-4d54c470d8ac | -10.3067 | -46.8964 | 2026-09-09 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| f54922b2-8e27-315f-8d63-d64b06018366 | -5.7571 | -45.0613 | 2026-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 379bbcc3-fe80-3f45-bc9b-df7cbd619350 | -6.3515 | -43.5914 | 2026-09-09 00:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| f4e3c11a-7657-37d3-aeff-d4f2d6ba1345 | -6.3703 | -43.5898 | 2026-09-09 00:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2ee55751-93dd-3277-b2f1-1bf2023c9f62 | -2.9576 | -50.4826 | 2026-09-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ed7d2476-54d2-3ac4-bd36-4d3f4ee1127e | -2.9391 | -50.4832 | 2026-09-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 66ac49f0-3bd5-368c-861e-84caeecdfa12 | -10.307 | -46.874 | 2026-09-09 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 401cefeb-5d29-35df-a5f4-b57adf0e08d2 | -6.1538 | -44.6446 | 2026-09-09 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c930645c-e0e0-3dd1-b49c-3b9f96ffff21 | -6.1536 | -44.6675 | 2026-09-09 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 87ca8937-ee5f-37f9-9be6-d1b334d9e22d | -5.7756 | -45.0826 | 2026-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 1d1f4414-30ee-32b7-bd0f-f8ac5548655e | -2.9392 | -50.4622 | 2026-09-09 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a8c1c235-a7c8-3cd5-9146-8addcac47a48 | -6.1723 | -44.666 | 2026-09-09 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c0bdda34-a74c-38dd-bafd-a0e4fc15c49d | -5.7569 | -45.084 | 2026-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c5bc9148-f395-385b-8065-8d137dca71e6 | -5.7758 | -45.0599 | 2026-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 42b62411-edd7-3dc6-9870-f2024375f880 | -9.7695 | -43.506 | 2026-09-09 00:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| f4786c82-4d8f-3627-bb0f-50ed49f70475 | -9.7885 | -43.5036 | 2026-09-09 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| ff159992-fe3f-3b6d-b3fa-2a6782f2abd9 | -9.7695 | -43.506 | 2026-09-09 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 8abfc5e8-6c18-3382-9321-93a5523e2100 | -5.7569 | -45.084 | 2026-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e4e00c1d-c459-34bf-9fc4-650ee361cb80 | -6.1538 | -44.6446 | 2026-09-09 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 68cb101d-7200-3008-a769-f2014ad21772 | -1.1991 | -55.7106 | 2026-09-09 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| da98a307-fc17-3721-a63e-0d494261edc9 | -6.1536 | -44.6675 | 2026-09-09 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| ac73af99-3303-38ae-ad79-5e4d4f686b21 | -5.8206 | -53.8052 | 2026-09-09 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 510affac-b1a4-3806-8d47-fcda64590c6a | -6.3703 | -43.5898 | 2026-09-09 01:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 374f0ec6-21c9-3eb6-b423-0c2f0b58e6fb | -5.7758 | -45.0599 | 2026-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 50f13ce3-2a11-383a-b04d-1b73c7706963 | -2.9391 | -50.4832 | 2026-09-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| a84f8b70-af12-37c0-8306-5559c462da96 | -1.1808 | -55.7108 | 2026-09-09 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d6eec13d-1174-30ab-86ff-696296f361e8 | -10.7578 | -45.9624 | 2026-09-09 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a75e9f46-6b67-3060-9acc-9543fd1af0e6 | -5.7756 | -45.0826 | 2026-09-09 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 6858647e-73ee-39fc-b8db-2442928581b8 | -6.1726 | -44.6432 | 2026-09-09 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 554eeeca-044f-312d-9489-7719d1eec442 | -3.1645 | -60.6503 | 2026-09-09 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b724b266-1fde-385f-9568-848dac839324 | -2.9576 | -50.4826 | 2026-09-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d43b2d6a-d692-307e-b934-7ea657c39893 | -6.1723 | -44.666 | 2026-09-09 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 2c64a607-74a7-3da4-82c2-046b088e67be | -10.3067 | -46.8964 | 2026-09-09 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7db6e11c-ce5e-3985-8cd9-dc42be82f88b | -2.9392 | -50.4622 | 2026-09-09 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 35e671a9-0220-37d9-b26a-c5547c7c77df | -5.7756 | -45.0826 | 2026-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| a5b87194-b766-3e0b-ad92-725d0a731d35 | -3.2731 | -50.0741 | 2026-09-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2c7cf059-f0f5-3ee3-8279-069f4963c917 | -9.7885 | -43.5036 | 2026-09-09 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5b65ffd2-c20e-3b32-9f34-6bb35af0eb33 | -6.3703 | -43.5898 | 2026-09-09 01:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ed567a90-7962-34ea-a4bf-92193d365782 | -6.1536 | -44.6675 | 2026-09-09 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| eefdfb92-8611-378b-b0c2-47f87c19f114 | -5.7758 | -45.0599 | 2026-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| ec2d1ceb-59f8-31fc-a600-2306ccfbcde2 | -3.2486 | -47.2438 | 2026-09-09 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 13d5d3cc-d97c-3c12-9dc7-963733dfbd99 | -6.1723 | -44.666 | 2026-09-09 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 0eabc28b-5b96-391e-912c-2b8f019cc796 | -5.7571 | -45.0613 | 2026-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2a9d0aa6-3a16-31a8-afc2-0443b99f8e0e | -1.1991 | -55.7106 | 2026-09-09 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7ed34f75-8d5b-3299-8878-25d7cfd5e3ab | -2.9391 | -50.4832 | 2026-09-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| eb374032-59bb-3130-a61d-61e1eb7e82be | -2.9576 | -50.4826 | 2026-09-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 29aa37ac-7d25-3891-ab5a-5547f2a6f6cf | -9.7695 | -43.506 | 2026-09-09 01:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 24fc605e-cf09-307b-ad6c-ab86a83b9634 | -5.7569 | -45.084 | 2026-09-09 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 936e6d5e-f55d-3d79-8c8a-d75907ff3913 | -6.1538 | -44.6446 | 2026-09-09 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 329e6079-7f72-324d-bc43-f6be4e656730 | -5.8206 | -53.8052 | 2026-09-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a2d0655f-7a44-399e-86a8-310f0a61eed3 | -2.9392 | -50.4622 | 2026-09-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| c325a8a3-40a1-32a9-8e74-2b65164853f0 | -6.1726 | -44.6432 | 2026-09-09 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 6cae90cd-d9a6-349c-9450-165c8cd79682 | -6.1536 | -44.6675 | 2026-09-09 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| bbe993b7-2cbf-361d-be2d-ee6f50ebcc10 | -3.2486 | -47.2438 | 2026-09-09 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 20b786c1-ddda-30dc-9fcd-13be5b629e4e | -2.9577 | -50.4617 | 2026-09-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 32224f3d-4d73-3b22-9fa9-a4d48438eded | -5.7758 | -45.0599 | 2026-09-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 1747a03b-4940-38c1-874b-698942e64789 | -9.7695 | -43.506 | 2026-09-09 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 20e1fb2a-f2bc-3591-ae86-f0211e63c9e0 | -5.7756 | -45.0826 | 2026-09-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 4f056498-7542-3757-b759-f211e8074f0a | -5.7569 | -45.084 | 2026-09-09 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 97f422a8-3c80-3534-bce9-8287dafdc246 | -2.9392 | -50.4622 | 2026-09-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 5371e72c-4b23-3643-855f-26918a9e9df4 | -6.3703 | -43.5898 | 2026-09-09 01:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0c71b847-59c2-3498-9784-d88ad21c7e0b | -9.7885 | -43.5036 | 2026-09-09 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 6b71efc6-a956-3b75-8e6b-1b2d70d987b9 | -6.1726 | -44.6432 | 2026-09-09 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 77b6df00-448a-30eb-8f18-070e024744f3 | -6.1538 | -44.6446 | 2026-09-09 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5a37fca6-6669-3d42-aba9-890d82bebbf3 | -2.9391 | -50.4832 | 2026-09-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| d6fd934e-4e44-3ed7-9941-269bfbf57a36 | -6.1723 | -44.666 | 2026-09-09 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |


[Clique aqui para ver as próximas entradas](README8.md)
