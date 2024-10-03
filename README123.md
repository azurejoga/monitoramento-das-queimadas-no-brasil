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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e6b6144-6170-365a-b9fb-88d3ecc27d87 | -12.4915 | -47.50343 | 2024-10-03 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f9986e3-6f51-3ff8-9c0b-3fe2e0d17285 | -12.28829 | -47.65343 | 2024-10-03 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db4fce54-be33-3b92-be9c-763453d24197 | -12.47822 | -47.49503 | 2024-10-03 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cd23ae8-b875-3277-8176-de381fa7e754 | -12.475 | -47.49219 | 2024-10-03 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11f8b421-0554-3356-91b4-3bcab6926920 | -12.4744 | -47.49658 | 2024-10-03 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 460d9c7b-2633-3d07-bd91-c17e4678340e | -14.78288 | -48.05744 | 2024-10-03 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0fec6d3-ad27-3659-b607-a99dc01435f2 | -14.79217 | -48.05483 | 2024-10-03 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe356b3f-cdd2-3bd0-a146-a11077c789f6 | -15.2024 | -47.51423 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a291cc3b-52b7-3d34-aae1-41c4b9b3bf69 | -15.20176 | -47.51936 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3d7ca48-3d05-3901-8728-b09b6d0550cf | -15.10198 | -48.23605 | 2024-10-03 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7574a2c-6f27-3454-ba09-76c366685ed6 | -13.74171 | -48.16439 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84a701f6-6dd8-386a-a27d-2834bb5cb7a3 | -13.738 | -48.15926 | 2024-10-03 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d078e54-37dd-3831-af88-664d6ddd5140 | -15.72366 | -48.38348 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2acf8636-2887-35f6-9b76-fca5015c0e35 | -15.71447 | -48.38596 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e9d5de5-db93-39bb-b08d-6647f473c61f | -15.38588 | -47.42535 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bed1700-f22b-3c8e-b193-38f4f6721f1a | -15.3837 | -47.42343 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6380c52d-5abd-381c-93c3-c96b90dac71a | -15.38132 | -47.42421 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e033330-372f-3de3-b839-80f6a1d8425b | -15.27728 | -47.5048 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d274f8f9-ce95-3169-a923-de6f865ec8ce | -15.27346 | -47.50692 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 645cd259-64e2-3273-ace3-548b30a5a18f | -15.26962 | -47.50051 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1180fa70-95a0-3012-a8d3-fdce2685dac6 | -15.2649 | -47.50074 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b110d37e-8291-37e8-998c-47b689b914e6 | -15.25478 | -47.4975 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e5a879a-a586-3dbf-9c71-26d7f75d5c16 | -15.25392 | -47.50467 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67535b38-d1b2-3edd-b81d-e75a04317bb6 | -15.25101 | -47.49956 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84d432c6-30c4-3348-847c-13937fce5b1a | -15.24638 | -47.49917 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7f6c8e9-7910-35db-a081-de7cf53e2c63 | -15.2418 | -47.49839 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49041d27-d7ca-3d00-9821-5208aaf3eeea | -15.23724 | -47.49744 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 417708e1-b665-37b2-a653-a89e21fd0b99 | -15.23187 | -47.50286 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eb9a6f8-4e47-39b7-b466-bb92385328a5 | -15.22742 | -47.50113 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e31e013-125a-3d40-9068-6d9d30c83d94 | -15.22663 | -47.50736 | 2024-10-03 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3df19e39-9d34-3ad0-bea2-02945975c4c2 | -15.15226 | -48.08848 | 2024-10-03 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57285409-946c-37fd-918c-aa800fbc6037 | -15.14841 | -48.08342 | 2024-10-03 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c60f6973-043c-3ddd-a0eb-ac6f31f72897 | -15.14785 | -48.08782 | 2024-10-03 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af687b15-4a47-3f05-b162-d079cf8051db | -15.14729 | -48.09216 | 2024-10-03 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d3f2281-f435-3ac8-b10e-c4b252992b21 | -15.71879 | -48.38691 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81e80132-2d0f-362e-a474-c742f65635fe | -15.59992 | -48.55038 | 2024-10-03 04:51:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12579c77-2126-3ceb-9ab7-2f1e4b92cf14 | -8.53433 | -47.31893 | 2024-10-03 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fde94ef-ed6f-3edd-91ba-0fe0732b175b | -8.53011 | -47.31827 | 2024-10-03 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09846b8f-597d-3b03-8075-4a5c2a97b791 | -8.51686 | -47.32031 | 2024-10-03 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e1ddc00-e47a-34db-a4d3-5b082a8f8e44 | -8.51263 | -47.31968 | 2024-10-03 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6701b064-0c2d-3176-99ef-d4b59714a961 | -8.5084 | -47.31911 | 2024-10-03 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83ebca77-a75e-34f8-ac89-40e6f59fcac4 | -8.43801 | -47.11978 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6058f187-407d-3d1d-9204-0ed667f71fb8 | -8.43745 | -47.1237 | 2024-10-03 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a99fc09f-3a6a-39c2-a087-e89213d1278a | -8.43689 | -47.12755 | 2024-10-03 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33f10387-0c7a-3d05-8ca5-eb55e2cefc2d | -8.35642 | -47.5372 | 2024-10-03 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af21b300-63fa-379f-863f-c407fa356e10 | -13.19762 | -48.64525 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23b0f932-e770-362a-8b4a-e2439dc9ece2 | -8.35588 | -47.54094 | 2024-10-03 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c06df80-0c47-30c4-9aa4-18157706761a | -8.35534 | -47.54469 | 2024-10-03 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc408b0e-0857-3e7e-ad18-505af20b8afc | -8.35225 | -47.53662 | 2024-10-03 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdfc3a8d-4a94-3730-adc2-8a4da3eb2752 | -8.35118 | -47.5441 | 2024-10-03 04:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22263c30-184d-3f46-b1b3-2f4fceb7890b | -9.17359 | -48.74813 | 2024-10-03 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 090df152-ff8c-34ed-afa2-7f75059c96b1 | -10.00805 | -48.85144 | 2024-10-03 04:51:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6b110adf-bb39-30ec-8bc7-ba9c78f31b56 | -10.72316 | -47.69049 | 2024-10-03 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d11b3d8-7840-3c38-a44d-5b41d600be4c | -10.72151 | -47.70229 | 2024-10-03 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 857ff95c-790b-3681-94d2-cb0af18f85eb | -10.72096 | -47.70619 | 2024-10-03 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bc448fd-608a-393b-b706-8076d7875d79 | -10.45624 | -48.25927 | 2024-10-03 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3a143c23-80fd-39b5-b160-7e800344e941 | -10.42458 | -48.16388 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64f0e20b-bc9e-36e1-840d-733132de839b | -10.4241 | -48.16722 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0f3c8d7b-983d-3fef-9d74-9c2d4af92cd4 | -10.42046 | -48.16335 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bfb3e03-d339-3f91-92be-af42d813fac3 | -10.41783 | -48.15227 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2b66a1f-cc45-3f70-9eac-ab93e1add8e9 | -10.41321 | -48.15528 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5f63cdb-205c-3f97-910a-ef4e3b18e5ed | -9.89754 | -47.76294 | 2024-10-03 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c1a3051-3bf9-3ab0-a95a-be92599b98c3 | -9.89334 | -47.76235 | 2024-10-03 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1170a78-4b54-318a-a434-332fd935e376 | -9.70404 | -48.23198 | 2024-10-03 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a5c201f-d47b-3a2f-b236-acb11cbdfa65 | -10.03295 | -48.21489 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e29f550-75de-32fa-a1d7-e01b5cf9d789 | -10.03194 | -48.22223 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 938be439-b819-3daa-9ca1-67a4cf8d3336 | -10.02869 | -48.21753 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 893ef53f-ff74-370b-aa36-f534475ae221 | -10.02838 | -48.21794 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 567d460a-6e11-3350-b110-693066b3a1a9 | -10.02815 | -48.22121 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b973f36a-0c56-3af7-a96c-a042b0dcad27 | -10.02787 | -48.22162 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cf1a67a-62d1-3e79-b3d3-7d69ead44db2 | -10.01033 | -48.22953 | 2024-10-03 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01cd15a9-583d-3b0c-b06f-fa7f8cdd521e | -11.89903 | -48.31041 | 2024-10-03 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb8ff534-c459-3442-a8a6-8079e57ed548 | -11.68045 | -47.81482 | 2024-10-03 04:51:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50f939cd-b3a1-3b20-9127-b264c3057f3b | -13.19847 | -48.60692 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c56a38d6-a6fd-34e0-bcea-ff4cea16e1e6 | -13.19794 | -48.61095 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31b2fbf5-1638-3b03-9077-a94de6be789a | -13.19713 | -48.64887 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dc68370-eed2-3614-9ab5-a165d915f93c | -13.19666 | -48.65247 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7209fbee-5385-3e7c-b6a6-ab5612e92f28 | -13.1966 | -48.60759 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e433df75-fbd5-3b58-be72-c4e87f9a0087 | -13.19617 | -48.65611 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 776fe886-283b-3272-919c-a767caa17bad | -13.19604 | -48.6116 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec32f49f-6207-3f11-bdca-205e9827cae3 | -13.1955 | -48.61545 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dce7e52-6f92-3522-844f-ac721f3c18b6 | -13.19497 | -48.61922 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8b4c0f9-f011-3e23-90b8-7d9184740bb4 | -13.19445 | -48.63726 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21288549-1687-39aa-8697-5afb053c76a8 | -13.19445 | -48.62297 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dae75c33-cc81-3678-b05b-66d587633692 | -13.19433 | -48.60622 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96dbe66a-2897-3d2d-8949-35bac62255d1 | -13.19396 | -48.64098 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab4cbb95-1b40-3b98-aca1-7ca4e472512e | -13.1938 | -48.61023 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2cccb10-66ad-3f62-9129-fdb800826f33 | -13.19347 | -48.64469 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3c919a9-cd63-3e4c-b6c5-83623af83df5 | -13.19341 | -48.63044 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bf6219b-c02f-3d3a-adda-5df832570d6b | -13.19329 | -48.61413 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeeba1b7-afff-3948-915b-5a5076de4bef | -13.19299 | -48.64832 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a535fab-5c90-3754-a705-8dbb7a4e3d88 | -13.19279 | -48.6179 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1c45abd-9c76-3fad-b3eb-6901f705a7f0 | -13.19251 | -48.65192 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0600df0a-8e8d-3117-965d-b10fa38af524 | -13.19246 | -48.60688 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cefcc33-2a1c-3e71-bb96-d7d74b8c6058 | -13.19237 | -48.63787 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4ef2447-8718-3052-8de2-c16efcf30534 | -13.19229 | -48.62167 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96459994-a2d0-3b17-b380-d452565b6392 | -13.19179 | -48.62546 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59854279-37ab-39c9-a2da-442a646d7737 | -13.19129 | -48.62925 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b149d5cd-48f3-3d48-afb1-5336c53e9421 | -13.19085 | -48.61845 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fc18ec7-f453-3c98-8872-e1bb6933f49b | -13.19084 | -48.64886 | 2024-10-03 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README124.md)
