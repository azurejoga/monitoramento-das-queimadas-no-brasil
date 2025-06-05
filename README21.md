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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19bf9b72-50a0-368b-a330-509fa27a331a | -13.515 | -56.5893 | 2025-06-05 08:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 3217f39d-6454-3a56-98dc-bb8ff9abe776 | -13.5152 | -56.569 | 2025-06-05 08:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 0167a572-e101-3c34-866d-e6748473300e | -13.5152 | -56.569 | 2025-06-05 08:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 178.8 |
| cda76be9-ebe9-36eb-ad3e-741106e12637 | -13.5344 | -56.5672 | 2025-06-05 08:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 4d8509b1-413a-3726-a6e9-33ea1d44f7a9 | -13.515 | -56.5893 | 2025-06-05 08:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| f584b51c-5ff1-3052-8b0b-77a9b8230ec3 | -13.5155 | -56.5488 | 2025-06-05 08:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 1d988ee8-d39e-3cfd-ac6e-da02cb9a87a9 | -13.5155 | -56.5488 | 2025-06-05 08:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9d049efd-c39d-35c1-b506-815fb8da3c72 | -13.5152 | -56.569 | 2025-06-05 08:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 2444903a-211c-32d2-aad4-257dc26839da | -13.5344 | -56.5672 | 2025-06-05 08:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5fdb6012-1731-3973-b2ef-7ef783394ede | -13.5155 | -56.5488 | 2025-06-05 08:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 72cec3d5-2942-36ac-8625-c9936d554a02 | -13.5152 | -56.569 | 2025-06-05 08:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 183.9 |
| e5b7d632-1058-3a24-9720-f7771a3cf113 | -13.5344 | -56.5672 | 2025-06-05 08:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| fe0a464b-0a26-36b4-9eca-d956458684fa | -13.515 | -56.5893 | 2025-06-05 08:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 43cbd0e4-ddf7-3b35-a1fe-c7c6759f1e16 | -13.5155 | -56.5488 | 2025-06-05 09:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 8a79bb47-f821-3df5-b6ee-2e01d66112b1 | -13.5152 | -56.569 | 2025-06-05 09:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 42bf41cb-99a2-3406-a577-049f4d6c749d | -13.5344 | -56.5672 | 2025-06-05 09:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6f2f9ae8-31fc-3758-baa8-e09cb9266ae6 | -13.5346 | -56.5469 | 2025-06-05 09:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| a0e925c9-236a-3c36-a718-8c8b9acfab7f | -13.5344 | -56.5672 | 2025-06-05 09:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d2ef40e3-1fd5-3db2-8b08-ff7d647f0d1e | -13.5152 | -56.569 | 2025-06-05 09:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 7c485b9e-66ce-3916-a022-d8d0207b1294 | -13.515 | -56.5893 | 2025-06-05 09:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 60235c8b-a44f-3bee-9a9e-aca80fee7aa3 | -13.5155 | -56.5488 | 2025-06-05 09:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6bf0bcce-8dd4-3691-b6ea-47d510c99b2a | -13.5155 | -56.5488 | 2025-06-05 09:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5099a132-98c8-37ea-bd11-8c9ee9d31966 | -13.5152 | -56.569 | 2025-06-05 09:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 12ede800-f973-3bfc-85b1-48a822d5866f | -13.5344 | -56.5672 | 2025-06-05 09:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b9cf17b2-2caa-3647-b5b5-299890f8c53c | -13.5152 | -56.569 | 2025-06-05 10:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 949552b3-2577-338e-8395-917f03efaeaa | -13.5152 | -56.569 | 2025-06-05 10:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 159.5 |
| a1caffa0-4c03-3e06-b51f-d5d1f58b8ebf | -13.5152 | -56.569 | 2025-06-05 10:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 3ebb2dea-5938-35c1-9c94-261d8c2365da | -13.5344 | -56.5672 | 2025-06-05 10:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 20b12f5a-765b-3ad1-984e-ee12df8884b9 | -13.5155 | -56.5488 | 2025-06-05 10:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 50942a9b-79ec-3d70-aec5-d677314bdefb | -13.5152 | -56.569 | 2025-06-05 10:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 2fa0ce22-09e6-3ca6-a79c-57d62b7acb38 | -13.5152 | -56.569 | 2025-06-05 10:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 95468879-46ad-35ca-a4ae-00a8f15f0419 | -13.5155 | -56.5488 | 2025-06-05 10:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 39beeebd-ce6c-3c96-8bb1-fb28081538ad | -13.5344 | -56.5672 | 2025-06-05 11:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 219b8fe8-8cc2-3aa9-9057-388b1fb189ab | -6.9602 | -42.9052 | 2025-06-05 11:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 9653f470-6564-3036-b2f5-65144bebde1d | -13.5152 | -56.569 | 2025-06-05 11:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 214.9 |
| ac407b20-507e-3253-b091-5ca8c15b1fc9 | -13.5152 | -56.569 | 2025-06-05 11:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 195.3 |
| a3420a03-1616-3257-9823-ca44da152800 | -13.5344 | -56.5672 | 2025-06-05 11:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 1a918055-c4a2-34d8-9a49-1a7860e21a01 | -13.5155 | -56.5488 | 2025-06-05 11:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a098af22-e979-370b-9f7d-d449b541a060 | -13.5152 | -56.569 | 2025-06-05 11:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 420cf9a3-d71d-3ee1-8bbe-6440191d5bc8 | -13.5155 | -56.5488 | 2025-06-05 11:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 967ff9b2-e7d0-38bf-bb50-817ac01f6169 | -6.9602 | -42.9052 | 2025-06-05 11:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| c4cba419-ff93-34a3-b2bf-04392279d50e | -13.5344 | -56.5672 | 2025-06-05 11:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 5aaf7cc1-d619-36e5-a0bb-491b17a614b0 | -13.5152 | -56.569 | 2025-06-05 11:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 4e54b683-3c88-3267-8d20-200e8b212076 | -6.9602 | -42.9052 | 2025-06-05 11:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 436ebb59-88fc-3735-ad9d-d19ae30a9f46 | -13.5155 | -56.5488 | 2025-06-05 11:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 79a609f6-340a-37e2-8bf2-e693f4f837a4 | -6.9602 | -42.9052 | 2025-06-05 11:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| b496e521-a954-35a0-b168-9bfdd327c2f1 | -13.5344 | -56.5672 | 2025-06-05 11:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6f733438-29dc-334f-829c-f0ef60f84464 | -13.5152 | -56.569 | 2025-06-05 11:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 184.2 |
| aea9e45f-1f3d-397c-b32f-8efbf4badb72 | -13.5152 | -56.569 | 2025-06-05 11:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 201.8 |
| f9b4c761-3a36-3292-8f7b-813d193318d1 | -13.5155 | -56.5488 | 2025-06-05 11:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 9d3cd49e-78ce-340d-ab31-71e5442d9fc5 | -6.9602 | -42.9052 | 2025-06-05 11:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| a7c8e336-7c36-3cd8-b4a3-5f3af0bd1dce | -13.5152 | -56.569 | 2025-06-05 12:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 1cd406f8-21c2-3e6f-8a42-0a27e98b47a4 | -13.5344 | -56.5672 | 2025-06-05 12:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 1b14e58a-67ad-3155-90ba-3b1dda70b9db | -6.9602 | -42.9052 | 2025-06-05 12:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 3b199de2-3587-33f6-aabb-966f9919abcf | -13.5155 | -56.5488 | 2025-06-05 12:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 47b0f84c-55d3-32f4-aca7-278a0389253b | -13.5344 | -56.5672 | 2025-06-05 12:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |
| c6efbad2-2e11-3018-856c-a598443d6c97 | -6.9602 | -42.9052 | 2025-06-05 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| bd215b35-ceab-38ed-a083-b9094aaa065e | -13.5152 | -56.569 | 2025-06-05 12:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 0e14a350-23c7-3972-80e4-1caed8659fcb | -13.5155 | -56.5488 | 2025-06-05 12:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 002da99a-0f70-307b-9490-810e21a2bf38 | -13.5344 | -56.5672 | 2025-06-05 12:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 5b98365e-90bd-375d-a03e-23fc27cb46ed | -13.5152 | -56.569 | 2025-06-05 12:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 190.0 |
| b8b5b7fa-e0c7-3ccc-a004-4f651be8f10c | -6.9602 | -42.9052 | 2025-06-05 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| af4c1adc-329a-36f4-9649-3a23e4359f67 | -13.5155 | -56.5488 | 2025-06-05 12:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3fe73e63-f46f-340d-bbfe-f6bdb880b972 | -6.9602 | -42.9052 | 2025-06-05 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 2b791d9a-ff54-3b03-80b2-8ca1ef91ccc3 | -10.858 | -46.8513 | 2025-06-05 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 390bd452-7b10-39b7-9608-ee73ae5b1f3c | -13.5344 | -56.5672 | 2025-06-05 12:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| b7732971-d3ff-3d2e-b4e6-95a6e161ee10 | -13.5152 | -56.569 | 2025-06-05 12:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 7d715a8b-7da8-3575-b899-12ec8ddd5740 | -13.5152 | -56.569 | 2025-06-05 12:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 205.0 |
| a10563cc-04a0-349f-85fb-49d2c9506598 | -13.5344 | -56.5672 | 2025-06-05 12:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 815ae1b5-9956-3a6f-8fc7-1d41ec08d3e9 | -6.9602 | -42.9052 | 2025-06-05 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| 4524b931-30fc-35f5-8b28-984080b5daae | -13.5155 | -56.5488 | 2025-06-05 12:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7ef35428-9147-3c68-b0b3-073c88aa9802 | -13.5152 | -56.569 | 2025-06-05 12:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 206.6 |
| fe248d0f-c9ea-3d02-b619-d36a56c810fe | -13.5155 | -56.5488 | 2025-06-05 12:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 2e042a9a-aa57-3006-bcdb-94dd311e54b8 | -6.9602 | -42.9052 | 2025-06-05 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.5 |
| 1c9f2097-deea-3ddb-9bf3-b36e17892b17 | -13.5344 | -56.5672 | 2025-06-05 12:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| bcbb47c2-19cd-371b-b61b-589cd3a0866f | -13.5346 | -56.5469 | 2025-06-05 12:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| cfa56f47-20ac-3139-a169-396f7e1289f9 | -13.5152 | -56.569 | 2025-06-05 13:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 299.5 |
| bbb1c176-eced-3482-8320-fd549eff7474 | -6.9602 | -42.9052 | 2025-06-05 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 179.0 |
| 36969a9a-7ad8-3d7b-a962-fbe2938dc9f6 | -13.5344 | -56.5672 | 2025-06-05 13:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| f4ec6878-1e71-3303-bf37-9fb69c49aebc | -13.5155 | -56.5488 | 2025-06-05 13:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 9a9ea1f2-91ab-3729-936f-249d89777231 | -6.9602 | -42.9052 | 2025-06-05 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 187.6 |
| 2017b4b2-37cb-35b3-bacf-d068e837fcde | -8.7993 | -45.1044 | 2025-06-05 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7bbf0bd8-4e24-3d14-b8a2-f63cca295b7b | -13.5152 | -56.569 | 2025-06-05 13:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 333.5 |
| 427ab112-c0ed-3b16-b96d-813aef330b9e | -13.5344 | -56.5672 | 2025-06-05 13:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| ec9bec9f-be3e-3a08-b6f8-85d879eaa969 | -13.5155 | -56.5488 | 2025-06-05 13:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 198.8 |
| f686eafa-7963-3be8-9b57-bc760eb72a96 | -8.7993 | -45.1044 | 2025-06-05 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d985d992-b296-3af5-87e1-6778bf21e2a2 | -13.5344 | -56.5672 | 2025-06-05 13:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| f2aca725-0815-353e-a99b-d60d03338879 | -13.5152 | -56.569 | 2025-06-05 13:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 326.9 |
| 953d2c6b-aa65-3cb4-af79-e93a3c361d6e | -13.5346 | -56.5469 | 2025-06-05 13:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 102058e7-c02a-33ea-b279-e05638e23854 | -6.9602 | -42.9052 | 2025-06-05 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.2 |
| ea07e71d-fc85-3cef-ba65-382e379f7688 | -13.5155 | -56.5488 | 2025-06-05 13:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 6914e611-bd2a-3e95-9935-6e952f0d703a | -10.858 | -46.8513 | 2025-06-05 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| da6f0671-df65-3356-8f82-72bf1d0b1497 | -19.051 | -53.4631 | 2025-06-05 13:30:00 | GOES-19 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 1bb453d8-d2a9-3c48-a10c-157c6636df69 | -13.5152 | -56.569 | 2025-06-05 13:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 366.5 |
| bde3148f-a307-3c3c-a2f8-6b190883fc81 | -13.5344 | -56.5672 | 2025-06-05 13:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 5e045bd7-82aa-301a-a3bd-bed33704a982 | -13.5155 | -56.5488 | 2025-06-05 13:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 493ec44b-b78a-3f4f-b458-b9f89266c008 | -10.858 | -46.8513 | 2025-06-05 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 20e81253-4a30-3a24-afd2-c30937347b37 | -13.5346 | -56.5469 | 2025-06-05 13:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 33fcaffe-c74d-39f3-b894-51f70c0ca8bd | -8.7993 | -45.1044 | 2025-06-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d458ab31-f404-3812-9e18-68cac65a082a | -8.7993 | -45.1044 | 2025-06-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |


[Clique aqui para ver as próximas entradas](README22.md)
