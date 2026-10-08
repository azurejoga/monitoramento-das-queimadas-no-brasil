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

## Dados Diários - Página 325

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26e16530-41bd-3a26-b593-73b330f5cf92 | -9.33834 | -48.34618 | 2026-10-08 16:37:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b0ca35d0-7c7c-3cbe-9ea8-f65b82f313dd | -11.27387 | -45.19498 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 28d79672-ffb6-3918-b903-2f080412518b | -6.98031 | -47.67807 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0bda28c1-3782-3274-a53e-6f8ddc29532b | -5.74803 | -41.59759 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1036810a-3603-3669-b040-f44bc05822eb | -7.31268 | -44.00386 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1ac9396f-be60-3e0a-ae22-277677986921 | -11.21098 | -47.71726 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fc52b46a-576c-3711-9446-f9b2d6adb162 | -11.25072 | -46.26111 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3b640aec-2538-3391-9017-a2078766bfcd | -6.92952 | -43.06525 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9000151b-0552-37b8-9503-82d5e73c0e26 | -18.97932 | -44.45753 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24bd81a5-963b-3925-b468-90a21b7c9280 | -7.07063 | -47.39365 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 14dca22e-6517-393d-8a0b-3279bea120e8 | -7.48037 | -42.79374 | 2026-10-08 16:37:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| b3ea109f-743a-392d-9f25-6cedee2bd83c | -6.82969 | -39.56079 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f0a9dad2-8f45-3c33-b677-bfc74cbfff34 | -8.93214 | -45.16881 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 29619abf-6b83-3640-832f-16cf3fe012f8 | -9.0989 | -45.12699 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 2c22820f-05c1-3125-99fb-625823507013 | -6.70594 | -45.28028 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5f9b1f4d-4b3b-3ffd-a2fd-da9267958545 | -6.88218 | -38.54976 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 10.6 |
| a8638dd9-03d5-3800-bb53-ccdfb8d2f9af | -8.65887 | -54.53162 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9a1548e1-a2b6-392f-8719-14f5b113b603 | -12.24729 | -44.74679 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 1a53d637-341f-312c-8b20-74db7a7affb5 | -10.76683 | -38.72552 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 03f6947d-3b65-36c2-ab9b-46029bcc310a | -6.91141 | -45.46868 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27a92f17-67d9-365e-9f6d-04d1479e1955 | -8.34886 | -47.66562 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 117941cd-634b-3718-9fe6-e3848849fa17 | -19.02174 | -44.34644 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55831629-343b-3403-9038-8ea095cb51f4 | -7.48549 | -42.82623 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f122342a-93fa-3e07-aa0c-e49c09c4f7b4 | -8.61628 | -44.87974 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 9de3bbee-7225-3d6a-8fe3-a31d9ccee104 | -11.01571 | -45.43861 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c632db98-3510-3b86-80ed-b6ffa1399afe | -5.49876 | -40.53598 | 2026-10-08 16:37:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| bac34864-5267-391c-a15b-4e270309371d | -9.14448 | -45.82713 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8d01ad85-fa4f-302c-90f5-e0bf32ebb2a4 | -6.98474 | -43.96901 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7dbe7965-ae77-30b8-b833-dd6ade95e4af | -8.30227 | -45.73207 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1e61d24d-3f5f-39b9-b80b-4def44680885 | -6.95198 | -44.89619 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5121e5f5-0e12-3ea9-8efa-b8f7cc8d2a60 | -8.29632 | -45.71519 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 8f7827ee-f01d-3e76-9115-7cad406b3db8 | -5.75425 | -42.07329 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 1bab3bf2-7482-3822-a92f-159591057985 | -17.61439 | -42.08787 | 2026-10-08 16:37:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4e74b773-629a-33e3-85c2-eb69e05288eb | -9.19343 | -49.76568 | 2026-10-08 16:37:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 23de94a6-45cd-35bf-8779-5e11360b5540 | -11.07524 | -45.76612 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 341b5f07-5821-3c95-b774-f1480144240d | -6.32129 | -37.75338 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 5dedded6-1307-3d2b-a46c-0a62f9693fcb | -6.72633 | -45.1701 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 7d83057d-511c-3b41-a5a6-2a5305fad959 | -7.3366 | -50.82777 | 2026-10-08 16:37:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 4e6004cb-7a58-3ee4-8386-35d4dddcc70e | -8.0842 | -55.30059 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bfe87954-3d2b-32d6-ab91-c654d3b08d49 | -12.21829 | -44.82339 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 1164c011-722a-326d-a5f0-d99c04a876a4 | -6.67427 | -45.3607 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2680d95-8376-3404-8ee7-327194e2e448 | -9.77617 | -44.78519 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 49f5122f-0be4-36c8-b86e-a78c15ddd1a8 | -10.58396 | -41.20161 | 2026-10-08 16:37:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 656750bf-955a-3382-9b89-be9e8d6fd0f7 | -10.76986 | -46.53389 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dd661532-d0f6-3ada-911d-a9b5f3e6102f | -8.29407 | -45.72266 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 34f9aab8-6af5-3fa1-8351-f62a852b0bbd | -12.02611 | -43.4455 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 2f4b8a1a-1ff9-3d2e-ba54-742ad3fe17a6 | -7.07421 | -46.44769 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b857ffaf-08f0-3aa6-9f65-ee6b28e91bd1 | -11.86576 | -47.40182 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4d419670-3e73-3418-809a-04038c9191de | -7.1001 | -41.74078 | 2026-10-08 16:37:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 9f7e0c8b-7234-3b08-8a96-f992627baab6 | -18.13089 | -42.38729 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 130.9 |
| ffc86afc-3707-3689-973e-33ad0ffc5774 | -7.21163 | -37.75177 | 2026-10-08 16:37:00 | NOAA-20 | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 153eadc2-09dc-3194-afca-c60950356366 | -7.75518 | -54.95027 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7116cb19-af30-3ac4-81cf-f02bd1151dcf | -13.22166 | -54.50143 | 2026-10-08 16:37:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f7d00dd4-7f50-3287-971e-55441dfb8020 | -6.93437 | -43.67 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 84ae8e4b-ba7d-3d42-aaad-22b02c15df40 | -18.05076 | -44.56408 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5a639a11-5229-3919-85ee-2f801b1b90af | -14.00653 | -48.75104 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 93a0bf33-1ec1-3ebb-a2fd-84d76c0d4b91 | -11.68678 | -43.68921 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 65d02213-15e5-38ed-ade2-d738b18a3620 | -9.90321 | -45.19415 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| d939baa6-0e2a-33a9-82f0-c64240d390d8 | -8.32213 | -45.46248 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bd812c5d-4e7f-3037-b069-fd573c8e14af | -6.97922 | -47.67072 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 99ac4ea8-96e3-3521-8580-89d915f285a1 | -9.0095 | -50.85518 | 2026-10-08 16:37:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a64669dd-8700-365d-a8fe-68cf679552b9 | -6.46634 | -44.98149 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d017ce0a-f705-3a7b-ab65-33c8d5dde938 | -7.05805 | -44.32835 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9cf56d64-30a2-315d-84ce-a87c428e251a | -10.52105 | -47.314 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3b8fd05e-8dd2-358c-a95c-dad4712ee911 | -6.32862 | -35.12498 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 914e0d00-e07b-359f-b30b-90b89e2918d9 | -10.45405 | -47.28118 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2fa96998-5a69-3422-877e-6665ce94f882 | -10.93265 | -45.38337 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| c9a3bb4c-27ce-3e0f-8780-8c7a63f92ef3 | -8.06538 | -45.60253 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b78857d6-37ec-3daf-b307-36776bd298de | -10.15922 | -44.67279 | 2026-10-08 16:37:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| b080130d-9d05-3fa2-9a8b-77dd473a3bac | -6.81681 | -45.05192 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 8d944c22-d02f-37f8-be30-a52af75506ca | -11.07973 | -44.01966 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bd5dd955-9dc9-347a-9ff1-69ea8fcf5449 | -6.1545 | -39.43333 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| fd16bf13-bde0-34f5-b467-3b7c48d55bf0 | -8.2128 | -46.32882 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0df0a9b8-e0bd-3458-982d-0a911312964f | -8.84123 | -45.46115 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7c86b3a4-a83f-3708-ab7f-bd36cb80937c | -18.34028 | -42.38029 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| db67d633-4a54-3158-973e-69f78d9fa2e7 | -5.99185 | -40.93631 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| fa34e84f-8bd6-3abb-b1ac-b2fdeebc259e | -11.46306 | -43.38575 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| c84114f5-ff45-3ace-a637-79281c31705a | -6.97648 | -45.11893 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 011602fb-c241-37ae-b381-0fd053246915 | -8.94111 | -45.13893 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 697f2450-7693-3e15-89e5-c435400f225f | -8.29513 | -45.7296 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 6657f9dc-bf1e-356c-bf1e-dbac0c54743b | -11.10748 | -44.00067 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af2f34d6-3f55-3769-910a-514865ba05ed | -10.67509 | -51.8894 | 2026-10-08 16:37:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 6ca567ff-eff7-3916-96b9-c411d3ad0386 | -13.20341 | -47.88315 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 02a6e751-5d36-3be7-b57d-d1f9ce908c6e | -8.59476 | -44.87237 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e5743836-c869-318c-a615-739191563898 | -7.61127 | -44.81221 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| be998df1-e4b4-3a2e-b197-ae93791b2aa7 | -9.36823 | -45.93836 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 13eb462a-4ed9-37d6-b442-34bca8074195 | -12.15305 | -44.75082 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bb93e8e1-889c-3c84-a11a-67af639bd6e6 | -8.39744 | -46.92727 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 367f60ee-53d2-3f28-9187-ad026c9af867 | -11.77691 | -45.58565 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 3ca628c1-a80e-3203-8819-0db7e7527fbe | -11.64611 | -43.68541 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 1c9dd69e-0512-3fc3-814a-af1ed196ccb4 | -11.07529 | -44.03492 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 2b2f0f97-46f8-3dde-8570-2f29580feff1 | -8.77213 | -47.26066 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 739a3ce4-3583-3ea7-bffe-e702ea337e9c | -7.70004 | -44.75083 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 843298fb-a3c4-38f0-922c-1f89b82c783b | -6.82502 | -43.68737 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ce61db90-b38f-37c3-9ab9-a66ce196b805 | -10.81421 | -47.33939 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 9ec86642-38f1-34eb-a126-6c937552cb64 | -6.79501 | -43.67648 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 031c01f1-0a77-3d34-8b2f-809b7c94157e | -8.84348 | -45.45369 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad46b011-19f7-309e-9f69-e421e3f398fa | -6.66924 | -45.37214 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 427.2 |
| 587168de-9cb5-3ef6-a3a8-8a7d4041a007 | -6.58778 | -44.86494 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 80ff3847-74c7-3030-9076-3828dfd5a25e | -9.93723 | -43.57606 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |


[Clique aqui para ver as próximas entradas](README326.md)
