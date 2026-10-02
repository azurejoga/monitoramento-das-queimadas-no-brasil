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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99f36930-3486-3018-a282-375d4e052726 | -7.84925 | -56.61224 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9239676e-1221-341a-859f-d6872bd03714 | -6.39794 | -56.41167 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b36c0ba2-0ceb-3895-969b-cc667f4b85ed | -7.8242 | -55.12006 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09af847f-52af-30af-b163-10f0a30d882e | -8.23753 | -54.77922 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ac6341d-69d1-3850-a2bb-b353eac491f7 | -8.08085 | -54.88069 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d489310e-24e0-3507-b027-67ba74c921c6 | -7.83266 | -55.1213 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22fa36d-5bc0-3b92-8758-b484dfc6de4e | -7.06166 | -55.62636 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 412dd80d-12ec-35b3-a71f-641f70d79d74 | -7.42335 | -55.58928 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8aeca364-4acd-39b1-b8d5-f614c250712b | -6.24341 | -53.15181 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e524b506-201e-3fd3-9333-16ac7f7f0ac9 | -7.45984 | -54.99465 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6576a370-4aaa-3f58-8b59-0e92a0a2b39a | -7.72404 | -54.80473 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0457a69-bc64-3e48-bfa0-7c3dbe14f7d1 | -6.843 | -55.53656 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc71d9b-62c2-3f5f-a53b-3e1f20776cb3 | -6.20871 | -53.25861 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b2727e-8cb7-3a65-a28c-e0513606c229 | -8.19864 | -54.73911 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fea4df7-19eb-3577-9f6a-d8d288fdee6e | -7.83093 | -55.13292 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81be35b1-7547-3d57-bba1-32a823a212f2 | -7.74251 | -54.79908 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cdf885a-e59a-372e-b087-984cb8dec926 | -6.0003 | -53.54101 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f13c1af7-4b4d-3aab-bacf-5155d7d23d4a | -9.80352 | -48.18641 | 2026-10-02 05:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2bb153d-0cd7-3951-b2a0-a13007e45063 | -6.10439 | -55.68589 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02151b70-e92a-3bbc-9626-beba7c7c6ce2 | -6.43605 | -55.80489 | 2026-10-02 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6dd99895-5060-3d2f-b1e6-bd15a2e97d0c | -8.1799 | -54.80663 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f222eaed-8b75-35ca-9bef-2cffb310fc1a | -8.53259 | -54.56158 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f926d260-5b2b-3a1c-b024-aebd6ed539e8 | -10.82574 | -51.09578 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c23b6f12-a1c3-3512-84f9-4be5e9440ba8 | -8.26417 | -55.69544 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3cabb4f-3005-3882-a0c9-a60ea3c67b81 | -10.41561 | -53.76949 | 2026-10-02 05:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6bd89f8-cc28-3e2b-a14f-b50837e4adbd | -8.5364 | -54.56661 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c613e39a-e0ca-3a04-a7a3-7635c7235411 | -7.39488 | -55.20706 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 56e74672-9e0b-3e84-81af-998021a24302 | -6.24641 | -53.13112 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85fcfd03-25ef-3f6c-b9c6-524ea7b1e383 | -7.83325 | -55.1174 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce66fe2a-278b-3ee2-897a-769d1e7dbcc4 | -7.33445 | -55.23389 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db265b71-1d5e-37ac-8877-a34728a23951 | -10.81305 | -51.09584 | 2026-10-02 05:36:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f0e5bcd-f495-37f6-80f6-158dd0fa76b2 | -8.23813 | -54.77504 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 512ea122-8a45-3ff8-ae88-da1b0863ae18 | -6.2362 | -53.13483 | 2026-10-02 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daa22b4a-b76a-3ed2-b768-0fafb5bd62c1 | -7.83809 | -55.1417 | 2026-10-02 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c0485f5-ef30-3cb2-9566-6e9081c2c2f5 | -6.00418 | -53.54645 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7850ec5c-17c1-36ef-9c59-1a844b27cc8a | -8.08402 | -54.88948 | 2026-10-02 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e197c857-86ed-3c22-a194-f2f487ce8b89 | -12.19149 | -57.11445 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3fe5b97-95b8-3abf-be59-30e0c143ba79 | -12.18753 | -57.11386 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f8ac68c-bef3-3670-9088-e5a7fa474137 | -10.94379 | -68.72147 | 2026-10-02 05:38:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b955b303-badc-3634-ac63-bdf99b6235b1 | -12.19077 | -57.11958 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5939d559-5ad0-3870-b263-1d0fab11819d | -12.19617 | -57.10989 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00c24590-ba8f-3c4e-8b5f-ec8a4fbdec75 | -12.18358 | -57.11324 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ab152c4-16f6-3c40-98a2-774ac66d6c7b | -12.18825 | -57.10873 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8fa19ad-5ad8-3221-8961-e9695d80934c | -10.93915 | -68.7206 | 2026-10-02 05:38:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c95e3ea-4e2a-309b-a5ce-db1ae0178050 | -12.18034 | -57.10751 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d10ee36-bf35-39e6-80f7-e852c4ed7e66 | -12.19545 | -57.11504 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 547e7cd4-1651-36df-a9bc-ee294d91c1bf | -10.93654 | -68.72235 | 2026-10-02 05:38:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a87afdf4-54c7-3f17-aed1-c2038922caa7 | -12.19293 | -57.10416 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43ac87bb-5f21-3394-82a2-a793aa6dfd1f | -10.94288 | -68.72636 | 2026-10-02 05:38:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad63c023-ef42-3882-9668-a98b961164f5 | -12.18429 | -57.10812 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4304d56-6a2c-353a-bf28-62357307677b | -12.19221 | -57.10931 | 2026-10-02 05:38:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 686955db-9a4b-3426-80fe-abf3e5d836fe | -11.73849 | -43.59124 | 2026-10-02 05:50:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 68246ab4-e03a-33c0-8725-438628d4453e | -11.74282 | -43.54728 | 2026-10-02 05:50:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| c6a2a178-183e-3a9d-bef4-eefbacbac8e5 | -11.74537 | -43.55568 | 2026-10-02 05:50:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| dec1d651-e1d0-383c-8e66-e82b08b6a7ac | -11.73604 | -43.58363 | 2026-10-02 05:50:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 2b80df71-f1d5-3d26-ba7a-453d6950eb8d | -15.32845 | -42.76588 | 2026-10-02 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 7fa4c22a-4cd9-3f10-878a-a79f376d6d70 | -15.30803 | -42.79366 | 2026-10-02 05:53:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 11c7dd86-e35f-3780-bc6b-e26c496aa128 | -15.31529 | -42.76712 | 2026-10-02 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 361.4 |
| 38807527-ab08-319a-ba95-0ca88dff879c | -15.31404 | -42.76158 | 2026-10-02 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 263.6 |
| f3403999-444d-30d9-90d4-9cdec03d8d0b | -15.3088 | -42.80038 | 2026-10-02 05:53:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e97b18ef-409e-3b20-adfb-8925ef2baaf6 | -17.70984 | -39.75712 | 2026-10-02 05:53:00 | AQUA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| ea8eca7c-bb84-37b8-a043-bb476e306fbb | -3.2851 | -53.84896 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| af3520a0-36ca-33b0-90e0-23a902a253de | -3.01353 | -53.88625 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c052fe25-4d55-3417-9e93-0ec3fbe490d1 | -3.17532 | -54.10093 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f3edd66-ea01-3496-967b-14de9afb4a32 | -2.88121 | -54.88251 | 2026-10-02 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4be27392-207f-317b-8eee-1c5b830927d3 | 4.3225 | -59.98815 | 2026-10-02 05:53:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1315c79d-5482-37e4-863d-33eeaed2d590 | -5.87077 | -53.50697 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf3beab5-871e-3b69-9350-53908c770c2a | -3.17448 | -54.10647 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d67dd76-8741-32c7-97cd-4e8da14dd3c9 | -5.89808 | -53.505 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 14de4255-368e-3e17-a9a6-5e394f004725 | -3.29665 | -53.86253 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 38af72aa-8b60-3efc-90d5-24b7f24aca65 | -2.89132 | -54.13548 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c51970c7-829d-37df-aa3b-9cf23d9b832d | -6.00043 | -53.53979 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e842f78-329a-3934-9305-0efefd769f23 | -3.16393 | -54.08781 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f58a3ee9-d195-3ab0-ae26-9485e8c1280f | -2.9019 | -54.15365 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99d22c42-3a92-38c6-afd9-51676be4868a | -3.29088 | -53.85577 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cda8b39-f34e-32f1-b2fd-5fc2ddb7e2d5 | -5.86627 | -53.48756 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08bbfc8c-e3c9-30bd-a209-32fadabb5a26 | -2.89461 | -54.15522 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ff65dea-97f1-3179-917c-90fde81f0c74 | -3.12922 | -53.74543 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2be5eac5-c3e7-306f-9d32-4f35fe5f38f9 | -5.85337 | -53.47727 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 202bc735-7f1f-3307-945d-59ffdd264cdd | -3.00694 | -53.88526 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c942ea99-8afa-3b83-88d2-f66d2feff47e | -3.15826 | -54.08111 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b9c8f4b-00a8-3a02-80e5-11e1b2de0e21 | -3.02215 | -53.97502 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7738f258-6c20-3d04-a47b-4987dc61bedf | -3.13116 | -53.75998 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6639d839-f2ea-389f-a4ad-a0c113e0673b | -5.99868 | -53.53934 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e167a964-dd0f-3017-a818-df866f6389b6 | -2.8898 | -54.14341 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76a11e50-4561-3aed-8e43-06a8e9a5d7ea | -6.08269 | -53.30935 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0210b906-34dd-3d52-aa61-fac179b51623 | -2.89061 | -54.13816 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fc8ec43-b792-3e09-b15d-2d3a7011a6fa | -2.89543 | -54.14987 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d81ae3da-7153-3a80-a167-10afd6385ca4 | 1.01179 | -59.53786 | 2026-10-02 05:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a1ab753-f17f-3b07-9a61-7739f8ef7844 | -3.13589 | -53.74641 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8e828d34-c4bd-360b-ac9c-8bf4d0154ce5 | -6.24975 | -53.14975 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 49487405-d33b-3100-9cf4-fa15770becf7 | -3.17044 | -54.08892 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 131f2ce3-6119-39c9-9476-30336a812052 | -3.18095 | -54.10266 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f61948b5-4e16-348b-b589-fafef8338558 | -6.00475 | -53.54739 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 146f868b-50a1-3eee-84a0-9f352bc90089 | -3.16227 | -54.09897 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73c9afcb-1982-3109-932c-988cdb22673a | -5.86094 | -53.47417 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 720d9d1b-8ce5-3196-b280-d62a1a0f68aa | -3.17438 | -54.10196 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ed8334a-344b-3f2e-a4b3-980bf5507a04 | -3.00949 | -53.88161 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 931791fd-25e2-39ec-9ae1-b23d64c034bb | -5.90078 | -53.49635 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a617c12-d179-3504-af34-9a702ab4d6b9 | -3.13413 | -53.75802 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README80.md)
