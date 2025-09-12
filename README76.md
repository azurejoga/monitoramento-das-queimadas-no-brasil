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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8f57b8c-1ce8-3edb-9432-7f10a49bc8fd | -11.6848 | -46.5249 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5127745e-2a1d-311f-9168-5aa9042c693e | -9.34874 | -46.59609 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a1b9eb3-c718-3a21-8f15-50fdf97fc6dd | -8.96386 | -46.0829 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21344d72-3415-37b0-802c-6599cc69d307 | -12.24982 | -46.75267 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca6d31b3-8d3c-3e3b-b3bb-eebaba9111cd | -5.73993 | -45.5957 | 2025-09-12 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db4cdfc5-c15f-34aa-acdf-bf8c78a8bedb | -12.0902 | -47.58198 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4304d981-1c4f-3de1-baf3-114900e7d479 | -12.11191 | -44.87466 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d54ee117-126a-3ef4-b4d2-10209b1cda54 | -7.15946 | -48.89494 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2bd0550-c095-3c90-b687-bd02a403d757 | -7.75745 | -50.7741 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7ac03b7-3330-394e-968c-51a7d1553967 | -10.68436 | -48.66011 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7d2c3b6-597c-37f2-9c9c-93e31ff351d6 | -9.9934 | -51.71609 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82e66b6d-39f2-3d61-bcfd-687691a120e5 | -6.90674 | -47.8991 | 2025-09-12 04:25:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23208f04-849f-3161-835e-a93679a6ede7 | -10.44213 | -50.60418 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9e95df7-f65a-34ea-a11c-f757f860314f | -6.31974 | -42.22338 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 41b3fd6c-f299-3197-9f37-8a16599ed73c | -9.70232 | -48.30716 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adbf794a-7c12-3c35-a30a-fcfb4fa81be7 | -11.53793 | -50.40697 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| c2f6e29a-af1a-3613-b785-c1cb77948422 | -9.78578 | -47.84571 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99570c2b-65eb-3d8b-b231-a603f2a07671 | -10.42103 | -50.61778 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f16bc03-4b97-378b-befb-6505a046a993 | -11.14283 | -45.23903 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d514020-d83d-32c2-aeae-9ee7bd39a86a | -12.54273 | -44.68899 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3dc39633-d94a-3a8a-945c-68a36963e79f | -9.69072 | -47.54918 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5af49100-26fc-310b-8cd0-2e690ebf1aed | -11.46776 | -49.27799 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f5fa4ab-001c-38b9-813f-508d86b96c3c | -11.68708 | -46.57642 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ed75a8a-864d-3af5-9154-78be4227426a | -7.24065 | -44.4816 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a59e86c-a783-323d-af41-4296660ce10d | -6.84203 | -47.86288 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0fd17a2-d2e8-3e5c-85df-94e95455afc2 | -8.95998 | -46.0859 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb343102-00ad-3ee2-a5eb-3d6d37ab2933 | -7.07388 | -44.13218 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb329e9f-772d-3eab-af8b-956dacc646ad | -10.21611 | -46.23627 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d2cf39d-d02c-34b9-9490-2bb34c0212b9 | -8.95529 | -46.72278 | 2025-09-12 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99cbd40e-ebc3-3e7a-ad16-a83f1922e6c9 | -7.47204 | -45.30344 | 2025-09-12 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97d2fe59-9125-3d3f-9497-d93fa903b3ca | -11.20058 | -48.41228 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03bb630e-64f2-39e7-8c1a-9728f833cdf7 | -8.87792 | -49.53271 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84c14aff-457f-3dd5-8b2c-3de9b490ddaa | -8.17586 | -46.08541 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dae4093-c0e0-3ec4-ab09-e18df88715e0 | -7.55509 | -44.39409 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af6494c1-ae7a-3c21-9a5b-2c7ae466067c | -8.57817 | -51.35413 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33d2e624-5ae1-3e0a-8b55-6685f5da067c | -11.66488 | -46.58746 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b01b3c67-02a1-3390-bf84-d269e038c091 | -5.54141 | -46.42498 | 2025-09-12 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3adc3cc3-fa9f-394e-b9d5-bd40a6897138 | -11.52674 | -50.39327 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af41abdc-7b70-3ef5-9659-838bcffe450f | -9.99085 | -51.73118 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4502cfa9-ac1c-35a8-b263-cae963c63aba | -11.87771 | -47.52979 | 2025-09-12 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b13e6b10-cad0-32e1-851c-1279edae89bc | -6.81786 | -45.65052 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e2600da-ddb5-33e8-ba38-83908fdca68d | -11.52385 | -50.38853 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 70082f61-df06-3a3b-b673-deeb60d341b1 | -8.05466 | -52.32184 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48913dd0-0b67-3f01-a9b4-74979649de93 | -10.27369 | -47.01954 | 2025-09-12 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1095df53-1b6a-3154-92f5-8cae46efa5ba | -12.11839 | -44.85505 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27088ff0-546f-37f4-bdec-9d8a908abf89 | -11.6588 | -46.60472 | 2025-09-12 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70d8138a-fd4c-3eea-80b6-1a65c01a844b | -9.21796 | -59.37978 | 2025-09-12 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8fe2b19d-9920-30f6-860f-b3941af66305 | -9.06874 | -50.49826 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b87c7f2-080c-32da-b845-8742c7e0f35c | -9.03513 | -47.07821 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eb71cd6d-66ff-3437-8c9c-2bfc80475e53 | -11.6849 | -46.61256 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 403469ad-8e2c-33ef-ab2c-ec63435c3e96 | -9.91029 | -47.76818 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b37e7cf-2ac5-3d2b-b66e-ea3d2ac87434 | -8.40957 | -47.27425 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 641e2b3d-840a-3ca7-a2a9-8bd5e2a8b93b | -6.40957 | -42.60432 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1389886d-4ecf-30f5-84e3-77f5f4647f2f | -6.49604 | -44.49616 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27382f47-bb25-33a5-9025-0546d531ddb0 | -10.35894 | -46.38577 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2294b34c-2c8f-382e-a5a3-b4d74fb3c6d4 | -5.51823 | -42.69284 | 2025-09-12 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| da91d782-0f69-3df1-9f8a-a975d6ad7737 | -11.1108 | -51.98446 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95dc717d-0750-3cc7-8e62-0c0741f10999 | -11.69375 | -46.5775 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95288e79-a0cf-3bd4-9d8b-d514b1ed7a6d | -12.08853 | -47.59253 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7a1da7d9-3603-3204-a39d-38b0549ef97b | -11.67543 | -46.58551 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3119f61e-fa2d-322d-b211-acd0f592fe95 | -10.40647 | -50.01903 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34caf70b-d07e-3415-aa7c-6907668e4fe3 | -8.6696 | -47.00535 | 2025-09-12 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae71e820-6be5-344e-aba7-48928128288c | -11.48202 | -49.2765 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e44ac7cc-8215-395b-b4f8-07e707ae0518 | -9.0401 | -47.08971 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 45eeeb61-4cdd-3680-a8da-c84676d480dd | -8.18694 | -46.10151 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 873aa093-ae50-3e64-9f3d-112d4a33ee04 | -6.88471 | -46.39328 | 2025-09-12 04:25:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c49d3f42-5961-37b8-b078-616cc00f91eb | -6.44815 | -44.0366 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0041964-05f7-391f-bc93-ce5527984cf0 | -9.71672 | -46.89113 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85a21651-24e9-353c-a170-a356491d6bbd | -11.69876 | -46.58927 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03b07971-e30f-3ecf-b31d-8a1d4f6a1f0d | -6.70899 | -42.04913 | 2025-09-12 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5efa11b1-3e88-303b-844b-a1d81832ac98 | -10.21779 | -46.24741 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c2d122c0-b68f-3f7f-9b9b-b58603751327 | -12.11306 | -44.86677 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b6b28b1-581a-32d5-824a-11f566bb5c92 | -9.03403 | -47.08517 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd4d9a18-70ed-338d-a3cc-b36cab84202b | -9.07816 | -47.04225 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02c5be6f-9a63-316e-8c4b-ec5475a7e6d6 | -7.24362 | -44.41676 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 024a3e07-add0-387a-81f5-efb7faa8df13 | -5.12173 | -47.52751 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5e6a5b2-3720-360b-84b1-ea9659a6e790 | -11.69318 | -46.55912 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbcc6397-1436-3c83-b7bc-af589e1f550e | -6.47788 | -45.15411 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd9ad5bb-b52d-3695-ba30-618ba22c1e04 | -6.81778 | -52.80322 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e875e88a-f462-387d-b15b-b38c2d52aff3 | -6.33087 | -44.63588 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 370df6ba-802d-3a6d-8bb9-eae58d6f20bd | -9.97085 | -51.7066 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7253e09e-a6e1-3cb9-966b-912ca5e8c732 | -11.40712 | -45.59448 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 318079c3-fa01-30ff-9308-fbb87a0ed1f0 | -8.42648 | -55.63274 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4efd1788-29ce-3801-a51d-afe0e606680c | -10.7116 | -48.61998 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 886117ca-0e02-3c2c-bfee-854b3914ed51 | -6.82615 | -45.64104 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f6b7aec-bb9f-39b5-a86d-8d05b54a4250 | -12.08909 | -47.58902 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5aff2f8-f2f6-33e0-b657-a502588be933 | -11.11946 | -51.98097 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07aa4892-dad4-3af0-aaa0-6fa72af4fe20 | -10.53972 | -51.53453 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 65118d61-852c-3a31-9e5f-79381c6923e4 | -11.52972 | -50.60689 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 63979eb5-af51-3eb6-9386-14d349616f60 | -9.07608 | -50.49977 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bb7155a-a460-3e7f-8b13-18e92464c843 | -6.68801 | -44.13367 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d4019d8-8061-3045-90a9-938b6eaaa56c | -9.59898 | -55.0098 | 2025-09-12 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff28a83e-f02e-3da1-a499-71b04f2680a8 | -6.65674 | -44.13715 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b64ba31-b139-30fa-8bfa-e13adfa6c7a1 | -11.6932 | -46.58106 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e560a33-cf5c-3e47-95fd-9361e6525845 | -5.65416 | -45.94741 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90b7e6f2-378e-3ef5-8e82-b97683f59b0c | -11.46373 | -49.28117 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfb6bfd9-af78-38e9-96e7-65489f2efb1d | -7.32009 | -49.62532 | 2025-09-12 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b1180bb-26aa-3d18-8609-44b73900a272 | -7.45036 | -51.81767 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6fbac8c-4e2c-34fb-bb91-2bc7645df9c3 | -10.40156 | -50.02652 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f1e771c-1b69-3c1b-b354-2535c8fb5830 | -6.44687 | -44.06771 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README77.md)
