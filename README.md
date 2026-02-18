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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aa61527-5691-32ab-ae4c-c841e97b0372 | 2.6906 | -60.2021 | 2026-02-18 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8f2ff598-10cb-37ff-8328-cd41856b3974 | 2.6905 | -60.2211 | 2026-02-18 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5e75f7fe-0f1f-383b-9330-c2020593d8d9 | 2.6723 | -60.2214 | 2026-02-18 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.1 |
| c1dba85b-fa6b-3b79-98e6-293ff9251e7a | 1.2852 | -60.4075 | 2026-02-18 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 671a81eb-b124-3c7e-993d-de4e6d3c7c6d | 1.267 | -60.4076 | 2026-02-18 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b2c138c3-399a-398d-b889-7cbe91fbf60a | 2.6724 | -60.1453 | 2026-02-18 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d194b88e-bf1d-3db9-b993-0277c1131b21 | 2.6723 | -60.2023 | 2026-02-18 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e1722d6e-a75f-3627-bed7-d99b4af3c7a8 | 2.6724 | -60.1643 | 2026-02-18 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1d859fa1-87e6-3eb3-adef-07002c58f78a | 2.6905 | -60.2211 | 2026-02-18 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 4fafd89b-7618-3cf6-b07b-564cc67256a8 | 2.6724 | -60.1453 | 2026-02-18 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 5fd15a69-f48e-3419-a11f-eb471ac554ea | 2.6906 | -60.2021 | 2026-02-18 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| fdbd7a73-7ca1-33cb-b581-55f62164d03b | 2.6724 | -60.1643 | 2026-02-18 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 26899a3f-34ec-3c6c-8010-748854b96975 | 2.6723 | -60.2214 | 2026-02-18 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 3351dea4-23b5-3eab-8d14-3f456db71665 | -18.813299 | -51.587101 | 2026-02-18 00:11:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 85a9e5c2-1a5d-348f-8927-96ac99890217 | -12.4832 | -43.628899 | 2026-02-18 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2508b3d4-0502-3170-995a-73c88a6cc034 | -11.1942 | -43.557701 | 2026-02-18 00:11:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 641b47a5-16ce-386f-904b-85eda1e60897 | -13.0172 | -45.035599 | 2026-02-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e09ce407-d672-31ef-a28b-78c33844c74c | -11.8954 | -45.274101 | 2026-02-18 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 908f5a96-09db-3967-bd20-85ead6a0b303 | -12.8207 | -44.817299 | 2026-02-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 952c0bc5-4302-3c05-8890-0662fa42115f | -12.4955 | -43.636799 | 2026-02-18 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83364d71-9347-3057-847e-db4bea638d06 | -12.4857 | -43.639198 | 2026-02-18 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52eb0e11-42b6-3fb1-995a-388e253725c1 | -21.028999 | -43.296299 | 2026-02-18 00:11:00 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c7c80ad-6390-37cf-8d2c-438da218c1fb | -21.026899 | -43.287601 | 2026-02-18 00:11:00 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85d08680-fb5b-3a8b-b2f8-61119aceded7 | -11.8933 | -45.265499 | 2026-02-18 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f252ee0a-f8f3-3ae2-a734-735fba06d02d | -11.8835 | -45.267799 | 2026-02-18 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3bf2b072-f1d4-34e1-ac6d-9edfcb0ce766 | -11.8856 | -45.276402 | 2026-02-18 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89edf970-3eeb-35d1-ab8b-4c8327ef2715 | -18.8055 | -51.599201 | 2026-02-18 00:11:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f665629a-66ea-3406-a6c1-a8c88a9b9695 | -12.9912 | -41.175098 | 2026-02-18 00:11:00 | METOP-B | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dca0867f-1877-3296-8369-c549d3b307e5 | -14.4183 | -44.577999 | 2026-02-18 00:11:00 | METOP-B | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f2af5b26-e86d-37c9-9f03-9e64c967aa7d | -18.8153 | -51.597198 | 2026-02-18 00:11:00 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9300fde9-142b-3cff-a4e2-15ad9201b530 | -18.803499 | -51.5891 | 2026-02-18 00:11:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fdbaae0d-b3a3-3220-8800-530dc7d2e6d2 | -12.4287 | -47.166901 | 2026-02-18 00:11:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b2547f3-b9c2-37a9-b281-e6d175b5ae96 | -12.493 | -43.6264 | 2026-02-18 00:11:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 745a33f2-ced1-3bec-a84f-642a754b1c98 | -21.7717 | -42.889599 | 2026-02-18 00:11:00 | METOP-B | SENADOR CORTES | MINAS GERAIS | Brasil | 3165602 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6dfd83ad-c7ce-3ab3-a5c9-a39a38218a17 | -13.0193 | -45.044201 | 2026-02-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 225d9dc3-48dc-366c-82d4-5a12c40c1402 | -15.8515 | -52.894199 | 2026-02-18 00:11:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea061448-ecad-3aa2-b4fe-c03ad939ecf9 | -11.8974 | -45.2826 | 2026-02-18 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 939ab96a-a860-3b47-9abc-8dd044de3662 | 2.6724 | -60.1643 | 2026-02-18 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f0eaecb4-5ad0-3759-94c9-f5ee7e94703f | 2.6905 | -60.2211 | 2026-02-18 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f8866438-17f1-34f0-a6dd-565c0a32d0ab | 2.6724 | -60.1453 | 2026-02-18 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d071e71f-b8f8-3ae2-b844-02b49cf9a4ac | 2.6723 | -60.2214 | 2026-02-18 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.8 |
| e4450e10-9f04-35ab-aec5-88b6883a7874 | 2.6724 | -60.1453 | 2026-02-18 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0b51aec9-3c6a-303d-aebd-7e56027bb48b | -21.0304 | -43.2909 | 2026-02-18 00:30:00 | GOES-19 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.7 |
| c8173d91-624c-3d7a-8257-013274e13872 | 2.6723 | -60.2214 | 2026-02-18 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 841b41dd-53c2-3bc0-a997-247c96481594 | 2.6724 | -60.1643 | 2026-02-18 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7b83ae58-7d9a-3be7-bf55-44f67e0733dc | 2.6906 | -60.2021 | 2026-02-18 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e7f186be-6ad8-325b-95ab-770ce401aa73 | 2.6905 | -60.2211 | 2026-02-18 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 70dceecc-382d-3632-b2a4-448ab663d47e | 2.6724 | -60.1643 | 2026-02-18 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 03c8f086-baa6-381f-9b0f-0712c1cd2c16 | 2.6724 | -60.1453 | 2026-02-18 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f3182db2-3917-3cca-9634-aec8ebab11a3 | 2.6906 | -60.2021 | 2026-02-18 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| eedaddb4-8e3c-30ff-92dd-e1e0319aaccc | 2.6905 | -60.2211 | 2026-02-18 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 51e42eb6-bf56-3039-bcd9-140e2a0dcf15 | -13.0238 | -45.046799 | 2026-02-18 00:47:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4130b5de-8ef6-3499-b176-e847149c3373 | -20.3018 | -49.576599 | 2026-02-18 00:47:00 | METOP-C | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db3d700e-4983-321a-a765-c383c8685195 | -18.807899 | -51.612701 | 2026-02-18 00:47:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d315759c-7d0b-34dc-9039-8c2af94d9283 | -14.5113 | -43.611301 | 2026-02-18 00:47:00 | METOP-C | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2377c53a-4d5c-3e38-a395-a8b3658e12a1 | -18.8043 | -51.595001 | 2026-02-18 00:47:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7eaa7823-cdb0-3763-b651-d90bcb64c7a0 | -21.0373 | -43.2943 | 2026-02-18 00:47:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e748b664-4d54-390d-be7b-c7fc96faba2f | -12.4922 | -43.648399 | 2026-02-18 00:47:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89ade280-56b6-31a7-9944-af7b0d5aef0b | -18.806101 | -51.603901 | 2026-02-18 00:47:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5b65782f-6b4b-3340-9a7f-db34ee1215f9 | -15.8544 | -52.9076 | 2026-02-18 00:47:00 | METOP-C | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1acc38f5-b501-3a9f-a95b-69e671d5d301 | -13.0214 | -45.036999 | 2026-02-18 00:47:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae63d357-6f7a-3bc4-a4a1-6de9e2468bcf | -21.027599 | -43.2971 | 2026-02-18 00:47:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8f1a14c-9543-364a-9af4-7c46824f70ef | -12.4891 | -43.6362 | 2026-02-18 00:47:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 145ba00b-6a43-3b1a-b95e-e558c6cdbbcd | -12.427 | -47.171501 | 2026-02-18 00:47:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60b5e080-9bd7-3717-8862-414c7eb1462c | -21.034901 | -43.2845 | 2026-02-18 00:47:00 | METOP-C | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73800001-d359-35fa-b72f-7a9b69e59fca | -13.0141 | -45.049301 | 2026-02-18 00:47:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9bc636b2-3660-3f79-930f-c405f4fb3cb1 | -18.815901 | -51.601799 | 2026-02-18 00:47:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eb2e6c9b-4417-3d96-9439-57d5549ff6b8 | 2.6724 | -60.1453 | 2026-02-18 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0a68569a-407a-3523-843b-889818593e60 | 2.6724 | -60.1643 | 2026-02-18 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 10d582a0-c4ee-38b3-b098-d85eead3bdf3 | 2.6723 | -60.2214 | 2026-02-18 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 15c7214c-0df4-31fe-9a2d-6093b9543b66 | 2.6906 | -60.2021 | 2026-02-18 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 93d9c3ab-56e7-3495-aa66-44ab90e40fa1 | 2.6905 | -60.2211 | 2026-02-18 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 53414cee-a431-3aec-aa43-5ccbcbbd259b | 1.267 | -60.4076 | 2026-02-18 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fcf19aab-2449-360c-b04b-405c028b17cb | 2.6723 | -60.2214 | 2026-02-18 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 5b0f345b-71de-3be4-b42c-9b504a8d7156 | 2.6724 | -60.1453 | 2026-02-18 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0565ac7f-32d4-3c84-8c20-4b260ea3c371 | 2.6724 | -60.1643 | 2026-02-18 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 75956311-71ad-35ce-ae7e-8dafbf38fd18 | 2.6723 | -60.2023 | 2026-02-18 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 092fb45f-6489-3650-927b-f027a9aedfb8 | 2.9266 | -60.8437 | 2026-02-18 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 76e4f16c-93bb-340c-8c6f-de8ea1839858 | 1.267 | -60.4076 | 2026-02-18 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 8ec2ee32-7162-3005-9dd5-4a5e61a37901 | 2.6905 | -60.2211 | 2026-02-18 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ff426556-e357-36be-b024-3cb1b8b24ba6 | -18.80302 | -51.61095 | 2026-02-18 01:04:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b955c93d-793d-35bf-bb3d-67015ea6668d | -18.81545 | -51.60876 | 2026-02-18 01:04:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| bf4aaaf5-2066-38ae-a4cd-13cd6fd3a40f | -18.81047 | -51.59481 | 2026-02-18 01:04:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 43e14444-dd63-3c80-b41a-504a3b899da2 | -18.81382 | -51.6145 | 2026-02-18 01:04:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| cf8aa97e-a4ac-35a3-b330-187e87bd6cc9 | -12.2073 | -57.78654 | 2026-02-18 01:04:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3d03443-5ab7-33dc-b6a4-31b3cbc9bc72 | -12.20869 | -57.79625 | 2026-02-18 01:04:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cc7011eb-b5bf-3ced-b44b-c9681dc61f64 | 2.67258 | -60.13983 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8cfa42be-d49b-38a2-b497-9c737a7a3aeb | 4.05702 | -61.1434 | 2026-02-18 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0b1424c6-d5da-34c0-8527-adc2a7758530 | 1.36915 | -60.0638 | 2026-02-18 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9dff2d3a-b717-363c-adbb-1304f90cb864 | 2.68069 | -60.15142 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 76ee32b2-8518-3bd9-a23c-5a2911b87149 | 3.99458 | -59.80874 | 2026-02-18 01:09:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3423b742-d8c2-3c0e-b85e-3747a43c0c04 | 2.91221 | -60.82709 | 2026-02-18 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d3b2c376-bbbd-326b-b823-4a8b37c6ef81 | 4.08484 | -60.65991 | 2026-02-18 01:09:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b208a910-22f3-31aa-9ce4-a34dae98938c | 1.80983 | -60.46329 | 2026-02-18 01:09:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d26774b4-ddcc-3a65-93f4-eae77033066e | 2.93057 | -60.82975 | 2026-02-18 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0a3bd16c-193b-3b9a-b0e7-e91966440af8 | 2.92925 | -60.83924 | 2026-02-18 01:09:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| fc293598-dc39-38cd-aa80-b104ef0b5c40 | 1.27377 | -60.41121 | 2026-02-18 01:09:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.9 |
| bf06538f-88fd-3de4-877b-a909a1d39c58 | 4.01499 | -60.31594 | 2026-02-18 01:09:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a9928e91-4ded-3e28-a12f-c44889f88038 | 2.68325 | -60.20386 | 2026-02-18 01:09:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a883f48c-86ad-3bac-a911-c20329c14434 | 0.82341 | -60.33789 | 2026-02-18 01:09:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README2.md)
