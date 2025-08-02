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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1502e697-d175-396d-bed7-af60becf73d7 | -4.23094 | -41.15455 | 2025-08-02 03:53:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9ee5693-dfdf-38f3-8eb2-8251804deb0a | -8.04457 | -43.11437 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 8a09abe4-fe0b-3ed9-b239-7c8c24f2a012 | -8.42665 | -47.47234 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3f18966-8fa4-3044-b327-bffa68eac448 | -4.25488 | -38.12064 | 2025-08-02 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b98a8b86-10a7-3c39-81bc-719e8c1ab14a | -3.24771 | -43.26391 | 2025-08-02 03:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 642cf3cc-00e1-3bb6-9277-bf3d5ae91df8 | -8.02682 | -43.12612 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 19cb7722-971e-33bb-9da9-e14584a120f4 | -7.66079 | -44.78138 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9e40fe7-cd1a-3f08-b805-68adaf429fbd | -8.02438 | -43.14048 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 8e2bc051-81a0-371e-97ca-97be47120fbf | -7.87448 | -45.53448 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cae5652-aee7-3e69-bcf3-0f9dc034d80c | -8.02822 | -43.14113 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 68360969-a4b9-368a-bae7-2bc955b2be6b | -4.3182 | -38.12703 | 2025-08-02 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 99e4a16f-3205-3d71-8ecb-f413190742ba | -8.05001 | -43.10549 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 633bdfd4-9ad5-3676-a821-786e2f037c02 | -7.24644 | -43.38553 | 2025-08-02 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 865a2009-a35a-34c7-9a31-1fbfacd11ae6 | -4.30795 | -48.10544 | 2025-08-02 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7cb199b-7954-3743-a242-4fef866ca12b | -7.43926 | -43.82642 | 2025-08-02 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a94b0cd-6e77-3d88-a1c7-a839d70d34a1 | -7.27812 | -43.05449 | 2025-08-02 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5691ef1c-4ef4-3150-a191-d0c601486337 | -5.48713 | -42.15835 | 2025-08-02 03:53:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 17edba0f-ca85-3f5b-9fdc-3167ab7704c5 | -3.59781 | -44.79828 | 2025-08-02 03:53:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 225ebf8a-fe82-33aa-a196-8876ebc502b3 | -8.43975 | -47.48732 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df7aefa1-4c3a-3797-8b6e-fb3c0bf4c92a | -6.52175 | -42.81662 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3409520d-cf34-318b-b267-36e68ecf5c54 | -3.77563 | -41.68301 | 2025-08-02 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b3ec9817-dcb7-37e8-9cf6-0a6e926571cc | -7.29192 | -43.06684 | 2025-08-02 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7e1b32c-f183-3432-9728-f3fdfff1fe96 | -6.90186 | -38.57138 | 2025-08-02 03:53:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 42827155-e1f6-356b-ae39-8b52d60ac4b5 | -5.57298 | -43.60448 | 2025-08-02 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dc77cb04-fefd-3c70-85bb-df1a6a9e577d | -7.28197 | -43.05516 | 2025-08-02 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb68d15d-1b66-33ea-9d69-b63c037a6017 | -6.52257 | -42.81178 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14ec2bb2-0293-30b1-ac60-1bc78a49a29b | -4.31428 | -48.10258 | 2025-08-02 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a619675a-0128-3dd1-844f-e10057f75391 | -8.43627 | -47.47729 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cfda4eb-d764-3564-a954-ec9d4b98e8fc | -6.88364 | -38.98683 | 2025-08-02 03:53:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82f469cc-95e4-3fe2-8d62-d0b811d1d75a | -8.44081 | -47.4813 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4aff3e0-3fa1-3ed5-b83d-355f0277c08d | -7.27321 | -43.3952 | 2025-08-02 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f8899aee-e1b7-3c78-9f5c-3891ebc9665c | -4.22732 | -41.15401 | 2025-08-02 03:53:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d655dba2-e15c-3e88-bd5d-0c66660d094f | -7.7429 | -45.14408 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c74a17f5-9e53-364d-bfe0-9121e383551c | -8.04074 | -43.11372 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| ca303b40-17cd-3e84-ae81-677509054b7c | -3.66208 | -41.12881 | 2025-08-02 03:53:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 35588ccb-7eb6-31bd-9d40-b7d3ec8773d0 | -3.59556 | -41.65113 | 2025-08-02 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70f3e49e-527f-378a-9218-a3df2d8a7f24 | -7.80944 | -44.92006 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ff75e05-2ede-3ef8-b458-32751fb44424 | -7.58183 | -44.8154 | 2025-08-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59e93a2f-d24a-3fe2-a5a3-076d51510013 | -3.77718 | -41.6816 | 2025-08-02 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c4012313-21bb-30aa-ba7a-3130e9bd2769 | -3.91181 | -42.42041 | 2025-08-02 03:53:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b3100954-9d0e-3ec8-a83a-cfac5fee5218 | -3.25125 | -43.26838 | 2025-08-02 03:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa92bccf-7abb-3176-8672-ef1ad3d5a6fc | -8.02357 | -43.14528 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 670c29c5-4478-334b-b808-23c10306caf3 | -8.03691 | -43.11308 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 641a7aa2-4315-3e47-ad08-c621a9286e78 | -5.64866 | -42.59208 | 2025-08-02 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00e75c61-97d8-384f-88df-2f0fdf0251a6 | -6.52725 | -42.80753 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a0388d3-0b7e-3cc2-a081-41724e86259e | -8.6673 | -36.23375 | 2025-08-02 03:53:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7bdc515a-3e1f-36b5-a59c-4a4dea700147 | -3.59109 | -41.65502 | 2025-08-02 03:53:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71e3739d-15d1-319b-8471-3aa4926a38d7 | -3.58144 | -47.51427 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d29e597b-f7ed-3271-a440-0fa886925336 | -8.02903 | -43.13634 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 58cef199-fbd9-39f0-97f9-21f5c8e56567 | -8.05384 | -43.10614 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 23ef36bc-9b68-3428-a6c8-cd98428de50b | -6.47482 | -37.91509 | 2025-08-02 03:53:00 | NOAA-20 | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e3daf9d-0d69-34a5-9a58-a0894bd4459a | -6.36418 | -36.90584 | 2025-08-02 03:53:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3bebf919-2853-3511-b95e-2216449a7cc4 | -7.87976 | -45.53075 | 2025-08-02 03:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adafbbf3-ef3b-3a49-b8a9-d57b4ac2c348 | -8.37724 | -44.03313 | 2025-08-02 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd2a1f2d-c6be-30f7-9c76-3666cfa4830a | -6.52034 | -42.81427 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ec2b23b-497a-382b-9f43-4d632a1266e3 | -8.03368 | -43.1322 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 183a317e-a12e-3416-9646-93d8a8d50db1 | -8.02741 | -43.14593 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f47e0076-e456-367f-8187-ee48166e9a85 | -6.69895 | -43.0745 | 2025-08-02 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0f54a0ce-16bb-338b-a9cb-9a84bceb44bf | -3.51194 | -47.2183 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27a091a3-3ef1-3bbc-b1d3-21f44d0fb869 | -7.23771 | -43.38924 | 2025-08-02 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c5dfe8ee-c3df-3d8b-acc4-b8f47d37b801 | -8.44028 | -47.48431 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd79b741-f5b0-3b40-8c4d-dd7b232d5775 | -3.82137 | -38.51902 | 2025-08-02 03:53:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dd62b7bc-f72f-343c-9705-543c75cfbd31 | -8.0361 | -43.11786 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| da287297-b504-3146-a1b2-aa8efbe217db | -3.77189 | -41.68243 | 2025-08-02 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9db361d6-08ee-323f-bd78-9f237dd5510a | -7.74728 | -45.14493 | 2025-08-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70004764-983f-3e72-b4cc-dfe72f18a56b | -4.26766 | -40.86072 | 2025-08-02 03:53:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 14d877f6-1057-3b67-ac68-9f3ec0891a9a | -8.43858 | -47.48246 | 2025-08-02 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7e81f20-04fb-30db-9b9d-64cc0cc628bc | -3.57638 | -47.5141 | 2025-08-02 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab04a146-d1b7-3ef8-a55d-e2610b84b0b6 | -6.42079 | -41.12529 | 2025-08-02 03:53:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 13dfa3a4-d809-3863-adaf-fcbbaef549c6 | -8.03449 | -43.12741 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 07bc1626-895c-352a-bc2d-5cf83b458096 | -8.01973 | -43.14463 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| d3529410-44ee-3b4e-92f8-151a73402b31 | -6.66481 | -44.73997 | 2025-08-02 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bf2eb6b-5f46-36c4-b9c6-6cd87a97b049 | -8.50443 | -37.94492 | 2025-08-02 03:53:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 94c86775-11f7-37ff-a6bd-3bc662ed8f93 | -6.88419 | -38.98337 | 2025-08-02 03:53:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25c9bea9-4710-356d-b671-5b6a30b0be2e | -8.02763 | -43.12135 | 2025-08-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 935931a1-0344-3f6a-a54e-2e8deb21a8f5 | -6.52498 | -42.81004 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f19b16d-4cea-3720-9791-2c72997188aa | -12.65442 | -44.50654 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c65d5b60-c4a2-35fa-83e0-bd3dcc94f5e0 | -12.42903 | -44.71199 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd15e36d-63d2-3d33-8e82-6790ea34d639 | -10.45597 | -46.93135 | 2025-08-02 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8766d421-893c-3567-8669-ec40440a2c22 | -11.51635 | -44.33356 | 2025-08-02 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68fb232c-d149-3910-9a7f-cd27c9e4ae07 | -10.25409 | -50.25859 | 2025-08-02 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0a0e2038-fddb-3c4b-bcba-25e6a3e6abef | -11.77576 | -44.99787 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d08f6776-3f2f-3298-a22f-2e5a2a584b97 | -12.65154 | -44.50325 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 617ab15c-bcd0-3cd7-a2b3-1144eb62be08 | -14.24645 | -43.13417 | 2025-08-02 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c565ec51-9a6b-328f-bcf9-bc951a57c114 | -12.65831 | -44.50726 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 73b574ff-618c-3858-93b8-77e611c656e8 | -12.65917 | -44.50224 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 17565428-d4f7-3d7f-9f09-82bf8ec8926a | -12.70854 | -47.79539 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c02d97e-86b1-3cc5-bd0b-a9bb984c5b8b | -12.67081 | -48.09122 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b9327e6-0ed8-3f82-860e-45d6a4748634 | -10.62361 | -45.29901 | 2025-08-02 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2652c38-e8c7-374e-9336-4ed5a2ce96b3 | -12.66391 | -44.49795 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 228e54c4-96bc-39f1-9277-b14b66996d5a | -12.66561 | -44.53699 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 82c86901-4168-3a3d-8191-9c54c93b25dc | -10.46465 | -46.96479 | 2025-08-02 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e87d463-8a75-3935-a630-e4e0b0da1f41 | -11.95635 | -46.66941 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6c7fe1d-bd42-392c-90c4-ddabf211a5c7 | -15.76317 | -49.94684 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| eb0dc8ff-4711-3358-8842-29cfd2a405fb | -15.10898 | -41.23098 | 2025-08-02 03:55:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46be2aaa-ac59-3861-aff4-733aa05b9379 | -9.19116 | -45.29116 | 2025-08-02 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc13afc4-7941-3331-ac57-cbb0a71b63b8 | -13.06006 | -47.44339 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d6ef360f-89e2-3ce4-a341-429b787b46d8 | -12.45744 | -47.07567 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cc5952b-8ab3-3232-8786-6aa315a221df | -12.65899 | -44.48396 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3d2c42c-8db0-3c45-9e14-68e8d3e61770 | -12.67751 | -44.49255 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README10.md)
