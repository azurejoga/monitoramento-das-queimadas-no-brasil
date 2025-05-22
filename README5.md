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
| 2038dcd8-4766-3b98-8e51-4962588a8d21 | -10.8304 | -56.954102 | 2025-05-22 01:18:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f86526ab-1f56-3a4e-8e8b-3733e3e50824 | -21.484501 | -57.1171 | 2025-05-22 01:18:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb78d49b-d346-300e-92b0-bc07257c50c9 | -20.946699 | -56.597599 | 2025-05-22 01:18:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f8b5a614-4db4-33e0-8de9-ac1adad2abf6 | -12.2943 | -52.4995 | 2025-05-22 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| cb94710a-d241-3c14-bd02-e888988acff5 | -20.9601 | -56.5967 | 2025-05-22 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 140.7 |
| a9fbaeef-8b1b-3d2f-a24e-78dc47b49b47 | -20.9402 | -56.5786 | 2025-05-22 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 52139c15-c7fa-3ffe-ade6-28eb5e756090 | -10.3237 | -47.0283 | 2025-05-22 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 31ba014a-3e43-3ea8-81e0-3ec9b581122c | -20.9398 | -56.5998 | 2025-05-22 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 3b663e62-fb63-300f-b506-9cb704535081 | -11.5719 | -47.4521 | 2025-05-22 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 61bbc28d-4300-312d-8d95-edddac4333f8 | -11.5528 | -47.4546 | 2025-05-22 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| f19db21e-59d0-33cd-b3c0-08a0828da487 | -11.5723 | -47.4298 | 2025-05-22 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 88786bae-15cf-3b65-aef4-e012921e494c | -20.9606 | -56.5755 | 2025-05-22 01:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 6b11058c-ff9a-3b65-b691-9ce9f6067065 | -11.5532 | -47.4323 | 2025-05-22 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b4ee2ed0-08b8-3c16-a1bb-4375b48f377c | -20.9606 | -56.5755 | 2025-05-22 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 0dc54760-5ce3-3058-9f2e-3b6d15860d0f | -11.5719 | -47.4521 | 2025-05-22 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 601f5c81-72d2-3556-89a5-5e4262f024c7 | -20.9601 | -56.5967 | 2025-05-22 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 136.6 |
| d4f1d46e-38bb-3431-a221-b77fc48a7f12 | -20.9402 | -56.5786 | 2025-05-22 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e71cba8b-1d85-3ce6-88fd-28524e94b6da | -10.3237 | -47.0283 | 2025-05-22 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5d2c6d79-1682-3de1-ac02-9c3fe44e8330 | -20.9398 | -56.5998 | 2025-05-22 01:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 21e800d1-396d-382d-aed4-a708bbe7c9d4 | -12.2943 | -52.4995 | 2025-05-22 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e227fd9d-11ad-3a3f-9c95-9f1ae37297fc | -11.5528 | -47.4546 | 2025-05-22 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 8c3e40ed-a956-32c7-bad9-53c65e3eed65 | -12.3515 | -49.9833 | 2025-05-22 01:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| dc5b94c6-a511-3f60-8569-5dfaaec2757d | -11.5528 | -47.4546 | 2025-05-22 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| ced5d408-7c1f-3a83-8246-895ae9514a73 | -12.2943 | -52.4995 | 2025-05-22 01:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 2e721c2b-9aa0-3ef2-978e-98b6fae5f6d4 | -11.5723 | -47.4298 | 2025-05-22 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| be602a75-b1df-3b58-818b-e7af34966fe5 | -20.9398 | -56.5998 | 2025-05-22 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 72.1 |
| a204b8c5-0642-3f06-b26b-b2d24288abc6 | -20.9606 | -56.5755 | 2025-05-22 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 04ca2d7d-589b-374a-b7c0-0ad069106fbb | -11.5719 | -47.4521 | 2025-05-22 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 137.5 |
| ca2b60d9-6479-35b2-8eb6-7b76a186f7d4 | -20.9402 | -56.5786 | 2025-05-22 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 531b9cff-ec71-3f77-b703-4cb0267c22b0 | -11.5532 | -47.4323 | 2025-05-22 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| b2fe2bf9-976f-3231-b76a-24c6c991df06 | -20.9601 | -56.5967 | 2025-05-22 01:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0479640f-7cbb-3e6f-8f91-cbe818729db5 | -12.2943 | -52.4995 | 2025-05-22 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 636c6c88-b699-3b12-82dc-10824b4a61f9 | -12.3515 | -49.9833 | 2025-05-22 02:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 122802a6-3e1e-34d4-a3a3-314a41451182 | -20.9606 | -56.5755 | 2025-05-22 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f28cb8f1-33d0-3d08-8529-765465a4ed04 | -20.9398 | -56.5998 | 2025-05-22 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 57fe45e6-b3ab-3272-b5fb-a2c37f12b16b | -11.5719 | -47.4521 | 2025-05-22 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 540c5270-c6e6-3a38-9fe4-ca9c4f6730d3 | -11.5723 | -47.4298 | 2025-05-22 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 2bb28431-0286-3de3-943d-05050c0bf312 | -20.9601 | -56.5967 | 2025-05-22 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3bb83cbf-12ae-3b98-8920-1f9f76f7141a | -20.9402 | -56.5786 | 2025-05-22 02:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4d331a6d-eb3d-35ba-9030-8f22b85b7db5 | -11.5528 | -47.4546 | 2025-05-22 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7b81db93-ecb7-3a85-a224-7bbeacee8292 | -12.2943 | -52.4995 | 2025-05-22 02:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fdb39a9a-e8e9-3b58-927c-ea019270fc0f | -20.9402 | -56.5786 | 2025-05-22 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 7b569e2d-aa20-38fd-a9d6-7b22956df5ca | -20.9606 | -56.5755 | 2025-05-22 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 948b91dd-1f30-3bf4-be9c-d43e4860eb55 | -20.9601 | -56.5967 | 2025-05-22 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 07a9beae-a004-3495-83bd-a72f177a1f03 | -20.9398 | -56.5998 | 2025-05-22 02:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ca8dbc48-1c5c-368f-bfdf-985af75a5b6a | -11.5528 | -47.4546 | 2025-05-22 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 26d7a189-ea54-3b3d-be0f-b061be423335 | -11.5719 | -47.4521 | 2025-05-22 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 99793592-5efe-3bd3-bd2f-7cad877d085f | -11.5723 | -47.4298 | 2025-05-22 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 0156a47b-8645-37af-8329-f540cdfe8abd | -20.9606 | -56.5755 | 2025-05-22 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f306db95-53ba-3e4b-934b-3efa5103aad9 | -20.9398 | -56.5998 | 2025-05-22 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 326c798d-4afa-3dc1-a066-dc427b9246a6 | -20.9402 | -56.5786 | 2025-05-22 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8e5c7710-dc21-364e-9b91-2e98db6b71fd | -12.2943 | -52.4995 | 2025-05-22 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4e2b0563-e562-36e2-bd7a-45037d0b4c0d | -11.5528 | -47.4546 | 2025-05-22 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 462edf79-255d-3c93-a641-5c6fc6e3abb6 | -11.5719 | -47.4521 | 2025-05-22 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a089e48d-a321-3e91-9b7f-900ab0c94977 | -20.9601 | -56.5967 | 2025-05-22 02:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d6e16482-7ed4-3510-ace6-0733c64c12ee | -12.2943 | -52.4995 | 2025-05-22 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| cef3fffa-9cf4-34ae-a12f-95a92f1555ad | -11.5719 | -47.4521 | 2025-05-22 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 83f22137-89ef-3e65-b839-b956933459fa | -20.9398 | -56.5998 | 2025-05-22 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b4179def-d382-3c3d-a8d9-c4f110ed2efb | -20.9402 | -56.5786 | 2025-05-22 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e5ee673d-ae98-30d3-9f8e-66b536cfb9e9 | -20.9601 | -56.5967 | 2025-05-22 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 091e1354-d032-3248-9b94-a32bcb6e4e63 | -20.9606 | -56.5755 | 2025-05-22 02:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0a4c82fc-4c22-3135-a443-3795119a61bf | -11.5528 | -47.4546 | 2025-05-22 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| cdbbe146-a74c-3bc0-bd97-a4b52b2502c7 | -12.2943 | -52.4995 | 2025-05-22 02:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 792dfbfc-d59d-3a01-bbbd-71d29f413909 | -20.9398 | -56.5998 | 2025-05-22 02:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 32009e5b-e11e-37f8-b840-8f15cab444c3 | -20.9402 | -56.5786 | 2025-05-22 02:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fa64780c-f29c-34df-a11a-7934520e34dd | -20.9601 | -56.5967 | 2025-05-22 02:40:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 03e26e61-9759-362a-9610-8bc5c4c7b326 | -11.5532 | -47.4323 | 2025-05-22 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 29ae3733-d12a-362c-a581-d1cea2a16aef | -20.9398 | -56.5998 | 2025-05-22 02:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8ba71769-e7a8-3786-88a7-b1a00890f9c7 | -11.5723 | -47.4298 | 2025-05-22 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 8a9298f3-5422-3609-9598-d4096279673d | -11.5528 | -47.4546 | 2025-05-22 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b10c35a4-292c-3f2a-853a-6cd1457d35cf | -11.5719 | -47.4521 | 2025-05-22 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0c8e1999-f83b-3ff0-a027-6afdd83a54d7 | -20.9606 | -56.5755 | 2025-05-22 02:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1b4d79a2-3f7a-3758-ae5e-6c224be326e8 | -12.2943 | -52.4995 | 2025-05-22 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 58a9be66-5695-34f9-8c35-a9969efd549f | -20.9601 | -56.5967 | 2025-05-22 02:50:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7e694677-7cbb-355d-b276-dd52d43d6c6b | -11.5723 | -47.4298 | 2025-05-22 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e0b23b6d-2891-3217-8341-bf2c5f8d0d63 | -11.5528 | -47.4546 | 2025-05-22 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8bc27546-55d4-38a5-992a-94b7a3ed8eb0 | -20.9601 | -56.5967 | 2025-05-22 03:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4675ed13-3005-3c45-a216-73c7d7e1c1dd | -11.5719 | -47.4521 | 2025-05-22 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 95df0575-3c8e-33ff-912e-841d8eaf3e9c | -20.9606 | -56.5755 | 2025-05-22 03:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 8988014f-5ee4-3e33-b4a4-862ebb9e1991 | -12.2943 | -52.4995 | 2025-05-22 03:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8717f23c-104c-3d15-a26a-f094938fe6dc | -17.27547 | -42.64922 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 146cc95c-e559-3a56-97d7-2881c8996a6f | -17.27785 | -42.65577 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c606138-744c-3ce9-8a34-0b04e8eaae24 | -17.27395 | -42.65567 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e1c98a11-1622-3242-a0f2-2e9602d6f469 | -17.26521 | -42.66133 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a822ce75-098c-387f-b9bf-08178c622fe7 | -17.26684 | -42.65436 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 25237066-eceb-3096-b04c-292e079fa93e | -17.26903 | -42.66153 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b663652b-7023-38c6-bef8-860effa74d89 | -17.27073 | -42.65447 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 36c26b2f-629a-3850-9bd3-26da9736827f | -17.27939 | -42.64934 | 2025-05-22 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccb47026-ab1a-32ce-b7cf-f5eb3ae2644f | -22.6755 | -42.85715 | 2025-05-22 03:08:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 20e434c1-7fd8-35b1-882f-6dc204df5e59 | -22.16444 | -42.94081 | 2025-05-22 03:08:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1bd3be0f-140e-3f5a-b02d-5c6c7ad073cb | -22.67446 | -42.86249 | 2025-05-22 03:08:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 167f268d-dcde-3d5f-b73d-f9b62ffa7c51 | -22.16293 | -42.94693 | 2025-05-22 03:08:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6cf3d0ce-0633-3b96-b381-6bef9aec5302 | -22.67586 | -42.85672 | 2025-05-22 03:08:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 34e2047f-a2c1-3c17-8298-c6fab38796cf | -20.9402 | -56.5786 | 2025-05-22 03:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2a449b2e-2ee2-34a4-8370-8b3043021dfd | -12.2943 | -52.4995 | 2025-05-22 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 07735bf4-7c85-3bfd-8349-ca0041c05c94 | -11.5528 | -47.4546 | 2025-05-22 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| ff508abd-94fa-3d5c-83c1-f152a9b980fb | -11.5723 | -47.4298 | 2025-05-22 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b9a8cc70-16b5-3a69-80e6-7ab2aef79202 | -20.9398 | -56.5998 | 2025-05-22 03:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 07ffeca4-b2cd-3ebf-88ba-e1f62b45c96a | -11.5719 | -47.4521 | 2025-05-22 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 47ec2d7d-4a82-3544-b3fe-0ff3f4aae514 | -20.9402 | -56.5786 | 2025-05-22 03:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |


[Clique aqui para ver as próximas entradas](README6.md)
