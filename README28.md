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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60c08b0e-8075-3d67-ad9a-100bdc2130b8 | -5.27384 | -43.36567 | 2026-10-03 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a88b7886-0229-3407-80c8-431f13fa5528 | -4.41393 | -49.97032 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ac8e4ed-95aa-3bc0-91ab-a8ab86dac3da | -5.15425 | -46.04219 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71044f82-335e-3f9c-990c-801d0e1b2a80 | -5.74064 | -45.1542 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 85757b99-044f-3d58-bd92-c2758d38364f | -7.83705 | -47.92582 | 2026-10-03 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bafa26e0-2ccc-3bf6-bfa8-9564b568f8e8 | -5.85788 | -53.46872 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 258313d1-f757-3a8c-84c7-b907d23548c3 | -5.7272 | -43.27846 | 2026-10-03 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26d70ef5-dffb-38b4-86ef-9d833e63f0ca | -4.27447 | -50.74535 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fab9fcc6-2fa3-3b6b-804c-c2234dc7bb09 | -6.30553 | -43.48684 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| efc1412d-d908-3a51-96f7-7b213d425aa4 | -4.4117 | -49.96285 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faf68618-0b55-3eee-b282-13e90753f593 | -4.29973 | -50.78259 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bb3a5fc-062e-3fe3-9131-8ab747b31cef | -4.27052 | -50.74846 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab5f2f1a-fb65-3774-a4e3-22a04f0f138e | -6.8374 | -59.25576 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84008c36-aa00-38db-b2ca-ab61f92ceda1 | -5.72659 | -43.28273 | 2026-10-03 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8d610f10-f849-3c39-9fe1-35d19d18168e | -6.84953 | -59.29076 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7ba227c-b2c4-38a3-9d5a-b6654dc686da | -11.85511 | -44.73646 | 2026-10-03 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4c22ecd-2523-37b0-8031-8ef47e0b3f57 | -9.47092 | -40.36919 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.2 |
| c94f8851-38a4-30de-b80e-b5ae4983078b | -4.30425 | -50.77589 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b6e1bbc-65df-3997-a7ce-7a51172474e3 | -5.95048 | -43.65262 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 656de96a-26a2-392c-86ce-fab4ed052098 | -3.85028 | -55.80071 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0a600a01-a613-3542-a03b-9a0f9c33de4b | -5.94931 | -43.66054 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 2eddf127-8aa0-3d18-aa37-1ebba63f485a | -6.20759 | -60.02519 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c724a4db-ddad-3091-bc3f-a8d4f9cce551 | -6.0618 | -62.5335 | 2026-10-03 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 138f5b53-9c0a-35c4-82b5-5115d9f44857 | -5.85223 | -53.47488 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9997fe30-6d08-38c1-9a38-8ea772a4a7ed | -4.78923 | -55.71581 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73e84aaf-a414-3754-85a3-52deddf00a03 | -5.95532 | -43.64934 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36152819-9332-3d15-8c82-a80c64890662 | -7.46258 | -54.98839 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04e0bfd6-e7a5-3b23-81e4-573d368e54ff | -5.74184 | -45.15766 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 214dd294-9b9b-3d88-90a8-8fbb043d0906 | -6.00331 | -53.52792 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dad862d9-b7a5-39cf-8500-ed86daa16f5b | -3.64028 | -55.50391 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d783373e-8748-38b2-b3a7-80ca279a6089 | -7.22748 | -46.04852 | 2026-10-03 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1887f35d-8218-3338-b39e-8e10260ae771 | -4.80782 | -49.86895 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85119b53-7cfc-313c-bb03-2f0eaea833ef | -4.43119 | -55.74702 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e76a6a94-c1fd-30ed-ad07-062126f28de3 | -5.37593 | -56.04517 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3683778-f210-3149-946f-cf9f079e69dc | -4.40729 | -49.96929 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dff471d-78bb-3bbf-be29-8e391affac79 | -5.94622 | -43.65199 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b829b02a-853f-338a-a8d5-a4f9797ab47a | -6.04434 | -59.93167 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4e9b55e-1dab-3625-97c7-3a561002ffb1 | -5.94873 | -43.66447 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0b57a694-7aad-3c9b-a4ff-837b37dc1d2e | -5.37518 | -56.04964 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5156c13f-d36a-3fd0-a338-9176f0c48caa | -6.865 | -59.3298 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56efa30b-b645-383e-b172-48bb60294dac | -9.46676 | -40.35693 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4928dd3e-073f-3534-8f06-f98392ab8ea3 | -5.13283 | -45.58113 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23847b92-582d-39bb-8ea1-2f726742b21f | -3.9154 | -54.42654 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01c29611-024f-30ef-b088-9ec3cc4b0caf | -6.34062 | -43.36295 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 026db4ed-e788-3320-8f85-5a20a9576b2d | -4.28844 | -50.78827 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3686085-44ba-3db9-a78e-aa9c8d8ff5fc | -4.1141 | -54.41136 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08ea120f-43d2-3e50-a5dd-50d397ad7ced | -5.74169 | -45.05394 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c1710aa-c332-35af-b8bc-2450e9e2adec | -5.13143 | -45.57874 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7b929b51-b571-3ac6-9747-f1268c2f501d | -7.47251 | -44.42403 | 2026-10-03 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c68ab7d7-2f39-31a8-8883-40efc595103e | -5.75028 | -45.15396 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 49807520-a7c6-3095-935f-d9fa21e5d759 | -4.26154 | -50.73966 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39f15da5-909b-32e4-9929-610fec754bda | -6.23898 | -53.14492 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 378b564c-680f-3282-af44-4855f1c886a5 | -5.7438 | -45.15955 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e784fc6-e270-3029-a755-9451376a947d | -6.21482 | -60.01799 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61ebd37b-9a5c-38c5-82b6-9b68095e530f | -6.33147 | -43.35924 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 917e958b-976c-3e5c-8e9c-5167f5edff66 | -6.10891 | -47.66615 | 2026-10-03 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 785bb8aa-e19b-3265-969c-c4d9f0d399e8 | -6.84436 | -59.25721 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f17da7a-9841-36bd-ac50-15b1bdbb5a13 | -11.85256 | -44.73832 | 2026-10-03 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca5bb61f-a056-3174-8fb1-d3a51bbd3201 | -5.64125 | -44.36643 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7948b2ab-a855-3e93-b49e-39c321adaa3e | -4.40066 | -49.96826 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b305e62a-617e-32ef-ac6c-1413e4ce209c | -5.9965 | -53.54583 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac644f8c-5812-3b93-ac0e-edd3d036633b | -5.85982 | -53.47559 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b239686-2a4f-3493-a4b9-7a168e7966cc | -11.20235 | -54.12711 | 2026-10-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e1549fa-ca10-3b7b-a1d0-5ec65c94a7a9 | -3.85132 | -55.97297 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2f4822c-7a65-3fcb-ae64-6ec94300a07f | -6.84044 | -59.27055 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48a98190-06f8-3a55-80d4-5c6715a309d2 | -4.79448 | -55.76656 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d485aeb2-9fca-3617-a360-70f20d94c309 | -5.06303 | -46.09864 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1be423f3-4df1-3e63-a97d-813959639d32 | -5.40456 | -50.16242 | 2026-10-03 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9e2fd35-2d25-3a22-a5d5-b32dc6d235ce | -6.73454 | -44.14678 | 2026-10-03 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 193e2e3c-680e-3d3b-91a3-120d1c9192a0 | -6.25028 | -52.68314 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9e76f0a-6e99-3013-9337-cc00790cba8d | -6.92798 | -49.62827 | 2026-10-03 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b50aa8d4-023d-334e-b966-1ecae001a3e2 | -6.2186 | -53.26541 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d67f072e-3801-3ed7-b343-f4096428a8be | -7.85962 | -46.6261 | 2026-10-03 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76832015-0ce5-3ce1-811c-e54808a26058 | -5.86091 | -53.47369 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f9da56c-b149-3a30-86bf-ac0e708cca66 | -5.73524 | -44.4938 | 2026-10-03 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fbae178-d657-3f88-bd94-851e65525974 | -4.79366 | -55.71645 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c645efaf-06bb-3a2a-8a05-97dbf9a324cb | -4.99049 | -45.6412 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15dc3a4d-35c1-3dcf-91c7-d18c924f849f | -3.64472 | -55.50456 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9915277b-a924-3c21-8a74-c5e7dbb949e3 | -6.23751 | -53.15181 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b35ac359-a31a-3f41-90c8-fd56f5c8340f | -5.74091 | -45.13775 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 220cf072-696f-3696-8b63-9a720d38049a | -6.01766 | -53.5346 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a088200b-c3c7-3351-818d-8b8f3acd08a0 | -3.76229 | -55.53258 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 352a95e7-92db-3b6a-8949-360b2509b081 | -5.8639 | -53.47887 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8124a4d5-6299-3abd-8be2-a91374be0ee4 | -4.79518 | -55.76226 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a210444-1284-380c-aa98-30e9499a71c3 | -3.64542 | -55.50026 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be5981de-1861-3dbd-a1ac-fa9e65c30d1a | -4.40839 | -49.96233 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d30edbd-6187-31b5-952c-8cc15bfaef6f | -4.16844 | -54.3345 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 281dd11e-01bb-3dfb-abb2-2186f3c67040 | -4.26492 | -50.74017 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7898f2fc-8e1d-33a3-8b01-a297bb81f3e1 | -6.21911 | -60.02729 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e15d7188-d935-3d0b-b156-ea47cb004fa0 | -5.89053 | -55.48772 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 20366a63-5eb3-31f3-b6c1-b4bf4abb32ee | -4.21228 | -53.56921 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5999c2e-030b-3354-bfc1-c0409fd89e75 | -5.95918 | -43.64808 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 446f1af0-dbc1-3cc0-b95d-fc7688ebb6ec | -4.29578 | -50.7857 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ea8a62d-0fd3-3b7e-be1c-87737f9a0530 | -4.27946 | -50.77942 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc7ef80a-0953-3738-a18a-68e4baf290cd | -5.13956 | -45.57541 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a313b1ae-9951-3ec7-ab0b-8623b13c8eaa | -5.60706 | -48.84391 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f22ace7-3a46-3855-bd35-c3253491ee2b | -5.94164 | -45.39737 | 2026-10-03 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0473d23c-8b05-3390-b889-b095d0b1ca11 | -7.02549 | -44.63511 | 2026-10-03 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9cfbce6-fd09-344a-a777-894611700f4f | -5.09115 | -56.25421 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fadb7cd5-b374-3cc8-812a-173fe1d92443 | -4.41197 | -55.7525 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README29.md)
