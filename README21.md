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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d86d0d4-2fd8-3811-8981-613fe1b05257 | -7.34849 | -45.00167 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c42767a6-3f36-3baf-935f-87fef11bf776 | -6.56956 | -41.58607 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1304ad7c-0472-355f-bfed-e3df6a46bff0 | -4.90553 | -45.72885 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7d243d0-8f34-3d96-8670-44d04b0a637f | -3.60219 | -50.62367 | 2025-10-31 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5aa046f5-34fd-3575-a63b-3f34a48105f7 | -6.08619 | -44.54253 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56d821b8-a24a-3995-adfd-c8d44ecc5d48 | -4.05775 | -45.6307 | 2025-10-31 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc27551-6a0c-3292-a945-82c703190ca9 | -3.47869 | -46.01748 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60143382-263b-3758-b737-2fe076bb64fc | -5.60062 | -44.91444 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19aaccf7-e80a-332c-b01f-053079c43690 | -3.45482 | -45.98786 | 2025-10-31 04:06:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97009a58-1f78-3f27-b61a-eb5614573b94 | -3.01996 | -49.44638 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 1f5394c4-d9f3-3662-b905-4701f10e7c21 | -3.54879 | -46.43241 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab89cd3b-477e-3635-8e14-6b56a2303871 | -5.45476 | -42.71766 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 14299a96-7dfb-3656-96d4-7e5f8d5bdd97 | -6.52954 | -43.71347 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7c7754e-7638-3640-adea-bf949242d360 | -2.63766 | -48.50702 | 2025-10-31 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae527886-0609-3520-ac40-b898064244d3 | -6.34175 | -44.35775 | 2025-10-31 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18ae07cd-4b5c-3722-9459-cbdd0e38a665 | -5.63286 | -42.81209 | 2025-10-31 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a8325737-abe7-3c33-8484-2c847089efd3 | -2.49022 | -48.15352 | 2025-10-31 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce230405-8266-3e68-9e41-299abebd4f5c | -7.39558 | -42.46193 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 16763057-16f4-3cb3-b34d-aacb9bee3be6 | -7.39239 | -43.01434 | 2025-10-31 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee51c8b1-ad81-364b-b8db-9fd789540694 | -6.06838 | -47.28846 | 2025-10-31 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c14fdc80-c4ae-300e-9089-f7572f528807 | -5.92846 | -43.37193 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 047d95bf-5a92-36cd-a753-8a08d4df9562 | -3.08554 | -49.50312 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 496c28bf-9b7b-3f6b-89ed-f4d3471a05c3 | -5.41858 | -44.83841 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4063a84c-8bad-34d8-b17c-c0356b36b223 | -5.64247 | -43.27286 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e3a877e-05b1-3882-84b3-19049664bd82 | -2.96859 | -45.06133 | 2025-10-31 04:06:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f20fdcdf-4a14-3277-96bd-4f748e18f34d | -7.75925 | -39.74291 | 2025-10-31 04:06:00 | NOAA-20 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a435c43-b378-3c00-b0db-8b1d937d9441 | -4.23615 | -48.37318 | 2025-10-31 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4a8b8be-a827-30ed-b081-e8375ca07f1c | -4.63599 | -49.48804 | 2025-10-31 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bf8d9b3-0056-39a1-acd9-cea7636f6b61 | -5.03764 | -43.61684 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 3b083907-fdcb-3349-9142-13112cfedb07 | -5.06288 | -45.11331 | 2025-10-31 04:06:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30625970-f2cb-3ae5-9897-5b4745b7e4e8 | -3.60426 | -45.15802 | 2025-10-31 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c5c584cb-c2db-3bbc-ba68-d048723fea25 | -4.47269 | -43.43848 | 2025-10-31 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c9ac0577-eb07-3b03-96db-fe44c7b33419 | -5.31632 | -44.84612 | 2025-10-31 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bd3a12a-e748-3657-b62d-230b1b5de22a | -5.1407 | -46.13465 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ccaf8aa8-933f-35a8-a894-0c9d9b3dd6cf | -5.93436 | -44.8469 | 2025-10-31 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 180b9694-50f5-3f61-b6e7-614026062589 | -6.1905 | -41.59671 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 389bd15d-4227-3f71-bb61-77b3a5b03a6c | -6.06907 | -47.28442 | 2025-10-31 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f9b7d25a-0bc0-3391-8598-a4ad6e3b5221 | -4.80905 | -43.0248 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 09407e50-cee9-3d30-9b38-2c76bf760087 | -5.67876 | -43.57362 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 496052a7-1c49-371e-a92a-43b5219591d9 | -4.83656 | -45.80473 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb26fa5c-69c6-3ae8-9540-e5a1d91b9e0d | -5.02016 | -45.56769 | 2025-10-31 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 871540ba-341e-35c6-8241-2a61da7174ab | -4.4591 | -45.75674 | 2025-10-31 04:06:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 225b48ce-ccca-3058-97e2-bab689fe87f2 | -7.34444 | -39.33707 | 2025-10-31 04:06:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd9897b4-c73e-34a7-b8d0-27d7318cde0e | -4.8561 | -42.73461 | 2025-10-31 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4dba1e29-900a-39f7-ba5a-819db7f41116 | -5.45526 | -40.87226 | 2025-10-31 04:06:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 59e02b96-1749-3d45-9b00-384435dd6d60 | -3.95419 | -43.25991 | 2025-10-31 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c89c40ef-0350-3e8d-813c-e627dff67c51 | -2.31183 | -48.58142 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| deb47367-c1cb-3967-8b6c-517694fd7ed6 | -4.85949 | -42.73515 | 2025-10-31 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e909b46-5fa3-398a-8fa6-9fad077be91b | -4.83309 | -45.33421 | 2025-10-31 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b21e28b4-e881-314a-ae41-a27fa2907aa0 | -7.36568 | -41.87929 | 2025-10-31 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c88d5591-674b-345f-8526-4d687b3bb145 | -3.42338 | -45.42788 | 2025-10-31 04:06:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 70c81b27-9497-30ad-9c9b-d0cee4831876 | -6.11022 | -41.71851 | 2025-10-31 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| fdb2a6bd-b16c-3518-94dc-23c45ce9f5e8 | -4.67548 | -45.81041 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d37a132f-409b-3807-a501-7193cfbd40d1 | -5.4104 | -41.24291 | 2025-10-31 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3574fde3-bb10-3faf-8903-81895dd18e4e | -7.22864 | -39.36286 | 2025-10-31 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 681459ec-0ba6-3058-9c2b-d8166c810153 | -7.3492 | -44.9974 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ca9deb51-8860-37b5-8c0b-ca967bde10dc | -4.0242 | -46.20275 | 2025-10-31 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a1586f1-bfad-39e9-bcec-9c02bab70127 | -3.39145 | -42.35246 | 2025-10-31 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d69dca8-0461-32d9-bd53-1c41d6e45dfc | -4.63496 | -49.49403 | 2025-10-31 04:06:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 251082e5-8404-32d9-9e97-38deb6b93ceb | -2.08073 | -48.36826 | 2025-10-31 04:06:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d972f60c-c0cc-31df-94e9-cbf5b035cc34 | -7.00177 | -39.13367 | 2025-10-31 04:06:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c3734c0-38bf-3075-b1e6-cfcc41eb0fbf | -4.77831 | -44.6055 | 2025-10-31 04:06:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 891464eb-ac45-3353-8fa3-27ba6b766f4c | -3.52591 | -47.55049 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6092a9ef-ccfc-32ff-b550-7388ee799693 | -4.30369 | -41.43187 | 2025-10-31 04:06:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8fe1f7eb-26ab-37ed-aa44-51791ea22a1a | -5.54231 | -38.03592 | 2025-10-31 04:06:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a180518c-7ecb-35dd-b667-7ec59a672136 | -3.52966 | -47.55584 | 2025-10-31 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d89c565-9de2-343e-bafa-c35468eb05b7 | -5.80253 | -40.82475 | 2025-10-31 04:06:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e14b79d7-b05d-31ac-bba1-c6e32094d2e0 | -6.01311 | -41.96618 | 2025-10-31 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 970462d4-6272-3bb0-bf8b-45375056da15 | -6.27268 | -41.8079 | 2025-10-31 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb934ecd-12da-3788-86c5-ae2ba2f3b8ab | -3.23021 | -50.65777 | 2025-10-31 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dc2ef8a-9ec5-347a-b34e-6b547fdd583e | -6.36316 | -43.71895 | 2025-10-31 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96754ff5-407b-3177-a562-ee3c0a124d32 | -6.2364 | -42.52568 | 2025-10-31 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1cc29ee8-03b2-38c4-95e2-6fc1243bbf55 | -3.8672 | -48.03475 | 2025-10-31 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5503900-5a89-37b3-92f7-44be09646209 | -6.55976 | -42.86723 | 2025-10-31 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 309a334c-f7b3-3d02-ba25-7862b18f5e5a | -5.21889 | -43.75303 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a171851f-27c4-3885-978d-9ad737128a30 | -3.78718 | -43.89807 | 2025-10-31 04:06:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9003a50b-cf3c-31be-862f-228aeac08944 | -3.01889 | -49.45271 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 14c64b9a-f59f-3a17-8753-d39a90a4b63d | -5.11623 | -43.29513 | 2025-10-31 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0bb2b124-18e5-3e4c-becf-076d33225003 | -7.33406 | -42.46289 | 2025-10-31 04:06:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42299ee2-d0b4-3d84-b49a-3f097dafff0b | -3.93241 | -46.0494 | 2025-10-31 04:06:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6275e27d-f7d9-39b7-98b0-947b3c62e720 | -5.63845 | -46.80516 | 2025-10-31 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12353c65-791a-396c-884b-5b9e2290b812 | -3.147 | -49.4264 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e976b8f8-907a-3395-ba83-797ff43ccd71 | -6.01974 | -41.96723 | 2025-10-31 04:06:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ec786408-1258-3524-a94d-7492e25ac9bc | -7.36899 | -41.87981 | 2025-10-31 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 568366d4-8f2f-3752-8b73-bf6207556442 | -5.20322 | -45.41376 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2adf0893-6035-3c5f-b13e-c04e9820efb5 | -4.67068 | -45.81496 | 2025-10-31 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcbf1e44-0711-3be8-9056-e3afb7febfa5 | -6.92001 | -42.24619 | 2025-10-31 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5831ce8-a415-3330-a2a2-a4fadf8c1058 | -5.05677 | -45.93396 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee10c9a4-ee02-3992-86bd-b62b115f8760 | -7.62225 | -43.57043 | 2025-10-31 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f43f1e4b-bd8a-3347-aef0-bead5045fea8 | -2.42401 | -49.30393 | 2025-10-31 04:06:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd0b9ff0-bbdf-3514-8f06-a7f0f3a0408f | -4.94304 | -44.92341 | 2025-10-31 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9596ca78-2e4e-3856-9d01-85fe8a7cf6de | -2.44776 | -49.03223 | 2025-10-31 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8816b749-eb63-3691-a382-2cfc11cfc770 | -6.18707 | -41.51129 | 2025-10-31 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2fa6134b-ce8c-3a65-a9d5-612049ac1203 | -5.07224 | -45.76557 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df8590ae-3f01-3a64-a422-37e8a6e09198 | -5.69312 | -43.15538 | 2025-10-31 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 327a86e5-411f-3f27-b7f4-aa48489899f8 | -3.6009 | -50.63129 | 2025-10-31 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c26180d3-85f0-32e4-b1d5-e80ab8958908 | -5.36891 | -45.52218 | 2025-10-31 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d83ebf77-1452-37cd-87e4-46e2cde7286c | -4.86276 | -45.79322 | 2025-10-31 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 442d0f1b-d78a-3a6a-a354-9243f6c7ee1b | -7.36746 | -44.62973 | 2025-10-31 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ba48e5d-20c4-314a-a898-efbf8a201254 | -6.21435 | -43.94202 | 2025-10-31 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README22.md)
