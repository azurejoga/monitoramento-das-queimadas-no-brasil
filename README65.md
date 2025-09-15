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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e400fad-7324-3b81-a70d-7d47c1bdbca2 | -20.4101 | -54.62986 | 2025-09-15 05:14:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73ce7d76-fc8a-32ba-b85a-7221f3ba3635 | -22.26967 | -56.04788 | 2025-09-15 05:14:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0a1ca50-520b-3991-bc3b-d89553f480c7 | -18.97734 | -48.59139 | 2025-09-15 05:14:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f48d0dbc-f7a4-312b-be13-9dd68f8a9c58 | -20.90759 | -55.17006 | 2025-09-15 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ea5d09b-3189-31a2-a88a-e771935f42ea | -20.73993 | -56.74387 | 2025-09-15 05:14:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11b17e01-cff0-32e2-ae5f-5f687f58e81a | -21.62881 | -46.81944 | 2025-09-15 05:14:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f9f1199b-55be-350b-9d56-dd65e8cc55a2 | -24.84458 | -50.35546 | 2025-09-15 05:14:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89ad8254-e382-33e7-9547-742eeb0c3829 | -20.77535 | -56.93158 | 2025-09-15 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8910f03-e642-33be-b8a3-1fe6119b21a9 | -20.52177 | -55.63596 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 441e9b1a-86f3-36df-80dd-5ccac9c967a1 | -21.92464 | -46.56638 | 2025-09-15 05:14:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b4aeb59d-99f2-35d6-8a85-1503bdb22bce | -20.96354 | -54.98593 | 2025-09-15 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ea94f97-5211-3d21-8f7c-b02509863e2d | -22.29787 | -47.95328 | 2025-09-15 05:14:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06f447dd-2c50-3be3-9aaf-96f66cf97651 | -23.47065 | -47.36946 | 2025-09-15 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fe767522-07be-3157-ab32-d5a4407061cc | -20.52397 | -55.63815 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3aa5c62-06a8-31e3-b8b5-d4a17c10725d | -25.19313 | -51.37764 | 2025-09-15 05:14:00 | NOAA-20 | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a0984325-2471-34ee-ba86-72dbd2eae597 | -22.658 | -53.1143 | 2025-09-15 05:14:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8f5ba501-3f54-3eb1-9729-5c008a9b3268 | -22.04921 | -56.08976 | 2025-09-15 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b083a6e0-10ce-3e2d-9846-35b61ad31aa9 | -20.77165 | -56.931 | 2025-09-15 05:14:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39ec83ed-904e-3dad-a8e4-f8f47e4f54f7 | -22.66223 | -53.12048 | 2025-09-15 05:14:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c86d66a1-82c0-389c-9dca-7638e40a1b47 | -22.66703 | -53.12108 | 2025-09-15 05:14:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8492a664-9211-3fbc-a0bc-07ffb8d91883 | -20.88773 | -55.17318 | 2025-09-15 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19b01abf-976f-3334-b500-bd2229c0a758 | -20.23495 | -46.17669 | 2025-09-15 05:14:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 53fd984e-8bd5-3c70-8009-ced12aa4c7f1 | -20.40958 | -54.63399 | 2025-09-15 05:14:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 064da5e5-aa6d-353a-8724-e7944331c620 | -23.47751 | -47.37016 | 2025-09-15 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f6796f88-3990-3ed4-8db2-a67fc1402e57 | -22.50303 | -52.97984 | 2025-09-15 05:14:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c6fed177-ad15-36f5-ae6b-4aba62e0ecce | -20.51711 | -55.64059 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3607fb4-1fef-3120-ba43-aae7bdab91e0 | -20.52331 | -55.64346 | 2025-09-15 05:14:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9271262-722f-3acb-92a7-f80ddf5f1382 | -23.47018 | -47.37602 | 2025-09-15 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 633ed4a4-2b45-3c16-9ebf-55b7cb47bf04 | -18.97846 | -48.58241 | 2025-09-15 05:14:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d1185ad8-b703-3a7f-94b9-4383c4d8eb4c | -18.97802 | -48.58713 | 2025-09-15 05:14:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0756f04e-0708-3986-9258-9f5c330cd472 | -22.19944 | -48.36058 | 2025-09-15 05:14:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46281b91-3871-3318-af29-133638bb0c39 | -18.97759 | -48.59181 | 2025-09-15 05:14:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 12050f99-2b4a-35b9-975b-a3d5bf9f008a | -22.50786 | -52.98052 | 2025-09-15 05:14:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7c069ed1-6d2a-3ce6-a4b0-bc1b0f81960d | -22.04526 | -56.0892 | 2025-09-15 05:14:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c379a12d-072c-3af8-95e4-c933a3dbf03d | -20.52668 | -46.86496 | 2025-09-15 05:14:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86f41d6f-0f20-3b6f-90a1-c2841ae1b05f | -23.47123 | -47.37072 | 2025-09-15 05:14:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3577492-a4cd-3b38-b21f-5d99a82c34f9 | -21.92513 | -46.5595 | 2025-09-15 05:14:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 99905bc7-75e9-37fd-a0a3-e59ec8699efc | -20.90516 | -55.16766 | 2025-09-15 05:14:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ccef4c3-cc84-3330-be1d-a54d65ab329d | -18.95695 | -48.21742 | 2025-09-15 05:14:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9da96224-baaa-3a4b-915a-632dcf9eeb7f | -26.08048 | -52.17899 | 2025-09-15 05:16:00 | NOAA-20 | MANGUEIRINHA | PARANÁ | Brasil | 4114401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 94b4c084-6187-35d5-8bd2-6e23526e8544 | -15.8621 | -59.398 | 2025-09-15 05:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c5ec0b69-0f2c-3633-8abc-d2b20b9e4690 | -15.8621 | -59.398 | 2025-09-15 05:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ea8c8604-fbd3-3006-9495-5154ba10e022 | -15.8621 | -59.398 | 2025-09-15 05:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 111b6bac-d02a-352a-a2e7-0150e4130f80 | 4.30793 | -60.96296 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b0d7608e-d13c-319a-af60-03c6821a18c7 | 4.30343 | -60.96393 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 054348ad-4ffc-3ed6-a5c1-a12144e2eed1 | 4.30596 | -60.96994 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 96b0cafb-6e49-3495-8ec6-377ec3a8c723 | 4.30521 | -60.96547 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b089d157-9a13-3e0f-820e-61fb2cb7bedf | 4.3124 | -60.96183 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fe6029fa-8219-3bdf-aebf-c45a138cf070 | 2.04153 | -61.18124 | 2025-09-15 05:57:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa71d1d9-91a0-3dab-b0fb-c1b1275304ea | 4.31337 | -60.64953 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 991cf7db-32f2-35dc-a7ed-9b17efefabad | 4.30415 | -60.96839 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3be53fa6-322e-3915-b2e7-ae712a754116 | 4.30969 | -60.96444 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a06bc1fe-506b-301d-b098-3a8a17a202eb | 4.30891 | -60.95986 | 2025-09-15 05:57:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 764df201-1ca5-3004-b0ea-194c0201409b | -10.21448 | -69.04587 | 2025-09-15 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abb7b1f8-b473-3753-bba6-017eb492892a | -11.79704 | -62.74114 | 2025-09-15 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 113dcce9-9524-30ed-8149-f238f363451b | -9.23736 | -65.32725 | 2025-09-15 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2b25c44-4b89-37f3-b855-a7b54edb52d1 | -8.60692 | -69.92138 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04ff915c-d1db-3949-87df-0a1d75ae1135 | -7.79473 | -71.98996 | 2025-09-15 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d7b134-79a7-3073-862d-aba5fc928f5b | -11.79413 | -62.74478 | 2025-09-15 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cd2c39d1-8e5e-3391-acf9-9700aab7296b | -9.49624 | -70.43757 | 2025-09-15 06:01:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18db3698-9329-37a5-aced-a258f7af7c4d | -11.75376 | -63.11864 | 2025-09-15 06:01:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42186e8e-8ff1-3aa5-a1bd-714f45e8d79d | -10.21391 | -69.04964 | 2025-09-15 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a35bc6f-f548-36ec-bd7e-f44030cecb95 | -7.66896 | -72.3335 | 2025-09-15 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e7dc376-82ea-3b77-a2fc-c6b0141802c0 | -7.80146 | -71.99104 | 2025-09-15 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54141b47-a5e0-36d4-8f7b-6ae8975462dc | -8.45802 | -64.13923 | 2025-09-15 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c67f0dc-7bd2-3b1f-8462-216e0805805d | -9.23792 | -65.32317 | 2025-09-15 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2248ddea-a7d5-3c15-9bee-fe1663ec6d7a | -10.58199 | -69.05014 | 2025-09-15 06:01:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8766272f-e3b1-3a07-898b-5362c65c078b | -8.25587 | -70.51777 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89c39129-53b2-3318-8672-d1bb8e931f42 | -11.75412 | -63.1157 | 2025-09-15 06:01:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a79cf01d-32c0-3092-8441-dd6075c7414d | -9.69317 | -62.00171 | 2025-09-15 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f14a808b-6e64-3275-975a-dd083ed3a064 | -9.69275 | -62.00494 | 2025-09-15 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a61cda40-ee0e-353b-a75f-9c68e59a2068 | -7.79809 | -71.9905 | 2025-09-15 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f591163c-f68a-3760-933c-789c0f453a1a | -7.89208 | -63.69354 | 2025-09-15 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71653dbc-0160-3b54-ba86-3870e130e6c1 | -7.37271 | -72.77763 | 2025-09-15 06:01:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4f23d0c-92c3-38c7-a239-f5e38cb96c76 | -12.0543 | -63.12076 | 2025-09-15 06:01:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce012f41-238f-3a99-9988-8df5f98db6d6 | -8.6097 | -69.92539 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd930398-d92e-3c39-ae19-47bc48955d07 | -8.7412 | -70.54507 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5cd8c81-dabe-3b05-9bb5-b80e1a4c76bc | -8.07229 | -69.96946 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa2b96c4-9dbe-3ecc-8181-de5f18c02e32 | -9.68835 | -61.99773 | 2025-09-15 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e729f4e3-1c5f-3169-b118-42af55cef9f3 | -7.89143 | -63.69818 | 2025-09-15 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 708b0e35-1739-381d-9002-798521423a5e | -10.78399 | -69.75562 | 2025-09-15 06:01:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c87a3c8e-69b6-3ed5-a6ba-ad144dd89b24 | -7.80204 | -71.98743 | 2025-09-15 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99d0ffd4-548f-31f6-bbcd-4f1c66b654fe | -7.79136 | -71.98943 | 2025-09-15 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a235e87-291c-3856-b9d6-2b2673ed167f | -9.69358 | -61.99848 | 2025-09-15 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02bf205a-93ad-3101-97a8-3f0af9d030e7 | -8.74174 | -70.54161 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9dac9fb0-4145-3f3f-8f1f-12623fe867e8 | -10.21734 | -69.05016 | 2025-09-15 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fb3746e-d3ab-38c8-8184-c88fd293ab71 | -7.82849 | -71.97312 | 2025-09-15 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a0bb315-c25b-3221-af07-6a7cebdf27c8 | -8.60638 | -69.92487 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75786984-94ab-3e7b-ba70-c77c3feccfa2 | -12.04928 | -63.12007 | 2025-09-15 06:01:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c1f769-22d4-3e3c-9f8d-a723c0c3982f | -8.74228 | -70.53815 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10116a51-127a-3c8b-a7fe-39c5318fa4bc | -10.2145 | -69.39206 | 2025-09-15 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92a2d210-480f-398e-8d76-de0fd9625f56 | -9.25833 | -68.2451 | 2025-09-15 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a182ccfa-7b89-3060-8886-0fef8d5fcc52 | -11.75384 | -63.11436 | 2025-09-15 06:01:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 920cb958-f732-3020-916e-8721f352f4ec | -8.53926 | -70.35704 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22a50560-0cc8-3d1c-94a2-a0568f403012 | -10.85658 | -69.41364 | 2025-09-15 06:01:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8afd653-f3a2-3d05-be47-76baba1e33c2 | -10.06656 | -64.9838 | 2025-09-15 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97a6e854-4971-3ef8-a7c5-c4cd62e6bb64 | -7.37209 | -72.78147 | 2025-09-15 06:01:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3303357-a3a5-37e0-8ea5-c1e8117918e4 | -11.7945 | -62.74173 | 2025-09-15 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3af496cc-9cf9-3256-ba06-d52edfd4ae78 | -8.73844 | -70.54108 | 2025-09-15 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92f9ba35-7526-3838-b882-0361797a5167 | -11.79664 | -62.74419 | 2025-09-15 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README66.md)
