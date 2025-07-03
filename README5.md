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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a7187e5-746a-38b8-941f-dbd3019b4ab3 | -6.9793 | -42.8798 | 2025-07-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| c91742d2-3ed3-3953-b82d-5f6eb0dfc34c | -14.6484 | -53.8785 | 2025-07-03 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 827786e6-c948-3fb1-9cfb-7ea3f94c3228 | -11.64 | -44.577 | 2025-07-03 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| bf11e077-5a7c-3589-bdf9-f5d9555043ed | -6.9602 | -42.9052 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.2 |
| e8099c7f-1aba-3473-bfa7-6b520fd8e9ce | -6.9605 | -42.8816 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 412.6 |
| ad94e4ff-14a4-3348-aab4-ee8e7b8d3c12 | -11.6396 | -44.6003 | 2025-07-03 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 0d03311f-975e-351b-babf-8af0088fb3fa | -7.2408 | -43.0664 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 37ae89c5-620c-37d8-8fdd-2e42b1b1106e | -6.1792 | -48.0494 | 2025-07-03 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 39ad5905-ce62-335b-b0a9-a2069624763e | -14.6287 | -53.9018 | 2025-07-03 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 6e37e82d-db56-329b-8b67-0528b91e9e42 | -6.9416 | -42.8834 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.0 |
| 082f964a-9c35-3672-8ccc-1438812e9986 | -18.2 | -51.3481 | 2025-07-03 02:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| c4adc41d-faa2-34f5-923d-bc330037a3f5 | -11.6592 | -44.5741 | 2025-07-03 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 6d0f039a-223c-350d-a91e-826fadc18a77 | -6.9793 | -42.8798 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| cc4fbdcd-dadb-3495-ba06-f5427617bf99 | -18.22 | -51.3446 | 2025-07-03 02:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 225.8 |
| a2f68c5f-cbdf-3572-a204-39082f906cb7 | -11.6785 | -44.5712 | 2025-07-03 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6f8f1e2d-448a-3656-93fc-659fab996f6b | -11.678 | -44.5945 | 2025-07-03 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 1f91ce56-5746-3e9d-ad1b-e6fa5743e215 | -7.2219 | -43.0682 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 177.0 |
| ac1ee483-a46a-3633-80f3-23fc546aa492 | -18.2195 | -51.3666 | 2025-07-03 02:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b51a1f5f-025c-3ae0-b81c-67a7cc488577 | -6.9607 | -42.858 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 3f47210a-3632-38af-b473-d59035d3acf7 | -7.2222 | -43.0447 | 2025-07-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 15c54f96-9648-3072-a15f-91f0994ba96f | -14.6291 | -53.8809 | 2025-07-03 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 85ad44d9-b7e5-31aa-a411-d24ae7db2e7f | -11.6588 | -44.5974 | 2025-07-03 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 408.2 |
| 3c8ffe97-44af-3e14-83be-f4f77ea1b7ba | -18.22 | -51.3446 | 2025-07-03 02:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 159.9 |
| c9a2bf8e-c784-3710-bdc6-813d31860f3a | -5.9938 | -43.7366 | 2025-07-03 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 4ea20a0f-6b64-3063-8374-a0c3f1ed425a | -6.1792 | -48.0494 | 2025-07-03 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5c599587-65d3-3a5a-b8c3-8d4d1b9a1ea7 | -6.6112 | -43.8941 | 2025-07-03 02:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| a67f7542-7ebc-3d3b-817a-1601af6e00d4 | -6.9607 | -42.858 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 784f8942-1d08-3ba5-93d5-6037deb10ad1 | -6.2757 | -43.6675 | 2025-07-03 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| e9f40c52-e6e5-3b8c-bce0-88b93379d588 | -14.6291 | -53.8809 | 2025-07-03 02:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| cb5cfba5-cd9f-3f49-af3e-89db33965a60 | -6.2943 | -43.6891 | 2025-07-03 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5830127d-acbb-324f-a314-bc26dde1c0ac | -18.2 | -51.3481 | 2025-07-03 02:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 2612f367-7688-3826-9b97-3843748e70c1 | -6.9416 | -42.8834 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 199.6 |
| c49de768-84d6-3036-923e-cadf72b8f36b | -6.9793 | -42.8798 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| d390527c-2d75-3105-b0c7-ddd2a5a7780a | -7.2408 | -43.0664 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 8708b465-fdae-366a-ba33-e8fddaffc0ed | -6.9605 | -42.8816 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 416.0 |
| 54f13e9f-895e-3954-bae1-2980a3d81eec | -6.2755 | -43.6907 | 2025-07-03 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| c64f7f61-8882-3e7a-9b24-62dc114d9749 | -6.9602 | -42.9052 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| cc09f6bf-1972-3f81-8f17-9dbf5bf56124 | -6.2945 | -43.6659 | 2025-07-03 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 72be5553-21ca-31d1-a4ea-ae58124ae031 | -7.2222 | -43.0447 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 8b3589a3-348a-3e71-9909-429ca63950d3 | -7.2219 | -43.0682 | 2025-07-03 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| 297fd664-ce13-35a9-b155-4a476a994b92 | -18.2 | -51.3481 | 2025-07-03 02:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 07e4a45b-0625-3632-8ddb-fff9cd4192cf | -7.2408 | -43.0664 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| b127c2ec-f981-3d7e-a218-f2626bfa5bda | -6.9605 | -42.8816 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 454.7 |
| 8e32f48a-4dc2-3509-a734-daf75f87a9c1 | -11.6396 | -44.6003 | 2025-07-03 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 2a5c0160-5c80-3802-849f-f6914116b30a | -6.1792 | -48.0494 | 2025-07-03 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8212ea33-7ffd-3362-bd69-681f0867295b | -11.6592 | -44.5741 | 2025-07-03 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 94c57e36-8e24-3b9c-95a1-4a804fdfc582 | -6.9607 | -42.858 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| c8c67dc2-35c9-3987-a72a-9eb9d36fe484 | -11.678 | -44.5945 | 2025-07-03 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| da5d25a8-ff12-3e78-842e-811db4d22acf | -6.9793 | -42.8798 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| a9d69027-f7d9-3ac8-8f9c-50d26fda22b2 | -11.6588 | -44.5974 | 2025-07-03 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 233.5 |
| a232eda4-a1c0-39cc-8b33-29b89b10b079 | -6.9416 | -42.8834 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 186.8 |
| 7a709936-d15c-30f6-9c68-efdc4f9893c7 | -18.22 | -51.3446 | 2025-07-03 02:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 8326a0fe-f271-38d9-8b47-9f3d73eb37f2 | -7.2222 | -43.0447 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| be886626-7215-3131-b9fd-ac72a4bad318 | -18.2195 | -51.3666 | 2025-07-03 02:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 95ce7305-4374-3220-94f3-884739dd70e2 | -5.9938 | -43.7366 | 2025-07-03 02:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8a99a44a-3e4f-336c-bf1b-b803abfc0af6 | -6.9602 | -42.9052 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 1e5f4107-8a4c-3f51-b4f6-c5d5999a08a5 | -6.6112 | -43.8941 | 2025-07-03 02:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 6e259beb-0b46-3e17-bdfd-f03e647a42cd | -7.2219 | -43.0682 | 2025-07-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| e5014584-cdda-3c60-87aa-62a1495f56f7 | -6.9793 | -42.8798 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 84f83916-4c71-3aca-a887-b48633997e2f | -7.2219 | -43.0682 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| f3ccfaa8-3fbb-3843-9da7-7ebca78d81ce | -6.9602 | -42.9052 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| 5cfb575c-b6ec-39ac-8e85-bb73d4d8aab5 | -18.22 | -51.3446 | 2025-07-03 02:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 067529c5-186c-3cfe-847d-3a3f44e07f60 | -11.6588 | -44.5974 | 2025-07-03 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 870b1f6c-1ca1-3239-94f4-4c3044f2715b | -6.9605 | -42.8816 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 470.6 |
| b2619967-6f65-397d-8bcd-46f87ceed74d | -11.6592 | -44.5741 | 2025-07-03 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 19c0f93c-be31-361a-b816-b2262ca8c042 | -5.9935 | -43.7598 | 2025-07-03 02:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| ac0d80c6-c6fa-3f29-afa8-5b89d5fcd2a8 | -7.2408 | -43.0664 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| ee1328f5-2243-3b19-ac55-2fca5e179c2a | -6.6112 | -43.8941 | 2025-07-03 02:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 28cd6c4a-93d0-3392-bd18-2b932ac0e2d7 | -6.0125 | -43.7352 | 2025-07-03 02:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9eea0acf-2d58-3125-a68b-5bd1d1a23f84 | -6.9607 | -42.858 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| cf55a7d8-2a66-3dff-a4be-7ae255212c74 | -7.2222 | -43.0447 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 3bd82292-b5a1-34cd-89f6-ee28212d833a | -14.6291 | -53.8809 | 2025-07-03 02:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| d0e54007-cc33-3432-9e83-b62ce0508d70 | -18.2195 | -51.3666 | 2025-07-03 02:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| b1f663a5-5bd6-3c16-9c95-bb110a4ba2b5 | -5.9938 | -43.7366 | 2025-07-03 02:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| cd7136c7-fe93-38b1-8f85-9efbb1a1e4d0 | -18.2 | -51.3481 | 2025-07-03 02:30:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| daa0b7fa-c49b-33fc-9689-0298609950c3 | -6.9416 | -42.8834 | 2025-07-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 199aaae0-c9a4-3af5-b257-509b09b06115 | -6.1792 | -48.0494 | 2025-07-03 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0526c374-32ba-306a-a5eb-c5018d5c2cbe | -7.2222 | -43.0447 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| b8ed275a-ae65-3a94-854a-f4597c9ecc69 | -6.9416 | -42.8834 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 201.7 |
| b4feb6c2-b316-3d17-a532-4518bd383478 | -6.9793 | -42.8798 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 8db1757b-535e-3f32-84da-88e3b0c6d0d6 | -11.6588 | -44.5974 | 2025-07-03 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 2a885019-6937-3dd3-8356-07bc665aadf3 | -6.9607 | -42.858 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 65661105-5bce-32c7-b02d-fb7a47910f8c | -6.9605 | -42.8816 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 337.8 |
| 586b78ec-5fec-39ce-8624-4f79660c99eb | -18.22 | -51.3446 | 2025-07-03 02:40:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 8d8bd228-61bf-3055-a2c6-0cdccaabd754 | -14.6291 | -53.8809 | 2025-07-03 02:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 8238b08a-d0cf-3348-9dd6-8714bb861214 | -14.6287 | -53.9018 | 2025-07-03 02:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 40625c9a-f0c4-3e89-8fa9-ee9fc099f5c4 | -5.9938 | -43.7366 | 2025-07-03 02:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a1f1c1f5-a983-37e6-bca2-f2c39da286d6 | -5.9935 | -43.7598 | 2025-07-03 02:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 1a406d9a-65e9-3186-8b44-0a1d652669fd | -6.9419 | -42.8598 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 12a747a1-ff70-3d2a-aa58-4c0a2d78959d | -6.9602 | -42.9052 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 2d8b5c25-a138-34ae-9fff-92971a676d8b | -6.0125 | -43.7352 | 2025-07-03 02:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f35a802a-204f-3e39-99a6-2d34e0359a01 | -6.1792 | -48.0494 | 2025-07-03 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 53a2ccb9-850d-3b2d-be6c-54020ee32f36 | -7.2219 | -43.0682 | 2025-07-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| 5c43c8bd-fd08-350a-a5c0-81595f47615a | -6.9605 | -42.8816 | 2025-07-03 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 389.1 |
| c78c43fc-e76a-35cc-a136-124b34fa5076 | -18.22 | -51.3446 | 2025-07-03 02:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f7af7804-19b4-3916-9965-6c5d5bcb7a5e | -6.2943 | -43.6891 | 2025-07-03 02:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| be86f2a3-c222-3f25-8469-80ed204c80ce | -11.6588 | -44.5974 | 2025-07-03 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 13575346-566e-38d6-b43b-c22f0f1b41df | -6.1792 | -48.0494 | 2025-07-03 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 48e4fb37-728c-3983-a56d-54ed7d5bfebb | -6.9793 | -42.8798 | 2025-07-03 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 234c43b9-f685-35b0-8d0c-e9b5f2870658 | -18.2 | -51.3481 | 2025-07-03 02:50:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |


[Clique aqui para ver as próximas entradas](README6.md)
