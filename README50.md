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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30c156b5-7132-3cf7-9313-6d88f7422f12 | -1.19391 | -51.9777 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13ffac08-5f69-349c-a8c2-6d9a4e8f767b | -4.32172 | -49.3894 | 2024-11-20 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d515a40-3efd-37ff-a71d-06da5b615851 | -1.51004 | -52.0913 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e9fd22d-ce48-39db-8839-374c39308f6f | -2.30091 | -48.49284 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d71020bf-56e7-3ea3-b4c3-8c3c2f5425a7 | -1.15138 | -53.5191 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54650f2d-d3fa-3c75-9fd7-9fe721477c37 | -2.29506 | -46.37405 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0b81b91-d01f-348b-8847-8193f31195c8 | -1.33518 | -52.23898 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f4be170-7efb-3c0f-9149-a2344ec3047a | -4.05952 | -46.8434 | 2024-11-20 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 127fa081-c7a9-3330-8925-1ba936f89acd | -1.30008 | -52.24429 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f47e5d96-c38d-398b-af94-b7d2f92131f9 | -1.51893 | -51.1585 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bf99a9d-b9a6-3263-a768-71eab277aa1a | -2.00606 | -49.00549 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6df1d6e-513a-3644-a43c-8b6509037f81 | -4.43852 | -50.13192 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9954f438-539e-3f72-9149-672e9564cfee | -3.55084 | -50.27556 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a638e7c0-7d3b-35f1-8697-5484051fa6d7 | -2.88149 | -53.96459 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8a83f6f-091c-3c41-8842-31ce9ae717ee | -2.03363 | -48.73199 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83d8b19b-d692-368c-843b-65fbcaecab94 | -2.52423 | -44.99377 | 2024-11-20 04:50:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55af2986-52e1-3b17-9ea0-1e2768fae52f | -2.36052 | -48.60665 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f767cb9-f604-34ca-b37d-199c514bf307 | -6.98411 | -47.08661 | 2024-11-20 04:50:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc053a8e-f11d-3e98-a31f-a76055b9a171 | -0.81804 | -52.5096 | 2024-11-20 04:50:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dbb42e5-cc84-3ca2-985e-4704ce557650 | -3.51579 | -53.79782 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ce64f16-a94c-3d0d-a675-257f65a31bc5 | -1.51616 | -51.15454 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6c090f-251c-3bff-808d-22a49f69433e | -4.15539 | -43.97493 | 2024-11-20 04:50:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbf25af3-c235-3393-9b1c-f6c2c141631a | -1.26927 | -53.41317 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3962228-e702-34ac-a86d-f39b5dd662a9 | -1.20772 | -51.75968 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1f2a225-8f6c-30f3-b1b9-803121243534 | -3.59008 | -43.62328 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c7ccff1-a7b3-3bc8-8bca-2cc8321bcbb9 | -3.36549 | -54.10056 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03605d65-a842-3029-8a73-b3ef161647b8 | -1.45597 | -52.67083 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 056a4664-c842-331b-a1b8-18cb4959a92a | -0.91277 | -51.73817 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1d24b01-23ce-30f5-8c47-5b6e2b4ffa14 | -3.37394 | -44.42774 | 2024-11-20 04:50:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf6f77f4-8d3a-38b3-ada2-8b764805d617 | -3.84122 | -41.56535 | 2024-11-20 04:50:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 84aa9a81-9e97-39b8-bc39-a95fe2204a4e | -2.58101 | -51.72034 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779ee091-9d15-394a-9f48-78c00df2b6c1 | -0.91025 | -51.73793 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a979b7f-1bb3-39c2-9991-fb95de1630df | -3.18541 | -53.24346 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee475e4d-b805-37dc-89e4-cff12ddb778d | -0.93639 | -51.65331 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fb77db9-65d5-3490-8473-5988102f48f5 | -1.64596 | -52.68535 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23d64335-5d9f-3c99-8b77-0e8b64452140 | -4.07687 | -50.03643 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0df98f8c-1d2d-32e7-8929-21546f3dd650 | -1.6649 | -54.90315 | 2024-11-20 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e1888f4-6cd6-3fbe-95f7-0271e1dba8b1 | -2.23964 | -53.61493 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b63a4664-dc07-313f-b7aa-4cf5f1ca463d | -3.07146 | -49.20058 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1873b26-7752-36ca-9808-c2f8ba21e6b2 | -5.25467 | -43.83551 | 2024-11-20 04:50:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f157fbca-b42f-32d5-92b0-400ab0f62203 | -3.18822 | -53.2476 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30a82bf7-ec1e-3a1f-aeee-628b2c6176bc | -7.14913 | -48.31861 | 2024-11-20 04:50:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ccd6a58-321a-3144-816c-d3a3b7a70b81 | -0.63348 | -51.73046 | 2024-11-20 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc04b8e1-8b41-3558-8690-afa8e16ef779 | -8.31898 | -45.10729 | 2024-11-20 04:50:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba0d2d91-f264-3b0c-9ba8-561945c4482b | -1.32166 | -51.8767 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b90ecf6c-ccef-392e-814c-717b9e9c6e4a | -3.07012 | -53.28489 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64a892f0-31dc-3887-92bf-fa0d9fc4cc3c | -1.72921 | -52.80073 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0647e836-28a4-3a76-befc-a30d3e470159 | -1.96867 | -52.1025 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d943a39e-00ea-3262-afe1-7c3bfde15779 | -3.72956 | -47.37461 | 2024-11-20 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0358b93c-fefe-39e1-9486-e98845878f08 | -2.61992 | -51.79703 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2ac3988-f433-3bbb-b122-b936336728c5 | -3.36076 | -46.23923 | 2024-11-20 04:50:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 010020f1-cf5d-3fa7-a686-96b37fe57a66 | -3.22033 | -53.02477 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b155d583-5e7d-3902-a83b-7a7c41e2202f | -2.79109 | -51.71767 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d703a680-0454-35f8-819b-6da27baece63 | -1.23935 | -51.75045 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d14ff599-a16d-3b96-877f-eccc396edbd8 | -2.62957 | -48.48887 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 232d2ba9-0a59-3f09-8f66-d1b921b40a8a | -2.4895 | -49.02467 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7326306-2724-3628-9ace-4027cff40668 | -1.64542 | -52.66702 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8fa7556c-f9ab-3023-bf0a-241460f123bf | -2.18625 | -46.9895 | 2024-11-20 04:50:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc1f4291-92f1-35be-9230-ff681d67bbc8 | -2.14356 | -50.65242 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c5d4fe7-0bb1-3dfc-ba2b-007eee2ad5a1 | -2.06837 | -51.47066 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f76282c-355b-3339-bee7-8e8ac9e95bac | -5.46864 | -43.9433 | 2024-11-20 04:50:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a5744de2-bfcf-3daa-9b53-1d0707e7d812 | -1.31698 | -52.39819 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7cbc06d2-a4b9-31be-8432-a3ed3dba46ca | -1.23711 | -52.02362 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dfaa49a-1a5e-387d-90f5-6054d9487b01 | -3.5164 | -53.79409 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad904248-7863-3687-98bd-6a058cacd459 | -1.14109 | -51.6856 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dc61784-4cc5-3b95-9905-4a6106f67553 | -3.28422 | -53.83226 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 33aadc77-10cb-3119-b090-9ed84384197d | -1.54386 | -52.05025 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3421c0ea-bcdf-3e8c-98a6-8b2f901dd0fd | -4.10744 | -51.04988 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d40b65e-dafd-3eda-a2f8-342212663bef | -1.33024 | -51.41142 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15257cc6-b2a2-3c70-83da-868b2a0bd614 | -2.81006 | -48.23424 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b163c8f5-47e6-3516-a79a-9f46cf132645 | -4.24625 | -53.66582 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2a91b72-1224-306b-ae2c-6b1802ab8e5b | -3.51371 | -50.22211 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba65755e-47fd-3fec-b929-44d38e6599cc | -2.66074 | -46.61179 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d807a8ca-b336-376b-9714-78e15306ab95 | -2.21621 | -50.70334 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74b3565a-0331-3e24-a717-6d07d864a073 | -5.96187 | -48.06496 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e15c8768-ba8a-35ec-aad3-2b782ad3db78 | -0.9694 | -51.78954 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c602221d-0805-3ce8-864d-5f4f008951c8 | -2.68749 | -46.07972 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eea70e27-4017-3ded-b6ed-072f498d01a1 | -1.64822 | -52.6711 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f4f94ec6-d47d-38b8-9035-7d04ef24a0b0 | -2.19758 | -49.86626 | 2024-11-20 04:50:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9704e97-a913-39aa-ac09-c8cafcc43d08 | -1.20757 | -53.69191 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e2df18f-36df-3831-95b0-def1634d0b36 | -2.5799 | -51.92155 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe4e7ed5-0f2c-3b1e-a46b-06ea2f8c2672 | -2.7634 | -53.2158 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73e20c66-2622-3f88-a476-fc7a72988e23 | -2.69836 | -49.32418 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bcdaf4c-2e9a-3a9c-8d86-a70a5f5b10eb | -2.64145 | -46.21575 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 879cee3f-54c0-34b8-831e-5765b7b907d1 | -2.56721 | -54.96955 | 2024-11-20 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77f09d07-82f6-3d8d-953d-f3ff56759671 | -2.1309 | -48.5283 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbff022a-3004-3011-ac1e-37d57464d980 | -1.64485 | -52.67058 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a55a6917-f7af-3b0d-a41a-28309bd9bdfa | -1.00859 | -52.44868 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 406a4dd9-3d90-35bc-a1e7-3bdab18d9b82 | -3.06091 | -54.40289 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d468084-8f4c-30a8-beb7-c6b2f358144a | -2.89364 | -52.43987 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5c50915-9df8-3b87-a5b8-e10f1d40ea88 | -1.22277 | -51.79391 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58b496dc-3439-345c-903f-2c3b80d01327 | -6.24544 | -47.26947 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a3f5f37-24e1-340e-8b09-0344f7470eb5 | -2.90655 | -53.06045 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9848416-1d96-324f-8497-0e4a22a7c854 | -1.32314 | -52.40277 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0c177e49-e975-3a4e-af70-9a64a70571d3 | -1.13946 | -51.69596 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14afa8b9-da2d-3bb7-bdaf-7b8a05f8c5f2 | -2.15589 | -50.7044 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bff70f53-2f6a-34b8-ae61-256002d212fd | -2.72632 | -48.72877 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e161c4c-f32c-3e5f-b3ea-d14ef83700ab | -2.03066 | -51.17497 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d61028df-0bf0-315b-b35e-133387f73eec | -2.57128 | -54.07597 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c526897-b267-3bff-a9ff-5f364177414c | -2.92625 | -53.06729 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README51.md)
