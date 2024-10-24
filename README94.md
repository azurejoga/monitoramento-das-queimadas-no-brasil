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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc7a287a-d7ee-38f5-8dc9-39fc6e7b787a | -3.40635 | -50.34182 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 259bf089-7c86-36ed-a0f0-5ea1645da033 | -3.4014 | -50.33734 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f07a9838-e032-3c6d-a04d-5461d1c4ab54 | -3.40086 | -50.34102 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 270cecc3-7e59-3008-b847-bf84badf42bf | -3.34906 | -50.15693 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0840b8fb-5aa1-3de0-be6e-729aefd3aecc | -3.34728 | -50.31966 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d0d1191-35b9-31a9-86a0-dcc795a23218 | -3.34676 | -50.32311 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99ce2eda-36c8-3dc4-ab1f-48f12432b309 | -2.97095 | -50.42602 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2e46d25e-803f-33f3-8483-429d87b19c10 | -2.97043 | -50.42948 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56f0d890-c355-3678-8f3b-b5d6e32e587a | -2.96656 | -50.41822 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 70073951-ab65-3bf9-8e83-35fdb7b7f0b5 | -2.96604 | -50.42173 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f676877-e05a-3700-a1cf-c768c83724d9 | -2.96552 | -50.42521 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 567f7b66-6309-344a-938f-f4b14094c13a | -2.96501 | -50.42868 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d226da4-d06b-3194-8c17-83378711c715 | -2.96449 | -50.43214 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a61b6540-0e56-3721-94c6-90c407b5a576 | -2.96196 | -50.52325 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e819604-de9f-30eb-a3be-a528a743d23b | -2.96145 | -50.52666 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3380575-4e53-395b-8a06-c145e8bb121d | -2.96113 | -50.41742 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b540445-5c60-35b3-89ac-5598673ca7e8 | -2.96094 | -50.53007 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 367327f9-d398-3492-835d-cf60ded39864 | -2.96062 | -50.4209 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fa7da89-9660-3989-9d59-7b5661fbb057 | -2.9601 | -50.42438 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3254b26-4cdb-33ff-9d80-5ffa22cc15dc | -2.9576 | -50.51553 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18675d08-8ca3-370c-8b05-4f7e98e8faf1 | -2.95709 | -50.519 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d49438d5-003b-3ce5-906b-09ec643bc0a6 | -2.95657 | -50.52244 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42e6ed52-836c-3413-8193-be1a53d3c557 | -2.95606 | -50.52588 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f5b49ca-d560-3538-940c-ab5dd1656dc9 | -2.95555 | -50.52929 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62e9f188-ec42-3661-85b5-de1e16fa11b6 | -2.95504 | -50.53271 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcff96aa-b9c2-3f03-8ec4-16001073ed22 | -2.95017 | -50.52846 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199e1b13-1a53-3778-8f10-5b96d6809e77 | -2.89423 | -50.40649 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ead0c3bd-08ce-31c8-a6a8-f454f5da871a | -2.8937 | -50.40998 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a9bcc93-59a6-3648-93a8-5c266ef1c77c | -4.40641 | -50.82745 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96a17615-7a4a-3408-9742-d648e1542ce9 | -4.40591 | -50.83095 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 943341ea-84c3-34e3-9015-033fe8cd73ed | -4.85036 | -50.67862 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba06662d-772c-3609-a079-bca0e2132ca5 | -4.84986 | -50.68214 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 217d4377-8130-3cc7-83cc-80c5982adcae | -4.84488 | -50.67778 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63949fe5-1130-3671-ba11-c948c4031acc | -4.82034 | -50.88892 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fc40daa-66c7-3b96-8989-f34da081edfe | -4.81984 | -50.89241 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f10c5e4b-4d95-3331-916b-9e122f561ef5 | -4.73595 | -50.69035 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa03c76d-add2-3d2a-ad89-94132cbcd104 | -4.73543 | -50.69403 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfec6f83-b2f1-312a-bb8e-fae78f2bbfa8 | -4.73492 | -50.69759 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2501c06-0c7c-3533-92da-83ea62efe2a6 | -4.62362 | -50.53146 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19769e30-610d-3532-b619-e848dae14853 | -4.62312 | -50.53505 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893c8671-f788-3d8f-b51f-f65e766d7b4a | -4.62307 | -50.53464 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2766c15a-5786-3948-87d2-debec673af9a | -4.62254 | -50.53822 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec198444-032d-3288-9aee-4efbe1bbb012 | -4.6176 | -50.53425 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff07d33-fd58-373a-be09-6ed704e97664 | -4.61755 | -50.53386 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5c65577-9d35-3f2b-bade-cc2b3a5ea40a | -4.39343 | -49.76128 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26538df8-1df0-37fc-8a93-03b51363e0fe | -4.38765 | -49.76036 | 2024-10-24 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78137f84-db84-31c5-9cf5-e2967ca685df | -4.06944 | -50.03836 | 2024-10-24 05:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f39f83d-cab2-3ddd-91a8-2f93d50ea6ef | -4.06887 | -50.04235 | 2024-10-24 05:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 161e590c-b50a-3d3f-9113-1a236a0397b4 | -3.80408 | -50.16816 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 968fd116-e7e3-37ec-8d62-361bcd3e15eb | -3.80278 | -50.16813 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dd3a7b9-c1ee-35e4-a109-82fa20e8abf5 | -3.7985 | -50.1673 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df18507f-25dc-3821-be6d-5cd80ba2c54c | -3.79795 | -50.17102 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5faa54d-555d-3f9e-9b2f-c217f521f8bc | -3.79558 | -50.03224 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b880da0d-6aae-3a8d-a52a-80fbb68eec8b | -3.76073 | -50.38278 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50fec62c-8c85-3fe0-92f7-2264e9d46ed5 | -3.7602 | -50.3863 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 418626d0-4310-348f-8fa8-de324d53cb7c | -3.75966 | -50.38993 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ebb39b8-ed16-37ec-8e13-335542396353 | -3.66353 | -50.12583 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 845642c1-d1f7-3a3e-b5d1-ed68168323a4 | -3.65908 | -50.11725 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 808abce7-ecc3-3da8-a24c-863cffda1398 | -3.65851 | -50.12112 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7271c2c0-6dcb-38e0-a83a-e059714f0d70 | -3.65795 | -50.12493 | 2024-10-24 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cde363bf-2248-3901-a916-9572c23f9eef | -5.24195 | -50.89574 | 2024-10-24 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25db03ed-1ae9-3a5c-a574-fc9eb41ea628 | -5.23702 | -50.89134 | 2024-10-24 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73074d70-640a-3105-a485-104c304c2229 | -5.23651 | -50.89492 | 2024-10-24 05:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 358214ef-f42b-3fc6-83a9-99187675aaa0 | -5.22014 | -49.95114 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7150972-1d03-3a1b-973b-6c1778b40558 | -5.21955 | -49.9552 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfd215ec-5e29-3676-8756-3bd8e27f1d6d | -5.17913 | -50.07312 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c796603e-03ef-3a16-b66d-b61b57b7c070 | -5.17859 | -50.07689 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f900b646-e44f-322f-bd12-9bdb29fffe6b | -5.06369 | -50.45015 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c96be18d-524a-36c8-9a1a-695b621f7582 | -5.06244 | -50.45033 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e05dec4a-da71-3385-baf5-79a3714b7d84 | -5.05756 | -50.45304 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f2a5540-c2ac-3939-91c9-79e01277408a | -5.05636 | -50.45311 | 2024-10-24 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd2e987b-3ade-3cb9-b41c-20aa6260d278 | 1.81746 | -50.47215 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f843809e-4db4-32d5-8c5c-2d7a0cbce2e6 | 1.81292 | -50.4758 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5e990e0-1b78-3942-9f2b-6a90a256b497 | 1.81281 | -50.47469 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 902e6433-1d2f-3fa5-a452-7cbd7ea318fc | 1.81244 | -50.47291 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 512f3aa0-6660-3233-a02e-f10c4f76ffe3 | 1.81235 | -50.47179 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dfe0e8df-0fcc-3cfd-a844-07b02e330e7e | 1.81196 | -50.47002 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58aa3732-3203-33ab-abea-26e3d4ade95f | 1.81189 | -50.4689 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fda01e4-d33e-3a4c-8e18-66c558f27e99 | 1.79776 | -50.47713 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8426ca4c-b0b8-339b-aeea-b173a09fccca | 1.7973 | -50.47424 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9c2f93e-53e8-3c64-8b16-ed606ae7bfd8 | 1.79275 | -50.47795 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d831d18f-fb07-3ac6-880a-d697b07edb2c | 1.79229 | -50.47505 | 2024-10-24 05:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1002eca8-9846-39e5-979c-381efe4b808e | 0.00602 | -51.22305 | 2024-10-24 05:21:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50fab6fd-3398-3656-9b7d-a0564dfa1fed | -3.26754 | -50.77618 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bd00fb0-6a0c-3ad1-9ab4-354f5d76630f | -3.24033 | -50.84924 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01347e72-2afc-33a9-8b81-cd093da8d344 | -3.23984 | -50.8525 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77f84538-7b93-3259-961a-a135d286b67e | -2.95552 | -51.45435 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73f1ba78-a897-37fc-8a38-fe28f7e5f7d2 | -2.95508 | -51.45724 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f8b9721-fc26-34ec-a7bf-06f0a3720d9e | -2.86712 | -51.59854 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8523609f-6fb7-38fb-b5fc-8485a5ddde39 | -2.86254 | -51.59492 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bb1c386-9737-38fa-a6e1-7f3fb6aa197b | -2.86212 | -51.59778 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46d4e026-95ac-3f3d-9b45-fed26a4842d5 | -2.8617 | -51.60062 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3da6e3ac-3698-3527-9a89-844952cdc37b | -2.86129 | -51.60345 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f285b77-9d9e-3292-9acd-65838efbaa86 | -2.85712 | -51.59702 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf17c7ae-918b-3336-b08e-4371bd08ad75 | -2.8568 | -51.59867 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38da6bd1-c95a-3bed-a126-f087a52c1a3f | -2.85671 | -51.59986 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acf0be65-dd11-3333-b07f-a107b8436eac | -2.85636 | -51.60151 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29f37ba2-3dd9-3080-bedb-703a22ad798e | -2.85629 | -51.60272 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a99e71-f7ba-3360-8526-08e11d640963 | -2.85592 | -51.60436 | 2024-10-24 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c7ace7f-82ec-3899-a4a4-1deae93ab63c | -2.81705 | -51.35119 | 2024-10-24 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README95.md)
