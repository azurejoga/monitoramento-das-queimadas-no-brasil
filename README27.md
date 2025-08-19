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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a41159c-139c-3d54-81f6-898011dff7b3 | -13.01023 | -56.83612 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08e36f0b-d7b1-384f-856b-936c0d94a882 | -13.47666 | -47.06463 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 064ea667-8454-33cb-8365-7f112fbd54b4 | -9.85496 | -44.68716 | 2025-08-19 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7630dacb-64ff-3df7-800a-cf0510a2246f | -13.30873 | -50.81717 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e1bdd6a-398c-3bc1-9ce7-d847ffe1c0d6 | -12.50973 | -57.78386 | 2025-08-19 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c8fae0-7cf5-3dc9-9282-ccf0493ee70d | -7.9714 | -55.30476 | 2025-08-19 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41dcfb2c-030f-3a70-8e0c-b95e91664cc2 | -14.85505 | -48.04877 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44ac4719-48cc-3e9f-8373-dd9de8c3d2e6 | -13.30167 | -50.81628 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 91d1dd40-57fa-324a-8d2a-c90c64890063 | -12.99 | -56.85785 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80ed4ec3-afd1-31ee-901b-8d6178bbfac9 | -10.03668 | -59.35592 | 2025-08-19 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 944620ea-2e64-32c9-aecc-65622c21d52c | -13.31141 | -50.80125 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7062979b-5685-388d-b9c1-086a62d4b494 | -7.25822 | -50.15154 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f4a2d72-ed5f-357f-8b8a-c0b6268a725e | -9.34445 | -48.51671 | 2025-08-19 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28761b7d-27da-3956-bf40-5762f99d2418 | -7.25608 | -50.16448 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 00ef8fe8-1ded-3c72-bdf5-a8099a9f918c | -13.31007 | -50.80937 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a35cf583-8ffe-323c-96f5-04bd5102b862 | -8.70341 | -50.69487 | 2025-08-19 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23ab8548-c9e3-3543-b7f4-7f8fe64f6532 | -12.97682 | -49.36272 | 2025-08-19 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c96e31dc-61ee-3d52-8e55-6abfd2066b27 | -13.1859 | -54.94525 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6dfb73f-4d16-39c5-b09e-957bc675d39d | -12.95713 | -46.12983 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b27b85d9-9322-3efd-ba90-723e7bdc35c8 | -12.97795 | -56.85458 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92d4d188-79c9-31a5-af36-32505339b170 | -13.59387 | -46.99134 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da745f17-5218-3d69-a51d-e99c97e4d10d | -13.58999 | -46.99437 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62e7a5c5-f403-3009-8c13-4192e5843323 | -13.16421 | -54.93631 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 622043f0-5e9a-339e-908d-b10db61d75cd | -13.31708 | -50.78941 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb3afa30-ee74-3c9c-9c1d-7b95dfeaa71b | -9.17753 | -59.62152 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc53d652-0a06-3105-8b22-8f8b283209ff | -7.70856 | -47.36235 | 2025-08-19 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 612e14d6-166b-3359-9b3e-619dac84f59b | -10.6082 | -46.36186 | 2025-08-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2c915f6f-535b-3a64-9aaa-03b6b6a0ba44 | -13.14343 | -57.15471 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a54d4597-8b67-39e6-8cc9-cff1b7f887f6 | -9.18976 | -59.62479 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94c9b19e-7071-3711-80e4-23473b55f59f | -13.85999 | -45.53831 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80daaa5b-45e6-35c8-bf71-f02092a7e39d | -9.34386 | -48.52034 | 2025-08-19 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e81fa636-a8c6-3aed-8cd8-f749ddda9504 | -13.00512 | -56.83504 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4b01d6d-ad66-3983-b308-d51639ec1a1e | -12.9822 | -56.84328 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8958637f-f00e-3675-bd23-795ec2ed39b4 | -13.18142 | -50.79655 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4c38395-9781-3762-b787-456a7873507a | -9.82698 | -45.96266 | 2025-08-19 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef9a7cdf-7697-30dd-9e07-ba12a557c0e9 | -13.25509 | -50.8124 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe2034c6-6abb-37b4-8cdb-444177b75f36 | -13.47462 | -47.06083 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baa263b3-287a-36f4-a13f-1fa357d571ad | -11.74642 | -58.32726 | 2025-08-19 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dda11a9-354c-3753-9efc-fb9e278d6357 | -9.18864 | -59.63045 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 735e0b09-c199-36f2-bef7-dd9f593a2e4f | -12.9994 | -56.83706 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36ab9eba-9817-34a6-8696-c7e931eebd8a | -9.85438 | -44.69108 | 2025-08-19 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9af987ee-8666-323f-8017-f19221585272 | -13.16057 | -54.93076 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e996c662-f2ab-3a1e-8aa8-4367b4d5a770 | -12.98821 | -56.85669 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4fbfcf5e-0b05-3d5c-89ef-1a8cd52abe80 | -9.19413 | -59.63683 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e247b406-6827-32b0-96b8-a27804b5117b | -12.62744 | -46.89057 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e1ec142-8745-3590-9359-2c402becb992 | -10.82924 | -45.04067 | 2025-08-19 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f5b16d6-049a-3714-972f-6f8648a88e08 | -13.16145 | -54.92606 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99776a40-7a40-30b8-971b-762fa34efef2 | -13.13788 | -57.15475 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb8fe59f-3c85-3209-bebe-b28db5962706 | -12.98248 | -56.85882 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7ada961-a50f-380d-9979-207706054a40 | -12.98551 | -56.85359 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18d560da-6d02-3df7-8c54-7368688373f8 | -7.26566 | -50.17502 | 2025-08-19 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e34b559-77d5-3732-90d0-ec09cd4768f5 | -12.99577 | -45.19236 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 646c3f36-603a-3bec-88e4-9ac28e73a930 | -13.86701 | -45.53938 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64e96594-41a0-3afb-b4fe-e97ef1a6cccd | -9.71502 | -51.9663 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 126a24f3-7230-3985-b029-54027dc0e302 | -14.86498 | -48.07227 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bc147b2-3ef0-3a59-8955-be944780f083 | -11.86008 | -51.5793 | 2025-08-19 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1fd4a01f-92ab-3e2f-b46b-51e7bef9ed44 | -13.8635 | -45.53886 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d7f625a-c011-3c35-b109-1d603eb3629b | -12.65819 | -45.81012 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f0f822d-65ba-3bb6-80b4-a752e92f770d | -10.96571 | -49.56622 | 2025-08-19 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c321b5af-d3e4-39be-b592-40be1a433679 | -9.0731 | -60.41822 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8912b5c-537f-34d6-a0cf-a711214af221 | -13.13661 | -57.16143 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c32e94c1-3b3b-3303-a0df-8da4c7f8d6d9 | -13.16508 | -54.93159 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fef58260-237d-3e04-8818-ce5fd2db2fcc | -13.47891 | -47.07236 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31e64dae-e6fe-368d-8fa3-74085d20f934 | -12.99242 | -45.18922 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fb9039b-d3cf-3bcf-b08c-ce9fa8878fe5 | -9.17763 | -59.65165 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7380a5e3-e5f0-3dc7-9443-275ba060e384 | -13.19042 | -54.94608 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc3bd17b-09e3-3cbc-8a0f-62a286f74658 | -12.62799 | -46.88699 | 2025-08-19 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d418fa4-97fb-3621-963e-70543e37721f | -13.4405 | -56.85865 | 2025-08-19 04:27:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f403a56-98bd-331d-8cf8-34557505b42f | -14.86994 | -48.06214 | 2025-08-19 04:27:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db3e1a5-e1d0-3ade-905d-b814ed2c20b0 | -8.82708 | -52.04814 | 2025-08-19 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff1d5455-dcd9-3333-bd95-dbae463b5f4a | -9.3792 | -48.30102 | 2025-08-19 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11d7360f-0a8e-3b22-96f9-25cea870ad70 | -14.16819 | -45.30797 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69628e0d-5325-3b9e-85bf-4ec3f822e9e8 | -13.17148 | -54.94744 | 2025-08-19 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d1a674f-650f-390c-9906-d5fdb0a6b888 | -13.61839 | -46.89128 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df348fee-ed4b-3666-97b5-61406e626b11 | -13.29528 | -50.81099 | 2025-08-19 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3511256f-5d0b-383e-b512-b50cb49b968c | -14.84733 | -48.05478 | 2025-08-19 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91cc945a-21c0-3531-b9a8-00b3026e32d2 | -12.96124 | -46.15284 | 2025-08-19 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 190e974d-b274-3c3c-8084-0f97199ee0bb | -13.48 | -47.06517 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbb1f2e3-3188-36ef-99e3-ae2f28db2361 | -12.99302 | -45.18517 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c655ccaa-ceb9-3315-92f1-38eed256daca | -12.98037 | -56.85256 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72ae9fe8-b2b7-3bb7-ae78-412c725bab34 | -8.50322 | -44.75549 | 2025-08-19 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fcadcb3-8a19-37d5-990e-798ab0de17a6 | -9.17867 | -59.65062 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f7bedb54-71cd-39ff-ab16-fe319b488e28 | -13.86584 | -45.54745 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e3b8c91-ce9e-346e-9b44-3d75de71851a | -12.99356 | -45.20596 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca02990c-a591-38f9-97a1-5c056e1ca293 | -13.74491 | -52.02562 | 2025-08-19 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8c484ca-f3d4-30e8-8b87-1ebd2bb625a6 | -14.17415 | -45.31221 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b79ae0a9-251a-36cf-83d9-9d9f3854d430 | -12.98602 | -56.84005 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc8e836e-22f4-3bf6-8393-a3bb9f79b7cb | -8.18075 | -43.27708 | 2025-08-19 04:27:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae645708-5e2f-300f-b53c-383cdf7d3041 | -14.17114 | -45.31265 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d9da0f6-4a0a-32f5-b6e7-966fadc62dd9 | -9.19613 | -59.63021 | 2025-08-19 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66f0bfec-49d0-3d0b-9b48-9d299e13fe94 | -13.18567 | -46.87908 | 2025-08-19 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8f81dba-d0b3-3424-839a-0234db9c7dd8 | -12.64903 | -45.82439 | 2025-08-19 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc5fdc18-31f3-39ab-a031-e642b12d2c16 | -14.17712 | -45.3169 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65e61f86-c56f-36da-98ab-1420ff146479 | -12.97675 | -56.86095 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5970921d-259e-3b6e-9570-c7c73b9bcc43 | -12.98098 | -56.84946 | 2025-08-19 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a9fa761-126e-3014-a37a-27748c182924 | -12.0976 | -47.91695 | 2025-08-19 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 005709b1-918d-3299-81c1-5bc47c382f53 | -14.16994 | -45.32089 | 2025-08-19 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4007b122-d03e-3b9a-ab0b-ff3b7a4fbeb4 | -13.60744 | -46.96413 | 2025-08-19 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1051897-c6ed-3045-a2ef-575181234668 | -13.67514 | -44.22322 | 2025-08-19 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c46bd777-ad97-3102-860e-ecf3fd8d3b3f | -10.1876 | -46.81989 | 2025-08-19 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README28.md)
