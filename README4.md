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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 778fe7a4-0c18-36f3-9f07-92775bedb0e0 | -5.91059 | -45.54387 | 2026-06-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 171bec99-8c34-3417-8511-83d62456229d | -7.40372 | -39.76588 | 2026-06-03 04:25:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a5aeae8-b0cf-394a-a1d6-031d4137a412 | -4.63538 | -43.04994 | 2026-06-03 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 105ed4eb-46b5-3c06-a543-e4835a77bf9c | -6.7583 | -45.0085 | 2026-06-03 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bd0c269-aea2-3428-ba0a-06a6e67c0298 | -11.57727 | -56.33561 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b93a26b1-2e7b-3fce-bf3b-5fb2b2e4cfb3 | -11.6315 | -55.18525 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbc29f36-2955-39d7-9c01-b1e17409a5f3 | -8.08605 | -49.08502 | 2026-06-03 04:27:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df9250de-6f56-342b-a0f8-7fa0d5c3d0e7 | -9.50587 | -46.1357 | 2026-06-03 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78e75b1d-e12a-3f12-9c6a-f1e29d72c7b0 | -10.56052 | -46.63926 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cac2c65-0fa8-3ae0-ac60-4ad4b564a1c8 | -10.54892 | -46.62669 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c38f5195-ad03-3b51-942e-c958e8a386ef | -11.79911 | -47.33985 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87ca7af6-7787-3395-b511-a906fe92c497 | -7.35111 | -46.21236 | 2026-06-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ee29976-664f-39ab-b0b6-164a1d6983c1 | -7.95496 | -46.83647 | 2026-06-03 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e816e998-6aba-3d6c-8cd0-a6801a200394 | -9.18369 | -58.06063 | 2026-06-03 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6275c539-b14f-3894-9147-d36e4bca4e81 | -8.75853 | -39.82935 | 2026-06-03 04:27:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14dd1fd2-7094-3de1-8ab8-d70cc9a77d4e | -11.57545 | -56.34516 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f708f8c6-a68a-356a-bb42-9d893b2981bb | -11.32202 | -51.38911 | 2026-06-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbc26f72-f29b-3a56-baac-b4ae5e0f8c4a | -14.05034 | -46.35006 | 2026-06-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9d00236-927e-3443-87ed-b56c3decfaf7 | -11.9947 | -43.78598 | 2026-06-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a752a820-d5e9-306b-8b7a-0a967804e7a8 | -11.7969 | -47.33232 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c3d60202-14a3-30d8-89c3-1195b4db8f61 | -11.56578 | -54.5795 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7fff5f6-7086-379e-8a1d-a0e311934eee | -8.05087 | -46.19542 | 2026-06-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e991159f-e70f-3d22-b9e9-4a070698656b | -10.61071 | -46.69068 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32dbe25f-1eb2-327f-9108-20fde361eb86 | -11.79426 | -42.63981 | 2026-06-03 04:27:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b807efb2-570b-3fc3-b19e-bea79cdf2ade | -8.23387 | -47.09389 | 2026-06-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cc10969-a0d0-3b2f-a902-517bc6c30a39 | -11.79966 | -47.33635 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0636dee1-0a38-3a1a-89c9-1924099d0ec6 | -8.87617 | -48.4986 | 2026-06-03 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 734fd48b-4467-335c-9dbc-6bc33d3f1834 | -11.79497 | -42.63472 | 2026-06-03 04:27:00 | NOAA-21 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7106317a-5622-3de3-9649-c3b9793e3e6b | -10.57366 | -57.32047 | 2026-06-03 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e687e17a-0330-3d36-a7f0-3fc70f934a6a | -11.62865 | -55.17371 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c8edfdc-e86d-3ba6-a206-9a104560ced9 | -10.97874 | -49.42836 | 2026-06-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07b0a70a-1a1d-3542-9d70-23cfa425b65f | -9.98342 | -51.0223 | 2026-06-03 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b272583-5743-352b-9b4a-14a8bce98b52 | -10.90917 | -47.06758 | 2026-06-03 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcebd88f-55e2-3a3b-ae7b-2fcb385c7dce | -12.40264 | -46.51033 | 2026-06-03 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77a63539-a134-3b75-9514-081654383b45 | -7.27147 | -46.80842 | 2026-06-03 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36e5e8cb-102a-35d0-a109-aa5238c48c2c | -11.57026 | -56.34416 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc857698-c98c-3729-918c-59b0b829b0f5 | -9.18455 | -58.05614 | 2026-06-03 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e6757b6-1268-3298-9cf6-9f1484d1a148 | -11.57606 | -56.34197 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25b96118-e4da-3760-931b-b95c0575abf4 | -10.57219 | -57.32826 | 2026-06-03 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 684f4c6d-be90-39f3-b3c0-bb743c030aaa | -8.57405 | -46.00385 | 2026-06-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c956e13-477d-322c-88aa-26c389095c56 | -11.63344 | -55.17463 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 806f3755-c987-3a57-8de3-cf05bedf87e8 | -11.63248 | -55.1799 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3fe2f45c-44bb-3a5e-b6aa-01065f76f246 | -8.57513 | -45.99685 | 2026-06-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73c52606-5b6a-3bb4-91e0-530a68c2529f | -9.79945 | -48.9215 | 2026-06-03 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2584d73-4697-3bdc-b5c7-ad6f234acd6c | -11.60684 | -49.32766 | 2026-06-03 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71f4f125-3c4e-386b-a81d-0894e0bb831c | -11.9494 | -43.40778 | 2026-06-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20d6d72c-b2e1-3ca8-bc8d-552337ea1812 | -13.39656 | -47.38882 | 2026-06-03 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c090d5d6-16ca-3074-9867-65b3d5084a2d | -10.54561 | -46.62617 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a66f16ce-30b3-3b82-9b85-fb38b4124bca | -8.23968 | -47.10268 | 2026-06-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c421f04-521a-33a3-bb4e-b795b65c6ed0 | -9.08849 | -48.64606 | 2026-06-03 04:27:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce09f29f-f9f2-30d0-9317-b3a3a592cf86 | -11.75795 | -47.07806 | 2026-06-03 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d22d6c5c-8937-3cb4-8c95-03b16bda71e9 | -9.1785 | -58.05508 | 2026-06-03 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff1193c9-4256-341a-b115-7b4d412bb55d | -7.59473 | -46.46331 | 2026-06-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90bf647b-824a-3302-8764-a2aaefb85797 | -11.99395 | -43.78436 | 2026-06-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b76f7fc-4a39-3aa7-9047-4ecb1839ec7f | -8.23608 | -47.10135 | 2026-06-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83333b3f-9747-34d5-ba67-49dbbf9eb39c | -10.21373 | -48.26324 | 2026-06-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3122054c-4efa-3d16-bbe7-70eebb8a8804 | -13.39602 | -47.39236 | 2026-06-03 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 191ccaf7-8244-3009-ad89-a01c6ec65402 | -9.88682 | -52.4403 | 2026-06-03 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 574c9a6c-007b-3bc5-98a2-6ece8574d30a | -11.6267 | -55.18435 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 875dee10-ac25-3ce9-8710-32a07a943049 | -11.80296 | -47.33688 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 751287a8-0491-31db-9b41-a55f2a82209e | -11.85548 | -46.64294 | 2026-06-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6f2ea2d-04c6-3e25-a4e5-f8a82e9810a9 | -9.18368 | -58.05289 | 2026-06-03 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7ad7632d-e47c-32e5-8a38-74eb1ad21ab3 | -12.81026 | -54.86022 | 2026-06-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dd52a7d-3a7f-37ea-9f20-e08391f0071a | -10.53846 | -46.62862 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9068a4cc-a344-3dc3-8022-52902afbd400 | -8.57459 | -46.00035 | 2026-06-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9b704bb-c079-3598-871a-9e843d175986 | -8.05534 | -46.19308 | 2026-06-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62cfaf15-9a9e-3667-809d-0ffc6f9361e5 | -12.80595 | -54.86187 | 2026-06-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d30033e-1572-338b-8fd5-40731b8afdf6 | -11.32501 | -51.39446 | 2026-06-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ba93a30-5fa2-3218-abab-fea8754f08e5 | -10.81271 | -56.59475 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7924331c-ebd0-34bf-bb91-f2f1b740ab7a | -12.7368 | -46.97151 | 2026-06-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98cc8568-023b-3869-a3ce-8c256146bd02 | -11.6219 | -55.18344 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2003fa1-2faa-35c6-9d59-fb1d2b003eff | -11.20834 | -54.98766 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f61de9c8-cf46-3d68-a35a-daa4e64a8f2f | -11.13817 | -45.14903 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e181c93b-d5ad-3a1f-925c-7ee8584b67d8 | -11.95004 | -43.40313 | 2026-06-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 608cdcba-a1b6-313f-91a9-3bb0901d06cb | -11.13531 | -45.14471 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4714a572-650f-3923-9b0c-312025d2f02c | -8.06026 | -46.18324 | 2026-06-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 067944f3-81eb-35c4-b0df-6c1c8abe2912 | -8.05972 | -46.18669 | 2026-06-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d9f0982-4711-3855-b374-194e7d5cbda7 | -11.79636 | -47.33582 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5a2034b4-790d-319d-92bb-76bc0dd92d94 | -11.43779 | -54.0918 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb74d63b-3671-3d2c-b886-d7ec9ee58865 | -10.22144 | -48.12859 | 2026-06-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c35c4bcd-961e-32d3-b293-5ed4fdd49fc3 | -10.55553 | -46.62773 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60cb5253-d33c-36f6-bfcb-60b4a6f15910 | -10.56731 | -57.32322 | 2026-06-03 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f493f19-cd52-332a-a8f7-d907b5462c74 | -13.95899 | -46.18765 | 2026-06-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5d57dc8-6001-33a9-b45b-1f83d94bf9b3 | -8.5779 | -46.00086 | 2026-06-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce780d78-ed59-3e4e-9597-b98303b85bc9 | -11.95316 | -43.4084 | 2026-06-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12a55d1d-f807-35fb-93fc-75219c604169 | -9.14307 | -46.91942 | 2026-06-03 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc25d261-d403-33ab-a1b2-018f5ed6b4c2 | -10.98219 | -49.42893 | 2026-06-03 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ada1a34-3b9c-331f-b6ad-807dcd9d8c93 | -10.2143 | -48.25962 | 2026-06-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b04dff3-459c-3158-ac67-0c43f9da40e0 | -8.08954 | -49.08558 | 2026-06-03 04:27:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c308afe-27d1-3a14-bacd-b69bc4970971 | -11.5721 | -56.33456 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e025184c-64aa-33ef-b603-461d145b470c | -10.98429 | -45.09887 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf2a8d62-7700-32d2-876d-e088c54a09eb | -11.08177 | -48.26231 | 2026-06-03 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa00676-1ca7-3f9d-b770-0de2df432a80 | -12.737 | -54.20752 | 2026-06-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 449c99bb-56e6-3ea6-a26a-fb409c5ac197 | -13.20051 | -43.35852 | 2026-06-03 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59d2307c-af16-373d-9e50-daa39a5bfad6 | -12.73349 | -46.97097 | 2026-06-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e5f6493-ba00-33f3-927f-a79c8a8ebf25 | -11.75849 | -47.07455 | 2026-06-03 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 69fd27c4-6df1-34db-8dfe-f88c67feaa44 | -7.50727 | -55.00614 | 2026-06-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc5339c1-5b21-325d-887c-30416900a204 | -12.80936 | -54.86502 | 2026-06-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c97503a6-b3f2-34ca-923d-3bcd0627325c | -10.18713 | -49.5839 | 2026-06-03 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26c3d4a9-3b6f-3e15-b1a9-c453a70527a2 | -11.26725 | -48.35828 | 2026-06-03 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README5.md)
