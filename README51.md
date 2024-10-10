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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e60be370-8c5b-3426-bac1-26daaf3a100d | -3.6851 | -50.12144 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f54e8fdc-bbc6-3cd6-b5b2-43db7d42333f | -3.56192 | -50.37232 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0c3d49a-9ecd-3dc9-aa16-b3a52bb678fe | -5.06371 | -50.75126 | 2024-10-10 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28a5161f-dbec-3734-bb99-dbb0a0592f65 | -5.06274 | -50.75659 | 2024-10-10 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98fbb14b-fdce-3af1-b6af-db46441c15d7 | -6.32354 | -49.98999 | 2024-10-10 03:55:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94d4fac0-8725-3258-9bc0-f553dc6212d8 | -6.31904 | -49.99007 | 2024-10-10 03:55:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86e69951-43c0-3863-97b4-7a41325fabfb | -6.31574 | -49.99728 | 2024-10-10 03:55:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1adc67d5-f990-3053-806b-07570eb4e60a | -6.31115 | -49.9982 | 2024-10-10 03:55:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b1c03905-4c83-3509-8eb5-7586c21e2bdd | -9.24835 | -50.3655 | 2024-10-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0f24d38-5b11-34b5-9df1-4fcb979c56d1 | -9.13867 | -51.49721 | 2024-10-10 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 50b491ea-7761-31f3-8998-260e2cf11c00 | -9.13749 | -51.50332 | 2024-10-10 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0db1d9c3-eae2-3c0b-88d1-0c323c2acfd3 | -9.03545 | -51.47627 | 2024-10-10 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c2cb2ef-6cd6-3dd7-b202-fa8765a655fb | -9.02902 | -51.4746 | 2024-10-10 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5675427a-cdb5-378b-abd3-366bc3303654 | -8.56468 | -50.52966 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29d3d53f-f051-3626-8923-fc7f2c940581 | -8.55847 | -50.52855 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 409df254-7829-3c4b-8fea-b774762e8015 | -8.5051 | -50.80948 | 2024-10-10 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2845fbf0-1e3f-3520-a9fd-474821388650 | -8.22059 | -50.99996 | 2024-10-10 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b6aed3aa-8de6-3727-b74c-a06039126877 | -9.49883 | -50.98277 | 2024-10-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6fba3e8f-31d2-3725-a261-91640f6f5232 | -9.49646 | -50.97954 | 2024-10-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e5cf7bc-82e3-3c92-b704-da617257ac7e | -9.49556 | -50.9841 | 2024-10-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e3dbe53-b7bc-3eb1-945f-f8b870c07374 | -9.49249 | -50.98185 | 2024-10-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e52bebfb-928b-3652-b688-6862f06f54dc | -9.4916 | -50.98653 | 2024-10-10 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70d9af72-cf2b-33d4-88e7-0c7e73ee9a56 | -10.41902 | -50.70998 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f39f925f-a98e-3627-8057-02a8dc2a9a6b | -10.41833 | -50.70984 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e3b23f8-42ad-3506-82d0-88d25f62dbb8 | -10.41809 | -50.71467 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6482f4f-0c33-3a88-91a4-221363d5ad97 | -10.41743 | -50.71455 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d081403-0473-3cab-8d3d-a2c3d9db6429 | -10.41716 | -50.71937 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c2cb296-3901-32da-a5b4-8a57daa6d287 | -10.41653 | -50.71927 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 173b947c-a3af-323e-a624-27d34f47766c | -10.41623 | -50.72406 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 274f779f-6ea7-343c-92f9-62b4d3324f9f | -10.41563 | -50.72398 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b8ceb84-414d-3c63-a1ed-2d209cfe7b08 | -10.85586 | -51.06565 | 2024-10-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 265c7906-92f3-30ef-bb7d-797863482429 | -10.67857 | -51.0971 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 98300608-878d-3526-a024-84cb0a23340c | -10.67759 | -51.10203 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fa5204b6-c6f7-34ef-83e9-5c0812359419 | -10.67238 | -51.09587 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6adfc3a8-23dc-3581-a7fa-b2ec3a3db845 | -10.67139 | -51.10079 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7c12da46-1c1a-3657-b7a3-aa8c85f56745 | -10.66773 | -51.09544 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a90e4ea0-2c15-3827-a17e-5498156168d0 | -10.66678 | -51.10036 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45ef21d6-a99b-3af3-b0ae-a067a2fb4941 | -10.6652 | -51.09955 | 2024-10-10 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8f3f7a19-2f45-3d5b-a4ab-799ba16f8739 | -3.54052 | -50.78911 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 604d120d-4b64-3480-bbf1-18e0a70d274a | -3.53943 | -50.79528 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4df25cd4-acfd-36d1-9e9c-05b8a485098a | -3.5388 | -50.79122 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 366907a8-22e5-3024-b22b-f5efab23437d | -3.49465 | -50.80289 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d940a7da-a5ab-3682-bc97-b4b006a297c8 | -3.39237 | -51.35321 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ae49ff4-b179-317c-902c-d7824417a8bc | -3.38529 | -51.35211 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cc0a97b-a2cf-3107-bd80-4b5acd76c843 | -4.16336 | -51.04635 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5648c8e5-42c4-3d7a-8761-64ec4e02d788 | -4.16229 | -51.05238 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 033ee1ae-6635-30e6-947c-ebdfa52dc186 | -4.14059 | -51.09475 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 745feac6-abb7-3d62-a71b-32302c36cd20 | -4.13949 | -51.10087 | 2024-10-10 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9957ce9b-8360-3938-b1f2-7d7124b0eba0 | -4.09611 | -51.0272 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 79535f7b-9eca-3fd3-b030-f79fdc72b64a | -4.09491 | -51.02959 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e598601-b1b7-330e-a14b-18e948f79aeb | -4.08931 | -51.02575 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 319c7b0f-6f61-3ee2-8313-5a049cf001a4 | -4.08929 | -51.02135 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fd07aaaf-df99-39a6-ae6b-30690237eec7 | -4.08809 | -51.02818 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a10b0d0c-797c-3cb7-b30e-147fa8608f5b | -4.08805 | -51.03267 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 63ed4278-591c-3e46-ad6c-ed7dbae2d377 | -4.08687 | -51.03514 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d040e9b0-efb7-348e-97d6-8a71b32636c0 | -4.08242 | -51.02027 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e58a42f1-e09c-3ea5-ab30-8f012d001804 | -4.0812 | -51.0272 | 2024-10-10 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9446ac89-8638-3858-83ef-de072b006a67 | -2.6533 | -53.3506 | 2024-10-10 03:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 9a0422a1-a134-3b74-97ee-5d3eb1ae3b5e | -2.6716 | -53.3704 | 2024-10-10 03:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 506e86d6-f5ed-3bc7-b641-fd78bd99c712 | -2.6716 | -53.3502 | 2024-10-10 03:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 318.4 |
| e7d68937-fd85-3fd4-a7d0-f8a0affe631c | -2.6717 | -53.3299 | 2024-10-10 03:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4389796f-b86a-312a-853c-c733e96d2f22 | -2.69 | -53.3497 | 2024-10-10 03:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 83627af5-7fe8-3263-b49d-e28e7d6053e4 | -3.9103 | -48.3466 | 2024-10-10 03:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1fabefba-6df6-32c1-9184-390344f92f1a | -4.0961 | -48.2739 | 2024-10-10 03:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| cb05d8aa-3feb-37da-a143-4497eb66406b | -4.0962 | -48.2523 | 2024-10-10 03:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 10011b42-b134-3e52-978d-33774e041871 | -4.1146 | -48.2731 | 2024-10-10 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 421ba5a4-883c-33d7-80c1-ce54b4cb1b31 | -4.1148 | -48.2515 | 2024-10-10 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| eae6dc56-1218-37e6-bc29-d7ba8c9915ab | -6.7654 | -59.3252 | 2024-10-10 03:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 02e28f29-489a-3ab4-ad43-f1c473d5d399 | -6.7655 | -59.3059 | 2024-10-10 03:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ecc47efe-80ef-3393-b3b1-3ab8da26f981 | -6.7839 | -59.3245 | 2024-10-10 03:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 66870b46-694d-3dff-91ad-90a133c32948 | -6.784 | -59.3052 | 2024-10-10 03:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 3e4f4be7-e674-375c-9a75-74d459646bca | -9.0655 | -61.4125 | 2024-10-10 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c21b2f4c-59b8-356a-bfd7-618f29f13ff3 | -9.0656 | -61.3934 | 2024-10-10 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4347f202-6724-3509-adba-77815a561538 | -9.0841 | -61.4117 | 2024-10-10 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 690c6657-a811-3ae9-8ecc-a3a14de59cb2 | -9.0842 | -61.3925 | 2024-10-10 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| bb667939-10f0-369e-85c6-3b70ee924823 | -9.122 | -61.2951 | 2024-10-10 03:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 5af0a455-b473-3924-8f6d-e71b267cf7d9 | -9.1221 | -61.276 | 2024-10-10 03:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 0cb2e04b-8acd-3388-9237-dd83d2d62dc0 | -10.4287 | -60.9979 | 2024-10-10 03:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ff4fea56-5a51-31dd-ad76-7e9176a9b45e | -11.0254 | -57.2237 | 2024-10-10 03:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 5dde88c1-8122-3091-808a-fc557fb7dec8 | -11.0256 | -57.2038 | 2024-10-10 03:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 293a44a0-9647-3682-8ba6-f782e4a53e75 | -11.0443 | -57.2222 | 2024-10-10 03:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| eaab2934-586b-39f7-adc3-ffbc26b8bd74 | -11.0445 | -57.2023 | 2024-10-10 03:56:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| c23ec755-18a5-30e0-9a45-f8de828a379b | -11.281 | -64.9018 | 2024-10-10 03:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 73fa9ab0-4be6-38bc-922e-49b316298378 | -12.2893 | -43.7258 | 2024-10-10 03:56:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 8b128543-b4a1-3978-ace8-d6ec5ef3ef7c | -12.3067 | -59.1641 | 2024-10-10 03:56:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d9a2be85-0243-327a-919a-24e75e06b6ca | -12.9922 | -62.7361 | 2024-10-10 03:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e5145453-efbd-3227-91d5-363323867028 | -12.9736 | -62.6987 | 2024-10-10 03:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 4bc8401b-abce-3af1-be3e-f72c1bb2cc24 | -12.9921 | -62.7554 | 2024-10-10 03:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2b65dfc2-f8e0-3c9f-95fe-694a2cef102a | -13.8379 | -44.522 | 2024-10-10 03:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 47a88fd9-eb13-32db-80ba-22a682394ad8 | -13.8574 | -44.5185 | 2024-10-10 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 7669995f-0cdb-3e06-8e22-823236cb633c | -13.8579 | -44.4949 | 2024-10-10 03:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4ec1a9b4-8124-356d-a20b-ec64be05e63a | -13.7346 | -60.6079 | 2024-10-10 03:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4c1b26f7-4610-3403-a6c2-ccc0360fba7a | -13.83266 | -44.51814 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03bd9bab-58f0-3a16-abf6-a28790d1746e | -13.87378 | -42.42243 | 2024-10-10 03:57:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 34ed89a0-9b93-35c1-b320-e85cffda9a13 | -13.80378 | -44.62831 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00432810-baba-3fc8-b649-710df7375e4f | -13.05089 | -39.96755 | 2024-10-10 03:57:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 72e9b426-90f3-381b-ac4b-8961d19cbf7f | -13.63181 | -40.8747 | 2024-10-10 03:57:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35c8d129-e5c9-324d-8a41-932604972b63 | -14.56664 | -41.74504 | 2024-10-10 03:57:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c5ecd00f-2d19-3bad-90eb-070be33e5f83 | -14.20869 | -42.0181 | 2024-10-10 03:57:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b0d1554-0057-3e99-afb8-2efb2b882209 | -14.20528 | -42.01754 | 2024-10-10 03:57:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README52.md)
