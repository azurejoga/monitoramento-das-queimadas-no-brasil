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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a901817-f9b2-38f8-ab09-034ef8e08fb6 | -7.27633 | -44.21495 | 2026-09-17 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f774d7df-2bfd-348a-8eea-83363c739373 | -7.15098 | -42.09673 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f68ab4c-0525-300a-9faf-03a1b2f56124 | -5.86079 | -52.06707 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e39b608-3dfa-3212-875b-fb01a6c18971 | -11.31664 | -47.0674 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aea9a87c-c76a-3441-943d-00caab499c1c | -9.04628 | -45.08804 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e47671ad-642b-30c9-89e2-ee9de1abb062 | -5.85629 | -52.06635 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2f5c1e4-a692-3f53-8317-e8b91ee1dcd1 | -6.93257 | -41.70244 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ba97f6d2-a82a-335d-b793-0dfa64c64b24 | -9.60443 | -45.33902 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 676049cd-c2e9-361b-bef9-6622dbd2d2cf | -5.79886 | -47.23935 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfe6ecac-e334-3715-958b-004e92f4122b | -7.12869 | -42.15274 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0cfb640a-16c9-364e-9a0c-896f42fd2252 | -6.83754 | -55.75931 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5eb9deeb-cf54-3d1c-add4-9dfb550197e2 | -12.51274 | -45.94661 | 2026-09-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fd57171-e4f5-3d5e-a3e5-04801cf9898e | -5.8609 | -51.947 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7589d7be-de21-3436-8d2c-ad7805a04cc9 | -9.23937 | -46.19708 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5948854c-8a59-3c16-86c4-1edab2144e06 | -7.45774 | -42.11106 | 2026-09-17 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 98877d72-3e6c-3d78-8193-3f78c6a2e943 | -6.76349 | -55.84526 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbc48953-8771-3ca4-b447-79512c6ec66c | -7.58943 | -46.33276 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| adafc25e-c39c-3647-955d-560af87da139 | -9.9452 | -45.43773 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78e9f480-b65b-3e14-8d82-024a2d03a028 | -7.09279 | -41.84417 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| fbcc7742-df6f-3197-8c61-89230f8f5bde | -7.86025 | -44.8325 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53d7c427-bdcb-32b5-b266-256405a41ffd | -11.63888 | -46.75191 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e51625b2-2378-3cca-94aa-0b1c1faeea29 | -8.6119 | -44.48883 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f079b75d-6c59-3650-9d57-9fbee77df22e | -11.52946 | -46.86657 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47173e35-f688-3f19-8012-ae6a35970cd8 | -5.67703 | -44.82917 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f457236-8776-3c22-8f93-369e342dc87b | -4.60806 | -50.92263 | 2026-09-17 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c02fc3c-ddba-3421-b73d-9402a4d22f29 | -6.9999 | -43.33167 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dc03bd0a-1806-3888-9c53-330f2372ceca | -5.6479 | -44.8094 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a472d1f3-87e2-3574-88dc-b930749be993 | -8.49241 | -57.63668 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9fbd6a4b-152a-306b-8e9e-cc9e24399a32 | -4.51091 | -54.97279 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ff3f6ac-90c3-374b-ac86-9d3ae416820f | -9.61925 | -45.36265 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 535f1386-1a48-3789-b6af-099bd1eee575 | -9.88306 | -48.39428 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 556abad2-42c5-3b01-a5d0-d77927bb4c6c | -11.49373 | -45.74005 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9446994b-06ce-3093-9a27-179efe0bef7c | -8.84155 | -46.92401 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35963257-d2b8-3ce1-b785-aab60a71e405 | -9.83554 | -48.36018 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cbb57af9-1816-38f3-95df-e2e0c6c2d06d | -5.4795 | -45.13129 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c10d1a29-bd8d-3d5b-b1b0-76a6a47e3a06 | -5.85802 | -51.94268 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57dfafe8-087a-30e8-b8fd-e2971fdfb7d7 | -6.90244 | -59.02456 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f15de91b-7315-3c80-826e-52575e264cce | -10.40669 | -48.6635 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f476e0c8-7ccc-313a-8249-9cc61f513521 | -9.89106 | -48.38776 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32f362ea-c725-3e65-a9ec-5802b614940d | -11.53186 | -46.87644 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51c54ce3-4301-3e51-b22c-161e76ff4c6f | -12.50109 | -45.91198 | 2026-09-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77a5aad4-5171-31c0-9a39-3a5d156b37de | -7.19226 | -41.81395 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 13dcc17d-fbba-32fe-955f-cde5893c2962 | -11.52879 | -46.87121 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f91be17f-4a48-3633-9398-af3ef6a95aea | -9.94917 | -45.29008 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f5940d6-6712-3ad9-a27a-c85f59936ca3 | -7.02805 | -42.06627 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9a5e03ac-1100-35e6-91a8-e999790731b4 | -10.83132 | -46.14731 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f5435e0d-b7c0-34ee-809f-fb35790148f3 | -5.73465 | -43.28068 | 2026-09-17 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94c57a0c-6144-3f37-ba54-fea17bd6393a | -7.12659 | -42.16837 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| de409b87-0a1f-3d64-a2e7-9a24a0bafbc7 | -5.76873 | -45.10798 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 8da48c96-d8ae-3b25-8c97-fe93c04ec809 | -6.89068 | -43.74664 | 2026-09-17 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4741b576-51e0-3a8f-bd4f-a50d4ed412b4 | -7.11458 | -55.1279 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52fbeb6-98ca-3dba-bcaa-32726e483158 | -6.77933 | -47.87119 | 2026-09-17 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2edc6dee-39f5-38a8-b46b-4ce8b18f1cac | -10.98658 | -48.30208 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43d5311c-c87c-3e08-a58b-d67eacaadce4 | -11.48824 | -45.77881 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c949729-1727-3d5b-b9f9-3498bcf2e70c | -6.45433 | -52.8376 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e685c2a3-f196-34f3-8e2b-440b7ad85682 | -6.27032 | -44.14732 | 2026-09-17 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b84c295-cf1a-3968-a674-c2818088a971 | -5.89366 | -52.06384 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dffcd53f-3627-3954-a4a8-9263e2a333c2 | -8.47771 | -44.70199 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b266c641-841f-342b-be59-734fd65ed6c9 | -6.76908 | -42.77009 | 2026-09-17 04:40:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 440373ad-cf99-31d0-b5c7-d36798a40e22 | -9.11622 | -45.72594 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| e062d8fd-8c4a-33cb-902f-eac6403028f4 | -10.80855 | -46.1688 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55671f2f-ec6e-34b8-b69a-7cc7da92291c | -9.77263 | -60.46566 | 2026-09-17 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| da47c4c1-b547-3ad4-b70c-26af0040f915 | -7.07504 | -47.49284 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00df390d-2159-3f44-8d7e-ab68b34e08a3 | -9.27882 | -44.38543 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62ccb33c-7ab2-38c3-83f0-2f390ffb6615 | -9.15576 | -49.99469 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50015885-25b2-37aa-a1fc-ec26c7d03dcf | -9.49065 | -45.42223 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02c1068b-823d-321f-9721-53f9bb7da0cc | -11.53935 | -46.87758 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2be5232e-b4ae-3dd3-b8af-8021ff4b770d | -6.67161 | -43.64625 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 306157d7-5817-3674-8f70-a3b2ff9b5f93 | -12.32461 | -47.95962 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2afaf631-986b-3922-b576-3de311600539 | -5.76594 | -47.17587 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efb79769-92d7-3600-8416-7417febe4c99 | -8.20125 | -43.6741 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54db4e6d-3b25-3001-b1c3-ccf9e84e7214 | -11.90089 | -47.5837 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eca70146-d449-38f3-a399-e42dfb335e9c | -9.94568 | -45.43425 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00a93c97-dbbc-37bd-b2a8-3470c4eafaef | -9.42594 | -49.54351 | 2026-09-17 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a62edc85-d610-3403-b8a9-6ea9592dfa7a | -8.52665 | -44.50891 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c45ca11-378b-3ece-9c99-871628f5e073 | -5.9026 | -52.09745 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 410ef2b4-4ced-38bb-b36d-f46cc1b1c439 | -7.12702 | -42.16742 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e8373276-5c54-33c3-8a3f-e66a209cdc28 | -6.37308 | -58.28909 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e486924-59a4-34f3-a53e-5cb1a6b47581 | -9.96448 | -45.32848 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ff59f28-1557-3e2e-86a3-6d1c296d9df2 | -11.0208 | -54.15199 | 2026-09-17 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cac23fcd-99ae-3b08-b76a-f3a99d9faf12 | -8.57847 | -44.57456 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a45daf17-0d5c-3a40-83f9-228dd2073f01 | -9.8413 | -48.36863 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae485a46-65ac-314b-8a05-d49c26d8a3a6 | -6.66058 | -50.9139 | 2026-09-17 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43044777-7fba-3e4e-827e-3bbcf6c2a539 | -7.06637 | -47.50337 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7088bd46-f6c4-3e4c-b8d1-e3a02b9540e6 | -9.78246 | -46.59164 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c51d8ec9-387e-3c0d-9903-b07c41d79855 | -8.47825 | -44.9002 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d5da38c-841f-3762-926d-45fb7e7628b8 | -7.9717 | -47.65419 | 2026-09-17 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90a7fb98-d12d-3a38-9c17-5169dae00f04 | -9.84408 | -48.34994 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 276560ca-9aad-352b-a420-326fe63ec965 | -4.49391 | -55.49861 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e6ee8b4-749d-3599-940b-6af3de48dfcd | -7.02735 | -42.0715 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| d1ceab54-aa1d-3916-8ccd-f68ab0e6d3e8 | -6.77822 | -47.87848 | 2026-09-17 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9253fcc2-e059-3309-a19d-876ae0d61c0a | -8.28494 | -45.65176 | 2026-09-17 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16562158-b43f-390c-b820-e2c50e08268d | -7.11892 | -42.08583 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6dfda3c5-2ae5-3997-890f-ef5d16a8982f | -7.38127 | -44.51694 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06b87282-9d57-383f-be86-4427dcbe154f | -9.62072 | -45.3521 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b89a06ea-69a1-3b5a-99d1-47c197e089a9 | -7.49842 | -44.91103 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e229da0-d7b4-3676-88a4-b7bb8f1b59d8 | -8.55386 | -44.47653 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7e7e07d-4982-3bb5-b21d-0cc5924ecea6 | -5.19413 | -49.33287 | 2026-09-17 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91478ea8-5c10-39a0-95bd-58f6cc69686f | -7.83627 | -50.23249 | 2026-09-17 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d74382c8-9997-348b-b447-e5182e0b4a92 | -9.40731 | -60.35575 | 2026-09-17 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README43.md)
