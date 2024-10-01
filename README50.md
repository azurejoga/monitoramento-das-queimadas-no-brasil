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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be4991f1-c372-3eb5-8bfc-9cc988e327cc | -13.02129 | -51.23398 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 48336a32-1b26-3ac5-883c-6e0d7981fb5c | -13.02098 | -51.22209 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ee075efa-cb50-3a6b-b210-dcc3b4c8cb25 | -13.0206 | -51.30243 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 1073c9ac-879a-3bfa-8422-a15c25913ca8 | -13.02024 | -51.25923 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 15a70ebe-570b-30c8-8e4b-6f81f13ec633 | -13.02002 | -51.23989 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 05f1b0cc-489d-391c-a19c-9c7ccbdd6e5e | -13.01975 | -51.22802 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| da49f9f8-fc1d-3261-a6e1-54e426a88bb3 | -13.01932 | -51.30842 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 8ee8a48e-d6fe-302f-a869-3262ef99e3fc | -13.019 | -51.26519 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28cfc182-792d-313b-ae66-37399a94137a | -13.01852 | -51.23395 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 921368e0-b26e-35ea-846a-de5754071dc4 | -13.01804 | -51.31441 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 9817d9f7-a797-39c5-96ed-e8d2cb04d545 | -13.01777 | -51.27114 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 51995884-91dc-3f62-a01a-22f82683c771 | -13.01749 | -51.25174 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 030a895d-aa60-3218-ba6e-b871de309beb | -13.0173 | -51.23987 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4aed7efc-40ee-382e-a71e-619d9dfec399 | -13.01719 | -51.22066 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| bb202a99-d9d7-3e7f-b41a-1f4b9e2aebe6 | -13.017 | -51.3086 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| fe8d67c6-fb4e-314c-b3d4-315ef70b84af | -13.01677 | -51.3204 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| cccac0b0-b335-3c49-b16e-8e2580fd4654 | -13.01622 | -51.25769 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bb7a0f16-5e27-3e74-8da3-1dfd23d78b90 | -13.01607 | -51.2458 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| cfe978dc-ff74-3c3f-91e9-c578b0d0f75e | -13.01593 | -51.22657 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b99f2302-a821-378f-904a-7997e90405ec | -13.01575 | -51.31461 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 84a2fef3-2186-3ac4-87ae-5dc4fa2455d4 | -13.01548 | -51.3264 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 2ba19509-a151-3acd-ad18-0df89f6d1448 | -13.01494 | -51.26365 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5c5bb685-7bf4-33a9-86bd-53c923ab1d48 | -13.01484 | -51.25175 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 2d041d65-8467-3147-9593-5929d10f4e4b | -13.01466 | -51.23249 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e6a36915-f931-3bc6-8760-79b2a0e251e6 | -13.01451 | -51.32061 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ebd985cc-38f0-3783-907a-d3c77ac6e11d | -13.01435 | -51.22057 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 94763b54-a701-3062-8413-a4393b43943a | -13.0142 | -51.33242 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a9bca32d-ddb5-3157-a09b-0d11582f113e | -13.01367 | -51.26961 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e6ecaa1-378e-3c7f-9325-41d65420faf9 | -13.0136 | -51.25771 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 226a7c8c-a80d-3eb5-b20d-908e4f0ffc19 | -13.01339 | -51.2384 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 51ad61ce-7206-3a63-86f7-1adf7a086a5e | -13.01327 | -51.32664 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cd254113-af95-3868-bc5a-d93be6e8ec2e | -13.01312 | -51.2265 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c61462c9-f6f6-31ed-bd99-0cf412ad3914 | -13.01266 | -51.30692 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| def1aec5-5ab3-3998-9b77-8fd6110d9556 | -13.0124 | -51.27555 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ca8c58d-4df0-3c94-859c-8021e81176f7 | -13.01237 | -51.26366 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| cf40dfa0-59fa-3d30-826b-52eb33cc3832 | -13.01213 | -51.24431 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 75a66ec0-5ad3-31d4-837e-563dfcdee7fe | -13.01202 | -51.33266 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8f20add-592c-3969-a5c2-000158d2244b | -13.01189 | -51.23244 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| cedf9726-452a-3f79-b10d-b26ab053ba5b | -13.01164 | -51.34444 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a202e795-d0a1-33a2-9868-7cbdf98c5919 | -13.01138 | -51.31291 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 225fb990-cf1a-3c7d-b00b-cc9931fe5802 | -13.01113 | -51.26963 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 55fc5ff9-0a67-3b16-9b53-a1b0a542d3fd | -13.01086 | -51.25025 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 08f98653-ee21-31de-a200-6379a7fb848f | -13.01066 | -51.23837 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 20910a54-fec0-343c-99b6-b72e1ea2ef13 | -13.0101 | -51.3189 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f66e285b-e44d-30ff-aebb-fd5bb37cdf07 | -13.00989 | -51.2756 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 752a2cd7-0b3e-3d7d-b290-515731a2769a | -13.00958 | -51.2562 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 096c2b8b-8977-3a49-9e8b-ee4a88f440cf | -13.00953 | -51.34472 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a91fe354-b1d1-3fc8-8e01-71cf07f3ae5e | -13.00944 | -51.24428 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 4be4d33a-e6a5-3545-807e-2f018c4c65f9 | -13.0093 | -51.22507 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 28543789-546f-3c76-976a-814051554bf5 | -13.0091 | -51.31308 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f2a36a68-4a47-36cc-ad3f-020ef6879dec | -13.00882 | -51.3249 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6a12006e-1e3b-3a67-8084-ae6015e38e8e | -13.00831 | -51.26215 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 624475e4-386f-3fc3-bb90-738cfe0eb6ca | -13.0082 | -51.25023 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 78e00947-d330-37f4-b624-c58737c7c986 | -13.00803 | -51.231 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 596d6428-f021-3631-839e-37e89c8eafe1 | -13.00785 | -51.3191 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 33cc239d-87a9-3e5d-9f9e-5181fa572acc | -13.00703 | -51.26811 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1b041cd8-ecd3-3145-92aa-37ce8c232d69 | -13.00696 | -51.25619 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 38ca7ccd-7a1c-38d2-99e1-8da7749d85c9 | -13.00676 | -51.23692 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| a93aaaaf-747d-350c-9601-2330722f3615 | -13.00661 | -51.3251 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6f7295ab-af7f-3427-aac6-1ba4044db2e3 | -13.00651 | -51.22496 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| eb46e59f-c5d3-32ee-9f0e-36f25ae4248f | -13.00575 | -51.27407 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 24e536ed-25a1-35f0-bc85-f70a50a9ea41 | -13.00573 | -51.26214 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c81ae684-abfc-3fba-85ab-5c01e4df909a | -13.0055 | -51.24281 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ff016626-fda4-3ecc-a48a-f13492a049cc | -13.00527 | -51.23092 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 24f9f723-4498-391d-b2e5-38bea50b37c1 | -13.00449 | -51.2681 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 9c445afa-a075-349b-b641-76abdaedb744 | -13.00447 | -51.28004 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6e79b9db-af7b-322b-9ba1-d5894daad67e | -13.00422 | -51.24876 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f0cf757b-e03e-3d56-90ed-3e8f42688737 | -13.00404 | -51.23685 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 5d379b6b-74d7-37dc-b31d-9ca139ab8e27 | -13.00368 | -51.34896 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 136facbb-6da8-3475-8f71-60a2a363d41b | -13.00344 | -51.3174 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ac639943-9b2b-3a99-85a6-364e3f2543a9 | -13.00325 | -51.27407 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56aed393-0ee6-3861-8497-57a8dde38630 | -13.00294 | -51.25472 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a1d95529-f1ce-3781-afa7-f0d5adb14e8c | -13.00281 | -51.24276 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2ede57bb-a5ae-3e85-bf0c-f5a391fbb2f0 | -13.00244 | -51.31155 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| da166e67-8d04-3105-a5ab-0d977fedef26 | -13.00216 | -51.3234 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 23637dec-467f-31ac-bbc8-5692acf66752 | -13.00201 | -51.28006 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2f9760ab-a694-3552-9d90-80a2274f229e | -13.00167 | -51.26065 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 67cad75b-d6b8-35fe-b735-29917ec61d95 | -13.00161 | -51.34923 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90f14301-2b09-39a1-97c1-0c0f46ba20b6 | -13.00157 | -51.24871 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d47bcfbe-bada-3bb7-96bc-ecfd9e61e99c | -13.00141 | -51.22948 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bf75a499-0f0c-3460-8c0a-da8163f5d8b8 | -13.00119 | -51.31757 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 18448c8d-46c0-37ab-a40f-0fdc2b58164c | -13.00039 | -51.26661 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4807e8b3-3f0e-3a5c-a342-0ac312db1a58 | -13.00033 | -51.25468 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8bc6c96f-b0f5-3e46-a221-4e5ce752131a | -13.00013 | -51.23541 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 036aab58-79d3-3cc9-984e-8207d3ab6b7c | -12.99994 | -51.32359 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 31177d7d-d777-384c-8f48-eace318dd867 | -12.99911 | -51.27257 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 77b65775-e93d-350a-b0d0-53d5f6b35633 | -12.99909 | -51.26064 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3a3051ee-140c-356c-a96a-e123bbdb8e84 | -12.99886 | -51.24133 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 85a25187-d1e7-3fc8-a817-de5c9e88b3d6 | -12.9987 | -51.32959 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7c5eedda-268f-3b4e-ab4c-bfbe07fed63b | -12.99865 | -51.22938 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 18f68576-e33b-3f78-bbd8-93536512640e | -12.99785 | -51.26658 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2cfef3f9-2e7c-3f62-afd9-153fd1017f70 | -12.99782 | -51.27853 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8baed567-ba9f-3f02-816d-9a1ab220bb30 | -12.99758 | -51.24728 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| da43a26f-94f5-3f58-84ff-5842ebeae28d | -12.99741 | -51.2353 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 8c6909b6-597a-3f1c-a31c-88d3f1c55f39 | -12.99678 | -51.3159 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| a3dcdfe9-3d43-385c-b55b-d12bec63552b | -12.99661 | -51.27256 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f48a0cd5-4ecf-3d75-9c4a-2157329abb19 | -12.99655 | -51.28448 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 01f42db1-7f48-3d17-ad86-bb47c7535b4d | -12.9963 | -51.25322 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 093aa2b3-4363-3db8-a5de-a8314393dc1a | -12.99617 | -51.24125 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1f3fa180-47b3-3a12-91ab-6ab9233b45af | -12.99605 | -51.22208 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README51.md)
