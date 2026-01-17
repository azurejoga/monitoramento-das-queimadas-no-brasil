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
| 470e5690-ad10-3ac4-b376-87ad31d6f5b8 | -12.88308 | -48.60772 | 2026-01-17 12:16:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6e240803-4cbb-36db-ad4c-189fc2dca780 | -13.99591 | -45.79628 | 2026-01-17 12:16:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 25562320-0b36-31ab-8e38-61f6be46f359 | -15.67423 | -43.50504 | 2026-01-17 12:16:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 581ad0fb-d5b5-370a-9730-b3040fde2ce0 | -12.67057 | -46.76123 | 2026-01-17 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| deb6907c-6b4f-31eb-a7a2-df48ccf6ee3b | -15.49175 | -50.94663 | 2026-01-17 12:16:00 | TERRA_M-T | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 14bebfdf-e6b0-3db9-ad9f-c89d17c5005e | -12.68828 | -44.98864 | 2026-01-17 12:16:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3239d17a-ef07-3ea0-9070-79f9d70d5dab | -13.99765 | -45.78226 | 2026-01-17 12:16:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 3b30bcd8-49ce-37c0-a427-ab60e8190867 | -14.74721 | -45.91242 | 2026-01-17 12:16:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| cebf9e48-1b2b-37e1-a566-c048c59af641 | -12.68944 | -44.98296 | 2026-01-17 12:16:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| be135b02-2be7-3df7-9571-b27db7c5e161 | -14.79038 | -48.99641 | 2026-01-17 12:16:00 | TERRA_M-T | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc0dfa83-d90d-3d4c-ae1e-118ecd0a2322 | -12.65915 | -46.77139 | 2026-01-17 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 95bb3801-0f79-3a5d-a004-066e1c5e60bb | -13.9868 | -45.78082 | 2026-01-17 12:16:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 9e3668ae-ff16-342f-8b01-6a5de064b54a | -12.65071 | -46.75856 | 2026-01-17 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 003cc44a-1990-34bc-8377-0c13e517017b | -12.42207 | -47.1803 | 2026-01-17 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 79d93170-4c03-3c38-90f5-34cec6b4060a | -16.6121 | -47.11025 | 2026-01-17 12:16:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 66786c67-22d8-36c7-a6df-1823e786a0f4 | -12.66064 | -46.75988 | 2026-01-17 12:16:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 8df336bb-565e-3f23-adca-e9e7f2600313 | -13.95518 | -48.51236 | 2026-01-17 12:16:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9c422f9b-671e-3cb6-b773-bb3b4afb8102 | -12.6901 | -44.97355 | 2026-01-17 12:16:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 81fac1a8-91b2-3330-9af4-158eb7499c36 | -15.01971 | -48.66568 | 2026-01-17 12:16:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7cb33a17-23e8-3c39-b881-3e2a3949d90c | -15.49042 | -50.95579 | 2026-01-17 12:16:00 | TERRA_M-T | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5ac22ecd-067e-33fd-ac4f-2926cfeef793 | -20.17624 | -48.91088 | 2026-01-17 12:18:00 | TERRA_M-T | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a80f6a5-a725-3113-b7ef-6735d7aedbd2 | -29.49592 | -56.34002 | 2026-01-17 12:21:00 | TERRA_M-T | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 4.8 |
| 3b887089-a971-3a9c-a742-754bfc357041 | -13.6993 | -55.6773 | 2026-01-17 12:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| da3d95eb-8287-3480-8d3a-d9b468ec26b6 | -13.6993 | -55.6773 | 2026-01-17 13:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 6ed9d48a-14cc-3738-84ef-6ab4d91b232c | -20.4496 | -57.8686 | 2026-01-17 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.5 |
| 1826a1df-7e48-3c62-87cb-3a076e13fd7a | -13.6993 | -55.6773 | 2026-01-17 13:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b4967055-6bb1-3462-b336-82f4b1fa7f85 | -20.41 | -57.8323 | 2026-01-17 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.2 |
| a2b67eca-6fbb-3a7c-afa4-3bf6c47b4155 | -20.41 | -57.8323 | 2026-01-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.0 |
| 5ba65bc5-0e74-3d17-bfbd-ae1286fb7867 | -20.5279 | -58.0039 | 2026-01-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 172f23b7-489f-33ca-a42c-32f007b4fc7f | -12.6745 | -46.7605 | 2026-01-17 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |


