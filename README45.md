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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f88a4ff6-d6ca-392f-a124-37942ac6a074 | -7.50226 | -60.07671 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37932eb0-1bb5-3338-a13f-d78d7658a33b | -9.06182 | -60.44013 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d450a0fa-54e4-32d2-929a-cf56cb77193d | -6.7766 | -59.43833 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1642e45-e717-3e40-a096-3222ca0a3898 | -11.58577 | -46.93333 | 2026-08-23 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4c30d0e-8c52-351e-8ee2-53baa5ddccec | -12.24935 | -43.1888 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c5c8d06e-b213-3e5c-8118-75003904b03c | -6.77542 | -59.44522 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34b406c3-a18f-32ca-be35-0d9c76a51d0b | -9.11146 | -61.59482 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d643cf0-7cf5-3849-8c8e-4e834d6e4ce2 | -7.10363 | -59.77581 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e422f41-ee53-3cb6-87de-dd24c9c94350 | -9.13967 | -65.95449 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad0e7d8a-21dd-319a-8577-b862deceb4e6 | -6.68852 | -58.74384 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4bd1b1be-9bf0-3c2f-bbee-2af767e45a52 | -6.90213 | -59.00404 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb9b1504-c8d9-38e0-9757-109ad4facc5b | -6.37427 | -54.97053 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98c5dcd8-b335-33b9-b8e5-a187f7cb5fe4 | -6.85118 | -59.46938 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3094573-a4b4-319e-871d-c0a9c840d13b | -9.43061 | -51.61512 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b9e5c1f-5c01-340f-a948-1ada87b2a2f8 | -8.22062 | -55.02428 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c62480e-b25e-3151-92dc-4506ac3f7f48 | -11.61332 | -50.55289 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 329c6f93-f0fe-3dbc-a158-296501c97e7e | -6.76742 | -59.44384 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25fcbdd7-5eba-3b89-b66f-893a0aa31bf8 | -7.61527 | -60.97692 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf52aeab-2a98-3a33-ab1d-87bc8864c152 | -7.60654 | -60.97535 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c27eb64-6e7b-3fe6-89c0-d14ad4b4e0a9 | -10.84304 | -50.98284 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d57d1320-f3fe-325a-aaa4-b74d903c647d | -5.56964 | -60.18001 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| decfb807-4617-3a95-b251-614dcfcbf61a | -12.56278 | -47.93735 | 2026-08-23 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40ebc960-4b22-3d44-8688-e9456e739046 | -6.70322 | -58.72663 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 689a7960-b217-327d-ad7c-875f4e403a96 | -12.26715 | -45.08254 | 2026-08-23 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1681b165-6d9b-3f1a-bfb1-ae4319b089a9 | -10.79337 | -50.97052 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9abeddde-ead8-3444-aec3-7e3b75f4462a | -7.43713 | -59.77721 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 035f7f44-a796-3514-a828-76ceb7818ade | -6.11963 | -59.93324 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d38f453-9821-328e-8b80-078f6f62aee2 | -6.77372 | -59.14888 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24f6f91f-5cce-3e3b-89b9-00ad02e8ebc0 | -8.69899 | -62.87574 | 2026-08-23 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13644718-7f19-3aac-832e-dc1d97f6d55d | -6.43781 | -56.17771 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cceaa4df-192c-3bff-9edb-6b4e9a85a405 | -8.9241 | -48.53673 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6b31d63-7934-3ad1-af99-37931ad44240 | -6.70244 | -58.73135 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3977efa3-9a94-34bb-ad7d-3ff022cd3f90 | -4.52984 | -55.52141 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd1ae6c9-811d-384d-a3a7-ca02abacda9f | -9.16451 | -59.45506 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c9976cc-59db-3359-b31d-7cbebf993190 | -9.02135 | -50.73698 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd1cf252-5a3d-3324-857c-193b0b745342 | -9.13375 | -65.95336 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8721bd74-aa2f-333d-9149-4d2298e788c2 | -9.01818 | -50.73184 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4e22465-7807-352b-b7e8-7dae21419d01 | -8.53144 | -55.33458 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba69cd64-b0d9-3f05-af40-a4f8832e2068 | -6.80471 | -59.418 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a452807-f729-3d50-9235-a46c1d1a5bef | -5.67375 | -47.49311 | 2026-08-23 05:04:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70feae73-6c0e-3ba3-b07a-cc3f1e83c5aa | -9.03933 | -60.44756 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b6367bd-5c1e-32a8-91d0-dc897d5bf452 | -7.78019 | -61.06837 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d85c8017-c0fd-39a8-b7bc-812f32ddde11 | -4.53717 | -55.51891 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65598b82-9aaa-3147-9106-ba9495bbaf47 | -9.16833 | -57.01147 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3273249-32f3-39ae-b7a2-9728f428853f | -6.9452 | -59.08501 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 926b6edd-72f1-34f6-b081-b25b14eb9410 | -7.3935 | -60.01324 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fff8cc2b-2bd4-3561-b114-0f376ff40d7f | -8.50729 | -54.90998 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf5eac34-d126-3200-bd5e-f3df101f230f | -9.14911 | -65.95567 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fbc3de3-8293-3676-9bf1-7924abdc6452 | -6.76503 | -59.77845 | 2026-08-23 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc57826c-a086-314d-b48f-d1d23698d050 | -9.20512 | -59.56833 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7003cd60-a977-3833-a4cd-17743d63d7fe | -8.89771 | -60.54105 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a1e0085-526d-3185-820b-7943664a4d60 | -6.85494 | -58.9757 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70ee8a65-e832-3cb6-99fd-9358267e40d3 | -9.21173 | -59.78891 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58443bc8-894e-3947-af61-5bc3ce616380 | -9.3989 | -60.56062 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1160c425-613f-363a-87c0-d78173a95fd7 | -8.81013 | -46.6208 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a4dee84-879f-327a-a590-2445ab997eeb | -7.68713 | -63.33959 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcfd707d-6a45-36b2-abb3-65ee809578ff | -7.85092 | -56.57039 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e331ea0-9875-3bf5-9ed7-578fd18d6194 | -5.27032 | -48.21725 | 2026-08-23 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e01b6bc-ca69-3eb7-8c7c-c0b63cda8d18 | -8.22448 | -55.02134 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e206257-4d46-358e-8315-b0b99f0b1b7c | -6.93908 | -59.07377 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79a528bc-7fd2-3b5a-b6b2-a3a91e09ac5d | -9.03874 | -50.83216 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f1e698c-ab05-3cf7-8d6a-117dde64d0ec | -6.93773 | -59.32165 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbaea207-051f-3d7f-a2df-7b55e41c2a7b | -11.439 | -44.53549 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| faa8c770-4dcd-3052-8acc-46d008d2ada7 | -6.80125 | -62.91462 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f13e111-eafa-303f-a775-78e57cd7c151 | -6.81953 | -59.42767 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8d0e72-9dba-3905-af5b-d97d28cf29f8 | -6.80069 | -59.66516 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ecb93b5-4ee2-38d9-9f95-1a65cca64304 | -6.66389 | -58.74946 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7e468031-a1e3-36ce-8376-df883e6e4fbb | -6.83557 | -59.95468 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87e8eed-dddc-37ae-9a64-7fd0a154ad95 | -6.81351 | -59.66391 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3df8043c-566e-3e81-aa71-064ff054e71c | -6.18902 | -55.42915 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 285657fe-9536-3e8e-8d60-f1ddd29d8326 | -8.54033 | -54.8298 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a269b79d-dde2-3b50-96a1-e944319be085 | -6.76463 | -58.68821 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7602ef4-855d-3511-9b0d-5ea75fe42dae | -9.0134 | -50.76487 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a983d3ff-5218-300a-8fd6-2a9840f3cc86 | -7.26132 | -49.90315 | 2026-08-23 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3bc030a8-de38-3dd0-886e-3343a5c439b5 | -8.59316 | -54.71002 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 494069ee-cd18-338a-bc64-2d0150125e0b | -9.42976 | -60.48135 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dbc7747-30a5-3fe3-9f7f-f84b25788d10 | -6.55436 | -58.59242 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9bd43b6b-963d-3611-ad4b-8597394d53cf | -6.19763 | -53.52865 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28b16dac-62c1-3927-9e3b-86635813db37 | -7.5702 | -61.21024 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6010609-ea9c-384c-8ab4-15cd17d420dc | -9.43042 | -60.47762 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4308128b-fe5d-3a06-b5df-d4842576a9d6 | -6.60475 | -58.38694 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 226a440e-76e7-3d0d-a145-272602777401 | -7.0698 | -59.97834 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd8c0b19-e502-30b9-ac6d-93fc5ff44c47 | -8.53039 | -54.80684 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f412301-3814-3cfa-a98c-c34aee0cad58 | -6.17029 | -55.56805 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05b701f6-c592-3d9f-90f2-4392e645a489 | -6.37096 | -54.94859 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa889f4f-dad2-31f8-89a8-e2130b6ace42 | -6.82189 | -59.96006 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8580c297-ef6a-3f8b-9356-858a7148b483 | -6.57697 | -56.24939 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2828939-92ff-3c5f-b2a9-ac2ee2cf8970 | -6.76086 | -58.66327 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32f4a13a-6ced-35ab-9124-6531696c1abb | -6.96723 | -59.07341 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| af8f647c-07c7-3424-a08e-b0dc2ab51aac | -6.67861 | -58.73238 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4bbf0979-5a59-3e1c-b020-9117d4381502 | -6.96333 | -59.07275 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c4ad869e-0da7-3314-84db-250d7ab20b4e | -6.37925 | -54.96062 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 052de48e-6674-388f-aa78-423d1e2cf26f | -6.79522 | -59.59793 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad14b941-6543-38ae-bf9b-db3ddbe41080 | -8.10351 | -50.05751 | 2026-08-23 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f06b92b-dcc3-357f-91e5-619369076e3d | -6.94169 | -59.32234 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22d4e77a-6ce8-3519-94d1-f4f194329798 | -6.12364 | -57.83907 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1cebb857-3ed7-3ea1-b8a5-72d600ef5623 | -6.68404 | -58.72348 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93e52111-95bf-3371-9d39-1fdf33f7298e | -6.78099 | -59.75838 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7dc54af-0b56-3815-a3b1-0fd343c54c25 | -5.95276 | -52.1249 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 31011b1c-a45e-3329-a7c2-0f6cbdc5c0c0 | -7.56808 | -61.19614 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README46.md)
