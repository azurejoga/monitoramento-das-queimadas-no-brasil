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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bdc4713-f98a-372c-b2a0-fb63f5ebc31b | -15.29879 | -52.80684 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06cbe4cd-6752-3662-93c4-9659d14069eb | -15.2407 | -52.79876 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a767967-f70a-30e0-bbd1-edd845cdd0dc | -14.54235 | -52.29612 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b4488e5-c342-3c3a-ae9d-d84e2441860e | -13.18323 | -51.49537 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 131ca18b-8744-362c-92cd-f930ddd90b5e | -15.30144 | -52.80882 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f557bb4-ccb7-3539-9a94-44049e1236a0 | -16.39022 | -49.91865 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41b84d4f-5b19-38b1-952f-ce2fe5bb92ca | -14.35566 | -52.92915 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10a9593d-07c0-3f6e-974a-95c7262a1194 | -13.20895 | -51.48304 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e743fab-d0bb-38e5-a9eb-7a792c9be1d9 | -14.92462 | -52.64016 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d47fa18-b4ca-3fb1-8301-4acb218b0668 | -20.72598 | -57.82037 | 2026-08-25 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f3c9fc3a-fd02-3959-876c-ff0d648dd00d | -20.71412 | -57.82727 | 2026-08-25 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2de935c3-d123-398f-9c7e-ab4785687049 | -10.7801 | -50.9113 | 2026-08-25 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 6f2cde89-576a-30c1-9a63-8d6f6df11f7a | -11.9991 | -45.9287 | 2026-08-25 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 84620934-1255-3dda-809b-5ada069a59b0 | -3.5407 | -48.1673 | 2026-08-25 05:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| ceddea0c-a364-379d-bda1-1647c66c7625 | -7.2901 | -45.3683 | 2026-08-25 05:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5a3377e2-6090-3c00-97d9-7c55d3d29070 | -11.1443 | -44.4865 | 2026-08-25 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 21db8d2e-d842-334a-8526-137ee24c2cdf | -10.7799 | -50.9325 | 2026-08-25 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 07de80f9-9edf-3fc1-b463-a39f3d12e069 | -10.7988 | -50.9305 | 2026-08-25 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 152.4 |
| f6d3108a-d206-3368-955f-fc188c7a733c | -3.5221 | -48.1896 | 2026-08-25 05:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 38f3cf0d-4d8a-3e87-9f2b-2038502c1e58 | -3.5406 | -48.1889 | 2026-08-25 05:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 8e4d4c9a-795d-3b16-b152-9d07d28fafb2 | -7.0057 | -59.2575 | 2026-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.7 |
| eee94a23-ab7c-357f-8f27-07332aa93d51 | -7.0058 | -59.2382 | 2026-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 3801996a-5ad3-32a4-8d5e-b991241eda30 | -10.7991 | -50.9093 | 2026-08-25 05:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c8a0d821-4fe8-3bf7-98f6-f2c187476461 | -6.9872 | -59.2582 | 2026-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 600f4fb9-ce45-355c-af94-efe01aacfd70 | -6.641 | -58.4987 | 2026-08-25 05:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9ff1a885-3804-343d-ab2f-36a3d6c1348f | -11.9803 | -45.9086 | 2026-08-25 05:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c65863b5-9770-3ae0-a25d-8c105672ca52 | -7.2903 | -45.3456 | 2026-08-25 05:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| cac3e4f3-3d2f-37fa-a2f3-24084518d6ba | -11.1447 | -44.4632 | 2026-08-25 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 3ab7fba0-93b6-3435-8250-fdbbd908fbe6 | -6.9873 | -59.2389 | 2026-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 739e2592-7385-3a0d-b321-5b1418581851 | -7.2194 | -60.6125 | 2026-08-25 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 792ae806-993e-38dc-8dc6-977b57287a4a | -7.0058 | -59.2382 | 2026-08-25 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 7a1c65f1-b219-3c05-9893-c37306169398 | -6.641 | -58.4987 | 2026-08-25 05:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 35fdd3f5-2997-30f7-868c-b0899d62f14b | -3.5407 | -48.1673 | 2026-08-25 05:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 876da6aa-bd45-3849-b416-63c7395b13b9 | -6.9872 | -59.2582 | 2026-08-25 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 49f05c62-d18e-341b-b841-a97cfd577d09 | -6.9873 | -59.2389 | 2026-08-25 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0de8984c-334f-38c8-a941-ad5425ed5726 | -11.1447 | -44.4632 | 2026-08-25 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| c5069a58-9192-392b-ae24-d7f5d3ef825c | -7.2901 | -45.3683 | 2026-08-25 05:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 37e5fca0-e7da-30f4-8973-b3c008a109af | -9.7125 | -46.0682 | 2026-08-25 05:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| e98335a8-1460-3c6d-9de6-a6c32802e9bc | -9.6935 | -46.0704 | 2026-08-25 05:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 00625af7-f16b-38e2-968a-54bb751f4477 | -3.5406 | -48.1889 | 2026-08-25 05:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 1fdda113-0e89-3733-bb9d-6b7725bf739a | -9.6938 | -46.0478 | 2026-08-25 05:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| c658ac46-e212-3af8-8daf-2b4ac02307e8 | -11.1443 | -44.4865 | 2026-08-25 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 3261b5c3-5c55-3ae4-bc82-86e34a0ca9eb | -7.0057 | -59.2575 | 2026-08-25 05:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.2 |
| c73a2768-ca72-3060-a239-f001027b150d | -9.7128 | -46.0456 | 2026-08-25 05:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ebc38185-7aff-36da-a16b-21c4009d0472 | -11.9995 | -45.9059 | 2026-08-25 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 6989c3fc-cd8c-3d7e-91d5-aa188876d989 | -3.5406 | -48.1889 | 2026-08-25 05:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 6e6b0ad1-1c00-36e2-a5ca-ef42b196944c | -7.2901 | -45.3683 | 2026-08-25 05:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d4efedff-eef2-3e76-8751-498950d2d6a0 | -9.7128 | -46.0456 | 2026-08-25 05:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e8e2d516-538d-37f5-b347-3621e60cf5c7 | -6.9873 | -59.2389 | 2026-08-25 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 02ce6617-200c-30b5-a766-6bc0f973e9a8 | -11.1443 | -44.4865 | 2026-08-25 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 445e9867-26c9-3179-91b5-9ca3227813da | -10.7988 | -50.9305 | 2026-08-25 05:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 3e082c81-a70b-3012-88a9-5555e3e7715e | -9.6935 | -46.0704 | 2026-08-25 05:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 55cda9c8-8453-371b-9c4e-0b8df5c2d66f | -11.9803 | -45.9086 | 2026-08-25 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7a1d371f-2093-3963-920d-f62d97f543b1 | -9.6938 | -46.0478 | 2026-08-25 05:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b9bec387-b098-3edb-b375-d05f42e60c40 | -10.7801 | -50.9113 | 2026-08-25 05:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 90de51ff-5932-31ac-946f-1547382409b7 | -7.0057 | -59.2575 | 2026-08-25 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 6d0599fc-9809-3572-9be9-9c198eee7a4b | -9.7125 | -46.0682 | 2026-08-25 05:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 5beb5b7b-f5c4-3bf3-a83a-4492716a32d0 | -10.7799 | -50.9325 | 2026-08-25 05:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 340a2d7b-250d-34cc-8890-922b6c257eec | -3.5407 | -48.1673 | 2026-08-25 05:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7dc67cdb-dcd7-3f91-9572-b02181ad2bf8 | -11.9991 | -45.9287 | 2026-08-25 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 0acee2c4-0463-3fe5-8932-61f8385ddf44 | -11.9799 | -45.9315 | 2026-08-25 05:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6ad82814-5c4c-3791-a4e0-3655c7f7da58 | -6.9872 | -59.2582 | 2026-08-25 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| b212e321-0165-3ba7-80b1-8b876e5011bb | -7.0058 | -59.2382 | 2026-08-25 05:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ffaa94f0-495c-3457-b097-608ac7004d7c | -6.641 | -58.4987 | 2026-08-25 05:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 41a99e9e-f6d8-36a7-bac7-872323dea173 | 4.41956 | -59.88956 | 2026-08-25 05:44:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9206c05-6faf-312e-a70a-77c0b7731c1e | -4.83569 | -55.91102 | 2026-08-25 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8ad233c-963f-345c-ad2e-eaf1cc61622f | -4.47812 | -54.80546 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06250d70-fc09-3f22-9a42-671db2b9d855 | -3.10025 | -61.22453 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3efd67ad-eeea-3bb8-a9b2-db2e020a20d6 | -1.42472 | -55.25309 | 2026-08-25 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a3e84a-212b-30bd-a257-905692babf1b | -4.19679 | -54.57725 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47bcf1c8-ebdc-3925-a508-b98e69c4764b | -3.13403 | -61.18811 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f8ccc34-31dd-37c0-803c-e7d741f43df4 | -3.09399 | -61.19706 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 846ddf40-7c06-35e1-8929-ab9fbf564afd | -5.95509 | -53.6028 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6ad643b-5ee0-33cc-9b71-194c3e348752 | -3.54596 | -54.49463 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 907d3a03-2bc2-3887-bb2d-5b909df597f5 | -3.1031 | -61.22875 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38a8643e-bc18-3546-ba31-2deb19e6c3b4 | -4.19157 | -54.57645 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e60e6f52-6d18-3f65-868a-17267f957597 | -3.1071 | -61.22559 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f687acf-f0b3-3a6c-b08c-3beb8fd3b077 | -3.59047 | -54.83962 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e321ac81-953f-3be4-99a8-0251d023db2c | -3.49152 | -59.28944 | 2026-08-25 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78892552-5f6b-3edf-a0c2-b42fc853b733 | -4.78782 | -56.10505 | 2026-08-25 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fd9fa7a-8e74-3ccb-8679-20e46916c4e1 | -5.0122 | -56.13692 | 2026-08-25 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efcc3f34-5bce-3ca9-9043-f891a4d0bbbd | -5.9583 | -53.57962 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f4b3798-87cf-3a9a-a5e9-8468994a2b95 | -3.0114 | -51.05227 | 2026-08-25 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 681934f1-d333-33dd-8463-93dfc6121f0e | -4.19155 | -54.5793 | 2026-08-25 05:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dfaac96-af8a-384e-9225-070cbde3cd51 | -4.6079 | -55.74115 | 2026-08-25 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8f2dfac-5b35-3530-8bd6-b917017216c5 | -4.13797 | -56.35902 | 2026-08-25 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59c11379-45ec-36ed-8adb-b3a34ca1b746 | -3.01269 | -51.04766 | 2026-08-25 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65a31c98-5bfd-3ab5-be7e-58edf4816345 | -5.95777 | -53.58348 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5632f845-0c70-3382-8860-982f6b1498a7 | -5.95203 | -53.58271 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c38de04-580a-33c8-b065-cd8ebc214a32 | -5.95671 | -53.59114 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f14e86e4-62a0-3111-a3a7-225efb6da224 | -3.01191 | -51.05303 | 2026-08-25 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80d2e8d3-f911-3d7f-ab15-50dcfe54f2c7 | -3.13118 | -61.18388 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b00f8471-33e3-30b4-8f6b-8809cf7a1e99 | -5.95723 | -53.58733 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4bdd2a8-d0bd-38db-bbed-1e1ae8df4b4d | -3.59812 | -54.04312 | 2026-08-25 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65204495-9a50-35e4-a4b7-31c86243e254 | -3.391 | -59.56366 | 2026-08-25 05:46:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1d1e80e-83e3-3f37-bf19-893a60dc87ba | -3.10046 | -61.51286 | 2026-08-25 05:46:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be9b18da-2032-30f4-ac77-88a3a9fa9bd0 | -5.95257 | -53.57882 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac04b225-4190-3cc5-b091-326fb59f01a4 | -4.83684 | -55.90836 | 2026-08-25 05:46:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bae85d2-d52b-3e61-8aab-b003b22df947 | -3.13461 | -61.1844 | 2026-08-25 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8496d8a3-3f3d-32fc-b852-8787cdf1abf5 | -4.4792 | -54.80406 | 2026-08-25 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README59.md)
