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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04488d88-b2ce-3cf1-8915-4bb425d667b0 | -8.4517 | -45.7318 | 2026-09-19 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 566b0935-e872-3b12-b828-34fc2446dda1 | -13.2222 | -51.7382 | 2026-09-19 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6ba07289-b20d-3f3e-889a-701c004ea9dd | -3.1514 | -58.644 | 2026-09-19 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3c673bd5-93b0-3393-9e74-6d73aab4fee5 | -7.7656 | -44.8688 | 2026-09-19 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 0e10bc13-24fd-39cd-810d-5706628c3e21 | -5.9465 | -44.7974 | 2026-09-19 15:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 9664a8c1-f266-311d-b83b-d11f3e8f4306 | -7.0029 | -49.7551 | 2026-09-19 15:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| d53d7247-2811-3573-ae80-fb396dd7e3cd | -6.2582 | -41.6858 | 2026-09-19 15:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 180.3 |
| 81f4fa08-47e6-3b4f-be61-683aacb96325 | -2.0765 | -56.585 | 2026-09-19 15:10:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 183179dc-c2b3-3210-9a3a-77c336ce9d92 | -14.931 | -49.9322 | 2026-09-19 15:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| cf5cba69-6732-3c18-9fae-89e0a25476e4 | -6.2585 | -41.6617 | 2026-09-19 15:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 170.3 |
| 9c9959a6-3497-31d3-9458-09e6fb92b5bb | -9.2417 | -45.9185 | 2026-09-19 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 71adccec-6a2a-3f67-a858-1468d7c46af0 | -12.2879 | -49.1883 | 2026-09-19 15:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 302.2 |
| 7e340900-b5d0-3952-b37c-a7a5b89d0189 | -5.6408 | -43.392 | 2026-09-19 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 280.4 |
| e0c3335f-c5e8-3503-ade0-298f37707150 | -11.7823 | -49.8152 | 2026-09-19 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 7a8e11c8-28fe-3674-8d15-798a502acbc8 | -12.2692 | -49.1689 | 2026-09-19 15:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 6c08a481-bac2-3897-b527-6babbac785cd | -10.932 | -50.8742 | 2026-09-19 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 3c64e751-36ae-30ee-a90b-c2e1e2d8fe17 | -9.0358 | -48.727 | 2026-09-19 15:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 138.0 |
| d117db7b-884a-36fd-b7a2-9c7fcc46a974 | -9.6202 | -45.8981 | 2026-09-19 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 387.3 |
| d981aca6-f422-3fd6-97f5-6e3c74446f00 | -13.2414 | -51.7359 | 2026-09-19 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 48bb268d-b701-3d25-96b9-80793ad9844d | -5.65 | -43.4 | 2026-09-19 15:15:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1f1843e-13c6-34a0-8344-1f885dd6eaa1 | -12.13 | -46.99 | 2026-09-19 15:15:00 | MSG-03 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcd6a9a3-5be9-3688-903e-d8aafb1d633b | -6.26 | -47.62 | 2026-09-19 15:15:00 | MSG-03 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 727266ef-6066-3e39-a950-5d6e4465690d | -12.29 | -49.2 | 2026-09-19 15:15:00 | MSG-03 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 024b1db3-4b9c-3284-9dcd-accc7af2a5de | -11.13 | -53.98 | 2026-09-19 15:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b0f12a8-b58c-3dfc-87d4-4f9bc163635e | -5.62 | -43.39 | 2026-09-19 15:15:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 240e7e5b-7897-3c81-93be-f143a6381021 | -11.22 | -48.35 | 2026-09-19 15:15:00 | MSG-03 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61f95e37-605d-3d31-87c2-7cb4c7d07032 | -11.14 | -54.04 | 2026-09-19 15:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ade774dd-aa1c-3176-8c9a-97f251d9868e | -8.5986 | -44.5762 | 2026-09-19 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 187.1 |
| b9651741-8f95-3b08-b88a-e9ca1215bab8 | -11.8746 | -47.6125 | 2026-09-19 15:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 213c8e28-4235-3da1-bca7-964d953c4fac | -8.6173 | -54.5924 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 199.3 |
| e00fa872-9602-3596-ab59-7387ea6435a2 | -11.1035 | -49.4623 | 2026-09-19 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 0030d110-dfb7-348f-8be1-abc63aad152c | -10.932 | -50.8742 | 2026-09-19 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 8a62b924-c9ee-3c3e-b3ed-926bd74d5b1c | -11.0608 | -49.7909 | 2026-09-19 15:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 3b5f7cf3-94ac-346c-b772-cf42e37dc94f | -7.8748 | -45.1774 | 2026-09-19 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 51090973-9324-3dd4-a413-5cb7dafcc3fa | -8.5986 | -54.5937 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| aa2bd8c4-05e9-3c8b-938b-8d9103370081 | -10.8367 | -50.9266 | 2026-09-19 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7f8cf2e7-c552-38d6-b39a-4f5e620ec4ac | -9.247 | -57.1488 | 2026-09-19 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 547e06a0-0ddd-3c1f-b150-f80a3c9e9346 | -11.3171 | -43.3585 | 2026-09-19 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 161a88e5-f4d6-343a-8211-35e17078d868 | -10.7133 | -50.258 | 2026-09-19 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 4c75a411-cb1c-30bb-85db-3afd18645385 | -10.6703 | -50.6465 | 2026-09-19 15:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a97f0666-6aa8-320b-adb0-4e6b38093d6b | -9.2567 | -46.2098 | 2026-09-19 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 402f488e-8046-3b62-ab42-a2c8712af935 | -7.7847 | -44.8441 | 2026-09-19 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| ad65bc35-97b0-3046-9374-720c74707798 | -3.1514 | -58.644 | 2026-09-19 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9d1a4bd4-71f9-3928-aca0-29bd8a45195a | -7.7631 | -46.7167 | 2026-09-19 15:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| a817e7ed-4e55-3fc3-8931-0adeed7b9b78 | -11.4351 | -51.4774 | 2026-09-19 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 66645cf0-16fb-393e-80ce-534fa9fa0b08 | -14.9505 | -49.9293 | 2026-09-19 15:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5a71967b-481d-36be-aa79-c2fe3a43432e | -3.7311 | -60.6018 | 2026-09-19 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| abdbb39d-050e-32e4-87b4-7f5d5dd7aeb4 | -10.8735 | -53.9668 | 2026-09-19 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a83ec526-2494-337e-af32-f9ef9d198f75 | -9.0358 | -48.727 | 2026-09-19 15:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 77002486-463f-3f38-9921-955c6aecf82d | -6.3286 | -55.2877 | 2026-09-19 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 98a6a1cf-1155-32c1-8a06-703962f75b9c | -11.3167 | -43.3822 | 2026-09-19 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 5495590a-ff80-3c4a-95f7-7b50e9a787be | -13.2414 | -51.7359 | 2026-09-19 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 062587d9-5dec-3195-b170-162aa8aedab0 | -9.1523 | -49.9853 | 2026-09-19 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 859cc92e-fd4d-33bc-b25b-c8667be3ff9b | -2.6783 | -57.5893 | 2026-09-19 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| aa9810d3-7ee7-3c08-acf9-cb43c7cedbc6 | -9.0096 | -44.9209 | 2026-09-19 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| b088b906-9818-317d-aa8f-def322c3f2ef | -10.7927 | -46.1618 | 2026-09-19 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| e941466a-5c33-30de-bc2c-a488b77bc384 | -5.5661 | -45.5491 | 2026-09-19 15:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4ad79089-6a6e-318e-b831-459bd713c3e9 | -11.299 | -51.7238 | 2026-09-19 15:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 563fb25d-ae98-3124-9b72-df490ab15646 | -13.884 | -47.9929 | 2026-09-19 15:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 4fe356ae-0b5e-34d3-b9d1-ed4901840a0b | -9.2472 | -57.129 | 2026-09-19 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4c70e672-cdea-3e77-8ede-f78827ab0153 | -3.3637 | -61.3282 | 2026-09-19 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 7cf98f92-235d-309d-be2c-b361a0b70c14 | -14.931 | -49.9322 | 2026-09-19 15:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 898ce62b-faa1-3e25-a4da-48de9edd9cd9 | -7.0029 | -49.7551 | 2026-09-19 15:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 03f79760-e55b-3e43-a1d5-286209997c00 | -11.3604 | -44.1521 | 2026-09-19 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 1a0784e9-2f6d-3a8d-8aab-250d18e7e187 | -11.4354 | -51.4563 | 2026-09-19 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| c15be2cc-7d42-353e-bf1f-fa9ff6c37d60 | -9.6202 | -45.8981 | 2026-09-19 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 185.5 |
| c4c5840d-8de3-36e1-93ed-851594597979 | -3.4461 | -58.0005 | 2026-09-19 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 1e8e0d3c-072c-3465-8cf6-e0e6362a8d45 | -13.2222 | -51.7382 | 2026-09-19 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 26d9e947-d448-3987-933c-2047a38d2182 | -12.2879 | -49.1883 | 2026-09-19 15:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 5e96d403-3e34-374c-80c1-b35d53f63fe6 | -9.3575 | -50.1156 | 2026-09-19 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 91e81c04-d3b8-3d86-8361-5862b7241373 | -12.2883 | -49.1664 | 2026-09-19 15:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| df00f364-d3e7-330c-9ca8-4529169783b7 | -7.6574 | -46.1013 | 2026-09-19 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 366c0117-0bd9-3da6-9a27-ce45842a64e0 | -7.7656 | -44.8688 | 2026-09-19 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| b86e4b03-92f2-3f86-80d1-bda03a5db3b6 | -7.8843 | -47.6333 | 2026-09-19 15:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| ae5e1f37-df41-3159-a243-e574da4487ab | -6.6703 | -43.6337 | 2026-09-19 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 8ac54a46-da43-344c-ad7c-1cda55420d15 | -3.331 | -59.8292 | 2026-09-19 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 8265d712-b14b-3cbc-8d25-0a839f6aa067 | -6.2236 | -45.1853 | 2026-09-19 15:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| bc73c325-956f-3ef6-a2ed-f22bbb74392b | -8.1496 | -54.8049 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| df6088a4-3dab-3cbd-9b96-5e64385be777 | -9.7304 | -46.1337 | 2026-09-19 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| ec14a907-dc9e-3345-adf0-0cae7f3d0a4d | -8.5984 | -54.6139 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0210d2ae-f54d-35dc-be44-3d2860007af2 | -7.7844 | -44.8669 | 2026-09-19 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 2cb8fe90-85ba-32b1-92c6-7f747c2cd22e | -8.4797 | -57.6282 | 2026-09-19 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 70833230-7e31-39fa-9944-446a4628a40f | -7.5888 | -57.6953 | 2026-09-19 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 09e9b3cd-6d9b-326f-9538-a7ff2be0dce0 | -8.411 | -54.7274 | 2026-09-19 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 68e0f052-0dc2-35cb-bbba-f7a8fe900995 | -13.2606 | -51.7335 | 2026-09-19 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 36097bcb-4ade-3145-8e80-3de98a56b40c | -8.7731 | -48.6868 | 2026-09-19 15:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 174.8 |
| f610a528-9d3c-3bc3-8efe-92ea089e281e | -10.7991 | -50.9093 | 2026-09-19 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6dc94a9c-b288-31fe-9fa1-1480a0b16922 | -2.8791 | -57.799 | 2026-09-19 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 492733a7-b43e-38ac-9a84-fed8c4583a09 | -3.7311 | -60.6208 | 2026-09-19 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a1da6828-65bd-34fc-9f28-a373856592c2 | -3.2955 | -59.4284 | 2026-09-19 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| fe980fad-be2b-37bd-9967-202252eb6042 | -10.7994 | -50.8881 | 2026-09-19 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 7557100f-ecb1-3022-9879-ebcf71e14b8f | -2.9157 | -57.7983 | 2026-09-19 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 418.9 |
| 7bb12369-6675-30b6-99ac-3a9000a4dae5 | -9.2603 | -45.939 | 2026-09-19 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 09ebb2ff-1b93-3465-bcec-df6f3bcaa0d9 | -12.1531 | -46.9707 | 2026-09-19 15:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 49c170e1-f8b7-3b77-a68c-3375ca59bd7b | -6.2585 | -41.6617 | 2026-09-19 15:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 165.3 |
| 502f3397-1bfa-37b8-bbcc-e12ca2a954f0 | -9.0355 | -48.7487 | 2026-09-19 15:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 123.4 |
| e1361952-3d5c-3bca-8c7c-6470d7bbfb8a | -3.3638 | -61.3093 | 2026-09-19 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| f59fcb96-e407-379a-b1fb-00c4b253092d | -5.5663 | -45.5265 | 2026-09-19 15:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f82fd8a0-48f6-36ca-81f8-13ab711984ca | -8.45 | -45.8674 | 2026-09-19 15:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 23f271ac-9e59-3782-9609-5c4464e6ef71 | -3.6077 | -59.0577 | 2026-09-19 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |


[Clique aqui para ver as próximas entradas](README122.md)
