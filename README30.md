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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5448bc09-3f75-33c2-a7f4-d53ee350d1b0 | -15.26774 | -56.49195 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3eb6d8d-36d5-330d-b0e5-7e575c435bb8 | -14.03314 | -53.681 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8cacd6e4-1dcc-3bff-8119-479502ff8148 | -12.40163 | -54.96438 | 2026-08-18 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b389cc0d-b44a-377c-8a1e-5aa8a03f7468 | -14.17144 | -52.88932 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6475ffb-7a40-3b0d-91fc-b7e8709d5e0b | -11.19864 | -54.81294 | 2026-08-18 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ccecff5-d550-3ac7-b00b-d36d51048ecc | -14.80613 | -46.64443 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 99123319-c499-3bf4-907c-a1288a27bd3f | -14.17351 | -52.90061 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a477dc06-e789-3ae9-bd58-6c51be2f8ebe | -11.20243 | -54.81866 | 2026-08-18 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8399210-ce9f-3692-a9b6-b2e0de63b699 | -14.83677 | -46.64965 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98152c92-08e3-37bd-9a10-df80524772e9 | -14.05377 | -53.68481 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcfe0fc9-bf6a-3baa-8b27-6741473a2763 | -11.13272 | -46.49365 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06baad11-e351-3cce-99a8-a39cc19131e8 | -12.54478 | -47.84543 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cae62ac5-8f5a-3c96-9c8e-c18e81d6b836 | -14.49293 | -45.67264 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e4bdbb5-21b0-3c76-9a22-e20434e4bc61 | -14.19081 | -52.93316 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| e871de35-099e-336c-81e1-4b0ad50da282 | -14.84469 | -46.64339 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9159ed4c-310a-3d72-9da1-cd111044252f | -15.38588 | -52.796 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abb27b9e-ee99-322e-8a92-56d49693e64c | -13.41473 | -54.32911 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fff674b-72d0-3aba-b3bb-2afaf382a122 | -14.1869 | -52.93237 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| cdaa1ce7-6ab0-3d0b-b239-ac4fafa14a89 | -11.18868 | -49.68756 | 2026-08-18 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7260942-bb87-3a72-9d6b-a1b4a94736b8 | -10.77134 | -50.36773 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0ca929f-946f-337f-8bfe-c26fb9f14881 | -12.01425 | -46.499 | 2026-08-18 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 874b794c-2dd9-3001-9491-a0ad001f4b5d | -13.56331 | -51.77399 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c95db904-48e4-3dd5-8198-e57f29d15001 | -14.22934 | -45.41073 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4250c495-10dd-36c9-9553-bdc8c5518254 | -11.11046 | -46.49432 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71815fa7-f406-3190-b664-578fcc5e4395 | -10.14894 | -54.27769 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96c8c94f-e127-3a3e-8c4e-bdab8d39c76a | -9.1661 | -59.67498 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9552011-4b29-3a7a-b0ce-1b91ec8866b0 | -12.71288 | -48.49109 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56b2c4d5-fcd6-3ba9-973e-a77aaa598d5d | -11.47027 | -46.56557 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23cb9743-bc48-37a3-a16e-91cd3d608fd2 | -14.47547 | -45.67139 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a43cc63-b204-30f7-9343-69c7e61c2909 | -14.8521 | -46.64061 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 198a7519-5253-34b7-8ee1-f3c06a7a08b9 | -13.02269 | -56.59135 | 2026-08-18 04:40:00 | NPP-375D | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd681a0c-f75b-3a2c-941c-fbbdddbdd216 | -11.18932 | -49.68372 | 2026-08-18 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9afc5a4a-1d5f-3f76-95e1-2b829b5f1a0f | -16.17638 | -55.95146 | 2026-08-18 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f7d3cad3-16ab-36f4-a0b9-b15cf21c4bf7 | -11.62605 | -46.77989 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f1ce297-209b-392a-88dd-b8621ce35020 | -12.39702 | -54.96345 | 2026-08-18 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6265191-0c88-3a79-93a8-fcc808f0f504 | -10.14351 | -54.28161 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a65d9a6-fc81-382f-ade5-9e3c03789624 | -14.35751 | -51.88177 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b533698a-c8e8-306e-a977-8fd321bd42a3 | -11.49388 | -45.10517 | 2026-08-18 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 126fa70a-b1a3-337b-a0ea-8e6501f096bb | -11.3234 | -55.23167 | 2026-08-18 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b35edb58-c778-3f12-af31-4f42242945fe | -14.17291 | -52.89773 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2aab3b77-63b4-33b1-b7bc-b6c6830416d5 | -14.03922 | -53.68596 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 944e869d-c3bd-3a03-bbf0-d9d17994a044 | -14.36167 | -51.86728 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f6686c4-40fc-3e3a-8e12-4c2dfb423add | -15.02003 | -52.70234 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44bc1cbe-aa19-3044-ab58-f28b85e02aa3 | -14.42359 | -51.88325 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75d7fb95-ef1f-3a6b-aa85-10e071f6d514 | -13.41988 | -54.37444 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39ff2540-f99c-3316-8e42-c88211f01ced | -15.39119 | -52.79984 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3342e1b4-b263-3015-8ab6-854b5e37ae5d | -14.16571 | -52.8989 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a144024c-4b0b-3916-8164-e8b4d75f1e64 | -13.4085 | -57.0544 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fe7fb07-53ea-344c-bb3b-2a0c37e70496 | -14.16663 | -52.89369 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 46678c0b-cb57-381b-9ff6-77ea6e733226 | -10.14787 | -54.27967 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 735ff61e-5562-3f29-8b60-4e7b3eb696da | -11.8731 | -50.21787 | 2026-08-18 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b676069e-e738-377d-92c2-ef6809727d07 | -15.91763 | -55.55319 | 2026-08-18 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86641a1f-2f4e-305b-964f-ffc1ef4ee97f | -14.17626 | -53.05888 | 2026-08-18 04:40:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 882e4129-cebf-3f00-b87d-c29bc31fa734 | -15.26398 | -56.48545 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2cee018-8ba7-37b9-80b4-daff28b1d9c6 | -15.22951 | -57.65608 | 2026-08-18 04:40:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 066c7c8c-bccc-360a-8280-14b8ad1684c9 | -14.35434 | -51.92264 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44bdf091-7ec0-3d66-877a-a0560d6aad84 | -15.91678 | -55.55762 | 2026-08-18 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dded4dad-c117-3100-88f6-b36180757ee9 | -14.63119 | -54.46284 | 2026-08-18 04:40:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66721304-f659-3a83-a305-1e5cb685bd3f | -14.18299 | -52.93158 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5850421b-b97d-32ba-ac9f-ba62dcff87e7 | -14.25784 | -51.92835 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2e0cc45-09fc-383b-ac5e-90ff3e13b401 | -14.17305 | -52.91925 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c612e0d6-38a1-324b-9bbd-81d5374fd3fa | -12.72012 | -48.48865 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad35e877-e824-37d3-916c-a46ddfd5a8b5 | -17.45317 | -47.856 | 2026-08-18 04:40:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4f2e86f-6b29-3b97-b8e1-b86394066e3a | -14.17721 | -53.05363 | 2026-08-18 04:40:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6b5d2b2-6833-3873-957e-31589c40374f | -13.44226 | -43.84151 | 2026-08-18 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88b6a581-4ed5-33f8-a48d-627f84563409 | -14.28299 | -51.93763 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca1bca43-e9e5-3b31-baec-16903404dfb2 | -13.57675 | -51.76258 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a078ef84-ecbc-38cc-8270-ca5ab5d5c765 | -11.35585 | -46.38187 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22912a15-b964-38df-8af3-9d90444a01b1 | -12.53145 | -47.86499 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbb8a965-e863-3916-a7ce-b53b6ad7888b | -14.44834 | -51.82793 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daf04728-2289-32ec-b7f5-01d8c06d27ae | -14.17998 | -52.92576 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d1b6f155-dc27-3bda-a0c4-550dd35d8496 | -14.43234 | -51.8987 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4353c279-7349-3063-a70c-0bf5847d87aa | -14.47899 | -45.67194 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b388b7a0-95c5-3859-822e-36084003fe62 | -14.18167 | -52.92352 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 7805f3e5-78c8-339b-8c60-246aa3cd6141 | -12.94293 | -56.6478 | 2026-08-18 04:40:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c8258e2-1706-30c7-8a01-4ac23afaab99 | -11.12479 | -47.28275 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e11c9829-6dfe-3606-aee5-ce3f0ef8a547 | -13.40879 | -54.33688 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80279e36-bf67-3f7a-83ac-088be6f273f9 | -13.41908 | -54.3299 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb8d4207-601a-3b7c-8123-d796b923db6c | -14.3055 | -47.18279 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a28557b8-b7c6-3473-a72e-69a2183e8034 | -15.28938 | -56.43312 | 2026-08-18 04:40:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 015b6d0e-ef69-3024-b05b-6d1739c957ab | -14.45202 | -51.82859 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f767eb57-5f41-3aad-8807-fd81678f6b67 | -12.73917 | -48.45512 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1562a4b-e641-3e28-a349-1c0a0a2e9638 | -11.50492 | -46.60764 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 197e1f12-9bad-390f-9fdc-16b3cd01a50e | -10.17644 | -54.22685 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0db177bb-7480-3ca7-a764-1248ed9061cd | -14.80444 | -46.65571 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be266698-f385-3ef1-a939-eacf2f72373f | -14.86974 | -46.63945 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa86cbf6-a47e-39bf-b4e2-ef621c9f6c99 | -13.45771 | -51.80317 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 945e3841-c5c4-3cf6-81e8-200e73f8d7e7 | -14.87771 | -46.63299 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a89e971d-36f0-3337-ae9f-c0cc4e5f8c8b | -14.04967 | -53.68393 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 49c83cf1-97cf-3d03-b2e8-dfc2d6fe15e9 | -15.3793 | -52.77745 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25772bd6-efd6-3c24-9942-bf334edf15a4 | -10.51431 | -50.78671 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3703a203-987c-358b-9254-44ca7c9f70e3 | -12.69771 | -48.52154 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 582702ac-3048-3fbb-94ac-c8d87f93603d | -9.42379 | -60.41884 | 2026-08-18 04:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43ba3cf8-2bad-3f2e-a29a-b1e74981f905 | -13.46173 | -57.05855 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 803141d4-f05f-351f-9d8d-dc94cab2d98f | -12.00571 | -46.41964 | 2026-08-18 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 549268c2-a245-3f3f-843f-599659412b0e | -15.38971 | -52.79668 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3294375-4ad2-3db3-a41d-8197c45cd502 | -14.54536 | -48.15945 | 2026-08-18 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7414a230-ea44-3895-a33e-39546e3329e8 | -10.51723 | -50.79175 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 101db0d0-38f4-31f8-b45a-4352fbe7b12d | -13.78813 | -48.49755 | 2026-08-18 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1aa25d4-af4a-32a0-9b34-9d197f108e05 | -15.39205 | -52.79491 | 2026-08-18 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README31.md)
