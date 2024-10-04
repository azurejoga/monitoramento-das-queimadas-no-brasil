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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f01e95ba-d7ed-3d1c-8962-600c48eb67a6 | -10.48795 | -48.18473 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7b92ed2-da85-3df9-83c5-96a8f0838526 | -10.4874 | -48.18824 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72524dc2-0423-3890-8402-2b4a27824f7b | -10.48625 | -48.17369 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e092a971-660c-3b2d-add6-e729602f7fa0 | -10.4857 | -48.1772 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a3d6bf12-4737-3d24-a1b1-fcbc59bb7058 | -10.48407 | -48.18771 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65b77dc1-393d-3683-83bd-6a04192b4ff1 | -10.48346 | -48.16968 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 40bce92e-bff4-36d8-927c-5b18040d0554 | -10.48291 | -48.17319 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2379fb40-b0a7-3814-af7d-da85705c44ca | -10.48236 | -48.1767 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ad8022be-63c2-3df7-a638-f05d629d3137 | -10.4729 | -48.17167 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fc288523-365a-3856-80ef-04dd4c10a5fa | -10.11608 | -48.8272 | 2024-10-04 04:32:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15bb648d-87fd-37f7-b189-8fea261c8bc7 | -10.11275 | -48.82667 | 2024-10-04 04:32:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a9500ef-a756-3ffb-91e6-7bd5043fe1c9 | -10.03677 | -48.21442 | 2024-10-04 04:32:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cde7633d-0973-344a-8667-0beca817a355 | -10.03622 | -48.21793 | 2024-10-04 04:32:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe60bfc3-34c4-37bd-a12b-dd3bc75af88a | -10.03567 | -48.22144 | 2024-10-04 04:32:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72ad7c33-e73a-3254-b7c8-2f925e5fe499 | -10.03344 | -48.21389 | 2024-10-04 04:32:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6911e65-d8da-37b0-8556-3e304f61bfcf | -10.87623 | -48.14087 | 2024-10-04 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d109d8ac-84d0-389c-bf8d-53659fca2d7e | -10.87497 | -48.39036 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4914eada-2c79-334f-a3db-0bf10038a4fc | -10.87164 | -48.38982 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| eeb1c0aa-e97e-345d-9f67-2cb878fcc337 | -10.87109 | -48.39334 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f95bd6b-2ec5-3bfa-903c-473b4a09b79c | -10.86831 | -48.38929 | 2024-10-04 04:32:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 323b1ea1-9f38-3f52-96ee-5dc5847a40df | -3.48755 | -48.90924 | 2024-10-04 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae4f1af-feff-392e-acee-e72fc57d1bf5 | -3.46608 | -47.66183 | 2024-10-04 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a03b8e72-33ad-34de-96b8-2dbdc8db820c | -3.46553 | -47.6653 | 2024-10-04 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 375bdfd5-94bf-32c0-a732-d28d3c964abc | -3.31656 | -49.04257 | 2024-10-04 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ea8eb79-05c6-3138-9924-6f7cd0da421e | -3.48814 | -48.90556 | 2024-10-04 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62d2e03f-8a9b-3fdc-b0e4-79b135aed54f | -3.46275 | -47.66132 | 2024-10-04 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b54ec51e-0c66-3915-a365-21d1a03d9b61 | -3.69626 | -47.61982 | 2024-10-04 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e32dc170-4140-3640-a132-2d7d8d1169e7 | -3.49097 | -48.90977 | 2024-10-04 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c27c3ad3-1071-385b-a819-2cfbfa531772 | -4.10382 | -48.48555 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be8375c1-c62a-3f72-a49d-01f82c10c660 | -4.09708 | -48.4845 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 14ae9383-baea-3cf8-b25a-fd0d3ee20ae5 | -4.09371 | -48.48397 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c57b1c4-d8bc-3cf4-881f-dfbada9351b3 | -4.09314 | -48.48755 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d59f4795-28fd-3b16-a1e5-a83c7100427a | -4.09205 | -48.47274 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae03693-18d3-3425-8a86-a7eb6fffa30d | -4.09148 | -48.47631 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9fdee567-d515-3a50-9de6-ea501487f48e | -4.09091 | -48.47988 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 74f2abde-45ff-36af-a5ef-a729466ead93 | -4.08925 | -48.46866 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe83afdd-0dbd-35f8-b378-93da7bd6269d | -4.08811 | -48.4758 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1bf2161f-55af-326f-a5b9-5c5ef7953440 | -4.08474 | -48.47528 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be3f70e7-2502-30e3-970a-679fafd0be04 | -4.08417 | -48.47885 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d8855b1-0770-3891-b58f-5d871163d96f | -4.08359 | -48.48242 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6a4b80df-e0f7-3e38-86e7-99e264b91b20 | -4.08302 | -48.48598 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 65dfef38-e379-3141-b04c-7a566a66291b | -4.08022 | -48.4819 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 977973fd-3d35-3cd6-b5e1-f59e6c567c34 | -4.06098 | -48.13805 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeff3232-1ea0-3738-980f-c9900b57442b | -4.02721 | -48.92131 | 2024-10-04 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95ec1fc1-c883-3342-bda1-75c3a34f3cf7 | -3.80683 | -47.80087 | 2024-10-04 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dd42c0a-360b-3fd8-a174-6e7201d4288a | -3.80294 | -47.80383 | 2024-10-04 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c32fc91f-1bb6-3949-9a16-71ded179ef03 | -4.82727 | -48.54725 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac9400dd-53ee-3ee1-80a8-c8de3529ed7e | -4.82447 | -48.54317 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4032e9be-cedd-392a-a4af-c398c6caab09 | -4.80246 | -49.07158 | 2024-10-04 04:32:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d56b39a8-b94c-37fa-a281-46b016d16e00 | -4.72436 | -48.83949 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6059f7d7-5a9b-3804-9402-51491b263ca9 | -4.71757 | -48.83847 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 051cb9ca-d1cb-3296-9434-09aaf2b67467 | -4.71699 | -48.84212 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d08f4496-69a4-3f42-922a-73ceabde7ac6 | -4.57429 | -48.01809 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 811d8729-76c4-347f-9170-4b1193325353 | -4.40207 | -48.62754 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed028e71-fa1f-3137-802d-e1249f122ac2 | -4.27891 | -48.06424 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98654f90-7990-35eb-b8f5-0e815be34843 | -4.27835 | -48.06773 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0b2ef5b-bdb2-3a7e-aaff-97c208645deb | -4.19693 | -48.22427 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2384bb94-791b-33c4-821b-ce6b7eb54660 | -4.19302 | -48.22728 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d5baaef-45b6-3309-8f02-407bf23330ac | -4.17775 | -47.89137 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0b5d6da-bfb2-3e85-925b-6180a53c97c5 | -4.17552 | -47.88387 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 205aa04d-5e31-342a-a63d-32d05a18531e | -4.14882 | -48.39784 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59e3d440-c4c6-3c75-a5a2-e0c0ad8f6d27 | -4.88322 | -48.98368 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14cf3ac5-90c0-3a15-a070-8e87008eb790 | -4.72378 | -48.84311 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3c36c4d-e3e0-3bf9-a20a-f080d8b8c617 | -4.61392 | -48.06372 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5babf40-2738-33ab-94c2-b2d9a7d807de | -4.57484 | -48.0146 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ae0bfc7-57d1-308b-88f0-be9e82ca0083 | -4.49097 | -48.1124 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba6aec34-6ce8-3edc-a8ea-fbebe11db0ae | -4.49041 | -48.1159 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01118663-a282-3269-89dd-fdcd40f8f39c | -4.39869 | -48.62702 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bae07a1-9664-3768-9028-a089cae976c3 | -4.38105 | -48.69402 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aaafc64-8d43-3514-9a8f-781a08d3b1b2 | -4.19637 | -48.22779 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 095006dc-b96b-3858-b0ff-63479e67b5be | -4.18163 | -47.8884 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2795469c-376f-3cc9-aa38-44045f1b0f31 | -4.1783 | -47.88788 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86835099-96ae-3b42-a9d9-db3b6f8f842a | -4.14546 | -48.39731 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ae5e153-5284-3d81-aefc-36fef5078600 | -4.10045 | -48.48502 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df79795e-4c52-3c2f-9319-14d99ff25a33 | -4.09398 | -48.27678 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b1a811e-71b2-3746-933f-dbc6e2fec6d0 | -4.09342 | -48.28032 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 469bc139-685d-331b-85e6-c9b2c744e79f | -4.09262 | -48.46918 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa4ae9c1-6ef8-38d2-9888-8f31d4339a8e | -4.09063 | -48.27625 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 153d5362-9164-3054-8da9-eecdaece7270 | -4.09034 | -48.48346 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 5f3c3b44-cf2f-3771-9a71-e8dbc44e5ecc | -4.09007 | -48.27978 | 2024-10-04 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91070a5f-cc93-3314-bc4d-f3f24ea23413 | -4.08977 | -48.48703 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 48ec25c3-e27d-3f43-b868-2dd001c91611 | -4.08868 | -48.47223 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b0d64ea-66ef-36e5-892a-a6f7e6e11b4a | -4.08754 | -48.47937 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b79962e5-53b5-3768-90d6-f5426e95654b | -4.08697 | -48.48293 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 679957f9-f2cc-3b4b-a9ff-cdb709597e99 | -4.0864 | -48.4865 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 53a056d1-5389-3bfe-9ec9-5fb9d79fb5c8 | -4.08531 | -48.4717 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1014f36-9b29-3727-844b-4ef49b2dd596 | -4.08525 | -48.49366 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| df32fe1b-49a1-359b-b8ea-bd2116939bd2 | -4.08245 | -48.48956 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2b6a6ff-2a7b-3fd6-9a7c-cf7c2cbd83a2 | -4.08188 | -48.49313 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 173039f6-63fd-3c83-b841-f539df761494 | -4.07965 | -48.48546 | 2024-10-04 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f09a3f3a-cebc-3c47-a00f-50a632887b6e | -6.00826 | -49.26396 | 2024-10-04 04:32:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1365ed3b-03c8-315d-bfd5-b5fa1698b000 | -5.79526 | -49.32817 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd12a695-e8f0-3764-a20f-e4c7599e5a02 | -5.79185 | -49.32763 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d8992f8-2644-3fd0-bddd-96e8b8bc4876 | -5.50861 | -48.8047 | 2024-10-04 04:32:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d44b904-6c00-347c-aed3-61e78129c404 | -5.50804 | -48.80828 | 2024-10-04 04:32:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 729b258f-4d48-3191-b068-6605bc7cc857 | -5.50467 | -48.80775 | 2024-10-04 04:32:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff7993ee-5a50-373a-a0f9-c22a39cf077c | -5.5013 | -48.80721 | 2024-10-04 04:32:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a5bbbd-1fa4-332d-b0a8-7fcb9d2ffeeb | -5.45689 | -48.99903 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3230eab4-c6bc-354e-916a-f19a2f4114f9 | -5.30073 | -48.11097 | 2024-10-04 04:32:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61d5a1fe-29e2-3e60-958a-6b1ba2bde2fd | -5.30018 | -48.11445 | 2024-10-04 04:32:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README104.md)
