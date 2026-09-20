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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 642fa9f9-67c2-314c-b4f8-8309624e4a00 | -15.61508 | -49.84103 | 2026-09-20 04:42:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af8cc186-faab-33d5-9281-c0bb33d4c842 | -15.46521 | -48.44094 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41c5899a-1109-31f4-85d1-a98a5fe17d7d | -16.82791 | -47.63746 | 2026-09-20 04:42:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d073ca36-e17a-3b4f-b0d2-c93802f3bb09 | -14.69137 | -46.69731 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6d04b41c-5d62-3481-ae84-23ec3cb3d037 | -14.67326 | -46.69454 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c2ab4727-9577-3fe7-9baa-2c6e4662c733 | -14.79125 | -48.54601 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1631cf9-2636-34ca-b3f9-1464be65e8ca | -15.04856 | -48.60847 | 2026-09-20 04:42:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d4c426e-78c9-3792-bbf8-bce838d7a488 | -15.8759 | -49.91029 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d6837cd-9037-3aae-892c-1b5f79c9a1b2 | -14.6696 | -54.45868 | 2026-09-20 04:42:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9524afd5-d9ee-3a99-af10-1f14e9aaed1d | -18.1893 | -51.7817 | 2026-09-20 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ebe05f0-e076-3f6c-ba88-7bc38537219b | -14.68536 | -46.68761 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93af4973-9e4d-3e4e-9ccb-e8550a618f92 | -15.17164 | -48.16267 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53b4bb1f-7097-3fe1-bf12-0090414f1a62 | -14.68475 | -46.6919 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2120f77-7014-3fc4-b750-ad8af9be46aa | -16.88847 | -50.59451 | 2026-09-20 04:42:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3ad1ae9-6068-3754-b188-5ec30fff17b9 | -14.95928 | -47.53728 | 2026-09-20 04:42:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5486b2a-8c60-3e33-9c0b-3686a5331532 | -16.53729 | -49.10159 | 2026-09-20 04:42:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a86bc30-4324-36c9-af80-b6ea35501ebe | -16.59019 | -45.34169 | 2026-09-20 04:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1d57deaa-f0e0-31f4-963c-3c045949d0c6 | -15.47834 | -48.42727 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f28af57-1612-3a64-b065-2cee1a6c43a7 | -15.87703 | -49.90312 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58594819-8771-33ca-800f-2c7f1d6b07fd | -15.61564 | -49.83745 | 2026-09-20 04:42:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e027cab-31b3-360d-a950-0a354b58fa12 | -18.67743 | -47.05318 | 2026-09-20 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d050b051-5954-3281-a085-4e2fc3077370 | -16.59468 | -45.33865 | 2026-09-20 04:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66a1e2c0-1a1c-390c-8f78-c4dfe522f36f | -15.86595 | -49.90866 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25e4f6e0-cb76-3255-9917-831ca8aaa473 | -14.04648 | -52.08602 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7cd01aee-b0ea-334d-a664-ec20a326b76c | -17.57799 | -45.3846 | 2026-09-20 04:42:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f125ece-b9a4-38ba-ae12-54d0715bc1b2 | -14.05208 | -52.09503 | 2026-09-20 04:42:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d0dc29e-5b10-30ae-83b7-4a928b9149e6 | -14.69499 | -46.69787 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2262d0a-d075-3768-9ab6-f50a21672475 | -14.67087 | -46.6854 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7ba4a05-a11c-34e6-b728-6ed1193446c8 | -19.87708 | -49.00548 | 2026-09-20 04:42:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e370fff8-eee1-3eb8-ae09-7caf2673cf3f | -14.67449 | -46.68595 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4aa57330-af18-3067-9251-894d5c436f5a | -16.0945 | -49.6398 | 2026-09-20 04:42:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32356a55-5d6d-3440-9eec-08003697935a | -14.69437 | -46.70218 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f276d0b-797e-315c-9d7a-7df1c0deaa85 | -15.86983 | -49.90562 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a640f115-363e-3bbd-a716-70dd9a828465 | -16.59066 | -45.33808 | 2026-09-20 04:42:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a8451d7-d4bb-316d-88de-24c14750a5a4 | -15.3482 | -48.1038 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e23f98e-91e7-3af0-ba4f-e4de90229045 | -15.61895 | -49.83801 | 2026-09-20 04:42:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3354b5a0-7351-3ae4-b706-5c5573d8bf02 | -20.26482 | -45.56055 | 2026-09-20 04:42:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a3b0102-6b63-3383-8be2-aba9d344c68f | -14.80055 | -48.53968 | 2026-09-20 04:42:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b574f891-dd9c-34ba-81b2-ca089bbfb2a2 | -14.68775 | -46.69675 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e6b32a7a-52cf-3af4-b323-c09b708d1883 | -14.67689 | -46.6951 | 2026-09-20 04:42:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b40bf8e7-e592-3587-bf2d-883c4acbfddd | -15.87258 | -49.90975 | 2026-09-20 04:42:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a154f5db-5b0d-30c6-b9df-697c43d3d6f2 | -17.03856 | -47.28289 | 2026-09-20 04:42:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908ef2d9-754b-3ab4-9ac4-c2475e9cd13a | -17.03735 | -47.29889 | 2026-09-20 04:42:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4151db28-5e51-3361-8be1-55f2ac44f22a | -15.46464 | -48.44467 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98f2b02a-7555-3446-8052-15c0831ecd79 | -14.91689 | -49.91949 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80952a72-08a3-32bf-97e0-450682ad3085 | -14.91801 | -49.91236 | 2026-09-20 04:42:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cde58ec9-7c7a-3994-934c-996f801d5b44 | -15.4698 | -48.41448 | 2026-09-20 04:42:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f0dc60c-03f5-3857-b8ea-eb09fd8529ba | -17.8328 | -44.84791 | 2026-09-20 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e24a139-0ff5-30cd-8e48-4a46a0923c46 | -15.04799 | -48.61217 | 2026-09-20 04:42:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad87728d-57c0-3be9-a54e-88f12657c700 | -21.28105 | -56.1367 | 2026-09-20 04:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0682d20a-c9e2-3168-86d7-9cb28bec073a | 4.53183 | -60.87384 | 2026-09-20 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1e423d41-cc1a-33c9-b41a-cae762f2ef30 | 4.53527 | -60.87296 | 2026-09-20 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6c9f148-4323-397c-8ac7-47b917dd6e4a | 3.6466 | -51.81121 | 2026-09-20 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bda7f95d-ca85-3bb8-bab8-35e080571675 | -3.84683 | -51.33862 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78ef3686-68ff-3c84-9115-625d0d161364 | -9.28012 | -48.2418 | 2026-09-20 05:23:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1973e0ee-2315-39e2-8828-f4685fbb92fa | -7.8668 | -62.5376 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93f9baed-f66d-30a3-bfd5-1113b32b0455 | -10.77821 | -50.88108 | 2026-09-20 05:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 10c1d845-c28e-3ee0-89f5-f408bb201f96 | -8.80196 | -60.78994 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dd8445e-3c6e-38a1-b43d-d7f865929201 | -8.22137 | -62.84798 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e904aca9-0f7f-30aa-938a-89270cf3cbfc | -1.63999 | -55.1538 | 2026-09-20 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a39121b-f5f8-3011-86db-41caf25d4852 | -3.37685 | -57.96274 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45265843-8b30-3073-8663-0aa8d62f5897 | -2.98379 | -54.7664 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f917e9cf-5107-3702-aa87-8950190f1622 | -11.09039 | -48.30572 | 2026-09-20 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9b19a9ca-761c-3b25-93ce-5b09f53b4af1 | -2.91838 | -57.79487 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 24f93288-4aad-3664-9ee1-c0b3475af23f | -9.67627 | -53.58828 | 2026-09-20 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9764b0de-8c27-30f0-9074-c9a0bd89ecc9 | -2.91725 | -57.82545 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe42d324-5c18-39f5-a152-c8a571d8bb7b | -1.82574 | -55.33114 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8f5d0dd-098e-3662-ac01-9c729d4e4463 | -8.46547 | -57.62344 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ed7ff1f-6bcf-32fd-9d43-f34b8401f1fb | -3.0043 | -54.16979 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9685cda-bfce-3fae-8d27-7b537d8d36ce | -8.25627 | -61.36805 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a8885ca-e06b-362a-83c5-93ed46d601f2 | -3.3746 | -50.44337 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bc9c79e-a9ca-358a-a862-2c1604f574a9 | -3.22015 | -60.04972 | 2026-09-20 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ded243-cce3-3cb9-af26-8a6dc3bc583c | -10.46533 | -51.27531 | 2026-09-20 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a162aa34-12cf-39e5-a64e-e263ba57251b | -2.82326 | -50.47414 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41eaa23-b8b2-3f57-a865-b0ba9efaa9b4 | -2.61041 | -54.75806 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26ae6260-33c2-3b4d-a18b-06037f0934c8 | -10.31289 | -50.22047 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e906aea-cd80-3b8d-b51a-f548dc3fa0a2 | -9.06827 | -61.37344 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b772061b-6326-3838-9a6f-fe2da38ff124 | 4.35502 | -60.3201 | 2026-09-20 05:23:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fed8b1e6-4238-3622-b8e0-e210394f72de | -8.46482 | -57.62782 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0728d360-9cb5-3075-9f4e-538e17bf92ae | -6.79584 | -58.79142 | 2026-09-20 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc8374f-d3ca-34e3-88ec-1c45d121ae26 | -6.7275 | -55.05791 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d7ae34a-337a-3419-8977-f20cb98d8256 | -6.32788 | -59.94543 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ac70e8c-2844-3504-8ba8-4c347212be42 | -1.2584 | -55.76301 | 2026-09-20 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a006d01d-7496-357c-b08c-c6173818cca0 | -6.43871 | -59.97669 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db0bbbd5-36cd-385c-a7d2-5e8a0853e28d | -3.53903 | -58.69263 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 856ec0ad-3023-3dbb-b009-8c8f953cc89c | -2.71441 | -57.95886 | 2026-09-20 05:23:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82a40e62-3e77-3e7b-9536-bd06b43e9ace | -3.55515 | -50.28913 | 2026-09-20 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e273a7b-bfe7-3e35-94db-a71e6c2ba6b8 | -10.31526 | -50.25458 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 421e37dc-b3bd-3062-ad53-d031eb845bbc | -1.30105 | -61.37297 | 2026-09-20 05:23:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7ebe841-7267-38ac-889e-85d2b160fef7 | -10.60254 | -50.2525 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1c9866f-c820-3add-80bb-0610f27a6b69 | -9.03675 | -49.83723 | 2026-09-20 05:23:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e15f8eb-2a70-30a4-a297-b3fd33869d5b | -2.90995 | -59.20034 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68c3ddaa-71d8-3d9d-83f0-722260eab7bd | -3.38062 | -50.4406 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cbe49730-ebb5-3014-ae64-6263a489b0c3 | -8.79703 | -60.79988 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| ea10c5f6-781b-3f93-acfb-080cee140de0 | 0.79106 | -59.1998 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7045403c-0573-37b6-80a3-19ac9d10d970 | -3.33569 | -59.80744 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdab0603-357b-3799-85fd-f7792f556767 | -3.11569 | -61.40564 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e434e901-65ce-34ed-9ceb-2a33becc4a93 | -1.5112 | -49.46943 | 2026-09-20 05:23:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58107b53-f344-3af5-85bf-aaad64f05ab5 | -3.4523 | -50.60083 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3487473-23e5-327f-bda9-aaba07ebc901 | -3.13144 | -52.71795 | 2026-09-20 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README84.md)
