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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fb56f90-4ed8-3f9d-8f8b-df3ffaed2321 | -8.87744 | -62.41826 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c841e17-0bd8-3a48-85e2-2f4118661879 | -8.871 | -62.39939 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f0626b89-45b2-3b61-b39e-5bdaee8a6a38 | -8.8653 | -62.40757 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0afe32f0-ebd7-3ac2-9cf1-1e7d22f085ff | -9.8682 | -58.67255 | 2025-08-21 05:57:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f63c01df-1422-3c68-a62b-0737d06da28d | -8.86592 | -62.40319 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d0fc464c-9231-3d59-9c5e-dda3711d5589 | -7.78919 | -66.96078 | 2025-08-21 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e757233b-e031-3e5d-87b5-41d6ab2ad2d1 | -8.3582 | -70.28347 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f86a844a-481b-3445-a4df-80b9db2886ec | -9.16236 | -59.60329 | 2025-08-21 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48e91953-d8ee-337b-b28d-dffda302e712 | -8.86776 | -62.39002 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| dfebaf44-6c34-376c-8696-b708b2f2c213 | -8.5686 | -70.04216 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f0d500-14d5-3703-8e47-91d0654e50ea | -8.29311 | -70.10198 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20ab8887-0ffa-3491-9496-3e982facdcb6 | -8.86715 | -62.39441 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 90238248-e4ab-3f5d-8f90-a2b12caddf63 | -8.57197 | -70.04272 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fec68c18-66e3-35a8-95b6-c7cc85b54220 | -8.86407 | -62.41637 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0eeb378d-7467-3442-bf13-bb3ec49268c3 | -8.025 | -71.40556 | 2025-08-21 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87fcfc9d-1d16-3a54-a4c3-325fb749f0c0 | -8.92315 | -63.63379 | 2025-08-21 05:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e65f95e4-3564-360c-97e0-d13af289335e | -7.00145 | -71.76839 | 2025-08-21 05:57:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40416389-4881-38ce-bd8a-678e978d978f | -8.55435 | -66.95422 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b079646-652e-3484-9bf2-03b0c98d20eb | -8.87806 | -62.41386 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1895937d-06c1-3b16-b0e8-deafc62b795b | -8.6151 | -62.13128 | 2025-08-21 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1716ee8f-7ba3-3f5e-9103-53082279c19a | -10.40596 | -59.37891 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1623d233-57b7-34c8-8447-0f9fcceaac34 | -10.41044 | -59.37461 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 231a99bd-145b-3647-9d69-2a9b40b59de0 | -9.20941 | -59.45967 | 2025-08-21 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d0c8028-49b2-3c4d-a62d-463e161e93db | -8.55492 | -66.9505 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 129da951-f2f9-3707-a462-4455e90ae524 | -8.56523 | -70.04162 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6d6fcea-cf4e-30ef-9a4a-db4545fefd24 | -8.87298 | -62.41764 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0b8b49af-8422-3dc6-b60d-c360b4508531 | -8.5555 | -66.94677 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cc79081-caac-398c-a943-30c7df73ff03 | -8.87422 | -62.40882 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c9ffcc7-1373-302a-98a1-41e7e7f63828 | -8.55264 | -66.94251 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 357353b8-a89a-340b-8bb0-9cea6fe9a475 | -7.45426 | -70.01933 | 2025-08-21 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f28185c7-9663-32ca-8aca-19dbf63eec67 | -8.62029 | -62.12729 | 2025-08-21 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2586c1ef-d1a1-3eec-9ac8-c0491ff1517f | -9.05187 | -67.46281 | 2025-08-21 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e82e0b3-3ab5-3ea0-830b-ffb10e0353f4 | -8.5657 | -70.06013 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4ab4d25-9b64-30ba-a0f6-7b72935e4d7b | -8.87161 | -62.39502 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fc8c2f6-eb1b-3726-bc6e-b25d0e0cc7fb | -7.78578 | -66.96026 | 2025-08-21 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 839da6dd-ba9f-3491-81fa-8dd817292072 | -8.35481 | -70.28292 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 104cb83e-5e55-3777-9f2e-46b16d3d0f8b | -7.77953 | -66.95552 | 2025-08-21 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebca787c-7bcd-33fb-8b3f-7830c32d8f61 | -11.81065 | -55.52032 | 2025-08-21 05:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 87c0072e-2e5e-3d34-964e-4593b9b999ff | -8.83998 | -69.10881 | 2025-08-21 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60dc8df-3690-329e-9c9b-7d15e7f20235 | -8.51827 | -70.8458 | 2025-08-21 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3d1146-1a0b-3626-927f-56489080ba05 | -8.89691 | -68.89967 | 2025-08-21 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b587e78-cbcf-31b0-9983-e7e5a4b992d0 | -10.40646 | -59.37514 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff0f6ea-bf55-37bb-ad43-edb68308a686 | -9.19389 | -65.66475 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8901be5-1d72-3d55-95f3-40626a60be07 | -8.43896 | -63.8639 | 2025-08-21 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90a6282f-53b7-37cb-a9e9-37cd72a7f9bc | -8.83943 | -69.1123 | 2025-08-21 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2482293-53a4-3545-a10e-23c2eaf24d7c | -8.8876 | -62.41072 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36ccc8cc-f38f-30fc-b55e-93c75b4ad109 | -8.86791 | -62.42143 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 93466b63-7585-316c-9068-1be681bd3daa | -8.8736 | -62.41323 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dbb175f9-8ef5-35c3-87ee-b0d7232911cf | -8.86207 | -62.3982 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 49528941-8019-3a50-95fe-9329711b57c3 | -9.20973 | -59.45668 | 2025-08-21 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb59022e-dfe2-38c2-b2e8-89121b82fd07 | -9.39116 | -70.46446 | 2025-08-21 05:57:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2296cd7-9587-3150-ad1b-c252e20b4d93 | -8.8633 | -62.38939 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| b5fab67d-0304-318d-8bad-8f4509471c1d | -8.46678 | -70.08879 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2438831-43da-3f5e-aa63-58196ed99d2b | -11.80913 | -55.52193 | 2025-08-21 05:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 845f9e44-4475-3da6-961e-7465b13af833 | -8.88821 | -62.40639 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 67f379b3-eb51-306a-9f54-c6cf7cf3b5db | -8.55149 | -66.94997 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 751e7315-baf8-3336-87c9-31119fb03880 | -8.241 | -67.35777 | 2025-08-21 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50a86fa1-deec-3289-a661-e971a7c36861 | -8.79346 | -67.00493 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f00a713d-44ff-3d91-bc52-28611633a215 | -8.87485 | -62.40441 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2e95f6b3-e560-35fa-b04b-36188e559278 | -8.86653 | -62.3988 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e515e4fc-4fe7-3d37-b11c-2ece8201fd45 | -8.67614 | -62.09497 | 2025-08-21 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd148774-9b8d-34ce-ac15-c1e2945a3151 | -9.91285 | -62.14737 | 2025-08-21 05:57:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c979b26c-db5f-3542-b59b-ab7486f7f265 | -8.28973 | -70.10142 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f2c13cf-51ab-3113-bbaf-f466d34b1449 | -9.51697 | -70.42188 | 2025-08-21 05:57:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5290381-0949-3fae-bc74-7d4982e25a76 | -10.40998 | -59.37836 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c735e141-027e-3735-b808-8ffb92d15e8d | -8.02854 | -71.40617 | 2025-08-21 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21a37714-e16e-30e5-8ccf-dde44ceda536 | -9.20928 | -59.46029 | 2025-08-21 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8593ee2-292a-36fc-9446-7b92542ea763 | -9.52195 | -60.54136 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e97fe93-d80e-3c32-974d-a539acc06189 | -9.21943 | -67.45841 | 2025-08-21 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 056781b5-302e-3eee-99f2-ad68e009b7b7 | -9.2099 | -59.45606 | 2025-08-21 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 426a28e9-1ca3-3b42-be38-0390c8f41f5d | -10.40435 | -59.37778 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b820d5e-bf3a-3abc-b080-92dd990f3e19 | -9.21886 | -67.46207 | 2025-08-21 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a161b9-cd4a-3506-8304-88c11ff71b41 | -8.68132 | -62.09105 | 2025-08-21 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c467605-4795-371d-971d-608970dab5e5 | -12.58778 | -60.36385 | 2025-08-21 05:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e42c96f0-66a3-3c48-9d4c-bc402df60ffc | -8.69007 | -63.6717 | 2025-08-21 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0322481a-f38b-364a-8e9f-05502c740291 | -8.8736 | -62.4115 | 2025-08-21 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 69eb570f-2007-331a-833f-c3513aa85069 | -7.0164 | -44.6413 | 2025-08-21 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 24b1a1ca-621b-3a70-b956-5527b5dab99a | -7.0354 | -44.6167 | 2025-08-21 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| bb460025-b599-3960-96c7-105365d8cd66 | -7.0352 | -44.6396 | 2025-08-21 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 2860191f-239b-3237-add3-54168ea974f2 | -7.0166 | -44.6184 | 2025-08-21 06:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| f678fbda-b08c-3359-8769-68b1150765f4 | -8.8737 | -62.3925 | 2025-08-21 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 76bc9e69-84e7-368e-9386-60e98f8975e6 | -8.8736 | -62.4115 | 2025-08-21 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 127.9 |
| ecb6291c-3eac-3f69-84c8-47adbcba9db8 | -7.0166 | -44.6184 | 2025-08-21 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| ffa11fef-6a67-384e-882c-138ea126d41f | -7.0354 | -44.6167 | 2025-08-21 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 0c770f33-a580-3ff1-b3a7-1ae90e0fb8d3 | -8.8737 | -62.3925 | 2025-08-21 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 156.2 |
| b4de515b-95a7-3a81-961a-66165ef8678d | -7.0164 | -44.6413 | 2025-08-21 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| fc3977ae-28c4-3f89-aebf-22a33f744d80 | -12.8988 | -46.0677 | 2025-08-21 06:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b1edc6dc-cb6a-3a76-ac16-45f184dbfb9a | -8.8551 | -62.4123 | 2025-08-21 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| bc573243-4881-3d30-97ef-9dfb560d4192 | -8.8552 | -62.3933 | 2025-08-21 06:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 178dabcf-a508-31f9-af24-8ffca4380256 | -7.0352 | -44.6396 | 2025-08-21 06:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| fa831c31-9a9f-31d0-bcc5-f3da644a8e2c | -13.051 | -45.1693 | 2025-08-21 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a58ddefa-e1d0-3961-9c74-1425b78b5d58 | -8.8737 | -62.3925 | 2025-08-21 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 4e429a1e-4fca-3899-9099-d5401df2d020 | -13.0321 | -45.1492 | 2025-08-21 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 8ee3b026-7086-38d0-9f0d-f60f8e657dc2 | -7.0166 | -44.6184 | 2025-08-21 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| be9d1462-b09e-3ebf-90a2-6b304f67fa16 | -8.8551 | -62.4123 | 2025-08-21 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8a50052d-3a59-3664-8bcf-c6c607e80136 | -13.0128 | -45.1523 | 2025-08-21 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ebe347f7-2892-3a8a-b767-fb00e1c480e1 | -13.0317 | -45.1724 | 2025-08-21 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 62a4b5f3-e983-3dc0-9b68-16fc212e2e9b | -8.8552 | -62.3933 | 2025-08-21 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 30983df7-8fc5-34ae-9375-66cb50d2e42e | -8.8736 | -62.4115 | 2025-08-21 06:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| b51037c6-d2df-30b3-b41a-dbb95ddbcf5c | -7.0352 | -44.6396 | 2025-08-21 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |


[Clique aqui para ver as próximas entradas](README57.md)
