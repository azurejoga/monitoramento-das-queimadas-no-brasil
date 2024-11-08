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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf92c331-c35c-3edd-a09f-6a1693d02d71 | -4.68138 | -46.4479 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a93865fe-193c-34d6-a98f-eaf68f67009c | -3.36178 | -53.3891 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4982b135-5f6b-3e33-af1d-41295987ca03 | -2.95131 | -54.45534 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b18720b3-c825-39b0-acf0-5a1ed5ed6c6b | -4.57138 | -50.60231 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55004209-b35a-3b50-8147-b9491bb05941 | -0.89661 | -51.76983 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c9f0088-a593-3839-8431-9f77df9fc8b5 | -3.15871 | -54.47509 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e98e9a6c-dbae-31bb-93fb-5196e5a9637d | -3.03228 | -53.27579 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7c90761-7e1c-3446-92d1-6eba01166dcb | -1.59191 | -53.72792 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2fcf13e-6dc2-316e-a838-7ed5339d1410 | -1.14098 | -53.71585 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26185010-9e32-366f-b9fc-936711943cf8 | -0.91372 | -51.66012 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 514219ac-34c2-35e6-985e-91a048638d6f | -2.80016 | -52.93593 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8944a950-8a82-34ef-a425-a3e951ba713c | -3.02669 | -53.26767 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 836cfe93-7f2f-3b4c-9814-d9b603595349 | -3.09337 | -53.31778 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dff8edb6-8172-331c-9070-c7fb4bdd19c3 | -11.87271 | -47.70845 | 2024-11-08 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75da49a7-bcac-3bc9-8785-73614293562a | -1.38047 | -51.43826 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9dea2d8-fca0-36a5-9517-51f490fad997 | -2.17503 | -46.44251 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b9cb3a8-05ab-32a8-85cb-ca7dd2896940 | -2.05906 | -53.27843 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82d93fe9-c067-39d1-9589-b9d4c4fb6006 | -1.49847 | -52.5573 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e75be992-cde8-3e25-bf75-ebd9b02827ef | -1.45724 | -51.47116 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d902ccc-189f-30fe-b71e-097523ad6a0f | -3.96377 | -48.13845 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 872b68d7-ad78-3227-b3e4-9801d8fc6a11 | -3.1422 | -51.2009 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df82d414-f803-30df-b600-6678bec0c6b8 | -4.46771 | -50.25095 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39d8657c-75e0-3454-a201-dcebb0308b32 | -2.82805 | -52.90792 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cf83ed9-1a4e-35e5-be80-e3143b07c8a6 | -4.0728 | -48.31892 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18819834-8f90-316e-9c2f-6aae5d70df53 | -2.1626 | -53.69341 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00b8d204-f9bf-3275-8a47-69e35a2bab57 | -1.20577 | -54.20582 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8689c88-8e83-36e5-9470-8365b55faf5a | -1.71014 | -52.33404 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a8d7935-f5ff-3ca8-b44b-a086160a4541 | -2.94172 | -52.7043 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07b1a76c-782f-37c3-bce4-09d8826fdbdc | -2.96041 | -53.86478 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e0ee19c-28da-3625-a216-3793cb20b431 | -4.67913 | -46.4025 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 144834fd-75c8-324c-9f3b-4000591b300c | -4.77247 | -45.74459 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60083ed7-dd32-3c36-bf00-e8d77eb47ea8 | -3.0098 | -53.44051 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a9421f-0974-3842-af05-d00c77726cd0 | -3.96641 | -48.17187 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5d869283-d4e5-34cf-a6c4-edc4cfb89e7d | -2.16201 | -53.69711 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf24486e-7253-3763-b2ad-b124dab27321 | -0.64703 | -52.38861 | 2024-11-08 04:53:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 315fb0ef-98c9-3c06-a813-6cbd3465be80 | -3.38202 | -50.21767 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9ff3a05-64b4-3003-85d0-df5dce774517 | -10.73078 | -49.52323 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 884885f5-d994-3c65-ba02-6bd94e5e018a | -3.38374 | -50.22922 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 423e0575-b8b0-322c-9250-0cd0a8a91a1a | -1.2259 | -54.1752 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a586b98b-9a73-3cc8-b012-f5814e2298e2 | -12.32088 | -48.00839 | 2024-11-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87ab5084-7d29-3156-a0dc-b6fbc166c674 | -3.5495 | -47.37535 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c908993-39e0-3557-a538-69e709d3ec3d | -9.03442 | -61.99535 | 2024-11-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fb2e2dd-2c97-3275-b557-1c7884194c4a | -4.77619 | -45.73378 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54c97fd9-4811-341d-94c1-e087383508c3 | -2.45051 | -53.69179 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cc630f8-229e-30f1-89da-ab89c49b6e9b | -2.62309 | -51.30136 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 159221fd-dd2d-316f-aa2d-73bd5644411f | -3.05202 | -51.34322 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f5c349f-baa4-3ad4-9c83-f7df53f586c1 | -3.88371 | -43.15049 | 2024-11-08 04:53:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61b95254-a11b-310d-9e90-273a2079b8fc | -4.78699 | -45.40921 | 2024-11-08 04:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f1f5f83-61f7-3b68-a92c-669e7d3ae050 | -3.25712 | -53.40584 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b486b5ad-7496-31d3-afaa-52ccc939aaa1 | -1.14587 | -52.006 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f45a118d-2cb1-3efe-b416-71232d8fe063 | -2.29759 | -48.55745 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11595228-36d0-31e2-a75b-a4702ada66bb | -1.72146 | -52.35054 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4191fc87-2fa1-3159-b300-08b09a490054 | -4.56018 | -48.01542 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 5f6267ca-0a43-3040-a4a0-3a7735c9cd77 | -3.24572 | -50.4646 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d2977ed-e0f5-3618-a5bd-8d2d24814534 | -3.40703 | -50.28151 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3a1d29c-b3ea-36e2-b808-d0ed19d44f58 | -1.34301 | -51.41847 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b0af91a-54e4-35e0-ae1d-259403ed5a72 | -1.2192 | -51.77465 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0d451ac-f7bb-3cbf-97b4-4acac6aaa8a9 | -1.45993 | -53.4949 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac6b1d58-b643-35d6-8e8f-64b0d2bf17b2 | -2.13324 | -48.74202 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c49d6b2-0ff3-31b1-9c11-9275f676db74 | -4.07569 | -48.31735 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a20fb148-c326-3a2a-9ca0-4cbe7709699e | -2.23852 | -48.37666 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ae6c1ca-02ee-344b-826b-61937afde634 | -3.32499 | -53.18734 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6eebe98d-d117-359e-860a-cbb70a1164ba | -3.37861 | -50.21715 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25090139-31b6-3760-88d1-b73feee96ec4 | -1.54574 | -51.20716 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d537189b-0983-3da6-b834-e31192ce23f3 | -4.30607 | -46.74466 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de44d6a4-8648-338e-9373-c738f5889730 | -3.89579 | -50.25288 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e4698e6-c905-3d50-b087-d2fd1895f895 | -2.23263 | -48.02545 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68586de5-ead2-3769-a613-2e6dcd037b59 | -4.61342 | -45.97875 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a49c1532-4a42-3af6-aac3-7199df65f728 | -1.13755 | -53.71526 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 080bb3b3-9b6b-37bf-8d85-c896307241eb | -5.98326 | -45.36981 | 2024-11-08 04:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 97a1b926-84e9-36f4-8275-bc05c3f89b7e | -3.19999 | -53.39697 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20dad6c9-2b33-3154-991b-4f30f540d17d | -4.24369 | -48.02573 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f9d1109-54a3-34bd-ad9c-051cdde19b89 | -1.70449 | -52.67557 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4b70533-4e00-3949-8880-8ae737f75ece | -2.08232 | -54.69955 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5310f9ff-e27b-3e65-b9b9-f9d43d737119 | -3.00992 | -53.24333 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb1b3814-56d6-3294-ab9b-8ccda749244f | -2.92795 | -51.047 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a71f19ee-85fd-3f55-b5fd-79fb3b06dbf0 | -3.24062 | -50.45276 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d875cdec-9a9b-388a-bdcb-2e56fa401148 | -1.32 | -54.66043 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d253d8f7-f676-30c5-9136-f3eff5f16e69 | -3.20198 | -51.03513 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30bfe86b-92d3-3c4b-a7c2-135587efd9c0 | -3.03514 | -51.53844 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c540f5b8-a274-3c44-8c47-c60d43a56e3c | -2.82198 | -52.94641 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d742691-bad9-3346-9dd3-bf1bb9f5b7ca | -1.59075 | -53.73535 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efb5d4e9-fb2c-3f61-9a79-738b4d7149a0 | -2.76169 | -53.22629 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36917af1-9978-3289-bff5-fa4b4a2aac5e | -3.0126 | -53.44465 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ee0c38-51e9-3c2e-8453-8b4ce018bb43 | -4.51056 | -45.69809 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b90e48fe-dff5-3e93-a4ad-182a9573a43a | -3.11425 | -53.71166 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db69523c-829e-3124-b8c2-d481be0b8e0e | -1.50528 | -52.16442 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc7bd3f-e349-3e64-bba1-e194658129ee | -2.61173 | -51.74689 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88da451f-91fe-3daa-8d4c-63fb8374c338 | -2.43361 | -48.47311 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a36846-394d-3bd2-a967-6b436f3fe34f | -2.88796 | -48.28814 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5dfaaf6-c5b0-3941-8c10-14ce5f893b79 | -2.005 | -47.94431 | 2024-11-08 04:53:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7ec9150-86fc-3b51-8422-8a29b8618a2f | -3.4523 | -50.37766 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf853ddd-9e5e-344c-aa7d-03658b981f14 | -4.51231 | -47.59411 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf718d97-78a9-302b-941a-bec0908c9e37 | -2.17375 | -53.24088 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c32e415f-9507-3593-a261-09d0592dfe32 | -2.72339 | -54.146 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 921f9ed4-5592-36f5-bcf6-d4e902574086 | -1.48672 | -52.06637 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a75b0eed-c0d8-36a8-b6ea-8df500b8d119 | -4.77311 | -45.74005 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2557b526-2344-3686-82a8-963f8d950a58 | -2.27874 | -53.80195 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fb4415e-cd22-3b80-bd29-2416f214707e | -2.97684 | -50.29436 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 753030fa-caec-32bb-a9e1-05a9e1c64f65 | -3.24424 | -53.40017 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README29.md)
