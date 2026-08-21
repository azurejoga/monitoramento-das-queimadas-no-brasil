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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5508acd1-09b6-352b-b1b7-01ba9e2182a5 | -4.09838 | -42.49705 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 183dbbc7-8551-3a6a-b8c0-cde2da3ac4ab | -2.04588 | -48.03341 | 2026-08-21 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e149ac9e-37ef-3686-abfd-d97073d6ff14 | -4.09754 | -42.50269 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 0e1d86c6-9166-3cfb-8216-d8ba993fc889 | -2.4835 | -49.41761 | 2026-08-21 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eae5dc32-6a2c-37f8-a346-84f585915243 | -2.56157 | -49.1139 | 2026-08-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11805844-4237-3217-8b87-d219a7c7f699 | -2.76625 | -48.57221 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6a82dc5-cba8-3c78-911d-389bf76dd6b4 | -4.09172 | -42.5076 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1a374a02-c8d6-355b-98d9-5fefc7a646a3 | -3.54516 | -48.18149 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ff26beec-0f01-3525-850a-4f42321d0d61 | -2.87431 | -48.68957 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 481f679f-4dc2-30b6-835b-6c9d76b2d893 | -3.01601 | -51.06172 | 2026-08-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c35014a2-84a2-33e4-ae2d-96d854404e4c | -2.48404 | -49.41413 | 2026-08-21 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b846a757-17bb-35e7-bb51-a3decb7bbece | -2.80313 | -49.41714 | 2026-08-21 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b607f20-0a17-37a7-a7c2-e8240277531c | -2.11601 | -47.11601 | 2026-08-21 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b0799b5-1fe1-311c-a555-2f48238310eb | -3.963 | -43.11023 | 2026-08-21 04:44:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1141723a-4f1e-3614-90d2-a6b288e9f84e | -4.0967 | -42.50835 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cbe61ee8-fa40-3336-819d-81d42e092f8b | 1.29773 | -50.79072 | 2026-08-21 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39ff3abf-80f2-3706-b78e-a093e61f6175 | -3.03591 | -48.41338 | 2026-08-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efc07a19-4b7a-3423-80f4-6bbdc46fcff1 | -4.09813 | -42.50418 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 28f27dc5-ca79-3472-9219-6e1bb8c78431 | -3.26859 | -49.52818 | 2026-08-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2b13949a-9e25-3711-bcc7-c2c51d3981fe | -2.76569 | -48.57586 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4afe2e72-cc22-3ba7-a714-10652c371516 | -3.53359 | -48.18748 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1aa4abc0-5b8b-3cea-9f7d-fab429b32ed4 | -3.54458 | -48.1853 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 9d5e603e-8ecc-32b4-840d-078c647f365f | 1.29718 | -50.78716 | 2026-08-21 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 376b3599-00a1-3db0-b5aa-1e8dec0598d3 | -3.26526 | -49.52768 | 2026-08-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 38f81506-955e-310b-a74e-702a042c7d60 | -1.09843 | -48.05819 | 2026-08-21 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ca0817c-8889-3847-9ac7-d14181cabbc6 | -2.76909 | -48.57638 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e2403f5-8ad4-3d56-8ead-714bb92ff7af | -3.01655 | -51.05825 | 2026-08-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 187766ef-cdd7-33e0-9756-dad6346f7966 | -4.09873 | -42.49994 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 733fb003-c6a4-3027-9ecf-159c907113d9 | -3.96375 | -43.10511 | 2026-08-21 04:44:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c74049c9-7943-331e-a00f-c66b3f90c260 | -3.53823 | -48.18039 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 161f1184-1b0a-3a72-9c09-eb6a0e51f28d | 3.84839 | -51.81233 | 2026-08-21 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b492125d-1b8b-3160-9a37-489a0be565f9 | -2.04932 | -48.03394 | 2026-08-21 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e459e8e-fe79-3d7f-97fe-44c5109359a8 | -1.82549 | -47.89243 | 2026-08-21 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71138e05-f568-3adc-b9a6-2e4cc1d3a625 | -3.54169 | -48.18094 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 8716ad63-9e79-3a29-b064-46b9aa4c74fc | -3.2658 | -49.52418 | 2026-08-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dab6c983-6886-34da-8b93-f93e9cef58f3 | -3.26913 | -49.52469 | 2026-08-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11c1bab3-3690-3992-be9d-6f7c82a19f18 | -3.53071 | -48.18312 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96a55693-32f4-37de-bc4a-cc4856516d9c | -3.2085 | -50.91862 | 2026-08-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5638a99-0d60-3350-a569-c969c1a3254f | -1.4017 | -50.70601 | 2026-08-21 04:44:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80e17faa-c185-3e6f-812d-19f74e9d8aac | -3.53417 | -48.18367 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| dd1f3b4f-44ec-3eb6-88a2-2ad45932f917 | -3.54111 | -48.18475 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 6ca5e547-e7dc-345d-a372-158ff13b2e22 | -3.53764 | -48.18422 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 808c59a9-b7e1-3ca9-a6a5-9c03ba0f1b1e | -3.01323 | -51.05774 | 2026-08-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9e082a0-4c8a-3f40-b958-89cddfaf96c7 | -2.89931 | -48.7971 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f0fe7be-8283-3f7f-9151-9933cbd4fdef | -2.47406 | -49.41259 | 2026-08-21 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8220f87-a907-3d30-9ba2-8bd168531ce5 | -10.2456 | -54.37598 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1ef682c-74dc-3187-be9a-6f62dee405fc | -6.11513 | -59.92256 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f7295c1-f57e-39ec-b25a-c08e2422028a | -8.58042 | -54.78912 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fff11e4f-8825-3ca7-a23f-5093f767cdc9 | -8.71745 | -49.61572 | 2026-08-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cf5d0a3-32dc-3c12-bcd8-0866a44bc131 | -7.45375 | -47.16927 | 2026-08-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61e071be-701c-3e63-9ef6-1d146eb805b5 | -8.09385 | -51.66937 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be7b5ef4-2f0e-3ffd-8a66-9eb19f3c5c17 | -6.72333 | -59.09896 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43f7c881-dbeb-3fbc-8aa4-05e17679f4a3 | -8.60054 | -54.71144 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5e0b6ac-191d-3db2-ac68-dc8e9b22e335 | -6.65439 | -56.34118 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17965cba-a92d-375e-a89f-efa0da687e79 | -6.22102 | -55.48526 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 320d5a0f-bce9-35dd-86a9-67a658925105 | -4.51223 | -55.45128 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16e0796b-9f34-34ff-a2df-9da738d45378 | -6.87248 | -43.7403 | 2026-08-21 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5a69cb2e-4699-3e3a-81ac-9aead729072f | -11.55612 | -46.94183 | 2026-08-21 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2371b44-a943-3695-9ce1-ad28ea458f80 | -7.29045 | -52.53561 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d8bf1d1-211e-3b08-b2de-2eb112fc25d1 | -9.41483 | -60.41558 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a0974bf7-ae80-33c7-be1c-1475836b1412 | -6.87816 | -59.43311 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79cc2b83-9b74-39f2-a7c9-62c379d761c9 | -7.45752 | -46.15569 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 702f891c-c6db-3350-996e-f936c4102877 | -10.52562 | -50.77735 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1281ed4a-2308-3a89-9a2f-54758060cf23 | -6.439 | -52.76192 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b23c97bf-070f-37dd-866c-772ff0b3c873 | -6.36494 | -58.33817 | 2026-08-21 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 787aa1da-29d0-3f18-aa93-7c5ce3f68201 | -10.16784 | -54.91103 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 856a9917-fcf5-3c02-91f6-19c175863bb6 | -9.4064 | -60.41573 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 4e144afb-b535-3e33-a2f3-e0aa113866cf | -9.20206 | -60.77475 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8d3ca4f-fdf4-3f29-b6aa-a83869fa3d89 | -3.84395 | -59.37704 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88d05c99-4b08-375e-8e83-93748b420213 | -6.42712 | -54.9297 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60809271-a700-3b0a-a88e-e9d677aa74c7 | -10.74975 | -50.33553 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca05be21-3d0e-3e85-9892-38593a60d29f | -6.58356 | -58.96167 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a979231a-8872-3b9d-b0aa-71117fc5218d | -5.49643 | -60.12992 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bee4f739-4f64-3470-9f0b-72f224346ed5 | -7.78616 | -46.04226 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe156280-c646-3395-a152-591289b1b42d | -6.54694 | -56.26033 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c7f139e-bcb3-3022-862d-30ce582126d2 | -6.25524 | -48.65464 | 2026-08-21 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ade6fc6-c573-39e7-a395-9deaa193b241 | -5.87051 | -57.6603 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07cde900-fdf9-38c9-a7b9-cf16abb33e1f | -3.84447 | -59.37387 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7c4e0fd-2f8d-3771-a1f6-fd49e57a0c3d | -7.35985 | -45.82496 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 305abced-0854-394e-a841-dca2106e3767 | -6.90938 | -59.34687 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2d2831b-6f6b-3fc5-bced-ec321966c0c4 | -7.42957 | -59.78983 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1acce21e-cee2-3d94-a366-66e7984a8406 | -10.62115 | -51.6176 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d42dbcdb-7d2c-3052-b606-298b827d5eae | -6.37797 | -54.94933 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c75f7519-f63e-3bf9-91d3-7ab17de6b309 | -8.06359 | -50.10934 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdffad80-0950-32b1-bc9e-93f07d7a52cc | -8.59156 | -54.74379 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 920c1310-bd98-3019-9400-7eee8551e354 | -8.1801 | -44.43485 | 2026-08-21 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38f23c38-3d09-3c86-bc99-b3e0b912043c | -8.52129 | -55.33254 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 18def783-f92c-3a39-ac2e-4690e6f095a5 | -5.59939 | -44.00583 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cf4e31f5-d1a8-3f7c-bf82-25c90422e65a | -7.05354 | -59.84545 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e0ed128-bd76-366c-8732-751eb0eb944c | -9.05707 | -60.43585 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1768d56-e4cf-3180-8651-73185c8404b0 | -6.47934 | -55.90229 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06c5f72b-7d85-3795-84b3-892b1617efb9 | -9.06883 | -50.88365 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55829f2c-916b-3902-b507-6598f53e6c49 | -9.45088 | -51.60056 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3012ebd8-859c-3b6b-9ad5-a836ef64e1b8 | -6.86009 | -59.44896 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b9f715f-d1bf-3c84-8d86-21cc3fb5f497 | -8.56926 | -54.6555 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d5afad4-c746-3497-a1de-8822363c6311 | -8.64827 | -54.68003 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfc5e355-058a-39b5-a3a8-7faa259902a1 | -9.41091 | -60.43681 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8be345e8-ddfb-3c66-b25a-b5ce42bb9d11 | -6.32323 | -43.75322 | 2026-08-21 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26e85469-4062-3808-bb55-2774bb603eef | -4.6547 | -50.87021 | 2026-08-21 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4114c67a-16fc-3fbf-867c-54f8ba541aab | -8.02434 | -54.01857 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README34.md)
