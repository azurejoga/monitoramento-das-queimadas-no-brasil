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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a06fc23e-0e35-3d73-ac26-1146513f8e32 | -8.93281 | -62.36959 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bee7e339-74b0-3b2b-93ee-4832657588e7 | -7.73352 | -60.97152 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de6ee98d-ec0d-33ab-8d39-77fe753ac5db | -8.21534 | -61.48092 | 2026-09-02 05:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048ec8f2-192a-3238-bbbb-b7e27360222c | -12.14099 | -47.06408 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc33f08b-df05-38e4-bab3-aeda2f57e15d | -11.29851 | -45.18394 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24ffec73-6584-3629-a8d5-cf0c7f54dd79 | -10.90357 | -45.3287 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 5d6b47c2-5038-39ac-b343-e97ca1328747 | -12.14679 | -47.12584 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 410cda45-377e-3822-9ff4-675bf7bf42fa | -10.39236 | -49.99884 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| becd17d8-1197-3c68-97cb-f36edfe3358c | -7.6927 | -67.1272 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b93afb8b-4adc-3420-a12f-30064b6293e6 | -11.12518 | -51.53251 | 2026-09-02 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe4249be-e4ff-3645-8d8b-7b49670ed5d6 | -10.06218 | -59.40761 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f0a7c0b-e676-3bbb-a379-63d233acda00 | -12.1393 | -47.0791 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| daec2684-5ba2-3ab6-b382-52f4f0efcb58 | -8.75979 | -62.58577 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| faa63355-cf6e-3dab-a711-7c307ffde93b | -11.65277 | -50.19701 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e1578e4-8800-3b42-896d-ffb14a8b437a | -11.33856 | -50.6274 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0442adc3-e7d2-3f2e-b71c-f3f8afd41c31 | -10.86349 | -45.36758 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ea6834a-1ece-3236-a9bc-2737b356ab7c | -8.78513 | -69.01807 | 2026-09-02 05:18:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2adac702-2b1d-3f08-849a-b17f3dcf3c69 | -9.44207 | -67.44937 | 2026-09-02 05:18:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3f726da-3185-3119-9d0d-8bba0f288190 | -8.90688 | -62.36025 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1beeb038-d34b-37e7-bf70-1e131dba37a6 | -7.76351 | -61.19969 | 2026-09-02 05:18:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a4bdce3-7507-3ed3-a6be-6c867b97c070 | -12.11985 | -47.05079 | 2026-09-02 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3750c07d-b6b9-36ac-bc5e-f2bcbb659a2c | -10.99459 | -45.0762 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1acb1674-9e04-3f0c-9048-b46dea152432 | -9.3951 | -51.60594 | 2026-09-02 05:18:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 642ff3dd-72f5-335c-a5a2-046aa60c54fd | -10.78773 | -44.75826 | 2026-09-02 05:18:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5ccfd077-a899-3382-ada8-88c66fd23c00 | -9.57232 | -60.63143 | 2026-09-02 05:18:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5f2969e-7125-32d6-83ee-c4b13767008b | -8.90306 | -62.35958 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a51dd1e2-ed2a-32a6-aaa3-1cae7a891a07 | -15.67848 | -45.89682 | 2026-09-02 05:18:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9054c9d-8022-3cc9-b822-17c7d308f89e | -9.92572 | -67.84678 | 2026-09-02 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c9ee51e-8a63-3b2d-9e72-0fd5d4a3ca6e | -12.00946 | -60.53235 | 2026-09-02 05:18:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d6d7eed-ff49-3f21-a5e0-c72f4abf5e48 | -11.30164 | -45.1463 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5f33769-d773-3500-b84a-c744ad086a98 | -11.83452 | -46.0555 | 2026-09-02 05:18:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 067c5d16-e106-3b24-ac6a-2433fc3208a0 | -10.96501 | -50.48007 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04c44ddb-0c9a-3e05-a480-2e6ebacc2d1b | -11.29544 | -54.062 | 2026-09-02 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e3d22336-1cf7-3731-889b-63f222bb63ed | -11.66415 | -50.18921 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2f79d5e-ea5f-3365-b8e1-360779671deb | -10.78253 | -50.47662 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f42c76b6-a267-340e-8e75-121d1fd03f62 | -9.93172 | -67.84444 | 2026-09-02 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3892a944-3fdf-3894-bc80-0da292be397b | -9.39277 | -51.68733 | 2026-09-02 05:18:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fff61ed5-5d0f-3948-afc3-3330a7391da1 | -11.30789 | -45.15393 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 49c59294-0a5d-3e3f-b3ad-9e8cf4dd93fa | -8.99967 | -65.43321 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd6c8dc-02ef-3c2a-bcd6-3ef81d6140aa | -9.92898 | -60.48813 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4df3257e-00a9-3aaa-a865-6b1a301d9085 | -10.43865 | -67.84411 | 2026-09-02 05:18:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 030b9803-e007-3608-b8c9-a835e91bb2c8 | -8.87088 | -66.82117 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41b4de53-9e40-325a-a0b1-cb08ff988ee6 | -10.75489 | -54.06478 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 073bee44-41b5-3dd9-89f7-1e48ce2dad48 | -9.70163 | -47.21006 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91b68662-cf68-3758-9e41-703d621e7918 | -11.82415 | -46.06256 | 2026-09-02 05:18:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 092c70c7-2cd7-3d7f-93a8-f5fc82b878b2 | -10.96921 | -50.48643 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d61b705a-5dc6-3101-be45-4ec3104d12ea | -11.3491 | -45.41268 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2f1a1bd-dd06-3e77-926e-d7af08571e00 | -12.14979 | -47.12104 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a00151a8-98e6-3455-9c80-da735410d925 | -10.74358 | -54.03259 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6b390cb-c8e1-3399-b937-f0962ec6a004 | -9.71579 | -54.33669 | 2026-09-02 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43c02144-82d1-3316-9af8-8b521bca6fdd | -11.03714 | -54.10746 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30598222-4297-38c2-af98-86ff1d01a558 | -11.30853 | -45.14812 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59f8793f-247a-3871-bfdb-8df0c560fd2c | -11.00243 | -45.08452 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8d66674a-bf3e-33e8-83d3-f493da54a05a | -11.04249 | -57.21449 | 2026-09-02 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 912048fe-bebe-3096-ac0d-4c7525857217 | -9.92688 | -60.4949 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cc60990-c86e-3eca-a132-f0287cd39ad4 | -9.47269 | -57.03449 | 2026-09-02 05:18:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c2692b7-73d6-33c1-8313-9881bf1c10d1 | -10.40173 | -50.00621 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b93a5920-d118-34e1-8764-005e1ada5ca4 | -10.43992 | -46.74004 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9172afc6-91c0-36ad-885a-539b8683c40b | -9.72219 | -47.77151 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14092e17-1a39-307f-b46b-13f4ffef34fc | -10.13615 | -55.89708 | 2026-09-02 05:18:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3263dfd-9d14-3292-83ce-afd8175912fd | -9.94868 | -53.98986 | 2026-09-02 05:18:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 521adc01-966a-3aba-95d9-f9586bae1e69 | -10.34973 | -49.96863 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2cad407-e6ed-30cd-8998-52a6bcc6685e | -11.29775 | -45.18174 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ebf1cf7-b9a4-3012-91fa-6deae7b96f14 | -11.30885 | -45.15604 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d3f55804-d679-3a49-85f9-73721e115ace | -9.00521 | -65.42916 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec8900e5-caaa-34f5-a35f-29e1ba42b3e5 | -11.0505 | -51.52694 | 2026-09-02 05:18:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 122e0c4e-eaae-3389-91b0-c7b1ffc7ae1d | -12.13198 | -47.14421 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3ecacca9-1cd2-3e87-9b9d-a78d3a5e2605 | -10.97059 | -50.48196 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06e11bb2-3d14-3cf7-a792-42bb5eedb9f4 | -11.66671 | -50.18884 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3415e1b-3e76-3384-adac-61ee6fa8620b | -10.67346 | -54.04641 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3d599297-d07b-386f-8df4-1dd164f3d664 | -9.70366 | -47.20335 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daeadf1f-5ac4-34e6-ba41-792c0605d72a | -10.67807 | -54.04202 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c3fa422b-f93b-3257-b609-1f9c59211fa0 | -9.7031 | -47.20792 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b01385-e7e3-3e21-9c8d-c0687e91f665 | -12.12556 | -47.08778 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3799fd25-f694-3e0e-b3fd-059ec7649198 | -12.14163 | -47.11505 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2096a98-1c42-3901-8c56-bd2ce37098c7 | -10.99623 | -45.07688 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 490c6bfb-04cf-3f72-ab24-8887cacb8015 | -10.04377 | -48.69285 | 2026-09-02 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d5cb83a-70ab-3c2e-b151-c2e96c03946a | -8.90005 | -62.35416 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84c5bbec-f90a-3580-9d5a-3e52bb4ea1ef | -10.90331 | -45.32677 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7f7556a2-16ec-39d1-a8b8-ede4eea1326d | -10.40486 | -50.00733 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c653972d-c7dc-396b-ba13-ee05a1cf974c | -10.43612 | -46.7187 | 2026-09-02 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1ab609da-c2ee-3063-93df-ef33f32933c4 | -10.99382 | -45.08311 | 2026-09-02 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3fec643b-8616-3bd1-aea6-6b7f5729383d | -10.96562 | -50.48129 | 2026-09-02 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 273d3151-5b92-34d3-9aa2-0a4290fef9b5 | -12.63077 | -45.07608 | 2026-09-02 05:18:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 82b524a3-a31e-32c4-9bfd-9ff76437ef15 | -8.90989 | -62.36565 | 2026-09-02 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7166ddc-81b6-3cb9-a9a2-23c62660a305 | -9.92774 | -60.49574 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd98747b-bdfe-361f-b5f3-c547fae0623d | -10.78146 | -44.75004 | 2026-09-02 05:18:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 09735505-a67d-34c2-86f0-581f5d9083b5 | -9.10708 | -63.97632 | 2026-09-02 05:18:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cc087d7-ef31-3958-a269-3ce5c7ffe555 | -10.75738 | -54.07516 | 2026-09-02 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42317725-afce-36fb-9403-b7defc58701c | -10.41072 | -50.00201 | 2026-09-02 05:18:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c31026b7-a478-36b4-900e-3a4b58cd0496 | -12.14052 | -47.14521 | 2026-09-02 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 96f82128-cc04-3774-9279-bd50f041bf53 | -7.68569 | -67.12231 | 2026-09-02 05:18:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a68849-fae7-301c-8afe-43c625b4e2b0 | -9.68828 | -47.17803 | 2026-09-02 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ba5912c-69ca-3437-9f90-36d773700704 | -11.29616 | -54.05692 | 2026-09-02 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cece29b-ddc4-3dbd-bfd3-ead9f865e33e | -10.50038 | -59.62199 | 2026-09-02 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3014847d-6b63-3b90-9d11-914a1218f8e1 | -14.97576 | -48.12025 | 2026-09-02 05:18:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6555f763-a0d3-3958-b07e-8b679f4bfae3 | -8.61383 | -54.82665 | 2026-09-02 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca1a1bd-68fc-359f-85ef-03bcbc839c3e | -9.00875 | -65.40945 | 2026-09-02 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85d19a60-aace-30fe-91da-fb06767c6484 | -10.6818 | -52.50619 | 2026-09-02 05:18:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a7b21a1-5895-3d1d-acd8-f2b955419cf2 | -8.61683 | -54.83138 | 2026-09-02 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
