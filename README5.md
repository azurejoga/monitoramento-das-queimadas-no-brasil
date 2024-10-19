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
| 9ed033c4-8b27-3c99-b191-f9a608318640 | -12.5149 | -63.2822 | 2024-10-19 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ebb7066f-9948-3344-9605-5584adc9ac0d | -2.8155 | -51.2943 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92b1927d-f46a-3514-abb6-0d48a87b2146 | -2.818 | -51.305599 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1c2cba-1b16-3d0f-8edd-c6e71186e7fe | -1.71 | -46.479 | 2024-10-19 00:36:17 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3afedeaa-7b41-3dce-9a72-dea6ffabb3d6 | -1.7116 | -46.485901 | 2024-10-19 00:36:17 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67647741-3fba-3b12-94bb-44a1ebb84d33 | -2.2448 | -48.82 | 2024-10-19 00:36:17 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1477a95f-52de-36f3-ae0e-8fe425f6c117 | -2.2466 | -48.827999 | 2024-10-19 00:36:17 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b796166e-2833-3cd9-8334-882f7097623c | -2.235 | -48.822201 | 2024-10-19 00:36:17 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7bad0d-a3b2-3546-bd57-edb71331bc3c | -2.2368 | -48.8302 | 2024-10-19 00:36:17 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e68beaca-64d5-315b-a31d-94e61338e502 | -2.8062 | -51.3437 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 583f33e6-4fb1-3f50-bbbf-87e3a6f5c064 | -2.3452 | -49.351601 | 2024-10-19 00:36:17 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb9dbf1-f2b6-3ee3-8df3-8b0b1b226677 | -2.3471 | -49.360199 | 2024-10-19 00:36:17 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d55794b7-77ad-399a-857a-0e8e37e5970a | -2.7938 | -51.334599 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 660e69d1-e157-3a6c-b6a7-f477c187e2d9 | -2.7964 | -51.345901 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32efee2a-1994-3dbc-aa90-c64c64acb7c9 | -2.8563 | -51.6119 | 2024-10-19 00:36:17 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab234a3-8675-3555-8e93-9ad00dc47474 | -2.7891 | -51.359299 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d99087df-3b1e-306f-b7fd-069014e54c60 | -3.4122 | -54.142601 | 2024-10-19 00:36:17 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be28ed63-e56f-3a0a-9523-b9c698bc32c9 | -2.7768 | -51.350201 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdf5ce7-b5fe-3f10-84c9-9841f052536d | -2.7793 | -51.3615 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb3f441-9040-38bb-89ed-88a7ab21e42b | -2.7819 | -51.372898 | 2024-10-19 00:36:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c501a6a1-28bc-33e4-b54b-6a505c45afb4 | -2.7696 | -51.363602 | 2024-10-19 00:36:18 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85d79620-aa46-3183-8b99-2cbacee19a0d | -2.4452 | -50.2463 | 2024-10-19 00:36:19 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e04a1cb0-c6a7-3917-b1a1-dc568af73229 | -2.7239 | -51.616001 | 2024-10-19 00:36:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac7ad42-0e0b-3c7a-be81-9aaffa005f0d | -2.7266 | -51.6278 | 2024-10-19 00:36:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25cbae4d-2b9e-3928-b335-81b5990c0365 | -2.9689 | -52.842201 | 2024-10-19 00:36:20 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f04404bc-368c-3260-b8cf-596dd3bb5cb4 | -2.9558 | -52.829899 | 2024-10-19 00:36:20 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04954109-9e17-3587-9ee8-4b69408e7603 | -2.9591 | -52.844299 | 2024-10-19 00:36:20 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6cbba26-fc86-34fb-9c9a-4cd5039359d5 | -2.9623 | -52.8587 | 2024-10-19 00:36:20 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f27e8621-9268-3189-a490-00142df20487 | -1.659 | -47.1563 | 2024-10-19 00:36:20 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f6e1e0-f5db-3dac-805e-41cd2b6e8702 | -1.6606 | -47.1633 | 2024-10-19 00:36:20 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468d2cfd-3eb0-3960-b7e1-0223bb2ce299 | -2.9396 | -52.893902 | 2024-10-19 00:36:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcacd4e2-a380-3726-a4e8-54cda4155100 | -2.9428 | -52.908401 | 2024-10-19 00:36:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adfc140c-9763-3998-82e3-29ac15b00a72 | -2.9461 | -52.923 | 2024-10-19 00:36:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a777e7df-c878-3bdb-bbd1-de63a3d8e580 | -13.3717 | -50.8013 | 2024-10-19 00:36:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b8599341-909f-315d-98bf-db5562e835a9 | -2.9298 | -52.896 | 2024-10-19 00:36:21 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dfc561c-eb9c-3032-84ee-8fae756dfade | -2.933 | -52.9105 | 2024-10-19 00:36:21 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aace495-8c2b-3326-86b8-4258259f4419 | -2.9363 | -52.925098 | 2024-10-19 00:36:21 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edb7b4a0-7f44-396d-8add-b8ee03a4d938 | -1.9565 | -48.684399 | 2024-10-19 00:36:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13cc578a-bc4b-3168-90d6-2a7d2b6b6e4f | -1.9583 | -48.6922 | 2024-10-19 00:36:21 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e514ee75-588a-3c6c-9fd6-82b5ca398125 | -2.6015 | -51.754799 | 2024-10-19 00:36:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e45b0dbb-c8da-3313-a59d-9caf5486b59c | -2.6042 | -51.7668 | 2024-10-19 00:36:22 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c09d0bc9-6202-37a8-913d-9b0dca502990 | -2.7144 | -52.574299 | 2024-10-19 00:36:23 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93090af7-fabb-38bd-987f-09985bc4e848 | -2.5021 | -51.814301 | 2024-10-19 00:36:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c5ae98-25d5-3360-bca2-d345e1c9e740 | -2.8416 | -53.323002 | 2024-10-19 00:36:24 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ef5d99-5dee-37b7-8063-946b59753a63 | -2.4923 | -51.816502 | 2024-10-19 00:36:24 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2c84d7c-bcb4-3c9a-9fc6-8e1c60abb2af | -2.8318 | -53.3251 | 2024-10-19 00:36:24 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f82c9b55-2015-3d72-b014-4bf01c4b2b4a | -2.8353 | -53.3405 | 2024-10-19 00:36:24 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c00bd92d-0241-348a-8aff-39e63e59bf8b | -2.643 | -52.5756 | 2024-10-19 00:36:24 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 213ae118-3a69-3193-8725-25cf2c79d144 | -1.3321 | -46.945099 | 2024-10-19 00:36:25 | METOP-C | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7f6bd14-00e9-3252-bc3e-6a6956cf67a0 | -1.4221 | -48.148499 | 2024-10-19 00:36:28 | METOP-C | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a3aadc-e4cb-3a20-b353-eb955bf7db9c | -1.1258 | -47.304298 | 2024-10-19 00:36:29 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 147ca42a-9305-3fbe-b0aa-b8d473e20add | -1.1274 | -47.311298 | 2024-10-19 00:36:29 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79ce22ae-32a0-3b55-8578-94b0da0d4e13 | -1.129 | -47.318298 | 2024-10-19 00:36:29 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662b3e20-710a-3dff-bf8d-781aaa07c876 | -1.1305 | -47.325199 | 2024-10-19 00:36:29 | METOP-C | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9c502b-ad5e-3689-a072-7f20bc97f95c | -1.8444 | -51.355598 | 2024-10-19 00:36:33 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 496acffe-115f-32f8-bbb4-bbc87c1781f1 | -17.8207 | -41.3639 | 2024-10-19 00:36:44 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.5 |
| d600a833-5040-38ed-a55c-0bced1dccd98 | -17.8214 | -41.3384 | 2024-10-19 00:36:44 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.2 |
| 33506f6a-5a55-394a-9fac-16370c3361fd | -17.8409 | -41.3586 | 2024-10-19 00:36:44 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.5 |
| 787ef996-424c-3888-b5c5-8da4b5a80bd0 | -17.8416 | -41.3331 | 2024-10-19 00:36:44 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 160.8 |
| 9dbca549-c522-3526-839c-01872598205d | -1.1375 | -47.3179 | 2024-10-19 00:45:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 309b6946-afb6-3d7e-a3a6-af1441304134 | -1.1375 | -47.2961 | 2024-10-19 00:45:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fab408fe-23d3-348d-ba0c-c85995ccc9fe | -1.156 | -47.3176 | 2024-10-19 00:45:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bc25c0a0-968d-312b-811c-447c53722aca | -2.7885 | -51.3618 | 2024-10-19 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7b3d54d6-de3d-3fd9-a446-20661526840a | -2.8069 | -51.3613 | 2024-10-19 00:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 21d367f9-d671-3d2e-8646-4705283be3ca | -2.8738 | -48.2552 | 2024-10-19 00:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 55efb0c8-189c-377f-a958-606feeb27915 | -2.8739 | -48.2336 | 2024-10-19 00:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 90df3d37-1025-31af-a704-bfc0ef5cf72b | -2.8923 | -48.2546 | 2024-10-19 00:45:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 48771300-f25f-346a-8c0c-62b869ecafad | -2.9489 | -52.9174 | 2024-10-19 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 1cd9a52b-23c3-3d89-908d-956689e1e343 | -2.9489 | -52.897 | 2024-10-19 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 05949740-26e4-3af2-9705-ba6f1e1ab6d5 | -2.9673 | -52.9169 | 2024-10-19 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 702776a5-3cff-31f3-af7a-128344f6e178 | -4.1727 | -51.2337 | 2024-10-19 00:45:30 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 308dffdb-3cdd-3e9b-b5e9-d69852df6ca9 | -4.4167 | -50.535 | 2024-10-19 00:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d844061c-44ce-3ee6-b92c-5d74eb1b9187 | -4.6873 | -45.8504 | 2024-10-19 00:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 35bc234c-9933-32b6-92a8-75446bda7045 | -4.6875 | -45.828 | 2024-10-19 00:45:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 106.6 |
| a9295a63-b05e-3700-b98d-18fb55193d3c | -4.706 | -45.8493 | 2024-10-19 00:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 300.9 |
| da634823-5b79-38bd-9e00-ae8d1423c9cc | -4.7061 | -45.8269 | 2024-10-19 00:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 216.2 |
| 92f14d4b-950f-32f7-8530-642251c3ead5 | -4.7246 | -45.8482 | 2024-10-19 00:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4b3ba47f-cded-34a4-9f8a-77a652182cf6 | -4.7248 | -45.8259 | 2024-10-19 00:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7780b63b-0e6a-3929-8c71-7e1589c9f880 | -7.6815 | -47.3213 | 2024-10-19 00:45:49 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b95d8939-d849-33c3-a2e6-cca0b9158960 | -7.6391 | -73.1162 | 2024-10-19 00:45:50 | GOES-16 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 41.7 |
| ed6154c5-62e0-3148-a2fe-2c7676006959 | -9.0159 | -67.4645 | 2024-10-19 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 4e803ae6-efcb-33b3-a67c-5b895817fe0d | -9.0344 | -67.4641 | 2024-10-19 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 139.1 |
| bfe99d6b-32ad-379f-b388-2e7384e9346a | -9.0345 | -67.4455 | 2024-10-19 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| a33c8ff1-7cd8-39ec-ac56-0c2de2bcec6d | -9.053 | -67.4636 | 2024-10-19 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 53f0f3b2-949e-3da1-ab4d-6bd39bf34468 | -9.053 | -67.4451 | 2024-10-19 00:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4b8f3761-03ae-3c84-baa1-e23efd3e8c8a | -12.0041 | -63.5008 | 2024-10-19 00:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| bfa1133e-d358-3582-812e-21a6cab517b3 | -12.0228 | -63.5189 | 2024-10-19 00:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1289f2d0-bda8-3b05-9f56-487050176c06 | -12.023 | -63.4998 | 2024-10-19 00:46:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e9adce47-6a5b-3c75-ba8b-365a8e6e9566 | -12.4958 | -63.3024 | 2024-10-19 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f7d48d64-ff3d-3e91-887b-3902d3b6ec90 | -12.496 | -63.2832 | 2024-10-19 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| de73802f-32d5-358f-b300-5e3b0d638d39 | -12.5147 | -63.3014 | 2024-10-19 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9f01ac8f-8a35-3c0f-a944-8d0fd2f96a20 | -12.5149 | -63.2822 | 2024-10-19 00:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9b861294-7cd9-31a8-b2d4-5712de13e192 | -12.5336 | -63.3003 | 2024-10-19 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f3c3b8fc-0693-3a72-bb8a-98ec8885aaa5 | -12.5338 | -63.2812 | 2024-10-19 00:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7da15ea5-57b5-33a8-bd85-5e223ed31de2 | -12.7821 | -62.9601 | 2024-10-19 00:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0d5fdb3d-3901-3fa5-bf01-60adac2c64f9 | -17.8416 | -41.3331 | 2024-10-19 00:46:44 | GOES-16 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.8 |
| 9ef915d1-1b24-3de1-a047-9fd9811a4ce8 | -1.1375 | -47.3179 | 2024-10-19 00:55:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f77fa10a-459a-3db2-ab35-ca66a80f3b65 | -1.1375 | -47.2961 | 2024-10-19 00:55:12 | GOES-16 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 27fa551c-e717-3ff8-b5fd-6f131224e2b9 | -2.7885 | -51.3618 | 2024-10-19 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8b67569b-97e0-33e1-9f6b-ec52bf435226 | -2.8069 | -51.3613 | 2024-10-19 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |


[Clique aqui para ver as próximas entradas](README6.md)
