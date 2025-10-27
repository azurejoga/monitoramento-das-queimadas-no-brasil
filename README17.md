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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82ec7df1-32f4-3ca7-9c06-c3e8ca1ed8c8 | -4.83545 | -45.33859 | 2025-10-27 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c3f9f3a-d81b-34cd-8802-f27e8d15501c | -4.44806 | -43.42313 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 864d23b9-d1f4-3da0-b570-cb1eebdba55e | -5.44571 | -37.87433 | 2025-10-27 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 578f1fbc-ac87-31dd-869c-94e8cc33ddf4 | -4.44072 | -43.43504 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1edada94-86e7-33aa-bea8-fc0fd05b5c8c | -6.00105 | -36.06497 | 2025-10-27 03:40:00 | NOAA-20 | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0d6b29e9-02a2-3ded-910d-d2f7bd4c7f0a | -6.16465 | -41.57703 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bff44a0a-b19a-3cf4-8344-a7e699dda653 | -6.16543 | -41.57234 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cd88acd-14eb-319f-8cb3-5816f2cd20c8 | -4.4787 | -43.4352 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c39612ce-250f-32ae-b828-94e629b34cb8 | -4.46881 | -43.43037 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 612c9680-e81c-3b01-870c-edb068106273 | -4.4522 | -43.43048 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd6e087e-402b-35c0-9bec-be15e16df33c | -6.1393 | -41.81916 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 33936474-65f2-3ee7-82a4-a3b7b5ffa467 | -5.85624 | -39.47596 | 2025-10-27 03:40:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17935ed6-f1ae-3cc8-9cd3-87ed6cac7fa1 | -4.38407 | -43.32774 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 428ea3ea-0e7d-3514-bfa7-ae5076313368 | -4.24942 | -40.68901 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a3931ba3-4808-39ba-b38a-75851f20cd6b | -4.42697 | -45.98553 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b561dc0b-89a6-31ec-bb5d-d90fe1c938b9 | -4.82818 | -45.34561 | 2025-10-27 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdc5228b-1d51-3b18-86ed-1ab50e70787c | -4.26068 | -40.70174 | 2025-10-27 03:40:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 90652079-33fa-3503-b778-fed0b8e634f0 | -4.95797 | -44.88056 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d06dbd19-05ea-3c2e-b4c2-74403a904098 | -4.48142 | -43.41937 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e507a8a0-9810-36e9-93cf-55499ae3394a | -4.44339 | -43.41902 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5cb0d54-b3df-3d69-a1bc-7133d0d55212 | -5.51628 | -41.71632 | 2025-10-27 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 324e9e09-3601-36b0-ace6-344b0f7f62e3 | -4.44232 | -43.42544 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29e2f964-7aea-3868-a7c8-93fb254ef9ca | -4.42097 | -45.97966 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35171944-e1b4-3fd1-9313-df7f770b13e7 | -4.42794 | -45.9761 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dd4d2b1-6c5d-37cf-a281-b07294942aa4 | -5.96386 | -42.77625 | 2025-10-27 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5d03c05b-fa03-3e58-bed2-ec2071e3381d | -5.57065 | -40.91981 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d725cb87-3e31-3f07-ac9c-e7a171df1f36 | -6.15043 | -41.69013 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9b6f2ed2-d2f9-32f8-8bbd-a4b7a90f173b | -4.44753 | -43.42633 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e734ef7-5b1d-319e-81fc-cc7c2b01659e | -4.46991 | -43.42404 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f508b8e5-947c-3784-b630-55198493324f | -4.47099 | -43.41776 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92b646a4-fcbb-3f60-8caf-a92a2d7ba88d | -3.19364 | -41.42508 | 2025-10-27 03:40:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b215341b-c14d-3074-ab32-2b1da922985a | -4.39141 | -43.31598 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baeaa05d-0ca2-3033-999c-bf434a867783 | -4.25746 | -40.70272 | 2025-10-27 03:40:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f43411b7-deb9-3116-8bae-7d7ba5a6fa7f | -6.13767 | -41.82857 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3a7a54dc-2088-3eb4-b00f-51b7ec38fb73 | -7.96337 | -45.47077 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c2f95adb-a578-3851-8a0b-24bf01186f61 | -6.42825 | -43.1406 | 2025-10-27 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a64a138e-ddcd-317f-ba11-de6afe3ff526 | -8.13906 | -43.41733 | 2025-10-27 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| daa45fde-3c42-326b-bbe9-a6dcd7466ad8 | -7.83028 | -46.5052 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| efd9a8e7-690b-326a-aa14-d7938f4fd273 | -7.30451 | -42.48183 | 2025-10-27 03:42:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 504e3c64-27dc-367c-97b7-adb2b8e85c6e | -6.50949 | -46.22746 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c78944be-095d-31ec-b988-18d497ca8c36 | -7.82454 | -46.43613 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad1c1694-fda3-326b-8feb-6ac4a3155c1c | -7.40887 | -38.45571 | 2025-10-27 03:42:00 | NOAA-20 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 852b7db2-4954-3a85-bd0a-8778d5f6337f | -9.36517 | -40.61499 | 2025-10-27 03:42:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 33a6be58-25fd-3afb-8833-dbd66e67fa41 | -9.13 | -45.85894 | 2025-10-27 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecca2e0f-a89b-3170-b99a-ef3a52e5f587 | -7.83972 | -46.48781 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4cc6fd63-125f-362e-a281-f5c46bfa4674 | -7.44139 | -41.86725 | 2025-10-27 03:42:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bcd2ca92-edf7-3e66-b7af-20f29c111c84 | -11.42664 | -46.12786 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8db678dd-71c1-3ee5-8e05-9623a5743c77 | -6.88236 | -43.57288 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b158cb6b-4454-3991-a184-556ecb783f04 | -7.68302 | -42.18401 | 2025-10-27 03:42:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 47006e04-cd40-328a-9a66-98eabac3269e | -10.35672 | -47.19712 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71f8deb2-e45e-3004-b199-f28423f8adbe | -8.30817 | -46.18521 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4713c418-de94-38c1-87ee-18d613d31b84 | -11.42735 | -46.12423 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b012c2a-a2ae-3182-a275-ad797373dae7 | -7.87156 | -47.25818 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae8bb047-93d4-322d-be9e-ab0cfc6c8c48 | -8.32067 | -46.18309 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c801901-f28a-38bd-9c2f-ff389ec8f655 | -7.8287 | -46.48029 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0d46006a-98b3-3148-895f-dc19edc233a7 | -9.29953 | -45.22999 | 2025-10-27 03:42:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e74ce86-7dcd-3640-baef-40576988f7fc | -6.88791 | -43.57084 | 2025-10-27 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27ea8356-9a0b-3b3c-84f5-7d2876002856 | -6.17322 | -43.74274 | 2025-10-27 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f8eb8c6-6678-37dc-ab42-0004bf322214 | -6.88639 | -45.16212 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 642b32e9-31bf-3c92-84fc-5721704cf4fb | -10.75736 | -44.20283 | 2025-10-27 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| df8486a1-be76-3c86-8ee6-d7ee553a90ae | -8.95873 | -47.19989 | 2025-10-27 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c957ade8-cffd-31ed-b9a0-19fd4d288038 | -8.31571 | -46.17723 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0eb3c60-8d17-3afe-ba12-2a899bb704d0 | -7.83132 | -46.46621 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecfc1119-3e3f-3e07-b53b-989fb3c5b2a1 | -8.14 | -43.41186 | 2025-10-27 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1071ff84-2429-31cc-90cd-f448adfcd54a | -9.86298 | -44.88507 | 2025-10-27 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b47217de-8e5d-361c-8ed5-733cbcadc235 | -10.31883 | -47.20795 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8312dfdb-207a-33c0-b177-55f7836c3b8c | -8.47736 | -45.55722 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4731dbcf-412c-3d91-b3fa-d5c847413bc2 | -7.77775 | -45.38404 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec9bdc03-4738-3815-9a16-e60696a6084f | -8.88198 | -48.00272 | 2025-10-27 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4cb5cc08-3ae4-3794-90b3-5f73f4f0f528 | -7.83724 | -46.46773 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d04d32d-e2a6-3234-98d6-d464a26756c5 | -10.35441 | -47.18601 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7847110-f60e-3173-bcfa-22912c07cc08 | -11.4251 | -46.10859 | 2025-10-27 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e45a24e-518a-30f7-8ffc-c14f945ffb90 | -6.26103 | -41.82239 | 2025-10-27 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 56287c1c-6f9f-353c-8e40-4262965c4923 | -7.96588 | -38.28518 | 2025-10-27 03:42:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5149933d-a2e1-33fa-87d1-21f552a15ed6 | -8.06655 | -42.49638 | 2025-10-27 03:42:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 88829b77-cc5a-3307-857f-26ca14144400 | -7.8542 | -46.47668 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a60e60c-f8d3-3f28-be94-b6d8381ed792 | -7.93685 | -44.84369 | 2025-10-27 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d09633cb-2e9e-3b44-8423-2178d71b3193 | -6.88846 | -45.15066 | 2025-10-27 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd805d91-804d-3ac0-a1bb-f4ce7be0db42 | -9.49669 | -45.81505 | 2025-10-27 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4569046b-6ae8-31ee-8ac4-a7e10fa5e7ca | -7.85336 | -46.48125 | 2025-10-27 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1dad5ac-fcb3-3c49-b8e5-49d6a896f1e1 | -7.85489 | -46.40602 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc85f7a9-1289-31e4-b34e-6179f1d5085a | -7.82799 | -46.45082 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74c22a7a-037c-38fb-baed-aecf2d8ea580 | -6.53581 | -41.61932 | 2025-10-27 03:42:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 02c5d470-f1f9-3125-a660-cf081762be52 | -8.87651 | -44.83961 | 2025-10-27 03:42:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e347046-7046-3a4c-b3f8-e260326825a0 | -7.96563 | -45.47285 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7138ce0d-09a1-3fb7-95b4-86aede858f22 | -8.88904 | -48.00126 | 2025-10-27 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2c9c5ad-615d-350f-9f09-2483324c4ff6 | -10.21596 | -44.81927 | 2025-10-27 03:42:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c54d482-c4af-3412-b2c4-ca15b6d58818 | -10.31614 | -47.21348 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 639cdaf7-912a-3fdc-b2cb-50e3b76f3104 | -9.29814 | -45.22844 | 2025-10-27 03:42:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89783ffe-a9d9-320d-bd77-a27b48e5e813 | -7.13011 | -39.43695 | 2025-10-27 03:42:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 274219b8-b516-3380-bc9b-a5f673359dd1 | -8.02285 | -46.76038 | 2025-10-27 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c0186b5-d6ca-30f6-923e-0405ee50d761 | -10.92024 | -48.03162 | 2025-10-27 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1429c95-23d6-310b-88bb-5e0e23c1824e | -7.97426 | -45.47468 | 2025-10-27 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a114709d-32be-34f1-9be0-9d7abcbd7042 | -10.35264 | -47.19501 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6db7773-183f-3e0d-bad0-6e80aa0a1266 | -10.31036 | -47.17866 | 2025-10-27 03:42:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cce41b8f-bff8-3586-8ccf-a6f77433a251 | -6.90512 | -39.48298 | 2025-10-27 03:42:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c011700f-fb8c-3d92-adc0-4ade05345e19 | -8.69603 | -44.43534 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e676e194-8e95-3c17-9895-3d0741438744 | -7.87877 | -47.25454 | 2025-10-27 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4413850b-75fb-30ea-840a-7f1f03418641 | -8.70117 | -44.43657 | 2025-10-27 03:42:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02c63016-a268-3626-912f-6483b4177a8c | -8.31406 | -46.18608 | 2025-10-27 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README18.md)
