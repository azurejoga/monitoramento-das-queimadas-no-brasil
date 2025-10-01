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
| a138cf88-06e9-3ba6-9652-ba68660f7f1b | -9.9189 | -43.6743 | 2025-10-01 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| d8ffc954-8684-3023-9cda-20d3596b851f | -8.5587 | -44.7414 | 2025-10-01 00:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 659bb12a-69f0-3ee2-b2b4-27c6c3a5937c | -6.2707 | -44.1766 | 2025-10-01 00:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a76f6ccc-75fc-3ed7-94d6-c0b0abe79c62 | -13.2969 | -50.6821 | 2025-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 1dac0550-b175-3a41-af31-676debeaa8e5 | -3.4577 | -50.089 | 2025-10-01 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| f3938e09-4653-3e12-8045-4562aa1cb610 | -10.9395 | -46.504 | 2025-10-01 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| c76e973d-af84-3dc1-ac0a-c24e41488b40 | -11.8246 | -44.9669 | 2025-10-01 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| da53adb3-a594-31b8-8fa5-c23845c9747f | -13.2781 | -50.663 | 2025-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 144.3 |
| febeebff-e586-3001-93a7-80197772062e | -3.5161 | -49.4528 | 2025-10-01 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c2c44865-7e27-3a71-9f1e-3bc3c2727abe | -7.2765 | -48.4684 | 2025-10-01 00:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f02ed1ce-1ebc-3c2a-946a-359b2525e0ea | -9.9193 | -43.6508 | 2025-10-01 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 222d0ceb-509d-3f84-9eaa-8e049947705e | -9.2902 | -54.5242 | 2025-10-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| b4d4498b-a620-3069-9a85-165632693536 | -10.0145 | -50.2657 | 2025-10-01 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| fba9fd2d-6c66-3f36-b4e9-beb102e55e30 | -10.0337 | -50.2424 | 2025-10-01 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ac40cfb3-623a-31f3-8956-09b350690220 | -22.6279 | -49.0535 | 2025-10-01 00:00:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 75.1 |
| bcbf8fde-de9f-3a44-b421-6326916d04fc | -21.0564 | -45.6881 | 2025-10-01 00:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ef8f7405-f5e4-34cf-acf8-32862ef76246 | -5.6363 | -43.9027 | 2025-10-01 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9522b8b3-e3a4-3de7-9048-a3b777dfc974 | -22.1217 | -44.6886 | 2025-10-01 00:00:00 | GOES-19 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 9817e4cf-15d2-3421-bc99-0a0c65a61331 | -3.5162 | -49.4315 | 2025-10-01 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 0ac33620-d9a6-3b69-a58b-bd454de8b48c | -3.1013 | -47.0082 | 2025-10-01 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 5de019ed-c7c9-3563-89e8-8965bb06f731 | -3.0827 | -47.0088 | 2025-10-01 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1dd8c62d-ed6f-3f5e-baab-acc6326d83db | -8.559 | -44.7184 | 2025-10-01 00:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 1dc50bb3-12de-34ef-8df8-f224c43e6c50 | -16.0225 | -50.8771 | 2025-10-01 00:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 39af9ed7-a16b-3806-8ad8-410829c3f87e | -9.9383 | -43.6483 | 2025-10-01 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| f463f16a-3aaa-30a9-b145-470ae98a2adf | -11.8054 | -44.9697 | 2025-10-01 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f3f541db-4451-3457-8392-2c2ffda5240f | -10.9204 | -46.5065 | 2025-10-01 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6ec10863-746e-37df-86b5-43598597c9f0 | -9.4206 | -54.5753 | 2025-10-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 724d3947-e365-31c8-94b6-2d2ef41cae74 | -13.7869 | -51.2404 | 2025-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| dd55891a-782e-3b97-b5d0-f70f29f06afb | -4.9714 | -45.2267 | 2025-10-01 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c49229c7-1d55-3a96-84b0-2e3f90456766 | -2.246 | -47.8838 | 2025-10-01 00:00:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7b14cf76-7c64-31e9-bad3-59dc5177a07c | -5.655 | -43.9013 | 2025-10-01 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9d59a198-64b9-3eed-b2cf-a0510a11672f | -9.4396 | -54.5537 | 2025-10-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9c855049-6638-3006-8271-a3655d766864 | -5.6548 | -43.9244 | 2025-10-01 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 20addfe4-1005-3c15-acc9-905a420a583c | -5.8655 | -43.4214 | 2025-10-01 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| a0d6130d-edf0-3883-bcec-d8ab2d1e9f41 | -13.3467 | -47.8508 | 2025-10-01 00:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 13ea4491-f7a8-3092-93d8-a80db6c766b8 | -6.4605 | -43.9532 | 2025-10-01 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6bdb547f-0744-3b0f-8f70-aeaf923b75ed | -13.2973 | -50.6605 | 2025-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 38b0e888-0f3d-34a0-ab33-692bf9e3e62c | -11.8242 | -44.9901 | 2025-10-01 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 84dc4b29-0169-3a62-96a8-9c72fb7fab3c | -11.3858 | -44.8923 | 2025-10-01 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 74c7a6f2-442d-3d32-a502-bdf855013695 | -21.0572 | -45.6638 | 2025-10-01 00:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| e5f07764-bf2c-3366-8749-0e95e595cf0f | -5.3195 | -43.7405 | 2025-10-01 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d582a2f2-8fa6-3289-9858-f401357e7717 | -9.0821 | -48.0252 | 2025-10-01 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 546f6223-07c1-332b-b879-6bc5b48e1492 | -5.8469 | -43.3995 | 2025-10-01 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6e1291d9-1f6b-3285-91ef-d1b7148d7321 | -5.6361 | -43.9258 | 2025-10-01 00:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| d4ff8e4b-fedc-3eac-ab64-e8f42cdcf598 | -3.6845 | -49.0421 | 2025-10-01 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 45157019-64bb-3b1a-b7ae-08a10bdde991 | -16.2562 | -50.9275 | 2025-10-01 00:00:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5cc8c550-62c8-3e07-9682-4030c4c17041 | -6.4607 | -43.9301 | 2025-10-01 00:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 203.6 |
| f72599c0-1f44-3f8c-9285-ee64180721ed | -3.1012 | -47.0301 | 2025-10-01 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6cf4cdd7-280a-32a0-8a88-f9d33e4819fb | -21.0365 | -45.6693 | 2025-10-01 00:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 78eeff8e-c0e4-364c-ab87-ec5e3cafa5fb | -9.3089 | -54.5229 | 2025-10-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 21f0df3b-61bd-3752-a471-e93b77d4ea06 | -3.4762 | -50.0883 | 2025-10-01 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 724ba635-bcb9-3b57-83f2-8c98ef89b253 | -4.9716 | -45.2041 | 2025-10-01 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 24ec9e77-a991-3732-b7dc-2ae1bb36fc4d | -21.0357 | -45.6936 | 2025-10-01 00:00:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0f3510f9-0383-3c25-81ff-662f21e78b6a | -13.2777 | -50.6846 | 2025-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| fafaa549-caa5-3328-b061-149a99990629 | -11.1523 | -54.3104 | 2025-10-01 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| dd3d1555-60eb-3e59-b097-3f75b7113557 | -5.8657 | -43.3981 | 2025-10-01 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 484f5b50-4b19-3cc3-8295-fba3e9209efc | -13.7873 | -51.2189 | 2025-10-01 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| dab93471-e4a5-30b1-a12b-0340d25c3527 | -9.4394 | -54.5739 | 2025-10-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d53c5fa1-650c-3db4-a161-643dc5785052 | -5.3382 | -43.7391 | 2025-10-01 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 13f6df61-671e-3718-8563-43cc14cd466e | -9.938 | -43.6718 | 2025-10-01 00:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 718dd577-4cda-399c-aad9-6a8e20d9bc5d | -9.3087 | -54.5431 | 2025-10-01 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 79bb1260-2027-3c44-8051-1d02c94b9f3a | -10.0334 | -50.2638 | 2025-10-01 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 83a10c26-66de-3b81-b72e-184be7740283 | -5.6363 | -43.9027 | 2025-10-01 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| fa7f6e50-3b18-3fb5-aafc-7e6f5b40c926 | -20.6309 | -46.2046 | 2025-10-01 00:10:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 726f5b81-f34f-379f-9559-5884e3b239ed | -11.4049 | -44.8895 | 2025-10-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d268cf3d-27ea-3e15-9034-3b8b2e454c1d | -9.0821 | -48.0252 | 2025-10-01 00:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| bef9858e-a90e-3e94-a4ac-aaada3ff40e2 | -3.6845 | -49.0421 | 2025-10-01 00:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 46ca5790-80e1-3aa0-bd75-98bb2a667636 | -9.4396 | -54.5537 | 2025-10-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 38530f53-2050-3770-97ce-2d25711da34f | -5.8469 | -43.3995 | 2025-10-01 00:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d3f602fb-32c3-36ae-b7a3-93e3ff8b17a3 | -11.478 | -45.0868 | 2025-10-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 67a21790-b856-3438-8ddc-2ada8ef1a30a | -5.6361 | -43.9258 | 2025-10-01 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 05061315-671e-31e8-9efa-315c6bc6bb82 | -20.6316 | -46.1806 | 2025-10-01 00:10:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| be9f2f02-dc46-34ff-8cea-ec254679457b | -10.0334 | -50.2638 | 2025-10-01 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9f31cc6e-f2e7-3ef9-9396-0a1aee5aecbc | -13.7687 | -47.9659 | 2025-10-01 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 50d524ef-6c60-34de-b2e0-a2356dbb7e2a | -9.4394 | -54.5739 | 2025-10-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d9b3b2fd-0ab3-3eb7-a8bc-b0110603615e | -9.3091 | -54.5026 | 2025-10-01 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e6df3064-781c-3b9b-ab79-6f80f2b237dc | -8.5079 | -47.2897 | 2025-10-01 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 21f97965-410f-3b70-bbc0-2b44b01409f0 | -13.2781 | -50.663 | 2025-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 519c721c-9fe8-34b9-965b-c0360a5f1653 | -2.246 | -47.8838 | 2025-10-01 00:10:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 814f1329-78d8-3a8d-80ba-778e141ddab0 | -3.4577 | -50.089 | 2025-10-01 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 4e6c774a-ed4e-3319-a9eb-2b9c89889e10 | -22.1217 | -44.6886 | 2025-10-01 00:10:00 | GOES-19 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 8786f108-be0a-32be-ac3a-4c6da34d14d4 | -9.938 | -43.6718 | 2025-10-01 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| fe8c260c-4eee-3dff-9232-8b2ea19661d9 | -9.9189 | -43.6743 | 2025-10-01 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 7bf85b14-0fa7-30d5-b077-e6ed4249d12c | -21.0357 | -45.6936 | 2025-10-01 00:10:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d07e06ef-d09d-3eba-b332-878f86fefcdb | -13.2969 | -50.6821 | 2025-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 3684d41d-fd47-3b2d-91a6-f66fdc7361e9 | -8.5081 | -47.2676 | 2025-10-01 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9241f1c9-3e41-30a0-b4ac-2ce3b9220307 | -9.9383 | -43.6483 | 2025-10-01 00:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 87e16b21-82ec-37dd-8a84-118eaa1492d6 | -20.6103 | -46.2098 | 2025-10-01 00:10:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 4f181aa6-0470-3924-8ad0-4d31ca1fc4e1 | -11.8242 | -44.9901 | 2025-10-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f6f9e179-7f80-35a5-8985-b9df345e4500 | -16.2562 | -50.9275 | 2025-10-01 00:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 8abe2dd6-13ae-31a2-8560-fa5962b5e780 | -3.5162 | -49.4315 | 2025-10-01 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7da46064-716f-3568-95c0-45211656ee08 | -13.7869 | -51.2404 | 2025-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7d0e8798-29a5-397c-885c-d4a7ad425746 | -22.2634 | -46.7146 | 2025-10-01 00:10:00 | GOES-19 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |
| 75c65d18-d37a-3269-952d-9ef84b035a09 | -11.8054 | -44.9697 | 2025-10-01 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e7592e8b-0a23-39d8-9a34-6c98113c3d2e | -13.2976 | -50.639 | 2025-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 43af47bd-52ea-3b1e-bab6-c9a3e7bce43b | -21.0564 | -45.6881 | 2025-10-01 00:10:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 2973b41c-718b-3b6e-90b6-59603f500f83 | -13.3467 | -47.8508 | 2025-10-01 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| ccf1281a-db28-387c-9e4a-30b430eb6721 | -13.2973 | -50.6605 | 2025-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 279.7 |
| 2d66f69a-ff3c-350c-805d-79b29a9019ba | -20.611 | -46.1858 | 2025-10-01 00:10:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a8d82618-7f0c-3647-8c2d-8e3798b25968 | -13.7873 | -51.2189 | 2025-10-01 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |


[Clique aqui para ver as próximas entradas](README2.md)
