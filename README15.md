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
| b3a0d8bf-cd4a-3298-bd43-cfb93a745b5b | -6.11875 | -42.94987 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| dc3bbbfb-91be-37a1-ae23-6c02eb9dd226 | -6.24967 | -42.64594 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86e74d97-1613-3d27-94a4-227ccab5f0de | -6.26167 | -43.51129 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14f80045-ad8b-3450-9cd9-20da30240419 | -5.90501 | -44.16266 | 2025-09-04 03:34:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dacf53e1-d53b-3415-bde7-a1b33ba40af9 | -5.34463 | -45.09451 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b16501cd-17af-3b66-9137-f0c553d35d89 | -6.22801 | -42.67632 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5a3f3240-cf63-3a79-a517-f4904ee7a663 | -6.22924 | -43.41082 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b924d01-b301-3c54-a739-e1cd2c5ed035 | -6.17699 | -43.31866 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ecd1ec-f2d3-399e-913f-c57af6ffcf07 | -5.68798 | -45.59986 | 2025-09-04 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3233060f-a460-3d97-a2c5-c01386429434 | -6.24559 | -42.6381 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b8bace45-ec32-36e2-8345-eee6e2b45214 | -3.74872 | -40.41483 | 2025-09-04 03:34:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43831681-c803-3e8b-9cdf-78833d9191a6 | -6.22613 | -43.56055 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f103efff-e5c7-3af9-8498-de6a3583a90f | -6.25513 | -43.29551 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 435905b3-f11b-3d80-8de2-9f7af44aeaf6 | -5.3128 | -41.55212 | 2025-09-04 03:34:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5eccc26a-5626-3b0d-a228-aac350be2f82 | -5.69808 | -45.16687 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b15f1f9e-96ee-31be-94ba-37a58a1ed839 | -6.211 | -41.80098 | 2025-09-04 03:34:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5a850949-e857-33cf-9841-b7b6c8b2d4d7 | -6.19527 | -43.34411 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 965fd7d4-f39f-3916-9d43-d41f9ff16e4b | -6.23849 | -42.61649 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 466b2bf1-85f4-3aa9-842d-c7c9402d8f7d | -6.11939 | -42.94631 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d94f1711-b69f-3792-8d64-c00e9dd29078 | -5.69719 | -45.17187 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 16fecc3e-d277-37e2-9904-1564fbe32ba3 | -5.7807 | -46.16591 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00a62e43-592c-301b-bc3a-fe44729267bc | -4.90287 | -41.75843 | 2025-09-04 03:34:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f556fc8-ee98-3462-a3f1-bbf0c07d9885 | -6.22506 | -42.44751 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cdb7a329-d1f2-3e55-9249-0837fc0a1a4c | -6.20014 | -43.3488 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 895035de-9b95-3238-bbc3-88d06741d08f | -5.84304 | -42.99574 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec82252f-9cee-3c8a-8e50-db2b7796abfa | -6.22986 | -43.5594 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c36544f5-8a29-3f1b-ac94-1ca83ffc882b | -4.83822 | -42.74294 | 2025-09-04 03:34:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8807aee-3625-3df7-83f3-9289669f8e1f | -5.97885 | -44.12147 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7c8f319-7224-3c61-bf47-e03e564f96ae | -5.83761 | -42.99467 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eb530ab7-bcfd-3112-92ea-a811a7ece6d7 | -5.6096 | -45.02695 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5415dd90-84b5-3e3a-bc57-b51b46348437 | -6.27274 | -43.32513 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17834583-29aa-30a8-85c8-ee8b15552df8 | -3.48492 | -43.33559 | 2025-09-04 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30db8aad-a0b0-32fd-ab0c-3f9f8fd28d28 | -6.245 | -42.64152 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 61e88f87-f050-3ed8-8344-f4b72a50c5b0 | -5.69179 | -45.94188 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6e6aab6-eac5-39e1-946d-e36ea01d8433 | -4.83882 | -42.73944 | 2025-09-04 03:34:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc50a13a-4d84-380a-8323-8cd5dccd3d5b | -4.77898 | -43.82206 | 2025-09-04 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15688f6b-8635-3b77-b3e0-a27e86da5c84 | -6.1599 | -43.32325 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f997fbc-7073-374d-a857-e426d7b78f52 | -5.83095 | -43.00066 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3839b5e-c89c-3ad1-9d10-5354363efd80 | -6.22339 | -43.37894 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bcc12f2a-3c0b-3a5e-8223-fc892f9d6004 | -6.2226 | -43.54757 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e958c032-19b1-3c80-8068-15f158d2ef92 | -6.21072 | -41.80187 | 2025-09-04 03:34:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 624dbc6c-5327-3150-ab00-9c0c3e31909e | -5.35091 | -45.09557 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0251a62a-3593-34fb-95ee-e3708ca05068 | -6.22678 | -42.43785 | 2025-09-04 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2b94e65a-9503-3c1e-8747-a453a130aab4 | -6.22682 | -43.55653 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f3ca374-f402-3b0a-b03b-8ad92a01b548 | -6.12172 | -42.9532 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6949e46d-a27e-3fa7-969d-dd35e3218b38 | -6.22273 | -43.38269 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 666b73e6-31cf-3f6f-8ac7-64f07857926f | -6.15984 | -43.31885 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 77b7a84c-4dc6-36b3-b73b-b54a472165d8 | -5.69074 | -45.94755 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48fcaf4e-34f5-3156-ad5a-a665c63baaa6 | -6.27255 | -43.32376 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c96118b-353b-3e27-b667-ee6b3fbdc87d | -6.27346 | -39.6928 | 2025-09-04 03:34:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54d002b7-b266-3337-a2b8-4b5f088caff5 | -6.24616 | -42.63482 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b852a9e5-7448-3e13-87bb-bc63927c7bb5 | -6.22326 | -43.54376 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92f49e70-8819-3a9e-9333-fb9aa13dfcd0 | -6.45517 | -42.39797 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1e92210b-3b2a-397d-8cf2-9064e9328a35 | -6.23591 | -43.53746 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af875138-5c93-3e76-ad97-cc52d6467230 | -6.20141 | -43.34167 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eff8f94a-4521-3c00-9152-c66b39b642f4 | -5.78357 | -46.17204 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c57d4707-0443-3682-8688-7a8206847b91 | -6.2914 | -43.60406 | 2025-09-04 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be7e0898-ec30-3f93-98e6-61f21989174d | -5.60251 | -45.03073 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d1edcb2f-6ac2-37d5-995c-74c247a3f9e4 | -5.77967 | -46.17173 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56776f90-c9cb-3dee-895d-f8c8f5eb4755 | -6.22989 | -43.40715 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e5592a4-7a3b-3e1b-a7ef-66e89f6d87fc | -5.74512 | -45.5461 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0705f8c9-f9e3-33fd-9595-0d9ad9caa75c | -6.17635 | -43.32221 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4010df14-89e2-30a0-ace5-16cb87fd2adc | -6.22191 | -43.55154 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2bbd0af-9582-3ddb-83f2-45c384503bec | -6.29208 | -43.60021 | 2025-09-04 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31e5ea66-08af-3bd5-8347-ef19b3f06ff6 | -6.12292 | -42.94618 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 2f373b09-ed19-3cb9-8fb8-24a8249c30a8 | -6.16114 | -43.31609 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ab701dd1-e7c1-33fe-bd78-e45c4cd78de3 | -5.92868 | -43.0262 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f8759b0-c029-3db5-8506-bee844e9fd54 | -6.28425 | -43.51405 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fdd9322-76c5-3f5c-91d2-63887fc14539 | -6.17216 | -43.31827 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ae514c5-55df-392e-bdf9-b11b01541d1a | -5.47876 | -45.23304 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ebba5eb-4915-3166-86d0-975dcb5e1c6c | -5.86072 | -42.55267 | 2025-09-04 03:34:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 68fde135-25b2-3b3e-94f6-3effae3250f5 | -3.13658 | -40.06885 | 2025-09-04 03:34:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3074e901-8eb5-3c84-b0b6-67dc4074b3f0 | -6.22564 | -42.44428 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 74c35262-95f8-3a0d-8d8b-38b071f42766 | -5.79052 | -43.22973 | 2025-09-04 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 525fcf99-91d5-3e1f-8ec7-e598525b7c1a | -5.97214 | -44.12527 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7de81bf-7c5f-3391-a410-bf0f72fee4c3 | -5.90573 | -44.15867 | 2025-09-04 03:34:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f103e37-68e8-3ce7-837e-1f24ca8feba0 | -6.12232 | -42.94968 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7d0712ee-80e6-3599-ad2a-3b11d2b1b15e | -6.27339 | -43.3214 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db25babb-dd46-38f0-8611-7514922f2d0c | -5.49889 | -42.6567 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a2fd30f6-8a39-3fe5-aaad-6b2aecef90f5 | -6.12414 | -42.95087 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d265dbaf-f0d9-3c4e-9fe6-ff7d24449e93 | -4.78402 | -43.82114 | 2025-09-04 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e893af0-87a9-3bf1-aa53-778e096f48aa | -6.29049 | -43.51136 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb4169da-48d7-3e51-9c33-f45288b06b09 | -3.48562 | -43.33156 | 2025-09-04 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea91a63c-a12c-345c-9030-de69dc271b6f | -4.89779 | -41.75747 | 2025-09-04 03:34:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e4d3197-6185-3130-bbd1-aabcef371a2d | -4.83339 | -42.73845 | 2025-09-04 03:34:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9be88975-c297-320a-8120-870c6cade89e | -5.76232 | -44.87424 | 2025-09-04 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7123cfcf-37d7-3b4c-b1d7-626fcac1c117 | -6.22497 | -43.55444 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 067eb3fa-0685-3329-b445-7e12a5cd9f4e | -5.76845 | -44.87539 | 2025-09-04 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eca57625-ee26-344e-91a8-7915e981de2e | -6.45573 | -42.39481 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a985f817-3539-3946-a24f-374ec715d2fd | -4.90187 | -41.76435 | 2025-09-04 03:34:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7eff8c19-ce62-3e6a-8aef-098ba6b9eb8d | -6.29405 | -43.58908 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c9e7ccd-2ab9-3fa3-b1c2-ec324d7268e3 | -4.56475 | -40.35036 | 2025-09-04 03:34:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1373adb8-e954-3a33-bba8-9a539c654886 | -6.12274 | -44.14803 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d27a0f0-9ca5-39b7-91f9-d01c7c0a352f | -4.78327 | -43.82534 | 2025-09-04 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 847507c7-9b59-348d-b5f8-282783dd2e2b | -5.69631 | -45.17678 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 90396041-1c47-3f39-9ab3-d2bbcf03c3d6 | -6.16599 | -43.31638 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0ee3270-aefc-3b06-88ef-a04b9123bf9d | -5.50424 | -42.65769 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c0af4f8-d13b-33f6-9433-94a11e2456f4 | -6.23178 | -43.56133 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 900bbde5-392f-3f3b-8ff5-3a0c1aee7f21 | -6.19589 | -43.3406 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f363a7ed-fc47-362b-9161-9e70105991ff | -5.69256 | -45.9472 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
