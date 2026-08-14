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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 355dfb3d-9eab-319e-b408-fa6b0334956c | -14.44802 | -51.85604 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71b72273-c95e-3891-afd6-a3f77798051a | -14.03067 | -53.58792 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70ada1fc-ce8e-392d-bde1-24f36286c873 | -13.75138 | -53.41753 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a3994c0-30a1-35db-ab5e-1a5bfe9f6182 | -14.28908 | -51.97213 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6027f765-6479-374a-99d0-cbd285789a43 | -14.36572 | -53.32809 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4acf5189-c430-33c5-8548-410539bd30bb | -16.90164 | -54.15141 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caa099ac-c8a4-3148-8cff-8952f5db6757 | -14.45039 | -45.69736 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c7ae446-34a7-34e1-a772-165d582c037c | -14.99239 | -46.58219 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2024b4fc-c309-34ab-972f-582850ca7b65 | -13.92592 | -53.95878 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 186852bd-e1fa-3089-9037-c15405ae622f | -14.74259 | -48.2357 | 2026-08-14 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97375182-952f-315e-bc64-a7400b282f5b | -15.04901 | -52.6776 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c64404d-3194-39b4-be10-84ad2875293e | -16.91237 | -54.13839 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bea4ca2c-676f-3801-81cd-8941f1e77dd2 | -14.6278 | -42.52405 | 2026-08-14 04:34:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 12e004e9-09f3-3338-9f4d-5d73aed99a47 | -18.44836 | -43.44238 | 2026-08-14 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ed7ce959-1503-3e8d-8dfc-5da0405ad556 | -11.06578 | -50.93867 | 2026-08-14 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e83097bb-72cb-362e-9eee-3591ca82d769 | -15.52089 | -45.85796 | 2026-08-14 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccc5ab05-ac65-3c23-8a5d-8c02b26543a8 | -15.33132 | -48.01081 | 2026-08-14 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2423905-ec9c-3592-b8ed-ccd97423fe94 | -11.31452 | -45.21733 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd13a906-e638-3c69-aca1-b36cf34a3c6b | -11.50579 | -54.61555 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6be3ce36-3885-3fbd-83f8-0dafb8024076 | -18.41386 | -45.19459 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a5244df-bf78-3a68-b601-37e8704bdaee | -14.72357 | -52.88371 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a189f94f-8203-3fd7-969f-7a65a3efa9bd | -14.06416 | -53.60838 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b6944dc-8165-31c3-a737-a389d44a3818 | -13.24294 | -54.24964 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c440f1fc-3c58-37fe-bcce-a88ed5bfabbb | -14.4545 | -45.69387 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e103a107-035c-3dc8-b9e1-07499093c44c | -13.2437 | -54.24543 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01dcabcb-15bd-3818-9434-1b157e56ccf3 | -13.28048 | -54.225 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 521335cb-03bc-31f2-8da0-f741cb22428b | -18.04049 | -47.8593 | 2026-08-14 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da8f8ebb-637a-3499-971c-61e21359730b | -14.98898 | -46.58163 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eabd24b-204f-3715-981a-1dbcfb3f619b | -15.35344 | -49.66335 | 2026-08-14 04:34:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b79c9f7-679f-3bd4-a397-41f8c117bf13 | -8.89579 | -60.55987 | 2026-08-14 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 579e25a0-c69d-39c2-901d-1a683627d7d1 | -14.48965 | -53.08498 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6126eb0a-abda-39ac-a2ad-fd1653eadfd0 | -13.75476 | -53.42193 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6a94df0-04d5-3d02-9cac-1b1bdc10bb12 | -15.63373 | -48.89248 | 2026-08-14 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 246573ac-8ffa-3b3f-8620-45a8f04a5ae0 | -13.56441 | -46.26104 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6390e45f-248e-3833-a0e0-2657f087505d | -14.93756 | -46.62115 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b94e0e5-2c86-36af-a774-8d6d9766e374 | -12.03075 | -47.81566 | 2026-08-14 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a4e239c-da9e-349a-a8b1-3ab6f6340fdd | -14.05343 | -53.64409 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a1412d4-b5be-3076-a265-01ee5cc20aed | -14.09609 | -53.64157 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b9ee273-1aa5-3f21-a202-e07d89a06b86 | -15.05193 | -52.68332 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07dc04db-7f01-3787-86a5-2d9738aad35e | -13.58599 | -46.23381 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ab61ab1-8eea-3f48-9d07-eee2718dd82e | -11.48505 | -54.62603 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10e30cfd-6a21-31fd-99b0-93b4afb40337 | -13.82038 | -53.79824 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f1ee609-135b-3d87-a1af-6c6c68d462d6 | -14.44704 | -51.85892 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8effbe4f-5633-3225-8380-bb6adb2d641a | -14.08115 | -53.63084 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd7e17fa-201e-36ea-9406-164d64299b00 | -17.56544 | -47.50377 | 2026-08-14 04:34:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2fc081a2-76af-36bc-99b0-b2b78c367db3 | -15.03337 | -47.033 | 2026-08-14 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28d52563-2c3d-3195-b7c5-b073bd0c4796 | -13.24674 | -54.22855 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b0c008b-1711-32e8-8948-bda3919835f1 | -11.45599 | -44.5593 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 418666e2-01aa-3b8b-a863-ea08b34af26e | -14.95575 | -46.61624 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5730c156-7a10-3708-9d32-c0e232620dcb | -12.35128 | -51.21215 | 2026-08-14 04:34:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1eca7d8-dec3-35e1-8976-e3b13b87714b | -14.62833 | -42.52004 | 2026-08-14 04:34:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4040b6dd-b941-353c-ab67-7640cca6a789 | -15.12039 | -48.65976 | 2026-08-14 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e800bd49-844b-3e84-8453-0fb386097f48 | -14.4533 | -45.70193 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebd501b8-dc38-3383-a5e7-14bc2c381854 | -14.95812 | -46.60065 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b003be53-7f8d-37b8-860a-a4799919436f | -12.0335 | -47.81972 | 2026-08-14 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6723e6e-5655-3744-b9ba-c920e39f048e | -12.49202 | -43.76837 | 2026-08-14 04:34:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a34e04b-a98c-3c8b-8d1a-191652b02add | -14.36507 | -53.33172 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2392e078-c9ac-333e-ab92-b56b927341d9 | -14.93986 | -46.62907 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f5ec450-cb80-39b1-8fc4-511cbbe2272f | -12.71418 | -48.45279 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c944343-4c25-3b53-b86a-4094644959c0 | -16.17207 | -46.80942 | 2026-08-14 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c9d4d31-4ae5-306a-9067-a8cfcb6fa1dc | -14.29669 | -47.15308 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4ef6143-7d80-374d-9a6f-27e7a33863c1 | -15.44549 | -52.9996 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfadd00b-de8e-3153-a6ff-2e18feb2b7ff | -12.71256 | -48.44156 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b26cfd9-b251-369a-aebb-ea04dbeacb0d | -16.90235 | -54.14755 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 714ccc61-f955-3d43-aa47-86a8dcb75578 | -14.32921 | -51.99484 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d53a864-22a0-3a06-bae9-1c28bee5db5d | -15.50946 | -52.99691 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caabcfb3-72a0-3e00-aab6-4c7843af349e | -18.49188 | -43.40168 | 2026-08-14 04:34:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 94221831-c8bc-38f0-8f43-ead392c91918 | -11.85108 | -51.91075 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcbaf867-6312-329a-864f-4fb27473dc5c | -13.23482 | -54.26997 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bbfa751-a869-3dd8-9939-665c0160a551 | -15.44421 | -52.9974 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c944dd5d-4d1d-315a-9640-5d1dc6c5d478 | -10.70921 | -50.51672 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7278958-d2e3-3d98-8fb9-02b695b3b1b4 | -14.44277 | -45.70029 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c7891a4-785f-370c-ac1a-086a839cc45c | -13.24598 | -54.23274 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e966e859-8491-388b-b6e8-b15191603d5e | -13.65282 | -46.25552 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cb3605ee-a5e0-371c-ac4a-8d5986dab6b0 | -14.05464 | -53.59127 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bbdeec2-d290-3035-ad81-eb8aece2531f | -15.06267 | -52.6623 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c3aee66-6ce9-3017-bbfb-49cded30f5be | -11.50212 | -54.60991 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bc92e7c-8a4a-3d37-afa9-1449a4382858 | -14.09781 | -51.75277 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77b57194-a76a-3aca-8630-0fba761030ea | -10.8046 | -48.57567 | 2026-08-14 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bacd01c-6c29-3284-b04a-8b1b7968cbfc | -12.03406 | -47.8162 | 2026-08-14 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4b25ac9-19c2-3500-b899-fed7e14fd65d | -14.07434 | -53.6219 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b539c82-d84d-3329-85c0-8beb9e486eca | -14.43186 | -51.86227 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97ba29b7-2d22-3123-8efc-f8e4e056df90 | -14.97193 | -46.60246 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36d2bfc0-d0c2-32c7-8025-4e01abac5edf | -12.02533 | -46.41469 | 2026-08-14 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ef599d1-ca2a-36fc-9ba5-ad45246be6f9 | -12.55766 | -48.34681 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fceb1f39-9a9b-320b-8182-9f5c58fcfc1b | -13.42362 | -57.04758 | 2026-08-14 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd89da72-4662-37f7-b557-817aeb392a76 | -11.4524 | -44.55876 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f309f23-cebf-3588-8023-e01c56c314e7 | -15.1672 | -50.05233 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28b99c12-c277-3b25-8a88-e1bde2e0f5d5 | -16.87551 | -54.13044 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f61b3992-b9ca-321e-b1c6-fba6a6b2c645 | -10.69846 | -50.51485 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8103f9f-f853-3fef-bc0c-155512e859dc | -14.47269 | -45.69553 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14264603-8c2c-3425-95f3-e972d349b606 | -13.82593 | -53.79129 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5885695c-cc07-3f94-a22b-d9d2a0240411 | -14.35682 | -51.96761 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3bf2cfd-470a-3033-a096-37a3f09239b7 | -13.55982 | -46.24511 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b532efb7-2553-31ea-a2cb-adae7217f1d8 | -12.71644 | -48.43858 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b040b1d-daaf-3eee-9bad-5317c3faf315 | -13.23989 | -54.26655 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 814da584-f54a-388e-9026-a27caaeffbfc | -12.51754 | -55.78781 | 2026-08-14 04:34:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| deec3958-474a-317a-8936-f9428783e91f | -15.137 | -41.55624 | 2026-08-14 04:34:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 62b706a9-49ae-3a54-92bc-c362dd6f7a5c | -15.16197 | -52.80356 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 715abdab-ee3d-33df-a31a-9d4088ad2bcf | -13.38425 | -42.38805 | 2026-08-14 04:34:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |


[Clique aqui para ver as próximas entradas](README26.md)
