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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a52c919-a28c-348a-b6a8-86494288aecc | -2.4537 | -53.651199 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ded5356f-3f1d-306e-b75a-89293016b3b3 | -9.2024 | -49.474899 | 2024-12-10 00:51:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db73839f-4720-3aaf-9567-39f39a9ce29e | -17.4657 | -47.025902 | 2024-12-10 00:51:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b8939679-5cdb-3b9a-93ef-b919d82233c1 | -2.1741 | -53.6455 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7234f04-fc18-3cff-8e28-4ddbabe2454b | -2.8248 | -53.063702 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed080896-df8a-37bc-a4c2-e930136a9da6 | -9.9969 | -47.963299 | 2024-12-10 00:51:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bfdecd1-f378-3953-bb6b-f4ec0b8070b2 | -16.870899 | -40.828999 | 2024-12-10 00:51:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2e85276-5a7d-3248-ab5a-5a828b5da6c9 | -2.9234 | -52.953899 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3138791-bd9f-3385-a26e-cdea22f3a21f | -3.784 | -50.053101 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46e3a895-9547-37b9-b645-8cd8c75c18e6 | -12.8562 | -51.9412 | 2024-12-10 00:51:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5ad0cc-9438-3652-8e6f-755248660320 | -2.9584 | -53.107399 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddf5b02-4056-3841-8860-ae01104283c4 | -3.8224 | -51.069801 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0055be7-0d6b-3bd6-b975-d843ccc2bf7f | -2.4618 | -53.6418 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b60fecd-903e-33a5-abf6-f8988c627e8e | -6.9184 | -43.509499 | 2024-12-10 00:51:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 772efb9c-a557-3b8f-b2c2-feae192fb6f3 | -3.0492 | -54.230801 | 2024-12-10 00:51:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54837a69-6799-3915-902b-4c06c28d64c7 | -2.9218 | -52.946999 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa085ce-837f-371d-8299-7c69dc0a55db | -3.8241 | -51.256901 | 2024-12-10 00:51:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffecd466-608f-3b3e-aaf0-d661518b0362 | -1.6906 | -52.973999 | 2024-12-10 00:51:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f43ea3d3-076e-358b-8cc4-0fd64dc03563 | -3.2657 | -53.868698 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc9607f-23a1-3fbe-9779-6379375b49bf | -13.1069 | -43.312 | 2024-12-10 00:51:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e1746fef-2735-34b3-ba36-870150bf6df1 | -4.2483 | -47.5756 | 2024-12-10 00:51:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78e47632-98d9-3c98-9788-2cc4667224a4 | -6.9106 | -47.8391 | 2024-12-10 00:51:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25a375d2-7e5a-3832-a604-67bc16c43330 | -2.8614 | -52.547298 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f53ac7e-86d7-3e2b-94d0-8bca32388860 | -2.9136 | -52.9561 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86bb225c-113c-34f2-8581-995939cba5cf | -3.1016 | -53.238201 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c96966-ac80-3f7b-ab0a-b21d470541ab | -3.064 | -53.797401 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85c0615-29e6-3799-b60c-5908d8e0ab88 | -8.2255 | -49.714199 | 2024-12-10 00:51:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99dd2acb-1bdb-3730-8651-dc9ea6213d8a | -2.815 | -53.065899 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c05773c-3ab2-3cb4-8c22-8d2b9b622007 | -1.7283 | -52.778099 | 2024-12-10 00:51:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88c5874e-7f52-37f2-8c79-e63837cc71d1 | -11.5336 | -56.4398 | 2024-12-10 00:51:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5bd7d2b-639d-3247-93bc-c88b3babe5d9 | -4.824 | -47.305599 | 2024-12-10 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc79772-741a-36fe-ac36-aebf2967fe6c | -2.4209 | -53.688599 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 542db56d-4ba3-3883-aac8-922ecfea2568 | -16.8613 | -40.831799 | 2024-12-10 00:51:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb4c2119-0337-3c77-ad9d-c280275e8259 | -3.6339 | -52.679199 | 2024-12-10 00:51:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f5d3fc9-76e5-3f77-9b6d-901dbf017335 | -6.8369 | -44.393799 | 2024-12-10 00:51:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff8363ed-90ce-36df-a470-bfa77d5a429a | -2.47 | -53.6325 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49ac3428-9ab3-3c4c-bb80-5fa86ea36570 | -2.912 | -52.9492 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195750c1-197d-3193-b320-ae9b8a896006 | -15.3728 | -53.130901 | 2024-12-10 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac9aafbc-4474-3a34-a244-cc79747e2782 | -12.2466 | -52.4445 | 2024-12-10 00:51:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b218d3b-1716-3458-8ccc-91c23dbd2794 | -3.6815 | -49.566299 | 2024-12-10 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a160ce6e-3da6-3df3-a6bf-5b6accbebeb3 | -18.774 | -39.8629 | 2024-12-10 00:51:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2a40a147-18d2-3cf8-b4d2-a08eaa86e972 | -3.6106 | -54.299702 | 2024-12-10 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd608482-0cb6-3cf5-a511-3a205408afff | -8.8647 | -47.674 | 2024-12-10 00:51:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34da9c0e-aa60-3f66-9841-67ffb74610f7 | -2.964 | -53.720001 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a33d81-f90f-3c21-87a5-8a0f804eed0a | -8.6949 | -50.184898 | 2024-12-10 00:51:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59409be7-690d-3c8d-9038-0df62bd01f3a | -4.0412 | -50.810398 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6a7b6b-3059-3c9d-9d8c-fab5d3983588 | -3.8777 | -50.369701 | 2024-12-10 00:51:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42ed215a-0513-30b2-adf7-c2e61ecbb2e1 | -2.5553 | -53.4189 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f83888-3735-3297-a257-805261ad99b2 | -12.8529 | -51.9258 | 2024-12-10 00:51:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad9010b-b28a-3925-9a0c-7559dad81feb | -12.3668 | -54.160999 | 2024-12-10 00:51:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4024b7-43de-36d0-b939-03ab821198bb | -2.4553 | -53.658298 | 2024-12-10 00:51:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e00510cc-4433-382a-8cb5-d811b1e8b3a5 | -3.1031 | -53.742699 | 2024-12-10 00:51:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4a75247-c1e3-333e-86f3-3b53c11224f8 | -13.317 | -52.411598 | 2024-12-10 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 469542be-20ab-3308-b845-5a263326e610 | -2.8134 | -53.058899 | 2024-12-10 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6275223b-dd5f-3752-8c96-056d8cab5815 | -13.9459 | -44.348 | 2024-12-10 00:51:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 949ef82c-ed28-3959-bca2-1ef23c7c70db | -2.9119 | -52.959 | 2024-12-10 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 097dcf51-e30d-3e41-9026-102f191d4e40 | -12.5495 | -57.7395 | 2024-12-10 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2f1211b1-c1f8-3d4e-9752-92a94019a872 | -3.0547 | -54.2478 | 2024-12-10 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 281ec1e3-dd3e-3ea0-b542-2cf2c624dfcd | -2.986 | -52.835 | 2024-12-10 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4a0c7d48-d69a-3adb-b263-aa258796744a | -5.8998 | -48.0461 | 2024-12-10 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c7921b76-c6d5-38a2-96e1-decbab9d8fb9 | -12.5427 | -58.3362 | 2024-12-10 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 8b0062a8-2e62-3e88-a2a9-a1a9a377380e | -2.9859 | -52.8554 | 2024-12-10 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 0142c234-1dbf-3df0-a699-ecd4fc6b2e7f | -6.9158 | -43.5185 | 2024-12-10 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 4138b563-3844-3b20-a8de-9f68a7ec789e | -6.9161 | -43.4952 | 2024-12-10 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 9d233c6b-969a-34ed-ba01-9741f0d7b7c4 | -5.9183 | -48.0667 | 2024-12-10 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4bfb279e-e101-3b4e-8acf-fa6ffafd3dc5 | -5.9185 | -48.0449 | 2024-12-10 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 38d2bbe9-dfa5-37ce-955b-ca50a2aa65e8 | -12.5425 | -58.3561 | 2024-12-10 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| bf312cd9-c3b9-372b-8693-a904a600f673 | -3.0043 | -52.8549 | 2024-12-10 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1667a1b8-dc93-3ba5-8c02-449419f32dae | -12.5615 | -58.3546 | 2024-12-10 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 61665cdc-6869-3399-b9da-d97bcf659ee8 | -5.9371 | -48.0437 | 2024-12-10 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a9f56b93-90be-39e8-8692-7ea1a23125f4 | -11.5426 | -56.4438 | 2024-12-10 01:00:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 2a182a37-68e0-3d0c-93c8-789ca035be97 | -2.8199 | -52.9816 | 2024-12-10 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 5bbd1f08-2d7c-3fc6-ab74-3f964f10bea7 | -12.5425 | -58.3561 | 2024-12-10 01:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 68cec28a-2703-36b5-a483-688c29be41a6 | -4.3959 | -47.7618 | 2024-12-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 1ba55398-7c2b-3d2e-ad2b-55cac037bac3 | -4.3774 | -47.7627 | 2024-12-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ea212b9d-884d-3e31-9b9a-3f9fde74e3a6 | -11.5426 | -56.4438 | 2024-12-10 01:10:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| bd88b32a-a27f-3f8c-a817-252051767061 | -12.5615 | -58.3546 | 2024-12-10 01:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2fb6979e-e8bd-3c9a-98da-9d7206b57ba4 | -4.3961 | -47.74 | 2024-12-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ac9c4dd4-7d87-3f83-a5e8-03839bca73a0 | -3.0043 | -52.8549 | 2024-12-10 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| e20177af-e5be-3fba-8012-f6e2f40c9fad | -2.986 | -52.835 | 2024-12-10 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8ce0592d-b95c-35be-959a-b26869c714b0 | -10.1816 | -36.2421 | 2024-12-10 01:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| 4573503b-8fe8-3a77-8cb6-c75c50f31478 | -6.9161 | -43.4952 | 2024-12-10 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8a45e156-95e4-3e7f-9603-02327dff2660 | -5.9183 | -48.0667 | 2024-12-10 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| cac04829-7db7-3397-89d9-f86c3318f7b2 | -5.9185 | -48.0449 | 2024-12-10 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 09a6d48a-f69e-3144-afb9-269a76d9265b | -2.8199 | -52.9816 | 2024-12-10 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ab35e4b8-2202-37ba-b7af-94123737ab83 | -3.0044 | -52.8345 | 2024-12-10 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a42a8ea1-6cb2-3cfc-874b-ece828af1e34 | -6.9158 | -43.5185 | 2024-12-10 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 083ca245-66c6-366d-948e-7c38409fc1e0 | -12.5613 | -58.3744 | 2024-12-10 01:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 017e2bfc-7acc-369e-aad9-3e6b832a166d | -2.9119 | -52.959 | 2024-12-10 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b8354b08-472c-3fe5-a9f8-3596212b27e5 | -2.9859 | -52.8554 | 2024-12-10 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| c6342533-b7d9-3ee0-99dc-eb72f26e380d | -4.3775 | -47.7409 | 2024-12-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f797c439-09aa-3696-b865-6cf005b94671 | -3.0547 | -54.2478 | 2024-12-10 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6579045b-dff5-375d-b7d6-c4cf3befae8f | -2.8199 | -52.9816 | 2024-12-10 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c48ae538-4c31-3cb6-8550-f04f5ee5b138 | -6.9158 | -43.5185 | 2024-12-10 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 99772c9c-d2fc-3ab1-932d-c1d6d5c33596 | -2.9119 | -52.959 | 2024-12-10 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b5e82427-4f55-3140-ae66-d56f4d3d3e81 | -3.0044 | -52.8345 | 2024-12-10 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d34bd6af-d026-30ce-b9df-de68e7aa56c1 | -12.5427 | -58.3362 | 2024-12-10 01:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 32fe6ef4-a518-3973-a5b8-dec376e97129 | -6.9161 | -43.4952 | 2024-12-10 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c17e699e-9429-3f85-a988-cd13898672f3 | -2.986 | -52.835 | 2024-12-10 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1c83f2eb-c200-3060-9c1d-46a4666c675c | -4.3959 | -47.7618 | 2024-12-10 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |


[Clique aqui para ver as próximas entradas](README6.md)
