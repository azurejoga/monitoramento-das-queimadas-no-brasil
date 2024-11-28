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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdff12a5-86d0-30e3-a6f9-e20ac5d69dc0 | -4.92863 | -45.42287 | 2024-11-28 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd45802a-3cea-371e-b199-d5474815500e | -2.1725 | -52.1407 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1381d0bb-0357-309f-8980-8a1d88127221 | -3.63245 | -54.44513 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0b698ab-75c5-3953-ae92-0448eec71179 | -3.96934 | -46.72201 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 630c5eb8-11b8-3a8b-9a9c-85c457173326 | -3.61053 | -51.16102 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0469cc-41d1-3ea0-accf-60d97aa3a582 | -2.01936 | -51.19036 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75dbd13c-5746-3802-b4ab-71f05b2da807 | -3.893 | -46.13156 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c4b3b27-2aaf-3b11-a5a6-8d6b3c194170 | -3.78839 | -50.13728 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f722914-35e1-321f-9cf8-415eda13e0dc | -2.70019 | -48.65606 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ceac6c4-e45d-312d-90bf-6f62c2670a8c | -3.80566 | -52.36166 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c4d6f2c0-52bc-3913-90cf-1d2627994ff4 | -2.71204 | -48.67523 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d9cf24f-440c-3456-8b09-2a4a8467eaeb | -4.00316 | -46.31591 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5191548-3f05-31c0-9377-b1ce20bf7c68 | -3.69551 | -43.42976 | 2024-11-28 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e902c4d5-6a03-32f5-acc8-ca53fba3b606 | -3.99161 | -48.93966 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82bf8456-b041-3e79-9e36-3a487ff9d41d | -3.20051 | -46.59866 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6bdfedc3-7834-39ae-ac38-d4d7ff2e01a6 | -3.7051 | -51.80027 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c127feaa-05f3-3166-a2f3-e89aa5067be1 | -3.0796 | -48.66875 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a887687-dda5-3c24-9d9d-6548f2d3de40 | -10.42061 | -49.24496 | 2024-11-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bfdacc9-c5b3-38e1-a717-e4adcaa93e23 | -3.49426 | -53.81786 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6af138d2-242e-394e-bc58-afa60e00c3cd | -3.46598 | -50.53695 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a94824c-81f7-3cc2-b57b-1298a7fdd1e2 | -4.00633 | -48.30298 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d5825f-2691-3fc3-9f24-9b42b298498c | -3.46282 | -51.59377 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 931f387b-4cca-3b0d-8cf1-d9d46d3d394a | -2.84979 | -46.83822 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83979438-beb9-30a8-a2b4-9d2f1f46dd5d | -2.47838 | -48.8028 | 2024-11-28 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3157911-b702-3177-956a-fc985389a3c6 | -4.1343 | -44.8328 | 2024-11-28 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e2149c44-333f-3888-afe8-3d47c9eadc55 | -4.30349 | -48.23252 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93c53b7f-c338-37b6-b270-6f45a6902bdb | -3.9619 | -46.89841 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7421efc-d6d9-3be5-9ff4-0742416591d1 | -3.73267 | -49.95633 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29c0e224-0b76-364a-838a-b827fb4e6c03 | -3.67787 | -51.85642 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50c4657e-8fa7-3533-a1db-5de4afc15ce8 | -2.65597 | -49.51148 | 2024-11-28 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3362341-6041-3d23-a1da-432f513f7e4b | -3.44942 | -50.29732 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c3d0adf-1274-3138-a7ee-affb36919114 | -2.65673 | -49.5068 | 2024-11-28 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eaf4b402-0030-38ad-b84c-fcda8a28d176 | -3.51669 | -51.656 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e31d0578-a942-36b5-9af3-f988fa982de2 | -3.39003 | -54.28516 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99bfe1fb-e7cb-38d5-bf63-38166ffce9a7 | -2.89101 | -48.09563 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90a19f28-0bf2-334c-870c-20e31fd6ce22 | -3.37225 | -50.42104 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d13d5a9-6a81-37e8-8a45-270b07012adf | -3.92601 | -46.39632 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3db116f2-4610-3bd6-8a84-018a53b5d7ca | -3.41728 | -53.88342 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65a03d5-af12-32b5-a3ec-3461afda79e5 | -4.22056 | -50.89582 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 194a8bec-a189-38ed-bfcd-28225b459434 | -2.58931 | -53.98138 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa7f2bb5-ab68-38d5-ba19-39fad00e9172 | -3.62196 | -44.04404 | 2024-11-28 04:25:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0407604-6de4-33f0-b13f-14c196e9ec2d | -3.96097 | -46.73159 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1efbedc7-f670-3162-b4e2-cfb1113033e2 | -3.68888 | -50.23157 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8cd527b-40da-3b16-b500-eceb0ba100eb | -3.18878 | -50.8282 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd253e96-8a76-3add-926d-4086829673ec | -3.37375 | -50.1179 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3da25aff-1b33-3440-a304-30bc5ff375b1 | -3.38414 | -50.32346 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06d14f72-5575-3989-a2c0-7023ad6758cb | -3.26897 | -50.44014 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92284447-2679-35b0-9ba2-e478ec474b26 | -2.777 | -48.10703 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 643def4f-583a-3e39-87e5-68de7912d646 | -3.23835 | -54.22273 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17e670fa-26e9-322b-99a6-44810bfc8c5b | -4.52769 | -50.4611 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a78e7587-4a20-37de-b511-df39b23a0c68 | -3.27707 | -50.01836 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9396853d-0963-371e-9c72-e793cefaedd3 | -3.4111 | -49.80882 | 2024-11-28 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f541544-fb92-3a59-8092-f3b0a3378f1e | -3.10546 | -50.36418 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 746a5404-feb6-3cea-bfc9-721eaeb9d1a6 | -4.47394 | -46.36852 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8cb6b3e-64eb-3fda-b150-dab77788c874 | -3.814 | -47.47561 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd14372-63fc-3160-8a10-682804cd71c3 | -3.43282 | -54.54257 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3627730-510f-3cdb-aa94-cbddf6e79e02 | -2.80226 | -53.04322 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd58c85-fd5f-3501-9efa-dcd9195f683a | -2.85704 | -46.85773 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dc2b019-5b48-3cc0-b62f-d2a7844e7459 | -3.95519 | -48.19161 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e845a16c-4d3f-3c56-b94c-81450dbbdcdc | -2.87876 | -51.47562 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef59da1e-01f2-3f60-8d79-b94e6cb9d24d | -3.93819 | -46.70269 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c56a45ff-452b-36be-ade7-3508c30e71ee | -3.37846 | -50.11357 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ebcbdaf7-e162-3272-a900-5ca6385ce428 | -3.80283 | -46.59496 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ae24f05-ca43-37e7-b9b9-dddbfc502fbd | -3.22 | -50.58759 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b3fe50f-82de-3653-9b7f-c5d64fe1c0a1 | -4.02235 | -49.54759 | 2024-11-28 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d58b731c-cbf9-339d-87d6-9aeef2086e48 | -4.08224 | -48.81982 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 077d0e2f-1ff3-35d8-83a9-86624be1c725 | -2.83553 | -54.12504 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae381458-7693-3750-a0ea-3b8febcd3a84 | -2.25754 | -53.7474 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe375121-0b23-346d-bc8e-a720958ef514 | -2.69567 | -51.68515 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a80aaf2-8fea-3518-8843-611c87f03bca | -3.95237 | -46.91517 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aea855a6-de36-3d16-ada1-e5384ae68dd2 | -4.1831 | -44.26117 | 2024-11-28 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf7af6c0-2d89-3ec0-a07d-893ed6b4db04 | -3.79806 | -51.39349 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12dcffa2-9b32-3506-92ad-a1fe8c9c50f4 | -4.05362 | -46.83323 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90a0a6eb-4340-3b84-97a9-880de2d5ba12 | -2.84463 | -46.87053 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e26b477-d939-3bfd-bf3c-34401e2920f9 | -3.9322 | -48.15604 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86bea54b-6c6d-3226-bd04-a8deff5b1ac3 | -2.64461 | -48.48553 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e4657fb-70a3-3889-8c24-9e56ed4a4c00 | -3.93761 | -48.14484 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03713236-cdf9-3da7-a1c6-a1aa5badb7a9 | -5.07771 | -44.83906 | 2024-11-28 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a320422-48b0-38a0-8bfc-c4a7ba72432a | -3.99984 | -46.3154 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7e1306e-58c6-395f-8d17-a6534d05432d | -4.21648 | -50.89516 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a876c2d7-3100-3f80-bf92-e2984b26d718 | -3.79949 | -46.59445 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eada7c5a-6dfa-3cf7-b514-27f6d414d484 | -3.85917 | -40.44739 | 2024-11-28 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1f51258-6186-3fd2-bc51-ee9ea94e761c | -2.05402 | -51.16698 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbd26230-0d53-3c7f-b937-8703c50d1dbf | -3.65582 | -50.23644 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bafa2f94-5a2b-3b24-b30e-0d158d325b43 | -2.83459 | -48.4711 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c614f1d5-4c39-392a-9e7c-d4081ef8aaad | -3.17264 | -48.58023 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c958f80c-8a48-3119-aecd-ddf2660b6ac7 | -4.43745 | -46.3415 | 2024-11-28 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 116eb4fb-41f8-31c7-a8fb-083660a33d6a | -2.90609 | -54.18216 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df720d1a-497b-3a00-b273-963bc0a4dda3 | -2.94216 | -51.58543 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1772b1e8-fa0c-3118-be98-5f3d5322d33a | -2.86192 | -46.6757 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5fcd1ec-1be1-3de2-b2f8-0ed0791b9960 | -3.82502 | -46.54096 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17cf9be-f9b5-3209-84f6-143bdc32fa8c | -3.57927 | -50.33295 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61f492a0-d644-32a1-96ee-eb0c8f0ac1ed | -4.48423 | -45.44126 | 2024-11-28 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a455acc9-c9d4-3032-9bb4-f2808153a9c7 | -3.19244 | -46.56818 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abd87e7e-ea17-360a-b1b7-476b2e408c90 | -4.04076 | -48.08189 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f1a7b2d-251c-352a-833f-3a7710c92517 | -2.91128 | -51.71738 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3035ddbf-0d41-37eb-a01a-8ae96cafb07c | -3.28981 | -45.51858 | 2024-11-28 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 21aa1137-acdb-345a-b317-7c8bddbe4660 | -2.53441 | -50.09613 | 2024-11-28 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36a00ea6-1a6c-3a2b-90b6-8c190a70f7e3 | -3.55004 | -51.50602 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d0480a9-0506-3a18-9582-99c6617fe81b | -2.9559 | -51.00417 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README67.md)
