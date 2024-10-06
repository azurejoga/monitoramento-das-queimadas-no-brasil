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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 012ae5ec-d881-31b0-94cd-8e701ebbf16b | -8.22524 | -61.2263 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd2a4e43-91d3-33cf-9256-6f5b46b69e92 | -8.22261 | -61.20531 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a5d1a5c-f063-362c-9bc3-5aeed7a9b164 | -8.22216 | -61.20871 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cadd5418-0d24-3582-81b1-560d7b4ed056 | -8.2217 | -61.21211 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28a5ac5b-8bce-3465-8436-99df8dbc3ffa | -8.22125 | -61.21547 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23292c96-a0d6-3378-9eec-857a7db55937 | -8.21771 | -61.20117 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1b7c734-8f96-3b55-afe3-7e5463430fa4 | -8.21726 | -61.20457 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee1c296f-fe92-364f-b3a4-c978d10faf8a | -8.21681 | -61.20796 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a065078-8141-3ebf-9b13-f63ed3ee3be4 | -8.21635 | -61.21136 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13d76a85-f693-35f7-998d-cdc70aef0ed5 | -8.21236 | -61.20042 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2293342a-f0c0-3656-9e3a-5a90f937c6d4 | -8.21191 | -61.20381 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48dd3cf8-abed-3128-a0db-6966913993e4 | -8.21146 | -61.20721 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57e269fa-2d7b-32b8-97be-3e9c8a364b91 | -8.211 | -61.21062 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9fbaebd-6749-34a6-9d44-d1cf22090ad4 | -8.20611 | -61.20644 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66e29b64-e493-3e68-9934-7d91279e0536 | -9.69779 | -62.17286 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf6e01f3-d746-3bab-a0a0-29c05a715768 | -9.69267 | -62.17221 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3812a2da-2a2e-3047-8cf6-8d22b8d9af09 | -6.44533 | -62.86338 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0f008f2-35c3-34b9-b289-a34e87cd5eb2 | -6.44463 | -62.86816 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a6a6df8-0763-364e-808f-6afdc1cb91e3 | -6.44351 | -62.86581 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90e6fe5f-2387-385b-962e-3b02d3a841a8 | -6.43998 | -62.86746 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9dd995-724c-330b-8083-a6199dc633c5 | -7.52463 | -63.26243 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec2c612d-4169-3ef9-9848-9a3f423a9f3d | -7.50212 | -63.3553 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdb8628f-5910-38c6-b9d3-6f6515d23ccd | -6.98089 | -62.91576 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3efb8f6-f305-3939-a33e-f1de560d82b5 | -6.98017 | -62.92066 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19b7b75c-d293-36a3-95ec-116a1c7989d7 | -6.9791 | -62.91245 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79582d1a-c69a-36f5-b0ab-b79448510262 | -6.97841 | -62.91737 | 2024-10-06 05:59:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b14c30bb-6225-37ea-a925-6486397106a1 | -8.791 | -63.22801 | 2024-10-06 05:59:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7c64252-b54f-3adf-a143-63cce2fc906e | -8.7863 | -63.22733 | 2024-10-06 05:59:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08e1740b-85a3-3f79-a15d-91ad8f064cbe | -8.57966 | -63.09681 | 2024-10-06 05:59:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26385f69-3839-3bf0-ac85-f50fbc378abb | -8.50296 | -64.01994 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e0d3059-8a4a-35f5-9c1f-2becca12d686 | -8.48796 | -64.06223 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22ecb825-d566-3ee2-9e65-6d69f1051762 | -8.33209 | -64.01926 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68eb4591-9a0c-3725-ae1f-4499c7148f6b | -8.31899 | -64.02044 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2c42434d-8f49-38a3-adec-29e3b9a48881 | -8.31836 | -64.02478 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ed6c05eb-d661-3715-a3a3-d097221e4e52 | -8.31824 | -64.02171 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a91446c-62d6-3a86-bc21-aa1c250937e1 | -8.31764 | -64.02605 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dc8c8fd9-47eb-34b6-a271-d5081d11c9ae | -8.31395 | -64.02415 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 850a169c-c08a-3bea-b030-a5fa33dfe3d1 | -8.31382 | -64.02109 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1b98cbe2-02e1-37c7-a94f-a8c57e302653 | -8.31323 | -64.02543 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0655c6f3-847d-3208-bd36-6405ad99a0d6 | -8.26675 | -64.0395 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d2998e3-16bc-3173-8ee7-84b2f463d9a3 | -8.26234 | -64.03884 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df6d7fa9-7d3f-3422-8ed7-f00ef5f51660 | -10.59196 | -64.41232 | 2024-10-06 05:59:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38283dbc-1b1d-378f-9485-3258bd299ca0 | -9.6139 | -64.05017 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1431498-0311-3483-a4d9-c07634c3a7c7 | -9.6133 | -64.05468 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7e4ef7b-828d-3d07-9875-d2f3cdeb944a | -9.61155 | -64.05209 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06d1addd-e85d-3902-a5b7-0219a8ce1d19 | -9.57801 | -64.22459 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87765c4a-1146-3b17-bc3c-1f975bfbb105 | -9.57719 | -64.22245 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c80c53f-22a7-31f0-b0b1-401e54706b4e | -9.57659 | -64.22689 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1e184a3-4d5f-3383-b50a-90cc18d1283a | -9.57419 | -64.21958 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19a0ecc5-8c9c-384c-982d-f01e790e96d4 | -9.57357 | -64.22401 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eddf353a-a02b-37d5-b67f-319838a6b7b1 | -9.57294 | -64.22845 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6925c1af-1f04-3cea-8303-120f9876dfba | -9.56975 | -64.21899 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 513000d0-3995-3e67-ab26-cd488c107f63 | -9.5685 | -64.22787 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fcdac6f-e1cf-3d5c-bb5c-58a6bfe29d38 | -12.02381 | -63.74261 | 2024-10-06 05:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d484726-7655-3abd-bce5-7ffc9888a416 | -12.02379 | -63.7482 | 2024-10-06 05:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df782a7b-403e-39e4-a524-4e46167e13e6 | -12.02311 | -63.74777 | 2024-10-06 05:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59733a05-c02c-3a5c-9c77-3709836ee831 | -12.02242 | -63.75288 | 2024-10-06 05:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8222ebab-ab24-332c-b39a-2d7d9f423555 | -12.01904 | -63.74755 | 2024-10-06 05:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fee75ef0-72ab-3862-8979-6622ab5eb9c9 | -11.98866 | -63.52925 | 2024-10-06 05:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac508283-4c1b-3d2b-9d81-c5e58b55db4a | -10.99671 | -63.90883 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 774f0437-b827-3af6-9e37-42c6950d7797 | -10.99604 | -63.91372 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af9fe76a-3a7e-30fd-a86a-56c87705bc52 | -10.91922 | -63.88871 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26ed8364-df6b-3b63-bd70-c563be9a9231 | -10.91537 | -63.89122 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76a639e6-0edb-3af3-ae88-68e3443dde70 | -10.91395 | -63.893 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ef320f5-6bcb-3ef0-8454-b6680b6daff4 | -10.89864 | -63.91019 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8759ef2-e80d-3266-acf1-501b346cdd1a | -10.89397 | -63.90992 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efb1bbd7-ec50-363d-952c-144d32b57032 | -10.88471 | -63.90876 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6d6a7a74-54d5-354d-9a12-f1cc5fd5741b | -10.88081 | -63.90286 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64816947-994d-3274-9d05-fb8377645ad4 | -10.87691 | -63.89681 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b38025c4-e3f0-3171-9f9a-56c1106218d9 | -10.87625 | -63.90174 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b5c2849-6a64-3cb9-aacd-d5968db005b6 | -10.87417 | -63.91715 | 2024-10-06 05:59:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5ff50af-c70d-30bf-b99b-8850259b07e0 | -10.86501 | -63.91537 | 2024-10-06 05:59:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9e22918-1c22-3432-b188-0bccfce10156 | -7.37479 | -64.67155 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3251ede5-157b-3f44-904b-25dd46399f08 | -7.37116 | -64.66713 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 250d2744-657b-38a2-9bba-db45cf3596a5 | -7.37062 | -64.67096 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1adbee1-e63b-390c-857b-84d50d69c7d4 | -7.37023 | -64.66382 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16589c8a-23df-3c93-b449-94df09010b21 | -7.36966 | -64.66763 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e67665ab-ef79-32c5-8bfa-8ea65a8278b5 | -7.28994 | -64.65994 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45441e9d-3bcd-3e87-9b15-ac325cf12a47 | -6.81967 | -64.32661 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43ba4026-745f-3452-af5b-7118377b5b2e | -7.51147 | -64.67937 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe38786f-4ea2-385c-81c2-5957a8daec0a | -7.37533 | -64.66773 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3dab507-052a-3f8e-a18c-facaf1985c37 | -7.3717 | -64.66331 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bb28d45-689c-3107-9b14-378211a66a17 | -7.35379 | -64.68861 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9efe767e-0061-39ab-bb4f-6ba1237cc333 | -7.29356 | -64.66436 | 2024-10-06 05:59:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faeb56fe-fc38-3255-9e0d-952111daef2d | -6.82024 | -64.32267 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d6d26c6-23ee-3383-b1a7-624964fff5b3 | -6.81601 | -64.32206 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfac77fa-69e0-3d68-b38b-857a08b29190 | -6.81544 | -64.32599 | 2024-10-06 05:59:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f0acbb6-3ca1-30d0-9789-36b17b369f69 | -9.45373 | -64.53899 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93100bb6-2fc3-3b82-b390-8d5310da6520 | -9.36956 | -64.33388 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f44ba9cb-4fce-3ec1-b87c-e308454dde74 | -9.36692 | -64.32035 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0f42587a-ae33-376c-97f0-682b4367b725 | -9.36634 | -64.32465 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cb2868d8-d0f4-3ad7-ab1c-774e9bce775f | -9.36575 | -64.32896 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efb4edc1-35da-3388-a2f5-16bc7b2babc9 | -9.36517 | -64.33327 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 071096f2-efee-34a7-bbe9-bfdf38b7a223 | -9.36458 | -64.33757 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f079f45-4aec-3e8a-8de9-ee2c80099a9c | -9.36275 | -64.3183 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81a7b001-c8a4-3553-a96f-e306d647db34 | -9.36253 | -64.31972 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac1fcb68-58ca-3280-8da2-73d639088cb4 | -9.36214 | -64.32259 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4b654d5-8822-3a83-b895-247a68e6be23 | -9.36194 | -64.32403 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04f947b9-34ea-3d73-9d0f-00af72e333d2 | -9.36152 | -64.32689 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5f6fedd-3038-366f-9b44-e0821c7f511d | -9.36136 | -64.32834 | 2024-10-06 05:59:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README154.md)
