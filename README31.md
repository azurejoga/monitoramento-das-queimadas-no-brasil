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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32c75c32-4c90-3978-a7f4-b9e666132a87 | -6.61718 | -44.94216 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86ee401f-27ac-3ce4-abf2-2d8c67750d31 | -7.70898 | -46.818 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20ce4f2b-1070-3cd7-bb40-7c112642246c | -8.5267 | -44.62284 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c1eb3d3-8fe2-35df-84df-3c8f09bdea4d | -8.00654 | -47.03616 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0fa48345-a083-3e9e-8dfc-cb1163eae967 | -2.70147 | -48.83591 | 2025-09-29 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cd5a48a-cd90-3161-9ef7-a9510229bea7 | -6.81935 | -44.91929 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68be368f-7345-39d4-9dbb-ab906fcf8545 | -7.31426 | -44.71733 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adbc9182-5932-33ad-9e06-a4d54e51866e | -7.50077 | -45.42545 | 2025-09-29 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 245ab562-70f5-370b-b0f0-f23c0ac026e8 | -6.47191 | -42.92212 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82e9c159-9e9d-3eaa-b95a-825e4f29ad3f | -6.24685 | -42.46074 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d7e87687-60b0-3bec-ad96-c857e0c5a9e5 | -7.36953 | -47.04509 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58b568ba-7d04-3028-b149-f0e2873b1cba | -5.79955 | -42.85244 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1ad66b02-2241-3994-ae33-5832d8f30789 | -6.1218 | -41.81385 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0302176-a08b-3386-9222-28ad626060c2 | -8.63486 | -43.99208 | 2025-09-29 04:06:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92717df0-f74d-3245-90fe-dafeccfcc7d7 | -5.67715 | -45.28892 | 2025-09-29 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fd4dd2d-04c9-3516-a5a9-809e482c19e8 | -7.61829 | -43.79534 | 2025-09-29 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42d6287e-28ce-3d74-89c2-a4af9ee0f653 | -7.02927 | -44.78209 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83cedc22-b595-3f14-bba4-db5fdc810e0e | -7.39318 | -44.46233 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a306184-d88d-3ca2-a3a2-c398f91fa05c | -8.13876 | -46.40936 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09069dce-ce0b-3453-ac2a-3d8894fea81d | -7.39384 | -44.45835 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad4848f7-33a0-33a2-97c9-43c32b744ac6 | -6.28463 | -44.93668 | 2025-09-29 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ff57a83-fb39-3b8b-bcd6-ed18256e48c1 | -5.55669 | -44.84628 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 84db98c3-943f-35bf-8c66-f4969b34c292 | -8.3024 | -45.48924 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d14847a4-3b2a-3781-a275-8a18e8e80fb8 | -3.36912 | -49.75329 | 2025-09-29 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4289172b-bc2b-3b2a-8b42-9fccbb3195e7 | -6.43369 | -45.90132 | 2025-09-29 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d16f559-2099-3a27-a105-050d6bfef570 | -6.12492 | -43.4865 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3bf8f10-c7ef-3456-8c4d-70b7655d5963 | -6.07016 | -42.60755 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3d4ad330-40ba-39f4-8e86-e80db3427f95 | -6.27601 | -42.48719 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd42acdc-13db-3ed1-8e0b-d91d81d06fa4 | -5.69055 | -42.63888 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d6ed18bd-d704-3e24-894a-7c90b264f79f | -5.81624 | -42.79182 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 85f8002b-7114-30fc-b7e7-6b8fcdf15b34 | -5.81834 | -42.82189 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 28514871-b698-31ea-b266-e6f5116a2ebb | -5.72297 | -42.67342 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 891c06a5-2b2a-3b11-af6c-9cf6307ed753 | -5.73703 | -42.67189 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cf6402b6-a657-3f04-a481-0c665aac6d23 | -5.39356 | -42.29305 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa439e14-5e7e-390c-9e78-c3a738068909 | -5.82183 | -42.80014 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e0c3e0e0-6b8b-35df-890d-e27eff6887b8 | -6.74933 | -44.72697 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d331d0c-18e0-3675-9ed7-ab0a0a9fe783 | -7.22021 | -44.78513 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 829cc9c1-6724-395b-a2b0-198402e1829c | -4.97333 | -44.49909 | 2025-09-29 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 24a7db52-713e-3fe4-9863-61c39b249e51 | -7.22743 | -44.78631 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 9fe8345c-b386-3b97-b2db-22358a36a631 | -7.76671 | -45.74326 | 2025-09-29 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a91c0422-3ac2-3dd9-b1ad-2314c1fff8b5 | -8.25755 | -45.49439 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1af663c-6133-3c83-9bc6-b133ee7ef163 | -5.40602 | -45.52465 | 2025-09-29 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 530e1a3c-77e6-332b-9bec-74be22b04983 | -7.28822 | -42.83451 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20752dd2-d95b-3a73-b284-7379fca83084 | -6.74525 | -44.75211 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bfeafc4-8c6e-3087-b0cd-9d14741de145 | -5.74076 | -42.86532 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 79462322-e8bf-386d-ac38-085df2f3f886 | -6.45008 | -44.02659 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52531559-2898-39cf-ae81-db1c46796251 | -3.36384 | -49.75237 | 2025-09-29 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92c9c43d-a715-328a-b95d-b8b4e5b05f16 | -7.56702 | -42.40508 | 2025-09-29 04:06:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ceb9a721-7517-3a66-b208-e61530fc1d89 | -7.30719 | -42.94404 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c2d33af-37f7-3020-88c9-6bffb8350e7c | -7.76143 | -45.75169 | 2025-09-29 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 558fbd80-15e0-3ce5-a1ea-424c0879fe4e | -6.24198 | -44.48294 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11099a3c-27ad-3f62-9ac8-1b763fde7a2c | -5.74984 | -42.85185 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9fc37c1f-c062-33dc-a8df-65ce2d6970b8 | -6.07562 | -42.46624 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce0223f5-9490-38cb-8dc4-1dc625102472 | -5.68658 | -43.05166 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2134e8f1-e27f-3e6b-b79f-a0fa31c1ef5b | -6.11665 | -43.45053 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0b1f353-e27e-315d-b421-15e085d593e3 | -8.32864 | -46.21269 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a4e7f622-e9b1-30f1-92b1-837fc2ccfa15 | -7.74133 | -46.99825 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02e285dd-f438-38d3-993b-52a5c22fcc95 | -5.19361 | -43.75321 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| adfed042-a485-3700-a286-015d18023b4b | -3.0989 | -47.02202 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a402719e-b8a3-3784-bff6-f1460d53e27f | -6.65355 | -41.39504 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 86316fc5-6b81-395b-ba73-49dada1164f7 | -5.36595 | -42.84415 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 76d97866-7f4f-3f6c-b9c9-53052f8a2ce0 | -7.11085 | -45.53399 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33738a3b-1c96-3949-ab8b-5a599667309c | -2.80696 | -41.80637 | 2025-09-29 04:06:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 467d0b75-67c4-3c6e-a0e6-4b8477787a56 | -5.30868 | -43.15569 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 357a45bb-ec1b-378b-8e9d-164f1d153435 | -5.90988 | -45.85908 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0ea1580-ffa8-3e7e-a52d-bfbf7ca4bdd8 | -6.07953 | -42.46326 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff8449e7-d380-3e40-8a87-b34daf557a92 | -5.69968 | -42.6037 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85e45475-03dd-38de-a3e6-1dd40f2f7671 | -3.08186 | -47.76419 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2a66e27-8497-374a-a2f3-95cd4da7abcd | -6.91483 | -43.99884 | 2025-09-29 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e77faf9-364a-37ce-a732-a1c035cb4160 | -5.47987 | -42.87621 | 2025-09-29 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40471068-bbb9-34e2-8e89-babc87186ff7 | -5.19585 | -43.7616 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6c7087f6-3aaa-38e8-a905-efb648ecc916 | -5.86523 | -45.76603 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3305332b-c89b-3460-a6e2-45ca96663d34 | -7.28657 | -42.82328 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0fd689a-9d05-371f-974d-366c71f8b1c2 | -6.47495 | -44.2508 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89eb7145-e39b-3f5e-9391-70fe892636f1 | -6.07057 | -42.47632 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0bdf2be-c60c-361a-89dc-524f656f1fc8 | -6.47096 | -44.51232 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27b5d4d4-40c9-3d63-b5c2-9751fa274c29 | -5.17907 | -41.24607 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52e5c37c-7cf3-3a48-9e22-6d77a75dbb35 | -7.77659 | -46.64542 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0e79193-e61f-308e-aeea-c4dc937fab2f | -6.28269 | -42.48832 | 2025-09-29 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb867bf2-5458-3756-b451-879dbc6f485e | -3.83246 | -40.32764 | 2025-09-29 04:06:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3c091b35-4e49-373b-8029-b45fe1bbbc6d | -2.96358 | -40.84052 | 2025-09-29 04:06:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2fd81e3f-0e3d-33d0-b357-8ca902dbfd85 | -5.09288 | -43.85892 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08f427a9-295a-38ba-8f2b-0e73f1f25d9e | -5.8252 | -42.8007 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a05c5368-d61b-36b2-a593-2f01743c2fd0 | -7.28765 | -42.83808 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4b072756-99a6-3fe2-9254-749f26af3bc7 | -5.42201 | -42.265 | 2025-09-29 04:06:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 15a16816-afbc-3fea-98b5-c10ae5a6e198 | -7.31785 | -44.71793 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8637b75-b7e0-340f-bc72-4404162d3620 | -3.49995 | -52.47533 | 2025-09-29 04:06:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfb76f54-baa9-3c03-9e7f-53df9bc3ce42 | -5.73979 | -42.82785 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 260dfd4e-2abf-389f-8b0a-e2095fc953c4 | -7.73286 | -44.94891 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfefcaf5-1c5a-3f14-aad5-4904ce903bee | -2.22204 | -48.37439 | 2025-09-29 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe647539-4bc4-3368-b0d7-fdd22614d7a0 | -5.71232 | -42.67527 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de9c90ba-02de-3917-afb4-9032b1db0c90 | -8.29416 | -45.47054 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3217a0d-33fe-3e3f-bc0f-a48da2ccc67c | -6.47073 | -44.25441 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6461df59-ec1d-360c-8c03-de03a293d608 | -6.06666 | -42.47932 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 10eec106-3bc7-3320-93fc-47fca713b29f | -7.46519 | -46.30125 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc009b1e-2748-3afb-8e94-602d18d95116 | -7.82657 | -44.80672 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18bbd6d9-8c64-382b-a299-de0dce6d07cb | -6.61352 | -44.94151 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21b4143d-0100-3c76-abf0-bc8b9f0744a9 | -7.76371 | -45.7379 | 2025-09-29 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a8a9395-8621-3311-993a-a8abefc95f6f | -8.29199 | -45.48344 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d282dfe1-a3b7-3214-94c5-04df46ed4331 | -7.39253 | -44.4663 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
