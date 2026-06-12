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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ea1d9d2-a61b-3ef8-b802-34c1a7de1d23 | -12.4277 | -58.4642 | 2026-06-12 13:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 438.3 |
| 48678359-c208-3b2b-9bc1-921190bf8938 | -12.4277 | -58.4642 | 2026-06-12 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 331.2 |
| f08e13d7-a29e-33d4-a0fc-9a438462f1d2 | -12.4085 | -58.4855 | 2026-06-12 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 146.5 |
| dd78e26c-e33b-3ef3-86a3-72053ce00250 | -12.4274 | -58.484 | 2026-06-12 13:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 333.3 |
| 046fd97b-f08d-3532-a5d7-cb53cb57c7c1 | -8.1667 | -47.5421 | 2026-06-12 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 2bbb18b5-d1fd-33c3-806f-356c8e4e2b26 | -12.4085 | -58.4855 | 2026-06-12 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 142.4 |
| e4e750d5-f127-3f46-be79-b8fafa11fa19 | -12.4277 | -58.4642 | 2026-06-12 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 442.4 |
| 5719de18-9141-314e-86d0-9d7c90addc8e | -12.4277 | -58.4642 | 2026-06-12 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 325.8 |
| 68f942c5-f848-3f6e-bf20-3a124516a6d7 | -12.4085 | -58.4855 | 2026-06-12 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 92f0ae7f-aeb5-3e4a-abed-35ec4413e22f | -12.4085 | -58.4855 | 2026-06-12 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 51083dad-a39b-33c3-ba61-f4e79199c77d | -8.1667 | -47.5421 | 2026-06-12 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 3820c828-3d29-329b-875e-cc4b93db84ba | -12.4277 | -58.4642 | 2026-06-12 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 317.5 |
| 1e81cc6e-4213-333d-975c-4d928797dba1 | -12.4277 | -58.4642 | 2026-06-12 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 437.4 |
| 5072c002-4a6f-3405-a418-aea18efb5f32 | -12.4085 | -58.4855 | 2026-06-12 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 1b512b65-216f-3609-b9ab-9bb86957169f | -12.4085 | -58.4855 | 2026-06-12 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 177.0 |
| bef6f255-3e54-3b46-80b6-b1b7943cc757 | -12.4277 | -58.4642 | 2026-06-12 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 377.7 |
| 5a3887a2-9e04-379a-8e21-02e13424dcdd | -8.1667 | -47.5421 | 2026-06-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3e96c139-760c-39d8-a948-29149b9f6b03 | -12.4277 | -58.4642 | 2026-06-12 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 369.6 |
| ad1ea047-825b-3a48-9810-f8e9a95a09cf | -12.4085 | -58.4855 | 2026-06-12 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 207.3 |
| bad34fc8-350f-3730-ad13-de9a54a1607b | -6.9793 | -42.8798 | 2026-06-12 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 712bd0ea-8552-3dbd-a869-45497c2d3124 | -12.4277 | -58.4642 | 2026-06-12 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 333.0 |
| a5fb6005-4525-315b-adbe-ac62cd63045b | -12.4085 | -58.4855 | 2026-06-12 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 967815e1-8f16-3d8b-ac4e-119599e76738 | -8.1667 | -47.5421 | 2026-06-12 15:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8f78b337-efa8-3b17-bd30-20a9c0e3f9dd | -12.4085 | -58.4855 | 2026-06-12 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 3e412205-726a-3a1c-8eef-892be3c33d83 | -12.4277 | -58.4642 | 2026-06-12 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 268.6 |
| c8146d16-676d-363c-9a4a-107ea24ad677 | -12.4466 | -58.4627 | 2026-06-12 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2be5ffd9-ecab-3fe0-b707-148afabd6c71 | -12.4085 | -58.4855 | 2026-06-12 15:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| d88c398b-b711-3cee-9217-bdf38295ff41 | -12.4277 | -58.4642 | 2026-06-12 15:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 318.6 |
| e3b4d7f9-204b-3ba5-b8a8-de3ae48aa348 | -12.4277 | -58.4642 | 2026-06-12 15:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 232.7 |
| ea0235b4-f991-3bd3-96f9-ecd01515911c | -8.1667 | -47.5421 | 2026-06-12 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c5807ba5-98dd-349b-8e68-8f63f848b6e2 | -12.4085 | -58.4855 | 2026-06-12 15:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 151.2 |
| a22444ee-9c8b-3ee9-b968-c5a1c3c3392b | -12.4085 | -58.4855 | 2026-06-12 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 93a2a5cd-4a37-3409-afdd-60241aafa300 | -8.1667 | -47.5421 | 2026-06-12 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bb7d6d86-504f-3170-bb67-241d9a51372e | -12.4277 | -58.4642 | 2026-06-12 15:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 4e0506aa-270e-3250-a82a-d0676eb83f26 | -13.4687 | -55.7619 | 2026-06-12 15:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bbd27c46-9d3e-304a-b376-941e3cb5cafa | -12.4277 | -58.4642 | 2026-06-12 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 3f15bc03-9568-337b-b205-43dcfc813eb1 | -12.4085 | -58.4855 | 2026-06-12 15:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| db1f2b80-ab0d-3244-917f-0ccc89b71d51 | -8.1667 | -47.5421 | 2026-06-12 15:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| fefc1132-260c-32ea-9e57-57a782755b4b | -13.469 | -55.7415 | 2026-06-12 15:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| afdaf0ab-e099-353f-975a-c93de1bf30bc | -12.4085 | -58.4855 | 2026-06-12 15:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d7bd492a-2f3a-35b7-a6f7-4c37f1aa5bde | -12.4277 | -58.4642 | 2026-06-12 15:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 54cdb328-040e-3aee-9285-fea0fea204b5 | -13.4687 | -55.7619 | 2026-06-12 16:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8deb55e4-d93b-3eb7-894f-afc147548e2c | -12.4277 | -58.4642 | 2026-06-12 16:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 137.4 |
| d86f18e6-2fdd-3fb5-a966-866cb109ecdb | -9.1529 | -46.9143 | 2026-06-12 16:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |


