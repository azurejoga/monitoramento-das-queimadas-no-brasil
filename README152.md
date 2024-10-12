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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b53451ef-22cf-3e56-8fb7-a39688c2a245 | -12.78862 | -41.60459 | 2024-10-12 12:23:00 | TERRA_M-T | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| eefbb608-319a-3b13-bb6e-2af79a730b43 | -12.75136 | -40.60123 | 2024-10-12 12:23:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 848ae3fe-df61-3051-a5eb-389a4fa02f4e | -12.74996 | -40.61161 | 2024-10-12 12:23:00 | TERRA_M-T | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| a6742916-e0b0-3bc9-80aa-1ad3a29996a8 | -12.65358 | -41.64964 | 2024-10-12 12:23:00 | TERRA_M-T | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 0f321ff0-ac2b-377c-8afa-d271c792bba2 | -14.39438 | -41.50328 | 2024-10-12 12:23:00 | TERRA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 6fc576cc-3a86-3c6f-b8f8-2b7b3f0d4a61 | -10.50578 | -42.49553 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 0345b314-1269-3e53-a85d-fc9eae01d76e | -10.50448 | -42.50449 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 55f7269f-bce5-383f-9b2b-2501499ac631 | -10.49691 | -42.49425 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 6b609a8d-d72e-3c72-8ace-7c3ff90153a6 | -10.49561 | -42.50321 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 56c1a4b3-ff1d-3048-a0f0-969ffc570255 | -10.21845 | -42.44468 | 2024-10-12 12:23:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 8df482a4-401f-3859-9de2-423b9473eced | -12.3163 | -41.88684 | 2024-10-12 12:23:00 | TERRA_M-T | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 019829ef-b7cb-3e1d-b443-c48183dd1b4c | -12.11221 | -43.17989 | 2024-10-12 12:23:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 45.9 |
| 7f728e96-adda-30ef-afd4-bc4294b8b657 | -11.87454 | -42.91388 | 2024-10-12 12:23:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 26fbbe79-6e6e-3e92-bf13-2a4e38a0adc2 | -11.76178 | -42.54482 | 2024-10-12 12:23:00 | TERRA_M-T | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 327d6f25-1356-3377-83a2-85a6846db87d | -11.71519 | -41.64433 | 2024-10-12 12:23:00 | TERRA_M-T | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 2e165f80-5f41-3d9e-aa7c-f5a88ab75e87 | -11.70965 | -42.59235 | 2024-10-12 12:23:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| cd534e1c-125c-3ee9-9a09-a74dda61719b | -11.69014 | -42.72724 | 2024-10-12 12:23:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 289563fd-240b-3598-8550-731276caa4d2 | -11.68884 | -42.73623 | 2024-10-12 12:23:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 21621157-9f50-3b7d-aae7-93f97f1dad82 | -11.55985 | -42.60409 | 2024-10-12 12:23:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 0413751f-e7a2-3769-94b5-0b7aa9b79ba6 | -11.55855 | -42.61307 | 2024-10-12 12:23:00 | TERRA_M-T | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 2342d9cb-078e-37d5-bd25-275e66ebc8ad | -11.55751 | -41.71951 | 2024-10-12 12:23:00 | TERRA_M-T | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4ecac906-9113-350d-a334-8366a4ddf737 | -11.33443 | -43.07373 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5980c703-7ae5-34ed-bc10-a13e154c029e | -11.22588 | -42.03769 | 2024-10-12 12:23:00 | TERRA_M-T | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c52971b2-e5ee-36b3-9b27-32ad355ec9e2 | -11.03762 | -42.90109 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 58f7b95d-1bfa-3bc4-8eaa-2da94373eec2 | -13.63619 | -42.38535 | 2024-10-12 12:23:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1e3dc271-e85c-340d-8717-3c81c5e28cbc | -12.88369 | -42.43144 | 2024-10-12 12:23:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6b93a0dd-8d2e-307a-8607-61fc99901ecf | -12.61396 | -42.44809 | 2024-10-12 12:23:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 8d7a4d86-64e4-3ad9-a9ff-9c1829151a6b | -12.46241 | -43.18264 | 2024-10-12 12:23:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 32b760b1-427f-3bc3-ac8b-ef523d8b43f2 | -14.23743 | -42.2352 | 2024-10-12 12:23:00 | TERRA_M-T | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5ffae5fc-c271-3a81-aad2-e12344376d6a | -14.18349 | -42.61451 | 2024-10-12 12:23:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8cdcf793-72e9-399c-af98-54ba7def9da4 | -14.05497 | -42.15834 | 2024-10-12 12:23:00 | TERRA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 66.7 |
| d0f26ef5-bd9f-3da9-9dc2-fd361393e91d | -14.05365 | -42.16769 | 2024-10-12 12:23:00 | TERRA_M-T | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 65f32722-0a60-37bb-9996-05f0e823c593 | -13.78025 | -42.99281 | 2024-10-12 12:23:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 3361cf74-ab48-3d33-ae09-41f70706ca85 | -13.77895 | -43.00188 | 2024-10-12 12:23:00 | TERRA_M-T | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| da0e9733-2cd0-33ce-bcc1-0db1ce749439 | -11.36235 | -43.1397 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| ab603571-49f5-3025-bdc5-0157d5c264c0 | -11.36102 | -43.14876 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 3edf7508-7e1a-37f2-9e68-1102f95ca9a8 | -11.33311 | -43.08278 | 2024-10-12 12:23:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 05097272-5879-3a95-863c-7d44f2d266c5 | -12.24487 | -43.59369 | 2024-10-12 12:23:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cd616cd9-7ad3-3dba-a004-06bd88b3cea1 | -12.06809 | -43.48002 | 2024-10-12 12:23:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 29577288-23fe-3f99-9f8e-1478f12b0813 | -11.74233 | -44.48747 | 2024-10-12 12:23:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e1d22baf-2b10-3732-9cd5-6a007ad237d3 | -11.46783 | -43.92056 | 2024-10-12 12:23:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 80785601-1f8e-3905-ab57-b59fa852a690 | -11.46643 | -43.92997 | 2024-10-12 12:23:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5510b387-19ee-3044-bcfc-b6413eea4681 | -13.36802 | -43.79028 | 2024-10-12 12:23:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8bbb0c92-0a15-3a94-b6d8-8a155a7c9dca | -13.03108 | -44.69221 | 2024-10-12 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3706755f-ef19-3de5-9f53-a7e8183b19f5 | -14.07202 | -43.95626 | 2024-10-12 12:23:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dc13bf51-0754-33fa-969a-1a3f78bdbe7b | -12.298 | -45.33484 | 2024-10-12 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3e22fc06-0a3f-3d92-83de-61f9987c45bf | -12.28683 | -45.34385 | 2024-10-12 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 584.4 |
| 18cbd44a-0df4-3473-a869-d2c464d6dd62 | -12.27726 | -45.34229 | 2024-10-12 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 93db8b71-81e5-30e0-b854-ba0ad251087f | -12.27565 | -45.35281 | 2024-10-12 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 3fc8e8be-5745-3d2f-ae00-da6c5be0b83b | -10.95212 | -44.64214 | 2024-10-12 12:23:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f1617b2e-a8cc-3f4f-8b06-327c7f44a4ab | -10.95058 | -44.65223 | 2024-10-12 12:23:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 9f81e62d-13d1-3845-927b-31d9aa89e9d9 | -10.94903 | -44.66234 | 2024-10-12 12:23:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 30cb775f-f1a0-3c3c-bfd8-436c433dca7e | -10.9412 | -44.65079 | 2024-10-12 12:23:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4f59caed-2575-30b4-a9d6-fc5e02fa6e01 | -10.94275 | -44.64071 | 2024-10-12 12:23:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d3e8aa8e-bf2a-32c0-be14-3a5492a11d7e | -10.9506 | -44.653 | 2024-10-12 12:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 16e629b0-0976-3a6d-999f-11365564912e | -10.9315 | -44.6557 | 2024-10-12 12:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a32b33c2-3af6-349c-a370-15e28b97d12d | -10.9506 | -44.653 | 2024-10-12 12:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| fc6f39f1-f9ca-3b2f-a8f2-3ea036ef2a4e | -12.1704 | -50.5861 | 2024-10-12 12:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 6e0541b7-d7a2-3e4f-82b3-f5d6cb73742e | -12.1895 | -50.5838 | 2024-10-12 12:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 26aa3a71-124f-3a70-92a6-c1dec85655b4 | -10.9315 | -44.6557 | 2024-10-12 12:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 48a4f66f-269d-3857-aee9-fedf6a082e66 | -18.21 | -56.56 | 2024-10-12 13:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0230132e-4c23-3205-b29b-8cc0d6fc6688 | -18.18 | -56.54 | 2024-10-12 13:03:43 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 33314382-47ae-325f-8b92-e2a10c361762 | -3.7 | -40.72 | 2024-10-12 13:05:07 | MSG-03 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1be473ed-125c-3508-b1bf-548e94b014ea | -9.9418 | -50.0594 | 2024-10-12 13:06:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 989ef065-eacf-3446-8633-8eed2125f590 | -10.9315 | -44.6557 | 2024-10-12 13:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0c980be8-f243-393d-bfe1-f3e990fa6b63 | -10.8529 | -49.7494 | 2024-10-12 13:06:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b69a73d2-62f7-30fc-87d0-a9735abc7323 | -8.2325 | -61.1823 | 2024-10-12 13:15:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0ec9c9cd-35fb-3d73-a0c1-93c05d8f0beb | -9.9418 | -50.0594 | 2024-10-12 13:16:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 3d626df5-cdd6-334d-a63f-b166c2e46e45 | -10.4925 | -49.8099 | 2024-10-12 13:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 949def14-0ec1-3cd5-8e63-e165b3197c7a | -8.2325 | -61.1823 | 2024-10-12 13:25:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5d2c699a-7612-37e0-bcb7-aa932f136d7a | -9.0179 | -42.9882 | 2024-10-12 13:25:57 | GOES-16 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 5de878e3-100b-3bf3-90ea-7c362f8c2002 | -9.9418 | -50.0594 | 2024-10-12 13:26:03 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 69ff0b44-2e09-3080-b35f-7932ecb2eda3 | -10.5665 | -49.9309 | 2024-10-12 13:26:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 8a5b4ad6-9a6c-3896-a3cc-13aff8106a2c | -10.5473 | -49.9544 | 2024-10-12 13:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| a31e8512-d63e-3678-848d-f13e1bdba7d8 | -10.5476 | -49.9329 | 2024-10-12 13:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7bee610a-2d61-3147-a24f-ca209ae0016d | -10.9502 | -44.6762 | 2024-10-12 13:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 7df073ca-526a-3ea9-b5b6-8e4d8a694b54 | -11.9729 | -51.0575 | 2024-10-12 13:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 821d8529-7642-3191-8037-9873f9cd4eec | -11.9917 | -51.0766 | 2024-10-12 13:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 9d40329b-c278-3705-a657-aca00d891cb1 | -12.011 | -51.0531 | 2024-10-12 13:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 8aed54bf-2db4-35df-a4ad-c169a41dbee3 | -11.992 | -51.0553 | 2024-10-12 13:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| a70e2340-6f7a-337f-ae1c-22010dcf65a4 | -12.1142 | -50.5285 | 2024-10-12 13:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| bfc039ce-3464-34fc-b8b0-a0b79e1655ad | -12.1483 | -59.8816 | 2024-10-12 13:26:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| cb0ac30a-1e0f-32ae-a4c1-1b5c3685f449 | -14.33 | -57.63 | 2024-10-12 14:04:03 | MSG-03 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81f71527-c5f1-3f26-96e5-c34fe9b54340 | -0.803 | -48.6611 | 2024-10-12 14:25:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 17156334-687b-3b5d-8b3d-8dcee412be4f | -1.3927 | -49.2939 | 2024-10-12 14:25:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e39a0906-1e81-3e9e-8390-3b18f3c2e7ed | -2.1692 | -48.8322 | 2024-10-12 14:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 6780c40c-b5d9-3e47-8721-57a1bb3656ce | -3.4169 | -43.3403 | 2024-10-12 14:25:26 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| a173b134-23d1-33ba-91c7-cfd1487134c5 | -8.4383 | -42.4406 | 2024-10-12 14:25:54 | GOES-16 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 382a39e1-da8b-351e-a668-8b30d1f87fe4 | -8.9666 | -62.3696 | 2024-10-12 14:25:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| fe7ece21-b538-3596-8c1c-5740ba92b713 | -8.911 | -62.372 | 2024-10-12 14:25:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fec47c34-3f24-356a-a867-c778f9682a89 | -8.9376 | -64.2406 | 2024-10-12 14:25:58 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 08b08f95-4820-3f44-9871-87b14a4d9b31 | -10.1865 | -42.4291 | 2024-10-12 14:26:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 1aaab93c-22c5-38a7-a373-ef44ebefb1d9 | -10.4078 | -61.2877 | 2024-10-12 14:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 13b835d7-83ff-3d3d-bf67-c068be0355d4 | -10.3891 | -61.2887 | 2024-10-12 14:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d77d47d0-66d4-36ef-95c0-cc1b96fe997f | -11.2446 | -44.2158 | 2024-10-12 14:26:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 3d56837a-ee42-3751-8ad7-c374c27a3643 | -11.2637 | -44.213 | 2024-10-12 14:26:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 70b2e6df-4792-32e2-8ed6-4c40a9955775 | -11.4622 | -50.9021 | 2024-10-12 14:26:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 21de8ca6-bb13-37dd-b0ed-8121c87c0cb8 | -12.1142 | -50.5285 | 2024-10-12 14:26:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 8d101974-b609-3100-b449-b72e876511e1 | -12.3374 | -59.8682 | 2024-10-12 14:26:17 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 7e17e0fb-4fc6-35d4-86fb-39c8ed3b521a | -12.679 | -45.4827 | 2024-10-12 14:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |


[Clique aqui para ver as próximas entradas](README153.md)
