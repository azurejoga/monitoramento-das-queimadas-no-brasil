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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfde6da8-296b-36b9-bd51-fc5dbcc85ac3 | -9.79159 | -48.32681 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b09bb9ce-0013-33e8-b4da-96f3242dafb8 | -9.95997 | -45.27506 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68d8aea6-a5d2-32cb-9dda-86c42fbfa4b6 | -5.66632 | -45.31424 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bba2cb1-e681-3b4e-88d5-214a8fea9920 | -8.87207 | -45.95364 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 42624fc6-28d6-3198-914a-3c8326ac071e | -10.46707 | -45.08927 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cf8e6e7-e7a1-37f5-82d0-afef4dbed2e4 | -6.92599 | -42.89775 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9b842447-05bf-3fec-8ef5-63181ee5369c | -8.67138 | -45.43109 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a957dba8-fa12-314d-9bb2-ecc54e28c3c9 | -7.64067 | -45.82498 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d24db62-25b1-3176-9e38-efb177d33ee7 | -10.13667 | -45.55806 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad6a1339-a356-376b-8a0f-20f3347c1a7b | -8.76075 | -48.65803 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c4835ea-266e-3dea-880c-9cccdf75d9b1 | -5.45925 | -44.31545 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c84c805-ee02-3ad1-b074-5b05cc4ced21 | -11.32302 | -47.28527 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ed7c12a-a777-3458-9513-208c6e501036 | -11.42842 | -45.40931 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70f6b2f3-256f-353b-b9ff-6fe540d16f50 | -11.01103 | -46.51963 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18896197-8d43-39db-bc9a-9e99947161db | -8.62812 | -47.61926 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c991567-39cc-3671-990f-34df1c81945c | -8.2568 | -50.85979 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edc94548-6f13-3cc6-ae22-bd162909cb6f | -7.06098 | -47.53107 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 200b8bad-c73d-30b6-8dc4-24fcc88e49f3 | -7.8829 | -44.85218 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07dbc485-c8a1-332c-9eb3-9daa84539405 | -7.54044 | -48.69229 | 2026-09-20 04:19:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 310374b0-7826-3bc2-b5e1-bfa6cec290c5 | -9.54859 | -46.57506 | 2026-09-20 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79d600dc-3719-307f-a69e-08155e48a3b3 | -5.66941 | -43.40226 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f327ef8e-9599-36e8-8739-cf8cc244f821 | -10.84048 | -50.93838 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f4bea20-32a0-3d8a-bdbb-9a275226f751 | -7.04393 | -45.2334 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 52f37d84-d747-31a2-aafc-8daac443644a | -8.50401 | -47.4347 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d7fd236-173c-31e2-b304-dde0c5ea7bc8 | -7.75512 | -49.20436 | 2026-09-20 04:19:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86ac45f1-e73a-3d37-aba4-dcf253cda04b | -7.15211 | -47.47606 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 758261af-b282-3fe4-8749-95a125c3dc98 | -9.71869 | -47.22044 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0480b29e-2124-3865-853e-71291dc19e4c | -8.37063 | -45.64644 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 998f3efc-87ab-3e43-bd08-0bb77268c0af | -8.44552 | -45.86966 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72a9a051-2147-338c-bec5-6b0cb3563987 | -5.84296 | -53.50913 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21ee7df3-4c24-3700-a530-325836c2444e | -8.60877 | -54.6003 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 980b1402-c5b2-3fa5-a44c-422f8e8a50fb | -8.63298 | -47.61618 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87d9c52b-24b7-3e86-83a0-c66925de6358 | -9.54776 | -46.57997 | 2026-09-20 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ec4b1f5-6e59-3727-9c10-73921abaaacc | -10.59835 | -50.24966 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab6d605d-d61d-336e-8073-6acc1160a884 | -9.12165 | -45.73296 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 239dbee6-67d1-3e1f-baef-e5e141635e16 | -9.12536 | -45.71082 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a698da3-2a86-3bac-81de-fa2839f222ff | -5.67242 | -45.30109 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17d23b80-4735-3ee2-997e-42d7335b3e63 | -9.98183 | -46.62732 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21b024c7-fd42-304d-8f17-19554b3f234a | -5.65362 | -43.36884 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e55036ef-cc9f-380b-bd16-95340daafdae | -7.16965 | -47.4505 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e81471ca-40ca-3e54-866c-86bb4385f10e | -9.36173 | -40.31 | 2026-09-20 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 346036cb-fe6f-3f3e-999a-135a65ffa410 | -9.02079 | -44.92934 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92e0c922-c349-3e15-975e-c153c9f2cd44 | -11.45288 | -45.37217 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a42df976-4116-311a-aba6-8625b73c23c2 | -9.7809 | -45.07122 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76a4c971-3593-3b35-9c5b-7e6d7ca82710 | -5.64366 | -43.37511 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d82ff9b2-5993-308e-a85b-865f4eee5af7 | -9.72466 | -47.20978 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60cc8412-0f6a-315b-bd06-30459369e2e0 | -9.93421 | -45.27489 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89b858f5-94bd-3383-af3a-8f68fd99af22 | -11.34085 | -47.34588 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef60b9e3-8305-37b5-ae47-a9fb5d787d6b | -11.48231 | -47.77713 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fbdff93-a3f4-37dc-9043-11d135580f06 | -7.79416 | -44.91849 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2ae23c3-307f-3fd1-87f3-fdf88274db29 | -9.68844 | -49.28298 | 2026-09-20 04:19:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90fae64d-762c-3b11-a3eb-818803b73345 | -7.18636 | -47.90121 | 2026-09-20 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43606a42-c880-351c-b3ed-3fb818b9f0df | -10.26787 | -48.11559 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85420370-207f-3b9a-b44e-88600e54f3c7 | -4.86198 | -43.54722 | 2026-09-20 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 791a5926-425d-3788-83ba-836ab3847285 | -6.30996 | -47.63143 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e95a67c0-e14d-3ffd-81ee-a4a29c89bbec | -7.80109 | -45.12236 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 615fee37-21ba-3a60-9578-e6571ae2b480 | -6.26525 | -41.66031 | 2026-09-20 04:19:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4c90e28d-db77-38e2-9ffb-850e4d877730 | -10.84229 | -50.93806 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 012b0022-2c19-3bb3-b9de-2728d8ffc644 | -5.847 | -53.55909 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd95ec73-ce2b-3354-82c2-5cbc3dfa4640 | -10.84282 | -50.93511 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f66002a7-3f37-3128-b4ee-63e9c562a7e9 | -8.38855 | -45.63079 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e507326f-6d26-3b7f-bf83-3d161c66a895 | -5.43641 | -47.61191 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7a110b8-34e6-3558-aa1c-b224aec5eb52 | -7.32379 | -47.43736 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fae11e1e-064b-3ae7-92ea-2f648ae5278a | -8.60948 | -54.6119 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 197a4147-d28a-3ce3-b67d-abbfac0a5be0 | -6.66895 | -50.89589 | 2026-09-20 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efd1ff83-1edf-3c7e-8930-75661c5fe8c4 | -11.1862 | -45.38739 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0be6e4e5-6785-3486-a334-890487985e5f | -8.67651 | -45.42311 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8e8b73a-9de7-318a-97ce-531241d4753c | -11.48571 | -47.78156 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5057c9f6-03ea-3a04-9a2d-2cc557e23b5e | -5.84835 | -53.51789 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25ba2a65-8aea-3b0f-9a15-8d66cd1b1a4f | -5.35124 | -44.83755 | 2026-09-20 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42ba8443-3f0f-3684-a9e5-f136bcbb2239 | -10.27274 | -50.26161 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 58350aa0-2407-3f80-8158-a82700e8ff27 | -5.85023 | -53.50737 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20ca5d36-0a25-38c9-bfba-baa2d56d94ea | -6.99376 | -42.16579 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3e76f139-ea74-31b7-89a9-9fffab761e04 | -6.74333 | -44.09763 | 2026-09-20 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2e63528-fa21-3e9c-92ca-8844e8b42250 | -9.2296 | -46.23871 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f110575-9219-3555-bde5-adfbe6813aa2 | -6.59621 | -45.88058 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6f5354d-c73a-3b5d-abda-b9edce92266b | -9.78499 | -48.33167 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3df87a74-428d-3abc-af2f-8d0bf8f3fd40 | -10.28152 | -50.24094 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e1b20ee-6aad-3824-bad1-a510b1e84ae4 | -9.23343 | -46.23925 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 245f80e8-ea32-3c81-90c9-b7a6c188b061 | -6.41191 | -42.812 | 2026-09-20 04:19:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df96de15-2f04-38ac-a6fa-382272205978 | -11.02043 | -48.33683 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e16c5000-3820-3b6b-b955-8569c3f3512b | -3.85061 | -51.33978 | 2026-09-20 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 683d5e7b-150c-3a7f-9036-f9cdca43e4b4 | -11.21953 | -48.38533 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20d8a875-d46f-3e8a-8c85-e7da30b2cee3 | -9.83923 | -46.40559 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 121e5fee-7b34-391d-b385-f0551f84cb23 | -10.30088 | -50.27259 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b14a9e24-3137-3971-a608-55c894117680 | -10.99872 | -48.31241 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c71f07a7-b49e-3915-8ede-c01916d7d05a | -10.57013 | -46.5407 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 499fc865-36bc-367f-809c-7024a594be2e | -9.92946 | -48.38547 | 2026-09-20 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b90e8b9a-f0e6-3bd1-990f-e7151be1020e | -10.38344 | -48.3174 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9450c745-ef94-3830-a708-73c8045a0fb2 | -9.53791 | -45.40886 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b9d49e6-61eb-3ab3-b86e-d155bdc332b9 | -5.60176 | -44.3832 | 2026-09-20 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f9f6855-e54d-3160-9c95-87d58fbdc698 | -8.4382 | -43.86408 | 2026-09-20 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 66e35d00-5e51-35d7-a780-56ff06edb527 | -8.75915 | -48.66726 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd245280-d0a8-3683-9495-f4b53c5501b1 | -4.95039 | -45.39465 | 2026-09-20 04:19:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15db0262-28c2-3249-9733-80d4be45afb3 | -11.03372 | -48.31108 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f40a78da-cbbd-3df4-be3a-4c853d7ead86 | -10.60045 | -46.52357 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92dd7bfc-179b-34d8-ad23-75c555b95029 | -9.26159 | -45.9375 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00a883b9-99eb-3425-b298-ebb60ea63615 | -9.57209 | -45.47473 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a22565ce-3404-3cc9-9168-1aeb4230ab72 | -3.44638 | -50.60243 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3cbe97da-078f-3d5e-afd2-08d85f52899a | -7.17838 | -47.89539 | 2026-09-20 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README26.md)
