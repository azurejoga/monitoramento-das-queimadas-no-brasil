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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49150344-c44a-34dd-bb8e-4bb351308189 | -17.0529 | -56.59 | 2026-09-27 14:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 6e4e3616-19db-3caa-881f-52b022dad342 | -10.2635 | -49.984 | 2026-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 509cf0c2-9f9b-3e3b-b9ad-7db21739b82a | -11.9615 | -50.5465 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ada7190e-1442-3715-9e16-a8a3e16b2965 | -7.3653 | -42.1058 | 2026-09-27 14:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 223.9 |
| 4a403723-79fb-31e7-a54d-31984c5fc83e | -11.9609 | -50.5894 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 4854d982-80fd-3f6c-a9e6-bf7fc10d33aa | -10.0162 | -50.1374 | 2026-09-27 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 286.8 |
| 2cb2d858-c683-3e7b-bbd2-230ca4cff7a1 | -15.9869 | -54.9419 | 2026-09-27 14:30:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0fea6549-3c64-3260-a649-2a6c56ffb196 | -11.9421 | -50.5702 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d44b1615-62ab-3144-b7c8-634d27017ddb | -11.9425 | -50.5487 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 4a78e3d2-01c9-36c0-a34a-a0a250f6f306 | -17.0533 | -56.5693 | 2026-09-27 14:30:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 7fe9de0c-f645-3917-98e5-befa8ddd08b4 | -12.8059 | -54.0255 | 2026-09-27 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2d9898c9-faa9-39e9-b834-fa70adc39902 | -12.6643 | -47.3245 | 2026-09-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 3906a21c-b07c-3737-9208-4125834317d6 | -10.4234 | -53.8014 | 2026-09-27 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| efd2c5b8-4ac5-3e38-a1f9-53e74274f5b5 | -11.3739 | -43.3972 | 2026-09-27 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b9482173-89ae-3b27-945d-83c1acc6eafe | -6.2213 | -47.5013 | 2026-09-27 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 0c4b072a-b528-3b07-bbb0-a966015c2123 | -12.6655 | -47.257 | 2026-09-27 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9e898d35-9472-346d-814d-a4a891df0874 | -12.0181 | -50.5827 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 4756ad54-4b1d-332e-8258-50c8c46872be | -12.8061 | -54.0048 | 2026-09-27 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 5bf0b75f-b878-3430-bd23-2b5ad4d2ee83 | -11.9606 | -50.6108 | 2026-09-27 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e4ffba33-9819-3ec7-95aa-8d8d5a1dac7a | -14.3499 | -52.1051 | 2026-09-27 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e3f143a7-2d9d-37c9-8e35-757559ff7519 | -11.2859 | -51.3031 | 2026-09-27 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 3b2d771d-2e8d-396b-a926-22480469f3a4 | -12.7225 | -47.2937 | 2026-09-27 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 273.2 |
| 6ca23c8e-35f6-367a-81bb-a6cc9dd24e0d | -7.4492 | -44.5786 | 2026-09-27 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| fdbe7850-e257-3b8e-a42b-9a2007c84481 | -12.2512 | -50.2974 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4e55635e-60bb-3732-8b0a-acbe6244d5a5 | -10.7114 | -60.7505 | 2026-09-27 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f5e8aaa0-74f3-35c4-9b42-f8e5ecaaac16 | -6.8408 | -43.5021 | 2026-09-27 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| b4fecdc5-ba7a-3513-b075-fd0ee50fa58f | -11.3739 | -43.3972 | 2026-09-27 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 6fcc8b49-036d-3e1d-b453-49b2c135dce9 | -11.9405 | -50.6773 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 7e87d4e3-bdf8-3c17-935e-b200d5dc9dba | -15.9869 | -54.9419 | 2026-09-27 14:40:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 9f2161ab-9289-39c9-be48-05d5746cda8c | -12.0175 | -50.6256 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 00b3e572-5e29-3233-849a-e16568f1f25a | -12.1188 | -50.2274 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 55e7aa06-207c-3842-8a2e-cce72de3851d | -11.8034 | -50.9491 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| be0b01e0-f970-3e76-9439-5f6c37ffc5e6 | -9.2415 | -47.3487 | 2026-09-27 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 5217a105-f1ac-3206-90df-ffe39e42ba63 | -10.6094 | -53.9902 | 2026-09-27 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| dbf64a5b-3a29-3d8b-83c1-610851b386dc | -11.8014 | -49.8129 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| eba20d48-a725-309a-962d-d68c15896a13 | -10.2257 | -49.9879 | 2026-09-27 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 5db30b21-1679-3910-bfee-b09fdd331156 | -12.2703 | -50.2951 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 58c4b3ab-5567-3e92-a9bb-975c3ba45d90 | -11.2307 | -54.078 | 2026-09-27 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4bf2dae9-a55e-33ed-8fe4-6b2d53eadde0 | -10.2446 | -49.986 | 2026-09-27 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 81384b06-1a53-3a5a-a818-6f944819755c | -11.0991 | -54.0285 | 2026-09-27 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6b097daf-0ef6-3a0b-827f-f12887bc8310 | -11.7141 | -50.5538 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 94159c7e-657d-3a4b-a71c-3b68eccf8694 | -12.684 | -47.2992 | 2026-09-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| d703a027-0ca6-3d25-ae9a-3d877259d6f3 | -12.7038 | -50.6499 | 2026-09-27 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 1b9bc608-3be7-3a59-8f96-01118f46ca58 | -11.6989 | -44.4984 | 2026-09-27 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 715a3bbd-bdef-3743-a48d-a28468c68b0f | -11.9202 | -50.7651 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 7ec80024-5f03-3c4a-b438-e3332a7c41c1 | -11.9018 | -50.7245 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d71ca34a-739f-3337-bcf8-fccb30b5628a | -11.2853 | -51.3454 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| bf0682f7-3a51-367a-89d8-6a1f5aa3ce7e | -12.3679 | -50.1539 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bba92552-1d7d-3120-8afc-ac425e095c03 | -17.0529 | -56.59 | 2026-09-27 14:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 4600ffa1-d6fe-3a60-89e2-6d8c667584d4 | -11.2859 | -51.3031 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 34f156c3-946e-3ee6-b9aa-c24850dfb8ea | -9.7874 | -44.8289 | 2026-09-27 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| a6f43da4-93fc-38d0-a75a-94d5ab5f2df1 | -11.2856 | -51.3243 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e471c975-4a74-3671-aae0-c5edb191a0b0 | -8.5984 | -54.6139 | 2026-09-27 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2e7506ec-ce4e-3907-9b55-db1f4f27c983 | -11.9596 | -50.6751 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e05e0d12-1397-3a3c-bf6b-5633cad0feec | -11.9352 | -49.7752 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0bf33650-6263-371b-a0c3-5c58c7fdb608 | -12.0365 | -50.6233 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 8493c85c-9f6e-3b13-9e0e-7c19e15d4a35 | -12.4355 | -44.1262 | 2026-09-27 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| b145de36-0794-33f0-a90d-fe6d6453d858 | -11.7843 | -50.9512 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 659b7be2-d141-33f6-ae40-a51258dcd41e | -12.9457 | -51.0695 | 2026-09-27 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 435a3c2e-e025-3b8c-aa30-35729663a67b | -7.055 | -42.849 | 2026-09-27 14:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 1be05e5a-05b3-372b-8089-72c4b8c7625c | 2.946 | -60.3122 | 2026-09-27 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a57ca5d3-12a9-3c35-a837-379edb70e893 | -11.8662 | -50.5576 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| dcc0e9bb-e360-302f-a42a-d2e613fec3ac | -9.1525 | -49.9639 | 2026-09-27 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 2bff33ed-6da4-3482-a189-e9f19c41d690 | -10.7115 | -60.7312 | 2026-09-27 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 72c6b692-3d2a-3322-a2e8-83d869d90e06 | -11.9418 | -50.5916 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 00ab2773-46ea-3d77-a279-11ff7bf03f07 | -11.73 | -50.7656 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c5d5d1e8-3988-30f9-9f80-f9f1d33df02c | -10.4234 | -53.8014 | 2026-09-27 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2263a68a-428d-3b13-83e9-1534afca83ae | -9.2226 | -47.3507 | 2026-09-27 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 21a6925e-31bb-374f-9030-022913388cba | -12.6647 | -47.302 | 2026-09-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 365.7 |
| da403b69-bf3e-3194-bf6b-9640fb014cf9 | -12.8059 | -54.0255 | 2026-09-27 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 60fcfb03-d6b2-30b7-8ac2-9eb911156c90 | -8.6171 | -54.6126 | 2026-09-27 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d7818bc6-c1cf-35cf-aa35-feae7e7c74d2 | -10.8189 | -57.1993 | 2026-09-27 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 598bfe99-9da5-360e-81fb-94abcc5d95d0 | -11.9606 | -50.6108 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2146c936-5c3e-3af4-a79a-647449bacf02 | -10.4046 | -53.803 | 2026-09-27 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8f18c147-16cd-372f-8049-427809feb72c | -11.2669 | -51.3051 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 48d00fc4-f75a-3941-b206-86df515a5292 | -10.8187 | -57.2192 | 2026-09-27 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 5555c365-8d7e-300d-86a0-d6e2021573ef | -8.5982 | -54.6341 | 2026-09-27 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6fdfd001-41ca-3a28-a871-d38d90ff31d9 | -11.9402 | -50.6987 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3eeb24c9-171b-31c0-9f27-aca6a487b4a8 | -11.1901 | -51.3766 | 2026-09-27 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ae560202-33cf-3e02-bcf0-692243d60799 | 1.6565 | -55.9621 | 2026-09-27 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 95e8f903-eceb-304e-9441-b52ea05c91bd | -11.885 | -50.5768 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| bb5b31a9-f6f8-3b53-85d8-8e6755e0a8b3 | -11.803 | -50.9704 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| eaeb79b8-c734-366d-90ca-00926cb59532 | -10.7466 | -50.5959 | 2026-09-27 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0287f91e-62a0-3d9c-a84e-bd0453036b2c | -11.9199 | -50.7865 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 26ba958b-a4c9-3b00-9e4b-3aab9684cf4a | -11.9415 | -50.6131 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 643387d8-8fb4-35fc-bcb7-2d2a7941fdac | 3.5659 | -60.8516 | 2026-09-27 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 027e50ca-6805-3d52-af85-3e01cbbccef7 | -12.2894 | -50.2927 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b2b87ca2-301c-3dc0-af99-5843827567bc | -12.289 | -50.3143 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1759b4a7-2fcd-3c0c-a7b0-b5264b9d49d9 | -11.9392 | -50.7629 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0ac8f079-aa15-30db-a06d-f8e54a0f2cd3 | -11.3048 | -51.3011 | 2026-09-27 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| ca9ede41-8134-364f-ba1c-59c83c2a5f0a | -6.84 | -43.572 | 2026-09-27 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 42315c78-ca14-34d2-a0ce-6436d650ce14 | -12.2508 | -50.3189 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| bbcf3212-313f-3b16-9073-904e8d8cdb5f | -11.3547 | -43.4001 | 2026-09-27 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 672cc6e9-e976-3774-925a-501185934e28 | -17.5697 | -46.9019 | 2026-09-27 14:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 122cbff5-a205-36c5-9ae3-94ae8dbd3823 | -12.4351 | -44.1497 | 2026-09-27 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 587.8 |
| a4ffd3a5-76bf-3a15-aef6-d0d80f0706bf | -10.4043 | -53.8236 | 2026-09-27 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 42284d61-5aca-3874-81e3-037e1684f659 | -12.6651 | -47.2795 | 2026-09-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| ed2f8373-fbff-3414-bbfe-0110b37c3883 | -7.3653 | -42.1058 | 2026-09-27 14:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 171.9 |
| d5835cd0-e2f9-30cd-94e7-a7e73380e457 | -10.7677 | -60.7279 | 2026-09-27 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0bd18596-9a38-3e2d-9925-47010b3ab310 | -11.79 | -50.5664 | 2026-09-27 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |


[Clique aqui para ver as próximas entradas](README61.md)
