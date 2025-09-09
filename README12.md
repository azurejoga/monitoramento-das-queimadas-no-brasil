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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e77072f-cbff-32f0-aec1-45239800078a | -9.34891 | -46.59632 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d9d73de-2752-3e86-84d9-5adffb39a676 | -10.97414 | -45.09634 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 05323339-2fe6-3120-9e0c-3c1c0917535e | -5.72343 | -45.4052 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59af8fb2-9feb-37c9-8405-0d0f9572cfba | -11.37424 | -43.52836 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e484a771-c5ec-3635-9178-c634b38281d2 | -7.24808 | -44.81974 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45bc26ed-f4bd-38c3-95cb-14f8e30fd62b | -7.08798 | -44.15113 | 2025-09-09 03:42:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cd277e7-3774-3dd0-909c-ba05af630832 | -11.41189 | -43.66272 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d26595dc-9c76-3104-a1be-5b956f6f02d9 | -6.56354 | -43.14535 | 2025-09-09 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bd772a1-63e6-3a4a-b7a4-c497428790e1 | -10.17873 | -46.22824 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be4d6f7a-993e-3a3f-965c-842fe76cf489 | -8.03978 | -48.63546 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96c06e16-8c63-30a9-a661-d4de81561c98 | -11.37796 | -43.53408 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f64a9494-29e9-3b50-94b8-887c0283b975 | -8.02507 | -45.50739 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a06d9a99-db2a-32f1-9ba1-55bb99923ea9 | -11.43288 | -43.59991 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 233aa6d2-63a2-307b-be81-9f594f8c2236 | -7.18581 | -44.90825 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96b7b76e-079c-3934-9b5b-88c8d0edb0e9 | -10.97355 | -45.09955 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 6d8a5700-adfd-35de-ba36-cb01c6ce0eab | -7.56471 | -44.65936 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93936083-f3d5-3dda-a99c-d9671abb0429 | -5.84888 | -44.201 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df62ebdf-1e04-3734-b4a3-847cad1ea657 | -6.18408 | -44.73942 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cbebb2b-33ca-3928-b272-b112a4406a73 | -9.44174 | -46.73903 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05d831bb-ab03-3d60-92da-99abeada3a31 | -6.43357 | -44.06792 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b68d2a5f-14a8-3e45-99ca-6dfb6f488601 | -11.03459 | -45.93887 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a97e8477-d010-303a-8ed5-a7e06dd33ac5 | -10.96485 | -45.11781 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 02872e96-6e2f-3aed-8eae-9eeb7c1ab73f | -8.21411 | -44.77061 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80bce848-ccdc-379b-98ba-3f31fe52cd34 | -6.86523 | -45.59784 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 943d9285-2e4d-394e-95fb-8caa92e50fb6 | -8.18693 | -44.76944 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf65471a-be79-370d-925a-b706ee82e56c | -9.4956 | -48.2863 | 2025-09-09 03:42:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cdbff8a6-4f2b-3684-b65c-d35c059be2f6 | -9.8171 | -46.03003 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f867dd0-6789-3142-897f-3aa69cc19d7b | -6.1828 | -43.38957 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51c941cf-9564-3bc1-a94b-421063b1d038 | -11.41332 | -43.57581 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b6ba042-ebd5-3c7b-a7bb-029d255b4c97 | -11.43663 | -43.60571 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b58f8d45-6ad0-3371-9e51-384aa1a2d384 | -6.20175 | -42.46957 | 2025-09-09 03:42:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 142eeb87-32e4-33f1-a0ba-80d787cb396d | -11.43199 | -43.60483 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 63997409-f7bc-3bf1-bd7b-5003476b342c | -5.69298 | -45.9804 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9150ee52-4bf3-3871-aad3-5c60faf5c3be | -5.88235 | -43.95148 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64d9fb7f-d390-3885-89eb-5f7ea41c7980 | -11.42184 | -43.60794 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd07c1e4-7c2f-304f-9400-45d0804cfc34 | -7.27922 | -44.56757 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80a1511a-4c87-3967-92fe-1d1878e11f7b | -8.03629 | -45.50912 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb86756e-7f7c-36b5-b795-29ec50dca0f9 | -7.87582 | -46.25246 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3f46254b-f744-38a6-b7e3-f9779008ca46 | -6.19072 | -43.3733 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef655824-5a62-364c-806d-2ba30ed2d5c1 | -5.68494 | -43.90797 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83300b94-814e-318e-b475-ce9adaab2c83 | -5.68439 | -43.91111 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2656ab5-bb93-38bd-8b81-20a7cb3d5094 | -8.05782 | -45.51766 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b22d0b3e-1d96-391b-91eb-c46aafde4b33 | -7.08142 | -45.2042 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5777d3fc-7983-3915-a208-4231d0cbf856 | -9.79357 | -46.24352 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9ddf29f-befb-3d37-ab4b-57ac74cce72a | -6.43411 | -44.06485 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d29e5af-3d4d-397c-b125-541be2be9e9f | -5.81877 | -43.97471 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7df72850-7c5c-33fd-a73f-6c35d36e43d0 | -6.62127 | -44.01035 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f9dcddb-64b4-3903-945d-a315a18e70b7 | -7.79352 | -46.08277 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d3c23d9-02e4-3015-8844-27a321b98bc6 | -5.83796 | -44.21053 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61b08f5d-c10b-3459-b376-175a654c6ae5 | -6.05681 | -43.31512 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 21a09ee2-d815-33f4-a43f-71a202f390fa | -5.93354 | -42.77378 | 2025-09-09 03:42:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 521c8936-2dfa-38cb-b898-6ca9eb3381a7 | -5.73218 | -45.28451 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7e562d6-03e8-3c09-b3b3-ab99119bc9ba | -7.19975 | -44.89304 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e64e1b78-4009-3525-83b6-4abaa5187b55 | -10.74531 | -48.18115 | 2025-09-09 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 25df7aff-81f4-3d39-9d3b-d48ed4ff0043 | -6.19331 | -41.03293 | 2025-09-09 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e5c75c34-26ec-3346-a808-fc6c3fbb62e3 | -11.43808 | -43.6905 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08aff1d7-aad9-3bc1-8f82-566f380429fe | -6.09631 | -44.14536 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66cb511c-2ad9-3603-9d92-2b8580d55aa3 | -7.80149 | -45.20841 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d068f68f-3634-33b4-bd62-f3e26d69eee2 | -5.57256 | -45.04862 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 78729baf-3f79-3b53-9eb1-a4df7aea3a16 | -8.35766 | -42.2332 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6d00b5b5-9455-3a34-aeb1-ccefef77b7d5 | -10.9795 | -45.10264 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 5cacd8a8-5411-376d-bf71-f564c696c098 | -10.97371 | -45.10495 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| cddc7bf7-f7c3-3e21-b026-8d90f8960a11 | -8.21782 | -44.77105 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b9926a8-584c-396d-abb2-a33b6a8b2af2 | -6.20239 | -43.39465 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44c2a595-36d8-3a90-af1e-0cfb23f07be8 | -9.79153 | -46.24313 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00ff6297-b9cb-3f9d-bdfb-98d9ea03833a | -5.54688 | -45.18166 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4e5c3a6-f982-3505-a605-ce55ad930d85 | -9.43022 | -46.73535 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d463f447-847d-35eb-85a6-8c161403edaa | -8.00718 | -46.35357 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44e271b9-6942-311f-9dcb-9fe5e06b922e | -5.84595 | -44.18671 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65ef1393-6873-36c9-8c04-0f4476945c87 | -9.08803 | -46.97832 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3721c142-f506-3897-beeb-497b71fa255e | -8.06336 | -45.5189 | 2025-09-09 03:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6c42ba9-52d8-3ede-a382-5676bdb5e8a4 | -6.0969 | -44.14203 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a876a33-53d3-3e79-bf66-3731fe186440 | -5.80886 | -44.84356 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2224d156-d3bc-35e4-a24b-fe9df597fafb | -8.37529 | -45.02705 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17f4a5dd-92f6-3a6c-a1c5-3fbed9c0575c | -5.83999 | -44.1894 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8b5be90-e071-38ac-8698-ed763d843e11 | -9.81845 | -46.03417 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fade40a-4e0f-35bf-bf4d-0f0e847f584b | -5.81763 | -43.98125 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cfa7414-9577-304b-a7d6-3ec88882f232 | -5.48014 | -44.1255 | 2025-09-09 03:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ab10e24-b4fe-30f1-b4c9-f59f6edef88c | -5.93648 | -44.89242 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25caef88-c71f-3dab-98c8-8dc1760a2158 | -6.17795 | -44.74207 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95be29e5-0f8c-396c-ad88-4498828ad4da | -5.84925 | -43.86109 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79d15e48-a77c-3221-b677-b4be91bcc806 | -5.66792 | -45.31411 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f18cfaf-4c0f-337c-91b9-d527daf69078 | -9.1425 | -45.57456 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0372f1b3-3ddd-34ff-8ff5-120a8bf36da9 | -5.6922 | -45.98479 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4364f887-6c9b-34b8-a6d6-618ad1836484 | -5.81298 | -43.97693 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36ca32c3-3809-3208-bee7-0e9ab568a217 | -10.97555 | -45.09532 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 41402a8e-85d7-3bc1-9c96-27f312470425 | -5.73288 | -45.28046 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bc71431-b6fd-3af0-95c1-fea5ef95a719 | -8.36132 | -42.23848 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e014a517-2f37-362c-88cd-f907656d4d46 | -11.41371 | -43.65266 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d6a0eb1-a4d2-3563-a1f1-4eda4a78d79d | -5.88727 | -43.95234 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d71b216-1a10-3157-b0c5-41611bc7938f | -6.43044 | -44.05526 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb0a6f4c-b07b-31e7-9163-8371e2978b5d | -5.58104 | -45.05122 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d6a7316a-2ccd-3540-98b8-57e4c377539e | -6.86976 | -47.91033 | 2025-09-09 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 540430d7-3ff1-36df-bc55-39cfda9e30db | -6.86287 | -47.91071 | 2025-09-09 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7776cdfb-44bd-3364-8899-323537e3a2ba | -8.06631 | -48.6431 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2b667019-d5fb-348f-84b8-a115584f258a | -6.08466 | -43.36107 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10451387-2116-3fd1-a305-d8e1d4e82379 | -8.05714 | -48.64397 | 2025-09-09 03:42:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1cc988c-cea6-3616-879e-c33290e90043 | -7.46943 | -45.19487 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea37367e-9dfb-3cf7-997f-48f193329d3b | -9.70592 | -46.82457 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f0d9aca6-5a56-3717-9442-bd64a905ce80 | -7.99715 | -46.34187 | 2025-09-09 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README13.md)
