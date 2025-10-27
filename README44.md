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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0264e1f5-d173-367d-9b9b-4543b218fe89 | -4.26432 | -50.50792 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf77afeb-22f4-3187-bd13-4260693d3374 | -7.00377 | -46.98232 | 2025-10-27 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8119b5c8-279f-3c8f-b332-38b5d27618dd | -7.41256 | -46.99948 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b335997-05ed-35ac-9d40-1338d563859e | -4.45602 | -43.42929 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75b27b7a-db07-3550-9858-2a5a331f80a8 | -2.22615 | -48.37164 | 2025-10-27 04:32:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e56b1df3-66ac-3881-909a-96ac77937ca7 | -4.51888 | -46.46668 | 2025-10-27 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ed0cfaf-ba7e-3e48-a543-b8146438f30f | -8.48245 | -45.55695 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d83f146e-9b99-38c1-a378-6cd9773e98ae | -3.11795 | -49.11056 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f7e2938-aa38-3a27-9c39-b6844f1c134c | -6.16523 | -44.21657 | 2025-10-27 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e13750b3-a2fb-303d-85e2-7e6b18c3461b | -9.25446 | -45.5974 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 52ec62ac-81ac-3a22-8af3-73770259fcac | -7.76519 | -45.39018 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cf86619-77f1-3adc-adb5-b51cb5caf5af | -3.84122 | -55.79559 | 2025-10-27 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34ff8ca8-0ae8-3cf5-acbb-cd59bc5210a9 | -4.32337 | -48.08591 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c245e53-ba7d-348d-af5c-0503dd7da445 | -4.05457 | -47.50224 | 2025-10-27 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecf8b3ca-072b-3260-a525-db8f08e9e468 | -11.0275 | -47.85739 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c61af101-8a95-3a6b-a4a3-cd565e956637 | -16.62481 | -44.58577 | 2025-10-27 04:34:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 709d8a01-19d7-3f8b-aa8f-10a553bb4cfb | -12.07357 | -47.99552 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b061d5f-a98e-35e4-8913-3ac7bf4a9502 | -12.28395 | -43.75519 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0eb8529-ec62-3992-9048-cf9c1aa95438 | -10.63517 | -52.18655 | 2025-10-27 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0bbc2098-4fdc-3f03-a181-1d1c004edce6 | -10.31486 | -47.17999 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5c67852-32f9-3838-9e29-5906cc136e89 | -17.69634 | -43.96262 | 2025-10-27 04:34:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25a32642-d951-3234-8319-60a74c613fb1 | -18.15142 | -44.25711 | 2025-10-27 04:34:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35db848c-5a55-36c7-90f8-8b5f426316f2 | -11.01908 | -47.8013 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7400a93c-5dee-3f23-9176-a0064a2633c9 | -10.34122 | -54.19708 | 2025-10-27 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33c9cc14-ce3c-3158-a747-820a333fedaa | -15.50837 | -50.01551 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49671f2f-1f62-3193-9a1c-642454a43d48 | -14.63786 | -48.40654 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2addb7fd-edf1-375c-afb3-0cf30f3c2e1b | -13.2872 | -54.38988 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3710a3bb-6466-327e-a143-a5b2ec52e1f6 | -12.31171 | -47.44836 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9550bf27-c12d-3594-a011-48ab061b60d6 | -11.63168 | -54.5792 | 2025-10-27 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b022e141-1010-31f7-b16c-42325c2d6249 | -10.35745 | -47.17179 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fa0b9091-240d-363d-a2ca-c9f7a827f729 | -10.95757 | -47.58247 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 359ca8b6-2b7e-3a81-b622-aa30911c8e74 | -11.67416 | -41.32277 | 2025-10-27 04:34:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| afc10b12-036b-3f40-b461-cadb8c828c13 | -12.22191 | -46.52217 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43f3a177-d7cc-3454-863d-a67d8fbcfaf7 | -11.42125 | -46.09031 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a94ab875-8493-3743-b328-bd66b2697c23 | -14.55078 | -48.03499 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62fa78b6-cc9b-3816-b151-cd52862953a6 | -10.97714 | -47.87487 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 307fdba7-c88d-3fd6-b8d8-d4e58aaa372b | -14.62334 | -48.38928 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d7b1a33-9efd-3d62-a096-014c0ff0922c | -10.75954 | -44.20151 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 86f8b55a-06e8-3c64-8eb4-f66958c92d55 | -10.75247 | -44.19529 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e963ec7a-a5aa-321b-b4bf-6b17ace9041d | -14.82696 | -52.43243 | 2025-10-27 04:34:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1331a5b9-5f9c-3673-b9c6-756ebb43f9cd | -11.07067 | -48.32631 | 2025-10-27 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c5bfe030-d6c2-3e3c-a8b6-8f202c9dab33 | -12.53185 | -47.56839 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1998d325-6259-3503-9fc1-2b1bc3b881fd | -11.78969 | -45.259 | 2025-10-27 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de602a22-9170-3697-a1de-87cc7af081cf | -11.37828 | -46.06306 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b05c17fc-3e2f-3b77-b01a-e2392d6028b7 | -17.51709 | -45.09958 | 2025-10-27 04:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e34b0034-3ebe-3c1c-bad4-8fbc731a4db6 | -12.21144 | -46.49632 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13ced1da-0e20-3402-bac6-f5004cb1c708 | -12.76098 | -48.63272 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fe8942a-c3a6-36ec-b728-6621dbacde11 | -12.87639 | -48.65532 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f25d2a04-a161-3d39-bbc2-c8bcfb37fa4d | -15.50949 | -50.0084 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 4d87bcda-0db9-3d29-9f97-a041c5233215 | -12.13268 | -45.2116 | 2025-10-27 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 907f3d9f-ab55-3ccd-b95c-8aae2d0894a4 | -13.64264 | -47.61439 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dde23b2d-13f6-30b8-ba9c-b0d1793e6657 | -10.31541 | -47.17637 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d7bc611-5563-355f-b08c-81f992962657 | -10.31987 | -47.16967 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b83fb91-7c89-3ace-9707-57bf269c42fa | -15.15373 | -47.93613 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5bb4af5-cdb1-3996-bcb6-b9f3a706c3d1 | -14.25872 | -48.12985 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78de5382-7faf-36e0-85be-2278d2e0d176 | -12.5324 | -47.56471 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 922a56c2-2d73-39ca-9bcb-664bfd7b6e04 | -16.05739 | -51.48924 | 2025-10-27 04:34:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f0ac290-b097-3b16-9aac-6b3fe10b19ef | -14.55402 | -47.99011 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d592f4d-f1b5-39c3-a45b-00b0b6bd871b | -13.5563 | -49.55374 | 2025-10-27 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98f21923-8cd4-3487-9c28-2850841708a7 | -13.24579 | -47.97234 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dce9bc2-d916-39fe-9233-fbc9eee7e1df | -13.5596 | -49.55429 | 2025-10-27 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fd3a5f0-fa51-3798-bce8-3d259b7c3da8 | -14.83181 | -52.42513 | 2025-10-27 04:34:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dccbffb5-8f59-3470-a090-fe57b493f5bb | -11.83977 | -49.86173 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 050aa67a-26f3-357f-9c1a-ff14b849794d | -12.22891 | -46.52321 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f9ba395-db71-396f-82da-5401d0341c3c | -13.65443 | -44.30716 | 2025-10-27 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 409ae0ca-9c04-3632-a6b8-7fe58a982d46 | -11.16421 | -47.78712 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88674a6b-011b-35ea-adb7-3bdca8513142 | -11.42565 | -46.11036 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dd712ab6-12d2-3e7d-9ed0-d78925f1201d | -15.02728 | -47.39664 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 461af9a4-cb84-3355-9e02-39ad6886d0a6 | -12.5251 | -47.56733 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 40dd4d9f-d474-3745-b6b7-c91ba3f02dbb | -17.32197 | -43.65568 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 727255a9-a366-34e5-a6e7-8e926316f400 | -18.1557 | -44.25774 | 2025-10-27 04:34:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ee0ba26-5644-3f5f-b750-ef53772f04fb | -12.66088 | -52.63055 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bab510c7-2886-31df-8d71-356bf3c0d9a5 | -12.33152 | -47.47799 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 01800a3f-db2d-3a83-a1a0-cad7d4d57ab6 | -13.23634 | -47.98946 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cfb96f7-799b-3a49-8e0b-3e5d26dab786 | -12.23378 | -46.52277 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56cd32b0-c661-3456-9c00-e6909672bcf4 | -11.51067 | -48.23019 | 2025-10-27 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5646454-c0bf-35e3-92dc-e9f25cb5a425 | -16.62844 | -44.59021 | 2025-10-27 04:34:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c3efa79-57a1-386f-9080-62ccccbdf477 | -10.35847 | -47.11975 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d4866c0-d2f1-3ab3-bdad-bf920bae6cc5 | -13.6574 | -47.63186 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57c1344a-504f-3e1b-b4f9-8499560dabd2 | -12.23321 | -46.5267 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee17f06e-c406-386b-9fa9-899edad2e327 | -10.95477 | -47.57843 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85ba5940-694b-34bd-8984-5baacc629b3e | -10.50848 | -47.67353 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b39b4bc9-f408-3ead-b403-79263c8f3c72 | -11.02191 | -47.82731 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5c76314-7f2e-3c9f-908b-a33232b6d9f2 | -10.35971 | -47.1796 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8faf7b35-0352-35f1-a5fd-c405282c9251 | -13.28257 | -54.39278 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08211d80-70be-3790-acc8-1ff59a7156a2 | -11.05236 | -47.87166 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d565d8ca-8f62-3ad3-8a2a-6dac0e014bf4 | -12.87694 | -48.65179 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4b935ef-c36d-3ee9-963e-9f015ee8eb41 | -12.21492 | -46.52107 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6071ca20-7a2c-30c8-a4e2-bb5a459e2463 | -14.25535 | -48.12934 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feec7a26-d307-3d0e-8cd6-4fda1ba6da62 | -10.41494 | -51.61199 | 2025-10-27 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59bcda6d-f754-30c2-9288-476cf7af138e | -12.86808 | -48.64324 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a3ab719-c3b3-3f05-94b2-f19c1addce63 | -13.64077 | -51.96125 | 2025-10-27 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e21a5ec-766f-3887-9dc6-e825257d5e0c | -10.82852 | -47.62501 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f237b2b6-7944-3cbd-941a-2ca9ff7072ce | -10.99669 | -47.92491 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea024587-3daf-389e-a36c-dc30aa74efcb | -12.08188 | -47.98582 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed9cc4af-57a7-306f-bba0-d1abd4030a68 | -10.32989 | -47.14902 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ac86967-16f2-37ba-8134-d2be16c7e9e0 | -13.6432 | -47.6106 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a16fcd-d8d9-3a87-90e1-3c9bb855b98d | -15.51665 | -50.00595 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ca725cb-4927-3fe6-b13b-24950475fe09 | -13.50255 | -48.00761 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f1e531a-e4c8-3e2a-8c41-15bdb8cb5a0f | -11.91219 | -43.83109 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README45.md)
