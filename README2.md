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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c4fcad6-06a1-36e7-a1c4-51f50658c736 | -6.97042 | -42.87064 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9aaaf272-47af-3238-9c8b-6e440abef763 | -10.14733 | -36.26274 | 2026-01-20 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 67dae8f5-43ed-3e15-83a7-baec37024d4a | -6.99046 | -42.87769 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e75958de-1f46-3eb3-9bc2-8fb8fd5784b1 | -6.97108 | -42.86671 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 589a573f-0929-322a-b963-72b5a48cb81b | -10.14677 | -36.2664 | 2026-01-20 03:49:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9bdd014f-8014-3d1f-a258-064b2f0f9752 | -6.99162 | -42.87439 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d8187c9a-fd48-3b60-9aa9-8239d2ba00ab | -6.97532 | -42.86749 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5c3cfdc6-1fcd-393c-9bb3-dd1c60fd52b7 | -9.85558 | -36.92532 | 2026-01-20 03:49:00 | NOAA-20 | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9dbdd480-a380-3a7a-b011-3e84ede2004d | -6.98738 | -42.87363 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 744623dd-e1b1-30a9-876f-c1ff1d14892a | -6.61381 | -38.72177 | 2026-01-20 03:49:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 453d8884-b389-3454-bfad-1e39318069cb | -10.13916 | -36.40656 | 2026-01-20 03:49:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3d9744f2-3d0c-342f-81b3-7623795d2e27 | -6.97333 | -42.87932 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6ce8b4a2-c6ee-3f65-8502-dace9f01cf8b | -6.974 | -42.87537 | 2026-01-20 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bbe3e2f3-0321-3376-b74e-53edf7b90422 | -12.7797 | -38.49926 | 2026-01-20 03:51:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30a62bff-dbf6-33a4-8475-bd0c22f86c6d | 0.75184 | -59.65486 | 2026-01-20 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 671f9dc6-549d-307f-a73b-3ae9d85185b2 | 0.75459 | -59.65386 | 2026-01-20 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 814ca57b-defd-3d3a-999a-0e85c0e65092 | 1.13313 | -60.52736 | 2026-01-20 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e227216-80ba-36a9-a919-cea35ccc2384 | -2.46126 | -48.2333 | 2026-01-20 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2639710a-1897-361f-a21c-0c8afc126ddf | -2.46068 | -48.06021 | 2026-01-20 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c8cefae-19cb-3cd6-8b46-41f35f721191 | 1.13679 | -60.52546 | 2026-01-20 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6739676b-1295-357a-9134-49e795f81581 | 1.13219 | -60.52145 | 2026-01-20 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4c6e3f77-efd8-3847-89f6-a6b4ef1a45c2 | -1.52738 | -46.69448 | 2026-01-20 04:38:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b94cbfa-6cf4-3f2c-b389-b6ec6ccb87e6 | 1.12645 | -60.52831 | 2026-01-20 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 20942059-b293-3a20-bc5a-a6f96605fb91 | -2.41203 | -47.45873 | 2026-01-20 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f5edac8-f9d7-3f1c-9ae8-b9b5408f9fcf | -2.53256 | -47.79757 | 2026-01-20 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 567acedc-0034-364b-8fed-ab54914c5ca0 | -2.65624 | -47.26706 | 2026-01-20 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41367877-6980-35ee-a5a3-da03adabc3fd | 3.30877 | -59.99353 | 2026-01-20 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 123ef138-dbdd-3a67-84fb-4721b334df50 | 0.7526 | -59.65988 | 2026-01-20 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14d7ffdd-a14a-3dac-9b96-089b6e9e5e54 | 0.75539 | -59.6589 | 2026-01-20 04:38:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 265b4125-d89f-3d3e-b30b-89a282613a74 | 2.05094 | -60.86551 | 2026-01-20 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7d4e837d-2ab4-3f15-9b17-abad2576155f | 1.13589 | -60.51954 | 2026-01-20 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb1d5843-4d63-3ae6-9ac4-32b01d34e436 | -2.43778 | -46.91486 | 2026-01-20 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e05426a-c058-3c9b-9aeb-2fb742c3c252 | 3.31546 | -59.99279 | 2026-01-20 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8c0c3ee4-39a1-39de-a8dd-81bb0fd9a3bc | -2.5287 | -47.80055 | 2026-01-20 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d10b844c-893f-36d2-8b92-bdca9206b93b | -1.26254 | -47.173 | 2026-01-20 04:38:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97bb18b4-9c55-3337-9a70-4cf8ec04ce0f | 1.13012 | -60.52648 | 2026-01-20 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2419085e-fd5c-3e6d-a2e7-e99bddd8a864 | -1.67681 | -46.70273 | 2026-01-20 04:38:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97188093-a4a1-394a-b7ca-cae15c83546f | -8.23233 | -48.17979 | 2026-01-20 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90a1120c-3d59-39fa-aef9-77620a6f457b | -6.99651 | -42.86935 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9b89c6ef-144e-3266-9d50-b158a6d76f15 | -6.99584 | -42.87403 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| eda5a48c-271b-3e00-9a84-9b0a127b3ba2 | -2.36142 | -51.88939 | 2026-01-20 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24cafacc-7573-3953-80b3-880a7c315094 | -6.59961 | -44.32525 | 2026-01-20 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09622544-3070-3c4f-ad00-2913e10c3b2d | -9.11086 | -50.52813 | 2026-01-20 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb7e5d68-f86e-3971-a18f-9c5ecb991d8e | -2.36076 | -51.89355 | 2026-01-20 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 389b1adf-6334-31eb-ac47-025a5828afc3 | -9.1114 | -50.52465 | 2026-01-20 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 785eb5b1-0a2c-31a5-ab18-8b8d74f6e277 | -6.97698 | -42.87604 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a5d169a1-ec00-3601-aaa9-6e6184be4cdb | -6.38059 | -43.81745 | 2026-01-20 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 692626cc-5b7c-385a-b426-7f92dd724ebb | -6.99129 | -42.87339 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b5d22980-7ffb-34dc-a205-ff8dd4e21f63 | -2.35847 | -51.88466 | 2026-01-20 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 976838e9-cc70-3b8c-85c1-dbe47e4863d0 | -9.11031 | -50.53161 | 2026-01-20 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0223de14-df60-3b57-b80a-5195a7876a5e | -2.35715 | -51.89298 | 2026-01-20 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb592d75-9fda-39f6-b392-c7c7144e5e43 | -6.59906 | -44.32898 | 2026-01-20 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec6ec73e-3818-3859-809f-3dc511c5e117 | -2.35781 | -51.88882 | 2026-01-20 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 318eacb3-3c33-321c-9190-48d33a58623d | -2.93797 | -48.23001 | 2026-01-20 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fcc7f7d-7463-3480-87cb-c66dd9c2a992 | -2.93466 | -48.2295 | 2026-01-20 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c73a1d2-05ce-34a3-9d8d-3490f8f4fce8 | -6.97632 | -42.88073 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 087f637b-6ea1-3e1c-b208-327b538ebfe4 | -6.97308 | -42.87073 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 068759da-ae45-3c2f-87be-ed60cd0a4af6 | -6.97374 | -42.86603 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 73c078db-7d17-30d3-a2e4-b77c9fcb0aed | -6.9783 | -42.86665 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7d439e77-9ea9-3c4f-81e4-95ad7e829985 | -6.97242 | -42.87542 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 120f95a4-e08b-3832-817e-29b02aa52ce7 | -8.23177 | -48.18351 | 2026-01-20 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfac722a-b807-3df7-acc1-acaf678a291e | -8.22837 | -48.18298 | 2026-01-20 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59620282-6678-342a-aeb6-4a34ebbdbee0 | -6.98673 | -42.87273 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1b9b20b7-5936-35e7-9caf-e74db5b0bccd | -9.107 | -50.53109 | 2026-01-20 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 474b941a-44cb-368e-bf3d-f238515ba05f | -6.97176 | -42.88009 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0afce35e-d1de-3d06-abaa-f7a80690ee64 | -6.97764 | -42.87134 | 2026-01-20 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3feb9499-2977-36e0-a77d-2951f76ae738 | -12.65509 | -46.76917 | 2026-01-20 04:42:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4364d774-26b3-355d-9566-96c85f13ab6e | -10.94858 | -48.07727 | 2026-01-20 04:42:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8953473-fbfe-3754-bf94-8112240fd3a6 | -15.11875 | -52.95437 | 2026-01-20 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4459f3e-cd84-39a2-9795-67a1a9de90ce | -12.65784 | -46.77134 | 2026-01-20 04:42:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0e79661-8035-35c8-9505-5dc51039f0e5 | -12.65468 | -46.76597 | 2026-01-20 04:42:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87d685e1-7c56-3f2e-b32d-ab465ffc6eae | -12.66232 | -46.76715 | 2026-01-20 04:42:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21712478-84bc-34dc-ae65-52b2c59a7808 | -20.85094 | -53.74888 | 2026-01-20 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b89f157a-266c-3a1a-9e5f-ba6283d3c206 | -18.82437 | -51.61621 | 2026-01-20 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0964d193-fba5-3941-99ff-dfb2d59275fc | -20.85652 | -54.81821 | 2026-01-20 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7de02da7-e139-3eee-a7d3-a14b7581b79f | -23.80421 | -48.86852 | 2026-01-20 04:44:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eba967e2-5f32-3f69-b25a-9472d1a3349d | -20.85426 | -53.74948 | 2026-01-20 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3b539cb-3ffe-3cff-91f0-5f1f4c0135f1 | -18.81772 | -51.61509 | 2026-01-20 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c840e101-9324-3627-9a5e-bb170d87a932 | -18.81439 | -51.61452 | 2026-01-20 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86a2737a-0645-39e7-88ea-864adada0685 | -19.42813 | -57.2235 | 2026-01-20 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 89540786-428e-3edc-a159-dacebe9d6eec | -20.71141 | -48.82198 | 2026-01-20 04:44:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| fe761281-cda0-3ca1-9e61-9c7f250bb66c | -18.81495 | -51.61084 | 2026-01-20 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd4216a0-7cc6-3117-898c-0b0a8bf5b235 | -20.70765 | -48.82146 | 2026-01-20 04:44:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 3f7a816b-03bc-3fce-93ae-5a5c7b356ae0 | -23.8049 | -48.86312 | 2026-01-20 04:44:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2899cf10-f6ae-3f25-aa76-4a5602d151aa | -19.43872 | -57.23086 | 2026-01-20 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| af596f05-d529-304b-9943-d2911f4b2be4 | -21.94579 | -52.98167 | 2026-01-20 04:44:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0fd27a9-69a2-3d15-be5f-33421860a519 | -18.81828 | -51.6114 | 2026-01-20 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f9fd0aa-67b9-3db2-8206-4a12fd92675c | -19.43288 | -57.21922 | 2026-01-20 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ad0ee1b9-dff3-3f4a-a583-ce1886728cc6 | -20.85587 | -54.82211 | 2026-01-20 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd215aa5-8113-3aa3-82c2-387b077e8f51 | -21.25774 | -53.16122 | 2026-01-20 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16860d0a-64fb-30cb-9e45-5858107ab890 | -18.8216 | -51.61197 | 2026-01-20 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c87bd36-770f-30a9-8adf-918877c4a8dd | -21.94715 | -52.90634 | 2026-01-20 04:44:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0f91e2f-4130-3271-88ed-37515afb0e62 | -20.85154 | -53.74517 | 2026-01-20 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60e1cce7-be85-3a90-aed0-4844462dcecd | -19.4358 | -57.22504 | 2026-01-20 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 6b730a0a-ce93-3b9e-a299-84db9e28da33 | -18.82104 | -51.61565 | 2026-01-20 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| daa59c02-1a57-3867-a2d2-0b0904352ac8 | -19.43196 | -57.22427 | 2026-01-20 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ba2396f3-9e66-39e0-9808-12aceea1c933 | -23.77945 | -48.87603 | 2026-01-20 04:44:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88c8cc36-8a85-37b0-a03d-d3ef48c4eaac | -31.54828 | -53.73959 | 2026-01-20 04:46:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 25047eb2-d121-36d0-b899-e621c8e2c9d1 | -23.69263 | -55.26401 | 2026-01-20 04:46:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8f4d1f5b-8543-3d42-b7a8-2325ff2e3513 | -24.63296 | -50.87643 | 2026-01-20 04:46:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
