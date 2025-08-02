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
| 8f7fd716-e94c-3f9e-8101-ec06ff00361e | -28.74812 | -50.39619 | 2025-08-02 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d7d30d1a-df11-3922-bce1-d7c0976607f5 | -28.44855 | -49.57728 | 2025-08-02 04:53:00 | NOAA-21 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7868fda3-10e4-38f7-a6ba-dceccbc2babc | -28.91446 | -50.1692 | 2025-08-02 04:53:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2c90381-e423-3f31-b93e-9b3cdeb1427d | -27.59096 | -52.44129 | 2025-08-02 04:53:00 | NOAA-21 | BARÃO DE COTEGIPE | RIO GRANDE DO SUL | Brasil | 4301701 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dbe9fd69-732a-3ba3-addc-036197baab15 | -28.74725 | -50.40414 | 2025-08-02 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1bceba3a-3d38-33ff-b8d8-e1e201f72621 | -29.78081 | -53.84895 | 2025-08-02 04:53:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 7.9 |
| fb457ad6-978c-393c-9b75-3333f8bb0fa6 | -28.52052 | -50.55265 | 2025-08-02 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c47af265-2c92-3105-a417-43c12b1d8b1d | -28.91426 | -50.16615 | 2025-08-02 04:53:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4c6efb6-a988-3982-a7f9-29e39b0d63fd | -26.21986 | -52.70399 | 2025-08-02 04:53:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 19ff5516-57c6-3a42-b78b-141d1f2b93df | -28.91495 | -50.16473 | 2025-08-02 04:53:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fa7dbd77-3ffa-32b2-8997-0bde56429198 | -28.74768 | -50.40019 | 2025-08-02 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b2911ec-2688-3b0f-8e9e-00e119e46575 | -28.9029 | -50.85645 | 2025-08-02 04:53:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0685a672-1ea7-3787-89cc-954142b74446 | -29.77727 | -53.84833 | 2025-08-02 04:53:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 7.9 |
| d818a727-1294-3dbb-bde0-aadc52564302 | -28.79087 | -54.76256 | 2025-08-02 04:53:00 | NOAA-21 | BOSSOROCA | RIO GRANDE DO SUL | Brasil | 4302501 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 73a0777f-fc83-33a7-a17b-c729e74f9f62 | -8.0321 | -43.1257 | 2025-08-02 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 04bfe61f-af25-3850-a154-1fb98b4f3939 | -12.6789 | -44.4851 | 2025-08-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 07c21824-bd65-3444-bc6a-eab24e1cf050 | -12.6591 | -44.5117 | 2025-08-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e56875ca-42fb-3c4a-a493-ac7cfb351510 | -12.6784 | -44.5085 | 2025-08-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 3cac282f-143b-35a9-a553-f8743ed8fcd8 | -12.6595 | -44.4882 | 2025-08-02 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 23285df8-d5d8-3439-88bc-ce08e55a4d59 | -12.6784 | -44.5085 | 2025-08-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| ab10a241-623f-3f75-a7b2-4e979f77cff6 | -12.6591 | -44.5117 | 2025-08-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 41136da5-dbd7-3e3d-a86b-9620547789ee | -12.6789 | -44.4851 | 2025-08-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 06eb8937-e6da-37c1-a132-ad527d218241 | -21.151 | -48.0111 | 2025-08-02 05:10:00 | GOES-19 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 81976301-982d-35a5-9648-a81936342459 | -12.6595 | -44.4882 | 2025-08-02 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ceca5060-5089-343e-b645-7c583cf0b290 | -8.0321 | -43.1257 | 2025-08-02 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 04c85ca0-e175-3ae7-99b9-72276f57811a | -1.29143 | -55.74729 | 2025-08-02 05:10:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 760adb4b-d204-3418-bc4d-462a78f5d8c4 | -2.92442 | -48.67436 | 2025-08-02 05:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3aa4065-d61a-3e87-90f4-4acb5e947e35 | -2.9195 | -48.6737 | 2025-08-02 05:10:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55054b97-5983-3597-a4fb-1f177b134db1 | -2.90283 | -48.24747 | 2025-08-02 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06b18875-32ca-32f2-a7a3-b0566e5bd3cf | -2.80944 | -49.00924 | 2025-08-02 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 446ad52a-0743-3e5d-b818-d2f29b8ec595 | -2.90665 | -48.24869 | 2025-08-02 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 493d1448-b5e1-38d0-a027-7dca54c5985d | -2.90239 | -48.25035 | 2025-08-02 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4264c352-7cc1-3da1-beaf-33a6950811cd | -2.90573 | -48.2955 | 2025-08-02 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7e06557-4294-3e26-bdbd-579cfb60492c | -2.80908 | -49.20641 | 2025-08-02 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79e1cf52-c4a2-3f3a-a150-ea71dc993d27 | -2.90485 | -48.29609 | 2025-08-02 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfd5163b-78d2-389f-abfb-c211099a8185 | -2.90159 | -48.2479 | 2025-08-02 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee6c1b3d-65eb-3b99-bc5b-dd174ad9e871 | -3.51099 | -47.22221 | 2025-08-02 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b93fc13d-513f-3380-941e-b519d3c743f4 | -7.8776 | -45.53789 | 2025-08-02 05:12:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c472384-ac77-375c-830c-a2cac73c22cd | -7.87708 | -45.53795 | 2025-08-02 05:12:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a391b138-40db-3690-8fdf-c6e09eccba73 | -4.3168 | -48.10207 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1af7eaa4-2e42-3c27-a0bf-8d7e8d69a8e5 | -8.28934 | -46.35584 | 2025-08-02 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aef1f60c-c673-316e-863b-5a56ffdf1eb5 | -3.57999 | -47.51541 | 2025-08-02 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c5e3a20-db1d-3413-b47f-dc2342378a4c | -9.19796 | -45.28827 | 2025-08-02 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed6da192-b71a-3534-b0c1-950eee3f8a88 | -7.04012 | -44.41218 | 2025-08-02 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fb86bc2-7a42-37b5-9f31-7c9ab58dcfea | -7.69352 | -45.11456 | 2025-08-02 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dec2763-1d7c-37a6-b8d5-e33e15a821f3 | -9.05704 | -45.06173 | 2025-08-02 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd9cbe7b-62d5-36c7-abda-ba9aa88423e0 | -3.52919 | -52.87076 | 2025-08-02 05:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f119d2f-4dd5-3cc4-b4a7-f0cbfbbb51a3 | -7.75107 | -45.13927 | 2025-08-02 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93ed3aa8-906c-3b8d-950c-cf75fffa8e84 | -9.19718 | -45.29461 | 2025-08-02 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8331dfb4-a390-34ab-9429-604b9dccb988 | -8.29616 | -46.35201 | 2025-08-02 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c2c8db6-96e8-357c-a98b-201a707eb426 | -6.70445 | -44.09179 | 2025-08-02 05:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 816814e9-1257-3fb6-8fe1-d752509c77b1 | -9.08339 | -45.89354 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad417315-6095-30ac-a93e-b59d49c30444 | -9.06656 | -45.05952 | 2025-08-02 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ad1d7bc-da62-3fad-a866-2c07e85a9665 | -3.43205 | -48.95737 | 2025-08-02 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f232f71-bd6f-3bda-8171-f6bec31be391 | -8.57119 | -51.54616 | 2025-08-02 05:12:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fd23c40-a785-385a-b00a-c5c8d734e400 | -8.22884 | -49.93548 | 2025-08-02 05:12:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85783e80-26fb-31d3-8652-ba19ba10f5a4 | -9.05038 | -45.05999 | 2025-08-02 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b31ec496-e5a3-3934-95f2-b3924050ff72 | -3.5175 | -47.21595 | 2025-08-02 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2079ac9-2bcf-35c7-a79a-32cc90b8ead2 | -9.38843 | -45.50303 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54ea66a3-c46d-3c98-a345-7a8cba88f7ac | -2.4975 | -56.08112 | 2025-08-02 05:12:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72ce03f2-04b6-37d1-92fb-ff9ce5880f3b | -6.70358 | -44.09819 | 2025-08-02 05:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7dec9842-3fd9-3f73-990e-2f44f052f725 | -4.31158 | -48.10131 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8edb551-8a38-3c6c-a605-79b99ec1cef8 | -3.517 | -47.21939 | 2025-08-02 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f36b80b-7366-3ba0-a381-b73014993735 | -9.19119 | -45.28811 | 2025-08-02 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 941471cc-e4c2-3460-bf3a-aea5421ec8a0 | -7.69037 | -45.1114 | 2025-08-02 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fabe13d4-8863-36aa-8091-37a59f3fb3ae | -6.70336 | -44.3601 | 2025-08-02 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74b8ce8c-1cbf-3ddd-8120-66962fe1cffc | -3.43582 | -48.95375 | 2025-08-02 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80daa3c3-86e6-39b0-be24-88f411cccc04 | -9.05904 | -45.06492 | 2025-08-02 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 310463cf-44d4-3923-8cbd-f17991343382 | -8.23372 | -49.93618 | 2025-08-02 05:12:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64faeaae-064e-3729-a829-e8e6b910fead | -7.68964 | -45.11689 | 2025-08-02 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95647611-27f1-3d27-bc45-fe3a31a1ed0c | -7.60062 | -55.20061 | 2025-08-02 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c71c07a8-c741-3a3a-84f4-bf8faa2ade51 | -4.77447 | -45.33895 | 2025-08-02 05:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c21800b-e32b-3f8b-b14e-4edc2bc5b4c5 | -4.02867 | -48.06487 | 2025-08-02 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50f2f754-52c2-3070-b338-bfcb2ddb0e6c | -7.87778 | -45.53247 | 2025-08-02 05:12:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 817420ce-3327-328d-8a51-3e06ba59c145 | -7.35107 | -44.66052 | 2025-08-02 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18f299f7-0152-3018-bd48-b17732caf3ad | -4.31113 | -48.10445 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00f56c30-0382-33b8-8b25-00900fb6f759 | -7.68691 | -45.11348 | 2025-08-02 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d130bf9-a091-3766-a36f-416d308bd226 | -8.2942 | -46.35845 | 2025-08-02 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40c2bc89-20a8-3fc5-ac54-35596cc74dba | -6.70273 | -44.09815 | 2025-08-02 05:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4901ccf6-e3a3-32a7-8f61-b39d5a5f6c5b | -4.31725 | -48.09891 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad631755-9bce-37dd-9a5e-ed2d630e4e1b | -3.43505 | -48.95906 | 2025-08-02 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21a6951f-fd14-3e09-82c1-154adb6331e9 | -9.05232 | -45.06366 | 2025-08-02 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 450bf924-a775-3ddf-994b-558598e4bd3d | -9.19045 | -45.29409 | 2025-08-02 05:12:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc0561c3-522f-3409-9f64-80b6c6faf9b2 | -3.4369 | -48.95813 | 2025-08-02 05:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8ec67b1-8da4-3641-93a4-d0b1f872f9cb | -7.0332 | -44.4117 | 2025-08-02 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 971f2fde-c805-3af5-a690-801d232574c7 | -9.08288 | -45.89915 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19479cbc-914e-37ef-8be0-f5405a2bb8a4 | -7.87834 | -45.53239 | 2025-08-02 05:12:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df67fea5-b585-353c-aecb-89e0da0b784e | -8.29552 | -46.35678 | 2025-08-02 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2f82957-9cc6-3309-8315-68411ed82757 | -8.2948 | -46.35369 | 2025-08-02 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca6d44d0-65b0-3d88-9bc7-64b45b53a844 | -4.31731 | -48.099 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8c270b3-e6c4-3e8b-91b7-ca6682fae656 | -4.31162 | -48.1014 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4291dd76-5acd-3e13-b379-bafe6d6b2a04 | -4.31115 | -48.10453 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed35aed4-71ad-3931-95a3-76f369a52d10 | -9.08352 | -45.89397 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa4795a3-a671-30a9-bb1c-acf99edcd373 | -3.51151 | -47.21864 | 2025-08-02 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a005ae11-9587-3f12-b971-a0f17a974268 | -9.08272 | -45.89872 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ad97433-445f-3f75-929e-d442045c18ab | -6.70412 | -44.35439 | 2025-08-02 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d29790f-232d-3129-98d5-a09cfb49c58b | -3.48522 | -51.18927 | 2025-08-02 05:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63baafdf-1d2b-3036-874a-d2a8678883bc | -8.30619 | -55.10668 | 2025-08-02 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a243fce-2cad-386f-803b-048ded68b860 | -7.7518 | -45.13367 | 2025-08-02 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fbf6c11-54ce-3790-8d6f-65762fd0f8ff | -3.52986 | -52.86636 | 2025-08-02 05:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README21.md)
