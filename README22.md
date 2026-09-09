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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 116aed00-8e5a-39dd-8036-63984be8c5cb | -17.12119 | -55.8993 | 2026-09-09 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3dba9fca-c16c-3edc-a5db-0a7d89716f0c | -6.86646 | -46.00849 | 2026-09-09 04:46:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab569c5f-f57c-3f06-8f35-aea96115b542 | -6.79362 | -58.95379 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c40dc2c-e270-33e0-ada0-7be7be93d8b8 | -5.3639 | -56.01949 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb04f1c2-a0d1-3b7e-b406-7a7623dfc526 | -8.7544 | -62.4101 | 2026-09-09 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89bde562-4423-328a-92c8-bec3da04bb36 | -10.58695 | -45.74367 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be0e4318-9029-3e99-9883-4ec399a7f47c | -9.73931 | -43.49255 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58da8fe3-56ce-3b0d-a470-56e9ffcbbd41 | -9.72535 | -43.39259 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b3829c94-c00a-3f39-a117-92a522b03f8b | -5.21626 | -55.99307 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8025abc0-e9d0-328b-b38f-b34f5dc3205e | -8.74108 | -62.40629 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7409e81-dae3-3cef-9387-ec270471460a | -5.38119 | -54.4511 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0f16591-6349-3fbe-a189-36f9fd682ccc | -9.70998 | -43.50284 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b8c1af6-36ab-3c90-b138-d8c50c02139e | -11.00573 | -45.0843 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d981b48c-1440-31f9-8d18-6ca16985463b | -17.10773 | -55.91085 | 2026-09-09 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c597fae4-35d8-312a-831a-c8da70a1e83b | -9.69753 | -43.49158 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc8325e3-8b5d-3f6a-9393-e856126d7176 | -11.18321 | -40.88824 | 2026-09-09 04:46:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c2443a4-a0f0-3012-bb46-b5b850a13672 | -7.19602 | -43.62377 | 2026-09-09 04:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 928c8519-44ec-3d4f-a940-2afa4edb68e6 | -8.74011 | -62.41143 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dae2ad5e-13b3-31c4-9335-1bc2b01afd1a | -8.21526 | -46.00724 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7fad51e-6bbd-309b-8c33-fe5beb2e8b84 | -9.69791 | -43.45382 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a7b53e5c-1c5c-38e1-9084-34816e5910b3 | -14.28638 | -44.58662 | 2026-09-09 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dea6ade-1e49-395b-9937-3fe71286ba25 | -8.7416 | -62.40751 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 631cf7f3-5a9e-3e02-b686-84500eb320ac | -5.36836 | -56.02028 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ba4807b9-63a6-3fe1-8f13-ee96e797dd1b | -9.70349 | -43.44769 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 24fa0573-7712-39a3-90c4-86d97fbdee36 | -6.23903 | -51.67581 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26272807-6830-3d78-9428-96526e49ee80 | -5.58784 | -60.24953 | 2026-09-09 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b70efc52-23ed-3821-9eff-e14ef2cba594 | -9.71836 | -43.47525 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2246e1c-a03f-3f2c-8c62-f703257ea6c9 | -9.69693 | -43.49408 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aa5c5503-3446-3d3a-8bec-c62200c11aba | -7.53298 | -44.99128 | 2026-09-09 04:46:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50038b22-3f1c-3c7a-9370-bfcb64110f55 | -9.2597 | -45.65849 | 2026-09-09 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1654fadf-c2d0-3138-a829-909640deaf2a | -5.81125 | -53.81307 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dce9de6-c966-33ba-8da6-b3311209e8b6 | -12.95363 | -48.61541 | 2026-09-09 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ad69fcc-a67c-3090-8d0d-744bab136014 | -9.05911 | -45.77456 | 2026-09-09 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 693b896c-d085-3ebb-8051-7dc4a60cd401 | -7.37722 | -47.01712 | 2026-09-09 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e11eb7f-6e93-3652-9f92-7edbaf2056fa | -9.50176 | -41.99588 | 2026-09-09 04:46:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf676c5b-fe0d-3f73-81d2-2af7fbf12f3d | -9.70959 | -43.40454 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5eaf014b-9d54-35f8-b286-bb438f570b97 | -11.26789 | -45.70794 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d8298f2-ab19-3760-8073-7b32b40a8632 | -9.05782 | -45.77688 | 2026-09-09 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3947853-853e-3ec8-912e-4bed99611cae | -9.76469 | -43.40965 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5eba8c8c-7ae9-3ff5-9588-6a0d6e73b6eb | -6.7942 | -58.95045 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd88124b-afbe-3a8e-ab64-88c137de2ed8 | -8.75543 | -62.4048 | 2026-09-09 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d89bde44-f93e-38ca-9ebe-21ef103e70c8 | -11.48161 | -42.2387 | 2026-09-09 04:46:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e0e50f91-4228-33b3-b8eb-bd012453bc97 | -8.76074 | -62.41169 | 2026-09-09 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 219a1939-c3b5-3295-b4f3-6497b4ba7adc | -8.7202 | -62.41476 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8bf0a66-486b-3488-925e-f55019b23b60 | -8.72125 | -62.40943 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e37ba149-b66c-3bfe-a6b7-ba39b6a8dba0 | -9.69627 | -43.49877 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6dbbaae6-6ef2-314a-b452-2db2bef1a9d0 | -15.98895 | -56.42941 | 2026-09-09 04:46:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5551b14e-40e6-3627-b460-870491fd00fd | -5.81823 | -53.79454 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2be732d-3466-3fac-8b62-302eed09ff33 | -9.72357 | -43.47118 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63d63a8f-8967-3922-a363-73e17eb19cea | -10.23184 | -44.6348 | 2026-09-09 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89ca1674-15f7-3636-b111-d20fe6c4f77e | -9.69369 | -43.45094 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb09bbb8-8f88-3f46-950c-642544dc59f8 | -8.72079 | -62.40811 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e8a9d7c-dfb6-3cff-b9fa-c2691076daf3 | -9.7798 | -43.46955 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c3d61dd-4a98-3e77-a391-b0483e0b715d | -9.70997 | -43.50062 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af6a1c69-90be-3545-b7ca-a3cfaecdd5a2 | -9.77262 | -43.45391 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7224e179-deff-3c5a-93ea-69d3bf531a10 | -8.71977 | -62.41343 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c0d04d6-f593-36d4-9077-64a7d52b3999 | -8.08821 | -45.68066 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2841f38-e070-3cce-b92a-d04efe353ccc | -8.72621 | -62.41459 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f580ca3-006c-350e-8208-14e976a0054b | -8.98163 | -60.58138 | 2026-09-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a2e327b-a396-3785-a1d9-7a11eb872be3 | -6.43126 | -54.71104 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 723b807b-03e2-3575-b575-de10af5389a2 | -10.64893 | -58.7706 | 2026-09-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a893ead9-e516-3944-adc9-4316b6bffdd1 | -9.77846 | -43.51258 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 865b3e7d-4f82-3ad3-b756-260cfd5575e8 | -8.7539 | -62.40884 | 2026-09-09 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a678a394-814a-3269-9483-592ad983379d | -15.9946 | -56.42017 | 2026-09-09 04:46:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fa8c8797-5569-3c93-bab4-67aa7dc6b4e9 | -6.23964 | -51.67204 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7d00abb-68ed-3a04-bac5-cc148a8524a4 | -10.74761 | -45.96742 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad2e6518-1e1b-3d4e-9abb-7541728451b9 | -12.85482 | -44.39426 | 2026-09-09 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8929958f-828f-37a8-a7c0-55971043c284 | -6.79893 | -58.95487 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31b92fa5-f5d5-3d4b-9e05-6abe005583ae | -11.48122 | -42.24182 | 2026-09-09 04:46:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8bacec35-80c5-3379-a16c-799c07befa50 | -7.52751 | -45.92792 | 2026-09-09 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c500c91a-a361-3b37-9a3f-c54de2a072d7 | -9.70005 | -43.47273 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eee97833-9826-3a81-b147-367ec357d9b8 | -9.87033 | -46.70354 | 2026-09-09 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20834629-7343-3fbf-bcfb-530ac9e2c01b | -10.36353 | -45.17451 | 2026-09-09 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4710d71e-0488-3e72-b501-30971a40c9a0 | -6.31155 | -55.15004 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7724f8ec-65e2-3c7e-9530-d8d2f3349a9b | -8.72663 | -62.41591 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7e2756b-e602-37a3-9438-bb8b1ab4acb5 | -5.80357 | -53.81174 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bce0b251-9740-3a0f-8318-57a378a497c3 | -9.69236 | -43.49346 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc556f32-a370-3c7e-b50a-a40686ed232f | -9.69826 | -43.48469 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f798526d-2721-3173-8ea4-527ce62cf006 | -5.79973 | -53.81107 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1c304b50-6099-3d9c-b527-ad95c6d26cb7 | -10.72269 | -46.05602 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4afd0149-0e82-38c1-a036-8c0bef472d22 | -10.73633 | -46.01724 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11c034bd-5cd3-3b7b-8b89-5e0be5b3a078 | -9.74521 | -43.51742 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6b20723-36d8-3394-b656-6cc6a629f3bb | -8.09018 | -45.68377 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f1e3c59-c878-3a32-b941-8a5eee5942fb | -8.09664 | -45.67693 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b5279cd-4186-3052-9631-245485fd8140 | -9.70311 | -43.4498 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a092a743-4b90-31fb-a4d9-ac4247c87910 | -10.99127 | -45.08808 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfa5be25-a38c-3385-9a86-89a91ccf00dd | -10.65378 | -58.77193 | 2026-09-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bb6b010-3567-386d-86c9-17745ed1d655 | -9.70248 | -43.45452 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ea27968f-df0e-3dee-a318-e72bc8d1af98 | -8.21148 | -46.00663 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 548682b1-c324-3b36-acc2-4c9dd5bdb01e | -9.44992 | -47.79427 | 2026-09-09 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ccfa4db-848e-3ae7-b046-1a48041364b3 | -17.10998 | -55.90897 | 2026-09-09 04:46:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9d27d3ac-f2dc-3d5e-82df-1c612ee3b5a0 | -9.76091 | -47.03637 | 2026-09-09 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 390765c9-10c6-316b-936b-d85dac73329c | -7.37702 | -46.51783 | 2026-09-09 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98056887-0fe8-3dd2-b166-0be0836bc364 | -10.65478 | -58.76656 | 2026-09-09 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fc84202c-8edf-3697-b04d-68ac46fb824e | -9.70952 | -43.40181 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0a0c2e98-d7c0-3381-98b3-95f5273fe2f6 | -9.70367 | -43.4133 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 748bd062-32a2-3a9a-925b-556e97bfbbb8 | -8.09624 | -45.66977 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2edb876-d22e-34b5-81a6-eb1bed13eb32 | -10.69465 | -46.00099 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99384e87-fa6b-3968-9d02-89d45512a5d8 | -10.52376 | -47.95731 | 2026-09-09 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bf83c2d-4b25-38a0-aa18-19f440000500 | -6.8362 | -51.49602 | 2026-09-09 04:46:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README23.md)
