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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da44cf5d-7b9e-3d65-b56d-2a366fe45586 | -13.9353 | -44.5046 | 2024-10-11 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 52f91ac7-bc3b-3bda-92e1-4a4f878e23d9 | -13.797 | -44.6231 | 2024-10-11 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8964b68f-df3a-309e-8b0b-e43e31e81fdc | -13.9348 | -44.5282 | 2024-10-11 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 43d86358-e794-3cfd-8586-abebeded1c66 | -12.29 | -45.33 | 2024-10-11 13:04:14 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c74329a7-b0d0-3215-b782-cdf9fb239879 | -12.32 | -45.34 | 2024-10-11 13:04:14 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a36032f-57e9-3bfc-99af-ba884684d7fb | -7.0786 | -59.4087 | 2024-10-11 13:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 062b2b08-4ec9-3964-9cab-7404a6765def | -7.0417 | -59.4103 | 2024-10-11 13:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 7c69b897-aa5e-3e2b-9016-53b44debf278 | -8.4231 | -55.4704 | 2024-10-11 13:05:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 28fc8bfa-9fc0-3363-9f8a-2aedc9100388 | -8.4417 | -55.4692 | 2024-10-11 13:05:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| f710dc35-c728-3454-a172-ff231b1c2eb4 | -12.2974 | -45.3343 | 2024-10-11 13:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.7 |
| b3606d32-cb32-3b59-a156-e559bf07e49d | -12.297 | -45.3574 | 2024-10-11 13:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 65e2f38b-6441-3dd8-b92a-5b489f6b1274 | -12.3167 | -45.3314 | 2024-10-11 13:06:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 329.0 |
| ec1d5ce5-920f-330b-8005-0673773dba28 | -12.3171 | -45.3083 | 2024-10-11 13:06:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 690f98a1-b3e5-3655-96ea-4b730baa7771 | -12.4757 | -53.1274 | 2024-10-11 13:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 33ed87d6-2b76-34d9-838e-797fabc45c20 | -12.4182 | -53.1544 | 2024-10-11 13:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 37b83cdc-c5dc-3301-84fa-2819cba57758 | -12.3992 | -53.1564 | 2024-10-11 13:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 8762633f-d8c7-3b45-b7cb-eb93147b226d | -12.5996 | -55.1958 | 2024-10-11 13:06:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 126816e5-440e-32f0-8769-bd099422604d | -12.6909 | -45.8712 | 2024-10-11 13:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 480c9ba0-0397-371f-b20d-def858fb37b2 | -12.5913 | -53.0315 | 2024-10-11 13:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| f9bd3010-0b01-303b-a267-a3f9d42c6202 | -13.9353 | -44.5046 | 2024-10-11 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 97eb164d-db70-33c4-8d76-0512b990ca01 | -13.8559 | -44.5892 | 2024-10-11 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 3eec543d-e04f-3440-838d-715fc3d6d5d3 | -13.9348 | -44.5282 | 2024-10-11 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 19cd27cb-f74a-3699-9216-7c6961c2d190 | -13.797 | -44.6231 | 2024-10-11 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| e764ff1c-04f3-31c4-9859-47527c278a60 | -14.1197 | -44.9637 | 2024-10-11 13:06:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4e0c5536-2186-39a7-b532-57d0d8123607 | -6.747 | -59.3259 | 2024-10-11 13:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 5b278251-f0d0-3918-b637-3e2e7e8f8fd6 | -7.0786 | -59.4087 | 2024-10-11 13:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 140dcfd6-113d-3947-9ea4-721214f2d894 | -8.4231 | -55.4704 | 2024-10-11 13:15:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e1142b82-fc00-3af9-8d3d-97c5a8537ec7 | -8.4417 | -55.4692 | 2024-10-11 13:15:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 13a4dafc-dcfb-3bbe-aa72-beeb56fa15cb | -12.1266 | -43.1829 | 2024-10-11 13:16:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 90500ad7-d995-349c-865b-3134e7dfe549 | -12.2974 | -45.3343 | 2024-10-11 13:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 30f6a640-d17f-350f-8787-ee0160b8e66c | -12.3167 | -45.3314 | 2024-10-11 13:16:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 20933654-f1cb-326b-8fb7-63b11db1dfea | -12.3171 | -45.3083 | 2024-10-11 13:16:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 59df4989-89fc-30df-9350-3c744e1dce33 | -12.4182 | -53.1544 | 2024-10-11 13:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 610b2666-a37c-33f7-a23c-9ebe63adb29f | -12.3992 | -53.1564 | 2024-10-11 13:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 2d21aa0a-8d14-3f38-a666-5d607a061d04 | -12.6909 | -45.8712 | 2024-10-11 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a683643d-04b8-3438-82be-f0cda918bc5a | -12.5913 | -53.0315 | 2024-10-11 13:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 87c1c5e2-b0bd-37ba-8482-d0bb64ae3f33 | -12.5994 | -55.2162 | 2024-10-11 13:16:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 571699ec-b3d0-3133-a33c-08290d01afcd | -12.5916 | -53.0106 | 2024-10-11 13:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| c4ad0779-c43e-3249-948f-4fb4b5eb2cdd | -12.5996 | -55.1958 | 2024-10-11 13:16:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 3bec28fd-c0b9-3d55-953e-f7858b490805 | -12.9658 | -53.511 | 2024-10-11 13:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 0fa62a28-5377-39f3-b7d6-e73030231fb8 | -13.9348 | -44.5282 | 2024-10-11 13:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 5b24aac0-3762-3a68-9c9b-ca88c25cb0f9 | -13.9548 | -44.5011 | 2024-10-11 13:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 475d4fd8-5a6b-3d6a-abf2-082c65f72d1b | -13.9353 | -44.5046 | 2024-10-11 13:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1e869882-03a4-3e24-bd30-c68a42c22600 | -14.1197 | -44.9637 | 2024-10-11 13:16:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| cc53f4da-104a-3d6c-b604-6164ee26b56d | -6.7654 | -59.3252 | 2024-10-11 13:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c55c0207-f20a-3c2b-87f3-745cfac3a405 | -6.747 | -59.3259 | 2024-10-11 13:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 6c9f4ba8-2f64-3e0b-a1c3-fa2795d34847 | -7.0786 | -59.4087 | 2024-10-11 13:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d3d678e5-50be-30ba-8b4f-0002c49caa7d | -7.0601 | -59.4095 | 2024-10-11 13:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b3aba8c7-a6eb-3923-a79a-2be69b1bff91 | -7.0417 | -59.4103 | 2024-10-11 13:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 1c362d1d-b568-3ab9-9a02-98247b7b7f08 | -8.4417 | -55.4692 | 2024-10-11 13:25:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 15bf70d6-19f2-372d-a17b-c3376dfa9271 | -8.4233 | -55.4503 | 2024-10-11 13:25:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b922d996-9b07-3558-9a60-6b88e4eb68f0 | -8.4231 | -55.4704 | 2024-10-11 13:25:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 64edc39a-454f-3b01-952c-421e29cc9e94 | -10.7151 | -53.0337 | 2024-10-11 13:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 814305a1-911e-35dc-aa1b-41d466669012 | -10.6962 | -53.0354 | 2024-10-11 13:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1e9a6820-904b-3e9a-8189-49c09b5b9183 | -12.1266 | -43.1829 | 2024-10-11 13:26:14 | GOES-16 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 6eaefdce-df94-34d7-963e-76b030f88237 | -12.2978 | -45.3112 | 2024-10-11 13:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| cbc172b8-0e96-3a94-9bbc-04940bc4a760 | -12.2974 | -45.3343 | 2024-10-11 13:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| fe66607a-7f2c-3050-97de-a94fa0156a5b | -12.3167 | -45.3314 | 2024-10-11 13:26:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 240.5 |
| f16ed15c-e41e-3b8c-b145-f0c7a2526b54 | -12.3171 | -45.3083 | 2024-10-11 13:26:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 09068b2f-20a4-3bde-b3fa-2134418e6f64 | -12.611 | -52.9876 | 2024-10-11 13:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 50d5f9d1-d398-3dff-846c-11970550c08e | -12.5994 | -55.2162 | 2024-10-11 13:26:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 6ecc4360-4fa4-3a68-b2ed-db98084129d4 | -12.5916 | -53.0106 | 2024-10-11 13:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a18e0d73-0bdf-36dd-8830-a79d3f026236 | -12.5996 | -55.1958 | 2024-10-11 13:26:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 05c81b69-5faf-39b3-b348-c4bd524e0570 | -12.6909 | -45.8712 | 2024-10-11 13:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 277.4 |
| 5dfda40f-c552-3d96-a70f-fdf62f0c8718 | -12.5913 | -53.0315 | 2024-10-11 13:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| cd56e419-0b1f-30af-a116-59285b132373 | -12.9658 | -53.511 | 2024-10-11 13:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 274.1 |
| bf9b41f0-b0c2-38b0-a00e-839a35659f77 | -13.534 | -40.6789 | 2024-10-11 13:26:22 | GOES-16 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 612d931d-baaa-3a60-9e2d-9475afd7316b | -13.8739 | -44.6564 | 2024-10-11 13:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d924910f-8555-3402-9ff3-4cdd49ef08ed | -13.8933 | -44.6529 | 2024-10-11 13:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 9a887a66-fb24-3368-b34b-930977e3e7d4 | -13.9353 | -44.5046 | 2024-10-11 13:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6948aaed-ea28-3797-838c-d84e6a4f08a1 | -13.9333 | -44.5989 | 2024-10-11 13:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 8a757213-bedd-3077-a70b-6be68da66a08 | -13.9543 | -44.5247 | 2024-10-11 13:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 152d4736-80d6-3c37-80c5-edfba145e34d | -13.9328 | -44.6225 | 2024-10-11 13:26:24 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 43837664-a517-3625-afdb-c4ae031632d4 | -13.9348 | -44.5282 | 2024-10-11 13:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| adc41b85-f30e-3c73-970b-f7ce59e06f3d | -13.9548 | -44.5011 | 2024-10-11 13:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2407f6f9-0a90-3e13-a2ac-81b49e236654 | -14.1002 | -44.9672 | 2024-10-11 13:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b2469735-cd08-3803-9f5d-a2f3a546bcc2 | -14.1192 | -44.9872 | 2024-10-11 13:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9b3a8376-c31b-35b4-aa6f-bb8c15fc18cd | -14.1197 | -44.9637 | 2024-10-11 13:26:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ebebe2a0-1d04-388d-8164-21a734e59717 | -14.8001 | -41.6588 | 2024-10-11 13:26:29 | GOES-16 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 134.1 |
| 93d0f0a8-e109-392a-8a9b-58f11b32ee4f | -7.0601 | -59.4095 | 2024-10-11 13:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 481bdbbd-f635-3e3c-a0a5-34314ea1fe56 | -7.0417 | -59.4103 | 2024-10-11 13:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7b6750ad-db64-34da-86b0-2cd288bdb363 | -8.4233 | -55.4503 | 2024-10-11 13:35:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| b063f118-9241-3e30-bdf1-e71749704515 | -8.4417 | -55.4692 | 2024-10-11 13:35:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a102037b-6fd0-3752-b12c-493509541749 | -8.4231 | -55.4704 | 2024-10-11 13:35:55 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 244c1d83-2c98-3106-9090-2ff0aa29efc4 | -9.8367 | -60.2783 | 2024-10-11 13:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 41c33384-ec31-3f09-b897-a5b9adb07443 | -10.7151 | -53.0337 | 2024-10-11 13:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 6fb991a1-4fcb-3317-922b-0363d8b3683e | -11.2597 | -53.272 | 2024-10-11 13:36:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 14d3f381-1750-3efa-8bdf-56b021aca09e | -12.2978 | -45.3112 | 2024-10-11 13:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 4d26bdd4-cb56-327d-b24f-89835f170428 | -12.2974 | -45.3343 | 2024-10-11 13:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 06f8b8c3-f31f-35bc-9e9c-1445449770b1 | -12.3171 | -45.3083 | 2024-10-11 13:36:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| e9ae176b-ca8b-3509-af0d-68ed8be79ac4 | -12.3167 | -45.3314 | 2024-10-11 13:36:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 6ff7d8c1-126e-3e39-8e43-4bc6f7fc052d | -12.4373 | -53.1523 | 2024-10-11 13:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 1a2e0263-1392-3381-bb57-dea396cd9632 | -12.4754 | -53.1482 | 2024-10-11 13:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 228fd793-45af-3fca-ae5c-806d285de4f9 | -12.3989 | -53.1772 | 2024-10-11 13:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 363.1 |
| 7ebba884-865a-3425-b291-8efa1b78ae7b | -12.4182 | -53.1544 | 2024-10-11 13:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 459.6 |
| 274e5d9c-ce98-3b87-8aff-860cadb6cab9 | -12.4563 | -53.1503 | 2024-10-11 13:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 154.8 |
| f3cede16-df11-375d-9b2a-2d164f75b402 | -12.4179 | -53.1752 | 2024-10-11 13:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 182.8 |
| 817a53d0-86a1-3e9d-a768-dff85226a488 | -12.5913 | -53.0315 | 2024-10-11 13:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| b31a897f-2d2a-33ba-b65a-e2a0d0499cbb | -12.6909 | -45.8712 | 2024-10-11 13:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 3a4740af-ec87-3237-955a-f6ee994559d6 | -12.5996 | -55.1958 | 2024-10-11 13:36:18 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |


[Clique aqui para ver as próximas entradas](README120.md)
