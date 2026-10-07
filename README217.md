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

## Dados Diários - Página 217

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4ce8c8b-f108-3f53-9183-a341658dd841 | -6.40187 | -52.72141 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f31a0715-2527-3e0d-8fc9-6353c643de13 | -11.2269 | -47.81785 | 2026-10-07 16:37:00 | NPP-375 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fab08ed9-4fc8-309d-99e9-e37097738e6b | -5.93491 | -53.48424 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4ce18948-6943-3104-b14a-c16cad747c94 | -11.14724 | -46.12424 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a9786455-7d26-3df8-acb2-3cbf00bb0b71 | -10.77507 | -46.54151 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 293f9d80-97bb-3d55-9c07-ea58446da07f | -10.0778 | -45.98003 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 04f974d1-07e7-30a1-a801-ce35ae5c7799 | -3.76831 | -41.72182 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| d6010cb0-5ede-3cdf-b68e-ef299fb5f0d4 | -6.15696 | -53.30886 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7caf5c6b-6d9f-3177-bc21-91ecd57bf227 | -3.74353 | -41.71276 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 644a1872-3e0d-32e3-a763-ece3a767fb95 | -10.87442 | -48.37586 | 2026-10-07 16:37:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 68ed4ba7-1b73-3718-9fe6-c95bbb68e5f9 | -11.38396 | -46.69113 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 1495cc08-9ca8-31a9-b322-3d0b09f173e5 | -5.80082 | -52.35038 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| efa3b4aa-10e8-3eb3-9ed7-0aed7ac449dc | -6.36873 | -55.46995 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| af8170ab-02ae-3a41-a057-d801c03b0954 | -6.63486 | -43.77556 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1856dc03-f267-35bc-bf46-51da155cc38e | -5.74591 | -43.27966 | 2026-10-07 16:37:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9a2adc11-8a5f-3b3b-9ffa-718cffdd154f | -11.16053 | -46.11393 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| b0bbde16-e668-31b2-b6b6-aa5bddd50d1e | -5.17551 | -46.27282 | 2026-10-07 16:37:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2493f5c-b109-3054-a6a7-7b92bc5211a3 | -5.50296 | -42.84379 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| b97ded30-0ebc-3c4c-a1a2-c66a97fa9514 | -3.32985 | -44.5803 | 2026-10-07 16:37:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 95753420-5099-3b1f-874d-041ea6a47ec8 | -5.75956 | -42.04462 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| fac9a205-973f-3eb9-862e-6629e38ad60e | -3.76026 | -40.82792 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1ef305cd-2cfe-3c78-833e-2b99e5c3ab47 | -6.59908 | -47.40465 | 2026-10-07 16:37:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 0e6111fa-c8cc-3ff7-8d81-c04ced782aee | -17.15609 | -46.42134 | 2026-10-07 16:37:00 | NPP-375 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3e246477-fee1-3c7d-a93e-64c3476c4463 | -8.02721 | -47.96316 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 44de86f5-1f99-3bd2-acb3-a0497d6f8f6d | -15.1789 | -41.58455 | 2026-10-07 16:37:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| bf9dd246-e9e4-3ada-88bd-1d6872ab1f93 | -10.80257 | -47.31487 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 02b30f74-6a93-3aa4-8c45-fdac7f13011c | -10.34307 | -46.24756 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d3ae0489-d160-3698-b612-c25f459de275 | -9.17245 | -36.04616 | 2026-10-07 16:37:00 | NPP-375 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 137a8858-2b6b-3367-832c-4aa5b5816ea5 | -7.7684 | -43.80725 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 8c894a21-7cd9-3244-a63a-ff4e2de8a2f8 | -5.21805 | -48.33922 | 2026-10-07 16:37:00 | NPP-375 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cf21fb70-5c19-3c86-9a0b-45fd4953c2c8 | -5.93663 | -46.63732 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 36720c70-29a4-3560-962a-f8ac80b660ed | -5.75912 | -52.01471 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| dc84e6cd-8f18-31a9-aaa7-dd8dc384ef33 | -11.14298 | -47.30225 | 2026-10-07 16:37:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c49be7fd-3db1-3ddc-9b61-7cca30aa46ac | -15.97153 | -44.87801 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c7646498-d620-3ec6-ab1f-b2cad919a509 | -3.95247 | -41.54693 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 96b8793a-205d-3289-8c41-b306b808c03b | -9.93247 | -46.95436 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| efcd4de0-b530-3b7a-b63d-af314ce0b9e5 | -7.75881 | -43.80609 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| ba48c27f-652f-3360-a5ca-16f8dc871025 | -7.55836 | -47.78329 | 2026-10-07 16:37:00 | NPP-375 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7792ed3c-2a48-3b88-8fcc-cf958e2caa1b | -4.70829 | -41.9151 | 2026-10-07 16:37:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| a8a0f4ea-59d2-3272-9a2d-5e8bedf127fe | -10.81271 | -48.7674 | 2026-10-07 16:37:00 | NPP-375 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1750e190-180d-3ccf-aed9-fd9f3d0907ee | -7.22078 | -44.29374 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 170d7062-dd7c-3264-a6e8-c2cdbcef7b9b | -17.02304 | -45.91795 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 818b98a4-0a9e-3d64-9c5e-30d08b6ae6f7 | -8.78632 | -47.57556 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 287c83b6-384c-3611-8345-2799e93ec8aa | -6.23317 | -46.00323 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b338f7e1-0059-3725-981b-4787b2b94b56 | -5.4851 | -41.40035 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 549f9983-173b-34a5-ae90-db1b58a4ed9c | -4.58623 | -40.29045 | 2026-10-07 16:37:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6601eb8c-e28b-364d-8601-890120127310 | -9.53415 | -46.85446 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ec1d88ba-8fd3-3293-ad63-b8069ca5493d | -8.25542 | -54.72763 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4f43688f-b746-3cfe-a4c2-be748d17a684 | -9.13723 | -45.09934 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 0c0f9432-791a-3cff-b689-aa42fe821a00 | -6.58726 | -44.19474 | 2026-10-07 16:37:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4c3fba4e-e72b-390e-83c1-ad83995e08d3 | -3.6794 | -45.1224 | 2026-10-07 16:37:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dae67c2d-755d-37f7-9678-f247ee9e519f | -9.9193 | -44.80389 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fccaac49-cd7e-3642-843f-b82b9f35d8cb | -6.98343 | -43.29487 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b0a75e5a-ecd5-31eb-bc05-466efe8c5d8d | -6.92515 | -43.66458 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 2881db63-9058-31b6-ad36-596e6fb28a3f | -3.80693 | -42.26088 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 222a1d4e-63aa-31ed-8518-9df6953dfa18 | -5.45985 | -45.58874 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d33ceab1-d416-3227-ae86-febcc9d7f17a | -3.47794 | -39.48421 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f40f873a-91ad-34bb-987e-d893bedb4836 | -6.3701 | -55.15924 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f9864564-3b24-36f9-ac98-63eaee93768c | -11.09141 | -45.6549 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4852f0ac-ddcd-3775-8b9a-37e9fd1bd52a | -16.19069 | -44.56916 | 2026-10-07 16:37:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 115c2aa1-ccc6-331e-ab25-ffc9f4b38657 | -9.20285 | -46.69189 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 6515f890-4249-344a-90ac-84ea3760c9c4 | -6.69485 | -44.92466 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c7bb3f54-82b6-32a1-8618-9d648652f5ab | -8.35171 | -45.48716 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 89db0272-9e93-3944-8f05-8add3e826245 | -10.88347 | -46.67992 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 12e82915-339f-333a-8fe5-12e3359dedb6 | -3.69548 | -40.85918 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 720149e4-bb7c-314c-b290-918571df987f | -7.46351 | -42.99075 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cdcf58e7-de1a-3f10-9af5-ccf5c1962498 | -10.49619 | -47.2946 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| c61e2c6d-b370-3b7e-afe7-98b0405dbd99 | -8.05294 | -45.61226 | 2026-10-07 16:37:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 14f936a9-cddf-3284-a01d-584d2bc48be5 | -6.4669 | -55.46379 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| ba1b8b99-5477-3c74-8dc2-c01b3b55e35d | -4.05246 | -42.21529 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| d721af24-cc07-3ef3-b945-2e56a315805d | -6.14771 | -51.69793 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 60439ac1-9fe7-3a59-819f-fc303393bc6f | -10.79872 | -47.31542 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 6947e177-2fb4-3482-84cf-3bfa148d3d9d | -11.11305 | -45.70497 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b29be364-2a78-3693-83b4-ad432f844c2f | -9.03745 | -46.91081 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7f53840f-cb0d-36c5-99f8-81b8d68c02b7 | -3.95244 | -41.54297 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| fcf79297-0a1e-3ef3-963e-e3a083c5b2ba | -15.11792 | -43.62909 | 2026-10-07 16:37:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 03e33b9e-aaca-38a4-a873-02bdda22b2d6 | -8.59723 | -45.68901 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| dfdfff2b-d82d-36ad-a0c1-0d3f49dd8fba | -6.36339 | -55.1556 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96ecb6fe-87fb-3fd6-b8f3-cfa380739c1c | -5.57466 | -44.38063 | 2026-10-07 16:37:00 | NPP-375 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bba52654-21c3-3b20-8408-36f27617338d | -9.88577 | -44.83516 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 99822fde-988c-39d1-9234-45146e5d45ed | -7.71605 | -49.97261 | 2026-10-07 16:37:00 | NPP-375 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3e51b4f7-94c4-360f-97c7-95c7cf412213 | -5.78258 | -52.36099 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 066eceb4-3e41-38f1-a2d5-ce839293f533 | -5.26543 | -48.03658 | 2026-10-07 16:37:00 | NPP-375 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f82d9c8a-a5bb-31b8-ab78-1ac2a4d89bb4 | -10.34668 | -46.24706 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 03d04040-efbc-3c84-8adf-5dd3bb351462 | -5.96762 | -55.3584 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a27f0193-4383-3010-88d7-9ff76dbcae5b | -5.65764 | -43.16375 | 2026-10-07 16:37:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cfd9ce34-fc37-3a8f-92cf-ea44d67d63b9 | -6.29405 | -44.90877 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 22ee9319-800f-3d5a-83e8-4802f5d8e555 | -7.17158 | -43.77145 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 13c1d24c-f6cf-3c76-960a-f1b0a0039dca | -7.83449 | -45.50116 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8b7df7f5-2f83-31ea-af18-3b3d6fad423d | -16.02824 | -48.24302 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 58112787-e625-399a-9e64-9fd781e1bdb6 | -5.61117 | -39.27113 | 2026-10-07 16:37:00 | NPP-375 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 77e7a3fa-fb66-374b-a2e3-fb5e4e00ca67 | -16.19423 | -44.56862 | 2026-10-07 16:37:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ed6fd306-fb2f-3ba6-a924-23dd0f61402f | -7.09176 | -36.08542 | 2026-10-07 16:37:00 | NPP-375 | POCINHOS | PARAÍBA | Brasil | 2512002 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2bb877fa-cf1b-3caa-a209-a00a3579b81e | -8.53807 | -47.5304 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cba49dfc-4d1b-34bb-94c3-d98eb2ef9354 | -5.99904 | -44.12838 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 01d00e13-7df6-36ed-96b9-032166ec1263 | -10.6333 | -47.33514 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 329b86dd-077b-3e13-8f85-34c07c5c3b01 | -17.19414 | -43.51778 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e3d47b9-94f2-373d-8ff8-aaf5bb99ea59 | -8.16917 | -36.67448 | 2026-10-07 16:37:00 | NPP-375 | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| fc2074a7-b1bc-39c4-a27f-584915363dfb | -4.03339 | -46.98352 | 2026-10-07 16:37:00 | NPP-375 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 6b9e0016-80fb-311b-8ec2-38fd4678b4c4 | -11.39567 | -50.88964 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |


[Clique aqui para ver as próximas entradas](README218.md)
