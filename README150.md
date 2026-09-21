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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7325806b-2c96-3791-9a91-665e8848b02a | -13.90219 | -45.491 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3c6b07bd-e56e-32d9-95dd-ff5655a80d34 | -10.96274 | -50.58614 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2fc99c0e-b1a4-30c2-a0d2-6491735665a8 | -11.66998 | -43.4526 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 6c0548ca-5dd4-3ba6-99fa-d2ef2d3456c7 | -10.71647 | -50.76707 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 89843124-6268-3429-8353-3b76a3cd1f68 | -11.8322 | -46.81879 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4048a64c-fe67-3226-85cb-38b72ee05615 | -11.14853 | -42.82544 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 7b0fbe15-2fb8-392c-bbee-6e231d489fab | -12.0295 | -50.04139 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 58ee227d-ca6d-367a-bfde-da6844928466 | -13.9015 | -48.57144 | 2026-09-21 16:01:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c89a0f04-f711-33c6-890e-8bad22be2dff | -9.53487 | -47.95533 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| e854715d-cd4d-3f2a-a3a3-534cb44e56e2 | -13.75591 | -43.48359 | 2026-09-21 16:01:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b011b618-1c61-3d5d-96cd-a0c24a60fa3a | -9.01442 | -44.99736 | 2026-09-21 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ae1ab7d9-105a-3e8f-99a4-aa8e0dce9d6f | -11.55474 | -41.78528 | 2026-09-21 16:01:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9548071e-771a-3c5d-a35f-3a350c0d6689 | -12.39837 | -47.00351 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 53f2640e-b390-3d28-86b4-db1e52cc2fd3 | -13.55058 | -44.88752 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a6219154-b496-33db-9b35-364e41237980 | -13.47822 | -46.93359 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 01c92121-6dae-3a50-b059-8ff3a61bdbc4 | -11.41082 | -47.33974 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9915b279-0979-3140-bdae-8343082683c9 | -11.83221 | -38.2662 | 2026-09-21 16:01:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 797d84af-d7d2-34e1-b9cf-c8bee503bf89 | -12.79957 | -44.22554 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fbf9bd50-bc18-366f-be90-ff74c35efcf7 | -8.68129 | -45.32385 | 2026-09-21 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f9496bcd-828e-309c-85b3-aa5376f3f919 | -10.11457 | -48.43367 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 3b5eee3b-3ddf-384c-bf08-faa9312641ef | -11.81937 | -50.03632 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 5c940788-76ff-3c24-8c05-0de718c092a2 | -10.14652 | -45.56055 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 61f40184-a5b8-3b74-aaad-f797178dc9d5 | -9.39196 | -48.28899 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6bdb38da-8f6d-336f-bd10-cbb11cb1958f | -12.43488 | -47.06499 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 13b36b3f-de40-32b9-b6d6-0fcb776e084d | -11.05004 | -46.57569 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 4d97e449-6873-3314-84ee-9c0199c538fd | -9.82281 | -48.44029 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| f3771536-1a86-3683-ac33-1da51726d5c5 | -11.67707 | -43.44762 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 00b01876-3af9-3749-8c14-557257672b03 | -12.3142 | -49.18659 | 2026-09-21 16:01:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a5e64b8-7bde-3584-a9a3-f127b1d4abba | -9.6193 | -43.92791 | 2026-09-21 16:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 558d07f8-09b6-37df-bdbb-5c07fdd7a05a | -10.72672 | -50.7939 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1b981d01-eb8f-3de5-8eef-42c9eca81d9e | -11.44447 | -45.37489 | 2026-09-21 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 87eabc81-2c5e-3962-a604-18fbf9b91520 | -11.95172 | -46.50808 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 857a03e8-45a0-3fa5-b6b0-929a1b61dae4 | -10.86258 | -48.07218 | 2026-09-21 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7ae76a59-d4d5-3a85-8f94-7d27fb0f5ce1 | -13.9059 | -45.47703 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c90d4cb1-e51c-3907-bded-2df611e87e08 | -12.8228 | -44.21731 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 488421c0-a54b-311f-8907-e4d10d1d5fd3 | -11.47347 | -47.67118 | 2026-09-21 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ab04dc45-8c12-309c-b23f-76bc39dd6caa | -9.36978 | -47.77243 | 2026-09-21 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 223669e1-743a-3fe1-a2a8-eb6432705119 | -11.94023 | -46.5055 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ab6d7c22-8777-3eac-ba2b-24cff6c616bf | -13.89045 | -45.48233 | 2026-09-21 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4064b411-ad94-3797-88c7-22af4c515b34 | -12.44191 | -47.06269 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 81129d5a-e6ea-3229-946c-cf02b54c8040 | -10.11513 | -48.43827 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 7be1ac80-4bc9-30c3-9b4d-d32d6b2ddb11 | -9.75356 | -46.05664 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 330e08e4-edc4-3456-b998-7852b1d87a24 | -11.94542 | -46.50628 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8b0de31e-c5e7-3ddc-9415-1c1e5dc73185 | -9.40528 | -48.3223 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0aae6d09-2f3f-3f49-9e45-4aafbb4ec9b2 | -9.83861 | -48.31616 | 2026-09-21 16:01:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0fde7e3d-6726-33aa-9f9f-a10bbb83546f | -11.82555 | -50.02928 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 5c9c2d2c-b88d-328f-88ea-b6d31d94a3e0 | -14.8724 | -49.21556 | 2026-09-21 16:01:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 4190da06-8769-3f44-aa09-50235a94d82f | -7.5162 | -37.88544 | 2026-09-21 16:01:00 | NOAA-21 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 418c0297-7a82-3615-8972-a1350a35a47b | -11.84677 | -46.84472 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bfbf4fa7-6c3c-3398-a29a-a448b86fbd2b | -12.30543 | -50.66525 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 68f7621a-069f-3908-98a4-eb9008abffc3 | -8.76862 | -45.87315 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e41bdd2f-0efb-3626-9e7f-03e49bf734ec | -12.8098 | -44.22963 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5502f181-cdc0-3862-a3b9-a686c5482d8e | -10.72752 | -50.8008 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c13d43b7-72a4-378e-9bd6-081bc6b6bebf | -11.80962 | -49.83882 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 21354a76-3fbf-3218-b191-7d2fe4cee8ce | -8.76226 | -45.86432 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a177008b-4dfa-385c-9441-a31d7eeefc83 | -10.72974 | -50.77648 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 7d66c614-d430-3041-8e6e-ceedacfc5ff9 | -10.86474 | -48.06767 | 2026-09-21 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 32cadf4a-c180-3e1a-8661-36681bb6db83 | -10.48395 | -43.58025 | 2026-09-21 16:01:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a7144cf8-85bc-3a4f-95eb-956080a1740d | -10.98411 | -50.59663 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9144fdce-3516-3f2d-9ac6-0418d7c939b3 | -12.38455 | -47.03391 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 178d6814-4c8b-3b96-aa91-99d11c851c41 | -10.98097 | -48.2178 | 2026-09-21 16:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2907a0a-20a3-3687-a618-8a0dcfefee89 | -8.23081 | -35.22062 | 2026-09-21 16:01:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f998c3da-8d23-3c5a-90b9-a4475bf3630c | -9.27999 | -46.19597 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92170b01-18c0-3cf0-9ebb-6d7ca8398541 | -12.45056 | -40.27626 | 2026-09-21 16:01:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5164b961-14b7-326b-a41f-0404b891bf26 | -12.59475 | -39.57381 | 2026-09-21 16:01:00 | NOAA-21 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d61bed8b-209e-33d5-9e7b-e09945d13135 | -7.57023 | -34.92252 | 2026-09-21 16:01:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4e072672-8561-3d96-8ecb-02135944bcd3 | -13.63543 | -46.91926 | 2026-09-21 16:01:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ae66a36c-7ead-3d87-82de-ff195926b321 | -10.12444 | -45.5481 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee16403a-fcce-3bb0-8b36-9f686decc7ad | -11.66814 | -43.44878 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 2130186a-cf19-3e41-9c42-cf2aa5abf251 | -10.87002 | -50.15523 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7c597e86-5f9c-3080-bd1d-0dd7e3a74f26 | -7.63635 | -37.67221 | 2026-09-21 16:01:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c211aeb0-4b18-35d0-b7a9-a9c66541fd9d | -12.40365 | -47.0477 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d82208ca-d254-32a8-99ef-712c3284cc2c | -12.26587 | -50.1505 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0e99f275-bb12-3090-b90a-7d7468cc4b04 | -9.95044 | -45.46582 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 684b670c-aade-39db-999e-2e4fc39904b8 | -14.007 | -42.14009 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 40.2 |
| a4867b18-b53d-3b02-92a3-f78aa2a063b1 | -9.75504 | -46.0552 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 731eaee6-e192-3e0e-aa22-284721e99eee | -8.75778 | -44.28091 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 43fb39d1-ee60-385b-8c49-cc2b6226cb73 | -10.27655 | -50.23508 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a312d4ad-0664-37ad-a2fa-ba58534618c8 | -10.09048 | -45.83873 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c7a848f-d61c-3e7c-a9dd-0602e3441e4b | -9.24461 | -46.25042 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3d675885-fe63-3f3e-86e3-e04eb64ffbe9 | -9.39463 | -48.28704 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c33ffd1-4e93-3e86-9ef5-56cccd0edb24 | -11.93212 | -46.48928 | 2026-09-21 16:01:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34ca3df1-6e51-3ed8-9ef0-1c4abe133fa2 | -11.81801 | -50.02364 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bafd74bb-6f55-3276-9843-8499f2c7edf1 | -11.3989 | -44.08251 | 2026-09-21 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bc0a737e-ca90-38eb-922a-db8377357cba | -9.53652 | -45.39082 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| def2eecf-844f-3204-bf0f-c45568a9904d | -9.15622 | -50.00507 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b5313b17-ae76-3ec1-a101-e751a17f65a4 | -10.9475 | -50.58674 | 2026-09-21 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ddb9717f-c991-333e-8b3e-282b813c1a06 | -10.68082 | -46.71894 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e617731a-73ed-3ed5-8244-f770733aa59b | -10.99657 | -48.24412 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5607ed2d-8190-3e9d-8a0d-42f2cbfb0285 | -10.07854 | -50.24425 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2ef58178-e745-3c22-9d67-458a34d0ec38 | -11.6726 | -43.4482 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b9c0205c-6486-3a3a-9329-0fd18130ac6c | -9.89799 | -48.44961 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e83d2776-5f5b-346b-b881-1c4687c26974 | -9.58508 | -45.48198 | 2026-09-21 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ce8f7411-16d0-3987-a5ef-d25ae7643d6f | -10.996 | -48.23952 | 2026-09-21 16:01:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d5850a0-49ad-30b6-883b-c7602e9be523 | -12.44014 | -47.06026 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 42c1abf0-5173-3a62-9b5a-9a34db4586af | -14.09916 | -44.83916 | 2026-09-21 16:01:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| be17e6cd-2c8c-33a8-b14e-641c7e0ddc11 | -9.16799 | -50.00613 | 2026-09-21 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| cc221a2f-b0d4-34dd-8282-6bea5c20b163 | -9.87978 | -48.45215 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1e99c1ce-2adb-3a46-8be3-6f1680fbe521 | -11.68311 | -43.42408 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 6908e399-7e08-34da-94d3-db9555f94e88 | -10.46477 | -45.10683 | 2026-09-21 16:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README151.md)
