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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f32e9dc-2ed0-3184-9d8e-cab5f114a89c | -4.16167 | -45.09647 | 2024-11-01 04:29:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b10ffa6-3e03-3958-b527-50727deaaca0 | -4.08893 | -45.66025 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03588195-958f-3e93-9738-934c2f844b4f | -4.08554 | -45.65973 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9f7874e-52eb-350c-96f5-1fa9ab29fbb6 | -4.07552 | -45.81395 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7bfc2f1-d4cf-3e60-8e15-41018b742600 | -4.04833 | -46.07729 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4b5d1af4-4cf2-3545-ad10-2efbdcb34b95 | -4.04552 | -46.07327 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0d2b0b0b-5d4f-3c59-a973-eebe44727e82 | -4.04497 | -46.07678 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 087260ca-fae8-30f8-a87a-7d53c95cb36a | -4.01851 | -44.82382 | 2024-11-01 04:29:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb56399b-97c0-367a-a2ea-eff100c98894 | -4.01791 | -44.82771 | 2024-11-01 04:29:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70650a7e-99a3-30b5-9226-1dddd07c0bc0 | -3.97874 | -45.30824 | 2024-11-01 04:29:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0556d80-3a1b-391d-9824-071170943352 | -3.9564 | -45.81399 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c40ad0d-d706-30e2-b6dc-135fb35c056d | -3.90304 | -44.93704 | 2024-11-01 04:29:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21448bdf-8e7d-3c89-83ec-a46b1e01a972 | -3.89668 | -44.93214 | 2024-11-01 04:29:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca31eaf7-9fa5-384a-9ead-081083f4fcb2 | -3.71539 | -46.01093 | 2024-11-01 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 39afcbb7-f98e-3555-869d-0cbdc49c2716 | -3.71204 | -46.01041 | 2024-11-01 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c1112be-9c40-3064-9f9c-3cf0fb1ae4f0 | -4.94538 | -45.62734 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 280d60d7-a996-3b4d-80cc-8e510d5693fe | -4.94197 | -45.62677 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82106d70-21e8-3a8e-88c8-afc165bebf91 | -4.93973 | -45.70968 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba61d4dc-19d6-3957-88f4-c9a391b057cb | -4.93746 | -45.70178 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac0ef944-9031-371f-816b-ab63f5944291 | -4.93405 | -45.70129 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 034c9d13-d662-39a2-bfea-b70037d363cd | -4.86755 | -45.76646 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f79974f-2661-31b7-af0a-2e76c287ed98 | -4.86698 | -45.77014 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a194a66-7113-310f-a287-da929461dc79 | -4.8273 | -45.68872 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60c689c2-0548-381c-9573-137c9c86b39e | -4.80967 | -45.66713 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d754a4e-53d3-34c5-acfc-47963cbc4c44 | -4.8091 | -45.67085 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd3ac0f4-f6ab-3e5d-ab59-1b5126e454df | -4.80854 | -45.67456 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 267e1a8e-e60d-3c9e-8cc5-9b09c925fca6 | -4.79444 | -45.7441 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 487e01c7-1369-3759-b71a-61c06be7813f | -4.79366 | -45.74498 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79056b02-d440-3a65-946b-316f1c9ce480 | -4.76704 | -45.84874 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c88330d-f142-36ab-ac5a-5b86b78675c3 | -4.75238 | -45.35429 | 2024-11-01 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4345fdeb-9dd9-3725-a6e3-aeddab872a48 | -4.73367 | -45.75044 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10d090c1-5722-325a-bb61-4947e8a5fe8a | -4.73303 | -45.68684 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7490991d-0e6a-33e2-9a7c-a8bf1c014214 | -4.73247 | -45.69053 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36d9d458-392a-3650-a308-bf5b85e1c6d9 | -4.73083 | -45.74631 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 910edf5c-8ae5-3576-b1b8-45ec2dedfc95 | -4.73027 | -45.74994 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ce4d143-9110-380e-94ff-ca62adee84c7 | -4.73002 | -45.16061 | 2024-11-01 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bd4dabf-d4d9-30e9-8bc3-34fc3b2bae75 | -4.72971 | -45.75355 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac9c64ac-ad49-3fa6-a33b-30e030cb1862 | -4.72906 | -45.69002 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73f79748-11de-397e-a6fa-230bf99bd8b0 | -4.72743 | -45.74577 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c491ff59-33a6-3136-9c73-0e64977a51cd | -4.72687 | -45.74939 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 140a5f26-8921-3bb6-949d-689cd99995b8 | -4.72404 | -45.74518 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d47065e8-6816-3e7d-bbb9-0b2b46b0aa5b | -4.68564 | -45.81422 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01f51501-bb7c-3eac-87dc-6e4e5d0d91a9 | -4.68225 | -45.81371 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4a5514c-6cea-3051-9674-e5c964008cb5 | -4.63821 | -45.36754 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 194829b9-b58d-318e-a0e9-d029e9c185bf | -4.62969 | -45.62943 | 2024-11-01 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3ea7ebf-bcea-3d75-b036-2beb8f5acd23 | -4.54236 | -45.71767 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f918dd5e-e3ab-3449-9c94-65d2a42571fc | -4.53952 | -45.71354 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 77eaff9f-37df-3586-ad2e-4b7e428caeed | -4.53896 | -45.71719 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc751893-2e7a-31f3-a515-3f40571a833e | -4.53612 | -45.71305 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aced87ee-1ada-36e8-922b-81b6d00630da | -4.50579 | -46.04148 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3936655e-4a18-3345-965d-83e9590a992c | -4.49249 | -45.68016 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc79764e-da29-33b3-8406-ca9779ab95db | -4.4692 | -45.07452 | 2024-11-01 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49d3db0c-d505-3f30-9186-8640c50fa786 | -4.39499 | -45.81021 | 2024-11-01 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a243b703-18c6-3aaf-a896-47e26d317fbf | -4.37718 | -46.0141 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cf34879-ee4e-3c24-a8db-b05bfb82150d | -4.36989 | -46.01669 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7a2407a1-2d84-3ab8-ac70-547e80e53228 | -4.36653 | -46.01621 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 33a37f51-0064-372b-b5aa-1da289d704b1 | -5.66439 | -45.20555 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8f7f1c0-3b76-3134-bdcb-60ca3b4dc8a1 | -5.62776 | -45.27174 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a11989bc-3661-3e9a-96be-bbd2d9c021d2 | -5.62716 | -45.27562 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ff142ef-8aa2-361e-ab80-0c47f13fc36c | -5.62535 | -45.27488 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 998c6ede-ee57-3a16-8fa5-0bfedb67dbbf | -5.59485 | -45.20731 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e7b209e-8fc5-3529-98b5-8227f00863cb | -5.59426 | -45.21119 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e674c20-e3f0-32c2-8dea-c0068fea4cab | -5.59135 | -45.20679 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28df8a11-1387-3738-a003-b372164b48ab | -5.59076 | -45.21067 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dd77b62-00aa-34b5-9518-128ebdfa21d5 | -5.33537 | -45.11006 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65928164-0fba-33bc-a5fb-172dad68ff60 | -5.33478 | -45.11398 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e97212d-29b4-353b-bc6b-d6d3c4bb52a5 | -5.33188 | -45.1095 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7e12675-d426-3190-b0b2-37ec818a4673 | -5.3254 | -45.15245 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58c3ceb0-a809-350f-8a8c-fd0491105f3a | -5.28687 | -45.13948 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0a560a5-a5e9-3e13-af76-bcf62e8705ba | -5.2671 | -45.1285 | 2024-11-01 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 763ea12f-499e-32a5-984b-61c17b44b3a9 | -6.35141 | -46.11659 | 2024-11-01 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 584fa2dd-e7d2-380e-a715-5004ddfd98f7 | -6.05365 | -45.80022 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 519bf577-bf3e-3dc4-93c3-649b73b90d5d | -6.05307 | -45.80397 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ec0364e-3aa6-3c46-9d68-c7568b0647c3 | -6.04851 | -45.81086 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abab6f14-0e33-3e3e-bdc2-3a1ea01f9817 | -6.04793 | -45.81458 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f596a7aa-a0a1-3251-a6ce-0e81eb4e2976 | -6.30436 | -46.06051 | 2024-11-01 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 270625d3-ee76-3986-80dd-6a387ddbff2d | -6.29638 | -46.04434 | 2024-11-01 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4877f43e-4f78-32a4-931d-1340ec499d49 | -6.05423 | -45.79648 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cc4dcb6-4a57-3e69-8e00-926c1d26daa9 | -6.05135 | -45.81513 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecb8acf8-d195-3ac9-b025-4670bbee5655 | -6.05023 | -45.79967 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28478691-6022-32ef-b6a0-ea868b5c53c0 | -6.04965 | -45.80341 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1898bf4d-e914-34a1-84ad-311483a4519f | -6.04908 | -45.80713 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54112caa-f755-321c-89cf-2d2843882065 | -6.04623 | -45.80286 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c616b58-e021-3da1-8c5e-d61f1fbc5941 | -5.83895 | -46.24004 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c499fb17-4a2a-34a7-8dc3-80eba4fb35fa | -5.83765 | -46.4491 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3be1ff39-04a1-3794-9619-87e54efa2168 | -5.68589 | -46.30563 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 290bc246-8ba9-3186-92b4-d7b2300d26ae | -5.68402 | -46.30522 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5bcfc09-ae3e-3d54-b53d-31307cb1ab32 | -5.67677 | -46.32964 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db162f6e-3e10-3a4a-a68b-ce40219ad28c | -5.59965 | -46.18162 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 851e6d7f-1b2f-3111-8606-7db48df9f545 | -5.59964 | -46.40558 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83b6422b-6929-36a4-bd41-98ad020ad8cc | -5.5991 | -46.1852 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c7fec93-72d1-3a18-bd4a-14571c266659 | -5.55565 | -45.85075 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be8317df-9f0e-3687-8cbe-38b275c58682 | -5.55224 | -45.85023 | 2024-11-01 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 369f2300-b518-3880-aa17-0a4f914842cf | -5.42372 | -46.36031 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99d16cc0-0f27-3e03-b00b-3935ec927975 | -5.42316 | -46.36388 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ccc0046-e6fd-31fd-8d01-64bc624de307 | -5.23972 | -46.16808 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4428415c-53d7-3ee3-822b-b9c6167ad388 | -5.21838 | -46.15007 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9e6608f-5a14-3d15-85aa-9a969f0cecce | -5.21312 | -46.02748 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f25c47a-11f3-33d5-b411-3627545627d9 | -5.19033 | -46.15308 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64f88940-3613-3174-a988-0aeebaf7c67e | -5.18696 | -46.15253 | 2024-11-01 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
