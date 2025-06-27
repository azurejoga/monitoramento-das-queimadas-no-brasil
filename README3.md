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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 325b794f-1a1d-3d6a-bc93-86e1448579b1 | -9.74608 | -48.04871 | 2025-06-27 00:22:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6cf18417-3278-3bdc-95a3-e37ad2ffc393 | -6.96095 | -42.90348 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| dd931647-a218-3efc-8264-cc67ac98a18f | -6.7737 | -46.3386 | 2025-06-27 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| aecaa214-60bd-399f-b973-46b4725a2d4c | -6.47148 | -43.74552 | 2025-06-27 00:24:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 8634ed57-725e-3e8f-bcaf-f444e2c392e8 | -6.95044 | -42.89528 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 978acaa1-dda8-38fd-96ac-295ae8454d34 | -4.69014 | -48.86792 | 2025-06-27 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2e85f283-7974-3702-a497-e027ec78e9c8 | -6.17919 | -48.10061 | 2025-06-27 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8e9ec8f5-6764-3fb9-9743-71449006deb0 | -6.21533 | -43.36477 | 2025-06-27 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3cc67e2e-7b3e-3df1-b263-4e2db385eca3 | -6.26831 | -43.676 | 2025-06-27 00:24:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d8469691-0c54-3513-af2c-27ade617b0b4 | -6.69058 | -43.07743 | 2025-06-27 00:24:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 04fb0596-4d3f-32bd-9ebc-42aa257679f0 | -6.48039 | -43.74418 | 2025-06-27 00:24:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 545e06a0-a54e-3845-9b18-dd15bc5049f1 | -6.95181 | -42.90478 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5e2ea162-8198-30c4-b00e-ebfc51443370 | -3.99517 | -43.24 | 2025-06-27 00:24:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 979906e7-0cbd-3152-8ca5-dfb2350edaa0 | -6.66255 | -47.5813 | 2025-06-27 00:24:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0dd9bed2-0d5d-3142-8aa9-2e3b121d7d2b | -7.08384 | -49.60027 | 2025-06-27 00:24:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cc274197-a02c-37e7-8c4c-ce82407493e2 | -3.03776 | -49.43689 | 2025-06-27 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 661d238a-e257-3ca8-a831-c8528a45d663 | -6.16754 | -48.09003 | 2025-06-27 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a30d7cf1-229b-32d3-8f9e-5a790346ebe0 | -6.26959 | -43.68514 | 2025-06-27 00:24:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7367a953-e068-3651-8aa9-a369f69f0e43 | -5.91734 | -43.47311 | 2025-06-27 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 29b03801-0630-3347-9fa2-77f45befbef3 | -6.27725 | -43.67471 | 2025-06-27 00:24:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b68cadda-219a-3529-9c3d-3c5b6111438f | -6.77241 | -46.32898 | 2025-06-27 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 71507857-0252-3460-adda-4607db015976 | -6.95822 | -42.8844 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 988dc4b1-1459-33b5-b519-4879c6d9d797 | -6.94908 | -42.88573 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4b6e50ac-16ea-33c2-840c-9bb936baab26 | -6.17762 | -48.08862 | 2025-06-27 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 676.5 |
| f927ea60-afd9-3ac3-a473-10017412a05b | -5.17805 | -46.11123 | 2025-06-27 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9b6672dd-a514-3b9b-b2d4-07d0fda411f4 | -2.44347 | -47.4631 | 2025-06-27 00:24:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7acd2e41-de87-382c-963e-71c401fc91ce | -6.16716 | -48.08434 | 2025-06-27 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b6756aed-5a13-3e9f-b993-c856147719f8 | -3.0332 | -49.44379 | 2025-06-27 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 8fdb63ef-4076-35cf-b101-001edf17d402 | -6.97009 | -42.90214 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| dd1cc5de-3bce-3fc1-aa65-fa6cd611fa5e | -5.92635 | -43.47178 | 2025-06-27 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca62466e-2c15-34cb-964e-6e7ece69922a | -6.96737 | -42.88304 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 6cbe22fb-96d2-3afe-8769-ed24a40dafa3 | -5.97549 | -43.75436 | 2025-06-27 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f9e3dde-3462-3952-ae21-c43ee93a9888 | -6.95959 | -42.89394 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 357.8 |
| d69beb53-c2b2-3acb-ad16-fe3526f01fd5 | -6.48165 | -43.75317 | 2025-06-27 00:24:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 033dc0ae-12b2-3c81-b5e2-a9a2d4b2ce2a | -6.16878 | -48.09616 | 2025-06-27 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 52f3ac4a-0f98-37fd-bc26-852b39ad28f9 | -4.12676 | -43.06855 | 2025-06-27 00:24:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| af1c1f7d-bea8-37b8-950a-b0b176ef0ac5 | -6.78158 | -46.32771 | 2025-06-27 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0759d851-9b78-3391-a212-3b16b0b6c2f9 | -5.85769 | -43.63823 | 2025-06-27 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a2babdab-0e8f-34c4-9ba7-f0e10651b2d0 | -6.47275 | -43.75455 | 2025-06-27 00:24:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| c169cd92-bca7-3c7b-9fa8-3826c467b1b7 | -6.96873 | -42.89258 | 2025-06-27 00:24:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 269.2 |
| 88a6ab3b-a9b8-326d-b0f8-7e4c05a078e9 | -3.03139 | -49.43077 | 2025-06-27 00:24:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| d50233d6-00c4-37b4-96c5-862916e94fc4 | -6.27853 | -43.68387 | 2025-06-27 00:24:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d39b6041-4836-3125-99d0-5269950da20f | -5.44233 | -46.56551 | 2025-06-27 00:24:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3218c662-c489-37f9-bfca-1ebbf2c7175c | -5.91865 | -43.48233 | 2025-06-27 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d9035c40-941a-3558-a76e-a289890fe4b5 | -5.85898 | -43.64738 | 2025-06-27 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1f3d81f2-3cf5-3872-80fb-b66fc478ff83 | -6.17607 | -48.07676 | 2025-06-27 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 8ead76fb-7f10-336b-8c14-115bc554f8f0 | -5.6149 | -44.00584 | 2025-06-27 00:24:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 86aad3c6-a399-3191-a414-f0988ccb5a28 | -6.65275 | -47.58271 | 2025-06-27 00:24:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| de273b6f-70be-3cee-b864-e377ba63d6fe | -6.22437 | -43.36349 | 2025-06-27 00:24:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4f7d6497-579a-358f-a7da-020263510a7f | -6.68924 | -43.06805 | 2025-06-27 00:24:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8c7e4506-0328-3856-aa0c-cb4e06fcda50 | -7.2031 | -43.0701 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 8d7f8a16-801b-380f-bc59-66c03c6e46e5 | -9.0648 | -49.4366 | 2025-06-27 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 72cf4a50-526e-3bed-bb69-493668d26ef6 | -8.6094 | -51.594 | 2025-06-27 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5a1bdee3-7c45-3011-a228-6f6c36db83e0 | -7.2028 | -43.0936 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 18768a93-519d-3ae2-b352-33be1b812166 | -11.5969 | -52.113 | 2025-06-27 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| cf7b0999-d4d2-3101-a3e5-8904c53fc562 | -11.5779 | -52.115 | 2025-06-27 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 548.8 |
| 60120e41-b24b-30a5-a417-31046b369b67 | -11.559 | -52.117 | 2025-06-27 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 217.0 |
| 4ad5e512-c28c-3d96-bd8e-1561a2dae3ff | -11.0455 | -55.3773 | 2025-06-27 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 49db4009-dd8a-3de5-9540-8d9d1a4865fe | -6.1791 | -48.0712 | 2025-06-27 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 217.6 |
| d6c41ab0-fc51-34fc-8546-5341a269554b | -9.0651 | -49.4151 | 2025-06-27 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 6ac4a5d7-2edc-39f6-8360-3e93e9698372 | -14.4281 | -48.8649 | 2025-06-27 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 59c50275-c39d-366c-a49f-c988484df5d0 | -11.5776 | -52.136 | 2025-06-27 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| a03d3534-0d23-31db-897c-d71a4d9fb348 | -10.2941 | -57.138 | 2025-06-27 00:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| f220686f-5a7a-3e0e-8f9e-17c4128996d3 | -11.3616 | -48.7142 | 2025-06-27 00:30:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 01ce36b8-85e9-34e5-ac59-ab37f55a7f53 | -12.0248 | -47.7702 | 2025-06-27 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 430a44a6-15bd-3d52-b334-f4f20881a587 | -6.9793 | -42.8798 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 9e6704d1-00f3-30e0-b032-a6c1e7cf6e79 | -6.9416 | -42.8834 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| ea65a9b9-3e4b-3f58-beeb-e9488e4212f2 | -8.6282 | -51.5925 | 2025-06-27 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 4cc73ed1-8574-3d9e-b6cf-6a218fe76cb7 | -7.2217 | -43.0917 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| cd7c6464-77ad-3f35-8fef-cd5ac9dc5582 | -6.9605 | -42.8816 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 286.5 |
| b381a5ba-ae42-391e-b797-e80abf28c8c6 | -8.6284 | -51.5716 | 2025-06-27 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| f37d5d35-a221-31b3-9f50-494f7f1a1070 | -6.1977 | -48.0699 | 2025-06-27 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 952436ad-1920-338b-ab78-93831aa2621d | -6.1602 | -48.0941 | 2025-06-27 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 07026965-927f-37c4-ad51-9c2f2a96d709 | -14.4476 | -48.8619 | 2025-06-27 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| d3987e8a-af33-34a1-a510-363227ec1384 | -12.4433 | -43.7242 | 2025-06-27 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a55eb8aa-a152-3ec8-b105-665042345b6f | -7.2219 | -43.0682 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 7c70d0fc-e89a-39ec-ab0b-514e578ea2e5 | -12.424 | -43.7274 | 2025-06-27 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 425ca7b1-6110-3fc0-9992-eb4d4a0db052 | -6.9414 | -42.907 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 7bf2534f-7e21-3982-80a4-ac77155401a8 | -6.1789 | -48.0929 | 2025-06-27 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 369.1 |
| 33f08539-8cf1-395e-9000-8869d43aee26 | -6.9791 | -42.9034 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| 2f563032-409f-348d-96ad-2b73739477d9 | -11.0646 | -55.3555 | 2025-06-27 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 09fd49fa-1a1e-3213-ab96-6962c238cf0e | -11.5592 | -52.096 | 2025-06-27 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7ee7e847-cb2f-3140-889d-59f3215ab194 | -6.1975 | -48.0916 | 2025-06-27 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e2d31603-26dc-3671-9a77-59ee1b5b9741 | -6.9602 | -42.9052 | 2025-06-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 336.8 |
| 91bb3110-01f7-3a3c-9666-2d980645534b | -6.1604 | -48.0724 | 2025-06-27 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 7d7fd30a-ca07-33c9-bb44-8a2fc466d916 | -8.6097 | -51.5731 | 2025-06-27 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 221.8 |
| 96bca67d-c73c-31c9-b7a8-509840d3207b | -11.0644 | -55.3757 | 2025-06-27 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| ea6c3e67-40b6-3233-a89b-e303ee239727 | -10.2942 | -57.1182 | 2025-06-27 00:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 77722c41-c79a-318e-ac44-1a1ad393b68c | -11.5782 | -52.094 | 2025-06-27 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 1c3871ee-1f9b-3b3c-8830-0ebde6e6c01f | -6.1791 | -48.0712 | 2025-06-27 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 227.8 |
| d28bc574-8f1f-39ae-bbee-89754c7359c3 | -14.4476 | -48.8619 | 2025-06-27 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1d710331-b695-3c93-9f3d-dc057bb4932a | -6.1604 | -48.0724 | 2025-06-27 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8853ad7a-50c8-3363-8a78-60ada98b088c | -7.2028 | -43.0936 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 6a43cd81-2b42-3e80-93af-a6e02d322747 | -6.1977 | -48.0699 | 2025-06-27 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 17ab1345-7853-38a8-8342-57fad2179a29 | -7.2031 | -43.0701 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 88737f09-b76c-3364-aa59-c113bdc28414 | -6.1975 | -48.0916 | 2025-06-27 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 98d51e47-b08d-38c9-8a3e-cee6daaaf6e5 | -8.6094 | -51.594 | 2025-06-27 00:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3869cff4-3ccc-3ecc-a7da-6a413c54b9d9 | -6.9791 | -42.9034 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.6 |
| fdf970f3-9c3b-3157-8954-d7b3c18692bd | -9.0648 | -49.4366 | 2025-06-27 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 8eb7bb76-f594-363c-9149-513bdad20c42 | -7.2219 | -43.0682 | 2025-06-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |


[Clique aqui para ver as próximas entradas](README4.md)
