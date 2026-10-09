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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ace672e7-49af-3371-9aa4-1a1a3efc7023 | -3.5676 | -54.6946 | 2026-10-09 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 5c5bda85-f937-356c-a38f-15e4cb2760b3 | -4.2768 | -49.0816 | 2026-10-09 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 5bbd92f5-523d-32b6-88c4-162da7f6d740 | -3.0925 | -53.9455 | 2026-10-09 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 4446754f-2ba8-3e42-97fa-39749539a758 | -13.2018 | -54.3551 | 2026-10-09 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 3074e540-5626-3728-bae8-53f50dd5d45b | -4.6096 | -49.2156 | 2026-10-09 01:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f36f3e0b-450a-3290-96ec-9cbcda1573f7 | -2.499 | -56.0675 | 2026-10-09 01:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 87ea9f35-1fc7-3fc8-9581-b6773ddb7d5a | -3.1101 | -54.1661 | 2026-10-09 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 3a34a9ba-55fa-35e9-bebc-04f0535bc18f | -4.2953 | -49.1021 | 2026-10-09 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 2afbf839-cead-3a1c-b3bc-ca39b8b266fb | -12.0058 | -43.464 | 2026-10-09 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 7b31d71f-3fbd-3d7e-a219-fb472722db59 | -4.6282 | -49.2147 | 2026-10-09 01:10:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 94274bd9-b119-3b69-8bdc-18c35091fa34 | -8.742 | -45.1563 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 272.9 |
| ea2be125-19aa-337f-98be-ff6a2852081d | -7.2367 | -55.1406 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| d8e89f6e-2bb1-3a5d-b5f0-d591927d9ad7 | -8.7423 | -45.1334 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 314.5 |
| 785fa123-4821-34e6-a7ff-660016768574 | -18.6464 | -41.3443 | 2026-10-09 01:10:00 | GOES-19 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| 371ae067-b8a9-3fa1-98cb-80aaff13b57b | -7.2366 | -55.1606 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 97da86dc-9297-342e-b871-ab1147606f53 | -3.1787 | -50.5807 | 2026-10-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 8e8bd9ca-01ae-3c4a-9e30-7bbd38ce53e5 | -11.6173 | -43.7142 | 2026-10-09 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| b5cc78db-8a7a-36c5-b9aa-45ab8d10e812 | -12.0054 | -43.4878 | 2026-10-09 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f359368c-cc24-3d65-b1d9-f0321e701622 | -6.4949 | -55.2995 | 2026-10-09 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| b829ee6b-003d-322f-b845-460a3ac2b3ad | -6.0021 | -40.9594 | 2026-10-09 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 349.2 |
| 2689adf2-93cf-3776-8186-d0747a39b36b | -3.1787 | -50.5597 | 2026-10-09 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 505a0730-e4e1-3bc6-8740-15e92cf5b2cd | -11.7601 | -61.0743 | 2026-10-09 01:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| fe00cb53-0a4e-3ed9-b373-1b2b2cc3fe8f | -1.1094 | -54.1601 | 2026-10-09 01:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7091ce57-8c45-3685-a5c9-38b17452d5de | -6.7365 | -55.1474 | 2026-10-09 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| dd83ca25-f6e0-35b7-8817-1d3ff120c137 | -6.0024 | -40.935 | 2026-10-09 01:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| be16930b-4403-36b7-ab11-15087d42bbb0 | -3.0007 | -53.9075 | 2026-10-09 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 80b73793-3724-3408-8083-4a649279dece | -3.9912 | -59.356 | 2026-10-09 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| db55a608-e7eb-3b00-b97c-6c226d00ed98 | -3.1109 | -53.945 | 2026-10-09 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 1b6d27b8-55f3-3795-9439-9007633a5083 | -3.1285 | -54.1657 | 2026-10-09 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 4000168b-1bbb-34bb-a017-a1fcedabea17 | -12.2346 | -57.1071 | 2026-10-09 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 83b5e43a-2edc-357f-8a36-030ada6c7484 | -8.7417 | -45.1791 | 2026-10-09 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 9028c7c1-a563-348d-9252-3813bff75faf | -3.0002 | -54.0684 | 2026-10-09 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ff24c8e9-f070-3d9a-9986-1f1fef0ed49b | -3.5677 | -54.6746 | 2026-10-09 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 03915c79-e995-3bfe-a4a4-6982cd8f34f8 | -8.91 | -45.23 | 2026-10-09 01:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ef676e8-6680-3977-ab09-8e3de7f1253d | -8.88 | -45.23 | 2026-10-09 01:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c3d6e0c-86ea-34bf-83ba-85f8f576da8c | -8.73 | -45.15 | 2026-10-09 01:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2ff07ff9-2032-3f18-b0bd-c6d4c299d6bb | -5.99 | -40.97 | 2026-10-09 01:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ebe651d-d19c-326f-b6ba-d78641589d2e | -12.2346 | -57.1071 | 2026-10-09 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c884f75f-933f-334c-83a4-fbc3ae2f9445 | -13.1636 | -54.3591 | 2026-10-09 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| eed59e71-db63-311b-a149-10430a7dbd5e | -8.9299 | -45.2269 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| f3e61adc-1ad4-3afd-af3c-e63cfad481cb | -2.7428 | -54.1146 | 2026-10-09 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| b0b9e553-28d9-3d6a-a488-d0dbd469bc72 | -3.0007 | -53.9075 | 2026-10-09 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 1f790659-bfb2-32a1-b656-a1f46e752286 | -12.2156 | -57.1087 | 2026-10-09 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| b95ea6df-9d67-366e-8868-babb09a59878 | -5.9833 | -40.961 | 2026-10-09 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 571812a4-d81b-3600-8ed6-61671adda5fb | -13.2018 | -54.3551 | 2026-10-09 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7d1bfa59-712c-3b4b-bd1d-6b3d7ab86274 | -3.364 | -50.4072 | 2026-10-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f582b8c3-3cd8-3eff-9c3a-fe7198a5ca51 | -8.8921 | -45.2311 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 34d53607-85e3-3a3f-b333-4ea49417e098 | -10.6199 | -60.4852 | 2026-10-09 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1cd398d1-5e38-3861-a980-e9f633ca7f5c | -3.5493 | -54.6951 | 2026-10-09 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 63c43014-e1b1-3e66-bab0-d1369b3a5f5b | -12.0054 | -43.4878 | 2026-10-09 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c700fce2-e590-3884-8352-32871a7366e6 | -3.1101 | -54.1661 | 2026-10-09 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b4e81b58-301f-33a4-9961-8ad86cb48e0d | -7.1995 | -55.1627 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b604555b-3a3d-3dda-8d27-8032ff6a7ab8 | -8.7234 | -45.1355 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 258.1 |
| 0603c5e6-39ab-3776-9b89-fa6cb4c84de3 | -7.218 | -55.1617 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| e11a47dc-c935-3f3d-bd2f-7a391902bff6 | -6.4903 | -62.8554 | 2026-10-09 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| addcfc81-3850-31e7-8bb4-b5e3eeb56263 | -6.021 | -40.9577 | 2026-10-09 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 153.9 |
| 00c6bf24-bdc5-34b7-9a27-1a92b01a3198 | -3.9912 | -59.356 | 2026-10-09 01:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fa551914-4fa7-3208-9f10-1c8fe2f5418e | -3.1284 | -54.1857 | 2026-10-09 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 96f93150-42c4-3e24-b7b8-c68e3c7a654a | -3.1787 | -50.5807 | 2026-10-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 055d46f2-6183-3b50-b186-a2bd43b48e6c | -2.499 | -56.0675 | 2026-10-09 01:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 937f6234-5897-3894-9068-0db14e391831 | -8.7423 | -45.1334 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 1ad75cb6-ae1a-3c1f-8116-97d7a94ad41b | -4.2954 | -49.0807 | 2026-10-09 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 35492232-d87e-3b1a-9fd5-e05de52e9b1e | -7.2367 | -55.1406 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9a203543-eccf-3783-9b1d-d8d0c98d1efc | -13.2015 | -54.3757 | 2026-10-09 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 77a4dc2c-c7b3-3185-8ce9-d3b1aeeb518b | -12.2158 | -57.0887 | 2026-10-09 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.8 |
| e1390f88-da02-3bba-892e-529248e8dd15 | -4.2768 | -49.0816 | 2026-10-09 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| dd5c0ae2-cdbe-36fa-90e5-34c08db27d31 | -5.6934 | -53.4667 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 31cfd476-bbfa-3f78-a611-16872d7487f2 | -3.11 | -54.1862 | 2026-10-09 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6e03a90b-11ab-33ca-9ee2-837644fad8b3 | -8.911 | -45.229 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 0bf8cb93-d325-36d3-864d-0cedb475bd43 | -6.0021 | -40.9594 | 2026-10-09 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 504.0 |
| 5d8b5f6f-4ee4-3e31-853f-7a64d29644d9 | -13.1668 | -43.2673 | 2026-10-09 01:20:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 151f7247-44df-3ee5-82c6-87fc1be30b91 | -11.47 | -43.3824 | 2026-10-09 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 35760ccb-c689-3b86-9b45-6aadec779c1b | -6.7365 | -55.1474 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 93a34613-e926-3d6e-b94e-d10d228f0113 | -4.2953 | -49.1021 | 2026-10-09 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f16ae352-d6b1-31e3-a654-9539be438a99 | -3.4396 | -54.5382 | 2026-10-09 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 30b557d7-5005-3f65-8985-1328b8fe8e91 | -11.6562 | -43.6846 | 2026-10-09 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 1df285c4-7a9a-3d4b-96f3-5957de923a9a | -3.5493 | -54.6752 | 2026-10-09 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| b6675edf-12e7-31c4-a8f7-140add2dc67e | -3.1114 | -53.7839 | 2026-10-09 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| dc2862fe-4677-3729-852c-312bad4e4b70 | -11.6369 | -43.6876 | 2026-10-09 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 34496cd0-feb7-3670-82cd-27ae670535b7 | -13.1827 | -54.3571 | 2026-10-09 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| f2f2e46c-d177-3ba2-a501-dad465f24c34 | -3.1786 | -50.6016 | 2026-10-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 87646129-488a-38cb-a7cd-ad574e099622 | -13.1639 | -54.3385 | 2026-10-09 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 37fae34f-d4ed-3574-bdd1-3fe59be3336a | -3.1109 | -53.945 | 2026-10-09 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 1037ea75-85e5-353f-ba9c-85b6105e301e | -3.3455 | -50.4078 | 2026-10-09 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7d79fd86-90bb-32b9-b632-7060dec3d2b5 | -8.742 | -45.1563 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 0668de02-ced0-3502-a51b-2146ab5960bc | -8.7231 | -45.1583 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 256.5 |
| 2910ef18-1d33-3794-bdf1-1ebc6ffc124e | -8.9107 | -45.2519 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 9236d527-6611-3024-b77d-7e8a0ad30dd4 | -6.0019 | -40.9837 | 2026-10-09 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 194.2 |
| 2064ff28-4433-3390-9888-13e2b0c4a515 | -3.0925 | -53.9455 | 2026-10-09 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| b90e2ba9-1772-3401-8184-d50c3e00d90e | -4.6282 | -49.2147 | 2026-10-09 01:20:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 69ebaab5-7f8c-3adf-8fbe-10f0ee9084eb | -8.9113 | -45.2062 | 2026-10-09 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 6cf2c6f1-d16b-35be-841a-83fcd4c9763b | -3.2577 | -54.0217 | 2026-10-09 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 987611a4-321e-3c55-9130-ec1b3d0173e0 | -6.4948 | -55.3195 | 2026-10-09 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| baad56fe-fd70-384c-ba7b-bae94e1f178c | -5.6932 | -53.487 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 92f5e4f7-4ed2-3ba2-b15a-973dbc7a5f51 | -11.7603 | -61.0549 | 2026-10-09 01:20:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f6f89e17-564e-3d3c-872a-6efad3663cdb | -5.7116 | -53.5065 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 308dea03-e416-39bc-b125-be396a1f8357 | -12.0058 | -43.464 | 2026-10-09 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| baa93192-6551-3409-9c01-85d29f7a6268 | -12.2154 | -57.1287 | 2026-10-09 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| ad3a8fd7-7b77-3019-b85f-06cc8cc4c95e | -6.0024 | -40.935 | 2026-10-09 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| dd2275ca-a503-3867-8326-885ddca7c969 | -5.7117 | -53.4862 | 2026-10-09 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |


[Clique aqui para ver as próximas entradas](README48.md)
