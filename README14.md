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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e456337-e58f-32e2-8d27-7331b337998d | -14.31022 | -51.54583 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ecf2472-2048-3f60-bce0-ba77e2f3a90f | -14.21525 | -51.51112 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 56665af9-cdee-34e3-b62c-a3e2241ca90c | -16.12575 | -53.9679 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9221db0a-6757-3650-95ba-f8e16f940dc3 | -16.11772 | -53.97259 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ee19f65f-216e-3d00-900d-25f8ad60a87b | -20.84902 | -42.80573 | 2025-10-13 03:57:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 64dc0075-1444-3a9c-9df1-7cc2c9fde500 | -19.86883 | -42.44654 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6a8171c-eb12-3b3b-9377-d0be66c174c0 | -16.12904 | -53.96949 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1cdd6d4b-5745-3249-8ffa-525f312cda93 | -17.17951 | -43.0986 | 2025-10-13 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27c086d7-08ef-3a98-9ff4-1c1bc02747bc | -14.30732 | -51.55957 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b7db586-b4fd-3d87-977f-397043b4f15a | -16.12621 | -53.98181 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33faa718-ae11-3957-bf9c-72c0609ee4a2 | -16.11637 | -53.97865 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bc21868c-aacd-3c8e-921e-bd33dc287ced | -14.29828 | -51.5433 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a364ea-c3c8-34cc-9b8b-27289368980f | -16.12298 | -53.98029 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1039400b-c444-3e04-893f-1cd3f49cb94b | -16.90774 | -43.95517 | 2025-10-13 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1865fe6b-8be1-3560-9106-9f8ee0d2497d | -16.42571 | -43.66919 | 2025-10-13 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9f34b9e-a21e-36df-b8e5-192cef81cb75 | -16.35015 | -42.39623 | 2025-10-13 03:57:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a802656-e40d-37f1-95ba-b25b86c576d6 | -18.3152 | -42.26311 | 2025-10-13 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3e5baeba-8b52-33e9-a714-f7e4c1a022b3 | -14.31196 | -51.55577 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64a79956-b506-3fa8-8054-31abdb463908 | -17.3315 | -53.8143 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89add4b0-95a1-3662-984c-12d695eb48f9 | -16.31762 | -43.09987 | 2025-10-13 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdafa548-e790-315d-8213-081424d1fc71 | -19.86278 | -42.4416 | 2025-10-13 03:57:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 15870398-d21e-3585-81ff-b7f297e091b9 | -14.30829 | -51.55498 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fc5322f-1ae6-30c2-9529-c49c5ff85803 | -15.79904 | -42.51544 | 2025-10-13 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5b46605e-a832-3cd2-8511-bf6954a9f91d | -14.80874 | -48.39279 | 2025-10-13 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ddd1ff1-0ac8-3cb8-83a4-34c251e47f4b | -21.08714 | -42.93476 | 2025-10-13 03:57:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ed9fb61-9a50-3f32-8b5b-664177497ebd | -17.35465 | -44.46115 | 2025-10-13 03:57:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bdc790b-1ea3-3667-88e0-7eeb04ff4163 | -17.3279 | -53.8003 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20f11c0c-6e2a-39fe-a9d1-2e634251d410 | -14.9375 | -46.73279 | 2025-10-13 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07a52fec-6495-37df-a0b9-332db1559405 | -16.91204 | -43.95162 | 2025-10-13 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f7758e3-fb0c-3370-8ec6-3e734eae3392 | -15.66643 | -43.01737 | 2025-10-13 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c422e48-196f-3a2c-b572-9a8a43df0ce5 | -16.12763 | -53.97562 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 26280361-e060-3b67-8680-76b359d8c111 | -19.8622 | -42.44525 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c2703d23-c780-37e7-b8f9-5f20212b1b2f | -14.21174 | -51.51705 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| de60f388-4b66-30e8-ae34-d8470758a83e | -14.18945 | -51.5152 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d3f3f08-b51c-3537-9f7e-eaded2a93eea | -14.18975 | -51.50274 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f56f9c19-c0a1-380a-8593-9cee831a01b3 | -17.3251 | -53.81264 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b07475d-1a74-388c-b95a-b084544af978 | -14.80968 | -48.38782 | 2025-10-13 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a307a7c6-d86d-3606-a8d7-a5aa1f137794 | -16.35541 | -42.3855 | 2025-10-13 03:57:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03fedbca-7e4f-3a33-ad04-8a9872af843f | -14.30425 | -51.54457 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 501942bc-f1f8-3571-8fc0-7967053f5ade | -15.79967 | -42.51165 | 2025-10-13 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| edecfbb7-9bb7-3c2a-ad04-518fd06d122c | -14.20833 | -51.51442 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9bfefb1f-22a5-3f76-95c7-e3c414d8e33e | -17.34072 | -53.8035 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc0e7f39-236f-31b0-b0fd-36255e0ae793 | -20.84508 | -42.80885 | 2025-10-13 03:57:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d2530c80-4b97-3b93-990f-6e3eed2a2b4d | -16.23829 | -43.50891 | 2025-10-13 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4574185c-64cf-3d22-b913-fabd428a616b | -14.31103 | -51.56036 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f7c227c-5fff-3949-8a90-41e5ddff7329 | -15.02034 | -48.75085 | 2025-10-13 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6015577f-8db3-3d7f-a0ed-2797192cbb98 | -16.73615 | -43.97413 | 2025-10-13 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1871512-67d5-3b67-8913-47195c1629f1 | -16.95324 | -43.0838 | 2025-10-13 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3deedee-3b8c-3e7b-ad19-66777a9191ba | -16.19592 | -43.67275 | 2025-10-13 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ba6b8874-32b1-342e-84cc-fa0c95b47d6f | -15.66066 | -43.90248 | 2025-10-13 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6197cfbc-e27b-3096-8a71-a114e25f2935 | -18.3146 | -42.26683 | 2025-10-13 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 813bcd20-01f8-32c7-90d5-4a04cc8f8fac | -16.34865 | -42.38427 | 2025-10-13 03:57:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b5a456a-1562-3a5e-95ab-3a4145042eab | -20.47403 | -42.78877 | 2025-10-13 03:57:00 | NOAA-21 | AMPARO DO SERRA | MINAS GERAIS | Brasil | 3102506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 090eec16-906a-316b-99d1-dca57606e85f | -17.17607 | -43.09794 | 2025-10-13 03:57:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 560a279b-32ab-3afd-a432-d0747204909e | -14.32024 | -51.5575 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 439513e1-b87c-3182-859b-8c8773a95e4b | -14.93309 | -46.73231 | 2025-10-13 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 901c6009-ae2c-33b8-b484-7a1917e3df22 | -14.20929 | -51.50985 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a31870fb-573c-3764-bff7-e0c03dd3827d | -15.6599 | -43.90686 | 2025-10-13 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22346d51-cc42-31a7-9f42-486c6ab6d843 | -14.21429 | -51.51568 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e3ef0b44-0d43-37c3-89e2-562c25323715 | -19.86127 | -42.47204 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 711e2fc7-d1d8-33b1-9058-5d4a89de0fd2 | -19.85312 | -42.45899 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4253325f-bfd2-3887-87f7-6965fd9bddd1 | -18.3188 | -42.25651 | 2025-10-13 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5c5d865f-59a3-3807-8978-82300abdb1c8 | -18.05632 | -41.45587 | 2025-10-13 03:57:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 24ded7cd-2487-3245-b5ff-21795da4cbbd | -14.80747 | -48.38925 | 2025-10-13 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df1a7edd-7fe2-35ae-a05e-604d0d494bf8 | -15.02529 | -48.75181 | 2025-10-13 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00ffc3c2-e964-3f5e-a3b7-cb3520a1f91f | -17.34577 | -53.81113 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ace4c6b4-1744-33a5-84b4-00565f1baf54 | -14.29593 | -51.54273 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| efe50610-5360-30a9-853b-e6731e38db3f | -19.8661 | -42.44223 | 2025-10-13 03:57:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6c31809-ebae-382b-b720-6bd36dac5d53 | -18.37196 | -42.14073 | 2025-10-13 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7b246489-6601-313d-abcc-c2a566d471f5 | -14.31426 | -51.55625 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 63a66fae-575a-3c76-b0a8-fce21abf6354 | -19.86551 | -42.44588 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f3dffd6c-25d3-39f4-87f7-1e72cdbe41bb | -14.27551 | -51.56236 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fe2ddd8-10bc-3f79-b520-0c2266353e34 | -15.76816 | -43.75308 | 2025-10-13 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af45b2ae-2136-366d-b320-c3839fea7d21 | -15.79298 | -43.26208 | 2025-10-13 03:57:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfe218cc-135d-3b28-8818-91f0c9988783 | -16.12436 | -53.97412 | 2025-10-13 03:57:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e19dbf8a-f46a-3d8b-8224-d114fe1cf262 | -14.30189 | -51.54402 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d10fba8-0ce8-31c1-a938-29407ae98fc3 | -20.84309 | -42.80505 | 2025-10-13 03:57:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 37354713-278a-394d-a63c-e8aedb56cb78 | -16.35204 | -42.38488 | 2025-10-13 03:57:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1250a62-1e5c-3b0e-b97a-d6ae9684af99 | -15.66429 | -43.9031 | 2025-10-13 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3759a5fd-ba4e-3d57-8838-4d5f1c726e35 | -14.19235 | -51.50149 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ee71330-bb1e-35b0-8663-ef907fa23066 | -17.3475 | -42.46873 | 2025-10-13 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 64655dcb-60ce-3c8a-9b4d-22acbf86ddb5 | -14.31382 | -51.54659 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56210b0e-0b5d-3ba0-b7ba-b51f44ee2e75 | -17.3343 | -53.80192 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b051455-7fd7-3da1-ad43-54fa66585c4e | -15.78087 | -43.86075 | 2025-10-13 03:57:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b406446d-11bf-37fa-b023-78aec577c30f | -16.31416 | -43.09923 | 2025-10-13 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c7a9800-66a8-3fa5-bb3a-5b39ca5f6233 | -14.94419 | -46.72106 | 2025-10-13 03:57:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86719976-0e28-3ae5-9b9e-febc199791d0 | -14.30786 | -51.54531 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7acbd453-99f1-3227-897d-eb7c5e613bc2 | -15.02636 | -48.74631 | 2025-10-13 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f964dcd5-7404-3e01-abb8-e7a207053471 | -14.20671 | -51.51118 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d744671e-5400-380d-a4b6-93ab7e16a445 | -17.33289 | -53.80817 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 050f2476-c1a0-3c48-b705-0b3c5d95de0d | -14.18881 | -51.50734 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a74a96d7-2319-3f68-8c68-6487bc547437 | -19.86955 | -44.16582 | 2025-10-13 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f60f8951-ac95-32f3-b7f1-4936729bc093 | -17.32649 | -53.8065 | 2025-10-13 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dbab53c-b491-3d30-aa46-d4bbf725bc44 | -14.19291 | -51.51776 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 718ca2da-d6d7-333e-b9c4-1d9ad52223e0 | -19.86187 | -42.46832 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c515307f-539a-3dd6-9b16-fac9429b67ee | -14.21267 | -51.51245 | 2025-10-13 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9dbabb96-d10e-3b67-8b68-88e05575cf49 | -21.1108 | -43.10567 | 2025-10-13 03:57:00 | NOAA-21 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2289a890-8490-3408-89d2-4cf859cf5079 | -19.87305 | -44.16646 | 2025-10-13 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 738d5e13-b7c6-3725-9b10-932d261c142e | -16.16867 | -42.85 | 2025-10-13 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2dd3c57-9b04-38f1-bd2f-44cf4b51cff2 | -19.8652 | -42.46891 | 2025-10-13 03:57:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README15.md)
