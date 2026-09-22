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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7d07b0d-d47b-3950-81e7-48a09f411675 | -12.2726 | -50.1441 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 0ea45a8a-ff99-39e3-9d56-e48e21e0747b | -6.3842 | -55.265 | 2026-09-22 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a32c87e2-67f9-367b-80fb-ba6998300a83 | -8.7703 | -45.8793 | 2026-09-22 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ae76f6e4-7920-3f90-86fe-6b11dca5f433 | -2.9525 | -57.72 | 2026-09-22 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 7aa84e93-7935-3ae8-9981-ceff3b09503a | -3.0534 | -61.2767 | 2026-09-22 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d16196d2-2db5-3f34-bbe1-eadc0a33b62e | -12.9478 | -50.941 | 2026-09-22 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b6b08c43-0903-376c-b0cc-6361cec1d373 | -10.4536 | -51.325 | 2026-09-22 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e14dcacc-3b78-3aab-8e17-62c033c76d86 | -3.4599 | -59.54 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| a832218b-3ced-3860-a9c2-074de7b43dbd | -5.9151 | -59.9522 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 41d5388f-5199-3f22-a174-3fe245749866 | -10.252 | -45.4811 | 2026-09-22 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e66d04f0-fefb-3031-9e05-2cc91d6fa34f | -10.7821 | -50.7624 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 19684928-79c9-38db-a60e-21f9620b13b2 | -6.3195 | -60.0147 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 17d6a348-99e6-39a7-a9e7-8bc8853035cf | -10.279 | -50.2391 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 752de000-d6e7-320b-9cd3-4db31b09c488 | -7.5247 | -46.2252 | 2026-09-22 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| c802d72a-c530-328e-b1bb-517def736db8 | -11.4213 | -47.338 | 2026-09-22 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| c806b080-642c-30fc-bac0-b5af1ad54084 | -12.6799 | -50.9526 | 2026-09-22 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a1100906-8e6d-39d5-8adc-327d099ff489 | -7.5945 | -43.4296 | 2026-09-22 14:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 79005939-1104-3f04-8bb5-3f268ea474d3 | -10.8011 | -50.7604 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3518d39b-db86-3499-8eb1-b845cc437ec4 | -6.2394 | -41.6875 | 2026-09-22 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 4ebd8776-2b2a-3246-95e0-d482c490d100 | -3.2395 | -53.9618 | 2026-09-22 14:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 223.9 |
| b4f50aea-7e5b-3bda-81ac-b2d0b218e682 | -8.4799 | -57.6085 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| cea6d400-6b42-34ac-a76a-fbffa6f88e02 | 3.9505 | -60.6352 | 2026-09-22 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e660dcc3-cff1-36cd-8d47-51595c052f1c | -6.3926 | -45.1268 | 2026-09-22 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 151cea6c-c064-39bb-9a25-72f1e4e6c7bd | -6.0925 | -57.6847 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 172.3 |
| ff79d63d-caee-35c6-a436-66c7c3beb34d | -6.3014 | -59.9579 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 4903a275-1003-3982-936b-13935a5b054d | -10.3357 | -50.2333 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| dc6ffad9-e4f2-35f1-9958-5f47d10d03e2 | -3.4599 | -59.5209 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d7ad8b93-0feb-3814-be05-529c2028f20c | -12.8056 | -54.0462 | 2026-09-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 211.1 |
| 95c08a27-2c73-338e-9603-dba2c2e5881f | -10.5425 | -43.9649 | 2026-09-22 14:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 25f9248d-db1a-3b07-88fe-60357288f6fa | -6.3287 | -55.2677 | 2026-09-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ef3a82a9-171a-318a-ab82-6a9dd025f500 | -3.2372 | -60.8007 | 2026-09-22 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 71f67982-7cca-35ea-91f2-6d438ddb9efc | -7.1555 | -47.4751 | 2026-09-22 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e99f4674-c1ee-3d06-b625-04e5b1148b4a | -3.2212 | -53.9422 | 2026-09-22 14:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e27d0ecc-bd93-3f83-ad1e-db280e29ff3f | -11.0991 | -54.0285 | 2026-09-22 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d02ed2ce-331f-3a08-97e4-f3a8629d9171 | -9.6108 | -43.9477 | 2026-09-22 14:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 6745667b-43cc-33c7-9bda-54e0a9b98ee7 | -3.0358 | -54.4085 | 2026-09-22 14:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 960bc557-95ae-3a5b-95c0-22f9eec26a76 | -6.1651 | -47.5271 | 2026-09-22 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4bade183-f0a3-3b3e-85fb-d23a86a7cd1c | -6.9871 | -47.4885 | 2026-09-22 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 24b53b85-c71d-31a8-a16f-ff54aa43c149 | -3.0717 | -61.2764 | 2026-09-22 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 62967282-bba8-3881-a386-81cd44724a9c | -6.0365 | -57.8235 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 975fb793-3241-3650-b594-2a45cd447cd0 | 3.5482 | -60.6623 | 2026-09-22 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 172b994e-8109-37f8-b74b-ddc7efd18bc5 | -6.9681 | -47.5119 | 2026-09-22 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a6256570-c801-3421-9b51-4043126c7630 | -3.4272 | -58.2138 | 2026-09-22 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 027296b1-30df-3c46-a111-aed4b68ff743 | -6.1838 | -47.5258 | 2026-09-22 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| aab7fa46-3117-3d03-b4c2-8eceb389c083 | -10.6878 | -50.751 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 878b7700-35af-3de7-8229-e7206e00c973 | -9.8404 | -46.3911 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 8d56945a-1280-308c-b790-c20cd6d119cb | -6.7464 | -59.4223 | 2026-09-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 69e61b99-357c-3738-9557-e50419380339 | -5.5717 | -42.7414 | 2026-09-22 14:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| f3f99fd6-8f25-360b-9172-bf4dc1860344 | -6.2587 | -41.6377 | 2026-09-22 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 4245a29c-d7f2-31ae-bc6b-3872fab8abc7 | -11.7079 | -50.9811 | 2026-09-22 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 85582f79-7a4c-3e93-a52a-6adb3d505922 | -6.295 | -57.735 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 616b9c07-e68f-30e0-9d96-e147bab73c07 | -2.5687 | -57.5135 | 2026-09-22 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 85e6e0c9-ca78-31a6-b82a-b808d676fac1 | -6.0926 | -57.6652 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 7eb3ba32-9e07-3552-84eb-e3d9f6cdaf2f | 3.7681 | -60.468 | 2026-09-22 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4980cb44-7f8a-3b2f-948d-86d995beca79 | -2.9723 | -57.214 | 2026-09-22 14:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 4cc6ab33-a895-3011-ae96-959d4309f708 | -11.4209 | -47.3603 | 2026-09-22 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 62fce7ac-ac92-3614-ae7c-6c4e7ca7bb81 | -10.4108 | -50.2683 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 819ff5fa-dd2b-3937-8e4a-cdf84d5b2822 | -11.4404 | -47.3355 | 2026-09-22 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c844726b-e017-377e-a76d-25a587305e5d | -4.0925 | -62.0874 | 2026-09-22 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| dfc75be2-c878-3d64-b7ac-a674d9b9a7e0 | -11.8559 | -49.979 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1b8e4ec2-b7f9-3574-81b1-0d94a291cff7 | -3.2211 | -53.9623 | 2026-09-22 14:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4e64d755-0251-3bdb-882f-40fac2ea83b4 | -3.7364 | -58.8818 | 2026-09-22 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| becdbb84-8992-3cbd-b0b9-d6c4332b19c7 | -2.9723 | -57.1945 | 2026-09-22 14:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 966e226b-3ae5-37a1-82cf-395d327c9690 | -10.7437 | -50.8089 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 41bd20b7-a26d-3a00-b490-39f2b281d595 | -2.9906 | -57.1942 | 2026-09-22 14:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f9f3037f-88bf-3648-a0e5-1248da6c96dc | -3.3867 | -59.5415 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 05ccc43b-9e32-37a8-bc5d-f6b3e33f0a5a | -3.331 | -59.8483 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 88bde8ab-be5f-36bd-93f2-c5e4d09bdb55 | -9.5329 | -45.3861 | 2026-09-22 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 6990ad19-f472-3117-80ac-bdc6de45d044 | -3.405 | -59.522 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 198.6 |
| d9e3f961-0c99-3f39-a523-24c3e72b3ce1 | -3.3001 | -57.8487 | 2026-09-22 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 54a8aaf6-03bd-3406-ad65-f035c17f3249 | -3.3492 | -59.867 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 5442ce89-e399-3b5d-8d27-9bdcbc3b60a1 | -8.58 | -44.5552 | 2026-09-22 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 88b6e964-78a7-3057-904b-1c544e48aaa6 | -9.6302 | -43.9219 | 2026-09-22 14:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| bfa70f81-d737-3e8e-8b2b-aa1c0d7432e1 | -10.4539 | -51.3038 | 2026-09-22 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a15c03ab-628f-3628-96e8-af6475a301fe | -9.84 | -46.4136 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 80fcf954-758b-34a4-b5ed-1f45efc7c42b | -2.8608 | -57.7994 | 2026-09-22 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 162.6 |
| c5238195-ffc8-3e07-a10e-aa933a9dbd2d | -12.4016 | -47.003 | 2026-09-22 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 157.9 |
| e98b9c81-6e29-3ab3-b6aa-c867bf31f5d6 | -2.8791 | -57.8184 | 2026-09-22 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 606461d3-61f1-34e0-880e-2843939c50f1 | -11.2879 | -54.0317 | 2026-09-22 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1b6936d9-59bb-35dd-afaf-0a0cb9e5a9b4 | -12.9273 | -51.0291 | 2026-09-22 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 84642418-3f18-321c-a6a6-590cb6b9ded7 | -5.8489 | -49.7875 | 2026-09-22 14:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b01316c8-b5e1-3497-a22a-05b3604cc792 | -6.0992 | -59.9267 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 23d93fe7-811e-38e8-b84f-dffa49c4fa91 | -12.7865 | -54.0482 | 2026-09-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 211c0e6a-259b-3a3a-bb68-4e2f73302cb5 | -10.4111 | -50.2469 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 55381e54-65de-3d29-94ca-d9ea8a52867c | -12.2918 | -50.1417 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 71c8a88d-1bbe-3e59-979a-13ffe54b1285 | -3.7364 | -58.8626 | 2026-09-22 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 4af2fab1-9935-3728-8c10-d0b5233af3f8 | -12.4008 | -47.0481 | 2026-09-22 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| d98d4352-4188-3233-aa3b-6c5bae373d0d | -10.5906 | -53.9918 | 2026-09-22 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a390d42f-8697-3880-8784-844f84a44230 | -6.8985 | -41.6976 | 2026-09-22 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 8a7a5319-e0b2-3122-9047-0efc58dee4c1 | -7.146 | -48.4352 | 2026-09-22 14:40:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 4efe6019-ead2-337c-b464-64cf1dcf42bc | -8.4985 | -57.6075 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0bfd33fe-13d5-3a82-8c95-ace0f94a9302 | -10.7073 | -50.7064 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ae77a836-b4c8-3d1d-ba20-5f0f80886d27 | -10.4105 | -50.2897 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0c943000-99b1-3fa3-98f3-5ac0c981e43e | -12.3672 | -50.1971 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 29142de6-7dc6-30bd-97e9-faa6ed10c3aa | -5.9148 | -53.5372 | 2026-09-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 3214b251-10d1-3400-82a9-624ba0c2ba0d | -3.4781 | -59.5396 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 1cd9ffba-2639-3e5d-b230-bed909d1f5f6 | -6.9948 | -52.8658 | 2026-09-22 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 125da46e-fd7c-39bb-9fe5-9c07d2f3792a | -2.8791 | -57.799 | 2026-09-22 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| a687be1f-d7f3-35dd-b654-446cff1d9728 | -10.4541 | -51.2827 | 2026-09-22 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 9c0b6d4e-c641-3414-b2a8-37ae86da4271 | -8.7912 | -44.301 | 2026-09-22 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |


[Clique aqui para ver as próximas entradas](README142.md)
