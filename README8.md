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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4da2872-8883-3266-9cee-61abd1f7e85d | -4.56698 | -43.10849 | 2024-11-02 00:54:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 37611cfc-45b6-3954-aa03-747d04f1ecfa | -4.56466 | -43.09266 | 2024-11-02 00:54:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 63730511-8f0e-3607-b78d-b905157cabde | -4.55539 | -43.11021 | 2024-11-02 00:54:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 84785fdc-ef76-3514-889e-d0990ca63429 | -4.55306 | -43.0944 | 2024-11-02 00:54:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c568b95f-85fd-3881-b1e7-8588eca28c7b | -5.32091 | -43.0737 | 2024-11-02 00:54:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3587863e-0b8e-3aaf-850b-7904d614461b | -5.32066 | -43.08412 | 2024-11-02 00:54:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 62ca70dc-14c8-381f-b6ad-28fe3e98a662 | -5.31828 | -43.0686 | 2024-11-02 00:54:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 178d694b-6788-304d-a80f-8354743a369b | -6.93729 | -42.80993 | 2024-11-02 00:54:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6959770b-aa8a-3dc7-9ac4-b17b43854245 | -3.54277 | -43.57138 | 2024-11-02 00:54:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d52cdd5b-0de2-3532-922a-c806bec02985 | -3.5266 | -43.61983 | 2024-11-02 00:54:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 32969e42-df97-3276-b108-18669538560c | -3.23096 | -44.42006 | 2024-11-02 00:54:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 112.0 |
| e3416bdc-2eee-3659-951e-ccad883e78a6 | -3.22903 | -44.40693 | 2024-11-02 00:54:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8ba7774f-c8e5-3482-8246-b77480388ded | -3.22518 | -44.41372 | 2024-11-02 00:54:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 194.0 |
| 0e729cce-a1b4-3aa8-a290-69b47959ec56 | -3.21833 | -44.40847 | 2024-11-02 00:54:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 17e1c4a5-e4b9-3342-859f-ca180727dd2e | -3.1893 | -44.39194 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 15f8e9e8-e544-39ec-b84d-04552d360018 | -5.00749 | -44.38401 | 2024-11-02 00:54:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f1523666-1acc-3985-97f0-eeaa62beb5df | -5.00565 | -44.37145 | 2024-11-02 00:54:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| fcf36ec7-d05c-3462-83cd-ffc8523ee704 | -4.91584 | -44.6602 | 2024-11-02 00:54:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 32e70add-cfd7-33ae-bc75-6189fb932088 | -4.65976 | -43.82053 | 2024-11-02 00:54:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b810c0a3-15b0-32bb-ac3a-71d0c8ff5390 | -4.60341 | -43.9894 | 2024-11-02 00:54:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 5f5fc097-e63c-3288-8a37-88a894e5863f | -4.5349 | -43.28807 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c4859eb8-3170-3106-b848-c60709006407 | -4.52578 | -43.29595 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a87ba5be-9249-3fc9-a737-99a397003d74 | -4.52348 | -43.28983 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 17cec741-4d7c-3e04-a71e-f64963373370 | -4.41548 | -43.48745 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aef924fa-efb5-3720-b7b7-f63da9a07d4e | -4.40422 | -43.48917 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 3c834c32-4c29-307f-b459-9b8018b289bb | -4.40202 | -43.47435 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 4e84118e-1177-341b-b4bf-f91537ca1e65 | -4.3998 | -43.45943 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 8c3d8419-118f-3958-837d-286044328fa3 | -4.39297 | -43.49097 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 6a0d64e6-6931-3f73-9445-73b3ca2a5c31 | -4.39074 | -43.47606 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 3bafe59a-2a1d-3177-8be6-05da3f5ea7a5 | -4.38849 | -43.46106 | 2024-11-02 00:54:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 9cc2ca56-c471-3d2f-a50e-23a28ee91f84 | -3.78276 | -43.56403 | 2024-11-02 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dd17fe3f-52d6-3bca-aaff-24c95fe4c584 | -3.78053 | -43.54884 | 2024-11-02 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2bdc76b1-8974-34e4-ad58-5cf84de4a0d6 | -3.77144 | -43.56569 | 2024-11-02 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| c7e13cff-bc94-3989-8198-c0e78b0b5b8d | -3.76922 | -43.5507 | 2024-11-02 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 1f5b3ed4-7be8-3e93-b9bb-b2533375b3a1 | -3.76697 | -43.53548 | 2024-11-02 00:54:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1fdc9549-9fb2-3894-9b6f-f00ea149f4bd | -3.65338 | -43.70165 | 2024-11-02 00:54:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 572d38ca-e3cf-3a87-97b3-c0e94972d9e6 | -4.70175 | -44.47257 | 2024-11-02 00:54:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e3f1152c-08a9-34ad-8e45-ee5dd17e932a | -4.60538 | -44.00295 | 2024-11-02 00:54:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| ddb6938c-527a-39c4-9766-09876e1ac4ae | -4.45696 | -44.17393 | 2024-11-02 00:54:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 86042ee5-64d4-3b9d-ab90-c0a4115d0fa4 | -4.44629 | -44.17553 | 2024-11-02 00:54:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 52a0b9d1-bb04-31db-91f4-f2f44ca2002e | -4.44438 | -44.16231 | 2024-11-02 00:54:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e0ad190a-7dbd-3c95-badb-4b34ec9a8fb6 | -3.83374 | -44.13865 | 2024-11-02 00:54:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d5852596-e4a0-3df1-91f8-95b05ab13a93 | -3.83101 | -44.14477 | 2024-11-02 00:54:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 536b12de-7843-3c04-b866-b5544699eaab | -3.82909 | -44.13122 | 2024-11-02 00:54:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 72fc6c43-7fd8-34a9-be1c-99ab959f515b | -6.12407 | -43.98167 | 2024-11-02 00:54:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e5fc2853-856e-3d15-a2a7-94ec3f02a617 | -6.12213 | -43.96873 | 2024-11-02 00:54:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 09a0ea3e-5b05-308e-98a7-3f97b688b7ab | -5.25783 | -43.35191 | 2024-11-02 00:54:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3edaef9a-e386-3dc1-b00b-b84142764a54 | -6.31673 | -44.72582 | 2024-11-02 00:54:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6cfd188a-7f83-3273-8688-7aa845b57b89 | -5.2032 | -44.31718 | 2024-11-02 00:54:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 4b706426-9bef-376c-a188-b51ab99b4d61 | -5.20136 | -44.3045 | 2024-11-02 00:54:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 2056ec20-bc94-3df0-a459-fb9bd4214e67 | -5.14931 | -44.16882 | 2024-11-02 00:54:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| e810b33c-430d-3f1b-975d-3eecda11c7c1 | -5.13875 | -44.17032 | 2024-11-02 00:54:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e3f0cdf-bb27-36cd-ae65-6faf19a4724c | -5.09113 | -44.10342 | 2024-11-02 00:54:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ad13f04f-a532-3329-a17e-7254410f4dc8 | -5.08924 | -44.09037 | 2024-11-02 00:54:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 259b27ad-a7b4-3f2d-854a-fcdefefda92a | -5.06776 | -44.23909 | 2024-11-02 00:54:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a59fe1e-97f2-3c00-81ca-e66fe8695840 | -5.06586 | -44.22623 | 2024-11-02 00:54:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6fd7ea6f-7fa7-3aef-aa29-e8ef8695537b | -6.93862 | -44.29049 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cfca661b-c6bd-36a7-b005-9d0628a55bb4 | -3.37644 | -45.70557 | 2024-11-02 00:54:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d767ba30-7f0e-3ea7-bed6-febca5d0982c | -3.37491 | -45.69475 | 2024-11-02 00:54:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 544642d4-732f-3bd3-b0e0-48b99e11e9bb | -3.32571 | -45.41954 | 2024-11-02 00:54:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 2b8dce57-512a-32d3-9f5d-dc5af515855d | -3.3241 | -45.40825 | 2024-11-02 00:54:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1ccf04d1-190a-3e0b-b9d6-ed7e6f46a1de | -3.30259 | -45.3998 | 2024-11-02 00:54:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 02762bbf-b7ac-3883-af78-82b598c4224f | -3.30096 | -45.38848 | 2024-11-02 00:54:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| cf636b79-b080-3d66-9cb7-d4f80d6f05ac | -3.23906 | -45.59747 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 451877a8-e5fe-3413-be82-735403c83c05 | -3.23747 | -45.58641 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 19cf2ef5-003c-3b68-9754-e623a849768a | -3.22923 | -45.59887 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2c518a9c-c9e6-3d30-bd47-dff7ad0f01ee | -3.22763 | -45.58784 | 2024-11-02 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| df69fd04-c3b4-37e3-b782-1195ee90661b | -3.14753 | -45.31803 | 2024-11-02 00:54:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e41366ff-fa28-3b90-a1c9-cac2ad7cf3a3 | -3.08047 | -45.13702 | 2024-11-02 00:54:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 16631567-5989-307c-9111-e59b4e41b368 | -3.07032 | -45.13853 | 2024-11-02 00:54:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5cf15e03-28dd-3f2e-b4fb-84340f48f03f | -3.06619 | -45.74649 | 2024-11-02 00:54:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d3ab85cd-a78b-3f8f-8d6d-b435a41d6523 | -3.06462 | -45.7356 | 2024-11-02 00:54:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a4f17481-7caa-3bd9-81ef-c6cf416221dd | -2.99964 | -45.21483 | 2024-11-02 00:54:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e2ae883e-e416-3740-87b1-015e9894a0a8 | -2.63909 | -45.77215 | 2024-11-02 00:54:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3fe07fca-fa93-3fb8-a8ce-81efa234800a | -2.61807 | -45.40788 | 2024-11-02 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ae92d27e-fb05-305a-9eae-0f4addad6eb1 | -2.61645 | -45.39633 | 2024-11-02 00:54:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d4a5ad89-4093-345e-83d1-1bdfe996c8dc | -2.39603 | -45.35712 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| da494cbe-11cd-316f-93bd-75f633caec7f | -4.62036 | -46.03179 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 9b9cc449-906e-3339-9390-2606beb1810c | -3.22703 | -44.42686 | 2024-11-02 00:54:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 7c20aea3-5fa1-393b-84d6-7f45525a930b | -3.22028 | -44.42162 | 2024-11-02 00:54:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 70c5f0af-ead3-3f9e-9ef9-e4ed73b3f7c3 | -4.92751 | -45.02947 | 2024-11-02 00:54:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d2b9ec7c-d268-3e9b-a5c4-4c35908cc31c | -4.41582 | -45.65664 | 2024-11-02 00:54:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 19e18af6-8627-37e8-afda-55e1a75cea09 | -4.41428 | -45.64609 | 2024-11-02 00:54:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6ccd05c0-53be-343c-a455-05d71d057f19 | -4.41162 | -45.65222 | 2024-11-02 00:54:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 35.0 |
| e6c1717b-c22d-3624-b5b3-ef8c02d9efa6 | -4.41013 | -45.64157 | 2024-11-02 00:54:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| c8ebb922-3ec9-372d-a942-0a30e6bb89e8 | -4.38119 | -45.64578 | 2024-11-02 00:54:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 869192cf-eeab-3f47-88c0-d83fb66b130a | -4.36085 | -46.01571 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e9259fee-a661-399f-aa37-9a0103429e15 | -4.3594 | -46.00541 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b18943a3-7a17-379d-87d0-a2c6886c05cd | -4.33256 | -45.8838 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1071f5b4-0dbb-3e8c-b76a-ce295878d0fa | -4.31507 | -46.03262 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ae41beb8-bcd7-37b8-a764-4e34e86ebcd1 | -4.30709 | -46.04411 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d2af9fd7-0f29-3dce-bf54-07f5323055fb | -4.30564 | -46.034 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bbba36ce-76fb-32e1-8a09-791990d58a98 | -4.27799 | -45.56855 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 49e11b39-e7b0-339a-947f-852453e1fd41 | -4.27646 | -45.55783 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 91288d7f-5941-388b-b8fc-93d96b6a5e3c | -4.24073 | -45.58498 | 2024-11-02 00:54:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d5013235-648f-3c57-b1a2-8730e3554024 | -4.22052 | -45.94774 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 670a6733-2bc8-3a3c-a352-9bfc9095a240 | -4.21101 | -45.94903 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 972cb0ae-544c-3753-9b6d-c24310537b5b | -4.14449 | -45.69201 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2c359abc-d981-3e0e-9488-b1bec6915d82 | -4.14293 | -45.68136 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e737b3e5-503e-3b66-b4ac-92e40525cd7a | -4.14038 | -45.68812 | 2024-11-02 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |


[Clique aqui para ver as próximas entradas](README9.md)
