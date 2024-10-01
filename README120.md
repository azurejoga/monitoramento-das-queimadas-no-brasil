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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 324a5c42-efcf-3e5e-be6a-09d2b2400fe4 | -16.73439 | -57.36018 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 73b768fb-0341-301e-b6df-9b6db0f405af | -16.73384 | -57.36381 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 79aa814f-6caa-3ad2-b21c-fc73a02d97cf | -16.73215 | -57.41924 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f1f67816-326e-353f-bb83-36d867ab9b66 | -16.7299 | -57.47821 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3cf1956e-63e0-3261-94a3-1b15b93dee4d | -16.72767 | -57.49267 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3bdc74f6-e2a5-3644-825a-a270042477f9 | -16.71944 | -57.36886 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7a5a6802-d886-3cfb-8df1-7bdeafca37a6 | -16.71889 | -57.37248 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3bc8993c-9f51-3bab-8f80-d954aee1228a | -16.71824 | -57.53185 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 59324b65-1c34-373e-9455-89e9ea159fab | -16.71774 | -57.46878 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cb6f1c19-54a8-321f-abd0-a05fdc9fab66 | -16.71718 | -57.4724 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9e9b7346-680c-39fe-b01e-5a67cf742f86 | -16.71556 | -57.37194 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| b572373a-705d-37a7-88b0-cdce9892fa23 | -16.71224 | -57.37139 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| d8bc13ef-c174-3a73-9cd2-e3b7e523d058 | -16.71169 | -57.37502 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 46b3e4cd-bd3b-314f-a3ea-82777b81b117 | -16.71113 | -57.37864 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 27bb9d76-4521-3c8d-aa06-7e905800f2c8 | -16.71055 | -57.4713 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d42cc6cc-9eb0-3d0a-84c3-343d9b1127d4 | -16.70615 | -57.38896 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| fa436044-4149-3b99-851a-6e0c936c1b70 | -16.70393 | -57.38116 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 7cba3570-91f0-32b8-acd7-922214484cad | -16.70338 | -57.38479 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c2dca916-2630-3ea3-a3ea-115285fbd9d1 | -16.70283 | -57.38841 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f6f21516-b4da-37e1-b734-20f20401af2b | -16.70061 | -57.4029 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dcd963e8-3f33-3b87-8018-76cc7f5e77bd | -16.70006 | -57.38424 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 27cf0c4d-9266-3736-956f-d538f8915966 | -16.69895 | -57.39148 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1adebbc9-e7a1-3fe4-8774-dd476fcff209 | -16.68898 | -57.47886 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b409f2f4-5020-33a7-8702-b2323dba8a6f | -17.06705 | -56.71249 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7102de71-ec66-3a87-8664-db11ceb2c9fc | -17.06649 | -56.71624 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3b326c4b-d009-37df-b8e5-cc5f086acf0d | -17.06593 | -56.71998 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6f45211d-76d6-3558-9b62-1930a5150762 | -17.06537 | -56.72372 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a3ee6197-7b70-3922-8fc9-84a283b4982a | -17.06481 | -56.72747 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1daf43a5-f419-34b2-bd18-035a886d7c76 | -17.06425 | -56.7542 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| daeee5cf-dc29-30b0-976d-117de3275c7a | -17.06425 | -56.73121 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4d0dc8bd-ed8f-3d35-affb-6ea4e234e0c6 | -17.06369 | -56.75793 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| eeb6f714-11b2-3615-ada1-d2b69af06b26 | -17.06368 | -56.71194 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fe89902b-b02f-3954-ad5b-1342aa0c32d8 | -17.06312 | -56.76168 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9cc9e68c-ae95-345b-bd71-e9254f6c1c3c | -17.06312 | -56.71569 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d0b0d860-491a-3c9d-82d0-5f078f07e275 | -17.06256 | -56.71943 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 58e9dbbe-17a2-3662-a14f-1139ed321dae | -17.062 | -56.76915 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f4411437-72a5-3265-b8ee-384eb16d1aa2 | -17.062 | -56.72318 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bf62d2c0-9507-37f5-88ec-022b4aa41dc6 | -17.06144 | -56.72692 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 744af688-0d92-34cc-a0b2-d73b71393422 | -17.06087 | -56.73067 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2fb1a983-4722-37b4-899c-9e620d866e8c | -17.06031 | -56.7114 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4083ba5e-04bc-3c92-8a87-4e5b27929ec2 | -17.05975 | -56.71515 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f6a8292c-eb79-3912-8692-d0ade83e022a | -17.0592 | -56.76487 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| c01c1c08-2053-3281-8e69-e644fb2fcb02 | -17.05919 | -56.71889 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 830eb954-95da-3e60-b6e2-98f613bc8d81 | -17.05863 | -56.72263 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c5502fe3-344e-3844-bf1b-646be563d576 | -17.05807 | -56.72638 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5ef9a97c-06e2-3f1f-9421-92b0a0fdb446 | -17.05694 | -56.71085 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| cfb1a053-fc4a-37b5-91d4-58b14674310a | -17.05638 | -56.7146 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0b345c7b-7930-31df-93e1-b657ba79db6a | -17.05583 | -56.76432 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 45155bd4-3174-3d1f-8c96-903c2b31954e | -17.05581 | -56.71834 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b467a8cd-a311-37f3-b631-86fb9a92fae0 | -17.05526 | -56.72209 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 09ac6bd3-7c70-3b23-b87d-1f992a4a2664 | -17.05469 | -56.72583 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 21d9252b-d29c-3cab-943d-c74005b80285 | -17.05413 | -56.72957 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cb66ce39-89e4-37cf-bfb4-c43ceb96e5ca | -17.05356 | -56.7103 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e67e69c4-1549-3790-88fd-0a33d45ac410 | -17.05302 | -56.76004 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 84ad1e87-799a-346e-befa-1d8075ea6979 | -17.053 | -56.71405 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0b47ac93-18a8-3bc9-bda3-b7134981fd86 | -17.05244 | -56.7178 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e1648d54-d38b-3674-8dfd-c594b759af50 | -17.05188 | -56.72154 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 5580074c-7a05-3091-9dde-789b3610a859 | -17.05132 | -56.72528 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ec89051a-ed64-362b-bd78-f1b83c2100c1 | -17.05021 | -56.75575 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 51fe8e65-dc37-3434-90a4-2ac5b9ee3dfa | -17.04908 | -56.74025 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9f930d63-a003-314b-8c4c-5ffcf86301f1 | -17.04852 | -56.74399 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 55fbd1bb-138f-3f13-a300-0950702914d9 | -17.04795 | -56.72474 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e150f7f6-937e-3ead-a9c1-ff42c13579ab | -17.0474 | -56.75147 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| df6a1783-9c92-302e-998c-f0a769f30fff | -17.04739 | -56.72848 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 985f52d0-002a-349b-8d43-0cdc95b124b3 | -17.04627 | -56.73597 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e150e1e3-6fd7-3af9-8592-7f5e3bcdb069 | -17.04571 | -56.73971 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0fe906fd-beff-335d-9254-c9076e1c409e | -17.04458 | -56.72419 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 33772fe6-6811-3232-b75d-ec8b7b46611f | -17.04402 | -56.72794 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d8574b71-ea27-3543-89e3-31cf3dd8eb19 | -17.04346 | -56.73168 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c68bdee5-f5f4-3cac-b5b1-66bc63d73170 | -17.0429 | -56.73542 | 2024-10-01 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b6468153-4415-3d38-860a-2f6efa458e84 | -17.00159 | -57.9627 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 455477bb-98d4-371b-9610-aed69630ea03 | -16.99717 | -57.96933 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2a5a59f2-f15c-3c18-b4a8-3d3de910f840 | -16.99661 | -57.97292 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8a51bb69-f1fe-3682-894b-ba84bd4c5c7e | -16.99605 | -57.97651 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0413e6bf-a87b-3853-88bb-b2af9168e7b4 | -16.99442 | -57.96518 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d8e555fa-38a6-3135-b1d5-741e572a0b2f | -16.99112 | -57.96463 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a8759989-c8a3-3fe6-9f1b-d2d0dca4684a | -16.99056 | -57.96822 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2ea7715d-9841-3c88-9c6d-fc4024250385 | -16.98781 | -57.96407 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1a2600cb-e669-3081-b653-e8d1d02680a1 | -16.98725 | -57.96766 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| abbf68e3-48aa-30e0-9063-e58c1e03d22a | -16.98557 | -57.97844 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ec8f6b28-fb99-384b-82fd-065478ee2d5a | -16.98227 | -57.97787 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| da6d542f-a30d-30ac-87fb-6dbbd48d2021 | -16.96965 | -57.94996 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 82ba3886-88c7-3034-a2d5-d4816ad9e274 | -16.96909 | -57.95355 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 988121b8-fa31-3e8f-a6a3-68980dec64bf | -16.96634 | -57.94941 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cd02488c-3bce-3518-9231-624bddafe4c6 | -16.96579 | -57.953 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1414d4c3-84df-3092-a85c-a324949801c5 | -16.96563 | -58.01929 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 679ffe78-5892-343f-ab6a-641f7bcb8586 | -16.96523 | -57.95659 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7a8b0754-5f3c-3265-951e-f4b32c9e321e | -16.9636 | -57.94526 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a9e3cbad-b82a-37f4-9d1c-b1c6f2cb5f6a | -16.96304 | -57.94885 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 881396ca-bdaf-3c62-b942-8c38d4e42df8 | -16.96248 | -57.95244 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f395b88a-5815-3a87-823b-72c8978f90d0 | -16.95973 | -57.9483 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 36f6ecb6-8e46-34de-bb1c-de46495d28d5 | -16.95917 | -57.95189 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c3e74d24-6d62-3537-9ecc-44f97d96c2fa | -16.95643 | -57.94774 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2e478f75-5edc-387c-a46e-95a1929d1004 | -16.8617 | -57.76999 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6d88834e-ec7e-3402-816b-70771345565b | -16.86114 | -57.77359 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5fde01c7-b3e9-3507-af65-941523adceb3 | -16.85452 | -57.77249 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9643a30a-af3f-3cf3-b1ab-b68728fa9626 | -16.83469 | -57.74704 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 56745e2c-e450-398a-80c8-bb23c2ef7ef0 | -16.83464 | -57.7913 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9a476372-5641-30d8-9453-30520e4cd441 | -16.83192 | -57.76502 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 0d69f513-a181-3134-8c70-4102466463b6 | -16.83136 | -57.76861 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |


[Clique aqui para ver as próximas entradas](README121.md)
