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
| 1269ef0a-ebbd-3b88-8e97-b042d42ca6a0 | -3.75108 | -52.27367 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea57925e-d75f-364f-a177-56ef52a9e0fa | -3.25259 | -53.93457 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d329124-40a2-3a0b-989a-e60d95059ebc | -3.46953 | -50.26929 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4cc2757-0634-35b2-a3df-cbeabd2b646f | -3.16313 | -51.11576 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01584818-8ba7-35df-bab3-631821469489 | -2.89447 | -54.16161 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59871474-e111-3710-8095-be987fbc2968 | -3.94373 | -46.3469 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9f12e6f-ed12-3374-af2e-eacff4890cf8 | -4.04814 | -46.82341 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76c2566a-79ce-39ba-a29b-6b98260f62dd | -3.64679 | -52.62139 | 2024-12-02 04:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f534c4f-1c91-3649-8c4e-9d44120eb659 | -3.25758 | -50.57639 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08f9de45-1e98-3c9f-9b21-f771af2f0627 | -5.23859 | -43.7473 | 2024-12-02 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 903d7b94-0dda-3169-bc25-29daca56a267 | -5.21926 | -50.12295 | 2024-12-02 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4f08c5f-62ba-3633-8d24-0b5d8bf3aed2 | -3.3306 | -53.54727 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 447d7309-b3e1-3e0a-b3bf-81dcfeeea931 | -3.65458 | -51.1216 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5924cc64-679b-3100-a82f-e2e209d8f4ff | -2.8732 | -51.82938 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39e79c14-9521-3fe5-aa0b-3edfb2d3d777 | -3.85728 | -50.89418 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce7ebe16-555c-3f90-86ef-5b9f313172af | -3.49669 | -53.83787 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a4782c4-e4a9-35bd-a9ef-d0b2f1fa6131 | -5.00339 | -44.16795 | 2024-12-02 04:25:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a862ddc-c07d-35d9-8792-596d3968c709 | -4.17189 | -46.55421 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec4d35e3-3522-3ded-8156-f76534d81cfa | -3.06821 | -53.68444 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cc02377-cda4-32cc-8ea8-3bfbfc060664 | -4.11376 | -50.49507 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a4aaa20-b9f0-3367-bb9e-d50475c3f2fc | -3.07135 | -53.68843 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b88377f8-9cd8-3aeb-9a47-ec8646d8c054 | -3.85908 | -47.05007 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dff8763-f804-36b9-93cf-8627fc76979a | -3.94488 | -49.98044 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f2d8c92-08e3-3fce-9db0-a12b9b00f6c6 | -3.85752 | -46.52959 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cc982ce-9309-3e8b-a3a9-e16364f88e67 | -3.92102 | -47.09669 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a197f1-0b7a-3c01-a228-8998566752d9 | -6.08647 | -48.06033 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fce6e9d4-4f65-3f69-9d22-fa6fa4b02abd | -4.02342 | -45.88701 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10ad61a1-d25a-3b65-858d-d19f2af2798a | -3.26135 | -53.62717 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a1dd07d4-c4f7-33db-9795-3eaf1abc1a0a | -4.32148 | -48.21555 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98faf339-45fc-3b0b-b80a-7b7fb8bbde68 | -4.03742 | -46.93462 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8503b8e-77e1-3b02-bc24-7c9d88c539dc | -5.58606 | -45.15606 | 2024-12-02 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b874105-495a-313d-96d8-d8b0c9ac1f0f | -6.49323 | -35.18458 | 2024-12-02 04:27:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| cc3288da-1cbe-3ab1-94c5-2d1e2fc7cd56 | -6.48304 | -35.18305 | 2024-12-02 04:27:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| d04b07d2-3d02-319e-848a-1c552b9da371 | -4.91324 | -41.33529 | 2024-12-02 04:27:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| e0ea8627-0c09-34ae-87f4-771df4f8157f | -4.90125 | -41.33767 | 2024-12-02 04:27:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 48ee2b9e-5a09-35b7-b529-c7f9d79043ca | -9.34498 | -58.22786 | 2024-12-02 04:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f9ff33-1d75-3433-be55-9aef0103979f | -9.35106 | -58.22909 | 2024-12-02 04:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fd712d5-b25d-3166-a99f-c0e3b390bb19 | -19.16723 | -40.14145 | 2024-12-02 04:27:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1264b3d7-5c45-352c-a9b5-800a019b7dcf | -9.3517 | -58.22822 | 2024-12-02 04:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4261318b-f1dc-3b3d-80cf-399d232af2a9 | -17.49919 | -45.17644 | 2024-12-02 04:27:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d79ad1f-e888-323d-8e70-d31ce8ba4110 | -13.26685 | -43.92863 | 2024-12-02 04:27:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b250f26f-dfd4-3d9c-8810-3670530ddf52 | -14.31779 | -44.16193 | 2024-12-02 04:27:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25e4c976-ac80-315f-bc6f-151ee3983850 | -15.57013 | -47.85559 | 2024-12-02 04:27:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbccc406-0f57-3a4b-aeff-c8da34cfce1c | -17.75091 | -42.8951 | 2024-12-02 04:27:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c2b4fc7-77da-3ad1-8944-647c5527abd3 | -13.74077 | -43.62598 | 2024-12-02 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a753da57-2776-3aef-9e74-3b099fa09d46 | -19.16688 | -40.14469 | 2024-12-02 04:27:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5b117b7-360e-30d5-98d5-0c83f002bc10 | -9.34562 | -58.22696 | 2024-12-02 04:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a528fabf-c583-3636-a790-27f8bcfb323e | -17.09448 | -43.80581 | 2024-12-02 04:27:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9bc8b0c-f544-3d5e-9d18-bb6dd72266d0 | -16.04741 | -46.19981 | 2024-12-02 04:27:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d4ce984-a2f5-35a8-b5ac-442e19e16d8d | -14.31753 | -44.16389 | 2024-12-02 04:27:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b68116fd-5d41-35a7-b986-8d2ce0ceb6a9 | -15.07731 | -48.94363 | 2024-12-02 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd13aaf4-46d4-32ce-bacb-354caba4def3 | -15.08064 | -48.94419 | 2024-12-02 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fece64de-3589-3794-9a88-1907b05cc235 | -9.76763 | -56.92946 | 2024-12-02 04:27:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b16e6541-30ff-305f-83ba-01858ea5eb14 | -9.77321 | -56.93052 | 2024-12-02 04:27:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3066407d-103e-3dc6-a2bb-e1a9f8d3f69c | -17.77932 | -42.80731 | 2024-12-02 04:27:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6681874c-b098-362f-bb8b-4f720608d6ec | -17.40961 | -49.04064 | 2024-12-02 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ee4848c-32ff-311c-bf58-3b304754470b | -20.73118 | -54.94511 | 2024-12-02 04:29:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04f0ff62-6f8a-38c8-90f2-af6129b41a48 | -22.55424 | -43.55141 | 2024-12-02 04:29:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 88b4f486-3a85-3f93-ab06-243f41565049 | -23.45897 | -52.82221 | 2024-12-02 04:29:00 | NPP-375D | RONDON | PARANÁ | Brasil | 4122602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5241762d-43f4-3782-99fe-80e0b2b66742 | -22.71656 | -48.23524 | 2024-12-02 04:29:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 58df8f75-25e6-3f38-b6a6-7736c9eba781 | -20.72784 | -54.4283 | 2024-12-02 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 17.2 |
| aff131ef-4d0b-3b50-bc7f-71e97818d825 | -23.40598 | -46.55733 | 2024-12-02 04:29:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 362a8abc-d156-3930-80cb-3479f5d73ba3 | -22.55858 | -43.55214 | 2024-12-02 04:29:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 381ddd46-6002-3228-b4ef-bf0091b9c273 | -19.72716 | -49.63686 | 2024-12-02 04:29:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| abe0e9af-98e1-3ba0-bcea-0b3b63ffad16 | -23.33976 | -46.77328 | 2024-12-02 04:29:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 15217ff6-50e9-3027-bb94-646551b6bd1b | -20.72297 | -54.43264 | 2024-12-02 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 44ebb5c3-619f-377e-8984-2d5d638011c5 | -22.55904 | -43.54815 | 2024-12-02 04:29:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ed54f90e-d4ee-3304-b140-6497689fe75a | -22.71998 | -48.23583 | 2024-12-02 04:29:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 701268ad-1f65-3ea2-b472-a6dc62cd5040 | -22.54992 | -43.55056 | 2024-12-02 04:29:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 298f0704-bcda-38dd-a405-f4136191ff24 | -22.55392 | -43.55255 | 2024-12-02 04:29:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6af5d7eb-af38-35c1-8c50-8bae71bed6ec | -22.55437 | -43.54873 | 2024-12-02 04:29:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c0dd5322-b1e0-3514-b83e-c2d55020d79f | -22.55468 | -43.54757 | 2024-12-02 04:29:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 07d1654e-cbee-3471-bb9e-d4e0d4d434fc | -20.72394 | -54.42745 | 2024-12-02 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85a127ce-5b47-37b6-b2e6-6b12f16b79ba | -5.118 | -43.2198 | 2024-12-02 04:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| db56a89e-a300-30b1-abf9-ac2863a2ddda | -3.259 | -53.6388 | 2024-12-02 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d9a8fb35-57c5-34a2-85b3-9a1818bddcc5 | -3.2708 | -46.4511 | 2024-12-02 04:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 20353dde-9da2-3596-858e-2f9d146cb732 | -3.2591 | -53.6186 | 2024-12-02 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f1dccc6e-764f-36a7-9b5b-f24da13cb4ad | -5.5882 | -45.1412 | 2024-12-02 04:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| fa265b7f-05b0-3ca0-be0d-6bbe941213cb | -5.1181 | -43.1964 | 2024-12-02 04:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 67f94c15-5470-3324-a88c-e51ffadc443e | 1.1072 | -56.007 | 2024-12-02 04:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9d268303-00b9-3651-809b-c948ee33b1ae | -5.1369 | -43.1951 | 2024-12-02 04:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 834badfb-7aab-3975-9fa8-5fd822a22b85 | -5.5882 | -45.1412 | 2024-12-02 04:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7bdf1de5-66c0-34cd-ac66-b7afa2eb74d9 | -3.2591 | -53.6186 | 2024-12-02 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| dc40a2e8-1204-382c-98b4-7ca0bd9f0863 | 1.0889 | -56.0269 | 2024-12-02 04:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5d048218-6c0c-308a-bdb2-cfcb2b02543d | 1.0889 | -56.0072 | 2024-12-02 04:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 33afdede-6486-3f03-b48f-27872be502a1 | -3.2708 | -46.4511 | 2024-12-02 04:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 5fef22f5-35ff-3f83-8e4b-cb6789b06400 | -3.259 | -53.6388 | 2024-12-02 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 68d96679-ca72-3798-b0f6-64e6d72cdbef | -5.1367 | -43.2185 | 2024-12-02 04:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0a7339dd-b76c-3e0b-96c7-0b66f81a4813 | 1.68182 | -50.66213 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0c8b702-a0c4-3102-a4d5-12c7c7483ed8 | 1.65892 | -50.77456 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5eabdb7-05d3-380d-b2d4-3ce1e4345c51 | 1.60951 | -50.93729 | 2024-12-02 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 828f66a5-08bf-375c-a912-ff35e459f9e0 | 1.67671 | -50.7156 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d984fc6-dfa9-3151-899e-fbe531484867 | 1.65838 | -50.77113 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0ee282e-0870-38cc-825d-e6ab6ce9163a | 1.67522 | -50.66315 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9f681f0-2138-35ad-8f78-272600f8691f | 2.44387 | -51.20943 | 2024-12-02 04:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c98cd11-bea6-3897-89b5-4cca9b191078 | 2.44441 | -51.21289 | 2024-12-02 04:46:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff46c9f3-efc3-3f5e-92ac-7648e3d7f1e4 | 1.67617 | -50.71217 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1946e4cc-e623-3ac5-a921-92220da83620 | 1.67852 | -50.66264 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62a9e374-faef-33b7-bf0c-5cb4ace445d3 | 1.61005 | -50.94072 | 2024-12-02 04:46:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89421442-db98-34ac-aab8-cdeb8f909b06 | 1.67576 | -50.66658 | 2024-12-02 04:46:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
