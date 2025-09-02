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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e02c926-d7a8-388e-a9d9-da5900b2e1bd | -9.93236 | -51.62798 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae9a6cdf-36aa-31f2-941d-f971c2e55b6e | -8.65879 | -62.61042 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04630b0f-b5e0-3bf2-b3fb-7c18e4a017f4 | -9.60651 | -55.38497 | 2025-09-02 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c83931a4-1b46-39b0-a149-25ba672c1a33 | -11.66181 | -52.16354 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5db83c52-c690-3700-9bb5-a06752b95c50 | -7.36477 | -61.6522 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85f47776-acf0-38af-8e82-acf76bdfd375 | -12.67325 | -48.2262 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f8b10d6-d87a-3a15-b6dd-05e9c7880dcf | -13.09896 | -57.11821 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6efda682-12d5-3692-891d-76af2fe25064 | -10.75792 | -49.56652 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ea9c3aa1-76bb-3cfe-9088-8e5800f82bc2 | -11.663 | -52.21371 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 29ec7969-6351-3ac4-93a0-876c83b16ad5 | -7.60293 | -61.6039 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11d7c8d5-f861-31f5-a91f-898818109652 | -14.49316 | -45.94958 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04eba1b6-06ef-3344-805e-d04104acf4cd | -12.94163 | -48.083 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21ea8efa-d99b-33c8-bde5-f17c7d76b8e7 | -7.70282 | -61.10345 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7303919a-b60d-349e-b13c-d3625ec55fda | -8.69399 | -62.40182 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5068af44-75ad-3ef5-ac16-2a02ea1d2b54 | -11.67942 | -52.21264 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e962c953-516e-3756-8cca-fb0b29c217fe | -12.92016 | -56.93348 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bcb7bde-35c2-3d89-a3fd-3181541ec656 | -14.60847 | -54.4862 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a8fd781-b209-3520-a2c8-d2bbe3fa27e4 | -8.75873 | -62.42853 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a657bef-9314-3a0a-8c2d-fdec8eb08263 | -13.30659 | -46.83473 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ae133d4c-ac7e-397c-a096-a8337344dbd3 | -11.85102 | -51.53931 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffb1a0bf-5ffc-3e09-ae61-a405a70d2939 | -12.43621 | -48.72232 | 2025-09-02 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b7c23b2-76bb-37ac-b2ef-77de306fa407 | -11.21249 | -55.06413 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19b10505-c38c-3022-ab6e-3877ed822298 | -13.71998 | -46.93385 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 294993c4-e75e-389f-8523-2e4a9c179063 | -14.72515 | -46.75218 | 2025-09-02 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cea0b813-a64f-3097-adfb-4dfb9c311359 | -11.65938 | -52.18114 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aea36ba3-3cbf-3ba7-85e2-6c925cd96b39 | -11.66552 | -52.22475 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec93caa7-4eb2-33a8-986b-52b7b79c2fee | -10.05049 | -48.12209 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bca2e9b8-e8d4-3d46-84a4-752517cc0f36 | -11.66142 | -52.19575 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d6fa8e78-33e6-33b8-b8ee-471407f86d32 | -9.6188 | -55.3721 | 2025-09-02 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84fb1c74-1785-3b98-99ba-d811bd19f99b | -12.88191 | -48.17453 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 465cefd5-7261-33ce-be2b-e55ac10a5600 | -10.05821 | -48.14314 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b8c6f33-c8b8-3bf2-bcd7-00742fed9966 | -12.92797 | -56.99269 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab99ab83-97ee-39be-a5a1-ee311cfaa264 | -11.65685 | -52.16998 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be2f38b8-890a-3737-a5cb-84f21ef79658 | -12.93842 | -56.96904 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 077955b2-406e-3f79-ab1c-6daa9e7fbec8 | -11.66035 | -52.17414 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b78809dc-246d-361a-8c66-d4294e718cba | -14.72236 | -46.74796 | 2025-09-02 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c96ab0d2-d33d-3782-8885-f602a6f96625 | -12.91907 | -56.94056 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f57bb901-0b82-3d02-b45e-5cd9beec17ed | -12.92739 | -56.9745 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76e99834-a9f8-3912-bcec-1aff71f2b910 | -14.78155 | -48.17897 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 845c03b0-02fa-3612-9faa-e78eccddb2a2 | -14.21784 | -48.06327 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b0998d5-254f-3ee2-8e8e-fb614ed4c376 | -14.78107 | -48.18313 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a22ab74-f07a-3e56-a829-7147be147a27 | -11.01098 | -46.93792 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3395b507-6941-348a-971d-33e5407834fe | -11.6695 | -52.22537 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a16aa52f-eb2b-3ad3-bc69-2ed98d527469 | -10.76204 | -59.84011 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0719cb9-9e3b-3118-865f-aa1a60699374 | -13.69603 | -46.93621 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c2add14d-7f51-3d9a-acfb-b1fe6d2ba686 | -12.92849 | -56.96745 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2a2a788-8ba5-31c4-968a-c7da1ff02c38 | -11.79348 | -46.4035 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ff4a2d7b-6b7b-337a-82b0-df79944efd29 | -14.58536 | -54.54441 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d48a4e19-558e-3f6d-93c9-5608b1e18e39 | -11.03006 | -46.85675 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff0db85f-f3a9-3407-b4d9-00b950614948 | -8.65239 | -62.60805 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 159f0474-310e-3aa7-b7af-8a51da8544ce | -11.6769 | -52.20157 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b48b1eb0-c2f7-3de0-bc4a-daa52c0657aa | -12.98319 | -48.09946 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 16efe1dd-4b73-3a60-bb0e-75a5351e5be3 | -11.67397 | -52.2225 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 4364f660-85a1-3e12-b446-0d47e59faf65 | -14.49467 | -45.95517 | 2025-09-02 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5756385-cc87-31c5-8b7a-254ccb13e713 | -11.86213 | -46.71996 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 028923ed-87a8-30f8-9ec4-24ad7415656c | -8.68973 | -62.40109 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8676a73f-d1c0-3e0f-ac76-ed2079b6ef2e | -10.75726 | -49.57144 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 997c7b80-ee76-3cdd-b9a6-c49006d92d95 | -14.58805 | -48.06425 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04e21ca2-08a8-3c42-8905-c33cadc4cd0b | -12.92572 | -56.96338 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c7f5773-6555-3503-989f-3f232597adc1 | -10.44955 | -54.77757 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c3a020e-8fd3-341b-88be-4d5d590a5dde | -8.65744 | -62.60465 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c16828d-5a7d-3b23-b38f-37578b4cb255 | -11.86354 | -46.70766 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75c1d826-222f-36f0-85f8-989b9ff90314 | -11.86788 | -50.60879 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43deef3b-aa6c-36b5-bd47-c0e5ef16adaf | -12.93896 | -56.96551 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fa84a41-b0aa-3311-8aa2-554aa97b1b24 | -12.76875 | -48.09212 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7844874e-8a53-339c-9e24-173d74930554 | -12.81081 | -48.05799 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 457552c3-6fa4-396b-8fa6-335f597fafaa | -13.68935 | -46.94305 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d1a2e598-a809-32f1-8ca6-1e1559367ab0 | -11.65297 | -52.19798 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3caadedb-ad51-3399-890f-cee7c34edb93 | -10.44669 | -54.77324 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c349556e-cec1-3ae2-9d36-f13df9f3dd23 | -9.25011 | -60.49068 | 2025-09-02 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 436278b3-e186-36ad-ba49-6b1ebc3514da | -8.69756 | -62.40661 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 665318f7-4453-3931-ac64-8796ec366acb | -11.79148 | -46.40666 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc906241-a95b-3320-bbeb-375f9f81ab25 | -11.06417 | -46.90728 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db8fc31a-9580-36c2-96d6-f7527c4c2ec8 | -14.22373 | -51.65823 | 2025-09-02 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2f4526e3-fbd0-3a0e-8116-43f09d1bb552 | -10.05186 | -48.15177 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46b2b545-8dbe-39c0-80a3-8d801802468c | -11.0596 | -45.39502 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6ca9489b-8e84-3b92-aae8-7da38896bae7 | -9.0923 | -58.89144 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0e41a4f-9343-35b3-9efa-140479dad8fa | -12.76359 | -44.70186 | 2025-09-02 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ca20a51-9697-39d7-a7c6-3103c963ea44 | -10.45012 | -54.7738 | 2025-09-02 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1610d20a-28aa-3dbf-b569-5927f5c73d92 | -9.73894 | -48.9719 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92b9e4ae-4cad-387f-b422-5f6d9f72d091 | -11.8548 | -51.47974 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09c57c67-0694-3e84-832a-703b8ef8f405 | -11.64838 | -52.17218 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eb5c331-f0da-3e7d-92b2-ff556359ecb4 | -10.05479 | -48.1293 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bf67903-88a6-3f34-a5b0-16eec3bfa528 | -9.61098 | -55.37825 | 2025-09-02 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dd40994-40e2-3d21-9e8a-804ad2c604a6 | -11.54813 | -44.84298 | 2025-09-02 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a78227e1-be26-3070-b631-aab8e682ad26 | -7.08647 | -63.17928 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7d7bc95-c872-31f3-a97d-7f8df398e59a | -11.97096 | -45.86323 | 2025-09-02 05:06:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d8277bb-df2d-3643-bb15-1c0f1c5349e8 | -11.65394 | -52.19099 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8112162e-f92b-31a5-b72e-00f316972315 | -10.88513 | -55.75202 | 2025-09-02 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57b2fab6-d7be-3370-b996-30f0a2ba996d | -11.8037 | -46.40449 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 58b24d80-6d33-3469-b2e0-22a7c5768782 | -11.9165 | -46.45181 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 890f4678-fe25-398e-a4ab-694340df3fea | -14.61932 | -48.03349 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91637900-30c4-358d-8590-e976aae20a4d | -14.31466 | -53.09805 | 2025-09-02 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a815761-81ae-39d9-b358-408f2d944436 | -8.96783 | -65.96495 | 2025-09-02 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51cb8ca-c572-369e-991b-c43eafa581a2 | -14.21329 | -48.05455 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 312d6838-0d3f-33b7-b827-dad0021b46f4 | -8.50686 | -63.90966 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b845f51d-4e6d-35ed-9e9d-ba3881acb53f | -8.73745 | -62.42484 | 2025-09-02 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 673e9e52-87b3-34e8-b9d7-b2e053532933 | -9.72718 | -48.98632 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4178d5c0-7af1-3538-8d27-9630fe632acb | -11.06842 | -46.91933 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eafb852-158d-38f1-9df6-4e6c40ad425c | -7.6665 | -61.10092 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README69.md)
