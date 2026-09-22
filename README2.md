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
| a3a0e5c1-5e04-3fe4-b1c1-a2c8e1239d98 | -11.6793 | -43.4684 | 2026-09-22 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 34ed9eee-2640-3687-ac30-5384babd688f | -2.8608 | -57.7994 | 2026-09-22 00:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d51bfe98-45bb-3b24-9130-d6c8c32c4111 | -10.6097 | -53.9697 | 2026-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e67b597c-0e3f-37d9-912b-92017d620917 | -12.8056 | -54.0462 | 2026-09-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 224.5 |
| ceddb6a8-5b40-363a-ab20-7d32bd029bdc | -11.6798 | -43.4446 | 2026-09-22 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e7e50445-7483-3449-95c1-40abeb885df0 | -8.2574 | -55.2604 | 2026-09-22 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 79a9702e-d02b-336a-a907-b9bc4a9a53f9 | -8.257 | -55.3005 | 2026-09-22 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1638cc90-2505-3c58-a08d-1c60490c10a8 | -12.7868 | -54.0275 | 2026-09-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 272.5 |
| ed7e58a9-0628-3b8b-a37a-55167f8750e1 | -11.3444 | -54.047 | 2026-09-22 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 627462ee-7e0d-3263-92cf-dd62e56841ac | -10.5906 | -53.9918 | 2026-09-22 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6dcdce85-cbdc-3bc5-bd18-18125e62748f | -9.2762 | -46.1627 | 2026-09-22 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 323.0 |
| 1aa97216-2360-316a-a29a-54325c17d8c5 | -12.574 | -45.9576 | 2026-09-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 306f7ed1-8e6c-3482-a989-8c2491bbe79a | -8.6169 | -54.6328 | 2026-09-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0bba7dea-20f8-370d-a87a-42b98ed58314 | -6.0928 | -57.6262 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| dc825a9c-ec99-319d-adfc-c11b0cf08edc | -12.7865 | -54.0482 | 2026-09-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 216.5 |
| 42327f94-1e43-3705-8afc-e0d78af26c0c | -6.467 | -59.9902 | 2026-09-22 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.8 |
| fe6cadb8-3f27-338b-8a55-9a2f27fc3be9 | -12.5551 | -45.9376 | 2026-09-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 97f5e681-7ac7-3f51-a3d4-996991f0d7d4 | -12.8246 | -54.0442 | 2026-09-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9d241ab3-0adc-3c0a-9149-07700ee3a5c5 | -6.0925 | -57.6847 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ce7532c1-651d-343e-8e38-fa62dd6741dc | -9.2573 | -46.1647 | 2026-09-22 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 284.6 |
| 1c2c3db4-2dda-3638-a2bb-1fa979cd5e88 | -18.7472 | -46.93 | 2026-09-22 00:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4f3131ed-4252-312c-b76f-bda74c8f96c0 | -9.2759 | -46.1852 | 2026-09-22 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1506003d-f43c-39b3-a407-5eec6367f23d | -12.5547 | -45.9605 | 2026-09-22 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c8b49363-eb83-3499-93fe-7ab323e5a4a4 | -3.0542 | -54.4081 | 2026-09-22 00:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| cb6934f6-6662-37cf-b400-e333d29c11b1 | -2.4206 | -58.2712 | 2026-09-22 00:10:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a7cce038-a284-3dc7-9cb7-06ee66f06f6c | -6.0365 | -57.8235 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6ae29f59-7747-3f2d-9fe5-72c528c74f8f | -7.5704 | -57.6766 | 2026-09-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| c92dd4c9-ceb3-335a-81f8-9db00a8393a4 | -12.8249 | -54.0235 | 2026-09-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| a7a6f98e-a0e4-36ad-acff-d50febecac3d | -11.3068 | -54.0299 | 2026-09-22 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 63f5d016-9782-3764-a411-58aedb6af8c1 | -5.7567 | -45.1067 | 2026-09-22 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| b01ee2c1-276b-3f17-99bc-fcd4e1aa48d8 | -5.8052 | -43.867 | 2026-09-22 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 56502fa5-8c9e-3dba-8e20-376445a7199c | -8.8275 | -50.482 | 2026-09-22 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| df8ad704-5b2a-356c-a410-805e664f4640 | -9.25 | -46.16 | 2026-09-22 00:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb95c374-102b-38fb-b9b9-f87634a14aea | -6.64 | -59.9 | 2026-09-22 00:15:00 | MSG-03 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f20e9fc6-e538-3700-a933-fd2be68c4bdb | -9.25 | -46.21 | 2026-09-22 00:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77eaab12-c73b-3ab5-928a-2b1989afac24 | -9.28 | -46.22 | 2026-09-22 00:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48829f1a-08fe-34c5-a137-2813d28224fd | -5.76 | -45.05 | 2026-09-22 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9ad6bfb-36ae-30c0-984e-716970431a18 | -9.28 | -46.17 | 2026-09-22 00:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 221fb7b1-f702-3661-82de-2f57256b7385 | -5.76 | -45.09 | 2026-09-22 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6c5be61-f60e-3d81-adde-0047ac911dbe | -5.73 | -45.09 | 2026-09-22 00:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f14352d8-8780-3a0c-8f1a-6c2b4c202a16 | -6.4671 | -59.9711 | 2026-09-22 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7336f35f-cc43-38ce-9753-78c45ccf4154 | -9.2759 | -46.1852 | 2026-09-22 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 1bfc56d9-ac30-3326-932e-5c89994983c2 | -9.257 | -46.1873 | 2026-09-22 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| bf8acb53-c14c-317e-8d3e-7de1b83c9c53 | -3.0726 | -54.4076 | 2026-09-22 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 1ea77ff7-3310-3dbf-8df5-1655334fa133 | -12.8056 | -54.0462 | 2026-09-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 08f4e86a-d5e1-3ac1-82b3-68602574420c | -4.3137 | -49.1226 | 2026-09-22 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8e4ec6c0-9f2d-3dea-9958-7f1948bf38f0 | -8.6169 | -54.6328 | 2026-09-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 634e74c8-9ea9-325b-a8a3-0cad7d7e6405 | -5.7382 | -45.0853 | 2026-09-22 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 212.1 |
| a37498a3-fb1f-3b46-881a-d67744fd4ef5 | -8.2388 | -55.2616 | 2026-09-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7c895505-1796-3d0d-898d-8e9f049110d2 | -6.4669 | -60.0094 | 2026-09-22 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 47290282-625f-3f13-be15-758f9363bf1d | -9.2762 | -46.1627 | 2026-09-22 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 14f10fe8-68dd-3466-b83a-44c263957c93 | -8.257 | -55.3005 | 2026-09-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e6cfb9e8-229b-3988-a9e0-26ecb45d5e66 | -11.7672 | -50.8253 | 2026-09-22 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bf02ea52-33e9-3513-9362-e7bff9695c05 | -9.2765 | -46.1401 | 2026-09-22 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 0db76b90-e158-385d-a0b1-f20faf835621 | -6.0365 | -57.8235 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| cd4def2d-5f66-3357-961c-5e0b4abdaf29 | -8.2757 | -55.2994 | 2026-09-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 4d84b612-843d-36df-9b7d-45e41870cf3e | -5.7571 | -45.0613 | 2026-09-22 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b797018d-d3b0-3feb-b038-b63af2aaeac7 | -9.2576 | -46.1422 | 2026-09-22 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 8a111754-d902-378a-8b13-87bd5c6c89a3 | -5.7864 | -43.8684 | 2026-09-22 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 320.5 |
| b4472004-9e55-3d44-8f3d-1e0a143d5757 | -12.574 | -45.9576 | 2026-09-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fe8552d5-1d02-31d9-aa99-6f90e6e15043 | -8.6171 | -54.6126 | 2026-09-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4660642d-38ef-3a2e-a90d-5e2833662632 | -12.7865 | -54.0482 | 2026-09-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 35d4b787-d2dd-3f52-88f3-a18b9ee30cf8 | -5.8052 | -43.867 | 2026-09-22 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 227.9 |
| fa884211-e8e2-3ed4-a2fa-941af0de7545 | -5.7569 | -45.084 | 2026-09-22 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 606.0 |
| 0d5bde61-666e-3ad0-9fdf-4f85640b398c | -8.8273 | -50.5032 | 2026-09-22 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| dfc998be-f775-34e8-bc63-a1a42098254c | -6.0549 | -57.8227 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b97de4a7-7019-3369-8893-de5be2284a76 | -11.3255 | -54.0487 | 2026-09-22 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 188.4 |
| c147a211-eef0-34a7-a2ae-5edf25f07a24 | -3.0542 | -54.4081 | 2026-09-22 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 705fdeab-b3ab-3aba-a6a8-697d2e97972f | -12.8059 | -54.0255 | 2026-09-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 1cd86fe9-868f-3457-a93c-1be65cf5ca99 | -6.789 | -48.6779 | 2026-09-22 00:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 71ebafed-d787-38a0-8f9d-449f77273f1f | -6.467 | -59.9902 | 2026-09-22 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 6d86a283-ed40-3974-959f-ba3f20857bd3 | -8.8275 | -50.482 | 2026-09-22 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c0240bcb-fcf7-3e9e-860a-86c78aee77ea | -2.8608 | -57.7994 | 2026-09-22 00:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 713d159a-8cb7-3f1f-b25b-a2e5bc19f809 | -8.8463 | -50.4804 | 2026-09-22 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 659e94a5-49a3-321f-853d-29c7f2b6f874 | -5.738 | -45.108 | 2026-09-22 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2228993a-9fb5-39cb-a166-26b8e50e421c | -5.8054 | -43.8438 | 2026-09-22 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 7e746737-11c6-3846-bbff-6c71ef3dc9e9 | -9.8872 | -48.4669 | 2026-09-22 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c149cfa4-4a83-3c4f-91a3-1f0a87d305b3 | -6.571 | -44.1516 | 2026-09-22 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e4840aa2-2559-3eb9-a78f-82a5683c6b8c | -6.0928 | -57.6262 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c6d41057-3066-3a48-a370-0aa848410aa5 | -12.5551 | -45.9376 | 2026-09-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9bd69ccb-4015-33ee-b0a8-5801ad58e548 | -7.5704 | -57.6766 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| c1ceccdc-8746-3809-9df2-b60762ecc484 | -18.7472 | -46.93 | 2026-09-22 00:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 9c1a1de2-dd50-38e2-9c16-1660cbbd86e7 | -12.8246 | -54.0442 | 2026-09-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c2fc8cda-821c-32aa-9fcd-d7ced308154a | -11.7484 | -50.8061 | 2026-09-22 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3395ad49-76a1-334a-b3df-c99333bb8ad9 | -11.3066 | -54.0505 | 2026-09-22 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 48560c40-68b0-3774-939c-2eb02a73c797 | -3.3867 | -59.5223 | 2026-09-22 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8aef55a1-ecb3-3f79-9cdc-e6ad96e81430 | -4.2239 | -48.6127 | 2026-09-22 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2ca8795e-aca2-31a3-9b90-00c0ad74214e | -8.2572 | -55.2805 | 2026-09-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b66136fe-9da3-353e-8503-e6f6fdb10571 | -12.5547 | -45.9605 | 2026-09-22 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a9ee8b03-032a-39ce-866a-8fe0537cbc77 | -11.6798 | -43.4446 | 2026-09-22 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4a535a5f-17c3-36f2-87ae-c8744c0e6894 | -12.8249 | -54.0235 | 2026-09-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 9246a1d9-a9a8-3806-abae-57087458480d | -12.7868 | -54.0275 | 2026-09-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d5dde572-e267-3f31-b8d3-0ff8fe4b0025 | -4.2951 | -49.1234 | 2026-09-22 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1cd123fd-7c48-37d1-917b-424be2e632ee | -7.5889 | -57.6757 | 2026-09-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 55ec78d3-9846-3a1c-97ed-c15e51d26503 | -8.2576 | -55.2403 | 2026-09-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 7b4684ca-49e9-3980-a739-da08d589b89c | -5.7756 | -45.0826 | 2026-09-22 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ff97893b-8fe1-3031-80ea-140ab0afc9b9 | -7.326 | -55.5953 | 2026-09-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8e9eb0fa-100b-382c-b988-480eafe32704 | -3.405 | -59.522 | 2026-09-22 00:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bed151e8-994e-3a65-ad35-e0f7e6d75752 | -8.2574 | -55.2604 | 2026-09-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 14968543-7c80-36bd-876b-cfe85422a589 | -18.7466 | -46.9534 | 2026-09-22 00:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |


[Clique aqui para ver as próximas entradas](README3.md)
