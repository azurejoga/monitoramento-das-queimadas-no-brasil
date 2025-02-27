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
| 865731cf-48da-3aeb-8b1c-685a02daa170 | -6.95753 | -43.00655 | 2025-02-27 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 53a76e3f-1e77-3f94-965c-3cc1fb9669ef | -6.97115 | -43.00867 | 2025-02-27 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e0259776-9cbd-3f44-a1cc-3e519cc4491c | -6.96775 | -43.00814 | 2025-02-27 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 663febc8-a99b-35e5-8f6b-067839da87b4 | -7.06052 | -44.35213 | 2025-02-27 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15340c11-1177-39cc-bb2d-3966ed3fc9ca | -7.80582 | -44.19008 | 2025-02-27 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ca2364d-a631-32e9-b412-3e371ed402e5 | -4.80586 | -43.0032 | 2025-02-27 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 958f2a7d-0979-3ec9-8d0a-23691b780b3d | -8.11977 | -43.14669 | 2025-02-27 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07c2314f-8b3e-3856-b407-de612888fd5c | -8.12034 | -43.14296 | 2025-02-27 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b9279322-1a44-3045-82e7-8c51ade37266 | -9.8718 | -37.13031 | 2025-02-27 04:18:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fdb29122-2966-3241-b875-b85c929b6e18 | -7.80968 | -44.18709 | 2025-02-27 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 934c59b7-5010-37e9-9afd-be87c869c102 | -5.43753 | -44.02284 | 2025-02-27 04:18:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a9a7661-de41-3924-b20e-195b4c58907e | -7.05444 | -44.34763 | 2025-02-27 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 42593837-ed25-3a5a-9fc1-5e4669e1888a | -7.0539 | -44.3511 | 2025-02-27 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80d6647b-5c73-35b1-a7c4-351e7278b886 | -7.80358 | -44.18252 | 2025-02-27 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25eef729-c9b1-30f1-9631-9766a4873fe3 | -6.96377 | -43.01131 | 2025-02-27 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9aff53fb-95f2-300c-bd34-781a27a4d04b | -7.8069 | -44.18304 | 2025-02-27 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42684d90-4d11-3319-b9ed-8dd1038fd6e2 | -8.1135 | -43.14191 | 2025-02-27 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2c0eeced-96e3-3774-87d1-d04b67b1e024 | -6.96434 | -43.00761 | 2025-02-27 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00d515d7-d156-3b48-a379-da94a1d07342 | -7.05775 | -44.34814 | 2025-02-27 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b98af343-d491-31cf-a7ae-046429bc46f5 | -6.96718 | -43.01183 | 2025-02-27 04:18:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 631480c8-bfd5-3b5c-ae38-5f0b8eef0653 | -8.40183 | -43.84631 | 2025-02-27 04:18:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4a1bf4b3-54d0-35af-a3f0-7b4fc35b1272 | -7.28451 | -43.72271 | 2025-02-27 04:18:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e82fd84a-3f63-3dc5-9666-c49900b3e4b4 | -6.25543 | -43.78732 | 2025-02-27 04:18:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7748efe3-4c46-349f-863c-c4e9520980dc | -8.11407 | -43.13818 | 2025-02-27 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 52e95fce-3efd-3fc9-85c5-03fd5d5bd7ab | -7.05721 | -44.35161 | 2025-02-27 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d7ecfb-bc18-31ad-a008-51a3af657c24 | -6.15942 | -44.42324 | 2025-02-27 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 548cffdc-2320-3b72-bad7-7dd5e634a919 | -7.80636 | -44.18657 | 2025-02-27 04:18:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c8964a0-4f17-3e6c-8fc7-cc8bf2b4af17 | -21.0553 | -47.777 | 2025-02-27 04:20:00 | GOES-16 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3d3d71cc-9de6-3476-ad7b-fe45f1d92c67 | -9.79705 | -41.96569 | 2025-02-27 04:21:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec6b6a95-c810-3adf-96ca-e3db3ec2416d | -10.48822 | -42.42146 | 2025-02-27 04:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e8ec51a-c627-3984-a2b5-b274929042a4 | -16.68112 | -43.88473 | 2025-02-27 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85351a49-a9e8-3a8a-8db8-0c0c966f4dd5 | -16.83119 | -42.86859 | 2025-02-27 04:21:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 455268a7-0bb5-3713-84eb-50060e6c717c | -10.49299 | -40.39231 | 2025-02-27 04:21:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e0dc517-402c-3d04-beea-c7a4812d6da9 | -10.48461 | -42.42091 | 2025-02-27 04:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7330a59c-c9e8-3625-80a1-2780996e1121 | -15.49988 | -44.77501 | 2025-02-27 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 981ed41d-4fa7-31b4-853f-6faefa447dbf | -15.088 | -42.44732 | 2025-02-27 04:21:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f55b3ae0-5f27-37df-9c22-ceeff5b9c851 | -15.82423 | -40.70457 | 2025-02-27 04:21:00 | NOAA-20 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f0f1adff-b637-3d60-8735-e69b64020a8f | -10.49707 | -40.39284 | 2025-02-27 04:21:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 924bb479-5dfa-3af2-8b40-ecf2baad18ed | -15.37386 | -43.71633 | 2025-02-27 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15b6cedf-abca-3a1f-8d3a-6b5e7e70455e | -18.90395 | -45.03858 | 2025-02-27 04:23:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af872593-2169-3e18-846d-4d56763ea935 | -23.50815 | -47.37524 | 2025-02-27 04:23:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a62ab74e-7d52-3d14-ac18-0cba46863c3d | -22.67822 | -42.85489 | 2025-02-27 04:23:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 668d105a-4f3a-3cdf-9f15-b73c7fda401c | -20.69095 | -49.00596 | 2025-02-27 04:23:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bce115fe-beed-386d-b121-3d69ad44d2f5 | -21.17266 | -43.52802 | 2025-02-27 04:23:00 | NOAA-20 | DESTERRO DO MELO | MINAS GERAIS | Brasil | 3121506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f93cb4c0-6fbe-3719-88fe-a23e5ba44685 | -23.40341 | -46.55711 | 2025-02-27 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1628192f-d3f6-30a1-a57b-d7ff1ccd57de | -19.3208 | -42.39209 | 2025-02-27 04:23:00 | NOAA-20 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3bf8ce25-30be-3b53-b174-489a7b25a94c | -17.67624 | -42.74223 | 2025-02-27 04:23:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 216e871c-87c6-36a9-858d-a20c7d3732c7 | -22.64565 | -42.24902 | 2025-02-27 04:23:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 131a41cd-9d74-3fc0-bea8-6798a0bef910 | -22.85124 | -47.62217 | 2025-02-27 04:23:00 | NOAA-20 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c40faeed-592f-376c-87af-b54ebfd52e53 | -18.58652 | -46.58392 | 2025-02-27 04:23:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2bd903c-10b6-3df2-9b36-41472aed1997 | -21.05195 | -47.78254 | 2025-02-27 04:23:00 | NOAA-20 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 35.3 |
| df5caadd-30b3-31a0-811b-f705cd6a7f62 | -22.6741 | -42.85434 | 2025-02-27 04:23:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e8d9eab6-3257-3c2e-b996-104d5ba7e209 | -23.45154 | -48.91607 | 2025-02-27 04:23:00 | NOAA-20 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 030903b2-292b-3c0c-bdc3-132eda98fbe6 | -20.89922 | -43.81774 | 2025-02-27 04:23:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dcd6286c-a54f-3616-8f6a-e3b6c7a237f1 | -22.64444 | -42.24703 | 2025-02-27 04:23:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f089ff3f-a294-3f2b-b74c-c319cf1177bf | -20.00312 | -45.40395 | 2025-02-27 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e0c2cfb-9d63-3bc7-a9e8-0d04fe9f6b91 | -21.04864 | -47.78196 | 2025-02-27 04:23:00 | NOAA-20 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 17f2680d-e823-36f3-b5a0-73890d5fa8da | -20.31284 | -46.73157 | 2025-02-27 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 259dd6a7-6efa-3326-87e7-ef83ed86e2c6 | -22.54047 | -48.81374 | 2025-02-27 04:23:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2219889a-5cc9-3203-ab29-8c6289fd0448 | -21.04806 | -47.78565 | 2025-02-27 04:23:00 | NOAA-20 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 52a22000-0e48-38f5-8b19-aac01579e665 | -20.616 | -47.70398 | 2025-02-27 04:23:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fefd0866-652c-3f01-b4d6-23e5dc2ba1ad | -23.98508 | -48.91652 | 2025-02-27 04:23:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ffe113b-6914-326a-820c-d8c6191a6149 | -23.59368 | -47.43732 | 2025-02-27 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8eb7f14a-477a-332f-ac4b-3d07a242c13b | -23.29797 | -46.685 | 2025-02-27 04:23:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6801fb1-333b-3cc1-9d0a-a292a91da950 | -21.34717 | -48.6455 | 2025-02-27 04:23:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f37d9a6-c3e3-31ce-971c-714f6b9a8b02 | -21.18473 | -48.57846 | 2025-02-27 04:23:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 27edf90b-37d6-3e37-b58c-7fbbb3c6576c | -23.56494 | -47.88077 | 2025-02-27 04:23:00 | NOAA-20 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a6243f4-c756-3a2a-a700-99929a4c309a | -23.33751 | -47.53989 | 2025-02-27 04:23:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| db3f2f0e-8d1f-334a-895d-c7464d9c9a29 | -22.85679 | -42.97921 | 2025-02-27 04:23:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e552be09-0330-3006-9105-ab4467c32668 | -22.95501 | -46.78457 | 2025-02-27 04:23:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0b716a46-f0f0-3caa-88a9-995786d10ae7 | -17.40365 | -48.03685 | 2025-02-27 04:23:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4acd4788-3108-3ee4-a88c-e0412fef5209 | -20.02744 | -45.84051 | 2025-02-27 04:23:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bbf6a66-4ee6-3dfa-bbf9-fe954661c07d | -23.22512 | -47.27713 | 2025-02-27 04:23:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 848dd42e-00b0-32d3-8251-a51eaccb63b0 | -20.31022 | -46.73621 | 2025-02-27 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0ed7c82-dbc7-3084-8cd8-efc25b91e4b4 | -22.84987 | -42.54725 | 2025-02-27 04:23:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ed1f684b-92e6-356d-bb6a-f3a4f38d11bc | -21.18804 | -48.57906 | 2025-02-27 04:23:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 39be2ba5-97e2-3673-bf87-e35ce7deae69 | -23.70094 | -46.74839 | 2025-02-27 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1ecebde7-fcbd-3077-bf0b-cf16bf883145 | -22.7861 | -43.75872 | 2025-02-27 04:23:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 540a9d64-8e62-37f9-992a-1eafed33b8f3 | -22.67701 | -42.85413 | 2025-02-27 04:23:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| caae068b-661e-32a9-a9e2-bf04a99cda2c | -20.31191 | -46.72505 | 2025-02-27 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50ac3d06-35e0-3d1b-aea9-6caeb73122bf | -23.40686 | -46.55763 | 2025-02-27 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e003771a-9797-3cf4-b8af-219afd1d8a2c | -20.76487 | -46.7709 | 2025-02-27 04:23:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| daad81fe-8186-34f5-b6c7-cd2f57c23711 | -23.22849 | -47.27771 | 2025-02-27 04:23:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2c0446cf-a56d-3e92-8c8b-a1c4a32d0fc2 | -20.69428 | -49.00657 | 2025-02-27 04:23:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4eb40b4f-540e-30b4-8a65-301661a00606 | -22.85035 | -42.54313 | 2025-02-27 04:23:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 95cdf03e-c2d8-3046-85a7-eb191570b029 | -21.47862 | -45.24584 | 2025-02-27 04:23:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f172386-7756-3317-834f-643be9b45872 | -21.19413 | -44.93544 | 2025-02-27 04:23:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 67bab961-bf27-3c75-adfa-093f795fea68 | -20.41434 | -43.55504 | 2025-02-27 04:23:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dcdd01c9-fff9-39b6-bfe9-f248a44e8ce8 | -23.9921 | -48.32452 | 2025-02-27 04:23:00 | NOAA-20 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 08bcf583-3805-3984-8111-efa7210b7321 | -20.3134 | -46.72784 | 2025-02-27 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7b80d5e-6d0c-34d8-998f-5a4fd88fea53 | -20.97832 | -47.64505 | 2025-02-27 04:23:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcb1644a-613b-3e6c-aed7-3e8adc090362 | -22.64617 | -42.24474 | 2025-02-27 04:23:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 78758c10-6655-3491-8571-a489f5390daa | -20.76152 | -46.77031 | 2025-02-27 04:23:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 30eb232a-7c37-3be3-b7c3-bc160181292a | -20.30688 | -46.73563 | 2025-02-27 04:23:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63ef6629-f280-3a0b-b77d-3994bebc30d2 | -23.33757 | -46.77365 | 2025-02-27 04:23:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 647f5526-bf3f-3cf9-be49-6e4bc0ddb08a | -19.28799 | -46.58386 | 2025-02-27 04:23:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea045d2d-5b14-3f68-9ff4-3b4398eede1f | -25.18448 | -49.23672 | 2025-02-27 04:25:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 11d7ef96-0ef3-35f7-ae71-a138ba635ffd | -21.0553 | -47.777 | 2025-02-27 04:30:00 | GOES-16 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8958c006-15e1-3258-9320-e7b5f9e7d855 | -21.0553 | -47.777 | 2025-02-27 04:40:00 | GOES-16 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 13465ef5-3e49-3b83-878c-3eb92f7cc3cf | 0.83153 | -59.94766 | 2025-02-27 05:08:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
