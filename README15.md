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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 423c430e-262b-350b-ad20-13205ffe291f | -6.0418 | -44.6076 | 2025-10-03 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 02fb1ef3-28b1-3013-b5f4-08988b9d8c51 | -7.7749 | -42.5628 | 2025-10-03 03:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 74.9 |
| bbb0bbf6-f01e-3c6a-a66c-8b94ac9fb6ae | -8.798 | -46.6616 | 2025-10-03 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| e8933bb3-383b-361e-99c1-0d84bf34711c | -7.7746 | -42.5865 | 2025-10-03 03:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| c907321e-d512-3f6d-9442-ee3b2004b317 | -7.7682 | -46.2703 | 2025-10-03 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 85c85227-bde9-327b-a971-15224ca61656 | -4.6504 | -45.8077 | 2025-10-03 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 302.3 |
| 7260aafa-3390-3a1e-9775-f801779521ec | -6.0603 | -44.629 | 2025-10-03 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 573d6784-21e0-35c2-93e9-9017315ed966 | -4.6689 | -45.829 | 2025-10-03 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cdf77fa8-35bf-35d4-b780-e14235afe698 | -7.7684 | -46.2479 | 2025-10-03 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 87ab1dbb-d4ed-30f0-9643-eaff6cdc059f | -12.6319 | -46.9923 | 2025-10-03 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9eff8aa7-1d3e-3e8b-b57e-f481ee044922 | -6.0605 | -44.6061 | 2025-10-03 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 5e1f8d64-c4bd-3a4e-a3e8-cedf7d4c9ffc | -12.6131 | -46.9725 | 2025-10-03 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 948a4d84-757a-338d-9bea-7362eaab815f | -13.776 | -47.5843 | 2025-10-03 03:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 775feb24-6139-3050-bbcc-290e6469b594 | -13.1341 | -47.9043 | 2025-10-03 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f9b6a0fe-8595-30b3-b8cb-67251f4a9b30 | -7.7494 | -46.272 | 2025-10-03 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 9140b762-b42f-3fb1-9e74-c1ca60945874 | -10.912 | -47.0458 | 2025-10-03 03:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| c42acbf5-c5ac-3eb7-87ca-b98800c595f4 | -6.0416 | -44.6304 | 2025-10-03 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| dc1401a9-f771-3bfa-97b4-87b6933a0145 | -13.1345 | -47.882 | 2025-10-03 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 431c687e-3aef-3a9a-9b52-bb0a5ce9ba0a | -7.7499 | -46.2272 | 2025-10-03 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 808df25d-49af-3c1e-92f8-e49165376172 | -11.9163 | -46.2817 | 2025-10-03 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0ce06fd3-01e5-3996-bb86-b6dceb3ad370 | -13.7764 | -47.5617 | 2025-10-03 03:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 42c0fae9-b419-3023-a47e-fd2e4cc3696d | -14.9342 | -46.8965 | 2025-10-03 03:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3badc4e7-b8b4-3cac-8a3a-6ee309d4dbcf | -12.6323 | -46.9697 | 2025-10-03 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 72f59f8e-3af1-3547-8a90-1f2bbd4ae81c | -12.6127 | -46.9951 | 2025-10-03 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a2a7d86b-62b4-3224-8f4f-0d2c96e5768b | -4.669 | -45.8066 | 2025-10-03 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 521.5 |
| edd1568a-1c69-3fdd-b794-50775d6f1a6c | -8.6138 | -54.976 | 2025-10-03 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 2707695c-e6cd-33f4-b320-cf45d54a0503 | -4.6505 | -45.7853 | 2025-10-03 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 342.1 |
| 47017bac-f721-3c18-a2bc-72ea2495a2cb | -7.7496 | -46.2496 | 2025-10-03 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 288.2 |
| d3958304-4619-380d-a0cb-a9702af339c1 | -9.9182 | -43.7212 | 2025-10-03 03:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 49b606a9-72fc-312a-9a68-2c931f768464 | -13.1152 | -47.8848 | 2025-10-03 03:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 4bf32abf-989f-3cef-becf-a670b93007f1 | -4.6692 | -45.7842 | 2025-10-03 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 517.2 |
| 53138192-94e0-3384-86ba-dffb53a59294 | -6.0605 | -44.6061 | 2025-10-03 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 396d6133-559e-38fa-8e9e-15abe286d297 | -11.9163 | -46.2817 | 2025-10-03 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e6ef59b1-df52-3a86-ad95-6620fd20611c | -5.6363 | -43.9027 | 2025-10-03 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| e68f28a0-cafb-38e2-bd34-5c255039dbd4 | -13.9775 | -48.157 | 2025-10-03 03:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 102.7 |
| d8b2c66a-ef9c-3679-88d1-8893dc224554 | -10.8929 | -47.0482 | 2025-10-03 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 23890fc4-d07d-3b69-bdef-ae9a6a6828f7 | -7.7496 | -46.2496 | 2025-10-03 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 403.6 |
| 122385ef-296f-3a11-9364-bf920c7e9f65 | -10.8735 | -47.073 | 2025-10-03 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 25acbe0d-3515-311f-b699-af27a22ed469 | -10.8739 | -47.0506 | 2025-10-03 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 230.0 |
| d14d6794-a49a-3f65-a856-e473fd6cd135 | -12.6323 | -46.9697 | 2025-10-03 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 53d46b31-cefc-35af-9fcc-9c63595afdb7 | -7.7746 | -42.5865 | 2025-10-03 03:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 47df70c8-429d-3ae4-a0b1-8925ed8c5755 | -13.7764 | -47.5617 | 2025-10-03 03:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 70d126b8-290c-302f-97e0-96d86dbeb1b8 | -7.756 | -42.5648 | 2025-10-03 03:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| a087a661-b25f-35f9-a751-12c3df1f6ca1 | -7.7684 | -46.2479 | 2025-10-03 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 5adcb68b-7985-3a20-97f5-219e8c32a95d | -13.1345 | -47.882 | 2025-10-03 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 48ce2060-0e6c-3d99-8298-89319176ce21 | -13.3418 | -48.1188 | 2025-10-03 03:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| cbddfde6-032e-3aee-8f2e-4d091c032200 | -14.9342 | -46.8965 | 2025-10-03 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 23e1ab4a-62e5-3f87-8c55-218fdf77e8df | -10.912 | -47.0458 | 2025-10-03 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 6f699f39-6db9-3ad7-b446-1b224123cd8a | -13.1341 | -47.9043 | 2025-10-03 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 21b58e48-68f7-39a8-904a-e9ce858e4be9 | -7.7499 | -46.2272 | 2025-10-03 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f04d1fd8-7274-3957-b000-0e64b9aa20a0 | -6.0603 | -44.629 | 2025-10-03 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 331a6f34-5a17-3ae8-8888-72c1d72297dd | -12.6319 | -46.9923 | 2025-10-03 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 23736e38-9987-3660-9e81-373ebbbf53f4 | -4.6505 | -45.7853 | 2025-10-03 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 254.2 |
| bf491e5d-0ccb-3e75-b506-3c954bb7c18f | -6.0416 | -44.6304 | 2025-10-03 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| fc88d716-8390-35c0-aa43-fd34fef5cf4e | -4.6504 | -45.8077 | 2025-10-03 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 310.1 |
| 6e18e8de-245d-398d-b8c2-7571d6ad0274 | -7.7682 | -46.2703 | 2025-10-03 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| ade08cbf-ba13-334e-a1c0-5020b8935021 | -13.9771 | -48.1793 | 2025-10-03 03:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 0a10dab7-a015-33de-b04c-35ec5ca60ab5 | -4.669 | -45.8066 | 2025-10-03 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 463.9 |
| c96c5310-626b-33db-86b1-3ac511a0c93c | -5.6361 | -43.9258 | 2025-10-03 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 697dfada-39aa-3849-aa64-2420fdf33147 | -12.6127 | -46.9951 | 2025-10-03 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 6632f03d-60d3-3ef8-9608-b70d1fa2dabf | -10.8742 | -47.0282 | 2025-10-03 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2ebebe89-9a3c-346f-ba0a-c8d7e47f4309 | -12.6131 | -46.9725 | 2025-10-03 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c9fe7297-face-3732-94c5-683bedeb38ce | -17.8614 | -57.623 | 2025-10-03 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| a9b8e10c-6d51-3ffa-baa4-e93af423a94e | -7.7494 | -46.272 | 2025-10-03 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 744355d1-7593-3724-a2ac-6184bdda3066 | -4.6692 | -45.7842 | 2025-10-03 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 326.5 |
| 75deb2aa-d675-37b5-b874-5dd6d6787c65 | -13.776 | -47.5843 | 2025-10-03 03:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 59b525d9-ffba-3050-a02e-efb752bc5d10 | -8.6138 | -54.976 | 2025-10-03 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 14a103e0-334d-3745-a517-2f8ddc2539ae | -13.7769 | -47.5392 | 2025-10-03 03:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f7671fd6-ea55-37d1-a092-aa67a5e97d07 | -4.6505 | -45.7853 | 2025-10-03 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 242.1 |
| a37f7efe-89e9-334f-ad06-7cbe031c3c25 | -12.6323 | -46.9697 | 2025-10-03 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ca27da95-95c2-3c6d-8ae8-e842db111b0b | -4.669 | -45.8066 | 2025-10-03 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 413.9 |
| 5e36e49b-f59d-34ed-8cfb-81784067a93e | -10.8982 | -46.7117 | 2025-10-03 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 451f3e29-2454-359b-9bf1-3fc56057508c | -7.7499 | -46.2272 | 2025-10-03 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 48be59b5-0fe1-33ee-aada-6043a9abafa9 | -4.6692 | -45.7842 | 2025-10-03 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 318.7 |
| 5bf11eb9-fadc-3e5b-aa47-a8fa6c8e286e | -6.0605 | -44.6061 | 2025-10-03 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 767d00d0-eb4a-3dfc-8c90-9eba9e7896e6 | -7.7557 | -42.5885 | 2025-10-03 03:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 5498f739-5618-3417-bc7b-480d19b697bb | -4.6504 | -45.8077 | 2025-10-03 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 263.0 |
| 2ea5878d-082c-3a58-ae3f-25d7b64e4a7d | -7.7746 | -42.5865 | 2025-10-03 03:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 8286b82c-e51c-3f43-b90a-d4d2ef290218 | -10.0148 | -50.2443 | 2025-10-03 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 961ace82-babe-3feb-9c1e-4055dfa482c1 | -12.6319 | -46.9923 | 2025-10-03 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e3ab2240-664b-3ad9-ad5b-828d8ca23177 | -14.9342 | -46.8965 | 2025-10-03 03:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| bcbee2b4-6069-3949-8fc6-80f56d1fd59a | -7.7684 | -46.2479 | 2025-10-03 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 246.9 |
| fe998775-1b9e-34b7-a77f-99b65a6a6a0d | -6.0416 | -44.6304 | 2025-10-03 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c8d2edba-1ecc-3a32-9706-2e6a285adca6 | 1.5285 | -55.8454 | 2025-10-03 03:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 70b988b7-9174-3a5c-954c-6e6781c9bab9 | -4.6689 | -45.829 | 2025-10-03 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0ba5dbe8-4291-3303-a0ab-1834bf1a22cd | -6.0603 | -44.629 | 2025-10-03 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7771d345-f720-32e4-b55f-b2aae3ee9cfc | -7.7682 | -46.2703 | 2025-10-03 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 236.2 |
| 765820df-b003-3edb-b0af-38770cfb58aa | -8.6138 | -54.976 | 2025-10-03 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| a1af9deb-632b-3b4d-8ade-51d3e7440948 | -5.6363 | -43.9027 | 2025-10-03 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 00992dcc-6963-342f-94fd-7eeff8831010 | -7.7494 | -46.272 | 2025-10-03 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 512.9 |
| d377115e-123c-3f6b-bf52-b52b3a685a55 | -13.776 | -47.5843 | 2025-10-03 03:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 283decae-9def-3319-907e-034590d4653f | -13.7764 | -47.5617 | 2025-10-03 03:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 87bcc7f9-72a3-36d2-af41-69c62d7cadd1 | -13.1345 | -47.882 | 2025-10-03 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 91af46e7-3745-30cf-bf80-ba79c2b0a4f3 | -10.8739 | -47.0506 | 2025-10-03 03:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 0d45a5bd-f171-39a3-a2e3-a2c1a1843f15 | -12.6127 | -46.9951 | 2025-10-03 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d486c299-14ef-3eeb-88b3-a1c7962677f7 | -11.9167 | -46.259 | 2025-10-03 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 58098666-d04a-399d-b6ba-c27c471cc50d | -10.8608 | -46.6715 | 2025-10-03 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3d747ac5-fa82-3144-8ff7-676efbcc0685 | -7.756 | -42.5648 | 2025-10-03 03:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| ef205fb7-72c6-352a-aa2d-0ff4860aa8c8 | -12.6131 | -46.9725 | 2025-10-03 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 7e0536a9-f64d-3d7c-99fe-ab2930562ca3 | -7.7491 | -46.2944 | 2025-10-03 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |


[Clique aqui para ver as próximas entradas](README16.md)
