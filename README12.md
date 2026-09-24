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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08dcba43-410d-34bd-b069-fcd71f228be7 | -8.9056 | -45.901402 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afff75c7-38e5-3971-a2f9-cc3fd4ed2d81 | -3.7171 | -54.205002 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be01b595-0373-347d-add2-a5b5d83019cc | -6.265 | -43.260101 | 2026-09-24 00:38:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e6f529d-b71e-3a73-94dd-6ecd6f646508 | -8.4527 | -48.685902 | 2026-09-24 00:38:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c0ea5047-da9c-31a2-8a27-2b44fc3533b4 | -10.9368 | -43.832802 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15937d88-5d1e-3c4b-a92d-e15d746fce0f | -3.1765 | -48.0294 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d007ce8-4b6e-3258-885e-91d85287d941 | -0.941 | -47.550999 | 2026-09-24 00:38:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7b15aef-fa14-30ca-80cd-669709128d12 | -10.2855 | -47.542301 | 2026-09-24 00:38:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ec0968d-3f3f-362c-8215-0ce090875631 | -3.1652 | -51.3536 | 2026-09-24 00:38:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 593bd757-d2b3-38bd-ae2a-e0be5e66f44c | -4.6782 | -45.967098 | 2026-09-24 00:38:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 561edbc9-3e6f-3870-8729-8a037a0770c2 | -11.4928 | -42.331299 | 2026-09-24 00:38:00 | METOP-C | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7a4836fc-9e8f-3c1a-bfad-87ff20c5d6e4 | -10.5629 | -44.604801 | 2026-09-24 00:38:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b40077ef-405e-3040-bd40-49f9365ce93f | -12.8577 | -44.387798 | 2026-09-24 00:38:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d082048-214c-31f9-9915-7da25118e126 | -3.1749 | -48.0224 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcb1df4f-ec0f-32b4-8e72-f777ae250307 | -12.6859 | -46.990002 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42258c57-fd73-3a9e-81ea-01a2ed2f18e0 | -1.8209 | -55.707001 | 2026-09-24 00:38:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 229f07ab-b775-33e1-ae3f-094f601f511a | -11.966 | -50.772499 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5597d22-0dec-3a96-827d-467df9f5b40d | -6.4337 | -59.955601 | 2026-09-24 00:38:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84098143-4ce1-31cc-b847-041601861059 | -12.0737 | -50.749298 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 535bc466-c797-3867-9aab-fae00da89040 | -6.2566 | -39.363998 | 2026-09-24 00:38:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f8c2bd55-8935-3393-ba7c-cf79b5c1d412 | -3.7206 | -49.048302 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 828b7566-b639-339a-aaa9-5384ed3d2aa5 | -7.4219 | -49.868801 | 2026-09-24 00:38:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb52e6d6-0eee-3a6b-a2cd-60643647501e | -6.0575 | -47.280499 | 2026-09-24 00:38:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd80bf0-5c67-3e4c-8ff1-b49c72267e92 | -1.3919 | -47.940399 | 2026-09-24 00:38:00 | METOP-C | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5f3842-97d7-32e3-996f-b4de045f2f53 | -4.0154 | -52.0611 | 2026-09-24 00:38:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dff23af3-21c7-3246-bc2f-04156d0261a6 | -10.0979 | -46.055 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18c9a968-8762-3599-b8f6-0907fdb2d085 | -3.1847 | -48.020199 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0fc605-b041-32ec-8815-1cd23dfebaf8 | -10.0895 | -46.018799 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7078eea-c501-37b1-b74f-82c13a68c48c | -8.777 | -45.8372 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 433ff1ba-35bb-31c5-aa39-b0d89e4f0593 | -3.4506 | -50.074699 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3128d439-eb6d-3a52-83da-5fdf8a33d5aa | -5.2007 | -44.679901 | 2026-09-24 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a92b2ba-72e6-316a-89b9-6b85301022e0 | -9.587 | -40.3223 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dc59f67b-fbbf-3fd4-b176-c2729ec994f6 | -5.8487 | -49.879601 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47539bb4-c5b4-3c32-8c63-a0a70056e950 | -13.4608 | -46.270802 | 2026-09-24 00:38:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54b76429-7852-3dac-bfe8-b8bb2c48418a | -11.7868 | -50.988499 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dd4ab79-45c0-3c7c-9854-e3a2815ef158 | -1.2741 | -57.037498 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d23d52b9-c4ba-3298-9343-95848c20e828 | -12.5052 | -46.965801 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3433775-bdfe-3922-b7f8-c731db31e5a9 | -12.5115 | -46.993698 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5e559aa-9f04-3eae-8751-947aa160fb5a | -2.8175 | -60.2136 | 2026-09-24 00:38:00 | METOP-C | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 421f3260-6b58-3494-b329-234eeb1c6c93 | -10.0861 | -46.004299 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6ee767-85bf-3ccc-9a4f-2d760c43f529 | -5.854 | -49.766998 | 2026-09-24 00:38:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa0aaeb-344a-39db-9de3-1d8c1eb204b6 | -9.8407 | -48.490601 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e0a7832-6573-32f2-ab26-35912f77e1a4 | -7.6811 | -45.48 | 2026-09-24 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64a2d284-83c7-3fe9-be73-6e951a8ceecd | -4.9996 | -45.533298 | 2026-09-24 00:38:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caebe450-3e98-3f5a-9456-219db656d393 | -4.8176 | -43.5452 | 2026-09-24 00:38:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9477a4c0-42e1-3c8c-8e80-78dbea79d24b | 2.4569 | -50.9389 | 2026-09-24 00:38:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bab309de-32bd-391a-beee-7edd9c009424 | -4.9898 | -45.5355 | 2026-09-24 00:38:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66e040fa-a992-3a41-a9aa-27180ae650e4 | -10.2135 | -44.1357 | 2026-09-24 00:38:00 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1cdb5921-5b69-3003-9ee6-bea6f8d7b966 | -3.5551 | -43.4771 | 2026-09-24 00:38:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00eae6e3-f796-360a-88b2-98078f6ceb25 | -9.0494 | -48.1362 | 2026-09-24 00:38:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8758a6-04a2-3944-bf73-4c224052b942 | -12.422 | -46.963001 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 168096b7-c0bf-3870-97bc-e839d575e9bd | -9.5811 | -40.339699 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 50a6d405-b304-3755-98e8-5a0320ad3318 | -2.564 | -54.7332 | 2026-09-24 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2d4aae7-9144-3509-82e5-0fc4007624bb | 1.284 | -50.834599 | 2026-09-24 00:38:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ff8d6ef0-0bb5-3a44-a346-e45ff62cc2e4 | -8.8958 | -45.903702 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 02571219-2ad0-3d27-abbf-480b1c08f35a | -8.7476 | -45.844002 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cc7eb11c-5cfa-3391-ad9a-8c68b2797d49 | 0.6105 | -51.564701 | 2026-09-24 00:38:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7c1d98e9-0550-3ffb-8a26-b7b1f4d2b1e0 | 1.6006 | -55.961899 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e8c73d-d00f-3e16-b320-e76f6cd2b5a1 | -8.7212 | -47.601799 | 2026-09-24 00:38:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9bce94b5-5372-3f5b-8e02-c1ab9d12cd5f | -8.0431 | -48.515999 | 2026-09-24 00:38:00 | METOP-C | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61641c51-3074-3dbe-937d-e4fe11a4c4f6 | -12.4204 | -46.956001 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7b8655c-9036-30f5-9374-f14b6685067c | -9.2655 | -46.249298 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89090b5f-bfd4-3b7e-9fca-890269c431e8 | -8.9177 | -45.953201 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3587b6a9-76ba-393b-9c32-c9f365a07b60 | -14.0146 | -42.912399 | 2026-09-24 00:38:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f20c85ce-88c1-3848-832c-68f209104a0e | -11.4803 | -47.355999 | 2026-09-24 00:38:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 922852de-2886-3af6-80e0-ce7713f28450 | -3.4522 | -50.081699 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494f4499-add8-3ea8-90f4-d48c228b6888 | -10.2694 | -49.953098 | 2026-09-24 00:38:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11372104-245c-3abf-819c-10fb911e5759 | -9.9985 | -45.189301 | 2026-09-24 00:38:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01cb9f93-f9ea-3b0c-bea1-63a9ebceff5d | -8.7448 | -44.259499 | 2026-09-24 00:38:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c83f4542-1f02-32ec-b99c-6ae3faace2c1 | -10.974 | -54.074299 | 2026-09-24 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eef478e3-56fa-36b5-ae1d-4ecbb194ec6e | -8.46 | -51.486698 | 2026-09-24 00:38:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b54c7c0-6ac4-33bb-ad25-35c5461fcd15 | -2.5666 | -54.7444 | 2026-09-24 00:38:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28b4352f-e443-343e-9853-e50332a157d5 | -9.3935 | -40.291698 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a4ca836c-8fe2-38b3-81d8-5434a59854a9 | -1.0214 | -53.7342 | 2026-09-24 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9104bdb0-e1cc-309d-b2ef-34fab96ffc1b | -12.846 | -44.382301 | 2026-09-24 00:38:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92f025eb-1d2f-312c-a0be-a696c3266062 | -7.4203 | -49.8615 | 2026-09-24 00:38:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d58ff62b-81b8-35f6-94c5-3bcf67fc0437 | -5.7944 | -49.187901 | 2026-09-24 00:38:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06235c71-8402-3771-a0ed-74a042611a33 | -1.789 | -47.8284 | 2026-09-24 00:38:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468e307b-64a7-31e2-8389-810f3bd6fa56 | -3.2032 | -49.085602 | 2026-09-24 00:38:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 061a1467-34bf-3af8-93d8-bc9bdb9fb982 | -8.4641 | -48.690601 | 2026-09-24 00:38:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b8bb1475-a691-3cb5-936b-67a733e2217c | -5.3859 | -46.566502 | 2026-09-24 00:38:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55cecf41-632a-37de-9b3d-6657be5c8822 | 1.5741 | -55.9436 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9481ad65-39da-3692-990a-a3460b568670 | -8.2547 | -54.752499 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14820842-181e-30c8-bc5c-387ab5a8f1a5 | -8.1428 | -49.549099 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b60fc7b2-5b1f-3f86-9e34-1bab519176d2 | -2.8279 | -46.703201 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1495c67-00b6-398e-b2ad-31d482573409 | -3.7191 | -49.0415 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d190ecdb-5252-3f1e-aff3-c4c939160060 | -8.7574 | -45.841702 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| eeae6a4d-a4ee-3b61-8eb7-b5a732513f4e | -9.081 | -46.077801 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd31a3e8-48ba-3b2f-825f-8f767550146e | -15.5565 | -42.3559 | 2026-09-24 00:38:00 | METOP-C | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac8da1a3-d475-337c-bf3c-2b506df65992 | -11.2502 | -51.3526 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0ee200-5b07-3bfd-9e55-300afff25aa7 | -5.6039 | -45.9538 | 2026-09-24 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe4e3c14-b176-319a-9e85-97decb9edd43 | -8.2302 | -48.2057 | 2026-09-24 00:38:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 994ad02f-5250-32cc-baae-285b3637a256 | -7.032 | -44.6562 | 2026-09-24 00:38:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91bb421b-fa33-3699-bc18-ed40400d78b4 | -6.5698 | -44.8834 | 2026-09-24 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0cee61c5-696e-3205-896a-fd724481cf94 | -3.0081 | -51.523102 | 2026-09-24 00:38:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6247453f-7119-3efc-baee-0a85de3ee689 | -4.9937 | -45.552101 | 2026-09-24 00:38:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2e387c9-ae80-3c73-bcdf-4faf879b243c | -5.1931 | -44.691299 | 2026-09-24 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 842a0c82-fc51-3900-a9ba-499eb06c7339 | -9.9967 | -45.181599 | 2026-09-24 00:38:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4726f164-161b-30c1-8008-c305b26a46d2 | -10.9045 | -53.934601 | 2026-09-24 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d4f00f7-091b-3557-8650-0f2f269ced07 | -6.5696 | -51.483299 | 2026-09-24 00:38:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
