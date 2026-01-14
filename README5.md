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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff44a71f-a8df-31ff-b337-94c34f9e6dbd | -12.11219 | -45.59875 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b25465a4-d1fa-3e2c-a3df-6d0d5287d1b0 | -12.11357 | -45.59629 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ffb2b73-9960-3030-b44e-ebe7f4cc37fc | -12.9168 | -43.0194 | 2026-01-14 04:04:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e13ecd62-43db-34ee-b4f0-50031ad50ff1 | -12.11471 | -45.58439 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88206ad2-824f-3920-8aa8-340f5850e5c0 | -11.85339 | -43.72505 | 2026-01-14 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3256f21b-a07a-3dc8-956c-cd7e157d66b3 | -12.11388 | -45.58916 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b45cdc3d-bf90-30f6-83e4-9a5d68573a22 | -12.11761 | -45.57243 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88c68aa4-2475-3cc3-bbc1-1b1b39a7f677 | -12.11851 | -45.58509 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e02602d1-54b3-3f33-b85a-1d5cf601e6ea | -12.55538 | -43.23348 | 2026-01-14 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e897498e-90b2-3538-9d5c-2cea0afc4eef | -12.07635 | -45.58459 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca422a31-853d-3047-a2b5-7b1b9a20430c | -12.11303 | -45.59395 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a652446e-7c5a-35e3-82f0-3cc1549a29ff | -12.11519 | -45.5867 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70caee09-e096-3560-b95a-4cb680ab809d | -10.55875 | -44.33939 | 2026-01-14 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffba0604-0f3a-30c2-90ba-3ec7f8026b10 | -12.11139 | -45.586 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59df6a46-c617-3130-a0b1-dbe7a75a63ae | -12.17911 | -43.49215 | 2026-01-14 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1a7ba0cb-5525-3938-9dee-04b2603045ce | -12.09046 | -43.76678 | 2026-01-14 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8d6650f-a69f-356c-96d6-fae1d4d7c902 | -12.11767 | -45.58987 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcdd4d5a-d6b2-3d87-a116-58d9451a53be | -12.08981 | -43.77065 | 2026-01-14 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaab19eb-3313-3e0a-a9ab-b80fc38d3b28 | -12.84063 | -52.52582 | 2026-01-14 04:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8ae57d08-3ee9-3284-89ee-b143af1ff3f9 | -12.09292 | -45.60237 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6cd754f-edce-3f38-8a3a-e50bd3b4580f | -15.02928 | -43.83119 | 2026-01-14 04:04:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43ad9cb5-063f-3011-a326-c35f4a4427fb | -12.10416 | -45.57758 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cae6073c-699c-3650-9138-6047516f6373 | -12.116 | -45.58193 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a2a1c49-773b-3f05-a305-7edfb94cbec3 | -12.16435 | -44.3391 | 2026-01-14 04:04:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0f0b334-37d9-3ce1-af39-311739fad0d7 | -12.12231 | -45.58579 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9d0b044-7fb3-30ba-98ac-c523d94d1b79 | -11.18063 | -44.80831 | 2026-01-14 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd49c4b4-a42e-374a-9df6-4dbbd2b14456 | -10.48736 | -44.93147 | 2026-01-14 04:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78acaaa6-7b7d-3b0f-bef1-38a40ef2d726 | -11.85404 | -43.72114 | 2026-01-14 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8728f020-9a33-370c-94c0-4676c77c2219 | -12.11092 | -45.5837 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b990b5d-2998-3527-a1ba-82292ecf8482 | -10.4836 | -44.93085 | 2026-01-14 04:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35941b71-828b-3ccf-a176-c253f3e03ac6 | -12.11008 | -45.58846 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e41ee4f-81cc-35c0-ad56-e2efc694e0f9 | -12.11683 | -45.59465 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b9ac850-87ca-3bfd-af97-9e8feb3da551 | -12.08819 | -43.77192 | 2026-01-14 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9681afc9-4b4f-3c1b-9712-a704c3d2a32a | -12.10581 | -38.91827 | 2026-01-14 04:04:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8556881f-f270-34ff-9c94-17eab5878d45 | -10.48336 | -44.92794 | 2026-01-14 04:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ab2721-ddaf-37fe-a3d6-b8be7b42bd03 | -12.11841 | -45.56771 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cc6431b-43ac-3446-9cfc-ba4ac42f16be | -12.11722 | -45.57017 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebfe31d3-6ccf-3c97-92bb-b06ddd72f52f | -11.25589 | -44.54364 | 2026-01-14 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fc78419-957e-3d12-8e42-cac7748c1c22 | -10.55512 | -44.33874 | 2026-01-14 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1758fd31-2153-37ba-aca6-fb4aa67b4341 | -12.84824 | -52.51833 | 2026-01-14 04:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f06b9ef1-af44-3c85-84ac-7e6ba45e2701 | -12.09374 | -45.59755 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9585869e-287c-39cf-aa82-a65628f15ca8 | -12.92017 | -43.01999 | 2026-01-14 04:04:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a3f512b9-fb12-366d-9941-239fbb690bcd | -10.48711 | -44.92855 | 2026-01-14 04:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89b6dbc8-62ea-3a01-b0e1-3ad3d426eac8 | -12.08882 | -43.76809 | 2026-01-14 04:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a151a890-4bf6-387d-ac57-edea81a1c56b | -12.11639 | -45.5749 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44e80145-b445-3d96-b992-256172997733 | -12.09836 | -45.59347 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 081522be-5420-329c-9093-8d3abef4aeec | -10.16647 | -42.2153 | 2026-01-14 04:04:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dea248ae-b9d7-3f63-adbb-c6a1a11688b9 | -10.41146 | -44.63923 | 2026-01-14 04:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0f916cd-968d-3a6d-b479-b1ec11c98488 | -11.1612 | -43.57516 | 2026-01-14 04:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c22f24fc-86f2-3f02-ba7a-c5a26ad771de | -12.11935 | -45.58032 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6a9e69b-abe7-3760-bf6e-c13bcc85914b | -12.84151 | -52.52142 | 2026-01-14 04:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 83fe3e10-24b9-38af-be47-067423d00416 | -15.14178 | -43.95558 | 2026-01-14 04:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4458e20c-fb6f-35a4-87da-12fce4ebf68e | -12.84736 | -52.52271 | 2026-01-14 04:04:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 33c239ee-27c6-36a1-b386-e0884fd17028 | -12.08342 | -45.56623 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59dfb47c-d31b-3cdc-95f3-edd70802a04d | -12.1122 | -45.58124 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3e4ab8a-e3f3-396c-a9c0-876ad9d4c16d | -11.8512 | -43.71663 | 2026-01-14 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33e5f379-017a-3142-8310-f8897e9b5869 | -12.09673 | -45.60307 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c88156b-a6e6-3924-a8aa-5a4d97eabf06 | -12.11555 | -45.57964 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54d410ed-8ff1-3087-b35a-b53ddd77ca4e | -12.09754 | -45.59826 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3de97b48-d246-3a85-9434-ce01b878783e | -12.08261 | -45.57099 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7691e60b-70f5-3356-be4e-6a3e4d1f21bc | -10.48259 | -44.93253 | 2026-01-14 04:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3584066b-5eb5-36b3-b671-072cffde4eb7 | -12.12315 | -45.58102 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2e9fd85-ba8c-3d93-bb68-3fa2eda01054 | -12.09917 | -45.58869 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94403d2e-a592-3e8f-9883-a76c33192dd0 | -12.11438 | -45.59149 | 2026-01-14 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ede59a06-e29c-3520-a8f0-74df0b09bc43 | -11.85056 | -43.72054 | 2026-01-14 04:04:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf075b60-e0e9-3466-8806-0dbd8632bf85 | -16.11033 | -56.75556 | 2026-01-14 04:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c11fdfd-38eb-3aae-9fae-e4117cf23417 | -20.84388 | -51.74431 | 2026-01-14 04:06:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 787d12f8-0c4a-3322-8cf8-87bbb16cb4a8 | -22.85301 | -42.88942 | 2026-01-14 04:06:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 35ad5195-0cb5-3aa0-a496-3487d71f6bcc | -20.84506 | -51.73876 | 2026-01-14 04:06:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9f20607d-fdd1-3614-b55f-5828033e9024 | -16.09468 | -56.75902 | 2026-01-14 04:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e1bb4ed1-7c95-369f-9ca4-5fcc8f950961 | -22.77099 | -43.00001 | 2026-01-14 04:06:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b413168e-1ebc-3cc6-b3eb-f36fa74ec20f | -22.80385 | -43.00972 | 2026-01-14 04:06:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 54dd4847-44f3-379d-a74c-ed1ce0a1ac94 | -16.093 | -56.76627 | 2026-01-14 04:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 919cce51-7ea3-3025-9b19-95c0a1e98f05 | -0.08863 | -51.27711 | 2026-01-14 04:50:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2930f6a8-0cfa-3fce-bd98-3f94942c44f5 | -0.90694 | -47.55335 | 2026-01-14 04:50:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4efc539-81d1-3ba4-bd37-b5b9723f63b4 | 0.05378 | -49.92522 | 2026-01-14 04:50:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35b37d5b-9cb8-3bbc-be34-a4473cd41d8d | -0.09193 | -51.27763 | 2026-01-14 04:50:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb98e705-77e6-3af8-9767-216f075685af | -1.06892 | -46.80136 | 2026-01-14 04:50:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ded31041-f3a3-397a-bed3-cceec67717e0 | -12.8366 | -52.52457 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cba9f12e-64e6-37d5-b386-ed3623fb4f8e | -12.84055 | -52.52139 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0d6d8dc-71f4-31c4-8cee-78f8c4992f2d | -5.10698 | -43.24212 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 75dd36be-0262-366f-8d97-d027c3eb7d9c | -2.36001 | -51.89764 | 2026-01-14 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9074af4d-f2c2-3423-bfec-ca015cf11ea2 | -12.96805 | -49.92027 | 2026-01-14 04:53:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c49ebc90-9975-3130-aec1-b3ec0663d3b5 | -2.37099 | -51.74136 | 2026-01-14 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45b445ac-cd8d-3932-81ae-d1233638d43c | -1.94714 | -53.46329 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd16906a-fa45-3f7f-8f45-a915dcb309cf | -1.94996 | -53.46745 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dc1786f-b681-3dd1-9bdb-339249ce2120 | -1.88824 | -53.25464 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73bbc196-3e92-3b4a-a02e-54883b5347f8 | -1.89049 | -53.26235 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5d38f7f-a2b1-351b-8e7e-f3cbd52d97c5 | -1.94656 | -53.46693 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1e3fc0e-ef4e-3e11-9166-89c49a7974a2 | -1.95221 | -53.47525 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1eda6bba-fe9c-33ef-838c-757e7e9f684d | -12.83716 | -52.52085 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeb03796-8f16-3e57-bf03-280d414be222 | -1.29078 | -53.68611 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2df93835-c16d-3afe-8f76-d599aa934c13 | -13.68722 | -55.68746 | 2026-01-14 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11c191d4-4ba6-3524-bdea-fa76a9e5e555 | -1.95335 | -53.46798 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b3ae32a-482e-3b51-af5f-e06b44ac9f02 | -12.84845 | -52.51501 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80be2687-def1-3b5f-baeb-6b42307d52f6 | -5.10208 | -43.23808 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94003132-1fb9-3d59-8132-2a312132d130 | -1.95674 | -53.4685 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9be5553b-4f01-34a1-9b43-33fcc3f5ec84 | -1.933 | -53.46482 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f6b7011-1617-31fd-9be9-0c33dfc47e09 | -3.49054 | -54.78634 | 2026-01-14 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4b79ec5-cfe0-3b6d-805c-4feb5e1d91af | -12.08884 | -43.76749 | 2026-01-14 04:53:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README6.md)
