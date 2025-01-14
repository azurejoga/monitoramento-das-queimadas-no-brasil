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
| 82aa474c-325d-3cb8-bfe8-a7e75a9aac51 | -28.7824 | -55.6063 | 2025-01-14 00:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 76.8 |
| ca3b3a5a-2f7b-3624-b5a3-ebd8414af3c2 | 2.9463 | -60.179 | 2025-01-14 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| d94e4e2e-f17f-3ac1-813a-0e4fc0c26d12 | 2.4341 | -60.6424 | 2025-01-14 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 5766d11d-7047-3144-aaea-54514123cdf9 | 2.4341 | -60.6613 | 2025-01-14 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 232ff95c-612f-329f-ac7e-e2fbb02a9e59 | -28.7824 | -55.6063 | 2025-01-14 00:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 75.0 |
| 5b9810c7-296d-32be-900a-dcf90b51557d | 1.3217 | -60.4262 | 2025-01-14 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 14b73332-1c07-3323-ae14-f137e6893b3f | 1.3034 | -60.4263 | 2025-01-14 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 99.4 |
| b871bcfb-0aff-3cbf-a324-ebc68b885020 | 1.3221 | -60.0272 | 2025-01-14 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 35cae7f3-d9f6-3f35-9fae-2c8f058c0537 | -28.7824 | -55.6063 | 2025-01-14 00:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 79.3 |
| bb95e738-309c-3950-94ab-c30c177194fc | 1.3217 | -60.4262 | 2025-01-14 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| aa00e631-6756-346f-ba6b-bee2f2a4b107 | 1.3221 | -60.0272 | 2025-01-14 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7daf340c-f60d-3ea9-bdb3-4c68324bccdf | 2.9463 | -60.179 | 2025-01-14 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| b1e90357-6c6f-3a28-9c9d-4f607e7ccf9f | 2.4341 | -60.6424 | 2025-01-14 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 411b7e22-21ee-3158-b2d3-ef887299fdc5 | -28.7817 | -55.6294 | 2025-01-14 00:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 67.6 |
| 5d34a6ca-2185-32b8-ae44-585ba5bfdce6 | 1.3034 | -60.4263 | 2025-01-14 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d4473229-4a41-3ee0-ad25-963577e5a980 | 1.3217 | -60.4262 | 2025-01-14 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 162adc9b-e715-33ed-99e6-9c333655ec95 | 1.3034 | -60.4263 | 2025-01-14 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 8f8f81d3-ead4-3525-99be-e85d8dfaf2c8 | 1.3221 | -60.0272 | 2025-01-14 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 51b8c96e-696c-361c-8d81-94f54969d387 | 2.4341 | -60.6424 | 2025-01-14 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d586a618-d8d6-3cf8-9324-3b991b4dc7ef | 2.9463 | -60.179 | 2025-01-14 00:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 964ff17e-a149-3ec1-b391-5664c392323c | -28.7824 | -55.6063 | 2025-01-14 01:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 71.7 |
| 64a3e1b6-b0f1-3843-a36d-190e6573463c | 1.3217 | -60.4262 | 2025-01-14 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e74cfa84-9137-3043-8bc3-64c864c3c4fc | 1.3221 | -60.0272 | 2025-01-14 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f9bcb6bc-7a22-3873-8cea-8fbcacc362ba | -28.7824 | -55.6063 | 2025-01-14 01:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 78.4 |
| a34fef9b-2e4c-32ce-8cc4-663e8269081c | -16.1118 | -58.1666 | 2025-01-14 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 12f60a73-21e2-307b-ae2c-16f762544d38 | 1.3034 | -60.4263 | 2025-01-14 01:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e1b85b9a-0fa8-3ef0-b7ab-ccd78d3a1c4f | 2.9463 | -60.179 | 2025-01-14 01:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8fa0e4aa-c150-34b5-a7dd-20ef77bb7de6 | 2.4341 | -60.6424 | 2025-01-14 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b24256a9-e1c4-3bec-946e-414eedffa2f8 | -16.1115 | -58.1868 | 2025-01-14 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 00b23652-b2a5-3d11-8823-cd8bd95c4101 | -28.7817 | -55.6294 | 2025-01-14 01:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 68.4 |
| 37ef57cf-20b2-3021-b405-91e975d01776 | 1.3217 | -60.4262 | 2025-01-14 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 25173b8a-f955-3df6-8a88-3b3f2189892f | -28.7824 | -55.6063 | 2025-01-14 01:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 80.6 |
| af1c88ca-6b89-34df-a3d3-6e6f2b0c2296 | 2.9463 | -60.179 | 2025-01-14 01:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9e433aed-679b-32fb-81c0-6393649f0893 | 1.3034 | -60.4263 | 2025-01-14 01:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1e5a242a-92d6-3536-af04-e1f86196af5e | -16.1115 | -58.1868 | 2025-01-14 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| 38b36a4f-c2c1-3bf2-b22f-fbcd825d83f4 | -16.1118 | -58.1666 | 2025-01-14 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| ea70859b-fef0-304d-8f09-a3f967eb9de4 | -28.7817 | -55.6294 | 2025-01-14 01:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 72.3 |
| 1c91a330-f791-319a-8df2-06173fbfb724 | 2.4341 | -60.6424 | 2025-01-14 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ba0acb3f-46fe-3716-94e1-217d70a6d6e2 | 1.3217 | -60.4262 | 2025-01-14 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 40e3479e-ca5a-3d5b-b181-5bf0181a1129 | 1.3221 | -60.0272 | 2025-01-14 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0b686ca3-12c7-3326-8c53-9c692744b4a2 | 2.9463 | -60.179 | 2025-01-14 01:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 7360c96c-c459-3b60-aed5-a646f59ca249 | -28.7824 | -55.6063 | 2025-01-14 01:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 95.3 |
| 1db3a8b6-2acd-3578-adef-520577214e43 | -28.7817 | -55.6294 | 2025-01-14 01:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 106.6 |
| 2c397519-5b3d-3030-895f-b80d0a0b9059 | 1.3034 | -60.4263 | 2025-01-14 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a4e7d605-5ce8-3367-a8dd-c894fd097539 | 1.3217 | -60.4262 | 2025-01-14 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d19042ce-d6de-3b99-88a8-a47f5fefa87d | -28.7824 | -55.6063 | 2025-01-14 01:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 83.9 |
| 15ea0d57-fbb6-3f0f-9937-3723f48b9772 | 2.9463 | -60.179 | 2025-01-14 01:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e8425120-b939-3dfa-87c2-0f3d35b0ff2f | -28.7817 | -55.6294 | 2025-01-14 01:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 90.5 |
| 4daa0247-6c4a-373f-b5f1-f93e6abb33c8 | 1.3034 | -60.4263 | 2025-01-14 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 498383c9-1321-39cd-bc95-4026aece0dc2 | 2.4341 | -60.6424 | 2025-01-14 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 9f42d8d3-0166-3b5e-bebd-f00ab504b771 | 1.3221 | -60.0272 | 2025-01-14 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 83823502-0e07-3b24-bb7c-08d0e9d7f26c | -28.77827 | -55.62307 | 2025-01-14 01:49:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 68.6 |
| 1a4678fa-d09f-3575-b174-23ba7d1d1713 | -29.73528 | -53.87154 | 2025-01-14 01:49:00 | TERRA_M-M | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 10.2 |
| f2e87acb-b72a-33dc-a603-adc51466f12f | -28.78048 | -55.63619 | 2025-01-14 01:49:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 14.8 |
| 02258d6f-5817-3177-9aae-11b15e7f2b8a | -28.77606 | -55.60996 | 2025-01-14 01:49:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 48.6 |
| 36db5856-cbe4-3c04-959b-d0737550bd3c | -28.76823 | -55.62535 | 2025-01-14 01:49:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 14.1 |
| fb5bc49a-1d49-3840-9547-a5d8d7d63887 | -28.77045 | -55.63847 | 2025-01-14 01:49:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 23.8 |
| fbe7d488-4dba-3dd4-a83c-9b5343ad12bd | -28.7638 | -55.59912 | 2025-01-14 01:49:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 25.0 |
| 87181c73-ca15-38b4-afd7-090c98fd5217 | -28.77384 | -55.59679 | 2025-01-14 01:49:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.7 |
| a78c1d6c-580f-3605-9870-775184694ff6 | -28.7817 | -55.6294 | 2025-01-14 01:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 102.0 |
| 9f249e15-a844-3ef6-b375-5f1ffae671dd | 1.3217 | -60.4262 | 2025-01-14 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 630e27af-7ea5-37e0-b5d4-aa47385e63a7 | 1.3221 | -60.0463 | 2025-01-14 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c7143f29-46ee-3e50-87b3-722233fe60ef | 1.3221 | -60.0272 | 2025-01-14 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 79223cbb-4d38-30cc-a425-a74fd635dd6b | -28.7824 | -55.6063 | 2025-01-14 01:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 83.7 |
| e69f2083-973c-3cc8-b6b4-9225c4882cf6 | 1.3034 | -60.4263 | 2025-01-14 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b0cb85cb-3537-3b5c-9af0-6f0016d16267 | 2.9463 | -60.179 | 2025-01-14 01:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 621ee8f4-0b20-351e-80a0-bd21c4392e7f | 2.94323 | -60.16904 | 2025-01-14 01:58:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| d8d5d34f-5fc2-324d-85e3-69507b0bfabe | 1.3073 | -60.42782 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 61b6169e-39d7-3816-8f57-4d5e221a694e | 2.4304 | -60.66411 | 2025-01-14 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b819892a-c00f-3902-a8d8-36a9f2bac377 | 1.3194 | -60.42943 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ed2da534-8efb-319e-b13a-b307cf914a15 | 1.31417 | -60.41773 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 784cd90a-d11c-3c77-a463-ef70f8080f95 | 1.32332 | -60.04683 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e9b017c1-a3ca-35ec-ab96-e693c82bda75 | 1.32589 | -60.02833 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8f4ac759-5491-3b36-bb86-f93809f46a3c | 2.19214 | -61.81087 | 2025-01-14 01:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2bd32b4c-b400-318a-8734-2e281938e5b7 | 2.43276 | -60.64686 | 2025-01-14 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b4a9df6a-542a-3a13-bfdd-5803326d802e | 1.31184 | -60.43498 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 75982da3-b35e-3493-82a6-8684a11f8d5c | 1.32187 | -60.41219 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c91f1819-0c1e-35e7-a68f-5ef6f29abb1c | 1.1819 | -60.492 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| f9cd0306-7ad6-3d19-9898-bd04cdd366e7 | 1.17952 | -60.50896 | 2025-01-14 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 11260348-1023-3db9-9d87-fd169a3d0ba6 | 2.94063 | -60.18836 | 2025-01-14 01:58:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 54100bb2-3c78-3f89-a5db-e9aca69db231 | 2.95333 | -60.18996 | 2025-01-14 01:58:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 75c8b9e0-23f5-3045-a713-fb503cb9b27c | -28.7817 | -55.6294 | 2025-01-14 02:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 79.5 |
| b15a49f6-fad8-3129-bd3c-7dfbe771f490 | 2.9463 | -60.179 | 2025-01-14 02:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7a442ce1-d33a-3975-bc86-0550d97e29d7 | 1.3221 | -60.0463 | 2025-01-14 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ac21d51b-e247-38b4-8743-23819e133884 | 1.3217 | -60.4262 | 2025-01-14 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 32c94a30-8809-354b-b183-5f3d764afe48 | 1.3034 | -60.4263 | 2025-01-14 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bc665214-8902-34c2-93c6-588d97484c4d | -28.7824 | -55.6063 | 2025-01-14 02:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 74.5 |
| 6b743e34-0410-383d-bcbc-15fe6f007418 | -16.1118 | -58.1666 | 2025-01-14 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 33c7d2ac-7f86-37a1-a5f7-450b2a94060a | 1.3221 | -60.0272 | 2025-01-14 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 289a9961-b943-35a2-b0ff-acbae5c55ecb | -16.1115 | -58.1868 | 2025-01-14 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 69a95f19-4f5f-3267-ad51-6cbab769038b | 2.9463 | -60.179 | 2025-01-14 02:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e560c1f5-5710-3b31-945a-cae3e05916e7 | 1.3221 | -60.0272 | 2025-01-14 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 2b07b8b5-90a4-342e-becd-6192fb2e9d2e | 1.3221 | -60.0463 | 2025-01-14 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 61e478a5-62c5-3aad-9fd0-d9beb1ae0a89 | -16.1118 | -58.1666 | 2025-01-14 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 4b663e31-3ce7-3c91-a486-dbe01c2e9f8c | 1.3034 | -60.4263 | 2025-01-14 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0d2111d3-c12d-3316-994e-9077569c12c6 | -28.7817 | -55.6294 | 2025-01-14 02:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 85.9 |
| 9a44c738-73f8-3745-9c20-4e5e319ca780 | -28.7824 | -55.6063 | 2025-01-14 02:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 74.5 |
| 88ef6dc1-2982-3872-b9c3-be8056671403 | 1.3034 | -60.4263 | 2025-01-14 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f709c78b-8cdc-3953-9ad1-b651a41816bf | 1.3221 | -60.0272 | 2025-01-14 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 11d57505-c71f-334f-9d6b-61c593866c8d | -28.7824 | -55.6063 | 2025-01-14 02:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 88.0 |


[Clique aqui para ver as próximas entradas](README2.md)
