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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bce3ed4-07a4-3f68-a6f8-1470feba15f8 | -11.82084 | -44.96374 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a20d4906-0b52-3d5f-b99e-1fd28504bf16 | -10.08828 | -50.19604 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2585a7ae-f045-3d39-8098-c19328776771 | -13.13285 | -47.42382 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3594be59-f92a-3c56-af85-7e3bd1d1d137 | -10.91084 | -46.56634 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3528ff01-880e-3dd8-8dba-0cb1e38d55ba | -14.70382 | -48.22037 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 861058d0-6684-3642-a8ed-bc0712701a35 | -15.08878 | -44.96434 | 2025-10-01 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 523f204d-e396-3918-8fde-a88b5edf99d1 | -13.66384 | -48.04148 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 49f69100-2e12-3be6-95d1-c59942b1ea51 | -14.68528 | -48.1221 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd6f2540-c06d-3b8f-8e12-479e66815368 | -10.47833 | -55.62228 | 2025-10-01 04:21:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63ac4860-7d7f-3c37-b564-cd1809a23de1 | -14.98399 | -46.96036 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95975f51-1647-3edc-af68-635a91973744 | -14.00345 | -44.8406 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5910c8a7-b1e3-3fe1-950e-4508407c6eb7 | -15.25347 | -46.97584 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 054f7f3c-e979-317f-aa00-7fe37638cca4 | -13.34882 | -48.14559 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ca530e4-0a29-3b90-a402-d95c66ffe20a | -10.91454 | -44.30615 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 499b6442-ea1e-3bd9-a644-96e3f9120978 | -11.759 | -46.86213 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ee1a17f-9564-3de2-b5a5-7f8b7da3807a | -13.35807 | -47.80349 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fbdecc9-870d-36f9-9b19-3393509a60d7 | -12.78748 | -46.86068 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 721ccf19-9020-3784-9538-028265f675b4 | -11.64986 | -45.32516 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f64a06a-06a8-3e94-9e79-ddeccd460c28 | -13.91616 | -48.09511 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f3e7c3e-631e-39a6-b115-6f1d2230d97c | -13.46288 | -44.37426 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1085085b-4991-32cf-a1da-35503e95c4d1 | -13.5619 | -47.27729 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb02367d-a0fe-3e18-b7b7-d75634417d39 | -13.3072 | -47.20937 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc90fc1f-1220-39cd-b162-b31049fb93d9 | -10.91633 | -44.33992 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65c6d78d-3964-3ca1-be08-dea86666e7ba | -14.68403 | -48.12971 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb137ef9-23f7-3df8-a567-09c59391da12 | -11.80376 | -47.59515 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b15277e-a05b-302a-8e04-312334bbd8f6 | -11.81975 | -44.97085 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69812ade-ba5f-3a61-9a2a-8fcab33e019f | -10.90978 | -46.55169 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad3c750e-7e72-337b-8afe-e37f28c4a7ec | -11.5689 | -50.18419 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e404135d-18a2-3016-9734-99f22bb155fd | -16.57402 | -45.10746 | 2025-10-01 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 79df0c2d-bf0c-3b7a-bf1c-ce1410d92021 | -13.30191 | -50.65736 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b80cd552-c28f-3df5-857c-151cbf19d41d | -13.93738 | -48.11384 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7400fc00-bd93-3c64-aae7-66e1f3994e67 | -15.84985 | -54.02195 | 2025-10-01 04:21:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd4c9169-80a5-3af6-97ad-c17c19f4d246 | -11.84081 | -44.96689 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1763a33-324d-3225-88c5-2bced93ed827 | -12.76504 | -46.91522 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62f46940-fc97-383f-bc17-6ad5b390fa24 | -10.97118 | -46.50742 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5026fb73-27b1-3dee-9475-91a1b3fdf8c1 | -17.32323 | -44.44853 | 2025-10-01 04:21:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfe204ac-166a-3855-8137-cd850c7c2c1c | -11.81254 | -44.97342 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4156efd-456a-3f81-98c9-d6d0100cc72d | -13.33159 | -47.81788 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79b9dc6f-9f6c-337c-8e33-383f27a0d543 | -15.1689 | -49.08885 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a56c526-67f9-31fc-8795-0bf796410276 | -9.4018 | -54.70716 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e04e1d2-d8da-3f26-ac7f-ea8eb6bdbc64 | -12.01579 | -46.61721 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2d2a368-81ee-38bf-874d-b5fd1d43aeb9 | -15.31577 | -46.40303 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a67f48f-6a8a-3f3c-bd1f-1f3559304d57 | -10.96055 | -44.32075 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc0e380c-254d-334c-ac2f-ecaa0584e958 | -11.81811 | -44.98158 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96f7e111-e84a-3173-83ef-cf66aca1a715 | -15.61775 | -46.91236 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cece065-33f4-341d-9df3-9b7568cbe5df | -14.68334 | -48.23978 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e2a8971-fefd-337a-9ad4-1684711e5508 | -13.33011 | -47.84819 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3bbcff15-90e5-3f97-b6e1-71485377f715 | -13.29523 | -46.3837 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1efff9b7-f3cf-3fde-bd72-8b99a8bb308b | -12.76461 | -46.87504 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a2fc439-e56d-359f-b987-4b77fe2ac891 | -12.03687 | -47.90814 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30205743-df18-312a-8f43-a4219910423c | -14.02284 | -46.31851 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4269805d-457d-3945-9293-bfe5c143a7e9 | -11.63248 | -47.91081 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8583e4f3-330a-3ec9-b0ac-bbc49e8d441c | -16.02831 | -50.90182 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b5e460e4-3818-3f49-852c-47083a384957 | -13.81875 | -47.50088 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76eeab19-cb31-3f6f-9d22-531704a75028 | -13.97756 | -45.0597 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2646a54b-9466-38f6-90b4-650a63f83c0c | -13.66721 | -48.04209 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cacb0e9d-3bd6-3c75-b069-e2e77b7ecedd | -10.84792 | -45.40898 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f945b67-f6e9-3d35-a880-42f37e3db53f | -15.44256 | -43.64219 | 2025-10-01 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c62153a7-95e6-33fd-b7bc-a812c4ed0195 | -15.41823 | -47.05463 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 313fbd0a-8f0b-3a4d-97b9-398efebaca87 | -16.76675 | -51.33851 | 2025-10-01 04:21:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 86b11db4-01f1-3568-b4ba-e1e8fe01d6d8 | -13.07541 | -47.08333 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 816b0939-fb8b-3987-a281-f7a4690c34e4 | -17.63639 | -46.14093 | 2025-10-01 04:21:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81221a07-2255-3810-964f-0f56c3d40f51 | -12.76018 | -46.88161 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a800497-4113-3ee5-bd62-758f628e0c27 | -13.73062 | -48.68641 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1daa3cc9-ecb8-3d93-a516-66ce81527701 | -14.77968 | -45.79947 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55f47595-b8ba-3171-ac84-acead9f975ca | -11.37971 | -45.06931 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 882fbdd0-7a86-36e9-94f6-2e7af78d49a9 | -11.76783 | -46.87088 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05c32e18-edbe-337f-8ed3-51ea326aae76 | -12.78743 | -46.88238 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e0ef919-dd2f-3563-aacd-59dce072b763 | -12.86601 | -46.98651 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efb55d87-7bb3-3799-8de8-05b9979198fd | -12.86714 | -46.97938 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39a44937-658e-3863-912f-38c9e4d46a93 | -13.66661 | -48.0458 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4cb1fbb-d93e-3578-b4d2-faddb621e4ad | -13.32917 | -47.83276 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afda5ad9-f1d3-384f-b698-3b7e45671847 | -9.431 | -54.57857 | 2025-10-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e8bbbf78-c3a3-357d-b6cb-0f7304e7d1f0 | -10.57448 | -57.81219 | 2025-10-01 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 046c1866-34e5-35b2-9d44-ddfdb75c9e88 | -13.52936 | -44.85068 | 2025-10-01 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89c70115-335a-3a5a-b421-c780396a66c3 | -13.67203 | -48.08463 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a1c8e5e6-a3fe-36c7-8ad5-8dd064808c19 | -11.38871 | -44.89956 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b13e73b1-2b53-3899-858d-de79fadc7227 | -11.09342 | -47.72205 | 2025-10-01 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f14dfc67-30d7-3492-ae04-8e282081fc48 | -13.30489 | -50.66287 | 2025-10-01 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2499d53-1ad3-3cd3-97d9-7a84affe01e0 | -14.95888 | -46.8834 | 2025-10-01 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 670855b1-49ee-3292-8d98-a333b8bf5da4 | -15.26718 | -51.47673 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23823005-ba9d-3491-9739-50f3719c1dd0 | -13.56351 | -48.20852 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6df10665-83e3-38f2-b80b-6217c820173f | -15.93646 | -46.23633 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6361cd6e-472c-3564-b9e2-e05e2cf0b888 | -10.66753 | -48.53174 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 513f806d-0e3b-3de0-a477-0e7377c4b4ad | -10.62767 | -48.5966 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24aecf8d-a14b-3847-8350-b4eb52ae47cf | -15.85526 | -46.23444 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7fac361-e133-307e-b5c3-beb47d4a01f2 | -14.022 | -44.80907 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14c3a621-5f51-3f85-8ff4-8f8c3912c5ca | -9.44848 | -50.89602 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8b983612-a931-3c4c-a9b9-8eb88a9265a1 | -14.90165 | -48.13202 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb45221c-8d65-363d-99d1-c28a3c669cf4 | -16.0204 | -50.88097 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 469114b0-dbe6-36bf-a49a-f6e59de8fb45 | -15.32833 | -47.36518 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 237c0e2c-702f-39a5-aeef-23202a011aa6 | -17.39268 | -47.1328 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91df3644-5b87-338b-b581-9000e36cc6d8 | -16.19449 | -50.0078 | 2025-10-01 04:21:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e50c828-5deb-34cd-8327-a83beadf2946 | -15.47634 | -45.88854 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db3442c5-0900-3bd7-aba8-b6c11eb930b8 | -14.78797 | -45.76755 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38a91a72-e394-3680-a943-83f428b3a16b | -10.63256 | -48.589 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4568da5f-d804-3ac1-ba2a-5264eb974aef | -12.85841 | -46.94868 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6b1e621b-023e-324f-abae-84867030c019 | -10.1992 | -44.89658 | 2025-10-01 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad438bc7-f88d-3466-989a-0dc2a3e5a5e4 | -13.35962 | -48.10126 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fac0ccfe-7a47-31e5-ab36-5df075b044c5 | -11.83966 | -48.06167 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |


[Clique aqui para ver as próximas entradas](README46.md)
