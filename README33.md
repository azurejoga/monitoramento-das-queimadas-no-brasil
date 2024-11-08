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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d04686a9-8723-3da5-a449-92a1a3b87510 | -2.74827 | -53.22425 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 174f5eed-7ae4-3170-99f1-24a73ca81b56 | -2.44993 | -53.69547 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2d68dbc-ede3-3427-aba2-0d7c0bd15904 | -3.56063 | -47.37865 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5b33f937-096a-3a17-abd3-864f79a09abf | -3.72129 | -53.39775 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 344cf245-43d0-3f20-9afe-574f00903e0e | -3.25656 | -53.40943 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1522fa40-c08b-3e5e-8141-87f9dcdeda4c | -0.25662 | -51.64154 | 2024-11-08 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60527c1d-8193-393e-b877-0f8add91e281 | -3.24234 | -50.46407 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18af5c6c-117c-3dc3-971c-0f5a7e062436 | -1.53987 | -52.00764 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cf0ab3f-9212-3681-a7c8-9e5b0b8480e0 | -3.96265 | -48.17122 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d32d537d-0ad0-327a-9ee9-65ad4fac1dd2 | -3.17647 | -53.8531 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdd18505-fd43-3104-8053-a16975c659fe | -3.2241 | -50.37996 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c647c755-dcd4-329b-8e47-3e7ecee79c78 | -1.6734 | -54.34784 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb8edd2b-9ba5-30c6-99b6-48d95990090b | -3.24951 | -46.47337 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8add6aa9-6f4a-35be-a662-ea0f0ae2949a | -3.25427 | -46.47013 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5707f4ab-140a-36df-adbe-f56305690a66 | -4.23916 | -48.54289 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a63275a-9537-384f-a94a-ba496242a236 | -4.67843 | -46.44499 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4e7e201-258c-3023-b006-2467c394229d | -1.72929 | -53.7905 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6dd5ed3-26f0-3db4-9c3e-2ae367b8968f | -5.6862 | -46.43415 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27ce03fb-c4a1-366d-80a2-02777040303a | -1.38496 | -52.19465 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fcab906-d1f2-3bbc-996d-18931ad7cdc5 | -2.79859 | -46.64315 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c179de2-7fd2-3046-ae69-3ddc6cd5efde | -3.22017 | -53.37815 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32cb181e-1e2f-3417-946f-c65a72c2b75c | -2.63642 | -46.77766 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd7b0f92-e993-3b7d-ab8d-91814af04a17 | -3.10407 | -53.71009 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aadfacb-95d2-3773-a357-5ce53b939ed9 | -2.21165 | -53.67069 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62565809-1bd6-36a9-950a-ff0cd3d48c37 | -5.73128 | -43.81955 | 2024-11-08 04:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33f8947a-e0a9-3661-bf14-d15200fdde2f | -1.22241 | -51.75409 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 126dae63-d28d-31e9-bd87-de706683a526 | -2.27637 | -53.81689 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10d0e10d-1018-34c4-bb79-e62dafba9686 | -3.95032 | -48.15058 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71ca365a-3860-334f-b05f-1bca8cd63b82 | -3.24984 | -53.36454 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d72e2b6-36b9-3357-9d90-df85e31daaac | -1.15037 | -53.65563 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d624bffe-b602-3577-bff5-9c5851d3a35a | -3.07702 | -50.57166 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c068d8e4-ee97-3186-b855-113c603d964b | -3.20745 | -44.11671 | 2024-11-08 04:53:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c8dd6c6-9cc5-38b4-99d0-506cfa0e35eb | -1.17033 | -54.15616 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dec595ea-5989-3ae6-81cb-c141ff0ceaea | -2.9637 | -52.91157 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0d51cc4-8b50-30d3-8954-cd6a97517e7f | -4.45154 | -45.9172 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbc53714-2924-3167-ae1a-1f85e9cd2a26 | -2.23496 | -53.67805 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67e1c49e-f1df-3e16-9d30-c03e5b46574a | -2.87764 | -51.87647 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348f2615-5bb4-35fb-8efe-a04881609685 | -4.2186 | -48.55336 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 391c2376-7e5d-3168-8bcd-ab4849d4278d | -2.15918 | -53.69289 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d199ed62-b669-3dff-98d1-a87e54f352ec | -1.5751 | -52.13286 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b69f2e47-0cda-3b41-adad-46d6b9fdd01f | -3.55187 | -47.38625 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 1ef80274-185c-3ff7-a3d9-0b86c4bd5a34 | -2.16168 | -53.65142 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ebbc106-2ae0-30a9-867d-b0248c641623 | -1.44116 | -54.48774 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53e3072e-5940-3328-8b8b-e301a8e795f6 | -3.96334 | -48.16665 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 253a781a-89d3-3cb5-b5e2-da95cb87272c | -1.59133 | -53.73164 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22aa87df-fc10-3aea-b3ac-5bcbaa22f830 | -0.88331 | -51.74672 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e89ea10-c66c-3caf-8759-9ebf5c205cdd | -2.95856 | -53.72155 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f8eb14b-bf94-32ff-a87e-6a3fb07ce6a2 | -3.06157 | -57.10962 | 2024-11-08 04:53:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beb9c8ee-6826-3723-b28e-7ee9550901e8 | -3.33168 | -53.18837 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b06412f9-c052-3089-9bbd-c3df835d1d7d | -5.64225 | -44.24342 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41623f8e-e215-3608-94ec-5ea305fbf97e | -1.11267 | -53.17677 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b50c4f47-d016-3842-a29c-4ef10e0c02ae | -4.22964 | -46.90235 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9d9336f-db2d-3638-a965-e36c835e9e7b | -1.14806 | -54.16064 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f54f440-48c4-37bf-be4a-af7ac7799be0 | -2.80744 | -52.95494 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adfbaa92-d56b-380d-aa27-e7f3cabc5c12 | -3.02293 | -54.48635 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c43b1692-8b05-3b49-9437-28ee4529f706 | -2.64904 | -47.38021 | 2024-11-08 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4bbed24-6817-3978-9878-d10c2be97fa9 | -3.97158 | -48.16335 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2344e00a-8439-3a2c-81f3-bd4ec2053c82 | -1.64811 | -47.82219 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f28b28f-ecde-31c9-a483-23cf120dec81 | -4.87139 | -42.94791 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 09828467-5a5e-31f2-90ee-0aee51f70924 | -3.38317 | -50.23289 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2596d3ed-fc7e-35db-a9cd-481c81c8457a | -1.38612 | -52.20897 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09e96078-9348-3c69-807b-1f3293070a7c | -2.62085 | -51.29395 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a385a1d-9830-31b3-9f3f-af772f962078 | -2.61557 | -51.74397 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a3b8531-33d7-38fc-864f-e87fb9c1109c | -5.66428 | -46.64773 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8de70f3-88fd-3eba-961a-562758c4bbd5 | -4.7755 | -45.73835 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9028679f-3d0b-35bb-896b-d88e804006fb | -4.51768 | -45.68068 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 735a74f8-bbeb-3d3c-b939-95c1024c0c87 | -2.81642 | -52.95995 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93db0e77-e99d-3778-8076-f9577a7c5029 | -5.68441 | -46.3219 | 2024-11-08 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d855815-ca71-3fda-a9ba-fe0885c8457f | -1.41024 | -54.49912 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84fcc307-5890-317c-b385-ee6adc48c5f4 | -4.88657 | -42.75702 | 2024-11-08 04:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20f772ab-a8c5-30f9-b0a0-937bf722551c | -3.28889 | -53.24689 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bf7067b-0789-369b-ad7d-1c863a16bd2c | -2.61066 | -51.75375 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4983cad-dfcd-3236-b388-746dd12d0bf7 | -2.79798 | -52.94992 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 33d7a8e6-3e03-3517-ad14-e779fbd32566 | -4.52668 | -45.68181 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c2fa1481-6b58-3492-b6e3-54cd19af851a | -3.01766 | -53.43438 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 980914a9-1875-3f77-a237-8b63ade21784 | -3.91242 | -46.44301 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cefc706f-e804-3d35-9ddf-ec4efe351ffe | -2.79574 | -52.94242 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f4d2e14-3af1-34b5-b9d2-36cc2c42e7d7 | -4.8709 | -42.95147 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 4c5e0361-caa4-32cd-bcd4-f836a09eb8ea | -2.81531 | -52.96699 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feaecde9-a547-37d5-aeeb-b8a83e8ea91e | -1.66531 | -53.79628 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a302423-6d5c-38e6-99b0-5b0963f99eb8 | -1.2085 | -53.64208 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d212bff3-a231-3ef4-a322-8ec2200499f6 | -3.01499 | -53.21133 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81fd31aa-a58b-31cb-b211-3cecb6edbf8b | -3.24425 | -51.55013 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c6043b6-779c-3686-b12a-9a4a5c976ebf | -1.45841 | -51.48538 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccb89e17-1260-3021-91e2-ed0593659881 | -2.6178 | -51.75134 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8904f50c-38cd-3da8-9d17-07a788ac35c8 | -1.38101 | -51.43483 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f12d2f2-46aa-31c4-a78d-711070fbf410 | -4.60919 | -49.57962 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3509801-a6e5-39d3-92f8-cad8f21d856a | -2.0171 | -46.575 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 223c53df-3fef-37a8-93f4-92df5c64d53f | -2.47982 | -48.53642 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e509f0d-f2c6-3642-9e61-eb4cf7c58e98 | -3.03061 | -53.26463 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 664fda1d-fe42-3d34-8d72-dad2de1a40b4 | -2.82309 | -52.96099 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bc60def-d94f-3b95-b484-d2e070f0c4ae | -4.77223 | -48.68218 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e866db2-d257-3e8a-8cfd-df0343c4c2a9 | -1.34011 | -54.62553 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b52dd0b-85b0-3ea9-8937-44eee39a41d3 | 0.04469 | -49.52067 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 088526bb-57bc-3caf-81d9-e2a82bfbdf23 | -2.71951 | -51.71084 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28fa7f4e-d3f4-3717-be36-e8523f7e7b24 | -0.92339 | -47.13161 | 2024-11-08 04:53:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 334b2736-17b4-3987-86b7-62d4f4398d4f | -3.80392 | -43.59949 | 2024-11-08 04:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bf90dbd-e7f5-38e7-b8b9-c91f863cdfad | -2.17093 | -46.44185 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 235d0d49-a87d-3921-bd14-2ee1f7d2fbcf | -1.46232 | -52.33115 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9776d42-ac5c-3970-ad49-431412bf3c8d | -5.98794 | -45.37051 | 2024-11-08 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README34.md)
