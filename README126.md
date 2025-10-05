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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a95f18f-2090-3758-9c40-7896bc23790e | -5.11275 | -45.46512 | 2025-10-05 05:14:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26166624-d589-3484-b11a-a1e9509f1bf7 | -9.85846 | -60.27916 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c0428d-dc58-3396-9fea-f0d4fa085bee | -10.09981 | -57.78037 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eafa7365-e4cb-3b84-9f3e-7529bf8606db | -9.33538 | -54.51781 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5d602212-6cde-37b1-ad1b-2b07efe5fc2c | -6.43167 | -46.02726 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 798062e1-a12b-3caa-adcf-9d5c64e13b54 | -11.82244 | -46.8578 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b883f856-6e0a-31a8-bf90-810e5a1a528a | -10.40015 | -45.40858 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62866a2a-3900-30e2-af12-7474ee3d0abb | -11.15998 | -47.17517 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c6afef-0f97-3b90-a7fd-9ac8f480686c | -9.05588 | -47.01949 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3fc0014-8867-3067-a4d7-69bbf211180d | -8.86462 | -46.80847 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77589150-d5d4-350c-ba89-858becda29ed | -11.11859 | -47.20979 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c85f4d5-897a-353e-aa6d-ab98c5371e8d | -6.18796 | -44.60293 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81358fa3-76c8-38ca-a5b2-209abad83daa | -4.56784 | -48.60419 | 2025-10-05 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13fc9440-ec5b-3b67-8f2f-4b3c441e68c1 | -7.44111 | -46.52047 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3096bf7-9349-3514-ae3f-b6dc4382ec0b | -5.00222 | -47.2122 | 2025-10-05 05:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2eb01ef5-14e9-3dfb-b430-20dd531e4348 | -6.08436 | -46.19139 | 2025-10-05 05:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| de8dae10-c405-315f-b055-c362f4477d3f | -4.9149 | -48.02434 | 2025-10-05 05:14:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd16c93c-148a-3496-9231-298b7001c012 | -8.5779 | -46.34124 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| d49e64b0-2b65-37c8-9b10-92a31fe142ce | -10.45399 | -48.37749 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2377f8f-a7bc-3c3b-931e-eddcf89d89c2 | -6.1711 | -44.62542 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c681eb4-dae3-30d0-aeb3-04bce5e4cb11 | -9.34149 | -54.52775 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e827029-0610-3857-95ab-a7e8e33cd798 | -8.61819 | -54.967 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 307a4dc7-fa99-3e70-97dc-491c04cbd436 | -9.85217 | -60.27421 | 2025-10-05 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65984f79-a993-300f-98b6-e6205a5896f4 | -4.56272 | -48.60349 | 2025-10-05 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfed416e-6e9d-31d2-8011-f91c3a78361c | -7.85869 | -61.40257 | 2025-10-05 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e089f4af-5998-3602-8b2e-14d41cdd0f04 | -6.35904 | -43.91447 | 2025-10-05 05:14:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb8ee8e7-5051-3452-8782-7182e08486b0 | -10.46106 | -47.81527 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10a470b4-87c5-3169-b7fc-21e613a527a3 | -11.11475 | -49.86531 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c24ef33f-91d1-3bb6-aaea-6ca6b57478ad | -8.04742 | -54.89597 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bfa5888-d107-316c-93f4-ed1b1756cb6f | -6.17443 | -44.60109 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0237a8e4-c696-3946-9a01-39742ebe7d20 | -9.84962 | -52.22068 | 2025-10-05 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d341cbf-35ab-3444-9ea2-3237a8570e45 | -8.61942 | -54.95878 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e499032-0423-3af0-aa4e-20ca74fd426e | -9.04513 | -61.64022 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb6607ae-7a3d-3ad8-9107-2c7581d52058 | -11.05422 | -47.77602 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b57b14f-dd36-3847-9ab9-dada848e4ccc | -10.80362 | -48.82488 | 2025-10-05 05:14:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8e37ec6-268d-31e1-bda2-f82b0628e5b0 | -9.19132 | -59.55189 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 514ff05a-b30c-3c77-b41e-bfe1c936fa5a | -11.07206 | -47.7776 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 826bd6f8-0333-3128-a38f-818760a30724 | -11.51676 | -47.67385 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1f7f4cc-4bfe-37b4-8fc4-7a012a1a3070 | -7.45904 | -47.1835 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4dddab12-c7fb-313b-9adf-a73e90490122 | -11.12305 | -47.17045 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4033851-47a2-3b0e-9ee7-b364cabdef2d | -10.35579 | -58.45462 | 2025-10-05 05:14:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15b7daf5-bd7a-33c6-9017-cf6f35ef9040 | -9.05041 | -47.01401 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23b9a77e-1ab0-3637-9a28-68247c871917 | -11.80446 | -46.84655 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee9ba2ee-9913-3744-a85e-f54f649e2a3c | -9.73382 | -63.43269 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56bb81f5-9706-3c8d-a677-554319449eed | -8.62936 | -54.66641 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6d79a22-ebb6-3f1b-94cd-745c8b46d732 | -11.03952 | -47.79749 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d2ee63f-edad-3d6c-b9af-a41ff672ccc2 | -9.29476 | -45.99264 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4733ef3-ed07-3bdc-b0f3-3e47be1534b6 | -10.36267 | -48.28041 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 816eae0c-ca14-30f3-80e2-8ad5651272fd | -9.06066 | -47.01854 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f2fe39-0718-37cb-b434-d36748d0ab6f | -10.94147 | -47.08842 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7eee75fb-2b85-3f72-8292-aa4bd08eaa6b | -11.10765 | -47.76409 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d9039bd-86c7-3f10-8c23-b6d827dd4b05 | -8.59991 | -46.27073 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bcfc371-4c41-3f80-9789-b596582d4ce5 | -10.56954 | -48.68854 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 138bd1fe-7164-3d96-bb86-cc7541fe3d0c | -8.5365 | -46.31573 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09663f5f-45df-3453-8b27-6b53e54fb56a | -11.12539 | -47.91204 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af03c25e-f63c-3b1a-a8aa-ed07792f85bb | -9.56869 | -46.12054 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a88cc4a5-f7bc-3e5b-bd28-276931a656ae | -11.89608 | -44.98798 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25aa5505-1b68-351a-90ef-bb648252f0aa | -7.45849 | -47.18764 | 2025-10-05 05:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa2bf355-cb8d-3538-a980-e9f3d21acb9c | -11.06406 | -47.77653 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d1d4680-ab83-3db6-a2de-ab7baade2fac | -6.18461 | -44.6272 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1538112e-4e96-33e6-a161-2517643f515c | -6.08512 | -46.19191 | 2025-10-05 05:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7371e30c-8a3f-3088-8128-69b17eafd2a0 | -11.81902 | -46.86142 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bdd17145-6b84-383a-a1b9-595dcb515f53 | -5.76986 | -43.9822 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6862e6a8-a4aa-3fc8-985f-e12470ece65e | -9.54718 | -54.59525 | 2025-10-05 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71f584f5-6c11-3ff2-b4d1-a20f1fa131d9 | -9.3287 | -62.17834 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b645adbc-e5bf-3076-a365-0cec969fe4eb | -11.07182 | -47.9113 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e19749a-657a-3047-9bc5-e3bc01ffe7d9 | -9.29096 | -46.02199 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 782cfc94-2ecd-3c4e-b8f4-409c6dd6105a | -9.32861 | -54.51226 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85c81c35-8394-331b-9665-7b19f5518dee | -9.31063 | -45.66094 | 2025-10-05 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e313fb5-d895-36db-add8-ffca76b16ed4 | -11.77702 | -47.94577 | 2025-10-05 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eebf3d9-a22f-34c5-b950-c2b0092657b5 | -9.33778 | -54.52722 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88158c3b-b4d2-319d-a462-e91bb5af1a48 | -11.01875 | -46.69657 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 323a671a-246c-316c-ae71-d94aea9c4211 | -11.83035 | -45.09768 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78d8c004-e72c-3c31-a5e0-74f3cb629419 | -8.60693 | -46.28622 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b89ee2df-fae4-30d3-ab6c-7169434d1db6 | -9.3018 | -45.98903 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3e6527c-422e-3696-a6de-4bd1e89ca498 | -9.45702 | -56.65536 | 2025-10-05 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3991c5c-c163-38d1-9799-e340f1555e74 | -10.46432 | -57.48964 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77cfe690-8e0a-3cc8-b10d-ee7851c032ac | -9.04253 | -47.01598 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 287298cd-613d-3323-b15f-5ef6f430f9f4 | -10.04754 | -49.20283 | 2025-10-05 05:14:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9df9e90e-5193-36ac-a8a9-758794a6d277 | -10.40248 | -51.58758 | 2025-10-05 05:14:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78f2493e-050b-30ab-b320-1d4e3f0a879c | -5.76898 | -43.98844 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 05791f75-4b19-3c2c-b2f6-7a0077b0a65a | -9.37082 | -62.2909 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d590e16-bd92-383b-9a0e-11edf81ec62e | -8.60291 | -46.26701 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad7a5b70-4576-3145-a071-4fda80ee0e5d | -7.02324 | -50.73903 | 2025-10-05 05:14:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| de624277-7107-3a10-a48c-fb278fe914d0 | -10.94287 | -47.07045 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 699f7fd2-70c9-3ff6-aa76-b3338ad4b6ac | -9.33908 | -54.51838 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52f35e99-abc2-333b-bceb-71f86c377bbc | -10.95022 | -47.06131 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f492f0fd-ba08-315f-a3d3-ed53bde9f2e2 | -8.17054 | -55.07424 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e7ab1a9-517f-369e-83c4-35eda2067ce8 | -6.17614 | -44.58864 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d371d6f-1ddd-344d-885d-5498d4c1ebb0 | -6.1567 | -44.57949 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4473174-f39c-303b-86ce-2edf7cb4def4 | -9.31425 | -54.53281 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c3a54be-8058-392e-9231-ff3e7569f2b4 | -10.35872 | -48.15664 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6ffa583-a9c2-3964-a717-2133c5a83092 | -13.24748 | -48.47993 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86f77f8f-3547-3507-8aa4-b03f19757304 | -17.88448 | -57.64157 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| aee65ee7-c279-334e-b6af-4fd8bd80356f | -12.4538 | -44.63881 | 2025-10-05 05:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e5cc4f9-0fbf-3173-9b24-e1b87c131f05 | -13.72902 | -47.95949 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecf6dcc8-2f4e-3103-b5bb-5af883606560 | -15.2877 | -47.33533 | 2025-10-05 05:16:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a15d65dd-1a97-3abb-a8c0-285438544523 | -13.30751 | -47.63009 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 615b7686-c073-3217-9a7f-841e124eab47 | -14.66979 | -48.35698 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3525c616-81f7-3b3c-87e3-c89693805c3a | -13.3594 | -48.05995 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README127.md)
