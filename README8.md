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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abc0739b-d311-3333-be25-5a322ef96aca | -3.9376 | -46.022499 | 2024-10-27 00:14:23 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39d78443-4b47-3e30-b8cb-efb81b9279df | -3.9393 | -46.030102 | 2024-10-27 00:14:23 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7258b3f-d620-3704-8716-992cba875f58 | -3.9278 | -46.0247 | 2024-10-27 00:14:24 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6342af6-141a-3bbf-9c29-0e0fed22d9d6 | -3.9295 | -46.032299 | 2024-10-27 00:14:24 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee1bbebd-71de-3a04-a120-15f3c4163974 | -4.0072 | -46.428001 | 2024-10-27 00:14:24 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 023d0180-778c-3e15-abf6-23d79f187fdd | -3.9974 | -46.430099 | 2024-10-27 00:14:24 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d427539-4e34-3c07-aa12-cbee34368976 | -3.749 | -45.361599 | 2024-10-27 00:14:24 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba9860d-741e-328f-af3d-a3a6e1243da8 | -3.7506 | -45.368801 | 2024-10-27 00:14:24 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27ee30c5-4f85-34fc-8496-caa3b1a6282b | -3.5982 | -44.780499 | 2024-10-27 00:14:24 | METOP-B | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd9dda47-7111-36e9-91f1-60c1f11a0018 | -3.7599 | -45.502899 | 2024-10-27 00:14:24 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 680fbfaf-f4bd-3349-bba4-64e6d475af41 | -3.7615 | -45.510101 | 2024-10-27 00:14:24 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3de1a2-023e-3812-ae0f-ac9fc24cf981 | -3.3823 | -44.0494 | 2024-10-27 00:14:25 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71b66846-2804-3c83-9a98-e52b6e342a4b | -3.3839 | -44.056198 | 2024-10-27 00:14:25 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb764990-1809-3186-a8e7-d51582306974 | -3.7553 | -45.896999 | 2024-10-27 00:14:26 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| affe54b4-af0d-3f5c-800a-f7d587276c99 | -3.7569 | -45.904499 | 2024-10-27 00:14:26 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b91b0d8f-0091-3f3c-9074-17ed06c544a6 | -3.7586 | -45.9119 | 2024-10-27 00:14:26 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32b134fc-389d-3bda-ba82-651fecd62cfc | -3.7388 | -45.869301 | 2024-10-27 00:14:26 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbf83022-8488-312a-819e-dacafe13f68e | -3.7405 | -45.876801 | 2024-10-27 00:14:26 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 789ecd78-fbe6-3f4f-9bcf-866a83ba0f7a | -3.3633 | -44.3764 | 2024-10-27 00:14:27 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f07061c-e8ed-3c5b-b87f-58ddb8dc1ac3 | -3.3648 | -44.383301 | 2024-10-27 00:14:27 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12722b52-31d5-36aa-8f7d-bf25a49fe0f8 | -3.3663 | -44.390202 | 2024-10-27 00:14:27 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d71f247-cd1f-3651-b05c-cfdfad84087f | -3.6785 | -45.9217 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf6b91f-7c5c-34d1-9d92-1a4d5fad6c05 | -3.6801 | -45.9291 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c76f127a-4b94-36ed-ad5c-ce702858787b | -3.6637 | -45.901501 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be8a885e-4647-3bd4-bc0a-3c267025a01d | -3.6653 | -45.908901 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a05c580-a0ea-3131-8539-3d04492ffcfa | -3.667 | -45.916401 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41f363e8-79f8-3e1d-9557-194e15ee67b6 | -3.6687 | -45.923901 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f87dbfc8-54da-3c4e-893b-70f38fb56582 | -3.6703 | -45.931301 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 185e6855-3580-36f8-bcbd-c5041bb4cbe3 | -3.672 | -45.938801 | 2024-10-27 00:14:27 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fba93a9-f212-3ad2-ae3a-a70108bb8abf | -3.2689 | -44.232101 | 2024-10-27 00:14:28 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52e24d5c-b790-388b-8e42-14258436549f | -3.6228 | -45.902599 | 2024-10-27 00:14:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a448eb3c-0c77-3d29-acfa-a9052870b671 | -3.6245 | -45.910099 | 2024-10-27 00:14:28 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9da36f23-5c9b-3973-97a9-c07cda01bc1a | -3.2789 | -44.4599 | 2024-10-27 00:14:28 | METOP-B | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba48d2d3-1dba-3a76-87ce-986cc3f69a40 | -3.4482 | -45.397701 | 2024-10-27 00:14:29 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc3b2a63-2a58-335f-9b25-e774001e13f7 | -3.4498 | -45.4048 | 2024-10-27 00:14:29 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0cc5bb-f76c-3b43-9c77-f13d6514c16a | -4.3844 | -49.726299 | 2024-10-27 00:14:29 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41cce903-fcc4-3f84-b686-c76356f78655 | -4.3871 | -49.738701 | 2024-10-27 00:14:29 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84b5620d-4351-3299-9fe0-fb46b071aa1a | -4.3898 | -49.751099 | 2024-10-27 00:14:29 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f677bca0-11d1-32bb-acde-4596e1fe951e | -4.3746 | -49.728401 | 2024-10-27 00:14:30 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b65915ab-adf5-3617-b9fe-1a90f4a14149 | -4.3773 | -49.740799 | 2024-10-27 00:14:30 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae448a6a-e548-3d35-915e-020411c4e90c | -3.4639 | -45.651699 | 2024-10-27 00:14:30 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69a63338-c577-3f0e-a3a4-55f1622f4bd0 | -3.4655 | -45.659 | 2024-10-27 00:14:30 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 725295b4-6aec-3421-8bbe-985dd85b72c7 | -3.4524 | -45.646702 | 2024-10-27 00:14:30 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0edd1b9-e708-3dc7-90d6-c966900e9436 | -3.4541 | -45.6539 | 2024-10-27 00:14:30 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8001528-e6ea-329f-8fee-2c1dfb6b2d50 | -3.4492 | -45.862801 | 2024-10-27 00:14:31 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2fb9a65-b0f0-396b-8afd-d19637b70fc9 | -3.4509 | -45.870201 | 2024-10-27 00:14:31 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb999fa-0bc7-38bd-87d4-e8447e9173b8 | -3.0623 | -44.3209 | 2024-10-27 00:14:31 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54fe9d73-9add-3a8e-b145-08b108e27629 | -3.0638 | -44.327801 | 2024-10-27 00:14:31 | METOP-B | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37dfaf12-183c-3fc7-bc34-7e802d646cb5 | -3.27 | -45.429401 | 2024-10-27 00:14:32 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0ff3a1-954e-3601-bfad-b1fa867c31f4 | -3.2716 | -45.436501 | 2024-10-27 00:14:32 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 023f979d-325b-3308-9b6c-a0a3b362335f | -3.4522 | -46.337002 | 2024-10-27 00:14:32 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1d3b041-53d7-38e4-ba2f-80a651af3b46 | -3.4539 | -46.3447 | 2024-10-27 00:14:32 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21bab05a-06f8-369d-926e-ddffa39a27c1 | -3.4424 | -46.339199 | 2024-10-27 00:14:33 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 209a29d3-50ee-3954-9a2b-72e182829e58 | -3.4441 | -46.346901 | 2024-10-27 00:14:33 | METOP-B | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ead95506-50f7-362c-ba5c-c92251f98ef9 | -3.115 | -44.967602 | 2024-10-27 00:14:33 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67c5c369-0ea5-37e3-add4-590de2bdfd02 | -3.1165 | -44.974499 | 2024-10-27 00:14:33 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35e44c67-a61d-3b3f-962b-ec6df7f1a647 | -3.1181 | -44.981499 | 2024-10-27 00:14:33 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfbd3a6-cd55-3ea8-a19e-ef3d3af20283 | -3.1067 | -44.976601 | 2024-10-27 00:14:33 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88189057-9cb9-3ced-aec6-57800ef69ac7 | -3.1082 | -44.983601 | 2024-10-27 00:14:33 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ebd2880d-3790-373d-a299-60dc5d218dd9 | -3.0954 | -45.385502 | 2024-10-27 00:14:35 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba146d7e-1eef-303d-a1f9-e7a2b0502bde | -3.097 | -45.392601 | 2024-10-27 00:14:35 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09c1407a-fd5d-3b84-95f2-7c36303e9a57 | -3.0986 | -45.3997 | 2024-10-27 00:14:35 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b85187f-67d9-337f-95a0-fa81a3b8947a | -3.1842 | -45.782101 | 2024-10-27 00:14:35 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91250421-62bc-3afd-8161-d027fd1c933e | -3.1858 | -45.789398 | 2024-10-27 00:14:35 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35adebc4-4f94-3b1b-9db4-c3f496953dc2 | -3.176 | -45.791599 | 2024-10-27 00:14:35 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1dab0028-ddf5-3672-aa0b-92a0f895319b | -3.0109 | -45.100399 | 2024-10-27 00:14:35 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 368782f5-151b-387f-8ad8-7db509aa95d9 | -3.817 | -48.865101 | 2024-10-27 00:14:36 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb8a32f3-4330-3789-8cfc-5c883aa63095 | -3.8193 | -48.875801 | 2024-10-27 00:14:36 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a22447bb-7d79-3fa1-842a-05f5c758c9c4 | -3.8072 | -48.867199 | 2024-10-27 00:14:36 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b721d3ee-76b6-3531-bd44-8b8e024f4beb | -3.8095 | -48.877899 | 2024-10-27 00:14:36 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc8dc8d0-3ec5-30b7-8e92-d4b95f6d808a | -3.0781 | -45.6301 | 2024-10-27 00:14:36 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1762fa97-dffc-3c80-82ca-885d47eb1d8d | -3.0798 | -45.637299 | 2024-10-27 00:14:36 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35b09e25-a72f-30e0-bce6-30a6bbdae3bc | -3.0814 | -45.644501 | 2024-10-27 00:14:36 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94fd5f4b-cb8a-34d9-a062-e3887f572433 | -3.083 | -45.651798 | 2024-10-27 00:14:36 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2b86e4a-bcde-378d-b523-814901b1f755 | -3.07 | -45.6394 | 2024-10-27 00:14:36 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee33ab00-1d50-3b01-8ada-e1a8e18d2c45 | -3.0716 | -45.646599 | 2024-10-27 00:14:36 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35e24188-d1dd-33b5-8be1-e721e4820641 | -3.1871 | -46.1632 | 2024-10-27 00:14:36 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1a192d6-f0a5-3702-8997-56f03c2d2b63 | -3.1887 | -46.170799 | 2024-10-27 00:14:36 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5eeeafa-0e82-360e-b254-399698bead69 | -2.9041 | -45.175499 | 2024-10-27 00:14:37 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4c239792-35d2-3100-8b46-52253d56cba3 | -2.8716 | -44.984699 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 20ae5e86-9be7-3704-b02c-49e80503d974 | -2.8731 | -44.9916 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3b8e181-c580-3cac-8ae1-4ce8a21b6d20 | -2.8602 | -44.9799 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1b9d2a1-4280-3476-95e9-ae2b38738ce5 | -2.8617 | -44.9869 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 603146b0-00ee-3d7f-99ef-985c0013349f | -2.8633 | -44.993801 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0db79fbf-4fb7-37a2-a3b3-00126985bb4c | -2.8649 | -45.000801 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82174561-ae8f-3c95-a66f-17a8b7941224 | -3.4565 | -47.6511 | 2024-10-27 00:14:37 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b92de287-93dd-3f29-b9bd-a6de62c6904f | -2.8488 | -44.975101 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2563cf-9d71-3c6e-9507-5ea5cdb33c0e | -2.8504 | -44.981998 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8968f8ac-e632-30ba-8909-9ba624e31829 | -2.8519 | -44.988998 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28bb2d0e-1a23-3ce2-b411-4641ec0554ce | -2.8535 | -44.995899 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c629e94-c711-31d8-94f1-a185684f2e85 | -2.8551 | -45.002899 | 2024-10-27 00:14:37 | METOP-B | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8df679bb-3ddf-3efd-8ba9-cfcd0451db7b | -2.8406 | -44.9842 | 2024-10-27 00:14:37 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3964c5-0fb1-3808-be48-c54c07d68019 | -2.8421 | -44.991199 | 2024-10-27 00:14:37 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32dbdb86-e1f2-3d18-8790-cb693917169c | -2.8437 | -44.9981 | 2024-10-27 00:14:37 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6cd721c6-fc95-39e5-a72c-4443f54a28ae | -2.9239 | -45.400902 | 2024-10-27 00:14:38 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 705c2fce-34c7-32a7-b605-91fa89ec0028 | -2.9254 | -45.408001 | 2024-10-27 00:14:38 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d954a7d-3935-3b0b-b7b4-0ea94fdce7a6 | -2.8501 | -45.439499 | 2024-10-27 00:14:39 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7ba720e-239a-391b-8e37-e4fb9316fc40 | -2.8517 | -45.446602 | 2024-10-27 00:14:39 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71d3c613-a2f2-3ed3-8d8e-cbabf1511dbc | -2.8533 | -45.453701 | 2024-10-27 00:14:39 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8629141-ff06-3e93-894c-af055a04a43c | -2.8507 | -45.855499 | 2024-10-27 00:14:40 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
