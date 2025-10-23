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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e0ebdbf-e63e-3d9e-8702-67388464d0bd | -21.44084 | -54.54882 | 2025-10-23 05:01:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 464ed491-2d27-3ca2-ac45-76e830365369 | -21.43924 | -54.5512 | 2025-10-23 05:01:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 766d3827-b96b-3de8-bccf-2fc8a563c06d | -21.43983 | -54.54688 | 2025-10-23 05:01:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e95c29-6ce9-348a-85e6-21dee67b1f5a | -21.64157 | -49.75687 | 2025-10-23 05:01:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 900d9331-117a-3513-a9a8-eb127f492224 | -23.44024 | -47.43027 | 2025-10-23 05:01:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 250f6b67-3010-3818-a2e2-b7acd8cc140d | -23.7231 | -51.69568 | 2025-10-23 05:01:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 590f8efe-ffbf-37fe-bc2d-b532095da6c4 | -22.23873 | -56.1049 | 2025-10-23 05:01:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3dddfb1-c3c5-3738-92fa-054edcb2f2e0 | -23.4369 | -47.43054 | 2025-10-23 05:01:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7fa2b745-1feb-3f1e-b3a7-bf784c5d2615 | -22.23477 | -56.10825 | 2025-10-23 05:01:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78063592-bcea-3cfd-b008-cf00a56734c7 | -22.14494 | -44.83818 | 2025-10-23 05:01:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 71be3d48-ea91-3ce5-af6d-6525a5449e43 | -23.5915 | -54.76903 | 2025-10-23 05:01:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1927b65a-de0c-3f4b-a859-d12c3fb303e1 | -23.86536 | -50.51141 | 2025-10-23 05:01:00 | NOAA-20 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e4ce697c-f074-31e4-bcff-e569dab96adf | -22.14494 | -44.83817 | 2025-10-23 05:01:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b4b81ed5-b30b-32e4-a940-06090dfaf344 | -23.43988 | -47.43437 | 2025-10-23 05:01:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9511e128-5a36-30e0-90fe-34b9593cdb20 | -31.56707 | -53.72282 | 2025-10-23 05:04:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 3ac4e486-645c-300f-ae04-388a81c68c07 | -3.0168 | -49.4906 | 2025-10-23 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| e64670dd-6bc8-3dd3-84e5-147d7cf85f4a | -3.0169 | -49.4694 | 2025-10-23 05:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b1adf8d0-dec3-366f-90b9-4eb9a70680f6 | -3.0169 | -49.4694 | 2025-10-23 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b60954af-e30c-33b3-8ead-c5da7fc0286e | -3.0168 | -49.4906 | 2025-10-23 05:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 421c78ca-0faf-3165-a39d-e19151cd7180 | -3.0169 | -49.4694 | 2025-10-23 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ab633ba2-0692-3452-9c0c-df561fe13136 | -3.0168 | -49.4906 | 2025-10-23 05:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 79066709-58b9-38c2-9aae-875512740a70 | -2.80946 | -54.37754 | 2025-10-23 05:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 279b8740-c552-3da7-8231-a0e240507a31 | -2.81126 | -54.38262 | 2025-10-23 05:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09b4fd4d-e7b6-31c8-a7fd-ee0f705a3932 | 1.65734 | -55.74908 | 2025-10-23 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 559b2cd1-15e5-375b-a817-544649876bf2 | 1.65842 | -55.75591 | 2025-10-23 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f225ad6-7f70-377a-b6ae-807e6220a572 | 1.65733 | -55.74908 | 2025-10-23 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5754989-2055-3100-949e-5f003dfb3f39 | 1.65788 | -55.75251 | 2025-10-23 05:46:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcf1b937-a17c-39e8-99b6-e5d22db5d04e | -2.81202 | -54.37755 | 2025-10-23 05:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 23289c5b-aa36-3e5f-a946-9c88682a6b2f | -2.98296 | -53.99861 | 2025-10-23 05:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39e816bc-3ff5-3148-8967-8c2bab709d5e | -9.01343 | -65.93917 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41353c04-4f55-3fc2-a3ab-5d0dccb05561 | -9.55483 | -66.64792 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc90be1-43a3-3168-b4a7-eb896c243470 | -11.78588 | -62.71019 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26965a64-924e-371b-91f1-c670c1e06ac7 | -9.76076 | -64.97507 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 306b0038-6a85-3004-aa13-fc7ac0602881 | -14.87661 | -59.63063 | 2025-10-23 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4fe4d5c8-1927-3ea5-ad86-930237596219 | -9.97849 | -65.1154 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83b8f94f-1f23-329d-8246-136442f22afe | -10.26853 | -62.08731 | 2025-10-23 05:50:00 | NOAA-21 | VALE DO PARAÍSO | RONDÔNIA | Brasil | 1101807 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78ee8884-f4e0-3e98-9a61-ffe068bef451 | -9.11326 | -65.93987 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f1f9ecc-f38b-3eb9-be71-cfa44052d95c | -9.975 | -65.11486 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b408f4-570f-3f8f-984f-d18997a52990 | -9.68128 | -64.11942 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddad36b8-b83d-3dce-9385-ace8e7cab6bf | -12.09743 | -63.62045 | 2025-10-23 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 87d52bde-4a51-3335-aa30-11e8bbcc0591 | -10.73147 | -69.35375 | 2025-10-23 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93e2d0bd-5446-38b0-b3bc-a82633b85886 | -10.87032 | -68.41987 | 2025-10-23 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a577edd1-6675-3d71-a6ae-2fb6742f7abe | -10.46148 | -68.46508 | 2025-10-23 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65fa19e4-af98-3266-b787-03f8842e7849 | -12.37542 | -63.87171 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ba492c3-e366-3aad-b21f-d32c1623cfb6 | -11.78588 | -62.7102 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c80dd3e-7f4d-3199-9b77-70a58b617ab2 | -9.98277 | -66.76173 | 2025-10-23 05:50:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ccb9083-ab18-35e4-aba4-3a58c0d549e9 | -11.96133 | -63.12781 | 2025-10-23 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03c9e9cd-5d41-30d4-b617-6bcfc74c9838 | -9.78149 | -64.17641 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da4f3f02-5ff0-3001-a41b-254b4617c6c0 | -10.86977 | -68.42337 | 2025-10-23 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16119563-5bf5-3327-b7a5-8f992351c6c0 | -12.13659 | -64.08853 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 443dc180-f1ab-3a15-b01c-c57f42565ec6 | -12.40044 | -63.86055 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0e7c196-0b78-30cf-8ac2-ceadf4375887 | -14.87661 | -59.63064 | 2025-10-23 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aad2b493-1dd2-3c8d-a59b-8297c24e6d87 | -12.13266 | -62.9674 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a029d845-c487-33b9-9406-5b503567f1ec | -12.69994 | -61.06387 | 2025-10-23 05:50:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 584a8949-b6f8-379e-b146-50ad3074535d | -10.88025 | -68.42146 | 2025-10-23 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbfe2c79-4ca6-3cd2-a924-96aefb3d3909 | -9.79101 | -67.95068 | 2025-10-23 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67b65d34-9977-3136-873f-ae214e244b20 | -9.98277 | -66.76174 | 2025-10-23 05:50:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e67ec18-4853-396a-a857-a3769b6ca3fb | -9.76585 | -65.08447 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea4abec1-bb19-3c4d-b542-9ec38d63b285 | -12.37159 | -63.87114 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b01cf933-544d-3fbe-a06d-efc027d4a09f | -12.13317 | -62.9638 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f941e261-c56e-3551-a64d-ed89e923ff4f | -9.55155 | -66.64709 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24a6c735-764c-3d8e-a86b-2a30d345e486 | -9.11906 | -65.93663 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7423b81-d2ad-3e4c-8ec4-ce5576bacbe1 | -10.53212 | -68.53441 | 2025-10-23 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eef80a2-a8a7-34a9-86eb-16632fe5fde0 | -10.45817 | -68.46455 | 2025-10-23 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e0adb64-49bf-32b6-9a4a-789ed841bf25 | -11.11124 | -62.66146 | 2025-10-23 05:50:00 | NOAA-21 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032e9d2d-8e8d-3bbe-b00e-4e4e8cc6e646 | -9.75493 | -64.96606 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fede67af-97dd-3fe8-afa6-c997cc4bc2cc | -9.72221 | -64.96919 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f6eea6e-584e-3d2e-9234-c6e15e7ef995 | -9.1258 | -65.93769 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5db8dbf-b7dc-3fc8-b546-e9ec9f7066b6 | -9.1127 | -65.94348 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82cc13a0-8660-3d41-bf5d-6a2bd0c38e0a | -12.12913 | -62.9632 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91cd4343-2727-3de3-b87c-4b1562de5d12 | -12.12863 | -62.96681 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 030a41fe-951e-3c91-afc6-a2334e2244c7 | -10.46204 | -68.46156 | 2025-10-23 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcf6387c-118c-3eb2-b61a-a94a2c416987 | -9.11718 | -65.93676 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16e78cf8-17c3-3098-ac70-76e88dc46eb7 | -12.31702 | -64.0418 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a933947-9199-303b-8c95-89fd3a36ac8d | -12.37609 | -63.86688 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f624b77-1072-354f-b24c-06387f303d50 | -10.99019 | -68.3931 | 2025-10-23 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c7ae223-c495-3f4b-9aea-fd421cb32d44 | -9.78624 | -66.86771 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d46f62ad-4353-37b3-ba7e-f03cdc4e5d30 | -9.75784 | -64.97057 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc25ca5f-ca92-30da-a9cf-a95fd24b1044 | -11.11073 | -62.66505 | 2025-10-23 05:50:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 565f2013-39b6-3b13-b9bd-7084995983ac | -11.97519 | -63.91688 | 2025-10-23 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8011e23e-b2d3-34e7-bedf-ba418ef6c6b8 | -10.34712 | -62.84234 | 2025-10-23 05:50:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5d2e9f5-0df6-3f3b-8ae4-e85ccee9e4fd | -10.86977 | -68.42338 | 2025-10-23 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11805590-e987-3141-92e8-043beeb76783 | -9.97849 | -65.11541 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 09c9e8a6-c5e7-3b19-9a3b-9eb3ec6b0ce3 | -12.10005 | -64.29441 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42aadedb-f503-3b40-baf1-d926dc4d7800 | -11.96398 | -63.16745 | 2025-10-23 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3675f586-1cf4-386f-8a21-327c1dc8bdac | -12.37992 | -63.86745 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aaf627b-c570-31df-8add-06755ca84ee3 | -12.31702 | -64.04179 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bff22e2-933b-3c79-9ff4-e4b8068c3338 | -9.35045 | -65.67567 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45f723ff-ca3d-3ee0-9e5a-96aa5e6d67d2 | -9.72514 | -64.97364 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c054252c-599e-3216-8075-23963495e64d | -9.72163 | -64.97311 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 052c0961-3de6-37b8-8927-ab067a52d712 | -11.78638 | -62.70655 | 2025-10-23 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4972e501-0425-349d-949a-9c7187b6c361 | -9.97945 | -66.76122 | 2025-10-23 05:50:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03b2e8b8-550b-325a-b0f9-ae6d5ee711b1 | -12.37925 | -63.87228 | 2025-10-23 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e295220-989a-36f7-9e10-eff1f9118fe1 | -8.7308 | -67.05086 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0551285-6e6e-3430-8a1b-e36bf9a2f9ad | -10.35109 | -62.8429 | 2025-10-23 05:50:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f79268f-f077-35c6-909b-fbe7ae6cb279 | -9.68494 | -64.11997 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 071c7e6b-438f-37c4-b4ec-15a4db031095 | -9.551 | -66.65063 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5189765-1c11-3670-9ef9-2fe42fc2f549 | -9.1258 | -65.93768 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4df1a62-15b6-349d-8ab2-b2a3cdcb4579 | -9.85528 | -65.18932 | 2025-10-23 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 024f2b8b-258f-38a4-a693-37df417d49eb | -9.01007 | -65.93865 | 2025-10-23 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
