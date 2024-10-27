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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03e7b7e4-0b61-3986-aed2-bd300add45bf | -10.56252 | -44.28185 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac69a3d5-83f9-30a6-a1a4-a3528686834f | -10.56019 | -44.27302 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24831a73-dbc3-3d57-8aa6-879ff622bb17 | -10.55958 | -44.27717 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02ec4ecd-5a22-3f26-b8f3-7ff387a2bad5 | -10.55663 | -44.27246 | 2024-10-27 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d263dfbd-d0a1-395e-ae8a-b514d1ee5cd4 | -11.94418 | -44.23795 | 2024-10-27 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1c20d1e-4000-3138-bd44-b1239efa2455 | -11.94227 | -44.55152 | 2024-10-27 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8430beb-6766-3cad-ac8c-d2b96ee790c3 | -11.93809 | -44.55512 | 2024-10-27 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 869513f9-01a3-3583-b57a-a3bacc2fb5d3 | -10.94731 | -43.93064 | 2024-10-27 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7829a092-b6aa-3517-acbe-ea436e11da83 | -10.94668 | -43.93493 | 2024-10-27 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94edf44a-bda4-316a-8d71-e52fb4644690 | -10.86727 | -44.2721 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6d64bc7-3d32-33db-bfda-4373743275cf | -13.65019 | -44.11941 | 2024-10-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 339bf56e-8d41-316a-b6a2-d7e29781e4be | -13.64646 | -44.11884 | 2024-10-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 391cf314-dd3b-3028-8cc9-f3a609a5db47 | -12.89433 | -44.60672 | 2024-10-27 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 448f9915-1716-3d65-b576-f5e87f187f27 | -12.69079 | -43.82614 | 2024-10-27 04:25:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0788f1c5-4402-3291-93ae-9bfb6be25563 | -12.62576 | -43.4445 | 2024-10-27 04:25:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 933d7d44-9e43-3d47-b5e9-e68b9d469f73 | -12.4646 | -43.78837 | 2024-10-27 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dbac24c-ac56-3b4e-86bf-083dff110144 | -12.45555 | -43.74476 | 2024-10-27 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06230599-ca6c-328b-8c4f-9e2315aa4d5b | -12.44654 | -43.78107 | 2024-10-27 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b15ed9d5-b1ce-3050-b209-7b1a827ab677 | -12.43239 | -43.74606 | 2024-10-27 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef4e6b84-4256-38c3-93f2-0358d91e273c | -12.43174 | -43.75068 | 2024-10-27 04:25:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71be9092-0c5e-34e6-a6e7-c9533c299697 | -14.29883 | -44.30798 | 2024-10-27 04:25:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61738fa3-810e-3847-830c-c7880ca85d39 | -14.09259 | -43.98716 | 2024-10-27 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b3039d7-21d9-3d2e-bc6f-91820bc4aea3 | -14.09257 | -43.98899 | 2024-10-27 04:25:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 574f6699-8d44-32fd-b31e-47ec7db3801f | -7.67659 | -45.37016 | 2024-10-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ebc8dfe-6f4b-35af-86a8-7407e222d83f | -9.44334 | -44.46612 | 2024-10-27 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 346cb91d-b2ac-3991-b0a4-69ee96deab26 | -9.44044 | -44.46161 | 2024-10-27 04:25:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b97897f2-6b9f-307f-b3c0-7b866efcda32 | -8.78884 | -44.71747 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04cce452-c9fb-31e2-89b5-580f7ce555c8 | -8.78828 | -44.72125 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30ac568b-d46e-3da8-9747-5c48a32c7a1e | -8.78771 | -44.72503 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 183e5cf7-aac7-3979-bebf-e7d1a48a7d45 | -8.78371 | -44.72828 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 775da7af-0e26-30ff-8be9-61cce9e483b2 | -8.78314 | -44.73205 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 511224ae-548c-34ae-9a61-5292dfa38510 | -8.78258 | -44.73582 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c9c5422-9192-3b7c-83af-01198ec2a48f | -8.77612 | -44.71194 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7e0d0b5-05b5-324d-a9eb-30349a08ff7d | -8.77554 | -44.71572 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cff788b2-d9a2-372a-a6bd-1c648c550930 | -8.77496 | -44.71949 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a909186-612e-30df-a2fe-63a061b96a49 | -8.77152 | -44.71897 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a6127c9-b77b-3886-9cfc-8658815d9858 | -8.77095 | -44.72275 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ec571b4-aa42-3e78-a9d6-91ccb87a38de | -8.77037 | -44.72652 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f221e955-41dc-34f2-a723-fbe5f36593b3 | -8.76293 | -44.70609 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c77b17f0-1971-3f2c-8343-dd51aca9d81a | -8.76236 | -44.70986 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 495f89dc-6870-39e4-99db-22197272b228 | -8.76178 | -44.71363 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1480eb5-240e-38b3-9f38-a11cbc5a7369 | -8.76121 | -44.7174 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73d1f46b-f87f-3e45-91df-948b76cf6c7c | -8.76063 | -44.72117 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65b795a4-47fd-3dea-b01d-a81a3b6c6604 | -9.08946 | -45.04516 | 2024-10-27 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd1dcf8b-7163-369c-b857-f89d417ae6f8 | -9.08605 | -45.04463 | 2024-10-27 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6ab3cdf-1061-3681-905c-a04f1cbbb184 | -9.08548 | -45.04837 | 2024-10-27 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 301e9108-4094-3904-b31d-34f6e886b42a | -8.87824 | -44.96038 | 2024-10-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31142a27-bf8c-3a74-a103-354d2376f766 | -8.87483 | -44.95986 | 2024-10-27 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d3a5d7f-e3a9-32c7-9230-27444c308ae8 | -8.54351 | -44.95263 | 2024-10-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba3f7dc1-380e-3d81-87d5-ea6c1f87599a | -8.54295 | -44.95634 | 2024-10-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef70ba3a-f6c2-3f5a-a169-38e1fd14d9c3 | -8.54066 | -44.9484 | 2024-10-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 887a3357-e2c6-3ecf-b481-e43c131e1fae | -8.5401 | -44.95212 | 2024-10-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f69034f1-3397-317e-99d4-151a6da225c5 | -8.4495 | -45.08531 | 2024-10-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 144c1117-975a-3f6a-b462-9d7b54f71f95 | -7.92554 | -44.89421 | 2024-10-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6345767c-f317-39de-831e-fb856323cb6f | -7.92214 | -44.89369 | 2024-10-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6630296d-023c-3dab-88c8-b7ce8d7de7f1 | -7.87586 | -45.37558 | 2024-10-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f654b89-a5a5-3d26-bf3a-a52365b5bd89 | -7.86916 | -45.37452 | 2024-10-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b5288ab-1472-312f-a7ea-f91e03c031d1 | -7.86861 | -45.37807 | 2024-10-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 555efb6a-47d0-3fae-b6d7-6e98952b7dc3 | -7.8603 | -45.40969 | 2024-10-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c02b9e2f-aa3c-3d83-915a-8310881de4f9 | -7.85641 | -45.41273 | 2024-10-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa92672f-1c8e-3e80-a16d-d0b8a0f4dcf8 | -9.98515 | -44.39779 | 2024-10-27 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77fc43e7-3e37-351c-b280-7a27a136ecb4 | -9.98455 | -44.40179 | 2024-10-27 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b23970a9-fe4f-3342-a81b-50e61e2bc964 | -9.98102 | -44.40128 | 2024-10-27 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8825e0e-bb17-3d7b-8db1-a8d502954963 | -9.70066 | -44.75315 | 2024-10-27 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e58e94a9-9244-329a-b7f1-a70513198b62 | -9.64004 | -45.1083 | 2024-10-27 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77fc3d75-7754-39ee-980b-51b42f0d7fb7 | -9.63662 | -45.10778 | 2024-10-27 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e1f9f62-aa05-3d6c-83ed-c2dc90786caf | -10.87803 | -44.53984 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed31547-5e4c-39e7-a2b8-94cc26c11299 | -10.87744 | -44.54386 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d930575-019e-30bc-9762-cdb4d475fc1b | -10.87449 | -44.53931 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b59587a9-e236-34c4-8fa5-faf0ea53188a | -10.66266 | -44.50649 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9129bd63-7a73-37d6-aebb-fe9bb8e89ee4 | -10.59027 | -45.16501 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a07e38c8-e51e-34b6-8624-8e0ad2f56960 | -10.58684 | -45.16447 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fb883da-993e-3bc1-89cd-03f5326cc91e | -10.54035 | -45.15028 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5ee3c0b1-788b-3235-80fa-5293aa7e91b7 | -10.53749 | -45.14596 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5dbe3962-093e-3dfc-9e1e-a947fd72744e | -10.53692 | -45.14974 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 003868fb-9d51-3ba1-88bc-46c0a32ad169 | -10.53464 | -45.14161 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e87a533e-8061-3ecc-a1b1-cba02d2b1066 | -10.53406 | -45.14541 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3bc0a2b-1d54-35cc-a2e4-469f165ab944 | -10.50576 | -44.86216 | 2024-10-27 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4a0579f6-d048-3545-a2b6-ed481dd6997d | -10.49515 | -45.17043 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d58226f0-267a-3658-a475-06a37f0793cd | -10.49171 | -45.1699 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29769288-74d8-3121-8615-d76405ecdcf9 | -10.45216 | -44.94544 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 332022f2-153e-3dd0-8206-bc34d9fa6414 | -10.44585 | -44.8932 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bf7a7857-360a-3cc6-b373-73d3d114b6e4 | -10.44527 | -44.89706 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4d25bd30-e320-3a30-8ba0-65890c1d72ea | -10.44239 | -44.89264 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0178100d-d9ac-3753-a633-96c176bb6791 | -10.44002 | -44.57181 | 2024-10-27 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7d0357e-08e4-31cc-882b-17e4cd4bec4e | -10.43943 | -44.57578 | 2024-10-27 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05ae4f20-7615-39d7-b3da-f3c4d8e2b46d | -10.43776 | -44.92349 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de333e1a-d59a-34bd-9e18-a436910456ed | -10.38734 | -45.2813 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2e95dde-32bd-3307-9777-450ab1bc49b2 | -10.37513 | -45.08254 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 07854e40-6b47-3bc1-8e1d-152b13c4378b | -10.37456 | -45.08635 | 2024-10-27 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc8d2670-39ac-3b81-acc8-91019568b66d | -12.09459 | -45.93848 | 2024-10-27 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00e32926-cfa7-3368-a9d0-268f0f357ce2 | -12.0912 | -45.93795 | 2024-10-27 04:25:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02d79616-5980-3d50-b4fd-cf5372c19b83 | -11.62791 | -44.96526 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8a054dd-b87a-3c74-8187-8fc78c5b1b37 | -10.96842 | -44.71238 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65c6650d-99b7-3e70-b33f-b902f5f1a58e | -10.92172 | -44.77903 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea8f4b84-3aef-31e2-b860-0268313937ef | -10.92112 | -44.78301 | 2024-10-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d50f569-5f92-300a-a692-4e6bb9420ca6 | -7.60472 | -46.87362 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7e94ef2-884a-3569-8eaf-be83f9cef499 | -7.59756 | -46.87603 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a43657aa-6301-3053-93d4-f1ac679387af | -7.59701 | -46.87949 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ebfa601-4019-344a-a437-202c6b649ec8 | -7.58614 | -46.81705 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README54.md)
