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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93ac2dab-38e7-3e8e-8f47-e24aded57106 | -6.1612 | -45.8662 | 2025-07-11 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 89a0a2d1-c2f5-3221-9450-3a6864c56052 | -12.4121 | -45.3628 | 2025-07-11 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| b870a71a-31db-3252-8901-d2984827837d | -6.4498 | -45.0314 | 2025-07-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 6b584e8e-0a05-383d-9615-1edd53146ec5 | -6.1419 | -45.9349 | 2025-07-11 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3a2daabc-816a-3343-8e06-62a922618e9a | -6.1423 | -45.8901 | 2025-07-11 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c8c49b96-52c4-381d-995f-daf056499fb1 | -9.9148 | -47.8282 | 2025-07-11 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 51874d73-0f7a-312c-91ef-a24fe2adf577 | -6.5824 | -44.884 | 2025-07-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 58a9a2a8-a7b3-3f78-acd6-26da9be4241b | -6.1421 | -45.9125 | 2025-07-11 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3e6e7aa6-9014-3f68-ba9f-45e1fdbce7f9 | -7.6396 | -46.0131 | 2025-07-11 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2f9311f9-2279-30a4-8a8f-6d0c6da23dd4 | -6.1612 | -45.8662 | 2025-07-11 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| dc0fa27e-b2eb-3a65-964c-b5538936cfa7 | -6.1419 | -45.9349 | 2025-07-11 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| d4a40a38-3dc0-3415-aae2-bfcbd60f8e69 | -7.6777 | -44.3496 | 2025-07-11 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 88c78ac5-66de-3db7-a89e-1822979996b5 | -7.6774 | -44.3727 | 2025-07-11 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 168ce05f-0ba2-3d28-8fbd-48fb23501019 | -6.161 | -45.8887 | 2025-07-11 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 08dc061d-3f0b-3682-a1bd-2551994e8e5a | -6.1421 | -45.9125 | 2025-07-11 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| fc9cd029-fcdb-3954-a2a0-0650360779de | -12.991 | -46.2816 | 2025-07-11 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 1e7083dd-1f63-3a73-8570-01f4a777ccae | -6.4498 | -45.0314 | 2025-07-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ba0ee45c-6228-3431-b178-07ab0ee592e3 | -12.4121 | -45.3628 | 2025-07-11 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| c5b38d69-e786-3d64-845e-b73c5eb34710 | -7.6396 | -46.0131 | 2025-07-11 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| cdd06311-2275-3dc9-aff0-d69c7694f659 | -6.713 | -44.9415 | 2025-07-11 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a14c5644-c56c-3ca3-a8eb-da740b673cd2 | -9.9148 | -47.8282 | 2025-07-11 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| b39a1e8d-53aa-38b7-82eb-f0b30b637225 | -7.6553 | -44.6506 | 2025-07-11 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| ae2631eb-1d18-3aee-941f-244c83dd0c34 | -12.991 | -46.2816 | 2025-07-11 14:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 6062a4b1-ba66-3934-a7c2-8c74ae840955 | -6.4498 | -45.0314 | 2025-07-11 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b464e607-287b-3594-aad0-e5eeabbfb76a | -5.7887 | -43.6134 | 2025-07-11 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 08442607-98fc-3adc-b6b8-38a8b354e973 | -6.1421 | -45.9125 | 2025-07-11 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| d837bc72-f08e-3f34-8b42-57cf22fa3cc7 | -7.6774 | -44.3727 | 2025-07-11 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |
| ec28eb58-e2cb-36f2-a0a8-723bd0613b2c | -9.9148 | -47.8282 | 2025-07-11 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 063b33b6-43d2-39cc-85bc-dbe91bd5be83 | -7.6962 | -44.3708 | 2025-07-11 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 415e0a8f-c31b-3973-937c-57e6484f55d6 | -12.4121 | -45.3628 | 2025-07-11 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 7c0df95a-a8bb-34cc-83ad-cc8d3d662a37 | -12.9902 | -46.3273 | 2025-07-11 14:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 3b7c4c32-2bac-3721-bbc1-5a0c497af06d | -7.6777 | -44.3496 | 2025-07-11 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 160.4 |


