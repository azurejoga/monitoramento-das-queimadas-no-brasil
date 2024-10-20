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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eee3860-3e56-37c2-b5f2-2cafe12bce1b | -4.57849 | -48.01857 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b340f30c-69d2-3356-a06f-72d870b46fa7 | -4.57515 | -48.01804 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1211f260-1ad7-3d73-8a69-bfb171d8cb67 | -4.5746 | -48.02153 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1196e04-829e-3bd6-bbb7-980f3a613a6f | -4.57182 | -48.01752 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e3104bc9-cacc-3501-b2db-1c9e0760eeb8 | -4.57127 | -48.02101 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ff483294-28ac-3544-9b3b-9e698e9873ca | -4.56351 | -49.23213 | 2024-10-20 04:32:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f22e715a-a221-3484-98c9-2d93b140ed4e | -4.40788 | -48.07396 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 174298a4-b21e-31be-920f-70495b7ef04f | -4.28303 | -48.22345 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 545ed0d8-e74b-3f5b-84bc-1a8bf472e606 | -4.28014 | -48.06836 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5263fd9f-ddb8-321b-a778-5a08f4e333a0 | -4.20207 | -48.02742 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c8bed85-aaf4-3965-93d1-288dba06e6a0 | -4.1915 | -48.02934 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6a69dc1-f4f1-3cd3-8bd5-64b56ee6ba42 | -4.19095 | -48.03284 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10e4a4b4-c1fe-3bf5-81e5-32d0e88a898f | -4.18984 | -48.03986 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29eff7fc-b0d5-37b3-8da1-d72661b1e1c5 | -4.18928 | -48.04338 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d10f553e-0ff9-307a-adcf-d152639ccec0 | -4.18594 | -48.04287 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 921e664c-9b5e-3069-8fcd-c039e2a354e4 | -4.1431 | -48.40078 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3109d99-1acb-38ae-b9b7-7f4fa3df4398 | -4.12803 | -48.27863 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6162481-e314-338b-9e8e-8f980d726ad9 | -4.12635 | -48.26753 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f284a412-23cf-3296-9a32-1ca448ab6e97 | -4.12579 | -48.27107 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa81e91a-bf09-3273-b6a2-2326b69512ad | -4.12077 | -48.25939 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44376f69-736f-38c4-a221-c8a858a422f1 | -4.12021 | -48.26292 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15a530e8-649a-396e-82f4-c45a36e1a1f8 | -4.10234 | -48.24564 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f88dd283-5cdf-315e-84b6-7c3499baa3a8 | -4.09899 | -48.24512 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2ce3b0f-4e0e-3ab7-a72e-0339e65ca78f | -4.09619 | -48.24109 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 438b1753-5e7b-3aa4-852f-ef826c28aaad | -4.08051 | -48.27478 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b61aa6-3353-3b80-a421-88488d6a3201 | -4.07715 | -48.27427 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de55470f-579e-33ed-a277-ca419da9f1ae | -4.06899 | -48.25148 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98cce394-90c2-3723-a39b-246f76410810 | -3.96735 | -47.94791 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 289f5f2e-de0a-3643-9805-ae03ccb5463d | -3.9668 | -47.95139 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f51c2a11-8678-3104-948d-63c5b7bfadbd | -3.96346 | -47.95087 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a53cc3-74ed-3875-b45d-a4cbc471fd9c | -3.95957 | -47.95385 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fb34440-5c78-39ca-bc57-f4fba5377234 | -3.95678 | -47.94984 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9028201-8e46-3aba-8949-ca305c1dd4f6 | -3.92285 | -48.33748 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee35367a-a392-3604-8e56-0343c1a11989 | -3.91891 | -48.36237 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a20dece-a30e-36e5-a5e1-74789040e0e7 | -3.91835 | -48.36594 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ce199890-0f25-383f-bed7-6d698481cdc4 | -3.91498 | -48.3654 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3a38daa-d42e-3f7c-ab40-240d5f77505c | -3.91442 | -48.36897 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a89d56c-2018-3d6c-95cb-d08484a48eb2 | -3.90996 | -48.33183 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9e3d761-ece3-3db4-9284-982c97c398de | -3.9094 | -48.33535 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba031bc5-dc63-3979-b697-f798f26c3ad8 | -3.9065 | -47.95222 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af8cb85f-cca8-3c6e-9a8d-76d0451b5fb8 | -3.90604 | -48.33483 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c41f990b-e085-3dfe-9598-ad2b455bbb42 | -3.90324 | -48.33078 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03579f5c-593c-3d48-a2af-f60c59a4c6d7 | -3.90268 | -48.33431 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d728421a-df07-3b68-af53-535d2aeb2e65 | -3.90044 | -48.32672 | 2024-10-20 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28f590cf-74fd-30e3-9512-f4c41ad622b9 | -3.8082 | -47.80106 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bec33b9-ec1b-3d66-8b82-6c6f4e3edf3f | -3.80487 | -47.80054 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9447b9b-518d-3429-996a-8f62b6005556 | -3.77424 | -47.73512 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a88c78a-a45e-3bfa-bd73-0fd130076858 | -3.77091 | -47.7346 | 2024-10-20 04:32:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd48884f-dc5c-345d-b523-4c0ad768c587 | -4.4 | -48.61298 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0b5d617-593b-3a48-b77f-a59610fdd862 | -4.39662 | -48.61244 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8ffdb7b-bdff-3ed4-98a1-0287d3850d99 | -4.37751 | -48.60212 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11ed7359-7fbd-37a6-8317-d066633d4d98 | -4.35047 | -48.56821 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05893c10-f794-31dd-9f1b-13e899d1eea5 | -4.34767 | -48.56411 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c8ff6cf-a64e-3c67-86f9-a1ef7f3fa4d0 | -4.3471 | -48.56769 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83b1784b-e844-3590-914c-114583b1fb21 | -4.34654 | -48.57127 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 076f8687-b92b-30c5-91da-1b4129a9fb55 | -4.34562 | -48.71485 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d6cd97-07e0-35c2-b292-9c9448bb5d34 | -4.34429 | -48.56359 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18d8ff7a-dec9-3a5c-96e2-871623be68b6 | -4.34373 | -48.56717 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1290283e-7e2a-3402-8b2d-c2448d06519f | -4.34316 | -48.57075 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f044013d-e594-328c-b5a2-e1d7200e38d0 | -4.3426 | -48.57434 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8e05a9e-b4ba-32b8-b17a-072484a2e756 | -4.34223 | -48.71432 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0324a9ec-ae1f-3edd-856c-514aad78efc4 | -4.34145 | -48.62544 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21be14a0-f772-3522-817f-bbfab7e88856 | -4.34088 | -48.62901 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 338252ee-f963-342a-bead-0f064ac081e3 | -4.34036 | -48.56664 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acd0c2c2-526a-3d6a-97bf-7d64a5ec403d | -4.33979 | -48.57023 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d655e02-9891-3d73-8b07-39fef8df8f52 | -4.33698 | -48.56611 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0970f215-99a1-3df3-8164-a1b7a9c7e67a | -4.33642 | -48.56971 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a073dece-8f53-3490-8a15-f3a449e53ba2 | -4.33245 | -48.61667 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 32897238-91f7-3878-a667-4831965d4613 | -4.33188 | -48.62024 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 300e96ab-41cc-357d-a883-c3f6c36e226a | -4.33132 | -48.62383 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3937a138-5541-3d11-a604-a87e25facf0c | -4.32851 | -48.61971 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 212ea7bf-3990-3ef8-bc47-717041beac0f | -4.30821 | -48.6386 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c27a69e7-5cad-36a2-8ff0-047de5664fac | -4.29644 | -48.60366 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53a08895-c7ec-3de8-9e33-e25c88dbd0ba | -4.29307 | -48.60314 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da84c507-09b5-3e2b-86be-83417fbdfc56 | -4.28965 | -48.62463 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad99e07a-d992-30d1-aca7-3e189d59ffbc | -4.28627 | -48.6241 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798269d6-d0e0-3e1d-a672-607a40dfb7f2 | -4.28066 | -48.61587 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73706708-6bb0-319c-b9fc-dd0bb8cd69e2 | -4.20663 | -48.61939 | 2024-10-20 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a66cc24-0167-3f4e-b326-05e7a1703a12 | -4.05845 | -48.82586 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42dc0ebb-ab07-3195-a440-0d316ccd227d | -3.97451 | -49.02283 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 46994dda-8516-386d-bea6-420125774697 | -3.93904 | -48.91978 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0beaa642-15ef-3ae2-b72a-74b84e287337 | -3.87492 | -49.07985 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02d80314-a32d-3f68-9a11-d43bc64fbf9a | -3.84096 | -48.96491 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 432ba43b-d96d-3138-861a-a0c37ca64999 | -3.84008 | -48.88199 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| da53c69d-04cf-30ac-8401-8d51f52904b7 | -3.83812 | -48.9607 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 642ce215-b878-3f9c-a416-dd2d16acc09e | -3.83754 | -48.96437 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19406c96-cb39-3bed-9697-4e0b2b16d6e8 | -3.83696 | -48.96804 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b62855c-d32a-3108-bf2b-29cad01f25d9 | -3.83667 | -48.88144 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| efd55708-e7cc-3182-a2ea-578c52f5c41c | -3.83608 | -48.8851 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 337b0bee-a171-318b-a46b-e6408742bd31 | -3.8355 | -48.88877 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74819440-763c-3e5e-b09b-8398be3d9e19 | -3.8347 | -48.96016 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2e20fc3-4f3a-3a00-a541-154b2d4dc60b | -3.83412 | -48.96384 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 090e4664-d159-3e8c-8777-9e0c9921335d | -3.83384 | -48.87722 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c8163b2-9a49-3843-8869-925818fdde00 | -3.83353 | -48.9675 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c92deae-8f9a-387b-afa5-78517e1c18ca | -3.83326 | -48.88089 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 113b3bed-5f28-3ebc-99a5-6da1475ac81c | -3.83267 | -48.88455 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c3757fa-b708-3bf5-aaf9-be018cedb18e | -3.83209 | -48.88821 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b4b466d-e6ba-38cb-8ec8-8c2da985f4a7 | -3.83128 | -48.95962 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1eb7c6ee-9dc8-30d9-81b5-89a2d5c425e8 | -3.83069 | -48.9633 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72e465e6-ffa1-3b2b-b705-c8ca52e3851f | -3.83043 | -48.87668 | 2024-10-20 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README36.md)
