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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b69cd52-485b-3ee9-98fd-6adf001a25ae | -9.0402 | -66.0333 | 2026-09-25 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| db56efd1-2003-36a5-86c2-a46c078e7085 | -7.235 | -73.1364 | 2026-09-25 16:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 3a5b6503-b540-342f-b4b2-d9a69b70fd70 | -10.6928 | -60.7322 | 2026-09-25 16:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a043d535-209b-337e-8262-d00d6290d323 | -8.7129 | -69.8135 | 2026-09-25 16:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 46dd60a7-50f2-3be1-8a29-ec92b1edb6e8 | -11.3845 | -63.4178 | 2026-09-25 16:40:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 00548f49-e69d-3f7b-bfb6-4d90b8c9f6a8 | -12.3706 | -62.4459 | 2026-09-25 16:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| edbcff66-3e62-3208-8f95-3e99201681e3 | -11.3845 | -63.4178 | 2026-09-25 16:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 612d3d87-1acb-32da-b43d-caa7a0f2c43f | -10.6928 | -60.7322 | 2026-09-25 16:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 4509e36c-0a69-3f7a-a07b-5059173ccb3d | -12.3706 | -62.4459 | 2026-09-25 17:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2b912768-c4ab-30d3-a515-72bc7cd73668 | -10.6928 | -60.7322 | 2026-09-25 17:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| cde40ce7-a872-3d0f-90d4-7d5aed21f94f | -12.8059 | -54.0255 | 2026-09-25 17:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 1a0e9159-5e0b-3bfb-aea2-949727461aa6 | -10.7115 | -60.7312 | 2026-09-25 17:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 245a2d7c-f484-3ca5-90ca-b6c2a6b6093f | -12.8059 | -54.0255 | 2026-09-25 17:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 3ad88c24-03de-3672-9583-b3525e1db646 | -10.7115 | -60.7312 | 2026-09-25 17:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 1c1cd62c-1b86-3a0b-974b-6b3af6125079 | -10.6928 | -60.7322 | 2026-09-25 17:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| b9297c72-bd08-3ca2-9437-edef3a6abeb9 | -11.76 | -50.55 | 2026-09-25 17:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83324c3a-2792-30bf-bb8a-992cf681fffb | -11.97 | -50.73 | 2026-09-25 17:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5903f805-0f0c-3888-8215-335f734e34b2 | -12.0 | -50.69 | 2026-09-25 17:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82d465ab-02e6-3486-9c7c-9660a18eefba | -15.15 | -41.33 | 2026-09-25 17:15:00 | MSG-03 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 030c6a53-aef4-3e8a-ba31-00c19457051a | -11.82 | -50.57 | 2026-09-25 17:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a6d95c9-156e-3b2b-a519-b68728f841ce | -12.0 | -50.74 | 2026-09-25 17:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcfa5e53-6e13-3d4e-8321-0d758ca6213a | -15.12 | -41.32 | 2026-09-25 17:15:00 | MSG-03 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a363382-8917-3ae4-b0f5-5f781b967441 | -11.79 | -50.56 | 2026-09-25 17:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6850a144-3733-31c8-9c09-1c380f696cb1 | -11.79 | -50.62 | 2026-09-25 17:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e171ed1-2e1d-38a6-9d68-e4e4f2839d79 | -1.3742 | -49.3154 | 2026-09-25 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5ab12053-3bfc-3fdf-a61a-058c13a82659 | -10.6928 | -60.7322 | 2026-09-25 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 51aa42fc-1fa3-3f97-882e-17d3cb3ca8c8 | -8.7892 | -68.929 | 2026-09-25 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| d1a3e281-e368-3154-a86a-ded7f059946e | -1.1345 | -49.2123 | 2026-09-25 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| af3cd21b-d50a-379a-9eeb-6bcc545f6caf | -12.3517 | -62.447 | 2026-09-25 17:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9dde2f50-d0ab-3d98-8a68-5684a234d8f0 | -9.0402 | -66.0333 | 2026-09-25 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 64ac939f-5f45-3046-acde-086283f3d27b | -12.8059 | -54.0255 | 2026-09-25 17:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| fd0c1457-92f9-383f-8993-9828709c7f62 | -12.7865 | -54.0482 | 2026-09-25 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 2f55a37e-8414-32ea-be51-d23aca874d38 | -12.8059 | -54.0255 | 2026-09-25 17:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| f2421101-a449-3f6a-ac42-f67a6531824f | -10.6928 | -60.7322 | 2026-09-25 17:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 2d45620f-1c62-37fc-9b8d-07ebcde59c6e | -9.0402 | -66.0333 | 2026-09-25 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7ebee011-71e0-3f96-bf7b-d73251818931 | -14.3499 | -52.1051 | 2026-09-25 17:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 54589a31-8ce2-329d-aca5-4931841cac79 | -10.8757 | -57.1554 | 2026-09-25 17:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 89c523c2-7932-3974-b9c7-00e93722e656 | -1.3932 | -48.9961 | 2026-09-25 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b1f1f056-6d42-3f10-a2c6-4e6529ec3ad8 | -14.3693 | -52.1026 | 2026-09-25 17:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 8674958c-ce00-349b-b656-7cd608637ada | -7.235 | -73.1364 | 2026-09-25 17:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 922ac761-90a0-3678-964b-fa5ca0bab4bb | -7.6759 | -73.0795 | 2026-09-25 17:40:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 71c42f0d-1cd4-34ae-a126-0ff341a26512 | -12.8056 | -54.0462 | 2026-09-25 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 2bd08882-bc2f-3cb7-8d56-2d6dbc1d7cf8 | -14.3696 | -52.0813 | 2026-09-25 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 00fde68d-4abd-30ef-8d57-88472ca87ccf | -8.4126 | -72.765 | 2026-09-25 17:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 143.9 |
| 3cb63fd3-f3d1-357f-817e-ec37fe14f858 | -1.2086 | -49.0625 | 2026-09-25 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b4eb9e23-5f8d-3f12-8805-eec4950cd9e9 | -12.8059 | -54.0255 | 2026-09-25 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 73beeb40-4e5b-3549-b9ae-b383e7ea6828 | -14.3499 | -52.1051 | 2026-09-25 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 2950aeef-77f6-3a63-8f47-8740411fa081 | 1.9976 | -50.8813 | 2026-09-25 17:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 26e8779a-7ad8-3650-b309-343318475293 | -10.8569 | -57.1568 | 2026-09-25 17:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 7462f789-b1ea-3666-afbd-6be7a83771ed | -9.0602 | -65.697 | 2026-09-25 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 80e89058-e295-37b6-9137-762a884bf99e | 1.4452 | -50.8071 | 2026-09-25 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 136ee8c2-ebfd-3c25-8ed2-7ab0e0bc0f98 | 2.2246 | -55.8358 | 2026-09-25 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 62f0f44b-0aab-3307-816f-f11dd273735d | -9.0408 | -72.3762 | 2026-09-25 17:40:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 93b49ab0-dc72-3c47-924f-93e70491a0af | -8.7276 | -71.7019 | 2026-09-25 17:40:00 | GOES-19 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 72239703-8bcd-3c92-8a41-0cdeccf9e6b9 | -12.7865 | -54.0482 | 2026-09-25 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 3e8aaccf-ad4a-32fd-82a3-392ea6f5f3b8 | -1.4116 | -49.0597 | 2026-09-25 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |


