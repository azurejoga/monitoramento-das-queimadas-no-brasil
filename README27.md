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
| 1b15a63a-aa64-3a19-827d-3ac449cd7a31 | -2.66172 | -46.60165 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 315da1f0-12cb-3844-a222-e11a543eaa46 | -3.79974 | -51.17707 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96eca4b4-f130-3dc8-a8f2-e70f18eae6d3 | -4.08904 | -46.82681 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c7fb26-b68b-3d35-abdd-72dd57ab188f | -3.10258 | -53.73852 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2686249-9075-35e6-b597-b5a5855e34e1 | -6.84158 | -44.38703 | 2024-11-25 04:33:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb7ac442-84ac-39fe-9002-6a5a7c7cce1c | -4.66339 | -49.39037 | 2024-11-25 04:33:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c279c90a-3495-35cc-8d3c-649f0e5d70b6 | -3.94601 | -46.8938 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fda1ce51-854f-3db4-ad4b-eeaa542bfc42 | -3.8808 | -52.35921 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b68946c1-3213-34d2-9f4b-b7f5d4e2e540 | -4.25135 | -48.70565 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 912a5af2-0eb9-3eff-b44b-8f0de8c88cb5 | -2.70849 | -46.1043 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6147a8b5-81f2-394c-9c04-5da06e01aba3 | -2.69448 | -46.28196 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b44cbf31-b1a2-3c72-87dd-c95505ae3a9c | -4.3167 | -45.89795 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af8bc73b-c691-30dd-9d64-b46f3f00375a | -1.72609 | -52.48886 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99af0856-bf06-3c93-94b0-31b0e3978adf | -4.03548 | -48.08585 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69fa45fb-ef58-33df-87e6-22f6296b1b24 | -8.50484 | -47.06273 | 2024-11-25 04:33:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 683bdda1-85ff-34ae-864e-89655cd7eba8 | -4.50759 | -49.66422 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a135a65-454e-3608-8ad5-37d94df1e198 | -9.48319 | -47.7097 | 2024-11-25 04:33:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23214b70-fad1-3b50-98f0-199a8825e3a5 | -4.34994 | -46.78896 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 261f9c6d-8bfa-3aae-848c-468a779b381c | -3.24948 | -53.28519 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c02b574-b4bc-3fa5-85be-2109c6914425 | -3.79385 | -51.92714 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06ed5ad1-3ca3-3774-b411-087c3bfc8cf6 | -2.45605 | -52.16054 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd034afd-0628-36d4-8483-a8c97f2337b4 | -2.71018 | -46.11539 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90de28bc-1f4e-3eb6-9a9d-eae88ced72f2 | -3.04628 | -54.02836 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41423046-ae75-3118-a795-2645888b39b5 | -2.62252 | -46.19559 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11a2f217-9929-3627-9486-1902b9712dd3 | -3.63653 | -51.14631 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92e6e2d0-b8fa-3a04-80d4-1d31b6d3d954 | -3.51402 | -53.81813 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aac1aa66-5b1a-3315-a60d-420f01e4668d | -1.63201 | -54.46775 | 2024-11-25 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7e359be-fbbc-3d9d-8f62-751037ea27f0 | -3.97315 | -46.65217 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a58a28-2e51-3364-abca-82747a97bb18 | -4.34507 | -45.93955 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3a654d9-eba7-377d-b85a-1897371eb17f | -4.70108 | -49.64039 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d217610-97c2-310e-87b5-f2d94433456f | -4.02332 | -48.07687 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f0b8204-3548-3aaf-be79-35edc633f753 | -2.56875 | -46.56551 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9768e674-67f5-3c33-b953-0699c6f352f8 | -2.7898 | -48.56427 | 2024-11-25 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 208f00ac-713e-3379-a05f-15466bf1efdb | -3.31845 | -46.66462 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f649167-fd45-3967-bb3b-43b44e8c7345 | -3.24459 | -54.22606 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2106657-cf8b-3f7b-8008-e22c4ce126c4 | -1.74235 | -52.7331 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 63fbe97c-d15e-3c34-b2bc-798c724b15c6 | -3.25015 | -53.28115 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89f6f051-80c4-386a-b047-f24f78767328 | -3.37263 | -54.67953 | 2024-11-25 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23d82a1f-d889-3003-b52c-b67c803f9eee | -2.73653 | -46.09458 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d08f0fcb-ec35-38aa-b8b4-6508399eb0f5 | -1.24054 | -53.39199 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acb101be-91db-3f8e-af88-ca287b8d9c18 | -3.68025 | -54.58212 | 2024-11-25 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6df7089a-3b59-398e-b210-cdb97510c751 | -3.95846 | -52.22509 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1757f228-452c-32b5-8907-9b473574117e | -2.73771 | -46.1092 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c9a05e0-dfe8-370c-ae1e-615f46310349 | -3.0005 | -52.51111 | 2024-11-25 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 540f6529-9526-316d-b096-e9bf59bcdadd | -3.689 | -47.12577 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19975290-66b3-3583-9f20-98cb9fb75a0c | -2.90626 | -51.46541 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82ffd6fa-3bbb-3db6-a923-ab2be9e7f601 | -2.71408 | -46.11237 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d0d7d96-e902-3c52-b392-b907e809a796 | -3.80665 | -46.60823 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0f0e11f-473a-3c03-83d8-49b6f42f9704 | -2.79413 | -51.68356 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ed36650-9922-3b20-8d0f-ce4021a2156b | -2.81199 | -54.02308 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a5ff92b-78d7-3315-bdd2-c4bb07fb9125 | -4.57131 | -46.29884 | 2024-11-25 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f84ffb7-f6c9-3113-9b90-d275637fb66e | -4.13506 | -50.04203 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5054a31-f98c-3188-93ad-e596619ff0ca | -3.58827 | -44.92397 | 2024-11-25 04:33:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9964d85f-e166-30f6-a7be-1dbdff804be0 | -2.59743 | -46.55572 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38875ae1-cb45-30b1-a754-2a08902baf1d | -2.50471 | -46.23153 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 713e320a-638c-39d5-a48a-aee0dbaf3773 | -1.61637 | -52.57541 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c781cc3-c184-3191-b4cd-f705b5ffc207 | -2.45746 | -46.5591 | 2024-11-25 04:33:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d58d79a-67bb-37d1-9cd2-fd4ec4716cd2 | -4.10278 | -46.804 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d937f855-f96a-3979-8b3c-7cad65669c12 | -2.64619 | -46.13081 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89a3b887-5f59-3b90-9adb-f747fce91960 | -2.82069 | -51.29683 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1ef67f01-383f-3cd2-87af-377958bd8dd3 | -2.67721 | -46.26138 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dd68ad3-676f-3cf4-bb9c-741ea07b15bb | -2.70776 | -46.26249 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5930fde0-bec5-3ec0-8518-153c71e8b3d6 | -1.52135 | -52.0509 | 2024-11-25 04:33:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74a7c38d-6b38-3c1d-9460-9294df3287f2 | -3.25596 | -54.21351 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8dad7b0-f628-39c4-8b32-ce247c6e29d4 | -2.89648 | -51.57508 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8069bc7-6073-315f-878d-d41b507db08f | -2.58154 | -53.96613 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 79ea9f13-b540-32ce-bfd0-b41c001828c3 | -5.61443 | -43.47588 | 2024-11-25 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0083252-93c9-34ac-90f0-eee4f5c35874 | -4.20601 | -48.12717 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d01a25f-d1de-310a-88b7-01bcd21d39e9 | -1.13275 | -53.81194 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4420af5-9ff9-3c7c-9967-ec65ed96a2d9 | -2.4793 | -47.96624 | 2024-11-25 04:33:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cb55d86-0383-383a-99cb-0d03f37db7d6 | -3.76122 | -52.07758 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99806a3d-71e6-3af6-9b1e-5fe974de4c19 | -2.13564 | -51.01619 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 011b52b4-1214-39f9-94b4-b9d86fdfdd87 | -2.55602 | -46.56001 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83dc2720-96df-3022-9a01-5895753b7b24 | -4.27331 | -45.92522 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d532e07-64f5-34be-815c-8f1229978c3a | -3.27023 | -53.81702 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5463a39d-70af-31a2-8b43-bd2e050811cc | -3.82334 | -52.23828 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 703f4164-389a-301d-9de5-e415f6fbba77 | -4.05253 | -46.68946 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a991f8-9e06-3248-8844-73b0453beee8 | -2.7129 | -46.29246 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 496c7805-8e46-3946-976a-aa0d41fe30c8 | -4.35112 | -45.7867 | 2024-11-25 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64769eaa-dd3c-337b-8e86-5ccf4af99017 | -2.92607 | -51.76957 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cb5378aa-427d-3806-86d6-da37fc866f94 | -3.22654 | -53.92427 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52830f23-b575-3f26-8399-1b4b14767857 | -4.93004 | -50.47103 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b70caff-c7f5-32a2-847f-dc6a86d551b8 | -4.25416 | -48.73138 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 91dff3a9-ddfd-376c-88eb-e6fbd7eb01c2 | -2.50804 | -46.23204 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d67c934-e840-33e3-95af-7d6fadd6e6da | -2.71128 | -46.10834 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 189ae282-fd8c-370f-8c57-9b1d4ccfd452 | -2.67496 | -46.25387 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d239fa7-5844-35f3-9443-43840766e627 | -4.30112 | -46.90626 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e0e2ff15-c746-3336-9357-be98c8c43b3d | -4.02387 | -48.0734 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a0f2e23-6a74-3d6a-8046-2f430cefce05 | -3.71045 | -47.1185 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3dff5759-c34e-33f7-9b3e-1da9c8816626 | -8.50822 | -47.06326 | 2024-11-25 04:33:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8ad6908-2578-3611-8857-8f2141ded11d | -3.96965 | -49.93776 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fd9302e-8f13-3610-a3ea-39bdaf71816e | -3.50671 | -53.80756 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1893b3fc-2f54-3d2f-aeca-b3327b8e6201 | -2.73436 | -46.10868 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b47195be-c73a-38d3-ae1e-465bdd4727d9 | -3.27687 | -48.76024 | 2024-11-25 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2bcd45a7-64f6-3d16-b4cd-6b03f9ef78e2 | -2.81546 | -44.10839 | 2024-11-25 04:33:00 | NOAA-21 | AXIXÁ | MARANHÃO | Brasil | 2101103 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a4a027-949e-393f-a315-af68038db749 | -4.847 | -50.80513 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daabbefa-7ca0-34b0-b875-e63a0c4d0ce7 | -3.13299 | -48.98468 | 2024-11-25 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a34bd65-84f1-3708-82ea-04ddc6f3c233 | -9.46034 | -47.34914 | 2024-11-25 04:33:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41b84fa6-a69c-3d61-a252-7995aadfb1b6 | -1.7218 | -53.25463 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 909a8c14-f199-333c-94f1-7391e56f202d | -3.38686 | -50.32103 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README28.md)
