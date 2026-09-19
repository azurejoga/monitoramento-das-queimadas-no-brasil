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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6650f5fe-690c-3a4e-9b87-b49581a1b516 | -6.9224 | -55.0376 | 2026-09-19 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5fd6a9b6-0552-39dd-a585-535f2d573b1d | -5.6596 | -43.3906 | 2026-09-19 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| db390153-dea0-35ae-9852-0831cdf88e02 | -10.7994 | -50.8881 | 2026-09-19 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| aa10c264-96e5-3bf6-9040-9d1529bc61a7 | -11.874 | -50.0415 | 2026-09-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 89ef8dd5-8b11-3036-b37b-3458c0e58952 | -12.2879 | -49.1883 | 2026-09-19 14:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 0f8100b2-3db3-37dc-a1c1-be04f0f7a0f6 | -3.4243 | -59.1959 | 2026-09-19 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| bb2f80c7-a449-3f83-89fb-5d0041150742 | -12.1527 | -46.9933 | 2026-09-19 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b291d111-daf2-3004-a24c-65e58c077ac8 | -5.7431 | -57.5814 | 2026-09-19 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 07e63fa8-e4a6-3f1f-a18f-0c99a3d10c7a | -8.7492 | -50.7847 | 2026-09-19 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c62b6836-44a5-39c1-96d3-b2d1500c24bb | -11.1228 | -49.4384 | 2026-09-19 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 34db424d-c34f-30f7-b1ad-8be2a15f7b1d | -5.6408 | -43.392 | 2026-09-19 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| f90ad23d-7c91-38f4-853c-19c510742f96 | -11.8937 | -47.6099 | 2026-09-19 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 8aa7cb1c-4c36-331f-b641-7cc06b7b2e9f | -8.6628 | -45.4379 | 2026-09-19 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 6d5f59a3-270b-3e7c-bf47-c35337535954 | -11.5107 | -47.7045 | 2026-09-19 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 2b0530f5-0e69-385d-8a11-233d20362ba7 | -5.1351 | -45.7791 | 2026-09-19 14:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 1e6d4895-2cf5-3afd-a28b-2a0322489531 | -11.0611 | -49.7693 | 2026-09-19 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 3ca11ed4-5475-32ea-ace5-16677995f4e2 | -5.9344 | -42.0966 | 2026-09-19 14:10:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 156.4 |
| 523394ed-2faa-374a-9028-1f2bda49497b | -8.9412 | -44.3995 | 2026-09-19 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| d7c11dc4-5e26-3415-a685-e98a868849a0 | -8.4737 | -47.0053 | 2026-09-19 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 26800cbf-7ed1-30e2-9495-9e351f6e71bc | -3.6946 | -60.6025 | 2026-09-19 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 5a14c1dc-20e1-3061-b2b7-57c6129327c6 | -8.4797 | -57.6282 | 2026-09-19 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 00d94993-e9cd-3b96-b349-6b2905d296b9 | -7.0029 | -49.7551 | 2026-09-19 14:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 1842335e-a59c-3e8d-b2e1-53c397926186 | -2.8975 | -57.7793 | 2026-09-19 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d9d43dc9-ae3e-36fc-b304-25921f06375a | -13.8726 | -48.5949 | 2026-09-19 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| cfe8f59d-fec5-349f-bdc4-9558ba003583 | -11.8746 | -47.6125 | 2026-09-19 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 4244f837-c52d-3b3a-8360-fa4f716d0ec0 | -11.3604 | -44.1521 | 2026-09-19 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| b3113e57-4fc5-31ec-8470-cfb2f6f50ac1 | -10.6703 | -50.6465 | 2026-09-19 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 8eef907c-1729-3371-803d-48c7fd75a842 | -8.4314 | -45.8467 | 2026-09-19 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 256e56e8-862f-3478-912c-2741c58252fc | -6.2034 | -45.3453 | 2026-09-19 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 19006079-1777-3331-8eeb-06075f10e97b | -7.7118 | -44.6451 | 2026-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| d9e434c2-8eb2-3c3c-a4f8-c6f2f499c68e | -10.0956 | -48.4226 | 2026-09-19 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4ee0e736-77d1-38b5-a2a6-320c97dfaf14 | -7.8595 | -44.8824 | 2026-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 2a76cfaa-06ef-3b5e-9a38-e08aa59cda4a | -11.1369 | -54.0251 | 2026-09-19 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 424.2 |
| eb73cd39-5a03-324f-9c40-12df893a02c3 | -13.892 | -48.592 | 2026-09-19 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 89b39667-ff51-3659-b015-1a5c004ab086 | -11.8934 | -47.6322 | 2026-09-19 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3cddbd2b-3777-38f6-9b78-9a2df2d891f0 | -10.9133 | -50.8549 | 2026-09-19 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 0bb48efc-52d6-3253-9a0b-d09e955f1da7 | -12.5761 | -49.1071 | 2026-09-19 14:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 24cfb2ff-ec41-32a7-b551-8d1b5322f73f | -7.7629 | -46.7389 | 2026-09-19 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 366.7 |
| 23720f4d-a1d2-3114-828d-7399ca770bec | -7.0448 | -42.0906 | 2026-09-19 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 199.8 |
| 19484e7d-a86c-3ee1-82c2-646048478aba | -9.2567 | -46.2098 | 2026-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| ac8b1cb7-10be-3552-9d7b-00fc836fa8b7 | -6.2585 | -41.6617 | 2026-09-19 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 227.5 |
| af6acb68-2e0c-34b6-8176-6401618a1f94 | -11.0065 | -48.3187 | 2026-09-19 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 03daead0-3229-3124-8ad5-055cb26c6c0e | -8.411 | -54.7274 | 2026-09-19 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 07a15bcb-1d34-398d-ada1-abd0d4c36efd | -8.7919 | -48.6851 | 2026-09-19 14:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 384.3 |
| 40c613f6-8bb9-3fb5-b01f-d9f61603e26e | -10.911 | -53.984 | 2026-09-19 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 52d2cc4d-5650-37aa-8f54-e16ed7786307 | -3.7128 | -60.6211 | 2026-09-19 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 64121727-f6fd-39fd-b2dd-9951e65bf2fc | -6.0197 | -51.7686 | 2026-09-19 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 297f653b-cfcf-3038-a185-30c88a72d764 | -2.458 | -57.9033 | 2026-09-19 14:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 14f73e1f-302a-389f-aa72-caa8376321af | -4.5585 | -42.9758 | 2026-09-19 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| e7b843ee-869f-325a-ab67-c331314c8008 | -8.6173 | -54.5924 | 2026-09-19 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 05ae3e98-69b3-3b2a-b35f-e399a78b98c1 | -12.2692 | -49.1689 | 2026-09-19 14:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 91d5b66b-d192-395c-bcb9-d1cef0805efe | -11.4912 | -47.7292 | 2026-09-19 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 5139c5a5-d91f-3505-8c11-04320c57b165 | -3.9902 | -41.2759 | 2026-09-19 14:10:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 9ea41bba-a153-36b3-b8ec-4f2d7dc3f333 | -11.5103 | -47.7267 | 2026-09-19 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 65be08d9-8cec-3d94-be20-802e5a22555d | -11.234 | -48.3571 | 2026-09-19 14:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| d06b334e-89e5-3e53-ad40-6b4b5e2835e9 | -9.0167 | -48.7505 | 2026-09-19 14:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f8c68f2e-096b-3e96-ae03-ce7e3f726e10 | -10.7133 | -50.258 | 2026-09-19 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| e36e418d-4fa5-3425-8e7d-267c6f46a178 | -6.941 | -55.0366 | 2026-09-19 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a351dd9a-6a11-3d8d-8279-280f9838a64f | -3.4455 | -58.1941 | 2026-09-19 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| af9509e5-ae77-3e57-a3a2-6499f2b4c802 | -11.7823 | -49.8152 | 2026-09-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 302326da-49df-3e64-b204-d7ea315330e6 | -17.0449 | -47.2835 | 2026-09-19 14:10:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d7796dcf-a64c-357e-a359-0cec3c9112b5 | -12.6896 | -45.94 | 2026-09-19 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| b0101488-e9cb-3996-bbb1-ed342432eb0e | -6.001 | -51.7903 | 2026-09-19 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 36334cb7-e8d7-3c1c-ad36-5df4c73734ea | -8.4503 | -45.8448 | 2026-09-19 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| bfd34f11-159c-34ca-8204-96ea1c3baa0c | -7.026 | -42.0924 | 2026-09-19 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 159.6 |
| a1ac6b15-9a60-3eb1-8f1a-428f9648e781 | -11.8742 | -47.6348 | 2026-09-19 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 84491726-b3f7-3129-9643-6c0874a7d7b7 | -10.955 | -50.5738 | 2026-09-19 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| df29478e-e017-3e4d-9da6-9c3b8bd2eef4 | -12.1535 | -46.9482 | 2026-09-19 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| d438f54c-f7c5-3abf-ab22-01646513d996 | -9.7501 | -46.0863 | 2026-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 9d47e174-faa3-3d40-8022-2eddfa71f15b | -9.7504 | -46.0637 | 2026-09-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ae3b6977-89da-3aac-92a5-0fb42578d449 | -13.2414 | -51.7359 | 2026-09-19 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| b044fc8a-9d73-3dfc-a3c8-25933a3b6daf | -3.7129 | -60.6022 | 2026-09-19 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| dd57a36c-6ba3-3e6e-84b1-368513d0bb4a | -12.5952 | -49.1046 | 2026-09-19 14:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 083b255b-dc7a-3f32-954e-a9510cc23e55 | -3.3311 | -59.8101 | 2026-09-19 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 7542ff2d-9550-39c9-b162-50175b7adde3 | -6.2582 | -41.6858 | 2026-09-19 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 294.5 |
| e911d978-fbed-3800-ae40-b66d736c4af8 | -12.2883 | -49.1664 | 2026-09-19 14:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 3bff9790-a774-3c48-845f-16c803837ec7 | -7.7847 | -44.8441 | 2026-09-19 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| b258535b-bee4-353a-a211-c5150ce73d9a | -2.6966 | -57.6084 | 2026-09-19 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ede225e4-e843-3629-9f07-9ad40979debf | -11.0062 | -48.3407 | 2026-09-19 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2e9bc944-842a-3da4-b9ef-ce7c21e6426b | -7.7626 | -46.7612 | 2026-09-19 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 356.6 |
| cedaafeb-a1d2-3b85-bc57-d448664040e9 | -2.8791 | -57.799 | 2026-09-19 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| f4b10b83-a67b-3ae2-ae8a-7582585db916 | -11.155 | -42.7885 | 2026-09-19 14:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 132.2 |
| 73dd4979-8089-39e6-be3d-9cf38c8f07c2 | -12.7085 | -45.96 | 2026-09-19 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 511.5 |
| 44f00502-91f6-3719-a6f1-3299e11a6de7 | -9.247 | -57.1488 | 2026-09-19 14:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7466d4fd-a3f0-32d3-ae69-15604d714e69 | -2.9157 | -57.7983 | 2026-09-19 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 235.6 |
| ab1fe3c2-b7b2-3514-91f6-aca17dc5a9e6 | -6.8438 | -48.8033 | 2026-09-19 14:10:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 81.6 |
| bde35682-20e6-360d-b197-b26157bd961f | -11.0827 | -48.3095 | 2026-09-19 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5dfc64c6-532e-3658-8539-f307c38b230d | -8.7731 | -48.6868 | 2026-09-19 14:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 180.7 |
| b0012604-ada6-37b2-ae00-2e0adad4f9cd | -8.45 | -45.8674 | 2026-09-19 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 4851e56c-e6de-31fa-abea-5a3d4cdfaee6 | -8.4296 | -54.7262 | 2026-09-19 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 326ec96f-7f23-376d-9aeb-d2fd6e19c8c0 | -11.318 | -51.7218 | 2026-09-19 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 03c70e8e-db98-3464-b917-0c09f45dcf71 | -10.567 | -51.3137 | 2026-09-19 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| f5629994-9b9e-39c2-b011-bb0f235ca7ec | -2.8974 | -57.7987 | 2026-09-19 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 242.8 |
| 97cc7afa-095f-3be1-9527-42a9c58db00d | -3.4455 | -58.2134 | 2026-09-19 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| b6ab47e7-2e55-3a7e-92e0-e9a7c518ec62 | -5.1538 | -45.778 | 2026-09-19 14:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 0f77bb7f-dec2-3e93-9f14-746825c8a8e6 | -9.0355 | -48.7487 | 2026-09-19 14:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 246f1aa6-ae81-3dc5-aaad-b9ef50c8baa0 | -12.1339 | -46.9734 | 2026-09-19 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| fe8b4f38-4a6a-3339-9c35-011b15aa0066 | -9.2472 | -57.129 | 2026-09-19 14:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e0635d45-4ce8-309d-ad7e-a5bdd592c1e9 | -9.0358 | -48.727 | 2026-09-19 14:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 6b5efa40-bf10-3ce1-a0df-0799b96a2de6 | -12.1531 | -46.9707 | 2026-09-19 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |


[Clique aqui para ver as próximas entradas](README114.md)
