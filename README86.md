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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86af8023-58cc-330f-bbdf-ad2f69f4dff1 | -8.22725 | -44.35912 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 72d9a833-c1f8-38b4-bc9f-b6a386870b4f | -8.21403 | -44.35266 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b96aeb26-050d-3e7b-bfe0-6d2da4768bd5 | -8.21339 | -44.35731 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d012456-d8e5-3157-8583-6ffa7ac9a9fe | -8.20876 | -44.3568 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 544d1a9b-fe21-3060-aff5-7f17c0152a74 | -8.20811 | -44.36151 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17fdd232-c438-3c12-8ec7-bef958b75df2 | -8.20412 | -44.35629 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2bc2ea42-6785-3d59-a432-a1e45ba4a14f | -8.20347 | -44.36106 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a4fd19f6-d76d-3fa9-b655-69fc8245748d | -8.20282 | -44.3658 | 2024-10-02 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 437bd5fb-7d06-38df-94c2-b6f0fcdf94e8 | -9.31488 | -45.65863 | 2024-10-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17ffbcfa-45b1-31fe-a113-50e4320bb248 | -9.31062 | -45.65777 | 2024-10-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a972b5d1-6b2a-3ce5-b2b3-479c14412c7f | -11.67512 | -44.70808 | 2024-10-02 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79d3db63-a8ca-3951-bb15-38236002dc3e | -11.14775 | -45.95276 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 022e1217-ee3b-362a-9cf0-637267d50e13 | -4.98338 | -45.51571 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ab71453-225b-31ea-bc3d-50c93d416725 | -5.98431 | -45.37009 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 91d747e8-ba16-3b51-a2fa-0460969b0c46 | -5.98375 | -45.37388 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4ea1ed9c-adca-3e66-b734-d0210bafd8bf | -5.98228 | -45.36836 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fce5a047-1c5e-3ca4-bfd9-2d0b8961eab3 | -5.98174 | -45.37217 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| e5b59149-8550-35b1-bf40-3494cda43500 | -5.9812 | -45.37597 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| bd52815f-cce5-3413-b2f5-05266e13359f | -5.98016 | -45.36943 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b189f870-7d9e-3861-b32d-a032512d606e | -5.97959 | -45.37323 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e2b7cdd7-b8de-3dfa-a931-3ac74198cfde | -5.97902 | -45.37703 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8fa5b67a-4504-3bb4-9653-614746b41c57 | -5.97544 | -45.37254 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e4ddd897-f63c-3bb5-8f85-132463d0db0f | -5.97487 | -45.37634 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 76d5ee49-c32b-3206-9e12-a1b426955ea0 | -5.97431 | -45.38013 | 2024-10-02 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac970192-ba96-372a-b9f5-98370ada8faa | -5.9065 | -45.40838 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e792ba1e-ecfb-355d-9cdf-fed305394bfe | -5.44555 | -45.18308 | 2024-10-02 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f68e1560-b7c1-3628-bc65-08b42c35eab2 | -5.44498 | -45.18685 | 2024-10-02 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d215922f-a115-30c5-8df2-0d43fbc0fff6 | -5.44138 | -45.18233 | 2024-10-02 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b43ce9ed-05a5-3dd5-86b3-13db438f6ac5 | -6.23793 | -46.3794 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde72391-e422-3962-8337-efb3d5ba0fb5 | -6.23719 | -46.38432 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21aa662b-cb6e-3983-8ca2-8a48da90a915 | -6.18451 | -46.09285 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc608d27-2811-3e6b-81a8-00dd6d61bdfc | -6.13837 | -46.45382 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe5c1b73-5f40-3b69-9f87-0f55a18b544d | -6.13449 | -46.45321 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 411c2fcb-ab51-3c9c-82c8-332d9650784f | -6.06768 | -46.31111 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b200af8-4ff7-3e53-b8bb-241493da1004 | -6.02117 | -46.45883 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ba2246c-9a73-355b-92e4-e3b8fed9ef28 | -5.89785 | -46.29217 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4174620a-462d-36ea-b43b-a99321669ba7 | -5.85417 | -46.42677 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 010ef2ee-9d8f-34ad-b700-58ec55b2de7e | -5.85345 | -46.43164 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5e024d49-90f1-33df-ad52-0ddefe31b8e3 | -5.85029 | -46.4262 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1886787-b59e-3062-8ecc-4bf938e903f5 | -5.79253 | -45.96671 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f7b10bd-62bb-3894-9ca7-644c07a85f18 | -5.62514 | -46.45677 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3835f431-fca7-3b9b-a37b-350c39270c6a | -5.58138 | -46.31384 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82aa9cf3-13b2-3273-82e7-afd8729e9fcc | -5.5775 | -46.31323 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20c4d07e-a2d3-3996-a6dd-832e07a971c3 | -5.40698 | -46.00222 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d89ba3d2-4d88-37c7-9b47-a6c5a2aed218 | -5.38237 | -46.08661 | 2024-10-02 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d449649-8822-3750-af94-0d334503182f | -5.11607 | -45.99002 | 2024-10-02 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5aa60a6-d28c-3f56-84b9-41165ba73605 | -7.80334 | -45.47806 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba560bf7-2724-3c9f-9859-24cb8b9ea352 | -7.80302 | -45.47747 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68c447ae-83a8-3352-a03e-5aa21129e115 | -7.79909 | -45.47747 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06c3179c-34f5-381a-a5b7-40f09e34bb93 | -7.79854 | -45.48121 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f7d012a-a2fd-3e84-956a-2b5a19178262 | -7.79484 | -45.47687 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3386ec78-25b5-3223-aac4-790b184f75e7 | -7.7186 | -45.43365 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8cb8cdd-4060-340c-8469-69e5b7244d58 | -7.71806 | -45.43754 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 50f90dbf-dbbe-3e48-a2b6-39e7178e2f90 | -7.71753 | -45.44129 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 5cf6216f-0ab3-37b1-9e2c-f7cf0e41bb48 | -7.7155 | -45.42476 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 27b41181-195e-33c5-9484-b674724d2488 | -7.71491 | -45.42898 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e7e613af-de25-3a50-8c37-f0de080ab0cb | -7.71437 | -45.43291 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 53ae0acf-d020-344a-bb44-c32a944a7bc7 | -7.71382 | -45.43679 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 635055b0-8352-3e71-8891-6b472ddcdcae | -7.7133 | -45.44053 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd08fcde-34b8-3a7b-a747-70617e8fc59a | -7.70705 | -45.42302 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6167269-e3c5-3121-9a43-07cb49aa30b6 | -7.70009 | -45.44397 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3538455e-87e7-3c38-bab9-53e5518c9f2b | -7.70005 | -45.44221 | 2024-10-02 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21ffb686-17df-3e6a-8184-f4115b9097dd | -7.60035 | -45.50642 | 2024-10-02 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51301508-3a4c-336d-b1d3-d1e7c25b93cb | -7.09667 | -45.6689 | 2024-10-02 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9ab023dd-d19a-3e7a-9514-9aed14672fed | -7.09612 | -45.67269 | 2024-10-02 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c5da4f4b-96f6-38be-af0f-166036929038 | -7.09252 | -45.66832 | 2024-10-02 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 462278ea-bbc6-3dd5-b1c2-cf22694ac2ec | -7.09197 | -45.67211 | 2024-10-02 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8c6af78-8577-308d-9290-41f9fcecb089 | -7.06092 | -45.34893 | 2024-10-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07bdf581-29ab-34d3-a42e-734cf4cb9cd0 | -7.05726 | -45.3444 | 2024-10-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6767867c-fa27-381a-a99b-dd0cb2451ce5 | -7.04395 | -45.34663 | 2024-10-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7923fba-d2ae-3d85-8bde-c710275623b6 | -7.03972 | -45.34599 | 2024-10-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| affa26d4-1d26-3086-95c4-4a2cf9323908 | -7.00103 | -45.34449 | 2024-10-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c95ef28-995e-3d77-be84-3264b8c8193e | -6.96125 | -45.35091 | 2024-10-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48d5b572-7405-3c7d-97cf-097e14e84837 | -6.96099 | -45.35237 | 2024-10-02 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41e30f11-2728-3ccb-8c48-ff9ec4a14902 | -7.71673 | -46.15645 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3700650a-32be-3d89-afb3-11badd14a400 | -7.71622 | -46.16005 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c22eec7-e53b-332f-a9a4-67e8e6d28bd3 | -7.71065 | -46.16599 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 336911ab-5f16-3341-b4a0-5b440dd31850 | -7.51927 | -46.58892 | 2024-10-02 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b9862c4-0bde-3b67-8f6d-6f198c9d04f5 | -7.1026 | -46.44902 | 2024-10-02 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ef2153f-a5dd-3851-88da-072d3bc4c208 | -6.79038 | -46.02923 | 2024-10-02 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d8a30dd-0480-3209-8ad3-d2f643d5f6af | -6.78584 | -46.0322 | 2024-10-02 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc896b80-c34b-3bd8-afad-a6fe249be00d | -6.66033 | -46.67946 | 2024-10-02 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce0a2f13-977b-348a-b56c-ee7c96f1591d | -6.51942 | -46.23758 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e68a3e8-6dc7-382b-be64-d05f6edd12b2 | -8.92853 | -45.64608 | 2024-10-02 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f346fa-1ffb-38d9-b70b-907c64e1435e | -9.02196 | -46.59619 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 327fe30e-46ae-39ec-8367-c10615c3873b | -8.76145 | -46.81682 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fd9fdf9-aca3-3fc1-9a14-3e7e4f599c4f | -8.75752 | -46.81618 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f683c26a-14cb-3e1f-8ff5-81df16b2e87a | -8.75606 | -46.82635 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e23edeb-7a65-3bf1-93cf-d7a8a37ffb0c | -8.63048 | -46.53577 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ffe7d22-1a76-34eb-81ad-04363e87cd37 | -8.62945 | -46.54276 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ad6d173-6a1d-35aa-9513-610c339daed1 | -8.62853 | -46.53478 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b7f561e-b82e-36e6-9934-31bf68f08ff0 | -8.62803 | -46.53836 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dbdaf0a-7dd1-3761-a2bf-7b317d7bf7ad | -8.62755 | -46.54183 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d59bef5-4ad8-3060-88eb-ad3bbcdbb7d5 | -8.62648 | -46.53515 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b79745a6-a65e-3ea1-9060-145e2dba24eb | -8.62596 | -46.53871 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 792d65ab-d04a-38f3-9357-fdbf9d514998 | -8.62249 | -46.5345 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd01efca-6a52-3394-87bf-5fc6ac185f3a | -8.61849 | -46.53388 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6d864e4-2cfe-3a0c-95ad-003b8c20349c | -8.60995 | -46.53635 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77b2fb14-7008-3f54-bfe7-c2b87166c0d8 | -8.60543 | -46.53932 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05241236-257d-30dc-a1d1-26923c6b4a3a | -8.59794 | -46.5346 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README87.md)
