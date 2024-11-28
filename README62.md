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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a455a722-f725-360b-9567-b649f1255297 | -1.91753 | -54.44287 | 2024-11-28 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 685abfa3-c45b-36f0-8dbe-30a60367f033 | -3.96159 | -48.08514 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 09be01cb-1632-368a-9487-c1c8131c2594 | -3.08063 | -49.20725 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1b195a7-19a0-3b32-928f-7928525b934c | -3.32993 | -45.50019 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7abcc01f-747b-3378-b89a-86c301f98869 | -2.81115 | -46.83242 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef6af86-012b-3489-ac59-f1cffaf7dc7d | -3.86599 | -52.10984 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45b06167-156e-3e95-bab7-cdb3d16f49cd | -2.97053 | -48.00347 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1c75dcd-5d28-3f8b-905d-a30a6bf0671a | -2.88722 | -51.58769 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8dcd683c-a74a-3024-9fd6-64476b21372a | -2.94582 | -51.59027 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 998e4645-f7e2-3857-ae5e-c427f98761e1 | -4.01865 | -46.32545 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec3cad7e-e9bf-318f-ae4c-08f630bc6c12 | -9.41208 | -49.38011 | 2024-11-28 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fc2eebc-aab4-35ee-a119-6f21a7acc49d | -2.9863 | -51.45269 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fa99f09b-3429-39a6-9c7a-2933b02246c0 | -4.0929 | -48.48282 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e669ad8f-6af0-3f14-902d-8d4ea9c92656 | -3.4654 | -50.54046 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e37285b-a186-3275-ad13-e7016b2f7d57 | -2.94436 | -51.53716 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7838279f-f560-347d-99f0-524bf628cbfc | -4.22231 | -50.88497 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5f168bd-aaa4-32cd-9b90-0cafd55c7560 | -4.46624 | -45.68543 | 2024-11-28 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7620f3a8-7fad-3b6a-9c7c-bbe476e5b89c | -3.27325 | -50.61819 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c401a62-86d8-3f91-9738-0c004d97fccc | -3.82945 | -46.53449 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c41e4e0-31a8-3fb3-98b9-d250533e1bd2 | -3.93928 | -46.7173 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85b90d33-3863-3458-9c0a-1b45c8c72dc6 | -3.85399 | -50.1298 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 102fc0ad-c3d6-3420-b8cc-e6009decf02b | -3.80009 | -46.67717 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 961cf303-9d84-3b62-baf5-bcbea9682d80 | -4.30373 | -48.20859 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 051098d6-2eef-3d2d-8976-287b1ff31e9c | -3.01563 | -45.64071 | 2024-11-28 04:25:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25b7c9bd-ab1d-32a7-89ef-af23970d68e1 | -3.07664 | -48.66397 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba9525ce-a9cf-3951-bca6-a3ace7b13884 | -2.93522 | -48.02194 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c21530ea-e00b-3c04-83e6-7909e6ae7182 | -3.44028 | -50.02921 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e413ae41-05af-3b58-99f7-707e490dde3e | -2.95318 | -51.28834 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8a166bc-33b7-3942-ad87-db80c805da18 | -5.21939 | -44.90748 | 2024-11-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a15c20f6-a3c8-3dbe-9368-9cf355d88001 | -4.20042 | -46.55042 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cd0fdb1-e58d-37d5-ad4f-c8412ebb1200 | -4.02492 | -46.5439 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffee6e3d-a095-3d5b-a804-e8aade471cb2 | -3.94231 | -46.91356 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94fb8752-fecb-3a33-990d-aa2efab3d4b3 | -4.03878 | -46.54253 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 157448a5-6cab-339c-8622-a49ed9f97d26 | -3.94885 | -46.51056 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5631a3d-7b30-3a2d-bd6d-d144f8df0643 | -3.44429 | -50.00455 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 510df2f1-7f10-366e-9897-151944f50556 | -4.04687 | -48.25313 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fe66991-8c33-3feb-b2f7-33de2e10ce26 | -3.37687 | -50.12357 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b91edbdd-bee5-3723-b007-614662c385c0 | -1.7827 | -52.74039 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 95641f1c-2e08-35bb-8fb5-dfb8e911c8e5 | -3.37182 | -46.65734 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdd678ba-adf9-330e-a537-7c299d92752a | -3.72803 | -49.96055 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 962cdad6-d1d9-302e-bcd6-588c20f1200b | -3.08294 | -49.21679 | 2024-11-28 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5f255c0-6e4a-3d66-a2ba-d281ecd985d2 | -2.73257 | -48.89604 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b56792f9-c9d7-3dc1-b098-58a3e7270475 | -3.037 | -51.03905 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2b6acaa-2588-3cf7-818c-b72e78436b60 | -4.64291 | -41.12635 | 2024-11-28 04:25:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3c968760-fa2d-32fc-8a50-3efbf4709b3c | -1.98797 | -53.29698 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dd020b66-223b-37be-9d4c-0c9e57a74490 | -3.93707 | -46.70972 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a2844bf-b1d0-3c0d-8c79-f10da057cff5 | -4.19239 | -50.68691 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6be2b74d-8e11-37e8-9695-01ce6c9fd06d | -4.10488 | -46.94311 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87418d7c-4153-3e64-883e-687615f2be91 | -2.62218 | -54.30387 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60633420-80b4-3fcf-9ca5-b14dab9c3f7b | -5.09074 | -45.84026 | 2024-11-28 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5f625a51-f490-326a-80b5-ef16c2d4be52 | -3.19634 | -46.56519 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01946339-6e40-3fc0-b309-52c17aa11bc3 | -2.2375 | -53.62619 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e31f6ef9-026a-3e9b-8544-3bc78bd5064a | -3.64611 | -51.3934 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c54bb6f7-04b0-3d22-837d-880442eea735 | -14.91251 | -52.86506 | 2024-11-28 04:25:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 22f78b3a-73d2-33fc-801d-860bb39cba24 | -3.43559 | -50.03344 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86d21c3a-7277-3170-ad77-37c809d6b207 | -3.24427 | -50.61723 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b706462-66ed-33d3-8593-2222a4d3862c | -2.91608 | -51.71534 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1b078b4-ba87-3c16-8048-91ff42a3c647 | -4.31153 | -48.18221 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7edec878-1c70-3cd1-b4c5-1e506031e5be | -3.09293 | -53.2542 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2754296-c3ad-3eb7-985b-4d7e368b5dea | -2.83796 | -46.84741 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c8d412c-d6b3-3461-972d-397ef7bb56a1 | -3.52923 | -52.15446 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9f3c95e-d7fd-3a0c-b002-8ebee9d76c53 | -3.24724 | -53.63589 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 34654aaf-e239-3323-8d3e-1eacbbf4706c | -2.69576 | -48.59081 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1016685b-f53c-3daf-9d9e-1907f944f552 | -3.59489 | -50.3617 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 10a72e17-4767-3c43-91f2-4cef5d4f870c | -4.87905 | -43.30076 | 2024-11-28 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2af576cf-a633-3f4e-b9cd-e0df92ef5d5c | -2.69774 | -52.00346 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc727b55-fe44-3a9d-9159-cff37d70bd19 | -4.21241 | -50.8945 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7370c8f1-91ce-35fe-9414-7639cfb2ef47 | -3.6134 | -49.90049 | 2024-11-28 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 507d7cda-e640-3691-a8ec-ec85cecffaef | -3.81229 | -46.59995 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d04cd6e9-b4d3-338a-bd7d-e2311bf24816 | -2.99413 | -51.00648 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dd4ccdd-2df5-3c4a-ae27-33b1ede043af | -4.30311 | -48.21247 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 446aabe6-8a81-3c18-ac90-43a6f6459fc2 | -4.65838 | -44.0445 | 2024-11-28 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a97351b-996f-35d0-ac60-f45d408d13ec | -3.51236 | -51.6553 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a0a000-fd07-3151-bfe8-77d97dd8f544 | -3.05962 | -51.29908 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00f50182-622e-3bba-b1de-5e3a0c8447c8 | -3.77449 | -46.51521 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1234c5f2-79fe-378f-8bd2-c7c12052992a | -3.4678 | -51.59037 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a6bd67f-635b-3838-8e38-fe5c55fe3deb | -3.52932 | -50.19872 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25a4686b-f103-3ae0-87b9-148ff318b181 | -4.0024 | -44.28174 | 2024-11-28 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55bbca5a-8f71-3e05-bb93-e07e1feca693 | -3.59007 | -50.69527 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba4dd4f0-534f-3c68-8eeb-b78be75f51a2 | -3.96508 | -48.08567 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b4a8b293-d4f2-3141-838d-546fefcc0b81 | -3.08712 | -54.13249 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90f4f22c-add5-39ff-bebc-c83ad2ae7594 | -3.23264 | -54.22504 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a5547c2-7650-3da9-8096-33636e37f5e5 | -3.03871 | -50.97687 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b4adaa0-576c-3b0e-81e6-ad1240eb1909 | -3.49225 | -50.45161 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57b49037-0b57-3b8b-b6cf-f2f03b440c92 | -1.80139 | -52.74441 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ee6343d-2e9f-337b-b821-0e72339608d8 | -3.77782 | -46.51573 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbee6fc8-9b0d-3b1c-bd74-35e2f9ec6cf1 | -3.07082 | -50.98979 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 36447a4c-27c6-37fa-a240-2f0c87af6134 | -2.73652 | -51.65496 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ed582f5-1f08-3253-ae8b-302dfc3b349d | -2.80834 | -46.82831 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4d915960-22b2-365d-9f16-b38d92158515 | -4.16539 | -46.6633 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0006c257-ad50-389f-8a38-fd47afa6c5fc | -3.35744 | -50.51159 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 310e8609-c249-3fc9-9ba3-47725d5803a9 | -3.63296 | -54.44202 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 666e69b8-9d84-32b3-854c-aa5283d75beb | -3.48563 | -49.89669 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea8d919d-7d8b-36ce-8e8e-d12e41a8243e | -4.01806 | -46.99148 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb1dd997-3768-33e2-8924-98f4b9d59fec | -3.86038 | -40.71189 | 2024-11-28 04:25:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 763d38b6-92a9-3675-9057-8f0c6c7cdea0 | -2.75266 | -52.10271 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cd62e4e-c20d-3fde-9ba6-f7e47c8ee75b | -3.11691 | -53.10504 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b4cd23e-3dd2-367e-97b7-5d682469a24a | -16.83539 | -46.12845 | 2024-11-28 04:25:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fac1b63-1b7c-3468-8020-6b586e5e25ba | -3.38514 | -51.24152 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 308f6f47-e72c-3d5a-8772-2f386429f483 | -3.77503 | -46.68409 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README63.md)
