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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdf97155-151a-3e33-ac5c-febf822f0f4d | -3.587 | -53.778301 | 2024-10-28 00:49:39 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2112d32a-29b5-3b39-97cd-9db72c1f2b55 | -2.3843 | -48.537899 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a767c136-6eb8-3976-9600-9b8e20441549 | -2.3859 | -48.5448 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99ed080e-d9bf-3fa0-98d9-eab29582d469 | -2.3939 | -48.5793 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 003c253a-de20-358f-8e39-dda42f74fb4e | -3.4598 | -46.319401 | 2024-10-28 00:49:40 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c83f60e2-1399-3f48-97a5-f8878eef212e | -3.4616 | -46.3274 | 2024-10-28 00:49:40 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90d1f548-8169-3f71-928f-4bcd9272e412 | -3.3374 | -45.8825 | 2024-10-28 00:49:40 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3fb632c-5323-3046-868e-45b09bd8469c | -3.3394 | -45.8909 | 2024-10-28 00:49:40 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21b94296-ffa0-356b-9b80-ac82e798d87b | -3.9119 | -48.361599 | 2024-10-28 00:49:40 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa1ed8fd-fe74-34dd-9aa7-f0e013fd4b74 | -3.9135 | -48.3685 | 2024-10-28 00:49:40 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40164a5a-4cc6-3ae3-96b2-1653b8a6a164 | -2.3101 | -48.394199 | 2024-10-28 00:49:40 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9d1e09c-1c9f-3a5d-a314-a2359962f29a | -2.4728 | -49.101799 | 2024-10-28 00:49:40 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d0dc8e0-2ca5-34cc-8581-96b6361b6333 | -2.3401 | -48.569599 | 2024-10-28 00:49:40 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e377a689-0f8b-39a1-be18-79f3bd8bc98e | -2.3417 | -48.5765 | 2024-10-28 00:49:40 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc4ebfe-937d-322a-a81c-5a34e2b107c0 | -3.417 | -46.312302 | 2024-10-28 00:49:41 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9e79dd3-6ff6-3372-8deb-fea8a589b265 | -3.4188 | -46.320301 | 2024-10-28 00:49:41 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9c3c820-20bc-38d6-ae51-e570d183e327 | -3.4053 | -46.306599 | 2024-10-28 00:49:41 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c655707-61d1-33d4-92fe-3e3a6ccdff78 | -3.4072 | -46.314602 | 2024-10-28 00:49:41 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53e88b46-6215-3dbf-beb9-6e37edc3b12e | -3.409 | -46.322601 | 2024-10-28 00:49:41 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d580cdce-8e2c-3b3f-b65a-e4e139b42b35 | -4.4785 | -50.979099 | 2024-10-28 00:49:41 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3bb23f0-db65-3a4d-9aa5-48dee262bf0a | -4.4802 | -50.986599 | 2024-10-28 00:49:41 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59bc8050-39c9-3caf-a471-19397fb1b29a | -4.4818 | -50.993999 | 2024-10-28 00:49:41 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cda1844c-cb3f-3dde-8a89-754d5584aa8f | -3.6133 | -47.247002 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b87c04cd-0829-3f7c-b0da-7f6a5e36d017 | -3.615 | -47.254299 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15d753d6-5007-3ac1-9080-04416cc45566 | -3.6167 | -47.2616 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d577e55-d0a8-3d86-8ee0-9df0bd0e3bc5 | -3.6184 | -47.268902 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d45b3b9-8eaa-3514-ba65-4c9ab061a12a | -4.4704 | -50.9888 | 2024-10-28 00:49:41 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbc45d29-fa64-36d3-b375-1d026d895b94 | -3.395 | -46.350899 | 2024-10-28 00:49:41 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e98c43bb-b50e-37a4-9d9b-082c8ec7c1fb | -3.6069 | -47.263901 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4efcf780-cb57-39c6-a733-f1c80160c61e | -3.6086 | -47.271198 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd28562e-dcca-3744-b8a6-24a9a1638591 | -3.6103 | -47.2785 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 634d4db3-56fc-3e22-bbf2-e4f18baabb1a | -3.612 | -47.285801 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c17caa-54ce-3130-b2b4-267c96859143 | -3.5971 | -47.266102 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b045c1e7-3e0b-34a1-965f-75090993d3bf | -3.5988 | -47.273399 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c49b4c25-1ed9-3d43-8057-cad89f0f19fd | -3.6005 | -47.280701 | 2024-10-28 00:49:41 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca96e025-03cc-3ecc-8c75-c802f20d32ac | -3.2393 | -45.992802 | 2024-10-28 00:49:42 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c45c035-97b8-3901-be1a-7242d96fb0ab | -3.2413 | -46.001099 | 2024-10-28 00:49:42 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef3148f6-ee23-3e90-a27e-31b499f1b912 | -3.2451 | -46.017601 | 2024-10-28 00:49:42 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b39e7f6-a3f9-346b-bb34-24c5a40a2f5e | -3.2471 | -46.025902 | 2024-10-28 00:49:42 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97594206-779b-3453-bcbd-c3002e928f07 | -3.2773 | -46.2001 | 2024-10-28 00:49:42 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d35cfc9-4278-384b-a495-73567805f95a | -3.2792 | -46.208199 | 2024-10-28 00:49:42 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2f23ae0-f6be-3780-b011-665910bcabb6 | -3.2811 | -46.216301 | 2024-10-28 00:49:42 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c363b189-3b47-3c60-bd6b-ccfca8b9111a | -3.2676 | -46.202301 | 2024-10-28 00:49:43 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7569cf11-1629-3483-92f2-c7c129ba0426 | -3.2695 | -46.2104 | 2024-10-28 00:49:43 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 868ab189-51e9-34f3-ba72-8ecb31249a3d | -3.2714 | -46.218498 | 2024-10-28 00:49:43 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 431999dd-6e00-34c1-896b-a8066c95dfd4 | -2.8879 | -51.822102 | 2024-10-28 00:49:43 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9205754c-078c-3920-bf87-e2e5fe4e857d | -1.9692 | -47.944801 | 2024-10-28 00:49:44 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be9f7022-dd56-31c8-a155-4f163defab95 | -1.9709 | -47.952 | 2024-10-28 00:49:44 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa432aa-9585-3a87-9ac6-0c9be59527c7 | -1.9495 | -47.904099 | 2024-10-28 00:49:44 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15568354-f422-31ca-8872-cac8edf7a4d2 | -1.9512 | -47.911301 | 2024-10-28 00:49:44 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c5e299-57a8-3dc2-a622-09e29cb38121 | -2.8418 | -51.799999 | 2024-10-28 00:49:44 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa804a7b-d649-3f47-8af5-475f561dd3d1 | -2.9137 | -45.259998 | 2024-10-28 00:49:45 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63ad8eb0-0eee-3bca-9362-9584ef87f494 | -2.9158 | -45.269199 | 2024-10-28 00:49:45 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89b57cd6-1ca1-335d-a50d-9d8993690cec | -4.1229 | -50.5014 | 2024-10-28 00:49:45 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86645acc-e662-3a5d-9cb8-59a5c9b03ac8 | -2.9039 | -45.262299 | 2024-10-28 00:49:45 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 594db189-d061-3587-81c1-b91fc1cef2ac | -2.9061 | -45.2715 | 2024-10-28 00:49:45 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 159a4475-fd5a-313d-b1f4-ad5dbd66742a | -2.8106 | -51.798801 | 2024-10-28 00:49:45 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 536562fc-3af3-328a-bf76-2f45fa150dca | -2.799 | -51.793301 | 2024-10-28 00:49:45 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b679bc4c-0020-3265-9de6-e24476d758bc | -2.8007 | -51.8009 | 2024-10-28 00:49:45 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36947ab-e4dd-3871-9b06-b5fc48f1ca17 | -2.8025 | -51.808601 | 2024-10-28 00:49:45 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3e375b1-662c-3b1f-94e4-f9c037d810b6 | -3.4044 | -54.4734 | 2024-10-28 00:49:45 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cff62d9-76f2-3770-a03a-283b84012440 | -3.4068 | -54.484402 | 2024-10-28 00:49:45 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9f1b81a-47c8-364c-b90e-29f224d34593 | -3.4093 | -54.4953 | 2024-10-28 00:49:45 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae130a3-74de-3da9-a174-2a3b2a247193 | -3.4266 | -54.572498 | 2024-10-28 00:49:45 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60e2bd8e-8eb8-312c-a347-c6cf16e3f3a1 | -3.4291 | -54.583599 | 2024-10-28 00:49:45 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd9a0a7d-b877-3d87-be47-8fe53c98155f | -2.462 | -50.405201 | 2024-10-28 00:49:45 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4391cc89-0903-38f6-8c58-ba54b91639e7 | -2.4636 | -50.412102 | 2024-10-28 00:49:45 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe264cc-176e-30d2-80df-cc47d581fb3e | -1.789 | -47.834301 | 2024-10-28 00:49:46 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e72748cc-ac31-3dee-919d-0adae50831a4 | -1.7907 | -47.841499 | 2024-10-28 00:49:46 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da459e25-8c3f-3b4e-828f-834daecbd112 | -3.6025 | -49.350101 | 2024-10-28 00:49:49 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2ea3fb6-2b3c-3535-bb73-c00b312f4d6d | -3.604 | -49.356899 | 2024-10-28 00:49:49 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56041ab3-0ba7-32e8-8c81-66db447e6c80 | -2.7813 | -45.9739 | 2024-10-28 00:49:50 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a684829-0c4a-3863-80c5-599feee891c0 | -2.2441 | -50.985699 | 2024-10-28 00:49:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e33262-9bb0-35d3-af50-eb05ea15607c | -2.2457 | -50.992901 | 2024-10-28 00:49:51 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38421dae-e726-3ca1-a7eb-b723ae05ddfc | -3.1739 | -49.145302 | 2024-10-28 00:49:55 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c89abf8f-6310-3fa9-8d08-8c8031eb9960 | -2.3245 | -46.493 | 2024-10-28 00:49:59 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b46fed9a-3824-3e03-9e2d-b8d4f6f2365b | -2.258 | -46.250801 | 2024-10-28 00:49:59 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42ecfb9e-0be5-3a8d-ae3e-de398c609182 | -2.2599 | -46.258999 | 2024-10-28 00:49:59 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f864e2f8-2a1d-36fe-9684-640e78fc86dd | -2.5312 | -47.429798 | 2024-10-28 00:49:59 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02b246a0-c055-3e5f-b205-7d15702f37dc | -2.5329 | -47.437199 | 2024-10-28 00:49:59 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 094d5f02-a185-3468-9ced-6640bdc9c9d6 | -2.5346 | -47.4445 | 2024-10-28 00:49:59 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794b31fd-00b0-33fd-b29a-44975584f706 | -4.47737 | -42.8823 | 2024-10-28 00:50:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c219f8c9-49fc-34af-88d0-452d7f8766af | -9.93832 | -44.49748 | 2024-10-28 00:50:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 705f92bf-9ae3-3903-929d-d88154344e83 | -9.93692 | -44.48775 | 2024-10-28 00:50:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d2745bb7-576f-387c-9d76-6c6d3d1ea784 | -9.44571 | -44.47414 | 2024-10-28 00:50:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aa537c03-7843-30f9-a7e2-a17c18b3eae4 | -9.43791 | -44.48515 | 2024-10-28 00:50:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f63fbc2-48b1-323f-9eb0-ed5e870d773f | -9.4365 | -44.47547 | 2024-10-28 00:50:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 18752b7a-3721-3b70-85ce-b3adca8ba86d | -8.76173 | -44.71499 | 2024-10-28 00:50:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 04b09481-738a-37b0-8cd8-cce393fdbabe | -8.07917 | -39.92613 | 2024-10-28 00:50:00 | TERRA_M-M | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 836f0787-56cb-3949-be6e-463f9f86ee39 | -7.98004 | -38.87424 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 8904462b-3206-392d-9f36-371a73102f3e | -7.88542 | -45.42049 | 2024-10-28 00:50:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3cfe944d-f46c-34e9-9179-a8e7b7e15190 | -7.42853 | -44.79634 | 2024-10-28 00:50:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7e5bb80-8d61-3e0b-b0c7-9c48453f7662 | -6.30063 | -41.92573 | 2024-10-28 00:50:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 210df660-f0bb-326f-a481-4dd405fe686e | -6.23376 | -39.52878 | 2024-10-28 00:50:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 32.2 |
| a2f7cad7-5ff0-371d-a8bf-42dd16f70afe | -6.09691 | -41.87387 | 2024-10-28 00:50:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| fcaf81dd-6589-3a30-94db-32260d32130f | -6.08843 | -41.88076 | 2024-10-28 00:50:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 1ede5e84-fb86-3ca1-8286-1863133b15fb | -6.08538 | -41.87559 | 2024-10-28 00:50:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| f5f87d51-1ed7-374f-ba59-3ed93ef089c8 | -5.6553 | -43.41413 | 2024-10-28 00:50:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c7f3b0cc-8c65-3a3c-93c5-b5f683f8c8d6 | -4.98151 | -43.71769 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 56c05706-0dec-3eaa-a99a-3baba7ed2c8b | -4.97973 | -43.7057 | 2024-10-28 00:50:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README10.md)
