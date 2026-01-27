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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25d97269-fe43-3dee-b6ef-9602f9b0ff63 | -27.7558 | -50.791 | 2026-01-27 13:30:00 | GOES-19 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 107.9 |
| c912b296-42cf-3881-a1bb-2fd3b9bd4380 | -20.3291 | -57.8433 | 2026-01-27 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| edca1b94-6364-35c2-8fc9-aeb7b192d832 | -27.77 | -50.38 | 2026-01-27 13:40:00 | GOES-19 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| 5606222e-06ab-329d-bbfc-b6e7c57f6f77 | -20.3291 | -57.8433 | 2026-01-27 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 20eceb94-6dbf-3a07-90b0-9236c3255fd1 | -20.3287 | -57.8643 | 2026-01-27 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 67c667c3-f238-3c2c-80a8-e0b7e47bf038 | -20.3294 | -57.8224 | 2026-01-27 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| b15c69e6-56c0-30e0-8e29-91e98f7930f7 | -19.7041 | -56.8436 | 2026-01-27 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 1604e3da-2f70-3fd9-9345-c94d9b2908aa | -20.3291 | -57.8433 | 2026-01-27 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 027dbb8e-8cbb-3836-8858-71ffd2e9d50b | -20.3092 | -57.8252 | 2026-01-27 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| bad54835-eef3-3c40-b209-5dafde7272d0 | -19.7246 | -56.8198 | 2026-01-27 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.4 |
| 6b46ad87-9c61-3d66-b34a-20eb013456a2 | -27.7558 | -50.791 | 2026-01-27 13:50:00 | GOES-19 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| ce6826b3-24aa-3f98-88f5-617ed59c9ced | -19.7045 | -56.8226 | 2026-01-27 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 153.7 |
| 8c481f72-464b-3675-a4e1-a6bfe0252b36 | -19.7041 | -56.8436 | 2026-01-27 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.7 |
| 2d86d4bd-4860-3116-8a1b-a71b187a47ae | -19.6836 | -56.8674 | 2026-01-27 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| ef61eb86-dd03-3135-8982-e86850d4d411 | -27.7558 | -50.791 | 2026-01-27 14:00:00 | GOES-19 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 128.1 |
| e42302b0-efc5-3944-a7dc-7c60b9e6977a | -19.6364 | -57.2499 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 3c356cec-5050-3c5d-987a-31897a05cbaa | -19.6554 | -57.3099 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| e7bf0824-8ea5-3e80-aaad-53b4a847d8c7 | -19.6643 | -56.8283 | 2026-01-27 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 18c99b90-1a6f-3b4b-b6a7-df0b7a86cd54 | -20.3088 | -57.8461 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 6a859a98-47b9-3bf0-a2fe-238197789920 | -19.6639 | -56.8492 | 2026-01-27 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 74217ccf-1fc2-3998-b8cf-d80d3566fd47 | -19.6357 | -57.2917 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 4f6034fb-311f-3a8f-8c14-593b854e96b0 | -19.636 | -57.2708 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| ea43c350-17a4-30e0-8c90-272e706a98b3 | -19.6557 | -57.289 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.7 |
| a1483926-fcb1-3b5a-a5db-fb87ef159abb | -19.7045 | -56.8226 | 2026-01-27 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.3 |
| df778ad7-671a-3318-91aa-ba1686b8d2df | -19.6569 | -57.2263 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 82c146d9-b3ec-3dfd-9f03-902c8f01b269 | -19.6774 | -57.2026 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 0367d588-ecdb-3b18-a48a-1d5ac605039d | -19.7246 | -56.8198 | 2026-01-27 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 493127a8-1b03-35d4-b39f-6a8ba5091af5 | -20.3092 | -57.8252 | 2026-01-27 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| c269d7af-9be3-3e2e-9bb4-15c0c36d51f5 | -19.6774 | -57.2026 | 2026-01-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 0dd6ad9d-64b5-3f4e-b0a8-d8cb27250332 | -20.3092 | -57.8252 | 2026-01-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 417312eb-65b3-3417-bbf7-b29f841ccedc | -20.3088 | -57.8461 | 2026-01-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| f608c665-8731-377e-84be-2ac62bc8c035 | -19.6573 | -57.2053 | 2026-01-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.2 |
| b320cc33-9549-34bc-92c9-46ff99383b75 | -27.7558 | -50.791 | 2026-01-27 14:10:00 | GOES-19 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 98.4 |
| 578ca020-f48f-3a7b-8267-00f0d55eb73b | -19.6569 | -57.2263 | 2026-01-27 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 90cdb774-928b-3d8d-8baa-b00872129d72 | -20.3291 | -57.8433 | 2026-01-27 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 61a64b50-e9d0-3417-aa22-b1fee26ea6fc | -19.6639 | -56.8492 | 2026-01-27 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| f74302ed-92bf-306f-a854-740aa426325f | -19.7041 | -56.8436 | 2026-01-27 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| c8bf6b2f-6337-3c8c-b5be-f56f39f0cfef | -19.7045 | -56.8226 | 2026-01-27 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| e265d7cd-d62d-3418-a7e4-44f829c7fbe2 | -19.6844 | -56.8254 | 2026-01-27 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| e3666c7e-37ac-3488-a7b1-158da67496e7 | -20.3897 | -57.8351 | 2026-01-27 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 11c6f459-c81f-3071-93a2-8bff120643fa | -27.7558 | -50.791 | 2026-01-27 14:30:00 | GOES-19 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 138.4 |
| 7a0bc916-739d-3200-821a-4aed2a3a124a | -19.7246 | -56.8198 | 2026-01-27 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.6 |


