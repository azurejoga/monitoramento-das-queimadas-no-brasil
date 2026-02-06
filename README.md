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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29af65da-0ae1-3595-951b-b94b9c44277c | 1.3585 | -60.084 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0858edf2-2f07-3d3a-bf9e-3019e7bdc505 | 1.4852 | -60.9363 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 5b2fa6f4-6d83-3c1c-ac50-6c83dc159909 | 3.3282 | -60.9128 | 2026-02-06 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c7920201-43f8-33f1-a24e-b5abb86fc47d | 1.4853 | -60.9174 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 209.9 |
| 44e999b4-2bd0-34c8-9135-5a30b0998a46 | 1.3585 | -60.065 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a1da20a8-d007-3f17-bf6c-e55e5967b549 | 1.3403 | -60.0652 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| db552911-59d8-3c63-b3b6-2af58a3b27e7 | 1.467 | -60.9175 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2241770a-ad60-3907-a506-b183dd71527c | 1.4853 | -60.8985 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 986beb11-8e4c-3190-b1d8-07bb65c2f299 | 1.467 | -60.9364 | 2026-02-06 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| b05e0222-d8c4-3858-a513-90d018a3b462 | 1.2852 | -60.4265 | 2026-02-06 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6a7df0e5-c509-3f59-8a19-6fe9cd6ac982 | -3.1894 | -48.0289 | 2026-02-06 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| d80bdc57-4c3b-348e-ba6c-7573746f06da | 1.467 | -60.9175 | 2026-02-06 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 31e7f5af-e549-3b42-8a99-be04dad1b902 | 1.3585 | -60.065 | 2026-02-06 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a5f16519-d7b5-3877-8166-03b1f9cc2b1c | 1.4853 | -60.8985 | 2026-02-06 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 809247db-e443-387e-84ca-7f54235b82b0 | 1.3403 | -60.0652 | 2026-02-06 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 7bed0ee9-d9d3-33f6-a011-af7b8d5444a6 | -3.1895 | -48.0073 | 2026-02-06 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7c5e831b-94b3-36d3-8ab9-cffe1b149db1 | 1.4852 | -60.9363 | 2026-02-06 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7c5a874c-43bb-3135-a8e1-a0401b5a806b | 1.4853 | -60.9174 | 2026-02-06 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 215.2 |
| 9241bcc3-32dc-3aea-90e4-cf3d8fcb17f7 | 1.467 | -60.9175 | 2026-02-06 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3ef54258-6a8c-39a1-a6de-e07c6d9c452e | 1.4853 | -60.9174 | 2026-02-06 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 0aff3a17-ca45-38b6-8d56-c24e29ca8298 | 1.3585 | -60.084 | 2026-02-06 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c33fefd6-d6c1-3a7e-9de8-44b70d9ce0bb | 1.4853 | -60.8985 | 2026-02-06 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 641d20c4-cdbe-3d70-9639-7cb383c4bde4 | 1.3403 | -60.0652 | 2026-02-06 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 11689d0f-2c18-3d63-a9d5-cf2b5236da8e | 1.3585 | -60.065 | 2026-02-06 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ba21201e-7eb1-3921-8076-dbef83b0e73e | 1.4852 | -60.9363 | 2026-02-06 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a071faa8-cc94-3e86-b223-bb61e1aa4590 | 1.4852 | -60.9363 | 2026-02-06 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 065fbe41-1b41-3c99-a966-fb91b7490c46 | 1.3403 | -60.0652 | 2026-02-06 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.8 |
| fee239d4-cbc5-3ad8-a108-8b57f41815bc | 1.3585 | -60.065 | 2026-02-06 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7dca1cea-87d4-3001-b380-e8b79414cb2c | 1.467 | -60.9175 | 2026-02-06 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 52697007-49e4-3c8c-94b6-8adb6300c35a | 1.4853 | -60.9174 | 2026-02-06 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.7 |
| eaefa415-7ac4-3490-b828-aceafa140aad | 1.3403 | -60.0652 | 2026-02-06 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 810fe895-0eb5-3e9e-881e-b7b64f99ec35 | 1.4853 | -60.9174 | 2026-02-06 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.8 |
| cfd394de-ba32-3bc5-8b45-f9cbfb67c8b3 | 1.3585 | -60.084 | 2026-02-06 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 80fc76ba-7dbd-30ba-9112-09232fb3e89a | 1.4852 | -60.9363 | 2026-02-06 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 732b44a5-0f3b-3a25-8371-13772255dac0 | 1.3585 | -60.065 | 2026-02-06 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ae433853-26a3-37ad-8a2c-e4ed79f4408b | 1.467 | -60.9175 | 2026-02-06 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5ca02dd3-cc58-3914-b9a2-27ec2283c7a5 | 1.3585 | -60.065 | 2026-02-06 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 2e5f6138-e977-3fac-896b-e36f3c385974 | 1.467 | -60.9175 | 2026-02-06 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c945a98d-4a15-371f-b466-6c19e8f3c753 | 1.3403 | -60.0652 | 2026-02-06 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e3a3c58c-4ef8-3665-870f-e6e2731deb15 | 1.4853 | -60.9174 | 2026-02-06 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.2 |
| bfae6940-9f7f-3189-8382-1980521cee07 | 1.4852 | -60.9363 | 2026-02-06 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b4f7e0b6-9447-355f-91f7-44afb7b8b1f5 | -10.088 | -36.0968 | 2026-02-06 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 149.4 |
| 78b8e5e2-2292-3667-b220-af37198f9b67 | 1.4853 | -60.9174 | 2026-02-06 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 9dd2f2cb-74b6-39e9-9160-7d40f12d1fb3 | 1.467 | -60.9175 | 2026-02-06 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 21d0c374-cf98-316e-a59c-e50b72b45c99 | 1.3585 | -60.065 | 2026-02-06 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f0f8d552-7006-31b0-8747-9a122d918cc3 | 1.3403 | -60.0652 | 2026-02-06 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 270e5be2-ef08-3e98-8467-1f29856e6db3 | -2.8144 | -49.2844 | 2026-02-06 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e6bce8c7-c762-32cc-9cb2-f8ec14101271 | 1.3585 | -60.084 | 2026-02-06 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| adea85e0-cdca-3948-b0d6-173f360db233 | 1.4852 | -60.9363 | 2026-02-06 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ccefd227-38cd-3130-bd1e-937318274371 | 1.3585 | -60.065 | 2026-02-06 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9e030228-e1c8-3b97-a0ee-93e37231a9b7 | -16.58112 | -57.79818 | 2026-02-06 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| dd63fd7d-625c-3ffa-9c76-1ca8c4af6306 | -16.58392 | -57.81513 | 2026-02-06 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| c7eca9fa-f3c9-31dc-a3e6-2e3dd98f40b5 | -16.58988 | -57.80848 | 2026-02-06 01:24:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| fdd42de5-4323-386c-8990-ff6ca491be45 | 1.3582 | -60.06049 | 2026-02-06 01:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a86a14f6-3a1f-3ab9-872d-93c285c0bb9e | 1.34835 | -60.0761 | 2026-02-06 01:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 570b8c98-f2f6-3a67-8af9-d04a1b68b11e | 3.32399 | -60.91497 | 2026-02-06 01:30:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 258087f2-6275-39b2-ba07-c24212a41707 | 1.3551 | -60.08354 | 2026-02-06 01:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 0e468bf6-44af-384a-9b54-afc936a1b7c3 | 3.32316 | -60.89894 | 2026-02-06 01:30:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ab394362-861f-3dcc-9e42-5e724f7b82d3 | -10.175 | -36.5928 | 2026-02-06 01:40:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 135.7 |
| ceec36b6-60ff-3fcc-a188-7783d903de23 | -10.1755 | -36.5659 | 2026-02-06 01:40:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 966cea79-482b-3401-9e1d-db2df31a1294 | -5.10091 | -39.46984 | 2026-02-06 03:10:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4fea775e-467a-3fd2-8259-6263a1939f1b | -5.10218 | -39.46278 | 2026-02-06 03:10:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 21477a69-c8b4-38ca-b3ea-62dff57a8d12 | -5.10335 | -39.46427 | 2026-02-06 03:10:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bd8f1ad5-f31a-3999-8ccd-6ebc13f55874 | -10.09155 | -36.09943 | 2026-02-06 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 35ef91b0-4f18-3254-bfed-e83a3307fddc | -10.09282 | -36.09259 | 2026-02-06 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| f4cc62d8-2f9d-3044-a041-86141f84134b | -10.09219 | -36.09598 | 2026-02-06 03:12:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 774d293b-9baa-3a40-be37-55c2d8d1eab0 | -10.21022 | -36.372 | 2026-02-06 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 50eb2ba7-c7d1-308b-a2cb-54edbf8c7d58 | -10.20538 | -36.36749 | 2026-02-06 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| bed499d6-fdd8-3a3f-8325-9c46beb263ad | -10.2047 | -36.37107 | 2026-02-06 03:12:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 83fbcc00-fecd-3b43-a26e-6dd631e651d8 | -10.32254 | -36.78107 | 2026-02-06 03:32:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9fe64fd-10bc-3853-a060-6b1ff1282c4a | -9.40012 | -35.5481 | 2026-02-06 03:32:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 91af173c-b98d-39bc-adc6-3dc6138453e1 | -10.09037 | -36.08964 | 2026-02-06 03:32:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1d8e4ddd-a93d-3194-ba14-7c3800caa2d4 | -10.09328 | -36.09441 | 2026-02-06 03:32:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8d19514c-4e67-331e-b4b9-b1c025218f9a | -11.13306 | -37.19616 | 2026-02-06 03:32:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 101ff99d-2afa-309a-b542-ec6cd9c151a1 | -10.47031 | -36.95695 | 2026-02-06 03:32:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| e1f78efe-3d0b-3709-af82-c34d7f55d9ab | -10.47405 | -36.95762 | 2026-02-06 03:32:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 6ca09930-4ed2-3228-9aab-acefbb8454e6 | -10.20571 | -36.36747 | 2026-02-06 03:32:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fcee445a-1b5d-39cb-8f64-88e5e150d6d0 | -9.07113 | -35.56535 | 2026-02-06 03:32:00 | NOAA-20 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e14350fa-f804-37dc-9203-bb1e2acce1e2 | -10.20499 | -36.37174 | 2026-02-06 03:32:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6df811ca-0420-33c2-a314-e8e2ff6c5527 | -10.08968 | -36.09378 | 2026-02-06 03:32:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 7ccff3dd-9a08-3b42-8441-fe37658ab3cc | -9.40077 | -35.54411 | 2026-02-06 03:32:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae4ae1b2-9d00-33b4-8409-16270a3e5f59 | -11.10856 | -38.55008 | 2026-02-06 03:32:00 | NOAA-20 | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3c34e49-5027-3425-a08b-a99511574306 | -11.7541 | -40.68553 | 2026-02-06 03:32:00 | NOAA-20 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4cbaad1b-0f4c-315b-8050-ae84899fefad | -10.03635 | -36.21394 | 2026-02-06 03:32:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ee7cb552-8611-34a8-a9a5-e7aee9d4b092 | -10.03996 | -36.21457 | 2026-02-06 03:32:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1b30e8ce-c55a-3005-ae11-7a0e295cecf7 | -24.32191 | -49.72992 | 2026-02-06 03:36:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff0e0ecb-4c32-3811-9e0b-462c7efacf17 | -5.34134 | -45.12136 | 2026-02-06 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3cf1fc2f-742f-3d32-8208-8a62535c3ca4 | -5.10385 | -39.46251 | 2026-02-06 04:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52a65999-8197-3a27-9f0c-762b021ea7a3 | -5.3441 | -45.12534 | 2026-02-06 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cd652df-0a95-3d50-a250-423d6dd70c27 | -3.85824 | -50.19048 | 2026-02-06 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01ed80cd-64f0-3017-a53d-6f2eb157780f | -5.33804 | -45.12085 | 2026-02-06 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77c6603a-dd47-397a-905e-b79bdcff0772 | -1.96535 | -54.69772 | 2026-02-06 04:21:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 402fbe03-c9c3-38c9-9aaf-38459157d7e3 | -3.14722 | -48.14809 | 2026-02-06 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1ff0080-8c88-311b-ac64-8661cac7bca4 | -5.10333 | -39.46606 | 2026-02-06 04:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1794b763-d502-366f-968b-4eeb8d08e4b7 | -3.02731 | -51.64034 | 2026-02-06 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab53fa5d-fa34-3a64-ae6d-69c2f3659e01 | -1.67067 | -45.80317 | 2026-02-06 04:21:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96bd60b7-52ef-3f80-80c3-3918ea49797b | -3.03211 | -51.64103 | 2026-02-06 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8dc35f5-ee91-3b89-a70c-1d232181a4cc | -5.10789 | -39.4631 | 2026-02-06 04:21:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9e84a54c-aa5e-363b-b622-00fcc36492b0 | -2.98788 | -52.36184 | 2026-02-06 04:21:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb1dace7-4e4f-3f4f-9fe3-44721c5518d7 | -5.90843 | -43.84601 | 2026-02-06 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README2.md)
