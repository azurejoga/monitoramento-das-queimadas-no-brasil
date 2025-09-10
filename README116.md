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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6705d504-c204-3efa-ac7f-c651f0acb7ca | -13.1367 | -54.9171 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 212.8 |
| 46edd929-ba7b-32ca-a8b6-86efebb8f89c | -5.0251 | -43.1327 | 2025-09-10 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 58870dec-1c59-3e9d-b017-4bfc89293c1d | -14.8877 | -55.8567 | 2025-09-10 14:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2fa805b4-7556-3fe3-b2d4-ebaff393e813 | -5.9374 | -45.8153 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 031fa858-13e3-3f78-819a-10f73689037c | -5.9187 | -45.8166 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 4a564dee-c42c-3dbc-b797-3d6352c35792 | -10.0157 | -51.6821 | 2025-09-10 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 236975c2-39e6-3ee3-ba09-35d42b8bec6f | -14.3878 | -53.3037 | 2025-09-10 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3cbadd40-d6f7-35eb-92e7-0dcc8a9a3023 | -11.4705 | -50.3247 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 177.7 |
| e79641a4-4fc3-33f7-8b9f-5ac3446966b1 | -6.3427 | -42.6075 | 2025-09-10 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 162.2 |
| d3fd3fae-575b-3724-bbfc-cd29489dc447 | -20.5277 | -47.6448 | 2025-09-10 14:30:00 | GOES-19 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 173.1 |
| e0ffb4ab-f148-32d3-b54e-86812d0dcfed | -13.3377 | -51.7028 | 2025-09-10 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| ef5e246f-bca8-3cca-ac41-e349833ea68c | -5.9561 | -45.8139 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| fa0f0c08-e843-319e-9a74-669c59955a84 | -10.8513 | -46.0637 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 296943d0-1af7-35ab-9449-a7ada1915edd | -9.3437 | -46.7603 | 2025-09-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 96d46912-174d-32da-bea8-0c1ae1795e44 | -5.9189 | -45.7941 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| e2ab7d03-8318-3166-9b28-baa03ff3870a | -5.4157 | -43.4319 | 2025-09-10 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 63ca5d8f-ca02-3018-96ec-cd74717771c4 | -5.9382 | -45.7254 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2add56f8-e037-36a2-a226-cf51fefe8373 | -5.6788 | -43.3425 | 2025-09-10 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 321507dd-e82b-3808-8b3a-965a036a8da5 | -6.8521 | -47.9143 | 2025-09-10 14:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 4d68811f-f4f3-3dfc-a2e9-c5a634f10a9b | -11.4648 | -43.6668 | 2025-09-10 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 410.6 |
| 3ecc5761-a6e2-3268-9b39-5f76f7508ef8 | -9.8835 | -50.1933 | 2025-09-10 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| cef610da-66f0-30e1-9e1f-d98a08c97b20 | -13.1364 | -54.9376 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| a1ff7561-c345-3c62-a0b4-9018353067c1 | -11.4515 | -50.3268 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 9ea90fed-b581-33ea-898e-5159e08e9dbc | -6.8895 | -47.9115 | 2025-09-10 14:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 39f45463-18a0-3142-8bbe-7b3d8f01a027 | -9.6284 | -48.0568 | 2025-09-10 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3ef14fa0-e820-382f-9199-de6ab3b635b5 | -5.8582 | -44.2088 | 2025-09-10 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 5c1d86e5-3c13-3f0a-b2fb-ab5a8cb50a8f | -10.7179 | -46.0809 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 06ee85bd-7a55-336d-a8ea-14b70e21a5c1 | -9.0745 | -45.7109 | 2025-09-10 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 63602a3d-ffed-3e39-b9bd-e441485bba0e | -15.2877 | -53.7987 | 2025-09-10 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 53b27589-f0d4-3f9c-ae22-822ef57b197e | -6.6198 | -53.3576 | 2025-09-10 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 20618658-16d7-314c-ac70-b11a55402a07 | -12.9286 | -54.7949 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 5b3df2aa-ffc9-30bd-80a3-c31216c22950 | -7.4639 | -44.9433 | 2025-09-10 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 2c98ae15-44fc-34d9-94bb-896bc7bc779e | -12.9289 | -54.7744 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 79a8c1e5-dcc9-3541-aa46-5eaf4d4977ed | -11.1247 | -52.0149 | 2025-09-10 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 319.1 |
| f574f2d2-e47a-3a17-abb6-2509cbc7fd7e | -6.2409 | -43.3911 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 345baddd-95ff-37ba-859f-8480a4862ba3 | -8.0416 | -48.6656 | 2025-09-10 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.9 |
| ef5a01da-bb6e-310b-8381-def94f34f9bc | -9.9065 | -49.8703 | 2025-09-10 14:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1f93ea1f-fb31-3ec2-8ad6-0316b61a5a54 | -9.7223 | -48.0907 | 2025-09-10 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| a7505b86-ec88-304b-8cb5-f40c5a9e8bce | -11.1245 | -52.0359 | 2025-09-10 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 321.5 |
| c79ba951-d799-3335-a17d-e068fc63a319 | -9.8649 | -50.1737 | 2025-09-10 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ebc10365-a6ca-3869-b4b5-d3ca028dc8f9 | -16.5294 | -55.1434 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 207.6 |
| 1beb1786-4403-3443-8275-9b4c476dd6db | -11.4093 | -43.5573 | 2025-09-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 13332077-73f9-35ba-a6df-b603d05349aa | -10.8319 | -46.0889 | 2025-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 26aa1793-1a13-3ee3-ba52-bb5be332d779 | -11.4648 | -43.6668 | 2025-09-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 407.5 |
| 414daac8-86d1-3285-ad2a-55ff124bdf8d | -6.1616 | -45.8214 | 2025-09-10 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 9b6fb006-28ef-3e82-a026-86d6d55bd987 | -7.8081 | -46.0649 | 2025-09-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 25c92026-abcc-3321-89a2-b8d8ad76e8eb | -5.6788 | -45.4738 | 2025-09-10 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b485a1c4-0c06-337c-9f4e-9ed9a3720f3a | -7.4639 | -44.9433 | 2025-09-10 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 201f84b3-1238-358d-8b16-aac60699e814 | -6.2595 | -43.4129 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 335.5 |
| af5b645f-0b3e-39f2-9fc0-135d5808fd4a | -11.4097 | -43.5336 | 2025-09-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 282.1 |
| b2ad4b30-d125-3c14-a263-7cfc92282a02 | -6.2043 | -43.3008 | 2025-09-10 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 99d41549-e2b2-325d-9204-ce829d903ccd | -11.4469 | -43.5988 | 2025-09-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 381.8 |
| 35f07f44-99ea-320b-9374-c16f603f0e4e | -4.7346 | -44.4457 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| eeccb901-2824-309e-9224-f80407ff713f | -9.8835 | -50.1933 | 2025-09-10 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 465.7 |
| 3e22397a-af15-34af-8c6c-7638e3bf71ba | -7.3618 | -47.4364 | 2025-09-10 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 242.4 |
| dbe7a777-7eca-30e7-a027-5048cdc6f902 | -6.3427 | -42.6075 | 2025-09-10 14:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| a8485722-8155-38ff-952c-21f93c6867fd | -16.549 | -55.1409 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 146.5 |
| 7484091c-f1e6-3cfa-808f-e0466c66fef1 | -11.3901 | -43.5602 | 2025-09-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 8a65361c-1e92-382b-be69-8c7f57612827 | -7.7102 | -44.7827 | 2025-09-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 032cc712-166d-34f9-a96b-af1dd1696211 | -9.7596 | -51.075 | 2025-09-10 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 1e51f31d-ce40-3713-9541-0cbefd488fa6 | -11.3389 | -46.5419 | 2025-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a375f792-5525-345c-857d-bb7e28e17e8b | -8.0794 | -48.6407 | 2025-09-10 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 182.3 |
| 617323bb-8462-33e6-b6f5-d8170c1d6907 | -6.8523 | -47.8925 | 2025-09-10 14:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 58b7ca92-b733-33bb-96e2-170d23008f30 | -9.8263 | -46.0549 | 2025-09-10 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 22cffecf-0f2b-31d5-9c37-0f3bbb1ea8c7 | -9.0132 | -46.0563 | 2025-09-10 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 2f115fdd-b53b-310e-84ce-484b9afaa653 | -12.18 | -53.8836 | 2025-09-10 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 59c1e402-c91f-3001-bda5-1669bc1eafbd | -6.2597 | -43.3895 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 3bf7d505-eef8-332f-a1bc-33426634996c | -11.7897 | -50.5879 | 2025-09-10 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 88e71831-9f63-3a4e-a9cb-b755ea43d0af | -15.1374 | -52.4039 | 2025-09-10 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a2ca0dc0-7890-3b8b-be91-f3f4f38cf5cc | -9.055 | -45.7583 | 2025-09-10 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 89586175-e3fa-3dbf-b096-c7e312d22a81 | -20.205 | -41.5606 | 2025-09-10 14:40:00 | GOES-19 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.7 |
| 5b9b5432-1987-3323-8002-f089b813fd80 | -9.1142 | -46.9851 | 2025-09-10 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| c9542577-bb9d-3544-949d-ddd6c20c35cf | -9.0553 | -45.7356 | 2025-09-10 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 032499aa-4929-35b1-9965-cd84a481e8e1 | -6.8519 | -47.9361 | 2025-09-10 14:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| c2484f45-23e4-3eb0-a34e-986801316e40 | -5.8079 | -45.6673 | 2025-09-10 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 036b631e-5b2c-3c0d-ae34-07558e566387 | -6.2407 | -43.4144 | 2025-09-10 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 1943277a-ba9f-34ba-aa0f-4923737556a3 | -7.7104 | -44.7598 | 2025-09-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 252.0 |
| ed582bdb-23e7-3991-8945-83c17bd06581 | -9.114 | -47.0074 | 2025-09-10 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 97b34692-abc6-374b-a3b3-f805a6c334d1 | -5.589 | -42.9048 | 2025-09-10 14:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |
| d89ec6f7-353d-31b8-8051-04a745f26d7f | -11.7706 | -50.5901 | 2025-09-10 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| 2a8792d7-818c-3db2-9db5-491179ea2e55 | -7.6916 | -44.7616 | 2025-09-10 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 40688b3c-896a-3888-b216-739be07c7339 | -11.4281 | -43.578 | 2025-09-10 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 7f185bcb-7738-3443-9638-a13f8bb8b84b | -10.851 | -46.0864 | 2025-09-10 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 28f4087b-8b6b-391a-91b0-17c8387beb70 | -9.7591 | -51.1172 | 2025-09-10 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| cf9c0259-8e05-39e0-850f-8a4cb621f3c5 | -7.5033 | -48.2334 | 2025-09-10 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 203.3 |
| c6994366-4695-3c39-9541-e2358910d6ba | -19.282 | -47.9946 | 2025-09-10 14:40:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 300dc3e3-1bd8-3d0b-a2d7-35b1b76da150 | -8.4517 | -47.273 | 2025-09-10 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| c57ddc0b-e619-381a-9252-e6561bba773c | -9.0579 | -46.9688 | 2025-09-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 82a40a60-b9ae-3c65-970a-d742136631d2 | -12.5796 | -44.6412 | 2025-09-10 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.7 |
| da7c9d19-0c05-3425-abed-0e671e348991 | -11.2196 | -54.9975 | 2025-09-10 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 245.0 |
| 7f2f0f06-4ecb-3ec3-b2be-862eb917ad1b | -7.5218 | -48.2536 | 2025-09-10 14:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 99279d8f-8f55-3c6c-b05d-8336fd1175dd | -7.881 | -46.2598 | 2025-09-10 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| af43fe4d-ae22-387d-bc5c-3b34a322a9d5 | -4.1191 | -41.6048 | 2025-09-10 14:40:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| e9ba8bac-9be4-3893-8554-6a7a1bfd35fa | -16.5312 | -55.039 | 2025-09-10 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| adeb48f7-c0a2-380c-bef9-f69105e059f8 | -15.0627 | -50.1527 | 2025-09-10 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| bb5c1365-72ff-3ff8-b9de-c688d357ddf9 | -5.421 | -42.8234 | 2025-09-10 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 8816b325-f192-3571-a9af-da9c754e9e5c | -10.0157 | -51.6821 | 2025-09-10 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| d2d557e5-2d8e-3e36-ae02-fe2bcb430f8a | -9.7589 | -51.1383 | 2025-09-10 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 41b65b7a-9544-3797-81b2-dd0b41165994 | -6.3993 | -44.4419 | 2025-09-10 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e9f457cd-2b28-325a-8ef9-2c1acfc85de3 | -8.4903 | -45.66 | 2025-09-10 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |


[Clique aqui para ver as próximas entradas](README117.md)
