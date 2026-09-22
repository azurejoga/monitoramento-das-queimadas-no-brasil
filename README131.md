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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52a31c5a-7744-3166-8ca0-2770eb4f3980 | -8.8105 | -44.2757 | 2026-09-22 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| cebf3aa2-70bf-3594-a033-701d0ab4a0ea | -3.7673 | -60.7339 | 2026-09-22 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 166.8 |
| dee6ffc0-d2cf-3894-a7f3-e967fbc12d3c | -13.9311 | -48.564 | 2026-09-22 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 137.4 |
| f76d7caa-2f92-3ff2-9e81-24c14f92a908 | -13.2791 | -51.7737 | 2026-09-22 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 443b43dd-ca52-38b6-a8b1-212ffe530a6f | -13.2979 | -51.7926 | 2026-09-22 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 4e4959ef-0f54-3064-9175-b95d8ff13b75 | -7.0349 | -44.6625 | 2026-09-22 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 85e5df22-015f-3e07-9876-58b445a56826 | -9.5542 | -47.9549 | 2026-09-22 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b26605b8-444e-388e-9e14-12dfb38c1e7c | -12.2827 | -50.7226 | 2026-09-22 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 30bfd0ac-e8a1-376e-845e-2cbfa32da861 | -9.2759 | -46.1852 | 2026-09-22 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 44568d9a-73f4-342c-ae60-6070c5036442 | -11.7079 | -50.9811 | 2026-09-22 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 1347a068-de79-3374-bcb6-1aad5a69d22e | -3.5654 | -43.4727 | 2026-09-22 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 107d01e4-2fce-3b9b-854b-4fbc0eacf769 | -10.5558 | -46.732 | 2026-09-22 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 1cc7e166-4fb7-3f74-a34e-9b1bf448d2d8 | -8.7919 | -44.2546 | 2026-09-22 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3e113637-ff29-3e1a-84f8-20b798f604b9 | -8.2574 | -55.2604 | 2026-09-22 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1c405d25-90a2-34e4-af37-290513787bb2 | -12.0836 | -50.0378 | 2026-09-22 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| fce1fa4f-a9fe-3fcc-9c34-f423486a7b37 | -6.2761 | -47.6287 | 2026-09-22 13:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1ee54e9a-58cf-3c76-a1af-44494787a387 | -3.4599 | -59.54 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 931237b6-7242-3f97-b891-f8e378ca0b5d | -13.2983 | -51.7713 | 2026-09-22 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f99f6ecd-6e3e-350f-8fcb-4f6a4c58fa39 | -11.4213 | -47.338 | 2026-09-22 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 2b20e386-471a-3bac-b18b-be17bcbb5484 | -10.9112 | -53.9635 | 2026-09-22 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b3d9c01d-5a00-3f7a-8dea-823686ee0ce9 | -13.5134 | -51.5105 | 2026-09-22 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 910928fa-43a4-3d4c-9e9d-0b186c0fa70e | -7.0352 | -44.6396 | 2026-09-22 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| b4fb9632-5812-33f9-9536-3430dae1b6b9 | -8.7916 | -44.2778 | 2026-09-22 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 222.0 |
| f62d5166-b463-3336-8d40-e7ef4049dff2 | -11.6793 | -43.4684 | 2026-09-22 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| b72f0327-3ddc-301b-b089-e2d9baa9f4d6 | -7.1203 | -43.7323 | 2026-09-22 13:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| d6937a9b-8e62-3362-966f-dadcd87c8d51 | -8.3761 | -47.3023 | 2026-09-22 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| d47e30ab-0937-39d7-aab7-d0dbe4b73198 | -11.0052 | -53.996 | 2026-09-22 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| e8db793a-e89c-3339-bf3c-8fbd9ecdd04a | -12.3484 | -50.1779 | 2026-09-22 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 208.5 |
| cd45ce75-3495-3dd4-934e-aa10fb7ffdea | -14.6688 | -45.6565 | 2026-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| ddc69be7-2695-3ca0-b666-07384d75a37c | -7.1557 | -47.4532 | 2026-09-22 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 38c798a1-62c7-3df3-9897-909a80a9d765 | -11.1563 | -51.0839 | 2026-09-22 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 184.3 |
| bad33595-ecb4-3a0e-9c8d-153ebdb7e30a | -10.4539 | -51.3038 | 2026-09-22 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c7f70c00-4944-3e37-b590-4137097868df | -12.1458 | -47.3974 | 2026-09-22 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| c73e7ad8-ce87-386d-a949-5f666897e488 | -3.4781 | -59.5396 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 5827f94d-9251-3688-a868-c7cc4b4a8752 | -8.5984 | -54.6139 | 2026-09-22 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 15dcf5fc-8eaf-3d86-86cc-0efd623b9881 | -8.6136 | -62.4981 | 2026-09-22 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0d14521d-d3b6-385a-b730-e5e050a0780a | -10.6878 | -50.751 | 2026-09-22 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d14b8481-1947-37e1-a7a1-90253b067aeb | -11.44 | -47.3579 | 2026-09-22 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 799d7e02-b5df-35f3-a028-0bffedef65ae | -11.4209 | -47.3603 | 2026-09-22 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 35dc974e-4185-3dd4-a936-46e07103a6f3 | -8.3764 | -47.2802 | 2026-09-22 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 403fa8f8-e5ab-3378-884d-40e2c8ae0ad6 | -3.2818 | -57.8491 | 2026-09-22 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| f55eb1ad-cd44-3794-b152-9d531f1db381 | -9.6111 | -43.9243 | 2026-09-22 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 19a21aad-c8f7-3508-93df-fe93a9ed09f8 | -6.3436 | -55.8243 | 2026-09-22 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 2359bd12-664c-375a-a32a-6e883f1053a4 | -14.6492 | -45.66 | 2026-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 0da9700b-2cef-3a1f-b5d1-8c78ff923fca | -7.2811 | -59.5159 | 2026-09-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| b9011464-16ce-313b-adb9-b4750ddd2cd8 | -10.5906 | -53.9918 | 2026-09-22 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a77079dd-752a-3d94-955e-1de22939cd56 | -6.2024 | -47.5245 | 2026-09-22 13:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| b2afc819-bc25-3775-8ad8-718fbee6984c | -3.7364 | -58.8626 | 2026-09-22 13:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 459f2fac-0606-348f-b5eb-9ba36fa3ebc6 | -6.2949 | -57.7545 | 2026-09-22 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| fcbfc873-2ea5-3881-a1ac-fd55d934576e | -8.6169 | -54.6328 | 2026-09-22 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 1af6be0b-7793-3ed7-87c1-69cdb386b12a | -3.4963 | -59.5775 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 09358baa-f193-34f9-be20-719eb7e841c4 | -3.405 | -59.5411 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d34e6799-4d0f-3d3f-9c3b-5370cfdadfe5 | -10.7437 | -50.8089 | 2026-09-22 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 0bd530ce-9c01-3140-95b2-669cf9e6a133 | -5.8678 | -45.2346 | 2026-09-22 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| aeaf67f0-85d8-3f1f-b0ae-0a8dbd6dcded | -6.1653 | -47.5052 | 2026-09-22 13:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7960e94b-78b2-37a3-9078-0aaf04b497ca | -10.8921 | -53.9857 | 2026-09-22 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 41369acf-b345-3b4d-8e36-8d746974cb0d | -3.3367 | -57.8673 | 2026-09-22 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0c6ac908-a470-3551-9ccc-fe23d2f177d9 | -14.6878 | -45.6762 | 2026-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 313.4 |
| b7730451-ae96-301d-9405-a5b1787d7420 | -12.6608 | -50.9549 | 2026-09-22 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0789a831-344a-3e2b-9643-dec4d6de791f | -10.8924 | -53.9652 | 2026-09-22 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6c796dad-65e2-350e-94bb-9ab98882394a | -10.5748 | -46.7296 | 2026-09-22 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 302.6 |
| f4e51929-21a8-3ae7-b394-af5a452455cf | -3.3867 | -59.5223 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 7cbc7286-3a7f-330b-9f65-b5c774c9b255 | -6.4486 | -59.9717 | 2026-09-22 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 9c765abd-4ac3-3599-94a4-e54f0104ab0a | -8.5982 | -54.6341 | 2026-09-22 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ae988e66-14a4-3436-8d44-0e1c90c45273 | -6.0925 | -57.6847 | 2026-09-22 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 354af7ca-49ca-387b-b9f8-88520e880542 | -13.8952 | -45.4913 | 2026-09-22 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 2335b346-d381-3919-a460-ea484366c024 | -3.3 | -57.8681 | 2026-09-22 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 5d10b5e1-d589-3ab5-a35c-03562a9897c0 | -8.6171 | -54.6126 | 2026-09-22 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 11049a6a-7e00-3a0d-a7a5-ae08aeebdef6 | -12.283 | -50.7011 | 2026-09-22 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 184b2da5-52cf-349b-b9cb-c2b044debff4 | -9.5833 | -45.8345 | 2026-09-22 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 086951ae-b304-3e22-8824-1984dff4e776 | -3.2817 | -57.8685 | 2026-09-22 13:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| e7e34561-eafa-3bd2-9de7-d8cb1485926b | -6.0172 | -45.2462 | 2026-09-22 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8659e802-8a5b-3a7b-af39-b9c025b24809 | -12.6796 | -50.974 | 2026-09-22 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3578cee7-5091-3e08-af4b-b31262530896 | -11.156 | -51.1051 | 2026-09-22 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| d35e40ce-d9a7-3099-b1f4-91c6a66e6beb | -6.384 | -55.285 | 2026-09-22 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 9558657b-c8cd-3456-b53c-452cc19b3760 | -6.9416 | -42.8834 | 2026-09-22 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 194.0 |
| dba69f96-535c-3610-99ab-ebcebf418e12 | -5.6007 | -48.2166 | 2026-09-22 13:50:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4391640f-4ad6-39ca-836e-484388ff9829 | -9.7883 | -46.0593 | 2026-09-22 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ddbc72fa-b65d-3419-91e4-ca21d2d4555f | -5.5717 | -42.7414 | 2026-09-22 13:50:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 847cf4cb-abb8-3323-a90b-c7d283663572 | -3.6065 | -59.4413 | 2026-09-22 13:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0b3df32a-58d4-3b51-b6c7-5328e1e9a070 | -12.1462 | -47.3751 | 2026-09-22 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1e3998a7-ed14-3e14-8b3b-bf038c4ad16e | -3.405 | -59.522 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 172.8 |
| ac69479d-d5e9-31cd-b818-a2783771eae9 | -12.3293 | -50.1802 | 2026-09-22 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 3a2e9f53-5244-32a4-9367-cf324381c9fd | -9.8665 | -45.8918 | 2026-09-22 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 3f9333b6-269b-3858-a67c-4b9d0552e525 | -5.7873 | -43.7758 | 2026-09-22 13:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 27431edc-6337-3c33-ba86-e7dd1cf20a3f | -13.087 | -50.6231 | 2026-09-22 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 936e3221-6097-3152-af27-45763144576e | -10.0295 | -52.0991 | 2026-09-22 13:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 854663fe-3b86-3593-901f-7973e64f1e5d | -3.7856 | -60.7335 | 2026-09-22 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 366.2 |
| aa7c7022-6461-31b8-9dec-b2057bd4ee54 | -8.6135 | -62.5171 | 2026-09-22 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e1b6ce62-7755-386e-9fe4-b8bd0d3c6822 | -11.6798 | -43.4446 | 2026-09-22 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 0a4067e8-654e-30d9-b68a-82f3d956e246 | -11.175 | -51.1031 | 2026-09-22 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 5352c28b-cbc8-30b4-b7c7-0f23943f277e | -8.7912 | -44.301 | 2026-09-22 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 6255105d-bd73-3650-98fe-5678c049f843 | -9.5356 | -47.9349 | 2026-09-22 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c9725dc6-2156-3fca-b959-3f56b8b256c0 | -3.3001 | -57.8487 | 2026-09-22 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 2d9e3a55-4d9a-3157-839c-b42a95183908 | -10.4536 | -51.325 | 2026-09-22 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e1fb6b08-99f2-3a33-9996-70c83553019b | -9.3797 | -48.3232 | 2026-09-22 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 9c2a83d7-6ec9-36d6-8a4d-5affdb3a54aa | -7.4765 | -45.4872 | 2026-09-22 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ab2280b3-22b4-3d04-b740-2c6f823b537e | -6.9414 | -42.907 | 2026-09-22 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 229.7 |
| 7f7fa998-7889-3d78-867e-151677cb93d1 | -3.4781 | -59.5588 | 2026-09-22 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 949961be-6155-310e-95da-c8f2b3619de4 | -9.788 | -46.0819 | 2026-09-22 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |


[Clique aqui para ver as próximas entradas](README132.md)
