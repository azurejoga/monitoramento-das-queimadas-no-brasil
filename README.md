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
| 3826550c-9aa1-36b8-9bae-b06bab351d6d | -7.7444 | -45.0762 | 2025-08-01 00:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6f3df8b1-cab3-3ce8-9cc4-c6db91541346 | -6.7478 | -59.1716 | 2025-08-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 35082abb-2756-3065-bc3a-4d5e0b22021b | -10.434 | -47.2601 | 2025-08-01 00:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 540befec-3975-38e3-8157-65d86c540d5c | -6.5629 | -56.1906 | 2025-08-01 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8c6a1339-91b9-34ad-80a9-e62aa50a9b92 | -6.526 | -56.1923 | 2025-08-01 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ede29942-c541-3d85-983c-18cc32886bab | -18.6704 | -52.5973 | 2025-08-01 00:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 3dcaacc8-10a2-3198-958f-acb6fe3f4799 | -6.5443 | -56.2113 | 2025-08-01 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 02557b27-32ec-34cb-94f4-7a5de58f9c67 | -8.051 | -43.1237 | 2025-08-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| 9927d284-3a03-3d47-9231-70ea350120d4 | -6.5074 | -56.213 | 2025-08-01 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 2ed8f2ef-9a6c-3bb1-b79c-56a5b81b68cb | -20.8755 | -49.0699 | 2025-08-01 00:00:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.6 |
| d0c580b3-1d1f-3ba3-af78-b14bef72328a | -6.6376 | -59.0988 | 2025-08-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6eb109b8-30f2-3c2b-a58f-d8086ed0f820 | -6.7295 | -59.153 | 2025-08-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 59f541ee-3d8c-34fd-9943-3769cdc08382 | -23.5242 | -47.8109 | 2025-08-01 00:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| 31ee6891-bf3b-39fd-bed4-8458b9883a24 | -6.7293 | -59.1916 | 2025-08-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| b5d683aa-531c-3752-9605-36f8f0b14566 | -9.3989 | -45.4928 | 2025-08-01 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 61544479-b071-3473-ad3d-c7292addbf8f | -23.5022 | -47.8407 | 2025-08-01 00:00:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 31a4b4e2-93c4-3186-a840-c45fe52dd55d | -6.748 | -59.1523 | 2025-08-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b80b0f19-e6d7-3284-b597-9098d9f77dc3 | -9.4178 | -45.4906 | 2025-08-01 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| c402ad6b-46df-321d-9239-48a1839c5314 | -6.5258 | -56.2121 | 2025-08-01 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| e8bd2524-4fe1-3118-81d0-34c0e7a8e46f | -20.8549 | -49.0745 | 2025-08-01 00:00:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.3 |
| 38f67578-7f56-32e3-aff3-b404a91023c5 | -6.5445 | -56.1915 | 2025-08-01 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 115.1 |
| e1316da0-9681-3c05-bf90-b105437f1fd0 | -11.7666 | -44.9986 | 2025-08-01 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c7b69980-06f0-32ed-b2c7-11e646a5a3d7 | -18.6708 | -52.5756 | 2025-08-01 00:00:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 21a6b21e-782e-3c96-bc49-6e942192418e | -9.629 | -63.422 | 2025-08-01 00:00:00 | GOES-19 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5018871a-7173-3290-925f-ccfbb10ff539 | -18.6904 | -52.594 | 2025-08-01 00:00:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 366e4885-80d1-310d-a142-4136638d960f | -23.5446 | -47.8293 | 2025-08-01 00:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.8 |
| b44ac7cd-36b8-3999-a8a8-4fa0ec90cc9e | -23.5234 | -47.835 | 2025-08-01 00:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.3 |
| b1cc5a83-fa22-3543-bba6-a806f854daad | -8.0321 | -43.1257 | 2025-08-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| d5f2f5b4-ad66-37c8-b590-8cda3794895a | -6.7294 | -59.1723 | 2025-08-01 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| c0849f77-4a41-3580-814c-529299c6772b | -8.0324 | -43.1022 | 2025-08-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| eaed1ee5-5067-3a00-a9bc-ae9507024419 | -8.0513 | -43.1001 | 2025-08-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.6 |
| f39311e2-2575-3e49-946c-431162ab4af1 | -6.5629 | -56.1906 | 2025-08-01 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d6a7a8b4-fc31-3e4f-82e1-044e684100cb | -23.5022 | -47.8407 | 2025-08-01 00:10:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| f97b42e9-8755-37a3-9a1f-73d593e169e7 | -11.7666 | -44.9986 | 2025-08-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 088a7da6-8494-39af-9bb2-0d84fed17227 | -9.3989 | -45.4928 | 2025-08-01 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 98298f72-ee89-356c-a589-58058d5c00c0 | -23.5029 | -47.8166 | 2025-08-01 00:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| d6015574-8a3f-37b3-8a01-5e5145632e58 | -23.5242 | -47.8109 | 2025-08-01 00:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.8 |
| b780b6bf-87e5-3463-a519-2ba4e00b844e | -23.5446 | -47.8293 | 2025-08-01 00:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 065b2c76-2edc-3b1f-815f-3b86bd937292 | -9.629 | -63.422 | 2025-08-01 00:10:00 | GOES-19 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 8eff16d5-2fa2-3433-86dd-400646ed1e73 | -23.5234 | -47.835 | 2025-08-01 00:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 262.5 |
| 3115252f-aa7f-36a9-9601-2d27d6e92995 | -8.051 | -43.1237 | 2025-08-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 1787df0d-be99-306c-92c6-f7ec326c3489 | -18.6708 | -52.5756 | 2025-08-01 00:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 160.7 |
| a33677a1-7e10-3876-b3ab-682bb989d568 | -6.5074 | -56.213 | 2025-08-01 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 911a86bc-69d0-3c94-b33b-05db62f949f3 | -8.0321 | -43.1257 | 2025-08-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 951eac04-3c2f-3bb5-9792-bdc400bcd116 | -18.6904 | -52.594 | 2025-08-01 00:10:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 153.6 |
| a0f8afd2-f91e-30e2-8748-595708fb47e9 | -8.0513 | -43.1001 | 2025-08-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.1 |
| 5bc41b64-8501-360b-8e84-f9ca270d8a56 | -6.5258 | -56.2121 | 2025-08-01 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3dff7aa8-c1d3-3328-9877-57c5bdabbd0b | -18.6908 | -52.5722 | 2025-08-01 00:10:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 0263aa05-aa92-3bee-87d9-cbb7ee8668bd | -18.6704 | -52.5973 | 2025-08-01 00:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 8772b9a2-a9be-3ada-8f13-6a7a8d5380a2 | -8.0324 | -43.1022 | 2025-08-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 0e3c5255-5b08-3f5e-b5dc-bdd73385331f | -6.5445 | -56.1915 | 2025-08-01 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8f10a009-d6e5-31b5-b68f-9ea4f493f513 | -7.748 | -45.073101 | 2025-08-01 00:11:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0dbdb0c-c5bc-35ab-9b5f-024a3fabf3e3 | -9.8578 | -44.699402 | 2025-08-01 00:11:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2e3a5e14-05e0-38a6-a0ac-b58d113407bc | -10.7173 | -50.453701 | 2025-08-01 00:11:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce0cf526-8dde-367e-bbe6-1b62d9d3fde4 | -10.4338 | -47.262299 | 2025-08-01 00:11:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eda33afb-daaa-3b76-a013-3ba4f506c30f | -3.6935 | -43.427101 | 2025-08-01 00:11:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae8561ce-e99a-34d6-9eba-5c934260f77a | -8.3139 | -50.553902 | 2025-08-01 00:11:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8fd8cf2-c31e-3ef9-8f29-99a56e3e5181 | -10.4403 | -47.244598 | 2025-08-01 00:11:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4049cea-5d80-37f5-858c-088cd263c6a8 | -10.7975 | -47.254299 | 2025-08-01 00:11:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a51f050-250a-3974-a74f-516cc6e7eb07 | -11.769 | -44.998001 | 2025-08-01 00:11:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5317fcd-fae7-3ea0-aae7-40102b5a2e20 | -23.5096 | -47.798401 | 2025-08-01 00:11:00 | METOP-C | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7fbdc134-fc4b-3e07-bdc8-860da7d8f324 | -3.824 | -41.556499 | 2025-08-01 00:11:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20b13ea7-ecac-3276-940e-e6705c06af98 | -7.8687 | -45.535599 | 2025-08-01 00:11:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7765a42d-3b62-3280-9633-8e4adf9da7e4 | -14.2004 | -42.838001 | 2025-08-01 00:11:00 | METOP-C | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f122a014-e974-3330-b56d-cf4f4f730d31 | -8.0379 | -43.118698 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad231235-dc31-314c-b5f6-a25cce9736ae | -3.8189 | -41.579102 | 2025-08-01 00:11:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6174715a-c44d-36ea-8c02-fc5b691a6389 | -23.504 | -47.827099 | 2025-08-01 00:11:00 | METOP-C | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e697cb0-22ec-3095-9261-4b778a9b356f | -9.391 | -45.483799 | 2025-08-01 00:11:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ecdf769-4ea1-366c-8d0e-26176ea7cfdf | -3.5071 | -43.2411 | 2025-08-01 00:11:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46f9fc6f-462a-3f6e-a2f9-fe53afc81fd4 | -11.7739 | -45.021301 | 2025-08-01 00:11:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c072750c-aa39-3729-adad-06db899ab0eb | -8.513 | -43.317001 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 066b8c0d-ba99-3fa9-88a0-e418df03d808 | -8.0557 | -43.1063 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 57876ed9-5994-3d45-9888-c1e6ef00e766 | -3.5054 | -43.2337 | 2025-08-01 00:11:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1a1caa5-0ac8-3b41-b1b6-5501360c80e8 | -23.5233 | -47.823898 | 2025-08-01 00:11:00 | METOP-C | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d32cfe1-946e-3cbe-bb69-ef2db164a385 | -8.0459 | -43.108398 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7f3edbf-4dfd-3cf9-89a8-20d99ad91658 | -11.7714 | -45.009701 | 2025-08-01 00:11:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d7e4add-131a-3070-ad83-e32f91252e30 | -3.8224 | -41.549599 | 2025-08-01 00:11:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5648178-9563-3cdd-9574-5088b8ea3305 | -23.513599 | -47.8255 | 2025-08-01 00:11:00 | METOP-C | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3417e1b9-d517-3910-90a0-cbb73ff82277 | -11.7666 | -44.986401 | 2025-08-01 00:11:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad1f1db4-7b7e-3264-86ee-f781cd668442 | -10.7878 | -47.256302 | 2025-08-01 00:11:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d25c7335-d5b1-3386-9862-76217979a1e8 | -8.3235 | -50.551998 | 2025-08-01 00:11:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a02a627-0bd0-3033-9aed-ccf3cf2cd1df | -3.8256 | -41.563301 | 2025-08-01 00:11:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf1a7047-e80e-3b39-ac79-efb723060bfb | -8.0539 | -43.098202 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8aa9375-a1fc-36ac-9f8e-ea4fb5bcc628 | -11.7617 | -45.0117 | 2025-08-01 00:11:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45aab1d2-3d6e-3920-8fc2-19a579d8a4f1 | -7.589 | -44.813301 | 2025-08-01 00:11:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ce437681-7a5b-3e7f-8843-469816ffa287 | -9.4032 | -45.493301 | 2025-08-01 00:11:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4b81358e-4e31-38f1-adfd-4fe63fde9d4b | -9.3934 | -45.4953 | 2025-08-01 00:11:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea5f900-7edf-3750-b44c-5581b47578ed | -9.4007 | -45.4818 | 2025-08-01 00:11:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c2ec1f3-f8fc-35ae-b3ea-26d3c394032d | -3.8173 | -41.5723 | 2025-08-01 00:11:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db772ec5-41df-30fb-b703-bfddf89f15cd | -10.4306 | -47.246601 | 2025-08-01 00:11:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39457afa-d587-3776-91ea-bdd8381a5676 | -3.6928 | -42.200802 | 2025-08-01 00:11:00 | METOP-C | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70851852-ae94-3e65-95de-59bef05c0af8 | -23.5 | -47.799999 | 2025-08-01 00:11:00 | METOP-C | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb0bed66-e430-3f7e-8324-ab8c6022ef0f | -7.8711 | -45.5466 | 2025-08-01 00:11:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec16c46c-886c-30e5-853f-73215fe8f3ae | -8.0441 | -43.1003 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f7af0124-13b4-37f1-8e4a-b17b2b3c07f9 | -6.9917 | -41.934799 | 2025-08-01 00:11:00 | METOP-C | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6cc1bf70-b285-376c-8044-452b00267a62 | -7.2459 | -43.394001 | 2025-08-01 00:11:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5421c3d7-4bb0-3df7-b847-04a2eb53a67c | -8.3189 | -50.578602 | 2025-08-01 00:11:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af5abca2-a539-3790-ad27-7d86b2e5437d | -8.0477 | -43.116501 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b44dbda-a20d-368c-8e04-0639d9f5bd73 | -8.5093 | -43.300301 | 2025-08-01 00:11:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc2f98cb-1781-381a-9f71-991405009716 | -10.4435 | -47.2603 | 2025-08-01 00:11:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
