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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e11fb9f-a175-3395-a131-23fd6f6a7760 | -22.92093 | -49.20931 | 2026-07-09 04:10:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1333766-1ec2-322e-b29e-0f6324829f73 | -20.70262 | -43.84046 | 2026-07-09 04:10:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6fa80d4-1156-3552-9789-d9101b9e1f39 | -21.80616 | -52.71702 | 2026-07-09 04:10:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58d2e42a-c19f-35e4-93d8-2d2b57b251d8 | -21.50739 | -48.8176 | 2026-07-09 04:10:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ac0d8335-61d6-3c89-a432-dad6979e51d6 | -22.91806 | -49.20281 | 2026-07-09 04:10:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 892682d3-9799-3a75-8b71-ac00802f428a | -21.47052 | -54.48713 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 806a3a1c-c8f6-3740-8233-d32ec0953eeb | -20.88079 | -44.68518 | 2026-07-09 04:10:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 11a9b008-f53d-3ddb-b021-c33c5f2c6c10 | -18.0215 | -54.35753 | 2026-07-09 04:10:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8c9d0e8-bb93-3062-a359-29b049c7ed0f | -21.47144 | -54.48302 | 2026-07-09 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a4cd397-4a63-3356-bb6b-9a46db964e70 | -21.80026 | -56.26995 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd186ad9-16cb-3579-85f2-9def480dc6b8 | -21.77575 | -56.29053 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78c452e4-49e8-3186-a05a-3abe0c1a3f76 | -20.70202 | -43.84415 | 2026-07-09 04:10:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1688188b-fb06-3460-8b1a-a8bbbf972218 | -21.77448 | -56.29591 | 2026-07-09 04:10:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0efeb7e-5c6d-3bb0-8444-b7e3f5ad3ab3 | -20.18347 | -41.89858 | 2026-07-09 04:10:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6c7fecc9-8b2c-330f-b423-7198be20832e | -21.81114 | -52.71831 | 2026-07-09 04:10:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ed77b06-cb80-3a6a-adb0-1974d26d84c0 | -27.45671 | -48.45041 | 2026-07-09 04:12:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f5708f72-77c6-390a-b2f9-31f699ece6ab | -2.63883 | -47.98384 | 2026-07-09 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 290a0639-93a3-38ae-8063-dbae75a65035 | -1.81675 | -54.47931 | 2026-07-09 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96730460-79ec-346a-b923-1c57a964ebf8 | -1.82032 | -54.47987 | 2026-07-09 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 781cb7a0-2b6a-3f15-a443-c75d952a8185 | 0.87164 | -59.70513 | 2026-07-09 04:49:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3e690937-6f05-3c36-b6fd-a42fc4e37694 | -2.80908 | -48.59288 | 2026-07-09 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a254b14-4cf7-3b87-9c9f-c60ba6cef8fd | -2.64188 | -47.98883 | 2026-07-09 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6840ab2-041f-3bf3-be65-cff42d8502da | -2.96122 | -51.51145 | 2026-07-09 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a3384b2-418f-3476-9435-0c55b700a94b | 0.87686 | -59.70436 | 2026-07-09 04:49:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d36a3d8a-5abb-3645-9757-b6a82967c266 | -1.82388 | -54.48042 | 2026-07-09 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37e81c89-fdc6-3bbf-8d70-ce9ac4ac851f | -1.82095 | -54.47581 | 2026-07-09 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3daf1241-679e-33c7-a6da-b3aa8c170f44 | -2.64006 | -47.98622 | 2026-07-09 04:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 37f7a443-b73a-3c85-856b-2e9357a6d028 | -2.00513 | -50.87959 | 2026-07-09 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4728e5da-ef74-3d66-bed6-42f623eb255f | -7.89688 | -48.25324 | 2026-07-09 04:51:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ff1a8a-322b-3527-b388-503cd2e425d0 | -7.00059 | -43.11593 | 2026-07-09 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ff1bc2d-5e44-3f41-a336-24b0edd00a66 | -5.7519 | -43.26547 | 2026-07-09 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 323d887b-bdac-3fae-ad11-00ade2cb6145 | -8.86231 | -50.18212 | 2026-07-09 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07167c98-d400-31ba-b1e4-796aaa417045 | -9.37009 | -44.72034 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c73c6a8-48c1-39e4-b65d-708c6360e79a | -6.94467 | -43.71172 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ada6955-23ff-3d3f-8f5b-40303d62d5ef | -8.71813 | -48.34184 | 2026-07-09 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9334583-6207-345b-8a9b-dfaa8ad51443 | -8.11572 | -47.10284 | 2026-07-09 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7d349ae-6b58-3cb5-892f-67e41ce0d385 | -10.87083 | -47.59644 | 2026-07-09 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c629d04-1c00-3733-9a14-e3c71a4a01f7 | -6.43171 | -55.79888 | 2026-07-09 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f46e1c1-f8a1-3c82-ad4e-6f81ae131256 | -8.70213 | -54.53956 | 2026-07-09 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85a90dbc-2eb5-3bd8-a03d-ce1abf71bb14 | -5.48947 | -44.12091 | 2026-07-09 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccf2a6bc-86ca-3db9-980a-029da6f0987f | -6.94116 | -43.69777 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 266234f2-3ca1-3390-b656-83d7e67a5375 | -8.98308 | -49.88676 | 2026-07-09 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98142ef2-c212-3eec-b851-0fc11356a251 | -7.29037 | -46.25143 | 2026-07-09 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 08b1d264-0974-321a-89a9-0aebcf3e100c | -7.71152 | -45.16312 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f94a99c2-4c3c-3dc3-91dd-5602cb78858c | -5.53358 | -44.09811 | 2026-07-09 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db8ca8c-2d5e-3c81-8923-e4499f42e224 | -8.9805 | -49.88871 | 2026-07-09 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74d24509-99dc-3ea9-9ded-9827e976831b | -7.71121 | -45.16795 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac1ff3be-47a9-3c54-847e-850e12e45f0b | -6.52087 | -49.86463 | 2026-07-09 04:51:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c078f5ca-1259-3014-9114-3c95e3120db3 | -4.56942 | -48.0274 | 2026-07-09 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd2d1ea7-0d24-3fa9-a84e-777e85266a52 | -8.3494 | -45.3974 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68356221-ae05-3cba-a748-11ee20670f02 | -4.52229 | -47.38188 | 2026-07-09 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e769d15-6d5f-3758-8a92-6f08300abaa2 | -9.54722 | -46.50138 | 2026-07-09 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87a205ec-360f-3426-92ad-4c8fefc8ad7e | -8.33372 | -47.4225 | 2026-07-09 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d142f9fa-6a6e-3ebe-870a-1d42254b32ee | -10.80562 | -49.64624 | 2026-07-09 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f568b11-4638-3c7a-93f5-d8aa5090908f | -9.23341 | -50.14591 | 2026-07-09 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| defa852d-bd45-323e-a99a-3a95cfb42ff2 | -5.48133 | -47.43525 | 2026-07-09 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 457998b2-50c3-3d48-aba7-14b31a32de2c | -7.71046 | -45.17325 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5626786d-968a-3328-aef1-babe008617e7 | -7.73031 | -44.56086 | 2026-07-09 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4655ea7e-a6ba-385b-8781-843bb2f56caa | -8.12754 | -42.97232 | 2026-07-09 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31709fb9-ccc8-3ed9-a82c-0667a338878d | -11.45912 | -47.58913 | 2026-07-09 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c9b578c-86f4-3f14-968c-d450ef06d236 | -6.94525 | -43.70917 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04ef65cd-5891-395b-b5a5-47dc4fcac81a | -6.42879 | -55.80156 | 2026-07-09 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59ec3971-fa58-30a3-b25c-07c93d7a6444 | -4.70142 | -50.4428 | 2026-07-09 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aef968ea-dcb2-3375-8188-c21b1f49ca0e | -10.34712 | -48.26515 | 2026-07-09 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ce903a2-9607-3f28-949d-f4a5e84daf42 | -7.72992 | -44.56372 | 2026-07-09 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8197b128-94e9-3dc4-908d-b12f98041e98 | -5.92113 | -43.85575 | 2026-07-09 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c133414-c891-388f-80a6-8f7f0315c0ad | -8.12051 | -47.09953 | 2026-07-09 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a350ad9-cfaf-3e90-be69-04058740b20a | -8.08283 | -46.69048 | 2026-07-09 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db6d6ad-4939-35c4-819a-493a70b5853d | -7.70715 | -45.16193 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14d29e78-3d59-3d45-b8bb-45dbbeb1df0f | -8.96503 | -48.0113 | 2026-07-09 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9ddf94f4-c3f2-3cce-9140-1263f4708fb1 | -6.74038 | -47.1353 | 2026-07-09 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 750910bb-2dbc-3688-857c-38f5088fd50a | -8.11994 | -47.10355 | 2026-07-09 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 984b0da8-c17f-3fbd-b8e7-7f49f9d0b4c8 | -8.72675 | -48.33787 | 2026-07-09 04:51:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be125992-c613-3c10-832b-37cda8230994 | -6.64902 | -43.91265 | 2026-07-09 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5a60707-5c24-3b28-88bd-e5ecf6c70dff | -7.28469 | -46.25961 | 2026-07-09 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3026eb7-92a2-35b2-92d7-7741b258575a | -9.64477 | -48.56127 | 2026-07-09 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1539ded1-b9e7-3b0a-a039-7301d26295ec | -4.83573 | -45.34334 | 2026-07-09 04:51:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c1cc715e-3f73-356d-9f05-5a62e07d07df | -4.61946 | -49.05232 | 2026-07-09 04:51:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a90cd3c-cd0e-35df-8503-86a6ab0ebb87 | -8.35355 | -45.40281 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e280de9-482c-3205-9269-7a2083b8f6cc | -9.36925 | -44.72654 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0e24d2a-837d-3c5e-8ccf-570dd3bb6166 | -8.72905 | -54.54386 | 2026-07-09 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cd041d2-9ad5-3ead-9e2a-2fb1d8a156e5 | -9.23638 | -50.15058 | 2026-07-09 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da864bb1-80b2-35d5-9105-1169d4b175c6 | -5.52857 | -44.09727 | 2026-07-09 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7703f6bd-4864-34d4-85e8-436772fa3ac6 | -4.83504 | -45.34803 | 2026-07-09 04:51:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 445590db-7949-3e06-bb23-945677bc0369 | -7.00109 | -43.11234 | 2026-07-09 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4607823a-07c4-3af4-8090-835bf69c9c14 | -6.92557 | -43.69639 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dd6cfa3a-d6e2-39a4-9785-ac30d33bd170 | -6.94555 | -43.70512 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f6d1825-6dac-3405-b1df-d41d0b8bbe14 | -6.94091 | -43.7019 | 2026-07-09 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 852f857b-d201-34a0-8c38-c8f2d224a36a | -7.71081 | -45.16844 | 2026-07-09 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83bb0ad4-9fec-3763-a92b-862faac36678 | -6.93829 | -48.19482 | 2026-07-09 04:51:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a37031da-e930-3e6a-bd6c-96aeb5e02af6 | -9.37314 | -44.72381 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3533063d-61a8-3ab7-8935-7aec029b4d51 | -5.48908 | -44.12372 | 2026-07-09 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0873e737-002b-3061-b068-a7effd200493 | -8.12107 | -47.09551 | 2026-07-09 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4420a2c-b8c7-33b1-b011-08c973f56690 | -5.48881 | -44.12354 | 2026-07-09 04:51:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bdafd6f-90fc-3ab1-8d7a-ae8e51db7118 | -9.37275 | -44.7269 | 2026-07-09 04:51:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2006081a-6b64-38c9-8032-0748860f4b7b | -7.28531 | -46.25522 | 2026-07-09 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e5af5e6-cd47-3489-8340-e4587b32fbc3 | -8.96049 | -48.01424 | 2026-07-09 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40a21cda-53d7-3025-a281-d8dd872a3431 | -2.98673 | -54.60313 | 2026-07-09 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 692cae80-be3f-3f48-94b9-3b061e90e002 | -10.86602 | -47.59985 | 2026-07-09 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05c16f7b-7363-3139-b3f5-28d6c9cb4734 | -5.75144 | -43.26878 | 2026-07-09 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
