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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78b8b681-e78b-3274-9f36-0d47edc4b37c | -2.01635 | -48.06708 | 2024-11-30 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ff72c23-0b8d-30f5-bf97-180b5c8160eb | -2.83371 | -52.94442 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46227c68-175c-36c8-b327-0b20a55f8ee5 | -2.77972 | -54.03048 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17a1dda0-c3a4-3577-bf9b-4465d5e6663c | -1.53673 | -51.56576 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83aa0dec-b03d-3497-b711-2f33139da04c | -3.70832 | -47.14455 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82b3fd5b-e311-3e22-85ac-40b79ef1c3b8 | -2.91799 | -53.07529 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fdbdefd-3957-35a9-8296-87a132a751f7 | -3.00063 | -53.72857 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8af132d6-2743-3f9a-845e-b434c256c34f | -4.07391 | -50.03112 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8765efc-76fb-3609-831b-9ee644dea5dc | -1.3699 | -55.8787 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd0bd49c-1bb8-370a-9211-b4c9ed4adb7d | -3.08049 | -49.50481 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69275590-4570-313f-94fd-6e9ec41894b9 | -1.59187 | -51.26539 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b688d475-0ec0-300c-9b9f-7e536c376f88 | -3.81912 | -46.5545 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d43856d-d6d0-3970-b110-8fcf1eeb202f | -2.79677 | -53.04517 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 175ad195-5b11-36b0-8bd1-277d189f3b47 | -2.08341 | -48.54078 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb24864b-cfb3-3ac5-abc4-05bd50d634d7 | -1.08344 | -53.35413 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47086e96-092f-3413-9403-52080ebcccbd | -2.85974 | -53.93505 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecc68873-fbd1-3d44-9f4a-a55d70ffdd1e | -1.15856 | -53.58587 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5994040c-bd68-378d-8939-46c8655e4b52 | -3.43513 | -54.53864 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db8c0fe9-7549-349e-b6a9-19107a7f9b9e | -3.18713 | -54.32602 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56d721b2-b657-38f8-b518-aeb02fa3e654 | -4.15197 | -48.9943 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2147d2f6-7e93-3305-aa29-a23609974f6b | -1.06588 | -51.75935 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faebd4ed-4f9f-3b04-afd0-3222e773034c | -1.09132 | -53.39165 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59eb5a34-e307-38f6-abc0-f317abb82a90 | -2.20726 | -48.55008 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cc14b03-bb81-32ec-a835-b8ff05ead898 | -3.5953 | -50.37563 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b007a52c-69c7-32bd-88be-b14950bc9f54 | 1.89467 | -55.71969 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89a6cb10-7d58-3848-aaf9-8cc36832caee | -2.26616 | -53.4695 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 296b70bc-1da9-381a-901e-3e5c3d580321 | -2.86907 | -51.65401 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23886401-d700-33af-9121-63de7c152d6c | -2.98771 | -53.29596 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0770df5e-5a4c-36c7-9985-fe833596ec1d | -2.88214 | -53.98891 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acbc831f-dd1b-3382-8a31-c38b38330faf | -3.10758 | -53.1791 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4a796ae-e980-3e8b-ad57-d51679f1f73d | -2.75746 | -54.11668 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cec95020-6de0-3048-8f9e-0f8b28bf95c9 | -1.37018 | -55.18841 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b83a825a-1d95-34c8-8a61-8a35e01c45e0 | -2.82886 | -54.08828 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a00b5d9e-c9ae-32b6-8e0b-bb8776d1d458 | -2.6022 | -54.08838 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 777b3087-42a4-3eb1-af2c-55cbd3f1f119 | -2.61829 | -54.07302 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcde6fb5-fa94-3e15-b2c2-6b252bf8c0b4 | -2.00086 | -52.09769 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b875e812-41fa-36a2-ab23-256c0957bde2 | -1.46554 | -54.49653 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89a855cb-715c-39f8-a077-47bde67dad5f | -3.35702 | -49.75866 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa3a31a9-9472-346d-8d5e-a9b41dba1b4e | 2.37019 | -61.26139 | 2024-11-30 05:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd4de9ee-8818-35b7-b9c8-98f4d17be0ad | -1.1591 | -53.58241 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4c4505f-0c39-34b3-9adb-f6a32f28537d | -1.08516 | -53.38704 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c1d7e05-d0a1-3f26-83fa-d5d8e4aee367 | -3.37244 | -50.17975 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f0b1475-9558-3d19-8be8-d1aa3405756a | -3.30036 | -50.37731 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5286bb4-90eb-31aa-aba8-c8436d413a25 | -4.06474 | -49.06483 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 579c0b14-7f0e-30ea-96dc-b0b325bc7f30 | -1.05369 | -55.24541 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2789f44-031a-373f-891b-138d0f60d3f7 | -0.96416 | -51.65063 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7234378b-d400-3e0d-a2c1-a8cafb678edd | -2.38285 | -53.68084 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb0d4903-7720-386f-918d-429432fb4a93 | -1.05757 | -55.24243 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97d80201-17a3-3a7d-82fd-9f8e193277ae | -3.49527 | -53.80433 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e0f11a1-cd53-35e9-9b5a-fa533eceff59 | -1.71308 | -52.62757 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d181230f-8a8a-310b-ab9c-462bbdbf4f80 | -2.63202 | -51.76624 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa573a6f-9452-3b96-8e27-eb6acb9c02d3 | -1.7759 | -46.12561 | 2024-11-30 05:01:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00669ced-94a3-3ab7-9c23-13b6f1e1e1f4 | -2.58019 | -53.67109 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fe012dd-7be2-3044-ad52-17c091f28ca4 | -3.63138 | -54.53752 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a96244c-11ee-32f3-9506-4d6ea6e712bb | -3.33779 | -53.22114 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc31340e-5964-33fd-8db4-af2134965514 | -1.45221 | -54.4733 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66da51b6-ec2a-3f1d-8199-d244e022b98f | -1.34297 | -52.12963 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c98fa18-02d9-3977-b164-e94830cacaa1 | -1.66403 | -52.40826 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a8d804a-0f72-38fc-9dac-356bd6dc48a1 | -1.09858 | -53.36734 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35153bdb-68c5-3c32-9b9a-0d24dc426261 | -3.48103 | -51.25676 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 926f7371-4bc6-3791-a71c-058eb788442c | -2.97583 | -53.28281 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bba955c8-2224-3cc9-976e-0d15917057d4 | -3.10031 | -54.04391 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43d684ed-19ba-3d9d-bd55-f5a32fb357f9 | -3.60808 | -54.21574 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d413aef-372c-3d93-bca2-e64562fcbcac | -2.66358 | -48.79178 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38474a3e-4e0f-31d6-8bee-d171d49f1837 | -1.53185 | -51.61978 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb9ab342-6047-3ac8-aa44-40d8454816b2 | -2.44119 | -53.62426 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 402f6c8b-d181-33be-968d-03389a693b02 | -1.37055 | -53.6368 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 858b8024-8cc8-3914-aae6-a9b47f9ce6d6 | -0.98623 | -53.67437 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eab49e28-555d-3910-bfbc-76dbdd9d7f2f | -3.0982 | -53.72885 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4b5d7db-1ef3-3895-9daa-9c11f258da2e | -1.3334 | -55.84748 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 34e6cc44-1a35-3c11-8769-e74d50b9845a | -1.25444 | -54.54832 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6650c93-f397-3fad-9368-fe44466ac252 | -1.5361 | -51.61622 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cea604c-a684-3327-a2d1-43fdbdbd081c | -1.14654 | -51.68092 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b831c7e7-cc85-3e4f-aa8e-fd09d23efb53 | -3.16139 | -46.29863 | 2024-11-30 05:01:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ceab95cc-a8a0-3b28-bb07-d975e653dfed | -3.26768 | -53.83153 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63b4ce22-b80b-3ce0-a506-bbce504469aa | -3.02228 | -53.41246 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d327479f-11b1-33f1-b1a6-ad1fb11cd706 | -3.161 | -50.5812 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fd140f6-4887-3be5-b9fb-98378755b21b | -2.63942 | -54.06913 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b77f9d06-5918-3da6-84fa-43ca13cfda7d | -3.05235 | -51.06097 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aefa58ff-9f94-3dc0-b467-59b3c7215b19 | -5.20946 | -47.19294 | 2024-11-30 05:01:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a5e9d2-55d1-3e68-a0dd-786581956a5d | 1.94886 | -50.84763 | 2024-11-30 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfbf16d4-df2b-3371-8352-f09626008c55 | -2.96508 | -48.0328 | 2024-11-30 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dd1c68f-e86a-3ed5-bddd-f844e7239557 | -2.84776 | -54.07687 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b946376-35c1-3b8b-97a3-dd9c093b1773 | -2.69229 | -51.97937 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d470464-3b2f-3ea1-a013-2c5d4c0b6e75 | -2.02809 | -52.08115 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b4746835-7b33-3a73-ba60-5a661c88e4b4 | -3.41566 | -50.1651 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ea297fd-e519-3076-affb-c110f8a0e8f6 | -2.64441 | -54.05917 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 853fed55-34c6-34a4-8215-8079341e14c8 | -3.76597 | -50.17905 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 377c1990-73e4-3b5a-8c64-b4dab4e14032 | -3.78189 | -49.36408 | 2024-11-30 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47bb8554-df64-387f-9e05-012c7f831d2c | -2.84442 | -54.07635 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 340bbd06-9254-354a-afb3-502e3fbd04ac | 1.4834 | -55.94839 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2467addb-3dce-30dd-9313-f6a221b8cc55 | -3.25228 | -50.61285 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc1248ce-1687-3c1e-b01d-0eac09e925d0 | -2.62306 | -54.21649 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7467db43-0769-3190-a403-43c14ffc3a7e | -1.32681 | -51.67712 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f8c41ca8-d559-3205-9f84-a9a78f89b3d0 | -3.2278 | -54.17518 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83b2b858-2bb0-3889-9e96-5eb04b84e6ff | -1.42859 | -54.88232 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 689beb7a-f1e0-33af-be9c-068c895dd985 | -3.09043 | -54.12184 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c967dfd-3e0a-376c-bac6-33ef4cf251d7 | -2.3646 | -53.86206 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e2bda31-ce1d-3de3-8ebd-79cd05604575 | -2.60548 | -54.06746 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa667c4e-e343-3287-aaf1-d82d68c641cf | -2.78142 | -54.21655 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README76.md)
