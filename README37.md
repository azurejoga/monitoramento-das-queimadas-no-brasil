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
| 5a29699a-4063-36b0-a9a2-8f08023310ad | -8.41366 | -62.6642 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47164da7-b4ec-300a-9749-1723b8a390c3 | -6.40143 | -45.69035 | 2026-08-16 05:16:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1797cecf-6352-3e01-aaeb-ffb0ac4f2e10 | -6.6303 | -55.30633 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba26ef7-27d3-3d42-84e6-0fd0fcbf971a | -6.79171 | -58.78722 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ca66d1f-2df0-3922-af4a-0613c85bcbde | -8.26251 | -57.34483 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28155e32-550a-39aa-9267-7fd62f2edf31 | -6.70605 | -58.95228 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9eda9d1-a416-3846-88db-aea3ff0a3dfe | -10.68014 | -48.99984 | 2026-08-16 05:16:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e3519d2-301a-3853-b947-2db8b93e8a50 | -11.20791 | -54.80923 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bec7d95d-73ed-39fe-ab76-0cb4acd26f18 | -12.01078 | -46.43403 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 674c1cd1-dc48-3b40-a1e3-28e722bf7517 | -6.84789 | -58.97079 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2724db55-45da-3800-8a22-d412a5584e40 | -6.54988 | -56.53949 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e1f6e04-67b0-334f-910b-c2a7302000d5 | -6.70248 | -58.95164 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f387e22e-9cd3-3dad-87a8-8d9daba88c68 | -12.45294 | -46.65199 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 340adbca-b770-3413-802a-8ea330cf1554 | -6.85804 | -56.43554 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e3fe5ef-1e22-3565-817d-700cbadf0bb9 | -8.54562 | -54.59118 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2258cec-d27c-318b-ab7a-2f12ecd9a943 | -8.66194 | -54.74069 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 003c6d74-385b-3377-969d-004e2b2acb0d | -6.81596 | -56.4431 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e988b82-dfe6-3142-b376-3a9179058fbb | -6.82316 | -56.46208 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c34ad6dd-6bcc-36be-b845-094b3d5c822e | -11.07902 | -47.2777 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bdfd65f-c139-34b5-ad57-24b7ecb28f9d | -6.3725 | -44.36565 | 2026-08-16 05:16:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde06ecc-f57c-3f11-9493-6186b9a78c86 | -8.95686 | -60.54909 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6df4dc56-fdad-348a-b6f9-6d228365cd74 | -5.26006 | -47.7071 | 2026-08-16 05:16:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56196e3d-e5c5-3353-ab40-1dca0ab398c9 | -8.79593 | -47.92418 | 2026-08-16 05:16:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d5b85c5-a5e9-3750-b6c5-d53690ce11de | -6.65128 | -56.43467 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da9e7fe2-c3df-3ebb-b453-d68e5e67ab47 | -7.83512 | -61.34602 | 2026-08-16 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66764dcc-75a1-3ed8-8b1a-33fd5195418f | -8.43002 | -62.67422 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d4c38f2-2484-3a38-a11f-26f7013bbbf2 | -6.6989 | -58.95102 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a21bedf-9438-315b-a307-846b019dfd4f | -6.83368 | -56.43879 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22e1c1dc-65a4-3d01-877c-d857678e42bc | -6.78701 | -55.83751 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f088c854-ba14-3679-a533-064a5a8848f2 | -6.85639 | -58.96377 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2e4653f-0318-3421-9a76-64aedf5d9953 | -6.97905 | -59.01238 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f6bef9a1-e9e1-3f71-a776-221a39fa8070 | -8.42926 | -62.67847 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 105ec2d0-06b0-3600-b7e1-efc93bdbf53f | -6.85638 | -56.42459 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc97848-fb7e-3379-876d-1b6c27fbd81b | -11.46515 | -46.61456 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1775a3a7-ec69-3f2f-b9e1-972a96b1abd0 | -6.8499 | -58.95853 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 856582ec-31d8-3191-8135-532734b1d947 | -8.90254 | -60.59258 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e0a7b2ff-43ec-3e82-babd-03ebe14b230e | -6.84475 | -56.43342 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22474c86-41e9-33f1-8924-865ecb8974b2 | -6.70895 | -58.957 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b58601e4-b534-3b6f-99ea-8a9bd2372bb7 | -6.86755 | -56.41561 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63e4830-2118-3463-8c7c-1ba7d92c3add | -10.62367 | -53.90216 | 2026-08-16 05:16:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e6d9188-ecb5-3268-9e48-d28f9bd1dedd | -11.07735 | -47.2569 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 80dec94d-fac8-3271-9d41-6258130c4fc3 | -6.85085 | -56.43795 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b30da44-b217-3a71-b5c1-1029d9274bc9 | -6.86578 | -56.40828 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a0ef5d0-f8e4-3acc-b245-870ba28a91d0 | -6.84752 | -56.43742 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62f0a955-a837-3ede-980b-898f80b6f2bc | -6.10582 | -57.71313 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ef3f76a6-0df3-3b37-b147-c1e2c9daa196 | -8.98051 | -60.52439 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 90307b20-92c1-3772-9a93-d832f4b0d575 | -6.1154 | -57.7141 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00920a8b-94ed-3732-b94e-87b54af698af | -8.94565 | -60.52323 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3baa945c-5cb4-3a34-9f45-2a933e35ed86 | -12.03914 | -46.44805 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a811a538-0bb1-3780-80e5-7c75fa190c7c | -6.11728 | -57.70742 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0c4445a-ddcf-3beb-a9cf-a3fea72dbe55 | -8.89691 | -60.5649 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0e5f700-240b-3036-9ddf-27c8d2adc8ff | -6.40134 | -45.69061 | 2026-08-16 05:16:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86d25ea5-66f6-38ce-bd02-19b692c5ffb0 | -11.46138 | -46.59735 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff904711-1d48-3935-9da6-ef0172492c8d | -8.42607 | -62.67075 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bd1aa4d-6d57-3b0c-8c9a-a34777afc36c | -6.86533 | -56.42952 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a40331c-5aee-3e9c-b2a5-d78b8029c8fe | -6.8608 | -56.41817 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8448bdc-97d6-37fc-9ead-dcbf84124e62 | -9.42337 | -60.33026 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cf71318-9900-386e-897c-2f499fb675e3 | -8.97071 | -60.51321 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c8ca26da-ffd6-3a8a-942d-3e65da8be330 | -6.61145 | -56.34586 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51ca8da4-9279-3d48-af03-023dca803b6c | -12.24007 | -47.00875 | 2026-08-16 05:16:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8581814f-1dc0-3850-ba4e-81fbee275e5f | -6.68985 | -59.0725 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1d99490-6904-3ab6-8d75-cba754f6b05c | -11.20732 | -54.81311 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a651ba67-90e5-3d0a-8abe-1705862f0207 | -6.85796 | -58.97668 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e4f11d5-dc99-3c62-aba5-252ac73f662a | -8.89606 | -60.59357 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5c947b6-e190-3828-9486-78843a370664 | -9.26137 | -56.90379 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea16a53a-8fb4-3e2f-8d39-1f5f8abbe30b | -6.84309 | -56.42247 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7fd9caa-d2a5-3688-84bc-49da943147ff | -11.48521 | -46.59344 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c32f3a7-8808-3d25-90da-d5fa8ea41e67 | -8.97216 | -60.52776 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0ea1bf5b-6ca8-3a80-9f0e-58befbf76d07 | -8.90056 | -60.55865 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10af2efd-2d15-3cdf-9e50-b374d2a714e2 | -9.26912 | -56.89787 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd520eeb-1530-363f-95c2-8db30ca4d7f0 | -6.62502 | -59.05449 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2704f280-71bd-3169-87ab-b42d57209346 | -9.19814 | -59.67049 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9001895a-c3e6-335c-837b-d835252335ae | -8.65569 | -54.73593 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f353c5cd-fb88-34b0-8a63-b912d61de53c | -6.84856 | -58.9667 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5add26eb-e851-326f-8eae-9ac4be7adbe3 | -6.70942 | -58.93192 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b4fa446-7412-3493-b714-768bf4279560 | -8.89377 | -60.55269 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8278c6af-8a7e-309a-85c3-96034ec829d2 | -8.62244 | -63.73089 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2326f40a-fbc0-30b4-8761-d23194fbeffa | -6.85572 | -58.96788 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf870a9b-8629-3408-801d-40d30d2b64d9 | -12.00687 | -46.41662 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1908736-fc7a-369a-bc9d-8c1ab6372b4d | -11.10182 | -47.24248 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 098a31f2-e24d-3891-a75b-2815164000d8 | -9.97766 | -53.94134 | 2026-08-16 05:16:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cd03e9a-b9ea-3064-b4f5-bd39e02b30ab | -8.95658 | -60.59708 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| febecfca-9f27-3182-a82d-3b56c93f9d63 | -6.82981 | -56.44173 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1bd5ab2-4581-3421-9226-eeb87cacb596 | -8.02366 | -55.14069 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac1e9ce-5666-3845-af68-f8e0924014ff | -8.79552 | -47.92731 | 2026-08-16 05:16:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d237c19a-63bd-3607-a3c5-4947127d50c2 | -6.81873 | -56.44711 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0dc37728-9fbe-3e4b-bcdc-159783ca728a | -11.22001 | -54.82301 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21065496-2847-3673-a7a1-a39828868e9c | -11.62198 | -51.09517 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b21a6cdc-8b58-3403-b947-617ddf8610c1 | -12.45883 | -46.65268 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe54068d-471c-3e8a-853e-d64d6035c378 | -6.7074 | -58.94412 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 584bbf01-d6dd-3587-8c08-4f9d71c9b8ef | -9.46537 | -60.54029 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f02e1f21-6a6b-3557-972a-9553aa43eac8 | -8.89216 | -60.56205 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a946cc52-7365-36a1-b1bc-fb88e7f9897f | -6.36623 | -44.36469 | 2026-08-16 05:16:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 183e07b5-4f66-3e2f-9c14-2c23f557b550 | -6.93071 | -43.63389 | 2026-08-16 05:16:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc965f6-bb47-3aa7-ae74-f19e4e197921 | -7.55282 | -61.16959 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2ffb291-d009-3fb7-82ff-0e2d82db3861 | -6.8593 | -58.96847 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17d454d4-70bb-318a-ac23-57a8d887d622 | -12.03382 | -46.44243 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 25c60bee-a1dc-31f0-b82d-8abd2c163051 | -6.36532 | -58.3246 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f11684a2-26c3-361f-a6a3-efc13e57a7de | -11.82453 | -51.7991 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91b44e6b-c0f9-3be9-a811-c95d1799fc2c | -6.62456 | -59.08005 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README38.md)
