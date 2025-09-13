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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57a3baed-18f6-36e5-926a-cd358e532910 | -9.2653 | -59.41292 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 40855327-4fa5-3abe-8533-240d566a8e6b | -11.58761 | -50.57347 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 93094819-c2c1-310e-bfdf-ef4771e6f9b9 | -11.14066 | -50.72299 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d772f749-5783-318a-8cee-f2d70fb98d39 | -9.69034 | -59.21539 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e21be07-7a7c-36f4-896d-fbfc017fd768 | -11.11731 | -51.33448 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 05c8b0e9-ac93-3cea-b6f3-113d0619dbcd | -10.10222 | -59.16242 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa11ae81-b8dd-38c6-9613-3984023b08e2 | -10.38083 | -50.49409 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 966ec221-3d83-37f5-a34e-61829a10ea0e | -9.72227 | -64.92996 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f27def6-3fd0-3e2b-b86a-98601b73842e | -10.00581 | -59.97283 | 2025-09-13 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2fb2516-fa1a-39a7-8260-30ebe67838a5 | -11.84662 | -50.58596 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1fc7ea4-5355-3876-8b8d-18d0dea79649 | -11.09882 | -51.43288 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9e3c2719-1864-3f11-8af8-8381ca4ef5cd | -7.86357 | -61.16905 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08ffadc2-8abc-39b1-8205-10b1cd8e164c | -9.26244 | -59.40866 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2cc1294-6a8a-375e-89fc-c193361358c2 | -9.79654 | -61.51828 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 008e28ff-ed02-39d8-a05e-43c173a19064 | -11.0119 | -51.33696 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12765355-4ca9-392c-b07d-fb8c831c89f7 | -11.41904 | -50.74329 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 276b4bc4-2b56-30b5-a801-fc0e15cdbea4 | -11.89185 | -50.57663 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 3c8f222e-153a-32a2-8365-2b01e127dc8e | -10.34069 | -48.81343 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6eea9c2-a1d5-3e1d-932d-902a8119e2dd | -9.25902 | -59.40815 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4cc91edd-d2c0-339f-889b-520dabcc2f87 | -11.99777 | -47.7574 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 16eced51-5d40-3277-a8db-67dd852e956e | -10.40107 | -60.81861 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13613ca7-1219-3c25-a34f-14e5a125b347 | -11.87465 | -50.56507 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 282987f6-1a32-32f0-a302-ea4dbaee441a | -3.44091 | -59.5713 | 2025-09-13 05:25:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 80a91927-9d9f-3c67-8b85-4b9a6654f7ac | -10.78595 | -50.5355 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a95b6181-f67e-34da-8c2b-41271ba7ffb3 | -11.18804 | -51.43098 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33501466-9497-393d-b979-92833ed8d276 | -9.2331 | -51.25172 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8885e086-58a3-36f7-a568-e1cdb2c6d361 | -10.78541 | -50.53999 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71d14572-3416-3703-831b-c3afc7f96072 | -9.73983 | -65.01443 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31ec861f-622e-3d8c-b8ab-430c254276f0 | -11.37513 | -47.32523 | 2025-09-13 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 54aec010-fc5b-32ae-87e5-e478f2894238 | -10.50706 | -51.55603 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 083998f8-a62f-385f-94e5-43805fc4133e | -9.05499 | -47.0376 | 2025-09-13 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 187ef4e9-2628-385e-a39c-14ac77473c38 | -9.25047 | -51.25042 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd349361-9a7e-35e8-8629-7eba728fea90 | -9.27042 | -59.4023 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 84f6ac84-0e2b-347e-a097-fddb65573e49 | -11.10352 | -51.44147 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4d96c547-d474-353c-9b15-d1be992eab1b | -11.58154 | -50.57269 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 4d3fd9d5-d871-3488-8db6-448aa1fdc6a1 | -9.26417 | -59.42035 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f10ddf9e-b84c-3181-b651-3b65bf221d66 | -9.23039 | -51.22814 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fa06175-f373-3ae8-affa-3634de80cfef | -11.11192 | -51.34018 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3a5b683b-32db-3548-8605-827104b6df8a | -10.7007 | -54.44667 | 2025-09-13 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5584a7d7-1aba-3e7c-9c69-0fe3e251d542 | -9.27784 | -59.39964 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d874aa64-2a68-316c-a892-a092580ce3d3 | -9.95916 | -50.39035 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca331ec6-fce1-38cd-9c9c-84d05e095834 | -7.54018 | -52.51508 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29ee425d-e9f7-3538-8e36-f76b94559ead | -4.92798 | -55.77832 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c836fe97-1e9c-352e-b0fb-5e9c95bb42bf | -11.98975 | -47.76387 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c181f4f4-b759-3157-b48a-ac540da98c47 | -9.27613 | -59.4108 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9601cc8a-298f-3413-a5b0-e23507b4467b | -7.86024 | -61.16852 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18663401-0d17-353c-805c-ba08fbc8f787 | -5.29164 | -60.10302 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e95fecf-fdcc-30a9-a8b7-03a424dae3f0 | 0.67267 | -50.66631 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d82194-ddaf-3609-8755-58b2f2ceb764 | -10.52936 | -49.87077 | 2025-09-13 05:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a02c87ea-d5a8-398b-9f8b-ddd5476317a5 | -11.108 | -51.42047 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d62c8d34-fbd6-3cd7-8ba8-393e6e7c1c83 | -11.09417 | -51.43869 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 535ee9d7-b3bc-3e25-8fc0-13eebc5a3b26 | -10.33648 | -54.31573 | 2025-09-13 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51c59d73-8a63-3fda-8037-0c6943b70167 | -9.79768 | -59.10283 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6adc09b6-bf94-3a6e-9fc2-8fd76c67af93 | -11.1793 | -55.06921 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a74b4bd6-0157-3d26-a99d-3299ac592aac | -9.13658 | -60.53642 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ad4f4f6-d57c-3846-b6e7-01304c855e21 | -10.01389 | -50.393 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24e86026-9af2-381e-8d07-04809709f26a | -3.86267 | -61.20602 | 2025-09-13 05:25:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc53cf41-eecf-3591-a2ef-f6a3e37e30fb | -11.58099 | -50.57726 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 6c34826e-7925-386c-b327-3a87bc334425 | -11.33837 | -50.78493 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3220c9be-875f-3ea2-b457-3fabc1ac4ac9 | -9.28012 | -59.40762 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fe04936-51c3-3982-9c34-ccd9cdc16658 | -9.267 | -59.40176 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e2a73f43-7450-3f0a-bce8-fec72c1c161d | -3.90809 | -59.65169 | 2025-09-13 05:25:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| feb9f5bf-54b7-3c9a-9395-c1cb6c212eea | -11.19527 | -51.41985 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 404b2d88-559b-38b2-879d-c841ad3a05c9 | -11.11815 | -51.33694 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 5e483c00-3a1a-35d7-a334-6ebadc45518c | -8.54091 | -63.99657 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aa16b43-82d7-360a-ae05-6dfd462e1daa | -11.14392 | -50.69651 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.8 |
| de02e830-2524-3f02-8abb-3c8553ce9fa0 | 2.8982 | -60.26945 | 2025-09-13 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e492fd2-e46f-3c26-bd7e-e592dc1ca29c | -6.90671 | -49.41224 | 2025-09-13 05:25:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d692e9a3-5e2a-3bb3-8023-554d9b72bf5e | -11.08418 | -51.42535 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 950a9307-4b13-3443-9210-3702738b23c7 | -10.32835 | -58.02425 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 096af61f-a111-3623-b1d7-21455bb6f698 | -9.24048 | -60.41167 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 916e16c9-0a85-35b3-b6b6-88890a0e4d3f | -7.66621 | -61.16978 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2880b646-8ff6-30fd-9394-d8d7d61c663a | -9.26075 | -59.41981 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bae7f73d-1329-3038-aa03-13d4ddcda9dc | -9.82651 | -62.33156 | 2025-09-13 05:25:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 274e75cb-da73-3fe8-96f3-5e79dad05499 | -9.27841 | -59.3959 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc821411-47f8-33c4-aaf8-553b797b8305 | -8.26935 | -64.05721 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37f1faba-6a81-3cb1-aa7c-6f9d46270d92 | -11.06082 | -51.50361 | 2025-09-13 05:25:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb892bb5-8ddd-3dde-81fb-0d718e98b4b3 | -9.8032 | -61.51935 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83ce3d32-ea28-351a-a02e-d7a629bf7b1a | -7.66461 | -61.12318 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5632f2e7-48a2-37b9-bc84-99a04c7bcc00 | -10.50843 | -51.54527 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfee4245-011a-3205-9f9f-bc504a7b105a | -9.27099 | -59.39857 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4fa9958-4f21-347e-a2f5-379837e5db3a | -10.33702 | -48.81984 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4441b7f-d0b9-3df7-b32e-19356d0ca883 | -11.07847 | -51.42459 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d1b320a5-eac5-37ce-b99f-3da1ed9a72d3 | -10.40217 | -60.81156 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc9c9ad1-f46a-3881-9304-11e1d985948e | -9.29259 | -60.18707 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a28342ef-5edc-3b43-9d0f-1ca071e26044 | -9.72673 | -64.92617 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27a284d3-902a-3c4e-8958-17efdfe88a6d | -9.79421 | -59.10228 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3da04eb5-e9b3-3a7d-93a1-bc6ae6fb9ad0 | -11.87301 | -50.57896 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f89e39ef-e8ca-3a3a-83bf-28ea11a221e5 | -9.79377 | -61.51423 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a9b2d7e-20e2-3f8f-bcaa-04c74e78c066 | -8.27726 | -64.05424 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 359c9636-7ef0-3eda-8edd-051649cd26b2 | -9.21721 | -59.56818 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 154df85f-bd59-3521-a1bb-a4d1a6b4edb0 | -7.90963 | -55.26714 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e042b4d7-db8a-3933-9e07-4f38d315f369 | -11.10132 | -51.42763 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd771873-919a-3dd8-a104-7e3689a46d48 | -9.91132 | -51.88509 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6ed8b7f-f06f-3b08-b6b8-64af27bdfc57 | -9.23874 | -51.25249 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| fb9c3b83-caff-3731-9563-20b38f0e46ad | -9.7424 | -65.01626 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f2ab0bc-badc-3351-9ce0-19b6f6c1c9fe | -9.48899 | -55.97036 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa865929-072d-361b-9092-0973d1c0fa3a | -11.09989 | -51.43944 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7a9d7f6f-1d8b-33a8-bcad-6433462000e6 | -9.23748 | -51.21774 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcbf408d-6617-3567-ab56-c38434f7ddf8 | -9.52174 | -54.62687 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |


[Clique aqui para ver as próximas entradas](README104.md)
