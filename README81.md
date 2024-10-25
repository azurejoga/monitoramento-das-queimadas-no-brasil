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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3670c36e-ea2e-398c-9fdd-0e28035c9d88 | -4.94678 | -45.54934 | 2024-10-25 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddc15490-767f-380a-9f4d-4794e91f0d47 | -4.94612 | -45.74156 | 2024-10-25 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff216641-c35c-3a16-8902-8394a1675cf9 | -4.94577 | -45.54139 | 2024-10-25 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5056f20-e454-363a-9cc8-f09ea1e1bd8b | -4.94562 | -45.74513 | 2024-10-25 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1e16afe-9d02-333e-8310-60adb8bd3c56 | -4.94521 | -45.54541 | 2024-10-25 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fbee16c-e641-356e-8411-505be18782f2 | -4.94469 | -45.54912 | 2024-10-25 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5ac4879-aa83-3855-a487-0ecbe98ab2cc | -4.54952 | -46.03778 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7cc14d1-eae1-3770-870f-d049b79e7f54 | -4.5477 | -46.03769 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4bac7d3-a964-3c8c-b229-687a879a33a4 | -4.54407 | -46.03719 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3697ec35-b91b-3deb-81e7-8c2e36bc9acb | -4.54359 | -46.04065 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c89d379d-041c-3ce4-bee0-8ed37b976fe4 | -4.54226 | -46.03706 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e024b3b-5cdc-3f87-9d6b-32948e5d4e6a | -4.54175 | -46.04051 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65ec229a-d201-3f5d-8ce8-3557041a11e8 | -4.53916 | -46.03279 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cfd6a80-5eff-3701-8da2-5db3d65ef783 | -4.53864 | -46.03649 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 857f4461-e035-3201-bd22-0815c11cc9f2 | -4.53683 | -46.03638 | 2024-10-25 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff50aa2-a2eb-3d0b-9d47-611b609cd5cd | -5.09133 | -45.82891 | 2024-10-25 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d473e57-c7ec-32e7-843d-781353698e2d | -5.09078 | -45.83271 | 2024-10-25 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52682ea9-b17f-36eb-8079-1a389045127f | -5.98296 | -45.36679 | 2024-10-25 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0c493bcc-ebdb-3db7-b890-13972dbfe7f2 | -5.98239 | -45.37087 | 2024-10-25 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 3880c444-15f5-3b6d-8ec6-c1a07af2c1d8 | -5.98183 | -45.37492 | 2024-10-25 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8f00e148-c977-325d-8f1f-9366117f13ec | -5.9772 | -45.36586 | 2024-10-25 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7437a34c-ced4-354f-96ad-de4fc3c434b0 | -5.97663 | -45.36992 | 2024-10-25 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 72d20951-1877-3cf2-a3f0-105b22cd3e85 | -5.97607 | -45.37397 | 2024-10-25 05:01:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 5dd14cf7-1cc6-34fc-bd59-69cccd0d5efa | -5.9032 | -45.56285 | 2024-10-25 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51399ed0-a51f-3119-b4ca-00e3535aabd8 | -5.70707 | -45.01049 | 2024-10-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e076e69b-c29e-3854-b0e3-75f4816756a3 | -5.70646 | -45.01487 | 2024-10-25 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2999a0fb-f41b-3d64-82bb-f460fc6e08c4 | -6.44254 | -46.0625 | 2024-10-25 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db4934a3-2a30-37a5-92db-6bce3c53fcbb | -6.44203 | -46.0661 | 2024-10-25 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b237408d-3c31-3980-a666-9e9d6419e5ed | -6.00808 | -45.951 | 2024-10-25 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0664365d-b93f-35a6-a195-9d66de6777e0 | -6.00754 | -45.95485 | 2024-10-25 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b8101f6-753f-39c6-8962-bac9378eea1c | -6.0025 | -45.95035 | 2024-10-25 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58ab2c39-1336-3455-b595-c939d3ade14e | -6.00143 | -45.95797 | 2024-10-25 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4faf1563-b02d-3f8d-be38-fdae95e3eb4c | -5.84367 | -46.23964 | 2024-10-25 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2b4d867-4446-3b82-bcca-4e6713739b43 | -5.83822 | -46.23892 | 2024-10-25 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1be5aeb4-1371-3b5e-a92f-d988bbdf0992 | -5.45978 | -46.35447 | 2024-10-25 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d2ee188-99b6-3e63-b961-0c5f67a0cca7 | -5.45929 | -46.35785 | 2024-10-25 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61699f03-8787-3739-bcf2-8cbde38c8f68 | -7.93924 | -45.69747 | 2024-10-25 05:01:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a68ff8a-842d-3309-9e9d-e0a28f346962 | -7.42872 | -46.65576 | 2024-10-25 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c8f71a-8bde-3869-ae3f-5f9574712e63 | -7.42378 | -46.65161 | 2024-10-25 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 266d7684-14c1-35c7-b9cf-54e0d538844d | -7.42328 | -46.65519 | 2024-10-25 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52cb4115-783c-3984-9d5a-509cc2db6108 | -7.38325 | -46.54218 | 2024-10-25 05:01:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67a34cab-e03c-3e2a-b315-0389377a0c68 | -7.21418 | -45.58733 | 2024-10-25 05:01:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 99dbf1d2-e756-34b2-89b6-e06c8c519bfe | -7.21363 | -45.59145 | 2024-10-25 05:01:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d809cef9-ec1b-3113-8b02-bece5526c4ee | -7.20839 | -45.58649 | 2024-10-25 05:01:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f325ef2d-1888-3159-8b12-eb3eed587e2f | -7.04716 | -46.32417 | 2024-10-25 05:01:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe9bd672-372f-3c7d-b813-d61c8cc497eb | -7.01568 | -46.4301 | 2024-10-25 05:01:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1b07a04-3a07-3e9c-9a5c-563ea6d45e18 | -7.01519 | -46.43368 | 2024-10-25 05:01:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 725cdc94-2078-315e-aaac-721b7c3f8ece | -7.01021 | -46.42931 | 2024-10-25 05:01:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e45c2e18-0442-33b6-9f4d-c176f6c1ceb5 | -7.00973 | -46.43286 | 2024-10-25 05:01:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73776938-c24f-3e01-8cf3-940bd4f0252e | -6.96206 | -46.33106 | 2024-10-25 05:01:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 192257d1-66f1-3d77-b43e-3d3604bb3c9f | -6.95656 | -46.33025 | 2024-10-25 05:01:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 111e61bb-96c7-335c-9466-852fc4286887 | -6.85225 | -45.8996 | 2024-10-25 05:01:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cd1f512-7395-3bfd-b629-35cce14832f3 | -6.84664 | -45.89847 | 2024-10-25 05:01:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71d920aa-ecb2-36ed-b351-4cc1b97015f1 | -6.77581 | -46.25325 | 2024-10-25 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50faff51-9c0f-3927-b9b6-eb7f0e454d47 | -2.57406 | -47.25267 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 950bc79c-95b9-3214-a0d8-95936beb513b | -2.57326 | -47.25796 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8937a938-6dd0-3201-987b-29f2a0c9788f | -2.56922 | -47.25193 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7da626de-c024-386c-a1c8-4517f9d28239 | -2.56842 | -47.25724 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53479387-7af6-3620-973b-48cbb93e68cb | -2.31202 | -46.64519 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4fc4de7-f36c-3b46-ad00-b4d193362e56 | -2.3118 | -46.64312 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc52c637-dffa-308d-a8fd-cb8d0279a2ca | -2.31156 | -46.64808 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71ab5528-c221-34f6-b27a-7eb8e8f78f4f | -2.31137 | -46.64603 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 467e9c48-222b-3ae7-8364-d03576669e87 | -2.31094 | -46.64893 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45bf27d4-6acc-3ed1-926b-be9cd3a2c9d2 | -2.30654 | -46.64735 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb012658-c644-36e4-bd61-ee004e2ee1cc | -2.30591 | -46.6482 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f10e72b3-9ac2-387e-ba96-83537f11d2c8 | -2.30151 | -46.64662 | 2024-10-25 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 770330d1-19b7-3dce-94e1-4637a6d1ff44 | -3.20995 | -46.80047 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ea46395a-18f7-3085-9ae2-da1858e1a0a2 | -3.20952 | -46.80338 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4d08473a-b98e-3235-9f77-b2888410d61c | -3.20908 | -46.80629 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7cf87a0d-0c62-3bca-934b-3700c770452f | -3.20492 | -46.79971 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e08c4b76-1e97-3254-b02e-36ab8f48e3a6 | -3.20448 | -46.80261 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0363f97a-ad1c-3dce-bfdc-4f2666b0fb9b | -3.20405 | -46.8055 | 2024-10-25 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e4d36826-d85c-3bd3-a6ad-a5cd535be42b | -3.54598 | -47.36224 | 2024-10-25 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c68db033-9a52-3b16-9c2a-d8b9b5294a86 | -4.77468 | -46.41885 | 2024-10-25 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 05933e22-a028-3d3e-9a46-e659d99d5747 | -4.77421 | -46.42211 | 2024-10-25 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05c7ad85-7d99-3d44-a1cf-c6736a213f72 | -4.76942 | -46.41785 | 2024-10-25 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10b31dae-bd5d-3834-ace3-5526f3dedf26 | -4.76895 | -46.42111 | 2024-10-25 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbc31541-6a20-30e5-82e6-ea1925ac0a41 | -4.76845 | -46.42452 | 2024-10-25 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fff6cb1-17a7-3697-ae72-655a9ad0ba9d | -4.43082 | -46.64311 | 2024-10-25 05:01:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 974c76e3-6ee7-3adf-8d37-12d8233145b6 | -4.18613 | -46.80996 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52ee2d15-a1e9-30b4-9e53-85405682d431 | -4.18109 | -46.80878 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eb73bb8-b5a1-345b-abab-4762107d96f3 | -4.14641 | -46.83178 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 50e109c0-42c6-3805-8acf-b2ed1b912036 | -4.146 | -46.83459 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| de9821a2-c3a8-31c0-ae7e-05c068edb1aa | -4.14559 | -46.83739 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| a743260e-aff6-333b-8ce9-54a15cd558df | -3.95295 | -46.43003 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bcba3e38-1510-3414-8e60-40455bb331c6 | -3.95256 | -46.42862 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37cf924d-ab24-3ea9-a73c-0cc2fe234204 | -3.95246 | -46.43344 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| c672cb58-a672-3869-930b-1ef64e76f1d7 | -3.95205 | -46.43198 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b018f047-8e20-33bd-9663-137a93127902 | -3.95198 | -46.43682 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e4012c0b-a865-389a-92c6-26cc8d91ef90 | -3.95192 | -46.39979 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6346b311-29e2-3e05-b750-ce5e0f8b480c | -3.95154 | -46.43536 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 0792e94b-d75a-3b64-9411-87797dea5fa0 | -3.95146 | -46.40303 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3dc272d-44e7-3066-8496-d84b6e426ab4 | -3.95128 | -46.40165 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b728fb5-1bde-3439-86cc-357de36af89c | -3.95106 | -46.43859 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 22ecf8eb-baaa-3224-8127-961d52e44f2c | -3.94812 | -46.42642 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c9f3261-db15-3756-9a16-5266d9fa9be3 | -3.94767 | -46.42963 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dbd633e1-1649-31e6-bb43-6a0b33d54f54 | -3.94727 | -46.42827 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 294a2458-fa21-336a-93ce-ec02e8391c2a | -3.9472 | -46.43292 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81eb0f1a-ed36-334d-b94c-8bc131dd154a | -3.94678 | -46.43152 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 865e16ab-2f71-3079-b0c9-941c008df567 | -3.94673 | -46.43618 | 2024-10-25 05:01:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README82.md)
