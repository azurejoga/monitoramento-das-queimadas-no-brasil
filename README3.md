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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da303787-76a1-3917-a5e5-251710208699 | -7.8792 | -43.92522 | 2026-06-07 04:04:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1a45b13-b7b9-3fa7-8407-b4a812680e03 | -8.94254 | -45.67464 | 2026-06-07 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee2214c1-ca3d-30fd-b635-4ca61bed5397 | -6.43778 | -44.5832 | 2026-06-07 04:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c45ffd01-43d8-303c-86e1-793d2c21755b | -6.98292 | -42.87873 | 2026-06-07 04:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6771a2e2-704b-3a84-bd47-0ce42fbc880b | -5.94364 | -45.50362 | 2026-06-07 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 896669d5-d697-3de6-8bd6-a2a6ba11b0fc | -8.93383 | -45.6768 | 2026-06-07 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01858985-c0f9-3f27-a769-6b971e440290 | -5.93944 | -45.50293 | 2026-06-07 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f9a0ac5-c146-31ee-854f-e56baf944ca6 | -8.83266 | -44.21212 | 2026-06-07 04:04:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac7c281e-8245-30cd-b112-82ef5845bf78 | -6.91353 | -43.62193 | 2026-06-07 04:04:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0f040cc-0abf-3084-98cf-96f4e9c44b86 | -7.18236 | -46.55012 | 2026-06-07 04:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9591df09-8128-3df4-b6df-2a6de962ebe6 | -7.15754 | -44.06483 | 2026-06-07 04:04:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df31ff19-7864-3c10-a471-842b3a703c66 | -7.32165 | -47.07449 | 2026-06-07 04:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02ff1ecf-1331-3d21-a41e-2edb205f43fe | -7.18594 | -47.09653 | 2026-06-07 04:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a0d6527-419d-350b-bcc5-7d8f3bd750ff | -7.15378 | -44.06421 | 2026-06-07 04:04:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a438496e-32b6-3dfa-bdb6-1e32db55117f | -8.94317 | -45.67106 | 2026-06-07 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da0b7b68-bcf1-31cd-8766-76958b3b277c | -8.02903 | -46.05057 | 2026-06-07 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3977554-9f2f-3651-9ea5-ccd150ea0c82 | -5.9111 | -45.54207 | 2026-06-07 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e09defcd-3a3a-3cef-b8c6-474605922854 | -7.11574 | -48.13083 | 2026-06-07 04:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a33e6268-413b-3139-a1fc-f8a1c1674ee5 | -4.653 | -43.15377 | 2026-06-07 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3dfe619d-a993-3f95-a308-655c455acde2 | -7.87849 | -43.92952 | 2026-06-07 04:04:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b91f03db-b10a-3561-be89-e40ef57df7f4 | -8.02836 | -46.05439 | 2026-06-07 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 028ddf28-5d49-3092-b608-55e1eccb7200 | -6.99744 | -43.86105 | 2026-06-07 04:04:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c8a6f38-b3e6-3ef5-8698-abcf7eb5e7a8 | -4.84135 | -42.9165 | 2026-06-07 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fc9c582-6257-39f8-9273-a34df549f090 | -5.94429 | -45.49979 | 2026-06-07 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bd9b8a3-6219-32f9-9aff-10295ec2cf59 | -7.18674 | -46.5511 | 2026-06-07 04:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8901afe3-eb07-3e34-a1e7-e02e8dfec609 | -7.00116 | -43.86169 | 2026-06-07 04:04:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aecbeda1-f300-3617-bd35-dd0ea24b543a | -8.93349 | -45.67651 | 2026-06-07 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e515ee7-1177-3e9f-aba7-415664ae8419 | -5.91043 | -45.54595 | 2026-06-07 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fcce82d-e6f8-3da4-beac-7481e87c0d5a | -5.9401 | -45.49906 | 2026-06-07 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cbef5a4d-72cd-39e8-b816-c53733ef168e | -12.40706 | -47.49176 | 2026-06-07 04:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15aabd58-7b83-3a1f-989b-2f71a286b573 | -10.18871 | -52.65406 | 2026-06-07 04:06:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 533e8226-7c15-3f86-a8ef-41851c8e99d2 | -12.49802 | -46.26204 | 2026-06-07 04:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe337826-0dbc-3c00-ba9c-c1f1ef48cc52 | -10.83593 | -53.75213 | 2026-06-07 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17623b82-4228-3618-b599-e067c32ed574 | -11.97822 | -47.36007 | 2026-06-07 04:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 838a5f95-853b-3aed-9c2e-dba5d965517f | -12.06312 | -48.43167 | 2026-06-07 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 632da193-5951-39c9-82ec-0ad2159d846e | -9.06993 | -50.59467 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 988908b3-e88d-30d1-b09e-8c1b09cef725 | -12.04055 | -45.26971 | 2026-06-07 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 555144bf-7d16-3e3f-94e9-fb9d75c1542b | -9.07063 | -50.59092 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e0656b1-499a-3f39-acf5-4ea2a6693df0 | -11.54182 | -52.79343 | 2026-06-07 04:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db0562dc-8039-3552-ac09-2724e03589f6 | -11.26357 | -53.96527 | 2026-06-07 04:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5a8ad67-1c33-30b4-96ed-45ed23ac277a | -9.08528 | -50.60558 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff42fcd-787e-32a7-b76d-ee2ef92335d2 | -10.09433 | -47.06253 | 2026-06-07 04:06:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40f30fa6-2a0b-3fc8-8931-274773e4c322 | -15.65918 | -43.31701 | 2026-06-07 04:06:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d71d163e-991e-3a5e-876c-a2a801062b9a | -11.5583 | -52.80689 | 2026-06-07 04:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e6e3c87f-46eb-35e6-847b-332c51c41dee | -10.85132 | -53.74377 | 2026-06-07 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f95c2c15-e082-340c-b871-9e6dc1898df5 | -12.06772 | -48.4326 | 2026-06-07 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f070b263-6651-3dd5-a2c6-0d3afd94b241 | -9.09227 | -50.59917 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4da55fd1-5893-3948-b89c-235312f8e58a | -10.1825 | -52.6527 | 2026-06-07 04:06:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce5cc5b6-3d1d-3f17-b21e-75b12e1325a3 | -11.55511 | -52.79099 | 2026-06-07 04:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72baa968-a111-380f-836a-9d8a8b9b1221 | -12.04362 | -45.27303 | 2026-06-07 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36499726-e5eb-3cd0-ab77-5c8e8e873d12 | -11.54798 | -52.79458 | 2026-06-07 04:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 02bc6e82-3343-3c0c-949b-d764d2e62ded | -10.85245 | -53.73819 | 2026-06-07 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2bc220b-17b2-3e2b-8fd1-2823e7b743b9 | -9.10595 | -49.64596 | 2026-06-07 04:06:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 234d69d1-d3d7-36a1-b6c1-72ecbbcd11b5 | -14.2459 | -47.9702 | 2026-06-07 04:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc7fc22d-9783-3554-99ad-52efbbda1787 | -10.40662 | -46.41406 | 2026-06-07 04:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec7ffe5e-0853-35c4-b1a3-a75aaa24f799 | -13.36019 | -43.20477 | 2026-06-07 04:06:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0a0c4c50-76c3-35b9-8396-65f3418c521f | -12.97631 | -40.64885 | 2026-06-07 04:06:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| f34974b2-79ee-3c1a-ae15-480742c9f522 | -11.56891 | -48.14207 | 2026-06-07 04:06:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed4b3fd8-91c8-335c-9e43-e7cd783031b5 | -14.25014 | -47.97134 | 2026-06-07 04:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c328c662-c655-387d-843d-5a2f20abbd5a | -11.26897 | -53.97264 | 2026-06-07 04:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83e05337-03b0-3171-ab18-1daa0da216da | -9.52089 | -48.68695 | 2026-06-07 04:06:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d090adb6-d2e8-3cf3-b636-f5d2951a0119 | -11.55117 | -52.81054 | 2026-06-07 04:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9ed4a3f-6531-3063-bb94-2c60257fd961 | -12.50684 | -46.2584 | 2026-06-07 04:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d20ea695-91d9-385d-a131-efbf4be53b55 | -9.09157 | -50.60294 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8214ca5-27e7-3a5b-955f-58276e7ee6a6 | -10.98664 | -45.09473 | 2026-06-07 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47328a53-be13-3c4d-9f6a-de6bb07fec95 | -12.49591 | -46.27421 | 2026-06-07 04:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52111ef2-bcae-3a0a-8ee1-d8c3e8deda83 | -13.3608 | -43.20105 | 2026-06-07 04:06:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| dc7ec5b2-ee36-3927-a6ee-005e25e00c15 | -12.97298 | -40.64832 | 2026-06-07 04:06:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 12ac382b-e257-3f71-80e1-239164953954 | -12.40631 | -47.49596 | 2026-06-07 04:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d61b76e4-7caf-35bb-96c4-de2c3fa5c020 | -12.06862 | -48.42772 | 2026-06-07 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1329a74c-6965-3c8a-8d72-fb573d62e237 | -11.03117 | -44.31636 | 2026-06-07 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c78a33c6-365f-37fb-b254-56fdc67425e5 | -8.86699 | -50.19049 | 2026-06-07 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a409c23-da38-3b56-b929-ffd4ed0d6470 | -13.36418 | -43.20163 | 2026-06-07 04:06:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d79522aa-4938-3c98-abd2-01b64e4b4df1 | -13.36357 | -43.20536 | 2026-06-07 04:06:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9d2b5b43-3230-30d2-a9c7-eb2bb8827ed5 | -9.08458 | -50.60932 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a674ff2-94f0-3ba8-9644-c3335ea79085 | -11.47508 | -47.34407 | 2026-06-07 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4c46c143-6741-321d-afe5-6a187bdd3cf9 | -8.86633 | -50.1941 | 2026-06-07 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90c9814a-b1d5-3f09-a61a-e898da8174da | -13.08768 | -42.1378 | 2026-06-07 04:06:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3bdb7efb-a8ec-3a15-bee3-a7fe3ec282e4 | -12.40843 | -47.49481 | 2026-06-07 04:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4947d54e-9b30-3e34-b0d2-a7dc0e72cc7c | -12.04432 | -45.27039 | 2026-06-07 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf853b54-045d-3be1-b937-66f646d94268 | -12.06193 | -48.07752 | 2026-06-07 04:06:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 881b31f1-8825-3659-845d-0ca885a7adef | -10.1897 | -52.64906 | 2026-06-07 04:06:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ec0a7d7-9498-335d-ac1f-d964b7430e3e | -12.03973 | -45.27436 | 2026-06-07 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f38ae7d6-68fa-3536-b15b-4bcf666a70a7 | -12.06482 | -45.97295 | 2026-06-07 04:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ba95cae-3dc4-34ad-9cd7-45174df44494 | -11.87499 | -43.90015 | 2026-06-07 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc11f485-b7fe-336d-ab8a-32ccac3f1a7f | -12.49991 | -46.27477 | 2026-06-07 04:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8994e0a2-4b95-397d-a885-5ebe2c87cd6e | -12.49897 | -46.25658 | 2026-06-07 04:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80523f6f-8328-3684-9ab1-f243be35cf5a | -10.09482 | -47.06416 | 2026-06-07 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eada0235-10c7-35af-97a6-03a9f0af7aa0 | -10.85901 | -53.73958 | 2026-06-07 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c37e176c-2567-3f88-b7e0-bf8b498c6742 | -9.09087 | -50.60668 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c935e36c-48fb-3ac5-960a-24a3d59ff6b4 | -9.07481 | -50.59952 | 2026-06-07 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 074bfbe0-ec6c-393e-aa43-dedef127888c | -10.09361 | -47.06671 | 2026-06-07 04:06:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbb5bd91-38a7-31ae-ad39-2990a351b7e2 | -10.98601 | -45.09659 | 2026-06-07 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee0d452-032a-3e5f-9bff-7c78f3d491d8 | -14.24165 | -47.96915 | 2026-06-07 04:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9bd0b7d-4b07-3ba6-a75e-7b84f3348df3 | -11.54897 | -52.78967 | 2026-06-07 04:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a270cf67-77ad-3c67-a473-e1ce31367896 | -11.68069 | -44.8693 | 2026-06-07 04:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52e8c9b9-7907-346c-b3b6-ba17c5b72380 | -10.84248 | -53.75363 | 2026-06-07 04:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 287d1c88-7152-3bf6-b9f2-c7b865ee5000 | -11.47152 | -47.3391 | 2026-06-07 04:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b239da77-690b-35bb-be90-443c191797f7 | -11.47038 | -47.98509 | 2026-06-07 04:06:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1fca551-26ba-391d-b797-e98cd3fc4081 | -11.03044 | -44.32062 | 2026-06-07 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
