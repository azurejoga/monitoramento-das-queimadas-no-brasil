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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ef16ce5-d104-3efc-b072-ac13ba625ef8 | -12.83296 | -48.12026 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebaf7f0b-9fa9-3acc-9fc6-e5b1b2717490 | -13.4595 | -46.97045 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b731774-77ee-30fb-929b-fed6ccb8410f | -12.92553 | -56.98126 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96061ad4-d495-3d0a-a2f7-f6ce5429efb8 | -10.74658 | -59.8182 | 2025-08-30 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9848204-50bf-33ec-89d8-634dd93a010b | -13.50748 | -46.94657 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7ed4a48-4b9a-30dd-9676-735a04c87b8a | -13.5783 | -46.91037 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab9d075b-4276-3a5c-8ce0-14fb603313bf | -9.75942 | -65.08735 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d583bd7-e20d-3a5e-be32-ee86afcb0cfb | -12.69562 | -48.14545 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e47de9e-6401-3076-b47b-a63f5084d80f | -13.38954 | -46.96016 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9cfc075e-00c7-3ee4-b0ed-127f52dbae29 | -13.19383 | -45.28698 | 2025-08-30 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6624e15-ff97-3e74-b037-27e9db1c689c | -13.68991 | -46.91159 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86be06f3-ccf1-3558-9434-027c0b0e417d | -12.6241 | -57.00853 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da6870d6-1121-3927-8752-66b32c6aaa4a | -12.93851 | -48.12523 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fa8333b-8726-3b24-853d-e7f520a5a487 | -13.38376 | -47.01407 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a36c4ff-9a9b-395d-8ac4-f6220519322e | -13.57177 | -46.91072 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 644ae890-493c-3caf-b8fa-4eca022a4cf5 | -12.89704 | -48.88681 | 2025-08-30 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 181b55a0-90f8-3625-91bd-40b1b1d3bde7 | -11.30402 | -63.25478 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8154a50-839c-3235-92fe-a02a650a7e9d | -13.50689 | -46.95175 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18a11256-734e-3c3d-863c-52c9cace309c | -13.46638 | -46.96675 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c5ec315-a8aa-3a3f-99c1-0dd6b8b0d61f | -12.62353 | -57.01231 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd5fcd6b-4065-3155-a94e-42811532220c | -13.36574 | -47.00189 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1ffcc1d-f28f-3ea2-a42d-8988098f6b94 | -13.37795 | -47.00822 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f941fa38-c578-3a56-b00f-895878e6d493 | -10.74321 | -59.81766 | 2025-08-30 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97b7a2c8-22a3-349f-b958-828e201b35f0 | -10.74263 | -59.82128 | 2025-08-30 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d82515c9-4d21-3425-9abc-4ba48dc1421c | -13.38546 | -46.97962 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f93a6fa1-a008-33c2-9dbe-f2aedc421f19 | -8.84592 | -70.63408 | 2025-08-30 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2590a7d0-559e-33a7-bb47-0c8e02472e3a | -10.25421 | -64.49922 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cda0d257-eac7-37fd-b19d-3df2e9b0072c | -12.94399 | -48.12968 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f9f46c5-e871-3b91-a53b-11b754188cfd | -12.39266 | -46.43621 | 2025-08-30 05:12:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3db54ba-18c2-3d66-8829-a02f3e4b711d | -13.37264 | -46.97879 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c332b6ad-6ce6-377a-ac32-16acf5c01394 | -13.46192 | -46.94875 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58307f44-5532-3d8a-b8bb-bf8824c83411 | -11.30313 | -63.25987 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06b2cddf-ef7d-3717-9477-a3f4e4dbdea0 | -9.54342 | -65.70135 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6be90d14-4f92-3447-8f26-2ff12881d4a3 | -22.55754 | -54.92025 | 2025-08-30 05:14:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6b604f86-b3df-3b8c-b9da-de6a15d4fba0 | -22.19309 | -54.84215 | 2025-08-30 05:14:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e49f1679-469d-3e6d-9271-06acb95be1e6 | -22.19505 | -54.83924 | 2025-08-30 05:14:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1f8f6ea0-62ae-3a79-81e7-550caf8b280d | -18.91647 | -56.25616 | 2025-08-30 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2e4a8b0f-62e1-387d-abaf-4fb437f7c6b9 | -22.19452 | -54.84356 | 2025-08-30 05:14:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0859360b-947d-3a92-bd75-3fa98a1f60fc | -20.38569 | -54.57979 | 2025-08-30 05:14:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ac5c870-734d-32f5-9a1f-9b4ea5549fbf | -20.47776 | -53.67529 | 2025-08-30 05:14:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d35e834d-ba80-3bfd-8116-e31f3f224cef | -18.91334 | -56.2508 | 2025-08-30 05:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 4feb3b75-5343-3e84-aa82-0f2a09683a70 | -28.72078 | -55.59556 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| aff2881b-e4ae-3586-a310-70c140fe211d | -28.72498 | -55.641 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| db9ad330-8a01-3774-8254-d6226c346110 | -28.72845 | -55.63897 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.8 |
| 8fa5c327-86bc-3387-9e9f-99c3856134dc | -28.72352 | -55.64325 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.1 |
| ace6cc80-7244-372a-887d-bbe195c26055 | -28.73338 | -55.6347 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 3ec28229-9f7c-32eb-8b70-eb757e977a19 | -28.72207 | -55.65775 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 8a32bc6f-00b4-33d3-b318-a28c2da0a27f | -28.72523 | -55.59622 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| abed025b-ebb8-3ed6-a91f-a2938939f47e | -29.16596 | -55.00119 | 2025-08-30 05:16:00 | NOAA-20 | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 9c3194a7-c395-3b72-bca4-3cc16f0890e7 | -28.71137 | -55.59922 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 6dd2fce8-db55-3ab4-8f4a-0086354a03c1 | -28.71581 | -55.59986 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 5c6a106b-85e8-3751-ab0b-63bb9cef7a00 | -28.72158 | -55.66263 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 2c5b3adc-a56c-32c0-9d77-45a83535d620 | -28.72893 | -55.63412 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.8 |
| 4a625673-bf02-3376-a4a3-476a5a6ac1b0 | -28.71633 | -55.59491 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| e0e40848-3556-391f-807f-803217c6d0a7 | -28.59081 | -53.62106 | 2025-08-30 05:16:00 | NOAA-20 | CRUZ ALTA | RIO GRANDE DO SUL | Brasil | 4306106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a5cb47f-6448-3831-9cd4-06514f3bd805 | -29.02908 | -52.36953 | 2025-08-30 05:16:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3eab32f8-8254-3e6a-917a-ddd036d0fefc | -28.72994 | -55.63673 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| 19ae0f31-6766-363e-aca7-d0733033edff | -28.72447 | -55.64583 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 8.5 |
| 7b07c542-9c20-3787-b141-b1dd12e2a162 | -28.72395 | -55.65063 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 8.5 |
| b77bd855-93c6-33f1-8a2a-2dec3a5a51a4 | -29.02774 | -52.36964 | 2025-08-30 05:16:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6e1b51c1-a22f-3b36-ae95-2b307d085582 | -28.72304 | -55.64809 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.1 |
| a91541d5-032e-3b16-956c-080e5e66516d | -28.72344 | -55.65546 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 14ac0b92-5a21-35e3-9c33-df4d72aa610a | -28.72002 | -55.64527 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 45936440-1a24-3bee-9b3e-52ba0886450d | -28.7255 | -55.63615 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.4 |
| 9b3fc016-0616-306a-b654-8d040b41e659 | -28.7124 | -55.58938 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 88b92d2e-6a2e-3399-b394-9a14e7a96c2a | -28.72292 | -55.66034 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| ff4b3229-62e1-3fe2-9243-f77fa22aefc3 | -28.724 | -55.6384 | 2025-08-30 05:16:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.8 |
| 0a73728b-36eb-3789-a04a-376323a217f7 | -9.1155 | -65.7699 | 2025-08-30 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c9777bb6-fa2a-3cc7-94e0-acf6beaebd3f | -12.0148 | -44.0054 | 2025-08-30 05:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 48c5a2f2-9f8a-39bc-b49c-c8e058c60153 | -6.7814 | -43.7865 | 2025-08-30 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 367fb558-e851-3eba-a370-d18a40873735 | -11.8365 | -46.4741 | 2025-08-30 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 222.1 |
| be1f0b65-ce9b-3797-bd2c-8033ad713d49 | -6.1853 | -43.3257 | 2025-08-30 05:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 331.6 |
| 27a9c4d4-9d2a-39c7-93e0-379166aa0609 | -6.185 | -43.3491 | 2025-08-30 05:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 206.5 |
| aee7748b-6493-3d28-9081-dcb90225cfc2 | -9.4498 | -62.3294 | 2025-08-30 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 267.2 |
| 07cb9800-4516-3b21-b313-a65ad6f6bd87 | -9.4497 | -62.3485 | 2025-08-30 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 231.1 |
| 8165efca-7fc4-3f58-bcdd-6e51ce5b6d49 | -11.8177 | -46.4541 | 2025-08-30 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 083be747-932b-3ef1-ac17-642b90690813 | -9.4684 | -62.3286 | 2025-08-30 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 221.5 |
| fff09aa6-24bc-3c5a-a079-6bbdd9125db5 | -11.8556 | -46.4714 | 2025-08-30 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a5b2753e-0ec6-369b-a5bc-cb92fc0731de | -11.8173 | -46.4767 | 2025-08-30 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| edc49288-05fe-306c-a195-0ee74230b332 | -11.8369 | -46.4514 | 2025-08-30 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 254a85c8-bdd6-3547-99e1-b6518f29db4a | -6.1665 | -43.3273 | 2025-08-30 05:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 997cffb6-807a-3f27-935d-7c06ea2d5a06 | -6.1663 | -43.3506 | 2025-08-30 05:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2974348a-ecec-3393-926b-bee4715e61a7 | -9.4432 | -60.5692 | 2025-08-30 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1e7ad02e-0e59-353e-a9ca-be96a5811e2d | -9.4433 | -60.5499 | 2025-08-30 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| e30aa9fe-1c0b-3f7c-ab67-3a85c033546e | -12.0153 | -43.9818 | 2025-08-30 05:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| c5faa7e0-0875-3bc9-a2da-aa5068718cca | -9.4683 | -62.3476 | 2025-08-30 05:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 7eee9cf5-ce53-35d8-811b-b099d3f68246 | -9.462 | -60.549 | 2025-08-30 05:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d90b05ae-ae92-317c-8228-f8683e3130cf | -11.856 | -46.4487 | 2025-08-30 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0ad9d411-08e4-3062-a2eb-1985cabe2916 | -11.856 | -46.4487 | 2025-08-30 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 28c1ee39-96b1-342b-8225-2f17943ffa2d | -9.4497 | -62.3485 | 2025-08-30 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 203.3 |
| e9744360-cf10-3b9b-99c5-f981969283ae | -6.7814 | -43.7865 | 2025-08-30 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9056c5af-5921-3da9-a31e-55eea10fe25c | -11.8173 | -46.4767 | 2025-08-30 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4cd1ce1f-dd29-3a5c-b44c-9b487bbeff5c | -6.1853 | -43.3257 | 2025-08-30 05:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 8c718367-d20b-3782-bfda-98ef9833e8ca | -9.4433 | -60.5499 | 2025-08-30 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0c4b795e-6e70-3ac8-a7f2-04607b7a5dad | -9.4683 | -62.3476 | 2025-08-30 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 134.6 |
| cbaa5bad-0436-3982-b5c5-a636266e1b30 | -11.8365 | -46.4741 | 2025-08-30 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 234.4 |
| 1bd7c91b-df07-39d8-b4e2-5c905aede8e8 | -13.3825 | -46.9697 | 2025-08-30 05:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 9da51f1c-6e8f-30d3-9d87-2fbe388b11ec | -11.8764 | -46.378 | 2025-08-30 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| a7cab8b5-825f-3206-9b06-6d5459304059 | -11.8369 | -46.4514 | 2025-08-30 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 752ab0e7-b1c0-39a4-96b7-55a1c4167f5a | -6.185 | -43.3491 | 2025-08-30 05:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |


[Clique aqui para ver as próximas entradas](README77.md)
