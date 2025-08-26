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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e8f677d-f271-3a29-9d8b-145d37cabe2a | -14.59053 | -54.50897 | 2025-08-26 04:46:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55994663-6e86-38bb-89ea-3cafbdb6ec0e | -13.61625 | -48.14674 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c184702-abab-3f2e-8647-e812d742d397 | -13.42218 | -46.9206 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d39e3688-f2e8-3994-95aa-b9e1ab951ef5 | -9.15232 | -59.55088 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 149559a6-94bc-335c-85ad-ed69134bf05c | -9.26471 | -59.79539 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3069d80-eed3-3e7d-b68b-5fe1fce1506c | -13.40449 | -51.76856 | 2025-08-26 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b82d8b0-fd77-385d-9f2e-b761342c3b2c | -11.51447 | -52.13803 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 065e77b5-182c-356a-a85d-fb0369dc126e | -12.77782 | -48.14161 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c15599fc-bab4-3710-8ac1-62cdedd96dc1 | -11.63148 | -46.40958 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb43150a-77b0-383e-8d3c-b06f2047c02b | -13.4471 | -46.98878 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce78614f-ca57-3032-a2b8-d9dec7625d7c | -13.58969 | -48.19365 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18c7b224-39be-36cc-bbc0-422bc28fa02e | -13.4498 | -47.00766 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59b20141-bb37-3ec8-8537-ace2044e4e04 | -9.15428 | -59.55818 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 9bf76117-7b07-32a8-b117-28bfdaf068fd | -12.93178 | -46.30723 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 55fda837-600e-38ba-87d9-e3d876d3c42c | -9.31095 | -63.44093 | 2025-08-26 04:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 36a22098-b4b9-3c52-a9a8-a8f96ec59700 | -7.38292 | -64.35109 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2d758cb-895e-3f9c-a610-5b9c13b33d65 | -13.43708 | -46.9994 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a139b7a-d6fa-352a-bc9b-47b0d17ec71b | -8.91022 | -62.42213 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0645bcff-7219-3642-b706-4bd1b7f901bf | -9.61971 | -57.38241 | 2025-08-26 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b1dfc6e-d306-355c-b2b6-c13b8bccfdeb | -8.85688 | -62.44707 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ff3018ee-aac4-36d6-9609-f4c25fbfdea9 | -9.15371 | -60.78875 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5704bdb-4007-3a10-904e-4478a971392d | -12.48801 | -53.828 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e764f6f-2176-34de-ba51-d4cc71e52df3 | -13.59708 | -48.20177 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0358c35-b5d9-3cf5-99e0-260f040c0a8e | -11.51502 | -52.13452 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9629eeb1-9c7b-3ce4-841e-4bd67be10c57 | -11.51557 | -52.13102 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ab3c286c-2eaa-374e-888b-fd84ab806720 | -11.15196 | -44.7472 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5767bef-8dca-3f70-8c0a-bd8770e2a5cc | -14.31203 | -53.06866 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a93f9c-cf17-3ecb-836b-feddc147326c | -8.86988 | -52.04524 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a77094e3-6edd-36a5-b669-4ec8e478a3c8 | -11.63273 | -46.20677 | 2025-08-26 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54702dcc-ef54-3892-9b73-8b2041c2f2fe | -13.42638 | -46.92126 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff5b4d8c-3e35-3987-bffc-57fff56c1ee6 | -13.44409 | -47.01866 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8df571a6-eb3c-3599-a8f2-bea2e03cf4cc | -9.17191 | -59.46218 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| baeb7354-a6fd-3b92-8c99-5ad2fc4520ae | -10.14822 | -48.88362 | 2025-08-26 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8dea0816-e477-334a-80b5-7f55099a18bb | -10.60529 | -54.89406 | 2025-08-26 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd68e116-7d4c-3b17-a167-21fd864680f1 | -8.60533 | -62.59007 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26399e97-341e-35a0-a2be-549d7000fe63 | -11.50178 | -52.13239 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 40d6f4cf-2dc7-3aaf-8596-f32100ba1cf0 | -10.51938 | -57.98106 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20fd84c9-9a26-3776-922a-312368e1864b | -12.7435 | -48.16193 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c20e7177-c9c1-3274-918d-3142a87d4233 | -6.81865 | -58.97355 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4d421838-62f4-3817-a789-739c94bfaa15 | -12.42089 | -46.81264 | 2025-08-26 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 320ef4e1-e54e-3f16-bc9e-5a08648cd336 | -13.60134 | -48.19556 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b61a7b47-d21e-36b3-b047-31165da385b4 | -8.70616 | -47.86869 | 2025-08-26 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f25896f-bd60-34f1-8e2c-4d2a399da673 | -11.54799 | -51.88059 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c349ab45-fdc9-3abf-a412-d4b0c4becd2c | -15.11662 | -48.65423 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7811681b-6dbc-3206-adaf-e0f640cff59b | -9.00173 | -65.39466 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76944f85-764f-3361-a7b4-46ef5b84473a | -7.53824 | -61.38489 | 2025-08-26 04:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e06e936-f312-3a2f-b71d-f29125d4587e | -11.02798 | -49.14111 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c81df8e-ff46-344c-a31a-b119b39c9f12 | -9.2682 | -49.62022 | 2025-08-26 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e31e688a-8e8e-3c39-ae05-b82dd39bcda4 | -10.61607 | -54.58753 | 2025-08-26 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e3988e8-20c1-375d-9d73-ff84308b152c | -12.73257 | -48.14465 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87b4f51a-a207-38ba-9d22-922a6a0bf272 | -8.11838 | -61.46243 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d1a860e-c114-3c39-9b11-164d390d56f2 | -11.53213 | -52.13369 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a5147720-5623-3b68-888b-930fcf79657a | -12.48465 | -53.82744 | 2025-08-26 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d85a85b1-f56d-31df-8c5b-c15059cea36a | -8.86356 | -62.44396 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a977f182-45b8-3bcd-9346-7c90337e5f80 | -9.16483 | -59.53645 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| db510ced-25b8-3f47-80a9-7da4a99510d7 | -8.54777 | -62.63408 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 590d1eef-4b7e-3fcc-83d9-9765d5636997 | -13.48512 | -46.86974 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db404208-b30f-3f73-b501-414969d824c9 | -11.08387 | -44.77806 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be7d9007-141b-31fd-ba4e-6a8d9bc290b1 | -12.74529 | -48.16578 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e6f4bd1f-b0bb-322a-adcd-cfe915cf3fda | -7.56343 | -57.67255 | 2025-08-26 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c6511c-80a0-3cbc-b73d-223b30067642 | -9.69046 | -48.33778 | 2025-08-26 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b0991b1-4ca1-3302-ad4c-16b3c44c2cb3 | -11.16343 | -44.75807 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 85d73fcf-7439-3753-81a8-17e16b8413f6 | -10.32893 | -54.37162 | 2025-08-26 04:46:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5beb647-7788-3147-aea5-c2a08e516c71 | -11.16273 | -44.7632 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| bca81be7-447f-3bd5-a1ec-dfc8d0bd3499 | -10.52986 | -46.7935 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3bde8df-52f7-3f29-a7af-8383b0d40a33 | -10.53551 | -46.78305 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 99f1d2f8-51af-3b71-8f26-d0370b0b519d | -8.86861 | -62.4494 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50a52846-c2b2-38d1-a641-305865ad4a40 | -11.55365 | -52.10477 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d77d01c-ad04-39e1-8480-12a5cd500750 | -10.45409 | -58.00285 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b79a55d6-aa14-307c-9f95-232d3d3475ea | -8.86942 | -62.44511 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7ed337d-c78f-3d41-a0d7-da42875eb22e | -11.52771 | -52.11858 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cac50e8-9361-35c3-91b8-29f50927e9ef | -7.62138 | -61.04327 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffae9567-8eed-3fc1-82e2-e654f66ee2a0 | -15.05194 | -48.69571 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d11a4ea-5636-3243-b883-8099f73e4528 | -15.00628 | -49.59842 | 2025-08-26 04:46:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3381282-3866-3cdc-af2c-93176f4a0f5f | -11.55751 | -52.1018 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 875038eb-e065-3015-8068-ecbd5c281b73 | -9.25416 | -56.90788 | 2025-08-26 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 283e011e-7180-3d0e-97bf-10b9723b7c87 | -11.62841 | -44.86187 | 2025-08-26 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd2e4489-c3b2-3c40-bc76-90d237894111 | -9.15716 | -59.55172 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 12cface0-c66d-355e-bfa4-3050ada78acf | -15.06759 | -48.54459 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4accf797-4819-32b0-9ff8-2599a74b0179 | -9.64402 | -59.63262 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1356e059-b1e1-3a9b-abd5-b0f6632b42b1 | -9.19394 | -59.64315 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db788fa2-011a-3f91-afff-1b6fa59a1dbc | -6.81084 | -58.96116 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6594ae34-8b77-3901-a774-ab2290fa7c1e | -13.45028 | -47.00399 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a00bf9c1-9780-3e6c-a013-5207d724e0ac | -8.89127 | -62.45826 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bde8cd4c-b2aa-37f9-9429-f2a5884e8162 | -9.18458 | -59.45205 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e4ac9a58-0ae4-3f21-a7ce-81befb69cdaf | -8.83846 | -62.44786 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 008c3de2-2880-3f01-ae1b-ba40aeaedae9 | -9.1647 | -59.5088 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24aca423-9f2e-3d74-b6e8-1fde1f25c775 | -9.80055 | -64.26202 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f88c5a2d-7597-3eb4-8e8b-930b5653fb51 | -15.06483 | -48.54121 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5f58ed1-81bb-3a68-9da5-952ff7b657a1 | -14.59347 | -52.02376 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5beaefa2-7b5d-3584-809a-0a2df202160f | -9.19254 | -59.79168 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7701bf07-6cad-3d34-bf11-7a63a8faa56c | -13.43382 | -46.92972 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3780adbc-8349-3072-82ff-d45ac0638c54 | -11.14785 | -44.76653 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| af0e3c81-607f-3fc1-92f7-f1d5e737cd55 | -9.16351 | -59.45911 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 87b3545e-a73f-3d77-adcf-5f1fd19930a0 | -12.48402 | -47.23269 | 2025-08-26 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31eb3653-7bc0-3966-84d4-da98064adee8 | -9.0107 | -65.39478 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6be4739b-96e3-32e9-b935-12b82dbbaae8 | -12.7467 | -48.16728 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6f8fc44b-8e72-3a65-8a25-675c615fce87 | -6.91456 | -59.36862 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 468073b0-1c54-3df0-a948-c22ade577c60 | -11.15729 | -44.76778 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 97c547fe-83da-3325-9f4e-1ef5232398e0 | -15.0258 | -48.50278 | 2025-08-26 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README62.md)
