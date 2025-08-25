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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c8271d7-225e-300a-8131-97650198cef0 | -4.66928 | -43.11167 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed4de937-3336-3848-87d4-165eb615d2b8 | -6.02399 | -44.22287 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1db87256-b6d5-3ec7-8abe-7f55364afddf | -4.77655 | -45.32614 | 2025-08-25 04:40:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03482ecc-849b-3270-b374-8596097410e7 | -6.70033 | -44.01388 | 2025-08-25 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c842b193-f71c-39b5-bc61-6d739365e732 | -5.53275 | -41.29039 | 2025-08-25 04:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 29030654-8937-3a10-99e5-76db11550786 | -5.50265 | -41.41722 | 2025-08-25 04:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 01fcba22-36b0-3970-98b1-87498fb03dfd | -3.21366 | -50.5891 | 2025-08-25 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 122b63c8-a531-3e42-9f53-72a3116c8579 | -6.42919 | -44.56021 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29cfb1dc-1766-3343-89ca-3cbdb7714e08 | -5.79837 | -59.22549 | 2025-08-25 04:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d91216-0b77-3966-91cd-e0ec33548652 | -6.22238 | -44.11111 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73b7a322-b868-39a8-8d3a-5a0013174b4b | -5.85995 | -51.74953 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72b2d10c-ba3b-3267-bb8f-2960447b118d | -5.49297 | -41.41552 | 2025-08-25 04:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42ab1a2b-ba4b-3418-9759-089b16ba6885 | -5.88902 | -43.38197 | 2025-08-25 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1ed95e6-15e0-3721-9213-9a7f862f453d | -8.23825 | -45.07997 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b0422a9-c0e5-32ef-82d4-12042e3aa016 | -5.94145 | -44.13909 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e068e57-a4fb-3549-a8f7-2c2968d1d9f3 | -6.03101 | -44.00511 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8c6223d-1c76-3f21-b160-5ad975f5db8d | -0.57619 | -50.43393 | 2025-08-25 04:40:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 894d95f5-d4b9-3f48-bfa1-84e532348ed8 | -6.19172 | -44.12843 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92e0131d-ea2e-3d32-97b0-14ca9407afda | -7.14376 | -44.15388 | 2025-08-25 04:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a0ed8be-73d6-3076-9986-b1966a07e7e6 | -7.47432 | -45.01506 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61160258-fd72-3c33-b003-7bd0791cb9c5 | -6.91445 | -44.41869 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f480c206-b85b-3bfd-b82d-1ceccde5f1c2 | -7.58649 | -45.22924 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 107bc452-cc57-3f20-95b6-2d83d42a9ba6 | -6.32303 | -47.65693 | 2025-08-25 04:40:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 639a02f1-4707-3daa-84ca-7ea112d7e238 | -6.03156 | -44.00133 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee05693b-d214-3da4-9fb0-c0b6e2f5a089 | -6.79618 | -44.32244 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fd61d2c-60a1-32aa-b609-d1b18f03b12d | -5.11049 | -43.21375 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 90468f6d-edb0-3174-80da-94350855ffbc | -6.90329 | -44.40742 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49a50dd2-a5eb-36c2-8b2a-f012bb4078b9 | -6.6811 | -44.42562 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 962f3479-6bc0-340f-8059-700f22d40631 | -7.66471 | -42.66472 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 797e07e5-70b8-33dd-aac3-0f93725a2340 | -5.74959 | -51.7168 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89d60fd9-03e9-3d81-90b6-05d77fc98003 | -6.22185 | -44.11481 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55d076bf-9116-3466-bd84-dc07b0b076b7 | -6.89826 | -47.93073 | 2025-08-25 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30edb4ee-487d-3283-a9a0-ab215234998f | -7.64694 | -44.98081 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eb3d689-ce1e-3947-87df-a4686d08b422 | -6.6776 | -44.42147 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a6549dd-637b-3980-9b2f-47bc82d6b995 | -4.96204 | -55.80828 | 2025-08-25 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebc7325e-e2c0-3571-abb5-911e7c00bee0 | -6.04089 | -43.99486 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db6c16c3-7bc4-394b-9a07-461f9e040c7d | -3.25741 | -46.90572 | 2025-08-25 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6b9a36b-d024-30ef-9411-219cf06ae6c8 | -3.44175 | -49.04566 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c544c588-dd41-3d3f-ad11-cd2d5df5633a | -6.78453 | -44.31696 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15c28bfa-d667-36fb-8183-c469caddd774 | -4.09974 | -47.72553 | 2025-08-25 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696960fe-fea5-32fa-8a1d-e73e9d0589ba | -6.91979 | -43.77597 | 2025-08-25 04:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d17428f2-c764-3da1-b7f8-8a1e857c7a1e | -5.74915 | -57.57862 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b49260bd-b4c8-3faa-a857-ac318b37b31a | -7.66402 | -42.66956 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e88f791-2ac5-3ca3-a851-7ccc93fbbbbc | -7.89231 | -45.89911 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c00f20d-ea48-39b2-855d-3bf07713a249 | -3.43842 | -49.04514 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 67a78b6e-4dbc-31a5-923a-d1f2de4315c7 | -3.59119 | -49.42568 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d958f48e-a624-3e88-8857-4dcb6ab14f21 | -5.71302 | -46.02497 | 2025-08-25 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8e1f04e-74a0-3874-adfd-f25c3f1c4123 | -3.4351 | -49.04462 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c05f8bae-2dc5-313b-903f-278993ff15f4 | -3.98597 | -49.49506 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf90fda1-f46c-3216-9b8d-7d9e24534f07 | -6.53169 | -44.43176 | 2025-08-25 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28715498-cf0e-3774-baf0-229c64a4247a | -7.58826 | -45.24417 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 612d6980-ce54-30e4-a15f-14576a127be4 | -4.29185 | -48.2651 | 2025-08-25 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad2f78ce-8d56-3840-b301-bed17f7ececb | -5.69964 | -45.52049 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c188115-825a-36da-aa9f-32fe4dc43b01 | -6.90505 | -47.93175 | 2025-08-25 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a29509ba-f3d3-3dbf-8d5f-75d45da321a9 | -7.29462 | -44.53282 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85908ec1-6e5f-3623-b3cb-ff7a38d2f4d9 | -7.9055 | -45.88745 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21729dc4-6990-3efe-9a94-e20d1c37840e | -5.79504 | -59.22417 | 2025-08-25 04:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f9c9fad-8a6a-3a0c-b63e-5970ec039e0f | -3.45582 | -43.34164 | 2025-08-25 04:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f928bcc-bc5e-3aaa-821b-9fbdcd6fee45 | -6.06142 | -43.99794 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1a17505-dcb6-3b5a-9e2b-0bd2f7885d5c | -7.73922 | -47.36236 | 2025-08-25 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02cf4da4-d8e8-30a4-a289-7a8cd8ff7c19 | -7.47428 | -45.01746 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd29b2e1-98e4-3ad3-ba1c-f172d17db33e | -2.29391 | -47.97806 | 2025-08-25 04:40:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d121428f-8abd-3c84-be85-31249f9d5e25 | -5.79269 | -59.22456 | 2025-08-25 04:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62299458-5091-3532-a04f-758e3de06fb6 | -6.88091 | -45.65498 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53e4ac12-ab66-34bd-b00a-fd44eb95a3d7 | -5.73845 | -57.57994 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8811b439-f510-32a2-bda4-2249e3c298cf | -6.19068 | -44.13533 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b5f2cc0-0f17-3e5b-8301-7a87baeca461 | -6.88866 | -47.9255 | 2025-08-25 04:40:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb093372-edb5-321a-bcce-53fd97d27f8a | -5.10015 | -42.95504 | 2025-08-25 04:40:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83d6ad9a-ae44-31c8-b338-f4513b2d870e | -7.47354 | -45.02239 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 537dca1e-794f-3bac-9e45-911bd90a27bc | -7.54377 | -46.0205 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 235da061-71fe-3ff0-8d60-adc4e0ed7988 | -6.90988 | -44.41866 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3049111f-a7f8-31d2-87a4-6c2c3ba68888 | -7.50486 | -45.83541 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e0844b4d-9e85-397b-b4f7-de64754a3620 | -3.43068 | -49.05102 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d94bbc37-1e42-3038-a275-8a7960b731ac | -6.87717 | -45.6544 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac6f6289-bd5b-3d3a-b11a-88109c44a251 | -6.03211 | -43.99752 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f753aaed-37b7-3741-b2b1-671ccc48dbb9 | -6.74509 | -50.95592 | 2025-08-25 04:40:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bee47441-992f-387a-99d1-224bcc33e797 | -7.65784 | -45.39868 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e69ac37-d735-3d4c-8c29-89823b440c29 | -5.30211 | -45.26817 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e3f5de7-e6b3-3119-8c18-8cf8c6f23c1f | -4.95971 | -55.82224 | 2025-08-25 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c111236e-20d7-3f64-be33-10f4a14f89cc | -6.25017 | -43.82468 | 2025-08-25 04:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f7f9970-bd79-3615-bca0-669c78a31526 | -6.87092 | -44.40263 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b0ccc4c-a2aa-3fc3-b23b-c0a0b4784188 | -4.66501 | -43.11102 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0df83a25-dff6-36d8-b4f5-f1fd3d68e41d | -3.45995 | -43.34221 | 2025-08-25 04:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8de10482-b08a-360d-a61e-5ec2fbbe6b04 | -7.65873 | -42.67373 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 970af527-1ead-3169-a6bf-9e380b8cac93 | -6.43788 | -44.55655 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88e4745f-6a7b-37bd-809c-6a8e6a770fc5 | -7.33141 | -44.5351 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebd07f63-daf8-3e57-a461-98993d4153cc | -7.59352 | -45.2353 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e3113f7-1cd6-378b-92d4-5a7dfd835338 | -5.55345 | -45.56133 | 2025-08-25 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 745fbc56-3d0b-31d2-93a3-236db4a3640d | -6.45213 | -43.71324 | 2025-08-25 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5cbccab-dfb1-3e43-810d-ff314ac4d650 | -6.65306 | -44.39246 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc835a3d-c2c1-3633-a816-373ced611290 | -5.70883 | -46.02623 | 2025-08-25 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 021476f3-7ffb-3603-968c-1546327f00dc | -6.68212 | -44.41877 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92bcc2ce-3b5d-368c-8f60-c30dd3df1cf2 | -5.63927 | -45.14861 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e012c49-11e2-37fb-94e7-212ecc6b7216 | -7.89671 | -45.89519 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03ead81a-9f49-3809-8fde-e09c4f181038 | -5.74965 | -57.57568 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 140f608e-0f75-3542-a1b1-a7a1c4110ec0 | -5.90306 | -44.08931 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| befed28d-9356-3519-b8a1-811d27f44ef4 | -6.21776 | -44.11426 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88ed29bc-fbfa-3267-845f-2bae9e85cbd1 | -7.29213 | -44.52177 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e69d4dc-b0e2-3346-b726-da64e0708860 | -3.98263 | -49.49453 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80f24755-9351-3c93-9007-e36862883bc8 | -6.794 | -44.33702 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README38.md)
