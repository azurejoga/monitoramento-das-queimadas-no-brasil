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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61252a98-6051-3ffc-b5d5-a749622fa1f1 | -5.9422 | -41.304 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 120.3 |
| d68fcfd3-d2c0-33e9-9937-f432b1978048 | -5.6057 | -41.0903 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| e5ac6786-c88c-359d-9887-2613fb0b0346 | -4.5745 | -43.3483 | 2025-11-04 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 410cd1e7-3296-3f12-9032-16ad0f72bcfc | -5.9234 | -41.3056 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 253.2 |
| 65836f0a-18d6-3d0f-84dd-510c4ed50aec | -4.482 | -43.2141 | 2025-11-04 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 20229ccd-5167-34b5-ab3f-b5984d84073e | -3.8387 | -44.563 | 2025-11-04 13:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 3a919d34-d642-3d8a-a62a-1d37398bcb1f | -5.942 | -41.3282 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 169.4 |
| 81adcbf6-cb30-372b-a120-15ac4cc7077a | -7.0685 | -41.6806 | 2025-11-04 13:50:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 91825571-1817-3a7b-9843-ca65ba978331 | -3.411 | -44.4459 | 2025-11-04 13:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d936a85c-9160-3439-ba48-b26dd0659b56 | -5.5302 | -41.1207 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 144.0 |
| 6ca9f0d6-d7e0-315b-b9aa-658c481129b5 | -5.6245 | -41.0887 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| cbf2c13e-b5b1-3403-ad45-3e4ea2f349ce | -1.3562 | -49.0605 | 2025-11-04 13:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| df501b12-d669-377c-82f1-c2b2317acbc0 | -1.1345 | -49.2123 | 2025-11-04 13:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 1e8f4a09-d298-35de-b8c5-0c263324f51c | 1.5099 | -56.0426 | 2025-11-04 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ca0b5db0-ed88-3c45-8c9a-3ced6c6266d6 | -5.5116 | -41.0979 | 2025-11-04 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| 53f5f673-00a4-3914-a4d3-ab09b17183e0 | -3.0203 | -44.3934 | 2025-11-04 13:50:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| e6234679-81ec-3456-b5bf-4e34a274221c | -6.1269 | -41.6494 | 2025-11-04 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| f3083059-9017-386f-8348-5a847e7f480a | -6.1278 | -41.5531 | 2025-11-04 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| fa63e787-76bd-337b-b91b-d557f1667c01 | -5.942 | -41.3282 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.8 |
| 04ed0653-6673-3ccd-8d58-c8612744a6c3 | -3.0203 | -44.3934 | 2025-11-04 14:00:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 69186941-d097-32ef-9a3e-f7b716c64798 | -6.1281 | -41.529 | 2025-11-04 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 98b84256-272b-3399-8272-77c7e340a335 | -5.5116 | -41.0979 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 7ce60917-022f-37e7-88f3-58f33746f392 | -4.4431 | -43.4259 | 2025-11-04 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| cfa8b40b-013c-3abf-b2f1-14d84687aacc | -1.356 | -49.167 | 2025-11-04 14:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d50b8026-a90f-3ade-b9e0-87ec6564fb13 | -5.6245 | -41.0887 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| e766c5fe-6f2e-32ac-b342-6b6221f2c8e6 | -4.482 | -43.2141 | 2025-11-04 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| aec31c66-ef15-39da-b5b7-35c1c8206b9a | -3.411 | -44.4459 | 2025-11-04 14:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 99ba1ac7-5e11-3526-8e9e-d889b9e39079 | -7.0521 | -41.4653 | 2025-11-04 14:00:00 | GOES-19 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| c85c0f3e-39a0-38f6-b09a-43de4e3c37ea | -5.6057 | -41.0903 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 126.8 |
| 1f07cdb2-6040-3030-b056-710572db02bd | -7.0685 | -41.6806 | 2025-11-04 14:00:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 005c0970-9c17-3dc9-b08c-8c937b178560 | -5.6055 | -41.1145 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 64ac7de5-63f6-3f84-866d-d91b7190dcc8 | -5.9422 | -41.304 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 190.3 |
| 67acc949-ca1f-33cc-85b4-b582110054f6 | -5.9234 | -41.3056 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 393.6 |
| f0466312-90e7-3acc-83dd-a6813158cece | -5.5302 | -41.1207 | 2025-11-04 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 3833be76-3093-3986-a60f-98211a592f23 | -4.4633 | -43.2152 | 2025-11-04 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| a59b7b34-766d-37ac-bad7-a0437847799a | -1.1345 | -49.2123 | 2025-11-04 14:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| efe8343b-d2ee-3c7f-9df8-99d820a134c5 | -4.5745 | -43.3483 | 2025-11-04 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 1802910c-e635-3c94-8996-f7eaef35d2c1 | -5.9422 | -41.304 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 414.8 |
| ac08c452-801f-3527-b9b1-87478678fa83 | -3.4111 | -44.4231 | 2025-11-04 14:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d7d1ab11-108d-3f51-9651-41282bb16146 | -5.6055 | -41.1145 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 35006bb6-001f-3dda-bd0c-6ab2f7d23acd | -5.5116 | -41.0979 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| a1266536-7a32-34c6-a924-0595cb81cb69 | -5.5302 | -41.1207 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 176.7 |
| 1559026c-abbe-31a6-ae0f-66288196bbc1 | -5.942 | -41.3282 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 593.1 |
| 84dd880d-7afc-3895-baad-4aa0ae42ef2d | -4.903 | -42.0085 | 2025-11-04 14:10:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 2c3905b3-ecf9-32e5-8e3b-44d430026ab7 | -4.4431 | -43.4259 | 2025-11-04 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 0e982f52-7502-39c7-9372-6b1007688264 | -3.411 | -44.4459 | 2025-11-04 14:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 0463b993-d910-3980-926a-2e069101d122 | -6.1281 | -41.529 | 2025-11-04 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 50296ffd-5cf2-3303-83fd-3154e36f9379 | -1.1345 | -49.2123 | 2025-11-04 14:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| d6771a09-39b7-30e0-b5ff-6bc42c9962ee | -4.5745 | -43.3483 | 2025-11-04 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 8b5b9f9b-5a21-34c2-a002-f217771f78fe | -6.1467 | -41.5514 | 2025-11-04 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 026ccfd7-e47d-3dd7-8076-535c930df8c9 | -5.6057 | -41.0903 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| d189577e-d7e9-370c-bf1f-978b4e7a324a | -5.6245 | -41.0887 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 8840875b-61c4-39cd-81f2-09fd6065d264 | -5.5114 | -41.1222 | 2025-11-04 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 144.1 |
| b4340c1b-9421-3d82-82a7-622efff6feb9 | -2.8324 | -49.4113 | 2025-11-04 14:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f069ab00-0333-3d8b-b98d-5551f304917f | -6.1278 | -41.5531 | 2025-11-04 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| dd8526cd-f9fe-350e-8eb2-a77af37a46c6 | -3.3135 | -53.839 | 2025-11-04 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 69a72d11-0cd9-346b-a517-8580033ed788 | -3.8387 | -44.563 | 2025-11-04 14:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 11188456-96e9-3ce5-94cd-f454f7ab5e56 | -1.116 | -49.2338 | 2025-11-04 14:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e82b2cd8-7624-376f-9957-d2ace7845bfc | -4.5745 | -43.3483 | 2025-11-04 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 920d66a6-56e7-383f-9d70-a367de1e38dc | -6.1278 | -41.5531 | 2025-11-04 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 32a7d5c6-a675-3c31-b0d0-788e6c09cdd4 | -1.1345 | -49.2123 | 2025-11-04 14:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 279a489d-6689-3a78-b5d3-7199bab13e90 | -5.6057 | -41.0903 | 2025-11-04 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 152.1 |
| 5d7aa52d-e2ef-3bfd-83c3-1f378a3b6502 | -5.5304 | -41.0964 | 2025-11-04 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 7f7b64cc-2777-3fe0-8d1d-6062b751fbf6 | -5.6055 | -41.1145 | 2025-11-04 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 178.0 |
| 4202d6bc-7f34-30e9-a8f1-276aa3e81349 | -3.3135 | -53.839 | 2025-11-04 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 34b6493d-93db-366e-b74a-66ca12f2bfb2 | -6.1269 | -41.6494 | 2025-11-04 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 3782c1ca-0cd2-3834-8e25-f738d3d5bba8 | -10.6453 | -44.6718 | 2025-11-04 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 730ef1d1-02cf-39d5-929f-0710e9416e17 | -4.4633 | -43.2152 | 2025-11-04 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 52088472-047b-35d6-8740-4fbcf5db46ae | -2.1597 | -45.9095 | 2025-11-04 14:20:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f2e14aed-84ad-3c3b-af8f-c988ba9a51fa | -3.0203 | -44.3934 | 2025-11-04 14:20:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 68c7e2e1-4b5d-3361-b12a-7f1cdd76eba7 | -2.8324 | -49.4113 | 2025-11-04 14:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 334f774a-d09f-3ff9-b02a-ee315e0462d2 | -5.5302 | -41.1207 | 2025-11-04 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 180.7 |
| 623833c7-b275-34d5-9ec3-f9e8d4efbda3 | -1.116 | -49.2338 | 2025-11-04 14:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 766fec74-fd34-3dcd-849d-0c6ec7b9f4ec | -6.1281 | -41.529 | 2025-11-04 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 21f6b93f-6b6c-3902-a152-7f52a53533e7 | -4.482 | -43.2141 | 2025-11-04 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 70ca6e3f-977b-32c2-8691-d80e6824b2d4 | -5.6245 | -41.0887 | 2025-11-04 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| cff91089-7afa-3f28-9cd1-8efe0ce2a949 | -6.3452 | -42.3705 | 2025-11-04 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 8c8a5d71-5678-3582-9223-4e0cfc68393f | -4.2847 | -44.7677 | 2025-11-04 14:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 62fd7236-b2ab-37b5-8be8-3f21d40bbf65 | -4.0989 | -44.6866 | 2025-11-04 14:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 358420af-d37c-3a67-a343-4eadd0229bd0 | -2.4934 | -45.967 | 2025-11-04 14:30:00 | GOES-19 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9b6056f6-56f5-364e-967b-59c8ba8fdaf0 | -5.6245 | -41.0887 | 2025-11-04 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 140.1 |
| b2506428-0c4c-31a9-8102-f3d5aa3715ad | -6.1281 | -41.529 | 2025-11-04 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 428ad11a-26e4-3621-9dc1-2ea1352945f8 | -5.9234 | -41.3056 | 2025-11-04 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 589.9 |
| a1b55e68-d6d9-3d84-b7e7-5476d1b19be1 | -4.4633 | -43.2152 | 2025-11-04 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 56f869b5-c02b-369e-8c05-d22e19e4cc36 | -3.8387 | -44.563 | 2025-11-04 14:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 693275b2-3dfd-390c-8d0e-539f8000abbe | -6.1269 | -41.6494 | 2025-11-04 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 7193fa1f-87e5-3238-a217-580fa408693a | -4.0987 | -44.7094 | 2025-11-04 14:30:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9f2bc3fa-2064-374f-91b1-afadc912d16d | -2.8324 | -49.4113 | 2025-11-04 14:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 8eba415f-63e5-303e-aab4-20b00610f14a | -2.1597 | -45.9095 | 2025-11-04 14:30:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 72feb34b-34ac-3fe8-863b-0049efca439e | -3.411 | -44.4459 | 2025-11-04 14:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 47dfd870-74a0-3d9a-aa65-aff73ee3e09d | -3.3135 | -53.839 | 2025-11-04 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 33e19df6-1228-3dc5-9f5a-f92b6bdef527 | -4.9552 | -44.9106 | 2025-11-04 14:30:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7e9fdc69-0a63-3f1f-bcf5-dea4f4e42292 | -3.3134 | -53.8592 | 2025-11-04 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| a2515836-d13c-3491-8132-ce8a4918d838 | -4.0196 | -45.4595 | 2025-11-04 14:30:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| beba76f4-26f8-3e2a-8797-bf7afa078c66 | -2.8324 | -49.4113 | 2025-11-04 14:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 57d9bb3a-ea70-316e-b896-2c5f79102717 | -3.411 | -44.4459 | 2025-11-04 14:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c6d5316a-56bc-3f3f-bac9-7cfaed3fff29 | -2.1597 | -45.9095 | 2025-11-04 14:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b5ece57d-910f-335b-a412-1ebad5e5816b | -6.1269 | -41.6494 | 2025-11-04 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| f77ebd5c-b036-3084-ab81-d55e1284303b | -3.4445 | -41.737 | 2025-11-04 14:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 4eb0df14-66c3-3b1f-b63c-0ab9be359216 | -4.9738 | -44.9095 | 2025-11-04 14:40:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |


[Clique aqui para ver as próximas entradas](README30.md)
