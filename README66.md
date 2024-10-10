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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdbb2fbd-7a54-3d51-b82c-e897bf8a4de0 | -4.82641 | -50.79039 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 864243ea-606c-3f1f-b1f9-73655b0bfc5f | -4.82567 | -50.79481 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 83a8e9e3-9609-30cf-bbd6-71e2ad26a3f7 | -4.82109 | -50.82208 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45dd5238-95a8-3020-8b0c-1ab8595994db | -3.95559 | -49.91417 | 2024-10-10 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b544c5b-4fbd-3cb7-8fdf-43ad346ad8d1 | -3.9531 | -49.91228 | 2024-10-10 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f672ac21-13bf-3abb-adf5-788e4222ee63 | -3.95131 | -49.91336 | 2024-10-10 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aac72a67-07f9-3d1b-bb37-9cff61ebc7ef | -3.92988 | -49.66878 | 2024-10-10 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94d2c41e-c723-3294-9a2b-2a18232e09bb | -3.92564 | -49.66815 | 2024-10-10 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0bdde28-221f-3109-8322-d200893fc0ec | -3.88562 | -49.9903 | 2024-10-10 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cbe75b27-f452-3e0c-b763-957c961b6ea2 | -3.71421 | -50.15578 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86350120-0114-3600-a8df-99ee06f236da | -3.7075 | -50.17394 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb318d73-57d1-329c-b706-536b8a01f253 | -3.70698 | -50.17204 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a905359-2e2c-3969-8e99-7cc83942455c | -3.70626 | -50.17632 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d95dcfdc-8e3f-321c-9f91-e06a7a420542 | -3.7031 | -50.17323 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d11c6389-021c-3027-a6ef-bd5bf3e1f554 | -3.70258 | -50.17133 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5335b5b-6d96-33fe-ac02-6ca112002aa5 | -3.70241 | -50.17754 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dba0a826-20e8-39d0-adc6-7153d0d90899 | -3.70186 | -50.17562 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a3f5d53-9352-3606-98b6-701a54a70a28 | -3.70173 | -50.18177 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad619017-0b4d-3830-b364-003301335ff5 | -3.70114 | -50.1799 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16e4059b-31bc-3f5d-a46c-8faf007c7e36 | -3.69432 | -50.17174 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76d5f83d-9561-3bfb-a420-e3ba4d0c5063 | -3.69381 | -50.16984 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9ca3c13-a295-31d9-b13f-37968794f197 | -3.69308 | -50.12351 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f64c9dca-348a-398b-a2ae-14ecceef3e6f | -3.6887 | -50.12279 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 672782de-a812-310e-92f9-b702450f4d95 | -3.68801 | -50.12703 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71360e76-6abe-3112-bbe4-46a832e182ba | -3.6843 | -50.12215 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5a38177f-a009-3971-9519-d4720f47893c | -3.68362 | -50.12638 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 078c4c37-23c3-354d-bf77-9f2efd19ba7d | -5.0574 | -49.95024 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0717a522-3dd5-3f49-9844-0272e67ddea1 | -4.94369 | -49.85611 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9092f6d-5290-36f3-9c77-aecbd5936fdc | -4.94364 | -49.85703 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de48c290-f517-3c9e-9b81-1e06f7dcd812 | -4.94305 | -49.85991 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c716af21-fe6c-3519-943c-4b893c6adf20 | -4.90795 | -49.86334 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c819008-b471-3169-9c8a-86374a8f3f2f | -4.90731 | -49.86724 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 083aafe2-f756-3366-9e01-008cfb14ca97 | -4.90554 | -49.93117 | 2024-10-10 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb7515b3-863b-3971-a24d-d58c4d6ea32f | -4.87353 | -50.53658 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e8c7bc-069e-3344-9a59-6d71caf86e82 | -4.84222 | -50.91855 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1267d93-268b-3261-b090-b3724068d4b1 | -4.83467 | -50.79636 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85bfa7e9-e818-3c1f-9bc8-9501d5ab33e8 | -4.49881 | -50.55235 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d30d43f-9382-3853-92dd-f788816612b7 | -4.44889 | -50.4949 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d849a794-985d-359b-84d2-3d51baac554d | -4.44817 | -50.49922 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 002b69b7-1f31-38f3-bc41-9cfea05e3d9a | -4.43614 | -50.73844 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2927e82-b54d-3e5f-85a6-f5fd1a5d59b2 | -4.39485 | -50.52809 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30448587-c7a6-3ae5-92ec-3a3f38ff6aa9 | -4.39345 | -50.52575 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fb96eb5-13e6-3551-a3dc-3dfca1b12675 | -4.3466 | -50.51554 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dce66f65-b23b-3884-b08b-34e6ca0ee5d6 | -4.26822 | -50.73592 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8467c4ae-73e9-3fcf-9515-c4d874ae0048 | -4.1807 | -50.40742 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a2ae47-095c-37df-8462-e5dc33b4e7f7 | -4.46573 | -49.56099 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10a4945e-b431-302a-ab38-a292aef4e3e0 | -4.38073 | -49.78883 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f9f5a38-db8b-306d-91ce-f7af7c3f961f | -3.56834 | -50.57902 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b73c6c56-4f8e-3958-9478-51fd1971c14f | -3.5614 | -50.37141 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6bf96961-c05c-3956-ab05-338ea3cad9f4 | -3.55895 | -50.3716 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0a013e67-4c6f-3f12-9f31-b692d8e6fc5e | -3.55694 | -50.37064 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3312497c-2cd3-37a0-8b6c-815130d0f8ed | -5.71772 | -50.1368 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c7b5947-bd54-3431-9c00-8d8f8ea19575 | -5.71347 | -50.13611 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 445d9fcf-5597-3d48-8aa0-375b9befef8a | -5.55509 | -49.94658 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b69e21ea-a25b-3412-aa2d-c892b394588f | -5.50941 | -51.01974 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 871e66c5-6111-39ef-b480-5c20ee2f9f5c | -5.34433 | -50.83537 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e946ae15-98b2-3017-a3b2-70548a7aea05 | -5.34357 | -50.83986 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89d4afae-25f1-32ed-a896-49b4907c1400 | -5.34212 | -50.82128 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 20ddf519-f979-3612-9bd9-07885b3d3796 | -5.34138 | -50.82566 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d660772b-b018-37c9-a676-e6eb0c73030d | -5.99312 | -49.67701 | 2024-10-10 04:17:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b033dee-cfff-3934-815f-1b7e4187b6b5 | -5.79026 | -50.11562 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f12be95-6b69-36ac-adca-e672d1e6c15d | -5.55446 | -49.9504 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41a17757-dfb9-3952-903d-f4a4a01ddabb | -5.51042 | -51.01727 | 2024-10-10 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4392d079-44bc-3ba3-9af6-5d4cf4fa70ee | -5.46377 | -49.95193 | 2024-10-10 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 688b2ef6-018e-3b01-ac82-361aef03714f | -5.06675 | -50.75404 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d24c8da-cdbd-3334-98fe-89a5c6be0b53 | -5.06229 | -50.7532 | 2024-10-10 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 039924c5-88c8-3c83-badc-cc15c5081ae2 | 0.45197 | -50.21391 | 2024-10-10 04:17:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce9dbece-01a3-35fa-8430-a809e54c9b4e | 0.44725 | -50.21462 | 2024-10-10 04:17:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0b6bab1-2052-35e1-972a-b79c4c107e9e | -2.22134 | -50.62222 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9466424f-77cb-3ed8-99f1-f0efd3c4776b | -2.10471 | -51.24366 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 260e1eee-8354-3ab4-9779-b8369389bbbb | -2.10386 | -51.24898 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d66928bf-84d4-3542-844e-fa3c1a65c364 | -3.59719 | -51.37626 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6c92725-9b50-3c44-a9f0-d671101ae5d4 | -3.58763 | -51.43659 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cab7eec1-81e4-30f3-a77f-f789f6227590 | -3.58369 | -51.43051 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 656a1da2-a4b8-385c-b677-3d1c42a0f767 | -3.55726 | -51.50145 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d6a25c3-a802-3a1e-a183-cf2cb8aaf920 | -3.54311 | -50.7885 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51d97119-e50b-3a2c-9fa3-c38338f93f25 | -3.54234 | -50.79318 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e049bb2-4753-302d-9d95-4fd23ae96100 | -3.49936 | -50.80165 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1c401b23-7c43-34b1-aae2-3305686d4eb0 | -3.49861 | -50.80033 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfcb8959-079f-39a5-b842-16432cabc031 | -3.49782 | -50.80502 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cad4fd75-58b8-3b5b-adbc-b9bc33bc661e | -3.49475 | -50.80088 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 26b5185c-1bd1-3764-ba88-f7e08801f16d | -3.49401 | -50.79959 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 76c12185-6d51-3681-b20b-c4fed1f3b480 | -3.49322 | -50.80426 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d4ac6087-e1da-3d6b-845b-1ac2c1280d41 | -3.26332 | -51.23972 | 2024-10-10 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1357ca80-bf9c-3e52-b390-bc54430ee1cc | -3.23406 | -50.84719 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f93130d5-631f-3000-9f0a-59db01279b6f | -3.23327 | -50.85203 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a514f1a-39cd-34d5-981f-9deb1b20121e | -3.22944 | -50.84633 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47c4ad96-f39b-33e0-ae76-3a94f8a15611 | -3.22864 | -50.8512 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a5d947f-1c5b-3f03-a021-0ee8103280da | -3.20362 | -50.91656 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56609209-5a40-35b2-87af-3b20f699bcaa | -3.18073 | -51.23489 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04bbb831-511d-3a48-ac1b-d9946966befe | -3.0369 | -51.10048 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9671c3a6-236f-3c65-b052-7ea303b526f1 | -3.03604 | -51.10564 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17f58e35-bd55-3954-9e7d-62a325220d65 | -3.03216 | -51.09972 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c34f0801-8eb0-3960-aa26-90b35d4457f9 | -3.03128 | -51.10499 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40e34cfa-893c-3f5e-a6af-f7890c890990 | -2.97087 | -51.1123 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f5f09f8-f048-3e1d-8f0d-7af287d3fa5c | -2.90098 | -50.70704 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c47eac2-a808-3726-a088-a174639c5b8d | -2.89636 | -50.70629 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e94cf702-ce9b-3588-a865-0334dce0d523 | -2.89558 | -50.71104 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c71139b-dca4-3ffa-b8f8-1c7a8549cf05 | -2.85917 | -51.02026 | 2024-10-10 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 485793c9-5c13-391c-af75-034ce8edca7b | -2.81573 | -51.59957 | 2024-10-10 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README67.md)
