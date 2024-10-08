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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4ddab21-0fbf-30d0-bc22-6ebe4f79df24 | -9.57956 | -64.1177 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f6a1ea1-acc4-3300-98a8-f6c8a41dca89 | -9.57893 | -64.12102 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bddf919b-4882-37d4-8e11-2b20bc1f7619 | -9.5778 | -64.11362 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5353ad71-f9f3-32e8-850c-fbde5ed5cc6c | -9.5772 | -64.11695 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fc235ad-ee1f-32d4-8d16-4cb0d4d53b26 | -9.57658 | -64.12032 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6df5fe34-0ffe-379f-9676-514386888d25 | -9.57245 | -64.11254 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 969617fd-4ea5-3934-ae8a-e7ceb5619552 | -9.57183 | -64.11594 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ddaa8dd-eadc-3dee-bdf1-c59dcc19f8f0 | -9.56908 | -64.22269 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a682f02-ccca-32e2-bb21-1f0930691fc5 | -9.56846 | -64.22611 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec15ef4-d1bd-3e66-a000-7194619af251 | -9.5653 | -64.22215 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29a26422-3788-349b-8856-a94be3bfdd79 | -9.56466 | -64.22555 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cafa942-24b0-3f6e-b6ff-64e85dc2932e | -9.56368 | -64.22167 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eb368a0-5351-3faf-8887-9be1df9222c7 | -9.55176 | -63.57747 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd1f68ba-0ca9-3027-82e4-8d2837c15071 | -9.55006 | -63.58685 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbde4874-db3b-37ef-9baf-360efa628ddb | -9.54772 | -63.57026 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c9a5d3d-721f-3374-93aa-bbbb25ac9173 | -9.54715 | -63.57336 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ecc28984-90cf-3acf-89d2-6d68d035d92a | -9.54659 | -63.57647 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| faa19e9c-6e7b-3a67-986d-b38428cc8f76 | -9.54602 | -63.57959 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c51e237b-c4f8-3902-a21f-ab223bb346f3 | -9.54545 | -63.58271 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3b2b66c-3978-3400-8c98-1eb8a60857da | -9.54488 | -63.58586 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7eda155e-c0b4-341c-8b6f-4dade0acedf5 | -9.54431 | -63.589 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 160db12a-6c53-32fc-b2dc-1f4c9b02629c | -9.41435 | -63.71003 | 2024-10-08 04:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c84c67a-f30a-30e6-80db-94f0046cf510 | -9.40911 | -63.70906 | 2024-10-08 04:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a6d1d40-b9d6-32a6-be34-30d7d76b0540 | -9.4085 | -63.71237 | 2024-10-08 04:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 740d4d40-26dc-37b8-b673-bfe70298b486 | -9.35811 | -63.80893 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ed862f9-aa11-35ab-9e1f-262ea178bbd9 | -9.35755 | -63.81196 | 2024-10-08 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29d7856f-1f15-3bb4-82e7-425181cd8282 | -10.02919 | -63.47672 | 2024-10-08 04:57:00 | NPP-375D | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac60cca8-d980-393b-8eac-a6f675e8927a | -12.19387 | -63.66905 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa44bd0e-5895-362c-babc-9feb28b38f25 | -12.18889 | -63.6681 | 2024-10-08 04:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74c1510d-d6de-3619-974b-f9b13205f9df | -10.88038 | -63.90813 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc6dbfe2-fb62-32a2-b65f-022918b7e3fe | -10.87868 | -63.91727 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 302b6ef6-59d9-37dc-a313-139a59d493b1 | -10.8781 | -63.92039 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8cec45e-e225-3bc9-9059-f373e98a967b | -10.87568 | -63.90464 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b89e013-3753-3120-b76e-f810ae2a85f0 | -10.87515 | -63.90747 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3077298-a748-366a-9df8-d6e06898db5c | -10.87463 | -63.91025 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86b7c57d-6d62-3910-9077-42ea45ee4e41 | -10.86991 | -63.90686 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 771703c7-7daf-3d68-a5a8-873e86874477 | -10.8694 | -63.90955 | 2024-10-08 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e15d7c6-6354-3592-8c77-471d41b2a63b | -10.86808 | -63.888 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d687b17d-018e-3ab1-98ab-3d993f20763c | -10.86751 | -63.89107 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be86c0ac-0ce4-36ea-bcab-c2e80927196e | -10.86358 | -63.91204 | 2024-10-08 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afd5f1e6-12c6-322a-a714-6b6c804a6319 | -10.86301 | -63.91508 | 2024-10-08 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5f129ec-6cf5-31bb-ad3c-bfc55228bb49 | -10.8629 | -63.88715 | 2024-10-08 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ac54165-6ecf-3d99-9754-4775684ee33b | -10.8623 | -63.89035 | 2024-10-08 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2e0486d-ec51-30ac-927f-d609b30fb3b4 | -10.4171 | -64.83363 | 2024-10-08 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b7f28ec-744c-34b1-8760-cefc29cd12a0 | -10.41637 | -64.83736 | 2024-10-08 04:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d6c2a59-b9b3-3caa-a619-535d25775680 | -11.6698 | -65.21578 | 2024-10-08 04:57:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 178c3097-a924-375e-8f25-c3094b23da0c | -18.81767 | -42.98471 | 2024-10-08 04:59:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| fdfd93c5-eb27-31db-9456-0c1989b16096 | -18.81067 | -42.98357 | 2024-10-08 04:59:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dbf3bd40-bec7-3149-8d42-8f130bbe866d | -18.55835 | -42.40389 | 2024-10-08 04:59:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 45cbbb62-bc9e-3b9f-adc8-8faca7de6a37 | -17.60905 | -43.25851 | 2024-10-08 04:59:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a901803f-297f-306b-9115-256a3773ddd2 | -17.60222 | -43.25768 | 2024-10-08 04:59:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb19d49e-a9eb-304b-b508-52c04cb77e9a | -19.45338 | -44.11913 | 2024-10-08 04:59:00 | NPP-375D | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79ff3d86-8424-3ea9-9c07-89b61ef0ffcc | -19.44678 | -44.11806 | 2024-10-08 04:59:00 | NPP-375D | PRUDENTE DE MORAIS | MINAS GERAIS | Brasil | 3153608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7a0a8c1-a931-30eb-9fd6-8eb84b2c31b8 | -20.91243 | -43.7438 | 2024-10-08 04:59:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fa3216f3-9500-30e6-bfa4-9b97bcdeef59 | -20.91203 | -43.7493 | 2024-10-08 04:59:00 | NPP-375D | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 63e18cae-e662-3ff8-8881-572a43b7e5cf | -20.40647 | -43.93403 | 2024-10-08 04:59:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| e3befcd0-c3a9-3c4d-8832-454d643167b7 | -20.40615 | -43.9381 | 2024-10-08 04:59:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 6636ad38-4b73-32a2-af53-c323ba3bedca | -20.40577 | -43.94291 | 2024-10-08 04:59:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 32f16c7a-afe8-3fc8-96ea-d17e60e67031 | -20.40538 | -43.94792 | 2024-10-08 04:59:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| cfa11465-236a-3652-aafe-0c03646dc71a | -20.40415 | -43.93448 | 2024-10-08 04:59:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| bbb05440-42cc-3daa-84a2-824a30fc35c8 | -20.40381 | -43.93856 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 6d40785d-2281-3941-9ebb-3478d9f1b93d | -20.40341 | -43.94336 | 2024-10-08 04:59:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| ca445238-e996-3f83-89f4-9d7c052f8ca5 | -20.40299 | -43.94832 | 2024-10-08 04:59:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| a8e29d03-e49c-320d-a781-7dc7ee59180a | -20.39968 | -43.93363 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 8f338398-eb48-3b2d-a4ae-721f31e73bd6 | -20.39938 | -43.93753 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7644610c-1d56-34c9-9cc4-90cc8c76d361 | -20.39903 | -43.94199 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 32b3f85f-0d7c-3787-b13e-2e1522afe363 | -20.39865 | -43.94688 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 66dd93d7-85d3-30e4-b4bc-8fe020af78ab | -20.39706 | -43.9378 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 11e35dcd-88dd-3c89-ab13-c49233f86620 | -20.39669 | -43.94226 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 5f9d2cab-ecf3-3cf5-93df-1c3f9f79edbe | -20.39628 | -43.94717 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e699c0cf-5e09-3925-aab0-ea3e78ace82b | -20.39577 | -43.95319 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 3bcf9ddd-8c87-30d0-80dc-7ea3897dfe07 | -20.39257 | -43.93737 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 25ebc345-8999-37d5-8f6a-d1ba9cfb5965 | -20.39223 | -43.94176 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 2509da0b-3e29-3eb0-852b-041f1c3b8fa2 | -20.39186 | -43.94652 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| fa961a73-7ca6-349e-aa83-b74f4d5c267b | -20.39145 | -43.95189 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 7f29eea7-0c7a-3893-b7d6-6d5dc490f952 | -20.38984 | -43.94256 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1cd2662f-cc1c-373b-9e01-80cdf7423e36 | -20.38945 | -43.94731 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4e3aa3ae-954c-34a7-9d24-92932eff89a0 | -20.38903 | -43.95234 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c012a4fd-c499-3a91-91cc-4f76905947ba | -20.38467 | -43.95149 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af9e2f26-72f2-33b4-9f18-2d7bdc8abf19 | -20.38425 | -43.95694 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0b58bd14-6783-3d48-bdd8-c3b91f3bdd70 | -20.38224 | -43.95216 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7a2d557c-ad2f-3874-9568-49e2a5371410 | -20.38179 | -43.95751 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b85119d0-95f4-3541-8c2c-56d927dd1b3e | -20.37789 | -43.95116 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c58ec96f-3ad4-3309-addd-a2a0c77a2594 | -20.37748 | -43.95639 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fb4dc442-5c4f-3de5-8374-49d1e3ed7dab | -20.37709 | -43.96148 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 501a6831-8c76-3ce3-a385-b4de4fc1f232 | -20.37547 | -43.9516 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4c060a9c-d78f-3b3b-a5af-6b9d66077d17 | -20.37505 | -43.95668 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1b39fa0a-1456-33b7-b825-c567d812e63b | -20.37463 | -43.96174 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8f7d9b89-0ff7-3230-84d7-b1caa4533537 | -20.36227 | -43.94641 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0c48acd5-bea0-34c9-b962-3ce1c9a86e9b | -20.36188 | -43.95122 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 789f3c00-a982-3b1b-90e9-eeafd5db3e06 | -20.35677 | -43.93033 | 2024-10-08 04:59:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e4322de1-ad09-350d-83fa-2c727c4787e5 | -20.35612 | -43.93842 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 961d96c1-1dbf-357d-b3f0-01b53eede020 | -20.35577 | -43.94262 | 2024-10-08 04:59:00 | NPP-375D | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 09217984-ce0e-31b2-9b71-61aa0b217155 | -20.23057 | -44.4395 | 2024-10-08 04:59:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| aac74e06-d6be-3cff-939b-97b7ad931ede | -20.22995 | -44.44664 | 2024-10-08 04:59:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 81799a15-3227-3332-9112-41cfef2d3563 | -19.87063 | -45.02911 | 2024-10-08 04:59:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fc3156c-afaf-3073-b63e-2515665cfba2 | -19.87016 | -45.03429 | 2024-10-08 04:59:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 512d48e8-4b1b-3660-a279-0c5bf2b735a7 | -20.65402 | -45.91969 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43e035fa-df1c-374f-9db7-df667fc0c304 | -20.65363 | -45.92417 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ee11acc-697b-33c5-9eb3-68647cdff648 | -20.65238 | -45.91843 | 2024-10-08 04:59:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README91.md)
