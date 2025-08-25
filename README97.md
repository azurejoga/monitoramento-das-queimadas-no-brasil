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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9fe250-6e1d-3835-98fc-39a1752a8123 | -11.6089 | -46.3699 | 2025-08-25 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 095e2afe-923f-319a-bde1-ad073e2180d8 | -12.6937 | -47.8339 | 2025-08-25 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 320.5 |
| ee0dc219-9bc9-3abf-973b-bdcec2dc16b9 | -6.8202 | -59.4194 | 2025-08-25 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c4ebc683-34e6-366a-a902-12447a17a8ff | -12.3078 | -49.1421 | 2025-08-25 13:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 150f4711-78f4-3dab-9bcb-bffbcadb9e2f | -8.5943 | -62.6315 | 2025-08-25 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 1bd5f01f-b4b3-3ae7-b769-4d538e10a8d2 | -14.2543 | -58.6082 | 2025-08-25 13:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 595dfba3-9aff-363e-a9d5-ad6c061e8fee | -12.6745 | -47.8366 | 2025-08-25 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 9a46930f-5959-3acf-aa5b-84a8ef844bb4 | -13.832 | -46.6946 | 2025-08-25 13:50:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7773b633-307a-3847-823c-2d6de6a912aa | -21.4303 | -47.5922 | 2025-08-25 13:50:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 124.2 |
| d024446a-128d-3d5f-8be5-0dcac502ff58 | -10.7206 | -47.1365 | 2025-08-25 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 4f92306a-a890-3f7c-92b4-c0d37ece6a55 | -6.8202 | -59.4194 | 2025-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 00a44f4a-e7a2-3d8c-a75c-6f2859156ba4 | -10.7015 | -47.1388 | 2025-08-25 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 269.5 |
| d7ad1885-9ecc-329e-a4e6-49e1ec7fcf86 | -8.8734 | -62.4495 | 2025-08-25 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 16a2bbe3-d4e0-3303-8c69-0cd8d6c15564 | -6.8201 | -59.4386 | 2025-08-25 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 68cff5fa-e0e1-33ce-b1c5-2e1ceb8a69ba | -6.4357 | -44.5535 | 2025-08-25 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a20f5d9d-6183-3a56-a970-f9ad95fb9095 | -13.4423 | -46.87 | 2025-08-25 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 887086bb-5ddb-374a-8d13-a318cf3f2798 | -7.9076 | -63.0919 | 2025-08-25 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2224ef14-4f25-34d7-9246-bef0ee9deb92 | -14.5076 | -51.914 | 2025-08-25 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 45f964df-cc91-3696-8f30-730d675a4985 | -8.5944 | -62.6126 | 2025-08-25 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 00a3a977-4eb9-340c-9562-4e6c990dd9b2 | -9.324 | -48.2633 | 2025-08-25 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e5eb747c-b9c0-311b-981c-67dd0e3dee9b | -11.6093 | -46.3472 | 2025-08-25 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 48f72052-0e98-3d73-8c8f-d0fafb933338 | -7.605 | -47.4599 | 2025-08-25 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 08575f57-63cc-33ad-866c-0ef18bb0c687 | -6.5216 | -45.343 | 2025-08-25 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 0d4ce88b-e1a1-37f4-84f7-775c9d55cda0 | -8.8919 | -62.4487 | 2025-08-25 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| c5c5f171-96f3-39a4-833f-a7926e7d5825 | -8.6313 | -62.649 | 2025-08-25 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 67209016-0e3c-3cb9-b0d8-c29e5274395a | -8.8918 | -62.4677 | 2025-08-25 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 94c0ba3c-e1f5-343b-b977-e0b5365eb785 | -9.2262 | -59.7119 | 2025-08-25 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a037805b-d1a8-3282-af9e-2b9e0908a816 | -8.9105 | -62.4479 | 2025-08-25 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 038b92b6-ab74-33c0-b4be-a2222679e3e8 | -13.4419 | -46.8927 | 2025-08-25 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fc229927-c374-3cb6-a975-7de73fe99dd9 | -8.5758 | -62.6323 | 2025-08-25 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 42a02b25-1bda-34f2-b816-e669b3bff2ea | -8.8735 | -62.4305 | 2025-08-25 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 8bfd9bf7-f3de-32f0-b100-6bedec4733df | -7.9077 | -63.073 | 2025-08-25 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 20577273-7671-3fba-864c-58d429cadf26 | -11.2697 | -44.9781 | 2025-08-25 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 7aaffaa0-cdac-39b3-b888-8d4e79d0961b | -7.586 | -47.4835 | 2025-08-25 13:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 0e5a451b-b6ca-3d4c-8337-0c9f98677bda | -10.7093 | -50.5572 | 2025-08-25 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| fbfa04dd-1d8e-3cf1-bf5a-8621b17ac06d | -7.8892 | -63.0737 | 2025-08-25 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| cb15b424-aaee-3dfc-bbda-2cb235baf76a | -9.1812 | -60.7939 | 2025-08-25 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| b645c321-77f8-3229-b45e-972ecac218c0 | -12.6937 | -47.8339 | 2025-08-25 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 259.8 |
| 885cb978-57b6-39e5-abf8-49af94e5c1e7 | -8.5943 | -62.6315 | 2025-08-25 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 118.2 |
| ad6cd02e-e467-3da0-a26a-a2c2dd7a7c81 | -14.5072 | -51.9354 | 2025-08-25 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 894f3b89-0471-3d71-9aae-d067a6f011f7 | -5.6817 | -45.1347 | 2025-08-25 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 57cf54b3-1125-3780-8153-273b22c48727 | -14.3722 | -51.932 | 2025-08-25 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 21b6b2ba-7acf-3d6e-abd9-54f27a2a5cd4 | -7.5862 | -47.4615 | 2025-08-25 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3fcbdf9c-0c0e-3f1b-820a-0dab2840399d | -9.2076 | -59.7129 | 2025-08-25 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| aa411f96-4a76-3c62-a554-d3b7df5aeef1 | -8.8921 | -62.4297 | 2025-08-25 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| fa519815-2f4f-3437-a81a-063efeb931ef | -10.7096 | -50.5359 | 2025-08-25 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 606283ef-ed3f-3fd0-a8e5-25046e435242 | -8.7584 | -49.9566 | 2025-08-25 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 1c9ea5d7-9f32-3b10-88d3-52c603b98e70 | -8.5759 | -62.6133 | 2025-08-25 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.8 |
| ae75e4d1-0cc1-3423-a702-62d19c7686f1 | -18.7359 | -45.1396 | 2025-08-25 13:50:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 6ef9a231-4ca8-302b-9453-82dbfc3c85f9 | -5.6254 | -45.1612 | 2025-08-25 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 16906248-300a-30ed-998b-56a37766068c | -7.9077 | -63.073 | 2025-08-25 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ade706e2-a3a4-3f64-a880-9a41689df209 | -14.3722 | -51.932 | 2025-08-25 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b5128c89-a375-348c-8f17-e3e043d15a6c | -5.6441 | -45.1599 | 2025-08-25 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 887d8fb8-1bda-3231-af2f-1014afee25f4 | -14.4362 | -56.4564 | 2025-08-25 14:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c7376ac0-3f22-3b58-8dcf-3bb200566e37 | -12.6745 | -47.8366 | 2025-08-25 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| ae8ba942-3aba-3a0d-b9b4-ab7e30bdb128 | -18.715 | -45.1684 | 2025-08-25 14:00:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 3cfaf6ee-3f8c-38f8-9c1d-79e30a3874f3 | -11.5441 | -50.4876 | 2025-08-25 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 2457451e-a003-3d36-878d-ec70e9b99663 | -18.7359 | -45.1396 | 2025-08-25 14:00:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 130.7 |
| dcd0cb9e-9ced-3133-9298-19318ffcbf1b | -6.8202 | -59.4194 | 2025-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| f98110cb-b4ae-3213-a91e-f6dd53c823f1 | -11.6089 | -46.3699 | 2025-08-25 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 3b0dc90c-be0d-3f0a-95e8-396963a501d9 | -7.5862 | -47.4615 | 2025-08-25 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 2c5bfcfe-fc22-3e86-b9a1-9723aecdcbe5 | -21.4303 | -47.5922 | 2025-08-25 14:00:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 3809ccc7-04bd-317f-abb2-aea073765d07 | -6.1377 | -44.3711 | 2025-08-25 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 266a75cb-785f-3b5b-b35d-16a6cfbbae9f | -14.7918 | -45.3786 | 2025-08-25 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 545f8f02-bafb-3e9d-94c2-3f10f11eb651 | -7.8892 | -63.0737 | 2025-08-25 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c9bb4a66-55ea-393b-8c3a-cd1cec717e44 | -6.4357 | -44.5535 | 2025-08-25 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 9c8c0867-71fa-3c21-b2f9-cd4588a79b03 | -11.6086 | -46.3926 | 2025-08-25 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 02b55925-8476-307a-b4c3-7c550cafbd75 | -6.5216 | -45.343 | 2025-08-25 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f0594899-46a5-317c-8854-0ba3e1d0d3a0 | -14.2543 | -58.6082 | 2025-08-25 14:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a982232f-142e-3504-83e1-bee641e4e46d | -7.586 | -47.4835 | 2025-08-25 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 304.1 |
| 80c6f39a-5e57-3b4f-895e-c12b43ca616c | -10.7096 | -50.5359 | 2025-08-25 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 2e09c33d-943d-3b33-b8e8-791c4a7e0ba0 | -11.6803 | -51.5777 | 2025-08-25 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 34901cc5-8150-3dd4-9c90-2b453cfe99e5 | -5.6443 | -45.1373 | 2025-08-25 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d09ad04f-5031-32ba-aab3-27f00a559c83 | -9.1812 | -60.7939 | 2025-08-25 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 286.0 |
| 7d3666cc-e8b5-37f8-8082-32840d4debdc | -15.0725 | -48.6745 | 2025-08-25 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4c9781b7-0937-3d46-bcd5-de641c4ae7e3 | -6.4121 | -45.0571 | 2025-08-25 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| d263f43c-f74a-3a56-bba2-1c373555cd8f | -11.68 | -51.5989 | 2025-08-25 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| df95bd79-6c1e-3e2d-8d5f-2e86d2750e74 | -9.006 | -65.4 | 2025-08-25 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| d5ca4d54-05be-3195-8571-6d57c2fae546 | -14.9247 | -45.5403 | 2025-08-25 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 310.2 |
| 6a4903c8-3548-3ff5-9a64-ded60833ee5a | -9.181 | -60.8131 | 2025-08-25 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9246123c-c44c-3324-ad6d-f20dc2bd149a | -6.9061 | -44.4217 | 2025-08-25 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1192f65f-b57b-3424-b406-8f719a64c764 | -9.0059 | -65.4186 | 2025-08-25 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 96071f51-3f2d-3a32-be95-06b1f69698b0 | -11.8601 | -45.1233 | 2025-08-25 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 82e2f67b-6ea1-333b-ba50-1cb322bd7fc0 | -10.7206 | -47.1365 | 2025-08-25 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 3440d6c2-2d3a-36b9-a841-2606b2c5a39f | -8.9874 | -65.4192 | 2025-08-25 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 813.5 |
| 3fddcf2e-9f92-3c26-bca2-d85fbbc2b09a | -6.0267 | -44.2189 | 2025-08-25 14:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 713ebc61-4e22-3c73-989f-bb1f6a60c8e2 | -11.5444 | -50.4662 | 2025-08-25 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| b923f877-91cb-375b-bbcc-dd3789df2b62 | -12.6937 | -47.8339 | 2025-08-25 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 256.8 |
| c5635122-8fbb-3875-be5a-158f0f7d2c18 | -10.7015 | -47.1388 | 2025-08-25 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| dad7cc0f-476e-321a-9cd5-21beaa6bc085 | -8.9875 | -65.4006 | 2025-08-25 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 36b3fe58-c739-37bb-af6d-dc89c7501e7b | -6.8201 | -59.4386 | 2025-08-25 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.1 |
| e31e9dd7-ddab-309d-8f43-7cb783bad25b | -9.2076 | -59.7129 | 2025-08-25 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b64bafe5-10e6-3e36-b3f8-118487cbe263 | -9.1813 | -60.7747 | 2025-08-25 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 993ca398-7cff-3543-a6f5-bdbbfd62ddc0 | -11.2697 | -44.9781 | 2025-08-25 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 786d4f6a-66c2-32b9-9232-ff5f74c2e90b | -9.1998 | -60.793 | 2025-08-25 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b6da4168-b7bc-3fdc-a79e-696efb85e877 | -14.7722 | -45.3822 | 2025-08-25 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 865f5d14-4e36-3a7f-a50b-84ac839efb2b | -5.6817 | -45.1347 | 2025-08-25 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a8a5a2f1-b89d-3c3a-b4b1-e3ab9ec3fb24 | -6.9063 | -44.3987 | 2025-08-25 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3c88bae0-0698-3bee-b34f-86586f8d7bb1 | -7.5862 | -47.4615 | 2025-08-25 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 2afe886c-0138-3b20-b1ea-385913c082df | -12.6937 | -47.8339 | 2025-08-25 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 265.5 |


[Clique aqui para ver as próximas entradas](README98.md)
