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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12d63089-5bbd-3b91-8597-3879ef3615cc | -15.4071 | -47.901798 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10c02ae3-41c1-3909-8954-4565269250a5 | -15.1103 | -53.875599 | 2026-09-28 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef8cb627-d4e5-38a7-a163-2c6645b6a07d | -4.0405 | -54.220402 | 2026-09-28 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90b8720d-662b-3a3d-b022-9a6610973afc | -3.576 | -54.353199 | 2026-09-28 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 942b0c99-c940-3535-8568-ce262ef638a4 | -8.9611 | -44.167 | 2026-09-28 00:55:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 919a2f02-2f7e-3ba6-a6c4-178e1c6a22c7 | -9.0831 | -49.874599 | 2026-09-28 00:55:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 227c305f-9df9-3943-82e6-29b4ff16ae7f | -13.8496 | -46.936501 | 2026-09-28 00:55:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9cfa1045-c5c0-3a8e-a6d4-27b2b951be91 | -13.6991 | -48.811001 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dc18fa50-fee3-3309-a6be-f3bec501502f | 1.6641 | -55.919201 | 2026-09-28 00:55:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8992405-f8ed-38af-8aaa-733b4e5def1a | -11.2799 | -43.547699 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ba4ddd2-e95a-36ec-a59a-0d42d65f12ec | -9.7794 | -44.833 | 2026-09-28 00:55:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fe1e9b3c-ff1f-3e45-856e-49b0589f51f5 | -8.2916 | -49.5835 | 2026-09-28 00:55:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ec0470-b6d0-3c63-8c6e-a6920fca1877 | -1.0444 | -53.5686 | 2026-09-28 00:55:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7cdc947-d630-3cf4-ae58-239c9a43ea0e | -10.4063 | -53.817402 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7e1f8e0-dc0b-3daf-8a07-58922c4998be | -15.2677 | -47.621498 | 2026-09-28 00:55:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 26e3f3c5-a0f1-3863-bc23-7c0195798fed | -12.2644 | -50.410099 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07cf6010-46c9-38aa-a55a-566a98cd9ce2 | -1.7383 | -57.180099 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8614d07-b970-31f1-99ff-2f7d4218474c | -21.3922 | -48.710499 | 2026-09-28 00:55:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f6a2d589-73a1-36a5-9033-af4f17a802a9 | -10.8918 | -50.679401 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 271f3f65-1e2b-3278-83ee-e068af7c9203 | -10.8875 | -43.6688 | 2026-09-28 00:55:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2abbb473-d73e-362a-abb3-668b18e952a2 | -3.2054 | -51.046001 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29804478-64de-3d0f-b39a-2ca96ced719a | -15.1085 | -53.867199 | 2026-09-28 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40c05748-b0b5-30ef-aaec-0391d5079705 | -3.5099 | -50.316799 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3962d686-c64b-3150-9ee0-d0a482086e37 | -7.8687 | -61.187401 | 2026-09-28 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0c4783b-b7bb-38cf-b34e-f9e19f5bbad2 | -11.7024 | -44.551498 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6cbf8ed-6d35-30b5-82dd-3e63c5778532 | -11.236 | -44.791698 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93fc7087-9f2d-3b74-930c-18109bc0bc75 | -11.5307 | -47.356899 | 2026-09-28 00:55:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58db825d-6e70-3064-a944-2e87815b01c8 | -2.6641 | -51.736099 | 2026-09-28 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ccc0762-1dce-323f-8aac-a1a82c301a0f | -21.516701 | -45.101398 | 2026-09-28 00:55:00 | METOP-C | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 55373e13-25e1-3a64-9def-648381f519c7 | -9.9734 | -45.3596 | 2026-09-28 00:55:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ca56b3db-b656-32d5-a0aa-1da039cc0b19 | -11.1804 | -44.776402 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9bef570-6ea7-38e8-990c-5f333e2a167f | -3.2927 | -50.3144 | 2026-09-28 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0cfc3c-525f-3682-bd5b-86575d26f30e | -20.197201 | -48.582802 | 2026-09-28 00:55:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f657ac1-3497-39f6-9c12-09284df3e73d | -11.0988 | -51.355301 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b532b7f6-6834-3ea7-b772-ca2eb3cb7df7 | -2.2639 | -57.002201 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a15cf1dc-6421-33a5-a213-52e4aa215083 | -11.711 | -44.503899 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03aad1d5-ebb9-3849-a7a4-af1e1d9ec35c | -15.1541 | -43.598499 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| aabd3615-ff29-3234-8ac6-10701459aa91 | -14.485 | -53.634899 | 2026-09-28 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3075bd3-a512-3fa9-b38b-6112ebfc21e3 | -13.3811 | -51.326199 | 2026-09-28 00:55:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd410fe0-932b-3784-bcfe-917429576e80 | -2.9292 | -56.578701 | 2026-09-28 00:55:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf44f51-f4d8-361d-8095-e374a088b5ad | -23.7626 | -51.919998 | 2026-09-28 00:55:00 | METOP-C | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f454d9f5-71e8-3d36-a65b-c1d939fafaa7 | -15.112 | -53.883999 | 2026-09-28 00:55:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecfa91a7-0986-363c-9d2f-4fdfbac5f6c9 | -13.4152 | -51.3405 | 2026-09-28 00:55:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29ba9cc2-ca99-3abb-bb56-0d892a56b94c | -10.4178 | -53.822701 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b528d9f-9dbb-3137-a225-80ef5ee5cc44 | -5.6442 | -43.739399 | 2026-09-28 00:55:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dcddd90-c425-3ce9-9d01-4a72dccb30cd | -14.7237 | -45.569698 | 2026-09-28 00:55:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 571c8421-7a7c-38c5-b593-90e99df2be2b | -10.9463 | -43.897999 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45765155-cfc9-38ce-94f5-554dcfba8c6f | -2.8646 | -49.629299 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8d57076-adc9-390b-8892-b3dd84a9754e | -11.4492 | -44.939999 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84ca1c61-2a50-3b8a-a077-6c5f3f3fb25e | -11.3838 | -43.430099 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29077ddd-9fc6-3a12-b8ea-fa96a08daf59 | -10.9114 | -50.674801 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6124f8a3-88aa-31a2-a314-e33398ab0f84 | -13.4168 | -51.3475 | 2026-09-28 00:55:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41b02833-0329-3fa7-8389-4f79d46ba19b | -9.9849 | -50.153198 | 2026-09-28 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a044e9fc-6437-3056-9dac-e1a15f4d210e | -7.8214 | -55.1423 | 2026-09-28 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5b22390-04aa-3799-b859-ee4f597a53ad | -7.855 | -61.1707 | 2026-09-28 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b79e0227-ce74-3733-b1e8-7bc2dd7b4628 | -11.3953 | -45.383202 | 2026-09-28 00:55:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cafb75cf-d161-3d91-bf0d-ef9057934470 | -15.1794 | -46.1525 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c28545b6-cece-3961-a051-b5ba9ec77189 | -1.1051 | -54.191601 | 2026-09-28 00:55:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9872a44-dd9c-3e08-88ea-dac3d815322b | -22.346001 | -46.959801 | 2026-09-28 00:55:00 | METOP-C | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b85601ad-1cc5-3e12-8384-93a08dd99e25 | -15.1697 | -46.154999 | 2026-09-28 00:55:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a64ef076-32be-3600-a089-5e167ff806d0 | -2.9129 | -54.203999 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee9e26d9-0fa6-3a53-9dfa-6c2354b2ce66 | -15.1579 | -43.612801 | 2026-09-28 00:55:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| b1536a15-eace-3156-9248-526e957813cc | -9.9798 | -45.343899 | 2026-09-28 00:55:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0fb411-af07-30d6-ac75-1027a7d81dd5 | -12.15 | -50.3619 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7590444f-c07b-364c-b79f-0eff8de5c100 | -11.2038 | -47.714298 | 2026-09-28 00:55:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 087dda44-4c7b-35a3-9ae8-23da04aa18af | -2.7693 | -49.486801 | 2026-09-28 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94fbbaa2-cad4-363a-aa0b-257bf73a181d | -10.913 | -50.6819 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8383a6e3-be20-3ab2-9481-761ab9261a0a | -2.6624 | -51.728802 | 2026-09-28 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdec537d-e35a-3ba7-9f7a-3809d5013243 | -2.9153 | -54.124199 | 2026-09-28 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03aaba90-3fc5-3d72-aff5-ab253cdcf50f | -3.2134 | -51.035999 | 2026-09-28 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab84e57e-a8f7-318f-b29f-1c6f00c67177 | -6.7022 | -45.646 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3315f602-e2b1-33c7-bdb3-416687cb85ee | -6.7013 | -45.600498 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f77fb2b-77f3-3f44-864c-014a7027b8ab | -6.6925 | -45.648399 | 2026-09-28 00:55:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5bf1d8d-33d1-3e04-bd1a-fcdddd15e796 | -11.0924 | -51.327499 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5cfc746b-1c30-321e-a371-3079dfa5c558 | -11.7121 | -44.548901 | 2026-09-28 00:55:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a82d4089-cd37-379f-bb1a-d56acadda535 | -10.825 | -57.229301 | 2026-09-28 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4236002d-8098-37e8-8935-f09031ff393f | -3.3603 | -50.471199 | 2026-09-28 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45ddcd28-b3fd-34a1-83e6-a2ce398f0fe7 | -11.3794 | -43.413101 | 2026-09-28 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 880ef6f8-9269-351d-bc86-2ef0e4f466c9 | -14.5215 | -48.310001 | 2026-09-28 00:55:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c59463b6-bcab-3018-b97b-523b3e904264 | -8.0179 | -43.737701 | 2026-09-28 00:55:00 | METOP-C | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ef3b8ca-1f5f-37e0-aadc-d72267fb0765 | -10.9163 | -50.696098 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e70999ff-8bfc-38ab-9227-2eb2e11e5fb2 | -12.3049 | -50.272598 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76cd20bd-3b01-3f81-a7e5-777f2948f118 | -10.4545 | -45.094501 | 2026-09-28 00:55:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd716a6-b51a-3290-812a-91d7f8b56489 | -21.137699 | -48.5877 | 2026-09-28 00:55:00 | METOP-C | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6e866cdc-0304-3a7a-a106-441ce3100bd9 | -3.1507 | -54.071701 | 2026-09-28 00:55:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33ad6bbb-574c-3665-a691-da26b09bcea0 | -12.69 | -47.317101 | 2026-09-28 00:55:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97ff5c50-cb71-3e24-9df7-b1becae3c832 | -10.9147 | -50.688999 | 2026-09-28 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eea31c60-e68f-322d-b6f6-71b7d436c833 | -8.1446 | -44.444 | 2026-09-28 00:55:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b2af056-e3ef-33ea-9353-ee1554cbdf58 | -12.1957 | -50.381199 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9389a1c-1138-3c58-bea1-2026d36e458a | -10.7083 | -44.422298 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e73e168-6f78-3e57-a7dd-44d010c6d245 | -7.6836 | -54.846802 | 2026-09-28 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2752b6-d09d-37a9-beb6-7c24195fc6d5 | -7.8647 | -61.168701 | 2026-09-28 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a039217-6604-323c-a82e-070cff0411db | -3.4249 | -48.332199 | 2026-09-28 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b908c15-0b05-3467-b0e4-9ea30259e1bd | -12.639 | -47.32 | 2026-09-28 00:55:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50a3547e-2f57-38f1-bba5-1f89b27bd448 | -21.028799 | -47.257599 | 2026-09-28 00:55:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4b8eee04-4702-3325-a376-2a9003bb611c | -12.1974 | -50.388302 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54299e16-b8f5-3ee0-984d-2c0b00a89c47 | -11.2007 | -44.815498 | 2026-09-28 00:55:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f341153-0de9-3d11-ae1c-8bc152a22163 | -10.4161 | -53.815201 | 2026-09-28 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2231ed3-daf5-3847-900d-5cf7469ac862 | -2.1142 | -56.887501 | 2026-09-28 00:55:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe782fc2-3aa8-3a9c-be47-c75af4db3a3f | -12.1811 | -50.362099 | 2026-09-28 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
