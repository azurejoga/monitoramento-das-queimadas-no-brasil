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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40b4cff5-df49-3dd1-a32a-886ee7c40763 | -5.86975 | -50.3088 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af5e5457-82d4-33e4-8f3f-2cbf0feac819 | -4.11283 | -46.90364 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6200428b-b821-3328-9e51-fcdd37b7939c | -3.40377 | -46.05999 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c88f8e7-5c3f-3c58-ab4b-fac10c3c8cfd | -4.38596 | -47.24667 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb45d1ac-ad41-38b1-a056-83fe9ab76af2 | -4.12581 | -43.59207 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4aa1f48b-1f03-3e69-903c-1c792c86b6b8 | -3.64757 | -50.13932 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 137936c9-44f0-3a3e-828f-67c20af07aee | -3.45405 | -50.37496 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 728203ee-a1ae-325e-ad44-540bfc1c8c90 | -2.99561 | -49.2376 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68123e6d-c129-3555-9031-c59f15667181 | -7.63533 | -43.54385 | 2024-11-09 04:33:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4131ef78-7f8b-33d3-81f8-9b32a61e837f | -3.96623 | -48.12597 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a45ff4d4-6e8d-3297-af5f-b9c8f2003d2f | -4.86294 | -48.11505 | 2024-11-09 04:33:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e6971ff-79d4-3cf4-ada1-1f09d2cdbd9e | -4.89073 | -44.59437 | 2024-11-09 04:33:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8ec3f35-1166-3a26-8813-d19285ce9c23 | -3.26576 | -46.31298 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0cbf5ce-3883-3364-b1c7-bf6191f9cf57 | -2.91702 | -49.35572 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50e7daea-73a9-3967-bb95-ba26abdadae3 | -5.47236 | -43.65761 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e0b0ebf8-f83b-3f9c-93da-852d4b6e17e5 | -2.8476 | -49.44149 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7c46633-70c8-34af-89b6-3b465624b05c | -3.33769 | -50.08083 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb120e24-f5df-3604-a20b-35e608117653 | -3.6294 | -50.18565 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dfe3e9f-7ab1-3362-aab4-3bcbd5282828 | -4.10794 | -51.07133 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 274c2336-278e-32c4-9239-b104160ed921 | -4.59144 | -48.47764 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e1d9661-2d75-3511-b739-69d6ee272ac7 | -3.09986 | -51.04 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dafe02e6-0b92-379f-ab5d-8cb73e9ddb10 | -5.13509 | -50.61332 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 815a707c-9b23-36ef-9460-66dbdd8b21eb | -3.96917 | -48.17273 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 527c0123-e7cf-3832-8a51-cb7a52705e89 | -7.45523 | -43.57023 | 2024-11-09 04:33:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24461bab-a199-33fb-b291-aa8226ee462d | -3.16909 | -49.09719 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da10b1c6-f2db-30a6-ad3d-a487fc45b406 | -2.86783 | -50.31741 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f47b52f-9aa1-316a-9f79-291d59115348 | -3.08952 | -51.2235 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4216f030-2f36-3e77-92ff-81a46e1e6301 | -5.9339 | -43.65386 | 2024-11-09 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6834d9d5-2399-3af4-ab2a-7ff17ffd7134 | -3.05123 | -51.3406 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19e5db91-0d40-30bf-b194-87ea0aade4c2 | -6.26859 | -44.54094 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0a8a7ad6-81fd-32c3-8879-b62de8519c5e | -3.55589 | -47.38062 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13d79a54-37f6-36fe-a280-92e31567b78a | -4.5125 | -45.70078 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff4b2eb3-d283-3c09-b75f-b997a0092c55 | -3.70837 | -54.34722 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6c07f0e-aa55-3773-a005-2fbabe2a1d4b | -4.3903 | -50.97143 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad23c16d-ba47-3dae-b1cc-313f98ab48e6 | -2.7351 | -49.28549 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9527822e-e0d8-324a-a7f2-04bee128a2a9 | -2.8608 | -49.22405 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8d7097d-6125-3559-8885-99f5760704c3 | -3.15589 | -54.47726 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dce73ca6-fe60-3dbf-b1c1-caae04c83ae5 | -2.84285 | -49.56182 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07384150-3b98-38cf-b07d-7684a8ef0ca2 | -2.92519 | -51.66922 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c65ac9c-1e18-3807-a655-84ac28d00ac6 | -3.63941 | -50.19132 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 230cb11c-7bd0-31e2-a629-f1010ffd8e51 | -3.25284 | -46.43959 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 546035aa-2e05-3928-a393-7cdadceca1ad | -3.53315 | -50.33181 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a6af7a0-eff5-36a8-babb-56431afeddf9 | -2.76918 | -51.60958 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f60dd11-4300-3180-94d1-ca8aac66122b | -3.24675 | -50.44994 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 939bcb53-3e7a-39dd-be75-13b1f4e4f5ce | -3.58711 | -47.35379 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| afc35c2d-3e24-3ff0-aa07-b80a0e6b47da | -4.67118 | -44.33932 | 2024-11-09 04:33:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| df5e672c-8e80-37f7-a0a3-692917d551bd | -7.60651 | -40.43321 | 2024-11-09 04:33:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| fb500dbd-057c-3978-ac1d-51ced830862b | -3.22126 | -50.37814 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 15189e6a-3778-3544-a024-f66dff8d5d78 | -3.39902 | -51.59603 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf459c0a-8715-3ed4-b166-72700be4a2d9 | -3.91167 | -47.95449 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03382821-489a-33cc-9698-d8ebada52fba | -3.70204 | -54.62246 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bee675e-9b18-31b0-a886-2ba203c6977b | -2.67936 | -51.82318 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1c059e7f-3bcf-30b9-828a-dadf6503f385 | -3.25885 | -51.01276 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30da582a-5363-34f1-a5c6-2323fb2f2d02 | -3.08053 | -49.57066 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ac17638-983e-358f-a0ae-5c209a2bc0a6 | -4.26423 | -46.91283 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6180220-b104-3cc5-849f-432dc2bd7c22 | -2.86766 | -49.22512 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7eee24b1-3062-3e29-9d2f-9e28f7f886dd | -4.40561 | -41.90991 | 2024-11-09 04:33:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d99cd3e4-e6d6-3444-b55f-807a2782881c | -2.88799 | -48.29679 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c73eac11-6ead-3e01-9591-3c15698888f7 | -4.89309 | -48.61484 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 607025b1-71e4-3ad1-aa3a-49efc63e1bb6 | -3.23212 | -46.5289 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34317bd7-16b6-38a8-9ae1-6d5e3f90c0db | -2.97495 | -51.43146 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3cde6bd-95a4-398d-95e2-403c749fd584 | -4.20113 | -45.85175 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e201ca54-04ab-3bf2-99fc-72673282dcf9 | -3.9514 | -48.15566 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 38247767-d470-3e56-89f5-429349c1c468 | -5.25251 | -48.08097 | 2024-11-09 04:33:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18d3bd08-51f9-3a28-9883-b2e8738f428c | -4.29229 | -48.585 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1aec9cd-7f75-3cd9-a515-82e52f494483 | -2.91642 | -49.35948 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1551d53e-9b16-3967-ab24-9171a356d9c0 | -5.47306 | -43.65294 | 2024-11-09 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b9263da4-bc22-3e70-a2cc-acc9836fc1ec | -3.19384 | -46.491 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 762dde31-1a2d-3560-837a-2c9b5640c5fb | -3.45598 | -50.18 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ea7a5ac-5686-3872-a21a-40a339c6a4a5 | -2.81091 | -51.80489 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10d1d95e-1b22-3433-a74b-dfb6d5172c7c | -2.97733 | -50.30062 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d9d0576-1362-34d3-b237-d7e179f19ebd | -3.92416 | -48.32978 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83038c33-09ef-3df1-964d-440080342ea5 | -5.1433 | -47.71474 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4742db03-804d-3a32-aecc-010570a59dd0 | -3.59862 | -47.34502 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 2c4a6949-f0e6-34e9-bef9-e458338c213f | -3.90153 | -51.92646 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ffcff300-8c0e-3725-a00b-4b6b0e765609 | -3.95972 | -48.16761 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 295fbfea-dcd9-3073-bae4-889c0a6540a9 | -2.94358 | -54.45243 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4eaec947-d08f-37e6-8dd7-5cd1ddea5439 | -3.79563 | -50.7966 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28978fdf-7ab7-3cc5-b5d6-509fb18a1c0e | -2.89215 | -49.40573 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8775efe2-f6eb-36e4-82cd-89511d895ae7 | -4.43443 | -47.26122 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88e7529c-e0a6-31a3-a1f7-9a74a48dba9a | -2.87413 | -50.41608 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56a04148-096b-3fd0-8335-0bc7c84ea983 | -4.73285 | -48.98147 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d672119-d4da-39a4-99ea-d0ec5c60f65c | -6.18474 | -45.44835 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ed4e23f3-75ed-39aa-8407-9e8c6800229d | -3.75978 | -51.76155 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 039f8d78-daa4-3884-987a-86328e153061 | -6.23103 | -47.28008 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef37a57-cbf0-3e83-922d-a4db5711b010 | -3.86366 | -46.44846 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b1ad0cf-8491-3b45-a81f-2349eebc1be7 | -2.94278 | -54.45741 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb11a56c-69e5-3632-b9ed-9777253c1ca0 | -4.78287 | -48.68764 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d4ba4ef-7121-3fc9-9c4c-2c5f1efd62ce | -3.72828 | -54.22458 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 5229b33a-8b6d-3d6d-ad7e-d259d38e782a | -4.0192 | -49.91845 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b03514f8-5495-35b6-8bf2-9aa3b004cc07 | -4.04019 | -48.28347 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7dab0b61-44ef-3085-a143-21dcccb1872c | -3.58634 | -50.27367 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54193815-b8f1-3b23-91d2-8c9f94c216c8 | -4.75235 | -48.36389 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c6801af-08c5-3226-8ef4-01f423d56c64 | -4.7466 | -48.80849 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2dcd7a2-e64b-30dc-bec0-d53dffd10b34 | -3.0939 | -53.31904 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 09c0f114-4a95-3779-a0a9-bd915ef00551 | -5.72881 | -41.99844 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d576ad48-644f-3e59-bdba-8d9a1bfe0702 | -5.51124 | -46.23497 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84d6f4c8-86ef-33ee-a38b-33da36c80cea | -3.98794 | -48.16143 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5475d5e3-c8a0-336c-bf92-c3c88b3e533d | -3.97249 | -48.17325 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 308aea09-7274-3002-9804-ee48900510a0 | -3.18078 | -50.38977 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README65.md)
