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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8ac31ff-93f4-3744-aa43-4ec939c94e11 | -3.77116 | -59.50984 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e4e74c1-d615-3dfd-b882-389953616834 | -3.78753 | -59.38205 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c85f5d51-aa78-32b1-842a-bafd76c77d22 | 0.91083 | -59.62675 | 2026-10-07 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 194e2e4c-363d-3f8f-a41a-f3d6b86ac79d | -3.28629 | -54.01983 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d40d504c-3e71-360b-a03a-ac650a3a8bef | -3.38468 | -58.20546 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 832f1a4e-881e-36ba-81ac-5ffe7875e37a | -3.29182 | -54.01548 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f30d2c1d-0eb5-3ec8-8948-4e4402e6dace | -3.06933 | -54.17218 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cd5ec71e-7cf5-3830-92e6-2867ee01faf5 | -3.2717 | -50.42761 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e1ef3d0-deb3-3d0f-ac62-9c7d00b50ab7 | -2.99097 | -54.04175 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c51ecbf-d676-3b5b-8d99-5282395631e0 | -3.51035 | -54.65251 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22d92590-c082-3890-ba3c-b79e1444e66e | -3.73719 | -51.21889 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8148d335-b822-30ef-887e-9beba02da666 | -1.287 | -54.56239 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 619901ab-ddd5-36f5-a623-702c82b25117 | -3.2902 | -54.0324 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f435886d-fb02-3594-abb1-751749b62428 | -3.04957 | -54.14424 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 977c07fe-a41b-3585-8535-b1b29aded466 | -2.99568 | -54.04249 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9599dcc1-bed6-34e1-b9ff-685988671df4 | -3.26871 | -54.01377 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cbcd66f-938c-3f4f-b8f9-84169eece086 | -3.27555 | -54.06598 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b2101798-48df-3276-a4ef-8f629be5b5c5 | -2.32387 | -57.98398 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af352c7f-8b00-3ff8-99fa-64840e569782 | 1.71277 | -55.61692 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec2d61b7-1b70-3dc2-9e35-d60c93c19bfb | -3.18327 | -50.56738 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 93aa4f57-f3e5-3a5b-b6fc-85d9d638a398 | -2.71271 | -57.47492 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a2502cf-e461-3f49-8db6-3d44eddd6f54 | -2.99023 | -54.0467 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e36665a9-6996-3127-a768-dfbfae8287dc | -3.14457 | -51.62375 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c96714d8-3a46-363e-8f28-d307f4daa63a | -2.83471 | -54.12985 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18a242e9-4e79-38fb-bd99-f34843d8607b | -3.04884 | -54.14913 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d02b94c7-b190-3197-8ed9-cee401d13e1b | -2.70628 | -59.80116 | 2026-10-07 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47bbf71b-0985-3b9f-abbc-19d245c65be1 | -3.27369 | -54.03849 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c7b63fdd-19b6-3411-a823-721cdc01f28d | -3.1839 | -50.56313 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c1c351ef-7b8c-3853-ba70-1fb5fa6627db | -2.80407 | -54.08035 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fc018d3-b109-3ce6-9ed0-eb6abdf46e81 | -2.95517 | -54.11008 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0001dec0-d2c6-31f4-a630-960b9b42aa85 | -3.66472 | -54.28667 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb266025-96e9-3082-8981-50d0e04b3f32 | -3.36486 | -58.18958 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02c8b52c-8a64-3103-be46-b98551905683 | 1.72266 | -55.60827 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15448416-8872-3dbe-921f-8b10dc3a22e0 | 1.03484 | -59.4538 | 2026-10-07 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f86edcaa-8884-391a-9f3a-ff4e78a2cb9d | -1.79532 | -57.10372 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c507e23-377d-38c7-9783-ca24e7ef7306 | -3.02638 | -53.90373 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3dce299b-e016-3d70-b2ea-e9a80a359eb7 | -3.26983 | -54.06341 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0c0ad0a1-0d91-3727-a03e-76604c41259b | -3.04457 | -53.88035 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6184a15d-13d8-37eb-87b6-df2ab958f152 | -3.99206 | -56.2608 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6400bf8d-a94f-3766-9e0a-041710ccd21c | -3.84532 | -55.98901 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a83d555-22b1-3f20-b8ae-fd66078d5f7c | -3.10901 | -54.16304 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb32741b-76b9-32ba-9744-3212f9e3a01d | -3.62931 | -58.93929 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7622596d-2b07-3c0a-ad07-9831ec32f3d2 | -3.10474 | -53.77153 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eaa3f8aa-8df7-3596-be9e-1d0be4188965 | -3.11146 | -53.7646 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8478d2a5-23a8-3bd6-8f80-f4b3b5b83de1 | -2.30717 | -57.08184 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3de936d-cd5c-337e-baf9-9167c91909e5 | -2.9939 | -54.11771 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 126005ff-ff4d-39f5-ac64-36b125636c4f | -3.59015 | -54.30528 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6f6260cd-ee04-36c0-aba6-d5c61a28eb8e | -4.1581 | -55.15009 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db4c6ec2-fbd3-3088-9148-6701637a8aa9 | -3.05739 | -54.22002 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bb19b6a-8b06-368f-ac89-c42f5eb1c1a0 | -4.13067 | -54.90543 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bf8c3b4-c0d3-389c-a690-62a7816efdbb | -3.27701 | -54.05608 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e9288f5-70a3-3fb1-8504-8195ab7f534e | -2.95279 | -54.1362 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b8655b9-479d-37d8-8711-c7035a3c0ff2 | -2.99311 | -51.05212 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a6efb74-fdf6-39dc-bbc1-81ef22be507f | -2.94437 | -54.14838 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c5b785f-b8fb-3fd6-b317-5f994d76bb0d | -3.27524 | -54.03531 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7fd963e1-be4f-3e27-8a30-50b5106bc068 | -4.44266 | -54.97569 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d07f0a20-6c47-3935-9373-dbfee69d5eb4 | -3.2682 | -54.04268 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ac1611c5-3fdb-3829-9a99-ba42aa3c48f0 | -3.50884 | -54.63077 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 856f243a-0d1d-3f30-bc8b-aff04a710cd9 | -3.29594 | -54.05892 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9768a28c-aecc-34f2-b29a-96a733fe2a6d | -3.10878 | -53.77743 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 16b2e701-01f4-3076-9c4a-786c69ebe279 | -3.12524 | -53.70802 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 528932f5-2844-337c-8380-f07bcd402590 | -2.80504 | -52.08687 | 2026-10-07 05:40:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37a138ef-1022-329e-8eec-89cfc37e0233 | -2.75404 | -57.66004 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dc4f90a-0406-3d37-b30f-727d970903f5 | 3.14309 | -60.58119 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dc4df92-f7bd-3dfb-b47b-f0ef0a7eb333 | -3.26977 | -54.03959 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 03ded0e5-ab58-39c7-968b-2b3390bd3771 | -3.80235 | -56.99863 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4cb71a3-d97c-3ebf-bbbe-123667d3032d | -1.09714 | -54.12263 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ace3e959-8a78-3f74-aaac-6a2422e6dc17 | -3.11466 | -53.77565 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c2a13627-b4ff-3d41-9b5b-814c2a1f8baa | -3.2822 | -54.02093 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ef673e4-16b2-35c8-92cd-d2e09ce7a3a6 | -3.23095 | -54.30343 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cd12fe1-2cc8-3d2b-965b-bbed5e95e874 | -3.27376 | -54.04531 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 632946d6-5b2e-3914-9d89-2d284493419c | 1.87109 | -55.73449 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83b7c827-361b-3a76-aad0-4f4d44696c68 | 3.13587 | -60.57875 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12f0af0f-622a-3324-a307-44ddba8e5a34 | 1.72971 | -55.60196 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfec6462-565c-3f7a-89ed-a57d4dc98192 | -2.76043 | -54.08368 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e0b215ee-0fee-374c-9e9e-01d611034493 | -3.01977 | -54.13665 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 753adac2-3ee8-3084-9a27-ba1452da99aa | -3.08168 | -54.24841 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6081cb44-8a06-3893-8fd4-098501d6d288 | -3.21514 | -53.87939 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| beccccf4-65b1-30d8-902d-49ee493b3167 | -3.80299 | -51.98913 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 048d92cc-51ed-3fc7-8cca-52485e4da1b8 | -3.51767 | -58.75541 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e4c936a-35d7-36d1-97a3-a7d54005ed95 | -1.29718 | -54.55518 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49ab96d3-cc2f-3190-9f26-f4debf5fb0e7 | 0.31536 | -60.4402 | 2026-10-07 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcce3be2-77a7-3948-85e6-012a5ccd631b | 1.71642 | -55.61951 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f0264802-cecf-3e0c-b598-42fea25fd046 | -3.41435 | -58.90803 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2115505-adff-3cc2-a41c-4bf4b0847679 | -3.58477 | -54.30934 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae4a931e-b384-3acd-8c1c-29cb9da454d2 | -4.29893 | -50.78356 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d2a2746-4692-3eaa-a9b8-18cee3b0b697 | -3.07776 | -54.24288 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f68237-9f4b-3359-bc42-de96ffd666b9 | -3.2623 | -50.40803 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59b88f62-bbdc-34da-a49c-2b09b5bbd50c | -2.93894 | -54.15256 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 786c110c-b64b-3097-ba18-40132dea7fdd | -2.87333 | -54.20679 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55ad6a0a-3ffb-38ac-aa9a-8ef914c638d7 | -3.47188 | -50.08918 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 499df0a8-24f4-30b0-b528-6d2ddcf3451f | -3.61874 | -55.28032 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| e8077717-4ed9-3db0-918d-ab5de36028d2 | -3.10345 | -53.75275 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9b5573b-18fc-3167-9ffb-7a1d3839f675 | -3.04629 | -53.93271 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4a7cd76-a448-3c80-8be9-42aec2246170 | -2.77548 | -54.11076 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a8b87c7b-75c1-33e8-adbd-8dfcbeee8b8b | -3.17511 | -50.44205 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4e9cf4f-b9c0-3d0d-aa75-8f0c71cc0bb4 | -2.78301 | -51.67856 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 38d2ffce-3100-3d36-9f58-e1f882763ef0 | 1.71017 | -55.63062 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe92dd60-89d7-3ff0-a1b1-f1a9877716a1 | -3.7355 | -59.4513 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 405120d4-6aad-3b7f-8090-0ed3ed347bc1 | -3.28248 | -54.05183 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README108.md)
