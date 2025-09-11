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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af140222-76ee-3f1c-98d8-58e02ced8a54 | -6.32299 | -47.74401 | 2025-09-11 03:55:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36010980-4f6b-3de4-bdb9-c43f30e23955 | -8.52132 | -45.69152 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f59fe74c-c8d3-3323-8711-9e6484280c2f | -6.45324 | -43.59388 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 647110cd-81ca-3b66-962a-05b019bfe0d2 | -8.08399 | -48.23362 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 66302dc4-8f59-3f0f-a74d-d41fafe2f7b8 | -8.43642 | -49.11113 | 2025-09-11 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8fbfd04-dbc0-3ec5-8681-b6507a9a74b4 | -7.165 | -44.13736 | 2025-09-11 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a3cf229-a37f-3a67-b250-b75699251c49 | -6.70004 | -43.54221 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5af07740-fe70-329b-a87c-8a38694289c8 | -6.32343 | -43.41368 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9886478f-c108-3a6c-a022-9915908b708a | -8.79147 | -48.0878 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a005a8b3-134c-394c-9dd9-f3a3e713cb24 | -12.06292 | -47.58771 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4584f692-419e-3d48-832f-3033802c3573 | -8.04582 | -49.04545 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5721b449-04f1-3505-8066-60171e2eb500 | -11.77203 | -46.49046 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a090f9a8-dd94-3752-9d9f-4634074b44ab | -7.35661 | -47.42618 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67f1bf06-4053-3f04-b4ce-6eb3f3774fae | -11.16021 | -52.04374 | 2025-09-11 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b7cbf71-44b2-3776-8141-660a92c5de9a | -9.04969 | -46.98065 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| bbc7c61a-c3e0-39f5-bade-779d78ad0c5e | -11.10551 | -48.43052 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d0c6c53-2c87-3230-9aef-c2e43525301e | -7.19359 | -44.96642 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb4cbaf4-14fb-31d4-b505-d312a14a03c9 | -7.79033 | -47.93912 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97566bf4-339a-3951-aef2-60160a6a1766 | -10.48627 | -49.373 | 2025-09-11 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2edfeb02-604a-3f34-9576-6bf6cfc212e7 | -12.41344 | -44.71797 | 2025-09-11 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 104493f2-b662-3b06-8d72-937598310905 | -12.48071 | -47.49031 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| dd79eca0-0bfd-3a90-91aa-60ad6ea26c56 | -11.15956 | -48.35085 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 481077a9-5dcb-396b-9ed3-36a44e84db1b | -6.2981 | -44.59074 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9541ed-9718-38f0-8981-6df80985eaa9 | -11.39124 | -43.5255 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d89595de-313a-335c-99ea-c6cd4ef4ca4b | -11.34346 | -46.48171 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5b79aedb-b25e-3339-88b2-298b3616ad1d | -9.78496 | -51.10354 | 2025-09-11 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aad1f65f-9e56-35b5-97c6-9d5207b7e7c4 | -9.00917 | -49.51564 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7f3cdfe-94df-381f-a592-8e1bb2ead53c | -6.22315 | -43.49663 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c81b4c0c-9c1b-3799-b480-09702088d93c | -6.18996 | -41.05888 | 2025-09-11 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53c4e687-10c2-3aa1-ac1e-6da3ca3d8ca1 | -6.40411 | -42.60762 | 2025-09-11 03:55:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c7463c4b-2801-3e91-bf72-a70f195535d1 | -6.39766 | -43.4978 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e1931d7-e96a-3b91-8a11-0424a08123a3 | -9.06593 | -47.04735 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e4c79512-234f-3fc0-af23-ca635f0461c6 | -5.9815 | -44.72323 | 2025-09-11 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf5eff39-bfe0-353a-8399-c46c4080ebb2 | -7.9247 | -44.86627 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a43f2400-c724-3018-862a-3b2092bf587d | -6.15897 | -45.81641 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7c416b2-339c-3fd1-9c29-355a094bba7f | -12.13456 | -44.85738 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8b539017-89e7-3acc-8cd3-09545cbe53e0 | -12.13766 | -44.83965 | 2025-09-11 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a333f645-ede1-3e9a-87a1-becb859072df | -10.37872 | -50.52138 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3fdb391-05f1-379a-bb5f-3d0b725223cf | -5.40971 | -45.93248 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 239d6a2e-a00f-3f04-ae7c-07fca6c24008 | -8.16947 | -46.08323 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f6b21d4-7674-3677-9523-d0a38b5318a3 | -9.89812 | -50.16928 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebfb870f-e831-342a-bf56-e183f71ca137 | -9.07369 | -47.07195 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9cb3e644-6326-3ef4-bd81-49f4298d02c2 | -6.24888 | -43.49101 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bb6586b-59ca-35de-99f8-aa9fc28cd6c7 | -11.96446 | -46.65641 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d13554db-0f33-318a-9839-ef457c9b1308 | -9.72089 | -43.533 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6b41680-607a-33af-8a2c-5aa40293ee61 | -9.0202 | -49.77896 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9da5f407-7e75-3a5d-afcb-3bca7e17b7de | -6.37174 | -45.16421 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69c2317d-572d-3e9a-89a3-4461fde565d6 | -11.48934 | -43.63549 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 361f2eae-6cd9-3602-9213-f896eae4b983 | -10.88968 | -47.25397 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f1c5dfc-1b7a-31f0-8c3a-5e8879996d19 | -8.53111 | -45.6883 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31bd2bd1-2b8c-34a5-a023-78a72e6f5e88 | -13.45006 | -43.48577 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b7ccafe-e289-390c-911c-1988423f0d12 | -11.77248 | -46.5139 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fd51c91-8ff6-3695-aa8b-6b5458176b9f | -5.9869 | -43.7061 | 2025-09-11 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1deb7972-2733-3a6b-91c2-146383992bef | -11.47773 | -43.68119 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df2432c5-69fd-34fb-9d7a-6d2e276696d1 | -11.48245 | -43.65334 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 157872c6-60de-3bf7-9fa5-b23f952dcc74 | -9.98159 | -49.06087 | 2025-09-11 03:55:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5eb4fe22-f274-3b06-a77e-d207e22720ae | -12.12656 | -44.85596 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fdef78b3-ba95-317e-992f-e1cbfdf7809e | -13.28386 | -43.77494 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af30eddb-455d-3c4f-bd2d-02fd5bc05af7 | -8.96983 | -46.07124 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81315d22-874d-35ac-89d9-f26d11a6ae3b | -11.49294 | -43.6599 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3c155a7-57b3-3776-bd7e-02c53675e8ba | -9.83928 | -47.78325 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03c0646f-a189-3e19-8777-e6d0bbf33966 | -6.7303 | -43.02491 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5070348b-833e-37c1-9c8b-e85674436908 | -11.71929 | -50.65793 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4944a4d5-b797-3ed6-ac87-11e465c85e86 | -9.89921 | -50.17319 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8c8bf3e-0ba3-3033-b04b-c2ad312b9fa2 | -10.13955 | -47.89043 | 2025-09-11 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edfb7ab9-831d-3398-8650-bede22f5a3ed | -11.45956 | -43.60639 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1990d567-b102-3c4f-8351-0ebc3d9a4db7 | -9.07407 | -47.08521 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bd64af97-ab71-3b9a-8bb8-664dff9f3328 | -12.07936 | -50.99217 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a32604e1-0166-3184-b1a3-f1ed2a14d9d6 | -6.7504 | -46.35257 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 677bee7d-6572-37f5-a5c3-def0b8f16396 | -11.0913 | -48.44976 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc5d9ddf-5b01-3fb7-8c0e-a8706e5cef23 | -11.8263 | -46.74282 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 416f99e7-f3c2-328e-a847-3e717f7197ef | -10.55261 | -49.8924 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcb11091-107a-3676-b39c-e5738218658e | -8.52502 | -45.69685 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b9def0f-ea78-3ad0-8bce-13500262d252 | -7.8641 | -44.88508 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b31deeb-db0a-39dc-a721-b42754b35d4a | -9.92017 | -49.8707 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7ac4e12-687b-3f30-9248-b74b35c28d06 | -11.31115 | -50.7552 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af931d50-be18-3608-8fb6-5dfc7df659e2 | -13.25649 | -43.77934 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eb5bf58-523b-3a49-a571-27573a913da7 | -10.27225 | -48.82656 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 342e97e0-8fbd-30cd-bdc9-49a34fc7f8dd | -11.02661 | -45.06322 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 881588f6-4368-36d4-8345-6a570bd0f68a | -9.06415 | -47.06898 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bdc053ac-3f71-3144-b8b0-321feaa38140 | -7.21671 | -45.31173 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31e2842f-fbc5-3343-9788-84feb770129f | -6.31488 | -43.41577 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c6bf159-0a16-36e3-8ef4-cea0f1936058 | -11.42921 | -43.57424 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f3e7fbc-3b65-364d-bb0f-75f5b23911a6 | -6.56009 | -43.14808 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1d8b3fc-00a7-3824-a268-94510f2b9e95 | -11.11647 | -48.39978 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fe187ba-005f-3e95-8efc-1c3e0b44fd99 | -12.24549 | -46.75217 | 2025-09-11 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 921fe2d9-9b9c-35c5-8c3b-7eb52d37c01d | -7.39719 | -47.37555 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5636ac9-2d57-342c-9e81-6415d032b697 | -7.5406 | -44.67127 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3d6ae8a-b514-3d23-8066-3bd49730645f | -11.48263 | -43.62949 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d9b31fd0-bb6c-3f61-82e7-6127ee6ffe18 | -7.49502 | -48.25566 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7d1ee1b-748c-37c2-a16f-d1c1eeba794e | -9.70032 | -46.8723 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3cb752b8-c816-3d90-9dbb-5c898c279175 | -6.20531 | -43.49659 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7799cb0-4bdf-3cf7-bfe0-d619340da2c6 | -9.59748 | -48.06186 | 2025-09-11 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44440639-be4f-3110-ad9d-482206a7e52f | -6.38674 | -44.42964 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc66f841-ecac-39b0-922f-388dbe633e7d | -6.31432 | -43.44426 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aab1c447-1701-3791-ade7-383686259db5 | -7.50298 | -48.24259 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21e97062-14de-3972-966a-37820581f715 | -6.38128 | -44.42918 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f946b6b-d86b-3e94-979a-b5b41ff60e21 | -9.07172 | -47.08318 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 50c68664-b581-313f-b98d-b4eeca7dd4c2 | -6.25438 | -43.40926 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce82cce8-2edd-38c0-81d3-ad8a302a893c | -9.53085 | -48.30583 | 2025-09-11 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
