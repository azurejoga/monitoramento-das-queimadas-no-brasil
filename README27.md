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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7838c1b-bbbf-3b9a-abc0-f3d3b6acde69 | -16.7155 | -57.3605 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28624cea-5f0f-36ff-a9b3-1f30f2d78690 | -16.7176 | -57.3694 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c783d419-0472-3637-abd9-48bb0254e780 | -16.719801 | -57.3783 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2069db03-81f7-3c26-ad85-c9fb85f53684 | -16.7283 | -57.413601 | 2024-10-01 01:44:48 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52d4357a-6dfa-352b-938e-2cb4ba131bab | -16.7304 | -57.422401 | 2024-10-01 01:44:48 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ef99362-2358-309c-812e-f8b0a9c0b999 | -16.7078 | -57.371899 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e24a5e9-6a24-36f7-9a16-97558ad9433f | -16.709999 | -57.380798 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45c130ae-3334-3481-aa7f-3b698edbd3e0 | -16.7003 | -57.383301 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c266b441-6628-38eb-8c2f-942bc536f041 | -16.653601 | -57.233898 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10b9985e-433c-3c1a-8fe2-d6444800e73a | -16.6558 | -57.242901 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 090c4708-f000-35ea-b0c3-44e23d497ff3 | -16.658001 | -57.2519 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ee616b5b-963b-35cf-a651-03a3556d13b6 | -16.6602 | -57.260899 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8bac6361-63da-392c-b0c9-9e44bdcf5190 | -16.6646 | -57.278801 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64e7fef8-0572-30bc-859f-0f96cb2f96a0 | -16.6667 | -57.2878 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 63e8bf73-a66d-3e98-b6b8-9371a24b6e9c | -16.6439 | -57.236401 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0e99636-af9e-37c2-8d96-08c466bfde41 | -16.646099 | -57.245399 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3cb8f46a-924d-342e-880d-f3a53dc288c2 | -16.6483 | -57.254398 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57ff4792-d53c-3cad-9105-70ab5a6e4751 | -16.650499 | -57.263401 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eab35df1-db1b-3f4a-9962-d1e5a696d0e9 | -16.652599 | -57.2724 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 060845a4-b97d-32a4-9b4a-f2bb7a9bf1a5 | -16.6548 | -57.281399 | 2024-10-01 01:44:48 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e932bce-b0e5-375c-8233-43acf5a9502f | -16.634199 | -57.238899 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4365d9e-79c6-3cd6-9999-1f228f4287fc | -16.6364 | -57.247898 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 482ed2eb-1e61-355c-a3a4-b57daef23293 | -16.638599 | -57.256901 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e45bd998-4001-3450-931a-afbd17fb5d0d | -16.6408 | -57.2659 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4bda0d7-47a6-3ea7-aec9-e5ad386a5d09 | -16.6429 | -57.274899 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7bc2f48-60bd-399c-9cff-938bb012495c | -16.6451 | -57.283901 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0464029a-652e-320d-9be0-f41ec6219ff7 | -16.6266 | -57.2505 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 990d62fa-6fab-341f-a2aa-a42c50a4a8d9 | -16.628799 | -57.259499 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9f70cce-4620-3d81-b6b2-f5ac0081feca | -16.631001 | -57.268501 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01b64819-dffd-324e-a809-8fbd84079160 | -16.633101 | -57.277401 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43a1c91a-49be-3326-95d6-ce1072c28ebd | -16.6353 | -57.2864 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c272aef-c312-325b-bc12-fce083878ad7 | -16.616899 | -57.252998 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8cae104-c600-348b-9803-8f684b8f9f67 | -16.619101 | -57.262001 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c20ec235-7eef-3405-b21f-624d87f91e44 | -16.6213 | -57.271 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41d4c6ce-1898-3523-ab67-cd8c7dfc5752 | -16.6234 | -57.2799 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 644dea47-f44b-32be-b053-b6ccc6c6522f | -16.625601 | -57.288898 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 135457ba-e7c8-32dd-bb70-77c6960367d5 | -16.609301 | -57.2645 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fedbaf0b-29f1-32af-a701-9df1668426fa | -16.6115 | -57.273499 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e460d962-77d7-34b0-ba91-8c8c425b787b | -16.613701 | -57.282398 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7ba01e2-a5c6-3410-9b5e-c612536a2423 | -16.601801 | -57.276001 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f2b37093-f9b8-3a9d-b4f7-97e850865b40 | -16.603901 | -57.285 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f8fe2d3-bd09-3db0-9be4-7bd6852e9f48 | -16.6061 | -57.2939 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 049405e0-8a21-3edb-8a1c-da01e4b8ab0e | -16.608299 | -57.302898 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bebb135f-c01d-39f4-b8b0-69b9938a7c78 | -16.6105 | -57.311901 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 006d8eb2-0c83-3371-af72-3356220820d6 | -16.591999 | -57.278599 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9710d6aa-2a2f-3834-905f-5e6eb940f6e7 | -16.5942 | -57.287498 | 2024-10-01 01:44:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0be3d5b-4da9-3d95-8717-95b374d1915a | -16.596399 | -57.296501 | 2024-10-01 01:44:49 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f5fceca-3aa0-38d0-958f-1c6c8125f350 | -15.6792 | -53.901199 | 2024-10-01 01:44:50 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4e5cf3b-0c14-3efb-8263-bc6a0dc0123e | -15.683 | -53.915798 | 2024-10-01 01:44:50 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce82942-693c-315a-b752-8a4801891b14 | -16.5228 | -57.334599 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e16d5ed9-db6d-3290-b0cb-6fda81c0cdaf | -16.525 | -57.343498 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c1128dc-6c57-31d8-a520-73fd778f172a | -16.5109 | -57.328098 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 04cb2305-851a-3909-a735-f85cc4d25264 | -16.513 | -57.337101 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e54c709-aed2-31df-9f91-167ddd49dc16 | -16.5152 | -57.346001 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fbcbafa-9402-34e5-b137-3262dd5e25aa | -16.499001 | -57.321701 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37407d7e-9934-3f50-85e6-20d8e59d23d3 | -16.501101 | -57.330601 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f237202-c80c-3307-a6cd-285bbaa74cc5 | -16.5033 | -57.3396 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95309893-79b2-3148-a180-63e613f319cc | -16.505501 | -57.348499 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61291919-2e25-3d06-be8b-c5125fd611c8 | -16.487101 | -57.315201 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9bf20fbd-8b83-33d2-ab08-3a8109f53721 | -16.4893 | -57.3242 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4cf5a02a-18ab-3183-a71e-9e39b9f0eb30 | -16.4914 | -57.333099 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b13369bd-622b-3889-8e11-c1deb588d7de | -16.493601 | -57.342098 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5832a0ea-9974-3f1b-8c92-d7798beeb302 | -16.4958 | -57.351002 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 95512565-1a70-393e-81c2-c23c52d8e3fc | -16.4979 | -57.360001 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 095f2c08-0ecd-3f91-8a99-d07067e0c9a4 | -16.477301 | -57.317699 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21e624b5-71ae-3fd5-83fc-6b6e379220bd | -16.4795 | -57.326698 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ceffa22-3873-3888-8f14-d04f4b59a7e4 | -16.4816 | -57.335701 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db836094-fd77-3f30-8bcf-4818a6020b3a | -16.483801 | -57.344601 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43be39af-0055-36ce-b667-d9d584f8b8cc | -16.486 | -57.3535 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6676c5c8-f8e2-3ca1-98d9-8290d1d4212a | -16.4881 | -57.362499 | 2024-10-01 01:44:51 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f80317c-0636-3588-bf12-b66d1404881a | -16.4676 | -57.320202 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7345d568-4dab-3947-bc5c-632b35960b67 | -16.469801 | -57.329201 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1d59f73-4bed-30bc-8f40-d3ec426c80af | -16.471901 | -57.3382 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d22b4958-59c9-311c-9fc9-a72439990457 | -16.4741 | -57.347099 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3026e1a1-d325-3911-812e-e7440ff39250 | -16.476299 | -57.355999 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ddc5f5c2-c03a-3377-84af-88c36762c80e | -16.478399 | -57.365002 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4c81b7e-2f09-35d7-bbbd-d42b64ebb142 | -16.4578 | -57.322701 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a26ada2c-8e84-3f1f-a0df-4e391740e0b9 | -16.459999 | -57.331699 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d55e05eb-0af8-3c32-aa87-98894f7a4366 | -16.4622 | -57.340698 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d86bdf2-9417-33b8-bd15-89f2a02aff8a | -16.4643 | -57.349602 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3f95e58-dd10-35b6-a418-ce0588f41330 | -16.448099 | -57.325298 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7be45ce2-39f9-370e-84e2-4204b6b9780c | -16.4503 | -57.334202 | 2024-10-01 01:44:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d26001e1-0886-35c7-bb91-83f429c539ce | -15.9117 | -57.163601 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae84c0a-3891-39e0-b616-a7d14256c1e4 | -15.914 | -57.172798 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f01b732a-9d8d-3f60-b860-3a7cb62018cd | -15.902 | -57.1661 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8fdc508-37c2-3580-9ba0-3ef97c9a64f9 | -15.9043 | -57.175301 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef04ae19-7fff-34f9-9368-cd849e0ae5f5 | -15.9066 | -57.184601 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1315c28b-f5c3-35f6-9090-eaf0c027325f | -15.9111 | -57.203098 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bad6c255-638f-3453-a7f3-79d5d6d4f00e | -15.9133 | -57.212299 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3734b1f-c0c4-3439-9ec5-10165a7d04dd | -15.8945 | -57.177799 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1019cee7-9e44-3d0b-a81a-5beed8775b52 | -15.8968 | -57.187099 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00015d42-b179-38ac-b51e-c42f3946f268 | -16.1828 | -58.4193 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1824b1d8-0236-3ea8-897c-e3f9144ec0a6 | -16.1847 | -58.427399 | 2024-10-01 01:45:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f8f2af5-a94d-3df3-840a-698e5b3ad0a0 | -16.1731 | -58.4217 | 2024-10-01 01:45:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 959ef296-f376-3217-ac06-6e06fe77b110 | -16.174999 | -58.429798 | 2024-10-01 01:45:01 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7b72e98b-63fd-314d-9500-91e1b0ec2eff | -15.7852 | -57.794498 | 2024-10-01 01:45:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfa6872-0459-3aef-a4c6-defbb6326905 | -15.6294 | -57.449902 | 2024-10-01 01:45:06 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07cd275f-e31b-31aa-a62c-e0ddaee8b0ac | -13.5781 | -51.1576 | 2024-10-01 01:45:12 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d66ed3a-98a5-3e33-93bf-acd264c2bbd8 | -13.5847 | -51.181599 | 2024-10-01 01:45:12 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6d8b8c1-3333-30fc-98e1-041ea6c684f8 | -13.5912 | -51.205601 | 2024-10-01 01:45:12 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README28.md)
