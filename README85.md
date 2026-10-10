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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f413512f-4251-38dc-8573-35582fbdb86f | -12.30376 | -47.04847 | 2026-10-10 04:46:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2905aa44-0907-3698-97bf-2da7e0ba02a7 | -6.46418 | -55.49594 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 302160a8-e2cf-3b63-9f64-bc94c8ef2a66 | -7.59291 | -43.07875 | 2026-10-10 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 057bb4da-7ac9-3850-94ae-eb5dd3d17f1c | -10.39188 | -53.81323 | 2026-10-10 04:46:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3a2fa2b-9b31-31f5-b76a-b7662cfd2488 | -7.91075 | -54.71168 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3aa8b76-dcc4-3fdf-8edc-34fba8a5a63c | -6.75492 | -48.72518 | 2026-10-10 04:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57b8f3d6-ce90-335e-a142-5d41a489d6be | -7.03281 | -47.68103 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edd3960e-6c74-3f9d-93ec-162cdce541b6 | -10.24718 | -49.66524 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4671d65-c496-3378-be70-5e85cec5a394 | -7.40047 | -44.7602 | 2026-10-10 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d327aad-6895-3981-a0a9-310ca6185c17 | -11.2462 | -44.84723 | 2026-10-10 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db744627-6e84-338f-8422-62fa953c115a | -11.9547 | -43.49641 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5abbf175-bc75-314f-8942-5b75049ed6b1 | -6.99625 | -47.71804 | 2026-10-10 04:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de09463f-d9a3-3c52-9542-74a5407defaf | -9.28351 | -47.39421 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c926a675-c525-3f14-be0f-727fa3f95e8e | -12.3575 | -46.59338 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d28781e-fb9f-31ce-9590-5b900f4d6f8e | -12.11706 | -43.31733 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 720bd02a-d856-31a2-801a-a4a1ca2e4f9e | -6.04397 | -59.90774 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e29781c-f3f0-3b8c-b6fb-eea2a6faa2fc | -8.2265 | -46.38807 | 2026-10-10 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f33aeac5-4fa0-3d26-83a7-8c02e61744e6 | -8.34097 | -45.0102 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 213f965b-ffc4-3903-a6f9-8cd9919a461c | -10.94963 | -47.73889 | 2026-10-10 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bdb9c5d-8c01-3e3b-90ca-c52693bbb91c | -12.0571 | -43.40919 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa636533-58c7-389f-9993-a45a83bac078 | -9.87049 | -50.51889 | 2026-10-10 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 999f9261-00c4-3d9a-8d34-eb0b3072903c | -10.28659 | -43.93139 | 2026-10-10 04:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51bffe92-c0fd-3fae-96ef-4072d062461d | -11.76082 | -43.53046 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdd916d2-7fa2-37c2-a800-500fc7431903 | -12.38742 | -46.61013 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5998b2c-3448-315c-8780-8266ef8603a7 | -7.23476 | -55.17749 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bff36e92-fb47-31d3-b513-cc92496a306a | -9.73468 | -57.3671 | 2026-10-10 04:46:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4844c90-38a0-340b-a475-49f8e1285840 | -6.45801 | -55.05253 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e284f332-860b-30d6-9878-e20012833c8b | -11.77697 | -45.5098 | 2026-10-10 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02ddebd1-8a9b-3c9f-a419-086a951ea15f | -11.83901 | -46.81107 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e47fa3d3-19f2-3e3a-9b70-964270cd14b5 | -6.6229 | -59.95065 | 2026-10-10 04:46:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fd74ea8-272d-3d99-bc79-266e04dee70a | -8.99889 | -47.74121 | 2026-10-10 04:46:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38452ea1-0581-3767-afe5-1830c54f07e6 | -11.12397 | -45.94902 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2c27c64-3559-343a-a945-696ad5ff094f | -12.38162 | -46.57663 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b810fb0-cd32-3595-8630-bd54bd880195 | -8.94851 | -47.37463 | 2026-10-10 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eada1ff-ad1f-3032-926a-5c6c7ba685a8 | -11.68447 | -46.85916 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a18d8bf-f41b-3983-8a16-2c722f64b498 | -13.77741 | -48.129 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9465d81-ad52-3279-9502-a0749b08f821 | -11.75856 | -46.79209 | 2026-10-10 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eb474cc-def1-31b2-8e43-d1820ee8ccb8 | -13.28885 | -48.55856 | 2026-10-10 04:46:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bc32048-6189-383f-a9a8-8108e50c7373 | -12.36922 | -46.61144 | 2026-10-10 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e401f02-086f-38f1-b06d-4c1a157039b3 | -6.45043 | -55.29325 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8c0f078a-854c-3b78-a2ef-5dd366cf10e4 | -11.08115 | -44.11713 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b478c5a2-05bc-3239-88e5-38322fba2131 | -8.20914 | -46.88205 | 2026-10-10 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c36ccbd-7dcc-335e-a093-f4bbf328161e | -8.32622 | -54.67373 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d89f923-f81b-3ada-9ca0-fd0ed6fdd07d | -8.24073 | -46.43185 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6b44766-82bf-3c92-aafc-9fcad8c5f628 | -13.51388 | -48.61259 | 2026-10-10 04:46:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e19ed3aa-a047-3b70-8142-afbcdba4332c | -11.66989 | -43.70092 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83754e11-46b0-3ba6-90b6-dd7d19e0c7d2 | -7.11188 | -52.65285 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba2a262e-b5fa-360a-acc5-c4f24d5c471c | -11.08412 | -44.11481 | 2026-10-10 04:46:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93dc9777-0364-3b61-85a7-ada723e56747 | -9.10073 | -54.69949 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8a90b32-0f89-3662-a4d3-6dbc8bb927dc | -8.58525 | -53.09854 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05472fff-ac3b-3e0b-934f-e1aab35431ba | -7.582 | -49.53006 | 2026-10-10 04:46:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0434153-4200-3bcb-9424-70da41b56d3f | -7.66604 | -49.78833 | 2026-10-10 04:46:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc051f8e-0e97-3e83-bac3-ce4731d40a32 | -9.3047 | -47.37898 | 2026-10-10 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc4cf969-8809-38ba-a195-0dd2f62205f4 | -10.99757 | -45.39674 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83e1b9c2-d243-3bf4-82fe-4e1923a74923 | -8.18942 | -54.72147 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b75f6b05-607c-3e94-ae10-235f155e81e1 | -9.71333 | -46.94175 | 2026-10-10 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72a187c8-fb41-3efe-8979-ac49e1521d71 | -13.52287 | -47.4155 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76be7225-e973-3c95-9e96-2faa70fe49bf | -7.18958 | -55.15976 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebfd06df-3470-3ccd-b051-3163dc6c131a | -14.01836 | -48.75603 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 737edd53-94a1-32e1-b59a-a12312689a50 | -8.94604 | -45.11913 | 2026-10-10 04:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4c9f568c-0591-3742-9097-7edbcbe5f005 | -5.85864 | -55.70309 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f725224-d5e3-37cf-a7bd-9ed58d09f483 | -10.98087 | -47.79224 | 2026-10-10 04:46:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e8a6a1c-3b1f-3e1e-b7bb-cc71fbb4169f | -11.1766 | -45.32277 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7690b38b-bef9-3e98-99ab-e40048901ce6 | -13.7746 | -48.12476 | 2026-10-10 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e1d49db-be76-3e99-9efd-16418515e985 | -14.68424 | -46.8554 | 2026-10-10 04:46:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2003cd29-36e8-3dee-b98a-ec9a6550e5c8 | -7.59813 | -47.08017 | 2026-10-10 04:46:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6e64a28-6010-300b-8659-d5d69aee2fc7 | -7.18635 | -52.63628 | 2026-10-10 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6e02ad4-df95-3935-a786-9a3287eaac0f | -13.53321 | -47.41712 | 2026-10-10 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f0b403f-2ab3-301a-b17e-0e5f44e42b32 | -11.0306 | -45.42753 | 2026-10-10 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ab68af1-655b-32da-a56b-45cd6a8efd50 | -5.09529 | -60.22172 | 2026-10-10 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f14dc542-c944-346a-beda-7602dfca72fd | -13.59637 | -48.57757 | 2026-10-10 04:46:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3b10ade-6cb7-3277-85bb-a6bff727cf22 | -9.51426 | -54.67768 | 2026-10-10 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f972ae4-75db-3dfb-855c-d85991acd117 | -11.60256 | -43.71551 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aec8ae50-ebf5-3fc4-847c-529bcbd8a8b9 | -9.32089 | -46.47533 | 2026-10-10 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99ceed23-98cc-3f4a-9761-6e50f553205c | -13.15221 | -54.36385 | 2026-10-10 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57c2038d-74f2-3bcc-a7d7-59ac2c20250e | -9.7385 | -44.79316 | 2026-10-10 04:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69cf6d46-d50b-38fd-a6f0-2af890d78f8d | -6.36963 | -55.1689 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c8699a9-06c4-3b97-8f5f-cbc08026c126 | -7.23019 | -55.15731 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da99cd7f-514a-3465-92fb-8a5205b2a044 | -14.96868 | -41.69277 | 2026-10-10 04:46:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bf498c1a-ccec-3d49-b926-1c50654c1878 | -6.37742 | -56.2272 | 2026-10-10 04:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f519f21e-8298-36f0-8430-a35bc539ecc4 | -12.02551 | -43.48457 | 2026-10-10 04:46:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72ebd94f-501f-3531-aa49-2da8eaa98b25 | -7.51676 | -48.022 | 2026-10-10 04:46:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 71506327-7a8a-3134-8e79-101f79efacd3 | -14.02114 | -48.76022 | 2026-10-10 04:46:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f73c26ab-dfd9-3198-949a-9f1657612aa0 | -10.05083 | -44.3462 | 2026-10-10 04:46:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c272bbfa-df53-313a-bd6b-1d3200f33c7d | -11.46783 | -43.38532 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f75be8cb-1b6d-38e7-a74c-fede10d5e6ff | -8.55489 | -46.90234 | 2026-10-10 04:46:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e813ef4-aaa1-3e61-a037-1a528a758e1a | -7.90917 | -54.72073 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae89dc9b-7e04-3509-84de-fcafba0c661c | -11.57038 | -43.70665 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b40d41c-0d0c-3972-b03f-9d4745ba79b3 | -7.21415 | -55.07386 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af14bb9f-d735-33fe-bf19-94dd754f4d4a | -10.0453 | -50.93304 | 2026-10-10 04:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8758adc-32ff-3a10-9f09-793873b69329 | -6.92876 | -59.26035 | 2026-10-10 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ba42a9-920c-328f-81c9-9d6e9a7fb109 | -10.24762 | -49.68372 | 2026-10-10 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a7a624a-7852-3eb5-adc8-ef36f5c742e5 | -7.20698 | -55.08752 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 909db539-2fd3-3242-bca0-8c91073a4e03 | -11.56063 | -43.6932 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e69858ce-42ca-346f-8cc3-cfc3ea7e13ef | -8.79423 | -47.57928 | 2026-10-10 04:46:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 977842f9-ef9c-308b-bf38-e40b48fd9370 | -13.39482 | -43.88389 | 2026-10-10 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf0f8095-eeb8-34a6-b4a6-841184f6e3f4 | -11.59235 | -43.69881 | 2026-10-10 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 192bbae6-2fa1-3ec3-b4dd-4e91416fc4a7 | -8.49037 | -54.61226 | 2026-10-10 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b9b4f62-d0a9-3402-9d3d-94db95a83fdd | -8.52107 | -46.89696 | 2026-10-10 04:46:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| def75fa8-0ccf-3372-b1ae-79bae92902f1 | -11.46034 | -59.1295 | 2026-10-10 04:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README86.md)
