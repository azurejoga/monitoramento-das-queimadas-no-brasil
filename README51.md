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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cfcf723-10f8-3d15-874f-fbffc39f7390 | -3.97999 | -48.40657 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 284bb677-ecd3-322b-aefc-54655d32be99 | -4.05722 | -48.23978 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d66c0f11-6edb-3699-a013-91a849f9dcff | -3.98098 | -46.41599 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6112f282-dcf9-3314-bc28-49054912f0f2 | -2.87185 | -50.40718 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70a98ba7-1fa7-39d6-ac24-3f8fa12a6e02 | -5.14053 | -47.71078 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d09d245-33f6-33df-a527-d3cccceea78a | -4.24892 | -48.53502 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5798246d-a1dc-317c-9e1e-6b6fe3a15a72 | -3.0718 | -51.35802 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68e95db5-4c4b-372c-8d30-4f84e60933de | -4.21128 | -45.85333 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4d75b62-18ac-334a-97f7-8562f24a9a3f | -4.74914 | -48.42764 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99a39820-cea5-3a46-82ad-dcae1cee9ea7 | -5.68985 | -45.86822 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee598988-5157-3975-a9dc-2974c7d7d450 | -3.28876 | -50.18405 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12459012-33ec-3f1c-98f1-2ee7af88d6b8 | -4.29174 | -48.58852 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c88e4ec-7e89-354f-80fc-8fe35640d776 | -3.82452 | -46.50324 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70ede7a7-7b9d-3c8b-8be4-73a8d87471bb | -3.72667 | -50.43596 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e0c725f-16fd-32a5-b513-3fe6348af563 | -3.95918 | -48.17109 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ff0e577c-a787-3a8c-b421-c5fa4fde9409 | -4.24391 | -48.54506 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d90ff665-18c4-3d19-8e87-91174b3a6661 | -3.81615 | -49.85942 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fb575ab-d857-37b4-a162-ee455f1c778e | -3.29397 | -50.08212 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 784f32e5-bc0f-3a9d-bbd0-31bc80839e01 | -3.11503 | -50.13749 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fcdb146a-5562-3837-bed1-68a8cbb6f55c | -3.97456 | -46.16913 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f9618e6c-711d-3808-8f7e-3e36e6794d23 | -8.84984 | -47.69169 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cdcbaa9-c275-3473-a4d8-668aac43a461 | -2.62732 | -51.29678 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| caeeb12f-a349-3670-b3bd-9e86bc84c544 | -3.12752 | -50.14744 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 886e9695-23fc-390b-833c-9253c615362d | -4.31124 | -48.61673 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba0ee0b5-7ce5-32a2-93a1-f16a5ab12abf | -4.73337 | -48.99987 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 660e332e-5642-3c5d-b7db-cdea59bb1452 | -6.28501 | -47.34893 | 2024-11-09 04:33:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b56c3fee-91af-3326-a61f-1b7066f9a0c1 | -3.72644 | -53.4032 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55ff5cf8-6982-36b4-925e-b95e1c6a16ef | -2.69143 | -51.69767 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f005d55e-68a0-3665-90d2-4f523540caba | -2.97765 | -47.9211 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5a515855-259c-3690-99fc-3080a14a3014 | -4.8672 | -45.67419 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbde6b35-6fcd-3aa2-88f0-4bc7f5d69af5 | -3.43512 | -46.20631 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39f4faf0-1169-3b9c-9b47-002a448861a9 | -3.83865 | -47.50528 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7919fed-75cf-312d-9b2d-91cf91bfdc3f | -2.56556 | -54.16597 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3000fa20-dee3-3075-9b53-89f461b99998 | -6.13288 | -42.55938 | 2024-11-09 04:33:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eca7174e-43c7-3b38-88f6-28108066318f | -3.21722 | -50.19784 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9ffbf7b-0f8e-3065-b972-b002a72e8b8d | -3.07826 | -49.56248 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c36391ed-871d-3579-8d80-3344159b5e8d | -3.17486 | -50.21704 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| beea4ee2-ecee-38a1-b172-1cd59864107e | -3.96081 | -48.16066 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e038a4d5-e235-3cdf-aace-bf389470e83a | -3.00917 | -49.10698 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2e14118-99c1-38d7-840b-f7289525edf4 | -4.21221 | -48.6847 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1b9ed5e6-907b-3f1e-af3c-4ab0a2ae5ab3 | -4.16071 | -48.25282 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3616f4e-61f7-3546-9da4-a2b4326c34bc | -3.51315 | -51.67367 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3d9c0f4-58d5-35e6-b62a-131eed6dccee | -3.25592 | -49.12199 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 598eff3f-9bf5-3f5d-ad35-ff3160de9452 | -5.18397 | -44.03563 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56355072-a4de-3b5d-998f-1e0a1b5be6f4 | -3.53232 | -50.87335 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22ee4e44-f0a5-3b09-80e9-caf2cb20d91c | -2.98235 | -48.02138 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34d45507-d970-3198-94bb-4bd72502a863 | -2.8882 | -49.38578 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3662ac0f-3029-35d2-a42d-e9cc49fd4ed3 | -3.07072 | -50.56969 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f1a4255-6272-340f-a3d0-dceaa8b4c5a9 | -3.07868 | -50.56653 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fa218a95-a0bf-3bf8-8731-8eebde1dc1ca | -5.58692 | -42.79766 | 2024-11-09 04:33:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 688d0382-d4fe-35ae-8711-1de697b27748 | -4.3856 | -48.57491 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef4089c9-6731-3621-9425-bc7cdde47073 | -4.56254 | -45.64791 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2d30661-345d-307a-9670-a1b33181b4cd | -5.3044 | -46.23307 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1942a589-ec07-3486-8dfb-3dfe2576cd64 | -3.91396 | -46.45243 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2af42699-abf8-35db-95b0-5cd28db6862d | -3.42864 | -46.40276 | 2024-11-09 04:33:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef93473-ad14-3aa3-8421-7cb1c1ce9981 | -4.36353 | -48.15282 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06713e2e-7276-3a80-9830-427edc444c60 | -4.11575 | -49.08006 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a93d56e1-5c6c-3407-8aef-ac21d252fef1 | -6.26832 | -44.54205 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b85dc2ac-cb2b-3031-95bd-5dd1f0c91a1d | -5.66269 | -49.99839 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0835bd68-cc70-310f-b20d-6fe948adf615 | -3.42943 | -49.24715 | 2024-11-09 04:33:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7812413f-713c-3c1e-b0df-39c266c42532 | -4.23271 | -47.5537 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3763e609-ad59-3578-9302-bfc6e1a29b52 | -3.73281 | -54.22544 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6bdf0510-a4fc-3ef5-8d7e-ac8b194e3c6f | -2.85558 | -51.77621 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d67f511d-2070-35de-bffc-c887e1687183 | -3.12066 | -50.21286 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5ac6dc9-3389-385f-8a4a-48b1891be144 | -3.95898 | -46.46998 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2dc407c-80c6-3666-9bb7-c70a7a025e3c | -3.33857 | -50.07586 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10549c23-7ed6-3a1a-8df2-14baa45687a9 | -5.63951 | -46.26523 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06e7c9e9-79b0-3db5-97b4-eb353e17a360 | -4.73228 | -48.98505 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 405640b2-c1af-303c-83e1-c017733c5454 | -4.12512 | -43.59659 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19ed4f1a-8337-324b-8c06-768be60606e2 | -3.12343 | -51.10794 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6838f35-c395-37ad-be63-7089f17aa4d8 | -4.61188 | -49.58606 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b9d0202-6542-3169-a360-06801408439b | -3.11685 | -50.14577 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9c39a6b0-485d-34ae-80ba-6467ca036f6e | -5.43269 | -46.94528 | 2024-11-09 04:33:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e28eecb6-dfdd-356d-9a22-92cd28ffb1d0 | -2.7211 | -51.7124 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9893bdf8-fde7-3db4-824f-a29b83697e8f | -3.03617 | -48.04752 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2dfef10-ad08-3743-b237-199cf7317c8f | -3.34795 | -50.35869 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9416ae6a-147a-35e2-97cf-c10747142b65 | -3.95749 | -48.16014 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9557b039-9f96-34d7-9298-2d6e4c9e37ff | -6.60616 | -47.99439 | 2024-11-09 04:33:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba37ff75-6f7b-3c48-b65e-f3c83a67cd4c | -4.38226 | -48.57438 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d38c8927-496d-3830-acc5-a783a4a55ff1 | -3.95472 | -48.15616 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 43a147ed-55bc-3c99-aa8c-9ee75062fc5b | -3.01643 | -47.95551 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1d997ac-d709-394d-a407-1ec7c97b224a | -2.18505 | -53.63675 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ea6ef34-e01c-3460-8065-affbaad39c4f | -11.06085 | -45.38754 | 2024-11-09 04:33:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2046de4-df41-315f-bcac-8138b22b09c9 | -4.73396 | -43.254 | 2024-11-09 04:33:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 629adb01-83e3-38d0-9932-ae791a61b4f4 | -3.85044 | -46.62144 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b0712c7-f123-38d6-a7fe-0ff0350bc792 | -3.95597 | -46.70868 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e96dd999-e543-32b1-9430-e0f333f0447f | -3.03062 | -48.03954 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fe6614b-70b6-3cc1-b6db-2600dc6335a2 | -3.01832 | -53.8707 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a572ad-83de-3c76-98f8-fc64cebaffa0 | -3.25271 | -53.40298 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97031eec-539d-399c-b9cc-84fcedddb811 | -3.96677 | -48.1225 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de0d044f-659f-3abb-bd0a-934260508be5 | -2.67461 | -51.82759 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 05956dd4-006d-32ba-b213-8449218c5113 | -2.87213 | -49.37555 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64870543-4786-30b4-bd6f-4c8b07d4aa19 | -4.03022 | -48.28193 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aaac8d2-4e62-35a5-bcee-140c43764769 | -5.51418 | -43.79169 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7354938d-dd8d-3dad-ba34-5f8789451680 | -4.74205 | -43.85905 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60b932a5-862d-3436-a477-f17e3c7cc104 | -3.29725 | -49.17395 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e750ffc-c3c8-33de-a2ff-7a3a3870b226 | -4.31963 | -48.65055 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 111797cf-a0e4-3e07-b6fe-d2513576b347 | -3.2808 | -53.67084 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f9060c46-01eb-31a2-909a-cb6dd13b8f32 | -4.20959 | -45.86419 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 01166e58-204b-3b66-adaf-1fbcf26134a7 | -3.82785 | -46.50376 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README52.md)
