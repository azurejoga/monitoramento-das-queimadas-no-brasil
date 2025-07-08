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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6acb57c-0e1a-396f-b6c6-656e57923842 | -7.18812 | -43.12727 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e590e7f2-de2f-3925-aa21-c208199f26a3 | -7.20215 | -43.1249 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 68a830d6-7b15-3957-a1be-eb50b21641e5 | -7.27999 | -44.64927 | 2025-07-08 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97593b7e-5459-36f5-8cac-6c5bbf6e7bd4 | -5.41191 | -46.06853 | 2025-07-08 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1722de0-f0bd-3a4c-aa5d-97229fcc28c8 | -7.3055 | -44.03224 | 2025-07-08 04:40:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a82bd5f-a2aa-38b1-9d95-0341a38380d2 | -4.28895 | -48.05815 | 2025-07-08 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b699ad1-279b-350a-bd3e-8f11571d928f | -7.24763 | -43.07965 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 38b36e0e-9765-3eb3-87fc-1ffc66ecf62d | -4.3707 | -48.2284 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc763a20-d0a6-3092-bf65-3fe48f6ea2d9 | -6.52982 | -43.53886 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb49563a-5882-379e-8c6d-ce5a4f771d16 | -6.36831 | -43.65223 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2970107-6515-3d7f-86ae-e78904e1c911 | -4.42302 | -48.14736 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d00ef752-f77e-3877-a564-25bb59fe9257 | -4.30401 | -48.07127 | 2025-07-08 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 504c32d0-8abc-351d-bcb4-3677df4b9799 | -7.19769 | -43.12424 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9e537dc4-9ef8-358a-b0b7-e0e85d7a5705 | -6.68021 | -43.35966 | 2025-07-08 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31b30ec0-7d34-35a1-ac94-dd038f6567b0 | -7.64072 | -45.36507 | 2025-07-08 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45a08784-5f66-3afc-b641-c802f357de8c | -3.01285 | -46.69032 | 2025-07-08 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7b9de78-6b5b-322e-9d41-27817fd41669 | -7.78717 | -44.57298 | 2025-07-08 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09f71ccf-6552-32ae-b6f8-1cd007570fb8 | -5.41128 | -46.07272 | 2025-07-08 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a9a45b02-fa39-3694-8142-d058105281d2 | -6.88885 | -45.23933 | 2025-07-08 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 937e1f52-bc92-368f-ac6a-37b87d4e46b2 | -6.82033 | -43.59303 | 2025-07-08 04:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f949894-08e0-353c-87f8-f204ddd2f0e2 | -4.30736 | -48.07178 | 2025-07-08 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23af2fde-d1ef-36ab-ad25-bddb79e63a29 | -7.19131 | -43.13669 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e33256f0-8d83-3b14-ad2b-98f441925e7e | -8.07109 | -43.11596 | 2025-07-08 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 36f31904-b80a-3676-b373-73dab9702653 | -7.21962 | -43.11642 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11879f85-51b4-3b12-af52-db75a1c999b8 | -7.28122 | -44.6128 | 2025-07-08 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a94a44f1-a1b3-33e6-8efa-c1df33a1cf13 | -7.23051 | -49.59626 | 2025-07-08 04:40:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20f0afee-2c9f-31ca-adb0-b7261f1ff0c2 | -5.41491 | -46.07323 | 2025-07-08 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2ffab406-8054-3356-89c7-4405e77c5e89 | -5.73688 | -49.13687 | 2025-07-08 04:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3486120c-325d-377b-ae94-c84c16082d9c | -6.26293 | -45.27105 | 2025-07-08 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a32e27b-df51-3cef-8c05-22fc055c7af8 | -3.48282 | -51.19061 | 2025-07-08 04:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a6ead05-b676-392a-972f-0da9e1d73aa7 | -4.81751 | -44.3554 | 2025-07-08 04:40:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fa11de2-8118-37e6-82ec-735da0b13d7c | -6.43583 | -44.80422 | 2025-07-08 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 606041e6-960f-3fba-aab2-ff7974daa1b0 | -8.21898 | -44.93448 | 2025-07-08 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9871bf47-3f2b-3e43-a720-3e64d85f0305 | -8.15377 | -47.6249 | 2025-07-08 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9a952a43-8dce-3cac-bfd6-b36be7313ccd | -6.00988 | -44.52832 | 2025-07-08 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d62f2d04-d2e5-361e-9c1b-f42600d5fa14 | -6.7338 | -44.33315 | 2025-07-08 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7118eee7-318d-3649-95fd-ab23339dd77e | -4.29285 | -48.05515 | 2025-07-08 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b061a7d-23a3-3ca1-9db3-f3ff295d2332 | -5.79296 | -47.02433 | 2025-07-08 04:40:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84ab73ca-e35c-39f0-8688-8b9a5cddc7a1 | -7.14885 | -44.01753 | 2025-07-08 04:40:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8feb676-e39d-3140-a065-5c0ff28d6b7f | -6.52868 | -43.54681 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a848bfde-44ac-3693-b884-c105d6d2db99 | -6.88044 | -45.24268 | 2025-07-08 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab3e94e8-1ef7-3481-b1fa-f397f01a30ff | -7.25596 | -43.08548 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 2adfa201-44a9-324c-a90a-a52bf3c9a571 | -6.6776 | -43.76955 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 890cf295-86a2-35f1-977b-5d8ccd95f573 | -6.82523 | -43.58961 | 2025-07-08 04:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05522658-929a-32b3-bd42-6bced56faf2a | -4.30067 | -48.07074 | 2025-07-08 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eac4d8e7-14c5-3f35-84dd-7dab58f06826 | -8.50081 | -44.76116 | 2025-07-08 04:40:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9b1af0f-8aab-3d93-a851-c208372c73e8 | -7.5778 | -45.22533 | 2025-07-08 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a20ed7b5-f01c-3938-8b8f-336fc445f01f | -7.09857 | -44.15846 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69a83e9b-36ee-3b7c-addb-e1feca1b3afc | -5.25329 | -44.45963 | 2025-07-08 04:40:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95759269-0384-38b9-a8d8-e4ace06c286c | -7.27907 | -44.62743 | 2025-07-08 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ce14dfc-2eb8-30f7-9d17-ca9f41b331bf | -4.69115 | -47.00587 | 2025-07-08 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a95e40-2e9c-34c3-804c-6e0db793a6bc | -6.34661 | -46.36442 | 2025-07-08 04:40:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eab4fc54-aad8-3751-8802-33f5f95bbac5 | -4.42691 | -48.14439 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70273323-8167-3c33-90e3-a7626c12aee4 | -4.2825 | -48.18626 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9a91693-5a85-3a63-8fab-31c7f91003a5 | -8.06656 | -43.11531 | 2025-07-08 04:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 91e27c08-7558-3c0f-b342-fb47f3a7f279 | -4.5533 | -47.08438 | 2025-07-08 04:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d3379f-8be9-38e1-a511-4f7cc2460f36 | -7.43429 | -45.41602 | 2025-07-08 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b04a8964-ccd1-331e-bafa-4f3738853917 | -2.99154 | -46.71376 | 2025-07-08 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49a57175-1713-3536-b9bf-adbc531a101c | -7.1116 | -44.15646 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2878ee3d-26f5-3ee6-93ca-9fa703393327 | -4.2923 | -48.05865 | 2025-07-08 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e8cb7a4-048e-3e31-ae16-191cbb4a6981 | -6.86566 | -44.06688 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d0750fe-843c-371c-b9dd-df721f2fc560 | -4.2895 | -48.05464 | 2025-07-08 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea84d485-1cdf-3128-9b11-fbdab11f0361 | -5.25253 | -44.46468 | 2025-07-08 04:40:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47943f4a-6d12-36ae-99a6-6b4c1fa30f96 | -5.73356 | -49.13635 | 2025-07-08 04:40:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19828c14-d659-34e4-b696-cc5361690bb3 | -7.25659 | -43.08104 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a8e49a33-9890-3a89-88c1-217b733b4bb4 | -7.24825 | -43.07519 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 276d6cfb-ddbf-36aa-a7d6-4d5419c99950 | -6.42082 | -43.51747 | 2025-07-08 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d6a62dc-32af-39d5-b51f-f1aef7904deb | -7.27593 | -44.64882 | 2025-07-08 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e60d9c35-ca6e-3f1b-8991-15ee8811170c | -6.26677 | -45.27155 | 2025-07-08 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd1cd467-0df5-34a0-bbf3-2546d0971885 | -4.821 | -49.27914 | 2025-07-08 04:40:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d668a1ea-e1a9-31c0-9cd7-e56261098036 | -5.65312 | -46.59335 | 2025-07-08 04:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8c0bdeb-f655-3efb-8c70-35b09097c326 | -7.5785 | -45.22046 | 2025-07-08 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d4d067e-de0f-30be-b467-887f9174534e | -6.69104 | -44.06195 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25bf1266-bc41-32e2-aa7a-a98217427411 | -6.34164 | -43.74459 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6dca03b-d031-3a4e-9ca2-55ca9e81f19f | -7.4488 | -44.59813 | 2025-07-08 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4de338bd-e97f-3f77-a915-67f0bdac4be4 | -7.14519 | -44.01315 | 2025-07-08 04:40:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7407ddaa-58da-3a37-ac1c-4c58d414ca38 | -6.53356 | -43.5434 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2e84f68-a2e1-3b01-baeb-0ea5ab9aa2df | -11.32459 | -55.21717 | 2025-07-08 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4298fba0-8c4c-3f5a-98ac-795288a28e2f | -14.19022 | -45.50581 | 2025-07-08 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73fe0167-f3cf-3b43-b5cb-78a8ce0c7a30 | -13.01342 | -46.76814 | 2025-07-08 04:42:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7023c3ee-aa84-3222-8cb3-d648a303dfe9 | -9.34461 | -58.84989 | 2025-07-08 04:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73ba5184-7fc2-3700-b30b-ebc79eac9ab7 | -10.64338 | -49.46942 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 872abeb7-a8ea-37e4-b865-9ebcb801f6bb | -11.42973 | -45.09933 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 877382b1-7016-3319-9159-4688f2bd5439 | -11.84284 | -43.79742 | 2025-07-08 04:42:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b19d21e0-fa5d-3553-b40f-301776e36c73 | -10.97655 | -45.11621 | 2025-07-08 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 575f1e8d-66d9-3334-9726-5c3018f8fbce | -10.64504 | -49.45873 | 2025-07-08 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7522a44d-b429-3413-b3e2-5b481e141ee5 | -11.4725 | -47.91948 | 2025-07-08 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9944b1a0-4e59-3f11-898a-efd73d684bbe | -11.44059 | -45.1125 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0ba805d-36c3-37c0-899a-267ae97d2e23 | -11.43389 | -45.09993 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6ae6083f-a5d4-3c7f-82a0-58812936d9a0 | -12.01537 | -47.77894 | 2025-07-08 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5445081e-868b-3912-bc80-301b58ef95f7 | -12.02744 | -57.08139 | 2025-07-08 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 612f9391-3261-3a42-94ed-7669a8cd1422 | -9.37608 | -48.9573 | 2025-07-08 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f673306-94be-31f1-992b-10c41082b0cf | -12.98853 | -44.88248 | 2025-07-08 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f39e1d3b-efa3-3893-9b6a-83ad338a4fd2 | -11.44582 | -45.1055 | 2025-07-08 04:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7a2d783-6a02-336e-9c4f-a9dbff72959e | -10.99913 | -42.78262 | 2025-07-08 04:42:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f8c0500e-427d-3899-9cd2-8aaf0a0d4051 | -11.02157 | -56.25303 | 2025-07-08 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 987aaa2d-3a39-31fd-a42b-e21585bb1b1c | -8.9595 | -47.27651 | 2025-07-08 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57ba3342-7821-3af1-afbb-a153f635d323 | -9.80966 | -48.25754 | 2025-07-08 04:42:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c5a0298-4e17-38fa-b8ad-6eacda24338c | -10.39401 | -52.17546 | 2025-07-08 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5664dd8-8952-31ef-911d-7286f22138b8 | -10.28554 | -49.66032 | 2025-07-08 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
