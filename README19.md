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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab02300e-fc43-31b3-9e97-3de622c2a40c | -8.07451 | -48.01171 | 2025-07-26 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b64f02ea-8446-3aab-8b4d-e4fce23015fa | -4.07435 | -46.90366 | 2025-07-26 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a77d26be-bc98-33f4-ba78-e457b3bf5636 | -8.81507 | -46.74923 | 2025-07-26 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e34e8890-4578-307f-98a9-5984f38de56f | -6.70396 | -43.05854 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a6a778b-1fd5-3c8e-a69b-21fe4e904e88 | -6.68307 | -58.84395 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3c0a7cf0-6705-3e6d-9534-96e1a6d313d0 | -6.86662 | -43.69062 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c845854-eebb-3b02-af6f-a69e3b059c17 | -6.64637 | -58.86009 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| fad1a629-b0ee-322c-b7af-b66558364097 | -6.87077 | -43.68718 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 639c52cd-6411-32ff-93e1-60c14853a0ef | -6.65618 | -43.05267 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc5c5533-df6c-323b-bc85-2da1bbcc85ce | -6.67239 | -58.86502 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| aa96875a-32ff-3127-bedd-bab74c3c27ae | -6.65496 | -58.85336 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 296.7 |
| 5de5dd78-f356-3dfa-a181-31c46637dfd8 | -7.29108 | -60.18515 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8980151-90c4-31ba-b277-8994e65fb395 | -6.67658 | -58.84268 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3671fe2b-22ca-3424-bb41-68d4f9b99ce0 | -6.643 | -58.84513 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 31339cbd-576d-3d97-82ad-745f92ed663a | -4.32493 | -48.3889 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfb15c64-07d2-32dc-a0b7-f529a3d29276 | -6.66567 | -58.82914 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 82d5de02-6105-37bd-a765-2526e713bff3 | -6.66695 | -58.86146 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f986fdc0-5850-3c71-ad60-7c1f91a750c1 | -7.93495 | -46.27479 | 2025-07-26 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1be1da16-d57e-34d7-be2b-d4de2c1abbcb | -7.23754 | -43.0657 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c9a8c6a1-9efa-30ea-ae1a-f7750bf904ba | -6.66379 | -58.87493 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3f55f62-cacb-329b-96d8-e77c341b3ffb | -3.98371 | -47.88872 | 2025-07-26 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 686db571-1822-3639-ae12-df2065fca283 | -6.67887 | -58.86641 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 7e65b220-3bf0-3fcd-92a7-d207dfc4d712 | -6.673 | -58.82798 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 59b49f34-e03e-365f-8e30-6d86c7570437 | -6.61804 | -58.83444 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| b2b84926-475a-3c13-9c05-a70fd3b99a23 | -7.09754 | -44.38196 | 2025-07-26 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ef6bd5b-f130-3c67-b0e7-e013f67b8b37 | -9.02199 | -45.35199 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9a52bbf-7cc8-3e3d-b6fb-2f53771a52f5 | -9.14596 | -47.15097 | 2025-07-26 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c27d6381-30b8-3366-a60b-83e489a82f1e | -6.88596 | -43.11488 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa272bd9-9b19-3fc5-bbf2-e943f8a2c7d9 | -6.22809 | -44.52428 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b0843ccb-dff0-311e-b594-32ae67e3e0f4 | -9.28766 | -40.44553 | 2025-07-26 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 98d879b2-c659-3181-a717-202615722f7f | -3.54374 | -49.54932 | 2025-07-26 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61a96985-949a-3091-bc45-890013c973b6 | -6.16084 | -42.59452 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 4143706b-5c08-3341-a70c-9105bc4e8868 | -6.01448 | -52.16953 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7e03367a-d2d7-393d-9002-bafc36207405 | -8.38045 | -44.6016 | 2025-07-26 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f96f5e9b-ed78-355a-847a-d1f4c006007f | -6.67217 | -58.8303 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 04ec5cbc-b98a-32b0-8f8c-ad60d77ef6bb | -7.83562 | -46.8844 | 2025-07-26 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76cb6b82-22d5-3d05-a599-c1ce3f658188 | -6.39213 | -44.75549 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28d1dd9a-2d61-3da2-b422-a258b54bfb71 | -6.65728 | -58.87372 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 40e59922-87cc-3eb1-9677-f08aa8c51196 | -6.63339 | -58.86086 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| cc14dbbf-bb82-3dc8-98f2-3e924237cda2 | -11.45861 | -45.19008 | 2025-07-26 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2c864bf-b20e-3ddb-bee3-2d58c9d89867 | -10.67897 | -51.89062 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0f8d6cbb-c647-338e-8d3f-bf4b24a2711a | -6.62456 | -58.83557 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| be49a29c-00b6-3ff8-bfb4-2cc471788642 | -6.64201 | -58.8475 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 63de4fdf-baa3-3336-a1b9-fb8b425dd668 | -6.66 | -58.82558 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a09d06ec-e5af-3065-a297-0cb0c0ae90b2 | -6.67765 | -58.83698 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a297ba1b-784c-3989-92c2-73695df3dff8 | -6.61493 | -58.85132 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7fa52c75-dde7-32f8-8710-afee015a1113 | -8.87113 | -45.58134 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da2ed0ff-e03c-3e2e-811e-bf740e76499d | -6.16017 | -42.59894 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| da9d423e-89c5-3b5e-ad11-19d848a2dbfc | -7.23922 | -43.07928 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fccf99a2-fb46-3417-904b-6bb8e189a23a | -6.63556 | -58.84601 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5e1fd604-95f2-3d36-bc0a-2b0706185d35 | -7.79027 | -37.60101 | 2025-07-26 04:25:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9724700b-8321-3c3f-a2ee-7776d8709a75 | -6.15273 | -42.59778 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| cd72d387-abae-3efa-a387-1a84ea276a68 | -6.68097 | -58.85519 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 00d2850b-0d1c-3e8d-8ffa-b1c0949e5515 | -8.06075 | -43.13039 | 2025-07-26 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 047ac239-dd53-357d-b710-37bad945729b | -5.98917 | -45.73011 | 2025-07-26 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 528e58da-4214-3547-b745-7e208ac511a5 | -7.24676 | -43.07426 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0bd8b9c5-2fa3-3f96-8077-4d76af481ceb | -6.66593 | -58.86713 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| bab9ad8a-97a4-3d56-891f-31091ea88488 | -6.93528 | -42.81538 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ace7f2aa-36af-3d7f-b00f-39ea319b7e75 | -3.987 | -47.88847 | 2025-07-26 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50c9c6c7-a828-30cc-9ba8-d3fc8e652c57 | -11.10782 | -45.12244 | 2025-07-26 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77352b36-2eea-3aa5-a9bf-a1942eea359f | -5.29107 | -49.18914 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32b7dd03-81e7-395c-a82e-7669b6975662 | -5.74173 | -43.97606 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bf75b57-9f8b-3c5a-8542-1c94607d5f4c | -7.23621 | -43.07439 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 81fb5dbe-0d4e-392c-9811-c36ce87c94cb | -6.90966 | -44.23753 | 2025-07-26 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f0b13d3-4ce4-34ee-a2e7-a4e4c1b71c46 | -11.11129 | -45.123 | 2025-07-26 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de6fb665-0fb8-343b-b8e2-782b956914e4 | -8.00102 | -45.04365 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b23a3d7-6410-31ed-911d-137d209f23f9 | -6.65349 | -58.82441 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| c2b91a19-d7ac-3a81-abb9-27cfacfa2309 | -5.74 | -43.9642 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97098f34-5d57-3314-b530-c9122100bc3a | -6.6775 | -58.84031 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| ef183e29-260b-3865-843e-776199ec0f17 | -9.80941 | -46.71059 | 2025-07-26 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 398fc2fe-1be6-3003-996f-84197c0dbfcb | -6.67868 | -58.83144 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fb468ffb-d6c8-3faf-8267-8d766186246e | -7.25044 | -43.07482 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b15bcf34-3954-3028-8f6d-032468d757ab | -6.67113 | -58.83586 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| d25a5ad0-62c8-3fd7-9aa3-36ad19a0f437 | -6.65291 | -58.86463 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 01247222-7873-346f-831a-1ee7973dad62 | -7.23877 | -43.07747 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2a0516a9-ac14-39e1-9be0-d75b0109f67e | -7.3538 | -49.78229 | 2025-07-26 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4222119f-fb49-3155-b12f-dbca48c9e74e | -6.88061 | -43.10091 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be4bdcd9-b208-3dba-803a-9d6fb2f05766 | -6.64498 | -58.83428 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| e3bd07b9-4caa-37c7-a9ff-8e9e7dedd16e | -6.66076 | -58.92707 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44361cee-131f-34e8-9b17-08c519113a2d | -8.07116 | -48.01117 | 2025-07-26 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89330e59-cfe9-3a07-b07b-eccdc174e46b | -6.56336 | -41.50566 | 2025-07-26 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1858d65d-4aeb-3ff9-b9c8-1babb40475ab | -6.63855 | -43.04567 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d4461d3-4853-304c-b0ce-57dce19d4f6c | -6.68501 | -58.8359 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 64c7eff5-16c5-3642-aef5-8919394ce45e | -9.232 | -47.55052 | 2025-07-26 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa8b4341-a9f5-3392-8672-27c88c5ab74f | -3.74848 | -49.0476 | 2025-07-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c088b58-fd8c-3569-8f9b-b8a64f182d74 | -6.14967 | -42.59275 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5c59b927-eebe-3b66-a621-acbb57c6f445 | -7.23989 | -43.07495 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| dbb65efe-4174-3e35-a2a5-a205dbf0e6f2 | -5.77102 | -43.64388 | 2025-07-26 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65697ec7-664c-39ff-9116-d38ff22b8f65 | -6.66449 | -58.83789 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 8759813d-9198-36d9-ad26-8ce08eae843b | -4.30668 | -48.10322 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 314bbcf3-3c9e-36bf-89be-3a5b4a0cc288 | -6.39793 | -46.24162 | 2025-07-26 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 408b423c-60a8-320f-af1c-37c054105242 | -6.98498 | -43.32984 | 2025-07-26 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5601ee24-f446-337a-ae1e-28b84b8abe44 | -7.17566 | -43.4937 | 2025-07-26 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76dd53a9-c891-314e-b2c7-76c5182b4aa0 | -9.72996 | -48.02755 | 2025-07-26 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 214ef668-d8cf-37b0-a5b0-a56656803e30 | -5.74231 | -43.97229 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81149586-ddaf-3293-a688-2238c92c5b7e | -6.69334 | -44.16311 | 2025-07-26 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 153feea3-0878-325b-8a6e-e93db5579faf | -8.81561 | -46.74575 | 2025-07-26 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed1cca8d-7c57-35c6-8fd4-2b113e2f2ddd | -6.63444 | -58.85512 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f3c01907-47ab-3a63-b77a-c084782ce942 | -6.68195 | -58.85291 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 6732b4ed-7ef3-3e89-87c2-af85e99832c1 | -9.71018 | -48.94649 | 2025-07-26 04:25:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
