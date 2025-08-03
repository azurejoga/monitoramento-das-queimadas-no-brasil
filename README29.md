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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e283aab6-debc-369f-9093-adde493f3798 | -6.82871 | -59.26033 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a21fd670-3fb7-3d4a-b60c-fb1fe3a6ca4f | -6.67105 | -59.16066 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65c2e255-cc01-3303-8abc-fbdec312a266 | -2.90956 | -54.15929 | 2025-08-03 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1e7cd0c0-cc06-3368-8466-a239acf1e52d | -6.82046 | -59.26966 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62e42041-702a-3641-8ff9-17b087adefde | -7.51928 | -61.3244 | 2025-08-03 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9f4dfd6-60f6-35f6-a59c-15589954bdc6 | -6.6248 | -59.96841 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c7c4cb3e-2be7-3667-832a-24ef16864b14 | -6.82431 | -59.26672 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30001045-bc21-377e-b686-2415bfecad0f | -6.63479 | -59.94844 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbae910f-1b5d-35a4-aae7-7b092da8e262 | -6.62092 | -59.97136 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f030568b-12b5-37dc-abad-dbf64ca63529 | -6.82762 | -59.26725 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77f2b9fd-c0ff-32fd-8bf4-ff92131b9401 | -6.61759 | -59.97084 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a46db264-d574-3221-9e29-baa9dbd0f937 | -8.33662 | -46.91227 | 2025-08-03 05:16:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffaa771a-8ba4-3e61-9edb-f64e6f021591 | -6.17327 | -58.06828 | 2025-08-03 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fd53b99-36e9-3fc7-9894-2549409508ae | -6.82817 | -59.26379 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e0f0386-95cc-36d3-84b1-5d8feb7c7ca8 | -6.6187 | -59.96383 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58b9ca25-698d-3595-b9e9-4e541619b5bb | -2.90737 | -52.55007 | 2025-08-03 05:16:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cd321c1-6751-3be0-aa06-13a4ee4c5a6a | -6.1766 | -58.06879 | 2025-08-03 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76f4e6ac-c40c-37a5-a4a7-97daa37baac2 | -7.88377 | -45.52414 | 2025-08-03 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9a882d6-99c3-3cad-91e6-7a6062a5b831 | -6.61926 | -59.96032 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4938094c-dbea-3c23-af7c-bfbb264651b4 | -6.73255 | -59.18134 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50ed770d-4f48-3b83-9de6-5ff8dcfff580 | -6.61261 | -59.95928 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09dd881a-f7b1-3d4c-8eac-3a38824cffc7 | -6.6782 | -59.15825 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d17fae78-56a4-347f-b6fd-9d098b5ba94d | -6.67602 | -59.17207 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51fe43dd-01f7-3d32-a1cd-573e0d4496d7 | -6.81992 | -59.27311 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d82dae08-eb9d-3fe9-8a7e-a5ad35683619 | -6.62147 | -59.96786 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 70de8df4-82b1-3c45-99ae-2c7f29adfb18 | -6.62647 | -59.95788 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 79f7b369-37f6-3d69-831b-99c989c17f1d | -6.67435 | -59.16119 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d1b3bc76-91a5-3867-a282-938279160361 | -6.72979 | -59.17737 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b42eec99-c8de-3dd4-8c13-ec8c17880328 | -6.67766 | -59.16171 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3a40f06-5c2f-3a2f-9c6c-13094efa9641 | -8.11379 | -49.75782 | 2025-08-03 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e45ecb5-deb3-3932-b91d-03cc34c45f9a | -6.62536 | -59.96489 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a40b0ba3-17fa-328d-87aa-785e4b32d43b | -6.68757 | -59.16327 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b731c15-c394-30d2-a20a-9af4900d2b38 | -6.67381 | -59.16463 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64cfde60-ec43-3986-9044-db03bcea39b0 | -7.8805 | -45.52773 | 2025-08-03 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1815e68f-3a06-36f8-bb67-319bbb9311a6 | -6.68427 | -59.16275 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8888b08d-c2c5-3ced-8dfd-4c4bb2683257 | -6.61426 | -59.97032 | 2025-08-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bcffe8c-2915-37c8-b8b2-2c128cb6692b | -7.88671 | -45.53601 | 2025-08-03 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 281684c5-484f-3228-8034-d985ffcea986 | -7.59855 | -55.20625 | 2025-08-03 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a914629-fac7-3c20-9871-908cb3410d66 | -6.72924 | -59.18082 | 2025-08-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 415badd0-9018-3459-a41f-6a93569924a5 | -4.77393 | -45.33684 | 2025-08-03 05:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f49f053d-3de0-34b1-a873-a6f2f28b7bde | -12.40717 | -47.07422 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 877775af-32a6-3905-8898-6fc8ef024db9 | -10.78715 | -48.80847 | 2025-08-03 05:18:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4c384e0-db1a-39e9-af15-db0e8e32de95 | -10.78671 | -48.8121 | 2025-08-03 05:18:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e63f469-860f-3136-a0a6-62e97817246f | -14.3726 | -50.32867 | 2025-08-03 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5eba898d-237e-303b-9f8b-942419bbaca2 | -12.75369 | -56.57468 | 2025-08-03 05:18:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81b9039e-185d-37e8-a8ab-028d996cde0c | -10.78758 | -48.80492 | 2025-08-03 05:18:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2439dad3-415f-37b7-98df-4a7df7114105 | -14.1035 | -54.00573 | 2025-08-03 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33f8a948-7d82-3f80-9b58-fd7a27ce1215 | -14.37792 | -50.32995 | 2025-08-03 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 79538f7f-c989-3467-9115-fbde8475d1b8 | -12.43156 | -47.04254 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 936e773c-5906-374e-bd40-48a7c5526dc0 | -15.54832 | -54.27433 | 2025-08-03 05:18:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3cdbdc5-a430-382b-befc-0eea3d512d14 | -12.68618 | -48.09452 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2d3aaec5-99d2-32bd-bd79-16d23ba277e3 | -13.06842 | -47.42982 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2e4eead-1be6-3657-8d3b-3dde262aec8a | -13.0671 | -47.44208 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b66b222f-5dc9-34cf-9c06-8edca620f577 | -14.3784 | -50.32937 | 2025-08-03 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff96a257-2208-372d-a65d-c78c67e7ca5e | -11.21297 | -51.53813 | 2025-08-03 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1074a393-8f30-378e-b082-ab523578821b | -15.54379 | -54.27372 | 2025-08-03 05:18:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07c6631d-48fc-358e-97c5-bc856e4c93d7 | -12.76122 | -56.57576 | 2025-08-03 05:18:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b71dc4cd-3114-3f4d-ae43-cb3d9c1dbb08 | -11.74423 | -54.7262 | 2025-08-03 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d67afeda-e43b-352e-b1e8-7098b1dbd06b | -12.40714 | -47.0728 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4081de6c-3cb2-30cb-8325-8b5bc930b45d | -15.59531 | -48.50906 | 2025-08-03 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4aada1c5-9fa6-34b3-90fe-64d71c51da15 | -14.00184 | -53.92719 | 2025-08-03 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8737a3db-06a0-3172-b170-8083eadf872f | -12.4141 | -47.07487 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 547a5659-e737-351c-8df4-bd851fd6a86f | -11.05092 | -49.54656 | 2025-08-03 05:18:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f674c7c-e3c1-32a6-b410-0111fb63a08f | -14.37839 | -50.3259 | 2025-08-03 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12a6faba-a381-3430-ab58-5ecd8dca5143 | -13.06903 | -47.42418 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6f273b6-9995-3d07-9a04-32bd35723a0d | -12.48775 | -47.16832 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c03c5f50-0713-364d-9578-e2bcb9b4b757 | -12.68569 | -48.09882 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5d0a9ec9-4ac5-34b7-b16b-81c5d3728e77 | -12.03504 | -54.2387 | 2025-08-03 05:18:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1016129-2f13-381b-b57c-f50ff6a9abd9 | -12.48847 | -47.16181 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9301fb7-ee95-3884-b1e7-8c101d3662db | -11.21337 | -51.53505 | 2025-08-03 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99a65f44-3951-3102-9fb5-bd951f7b131d | -12.03073 | -54.2381 | 2025-08-03 05:18:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d8e8c96-75c4-3e2c-94fb-7c2e4b8f4bc6 | -16.72052 | -49.42847 | 2025-08-03 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3fb6a354-79c0-3d27-b4d7-1d026952e4ee | -14.00637 | -53.92785 | 2025-08-03 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07438596-bfc7-3772-bba1-171c71e86d65 | -14.37304 | -50.32461 | 2025-08-03 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1aa7b053-31c3-3f9d-8437-b6a148c3ab58 | -14.37212 | -50.32927 | 2025-08-03 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b0354b9-cd27-34af-bebc-9b00e23087a6 | -14.37259 | -50.32521 | 2025-08-03 05:18:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2ba7ba7-df42-37ac-b935-fc46a9d8c99b | -12.41407 | -47.07341 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0288f5d-9b2d-344a-ba1a-88474e8466a8 | -16.72683 | -49.42915 | 2025-08-03 05:18:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44f165a5-9ff4-3df8-a017-9f237c504b26 | -11.20824 | -51.53433 | 2025-08-03 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8676b2a6-be6d-34f2-8233-39b3f5cc842a | -12.75746 | -56.57522 | 2025-08-03 05:18:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bab6f8f-9683-39a2-8c3b-d994763d1677 | -12.68524 | -48.10291 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40308369-572e-382c-8784-ed4b5f524e42 | -11.74839 | -54.72678 | 2025-08-03 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 255f3f5c-f682-327a-8ce1-d4dc44113ce2 | -15.55285 | -54.27496 | 2025-08-03 05:18:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 045de40a-e1d0-36d0-b837-5a91e4d35c62 | -13.0791 | -47.39493 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7bef22a2-07eb-3577-8af4-ded213ad0e6d | -12.43231 | -47.03598 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32e279f4-f75d-3f17-9e4d-23edffdbe1de | -15.54773 | -54.27909 | 2025-08-03 05:18:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d99c6a9f-1e95-3e74-b28f-93d416bf0338 | -12.43208 | -47.03746 | 2025-08-03 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 827dcf13-e737-358d-a035-fae1d39b0732 | -13.06777 | -47.43591 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54a9a5da-b976-366c-8166-09adb00a340b | -16.72105 | -49.42306 | 2025-08-03 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| be7ffcc1-3654-3511-b3b7-ad0f5c41183d | -12.68673 | -48.08961 | 2025-08-03 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a938cdb9-2b5f-3083-9d98-db038f4730a1 | -11.40916 | -54.71849 | 2025-08-03 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b9a947d-682a-36ff-b8ea-15de09e3b629 | -8.0132 | -43.1278 | 2025-08-03 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| db5b7098-d675-335a-af5a-51062a628326 | -7.994 | -43.1534 | 2025-08-03 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 4290de33-d821-3923-a9a1-8c8062aa3abb | -8.0129 | -43.1513 | 2025-08-03 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 268.2 |
| 6da148bf-cadd-3247-8b69-4a592c43ecb9 | -4.5497 | -44.2047 | 2025-08-03 05:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b660d9bd-08cc-307e-8a5c-608840aa98f5 | -6.6329 | -59.9649 | 2025-08-03 05:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ba134117-3505-3912-8169-90cb469ce2f7 | -8.0126 | -43.1749 | 2025-08-03 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 195.5 |
| 89cced57-b854-308b-8ed9-83bf4b06473c | -7.9937 | -43.1769 | 2025-08-03 05:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| e073da8b-c72c-3df7-9ba3-d19479c115e4 | -18.54338 | -48.90604 | 2025-08-03 05:21:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e838d1d-18c4-3e96-8e68-d9835ed429c5 | -23.83494 | -52.95785 | 2025-08-03 05:21:00 | NOAA-20 | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
