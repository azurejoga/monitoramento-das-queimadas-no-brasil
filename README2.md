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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c50779c4-0ff0-3c21-b08e-b88623e39fa4 | -11.382 | -54.064 | 2026-09-29 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 0d91950e-0578-399d-a306-8169a36c9914 | -11.3823 | -54.0434 | 2026-09-29 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 190.0 |
| 264cbf20-4d35-3df0-a35a-838d53b107af | -18.1251 | -42.6123 | 2026-09-29 00:10:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.0 |
| e62983f6-5d92-330b-8c9e-d49880b2c723 | -15.112 | -53.8838 | 2026-09-29 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| bb1a7819-1cc7-38a7-8b84-6e7100e826b9 | -15.1113 | -53.9257 | 2026-09-29 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| b5336e63-8f12-3953-b0ba-6474a8e717f8 | -10.8426 | -60.7429 | 2026-09-29 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 85f17684-5a87-3c5d-8c92-49621744c321 | -9.1257 | -67.8322 | 2026-09-29 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3a8beaea-68d1-39ad-a961-8df1cf839a7e | -11.48 | -43.45 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98ae6e0e-b9a4-3c1d-8963-69e951d2400d | -11.39 | -43.43 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37450564-a8cd-328d-a2d2-5dfc981ee5e9 | -11.45 | -43.49 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ba29f98-f7f4-3705-a7cd-60ad086efa0f | -7.84 | -45.84 | 2026-09-29 00:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cc52131-3514-3196-8dd1-52c3c12e1b8e | -11.44 | -43.4 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6f4c161-a832-3196-aaea-17d80b0086f0 | -11.42 | -43.57 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 729e64fb-0e95-3e56-a3b2-496c83ed5f4b | -11.39 | -43.47 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9dc0cd7d-3af2-301a-b7d4-b27f965bedf5 | -11.45 | -43.62 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec6a676c-6d13-3697-9ad2-13ba0ce3bb66 | -11.42 | -43.43 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23ce0914-520a-3e67-8b3c-8525b76dad48 | -11.45 | -43.58 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e285db81-cf0a-375f-a6cb-acfe4cf2b836 | -11.45 | -43.76 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 169c60ff-a852-35f3-9c51-69c3f65a63b0 | -11.45 | -43.71 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 790de24a-803d-3337-8172-8fe9c69ce9e3 | -11.46 | -43.85 | 2026-09-29 00:15:00 | MSG-03 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dd53dbf1-0a9e-3ff7-a635-b7f8defd28a7 | -11.45 | -43.67 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef59ae27-26d6-3104-8ffe-3ffee0989b4c | -11.45 | -43.53 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15907780-9196-3e7a-9b02-e474dda4bb17 | -11.42 | -43.52 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83612adb-f3bf-3fe7-ab94-1dd4edf53fe8 | -11.42 | -43.62 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45c8f716-1c5c-37cd-ac48-8adeccc47ccb | -11.42 | -43.48 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad24fbd7-3cf6-3e67-971b-c80dceb0e28d | -11.47 | -43.4 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0b40531-6e66-397a-a371-7a485a0d0267 | -11.48 | -43.49 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75683657-6c03-3eaa-a3a4-ebda182010a7 | -11.48 | -43.54 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ccdabe2-3cab-38c4-8d76-a8bc126d0a70 | -11.45 | -43.44 | 2026-09-29 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b0fbf7f-a926-3eba-a1de-fa3c8f15b5f6 | -11.45 | -43.81 | 2026-09-29 00:15:00 | MSG-03 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12feb5db-1082-35c9-a522-62b65327f73c | -22.6729 | -51.8581 | 2026-09-29 00:20:00 | GOES-19 | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| 21f95cd9-459b-3a41-a638-75a6aa7fae40 | -15.0926 | -53.8862 | 2026-09-29 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| fdb0264f-0e96-30b0-a2e0-245d5b192889 | -10.3894 | -61.2502 | 2026-09-29 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 170.0 |
| 1acc9fc0-dd29-347d-977d-1e97c7d15ae2 | -10.8103 | -48.7574 | 2026-09-29 00:20:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4496ff31-51cf-3985-9499-faefa4922205 | -9.1256 | -67.8507 | 2026-09-29 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c001ec40-761f-3c2f-bc8e-6756321d62cc | -9.1257 | -67.8322 | 2026-09-29 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a3a99cad-cd65-338b-8730-ee95334bec8e | -10.7064 | -44.4317 | 2026-09-29 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ebd0866a-f148-36c5-8ab7-201205da8877 | -7.6838 | -48.8682 | 2026-09-29 00:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f5f727d3-992a-3cc6-8d8e-277eab7e5f1a | -7.4728 | -45.826 | 2026-09-29 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f60dd247-dadf-3524-bd5e-8878c2191d83 | -10.4079 | -61.2685 | 2026-09-29 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 519eac2b-f652-349b-89b5-e54bc31383bc | -5.7374 | -45.176 | 2026-09-29 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 428fc385-d232-3dea-bc7f-ec02786741c3 | -11.3633 | -54.0452 | 2026-09-29 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e446c85c-0132-3ba9-b882-9f3bfd36d49a | -18.5885 | -48.415 | 2026-09-29 00:20:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| 7a49a392-356d-3928-a634-06134b823180 | -11.1775 | -44.7832 | 2026-09-29 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b3a5ab7c-05a1-3efe-bdf7-d1df96c55214 | -15.0923 | -53.9072 | 2026-09-29 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 178.5 |
| b6a310a2-9f16-35f6-a8b2-46dcff998239 | -7.8483 | -45.8363 | 2026-09-29 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6dc4f703-f056-38f3-99cb-a3f8d9cccaf2 | -7.8488 | -45.7912 | 2026-09-29 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| fa527464-24df-3142-9bb5-0dd7d1afeeed | -11.1897 | -50.056 | 2026-09-29 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 41d7bb27-cbbc-3802-be3f-61ee7ea00c96 | -6.31 | -52.6389 | 2026-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1ddc531b-4267-3ca7-9e08-66a7c9660735 | -6.3287 | -52.6174 | 2026-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9f145252-3178-3ebb-b01d-fefa8113ed23 | -18.1042 | -42.6424 | 2026-09-29 00:20:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| e47a968e-4e93-3045-9df2-c6985303f4ba | -18.5684 | -48.4191 | 2026-09-29 00:20:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| 38df6408-653a-3b3e-a666-6be4161e2da0 | -10.7913 | -48.7596 | 2026-09-29 00:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d9de62f4-ca4e-356f-abf9-f1435fb301f3 | -8.5738 | -66.994 | 2026-09-29 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| a96eda77-38ab-3c0c-9996-c0d3464b6952 | -15.131 | -53.9023 | 2026-09-29 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ce94d5b7-8faf-3777-8118-78c4f32e3e75 | -8.5738 | -67.0125 | 2026-09-29 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a0d9b94d-dcf5-322e-9ee8-9ce91910053b | -18.1244 | -42.6373 | 2026-09-29 00:20:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 55d07388-afdb-3320-b900-f43b914ba059 | -7.8297 | -45.8156 | 2026-09-29 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 51f5d959-fb50-3b19-8d81-db2ae9779fc0 | -9.9266 | -60.7171 | 2026-09-29 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 17ac0dd0-1ff3-31ef-8c04-5e748405d845 | -11.4012 | -54.0417 | 2026-09-29 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 78468adc-9de1-3142-9c4c-d0437dfe6f8f | -5.6081 | -45.0038 | 2026-09-29 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 915bb06c-99d9-390a-b75e-09e9bc2ee43a | -18.1049 | -42.6174 | 2026-09-29 00:20:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.0 |
| 2bc7d007-24f7-3759-a355-a96c67959d4e | -9.9568 | -59.2629 | 2026-09-29 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8a64625e-fd01-30ea-8405-58af34a1c144 | -10.4081 | -61.2492 | 2026-09-29 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 04fcf95c-1fde-38af-b0ee-23739eb39f97 | -15.1113 | -53.9257 | 2026-09-29 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3825b162-ed87-3631-89c1-808e3d5ebf90 | -11.1707 | -50.0581 | 2026-09-29 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 3365a719-3e02-3302-a817-c11b09a5a2d2 | -5.7384 | -45.0626 | 2026-09-29 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a5adb3f8-b878-344a-9736-911ec9e3c2dd | -15.112 | -53.8838 | 2026-09-29 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 9ea4804d-b5e5-3699-a407-cad6010ecd64 | -11.3823 | -54.0434 | 2026-09-29 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 54bd2b63-9b4a-384c-9ac8-1a465ff77001 | -10.3707 | -61.2513 | 2026-09-29 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 95c43af9-15c9-3831-b99a-d7773ed7bc17 | -15.4585 | -46.1367 | 2026-09-29 00:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f8ec74b1-369e-38f3-a2ae-8440fac8f380 | -6.6812 | -55.1103 | 2026-09-29 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b5df8d00-1f8e-373f-8fd2-026a4b77dbf3 | -6.2947 | -43.6427 | 2026-09-29 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 182.7 |
| c20e1688-44fd-3305-b141-e47a4b416ded | 1.6567 | -55.8833 | 2026-09-29 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 74cabc9c-8e98-3792-8ebe-388740744dbb | -6.3101 | -52.6184 | 2026-09-29 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 7b9fb49b-56fd-3260-92a5-b603e77c0879 | -4.4507 | -47.9112 | 2026-09-29 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cabb57bf-41f5-31c6-92c9-3296c92db174 | -10.3892 | -61.2695 | 2026-09-29 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 6d840c8d-59d2-377a-9387-c30a604780db | -15.1116 | -53.9048 | 2026-09-29 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 1f1d08ae-d4a4-399f-902b-b33767a59bbf | -7.473 | -45.8035 | 2026-09-29 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 636a1b67-1bad-3490-976d-619e83534f0f | 1.6566 | -55.903 | 2026-09-29 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0b0843ea-42da-3662-8a5e-e8490d5c74f1 | 1.675 | -55.9028 | 2026-09-29 00:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 69294302-7d05-3727-8e99-fd10a4b7fa0d | -7.8486 | -45.8138 | 2026-09-29 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 391.3 |
| 066558bd-3e2c-3b09-92b3-6c69e01ba9c2 | -15.1116 | -53.9048 | 2026-09-29 00:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 69c80290-5a9a-34d0-84b6-c450351757d7 | -7.8488 | -45.7912 | 2026-09-29 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 1b243471-bc7d-3f62-a453-7a62d5749d1b | -18.1049 | -42.6174 | 2026-09-29 00:30:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.4 |
| 6abc444c-b501-397e-9dd4-7c3675ff9876 | -7.83 | -45.793 | 2026-09-29 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 59193ebc-7163-397a-adad-1a4abe43094b | -8.5738 | -66.994 | 2026-09-29 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| bd5af823-20fb-35d7-b01c-2607873c1d50 | -9.1256 | -67.8507 | 2026-09-29 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| bb921cc4-abe9-3e31-8a9b-b9dae42dd81e | -15.4585 | -46.1367 | 2026-09-29 00:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 9ab1766a-e32a-3510-9883-f1c3b7dd9225 | -8.5738 | -67.0125 | 2026-09-29 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3d335c08-dedb-38b0-9560-6e63f0b915b9 | -18.1042 | -42.6424 | 2026-09-29 00:30:00 | GOES-19 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| 51b54af5-42ed-3b48-b2c6-151a6e5eff01 | -15.0923 | -53.9072 | 2026-09-29 00:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 951aa876-f6fd-3b02-b60d-2dd10db68df2 | -7.8483 | -45.8363 | 2026-09-29 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d7a84ba1-a7da-3c81-a672-cff58100ef11 | -9.9266 | -60.7171 | 2026-09-29 00:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 32efd450-95a5-33f4-ba3a-e16c4e9cfe5e | -5.7374 | -45.176 | 2026-09-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 97ca1f28-4a9b-389c-bf1a-9f55caae9161 | -7.8486 | -45.8138 | 2026-09-29 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 345.0 |
| 376840f4-d575-33ca-96d1-62a06ccdb92a | -18.5684 | -48.4191 | 2026-09-29 00:30:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.4 |
| 9d8f4711-4e69-3c75-80a8-4ffc15cb6e01 | -6.2947 | -43.6427 | 2026-09-29 00:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 162.0 |
| fa369773-9164-39cb-baed-54645974742f | -5.6081 | -45.0038 | 2026-09-29 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d4e66eb5-e4cf-3cf5-b476-54f7fe020af5 | -6.6627 | -55.1112 | 2026-09-29 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |


[Clique aqui para ver as próximas entradas](README3.md)
