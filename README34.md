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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6a622d9-177f-3a10-8451-d51f4014424b | -15.83473 | -59.59649 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db4831b1-531d-36ce-9fe6-e98d5b72462b | -3.49843 | -59.05511 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b26a707-0a42-3c1c-88f0-1fe3f427db2c | -15.77431 | -59.46861 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef23e408-f156-350e-b56a-327ccc8e08cb | -15.8067 | -59.48457 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 948bbae6-2f56-33e6-a6ff-42346105c4cd | -4.79826 | -47.27768 | 2025-09-25 05:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f05d35a1-7d74-36a0-b021-3592adc64c10 | -3.36423 | -59.49821 | 2025-09-25 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28120928-2a7f-33a8-889a-8cf6743f7526 | -3.82953 | -50.97238 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5803f07e-aa60-398c-a27e-37749829deab | -15.25413 | -59.43818 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1381120e-1242-3dc5-9c87-52ebc9d3b041 | -15.77238 | -59.46714 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7455b37-58ca-3f94-8e45-c838c1c1cb22 | -15.7953 | -59.48716 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 702b145f-9fff-3ca3-bda5-b9c72e7ff3e7 | -15.76594 | -59.47561 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 830fee59-ba57-3ba9-b63f-f2cf71410e8b | -15.88521 | -59.34854 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 233f5aff-49dd-3469-bd3a-acebe09e89cd | -3.08328 | -52.92168 | 2025-09-25 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25e6cf6d-6935-3192-ae07-1e4021e29306 | -2.44808 | -57.94244 | 2025-09-25 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1118e76e-3844-31db-8ff8-48c9634e50b8 | -2.95336 | -54.80225 | 2025-09-25 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70a4d6a3-9b9f-3dfa-9b72-99b4191f34dd | -4.7962 | -47.27497 | 2025-09-25 05:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 102a3b46-9a70-3648-81ba-7387b4e817a3 | -3.61341 | -51.79808 | 2025-09-25 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df1ec95c-5324-3fae-8363-72a11ac9188e | -15.26187 | -59.43535 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecc1d785-812d-3abd-8adb-f3cc00fdfd13 | -15.76594 | -59.50101 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6cfc1a71-5f6c-3c4e-9a30-9c21d444e5c4 | -3.90909 | -54.5607 | 2025-09-25 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae32d1a6-fe1b-39a2-8a19-41dc0954fc0d | -15.89309 | -59.3453 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2716010f-065d-3444-aeb4-477c733adde2 | -4.28904 | -48.26418 | 2025-09-25 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6358a684-df92-3c02-af7e-f8807ce5baf0 | -3.81829 | -50.97768 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6955edb-93e8-303c-ab83-64aa24382626 | -15.88583 | -59.34418 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| def48214-5078-3c57-a648-801069e37d91 | -3.74083 | -53.80849 | 2025-09-25 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf2dd06e-1b8b-3d8b-90b0-989f5282d1b1 | -2.45148 | -57.94292 | 2025-09-25 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 950eceb0-c815-342c-9bf3-80b9495a53fa | -15.26964 | -59.43222 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f169286-27f7-3c56-bcbd-d622e11ed5be | -15.28822 | -59.43058 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bfa70bd-03dc-339a-b4f9-aee112c167a2 | -3.83027 | -50.96963 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 980b79ab-a9d6-3944-9390-b17041c48893 | -15.76953 | -59.5016 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 36e21d7c-4a8c-381b-93d7-44b619c0557f | -3.38148 | -52.71443 | 2025-09-25 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b5c8fc7-bdca-36b6-8742-90c74971bd4b | -15.26546 | -59.4359 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53689e7a-5eeb-3ab1-b76c-12f85dde9baf | -3.75146 | -59.26143 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed01ef69-10ca-333b-a95c-ea73e1f9a44b | -3.76357 | -59.31307 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebc5e5f9-2512-3099-9a24-2915d3d2183e | -16.85614 | -50.51757 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b2b2927e-1148-3f73-8bb0-9754e27c58b0 | -15.77598 | -59.46769 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f854b308-f18a-39d0-bcca-449f758f873c | -15.35771 | -59.17783 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93fd3319-7cde-3358-9c00-96e377247672 | -3.75201 | -59.25796 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 658906db-7997-3764-b277-c54dc1675a62 | -15.29183 | -59.43096 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0419068-76b4-3a62-84cb-b3916bd2374b | -16.85512 | -50.51517 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 467886b5-bae8-383a-9a99-4e9b82c90d43 | -5.96224 | -47.30393 | 2025-09-25 05:23:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed2f0cdb-2e5e-3820-809f-4abf02e45d50 | -16.84871 | -50.5142 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a67098f-99ec-38a6-8093-68d522dfe202 | -3.8286 | -50.97884 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ddf430fb-0e56-307a-aee3-eaf98af2b2a6 | -15.77015 | -59.49735 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 27289416-5e13-3818-a553-cd37ed862040 | -4.08183 | -54.30567 | 2025-09-25 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d383dbd-7287-3f42-a549-da0003653c07 | -3.81877 | -50.97448 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1075b63f-8678-3106-95d0-53ea0115a9cb | -15.76776 | -59.50004 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7a38914e-b332-30b6-8b3b-bb41755a79df | -15.76957 | -59.47598 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38cd49b5-baaa-36dc-9ac9-dac26f7d983d | -15.77128 | -59.47494 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a8987b-597c-3928-aa94-62ea4ebc11df | -15.27683 | -59.43321 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29b4aac6-62f6-3272-9f34-1750efc01fae | -15.34983 | -59.18102 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25048866-8d12-3d0a-ac32-45fa0bc8f06e | -3.82999 | -50.96915 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e799a6ec-dbb7-311e-a223-989c8f9347e0 | -15.36259 | -59.16979 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b55ed444-0c65-31bf-b6cd-d30d1c0ea7cf | -15.76655 | -59.49682 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aa203b7-b14d-317a-81b0-efa2228999d3 | -15.83412 | -59.6007 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f15d656-742c-38c3-9919-23b81d9dd663 | -3.21319 | -60.60624 | 2025-09-25 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1b672df-f84b-3d0c-a78c-ddeef12206d7 | -3.82355 | -50.97849 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b52059a7-4384-3691-9be2-14f846c5af8d | -3.20695 | -54.9601 | 2025-09-25 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5f2a9b19-587a-39cb-9dee-13d4fc264b71 | -2.44468 | -57.94193 | 2025-09-25 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4506ce95-d296-36e6-969c-898232dca90c | -15.76717 | -59.50424 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4eac4ea7-33f8-39b8-991b-508f47dfae73 | -8.23443 | -61.16091 | 2025-09-25 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54c66732-88e9-373a-94cc-23a6bb1f9228 | -3.92974 | -59.87647 | 2025-09-25 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cafa1e4-5d2d-312a-8e76-4bdcd8b24c8e | -3.739 | -53.8096 | 2025-09-25 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45d27100-2f34-3639-aa85-8f332e1dff76 | -15.81091 | -59.48083 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4a87513-f006-31e0-b98f-88a270ab796e | -3.8293 | -50.97605 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f67646f7-2bf9-34eb-ab70-d6e5c17fef53 | -16.85567 | -50.50972 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 49b25e6e-ff35-308c-8b8d-3f996df53e4a | -3.82452 | -50.97203 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16c886f4-1d21-3ba1-92fe-81a97b3abd1b | -15.79949 | -59.48352 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 75e31fb6-c6ab-3565-abae-741b761f2dc6 | -2.70527 | -54.65128 | 2025-09-25 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ca5aaa0-8348-3703-92ec-bbbd69a4756a | -15.75696 | -59.48685 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| daa71ebc-de8a-33f5-be48-7157aaa0f3f6 | -15.3546 | -59.19952 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b7acfb9-35cd-38e3-bd66-57e4437edb2e | -15.83054 | -59.60015 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b44677c-184a-3db7-b2e0-3e8393d7f439 | -15.82993 | -59.60435 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea1efcdb-ff24-33db-8a4b-e9a08df71c24 | -15.27324 | -59.43274 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59635e5b-aba7-375b-9f86-6443e48d9f83 | -4.24582 | -53.55271 | 2025-09-25 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61df91e5-14e9-30ac-b198-f8eb2c7ac04d | -15.8061 | -59.4888 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b212afb-4a46-3141-8715-e21e11bf4b1e | -15.36499 | -59.17895 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 551e343c-3d8e-315f-8c62-cefdeeb904aa | -3.82404 | -50.97526 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ad1fb2b-3a95-320d-94d3-e05acd21c530 | -15.75814 | -59.47867 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 31c8416a-fb27-3061-b566-51853c405561 | -15.75395 | -59.48224 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c6d0a08-3228-3b5b-b539-ba1837dfcf39 | -15.77071 | -59.47897 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a647e3c-3275-391e-bf1f-82effa1ca1c8 | -15.76231 | -59.47524 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 28ac8580-e8f5-3551-b543-a300cfcbc4f9 | -15.85331 | -58.1312 | 2025-09-25 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5d3c0cb1-b9a1-39b4-9b57-fcb620beb833 | -2.71005 | -54.95426 | 2025-09-25 05:23:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 437989e5-95f7-326e-89ae-e2cc0575d9a6 | -15.77184 | -59.47097 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46bc35db-3a8a-3243-a961-05ee8f2af0a3 | -15.8073 | -59.48037 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd8c8472-7332-3912-aaca-4db1268c7147 | -4.02749 | -47.77584 | 2025-09-25 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 54d015df-a9a1-36e4-856b-a1f3c3c9dd8d | -15.88185 | -59.42299 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee5c08c6-01bf-3338-b8bf-debebab590ba | -15.35045 | -59.17664 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64f6b03f-3d06-3d50-95b4-1fabeff23581 | -15.88693 | -59.38795 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2204998f-6250-39de-bbb3-ef3525129960 | -15.77015 | -59.47197 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7a54a5b-95c2-36dc-959f-c14ef4243d94 | -3.83077 | -50.96636 | 2025-09-25 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7c0faa1-ea99-30cd-adfb-39e32b65dc25 | -15.76234 | -59.50044 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b3f914c-b599-3dea-b375-4f7a9eb611ac | -15.24642 | -59.44086 | 2025-09-25 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 231a084e-f9fe-30cc-969d-adac8d278f39 | -16.85023 | -50.51125 | 2025-09-25 05:23:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f7e26b91-6084-3cc0-9694-3b6d6e2c0622 | -15.25356 | -59.44219 | 2025-09-25 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c7bb9b5-e018-3045-9072-56b7b8c4b8fc | -15.35522 | -59.19515 | 2025-09-25 05:23:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4176bc0e-585b-394c-ad2e-923ee9e74428 | -3.14715 | -58.97915 | 2025-09-25 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f508009-dfd0-3646-9043-20ea86941910 | -15.81452 | -59.48136 | 2025-09-25 05:23:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e88686ec-1108-3c00-911d-5f027c55dd23 | -15.85393 | -58.13317 | 2025-09-25 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |


[Clique aqui para ver as próximas entradas](README35.md)
