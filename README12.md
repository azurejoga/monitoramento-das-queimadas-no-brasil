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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3168a407-b6d3-3981-a0ce-2211b6447ae8 | -6.01002 | -47.39967 | 2026-08-11 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14a53f6c-4a55-3cc2-8484-03fe247e8fec | -8.91274 | -46.91301 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5e4341b-70c8-3403-8e23-1eec19686638 | -8.54051 | -45.34267 | 2026-08-11 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4dedec4e-0179-334d-b675-c31ec810227b | -9.47058 | -60.5369 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19cf7837-c36d-3670-91ef-021700b08550 | -12.45595 | -45.3055 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a6264ec-56d3-3b25-aebc-f4280abe6d2b | -8.89259 | -60.56308 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dffc151-9a6c-3d8d-84d2-357399eb4ae6 | -8.95893 | -60.57159 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74c1a235-9d43-352c-ae40-aaeba15ede79 | -9.47784 | -60.53303 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b3f384d-7b4f-3e59-b379-039845f0a88c | -6.84204 | -56.41459 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f19dde53-3041-33cc-a6e6-ba54e7933cd6 | -11.4913 | -54.60435 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 574d241b-ec7e-3b38-82aa-540a1bf43a1d | -10.93614 | -57.11498 | 2026-08-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f6237e4-0a6f-345f-bebb-d0c610686d52 | -11.45427 | -46.67384 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7e9ce3ed-213a-3caa-b9ba-19e011c2dc27 | -13.51987 | -44.13789 | 2026-08-11 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5af390cc-62f8-31b6-a052-3cd6f48bea17 | -11.02201 | -45.65159 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5995e2a3-f435-3212-ba58-490d265916e1 | -13.5692 | -46.27822 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 72b7790d-a77c-37b2-80e8-1817e665ff6b | -8.95909 | -60.50195 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5c8add61-b7d9-3337-91fc-a1755b9f285c | -12.48149 | -45.34267 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 15bc6ea0-5c32-34b2-94de-6dbf0e3f2b54 | -10.22106 | -45.86601 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9fedeefa-ba01-31c2-8b8e-1867900d2cd6 | -8.89508 | -60.58491 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e44f00f0-8f19-3890-87b7-0a1c246b1d95 | -7.37611 | -42.86115 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55e59483-12ab-3d23-a9ef-dc1ef9952870 | -9.15083 | -50.89882 | 2026-08-11 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d457e3-7958-3884-b6be-1e9fc6557bbc | -8.94547 | -60.50473 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 144d0175-a2db-3e11-9db8-6981068701c7 | -12.4905 | -45.30602 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e2d5d84-89db-32fa-9e5d-32ab2f4be08d | -7.616 | -42.78088 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2992f576-9dac-3ff7-9423-e537131b794c | -12.48937 | -45.28673 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd95011-2605-3984-adfb-c360708fc9ba | -13.56135 | -46.28137 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 38516b59-af6a-381e-b1a0-96c75d137481 | -11.97538 | -46.35254 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99ef5527-afcf-3a9c-9f67-cc17b67acfda | -8.94686 | -60.53162 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 155c765b-5958-3c3d-92d8-7e93a0c0ede9 | -11.98074 | -53.46247 | 2026-08-11 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4a21582-ff8b-32d7-a5a9-9f04a3fcb7a9 | -7.71759 | -46.22013 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d99b13c0-731a-31b0-8372-fb21aff308a0 | -13.57468 | -46.26592 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 26068c36-7bce-3458-b2f4-0b78c6f6d70e | -9.48616 | -40.31217 | 2026-08-11 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 6c367651-be76-3595-b9e4-dd105125f05e | -11.47166 | -46.65276 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9f527ed-dfd1-344e-a137-eff1d28e48ae | -8.95953 | -60.53396 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aeb76505-9c75-30aa-8cc4-96118f0c060b | -8.96006 | -60.49688 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7a310e0b-dbeb-3442-8020-f6b7602ed9a1 | -11.48137 | -46.62103 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9965413-7f8a-3614-a959-1b33c84bfc28 | -7.84354 | -45.89589 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5db3eb6-b7c5-3f89-b7b7-01ca8896228d | -13.55767 | -46.30697 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f5f0cf82-5144-31fe-ba31-74c4a9a43a40 | -6.72088 | -58.93705 | 2026-08-11 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8c0eb83-6547-3f22-8688-dccf15af8858 | -6.84708 | -56.41546 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f93b79ef-82cd-3d39-9ea5-fa8cdd416459 | -7.62117 | -42.77415 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d08c8f6b-9811-3a36-b3ae-c157ac862212 | -9.14211 | -46.39142 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f563696-9289-3a12-8ac3-b4456684a9bc | -11.23138 | -54.85231 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44842427-387e-3f61-bc78-d3495d4d4db2 | -8.23525 | -46.25019 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe297a2d-332d-38b6-9885-483fe02c99fd | -8.89164 | -60.56817 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9afd4d80-42d5-38ac-a4f2-eff306be1a47 | -11.96592 | -46.34271 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 176c15be-c49e-3e3e-b53d-4777b0f05644 | -8.30158 | -46.39061 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8535d03a-60e4-369b-8d0b-ecace5668abc | -7.3802 | -42.86178 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 254a2e7c-72e3-3996-b563-b892dde6e55f | -11.96772 | -47.31579 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bea97586-7d90-396a-b345-6408eb1fe093 | -10.1096 | -46.20367 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1dadb5f3-3d95-3520-b889-28b5261a60e3 | -11.25778 | -44.89596 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a55118c-df43-38ad-9b8c-1a74d96df63f | -10.8892 | -50.37403 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c5d6107f-caf5-372e-8b10-6a02fbcf95bf | -10.42765 | -46.67352 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 661e4f49-9907-3def-bc8f-c4758cac305f | -9.8966 | -60.2668 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38b104c8-12c8-365c-b7a9-74f10a43c3ec | -11.45072 | -50.72934 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4752cea-4fe4-3f10-9c0d-cbef2880e514 | -6.84297 | -56.4146 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5031a7c1-31f2-3f28-94d6-f2b59368a76e | -8.89068 | -60.57329 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a3bd5e4-3a0f-3e40-ad54-5247ad88cefd | -10.11369 | -46.20024 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 866ea03b-2d5b-317f-b8b5-97867a9db51f | -11.45601 | -46.68602 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cd05d949-e7b7-33fd-9e89-31a5570e32b0 | -11.02326 | -45.64294 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 932838e0-f844-38a0-8fb6-2a183ffdd575 | -8.8914 | -60.58064 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fff1cbbf-97ee-3209-adb2-238b44168473 | -11.45311 | -46.6816 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 81daa748-b0ec-31c9-a1ad-eedc1307cf8a | -11.4676 | -46.65609 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d2488b-62df-3c4e-b767-d230d4723782 | -11.95587 | -46.33688 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4ca60c2-e2f9-30ad-a9b5-a36b95478edb | -8.90047 | -60.59129 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cf531634-d386-315d-9427-0c1a15291196 | -8.94449 | -60.50982 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 84f0a3ab-0eff-3c7d-bf2f-4324529ab55f | -8.95462 | -60.55972 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6ab8087c-807f-3600-8ccc-b3de81ac4fb2 | -11.48488 | -46.62146 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba1914be-c97a-35bd-9588-2049d78ae566 | -12.48739 | -45.30081 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5ee7f4f9-e0ae-342f-9720-08c8790c2f2f | -11.54358 | -50.25843 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3645093-3948-36c1-8692-653a6a97dc6b | -11.95615 | -46.33837 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cf47615-a1ed-36f0-8dd0-373fc07f00ef | -8.95219 | -60.53808 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2903ff1a-8a7a-307f-ba5e-43cb90a2f9a9 | -10.72862 | -50.43721 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffff223c-0000-3a2b-b91f-1c1ba418e404 | -9.39844 | -47.4488 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ca82046-5836-3cc7-8326-69ebd961a74d | -6.84759 | -56.41256 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b9e40f0-204c-3bf6-a1e2-42fcab0f4d85 | -9.39569 | -47.46665 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1e5472a8-8627-3460-bd55-8c41977153b2 | -8.89673 | -60.58708 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a1d5d785-d5f9-32e2-b057-a6ed614abe33 | -8.66103 | -54.95508 | 2026-08-11 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67eba091-25da-34e0-90b7-395655b01481 | -13.07512 | -43.06118 | 2026-08-11 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da3c80b6-7a32-34ce-8f29-7fffa7c5c9b0 | -10.23836 | -45.82253 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07e61f60-7253-3ee9-8f4a-1a0751c020a9 | -10.89199 | -50.37822 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45c19b54-e3f7-35e6-ba98-5088033a8270 | -6.8405 | -56.42326 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b193692e-b6f8-3637-a66b-087c91e10569 | -8.95995 | -60.56622 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d527744d-1d66-3123-b079-2078f62159d0 | -13.56251 | -46.299 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f12bd45a-ed14-3a7a-972f-41478ab72a6d | -11.24752 | -54.83495 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53185050-fb7e-330f-a730-b5d5d468cd26 | -13.59284 | -46.24889 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b85ddab-bd12-36cf-b0eb-045a3c441968 | -9.37203 | -57.36533 | 2026-08-11 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b88af5f-f1e8-3016-a6de-327d8a2dfa92 | -11.5907 | -54.48678 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 553702c9-9991-32f7-89ef-57c09acdba61 | -13.56682 | -46.26912 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 62df805b-0de0-321f-8331-a00d9dbda5c0 | -6.31112 | -51.13057 | 2026-08-11 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f90b111-826b-3342-b348-2634f8cc1912 | -10.24062 | -45.85692 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 360b0aca-a258-3e4f-bb2d-ff8a24513291 | -13.5662 | -46.27338 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 280dc0ec-e375-3890-a901-4eaccf43ed6d | -10.93718 | -57.11844 | 2026-08-11 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fff6fbb-75fb-33fe-961c-fdc2700bd5ee | -9.38505 | -47.44668 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c312cc5e-1b7b-3fbd-bf43-bad6424d1d50 | -8.89895 | -60.56422 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 18dc0c33-e02e-3398-ac96-cdefc9bcd8dd | -10.88979 | -50.37039 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a75578ac-e3fb-3970-a37f-f3a8690a69c3 | -13.57945 | -46.28413 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e81e0cea-b730-309a-b698-35412f3b282d | -11.95754 | -47.33721 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c68575d-6c69-3e7e-98a0-910e226d527e | -9.9986 | -48.55914 | 2026-08-11 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04045cd5-f8be-364b-b87d-2bc98f2957bd | -11.46936 | -46.6204 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
