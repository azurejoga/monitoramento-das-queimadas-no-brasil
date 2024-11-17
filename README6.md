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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9366cee-982d-39f6-919f-356f08396b6a | -2.509 | -45.456799 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9cb55a5-576f-33fa-9bbe-6ca62438c62f | -4.68 | -49.624298 | 2024-11-17 00:28:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c253d65-886e-314f-b2ea-aa8cbdee8f68 | -2.6609 | -46.209702 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| db0e8c5d-6fcc-367a-859e-6fc432457ebf | -3.5321 | -50.505001 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6113200-e991-34ba-961e-3293f63bb4e9 | -2.8167 | -46.665199 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ecd260-6ac3-3089-91bc-c08b80936f68 | -3.6047 | -44.792999 | 2024-11-17 00:28:00 | METOP-C | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 407b101a-d1ed-383e-b230-128d315d2ebb | -2.8363 | -46.660801 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e797859-55e9-3997-982f-67702c0019ac | -2.572 | -49.075001 | 2024-11-17 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae0f00f7-1823-3f35-b1ef-43d9af8101d7 | -3.9198 | -46.5289 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 832d6ac4-b115-3daf-9f6e-6d791f94f2e6 | -2.648 | -46.198299 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12f8e93b-b546-368d-8227-f7c5a7929583 | -2.9523 | -45.815498 | 2024-11-17 00:28:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fbaf1afe-8022-3c93-8de6-ae30ab206df9 | -3.2327 | -53.515301 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc124638-9173-368f-ab4b-e0704f8bc362 | -3.787 | -46.037498 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e695a95-98a4-3f00-b217-1bbeea5fb0b7 | -6.4874 | -47.4995 | 2024-11-17 00:28:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bbac5cd-7b0e-30eb-8a94-b8a7bb54bd60 | -2.8619 | -46.727798 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7b7c39a-e52e-344f-bbe2-424ccd1d4dff | -2.6743 | -46.178001 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bcfc89c1-4e1d-301f-9d4e-17f90d198ac9 | -4.0408 | -44.760201 | 2024-11-17 00:28:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7b2422a-ec16-381b-b0d1-74272fac5347 | -4.044 | -44.773998 | 2024-11-17 00:28:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89119412-3b23-3127-b84d-c05a9813a632 | -2.6184 | -54.1441 | 2024-11-17 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f06914-b489-3b63-bb21-233496a70328 | -3.3272 | -50.506599 | 2024-11-17 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12ba4704-b3f5-31fa-9003-83a72734b6bd | -3.0909 | -45.970501 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c307f82c-941d-3015-8a96-f9473b77003b | -3.3192 | -52.758801 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8386f7a-9759-3a36-ade4-173664ffb911 | -3.1788 | -53.227798 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa1d7b1-8510-3aa4-9863-3a6172c4ddfc | -2.5916 | -51.796902 | 2024-11-17 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9beb6f63-aa30-326d-a70b-4b5b4dd77e95 | -6.1649 | -41.165501 | 2024-11-17 00:28:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2afef258-64a3-3918-9c93-a8f6e6d0a8fd | -4.4024 | -44.313999 | 2024-11-17 00:28:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ef0c618-529d-3347-a32a-5b49a3cba58c | -3.3813 | -53.265701 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32f5694-3876-3926-ab53-8fabb78ab4e7 | -6.0783 | -41.936199 | 2024-11-17 00:28:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9f03736-c1e1-3bfb-a831-134c35350dce | -2.9858 | -52.5937 | 2024-11-17 00:28:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53bf0393-ad89-3c46-8059-f1cb7969b1e9 | -3.3396 | -53.307701 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b9dbfd-4086-3819-be1b-a2b10df06fc3 | -4.0996 | -44.477699 | 2024-11-17 00:28:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b282369e-199f-327c-b557-27d53976154e | -5.8736 | -40.157398 | 2024-11-17 00:28:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 91c11ff4-571c-310a-a7e4-4761a3f36386 | -1.2029 | -51.780399 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0efaeedd-aa5d-347e-a1a4-a7d726cb0e33 | -3.9182 | -46.521999 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04eefb71-4a5e-3b90-87e2-4058a58e0061 | -3.8193 | -50.2295 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebd04893-816c-3786-8688-36a5bf319e53 | -1.859 | -47.8437 | 2024-11-17 00:28:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96fb49fe-a644-3297-8b45-df5550c96240 | -2.6237 | -46.182201 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a85fac63-6093-37e3-b027-d66c315ab590 | -3.4722 | -44.531101 | 2024-11-17 00:28:00 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc875fd7-277a-317f-9e5a-441338253e25 | -2.2232 | -46.414902 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92505964-0ef9-35cd-88b5-c4d58dbfc3f4 | -3.5782 | -50.5275 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a23c947-f504-3cea-a401-e07b45bb9e5d | -4.5477 | -44.631599 | 2024-11-17 00:28:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afbf0b7b-b931-3dbf-aaae-0b3545915dcb | -10.5374 | -44.667999 | 2024-11-17 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8a3c4abe-6167-31cc-93bc-ff8744bf5951 | -6.9758 | -38.4855 | 2024-11-17 00:28:00 | METOP-C | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| e061fb55-6b7c-32cb-88d1-7cdde368e60e | -9.3928 | -40.323299 | 2024-11-17 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bdd9bd2e-ed0b-385b-b5ef-1f877a0ab313 | -7.8599 | -38.431 | 2024-11-17 00:28:00 | METOP-C | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| a95a9161-bfa4-3420-a014-934389d341a3 | -1.7921 | -48.453602 | 2024-11-17 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44c0ae03-dc8b-32df-aac9-602113ba7f2e | -9.4025 | -40.3209 | 2024-11-17 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 58b86332-2be2-3a7d-826d-2943982e74c4 | -1.4992 | -47.397499 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efdcfbbd-fc88-30f6-b5f6-c698b20af478 | -4.1556 | -43.916199 | 2024-11-17 00:28:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec6aa51-3dd9-380d-a4c6-0513e660c2d2 | -3.19 | -46.538601 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1de604e4-c525-307a-87e6-dfc75e985306 | -4.1573 | -43.923302 | 2024-11-17 00:28:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4a90c5b-eccd-3285-9c8f-88b5f8da804c | -0.3231 | -48.699799 | 2024-11-17 00:28:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d2b045-631a-3c75-886d-8264624c724e | -6.9324 | -42.806301 | 2024-11-17 00:28:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 08bf63d6-ee8b-3c20-9a55-2c4276b500bd | -3.7673 | -46.041901 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90052c61-92c1-3e14-9eb1-ff874d40bd29 | -2.5313 | -47.131199 | 2024-11-17 00:28:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29436866-001f-3478-95d5-f9ef64874801 | -3.8898 | -46.623402 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46cdadba-0df4-3145-bffd-98db7dfd596c | -3.5145 | -50.243801 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a428462-e421-3076-9249-ae63c32cc2b1 | -4.9952 | -44.334 | 2024-11-17 00:28:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f8c7a5f-dc8c-3561-acc5-d808a0b10585 | -3.6066 | -50.151199 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad6ce4f-d46f-36af-b65c-615f8514634c | -5.2633 | -47.1824 | 2024-11-17 00:28:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5baff896-cd3f-3bfd-bada-34bbd80f2e52 | -2.2767 | -47.912701 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ef5d4f-276c-30fb-968a-594919ba2063 | -4.447 | -44.552601 | 2024-11-17 00:28:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea4a6638-c933-3754-9d50-1572b424708b | 0.6168 | -51.7757 | 2024-11-17 00:28:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 82190e07-f00a-396c-9a28-4a923a1eded7 | -4.3911 | -45.5224 | 2024-11-17 00:28:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc08d0a-3f25-3c54-8142-c2bced9559e4 | -4.2515 | -50.188099 | 2024-11-17 00:28:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb970ec-b45d-385c-aa9a-172da59678cf | -4.2316 | -41.937698 | 2024-11-17 00:28:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 39467ba2-2282-3651-a9e6-d5fae3fe7c19 | -5.21 | -43.7897 | 2024-11-17 00:28:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09510d8e-e78a-33ce-8b99-940820943acb | -11.1236 | -44.571899 | 2024-11-17 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2081c9b7-5ef6-3dc3-930e-b5bda0c74649 | -3.6164 | -50.149101 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a64af98-ce69-3f27-b9df-cdc5f33c6369 | -2.6465 | -46.191399 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d736a701-0ac5-3225-8b57-8b76bdb1d644 | -1.9931 | -46.5811 | 2024-11-17 00:28:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a5757d2-6a2a-3059-916c-c325dde92170 | -5.5837 | -44.8745 | 2024-11-17 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d0af082-e994-3b69-8c75-bced957631a5 | -9.4003 | -40.311699 | 2024-11-17 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c4c7fef4-7be4-3d1c-9fd0-8ced6091bb02 | -3.5344 | -50.515301 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4197e3-26ad-3884-b5e5-4b0c44c1f1de | -2.6375 | -46.828701 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294c2c2b-269a-37f4-a52f-b34f57b50858 | -6.856 | -38.883301 | 2024-11-17 00:28:00 | METOP-C | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bf3b6444-3495-34d5-89bf-048ec30af669 | -2.6821 | -46.212101 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 824f7695-c6d8-3c55-b8c1-800be6b2aa82 | -2.1416 | -46.418701 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1808327e-f58a-35db-abfc-a16692f3dcdd | -3.9709 | -46.708199 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09c68dab-a44f-3fc5-999d-bedd6adebac2 | -2.6531 | -46.175598 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b330040-20e4-3c93-a89f-06222dba0137 | -3.6199 | -50.2104 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4a0f25-f1f3-3cf1-9036-86609eb840c6 | -2.158 | -46.4007 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ede6245c-bfa9-3119-9f51-a6870570d17a | -2.5287 | -46.217701 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc97ffb7-77b3-3d94-b4ca-408a7c71fb56 | -0.948 | -52.417099 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 227498d6-1182-3ab3-b6d2-5b618e9335a9 | -3.1435 | -45.479599 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3e5707a-675d-3a3e-8f6c-d6273bbc3978 | -2.1407 | -46.5051 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c723419e-6a21-383c-b186-0e2ea5851a03 | -2.6759 | -46.184799 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f93dc71f-59a3-3a91-a2e0-2b34c3da909d | -5.4215 | -44.303299 | 2024-11-17 00:28:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59845f8d-abde-39e4-9046-af8d10fc2c61 | -4.3674 | -43.005199 | 2024-11-17 00:28:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae7865ce-6f18-3bb8-9815-f785210ab7ee | -4.302 | -48.077801 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 707b392e-58de-3e01-9b61-18a6ec409b06 | -6.4793 | -47.509399 | 2024-11-17 00:28:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e85b879-874e-3099-b0d2-8b0d491995e4 | -5.3121 | -45.445301 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0d024a3-7374-362e-ae70-fd01884ebcdb | -4.293 | -42.199799 | 2024-11-17 00:28:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a50e2f9b-3ad9-3f66-a553-25905bda887c | -2.4617 | -45.6106 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d944c494-34ad-3f13-940c-21950d23d82f | -2.5994 | -47.565201 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffb5f8f8-35a7-3914-a60a-54ee498dd2dc | -4.6427 | -44.999901 | 2024-11-17 00:28:00 | METOP-C | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac24716d-a8f5-39c5-9f5e-a96a6332cd39 | -4.0279 | -45.467602 | 2024-11-17 00:28:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3dcae18-f0d2-3393-9ea7-c86d0c928ace | -2.8603 | -46.720901 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb075223-11b0-3ddb-92d1-562e3a610d7d | -3.7756 | -46.032799 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad3913e9-f870-3baa-b8c7-a9d30a872f0a | -4.4889 | -43.795399 | 2024-11-17 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
