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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0e0e813-7e36-3fbe-99f5-e4025624d6ba | -9.39768 | -50.16508 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 07d52ee1-84bc-30af-be2c-1333b8d0849f | -11.83451 | -46.39408 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8213da2-2cfb-3bd0-ad85-82c6d7a13ed6 | -7.96459 | -43.98604 | 2026-09-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7576a119-5be7-334b-b65a-76d39ce57a3b | -6.91265 | -55.63361 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26dd8e5f-d3cd-3694-8303-8ce581883773 | -6.79444 | -58.78651 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf1a7b9e-604c-300d-bedb-a1375f875591 | -3.90934 | -55.73439 | 2026-09-14 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05a2a894-a512-31e4-87fb-f70d4ea4cca3 | -10.43611 | -48.65855 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bba06e7d-3ff3-39f1-9af4-03ff011ddeef | -7.83263 | -47.93678 | 2026-09-14 04:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f4621e8-1a1c-34d8-a131-6b8d845d6656 | -9.40165 | -50.16191 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ca2e02e-f85a-3f48-a8df-9625f340aa81 | -3.8127 | -55.89216 | 2026-09-14 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1fd973a-a31f-3698-af27-32ba6c7e74a7 | -3.18343 | -61.11755 | 2026-09-14 04:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 182e99b6-8e8d-349d-8f1b-946ec73343f9 | -7.07599 | -41.80331 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6bbfce26-6c85-37e2-9879-2ac9f482439f | -6.31045 | -55.28616 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b1830d4-7f33-3f87-a925-02604a62d630 | -6.58273 | -58.84577 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a86772e9-d4a4-30ff-b74d-e4eb0e46bb4d | -11.21619 | -46.41805 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c67f0653-3e02-3167-be39-953c8c96959c | -4.53636 | -54.96888 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65a0bbee-488f-3d4c-8046-fa78e9be0491 | -4.77822 | -56.15363 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7a876df-b7d3-3264-a8ed-3946f1e22427 | -9.69684 | -54.34326 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 041b6d9c-5154-3c40-aa10-c12e3a161e33 | -10.55022 | -51.31318 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd7619e3-4765-3a79-898a-a5bcdd5f4a3f | -5.84041 | -52.0567 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b4bc533-b67d-3d10-9e83-fef916fa668e | -7.14617 | -55.29939 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d55916ea-2b68-3eab-840c-aaabb83119a4 | -6.74341 | -50.92719 | 2026-09-14 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eca02cfd-7b55-33bc-83b6-4186d34699a8 | -6.66285 | -54.98372 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 465c9996-7c9c-382c-9a8b-b045f2e036f1 | -6.28895 | -56.02684 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bfa1afc-1229-3154-b41e-b2b89416985a | -12.85288 | -44.38725 | 2026-09-14 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb774082-9495-38ce-8c57-543575826c3c | -4.56859 | -54.9101 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 660eac56-851e-3727-b714-a2714a53885f | -11.21506 | -46.42627 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c823571e-5ca3-35e2-830c-41fa3eb386c6 | -10.65661 | -54.13895 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ada41f7b-ef43-3d16-9504-a7f17a8a6bbf | -9.44087 | -50.13388 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48ea1992-93e9-3633-9ccc-9959890d446f | -10.46513 | -51.24514 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b26c7d16-7181-3cab-9966-b14da77fb4a8 | -7.01814 | -44.64682 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| affae98d-c8f4-3a59-b0b8-9e62ea3e4c15 | -6.59093 | -58.85431 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 728fe2f2-c6de-3253-bf8e-1456e955113f | -9.13138 | -51.56995 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaceadbd-e0a1-37ba-98ec-a0abc2333089 | -6.8678 | -55.2922 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b82022b-89f0-3eae-9333-68488d663118 | -9.39314 | -50.17195 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5446007-ff48-393d-8126-0a19f4ce8d26 | -5.12895 | -55.9507 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2c1a92a9-2caa-3c7a-b439-8eb96b526277 | -5.77299 | -47.17022 | 2026-09-14 04:53:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 772001e4-74ea-35e2-9127-07c2f5cd57d0 | -7.01618 | -44.62794 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 252b3a01-1f2f-3298-bc65-e8e7064ec91a | -4.39833 | -55.23266 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e32af630-e973-3b83-85b8-4d8f9fb8bf06 | -6.85736 | -50.80649 | 2026-09-14 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 056bd69f-25af-3692-bc73-563aa48de863 | -11.18318 | -42.80658 | 2026-09-14 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87131b00-9b23-3240-b945-8251cf454d56 | -10.69773 | -47.52864 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 265f22d3-24c2-38db-b76f-e83db600da38 | -4.11562 | -60.68409 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ec94004c-2ff9-3f33-a108-96592fa0c4ae | -6.85621 | -55.57018 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d880daf-e324-3e5c-9dcb-88e91349cf4f | -6.29227 | -55.27822 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b8c82b1-c59d-3733-a448-e3db172e9808 | -9.14077 | -51.57501 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0d3249e-1ad5-3f96-b6a7-2f5bf74dc271 | -7.8749 | -54.72696 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad400317-8fc1-33a2-bed0-32897b851ff2 | -9.19446 | -60.39189 | 2026-09-14 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd2ff881-5bbc-3c6f-a4d2-ded281441568 | -6.62393 | -58.37998 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b66e4c4-ae14-3b3a-bb51-ba2349f33045 | -8.54513 | -54.70871 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fd64f6f-2b82-3dc9-aaae-cdfa6dd4748b | -10.43061 | -48.6447 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 45bb8607-d720-36a7-b729-b99b2df13572 | -8.33911 | -50.75588 | 2026-09-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83ae7c9b-c299-39a3-829a-101937ffd8c5 | -4.12188 | -60.6813 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 76522687-6f31-33e5-95a4-ef040159dc54 | -9.32732 | -44.36451 | 2026-09-14 04:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83b8d373-5a76-3615-9ec2-a3c208137bc5 | -9.13414 | -51.57396 | 2026-09-14 04:53:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 699d654e-3346-3973-bda8-f4639de66a5d | -10.47069 | -51.25344 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 741e8089-26a0-34e1-8826-49eed35edbd2 | -10.17723 | -48.07048 | 2026-09-14 04:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c0d8715-d072-3d48-bde6-764d91e242d1 | -5.0868 | -56.2533 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6776ac2-a0ee-3b3d-868f-1310b6eb878d | -9.44769 | -47.85677 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d69c25e-699b-3694-892c-38c8e99c9088 | -4.36201 | -55.0361 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e46be445-1294-3496-b945-2647b88b1d87 | -6.37467 | -58.29996 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29d28359-83f6-3c0b-a35f-29011029908b | -5.84378 | -52.03556 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1147401-79f4-3b67-8ff7-bd5a4e28c022 | -3.40948 | -58.20745 | 2026-09-14 04:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5c384a5-8e5b-314f-8369-bb6aa254e004 | -10.41182 | -57.23139 | 2026-09-14 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c6551a7-ed06-3adc-85b5-26fa6c07f132 | -4.11314 | -60.68267 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec7bdc1b-84c5-3c71-aab4-1e729d381aa4 | -3.69807 | -58.8794 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 281afee0-bec3-3fc4-80af-712170ba49d4 | -8.53661 | -54.71573 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd1ef849-0af2-33ef-92e7-442e02164dc8 | -5.13349 | -55.95394 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2e685fd1-8ba3-3457-bd04-2693aca9ab03 | -7.1018 | -55.63618 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 588e6278-c9c4-37a8-9cf3-ffba2059b686 | -6.29456 | -55.28792 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ca173a-416e-3a3f-931e-f587344584d5 | -4.11498 | -60.6879 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2ddf6383-628a-3144-8610-c3d3af3f42f5 | -6.28888 | -59.93845 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bca062a-c1a3-38e1-889a-78ac95de2056 | -6.79831 | -58.79236 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fbaa7e3-8a19-31a9-8423-3333a53923f2 | -7.09035 | -41.81964 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f95a00a8-6629-3820-9120-352da3cc10e8 | -6.77479 | -48.66232 | 2026-09-14 04:53:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 232a02e3-a326-37f2-989e-4697395ba1b2 | -11.23354 | -43.4502 | 2026-09-14 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d125023-f9b5-3abf-8da7-5dc59e8ffdaf | -6.59385 | -58.86558 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 432d4943-6421-3bd3-8a77-cb363dc9fe1a | -10.06704 | -48.78144 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbb07574-1409-3348-b23f-473b31226355 | -4.36585 | -55.03669 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bdc78a3-473b-3998-86f2-d8611498d5f8 | -5.80414 | -52.11223 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 369eb0b1-7392-336e-949c-4e88d83acf00 | -10.1069 | -48.86833 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 011a8e98-c928-3a54-af6b-b5406be38f29 | -9.00266 | -49.53947 | 2026-09-14 04:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 083fd8f5-f4c2-3685-b1fa-99c7dcad92eb | -6.37654 | -55.26033 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1e0edba-8f9f-3f46-9836-410383bf7705 | -3.59458 | -59.06882 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 033262a1-4d89-32f0-b5c7-6cf187b7da2e | -3.71508 | -58.87038 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 353ffc5a-47cc-3e40-9def-d4b9767586bc | -6.28409 | -59.92658 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19052122-705f-3668-b0d5-bd9b829ceb06 | -10.66624 | -54.14447 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 8c9be444-9f3e-3f53-b1b0-225cf136113a | -6.29606 | -55.27886 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6142fb14-23b6-36d7-99fa-8f62b1a0529b | -10.665 | -54.15196 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 30e9c122-f6b9-3a55-a455-71a643390238 | -6.29586 | -59.951 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9aa8f707-33dc-31ba-a66a-64e4085fddd7 | -10.17369 | -48.06791 | 2026-09-14 04:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd8f4e9a-16fb-3431-8d6b-ea3e0a4571eb | -10.66096 | -54.15512 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f7b5a23e-a36f-3e98-9543-966cff2afbb3 | -9.42271 | -50.11586 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4949015d-05bd-3d59-adba-4e288556d30d | -11.22414 | -46.42341 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 341457cd-6cc4-3e49-8fa7-5a033a092268 | -9.43861 | -50.12593 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7f9e70ae-3a00-3171-bb5e-b57ae4223cb1 | -10.77183 | -53.12979 | 2026-09-14 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a16afd7a-33db-3792-b05d-6ad20dd7b206 | -10.47458 | -51.25034 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0bf7f6d-69e2-38eb-9635-103a0f295429 | -6.20076 | -53.08983 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0aa7bd4-409a-3f84-9d23-346fc9724ba5 | -6.28766 | -59.93671 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0edf4d4-f23b-3d55-8154-1126fa3b561e | -11.42687 | -45.13893 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README42.md)
