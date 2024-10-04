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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8773b6c7-05b8-3945-ab74-3789db91ea58 | -21.31623 | -48.87856 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf8705ab-2616-3d40-a0b3-f791b15a4114 | -21.3157 | -48.9076 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9896182-fedd-3501-a85a-6e5713903c4a | -21.31566 | -48.88263 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b375fd3-e8f2-376e-9596-3d839c0d0e68 | -21.31451 | -48.89074 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2327ca3-6e6f-346e-8447-fe3173377c85 | -21.31337 | -48.89887 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5afa9aed-f5d2-3ce0-8d7e-f04d98405cfa | -21.31279 | -48.90295 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee6b0b98-c512-31b3-a7c3-1a89e741549b | -21.31221 | -48.90705 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 817bac27-b81f-3e7d-b5f4-1e3f48996166 | -21.31217 | -48.88205 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 84a19601-f515-3326-9c61-45b835fbdbb2 | -21.31163 | -48.91115 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dee79321-20f2-3f88-870a-d7d886bf233e | -21.3116 | -48.8861 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e357f061-7009-3fa1-a213-d76fed4c3354 | -21.31106 | -48.8833 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c82013b6-e866-360f-8d54-4f6c84abefbf | -21.31103 | -48.89016 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cc18fc14-7199-3a12-9a16-240fb4786695 | -21.31047 | -48.88735 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 81f07a87-d29e-33de-a43f-e36c45ebaecb | -21.3093 | -48.90241 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9daa96e-656f-359e-8d23-9b7a453f1362 | -21.30929 | -48.89548 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02e16aeb-b0bf-370b-80fe-d7ecbfbafbb5 | -21.30872 | -48.90651 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 810dd51c-05d5-38df-ab47-303c8c4294db | -21.30816 | -48.87867 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e471f492-6382-3f7f-b6fe-d94560501d12 | -21.30811 | -48.88553 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e36bc940-be63-3d48-ae86-5efb569c2180 | -21.3081 | -48.90367 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e26aaa9-2312-3b9e-bee1-487e9bf36385 | -21.30754 | -48.8896 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fd923974-e9b8-3c6c-97f9-4d02dcd88ac8 | -21.30698 | -48.88678 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d6ff06ba-b6b3-3f78-b301-142c1f3fd141 | -21.30696 | -48.89367 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff542f89-8703-3ffd-9d77-46b2ebdda31a | -21.30639 | -48.89777 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 554f8bb1-3c26-3072-b9d7-aa77f0d19701 | -21.30581 | -48.90188 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f32a43e5-673c-3a35-8c7e-6acc9eb36f98 | -21.3058 | -48.89493 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 000d0d6c-028b-3507-9d56-e403e531a76c | -21.30523 | -48.90598 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2bea3f89-1ac8-306f-9de3-82ab00ab4e5c | -21.30461 | -48.90314 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81f5a758-51e3-3217-811a-e9ffbbd0d3eb | -21.30402 | -48.90722 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c0f9210-3310-3958-8076-c90bcab70a8d | -21.3035 | -48.88621 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bbb07b1-26b2-37b3-9068-16b7dc32ad25 | -21.30343 | -48.91128 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e796aa38-af93-300f-a907-f5fc5a02c75b | -21.30053 | -48.90666 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0a13bb87-59a4-3b96-be6a-7a0232e7366f | -21.30001 | -48.88567 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca0a90bd-78b6-3982-a16f-a36d9cd2cd76 | -21.29995 | -48.91071 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0e1f5c29-0b3c-3243-8eaf-54af816f810d | -21.29942 | -48.88975 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ec784ed-1876-3e09-9f54-c2f8dd49a23b | -21.29936 | -48.91476 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6694af56-ca2d-3141-b240-af9bb9646ccd | -21.29823 | -48.89795 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bd79167-ef1b-39cc-86e0-006e669a749f | -21.29705 | -48.9061 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b9d902e2-9f79-3fdf-81ce-761a2e7bb2d5 | -21.29652 | -48.88512 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 00fd9d32-89ef-3768-821a-44731c79a51b | -21.29646 | -48.91015 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 288a4777-e823-33d3-92b1-03bc5be754ed | -21.29593 | -48.88921 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 595f8f12-c361-3a5f-b53b-72c1ddc75ed7 | -21.29588 | -48.91418 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.5 |
| c3278e2a-ed52-3c8c-b353-b258b67d4232 | -21.29533 | -48.89331 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b1beec63-1b29-3271-b4b0-ab58d553c19f | -21.2953 | -48.91822 | 2024-10-04 04:36:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2fe56b31-1a8c-376c-8327-265081f4561c | -21.29474 | -48.89741 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2038f500-d3f5-3bd4-8862-53b9d5c6df53 | -21.29415 | -48.90147 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9d68156c-df4f-3bf6-a5e8-b433c95a1320 | -21.29357 | -48.90553 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4934ea67-04fe-3c4f-bda1-98ac1023c28c | -21.29298 | -48.90957 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8bdd1324-930c-3c11-a5fd-dd519ad9e5f0 | -21.2924 | -48.91361 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 13b5a373-31b9-30fb-9bbd-a86841567d73 | -21.29184 | -48.89276 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4c6e8ab1-c21f-34f7-afa8-29caf505ec0f | -21.29181 | -48.91767 | 2024-10-04 04:36:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 28.5 |
| cde5eda8-bd8d-3f77-899f-92e5b55f1e9b | -21.29125 | -48.89685 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8766a8f2-4a76-33d0-89a9-c126e051f753 | -21.29067 | -48.90091 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9475051c-dda2-3332-af85-775e154424eb | -21.29008 | -48.90496 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fbe9089c-d49e-3017-801e-a3a4af7a0a48 | -21.2895 | -48.90899 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 88063773-e69e-3d23-993d-424ef65658a2 | -21.28892 | -48.91303 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 775fe9c1-b00c-3e28-a3c2-5ed28ccc4ca0 | -21.28833 | -48.91711 | 2024-10-04 04:36:00 | NPP-375D | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 6be70627-e881-3a5f-87f6-0784b5e72ab3 | -21.28777 | -48.89629 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 126a80d3-1d0e-343b-9caf-e608dfed3769 | -21.28718 | -48.90034 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 85800732-1441-34a4-a0b6-9523d7a61d6e | -21.2866 | -48.90438 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d7dd5774-84b9-386c-b150-9957801b5577 | -21.28602 | -48.90841 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4d6a7178-7731-3fee-adf0-c8733e915928 | -21.28312 | -48.90379 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 33.8 |
| d2e09670-316e-3a77-9093-43daf6175764 | -21.28253 | -48.90784 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b90499d5-190c-3480-9a40-923d59b8a031 | -21.27964 | -48.9032 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ba42f17-5a16-3445-b0cf-13990c6b8862 | -21.27905 | -48.90727 | 2024-10-04 04:36:00 | NPP-375D | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1de8dc48-af1a-3578-a265-e0ae5f3ba721 | -22.53855 | -48.81371 | 2024-10-04 04:36:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48be2a68-fde2-3cf9-b95b-a70c70f63cd4 | -22.46611 | -50.12038 | 2024-10-04 04:36:00 | NPP-375D | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efa99f6f-b49e-359e-9d71-4fb02a6240a8 | -22.46273 | -50.11979 | 2024-10-04 04:36:00 | NPP-375D | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d8922d8-5d58-3749-a51a-be21ff6e40ba | -22.46215 | -50.12368 | 2024-10-04 04:36:00 | NPP-375D | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e8b131e-1a5a-3470-9f11-678b78790395 | -20.86545 | -50.96544 | 2024-10-04 04:36:00 | NPP-375D | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cebbd83e-a2fc-32ed-a85d-50f46cf5da87 | -22.27157 | -51.48484 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 91c61906-6739-30f7-90cd-63fb03f1d07b | -22.26824 | -51.48424 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| f99c6827-3325-3899-83e7-d2bdff99add5 | -22.26765 | -51.48797 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ab6b0c5e-5e53-3627-8d11-512d286e08d9 | -22.26706 | -51.49171 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 602d9bdc-f8a9-37e8-9941-576d8e35c2da | -22.2655 | -51.4799 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| f39a627e-4baf-3ad6-a436-8b7d4a50859a | -22.26432 | -51.48737 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5b182446-b979-3b9d-85d4-129fea1c1230 | -22.26373 | -51.4911 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 05bf8c63-6935-320e-8d53-341cfd7511c8 | -22.26217 | -51.47929 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b2a36432-0815-3504-bf4d-c5e4477e692d | -22.26158 | -51.48303 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d60c43e7-694c-30b1-97f5-bec5461a7189 | -22.26099 | -51.48677 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c74d7cbe-8d78-3f14-b0d1-c91671e4bf53 | -22.2604 | -51.4905 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 599e8323-b5e2-37e3-ab49-890d938ed86c | -22.25982 | -51.49423 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 964f1c26-4b16-3980-a928-82d28b5097ca | -22.25766 | -51.48616 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eda7f591-dfb4-3722-998d-a9a39ca0b29d | -22.25707 | -51.48989 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f8d03000-a5ef-3387-9b3a-eec0ba319d63 | -22.25648 | -51.49363 | 2024-10-04 04:36:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5008b273-195d-3b95-96dd-52cf082c5990 | -21.5506 | -50.75448 | 2024-10-04 04:36:00 | NPP-375D | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ba1b255-84de-38d6-bfae-c7e115187a54 | -21.55002 | -50.75821 | 2024-10-04 04:36:00 | NPP-375D | PIACATU | SÃO PAULO | Brasil | 3537701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a103edb-cad7-3629-b75b-4ea2ce3f292a | -21.42975 | -50.98209 | 2024-10-04 04:36:00 | NPP-375D | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f6c7dbe-1438-3437-8d7d-f092010861aa | -24.24383 | -50.73833 | 2024-10-04 04:36:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3662070d-ac66-3de0-a6bd-8bb4b30dd458 | -20.99732 | -51.79129 | 2024-10-04 04:36:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| be616ef2-3506-352b-914f-69623a9e35ba | -20.87559 | -51.49908 | 2024-10-04 04:36:00 | NPP-375D | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8915d50d-5434-3cf2-a726-18eb1bab88cd | -22.60657 | -52.55426 | 2024-10-04 04:36:00 | NPP-375D | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 01c4d6fe-4471-3ad0-9962-35aea24a3c01 | -22.5606 | -53.18935 | 2024-10-04 04:36:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a0144b26-abd1-3ac5-9188-ae248303d245 | -21.99524 | -53.69491 | 2024-10-04 04:36:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b66ed1f-a074-35dd-9a1c-a67ae1856256 | -22.12481 | -54.6673 | 2024-10-04 04:36:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1a886466-343a-333b-ba21-4599509c0c69 | -21.41814 | -54.18844 | 2024-10-04 04:36:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 916bc02a-5c27-3689-a839-0809e258950c | -23.81529 | -54.1955 | 2024-10-04 04:36:00 | NPP-375D | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40382530-5186-363a-99e5-6ae3ddf44f21 | -18.30771 | -54.25117 | 2024-10-04 04:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06b57a72-e368-3092-81d1-634af99c7ed6 | -19.95805 | -54.88685 | 2024-10-04 04:36:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b89504b5-1242-32b4-860b-f10e877f4b43 | -19.9576 | -55.48607 | 2024-10-04 04:36:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fb9ecca-efcc-304b-a3bd-74025fb5900d | -21.35296 | -55.68829 | 2024-10-04 04:36:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README137.md)
