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
| 994c243e-94d7-3151-ab5f-fdf4357ad823 | -2.18 | -53.2617 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc764f1-a27e-3d65-848f-5907c14b8634 | -2.8547 | -54.015999 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d39390cf-74b7-3ca5-812d-8ecd0a808a73 | -3.3515 | -50.520599 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f684e689-be2b-32d8-9660-fa1ba2f04e95 | -3.7521 | -51.827499 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd69b88b-c185-3576-a228-865beea59a58 | -2.5933 | -54.0448 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ddf0e0-b620-3e29-b8fa-eabde4b4b813 | -3.0917 | -49.206902 | 2024-11-28 00:38:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef57814-97b4-3f96-b217-fbe4cc0203f9 | -3.4017 | -50.108898 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab8c5cd3-0fb5-392f-93d9-cc298acba39f | -2.8972 | -54.159 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fcf3ee4-76ca-3a34-9b39-61f6c69c58a2 | -3.0897 | -53.274502 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55ff0b3e-1456-3874-abdb-f768e8619a62 | -2.8744 | -46.844898 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7566437-c926-33f2-8e03-6af836cc2d02 | -3.4437 | -50.0224 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53544bfd-9346-3df7-a7f7-4ef7444fe3e8 | -3.1062 | -53.2565 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ceb8c50-e906-34a9-ab15-2bc0144bda3b | -3.4456 | -50.030602 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9650ec7-faae-3b99-af2c-85d2bc089973 | -2.7509 | -54.104198 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fa7829d-8b67-35ff-8e76-53c169cca061 | -2.848 | -54.031898 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a174398a-d9e8-3b89-a508-44f10fcd4585 | -2.4759 | -47.030701 | 2024-11-28 00:38:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfff3603-3bc7-333e-b105-38a4fb8a8e6b | -2.5526 | -54.0466 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a406a7ef-61b0-32e1-878d-ad1e46991c27 | -2.8481 | -46.864498 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7338ef97-8808-3026-a124-cd7d913fddf5 | -3.9748 | -54.602501 | 2024-11-28 00:38:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9561befa-ee0f-310d-81dc-af23b0695dac | -2.6089 | -51.7859 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a05ccb80-8ab4-3a7e-98f1-389b9f5d9dde | -2.3082 | -47.860401 | 2024-11-28 00:38:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ade6fbe-54fd-3c29-8584-4e6b3760c59e | -2.2515 | -53.624599 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7b12432-a683-3c66-a788-9053308cb1c0 | -2.2438 | -48.518002 | 2024-11-28 00:38:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5583c45-cd54-3cbe-99c2-ac3f83237c0e | -2.4402 | -50.410301 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dc81555-9291-32bf-ab13-1e08c2bf26ef | -2.7513 | -48.667099 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02cd1a3a-65da-39d3-aa75-38e5518e4220 | -2.968 | -51.007801 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1a1242b-623a-3163-96b9-20e6ca0babdf | -2.8733 | -53.9613 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4841124a-c789-390f-87da-8e3691414eca | -2.6011 | -54.079201 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72060ac-b63d-3068-a8fd-acf4fba1589e | -2.8666 | -53.9772 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b24416-15f5-3269-b94f-4f8476bc476b | -2.9442 | -51.583199 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589f3022-c820-3587-a719-fd1aa1cf6cc3 | -2.8155 | -54.024601 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3069ff38-ad0e-3020-82a9-68b371d72463 | -2.5877 | -53.9739 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d772ca-e6c8-34f4-936c-3bf6d7bba2bd | -2.7785 | -52.900002 | 2024-11-28 00:38:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6c47ad-79f3-3475-9fe2-3c55af70bfe8 | -3.4085 | -54.280399 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21413662-1ab3-3578-9013-8721d9432369 | -6.0974 | -48.040798 | 2024-11-28 00:38:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4fbc95c-a955-3843-bc92-264753cba12e | -2.2554 | -53.459301 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba11d17c-7cfe-31f1-813d-12de4e26f930 | -3.1177 | -53.994099 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6b8c72b-c409-3d4a-8f7b-d3a7f2e068bd | -3.095 | -54.1227 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a40e272-0f4c-3c4d-a975-5457953ed3af | -3.0557 | -48.514198 | 2024-11-28 00:38:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13f06473-1a9b-367e-92b5-56c4eee38987 | -2.6573 | -49.512699 | 2024-11-28 00:38:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41323725-85ce-332f-ac29-4b4706e1013d | -2.5846 | -53.960098 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09db89d2-3cd3-3e1b-a0d2-7144ad96912d | -3.2458 | -53.922401 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaed5a41-77cb-3356-98bb-df06abd9845d | -4.7846 | -44.4179 | 2024-11-28 00:38:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99e930c8-40dc-3657-9bb6-5fb56f8883db | -3.533 | -53.7794 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaed4de6-d16e-3552-a2e4-d1102e097d59 | -3.2519 | -50.761398 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6f438ea-515a-391d-ac37-0c4ac474c989 | -2.863 | -54.006901 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84be8a98-4a6d-33f6-9638-f9568ceed53c | -2.8511 | -46.877399 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 976c29f7-5262-3079-ad6e-177f7e79625d | -3.2945 | -53.680698 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e18e617-c1bf-3f3e-9b7d-5b6b3fec2963 | -2.7418 | -48.8941 | 2024-11-28 00:38:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8531a061-9807-31f2-8209-fc233f0b67e2 | -3.6133 | -52.534901 | 2024-11-28 00:38:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7cd96d2-ee2a-3092-825f-193df2f1c34e | -3.7104 | -43.441898 | 2024-11-28 00:38:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08703daa-01d2-3cb4-863a-fe65b90665e6 | -3.9748 | -50.181499 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60ffde8d-c82d-3b7b-b44f-c546c144601c | -2.6043 | -53.9557 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5d428b8-8b8c-3047-8189-707d4e9ccaab | -2.8434 | -54.0112 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5de179b-1419-3e01-933f-29ddf9b1b947 | -3.5051 | -53.792702 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af50a77-0f5b-3d90-87fe-330d1a3bfd60 | -2.844 | -54.1054 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1ceb63e-7619-3b7f-98e5-42b0d6ec57fa | -4.6069 | -49.389301 | 2024-11-28 00:38:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 669715be-3aa1-393c-9850-f7e4f1efc679 | -3.1167 | -53.8064 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9845769-3fad-320b-9f97-557db2e6ac3c | -2.7623 | -54.108898 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74168e6e-2903-3b21-9220-96f178bdcee8 | -2.8134 | -54.061298 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06140e4c-2f57-315b-837b-ed26bc64bbdc | -3.2512 | -53.625599 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc7e31e6-4f5c-3249-b9ff-9ca3b72cc7d6 | -2.7406 | -54.150002 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c8f5505-da2a-370a-b1ac-68d8f1d35fcf | -3.9642 | -48.081799 | 2024-11-28 00:38:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dba8714-abe0-3302-9f61-783384561135 | -2.313 | -48.1488 | 2024-11-28 00:38:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69463e8b-e5d7-34da-8a28-d25fc53e5c89 | -6.174 | -42.633202 | 2024-11-28 00:38:00 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b0a9cb4-d02f-3f5f-aefd-a4b5e1a908bb | -4.0523 | -48.328098 | 2024-11-28 00:38:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f00f257-a148-3806-a341-a20f22e7047a | -2.8351 | -54.020302 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61345187-e346-37ff-b71a-f2951fb588d9 | -2.6073 | -53.969501 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcc8fbea-03a1-3463-bfe1-87511e294cfe | -2.622 | -51.752998 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e616f35-d399-3ba6-b707-a5c0c235edc4 | -3.5217 | -50.498501 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63870d54-6d98-33c1-834f-1bc8f7754524 | -2.8736 | -46.8857 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15ee71dd-3558-3c76-957c-21042af19cb4 | -3.6149 | -52.541698 | 2024-11-28 00:38:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f22cc93c-4581-3457-b59d-03f1ed3e334f | -6.1685 | -42.610901 | 2024-11-28 00:38:00 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c4bde8a-a8c9-383c-ad30-a8d397e5ba3e | -2.5598 | -53.987202 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd94ffb-58d9-3bc9-8abf-cf7ea7d92fd6 | -1.5318 | -47.299301 | 2024-11-28 00:38:00 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4cc935-54de-3916-96dd-fe7fbfc5ee59 | -2.786 | -54.031101 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e53d475-0543-304f-bf6e-962f0a48274d | -2.7956 | -53.2038 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7b7b406-60fc-3b10-a10d-7e8f440f1531 | -4.6766 | -44.609299 | 2024-11-28 00:38:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af069468-d488-3f84-87a1-abf4ce6431d2 | -3.798 | -50.129398 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9da84d6-e903-3001-a838-698062b59dbf | -4.1843 | -48.452999 | 2024-11-28 00:38:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6845843a-5755-3c70-bc45-0817b7d888f5 | -2.5724 | -54.318199 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df06fcfc-1858-34d2-82fa-5c18b2c0c4d9 | -3.1069 | -53.808601 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3942e67c-2262-3ae6-8752-41d050a143f6 | -3.8223 | -52.228298 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 240e4102-693b-348c-8f46-0297b37bcc20 | -2.9584 | -51.2826 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9553cedc-1273-3fd4-8b7a-64ae6b9dfbdd | -2.7845 | -54.0242 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f6770ce-31f5-3ddc-8c04-dda0044fdbac | -2.8646 | -54.013802 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4a1855f-8774-3cd7-a949-bb87a6d661e3 | -3.2641 | -53.6371 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1e00551-5704-33f9-acdb-ed9a977988b6 | -3.3348 | -52.762001 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| febf8de5-3a95-3d26-baee-b022dcd622ca | -2.9682 | -51.280399 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab529e1-7b5e-3f66-ad90-9c6f84c38001 | -3.553 | -50.184799 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92716e76-b3dd-3258-98af-5f60dce0b9b5 | -3.5211 | -53.8181 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6efc2860-dea6-3568-a309-84aa6b9803c4 | -2.2896 | -47.1133 | 2024-11-28 00:38:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73ef1083-a590-3e8f-bf7a-0a0e8680c5fd | -3.4739 | -54.480499 | 2024-11-28 00:38:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ecb11aa-0b61-3243-806d-f556ce87f0d9 | -3.7163 | -51.805901 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e05d95c-2f0e-3515-8d6c-a6b4d5a7f33c | -2.6235 | -54.2705 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11f4ebd5-7fee-34d5-a636-6835844a4373 | -6.0951 | -48.031101 | 2024-11-28 00:38:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e74fdf1f-8512-3caa-bd7e-18aeb1b1fe0b | -2.6172 | -54.242699 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c3ded3-f88c-3769-aad0-c04375dcc6f4 | -3.5359 | -52.1469 | 2024-11-28 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e38e2403-ff9b-3a24-84b9-dffea63bf4aa | -6.1039 | -43.9824 | 2024-11-28 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 85c85b87-a7a2-3352-8add-07f36c8120a4 | -3.1113 | -53.8242 | 2024-11-28 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |


[Clique aqui para ver as próximas entradas](README15.md)
