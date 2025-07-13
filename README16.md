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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7171d387-9f63-3278-9b16-c3758e8b49f0 | -7.67297 | -72.33077 | 2025-07-13 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 813c427f-77e4-3a5f-b191-f23901c7d95e | -10.05121 | -59.11506 | 2025-07-13 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e840193-4d9d-37a1-a92d-de29dbe5776c | -9.02652 | -61.22566 | 2025-07-13 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 232aa917-d936-366e-b078-e3dc28a676fe | -8.01774 | -72.39265 | 2025-07-13 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ac938e6-40e2-317d-b54a-eea775abeab7 | -8.69184 | -63.94192 | 2025-07-13 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5f6ab0c-908f-3319-8673-c3fe6673c2ac | -13.02156 | -47.81677 | 2025-07-13 06:01:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4fc043cf-9c9e-32c6-9107-dc919396b34e | -9.02056 | -61.22851 | 2025-07-13 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 822bbcec-c69f-382a-8087-9dbda775983c | -10.04549 | -59.10902 | 2025-07-13 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b046d80e-2f0c-359f-a90f-1a774b18b3e9 | -9.10468 | -63.55969 | 2025-07-13 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed4660cc-b050-34c3-9817-506687c86963 | -7.85302 | -72.45422 | 2025-07-13 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92e53a05-fe62-333d-be10-804ef2b32f8d | -9.9215 | -59.9142 | 2025-07-13 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9efae564-5ea1-3f1c-8197-03b68cfa439a | -7.38625 | -72.68885 | 2025-07-13 06:01:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22333e07-f1ec-3505-9769-79481181ad7f | -10.56629 | -49.11494 | 2025-07-13 06:01:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 430cf47e-9f7d-3b6a-b6f3-4a3a29385ff5 | -13.84255 | -46.88769 | 2025-07-13 06:01:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c7068522-564c-3850-88d1-0d9f03a8baa8 | -10.56493 | -49.12421 | 2025-07-13 06:01:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dc18d6c0-0832-352d-b179-0645d5c7086d | -10.04753 | -59.11409 | 2025-07-13 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5276ef2b-8185-3ef8-9ef8-0acf18327880 | -9.67045 | -65.4566 | 2025-07-13 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f557a0da-72c0-3986-8d59-47d69dbf4dfd | -13.11445 | -47.28453 | 2025-07-13 06:01:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3bd4445e-2599-3e86-831d-e97f792082ec | -13.02172 | -47.8237 | 2025-07-13 06:01:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 30b9e097-892a-3a83-8ddd-61b8d90aa2f5 | -13.84071 | -46.90157 | 2025-07-13 06:01:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0605b78f-5103-3a01-8886-9f9d7aaeaf93 | -10.04812 | -59.10894 | 2025-07-13 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21ac3048-257a-35e9-89da-ceab84878c5a | -12.02809 | -63.789 | 2025-07-13 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63025652-c6a7-38f8-9937-110f5a0bdb8d | -17.65336 | -50.48721 | 2025-07-13 06:03:00 | AQUA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1225f39a-6b4f-3550-9570-29ff38899f58 | -17.65474 | -50.47747 | 2025-07-13 06:03:00 | AQUA_M-M | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6dbff90f-dc1b-39b9-a1c5-098e6a0607e7 | -12.02328 | -63.78839 | 2025-07-13 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7853ed4-90a9-3732-91af-fdda30544a5a | -12.02397 | -63.78307 | 2025-07-13 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd304f19-898d-322b-b4be-008dac6da942 | -12.10184 | -63.70707 | 2025-07-13 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0312d6d3-edcb-3164-81fb-f4f56ed79574 | -7.38295 | -72.68796 | 2025-07-13 06:27:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de66a833-4489-32a1-bbc6-d7b5b04005e1 | -8.23304 | -70.866 | 2025-07-13 06:27:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3c231db-c3a5-3d02-bc9c-78baa950453d | -7.6719 | -72.3265 | 2025-07-13 06:27:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccf3b86e-613a-337e-837a-b37d749fd79d | -9.24831 | -64.40761 | 2025-07-13 06:27:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fedfeea-bb71-38b7-84dc-e91aeb0f4034 | -9.24904 | -64.40162 | 2025-07-13 06:27:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 994ca374-584d-37bb-b977-87b77d555eb5 | -8.01806 | -72.39132 | 2025-07-13 06:27:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5724dd0f-0f66-3da0-aed0-2602d724587f | -8.01678 | -72.39324 | 2025-07-13 06:27:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee3ffc05-1e50-3f5e-a509-3f67a615b3a7 | -8.01737 | -72.39616 | 2025-07-13 06:27:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7373117d-4d94-32ab-878e-69fe5529648e | -8.23064 | -70.86606 | 2025-07-13 06:27:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d63778c-a207-39d3-8297-9b8d9775f982 | -7.67118 | -72.33134 | 2025-07-13 06:27:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84671f1b-abd9-3f40-84bb-8095503ea848 | -12.01853 | -63.78616 | 2025-07-13 06:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d34ea33-1b2c-3fe6-aa2d-01330ffa587f | -12.02569 | -63.78689 | 2025-07-13 06:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a3cefea-7aa2-354a-b51a-761850bbd021 | -14.5671 | -49.7023 | 2025-07-13 06:30:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 41.5 |
| d2c89275-684b-3b7a-8223-3ce59f6e4b9e | -6.47856 | -45.26047 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 56a46b47-5a88-365f-a0da-5e90034b7691 | -6.44055 | -45.41075 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2dd71991-0389-3590-9018-0f9fa05ca3ef | -5.73523 | -44.98256 | 2025-07-13 11:49:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| f3b063b5-05f8-3689-886d-fff3cbe59e68 | -7.13298 | -46.87485 | 2025-07-13 11:49:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 445f5ca2-1b67-3d3d-812a-1918bb900e06 | -6.48198 | -45.25529 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| aaaf7d1e-b89f-3a64-b306-9ae5e1301373 | -6.43183 | -45.4035 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 1855de87-32a8-3745-b70d-54847b3371e4 | -5.15576 | -37.94748 | 2025-07-13 11:49:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 600263c5-0207-34f8-a401-ede5c68f5494 | -7.31021 | -45.33504 | 2025-07-13 11:49:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a86759ce-9d63-352f-b4fe-d0c990ce693e | -8.33444 | -44.91992 | 2025-07-13 11:49:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fb1e2a90-35cc-34c0-84b3-89cd562598a8 | -6.13035 | -42.9491 | 2025-07-13 11:49:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 8cfe94bc-400a-3b25-bcd7-d13c73d5ae04 | -5.3884 | -42.66674 | 2025-07-13 11:49:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a2d23e80-936d-3da3-9189-d543aec880bf | -6.95485 | -42.7415 | 2025-07-13 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 544b5576-2ec5-3b9d-a5c0-21177eed42e9 | -7.13349 | -46.86874 | 2025-07-13 11:49:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 2c20ab3b-c56b-334f-8d0b-6f584ca6cd6c | -7.04393 | -44.34361 | 2025-07-13 11:49:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 84d7552b-c172-3452-ba47-ee2f34a33fa3 | -6.47521 | -45.28121 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 64bffdf6-fa5a-3873-8d55-c7324224a18f | -7.30713 | -45.34148 | 2025-07-13 11:49:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3f781d73-b069-36cf-8252-545813a77cef | -6.78304 | -43.96357 | 2025-07-13 11:49:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5ac5ebc4-de38-329c-b8d9-cbfdc7548c27 | -6.42312 | -45.03225 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d9518384-42b6-370a-baf5-c1a41e2c9d4b | -7.04123 | -44.36095 | 2025-07-13 11:49:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| c902893a-3185-37bb-8c3b-92233ddddf58 | -6.79169 | -43.95467 | 2025-07-13 11:49:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c1f71b18-bb6e-3e3e-8aca-2d1b932db703 | -6.47882 | -45.27585 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| a5f9f5ba-6c6c-3c58-843f-1494de6e377c | -4.85745 | -43.22052 | 2025-07-13 11:49:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d15b91ed-1f8f-327c-834c-a67188c38f31 | -8.33144 | -44.93884 | 2025-07-13 11:49:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8214cfd9-462c-3512-a33e-b9c615957602 | -6.95683 | -42.72829 | 2025-07-13 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 247fb588-5333-3a33-a23a-42755e70abf6 | -5.37748 | -42.66515 | 2025-07-13 11:49:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e3555707-fe49-312b-a131-1ea362d13439 | -6.78909 | -43.97113 | 2025-07-13 11:49:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| abf75ccb-71c3-37c9-b555-c5581b84e061 | -6.87871 | -43.70254 | 2025-07-13 11:49:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| c1b2c655-d3c6-3d6d-83ef-02e657023785 | -6.74049 | -44.6969 | 2025-07-13 11:49:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| abbd8122-3e7b-34ad-bbf5-71995e8a28ae | -5.85848 | -39.03477 | 2025-07-13 11:49:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 01b83108-d831-31f0-afd2-a2792c139e82 | -6.12814 | -42.96343 | 2025-07-13 11:49:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 6f0f9ee5-bb5d-3c94-8750-c7cfe46e670b | -7.31054 | -45.32036 | 2025-07-13 11:49:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 304d81e6-2aa7-35f8-8d99-552e6735ee31 | -6.83644 | -38.51642 | 2025-07-13 11:49:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 11.0 |
| dcf8a512-73cb-32ad-ba0b-13b13bf250ff | -5.85717 | -39.04371 | 2025-07-13 11:49:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| fb67d38a-d6f2-3965-a150-6299f57f01e2 | -6.49171 | -45.26288 | 2025-07-13 11:49:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 297d7e2a-ec0b-31c3-9414-9378f1e9cc17 | -6.87628 | -43.71841 | 2025-07-13 11:49:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1b8ba738-6c62-32d5-b5cb-e47b418ecc37 | -6.70448 | -44.31937 | 2025-07-13 11:49:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f51a7476-3f32-3bcf-8561-66857ab3e6e5 | -2.76966 | -42.47583 | 2025-07-13 11:49:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fd91bfd8-57e8-3b1f-b802-50a269918d9d | -15.35268 | -43.66935 | 2025-07-13 11:51:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 16b75df8-aa62-3a0d-bd9c-64f29914871d | -12.43823 | -50.48265 | 2025-07-13 11:51:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 2ccd87f2-84c3-3d91-a5fc-168e13f4c101 | -15.35456 | -43.65753 | 2025-07-13 11:51:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 27.0 |
| aa193f45-9ba8-33c8-86f3-114e7de366e4 | -13.22469 | -44.97369 | 2025-07-13 11:51:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c6d24a31-2128-312e-8dcf-484832fae1fd | -11.438 | -45.10628 | 2025-07-13 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4a492dab-a4cc-3e11-834c-143aeed0684e | -16.04111 | -43.3452 | 2025-07-13 11:51:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 292cb8e1-21ee-3642-8dc2-b8c4a5d7a0e5 | -13.31772 | -43.6824 | 2025-07-13 11:51:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24cca1fb-d256-38c6-b4ff-b9fab33e765e | -11.44988 | -45.10825 | 2025-07-13 11:51:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 232eccb8-edb2-3d52-b587-ab5be728a18c | -13.88423 | -44.45701 | 2025-07-13 11:51:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1b437794-20cd-34c2-8167-77059770bf94 | -13.88661 | -44.46413 | 2025-07-13 11:51:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cfca51b9-e352-3085-b142-ba444bab6d0c | -13.84233 | -45.89062 | 2025-07-13 11:51:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b70f0a36-8b65-359e-839f-a8a1dac33c9b | -21.42192 | -42.42251 | 2025-07-13 11:53:00 | TERRA_M-M | LARANJAL | MINAS GERAIS | Brasil | 3138005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fad35230-b341-32be-a9b3-205e31cf17aa | -7.0381 | -44.364 | 2025-07-13 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9d06953e-2ab1-3441-8930-48bfb19ea5cd | -7.0381 | -44.364 | 2025-07-13 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| ddc78743-0de3-3450-8595-4726ef714d2e | -12.4393 | -50.4678 | 2025-07-13 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 21fb6d8d-e5e8-3f6a-89b7-114de2393d0c | -4.5429 | -48.0151 | 2025-07-13 12:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 8e72a9f7-c00d-338d-b7ec-f52bfc41c949 | -12.4393 | -50.4678 | 2025-07-13 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2c54950a-6901-3814-b6dd-ab320a1ffe20 | -7.0381 | -44.364 | 2025-07-13 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 05073e46-fc5a-3c4e-9229-c41200b97546 | -7.0384 | -44.341 | 2025-07-13 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fe82243a-9d36-3a07-914c-a6cbe89f747e | -7.0384 | -44.341 | 2025-07-13 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 229d66b0-f9d7-3bda-a40e-ddf4118e8099 | -12.4393 | -50.4678 | 2025-07-13 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 5623f957-fa40-3428-ae19-0475ed14d322 | -7.0381 | -44.364 | 2025-07-13 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 148.9 |
| aa109d8a-c7fa-3cb6-bb3a-ccfa204534f3 | -12.439 | -50.4894 | 2025-07-13 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |


[Clique aqui para ver as próximas entradas](README17.md)
