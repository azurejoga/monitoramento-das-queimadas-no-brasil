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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b13e648d-9ec8-35fd-ab08-cac300556fbf | -5.91187 | -43.6293 | 2026-07-03 11:28:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c5880cda-9513-3f0c-8ec8-ef7e3fe71823 | -6.91353 | -43.72147 | 2026-07-03 11:28:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 5a7aa054-dc08-3be9-ab96-6c0d17b9b6d0 | -5.80214 | -45.03556 | 2026-07-03 11:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| b21b39c7-894f-3e52-a71a-af6acc0d8507 | -6.78486 | -39.19011 | 2026-07-03 11:28:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b2ca214f-451b-39cd-ad98-e5b31d3c8bd2 | -6.90682 | -42.84674 | 2026-07-03 11:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| dafec4d3-28c2-348c-8b55-6a5790f3b1b2 | -5.78709 | -45.06144 | 2026-07-03 11:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 98adf7c4-f6ec-38b2-b166-b0516b7ffff0 | -6.78619 | -39.18061 | 2026-07-03 11:28:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 36809d7e-7224-312a-96e4-315a9b087a20 | -5.81298 | -45.03727 | 2026-07-03 11:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| c99dfc71-6402-33d4-aad5-f127341588ad | -6.93456 | -43.71347 | 2026-07-03 11:28:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d3a8269e-daf2-31f3-ad07-06119bf6604d | -5.79667 | -43.6337 | 2026-07-03 11:28:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 71c00516-0c22-347f-9e07-87baf5276a39 | -6.89758 | -42.84544 | 2026-07-03 11:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| b5c7b4eb-9f7e-33bf-95bf-1e13a6dbc818 | -6.89614 | -42.85528 | 2026-07-03 11:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| fd917ad1-2c25-394e-af9b-505ebaf971d9 | -3.41674 | -41.7064 | 2026-07-03 11:28:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 5ad23dd8-35df-3d01-bda7-d525b5a1f0dc | -8.00563 | -44.15974 | 2026-07-03 11:28:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6a3f4d34-51dd-3b4b-bee0-736bc81df1fe | -5.91352 | -43.61825 | 2026-07-03 11:28:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 42e6ff43-7c8d-3d94-a861-b9353751ccfd | -5.79797 | -45.06303 | 2026-07-03 11:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 632.7 |
| 123b88f5-764f-3be7-8bc7-42a9bc1eb23e | -6.93294 | -43.72432 | 2026-07-03 11:28:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 15586231-44db-315a-b0e0-a3211e0a42db | -5.7943 | -45.0813 | 2026-07-03 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 990c07d1-c8f2-353c-bf0c-a36cd41ade03 | -5.8132 | -45.0573 | 2026-07-03 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ba9a2fc7-1989-3fa2-8229-64453996e9db | -5.7947 | -45.0359 | 2026-07-03 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| f815c248-9444-31dc-9538-13f353e26725 | -5.7945 | -45.0586 | 2026-07-03 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 597.2 |
| 32b15a73-0b0e-3fb2-b631-786a9343f1e5 | -12.50668 | -48.27142 | 2026-07-03 11:30:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7d557d28-51d6-32b4-b64f-9616eecd597a | -12.77644 | -44.52305 | 2026-07-03 11:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5c7a6913-b347-335c-b5ef-a3ccf17e6928 | -17.59985 | -46.49644 | 2026-07-03 11:30:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6a719e9b-9e80-3e0f-a46b-56357da6c26f | -12.75145 | -44.52365 | 2026-07-03 11:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| df1f66b3-4ff6-395c-b37b-8c16630735a4 | -11.92337 | -43.389 | 2026-07-03 11:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0da9f05e-c50e-3783-87b8-01bc7e5a7f54 | -13.35409 | -42.4355 | 2026-07-03 11:30:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 91dc276f-40ac-32b1-9b16-e92828dd9111 | -12.77482 | -44.5335 | 2026-07-03 11:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 82c243cc-36c5-3a46-9d61-4101fcf0516d | -18.14019 | -41.97427 | 2026-07-03 11:30:00 | TERRA_M-M | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| cb258e8c-2737-3803-9a07-630e2e618e51 | -12.77031 | -44.5266 | 2026-07-03 11:30:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 64e2a6cd-fc4b-3842-92c2-7a980a7ad2f9 | -17.60174 | -46.48457 | 2026-07-03 11:30:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 33b81293-4276-3191-b473-0905a178e9fa | -11.92476 | -43.37954 | 2026-07-03 11:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8da52dc7-7dfb-3530-ad3c-336bafe74f5f | -12.20176 | -43.8784 | 2026-07-03 11:30:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d11b92e8-0cec-3ed7-9ce1-de905ed5c00e | -10.44283 | -46.41006 | 2026-07-03 11:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 964758be-b9b1-3413-a7cf-d82c8cbde4eb | -10.93919 | -43.04914 | 2026-07-03 11:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 71b877d1-26a7-37a9-8969-19e0d798ae64 | -11.43624 | -46.5463 | 2026-07-03 11:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| bc0f9005-60a9-3a88-a609-b43a328f167e | -11.43854 | -46.53157 | 2026-07-03 11:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d8ced3b4-259e-3595-a020-729e58fc3f8b | -11.43904 | -46.53857 | 2026-07-03 11:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 884339d5-4ddf-361e-90fd-78ae9cef5401 | -12.50981 | -48.25255 | 2026-07-03 11:30:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e9a4d67c-6043-3035-b85d-0ef9f3f3196c | -10.94818 | -43.05047 | 2026-07-03 11:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b4ac357a-a255-3791-9255-697bacdc0b81 | -18.14149 | -41.96467 | 2026-07-03 11:30:00 | TERRA_M-M | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 0db2ffd4-6967-3ea2-b621-060c87c589ca | -21.11569 | -49.00127 | 2026-07-03 11:32:00 | TERRA_M-M | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 10162347-47fc-3c4f-a316-6f2edf3c0bc0 | -5.8132 | -45.0573 | 2026-07-03 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 5239b509-638b-3bb5-85b1-a4a8edb0aa79 | -5.7945 | -45.0586 | 2026-07-03 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 371.3 |
| a930a37e-2683-3bbf-9f31-62d3834e6f09 | -5.7947 | -45.0359 | 2026-07-03 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 92447524-d8e2-346f-ba0e-f693a36e3a04 | -5.7758 | -45.0599 | 2026-07-03 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 12d3588b-62a7-3db2-8a86-4efafc079a7c | -5.7943 | -45.0813 | 2026-07-03 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| e40f21af-b6f7-3cbb-9d08-5a1e2c0a9ac0 | -5.7943 | -45.0813 | 2026-07-03 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 6ae636ff-4b52-321a-85a2-c125c7b54743 | -5.7947 | -45.0359 | 2026-07-03 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| c1ab64e8-c29c-3aed-a767-2330fca779a7 | -5.7758 | -45.0599 | 2026-07-03 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2c054a3d-c9e6-360e-8682-bc39be9a6a3c | -5.8132 | -45.0573 | 2026-07-03 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| d9fce616-24d9-31cb-abe6-dbcf964a9c1d | -5.7945 | -45.0586 | 2026-07-03 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 439.0 |
| fcca542b-b86e-33df-8f7d-cfd4a6999111 | -12.5138 | -48.2581 | 2026-07-03 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| eb925e52-916f-3035-8c14-eb083592433d | -5.8132 | -45.0573 | 2026-07-03 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 362f78a3-b111-3a5a-a32a-6843c6afeba6 | -5.7947 | -45.0359 | 2026-07-03 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 6fe8a4ad-f512-3fb4-b525-1849503fe12f | -5.7945 | -45.0586 | 2026-07-03 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 345.7 |
| 5acb6dff-e809-3435-bf83-f86c0d620b1d | -12.5138 | -48.2581 | 2026-07-03 12:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 230f06be-4477-3590-9a74-4f2748f3b848 | -5.7943 | -45.0813 | 2026-07-03 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 08c04b6a-dee8-31fc-9ae7-bdd2e23a6786 | -5.7943 | -45.0813 | 2026-07-03 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| b3b2f253-d9eb-37a5-9c9e-2d1a594e6cb1 | -5.8132 | -45.0573 | 2026-07-03 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| da21522a-b658-3b7c-93b4-287034dbedcb | -12.5138 | -48.2581 | 2026-07-03 12:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| a0134036-b70e-3bb6-96e6-184bdd3ef88e | -5.7947 | -45.0359 | 2026-07-03 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e18fb4c0-c17b-3bc9-b0b1-fe7fc85cc7ea | -5.7945 | -45.0586 | 2026-07-03 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 364.7 |
| bb41a187-050e-3dc2-99b3-85deef6322f1 | -5.7947 | -45.0359 | 2026-07-03 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5bed811d-8834-332e-87ce-bde4854b8422 | -5.7758 | -45.0599 | 2026-07-03 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 6db8811b-fd9c-3819-ba55-2216bf69cc4f | -5.7943 | -45.0813 | 2026-07-03 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9ab70d33-02c1-3de6-9ee7-716573007706 | -5.7945 | -45.0586 | 2026-07-03 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 304.7 |
| 66dda5f3-7a53-33d5-b32f-7ecf54fac68f | -5.8132 | -45.0573 | 2026-07-03 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| b87e2ca5-cd2d-312e-94eb-45bd53b42a6b | -12.5138 | -48.2581 | 2026-07-03 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 2e3c861e-3bdb-32ef-be16-b28ec19cc68a | -5.7943 | -45.0813 | 2026-07-03 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 20d4e0b7-e2e2-304a-b67e-134cd2ad5a8a | -12.5138 | -48.2581 | 2026-07-03 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 29129994-7347-324e-9ee3-0861b62d6a42 | -5.8132 | -45.0573 | 2026-07-03 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 99610a42-e61f-3d71-9aa6-b4b586ae8667 | -5.7947 | -45.0359 | 2026-07-03 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b56e4499-1a06-36f0-b37d-162a56c63d72 | -5.7945 | -45.0586 | 2026-07-03 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 301.4 |
| 4d0c4c7f-14f0-32b6-834b-253ca51080ac | -5.7947 | -45.0359 | 2026-07-03 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| eb0a29eb-751c-3492-8d08-3e0b99f39b57 | -5.7758 | -45.0599 | 2026-07-03 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5e7d4449-6415-342e-82db-11af452f4c7c | -5.8132 | -45.0573 | 2026-07-03 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| ff41c5e8-54f4-3fb7-a637-e8a8a68f478f | -12.5138 | -48.2581 | 2026-07-03 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 186.7 |
| a5737028-40de-3c58-bfef-1a125c7e75bc | -5.7943 | -45.0813 | 2026-07-03 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 71cd5a76-f043-3864-a45e-a625e330b84f | -5.7945 | -45.0586 | 2026-07-03 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 5e4c5db4-43da-3af5-9711-62e3b3a4aa5e | -5.7943 | -45.0813 | 2026-07-03 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| dec3f15e-19e9-3d8a-b8e6-2c0e386d416e | -12.4947 | -48.2607 | 2026-07-03 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 21394a6b-ecce-3a24-b8b8-ad7907b56e79 | -5.7947 | -45.0359 | 2026-07-03 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| e754f05e-fa68-3416-84d8-4ca5e75a454c | -5.7945 | -45.0586 | 2026-07-03 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 260.0 |
| 8d487abb-f575-3482-8f9d-bac19e7a9b6e | -5.8132 | -45.0573 | 2026-07-03 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d1eab291-1b26-30b8-ac0e-69315f59da30 | -12.5138 | -48.2581 | 2026-07-03 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 0124fbf9-c817-3d7e-b4b0-35eb73abb927 | -6.9323 | -43.7264 | 2026-07-03 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 37ef8b00-24ab-36f3-9840-c120179ddc0e | -12.5138 | -48.2581 | 2026-07-03 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 2cdac08b-3849-35d2-9751-2e9db59779d6 | -5.7945 | -45.0586 | 2026-07-03 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 277.1 |
| b1d6105e-3ae0-3150-8120-8b7d259c9986 | -12.4947 | -48.2607 | 2026-07-03 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5ef769dd-aa25-326d-909c-2d0aca48f4b9 | -5.7943 | -45.0813 | 2026-07-03 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4e429291-64fc-35f7-9a62-853620328038 | -5.7947 | -45.0359 | 2026-07-03 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e286334c-e7c9-315c-a1bb-b4f39c4aff34 | -5.8132 | -45.0573 | 2026-07-03 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d94defdb-734a-3989-8325-8e1c9e86d675 | -9.07474 | -65.42028 | 2026-07-03 13:06:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3e9cc9d-dbe5-3773-acc1-883e57ccef1e | -12.09436 | -57.13315 | 2026-07-03 13:06:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 184a6893-3aa7-3e21-8f2c-bb26f051c821 | -5.7947 | -45.0359 | 2026-07-03 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 905a1c4d-5c5f-3801-a5d1-c2a7f4c781e8 | -5.7945 | -45.0586 | 2026-07-03 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 325d5f46-085c-3a25-9c1e-6f08e3b7209a | -6.9326 | -43.7032 | 2026-07-03 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 8e3df085-2b45-3512-82ac-bcd3aaf674d3 | -5.8132 | -45.0573 | 2026-07-03 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 794972ab-6df9-35ba-b7f0-c505189c2f6f | -12.7553 | -44.5194 | 2026-07-03 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |


[Clique aqui para ver as próximas entradas](README21.md)
