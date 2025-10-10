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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3d3b19f-a45e-3ded-b3ee-09b951bfeb3c | -11.91835 | -43.34279 | 2025-10-10 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f45c00c8-7099-3421-901b-8fcb22b7d025 | -13.0195 | -41.43077 | 2025-10-10 04:02:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 555d5c20-4992-3d99-aa45-ada8703d8e65 | -13.06322 | -43.84725 | 2025-10-10 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef72c824-2491-3d37-ac0e-e55f433182d9 | -18.02522 | -45.01792 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cc14b5fe-5dde-3852-a556-d41ff79130aa | -16.29805 | -47.15843 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea66f21c-7c78-32bd-a25a-459f0d73bf33 | -13.25074 | -46.47906 | 2025-10-10 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f0e389-64a9-3105-97eb-a1689fca720b | -13.06456 | -43.83931 | 2025-10-10 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 13470e37-9112-3245-a52d-1fdc02fe7b8e | -13.38772 | -42.71362 | 2025-10-10 04:02:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b3cf73f-5209-3b1a-8267-896bb836a816 | -12.98299 | -47.94342 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc3016b0-9122-3723-b76b-214777106247 | -12.57795 | -43.86208 | 2025-10-10 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b2d2ea2-5c3b-3aaf-9e95-f986d09eb4cd | -15.75151 | -43.66544 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce1301a6-da79-3096-9163-8c0f2faf7972 | -13.32639 | -48.48321 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b525a44f-de50-3c33-bf92-2a9f1454c1ac | -14.73226 | -48.36246 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21f74f76-81d6-300b-a40c-713009f4bc9b | -10.93684 | -42.85112 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| af295b14-f8e8-3fa1-b3ce-2781ee3680e7 | -12.7454 | -45.85366 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a62bd9dc-9aeb-3b7e-a97c-b59d06f4aac5 | -13.81844 | -45.78226 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db825444-3869-32cc-8e59-3b31b14a480f | -14.05011 | -49.48556 | 2025-10-10 04:02:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe7fe50-503c-399d-8f07-377f5fa7a255 | -15.38465 | -47.29474 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49ca6c8b-9931-3177-991c-c963e8980f9d | -16.18939 | -43.67039 | 2025-10-10 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e188ec11-21d2-34c0-8418-588106e57735 | -14.87826 | -48.2327 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 01e7ca05-f343-32b7-a181-1790e130e7f7 | -14.68347 | -48.06338 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e649398f-75ce-3fd8-afdd-ebe264889cbf | -10.92654 | -42.84938 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c95e0063-cb46-305d-83a8-ff16da652402 | -15.78922 | -43.65149 | 2025-10-10 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcb29092-db96-3b24-8a2e-0956d611557f | -13.35369 | -47.75233 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ecf25d5-d7d1-34bf-89f3-85ca40c0596a | -11.53262 | -47.1048 | 2025-10-10 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 271ad53c-ec0f-32b0-8607-86e4ab0b65a8 | -11.97456 | -45.21223 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41b708b0-f329-3414-8512-2e9c52e76588 | -11.21874 | -40.46517 | 2025-10-10 04:02:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b42fa868-69e5-31f1-8a8b-4b7695280c66 | -13.84175 | -45.85194 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 53e3007b-752e-3004-aa95-a126075adb06 | -16.29539 | -47.15042 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77eb5f3e-815e-3be6-8ba1-a44cc031abdd | -13.07424 | -47.79445 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f7ffe86-d7db-3796-b8f4-6a140d59458a | -12.77406 | -45.78117 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01b160b5-0776-3e93-bd39-3729f1d747de | -15.7515 | -48.98658 | 2025-10-10 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 167af714-63a6-39b5-8b93-2217f7a0cef0 | -16.27476 | -47.1504 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab22cfb9-8ad2-3254-9206-a7e0155e8f3c | -17.94575 | -45.01954 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5db3f556-d0e3-3a6f-8e29-962b209d0810 | -14.54651 | -46.99932 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d072cd2-234f-3411-a80d-9b9fdab1d1a2 | -14.26451 | -45.87869 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 194c3ae5-3458-34a8-b9d0-3b25f8add437 | -17.3891 | -45.06577 | 2025-10-10 04:02:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f487d80a-6887-3d55-a5f1-f63e08ab1b77 | -17.66361 | -44.45369 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f05be48d-b03d-3602-8d34-dda5c5bc76ce | -16.33037 | -47.04885 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 726f7cd8-6e93-32b2-9adc-ff0ecba8f24e | -15.32749 | -43.19672 | 2025-10-10 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 237ec0de-aa74-38c9-a4ce-f3d6c393b11b | -14.87546 | -48.22355 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b10ce90-57db-3e46-9e1e-a115b1cb9155 | -13.2964 | -47.13792 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc8d029a-ac26-33c7-95bc-5442fd089128 | -16.25148 | -47.11065 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b62e0d93-a452-306b-b8e4-655692f246af | -14.42953 | -48.01157 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e46e605-ad3f-3889-97e8-f4c624f2244e | -10.77131 | -42.68443 | 2025-10-10 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9536ba30-e702-313f-a9bd-977db4db2d2e | -14.88677 | -48.23561 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 2e104fde-938c-3e89-81f2-97b2e542cebe | -17.93574 | -45.0313 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4508992-a1b0-39cd-bf4d-2a30fb8a0971 | -14.86072 | -48.47074 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 122a02cb-8351-3c55-8a98-bd902ac99ce7 | -16.74624 | -43.9767 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa6f636d-5a3c-3a9c-877d-d684e5a40819 | -14.87905 | -48.22852 | 2025-10-10 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 669fd258-19d0-3b44-b06d-3b64eeed4ffa | -16.7416 | -43.9835 | 2025-10-10 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20c25c11-4bea-3d2d-9805-1289502e830a | -13.28196 | -48.01559 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ec2b306-af45-3e41-bdb4-d534473de2d1 | -13.83626 | -45.81553 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c29278c-cd59-303a-9770-880e616f6dd9 | -18.00183 | -43.31422 | 2025-10-10 04:02:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b962a0a-8ece-3a0e-9d04-96103473860d | -12.10106 | -44.99717 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6594b872-d4ce-3958-9f51-92be8fb2e7d1 | -17.66704 | -44.4543 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd3ef79a-711c-35f9-a837-a9b58a9880e7 | -13.29703 | -48.48811 | 2025-10-10 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 05d33c15-ee93-3075-bb98-5e2ad7f24fa8 | -16.32053 | -47.0579 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb7c9b21-0a3f-32dd-bc9b-750039c6ece4 | -13.04861 | -47.93583 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d27fbc3b-25bf-3fc7-ab4e-04826573595d | -11.7292 | -44.29871 | 2025-10-10 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abf72594-30a4-39c3-b9c8-5a2ef0e96cdb | -12.71602 | -45.83782 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7299aa8e-a671-35cf-a087-8c92c532fa48 | -15.2008 | -44.48936 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c14317f-0c4d-3998-a37a-000f306b2ca5 | -11.86205 | -44.91519 | 2025-10-10 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f126dc1-4fa8-3155-9061-14df41d5fe6b | -14.94814 | -46.77245 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26d6f560-86b7-3858-8e35-0967b1e068f9 | -17.96329 | -44.95977 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cdc581d-2920-30ac-b2b1-a7e8a8ce38d3 | -15.20361 | -44.49405 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f913441-14d0-3c56-a8cf-189ceb3d5957 | -13.22899 | -47.61286 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 290749c1-d32b-3047-a5fd-38510974cae2 | -15.20393 | -44.49116 | 2025-10-10 04:02:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dd9135e-7209-3769-9f74-30c6e2f35fe0 | -18.04888 | -44.98425 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 77d560b4-ee86-33f9-abe5-4e13a5760334 | -16.27475 | -47.17283 | 2025-10-10 04:02:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 274f7ed2-a55b-3fd1-8900-524086510888 | -14.8435 | -48.46435 | 2025-10-10 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa944ee7-a458-32fe-be04-8f908363d3b5 | -17.65014 | -47.24998 | 2025-10-10 04:02:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7914d093-e464-33c6-9f76-d54f844b3fe3 | -13.40575 | -47.25652 | 2025-10-10 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d85fb63-0dd9-349a-aecf-d78c952aeb28 | -12.22378 | -43.79037 | 2025-10-10 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c637154-b9e1-3313-b19b-eda8b16c59b5 | -14.3355 | -42.8215 | 2025-10-10 04:02:00 | NOAA-20 | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b3f5e479-8fbb-31cd-92e0-074b8a0fc716 | -15.3281 | -43.19303 | 2025-10-10 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f32beb4e-62c1-3b78-ab01-21e33171b6e4 | -17.32179 | -46.8362 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d99e374-8ea9-3eea-8ee2-4cdcc4812e73 | -13.07351 | -47.79848 | 2025-10-10 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 796aade4-229f-3198-9de9-80a40e6ef19d | -13.82226 | -45.78292 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4c38a68-2743-340c-9261-b560789d13af | -12.71992 | -45.83853 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adf75b41-680e-3b9e-9ae7-bbdeabaa34e2 | -14.71314 | -45.17604 | 2025-10-10 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bed0fc17-76b2-34b9-8e2c-1245ce3896fe | -18.07309 | -44.48305 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18cdea64-e032-3689-a71e-991e68d17fcc | -10.42272 | -45.00153 | 2025-10-10 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3f401c6-2876-3c26-9dd4-76bf8dad07c2 | -12.62571 | -45.06626 | 2025-10-10 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2e2b7f86-343f-39ce-baee-59ff2dd6c1e5 | -14.26533 | -45.87399 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fdc4f8b-b74b-3626-98e8-f15bfc0c5e17 | -14.26709 | -45.90894 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2f9a46f2-14c2-385b-96a5-13d6a1e86107 | -14.99125 | -47.20281 | 2025-10-10 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8835e5b5-bac6-3084-893f-a0a18c9f1595 | -13.5224 | -48.11472 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c878b01-edb8-35b4-a735-53c6e4823eae | -15.09012 | -46.61157 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8fd66dfd-79e1-3875-b3eb-206023d9dbeb | -15.42538 | -47.99337 | 2025-10-10 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 599e74f0-9952-3be5-b751-e04bc79747af | -17.37631 | -46.68853 | 2025-10-10 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fbcbc6a-c762-3a18-852c-a494a74b1eab | -17.94783 | -45.02835 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88111f48-b179-3d27-9e8b-f033c7b3633d | -14.26878 | -45.89928 | 2025-10-10 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a554b9a0-021e-3cf8-a78e-cf55fc738f9a | -15.50503 | -44.29929 | 2025-10-10 04:02:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be765fbb-40b2-374b-ad67-e7cb16d2eba5 | -18.02104 | -45.02134 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 464a8618-9995-3657-8b7a-ae5549a082c4 | -15.09307 | -46.61777 | 2025-10-10 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d2006280-4c5a-31fe-8cca-000c681dee37 | -13.22821 | -47.61719 | 2025-10-10 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcea9692-48cb-353e-8796-31786552b1ae | -11.97538 | -45.2075 | 2025-10-10 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 086a4098-fa52-3ffb-bf23-7055efd193ad | -14.89618 | -46.85347 | 2025-10-10 04:02:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 751fb55a-c61e-3c2f-8b37-fd4b07724ade | -17.93643 | -45.02718 | 2025-10-10 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README29.md)
