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
| fb652521-08c6-332e-9f80-50c42af81b96 | -5.87284 | -57.77788 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ec603de-11b2-3b93-bd4c-143536ec316b | -11.27493 | -50.58663 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 93d3bcc6-f094-3fd2-b487-63a72802231c | -6.16754 | -45.91325 | 2026-09-01 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18034d19-95f4-376b-ac3b-9a619406be13 | -8.5926 | -54.72011 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb0553ac-5f86-3ee1-a58f-42eec741834a | -5.87692 | -57.78428 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d952446-48ca-33cb-b537-d93c05667fd5 | -9.67134 | -50.83721 | 2026-09-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c298b8e0-9027-3233-85e8-3ea97365ad2b | -6.95267 | -55.64728 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c28522b0-f146-392c-9aa6-c2a0de3d626b | -3.2634 | -58.24186 | 2026-09-01 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ee26c81-8d26-3159-a392-d80b2c351b1e | -7.9286 | -44.23167 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 195be97c-5ef9-3960-bdb3-3746779c65c8 | -11.29922 | -50.60487 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a23c5034-60cd-329b-b9f4-3d70fb68d79c | -10.03924 | -44.69867 | 2026-09-01 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68247211-0292-342b-b28d-dada6e6e1d50 | -7.62148 | -57.62012 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e95a6bc8-9d35-3755-89d5-da851e9806f1 | -11.26228 | -50.60256 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb374fd7-823f-3ad0-9182-cd7867dbcd5f | -4.64809 | -55.85245 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bcd56d5-c1cd-3687-be57-e4ece5f92f3b | -3.61898 | -60.55808 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd2efc06-8c12-3b8b-bb73-ce6c45cc2426 | -5.86732 | -57.77992 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab27d92d-6d8e-30c0-9581-45b23db8f5dc | -7.08526 | -45.78962 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e183ab59-14aa-3ea9-984b-bfe78d3c8d11 | -7.6548 | -46.72323 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62f5c41c-8d2d-3909-84c9-5842d1503c5a | -6.3796 | -51.75849 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ce2ddfcf-4205-363d-acf1-7e97e6aaa3d5 | -3.62352 | -60.56894 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7093d733-1dbc-365f-ab2b-05ce981a14cd | -3.63062 | -60.56508 | 2026-09-01 04:40:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98c5b753-7a41-321d-abd4-8fcfc87e04f5 | -6.13237 | -56.38359 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0546287-b124-3faa-964b-1cdcffbfe5bb | -9.71924 | -48.13812 | 2026-09-01 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac309423-2129-332e-b04d-a5e3c8d12d78 | -9.19079 | -59.44857 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3c552be-6f70-3731-b02b-cc8d5498becf | -8.62212 | -54.855 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 24f089f5-5f78-3875-97e2-2025c3eca369 | -11.48416 | -45.08058 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0fba6f5d-cae2-3841-9cf7-d967d0985eda | -6.93408 | -55.62776 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ce616f7-4846-3397-86fc-e2cd37d716e9 | -10.75572 | -54.06922 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec961bcc-e5d7-31bb-bc08-1663098b6db3 | -5.94621 | -57.68201 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9083892-de18-3d10-86ce-4589ad4a7cbc | -6.94055 | -55.64116 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fce6596-34f2-3b14-bce8-b612e28e7c39 | -6.95114 | -55.63055 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7de1e42-01d3-3801-8708-709726c75061 | -10.69073 | -46.25735 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab175cf3-d1e7-3d33-b86e-33d72cb84306 | -10.36201 | -50.00661 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 956aa789-cc09-3754-a7ee-b6a694c7211c | -3.83367 | -55.56362 | 2026-09-01 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16c9aed5-98e6-3b3f-acad-b49777e9b0f3 | -5.96309 | -57.6734 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec96f353-0fde-3830-91af-b02883c34465 | -11.15218 | -45.04667 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ac83c5b-28cb-3a81-ad05-aad86bad9504 | -6.92993 | -55.6321 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1615290-87ef-3d0b-b77e-2ca23db22ad9 | -11.67068 | -47.61393 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25673463-c535-3e41-8e28-31566347d3b1 | -9.43675 | -45.62942 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c2ed34be-aad0-3656-8d5b-66b7c721bc75 | -6.55956 | -58.55964 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18735e90-fae4-3382-b3cd-2042374a26d8 | -11.91373 | -45.06412 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ae6ac20-287a-3395-82c9-68a63d19f146 | -9.89225 | -60.28526 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 334c1645-96fd-3cd1-ae44-59a8de169264 | -6.25099 | -55.4305 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86d7a3d4-fae0-34a8-b2c5-f650aa7d76aa | -10.92018 | -50.61581 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ab36391-3ab7-39e2-ac97-3db7a4362db2 | -10.7447 | -54.04503 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f395939-3639-3676-bea9-3c493edabc0f | -11.19642 | -46.12951 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7734dfb-3937-36a5-9285-41bb92e58748 | -11.22841 | -51.27333 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 989b5f78-ff64-3758-b853-cae7ef6df01e | -5.48605 | -57.15591 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de0d6f10-ea63-347e-b364-081fb0d1121e | -9.40353 | -51.60395 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b1df999-0156-33c6-824b-901889d265fb | -10.74614 | -54.03637 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 520002bb-7b43-3f78-b762-7e41c3cac336 | -11.31087 | -45.185 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 728eb5a9-88a2-306d-b662-a809c9c8a8f4 | -6.80526 | -59.57156 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 609cd69f-eb33-3d3d-8b05-c71abc817c44 | -7.30705 | -46.99213 | 2026-09-01 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a1ee88e-2a87-3829-af7d-117e3cc5d6ec | -11.26322 | -45.1167 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9567712-7682-3f8c-a0f6-509b6d84ae6f | -6.90616 | -59.48475 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a7f2e91-4432-380e-b0fa-054107dd2c38 | -11.32181 | -45.16677 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5368d1f-d33a-3006-9786-dbd922654060 | -7.89276 | -44.24221 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18a3f3e5-2d4d-35c6-a8b9-75f71ea6b496 | -7.63317 | -55.2906 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e655ece-c266-3152-8164-6a657ed7df4f | -10.38579 | -54.54128 | 2026-09-01 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38b42464-9747-3777-9a2c-5c9aee56d033 | -6.10504 | -57.86639 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b78a50e0-e340-33c2-b23c-2c41fdf8ccba | -8.00816 | -51.81077 | 2026-09-01 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce3b0bb0-1640-3866-bb04-e8f8bccd6fae | -9.46826 | -51.578 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab2e547e-5c08-3d5d-9fd4-b08eaee0b1e5 | -10.7839 | -50.50752 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c1af268-5725-3445-916d-aa66fa137eb8 | -5.60342 | -43.99818 | 2026-09-01 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 861ed08f-3602-39d5-8037-eb4c3bc3410a | -8.27041 | -54.93198 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 331cf89f-d08a-388a-b9f1-ae47d0ff973e | -10.0083 | -46.44125 | 2026-09-01 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 250f998f-faef-3278-b222-23dae7eda69b | -9.15486 | -59.54375 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce5c8edd-a4fc-3ff3-addb-fb7b1d44f6b6 | -6.72628 | -50.46603 | 2026-09-01 04:40:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08bf4032-1b1d-3926-b4f8-75b9a50cbbd3 | -7.35119 | -60.59204 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 449a4b2f-3f83-384f-9531-8adf9e91f173 | -11.3166 | -45.17389 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4aca2923-1c2d-3d5d-9625-22e31cac1443 | -6.60101 | -58.60031 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a31141a-b2a3-3424-bd9c-d09795025a4b | -7.34097 | -60.5812 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3623f4d5-a737-31da-b03f-9e3b026a09c1 | -9.16625 | -59.37218 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 360ab463-01d1-3003-886b-b4ac2e3f4e18 | -12.06553 | -44.99408 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b084e64-c716-35bb-af88-3e7098071c3c | -12.06972 | -44.99514 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8c82293-b67c-36e7-b69d-da305c60189b | -7.41486 | -49.73949 | 2026-09-01 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 513262ef-e43e-33bd-a0b4-310adb9ac704 | -10.74172 | -54.0178 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e27950e-8da8-3231-b106-6f3c4ddd6ab8 | -7.34446 | -60.59566 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a10ab79d-dd77-3741-b74f-afc284d04efa | -5.54158 | -46.60238 | 2026-09-01 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1613ec74-a2eb-3f6a-9a61-c13239e1066f | -10.74176 | -54.04009 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7c4b798b-0c79-3fd1-9262-b0f5d830b314 | -10.41649 | -57.2301 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2c3616b-0ffa-388c-85cb-45f5fc129b1f | -3.61268 | -59.06514 | 2026-09-01 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 23fab381-bf89-3eeb-86b6-c5f8cea5959e | -7.9328 | -44.23238 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acde57c3-1a09-380d-9f32-c40f4122e015 | -10.45258 | -46.7386 | 2026-09-01 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 774d50e1-39ab-30a7-a297-8bce94330fb7 | -11.35802 | -45.41706 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c81e42f-5307-3579-84af-72bca5fcdd72 | -5.49367 | -57.1406 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99c4f3be-39c4-3046-ae37-8d9cb891c22a | -6.78367 | -55.6746 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25264f21-ca5d-3d30-9681-e3e497bba2cc | -9.89292 | -60.28161 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aa39678-445b-3133-8747-58cab54f50e2 | -11.06872 | -51.53011 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97248071-7210-335b-8485-d751818d6507 | -11.27163 | -50.58611 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8520c87-617b-3208-a66e-8ec14354b475 | -7.62241 | -57.61477 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bfcd8ec-8657-3a63-9200-82e76e7a80aa | -10.15927 | -45.7591 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0da4eb66-f3c0-3779-9ddd-3bad2bf2e734 | -10.05212 | -48.69765 | 2026-09-01 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e04868a8-70b0-33b5-a94a-e6440e461060 | -15.01106 | -48.16044 | 2026-09-01 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff71766c-354d-3630-ad7d-1e867df51611 | -14.39262 | -52.51134 | 2026-09-01 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0248a4b9-1fcc-3a45-8da0-feb7eb34db46 | -15.63329 | -56.3847 | 2026-09-01 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14191b81-9335-359f-bc8d-3bd5421b8879 | -15.42951 | -52.68581 | 2026-09-01 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 945a1e66-5df0-34ed-bca1-ec6dc3c4d903 | -15.24789 | -53.88574 | 2026-09-01 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dd3d47b-c90f-3334-984d-3ce464a6379e | -14.72024 | -53.56847 | 2026-09-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3e12b37-7411-3b66-88c2-299dc1d7cffd | -14.48998 | -52.21994 | 2026-09-01 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
