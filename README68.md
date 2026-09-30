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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b97cca8-d5f3-35dd-b68e-adfe96105ab3 | -6.7254 | -45.5749 | 2026-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ea699059-39fd-31c2-984c-262a3aae62fe | -9.8617 | -44.9347 | 2026-09-30 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| c73aa4ea-f02f-3eec-bd99-e6422ba5ff39 | -9.6654 | -46.7248 | 2026-09-30 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 81766e96-7fc4-36cf-8f94-54e037cae9d7 | -17.5338 | -43.7135 | 2026-09-30 13:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 8f6e479e-59df-3c88-ae92-998b462f2f9d | -11.7182 | -43.4386 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| cedabd0f-0f4c-3a73-89d9-b6382d797eea | -12.4346 | -44.1733 | 2026-09-30 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 81a1a9d1-97a7-3d3e-9b56-b5372cbe7098 | -7.2561 | -43.3697 | 2026-09-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 6091d32f-3775-342c-99de-1f5e30385403 | -7.2944 | -43.3191 | 2026-09-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 74ff1d7b-57da-377b-abe3-c3c88d2651e3 | -6.7059 | -45.6441 | 2026-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 8f34b176-0545-3a50-8a5d-8df60558f7dd | -14.1115 | -46.2834 | 2026-09-30 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 119.9 |
| e8d4392e-b10b-3ab2-a804-99a646977cca | -11.6395 | -43.5455 | 2026-09-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| b7a90d8f-fc7e-3d28-abc5-ff3c8d9c3e43 | -6.7062 | -45.6216 | 2026-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| ca4ec5e6-ec69-3409-95d0-3f81f0d74498 | -6.7249 | -45.62 | 2026-09-30 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3dee2dc1-7bfe-3471-bf90-052059340759 | -11.1942 | -46.0637 | 2026-09-30 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 711c856f-f685-3931-a721-2ef54b077a37 | -10.1881 | -49.9703 | 2026-09-30 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 77807593-aa56-31fb-ab0d-f3a6ff1ab75b | -9.88 | -44.9783 | 2026-09-30 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 6dd59eae-434e-3275-a3dc-8fa6dbb9f7c5 | -13.3469 | -46.8169 | 2026-09-30 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 6a3c8d07-1d1d-3b05-814b-a1077d550338 | -7.2564 | -43.3462 | 2026-09-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9c64c402-cf8d-3a4f-a17e-855922bf76ae | -7.0074 | -43.7428 | 2026-09-30 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e51467cf-ce30-3b0d-ab6d-467235dcdd5d | -6.98532 | -71.77136 | 2026-09-30 13:40:00 | TERRA_M-T | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1843ef1a-d87a-3b10-bf98-b7446985396f | 1.66774 | -69.32489 | 2026-09-30 13:40:00 | TERRA_M-T | SÃO GABRIEL DA CACHOEIRA | AMAZONAS | Brasil | 1303809 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 57fd49ef-b822-3a4b-9405-e1fffafe4891 | -7.78999 | -72.89674 | 2026-09-30 13:42:00 | TERRA_M-T | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 991524ba-7809-3edd-aa46-06ee4750408e | -11.7182 | -43.4386 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 2160f435-623b-3c2a-b8fc-8e3edf0cbc16 | -13.3469 | -46.8169 | 2026-09-30 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| bed226c4-f3ca-37cf-8dc3-b1a6d855751f | -8.6448 | -45.3717 | 2026-09-30 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 03aa9386-cb14-3faf-8668-52cbfca38c98 | -9.8613 | -44.9577 | 2026-09-30 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 64431270-9446-3a7e-8435-3ba1c23c83c5 | -9.88 | -44.9783 | 2026-09-30 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| f8e90b77-f0e0-3bf1-96ee-b8b2024b7c34 | -8.8362 | -49.7148 | 2026-09-30 13:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 2ae9e2d5-a204-356e-88cb-fa240d4805bc | -11.4687 | -43.4537 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 063d7899-ddc6-34c4-886f-8d8016ebc3de | -12.4351 | -44.1497 | 2026-09-30 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 9031b5be-c2d3-3615-88a0-9fde7e56c8a5 | -12.4355 | -44.1262 | 2026-09-30 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| af6b1abb-4108-32ba-a741-35f158c6a57d | -8.0166 | -42.8681 | 2026-09-30 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 15fe353d-4f6a-3600-90e2-54265001d272 | -11.1954 | -44.85 | 2026-09-30 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| acd81711-4fc5-3725-888e-304c78d5cee3 | -6.7249 | -45.62 | 2026-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c9719d16-6453-3d1e-8dc3-c083cd225f32 | -12.4346 | -44.1733 | 2026-09-30 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 2ccd99da-a1a1-3681-9716-37f56ca7eca5 | -10.5496 | -49.7823 | 2026-09-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| cd37b1f1-bf8c-3915-8d39-d7ab1151684f | -17.5338 | -43.7135 | 2026-09-30 13:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 9cefb118-3b4d-32db-b6c3-6dee4f1c3a18 | -11.3918 | -43.4654 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| c332f8df-ee26-30fb-bfd1-3e4ee6a4eb41 | -6.7251 | -45.5975 | 2026-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| a60d6779-4702-3e96-81c2-b955694f2e3d | -14.3348 | -44.9017 | 2026-09-30 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 2a39d7ae-79eb-39c5-a115-f98c3423925d | 1.7115 | -55.9221 | 2026-09-30 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 089d98a7-1604-316b-ba91-a51dee5ca2a7 | -7.3278 | -42.0858 | 2026-09-30 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| d9ff433f-44c6-3047-8c26-e3e6ecb636fd | -11.2095 | -45.1478 | 2026-09-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 46e264d8-a743-3445-87ea-41d342b605a3 | -12.0694 | -48.5377 | 2026-09-30 13:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3d99e9cd-9c48-30a0-8865-040fc361a24e | -9.5087 | -45.7525 | 2026-09-30 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 96a7aa05-64d3-30dc-aff3-a504ace99ec7 | -6.7254 | -45.5749 | 2026-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 430bca1a-e6b6-3418-b978-e754269f2afb | 4.1882 | -60.687 | 2026-09-30 13:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5cf35f39-10df-3518-9c81-03e33277645b | 1.6933 | -55.9026 | 2026-09-30 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 48419eb9-0cd6-3ff9-b457-59f172a09bba | -8.0169 | -42.8444 | 2026-09-30 13:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 126.0 |
| 3c7e65e0-5f24-3986-8897-d95a0b3a2f9b | -9.4328 | -50.1086 | 2026-09-30 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| cd18e6d5-14b2-3b54-8239-58fee2c22611 | 1.675 | -55.9028 | 2026-09-30 13:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6785a09c-a014-399d-955a-305e8822cf33 | -7.3965 | -42.6498 | 2026-09-30 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 4c9374c7-b47b-3df8-932a-5cacd4d071f1 | -11.6797 | -44.5012 | 2026-09-30 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 09fe11dc-97c7-30cd-b5f5-8cf9f1194636 | -11.1903 | -45.1505 | 2026-09-30 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7e730693-fdfc-36bf-b16d-2642e202b87b | -11.2566 | -43.5331 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 7f90bdca-21ea-3e99-acf3-f97a0dbc3166 | -11.1958 | -44.8269 | 2026-09-30 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 499f96c8-5e96-3475-bd84-8b9884a4c39f | -11.4311 | -43.4121 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 9f679ac2-4ebf-3001-adf6-b15c8f02cc85 | -9.2229 | -47.3285 | 2026-09-30 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f5c85c60-085a-3064-b35d-9816a3fcd63a | -12.5135 | -43.0943 | 2026-09-30 13:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 161.6 |
| aeb36b41-d1f0-389c-8b0e-79fa95c5ee2e | -6.7062 | -45.6216 | 2026-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 16114fd4-f452-325f-a645-51cdb755fe14 | -6.7006 | -52.4933 | 2026-09-30 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 7d1bd5e0-ae0a-3333-93b9-1262b44d2da9 | -10.2847 | -44.6042 | 2026-09-30 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 72f78de7-376d-3ce5-a204-a9f9e1776e86 | -11.1517 | -50.0603 | 2026-09-30 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ca877162-ba3a-3c91-8b58-ba30f11c700e | -7.0612 | -42.3035 | 2026-09-30 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 957627c7-7bd1-3790-a85e-39cb020fb0d4 | -13.8784 | -44.4442 | 2026-09-30 13:50:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 425.7 |
| 1654625b-b0db-364e-b9e7-0a035ba285d9 | -6.8957 | -43.6368 | 2026-09-30 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| e7e8c293-fa5a-38f4-9656-9ab3a0985c4c | -13.0556 | -44.9364 | 2026-09-30 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 56fa16b3-66c3-3d16-9980-0348e2a05374 | -12.7618 | -47.2431 | 2026-09-30 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 55354b2d-b600-371e-a14d-278c24dc29d0 | -6.7247 | -45.6426 | 2026-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7082b90b-2d58-3ef6-aed7-ed603464d271 | -6.7059 | -45.6441 | 2026-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 78ff1ea8-782d-30a2-963a-783e8846a2ba | -6.6874 | -45.6231 | 2026-09-30 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3cd02fa8-f1e8-3470-ae9a-391e19032842 | -9.8617 | -44.9347 | 2026-09-30 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 28d68cf2-1361-320e-9e8b-873600ac14ce | -12.5329 | -43.091 | 2026-09-30 13:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 123.3 |
| c16aa437-556c-399c-b6fd-cbdae77fa678 | -10.2843 | -44.6274 | 2026-09-30 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 197.2 |
| a35700eb-5092-3ab0-8afe-e4fe526a10ab | -12.4539 | -44.1702 | 2026-09-30 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 239.8 |
| 436b183c-fa1e-347d-a508-1e48b1977d5e | -11.411 | -43.4625 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 71935409-a246-3846-a575-bfd0db82efbb | -11.6395 | -43.5455 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 03f7e60e-14df-3883-bcf7-2fc78bf36d9a | -9.9207 | -50.2323 | 2026-09-30 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| c393bda7-9eb0-309e-8d67-263877b31e11 | -17.5345 | -43.6891 | 2026-09-30 13:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 5a308fcf-8565-31e8-8fab-0d8a487af741 | -11.64 | -43.5218 | 2026-09-30 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 7b04d45f-c265-334a-93bd-5be58d8c9514 | -8.0166 | -42.8681 | 2026-09-30 14:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 179.3 |
| 1823a350-9f16-36e6-bb94-30a9037cbd30 | -7.2747 | -43.3912 | 2026-09-30 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 50cfca30-06ce-3d4a-83af-054f1eac1d2c | -7.3965 | -42.6498 | 2026-09-30 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| b044803b-b9b2-331e-9fc3-ecf53e2ab7fa | -7.2561 | -43.3697 | 2026-09-30 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 24975c29-accb-38c5-b58f-35e8b64e9397 | -11.4307 | -43.4358 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.9 |
| 2b31ed51-3189-3316-86ca-6925d99e9ef7 | -14.6277 | -40.6982 | 2026-09-30 14:00:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 115.6 |
| 99cb1ab9-89fc-358a-8743-2da7c7e7bd0a | -16.1671 | -42.8587 | 2026-09-30 14:00:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 458d8af6-e7bd-31e5-a7c7-f7e9cfb83b38 | -8.9823 | -44.1633 | 2026-09-30 14:00:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ae92fb9c-a0ce-3366-9fa6-087639bf6e6b | -11.7182 | -43.4386 | 2026-09-30 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| f69b6e9f-a80b-3262-8f67-e317a98dd83d | -14.3348 | -44.9017 | 2026-09-30 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 283.3 |
| 25ea649d-2152-30c1-ab7f-4cf4caf654ce | -6.7006 | -52.4933 | 2026-09-30 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 91231b49-a098-3feb-912e-7f07d336eadf | -6.8957 | -43.6368 | 2026-09-30 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 595786ce-9035-3e8d-8ada-6bc639b8dc75 | -11.2095 | -45.1478 | 2026-09-30 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 67ab7403-f6aa-36c6-a3fc-195da11960da | -13.8784 | -44.4442 | 2026-09-30 14:00:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 992.3 |
| dfffc86b-ec2b-3f10-b4a1-66a5944b19de | -8.2235 | -36.2935 | 2026-09-30 14:00:00 | GOES-19 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 144.3 |
| 7faa9d38-6345-3d1a-90ed-bf87b6b42897 | -10.5197 | -45.3784 | 2026-09-30 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4e479dbe-5795-35b7-b771-076cc348bbd6 | -6.7254 | -45.5749 | 2026-09-30 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 8fc9b555-d086-3bfc-957e-7e4b701e33b9 | -7.055 | -42.849 | 2026-09-30 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| b772edfa-57ba-3b9f-8e59-fdb3b7f4166d | -12.4346 | -44.1733 | 2026-09-30 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 394.2 |
| a8b7c8b6-bb58-35a1-9452-c975b2dd9f37 | -9.88 | -44.9783 | 2026-09-30 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |


[Clique aqui para ver as próximas entradas](README69.md)
