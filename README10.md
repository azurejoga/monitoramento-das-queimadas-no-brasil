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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed85f8f8-b05c-37f9-9cc4-fdbc7b0c6897 | -5.86286 | -46.48195 | 2025-06-28 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cc0a4ef-188b-3f0f-b6e2-ae835b71bddc | -6.95092 | -42.87734 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc1137d7-d4b8-316b-a5b4-9271d499b67d | -7.34415 | -45.31443 | 2025-06-28 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 056b5926-d3a9-3b34-9927-035a7dce3880 | -11.83345 | -47.53446 | 2025-06-28 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 204d58a3-2603-3e2a-9555-1e94e21ac116 | -11.01424 | -45.2429 | 2025-06-28 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 79b6ceac-f37c-3c72-b435-ec82b6e4f51c | -7.11266 | -43.37684 | 2025-06-28 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c737a27d-cb60-3d9c-8fea-98a04c1b0676 | -11.84026 | -43.79826 | 2025-06-28 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05602ed6-ffec-3293-bead-3c08e9504d89 | -7.27092 | -43.85488 | 2025-06-28 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec99945-754e-3c88-8123-ca3b30b14306 | -9.11354 | -49.49286 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d36e6b4d-701a-30dd-bc73-c11b5a2064a6 | -6.45271 | -44.5718 | 2025-06-28 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4ca3a27-2cae-30ff-87b2-d668c6333a44 | -7.17879 | -43.72987 | 2025-06-28 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b05278fe-f7cc-342f-89ef-afe61b3170c1 | -7.21213 | -44.89835 | 2025-06-28 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2db79db0-783c-3a65-aaf6-596a68722796 | -11.60605 | -47.6131 | 2025-06-28 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12ad3764-e87d-310e-b3a1-3682c8f846e9 | -8.86065 | -50.16435 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cb08f6f-6064-3dfe-85cd-5fc67cc0eade | -4.54805 | -48.02269 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 90a7f008-d1a4-3210-b82d-123330aec8bd | -6.74149 | -47.22636 | 2025-06-28 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a45e55e-b373-30ff-88da-296ddeaa3a7d | -9.87666 | -48.05331 | 2025-06-28 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cfdfe98-49f6-3160-9cbc-fd67a7546963 | -7.21807 | -43.08654 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0f4d2fae-66da-3ca1-822c-af845ec1bc86 | -7.21935 | -43.0794 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9841bd17-e7cb-3e3d-a3c9-23dc4359af58 | -8.31094 | -46.30913 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fd72f64-a62f-3a0e-8924-e71b8be6cda9 | -6.91211 | -43.98272 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7b6cae9e-79b8-330b-80bb-8fc226e00049 | -6.69028 | -43.07148 | 2025-06-28 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c01a8a9-c4ad-3b4f-8672-7c28739d5615 | -4.54249 | -48.0248 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 5a155ff2-6c82-3786-8ce8-2e6cd62c2f02 | -4.54381 | -48.02322 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| a4f7782c-0f68-35aa-a419-74aa566e0afc | -7.22227 | -43.0831 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 8f343ffe-1ae6-38a7-8c4b-814e6639adf0 | -7.62976 | -43.07698 | 2025-06-28 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9e690e40-b0bf-3b8d-935b-6ac7b386638c | -9.11635 | -49.47735 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e57339f3-3b0b-31a5-8e0a-9e8929dffacf | -6.9563 | -42.91079 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e09a04cb-4ab9-399c-a81c-4f659240823e | -8.58147 | -47.97937 | 2025-06-28 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7020c233-6bf7-3d52-b3fb-bafce3361c29 | -7.11059 | -44.1933 | 2025-06-28 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a28b234-d040-3ca5-a3b4-474339b96477 | -8.32041 | -46.23078 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2b42c3a-af58-37d3-82cf-e1411732705d | -6.71838 | -44.40274 | 2025-06-28 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8dbc09a-578c-3c03-a78c-3b8b4c0f1680 | -10.95336 | -49.25127 | 2025-06-28 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47eac2d1-197d-3d07-8d3d-2a16930c5478 | -8.5641 | -51.57135 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27d9dea7-0667-358e-9603-15f2499026cc | -7.2187 | -43.0834 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 1029402b-5bc6-3eaa-85a4-5d8413a1ff28 | -9.11983 | -49.48755 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8386e712-0ea3-3963-a4c9-24eed46d5769 | -5.45617 | -43.07906 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f9ec666c-e0d9-336c-87b1-584ee47e5d27 | -10.83264 | -53.74923 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a361953d-e782-38e8-a8bf-a8e7ab69e480 | -11.84091 | -43.79433 | 2025-06-28 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 687d7b74-d629-3ceb-8760-3f2d66f2c38c | -7.5455 | -45.82854 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77a59de4-7fb5-362c-9b9e-011c9b0f7363 | -6.89947 | -43.98977 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 59c03485-dfd2-315b-b57b-1d82ae41fdc7 | -6.89721 | -43.98025 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ed55323-08c2-3063-96e9-698989de40d3 | -7.11334 | -43.37268 | 2025-06-28 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eec9e8ee-ee13-36d8-9ad0-1002fdb1b6a4 | -5.44008 | -46.56693 | 2025-06-28 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 370e4441-3475-361a-8a42-75d6efa619b1 | -10.95486 | -49.25336 | 2025-06-28 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 757bcba1-cf74-3222-8546-313a1472cb6f | -7.19895 | -43.18405 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 481fc348-2e01-30fc-834d-53545f18eea3 | -11.59036 | -44.6658 | 2025-06-28 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87ba5357-acdf-3df3-ab8f-728e3a0ce6b1 | -4.5443 | -48.02026 | 2025-06-28 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| b3fcebca-fb00-3741-b8fd-7d7f9e812e05 | -9.15197 | -46.37389 | 2025-06-28 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54d360c8-a955-35ed-98a1-7e7c94d14226 | -7.20743 | -43.08571 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 3e10b1ba-5739-3467-b031-cfb06474bd33 | -8.03322 | -47.64203 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b760469b-79e8-3dd9-8487-533d051bade7 | -11.54539 | -47.87324 | 2025-06-28 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9afb95a6-06ca-3c90-b5b9-8320ae7b7dde | -10.95233 | -49.257 | 2025-06-28 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09713e99-c675-3c64-b072-caee8e7c6d88 | -8.31091 | -46.30969 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 858bff46-5473-39a4-93b4-cec628b91ea4 | -8.80039 | -44.99368 | 2025-06-28 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f2b709c-d800-39be-8066-5c3b4c45291b | -7.20251 | -43.18463 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fc230a29-5fe4-35e0-b64e-c54e33d0bfd5 | -8.56654 | -51.57499 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7623004d-d798-3a5e-ac68-c14d322a9a09 | -6.90319 | -43.99041 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4943eaf2-b390-314d-b521-ae03ea5da221 | -9.11927 | -49.49062 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 1693a43f-7da8-3fae-8dfd-f0f8c6ccaebd | -9.43991 | -47.95921 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b66d43a5-c036-3b9d-9430-2402a0858c6f | -6.71455 | -44.40215 | 2025-06-28 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e321b4dc-2927-30be-816a-b0519a5a7f6e | -8.02857 | -47.64126 | 2025-06-28 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a92aee0-ec7f-3551-b6aa-1de4f11edf59 | -10.52687 | -53.62632 | 2025-06-28 04:02:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0289290-fb30-3a6b-bc4d-0464067f97f5 | -11.0631 | -43.1798 | 2025-06-28 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ba02602-7da7-3170-b613-d10cf6c12db0 | -7.71053 | -44.58672 | 2025-06-28 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecbe16b1-3bc2-3b6c-a04b-de1cd5d1126d | -11.6583 | -46.73333 | 2025-06-28 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75d841da-dfc5-365f-bfa4-2c54d64dbe1c | -8.31987 | -46.23001 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca250cca-f57f-349b-994f-297739ae5b98 | -6.91571 | -43.18167 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 438add6d-3e5f-3d72-a3c6-c9186de78d9d | -11.6104 | -47.61393 | 2025-06-28 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d21d269c-128d-338d-9015-a5b95334db5f | -7.55314 | -45.83363 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dfad339-02ec-3896-b898-c3187bd25d45 | -9.1141 | -49.48978 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5af97cc0-6f17-36f2-bd21-265f80c7da6c | -6.71377 | -44.40681 | 2025-06-28 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 871f1eb6-a03c-3277-a302-233bc97e7efa | -7.88643 | -46.32359 | 2025-06-28 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d180ddd0-dfce-3c44-a0d5-2e49f8125696 | -7.21558 | -43.18991 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f07089de-f770-3de1-9545-7b4c6c78066b | -8.86542 | -50.1688 | 2025-06-28 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7b5a2ec-0dc0-32c4-af44-f2f9d5103946 | -11.57885 | -47.43093 | 2025-06-28 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d61f6e2-ee8b-31e8-b59e-7ebb82e0d51c | -7.2158 | -43.07883 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 53ea1881-c2df-3131-9bf9-7b25aba775ae | -7.21939 | -43.07853 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| fced2847-5499-306f-9d93-9c3d84941ecf | -7.22515 | -43.08768 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4414b585-2c93-3bd2-89f4-ec489794439b | -5.46341 | -43.08016 | 2025-06-28 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0cf4e417-1a9b-338e-b50f-fae10b47bb76 | -10.82725 | -53.74217 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fb92a01-c7ea-3956-abbd-17d5705acaeb | -7.09761 | -44.36766 | 2025-06-28 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bfe5baf-5f83-39cb-a723-d0c6d255fa29 | -9.11872 | -49.4937 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0e470c3b-fdf0-31a9-9289-27eb83cf84d2 | -6.89574 | -43.98914 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ca5f582-d05b-39b5-84c8-aefb070500d2 | -8.56059 | -51.5739 | 2025-06-28 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| affd7967-db26-30a8-b33f-1cf6c3ef4d38 | -9.15613 | -46.37476 | 2025-06-28 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44828385-16e0-3ead-a3fa-5fe85564f986 | -6.90246 | -43.99487 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99b6ec90-c7ef-3d44-8a04-12aa2683c723 | -6.74239 | -47.22441 | 2025-06-28 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1624df6c-e3d9-3b91-a1c1-3e7ad83bb5bd | -6.91138 | -43.98717 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 53389d69-e15a-3807-b077-a9059456acb2 | -9.36588 | -47.63153 | 2025-06-28 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c172b3a-5ba7-3839-a293-53ae0bfb6ffc | -7.21491 | -43.19397 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 85d9a30d-8293-3b26-8825-df10a48c8df1 | -10.83041 | -53.76052 | 2025-06-28 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a3d414e6-b612-3834-b3f7-1832050d22ec | -9.44595 | -47.95819 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8347b15-5f41-39ca-9312-05bf6a1e7f84 | -9.12153 | -49.47814 | 2025-06-28 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c330850a-4418-3dff-a538-34cd09f71b1b | -6.9024 | -43.97197 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20ef2734-de78-3fc2-8ed1-08b375e9cc8b | -6.91284 | -43.97826 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8d00ccf2-be41-3b55-9611-628939028f7e | -11.54072 | -43.24686 | 2025-06-28 04:02:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f1005b7-4d2a-3362-af07-5821f1228d6a | -9.44454 | -47.96 | 2025-06-28 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1fd52952-1f1c-3577-9d09-05577c1481ff | -6.90392 | -43.98595 | 2025-06-28 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d68a7dcc-7f0b-39ce-aeaf-d3a570094e6d | -6.84386 | -42.79999 | 2025-06-28 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
