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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97346111-7609-35f0-9276-aedf065bb11d | 1.16079 | -52.74105 | 2026-09-19 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55905fd8-ec9f-31f7-9c90-c96636d84c83 | -1.22361 | -55.72609 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8abf5f14-6668-3b73-9783-926fb1d41150 | -2.5371 | -49.74679 | 2026-09-19 04:55:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24128b82-9866-3132-9c79-dfad61cd1087 | 1.21966 | -51.00804 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c031475b-c64c-39c9-9ae8-0f7554f9d313 | -1.41751 | -49.42512 | 2026-09-19 04:55:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ab8d71d-5ef3-30b7-9823-3ad2b8e18af0 | -2.82054 | -50.46555 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2e017c80-fd64-3689-89a3-ceaa4aaccfd7 | -2.82185 | -51.34025 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cacf8cf2-f883-3077-afb5-f5b8d95cf1b6 | -2.81828 | -50.47993 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1aa5673f-bec6-346f-aff7-915d10964882 | -1.58811 | -54.42958 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46835004-a744-3df7-88a5-9af61bab37b2 | -1.19423 | -54.2209 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fe75b4e-7e1d-3be7-98ed-889de7acb25d | -2.8256 | -50.47739 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b7f85c4-9698-3471-999a-0bc776880047 | -1.22741 | -55.7267 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09237d35-7d1a-3ab3-a1d8-9a3850ff5ee7 | -2.82449 | -50.46247 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 3dd63bc0-9ce8-3341-ac63-fb0d8dd50b90 | 1.25247 | -50.97819 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ceb958bd-f8a4-3139-a774-825e797aca6b | 1.22188 | -51.00066 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e9901ee-364a-3477-b4ba-93e9c75bb837 | -3.16761 | -48.61129 | 2026-09-19 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c27b4a19-10a6-35c5-bd94-f143820af62f | -1.65859 | -54.91785 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd0cecad-ad81-38e1-a49d-d24034b91337 | -2.39189 | -48.52477 | 2026-09-19 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| def6db76-b85c-3af8-afc1-ba61bb12ec5a | 1.22573 | -51.00357 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d20b041-5e64-3093-9c2f-3845126cf522 | -2.39246 | -48.52207 | 2026-09-19 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5abded8d-8d3e-3d83-b203-c7cbb0226ede | -1.83443 | -54.85374 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2fbec70-4a96-3e7f-a77f-679b6d0b7d24 | -1.62091 | -48.28772 | 2026-09-19 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 113da76f-701f-3fdd-b426-1e003f3d02f3 | -1.19135 | -54.21644 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 124d89fb-a31a-33a9-9ed5-f3eca6093210 | -2.81716 | -50.46502 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52930b84-2b13-3628-bef4-1776be89ec0c | -1.17912 | -54.17496 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81b6c7b7-fe21-380d-b8a4-5e3498d3e24a | -2.39254 | -48.52051 | 2026-09-19 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0019def-0d85-358c-b901-73b035e4453c | 1.22242 | -51.00409 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe7ed760-2778-3cce-bcbc-3cfce1718edc | -3.23009 | -48.86181 | 2026-09-19 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d86b8d80-009b-3ef3-8e9d-aa4b81ca07ec | -1.57786 | -54.44823 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 345f3856-8cab-3314-b93b-65b18290b114 | -3.24097 | -46.95101 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 60f68974-cd0d-30c9-8b17-ded8f45ec00a | -2.83125 | -50.46352 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 7685475b-8fc6-34f1-a872-76a782fecf5d | 2.32083 | -60.91958 | 2026-09-19 04:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa945ca7-9afc-3ebb-a492-d69e160d53de | 1.00159 | -60.41912 | 2026-09-19 04:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ded06fcf-4fab-3673-9a5a-804ac0f86ac0 | -1.22124 | -54.09725 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba1428cc-b895-380c-98fc-715f0614162f | -1.19486 | -54.21699 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46124961-7b38-38f5-98f0-ef5472ab9f20 | 3.13524 | -60.15667 | 2026-09-19 04:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c88f16d-a21c-312e-980f-eea49024252f | -1.21179 | -54.22364 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24b5bf05-2537-320f-b93a-c4db4ebc0efc | -2.29196 | -47.88408 | 2026-09-19 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e2c1eac-491f-3817-ad20-31fe9c68d955 | -2.82335 | -50.46968 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7876e27-5aab-3030-8fec-a1e06b75b197 | -2.80287 | -52.08175 | 2026-09-19 04:55:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1b4ce27-372f-3053-be33-ff5d388fd532 | -2.02753 | -48.78102 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 837f18d8-0d2d-3fc4-b0f8-2fa208923cdd | 1.25632 | -50.98111 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f3fb43c3-8c98-387c-9d75-88d69a5f5aa0 | -1.19774 | -54.22145 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fb047cc-ff1a-3016-a7c1-ba29d5f26113 | -1.21531 | -54.22419 | 2026-09-19 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a4cedb3-7b56-35e9-8978-8e8ab642b7a9 | -2.02609 | -48.77755 | 2026-09-19 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11464206-4880-3317-a8ca-3c55037e7204 | -3.23635 | -46.95402 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17d839fe-d67e-3b3e-9074-c4d57ea4496f | -1.59168 | -55.55333 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2b25675-6268-39bb-a9a4-e8bfb7ba2962 | -0.75556 | -48.70527 | 2026-09-19 04:55:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae6c129e-a9e6-375d-92db-dc8aabb60466 | 1.21636 | -51.00856 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d47a1ad2-59b3-34af-880e-df900a91fca7 | -2.82392 | -50.46608 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| a98287fe-9cc1-3e4e-bbf1-e9ea930405b4 | 1.28188 | -50.86455 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0467dda7-8eb4-3a0c-8a9f-4ecad6a618f3 | -2.39178 | -48.52632 | 2026-09-19 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 110a0c4a-3782-3137-b1c8-38a2730d15ff | -3.23284 | -46.94977 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 59239190-d3ec-3a7c-a3d9-6affd2b7f85f | 0.79309 | -59.20504 | 2026-09-19 04:55:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a53c112d-ac6a-32bd-b445-95734a61737c | -1.60971 | -55.56076 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1499516f-18c7-328c-bf3b-2547273564c0 | 1.22134 | -50.99723 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35bf7ec6-9dac-370d-987c-6bd6ec696e4a | -1.83376 | -54.85785 | 2026-09-19 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb1020ad-59ce-3f85-b324-29b918171629 | -3.28658 | -44.6867 | 2026-09-19 04:55:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66979605-6b6f-36c2-81dc-72d757b79417 | -3.23746 | -46.94677 | 2026-09-19 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24cd343-2712-382a-bbf7-10ccdae8b80c | -1.59989 | -55.54994 | 2026-09-19 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2715f320-fec0-375b-b0b0-db1bcb64d3f3 | -2.82844 | -50.4594 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 37f20a08-aed9-3768-a7ed-b731129531e2 | -2.82787 | -50.463 | 2026-09-19 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f15f80c7-748e-37dd-8453-3eccd2135de9 | 1.22464 | -50.99671 | 2026-09-19 04:55:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6be316e1-5c0b-35bc-8f1e-994ef9288a7d | -7.28729 | -44.5264 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2da18b05-c90d-3fab-b06a-834c31563ce8 | -6.57269 | -44.16316 | 2026-09-19 04:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b6b8fa1d-b376-3043-894a-3e51a98ede48 | -6.44048 | -44.94598 | 2026-09-19 04:57:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b04e936f-24af-3dca-a5a6-2d675f66751d | -7.77665 | -44.89169 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fc7b7f9-2029-3ef8-900e-6b63aa5a04a3 | -10.32827 | -50.40425 | 2026-09-19 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a046fb1-4561-3d57-a020-fd864c86a05d | -11.11875 | -45.28846 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3131e916-96b8-3b63-a1ac-02775d4c9564 | -7.86051 | -44.87695 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d083188f-7450-3bb5-9946-a9e5fbbd735b | -4.50004 | -54.97004 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2f5188f1-163e-37fd-81f8-98fe15e205da | -3.01085 | -51.39081 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c817bde-1b12-3075-bd17-22f65e435d37 | -6.99412 | -42.17964 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 775c7235-64bb-37ad-b922-37ddf6b03ba7 | -4.4322 | -55.07675 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd84ef40-ccb5-3ecb-9d06-65fa6a8162cc | -7.76346 | -46.76073 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e7164d1-418e-36a0-a684-ff309684c7c8 | -4.49216 | -55.48877 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f54afb5-5d7e-3bfc-b8c2-31da75e0456f | -7.64452 | -46.10709 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0fd6dfb8-63a5-3570-b56d-cf00513f00f2 | -9.93818 | -45.31664 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce693ca0-10a7-36dc-8972-e2ff77855161 | -3.36649 | -50.44909 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bea8659c-bcb3-33f7-8d9e-532af56ef5fd | -9.72919 | -47.13907 | 2026-09-19 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6092bf2d-2c0a-3192-803e-4c8e8f330d0a | -6.25736 | -55.43933 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fae4d78-7fb0-3229-beab-f87826f68de4 | -3.3631 | -50.44856 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c58334c8-56fd-382b-a794-1a7e5500ba05 | -9.74543 | -46.09025 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7d76ba5-f9f6-3606-a99a-fcfdf726b350 | -8.27051 | -62.74275 | 2026-09-19 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae2b6f93-cae1-39f1-b09d-a0cb748e508c | -3.76055 | -51.1356 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0981dc8f-d89b-337e-8b3e-4980787a1c97 | -7.58518 | -43.45001 | 2026-09-19 04:57:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31926db0-d461-34f5-a23c-eb33d75dedb3 | -6.77539 | -47.86556 | 2026-09-19 04:57:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0be1333-4022-3899-9433-d53c5190defa | -8.29282 | -46.85534 | 2026-09-19 04:57:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1274512-df20-399d-abee-8f1a05633b82 | -11.07613 | -48.31347 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e48b7ff9-7cdd-394a-86ed-b6b3a5b45386 | -11.08276 | -48.28693 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92244f26-1033-3623-ab9c-508e6ef237bd | -10.40132 | -48.31937 | 2026-09-19 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4db3da7a-7d2e-32cc-b427-36f336c67014 | -8.38805 | -45.63868 | 2026-09-19 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77eafe70-8b5f-31e9-9143-1ab9e5a899f5 | -5.55761 | -48.44289 | 2026-09-19 04:57:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ff8b404-e4e9-3a0d-8eb9-e08569ea1742 | -10.37526 | -50.46633 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 924f9923-3118-3213-b9e5-7e1a36e6c355 | -9.66379 | -54.31439 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb31f4f-c73b-31e6-b556-c3c7d269a1d7 | -7.86632 | -45.13298 | 2026-09-19 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc4cd944-adcf-395b-a86a-5fc91660311c | -3.72898 | -49.04013 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7ae5466-4cb1-3ac3-bb0e-837db3b525aa | -8.327 | -50.85952 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03187a83-d679-344c-a3c2-c81bcc6919cf | -8.66432 | -45.4457 | 2026-09-19 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1c6d0e3-2f4c-3275-af3c-f7100d87888c | -5.87757 | -53.62143 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README71.md)
