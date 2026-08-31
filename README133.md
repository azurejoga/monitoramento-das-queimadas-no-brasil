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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64276071-6bc4-3a4d-bc1b-8a26998ef66c | -5.88839 | -52.06375 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 81963e62-f55c-3fdf-87dd-972b00ec5208 | -5.36076 | -45.92166 | 2026-08-31 16:33:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 262bb019-a917-3fa3-a7dc-afb3c52b7072 | -7.62514 | -55.29162 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47a3557e-4a34-3a80-93f3-2daab7a4f0f7 | -7.77855 | -44.05888 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eac6f4e3-63e4-34ab-b397-62a959cc1eb0 | -7.9162 | -44.23982 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 01b9eb11-1e9e-325e-ad86-d06aff079af4 | -8.13646 | -45.58441 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 9c242800-1311-3dfc-87c8-3c9ec5188916 | -5.94291 | -44.96893 | 2026-08-31 16:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cdcc4fe1-634e-3ebe-90f2-e0a45e803ba9 | -5.86304 | -52.07996 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ffccab26-9b6c-3d14-ba55-b9c11058d4f7 | -4.95757 | -55.85353 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4dee785c-490b-306d-9441-ffe09a0384b9 | -6.13605 | -53.53299 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a63992af-4ab2-3601-9a49-910d905e42a1 | -4.24988 | -40.75771 | 2026-08-31 16:33:00 | NPP-375 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9349e9e3-f41b-353f-8699-39ffb09f9184 | -7.13924 | -44.30342 | 2026-08-31 16:33:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4d53f335-5ed2-3533-ab71-f847047288d0 | -5.76438 | -44.12827 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 07374193-a361-31e8-9a3d-b51fe1039b95 | -7.43702 | -44.94775 | 2026-08-31 16:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6a4245d2-d80d-3d99-b4c3-ab1fc4ca0b02 | -5.58785 | -42.32254 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9b2581b3-f086-3424-b57d-8bb89b413635 | -7.63406 | -46.73281 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57c9c439-1a31-3652-be75-e7eef2539f2b | -2.26656 | -47.86724 | 2026-08-31 16:33:00 | NPP-375 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| e1a8286c-c79d-3074-9ca1-8c988739d3b1 | -8.41974 | -47.72358 | 2026-08-31 16:33:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b8d1ce7-eae4-3595-8a08-d83570eefafd | -6.25667 | -53.67727 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e714878d-3cde-30af-a43b-ecd60bc3fede | -4.90647 | -37.43748 | 2026-08-31 16:33:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 12d5ba6a-1806-35da-b258-4571182a4874 | -7.62776 | -44.92445 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f56d5012-a620-38bb-8dbc-2b718c38524c | -4.96613 | -44.70677 | 2026-08-31 16:33:00 | NPP-375 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b58cabf4-7864-36f9-98a9-f931bf9ac2f5 | -4.36348 | -44.43576 | 2026-08-31 16:33:00 | NPP-375 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 46e9608e-be02-353b-b293-6c6e890dedf3 | -5.42568 | -51.20224 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 20fa1e4c-3c64-3559-a43c-fba7142db92f | -7.92595 | -44.23445 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 5a9a9a40-0e5a-3b09-b388-beaa3f38e0e0 | -5.46766 | -37.33081 | 2026-08-31 16:33:00 | NPP-375 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0b31c2c8-450b-31aa-a9bc-fc5b9ffdb325 | -5.65842 | -43.56095 | 2026-08-31 16:33:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 78010b7f-bac3-3438-8ecb-3a9c47e30e51 | -6.84319 | -41.69109 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| abe1a5bd-435b-3bd4-9fee-6918e10f340a | -7.62188 | -44.93344 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2282ce8c-4450-311f-9d34-78ea7ac6d12b | -6.9177 | -55.72597 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 166e3a96-edc1-32f1-8fd2-2a8f6662d099 | -3.42101 | -43.37622 | 2026-08-31 16:33:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 078f0fc7-80e4-3a8f-95d7-23e8c98a318b | -6.81632 | -51.1512 | 2026-08-31 16:33:00 | NPP-375 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d1c64a6-f04c-32e2-b014-7228f93fac50 | -5.88886 | -47.72907 | 2026-08-31 16:33:00 | NPP-375 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e5650eb5-25d0-3ed5-8361-754e172c3d2f | -6.40267 | -49.92887 | 2026-08-31 16:33:00 | NPP-375 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 0c8c5e17-d458-3adb-b157-97b2b1d43121 | -5.58666 | -42.33698 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f4dccc1d-df46-391f-a985-2e939ca5cc17 | -6.13287 | -53.5344 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 3cdf11a6-12a4-3090-ac1d-214695947e41 | -6.93209 | -55.62626 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| cbc181bb-eeed-347d-9755-2257519dbae8 | -6.6232 | -53.17848 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c88a9c2-54a0-34cc-9f50-6e8e657cc579 | -6.68657 | -38.49811 | 2026-08-31 16:33:00 | NPP-375 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b939bd89-7d81-347c-ac9d-344b8b40c37c | -6.8421 | -41.68403 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6ece819e-9374-3c08-813a-e5d912811562 | -4.7422 | -56.27009 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 69a14491-497e-31b3-a6be-ac0c094e8324 | -2.87767 | -43.59967 | 2026-08-31 16:33:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 270f7529-9dae-3ade-858f-fef494228a14 | -5.76101 | -44.12878 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dfaf31b8-38f1-317b-8737-c90065beab80 | -8.17964 | -54.92854 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 3a54ef27-ffd4-3828-b8b2-70ba3193ae88 | -6.38313 | -45.51369 | 2026-08-31 16:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 50c39894-e9ee-3b98-a01a-69974d476f82 | -7.52423 | -55.33333 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5590a61d-307f-3465-8452-dab13728700f | -5.58225 | -42.33052 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 302cd32e-8b81-32fc-b2e3-9cfe77b898ba | -3.22877 | -52.26229 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 125b8546-8710-31fb-89b7-963f9607d1b9 | -4.23482 | -53.52627 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bc1455a5-7751-3218-ad3c-04982d2779b8 | -8.96596 | -50.80651 | 2026-08-31 16:33:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8986ef1-d688-3c3a-bd45-2e22849614d4 | -5.65789 | -43.55745 | 2026-08-31 16:33:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 929bc70f-85d4-3897-9108-1353ba304b24 | -7.91344 | -44.25953 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 90e27057-3920-3fef-854c-f06de6481775 | -6.93274 | -42.7175 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 908a8e16-39f2-3a02-b31b-42ecd3c0bed5 | -6.26027 | -42.87093 | 2026-08-31 16:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c7e63f8-9966-308c-accd-7c82f273a37c | -7.17762 | -39.38085 | 2026-08-31 16:33:00 | NPP-375 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3a7ab38d-0f09-30eb-a369-7d0202598e59 | -7.99547 | -44.32354 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f35787ec-0265-3331-abf8-ea712ebcccc5 | -5.36136 | -45.92577 | 2026-08-31 16:33:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0e124880-6153-3c98-a984-3b9bdfd2e48c | -3.22782 | -46.36894 | 2026-08-31 16:33:00 | NPP-375 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ce1236d8-16f1-36fb-8ed1-7ca5c363f8f0 | -8.21669 | -50.77946 | 2026-08-31 16:33:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6e0f6e89-185a-356e-8fc3-f205de637703 | -7.64509 | -46.72335 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e40e60b1-595b-323b-91b8-28da3f479495 | -7.98903 | -44.35149 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 798680ad-8d30-36e2-8f7e-9f3a14b35143 | -4.67216 | -43.2247 | 2026-08-31 16:33:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 780fa102-5531-3ecd-a232-616a78a733bd | -7.94136 | -44.24359 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a2bb4dfd-d65b-3507-82d3-a60e53a6edd1 | -3.54827 | -51.11545 | 2026-08-31 16:33:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 89b86222-17bb-3ff1-98d5-25569779403d | -2.50289 | -48.13522 | 2026-08-31 16:33:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 0e2b235d-9a40-3785-89f2-5b8899fbd30d | -3.41803 | -42.83027 | 2026-08-31 16:33:00 | NPP-375 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9058d816-29eb-375f-ad7d-8f1f74e8342d | -3.73088 | -44.37284 | 2026-08-31 16:33:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03bf0af3-ee72-3a68-9c62-d036c3c7bed9 | -8.15256 | -45.46412 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d02a96e6-2577-313b-a7c7-c1d99778de0e | -6.93674 | -44.18352 | 2026-08-31 16:33:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5ec5a82-42bb-36c4-a731-55af76034227 | -2.55036 | -44.91248 | 2026-08-31 16:33:00 | NPP-375 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4b9b8479-3070-3ae9-a5fd-2a804e7024b7 | -6.77251 | -52.89723 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 51bee91d-5f58-3cf9-a0bb-54df6c80987f | -7.21336 | -42.73777 | 2026-08-31 16:33:00 | NPP-375 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9ce5a524-8c0b-3970-a1cb-dbbbe5b93ca5 | -8.14914 | -45.51728 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d2543971-6e82-3bb4-aef8-ee0fee683cae | -5.88745 | -52.05709 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 07f21d14-c7ae-382c-b57a-262a9a006862 | -1.67024 | -48.51691 | 2026-08-31 16:33:00 | NPP-375 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f4cfc4f6-2f9f-311d-8d60-da6b8526f0ba | -7.10565 | -42.23417 | 2026-08-31 16:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5c7c3cd7-9e67-37e4-833d-34983ccbffab | -5.5928 | -42.33248 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 998b1af6-ec2b-3a7a-ad70-ba99bf85fa89 | -7.91908 | -44.23554 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 41eec6b1-01e6-392b-8f11-6f54e1e15359 | -7.09637 | -43.88004 | 2026-08-31 16:33:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9cda9b01-aa7a-3b8f-847d-9e17af8ec123 | -5.57892 | -42.33103 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 51a3e26e-a484-3f8e-8d0a-af075ae7ed4b | -5.24716 | -55.91044 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| babf499a-408f-334c-ac82-7f77fe6121e3 | -6.41055 | -45.4273 | 2026-08-31 16:33:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22a1a6c3-d1c0-38bb-bf90-892f627495eb | -2.40029 | -48.16862 | 2026-08-31 16:33:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| f5ea7d1d-8287-356c-8d18-de4f9dd9ff5a | -2.73724 | -49.29286 | 2026-08-31 16:33:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 23901ce9-f80a-318c-bb20-5049cba0c89c | -7.63549 | -46.73951 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 53b86d45-7654-3308-9669-86fe67145a1e | -7.64897 | -46.72281 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 82396118-8a07-32c2-8624-9e70eaa07604 | -7.22214 | -42.75068 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c619b462-2e57-341c-9b5a-946d69fb5eb6 | -8.00518 | -44.34135 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 80e27514-b487-3e93-8823-e8c1504a0824 | -1.6055 | -49.9455 | 2026-08-31 16:33:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 7677f6a3-d65f-32d7-96cf-eaac443d1138 | -6.67976 | -52.86956 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf10494f-e401-3cd3-ba1e-9a272e434e38 | -8.80702 | -49.17091 | 2026-08-31 16:33:00 | NPP-375 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9f7994c-76ab-3010-9337-b554de3ef80a | -7.35941 | -55.19635 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d16515f3-55cd-3e52-901c-73d60f92557c | -7.13582 | -44.30395 | 2026-08-31 16:33:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0bd959fb-0bd3-3a87-90dc-efc12abf4492 | -6.93369 | -55.63488 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 8195af6c-81fb-35fb-97d4-38593eba1402 | -8.14955 | -45.46894 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 557b9894-3418-34ed-b9c1-da0d394cce55 | -8.21494 | -54.93791 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 90a58d87-5e15-3930-a666-fe63c7d59ff8 | -6.33716 | -47.30363 | 2026-08-31 16:33:00 | NPP-375 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| af1b39b3-a267-372a-892c-1e5d0bb46791 | -3.4239 | -41.71416 | 2026-08-31 16:33:00 | NPP-375 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 81ca2c98-24a0-3462-9d8f-2409a8364b79 | -7.92839 | -44.29899 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 7ff7c4ef-28e1-3457-af08-8ad776be770d | -6.33788 | -47.30865 | 2026-08-31 16:33:00 | NPP-375 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |


[Clique aqui para ver as próximas entradas](README134.md)
