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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3eae014-94fa-37df-abc5-a213d6290d52 | -11.7601 | -61.0743 | 2026-10-09 02:40:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d2a84bba-bf4a-36eb-af17-7c29995496e5 | -8.5183 | -67.0325 | 2026-10-09 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cb9e4037-8c89-3d91-8580-aa94b7fd2aa0 | -8.7426 | -45.1106 | 2026-10-09 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 967bd260-311e-3657-a56b-19b34a6536a0 | -6.8907 | -45.8988 | 2026-10-09 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d7267f49-dd5c-39b4-993a-9dbc41aca227 | -6.1689 | -39.4391 | 2026-10-09 02:40:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 41071343-afef-3054-b474-fe43e0231025 | -3.3455 | -50.4078 | 2026-10-09 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f4cf0794-e5fc-3b39-aa0a-141d06515b85 | -3.1284 | -54.1857 | 2026-10-09 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| bac4fa59-0ac8-3a01-ae62-f4cb184b8f13 | -3.1101 | -54.1661 | 2026-10-09 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 2f7aa29f-944c-3dc5-8c46-162a6e59d266 | -3.5677 | -54.6746 | 2026-10-09 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 80938ae9-fc65-3e5e-a27c-9ed90ee7267a | -5.6932 | -53.487 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f9a18281-1d80-3505-b7c5-2a83953e7df4 | -10.6199 | -60.4852 | 2026-10-09 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e7b3169d-6736-3662-aca6-ab1d44ff8ec6 | -3.1114 | -53.7839 | 2026-10-09 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bb2010a5-9279-354d-b32b-b6ac52047d54 | -9.4765 | -40.3613 | 2026-10-09 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.0 |
| ca24988a-8b7d-3a02-adf1-98d41645ec80 | -8.7234 | -45.1355 | 2026-10-09 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 41dc39f0-696f-38f2-87bb-58b73032c728 | -8.742 | -45.1563 | 2026-10-09 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 7414cfba-7f84-3ae2-82fa-e1720dd2dff4 | -6.0019 | -40.9837 | 2026-10-09 02:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 165.3 |
| 288ca7fb-e5dc-3ec9-bbbc-7145be42074e | -8.7423 | -45.1334 | 2026-10-09 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 278.9 |
| 085ea559-0784-3014-bb30-e49319c86482 | -7.1995 | -55.1627 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8ea3f30c-adae-3154-81cc-bb25d88b6106 | -5.7119 | -53.4658 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2e2a8d2b-abf4-37f6-b37d-363d7c6fbc16 | -2.7428 | -54.1146 | 2026-10-09 02:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 660bcea2-69f4-3bd7-a45e-9778dfa4dc83 | -7.218 | -55.1617 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 58d87763-8555-344e-a2a2-d48415babc8b | -3.5493 | -54.6752 | 2026-10-09 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bd43f17c-189d-392a-af31-37f3487913f9 | -3.11 | -54.1862 | 2026-10-09 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0d243508-71f1-3e0c-9cac-aeab8a971615 | -13.1639 | -54.3385 | 2026-10-09 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 28cc28e4-160e-3c47-8b44-7044c8f5cb39 | -6.7363 | -55.1675 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 3c215355-5a3c-324f-bc05-dca91738909b | -3.1285 | -54.1657 | 2026-10-09 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 059876ea-df8b-3c7a-ab9f-8d7a24db5f0f | -10.6012 | -60.4863 | 2026-10-09 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 3ea50db5-7002-374b-8908-821bde9d88b6 | -7.9086 | -54.7194 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a1f80ace-1d6e-3c07-8897-f406a94f8811 | -3.5493 | -54.6951 | 2026-10-09 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| f37d7a5d-9212-32c1-82d4-09482ee79bdb | -13.1636 | -54.3591 | 2026-10-09 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 77ad2478-7d2b-351c-9e1a-782fff0b6a71 | -3.1787 | -50.5807 | 2026-10-09 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 0cd97c29-1493-3741-99a0-9299f327bd28 | -13.2467 | -42.2401 | 2026-10-09 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 170.9 |
| 135173b2-6b35-350f-acfa-da37e11b0ec8 | -13.1827 | -54.3571 | 2026-10-09 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 74906e80-4d38-3e64-8cb6-334f902d9ae2 | -3.0007 | -53.9075 | 2026-10-09 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 75499605-0342-352a-a032-8d68726448bf | -6.7365 | -55.1474 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d0b522fe-45a0-3fd1-b136-7cb6a4ba788a | -8.3234 | -45.4506 | 2026-10-09 02:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 77acca10-1a07-3e0d-8aba-62f5419f347d | -13.2662 | -42.2365 | 2026-10-09 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 171.9 |
| a37ecefe-2a88-3e4c-9dcd-e13163fff752 | -3.5676 | -54.6946 | 2026-10-09 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 3e41ea09-8e50-39b2-b29b-e120879d0e54 | -5.6934 | -53.4667 | 2026-10-09 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 74a9acfa-dc5b-3f01-8be4-66592d5ab042 | -8.7231 | -45.1583 | 2026-10-09 02:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 503debae-a9d0-3aa0-935d-d7e9a4dc1a2b | -11.6562 | -43.6846 | 2026-10-09 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 06a1adf2-b1bc-3156-8c09-0cdce9655333 | -6.0021 | -40.9594 | 2026-10-09 02:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 376.1 |
| e2cf77bf-362d-3fd9-81dc-00e9a1d89cb2 | -3.1109 | -53.945 | 2026-10-09 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| dde5f0e4-ce89-3c62-ab7e-1f60bdfecb2f | -9.4574 | -40.3641 | 2026-10-09 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 150e3171-290d-3188-ab8f-182634828661 | -13.2462 | -42.2645 | 2026-10-09 02:40:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 138.8 |
| cca07d37-903a-3190-907b-48e9ddddd824 | -6.021 | -40.9577 | 2026-10-09 02:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 1a614738-f724-3a81-a939-f67a9aa0f2d4 | -6.0024 | -40.935 | 2026-10-09 02:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 46471e4b-df98-30ba-b408-84006e7b0a35 | -7.64284 | -34.99804 | 2026-10-09 02:45:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 4e119e47-acde-3e34-9362-4bc8748bd4bc | -7.64406 | -34.99162 | 2026-10-09 02:45:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1a43f4e9-90af-3d68-95f4-2e53c3d0f53b | -7.65099 | -34.99307 | 2026-10-09 02:45:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d39dd81d-b93f-384a-a613-d273616740c5 | -7.64925 | -34.99627 | 2026-10-09 02:45:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 47d06dec-5c3c-343c-9c56-f1015b894909 | -7.64925 | -34.99626 | 2026-10-09 02:45:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0d0f0969-a82c-3074-a8e1-17174eed73e1 | -7.64284 | -34.99803 | 2026-10-09 02:45:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 81ab5bc3-8dd2-37d8-a8fc-cb17c1ea5cd8 | -6.0019 | -40.9837 | 2026-10-09 02:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 133.7 |
| bcd9683b-6855-3ffa-a592-9c12b9395768 | -12.2156 | -57.1087 | 2026-10-09 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| c82e869e-0a22-3104-933d-fe8b1368255c | -6.021 | -40.9577 | 2026-10-09 02:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| ab54559a-b239-3aba-9f69-8a131d1736a4 | -4.6282 | -49.2147 | 2026-10-09 02:50:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 036f1df6-31a6-34d7-8574-3b38884f0033 | -8.7231 | -45.1583 | 2026-10-09 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e75ae858-e533-3257-8fa3-5f0c0b590759 | -12.2154 | -57.1287 | 2026-10-09 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bf930fd8-e3da-33ee-b950-f1f50d6c1c4d | -13.1636 | -54.3591 | 2026-10-09 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2dc598aa-2815-3e1f-b984-20ec1f81c1b1 | -7.2182 | -55.1416 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a076313f-417b-3142-96d8-4a5d92a5c220 | -3.3455 | -50.4078 | 2026-10-09 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 752e6e2b-2833-3b66-ae5e-f283f842ae99 | -3.0925 | -53.9455 | 2026-10-09 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d15b8b16-850b-3e07-abc1-156b5b4deaa2 | -6.7365 | -55.1474 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8eea995b-4e1a-3df1-b738-dbdca3fa88ea | -3.1114 | -53.7839 | 2026-10-09 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d5bf6b11-af04-3585-afbf-59324fc73df6 | -5.7117 | -53.4862 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 7e7db50c-a5e5-3d85-9f17-1f45139f4647 | -2.499 | -56.0675 | 2026-10-09 02:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f2af3928-f6a8-394c-8d9e-c5bc89aee0ac | -7.5649 | -61.5523 | 2026-10-09 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 8c865f4a-462f-395f-a6e2-038daf510241 | -5.6934 | -53.4667 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 87f2e44c-d13b-3260-8ea3-25fdfec6f51a | -13.1639 | -54.3385 | 2026-10-09 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c36e0bc9-2284-38d6-b6ab-7c4e24a4a8fa | -12.2535 | -57.1055 | 2026-10-09 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d78e422b-bc9a-35f0-90a2-f0cd3d53165b | -8.7423 | -45.1334 | 2026-10-09 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 6af04c1f-52da-3c52-b240-cbbb5ab7b5f2 | -8.5183 | -67.0139 | 2026-10-09 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 8024651b-f6f8-301f-951a-0116450acc02 | -7.218 | -55.1617 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e42603cd-56f0-39f7-ac7e-1ae9b99c65ae | -3.9912 | -59.356 | 2026-10-09 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b5147c9a-496c-3a46-bcb1-aa02383dfdbe | -10.6199 | -60.4852 | 2026-10-09 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 5766b2ad-dd3a-36f4-878d-bc2ddc94c4dc | -2.7428 | -54.1146 | 2026-10-09 02:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 1e082f2a-bcc9-3499-a543-2ebadd374bbc | -3.5676 | -54.6946 | 2026-10-09 02:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| f1a60f02-9285-363e-8634-de6ba376e4ce | -9.4765 | -40.3613 | 2026-10-09 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 22227e31-1fa7-30f8-bdd6-9005c5de9144 | -9.4769 | -40.3365 | 2026-10-09 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 197.7 |
| d03d4aa4-0aea-3b7f-af4f-bcf1474bf812 | -13.2462 | -42.2645 | 2026-10-09 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 330.3 |
| b1173036-845e-32bf-9543-f8a3975adf26 | -13.2657 | -42.2609 | 2026-10-09 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 179.0 |
| da0b52d3-eb2f-32c4-9618-d9c0307396a8 | -8.5183 | -67.0325 | 2026-10-09 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 9361ebdb-a92e-335e-9de7-c1ed4b7227a5 | -8.7234 | -45.1355 | 2026-10-09 02:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 5fd9cf49-b713-3ed0-9089-9b628525549b | -3.0007 | -53.9075 | 2026-10-09 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 3535abc2-5450-35f4-9e5a-06fc0ab4e826 | -7.1995 | -55.1627 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| aabc4686-0e17-3d0c-ae75-e0c7913cc8ab | -12.2348 | -57.0871 | 2026-10-09 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 910e374b-e28f-370b-bd4b-5182f1814c61 | -3.1101 | -54.1661 | 2026-10-09 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| d5236fca-55c6-3a08-b0fd-e28d66dbbbd5 | -6.0021 | -40.9594 | 2026-10-09 02:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 246.1 |
| 6b49d051-e8f2-3219-922b-6dc1377818f1 | -3.1109 | -53.945 | 2026-10-09 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d7d02730-c479-3586-a1ff-5997cf20112b | -6.0207 | -40.982 | 2026-10-09 02:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| b3664b7b-a801-3026-b9ed-21c8a20d5e4b | -3.11 | -54.1862 | 2026-10-09 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f1427016-bf8b-359b-aec6-0bd8cb45af3c | -10.6012 | -60.4863 | 2026-10-09 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| bbd80171-1be9-3754-898e-90d0ce13489e | -13.2467 | -42.2401 | 2026-10-09 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 377.3 |
| 2fbf8ecf-bab5-3642-9327-5bac0818eeeb | -3.364 | -50.4072 | 2026-10-09 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1cd47a5f-1042-3993-8411-fb7dacf09a62 | -8.537 | -66.9764 | 2026-10-09 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| cd440193-c5b5-3b6c-925e-3afd5e6f5476 | -3.1787 | -50.5807 | 2026-10-09 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e120d5e5-8d29-3ff5-9a38-05df7a838778 | -5.7119 | -53.4658 | 2026-10-09 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 217468f3-b86d-34f0-8b02-4892472ed19f | -13.2662 | -42.2365 | 2026-10-09 02:50:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 206.6 |
| 56940a4a-9bb4-3daa-b5ea-270313841e5d | -3.1284 | -54.1857 | 2026-10-09 02:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |


[Clique aqui para ver as próximas entradas](README54.md)
