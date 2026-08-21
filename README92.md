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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b7d6b84-7010-3fb3-a2ea-7352e56986be | -5.6168 | -43.9965 | 2026-08-21 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 08515047-8d5e-37d9-9d48-fe6eba4ef75e | -9.4071 | -60.417 | 2026-08-21 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 0f6752c2-8cda-31f2-bfcd-b86b4b334995 | -6.8755 | -59.4364 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7c5541d3-5f3f-34bb-ac58-efafb1389b96 | -13.4516 | -51.7736 | 2026-08-21 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1271079b-6c21-3b56-81e3-063aae1eb7f3 | -6.8203 | -59.4001 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ba14f109-86b3-396a-b893-80eba72cadc3 | -8.3717 | -62.716 | 2026-08-21 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 061c5303-9858-3f77-902c-d0ab99a1c36b | -13.2623 | -51.6271 | 2026-08-21 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 9e7989cf-3483-3855-b9a0-f90c3e2ebd40 | -6.5829 | -58.9851 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| c3bf9a98-df58-3ba9-9995-37c0b67f6bb9 | -13.6243 | -51.7732 | 2026-08-21 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ff358f8b-574b-34b0-a9c2-411a1d6b84d4 | -6.2487 | -48.6506 | 2026-08-21 13:50:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 948c34d9-556b-34ad-88db-27a69ec1bcd4 | -9.4072 | -60.3977 | 2026-08-21 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 99280624-a684-3cc9-8e7f-2485de36e4fc | -6.5829 | -58.9851 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 623c9acf-a0f4-3f41-8b24-e35f86505fd1 | -5.6168 | -43.9965 | 2026-08-21 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 0a8c503f-4ee6-3b7a-8d82-a1187decb0f5 | -6.8756 | -59.4171 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 23ce31a2-3372-377e-989c-93dc1da869d2 | -9.4558 | -48.2717 | 2026-08-21 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 245fb3da-d413-3109-b194-c1f91b139b9c | -6.857 | -59.4371 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1ae9f133-d55a-3d91-a474-81d4eb4a4c3d | -5.598 | -43.9978 | 2026-08-21 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 306.5 |
| c9ec4655-79cb-3780-81a9-84bfd50282c7 | -6.8939 | -59.4356 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a7e8f58a-8984-316e-9589-9ed9fd238c64 | -5.961 | -52.2056 | 2026-08-21 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 571b95ae-4293-3ec8-83ef-18b99a8573c2 | -6.8937 | -47.4738 | 2026-08-21 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ac6ae532-77a4-3e35-b39d-b18b71021d6d | -6.1177 | -59.9069 | 2026-08-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 025ca29c-7f52-3ba6-af3e-88065b7706c9 | -8.3717 | -62.716 | 2026-08-21 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 42b6a15c-87da-32fb-9a06-bbeae4aa4dfb | -8.8856 | -60.5394 | 2026-08-21 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 557b8a76-21a7-3b5c-bb87-5befc5f43db9 | -8.3718 | -62.697 | 2026-08-21 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f85be489-9ebb-3e01-b123-33f9d4862fce | -14.3343 | -51.8944 | 2026-08-21 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 2187a951-2587-3d2f-a7dd-a9f16528e160 | -13.738 | -51.8651 | 2026-08-21 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3c26f4ea-f826-33d8-a878-5b07fdd9087b | -17.9546 | -44.3882 | 2026-08-21 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 136.6 |
| bdb26713-f504-331b-be14-767993f23d77 | -13.2623 | -51.6271 | 2026-08-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 35e37dfb-f3fd-3566-8403-907390c7d63c | -11.3667 | -46.0177 | 2026-08-21 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f7c2ab07-d3dc-326c-9fbb-10e8a547a14a | -11.175 | -54.001 | 2026-08-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 660035b2-404a-341e-9e2d-027683d8a12e | -6.2341 | -55.6109 | 2026-08-21 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| efbe3f0f-8551-33ac-882b-f9c4bdef5722 | -14.4514 | -51.8149 | 2026-08-21 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d89ad5c7-6bb4-320a-98ad-c3718942c02a | -6.1361 | -59.9063 | 2026-08-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 1a231222-e328-3d5e-b520-1cb6a5df844a | -6.8571 | -59.4179 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9dcdc2e4-ddea-3fe1-b59c-458cfae1b90e | -8.3902 | -62.7152 | 2026-08-21 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 914e0f03-1a9c-3e0f-b90e-33858557541f | -6.8755 | -59.4364 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 39d4b51f-cb50-3053-9da4-9926e2e34f1a | -11.367 | -45.9949 | 2026-08-21 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| b886f909-0872-3f8f-bcd3-85e002b5be8b | -11.1747 | -54.0216 | 2026-08-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 19aae01c-3cfb-3ecb-91d4-2a7459253204 | -6.5828 | -59.0044 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 90e0080f-cc97-37ee-8bd1-569cca19f62a | -14.3149 | -51.8969 | 2026-08-21 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a67c1878-4be5-3e22-8015-9eaacff4c5b1 | -5.6166 | -44.0196 | 2026-08-21 13:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 333.4 |
| 9c817120-24b3-3d82-b9f0-86c14ebdf20f | -8.4554 | -46.9628 | 2026-08-21 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 7a6b1f21-87a8-34e2-94d9-99ada78f6b7d | -8.3903 | -62.6963 | 2026-08-21 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 290fd517-8c47-3df1-9cca-c0a83fff8ad6 | -9.4071 | -60.417 | 2026-08-21 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 9dcb3664-1678-33d4-9742-585fec50884b | -13.2431 | -51.6295 | 2026-08-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 55644b54-183a-3704-a6f7-23d2349fe0ac | -8.9042 | -60.5385 | 2026-08-21 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| f0279eea-124d-399b-9ab0-9f262aa14568 | -13.4516 | -51.7736 | 2026-08-21 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1ae101e0-c2d3-3c25-a6d1-4109a8e528f6 | -14.1174 | -58.8395 | 2026-08-21 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6b9b86e2-ee8b-30ce-a746-78c0b9c65191 | -13.7188 | -51.8675 | 2026-08-21 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 153.8 |
| f641926b-c039-3586-82ef-a6f64bd2ec2d | -8.8855 | -60.5586 | 2026-08-21 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 88bcf768-db8b-3e22-83b8-fc8338e78e0e | -13.3929 | -54.3551 | 2026-08-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| cb90e347-4d88-37da-87e3-6648f690bc40 | -8.9041 | -60.5577 | 2026-08-21 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| ce61caac-876e-3e76-ad06-ae17afc5675e | -6.1362 | -59.8871 | 2026-08-21 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 475caf90-708e-3532-8c4f-e2d587a4ae48 | -17.9345 | -44.3929 | 2026-08-21 13:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 0fe0e4ff-5981-3c95-94d2-3c0989acc08a | -13.7384 | -51.8438 | 2026-08-21 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| de0bf19a-8f0a-3fa9-bb29-ce718ba64c0a | -13.3734 | -54.3779 | 2026-08-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b1e3d19f-f8b4-3633-ac9d-70e423ebd2e0 | -13.3926 | -54.3758 | 2026-08-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| ae4b4434-6f81-3182-aec1-1b5b6ccdf686 | -6.8203 | -59.4001 | 2026-08-21 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d8a28a29-4ef0-3d96-a3b6-5bdd0bbfa92a | -8.8855 | -60.5586 | 2026-08-21 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 124c2a2e-66fd-3e6a-8d61-da910960f036 | -11.175 | -54.001 | 2026-08-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| fb43a571-7d88-3a4c-8cae-84944d2e3257 | -6.1177 | -59.9069 | 2026-08-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| e62a0740-21ba-3e76-8ea0-255013c8ed96 | -8.9042 | -60.5385 | 2026-08-21 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| add4e124-3296-3996-b926-f890136e1a65 | -6.8571 | -59.4179 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d1a9f65d-f73a-3a8e-a03c-72a98943d4b2 | -6.8939 | -59.4356 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| ceea0ac9-4aa0-3b82-8317-e0dcd1ad3b73 | -9.4072 | -60.3977 | 2026-08-21 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| ef766490-3fa5-301f-9294-192b0dd45d67 | -6.1361 | -59.9063 | 2026-08-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 998c3f67-a57c-3626-b3b8-6e204c6c16d2 | -6.2673 | -48.6494 | 2026-08-21 14:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| af140597-996a-3e44-b07e-1ac0d30b01f1 | -6.8203 | -59.4001 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 29481475-a718-3f9e-b3ba-81033170d006 | -13.4117 | -54.3737 | 2026-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 32f341bb-86b3-3994-b824-7cfe0a336841 | -8.5173 | -55.3441 | 2026-08-21 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e294260d-be02-3d5f-afbd-7622d6974454 | -8.9041 | -60.5577 | 2026-08-21 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| a3fd02f9-f0e6-3874-93bc-5e3f2545dfde | -6.8756 | -59.4171 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| d35db8fc-edaa-3fb1-b2dc-94a0bfe49a1c | -13.6624 | -51.7897 | 2026-08-21 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 27444c05-3144-32cd-b83e-cb61f3d3414f | -1.4188 | -55.7282 | 2026-08-21 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 38ae7c9d-9817-3912-8ab8-c4e65e2690ae | -5.6166 | -44.0196 | 2026-08-21 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 3e7c7918-479a-3779-85e0-6ec906597236 | -5.598 | -43.9978 | 2026-08-21 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 288.5 |
| 99730021-f5ef-35ac-a88d-b90202f2c854 | -8.4554 | -46.9628 | 2026-08-21 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 476266f0-0856-3890-960d-44d677c4d75a | -13.3926 | -54.3758 | 2026-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 85cb0928-6051-376a-b77a-ef7587f04e5c | -13.412 | -54.3531 | 2026-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| bc13ea18-b9cb-36e0-a1bc-0485c1d92041 | -13.3734 | -54.3779 | 2026-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 5e58afa3-1415-35a5-b874-cdc31ee702de | -6.2341 | -55.6109 | 2026-08-21 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 56b5f311-0879-3669-a973-e6d5dccb8230 | -11.1747 | -54.0216 | 2026-08-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| e7cf83bb-a542-39c1-b7f4-6a80946e581d | -5.6168 | -43.9965 | 2026-08-21 14:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| f460740f-e05d-301e-8e64-3e821a5dfd09 | -8.3902 | -62.7152 | 2026-08-21 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 40e817c5-7f8a-3e30-9103-618b2b8b1699 | -13.2431 | -51.6295 | 2026-08-21 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8a209e29-1ffe-31ee-82c6-24d8313e4a13 | -6.5829 | -58.9851 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| c09a22f0-7e8c-30f1-9533-e3a1e551cd60 | -8.8856 | -60.5394 | 2026-08-21 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| ac3299d9-33f8-375b-8515-9340d5452cfb | -11.1561 | -54.0028 | 2026-08-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 1911ed76-4a06-3946-b413-f728f47093a8 | -9.4061 | -60.5518 | 2026-08-21 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a341f181-b36a-3824-841a-2faae8c6937a | -17.9546 | -44.3882 | 2026-08-21 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 813e4c71-e5b6-30a8-8a10-569333842655 | -9.4555 | -48.2936 | 2026-08-21 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b80ac6e4-c70d-3acb-b3dd-850929c4d28a | -9.4071 | -60.417 | 2026-08-21 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| ec10f975-b601-3579-bd1e-2059373df9d9 | -6.8755 | -59.4364 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| b1b56f03-3cfc-3f52-990b-259d2ef57966 | -6.5828 | -59.0044 | 2026-08-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b43890d9-7991-3696-802f-89c73ed2e6d2 | -15.6958 | -53.7667 | 2026-08-21 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c0e3a14c-f5e1-380a-af37-73bab264734f | -9.4257 | -60.416 | 2026-08-21 14:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2bd28032-1a30-3377-ba58-2016b95c83ca | -8.3718 | -62.697 | 2026-08-21 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c68932d2-217b-356f-bf84-05ecff73d865 | -6.2487 | -48.6506 | 2026-08-21 14:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 170.6 |
| c529e7f2-beda-3add-b8d2-350e3ad47ca0 | -13.3929 | -54.3551 | 2026-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 5fc98a4b-9d45-32df-a4f5-fee3697253cb | -13.7188 | -51.8675 | 2026-08-21 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |


[Clique aqui para ver as próximas entradas](README93.md)
