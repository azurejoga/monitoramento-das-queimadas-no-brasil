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
| 478c6b92-aa27-32c6-8123-27a44190182c | -11.7528 | -43.646 | 2026-04-24 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c67e29ac-3acd-396c-9687-c4f2b2d9053c | -11.772 | -43.643 | 2026-04-24 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3fca627b-8144-3478-acfe-c87a8abf6edf | -11.7528 | -43.646 | 2026-04-24 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 66d1a448-4786-3303-b309-3e5cc475204b | -11.772 | -43.643 | 2026-04-24 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 917bf4cd-b390-3077-9203-897b2c63016a | -16.41984 | -54.9183 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4d38a7a7-2287-301f-8f38-6f7bede6967b | -17.2589 | -51.88436 | 2026-04-24 00:54:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 919fdf61-6aac-353c-8bd4-442a31d5acee | -19.45048 | -56.61517 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 04f21cf1-9156-3a12-805f-75da0698a017 | -18.26875 | -52.90224 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 88407fa6-f9bf-38ce-a185-cfddda50e0b9 | -18.27711 | -52.88654 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| ee14f5e6-52a6-392f-a81c-8a673bb5144b | -20.71989 | -55.17279 | 2026-04-24 00:54:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c9cd413e-449a-34d0-9fa8-60b7cf681a9d | -16.42145 | -54.92903 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 333b98bf-5ce9-3686-a06f-aaefa0235325 | -18.26875 | -52.90225 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ae5ed57d-9ac0-3c1e-a6b3-a380f9ec1c10 | -16.42942 | -54.91675 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5549a23b-8597-3ac6-a7a2-3870779cae24 | -16.42942 | -54.91676 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5d656395-45e0-36c7-b1e9-2ca703ce4801 | -18.27484 | -52.87264 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b809f26b-574f-3a80-9489-b72d9b97db0d | -19.43642 | -56.57923 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d6e27762-4372-32bb-8bb9-97f60a3b86cb | -18.28384 | -52.92792 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c3ad83a2-4c38-326e-ac5f-7821cc133b90 | -20.71989 | -55.17281 | 2026-04-24 00:54:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47729597-4cc1-305a-93b0-7f4e8bf37a64 | -16.41983 | -54.91831 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7645f6f5-7ff6-3cc0-8669-a7e329eba386 | -18.2771 | -52.88656 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 261e0e89-a9b6-3db2-afeb-ff2f5cafd9d8 | -16.43104 | -54.92754 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a77fce1-42ca-3ede-9fe6-e10093b3b745 | -18.30105 | -52.96697 | 2026-04-24 00:54:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2bf6a5ae-6899-3863-94ed-364249dfdc32 | -19.0965 | -56.06487 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 466f2a56-e4b7-3ac7-865a-ad454a44d5de | -18.28384 | -52.92791 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 734481a6-64db-3724-8597-740e28a58121 | -18.26647 | -52.88836 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 59d06d38-b781-34b0-a679-0f30b05f69eb | -19.0965 | -56.06485 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| bf146a52-7e5f-3fc7-92fb-13b4ab98e5a2 | -19.45048 | -56.61519 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 4492ed16-9908-3302-b46c-aa71f961f9bc | -19.45178 | -56.62453 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 50a7f748-8702-3365-806d-6e6aff4e862f | -19.43642 | -56.57922 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 988bf361-3619-340b-bbb8-2d6909e2070a | -18.30105 | -52.96695 | 2026-04-24 00:54:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d50b0202-996f-3b2c-9b91-70c3a8aa59b3 | -16.42145 | -54.92904 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d4c0bff-5713-3b56-8a14-d882cbfbca38 | -18.27484 | -52.87266 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 30b0ef30-b407-373a-88ba-874a5f8df3c8 | -19.44164 | -56.6166 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| eaeae2b7-6cb2-3edc-af94-6dce791e61f0 | -19.44164 | -56.61658 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 2e96f267-2dd9-3da2-9390-c6e9ce45759e | -17.2589 | -51.88437 | 2026-04-24 00:54:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ab641387-f492-3f99-a99e-ab3b4cebd2d6 | -18.26647 | -52.88834 | 2026-04-24 00:54:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| db1ae028-6648-3c26-a3fb-f12f0f8c37c4 | -16.43103 | -54.92755 | 2026-04-24 00:54:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5301b69c-3800-392e-a38d-05ea6f8bcb1a | -19.45178 | -56.62451 | 2026-04-24 00:54:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| d83a11c2-a00d-3c9f-8eef-d1ec0dd07daf | -11.94354 | -58.08353 | 2026-04-24 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ddd76aa1-27fc-33f9-9d63-a46766bc1ba5 | -12.09477 | -51.23061 | 2026-04-24 00:54:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 94b62ad4-44fd-395a-a8aa-4ca1e988031d | -14.20983 | -57.42514 | 2026-04-24 00:54:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a5488b44-990c-3e8f-9174-554f5b1acdd1 | -12.9904 | -54.68486 | 2026-04-24 00:54:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ce99149e-043a-38de-9d0a-5fc2c7085a7d | -13.71204 | -57.48419 | 2026-04-24 00:54:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 09465e42-3c4a-3571-b6eb-3acfaae2fb47 | -14.20984 | -57.42513 | 2026-04-24 00:54:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 048d2993-6109-39e2-9e53-37b7b76b1b0b | -11.94354 | -58.08352 | 2026-04-24 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e83bc8c8-1aa3-31cf-8731-4df87a8c79a7 | -13.71204 | -57.48418 | 2026-04-24 00:54:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 10b2912d-d536-329f-8c55-6dfdd094f5a1 | -12.9904 | -54.68484 | 2026-04-24 00:54:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 26cb1785-3c45-3f11-870d-754e712c8e84 | -12.09477 | -51.23059 | 2026-04-24 00:54:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6da36146-c689-3f8e-9e03-f94e8bf8a685 | -23.663099 | -51.587898 | 2026-04-24 01:13:00 | METOP-B | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ffda798d-78ca-3550-83ff-ab3970693a8d | -19.447399 | -56.609001 | 2026-04-24 01:13:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7359bb44-78c4-3f53-b5a0-b59fdc5958e8 | -23.6686 | -51.607498 | 2026-04-24 01:13:00 | METOP-B | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc582da1-faab-369b-9f2e-f1ee3734680c | -16.417 | -54.905499 | 2026-04-24 01:13:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 066277b0-ef93-316a-87d5-a354efd16c47 | -11.772 | -43.643 | 2026-04-24 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e98ec863-f625-37da-8e49-0f1f21181aa8 | -19.4534 | -56.612099 | 2026-04-24 01:45:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f258f059-36cc-3464-b465-e2d16d55f24f | -16.4282 | -54.914799 | 2026-04-24 01:45:00 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 641a0ca6-11a1-3e18-912e-8aa31192f52b | -11.7528 | -43.646 | 2026-04-24 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| aa29c422-f833-332c-9eb5-29cc5553d77d | -11.772 | -43.643 | 2026-04-24 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 313f6482-3d64-3f22-a8f2-6bbca7e73fd5 | -11.15913 | -43.50923 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bff1208d-998c-32de-91be-0c60b41d2f24 | -11.76368 | -43.63877 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cd72c68-fa26-364c-a391-265f9406da99 | -11.7585 | -43.63784 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44fcbebf-86b8-3636-8da5-fe646d73f45b | -9.23536 | -46.65269 | 2026-04-24 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4378aafe-0b06-31bf-bf86-37db8a2f4ee2 | -11.9552 | -43.3806 | 2026-04-24 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12f35ab9-724d-3b2c-b1cf-fe624ca9e6c4 | -11.16104 | -43.50396 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85bad20c-1901-33c3-83ec-8eedb5829a8a | -11.7625 | -43.64509 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9de33c9-895b-3cf3-81a0-2fc4f8de538a | -11.75732 | -43.64414 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d53304f9-f03e-3714-9fc4-ca35812b06b3 | -11.95013 | -43.37962 | 2026-04-24 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0727ec19-1380-3d0a-8fdf-3530b5cfbcee | -11.95172 | -43.38045 | 2026-04-24 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a7758eb-77a0-3b08-994d-dfc058890d3b | -8.78821 | -44.84469 | 2026-04-24 03:38:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59d138a8-e5a6-3413-8809-b27a0823a061 | -11.15972 | -43.50605 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7d208ac-039d-3e1e-b1b8-5ae248cd2bf4 | -11.76309 | -43.64193 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aafbfaa7-215f-398e-9585-2ab8a99c99a4 | -11.75791 | -43.64099 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a94ea75-6e73-37fe-acf0-e568957a9183 | -11.95462 | -43.38363 | 2026-04-24 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ff61aab-76a8-3aa2-9ec8-6396f46e1a30 | -11.15983 | -43.51031 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4c7826f-6135-318b-8d69-858f84a22406 | -11.75331 | -43.63688 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea06d69b-6ebb-3db9-9afe-58bfe6d7e804 | -11.95077 | -43.3763 | 2026-04-24 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fb487ec-3978-379b-839a-f96a23064ea8 | -9.22885 | -46.65139 | 2026-04-24 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae11d232-c440-3f8d-90f8-6ceae054fd6e | -11.95232 | -43.37719 | 2026-04-24 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f642429-e29f-334b-8f84-4d42ea57ced6 | -11.76945 | -43.63658 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff75ebb8-6137-3cdc-83b1-b072250d304b | -11.16043 | -43.50713 | 2026-04-24 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f984974-d7b8-35d9-8707-4676d11918fe | -20.56375 | -41.02073 | 2026-04-24 03:40:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d69c22f9-2db3-3c95-ac04-45606e832d84 | -20.19089 | -46.7287 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46387d41-66ca-321f-a7fc-57a608dc5bd4 | -20.16218 | -46.85904 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17142c2c-5f80-3326-b4a8-b0a2ff625975 | -20.161 | -46.85884 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd1d4df9-5a8c-3b0f-9c70-c88df0460d2b | -20.91668 | -40.8209 | 2026-04-24 03:40:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31813927-7fad-3fb2-b73d-08a6bd8c90b4 | -20.16619 | -46.86114 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8da341f5-9359-321c-acc9-b802bb471718 | -18.86269 | -41.97818 | 2026-04-24 03:40:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 40413549-d111-39bb-872f-0cbb22268c53 | -21.20472 | -44.20743 | 2026-04-24 03:40:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d5bcf86-fdd8-3b70-8199-689a178cfa53 | -16.00651 | -41.67831 | 2026-04-24 03:40:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d137afd-c0f1-3332-8035-c37414e4e7b5 | -19.80206 | -44.63515 | 2026-04-24 03:40:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1f567bb7-9342-379a-9a05-b6125d4dbf70 | -20.18887 | -46.72798 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7f8ce5c-0877-3bf2-a802-8e7e5796c5a3 | -17.52862 | -44.75314 | 2026-04-24 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4144d2da-dca3-364a-8f51-ec080cbdc544 | -20.16139 | -46.86264 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4e87a83-da2e-3672-b443-19378ff84d17 | -15.33244 | -43.8045 | 2026-04-24 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 760f91ad-afd2-3ef4-8600-ceca42bb3690 | -20.15707 | -46.85645 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4435cda9-488c-3fed-ab3e-8e0402203dfc | -20.20856 | -46.80279 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64a8aae0-f902-32d1-9408-dad445385193 | -20.20777 | -46.80645 | 2026-04-24 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17584584-c7f2-388b-8958-addb750cf8d3 | -17.50167 | -45.00807 | 2026-04-24 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e86e999-6f5a-308d-ad4c-8b299b36211d | -20.18424 | -46.75894 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 221d62e3-ca8c-3228-937d-091ce9ef70a9 | -17.53361 | -44.75422 | 2026-04-24 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8daf3914-aa05-37c2-9669-a25ee19e8273 | -20.2485 | -46.77497 | 2026-04-24 03:40:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README2.md)
