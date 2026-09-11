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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a5e62b3-caba-348b-8041-87ebe9ee4584 | -6.7686 | -45.0051 | 2026-09-11 11:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 34c4dfad-9da2-3a4e-af9e-d1c5cb11e43e | -10.7959 | -45.9575 | 2026-09-11 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| c3f9754c-f225-3e00-934c-302fca477905 | -8.6192 | -47.4114 | 2026-09-11 11:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c80c2acc-ac49-36ad-b5b7-af5c44fc6d1c | -8.6378 | -47.4316 | 2026-09-11 11:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 0c87daa4-fb60-3d2e-9f32-aba886c82c39 | -6.7686 | -45.0051 | 2026-09-11 11:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b41978c8-2d83-3a37-8cf6-1455fca9072d | -8.6381 | -47.4096 | 2026-09-11 11:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 03357fde-dbec-31d4-88cf-35fc703b107f | -6.7686 | -45.0051 | 2026-09-11 11:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 05f4bcda-3f7a-3058-8657-af0ac1be8ddd | -6.7686 | -45.0051 | 2026-09-11 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 37cf5a2a-9e37-38e9-bbdb-ee5240791f1c | -13.4453 | -43.8366 | 2026-09-11 12:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 271d576d-2097-3cb0-975f-3e4142339b6a | -10.7963 | -45.9348 | 2026-09-11 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5e7d3615-de9b-34cd-b9a7-b49f9f7cc09c | -6.7686 | -45.0051 | 2026-09-11 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e8d8003f-a17c-3419-a005-79a2d2075aca | -14.0864 | -45.6203 | 2026-09-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 95e037a3-53af-3fc2-af48-f79e68b7f7f0 | -13.4453 | -43.8366 | 2026-09-11 12:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| eb4d218f-8ee7-38e3-95d2-f5548dc99dfc | -14.0669 | -45.6237 | 2026-09-11 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 7defdfd4-5efd-3602-a8df-6264336c211a | -10.7963 | -45.9348 | 2026-09-11 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 7bb00f6e-e87e-3487-9100-f48a51a5ca65 | -10.7959 | -45.9575 | 2026-09-11 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 1f240a41-3370-396b-a518-43f7b55409b4 | -14.6026 | -48.8601 | 2026-09-11 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f354b28f-cd85-3764-bb39-e988357ef8be | -14.0669 | -45.6237 | 2026-09-11 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| daa8523b-c174-3c58-ae09-123374d8215c | -14.6031 | -48.8379 | 2026-09-11 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 194135e2-800c-307b-8051-2adf6f76dd69 | -8.6378 | -47.4316 | 2026-09-11 12:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f365a81d-6db1-3d4f-87c4-655d5d8693f8 | -10.7963 | -45.9348 | 2026-09-11 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 34e1cff5-72ef-3022-ac59-e68babcc1964 | -13.4453 | -43.8366 | 2026-09-11 12:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 92b9a279-3a89-3f35-afe8-d779cac1ed24 | -10.7959 | -45.9575 | 2026-09-11 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| ad44a293-f0e6-3184-9882-70f45c8d02fb | -7.1533 | -45.8766 | 2026-09-11 12:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 1cbd2b0e-7551-37e0-a647-54d359c9a169 | -7.5553 | -45.1624 | 2026-09-11 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 96a8f797-7a05-343e-b7d2-79f6c1ac7ea1 | -13.4453 | -43.8366 | 2026-09-11 12:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 95a4eae1-0c61-354c-8286-8335df9767c7 | -6.6888 | -45.4877 | 2026-09-11 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 3fe1e8f1-085d-3bc8-b945-38d7b1f092ed | -7.1533 | -45.8766 | 2026-09-11 12:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 37e6c166-7c46-3415-bf09-72b964b18945 | -10.7959 | -45.9575 | 2026-09-11 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 918842a3-c19c-3f54-9ddd-90e378d45913 | -6.7073 | -45.5087 | 2026-09-11 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 8724d3f9-d5a8-34b9-b6d8-14509ec2a1be | -6.7075 | -45.4861 | 2026-09-11 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 4b3762ff-4376-3c96-8fec-ec473f32a7bf | -7.9645 | -43.9971 | 2026-09-11 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f91c8231-3404-3c56-a39c-7048436d11e7 | -9.9041 | -45.91 | 2026-09-11 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| bfb08f94-9516-3673-b713-9f3a6edfead2 | -9.6951 | -43.3981 | 2026-09-11 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 115.3 |
| c261f12f-30c5-3cd1-ab8f-b97dfd7b0793 | -7.1533 | -45.8766 | 2026-09-11 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| de9a92ff-43dc-3a9d-b04b-a25883aa3f3c | -13.4453 | -43.8366 | 2026-09-11 12:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5e20008a-6de5-3e3f-9874-22b3ee43ebc3 | -14.6026 | -48.8601 | 2026-09-11 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f2666475-5425-309a-81cb-9b9380477957 | -6.6888 | -45.4877 | 2026-09-11 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 81b99a85-ad7f-38f4-8254-8878ba9ceff8 | -4.3582 | -54.77 | 2026-09-11 12:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 27534d02-68d8-397a-8ef3-6b9ca9126e98 | -7.9645 | -43.9971 | 2026-09-11 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e1de5569-e192-36d6-bc57-86a36006ff20 | -6.7075 | -45.4861 | 2026-09-11 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 01dc99e2-b303-3aba-a88c-045ff67137b9 | -6.7073 | -45.5087 | 2026-09-11 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 8eb42664-6e16-3f83-8ea8-8e761a04264c | 2.86609 | -60.78168 | 2026-09-11 12:44:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c341e180-79fe-3ea1-808d-f8f33b9abf2e | 1.32292 | -60.70794 | 2026-09-11 12:44:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 01d534b7-63ed-3128-885d-4c445b4a03f4 | -8.83689 | -62.48853 | 2026-09-11 12:46:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b616ff64-cd99-3147-92b7-e8fe1ab50442 | -4.86984 | -56.00663 | 2026-09-11 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 4e2c9754-1513-3ffe-b811-62396fd940ff | -9.21773 | -65.58125 | 2026-09-11 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| b7ee1e1a-f7e3-3263-a6ba-ec531772086c | -4.3664 | -54.77668 | 2026-09-11 12:46:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 98046ef0-06a7-369b-b989-7df3764db54a | -8.4558 | -64.05138 | 2026-09-11 12:46:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6c9a58e8-cd78-3964-adeb-88d49e5e6744 | -5.36497 | -56.01923 | 2026-09-11 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 12d0ca0e-d22a-3db3-bf15-c0465a51ded7 | -3.13872 | -60.66326 | 2026-09-11 12:46:00 | TERRA_M-T | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a46c4dd6-3980-3fbb-bc54-85526a12f1be | -9.02066 | -60.41512 | 2026-09-11 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fcdf2cb4-a03e-31a9-b272-82d66e184195 | -6.15168 | -57.80893 | 2026-09-11 12:46:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 1c9ee4db-8d61-3871-815e-c4c6087f3353 | -9.03993 | -65.40752 | 2026-09-11 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 784e444d-be72-37b6-bb38-87a44ec4a408 | -6.55774 | -62.8888 | 2026-09-11 12:46:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b81d77e-5263-396e-b1af-67465c1bb49e | -6.68849 | -59.97561 | 2026-09-11 12:46:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b8e37688-9357-36aa-a3da-e9a4dd67945e | -9.21926 | -65.57104 | 2026-09-11 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 24fbd0e9-4950-3565-93e1-98d82bcf4618 | -5.97284 | -57.77357 | 2026-09-11 12:46:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| e1a99824-0fe0-314d-9095-87b5307794c6 | -4.53931 | -54.95734 | 2026-09-11 12:46:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 7e5627e9-6f56-3e98-9a74-d83a284c4d98 | -8.83815 | -62.47955 | 2026-09-11 12:46:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4caca9a4-32b0-36ce-adea-dc4495246026 | -4.35243 | -54.77472 | 2026-09-11 12:46:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ac10ba4d-1d71-3302-ad70-dcd355cb3c67 | -8.25541 | -62.75194 | 2026-09-11 12:46:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4f61fb81-0757-3e0a-abaa-553c55275545 | -4.85698 | -56.00578 | 2026-09-11 12:46:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2e1888e5-7a00-3e3c-b1c9-1e57913fdca4 | -8.08051 | -54.83762 | 2026-09-11 12:46:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| f3f51e12-2dbf-34cc-9bad-380e7eb111fd | -9.21684 | -63.64139 | 2026-09-11 12:46:00 | TERRA_M-T | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f7cf1116-1b4b-3714-90b2-a4ad9dec34f1 | -6.80688 | -58.6518 | 2026-09-11 12:46:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 51fd33f5-95ae-3726-ab0c-c89fcb839016 | -9.54498 | -60.8363 | 2026-09-11 12:46:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4b21aadd-6df8-3ab2-8a87-53741a18e14f | -8.63624 | -66.51463 | 2026-09-11 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 65688ba6-6712-313d-abe1-303e7234da35 | -3.15961 | -58.64634 | 2026-09-11 12:46:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9afde673-e1ba-3b86-9f95-084afe43f878 | -8.63801 | -66.50286 | 2026-09-11 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3bfc3940-d0c3-357b-b0b5-2034aaa53f56 | -9.1437 | -64.39673 | 2026-09-11 12:46:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 63458fda-ea51-342a-b2d5-8755f1333553 | -8.46473 | -64.05266 | 2026-09-11 12:46:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c94c5d4e-00b6-318c-ba6c-bc4864b2486a | -9.03842 | -65.41759 | 2026-09-11 12:46:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8ae51199-9fd3-361c-9598-462c29a2de6b | -3.74155 | -61.75134 | 2026-09-11 12:46:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 081c7515-b23c-3649-a160-c4ad39943078 | -12.94941 | -57.24485 | 2026-09-11 12:49:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0fc8d72d-18dd-36c5-88d7-092e8e8a3a4f | -13.25732 | -61.59527 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 95.5 |
| d3f8fb46-469c-3f65-9eea-582bdb717ef3 | -19.99592 | -55.12076 | 2026-09-11 12:49:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6ee8a37b-2e32-3f4f-abf7-08b16605f97b | -13.25871 | -61.58468 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3f8e413b-f210-3df9-90df-95a74e721300 | -13.2164 | -61.834 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 49e9c020-9ddc-3c44-a7bc-67bca57ebc9f | -13.32362 | -61.67931 | 2026-09-11 12:49:00 | TERRA_M-T | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 909d16d0-0f88-3d0a-9ef0-fa6a579f9bb4 | -13.29444 | -61.82362 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 26e5361e-93e6-3d2d-b80c-a3ce0fe9e16e | -11.81309 | -60.45449 | 2026-09-11 12:49:00 | TERRA_M-T | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c3f75b0e-f99c-3b7c-bb8f-eaef6c6d181d | -13.21804 | -61.63714 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 21.8 |
| bbb6b780-6ff1-328a-9a1c-30057322140c | -12.16248 | -64.1343 | 2026-09-11 12:49:00 | TERRA_M-T | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1f78b7ff-a7ac-3d20-a9f0-2b01841b88b9 | -13.21945 | -61.62663 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7ab96893-4328-3cb2-ac2e-b1d27d964846 | -13.24779 | -61.59399 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c0f81242-7e62-3dec-b044-6b9e9a3ce614 | -9.75491 | -64.94684 | 2026-09-11 12:49:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d6efbe02-e865-3f30-90fd-1ff6d1d5adbb | -9.42281 | -65.86417 | 2026-09-11 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c01d45fe-3cd4-37d8-a0fc-3e0be911cb45 | -9.42441 | -65.85369 | 2026-09-11 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 313c4821-a94d-34f5-bdd8-2ac398cb87e4 | -13.22581 | -61.83528 | 2026-09-11 12:49:00 | TERRA_M-T | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ced3309e-588b-3665-add0-a658e5cfcf66 | -14.6026 | -48.8601 | 2026-09-11 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 90089112-6bda-3ac7-8bf8-2160e58be949 | -4.3582 | -54.77 | 2026-09-11 12:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 84a09672-6eff-3c1f-8ebc-87d85989409f | -9.9041 | -45.91 | 2026-09-11 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9656fb0a-69f5-3585-b3af-93b078610342 | -9.6951 | -43.3981 | 2026-09-11 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 18e70d80-3d59-3173-b273-5ab3900ef91d | -6.6888 | -45.4877 | 2026-09-11 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 13333847-ee7f-3729-a7d4-255ab3711b5d | -7.9645 | -43.9971 | 2026-09-11 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| e6e365ce-d135-3205-9221-00bea0f53cec | -7.9834 | -43.9951 | 2026-09-11 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 56d08966-2424-33d1-86d6-59755acf50bd | -8.6192 | -47.4114 | 2026-09-11 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a38bc43d-f608-3047-a3bf-5b1cd842e50e | -13.249 | -61.5983 | 2026-09-11 12:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ea790666-b3fc-31c6-9012-d5454ea063c4 | -14.6031 | -48.8379 | 2026-09-11 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |


[Clique aqui para ver as próximas entradas](README38.md)
