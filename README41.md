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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a80d087-199f-39eb-982b-a227b478bb85 | -13.20847 | -48.56546 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8831d4e3-4ed6-3866-bcd7-9cfb0c9b1e60 | -13.20569 | -48.56139 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f47cd7eb-be28-384e-913b-28ea44c644c0 | -13.20514 | -48.56492 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 763b771e-590a-3567-800b-3d19c6160572 | -13.20182 | -48.56438 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5b7f533-5fb9-3426-847f-798ef83d2a38 | -13.19849 | -48.56385 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9de2056d-8eff-3d19-8684-56157e903341 | -13.19517 | -48.56331 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8aed2709-2cd2-3613-8aba-0c59010d3216 | -13.19287 | -48.53401 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac8c8fdb-d76f-313f-95d0-d846b8c41190 | -13.19232 | -48.53756 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6433b9bf-354c-34ca-b6ee-0e184bf36afa | -13.19184 | -48.56278 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 778d64aa-d9be-360c-b316-4b69e24d307a | -13.18955 | -48.53347 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e038bf3c-074b-3de0-876b-2b92ed31c7b5 | -13.18798 | -48.56579 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5af37f8d-050d-39f1-88b8-b85a8d5084a8 | -13.18465 | -48.56525 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f09d0460-8437-3a1d-988a-ce849331bf8b | -13.18404 | -48.54708 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d91ccb6-a3fe-3479-9f34-d1bf6cd1ba1a | -13.18242 | -48.55765 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cfc06a63-587c-32e0-99e5-dc0ff9091846 | -13.18187 | -48.56118 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5755103-be0a-3a8d-b3bc-d9f5451281e6 | -13.18133 | -48.56472 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ae70504-89c4-39d2-9135-0b4a069d73c5 | -13.18018 | -48.55006 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0aba119-0438-3966-9911-e4b909d8ba05 | -13.17855 | -48.56065 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ffeb871-d561-3d9b-a01d-c912e84881f8 | -13.178 | -48.56419 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d0c0aa7-e03f-3c8f-8a31-3b263714f5e9 | -13.17468 | -48.56366 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32c1f9e0-5aef-333f-b132-2b940bb71c1f | -13.16083 | -48.56507 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ee0e2ae-4fdd-33de-9f27-dcd7ee6bfbb8 | -13.1586 | -48.55743 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 808b1c0b-6b9f-328b-941c-4a6254eeb774 | -13.15806 | -48.56099 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ff025e5-fad4-35bd-892f-86b7afb454ea | -13.15751 | -48.56453 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f321d23-8e95-3b8c-8973-c26188162546 | -13.04385 | -48.61905 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1f2ebab-b117-336c-aa5d-125d6ed83f39 | -13.04161 | -48.61148 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14ba82de-8cf3-391a-9795-44aac634b8c1 | -13.04107 | -48.61502 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 973afdf2-16e5-3455-b6f2-d38041dc5d75 | -13.03998 | -48.62207 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4866f232-d042-3a0f-9809-d68003baa669 | -13.03884 | -48.60742 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e4f288f-c07a-3ca3-a885-3baf9fb177e8 | -13.03829 | -48.61099 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| beea5921-1240-39b5-9cc0-0055f96b4337 | -13.03774 | -48.61453 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac3d3194-e0e6-32cd-b600-fcac74e7bf63 | -13.0372 | -48.61805 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0c96d665-268b-3a22-9cfb-502240de945d | -13.03551 | -48.6069 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1425c9a3-4ef8-3aa1-b2f0-45526c9276cc | -13.03333 | -48.62105 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32e85e57-0a5c-385b-92b7-2ede5cd498b9 | -13.02997 | -48.59866 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c411d804-847f-3ec4-9269-c0944bea6edf | -13.02638 | -48.6025 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de62aae0-2bc5-3afa-9ea1-918776b6892f | -12.98254 | -48.53371 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d61af90-48b2-3790-a5dc-4e9e76e435b8 | -12.97922 | -48.53319 | 2024-09-30 04:32:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c63cdf73-deae-3cf5-bb58-e63286d2205c | -12.9759 | -48.53266 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d075ffd2-9f49-3d41-9640-0aef92554722 | -12.97258 | -48.53212 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06185b4d-75e4-3e05-84db-3d9a63e42986 | -12.96925 | -48.53159 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c53fa0f5-a4dd-31e8-94b1-ca5c34949d28 | -12.96593 | -48.53103 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f751b7fa-2757-3140-a2a5-bfd728de78e2 | -12.95652 | -48.52585 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28f3546f-759a-3036-bcaf-d8bf20b5643d | -12.95597 | -48.52937 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52f46dcc-733b-3e79-b7f2-5678f99bb407 | -12.9532 | -48.5253 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7eccd9b7-0518-32d0-bc86-143173623d91 | -13.66847 | -48.64234 | 2024-09-30 04:32:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5007a1fd-549e-3c4c-b8c5-d50c6b55ef90 | -13.49304 | -48.58902 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c5d6f681-570b-3281-87b4-cb099bf37f64 | -13.49249 | -48.59257 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2fb8b619-d127-3b15-87d0-5de4ca4056ff | -13.48862 | -48.59556 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| affed75f-11b5-33a2-a9b9-4d5e29cfa21e | -13.48584 | -48.59149 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12bbf0ee-ab28-32f7-acc3-99accf79a81d | -13.4853 | -48.59503 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15535d3a-cb8b-39f7-9f67-a42850694a20 | -13.48475 | -48.59858 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6277e74b-2006-381e-b24d-daf6c5274b31 | -13.48311 | -48.60927 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88d1bc2c-b569-3972-a15c-0cee2fbfd435 | -13.48256 | -48.61283 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6e954d0-eddd-34a7-b424-86babefcc853 | -13.48142 | -48.59805 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da729ce4-7a5c-3e14-a015-6e55e14f2c5a | -13.47924 | -48.6123 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b1f57f7-5e90-3933-80c3-45a92fb38d3b | -13.47869 | -48.61585 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe9a5d50-8cb6-35e2-9483-c73c0d3a7989 | -13.47865 | -48.59396 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d540af4-d784-30aa-9acc-4d5896166d60 | -13.47591 | -48.61176 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 497b14cb-5a08-3a54-a146-9331a12ad942 | -13.47536 | -48.61531 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9177b900-de13-3af8-9b72-678f048fd2a7 | -13.47482 | -48.61888 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ee83e43-1eb0-3489-a65e-44f93d2b086d | -13.46097 | -48.62033 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| faf19a21-57a0-3d16-a82b-a1d6e48de2ab | -13.45922 | -48.61293 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72b7f7f4-579d-3eb5-990a-a706be70631f | -13.45867 | -48.6165 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73e67a7f-f50d-30b5-8f40-24055f8e93b9 | -13.45812 | -48.62007 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d78c4fc7-4491-3a15-8a73-e32880994379 | -13.4559 | -48.61241 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8dd53b9-7e4d-3d26-9fed-2364c59aaaed | -13.44422 | -48.57767 | 2024-09-30 04:32:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf407c55-e22f-386c-8175-9c4667eee7fa | -14.62439 | -49.58812 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abf2f76c-8fc9-3ba3-84d9-786f65db3c81 | -14.78863 | -48.74689 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24e46b32-07fb-394b-aefd-28f8b8b11d17 | -14.76973 | -48.75879 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 685244d4-e174-3945-a2d4-2e760ce61790 | -14.76696 | -48.75461 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f533acb-55aa-3271-948d-0304665630bc | -14.76473 | -48.74685 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73e9e90b-1905-3d8b-8fbb-8049f0e9e706 | -14.76362 | -48.75407 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 587fbe75-669a-3b1c-b36a-1918e746ff37 | -14.76307 | -48.75772 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9170248d-808a-3edb-9ae0-a84b9fbf91e1 | -14.76194 | -48.74267 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39a939dd-bab4-391e-8d7b-c550b366b9af | -14.76139 | -48.7463 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af4d80b7-87ca-31fb-9c28-0feeedaaa2d3 | -14.76084 | -48.74992 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 05bae721-6b39-375a-8795-30488a49f5c6 | -14.76029 | -48.75352 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ba6eb69c-7c18-3b73-87c9-45ecc94aa4d5 | -14.75974 | -48.75717 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aee7bfa2-ceb0-39fa-9890-4cb8b4f263ff | -14.75861 | -48.7421 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9525d03b-d5af-3cc1-8685-a9229b737c0c | -14.75806 | -48.74574 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dea2fcb0-54ef-3d2f-b2e1-3d59961f53f0 | -14.75751 | -48.74936 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 61a86be2-6b38-3f9e-ac3c-1e8d097b637f | -14.75584 | -48.73789 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d16afc2b-cd4b-3d0b-93d7-29d03b377a54 | -14.75528 | -48.74154 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 43efb521-b244-3955-958b-4b938ffd65b0 | -14.75473 | -48.74518 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 959f2652-5a5b-3036-97c7-d15221a41e24 | -14.75195 | -48.74097 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 556dbfc4-b342-396e-ba73-3775388e376d | -14.7514 | -48.74461 | 2024-09-30 04:32:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34343d89-d8a8-3726-9c9e-9be0fe52146d | -14.99898 | -48.52026 | 2024-09-30 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c391b17-65aa-3adb-b524-475c7c9f7813 | -14.96069 | -48.51054 | 2024-09-30 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da75d990-dc64-30a3-b29d-19a348a7d92e | -7.77239 | -49.48304 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0235d83d-b964-3da2-873a-1bad873b3a78 | -7.74646 | -49.21404 | 2024-09-30 04:32:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4b490d2-b468-3769-9aca-5f76eead5ea6 | -7.74589 | -49.2176 | 2024-09-30 04:32:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 935b5f5d-c71e-3505-b521-55fede67d4a1 | -7.66795 | -48.53405 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba27f67-e7b5-3e39-9f0d-426f004ec097 | -7.66463 | -48.53352 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40e4157c-e00e-3c20-b84b-022455f6ebd7 | -7.59194 | -49.18548 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a79f3c68-8a67-327c-ba5c-2ca459cf9624 | -7.59085 | -49.1707 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce1ef12b-a3b5-3e57-a3ec-8828bc3203ef | -7.59029 | -49.17425 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9ede1823-37e7-3f6e-b7bd-2e53e31ae0d4 | -7.58972 | -49.1778 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 557304c1-2d0d-3ac9-ba04-915aacd9e112 | -7.58916 | -49.18135 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab557eca-2940-307b-a6f7-6775e0990568 | -7.58859 | -49.1849 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README42.md)
