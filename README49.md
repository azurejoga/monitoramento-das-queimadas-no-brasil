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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed41d26d-9cae-35bd-a765-af4780c1a4f0 | -6.69754 | -45.65173 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83aa4372-fc41-32d8-8c03-234c54d3d007 | -6.99261 | -42.69727 | 2026-09-28 05:10:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80280d53-ff93-3463-86f5-03ec1a52a8a1 | -7.4202 | -55.63283 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c05d21c-c2ea-30af-9a68-ad9c04016448 | -3.22273 | -54.31858 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 39f1ac48-3968-39e1-acce-59ab2f3e4a76 | -7.26337 | -45.34178 | 2026-09-28 05:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bee0244-d647-30f6-b040-a5aa1014681e | -9.74674 | -48.95625 | 2026-09-28 05:10:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dda1fc6b-35d9-3af8-b4d0-f5f4dbd169c9 | -3.29415 | -50.3092 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64bc3151-4122-3b74-b656-9cebe915a15e | -2.78609 | -57.69754 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0badfe2-da0f-3dea-aad2-6ae0527a8a1e | -6.08095 | -57.8032 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 578115e1-14b0-34da-bd00-e4533ff02537 | -4.31568 | -50.39913 | 2026-09-28 05:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 90ebdb18-f1dd-3dae-b936-dd694f9e2e7c | -6.67435 | -45.62345 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c028900e-3c4c-3c40-918b-7e0f87c7340b | -8.1902 | -54.79753 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b9fbec7-b1ee-395e-bfa0-42e873db9e6e | -7.68209 | -44.78766 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 889d5b7c-5f6b-3c97-b801-331a9348b16f | -7.68836 | -54.764 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e5747c7-7231-3077-bde9-f358a346c77b | -6.6889 | -45.97736 | 2026-09-28 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b679a3c8-da46-3d58-8b8a-cb7be2d01c9b | -3.14182 | -54.07999 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87e44040-6b4e-3b7e-b07b-bd7b1ce0f44b | -6.69434 | -45.97532 | 2026-09-28 05:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b845158-95aa-3617-95c8-abcc7a8b69bd | -10.37481 | -44.97052 | 2026-09-28 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0012e361-f011-32ff-a745-0ccd53e60b5d | -5.89471 | -42.43793 | 2026-09-28 05:10:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b86204f7-6537-3ed7-9013-7f867bbd3f95 | -3.15295 | -54.09604 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3de828a2-fc0a-322a-9e79-9d625eb56526 | -5.72448 | -53.45328 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36ffe085-ba09-3a7b-abfc-0e7249e68521 | -7.82535 | -55.13366 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cda44b3-06c4-31a4-928f-f36994c77660 | -10.22645 | -49.98672 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c47f371-9e04-338b-a66d-db01de1e7fce | -2.77531 | -56.57222 | 2026-09-28 05:10:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 531543de-98dc-32f3-a483-ec08756914a0 | -2.67314 | -56.46459 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b0223e9-d371-31e2-9b93-a5da57fae2e5 | -10.20771 | -50.00217 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d372f95e-cc7c-31c8-bae4-6ce78177df17 | -7.82201 | -55.13312 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e144d3b-0d04-3e3f-b1f7-e867845468fa | -10.26184 | -44.61483 | 2026-09-28 05:10:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cb52adb-e212-3fbc-96b0-6fa4109d8b9f | -10.23353 | -49.99506 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbad3856-6f92-33b8-8baa-b2eecab3aab5 | -3.29713 | -50.31392 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6de0f42-4824-3178-be67-774669b5c268 | -8.13821 | -44.45274 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14395745-ff05-35bd-bbe0-94000f285633 | -4.7935 | -49.11441 | 2026-09-28 05:10:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 455b62c3-57df-392b-a1b9-23facda92a89 | -11.19117 | -44.79485 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 744004a5-7191-3732-879b-de189ca81a44 | -2.65734 | -51.73991 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e05512d-3570-35a6-9c94-1e80dd18ba16 | -6.71152 | -45.58823 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f9d538d-546a-3504-8ee5-a1dc84b19bb6 | -10.20974 | -49.98791 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5374c0fb-734e-363a-935f-98608edc439a | -7.46298 | -55.00386 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bcd790f-7a5e-3b3e-a27a-2f580b55607c | -10.12982 | -45.13677 | 2026-09-28 05:10:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75eb1f88-6dba-3e7f-ba87-44673cb6b3ce | -2.89709 | -54.106 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea4d4e23-4bf9-3eff-8f18-5183bf7b56b3 | -8.73464 | -47.97972 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f232550a-d357-35d3-a653-8ed548d247de | -6.74963 | -55.09125 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80ab096b-bd46-34dd-ac3d-f2f0c8830382 | -7.70756 | -44.93316 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13931f3f-ca3e-35fd-999f-5b896c9ccb39 | -2.91714 | -58.30644 | 2026-09-28 05:10:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba1bc762-76e4-331d-b51a-01f4b62a1489 | -4.79052 | -49.11751 | 2026-09-28 05:10:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f770d17-4bdc-3e56-8f88-7e1e6f3ac783 | -10.74943 | -48.91117 | 2026-09-28 05:10:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21def1cd-8672-3fbd-8a70-c3830311425b | -3.14962 | -54.09551 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b45a2f8f-48ee-390e-89ba-08aadda51bdc | -6.63727 | -59.94958 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c88fe035-6faa-3b18-8860-ac6b450d2267 | -3.42241 | -48.33807 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40698808-4da5-3734-87a4-d6b0392afb38 | -7.97626 | -45.01756 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 148f784f-75c6-3e0d-b615-8c34c2920577 | -7.3839 | -47.01574 | 2026-09-28 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 414854c3-3f8b-35d5-87d1-01a6753d6876 | -6.77565 | -46.68076 | 2026-09-28 05:10:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5ba56a8-3817-3e35-a666-ad9ce4bc5070 | -3.1446 | -54.08401 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a54cc49-6619-3629-88f8-9896c0adbc8b | -3.56844 | -50.29585 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8ec71a0-a94b-346b-b854-8513626bc2f7 | -6.64571 | -59.95114 | 2026-09-28 05:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f35e925e-dc6e-3a47-84f1-349c99c75c9a | -3.2922 | -50.32168 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b40edc83-de98-3e4d-9fda-119f7f320a16 | -7.88906 | -45.44023 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96d929ce-4abe-3b01-b618-9088bb835e6d | -8.72999 | -47.97723 | 2026-09-28 05:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d4630a2-2a0c-3291-90b8-8d9a670b0481 | -2.89208 | -54.09447 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0116142c-7379-3d08-9a2f-5d299722f3f5 | -6.15947 | -57.70501 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50f80d9d-371f-3a56-9cd8-5be1655cb34d | -3.01304 | -54.21026 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b16034e-471e-39c6-9d25-cc126e1cc313 | -3.14571 | -54.07704 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88cc3f23-1a2a-34ed-ae73-74b141ec2111 | -3.20079 | -51.04124 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0db47bb0-19df-3298-945e-755e40d9e009 | -4.28534 | -48.63216 | 2026-09-28 05:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01543ad6-5a59-3ae0-bae6-ee48f486f62a | -2.72984 | -54.19777 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f420fe0-f8c1-3540-af2f-9d8d522297e8 | -10.21835 | -49.98553 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3e9cd06-87bf-3090-88e2-d4e635cd36bc | -4.2529 | -48.54315 | 2026-09-28 05:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69e39c9d-f247-3e2c-9d68-3f1ed92145d4 | -2.97513 | -54.14697 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11959078-20af-3935-a09c-3d112f49e93d | -5.72498 | -43.27693 | 2026-09-28 05:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1931b348-cdac-3b9b-a96c-422cb3f12301 | -6.78489 | -59.38813 | 2026-09-28 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a70bf431-b4bc-31ec-9b01-6bc81f8db0b9 | -6.68504 | -45.65929 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b037d12e-ea82-31f2-a435-4586e5f50e33 | -3.20902 | -51.03461 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d0b9f62f-0cee-3156-aa6a-a23fd9252637 | -9.15369 | -45.63902 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 369c89ca-53a4-383b-b1f7-b8b87e9c61cd | -7.97604 | -45.01638 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a99a58c-3bed-31cd-918a-37d8b67f95c7 | -6.69193 | -45.64806 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da465c32-605c-36c1-ac3a-48ee672776ed | -6.35627 | -45.7867 | 2026-09-28 05:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5cd475a-4c3c-3ff9-8a17-141d8ddad60b | -2.96346 | -54.0914 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d5e5271-1ee3-3eab-a7b9-6165f3c7455d | -9.19692 | -45.76472 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e6b8efb-3e81-3b4c-9d7a-eea9602c6be2 | -3.2935 | -50.31338 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bea754a9-6037-3438-aeee-e77e666b16cb | -3.22999 | -54.31613 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 465dd2f6-9800-3c15-b99d-bf060d5594cb | -6.09448 | -57.62922 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e0af79b-2cc3-3662-bb0a-0f873043c88e | -10.45301 | -45.09407 | 2026-09-28 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e30e04-cbe3-3609-8441-aeb854350390 | -2.91158 | -54.1226 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da095f23-68e3-366b-80fd-b5873cba8449 | -3.4137 | -48.34044 | 2026-09-28 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 386d5dab-537b-3ddd-b3d6-125591b58f31 | -5.99849 | -47.39407 | 2026-09-28 05:10:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319eb51f-2ccf-3849-a87b-68912a396bc9 | -2.90824 | -54.12207 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 844c2921-7663-3967-9607-aa2f3524c0a6 | -3.04005 | -57.50854 | 2026-09-28 05:10:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3d20035-61f2-30c6-91ba-112754a61329 | -9.97794 | -50.16273 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9ae9f284-fb26-3acc-8fa0-9fd0673fefad | -3.07384 | -54.37803 | 2026-09-28 05:10:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f698194d-b089-33f2-bb9c-3e889442e60b | -6.67905 | -45.62753 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27e96436-63ae-324a-a9e4-9a2897941c5d | -4.25699 | -48.54374 | 2026-09-28 05:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1316958-6ce4-3ee2-bca2-262cd55531f8 | -6.72063 | -45.59586 | 2026-09-28 05:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f957e33d-81a6-3b8a-a0c3-99780e477b10 | -8.23699 | -45.43584 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f620947-46fb-3dfc-a5e7-6741d9c72f88 | -3.14794 | -54.08454 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ab630c3-d729-30d6-9d1a-4a28f48877b7 | -7.26291 | -45.34507 | 2026-09-28 05:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4c5caf4-a772-345c-a33d-63279bf90e50 | -6.16836 | -57.69748 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 379d8f69-688a-30be-ba0f-23ce6ec1e820 | -8.59585 | -54.64783 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4006d585-558e-3b43-a8d4-b319778bd57e | -10.21481 | -49.98136 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41573f1a-a3e5-369e-b66f-21e3b32146d3 | -2.66062 | -56.44978 | 2026-09-28 05:10:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c3ad4f9-2ba5-383b-a9da-37781ab69b97 | -5.13455 | -56.02506 | 2026-09-28 05:10:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09764d99-dd2a-3049-b56e-19fa7b5f4a1b | -6.0989 | -57.62547 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
