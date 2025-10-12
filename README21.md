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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46f754ed-f1c5-35a8-b195-4474373eef4a | -11.67666 | -43.77369 | 2025-10-12 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8c26867e-6515-3d4f-a43b-1492c2ec43fc | -6.35546 | -43.18204 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1ad9f23-da04-39ad-922f-083617c504d6 | -6.26841 | -42.97738 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cb2a4e6-aff8-3827-ae45-5b9e9011feed | -9.52901 | -47.86861 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7fb35440-4a1b-319a-be97-7f2b677964a6 | -9.56246 | -43.01795 | 2025-10-12 04:14:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 271f4bab-cac4-3e51-9d9d-a9a8c3cdb120 | -7.80633 | -42.42965 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e7dead77-3e9a-321a-b00b-1ccb8950d6a3 | -10.16821 | -44.54023 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 360999a6-06d6-33f8-8883-94f471422ee5 | -5.20953 | -44.35801 | 2025-10-12 04:14:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c27361f-8d87-322d-89a7-65fd42f0d152 | -8.8374 | -46.07544 | 2025-10-12 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8f2f1d1-6ffa-39ea-9f1b-6c3a4d54647b | -11.36686 | -41.88245 | 2025-10-12 04:14:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 7b9c0673-a106-372c-b51f-1dcb63967f1f | -6.80531 | -47.05775 | 2025-10-12 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3280b59-d403-3fef-af80-771763a3c575 | -11.36187 | -44.00688 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c72c0f8c-ea41-3758-8bdb-c1747dc0cdc1 | -7.55176 | -43.84347 | 2025-10-12 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cd2ad09-7897-3242-a9da-d809e7c6eb1e | -7.80579 | -42.43316 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80666ddb-4052-3aa3-8fc1-8dbe933e2377 | -9.40421 | -45.76329 | 2025-10-12 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94ebf014-cb41-3b6d-a3a9-af3636ba6954 | -11.64844 | -41.66156 | 2025-10-12 04:14:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2c2a54a-507d-36f8-b2c7-1736aa85cec7 | -7.14837 | -42.50652 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3e468dc0-961b-339a-833c-315df0ea467b | -7.68523 | -42.57626 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 102934ce-0292-34b8-916a-addeed4915ba | -5.48158 | -43.39618 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09b56488-5847-3e6b-b995-dc704b0a1722 | -8.10029 | -47.24244 | 2025-10-12 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7e21a3c9-8012-38b6-961f-b153db5fcd4c | -7.85444 | -38.69901 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc760bd8-0a92-363f-99ae-2c845672bac4 | -7.42077 | -42.96565 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 32d86103-5e4d-3a6a-b205-d86714a7898c | -6.04256 | -42.46526 | 2025-10-12 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3279bc19-f020-3b09-b0fa-eb5adf78c053 | -5.42156 | -41.33413 | 2025-10-12 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20eff094-2c08-30e5-ab12-d52d17a712c5 | -7.49168 | -42.77075 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c1ea663-faae-37dc-b437-37406ad97bc0 | -5.48402 | -43.07521 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6842f736-d376-3562-805e-45d8bf304bcc | -5.46837 | -43.39411 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51dfbbcf-30bf-3206-8bbd-bf1824c6dd20 | -5.83112 | -44.02677 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b3aa3f1-cbee-382e-bb43-cc611003d35f | -10.17151 | -44.54077 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83201f0a-e548-36b7-93ac-89d95fc57d42 | -7.5244 | -44.5977 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07d9a3ad-aae8-3249-a61c-0f176a5d80a9 | -11.67227 | -43.78019 | 2025-10-12 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 42eaf685-dc97-349e-af30-77f0c08525c4 | -6.66475 | -45.93082 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21d01117-292c-3f0f-9bf7-a12601b3e922 | -5.06666 | -42.6996 | 2025-10-12 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1089b9-5869-30c1-acb2-403dbcec08e5 | -7.15688 | -42.18814 | 2025-10-12 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec651851-f156-3167-ad5f-551d25b1d55e | -4.68249 | -43.25904 | 2025-10-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d34037d0-508c-32ef-a94a-79db2ad36f3e | -4.27343 | -46.92745 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2221ae7f-0910-3cfe-8b74-b4b01cf3c34a | -9.56192 | -43.02147 | 2025-10-12 04:14:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 282856f5-2a48-3841-9c67-db5cc5267a07 | -5.67182 | -42.67857 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4fb76b2d-6e44-32a2-bc2a-4e00fb5662e9 | -7.8802 | -44.45836 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 075d71bc-9512-3cb2-8e64-dee5b0a045c5 | -5.50141 | -43.787 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 176d3fa4-8820-3858-9117-28911fbf8fbf | -9.55914 | -43.01743 | 2025-10-12 04:14:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42cda46e-0a4d-3330-8146-786a5d28132c | -7.44862 | -45.70863 | 2025-10-12 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ece4272a-1a32-30dc-b30e-2b60b3c99d0b | -5.97851 | -42.15225 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a6fe8720-bae4-3590-a05f-f76d5892d09b | -4.2757 | -46.93763 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| adb6575c-0d5e-34b6-a727-fa657bc9af21 | -6.05305 | -41.89046 | 2025-10-12 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a6edbe76-38d6-37b8-92f7-1bfcaf893f82 | -5.05525 | -43.27213 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a26e97d8-aff7-3d80-9656-7a5146a85b1e | -7.42407 | -42.96617 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 69fb7a7d-6c5d-3fe1-9c88-da0ea9a1b459 | -7.5523 | -43.83999 | 2025-10-12 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30dd7b4d-ef8b-33ae-acd5-67b4f874b3fa | -10.1819 | -44.54246 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf567d74-1e9b-3177-9caf-10e42545315a | -5.94039 | -43.93935 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3be35854-620c-3905-90c7-74451c3caafe | -6.76879 | -42.8273 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6ec6e01c-7538-368e-a732-a574e0d20b2c | -8.16247 | -43.31331 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07558fbb-564c-33a3-8d0d-bd2178d7643a | -8.47595 | -46.20227 | 2025-10-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5173de4-17f9-3e9f-97a9-9eecd02d127f | -11.75528 | -43.30742 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afbaf02b-e2af-3653-9c27-549963d933a5 | -4.88743 | -41.55199 | 2025-10-12 04:14:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b80d13e9-2293-3c39-ab44-5f1023bfc4e7 | -4.78894 | -43.08154 | 2025-10-12 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41b61d64-2d0a-3070-b1c2-012260e8a406 | -4.65883 | -49.38425 | 2025-10-12 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b58e3cc1-6f5b-3088-8647-ba226b241497 | -5.6285 | -42.69649 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f86af895-29c7-3539-80e6-f5eb6e88f6d9 | -4.66334 | -49.38486 | 2025-10-12 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a56a96b3-778c-38fc-8407-4474729620e2 | -7.20578 | -45.4904 | 2025-10-12 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8fa01e5b-10c7-3bf4-b901-71b89a237c5c | -3.52103 | -49.71223 | 2025-10-12 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d919dd16-d195-3074-91b8-8cf7a181e0a5 | -5.34337 | -43.40628 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97b22b2-74ff-3433-8f6c-5f4ed23aeb63 | -6.27284 | -42.99218 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2e3d3a63-ae1c-3203-878a-03b64a17f467 | -3.93755 | -47.98422 | 2025-10-12 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad262843-318d-3aed-99ea-719a113be113 | -6.94124 | -46.12967 | 2025-10-12 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e851aa68-264f-3d80-9cb1-878f549138b9 | -5.91588 | -45.42547 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4dcd7567-3c06-3406-ab24-b54f9c1e2b92 | -7.85564 | -44.52708 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df4b5695-4c99-3c85-9c32-87ce1660aa71 | -4.88944 | -41.4943 | 2025-10-12 04:14:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 138e12ee-f879-3c38-b776-52e59c7e1646 | -3.93564 | -48.9193 | 2025-10-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 223ff4c6-4ab3-3a32-80c6-3860a19b71ce | -11.35346 | -43.99119 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e46d230-6659-345b-a416-967b134d4f0a | -4.94753 | -44.76283 | 2025-10-12 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d55160de-3cb5-3533-bc4a-d437631c0846 | -5.11992 | -42.79601 | 2025-10-12 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd59ba44-0cf1-32f5-966d-ed2b1480e7e7 | -16.73585 | -43.98148 | 2025-10-12 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3292e24-10b4-3283-b046-3e2fd93572ca | -13.98969 | -54.89591 | 2025-10-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81ffa944-7e3c-331a-9aae-9a51b8a0dab4 | -16.75572 | -51.61874 | 2025-10-12 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b2526f7-c217-3998-9a47-27fd988e1219 | -14.94632 | -46.72348 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 097d3e1c-7318-3a93-9448-d91bc71719d5 | -15.29578 | -46.13819 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dedcd0e-b8a0-3c5f-bb3a-01116334d9ac | -14.02521 | -43.48888 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| af7780b4-502c-35a8-8445-126bda19b44a | -13.03671 | -40.51064 | 2025-10-12 04:17:00 | NOAA-21 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7bdbac05-a15f-3507-88db-3768d2d56ac7 | -14.67957 | -44.76295 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 648d124c-c3e6-3e0e-a029-10e724a90ceb | -14.95433 | -46.72512 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7bba9e08-e02f-3639-9947-e18f1c2bbc0e | -19.78311 | -42.39206 | 2025-10-12 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ebaf5bb2-38b2-3a83-a52b-8930453a9086 | -14.95893 | -46.71828 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c09d74a3-0393-3818-8536-7e0134f22a17 | -14.98477 | -44.94403 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b05018a-8596-3751-8bbe-78d5d0c3e0d5 | -15.858 | -56.75107 | 2025-10-12 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be9f9c92-e994-3c25-86f4-de8cd6690756 | -18.04679 | -44.97678 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b997e9d-1a0d-3449-9e5f-b3e35033868d | -19.51809 | -43.04212 | 2025-10-12 04:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7c9edc0e-8b6c-37e8-b816-0d62b5fa84ee | -18.04347 | -44.97623 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffae5c87-a93d-3eef-b6bc-27b9ace5a4e4 | -16.34463 | -42.39165 | 2025-10-12 04:17:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eeea4ff-afbf-3d7a-85a4-e12b5d70fa2a | -17.18465 | -46.94827 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca2ff673-04d3-3a6d-a771-b874f0e612bc | -14.96233 | -46.71873 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ba2d4f14-9f78-3d51-9aa1-3f6c04b4607e | -16.34226 | -42.38275 | 2025-10-12 04:17:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5c9a96d-6c4f-3a0f-8b69-74a125e95ffb | -15.29304 | -46.13402 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8aed4ed-bfb2-3476-8716-45b672e2675a | -14.98258 | -44.9364 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e95d346-459f-30a3-a1df-62256e767283 | -18.57266 | -50.58965 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 579e042b-c4e4-3eed-ae69-0ad86e2ec14a | -19.53358 | -43.06165 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ddaf1476-0899-308d-9774-a36075ac6c6a | -19.53447 | -43.04775 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 8c501298-49c0-3a2c-bda3-dcdc55384027 | -14.58755 | -42.77477 | 2025-10-12 04:17:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc43e3ff-0fbb-315f-ad5f-fe28df75b720 | -11.85254 | -56.86308 | 2025-10-12 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf3d6f91-ac05-3f4d-97f4-462d653c82df | -17.18372 | -46.93278 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README22.md)
