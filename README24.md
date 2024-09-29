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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e23ac4d0-7818-3d19-a339-86ccc257e3b3 | -5.0862 | -46.17695 | 2024-09-29 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b2088a0-4cc8-3caf-9fb3-d8a5dfde2745 | -5.34316 | -44.90888 | 2024-09-29 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2169d5d9-989f-38c6-99d4-0506ae1090da | -5.3258 | -44.98829 | 2024-09-29 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0d9a82d-7adf-397e-bcbd-977ac8197ab9 | -5.32519 | -44.99196 | 2024-09-29 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 700d6895-8664-305a-9cc3-1bf3d802b766 | -5.32171 | -44.9876 | 2024-09-29 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b456a77-5f53-34fa-b3e1-cc20f9b3b0ee | -5.73137 | -46.48363 | 2024-09-29 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb6ba6e7-3d68-34dd-afcf-73a8ba3f9600 | -5.22545 | -45.14416 | 2024-09-29 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e0dd31d-20d5-350f-952f-0c5d4304b8d0 | -5.22131 | -45.14346 | 2024-09-29 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67dad8ff-ff87-3423-af0f-e7bd370a5be7 | -7.48967 | -46.12803 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e45e44a-1a8e-3d22-aea2-8a368dc2f998 | -7.21689 | -45.48135 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a32d525-08c6-335c-a68e-7cb92644a51f | -7.19662 | -45.88638 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eeb52633-0158-3f14-961a-95c7b24b617d | -7.19449 | -45.87366 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09be59fc-7aa7-3a9d-b686-7697f0c8f7c0 | -7.19426 | -45.87342 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a89f73ab-440e-3777-b0f7-da4fb643d4e4 | -7.19173 | -45.88954 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 42e1ea28-ebcd-3aff-bc02-2c4f939114fb | -7.19162 | -45.88934 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 35f098b1-1f0d-39a2-805e-a73100eed7a4 | -7.19105 | -45.89344 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92132935-772a-3cb2-9672-9c078a334b61 | -7.19097 | -45.89326 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4251edbe-7abc-38f9-9d7b-1c1c972392c3 | -7.1903 | -45.8728 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c69e55a5-2c0a-34f1-8cf4-5245aed2d6ed | -7.18749 | -45.86398 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17de4b2b-6fe2-3595-ad3f-35e3251cfd92 | -7.14907 | -45.43925 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76163d7a-e986-3772-b6f4-47d38083d128 | -7.14708 | -45.59255 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ed07f783-ec93-328f-a015-c891fd91d771 | -7.14642 | -45.59634 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c919b56c-2eb0-356b-bbce-a5b985cdbdf1 | -7.12823 | -45.85337 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc3947ac-d50d-39ab-8def-669f27dd6f8c | -7.05586 | -46.14725 | 2024-09-29 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 966f195e-6d4e-30f6-bc58-a9530d66074c | -7.05516 | -46.1513 | 2024-09-29 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42249686-997e-3f7f-a5bf-2a3dce76fc9c | -7.05084 | -46.15062 | 2024-09-29 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5930da7f-9574-3f2e-9184-4a4094e52a1b | -7.03788 | -45.35255 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bbe3d31-1c5b-3f64-ad80-e3067cdb82a2 | -7.0338 | -45.35184 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6db4654-bca1-3c7c-89a0-7a10f7da2a30 | -7.03219 | -45.33634 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ed2c839-f932-31aa-861a-54bd43e51f60 | -7.02811 | -45.33561 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e3fec6b-93cc-3993-a243-bde7aecd80b5 | -7.0275 | -45.33927 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c43d2ecf-13cc-3531-a2ca-c485f40b8bee | -7.00585 | -45.34319 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2473d99-b8bc-3a1f-b75c-b7620ff1d27b | -7.00523 | -45.34685 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83693ac7-1dd9-3657-af4a-7deb023767bc | -7.00116 | -45.34609 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c51a23f-1401-3e7a-975a-4f8ac2480688 | -6.95226 | -45.68577 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 527f4d98-6457-3211-a7d8-5e6a2b8fafb9 | -6.94136 | -45.853 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc869e37-a7df-308a-acc6-fa9856c86689 | -6.94069 | -45.85698 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 845f7389-696a-3852-b3f3-2b8b60dbe076 | -6.93715 | -45.8522 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1865537b-d80c-3958-b0c2-8602187ad5af | -6.93647 | -45.8562 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c3919d4-a3b4-39da-a9b9-a894c0be0e62 | -6.90286 | -45.97746 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d129e67-a1d5-3ff1-b662-c02276052de6 | -6.89364 | -45.98002 | 2024-09-29 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b548aea-451a-3ec9-ba63-d1d38865947f | -6.58361 | -45.70758 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81cd6565-5365-395c-b999-f26dcbb28a61 | -6.56575 | -45.70814 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd7ebf31-7fce-30e0-88e3-f06fe3d3b996 | -6.54479 | -45.72997 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 029406e9-7f3d-3080-9198-88d303613c03 | -6.54413 | -45.73397 | 2024-09-29 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f40abd06-78c5-3598-8b21-ae729ed9317a | -7.83322 | -45.47191 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 289a0e1f-f42a-3310-98df-5b72cc5091fe | -7.80843 | -45.49429 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4344f68d-10a2-3903-8b43-5c1358979393 | -7.944 | -45.65779 | 2024-09-29 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98d450f8-087d-3dfd-b7fc-93801f4c4942 | -7.83947 | -45.53346 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fba14800-1a7f-317d-b0b9-9461dfd06160 | -7.83886 | -45.53706 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c587f87a-ae1e-3f5b-9152-451831459793 | -7.83479 | -45.53628 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a60318b-1231-3f9e-9755-9f8a394be40a | -7.83317 | -45.52118 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cddcd8d0-5b51-30eb-9a49-bba2b773f39b | -7.83255 | -45.52481 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b2d6354-49cb-3f72-977f-4afe1379aee4 | -7.8291 | -45.52043 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b17e8d5e-310f-3d75-ba05-03ae504515e6 | -7.82452 | -45.57185 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c16f5db3-97a2-3aef-9c15-83f7405d3e94 | -7.82034 | -45.52256 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aaa29050-41ed-3c23-b004-ecddb5c003ca | -7.81342 | -45.51398 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3b87368-30df-37c1-ad9d-d6efe8b1299f | -7.80872 | -45.51689 | 2024-09-29 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d0cab92-2965-3d90-9468-3d7cee770aee | -7.73971 | -46.1681 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b666b524-f669-37d4-85d7-2341363fa95a | -7.739 | -46.17225 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2cc1b90-4b82-3fb2-8ae3-3b0065b1574f | -7.72784 | -46.55541 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 442daff9-86a2-3f52-ba6c-d2b2c2a60cc6 | -7.72657 | -46.55995 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afe86ec9-e9cc-3624-a6d9-0c8733c46a3b | -7.72729 | -46.55566 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c41a5be2-3d22-35c9-ade9-52266ac2335f | -7.72709 | -46.55968 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8533132-2f92-358c-81c1-f9eff991ef79 | -7.72272 | -46.5589 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce45e8ad-84d1-3700-bf07-26f322fe26f3 | -7.72219 | -46.55917 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc3c0a09-64f8-3203-877e-48424985705d | -8.3291 | -45.65518 | 2024-09-29 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e7f34fd-b570-3da8-9768-6e74576da980 | -8.90648 | -45.65664 | 2024-09-29 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4c5e0b6-a776-3114-8ff2-b8adcb06335c | -8.42096 | -46.35102 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 16b7b46b-f942-359f-8a1c-381068e8a723 | -8.42026 | -46.35503 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7502eb22-fcf1-3a6d-8dc4-7496c9c405ba | -8.4164 | -46.35847 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c62f03fb-04ac-361d-9b06-fae86b139db7 | -8.41172 | -46.35357 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27a03db2-eef1-3ac3-b525-0d28de5fdeeb | -8.96615 | -46.87975 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d30685e-e02b-38c5-80f6-b4dbc416f57f | -8.42448 | -46.35602 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d3c4576-1a35-303f-8a07-af1fe30c7b25 | -8.41709 | -46.35434 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c68fa102-baa3-315a-9a45-7b477419afe9 | -8.416 | -46.35426 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c9fc5b34-0e10-311a-9bd0-094311edcc5f | -8.4157 | -46.36256 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 836e0d37-3cf7-3f0a-bd95-40688d00a651 | -8.41527 | -46.35836 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f60b5b73-9dc4-3416-a144-3a798b8df2b1 | -8.41456 | -46.36242 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 971fc0ce-33ff-3056-b68d-1ef90422796d | -8.41282 | -46.35361 | 2024-09-29 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e208dc58-4934-3d7c-b161-9d954a515dc5 | -8.19914 | -46.81393 | 2024-09-29 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1accc05b-dbc2-3657-9642-0c40076294ed | -10.90007 | -46.35681 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 113ae8fd-cf2d-39f3-b6cc-715d9ea39eda | -10.89661 | -46.3524 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afe09652-d672-3f44-b468-fc3f48f1cd34 | -10.8925 | -46.35173 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49890213-7dd7-3110-8fb9-77485fdeb9f9 | -10.88301 | -46.35777 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a48f7b1c-2a36-3d61-bf2d-eadf6e562f24 | -10.88237 | -46.36144 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 436d2d9a-2fcd-3a2c-9f80-118c32aca26c | -10.78445 | -46.555 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c23390e5-7257-3e7d-8e10-ac2f0a447352 | -10.78315 | -46.56226 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 834f4cbc-6fd5-34e5-9078-0d5d2b21c13c | -10.78241 | -46.56639 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e768e0ed-0d88-310f-afa1-890b341bca68 | -10.77909 | -46.56102 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 260e45b3-9fd6-3f5d-9c02-b9b6926507b8 | -10.77833 | -46.56523 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f61a5687-e663-31ae-9c28-9ed0708bafbb | -10.77566 | -46.54609 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b23ec34-f8e3-3648-8662-07cad438be85 | -10.55477 | -46.02991 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1915a6c7-c914-35e2-a93b-12663876a640 | -10.55412 | -46.03357 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8606beaf-73fa-369f-ae7a-1efc73dac427 | -10.55074 | -46.02919 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecc6f311-f332-3834-b63d-64eb26af5672 | -10.53669 | -46.03804 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bb944b2-1267-305c-902e-e4d91b957f32 | -10.53605 | -46.03789 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bcaea5c-a117-3f09-9751-2859c052debb | -10.53022 | -46.07452 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a9901f8-b5d6-37a9-a79c-efbe88f2a681 | -10.52984 | -46.07445 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 566467e5-8a94-3b24-8ec9-e459ca69f85b | -10.52673 | -46.04373 | 2024-09-29 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
