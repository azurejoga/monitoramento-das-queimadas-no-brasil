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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca5864d6-bcf0-3382-835f-a51f7be61109 | -10.64059 | -48.08438 | 2025-05-27 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47efb9df-69da-3c61-997a-2963eb575f79 | -8.75604 | -49.75208 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 61079097-a0d2-3f52-86b2-67ea55c9a3d3 | -11.56284 | -47.44328 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc61a39f-7773-3cd7-a0d9-09d1a91622b7 | -8.43299 | -46.6518 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 111d620e-3a87-3edc-835a-0ceb214e8b10 | -6.64297 | -43.20728 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 429f83f9-c4ba-3622-8460-aff421c60df5 | -6.63008 | -43.21815 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 75f591e8-2bd6-3554-a12a-fef0bbf2cf03 | -11.14328 | -53.9209 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31a0678e-15ec-3648-b179-94c482dbdb4b | -10.83018 | -54.02724 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c35f6ade-06f9-3d68-9c7b-2089c52d5330 | -10.89156 | -44.67599 | 2025-05-27 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b52f245c-4f22-3853-b64b-2b589fa3c4e3 | -11.56989 | -47.44588 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ab0a4a44-ad37-37a6-88f2-eab788dd4066 | -8.43158 | -46.66013 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e0a69f8e-f2b6-3b01-b4e2-0a08f0d415f8 | -8.434 | -46.65507 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b725e918-a133-38aa-a83f-19a0c2c41731 | -8.74907 | -49.75155 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bbe549ef-a4db-3471-b99d-eaf3e996d2bb | -7.21356 | -43.11771 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| ae52176b-bfec-36b5-a929-7682231f9ed5 | -9.03334 | -47.74498 | 2025-05-27 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 389a59f0-bfe3-312b-b4f5-dad702bfcdba | -12.27669 | -44.60127 | 2025-05-27 04:02:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b911715-3606-3406-ac7f-c44db9c5bb39 | -8.75012 | -49.75447 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| edbd2f00-ba4f-3e2d-a815-f3d1e364df56 | -7.73779 | -37.59486 | 2025-05-27 04:02:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a76e32f2-7679-3f2e-9b9c-9555f91fd817 | -7.47828 | -43.3601 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d9276e2-8675-31d4-a7f7-1ca0f1daddf0 | -7.19574 | -43.11486 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b550145f-63d0-34e0-9270-ca93ac9a3b9a | -7.60137 | -43.40888 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb940558-9e92-34f6-b2a8-296f24e932ac | -11.87222 | -52.25705 | 2025-05-27 04:02:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e628a63d-978c-3093-a9c7-49002523b154 | -7.16599 | -43.31711 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 17be092d-3613-3ff3-9036-ed205846ca4f | -11.13546 | -53.92557 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b98a82ae-8d22-39f9-8e04-efe1a8f6a83e | -6.49793 | -47.48737 | 2025-05-27 04:02:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30a8fd3f-3919-3351-ae35-5c43d152027f | -8.42866 | -46.65104 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2aff5326-d7fa-3e7f-9c64-2667bba2ff52 | -11.05405 | -48.8563 | 2025-05-27 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3699bc2-a647-3396-a48c-b75230adf9c2 | -8.74969 | -49.74821 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 27f6d490-b6e9-3b4a-9102-d3365a8efa8c | -6.23191 | -43.35322 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e42a255-fa8d-346e-aebd-dc6665d780e5 | -12.83397 | -47.38296 | 2025-05-27 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee484144-24c6-30c9-93f0-3f8e1fb35313 | -7.20287 | -43.11601 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ea84e467-1fdb-3ab1-829f-189011ebf5c1 | -7.54737 | -43.18592 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da94d734-4d55-3855-9511-4083e7c0a4c8 | -6.31926 | -43.37061 | 2025-05-27 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0acbfc8-a2ec-307b-811a-f860372578d4 | -6.63439 | -43.21446 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fee1ec30-0b39-3363-bfc1-72ee95ab8517 | -6.638 | -43.21502 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 43cc664e-125b-357a-bb7f-d98540bc1bbc | -10.83683 | -54.02863 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 246c61c8-1897-37ae-91c6-dd7fc370e3fe | -11.40089 | -52.95354 | 2025-05-27 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f97ed018-15b2-3c46-a446-b5d042b65239 | -10.53017 | -47.58828 | 2025-05-27 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95dfb1fa-041a-35c5-9084-f1e70ad06c26 | -9.49831 | -40.35195 | 2025-05-27 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| cd026c10-aae3-3dad-b7e6-9f443a48b379 | -9.60215 | -49.02656 | 2025-05-27 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d21a967f-c57d-311c-9c86-a941bdde47d5 | -11.56483 | -47.44924 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c1ea05eb-1061-32f5-a7b7-e49f5354489d | -7.20454 | -45.35121 | 2025-05-27 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 985e3e63-5408-38f7-a51d-d6c7d9a073d9 | -7.20333 | -47.28103 | 2025-05-27 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e929f17-b21e-31c2-9444-5d8443d7ac0b | -11.40267 | -52.95405 | 2025-05-27 04:02:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2069577a-b132-389d-9909-2a10e5557926 | -7.22202 | -43.11071 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c8d89e22-b231-3a2d-874e-b81b8527acb2 | -7.2071 | -43.11252 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 382661b2-0d77-320b-a95a-28ea26495350 | -6.63869 | -43.21083 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d3506c8f-0630-36d7-923b-3f235f1c6ff8 | -7.41055 | -49.37749 | 2025-05-27 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e694fa72-7547-398c-b606-c90a43d5d43d | -7.60635 | -43.31187 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d55720f-5fb7-3262-b5fe-35666e3e47da | -10.83553 | -54.03492 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd649cd-1cdd-3c00-852e-9dc66f20736a | -10.74335 | -49.28419 | 2025-05-27 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8eae577-8f24-3e4e-8f95-267af8b70013 | -11.58375 | -45.02457 | 2025-05-27 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4700f3e7-788a-3f18-b4ed-e0d89fa7899c | -12.03365 | -51.59445 | 2025-05-27 04:02:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12593aae-73aa-39db-ad2c-419982e320d8 | -6.83775 | -42.79533 | 2025-05-27 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b8e71cc-6223-3266-8ee2-dc27b2395a79 | -12.0262 | -43.03365 | 2025-05-27 04:02:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 265afed6-5c7c-39d5-9971-836563284549 | -7.60188 | -43.38342 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8007059e-d610-35af-a16c-cdda9648cb7b | -12.35044 | -49.92501 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef62eba2-50b5-3548-bb29-6d221b4a3d2a | -6.86593 | -47.83701 | 2025-05-27 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69bcc814-9f5f-3fa3-8adc-13e5b3bc3e0c | -7.6012 | -43.38754 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e68f6362-144b-3530-9cf1-c1ae57fa5465 | -7.47399 | -43.36371 | 2025-05-27 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddc15fe7-ca08-3e73-a3c0-741ef2fd0f27 | -12.35157 | -49.91909 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 605055d9-8acb-3ec3-97ec-4b94ca8b9520 | -12.07268 | -47.35222 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32b498fa-1e1c-3140-ab1e-828fcabbda1c | -8.01908 | -43.18834 | 2025-05-27 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 59bca58b-1838-3d87-b39e-19e745cb70b4 | -7.2327 | -43.1124 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 661be601-c372-3ee2-88cb-dd0694c9725c | -6.64228 | -43.21144 | 2025-05-27 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a535047f-4cec-3b26-a919-08d08a085bd2 | -11.76965 | -46.4142 | 2025-05-27 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a78323ff-9914-3758-a4a6-dec8324604a9 | -7.33875 | -43.37812 | 2025-05-27 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5a212dc-94b8-315b-aac4-4aed32d21c3e | -11.77369 | -46.41489 | 2025-05-27 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed65f439-3a1d-33c3-9657-7d516e32e743 | -7.40682 | -49.37435 | 2025-05-27 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16cef26b-af68-3629-92db-0223f516cae6 | -11.57582 | -47.92643 | 2025-05-27 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf3f957b-0852-35b5-8f90-57baf86e1f3c | -12.91444 | -48.0929 | 2025-05-27 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65c45900-6718-3f9a-a54b-eb226795f3e0 | -8.75164 | -48.05001 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fc15a31-f450-3c72-ab86-a004ed3bfbec | -7.35298 | -43.68427 | 2025-05-27 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74ea53be-0671-350a-aa2e-589ce10f7441 | -10.84604 | -54.01772 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b1d7eca-644b-3da5-abf6-1aa2bbad2ec7 | -6.65055 | -41.99804 | 2025-05-27 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| def0421e-d979-393f-9e8b-3b9ea58e8189 | -12.37045 | -49.98528 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34da7d3e-c194-3fff-a29a-b48eb3170c58 | -8.75544 | -49.75544 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fd78029c-d191-376a-bf98-7c1a692d226f | -7.66022 | -46.10639 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acb3cd74-0d9f-32fa-9580-a32cb8d51925 | -11.56208 | -47.44746 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48c73c83-2589-31b2-bd75-823e378099c3 | -12.07696 | -47.35297 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8349a1e4-d783-3907-b80a-b5d28fae129e | -8.01922 | -49.68951 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f464d390-a6e6-36ba-af1e-0ec354986170 | -10.83296 | -54.03035 | 2025-05-27 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 667c4fb5-7814-3703-b7d2-7d016a241833 | -9.39442 | -48.42765 | 2025-05-27 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c109d196-8c89-3e46-9805-ccd44730e022 | -9.15279 | -49.65073 | 2025-05-27 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47a9b82d-6daf-3c83-a321-24d494e60fce | -6.83423 | -42.79479 | 2025-05-27 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ed7af93-f843-3071-9364-c0d7818ce340 | -11.56124 | -47.44422 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d74936c4-e18d-3616-a837-418216205555 | -7.15646 | -47.14105 | 2025-05-27 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fd26973d-f828-3417-9f0d-dc399d069f28 | -8.75091 | -48.04792 | 2025-05-27 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1f8bd47-16b6-36fc-9dd2-a19a3a62d130 | -7.19931 | -43.11544 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 29234543-ddf6-3e51-87af-ed9c0f7a0db2 | -6.88186 | -46.35727 | 2025-05-27 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da9fdca0-a03a-3903-9b58-e950bbea08fc | -7.19998 | -43.11139 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 72fa6527-fd17-3aac-85fb-c1c946a8da61 | -8.4344 | -46.64349 | 2025-05-27 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ca2ceab-29db-3b2a-bfed-05b9cca6559b | -6.22895 | -43.3484 | 2025-05-27 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a91c136-14fc-3fa4-aa3d-91839013e505 | -11.86755 | -52.26058 | 2025-05-27 04:02:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85a2272c-2776-35e3-af74-36d82c18ec2a | -11.56557 | -47.44503 | 2025-05-27 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7ba0df2e-aed0-3095-93e4-e0b8f7154103 | -7.15607 | -47.14471 | 2025-05-27 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fde0466-3df2-3755-9573-4011bdbd18e7 | -7.20933 | -43.12121 | 2025-05-27 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| bdf7ef90-a794-329b-9a07-7ca93a27a694 | -7.97054 | -49.69684 | 2025-05-27 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59782d54-0cd1-3591-9f13-31442e3d8972 | -12.36987 | -49.98833 | 2025-05-27 04:02:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 568e8890-4a96-3497-9e8e-129de8fd808a | -7.40624 | -49.37766 | 2025-05-27 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README5.md)
