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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9c853af-73bd-3fb0-b350-ff71341edebd | -9.1622 | -60.391998 | 2024-10-12 01:19:14 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be536699-3380-3fde-b3bf-f0befe151531 | -7.8782 | -54.693501 | 2024-10-12 01:19:14 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8718381a-c0ab-3544-bb39-9a7fbf91c199 | -7.8798 | -54.7006 | 2024-10-12 01:19:14 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0fce8ef-1ed3-34eb-a628-54ac89d0ad03 | -7.8814 | -54.707802 | 2024-10-12 01:19:14 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27eee95f-222a-33d2-adef-8adb3643073a | -7.8831 | -54.714901 | 2024-10-12 01:19:14 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4babc0d-9102-3775-84c4-fbe0c5d295fa | -9.2053 | -60.783298 | 2024-10-12 01:19:15 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1edb9d7-f27d-31f7-9d79-b77aca1f5f10 | -9.2076 | -60.793999 | 2024-10-12 01:19:15 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86555afa-6253-33b4-80e0-8698635c1cd4 | -9.0776 | -60.569698 | 2024-10-12 01:19:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 934863eb-4466-3c2f-b464-6329ee67cf7a | -9.0798 | -60.579899 | 2024-10-12 01:19:16 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 344640e0-14c0-34d5-86e0-f4f6807dc651 | -9.885 | -64.785698 | 2024-10-12 01:19:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ec134f94-ff1b-306d-87a1-baabf7e2aa6c | -9.8891 | -64.806 | 2024-10-12 01:19:17 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd76c54-c055-3ac7-97eb-beb9cbdaf32f | -9.4938 | -63.120998 | 2024-10-12 01:19:18 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40e69f2b-b325-38e2-9961-8b5d17bdfca3 | -9.5782 | -64.072098 | 2024-10-12 01:19:20 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db7b2ac1-5352-38df-bd92-e38aadf5da22 | -9.5819 | -64.090103 | 2024-10-12 01:19:20 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de565ad9-b9eb-3858-b47b-9cedfd1e1440 | -9.5615 | -64.188698 | 2024-10-12 01:19:21 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2ee111b-2cc0-3f31-a4e6-12060f8ee584 | -5.6663 | -47.9216 | 2024-10-12 01:19:24 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d1224994-d69b-3441-9ace-fcea7dad1a3a | -5.6566 | -47.924 | 2024-10-12 01:19:24 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef0e493a-2853-31fb-aa91-8f8b7b94b8a1 | -8.9633 | -62.335201 | 2024-10-12 01:19:24 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed214d30-e22f-3257-899e-0df51efddd72 | -8.9661 | -62.348499 | 2024-10-12 01:19:24 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87a9beb0-8438-34f8-bcf7-0b6ce64d4fec | -8.9689 | -62.3619 | 2024-10-12 01:19:24 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 299d7361-4fde-3670-bf26-4b0214df155d | -8.9076 | -62.360699 | 2024-10-12 01:19:25 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac01e5c-55d3-3629-aa2d-fcd500ba100e | -5.5187 | -48.072399 | 2024-10-12 01:19:27 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f55bc7a1-aebd-3f4f-bee6-f63bd1b5f848 | -5.5231 | -48.090199 | 2024-10-12 01:19:27 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fdcfa55-22fd-3956-af54-96108858b4e5 | -9.0239 | -63.596802 | 2024-10-12 01:19:28 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d99dd924-f768-3665-8701-4a8efd2ff21f | -8.9195 | -63.533798 | 2024-10-12 01:19:29 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a08f9852-fe31-3fc4-a9dd-db3123249a63 | -8.9063 | -63.519699 | 2024-10-12 01:19:29 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a1a8407e-b84e-34ae-a714-5c1da5ef62cf | -8.9097 | -63.535801 | 2024-10-12 01:19:29 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b946a6ed-657e-3577-88b9-a1787bf82250 | -5.2641 | -48.0392 | 2024-10-12 01:19:31 | METOP-C | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7b1f91-c24d-3112-a650-79902ae4142f | -5.2544 | -48.041599 | 2024-10-12 01:19:31 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 642a3fb8-d37b-37a1-8eb3-b0d805ba8d8f | -8.2351 | -61.169399 | 2024-10-12 01:19:32 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6f6199-7039-3254-bc57-703741d17146 | -8.2375 | -61.180302 | 2024-10-12 01:19:32 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3ef0ff-c687-3ee4-958d-9a81028a9aea | -8.2398 | -61.1912 | 2024-10-12 01:19:32 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 391d7020-a787-398f-9f7e-c39b833a88f4 | -8.2253 | -61.171501 | 2024-10-12 01:19:32 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a59116b7-aa59-3d19-98c6-7035ae97229f | -8.2277 | -61.1824 | 2024-10-12 01:19:32 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb7d756f-64bd-3b74-b00d-5144896f11c0 | -8.23 | -61.193298 | 2024-10-12 01:19:32 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c40d393-0e99-3ce6-9b41-0f773f78c828 | -8.2179 | -61.184502 | 2024-10-12 01:19:32 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac12572-5fc3-3ffe-8744-7856d450cbcf | -8.656 | -63.245399 | 2024-10-12 01:19:32 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 945cc033-cdfb-32b4-beab-1187fef537c1 | -8.6592 | -63.2607 | 2024-10-12 01:19:32 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30cb392f-f42e-30c8-a6a8-4c7191bfd515 | -7.9088 | -61.505798 | 2024-10-12 01:19:39 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1467cd02-1817-3959-9850-6f1e76689932 | -7.4034 | -59.7043 | 2024-10-12 01:19:40 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf2d7cd8-a30d-3361-8e0a-100aeb0422b0 | -7.4053 | -59.713001 | 2024-10-12 01:19:40 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39c17873-9f52-352d-885f-51f9f9059f64 | -7.4073 | -59.721699 | 2024-10-12 01:19:40 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b43c6f89-66ef-3b6d-913a-14904ac11612 | -7.8235 | -61.631302 | 2024-10-12 01:19:40 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 553b59f9-efd3-3a4c-961d-789b9eaf8cdf | -7.3955 | -59.715099 | 2024-10-12 01:19:41 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d17ac63-e021-3f3e-9b94-bf28eb2f661f | -7.8137 | -61.6334 | 2024-10-12 01:19:41 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3bc1192-e968-38fc-b3d1-605ff224595b | -7.6567 | -61.1908 | 2024-10-12 01:19:42 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9463c4c-0fc5-36bd-8734-07409e5e0c8a | -7.5905 | -61.216099 | 2024-10-12 01:19:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83a6be75-ba2d-3506-b3af-c0c55acb6257 | -7.5929 | -61.226799 | 2024-10-12 01:19:43 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af59273a-9775-303d-afcc-93a5474f96d5 | -6.9158 | -59.033401 | 2024-10-12 01:19:46 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbb9488-56eb-31be-892b-fa8795952e73 | -6.898 | -59.0457 | 2024-10-12 01:19:46 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e41e4d9f-e2ea-3592-8075-f0dafa213382 | -6.8704 | -59.060101 | 2024-10-12 01:19:47 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3037b9aa-ff16-3ece-98dd-06bbb8e68466 | -6.8722 | -59.0681 | 2024-10-12 01:19:47 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3187aa58-e278-3fe8-bd00-23a58f00f1b3 | -6.874 | -59.076099 | 2024-10-12 01:19:47 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 134f6045-cc61-3387-bca3-01f7f9abd583 | -6.8642 | -59.078201 | 2024-10-12 01:19:47 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c892ff8-ef05-3e51-8bcd-cdd7ea59ecc2 | -6.8659 | -59.0863 | 2024-10-12 01:19:47 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8a7e06b-2a08-3255-8856-b5d485efda87 | -6.7559 | -58.869499 | 2024-10-12 01:19:48 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 264aa525-b8d4-3da5-b9a6-e0615f42f253 | -6.7577 | -58.8773 | 2024-10-12 01:19:48 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6b359ab-55dd-3283-8e59-42afdafdf995 | -6.7594 | -58.885101 | 2024-10-12 01:19:48 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2b87c5a-b6d3-35dc-89a3-5481c03fae44 | -6.8107 | -59.1152 | 2024-10-12 01:19:48 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8277fc12-7c67-3ffd-a326-01f5a20e3b74 | -6.8161 | -59.139301 | 2024-10-12 01:19:48 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5c05e45-c8d8-3794-baf2-5fac30075937 | -6.7461 | -58.871601 | 2024-10-12 01:19:48 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 471bfcf0-6345-3a81-a08f-6bd0dc3a657c | -6.7479 | -58.879398 | 2024-10-12 01:19:48 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d420a603-0a03-34f5-9734-60fe12f3bee3 | -6.7622 | -59.312901 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd80209f-8f60-3e94-bbfd-2531d91d646c | -6.7626 | -59.083698 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3665c99-5184-3824-8660-6bd2c63de105 | -6.7644 | -59.091702 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53e42c6e-d1eb-3424-9b43-8cc5ae28b582 | -6.6826 | -58.771198 | 2024-10-12 01:19:49 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3a92651-9b34-3d91-b753-7e86095bff5c | -6.6843 | -58.778999 | 2024-10-12 01:19:49 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4f330cf-b5bf-3e1c-bc84-f63132646508 | -6.8069 | -59.328899 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4044af-345c-33af-b756-b6d907d3ae7f | -6.7916 | -59.3064 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4342cd39-451b-3abc-a4fe-42bb6fbe5996 | -6.7934 | -59.314602 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1a95304-6a9d-3b47-9002-54a5156f3a99 | -6.8007 | -59.3475 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 605cc48e-5c45-32f1-a83b-3703e4d4db20 | -6.8025 | -59.355701 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae268a5d-a78a-30fd-8580-e2aab875aa36 | -6.7818 | -59.308601 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac12854d-0e49-3a6f-b8fa-822cd4c50bee | -6.7836 | -59.316799 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 113af7c5-6e34-3574-aa3c-1c29dc8bfa3a | -6.772 | -59.310699 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b36578cb-7174-3ce5-9de9-8d39b93c08f6 | -6.7738 | -59.318901 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52064dfc-7cca-3ed4-9603-8bbc46ef7507 | -6.764 | -59.321098 | 2024-10-12 01:19:49 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0b6f757-94c7-36e0-a263-9458583af237 | -6.7469 | -59.290501 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c8fdb9a-6ac6-3243-a592-9c26c80b78ad | -6.7488 | -59.298698 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d983a5c-e8e1-3ade-a0ae-1f03b463fc2b | -6.7524 | -59.314999 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d001da45-0935-3dad-947d-ec631ca6547a | -6.7542 | -59.3232 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93255f7a-f44e-39bb-95b7-5ed30841734c | -6.756 | -59.331402 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f300fc0d-3f1d-3c6e-9c2a-786abbfbe949 | -6.7579 | -59.3396 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf29fe2-77e7-362a-b032-8b5338f62dde | -6.5369 | -58.3965 | 2024-10-12 01:19:50 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf0a263e-e268-3652-ad02-5a1734577a3d | -6.7371 | -59.292599 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec0f207-b61f-3f1b-8a80-57f3f2c60a57 | -6.7426 | -59.317101 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b06f36b2-2e8a-35fd-8baf-6489abb789db | -6.7444 | -59.325298 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dcbcbbea-7c1c-3a70-af9a-820f73b3a2c4 | -6.7462 | -59.3335 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 741ba856-5cd5-326a-9640-3e2590db5cdf | -6.7481 | -59.341702 | 2024-10-12 01:19:50 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82f65df3-7cc6-346e-ad5b-147f49144c66 | -6.5254 | -58.391102 | 2024-10-12 01:19:50 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a412c5a-9ec9-3e3f-9bd9-693b9ed932cf | -6.5271 | -58.398602 | 2024-10-12 01:19:50 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fec55694-1da8-3c51-ab68-db262f270e64 | -6.5287 | -58.406101 | 2024-10-12 01:19:50 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2ebe0bf-18ff-3000-8969-eb2db826b114 | -4.1228 | -48.238201 | 2024-10-12 01:19:50 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c89348-e701-3067-818a-a3fa9cde5f5d | -4.1272 | -48.2565 | 2024-10-12 01:19:50 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3405dac0-0fe6-3e5c-a9e9-b8334769935e | -4.1131 | -48.240501 | 2024-10-12 01:19:50 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2ea956-4af3-38b7-a21f-0df16a06f12f | -6.4831 | -58.4319 | 2024-10-12 01:19:51 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 739ac78d-8efe-3827-b1d7-a6842e2cfa52 | -6.4848 | -58.4394 | 2024-10-12 01:19:51 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6565d2c6-97b5-380f-94a1-d5c7d713f9c9 | -6.6801 | -59.451801 | 2024-10-12 01:19:51 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5adda37-f192-3de9-9902-2063baf1a330 | -6.8294 | -60.126099 | 2024-10-12 01:19:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4dab4c8-f0e9-316e-9e0d-deea30e31872 | -6.8177 | -60.119202 | 2024-10-12 01:19:51 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
