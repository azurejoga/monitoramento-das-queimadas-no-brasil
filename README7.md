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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdab4251-857a-3924-a8c4-a8c95281c824 | -14.82539 | -45.40739 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 559f0a3f-62d8-3bc0-baad-628d9a564bf2 | -12.84106 | -44.71007 | 2025-09-26 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 824f7ca7-dc63-37a8-98bb-fde49ec0d494 | -14.81882 | -45.4058 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce07a0b0-7512-395b-8ece-1cfdd0e417ae | -13.84387 | -45.61863 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d10856d6-0d67-335f-9944-d2a54e995dd0 | -11.67097 | -44.44859 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8e0ba37-995c-3a66-a76c-394d523bfed0 | -12.73445 | -43.46059 | 2025-09-26 03:23:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5736b9e-e631-3352-be53-c98ddef80b69 | -11.68121 | -44.43257 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55d746de-4152-368e-bbb2-292126ccc30a | -11.23019 | -45.61937 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f718877f-79b6-3326-bb91-3bdd96b2a7c5 | -11.23186 | -45.56012 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 3e15b930-303b-35d1-b8d8-56987f907603 | -11.21917 | -45.60149 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dfbfc580-4cf5-3dcb-8a4d-8e7278b2f590 | -11.66657 | -44.45015 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6fc0cd6-6920-3b48-a090-f39fd5270b7c | -11.66179 | -44.47363 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cd0fe81-19ea-3862-9703-f688af14cee7 | -12.73447 | -43.45729 | 2025-09-26 03:23:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 276e3a72-d688-31fe-a482-721193ff70f1 | -11.21947 | -45.63493 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a228913-771c-3e1e-b504-fdf9bc65399a | -10.10096 | -45.31932 | 2025-09-26 03:23:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf90e21c-8b2c-365c-ac1c-926dede3d843 | -11.67316 | -44.45161 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23ee95d8-249d-3f7e-b66b-43308e4efea4 | -14.03494 | -45.49507 | 2025-09-26 03:23:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7c6a002-010d-334f-83f5-552591a13f83 | -11.24129 | -45.62206 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41f361a5-5a6c-354f-a62d-18d2a473e4fc | -11.225 | -45.62927 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6bff3534-ce85-3752-80b1-0260487e75f6 | -11.38568 | -44.94943 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5944a408-a811-393b-8dab-711f0408bb61 | -13.89089 | -43.91636 | 2025-09-26 03:23:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51c03125-afee-3d06-a948-a103d6013331 | -11.42979 | -44.97871 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90325ed2-384b-334e-961f-2e19db9ef5eb | -11.61386 | -44.43856 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 610aa716-e22a-32e5-9ea0-9c7ef60481f8 | -11.00062 | -44.35335 | 2025-09-26 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5c6ba90-020f-3d49-af8d-c860557e445c | -14.82414 | -45.41306 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b22dfc37-ecb0-385f-93a0-10638f8605c7 | -13.88987 | -43.92126 | 2025-09-26 03:23:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a711a3f-a1b6-3ca2-b1c3-08ad571ae7e9 | -11.42314 | -44.9764 | 2025-09-26 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 689f549d-91c8-3cca-ac09-34a8e0a8719e | -11.67632 | -44.45589 | 2025-09-26 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e831d8b-616b-38e8-aa47-b55f84faf8d2 | -11.22856 | -45.61199 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02c02274-8072-31cd-b7e3-64b301e4705e | -14.81947 | -45.4156 | 2025-09-26 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1cf9efd1-4eaf-33ea-9e85-c7c31696234d | -11.23503 | -45.5966 | 2025-09-26 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 65b5aa69-1a6d-3448-b5de-47699fe1ba3e | -18.54514 | -46.97196 | 2025-09-26 03:25:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73ebf938-465e-3db2-abeb-c16bf23915ff | -15.25414 | -46.44381 | 2025-09-26 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92e677b5-ac3a-3730-a7f8-8c837d71cc9c | -14.95741 | -46.76794 | 2025-09-26 03:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 257fb06a-5b08-3971-8380-0687fd115eed | -14.9552 | -46.76292 | 2025-09-26 03:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2905c1a-5acf-35a9-846c-e62a1c54f0bc | -19.7482 | -48.15641 | 2025-09-26 03:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 33b3ff1d-fe71-350b-b6b9-539cf2b850bd | -18.54722 | -46.97129 | 2025-09-26 03:25:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a86a9e7f-48ec-32e0-930f-62ef4720d9b4 | -15.53758 | -44.33774 | 2025-09-26 03:25:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 394aef83-7702-33d7-b8c6-3111a85022f2 | -15.53147 | -44.33629 | 2025-09-26 03:25:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70133f45-c700-3acd-a4dd-8cfb8b139381 | -15.27263 | -46.42653 | 2025-09-26 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3571e873-c98c-3a1c-b104-f7485c2f8cec | -15.2714 | -46.43193 | 2025-09-26 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad59d97a-fc41-37bf-94dc-32f5840f040b | -18.54885 | -46.96448 | 2025-09-26 03:25:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9db115fe-eed1-3b7f-8a15-b6a62a2d5fdf | -15.26002 | -46.45001 | 2025-09-26 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eca54b0e-9d16-36cb-b231-0b7f574e55ca | -21.63884 | -48.06433 | 2025-09-26 03:25:00 | NOAA-20 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2500cc6d-a253-3ad7-8f3d-4e3f44d53ab2 | -14.95367 | -46.76979 | 2025-09-26 03:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 464e974d-5165-3d2f-aee8-b507bb0be54e | -21.65845 | -46.0659 | 2025-09-26 03:25:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a5fc22ee-1f04-3bb9-96cc-9cb609ffa20b | -18.54675 | -46.96505 | 2025-09-26 03:25:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d80022f6-84b2-3199-a2b4-6a0194bd9eae | -11.2599 | -45.5537 | 2025-09-26 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0699105a-abd5-320c-8d7d-9adac282f47b | -11.2603 | -45.5308 | 2025-09-26 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| deb14441-2182-3402-9901-35bb2c7350ad | -15.9966 | -59.4851 | 2025-09-26 03:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9e1be2c8-fbc9-3ff4-bab1-22b114c96159 | -5.7392 | -44.9718 | 2025-09-26 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| b986ef99-2bf5-3fc5-939e-bebaad502352 | -11.2412 | -45.5334 | 2025-09-26 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| a76ed6fd-06eb-39d8-8ebc-fe5a20b1eae9 | -11.2408 | -45.5563 | 2025-09-26 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 290.4 |
| ec854c30-bf0f-38df-bad1-b80531ab8fd4 | -5.475 | -43.0774 | 2025-09-26 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b63d618a-35d8-31da-8386-9ac0bfb2c734 | -5.6361 | -43.9258 | 2025-09-26 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 2f637fe9-47c5-3afe-8d9d-9e5226b78f76 | -11.2404 | -45.5793 | 2025-09-26 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| b89717cc-bd48-3f23-a182-54e0a6c8a601 | -5.6174 | -43.9272 | 2025-09-26 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| cf5604c6-23f6-321c-8003-76d1ccf20a42 | -5.4562 | -43.0788 | 2025-09-26 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a115ed08-102b-3159-ae69-16063fb42154 | -5.4752 | -43.054 | 2025-09-26 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 401039ac-c221-3613-a14c-1079822a4b44 | -5.4565 | -43.0554 | 2025-09-26 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9a136f8c-54b9-3c76-8129-7b6fb5dfc8ee | -11.2217 | -45.559 | 2025-09-26 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 35aed3dd-3b03-336f-9a2b-0baeaaa0fd6e | -11.2412 | -45.5334 | 2025-09-26 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 2012cad2-2a05-3b27-b103-a450c3a69185 | -11.2408 | -45.5563 | 2025-09-26 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 270.3 |
| 80599d0b-796d-3233-8127-b86648191fc0 | -11.2217 | -45.559 | 2025-09-26 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 412948c8-84c7-37d7-bbde-396b72db619e | -5.6361 | -43.9258 | 2025-09-26 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5b0db953-aa88-3556-ab0e-5a5e45a2afc5 | -5.4752 | -43.054 | 2025-09-26 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 674cff13-9442-3c98-b492-ab9c3d6db529 | -11.2404 | -45.5793 | 2025-09-26 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 93f44a31-4880-38a3-97c2-642084d4105a | -11.2603 | -45.5308 | 2025-09-26 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 32145509-0243-371a-b4d7-798ea3e52334 | -5.4565 | -43.0554 | 2025-09-26 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| dd188a21-2406-3ba7-bd03-6d692ee593d0 | -5.4562 | -43.0788 | 2025-09-26 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 7f4fcfc4-6a72-3430-905c-5ba107aa4b3e | -5.475 | -43.0774 | 2025-09-26 03:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4a31338f-f0cb-3659-89d0-4fd2f8c810ab | -11.2599 | -45.5537 | 2025-09-26 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 71864ffb-b212-3734-a14a-f66a82ed78b4 | -21.0454 | -51.1205 | 2025-09-26 03:50:00 | GOES-19 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.4 |
| 318cc836-a660-31e2-b297-24d8e036b82c | -11.2217 | -45.559 | 2025-09-26 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 779907df-c705-3f82-8ea9-ed4c1522beb5 | -11.2599 | -45.5537 | 2025-09-26 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| b3f58d0d-998a-3055-8b8d-c2c8ec5b4421 | -11.2603 | -45.5308 | 2025-09-26 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3d895e8f-b66c-356e-9207-af6c5ed67f45 | -11.2412 | -45.5334 | 2025-09-26 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| d158896e-3040-37d5-8925-e177e346907c | -11.2408 | -45.5563 | 2025-09-26 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 283.4 |
| 43030ded-0bae-3e49-8eb2-828422ee36e3 | -21.0454 | -51.1205 | 2025-09-26 04:00:00 | GOES-19 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.0 |
| 209d1af9-1967-3a4c-81f0-8d6b3d66306e | -11.2599 | -45.5537 | 2025-09-26 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 931c5810-5845-3d77-a482-78a6fa0ca742 | -11.2217 | -45.559 | 2025-09-26 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 302221eb-1fa4-3232-b788-cdacaf09374f | -11.2408 | -45.5563 | 2025-09-26 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 768.7 |
| ba30fc6e-faf7-369b-8db6-e3decdb4cbe1 | -11.2404 | -45.5793 | 2025-09-26 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 98f328bb-cdde-3ec6-a981-b24085c449e5 | -11.2603 | -45.5308 | 2025-09-26 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| ce42a858-16fa-3445-933b-f7462fa34947 | -11.2412 | -45.5334 | 2025-09-26 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 298.5 |
| da5bfeca-58c2-38b3-9691-d8f7f68d5679 | -21.0454 | -51.1205 | 2025-09-26 04:10:00 | GOES-19 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| a93f94ef-0482-374f-bfe3-16a1ebd3f4b5 | 2.64528 | -51.01184 | 2025-09-26 04:12:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03ed1159-0b8d-3c0f-a276-2f4c5be2f346 | 0.07413 | -51.05922 | 2025-09-26 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 326e210a-9df8-33e5-9fa1-c758a7fc2951 | -2.30596 | -48.14598 | 2025-09-26 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cd768db-8014-35b9-bc17-d8f13ce202dc | -3.41638 | -41.60474 | 2025-09-26 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c08147e-34bf-38d1-884f-91a6218a6004 | -3.30816 | -42.16833 | 2025-09-26 04:12:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 362faadb-69e8-3771-b38c-cbbabb017e81 | -1.37128 | -47.16463 | 2025-09-26 04:12:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ece8230a-9bb1-366a-a06b-8100d1387a01 | -1.19312 | -49.18196 | 2025-09-26 04:12:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdcefac0-4679-337a-ad96-56b94d541ff0 | -3.62964 | -38.76725 | 2025-09-26 04:12:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7ad979ff-d29b-3ae6-962e-df6973807e14 | -2.3784 | -47.71515 | 2025-09-26 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7390d09d-5e86-39fa-8a65-8042955ce22b | -2.30219 | -48.14622 | 2025-09-26 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 824c64ad-1f55-36a2-afa7-a0701b1cc031 | -2.3017 | -48.14532 | 2025-09-26 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0353ae83-001e-328a-a764-1f8caf3e5b60 | 0.69103 | -51.46265 | 2025-09-26 04:12:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 257a0099-d232-35d9-9ab1-8f5a2020ebcb | -3.82582 | -40.34589 | 2025-09-26 04:12:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9cc56701-51c8-397f-9640-1fd618ae772f | -3.16871 | -40.62145 | 2025-09-26 04:12:00 | NOAA-21 | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
