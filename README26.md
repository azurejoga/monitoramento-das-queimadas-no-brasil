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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ca0c186-8e92-330e-bfd1-f53bf6f472f7 | -11.98487 | -46.38709 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d532e34e-9c70-3fad-abb2-6c1434d94fd8 | -8.96023 | -60.53847 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 31d9bc48-a4eb-3b3b-a3db-5f568725e0e5 | -9.48083 | -47.82982 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abe2af0b-5599-3352-8665-ca851345e124 | -11.98756 | -46.36511 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 131e3eda-71bc-3638-bcd0-963bab87e932 | -8.94593 | -60.53127 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f15c5f0b-aa85-3cb1-9e8e-3655e6216e10 | -8.11301 | -47.18521 | 2026-08-12 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c0cfe56-a06c-3915-b6ea-8e3c4a46afc7 | -11.94804 | -46.34247 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1dd94123-8655-3eb8-9288-d54286e220e4 | -6.99977 | -42.64425 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 806e91f1-1ca0-3246-906f-77ab1c954c3b | -11.80878 | -51.82037 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 067e1768-6dfd-350e-95ba-a4e8ef12a845 | -6.59504 | -59.0098 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3ace180-049d-3ba9-8abb-80a2e589a0ac | -9.34953 | -47.48766 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a9e868f-f0b8-30db-b294-0e586c059434 | -11.82583 | -51.84092 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eae8caea-e822-385f-8c12-37eb4de15ed1 | -8.9497 | -60.53192 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56a48bb5-4c26-3aed-ad78-b940ac04b476 | -7.92675 | -45.11263 | 2026-08-12 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efff7e80-2638-3475-bda7-fef8bdb8b3a3 | -9.33893 | -47.52691 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aad5f607-c242-384b-aa78-0e7982011912 | -11.78709 | -51.85539 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f388a1cf-0271-3d44-93ca-f2d4b11658ad | -12.03204 | -47.80186 | 2026-08-12 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5a6ae56-42d1-3e3d-abbe-90e87972c7ac | -6.33933 | -44.06882 | 2026-08-12 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d01ac23c-c556-33bd-989e-516b5b4271b8 | -8.95472 | -60.54987 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a37b67d-bab1-37fa-967b-7407a774514f | -6.60594 | -59.0023 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b66fa4c6-ac5e-3fe0-8d88-55a2dac113bb | -10.05902 | -60.50112 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eddf00ca-9702-3bfc-870f-b16f314b6d5a | -11.94707 | -46.35057 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5cff6491-1e43-3b6f-ae2f-282c1a788709 | -8.62139 | -47.45975 | 2026-08-12 05:10:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47986023-39d6-338c-b939-a089151e1d5d | -9.34289 | -47.49686 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ed5ea18-2b40-3956-bdf8-66c37c99e4b5 | -10.46908 | -46.61896 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6d5d2d4-85d5-345e-a0c8-53a4a63313ee | -8.95728 | -60.50957 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5a5ee0b8-1452-362a-a699-9d57cbcb3ead | -10.09937 | -46.21479 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2ff8fb7-92d2-3e8b-b8e9-c5df6aa58898 | -8.98234 | -60.59256 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be27af3a-59d1-3d6f-8e00-45f312b340b5 | -8.95849 | -60.5505 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 768e9fbb-db49-3358-a169-7aa95af0d285 | -11.98085 | -46.39946 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1aece7b0-97cc-3ae3-b75b-7b917587e72f | -11.21713 | -54.83203 | 2026-08-12 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95c33db3-cfbf-38c5-8d95-17452f5dd993 | -9.36598 | -47.44551 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e68adb-5b68-38a1-a942-7c99f8a842b9 | -9.58259 | -48.41843 | 2026-08-12 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f25f1ca8-83f9-32ca-9767-6bbbb90f937c | -10.21916 | -45.92874 | 2026-08-12 05:10:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7bcb55b-46ff-33ce-8b46-c12ace63e5f9 | -11.82533 | -51.84464 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c0f224d-6a43-3086-b4ec-754bb8aea484 | -11.97948 | -46.38187 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6652e06b-283d-31d7-ba34-c77ad74aca9b | -7.45534 | -46.14086 | 2026-08-12 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dcdd9c5-edf0-3f33-b7fd-5b7668b4ecdc | -11.78194 | -51.8623 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8ce377b-f211-3b2c-ba9e-b246bb555971 | -6.85643 | -46.01005 | 2026-08-12 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf9ed8d1-2513-3f48-bc1f-ad6b40539566 | -5.68588 | -60.23006 | 2026-08-12 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f129c4b-4859-3694-8f11-dfbfd727996a | -8.94524 | -60.51223 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bae8ed5-46ae-3c59-be46-9955eef81f2b | -8.95417 | -60.55167 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e546b84-b29f-3530-957b-247f51d2d5a3 | -7.38292 | -45.10743 | 2026-08-12 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44c94e05-5d00-3d31-9073-b647b204761f | -9.1328 | -46.38966 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c33136a-b373-3b59-a6b4-5de4b4969524 | -10.84352 | -50.34936 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30ab2268-f66a-3777-821a-cfef883ea08e | -10.21209 | -45.93663 | 2026-08-12 05:10:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5d0a996a-e74a-38e3-ba48-b095d290a4ef | -11.94881 | -46.38632 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d125c652-52c2-3242-8404-f3eb441c70a9 | -8.95315 | -60.55901 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c8d1b1f-5857-35ed-b8b6-4ba7b2287ebe | -6.04913 | -43.86648 | 2026-08-12 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36ed5580-c1c7-3cb2-bee7-ffe31f91fc24 | -8.95276 | -60.5135 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 817f4dd2-a0cb-3b05-9c47-cb2d0ecfdc87 | -6.54175 | -43.11665 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb862731-ac97-3cfd-809b-5aae17e5644d | -8.35186 | -45.97936 | 2026-08-12 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a0e4f536-44d9-33c8-9422-e08ba77b6cc8 | -12.16397 | -50.12872 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12418e08-9669-3614-a286-4ba3333ca7ae | -11.82506 | -51.85327 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 546bf257-68cd-33a8-8da1-a46368d5e677 | -9.34909 | -47.49101 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7006406-39cf-3e65-b740-0902a89aee77 | -11.9853 | -46.36102 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c75acd5-4902-30c3-9f22-5250fc26c5ca | -11.48896 | -44.57005 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce15be5c-6e03-3925-8f88-4528ebc07376 | -7.4053 | -59.99284 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a682c4c9-ab18-37ff-a8bf-0eb3422524a3 | -11.49237 | -54.60871 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d0b2c5-e839-3998-9041-d7e3380f85b9 | -6.61378 | -58.99937 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bba6263-0b29-36a8-aaff-50b12ab604b3 | -6.33604 | -44.0584 | 2026-08-12 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 543ed71e-a8a4-3cb6-b303-9f083f1829b6 | -8.946 | -60.50763 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d3b744a-3d23-3391-8646-d5beaa727f90 | -12.17717 | -50.16224 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f45bb679-229a-3f61-b865-3ed1bed0e84a | -9.97233 | -53.95025 | 2026-08-12 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bddadb0f-1005-35a8-bd6c-0152f1f68ca1 | -11.94976 | -46.32814 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a243d5e4-280a-36cc-8981-32ae5524cf5d | -9.07197 | -61.3851 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba2ada1d-6664-3b3a-9a55-4cb876d4f27d | -12.17357 | -50.11703 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d274902-0e0b-354b-9b8e-c3e2da87a451 | -9.47393 | -60.53186 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5213e5bf-e23b-3b05-a767-845cfb2a45cb | -8.949 | -60.51286 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa0149c4-3c04-3da0-b1fe-f3923ab6b4a2 | -8.95888 | -60.50329 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ee25111-cec5-3a05-9fcb-f58b2e2590b2 | -8.95181 | -60.58935 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d77ba79a-063d-31a8-90cc-ade897c0ca2c | -11.97794 | -46.39446 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8ed3c81-0f77-33cc-b2b7-5d513bed9fcc | -11.98327 | -46.37855 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e83b4d48-7215-355e-b3f7-f37174adc26a | -8.89815 | -60.5849 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 491a3882-ca23-3054-aeac-3812c1fafab5 | -8.66338 | -54.95711 | 2026-08-12 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 169d76e8-0c9c-3792-9cfd-b12681be8bb1 | -5.6409 | -47.10477 | 2026-08-12 05:10:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abe4cba4-5378-3201-b339-f13b65f1c3a4 | -11.48236 | -44.56925 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f12ec94b-deb7-3aa5-8afe-c487e755217d | -7.74445 | -45.02575 | 2026-08-12 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f96e0021-dfa7-3cd6-852d-690af34c36a7 | -10.36656 | -46.39427 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a572df86-9e44-3503-b025-f972480b7268 | -8.66 | -54.9566 | 2026-08-12 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b202ec42-7cdf-37da-ba62-58d4de8c8834 | -10.09437 | -46.21572 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67114f7b-2992-3d22-8f42-18045fac8227 | -8.95254 | -60.54002 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 51e11062-c72b-3f72-b4c1-207abfebf3c4 | -11.80518 | -51.81612 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f207bd01-0889-3f2b-bb08-20dfaaf1bbd1 | -11.94265 | -46.33705 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4c54e79d-0640-3286-9d76-3cdf9a76a4cb | -12.17317 | -50.15673 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6821d273-96ec-37f3-adfb-47c716e302a3 | -12.61394 | -47.86596 | 2026-08-12 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 378bd4ab-dd62-3801-95ce-4e1502ee1a11 | -10.36707 | -46.39022 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4955a5e5-654a-3762-a7b3-24fb126b08d5 | -6.34009 | -44.06334 | 2026-08-12 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ea1791c1-0e9d-35ba-a2d1-cad06f2f7cda | -8.95341 | -60.55624 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e319aa7e-7048-31cc-a532-545ac5164c53 | -8.94828 | -60.49392 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2989218e-5526-3562-aa6d-ab400af2605f | -9.13332 | -46.38555 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2587981b-2e1e-34b8-ac42-df8269c3c5e7 | -8.11345 | -47.18199 | 2026-08-12 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bc1f724-086b-39c2-93df-72d4c65b81e2 | -11.9828 | -46.38259 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4c528c08-5610-3061-836e-4e0cc1cbeec5 | -8.89736 | -60.58953 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92254078-a539-30d2-9871-fea2c3f18c2f | -11.82633 | -51.83718 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f671a731-14a3-3cbc-b87e-2633aab2d2f4 | -8.95175 | -60.54464 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 217d7ab0-756a-32ec-893d-91e65b8d5516 | -8.94147 | -60.51158 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fbf3fd7-c8bc-3d98-ac60-64c7387ff275 | -3.15231 | -61.11712 | 2026-08-12 05:10:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a18577e7-c40a-3868-9538-4ebb4655529c | -8.95269 | -60.53719 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7667b230-d599-35ef-94ea-c85d0a9cb16b | -10.05609 | -60.49601 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
