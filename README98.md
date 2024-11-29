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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d951aece-9cba-3d1c-8f17-5ccd5a8870df | -2.90231 | -51.5765 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ca9bbfe-db73-3777-948f-903de830194f | -3.61614 | -50.18848 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8199d1a-7936-3654-b2f6-499623fdbbf9 | -1.42506 | -55.25789 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5af3b2f-92e3-3d2b-9419-e068e29bdd02 | -2.96513 | -53.88974 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cd16658-b53d-3106-ab2f-6bb79d96dace | -4.19299 | -50.68806 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e43a0e7a-e325-3f03-8d9e-27208dc87c60 | -2.96475 | -53.7211 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5f839232-c2f3-3a73-8206-fcace05d5869 | -2.98881 | -53.35604 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 885a5a47-4efd-3550-8d2d-35a330acc704 | -2.85756 | -54.02599 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7239129-e5da-32ee-bdd8-c641b1f324f4 | -3.05736 | -54.04217 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 881c79bf-2864-3a8e-8bbb-70ebbcab1c2e | -2.82692 | -54.11193 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2e53d9c-c701-3ad6-b33f-253e85427d54 | -1.89315 | -54.53944 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48463178-56bc-3f86-bc6e-0b16a0b51b20 | -2.20184 | -53.75142 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 230eb6be-6b23-3160-9cf9-92d68e30c009 | -2.60922 | -54.20783 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68bce521-5fc5-380e-a363-00a8f745811d | -3.37043 | -50.17789 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 314ce7b5-bfac-376f-bbc6-6b777b275d51 | -2.62828 | -54.06271 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 732632eb-0517-31cb-8d8c-037f697978bd | -2.29285 | -51.9844 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 754f6d3f-7f7c-31aa-978d-129a827c49ba | -3.35124 | -51.64299 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 323d7b34-9f54-3c81-b603-641d42faf381 | -1.65226 | -52.73856 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67bf462f-a5e1-32f8-9394-ecba6e3244da | -3.71574 | -51.80049 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74ab8bc4-bb24-30a4-8f47-faa10c2fd85f | -4.17736 | -48.62669 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b17240cb-0bef-3df4-af11-ca569245fc03 | -12.43968 | -63.69179 | 2024-11-29 05:22:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d48f83f8-292b-3f36-897c-3db0168b08ed | -2.50409 | -54.16547 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7dc026ac-2432-3f6f-9a6f-1cf3cf43f305 | -3.07653 | -53.91238 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fda17de-06e8-363b-bb5d-012db0574991 | -3.47568 | -50.53402 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e93ead76-7ee5-3c4b-a649-7ad399f74c1b | -2.86948 | -54.00402 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ca3d278-3c5c-30b3-9ce1-a98ec401911a | -3.28542 | -48.76247 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8f5ff1e-d5d2-391f-8493-70a183e4f56e | -2.37138 | -53.82317 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c38b5c9-bfc2-3f5b-973c-f4bc5f2b0102 | -3.9177 | -53.67161 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4691364c-36cc-36a2-a534-28e0bc02eeac | -1.35364 | -55.6422 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50976b47-6f7d-3edd-a1ea-6b91741c434e | -3.96823 | -50.18929 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fad9678c-2e40-3af1-a28b-8730e602ff6e | -3.90493 | -51.04182 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 713849db-2549-37a1-9583-2056c709c553 | -3.07327 | -53.91314 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60928640-89f0-3444-aedc-355dfbc58818 | -1.62065 | -53.3316 | 2024-11-29 05:22:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db41f7eb-99ee-3a21-bbc7-ff57f358c6df | -3.37596 | -50.17882 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e8e23d1-e95c-3680-8446-c3f4462ac6d9 | -2.01237 | -51.18845 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce61cd7b-7cfc-3b7e-a296-93f13108a893 | -1.66725 | -53.78286 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58f2a137-8074-31af-8225-b935c816d440 | -2.87676 | -46.86979 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70113a83-488b-3169-bf33-8c635357aab8 | -2.017 | -51.19216 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59613fe8-760a-3371-8ee7-849f558131af | -1.69074 | -52.46161 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39eb3c7e-b3eb-3ce8-9d2a-d09e9cedfd6a | -4.04541 | -48.33365 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee580367-25f1-3e0c-af69-ffdf9c93309c | -2.26119 | -53.67919 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a29f605-a81c-3a6c-9bdf-7cb5922b57ab | -3.49626 | -53.81998 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c8865bb-30a6-3a01-80f4-a4996f1ef378 | -3.24458 | -50.77018 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f8795ca-cdb4-3a7e-9bfe-da6c909c6d12 | -3.52907 | -52.15739 | 2024-11-29 05:22:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89bac28c-57f1-36d4-aa61-78defde1670d | -3.34829 | -50.51447 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e2dbf34-4de8-3ab9-9086-c228eb07c2d7 | -4.07167 | -50.03136 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45a6cc30-6122-3dea-a87f-c56c36a2b152 | -3.17456 | -53.63996 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9853fa9d-12f9-332f-9da9-bac68d449b94 | -1.60687 | -55.4274 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36cf1b8f-df20-3b88-9e98-5f8390a8dfca | -1.71056 | -52.63045 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 965d209c-480c-34d3-8b79-989c053513b5 | -1.63244 | -53.86863 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 481616ac-a1d8-3f5f-ba95-bfeba22748e1 | -3.15971 | -53.23648 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d82d251-6e61-31d2-b6e1-d1a2328e9806 | -3.27866 | -50.04181 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb1a151d-833b-3f3f-bd70-81089f0f8a77 | -3.10373 | -53.81733 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44cbb4ce-7707-3043-bd3a-9e90bfb4579e | -3.46975 | -50.5367 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4178fbf-f47b-3a16-b83f-27aa800818b0 | -1.74878 | -52.65519 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f61e70e0-9f36-3562-adf5-989cf805ecfc | -2.60506 | -54.20723 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec801e52-6d04-3444-96cd-c527813bbea0 | -3.49501 | -53.79919 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0274eacc-b4a3-3245-be12-82d337029fcf | -3.26016 | -49.89364 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efd007e3-0df8-384e-9ea6-09dfbdf56e34 | -3.26317 | -49.89135 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83326124-d9f6-3114-ae92-ee2d928f7ac5 | -3.07885 | -50.25445 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eaa8e95-c42e-3613-ae26-1032822f7ecd | -1.68612 | -52.46091 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d906f70-f5ff-384b-a98e-db0cc338e718 | -1.69061 | -52.43244 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b033602-d5c3-3888-bb30-f2c40fdb6263 | -3.10062 | -53.80867 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08c39588-9208-39f2-b546-97c36a27b0c2 | -3.49564 | -53.79505 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 283314db-3771-3906-8279-2c541a3d5251 | -1.70086 | -52.4467 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 936d5426-0bf3-3069-8fdd-aae5baa1f76d | -3.02959 | -54.02715 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e7c9406-816e-3170-8fac-6625fcfbb7a1 | -2.9597 | -51.00293 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f677032-aed0-3083-848e-2f32dda3c95f | -2.73416 | -48.8916 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ea17d62-1c98-387e-896a-474c4be9b39c | -2.77363 | -53.98135 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 045e2dfc-f532-38e4-a356-437a7906f55d | -3.9623 | -48.08622 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 84f85dd9-26e9-3932-b9fd-a1737190ca5e | -1.44495 | -55.15552 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bb450ca-5c23-3396-a613-cccd4bf0d369 | -2.88957 | -55.22372 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d6a550f-76b1-3ab9-8383-50d52fdce98b | -1.58449 | -53.84564 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4e24038a-62f3-3961-b4ee-a443ae80d217 | -7.98678 | -55.30344 | 2024-11-29 05:22:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07c7b5b3-e463-3c77-b885-a43508adc69e | -4.07416 | -50.03413 | 2024-11-29 05:22:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b308bd87-c776-335c-bb14-4d98a7d8e39e | -2.85413 | -46.82286 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0bbeab3c-7422-391e-8d6a-8e31e4da876d | -3.22551 | -54.06953 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16ede12f-04f1-3d84-a4ed-f7e6b44a5e6d | -1.43107 | -55.24443 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ea9db1-7c11-3030-a946-2f5497e1aa25 | -3.53368 | -54.08275 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b1f9804-0da3-3aae-86c4-be0cc5a7d8b5 | -12.40452 | -63.71292 | 2024-11-29 05:22:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc3f8b90-0fbb-366c-a937-5ec55259cd59 | -3.07996 | -54.56613 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bbb88add-fab7-3ec3-b07c-b97709653f67 | -3.02712 | -52.38194 | 2024-11-29 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40404051-d8f3-3de3-bbf4-e217b7b8af62 | -1.65884 | -52.72565 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| debbf612-0da4-3f85-9b6d-60cb75494dda | -1.43563 | -55.24032 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64eb67d6-e5c3-33cd-bc00-ae7b3a16fa10 | -4.10026 | -53.97767 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f835ba61-95c7-3cb8-81bc-57a2f2814d4b | -3.30073 | -50.75836 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d950f6c-876a-3188-b455-5ae076252086 | -2.38703 | -56.09115 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 159c5b2c-11e7-39c3-b2d5-8369fc9acb95 | -1.64253 | -52.74169 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b03bc394-b0c4-3e0d-8885-39dac4fdb80c | -3.0969 | -53.8175 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afee6ff1-0eea-3bd7-9617-126b7c3eaaf9 | -2.69322 | -51.97945 | 2024-11-29 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df7d85c0-2f5f-3e34-a603-15c76dad5b43 | -2.66778 | -48.79251 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 6f6a4846-4f3f-31ca-9397-db7dda4c0ebe | -2.58317 | -54.23864 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f56790d8-74fc-3762-a1b3-a9c605dcb534 | -2.12868 | -54.89827 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f68ce49a-cef6-398c-8fa0-ca79c5b45d27 | -3.41753 | -50.16635 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e00d4f02-bbea-3da8-8ecd-508b085aaa38 | -1.5993 | -55.42617 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d5f7f3a-a99d-3498-b960-470286f063fa | -4.40917 | -55.11317 | 2024-11-29 05:22:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce0b3355-4fd6-353b-9409-a236fea8e072 | -3.07014 | -54.41187 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a911228b-4b85-3a8b-8318-8064e930b965 | -2.20244 | -53.74751 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e02ccb7-c7a9-364c-8dc3-6b126ffde128 | -2.82929 | -54.09669 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f98b562-bfde-3e99-b59c-9b9c949d8a50 | -3.1304 | -51.04181 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README99.md)
