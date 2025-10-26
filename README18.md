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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1231c0bb-fe13-31c1-a39c-9305c88dc8ec | -2.97172 | -49.11825 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 410547b2-77b5-3c58-8ac5-7108e115d903 | -6.21785 | -42.53948 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f7a1db5b-f248-3efb-b68a-b1b8bf509bef | -4.71019 | -46.44169 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f1580c1-1f23-3559-af47-baf0283f7e51 | -7.6913 | -42.18133 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1e2a3af8-716f-33d5-b7a5-4a70fdb654fb | -4.32444 | -41.78885 | 2025-10-26 04:00:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 67521139-bf2f-326f-8bc2-d1736e4f4d39 | -9.3137 | -43.09251 | 2025-10-26 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 15a18e72-0a5a-32cb-ace8-ac6f4a1b5fde | -5.88101 | -43.93361 | 2025-10-26 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9622dce6-509c-376a-866b-902b40809d4d | -3.73988 | -43.38575 | 2025-10-26 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4878ac76-4ff0-3be3-8c60-7bf33eea6b7f | -6.73595 | -44.15118 | 2025-10-26 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c0d429f-a30b-3e28-a8df-b9f59082d5fa | -6.39494 | -45.77531 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de8981a0-f638-390a-85f2-ee5b583f2fec | -6.20593 | -42.54591 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3737407e-283c-3852-b716-ea460382c6af | -7.85222 | -45.37549 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63dc32f2-246a-384f-b3eb-641dbabc23ed | -3.44816 | -41.85274 | 2025-10-26 04:00:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 332735d3-f562-3150-b8ca-38806aa0b860 | -6.06245 | -42.15266 | 2025-10-26 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c94b33c-bb38-355e-b45b-ac27f5a100d9 | -7.84097 | -46.43815 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 09588e11-f5b9-3beb-b266-130f5fc14604 | -8.31703 | -46.81435 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ab0506a-e6be-3103-b14c-b6f83b99f29d | -4.63853 | -42.51241 | 2025-10-26 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b23dc38e-26f8-30d0-b3aa-18a8fa6f4928 | -6.11256 | -41.75077 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 36391d0c-3200-3ddd-aa5c-fbaefa1289ed | -4.32319 | -41.79659 | 2025-10-26 04:00:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3e41f13-87b8-3411-a4ac-9fb68b61d819 | -6.35014 | -46.12027 | 2025-10-26 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a229e41-872b-3b32-91a4-dab32e45d60f | -7.80295 | -45.39742 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da91037c-42ce-3cfa-9875-f716a083deb2 | -7.19754 | -39.41039 | 2025-10-26 04:00:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb24c8c2-8704-3d82-8976-7cfd2614eed0 | -3.71543 | -42.3793 | 2025-10-26 04:00:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| acec0921-4c2e-3007-9e2b-2a955a90ac2b | -7.16055 | -45.17004 | 2025-10-26 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20cf3c17-4def-3578-97e0-3a7593403064 | -7.68069 | -42.24564 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1da1418-690a-3005-88a9-d76e8374f578 | -3.09286 | -49.45541 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3db7c9eb-96df-32eb-9610-be089c2d524e | -6.30138 | -42.95751 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e25a5477-23c3-3265-8eed-ef46ef54a42a | -7.35833 | -42.43797 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5b78fb34-699b-3b55-8b39-68e028a7a922 | -5.89644 | -41.28674 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28d895be-6ff6-3e94-9d8e-ca90683f3868 | -3.13922 | -50.16185 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7615a64a-4b49-3d6b-b7c1-79df4a6707c3 | -3.46799 | -47.68581 | 2025-10-26 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fff2f581-2c7a-3f2b-9782-8df6c21c5d59 | -7.7995 | -45.39296 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f0eccfc-7634-31e4-a9ae-e0bd3356bbc1 | -7.09122 | -39.56769 | 2025-10-26 04:00:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80486651-6404-337a-89b1-5654f7bd1d41 | -6.20657 | -42.54189 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b0630f0-b226-344c-8d46-50ea3a3bc323 | -6.42899 | -44.68147 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 374f2ce5-7479-3146-b0c6-13fb46864bac | -5.47075 | -37.84801 | 2025-10-26 04:00:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fce5aa62-d46a-337d-949d-96bb0927ffb7 | -7.14503 | -44.84731 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9719ba30-50bb-365a-8b2e-06f83ff70f40 | -5.3279 | -35.93313 | 2025-10-26 04:00:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 563f0ea3-ed3c-36ea-9fd4-7cf31a142f82 | -3.87534 | -42.08084 | 2025-10-26 04:00:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22fee0e0-0e3d-36f1-b223-96fbee8161e3 | -6.43048 | -42.34494 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c19bb78-fab8-3ed9-a9ef-1c800a396386 | -6.80717 | -49.35234 | 2025-10-26 04:00:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b17a8e1-a1fc-3ab6-bec7-83227a475032 | -5.50708 | -49.5821 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ceb5f1cd-907d-30f9-99c7-dbd3dc632fca | -6.24509 | -44.62928 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e81c928-1940-333c-8fd5-c22b8c6ace66 | -4.73727 | -43.26302 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e18d34bd-e591-3214-8478-83b072e1de9d | -6.3309 | -42.75546 | 2025-10-26 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1ed4e009-a3b9-3e74-b8c5-8195745dfd7a | -4.29486 | -49.29646 | 2025-10-26 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4abc605d-0b45-36f6-97bb-7390e2144486 | -4.28294 | -38.71815 | 2025-10-26 04:00:00 | NOAA-20 | ACARAPE | CEARÁ | Brasil | 2300150 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 181edbec-cde9-329a-b91d-6791aea15059 | -5.10357 | -43.20303 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| cc748ee7-e429-3766-8328-3d880a55c6af | -5.43239 | -40.87763 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0e5d05ca-bdb0-3eaf-9dec-111536cb8985 | -4.26825 | -40.69757 | 2025-10-26 04:00:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a95cc5d-1c83-3c4f-8aed-21b21086eae5 | -7.01168 | -44.68879 | 2025-10-26 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 065d4ef5-8291-3d80-b1fd-ef19b3ee1208 | -6.71112 | -42.04179 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cbba783f-1e71-3a96-84e1-2be4449e1565 | -4.80831 | -43.30535 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f69ed38-4f0f-3324-84a1-3d30b3b2e588 | -3.71182 | -42.37872 | 2025-10-26 04:00:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80cee2b4-09b5-381a-a19a-95fa9a08e344 | -8.65816 | -43.87252 | 2025-10-26 04:00:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1f57bcd-7e0b-3174-b488-abcee9b4eece | -8.09554 | -46.94244 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e6f1eee-04bc-3641-837a-085cd30dfa68 | -4.26488 | -40.69705 | 2025-10-26 04:00:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ae3ec16-3d36-362e-a655-ac8cba9a7081 | -7.68783 | -42.18528 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35300f60-a2ad-361d-bafb-0a43e8021cdf | -5.7134 | -49.31141 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c12ca35c-059b-32e6-818a-8091a7db7f7c | -7.83718 | -46.74435 | 2025-10-26 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79d48367-8bfa-36e1-9d1a-bc812565ecc6 | -5.96525 | -43.63025 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 616b5d87-9dd5-3921-ad2d-271f6fc72836 | -8.04484 | -46.74498 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e463062e-6608-3d42-b3be-8f2242f9910d | -5.55283 | -41.25815 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 56ab96d8-f649-31bd-b4ea-49201ff5d7a1 | -6.44746 | -37.08912 | 2025-10-26 04:00:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 02962331-f319-38bb-be18-f09563461269 | -6.78555 | -45.41371 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b46bcaa3-f3a8-302a-8822-b5ce3228274e | -7.88576 | -45.71359 | 2025-10-26 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe03607-3d34-3daa-946e-4bb4c6f0bdce | -8.09437 | -41.08445 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01a5e80f-0fcf-38bd-9c88-ce0355872029 | -8.15304 | -47.75149 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5585aed6-3a05-3738-9636-9ef21f260ba5 | -6.71225 | -44.6278 | 2025-10-26 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 615a7753-ba8c-3f83-9921-0c2eb81b2898 | -4.0337 | -46.06898 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f17ce60a-ffc5-391d-975c-aeef7bcaee46 | -3.09219 | -49.45944 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e817370c-459d-31db-bbf9-7841fe080942 | -5.58802 | -41.3272 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| df039152-174c-3d5e-80c9-bdd5442421eb | -8.08117 | -43.93391 | 2025-10-26 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17f1d09a-33e1-3d01-b5ca-0a1d094b0685 | -5.41901 | -46.47784 | 2025-10-26 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f121fba5-9298-3aec-bd11-5720bda7bf37 | -3.69072 | -49.5516 | 2025-10-26 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e250482d-f994-3e6e-bec4-7cf7da82c183 | -5.47188 | -37.84069 | 2025-10-26 04:00:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca307f72-7cca-3bc0-98fa-67f3bf39e657 | -6.5086 | -38.60487 | 2025-10-26 04:00:00 | NOAA-20 | BERNARDINO BATISTA | PARAÍBA | Brasil | 2502052 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef30eb45-3fc5-3519-9fac-48cfc6103602 | -5.46679 | -37.85115 | 2025-10-26 04:00:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e6e365ec-9fcc-3ed8-81d3-042d158174ef | -6.02211 | -43.31001 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ba60c75-c1b5-30f8-a914-bf300dd8f79f | -3.10173 | -49.47377 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f191340-95a9-35ea-ab2c-85001262101c | -7.14799 | -44.12957 | 2025-10-26 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a360d27-b706-3059-9599-f26dc5d41229 | -3.27194 | -50.04933 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9db1f7dd-77fb-3679-9b5f-bd4c027ebac6 | -8.49679 | -44.73606 | 2025-10-26 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b5c248-2fc0-3014-8428-a8660782b7d7 | -6.09754 | -44.54603 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbad18ea-8b9a-31d2-9e85-b3955a888713 | -6.39068 | -45.77449 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f74facd2-8586-37d2-ad43-a94e18aea0a2 | -3.75948 | -47.57474 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c495b2ad-61f4-3177-b387-413ec3e284d9 | -3.10402 | -49.46107 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3fed38b-374f-3efb-baf4-c102f4888f6b | -6.5962 | -42.66381 | 2025-10-26 04:00:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4cd541b8-3099-3321-be07-9cbf28026943 | -3.0973 | -49.4645 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5c17b71-f56d-32af-83aa-d4f5387a689c | -6.43711 | -45.73346 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfd1c9e1-879e-3e52-88e8-661b21d17e03 | -3.78724 | -43.40814 | 2025-10-26 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d94ebdcb-16fa-37a1-8236-9d6cce92daab | -7.16402 | -45.17431 | 2025-10-26 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b98af6ce-fa43-3dd8-a223-bda625bafef5 | -6.52844 | -37.98526 | 2025-10-26 04:00:00 | NOAA-20 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c7b45f0d-d9ce-32f2-a27a-ba49fc06c24a | -5.29244 | -41.1574 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 451e3f69-1b4f-3398-acca-3cc0b6a416db | -3.8396 | -50.20074 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c69eed07-c955-3955-b05d-0ca8e5f3ff26 | -7.84103 | -46.43552 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fdc74dbb-2f95-3a55-a84d-59c2b16a2e68 | -6.21366 | -42.54296 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27b2af0f-28c1-34bd-8935-652137db6e3b | -7.88092 | -45.71677 | 2025-10-26 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a2fe7e3-3f14-383f-9bde-7bcf1f10b396 | -5.1154 | -43.20049 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 73be7b81-691c-3680-9f79-f1c917be3b68 | -5.54489 | -41.26439 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README19.md)
