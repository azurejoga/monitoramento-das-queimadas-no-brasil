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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76a63147-13ff-352e-9a29-0216f74d09a6 | 1.3761 | -60.6722 | 2026-04-08 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 252a346f-8be0-3c7d-b7c6-c99b93c1cdff | -19.5959 | -40.074501 | 2026-04-08 00:04:00 | METOP-B | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e823521-cea9-3962-ad11-0d9d605b6c30 | 1.3696 | -60.6264 | 2026-04-08 00:04:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dfc24102-41b5-3a0a-9617-75e82c91c1d2 | -19.5982 | -40.084099 | 2026-04-08 00:04:00 | METOP-B | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af8b23f4-a524-350c-96aa-5ff666fc17a3 | -23.54301 | -47.6347 | 2026-04-08 00:16:00 | TERRA_M-M | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 806c1d74-de21-3357-92c2-5cca095ea034 | -19.60271 | -40.0848 | 2026-04-08 00:18:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| cdf1bec1-dbff-3957-a154-7858f9a8f170 | -20.90932 | -48.71769 | 2026-04-08 00:18:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 436ee471-3ee1-3e6b-bf6a-833f850e694b | -21.03271 | -48.81711 | 2026-04-08 00:18:00 | TERRA_M-M | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 1988ef82-9abd-3685-b17a-8e5a4b67cb4a | -21.0314 | -48.80689 | 2026-04-08 00:18:00 | TERRA_M-M | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 6c994197-cdb9-36e4-b6d2-27b2397bd6d0 | -21.27454 | -48.62888 | 2026-04-08 00:18:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c96f5ef2-5f6a-3a9a-8808-d2ef305e637d | -15.01641 | -45.12204 | 2026-04-08 00:18:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c6090ff7-5ba5-3838-b86c-557a72fa15e2 | -19.59825 | -40.07923 | 2026-04-08 00:18:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 67ca9cce-9d7f-3c84-8e13-da8f1a313b3d | -13.699 | -55.6977 | 2026-04-08 00:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 40b644a2-a375-3f1b-a609-e3646bbc9210 | 1.3579 | -60.6723 | 2026-04-08 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a0ffe6fa-bc28-367d-a1bf-a2c03f91f37a | -13.6993 | -55.6773 | 2026-04-08 00:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| cdd20162-3bb2-35d8-975e-d1d16ea01986 | -12.02169 | -45.24388 | 2026-04-08 00:20:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 47dba17e-1cf6-330e-9bb5-854661f9e213 | -13.70235 | -55.68716 | 2026-04-08 00:20:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0656b7c4-7f70-38c7-b1bb-f7b3d049e456 | 1.32634 | -60.62816 | 2026-04-08 00:22:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 964c1d0e-93d9-385b-971d-cce51ea77402 | 1.31564 | -60.61993 | 2026-04-08 00:22:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 8fafcf75-f757-32e5-b4c5-bfc09691078e | 1.36846 | -60.66581 | 2026-04-08 00:22:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5680778a-7e9a-396a-a9b3-83e9eef0f5b4 | -5.50619 | -35.59956 | 2026-04-08 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1e2c2952-6ab5-3352-8d40-0b8f4544817f | -5.53357 | -35.51806 | 2026-04-08 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e0940b5-83c6-3675-ba94-5a070e9297ee | -4.97924 | -37.22931 | 2026-04-08 03:36:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9d87e326-1c98-3caa-945c-5a074dfa0563 | -4.98302 | -37.22991 | 2026-04-08 03:36:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3bda8bd2-d9ca-3d49-a181-504384fbbf1c | -5.53296 | -35.52185 | 2026-04-08 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dfc66c59-152a-308f-a6fc-b00fcc0e9306 | -5.52888 | -35.5251 | 2026-04-08 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59a115d0-7ac2-3255-ba30-eb29d792fde1 | -5.5295 | -35.52131 | 2026-04-08 03:36:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 723525ae-08a6-3496-b022-6dd8adf0de35 | -8.96106 | -37.17682 | 2026-04-08 03:38:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2578333b-706a-34fa-8282-f3280a7cb373 | -9.76722 | -37.61124 | 2026-04-08 03:38:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbf2c1e3-701e-33d8-8f32-3d69f18681b2 | -12.02797 | -45.24594 | 2026-04-08 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85e3441f-05a3-3458-8dd1-300213b3f275 | -13.03343 | -45.07096 | 2026-04-08 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6373500b-4fe6-3e75-a4df-c2e71cea653c | -12.58359 | -39.10022 | 2026-04-08 03:38:00 | NOAA-21 | GOVERNADOR MANGABEIRA | BAHIA | Brasil | 2911600 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a11a0b4-8e26-3d2c-8344-8857da457ad0 | -12.0262 | -45.24591 | 2026-04-08 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65c6185d-9d32-38b6-831a-b3081ad5c047 | -13.03418 | -45.06728 | 2026-04-08 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 647cf8c7-c43a-35c6-815a-ae60b4028024 | -9.88023 | -37.28607 | 2026-04-08 03:38:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eeb91d53-dee1-3e5c-9f34-cb8ebabd4057 | -12.03189 | -45.24705 | 2026-04-08 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa6cd382-2735-3970-927f-f01665353eb8 | -12.04523 | -45.33741 | 2026-04-08 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2f86d59-9383-3dbc-81b8-c427e82057c8 | -12.01326 | -45.25164 | 2026-04-08 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b6ca4ae-0393-347d-a654-20f5bbab78fd | -12.02148 | -45.24881 | 2026-04-08 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0eeb193-e341-3cb4-8b35-2903e59f7021 | -9.88293 | -37.28536 | 2026-04-08 03:38:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f6d07ca-c4ca-3c47-9c6e-04f98b03f41b | -12.01973 | -45.24878 | 2026-04-08 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dab7dd92-b6ff-3a18-bdf3-9d9322ad2b8c | -9.88295 | -37.20235 | 2026-04-08 03:38:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a205c63b-8e0b-3c79-bfc2-0906403fa1d3 | -19.59994 | -40.07398 | 2026-04-08 03:40:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b07a80d2-0327-312d-8958-9a23e9a82498 | -19.59916 | -40.07844 | 2026-04-08 03:40:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 76a6338f-e748-3eaf-a708-48c913e01534 | -19.58543 | -40.07119 | 2026-04-08 03:40:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e3297067-f4c6-3452-ab69-bcab049b1f92 | -17.12267 | -41.26083 | 2026-04-08 03:40:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bbf3c63a-58f5-329a-afb2-4e48af1a0ee3 | -5.53132 | -35.51704 | 2026-04-08 04:08:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 41cd5a16-c517-3809-b390-1635db62934c | -5.5306 | -35.52182 | 2026-04-08 04:08:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1ad16c76-1c29-32d7-8b93-2b97553fcfb4 | -4.97911 | -37.22861 | 2026-04-08 04:08:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 69e916ec-515a-313c-8eec-f17769aabca9 | -9.7645 | -37.61111 | 2026-04-08 04:08:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13ae2687-0ce3-341c-8425-ac267e2d5392 | -4.98261 | -37.22916 | 2026-04-08 04:08:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8790b9fc-1807-38c1-a3c6-8c8c799a51c7 | -12.0422 | -45.33677 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b2485cc-baf3-3f34-a2a8-a4277abd7cae | -13.69971 | -55.69116 | 2026-04-08 04:10:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d7f1d3ff-deac-390f-bb46-6a9c1c53fdb5 | -13.69731 | -55.69018 | 2026-04-08 04:10:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b675af0c-ca7b-3e91-ba44-92cda2294e90 | -14.44195 | -45.63074 | 2026-04-08 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 959bba8e-bb5e-37fd-892b-86c1b94372d9 | -13.03202 | -45.06928 | 2026-04-08 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab912dc8-c078-395f-ad80-622eff4f42e2 | -12.04598 | -45.33748 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eb07ae5-8feb-39b6-8cdd-8a3bdad7b7c4 | -12.01798 | -45.25072 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae643a59-76ac-3ce7-97b6-f185ec92bc8b | -13.47197 | -42.98009 | 2026-04-08 04:10:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f50f8723-34cd-3f3a-a483-952eec97cc5b | -13.69123 | -55.69644 | 2026-04-08 04:10:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9fc824c-acaa-3bb5-b34b-42ac9cd37e0c | -13.69574 | -55.6972 | 2026-04-08 04:10:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ff3b79ae-c9c6-39ed-9400-4b1ad830e24f | -12.02254 | -45.24676 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e0c53f5-3ce8-3309-84fb-0841baef88f2 | -10.05228 | -38.28329 | 2026-04-08 04:10:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da039ada-8b92-39a2-b4c7-05291ed7a9e2 | -12.0263 | -45.24744 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aca4571-6dac-3442-9745-5dbda0e4a987 | -13.0357 | -45.06994 | 2026-04-08 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab8447f-4109-3dec-abe7-cd12ce605cea | -12.01421 | -45.25004 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac8c859f-300a-3861-b15b-1d4cdaf2a25b | -12.03007 | -45.24811 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29ae3ba6-adc2-3a6e-be8c-690be004d9de | -13.6982 | -55.69817 | 2026-04-08 04:10:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d5700c4-c2f0-31e7-882c-242e5c6b582f | -13.21448 | -43.69012 | 2026-04-08 04:10:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93fb8201-9cc5-3fa7-ae53-44d56ebaf6b2 | -13.95743 | -43.26612 | 2026-04-08 04:10:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a60bb47f-a713-3b0b-94e1-c3da16bf9474 | -12.04511 | -45.3396 | 2026-04-08 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5105ac14-f6f2-3da0-acd7-8da3ed0b71de | -13.69275 | -55.68943 | 2026-04-08 04:10:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35fa2ef1-db65-34e3-8394-3f5332474d9e | -20.54708 | -41.59085 | 2026-04-08 04:12:00 | NPP-375D | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ac47c092-11c2-3d32-aa65-b60215dd9127 | -19.59839 | -40.0804 | 2026-04-08 04:12:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4daef859-361c-3faa-bbdb-bccf976e6cc4 | -19.60256 | -40.07669 | 2026-04-08 04:12:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8ed14b3-ec19-3f2e-8e53-2dbc0345aae3 | -19.59899 | -40.07613 | 2026-04-08 04:12:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3e1f14cc-61a8-33ee-afae-73bb98bf24d0 | -21.40821 | -44.05145 | 2026-04-08 04:12:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b166a5e1-3451-3bf7-a6c7-24647f1578b9 | -4.98063 | -37.22826 | 2026-04-08 04:27:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7335d422-a02a-387d-93b6-58c459b47be8 | -5.52949 | -35.52414 | 2026-04-08 04:27:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca21c8c2-cc0c-3cd4-8872-3bc49daeab77 | -4.98018 | -37.23141 | 2026-04-08 04:27:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 90d22fcb-7875-334f-a143-9ab32e67adb8 | -2.32964 | -49.08424 | 2026-04-08 04:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 403ba704-3026-3136-85e0-5c35e13d3466 | -5.32461 | -46.94976 | 2026-04-08 04:27:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d597f3a-bf6e-3edd-b813-b7c2aa2d4086 | -5.52881 | -35.51902 | 2026-04-08 04:27:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24a4a83e-15f1-3d73-aa92-b541a6016d6d | -9.00779 | -44.39434 | 2026-04-08 04:27:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cec37127-48b5-3314-ba98-09304e2261c1 | -5.5301 | -35.51991 | 2026-04-08 04:27:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| effa9d72-f30d-366b-b3c0-5547c6dc6adb | -5.52823 | -35.52326 | 2026-04-08 04:27:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8c9dc3d7-8c27-35de-9770-683a9a1a3ec4 | -13.47222 | -42.97611 | 2026-04-08 04:29:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c6817fee-0102-3d5c-98d3-ff558291199c | -14.44204 | -45.62823 | 2026-04-08 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc503d72-e36a-38d0-9f85-e216732a67bc | -12.04306 | -45.3351 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89cde706-2901-3d4f-b74b-2fa45b7e123c | -12.03151 | -45.24576 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f98ed2f8-0337-3d87-ac6a-a2e82ce02f1d | -12.01297 | -45.2509 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b8b8e5b-2a66-3614-8d73-a84d0c353b96 | -12.99426 | -54.67933 | 2026-04-08 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48d0d7ba-02af-3b1e-8968-e53d961fbe7f | -12.0205 | -45.24806 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09779e37-750c-374a-a049-9193b0295454 | -12.99342 | -54.68386 | 2026-04-08 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcfe07f1-a043-3741-8bf5-24e0547dede7 | -12.01702 | -45.24752 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 079f3f68-007b-3f6d-8261-b41692bfefca | -12.04248 | -45.33897 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78dde2bc-aba2-3b14-a9be-36640cbeb18b | -13.21388 | -43.6897 | 2026-04-08 04:29:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 087f7673-6826-3a9e-85b0-2faa6bb3a38d | -12.02804 | -45.24522 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13b2ca29-0167-31f8-9835-344d0d19415c | -12.02398 | -45.24859 | 2026-04-08 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56783c94-1b6c-3210-b996-c9ba76bfa3ec | -11.93428 | -54.45899 | 2026-04-08 04:29:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README2.md)
