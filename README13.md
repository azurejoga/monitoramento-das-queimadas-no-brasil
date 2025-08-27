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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b15d89a3-0e9f-3fc1-9b42-6e4bc0e8fd74 | -10.6027 | -54.8862 | 2025-08-27 01:11:00 | METOP-C | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c6daf11-2863-3eae-affe-fc82a3ac794b | -7.1793 | -59.728802 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba4ff23c-c026-3fb8-8587-9a450de94d52 | -7.3472 | -57.621399 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3056c2-b2bf-3fb4-b18b-b0f94e084b38 | -5.7989 | -59.2062 | 2025-08-27 01:11:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98467cf6-871a-3e43-ab4b-16a66dd34466 | -6.7965 | -59.6231 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73b34072-b9d8-3397-860b-2808114eaf0b | -9.1556 | -59.57 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8aa8d5d4-2311-36d1-92e5-e90f6676f420 | -21.5805 | -47.4683 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b9986ea7-6de9-3889-8e75-332e3029d4ab | -9.1934 | -60.790401 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 090c2c63-4b1e-3e83-bc98-b3552c8bdb9c | -19.556499 | -47.523602 | 2025-08-27 01:11:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4f9484b6-a133-371e-b943-89b8927fcc91 | -9.0745 | -49.591599 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82de93e6-53ad-31d2-8c9a-1f3b2de7c66f | -6.7885 | -59.633701 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b524ce62-9efe-3ed7-843b-b96c35774ecb | -9.5604 | -55.380501 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f301e3f-bcfb-3cc3-818c-f297db451e9b | -9.593 | -55.3876 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc87c23-1ac8-3f15-a09b-e18d6ee7ba0a | -9.405 | -60.536598 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cff29bb3-01d5-30a0-9ad3-7985b1beff60 | -8.9274 | -65.905502 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92ebbb12-629f-30d6-be17-7e68c558cfa3 | -8.8892 | -60.755299 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd1b437-895c-3e2c-a54d-6d29babf7a0e | -21.5777 | -47.457298 | 2025-08-27 01:11:00 | METOP-C | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f2a1dca1-be11-345e-8794-9eabb6183ba0 | -9.4201 | -60.5117 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eda880c0-70f7-3ab3-a247-f3832f3c3a69 | -9.1811 | -59.4986 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60f34d6b-da2d-3c18-9b55-c0cd35ad88f5 | -7.482 | -61.3461 | 2025-08-27 01:11:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72ed413b-4278-3498-b62b-4ed5b29fb618 | -9.2771 | -56.9067 | 2025-08-27 01:11:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75431435-0b76-3b48-8366-4e71fe1fd464 | -6.9457 | -59.555 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca15615a-cb28-3e29-b891-00b569d0da20 | -5.6153 | -60.224998 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9a02a1-d110-35d3-829e-7ad94909d97c | -9.1694 | -59.445 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1544eed1-63ea-3491-a8c7-4367de3a42fa | -6.8462 | -58.968201 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c49f9781-5e5c-3971-b509-928deb968790 | -6.815 | -58.966702 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d104649-2b70-3ae1-897b-00bd5ae6afdd | -7.4796 | -61.335201 | 2025-08-27 01:11:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47d964c8-8ae9-3c31-a5a9-ffbf17a05b9d | -8.887 | -60.7449 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f20dd349-b22a-3c27-a854-5316de72ba58 | -10.4207 | -57.701698 | 2025-08-27 01:11:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bec6a05e-d6bf-3a6d-a12a-3c6a2f62d158 | -8.899 | -60.753201 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77a4ed15-913e-37c7-aaca-ad894b87e0bf | -9.1928 | -59.505402 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 320b56d0-be44-3e90-b659-ea745f74171d | -9.4005 | -60.5159 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6169a1f-a3da-3fd7-82fb-60b2b8e7c9ed | -7.7088 | -45.767799 | 2025-08-27 01:11:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3696e01d-56cc-3376-bb34-4758537144bc | -8.9565 | -65.899696 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 048be035-1316-3c05-bd18-e5e1fd6de41d | -5.7595 | -53.763901 | 2025-08-27 01:11:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae9f1ce-a7b0-3802-bb51-4f5633d28ef4 | -21.156 | -48.553799 | 2025-08-27 01:11:00 | METOP-C | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7d9ed94-6a83-3946-95e0-365ac2a9d2e9 | -9.4081 | -60.503502 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78e1c294-928e-354c-bb33-98b13be64016 | -6.2561 | -60.0117 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 331ec841-1dd9-3c69-b311-b907ea907891 | -21.365601 | -44.2169 | 2025-08-27 01:11:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f1c6b2b-0e43-3bd7-bc9d-ece3681cb974 | -5.6173 | -60.233799 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04879da4-2c6a-333f-a50a-6f8766b64617 | -7.3499 | -59.664398 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c53327e-35fb-3f95-b0e5-9e8a5c227cfa | -7.1695 | -59.7309 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ddb8411-1311-3e47-bca4-56779eae9aa3 | -9.4046 | -62.464001 | 2025-08-27 01:11:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ddecd3e0-0c6a-3c9e-b90c-123bb2012ecc | -6.7134 | -58.5583 | 2025-08-27 01:11:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 938fa2d4-c720-3149-9c17-df870a906fbb | -9.1615 | -59.549801 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa598172-b6d2-302a-a1cb-7a843b606827 | -8.8968 | -60.742802 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9b4f39-0aa9-3d14-bba8-4f3a46ac10ac | -8.9564 | -65.948997 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca3bbcdc-7bca-3dac-9d05-04db53218ff2 | -9.5981 | -55.364601 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6f99d6-b5a9-377a-bea6-bd1b8e68dc8f | -9.2869 | -56.904499 | 2025-08-27 01:11:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8caf8f2c-a58f-38d7-a907-2e1b52797f41 | -8.9226 | -65.882004 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24a10eb6-d855-3d3d-9862-d53f7cb16d03 | -8.5629 | -51.3493 | 2025-08-27 01:11:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7912f88e-ed67-37ad-aef7-505b2f8db336 | -6.6293 | -53.335602 | 2025-08-27 01:11:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2924a3d-ead2-3ce2-aec7-e9d11675a59f | -9.1517 | -59.551998 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01fd7157-6669-3649-be33-3316609eac78 | -7.4148 | -60.614101 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4af4edd5-9fab-38f3-9650-e2b72798a7cf | -6.7983 | -59.6315 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 509b38f9-8717-3d84-b11f-9d14d0dbf267 | -6.6236 | -53.311298 | 2025-08-27 01:11:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da5d403e-6ef1-3951-9eda-e5bba0617810 | -10.0312 | -59.352901 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2419deeb-1553-39a2-864a-b1ccbff9463e | -9.0939 | -49.5867 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d7f7e05-fa97-30a9-92c9-b314ec50337b | -6.7727 | -59.654999 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44b739dc-d3fb-387c-8103-3e44cf40e7ed | -9.7899 | -64.233299 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17f0c069-082b-3556-b7af-f229c4ccfa1b | -8.0751 | -61.535599 | 2025-08-27 01:11:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 525efa55-cdec-3856-b762-c86d901b5b43 | -9.7862 | -64.214798 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4bffdb-b6d0-3667-8194-42033f724744 | -10.101 | -62.8792 | 2025-08-27 01:11:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8349b945-f0c0-342f-9596-f754ff9f7f8b | -6.8753 | -59.886398 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff6d30ad-009e-3a8a-865a-e22c29b40307 | -9.5816 | -55.382999 | 2025-08-27 01:11:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebfac23-4551-3136-8e87-9801930cc0d5 | -19.5662 | -47.520802 | 2025-08-27 01:11:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 889aa994-a637-32f2-917e-e5e94f61b22d | -19.405399 | -46.1422 | 2025-08-27 01:11:00 | METOP-C | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7a027c0-6e19-305a-b335-a7902fffa83f | -5.3117 | -60.1992 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63e04558-abd5-32c1-b346-76bbfdb3c364 | -7.5447 | -63.828701 | 2025-08-27 01:11:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4af8a8-c78a-395f-b22b-824ad88e4eb0 | -9.8035 | -64.25 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0157cfad-36a5-3b91-acc1-e1791ae16dba | -9.1714 | -59.453899 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7aedb696-83ff-319d-afc7-f801da33c257 | -9.1575 | -59.579102 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8de97211-cee4-3535-87f9-531b2f3c8704 | -7.3489 | -57.628502 | 2025-08-27 01:11:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb9a459-4b5e-39f2-b0eb-a957ed091a3c | -9.3977 | -62.4799 | 2025-08-27 01:11:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| accecfac-3907-3b57-ad0a-286039261ad2 | -21.0987 | -48.826401 | 2025-08-27 01:11:00 | METOP-C | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f47502e1-6345-3b92-abea-2586d71c8f95 | -9.1556 | -59.5228 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbec0d00-9fc2-32f7-b7c6-dae59e602fa3 | -9.6475 | -59.616901 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19a60076-b06b-3e78-9a41-c31220c56d94 | -5.4547 | -60.1497 | 2025-08-27 01:11:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b03bdb15-ec45-3b64-8805-28ad98eef208 | -9.0775 | -49.604 | 2025-08-27 01:11:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4207d39-769e-3993-8695-e8d1f27bad9a | -6.8444 | -58.960201 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0b9f4b-0970-3424-b379-a772461c2cd8 | -8.9516 | -65.925301 | 2025-08-27 01:11:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a29d714c-d123-308c-9fb6-9c2afdf55ef2 | -9.189 | -59.4408 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfe07bfa-58ac-3842-9345-01ab28e9b293 | -9.4126 | -60.5242 | 2025-08-27 01:11:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84a55d67-edad-311c-af47-0bc2cd187b30 | -9.1911 | -60.779701 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa9557e5-7cc9-3566-b2da-31c7079e55ed | -6.8248 | -58.9645 | 2025-08-27 01:11:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3c9f71-85c4-3f87-875c-493c1463691f | -8.9088 | -60.751202 | 2025-08-27 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d3630a5-89d6-3115-8a6b-111b983fc274 | -8.719 | -64.003098 | 2025-08-27 01:11:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68cad33f-89df-3ec4-8b1a-cf2f7ca72df6 | -4.09482 | -55.80937 | 2025-08-27 01:11:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c926f0c4-da6b-35d1-a09a-f64ded1c1aa6 | -4.11302 | -56.34277 | 2025-08-27 01:11:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b657501e-d3fc-381c-a91c-107f67c54746 | 0.77273 | -51.34281 | 2025-08-27 01:11:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d3725283-ca71-32db-9a7b-824cf09e49c6 | -8.9026 | -60.769 | 2025-08-27 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 297f8b37-b25a-3a7e-b1ad-371bbd519e9e | -9.7916 | -64.2461 | 2025-08-27 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 45912609-2044-376c-9430-b0a9d330a008 | -9.0819 | -49.5853 | 2025-08-27 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5510f898-fa25-31c4-b90f-a4cef041b096 | -6.8413 | -58.9552 | 2025-08-27 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 41d9c721-15e9-3cd6-bf2d-53537599f353 | -9.6104 | -40.342 | 2025-08-27 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 1c0935e0-01d5-385e-9183-d1795781879e | -9.1009 | -49.5621 | 2025-08-27 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| e15182e5-feec-339b-b3b4-cd48e84e5ca8 | -8.8841 | -60.7699 | 2025-08-27 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.0 |
| b18beb73-3db4-398e-97c0-e5ba3446c34d | -9.1529 | -59.5609 | 2025-08-27 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f779fa37-4fda-3582-a358-4d58fc0d532c | -9.1715 | -59.5599 | 2025-08-27 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5c7c965d-0085-3c0a-8f1f-fec59f5f2821 | -13.1837 | -45.2865 | 2025-08-27 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |


[Clique aqui para ver as próximas entradas](README14.md)
