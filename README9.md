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
| 4ec7aa62-6f72-3f0b-9d83-3fcadc1b3fc6 | -11.82083 | -47.09321 | 2024-10-24 01:24:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b9f332d6-5c5b-3509-8b05-f896455f1ca1 | -11.81651 | -47.06833 | 2024-10-24 01:24:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 9e245127-610d-32be-8a72-a2c39dfd1b35 | -11.78469 | -47.08109 | 2024-10-24 01:24:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 101e529e-f881-3700-8a3c-1dde0a46ba10 | -11.66372 | -48.80412 | 2024-10-24 01:24:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0fccf624-4343-3ca4-bf92-1715cc17c604 | -11.66132 | -48.8102 | 2024-10-24 01:24:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| be268c90-84d0-3893-9b1f-69a26d235162 | -11.60711 | -48.54084 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c2637929-e29a-308b-b365-42be5b5ebc65 | -11.60668 | -48.54654 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b23dbb1f-48f3-36b0-8e43-0b2ec6959e38 | -11.59776 | -48.56234 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| d5758bac-ca6b-318f-8190-c183afef0bc8 | -11.59717 | -48.56802 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c22a514d-b759-3a60-a195-f89df97e6077 | -11.5945 | -48.54298 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| bf456fef-107b-3f2b-a46d-645ec29e9810 | -11.59406 | -48.54869 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| f902cf56-44b2-327f-81bc-3816e4ceecad | -11.25572 | -48.72435 | 2024-10-24 01:24:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d8ccd98c-9067-39a4-95a5-ea8fe88d6670 | -11.12188 | -51.9215 | 2024-10-24 01:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 30e8a489-88fa-3c0a-b4cc-478bcc992b4a | -11.02741 | -48.29089 | 2024-10-24 01:24:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 6477306b-12f0-314c-96b6-4b123b138704 | -11.02471 | -48.28548 | 2024-10-24 01:24:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 36ea1c1c-0654-3314-b4fd-4e96ba765233 | -11.02399 | -48.26933 | 2024-10-24 01:24:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 26f163e7-9675-30c4-af3f-9fb29dc5d5ba | -10.97828 | -49.30655 | 2024-10-24 01:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8ff2a70d-1c53-3921-bb1f-950e9177b059 | -10.89865 | -47.91617 | 2024-10-24 01:24:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 31ce1025-2fd8-311c-8d7f-50f46f5f0bec | -10.87735 | -49.14253 | 2024-10-24 01:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8b9062ca-83e8-356f-b80e-f9eb3597b50c | -10.87437 | -49.54071 | 2024-10-24 01:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0d92c0d3-3554-3ec7-a048-4db38a7d8b67 | -10.8739 | -49.14971 | 2024-10-24 01:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b5793049-74a0-3e31-853a-21dc4c131a1a | -10.688 | -49.11208 | 2024-10-24 01:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 49296ced-3818-3640-9b68-476ace55061d | -10.68517 | -49.11921 | 2024-10-24 01:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 13905f45-4b11-3d30-9f5e-f9f1fdcb0080 | -10.518 | -51.85371 | 2024-10-24 01:24:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fb208449-0357-389d-8bb4-08fe560104a3 | -10.51627 | -51.84219 | 2024-10-24 01:24:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 30662368-ff2c-3565-9199-ae2648c724ed | -10.47607 | -48.2921 | 2024-10-24 01:24:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 83057eca-f0a1-30d5-ba68-26df210baf4d | -10.47263 | -48.28709 | 2024-10-24 01:24:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| e1727f45-6394-3c3e-982a-e56a0e638c4d | -10.41654 | -47.52251 | 2024-10-24 01:24:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 49d43498-f3cb-3969-a3af-df4425d55109 | -10.36659 | -51.39059 | 2024-10-24 01:24:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 357bb585-d0f8-3662-b682-c6021d7fe206 | -10.30972 | -51.89922 | 2024-10-24 01:24:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a3fce9a-e77b-3a80-8dfd-fe8ccc243423 | -10.30794 | -51.88751 | 2024-10-24 01:24:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8f408318-7d66-3680-ad8c-948a3781cbd2 | -10.19771 | -53.88145 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a1bfd795-826b-36ed-afb8-de43d269cc4c | -10.19638 | -53.87212 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f907abc2-fdb4-3dbf-a997-cfee82f2b8de | -10.18868 | -53.8828 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b008bf69-26a7-396b-b3b4-23784f6ad4cf | -10.18735 | -53.87346 | 2024-10-24 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8318aa56-66df-319a-afc7-4dde21d036b0 | -10.09937 | -51.12894 | 2024-10-24 01:24:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bdeea0ec-3563-3727-a2bc-7663c272f6e0 | -10.0103 | -47.46323 | 2024-10-24 01:24:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 76060b91-12ec-38d6-b765-5056a417457b | -10.00611 | -47.43782 | 2024-10-24 01:24:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 2ee2f71e-ff1a-3514-866e-c3c46171c6a7 | -1.4945 | -54.1962 | 2024-10-24 01:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 5bfe1cab-b7d3-3b11-a9f3-64fa9bc8cac9 | -1.4945 | -54.1761 | 2024-10-24 01:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a9fa1b04-a676-33aa-8a6b-b748fe6d3712 | -1.5878 | -53.3089 | 2024-10-24 01:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ef6dda77-e320-39b0-9a66-ff5a376f73e3 | -1.6062 | -53.3087 | 2024-10-24 01:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| b67c5c09-b3d9-3cbe-bc41-da3561f115ba | -2.9578 | -50.4198 | 2024-10-24 01:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3e4e0162-5457-3ab2-9af7-f3c45d572780 | -2.9763 | -50.4193 | 2024-10-24 01:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 132e0571-f466-3ba5-a153-41196fee1ff5 | -3.0745 | -53.8252 | 2024-10-24 01:25:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| b5c33520-f2a2-3b57-a218-e51140b6f91d | -3.1101 | -54.1661 | 2024-10-24 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 30519377-e668-3af0-8709-9db4d1f878d5 | -3.1102 | -54.146 | 2024-10-24 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cfccf834-63d4-3412-b0b9-bc36ef9d6c55 | -3.1606 | -50.4766 | 2024-10-24 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| cfe1eebc-2977-3d98-8298-645ce98e26bd | -3.1607 | -50.4556 | 2024-10-24 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| b4e5788f-e339-3b68-9e8c-327c7edd6a95 | -3.7066 | -41.6997 | 2024-10-24 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| bfef16d0-3851-3b1b-851b-00a17e81df41 | -3.7068 | -41.6758 | 2024-10-24 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 322c36fb-354a-3c05-bb8c-3f5e74958ef2 | -3.7254 | -41.6987 | 2024-10-24 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 044628ec-bdad-3a23-8a59-ba698477ce08 | -3.7255 | -41.6748 | 2024-10-24 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| c08fe0be-3469-3c8a-9671-d6c8c985fa18 | -3.6612 | -54.2715 | 2024-10-24 01:25:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 8d21399a-9f6c-3f00-83c8-f01eb16c6aa7 | -3.9396 | -46.4229 | 2024-10-24 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c9b0553a-bd0d-3957-964c-19b7c099a467 | -4.6588 | -44.61 | 2024-10-24 01:25:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b646f825-369a-329e-8aa1-361768ddb187 | -5.4373 | -47.6833 | 2024-10-24 01:25:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8cd98af3-ed02-3f5c-854c-48148f691f9e | -6.7238 | -40.4754 | 2024-10-24 01:25:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 082b56ae-3247-3458-b98d-1e31c3ca27e9 | -6.7427 | -40.4735 | 2024-10-24 01:25:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 87182721-ba22-3f11-82f5-ddf226ae637c | -6.9272 | -40.8466 | 2024-10-24 01:25:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 34a235d2-ed98-3432-a826-551b953719d0 | -6.9461 | -40.8447 | 2024-10-24 01:25:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 94cbab11-b71d-31e2-9ba0-b2485a7b2868 | -7.481 | -63.5577 | 2024-10-24 01:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3e3eafd1-d866-3121-9c2b-fb0a4cb9ec94 | -9.5343 | -40.3282 | 2024-10-24 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.4 |
| cd86a5d3-0e90-38aa-a235-0983432c592e | -7.57095 | -50.72201 | 2024-10-24 01:26:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 96c82fda-e241-38cf-8887-5847d1dcebe6 | -7.56858 | -50.70648 | 2024-10-24 01:26:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 77d5962e-858f-317b-903c-115c7463fb6d | -6.22809 | -50.89346 | 2024-10-24 01:26:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b2af3626-8b00-33a0-bfc9-2b614bf6acae | -6.22575 | -50.87788 | 2024-10-24 01:26:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ce7a3668-59c0-3ff1-bd16-aae211b19473 | -6.2002 | -50.86544 | 2024-10-24 01:26:00 | TERRA_M-M | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 619c00cd-43d4-3a81-8af8-68b846518a90 | -5.84194 | -47.29577 | 2024-10-24 01:26:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| deeff48d-a621-320d-972c-81bc53b505f3 | -5.7921 | -50.16603 | 2024-10-24 01:26:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 44c7ae31-29d4-3d40-8880-78beeb2790b7 | -5.57086 | -49.4093 | 2024-10-24 01:26:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 9d1e41b4-fb97-36cc-9112-f8bbc9b9b770 | -5.56738 | -49.40351 | 2024-10-24 01:26:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 4c49e265-dc32-3062-80e3-f6987838a637 | -5.44776 | -47.69703 | 2024-10-24 01:26:00 | TERRA_M-M | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 12ff44ec-06b1-3b38-8ac9-606770d9ad7c | -5.44316 | -47.66776 | 2024-10-24 01:26:00 | TERRA_M-M | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 0c9fe704-6374-32bd-8bee-bdb314a6275b | -5.30006 | -47.02943 | 2024-10-24 01:26:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f66d5f58-8ab9-392b-90e6-5052e91d4838 | -5.29497 | -46.99651 | 2024-10-24 01:26:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 8f60f42e-df4d-36f1-817f-69326c2f0988 | -5.29259 | -47.02514 | 2024-10-24 01:26:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 75f03f83-d792-3f04-b3bc-7b6c62280fe1 | -4.8712 | -48.20659 | 2024-10-24 01:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 50586eaa-c520-3bc3-8f56-1cf241b90f90 | -4.87092 | -48.21318 | 2024-10-24 01:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| a02561a0-5b3f-37dc-898c-e5f145af4c45 | -4.77143 | -46.41702 | 2024-10-24 01:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 509200a1-9cc8-3236-81ea-40122320c300 | -4.76759 | -46.42418 | 2024-10-24 01:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a63814ad-d29f-3b6b-b340-ef3f3e1ca174 | -4.76182 | -46.38647 | 2024-10-24 01:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 1f8a053c-ff22-391e-932d-06cbe200cb16 | -4.75694 | -46.64581 | 2024-10-24 01:26:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e835b372-3b57-3878-a9e5-f561edd002aa | -4.75179 | -46.65413 | 2024-10-24 01:26:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| d464e6b3-611b-3dd8-8cc5-7d66fbbf1ff4 | -4.7462 | -46.61845 | 2024-10-24 01:26:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 05485e99-0797-33ac-9214-4eb85f663917 | -4.53488 | -55.7492 | 2024-10-24 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac26bc58-a8fa-3e30-b9b0-e577dc838502 | -4.42554 | -55.43253 | 2024-10-24 01:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 29e7fb38-36b8-33bd-bc7e-4f6d189b8798 | -4.27817 | -46.75895 | 2024-10-24 01:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 05d22311-ec29-30c1-b28d-55d3f7d6e064 | -4.25175 | -48.34625 | 2024-10-24 01:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 04038893-dea6-386b-bc4f-703c993d9be2 | -4.25128 | -48.35147 | 2024-10-24 01:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 88237f2c-0253-33c6-b56d-3a9efbe4c720 | -4.23699 | -48.34812 | 2024-10-24 01:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 5b844bad-74c6-36ad-b604-ce3c81298002 | -4.23656 | -48.35358 | 2024-10-24 01:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 6b8a93de-8313-377e-a2a0-64762cad44b9 | -4.20429 | -55.55904 | 2024-10-24 01:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3a19a5cb-715e-3fe0-82ab-abfa883bd494 | -4.20302 | -55.55003 | 2024-10-24 01:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce17bd70-97ab-32bf-939c-b10dd6998ca0 | -4.14756 | -55.15816 | 2024-10-24 01:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c08cfea5-9b6c-37bc-bd47-b444033fc0d0 | -4.14625 | -55.14895 | 2024-10-24 01:26:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| baca7f0f-f091-3b01-9647-279f1506df69 | -4.09796 | -54.29867 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e06bdd3b-1738-3df9-98ac-5200625e1da4 | -4.09652 | -54.28872 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bd6e2758-a570-3965-bc7f-acd41c51a603 | -4.09359 | -54.26852 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1ec69ef8-ece7-3da7-b27a-3a98924611c9 | -4.09146 | -54.2958 | 2024-10-24 01:26:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |


[Clique aqui para ver as próximas entradas](README10.md)
