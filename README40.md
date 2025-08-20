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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2430c242-c2c7-3fef-962e-50fce1ef9b1a | -14.9913 | -54.82677 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c150b39-5d9b-3b62-a51b-6cd5d0bb2e89 | -22.45137 | -47.55357 | 2025-08-20 04:38:00 | NPP-375D | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5aace6e8-2db3-3df8-af2a-cdbf7d1a95ab | -15.64966 | -52.68796 | 2025-08-20 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4db8866-c694-3d11-a1ef-2f55fd3ad33f | -21.13184 | -47.03347 | 2025-08-20 04:38:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d9ca37c-c8ce-39e4-9df3-8788d8142d2c | -21.27223 | -45.40425 | 2025-08-20 04:38:00 | NPP-375D | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| da63cf53-2608-318f-a94f-662e099ab443 | -14.99936 | -54.82827 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52db5324-d2ac-3c0d-a529-97f2b504109a | -19.87551 | -49.8417 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b43192c6-68af-3545-a3ed-3dc967471741 | -21.90411 | -47.2234 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 1fb6313c-3fdb-3a4b-ab75-122e7fa36fa6 | -18.2053 | -47.9328 | 2025-08-20 04:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d16d8497-0327-36e0-ae29-02eee9fe8d13 | -21.50486 | -45.46265 | 2025-08-20 04:38:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 498a070d-f79d-35cd-b55c-e945ddcdffee | -21.90032 | -47.22284 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| b46b2aae-13e1-3028-9191-afefee480dfc | -22.69017 | -47.3416 | 2025-08-20 04:38:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83015278-f47d-35f0-a417-41600b790ccd | -19.12185 | -46.60391 | 2025-08-20 04:38:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e5da399-25c3-340a-840f-e393ae9af426 | -17.08923 | -48.97942 | 2025-08-20 04:38:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fcde7cb-fbe5-3b7f-b0d7-c50cfe8cfd9e | -22.45448 | -47.55895 | 2025-08-20 04:38:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 83ead413-eb3b-304d-80a9-2832ed99efb5 | -21.91002 | -47.24284 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 32d66482-2f59-3fff-90d6-c9236e0a3c28 | -16.74245 | -50.04229 | 2025-08-20 04:38:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ed57d88-abd9-33c1-9a85-e4fba3113deb | -22.26963 | -48.50016 | 2025-08-20 04:38:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 123d3ab2-2969-3023-b3b2-9f05e306a48e | -15.06732 | -54.84372 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff50e99-91d2-309b-a763-ccca3511ac2b | -20.76914 | -49.41293 | 2025-08-20 04:38:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31e06d50-e283-3aa0-b2c4-488733df9867 | -17.41186 | -46.69569 | 2025-08-20 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8395f64c-9771-3fa5-b276-9707dfa403a9 | -21.90661 | -47.23385 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d26fc46-adcc-3aa5-8f46-d0fa9fc05ddf | -15.0047 | -54.82174 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e12f02d0-4262-30d7-8fd9-c40a32361bdb | -15.06666 | -54.84731 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a41ddf4-79b0-3784-a45e-0327ee7d8033 | -19.35383 | -47.93889 | 2025-08-20 04:38:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 04a18373-0c04-38cb-b082-6d446c89e8f5 | -22.41299 | -46.62071 | 2025-08-20 04:38:00 | NPP-375D | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bee25ae0-dd79-3e40-bedc-e96af5b82438 | -19.56668 | -45.97345 | 2025-08-20 04:38:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6092d49d-c42c-3ad7-9592-395671364a1c | -14.98728 | -54.82602 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8b5afef-a9ae-34dc-9049-7b8b75828411 | -17.61481 | -46.70286 | 2025-08-20 04:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a34342f9-4b98-3ab5-8ce4-13250c2d4d33 | -22.37286 | -50.40646 | 2025-08-20 04:38:00 | NPP-375D | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1097f8f-9545-3093-8a5c-f655378162ec | -19.88337 | -49.83533 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74828bcc-31e0-3d6f-909a-bcba8513c0df | -19.7265 | -48.97391 | 2025-08-20 04:38:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a3b58f1-f161-35a6-a56d-d3ef31930b83 | -20.75433 | -48.87322 | 2025-08-20 04:38:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f8e0814d-060b-3ba2-bfce-e0d8480e27d7 | -20.75779 | -48.87379 | 2025-08-20 04:38:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e48c837d-16ad-3a59-998d-1800cc2edf1d | -20.04056 | -48.87893 | 2025-08-20 04:38:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b110312f-bff4-302e-8eec-c3fd369f59fd | -19.85592 | -49.83456 | 2025-08-20 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f6778c26-05c0-32f3-9078-ba31f4e42ca7 | -15.00134 | -54.81734 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eefb3dff-6a06-36f9-8c11-4c13411bcacf | -22.41061 | -46.61927 | 2025-08-20 04:38:00 | NPP-375D | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b53ffdea-b81b-3f20-9732-1ad1dae91698 | -21.90347 | -47.22834 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 4b010e57-ed63-3905-9931-4aa252010e4e | -16.34796 | -50.17906 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c39b50c-e5d7-3c79-96d7-9b53d495cad4 | -16.29256 | -52.93737 | 2025-08-20 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbbb993d-7b65-3487-b0e3-75f38ca66fcd | -20.34601 | -51.71402 | 2025-08-20 04:38:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b634ef95-7bc8-3fd7-9cb5-36a4fc571209 | -18.67871 | -46.97838 | 2025-08-20 04:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36acc1d7-d5b2-3bef-8b8f-7ba695b843ef | -18.18134 | -47.89975 | 2025-08-20 04:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9ac1920-3d50-3a2d-81c7-1ed123181f42 | -16.31414 | -50.17699 | 2025-08-20 04:38:00 | NPP-375D | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0fa4940-96d7-3b48-bc04-a3de2e4bc58b | -15.87239 | -50.65917 | 2025-08-20 04:38:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d68ec437-1b1c-373e-babb-bbd03c777396 | -17.33914 | -47.15948 | 2025-08-20 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b745e76-57d7-335b-8c74-b6007ea9c020 | -15.02644 | -54.83958 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f36a95c5-d19e-3fb2-90f4-35be63536aee | -18.80072 | -52.60295 | 2025-08-20 04:38:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61370cc7-729f-377d-b095-74df6fe59307 | -15.00332 | -54.80645 | 2025-08-20 04:38:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea40ad60-f42d-337a-80e3-7123063eb772 | -21.90095 | -47.21796 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36ac4cb7-7369-37d7-972a-3a051fba4b73 | -19.72593 | -48.97781 | 2025-08-20 04:38:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca26ef96-ace8-3c2f-a77b-00da9394ab14 | -21.90068 | -47.2264 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| 6438fbe4-c74d-3eb0-9527-3b607889d3b5 | -18.17782 | -47.89923 | 2025-08-20 04:38:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d34e8d8-38a6-360f-a41c-6ce95d0e78f9 | -21.90283 | -47.23331 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eb1a4878-841f-3d45-8fa4-176fcaa3d670 | -21.91354 | -47.23989 | 2025-08-20 04:38:00 | NPP-375D | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c6e8f81f-89f9-3b85-8942-b6664ed69399 | -22.36335 | -50.40089 | 2025-08-20 04:38:00 | NPP-375D | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8673b643-4cf3-308b-86ae-647106fd01df | -13.1555 | -54.9357 | 2025-08-20 04:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 454969ef-12f3-3b76-8ae3-c41af743f26f | -13.1364 | -54.9376 | 2025-08-20 04:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.7 |
| e643452e-babd-3410-8395-48d9e08bb661 | -13.1558 | -54.9151 | 2025-08-20 04:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 71845f3b-630c-312c-b2f2-382ba4314372 | -13.1367 | -54.9171 | 2025-08-20 04:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 029be5b2-d037-30ad-a856-eaf690596461 | -23.9908 | -48.56265 | 2025-08-20 04:40:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3f6788e1-457b-382c-be5b-defba202235b | -23.34665 | -50.86065 | 2025-08-20 04:40:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b36d4ec-838e-3fef-82d4-bb80c115ceec | -23.99141 | -48.55816 | 2025-08-20 04:40:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 254abd8c-575f-371f-916b-711d33d18f75 | -23.97296 | -49.65199 | 2025-08-20 04:40:00 | NPP-375D | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39537c88-bc96-3f5a-8bf5-50ba7fb72dc3 | -23.34607 | -50.86447 | 2025-08-20 04:40:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d8cdbe0c-0562-3499-83a9-92e9d9f91ee8 | -23.97642 | -49.65258 | 2025-08-20 04:40:00 | NPP-375D | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9b1a6f0-17c2-38bc-8c43-6f6f4c4e4b7a | -23.99559 | -48.60971 | 2025-08-20 04:40:00 | NPP-375D | TAQUARIVAÍ | SÃO PAULO | Brasil | 3553856 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7178fa3-7573-31c2-bbe7-784fed848964 | -23.70132 | -50.23453 | 2025-08-20 04:40:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2ed084a1-4174-31c9-8447-ad679e044940 | -23.84799 | -50.74213 | 2025-08-20 04:40:00 | NPP-375D | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f49e7a13-9282-3ea3-8a78-af1b8ba62bfb | -23.85136 | -50.74268 | 2025-08-20 04:40:00 | NPP-375D | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 45919bc6-bebd-3743-a522-8bd9b34bfd4f | -20.339 | -51.7062 | 2025-08-20 04:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ea6c852d-0811-3d5d-877c-f2c2adeb48ac | -13.1558 | -54.9151 | 2025-08-20 04:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 8163fae5-21a2-3746-a06d-a2f31a41d408 | -6.9607 | -42.858 | 2025-08-20 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.7 |
| fbbc43a6-409d-3246-bdad-fa2108f2b79d | -13.1555 | -54.9357 | 2025-08-20 04:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| bbe33c4f-01e6-3763-85a4-25350f81fa93 | -21.0181 | -47.6454 | 2025-08-20 04:50:00 | GOES-19 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 063207b3-a419-3f1a-af98-2dcb362ed4b1 | -13.1364 | -54.9376 | 2025-08-20 04:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 90c1f07f-16a4-39e5-9cdd-1cd386baea03 | -6.86294 | -43.60471 | 2025-08-20 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae025cca-24db-3089-8869-c64dec1dddac | -2.77617 | -48.59821 | 2025-08-20 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad328275-d82d-3a09-ba70-f08a4a533406 | -5.79564 | -51.6697 | 2025-08-20 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df7e2b97-6a66-35b4-a25b-16888ab5bbda | -6.13156 | -42.95555 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 625603cd-2b76-3fd8-9015-6924f34db341 | -3.8758 | -50.97949 | 2025-08-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5086270-3d6f-3224-8572-8bb00144e43f | -4.64776 | -43.125 | 2025-08-20 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fddc932-1dd1-380f-b1b8-21f5f24b98a2 | -6.05128 | -45.0535 | 2025-08-20 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 50b133d6-f510-3c2a-984c-58b4de37e6ce | -5.9912 | -42.83929 | 2025-08-20 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bc64beef-6338-3249-bc61-8d9c9328e1f9 | -3.98215 | -51.06422 | 2025-08-20 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 828f1ba6-7e8f-3e40-bb8e-0dcbc5eefd78 | -5.63285 | -43.39264 | 2025-08-20 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba00ef7e-4404-3e81-b9d7-15f79e89b1ed | -3.98362 | -43.2467 | 2025-08-20 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0dab6894-145d-3c86-bea7-425641a8d282 | -4.17293 | -42.025 | 2025-08-20 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 083aaf30-c505-329c-961f-7a24d1e164fb | -4.60085 | -43.32295 | 2025-08-20 04:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f78d4dc1-b9ff-3400-b2e7-79265b547c21 | -6.86414 | -43.59576 | 2025-08-20 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9c3f8cb-690e-381c-9c23-0e9227af248e | -6.96792 | -42.86654 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7141cf94-9a22-37b2-a14b-6fac74abfce1 | -3.23433 | -46.79916 | 2025-08-20 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b688aa64-1053-34a5-9e9a-53384065ed7d | -5.86963 | -48.12024 | 2025-08-20 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdf9725e-91c5-30eb-8232-2854d0a10aff | -6.06491 | -44.11725 | 2025-08-20 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f041cac-82be-35ae-b2f8-39c440a014a9 | -6.5229 | -45.46808 | 2025-08-20 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 624e9b87-86cc-38d6-b667-5c52b62e5c08 | -4.16971 | -42.02684 | 2025-08-20 04:55:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e7e14f4b-3b11-3f43-b266-eb7209cba7e7 | -3.40119 | -46.90768 | 2025-08-20 04:55:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3173370b-824f-3802-b7e1-44494c766096 | -6.96725 | -42.87154 | 2025-08-20 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1d4dc539-df0a-3d6a-92eb-8818a702cbf2 | -3.97363 | -42.50915 | 2025-08-20 04:55:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README41.md)
