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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55d6326d-6fb2-38b3-bc79-eb98a8840eb9 | -9.2393 | -60.914501 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b786e3bc-fdec-38f5-b3d4-5554de63e031 | -10.2451 | -59.66 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d9424ac-aa13-3842-a2ba-8d12d277d2c4 | -8.9828 | -65.404602 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eab8095e-1cbc-3aa0-87ad-75fd9111977b | -7.6205 | -62.710098 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdba2940-e4a9-352b-94c4-176b1dca56a9 | -9.5194 | -60.509701 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6b6afbb-1d71-3505-b471-ff350daf8fb0 | -10.4201 | -64.410103 | 2025-08-25 01:03:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27f54437-a5e6-3f9c-9071-69a15641e42c | -6.2672 | -60.0256 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99cb7707-559a-332a-a638-4ff1557030f0 | -8.8744 | -62.426701 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b26c789-d538-33a1-aa54-fcce7ca85999 | -9.2056 | -59.485199 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94cffa24-200b-3022-90ec-ca59a19405e1 | -10.2598 | -59.089401 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d730f53-4202-34f2-a83d-d94f52a65e7d | -9.2408 | -60.921398 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d818d4ed-6203-3ccc-b868-eb951433f0a0 | -8.2274 | -61.409401 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c7b3ba1-08d4-375a-837c-41307ccdb385 | -9.2251 | -59.6618 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5982c2c5-9fa2-3315-8766-328164343775 | -9.8121 | -64.2472 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7e4a570-b3b6-38b4-8831-2218e2542343 | -12.9989 | -56.8773 | 2025-08-25 01:03:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4635e72e-a0c2-3906-98b1-9e83bf6133cf | -9.643 | -59.641201 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61a39158-9f0b-3c6f-af5f-79258828a600 | -22.5264 | -46.794498 | 2025-08-25 01:03:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f66fb86a-c9ab-3b9e-8166-8cdd55368324 | -10.4181 | -60.291302 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1e52715-ede9-3cca-99db-a069be59db8d | -9.199 | -59.637798 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb7e16d-01e5-3c1d-a5b0-4deb80b0b7d2 | -10.2517 | -59.0989 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d933f257-8ad1-3669-a8a9-02e3aec1ae02 | -9.5734 | -55.366699 | 2025-08-25 01:03:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 269f4394-d4e0-3dbc-b21f-1ca4d2e443ca | -6.2656 | -60.018398 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44bad26c-73e4-3f05-a48e-b1c65c3be9ae | -8.5206 | -63.8675 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b6b77795-2cdf-3a37-87f3-105739a4e66b | -10.4182 | -64.401199 | 2025-08-25 01:03:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d84a60fc-cb8e-3172-87dd-2e32e56e23b8 | -14.2455 | -58.615501 | 2025-08-25 01:03:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 628dbfd7-b874-38b8-86d2-21b24b3ff702 | -6.2411 | -60.001099 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82e42100-1aab-346c-b96f-2529fe7d4fd7 | -8.9946 | -65.412201 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dac9a30a-bee9-3b17-992b-a0ce6cdc2dad | -9.6528 | -59.639 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92aeac46-0e10-3283-98da-fd32562caf0d | -6.9216 | -62.991501 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0072b054-e9a4-3c45-b0dd-bc67711c9e0e | -9.1722 | -60.799 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed05f65d-b65d-35a0-a0b5-99728fc7bc53 | -9.1859 | -59.444099 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e2fa5c8-6f3c-364d-bc4c-ae79087b54df | -6.2819 | -59.9995 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90dac012-466f-39d2-8ee6-579b78cbfddf | -10.0211 | -51.069199 | 2025-08-25 01:03:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4fa3f38-5b11-3f8c-b145-8920d77c7934 | -9.1991 | -59.5019 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bda7a21-a86d-3087-ab8d-00b58ddc1e6b | -9.225 | -59.706902 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca30252b-495a-3497-b55e-2fba0efca1aa | -9.2084 | -60.776299 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74ae86bd-6bbc-359b-82be-9cc8af0090fc | -8.8955 | -62.4296 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7da7e8e7-ba75-3f36-8465-64235d5d20be | -9.0138 | -65.357597 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89948a00-a3a0-3a19-9c20-e259b6946e48 | -9.1449 | -60.768902 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f76179e6-e78c-3f28-bfef-f332ea0e0cc2 | -7.9306 | -63.044601 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4ef81ad-66ea-3314-ad56-eadaf8ca2978 | -9.1737 | -60.805901 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e739244-964b-35c8-849b-cc93967e949b | -9.82 | -64.236504 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3151530-5e24-3459-a9e2-6634aca75fde | -9.0673 | -65.707703 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5aeb7f51-9b7e-3361-9791-369a8a756684 | -9.0003 | -65.390701 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f952e92d-2378-383f-9472-049015597c12 | -6.8231 | -58.939701 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6990628-b03f-39d6-b927-c57c0b708d95 | -11.04 | -51.9944 | 2025-08-25 01:03:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e46c6988-7103-3ec0-bedb-a4c054372666 | -4.9518 | -55.812599 | 2025-08-25 01:03:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| defe246e-7ba2-3cd5-9b52-4e2f47176d51 | -6.2444 | -60.015598 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd48080c-3bf1-3768-98e4-038579c1b20b | -7.6335 | -62.722301 | 2025-08-25 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8072b6-0fbb-30c4-8395-d357cf3fb643 | -8.2243 | -61.395599 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72d693da-faf1-3c8d-83a0-f6819d1cba44 | -9.1639 | -60.808102 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a8824e6-9080-3bc2-a5bf-e4b4c526685c | -6.2803 | -59.992298 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0429ff7-ce9a-3eed-af88-af6fa0053d32 | -7.8324 | -49.9767 | 2025-08-25 01:03:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7476139-7838-32fc-a015-a97a39a97670 | -9.2007 | -59.463501 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb3c1bf6-d3d7-3ef9-b087-77e144692a57 | -8.8759 | -62.433899 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6036cb99-ebab-35dd-b70a-94d4b6d83214 | -9.167 | -60.821999 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dad38942-613f-3c76-9b3d-6d7c7265b97a | -8.912 | -62.4109 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3e41c0-d450-3a29-a269-c9e2cca0dbf9 | -10.2615 | -59.096699 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1fa8064-5c26-3d58-8424-21f04e0932e0 | -9.2007 | -59.509102 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa1db9eb-19e1-351f-9bb8-fa66546bf8ae | -8.8937 | -64.170303 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| feb61d69-57d7-3052-97e4-ebe76d0140c8 | -9.1566 | -59.496498 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7d41f72-89a2-399b-9309-9c71093fd640 | -9.1533 | -59.481998 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b72a9042-8f7e-3583-88fb-82abdb3ad9af | -9.1958 | -59.487499 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3677bb59-6153-3aaf-a530-249dc45d1e86 | -9.1811 | -59.604301 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a67c5c1-1e7b-3008-afdd-f5040198fad5 | -6.8249 | -58.947498 | 2025-08-25 01:03:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6dec2400-22b0-368e-b5e5-396bef1ceed7 | -8.6102 | -62.6283 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 220d8cd6-fa74-33dc-b08a-5d1ef83555b4 | -9.1484 | -59.4604 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf9ad35-6195-39b4-9cb1-eb5234950d15 | -8.8791 | -62.448299 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ffa643e-de9e-3385-8e08-a92aa0e5f393 | -14.2925 | -60.3573 | 2025-08-25 01:03:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be732e0a-149a-39e5-ac1b-6fd60f5c5ead | -9.2 | -60.923401 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0343578-c769-38cc-99cc-7ab150238e89 | -9.8102 | -64.238602 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 97948ca2-9477-318b-b395-415589a2a98f | -9.1655 | -60.815102 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cc7181c-43d5-3f16-ae9a-0cd1cd858ea1 | -9.5707 | -55.355499 | 2025-08-25 01:03:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34e18a1f-8c87-3575-96ae-abfde6363e15 | -8.9787 | -65.385201 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b42fa98-11ae-33b6-b0b6-5ab7e4f290bf | -9.4904 | -58.9259 | 2025-08-25 01:03:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbc54c1-96ee-3a05-9835-357d324a8d73 | -9.0158 | -65.367302 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4d62783-2159-3e5e-93c5-1d03797f6a65 | -8.248 | -61.455502 | 2025-08-25 01:03:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc00c046-e7e0-3161-bb3c-d9fe4b4e7e56 | -9.0498 | -65.722 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b2ca04a-3f7e-3797-8b58-ba2758f311c6 | -8.9347 | -62.420898 | 2025-08-25 01:03:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b13ca71-76f3-3a27-acb4-53d40cab83f7 | -10.6088 | -55.0397 | 2025-08-25 01:03:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de8e84dd-a4af-313f-94d4-5dd524819550 | -5.7444 | -57.572701 | 2025-08-25 01:03:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 233fd3e1-c4eb-37b9-bc7e-f356f47cf737 | -9.1517 | -59.4748 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce9674a-5ae5-3540-8280-ab5177c9890a | -9.1957 | -59.441799 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66fd7317-e76f-356e-a14a-06511174452a | -10.2882 | -60.5397 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8aedd97-b79c-32b7-b339-363a187febcd | -8.9905 | -65.392799 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39193b0e-2510-3924-9b27-501f8fe68ca9 | -9.1599 | -59.510899 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0b9d9b-638d-3e2b-b976-edc595fe773f | -9.0477 | -65.7118 | 2025-08-25 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 685f209a-4208-3ba1-a904-0eb4ec3b2122 | -9.212 | -59.694901 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e070e832-9ff2-3542-b733-f4e4ebe0232b | -6.2427 | -60.0084 | 2025-08-25 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| deed1fda-b31c-38d6-82cf-5e5c11ae994e | -9.197 | -60.771702 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba7afbd2-54d3-3e92-a94d-507b26c353f5 | -9.5292 | -60.5075 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7143fb49-fbe3-3fe7-a473-3fa1b5866999 | -8.6428 | -62.636299 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8449e60e-09a5-3007-b25e-ea1b579b4908 | -10.25 | -59.091599 | 2025-08-25 01:03:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec429858-f96f-31f9-86b4-6daa0dce68af | -9.1615 | -59.518101 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c92f567-40a3-3f3e-9e2c-f4f7c6f57100 | -9.2377 | -60.9076 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf4162a1-fc7d-3fef-b99c-9e1ff45612bb | -7.5329 | -63.810001 | 2025-08-25 01:03:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6066507-dde9-339a-8956-c79e810dd3af | -9.1925 | -59.473 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd63604-29a3-3b22-b26c-dc393a985de1 | -9.1268 | -60.321201 | 2025-08-25 01:03:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc5049c-e3c7-3fcf-b476-b79880ba32cd | -8.6136 | -62.597301 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 73eb5385-b0ed-34e0-a3db-d8a688ca77df | -9.8237 | -64.2537 | 2025-08-25 01:03:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
