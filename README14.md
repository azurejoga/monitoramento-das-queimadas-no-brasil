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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31990c73-f5ba-3d60-8315-9d7e7769da80 | -6.23016 | -44.16728 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e51c4374-6826-34ce-a158-707c00e663b5 | -5.61357 | -42.72585 | 2025-10-15 03:47:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b0fe27b-c100-34b6-9c94-8869d5cc2944 | -4.90261 | -43.45692 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 72a42b26-baf6-34b3-8e36-749568c8f93b | -5.99634 | -44.08865 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef9b4dfd-50e9-3356-a56b-6f4654d6b21b | -4.5923 | -47.03415 | 2025-10-15 03:47:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b263de92-6b14-3f94-8581-6dd3958159f9 | -6.45415 | -41.8903 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa0d53e3-8587-3f8c-bafd-1f9ed587ec20 | -7.49949 | -42.14058 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 00da3654-d5b0-3b5e-bc33-9f3e9fcc1ebf | -7.56576 | -43.83934 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a05e695-7ef5-38f0-a4f5-726ffc1628d9 | -6.05421 | -41.89644 | 2025-10-15 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 29848c05-a6d3-3b0a-b955-f96af8dc66eb | -5.42499 | -40.98685 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5a1fa275-d30b-38c4-9a9b-b45916200693 | -7.16388 | -42.49978 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 678579fd-c3be-3eda-b430-624507c885dc | -6.05988 | -44.09255 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 915fbfc5-f352-3623-9012-c5aebf4047a0 | -5.33962 | -42.56439 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3f800ed4-c055-3af4-a608-305de8a71dfa | -4.86364 | -45.67413 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507814d0-7049-3173-84e2-dae6a3f5f784 | -10.82252 | -47.98347 | 2025-10-15 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f78b171c-4d58-39ae-a159-00ecafecfe06 | -5.86762 | -43.87212 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84d37a83-7c5f-36d4-b753-195483d20913 | -5.92447 | -42.82342 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| e2975641-8b1f-306c-a3e7-8d44f209df83 | -6.37314 | -41.49908 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 39e17ea0-6065-30d6-88da-0b0479b3b118 | -8.20127 | -43.98749 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26e54fce-2d7a-3c99-8c20-9d4fad2e1b96 | -6.89387 | -43.96314 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1edf603b-b28e-326d-afe7-d5eea25fdc5e | -7.03168 | -42.74219 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af46b3d7-2efd-3d4d-9b27-fcb6364610c9 | -5.57092 | -41.32054 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4841b400-55eb-32b9-b6e8-7f511ef9a00a | -6.2582 | -44.34192 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a8c2ab3-7fb8-399c-b69d-476b92722991 | -6.90743 | -38.26133 | 2025-10-15 03:47:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9d926b6d-fe16-3caf-ba0b-3c63ea60380d | -5.86376 | -43.86122 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6857dfec-e5fa-3d4a-b8c1-fa8876f0b8fb | -4.91508 | -46.71215 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75ff9b5a-4dc0-3928-8e4e-da83b9e43da2 | -5.87035 | -43.85673 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb30813f-5d2f-3997-b412-54a951eda11b | -4.87264 | -45.77634 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6616b370-6945-3592-8a85-0e5fd3d32436 | -5.94685 | -43.7552 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d5e5157-eb28-3c33-bbbb-3dc2e50e08a7 | -8.22245 | -44.093 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e534741-90ce-3f50-8206-4e17e46a4eae | -6.89334 | -43.9662 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c04c337-bac0-3b8c-853f-ec77153cb928 | -8.46158 | -44.19355 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e47daa64-261e-3131-ad4d-60d04382cd51 | -5.34115 | -43.74746 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c401b979-adf9-3358-b7da-a3a6b700f1aa | -7.04922 | -43.97106 | 2025-10-15 03:47:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f56f5c8-2647-379d-b841-3599d2761d97 | -5.38769 | -43.22586 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d997e042-3848-32d3-9671-b35963c0dc75 | -6.0279 | -43.39755 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14d6b531-03b5-3e6c-9f20-2eb6a806bb56 | -5.88944 | -43.74888 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ada8343d-d16c-39e0-a1d6-b63525332b46 | -5.57797 | -44.74376 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ef9a6b-e858-3e98-99b6-74870e4ee2d5 | -4.39693 | -43.62048 | 2025-10-15 03:47:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 123b707d-dcc7-3e69-887c-26af5478278a | -5.59263 | -42.84475 | 2025-10-15 03:47:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e9ee3a4d-ea1e-3024-85a6-90b37ff1e206 | -4.8964 | -43.46223 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 176beab4-516a-36d0-85f3-299ed058c049 | -7.258 | -44.91639 | 2025-10-15 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f5a28b2-c9ee-3970-8041-8283a535d39a | -5.87441 | -43.86407 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fbd6707f-496e-3b53-abe5-1104bc7adcc8 | -5.41415 | -44.22461 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be87b9a7-9598-32fc-9304-28abf925a63f | -4.89836 | -45.50932 | 2025-10-15 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7e0a964-1d55-371a-a884-c734bf8d31a8 | -4.66263 | -43.1255 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 93436c74-699c-3e8e-9a7a-631f2ed0a76f | -5.86816 | -43.8691 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5b85813-3df1-3152-965a-c8b830f7a58c | -8.20313 | -43.998 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed386556-73b1-39fb-bfd4-ca44193c3a95 | -5.43561 | -44.22853 | 2025-10-15 03:47:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 7e4fc6c6-4280-3f03-a467-d0ffc1b326da | -10.16749 | -36.17774 | 2025-10-15 03:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 80610be7-a9ac-3ec8-a378-9e28e7dd68de | -8.21898 | -44.08319 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63118ce2-afb6-3549-88e5-d3985bb2955f | -5.8767 | -42.82461 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5dc95b29-73fd-38c8-8ed1-391ca6c41610 | -6.17399 | -44.3022 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3ce01dd-6c0d-3b02-a896-3401a9fa0e23 | -8.2153 | -44.04577 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13f67376-54f0-383d-a8c7-017ba6fe5c31 | -7.01915 | -41.95616 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 042af468-76b5-35d3-b9f1-4bfab3096927 | -7.4843 | -42.65273 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 382ee859-b885-3e3a-8c78-a54a02d6902c | -4.9103 | -46.71368 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3129111-112b-316c-aa12-020cb39422ac | -4.80033 | -45.71933 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 268de87c-f35d-3fbd-b213-4f4ed323736c | -4.65758 | -43.12465 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bba656b1-dcf1-38c5-a8e1-12fe7300fe37 | -6.5862 | -41.51516 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3020ab15-caf3-3ef8-a1d5-dc4f90beef41 | -5.17112 | -45.16994 | 2025-10-15 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ddd1551-f78d-3ccf-8e80-50cb1902cc5a | -6.17147 | -42.61814 | 2025-10-15 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 92d69322-02f6-369c-9b2c-9a66e7477b15 | -8.18823 | -43.9729 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e996d8c0-bd98-36f0-9f74-ece282029888 | -5.91207 | -42.64739 | 2025-10-15 03:47:00 | NPP-375D | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| de9896a1-768b-3ea1-b1e9-e5e9c9771ee3 | -7.5714 | -43.83686 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 297b78b9-44fa-3499-b79a-e88a6057f5df | -6.23597 | -44.16511 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad6c0fbc-f593-3628-9e5a-ca5d63e0b186 | -4.82402 | -42.77702 | 2025-10-15 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c4b5fcc0-27ea-32a6-afc6-791ddda17711 | -6.45979 | -41.83064 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8bcee173-2442-385b-957a-150451ff6a5f | -8.20425 | -44.00021 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54898b0a-ce0f-33c8-969a-475cf7b1f4ec | -4.65054 | -43.1355 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1bc36150-0f02-34ca-947b-adfef0330cdc | -10.05847 | -42.61642 | 2025-10-15 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 10a3054d-32d3-3bad-8e49-1e014b8d6a2a | -7.94978 | -44.14715 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2488450-2164-36c8-bd5e-1821c2718c85 | -7.94494 | -44.13169 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bea2c75d-72c4-3d62-a414-e762698568e3 | -5.53871 | -41.32951 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d116a1b-316c-3c33-ad4a-e682d5a3539d | -11.88414 | -44.78623 | 2025-10-15 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b106e110-a482-3349-b9c7-ce5d608ee6ba | -5.25992 | -45.60918 | 2025-10-15 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f667b6d3-c58f-3e65-ba36-3ea407a02815 | -5.44154 | -44.22624 | 2025-10-15 03:47:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6c50b6ab-bff5-3bf9-b986-938eb82b56d9 | -6.21754 | -42.49484 | 2025-10-15 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f142d51d-c38f-31dc-b285-620e302234c9 | -6.14573 | -41.77273 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a92a4d9b-8f36-38c9-8e30-0a1b79435acb | -6.8391 | -42.77946 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 92f434d2-13e5-3a6f-88e7-9254132237ec | -4.86954 | -45.67553 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 00820990-0fb0-33b8-9abf-39209e9406ad | -5.92207 | -42.82191 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 14db3b4e-04e3-3b6d-af98-b3b4b38827b9 | -8.24002 | -43.33844 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 260d12a9-a9da-36b5-90ef-d41a7446dd0b | -4.90669 | -43.46402 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 5f824ab4-3a83-3424-8a31-9d65e66e6d6f | -5.24696 | -44.47019 | 2025-10-15 03:47:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d90bbd8-767e-368f-8a27-8432171fb971 | -6.13984 | -41.75325 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ca3f1642-07b7-34b9-b6d3-7e2ac974a8ea | -5.56575 | -42.99045 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef5517f4-7b08-3fe5-94f5-a495d0fb189a | -7.57088 | -43.83985 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8e66b8fb-b84a-38c0-90a4-6aeb0f828a53 | -5.44096 | -44.22959 | 2025-10-15 03:47:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d521a280-d406-326b-acaf-f115a30aa912 | -5.86274 | -43.86726 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 368c8e36-3001-35e6-9054-583543c485a8 | -4.90963 | -46.70592 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27801c2d-dc1a-3ce4-a885-29227217deab | -5.866 | -43.84801 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a603d16-ad56-38e3-b601-d287b1a1470c | -6.17665 | -42.61768 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 83168a46-f90f-3bb3-8308-d5cea3362ddd | -8.2206 | -44.07425 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0002585-7f6a-3dec-ba9c-724d75576c24 | -5.91299 | -42.83185 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9a917d29-5422-3074-a286-09a3c27354b8 | -8.2613 | -43.3587 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 549cf4f0-0309-3722-8351-6185c7da0e4f | -7.50248 | -46.64065 | 2025-10-15 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ea4fc5b-3c0a-3cc7-9b63-91f3b703f8a2 | -6.19713 | -43.28439 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52903f27-2c5c-3038-9961-257bb8f49106 | -6.28079 | -42.97908 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1db1a9c9-9cf3-3746-822a-7d64eb4a3c4b | -10.82137 | -43.95506 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README15.md)
