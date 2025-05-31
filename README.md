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
| a92f33c8-49e7-3b79-9e2e-cf59ea024c3b | -10.6489 | -49.4483 | 2025-05-31 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6857a7e2-8fc6-32d1-96b8-213ae8bc2c9e | -7.2405 | -43.0899 | 2025-05-31 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 5787de70-d349-30d5-baba-9e28a844343a | -11.8558 | -51.262 | 2025-05-31 00:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 260edbeb-9b87-336d-9bf4-d3d4b7f19c26 | -13.1068 | -45.276 | 2025-05-31 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7aab91e6-d468-33b8-9b1a-7d941a88744b | -11.8365 | -51.2854 | 2025-05-31 00:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 64a64648-6380-3b16-bfb1-1a6a4246069c | -12.0345 | -49.5248 | 2025-05-31 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 369c89df-985d-39cd-a44e-aa8d95578261 | -11.8368 | -51.2641 | 2025-05-31 00:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 142.2 |
| b769f192-1ce8-3dfc-8750-eb89fd67f19f | -12.0154 | -49.5272 | 2025-05-31 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 223.3 |
| 4694330b-4341-3cbd-bff5-9919c8b58dcf | -7.2403 | -43.1134 | 2025-05-31 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 44b17fa4-0936-3e6f-a82a-25d761dcb24e | -12.0157 | -49.5054 | 2025-05-31 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9c15d49a-b334-3c51-a636-a5096c8993d2 | -10.462 | -47.9428 | 2025-05-31 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a0219568-9b74-364a-bab2-3c8b4d207a91 | -10.6492 | -49.4267 | 2025-05-31 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| cdefaac4-9439-35bb-a941-c12b1dfd8360 | -11.8177 | -51.2662 | 2025-05-31 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 19b399ca-248e-31f8-9a80-fb21ccc1c0c5 | -7.2403 | -43.1134 | 2025-05-31 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| d3a0d8c3-4419-332f-84a6-993e9df36d6e | -12.0348 | -49.5031 | 2025-05-31 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 132f067b-0dd4-359b-9377-e9d712859da1 | -7.2405 | -43.0899 | 2025-05-31 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 3083f185-41eb-3631-bbaa-5c725dd51345 | -11.8368 | -51.2641 | 2025-05-31 00:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 4ccd2939-3b70-3ffa-840b-6f4016907563 | -7.2594 | -43.0881 | 2025-05-31 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 32609bbb-5d18-3808-a164-ea945350d6f5 | -10.462 | -47.9428 | 2025-05-31 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| be702e03-44e0-337b-a404-5e64bd97f180 | -12.0345 | -49.5248 | 2025-05-31 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 0b9a0023-4fef-35b6-b4d7-9794f4b9e8b2 | -10.6492 | -49.4267 | 2025-05-31 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 3c40b4f3-c341-3a39-9cd2-bdfb3049cd47 | -11.8365 | -51.2854 | 2025-05-31 00:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 29dbcb10-81a7-33da-bc03-be140c71ce68 | -12.0157 | -49.5054 | 2025-05-31 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| ae127396-e950-3da1-b424-492ff1f8ef9d | -12.0154 | -49.5272 | 2025-05-31 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 0952ee49-fe36-35a9-b347-0c3a297b0a35 | -12.0345 | -49.5248 | 2025-05-31 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| b4213aaf-f94b-3818-a303-5d5854bfa151 | -10.462 | -47.9428 | 2025-05-31 00:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b5270d9f-ca38-33c3-9874-b9585a518748 | -12.0157 | -49.5054 | 2025-05-31 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c91f5b8d-761e-301a-8de2-4756fcae04ef | -11.8558 | -51.262 | 2025-05-31 00:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e4bcf1d7-f3be-3208-b67b-aae7a7b7c0eb | -12.0154 | -49.5272 | 2025-05-31 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 6af93c4b-13ba-3878-9df2-71792a044d76 | -11.8365 | -51.2854 | 2025-05-31 00:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 93b1b95c-80e7-3e00-bc7d-0b42fe7bd3e3 | -10.6489 | -49.4483 | 2025-05-31 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 97e75971-5270-34e1-a198-a0e0a9f2c4af | -7.2211 | -43.1388 | 2025-05-31 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 7a1e82a2-79c2-3c2f-a4e7-1c432b764f22 | -11.8368 | -51.2641 | 2025-05-31 00:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 377d8f0c-3515-334a-a357-ea4f41b82d36 | -10.6492 | -49.4267 | 2025-05-31 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 66fcdf53-74c0-3945-a918-9461132f976f | -10.462 | -47.9428 | 2025-05-31 00:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| bd9a1d20-3d1e-39f5-8f85-6e800fac7121 | -12.0154 | -49.5272 | 2025-05-31 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 24a80c91-d8a6-33ca-9760-f78edaa598f1 | -12.0157 | -49.5054 | 2025-05-31 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a4c4fdef-6bf3-300a-968e-5672098c78f6 | -11.8365 | -51.2854 | 2025-05-31 00:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9bbfa0ed-bcfb-313b-b441-6d57c7f708c6 | -7.2403 | -43.1134 | 2025-05-31 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 1d2a9b25-2f08-3951-b423-62ea85cfacd7 | -11.8368 | -51.2641 | 2025-05-31 00:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| a35b1b0e-d23a-3a1c-900c-4f93c20eedf7 | -11.8177 | -51.2662 | 2025-05-31 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b0133cb3-36a9-3606-bd13-1fd4c356d70f | -12.0345 | -49.5248 | 2025-05-31 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8d7b19e1-6710-32c1-ba94-7f669d7d7020 | -7.2405 | -43.0899 | 2025-05-31 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 02eb91a8-9ac4-359c-8f3b-668eb527b413 | -10.6489 | -49.4483 | 2025-05-31 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1ba89b1f-967a-34aa-9e8f-1bcb4ec2bdc8 | -10.6492 | -49.4267 | 2025-05-31 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| ab5c5656-84e5-3fe0-9ebc-52227330efca | -23.43184 | -46.7588 | 2025-05-31 00:35:00 | TERRA_M-M | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 3b28c74d-c703-3f78-b1a5-33e5ecadf392 | -20.61282 | -48.86599 | 2025-05-31 00:35:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 57ebca79-8c5c-3f3a-b599-cd44fa491e82 | -18.38267 | -44.51525 | 2025-05-31 00:35:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3cd9c71e-c417-305c-9392-e98b0126a6d2 | -10.95568 | -48.36945 | 2025-05-31 00:37:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2ead35b9-1513-3779-b710-5fa2cf67e8f8 | -14.0722 | -47.65482 | 2025-05-31 00:37:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| cfe4b19f-2cc7-3018-ad7f-efbeb7b4e275 | -9.04884 | -47.02568 | 2025-05-31 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 85f8e48a-76a5-3304-bf9c-a38a12c541df | -11.1402 | -53.95082 | 2025-05-31 00:37:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8f39fa99-5dbe-389a-8cee-2bc22dcd8c2c | -9.50365 | -40.31443 | 2025-05-31 00:37:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 4b4db788-5a7a-382c-a4e5-10b41963ccc8 | -12.01977 | -49.51384 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 5eabdb1e-c434-3ff1-a470-cbe9fce63b2c | -12.03083 | -49.52332 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 143d2ba1-089f-30a5-8380-c45623f0f6ff | -11.44813 | -49.10118 | 2025-05-31 00:37:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fda6dd04-a609-30ef-a8e4-7fb12b7f9239 | -12.0294 | -49.51253 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b85b30c1-967c-338e-8dad-b7f744083779 | -12.19 | -54.24915 | 2025-05-31 00:37:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| fc1b71af-fe74-3cb5-ac77-41c5f667c22e | -12.03496 | -49.52739 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1e197e55-cb27-30a8-9e55-ec3d79bc7af2 | -10.65534 | -49.44185 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ef2451f4-0dc9-32b6-bc43-149a5cb88425 | -12.02119 | -49.52459 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 3f36e9ac-d98a-3732-aad9-00d20a2f53f4 | -10.73572 | -49.27892 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ffed45ec-5668-3b3f-ab06-2b6f7b2c2085 | -9.12911 | -49.6506 | 2025-05-31 00:37:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8de519dc-82e0-3c63-92df-cdcd1da5caec | -9.25514 | -48.8666 | 2025-05-31 00:37:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6beccbdf-992c-3c05-8bf4-46da4660a417 | -9.39789 | -48.42804 | 2025-05-31 00:37:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6b8189a1-341f-317d-9ac9-54383edabbe3 | -13.09702 | -45.27552 | 2025-05-31 00:37:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| f0aa5071-8336-35f6-92f8-8c5d10f98a39 | -9.39664 | -48.41888 | 2025-05-31 00:37:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b84a6469-48a4-32a6-8956-5b89a8b02a08 | -9.50852 | -40.31932 | 2025-05-31 00:37:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 6224ef05-4128-3766-84f9-f64bf7defa70 | -11.68666 | -48.25947 | 2025-05-31 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| b1bcc177-4d45-3a33-bd6a-461659ca6992 | -11.8269 | -51.28624 | 2025-05-31 00:37:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8eaf7068-83f0-35e9-9ecb-17edb9fcf134 | -11.83775 | -51.28468 | 2025-05-31 00:37:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| bf53fbbd-b57a-3bb5-82c5-007632c4ce0c | -9.98813 | -48.16234 | 2025-05-31 00:37:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8310abb3-1105-35ed-a3a8-e523b655f475 | -11.89807 | -47.4413 | 2025-05-31 00:37:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bfd75a7d-a6a0-34d8-a3ab-3ed6388c5879 | -10.82563 | -56.96128 | 2025-05-31 00:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8b7ea07d-77b9-3af9-97b3-9cc08465a312 | -10.6459 | -49.4432 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 342685f2-0fa7-3971-b90c-6488dd76543d | -13.10568 | -52.28509 | 2025-05-31 00:37:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 1fb9073e-bad3-3c23-bdc0-d0bcc2b94bbd | -13.62922 | -47.43844 | 2025-05-31 00:37:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8980f7f7-6660-3f22-8d33-1c968258e3cb | -13.10782 | -52.30262 | 2025-05-31 00:37:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| eda39982-a2a8-30b5-adb4-5586c31ee039 | -12.01295 | -49.53664 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 18b5624f-f0b2-3302-9cc8-17cfb6e51c2e | -9.04759 | -47.01677 | 2025-05-31 00:37:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4481fcc0-f2ae-3213-a4bb-57fc172ea488 | -9.34505 | -40.2159 | 2025-05-31 00:37:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 8adeff90-ccef-399b-822a-eb93b0b6ff15 | -12.03359 | -49.51658 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 62127817-3028-3e1f-ad0a-53444424bb21 | -10.654 | -49.43158 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 6277fd61-e934-337f-a5db-116651ddcc4c | -11.20514 | -47.83008 | 2025-05-31 00:37:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bdc5ca12-a387-381b-8439-e7bd3f689f9e | -13.09894 | -52.2796 | 2025-05-31 00:37:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b7aa531a-12d3-34ce-898a-8bfbc54d20b9 | -13.85618 | -43.52345 | 2025-05-31 00:37:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 85b349ec-c4a6-3705-9ad8-002a73cdaaef | -10.64457 | -49.43289 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 30eec770-ab49-3cd6-b2ae-3e6bfcca1741 | -15.37524 | -45.67573 | 2025-05-31 00:37:00 | TERRA_M-M | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0c20c6dc-c8d9-369d-95ab-0cf6dab8f370 | -11.89931 | -47.45035 | 2025-05-31 00:37:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 574db01f-5a26-356b-af9c-c01eb08f67bd | -11.78844 | -44.28292 | 2025-05-31 00:37:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 98056416-1e4e-3afb-af2d-1ef0da0ad2ee | -12.01155 | -49.52589 | 2025-05-31 00:37:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 7e74f1df-2447-3ea1-a384-ca8b8756dd57 | -9.75805 | -48.22578 | 2025-05-31 00:37:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54172ed3-1e97-32a7-9f3e-8122283f3f4b | -13.09837 | -45.28493 | 2025-05-31 00:37:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 949bf3c4-4574-3bdc-8b87-23f3b6b84c12 | -10.73705 | -49.2891 | 2025-05-31 00:37:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 5b97a79c-66e4-39f0-ab50-da412b35795e | -8.679 | -48.2856 | 2025-05-31 00:37:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6b033866-9bbe-362f-993f-11c667353fc5 | -11.68791 | -48.26892 | 2025-05-31 00:37:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72e99517-e102-3ef0-8a81-d095893d5ef0 | -9.60774 | -49.02591 | 2025-05-31 00:37:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dd80eea7-7d86-33ba-84b6-3d8e10fb20c1 | -13.08937 | -45.28631 | 2025-05-31 00:37:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c73ac9f5-8ca0-34dd-af30-15644eaf8921 | -13.63938 | -47.44632 | 2025-05-31 00:37:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf52c762-f095-3cc7-bd57-58e8cae18d51 | -11.79003 | -44.29351 | 2025-05-31 00:37:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README2.md)
