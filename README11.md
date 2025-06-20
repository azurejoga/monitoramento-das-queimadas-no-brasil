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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e00960b-7d10-3916-ba33-dff6fef182b3 | -9.09829 | -50.03107 | 2025-06-20 04:00:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3073c772-baa8-3c7d-ba13-d0062459d03d | -8.87792 | -49.26086 | 2025-06-20 04:00:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ef197c1-bb24-3e1a-a959-7db4f2dd9956 | -9.33266 | -47.82758 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ba5963f-a3a7-3f95-a3c0-c7e6890df57e | -8.16652 | -43.15239 | 2025-06-20 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 37e40ab5-70a7-3ac9-ba9f-824af683681e | -10.42166 | -47.08524 | 2025-06-20 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1af762ee-5610-3839-bd0c-9183ff364904 | -4.64255 | -47.96869 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22a54eaf-f439-31e6-b7cb-0110bbe02bd0 | -7.26713 | -45.36917 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 404d4110-9988-39cf-8614-cf4da82801e3 | -7.38705 | -45.40051 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61d116ec-9964-37c9-a54a-e52bad8d356a | -7.21588 | -43.07255 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 13a8dbe1-1b4d-3798-97f1-4eb1e28bb4a3 | -6.14167 | -47.2598 | 2025-06-20 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ddece83-fb59-3547-9990-65b7f53aed61 | -7.26838 | -45.36191 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1efbc3c3-90d7-3c46-9691-c4fb9b80bfcd | -6.66796 | -44.25048 | 2025-06-20 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2f9c209d-ed4d-33c4-b776-59371e1783fe | -4.84831 | -43.18814 | 2025-06-20 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a0b8ab8-8149-36ac-92d7-61ca5996096c | -8.37004 | -48.42229 | 2025-06-20 04:00:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e827c479-7f5a-3627-a37d-21671e699c13 | -10.72218 | -45.15925 | 2025-06-20 04:00:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04ece310-c721-391d-a4c6-0e96ad02d571 | -9.30473 | -44.72647 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 188923ec-972b-3611-a2f3-453a3f9243c3 | -7.26964 | -45.35463 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b6941bf7-f92a-381d-a1df-a2461b3e432a | -7.23497 | -44.6894 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 789c2e54-19ed-3cd6-9ffb-eecbe7c11e3c | -9.29842 | -47.78817 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e940c10-8c97-3fb7-b439-ea0d2d96f7dc | -8.1843 | -46.48837 | 2025-06-20 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4ec26f6-cfb8-33ee-9abf-6bc55c024b6c | -7.21962 | -43.22008 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13f46034-0db5-3cde-84cb-461ec828228a | -4.852 | -43.18876 | 2025-06-20 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bbd6aae-50a9-37c1-b197-992a1d01f637 | -8.2557 | -44.96025 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c978f712-75d7-3ce6-942b-f5b8c22c3908 | -10.4224 | -47.08101 | 2025-06-20 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b2220e9-74c0-3ffa-b28c-536fdee874ae | -8.26742 | -44.9623 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae405192-6c84-3445-a3a0-4e406f494d6f | -5.78538 | -43.45998 | 2025-06-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbe7c646-331c-35e0-8324-f436a4d99704 | -9.3285 | -47.83485 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a5c8b19-35e2-3767-ae46-17777e8c22be | -7.24254 | -44.24419 | 2025-06-20 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b98d520-e6b7-35b4-8e5b-9895e565fe49 | -7.21362 | -43.0638 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6e764edb-7fc1-3b0d-84cc-3e1e18ee91b5 | -6.84326 | -42.79879 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 227c0127-fd3c-3043-955d-0e0ca9177c4c | -8.64655 | -47.15324 | 2025-06-20 04:00:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d73089-47db-38e6-ba6f-a5256f91fdf5 | -4.77702 | -47.2523 | 2025-06-20 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1999483f-6800-3062-96ff-2998dfcfc5e2 | -7.75348 | -47.61739 | 2025-06-20 04:00:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a524e06-9b3a-3987-ae52-9b4b694361ff | -7.22202 | -43.07267 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| ce024aed-26f2-31e7-ba5d-2d03e21a4535 | -4.8476 | -43.1925 | 2025-06-20 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14ff4eea-3c92-3116-af62-cf99f20b6aad | -7.26525 | -45.35741 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a629bb2-27f6-3810-a07a-83f8bafa792a | -4.64306 | -47.96562 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56d7c140-fe18-3c09-ae4f-c141f99f2a8a | -5.48918 | -42.14217 | 2025-06-20 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8dab8d49-41fd-3b84-94c0-fd3f11f03cbd | -8.91521 | -49.85221 | 2025-06-20 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eaa5043-886d-3a18-bef5-cb0414e1d03c | -6.95896 | -44.06084 | 2025-06-20 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 414a728a-7c48-33f6-8282-43819cdfac81 | -5.78095 | -43.46376 | 2025-06-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46ec0ed8-8ec9-3c2b-9e7b-5a7b6e7e6b19 | -7.0218 | -44.5931 | 2025-06-20 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9d6298e-896a-3fab-838d-e30eccb36b82 | -10.72135 | -45.16406 | 2025-06-20 04:00:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82b4622a-2176-3660-acf6-a1b5fdb5f649 | -9.37233 | -47.63802 | 2025-06-20 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 541ecf54-527e-3a5e-a274-a3ff84577255 | -9.84289 | -44.6897 | 2025-06-20 04:00:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51301890-5b95-3f70-94dc-91ef8c0c7857 | -5.4518 | -43.57704 | 2025-06-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d00774e-b834-3a37-bfad-2e73e15e537d | -6.67259 | -44.24627 | 2025-06-20 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c9267b63-9683-3d96-99fd-5b5cbd6e35e2 | -9.30852 | -44.72717 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33f96cc6-4532-3ab2-89c4-eb9f17e48451 | -9.31316 | -44.83273 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1b63011d-c00b-3181-929f-7a3f89b1f627 | -8.17007 | -43.15298 | 2025-06-20 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 691a0cd8-f6aa-3ead-a1d4-c32163acf255 | -4.37653 | -48.08046 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88d067c6-512d-3ccc-bdda-e8a240aca698 | -6.15968 | -47.26809 | 2025-06-20 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 69764fe5-3bb9-387e-86c3-4ebb40f7e312 | -5.44805 | -43.57643 | 2025-06-20 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c779e759-58e0-32a5-b528-a3a1c946dca7 | -7.13356 | -43.28397 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c18681b8-3746-3846-adc6-8e6caf996d8e | -7.22253 | -43.22481 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a67713a-140d-3ef2-bc72-710ed2fb5fea | -9.30552 | -44.72179 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64d78089-3d4d-3097-8cc2-13eb8b64e51b | -7.27218 | -45.36617 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc2296b8-f584-3405-b476-30ba927b1532 | -8.95438 | -47.97651 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eb55554-25b0-3d9f-9dc6-e0a12438978d | -4.77568 | -47.25433 | 2025-06-20 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a334e9c9-42d7-32c8-992a-39c738b48d51 | -7.3896 | -44.55564 | 2025-06-20 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3b189a9-52b5-3e3e-b25d-e0c933ba3430 | -9.33229 | -47.84063 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7409d426-c3bf-3092-9426-07e21c0f43b9 | -9.30094 | -44.7258 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 525cf5da-6653-328d-a5cb-ec189cc963d0 | -8.2632 | -46.39135 | 2025-06-20 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc958391-b728-3c0a-8152-d379d699dd00 | -4.84688 | -43.19688 | 2025-06-20 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1072b78a-a45e-3341-b7b4-8c93f1665f7f | -8.17925 | -46.49176 | 2025-06-20 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07d0ad02-5312-3039-8063-e20a12a5750f | -9.3072 | -44.82896 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc8a3c5f-7bca-3e85-807e-5dd888860956 | -6.86878 | -44.83392 | 2025-06-20 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee239696-4bbe-37b2-891c-3f1c54b4c2f8 | -7.21845 | -43.07209 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 3b912940-bbdd-3994-a769-51e5c2ea5c55 | -7.21556 | -43.06745 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 0860ad03-c63e-3b7b-ad61-319b9397bd4d | -7.21777 | -43.07617 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 12a7ee73-09ca-3b70-b454-eff9abacb320 | -8.95911 | -47.97731 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24c28255-de75-3943-9bfa-ec091de17f52 | -8.25653 | -44.95533 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fde676b-db4d-3a8b-a687-c8797ec02c63 | -9.33177 | -47.83244 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9d2e9f4-88a0-3ad9-800a-b8b60c6e0c85 | -9.31022 | -44.8344 | 2025-06-20 04:00:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24e7b872-c0ca-3ce5-aa3a-a65e8764f0a8 | -8.11493 | -46.08972 | 2025-06-20 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f9a0f47-ccee-3b9b-9b09-5a12d5942059 | -7.2037 | -43.20473 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65870d0d-60f5-34f4-87f9-5f5cce556f58 | -7.26992 | -45.35451 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f95f6eb-0850-324a-a27a-8a706967276e | -7.60269 | -45.55698 | 2025-06-20 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fed18d6-af76-392a-a85c-3457dd43d20b | -5.48221 | -42.14105 | 2025-06-20 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7f37d77c-4089-3f3a-90a1-fea85be15a85 | -9.33398 | -47.83097 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4939b2a7-175f-3e2a-a579-aa27b5a31c82 | -4.82212 | -44.35409 | 2025-06-20 04:00:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 239f5150-27b5-341c-852b-e6cc06e2eafe | -4.58792 | -47.89127 | 2025-06-20 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40857228-ca12-306e-91d1-7572a3868730 | -7.38642 | -45.40416 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70629821-e6a2-3959-be57-3eb332308c2c | -6.44885 | -44.79671 | 2025-06-20 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeb37f16-b94a-3c63-8caa-c51f56b0a80c | -8.26435 | -44.95669 | 2025-06-20 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b7bb072-97c9-36a7-b1a2-c3984b382186 | -8.17072 | -43.14896 | 2025-06-20 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a447c6d2-0f9c-39b3-ad30-1d70cdc4041f | -6.69911 | -43.21384 | 2025-06-20 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ef1acbcf-cd63-317a-88b2-73f28b8c4824 | -9.30676 | -47.79512 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cd76218-2617-3b02-9ca5-ab256d9b8461 | -7.38579 | -45.40785 | 2025-06-20 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9291a44f-1f95-3140-b826-463775236e90 | -5.60668 | -44.9169 | 2025-06-20 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9db65809-fe22-3eff-b2bc-482c4caf314a | -7.38878 | -44.56059 | 2025-06-20 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea54e986-78fd-3b8c-ac2c-de9f7499826d | -9.32715 | -47.83149 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74ebedec-b3f4-3acf-aa95-1426ba06d5fa | -9.29714 | -44.72514 | 2025-06-20 04:00:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6da84f04-c425-3ee8-9566-ccd5e495ebf7 | -7.38797 | -44.56556 | 2025-06-20 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5464ed3-d374-3d92-82bd-1dcc3e8fb1bf | -7.20011 | -43.20415 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b4e296ba-4fe8-3b56-a4d4-070eb48bc9e0 | -7.11591 | -43.14455 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4c841ecb-beab-35d8-bae0-6b5ef0842bc5 | -9.32934 | -47.83006 | 2025-06-20 04:00:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bf577d0-aadc-3c48-be75-6ebff188615a | -9.37245 | -47.63523 | 2025-06-20 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0340183-ae12-3f0e-9424-b056785ba4c2 | -5.60728 | -44.91334 | 2025-06-20 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 304a6a9a-71bb-3f55-8a19-1e1ebe37a696 | -7.21296 | -43.06789 | 2025-06-20 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |


[Clique aqui para ver as próximas entradas](README12.md)
