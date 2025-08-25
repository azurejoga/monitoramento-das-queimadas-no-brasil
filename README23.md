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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b0c23ea-868e-3b55-afc4-9caffa0e193d | -7.33076 | -43.41788 | 2025-08-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b886dde0-36bf-3ac7-ae0c-0f024d3020e2 | -6.26522 | -42.87734 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 776579d8-aa36-3dba-80ff-3fdb5385bea6 | -7.3315 | -44.53476 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d988d92-b524-3497-812e-a9daf3d84c52 | -8.298 | -46.36189 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 076ba12b-455d-38ce-abee-c93f9753c9d5 | -8.02658 | -44.99725 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cfaf944-9fa8-3495-8e96-9db8fa5d887d | -5.79791 | -45.39752 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d29ee70-c37b-3da9-916f-bc2d6e8da32d | -5.87341 | -46.41099 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6318eb14-565c-3d92-a1bc-8ed8289bbdce | -5.50171 | -41.42348 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b5d6d3a-e049-369e-ac75-d7364a7f6e3e | -9.52604 | -40.32322 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1fc895c4-5829-3360-ac86-9cc1197be482 | -6.18282 | -44.12035 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f24c219-d1b9-3aea-aded-23ce99cf8b32 | -6.78506 | -44.31369 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b3bd692-07d2-3022-900f-c6584d1e7a66 | -6.19289 | -44.14066 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d77083e-165f-378a-bf15-2e16ca39c415 | -3.43843 | -49.04365 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75e185f5-dbf3-3b34-b5cd-eb4d0adbf60f | -7.8438 | -49.9987 | 2025-08-25 04:14:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c66ad3-eb96-3938-a346-4361940f39b3 | -7.58115 | -45.23075 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 911c5446-0a42-35fe-985c-513314f7bb37 | -7.54087 | -46.0214 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f0be0039-8fac-3093-aa36-d879d1ebc438 | -7.66041 | -42.67477 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f890bb2-53cf-32fd-897c-061d0e57b2cc | -6.90236 | -44.40856 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 072f6dbd-d40b-3139-b397-8d11e410c690 | -6.30109 | -43.75755 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad27cd78-66fa-3e1f-83a2-77e04ed5be63 | -7.47444 | -45.02348 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7fc149f-c9e2-3f43-94ef-fd37936bd0ee | -6.70354 | -44.01036 | 2025-08-25 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76a9cc07-a35f-33f5-8afc-497830cfee2d | -6.28524 | -43.85815 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9171a15-e75e-357b-86b1-75a28ea63e75 | -4.6751 | -41.0297 | 2025-08-25 04:14:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 158a8030-7ab8-3e32-b839-f97f0170b8d0 | -7.75387 | -34.91571 | 2025-08-25 04:14:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5c39f81-3fdb-3270-ad72-ce2e9ece3051 | -6.49757 | -49.91177 | 2025-08-25 04:14:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81162505-5e8e-3323-9679-0e4965028e42 | -5.87813 | -42.91903 | 2025-08-25 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 57835408-31f6-317f-abc4-fb04c0586eaa | -7.75581 | -34.91566 | 2025-08-25 04:14:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a6874bb-e9d8-3080-8afb-213f896d9a4a | -5.71202 | -49.10532 | 2025-08-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2513d017-15d1-3350-9738-1c531a36e280 | -6.99461 | -44.14985 | 2025-08-25 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f1d28a1-1375-357c-9b84-6f902162126f | -6.29078 | -43.86614 | 2025-08-25 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0103105c-6b00-3a98-9e91-38efbfd686ce | -2.2672 | -47.85415 | 2025-08-25 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d978dee-c31f-3979-bf69-d95e2cb3357f | -6.49306 | -43.42277 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 600aabac-aba8-39b1-a4a9-992d205a7692 | -6.16764 | -43.00374 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4704379d-7194-33ce-9328-298102c24b0a | -5.49268 | -41.41459 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3fee49d6-b902-3468-ba48-847e69803679 | -7.14834 | -44.1669 | 2025-08-25 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e743223-664f-3d39-983c-32eed63ba58b | -6.3813 | -45.59779 | 2025-08-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4e4410b-45dc-3060-a4c4-e7dbcf0325a0 | -8.75346 | -49.97277 | 2025-08-25 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f72dd3d1-cab9-3381-a06c-d1a99a94e2f0 | -3.6023 | -47.52597 | 2025-08-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f36d40aa-741a-3f26-bd15-3c7c4c4ea7ff | -5.53258 | -44.20562 | 2025-08-25 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b2e55d6-ef78-3952-9e7f-2b77b4b3de00 | -6.36092 | -44.47456 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a86e1ab-6349-3826-a6fe-deaf4dde6254 | -3.43847 | -49.04847 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7d30fac2-86bd-3254-81e2-d37255b18eb9 | -7.92305 | -45.89932 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2103c736-4a51-33de-bdb0-4059da489259 | -5.10331 | -46.16587 | 2025-08-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68c8b901-59a4-30fa-ad6d-c293893c9eda | -4.96085 | -55.82774 | 2025-08-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b83d2739-02ca-313b-84a0-7039f1a4c747 | -6.3002 | -43.89262 | 2025-08-25 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc19a020-3cbd-301f-9726-5db6e4b54f30 | -7.58957 | -45.24336 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0734c07c-cbf9-368d-adec-e56f5dd647c4 | -6.48921 | -43.4257 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3749d906-ee75-3fdf-a71a-b542e60d0c8d | -6.42319 | -42.78191 | 2025-08-25 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e682cda-27fb-32eb-8f0c-d354b523f23d | -6.37844 | -45.59344 | 2025-08-25 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1c8fbf7-2a0d-3318-8245-afd71c10483a | -8.05818 | -49.67159 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 595437bb-f45d-36b7-b3d4-def4a9bd7c21 | -8.8001 | -47.31016 | 2025-08-25 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0517a9d-0f8c-3365-817f-5bdaaf5dd38c | -6.04157 | -46.2958 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 936976f5-3dd2-3df8-9fb5-75a109060b08 | -4.96201 | -55.82141 | 2025-08-25 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d1e9c8e-e921-3692-b6d1-7bde7976bbc3 | -8.49937 | -44.74403 | 2025-08-25 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d8f6b69-7f9e-3853-a073-f049bd76e5f2 | -7.29193 | -44.52873 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78263fea-ed8c-3288-813d-8a817f28ee10 | -7.55545 | -46.24184 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a109c129-988e-31fa-9932-e7198417547c | -7.73974 | -47.36124 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8b1503a-3f46-34c6-b342-6ce35cc32b9a | -4.31031 | -48.10067 | 2025-08-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ccbd3b7-4057-3ddb-9305-90f40da73cc2 | -8.16629 | -45.06358 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2215f939-adca-3002-a975-e9ea72c11c80 | -6.50634 | -44.41792 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cfed325-883a-39ee-907e-3e33eef69096 | -5.10829 | -43.20708 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| ae57355b-8bf2-3dd4-bfa4-bc17ca16b129 | -5.65572 | -45.147 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 970764c9-152d-32a9-b465-06f08ea8cea5 | -5.74022 | -45.38876 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88b05b27-873f-39d1-8038-2a05ac3dde88 | -5.10031 | -42.95541 | 2025-08-25 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a489c6a5-6265-36d1-b539-c7c88fdec668 | -8.06542 | -49.68084 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b2b5391-125c-37ab-9233-6693b1ef9fdf | -8.05886 | -47.30104 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea5853de-42a7-3227-8527-a1fe40b194b9 | -3.91645 | -42.21524 | 2025-08-25 04:14:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e0cb251-528f-3cf8-8eb1-ea535a9c8f39 | -5.30259 | -45.26947 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f77d91d8-6925-3f89-855c-a17b924949c2 | -5.11051 | -43.21449 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b5f897ad-e70f-3605-8fc6-1d0689a6b036 | -8.54666 | -48.8618 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbccb930-7652-3e24-b66e-73f1c11ce040 | -3.58977 | -49.42816 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1e0e3a72-37e8-3637-87a4-f7030842eed0 | -3.4537 | -43.34594 | 2025-08-25 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88858984-6fe9-30f9-bdc4-39d3f4dfff0b | -7.65502 | -45.40533 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a63c19d4-bccc-361d-9b7f-d975aaf07b5d | -8.32333 | -47.26379 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59094aa5-f3c7-3d1e-a980-fa2b17354ba4 | -5.11159 | -43.2076 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 52f4a7e4-95ab-3cbd-8b4b-b8c82c1b5fde | -4.17598 | -40.71767 | 2025-08-25 04:14:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d88b4758-fa3d-30ed-8821-d69bf2fd8d5c | -5.11105 | -43.21104 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e179bb1e-9496-34ab-a5f4-3a2d07ad7ce6 | -6.50308 | -42.94678 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96ec5f54-38e7-332e-a762-bae45a378b1f | -6.36426 | -44.47512 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0020325e-a093-3b82-a6f2-7b047977ab6c | -9.53038 | -40.31934 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78d75c98-9fd1-32de-857e-2cd22e98de46 | -6.65317 | -44.39407 | 2025-08-25 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f9307269-ebe5-378a-b99d-4d82d0ba13e9 | -7.305 | -43.66892 | 2025-08-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74c4ad05-02a3-3dfa-a50d-a86ad44107f3 | -8.02218 | -44.98174 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f584a96-161a-3ddc-8f2d-8a71b31fa55c | -5.50565 | -41.4204 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| afee612c-b43e-3daf-8621-7853b1e3bd68 | -7.57717 | -45.23391 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 846408f0-567f-3cd7-8db8-1d11d9e3d763 | -6.90568 | -44.40911 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18d97ac6-d386-3cc9-a69f-0e768c0337ff | -3.8381 | -55.97156 | 2025-08-25 04:14:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 60853c46-1656-3d85-927c-8d639d63fd9d | -5.73077 | -46.1519 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8807294f-b335-303f-ad96-694c1e3dbac1 | -8.06899 | -49.68578 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 57e06f52-cf0b-3516-b567-eb91dc451941 | -5.50622 | -41.41673 | 2025-08-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 45914d03-a5c4-3998-b303-36db1162b245 | -2.99267 | -49.10071 | 2025-08-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a592691d-80f0-35de-a906-ccd352c946be | -5.94147 | -44.14018 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28985eda-2b12-3371-a74e-abd52a5bd4cc | -7.66204 | -42.6642 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 430b5c58-8416-3efb-b2e2-071142747bde | -6.0323 | -42.80157 | 2025-08-25 04:14:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8956b62f-cf14-3a5b-9cb1-83dcaf937352 | -3.43771 | -49.04798 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 46d5b642-a2b1-3975-9a0d-4738624f2719 | -7.91798 | -45.8867 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4edf03b-d467-3186-8f80-7cc3138126a9 | -3.35189 | -43.36576 | 2025-08-25 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3cadad1-1654-3772-b3ee-44afc2aa043e | -6.20734 | -44.13565 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22c12b28-0ecf-31df-bf9e-36f498946c2a | -6.79562 | -44.33335 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8de821b-49bd-3405-81bd-4a7946e678e7 | -8.42994 | -48.25771 | 2025-08-25 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
