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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a5251ff-a107-339d-b596-24314437649d | -3.66312 | -40.57986 | 2026-09-15 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bb4b3b27-8da9-3f38-9cbb-7ba3f08cb151 | -6.33588 | -39.39003 | 2026-09-15 04:12:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 73e772cb-c121-3eae-8b77-43896c20ff61 | -4.24355 | -38.05835 | 2026-09-15 04:12:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1b568978-b7ea-3c65-ad11-ebda3dfbc644 | -3.66534 | -40.58755 | 2026-09-15 04:12:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c65ae00-d4c0-3ffd-87f0-930c923593ad | -2.88947 | -50.42869 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0f889c5c-5c02-35a1-aa93-e9a8b60a94e9 | -5.61118 | -43.56337 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6cbfa088-02fc-338d-8d05-96274053c3c4 | -5.55869 | -43.43987 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35754c57-0fbe-3d82-b63c-057e7deb54c2 | -2.90846 | -50.42439 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c64e9c53-3d5d-3500-9f34-f39960e644ee | -2.98872 | -39.97086 | 2026-09-15 04:12:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e48372a7-c8b3-3eee-a8f8-93fa8ab84b5f | -4.67091 | -42.08989 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 05c77681-dfb3-3c37-88ff-0aa30afd7c1c | -2.89616 | -50.42225 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5922af1e-ad6f-36d6-a218-8b687f24c5a5 | -5.73925 | -43.27842 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b4235a2-81fb-36ff-998c-28a99e25606d | -3.2378 | -43.03086 | 2026-09-15 04:12:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd384d70-d043-35c5-8fe7-f92129d56471 | -4.6645 | -42.08483 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 7df6b8ca-c9e2-3229-980e-dc36b02d34cf | -3.23255 | -50.58251 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1c80c4b-2e4b-3830-a133-c37acb2af7ce | -3.77875 | -51.35086 | 2026-09-15 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d72d089f-6570-3b71-bb04-c88202106d91 | -2.88488 | -50.41822 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd30381b-0558-31fa-9255-98cc5cdd7fd8 | -2.91248 | -50.40091 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28a3b41f-e13b-336f-9075-abb8622702d3 | -3.22475 | -50.59095 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0352589-99c7-3d36-ade8-9b7b4632fa87 | -3.24995 | -44.63534 | 2026-09-15 04:12:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e27db98-66c1-36ec-8a51-2a8b5c57906f | -2.89327 | -50.44398 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11af1b13-03d5-3bfe-bdc8-33c290b34103 | -3.61492 | -45.52969 | 2026-09-15 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ebd7b85-ba63-3626-bcc5-b34308d836d0 | -3.84528 | -51.76746 | 2026-09-15 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61667ac7-f0f8-324a-b099-00be3bfba4e9 | -4.49558 | -45.91195 | 2026-09-15 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d404da3-ccf0-3177-815e-6ce085c6345e | -5.60364 | -44.84684 | 2026-09-15 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6239bc30-9fd6-3618-8919-35fac6a747fc | -2.92073 | -50.42659 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9641fd9a-807c-3220-ae6b-6b488136e519 | -2.89455 | -50.43163 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4a21cbb-0fb7-3127-8f34-fb2824369390 | -4.65218 | -42.44637 | 2026-09-15 04:12:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5bc89f63-000c-32d7-a367-b8aeb7dbf9cd | -2.89697 | -50.41755 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2faaaa79-8939-3309-8fc9-fe7567054df2 | -4.80523 | -42.87633 | 2026-09-15 04:12:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 473eb8db-fbe7-3f00-9b47-5bc4503d173d | -2.89717 | -50.42034 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ec8626f-ffab-3b36-bdb9-2688d54c955f | -3.96176 | -43.11319 | 2026-09-15 04:12:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2ea970d-7568-3606-a95d-ed5d6375b85d | -2.89082 | -50.41654 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13247569-9a27-3b7a-8045-767776e72ee5 | -3.48755 | -50.374 | 2026-09-15 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f522e07-9a3a-3810-b454-f58542d9c10b | -4.6821 | -42.08769 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8488e305-4527-30d5-a5f2-862b5e05c5c0 | -2.94929 | -50.40731 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d50e525e-572f-3231-a27d-d95b89b8cbec | -5.63711 | -40.85516 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 74f8a240-d9f6-37b6-91c6-ad906c7cf1a8 | -2.98816 | -39.97435 | 2026-09-15 04:12:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 41734419-1fc8-3e7b-8f65-6567fa7cdf1f | -2.89988 | -50.43743 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46cf8669-c957-35c7-8b9d-5726deff3fad | -2.89024 | -50.424 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36803907-fb19-34fb-9abe-343995a31c25 | -5.55724 | -43.44147 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 07e35e3b-d9e7-3c1b-a753-9ee63be042d9 | -4.1861 | -48.68749 | 2026-09-15 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2d111993-df21-36ae-97af-61c7dec77159 | -2.95008 | -50.40265 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7255e15-881d-3b7b-988d-8c42645514b8 | -3.07514 | -51.07531 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86db9071-6bd9-3eaf-ad1b-32d8de8ea389 | -2.92155 | -50.42183 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a9ea398-38ce-3923-9d01-4ab09d098149 | -5.55351 | -43.44088 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f39d6f72-d983-3654-ae6d-18d0c61e23b5 | -3.25595 | -47.08414 | 2026-09-15 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcdd9e07-9297-34ec-b6c6-72d1b73fecee | -5.55423 | -43.43641 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f56d56a1-bcdb-337f-bddf-50a305a0b60a | -4.66161 | -42.08036 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 379281cd-0074-36a2-8cfa-d1d809b9f942 | -2.90312 | -50.41862 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dff2496-d0ba-3fcf-919d-817f6e5cdf81 | -4.65284 | -42.44231 | 2026-09-15 04:12:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe5a3ce6-8f80-378f-bf58-8c6032bd6f5b | -3.85888 | -51.9828 | 2026-09-15 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| acfcd675-04da-3be9-9419-325e8d662590 | -2.88468 | -50.41547 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad9abba2-286b-3e1d-8b53-9530cf989c62 | -2.89907 | -50.44218 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f8d95e0-126f-38e3-ba78-271a106a9fb3 | -3.96221 | -45.68692 | 2026-09-15 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99257367-262b-3bb2-b162-4dd422bec83c | -2.91541 | -50.42075 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e5caea6b-5b79-31f2-8846-1fbe03f182f5 | -5.44858 | -36.31715 | 2026-09-15 04:12:00 | NPP-375D | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 194e0cfc-d670-34a1-bb7c-5404735b1112 | -2.89375 | -50.43627 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23e58813-d77a-3b7a-801d-47fca3221d18 | -2.89293 | -50.44103 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4810146b-5519-3201-9ee4-35beaa44a6d1 | -2.89102 | -50.41929 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11db4259-bca3-336b-98d4-6a1cf02ec08d | -2.95544 | -50.40828 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24d6755f-1c55-358a-9af7-4d499c06d1b0 | -2.91087 | -50.41028 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cfbd7b3-1adc-3ac2-971e-d640527e1492 | -3.3905 | -50.75432 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 229bf1fb-cc9a-3c5b-8a84-2b6246abd485 | -2.89485 | -50.43444 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 665b3a0d-6d63-331d-afd3-167a9b7aa9a7 | -2.82462 | -51.34118 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a86580d-d3b5-34c7-8752-c3a295d3ad23 | -2.90069 | -50.43274 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6572c8aa-f391-3a56-bff1-0e899d6f8e0c | -3.86224 | -51.98219 | 2026-09-15 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de4a6151-669a-342c-9695-d7feedbb05ae | -2.88565 | -50.41354 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bc7ee6b-34c4-3bf4-aa23-14960967923f | -3.07427 | -51.08049 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22c9de5c-f686-3bb9-8279-92072ddf1c28 | -2.90714 | -50.39522 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d83e2ee-fbef-34e7-acce-2b2f33d842c0 | -3.2458 | -44.63465 | 2026-09-15 04:12:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57be24c0-97df-3b96-b278-72156f7465f6 | -5.55571 | -43.43483 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce72ab63-3fc6-3dff-b190-2c838eedd381 | -5.64381 | -40.85631 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4500b941-f9ae-39c5-aba2-4c979187971f | -2.88869 | -50.43338 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02864bcc-ecce-396d-a8e0-6ec01e1166c5 | -5.5338 | -43.37403 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbfab076-d1e7-35ba-bd81-b0b5441e8a26 | -5.60743 | -43.56276 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72b01798-3386-3641-888e-544d9f25e964 | -2.91168 | -50.40559 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f3a6456-ac44-3140-8b4e-93ef3e139f1b | -2.92022 | -50.39258 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73c1320a-b3f8-3097-8b12-8056dfed1a1b | -3.49284 | -50.37964 | 2026-09-15 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6543e80-8639-3617-ae07-1f8eff420fe1 | -4.66513 | -42.08092 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 530f1124-c5a4-387e-82f6-40bef6218bcf | -3.37295 | -45.0937 | 2026-09-15 04:12:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fe943f38-c023-3dc7-ba83-cda0da32434c | -3.07237 | -50.5715 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7de6680-a570-3192-9890-cba2749ef462 | -2.95623 | -50.40364 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2724b770-c0c9-3374-8c37-d32dad210427 | -5.73557 | -43.2778 | 2026-09-15 04:12:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 847f7282-5487-3e1f-9570-80227c635470 | -1.794 | -47.83679 | 2026-09-15 04:12:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d567311-c479-322c-bf16-bbcbeea4e943 | -4.66739 | -42.08932 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 71cbb3ef-b12b-3dfb-881d-e5e8d3078140 | -2.95466 | -50.41294 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e0fe764-459a-3dac-ba2a-7a7b95c43003 | -2.8892 | -50.4259 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a816ee7a-7368-305f-aad1-7307555feeef | -2.89561 | -50.4298 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b8788cd2-5279-3363-b736-85aa55ceaefb | -4.24298 | -38.06195 | 2026-09-15 04:12:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 43498cb5-9892-3022-bf95-c55659adc380 | -2.9015 | -50.42803 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dee0c873-1396-3f29-aedb-c6474b83d122 | -4.66387 | -42.08875 | 2026-09-15 04:12:00 | NPP-375D | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8c0ceb8a-4b5d-31ca-8ec0-debf58502faf | -2.90683 | -50.43385 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 84b2f1ed-0675-35fc-9e24-4f1f0c904ba8 | -9.45937 | -40.38988 | 2026-09-15 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 08d7f7e7-7b18-3aea-ac45-2e0764997d34 | -11.24563 | -43.44691 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 251b9bbe-67be-3272-a304-d77626c7bab6 | -11.23254 | -43.46077 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70c59a33-4628-33da-83fa-cdc62c73861b | -9.45271 | -40.38882 | 2026-09-15 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 1dd0099a-466a-34ae-9b2b-23aa5a050520 | -9.42249 | -50.10246 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a710b14-8314-366c-8495-f9120095336d | -10.58248 | -47.73658 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59f80d24-2ed2-3931-a2c4-2f04bcd58d96 | -7.22876 | -46.15123 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README25.md)
