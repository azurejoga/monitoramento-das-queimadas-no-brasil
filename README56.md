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
| d7f09946-fab2-338d-8b55-1d021a4ad4a6 | -7.96983 | -63.07364 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d44a12f-b15f-381f-bdfd-16a72656d762 | -9.19927 | -60.77359 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e24b35a7-ddc2-3250-b78f-46debd50e59a | -11.2868 | -44.97596 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f380bf5-5153-3dec-8638-dcdd89c46cb4 | -7.43383 | -60.62403 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a64b6da2-3437-3f6c-9cce-90ebb6094cb9 | -8.6307 | -63.65238 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7be75f-231b-3d1f-aa45-df7b0db8a397 | -9.15827 | -59.49269 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f31464c-6f7b-371c-852b-2e4429efcdb2 | -8.134 | -62.8604 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8ec8e85-5363-3485-b56b-02c98c507dae | -11.31966 | -47.8542 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b7d64e0-648a-3505-9bc3-f6a5f28a2264 | -8.61271 | -62.60241 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 53fef248-9e6f-3a0a-9224-1a7db9c618c0 | -6.56156 | -60.05967 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f18e93fb-6e74-3c5c-9b37-d02f614bdbf4 | -9.14383 | -60.78493 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2ac3270-b49d-3c35-904f-823f1fad17f4 | -5.80805 | -59.21506 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19d650b1-2322-39b1-a461-2506d8e8dadb | -5.79982 | -59.21374 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef65655e-f178-3488-bbe0-8daf37c9d9de | -5.6097 | -60.23899 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c142bf22-10b2-3b2d-a310-1856cbe985f6 | -10.80529 | -46.41605 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be2053d6-5bfb-3072-a5b6-3036a8b9d633 | -6.57106 | -59.87163 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73e78775-afb3-3b18-83ce-ba6de1a660ee | -9.20215 | -60.78258 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a853bb5d-60b3-3d90-b6f1-b410c5d3b8c5 | -7.43749 | -60.62914 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84ecdaeb-3635-3daf-afab-4b30660cf996 | -9.15465 | -59.4655 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 01ad855a-cec7-3e60-8b1d-cd8e24ea0273 | -10.40914 | -47.17043 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2aed2c7-60d7-3deb-bc00-9a99f5ccdec4 | -7.55369 | -63.85769 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95b891a1-e7ab-35b3-9fcd-89e201b4a167 | -8.13797 | -62.86723 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c8c03a0-fcce-3f78-93dd-4254b319bf8b | -6.31075 | -59.8748 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 979894d9-368e-3199-a152-77f138ce0d18 | -10.29618 | -46.75299 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e558fecd-536d-3927-9757-006f6c9d60f7 | -8.13442 | -62.87083 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75a2cc4b-62d2-3bf3-b162-59da72e4b2cf | -6.91763 | -62.9122 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf84bf7e-c4ea-376e-9400-b0dce861d618 | -9.16308 | -59.47462 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8bda79ca-3033-3e27-9849-4456d955f234 | -8.92317 | -62.44177 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4718d52c-966b-35c9-95dc-60312db01b09 | -7.80719 | -63.5563 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db111791-deb8-3fb7-a0d3-bb141178d00b | -9.16257 | -59.50104 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e103efa9-3913-3f39-b8f9-62fac2ad5885 | -10.80968 | -46.40941 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad64a65c-3c4e-392a-9aea-e90c8091e518 | -11.11608 | -44.78649 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 905294c6-6aba-370a-a798-61ffce3ff73a | -8.06829 | -49.65485 | 2025-08-24 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3120c06-1ae9-3b85-bd14-ed2801f46f74 | -7.80506 | -63.5532 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10069d4a-48c3-3997-955d-c4173013045b | -9.15429 | -59.59581 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2729ae8-cde1-39e9-8dab-1c640dc797a3 | -9.16705 | -59.47532 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4e36d40f-8758-3965-807a-ca6edd26352c | -9.1631 | -59.48823 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3f02f94d-1a0d-3219-878c-1b86bf4fc2d7 | -6.62827 | -58.54571 | 2025-08-24 04:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf02b8c9-3c48-3644-9a0e-a76ef1e4a569 | -8.23269 | -47.46129 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e990474a-fc07-3b3c-a80b-3353e099c082 | -11.32969 | -47.85098 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39de144b-d38a-3dd9-8b01-e2fc9a3fb926 | -9.20071 | -60.79081 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81f5348f-7aec-3029-a1fb-a11b13a64e56 | -8.88536 | -62.40162 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0df736b2-3be8-3074-af17-21fb4f03305e | -10.81235 | -46.3894 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aec73d17-adef-33e6-96e7-d1947c5b2f3e | -9.14937 | -59.48289 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d0b762cb-a2f0-339b-a2e7-6369e987bb59 | -11.31572 | -47.84766 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb7550c5-a9b2-3c92-a4fa-e69d20370307 | -10.80877 | -46.41619 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95c178a2-ff83-34fb-9816-9a6d156abffd | -7.78727 | -61.57106 | 2025-08-24 04:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f745810-0f0e-3815-90b8-b059764633f6 | -9.13826 | -60.78551 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c854a6f7-7441-37e5-aa28-caefe7c355cf | -6.74791 | -62.87173 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82c20c7e-7905-350c-9cf7-b3376de328b4 | -9.16344 | -59.46178 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f474330c-d94b-3df9-9556-35291ad430c6 | -8.18413 | -45.10614 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a414435-c67f-3476-9a8c-82f198c91213 | -9.17013 | -59.48113 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| eaf05a6e-5ea7-3b73-9e3d-f32cd33b9c39 | -10.54502 | -47.14006 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d60d41f-e8dc-35ed-8a9d-6d1a1085f378 | -9.17191 | -59.47089 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 868a197e-08fa-3ae6-874f-f31f5a9082bc | -10.80716 | -46.38879 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 219f7b20-0f33-3898-a298-cfc5ecdb56f4 | -8.12453 | -47.14608 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63f93d2a-aeaa-34c0-9f2e-6b61e5a3effc | -10.40843 | -47.17588 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef549207-ba13-3e93-9daf-8fb7c8be99c0 | -11.13454 | -46.33273 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a176f42-16fb-395a-b68d-a8216f564487 | -8.13947 | -62.87177 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ebc32a3-94d8-30f7-b6c5-ae62ad10ab7f | -9.15032 | -59.49131 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d7e1180f-68ed-3410-a768-c5dbae5ec1f9 | -9.15244 | -59.48874 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d89cebf4-46a3-3933-be5c-dde30c00defc | -9.24852 | -59.63027 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acaeb632-0f96-3215-8152-421aea26c725 | -9.20862 | -60.79652 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e74dc0e-0d98-3448-a7b4-ab614d09de82 | -11.13988 | -46.33152 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cff2e531-4f3e-310c-8c77-21c77154f620 | -11.1165 | -44.78521 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e4c6f07-4511-37c1-b816-d7b59b33aeb6 | -8.06906 | -49.6496 | 2025-08-24 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd27e66c-23a5-3fae-8cc2-f8fb28a4c3a4 | -8.68612 | -62.88067 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fecc5520-5455-3dbf-b3d4-92a0a1a4e3d0 | -8.7119 | -51.13602 | 2025-08-24 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 584b8774-fa87-3455-a969-1a65bfddb546 | -8.11103 | -47.13925 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e0d8f6c-b045-39f9-b24d-2811cf8554f2 | -9.16228 | -59.5972 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69f7609f-2585-3d97-a1cd-225cf8140f44 | -8.60947 | -62.58812 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1b93f220-2120-38c8-a8c1-b69ff7d2c598 | -10.54429 | -47.14553 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3edb7b9-082d-3783-9454-4b6d963739c5 | -10.6458 | -50.11663 | 2025-08-24 04:59:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f1b02e3-6104-367e-b413-18a71f98fce5 | -8.90763 | -62.41675 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aeac4577-080a-3bda-bff6-a0bdb8a6fa32 | -9.17247 | -59.60971 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f7622c1-3090-38ec-8ca5-71241bd1fce8 | -9.5751 | -55.35789 | 2025-08-24 04:59:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 7978fb42-851e-3ea2-a3ba-0e998bda9f54 | -9.12558 | -60.32965 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33a1a937-e6eb-37de-8b03-f4f4946fa8ce | -7.91549 | -63.05081 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cd43f57-14ee-37c7-85cb-3990c0491f0c | -6.68627 | -58.86463 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f8ea7b5-4871-33ac-9d46-4ad9ce8d3df8 | -6.58378 | -59.87381 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e23f26d-eb2c-36b4-8020-1bddb10c09ba | -9.15462 | -59.49966 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b753006c-51ca-33e2-8e10-2254b7dfafe6 | -10.60277 | -44.32787 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bc6fd77a-e3c7-38ba-98fb-c52c80ac1cb0 | -9.15155 | -59.49385 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa673282-f699-3c9e-accc-dd885e39e60f | -10.40633 | -47.19194 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2160474e-5a81-376e-9cb5-c0b056b5e4c2 | -11.32434 | -47.85511 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49a68f02-18ff-321f-abaf-a6bae73f29ea | -7.50703 | -63.83517 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3196eaf2-3a29-30b3-b2d8-05ff8dc9b3d4 | -6.56586 | -60.06037 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 597c7b15-81a5-3a74-aceb-74698d2be89c | -7.55082 | -63.84252 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27b4b14e-a58c-3414-b809-547402b4e4b9 | -8.36895 | -49.29739 | 2025-08-24 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b316395c-6d60-3be5-a3bd-7339dc1d1ee2 | -9.16138 | -59.49852 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b63b8c7d-767f-34bc-9d29-3d3de83537c4 | -9.24508 | -60.48664 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72970d36-cb5f-3d3b-9e20-b674cd527923 | -10.5499 | -47.14084 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2141dece-9d61-3c8a-abae-474a1e5d966a | -9.15637 | -59.4553 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 72e2ce9b-b25a-3098-9cec-c9888006456b | -9.17548 | -60.80756 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 821f1103-7bb9-3fb5-b545-3a75a5697ac8 | -8.87853 | -62.43919 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d375a0a3-8c56-3be5-9d0b-f1fa48b01ed3 | -10.74964 | -49.57999 | 2025-08-24 04:59:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 483ddc5f-8f73-3fbb-ae65-399b8c20415f | -7.80789 | -46.62512 | 2025-08-24 04:59:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c3d6c4f-097f-3378-ab47-4db87b5b94dc | -10.80533 | -46.40257 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0339289e-2bb2-3909-8b24-74567369c3bd | -7.55304 | -63.86124 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 69bbf824-8c19-3a26-b204-bb52d47a2ad5 | -7.94686 | -63.05353 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README57.md)
