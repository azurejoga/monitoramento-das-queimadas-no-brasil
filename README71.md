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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f682bc4e-c275-3cd8-9bc5-3c524e7fb7ec | -8.28279 | -55.37474 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 622f73fb-36dc-3bb2-9ec2-9c05c834d44c | -8.2825 | -55.38753 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37e50d1c-69d6-37f0-923f-d835bf9f677a | -8.28059 | -55.38727 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc6857d7-cfb0-3975-b124-bb11a98d3ba0 | -8.27764 | -55.37384 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd65fdae-7073-3fa2-b78c-7c5b1909a095 | -8.27709 | -55.37696 | 2024-10-11 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f3b149a-c5fe-319a-84b3-70d4754f4d30 | -9.58461 | -56.4848 | 2024-10-11 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db36921d-62b4-3a9b-b3e5-817cbcf1a73d | -9.58048 | -56.47681 | 2024-10-11 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7753d3d-56c9-3ad5-8ea1-4bad475cda0d | -9.39753 | -56.29578 | 2024-10-11 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 604aadc6-437c-3777-9f77-59d288044a0b | -9.39692 | -56.29912 | 2024-10-11 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b60c2a-8cb5-33b0-a002-6d2c765f0041 | -9.39632 | -56.30245 | 2024-10-11 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 525c52c1-9b5d-3044-9085-784b33dff523 | -10.63051 | -55.88242 | 2024-10-11 04:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41c1a6f8-f004-3327-beaf-91a5f283ed6a | -9.96281 | -55.33492 | 2024-10-11 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 663efd63-3d80-3e28-8d9f-66a3972942f9 | -9.95783 | -55.33402 | 2024-10-11 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8cafb08-4b02-3448-8e8f-938d13713435 | -10.48467 | -55.61216 | 2024-10-11 04:25:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b123602-2860-380e-8358-917605ecfa4d | -6.5583 | -56.02144 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 706fc42c-69d6-3254-9d52-9ac20290ba1b | -6.55779 | -56.02059 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2801182-3869-3d06-915d-e528037f9010 | -6.55767 | -56.02509 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c75f0afd-4053-367a-b3f0-b439e363f318 | -6.55713 | -56.02422 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4d0bc7f-b2af-33bd-a2c0-56212d12bc92 | -6.55704 | -56.02873 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d914a82-ba8c-3160-9b33-fcada08b7404 | -6.55648 | -56.02785 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9dd0211-efc9-3633-bfd0-72ac1d4a4473 | -6.55217 | -56.02394 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c5a1efd-777b-3f2d-a9ae-d2557453991d | -6.55163 | -56.02311 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 963011e2-a3bd-3b99-82bf-3a0da804ec3e | -6.54665 | -56.0229 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e0248e0-56ca-386a-b58e-63f6ab49ddce | -6.54611 | -56.0221 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c79a7e66-8f25-3cb0-9119-a7d930f898c6 | -6.48562 | -56.04544 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b967cc43-3343-3c48-b43f-392abc074628 | -6.47941 | -56.04821 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 079a71ae-cd96-3eb5-9f99-5e44e812aea9 | -6.47877 | -56.05183 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b70d931-0da0-3ebf-a948-e23d916b9b07 | -6.47812 | -56.05546 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3643181-f0aa-3766-8f8c-674dcf24dd16 | -6.47258 | -56.05447 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12b29db6-9247-3436-99d7-0aa1b5a1c165 | -6.47244 | -56.0233 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76c28a02-c1ec-3cfb-8224-9796729f5fd8 | -6.47181 | -56.02684 | 2024-10-11 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd21bc9c-13f8-38b4-942d-d9406d178ef1 | -9.26896 | -56.90418 | 2024-10-11 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e976893-1513-392a-ae7e-e2cccffe95fc | -9.95574 | -58.10283 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18c70b88-98f8-3b2b-accb-7291e6c12fcc | -9.9549 | -58.1073 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c43b225-58a3-3b50-bda0-0031f90a8bc8 | -9.95407 | -58.11172 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a71184-6011-3436-a8d6-fd508ade436e | -9.95324 | -58.11615 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1213944d-0b74-32ec-9813-9b27229ff3dd | -9.95227 | -58.1035 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 390d9e9a-4b94-3393-8fb2-e0fecb18c122 | -9.95141 | -58.10792 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0165dc5-80f5-33cb-97d1-fecad89f1be0 | -9.95055 | -58.11231 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06067c95-2909-3932-83f1-9dce0f603188 | -9.94968 | -58.11679 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87b69826-d11f-3a48-90e7-a1de92218ed1 | -9.94895 | -58.10612 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b6b4018-b072-34bd-b4e7-06dd332876a0 | -9.94813 | -58.1105 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4db0050a-263a-3794-8067-1fcf91fbf9b5 | -9.94729 | -58.11498 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f750e12-e23b-3a8e-b161-626cc5d23cb4 | -9.94632 | -58.10235 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68c267bb-cb2c-3fc2-9e63-f318f2381ab6 | -9.94546 | -58.10676 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36edb0c5-9a45-3dab-a036-2c37ff46826a | -9.9446 | -58.11113 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5afbd20-a5ff-37ce-910b-f720980f73e5 | -9.94372 | -58.11564 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 256556a3-9a43-3933-972b-be8d6a1467cc | -9.94299 | -58.10497 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8028ef5-d2d1-308f-8f08-3e3053545ce3 | -9.94217 | -58.10936 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09b651cd-1803-3683-a2a7-74627c1120f2 | -9.94133 | -58.11381 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70b9a357-527f-313c-a1c8-7f272e6d3f49 | -9.9395 | -58.10562 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6902018-6235-3ef7-a0b6-464482e55bd0 | -9.93863 | -58.11003 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 556e881b-d554-3427-b86e-22bdda2b4406 | -9.93776 | -58.11451 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd04975e-48e9-30f4-9cec-98a5d57096e5 | -9.93704 | -58.10378 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70b0f885-5668-3c9b-97aa-803a4abcde0f | -9.9362 | -58.10823 | 2024-10-11 04:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 719ef165-4c95-3789-8ccb-9ef92cae40d4 | -9.90447 | -57.48136 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46dd8a3d-53f2-35d6-a723-730fdb1d2b93 | -9.90351 | -57.06639 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7709fa3c-03b2-360b-ad8a-a020ea9c93d2 | -9.89799 | -57.065 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d44dbecf-576e-3a83-989b-0a6af2481f0b | -9.89726 | -57.06889 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fe106b5-22e4-3df2-b364-3ffece0466fe | -9.79609 | -57.3895 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46dbe6b2-ceb1-33f3-a6bf-4ef08ba15d20 | -9.66112 | -56.96124 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 107a29a5-d5aa-3d28-b13a-358121376adf | -9.65698 | -56.95259 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f55c32be-94e5-3a5e-bad5-1eef4d68a187 | -9.65627 | -56.95638 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7559ccd0-fdcb-393d-b845-20c156e1f063 | -9.65554 | -56.96021 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ae3b3c0-5232-30b2-b7a8-abce9de7af8d | -9.65483 | -56.96401 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac626f84-5bc3-3070-b3d1-b8520212a385 | -9.65069 | -56.95533 | 2024-10-11 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3a11e3d-3c59-36b4-83de-1647805b0c82 | -10.3876 | -57.30149 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 90845a24-976f-3aad-8eb4-93fd1f7972cf | -10.33724 | -57.50584 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c624ec2-eb60-3985-a010-c9dd50268e4d | -10.33648 | -57.50982 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0c6d4aa-d6fd-3730-8467-2aeb65b0a1e8 | -10.33572 | -57.51384 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c5049a8-9158-33a8-b66a-b7b4e2c96e5f | -10.33152 | -57.50483 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ac39b13-bb79-3ad3-af78-df961d13fe66 | -10.33076 | -57.50885 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56a9086b-ab04-3d2f-9356-47b082679c60 | -10.33 | -57.51286 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78dc97a6-c91d-3b81-ace2-7a59cd75371c | -11.02917 | -57.21381 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b862940-2d5c-3213-a34e-e1c6fc669812 | -11.02847 | -57.21753 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb48aedb-7b4f-3008-abe1-02e86d298788 | -11.02776 | -57.22123 | 2024-10-11 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 118198a5-db48-337e-93a5-9629676de05b | -6.34865 | -58.17934 | 2024-10-11 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 273b0758-6c3f-3e41-b31a-b20b989ef3bd | -6.34772 | -58.18447 | 2024-10-11 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa549725-c4e3-399c-99a2-605cf471aec5 | -6.85742 | -59.09687 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21245615-794a-393d-b25d-4b09eeceb377 | -6.85078 | -59.09558 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f53cee2-7818-3e61-adf9-dbe1a0c3fcd2 | -6.79311 | -59.64234 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a21b66f-e130-37f6-83df-e85a8742d516 | -6.54992 | -60.03382 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 372ebd8a-5c9a-3aec-8a98-8b2d768a0b04 | -6.54863 | -60.04078 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2cd3030-57cc-3ec1-8266-eb911cb9ceac | -6.54698 | -60.03478 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4dc1d29f-a556-3067-9143-84c9dc2eeeea | -6.54565 | -60.04171 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 985d53fb-beae-31e4-a267-451f9424d07c | -6.54294 | -60.03212 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 025dcf90-3655-38c0-be0a-36ec5dcaac9a | -7.08677 | -59.41461 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a14e9ec5-2ab7-3c8d-88d0-653e2b821627 | -7.0856 | -59.409 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eebd4ff-8b23-3dda-8dfb-da014cf86c83 | -7.07887 | -59.40765 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e1d22e4-d91c-3f15-9afb-f5db538f32e6 | -7.07212 | -59.40638 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bc81d384-cab9-3a58-b342-405e2c0584ee | -7.06421 | -59.41131 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6202a601-772d-33c3-9260-31f46fe361a7 | -7.04105 | -59.37486 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ab1fcaf-c33c-3219-bc14-3d90c31e3a00 | -6.96552 | -59.48096 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f581e234-22d3-3e31-a3d7-5c52923da1bf | -6.79191 | -59.64867 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0fd5b46-1625-39b4-b32f-6ec725ad353d | -6.78266 | -59.31536 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be065263-7191-3f17-86d3-5850d851da15 | -6.78157 | -59.32127 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d200870d-31b1-3a67-b710-350e3434bb9e | -6.77485 | -59.31983 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d67eb85-c3e9-376a-a5f0-feea6b2b4044 | -6.76812 | -59.3185 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47497e64-edf6-3e09-8fda-68fa825c5ec8 | -6.76024 | -59.32336 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d82399af-1bf3-3117-8e55-65d70bf3fb65 | -6.75233 | -59.32829 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README72.md)
