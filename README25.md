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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bef4cde-092e-3955-bbc9-7406c031d10a | -21.19893 | -50.48209 | 2025-08-28 03:47:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 24bff564-7acd-3327-a56d-fda25c5c1402 | -20.14098 | -47.37585 | 2025-08-28 03:47:00 | NPP-375D | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b681d0f-ba04-3e8e-88d2-3d8963e730b8 | -13.67056 | -46.88606 | 2025-08-28 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 78557fdb-e3db-3894-9295-4d2c4bd1126d | -12.95418 | -46.34188 | 2025-08-28 03:47:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee282b59-af17-381f-9cc0-297eecdb7bd9 | -13.42412 | -46.992 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdfe1c98-bc85-35c2-99fd-200837165cbd | -13.42049 | -46.8544 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b6599a1d-a1c0-3cbc-804c-27584cff25ee | -12.81104 | -48.14636 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 613560be-7259-3b77-9124-cf2cb8eb6cee | -12.8692 | -48.11132 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e8d6900-a46f-30c4-b0b8-413d94a9363a | -9.86412 | -44.69064 | 2025-08-28 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6a6676f-7b73-3e35-81e8-48f5d111ca0c | -20.25161 | -42.01275 | 2025-08-28 03:47:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 667c0c5a-27a6-3ce0-98cd-9e2949e0ec87 | -13.42127 | -46.85049 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a2345b9b-c69e-3222-bc2f-fa5464a3ea3d | -12.40297 | -47.7926 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 107095f5-e53b-3d21-8cfc-b1aae0cb12ec | -13.4324 | -46.9803 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9178ea85-786f-3d1e-8e84-a045aa19ddbc | -10.70366 | -47.02169 | 2025-08-28 03:47:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0eb46961-f00f-33d0-b330-eba18bf94a47 | -14.13701 | -45.40775 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29063aa5-f59b-3e75-ac84-a050a85ab254 | -12.78631 | -48.18176 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ff6def8-39dc-33ab-9dbb-9faa5a5d6603 | -13.5509 | -46.91536 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dc5435e-137b-3439-b664-68ef60914bb8 | -13.55339 | -46.90273 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6248b6de-0a7a-3ef6-bc7f-57d2fc5e0b93 | -20.67965 | -47.07451 | 2025-08-28 03:47:00 | NPP-375D | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a2020df-a855-3afd-8823-76c0e3d36b83 | -13.5201 | -46.92341 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af4c12b7-5879-3575-ac91-f24f2bbb2b66 | -12.79266 | -48.14253 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ad272b4-a54b-341b-ae38-e1e9caf1bae7 | -10.54133 | -46.68785 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a480d36f-08a9-3ec6-871d-adc1ce5e6151 | -12.81906 | -48.13842 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cdafcda-997f-3267-b05f-18bed3911edd | -11.32851 | -43.52123 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06d3d741-5be6-3cec-b690-3a96008197d8 | -10.32704 | -46.78004 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 234c5b66-4f17-3b0d-9005-cfb441e01163 | -13.45529 | -46.98332 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1030d19a-d678-3320-820b-6dae7034ba8b | -22.68277 | -46.84493 | 2025-08-28 03:47:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d111249c-7722-3f95-9936-b6e1cbb95be0 | -13.46999 | -46.85358 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f69f0f90-5c12-3a12-b17d-4ed8df7eee1c | -11.3333 | -43.54778 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 505f9056-5a42-3dd9-9b97-735c9876a312 | -20.43601 | -46.01441 | 2025-08-28 03:47:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edde947a-338d-379f-98d1-a71c22bb7a98 | -15.08148 | -48.64464 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e134d01-84cd-3b0c-912c-eb11cf6b29af | -13.55175 | -46.91108 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bbaa845-c2ca-3f56-8ae7-6c332077e185 | -11.65213 | -44.87418 | 2025-08-28 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95832f4f-ebf8-32f9-b5dc-c858c642a482 | -20.09112 | -43.74438 | 2025-08-28 03:47:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 090200bb-905c-3cb9-9c3e-4655dcc41bae | -13.53609 | -46.93114 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21c40946-5874-30b3-88c6-82692a203faf | -14.13816 | -45.4018 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbe3353c-7020-3980-842a-d63a43f7b0f3 | -13.18173 | -45.28976 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44f3f244-98e5-30b0-baf4-ad80ac6ba579 | -11.32953 | -43.54197 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f870108-16e3-3516-8ee2-e52ab32eabbb | -11.83935 | -46.80087 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a1861e6-42cf-3264-a7cc-4a62035d64db | -11.33044 | -43.53701 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| caf02c47-c427-3d45-b454-d5f0a883bf3d | -13.97443 | -46.35098 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1330016b-4356-3d5a-9d62-b406485d0503 | -13.46131 | -46.98259 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f35e7905-1c1f-3e23-bb25-0cb873230dc6 | -20.1163 | -44.34112 | 2025-08-28 03:47:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9af287b0-e19b-3ee5-934c-ad756a146a5a | -12.78226 | -48.17002 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49651cf1-e258-39d7-a316-a02665ede4d1 | -21.89609 | -43.30786 | 2025-08-28 03:47:00 | NPP-375D | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0792a91a-5fbd-30d4-8776-6f6fc91993f1 | -13.47559 | -46.85469 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0fe2393f-7c17-3cf1-af81-cc11da34e5d5 | -13.4326 | -46.85208 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a01fa1da-df51-3b7d-8b7c-41425cea364e | -12.96371 | -44.57598 | 2025-08-28 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b923ff13-8e39-3829-bea2-d17795ef6437 | -14.14145 | -45.41184 | 2025-08-28 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 317c4222-de3a-3f5a-be94-967c4bff699d | -12.81864 | -48.10935 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f45c5bd9-187a-33db-96a7-9f0b32529cfd | -13.83488 | -46.68466 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d32aed22-7e02-3432-9e2f-d5989b1ed96d | -13.42258 | -46.99948 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 322d1d40-18ba-3072-9ef5-eae8db20c37f | -12.79016 | -48.16249 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e05df94-84dc-3436-b2aa-c5506d131e5d | -13.42577 | -46.97502 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b581ab57-726b-3134-8d00-0f28806a9944 | -9.85951 | -44.68654 | 2025-08-28 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1f79a98c-7d15-30b4-b8d0-1b527413fa98 | -13.45472 | -46.97701 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9eac91a-88c9-3be8-804a-491fd44e9149 | -13.45387 | -46.84693 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd1347f5-1554-38d2-a573-cfbb52906735 | -12.409 | -47.79387 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9082995-4197-33c9-901f-f8035cc5159a | -13.51342 | -46.86931 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64286548-d1b5-3046-941b-60811fc46e9f | -20.4373 | -47.34013 | 2025-08-28 03:47:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3175c9b4-8c05-3bd1-9ec1-9c930a4f4b09 | -13.39079 | -46.8861 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29b668eb-ebaf-3d7f-a930-1b9461ec0964 | -13.62572 | -48.21555 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da0da061-a0ac-30db-9f3f-87b6e5a3b84f | -21.69746 | -42.41999 | 2025-08-28 03:47:00 | NPP-375D | PIRAPETINGA | MINAS GERAIS | Brasil | 3151107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d39bdfe-cb55-3998-9fc2-62c8b0753b50 | -13.73874 | -42.68457 | 2025-08-28 03:47:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fce5edfc-afa1-3f90-8ef0-9cccaa240bc7 | -13.54798 | -46.91611 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f80645b8-faae-3f4b-9337-8d086a53bab8 | -13.42925 | -46.96698 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bfc985b7-b3bf-322f-be70-6fc78b4fc6cc | -11.33228 | -43.52706 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b19d72e-7c47-3fa7-8410-8b3adda58808 | -21.0289 | -46.23275 | 2025-08-28 03:47:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f8acbedc-ca0c-3b11-9708-c7315f8a6735 | -12.79566 | -48.18994 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4591434-082f-39ae-b215-b6443691881d | -12.44266 | -45.96518 | 2025-08-28 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02cfaefc-0386-3d8e-b65e-4516ce7e1c51 | -22.67804 | -46.84406 | 2025-08-28 03:47:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e8341bf6-eb60-3ebf-b673-c0e3bbf928b0 | -13.50874 | -46.86357 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09b71873-9e79-3d22-a964-3ebdb48eb245 | -10.53468 | -46.69091 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10549fe3-e7af-346a-b004-964ccc1828fb | -13.59859 | -48.22406 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff8c615d-94f9-3af8-884d-543d13538c95 | -11.55315 | -46.34187 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43f3aa8d-c899-3d90-9af3-a212ba4664db | -13.17606 | -45.29181 | 2025-08-28 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28a73dda-8b4d-32ad-adc2-0e23d90e9d1c | -12.78552 | -48.17702 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db5421a4-50e1-3047-ac3d-fcb717bb1b46 | -13.44685 | -46.96706 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 619ddc27-74d2-317c-b3d8-7d07ed3d4586 | -12.72107 | -48.18756 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 11ffdd18-e1d9-3713-9f55-bd9014fca46b | -12.81806 | -48.14328 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71a446c0-8b7b-3c09-9faf-6f3ef9f1eb65 | -12.70537 | -48.17023 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2597f7dd-eb0c-363b-b1f6-8e0c471591ff | -22.16526 | -47.07496 | 2025-08-28 03:47:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eb2d839-5eda-362a-b556-6a25c9f17879 | -13.98047 | -46.34866 | 2025-08-28 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f7ec4d2-8946-3646-972f-3aced9e628b5 | -11.81233 | -44.25922 | 2025-08-28 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5a694e3-f907-39c6-a161-f8658de1319e | -13.54858 | -46.89757 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c608dec1-c8f1-3cc2-b9d9-a04121e4c0b3 | -10.54212 | -46.68372 | 2025-08-28 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe231e42-24d9-3047-bceb-5e3a6606689f | -11.56009 | -46.33615 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d89f231b-e295-33c9-aeaf-213f3bd8c4d4 | -15.08412 | -48.5108 | 2025-08-28 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2153455-4d37-33bd-93ef-6b7f406d9b73 | -13.54884 | -46.91191 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30f4f61a-0271-3ee5-8bbe-482861afd409 | -11.57393 | -46.41495 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 847d9a97-427e-34a2-9851-6620ae9a6930 | -11.32485 | -43.54107 | 2025-08-28 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09628390-9be3-3a3d-a2b6-4f46e9bc146a | -13.38861 | -46.86797 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1daab6d7-fdae-3185-bde6-11d421d6d848 | -11.24358 | -44.9836 | 2025-08-28 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 195036c3-0782-3191-aee1-d3650224b171 | -13.4734 | -46.85184 | 2025-08-28 03:47:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f99c0b5-ed30-3d09-9afd-9289d5293b86 | -13.60431 | -48.22872 | 2025-08-28 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef4585dd-3723-3c00-acf9-9951a3c13143 | -12.43183 | -45.96339 | 2025-08-28 03:47:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f77bbbbe-b2e3-3938-bc66-929ea498c0a6 | -12.79883 | -48.1436 | 2025-08-28 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78b93b14-3a45-3ceb-969e-7fe2c80e2d06 | -20.09513 | -43.74551 | 2025-08-28 03:47:00 | NPP-375D | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7ca0068-3f5a-385d-af71-94294f33abbc | -20.3084 | -46.03793 | 2025-08-28 03:47:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e3dae56-adbb-35b8-a0dd-a531210e3c2e | -11.56665 | -46.39224 | 2025-08-28 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README26.md)
