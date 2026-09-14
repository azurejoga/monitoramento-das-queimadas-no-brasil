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
| e802b3bd-dd71-3e13-a78b-4046c85a085d | -5.2885 | -45.2518 | 2026-09-14 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 8ae0dcc2-4a18-3d95-908c-2d1a084df02b | -6.1111 | -57.6645 | 2026-09-14 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| eced15da-b2e1-3548-911e-dcfc147c03c0 | -4.1333 | -60.6882 | 2026-09-14 00:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| a7809910-2d3e-3407-9b1c-f3fbcdce2fb0 | -6.5837 | -58.8498 | 2026-09-14 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 3077254c-2cf7-3524-96a2-5c99914003fe | -3.1816 | -61.1235 | 2026-09-14 00:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 7266fc70-d33e-33bd-a866-f2af0c1a40a0 | -6.2916 | -55.2895 | 2026-09-14 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| eff77d4f-fd3b-33d2-b921-149b3ab5f60d | -6.3197 | -59.9764 | 2026-09-14 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 66285e52-338f-37ee-b363-d276eeef57b0 | -9.4325 | -50.1299 | 2026-09-14 00:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1ab68b4e-3ec8-3085-a30e-baf1de2749b9 | -6.3015 | -59.9387 | 2026-09-14 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| da2cb053-29c2-38ff-b109-41ba1d8818a1 | -6.1109 | -57.684 | 2026-09-14 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 23c0c76b-612f-3189-abda-6d414174daea | -16.9712 | -49.72547 | 2026-09-14 00:39:00 | TERRA_M-M | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| b0633a9a-5039-3fcb-b3af-1cfc296c5f20 | -15.55593 | -48.79092 | 2026-09-14 00:39:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| fc833753-2ffb-327b-9ffa-f0c94794350a | -13.55792 | -49.8974 | 2026-09-14 00:39:00 | TERRA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4732fe5b-2b83-39dc-a814-e26dfe73dac2 | -15.5512 | -48.7841 | 2026-09-14 00:39:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| c0ca2e93-3fe1-3595-9bb0-ca679b46a442 | -16.96686 | -49.73272 | 2026-09-14 00:39:00 | TERRA_M-M | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1ea23e80-93a1-3056-b93d-fe945cc71a13 | -13.56287 | -49.92562 | 2026-09-14 00:39:00 | TERRA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d26f0eb0-8d02-3967-8a46-451c40c7480b | -5.2883 | -45.2744 | 2026-09-14 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b415d489-1715-3f7b-9082-e5c5267cc8cb | -6.3015 | -59.9387 | 2026-09-14 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 02a70229-8beb-3883-9743-9c1338189fe7 | -10.433 | -48.6474 | 2026-09-14 00:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 7482cf9a-d236-3b07-a904-9bafd8a2744d | -5.2885 | -45.2518 | 2026-09-14 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 63d9a6a2-b9a4-3ee4-8aeb-57a10a2b667d | -6.3014 | -59.9579 | 2026-09-14 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f70d6c87-57b4-340c-96d7-0da53a6fc18f | -14.1861 | -47.3844 | 2026-09-14 00:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 3d8cb910-a920-35df-a434-a12b8f27e6ce | -4.1333 | -60.6882 | 2026-09-14 00:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 4f92d3b5-64ed-3024-aa10-11c5e10a10dd | -6.1109 | -57.684 | 2026-09-14 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 38de878a-de9c-3500-ad51-e682a12e87ea | -6.5837 | -58.8498 | 2026-09-14 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 51f63284-1cc5-338e-84fe-6329f78e16ec | -6.1111 | -57.6645 | 2026-09-14 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ca2ce3c6-ee5e-3c64-813d-2d8bb12bddd3 | -6.0925 | -57.6847 | 2026-09-14 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| be42eb1e-0437-34e4-ba2e-9143de46056c | -4.8562 | -48.3667 | 2026-09-14 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 6c5d1216-3159-3cb9-bf5e-d08c11471008 | -4.115 | -60.6886 | 2026-09-14 00:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9bfca1a6-9c59-3628-8c1e-767db5b3f3e3 | -3.4089 | -58.2142 | 2026-09-14 00:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4decbc86-3b2e-3607-a341-f47a052deb03 | -5.1255 | -55.955 | 2026-09-14 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 12cb1481-5fee-36d7-bac0-f4d63638f951 | -6.2831 | -59.9394 | 2026-09-14 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 4f17af8c-c5e4-3f2b-a80b-69ab682db930 | -6.2917 | -55.2695 | 2026-09-14 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fdee0626-d496-34c0-8747-57ad571cdb8d | -4.1334 | -60.6692 | 2026-09-14 00:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| feb2faa6-0eb4-3255-8dea-27c2b32fa009 | -9.4325 | -50.1299 | 2026-09-14 00:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d539f4f5-947a-3e52-8cc1-a21910f4c024 | -6.8446 | -55.5611 | 2026-09-14 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b2bbb3ae-d9ca-36c1-afe8-411844951719 | -6.74233 | -59.44009 | 2026-09-14 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b7e4897a-a5e9-32f9-ab1f-2a8f9b1cb3aa | -6.50774 | -58.28699 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 093c8b11-2435-30d7-bc46-5b834d55e716 | -6.68209 | -58.87564 | 2026-09-14 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32fc1107-6124-3b4f-bc79-74da7f1091a9 | -9.22522 | -56.57658 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 36579b89-ee59-3df2-9a77-12c8dbfafe02 | -6.32103 | -59.98822 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 7be8b1d1-8d4f-3f6b-b302-d68c40bcb4f3 | -6.31983 | -59.97943 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 0c737dcc-cafe-3420-95ae-81f5f71d81e4 | -6.37151 | -58.30278 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2d860609-61d4-33ca-b103-a2e81f83a2c5 | -6.5773 | -58.85087 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 46ba393a-7823-3f24-9e7f-fe938adfe4ba | -6.10251 | -55.668 | 2026-09-14 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| cc8af997-9574-3800-a156-bdf6dc88ae95 | -6.29872 | -55.27739 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| e1f698f4-64e8-3993-b1bf-6dd41e4ad08a | -6.30089 | -55.29185 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 870afd1e-a814-3dd4-b4f8-7693ef932657 | -10.68058 | -54.17334 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| e6ebeaa7-3a55-3f7f-8a7d-6e3422840197 | -6.32224 | -59.99702 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b836ae2d-852d-3ee5-bdec-91498a410960 | -6.11677 | -57.67603 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a75df16f-8915-3544-8d70-a03d71c48681 | -6.28687 | -55.28626 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 6638313f-4dc6-34e7-aadb-e00bab0843a3 | -6.10739 | -57.67744 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 14d1b159-7945-3598-8ff0-b185814022b5 | -10.6737 | -54.12866 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b3960015-ab5e-31c0-8715-a453aef28e59 | -5.81183 | -53.80531 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 7760d4b7-6478-3ac4-b0d5-59cc8de7074a | -9.69205 | -58.17657 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 40948319-edd5-36b9-8e58-c7c935c23b52 | -6.37606 | -55.26577 | 2026-09-14 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ba889002-9d01-3db4-b549-9e04db425cad | -6.69041 | -59.13068 | 2026-09-14 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1b9a758d-6e8b-33cf-988d-7ce74ead091f | -9.13738 | -51.57566 | 2026-09-14 00:41:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 328fcb64-3244-39ae-ad2a-a4ec45a1df66 | -6.07001 | -57.86279 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 60e1156f-ff06-334b-a549-279b853b10a0 | -6.14004 | -59.88249 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 444b0139-3257-3fbe-93db-14a22ea6d750 | -9.68767 | -54.84373 | 2026-09-14 00:41:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| bd4bccbe-df8f-378f-92bf-027d7ecbdedb | -6.28477 | -55.27161 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 339bbb39-6cfd-3ffb-bd85-3d6ac98b6406 | -9.44013 | -50.14839 | 2026-09-14 00:41:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5df38270-45d4-329e-adfa-ddaf03f8d8b3 | -6.64782 | -58.82522 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 37efc739-4038-3561-9ac0-38825fcd1eaf | -6.74111 | -59.43125 | 2026-09-14 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| e8493509-a35f-3d56-a5c3-0baf949668e6 | -6.58621 | -58.84959 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6518feef-8e0c-3d26-95e0-bacb593376c6 | -6.59762 | -58.86639 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 55d78ae4-0f03-3188-b4b7-45c758ecbbfa | -12.13364 | -57.18576 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 78a1180b-b5e5-33ae-a2e9-4b73bb14ebd7 | -6.85839 | -55.57317 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 7fcf10f6-f658-3158-9dc0-85c7e3b0dccf | -6.13125 | -59.88373 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 80603a39-9c4a-388e-a838-fc05ee27196a | -6.56822 | -58.98088 | 2026-09-14 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd714c3c-23e6-34fb-a56a-d862f005d5e9 | -6.10884 | -57.68754 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db73f2da-d67d-36fd-b649-c89a558ce900 | -6.58746 | -58.85863 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 3eba4622-5ce7-374b-891f-59fbfb96298c | -8.53872 | -54.70619 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 0bc751c2-486b-3a98-b626-2c1f51f42e53 | -9.40829 | -50.18161 | 2026-09-14 00:41:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 5bf00edd-fe17-3767-9f3b-1d3022d76f5d | -6.32466 | -60.01461 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| c996bab0-462e-3a17-93a4-f34850d07094 | -12.12595 | -57.19661 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f52eb824-f94b-3dbc-8fae-fd6b44ceef6f | -10.67599 | -54.14352 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 9d9a1a1c-f2db-3240-8fb9-77130b46a631 | -6.74991 | -59.43 | 2026-09-14 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23bf658e-782e-3f49-ba82-31a6d8d3ca4b | -10.66254 | -54.13061 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 74890511-325c-3920-9d5a-00e713ff943b | -10.65134 | -54.13238 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 81d3c0e5-f830-36c0-9b33-0b02b297ca09 | -6.6389 | -58.82649 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01cc365a-9f1d-3ea8-a587-a07d65bce6e0 | -6.30862 | -59.96308 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 50e80067-6e5b-3b7a-a5e5-d4ff17ae019d | -6.31741 | -59.96184 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1cd5eafd-076e-3661-9005-594a555f7b97 | -6.31189 | -55.28998 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 751155ca-70a2-3c44-a182-b6904587a477 | -9.70097 | -58.17527 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab0aea52-3ce1-378d-b3cf-f7f5ea718b9f | -6.30741 | -59.95429 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2f95a776-988e-37c6-bc21-549a5015dc82 | -6.27453 | -59.92892 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f5635cc2-2c33-3558-bc23-7d2766728604 | -13.39394 | -57.03392 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 32bd7bee-23d4-3a61-9d4c-d211e56fd3c2 | -10.25976 | -57.69189 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a8a4be7-3397-33f8-8166-6e671061ec2e | -9.13372 | -51.58141 | 2026-09-14 00:41:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c15c823a-140b-384f-abcb-1127452921d7 | -8.11534 | -54.80225 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6c1eade7-3189-3567-b4d9-54442e0a9a17 | -10.66714 | -54.16033 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1036.2 |
| bd147213-fe3f-3bfa-8fcb-1595df0f5b18 | -6.10594 | -57.66732 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| ba122bf5-f692-369c-8d40-7cc43b7b6a0b | -9.70791 | -54.36658 | 2026-09-14 00:41:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fc55f936-d131-33e0-b4b9-f1b78a6ff4c0 | -6.57604 | -58.84182 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7c9a02c0-eb4e-3604-b99e-9eae5774c345 | -10.69173 | -54.17153 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 8a4076cd-5549-32c0-9375-7d1a6730b917 | -6.28695 | -59.95406 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| d0be885b-c7d2-3317-86b6-c9b83d2435af | -9.43412 | -50.1442 | 2026-09-14 00:41:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 6b57147e-b58e-3b61-ad33-b49f66a4dbd9 | -6.14125 | -59.89128 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README3.md)
