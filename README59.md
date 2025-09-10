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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a431a173-0610-3e86-9112-e3da28cc9f97 | -8.06357 | -52.33029 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbb31bed-a884-32ed-a687-8ce95e27b884 | -8.8635 | -45.85473 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7d0693f-5d96-3229-badd-871d4711c7d6 | -9.01059 | -46.05645 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73b91811-89b7-3013-bcb6-73bd5fd9130d | -5.47991 | -51.22488 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b87b763a-dde4-3186-84c5-5b2ce744f616 | -10.14827 | -46.17468 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31f2bc61-59ca-3901-ab94-8ddd0dd5f35b | -9.34747 | -46.7529 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b556ccd-103c-3138-ae71-1e9f9e8ce20f | -7.74438 | -50.72717 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a08f24-2828-3ab3-afe1-eb1eb315393a | -7.30881 | -44.15608 | 2025-09-10 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccab7afb-b0d2-34e2-b9c6-57a7435b5c3c | -10.72358 | -48.2889 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31747821-bf90-36f9-9ff5-cfebb78caa82 | -9.51996 | -46.54628 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bcde4dd-27ed-316e-b161-4529d277d1a4 | -7.66653 | -50.26683 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e1d13ca-c59c-3e22-8f4e-cf19a55e9918 | -11.47456 | -49.26682 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44536bc2-3624-3ece-8445-edab37cf72ae | -9.51321 | -46.54067 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36c7b791-c3be-3c81-88b5-5c04aef9f860 | -11.12072 | -45.11895 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23abd32c-90fc-300a-b0dd-2ddbd6f06d30 | -11.95152 | -46.64854 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f66a5c3-de61-3cfa-b62d-6b0826c750e2 | -6.38286 | -44.45285 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02d77589-d680-313e-b413-dfbdd555ec2d | -7.80124 | -46.06704 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 079ad749-41b4-3c9c-b741-0644570bc6fd | -9.55489 | -48.30021 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec59738b-3e51-3c00-9dad-1d5bb5fabb55 | -10.74715 | -48.91608 | 2025-09-10 04:42:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bde013d-169c-3b4d-a403-1af4f11a208f | -11.66773 | -46.90845 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5fbac7a-0680-38e1-b54e-93c1b3bb9a27 | -11.85084 | -46.76343 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c816120-2180-3569-99c7-4fff9be1c0a3 | -10.55185 | -51.51128 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bedeb78-90bb-3659-9931-44c5e8637fe5 | -10.31048 | -48.80846 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27c0b722-a633-3b63-9a53-ee43c49e5f8b | -8.38535 | -45.02815 | 2025-09-10 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b0a0118-036c-36f4-b10f-c34808acd422 | -9.44151 | -46.72104 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6f2e7ae1-46b0-3fdd-96cd-2fcdb9a9461e | -8.52473 | -51.38802 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656c0370-1cd6-3111-9fb8-9a40b3d3adfb | -8.86419 | -45.85005 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d8d5d3d-3d8b-3269-93f5-85235e84bdd8 | -6.61874 | -43.99732 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03164209-6730-3781-b865-1a76d74c4a22 | -9.14565 | -46.05629 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b1a7759-41e7-3bd9-bcbe-ad10f2adff69 | -8.04353 | -48.66768 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 86db596f-96d4-3e1b-9e2e-09dd83d3a903 | -7.3664 | -47.43567 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8c001d2-c2bb-352b-8050-c2262b59e462 | -11.12309 | -48.43384 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95fac7e8-5ee4-3415-8780-9a283eb3a802 | -7.68631 | -44.7653 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd44c35f-8d55-3520-bd7c-cf9dd979e1aa | -6.88865 | -47.88494 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 99f1a09f-0a40-3833-933c-5193ba0098e4 | -11.33488 | -46.52544 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1643cdf-90f2-335d-9ba2-782a92155be4 | -7.5472 | -44.667 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1ddad7c-a93d-305f-a628-e1dc95cfe65c | -11.32348 | -46.52392 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb42e65e-9ca6-3293-85ff-11013d5d5308 | -9.16953 | -45.58977 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c21a3339-fd96-31d4-9492-3bb250b09a39 | -8.05236 | -52.33252 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c71a8a7c-b5e2-3fc1-81a7-80ded8695227 | -7.71058 | -45.1503 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a708362-a0c1-32c8-86b7-a5ba3b928ea3 | -8.4417 | -47.28194 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2df0f445-90d1-3a04-94c0-a3ed158c0952 | -6.55902 | -47.4906 | 2025-09-10 04:42:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 04f68a75-680d-3ecb-b337-38b070966c4a | -11.75189 | -50.62915 | 2025-09-10 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e8bb644-d9bb-38fd-9df2-8018f93919b2 | -10.02147 | -48.09596 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a66bd1e5-bd34-3c57-aa03-88a3605c4681 | -7.75052 | -50.73183 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 857e0a5a-d44e-3be3-80c5-c9ad608d6889 | -8.84763 | -47.26204 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 570cce36-f1df-3a4a-9810-e679afbc03a1 | -10.65398 | -48.61453 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df24277f-145f-3f51-bd7d-f687df1f6047 | -11.14252 | -48.35115 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9190e1d-904c-371d-a163-abd9dadc1630 | -9.079 | -50.46459 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c462bb8c-67a5-3ec4-8f31-dc7b431cab11 | -7.30937 | -44.15229 | 2025-09-10 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e422de2-dfb1-3804-b5ee-02c3d35c7a0f | -7.77166 | -50.77176 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad71723f-2490-371e-8734-042175605313 | -7.70225 | -47.29208 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbe85043-70a0-3b18-ac1b-3e69d651c2ea | -11.44082 | -49.28379 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88dc6ac6-c93a-3dbe-af54-e756818bc3fa | -5.65897 | -51.26817 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 316432e0-c647-31f6-b0f3-536bcc67aff5 | -7.85063 | -46.04228 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3f9f390-2cf7-39ab-bd9c-09674c77b39a | -10.3037 | -48.80733 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a381b7b6-f002-31eb-a097-8b96e73d7e1a | -7.99407 | -46.32513 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a63b4b06-8e09-394a-9f53-0a6738d67542 | -8.42407 | -47.27912 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d575c8b5-9e4e-336c-a3e9-c085d5ec3423 | -7.79881 | -46.07326 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2700aad0-3f57-3a4f-8905-5aa1ddc18259 | -7.34997 | -46.16064 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a78cbd5-2213-3ab1-8ce1-0dc5f9a7944d | -10.74659 | -48.91975 | 2025-09-10 04:42:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24072ee3-501c-3d59-8910-96d483886c8b | -12.08548 | -43.33047 | 2025-09-10 04:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 320f3e04-6375-334d-a526-e2acee5c22f8 | -10.30883 | -48.81924 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 69592a14-99d6-301d-a5f1-b7074d7a129b | -6.18397 | -45.80024 | 2025-09-10 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a318478-ff08-34a7-bd5b-f882cd0ef823 | -11.44823 | -43.62172 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a2958d8-56f3-3828-91e3-bb6b7c6f39d9 | -11.4442 | -49.28432 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3f8dc8a-dd52-3325-bafe-da397f9450fa | -6.22752 | -46.24534 | 2025-09-10 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 634519a4-d8a3-3a64-bd97-4306ce657be8 | -9.06741 | -49.83151 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4a0f774-7e92-3317-b7d5-c9e8777b8e4a | -8.07486 | -48.6537 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca6ff8e1-5f77-3896-a00c-7e58e467461d | -9.06622 | -50.48046 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3c6ae1f-869f-3d1a-b562-4a8eff688c31 | -9.05208 | -50.48899 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7c84a30-89d1-3d7e-b714-bbb27fa4b536 | -11.44132 | -49.25784 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30d3ce75-c620-3dde-ab2b-5c4a3a9b254c | -7.66541 | -50.29533 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ecabca7-b355-3fc9-8df5-fb5ddbc2b80b | -8.84998 | -47.27058 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4907e07c-6665-37a1-96b8-e030a4b56c18 | -11.43619 | -43.71031 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1ddc2d9-8505-38c7-bcfe-7d95095ac240 | -8.00384 | -46.3354 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb347f9e-4844-3e96-a9ce-2233d4f682e1 | -6.56679 | -43.14608 | 2025-09-10 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0938701c-5f65-3d06-9022-0bfba79181ba | -9.06317 | -45.74733 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11a6f1a8-72ab-3473-946e-4a89154b623f | -11.5366 | -47.314 | 2025-09-10 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cefaea5d-7a82-3643-a285-36b6a699653d | -11.19568 | -48.375 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8fa096c-c60a-3bc9-a379-4981f247b7fd | -11.11663 | -48.40606 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a76c68a8-9b3c-3200-a2eb-b50928f12daf | -9.02753 | -49.78897 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c12310e-e03b-3ac9-86d2-63b14d260ca8 | -7.78157 | -46.06133 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b09492f-4c96-3249-9231-be9db25ee5cb | -9.0493 | -50.48496 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a9e0848-9b59-3511-b045-872d88032d78 | -11.46428 | -43.63507 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8bd5f91a-bffa-3587-bc91-f7775811526a | -7.66708 | -50.26336 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bddcc4e-52ad-36cb-8d4f-c5905a614d46 | -6.87898 | -47.87974 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31178bc2-af74-3d75-8f97-0cae4203cbdf | -9.07011 | -50.47748 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f134e5b-93ea-3ffb-84fa-2c922d94f175 | -10.83986 | -47.75033 | 2025-09-10 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1c2aebc-a729-33ba-9010-836726be5d00 | -6.4074 | -44.39916 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96400643-6b45-399c-b55a-10d2adfcc95b | -8.06449 | -50.18691 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a375b941-831e-3f81-b90a-51efb38fc18b | -9.06241 | -49.81996 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f82dbd20-cc6d-36fc-b495-20fdd28b2962 | -5.8786 | -52.15971 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eecf200-ede9-3c39-b1ee-a0df77805590 | -7.73921 | -50.75928 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7494d84-5752-351b-9058-920aa455af8c | -9.13657 | -45.5701 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47061fd3-85d5-39b0-9dfd-7cd3249086c9 | -8.42951 | -49.11234 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2656058-e6ef-38cd-ae8f-bc0443b787ca | -9.04707 | -50.49905 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0fe2ecd-7cee-3d08-a5fc-e7bcca916282 | -7.10921 | -50.76489 | 2025-09-10 04:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e95dc6b0-de3a-35f9-95c4-f1957cd7feb9 | -10.02859 | -51.6572 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c71cdd7e-5306-3b3c-8d74-a0fc20530efb | -9.35675 | -46.49894 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README60.md)
