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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66f5e353-b5ab-3002-982f-4462be668053 | -6.78489 | -59.46955 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb4e8c61-09ae-3deb-83cf-bdfd2ebdc96a | -6.65056 | -58.95602 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2ce3ab31-c39b-3bb4-847f-5c2a2a9d97cc | -8.9533 | -60.56947 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71e053b2-848d-3239-b048-06bfd3026fc9 | -6.10211 | -57.73335 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23da32e1-01b2-34d7-b162-8cae70577fc3 | -3.80455 | -59.33543 | 2026-08-17 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64372e98-fb26-3d42-8bf5-cfa90074811c | -6.77252 | -59.76238 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 751774eb-b5c8-3aa8-a90c-fffe5575aab6 | -7.88275 | -61.7979 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8659bb99-a7ab-3f79-b5df-7480e98b81ac | -9.27132 | -45.65197 | 2026-08-17 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a426a3fb-e4b5-31cf-8dc5-93a498a4f7dc | -6.97964 | -59.04607 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a11784d-bae6-3c29-8d05-985c7f2aa591 | -7.37134 | -55.51048 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd24afac-94e0-3a3f-ae39-8d8eb4bd3940 | -6.65218 | -58.96737 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c7a8e07-823b-3663-874c-58a4a9ccbfe1 | -8.06937 | -48.5367 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52953d60-7421-3d53-a140-01245060066c | -6.6236 | -59.05869 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2e77d69-5d02-3a07-be73-99d8db4afaa9 | -8.0629 | -48.52973 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2536f987-971d-3fa4-8ea5-450cb17e7152 | -6.10098 | -57.69774 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3efad5e4-e4d4-3dc0-87f0-98fb9eb8cb99 | -6.70549 | -58.95757 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b20b48a-b37f-3511-9f70-d9be427d8110 | -8.94477 | -60.5122 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0421b7c0-6fbb-37c4-b2a6-06e4ebd5ea65 | -7.42035 | -60.0237 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26fac804-4b18-3ec0-97aa-1ac45924faa6 | -9.12719 | -46.02099 | 2026-08-17 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 959426ee-a84d-3443-b8d3-86cec07da7d3 | -9.57926 | -57.01969 | 2026-08-17 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4386fbdd-856a-3c70-b558-bed5a6b307da | -6.62419 | -59.05507 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ef210f-e029-3f6d-98fa-32c79a5be334 | -6.1054 | -57.71261 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1ebe6e9-4a27-3957-8457-237d061e1bdd | -8.4289 | -62.69987 | 2026-08-17 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 89906168-65b9-31e3-9b64-4abe03f5f22d | -8.9732 | -60.51296 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b07727fb-8f9b-35d0-a2be-e99b02f46c10 | -7.37777 | -55.4919 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f3e8c0d-2d15-39ad-862c-288f6622006e | -7.42162 | -60.01603 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6600f52-6418-349c-a2e1-4fba0f4df92d | -7.61217 | -55.26433 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f09b97d-8a91-33b6-85f8-67958abd278a | -6.84645 | -56.43306 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38edcfa6-b0c8-3d8e-ba43-eeee94c93c8d | -8.06394 | -48.53593 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2e8b7f70-ff20-38fc-9b00-2de86ce5e8b1 | -6.97349 | -59.0414 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be8f5432-96a4-38da-91e9-07fdcbd9e388 | -6.98358 | -59.04302 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07342cac-b0c5-3eef-a226-60d528b129d8 | -7.36331 | -55.49356 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 073be483-ae8a-33f9-9ae1-f25cae84d802 | -8.523 | -54.90973 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79809888-391e-341d-be45-d6e8ff967ff3 | -7.38724 | -55.48869 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3be7d039-085a-3327-af00-4149a6672c6a | -11.48307 | -46.58022 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3550b0cb-dd14-35a5-90fa-aeac82513d38 | -10.9247 | -57.12421 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8592a384-1282-3588-a30b-01b2bc409917 | -15.16706 | -48.64747 | 2026-08-17 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b625105-2ad3-3c5d-895d-3288015f34f6 | -11.49737 | -46.61318 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ef8977d-5a8c-337f-8645-bb6ab5fa7711 | -14.48463 | -45.68245 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 960d4041-8433-373f-b1ea-00fd6e010d74 | -16.66829 | -49.44991 | 2026-08-17 05:18:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5421d4df-9515-3afc-af23-cad1c3affb2e | -11.91991 | -55.45063 | 2026-08-17 05:18:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3d5452b-3d64-3f9f-8541-5f91f5043c66 | -13.51662 | -46.24053 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f7637a83-005a-3fd1-9ab7-155cce660870 | -11.22922 | -54.01226 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb8fee4-0649-3ac5-8afc-06e34c49d7a4 | -13.54716 | -51.8283 | 2026-08-17 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 311f19a7-a727-3bbd-95ea-ca07f069418a | -11.24102 | -54.01386 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cafe9209-86a5-3079-96ef-980d1a47fa8a | -16.71888 | -49.1315 | 2026-08-17 05:18:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db736531-8976-34a8-8964-964e3a1c56c1 | -15.78854 | -55.56916 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 159ff800-5e16-34ea-9541-4e849764a21b | -15.78791 | -55.57363 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4eecf899-c6de-342b-8731-71060e862426 | -13.42988 | -57.05906 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29c724b8-062e-33ea-b698-96b0473228e2 | -11.72403 | -54.60045 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 504b59ad-0546-3f29-980b-3790d0af203e | -14.3687 | -51.87162 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb98d00a-7064-3cd0-b0b2-05ead72da579 | -12.04759 | -46.4805 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43190554-3070-388f-89c6-14ae291bde8c | -15.81802 | -55.52528 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10bee566-57f8-39e1-9096-a8f96b7c7343 | -9.32986 | -62.33411 | 2026-08-17 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3cc85595-b184-3c25-afe8-309d84f5e8b5 | -12.70629 | -48.52481 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b8b4855-60fb-3a6a-899c-f85d1830eaa0 | -15.90418 | -56.48766 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5714bd6b-9f97-353d-bfe1-92381255d8fc | -12.65666 | -48.49587 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aaf778a-922a-3d97-811c-6b3027d64693 | -12.76504 | -48.42919 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2cbdc3b-a334-3e00-9eb1-0d20b14ece22 | -11.71295 | -54.62307 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56a61ca6-ec99-3a16-87d8-aafa2e866f75 | -15.81236 | -55.53136 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed7ec7bd-345c-3e7b-b11f-69874d43c68b | -14.75062 | -56.33907 | 2026-08-17 05:18:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 967f6b49-2490-37c6-9bed-86fa0d8bfa5b | -11.23709 | -54.01333 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c4c8e16-f413-385d-b7db-10ad3d25ba63 | -15.45779 | -53.04247 | 2026-08-17 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19c7ca7d-64a0-3180-b590-3279d453d375 | -11.91171 | -47.34951 | 2026-08-17 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcbfbfad-36b9-32bf-9fc0-c40e2fca2d28 | -12.75872 | -48.43251 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be93cb9d-da4d-3e2c-b63b-cff3d4e95679 | -12.0398 | -46.49462 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3c6efd57-380a-38f5-b1bf-f6caefafc8c8 | -15.91936 | -55.53849 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 88177a5d-99bb-36ad-bae1-7afe23c555c8 | -12.71147 | -48.48164 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19a76575-b438-3257-a96e-c195be510722 | -13.50611 | -46.23728 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 48dab4d3-85d7-3b32-be48-1ef87d0d2f1b | -14.38909 | -56.40275 | 2026-08-17 05:18:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 583f52b2-365c-3225-8cc9-cf9e8de5fe19 | -15.82934 | -54.21334 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d82ca3a-0328-3dd0-88fe-2a2c6bc2e553 | -13.5071 | -46.22768 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 61b5c9c6-341b-3558-bb34-ea6ff0769c2a | -11.4736 | -46.59399 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cbe39db-e2fd-3507-a213-cafd822440b4 | -15.81638 | -54.21594 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98fbf4a1-d212-3781-be2e-23a8d57d632c | -16.04724 | -56.52903 | 2026-08-17 05:18:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80ca5382-7304-3002-94db-c5b8d118d313 | -14.3005 | -53.09209 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f831b585-64fd-3cf3-ab4e-123be8ad317b | -14.87272 | -46.64772 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34f4287e-f06a-38b1-bf60-c25d6cbfaa96 | -14.32048 | -53.04916 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a61d9b9-7d42-3474-ad49-29c95d99d607 | -10.07286 | -60.49639 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 725c9543-7ca2-3cb1-8840-d58b6338aff5 | -11.4958 | -46.5831 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e6715293-e02c-3c1f-8400-270cd7d7d8b9 | -15.26523 | -52.90581 | 2026-08-17 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 622ff16b-63ef-3174-ac1b-165bd9e5c336 | -11.70358 | -54.60717 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78a157c4-28d4-39af-8a96-dcc451be02b4 | -11.73513 | -54.57062 | 2026-08-17 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa1179de-42d1-3934-9c3d-a2407a60d9e3 | -14.08876 | -58.4462 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae03a2cf-69a3-358d-944e-06d22715658b | -15.02316 | -52.72702 | 2026-08-17 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d0d65a1-699c-349d-a8ee-b4d55edd2a08 | -11.71744 | -54.61893 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45242287-28e0-335d-9601-f76f1a9b2066 | -9.47579 | -60.50242 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76f90384-4ab9-3908-b2d4-75cba06a7bf6 | -11.81201 | -44.80647 | 2026-08-17 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 807221aa-8690-30df-8dca-f4391e84d258 | -14.37967 | -51.86952 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0dfb1844-b844-3dae-a7af-50589e04430c | -13.50835 | -46.25391 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05b3e575-0225-3c02-b1c3-b28cc7bc035b | -15.90765 | -55.54471 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| aefa33f7-4341-3173-b947-4bba8d35487f | -12.67284 | -48.50977 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c9b72bf1-c464-3e05-ba2f-7c1e45a5457f | -14.87053 | -46.64349 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7378b492-85b3-35fb-894b-dbeb864e04a7 | -14.49868 | -45.68383 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e0c5f97-824d-3f12-9b20-87fd53dc8a06 | -11.4989 | -46.61294 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f389e96d-9764-3a44-af13-fabd80bb7d69 | -14.4947 | -59.32795 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 356ce744-9691-37cc-9abc-53ac06ec20ce | -14.86999 | -46.6489 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3b505dd-dc7e-3772-8c2b-b21f3fd9ed86 | -14.5073 | -53.02013 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b27e7f08-7569-3a13-8c98-3a3856e0e1ba | -12.00353 | -46.4659 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f3d98f7e-40a9-3d16-bf2d-31a008329b77 | -11.70914 | -54.62249 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README54.md)
