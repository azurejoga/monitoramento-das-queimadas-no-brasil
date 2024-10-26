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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3990ad1-1edc-3980-9037-373ca32a0efd | -7.2903 | -43.6696 | 2024-10-26 14:25:46 | GOES-16 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 23e65fee-e7da-3779-9707-dc9bbec763c4 | -7.3299 | -37.4457 | 2024-10-26 14:25:46 | GOES-16 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 180.3 |
| 82e762c5-db61-3501-b536-af2ce352a5d0 | -7.4097 | -44.7427 | 2024-10-26 14:25:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 38713963-38a4-372c-9f62-9e7efd092fd8 | -7.4288 | -44.718 | 2024-10-26 14:25:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| dfc9239e-c8c2-35a0-b71c-e5742ec5cddc | -7.41 | -44.7198 | 2024-10-26 14:25:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9a195fae-2ff6-3fbe-868d-1f1086be3393 | -8.999 | -44.3235 | 2024-10-26 14:25:56 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d4a9b9c2-a07f-399e-81a1-4b27b73ff893 | -13.133 | -43.0339 | 2024-10-26 14:26:19 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 80ea1901-5a12-3dc2-82b5-cad0438657e0 | -13.1136 | -43.0374 | 2024-10-26 14:26:19 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 24faa082-3395-347a-a4d0-7b845401a6d1 | -13.1335 | -43.0098 | 2024-10-26 14:26:19 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 87.2 |
| e12fc149-ae5d-3dad-9080-c6c53b2195a8 | -13.7334 | -43.0679 | 2024-10-26 14:26:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| b35f1180-79da-398e-bd96-870003473675 | -13.6686 | -43.3677 | 2024-10-26 14:26:22 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 8530d820-35a0-3ed1-bedb-181e345fa083 | -13.8758 | -43.6636 | 2024-10-26 14:26:23 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 5370a6f3-3ffd-3175-9728-7c5d5de71851 | -13.8968 | -43.5881 | 2024-10-26 14:26:23 | GOES-16 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 48649025-f335-35f3-bf3e-55e3f2febaa0 | -13.832 | -43.0012 | 2024-10-26 14:26:23 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 77.9 |
| c2029253-0a21-3d18-bce9-c5e9d06a5c52 | -14.0719 | -42.7136 | 2024-10-26 14:26:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 8ee6a9b6-a8ef-34d0-8b03-f746b36e059e | -14.1855 | -43.7248 | 2024-10-26 14:26:25 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| aa5ab1b9-ab5a-377f-b3ab-0b97fbf4e00b | -14.7677 | -43.0109 | 2024-10-26 14:26:28 | GOES-16 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 98eda0ad-f395-32f8-82a3-aa1bd8e03963 | 1.7959 | -50.4677 | 2024-10-26 14:34:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 60f3303c-626a-3068-8594-ad12a2d499c7 | 1.2425 | -50.8722 | 2024-10-26 14:34:58 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e208d084-2eb3-3a88-860e-f457c49f23a8 | -1.1831 | -53.8985 | 2024-10-26 14:35:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8958be44-005a-3884-a203-dfeadf4d10e8 | -1.7367 | -52.3302 | 2024-10-26 14:35:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d35e542e-4957-3cf6-a026-0ee63beeea04 | -2.7153 | -57.4526 | 2024-10-26 14:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f11f9a5d-0ede-39d1-8d3a-b853224ed957 | -2.8055 | -42.4769 | 2024-10-26 14:35:21 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 895f2d21-b001-3f86-a27c-08a05161570f | -3.473 | -43.3144 | 2024-10-26 14:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 337.9 |
| 30b97824-0b7f-3449-b218-4929d4cb1bf2 | -3.4917 | -43.3136 | 2024-10-26 14:35:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 188.0 |
| f18f3c85-84fd-3e46-b89d-9ca1034ac3b5 | -7.211 | -44.0252 | 2024-10-26 14:35:46 | GOES-16 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 4ae111d2-3643-3f86-a113-b60f02a07686 | -7.4097 | -44.7427 | 2024-10-26 14:35:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| abbc5e3d-4425-3bd8-ae11-4690d7b3f297 | -7.3912 | -44.7216 | 2024-10-26 14:35:47 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 361193d8-fc44-3a8a-bd62-e5464a22b039 | -8.3387 | -42.8084 | 2024-10-26 14:35:52 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 0a18c65b-4049-3a66-a1f1-1a0ff3045019 | -10.3533 | -45.0791 | 2024-10-26 14:36:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 179ca33d-615a-3a58-9452-0f7850e390c5 | -10.5278 | -44.8723 | 2024-10-26 14:36:05 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 36e7db27-6931-3c3f-9504-d61e41c628e1 | -10.5087 | -44.8748 | 2024-10-26 14:36:05 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 157.5 |
| de12ed9f-2f88-33fd-83d3-fe08943bdd22 | -10.5281 | -44.8492 | 2024-10-26 14:36:05 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 016a612d-ea52-399a-bfbd-f62271c89546 | -13.1136 | -43.0374 | 2024-10-26 14:36:19 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 72.5 |
| c4d6bee7-4064-3227-bf1a-bdcd132fe9fa | -13.5107 | -43.492 | 2024-10-26 14:36:21 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 95d6d60a-ad92-3e4b-9645-ae13568e1249 | -13.5297 | -43.5124 | 2024-10-26 14:36:21 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3676be78-4e81-340c-9b85-f5cdf9c9a467 | -13.6686 | -43.3677 | 2024-10-26 14:36:22 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 34bc2c5a-ddf2-32c6-91eb-e76d5d8dec19 | -13.8758 | -43.6636 | 2024-10-26 14:36:23 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5fc7196a-39cf-3a71-b39b-8e1d1f478565 | -13.8968 | -43.5881 | 2024-10-26 14:36:23 | GOES-16 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1239176d-da50-3913-96d8-a430b2716bfe | -14.0477 | -43.7983 | 2024-10-26 14:36:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| cb3ecabd-9dde-39e3-a148-f67c9d7fa774 | -14.0719 | -42.7136 | 2024-10-26 14:36:24 | GOES-16 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 812883e3-a8f1-3b37-b68c-876cd84225c7 | -14.4961 | -42.0923 | 2024-10-26 14:36:26 | GOES-16 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 0aa2a605-3bfe-3af3-95cc-8fab76abc07a | -15.3369 | -43.7856 | 2024-10-26 14:36:31 | GOES-16 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 277a5db4-c9e6-35e5-849c-7ef65be60239 | 3.6001 | -51.2961 | 2024-10-26 14:44:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 99438e17-392b-3bdf-ba86-a7f3cf1ee8da | 1.7959 | -50.4677 | 2024-10-26 14:44:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 107.1 |
| a9ad707b-0713-3b3b-9743-113301b9f55d | 1.3346 | -50.8919 | 2024-10-26 14:44:58 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e30f4df6-1f48-30d4-8c9f-ca469614c319 | -1.1831 | -53.8985 | 2024-10-26 14:45:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0ea21bff-a9a9-3da1-b274-bcb88f5fbfc2 | -1.7367 | -52.3302 | 2024-10-26 14:45:15 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ee6e9537-cd74-3e62-95a0-335a66b01210 | -2.5339 | -56.7537 | 2024-10-26 14:45:20 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b2a55b3c-c9de-34d2-878f-46f7e463bf05 | -2.7153 | -57.4526 | 2024-10-26 14:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| fe62c705-cf88-331f-918a-ad27bb06a5ca | -2.7336 | -57.4522 | 2024-10-26 14:45:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 108.9 |
| dcfd11bf-d02d-3e7e-aa87-e5a32fcf075f | -2.8055 | -42.4769 | 2024-10-26 14:45:21 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 0138d798-9d52-3687-a633-1e58e99e3e50 | -2.9724 | -42.7055 | 2024-10-26 14:45:22 | GOES-16 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 64a00ea7-65c1-3cc6-8c18-92a8c442d421 | -3.473 | -43.3144 | 2024-10-26 14:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 264.7 |
| c39c02e3-98a6-3ded-9514-6d6b1f5158dd | -3.4729 | -43.3377 | 2024-10-26 14:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 092c8a6f-5036-3933-b180-1d4b94d31c25 | -3.4951 | -54.4366 | 2024-10-26 14:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 672d2031-a7c5-3467-af5f-81551e90a750 | -3.495 | -54.4567 | 2024-10-26 14:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b7526dae-78c8-3914-9462-7a3125ff79dc | -3.4767 | -54.4371 | 2024-10-26 14:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 82007b9d-e745-30e5-8d77-2d1ee673889d | -3.4917 | -43.3136 | 2024-10-26 14:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 0420d3f1-f445-3f45-9043-7b276dec0e19 | -6.5592 | -41.7062 | 2024-10-26 14:45:42 | GOES-16 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 43b28bf7-f72d-3296-bede-70b0de07c0e2 | -7.4097 | -44.7427 | 2024-10-26 14:45:47 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c3fdce41-5b9c-3eee-9eb5-37aaa2100d8b | -8.3387 | -42.8084 | 2024-10-26 14:45:52 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| bdefdf1f-75b3-330a-aaee-8f4eaba5f716 | -10.5087 | -44.8748 | 2024-10-26 14:46:05 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 39950b85-9e64-3545-beb0-daee5b162366 | -10.5083 | -44.8979 | 2024-10-26 14:46:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 7e21f296-c653-3e54-9630-146bd64cbf36 | -10.5281 | -44.8492 | 2024-10-26 14:46:05 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 80a152c2-d56d-3b8b-9bf0-63b7347c0270 | -11.3072 | -45.0189 | 2024-10-26 14:46:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 3ce3d2e4-c138-3198-8b0f-6f25a64c390b | -11.5225 | -45.8369 | 2024-10-26 14:46:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4773bd6c-f039-3e08-9477-b5e2a1a0c87f | -13.5107 | -43.492 | 2024-10-26 14:46:21 | GOES-16 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b85f2329-9d84-3d4d-af78-4a9cb2452ee5 | -14.1401 | -44.0186 | 2024-10-26 14:46:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |


