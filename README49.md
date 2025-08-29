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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 416c30cd-23ec-3f81-b8ff-4aa2344b5eb1 | -8.92137 | -48.50874 | 2025-08-29 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9aca64e-3f90-3fb2-bbb5-e2870b26de5f | -12.66665 | -48.18523 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45ae0673-276b-3ecf-8b2c-42eb13ff8b58 | -11.5437 | -47.31115 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bc807dc-ef70-3b36-93a4-31217d90952d | -12.84765 | -48.13652 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ccc0c2b-a6d1-3d8f-87bb-ece6250d05e5 | -7.73475 | -50.2942 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5787d174-ba8a-3762-a1b9-4274b2561ea7 | -11.06418 | -52.02249 | 2025-08-29 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcc53645-26c8-3f2c-84e5-5463f2fd12fa | -10.72697 | -47.01658 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9fe49eda-3db8-376f-a97d-f2758114f1bd | -10.45476 | -57.96598 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6587735-d2c7-3bfb-88b8-4beaa4227a21 | -12.09129 | -44.73014 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 41a49eb1-733b-3e08-84a6-51ad326adfac | -10.98275 | -46.90541 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f555d213-e26a-3c47-a09f-efc6bfa73926 | -12.69558 | -48.1608 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4300a3ab-0f91-3f6e-9a5d-04fc04a056eb | -6.81622 | -44.33236 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38f39fe9-0771-32d2-976f-3ef684b7abaa | -6.48673 | -44.39792 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 027a02c3-68a3-3363-8604-91fca9d70044 | -11.28921 | -43.54395 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 838d859c-e73a-3e2d-9433-02071e97f42e | -9.94115 | -46.35447 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64c7b6a8-c388-3c1b-a407-62c5ce78d7d3 | -10.48453 | -57.96191 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3eaf9b3c-b479-36d0-a618-c543f65adc22 | -8.46809 | -43.63926 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edfee5c3-d251-3379-afa8-52c64e38924f | -6.44769 | -44.57704 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f22fc132-f5a8-36f7-8a45-95340c3a81de | -6.19426 | -43.31922 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5433a55d-1455-3071-ab0b-50469016688d | -6.26281 | -43.81553 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dee34451-d625-3aab-95c4-fb2de0da5f5f | -8.55999 | -51.3164 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49fcb94a-f48f-3d86-a60c-7dc4723e905a | -12.91233 | -48.11111 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e4d040a-2fd1-3b0c-b519-9972293e6c4f | -9.44681 | -48.25351 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef1ac185-32b5-3d7f-92e2-346978320954 | -9.59774 | -40.36053 | 2025-08-29 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| d39ce522-14b0-390d-9163-06a0ead9dfee | -11.54004 | -47.31062 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25ed67a2-f3aa-35ca-9906-9a7d7d302e9c | -11.37715 | -54.34182 | 2025-08-29 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 769eb1a1-d9a7-30c3-9bba-c1e1f37df86a | -11.22814 | -55.05035 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 085e606e-d474-35f7-9f24-17d7b6ab9e5d | -10.97838 | -46.90932 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cfed8a2e-4e24-3a1a-a783-709fe4afbee4 | -7.60994 | -46.24115 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29d4d8e6-8d2d-31e3-9329-36d58e10a344 | -11.02824 | -45.07132 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 999b531f-c344-3da3-be45-915984944a37 | -9.46235 | -60.55932 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 962a9b4b-559a-3def-b660-1bb82b773366 | -6.49079 | -44.39866 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21bffb73-5597-3e7e-b6b9-96101a824a65 | -9.46089 | -60.56724 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 162df708-465c-3eae-923e-391e91303d3f | -8.74724 | -47.39363 | 2025-08-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04e11397-297b-38c4-91cd-dc82c5430448 | -7.64818 | -42.66443 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b1aff7ae-da71-376f-9b04-2de35f313535 | -12.09561 | -44.73077 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e2250f20-d143-3c18-b3ba-b0fc4f921157 | -12.86076 | -48.09681 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fed2f0a0-6014-3df0-8f7f-4846833b0a53 | -9.96236 | -46.49895 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14bfd2da-5158-386d-ba16-f7e2bc695d16 | -6.47887 | -44.08299 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fca2799-6f54-383b-873b-71fb90cb1ef5 | -10.38522 | -57.82888 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6a488e3-9140-37d3-aa46-d13c7131956d | -9.46801 | -60.56042 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 499d928c-3965-3abb-84dd-0be65e0eb0c6 | -8.29799 | -61.40688 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86b64133-4e03-3894-a771-5480c5073ad7 | -12.88973 | -48.14163 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e62e21b-a764-3c45-b87f-3743df0ab781 | -9.16052 | -60.92672 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 28ce4190-cb02-3654-aeed-2696e649f94a | -12.86482 | -48.14355 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82b340b4-b319-3d3d-aa5d-10ac821495be | -6.54555 | -43.92071 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0878959b-9008-38e2-9b2a-c79634afc7d8 | -10.36956 | -57.83587 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 463d4615-2b64-3bf2-b8e8-a71366e38965 | -7.74133 | -50.27391 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7114d570-b97d-3710-ad74-da35125ffaef | -11.22732 | -55.0551 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be5dccbf-9212-3235-afa3-43afdad3f40f | -6.47834 | -44.08664 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90bc7d9f-fe66-3119-961c-c6e32477e59f | -12.70805 | -48.14995 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7ceafc0a-bc6b-3695-a707-29c59911ace4 | -6.33832 | -58.18801 | 2025-08-29 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd75bcf8-ee2b-37ec-947f-e392365f46a8 | -11.21882 | -55.05855 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 514280b4-ea6c-39f9-b768-3cf023d880ce | -7.62129 | -42.72096 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59778552-7e00-305b-a690-3c3d3bab0141 | -6.43564 | -44.57504 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 890d15c3-b2ab-3fa6-9238-e437e0dc21c9 | -6.1663 | -47.27676 | 2025-08-29 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bd45c138-a23b-3ef1-a256-b09a6546db2d | -6.22311 | -43.36728 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 728406cb-cdcc-30b9-aca4-a213a8ef1ca1 | -7.81308 | -55.22759 | 2025-08-29 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 308c2451-8798-3e42-8dbd-e9a252710166 | -6.39044 | -45.23215 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bbdeb7a1-df90-320c-a3ef-62e27fb90278 | -9.42958 | -47.64583 | 2025-08-29 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdacefd3-111d-39c3-977f-d8a07c2ff4aa | -10.07812 | -48.85705 | 2025-08-29 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae7b2831-c49f-361f-9d93-3d0f9ec18de5 | -12.69439 | -48.19397 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 4a1bd308-2ba0-3b89-8c57-239f45e051b3 | -8.07103 | -45.03648 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e00ef89b-fc5d-3fe4-a2f7-93f3f5f46882 | -8.69524 | -50.39475 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8af261ac-7e5d-316d-b4b3-e06be0076a41 | -6.24795 | -42.39709 | 2025-08-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c5902c93-fc9e-3f15-b487-1c94913c7481 | -8.44303 | -43.65754 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 79c03c9b-013e-3104-9328-c832ec61b573 | -12.92662 | -48.13834 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1905c475-c22f-3204-a2b1-205308dac87f | -11.64233 | -46.37737 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 692782fd-f8d2-38d8-9436-ec5d8b2dc69d | -7.0187 | -42.01946 | 2025-08-29 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 662d7f47-7138-3f6b-9614-cebb20ffbff0 | -7.04498 | -44.36208 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93e520c4-effc-3bdd-a6f2-7dc833b6d10f | -11.06031 | -44.76875 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5067efe2-fbcf-3fff-b97f-32790191c01b | -10.38003 | -45.17096 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e231b09-9f22-348d-bf0e-b90a0aa320ce | -10.84666 | -47.5036 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa2cd7b7-2f3e-3734-8041-f71312dd434a | -9.46333 | -60.56703 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ec1f18ad-fe2d-3600-ae83-2b0139c887d4 | -13.67304 | -44.21979 | 2025-08-29 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9cf7160a-1636-38bf-ac84-be40e43448b4 | -8.17065 | -61.37828 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0310577-c55c-3423-bcc5-32d2633fe4cf | -10.69601 | -47.07444 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e46727dc-5393-3a6f-96e9-ba2c13b89736 | -8.70571 | -47.86767 | 2025-08-29 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a92a0df7-87d5-3f9a-9504-d304cd938a7a | -7.56525 | -47.5052 | 2025-08-29 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba4825a0-69f1-3f78-b63c-44025118dc45 | -9.15722 | -59.53316 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b65681a0-7d2a-3604-b8d9-93ed7b511f15 | -6.70396 | -49.4715 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e204e463-dedb-3d37-a67b-8b549685c984 | -6.54141 | -44.10324 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6c6970f-5802-30d8-91ae-7c622ebefdfe | -6.48953 | -43.53919 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbe0d5fa-04b1-3d07-8cda-1655a22b07bc | -6.70066 | -49.47099 | 2025-08-29 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea0aece4-6333-361b-acb5-d5e2d5d4cdd7 | -10.79887 | -46.35972 | 2025-08-29 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1f518ab-df3c-3930-a96a-a80f9e6ed5f5 | -9.18457 | -60.8609 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83489799-1f09-3d19-9d39-4a29634bb53d | -5.56667 | -52.07144 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76d2b895-4c78-3b59-bad7-aba3c8020dea | -11.40732 | -46.91442 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69002f7b-ea0d-326a-8ade-1faebe6bb370 | -7.10789 | -44.59124 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26a21356-94c1-357b-ab44-9942e099bbc3 | -11.24088 | -45.46563 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e62c6d9-a49d-3980-a095-5ae99f03fa98 | -9.94188 | -46.70445 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3ad3b29-10aa-3495-a16d-4bef0550e196 | -10.9672 | -47.39573 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcde2b41-4d11-3c42-95b3-de84a67e79a3 | -12.82271 | -48.13282 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67c90953-03aa-3c9a-baba-fb321baae48f | -6.54076 | -43.92398 | 2025-08-29 04:40:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52a046ac-6a22-3762-add1-b94bbfeede7d | -9.23552 | -59.78407 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de228a2e-a016-398c-974d-9c35748cd266 | -9.9329 | -46.3581 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cecfcb2-d03f-3ce2-bcb1-7413bf78b841 | -12.8642 | -48.14202 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 32f9a38a-6039-3551-b0de-fb7aad28bcf8 | -11.35336 | -43.54958 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa4c7f6c-0424-3005-935a-28e6fb307642 | -6.1086 | -43.32043 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ccf544a-a991-3612-a19d-656a63466a0d | -5.33427 | -51.33035 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README50.md)
