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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00789e5e-951e-3261-98b4-ca190480d5d4 | -21.25196 | -48.65923 | 2026-01-07 04:38:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 942a7a62-7968-3600-bff1-c4f3905b38e1 | -24.55599 | -51.95582 | 2026-01-07 04:38:00 | NOAA-20 | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f66860cc-10aa-3074-a089-2b2149c130c8 | -20.52716 | -57.98449 | 2026-01-07 04:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 79f84192-189b-3d4f-93ce-312a95c92e34 | -20.80839 | -49.81622 | 2026-01-07 04:38:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 781153b9-61a1-3e71-814d-c5cbbeafa9a2 | -22.49481 | -46.93882 | 2026-01-07 04:38:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0875567d-ed6c-3ee8-a1ef-dc340aa6bdd6 | -20.81178 | -49.81678 | 2026-01-07 04:38:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c2341b03-c801-3754-877c-fdbcdf05f265 | -22.49444 | -46.9431 | 2026-01-07 04:38:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef9fbe3a-ec7b-38a4-afbc-d85919027f7b | -24.09516 | -50.1331 | 2026-01-07 04:38:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 737b64de-57fc-3213-9067-2e72d776339b | -23.87083 | -49.74413 | 2026-01-07 04:38:00 | NOAA-20 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0c4c5eab-8c88-3c08-b29e-42e2a6931e58 | -22.49874 | -46.93935 | 2026-01-07 04:38:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b62efb75-d566-302c-8ad5-93e43c6e72fe | -26.88526 | -52.40604 | 2026-01-07 04:40:00 | NOAA-20 | XANXERÊ | SANTA CATARINA | Brasil | 4219507 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea711cae-cf70-3d5c-bc66-dae4f38a9e69 | -26.90037 | -49.05717 | 2026-01-07 04:40:00 | NOAA-20 | BLUMENAU | SANTA CATARINA | Brasil | 4202404 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 71fcd109-cd4f-3890-ad67-f3fea742872f | -25.94851 | -53.79742 | 2026-01-07 04:40:00 | NOAA-20 | PRANCHITA | PARANÁ | Brasil | 4120358 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 307beb60-58cf-3ab2-a070-1257ece58bb9 | -29.88455 | -51.21452 | 2026-01-07 04:40:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 75e9cd76-ff6d-3218-be5f-31b0035f3a80 | -27.44783 | -48.4442 | 2026-01-07 04:40:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6924e5fb-e9d4-3316-b985-65a90b1579f9 | -27.01741 | -51.50823 | 2026-01-07 04:40:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fcb67302-6f4b-3781-bea1-17fc9bbd4f7b | -27.42322 | -52.50494 | 2026-01-07 04:40:00 | NOAA-20 | ITATIBA DO SUL | RIO GRANDE DO SUL | Brasil | 4310702 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 323b711b-673b-3aad-9e0f-d5d014c10f16 | -27.45659 | -48.45299 | 2026-01-07 04:40:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6347f22b-d82d-3ea3-b435-4f7fac4412c3 | -30.45681 | -56.38736 | 2026-01-07 04:40:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| bdca18bb-48a0-33b0-a010-c44584fd792e | -27.44717 | -48.44944 | 2026-01-07 04:40:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 037e2b7a-3fd1-32c8-805c-9f69c0154bd4 | -27.42382 | -52.50106 | 2026-01-07 04:40:00 | NOAA-20 | ITATIBA DO SUL | RIO GRANDE DO SUL | Brasil | 4310702 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73d43207-778e-322e-9dde-740960c0779f | -29.71416 | -56.00071 | 2026-01-07 04:40:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| d69d9c3f-9df6-3797-a1ec-dc977c419b42 | -25.94452 | -53.80064 | 2026-01-07 04:40:00 | NOAA-20 | PRANCHITA | PARANÁ | Brasil | 4120358 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 7bf847f6-d597-30fd-9077-28efc3ba1dc9 | -27.68539 | -48.75226 | 2026-01-07 04:40:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bd1055da-0f6e-36ad-8f2f-7f45a717ec85 | -33.58411 | -53.47014 | 2026-01-07 04:42:00 | NOAA-20 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 72ea1633-c9ac-3c3e-811b-6713f77eabd2 | -20.5283 | -57.983 | 2026-01-07 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.4 |
| e1d5e14a-5821-381e-b20d-2ce8203474ee | -2.79386 | -52.6812 | 2026-01-07 05:22:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 56ecddfe-4a84-3907-b436-dfd4f42602e7 | -1.25958 | -53.48819 | 2026-01-07 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee4fd9ad-59a7-352e-97c5-15c119fb419b | -7.77357 | -61.45203 | 2026-01-07 05:22:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c77a3f98-9f2b-396a-a19f-4f59eb950144 | -2.91355 | -54.14527 | 2026-01-07 05:22:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f5fc0df-8029-3c48-b7fb-fb5294ea0436 | -1.63073 | -55.38046 | 2026-01-07 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f65e51c-a27f-3e0d-b58a-b9b61aa86fe0 | -1.30574 | -54.1502 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b726dedf-ffd9-3235-b2f5-1c3dafcf325f | -2.69618 | -48.99086 | 2026-01-07 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4e49404-388e-3bd4-aa96-ce2036790120 | 3.93759 | -60.60419 | 2026-01-07 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e66aff7-22d5-39a2-ad50-346147072470 | -3.4246 | -53.41581 | 2026-01-07 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80616fd8-dbe9-33d7-a8e4-91c391daea4c | -2.73449 | -54.94191 | 2026-01-07 05:22:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 541f735e-a600-30ac-ab86-507707731b21 | -2.16856 | -53.66765 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd012ab2-8a70-35e1-a6e5-751c2bfb6658 | -2.69021 | -48.98992 | 2026-01-07 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 230ec88b-2e6c-3e00-ab0d-7de47f255db0 | -2.16097 | -51.99299 | 2026-01-07 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 01981659-5056-3c66-befa-5b20e8b32169 | -2.27474 | -53.78465 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5a41397-5e67-30d5-887d-0c65ede030f3 | -2.79457 | -52.67636 | 2026-01-07 05:22:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dc9a600d-9c71-36df-a19e-680070532b19 | 4.2681 | -60.65571 | 2026-01-07 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff922add-ec6b-33cf-9a17-cfa07d10de95 | -2.16257 | -51.9823 | 2026-01-07 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94ba6866-7341-3052-b07d-462e2b94ecd6 | -2.15772 | -51.98154 | 2026-01-07 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62b891e0-ad61-3f96-8690-f57865d30c49 | -2.36852 | -51.74236 | 2026-01-07 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66045838-737c-3744-a2c8-af058b29d47d | -2.74754 | -54.93687 | 2026-01-07 05:22:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f6de573-a140-33af-b1f4-1bbe6e215401 | -2.70217 | -48.99166 | 2026-01-07 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb8df1df-fa2e-3b44-83f0-9dc16077a763 | -3.42393 | -53.42016 | 2026-01-07 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03ef3f84-d853-3eab-80b1-cb69ec7d5332 | -1.89872 | -53.25541 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 305eb578-d0b8-3953-9d91-265a41861b6e | -1.56049 | -53.818 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc6ad403-5927-3fea-afbe-090113e13db6 | -2.90933 | -54.14461 | 2026-01-07 05:22:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d387e3ff-5fd9-326d-b087-44a97ff5076c | -2.16177 | -51.98765 | 2026-01-07 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f798e5ec-693d-3a8a-82eb-01f0c9dae6e5 | -2.74808 | -54.93341 | 2026-01-07 05:22:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83f63c7b-72b5-3d76-b603-dd7e89334c6c | -1.25524 | -53.48774 | 2026-01-07 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df34088e-de49-338a-b408-0181d17b06de | -3.80893 | -51.03086 | 2026-01-07 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c9942a3-5396-3acf-9eee-2300a5f1c6a1 | -1.21126 | -54.03171 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30bf55bf-fe86-3470-aa0d-00006a90c098 | -2.69323 | -48.9899 | 2026-01-07 05:22:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfd4e2d2-87a6-39ea-a937-70914c4f9b30 | 4.51459 | -60.61354 | 2026-01-07 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 583f47a4-5c41-3962-8961-f5b095c23427 | 3.28197 | -60.03796 | 2026-01-07 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e96e3c73-1a04-3e43-a64a-2dfe06aaedf6 | -2.79864 | -52.90298 | 2026-01-07 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9bef571-92b8-3be7-b910-d480766bb9b0 | -1.59958 | -53.98984 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b5b7c30e-913a-3739-8588-0e133fae5727 | -1.97746 | -53.35788 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dba5d95d-47b5-33f9-89e4-80e6fad28f1a | -1.59834 | -53.99078 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 72ae9343-055d-32a8-af8a-56f38df1054c | 3.28927 | -60.04051 | 2026-01-07 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b51638-93a7-361e-8edc-7f9ad2f3e4e2 | -2.27671 | -53.78253 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e96c53f4-4a5b-384e-9824-b0d6fe6d8a5c | -1.59894 | -53.98697 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 664b1c58-0d6a-3544-94c9-15f35b062c36 | -2.73848 | -54.94252 | 2026-01-07 05:22:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71e62850-aeca-3499-9092-908ab8075a2d | -0.08825 | -51.28001 | 2026-01-07 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85c0ec01-7266-3513-9337-9db598930e5f | -1.3051 | -53.90366 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7435ae95-131e-3163-845b-1ad42bf0544a | -3.80368 | -51.02964 | 2026-01-07 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbea3151-7ba6-3869-89bf-2ae883ebe3e2 | 3.51795 | -60.65858 | 2026-01-07 05:22:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c216db8-df42-3fa2-a77b-fa553bb91ee9 | -2.27902 | -53.78537 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 942fc8b5-0fcb-3bd0-9592-a69dbdabed9c | -1.7591 | -54.13096 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4dfb1ac-2fe9-3a72-b8cf-21d659cca479 | -2.0044 | -53.21161 | 2026-01-07 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f36fdd13-f20f-3a73-a828-3cdd4f21e50e | -2.27608 | -53.78656 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c421fa7e-358e-3e6c-aa0e-f4fbd3f0b9eb | -1.17074 | -54.07492 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f255aae-3ba0-384c-b200-658323d9dbce | -1.29615 | -53.90612 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 152ac3d4-70e7-3411-98c4-703571c18144 | -2.74862 | -54.92995 | 2026-01-07 05:22:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c3c43c5f-e10f-3aa2-8341-7f63df031652 | -1.55989 | -53.82196 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65cde9f2-9780-3c22-b4da-4d8dfbb08165 | -2.16792 | -53.67175 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04176f35-f35a-3823-83da-e72f7b57d096 | -2.16581 | -51.99374 | 2026-01-07 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8f297143-43d5-3fa6-bb06-8a920aa5b254 | -2.16662 | -51.98841 | 2026-01-07 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 349e0ca6-a9d5-3843-aabc-697515eaa569 | -2.28036 | -53.78726 | 2026-01-07 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf339521-8356-3eab-ba1a-7ae068550028 | -2.71998 | -54.54626 | 2026-01-07 05:22:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d1becd4-6a37-3f37-bc5d-163eea8f3d1c | -1.30034 | -53.90679 | 2026-01-07 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07330d67-c3ff-369e-bc79-02ec7da2b03b | -16.32109 | -57.56205 | 2026-01-07 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d749b0cb-2e64-3b91-ad9f-6b35f91f4f8c | -16.16436 | -59.32377 | 2026-01-07 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9d7bb3b-6179-318d-99ad-cddd4d63b2e3 | -16.36924 | -57.2081 | 2026-01-07 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| c2f72685-167e-31d3-9c31-aeb332ff766f | -16.20177 | -59.32475 | 2026-01-07 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9cb8951-00a4-3ded-880d-635079949ed9 | -15.68727 | -59.6597 | 2026-01-07 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83e50107-76c2-3708-acb5-29ca40af4ac9 | -15.97998 | -57.25051 | 2026-01-07 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bba9eb9-75cf-3540-8bd0-cdd49972596c | -15.51323 | -60.13902 | 2026-01-07 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1493e5f-6e04-3b41-849f-c7f7a8aa41a0 | -16.16006 | -59.32771 | 2026-01-07 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eea300b6-a82e-35d5-90ce-0a33716a2f16 | -16.31652 | -57.5651 | 2026-01-07 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a82e4160-1ac6-3f4a-a813-99d962431243 | -16.59679 | -58.21336 | 2026-01-07 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f699d3f1-781b-3941-ab51-3efac62de9b0 | -15.80681 | -59.23564 | 2026-01-07 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b851e91-aff5-332a-9c51-d7c3e41ef949 | -16.60073 | -58.21394 | 2026-01-07 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d77d28f5-fc75-34f1-8ddd-47343778f250 | -3.50437 | -54.67725 | 2026-01-07 05:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee8165f5-262b-3120-90ea-212b66d86db9 | -16.04577 | -59.20899 | 2026-01-07 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 377ffecd-629e-32d7-bed2-a7706dd8a3ca | -16.0495 | -59.20929 | 2026-01-07 05:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README6.md)
