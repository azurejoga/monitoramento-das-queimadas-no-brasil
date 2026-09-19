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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c6c733a-5aba-3d90-ac0f-47e84ea17a95 | -10.567 | -51.3137 | 2026-09-19 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 89bb1346-bca9-309c-8c7a-62fde023b466 | -3.3637 | -61.3282 | 2026-09-19 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 409e254c-c9dd-35e0-a1b9-c0fce337ef0c | -8.8639 | -45.937 | 2026-09-19 15:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 059dc163-3e41-3ae9-ba9c-932d2e5c75c0 | -6.1838 | -47.5258 | 2026-09-19 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 939ccbc8-b3a3-3411-98f6-06507223f012 | -12.1969 | -50.1102 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 0350cd66-ea4e-3b11-bf58-332db804e7e3 | -11.318 | -51.7218 | 2026-09-19 15:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 39ab7c12-5cf7-3d96-91c6-c2a5f3152274 | -9.3611 | -48.3032 | 2026-09-19 15:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 9c615c42-e28e-3343-a176-9ec8e1895959 | -11.3625 | -44.0347 | 2026-09-19 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 0703773d-8b9b-316e-8bb4-0d8d1e7df27a | -8.4797 | -57.6282 | 2026-09-19 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 9110358e-94a4-3827-abff-99ffbcdd8294 | -11.3604 | -44.1521 | 2026-09-19 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| fff58d6c-258c-3bf5-b4f2-44e2c79ee2e1 | -6.1649 | -47.549 | 2026-09-19 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 900bdb84-1dfe-3d25-840b-dc01066dfef4 | -12.3206 | -50.7394 | 2026-09-19 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 38c16797-17fc-3b81-ac1a-c3cfe75eb6e3 | -9.0355 | -48.7487 | 2026-09-19 15:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 134.7 |
| a0267bd0-0388-3b56-a670-862e3ebaf0c2 | -11.0614 | -49.7477 | 2026-09-19 15:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 230.9 |
| eb8c2009-8641-3c81-9cd7-e95451b4eb79 | -10.9133 | -50.8549 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 1efee8c1-ab48-3533-9693-736e7e962faa | -11.8533 | -50.1515 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 60a7da68-2392-34a9-a883-7bae5fe8df78 | -7.7844 | -44.8669 | 2026-09-19 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| ecfbb448-68ef-3fd0-a2e3-edbeb54121b9 | -3.3638 | -61.3093 | 2026-09-19 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 223717d4-a9bc-306b-9021-90613aa30d4a | -3.6077 | -59.0577 | 2026-09-19 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| eaeeec92-2a2a-3b84-b42e-e88f8e860a4b | -3.8096 | -58.8994 | 2026-09-19 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 9dcf0b09-0d40-3226-b9c8-954add6d0719 | -11.8746 | -47.6125 | 2026-09-19 15:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 08475be6-083a-3aaa-acb1-240f2d4203b1 | -11.731 | -50.7014 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| fe4f9d3c-1ac8-3db7-81ff-86368824fa70 | -10.837 | -50.9054 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 688a282b-7ea8-343f-8bb8-6e7e070ebbb5 | -5.6596 | -43.3906 | 2026-09-19 15:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 189.8 |
| c44aa664-7592-3469-ad08-e66890f1233d | -10.7133 | -50.258 | 2026-09-19 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 96505c64-c8e2-3115-870a-9789629b7022 | -11.8549 | -50.0437 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7040ab49-da11-3f8c-abcd-960fbb92afb9 | -11.8546 | -50.0653 | 2026-09-19 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| cd721b31-ae52-3d9b-84aa-039eb3ffee43 | -3.1514 | -58.644 | 2026-09-19 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 25203e96-d1ed-3c90-8aa8-08757764bd6e | -7.7118 | -44.6451 | 2026-09-19 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 472.7 |
| 01abaf30-009f-362f-8bfa-fd27bad1dddf | -10.8941 | -50.8782 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 40364b15-4ca8-39f6-8c7f-90c71b668657 | -10.1179 | -45.5662 | 2026-09-19 15:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 166.7 |
| a0119ec3-f954-3339-903d-edc434a96603 | -2.8791 | -57.799 | 2026-09-19 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 403e8eee-0e17-3997-808b-0c79557a7af4 | -10.5667 | -51.3349 | 2026-09-19 15:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| dafe601d-d120-3cf6-b799-7da7e6006053 | -10.7991 | -50.9093 | 2026-09-19 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7b299e12-05dc-3ca2-88ea-902dd94ee138 | -6.7687 | -55.8435 | 2026-09-19 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6f7832a5-59f9-3f03-80c4-9a9461e48086 | -10.4733 | -51.2597 | 2026-09-19 15:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 5b3bbfd1-f3b7-3df6-b992-2d9ce238e533 | -6.1839 | -47.5039 | 2026-09-19 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 18545eaa-3ae4-3eee-afbd-7b8d1782d5ba | -9.0358 | -48.727 | 2026-09-19 15:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 543b9696-66c0-3159-9454-51a9a563e4e7 | -8.1681 | -54.8239 | 2026-09-19 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7403affd-7ebe-3b99-91b1-ec18d430d108 | -10.6039 | -46.0728 | 2026-09-19 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| e0f9dc2c-41cb-35f6-809b-8615530e70ba | -7.6572 | -46.1237 | 2026-09-19 15:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 546.7 |
| f2f08941-b7ab-3f35-a37c-befcfcd33abc | -8.4112 | -54.7073 | 2026-09-19 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b8f194d9-d877-38c0-a35f-994ecb55b1dc | -7.8598 | -44.8595 | 2026-09-19 15:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 2bedf005-1960-3087-a274-098dbb2dfbae | -11.9303 | -50.0993 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 88e9e7d6-1fcc-3a7c-8366-f14329255f38 | -2.8791 | -57.799 | 2026-09-19 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 3e63e06b-9780-3143-a4d1-d6538a12d86c | -11.7122 | -50.6822 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5f103d68-b9e4-390d-8f54-f33b521e1b0a | -3.4461 | -58.0005 | 2026-09-19 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 590a9573-3dcb-303b-8b85-ed90457ff789 | -10.5667 | -51.3349 | 2026-09-19 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 19f911a2-16d6-311f-94ee-5dbc1f4116f0 | -11.9306 | -50.0778 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a58545a7-820a-3458-be1f-3904d628b590 | -11.9112 | -50.1016 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 40755402-9d2e-39ee-acd5-8e140046f95e | -3.331 | -59.8292 | 2026-09-19 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| ab0515c3-1298-3625-a74e-b933e312201d | -12.5039 | -50.0075 | 2026-09-19 15:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d822bc7a-5692-3470-b60e-096a07747e2b | -3.6077 | -59.0577 | 2026-09-19 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 315fc1fe-ff83-3988-9713-e7238e069a23 | 1.2611 | -50.7679 | 2026-09-19 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 053549a0-cb23-3e58-b862-c406800f8157 | -11.318 | -51.7218 | 2026-09-19 15:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 267.8 |
| 711de6c8-2cf2-3a70-be41-0b5b73e9080f | -12.4841 | -50.0532 | 2026-09-19 15:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 96db357d-ce20-35df-91f2-6f1dff582251 | 1.2424 | -50.9346 | 2026-09-19 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 289d21d0-e33a-3d51-a3e2-0e9f3cd8a3d2 | -8.4108 | -54.7476 | 2026-09-19 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7f63749f-fd0a-3eb0-9ae8-e3c00f39e8a7 | -10.7994 | -50.8881 | 2026-09-19 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f8a1227e-665d-328a-8b22-cfa8ff0d2a1f | -7.7118 | -44.6451 | 2026-09-19 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 469.0 |
| a9ae02bc-d754-3c7e-b8a2-06adf4878246 | -9.3611 | -48.3032 | 2026-09-19 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| a0b623a2-b2d9-3ab3-9f36-eec5e65212a9 | -11.7313 | -50.68 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 295.2 |
| dae95b2c-4ace-31ce-8d8f-591833e2751b | -10.932 | -50.8742 | 2026-09-19 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 2a2b90e9-f22c-3fc2-a35e-7b3dd5559227 | -11.9895 | -49.9629 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 6f371257-51f4-391c-8978-1954d3a31a7e | -2.9525 | -57.72 | 2026-09-19 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 8635bc68-9ae0-32a8-a42f-38b331dc32a4 | -10.7715 | -46.3001 | 2026-09-19 15:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 8fc6c264-61ea-3c4c-8033-06666448cfa8 | -12.2688 | -49.1907 | 2026-09-19 15:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 911f7fd6-1f06-3f28-aaf7-1888df3d2d3e | -5.6596 | -43.3906 | 2026-09-19 15:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 0e8326bd-08f9-32b8-805e-b341700975bb | -2.8974 | -57.7987 | 2026-09-19 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 293.9 |
| 6ff5927d-f17c-3fab-93db-b02fbc63336d | -11.8549 | -50.0437 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 4ab0a354-08b4-3e5d-857b-9e9d0fca2ec5 | -9.0355 | -48.7487 | 2026-09-19 15:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 139.7 |
| b235d5d2-d27a-3d02-806f-66a6c4301303 | -11.874 | -50.0415 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| fb2eaad7-8dbc-37a4-a3d7-2212bd1a6065 | -12.2156 | -50.1295 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 107a3645-88ac-35d0-8deb-d09d654e34f7 | -11.4354 | -51.4563 | 2026-09-19 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 41f32320-2027-3fd2-902a-ca4e3a926d7a | -12.5036 | -50.0291 | 2026-09-19 15:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 576de5e5-1610-3098-bf9e-47a706e68889 | -12.216 | -50.1079 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 36409da4-27bc-3c8b-8e09-eea26304ff09 | -6.6217 | -55.6917 | 2026-09-19 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 1cc61324-e911-396e-9c9a-15fe1b20c06f | -10.7991 | -50.9093 | 2026-09-19 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 39262a71-dedb-3695-a562-3debc5eedecd | -10.9133 | -50.8549 | 2026-09-19 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 118d7409-5f64-3e45-bd4d-1c93d9f5479b | -10.7133 | -50.258 | 2026-09-19 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 84608166-ad12-332d-8ab8-92d2f1c20ad3 | -7.8598 | -44.8595 | 2026-09-19 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 8c85363f-7b9e-3049-b6bb-22bdd7248c7b | -10.8367 | -50.9266 | 2026-09-19 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 49620cf6-8752-34d5-9572-8757ae4a4e3f | -7.7844 | -44.8669 | 2026-09-19 15:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 9df18f06-66ff-3dfd-905a-1e53e94d776c | -12.2883 | -49.1664 | 2026-09-19 15:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| f08e7651-1588-3a79-80be-fd76f9d922ba | -7.6572 | -46.1237 | 2026-09-19 15:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 610.5 |
| 52ec24e1-218a-33e6-82d0-56587fa7976a | -2.8975 | -57.7793 | 2026-09-19 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| ba26a811-df28-33fe-8c44-b14af9e7dee3 | -10.567 | -51.3137 | 2026-09-19 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 06b85e6a-78f8-3db7-9588-41955e46d76a | -3.1514 | -58.644 | 2026-09-19 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 74a1dead-dff4-35b2-8b70-b56669062858 | -10.8279 | -50.1815 | 2026-09-19 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 178.1 |
| d5f9581a-09e1-3c6a-a229-53649d912108 | -12.027 | -50.0015 | 2026-09-19 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 8398b72f-cfb3-30bd-8b0c-169925e0ddab | -10.7546 | -46.1667 | 2026-09-19 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 17f9bcf6-478c-3da2-a0a9-76052bd099c9 | -10.809 | -50.1836 | 2026-09-19 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| cb095f8f-a6d6-366b-a318-30f331183c7a | -3.3638 | -61.3093 | 2026-09-19 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 5e7ca94b-7f2b-39fc-9d22-4956e708122b | -3.4462 | -57.9812 | 2026-09-19 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 21e9e0c3-b51d-355a-9838-498720d92905 | -9.0358 | -48.727 | 2026-09-19 15:50:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 139.9 |
| c116707f-2ef2-3e17-bd57-af5a99376947 | -11.299 | -51.7238 | 2026-09-19 15:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 163.0 |
| b0145b89-d3ad-3ed2-8242-c8b800086f93 | -10.5481 | -51.3156 | 2026-09-19 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e55bef69-3313-3617-b149-8bf14ca57e5b | -11.3433 | -44.0376 | 2026-09-19 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 41ed091c-795a-3579-838e-cb018340e1e0 | -10.8282 | -50.1601 | 2026-09-19 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 3d529609-d98e-320f-ab76-933ce00de9c2 | -7.5642 | -49.6071 | 2026-09-19 15:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |


[Clique aqui para ver as próximas entradas](README125.md)
