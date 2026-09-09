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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e44774b-1bb7-3571-86bd-d8a0139d701a | -1.66478 | -55.66817 | 2026-09-09 04:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a2d5b53-bdac-3060-a079-ca47def5e5c2 | -9.77358 | -43.45916 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21faa67b-2276-3ba9-91f0-be15fcb1ad6f | -10.75002 | -45.96948 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 935376cb-4fde-3004-9267-ffd905a7c8ff | -7.73743 | -45.05284 | 2026-09-09 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 380f9783-6aaf-325e-a465-ffbd0029e820 | -7.19472 | -43.61621 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf0438b9-3901-3750-a46d-abf6a379ba4f | -6.86015 | -46.01123 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9028ab1-e6e2-3535-bfa1-130b1d9520cd | -9.50266 | -41.99265 | 2026-09-09 04:25:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81e19b2c-7116-37ca-b1d3-deda7197eebb | -5.66529 | -44.40658 | 2026-09-09 04:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eda20deb-a726-3d8c-adc9-2cd768869435 | -7.19638 | -43.62719 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2300c57d-7c47-3128-9037-b2545cf1cfa8 | -5.77604 | -45.06574 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e98be84-3c80-399b-bebf-ae76a5ae56d5 | -5.54208 | -44.49804 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e503482-e891-383d-bca4-e56cc6e9dc84 | -4.02091 | -50.44551 | 2026-09-09 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4250ce1f-ee1e-3253-aa88-3986096bca32 | -7.6776 | -44.59902 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4464d276-4cb0-367c-b503-726e0a4973b9 | -9.69817 | -43.4474 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83c8e9f0-529a-36e3-a2e0-02175397fd2d | -3.25013 | -50.82424 | 2026-09-09 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8af1fbd1-9673-3167-9bc6-e34b491cdbbd | -2.56224 | -54.7435 | 2026-09-09 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00726342-68e2-39f0-b6e6-28ad2f268e5b | -9.70427 | -43.45198 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 462ceede-2c1a-3303-9e0f-b34139fc0973 | -3.79781 | -52.40593 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2c4ad1c-4d83-3fec-9d6a-db1112cdc4fa | -5.80557 | -53.81023 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e95a5d6-bd05-32cd-8a27-2696c3724a9e | -7.37718 | -46.51954 | 2026-09-09 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70f661ec-b24f-385c-bd60-77248fcbb795 | -3.9694 | -47.58316 | 2026-09-09 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc43ffaa-6be5-31f7-aaa8-2e55c00da720 | -9.71203 | -43.40276 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 97ec3a3b-75c9-324b-b3d5-0a8e0e1fa23b | -8.08859 | -45.67957 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd86ed2-b879-357f-a0b0-734bebcf150f | -9.74755 | -43.51621 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8974cfe6-6063-3353-9c6e-11941f5636de | -8.09142 | -45.68394 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d06fe61-1241-3c04-8dee-edef03fb7476 | -8.85126 | -36.53369 | 2026-09-09 04:25:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 10697395-57d5-32d5-a916-d572a2d7f33e | -11.00327 | -45.08367 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 140a8907-fcff-3429-8d8b-09848cfc4f62 | -9.70426 | -43.40872 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bf658c2d-0800-3304-ae0e-3b09e6b4c148 | -10.71749 | -43.63117 | 2026-09-09 04:25:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07fd6fb1-3435-3681-acb8-93ff80b9bb50 | -3.25063 | -50.82125 | 2026-09-09 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9283a620-070d-3aff-933a-50d65ab56ba3 | -6.25649 | -47.34705 | 2026-09-09 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb51fa22-aab8-31d2-8bcd-678cdf79bdf8 | -9.05863 | -45.77639 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aef7220-852d-3523-b943-fd523bf55625 | -9.70041 | -43.47652 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9774ecc-51a9-33b8-aec2-8629692ebcac | -6.1617 | -44.66048 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8113f241-5f54-343b-93ea-8c9a63b848f7 | -10.71576 | -46.04854 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7af2240-1b7a-37d2-af19-8d223db365bd | -6.24733 | -51.67218 | 2026-09-09 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dac5114-f485-3d41-8728-0f8252b27406 | -9.92097 | -46.62905 | 2026-09-09 04:25:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62315adc-1529-3a06-bd3b-631e6038322d | -10.7466 | -45.96891 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4906517-13c3-351b-93d5-81664a9f8400 | -6.35911 | -43.59014 | 2026-09-09 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f12725ea-8606-3e4c-86a0-1800578d2f44 | -5.42648 | -43.43416 | 2026-09-09 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| abe76596-33c9-3b5d-8f77-f39751c2958a | -8.21756 | -46.01268 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd003b18-e80b-3a4c-be63-3a432b34c405 | -7.68915 | -44.31293 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8277a8df-5f7a-3487-955d-d9e7230f7ffe | -8.09614 | -45.67693 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb4075f9-89a6-36ae-b497-6d68547e654f | -9.77971 | -43.50696 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3682f3f6-319f-36eb-aaf0-00613fe3bba7 | -9.71483 | -43.47162 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5928d2bc-c608-3709-ac2f-1fa4eeb805a9 | -5.60434 | -44.84669 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e8c94d51-e379-399b-831d-0b1f56ee3b4f | -10.7164 | -46.04932 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91c64153-b5fc-3838-af85-456e125c3955 | -9.71761 | -43.47566 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53a37435-6e3a-3305-95ea-3f7794692b39 | -9.77638 | -43.50643 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92bbfb8d-8aba-320c-a596-1f194805c452 | -3.76383 | -49.10168 | 2026-09-09 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc3f6dc5-fbd3-3e34-81f0-af832b2c6d78 | -4.17466 | -48.70876 | 2026-09-09 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 990a2730-45f7-3b94-86d8-bfe7d96b9b7b | -5.74948 | -50.19296 | 2026-09-09 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7de35251-45d2-3ebd-b4e4-1b0af9d1aa7b | -9.70704 | -43.41277 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a1b67f1b-0d7b-3f67-9475-66a4783c116e | -6.69926 | -41.57773 | 2026-09-09 04:25:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| babf0d97-9301-3ccd-a7da-752d9ce4f52d | -5.4213 | -44.79128 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccd7a0b6-af37-3eea-8f6c-749f882aae7d | -7.26476 | -45.35439 | 2026-09-09 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34beabb2-aa22-349e-b84b-7efe739e32b1 | -9.50208 | -41.99639 | 2026-09-09 04:25:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 07a56224-da63-3b38-9e4f-e75011588e39 | -5.80706 | -53.81647 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfc57bf0-bc37-3df7-92be-3777d8aebbad | -8.21181 | -46.00382 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b9d0bf6-196c-3cf5-91d3-8fe8c7f6fd19 | -9.4074 | -41.18141 | 2026-09-09 04:25:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3491efb4-63a3-3df9-a336-118a95e71975 | -5.36346 | -56.0254 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04df3e00-358f-3cf3-9041-63ed310217ed | -9.70759 | -43.40925 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 710e7441-ab1a-3b67-9353-fee81675693f | -5.3714 | -56.02057 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5460948-e8de-3609-b55a-dbd634a0fff6 | -7.19361 | -43.62318 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20bc4b9b-01d4-3d32-8075-df859350f8aa | -9.77468 | -43.45213 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60d91788-2613-3b45-9810-c21f50b3b16f | -3.54401 | -48.18604 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 988a8636-8719-37bb-9113-540613a44e5d | -6.16286 | -44.65321 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a4019338-dfa2-36ee-8890-c00ad4d60bc2 | -10.26619 | -45.2092 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c822cc47-2505-3164-bad9-3fcd777cb1c0 | -5.77198 | -45.06897 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02b686f6-e2b2-3825-896c-0d5ee58ed4bd | -3.5502 | -48.17503 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67dd9a57-8afc-33e3-8088-db2ea0f73aa4 | -7.52786 | -45.92796 | 2026-09-09 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05042497-af28-31bd-801a-a76aa4d0cc5e | -7.13196 | -42.12033 | 2026-09-09 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6c70e89a-1f86-3d6b-99bc-81fe626ce088 | -5.81741 | -53.81258 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86e6f5cf-b1c0-3975-a423-407da7360464 | -10.72136 | -46.05728 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3795123d-00f6-3398-aeee-afc0ac2fa3d1 | -9.70094 | -43.45145 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 697ca686-7fbb-328f-92c7-4821c8f6f15b | -10.69633 | -45.99951 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fb0da70-2bfc-3094-b82d-677889d47c34 | -6.16111 | -44.66413 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e36eceac-77ba-3f7f-86dd-9ee2f32af299 | -5.67673 | -50.09832 | 2026-09-09 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7da82793-3621-3787-8736-6b57311b1f7a | -10.35721 | -40.55994 | 2026-09-09 04:25:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2084dd48-84cc-3d0f-b75c-1c2b766ffb45 | -10.58456 | -45.7436 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d1b1aec-8509-3a02-9ed3-55ac00a45dab | -6.50574 | -44.69596 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db52c455-5721-3303-8e9c-a39b0b86d4cb | -10.47021 | -40.57457 | 2026-09-09 04:25:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 537aa382-f8d3-313b-8f55-d733ef10eba1 | -7.26538 | -45.35062 | 2026-09-09 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf3629b8-0054-34b8-966a-3b5a7908290c | -3.54604 | -48.17866 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09a007dd-b3f4-3154-aa02-fbd39b486526 | -7.68802 | -44.32 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75e06428-a77d-3028-ba10-0377b9efe414 | -4.37613 | -55.04801 | 2026-09-09 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d7632f7-18c3-346e-a27e-f6f920516965 | -5.36459 | -56.0192 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8e0c43a-84cd-3e73-afc6-21f53abc5615 | -11.00662 | -45.08423 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 01f37472-f5e5-3043-ad7b-fca761271de8 | -9.72756 | -43.39084 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2f58e829-ec73-3ed6-a0b9-abdce49222dd | -9.6965 | -43.43631 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0366bdd8-68df-39b5-a371-9ddc8c5a4616 | -4.91236 | -55.82362 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e7cf9c2-15c8-391c-9ee0-dbc77b670d90 | -9.77583 | -43.50994 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57a3f1b8-557a-3bf6-9dee-03bd9d4cafe0 | -9.70482 | -43.44847 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3a93a5cc-922f-3ab1-afef-80f83952963c | -6.16568 | -44.6574 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6e22454-7322-3ed0-86a8-76d034578c7f | -4.38372 | -55.04327 | 2026-09-09 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1ccc1f3-2c53-32b1-a8af-923f5153cf3f | -9.7037 | -43.41223 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 205446cf-0d7a-350a-acc4-0d4c6056f80a | -7.52851 | -45.92404 | 2026-09-09 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88bddf57-0ff8-36c4-b1ac-09957c1d076f | -10.7438 | -45.96461 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03f6c691-9493-368f-b8de-266db8d9ed39 | -9.74422 | -43.51567 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6301af2d-381a-3ea0-9f4d-43f68cb395a5 | -5.80114 | -53.81528 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README14.md)
