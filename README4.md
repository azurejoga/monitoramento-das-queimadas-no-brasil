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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b23b3989-c844-3fdc-bf6c-64eaa549891e | -3.5099 | -52.908298 | 2024-11-14 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8edddd4c-4bec-336c-af4e-86e8a36599a6 | -1.3434 | -49.144199 | 2024-11-14 00:32:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7e9572-2ff0-30a9-8241-5557e7cda5bd | -1.9797 | -46.243999 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e7cc05-cd09-3cf7-aba3-75d25c3aa64f | -1.8416 | -53.685101 | 2024-11-14 00:32:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 829e7096-45e2-3127-8bb1-a8e7312377d6 | -4.2039 | -50.490501 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8529e742-d309-3359-aa45-e155a448aa4a | -1.1048 | -53.017601 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 481ddb1f-35dd-3455-bac4-bd9c2df95e62 | -1.79 | -52.171501 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1d5a70c-789b-36eb-ba28-52c7645f3a7c | -17.2551 | -57.4482 | 2024-11-14 00:32:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce7840b7-e925-3924-aa4b-d171e9dbc252 | -4.2712 | -48.197498 | 2024-11-14 00:32:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 397dc73a-6d0c-3a8c-a152-e47524664693 | -3.9424 | -46.408798 | 2024-11-14 00:32:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84312141-1dec-3465-92b4-458e152d5719 | -1.3916 | -52.369598 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4960e3e8-1170-365d-8806-c2f73d463f07 | -1.9256 | -46.277401 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 893bf06e-44ff-3e59-9783-cc6eda0ca65c | -1.5711 | -52.022598 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f1fd846-ea22-37f0-b975-fc1afac3e5a2 | -1.2202 | -51.745998 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddb27e72-4bdd-3ece-8de3-ad81e2833c7c | -17.251301 | -57.425701 | 2024-11-14 00:32:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6242fa4b-9a25-3e93-8cb9-74bedfa0286b | -3.0449 | -50.3325 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 132d521c-f1b6-3d5f-95af-862f04abae1f | -3.3293 | -52.790699 | 2024-11-14 00:32:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb5ca1b-4c0b-3dc9-9a8b-22d83d8d94f0 | -1.6032 | -52.485802 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97dfea45-6126-39b2-b73a-9fc5e0edb484 | -3.1219 | -50.308201 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b29ceb6-7252-3b35-ae87-8008def740bb | -4.0219 | -44.6707 | 2024-11-14 00:32:00 | METOP-B | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b28d701-d43c-357c-8b6e-ef3406be7f73 | -3.4882 | -50.835499 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 836cea72-f543-33a2-bba4-ca51781ff66f | -4.2895 | -48.0975 | 2024-11-14 00:32:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8597432f-b3b2-37c5-9baa-22c7a73db38f | -2.5298 | -47.027401 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35caefbf-790b-3609-be3d-bd76da70fe56 | -1.0474 | -47.341999 | 2024-11-14 00:32:00 | METOP-B | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c4c56f-6500-3746-bdd0-cf21aadffa20 | -17.579201 | -57.5308 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f470ca03-c9a0-30f4-b9e7-98e7d31bba0c | -2.1923 | -46.3638 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05fdff2e-4a34-3e6d-ac5d-9bb2608cfd04 | -3.1608 | -45.433701 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8972370b-b2ef-3121-b493-b766c9582cd5 | -2.6372 | -46.8223 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7af5dc-8d47-340c-a94e-9bad084f30ea | -21.898001 | -56.417801 | 2024-11-14 00:32:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 470303fa-def1-35af-be5a-35588525bdc1 | -4.4317 | -45.3675 | 2024-11-14 00:32:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4e7fd6f-85cb-3d5c-8cc6-bcab037731ce | -4.1424 | -45.761101 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb42f13-fc45-30b9-bdfc-3b3a74081917 | -3.1131 | -50.2239 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cdf36d5-ee80-32b2-8b6e-5e331fea9176 | -3.1203 | -50.301399 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dd52655-59b3-322b-97ab-89ee199ecb2d | -3.0103 | -45.672199 | 2024-11-14 00:32:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b45cdbfb-c478-371d-b74c-4717a5254812 | -2.0987 | -50.843201 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b55567-cabb-3041-a094-e6c6d5b02389 | -2.6435 | -46.177898 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8631c35f-e3f3-3f80-9b9a-4ca06bb581d4 | -0.7832 | -49.491402 | 2024-11-14 00:32:00 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb3765a-1ce6-38b3-9d38-657a2da4beee | -2.6291 | -46.160099 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab475972-5d4d-3a11-966d-ed9e25d7c2cc | -3.9946 | -45.5681 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c39b0c80-0289-3eab-ac86-b5f521d7d57b | -5.5976 | -46.392399 | 2024-11-14 00:32:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5889a02-2950-3873-ac81-9769c87e56ea | -2.0619 | -46.5574 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae8aff60-b206-3af5-bc04-a523d7294341 | -4.1361 | -43.843899 | 2024-11-14 00:32:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38dfeb4f-f15a-3201-aec3-cb4344ec1611 | -17.2416 | -57.427502 | 2024-11-14 00:32:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abf17b18-1ad5-391f-a0a3-19a2202d678a | -2.1124 | -50.675701 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd4fb945-7b7b-325b-9041-0331758c9c57 | -4.1392 | -46.235298 | 2024-11-14 00:32:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 77223e49-c7b4-36c9-ad6d-55098b7e468a | -1.3454 | -53.079601 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc77454-5e3a-3f82-9018-44f5693da0fd | -3.2776 | -45.360699 | 2024-11-14 00:32:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8839a38-081c-3577-bf4c-0b9170ffc5fa | -3.8165 | -51.931198 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d802ca1b-5deb-3825-a387-3cff2ca36360 | -2.6547 | -46.808701 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e08b395-2d14-361b-b486-1fbf218a8f90 | -11.4551 | -48.003201 | 2024-11-14 00:32:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4417849-853a-3ca6-92e8-3eaf7c488d34 | -9.1572 | -50.537102 | 2024-11-14 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9473f960-e794-3295-acc2-7e3f77bdb7f8 | -1.8399 | -53.677299 | 2024-11-14 00:32:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f9508b6-4fde-3692-a957-da3b4c031ecf | -4.2054 | -50.497299 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b78d1741-56fe-3ed9-ac41-8ebeb2bbd0cf | -3.908 | -49.909901 | 2024-11-14 00:32:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c054735a-ca1b-31f8-85c2-bbc3e58264a3 | -3.0679 | -45.4319 | 2024-11-14 00:32:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b17242d5-67a3-3d09-9644-845c997cc8ec | -4.2076 | -50.690201 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 825cb87d-ed88-3617-bd78-7e28fd7f687f | -3.0645 | -50.328098 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5384055-5a36-3a55-a328-6ff01819a02a | -4.1691 | -46.097698 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4c28f4a-5ad8-3f8d-9a46-3dbce49a578b | -2.1803 | -46.356098 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3070105-2d76-3001-a8fd-7a51b065f51f | -3.8786 | -52.255001 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e72e6ba4-df7c-3f70-baa9-ebd9ccbd9a0a | -6.0296 | -44.021099 | 2024-11-14 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c763c128-a4ae-3b78-83d5-35e9b5a92556 | -1.2037 | -51.764 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23356442-82df-35aa-b024-781c8b0a1043 | -17.592699 | -57.433899 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73c539d0-d17a-33e2-9d41-5ee40da28731 | -4.4317 | -49.582699 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82413135-2816-3c6b-b323-108badb94256 | -1.7982 | -52.1623 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed3eb2d-b74d-339f-85f5-044d7c5249d2 | 1.304 | -60.401199 | 2024-11-14 00:32:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0c8d094-8f6c-32cf-9de0-c7452e80d72b | -0.9715 | -52.425598 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfa1fad1-fa99-3394-b998-66c08c15b4cd | -2.9732 | -45.867802 | 2024-11-14 00:32:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af3cfe7b-3bbb-3e46-9fc9-b942fb073fc2 | -4.4415 | -45.3652 | 2024-11-14 00:32:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cbde23a-d41e-336a-a2ba-fed32ec65092 | -17.565599 | -57.509499 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f942c79-4b0e-32b8-a5eb-e1cdeb98be8b | -3.0336 | -50.327801 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67abb614-3059-3c99-90dc-c4d275bd19ec | -2.8677 | -51.7873 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e05601c-7956-3f9f-a802-b6640e9044ff | -2.022 | -46.922798 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e638c12-80b1-38c0-89aa-182eca6317d0 | -2.1569 | -46.075199 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bffc75a1-cd18-3cd1-a106-ec1020448a5d | -2.2396 | -47.469299 | 2024-11-14 00:32:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b8a1fba-0055-3c07-9427-fa5400cb873a | -6.9467 | -39.8158 | 2024-11-14 00:32:00 | METOP-B | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d92e04ab-491b-3f85-aaa4-4c0f97289187 | -4.5034 | -46.473801 | 2024-11-14 00:32:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35011fe3-6df6-3dcb-9add-4028ab23602a | -0.3372 | -52.034801 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 266bca6d-9c25-3d3c-bb47-a5d50e697fe5 | -0.2007 | -51.520599 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 00dbe401-ae9b-35fa-a3f8-7f4a80cd3d93 | -2.8909 | -46.851002 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23762ad5-da31-3a87-9c00-102e6c7bbf62 | -3.1249 | -45.2789 | 2024-11-14 00:32:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7ddab34-79dc-315b-89b1-c23505a53ec5 | -2.742 | -51.961399 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 880da5c4-d6c2-37ba-a0eb-ae44befae519 | -3.7988 | -47.7999 | 2024-11-14 00:32:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d3b10ed-1daf-31a6-bc8a-5c10e44b6a9a | -1.3802 | -52.364799 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66599cad-b3fe-30b4-9e37-57ceb70ba9d5 | -2.114 | -50.682499 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a83a73c1-8e00-3b9e-a208-908003f3d01b | -3.9922 | -45.557701 | 2024-11-14 00:32:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b01d066d-18a6-35b0-a41d-e189f8fc427e | -0.8861 | -51.726501 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5270b09b-996f-3991-bdb6-2604669d2403 | -0.1976 | -51.507 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 69380167-44a1-3213-8cf2-9e17b8ab818b | -1.7998 | -52.1693 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d783b469-3e2e-3eaa-8057-d7a2b93c927c | -1.3625 | -52.331902 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83827b39-8435-349a-81ee-30c6748dd720 | -0.1237 | -51.544701 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 559bdce0-c98e-3bec-95bf-8aaf02c67fb2 | -2.5084 | -45.325001 | 2024-11-14 00:32:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48e0eefb-affa-314a-bd90-9c71f6171e1f | -0.4087 | -51.574501 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5bda0844-5792-3ea1-92db-ec8b3ded70b8 | -3.7049 | -50.608501 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7479f793-a88e-3c95-8b24-87fb514cfe16 | -0.9269 | -51.724701 | 2024-11-14 00:32:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b7ea615d-6729-3efa-87ed-0856ef3f061a | -3.4611 | -50.304501 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7364882f-451e-35c9-a4c7-33815275f9d7 | -4.5132 | -46.4716 | 2024-11-14 00:32:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bdaa0b80-4a82-37c5-a808-3cc252d9a04a | -1.436 | -47.783298 | 2024-11-14 00:32:00 | METOP-B | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 864ee5d3-64f9-3438-9de8-f45aa2467c22 | -2.5286 | -47.111801 | 2024-11-14 00:32:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d23539-176d-338b-88fc-13bd07f121b7 | -6.0354 | -44.045502 | 2024-11-14 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
