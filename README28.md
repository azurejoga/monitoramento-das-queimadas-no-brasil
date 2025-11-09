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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32feda16-7298-3de9-8ff9-327d4177e4dd | -4.65718 | -46.84908 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72fb2733-be57-32ff-b176-2428adbde4b4 | -3.42978 | -50.24069 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fea4d9ba-2053-35ff-ba3c-7846d7e0dca9 | -2.91641 | -40.00903 | 2025-11-09 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6ce118bb-40a2-37f1-84e9-9019ed4ae9cc | -4.57547 | -48.52522 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4af9020-5b43-3350-a7fb-4343cfcd4151 | -7.70929 | -46.01438 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ece9c202-02c7-315c-bcca-7c98a3f365c4 | -3.33704 | -50.07557 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de57ce21-2623-3879-9186-3bfaf272a101 | -3.07979 | -52.92163 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 54fbb8e0-f3c5-39d6-b0cf-15b4f13c5e41 | -2.6676 | -54.8489 | 2025-11-09 04:38:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32648ce6-f19a-347d-9102-73f5953bbc17 | -3.037 | -50.30178 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 322b35f6-4f56-3496-87b1-20dab8458948 | -3.14646 | -48.73051 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60f0b12b-ba42-3360-8038-f972089a7680 | -3.31944 | -50.10955 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 323a8446-da6b-3ccd-bf61-b9867f6843f5 | -3.42616 | -50.43657 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7904766-2c26-31fb-bdc6-fb4385393277 | -3.12854 | -49.10106 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f38aba-7f47-3a3b-a0de-37b43102c367 | -4.75829 | -49.3907 | 2025-11-09 04:38:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d87ea31d-4739-382f-9e25-eb6ed5bff2d3 | -6.04814 | -58.05599 | 2025-11-09 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 413f063f-8045-3500-b3ce-8167216a75f0 | -3.4461 | -45.65107 | 2025-11-09 04:38:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf649048-9d09-33c0-ae47-8ea14ed73bfe | -2.70866 | -49.54297 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcd78931-6a82-3330-bdb5-befb7cd6afe6 | -3.76899 | -44.29396 | 2025-11-09 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 627ddcb4-d192-3424-be74-f5a4e123dd6c | -3.3056 | -50.22839 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d4842f6-5f5e-3f88-b55b-f01a299dd1ac | -6.71638 | -40.0004 | 2025-11-09 04:38:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fdc3dbf3-6a9e-34a7-8dc7-40899a3d3a23 | -6.85841 | -44.83392 | 2025-11-09 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b98c541f-6de9-3923-a39d-80ef76b7cb4b | -4.79767 | -46.01048 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faf94c10-04ab-3cd7-8161-2ac291563807 | -4.67874 | -45.69081 | 2025-11-09 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b11258-4daa-3fd4-9641-a5ce0e70c9cf | -4.68121 | -45.84585 | 2025-11-09 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5506b0a7-7261-3d21-962c-9583fb35c5f2 | -2.60893 | -49.22811 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b25b20fb-14a5-3d7c-b032-5b52eaf718c7 | -3.24621 | -50.02854 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb9f32ea-7b05-3a3d-b8fb-2cae7b47cde1 | -3.25617 | -50.07397 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdeb2898-c6f8-3818-8f77-a0abad409ef2 | -3.32437 | -53.36478 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e658c6db-a081-33b3-a403-ded7d800a8fa | -3.09297 | -49.2617 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ec9387a-d604-32e8-8f58-0bcfb07e652b | -3.50148 | -50.05067 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f280eaec-50a7-35fa-aebf-abbfccf212f2 | -3.50091 | -50.05423 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b5a2a35-76b3-3b79-a88b-9c5ef68b719e | -2.44653 | -55.41411 | 2025-11-09 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6b97a3-63e6-3b4f-9c59-65af0be8055a | -3.33098 | -53.24818 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d393a1b9-6254-3338-b200-effb19789493 | -3.06032 | -50.22026 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0951415a-0cc0-3c3d-b936-eff97ea933dd | -3.43315 | -50.24123 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffc764c1-f06b-368e-9b6f-1b0893cc2adb | -4.33752 | -46.15542 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48ea1ab8-8f97-3ca7-be18-bcb3ad369742 | -4.7102 | -46.46001 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b6686d0-57d3-39dd-9c17-8c244d79f94d | -3.06753 | -50.28429 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f26b9c5b-4b4f-3875-946d-c51d181207e3 | -3.56831 | -54.00061 | 2025-11-09 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da09fb90-9ae0-3166-9ba3-bcc313119eba | -3.88345 | -49.82832 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b730df63-1b0e-3454-85ef-1a3a82e72110 | -3.32481 | -49.12817 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 191a24d5-444f-3b2f-a529-9abfeb6efc57 | -5.8928 | -43.96149 | 2025-11-09 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcaab36b-ee37-35b3-9825-2fb4cdacf253 | -4.3255 | -45.69854 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49934fb3-e5fa-3e6c-a58c-85c4abfd6d4c | -3.61407 | -50.15589 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f950f5c8-bbcb-3f93-b7ea-5125d0f169f6 | -3.40169 | -50.27676 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0ea07dd-1d16-3d18-a3c2-5c54a3b9c150 | -3.09905 | -49.2662 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95ed6343-4f3d-3826-b0cf-aadfdcaed726 | -4.13761 | -47.65896 | 2025-11-09 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 235dec8c-90f7-3539-9e59-d2d99ff5b9bb | -6.31898 | -46.21032 | 2025-11-09 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddcb6f27-145c-3549-a34a-6da12cfd75ba | -3.77752 | -49.99913 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc309d84-382e-346b-9bc6-af526579d3bf | -5.3081 | -49.52398 | 2025-11-09 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a48b513-07f1-3d9c-bc2b-c73645529b60 | -4.51619 | -45.72473 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 183f18b8-a4d6-3ab2-bf28-0758a4aeaeff | -5.99862 | -44.03296 | 2025-11-09 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb79ecdb-0837-33c6-a2ca-a02faafc1d16 | -3.33361 | -50.09696 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4003ebd-4e43-3250-9721-7c75a815304a | -6.88 | -47.24208 | 2025-11-09 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5159931-04d2-36f2-98c5-d4d33d9a1ee2 | -2.94564 | -49.35569 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fba05633-ff61-35be-82bf-30beba5662f2 | -3.32372 | -49.13506 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f1a491f-e9cf-3815-af41-e1f94a3c0bce | -3.32415 | -44.36747 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e13ec19-c878-35af-8c61-5643b42c82d5 | -2.25829 | -47.87557 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 210fe2f7-c0fe-3fbb-9d3f-46f0b1fcf3e8 | -6.68934 | -46.66654 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b31246f5-5f71-3a37-aefd-a7d2d307c1f4 | -2.29651 | -47.87123 | 2025-11-09 04:38:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bc47111-e953-3c00-b63e-41d2d9bae468 | -3.09573 | -49.26567 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb3ce1a5-ffcd-35ef-a725-dd06270a9703 | -3.26743 | -50.04652 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 928dc238-606c-33a7-b0cd-45df96b61952 | -3.12393 | -50.15562 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bed940f-ed9d-346e-a04a-e615d10f9945 | -2.97694 | -49.20098 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3408099-1a6e-3203-946c-dc537f8c7e97 | -5.3995 | -47.25768 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 432e843f-a75c-32b9-9aa0-826a9b744f03 | -3.65271 | -50.27159 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abb161bb-9d2e-3192-937a-1c17e9ef34d3 | -4.21906 | -50.65702 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 557c3622-667a-3f54-a2ff-9fc6b5e3aa8f | -4.67937 | -46.4032 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b1de86f-5192-36f1-b822-40616cc83c1b | -3.86677 | -49.91201 | 2025-11-09 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ac5602a-0988-3426-8133-bcd4b7025961 | -4.2745 | -46.40011 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7ddea8d-0e29-3738-b09f-5bef86f59321 | -4.39953 | -49.65981 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7dd71c1d-5d4b-3e5f-bf1a-4ca1f3cd51ea | -3.75444 | -45.99292 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0ce8334-733e-3299-bee0-7dab79befe9a | -3.14983 | -50.60751 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc4f25c2-0d16-3b58-9bcc-b5f76f2bdf17 | -2.91735 | -40.0029 | 2025-11-09 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 383ae483-be93-36b7-bc43-d52ed201c725 | -3.14153 | -50.28397 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 337f5adf-6131-34e4-873e-3b24f8489859 | -4.27946 | -45.9704 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 544f76da-2413-36d9-9bef-340e5d2e3b35 | -3.21477 | -50.20331 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6040f6e2-1f2e-3790-b014-81548e5b95b0 | -0.84838 | -52.31518 | 2025-11-09 04:38:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0212b49-c213-3687-a0fa-24e6a981bbc7 | -4.79704 | -46.01455 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96ebfcb9-e8f0-3aae-9b66-f3da240711da | -4.41112 | -49.02831 | 2025-11-09 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 045b1053-659f-3f04-b33e-02f904f8a10b | -7.03623 | -44.2898 | 2025-11-09 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 976be00e-337f-37f8-8dcd-63a2909bcfdb | -4.45392 | -48.73548 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3c8026e5-7153-3bb2-bff5-c9788ab740e0 | -3.26464 | -50.04242 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd1b2f53-f20e-3b5d-9ba6-556db283bcf7 | -8.48335 | -40.52719 | 2025-11-09 04:38:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 421ed418-75b6-3177-86d6-c9de75490bdc | -3.86612 | -49.38002 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 41735e88-3ec2-3ac2-bac9-8cd9c2d3a868 | -4.41388 | -49.03226 | 2025-11-09 04:38:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afd3324c-8890-3157-878d-ea1b092f4a29 | -0.64256 | -52.36885 | 2025-11-09 04:38:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19b7f87e-6314-39be-9713-dd12982d485f | -3.98452 | -48.954 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1375499c-a8c3-3183-ab59-3527aadfe908 | -6.06096 | -44.19717 | 2025-11-09 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9914214a-5a04-35df-9560-0729d0dd8d08 | -7.03676 | -44.2861 | 2025-11-09 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 537552d3-8f48-3804-a1f2-3e59c249fd73 | -3.40172 | -50.45887 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e768c19-ca35-3ef7-9f47-00598dfa7f32 | -3.33368 | -50.07502 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e8d15a4-b1e9-3fa1-a7f0-e8f6acfb6d97 | -3.5009 | -46.30267 | 2025-11-09 04:38:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bf8947c-471c-34a9-ae41-0fb54eb5f15f | -3.42836 | -51.10159 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c8fb8a0-c932-326d-b3f1-11a8a630e459 | -3.60244 | -55.44791 | 2025-11-09 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 244ce2fe-35d7-3e21-9d22-24745b797a45 | -3.33425 | -44.37878 | 2025-11-09 04:38:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| bac4e86d-46a2-31ce-8d85-2b5139cfe677 | -3.24419 | -50.14899 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7a541b0-0297-39aa-b8c3-bccedfcebae7 | -3.15675 | -49.7786 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c334c8bb-cc56-3436-96c2-83a5001a37e4 | -3.67295 | -50.44878 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18b18897-9aae-394e-8405-17bd8476cc5b | -2.60726 | -49.21721 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README29.md)
