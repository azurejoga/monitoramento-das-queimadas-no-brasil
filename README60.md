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
| ff34335b-11a9-3172-8e8d-0ca6b630fa0a | -6.98448 | -47.08158 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c4090a3-0dff-3360-b3a9-786a78ee124f | -6.69191 | -47.64058 | 2024-10-29 04:40:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa4d9919-f174-3eec-a4c0-abaf11568700 | -6.68738 | -47.53382 | 2024-10-29 04:40:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f803b0ba-90c0-3a9a-9d72-939c782653c6 | -6.60789 | -47.38817 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| feec5fc7-0379-3de9-8450-c7c761c78c6f | -6.60731 | -47.39193 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4092bd8f-ccc6-355a-af26-550572caf94f | -6.60674 | -47.39568 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2720a357-36bd-321a-8b74-a50b11ac94fd | -6.60388 | -47.3914 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 93d658a8-9bbc-3300-b1fe-4d1a75ab597e | -6.55221 | -47.27236 | 2024-10-29 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85caa60d-18e1-3d20-b523-3b4f5ff669ce | -7.31589 | -47.4354 | 2024-10-29 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a3c4a87-f4a2-3d55-8ae8-530fa579eab7 | -6.6308 | -47.35337 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 56566004-29cf-34bc-b812-d777a828f5e5 | -6.60331 | -47.39516 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ffe52618-bfd9-363e-b2e4-ff194aed40bb | -6.60045 | -47.39088 | 2024-10-29 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f6a55102-0e21-38e3-bec6-bcfa3cc3cdac | -6.67772 | -47.66489 | 2024-10-29 04:40:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11844abc-e780-3560-89c7-3475c08c2f7e | -9.04641 | -47.81548 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98cfe3d9-613b-306e-a9a1-c82860b45592 | -8.72223 | -47.8951 | 2024-10-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfdb76ce-e071-3b21-9279-c33e2dd3a9ca | -8.68117 | -47.95768 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96b590a6-3287-3b02-87bd-402f7fbb90dd | -8.66736 | -47.86354 | 2024-10-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a350af9-feb1-39e9-951e-91968841a381 | -8.66073 | -48.00032 | 2024-10-29 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea7e48a0-1c3f-35a8-a122-a350d42034f0 | -9.14792 | -47.33364 | 2024-10-29 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc72afbf-4174-3cfa-9374-e556654973ed | -9.10763 | -47.65924 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc91a2b3-636a-3d53-b1d9-f88d65ad4717 | -9.10605 | -47.65602 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fba1aa2f-1599-3172-b7f4-b7fd5b9164fd | -9.10473 | -47.65485 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70471184-ec82-37df-ba4d-0451faae4597 | -8.66679 | -47.86732 | 2024-10-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fca36c8-0801-3a59-9e23-3319683fc1b4 | -8.09029 | -48.46976 | 2024-10-29 04:40:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 061815f3-fa52-3da5-bcd2-ce05c6dcdb34 | -9.8549 | -48.05497 | 2024-10-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a271f61-ea86-3860-a48e-1b796f16977d | -9.85146 | -48.05444 | 2024-10-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb3f4cb0-bf0d-3783-a598-b052a3ddc1b2 | -9.49995 | -47.80784 | 2024-10-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80a2e641-35aa-3600-ab0b-d09c05ea8971 | -9.78858 | -48.12313 | 2024-10-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b8a2c95-b168-33b6-9721-5ab40f346d2c | -10.51068 | -47.7385 | 2024-10-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ca5bdf0-80c5-3c7c-9083-402e4c3a1dd7 | -10.46925 | -47.67251 | 2024-10-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b9feb08-a64a-3e63-a2aa-67466482afcc | -10.44819 | -49.04764 | 2024-10-29 04:40:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 859e761d-7490-35d3-8ebb-c02b701462bd | -10.44764 | -49.05126 | 2024-10-29 04:40:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3c6c28e-7426-3403-b2e3-88e36f511224 | -10.44484 | -49.04712 | 2024-10-29 04:40:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99010594-b45e-3bac-bcd1-f3e0854a5b8c | -10.01322 | -48.23778 | 2024-10-29 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a251cb0-4943-36be-b02a-903e525164b8 | -11.96927 | -48.09536 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57a6abcd-364d-300a-bfb3-a5f7df5986ed | -11.96636 | -48.09087 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80373a88-bb1a-34b7-9cfd-c86d232dd216 | -11.96577 | -48.09486 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97f98e63-a7d3-3c76-bcc1-8d68861effa0 | -11.83223 | -48.09486 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b58b0b6b-eca5-31bb-a3f0-7a98fbd16ce3 | -11.83164 | -48.09882 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac860a01-940c-37e2-9d69-523c2ddb94b3 | -11.82444 | -48.75482 | 2024-10-29 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d201088-dc02-3a78-bc40-9ca03547a72c | -11.82387 | -48.75858 | 2024-10-29 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf61138b-a766-317f-a3fa-18fad8fef38e | -11.82103 | -48.75429 | 2024-10-29 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1802e438-3d48-3d91-ac72-030b9f4511eb | -11.72574 | -48.35814 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4eedd558-8430-3a1e-9a90-c97110cf0274 | -11.72517 | -48.36198 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15d4e3ee-794c-328e-9d73-8891a4be310c | -11.72228 | -48.3576 | 2024-10-29 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fbe86798-bf01-3eeb-8b1a-65f2a0d06eff | -11.58525 | -48.10346 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58774d5c-f8b2-39f2-9c1c-1c19631162f9 | -11.58505 | -48.48331 | 2024-10-29 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e458ce34-d02b-32b0-8702-b238f33c44fc | -11.4255 | -47.81269 | 2024-10-29 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c9f25bc-59b8-3c04-9c4e-14b111a79cb0 | -11.2464 | -47.90102 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d4fabf1-f5aa-304c-9afd-10f9be5551c6 | -11.24582 | -47.90499 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bf2a341-9256-3c11-b8e7-299578b84019 | -11.24525 | -47.90895 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc07a334-0cc4-3230-bc42-12c3887b5b92 | -11.2429 | -47.90046 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c53c26c5-a436-3983-9380-70c8b39cd829 | -11.24232 | -47.90443 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a31f704d-86ea-3912-a6d4-238740d8917f | -11.24195 | -47.90082 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d32f169d-59d3-3582-afdd-facd3029a234 | -11.24174 | -47.9084 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aad8a6ce-5819-3f39-bf6f-51131b2f0a1a | -11.24136 | -47.90479 | 2024-10-29 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7efa20ca-4bd4-38e0-abbc-87f2ef8efb8d | -11.01309 | -48.67047 | 2024-10-29 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf651ea9-9dfe-3534-8d94-80df3f3717fa | -4.93045 | -48.51392 | 2024-10-29 04:40:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 423341ad-eb43-39c0-8623-33c6225c49bf | -4.92198 | -48.63282 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 514ac663-75d9-3444-a4ba-7561aa1108c3 | -4.91814 | -48.63575 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ecb6472-7dc5-397c-bb08-530869620886 | -4.91538 | -48.63179 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf9c8dfd-7b39-3ea2-9fa4-96857d28250a | -4.91483 | -48.63524 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8e68d5f-69f8-3593-b3da-8e11174f47f1 | -4.91321 | -48.64558 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15746820-b70b-306b-969f-51ec64ad2f0f | -4.91045 | -48.64162 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b3698b42-9d4b-3dd6-aab7-77170c183901 | -4.90991 | -48.64507 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c500a14d-0b94-305a-9898-83418e77fe21 | -4.90937 | -48.64852 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d71ae96-317d-3a6b-b4e8-61d4e7c70899 | -4.90723 | -48.48905 | 2024-10-29 04:40:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6bd6851a-433b-3491-97f6-703b9bbf3568 | -4.90661 | -48.64455 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 455d2357-7071-3994-92fe-17f779aff8ce | -4.90607 | -48.648 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fde13e59-65b2-3237-aa9f-0bc87a615b7d | -4.90581 | -48.56314 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8298ce83-a22f-3af0-8ae0-e9a6f1448431 | -4.89812 | -48.56903 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8be63c73-24b9-3a22-957d-a6014390fb77 | -4.89365 | -48.72724 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adbfedd9-53b8-3009-9827-2444516c2a9d | -4.89292 | -48.66716 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32aac8c6-5414-3339-bfb6-2dfb8f43e701 | -4.89015 | -48.6632 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 612f89fd-ceff-3a4d-9f23-6dfcc1f03481 | -4.88961 | -48.66664 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9193031e-2f23-3a87-bd32-63a185431cbf | -4.88685 | -48.66268 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4615b00-ab3b-321e-8cd0-51b2cd4ac33b | -4.88624 | -48.64494 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5802fa82-8a0f-3d47-8243-e4900239dfc3 | -4.8857 | -48.64838 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45a1089c-b537-38f9-919b-c92244f7f0d3 | -4.88301 | -48.66562 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2921d366-e6ad-3370-ad8b-10e6d5ffaf53 | -4.87889 | -48.58374 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2231bed9-47a8-3775-95bb-68ab0f0c1d22 | -4.87605 | -48.55854 | 2024-10-29 04:40:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c97b94a9-ed8f-370a-b12b-74e6e45308d2 | -4.87558 | -48.58323 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b4da37f-769d-3601-ac47-4b03d201606f | -4.87497 | -48.56545 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ba646ac-26b8-323b-8f07-c4ca0888d17d | -4.87167 | -48.56494 | 2024-10-29 04:40:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8e01478-915a-3cee-938d-5c3dd31804b3 | -4.84936 | -48.64274 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efbcf581-8c34-3eb4-a5b2-ed47f54bf79a | -4.8466 | -48.63878 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803043e0-3aff-3f1f-a9c5-f5542eacd3e9 | -4.84606 | -48.64223 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0f42e18-768a-39b7-9d10-19f70e7935af | -4.24971 | -49.18872 | 2024-10-29 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9818265b-72c7-3389-9ded-fbfe4810d7db | -4.59542 | -48.54619 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a45df4c6-d84f-36df-933a-71a55519e19f | -4.36526 | -48.4955 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33497217-9492-36b9-ade1-b0a5ab23956f | -4.34969 | -48.61654 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7370e9c4-015e-3bfc-9a33-bcd2d5ff76d8 | -4.34747 | -48.60915 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adf826c1-6ce2-3b41-85f3-af44b47d7474 | -4.34693 | -48.61259 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c678ff8-bf1f-3b3a-94c3-a2d1981df04d | -4.34416 | -48.60863 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef7fda2e-5bf5-3093-9a4f-bedd8adb7408 | -4.34362 | -48.61208 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55adb1c2-931f-3ef1-8855-b8a0cf1568e6 | -4.34086 | -48.60812 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0343c5cd-03b4-3a1e-b62d-1ca57b4c1ca4 | -4.33978 | -48.615 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 108bca6a-205d-33b8-82dd-ed18589af478 | -4.29686 | -48.60833 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 108d3880-f7c0-3313-84b2-a0a6b6c62464 | -4.29633 | -48.61177 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ffcb108-6bb0-32d1-9491-9547a738488f | -4.29471 | -48.6221 | 2024-10-29 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README61.md)
