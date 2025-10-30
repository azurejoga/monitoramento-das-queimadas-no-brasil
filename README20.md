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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2958bc75-280b-3ac5-b533-6ee250fadc6b | -3.13221 | -40.05186 | 2025-10-30 04:04:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 293e1c94-1d0f-374c-b329-af3090f40cba | -7.32863 | -47.25143 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eaa1aa7-7e1f-311c-acbd-89096e3d9409 | -7.22301 | -44.33139 | 2025-10-30 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 218818dd-aaff-31ef-875d-8664717492e6 | -6.09615 | -42.43812 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ca5717c7-09f5-30b7-818a-94ea0c74eddc | -4.30554 | -41.43642 | 2025-10-30 04:04:00 | NPP-375D | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ce74e25-ee47-3dd1-adb1-5cb119c54f2f | -5.70612 | -43.15884 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 66ea83ff-b7d9-3677-ac03-bf7c351a9c7e | -5.59327 | -42.77599 | 2025-10-30 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 20f90901-652e-3f75-8c8a-6f0d8de0019d | -2.57288 | -45.80033 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3a7f57dc-dd82-3794-a32a-363073053b90 | -5.52053 | -41.24317 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 10ae4555-4cb0-3e7b-a851-8512f241697c | -5.80713 | -40.82684 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ea6b691-2db3-3303-8c61-37891593803f | -6.57726 | -47.54123 | 2025-10-30 04:04:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49e20229-47df-3836-9065-c88b3093e267 | -3.29488 | -46.05215 | 2025-10-30 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4ed6224-5e13-3042-88ae-8371a0ab5053 | -5.64911 | -45.98093 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3d08e5e-75e6-368b-b495-8b76fdb4d23b | -4.58166 | -45.5119 | 2025-10-30 04:04:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1cba184-4c20-3c92-80bc-80f9982dc8e3 | -4.309 | -41.43686 | 2025-10-30 04:04:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe8c935b-76fb-3e0a-9012-6d732858dd71 | -6.45413 | -42.21177 | 2025-10-30 04:04:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 218bdd8b-30cf-37b9-9f08-69e1aee35c62 | -6.50484 | -42.23868 | 2025-10-30 04:04:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7fcd9d56-e7a6-3511-b127-b4810cf65519 | -7.43863 | -44.24177 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41926df5-91a8-3468-9ff9-98bd08a241b9 | -7.66319 | -43.91628 | 2025-10-30 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d698421f-f36f-3cc9-ace8-dcb8f9f206eb | -5.79765 | -40.82169 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e17f0030-b355-384c-b7a4-67346946df4e | -5.40205 | -49.42479 | 2025-10-30 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bf05c04-14fc-3b31-91fe-bc3bd515ac1b | -5.46129 | -40.87404 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22e1b674-15a7-3f1b-986e-da52ae2ca9e5 | -5.21697 | -44.01266 | 2025-10-30 04:04:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdd91d29-cd64-39a5-b4b2-752cd6dc39b2 | -5.41921 | -44.63144 | 2025-10-30 04:04:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 491687c9-d745-3507-8ebd-49426ae307a9 | -7.78074 | -45.93943 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 688de277-fcfc-3a3a-ad3e-c1ba0408f0f3 | -6.5209 | -46.90386 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ddc9c0d3-1f44-37ed-8f1e-ef1223b1297b | -7.40376 | -43.93892 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49de2bae-4b93-3d73-84f2-5eef38cc785c | -6.12492 | -42.4388 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bfdd2567-e33f-309b-bdff-58f61ffaded4 | -7.00293 | -39.12389 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dca2cd6f-cf1e-3f41-92ca-8ab8c60737dd | -3.66944 | -51.71812 | 2025-10-30 04:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12808365-ed2f-3c41-9132-92460bce6c8f | -3.67504 | -47.62881 | 2025-10-30 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8b49c51-b500-30ee-a1c7-7f156c7780c9 | -6.10671 | -42.43982 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f6d380a3-1791-3b1a-bedd-335e2018844c | -4.90959 | -45.67307 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87eed72-3505-3e5d-b88e-967c4b438506 | -5.80881 | -40.83785 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d78265b2-5797-355a-b27f-c0b0330fa503 | -3.36054 | -44.26325 | 2025-10-30 04:04:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 581d1ac0-d1a7-3d71-b5d9-6d5a4380746c | -4.42923 | -43.37099 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61063dbc-3afd-3d42-b5d7-8de6e0a15751 | -5.70314 | -43.15401 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c4ff2fb8-450d-3f2e-b9e7-3d5b9703b54f | -7.3078 | -44.9779 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 19780992-492c-3451-8854-6896759e7a73 | -6.13344 | -41.71066 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4ecddf5e-b4d9-3c21-8989-f48aa422e618 | -6.13869 | -41.59064 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e2906798-7990-3bd3-afa7-c3b97d1ca81c | -7.3073 | -43.96426 | 2025-10-30 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22146ab8-3eb3-394c-b103-9c1eb95f47ed | -5.63626 | -41.54594 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 673443aa-698d-34fd-851d-2c22e2ee984c | -7.96506 | -43.19868 | 2025-10-30 04:04:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5748212-4b7c-37c5-bac4-9898255cd328 | -6.13937 | -41.67365 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b7aee936-3ea2-3d27-abe8-489aba74e69a | -7.80755 | -46.41293 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc67488b-b0a9-345d-a404-354afc89bb4b | -7.6173 | -43.5895 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6404f753-53a6-3a7e-9be2-b94d428dcd43 | -3.11715 | -45.10042 | 2025-10-30 04:04:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 346b5eab-39dc-30c0-b521-126d1b6cc12b | -7.78736 | -46.42628 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 77d5b40c-81c3-381b-89dc-a1e3f8d3cf8c | -4.31655 | -48.2307 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e74cff39-7aa1-34da-bcdf-c06de01c1420 | -6.12612 | -41.86634 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 54a16aed-be58-3e95-aef7-9a271d9056c9 | -6.01579 | -41.97978 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 50218e46-2e61-3457-8387-a43ce387221d | -7.86896 | -44.23383 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73163d73-d771-3b23-a049-efb772ec743e | -5.43805 | -45.09469 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f9668fb-b992-3991-8f6f-ecb10216eb57 | -6.08665 | -41.78304 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a476c33f-a317-313a-a93f-d965172210d3 | -5.80546 | -40.83729 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a4d12277-5b8f-36b2-bd65-853229e304be | -6.13924 | -41.69638 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e2957000-d694-3fb2-9375-821fb99e54e8 | -6.14026 | -41.71192 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80e99897-4070-3921-b76c-9cf10751015b | -5.30177 | -44.3222 | 2025-10-30 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c0aa73f-3818-34ef-8f0c-bc05dcbde41a | -7.14124 | -40.46167 | 2025-10-30 04:04:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0e1d87c-fd6d-3f73-b835-4680ab5a8d7f | -7.34473 | -43.90174 | 2025-10-30 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6690f644-3838-359e-a117-464caff577e9 | -6.70748 | -38.20964 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82d53db6-c747-3c6c-a49f-972807e514b4 | -7.12373 | -47.00179 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33584dc4-2690-3408-b678-004b58b7c644 | -7.38644 | -42.47248 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ef548c5a-be74-3ce8-82e9-f2f8ee9cf25f | -6.13701 | -41.68839 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 34dc2f4a-3f38-3db1-a5cf-801e51a981c2 | -3.46739 | -41.79948 | 2025-10-30 04:04:00 | NPP-375D | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1846c33d-23b1-37ed-9190-b97d79c92ca6 | -5.79487 | -40.81762 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b1ec7e2-f154-3486-9898-d2fb8eeddae3 | -6.31025 | -42.10355 | 2025-10-30 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 68ba3442-4430-3403-9bfc-4b7baff3c562 | -7.31515 | -44.12413 | 2025-10-30 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7191d4d3-9455-3bfa-b667-0e163534f119 | -6.13418 | -41.68417 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54530230-f99c-355e-b702-dfc22cf69e08 | -4.31716 | -48.22743 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e5b5a60-f607-335e-b60b-785d2c58e384 | -5.86242 | -40.78152 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 26d077e7-9490-3574-98c2-a912b8fc2e89 | -6.13017 | -41.86313 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 47b4e3e4-5a14-3d2d-8486-a296dcd30efb | -6.10994 | -41.72586 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8fa39dd6-db48-38e2-8543-c880083c4d89 | -7.30468 | -44.97209 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b246f246-18f0-364e-9004-0883f5db5f66 | -2.66483 | -47.87348 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 188a301e-777c-306d-85f5-25a721681c27 | -4.46724 | -43.44714 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ad69c73b-b34e-3196-a943-929281c1e414 | -5.67204 | -43.94566 | 2025-10-30 04:04:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ffad929c-c927-3da2-bceb-c13ae0dd859f | -6.12387 | -41.85836 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77ebaf7b-6428-3efa-9595-fc6e61223375 | -7.62238 | -43.58154 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 042f4a4e-66a9-31a4-bd17-52019ac0f0c4 | -5.79095 | -40.82062 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9fd42629-449e-3021-8057-f38a0b257cc7 | -7.76254 | -46.49143 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d599ad6f-93c9-3f8f-bf4b-f849c4206321 | -3.79877 | -43.89641 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 84bf7c38-8534-3bc0-bd04-52cb4157a6a6 | -4.49045 | -44.02496 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1efa8f60-0903-3e99-a138-13fa8cb195be | -4.81491 | -45.69979 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b58e43ab-f588-3ae0-94df-d426917e7bc4 | -7.15733 | -44.70448 | 2025-10-30 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bc285ad-2341-38ca-ba0a-cd456b84d7e0 | -6.71033 | -38.21384 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| efb58128-1982-344a-bcf5-44660023dbf5 | -5.52111 | -41.23956 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2e56c2d0-56e1-3283-9ad0-e8f6444e19d6 | -6.91962 | -42.25405 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c607bddc-0e9e-3ebe-8046-d7d2582c4ea1 | -4.68035 | -45.80785 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22e0bf16-7736-3257-b335-20797cbc69bc | -6.13883 | -41.56806 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ed33725-dd2d-3c69-aaca-f1be0b58b02c | -5.72865 | -39.03458 | 2025-10-30 04:04:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f2e234c7-3e7e-36e9-bc45-63f6a5a106e1 | -7.28493 | -46.44168 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 960e2fbf-5399-3b2e-86fd-37181fcd7cdd | -5.19763 | -45.61015 | 2025-10-30 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a7625ce-627f-3bd5-924e-c5d40c3efbbe | -3.70689 | -45.3875 | 2025-10-30 04:04:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 729ee846-38c0-33e8-a298-8d85abec8649 | -7.32778 | -47.25626 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b189b26-a132-350d-8d98-cf687f00e0f6 | -7.46034 | -46.8508 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faa0981f-0fae-3b01-8f0f-407b88bfc286 | -5.43013 | -45.34872 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84427a38-370b-3f70-af2f-dc355c432024 | -7.37759 | -46.22055 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dabf97c-128d-3c6f-a517-3f69efd57266 | -5.91772 | -41.91834 | 2025-10-30 04:04:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d10bd960-7dff-335e-8d69-269635fb0849 | -4.74928 | -45.71596 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
