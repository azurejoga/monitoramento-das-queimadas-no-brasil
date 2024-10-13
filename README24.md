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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c359e9c2-7f5f-3ea9-8f6f-da2ca01e2bd6 | -12.9193 | -62.5019 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 46c8a843-c0ad-38ca-a6f4-6261871ebaa6 | -12.921 | -62.509499 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ef64e6c2-5760-3c64-a920-734b467e3024 | -12.9227 | -62.516998 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 29621736-b3dd-30e8-91e8-3c956d533863 | -12.9245 | -62.524502 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20d097d2-bae2-324a-a696-588ec47bb5a9 | -12.952 | -62.644402 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 59844ef1-7846-3379-9219-9762e8c03abf | -12.9537 | -62.651798 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fda49c5-64a5-3664-84fd-fd817a001390 | -12.9606 | -62.681599 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a7838c6f-2368-3646-b521-fc0ecdb8c3be | -12.9623 | -62.689098 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 194e973a-b3c8-397f-adef-fcaca972fd0a | -12.964 | -62.696499 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee216cc-8edf-38da-886d-bd606a4f02b4 | -12.9674 | -62.711399 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 152a2e86-4355-3734-9700-224f94238b23 | -12.9691 | -62.7188 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df18bc8d-666c-39b9-a3ac-8e585c295e25 | -12.9793 | -62.763199 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae82b8dc-beb0-32b7-b8a6-3ac2364ca856 | -12.9129 | -62.519299 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9309bff6-c5db-392e-8f35-313a9e87c41c | -12.9712 | -62.7729 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 445c85ec-ddb5-3b14-905e-a9f45ac1dfea | -12.9729 | -62.7803 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b034410-691a-37e8-a76c-862c296fb0d0 | -12.9745 | -62.787701 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0c59b52-9fc1-3195-a805-96c7e0ca6ebe | -12.9631 | -62.7826 | 2024-10-13 01:43:13 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f224f517-1fd0-3db6-a88e-ea72423d5479 | -12.9647 | -62.790001 | 2024-10-13 01:43:13 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbe24c5-cabc-34e0-9567-f6d800bdf3b2 | -12.9282 | -62.720699 | 2024-10-13 01:43:13 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 782286d9-5f03-3b16-b698-bf299a0d2036 | -12.9299 | -62.7281 | 2024-10-13 01:43:13 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78de8fd0-a85d-385b-90e2-9cbccb5610b3 | -12.7729 | -62.091999 | 2024-10-13 01:43:13 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67b1d9a5-7755-3974-a32d-5d5aeb98c416 | -12.7747 | -62.0998 | 2024-10-13 01:43:13 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5fe60e4a-c519-3ed6-95f6-175bfb194957 | -12.7765 | -62.107601 | 2024-10-13 01:43:13 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f02b39c1-d1e1-35ab-aed6-d1eb25378108 | -12.7617 | -62.266499 | 2024-10-13 01:43:14 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e65e70b8-29a1-3fd1-942a-694e21003986 | -12.7634 | -62.2742 | 2024-10-13 01:43:14 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 917226b7-5aec-3e29-882b-ee34af911589 | -12.7652 | -62.281898 | 2024-10-13 01:43:14 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 92e31dae-f5c9-374f-8254-ff644fffa858 | -12.804 | -62.449699 | 2024-10-13 01:43:14 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a37671cf-515f-3979-a3b6-6060dc7b5b25 | -12.8831 | -62.7938 | 2024-10-13 01:43:14 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f9dd8c56-7dc6-3400-8432-e8924eb38437 | -12.7536 | -62.276501 | 2024-10-13 01:43:14 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b21857a7-2d98-30bc-b9c9-bdccf0e3f413 | -12.7217 | -62.2272 | 2024-10-13 01:43:14 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3feb59fb-3c8b-3686-8e89-f0f599621f70 | -12.7119 | -62.229599 | 2024-10-13 01:43:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b71297fa-8c62-3698-b79e-48fa84a469fb | -12.7137 | -62.237301 | 2024-10-13 01:43:15 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77dca692-81d2-38e6-a546-a102316f4a9e | -12.8239 | -62.986099 | 2024-10-13 01:43:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4326b7b0-3b35-31ac-b6b1-24ee15f1fd72 | -12.8255 | -62.993401 | 2024-10-13 01:43:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc1caad-c464-35e6-8948-6498cec732ac | -12.8272 | -63.000702 | 2024-10-13 01:43:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad573d2b-d92a-30c3-95ef-04768d1bf5d7 | -12.8141 | -62.9884 | 2024-10-13 01:43:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 91a1c023-28ad-3316-a682-a3f94faee8f4 | -12.7408 | -63.0289 | 2024-10-13 01:43:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a48a208b-eff6-3ed5-bec0-6839de00158d | -12.7424 | -63.036098 | 2024-10-13 01:43:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6c165752-73e4-3cc8-88a3-0393f29979c9 | -12.7311 | -63.0312 | 2024-10-13 01:43:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfbb76c-5987-3efb-afe3-1927c273c3a5 | -12.7196 | -63.0261 | 2024-10-13 01:43:17 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b8ee9283-7b9e-378e-afac-f0cd72fe6096 | -12.6947 | -62.962601 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eda59508-97c4-3005-93b3-e7721bed4281 | -12.6964 | -62.969898 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 66b0e587-ac01-3907-8e3f-e6db2811c48f | -12.7081 | -63.021099 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1028910-cfe3-392d-b7dc-b26a78d6028e | -12.7098 | -63.0284 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07c31456-d08a-3784-bc44-641c0bf46336 | -12.7115 | -63.035801 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 900434bc-4a36-358c-9887-80ade85b3d7c | -12.7181 | -63.064899 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f789b652-209f-39e2-8f05-3acef0909972 | -12.6983 | -63.023399 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7910ee-50ca-3e05-bac8-b8f14488a518 | -12.7 | -63.0308 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5b0cab8-ace8-34e5-a1ea-7693548bd4e2 | -12.6968 | -63.062199 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21a7848b-a36a-3b6a-a6cb-8c7fd8e18626 | -12.582 | -62.605999 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4107d886-8b71-3f36-b767-701c1a628e16 | -12.5837 | -62.613499 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40519b95-b5eb-3d2e-86c3-e0a041a1931a | -12.5722 | -62.608398 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 406d0e12-cb94-3839-82a5-fc6194336afb | -12.5739 | -62.615898 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c2619f5-9c7f-36b7-8263-735c68b8410a | -12.6674 | -63.069099 | 2024-10-13 01:43:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 770d21a1-0cfb-3e9b-a533-15c8fac6783a | -12.4841 | -62.989101 | 2024-10-13 01:43:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac23dcc5-c0c2-3f77-ba4f-fb5e023f5e51 | -12.4858 | -62.996399 | 2024-10-13 01:43:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 644c46d3-9448-3fc7-9d32-50d4a8a0845a | -12.4875 | -63.003799 | 2024-10-13 01:43:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae7f04b0-e4e2-3874-92e9-9ffaabf94591 | -12.3117 | -62.284599 | 2024-10-13 01:43:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06f167d3-6675-3164-9954-703d245f93d8 | -12.3135 | -62.292301 | 2024-10-13 01:43:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49198949-19b3-3d82-a671-43c44d603e9b | -12.3153 | -62.299999 | 2024-10-13 01:43:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f261f71b-7c89-3fc7-917e-abb8f76281c3 | -12.317 | -62.307701 | 2024-10-13 01:43:21 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e923f7d2-dc38-36da-bb75-fb3510960263 | -12.4744 | -62.991402 | 2024-10-13 01:43:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c395434-d6cd-37c4-964c-5c7d4a1544a2 | -12.476 | -62.998699 | 2024-10-13 01:43:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce000cc-64a1-3ed9-a268-b3efe40234e9 | -12.4777 | -63.0061 | 2024-10-13 01:43:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c554957-0e86-3b0e-a446-d8e9b10e2cfd | -12.4629 | -62.986401 | 2024-10-13 01:43:21 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b4fa9be-1717-32d3-b643-91b9f6291be2 | -12.4531 | -62.988701 | 2024-10-13 01:43:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3b303719-8e6f-3505-8ce0-3cd4e10e4ae9 | -12.5031 | -63.253101 | 2024-10-13 01:43:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e2fae1c9-3bab-3aae-8bdf-4ed481487a0e | -12.5047 | -63.2603 | 2024-10-13 01:43:22 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cb0f0c1b-72e7-321d-8a5f-d3b058e40672 | -12.3745 | -62.9608 | 2024-10-13 01:43:23 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3d2e088-e7cb-3872-afbd-c08008762002 | -12.4931 | -63.937901 | 2024-10-13 01:43:24 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 39f025fe-f1ee-39d2-b866-2f7d29fd752d | -12.4947 | -63.944901 | 2024-10-13 01:43:24 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0508a2a0-e1e3-3b1c-915b-1cddf0924c3a | -12.3916 | -63.716202 | 2024-10-13 01:43:25 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb2a581-f1f1-32b7-bf43-cb5ba58bb581 | -12.3932 | -63.723202 | 2024-10-13 01:43:25 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d497651-d149-3811-ac22-b7de719b9764 | -12.3948 | -63.730301 | 2024-10-13 01:43:25 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aade3364-bbf2-3e9e-9f15-1c27980e9d33 | -12.3964 | -63.7374 | 2024-10-13 01:43:25 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a5cf30db-782c-3107-b1b3-9ccdb8cb0198 | -12.3818 | -63.718399 | 2024-10-13 01:43:25 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 030c5145-4e5f-3609-930a-49c3764e79be | -12.3834 | -63.725399 | 2024-10-13 01:43:25 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58d7ad89-e7e0-392d-9f5e-202b2ea03f20 | -12.385 | -63.732498 | 2024-10-13 01:43:25 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb8813e-7938-3c97-af07-720ef9467f66 | -12.3614 | -64.315102 | 2024-10-13 01:43:28 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99192c50-a697-3d8a-95ac-2dcb59f9cb4b | -12.1422 | -64.717697 | 2024-10-13 01:43:33 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc18357c-528c-3d3c-b02a-89288297fb54 | -11.7617 | -63.802799 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cd99836d-cefe-3550-ae25-356890667c7b | -11.7633 | -63.809898 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c0084e97-a7d8-30bb-89f8-1e6088462345 | -11.7649 | -63.817001 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f39c6e2e-5f34-3f5a-8fb8-39a1d1fbb738 | -11.7535 | -63.812199 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ec77fed7-2c55-3c5e-9ec1-4ff8baed4977 | -11.7551 | -63.819302 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 686f1cab-66fb-35d2-87b2-6143597d8736 | -11.7567 | -63.826401 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ece3c35b-e73a-3891-9643-2fd393cab016 | -11.7437 | -63.8144 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 28d4f8df-d340-38e2-98d5-702ae728ad32 | -11.7453 | -63.821499 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a6ce19d-1237-365a-b2d8-d97922d962c9 | -11.7469 | -63.828602 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 92aed23f-c518-3a60-b4c0-ded9f89f5259 | -11.7485 | -63.835602 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 592e5dde-9ed2-3b5b-8e0b-b650a0c589e6 | -11.7307 | -63.802502 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5228025-fd43-3fdc-bdbb-af4443eb06b7 | -11.7323 | -63.809601 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 15abd002-34b8-3958-ba96-a770b2a3d71b | -11.7339 | -63.8167 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8eeb45-f148-3186-abba-74b04d4cf27b | -11.7355 | -63.823799 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2268dead-b28e-3ab4-aa78-8f3e4ef57d8a | -11.7371 | -63.830898 | 2024-10-13 01:43:36 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58a7cdb1-1b82-3519-83a7-ed9f975e04ac | -11.7619 | -64.0774 | 2024-10-13 01:43:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de27f42d-c3b2-3cbd-8dbf-87563579b350 | -11.7635 | -64.084503 | 2024-10-13 01:43:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9ed4ed1-adc2-3d60-9b6a-fa2a38119d6f | -11.7793 | -64.154701 | 2024-10-13 01:43:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 431a0cec-25e5-3913-aa18-2391cb0b6d02 | -11.7808 | -64.161697 | 2024-10-13 01:43:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 348ff8ac-3877-3abf-b35a-f499c3269793 | -11.7824 | -64.168701 | 2024-10-13 01:43:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README25.md)
