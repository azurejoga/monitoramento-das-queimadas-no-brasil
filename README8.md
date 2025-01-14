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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed5a458c-51ab-39db-a008-f27fc072bd86 | 1.3221 | -60.0272 | 2025-01-14 08:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 449a0a31-146f-3d24-ba3e-7011bfaebe2c | 1.3403 | -60.0461 | 2025-01-14 08:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| d2557460-5ad7-3f38-a220-8fbde03ecdd4 | 1.3221 | -60.0463 | 2025-01-14 08:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| bc53bc16-4cf4-3b91-8daa-7f6839fde869 | 1.3221 | -60.0272 | 2025-01-14 08:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9f2d89f4-224b-3a64-b33d-03a31a57e013 | 1.3221 | -60.0463 | 2025-01-14 08:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a940d001-b954-3d58-8e1a-32553dea352d | 1.3221 | -60.0463 | 2025-01-14 09:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 74746a8a-1444-3e8b-a547-73f1c8cfbdd9 | 1.3221 | -60.0272 | 2025-01-14 09:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a8b9ddab-1ede-3ffc-96d3-0468ca861bb3 | 1.3403 | -60.0461 | 2025-01-14 09:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| a15a6f8d-2c96-3e25-ab43-dfe0a1941bba | 1.3221 | -60.0272 | 2025-01-14 09:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 9f91ebcf-f764-3ce4-8927-94ec95f23988 | 1.3221 | -60.0463 | 2025-01-14 09:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2fe2cffb-46cb-30c1-958e-eb312e3b3f90 | 1.3403 | -60.0271 | 2025-01-14 09:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 42152942-e9da-3943-ac5f-e9735c25e48f | 1.3038 | -60.0464 | 2025-01-14 09:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 06d6dcb3-d520-30d3-98c4-1b27a15d539b | 1.3221 | -60.0272 | 2025-01-14 09:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.2 |
| aebbe86b-2cd1-3be8-a32a-4837374c60f0 | 1.3221 | -60.0463 | 2025-01-14 09:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 6066768b-688d-39da-a21e-d61df789f327 | 1.3039 | -60.0274 | 2025-01-14 09:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1c4795b4-d439-360d-aede-262d4b3263c7 | 1.3221 | -60.0272 | 2025-01-14 09:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 60e5e426-987b-33c7-b643-1f0e398f116e | 1.3221 | -60.0463 | 2025-01-14 09:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 15188d9c-dc17-3ed5-8c27-16c9bfcf55bc | 1.3221 | -60.0272 | 2025-01-14 10:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 591da94e-e187-3def-9e63-7eb19af6def2 | 1.3221 | -60.0272 | 2025-01-14 11:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 36f87a74-2ef1-3131-a601-91d3797a6ea6 | 1.3221 | -60.0463 | 2025-01-14 11:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d066dd00-dfb0-3dbc-8f72-0a054d68c773 | 1.3221 | -60.0272 | 2025-01-14 11:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 476a7e6a-a1b6-324b-a9a5-c4fa52cd87fc | 1.3221 | -60.0463 | 2025-01-14 11:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 54a73816-8679-361b-9f85-1437f47ade94 | 1.3221 | -60.0272 | 2025-01-14 11:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 3b188343-142d-3957-a68f-d3240f397709 | 1.3221 | -60.0272 | 2025-01-14 11:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 108.6 |
| a818d99c-2dad-322e-8c86-e960426f8474 | 1.3221 | -60.0463 | 2025-01-14 11:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 94.1 |
| c2472204-8ab2-371b-838c-b7548691b1d3 | 1.3221 | -60.0272 | 2025-01-14 11:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 43669d52-6fb6-3b0d-918f-2559c081ccce | 1.3221 | -60.0463 | 2025-01-14 11:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.1 |
| b0b64e6d-7f3d-3149-bc68-b358c9be11ea | 1.3221 | -60.0463 | 2025-01-14 11:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.8 |
| b7ddd578-4d2f-3b15-ba49-e4caa6d739f1 | -28.7824 | -55.6063 | 2025-01-14 11:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 123.6 |
| 930dc055-b1fb-3068-b453-ad11efb11fc7 | 1.3221 | -60.0272 | 2025-01-14 11:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 8f6a3a0d-ad16-3e66-bad5-1b8817d07026 | 1.3221 | -60.0272 | 2025-01-14 12:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 670605cf-88c5-3485-abc3-7f8da27b2f37 | -28.7824 | -55.6063 | 2025-01-14 12:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 111.7 |
| 125802b6-d169-34d5-841a-a953e8b45b3a | 1.3221 | -60.0463 | 2025-01-14 12:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 537c1f24-4d45-3f60-a863-5782c032b1d7 | 1.3221 | -60.0272 | 2025-01-14 12:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.0 |
| a0604c00-d369-3bb6-95a7-82da11203a36 | 1.3221 | -60.0463 | 2025-01-14 12:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 46246429-a2d7-3b4d-9dbd-51f861948098 | -28.7824 | -55.6063 | 2025-01-14 12:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 102.5 |
| d5089c82-17f3-37b8-90bb-04369c7b4db8 | -28.7817 | -55.6294 | 2025-01-14 12:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 111.6 |
| 00087102-87fc-3869-a4d3-2f95debde5c8 | 1.3221 | -60.0272 | 2025-01-14 12:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 151.1 |
| bd209872-20b2-33da-98d6-43afb7cf4470 | 1.3221 | -60.0463 | 2025-01-14 12:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 7a521e14-fc93-3da5-8d5e-7597fa54b418 | -28.7824 | -55.6063 | 2025-01-14 12:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 150.8 |
| 856a2cd7-ae90-3793-95c2-a366e828c55a | -28.7817 | -55.6294 | 2025-01-14 12:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 123.6 |
| 2ae471a6-23eb-3e3e-8d43-53289dd03f2f | 1.3221 | -60.0463 | 2025-01-14 12:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 8c2864e1-538a-3acf-94e2-ee56b0e5d504 | 1.3221 | -60.0272 | 2025-01-14 12:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.3 |
| ccabd87c-67ef-3348-9540-10927c545d55 | -28.7824 | -55.6063 | 2025-01-14 12:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 160.7 |
| 57ae3c1c-9c68-3aed-a756-792d94186e3f | 1.3221 | -60.0272 | 2025-01-14 12:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 74d2c34d-e450-3efa-bcbc-4f48ce425623 | -28.7824 | -55.6063 | 2025-01-14 12:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 258.3 |
| be578809-73cf-3f5d-956b-470a88c58b65 | -28.7817 | -55.6294 | 2025-01-14 12:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 185.1 |
| 23fb0df9-cdfc-354e-9880-ced3914fcc39 | 1.3221 | -60.0463 | 2025-01-14 12:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 0ef1be78-08d8-3038-b20f-b0f036517050 | -27.20305 | -49.02339 | 2025-01-14 12:44:00 | TERRA_M-T | BOTUVERÁ | SANTA CATARINA | Brasil | 4202701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 645956a7-6fa7-38d2-851a-ab3102a70fad | -27.21976 | -50.55262 | 2025-01-14 12:44:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 6e5587ff-d709-3373-9cc8-6562c2246a65 | -26.95098 | -48.75393 | 2025-01-14 12:44:00 | TERRA_M-T | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 68184179-69a3-3024-b710-2161f11201b3 | -27.21779 | -49.40956 | 2025-01-14 12:44:00 | TERRA_M-T | APIÚNA | SANTA CATARINA | Brasil | 4201257 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 41cf7838-ce05-3106-8460-6d222c9b7cdd | -19.60391 | -48.82182 | 2025-01-14 12:44:00 | TERRA_M-T | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a1881d02-183e-3407-b5e2-2a603fc586f5 | -28.79083 | -55.62193 | 2025-01-14 12:44:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 40.2 |
| 67692100-3ab8-30ad-a29d-0f32ba439e9d | -27.31734 | -50.51011 | 2025-01-14 12:44:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8029803f-b451-38aa-b6ec-9d008856c1d1 | -28.28286 | -49.92048 | 2025-01-14 12:44:00 | TERRA_M-T | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| f9eedfcb-54aa-3c69-bf97-f837734a6770 | -29.59803 | -51.72248 | 2025-01-14 12:44:00 | TERRA_M-T | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| fc9c348f-ddbc-358d-9c58-be9e8eaa51ee | -19.77576 | -47.92657 | 2025-01-14 12:44:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6309a518-cfb5-3ab9-a099-343647889208 | -26.5039 | -49.09524 | 2025-01-14 12:44:00 | TERRA_M-T | JARAGUÁ DO SUL | SANTA CATARINA | Brasil | 4208906 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 1ae1adec-4b3f-3ac6-9cde-f1a7fc4a2bba | -19.73481 | -58.02719 | 2025-01-14 12:44:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.3 |
| 333554e1-0a50-3e8c-8651-077b5df696a5 | -28.78117 | -55.61984 | 2025-01-14 12:44:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 27.9 |
| 70e8896e-fe24-3582-a2a5-6b5a349708ec | -27.21835 | -50.56317 | 2025-01-14 12:44:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 015a6e61-6bd1-33f5-ad11-5e25249679f1 | -23.95213 | -48.71981 | 2025-01-14 12:44:00 | TERRA_M-T | TAQUARIVAÍ | SÃO PAULO | Brasil | 3553856 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| e7adbf55-bf52-3ef5-8e32-ec316320c373 | -27.2016 | -49.03535 | 2025-01-14 12:44:00 | TERRA_M-T | BOTUVERÁ | SANTA CATARINA | Brasil | 4202701 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b83be03f-7568-32ee-a7b8-81537dc5fe08 | -26.70337 | -50.29227 | 2025-01-14 12:44:00 | TERRA_M-T | MONTE CASTELO | SANTA CATARINA | Brasil | 4211108 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f66d6bbc-ad21-33d7-bdc5-44208da19cd6 | -26.37726 | -48.70905 | 2025-01-14 12:44:00 | TERRA_M-T | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c6e38648-8dcc-3982-bb4f-5b7af171cffb | -29.73997 | -53.86569 | 2025-01-14 12:46:00 | TERRA_M-T | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 11.2 |
| 66b6fb8e-5a0e-3f78-8450-c53b7613ca83 | -30.75381 | -53.25288 | 2025-01-14 12:46:00 | TERRA_M-T | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 6.1 |
| be5905fc-cde2-3c18-b3dd-28c6b2968127 | -31.05456 | -52.82431 | 2025-01-14 12:46:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 9.5 |
| c5091f02-4d1f-3fff-81e0-77e5d4b8492b | -30.7121 | -51.77641 | 2025-01-14 12:46:00 | TERRA_M-T | CAMAQUÃ | RIO GRANDE DO SUL | Brasil | 4303509 | 43 | 33 | nan | nan | nan | Pampa | 5.3 |
| ffdc32bb-47f8-31d4-87c4-e3a1581045e4 | -31.05308 | -52.83467 | 2025-01-14 12:46:00 | TERRA_M-T | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| 4905e8d5-1479-346a-ac7f-3ef507bc927d | -30.66944 | -52.68517 | 2025-01-14 12:46:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 8.6 |
| 42aeee1d-e4f4-3228-8051-93b237d436ae | 1.3221 | -60.0272 | 2025-01-14 12:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 7f92925f-024c-3427-89ba-2c23a4d5c408 | -28.7817 | -55.6294 | 2025-01-14 12:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 289.9 |
| 766cd376-839c-304d-8131-bccd4e818443 | 1.3221 | -60.0463 | 2025-01-14 12:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 2ceda554-011a-322e-b4a8-37d8240875c5 | -28.7824 | -55.6063 | 2025-01-14 12:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 358.0 |
| f4ddfadf-c154-3b9c-82f6-fde9bf729ae5 | -28.7824 | -55.6063 | 2025-01-14 13:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 258.4 |
| 7633704a-8db1-32c4-8214-14831a1651aa | 1.3221 | -60.0463 | 2025-01-14 13:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 128.3 |
| bb8f0d0a-5d47-342b-82df-d98aff404979 | -28.7817 | -55.6294 | 2025-01-14 13:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 194.4 |
| 0353a4c0-3a40-394c-a024-01a95420d80d | 1.3221 | -60.0272 | 2025-01-14 13:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 5b9af634-2613-3840-a88a-86e4630b4db2 | -28.7599 | -55.6114 | 2025-01-14 13:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 114.2 |
| ddd784fe-5511-3be1-b574-3b672cca5fc6 | 1.3221 | -60.0463 | 2025-01-14 13:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 7ec34a5d-12e7-3d06-ad3b-625bb4a9495a | -28.7824 | -55.6063 | 2025-01-14 13:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 221.2 |
| a013ffab-3174-3ee5-a4fb-7c41a7b90815 | -28.7817 | -55.6294 | 2025-01-14 13:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 188.4 |
| b4f3c318-b43a-3ae8-b6e9-da70e7880423 | 1.3221 | -60.0272 | 2025-01-14 13:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 711a6036-81b1-3a2b-a024-5f820ee47cc1 | 1.3221 | -60.0463 | 2025-01-14 13:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 4148a5f0-f3b3-3750-939e-7442258dd43c | 1.3221 | -60.0272 | 2025-01-14 13:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 173.3 |
| ce42bf48-5198-3efb-beb1-ea2a75e0d733 | 1.3221 | -60.0463 | 2025-01-14 13:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d9dca9b9-6f51-35df-93e9-2f48bb515926 | -19.7029 | -58.0102 | 2025-01-14 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 600289e1-4bd7-3c67-a8f7-a69307fd0806 | -19.7033 | -57.9894 | 2025-01-14 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.7 |
| 40fd7cf8-f1f8-3690-8f89-03d638d442c9 | -19.723 | -58.0075 | 2025-01-14 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| f7559952-c8eb-34a4-9674-b2eada0d5f0b | -19.7033 | -57.9894 | 2025-01-14 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 9193815e-e83c-3680-8cc7-7546beb0745c | -19.6836 | -57.9712 | 2025-01-14 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.3 |
| 633f0748-56af-3808-8d08-30f899e31e7f | -19.7234 | -57.9868 | 2025-01-14 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 1b2a6878-a907-3343-a310-0741681161ef | -19.6832 | -57.992 | 2025-01-14 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 9229a0bf-c092-3fcb-9543-8817d98b030d | 1.3221 | -60.0272 | 2025-01-14 14:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 2c5461a9-2471-3b90-b6ed-dc4af1cefb4c | -19.7037 | -57.9686 | 2025-01-14 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.6 |
| 35446d7e-eadd-3ec6-a937-d6bcc47d9c6a | 1.3221 | -60.0463 | 2025-01-14 14:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 69e0d13c-f53e-358c-a23d-e5f6561af479 | 2.9463 | -60.179 | 2025-01-14 14:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.0 |


