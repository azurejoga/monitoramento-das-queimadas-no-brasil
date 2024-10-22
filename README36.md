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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1139b2bb-c65c-38b8-92d1-63274a887f1b | -17.6674 | -57.4411 | 2024-10-22 14:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| e12c6785-6b9b-3483-a7a8-962294f67efe | -17.6878 | -57.3975 | 2024-10-22 14:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 5c0d04ac-5aef-30ff-8dad-fc29623f63e5 | -17.6681 | -57.3999 | 2024-10-22 14:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 78ae5b32-9540-3fe4-8942-066e5a451cdd | -3.3194 | -44.1525 | 2024-10-22 14:35:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 135.7 |
| e3355481-a137-3180-b2b7-5a2687ceb092 | -3.3195 | -44.1295 | 2024-10-22 14:35:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 0fe68ed7-4d97-3197-a48c-8c8534c1d1fd | -3.3009 | -44.1303 | 2024-10-22 14:35:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 193.7 |
| e8b20da9-e2d2-37ae-b6f8-1189bf8452f4 | -3.8934 | -44.7652 | 2024-10-22 14:35:28 | GOES-16 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0f559787-7d40-30ed-bb3c-47bd25711f7a | -4.2871 | -44.4029 | 2024-10-22 14:35:31 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 0197f04f-55ae-3d61-9528-70ad6fba3c2c | -4.9122 | -43.2103 | 2024-10-22 14:35:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| e3023ab4-9744-31ff-8159-1d37cb93ca25 | -4.9309 | -43.2091 | 2024-10-22 14:35:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9ffdd6e2-02af-309d-ba06-a45c4eabf014 | -5.2307 | -43.1652 | 2024-10-22 14:35:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| c2a24bc8-b23b-3fbd-ab8d-1229b3c5ae75 | -5.2305 | -43.1886 | 2024-10-22 14:35:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 532.9 |
| b6c2005a-0938-35d7-b8f0-c3b5a02ab111 | -5.4363 | -43.2206 | 2024-10-22 14:35:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 666243b4-0fdc-3e65-82e9-e45290dabd8a | -6.0597 | -42.7261 | 2024-10-22 14:35:40 | GOES-16 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 3f9a645e-2b19-3c65-849c-503c8f206818 | -6.06 | -42.7025 | 2024-10-22 14:35:40 | GOES-16 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 00f8d80a-3f0d-3334-bf91-cde233c77732 | -6.1843 | -43.4191 | 2024-10-22 14:35:41 | GOES-16 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ffd729b6-e85f-36bb-8f02-d853b62cf8a9 | -6.4175 | -42.6482 | 2024-10-22 14:35:42 | GOES-16 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 81ea3928-57ab-37ef-b5ff-7ae6f88de64a | -7.3711 | -44.8378 | 2024-10-22 14:35:48 | GOES-16 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| bfdc1072-a8a0-3e65-9fa3-3ef83b9c834e | -8.61 | -45.1477 | 2024-10-22 14:35:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 270.8 |
| 88482ae5-6646-31b9-93b2-9559e540f5a1 | -11.9938 | -43.0855 | 2024-10-22 14:36:13 | GOES-16 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 156.0 |
| e80d7720-e325-36d4-a1c2-f4001c1d765c | -16.8961 | -57.8378 | 2024-10-22 14:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 99389d56-284f-3edd-9f86-0277c78a1efc | -16.9714 | -56.7852 | 2024-10-22 14:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 14b3c60b-6ce2-3591-af42-9d6f597bbed5 | -17.0184 | -57.5178 | 2024-10-22 14:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 74ad88f4-96fe-3eba-b692-ec0f972a7ec6 | -16.9988 | -57.52 | 2024-10-22 14:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |


