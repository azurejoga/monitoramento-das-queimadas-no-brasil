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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd0c0745-d8d9-3d27-a431-bf2a328bbaea | -3.10564 | -53.77659 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 959145ec-e7f5-36e4-ab1b-f549153862ed | -2.94626 | -54.11834 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a8d577e-1dda-3b13-b893-4185363ff66c | -11.65195 | -43.69018 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03b2fe21-5afa-323c-b2c8-7e01e1752495 | -2.99854 | -54.76248 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e5bf1a6-09df-3844-9041-2388eb5a1335 | -3.26145 | -54.02055 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54dcf134-e3bc-36cf-a39c-b2c4412180b5 | -3.6019 | -54.59068 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 525fa507-a6a4-3fb2-a027-e844500024ba | -11.45634 | -43.38026 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49dc13c8-c072-30ec-b348-7414d35f7394 | -6.8843 | -45.91032 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 95b10350-a400-3e69-ae8c-2f5b36190a97 | -7.41716 | -44.76248 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52fd76f7-3f62-3a72-a947-273b741831fc | -11.20376 | -49.41678 | 2026-10-09 05:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73540110-d0f0-3178-99a5-3567350f6e13 | -5.86922 | -57.75633 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 675178b5-5769-3ee5-bf0f-7f6172cb848b | -5.26174 | -50.14617 | 2026-10-09 05:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d94cd6ad-0b70-35e7-9815-38743d27337b | -6.11935 | -51.95975 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbce1ff0-bece-3673-a507-37e0df76c769 | -2.98871 | -54.14494 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66fba979-7f84-3908-9b4d-0d327cac33f3 | -4.80471 | -54.67389 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c739348-00b3-3aae-9c01-8d33917089a4 | -3.0797 | -54.29722 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e5fe3b0-9df2-3e5f-9069-02f2ff997cbb | -2.99171 | -53.90202 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38f47b11-3190-3cea-a6d1-cf8a611e155a | -3.60061 | -61.63696 | 2026-10-09 05:04:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a63f8ebe-0bc7-3cb8-ba2d-150c10d97e0f | -3.54012 | -54.68912 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14c78f60-af33-3ce7-aa2e-ad369dcd59cb | -3.0178 | -54.1883 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d65d7b18-ccfa-3cfe-a1fc-7d01dea9b108 | -3.78081 | -58.58477 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c7e9cf20-5a49-3c90-bd76-da29b0de103b | -6.22037 | -55.66936 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b33ee000-ffc8-346c-94cc-fd9a56527ed1 | -3.74703 | -49.38516 | 2026-10-09 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e888d737-29cd-3067-b1b6-cddd78857f1c | -3.16375 | -54.73577 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae0aa48f-e650-362c-a304-33c13b7a7539 | -3.90574 | -55.90057 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27c36023-544d-318b-a8d4-f8fd4ee6c1c0 | -6.93237 | -43.66405 | 2026-10-09 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0420a1f6-a3a3-39d3-9e50-73a63eaf2d6f | -3.10954 | -54.15855 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00ea1df9-4a30-38e0-ac46-c881be0a5011 | -4.22322 | -59.54979 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d8ed943-2d85-3c1d-b2ea-97822594d638 | -6.96334 | -45.28263 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3bf300ae-16a6-365a-b15f-a67311718ad5 | -10.45884 | -47.85632 | 2026-10-09 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 468bf967-fa82-320c-bba8-cc02fcb81d2e | -6.00716 | -53.49497 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f856065-a3f5-344e-93ec-3bfa7d6841ac | -5.95253 | -40.93584 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 046e575d-4dee-3880-9ca9-a9649c787183 | -4.37839 | -55.16103 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 020789c2-477c-37ed-b83d-f63792f13973 | -11.40958 | -46.6802 | 2026-10-09 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc9451ef-170f-30b4-9d75-a1bc7e9e9956 | -3.6002 | -54.66844 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 254760f5-0eb0-3ce0-bc5f-d9bd7e20a7c7 | -3.65598 | -54.52615 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eab4915b-60ef-3131-b990-17a31a9022b8 | -5.70296 | -53.48256 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e1f1419-9393-35b9-a7d4-f0f2268ee004 | -6.50713 | -55.31404 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd24f796-6a7c-35cd-9335-159cdb319f45 | -2.56643 | -56.17392 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b36d311-cd19-3bb4-bc90-7c35efd49e47 | -3.32331 | -61.27232 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e002d088-a5d0-3031-bd6c-28856dc5936c | -11.06902 | -44.0876 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e9d204e-0a8a-34b7-a0b4-8020158ffaa3 | -6.51026 | -55.40585 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9cdef06-18e6-3ac0-9c5a-f5f0a55fbaa1 | -3.92936 | -54.57585 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 723bc5f5-4ddf-3eeb-a2f3-350fa3d4401f | -3.81948 | -51.99874 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9839c06c-1226-3cb5-b98e-eacf2aeb1edb | -3.09457 | -59.19064 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50bd3736-e946-3d19-bab2-2d5e7abfa410 | -6.41129 | -55.19615 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f719c696-8315-3a01-b3cb-7588d5fec4ca | -3.21041 | -53.8658 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75a5ebf1-2071-304c-9f71-6c56290db8b6 | -6.00051 | -40.9578 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 559157c6-051b-3e18-8bff-88410d3ae203 | -3.00713 | -54.76246 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22e54c26-12b9-3032-99d1-23aba87696eb | -11.41989 | -47.58419 | 2026-10-09 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0a84edc-5397-3371-9869-84f2cdb110a8 | -5.92974 | -51.83365 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c43e832-33e6-36f6-bdda-ebd1da94c05a | -5.97083 | -55.35127 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4768c7d8-d53b-3f2f-ae87-43cb8edda7d2 | -2.52222 | -56.61295 | 2026-10-09 05:04:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3da305d-75c7-3cba-809f-a0bb0a0f57c6 | -3.47149 | -60.25033 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94852d3d-12ac-3310-9ff2-38dc4797a0bf | -11.64671 | -46.78491 | 2026-10-09 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94351d85-1401-39ab-a08a-6f895686ccba | -6.22601 | -52.88894 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85565f2-72dd-3f1d-812e-45df012dfe75 | -2.97878 | -54.07214 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17a2d978-8fba-309f-ae65-268ac6549d24 | -3.30952 | -54.03214 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 521a3947-8fbc-3523-9d5f-ec8b157351cc | -2.8811 | -54.18746 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 808cfa05-b78a-3c14-a4fb-b192b133c660 | -2.82335 | -57.6207 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0270d9c5-6639-3b53-b81c-644530cc58dc | -5.34651 | -45.17782 | 2026-10-09 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 725b6b37-b483-3b15-86a8-8c385ae35adb | -6.68811 | -41.75962 | 2026-10-09 05:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 36a947ed-81b3-3d58-9089-0fce6d7bc432 | -2.87042 | -54.16209 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa2d61c-092c-3f28-87c9-342e15951382 | -3.1716 | -54.73278 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f026030e-b0e6-3813-80be-4b86bd53d049 | -3.42669 | -54.06662 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1116cb09-536a-3ac7-a6fc-41b73221e518 | -4.73954 | -54.60736 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e163ece-0a45-3566-9f1c-4cb2194a4246 | -7.18308 | -52.60992 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26123344-f68d-3ec2-90e8-e9ad14aab6c3 | -7.90891 | -54.71811 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f20c8a32-3e02-387f-ad3f-eb71d4f51b40 | -2.49316 | -58.07272 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3012eb22-6210-329e-b41d-de8142d8b6f1 | -3.3239 | -61.26878 | 2026-10-09 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c2028e9-955e-3c9b-84e0-aab826a08543 | -3.59889 | -54.67646 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af6fbdf3-acaf-321a-8efb-d787e239ee4d | -4.56768 | -54.95875 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc3f3989-8a82-3330-a17d-c4a85b8519f9 | -7.44865 | -63.55694 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 038b7f4e-830e-3717-8021-b81f904d0e6c | -6.10681 | -53.50716 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1aa9c22-1847-353b-90e6-af0d31f0431a | -4.295 | -54.80983 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1223c177-ba1d-3208-aa70-8df3b17af8cc | -4.57834 | -55.72556 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c325017c-919e-390f-b179-275561d115af | -3.29927 | -54.00709 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd46cf1d-4782-33eb-b3b8-de76d831e0a4 | -3.25201 | -54.03473 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 059d1253-8f1d-3550-9d1a-6ce8b3e68041 | -6.36034 | -55.15625 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b7a7a7a-93ab-36ed-af6d-e701e10eb885 | -3.1259 | -53.76058 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a008e8fe-6c66-39f3-9976-5d0acac064f8 | -3.06199 | -54.15961 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d5bc9eeb-b495-382d-8f05-c90020e9a6e2 | -7.53184 | -45.87609 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5378930b-8732-35af-a0b7-c5de45bc3292 | -4.12953 | -46.86917 | 2026-10-09 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77cf8ecb-2d43-3901-944a-e661971e206e | -3.31239 | -54.0365 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d97ee4f2-70ec-31eb-828d-995575d9bf25 | -3.01274 | -54.75081 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0925982-e7a1-3bc5-b6f7-00a09da5b919 | -3.89953 | -55.88795 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f6f9d1e-e344-373f-917b-933b5deb8f8f | -6.48943 | -55.96497 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac975972-1b5a-3d25-9a11-2d6feb5c569c | -3.00718 | -54.14296 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae2c11f9-9b36-3e78-8621-84be990bfcb7 | -2.98166 | -54.07655 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adcdae25-5611-303f-8d22-4ef6ad86950b | -4.07664 | -59.8403 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00f490e0-9071-3187-85b9-f81a5e3f95d7 | -3.10729 | -53.78836 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a74ed5ba-beeb-3847-a70e-24354460c34a | -4.13029 | -54.42548 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e5862d-a36b-3de4-acb8-0840f4adb777 | -3.73997 | -59.45869 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8c24afed-0862-3682-8fd2-915d60146a6d | -6.25704 | -52.85793 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a714f8ac-b3bc-343d-b674-77db50806391 | -6.12316 | -55.6939 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f3ff157-f918-3261-bbb1-e745e43eadd9 | -3.53329 | -54.66319 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e219ac9f-2f78-30d2-8494-2b2e01c31006 | -6.49223 | -55.94773 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2ce6c1c-9516-300f-8c94-30f835511768 | -7.58276 | -45.64896 | 2026-10-09 05:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9508fbce-3ee0-34f8-b375-17db05064414 | -11.76877 | -44.95253 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e18c22ea-3903-3cca-8b71-f7338fefe674 | -3.20558 | -58.00326 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README164.md)
