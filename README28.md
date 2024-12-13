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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31f72999-e5aa-3b3b-80ba-04fb580aec67 | -12.02929 | -49.5502 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 862241bf-2f4c-3b1e-b34f-71e35e28ed30 | -12.01984 | -49.53725 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc50da41-73ce-3e26-9c4e-331f2aae89c9 | -11.68817 | -48.0732 | 2024-12-13 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2296ebfd-5012-3133-8227-116407b9f25d | -12.53419 | -57.72231 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ea1c77-e0fc-3005-bc3f-1b126e37b252 | -11.78197 | -55.12992 | 2024-12-13 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c0a9cb-3915-333a-ab4a-0759a3934aa9 | -10.23288 | -49.4827 | 2024-12-13 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae427844-6e73-3eba-a3f7-fdfd81434477 | -13.65485 | -55.24591 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01afc80c-048f-36a0-b99f-475259e805eb | -10.21498 | -47.58078 | 2024-12-13 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be329b90-16bd-398d-b56c-cbb6687b66b5 | -10.65973 | -44.71939 | 2024-12-13 04:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6825f4bd-a9f7-3305-b648-958029a362e1 | -13.69168 | -54.76 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a88f5b84-8046-3382-9902-799b913b2fe5 | -8.2674 | -48.03096 | 2024-12-13 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bd70fd4-2d45-311b-aa2f-dee8b00c2166 | -11.43469 | -55.89378 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0138916d-87b0-3e97-a2c1-0ecf574b5c47 | -11.11064 | -54.65132 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c8ada7e-dfb6-3df1-a4e7-09a68eb8faa3 | -13.06727 | -52.04097 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f5dc72b4-34e6-335b-8269-1b7a319c5ea5 | -11.68371 | -48.07733 | 2024-12-13 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebc820cb-8de2-3b6c-aa20-9bcca417d2a0 | -11.86319 | -46.94841 | 2024-12-13 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b182f5a-ff60-3e8a-af01-4e09dff3ade5 | -13.69386 | -54.76833 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6e9100a-d6bc-3b1c-aeca-7817b80b665e | -11.4362 | -55.92426 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32d4b324-9209-32d8-81cc-239c15d3a7a7 | -10.64875 | -51.65989 | 2024-12-13 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e300c0bf-5083-3d17-a37f-8490b2cd4064 | -11.44072 | -55.92032 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de80d768-281e-3ce8-89fd-af4651e675e0 | -12.50962 | -57.8388 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 54fb20e9-76f3-3da9-b54b-4baae21578b2 | -11.20642 | -53.82502 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6fc1172-2b73-3e39-9ebb-6514131a5d89 | -12.53781 | -57.7406 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1d2db01-2ad1-37c9-9132-72c96414149a | -12.74947 | -48.34561 | 2024-12-13 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f578b787-2f34-3e5f-92d4-2315a2bd2592 | -11.43365 | -55.92188 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0827a09-f4cf-355a-9e91-ef9e6c8230fb | -12.74882 | -48.35024 | 2024-12-13 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b10128cd-7047-39fc-b6c5-de6a75004053 | -12.28661 | -50.08224 | 2024-12-13 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5272613-23c7-3d4c-8e08-885c3784d464 | -13.37557 | -54.24851 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f93943fe-4d13-3728-a4c7-8e0e024c5c93 | -11.43783 | -55.89149 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3658b7e-63e6-3d33-983a-a95105aa7f48 | -12.5357 | -57.73799 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 664caf78-05d6-3989-b5d5-b546cc9b3963 | -13.6619 | -55.24715 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac71c057-da68-36da-a32a-01e32c96ebd3 | -11.47857 | -48.21767 | 2024-12-13 04:44:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01ca5446-a403-3f64-8821-4266f4d7920d | -8.29548 | -54.86205 | 2024-12-13 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d36fbf74-7665-3c08-884a-ab0bf2cd6a5c | -11.42498 | -55.92221 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 899ca65b-5b3a-389d-a6a5-59f9f3ac2765 | -11.20862 | -53.83307 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b9a3a68-407e-36ec-b7c3-8d9291f902b0 | -13.66542 | -55.24778 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b95586d7-c5a4-389c-bf56-6ee29fa1cba7 | -13.05677 | -52.04289 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06ad3a9b-4bbd-379b-8ded-1fc2a645b4df | -9.19822 | -49.47891 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 854c5216-10d0-3a57-b060-3ca2e0d15021 | -8.40302 | -49.70945 | 2024-12-13 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93e78ae3-de57-3193-9ed5-2c217ce1ac8f | -13.39991 | -51.07486 | 2024-12-13 04:44:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d73a146-a5a3-3bbb-a948-88554e11dc57 | -11.20362 | -53.82072 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ee65b34-a6f3-3cf0-9b7a-7e1000a53d1a | -11.43842 | -55.89446 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5578f9ac-a6ab-3ed1-84b7-12118df13107 | -9.17073 | -49.47472 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dbfc5642-0e51-35e1-83c4-b098224baeaf | -11.49708 | -52.92667 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 019c53d8-66ef-3560-be27-bffb8d32f74c | -13.69605 | -54.76785 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59f6208a-c691-3925-9115-cd03e71e8886 | -12.51029 | -57.83496 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| babb7d05-683f-3269-906f-e9cfa4a5382e | -12.35141 | -44.71571 | 2024-12-13 04:44:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad9e3c9b-4ed5-3ddd-9c34-6be39499cb31 | -13.6945 | -54.76447 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acf692e9-4feb-30b0-929f-07ecd970cf7b | -9.72771 | -48.02959 | 2024-12-13 04:44:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5ca3883-1705-3b41-ade7-f60346dcb75e | -13.68886 | -54.75553 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fbe0b21-7438-3be5-a5c9-223792c2a1bb | -11.20703 | -53.82129 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d6e42e8-6053-33c3-bce5-dc0bd2918dc0 | -12.0199 | -49.54063 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45579e35-b4d3-33dd-9356-efa07a531a48 | -12.53232 | -57.72411 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3d8e583-fb61-3891-9b10-1d24f7db933d | -8.16408 | -43.82507 | 2024-12-13 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7ebbcd24-73a7-3137-8dc1-174e8f1d40a1 | -13.06672 | -52.04451 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47c152a1-2050-36a3-9930-27269be090a3 | -13.37216 | -54.24794 | 2024-12-13 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb205665-2683-337b-bdf3-3a2b763a1e0b | -13.05732 | -52.03936 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b6149ed8-50c9-32e7-961b-14153f25b89a | -10.2638 | -51.49454 | 2024-12-13 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e139629-22d4-36c6-b1db-88c0fdb81b2a | -13.06837 | -52.0339 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d1f406e-3671-3fbe-b60a-c14b418168d4 | -11.19618 | -53.82335 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ae17ba1-b723-3ed0-96f2-b472dce39162 | -11.11349 | -54.65596 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18e1dd9b-7c7c-3fc6-bea3-bd83c846ce10 | -12.90134 | -55.04704 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a046bc96-ea06-3ae5-a374-01b29da226c8 | -13.698 | -54.75631 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83067ad6-0433-3b27-8bc3-ad3594050c45 | -11.4408 | -55.89677 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b384233c-3ab5-3c18-b256-01b3b4d88701 | -11.49331 | -52.9332 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20ffd70e-ac84-351d-bae6-d40333ad4e68 | -12.53708 | -57.72122 | 2024-12-13 04:44:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf2d966c-43bd-344b-866b-574a0c743d4e | -11.03874 | -54.07704 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d139d8d-edaa-39fc-803c-9601dd3e265d | -11.49765 | -52.92311 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2db23dbd-4393-3385-8cb9-86dbb393a295 | -13.7008 | -54.76075 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70477668-53aa-3f03-88ac-73e3f3d788c7 | -11.42873 | -55.92289 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fb66409a-8d26-3369-a43e-062ebaa0f54d | -11.48865 | -48.20054 | 2024-12-13 04:44:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f82c9581-8f0f-3df9-96ba-d31c24cc4d6c | -13.6967 | -54.764 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b61772d-5059-384e-90e7-8891363423b1 | -8.95547 | -51.37149 | 2024-12-13 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7984d040-36e9-31c4-bcd4-6302ae808450 | -11.69126 | -48.0784 | 2024-12-13 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5627135f-0947-307f-a2fc-7b9bb55d9ec1 | -11.49502 | -52.9225 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40579157-6294-3842-88f9-522540fb5f98 | -10.53201 | -47.81813 | 2024-12-13 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca1a6f82-d9ac-35a5-b00c-5b77af948f76 | -9.16271 | -49.48122 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 53ecf671-cec9-3d40-867f-52c650fb81b8 | -12.9119 | -55.04883 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d08a58c7-035b-31d9-9999-f48be50964d3 | -9.89416 | -52.1586 | 2024-12-13 04:44:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79d6ac2c-81ab-3e41-83cc-965b09926d21 | -13.05401 | -52.03882 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c8c8ac5-cea2-376c-8626-3b71021aef67 | -13.06947 | -52.02682 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d395cdb7-2020-35be-8b80-0b898f69a238 | -13.68823 | -54.75939 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23c34dde-3e86-3a05-97c9-2bd82fe450b7 | -13.06064 | -52.03989 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f2fd54db-6998-3b8b-9dfe-3237d416d8f0 | -11.19959 | -53.8239 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8aedfe1f-ffbc-3f46-8052-f8b01cd76328 | -9.13697 | -49.48882 | 2024-12-13 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4e2f326b-b400-3f6b-b96b-ac3fd7fb5104 | -11.68748 | -48.07787 | 2024-12-13 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6891abd3-2711-35f7-94a2-0e242edc2092 | -11.43698 | -55.91964 | 2024-12-13 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f342c264-0129-3fac-bdfe-b909220ad6e2 | -11.19679 | -53.81961 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 176217f2-b190-3a90-afb4-656294958fc8 | -12.02048 | -49.53663 | 2024-12-13 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e8b9171-5a31-3e11-9c41-126b8043a515 | -13.05346 | -52.04236 | 2024-12-13 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adf47e50-d835-358f-9421-ffb1c9df464a | -11.20118 | -53.83569 | 2024-12-13 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cf106d5-9022-35b1-8223-5f8b22659f81 | -12.90838 | -55.04824 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4505598-1ff2-37fb-a13b-602106839d4e | -11.68791 | -48.07546 | 2024-12-13 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 442493b7-f266-3b43-ba0c-70ba433ea744 | -13.65838 | -55.24653 | 2024-12-13 04:44:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85ecc4a2-be2b-3cb6-a719-ebdc77209ae4 | -13.6895 | -54.75168 | 2024-12-13 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f982b920-5a0a-3a40-996b-16d674ac3af8 | -10.21048 | -47.585 | 2024-12-13 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c523a24e-319f-355c-a7fe-1eadf754c970 | -8.2918 | -54.86142 | 2024-12-13 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 249e096e-a5eb-3e48-bed2-2fea8e7cef0f | -13.23923 | -53.06017 | 2024-12-13 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48741376-a3ae-3cff-9372-a87e11b9d530 | -11.49388 | -52.92963 | 2024-12-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a06ad01-5b00-32d0-9ca6-f7fb1ca827c8 | -11.94779 | -56.02299 | 2024-12-13 04:44:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README29.md)
