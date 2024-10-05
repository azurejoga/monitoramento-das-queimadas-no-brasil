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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 636e2bfc-a57e-36cf-8dc2-efd64f668024 | -12.6158 | -53.12334 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f6d5c643-fa4b-34df-bc9c-53230f1679d0 | -12.6153 | -53.12742 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c0dc725d-6360-34c9-8a74-e430335dac36 | -12.61295 | -53.10801 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9564fd6-2174-3be2-9f89-aeef349a148a | -12.61249 | -53.11201 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 210db7bd-4ffe-349e-b809-240d821d449b | -12.61202 | -53.11608 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 182ea420-bbb6-3068-a80b-f8a4523af2c1 | -12.61156 | -53.12015 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 65642e3c-6213-327d-ac2f-0591c929b48b | -12.61153 | -53.11042 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1badd9bb-b6b8-3c61-8eca-957990e228dd | -12.61109 | -53.12423 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ed20a39a-1f50-3d1f-b0a9-88f0cb65ab08 | -12.61104 | -53.11445 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9605d145-2a59-33ac-b6eb-edf419267403 | -12.61062 | -53.1283 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 89aeb388-dbca-3f14-a3d6-b92241ee7f56 | -12.61055 | -53.11851 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 385692b9-95ce-3dba-8d01-11fc96096ddb | -12.61006 | -53.12257 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c272b817-fa10-347a-a29d-fdb57033c996 | -12.60956 | -53.12664 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8e1e6bb4-7dee-3830-8f5c-93dacee0513a | -12.60627 | -53.11535 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d950dba-f275-37eb-bd31-391974c8f2cf | -12.60581 | -53.11938 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2eb407ef-a804-3f3d-90eb-caadb7c3930a | -12.60534 | -53.12345 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d7a142cc-76f0-3aac-a4fd-e1a190476a57 | -12.60529 | -53.11375 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfd3cc3c-75ed-332a-9f5f-a299e11f0039 | -12.60487 | -53.12756 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6a91265c-16b9-3d3c-834f-9fe19e407ba5 | -12.6048 | -53.11777 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ccf7b66-0371-3831-a83f-96cbaeee3e6b | -12.60431 | -53.12181 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be6ee871-b6e4-3e5f-9cbd-0799becc2866 | -12.60382 | -53.12589 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e005999d-a12d-31c0-b802-c9bad6ab0100 | -12.60006 | -53.11859 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b18b0a8-f932-39a8-a667-3ff510f9509f | -12.5996 | -53.12263 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a36fa604-aa31-3bd8-afd8-3ffef21e65c5 | -12.59914 | -53.12672 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0370b6b6-43ae-328f-b742-a2a37232a543 | -12.59905 | -53.117 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4446aeca-7101-39de-adab-869bee5f5da9 | -12.59857 | -53.12101 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83a6f20c-a0e7-31a7-aa49-cf4dac58c13c | -12.59808 | -53.12507 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c08bf169-833d-35e2-aa67-197e65005d46 | -12.59283 | -53.12021 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd1f30f5-36d0-347d-89fe-ebe4a8021506 | -12.59185 | -53.12831 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3b78a40-06fd-3565-9915-5184c6b1ae7f | -10.72705 | -54.20715 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00e8f7b4-dfe6-317f-8102-9ea09577e5db | -10.72663 | -54.21039 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb2ee5d9-84c3-392e-bbf4-99ebc0771048 | -10.39428 | -54.80346 | 2024-10-05 05:31:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a20efe19-cb64-3819-8e8b-63d82dc1b1d8 | -10.39391 | -54.80639 | 2024-10-05 05:31:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2bea041-85d0-3bd1-b44a-01670b08db89 | -10.3844 | -53.79776 | 2024-10-05 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ce92588-ff08-3dd6-8f9e-ae86f98a58e4 | -10.3829 | -53.79502 | 2024-10-05 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c1732b8-b672-3ca4-842a-03464fcfcbe6 | -10.38247 | -53.79848 | 2024-10-05 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f493cc7-8153-34b9-89c7-69da561018aa | -11.39222 | -54.35811 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a1bc530-d81e-35d9-9fbd-6a62b96d9af4 | -11.38768 | -54.35887 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b273ae6-4a09-31c7-8b33-a5ff70e0d893 | -11.38728 | -54.36213 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12287c6a-e4f4-3ed9-93c6-c5f4483772ae | -11.387 | -54.35749 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c02d4383-f4ed-3729-b767-b5e864fb43c5 | -11.38658 | -54.36074 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f47e9d29-036d-32b2-b854-b4a3689e1eeb | -11.38615 | -54.36398 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b00a9dba-666f-31b1-81ab-0214612b2d41 | -11.32368 | -55.11953 | 2024-10-05 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83662f50-8f76-3bdf-97ea-635e251ce1a7 | -11.30489 | -54.03935 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8205f0d9-65b0-375f-bfde-03844d0f6b8d | -11.30447 | -54.04266 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7002dda1-6513-390c-b350-17ab4b851499 | -11.30404 | -54.04598 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 234ee39a-c503-31cb-a219-9f1f623c7bc8 | -11.29915 | -54.04192 | 2024-10-05 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d648c73-3f0c-382c-812c-63a74df3193a | -11.10979 | -54.22849 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8309cca0-2e93-37a4-88c2-49032efdcf5c | -11.10939 | -54.23167 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb176cc9-5282-32be-8366-006d5ff5b059 | -11.10899 | -54.23486 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85a46ea7-d120-36d5-ad1a-f769b6fec085 | -11.10859 | -54.23805 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 618e2799-d4a6-3da0-8a41-f97d0220e685 | -11.10495 | -54.22453 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 458ff33b-f159-3096-a466-d5460471cf06 | -11.10455 | -54.22775 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca37554a-b519-3cd6-9141-373df40fb011 | -11.08214 | -54.77488 | 2024-10-05 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aec5ba2-b2ec-337b-87bd-de2535eff259 | -11.08175 | -54.77789 | 2024-10-05 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50b6049d-0304-39f2-b675-3c355546d870 | -11.08136 | -54.7809 | 2024-10-05 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b68c4df4-8b57-33b8-ae29-75877436c890 | -11.08097 | -54.78389 | 2024-10-05 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 740469a2-ca3c-3e7b-8ad4-ab027f9b2e08 | -11.07672 | -54.77711 | 2024-10-05 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d041a6d-1816-3862-a7d6-7e4a8851a07c | -11.07594 | -54.78311 | 2024-10-05 05:31:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fed8e2c-919e-3873-9f65-1fd70d4665d2 | -11.03213 | -53.9919 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31ec07bd-a72a-380b-81f8-22981eb551d0 | -10.97625 | -54.01627 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 974f8e5f-ed84-3d02-847e-9ef2d85ae16b | -10.97584 | -54.0195 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa2da9db-c709-32e7-bab6-03b823c81db2 | -10.97095 | -54.01558 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e60e343-9ac2-3936-8220-9b0428a30bb7 | -10.97053 | -54.01883 | 2024-10-05 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94dc0657-f3ac-3607-ac31-3636239bb177 | -15.40028 | -55.85063 | 2024-10-05 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a214d185-be81-3eb9-b97a-d1d337fb43cd | -15.39967 | -55.85577 | 2024-10-05 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 871948fd-8a1e-3331-bfcf-838b0442fecf | -16.65976 | -55.52091 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| df3895dd-ac9c-3414-bd5f-637b1c802d61 | -16.65937 | -55.5244 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7812c128-bd43-3850-92a1-2619387f5eb7 | -16.65897 | -55.52793 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6e4ad30a-e8ae-3155-886f-b4a935981b7f | -16.65857 | -55.53138 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9b6a5f93-61ac-3a94-ba4b-cd6887c27f21 | -16.65782 | -55.53794 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6258da8b-dd93-37da-9856-9e5b28fbfa3f | -16.65749 | -55.54088 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 132e99d8-d0b7-3a4b-9f53-9b6bb7cfab38 | -16.6561 | -55.50689 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fc2f7726-d180-397f-99fc-5df0f61500b8 | -16.65379 | -55.52727 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| da40491d-66e1-3a70-a46b-a20b621c541d | -16.6534 | -55.53074 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2c1b592a-59f4-3e5d-8422-86319404874b | -16.65303 | -55.53396 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8a20488a-5bfc-3277-b172-42701a2b2d22 | -16.65267 | -55.53714 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c608d450-4a68-3799-8c97-e515da695c21 | -16.65233 | -55.54011 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 599136c6-9b33-302f-b543-0e83a7bdc58b | -16.65092 | -55.5062 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e129f40b-f00d-3ed9-b6d8-fc0335f95cc5 | -16.65056 | -55.50941 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 87958cb3-4b08-3eee-a9e1-45d0ea783962 | -16.64945 | -55.51921 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0c836a0d-37f2-3ef7-9ac6-09aadb05f5ca | -16.64538 | -55.50875 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9bea6ec6-36de-309c-955c-2ca313161cb8 | -16.64501 | -55.51197 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6c738a57-4921-3433-8664-b98e4a1f5956 | -16.64392 | -55.52167 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5111c383-6980-3d27-9679-220373401d48 | -16.64355 | -55.52496 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a6453b2f-43f2-3a56-9b7a-f39088d04684 | -16.63983 | -55.5113 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bdab746a-790d-3136-9790-4ea002f4dd8d | -16.63837 | -55.52427 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d2381fff-2b25-3a6d-a568-d4567c359f32 | -16.638 | -55.52756 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d52604f6-fcb2-3650-8999-e026794c078a | -16.63429 | -55.51384 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f8a757a0-21a6-38b9-985e-42d6194b5ea7 | -16.63393 | -55.51706 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| af38f779-0043-33ec-8c75-4b1b1ec7c0f3 | -16.57897 | -55.91199 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 850a989d-bef5-3e0c-9ee8-d45010ac9baf | -16.14571 | -55.91913 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 06139e25-5e63-37e0-9362-b0dabaa4ff4c | -16.14538 | -55.92203 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9f22d57a-2507-3cb4-b086-137137f51bc8 | -16.13643 | -55.9113 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bd8123de-1572-3b40-b9bd-a847915c0770 | -16.13609 | -55.91428 | 2024-10-05 05:31:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 85c02544-c5f1-34ef-bf3d-0ccf2b39951a | -17.07972 | -56.67717 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3e7f037c-4e33-3645-a1ee-e1c3be199b19 | -17.06015 | -56.06506 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5abeed53-cba4-3e69-a153-4e741dda17d3 | -17.05992 | -56.06704 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9a4d2839-881a-3825-9323-d7d5a571eda5 | -17.05982 | -56.06806 | 2024-10-05 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a2030121-03e5-3398-ad4b-2a799e7e67a9 | -17.05979 | -56.68008 | 2024-10-05 05:31:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README138.md)
