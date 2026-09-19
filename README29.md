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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a5464e0-7ed8-3004-a675-784527517a4c | -10.1197 | -45.5639 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91f8f820-e9eb-3ee5-8f49-e652c62038bb | -6.97816 | -42.18457 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2c9cee3c-7ee0-3c5c-ae4e-1434b8955495 | -5.87926 | -44.97838 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5438a76-e06c-3a25-87a6-9353a4da457f | -9.95051 | -45.27795 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50c4107d-37f4-357a-8637-87bfae331ac1 | -11.19766 | -42.86207 | 2026-09-19 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 508978c9-370d-30c5-b493-ae0dbd1aa669 | -5.47097 | -48.99453 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 751a01cc-dc56-34c7-b41d-cd4db418bf62 | -6.31848 | -45.60938 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55ec9693-46fd-30ff-9c42-482f537d063c | -7.67016 | -46.12523 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8b6a2ab-f2a6-3e92-9ed3-595033c5de29 | -8.60818 | -54.60128 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6beef803-396e-3f20-8f92-c8eff5e7287c | -9.00141 | -44.97984 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 487fc2f3-37a4-3f15-9838-2d2d749154d6 | -2.82642 | -50.46914 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 50867fcf-b4cf-3dbb-bebf-db2e6213de40 | -4.56543 | -42.97599 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8f88a7f4-e181-3824-b142-49201b1b537c | -10.53514 | -46.74299 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3b2d8691-dedf-36c5-9869-a433b2b343d3 | -8.6161 | -54.61667 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5360c10-38d1-3761-ac32-16aef801ad8b | -8.38523 | -47.24237 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bf16aec-d253-36ad-bd82-354f5e52d492 | -7.22152 | -49.63642 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c1db639-b5cb-3e13-82fc-197b99a506f9 | -8.37107 | -45.65785 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80706c8c-1b60-39e2-aae4-5af8f073b3fa | -7.9264 | -44.82865 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fdb6eac7-666b-39db-a7ae-b3cb1624142e | -7.67371 | -46.12982 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9583832-ce2b-3dea-8d6e-b45f9bced0e6 | -8.47055 | -44.5276 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 525fd255-4ec5-3b8d-9833-246024b7ed3a | -7.65817 | -46.11942 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da479882-258d-39a0-acd7-287630496966 | -8.60682 | -54.60807 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9173dee-4ec3-305a-8c43-8e1cdc6b1c1a | -10.23909 | -48.84844 | 2026-09-19 04:02:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff4ed17b-25e4-3bfb-8d68-40c9f1cbaf9b | -5.58008 | -42.73297 | 2026-09-19 04:02:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b767b80c-87c5-3013-97a7-f97439c8bf6f | -7.04305 | -42.08455 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 314f4a4a-3167-3515-871c-6f26d0092a9d | -9.88939 | -46.5469 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2520df4-3037-34d6-b50a-5879df3e154b | -7.57835 | -44.90829 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98a5ec85-ce8f-302c-9de6-d2c71a1a95f9 | -10.09314 | -45.64869 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 407640b8-97c0-38cc-84fd-87823c81df33 | -6.38539 | -45.8338 | 2026-09-19 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 30b2db28-8e50-3a30-8b05-fb4649ff69ab | -3.23624 | -46.94425 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d53ad809-7466-327c-9950-d8b4724c7385 | -3.36516 | -50.45231 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c2d2ea7-6bc7-3a7b-909d-73f624d23b32 | -9.15745 | -49.99826 | 2026-09-19 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a92cfe1a-8c2d-32c4-9b29-b578967341c0 | -7.82066 | -46.63918 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ece94f03-6d6e-3ba6-88c2-025b54e61c9c | -3.35764 | -50.46029 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5cdf1fb-13a1-346a-8cee-0062088869e7 | -7.81584 | -44.95674 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94c37614-b80f-333d-882f-32d813884e9d | -5.61709 | -45.25203 | 2026-09-19 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 975ec4a9-b0dd-371b-882a-49e99f4a1fb9 | -10.11573 | -45.56362 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a19630ac-64f0-3878-bb1b-d8ba89fbee84 | -3.52203 | -50.79586 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5a723060-ecc2-31d3-a9ac-e4c8d1a92757 | -9.34154 | -48.19005 | 2026-09-19 04:02:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efabfb36-11fb-3042-8ae8-e55d46ae0c55 | -3.36056 | -50.45423 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1dfa98b-a9b5-3445-b86c-b2814772c32e | -7.04247 | -42.08823 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 056438e2-8610-307e-89dc-018908937a92 | -3.03415 | -48.41601 | 2026-09-19 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bfa8dff2-9600-31c4-902f-db2c8dd75f50 | -7.32571 | -45.33365 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a85b50a-b72a-3658-af4c-7858e2e54979 | -6.71042 | -43.54228 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cce5ff8-1854-3910-8ae3-1526affddc7e | -9.95688 | -46.56192 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4ed0a99-b2a3-37fe-b05d-c22952c2a3e9 | -5.47039 | -48.99785 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2a83f33-de4f-3e9d-b90b-03603d14f6f8 | -10.47351 | -46.30787 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98be8891-05fc-3bbf-95ae-462abd766401 | -9.94744 | -45.27272 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99fcc0f8-e9c4-3d2d-a045-d5d89307f461 | -7.71222 | -44.64431 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc27aa29-9000-3557-888d-0b74de4203ff | -9.64163 | -45.91093 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8371e96-413d-3193-b260-b535df3409f3 | -7.07012 | -42.13775 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca36d1ae-c1f9-307e-853f-fa9c01cd67a6 | -4.5618 | -42.97541 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7e09ffb8-4131-39f7-b3c8-0a08e0ab5168 | -7.40572 | -49.84543 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b31a1a3-5246-3427-84ee-1006db0c9953 | -10.12841 | -45.55983 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6dae407b-4ee4-31e2-9abf-48e8336e02a9 | -7.58512 | -43.45504 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfacf2f0-4ab9-3f58-b85f-4e3e1ae958ef | -8.76017 | -44.22301 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a02d6c3-8b9e-3d26-8f07-032b989553bb | -9.61089 | -45.3786 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d97401de-e2de-3f65-8257-23fbe49d2ad7 | -10.32298 | -45.31001 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d7170ee0-e8a0-379a-bcb6-607f9137671f | -8.47204 | -44.51857 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 406f9373-7580-3edc-95e6-456faff6a3bb | -6.97876 | -42.18083 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e2eb8f8d-590c-3bc4-a514-3ac58ede5cba | -8.45802 | -45.71368 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b1b6b41-9d11-37d3-80eb-c92535b136b3 | -9.83771 | -48.39624 | 2026-09-19 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 810c4ab0-c05f-3a23-a716-8c80e0898036 | -2.93887 | -51.06498 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2147cced-a3c1-3e91-9148-f8b085b51eee | -10.54413 | -46.5956 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05b6a48d-5abf-39b6-94f5-5a6d30fbc91a | -9.94844 | -46.53637 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d675462d-a431-3022-be90-debbe526290d | -7.08528 | -42.08695 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25adb982-ad29-3d66-b2ae-fa382a73bfd8 | -2.8211 | -50.46358 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a5dab3a5-4abe-3345-870f-fca5b7354413 | -6.97936 | -42.17709 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6eb40b9f-3f06-3ec3-a787-5a8cb5bf0957 | -10.09957 | -48.41776 | 2026-09-19 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5e2a0a2-3e91-3215-a440-85b202bc7446 | -8.91936 | -49.99691 | 2026-09-19 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba1582ca-3b06-3365-a15c-4fa693389763 | -4.55093 | -42.97364 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9bd72c61-208f-3c0b-917b-0b530856b06f | -9.80171 | -46.10191 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c158e3dd-5cda-3e4f-9731-8d1015fada22 | -8.1251 | -44.83444 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84ba7219-45c1-3983-ac27-3eeaad07fd16 | -9.95405 | -46.55346 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0aa5a150-9854-3862-8208-581311799abe | -9.79976 | -48.32763 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ae3931a-b528-3997-b7bd-e27167d01676 | -10.53023 | -46.72211 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71eca335-9ecd-36d9-812f-97bfc52727a3 | -7.38209 | -46.15912 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a2d5ac1-4def-337a-9f91-0e86ed0d7990 | -7.36092 | -44.46964 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c16c478e-a532-37f8-a0aa-571332207d7c | -10.07264 | -45.65055 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d5986e5-1468-31e4-bf59-5d259095c3f0 | -10.31836 | -45.31413 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5ccbdd8-ad99-306c-9af7-51f2dbd05be8 | -8.66995 | -45.44049 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d225c250-1f68-314f-b653-bdc2a9356428 | -6.23179 | -44.69525 | 2026-09-19 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f790b8ff-83cb-3c05-b572-931b50b64479 | -7.22688 | -49.63742 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 882067f8-e4fd-39e7-9629-9143bce77e55 | -10.05152 | -44.88478 | 2026-09-19 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97967bef-887a-3700-a624-8483afde6319 | -9.56981 | -46.5592 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40c37916-ffe4-3c4f-8788-8f87f53435d3 | -7.1518 | -42.08971 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06c42d44-d97f-3510-bb7c-244b8de0d7ab | -6.01338 | -49.16876 | 2026-09-19 04:02:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6fc884c-36e1-36e2-9d81-856e98c98777 | -9.90819 | -46.57031 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acc0949c-9ffb-3b84-8286-b96fc2e8c143 | -9.7281 | -47.12563 | 2026-09-19 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1fd1ac5-097a-3f63-ab3f-3d79aa3d2862 | -10.50092 | -46.27152 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b19ff2d-7c08-3558-887e-e9dc0009c8a0 | -9.55538 | -46.59338 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f677f81e-1bc1-37bf-9cf1-03b30b0fc7f9 | -5.85528 | -44.94926 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78b1cb61-4de9-382a-898c-03fe746e0dde | -2.83327 | -50.4655 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| f4a90d49-0d0c-3f1d-94cb-07de311651de | -9.25433 | -45.9278 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3a2d128-a80c-35e8-ae9b-26ba652201ff | -2.82564 | -50.47386 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4fc6baeb-3c20-3445-843a-c8a4c60d4019 | -7.77913 | -44.89072 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fdefaa9-214d-369f-b561-d9e7a4a5479c | -8.09876 | -45.50888 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b398aac-041b-380c-920c-6ea9fa605ff0 | -9.91022 | -46.58317 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc504a5a-37d0-3f57-9147-91f4a7bc05ed | -9.93797 | -46.52272 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4196e6c9-1315-3213-8718-5460c34ef518 | -3.8905 | -49.06431 | 2026-09-19 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README30.md)
