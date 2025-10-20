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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5b65e62-4a1f-3eb3-bd3d-4dbe2e7f241f | -11.60524 | -48.54174 | 2025-10-20 00:33:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b351185a-61f2-3e38-8807-8ebd17223bd7 | -10.66664 | -47.63454 | 2025-10-20 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 67c2e01f-8a7a-3ead-a024-eec96b95ea53 | -15.56442 | -41.63301 | 2025-10-20 00:33:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.5 |
| f8ff0923-6a28-3c16-9276-d20a39226516 | -4.33857 | -43.61073 | 2025-10-20 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3dcd2261-bb4f-32d3-aa03-a94dd1ff6462 | -6.8506 | -46.29482 | 2025-10-20 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1d5befd6-17d5-3da4-9c6f-b74e60d93882 | -2.91009 | -52.72075 | 2025-10-20 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 30597986-4cd2-30ef-84ef-452eb226e6bc | -9.46498 | -47.35701 | 2025-10-20 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db474889-cb96-331b-a0a5-e71e7e53e570 | -3.10222 | -51.28696 | 2025-10-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e216450d-356b-37a8-8d49-314524df2fd6 | -2.26854 | -51.9266 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 06c2723b-2893-35bc-a36c-c0f7e041a8f1 | -3.48321 | -46.00876 | 2025-10-20 00:35:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ef826223-b58c-324f-bb00-17438052780d | -7.71266 | -47.86535 | 2025-10-20 00:35:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5eb29472-8aac-3321-ada2-40952edd98c8 | -2.91948 | -52.71936 | 2025-10-20 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 13e36778-6796-3621-8f17-68c07ae0b7b4 | -2.25826 | -51.91866 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 41dcf2d7-53e0-361c-bd2d-95de8d39fb86 | -2.43391 | -48.60935 | 2025-10-20 00:35:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6a6cb43b-ed52-3f74-83de-8eae1d1c86bb | -8.33577 | -46.22981 | 2025-10-20 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 79d50f56-7447-3f52-a29b-bc681d4ccc0c | -3.20093 | -53.07835 | 2025-10-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6d39a49a-0cc3-3f89-b401-f297d8cab303 | 0.06742 | -51.15474 | 2025-10-20 00:35:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a1b0a09f-d3fd-3572-9995-a47daf3deacc | -2.69734 | -49.56317 | 2025-10-20 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 219e9a5e-97d7-3e80-a3cc-90655962175e | -9.09572 | -46.8921 | 2025-10-20 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 34e573ec-0288-33e7-91d6-e998531ac385 | -1.44306 | -48.89199 | 2025-10-20 00:35:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f656be0c-cb3a-3601-9b27-b081db57053d | -6.86064 | -46.2933 | 2025-10-20 00:35:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a77acfb-328e-3049-b9b0-e8f4e9d26754 | -3.7446 | -55.56379 | 2025-10-20 00:35:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1969c825-6a33-3e10-ba75-2810daf0f371 | -3.14375 | -49.52475 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85b634b0-3c03-3f34-a721-3c059062a1ef | -8.23662 | -46.25119 | 2025-10-20 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5219fd8f-309b-3cfa-b43e-10846df075da | -3.85255 | -49.91585 | 2025-10-20 00:35:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9d780f03-8a5f-3299-9c53-f52c8a55d566 | -3.26203 | -50.05094 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bddc84cd-712b-3310-82e5-90da24cc06b2 | -6.17182 | -47.85126 | 2025-10-20 00:35:00 | TERRA_M-M | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1172f588-6ad5-3f76-bfaf-5158bbd6fd81 | -8.47554 | -45.85293 | 2025-10-20 00:35:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 86299251-4e62-302d-8bec-81fa7c40de86 | -2.27756 | -51.92533 | 2025-10-20 00:35:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6279f540-100d-316c-9546-d20659cb61b5 | -2.24799 | -51.9107 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.7 |
| d1153ad8-a3ac-3f24-9aa1-e26943e2cb2f | -2.257 | -51.90944 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 71888cef-a488-34d5-9b45-82493915c05b | -2.50642 | -49.05534 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51a622e4-5144-312c-a3ee-f709fd3f4d6b | -5.61749 | -43.65286 | 2025-10-20 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9a6e33ab-ae5b-391a-b07a-3843ca518fad | -6.38304 | -45.7638 | 2025-10-20 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| fe01a966-f9c0-3db2-abbb-02770dbaddd0 | -2.87547 | -50.71723 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 2398d1b5-0eb9-3d38-a904-995d88bf917c | -2.86786 | -50.72725 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 911ea88d-4129-3bec-b90d-eec68aa4aa4b | -7.07141 | -46.19594 | 2025-10-20 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2184ff5a-dac9-39d1-bd63-f6aa376264e5 | -9.46359 | -47.34741 | 2025-10-20 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb455fba-7d65-3033-bf4b-2ed905820ffc | -8.33415 | -46.21869 | 2025-10-20 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 4e087876-fd2a-383d-8f41-48f971613868 | -5.9128 | -45.39989 | 2025-10-20 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ef2684bb-2182-3a8c-97d4-d87ac772c0b7 | -4.59172 | -46.52697 | 2025-10-20 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1c3cd312-db8f-343f-bb1d-b71a38acda74 | -7.13311 | -44.25724 | 2025-10-20 00:35:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7ce51117-9500-3025-91fd-d0e38a04a569 | -3.24072 | -50.027 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c1c635db-02ee-36eb-90e3-4c84998bd417 | -2.5051 | -49.04599 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 9c4413a2-6c40-328b-9094-0b88d68b2c73 | -8.79137 | -44.55272 | 2025-10-20 00:35:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 618e4cf1-d3d0-3e8a-a25f-d61cf9a7ad5c | -3.15266 | -49.52349 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8acccc72-b926-31f6-9d8b-7fe2589dcf33 | -6.35919 | -46.15537 | 2025-10-20 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2589307e-ea14-3177-a1d3-2769f6453aef | -8.3441 | -46.21766 | 2025-10-20 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f5fdc7ea-b6cb-3763-918b-b9782e1c5c2d | -3.61537 | -51.47044 | 2025-10-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 179df094-075a-35e1-8eb8-a6cec63818a4 | -2.86147 | -50.74606 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fbcb3603-e4e7-3670-9f0b-225ab1608fcf | -6.36941 | -46.15381 | 2025-10-20 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 38766a54-3481-3b03-bb45-a991ab1ffa3f | -3.74896 | -55.56885 | 2025-10-20 00:35:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 30b70798-02a1-3873-bd88-0f968551b7c0 | -2.97295 | -49.22864 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e16ba65c-5ae4-372a-8470-6c5751cbfda6 | -3.47836 | -53.45658 | 2025-10-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f8547c75-e2e5-3cf5-b36e-424e5809c0de | -8.42721 | -44.13382 | 2025-10-20 00:35:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 59c774dd-8a26-3ad2-9b3e-d1b026236d38 | -3.33312 | -50.22275 | 2025-10-20 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 5c49ea39-aae8-35e7-9b4e-489eaada1b5f | -5.10397 | -43.20489 | 2025-10-20 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 72cb23be-3f34-38d2-8916-bd203fe70e13 | -6.10377 | -44.02485 | 2025-10-20 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 676e7d6f-d131-3195-9599-4f851f8c85f2 | -3.62434 | -51.46918 | 2025-10-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e9ca9711-93d6-3011-801a-58230ad46123 | -6.48456 | -47.01658 | 2025-10-20 00:35:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f34f0d30-5c2c-383e-abc5-5aac6d1ea68c | -3.39088 | -52.45087 | 2025-10-20 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| c120ab6b-5854-30c5-b7ef-774e219cf803 | -5.8688 | -48.18465 | 2025-10-20 00:35:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb906c30-594c-360e-bede-bdfe38b14142 | -8.43215 | -44.16555 | 2025-10-20 00:35:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8ca100c0-3ef9-3d90-a443-541e615ed0a8 | -2.24924 | -51.9199 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 29dc333e-0f92-3eed-9573-6269c1266cfb | -9.62318 | -49.12723 | 2025-10-20 00:35:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f5da45c6-9463-361c-a4a1-86c561e07e0c | -4.49528 | -44.13276 | 2025-10-20 00:35:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5c23a6d6-73b0-39b6-a50d-afc079b79f42 | -3.33039 | -50.73976 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7faf107d-0821-38e4-bb49-4d0031a3b080 | -3.10895 | -51.20406 | 2025-10-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3653dae1-faa2-395e-9adf-dd514fa3a4c9 | -8.42478 | -44.11818 | 2025-10-20 00:35:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 30323695-3e85-3104-995c-accf88f9edb1 | -2.73856 | -49.39477 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cba08b08-c0db-39d7-8bd1-3329fc469a29 | -5.08438 | -42.74784 | 2025-10-20 00:35:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 5404c7ef-ce04-37af-a2e9-66a9e8611b8a | -2.86026 | -50.73727 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 4bdce835-2d91-3849-9479-385a05f7cda5 | -3.33346 | -53.22887 | 2025-10-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| a49059f3-8677-3340-ae77-50ca39a75645 | -7.13511 | -44.24589 | 2025-10-20 00:35:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 27.2 |
| f9e62268-b7df-3c06-afd9-3ccaa579dc36 | -3.13185 | -53.00214 | 2025-10-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc57e5b9-6b0b-3a03-bfaf-c77a4c543d47 | -6.88391 | -43.60107 | 2025-10-20 00:35:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3ccafc05-6ded-3a37-9737-09fed821fdc0 | -2.43529 | -48.61908 | 2025-10-20 00:35:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 07019ae1-2445-3393-8a35-8cf31999efd1 | -5.91483 | -45.41386 | 2025-10-20 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 351a9e27-63b2-3c36-8726-c85feb977a40 | -3.23211 | -52.91875 | 2025-10-20 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 82cc949f-b57d-31a1-9799-504b48052ce2 | -3.1579 | -51.3616 | 2025-10-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3912a5e6-8d4d-33ab-b3a6-b2677e1a39f3 | -3.09455 | -51.29719 | 2025-10-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 40bd5945-55ff-3b25-9bba-94df5d5cbf7c | -7.07311 | -46.20738 | 2025-10-20 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 47128542-1894-396e-8d0b-095a7895de3f | -5.30183 | -44.4463 | 2025-10-20 00:35:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a8d48997-b58f-3f41-bf5a-43f8f412a75d | -3.38953 | -52.44102 | 2025-10-20 00:35:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3d501a59-1be3-39b8-90e5-e4d91021b278 | -3.26647 | -49.48267 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34d9a4c6-6052-3e42-b87a-2a69abf35382 | -3.26081 | -50.04213 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24b2ae0f-f446-36db-8583-5da64e301a97 | -2.25575 | -51.90025 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e3ceff88-e71c-3eb1-b398-d076ea0b04ac | -2.73729 | -49.3857 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3dabeddf-d8de-3a74-9f95-41604c3a5cbd | -3.33433 | -50.23153 | 2025-10-20 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ddd49efd-6cef-3352-af2c-c7048cb3acf3 | -8.73818 | -48.85658 | 2025-10-20 00:35:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d18d3a63-5985-3b45-8ffe-f8a23d9ca79b | -3.65045 | -50.25846 | 2025-10-20 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ada5e555-c02e-3f1e-844f-2ceb63430c99 | -2.68591 | -49.54645 | 2025-10-20 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 387cfa4c-3b36-3afa-99bc-8b900b921571 | -3.3316 | -50.74857 | 2025-10-20 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 07d5727e-441a-3540-94f1-75e8eb29a3e2 | -6.88105 | -43.58252 | 2025-10-20 00:35:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 44d65b97-4fc5-30b0-9304-14551861e546 | -3.1425 | -49.51577 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9ee18e95-213c-30bd-a721-62cd9539ff4c | -2.81695 | -54.37935 | 2025-10-20 00:35:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e9746d8f-34db-36b5-887e-ff8c4182199a | -2.90873 | -52.71067 | 2025-10-20 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ed8d8f0b-df91-3b2c-aa86-8eaa83416e58 | -3.15666 | -51.3526 | 2025-10-20 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1c83118b-0cf4-3b9c-983a-3d2614716bb0 | -3.42404 | -49.48486 | 2025-10-20 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| ffd16812-68cf-394f-ade4-fa586794342e | -6.39163 | -45.74916 | 2025-10-20 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README3.md)
