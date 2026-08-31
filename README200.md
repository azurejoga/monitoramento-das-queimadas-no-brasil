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

## Dados Diários - Página 200

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df365599-b3c4-37c8-acd1-f4cd8323933d | -15.9898 | -55.9559 | 2026-08-31 19:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| c3213549-9d63-3b2b-93c0-af2d40cfac8f | -7.2747 | -46.8036 | 2026-08-31 19:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 82deb79c-50bc-3139-9ac6-5bf814549fce | -4.2275 | -59.8671 | 2026-08-31 19:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 70cf6f7e-0842-32e6-9089-fb2b7f077406 | -3.2623 | -58.2367 | 2026-08-31 19:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| d435e357-2059-36d6-8009-8e16530108bd | -14.444 | -53.4016 | 2026-08-31 19:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 341c9f15-037f-356c-ad8d-d3fb21feb765 | -9.1711 | -59.618 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| fa0a1506-58a3-3dad-b014-86acc0817941 | -7.9172 | -61.329 | 2026-08-31 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b274a2cd-29aa-327a-853c-887e7eb2afb5 | -8.0094 | -71.1611 | 2026-08-31 19:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 7de82648-dd46-3c25-8ac7-6b6d34ebfd62 | -9.1718 | -59.5211 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c49ab77b-4f80-3d19-82ff-e0f086348b0b | -4.1698 | -60.7064 | 2026-08-31 19:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 881f414c-a5ed-368a-a1c6-ef42ec25e2f4 | -6.8233 | -58.8786 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 3be8593f-9db8-35e8-8b3b-a4faaf0db8d7 | -7.4735 | -61.3846 | 2026-08-31 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 30738060-2ff0-39af-95d0-8fb39770d6e5 | -6.7514 | -55.6654 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 25067608-1e89-33e6-8dd1-9178912d27db | -10.1338 | -45.7688 | 2026-08-31 19:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 928d4973-c806-3d76-a40c-277040078e2a | -7.6253 | -55.2787 | 2026-08-31 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 7cd1aac6-43fa-32f7-a502-3979b34fe268 | -11.4828 | -58.5159 | 2026-08-31 19:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 0f30d352-ece1-31d9-8fcb-3ebf8e320276 | -7.2934 | -60.5713 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| dc1c6f42-1f8d-31db-a772-3dc2c1a2efea | -9.153 | -59.5415 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 091d0272-07b7-3645-ad66-d57e7454a528 | -6.8009 | -59.5742 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 9d64dd30-b50f-3115-abb8-0abd492ff02f | -11.1809 | -55.0821 | 2026-08-31 19:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 38317bfb-0d57-3d69-8b89-2169aad1d01e | -10.844 | -45.3356 | 2026-08-31 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c6a82c4e-c32b-3826-b192-55eddab1c8ac | -9.2081 | -65.7857 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8e8b7416-28dc-35ed-8aa6-8be2fd56d72e | -11.0747 | -51.5153 | 2026-08-31 19:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7bbd991f-cd5a-376d-9df3-ad0b38df9889 | -14.1263 | -52.8106 | 2026-08-31 19:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 6f13407c-4c52-3b60-bdbd-f78a1ae513b3 | -5.2547 | -55.9105 | 2026-08-31 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3d3823d9-f3f1-3b6c-8d5f-91a0c6515497 | -6.7997 | -59.7857 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 2a6f04c0-213a-3029-9350-3d757a1e5019 | -9.2144 | -47.99 | 2026-08-31 19:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d02f16e7-81ee-3e3b-b80d-c6ad1c23a522 | -5.2548 | -55.8907 | 2026-08-31 19:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ca0a75e4-ab53-31a3-97a6-838ad881e266 | -12.9782 | -45.941 | 2026-08-31 19:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 12c784c4-7c9c-3c4e-8c53-95c67ce5258c | -3.3871 | -59.4075 | 2026-08-31 19:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 208708e5-1ebb-31dc-a9c3-973717665375 | -10.8627 | -45.356 | 2026-08-31 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e6e5434d-f746-3c1a-9cb9-4a4e3b214519 | -8.87 | -66.9121 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 7350974f-4453-37ab-8a97-93a8f57487c8 | -7.0219 | -59.6422 | 2026-08-31 19:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 1e4c30ca-844c-3270-8b0b-566cdbcef555 | -10.8635 | -45.3101 | 2026-08-31 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| ba613ac8-5bfd-37d4-9833-7d8861c02f4c | -14.7108 | -53.599 | 2026-08-31 19:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 823506c1-2c41-3848-91ca-fe2c734f4c75 | -8.6154 | -54.7945 | 2026-08-31 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 12c6e3d7-5344-3bae-9d7c-f3ba322d564f | -15.6333 | -56.4081 | 2026-08-31 19:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| f9b1fddc-de87-3176-9f14-e4896124a473 | -5.9451 | -57.6906 | 2026-08-31 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| b2395da3-ea73-3cc0-88f8-89c7736aa51c | -9.1895 | -59.6364 | 2026-08-31 19:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 31c3694e-e6db-35c2-bb2f-f3673c4dbb74 | -8.3601 | -70.8458 | 2026-08-31 19:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d0bc0b5a-69d4-36ab-a9e5-d02c55df5821 | -4.1515 | -60.7068 | 2026-08-31 19:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| da558ae9-55fb-3587-b81c-190c9ae3313d | -14.6338 | -53.5876 | 2026-08-31 19:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 4e07af5d-303c-32d6-95a8-ba964682a40e | -8.5924 | -66.975 | 2026-08-31 19:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |


