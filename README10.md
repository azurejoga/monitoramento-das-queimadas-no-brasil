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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71530c9b-5306-36fe-86fa-25f65d006cd4 | -3.0983 | -61.2202 | 2026-08-19 00:59:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e02e3d0-6a94-39fe-8a77-81d5647b05e1 | -9.4285 | -60.420399 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2016ccf7-d375-3d82-bb0c-82a1aea16997 | -6.1349 | -57.861599 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e44ffc9-aafa-3ca0-bfe0-e9b3f6fa0af6 | -6.8572 | -59.012501 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50136a5d-9583-31a4-b264-feb8bcdf2928 | -9.4035 | -60.5821 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1db220bf-6e29-34a6-9cf7-5a1d482c1f95 | -6.8291 | -56.440899 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dec6fbfa-80d5-3999-b86e-a6cd7da425de | -8.5435 | -54.7127 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abde287b-2127-3d4f-9c73-e6cacc75d877 | -6.5908 | -59.108601 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3a093cf-4138-3454-a790-936803dd50d8 | -8.5669 | -54.766102 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bcb3901-2a55-3a7c-8b23-1e53966aa523 | -12.9432 | -56.6381 | 2026-08-19 00:59:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff30158-1907-300e-ba94-afb34db183ce | -10.9369 | -57.102501 | 2026-08-19 00:59:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 383d1c6e-db7c-380b-b5d1-801e1cd9f052 | -6.6992 | -58.953999 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0d428a5-8c7f-3889-a909-6170a3141295 | -11.6929 | -54.559601 | 2026-08-19 00:59:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba4bc73-e269-3098-aa22-9cc7cad0eeca | -6.1372 | -57.871101 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e17ea4a-e620-3960-9f26-788e53866ee2 | -9.4101 | -60.565701 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e72c1a61-b79a-3988-b578-0def7a94919f | -6.8455 | -59.006699 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 131a8ccc-c592-335e-ae1e-84b8b137d891 | -6.9566 | -59.0411 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4da5d1b3-d013-3978-84cb-bd4b280129a0 | -6.7071 | -58.943401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd517374-b5b4-3ee6-9cfd-fbab50e24eda | -6.6868 | -59.0779 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8738276-ab25-3575-87bc-3dff7b92388e | -9.1638 | -59.668499 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd35d78-b290-33bc-ba21-3fb01ffd379b | -7.4361 | -59.777401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eaeab8d8-d4c7-3c04-b419-3ba5341bb644 | -6.7484 | -59.1661 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae239b26-a51e-36a9-93e8-9591188376da | -9.2194 | -60.815701 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3a16af1-ad05-3817-9213-3cb7d1cee80a | -19.7432 | -57.944698 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e1367995-6d44-351f-b2e1-d17722ab538a | -7.0456 | -59.827599 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1e868e-d591-302b-a614-39594908c129 | -8.5601 | -54.738201 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89eaf8a0-b56d-3a37-9e64-256b298edb98 | -6.7559 | -59.465599 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a95537b8-a680-360a-ac15-720a30191d47 | -7.102 | -59.7589 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 416af547-7169-347e-9469-0f3ac07cb89f | -6.0192 | -57.8074 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69426a77-6395-3792-afc3-046309783d7f | -8.9502 | -60.537601 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96efdc04-b772-3177-aed1-fb7f10f1aae4 | -6.7503 | -59.174099 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6af9549-3c9a-3cdb-88ba-d1144d052e7a | -8.9534 | -60.551701 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79a26f85-6993-3ddc-a3b6-6b3998eccf61 | -6.8128 | -59.444302 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3916eee9-5481-315e-81d4-32747f892445 | -7.5393 | -55.5812 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dbbfd97-19cc-3d29-9947-c5760bd7c86d | -6.7933 | -59.448799 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19014c4e-e883-3b30-a8a3-4e7af6cdd1cd | -6.7662 | -59.1535 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5dfdb640-e7c9-391f-920f-95338bf1c6ac | -8.4963 | -54.8568 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a830fbd-2a6b-376f-a3b0-4e30b3662ae2 | -19.7661 | -57.9547 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 54778379-e2a5-3603-b0ba-1b08ec580cb8 | 0.2441 | -60.512199 | 2026-08-19 00:59:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0c329b90-aff4-37f1-982b-e94cf775c7f0 | -6.803 | -59.446499 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ffbc89f-432c-35a1-8989-0da87f0a8aae | -6.3036 | -55.8792 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 856e9fa0-d4af-3f1a-8927-d37bf2e08715 | -6.3066 | -55.891899 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1f841bb-f92d-3ea2-9358-1ec928efc600 | -9.1121 | -60.388802 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 005ecb80-bf8c-3405-9b08-ff172bfee6a4 | -7.4315 | -59.8022 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 975a8308-32b7-3d56-ab81-99ce46250ef3 | -8.503 | -54.8625 | 2026-08-19 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| a4ce86d5-e2e1-325e-9cbc-a7ff1f8a0af8 | -5.9995 | -57.8444 | 2026-08-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 02101dbb-1a55-3215-abf0-5312d4557349 | -5.4317 | -48.4212 | 2026-08-19 01:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| d75993ec-7e93-3125-83d1-162b505778e3 | -7.0576 | -59.8523 | 2026-08-19 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| de8c5762-7ab3-32fe-bf34-35c8c6efc573 | -6.7123 | -58.9412 | 2026-08-19 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| cffa676e-a27c-3504-8a0d-bc4a936d9f2d | -6.3496 | -54.9068 | 2026-08-19 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 75d6fdd1-9e42-324f-979f-6699e6c06c3a | -19.7438 | -57.9633 | 2026-08-19 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.8 |
| 35a50448-f706-37ab-a504-56a5ab4d8ec4 | -6.0912 | -57.9187 | 2026-08-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 8afcbc80-3f53-33f3-b9fe-6146a7ce24b5 | -6.0913 | -57.8992 | 2026-08-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 06ff064c-f3c9-372e-96e6-cd2d8b6289de | -19.7446 | -57.9217 | 2026-08-19 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.7 |
| 2e85eecb-4d95-3570-8263-582ec40aee4e | -5.9198 | -43.6264 | 2026-08-19 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 241.4 |
| fa415528-06af-30c8-a073-4ad5c5c67565 | -9.3873 | -60.5721 | 2026-08-19 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3df752c3-5ef4-3e21-b931-648386296a87 | -5.92 | -43.6032 | 2026-08-19 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| ae2e0325-429c-3a15-8a68-6ecd6d205c16 | -9.4061 | -60.5518 | 2026-08-19 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 6c6f7840-7175-3f69-af09-0e6621c6b442 | -6.8593 | -59.0318 | 2026-08-19 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e4e3202b-d7d2-3ec4-879e-92433c1199ca | -6.0179 | -57.8437 | 2026-08-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c0aee86a-1337-310a-aad7-c748ae73a480 | -9.3875 | -60.5528 | 2026-08-19 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| d65fa2bf-843b-3778-86f7-355ef9958031 | -9.4257 | -60.416 | 2026-08-19 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| ba394f8a-c3b1-3391-9936-22b80cc5af5a | -6.6938 | -58.942 | 2026-08-19 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| b334be1c-9b8d-3e0b-87b8-bc0564696ce6 | -6.8778 | -59.031 | 2026-08-19 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 504bc2c9-2182-3151-9e20-e9b59e6869e3 | -19.7442 | -57.9425 | 2026-08-19 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 427.0 |
| da6f4747-de15-33e7-87bf-08796260b190 | -7.0577 | -59.8331 | 2026-08-19 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 48c9b120-7eab-38bd-8d08-c8555674b435 | -6.0178 | -57.8631 | 2026-08-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c8ace30f-5f3d-3371-8abf-f921fd049fb2 | -5.9994 | -57.8639 | 2026-08-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 59d4b69a-7ab4-3179-8269-73b81149d32a | -7.5488 | -55.5629 | 2026-08-19 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3e711ed4-3f81-3131-959c-5c9e7d3a86cc | -19.7639 | -57.9607 | 2026-08-19 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.4 |
| 6256a59e-5c6b-3d12-b84f-11a2e4659c15 | -7.5301 | -55.5839 | 2026-08-19 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e07cb128-da0a-3f84-b712-927d7d158ede | -6.7486 | -59.0364 | 2026-08-19 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1534725c-0c9e-3cfb-91c5-2cf80b721ee9 | -5.4319 | -48.3996 | 2026-08-19 01:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d8198b5b-545c-3305-a63c-fdcfff04cda6 | -9.4256 | -60.4353 | 2026-08-19 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 6f472451-1386-3fc2-be5b-9c703fdca84f | -9.0865 | -50.7979 | 2026-08-19 01:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 97f24245-796a-3ff6-abc9-60571d5ac0f5 | -9.406 | -60.5711 | 2026-08-19 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 100e4843-637d-3eb8-b857-678f83295fc8 | -6.0728 | -57.9194 | 2026-08-19 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f1f19208-d898-363f-94f0-6289cda4d835 | -7.5487 | -55.5829 | 2026-08-19 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e9baf4c0-55d9-38ec-8412-1e772162edce | -19.7241 | -57.9452 | 2026-08-19 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| c5eb1212-6863-39d7-a692-0c91ef7f3e44 | -19.7643 | -57.9399 | 2026-08-19 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.1 |
| 42bf4a5e-6b0d-3ef1-be2b-a3e53ed9c3ff | -5.92 | -43.6032 | 2026-08-19 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 01dfdba9-70f4-3ca5-895d-1b724b630c5b | -19.7438 | -57.9633 | 2026-08-19 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 9a61cf1c-dfd9-372d-a149-245b348cd16b | -9.4061 | -60.5518 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fc29198b-e622-3472-b73d-44f59c0a15ad | -6.8593 | -59.0318 | 2026-08-19 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 134ca6c9-61c7-37c6-b039-a5ead66738f8 | -5.9011 | -43.6279 | 2026-08-19 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 39595bb5-46ce-3606-a20a-1890b1570e65 | -14.0355 | -53.6808 | 2026-08-19 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4de0400d-c50a-3faf-95cf-f2be09db5e7c | -9.4256 | -60.4353 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8fa1d86c-b92c-3289-af05-1ec32bf5873b | -9.3875 | -60.5528 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| b32e04f0-415b-3ae0-b28f-5c0ebbe9b027 | -7.5487 | -55.5829 | 2026-08-19 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 40ab9854-89cd-3625-8897-ab7e160ba124 | -6.0728 | -57.9194 | 2026-08-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 2e6c9c18-d920-3e00-81f0-c8c0e96bdf4d | -6.6938 | -58.942 | 2026-08-19 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| afeddcd9-6e19-3196-b2ad-8df11e5fa443 | -19.7442 | -57.9425 | 2026-08-19 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.3 |
| 4b916f50-b57f-3dcb-ba28-39429aec08e3 | -6.0179 | -57.8437 | 2026-08-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 18ff2eea-c64a-374f-a39f-f267edc56023 | -7.0577 | -59.8331 | 2026-08-19 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 87cc780a-5360-390a-917b-ab2fb99e2e49 | -9.4254 | -60.4545 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| bce16f15-ed84-3681-99b2-67e5d93acd25 | -6.0178 | -57.8631 | 2026-08-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 0f1a4ed6-1dab-3d9a-a672-0f064c4768bd | -6.7123 | -58.9412 | 2026-08-19 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| fdcd8d91-5927-3f38-a8c7-fd74ae65715b | -19.7639 | -57.9607 | 2026-08-19 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 186637ae-dc4a-3f0d-b714-8210e20a6b0e | -19.7643 | -57.9399 | 2026-08-19 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 40f2bb77-3bf8-36eb-a1c8-28e81586639b | -9.0865 | -50.7979 | 2026-08-19 01:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |


[Clique aqui para ver as próximas entradas](README11.md)
