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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5beb4153-26d9-32d1-8fab-31f9289084fa | -6.88978 | -43.878 | 2025-09-19 12:17:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 83adaaaf-1a72-3a9f-a8d2-e9219b054716 | -6.06973 | -44.68683 | 2025-09-19 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cddc8504-0707-3dbf-983e-247180734df2 | -6.26221 | -43.90155 | 2025-09-19 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fb8fce71-cd78-3723-97e1-94a0a25dfb42 | -9.67586 | -46.74337 | 2025-09-19 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 78673554-a419-3073-ac8c-bd5ed9070121 | -10.05691 | -47.23834 | 2025-09-19 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| f9e3b0a9-496b-3241-8689-2b17c5b0e4d1 | -6.19398 | -45.11131 | 2025-09-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2b7b5911-707a-32e8-9386-94ae3fdcbb23 | -6.26076 | -43.91203 | 2025-09-19 12:17:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 25021e5e-d233-31d7-820c-ab74c441d0fd | -7.29096 | -43.92436 | 2025-09-19 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| dc08cc69-aa03-3e8e-9424-4db2b25cd533 | -8.37424 | -46.95927 | 2025-09-19 12:17:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| f3510017-2174-38f8-b61a-9167f6858888 | -7.7167 | -44.41646 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ecd275ee-680a-343b-bc82-210c96c24f70 | -7.71001 | -44.39447 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7286c402-116d-38f4-8cde-fa9b0cdd8271 | -8.00409 | -45.73594 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 5a831e06-6b14-3740-8661-ed667a87a67e | -8.38323 | -44.67455 | 2025-09-19 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 33e4adf3-8ba1-3d0e-afb9-aeaf3455971f | -7.35754 | -44.17786 | 2025-09-19 12:17:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b59643aa-3f12-3884-a2e8-86fa4feff9d0 | -9.03139 | -44.96679 | 2025-09-19 12:17:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 636bc9d9-62e2-3e58-b4ef-45bf2ef872f2 | -6.05979 | -42.70139 | 2025-09-19 12:17:00 | TERRA_M-T | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| b1cd4b33-7a84-3c42-8986-d7c2b3d901d8 | -6.29792 | -45.54897 | 2025-09-19 12:17:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b3b2d9da-274b-3e2b-a43a-e44271f19610 | -8.97027 | -45.74355 | 2025-09-19 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cec59f73-dbde-3055-a3cc-d2c1913fc1e3 | -5.76113 | -43.3891 | 2025-09-19 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7d89cd71-bc09-32e0-9b7a-b0c951b9d86e | -8.74673 | -46.14945 | 2025-09-19 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5bb76957-19c9-376c-9d6b-6a7fefca7a65 | -8.99751 | -45.02681 | 2025-09-19 12:17:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0a200517-d1dc-33b8-ba3a-5926188d3b12 | -7.19408 | -44.41235 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b80e8668-32c4-3e4c-afd8-63bb96294c91 | -7.45636 | -46.14806 | 2025-09-19 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 734c78e4-b569-3fd4-9b07-55448978a571 | -7.22814 | -44.37507 | 2025-09-19 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a6caad17-4729-3744-9d7e-49b7f29a5d72 | -10.05819 | -47.22942 | 2025-09-19 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 2a7441f0-8bbb-3bd5-acff-d40f3c36e9ec | -5.74187 | -42.571 | 2025-09-19 12:17:00 | TERRA_M-T | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 0aa8ca87-a3cf-3285-8643-b3f9d35fbf8b | -10.24619 | -48.04038 | 2025-09-19 12:17:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fb237861-9d54-3efe-8eb5-bee8d103f334 | -9.00668 | -45.87777 | 2025-09-19 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5113fc0f-024c-3a55-bf9b-8a2fc4e7399c | -7.86342 | -47.10276 | 2025-09-19 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9f714291-44cf-37a7-b5d1-cc653848717b | -10.27985 | -46.45737 | 2025-09-19 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 80d3352d-22b1-3e03-a570-6f99397efce9 | -9.78372 | -46.96252 | 2025-09-19 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bd3d1672-82c3-351e-b180-193002db9b89 | -17.13451 | -47.74842 | 2025-09-19 12:19:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 3f3f3883-c693-372e-af84-650e37d5d4c5 | -15.78426 | -52.16924 | 2025-09-19 12:19:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 7189f29e-37f8-375f-a1b4-ed6fce6fa237 | -17.44937 | -44.78941 | 2025-09-19 12:19:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 47c5c3ca-ed1d-3761-8783-8a486e479d7e | -20.78746 | -46.10682 | 2025-09-19 12:19:00 | TERRA_M-T | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b3a30637-ef41-3631-9a0d-7eb394698cff | -18.75135 | -48.23406 | 2025-09-19 12:19:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 361ff26e-e3df-3c03-be08-e4536563cc59 | -15.25585 | -50.21367 | 2025-09-19 12:19:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 23c4a383-042d-3e68-ad1b-a602b1773996 | -18.75767 | -48.25436 | 2025-09-19 12:19:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 44c45c89-339f-320d-a553-ceb3a531a636 | -12.48237 | -44.7421 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| dfb5a6f8-6cce-3c2c-b03a-9790581290dd | -12.07871 | -46.56529 | 2025-09-19 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ed5ef40a-88a8-3309-812a-d3237786b5b8 | -19.18196 | -46.31735 | 2025-09-19 12:19:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5b573917-3898-33b6-86bf-bacb80e5888d | -15.26942 | -51.48029 | 2025-09-19 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 81651d1e-df00-38f0-b660-160e77cb0af7 | -18.58682 | -45.04484 | 2025-09-19 12:19:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3ecd2c37-ec1d-3130-9726-eae7e6486d7b | -18.91431 | -47.98728 | 2025-09-19 12:19:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| b4f5058b-96f1-36b1-a490-c91f1cc2900c | -15.27124 | -51.46889 | 2025-09-19 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| af227852-dc07-3b2b-9a10-b5a972473d21 | -18.75899 | -48.24488 | 2025-09-19 12:19:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 99f470f7-d02e-33d8-a548-b3f87fe28699 | -19.18343 | -46.30589 | 2025-09-19 12:19:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e3956ecc-0d1b-3947-a20d-f7deaa9b482c | -18.75003 | -48.24356 | 2025-09-19 12:19:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 40.9 |
| cf8d4658-0777-347e-ace7-87902449efb6 | -12.41644 | -45.01656 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 5ff7280c-3ba2-3841-9d21-4c6c0cb77658 | -12.69812 | -44.89293 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6c685ac7-0d0c-3f37-8f50-6531beb86512 | -21.50339 | -45.90125 | 2025-09-19 12:19:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 301ddd92-21d7-3f17-851f-edf1cbf4b2e5 | -15.24813 | -50.20234 | 2025-09-19 12:19:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4a8d5ccf-399b-3654-9376-4a0b86d29321 | -12.42471 | -45.02875 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 069fdb04-e361-3608-a2a0-06767f094e31 | -18.91299 | -47.99693 | 2025-09-19 12:19:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 0cc0943f-0451-36db-8cac-fa5b3e46753b | -20.58621 | -45.74422 | 2025-09-19 12:19:00 | TERRA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 48fcb7cd-904a-39ca-8282-90afaf261079 | -20.84755 | -44.95424 | 2025-09-19 12:19:00 | TERRA_M-T | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 8425c511-18b1-3c9d-bd59-375cb051487e | -12.69686 | -44.88681 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 8c8bff78-3b72-379b-b6dc-cbc537530b4a | -21.12741 | -45.7192 | 2025-09-19 12:19:00 | TERRA_M-T | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 16f045bc-b5a0-3b3b-9e07-96219ab2a112 | -21.72771 | -45.64245 | 2025-09-19 12:19:00 | TERRA_M-T | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 2339de1f-59c3-3bf8-848f-dd46e7f45034 | -20.59784 | -56.72603 | 2025-09-19 12:19:00 | TERRA_M-T | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d5e7e290-03c3-3a89-ae00-e567b2c36b03 | -18.47585 | -44.24929 | 2025-09-19 12:19:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f13651a9-e33f-3ee3-bbbe-c277b3c1339d | -18.74239 | -48.23277 | 2025-09-19 12:19:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 263458db-9fc7-376a-b75a-ad5d17141eaa | -19.13312 | -46.6204 | 2025-09-19 12:19:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a0d48be8-a6ad-3808-93de-d252b0f180e8 | -19.15737 | -44.56194 | 2025-09-19 12:19:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c6da4df4-a37b-363a-8445-41a680830cd4 | -18.74108 | -48.24219 | 2025-09-19 12:19:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 67af5eae-d0e3-38a2-9e8a-68da40326f3a | -13.21246 | -42.96519 | 2025-09-19 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| c008e8e0-e32b-3103-81c6-efcec2267e5b | -19.71717 | -46.59036 | 2025-09-19 12:19:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 31e6e1d4-6005-3eab-a167-9e097ce1f1bf | -15.25734 | -50.20372 | 2025-09-19 12:19:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7b35e775-6d8f-3702-ae7f-f61b630c2c10 | -19.71862 | -46.57913 | 2025-09-19 12:19:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| eeb7ede4-e779-3d38-82be-c8104d68096e | -12.27557 | -45.28015 | 2025-09-19 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 14706abe-dea9-37b3-a1eb-277f669a05a7 | -12.41501 | -45.02747 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 54c6db38-4d34-32c6-8ac5-8d644975b8ae | -12.69957 | -44.8817 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 316fbbac-7f73-3437-90ae-c1e77c9af061 | -12.42614 | -45.01789 | 2025-09-19 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 2a7ed627-65e7-3a02-aff6-2b7c1bbde501 | -19.15858 | -44.56797 | 2025-09-19 12:19:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a4fe6e2e-dff8-39bd-9b9a-96c7efc2c5ae | -7.7148 | -44.392 | 2025-09-19 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 7eaf08cc-2f50-3e22-900d-ac438e7c2b17 | -8.6027 | -45.7162 | 2025-09-19 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7715782c-bb33-3347-b2dc-f605c014ba72 | -7.1878 | -44.4193 | 2025-09-19 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 7094bd7c-5700-3f14-a7f7-ef378c9cbc93 | -9.1937 | -45.2886 | 2025-09-19 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6dcc5033-6f69-3c14-8a9e-ac74f1388809 | -8.9908 | -46.3284 | 2025-09-19 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 76164bd8-7b7e-3986-a924-131612c9e460 | -8.6216 | -45.7142 | 2025-09-19 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b91336a7-998f-3bed-a808-c39a73de3e8d | -9.0097 | -46.3264 | 2025-09-19 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 815579a2-18ee-3255-b87a-546a35ca1c2c | -8.9344 | -46.3119 | 2025-09-19 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 752739c0-2e0d-333e-b0d0-1a4572ec3b52 | -22.62842 | -48.26734 | 2025-09-19 12:21:00 | TERRA_M-T | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d756231d-ab69-3125-8ddd-d64198d9c9ba | -23.10646 | -52.10064 | 2025-09-19 12:21:00 | TERRA_M-T | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| af0641fa-1ec6-3750-90ac-1d94017f78d1 | -23.54901 | -51.50922 | 2025-09-19 12:21:00 | TERRA_M-T | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 6b8706fa-a334-3e11-ab61-439e89eabca0 | -26.60887 | -51.77596 | 2025-09-19 12:21:00 | TERRA_M-T | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| e01d1257-bfaf-30bf-aecb-1668e6037fc4 | -23.63407 | -52.84789 | 2025-09-19 12:21:00 | TERRA_M-T | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| e608c940-d029-3ae2-b3c9-aa3461791b12 | -28.10596 | -50.11221 | 2025-09-19 12:21:00 | TERRA_M-T | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8d1c6b9e-e5c5-377f-abcd-1f40e72e80ba | -28.10458 | -50.12251 | 2025-09-19 12:21:00 | TERRA_M-T | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1443e2ef-036a-39dd-a444-a3cda2810cac | -26.84823 | -50.69784 | 2025-09-19 12:21:00 | TERRA_M-T | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d0e2a79f-415f-3606-bfd1-b5458a2fe33e | -26.88933 | -48.72651 | 2025-09-19 12:21:00 | TERRA_M-T | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f6ed1112-2a65-30b7-8cec-f773c104e8b1 | -25.6894 | -49.89835 | 2025-09-19 12:21:00 | TERRA_M-T | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| dbb96e90-f606-3b36-8710-4602a3e9a5f1 | -23.63227 | -52.859 | 2025-09-19 12:21:00 | TERRA_M-T | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| c67c5df2-2247-3712-bbc8-6d830503cf40 | -23.1081 | -52.09021 | 2025-09-19 12:21:00 | TERRA_M-T | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| be92eeb3-37ef-319c-bf1f-9b63050dcb94 | -24.17621 | -48.78268 | 2025-09-19 12:21:00 | TERRA_M-T | RIBEIRÃO BRANCO | SÃO PAULO | Brasil | 3543006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 965e9ea5-f373-39a6-8a6b-08e82c1a8530 | -26.96751 | -52.87085 | 2025-09-19 12:21:00 | TERRA_M-T | NOVA ITABERABA | SANTA CATARINA | Brasil | 4211454 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 5a4d2196-5dce-3ebb-8eb9-69be98e27837 | -32.37307 | -53.57668 | 2025-09-19 12:23:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 26.2 |
| 87afd352-a894-3265-87ce-1bf35aecce67 | -9.1937 | -45.2886 | 2025-09-19 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 3cec249b-0b2e-3f19-9051-c16465e38932 | -6.9212 | -44.764 | 2025-09-19 12:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1be974a7-ea1a-33f8-b6e9-7e4ca7b6a891 | -7.7148 | -44.392 | 2025-09-19 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |


[Clique aqui para ver as próximas entradas](README40.md)
