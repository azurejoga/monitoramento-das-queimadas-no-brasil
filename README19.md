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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f32929d-dd56-3cbb-8711-9ecc30abc50f | -3.53629 | -53.80227 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d7a8908-b080-33d5-9475-cb8414b9b159 | -3.12155 | -54.50031 | 2024-12-28 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a60679b-7ec0-3227-8d66-af49deea5350 | -3.56989 | -50.67463 | 2024-12-28 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c040c68-245b-3405-8dbe-78bb2e3e084a | -3.94093 | -46.98325 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0f4db3b-6b7c-387c-9baf-5373d1f07c4f | -5.63982 | -43.72345 | 2024-12-28 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 264b6c4d-e9ae-3517-85d3-12f551dd3634 | -2.78718 | -48.09793 | 2024-12-28 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c8c2ba-f77e-39ce-8d95-1fd14227543d | -4.08172 | -47.09289 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 543c41ac-18c9-3fbe-b2c5-19a99381c185 | -5.42699 | -44.8322 | 2024-12-28 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 25c4b31c-d1c2-3c82-a56c-2810609a795f | -2.41631 | -54.21691 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6aec318-6a97-35a7-b436-caa175f7dd33 | -3.99353 | -46.91803 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70ff84ac-04b7-388e-873f-f371d4550cba | -6.44477 | -44.38331 | 2024-12-28 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f1b8381-8ccd-30fe-b8e4-4f4d6182b22c | -4.23148 | -46.80213 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9432aafb-1c3f-3229-ae51-80ca6101ee17 | -3.91987 | -46.88062 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef0e0b4f-515a-3a06-9e9c-ab01557a9f3a | -3.99049 | -46.75441 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16fad7cc-8f0b-376d-9256-4f8f33a03412 | -3.97468 | -46.34642 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d24b943-2132-350b-8913-19e627185955 | -3.86647 | -47.01833 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec1f13a9-0e12-363e-8746-4fe1e725038d | -3.75784 | -47.2221 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72f11c81-e403-33c0-aa9b-7a31069f88dc | -3.92713 | -46.98111 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ea3d7e68-7d54-31db-8bfa-eeb28788fab8 | -2.63036 | -48.08808 | 2024-12-28 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7180ca1c-097c-3c53-b4ea-532cfb9e6781 | -2.26464 | -53.88311 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfdfb260-6b8d-3d7d-b587-6e7316930233 | -3.89461 | -47.01892 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49821bf0-fc4a-3b49-bb05-548ce90aff01 | -5.23446 | -41.39433 | 2024-12-28 04:38:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8af3dbb9-b1de-3a0c-b283-063d57c6beaa | -3.18929 | -46.00106 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98060d80-6927-3387-9b44-badc8f72dfe2 | -2.37693 | -53.88141 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1c3d60f-f917-3490-894c-6a5b8c21506b | -3.98102 | -46.55961 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97f4ee75-316c-3c85-b000-061b6d52748b | -4.75796 | -45.70642 | 2024-12-28 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 147d5834-9fd4-3e65-8d12-ef1ad682a112 | -2.477 | -54.16425 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2cf7221-e726-3fc7-be80-25a7203a6874 | -6.7092 | -44.32037 | 2024-12-28 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b541fc8d-7680-3595-ba3d-fcd2212c6736 | -11.13704 | -43.29985 | 2024-12-28 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7d472777-eaae-37bc-94cf-ccfd5bd9c979 | -10.43054 | -44.89301 | 2024-12-28 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9465b6d6-5fe2-36bd-8351-4dd8df7c99e4 | -9.5507 | -40.91304 | 2024-12-28 04:40:00 | NPP-375D | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90f01e17-cce2-3c83-8c14-b34da13a77b7 | -11.248 | -44.47788 | 2024-12-28 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74ef8fc-21a7-35ae-9bc9-838af38a978a | -11.13638 | -43.3049 | 2024-12-28 04:40:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c04ab55d-3112-31b6-9f9b-9ae8d5074c02 | -11.24741 | -44.48214 | 2024-12-28 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c88b122c-eff0-3681-9789-b0e8e989522c | -9.23563 | -60.32954 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7a6f04d-7ad0-3f2f-a8de-410858c77e97 | -9.55656 | -40.91053 | 2024-12-28 04:40:00 | NPP-375D | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c381badb-0734-372d-8085-733c0917632d | -10.43109 | -44.88914 | 2024-12-28 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c3494b4-132d-3fef-803f-d3789c19d15e | -8.98508 | -40.62024 | 2024-12-28 04:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d150c7e-c282-38c3-bf32-cf99258c7b32 | -10.60277 | -44.98347 | 2024-12-28 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e33a01ad-4505-35c6-a045-7f80f91deb03 | -10.67173 | -45.0119 | 2024-12-28 04:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 637c3a27-01d1-3a27-81ee-8275703e4db8 | -6.71599 | -44.15538 | 2024-12-28 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a33e295e-549c-39a6-8c78-d6008d209b54 | -8.12227 | -43.14296 | 2024-12-28 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d34ce0ae-a2bf-313c-bb41-25b22cab4942 | -10.68842 | -45.01448 | 2024-12-28 04:40:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec66ff41-42b4-381c-8932-da47cd39be8a | -9.55613 | -40.91384 | 2024-12-28 04:40:00 | NPP-375D | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2ba4139-a32a-3db9-b5ac-541f2d8b3f32 | -9.23855 | -60.33574 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5903dc34-0a87-399e-83a2-2fb1a5dd91b4 | -8.69347 | -44.32892 | 2024-12-28 04:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e26baf0-c610-35e6-80c6-0f2a67e0bd2c | -9.24128 | -60.33062 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc477753-5f13-3794-9c88-ac4ce85c9e0d | -9.23925 | -60.33191 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c87f469d-86a2-31e3-b799-aa39958dcc5c | -9.23361 | -60.33083 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a79a1771-3ef6-311d-ab06-3261cff337da | -7.26576 | -45.36924 | 2024-12-28 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e087da81-9d02-34d2-995a-28e1fee661b5 | -9.2349 | -60.33338 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e94ad7dc-cc58-37d0-9392-663af4650a9d | -10.21714 | -44.76183 | 2024-12-28 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5afa37f-9032-3b3b-822b-358949eb91ba | -6.70976 | -44.31652 | 2024-12-28 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d93ebe4c-aa91-351b-9426-7243d4cc5be3 | -8.9846 | -40.62387 | 2024-12-28 04:40:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 60689dae-e68a-38b3-9851-1ad96472209b | -10.60224 | -44.98733 | 2024-12-28 04:40:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4d22d14-3e27-35ff-a9dc-4b09948f9ad0 | -8.62555 | -46.02675 | 2024-12-28 04:40:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bcb7f54-0173-3791-b281-ae275244f226 | -9.23431 | -60.32696 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 396003a9-029e-301b-b2ed-0e8580b183b2 | -9.24055 | -60.33442 | 2024-12-28 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca0ceda6-aa84-3ec6-ba62-d03fdba7ff08 | -8.62936 | -46.02729 | 2024-12-28 04:40:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fbf7d0a-2b90-386d-b5e1-8e463025da8e | -15.55203 | -57.78691 | 2024-12-28 04:42:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7da64a64-c124-3016-8a0e-41a13493a439 | -15.09336 | -59.62776 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9daa11b7-ada7-3053-9c60-5eacbd4aff0a | -16.10385 | -60.07171 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 364d2b8d-2824-3eeb-a4e2-a18f56938889 | -15.51755 | -59.42381 | 2024-12-28 04:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f61a1ba6-92a3-3bca-9d7e-032168d1bd27 | -14.1041 | -59.94207 | 2024-12-28 04:42:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 96525dfb-b6ee-317f-aa96-52aede0d9a20 | -14.10973 | -59.94006 | 2024-12-28 04:42:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d90e3fd6-e1a3-3341-8ba1-1e8b8a039343 | -15.02369 | -57.85431 | 2024-12-28 04:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08fc3e20-414f-3098-8855-abc53a76ddff | -15.09504 | -59.63234 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cec44e71-44a1-3fe4-aeba-8d5920082f68 | -15.5528 | -57.78284 | 2024-12-28 04:42:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbd10c85-a54f-3843-902f-bbca4610c632 | -16.203 | -56.81847 | 2024-12-28 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6568752-f955-31ee-86fe-09626e9a4e1e | -15.53941 | -43.14264 | 2024-12-28 04:42:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bdd4648c-a367-3f73-be2a-019c6dcdb01e | -15.0902 | -59.63124 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc090f50-5709-3a01-ba14-96f90e34cc16 | -16.1027 | -60.0775 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b2418a01-008b-37f0-b008-010549ad23ad | -15.48955 | -60.04768 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c85d5936-80f5-3418-85c7-5572e55efe85 | -15.51856 | -59.41852 | 2024-12-28 04:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3338cec0-a134-39d5-ac01-eb8f9c80f2f5 | -11.96979 | -63.51114 | 2024-12-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 408ca70b-037b-3e87-aad0-d5b24fbcbc03 | -16.09963 | -60.11859 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d593efd-e6b0-3a2e-a621-7e7fe6056b81 | -15.27546 | -59.88021 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f021b64-8c73-306c-8439-787a4fdf42b6 | -15.09609 | -59.62683 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6bfd9a6-b1a4-339e-a3f9-64a20fc23774 | -16.09894 | -60.07069 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 67bc1f19-c3c7-356b-bea3-2bc054c51a89 | -15.26942 | -59.88487 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94e15a99-2d03-3748-a56c-8d1e826535b4 | -15.09124 | -59.62574 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 91c3a06f-fe79-3d8c-add8-eaece72db4a3 | -15.27434 | -59.8859 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1395b60e-7877-335c-9634-84443ec78964 | -15.27054 | -59.87919 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49190534-57b1-31d5-a4eb-93f801840807 | -15.27926 | -59.88693 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a7728a9-bea6-399e-8627-6badbb78d5c9 | -16.09778 | -60.0765 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5abe7d6a-d0bd-3dba-ac84-dd39fed34457 | -11.97632 | -63.51252 | 2024-12-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a7b1e1d-2269-32f5-9be3-0b88c219617c | -15.4846 | -60.04663 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 166b4696-e35f-3106-9b7d-003b9e17a1d2 | -15.2853 | -59.88225 | 2024-12-28 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a45afb95-e797-3c98-88be-5a7659bc5b7e | -21.32905 | -56.11675 | 2024-12-28 04:44:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 667954b3-b0b7-3799-aafc-ac2c3cce6646 | -21.63325 | -53.42657 | 2024-12-28 04:44:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d20c69e0-f8ec-3bae-9682-10d6683d4554 | -20.59876 | -51.60847 | 2024-12-28 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5b5017c-15a3-358b-adc9-00e4ed855345 | -19.92138 | -55.7397 | 2024-12-28 04:44:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5bdebea8-e0a2-3827-8f1e-9312c6d5a848 | -19.02355 | -57.62083 | 2024-12-28 04:44:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e9f7b3dd-3231-3ad3-8877-35d75202667d | -22.30887 | -53.85128 | 2024-12-28 04:44:00 | NPP-375D | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c20bb26-e881-3f3d-b3d3-83ae94b48a4b | -21.20167 | -56.91906 | 2024-12-28 04:44:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bcc0e17-8d60-3038-9338-ab71fffd5c28 | -19.92312 | -55.741 | 2024-12-28 04:44:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a18986b7-da79-3c54-a389-9e9ad9c2b43a | -20.47773 | -53.67418 | 2024-12-28 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 842eda23-3722-383e-a902-92680483cd7b | -20.995 | -51.79397 | 2024-12-28 04:44:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 32cc269e-a6d6-3eee-9846-ce297e50cd5c | -20.26194 | -55.13717 | 2024-12-28 04:44:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 144230c8-e0e9-331b-a4b9-37147ef006f1 | -20.07475 | -54.90128 | 2024-12-28 04:44:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)
