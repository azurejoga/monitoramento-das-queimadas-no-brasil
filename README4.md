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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae32e812-3e5e-3922-8949-7a2b15ae3650 | -3.9806 | -48.06708 | 2024-11-26 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 548.2 |
| 3d10d78d-f322-3f3c-a577-59e41a221420 | -2.47868 | -49.11322 | 2024-11-26 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 42e6c534-b336-3320-a1f4-95579f7f66a4 | -3.59959 | -50.36314 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4864b9cf-71b1-3257-bf1d-4402b77c426e | -3.38024 | -42.21786 | 2024-11-26 00:30:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 80594266-1ffb-3435-9d85-06b3a48d80d2 | -2.54155 | -46.89094 | 2024-11-26 00:30:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2bfdc179-40d7-3f76-b872-7eae43913d14 | -3.91438 | -42.41983 | 2024-11-26 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 356.7 |
| a6c3253d-d78f-31e5-a1cf-4b3af653db35 | -1.82243 | -46.28032 | 2024-11-26 00:30:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 57b0084a-e44c-3404-ad05-c85e7d460355 | -2.54903 | -46.89641 | 2024-11-26 00:30:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 84e025e5-52e0-38aa-8878-6226dff9b325 | -3.32675 | -50.0599 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3810d507-2517-3b5b-9b7a-4254a9f05bc4 | -2.81334 | -53.04486 | 2024-11-26 00:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| d7da9ae0-faba-321a-a436-7c278bd815a6 | -3.58871 | -50.38927 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 232.1 |
| 21103a65-ae1c-3dab-90b8-bbb6b4681245 | -2.09768 | -45.77037 | 2024-11-26 00:30:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 62d524dd-3d33-369d-9f11-1b7a06fab953 | -1.60124 | -47.47026 | 2024-11-26 00:30:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 85a16866-2a21-37c1-8d81-078237883679 | -4.66354 | -47.95955 | 2024-11-26 00:30:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 04fe3657-173a-31e1-9129-e7b6fe5fb4e5 | -3.33112 | -44.05408 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a4754092-b037-3edd-8401-fa3a4cde57d6 | -2.54332 | -46.90346 | 2024-11-26 00:30:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 49b36bba-fbf7-372b-9119-4b2357de8e01 | -3.24238 | -45.68436 | 2024-11-26 00:30:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 5e0af2ce-7bcf-31c6-88c7-ba3cd51c45b7 | -1.56557 | -45.67411 | 2024-11-26 00:30:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1b73897b-aec6-3045-ae2a-553d0e23aa03 | -3.9861 | -48.038399 | 2024-11-26 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c776efbc-a08c-38a6-8c0e-5d0a209a19fb | -3.9673 | -49.936699 | 2024-11-26 00:38:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ab4736c-940b-32e3-8f6f-695fac27007b | -6.3681 | -47.359501 | 2024-11-26 00:38:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 526ae74f-cfd1-37cb-beec-da6da13d4c25 | -4.6545 | -47.938801 | 2024-11-26 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8429e99d-915e-3468-8d39-16129e8aa9ac | -21.3151 | -47.408798 | 2024-11-26 00:38:00 | METOP-C | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b62ab4f4-a3ad-345d-89d0-b32cca93b0bb | -3.9024 | -42.408199 | 2024-11-26 00:38:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 53478b15-b224-3cd3-9afa-375c022e4580 | -4.6561 | -47.945702 | 2024-11-26 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 407cdf11-d2ab-30d0-a6e8-fe516010e8e8 | -23.743601 | -49.012901 | 2024-11-26 00:38:00 | METOP-C | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ef63d0d2-fea6-318b-9eb4-b1b8acb958fc | -3.9877 | -48.0453 | 2024-11-26 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7e68c39-788b-35c7-944e-bc941f8e8ae4 | -3.2282 | -50.312698 | 2024-11-26 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eaad2bc-4ab9-3354-a03c-f856fedf22ce | -4.501 | -45.194599 | 2024-11-26 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 831f5a31-6d2c-31e6-8417-1a39ed1aeae5 | -22.098101 | -49.615299 | 2024-11-26 00:38:00 | METOP-C | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c2825a3-f4ff-3619-bb5a-0eb316730219 | -3.9925 | -48.0662 | 2024-11-26 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af5d77df-b43e-3bd7-8a64-ef0852ba4f6f | -6.0676 | -48.026299 | 2024-11-26 00:38:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a6246a9-5622-3273-9de8-aafca9f9f40c | -3.2791 | -50.264801 | 2024-11-26 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96f097e4-8a84-3d2b-89e4-67cb613e14a9 | -3.169 | -48.433201 | 2024-11-26 00:38:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 036738cc-266e-397e-9af3-53564e270f71 | -20.325399 | -48.834202 | 2024-11-26 00:38:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5001239a-4dec-31dd-8092-9640d19d6b38 | -19.562099 | -44.853901 | 2024-11-26 00:38:00 | METOP-C | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6cd92813-f39f-3c12-a2d9-9093a3d2d236 | -20.4513 | -44.174801 | 2024-11-26 00:38:00 | METOP-C | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 150df4ae-9224-3f1a-988c-f402ac8becc6 | -2.3956 | -53.673698 | 2024-11-26 00:38:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b09affa-15e2-38e4-936b-b4c242530351 | -20.404499 | -48.769798 | 2024-11-26 00:38:00 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b3bf1080-532a-3386-a411-4b10be9b7950 | -3.2298 | -50.319698 | 2024-11-26 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5c918d3-e577-3f6e-868d-87be7586e21a | -3.2425 | -53.282101 | 2024-11-26 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18ad29a2-441f-333b-87ee-6e224ac4f30a | -3.7473 | -52.6478 | 2024-11-26 00:38:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6ed4f8f-8e72-33ca-baa2-e1f1886a4e7e | -3.3865 | -44.181999 | 2024-11-26 00:38:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06aa2866-4de5-31d2-b0c4-8ad253d713f0 | -5.6453 | -46.646 | 2024-11-26 00:38:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78850242-d3e5-3d36-b663-ca914e44c33c | -21.3134 | -47.4007 | 2024-11-26 00:38:00 | METOP-C | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2f72c062-72bf-30b4-8c16-a844ac90c268 | -2.5349 | -46.893501 | 2024-11-26 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e32f0e3d-0d33-3729-84cf-586729fc4e46 | -3.9121 | -42.405998 | 2024-11-26 00:38:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7aea3519-8d3b-36bc-b94c-a96ada14eda6 | -3.9153 | -42.419399 | 2024-11-26 00:38:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f54f0626-321e-3329-8fd2-3d6fce68834e | -3.2823 | -50.278702 | 2024-11-26 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa00b98e-a30b-35d1-9513-2804cc707dfe | -3.2446 | -53.291302 | 2024-11-26 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be4f6a83-dc37-3bb1-b3fd-f8fa1e0f980b | -4.6577 | -47.952599 | 2024-11-26 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f80e2bf1-c3fb-38bd-8e4f-54f923f9bb8d | -22.0961 | -49.604698 | 2024-11-26 00:38:00 | METOP-C | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d05b9c18-b35c-3f07-9d96-d5f72b3ba96a | -9.4379 | -43.2103 | 2024-11-26 00:38:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 42d5415e-139c-354d-82a5-b5c306a640b5 | -17.625401 | -57.5555 | 2024-11-26 00:38:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c57a20a0-ffdd-37b5-92ae-615d969b9e1a | -6.0708 | -48.040001 | 2024-11-26 00:38:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abce9f93-25d5-3a4c-a154-a9bf20294994 | -6.0692 | -48.033199 | 2024-11-26 00:38:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d67f03d8-a047-3638-b69d-44eba7a1200f | -3.3815 | -44.160999 | 2024-11-26 00:38:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1392d71-ab76-38e6-a3e5-a6987f5c9d1c | -5.6563 | -45.8526 | 2024-11-26 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34aab00b-2ae0-3428-8a91-4712f59f5373 | -3.384 | -44.171501 | 2024-11-26 00:38:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e19bfdda-e448-3e01-b806-0dc1b363bee8 | -4.5031 | -45.2034 | 2024-11-26 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7108c3f5-98fa-3279-930b-af6595c7cdc6 | -5.1825 | -47.812199 | 2024-11-26 00:38:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e338ba8-da4f-36e7-945c-1fc814d9e4f6 | -3.9056 | -42.4216 | 2024-11-26 00:38:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96006cac-40fa-3fe9-87d9-2818b00429bc | -3.9893 | -48.052299 | 2024-11-26 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7de19ef1-ffe7-3456-992d-185a608d1114 | -4.4213 | -44.724499 | 2024-11-26 00:38:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc6a3354-948f-37ad-b471-ecf59b4327fa | -3.3938 | -44.1693 | 2024-11-26 00:38:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9627499f-e3c4-343c-9cab-1db0861b345d | -20.323601 | -48.825199 | 2024-11-26 00:38:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57758c8d-2e1b-37ad-9ba2-ed8455283749 | -6.3667 | -46.7742 | 2024-11-26 00:38:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fca2ac6e-59c3-3436-b2bc-a41924d9f7e9 | -6.3683 | -46.781399 | 2024-11-26 00:38:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcc4e4b0-8c95-39ba-9dbc-29926be35907 | -5.9442 | -39.651299 | 2024-11-26 00:38:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a912d57c-8c7f-37ed-b82c-4b5e48184466 | -4.9494 | -45.786499 | 2024-11-26 00:38:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be358e21-386c-3b87-99ca-0b67b6f1b7a0 | -3.1722 | -48.446899 | 2024-11-26 00:38:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb5897eb-e2c0-3aa4-a0a2-f9ace72aa2ec | -6.3664 | -47.352501 | 2024-11-26 00:38:00 | METOP-C | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dec202c-23d2-3e22-9740-7f23b09ef3b4 | -5.949 | -39.670502 | 2024-11-26 00:38:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e1d69feb-4217-3a08-b7ae-5bf2a129f0be | -3.1706 | -48.439999 | 2024-11-26 00:38:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1666fed8-d3ab-35cc-b11c-89d62ef8c515 | -3.9909 | -48.0592 | 2024-11-26 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3413bea2-d204-3013-a22b-d5422c04fc42 | -4.6463 | -47.948002 | 2024-11-26 00:38:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78987a4e-510c-33fc-ac37-8b5ad22d5f92 | -4.4235 | -44.733898 | 2024-11-26 00:38:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43205d9d-4f1c-3372-b9ac-d0507733db5d | -5.2195 | -44.9161 | 2024-11-26 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b8e88d0-7247-3e19-9456-f6210c379fbe | -6.066 | -48.019402 | 2024-11-26 00:38:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa817469-70e8-3061-bfd7-04c7f8edfc9c | -1.1863 | -47.6633 | 2024-11-26 00:38:00 | METOP-C | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2aac2f8-80bc-34f4-8118-d1a98ec9b2f0 | -4.5052 | -45.2122 | 2024-11-26 00:38:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e8024da-b6df-311a-8b8b-4a138f13670a | -5.1841 | -47.819099 | 2024-11-26 00:38:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc33ddce-9752-3bda-90b6-899183196601 | -3.2807 | -50.271801 | 2024-11-26 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 544dd37e-d785-3e48-98dc-536ced81baec | -19.5604 | -44.8466 | 2024-11-26 00:38:00 | METOP-C | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 09bbad29-fe79-369c-8ea6-e9e771280e9b | -1.6788 | -52.602699 | 2024-11-26 00:38:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44d30268-a894-3df9-b228-fd30ac4b42c5 | -20.3218 | -48.8162 | 2024-11-26 00:38:00 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cb2fdf58-12b1-395c-8dfd-c89ffc8fc17f | -20.4027 | -48.760899 | 2024-11-26 00:38:00 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c665146c-071d-3148-9570-e836ecd329b8 | -3.2404 | -53.2729 | 2024-11-26 00:38:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d8561c-8bdd-3c1f-b4a1-3ba561bdc492 | -3.908 | -42.402 | 2024-11-26 00:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 44.8 |
| fc21cfbe-c448-3953-a4a5-3d79ffa8b29f | -17.6453 | -57.5874 | 2024-11-26 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| c5baa8dd-87ca-349a-b21e-dc352d5302b9 | -3.986 | -48.0626 | 2024-11-26 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 0fa2fb91-d509-3831-85a9-574394a16cef | -3.9859 | -48.0843 | 2024-11-26 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 7c82f173-e036-3b98-b672-c51adcaecd08 | 3.8257 | -59.5896 | 2024-11-26 00:40:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 69a80ee6-b820-35df-89a2-da0c0fe999d1 | -2.8014 | -53.0024 | 2024-11-26 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d9600375-6248-3592-a098-d3796b53c565 | -3.9676 | -48.0418 | 2024-11-26 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| adaca084-1c29-309b-b948-bab2ffde4ee1 | -2.178 | -45.9758 | 2024-11-26 00:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 62775bd4-19d3-3470-b18e-770ad537c2fb | -3.2907 | -50.2627 | 2024-11-26 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 52c0a55c-362a-33c4-be62-1b0623d97166 | -6.0676 | -48.0352 | 2024-11-26 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f0f990fb-a83b-3dee-a5db-21c7aa0efac2 | 3.8256 | -59.6088 | 2024-11-26 00:40:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3c2a87a7-56de-30cc-bfc9-922fec7f9f43 | 2.6901 | -60.4111 | 2024-11-26 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |


[Clique aqui para ver as próximas entradas](README5.md)
