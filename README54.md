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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9814be8e-7ef8-3d99-8d6e-18e1acb1849a | -3.26782 | -50.40209 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 969637df-1707-3bf2-a5b5-af7d490700a8 | -3.50906 | -51.686 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4799a8a1-917d-3368-b638-53237505f936 | -1.07791 | -46.58038 | 2026-10-07 04:19:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0e733fe-a23b-3c84-942d-78e0fdd31abf | -3.36449 | -43.39454 | 2026-10-07 04:19:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 231a2d34-8976-3973-b850-46b6f06948fc | -3.46574 | -49.93884 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5c2053e-23b0-3e17-beb5-967ceef6ea7b | -3.09397 | -53.72942 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 240f8fa1-6552-3e6d-8a67-f3079c39e7aa | -6.38096 | -45.05403 | 2026-10-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cc6a141-b2fc-3278-9612-2c7a4a577d5f | -3.53526 | -54.65995 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8c9e0659-7799-3597-afd5-4194a505428e | -5.11146 | -45.88476 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52b2648e-aaae-30db-8436-8bbb379f0d4d | -3.2704 | -50.40325 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f583dcc4-8f83-357f-bae2-a0cbf8e0caf3 | -5.015 | -50.94003 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f079753-ad01-34f6-8f64-e75367432813 | -3.80601 | -51.03452 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c91ecfc-2274-39a5-b958-76d3aa879a44 | -3.02169 | -53.89941 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac33e03e-dc22-345a-9b81-2864aed128ae | -2.97987 | -54.13497 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58a9afdf-2c04-390f-a0bd-2bcf4afa8801 | -3.50146 | -51.69849 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 562fe182-06bc-3587-ac94-536386ae8cc4 | -4.7577 | -45.76877 | 2026-10-07 04:19:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 818c9078-1092-3293-b0ec-1474bd1d0676 | -3.10511 | -53.7749 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| caf9e608-d269-331b-b2e9-23b834c7064e | -7.75966 | -43.81021 | 2026-10-07 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3147247a-1239-3633-b0b8-447d884704c3 | -4.30406 | -50.78414 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23134673-b636-356a-bf66-deb047a4e07f | -2.77149 | -54.08159 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 14dc505a-4284-3eb7-9aff-54b8ebea9655 | -2.7677 | -54.0876 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d141bd60-0990-30cc-ac30-2fa9250aba55 | -2.77831 | -51.67904 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06268e61-4f51-3868-ad4b-3a67156b0030 | -5.23975 | -50.92041 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e5c2591-1e81-3fef-9703-59f3020635a0 | -7.86724 | -44.15925 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e281d29-5f26-39fe-9f08-38a0be407f6e | -2.76105 | -54.10569 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 13a16774-fcb5-3ccb-8278-2a43eec503bf | -2.99837 | -51.009 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80c32960-28bd-31d7-97c4-bb47bb23c50c | -3.27014 | -54.02595 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 732cd174-33ef-33a2-915c-c8b5fcc65f06 | -1.25513 | -49.05207 | 2026-10-07 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 480d77d9-ac54-3ada-bab9-0b82dbf4a279 | -3.28748 | -54.07429 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 567824c1-0dff-38d7-84a7-53c78c49a11a | -5.97602 | -40.91738 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1456ac17-a665-3aaf-b15f-99cd209b525b | -3.80504 | -51.04038 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38fc5f25-0ded-37ee-9712-706c6a1fa2fe | -3.26695 | -50.40745 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc0f6393-a1bf-3ec1-af9c-8cd176552691 | -3.08235 | -54.16144 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a6e4b6a-ce4d-330e-b870-9fcffa960b11 | -5.97077 | -40.92836 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4fca57b3-5e3f-3d3e-9ae7-b99e3a402198 | -7.82095 | -46.8631 | 2026-10-07 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 141a06aa-1083-340a-a486-98e67bcaa0d4 | -3.30765 | -42.27591 | 2026-10-07 04:19:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8f02a6a-b8e6-38ec-85c8-fa4d88246149 | -3.50203 | -51.69516 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42c047c2-15d1-38e9-9a15-d890df7f23f6 | -6.60443 | -41.58392 | 2026-10-07 04:19:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed3ce735-31b4-39d3-8bd0-27702c0e6b07 | -5.99938 | -53.51173 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23dcd44d-e336-3357-b04f-e250bbe4feb8 | -6.12187 | -53.05378 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a49cb4ee-c5d3-3f33-ac7d-95582ce2a888 | -3.49944 | -54.64417 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0903373-fb68-3a32-82b1-9d2ab4b8dcc8 | -4.51521 | -42.88967 | 2026-10-07 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ff64ba52-e711-330c-a695-eaeab91ac9d3 | -3.09768 | -53.74453 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a338c2db-1ec3-324e-8afe-7bda6b51850c | -2.99132 | -54.10595 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 447261da-aa34-3e5f-aa02-4e3ddafa88f5 | -6.43629 | -39.33729 | 2026-10-07 04:19:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ff13702-7560-3775-b681-33e180e914ce | -8.18462 | -45.14031 | 2026-10-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4a7220e-46cb-3a00-9e26-dcb1835349ee | -3.59073 | -54.57415 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 006f76cb-fd1c-3d26-a081-8b40a045cb06 | -4.75435 | -55.6546 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f745ba2-6ea6-38e1-a551-864d9fcb4c98 | -6.23344 | -41.98559 | 2026-10-07 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 9fd43433-920c-334d-9003-7168fd557f19 | -4.76089 | -55.65651 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbaf08d7-a861-3de5-8b3c-cd873e917168 | -4.28593 | -50.78181 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a133fcd9-63c4-3dd3-b8d1-7351b1507dab | -3.4988 | -51.69013 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 451f2988-2c24-3dd0-8608-7c4b43824659 | -5.41496 | -39.10946 | 2026-10-07 04:19:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 574d48cf-27b2-3005-8a2f-7d49229c5e04 | -3.28706 | -54.03897 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 67e7043e-a02b-3934-b954-e9b3fa2006b7 | -3.0787 | -54.29472 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 59a5fa0c-ba22-3b3e-b03a-4cac826d3348 | -4.04522 | -50.9835 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 457c28bc-3942-367e-a5bd-682d5a1d25a6 | -3.5021 | -54.6664 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e582d958-c2f7-3b7d-a394-1333983b46f2 | -3.05203 | -54.15044 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8247ac0e-486d-3356-97ee-809f69515fe2 | -3.28332 | -54.02341 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 833d11fb-16b5-3777-adfa-e2557afbd31c | -5.75808 | -45.2805 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 940e17b4-62cf-36a5-ad5e-e8adb664173b | -3.27554 | -50.43204 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca703691-45e9-35a1-b3d1-263d3868e6b5 | -8.21125 | -46.34464 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d09a9841-f319-3c61-b697-a57460978f9a | -3.09713 | -51.38292 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f67b090f-aa52-38fb-b9e0-bed850469cf1 | -3.07501 | -54.27847 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac677c34-70f0-3ea0-9f0d-51e55608532b | -7.87551 | -44.19281 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| aa47e53d-accd-3837-95a2-0726309b5716 | -1.29165 | -54.56564 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7717ae43-b68b-3a1c-a5b3-6e5c056ff022 | -3.27065 | -50.43123 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81d1199a-4d11-3ae2-99b9-be71a164029b | -6.87335 | -43.67922 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4300e88b-78f1-3b9e-8b4f-7ea352d894eb | -3.17295 | -50.44671 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39d71f77-ce01-3407-b37f-fd5211a20300 | -1.28066 | -54.5608 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b68e9a4c-ff4c-34f9-bccc-03e9fdec34f6 | -5.05184 | -36.94162 | 2026-10-07 04:19:00 | NOAA-20 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ac5c9a0e-9086-311a-93d3-7814811f020b | -3.38802 | -42.71146 | 2026-10-07 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45363800-fef5-3622-bf53-ba07de2094cf | -5.74046 | -41.66414 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a9b3b43-9891-3f74-abac-3bbe4da1bdec | -6.14836 | -51.73127 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 653e7747-1acb-3ece-be5a-cca68a88b118 | -3.52236 | -54.66392 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad32a4ee-518b-3783-bbd4-3e206514fafa | -5.97829 | -40.92559 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9a4f80f2-add2-3793-9865-d0e31035b866 | -7.27498 | -46.15281 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 50050d2e-1fbd-394a-b548-e7f8fc401618 | -3.52144 | -54.66914 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd61b263-4b02-3327-8aa0-cd051d5709bd | -5.67952 | -53.49524 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5f4a0f4-e4aa-3784-96bf-1583126f3387 | -6.89266 | -43.68583 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc848a72-63d2-34dd-b6b8-c28d8d042afd | -3.58073 | -54.31301 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeb3f7bc-2bdf-3ca4-9943-f4fe301160ab | -2.76422 | -54.10773 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 75ba5022-6448-3331-bb11-979414c25e99 | -6.3344 | -46.94894 | 2026-10-07 04:19:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbefa33b-ce92-333f-b364-8069e0b3abe5 | -3.09868 | -54.17887 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bc7473c-1a69-3b27-ba21-90d2cd2060f6 | -3.5032 | -54.65433 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc02da69-3233-3a6a-9420-b52006b789cc | -3.27577 | -50.14146 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| efd26604-a3a8-34fc-a315-edd2aca6eb94 | -6.14097 | -47.93633 | 2026-10-07 04:19:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ec9fa8c-c845-32af-b34a-633f03831fa2 | -8.29897 | -45.47049 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddce88ec-35dd-3293-9849-4ffba7030e04 | -4.15613 | -55.15539 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 575aa719-4a41-3543-8c7d-f127eeee84b7 | -5.27479 | -45.72908 | 2026-10-07 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64c9e13a-c461-37fc-b9c5-08c9743571b5 | -3.10742 | -54.16553 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 695b7edc-d491-3006-a1d5-c62aec5a7c1c | -3.18388 | -50.57462 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37ba28e1-19ca-34bf-93e3-a86ee8c738a6 | -7.99347 | -45.49338 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e751861c-f125-33d4-8785-c63b73c62c40 | -6.15239 | -51.73833 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a090bf5-b961-3d19-9980-94ce60e29fbc | -3.04013 | -53.93384 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed80b89b-6a9c-30cf-890d-63a1105a8373 | -3.07508 | -54.25957 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5207a52c-838b-3ddb-86f0-4215fb38e608 | -3.99142 | -56.25912 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd59d49b-4b1c-3f04-81d2-3e9c27b1e12b | -2.77221 | -54.09881 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 23ee4892-e6c3-3786-91aa-4615e5f62f95 | -3.70187 | -50.98168 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17ffb67a-26be-3e33-80e1-9b45c62a34df | -6.8334 | -52.19677 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README55.md)
