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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8432c453-66cf-31bc-bb85-950b31fb11d1 | -22.18541 | -46.93544 | 2025-11-21 04:18:00 | NOAA-20 | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9e026ad-59e3-3e5f-89a8-2c0e40f1ed0a | -20.88583 | -52.35157 | 2025-11-21 04:18:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| feb39117-64aa-3ac1-b1e0-12c16c15437d | -20.2528 | -49.33928 | 2025-11-21 04:18:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 940e0d28-b107-319a-af58-05ae194c98d2 | -20.88174 | -52.35058 | 2025-11-21 04:18:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74084e72-a1c2-31c6-87a2-26590633295f | -18.9568 | -55.18611 | 2025-11-21 04:18:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| e67eb21d-2462-3179-a9a9-0bfd5542c14e | -19.49604 | -55.35147 | 2025-11-21 04:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ff7099cc-47a9-3913-96a8-b6ec65ec678e | -20.18349 | -50.38227 | 2025-11-21 04:18:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ab84495e-5402-3906-aece-194bd4294543 | -18.93851 | -46.90238 | 2025-11-21 04:18:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a4fb1e8-97bf-347e-945e-359756e949c3 | -20.88662 | -52.34752 | 2025-11-21 04:18:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7adbc223-2e8e-3db6-bdfd-c661a7963858 | -18.83844 | -47.68059 | 2025-11-21 04:18:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e14d4e61-3435-36ff-b41f-cd46a137579f | -17.62366 | -54.19504 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0924d45a-f3ca-3b94-88d7-a9af05174119 | -21.1648 | -48.61881 | 2025-11-21 04:18:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 57f3303e-098c-3fe5-a714-d578b542356f | -17.61496 | -54.18731 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3fa4a673-d867-3028-aadf-df0b42804969 | -19.19301 | -50.85117 | 2025-11-21 04:18:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a195fcdc-56e5-370f-ac81-16a4c336bf4b | -21.24619 | -44.08741 | 2025-11-21 04:18:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef5340e9-2bf8-3e7b-ad28-01154fddffc7 | -20.77245 | -51.58936 | 2025-11-21 04:18:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f1a39809-bb8c-3dee-9fff-e1fd47a0f105 | -19.85605 | -46.30745 | 2025-11-21 04:18:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a37bb944-e362-34db-8d70-85d0f679d3c8 | -21.37114 | -48.60365 | 2025-11-21 04:18:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2673abfc-4dfa-3bb8-ad27-37ee1db447b1 | -21.1504 | -48.5998 | 2025-11-21 04:18:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08153239-7681-348c-8198-cdac616c662e | -17.66516 | -54.22351 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e84b065c-f821-3c14-884b-d75a38341438 | -21.04205 | -48.55533 | 2025-11-21 04:18:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d9c074ed-18bc-3e86-9021-f350493a6e3a | -22.41806 | -44.21778 | 2025-11-21 04:18:00 | NOAA-20 | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5468363b-9b95-3226-b027-1d96c3a5367b | -19.47684 | -53.94582 | 2025-11-21 04:18:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce00f596-50a9-308c-b7ef-4996f29576ea | -20.80323 | -49.05414 | 2025-11-21 04:18:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7fb3a05-d3fe-3083-8f12-7960a1dccb65 | -19.88542 | -44.76476 | 2025-11-21 04:18:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1c05960-70ac-3fc7-94f0-da9efedd2aa3 | -21.24329 | -44.08273 | 2025-11-21 04:18:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f13daa73-862d-3ba0-b658-9c6c02def13c | -18.10126 | -54.52559 | 2025-11-21 04:18:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9521e489-e822-3121-add9-b5b5e89b5932 | -20.3185 | -53.99123 | 2025-11-21 04:18:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40fffb24-9a6d-3e12-8acc-43d8294b3547 | -23.30413 | -47.50555 | 2025-11-21 04:18:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bdc8735a-b9d0-3a04-99aa-ef6ffc0d883a | -21.47904 | -46.59019 | 2025-11-21 04:18:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fc335ef0-ee1e-395b-a384-30c953c7457d | -23.30745 | -47.50617 | 2025-11-21 04:18:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 87d608a2-c524-3525-a6c9-710d64ec88a8 | -25.14313 | -49.69822 | 2025-11-21 04:21:00 | NOAA-20 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 36ff7e38-b196-3406-87af-b3f90f728f8e | -27.56457 | -48.66116 | 2025-11-21 04:21:00 | NOAA-20 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae557dd1-f3d4-3c81-990c-b6a47709442e | -31.43314 | -52.69503 | 2025-11-21 04:21:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 4b0904cf-40e4-3b21-8466-1b48174d5b3d | -25.28379 | -49.30586 | 2025-11-21 04:21:00 | NOAA-20 | ALMIRANTE TAMANDARÉ | PARANÁ | Brasil | 4100400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e39431e9-b6b6-3fcd-9ce2-26a8513b593c | -3.84818 | -43.36557 | 2025-11-21 05:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d025d1b8-d688-3471-9c49-521c20a494bc | -4.00611 | -42.48823 | 2025-11-21 05:01:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1c3c00c0-9574-3886-a8d6-2ec2328d360b | -1.63746 | -52.0524 | 2025-11-21 05:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38f976d4-0e58-3c2b-bc55-9ce2460e8de5 | 0.80955 | -51.84951 | 2025-11-21 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23d82aaf-3e9a-3061-97c9-06e16e25b44f | -3.99942 | -42.48724 | 2025-11-21 05:01:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c29cb3a5-8ece-3572-adc8-29d2870f2bd1 | -1.90124 | -45.60688 | 2025-11-21 05:01:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1658140-d650-379c-a2e0-689603d0ddc3 | -2.89259 | -41.68822 | 2025-11-21 05:01:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20d05ee8-7214-3817-b12c-f5c1936552b8 | -3.31843 | -45.5672 | 2025-11-21 05:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd417869-dd0c-30e2-9f14-e4697c800fa7 | -2.90168 | -45.36904 | 2025-11-21 05:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a97f43d-1df3-3b20-af7e-1964ab182a1f | -1.63685 | -52.0563 | 2025-11-21 05:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8c68902-fccb-3d81-ada6-e1768ec41af3 | -1.52856 | -52.9533 | 2025-11-21 05:01:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89fae873-c97c-31df-916b-efae5d437ab3 | -1.25148 | -52.63472 | 2025-11-21 05:01:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7eeb3ee-7b5f-37c1-a977-a82da3309807 | -2.89356 | -41.68172 | 2025-11-21 05:01:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0c2a524-bfd0-31ed-8e0a-a9e535a781a7 | -1.63624 | -52.06018 | 2025-11-21 05:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da8d03a2-2e72-32df-ad7c-b4b01d70dd0c | -1.52912 | -52.9497 | 2025-11-21 05:01:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbcf2c92-6fbf-339d-9216-29167d146222 | -2.22769 | -53.64508 | 2025-11-21 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df2a5f44-286c-3c19-93b6-5b5bb06ed40b | -2.23048 | -53.64912 | 2025-11-21 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91ffc1cd-a36a-3f42-84fa-37d0bb759f24 | -1.52573 | -52.94918 | 2025-11-21 05:01:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e052968-d3df-37be-8c00-c3c8a7882dd2 | -3.85522 | -43.36158 | 2025-11-21 05:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9e9bc07-9674-3d5e-86f6-02d3ab60def9 | -3.21339 | -45.47614 | 2025-11-21 05:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46ea457a-f4f8-343f-b4c3-e60c4a580963 | -3.31792 | -45.57067 | 2025-11-21 05:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 980f8e29-7f57-3156-ac7a-37b84e0b3c66 | -2.23103 | -53.6456 | 2025-11-21 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4410b72-718c-35be-b764-056910f67e77 | 2.34678 | -51.53591 | 2025-11-21 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8df0fd8b-1646-31cc-9cc3-8585b2d26182 | -3.31299 | -45.5663 | 2025-11-21 05:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fb11f83-266e-3ca3-8c39-f50f0bb21eee | -3.14211 | -45.34409 | 2025-11-21 05:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a9d51a1-271e-33fa-95b8-9c96380a5227 | -4.05151 | -45.99212 | 2025-11-21 05:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a90440c-1d80-3f22-92eb-d32cfa0d8850 | -4.00696 | -42.48223 | 2025-11-21 05:01:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 78d6980c-4b41-375e-acb0-c56c154d927c | -1.90075 | -45.6102 | 2025-11-21 05:01:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 838969b5-bd51-3903-aba2-3b2c960a3432 | 0.84691 | -51.84468 | 2025-11-21 05:01:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a9a3a6-16cd-314b-b119-83dc62d30408 | -2.89302 | -41.68561 | 2025-11-21 05:01:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 97605a45-9054-3266-9da5-6eeb8d20ba55 | -1.63334 | -52.05575 | 2025-11-21 05:01:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a7d91bc-28fa-37af-8a87-c5fb6346ba47 | -4.37944 | -45.52029 | 2025-11-21 05:03:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fe8e37c9-a47c-330f-b038-e7923b4441a0 | -8.12575 | -55.29809 | 2025-11-21 05:03:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eff3bdef-66a3-3165-be92-c2428b7accbe | -4.37389 | -45.51945 | 2025-11-21 05:03:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| db58e944-9525-3f81-9c3a-706dc76090e7 | -6.16246 | -46.10459 | 2025-11-21 05:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6a448e2-597e-3e5b-aea9-43d4aad1ea90 | -4.67154 | -43.22221 | 2025-11-21 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 271bf7f5-8186-3b5c-b005-fd840b679162 | -6.16797 | -46.10516 | 2025-11-21 05:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c88bcd5-8a0b-39d9-8710-a56124b8ed5e | -4.37892 | -45.52397 | 2025-11-21 05:03:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f8ef4777-92f6-32cb-99df-79fdfe4fb91a | -4.37337 | -45.52314 | 2025-11-21 05:03:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fe3515ca-c281-3965-8f8a-6190514a41db | -4.37499 | -45.51754 | 2025-11-21 05:03:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b024339c-c23d-3b34-8bf6-8ea65e93d57f | -4.37389 | -45.52491 | 2025-11-21 05:03:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b8104af3-cf77-3302-a31e-b07f4146e85d | -4.37445 | -45.52119 | 2025-11-21 05:03:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4d8d6ad8-fd67-3019-8b7c-8aeac09377fe | -4.67217 | -43.222 | 2025-11-21 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a71d29f6-fead-3746-8f96-e1dc1d32349d | -5.70581 | -47.06444 | 2025-11-21 05:03:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4435e616-8cd6-3e59-97d6-b7d1f8c6c0ad | -8.86106 | -62.95292 | 2025-11-21 05:03:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e91d0bd-79cb-3e40-9dd4-7dbd1ae27126 | -6.22162 | -48.07805 | 2025-11-21 05:03:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5b12260-a164-3f73-b550-b0c63427f087 | -6.16296 | -46.10099 | 2025-11-21 05:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5d109d2-185b-3ad5-a0a2-044d64b7aba6 | -5.66502 | -55.76916 | 2025-11-21 05:03:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bbcf88e-5be6-3ca1-a198-cf6f3f9fe8e0 | -12.8766 | -54.7427 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 940ea6f3-0fab-3127-9dbd-b17a3847717d | -16.40948 | -54.90049 | 2025-11-21 05:05:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72409edc-fed1-35ab-846e-f508f75a445a | -12.55287 | -54.80381 | 2025-11-21 05:05:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c1eb7e0-8255-3b43-af7c-35bc929ead17 | -15.13447 | -56.68334 | 2025-11-21 05:05:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4780f9df-be9c-3a77-af92-0c8371087fc4 | -12.86787 | -54.74261 | 2025-11-21 05:05:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f34e36b-99bd-3ce9-b179-5e1b0a2ae046 | -16.63296 | -51.30407 | 2025-11-21 05:05:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53234b98-5aa1-33bf-ac50-480e4edb0baa | -13.73946 | -48.44934 | 2025-11-21 05:05:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db96b980-8ee8-3f71-a4db-2194bb8c7c5d | -15.52786 | -58.83825 | 2025-11-21 05:05:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474eab2a-a166-3693-9159-8b7663393636 | -17.08056 | -46.59913 | 2025-11-21 05:05:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2943a63-7814-3aa6-b9af-932cfc852213 | -15.55869 | -58.88094 | 2025-11-21 05:05:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f333c9a7-5934-34e6-93d7-24c454b8f046 | -13.73805 | -48.46133 | 2025-11-21 05:05:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3a1f1e6-a822-3db7-89a9-9194c3e1b40a | -14.93032 | -56.27645 | 2025-11-21 05:05:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 415911cb-9628-30a8-8868-9262ac8e5de7 | -12.79493 | -52.02579 | 2025-11-21 05:05:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac0999a6-a814-3224-ac7f-785eb523fce3 | -12.46376 | -51.49237 | 2025-11-21 05:05:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9585153e-4a56-342e-83fe-2adaafec53fe | -14.4098 | -56.86704 | 2025-11-21 05:05:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce74a7b-658f-3886-ae85-3278fdc4c613 | -15.48331 | -58.7149 | 2025-11-21 05:05:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05af328c-b5c2-3bce-bc79-97f0bac89b1c | -15.20315 | -57.03515 | 2025-11-21 05:05:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README11.md)
