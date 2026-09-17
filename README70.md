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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26226346-4a65-3341-8b54-32732d5fcb28 | -9.48819 | -56.75923 | 2026-09-17 05:18:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d499fe5-d9df-3ede-9261-791eca00da29 | -11.31755 | -46.78191 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6863230e-cef2-30e0-b7c3-08c0a01a50f3 | -14.1318 | -44.00755 | 2026-09-17 05:18:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5cbf12e0-2c5c-3b46-ac34-e86ada07ec78 | -11.58656 | -46.89128 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8875eef-7877-3c7f-ad66-239fcc9c9b13 | -11.33608 | -46.77309 | 2026-09-17 05:18:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7d9ee67-39d9-3850-8729-5f6bb2e219c9 | -10.52118 | -57.45478 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fb40d4d-f889-39f3-bea9-780d52d12f5e | -13.43115 | -43.8101 | 2026-09-17 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2f6adaf-f265-362d-aad9-bd8962feb861 | -13.68324 | -48.59471 | 2026-09-17 05:18:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 543a6eb4-ddb5-3b6e-b63e-d00b1636cad8 | -12.42181 | -50.81525 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba594710-3d02-3677-819e-b4daf4146861 | -13.75462 | -48.79804 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2350939-633b-3f1f-b869-445db5156ec6 | -13.38351 | -57.02466 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a9c10a9-c32c-3fc3-9005-b332bb6a65be | -9.098 | -60.97733 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be4867c9-8164-3149-af5c-b316daf13137 | -12.44679 | -50.79659 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5eb51871-6864-3d59-acd2-c2e25015d9a0 | -12.43295 | -50.79909 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d603455-2fcc-3e16-af4d-a42f6b55a6eb | -12.42412 | -50.79784 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28c32061-d6f3-3d19-9fd2-dbd055ab9068 | -11.89613 | -47.58469 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a108fd4d-8508-3dd5-a97f-778d306b8f0d | -12.44004 | -50.8134 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d58cb6f0-8124-30d5-82cf-6873d6971370 | -12.45297 | -50.78412 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78a6b8e0-a39d-374b-bab9-86097f22165b | -12.45418 | -50.84193 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 49b905bd-993b-3055-bf10-be71e1dbf716 | -12.14048 | -57.18623 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b431dcc-1e94-349b-b6f2-5614b440b389 | -12.51558 | -50.68963 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99400d00-2a94-3480-968d-c22ef30592f0 | -9.0973 | -60.97921 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1f113ef-8515-394d-bbc1-a3618a290fec | -12.45329 | -50.81526 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cadd9f56-9a3f-37fa-86a0-71f2402da380 | -14.14594 | -47.37565 | 2026-09-17 05:18:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 198678f1-2852-372a-8272-63fb0761dfdb | -8.75876 | -66.56863 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 686a2851-3656-3cfd-8c7c-bfe21af422ea | -12.43412 | -50.79036 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0309989b-7eb8-3042-8f29-ee3d2044f1c2 | -13.43814 | -43.81116 | 2026-09-17 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d085503-b0e6-3823-8a6f-8bba066ac1d2 | -11.81101 | -60.46328 | 2026-09-17 05:18:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 209f0d78-36bf-3cd6-b837-686bc35b4aef | -8.77431 | -61.39474 | 2026-09-17 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42120e26-9f76-3154-94c9-2a3303cb9020 | -12.41528 | -50.79657 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0687dba-4c61-3000-9254-5a00e1b50129 | -10.91383 | -46.30027 | 2026-09-17 05:18:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81524c73-3d88-3c1f-b6d8-f69b2ece27c1 | -11.98578 | -52.46948 | 2026-09-17 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 73e5996c-1052-343a-a591-218ea2d73fcd | -9.09338 | -60.97854 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c8474ef-bb79-368e-ad62-346ad2dde205 | -13.4359 | -43.81631 | 2026-09-17 05:18:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 662ea22a-513a-332b-b6aa-fb112144a7f7 | -13.37962 | -57.02768 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55d13b37-1c17-3399-86b6-e8f6fa7473e0 | -11.57227 | -46.86675 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae49ee52-33f1-360d-a5bd-87f457395423 | -12.43744 | -48.48292 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa207dc2-763f-3c60-b6e7-adf835b786d0 | -13.38018 | -57.02412 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c6554b2-ccaf-3e89-86d3-6e95c50a8d3e | -12.44038 | -50.8444 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3fdc18de-9c9f-3b0a-823b-1e0f0ad4efaf | -10.76589 | -46.20421 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0da2f6a1-da9a-3c5a-800d-9bcd68c3871a | -10.51059 | -57.45668 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbb255c6-17f7-3e5a-bbfe-32d50aaaa0d2 | -12.45153 | -50.8283 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 65090eb9-7ff3-3e8a-8e2c-95985b08281e | -10.82362 | -46.17271 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 843d13d0-8b81-3df8-a81a-ca2b97353b2d | -8.11161 | -64.12202 | 2026-09-17 05:18:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3517109-d20a-3113-ba88-b3c70737332b | -12.45535 | -50.83326 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8ad2324-53ba-338b-9cf4-4b65455bbecb | -11.31233 | -47.0695 | 2026-09-17 05:18:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 625d5dea-4077-3e9f-a574-8732b39d11fd | -12.45238 | -50.78849 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 789b4fa8-00ab-3b55-b882-a8cfce245534 | -11.13379 | -49.04008 | 2026-09-17 05:18:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e9b0a17-d010-367c-b246-0b1e53940c76 | -12.43224 | -48.48236 | 2026-09-17 05:18:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcbc23b1-a527-353c-b9bc-aca08b23fa21 | -12.14324 | -57.19031 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae4c4c66-461f-30d1-8701-d7b1f97fb219 | -9.09295 | -60.95796 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbf62f64-f74b-3bab-ab1c-9d46cb9a865a | -12.51247 | -50.83451 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a986d4c8-1ac2-3b77-b1a8-ea90a6779f54 | -13.38796 | -57.01809 | 2026-09-17 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e03bb37f-c7fe-384f-9d35-a1fd51aac59c | -12.4518 | -50.79286 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7d83985-36dc-3c0c-b294-756b2e98f97f | -11.60725 | -50.63611 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d4cb6bd-d0a6-36da-9003-ba652c3e3476 | -9.09549 | -60.99228 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51a7d8a3-5ad9-35a1-ad2a-a44735718a06 | -12.80838 | -60.48821 | 2026-09-17 05:18:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f6c3f6c-e13f-3739-affe-22daff43b880 | -9.2814 | -60.63346 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9dcf24df-34b6-3510-9112-0b61c49730c1 | -8.76118 | -66.56377 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79bf92dd-b6c7-3566-89f5-7ac5b77ab5ec | -9.29842 | -60.53473 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da6e0dc0-40ce-38c2-a6b9-273141795a70 | -12.32378 | -47.9551 | 2026-09-17 05:18:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa52c701-3805-3c7f-a28c-ac85756861ab | -9.28385 | -60.61928 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cbef69f-dc21-330d-b0f1-caca4583392c | -9.6171 | -55.08557 | 2026-09-17 05:18:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1757501b-cec5-331a-96ae-5d349701a1f3 | -11.98256 | -52.46383 | 2026-09-17 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b6e5e583-741c-38af-8790-1ca68c895f41 | -12.46299 | -50.84317 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16367e01-585d-374e-b516-ad026ab91a80 | -10.52509 | -57.45177 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0009d928-af40-31d8-9ae1-e3f1ff484b8f | -10.52061 | -57.45833 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a633eebf-b0dd-37aa-a8dc-dfd0edac5862 | -10.8316 | -46.15691 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a3c1b534-8be9-3963-aff9-9a15b92c74f2 | -13.74952 | -48.7969 | 2026-09-17 05:18:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b3e0762-b10a-3a5e-acca-03de9205319a | -12.45533 | -50.76661 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb87ae0c-357e-35e5-aba4-6210c76d6dc3 | -10.83642 | -46.16625 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bd25e86-8187-3025-9633-8e3b219bdb24 | -12.14729 | -48.25653 | 2026-09-17 05:18:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e46e196e-fabc-3087-8ff9-c011dece8f9e | -14.13363 | -44.01247 | 2026-09-17 05:18:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f129a51-d855-3873-91bf-b661185ce8a7 | -9.29462 | -60.53405 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e4a5fed-779b-378a-8eb7-1793eddcbfa8 | -11.88435 | -47.59037 | 2026-09-17 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92775cbe-de8c-3c76-aede-db2ee127d296 | -12.43121 | -50.81215 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f15a861-8304-3caf-8dad-eaf2471f0308 | -11.53198 | -46.86522 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55595808-6f2f-378e-9f45-8c2681cd671b | -12.43215 | -50.83883 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e6692d7-bada-3894-8e24-55e5c7fc10f3 | -9.09659 | -60.96167 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf41d913-9c99-3375-8936-e4bf3e58da58 | -15.4588 | -52.89309 | 2026-09-17 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c20cc36-6a62-3dab-bd45-0e7b6fb75333 | -9.77093 | -60.46484 | 2026-09-17 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 165e7e43-a1dd-312c-acca-676dc9eef6f3 | -9.09633 | -60.98729 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a8699aa8-1fb6-3048-aaa3-b8f547620765 | -12.463 | -50.77662 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e43f395c-0ed2-3eb8-807d-31daf7fb5d28 | -11.88953 | -43.8299 | 2026-09-17 05:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3904cc5c-340d-390f-92aa-ddb34819de3b | -12.51605 | -45.94634 | 2026-09-17 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcdcfd87-3755-3e11-aec6-ac68ad7116f5 | -9.41155 | -62.71286 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38bf7ac6-2639-3711-adf5-7bc3ed529c16 | -11.21222 | -46.40135 | 2026-09-17 05:18:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbb95e9b-976f-35b1-a7ee-8ffc4b560e57 | -12.42948 | -50.82519 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 413152a7-cc20-357d-a1d0-db8f6936ad8d | -8.75235 | -66.57147 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1172fe12-95fd-3255-9a15-2102950bbaa3 | -10.52232 | -57.44765 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79ad4bd0-c8d2-3f3c-8c87-b7bb78035569 | -9.11242 | -65.93235 | 2026-09-17 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a8911a1-5e42-3aeb-a8ca-b1909880b9e7 | -9.40719 | -62.71209 | 2026-09-17 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9cb773fc-e680-34f9-91b3-7cb65735fed2 | -10.57745 | -57.69372 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3cf17ac-2274-3a1f-9ca3-37ff852681fb | -12.42912 | -50.7941 | 2026-09-17 05:18:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9a21a7a-3217-3697-8b10-4415b0b3c759 | -11.54145 | -46.88242 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c0c8eb0-23c1-3f48-b6cc-21af7256c6e1 | -11.53148 | -46.8693 | 2026-09-17 05:18:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7704a0f7-b9b4-3073-a6e1-7fb21a2ae863 | -11.16087 | -42.79089 | 2026-09-17 05:18:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fb20d901-5389-3dc8-bfdf-551668daf482 | -10.52566 | -57.4482 | 2026-09-17 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e5717d-7510-31aa-bea7-abe3dcd47e54 | -9.09883 | -60.97234 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba46c96e-dfc1-34bb-a884-845b70a0c727 | -9.09465 | -60.9973 | 2026-09-17 05:18:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README71.md)
