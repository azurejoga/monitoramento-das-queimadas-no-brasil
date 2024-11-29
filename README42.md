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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afcb6d14-b1fb-32b9-a914-47b43d8460ed | -3.9399 | -49.91058 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 915a1769-125b-3812-bc51-f3ac1d1dc6b9 | -3.05713 | -54.04306 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 144a5687-34b1-396e-b98b-bbb7e092413e | -1.7813 | -52.73768 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd5b8cac-59c7-3dea-a976-c13018657a89 | -3.22366 | -54.17536 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0b982d84-6d20-320f-8aff-c5aeacc735dd | -2.99104 | -53.35744 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c7f9f8f-3600-3726-9dcc-0857f34b604b | -3.153 | -49.43355 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a79a922d-4905-333b-b965-62575f557332 | -3.33398 | -46.69702 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ba6df4ce-9699-3561-a770-5f1bea1e31e7 | -2.20817 | -50.82727 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e669f92c-7cf8-392f-a772-582db9e8e15a | -3.0568 | -53.28297 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aee20d24-e6fb-3b5c-871e-25528d37ff59 | -0.91063 | -51.64439 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60edeb3f-3ee7-31b5-a753-9c7282d45069 | -2.82783 | -54.09567 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd5acf97-1ea7-3694-80b3-a1687f7d28e7 | -2.61324 | -46.55962 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37c32740-d7cd-3163-94e9-403ffcb3f567 | -2.76196 | -49.87878 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e11b8d85-d313-38c0-882c-9cd45dff8ac5 | -1.20478 | -51.78498 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eefbd5a4-3828-313c-b937-a27448f6916a | -2.59191 | -53.97383 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcb6f5d3-9328-3344-9a21-1eaa6ae90d3f | -0.77753 | -52.39018 | 2024-11-29 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d98145c8-bcf7-30e5-9c34-370649ee1fa4 | -1.09928 | -52.35458 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1dac764-8800-341e-bb30-7e620014e3c3 | -5.75995 | -43.39694 | 2024-11-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbd6609b-8e50-3824-8429-5b6afdebcf7b | -2.8386 | -54.0268 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e60457a-0f97-38b3-9760-093863fee5a2 | -1.14485 | -48.34227 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a47c4f80-c4e2-3b8b-b854-e379c177dfa7 | -1.35724 | -52.53304 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c7647a-f529-3eef-9582-a4f25bdc59ee | -3.57839 | -50.33585 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e0dd01b-500b-3702-957d-024af53a61eb | -3.11818 | -53.76045 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7115a024-23aa-3519-b50b-b8e781417b6f | -2.94372 | -51.40986 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e9f13d4-bd2d-3339-9127-62a806f68dbf | -1.49452 | -52.43706 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 200039d2-7393-35ba-979c-9f7032428ee8 | 0.81087 | -51.88685 | 2024-11-29 04:57:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff633902-3c6e-3ff6-b798-8aaba48de6ff | -3.08763 | -53.28065 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40cd6653-762e-3371-bad2-d624c6d0396c | -4.17489 | -48.61681 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ed0a32c-d878-3f0e-8973-f7e705312f3b | -1.60174 | -52.29594 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| fb63548a-1f30-3fec-9a54-4388158b1465 | -1.37465 | -53.62085 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e1448ff-4190-3292-a4cc-fe685a1954cf | -1.72537 | -52.48373 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffd6732a-9761-324a-867c-64256d6c86a5 | -2.80183 | -54.06696 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4b44bb7-48f8-3135-92fd-8a9073788254 | -2.66274 | -48.78279 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 78b5837d-2762-31d9-bb45-b24493484ddf | -3.76807 | -51.61263 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e4c46726-7d1f-3b5c-9d9d-300db1fdeb1d | -2.40505 | -51.98586 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 312b7b19-8fdc-36d1-84fa-f9985c62ed79 | -1.15612 | -53.58284 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc470cb8-74c9-317a-83f8-09639486578f | -1.95994 | -46.44464 | 2024-11-29 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e1b58a73-f890-3e41-8771-2a529462395a | -3.50291 | -53.82487 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7528b898-1b0e-3731-af3d-1816db536e51 | -4.18157 | -46.8396 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52ec746d-344c-38ac-a6f6-d6e2d990dd64 | -3.49238 | -53.80566 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf648b49-ca09-3352-b685-5be725a61229 | -2.79323 | -52.98719 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63546098-8805-314f-9f90-16fd8d6f455e | -1.69958 | -52.45418 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| de30eeb9-db7e-3ae7-b853-2ac25b74991b | -4.30466 | -48.23359 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daa4a63e-5db7-3f35-a669-5cceb1282c17 | -2.0062 | -51.16656 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20a711f4-7779-3c15-9ea5-8508ff40a31a | -3.2994 | -53.6907 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7f4d6f3-ca1b-335a-8e71-1af2ef931f20 | -3.97869 | -46.74286 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c75e813e-55d1-3445-81ec-b819eb3e6770 | -3.23866 | -53.03148 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b973867e-92fc-3d9a-bf0b-5e3f4877ddbf | -1.65878 | -53.8063 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 372198fb-446d-3c16-b8c4-ec603bc68260 | -3.22989 | -53.6341 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d260298-53bb-331f-9bc5-61df3307a2e3 | -2.45712 | -53.68144 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f24eb2d5-210f-3e7e-b213-27600392cafa | -1.49398 | -52.44054 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e93a0d20-9819-33be-a3cc-3aa338a92fe5 | -2.83838 | -54.11496 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39e299e2-4b59-3e21-94f6-be13d0728a78 | -2.34813 | -53.92133 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcd04caf-5c0a-3640-b43f-b5048363013b | -1.03921 | -52.1729 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be4b6f15-97f9-3a98-b451-c1558c81852c | -2.04275 | -54.67625 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f01a2d1a-d1e5-33d8-b696-1e9e6808531a | -1.11708 | -53.59445 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9c6e371-2303-30bb-8f95-557221592252 | -3.50101 | -50.49978 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c03b07c-f114-346d-9162-ab42f9f8fdae | -0.78573 | -52.66406 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33fabf81-35b8-365e-8480-261feac7675e | 0.98243 | -50.2524 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d62ff7f6-058a-3c24-af3f-edb302058ad4 | -1.14793 | -48.33513 | 2024-11-29 04:57:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82adc8df-34cc-3605-832a-bed2a330196a | -1.11406 | -52.30326 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29390d88-9928-33dc-b69f-abb4a975c028 | -1.08158 | -53.38514 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cd433419-b76a-3f7c-beb5-373083cdd2ae | -4.48243 | -48.11331 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ade52f00-500b-3e16-bbca-dab0736e47db | -4.19566 | -50.68544 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bc316f77-990e-399c-b967-06265dc53cee | -2.85426 | -53.94824 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba46177-c2c3-3cbd-8459-76e8a41b2b98 | -2.63137 | -54.06813 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd2f8b12-2e05-3ae4-8a58-bc4482617dd1 | -0.95793 | -51.65167 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17b16b5e-7189-3d5b-b7fc-79676159377b | -2.16067 | -54.48899 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cd45e5e-2827-3e00-aace-7e22f7acd6f0 | -3.05219 | -48.523 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4794729b-5103-3ada-abd9-c37add0a7f67 | -2.08553 | -49.939 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93102544-4633-36a0-8d8b-b2675205b536 | -3.58552 | -50.51106 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 191b05d2-ce06-3e52-9ed6-8c9ddd22292e | -4.16108 | -53.48752 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ff71f85-8e51-3c72-9cea-89209bd6b4f3 | -1.3032 | -55.7448 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e04611b4-2d0a-3c0a-8ed5-a02ffdd47acd | -3.31869 | -53.69719 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e098f824-c2b5-3259-adfc-966fa713623f | -3.50468 | -50.30442 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 308fb4e8-4547-3c8e-a75d-3cda42b2895c | -3.30271 | -53.69121 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a881cd3e-c0f8-32f6-a52f-82f93608686f | -3.55792 | -51.49641 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a271209-61be-3af2-a7ef-c5d6cadacb1f | -1.43764 | -54.5235 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7997b97-46a3-3850-b70a-878a01f5317e | -3.23274 | -54.09566 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d74e8550-0f40-302a-9dfd-b54f6322fd7d | -2.59137 | -53.97728 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c21a7e7f-bb00-35b2-8312-1c8ed277fb99 | -3.15414 | -50.58782 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5693f0e9-3014-3d59-966f-0f9477074b82 | -2.33825 | -46.86918 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 14166fab-3d5c-3f4b-8dad-023d5341a1bb | -2.69332 | -51.98527 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eb5c9e6-289a-3b4b-8429-518e3f7b8c91 | -1.58669 | -52.28284 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 211b71a8-4973-35a4-8f19-4978879a6a19 | -2.48995 | -49.04746 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77398126-6bb8-340a-91ba-22ca553ae4ec | -3.35294 | -51.64402 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c898e29-59ed-3365-bf43-4ed3e6968ffb | -2.59083 | -53.98072 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30a98089-166f-322e-a68f-b49e2ead226e | -2.96327 | -51.00553 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7098e1c2-4e10-3824-9d6f-473838a39a3c | -2.70463 | -52.00183 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bd59741-7f22-3327-83bb-2d5363ac2025 | -3.30542 | -50.75552 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d4d80cf2-0485-37c7-acd2-db957da3593e | -2.75642 | -54.07329 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a450395f-8022-398f-8b6a-4712e1541637 | -2.22849 | -53.62141 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8c73322-5641-3a23-aa79-4e875c513103 | -3.077 | -53.91589 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 347bfaa3-3d89-3269-904e-8809403b4b9e | -1.4177 | -55.2556 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5dbcf99-9ed6-31a4-95e1-11c9b281b8fd | -2.86978 | -45.53655 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b7bc3ed-0a62-32e1-b8ae-f4ae3f5c5350 | -1.13736 | -51.67484 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a04bf01-5834-3346-91fe-eb2bf753de9d | -1.21487 | -53.55744 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d3598446-6e5e-3e1f-9882-f559792fa572 | -3.84421 | -52.39307 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 989db3b7-3217-3dd6-9716-84def30a6d72 | -1.97996 | -52.07532 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8a398ce-b68a-3473-8862-3cb6fd40a7bc | -0.98433 | -53.6829 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README43.md)
