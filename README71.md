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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 633c27c9-af85-352a-ad7e-0b31ba84224d | -5.10269 | -45.21486 | 2024-10-06 04:19:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f187a49-a09f-3e85-8353-0b88cdc902ca | -5.07827 | -45.17519 | 2024-10-06 04:19:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebda8c0d-53ae-39d9-af4f-6d94aa4e8eb5 | -5.05166 | -45.12806 | 2024-10-06 04:19:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51ecc237-4a3b-3943-a650-1659f4aeef81 | -5.04834 | -45.12752 | 2024-10-06 04:19:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8408616-eecc-3419-9e9f-0b02cf9cef82 | -5.04779 | -45.131 | 2024-10-06 04:19:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 634ca4e7-0e68-3fa9-91c4-01391f6dbd0f | -5.04776 | -45.19546 | 2024-10-06 04:19:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92534a85-98b2-3ece-93fe-3879463fee5d | -5.04444 | -45.19493 | 2024-10-06 04:19:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d14cc8a2-ba2e-3d79-96d4-f67b427279cd | -4.95424 | -45.51004 | 2024-10-06 04:19:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc39813e-0229-370b-bde8-6b5e55e136fb | -4.95368 | -45.51358 | 2024-10-06 04:19:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc2604d3-1fac-3988-8a70-fa878e32605d | -4.87661 | -45.35612 | 2024-10-06 04:19:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4e2c7ff-5235-3f47-98e5-11de5ea340d1 | -3.9059 | -44.57422 | 2024-10-06 04:19:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b433e2b2-021e-39a9-86a8-0d533b2baa4f | -5.08918 | -46.11883 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 934247d8-d9e2-3478-9d57-63951a9f8a1b | -5.0387 | -45.79382 | 2024-10-06 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 711e24ba-a00a-3bd7-9fa6-661de69cfeb0 | -5.18272 | -45.24574 | 2024-10-06 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d05d7fd2-29b2-339d-87c8-35ad54fce6e1 | -9.35509 | -46.55057 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 188b3a46-2264-3c99-a711-d77057f5b51e | -9.35174 | -46.55002 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79eaec54-a8aa-31c7-a1d9-431cbe4918e8 | -9.35116 | -46.5536 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b313c6b1-b910-3976-a23d-14d15cbac8c4 | -9.35059 | -46.55719 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29ee7093-c50e-32be-aa92-bcbe82f3ef59 | -9.35001 | -46.56078 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f7d0624-a766-3423-8970-fa33a6890435 | -9.34896 | -46.54588 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| e82219f9-cce4-3018-836b-4ec77457ee04 | -9.34781 | -46.55305 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 204e334c-e2f5-3f68-aadc-a37b33e284ec | -9.34723 | -46.55664 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50796ebc-0879-303c-9ec2-66019a7a6f56 | -9.34666 | -46.56023 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c615e7a6-6ab8-3f33-9dca-6508d224ab58 | -9.34561 | -46.54531 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 5224f6a9-dfcf-328b-8834-eb90cf17c2ed | -9.34503 | -46.54891 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ba322ccc-abb2-38c1-bb10-1db863a6b6f4 | -9.34445 | -46.5525 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 281b6947-3eb6-3478-92ab-af6f224476f5 | -9.34388 | -46.5561 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b8811c61-3c72-3f65-8c81-2b35be76da76 | -9.34331 | -46.55968 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b59c89d9-279d-3eef-bf81-d374135b9836 | -9.34225 | -46.54476 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ebefd92-bbc1-3bd3-a280-ea1f04cdb468 | -9.34216 | -46.56686 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 971bbbd3-0d9e-396c-a9ab-3860a00fe25e | -9.34168 | -46.54836 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0323ed0f-432e-333a-b3a8-ab88f0dfdaa5 | -13.61016 | -48.13907 | 2024-10-06 04:19:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e21b6a78-a53d-3627-b671-77620dca9d8f | -9.3411 | -46.55195 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c4fb31b-ca0b-3ed4-8f92-d341eaa450e4 | -9.34053 | -46.55554 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 589d2b9d-eeb1-31c0-8c86-97bc394e95bb | -9.33995 | -46.55912 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85f662a0-96d3-3049-8616-60e066398061 | -9.33938 | -46.56272 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1e2f548-f5b5-35c0-a893-b0d4a4bdea44 | -9.3389 | -46.5442 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5903426a-4bb0-3941-ac9d-81314035053f | -9.3388 | -46.5663 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faf3841f-e83b-3c22-8f0a-f22255cf5631 | -9.33833 | -46.54779 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1caeb2f2-6d7d-3abc-b21b-e83b61b6b58b | -9.33775 | -46.55139 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04f0d8bd-6a07-34b7-92d1-8036f7fd71d9 | -9.33718 | -46.55498 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3084747-97e4-39f9-8852-cdbc7baf9d1b | -9.3366 | -46.55857 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d1bdbe4-378b-3a8d-be5e-e0b5af93720f | -9.33603 | -46.56216 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a73bdd88-856e-3ea5-9d72-d3dc128fce33 | -9.33555 | -46.54365 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4aa44c4e-3c38-392b-a179-bf2cf1ef6e30 | -9.33498 | -46.54724 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9777adfe-6456-36f9-84f0-8349a119ffd2 | -9.3344 | -46.55083 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4aac0675-950c-30fb-8629-5e6b333835e2 | -9.33325 | -46.55801 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfca0961-53a3-33ee-9bc3-6ce58b5d87d7 | -9.33267 | -46.5616 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb3a35e3-ab4a-3c5e-b58f-c829070d082f | -9.3322 | -46.54311 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f1f1c971-0bfc-3a27-aa8f-ccb51629439c | -9.3321 | -46.56519 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b965715-6124-3ad9-8b70-e914eaaf6e4c | -9.33162 | -46.54668 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 25bd18c3-baa4-3c82-848c-77843ccfa831 | -9.33105 | -46.55028 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0baad7da-cc66-3a79-a4c4-08031726ff51 | -9.33047 | -46.55387 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51d4b03c-6f52-3a23-a87e-7c5c3f2810b4 | -9.32989 | -46.55746 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94c1985c-75d1-3bf6-a8cf-02e8bf6499f4 | -9.32885 | -46.54255 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35d3514a-e55a-3c50-af35-b88e3fe37efa | -9.32827 | -46.54613 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8807705-5616-385f-97bd-6352ab093b47 | -9.32769 | -46.54973 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5a53669-3ca0-3506-ac7e-1ef68125afcb | -9.32712 | -46.55332 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e626db3-7e03-3ad6-86c2-f7ce5bef157f | -9.32654 | -46.55691 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57c10367-9fa3-3660-85d5-fa86734b2f3c | -9.32492 | -46.54559 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f47d7d8-8bc2-35e6-90c7-bb52c1df9a88 | -9.32434 | -46.54918 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7eff663-896a-3fab-9e35-211b6d1d9f2e | -9.32156 | -46.54504 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acc5688a-89e9-37ca-a0f0-1ebe82e9a396 | -9.04411 | -46.59587 | 2024-10-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9de34985-87db-314c-99aa-00b1595f8d26 | -9.3546 | -46.5321 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b3b4804-095c-3052-b965-e7f48068f386 | -9.35403 | -46.53568 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0687781-f8ca-3ba6-bacd-3f4d6bbf9f75 | -9.35125 | -46.53155 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2b19380-381f-3a96-9fb3-20580e6b0ee5 | -9.35068 | -46.53513 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b33025d9-53ea-33d3-a94c-d50fbdd8c3ef | -9.3501 | -46.5387 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 302d65a8-9998-3feb-8cb7-8998654a1e21 | -9.3479 | -46.531 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28596f5d-c974-310f-a642-eea251897969 | -9.34733 | -46.53457 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b75bcbc3-b119-3429-bb6e-188d3d431337 | -9.34675 | -46.53814 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9afe3cb0-d93f-3af2-8564-30ffb943764a | -9.34618 | -46.54173 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67c0ec7b-7fa7-3670-ad1f-5af0be2aa1fa | -9.34455 | -46.53045 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31b47c2b-b78e-3890-8508-e3901b9e36d7 | -9.34398 | -46.53402 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f83b9179-3448-33d0-b7e1-af7485a348c8 | -9.3434 | -46.53759 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1831c388-b5bd-3b3e-9c70-15ba43dca818 | -9.34283 | -46.54117 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| caf3ab08-d2a8-3ef0-a0f7-9411cefe0399 | -9.34062 | -46.53347 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9118719a-471a-39df-9178-660a6ed45c94 | -9.34005 | -46.53704 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5c71e394-2773-387c-83a8-95f6fee3f941 | -9.33948 | -46.54062 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 46fe8a1f-6a3f-3ca0-9877-b1428e1f0ca3 | -9.33727 | -46.53292 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f8ba062-6597-3c62-850a-0dda0d49f464 | -9.33613 | -46.54007 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fa1614c1-1b55-3bd0-8e03-3132805043d5 | -9.3345 | -46.52878 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c0c4c6e-cb5e-30ad-b71c-e990de9c8a79 | -9.33392 | -46.53236 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eccab0d6-8233-3633-9e78-42e5f6ca490a | -9.33335 | -46.53594 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 89c88b5c-a911-38d1-b247-48084ca8ffd8 | -9.33277 | -46.53952 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b767ff8d-5609-37f0-9887-eeeafb24b92b | -9.32942 | -46.53897 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d820aaf3-9f7b-33a5-b393-7128fc702c4b | -9.32607 | -46.53843 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e55aec45-2109-3219-93ed-042ed4942e8b | -9.32329 | -46.53431 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b5e72bd-93a2-35ca-8a9f-9f800dcd306f | -9.52945 | -46.49803 | 2024-10-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a7fbb0f7-761a-3c4d-a0a6-864bb917a8d1 | -11.46984 | -46.86137 | 2024-10-06 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f39ae49-6405-3dcc-a466-7eb115981583 | -11.46927 | -46.86495 | 2024-10-06 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fc36e93-4d35-3866-8196-f870ca31e472 | -11.36582 | -47.24949 | 2024-10-06 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18d540d4-655e-39dd-9c1b-00124d77af06 | -11.27983 | -46.79694 | 2024-10-06 04:19:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e935db4-fdba-3815-901a-ecc2be2c8b65 | -11.72766 | -47.71932 | 2024-10-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7090eb1c-2205-35f8-a4d4-04ef73268270 | -11.72424 | -47.71881 | 2024-10-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de70af5d-b6e5-31f2-853a-e0e1f21c29ec | -11.71397 | -47.71732 | 2024-10-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b55c5f7c-e794-3669-b363-82d55543da08 | -11.71118 | -47.71296 | 2024-10-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34fe2a96-6dcc-32e0-9530-c0750327387f | -11.68174 | -47.67717 | 2024-10-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac8d8183-64a2-3d46-bfdf-497898332f23 | -12.45356 | -47.52695 | 2024-10-06 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71329dd4-7834-3ca9-a296-90c1a04e65ea | -12.45297 | -47.53061 | 2024-10-06 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README72.md)
