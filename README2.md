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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03c51603-ebf0-3945-af27-5cde502a6a8f | -6.8189 | -59.6504 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 0ff2a241-1083-3f46-88d3-8c634dd2fe16 | -2.982 | -48.9598 | 2026-08-23 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 197.8 |
| 1c93570d-8516-3a9c-9e5c-7aea7161e370 | -6.8357 | -59.9571 | 2026-08-23 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 178a9130-7020-3582-8f89-4f8af34de43c | -6.5487 | -58.522 | 2026-08-23 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| e9ef2f43-48b1-3336-b945-f7a5e70384a5 | -18.5211 | -47.1418 | 2026-08-23 00:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 43711650-5e4d-3ef1-b4ee-72f6226964d3 | -5.7615 | -57.5807 | 2026-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 19e5699c-9acc-3b3a-8830-eac88eca5a67 | -6.1285 | -57.8393 | 2026-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 68139104-3f7b-3bc0-b64e-0a12a3cb57e7 | -6.8026 | -62.9212 | 2026-08-23 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| dd7c6b9f-c5ce-3a31-86d1-5caa79f9bc37 | -6.1925 | -53.5231 | 2026-08-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 5fae7c32-80bf-32b7-87fa-205a827ed5bb | -6.8062 | -58.6469 | 2026-08-23 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 41c4227b-7825-3803-b533-ca57457372c3 | -6.8373 | -59.6689 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| debdb4f5-0fa0-3c14-9df0-c52a866d8992 | -6.9699 | -59.0658 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 177.6 |
| e68c12f3-88bf-378f-a816-dcf17d38e35b | -6.8571 | -59.4179 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 53c22f90-0d90-3ac4-8155-b4b0146f9e8c | -18.5406 | -47.1608 | 2026-08-23 00:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 5a83765e-5e39-3264-a57b-4e245756ed5f | -6.9883 | -59.0651 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 0afb7224-1c62-38f7-9678-53e3758b566a | -6.8008 | -59.5934 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7ae3d291-00cb-34dc-922c-78271c2c0a27 | -13.1886 | -51.4447 | 2026-08-23 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 412e91a4-6e36-3ad4-9e75-57b017a48bae | -7.5669 | -61.1906 | 2026-08-23 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| ea8cda5a-7a7b-39df-8a1d-1d56e4849083 | -9.1722 | -59.4629 | 2026-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 96013d93-36a5-3194-9695-772e2e7bc426 | -18.5413 | -47.1375 | 2026-08-23 00:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 354d88b9-36a8-380e-a690-9833d7dde050 | -12.242 | -43.1877 | 2026-08-23 00:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 155.0 |
| 122159cf-75cc-38cf-8aa5-5988d3dab1d7 | -21.454 | -46.1371 | 2026-08-23 00:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 43aa9426-9f74-3a83-a812-6ed9dabffb99 | -6.8188 | -59.6696 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 1764f283-bdc3-31de-9088-20587303f971 | -6.8018 | -59.4201 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3ee57e96-dc82-3f13-9564-6e1929162f04 | -3.0005 | -48.9592 | 2026-08-23 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 186.0 |
| be1d0a4e-04c4-32f9-bc0e-cb699122e9d2 | -6.8061 | -58.6663 | 2026-08-23 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| ba914b5f-5040-380e-982a-8306474205e9 | -6.9698 | -59.0852 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 50bbe550-2228-38b1-a412-bb4c91459088 | -6.9329 | -59.0674 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9955924c-4c49-39d0-916f-e9dc5caf8ff0 | -9.1909 | -59.4619 | 2026-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d6b616eb-37b4-33cf-81cb-72632e7f6435 | -9.191 | -59.4425 | 2026-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 687f40f5-3f7e-3741-a669-b5fb8ecfb985 | -6.1286 | -57.8198 | 2026-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 8c56c5cc-69d2-380e-bf98-a02c3ca81432 | -6.9514 | -59.0666 | 2026-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 40637ab8-1e4c-3741-8325-d33cbe289b11 | -5.7799 | -57.58 | 2026-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 1facb878-aa63-3cef-97ea-904b2c673812 | -6.211 | -53.5221 | 2026-08-23 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ad40d88d-41af-3350-87c4-8e014fc21cce | -6.8188 | -59.6696 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| ff6c6d93-d92e-396f-8635-7a27b7ac8599 | -6.8027 | -62.9024 | 2026-08-23 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| fe74a3fc-6cfc-3228-87e4-567697d52301 | -6.8571 | -59.4179 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 19ecf713-addc-3092-81a3-3836c15e1ac6 | -6.8357 | -59.9571 | 2026-08-23 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1c200096-0c45-3d85-a6b0-bb9476513260 | -6.8062 | -58.6469 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 117.9 |
| d400dd25-1b14-3f72-b81c-9063ca73c404 | -6.1285 | -57.8393 | 2026-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 1b75db62-fab5-3fb7-80e5-1ba2dc6a708d | -6.5487 | -58.522 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| b1949e5b-add0-3d41-b696-8dfbd55d922b | -9.1909 | -59.4619 | 2026-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| fda22af3-7a20-380a-a7c6-0d2833c0940c | -7.5669 | -61.1906 | 2026-08-23 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bceeeda7-3cc4-364b-806f-04746997fb1a | -5.7799 | -57.58 | 2026-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d8ee21e2-f672-3235-aaf8-7db5038f50d2 | -6.9698 | -59.0852 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c3d4ef15-245a-34c6-a8a0-9040ac81becb | -6.6765 | -58.7492 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 194fa4fb-6ad0-3d8d-aa54-4c7edf2d9792 | -6.211 | -53.5221 | 2026-08-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 3577a027-434d-3b2b-a880-675859d760d9 | -6.8018 | -59.4201 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 63ea1955-6c0a-3ced-9253-5bdce050c3ce | -6.9699 | -59.0658 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 4e98d57d-eb10-3cc2-b1d6-c9c9eedb28fa | -9.191 | -59.4425 | 2026-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 9c94ded2-dc18-3db0-9bcb-ffed280bc060 | -6.8061 | -58.6663 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 02956e6d-2659-317a-a321-dc9171f61f47 | -5.7615 | -57.5807 | 2026-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5de6d62b-0468-338b-bf2e-89ad1748dab8 | -12.2613 | -43.1845 | 2026-08-23 00:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 52e02592-6c63-34ba-bedf-6c9d27d60e69 | -2.982 | -48.9598 | 2026-08-23 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 215.0 |
| 53f15123-45f2-35ac-b969-798721d40678 | -6.9514 | -59.0666 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.0 |
| e07808a9-1135-3582-b2cc-22d4fa41a1dd | -6.1286 | -57.8198 | 2026-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 856ac969-49dc-3b3d-a570-47e15ee48e60 | -3.0005 | -48.9592 | 2026-08-23 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 4254f17c-a4de-331b-82cd-1e2927cc3689 | -6.6766 | -58.7299 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 169.5 |
| d8c9af56-cac6-3ebb-bdf7-27ba9ca54510 | -9.3805 | -40.3998 | 2026-08-23 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 22e18b76-999b-3c69-a23f-a5a428e21340 | -6.6581 | -58.7306 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 827e7182-4c70-3097-9169-1fa1cc3ed8a9 | -6.6949 | -58.7485 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 4ec7fc0a-f39b-34b5-8c4b-6753e2fb37d3 | -6.8373 | -59.6689 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 24a0136b-f1d1-3d02-9902-bd8c5c4bb7d2 | -13.1886 | -51.4447 | 2026-08-23 00:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 680d996d-a392-3ac0-8122-0fcf9b21ad99 | -9.1722 | -59.4629 | 2026-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 92f1e4dd-90aa-351f-821b-11846474db43 | -6.7135 | -58.7283 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 072035d8-816d-3ebe-b2a8-f0ba0d1e04a5 | -6.8008 | -59.5934 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 62aba71e-f276-3dc5-bdd2-f7f390ddcda9 | -12.242 | -43.1877 | 2026-08-23 00:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 6cd6bf13-3fa2-304f-82c9-97139b2f8246 | -21.454 | -46.1371 | 2026-08-23 00:30:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| bda01db4-1971-32aa-a5a0-6a298e6453e8 | -6.9513 | -59.0859 | 2026-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 9517fbe1-7362-3ed7-85d5-98315ddff373 | -6.695 | -58.7291 | 2026-08-23 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 159.3 |
| aeb06f02-628f-3765-a9fa-8ff130124cbf | -6.1925 | -53.5231 | 2026-08-23 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| d8cfb054-285f-3363-b81c-cc44be63ce2f | -5.7615 | -57.5807 | 2026-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 7726aa6e-67c9-3ce4-a736-8408258eaa96 | -2.982 | -48.9598 | 2026-08-23 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 584207d2-2917-3cc4-88ed-fbbbc7e3c05b | -9.191 | -59.4425 | 2026-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| fc190c41-6287-3a88-aa87-6910300525c9 | -6.8061 | -58.6663 | 2026-08-23 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3f706f03-7869-3198-89bf-6251f2017369 | -9.1909 | -59.4619 | 2026-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 758a33e7-bd32-3c77-8fe0-f1b1542339ad | -6.9698 | -59.0852 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f35614bb-3ca9-32ac-b1aa-c338865ba5cb | -5.7799 | -57.58 | 2026-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| cfc644e9-743d-3ef3-a3cf-7eb8cb3094c0 | -6.8571 | -59.4179 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 62509daf-d19a-3d2e-93d9-ba241fdd1609 | -6.8373 | -59.6689 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0d44c157-7f6b-33f5-b5f7-fc42d59c7ba8 | -13.1886 | -51.4447 | 2026-08-23 00:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8e5a1a10-963d-36e0-ad45-ff3c6f6feceb | -6.9514 | -59.0666 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| bdb8ff06-50a6-31d5-93b1-a281da897404 | -6.8188 | -59.6696 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 8ccba89a-ccd2-302a-900f-ab241911e5f0 | -6.8062 | -58.6469 | 2026-08-23 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 0ca6a008-4e06-34a4-8b53-ebf4a52870b1 | -21.454 | -46.1371 | 2026-08-23 00:40:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.8 |
| 396e2518-a468-3af9-9034-aadc3f6bf2e3 | -6.211 | -53.5221 | 2026-08-23 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 089ae187-470e-30b8-832c-fb6d03748780 | -6.9699 | -59.0658 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.1 |
| fae9fa5f-6d0d-3e40-abdb-0940fd604132 | -6.8027 | -62.9024 | 2026-08-23 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8ec4bf29-41b8-3d4a-bdf9-56965cc7efbe | -20.2962 | -48.6473 | 2026-08-23 00:40:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 0838a2f0-6580-3fde-93b5-95cd3be88286 | -6.5487 | -58.522 | 2026-08-23 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| d3c4ceae-54d7-3fd9-ab04-076142316152 | -6.8247 | -58.6461 | 2026-08-23 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d0a5c753-3119-348e-8f38-082597b86c81 | -6.1286 | -57.8198 | 2026-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| dfa0e65f-e4f2-3bf4-8b63-8e6adb241089 | -7.5669 | -61.1906 | 2026-08-23 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a7742020-b1c8-32a3-8d33-5164ee7bcfa5 | -6.1925 | -53.5231 | 2026-08-23 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| bedc9040-6659-378b-9b2a-bba326d8a1a1 | -6.9513 | -59.0859 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 9d6e51db-725b-3e45-982d-72e975394693 | -6.8008 | -59.5934 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8b93ef49-dc6e-3dd0-a08a-de94c7fcff13 | -6.1285 | -57.8393 | 2026-08-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| db9c1774-1e41-376d-801a-80add6de0c82 | -3.0005 | -48.9378 | 2026-08-23 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4d01a103-1c8f-3798-ab2d-a9f417265e69 | -6.8018 | -59.4201 | 2026-08-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b7df9912-79c0-332a-ae93-28b5881fbd41 | -17.2637 | -44.88 | 2026-08-23 00:40:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |


[Clique aqui para ver as próximas entradas](README3.md)
