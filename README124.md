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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4526ef30-b562-3cd1-858a-f58a4cc637c0 | -8.52026 | -62.05424 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7560c79f-e04a-336e-bb4f-a1e530d23e5c | -8.51972 | -62.05772 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0d862860-69b6-34f3-a999-2661e458bb02 | -8.51917 | -62.0612 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a62442-1d5c-3b5c-b433-8dcc051f3472 | -8.51695 | -62.05371 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20c3f558-afd8-3fe5-bb21-aa0b02f3a327 | -8.5164 | -62.0572 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42e26c12-846d-37f7-b856-4890b6d24939 | -8.11813 | -61.99811 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea00074a-038e-32c6-b5e9-dc221dc525d7 | -8.11758 | -62.00159 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a073948-ca3c-343d-8992-4c96cce6bf20 | -8.08506 | -62.0143 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ef32f74-98f5-3965-8980-a42253591668 | -8.08174 | -62.01378 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e0503f6-3482-348a-a6fc-806fe8c843f3 | -8.00454 | -62.03011 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17983b62-01e8-3cea-b365-f23f73be48f4 | -7.99569 | -62.0216 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72620a10-ee9c-385c-835d-467ca743bda0 | -7.99515 | -62.02506 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9fcd686-7809-3d34-9bf2-1f4abde3e755 | -7.98178 | -61.76263 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a33f2de-1dab-3d12-9dfb-9995bfcb38fe | -8.14783 | -61.2803 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 473de886-007d-3722-897b-11c7d474f3d0 | -8.14728 | -61.28385 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b431dd10-66a3-3da3-b852-22c2f2e2a33b | -8.14673 | -61.28741 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 841b0b44-42fc-3205-aaa6-9fd457c666fa | -8.14448 | -61.27978 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 651e985d-d1d6-3a10-bbd9-3a3bffb13096 | -8.14113 | -61.27925 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 587cbe17-1450-3e31-9497-d6bf5286f338 | -8.14059 | -61.28281 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| baaab725-40cb-3978-9d7d-542165127c66 | -8.13779 | -61.27873 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 264d3743-c27c-3b3e-a1da-564163a51f1a | -8.13725 | -61.28228 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37477402-2e99-3901-86f6-2d4ef75ccb46 | -8.13445 | -61.2782 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5742ab1-4c26-3e61-8433-c59231ddf0fe | -8.1339 | -61.28175 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84046c0e-aa9d-3f64-8745-14653f7350e4 | -8.13001 | -61.28479 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b021f82-6760-37af-abce-0c254d7b40ec | -8.09371 | -61.28293 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07962560-35bb-3e81-a1a8-2efd2fc9fe0b | -8.09091 | -61.27888 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22a4ae45-bb56-3097-95d6-1eb12bd6645a | -8.09037 | -61.28242 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0701543-6f20-3210-b6b8-d6defd548981 | -8.08982 | -61.28594 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39fb4c5b-a55b-33b8-a55c-43c7ce1ba3e6 | -8.08757 | -61.27836 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee84184e-24a4-3913-864b-0e1e862384be | -8.08702 | -61.28191 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1046671c-5f16-31b2-9599-9aace8e6ca72 | -8.08423 | -61.27784 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fd205239-2545-3a1b-b25f-c4a108d4b052 | -8.08088 | -61.2773 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea6b5164-fc92-3e2d-af61-04b21c0e7828 | -8.07699 | -61.28033 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5501ba77-5a81-3341-80d5-0dff4e549395 | -8.03679 | -61.25223 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dab808b-2f34-33bd-a437-3cb0ba914f28 | -8.03345 | -61.25171 | 2024-09-27 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faab1f46-8bf3-3281-9559-034d14a20f3f | -10.73731 | -61.56418 | 2024-09-27 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b9694dd-be88-38b2-ac10-e247c4583ee6 | -10.7362 | -61.57144 | 2024-09-27 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c89ed803-ef28-397a-8306-88129f5f1cfa | -10.73339 | -61.56728 | 2024-09-27 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c662aa33-8bbf-391f-b5fa-e1f32ff727b1 | -10.73283 | -61.57091 | 2024-09-27 05:27:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f6d05b0-59af-3c13-80c7-9001c604ff73 | -6.96387 | -62.92298 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7f1f2f3-904b-309c-a124-9a0676ece293 | -6.96331 | -62.92648 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e23302e0-7309-3089-a2b4-27039bc4c7a2 | -6.96054 | -62.92245 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb6bb845-f44f-3c8d-acbb-841d5204d25d | -6.95998 | -62.92595 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1483c94a-7223-3493-a0c1-ef7fdd042ae4 | -6.95666 | -62.92543 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 986d3590-053c-3663-bc80-caa28265d0d5 | -6.9544 | -63.00425 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66116d28-1f0e-36fa-a72c-a5d619d38e9c | -6.95107 | -63.00372 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0096a1ef-7444-32bd-a4a4-bcebf3635ef2 | -6.94996 | -63.01075 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f023d113-0539-3602-8ced-1da18df440ee | -6.93765 | -63.10996 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbb75206-9d79-310f-b846-c46788078997 | -6.93709 | -63.11348 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd25a06c-e48a-39c5-bd20-235e22d0933b | -6.93375 | -63.11296 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 386853c8-edfc-3b53-9fd6-f695999a091a | -6.85667 | -62.69791 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45a6d85f-23f2-3b37-b39d-cca87fe2bc3d | -6.85215 | -63.13591 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbd1a8ef-5677-3419-86c7-294b4c39cd00 | -6.84881 | -63.13537 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7151d313-8352-38f0-b50f-6a1cec2e29d5 | -6.84825 | -63.1389 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7964b0-9da8-3eab-bc6e-8729dc990975 | -6.84769 | -63.14244 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3747da4b-baa4-364a-92cd-2f493f43e980 | -6.84713 | -63.14599 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6b956f6-c759-316b-8dba-81babb0303f7 | -6.84657 | -63.14953 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f847caaf-b39f-335e-b60f-1005e01df32e | -6.84601 | -63.15307 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 629ad04e-b864-3d59-9193-dd9f6b6a5be5 | -6.84545 | -63.15662 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eb4e2f2-6f46-308d-8688-16b33fb4896b | -6.84488 | -63.16017 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24bb31be-8a17-3448-9c2b-7d621702faaa | -6.84395 | -62.69233 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8539f161-9838-3900-a1e2-2edf5c76daa4 | -6.84324 | -63.12723 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ccddaa-052b-37d1-a197-9f835831302f | -6.84322 | -63.149 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5f73736-4df0-3d67-8b6f-288de04086b2 | -6.84266 | -63.15254 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 66276cfd-af34-32d4-9a8f-87750196fdb2 | -6.84212 | -63.13431 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 274ef368-309e-3112-893e-4a1771bdc410 | -6.84156 | -63.13784 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba4a9701-cb5f-33e5-8680-22f0f819bb5f | -6.83822 | -63.13731 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98ca156c-42ea-3974-a965-c7a17fca2316 | -6.83766 | -63.14085 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d67d5ab8-ec96-3da0-84a7-f6efd2a2430f | -6.82761 | -63.16103 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f6fc4994-256d-3034-99d5-00bb6eab3c36 | -6.82539 | -63.1534 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 720a8e22-3247-39e5-871f-631491db012e | -6.82483 | -63.15694 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5a6f4c42-6c13-3408-90de-b8ad6d755717 | -6.82427 | -63.16048 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d3fd885b-49e4-3f21-b219-458420a5afa5 | -6.82371 | -63.16402 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7cdd6ceb-2f2d-3775-9ee1-c1957907eb25 | -6.82149 | -63.15641 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ea30326a-47d8-3751-b038-c7457592e8f7 | -6.82093 | -63.15995 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d0b142a8-f505-3186-9267-c57596ec82d3 | -6.82036 | -63.16349 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ffc5276-b846-3552-b41d-fecdbf137217 | -6.81814 | -63.15587 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dd8ac00d-3773-3284-a56c-517f10864185 | -6.81758 | -63.15942 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8b541802-506e-3a52-be53-612c7efc8c59 | -6.81424 | -63.15888 | 2024-09-27 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e733157-3332-368e-af11-7a644e0aacd7 | -6.60695 | -62.49467 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abd4a239-45a4-360b-9d7a-4152e0c7f7db | -6.60641 | -62.49814 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65e29a9c-8aa4-303f-b85f-e4a4d035143b | -6.60364 | -62.49414 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 170f83cd-06ad-328b-9ccb-8f801a0cc921 | -6.60309 | -62.49762 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c99b7483-705b-3121-af82-04f87747d067 | -7.41686 | -62.98063 | 2024-09-27 05:27:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f475c30c-b364-3a1b-8721-587d70172459 | -9.34861 | -63.80136 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3613df96-f514-3c12-9dd2-df873fce4cd5 | -8.71831 | -62.91306 | 2024-09-27 05:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12b940a7-4a7a-3680-8360-c00c3ef1b7fd | -8.71616 | -63.75488 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94a0699f-ceae-36cd-abfc-7bb0ee1f6208 | -8.69232 | -62.81964 | 2024-09-27 05:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c52cd81-d53e-34a3-8d37-6579df58c407 | -8.63991 | -63.49456 | 2024-09-27 05:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 336363de-eddb-3265-9325-699b8e99bd5d | -8.57804 | -63.09081 | 2024-09-27 05:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f191dea8-4715-3f91-b76b-a59982c9b49d | -8.57226 | -63.74698 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eab8612f-c2ca-388a-a15f-eb7f0182b5e0 | -8.57169 | -63.75056 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b49da4cd-5225-30f3-8410-551b9d600ee1 | -8.57138 | -63.51621 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a917479-e22c-34d3-93a1-ddf8b7e1f037 | -8.53902 | -64.01968 | 2024-09-27 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2838ed7f-0779-356a-93ec-167e620ef03a | -8.51873 | -63.52945 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01a5fb25-97b9-3626-a059-1ba78baae8e1 | -8.51539 | -63.52892 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43b46f50-57d4-3e25-b22e-3504fa5d9ae7 | -8.51096 | -63.51361 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af051ee2-7c77-30af-b472-256a368ba168 | -8.50819 | -63.50953 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4d4fbd8-b7da-3c37-a673-a575cd1dc4f2 | -8.50762 | -63.51308 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13825b44-edcf-3fd0-ae90-b9655f9551e6 | -8.50706 | -63.51664 | 2024-09-27 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README125.md)
