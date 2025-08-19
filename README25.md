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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 989557e8-1f46-3c47-acae-481a1dbeb124 | -8.09517 | -44.8379 | 2025-08-19 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46908ebc-aae4-3816-a615-41ecb5d6fb7f | -9.05089 | -50.1791 | 2025-08-19 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 158e6cdc-507a-3228-9c8e-5657d9823b61 | -9.71418 | -51.97132 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f3d55230-95ae-3eef-a2fe-29eb752b1f09 | -12.63132 | -46.88756 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9fa579e-9fe7-3c3e-b863-504cf1dac169 | -9.18638 | -59.64578 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5a0b2dab-90a2-37ba-ac84-dcf4eba75a5c | -13.58838 | -47.00491 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 457eb59b-7f56-30df-8b4a-9f3d8bc471e7 | -12.99757 | -45.20507 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f5e0995-6883-3733-9b66-aba94610882a | -14.17654 | -45.32103 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6cbbb92-50a3-39b6-a980-ffe67e07d17e | -8.97014 | -60.50394 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a34cfa40-d4fa-387b-8da7-473d40528399 | -12.95769 | -46.12611 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57f52d6a-7577-3d0b-9b97-649989a1344d | -7.99719 | -48.41488 | 2025-08-19 04:27:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4224944f-40e8-3e2a-80ea-bb35e3cfa332 | -13.47183 | -47.05671 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeccef25-036d-3193-88ad-a07e8a229702 | -12.99122 | -45.19733 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a498aaaf-20bc-39d6-b89a-6cbc458a0bdf | -13.25713 | -50.8002 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5723901e-554a-32b0-8ed2-599a6aeef5f5 | -12.63901 | -46.90015 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5891e814-fafa-3a9e-aafe-c5c43d2f2c50 | -13.17966 | -54.95376 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bca45d22-ac73-35cf-9ecd-6ca532e1859a | -14.17001 | -45.31578 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 939aae25-0edb-3950-b963-fb6b39986a28 | -14.8727 | -48.06625 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7dd4db7-09ae-342b-b6d7-0ac63eaa92e2 | -11.93643 | -50.44265 | 2025-08-19 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fa0baa1-364b-3f77-b45b-88210be97778 | -12.99519 | -45.19642 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a6d1f269-95e5-3698-a6e7-ff829a3eb5ac | -10.36243 | -49.9253 | 2025-08-19 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8d4a0c5-3c8d-3747-a57d-43c5f18260a9 | -9.17977 | -59.64496 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2f48ab1f-fcff-37b5-9bfa-3fa164f034a0 | -12.49856 | -45.56647 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e5c3ebd4-bce9-3e7c-baa8-dbda223f9b63 | -12.97735 | -56.85776 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47f084ed-252e-3108-a038-b34118727404 | -11.86459 | -51.57536 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46a5b0ae-f45f-3649-8b10-19e7fec68294 | -13.882 | -54.04248 | 2025-08-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 891d906d-278b-337f-99b4-f0b5ab0dd9c4 | -14.17299 | -45.32046 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 771a90ef-9e35-36ad-9f2a-0415217b742f | -9.04011 | -50.17728 | 2025-08-19 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8fa2b2c-2ba9-3e4d-82c3-3cdebef13b07 | -9.71024 | -51.9706 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 41f012d7-3e77-3c95-ae30-51631a703ef9 | -12.37632 | -54.16141 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5ec1ec0-9516-342c-843b-c42ac83c754a | -12.9803 | -56.84215 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8149e92f-7ba3-3468-be3e-96f2ac2228c7 | -8.0865 | -46.66504 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d09a9653-5be6-32a6-9dfd-1ea4257d2740 | -9.18537 | -59.6468 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d938ecff-c013-3a7d-a20f-7be9226e3657 | -9.19717 | -59.6248 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 063edcca-0e02-37a5-8050-b0fbfe4364ec | -10.58224 | -49.13737 | 2025-08-19 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2c0f308-9bb0-3017-a7e7-c9fd808db77c | -12.64923 | -45.33251 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bc82c45-d75e-35a2-9ede-a74f10abd63c | -13.34755 | -54.41143 | 2025-08-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ffcbff9-bbf6-3508-9f06-a291941fa96c | -12.97398 | -56.84743 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5e3848b-bbbd-3cbe-91d1-a6b75a9c853f | -12.92249 | -46.10522 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5dc27d3f-1a86-3661-b1dd-74cb96b536f0 | -12.65017 | -45.81675 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80b6d8e0-5e09-3f66-a30d-1c6a1520dea6 | -14.86938 | -48.04378 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d6a3235-058b-3c4d-bf4b-8a4ba17d5e0e | -13.00168 | -45.20155 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a291f3f-9e8a-3123-8e9a-d866a2bb59dc | -14.84568 | -48.06544 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 087c6998-fa03-3f8a-88af-061a3608203e | -12.4465 | -46.98273 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebcddd11-ffd7-34a2-9910-1386d4b7ca10 | -7.12404 | -50.42077 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76f99d26-73ff-3ea9-b268-eeffb0a8c6f6 | -12.77705 | -41.25283 | 2025-08-19 04:27:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21b6ddfd-68f0-350a-8196-457aa722e655 | -13.16784 | -54.94189 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 225a4574-c84a-3983-8620-20a3a0a1d7f7 | -12.0389 | -44.01281 | 2025-08-19 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d50f6926-25e7-310a-aa08-aa61afaa0b5a | -12.98734 | -56.84424 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4345a662-c2c4-3fc1-a475-aa505b918b84 | -12.99404 | -45.20453 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5aac752f-0f95-3a6f-a633-550fcac8d58f | -11.85339 | -51.57341 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4bcfe34-2d23-3d6a-9c11-f8860b9f31ee | -13.00147 | -56.85375 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1108b1c9-654a-324c-9f10-38c0bc1518de | -8.824 | -52.06646 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d91eb28-1c2a-3414-8115-d1633931cec0 | -12.987 | -56.86311 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 999f7c84-c1f1-34c9-b204-08be28567371 | -13.25657 | -50.82521 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e39e49ce-d565-35f3-9a5b-114a66cd088d | -14.8749 | -48.05198 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6eb89ac-0fb7-3987-b468-602f98682c55 | -12.97854 | -56.85145 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e9151d62-a77e-3487-ac40-59b76656a897 | -13.15969 | -54.93547 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7edc4991-6761-3996-93ec-72da15a2e5c2 | -13.56669 | -47.01247 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a51cf76c-ec3c-3674-9645-b5d22e3e5f98 | -11.492 | -42.95244 | 2025-08-19 04:27:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba80547e-dd68-3b65-be6b-1f19e2395e26 | -14.74295 | -46.29729 | 2025-08-19 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 551772dc-780c-3122-a584-8ed1c29bf8c3 | -12.98761 | -56.8599 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5166c37-062f-3a94-937b-93dbfae67ac5 | -14.86386 | -48.03559 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 957dec70-4b92-30f9-9d5b-370d5fe101cb | -7.26495 | -50.17936 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2431cc1-e68f-3aff-b35e-13062d28dd66 | -12.99116 | -56.84105 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6b5082b-cb14-392e-90df-6d406e168d02 | -12.64788 | -45.80856 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01798dc2-2644-32b0-b08e-978959b1adbb | -13.378 | -54.4169 | 2025-08-19 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f84b221-90f4-3063-b129-1de570a7f401 | -14.17474 | -45.30808 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aedc439e-2b46-32f6-b06c-fab04da17379 | -8.23527 | -47.86119 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 047f8814-81b1-3cbd-8421-88c5c49b6c70 | -11.85713 | -51.57404 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3be3f64f-a480-391f-894c-c3de2c5abfcd | -12.04261 | -44.01334 | 2025-08-19 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cb36cbad-7ea3-39f2-a41e-8e0516a34825 | -14.51032 | -45.94457 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14c918f5-3f86-370f-a5b4-f0edb09363d4 | -14.17829 | -45.30865 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba2652d0-f330-3151-ba5d-da4174c09588 | -12.49914 | -45.56261 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e06ac67a-4b89-3ad5-884b-35ecb95464b6 | -12.99416 | -45.20191 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a6108a9b-b7b3-35a9-9d1a-bff89c95f2cb | -13.44171 | -56.85248 | 2025-08-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3dbdb23-c543-3ea7-bc15-1b0ba0c938f5 | -13.67287 | -44.22093 | 2025-08-19 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c957c796-ff1f-3c28-a61a-f8d7f6637636 | -13.17323 | -54.93803 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe13f62-a3c7-3e63-b879-971026116640 | -13.86555 | -42.62491 | 2025-08-19 04:27:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b62b8f1-2344-35cf-a890-904434bd7c7f | -11.74064 | -58.32619 | 2025-08-19 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6922d39b-e77d-307d-bc0f-6befb42df646 | -9.19506 | -59.63581 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e76f9a20-093b-3c96-b598-7972b9e2348d | -12.91853 | -46.10837 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ff92a5d-e14e-3e60-9c14-8b7f944b241f | -8.82085 | -52.03611 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dd94a3a-2a50-3542-b834-64565094d478 | -10.9651 | -49.57002 | 2025-08-19 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f40038b5-b3f4-36bd-937f-fa0c8221f39f | -11.34353 | -48.12569 | 2025-08-19 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b3149ed-4330-34db-ba82-adb60643e2f9 | -13.0011 | -45.20561 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da72d3f7-3864-30ae-93e6-38015a3da41e | -13.16683 | -54.92219 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8dbee9a-8ca2-3ed2-b1e2-5ebb9b794e62 | -14.51995 | -47.2891 | 2025-08-19 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3415bfe8-d099-348e-a12c-e7b36133f070 | -8.70414 | -50.69044 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8f0e28d-c407-323e-9ac9-c29d02e1d2b9 | -12.50798 | -45.5912 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6206edcc-731a-30aa-a636-8b5913bc82f1 | -13.38179 | -44.30883 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9723d33c-e17b-3f35-adc9-0a8e2ebb5ffc | -8.71463 | -47.8618 | 2025-08-19 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81a7e243-cdef-3c57-86ab-b14d6ce13d10 | -12.64617 | -45.82005 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 912d2267-0249-3807-a9c8-4efabbd40494 | -7.25538 | -50.16877 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 043bc064-98d4-3420-be2c-f3997058c205 | -10.60765 | -46.36542 | 2025-08-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8864ad1d-1db4-3c74-b3ba-5b7b92426106 | -11.83793 | -50.59707 | 2025-08-19 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7671944f-65d3-364d-a665-f14cdf73bfac | -13.17514 | -54.95291 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3df3e8ea-f452-3990-b685-7d96eb761a03 | -13.14408 | -57.15144 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4ebc02e-0d8d-3922-ab8b-5d699871e4f4 | -14.87269 | -48.04431 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73ae0426-e433-3077-83d7-d282d2b081b2 | -12.99758 | -56.84636 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README26.md)
