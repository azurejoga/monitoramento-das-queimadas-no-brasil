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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f97c949-696a-3981-9064-68c2808acd62 | -3.00902 | -54.13849 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 896e7dd5-87d4-397c-9660-7597fb833759 | -3.34785 | -59.51056 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd5e3472-9121-35a4-9268-f44f7aaafe05 | -4.15128 | -55.15131 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76fb61e6-0025-33c7-803b-dd0c2fb1eb14 | -2.7667 | -54.08052 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd635c9c-7e83-36e6-a918-5de75f77c4b9 | -2.83627 | -54.07609 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf29d4f4-a599-3427-be27-42161a78f9f7 | -2.85525 | -59.11347 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 788db678-e077-3433-a067-18e55a36fb1e | -3.52435 | -54.67028 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 24fde84b-c8e4-316b-9c00-fab22f69cb99 | -3.49947 | -54.64579 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91a75773-c9fe-3c07-8434-9d7c86abe173 | -3.73478 | -59.44411 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2afe8ea-eab9-3539-8ef1-e62930d94066 | -1.10385 | -54.16063 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd287bb3-e113-3365-86fe-7116a67132d8 | 1.0341 | -59.45068 | 2026-10-07 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efeb6258-1dad-383f-8ce9-73b3d5a8bafb | -3.10677 | -54.16708 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ba118fc-0f5f-30cd-89be-304079c6a38b | -3.67398 | -55.94764 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fa1d1f6-020a-3277-82d8-817653568312 | -2.76865 | -54.11602 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a4f42f8a-fc2b-3d96-9e1d-524391f44998 | -2.99959 | -54.13046 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 55cffcd8-a6fb-3905-8968-d3a376fe98a2 | -3.58478 | -54.30801 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 704f8bc8-2238-32a5-9e18-53be1809eb1d | -3.8586 | -56.00163 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01c3eef4-448d-38e6-97f1-6661d6817bd6 | -4.15227 | -55.15205 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 264999ec-4668-390d-b719-e893f238169c | -3.08297 | -54.27685 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80f9ec66-7860-35ff-aee0-bb039812fc7e | -2.76969 | -54.10908 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c3fff058-5e0c-336a-8534-65975cac36ad | -3.38536 | -58.21143 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c005394d-830a-3483-b83c-407f7e5b08c7 | -3.69182 | -55.96082 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37b2dbcb-4c5e-3b20-af3d-4c94c6329537 | -3.43793 | -56.9423 | 2026-10-07 05:59:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06b2cb24-fa4d-337d-9c8e-7c67eaf846f8 | -3.8957 | -59.33277 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3bbc36e-1d82-3e92-90bd-cee97c97943c | 1.97862 | -60.61533 | 2026-10-07 05:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a35ce6e-1bf9-3fe0-a247-1be9d61de98f | -3.50044 | -54.63911 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df086bf6-6465-3651-b31e-3683261a4fc8 | -3.09711 | -54.279 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ca797955-fc6f-3d94-b0b9-858dc37de94e | -3.48221 | -59.47209 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e39545a2-8640-38a5-9337-c91a48873325 | -3.5567 | -59.48092 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 029db283-7098-3cb1-ad1b-b313cc037c0d | -2.12883 | -54.79821 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a1395ca-4619-36d4-87e2-886ec56c9424 | -2.87256 | -54.20341 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cfeabad6-1fac-3650-9203-5babcc9db22a | -3.8545 | -55.98454 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 78605d27-08a2-3b88-95ca-108d5dba5f52 | -3.4887 | -59.58753 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c9d9458-7ed4-3b9d-9421-16a3a0587349 | -3.52123 | -54.64304 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ffca616-4550-3214-9174-71bde6c1b44c | -3.08569 | -54.28922 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5ac0df9f-6b51-32c2-950d-dc2faf9b2c2e | -3.51962 | -58.7555 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75db5f25-4c1e-3a24-ad4d-9aaece644ea7 | -3.07456 | -54.26602 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b9e873d-dbc8-3aeb-8308-7ad22ccc3524 | -1.8022 | -57.11473 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cfba853d-38fb-327e-aa05-ecedb3a0f6ce | -2.87348 | -54.14658 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e40d686-af31-329d-a966-81ec8d5975cb | -1.2956 | -54.56557 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4892ba7f-524a-3e97-a15c-52a6b6ee77b3 | -3.3764 | -58.19483 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 129e46af-37a9-3ff7-8b4d-5bdcc361864e | -2.1279 | -54.80431 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6204245e-1689-3a00-a809-63a95a9c52ef | -3.89617 | -59.32961 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ea2c96-dbfb-3676-9b69-faad7e4c4feb | -3.47662 | -59.47436 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc440419-d545-365e-8e22-4929c725085c | -3.3492 | -59.50165 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed557178-71e2-39e7-8e5a-bd5d7c87f345 | -2.77073 | -54.10217 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4afaa514-0d60-3dfa-8efe-7b900b402e05 | -3.07991 | -54.29715 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4aeb5fdf-1629-344d-a798-a4bdd33f8859 | -2.84019 | -54.07693 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0c14669-3b5d-3728-a855-c9a4d40c53d1 | -1.79832 | -57.10577 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ff015be-c302-3ea6-b8d8-202b6e0b758f | -3.99358 | -56.25099 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20ee0d39-3e70-391d-a3ef-b2cae454d230 | -3.07795 | -54.26208 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05ae690d-54f1-329f-98a0-65bbe7c75569 | -3.99376 | -56.26321 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b452dcc8-af30-397b-9381-0407cf421ff7 | -3.07041 | -54.24445 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21258e5c-222d-3828-912b-252d0b9bf3f2 | -3.65907 | -60.62455 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 43009b16-7a0b-39b4-aace-7813765ed2ab | -3.99205 | -56.2612 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de6ff64a-21f0-3431-a4e2-5f47f5646f44 | -2.52909 | -58.0976 | 2026-10-07 05:59:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57b1ff40-8bc9-3527-b6cd-a1e99675e415 | -3.4887 | -54.6286 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8347c4ee-6a68-322a-a26c-6f67ed1fbf0a | -3.79124 | -58.29123 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94cd0bf9-21f2-39f6-a8fb-e154c59bbc27 | -3.5174 | -54.66923 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 04318f61-d804-3b99-a181-b9bf8dc05bca | -4.14205 | -54.92541 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| afb6317d-3044-36e9-972e-2371c96c33be | -2.76566 | -54.08743 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 28bab7c9-cbb2-3182-917c-a69aea907a8d | -3.07696 | -54.26864 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e73b3c28-7eaf-3a71-8c10-29fbd21eb00d | -4.1607 | -55.14179 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98f5b590-06b8-3ba0-a25a-4021a974838a | -2.8013 | -54.09271 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74331c2a-a1a3-30c2-9f1d-a431b6db3337 | -3.5631 | -54.48745 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4d9c9c5-ac57-30b4-9e9c-195dc1bde4e7 | -3.77212 | -59.40559 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4b40410-3cc7-3884-bbbe-b49c4097f4e0 | -2.71572 | -57.47571 | 2026-10-07 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dd00c88-fd42-3d57-a945-2083b9269823 | -3.61809 | -55.28579 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8116a71b-18b6-3fce-9c2a-464890b27176 | -2.80236 | -54.08572 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3652822-c828-39ea-9483-733d85b6066d | -3.00289 | -54.13048 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1de5932-d59f-3f9f-b356-8c505ced54e7 | -4.15627 | -55.16463 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cf49264-a22b-3b70-a0be-88dca17da42a | -2.77176 | -54.09531 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1ecc1b32-e4a8-3c7b-88c6-01ef01352889 | -3.07089 | -54.26087 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0716f96e-2434-3ba1-8b5a-046d6de53d70 | -3.63952 | -58.89086 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31ab9edc-5c7e-3dc5-a048-b7e4f0e9e427 | -2.78303 | -57.65654 | 2026-10-07 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64ac6dbc-981d-3bc9-b262-8b99932b5a18 | -3.23898 | -56.80647 | 2026-10-07 05:59:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46134e1d-e4c0-3022-9b7c-705b59e13640 | -3.38143 | -58.19939 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad0bca50-8fa2-3e6a-b73a-c87108b8eab9 | -3.09748 | -54.18043 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1018f4a-cc74-36a1-8ceb-d31ac6fc5a95 | -3.3483 | -59.50761 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d11aec6e-0593-30d3-9b88-06a0439921ce | -3.47846 | -59.46231 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4133aabd-cedb-320c-96ea-230730052613 | -3.55203 | -59.47711 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58380468-abab-3d9d-b855-fdd0f95ee922 | -3.9889 | -56.25176 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a520dd3-3ee4-38e7-ba63-62890af23581 | -3.85296 | -55.99506 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09a58643-4932-3d88-9f48-580f9c5da5be | -3.68074 | -55.95121 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07681c21-de15-34ae-bc66-8454eec6742a | -3.08796 | -54.29173 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8f0fc8e1-2b77-37ee-9bfa-ea34b0927fae | -3.55112 | -59.48319 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4ae50b2-f536-39b1-a47f-3a7db8424bbb | -3.5245 | -58.75974 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38c083d4-7a72-381c-a6ff-236a09c2f816 | -3.07896 | -54.25535 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 108e167e-79df-3c71-9906-e1fe79b9dcfa | -3.68868 | -58.89112 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 318583b4-900a-366f-b9a9-d851f899a040 | -1.80285 | -57.11041 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a577146f-33a1-3360-847c-397da18ecc55 | -4.269 | -54.8746 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3218af5-01f4-37b6-a226-0421f332905b | -3.00064 | -54.12349 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| df76f7e8-ba98-3190-b0ed-652b696e6997 | -3.5333 | -54.65778 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5b71f87-ebcc-3247-b301-0d59f7553386 | -4.13072 | -54.909 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89023f34-323c-3485-a72f-d2643fd743ec | -3.67888 | -55.95908 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6115572d-c3d8-340f-aabf-57ca075eafe9 | -3.58764 | -54.56726 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 015211bc-c791-3f5f-8081-ae1988f5c586 | -3.74509 | -59.44568 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39f1ced1-c007-3d79-90e8-fc3a35e7c4f7 | -2.94254 | -54.17136 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f5e3e70-d138-3907-9fc3-5f5b1dda485f | -1.80414 | -57.10688 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3497588f-27d4-3a5b-8cf7-8143c6c35840 | -2.70531 | -59.8014 | 2026-10-07 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README117.md)
