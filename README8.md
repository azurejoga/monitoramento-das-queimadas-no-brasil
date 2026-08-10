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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89e84284-a9df-3a88-b5a6-a6b4e76f3cef | -17.13214 | -51.67747 | 2026-08-10 04:10:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5716d0b-2737-3789-9659-edc8855c8cd4 | -20.50018 | -42.3891 | 2026-08-10 04:10:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cdf82980-9a6b-3edf-8e5b-a5e66fc92430 | -18.99859 | -45.34319 | 2026-08-10 04:10:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5064245c-fc88-36b1-b1cb-f27f6cb55b80 | -16.14364 | -49.70259 | 2026-08-10 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59a4b8d3-9616-3b5b-b1c2-4ea05f3af270 | -20.55126 | -41.25141 | 2026-08-10 04:10:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6275c845-5535-368b-b016-a55b350de639 | -16.71603 | -46.39781 | 2026-08-10 04:10:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dc4cfbd-6397-30da-acc0-5a0e23fd71de | -18.029 | -44.38329 | 2026-08-10 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b61282a-2c23-3f22-bbf1-897e2044afdf | -16.7142 | -46.40068 | 2026-08-10 04:10:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bf7e905-690e-3600-b400-0a0f3a518342 | -20.39576 | -42.82419 | 2026-08-10 04:10:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f17bee48-2682-305e-9a77-b3fd2f577bc0 | -20.50477 | -43.64323 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 4c4621fb-1423-3225-8b13-08d24abca36a | -15.07885 | -50.3758 | 2026-08-10 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c8963d0-e3fb-308d-9fb2-1c386315021d | -19.17995 | -42.74198 | 2026-08-10 04:10:00 | NOAA-20 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| af73b06c-12f8-3c44-b254-a0a9412e824c | -20.04402 | -43.76219 | 2026-08-10 04:10:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac4b8383-aa34-38c2-a967-3a4cffb401a4 | -18.37157 | -43.66024 | 2026-08-10 04:10:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 574e5f74-b5ca-38ac-b027-b196e87a8170 | -19.82973 | -43.29645 | 2026-08-10 04:10:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ae5c8aa-7c42-3a4a-a5f8-ed6893c6b0a4 | -20.37208 | -42.91098 | 2026-08-10 04:10:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 245bd927-3575-3fe1-8496-a8bb3105ea79 | -15.84397 | -48.13809 | 2026-08-10 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3a28afdd-1d40-3d1d-a6ad-4e83def0209d | -20.39519 | -42.8279 | 2026-08-10 04:10:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b505eea5-f43a-3bbe-a4ff-5ec6ec781fc3 | -18.82028 | -49.64517 | 2026-08-10 04:10:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e33b50d6-c6a3-3746-804f-c0312db859fa | -18.02871 | -44.36401 | 2026-08-10 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c331f0d4-ec96-387a-a245-9f8ede9c4a52 | -18.02596 | -44.35962 | 2026-08-10 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b619179-5a32-3483-80cd-d2d5c9b01def | -16.06193 | -50.80132 | 2026-08-10 04:10:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 010deda4-bff5-3332-9855-781daf2c0802 | -20.56515 | -42.87263 | 2026-08-10 04:10:00 | NOAA-20 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a58665f8-cb80-34ad-820c-52cefb5c0621 | -20.04614 | -43.77017 | 2026-08-10 04:10:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| aa0912fd-0c47-37e4-8707-471861feb0b6 | -14.29762 | -54.93797 | 2026-08-10 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4416c59f-5087-3723-855a-62392176fb48 | -17.8291 | -45.25743 | 2026-08-10 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f77f2829-60e2-3eaf-ab94-edd520a7f4cf | -22.22084 | -43.02404 | 2026-08-10 04:10:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| cc1a80e7-1dd3-364d-8898-55a438d94a54 | -19.84207 | -44.99031 | 2026-08-10 04:10:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce586381-3781-3391-829b-87ef18bf10bf | -14.13717 | -54.01284 | 2026-08-10 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f58bd037-15b4-306c-b5cb-de55cbbad31f | -17.13145 | -51.68081 | 2026-08-10 04:10:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc5634fa-1baf-32a7-bfbc-c696ba42c848 | -19.86367 | -40.23988 | 2026-08-10 04:10:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea750a18-3fe4-3489-91a9-d866a9a9842f | -15.08167 | -52.69392 | 2026-08-10 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 305d6665-2fa8-30af-b7b0-f0f7b46aa6b2 | -22.22142 | -43.02021 | 2026-08-10 04:10:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6f5972a8-aa39-33ca-bca1-586f40831ae5 | -21.32196 | -43.78022 | 2026-08-10 04:10:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e07017c4-b93c-33f1-9b06-7a3369eb30f1 | -20.04555 | -43.77388 | 2026-08-10 04:10:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a165b4d1-5db4-3adb-bd30-910e407059f2 | -20.50075 | -42.38536 | 2026-08-10 04:10:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e5090c6b-8325-30d0-8d10-6260d8211dce | -20.50263 | -43.6353 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d41b214b-075c-38bd-961e-78ee39b85c7a | -19.50301 | -42.60925 | 2026-08-10 04:10:00 | NOAA-20 | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a18f7cc3-13bd-33be-a92d-4d87140bc29d | -14.13948 | -54.01764 | 2026-08-10 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e423d5c-357d-3e80-a147-ff02a80e9c55 | -17.50573 | -41.76268 | 2026-08-10 04:10:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29cc8ad2-46ef-3ffb-bbcb-f25c4086a1bb | -21.41476 | -43.88054 | 2026-08-10 04:10:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e01f484-1eeb-33fe-870f-4055e9d25ffc | -17.50628 | -41.75903 | 2026-08-10 04:10:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de82ea30-00df-3ea0-9cbb-4d4b6268d185 | -20.42475 | -41.58802 | 2026-08-10 04:10:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b06ca26-f15d-3002-b635-a4b16a4f4ad8 | -20.50049 | -43.62738 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6fccf4b8-f002-3f5d-be7a-9208724b164d | -17.76588 | -42.42907 | 2026-08-10 04:10:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 950a90b0-a450-39c5-ae0e-d5104ab0db3c | -22.22358 | -43.02849 | 2026-08-10 04:10:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49182896-1b3d-3cc2-862d-20f859a47c15 | -20.3765 | -41.60773 | 2026-08-10 04:10:00 | NOAA-20 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5e93979e-1c44-3c5a-953a-4d91d79f5d42 | -18.11937 | -43.97237 | 2026-08-10 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0538eed2-6d30-3bde-a74a-a0bcacf1e9c1 | -20.38967 | -49.30802 | 2026-08-10 04:10:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b560ae6d-ff17-34cd-acab-d79a98f84f72 | -20.49991 | -43.63105 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 30173cb1-0009-3302-b98f-df6dab926efb | -17.33991 | -42.78225 | 2026-08-10 04:10:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 484eded8-4a78-34e6-98e7-e5892b518102 | -15.7006 | -56.1598 | 2026-08-10 04:10:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e90044b7-cd78-36b3-9943-1a0f735627c2 | -16.13905 | -49.70164 | 2026-08-10 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ad812f1-52f7-365e-8b12-9b74dc5ab42e | -23.01842 | -46.6762 | 2026-08-10 04:10:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5317b14a-63b4-31c5-8fd2-ddcf4a74da14 | -16.06079 | -50.80706 | 2026-08-10 04:10:00 | NOAA-20 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0e0e8888-dfeb-37d3-9232-23b0eb1fe68f | -20.50632 | -43.65483 | 2026-08-10 04:10:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bf47e99f-c863-3867-a724-6947db9b30b4 | -8.9598 | -60.555 | 2026-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9e7aa959-4d27-3783-9dc2-bea4b824b423 | -8.9039 | -60.5769 | 2026-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8b10bb64-a4ed-3094-8939-1c882c67a7d8 | -8.9039 | -60.5769 | 2026-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 44e52e6d-e81b-356d-9051-7fd9163e8b0e | -8.9598 | -60.555 | 2026-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 95b3e414-1f6b-30d6-bfe7-da2fe5780d8a | -8.9039 | -60.5769 | 2026-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 730f8ad3-f85f-3a35-92e8-1ee4f38afe85 | -15.1512 | -52.7205 | 2026-08-10 04:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 0a795fe0-8d57-351e-8bde-b99f83ac375f | -0.85568 | -52.71342 | 2026-08-10 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc91f120-5eef-3814-b7e3-d3aec74b84f5 | -1.65253 | -54.45966 | 2026-08-10 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c450ddf-1152-377f-9516-967f6b9577cb | -1.64898 | -54.45909 | 2026-08-10 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca9202bf-34af-36a1-9e55-8b9e45552931 | 0.12276 | -51.18059 | 2026-08-10 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1345d9c8-f043-3707-914c-432034350f5b | 2.36014 | -60.14277 | 2026-08-10 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cdf6cdb8-2327-3d4d-8b8b-7f1a6802452a | -1.63706 | -54.46546 | 2026-08-10 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1307e076-5502-3194-9c76-d377895eff16 | -1.6519 | -54.46365 | 2026-08-10 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db1de4f4-51d0-389b-9b4b-0737b1dafcd7 | -1.65609 | -54.46019 | 2026-08-10 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0db7489-d0b4-371e-908d-6c744ee32fae | -1.46858 | -53.59914 | 2026-08-10 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ed35290-4c3c-381d-8071-dd65750ef067 | -2.38176 | -48.22762 | 2026-08-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78d70554-3e4f-32d4-9bbe-2d1a9f9e011d | 2.36066 | -60.14628 | 2026-08-10 04:49:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c50d65a8-9c9e-310d-a9a4-abe3f8c8a3fe | -1.64543 | -54.45854 | 2026-08-10 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4889e33-0ec0-3d31-9722-d04412f62777 | -1.64836 | -54.46306 | 2026-08-10 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e85e606e-583a-3552-922b-b72b7ff31d75 | -2.37807 | -48.22707 | 2026-08-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bf52b57-0af7-3335-a010-803115d9a029 | -2.5233 | -48.13558 | 2026-08-10 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1add843c-c30b-3c1a-a2d9-db969b5c8608 | -15.039 | -46.5581 | 2026-08-10 04:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fb343192-8fde-326a-a352-69ccfa8a1914 | -8.9039 | -60.5769 | 2026-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 71d6a2d3-f0ab-3244-a1db-856b81765da3 | -8.9598 | -60.555 | 2026-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 4a4cffd5-984d-3f59-8964-c0b91ca854b2 | -4.86744 | -55.82088 | 2026-08-10 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39a30820-f853-36cd-90fa-c607d39e654b | -6.13742 | -57.71016 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 027d1a04-2ddc-3c76-b5c8-89b2517e7e89 | -6.07043 | -42.51316 | 2026-08-10 04:51:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6c62807d-531b-3871-90b1-86a8b75c3526 | -11.0484 | -44.28164 | 2026-08-10 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71fedb60-ac5e-3693-8cdc-bd2577f149fd | -8.02403 | -55.11746 | 2026-08-10 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5c5ddec8-e8f7-346d-93f2-9a06a0ca3f43 | -9.49189 | -47.83741 | 2026-08-10 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 717f86e6-9fdb-3bf5-8022-69f346986ed3 | -6.85294 | -56.41083 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3528aff0-debd-3438-8423-38523cf779ad | -3.49135 | -50.05645 | 2026-08-10 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 444ad51d-06ef-3f63-8243-e459e0a88ff1 | -4.45714 | -47.91905 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 954d1914-cab9-3e70-bd36-1f9566624b2a | -6.83743 | -56.41283 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d30b348-05f0-3c76-b0e0-8dd4c36aed63 | -6.46388 | -47.85042 | 2026-08-10 04:51:00 | NOAA-21 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 24913453-abef-3c0c-8667-76e9ef8ba435 | -6.8293 | -56.41607 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9943be2a-4b7f-311e-ae66-12f27c5443ea | -6.14432 | -57.71861 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 48fcbd26-a127-33d7-8fde-08b1704382c3 | -4.45399 | -47.91367 | 2026-08-10 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d6067cda-4d63-30cd-ae5f-84d8adccf0e4 | -6.14029 | -57.7179 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 85da6803-d754-39f1-bf69-7271b7b9bd07 | -6.82873 | -56.42672 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13c945fe-51e4-3fda-920d-b9e5f5a86bce | -6.16145 | -57.91711 | 2026-08-10 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 527d47fe-1215-3855-9c93-dd14446e7513 | -6.8507 | -56.40144 | 2026-08-10 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ca9d01c-c1c4-3d9f-af7a-4425f943e283 | -11.0367 | -44.28721 | 2026-08-10 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c159e1d-7727-3c1f-a432-583c9363b704 | -9.4872 | -47.84063 | 2026-08-10 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)
