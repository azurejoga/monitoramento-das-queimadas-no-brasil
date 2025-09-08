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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a8aa55c-24f9-3c5d-a2b1-a148642c1af8 | -9.57127 | -53.59045 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f0e843-87b9-3e58-ad34-16066e700c9c | -6.82271 | -52.80396 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f98a6924-aac3-3e6d-96f6-d206607674eb | -6.30873 | -42.19735 | 2025-09-08 04:51:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 28167d69-1a26-3efc-b8f5-20e50dd1f806 | -7.76869 | -50.76663 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf203f30-1b08-348e-9e9d-677dd4108d2a | -8.93006 | -45.81526 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 38810d25-0c36-3e1d-8e1a-485e7595658f | -6.18164 | -44.73936 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 504703c7-2a0d-37b2-a84a-7455db57e9de | -9.05247 | -50.46331 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f7cb6bc-a159-3630-832f-87fd1ad6e1b6 | -6.38982 | -44.46419 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0274cb93-041c-3117-9b6c-72c7e1861bb4 | -8.04239 | -44.06314 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9be2684f-973e-3106-bc35-8c803765a0bb | -6.15661 | -53.68698 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a555e9e-de3c-30e0-b19b-5aa429363c22 | -3.3268 | -54.90955 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 353af1d2-650f-390f-a49d-c6202ce6ed9f | -9.82637 | -47.77061 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7b7786a-d646-32a7-8530-d4c4a06bb953 | -10.46347 | -53.62695 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cefd18c-bb62-356c-8b4e-120effa1cfd8 | -9.24911 | -57.06474 | 2025-09-08 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a05709e-dcd1-36b4-95c7-72365a2e5e83 | -5.58768 | -51.91196 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d2e987f-eb4d-3889-bdc9-80cbf62bfc78 | -11.2816 | -46.46405 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af7c4f13-c67a-3c00-a206-5ed7ea51a185 | -10.17991 | -46.2325 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acd20218-da46-3eba-8c0a-50ae818b73df | -10.0039 | -51.63402 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ececac9-48f2-3323-ac99-a10854621ab5 | -10.46017 | -53.62643 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69427ae2-3521-396b-9fd7-565962fc7ffd | -6.38386 | -42.61033 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b79eb3e-e24d-329b-bbff-623c16359d0b | -6.54749 | -54.9889 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8f0bf43-193d-3c52-af89-41339ec4f9a4 | -7.22265 | -46.20517 | 2025-09-08 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd8c00ff-5399-3793-96e0-dcfaf4a35734 | -8.89232 | -52.04602 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99b3398c-1d64-3919-a8bd-af9733c6a740 | -11.28701 | -46.45938 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1db8036e-dc53-36a4-916c-8f284ec9b120 | -6.26557 | -43.69583 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72bb1047-1875-3290-ae53-48f590fd6b25 | -9.55154 | -53.58366 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ca00e53-d94f-3f1f-865c-b41f32569fbc | -8.19748 | -47.5613 | 2025-09-08 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e7f832e-450d-3796-95e5-24ce670f7140 | -9.17148 | -59.37673 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d25882cf-71f6-358d-b5b6-cb1068f762ab | -5.85739 | -43.85416 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 522cbd7f-046d-3704-a66a-88816f6eb0e0 | -5.73954 | -45.3646 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75ca84ab-292e-3352-a26d-9f0954beee5a | -9.98293 | -51.68075 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8c65614-2341-324a-a011-30d752656689 | -5.94792 | -46.16321 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c4619d0-223c-3696-88ea-482dc9a8f42f | -6.88435 | -44.25854 | 2025-09-08 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66086f86-24d8-3aff-a742-94a10a897e66 | -8.86259 | -47.24436 | 2025-09-08 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9cb82cd-ee91-3bff-bcac-6fd49177ce44 | -6.87069 | -47.91466 | 2025-09-08 04:51:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| af34c653-6f83-34ae-9983-35f8582fbedd | -8.62453 | -40.20143 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5c8ef4bd-5d12-3763-983a-9a782235b301 | -5.4173 | -42.85762 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6c2df455-0c08-3ac3-a718-b9a4ef7c2dd5 | -7.99389 | -46.34985 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 855c739e-9507-354c-af87-14daedbbb89b | -6.62588 | -53.36442 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2002b14f-db81-3a10-bfd7-8bc213ff61ce | -7.83555 | -52.15157 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d192374-bf23-395b-966d-51def37c9eef | -6.19598 | -40.97295 | 2025-09-08 04:51:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 859feec9-cb05-34b1-b1e0-8d011c3537d4 | -6.30814 | -42.20163 | 2025-09-08 04:51:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 817474ec-5914-3f38-8d50-ecc1dc605e1a | -9.85389 | -48.85275 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e84a9c51-b510-3eb3-917a-a1136ab32886 | -6.47458 | -44.00581 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 06d1ba6e-85d6-3f09-a40f-885028c522f8 | -7.67894 | -50.25642 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a1f2202-a71a-3833-8eb3-699ad5e723e4 | -6.81503 | -52.80983 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f567bf71-b322-3c49-8eda-95e52fc1ff0e | -5.44947 | -43.43591 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2540d6e8-c8c0-3313-8198-9dc40c976347 | -5.85831 | -43.84767 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36e0d791-c1e2-3369-b0fe-bd22869638c1 | -9.99879 | -51.64475 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67f494ab-b0b4-3547-81a2-57482c55bb4c | -10.07891 | -48.10136 | 2025-09-08 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e362063-86df-31ec-b265-82bd2ecd5a00 | -6.27215 | -43.68724 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2f904e0-8242-3674-a137-89a9dc08f178 | -11.42272 | -43.63621 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c878e829-5623-3a19-9196-75dc4d60024b | -9.95944 | -51.2034 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| da746e10-6dcb-3670-8583-c39ddc37c800 | -10.47389 | -53.60359 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a123887-270a-339f-884a-0e10e44de76f | -7.81471 | -52.13396 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e1be76b-00de-3824-85e5-563d4eb95df0 | -5.22018 | -43.28543 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab4343c7-e42f-34a4-aefb-9272bfd61bdc | -6.84029 | -52.79964 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e9d2125-6586-3d53-b2e0-127508bad4bc | -8.04284 | -44.05978 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fbb5b0f-c585-31b2-b000-79cd330e213a | -5.8764 | -43.95694 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b605283-2b8b-3d28-951d-ed5cde4bfd0f | -7.35712 | -43.94392 | 2025-09-08 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d480436-3bc5-30a0-9365-242e6ae75791 | -8.19908 | -50.14331 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 930bc3ac-e34b-3050-b40f-2c8e44abec84 | -10.78213 | -47.72434 | 2025-09-08 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72e40680-bc4c-3c59-9f56-f907e0cb5f63 | -6.82655 | -52.80103 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61e15455-5bf4-34a9-8be6-5e330efea561 | -5.88027 | -43.96725 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ca2be65-70be-38fe-9cda-b49e428c1127 | -5.99387 | -44.1489 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c629a0e7-502c-39ea-8c53-4382b171ebe2 | -10.00048 | -51.63349 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1843fac-ba03-39c6-b9a7-9674808ad1f7 | -6.8203 | -51.8788 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d5591a1-3e55-3ef9-ba5a-bc58b41f9081 | -5.86393 | -43.84547 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2000da69-2ef8-3686-8073-51c4b4e3c7e7 | -5.89744 | -53.841 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e76b2528-adc1-3095-855d-546439efc65b | -5.95123 | -45.75117 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 256b6ed9-3bf6-3aec-ba64-b75388cdffed | -6.39467 | -43.81086 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55577ce9-aea1-38f7-a0ea-bf09306f78e5 | -9.99312 | -51.65932 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdb29c68-c460-3781-823f-7137f6d8cbbb | -11.02101 | -46.0299 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 32a810fe-2bcb-36f9-8a06-afa1bf038bd4 | -6.17752 | -44.73302 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78bf9253-dfa8-3fcd-b847-232d84b45728 | -5.99976 | -47.60969 | 2025-09-08 04:51:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b061f594-98c9-33cf-a985-4aac1fae2710 | -11.3208 | -47.38775 | 2025-09-08 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b35d16bb-e9ff-3280-aae0-a5a55b8d6d9b | -9.98856 | -51.66643 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 207d69c2-3852-33fd-a44b-eb644cb31549 | -9.98914 | -51.66259 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 133dcca4-d5d6-3097-9b34-03da28c5dbc5 | -6.60357 | -44.00342 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9787de9-e748-36f8-a077-d396eec9ea96 | -9.96058 | -51.19575 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f32da697-e517-300b-8ad7-2feaf469330f | -7.08406 | -43.90051 | 2025-09-08 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 343c1d76-1ca9-346c-8762-c36ff27c5220 | -8.70186 | -45.31005 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eea1f174-e477-3c8a-81a3-75d1f99ea40c | -7.43762 | -45.2204 | 2025-09-08 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 870e0e75-c4a9-31fc-8cac-0f1303713d07 | -9.82101 | -53.32052 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56fc7ede-e45b-3c02-8ba4-cd2698b3a064 | -5.21802 | -43.28408 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c32d9fd6-8c8b-380d-abb2-d3639f78688e | -9.85527 | -48.84297 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fa9d3265-2ba3-3ac7-833e-413b575eb2ff | -7.29205 | -44.14566 | 2025-09-08 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b059a515-df21-3b0a-a6d2-d58a55863426 | -3.20698 | -54.95685 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5d7a122-8b5b-3ccc-81c4-b0cb879646f0 | -9.71765 | -43.98266 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5ae1d79-f37e-385d-b500-bec82c6579e6 | -6.69881 | -52.09312 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 615a19f9-39e0-32f4-998d-ffd4f1dca129 | -10.96403 | -46.81698 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4ef7889-ec3d-35e3-84cc-f5c34e5acf1b | -7.29766 | -44.14343 | 2025-09-08 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3871f37a-d47a-3bfe-bc48-c017781cf813 | -9.48375 | -55.97468 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9c6df3d-b65a-3f99-9d85-7668e3784aee | -9.85594 | -48.83818 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb3878a9-8b68-3f6a-9227-c1a34874e883 | -7.6363 | -46.55651 | 2025-09-08 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 027e2fd7-d244-3d95-94bc-1a408cbf94b2 | -7.81804 | -52.13448 | 2025-09-08 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7626c62-ef73-3dae-8203-fdd336793ed1 | -11.01904 | -45.93076 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2bbfa97-7508-3fe1-9edf-0ec188298f57 | -9.87496 | -46.53197 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e3abf55-3220-3c37-b1fa-6c6e6c11f174 | -4.48451 | -48.11855 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8e85263-a856-3781-9aca-1208bc18ea52 | -11.03579 | -45.9543 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |


[Clique aqui para ver as próximas entradas](README54.md)
