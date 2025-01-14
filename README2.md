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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f4723de-e890-3de9-827e-750359f71e71 | -28.7817 | -55.6294 | 2025-01-14 02:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 151.8 |
| c411d815-a2e5-3a1a-9d21-d70626105dbf | 1.3221 | -60.0463 | 2025-01-14 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 66739197-14b1-3880-8822-fa07ede5e684 | 2.9463 | -60.179 | 2025-01-14 02:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 852d814b-b84a-361a-a25c-d36230199a92 | 1.3221 | -60.0272 | 2025-01-14 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.9 |
| c4950a1d-74b4-3aaa-915c-c8d13bcb54f3 | 2.9463 | -60.179 | 2025-01-14 02:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d81724ca-7610-3607-a04d-500035244948 | -28.7824 | -55.6063 | 2025-01-14 02:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 84.8 |
| f3d1f833-06cb-35dd-9bec-ae75ee878bac | -28.7817 | -55.6294 | 2025-01-14 02:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 127.2 |
| c41fad21-2220-3a50-bfe0-2e37f29b7c78 | 1.3221 | -60.0463 | 2025-01-14 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 039ec8b0-7585-3d4e-9755-35996c722e42 | -16.1115 | -58.1868 | 2025-01-14 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| e8ef6cd1-1bb4-325c-8935-8cac635c14e6 | 1.3217 | -60.4262 | 2025-01-14 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| df58b746-be5c-3f36-8766-599c04337b78 | 1.3403 | -60.0271 | 2025-01-14 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.4 |
| fe3be928-77e9-33e5-930a-b69cbadffb93 | -28.7817 | -55.6294 | 2025-01-14 02:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 75.1 |
| 4307fec3-36ac-370c-83b6-71bc897102aa | 2.9463 | -60.179 | 2025-01-14 02:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 226c1d71-3b0a-3732-84cb-176b9412617c | 1.3221 | -60.0272 | 2025-01-14 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 56ea6eae-0929-3c90-8f38-8e1d19bbbbc7 | 1.3403 | -60.0461 | 2025-01-14 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 3fae53e9-d812-386d-a057-897db46c432e | 1.3221 | -60.0463 | 2025-01-14 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 133.9 |
| 18cffd50-f672-32e1-8d3f-ad0b620ae1b3 | 1.3403 | -60.0271 | 2025-01-14 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 5593bc1d-b0d8-382e-9306-3c270e5792d7 | 1.3221 | -60.0272 | 2025-01-14 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 196.8 |
| e56193b1-545a-3902-83ca-04dcd0ff02a5 | 1.3221 | -60.0463 | 2025-01-14 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 232.0 |
| 5614f912-e4f3-3025-a1bd-c9e3647bf5ae | -16.1115 | -58.1868 | 2025-01-14 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 3f537403-6e86-3984-bede-c8c07efd8a55 | -28.7824 | -55.6063 | 2025-01-14 02:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 85.7 |
| 8f1aed98-c374-3430-86f6-c8ffa83b7457 | 2.9463 | -60.179 | 2025-01-14 02:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 329dbac6-033d-3e0f-b55f-e428f605be2f | 1.3403 | -60.0461 | 2025-01-14 02:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9be44064-3381-339b-8a73-6ad6bf9aa24e | -16.1118 | -58.1666 | 2025-01-14 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 21f91707-da29-3296-9f77-31d6584ce6fa | -28.7817 | -55.6294 | 2025-01-14 02:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 132.0 |
| 1725adaf-3b3d-3bde-8387-8ba17ee4b8e6 | 2.9463 | -60.179 | 2025-01-14 03:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| de2b977c-894b-3b9c-b454-df619aec80cb | 1.3039 | -60.0274 | 2025-01-14 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 633ca7de-9949-32ae-9672-999c16cd05c4 | 1.3221 | -60.0463 | 2025-01-14 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 48b83a43-00cd-3496-8dc6-1bc4cd767d43 | 1.3403 | -60.0271 | 2025-01-14 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 4ef91aa7-d24b-3db9-bc81-d122288f5d5e | 1.3038 | -60.0464 | 2025-01-14 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6dedc385-4c43-35f4-ab0e-f51955ad0988 | 1.3403 | -60.0461 | 2025-01-14 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 8ff6214d-1ec8-3614-af16-517ed653caf5 | 1.3221 | -60.0272 | 2025-01-14 03:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 185.4 |
| 5340f417-8a72-3d31-a411-ffe32db20520 | -28.7817 | -55.6294 | 2025-01-14 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 155.8 |
| 5d1beaeb-c521-356b-bdce-33d2f59554e6 | -28.7824 | -55.6063 | 2025-01-14 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 76.2 |
| 59b2d66f-a7a4-3218-b967-f632cc15c94c | -28.7592 | -55.6345 | 2025-01-14 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 105.5 |
| d1eccf85-d737-3bad-a496-e96ac84a7446 | -6.53724 | -35.27507 | 2025-01-14 03:02:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0818182a-3802-3c80-a4ad-3347279775cb | -6.54271 | -35.27599 | 2025-01-14 03:02:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c100dffb-b91f-3c1e-9541-abef65da4a4f | -6.53789 | -35.27137 | 2025-01-14 03:02:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4de33f6-d29d-3f27-8dae-9dc7c7da9a05 | -28.7817 | -55.6294 | 2025-01-14 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 173.8 |
| 6c4d3612-bc1c-3b0d-8b05-9ccea04601f8 | -28.7824 | -55.6063 | 2025-01-14 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 72.8 |
| b2567874-e4e6-3fa1-a772-9c141454dd72 | 1.3403 | -60.0461 | 2025-01-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 0f24d280-b1fd-328c-9ea7-542924a70913 | -28.7592 | -55.6345 | 2025-01-14 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 96.3 |
| f03e4603-fc25-3377-80fb-ae4db9cb5ff6 | 1.3221 | -60.0272 | 2025-01-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 165.9 |
| 7497cce8-7221-3f21-bba2-a8ea797f862e | 1.3221 | -60.0463 | 2025-01-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 219.7 |
| b25bb33a-fee4-3451-84e3-b8fa48df8a23 | 1.3403 | -60.0271 | 2025-01-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a7854010-17ea-3d2e-b4db-ac5b40a50ba5 | 1.3038 | -60.0464 | 2025-01-14 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 71f792eb-927a-34b0-9f35-8551bddd63b6 | -28.7824 | -55.6063 | 2025-01-14 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 101.3 |
| 36da1332-e10b-31a5-ae62-dc948f40520b | 1.3038 | -60.0464 | 2025-01-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d725e389-3ad7-30ca-b0da-d0402715560c | 1.3403 | -60.0461 | 2025-01-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.9 |
| e4925c57-f3df-3131-bf9a-10ab7f277399 | -28.781 | -55.6525 | 2025-01-14 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 100.2 |
| a2bf6b2e-ac1c-3441-8294-66002ac02a52 | 1.3403 | -60.0271 | 2025-01-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 802a29eb-5c75-3c82-9fc5-aa3624de14cf | -28.7817 | -55.6294 | 2025-01-14 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 229.4 |
| ae16f27f-83bc-31b5-9bf5-ac860b681531 | 1.3221 | -60.0463 | 2025-01-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 7b4c96fe-f4a4-3188-90dc-d186cbe54ea5 | 1.3039 | -60.0274 | 2025-01-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f200aa70-617e-3858-9421-5ae6acf5e649 | 1.3221 | -60.0272 | 2025-01-14 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 568d6310-6221-379e-b4ed-accb3c9f9018 | 1.3403 | -60.0271 | 2025-01-14 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e5264bee-49b9-340a-b50e-94cefb10bbf5 | -28.7824 | -55.6063 | 2025-01-14 03:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 77.6 |
| 62256cb6-aa2d-3666-bab8-3bde754440d9 | 1.3403 | -60.0461 | 2025-01-14 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| edbe51ea-44a3-38ad-b96f-ac1905621b2d | 1.3221 | -60.0272 | 2025-01-14 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 021651af-3b12-373c-ae5e-552949f0f13e | -28.7817 | -55.6294 | 2025-01-14 03:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 113.7 |
| 93b9ef1f-927a-3a82-86eb-931fa42ac1e7 | 1.3221 | -60.0463 | 2025-01-14 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 199.0 |
| b3df5224-9455-30ca-b181-0b5e97fbaeb8 | 2.9463 | -60.179 | 2025-01-14 03:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 20089f81-d8d2-38a4-8bf0-b0b707bf25ec | -16.1118 | -58.1666 | 2025-01-14 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 14c0b104-7679-3755-93dc-0077b47111de | -28.7824 | -55.6063 | 2025-01-14 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 75.3 |
| a31940bf-5a68-3ddc-a33a-528d096dee6b | 1.3221 | -60.0463 | 2025-01-14 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 195.8 |
| b03a582d-e36c-3495-8594-447eb111a5fb | 2.9463 | -60.179 | 2025-01-14 03:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0fc4ffef-4e34-324d-917a-61b14a2a9a50 | 1.3221 | -60.0272 | 2025-01-14 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 176.7 |
| bfc2d657-8452-38f1-a076-8611262324c8 | -28.7817 | -55.6294 | 2025-01-14 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 98.5 |
| ea5b0e28-0b97-3aa3-ad4d-69c3f3d6a2ff | 1.3403 | -60.0461 | 2025-01-14 03:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 693d1eb0-8f92-3dc7-9550-b92973250a06 | -28.7817 | -55.6294 | 2025-01-14 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 93.5 |
| ce3cc60a-7e95-3bd8-97eb-ae34314cd58d | 1.3221 | -60.0463 | 2025-01-14 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 569cb303-8d42-3f5b-a771-992a89d09578 | 1.3403 | -60.0271 | 2025-01-14 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 0f43a5d0-2c08-38d2-aee5-344ab2d7f533 | 1.3403 | -60.0461 | 2025-01-14 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| da417b5b-ce51-33c7-baf9-7efcffb6f8c7 | -28.7824 | -55.6063 | 2025-01-14 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 82.1 |
| 09924ff0-6801-3b69-be7b-b5af26774074 | 1.3221 | -60.0272 | 2025-01-14 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.5 |
| b2b1cb42-9f60-34ba-be51-cf4d1cfcb3a4 | -6.54296 | -35.27437 | 2025-01-14 03:53:00 | NOAA-21 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1636af21-23f8-3495-a8a7-692537f1fffd | -6.54235 | -35.27846 | 2025-01-14 03:53:00 | NOAA-21 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eb076793-14e7-3355-a09c-ca52125c7749 | -10.36559 | -37.06157 | 2025-01-14 03:55:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e6b47af8-0d11-3c4f-9291-0f79e45fbfb4 | -5.74084 | -45.60196 | 2025-01-14 03:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.0 |
| bb583fd7-9288-396e-a731-d14034818fc9 | -10.21492 | -37.45864 | 2025-01-14 03:55:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee22c9c6-617a-36d8-a1d6-2a2db8b5661c | -20.24904 | -45.5473 | 2025-01-14 03:57:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4bc6533a-c7be-308d-8abe-0e5eb8d2f4af | -22.11085 | -49.63352 | 2025-01-14 03:59:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 110feb7d-358c-3ab9-a6fb-58f84542415e | -23.43029 | -46.40709 | 2025-01-14 03:59:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d045a4d-74e2-3beb-af21-ca2db9494731 | -23.40708 | -46.55671 | 2025-01-14 03:59:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0523c41d-d86e-3289-b38b-e78407fc49ff | -23.34054 | -46.77213 | 2025-01-14 03:59:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5f7e9643-1fb4-3af3-a948-9275c7d3e52c | -22.11192 | -49.6283 | 2025-01-14 03:59:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9414dbff-f979-3614-9f75-cdcff5ef08a8 | -22.90857 | -46.53053 | 2025-01-14 03:59:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8615bc41-7f10-3d14-8a07-93be2bd09c17 | -21.45044 | -48.60788 | 2025-01-14 03:59:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9027c604-f291-3f1a-80f8-b7c73be3f684 | -24.82784 | -53.62176 | 2025-01-14 03:59:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 257b50cb-bedb-3606-b1a5-eef3abbb99c8 | -23.98561 | -48.91887 | 2025-01-14 03:59:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 663b15e4-73fd-3539-9d30-b10f834dbf69 | -21.4461 | -48.60698 | 2025-01-14 03:59:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aeb878d7-7c71-3710-8ad9-92db7574d6a6 | -28.7817 | -55.6294 | 2025-01-14 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 68.5 |
| 5cf81457-32d8-3fe4-9f92-a7113654c7b5 | 1.3221 | -60.0463 | 2025-01-14 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 135.4 |
| e215f3e8-acba-3c8c-82ab-00cc03c8166c | 1.3221 | -60.0272 | 2025-01-14 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 51dc24b5-e0f4-332d-bf65-4cf59d4f7694 | 2.9463 | -60.179 | 2025-01-14 04:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 170b80ed-a82a-3e0b-90ba-9eef6c72ba9d | -28.77078 | -55.59838 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 942805a4-0271-3279-a137-1d6dd166e773 | -28.77749 | -55.64396 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.1 |
| 8d803b81-e751-354a-8e5a-4a068b3d5578 | -28.78079 | -55.63072 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.1 |
| b6716c29-a1bb-3144-a464-231aa746ef82 | -28.77745 | -55.61992 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.5 |
| 4aba6abe-5df1-3cc8-ac05-804a9981a45b | -28.7819 | -55.62627 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
