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
| 83f3bee4-8d54-311e-950a-d92fca05406f | -5.655 | -43.9013 | 2025-10-03 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| bd5f4b8f-caf1-37ac-9056-121a0d2a4b0f | -7.7749 | -42.5628 | 2025-10-03 01:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 6b767e7c-4bfc-3b29-b481-b79527d6f9ce | -4.6877 | -45.8056 | 2025-10-03 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 454e8e67-2c0a-3b45-a14b-b8678c4b6682 | -4.669 | -45.8066 | 2025-10-03 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 225.1 |
| 96066999-66bf-32ae-b3b0-c3b4ee18492f | -7.7557 | -42.5885 | 2025-10-03 01:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 70155af9-22b6-3164-9be5-b0c6bcac37da | -6.0418 | -44.6076 | 2025-10-03 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 639dfcbd-e289-3b37-8eaf-f81d12dfd124 | -10.8548 | -47.053 | 2025-10-03 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 3705e3ff-c2ef-3bde-a49c-2d9c0fa38997 | -11.1631 | -43.4054 | 2025-10-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 506ce313-7978-3461-8da1-7c4315dc1e2b | -13.6497 | -50.2685 | 2025-10-03 01:20:00 | GOES-19 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 236544b5-7224-3aa4-b171-9b1cc6f27f80 | -11.1444 | -43.3845 | 2025-10-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 116.3 |
| ec57bff7-01f8-3903-a044-57ba0bd4aeb3 | -7.7938 | -42.5607 | 2025-10-03 01:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| c12a4f8d-5b6b-36e1-b09d-015ce927b558 | -7.7746 | -42.5865 | 2025-10-03 01:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 216.5 |
| 4d690d83-4da3-3f2d-b122-5f1a1a600ab4 | -4.6692 | -45.7842 | 2025-10-03 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 201.0 |
| b9e43127-6887-3977-9457-678600d35f60 | -3.9331 | -47.5655 | 2025-10-03 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 90ff92b6-6f72-32db-9c21-169381446456 | -12.6323 | -46.9697 | 2025-10-03 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| dedda649-68bd-3f96-aa42-0e8539741fc3 | -17.8614 | -57.623 | 2025-10-03 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 85de1699-6924-3ac2-8bdc-4d298c23bba5 | -12.6327 | -46.9471 | 2025-10-03 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c198787e-6c7f-3c7e-8519-9d0af6a8f86b | -10.8521 | -47.2317 | 2025-10-03 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| a87b2714-505c-33e2-969a-636bfa73fd43 | -12.6131 | -46.9725 | 2025-10-03 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 23330834-8db0-3a14-aae9-452f80b569fd | -17.8617 | -57.6024 | 2025-10-03 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| e0c4b69e-2079-3c97-a1f8-441ee740b87a | -4.6878 | -45.7832 | 2025-10-03 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 2bbc0ec0-8f93-3b3f-ae22-e69cb2f08095 | -10.8552 | -47.0306 | 2025-10-03 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| ee738f75-5ff5-3334-95a4-d4b8ec922c81 | -8.6324 | -54.9747 | 2025-10-03 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| aa725b2a-19e7-3619-8e93-20a09fa4b79d | -7.756 | -42.5648 | 2025-10-03 01:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| c63f363a-7630-3b9d-8008-4c2cc883b950 | -11.144 | -43.4082 | 2025-10-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 189.9 |
| 9ad99abe-306a-3678-b6ad-1824cbf5582a | -5.8657 | -43.3981 | 2025-10-03 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 56828ca5-00da-34e6-a13f-a9a81912a120 | -8.6138 | -54.976 | 2025-10-03 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8705a02d-fe49-3ab2-a89f-241920fdb590 | -11.9163 | -46.2817 | 2025-10-03 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| a6f841db-7501-3324-8652-98cfb2dd41da | -9.9182 | -43.7212 | 2025-10-03 01:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 0baf7a05-9365-3e99-8ad7-fb56c3a374d2 | -13.7769 | -47.5392 | 2025-10-03 01:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 8ff4c181-b43b-3ea5-a5d8-f2ff21c276d8 | -4.6505 | -45.7853 | 2025-10-03 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 139.6 |
| ffaf824e-9bab-3c8a-ac9c-4c41d2d0068e | -4.6504 | -45.8077 | 2025-10-03 01:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 127.8 |
| d20cf05b-b892-3899-acfa-dce1f771e1cf | -9.8772 | -47.8103 | 2025-10-03 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d1ab3298-f4bc-39a4-a577-4d52a1fd6289 | -14.6886 | -43.8907 | 2025-10-03 01:20:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 59.0 |
| a8f3b653-5871-3e64-956b-c6c647542548 | -6.0605 | -44.6061 | 2025-10-03 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 189e8a59-4e77-3738-ace2-92b2f283f1ff | -6.0416 | -44.6304 | 2025-10-03 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| aa1310f6-5caa-3a66-9495-d920cdc2c079 | -14.9342 | -46.8965 | 2025-10-03 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a167b7af-1dc7-3745-9032-4dc171197ad3 | -14.9538 | -46.8931 | 2025-10-03 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 60b67e4b-912a-3f72-a4c3-dc7b091132e1 | -5.6363 | -43.9027 | 2025-10-03 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| d407bb17-1ed2-3d10-b7af-6ae74458c9a6 | -14.7083 | -43.8869 | 2025-10-03 01:20:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 0c8929a7-607f-3690-9b45-c10f11ee3e77 | -6.2408 | -45.3424 | 2025-10-03 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 610f17c6-73f0-3a39-a923-9fd075ad6ca7 | -10.8742 | -47.0282 | 2025-10-03 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| cada53e4-d5e3-3497-b388-ad95d0f0e11e | -13.1345 | -47.882 | 2025-10-03 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 57c4d834-216a-3d53-84b8-abc029ad94de | -14.8966 | -46.8346 | 2025-10-03 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 4c7ddeca-7080-3aa7-8675-5d022d4b19ed | -5.6361 | -43.9258 | 2025-10-03 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 1a706308-5603-3f75-a1b7-303363f79dff | -10.8739 | -47.0506 | 2025-10-03 01:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 2225e3e5-4e6d-3bc5-a026-229a5aecc523 | -7.7743 | -42.6103 | 2025-10-03 01:20:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 9a945eac-fd85-3fd4-8864-5853cd42fa0f | -6.0603 | -44.629 | 2025-10-03 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b4933bd9-99cd-31a2-837e-31218141605c | -14.9132 | -46.9684 | 2025-10-03 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c540649c-8ddd-327c-8170-207b2ac5f0ca | -7.7743 | -42.6103 | 2025-10-03 01:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| de245103-9a15-3c00-bb9f-50d2a6adf8cc | -6.0603 | -44.629 | 2025-10-03 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 78eef831-f243-3e92-ab3d-eda320c84402 | -13.9775 | -48.157 | 2025-10-03 01:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8665be96-66ff-35c6-b29a-5d14f87ea56d | -10.2781 | -50.3032 | 2025-10-03 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| cd602033-33a3-3dc0-836f-57e755d81674 | -13.7769 | -47.5392 | 2025-10-03 01:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a822e8cd-ef76-36d8-a60d-82a76f25d46b | -17.8417 | -57.6254 | 2025-10-03 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 0f857955-4494-3d4c-b306-47a86086888d | -11.1444 | -43.3845 | 2025-10-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 96.9 |
| e3cb9bae-c7aa-3f48-9c5f-8701d0c2c83f | -12.6131 | -46.9725 | 2025-10-03 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 2bc542d1-b960-3b0f-a2f8-6c26e21065f3 | -6.0605 | -44.6061 | 2025-10-03 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8d575b8b-582e-3ae9-ac55-7dbdda69287a | -3.9331 | -47.5655 | 2025-10-03 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b3dff5ed-54e2-3e06-b6c4-240e33d9df06 | 1.5103 | -55.8259 | 2025-10-03 01:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 2ec1ff8c-cfe6-302f-bbe7-fccafcba67e0 | -6.0418 | -44.6076 | 2025-10-03 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c846546a-da9c-38e9-ad56-486c06be0b60 | -11.1627 | -43.4291 | 2025-10-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4af1dfc1-0488-35d1-941b-17fb7b006aca | -5.6363 | -43.9027 | 2025-10-03 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 32bf8751-d6e6-39db-959f-66038f23b684 | -5.6361 | -43.9258 | 2025-10-03 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 14e87c51-f817-3de6-8bbe-378e110818ef | -4.6692 | -45.7842 | 2025-10-03 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 245.7 |
| fad39558-e93f-356d-b201-6cede8b2d170 | -11.1631 | -43.4054 | 2025-10-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 157.4 |
| 89aab582-0ea4-3e20-b04d-d6afa4b7dab1 | -8.6324 | -54.9747 | 2025-10-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 9c8e2058-1b51-326d-a83c-2d146524d3aa | -8.6138 | -54.976 | 2025-10-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b2b79369-eedc-3f8a-aeeb-52f7689510ca | -16.3584 | -42.3489 | 2025-10-03 01:30:00 | GOES-19 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.4 |
| 3db6a305-8102-3811-b7b2-349774fe3454 | -7.7749 | -42.5628 | 2025-10-03 01:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| c34c4bd3-af32-308b-b050-006f81dd0bed | -11.9163 | -46.2817 | 2025-10-03 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 0f3c8775-d847-3b4d-a779-b75123b4f485 | -7.7746 | -42.5865 | 2025-10-03 01:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 186.0 |
| 65eb4e8c-c794-3278-85bd-5e943e0aa239 | -4.6504 | -45.8077 | 2025-10-03 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 085348f8-57cf-31a2-81b8-803c7f8fcd8e | -7.7557 | -42.5885 | 2025-10-03 01:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| 8d45e189-3fbd-3d36-ae7c-fac773c6eda6 | -11.144 | -43.4082 | 2025-10-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 180.0 |
| 6559f9eb-cf12-3529-9de5-5af5e02e3c2c | -16.3385 | -42.3535 | 2025-10-03 01:30:00 | GOES-19 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 212.4 |
| d7462624-1b6a-3be1-b586-eff2efa94d34 | -5.8657 | -43.3981 | 2025-10-03 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 555c1d8e-0732-38a5-a1dd-c28503e3ac03 | -4.6505 | -45.7853 | 2025-10-03 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 8388f0ea-dc41-315e-aaba-7ed65bedbda9 | -12.6323 | -46.9697 | 2025-10-03 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| aa8458c7-6bc0-3b96-9082-ea1408e53e5b | -14.7083 | -43.8869 | 2025-10-03 01:30:00 | GOES-19 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 2c8ed5fa-0ad2-3cd5-8346-21e926733d07 | -5.655 | -43.9013 | 2025-10-03 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a0e010ec-b7e6-362e-8565-f79c5cf3c699 | -13.1345 | -47.882 | 2025-10-03 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ce20d6c0-6b56-3cd8-b962-a5a109695c48 | -16.3378 | -42.3783 | 2025-10-03 01:30:00 | GOES-19 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 396.4 |
| 316c4605-1691-33eb-a1a7-7ff35167ccbe | -6.2408 | -45.3424 | 2025-10-03 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0acb9d4f-8c75-3f30-ac5e-5c55c9c60acf | -10.2587 | -50.3478 | 2025-10-03 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 9bc9c81b-aa3c-37e2-abe1-afcc9d2babd9 | -17.8614 | -57.623 | 2025-10-03 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| c4b7d0c5-ca9c-3029-bfd1-1c6a822bc19b | -4.669 | -45.8066 | 2025-10-03 01:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 284.2 |
| 9b2816f3-a2b0-33c2-99a3-db04665a1dd2 | -6.0416 | -44.6304 | 2025-10-03 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 9a04354f-3b09-3c2f-bbc2-09c1ec0efd32 | -17.8617 | -57.6024 | 2025-10-03 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 7c61827e-a548-320c-b62d-c4dbb447ae78 | -14.9342 | -46.8965 | 2025-10-03 01:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| fc4a4e49-7344-3ad6-bcdd-219d6a47f5f2 | -7.756 | -42.5648 | 2025-10-03 01:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 00fb621e-bb8b-3b51-8317-b318dd58197b | -16.3577 | -42.3737 | 2025-10-03 01:30:00 | GOES-19 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 173.2 |
| b84f0ee4-f432-3ed6-9f5c-5b6f72e18cdd | -12.6127 | -46.9951 | 2025-10-03 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f1a09f58-dff8-3faf-986a-6a16f0078bf0 | -7.7557 | -42.5885 | 2025-10-03 01:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 5982cf44-a951-330d-b975-e3366f3076b8 | -5.8657 | -43.3981 | 2025-10-03 01:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0bd70ec7-8f33-3223-a1b6-80f05cc8fe63 | -7.7938 | -42.5607 | 2025-10-03 01:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 7efa897b-453d-34a8-ba8e-9539d1c62890 | -5.6363 | -43.9027 | 2025-10-03 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 1038ad45-84fc-3229-8eb5-a5f98008b905 | -14.9538 | -46.8931 | 2025-10-03 01:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9ede3646-94a2-3c37-880a-e9d87c4c56bf | -14.9342 | -46.8965 | 2025-10-03 01:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b06d5893-278f-34ce-9340-64e9dd2ee4fa | -6.0603 | -44.629 | 2025-10-03 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |


[Clique aqui para ver as próximas entradas](README12.md)
