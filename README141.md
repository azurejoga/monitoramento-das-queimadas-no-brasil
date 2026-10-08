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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 849e88ee-e059-3124-b6a8-43ef7e1ba189 | -3.86231 | -50.4179 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a44210e0-21db-3ccc-923e-66d62a8d5d71 | -2.98042 | -54.13014 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b9e5262-0073-3e80-a52f-a022e96a377a | -3.00275 | -54.23985 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2db9c6e-8a53-3293-ab12-66636a87a328 | -4.80434 | -49.06686 | 2026-10-08 05:23:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3441d3a-c8a2-3376-a819-741032cd3c9d | -3.56161 | -59.43368 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b7cfe88-1495-305a-8aea-7bd2d98b616c | -3.54411 | -54.64133 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04235326-83f1-39c8-83fc-96f243ab25e4 | -3.35227 | -54.16875 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a042af85-053a-3634-84f8-b7f0e550d348 | -3.84877 | -55.98388 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb59b9e1-ca09-32c9-b4d4-fec3b539bc0d | -1.19331 | -54.14285 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0ade4ab-3ce6-3988-9456-192a26a5e34b | -3.30375 | -54.04313 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af4849bc-d58b-3d63-bb01-f5d5651aa9db | -3.02302 | -54.13288 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b614a9c2-f259-3951-b64b-1d5576966abb | -5.69549 | -53.48861 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3496aa0c-ee11-3a37-b34b-08bb44899f16 | -2.50242 | -56.13193 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe399949-154c-38a3-9a15-7c287170b3e2 | -3.20943 | -50.55084 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2853813d-8ea3-37bf-8616-a2f79a1369d9 | -3.99846 | -51.01437 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39b0782b-2b01-333c-9d3c-629beeb5d775 | -2.92771 | -54.11826 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f166d85c-56f3-3091-a03e-2ba74b2517e5 | -2.75825 | -54.09384 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f8f578a-f3c5-31d1-b2c9-d65dc252238f | -3.11385 | -54.17348 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a0855e09-7788-3eca-ab42-1b6e956777d5 | -3.59016 | -54.67858 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6e0e524c-b5b8-3f55-b48c-9164bec766ed | -4.77419 | -55.73812 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91a401de-4b70-35b2-88d9-dd90bfcadcf9 | -3.16608 | -54.73622 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 353fa577-d5cf-3947-b7b7-a68f9eba440c | -2.88042 | -54.12278 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c86340e-8a14-35e9-b437-40d02da70a21 | -4.30336 | -50.78506 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b7fd726-6f75-3b93-a845-4d5e41adf896 | -2.50805 | -56.1824 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bd8518e1-71d2-355d-86c0-b6ae5d96447d | -7.23234 | -55.12193 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c22e21c-9838-3af3-9207-06b1e410b446 | -3.27057 | -54.66837 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 975b1aca-f634-3faa-a894-e9abb6a0ebf3 | -3.53677 | -59.49583 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef229b1-f81e-3f87-8f24-9c05b42440de | -3.27953 | -54.05943 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf1a6b51-0bab-37f2-8b6f-c500a6db67c1 | -1.69895 | -54.87593 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbe7276b-31dc-36d6-a7a6-326b7f9a89f0 | -3.02622 | -53.95009 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58ac65c1-dda0-3fa2-82e1-1275f358e51c | -4.93393 | -55.8133 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1a6b93e-6a96-3be2-95e0-a42231b58c71 | -3.05001 | -54.21193 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a898335a-7038-3051-a35e-903a7275e3ff | -3.00579 | -54.05888 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d28c4068-56e1-358f-adac-b82ace7efc57 | -2.48242 | -56.10754 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f42cfc62-e4e7-3536-904c-958019ed7d4a | -3.40618 | -59.58834 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c93f6b32-e97f-3687-912e-6954c969f697 | -3.08092 | -54.2705 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e079123-1258-34e9-9424-3e097b7c55c6 | -2.96448 | -54.21031 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ce10f7f-81a5-363c-8317-86b0f48b126d | -3.47837 | -55.43561 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbfd098f-1781-3eab-8fe2-ce806c0bb86d | -2.75115 | -56.61008 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bcbb2cb-99cc-34f9-9bad-2b32540b580e | -8.62114 | -67.0241 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 28bcc171-8b52-3498-b12e-db512a094ca1 | -4.34977 | -43.80004 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| db3e2a69-adb8-31e5-92f5-17a706050fb9 | -2.52416 | -58.10033 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb2cf84b-f598-33f9-a007-5bbc27eff05f | -5.70291 | -53.48992 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 644d067c-e291-3b59-b883-1f11e4531bd6 | -2.58075 | -56.16883 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67be24d4-9349-3300-8ca4-25167f3af394 | -2.88332 | -54.12716 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 146fcf03-7fb8-31d5-ae26-1d686002339c | -3.51871 | -59.32489 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1277c5b0-d15d-38cc-80e2-244fab29f595 | -3.09263 | -58.43003 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1f357f9-830d-35bb-b037-9a8436d5be6d | -2.5746 | -56.14307 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 760a094a-dbdc-3b45-b979-e368d96724f9 | -2.48465 | -56.11497 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af948712-dd80-3cb5-bc40-9f9e31b8e56f | -7.38299 | -55.22229 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d99ca1e-8f22-31e8-b2af-08054e81448e | -2.51317 | -56.25754 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89fa8420-fd36-387b-8ac8-843a403a7571 | -3.98551 | -59.33927 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df4e9f0-0e97-3a60-a9db-1ffdda2da634 | -3.40853 | -58.90856 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ab16287-71f6-3313-ac13-90752216b20a | -3.98314 | -56.22239 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47d0465a-9eba-35f3-a624-88ebf4a82400 | -3.11737 | -53.76134 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae2c64a9-210c-30a0-b9e6-44922fbabb37 | -4.30761 | -54.7942 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc3da655-f2a7-3f0e-9411-bedd4ae596a3 | -3.04921 | -54.14881 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bca4d61f-8b78-3fb7-a6dd-2c07841306f7 | -3.51927 | -54.66437 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edf6e1fc-93d6-3fbb-b7d1-8821c597d69a | -4.54 | -54.98554 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a197881e-1097-3dc2-a3f3-6c417a56f4eb | -4.76971 | -55.72281 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37ab88c9-b135-3caa-9c70-8802c23d339a | -1.50568 | -54.81712 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d747a3f2-1019-3523-9b0b-77656b0f9b26 | -3.2347 | -56.82473 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 740b70d9-4b07-3dd9-9718-7c75ccb6c145 | -5.70966 | -53.49563 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7d81436-16b1-374f-b5c8-8ea20b897ac0 | -3.01402 | -54.05219 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bbbef53-ef61-3008-8655-1490f7a29b4f | -3.0428 | -54.25764 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 386ca969-bc7a-3e78-9da4-57e8ce25ecad | -3.01021 | -54.123 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0e15c4e1-4f71-3e8a-b5e3-39718b3a5755 | -3.35588 | -50.47696 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c9fac75-4f00-370c-bf47-eb019b483a49 | -3.93731 | -55.84682 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c29a901-85be-346b-a7f0-5bca2a9dd2c9 | -3.05383 | -53.95843 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 987ce795-c2dc-3bd9-813b-aec9ca3fe41a | -1.09971 | -54.16328 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7792786-1303-3886-a4ed-ebb6b9459986 | -2.98038 | -54.1027 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5793110c-c983-31f5-828c-494fedec0159 | -3.31431 | -54.04478 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a5b608b6-3fbc-3565-aaf1-c7279fdf28b2 | -2.94434 | -54.17199 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5463747b-1092-3136-b68d-cd44094b95ca | -3.49568 | -51.68711 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 485d6867-c2a8-3168-9e0b-0c9b3e68402f | -10.88215 | -49.1503 | 2026-10-08 05:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5e91649-0d3d-3247-b7cc-fa04698f7e15 | -5.69003 | -53.47424 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6675bb29-e700-3c74-9bf2-8cdd1f293bb0 | -5.7102 | -63.14936 | 2026-10-08 05:23:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ba89e72-1e05-39c3-a755-8fc1d3e61872 | -3.48319 | -54.62422 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46579e0d-534f-36f7-bf7a-0a4141f866ee | -3.13673 | -57.67606 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ba60010-eb2c-3c85-84d5-b94691c7cfc9 | -3.54512 | -55.52207 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f5e5656-2def-32b3-8e63-7ce142c0b580 | -3.04061 | -54.22618 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f220ca3d-5f9e-3b39-a786-b96e74f5a937 | -6.64417 | -59.93813 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c1021c9-68d4-330c-9ed6-e93c94870a0d | -6.73557 | -55.1233 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04691041-038c-3adf-8934-2e0e8cbeb7ee | -4.45785 | -47.91864 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c4f56692-ccb2-3402-8f17-9f5d87926365 | -2.96757 | -51.51041 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aeacae2-2ac9-3dbd-aded-0f16330abe72 | -9.47946 | -64.35728 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55ffa189-df3b-3b07-8ec0-5ee8d70895eb | -2.04283 | -56.38507 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09135968-5415-3e01-837f-bf32cbd31cbc | -7.22945 | -55.11749 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4e1e176-dae7-35bc-9c5f-d7a0e7dfd87b | -3.16295 | -50.59375 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8da128fc-5d0b-35ec-aefa-733f887a0a08 | -6.62167 | -59.94254 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 973b1aac-3409-3bf4-8056-e4dddf29e419 | -3.53961 | -50.08911 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc796049-504e-3de6-8c39-3f78adcac262 | -4.30621 | -60.94696 | 2026-10-08 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38f2cc85-245e-32dd-8e75-0af580205674 | -3.15578 | -54.08883 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e469333c-dd09-30c0-8781-66150dbb1f73 | -3.0175 | -54.19117 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b5a221b-efab-3f26-8d57-5c1eecedd849 | -3.55889 | -59.49524 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e05e6ed-4393-3557-ba3a-30b253ab05f7 | -1.60138 | -55.15943 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 667ee92f-4c80-33c1-bcfb-5cf6792d0cc5 | -3.02078 | -54.23875 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a93cb00-fb5b-35ec-8f3b-672b1bccddc1 | -7.38067 | -55.21405 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e31819d2-d7e2-3194-be8e-2960f3ee6918 | -1.2024 | -55.69017 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3eafa9ea-2d2d-3881-9cb8-71b4bc480487 | -9.14851 | -65.30617 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README142.md)
