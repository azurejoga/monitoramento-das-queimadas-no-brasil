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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac274a73-bff3-30c0-ae4c-e1abfad47f22 | -5.05946 | -50.4536 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e39575c1-5152-3e35-a977-ef9cab45aa4a | -5.05581 | -50.453 | 2024-10-24 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d93f3ed-6242-3ed0-90aa-da3675ddf8b9 | -4.98656 | -50.88462 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5082077-bf9f-398e-8585-291f58cf7c86 | -6.81764 | -50.86232 | 2024-10-24 04:55:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94ca3226-9675-3855-874f-ffee1d5a121f | -6.80906 | -50.86974 | 2024-10-24 04:55:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b47567a-f499-3e62-9450-179324e834c1 | -6.80879 | -50.92162 | 2024-10-24 04:55:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cd31dd4-9df4-3a86-a14f-06dd3803e886 | -6.79802 | -50.8937 | 2024-10-24 04:55:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9eef9ea-7d04-3b96-b630-3b64204abb3e | -6.7974 | -50.89789 | 2024-10-24 04:55:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46ee01ab-6a61-3b91-b438-6b117dc593bb | -6.79314 | -50.90144 | 2024-10-24 04:55:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abb38c96-6e66-32c0-a23c-b25755d460c8 | -6.67608 | -50.41463 | 2024-10-24 04:55:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff9eae93-d68c-30fa-93de-ec9ec1796380 | 0.837 | -51.15147 | 2024-10-24 04:55:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4688d997-6db1-3374-8ccf-32e42c5d93c0 | 0.00235 | -51.22046 | 2024-10-24 04:55:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2266ca5-6089-3a9b-a4bd-ec64745d364a | -2.22772 | -50.71497 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4df4e70d-15b7-36f4-89ae-a1d6be8c71d3 | -2.20408 | -50.63574 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d664304f-269c-3b96-9261-d0562fffb728 | -2.20348 | -50.63964 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03f6d108-fd04-362b-a144-273816e982d0 | -2.19678 | -50.70622 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59bcaa28-f27a-3c15-8a66-d7b42b75b98d | -2.19327 | -50.70567 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 703e1d98-e73d-364a-b0f1-85b8cdfefa9e | -2.18758 | -50.5096 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e49c9681-d449-370e-9962-67936251f205 | -2.18405 | -50.50908 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 255460dc-455c-3699-a38c-baf0892ddc86 | -2.17035 | -50.52714 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39f66481-4e5c-3c09-80a7-5965aa2827f7 | -2.16973 | -50.53107 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 928dc0eb-f548-3a7d-bcc7-ab0c6538d443 | -2.16232 | -50.69693 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b699d7a-23c2-397c-a004-b45b38963bae | -2.16172 | -50.70081 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf724b14-90a6-3422-a3a2-34520c835c82 | -2.16149 | -50.69762 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 354ca4c6-2c4c-354c-9a1c-17bb5f698452 | -2.14136 | -50.99519 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 136149a3-ae92-308b-bb29-aec1ed4a6acc | -2.13325 | -50.83116 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 251d33af-43eb-33d4-adee-b5e0db74393e | -1.84038 | -50.65435 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab96e403-6c75-3aff-88b0-6a77437050bd | -1.83749 | -50.64994 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f543d0fe-0c37-3ad9-b07d-ee71b84ebcc9 | -3.34877 | -51.64782 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2419447-baed-3ceb-a459-4a90299b3401 | -3.3482 | -51.6515 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dce5536-4c28-356c-a24f-ed3cd5e65134 | -3.34535 | -51.64729 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a453985-587c-373a-aca9-dadbd5ca2818 | -3.34478 | -51.65097 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 574657d9-7f35-3dc4-b446-5489c5b5d8da | -3.26733 | -50.77391 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c82513c9-2aa5-3686-a83e-03a8aae070ce | -3.24179 | -50.84626 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31117b55-01c0-3af4-ab5a-c6a312966eea | -3.24119 | -50.85017 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfef2a33-9329-3317-8eda-20242f4c3a0d | -3.23767 | -50.84964 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76393083-43aa-3769-9b7b-5a3b6f1d74af | -3.2123 | -51.20024 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0411751a-7521-3665-b3d8-f6ef23c50621 | -3.19426 | -51.27097 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f96a7b9-0a5f-3473-b694-8c22c1da72d5 | -3.18395 | -51.22296 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f351adaa-a1c5-3865-9e08-9b2004f965d4 | -3.17295 | -51.24839 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9af6c0a1-f18e-32f7-8c05-502619d7d578 | -3.08019 | -51.2618 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cccde50-6ede-3566-8bdd-da51bd1e7d9c | -2.28684 | -51.14002 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a5f9ebe-e8ad-3133-a761-52f901fe57dc | -2.27803 | -50.55487 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2a68e82-2283-3b29-acbf-6e483e39c93a | -2.26708 | -51.89005 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d1dbd3b-241f-3cd5-9418-ec25e6453563 | -2.22081 | -51.67059 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3bd6e9a-a3c5-3e68-a781-33d74023f56d | -2.22024 | -51.67419 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd598a84-df16-3af4-bf5c-b6e69c894ae3 | -2.21849 | -51.07955 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a5bc48c-a579-3d95-a29e-b01a20911877 | -2.21504 | -51.07902 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e17040c0-d9cd-37b8-9053-3c72e1cb8067 | -2.95668 | -51.45327 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95fd0eb8-79ae-3238-bc1a-acb66c2aba93 | -2.95325 | -51.45272 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6cb64d8-8f21-3ded-8fc3-e6bc50af64aa | -2.95268 | -51.45642 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ceac2c43-0abc-33d4-b413-4aad6c05ad03 | -2.87727 | -51.31225 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c9e69f9-0277-3235-bcc4-1d68602854e2 | -2.87383 | -51.31171 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 971f8ba5-ae18-370d-a51d-953594c1ea3f | -2.86429 | -51.59752 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89ebf075-54ed-3fb3-b699-20d755252b00 | -2.86146 | -51.59333 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 880c1e5c-8fcc-35df-a662-d1a27b6fe77b | -2.86088 | -51.59699 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e48a115-7fc2-3928-a199-b694567f07ab | -2.86031 | -51.60064 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 039ffa37-e1b3-3e7e-8e0a-5a513c09a00a | -2.8569 | -51.60011 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c76e6e83-9f7e-3617-8e52-f2ab678f7a0a | -2.81241 | -51.35186 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1865dc50-c292-314d-ab7c-3442f1832dae | -2.81182 | -51.35558 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41965854-ad8c-3309-8cbf-d034ceb5c47f | -2.80122 | -51.59896 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dc4cc94-e9f5-3f72-aef4-84cbb8d43883 | -2.79691 | -51.36088 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd009b34-70d9-3108-af73-42d4dc7094ac | -2.79633 | -51.36459 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfe8fa2b-61fa-3ffa-b273-b660face804e | -2.79348 | -51.36035 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae13ac49-7a8a-34c5-8edc-49e9c0c66d70 | -2.79289 | -51.36406 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ae2b4de-cb5a-3507-85c0-8bd49df527a4 | -2.79231 | -51.36777 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d762cd20-b958-39bc-8b4c-d814e11a53b6 | -2.78946 | -51.36353 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa8ea1f9-d9fd-3e90-9ad4-c1ffedded8bd | -2.60637 | -51.77328 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de125596-8cce-38cf-a875-0d85d9894bae | -2.60299 | -51.77277 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 658f8dc1-6529-381f-830b-2059f049fb03 | -2.60242 | -51.77636 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1829f383-338b-3807-a926-e8814a39918a | -2.59904 | -51.77584 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bd2cfb5-5f5e-3cca-bb16-23f0bd178d9a | -2.58672 | -51.92077 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b752a201-6469-33a5-b300-4b33785981f5 | -2.58335 | -51.92024 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ea8a021-5022-317d-82d7-1c348020c8c8 | -2.41203 | -50.48121 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32695850-02d2-3b41-92e6-f99633428bca | -2.41161 | -50.4799 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd71373c-df79-3b71-99e5-f2346a9b28a9 | -3.62038 | -51.15078 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5514da3-ee75-37d2-bb30-8e9bc5024c18 | -3.56868 | -51.24519 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0cb55c6-4fdf-35ab-8593-937ae048a200 | -3.56174 | -51.2441 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e66fd05c-9231-3c23-8c3a-676a728b7965 | -3.56115 | -51.24789 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c06b39e-c2a7-3d0b-95d3-a29cccb954db | -3.49253 | -51.59771 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 574c8eb2-75d9-311b-a85c-33dabcf590fe | -3.47305 | -51.2119 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 206f2738-bcee-3467-97fc-74859c730592 | -3.46283 | -51.63089 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f6e0e62-5180-3e6a-8fe6-01784ead336d | -3.45198 | -51.58771 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7c981e67-31ad-3670-905c-4572e87e7575 | -3.44855 | -51.58718 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cabeed3-6253-3db3-977e-59a74cf838d6 | -3.49666 | -52.08914 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 961982d9-7f6c-3ef3-9f3b-dc158e518889 | -3.46969 | -52.10706 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97066142-554c-30f5-be64-c28df96f7477 | -4.64481 | -50.92684 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9999bc62-f1d4-32c8-81a0-4db027e7bfb8 | -4.64308 | -50.91423 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 942cf4d1-d483-318f-ba89-76fba18d80a3 | -4.63954 | -50.91361 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1acb545-85af-36e0-8185-217acd55b355 | -4.61281 | -50.92184 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87c39059-c4da-3996-b760-45718103161a | -4.61102 | -50.91883 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a74de5f8-9058-3fdf-8d5f-abbcdde33b85 | -4.6104 | -50.92282 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b0a4feb-5bf3-3edc-8bcb-036bc1288367 | -4.57223 | -50.9579 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bc85a6b-2729-30a6-b34b-17bbad11e7c7 | -4.10683 | -51.03221 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f600738-a2f4-3b3c-977b-a42e334321bc | -4.10332 | -51.03159 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f660255-3680-344a-aa4c-40a6018b32bf | -3.82224 | -51.38349 | 2024-10-24 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e48502f-1067-3c21-b3bc-17aca25be366 | -3.97691 | -52.16255 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92f99216-ea13-31f0-b954-80b8f3e6b411 | -3.88953 | -52.12334 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0954f0e9-e41c-3b6a-a442-2cec5ddf3ebf | -3.88898 | -52.12694 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96b49bc6-dd29-3630-9971-d85b87398da0 | -3.88842 | -52.12346 | 2024-10-24 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README67.md)
