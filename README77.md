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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b69b575-7913-3692-b117-3d3dbf78f880 | -3.3447 | -42.9004 | 2025-10-27 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| c8a0da8c-4cba-361c-82e6-b31cb111f132 | -7.5242 | -46.27 | 2025-10-27 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 74b13831-708a-3723-be4b-50d1bfbdc66b | -7.8408 | -46.487 | 2025-10-27 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 341826a6-11d7-37db-be5b-3ff5af109fa3 | -5.7758 | -42.9842 | 2025-10-27 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 1dacaf7a-4855-39e1-8368-2a9e84688b6e | -6.5417 | -41.5876 | 2025-10-27 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 6c7600be-1bd1-3282-aa52-d7dc6f23b2e8 | -4.3877 | -43.3362 | 2025-10-27 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 257b2414-2cde-3aae-a625-c4e66f1d69a1 | -4.4602 | -43.6569 | 2025-10-27 14:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fb7c9cdb-2338-3494-beaf-80d972f32b29 | -8.6526 | -44.7771 | 2025-10-27 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 5d352044-c38d-300a-b459-263f239a3eb4 | -4.8953 | -42.9776 | 2025-10-27 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7b8c77e5-ab08-30b7-a0ae-991b59039d23 | -7.8225 | -46.444 | 2025-10-27 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5652420f-4766-3ae7-bcba-61c034911989 | -7.8411 | -46.4646 | 2025-10-27 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 03bb7a9b-d1a3-3938-8f29-5b59bb0f1c25 | -5.6431 | -41.1114 | 2025-10-27 14:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 333.2 |
| 3c1923ce-a1f1-31b5-98ac-54618f1ea67c | -4.0993 | -44.6183 | 2025-10-27 14:10:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 240cad30-ddf0-311b-9af2-fedc7a2502ee | -4.8933 | -43.2349 | 2025-10-27 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 63bda05a-8a72-3713-a340-b206e0a37e99 | -6.1923 | -42.6205 | 2025-10-27 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 3971eec1-9312-3536-b513-b677fec86137 | -4.4618 | -43.4248 | 2025-10-27 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 814e659b-9b1e-327c-b5b1-302a29a31527 | -3.0203 | -44.3934 | 2025-10-27 14:10:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| dfd01c96-6d52-36aa-86d8-38736a8e0b58 | -7.2379 | -44.9868 | 2025-10-27 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 64ff4c67-3149-3b9b-ad52-136b2ae9903e | -6.2306 | -42.5463 | 2025-10-27 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 19861799-3f09-353e-b4ff-b33b5ae16934 | -6.154 | -42.6946 | 2025-10-27 14:10:00 | GOES-19 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| dd1dd5c4-b68d-36c4-88a0-090458ec0509 | -6.1812 | -43.7448 | 2025-10-27 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| aca8c2e1-7a8f-3188-91b3-cdecb8315d6b | -7.8223 | -46.4664 | 2025-10-27 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| cfa49349-678c-3f8f-ac61-6f34e0ab051d | -7.0835 | -45.3865 | 2025-10-27 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 43d219bb-8cb2-3d82-842a-81b54d74735a | -7.5868 | -45.703 | 2025-10-27 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1a7ba4cd-8595-3af7-b8fb-453af2c42902 | -3.3448 | -42.877 | 2025-10-27 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| b9e4fa3a-3b77-318e-bc4a-59194df24f0d | -4.2035 | -42.95 | 2025-10-27 14:10:00 | GOES-19 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d8e8f871-1cb4-32a8-a201-5c3e357d5f59 | -4.8558 | -43.2373 | 2025-10-27 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3f76b62f-22ef-3451-b0a7-806572dc4791 | -7.8159 | -45.3875 | 2025-10-27 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c8116e76-623b-3f11-87d2-10594a5166bc | -7.0695 | -44.9335 | 2025-10-27 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d725be79-13ff-300f-97dc-09fdb27cfe79 | -7.346 | -47.1515 | 2025-10-27 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 5192dad1-115d-335e-82b1-3e28d74c1d35 | -14.7816 | -44.9599 | 2025-10-27 14:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| a59e09f4-5943-3bcd-a4ff-be87ba8c59ff | 1.6203 | -55.726 | 2025-10-27 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 4cbbcd57-e8fa-397e-943f-1717fad93017 | -2.9961 | -41.6859 | 2025-10-27 14:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| df5c4199-5bd8-3658-ae89-89d427cbce2d | -7.2567 | -44.9851 | 2025-10-27 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f0c2021e-33e3-36bf-b162-31c897625a24 | -6.4312 | -43.1411 | 2025-10-27 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ff6f374c-2268-367a-8129-ba17dec0dc80 | -7.822 | -46.4887 | 2025-10-27 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 356ea1b4-d6c9-3fd1-9363-e85529d8fc3e | -6.5603 | -41.6099 | 2025-10-27 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| 99052705-0a02-3e87-92e8-2b326b24e23b | -14.781 | -44.9835 | 2025-10-27 14:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 216.4 |
| def29d34-0c99-38d5-91c1-ee88acf1296f | -7.1524 | -47.782 | 2025-10-27 14:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0a57bb8a-6d8a-3e00-bf73-b2603d135d8d | -3.7096 | -44.3409 | 2025-10-27 14:10:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 0f74fca8-dfb0-390e-9cd8-e01570e64306 | -7.141 | -47.058 | 2025-10-27 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 045e84b3-e8c2-3486-a770-421a206912a6 | -7.9252 | -45.6937 | 2025-10-27 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4ac15de7-e113-396a-b3d5-259ac359b5b1 | -14.3982 | -51.5443 | 2025-10-27 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 7f7444ed-4552-3505-a09e-3738c05f6d85 | -4.388 | -43.2896 | 2025-10-27 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d66df722-271f-345e-a70f-fcbe354dca02 | -4.9138 | -42.9998 | 2025-10-27 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.0 |
| b285e313-29d2-3846-8b50-89c65fdec0e6 | -6.1735 | -42.6221 | 2025-10-27 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 87fc73b7-3241-3d19-8f98-df77c8d04d9d | -14.781 | -44.9835 | 2025-10-27 14:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 204.5 |
| 336b4eac-0187-3639-a7fd-5d5536891992 | -8.287 | -46.8902 | 2025-10-27 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 5ef4e2df-3114-36c4-8b8d-e0c11896b61a | -4.2457 | -42.2408 | 2025-10-27 14:20:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 2b22cc08-10da-34f7-97e8-bfeee09cb3fd | -7.6675 | -46.8806 | 2025-10-27 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| abda4743-804e-334d-b44e-ea0a3813fcb6 | -17.7119 | -43.7686 | 2025-10-27 14:20:00 | GOES-19 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a70ad8b7-b42a-39bf-ad4d-451255328f49 | -2.8972 | -42.8257 | 2025-10-27 14:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f2d6bbf1-b151-31c5-b319-ea1e50ecd09b | -7.257 | -44.9623 | 2025-10-27 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8c9b7871-f977-30b1-8200-d5478234d48c | -7.8159 | -45.3875 | 2025-10-27 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| e32b4448-4e71-3d98-8bfb-c6d78fceb81e | -4.388 | -43.2896 | 2025-10-27 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 64332c6c-f4aa-3a69-b666-0f342ebe547e | -8.9336 | -44.9523 | 2025-10-27 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| e59ea7fd-e950-34b2-86a7-ecddec20fdc4 | 1.6203 | -55.726 | 2025-10-27 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1606c1f6-d384-3354-a2b7-75600439626e | -6.5603 | -41.6099 | 2025-10-27 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 343.2 |
| 41af2cbf-f9f2-300f-9518-c3b7e3aadb82 | -3.0148 | -41.6851 | 2025-10-27 14:20:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 148.8 |
| 13800c91-22a8-3538-afb5-a5c2a840514d | -7.8411 | -46.4646 | 2025-10-27 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b580cb53-fb0b-3364-b9fa-e1a111304852 | -6.5605 | -41.5859 | 2025-10-27 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 458.6 |
| 8b637841-ebf8-3457-a8d5-0dba1bbcbfd9 | -6.1735 | -42.6221 | 2025-10-27 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 8e2c9bb7-4563-3f50-901e-49d648065391 | -7.0835 | -45.3865 | 2025-10-27 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| c2a7c89b-f055-3e0a-9da4-e3fc7cfe7096 | -4.3877 | -43.3362 | 2025-10-27 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 21fa2368-bbc0-3523-b4c6-3a46a6bdc2cf | -4.4618 | -43.4248 | 2025-10-27 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 03925160-d6de-35cc-a277-b7767d6e5dbb | -7.0883 | -44.9319 | 2025-10-27 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 869f0c0b-137e-3a01-960f-42d0a3c60fb1 | -7.9252 | -45.6937 | 2025-10-27 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b2bb6027-d645-31f4-bc56-c59f149a2b72 | -7.2379 | -44.9868 | 2025-10-27 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| a0a271f9-01e9-321a-892c-37b9199faad2 | -3.4217 | -42.4739 | 2025-10-27 14:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 83.9 |
| bb232030-457a-3d8b-8873-1f2fa943a070 | -8.2873 | -46.868 | 2025-10-27 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ac9989be-d2c3-3150-b33a-fe3fb4d3292d | -6.5864 | -42.6804 | 2025-10-27 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 2c64fd3d-5426-333a-ac1f-4bd67210d90f | -4.8951 | -43.001 | 2025-10-27 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 64929555-6bf5-3db2-99f1-6618f2f76f32 | -8.0608 | -46.9558 | 2025-10-27 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 8991c749-2e99-3e69-a43e-e02ea75b79ed | -3.3261 | -42.8778 | 2025-10-27 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| e356bdd6-5304-33c0-aaa5-dfa89b5c3df6 | -8.2685 | -46.8698 | 2025-10-27 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| bd90a0b6-48e7-366f-8bbd-e1c2b5f52a94 | -4.9138 | -42.9998 | 2025-10-27 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 7342a054-b437-387b-a0d4-a7b6d82aee03 | -8.0444 | -45.1606 | 2025-10-27 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| c0ef1631-9ad1-39d6-b731-376827f3bca0 | -2.9961 | -41.6859 | 2025-10-27 14:20:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 1ca2a93d-d4cb-3f6b-a646-80eb9bcc5f49 | -5.6431 | -41.1114 | 2025-10-27 14:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 264.3 |
| a0552081-d835-3220-bc5c-5328159f1d90 | -6.4314 | -43.1177 | 2025-10-27 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d1b58b9c-d1f8-3f85-a95d-0d2088ae0f77 | -4.8953 | -42.9776 | 2025-10-27 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1bbd17bc-e524-3be1-9f4c-94f5b5237707 | -3.3448 | -42.877 | 2025-10-27 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 464cd547-458d-379d-94ee-f838bc3e00ec | -3.6253 | -42.7933 | 2025-10-27 14:20:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 36dc93d4-107e-37c8-b455-09dfbc674c31 | -4.4066 | -43.3118 | 2025-10-27 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 96a7b1c1-329d-3f54-a476-a14bfdb81fb3 | -6.2306 | -42.5463 | 2025-10-27 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| fc601aa4-8b4a-32ed-b6dd-a33302fae4f4 | -14.2487 | -48.1372 | 2025-10-27 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c535914b-987d-3763-acbf-00e4650d059e | -7.8408 | -46.487 | 2025-10-27 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ac36ae66-5ff7-3706-947f-d1e327d2f7cc | -18.3199 | -42.1385 | 2025-10-27 14:20:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 164.0 |
| cc6841cf-fb83-365c-8738-260ae665e625 | -9.2619 | -45.8258 | 2025-10-27 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 38e226d2-2e3a-33bd-b6d3-2cb1d7972dcb | -4.4602 | -43.6569 | 2025-10-27 14:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 016bf30f-5776-3dee-a7af-71c719675548 | -6.1737 | -42.5985 | 2025-10-27 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 34a5f6e5-fc5d-3d11-b69a-51f8f13b4891 | -7.5242 | -46.27 | 2025-10-27 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 271383d4-196c-3c69-a181-d1bf456ce324 | -4.914 | -42.9764 | 2025-10-27 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 55afe85b-9218-32a6-8d5a-fb4aeb4c141d | -6.2304 | -42.57 | 2025-10-27 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| bfabf5cd-78cc-35f8-824f-9316a6d790c5 | -7.6673 | -46.9028 | 2025-10-27 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8a79b984-4cf8-3f88-b754-394a5ecc188d | -6.4615 | -45.7536 | 2025-10-27 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 71b90cc0-b7ac-3e49-b4dc-4a7207af138d | -8.6526 | -44.7771 | 2025-10-27 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 174882cf-7270-3d80-83a8-f95e0872b4d3 | -7.8157 | -45.4102 | 2025-10-27 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| be2f9812-0d97-32c9-8c9b-783325a2b48a | -4.4665 | -45.4589 | 2025-10-27 14:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a372f436-fa29-3e33-9a73-afad4232809f | -4.2035 | -42.95 | 2025-10-27 14:20:00 | GOES-19 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |


[Clique aqui para ver as próximas entradas](README78.md)
