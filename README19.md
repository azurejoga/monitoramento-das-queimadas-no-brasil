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
| 5fc38ce0-44ae-3f2d-81c2-f67aa2c172da | -9.30944 | -44.72335 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75449ae1-a708-30f8-93a2-4e70c9f8ee94 | -9.46575 | -57.83891 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 13dd05ab-6996-3ab3-9fd1-e9827ac3d3f1 | -10.81373 | -48.59181 | 2025-06-20 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0b37326-07e0-3edd-8c4f-fd0ec5fc7c4d | -10.83317 | -54.01081 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f48eb874-f710-3feb-bd3a-d0e749705c60 | -9.98604 | -48.54169 | 2025-06-20 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6791b551-6487-36cb-a448-2276d26dbcfe | -9.30373 | -44.82867 | 2025-06-20 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a7add9e-2c71-3e5b-b07e-fa22bab23e3d | -9.97379 | -48.60116 | 2025-06-20 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3b379f9-d314-38ac-a208-abf65acb8045 | -11.4687 | -47.29779 | 2025-06-20 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07da462c-a548-38cf-b4d9-507fc48c7800 | -9.30521 | -47.79424 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85e6791e-7c01-32bf-96ca-4ecfecec47dd | -9.46024 | -57.84805 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b44781dd-4613-305a-8d8f-f2404c76224c | -11.57486 | -47.87267 | 2025-06-20 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7970d43-3599-310d-9341-e1bed527bec0 | -9.33111 | -47.83525 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 730383a1-571e-377c-b8aa-9b6367baa0c3 | -8.26636 | -44.95275 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0325765-53d5-346f-bbdd-a652719029bd | -7.153 | -44.0629 | 2025-06-20 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 284e8faa-ad75-3b05-86c6-3f219a3ffe88 | -10.43552 | -46.7184 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35cb0dbe-6c5b-3474-9eb1-7cef7911ee5f | -9.98555 | -48.54526 | 2025-06-20 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59e2aa2f-3ad2-3792-8017-74c811fbcbcf | -4.37812 | -48.07596 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a9b2105-70b5-3d3d-bb7c-67d86ad82d97 | -10.47676 | -47.03598 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 2dd643e5-4797-3297-b510-6d1169cf2eb5 | -9.31355 | -44.83316 | 2025-06-20 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b06b0ae-f9cb-3fbc-9677-47e2a25a9513 | -7.38862 | -45.40161 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5fdc91ec-b0ee-3680-95df-8eb80a142ee3 | -10.52336 | -47.57953 | 2025-06-20 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de71bb90-6645-3478-b056-3ea3659f78b8 | -6.16094 | -47.26741 | 2025-06-20 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 286d8af6-6096-307a-8e5d-18701019d4a3 | -7.38822 | -44.56975 | 2025-06-20 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbeb8ea2-b4dd-320f-891c-c4dc3852a00d | -7.72245 | -55.13538 | 2025-06-20 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ac57b39-8617-3138-adc8-38112127ea1d | -3.73157 | -53.76662 | 2025-06-20 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ec9a810-6236-3d8f-86ca-4543fdbcc909 | -10.24517 | -47.45705 | 2025-06-20 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3afa5427-b323-320b-b849-e03080eb40e8 | -9.87611 | -49.33258 | 2025-06-20 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61768e64-5998-3325-b913-bcbbe1a9b73f | -11.80356 | -48.09088 | 2025-06-20 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b8b3a4c2-61b5-3059-8e25-6ec164d09ec2 | -9.49432 | -49.1358 | 2025-06-20 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 203fc06f-e17b-3b7e-be23-a687c4cf5df4 | -9.48196 | -56.0805 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c4396e2d-3638-35a5-ba5b-e30df3e263ad | -9.49609 | -56.08691 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b978db1-6d8e-3de5-a4d9-39ff5f1b235f | -7.15376 | -44.06282 | 2025-06-20 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6109303b-6740-3b5d-a2a3-33ade5e576e5 | -10.92914 | -49.27478 | 2025-06-20 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ee84786-2659-35c5-a46b-b44f41a36a4a | -9.31866 | -44.8339 | 2025-06-20 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d71b7c2-83f7-3e1b-8d69-aac6f595fa42 | -9.84388 | -44.7063 | 2025-06-20 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9682318-e937-3ed5-9961-bc3f6bc2a67b | -4.77739 | -47.25366 | 2025-06-20 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 614afd85-e574-3f22-9686-66b860d18dc4 | -8.26056 | -44.95807 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bd8d0b4-c3fb-3eee-9822-db3e3bf27988 | -7.75473 | -47.61059 | 2025-06-20 04:51:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2aaffd41-76ae-3eb7-a1bc-b4e638c405ab | -7.27105 | -45.36756 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0df14fd-4425-3969-ad68-23bbe0fb1ef5 | -10.49203 | -47.02418 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 88165ab3-c6bf-3531-9310-478f7f584d02 | -11.95631 | -46.92657 | 2025-06-20 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93acbc3a-3d66-38f9-91f6-57029d2927fe | -10.1665 | -51.65349 | 2025-06-20 04:51:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e39179e-4788-34d9-9d28-bb409c9355db | -7.22205 | -43.07913 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 0aab3dcd-521a-3127-b124-c990048955ec | -10.54533 | -46.9888 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3b881d1-148f-32d0-b568-5e20f72189a8 | -11.3217 | -45.2045 | 2025-06-20 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db82918f-f44b-3265-9486-16733c86f9ef | -12.21482 | -45.52998 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb52f2fa-3faa-339e-9035-98911d8a907b | -9.30386 | -44.72585 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b68b2698-540d-3639-9620-cc0b91558429 | -9.84429 | -44.70308 | 2025-06-20 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8752196a-ca34-3ff2-b43d-b3f9641726e5 | -7.23918 | -44.68526 | 2025-06-20 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d23d2a7-67fd-398f-9ba1-df68fdd4d3df | -9.33216 | -47.82753 | 2025-06-20 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5e9867f1-b306-3e55-a103-7e11f02891bd | -10.86542 | -53.76204 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a015102-c998-3dc7-9594-ee47a08bc3eb | -10.48631 | -47.03266 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a20e883d-d5e3-399a-a694-98e4401302d2 | -9.4619 | -57.83825 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f6175800-8918-3f11-8841-2e53e55e1de5 | -7.21799 | -43.06698 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 174b60e5-03eb-38a6-96f2-277159fb2457 | -9.30884 | -44.8294 | 2025-06-20 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea633942-d665-3937-ae9d-6204a84d76f6 | -5.48526 | -42.14289 | 2025-06-20 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 099ef012-1562-3478-b02e-f1962fec38c1 | -9.84348 | -44.70952 | 2025-06-20 04:51:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0328e1a5-e920-3864-8fc8-5e48d8a4bee3 | -11.14533 | -46.65805 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e124e391-ab1b-3f76-b399-53f1563cad1e | -8.12559 | -43.12547 | 2025-06-20 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 81cf47fb-5dfb-3bbc-9f18-23d696aef48c | -11.1565 | -46.64482 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a1bb3f26-1df1-326a-8361-570bc980134c | -7.22305 | -43.07164 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 11448657-f3bc-3977-9a00-32b059e5f0a7 | -9.10335 | -50.03138 | 2025-06-20 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e51a1dc9-d211-3160-a38d-683caa54b327 | -3.73044 | -53.77385 | 2025-06-20 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b341a04-e78d-332a-bbd1-b8fc2db6e99c | -10.46603 | -47.04805 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 8249273a-9195-3b75-8e72-dc4b07641596 | -9.31164 | -44.72586 | 2025-06-20 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1bd7656-5886-3b51-a930-3dc39916f739 | -11.13015 | -46.66609 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9db6e613-0c4d-39f0-b8a4-1b2a3f62d554 | -10.52766 | -47.58019 | 2025-06-20 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6be51052-0e76-3342-9351-0070d7c34f57 | -10.85718 | -53.77145 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e8b68da-557b-34d7-8e4f-2003a848ddf0 | -7.38716 | -45.41182 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5da815c2-b29c-3383-8744-a8cb8c145ad2 | -7.27252 | -45.35717 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6ed6599-326f-3c7b-b3b6-c989d7beb038 | -11.15445 | -46.62447 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b3f730c-4c8b-37ec-bdf6-0d979225ef98 | -8.16811 | -43.15134 | 2025-06-20 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5b7a9da1-4de2-3902-b904-ce9ded880c71 | -10.83648 | -54.01134 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 893b3120-587c-3dc6-8e0b-8f48ec8a610f | -10.49713 | -47.0202 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 091cad6e-59c8-3e51-99b5-cb5462f2920c | -12.21404 | -45.53605 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c760870c-c6d6-3f71-a63a-e98a5895a41e | -12.21443 | -45.53301 | 2025-06-20 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4651419a-a61f-386a-a4b1-db9cd5828480 | -10.76969 | -52.75454 | 2025-06-20 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f58541f2-2d6d-3fba-97b8-b1878ce3fe52 | -9.48688 | -56.07724 | 2025-06-20 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 95d31810-7829-3ce2-8d7a-c0ddb6faacd0 | -7.27179 | -45.36234 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ab88ab8-e8e7-3e38-bc2c-9011e69179e5 | -11.14008 | -46.66219 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f973935-59a3-3696-b759-829e43819610 | -11.58223 | -47.87189 | 2025-06-20 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39b60e25-598c-3743-a532-6c368ffa4218 | -6.60275 | -55.30111 | 2025-06-20 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c3268cc-4e6c-3944-b4c6-5613dcf2c773 | -4.48274 | -48.86633 | 2025-06-20 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7180f89-1320-35c1-bab0-ef5a3af51d75 | -8.37338 | -48.42293 | 2025-06-20 04:51:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a60ec0e2-dfa5-3dfb-8fbb-3d0fd507f4ac | -9.45418 | -57.83703 | 2025-06-20 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 367c4b8f-ffad-3544-a5da-008adffbfcc3 | -10.49265 | -47.01965 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 30d142c5-8cf8-38a4-bdc2-8dbbe0ab4a34 | -10.59432 | -46.93074 | 2025-06-20 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86ec0c4d-6c54-3f49-a472-54a685c68e8e | -10.5228 | -47.58358 | 2025-06-20 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2501b97e-386d-3f46-a42d-b088ddd8aa64 | -11.57794 | -47.87133 | 2025-06-20 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d5f0327-86b8-3a18-b7c2-16cd1a0d25b8 | -10.35271 | -52.52503 | 2025-06-20 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a5bdb7d-59c6-3ca4-ae35-0720ee7fb8de | -10.59691 | -49.46181 | 2025-06-20 04:51:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b53149a8-e27e-327b-bf00-a1fdf398713e | -11.5774 | -47.87544 | 2025-06-20 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13c0afcd-2a4f-3f65-9787-705064d4f532 | -7.26773 | -45.35653 | 2025-06-20 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb414b7e-8487-3cc0-89dd-2586327c79d8 | -8.26515 | -44.96172 | 2025-06-20 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 803c9032-ddbd-3ab4-a031-4350448a7fad | -8.1856 | -46.48914 | 2025-06-20 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ff24501-1162-3d03-b799-3498c21b04b1 | -10.85112 | -53.76691 | 2025-06-20 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e88eda90-38df-3a8a-b145-e4c3cfc3f1d7 | -7.312 | -55.30913 | 2025-06-20 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55e5b2b6-ad52-302a-82ca-0cc5620aa505 | -9.13123 | -47.5886 | 2025-06-20 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b9b7150-964b-327e-a6f1-478e1731c4a1 | -7.87944 | -47.15471 | 2025-06-20 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a46f7fae-fa09-3b50-ae2f-da101a4831dc | -7.13897 | -43.28068 | 2025-06-20 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
