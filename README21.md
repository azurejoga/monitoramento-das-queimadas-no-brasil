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
| 93b8cd58-23b1-33f3-86a2-07521a4394f7 | -9.42284 | -56.50035 | 2025-08-01 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eade219e-1dd6-3e0c-9f41-faccbe63fba3 | -14.33424 | -48.65608 | 2025-08-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff42e565-788c-3a92-9e59-1496a875eb9f | -10.40091 | -49.53173 | 2025-08-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77c8ba2a-4adf-3d54-b9f8-bb62ad61e5fe | -11.77215 | -45.00213 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1aed4d8f-de40-3f67-ae23-6253cb0e23b5 | -7.32361 | -59.62111 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3010a0a9-2187-3062-9fff-f18c74cbea7b | -11.52288 | -58.00177 | 2025-08-01 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14e91a19-a620-3975-96ba-bf1f4df37620 | -10.3461 | -56.48691 | 2025-08-01 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a476c2fb-a612-35e2-84fd-618a38f1db75 | -9.74186 | -48.66363 | 2025-08-01 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e749d220-3b7d-3b4b-917b-d90d4a538437 | -12.43761 | -60.56635 | 2025-08-01 05:06:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7859b026-fed5-3e2c-8205-d564419c38a3 | -7.32432 | -59.6168 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 189c8f3e-9a13-3953-9710-f5e198e991c1 | -12.26655 | -45.0696 | 2025-08-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fc1131f-2c4d-3dee-9dc3-acbe68d12f28 | -9.62405 | -63.42424 | 2025-08-01 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| add1e896-386b-3d05-987b-e0fe28ce0122 | -8.30818 | -55.10779 | 2025-08-01 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fb5bd02-c300-31fb-8eaf-c9fc6df108e7 | -10.4323 | -47.26436 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aee347d-be3b-3c4c-b25a-87070c3def85 | -7.32797 | -59.61741 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b4d6b94-956a-353d-9bee-d81d742e155d | -10.60056 | -45.26937 | 2025-08-01 05:06:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 001ae997-7f97-3da0-8bfb-56e62ab41ad7 | -9.0311 | -59.76051 | 2025-08-01 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfde444d-16bc-33b3-935a-b3ce3c7f152c | -13.22854 | -47.23651 | 2025-08-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c0f5209-48dc-3c53-bd7a-33c73c151406 | -7.33022 | -59.62662 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f08872de-32f8-3b72-8f62-f827f9aad424 | -7.33092 | -59.62232 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25895286-bd0e-392f-beed-8320d1afb105 | -10.44741 | -47.27706 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8665440-d71a-30c1-8797-39a858b0fad5 | -9.01561 | -47.97416 | 2025-08-01 05:06:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c44052c-b3e0-3fcf-9fc3-ff80034f63e1 | -12.66164 | -48.09329 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a7cc3e7-716a-3518-91f5-351b35fb0d50 | -14.96113 | -49.28149 | 2025-08-01 05:06:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fe252ed-cf18-3320-a849-704b015b86d0 | -10.43868 | -47.25798 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a2948f3-cbca-3f4c-a507-d6716400aa6d | -13.21679 | -47.23807 | 2025-08-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64b1336f-8eb6-3dae-8d7d-4fd9a20b6823 | -9.74679 | -48.66442 | 2025-08-01 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f18627d-2120-36c6-b7e9-cd7256352274 | -13.97949 | -53.9368 | 2025-08-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc29b8db-7800-36b5-9ada-e440fe9d6531 | -9.85813 | -44.70747 | 2025-08-01 05:06:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1850817b-06f7-31e8-abfe-c5c765e7e4c5 | -9.02034 | -47.97791 | 2025-08-01 05:06:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6310e32c-4bb6-3987-a958-a34003b82aca | -12.65163 | -48.08617 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85bd9ace-3232-32ff-ab1b-ca06d15c19e4 | -12.70866 | -47.79155 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3d912d1-d67f-36b2-a805-de7d7d51c221 | -11.0269 | -48.55825 | 2025-08-01 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f32d849-7cca-32d9-83d7-a406a6443697 | -12.0976 | -44.98528 | 2025-08-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e36edda1-8d13-3e48-9f37-1267204a3e4e | -9.45879 | -57.84477 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de65c87b-2693-3ab5-9f45-9ef816a4000b | -10.11054 | -58.23141 | 2025-08-01 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a5285353-47a9-3fdc-b03c-718f09e32a9e | -11.33075 | -58.58729 | 2025-08-01 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eae6505d-9012-34c4-a692-a523e8c5e2ef | -9.45544 | -57.84424 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c3fbeb9f-9c3d-3a3f-9c22-64851323d94f | -12.64632 | -48.08512 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db2a56b2-6915-37f8-a5b3-0e5a07d3d597 | -10.06099 | -48.33244 | 2025-08-01 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51dd175a-a8da-301f-812c-015c4e56b603 | -10.11391 | -58.23195 | 2025-08-01 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d0c86b7-cfe4-39ff-b1ee-770dd62b1e91 | -11.81312 | -48.78865 | 2025-08-01 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80086386-646d-399e-a2bc-dcd4e41d9a67 | -10.08135 | -46.75409 | 2025-08-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0817acb9-4764-3093-a47d-27eb803c8c5d | -11.76174 | -44.97881 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc8bf25c-8b05-3314-9776-8666fa3fa6c8 | -12.10411 | -44.98563 | 2025-08-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56a7ea8d-e292-3d44-b771-7edb878889fb | -10.11449 | -58.22832 | 2025-08-01 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7889731e-f42a-37ec-85ec-8f053ec1d8f4 | -11.90571 | -55.88677 | 2025-08-01 05:06:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| df75adba-44a5-3e76-ad5a-79e78a46be22 | -9.45601 | -57.84065 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e3818292-d739-3ed9-b52f-857c41a9fb24 | -12.64488 | -48.09724 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba517efc-10a9-3096-bb69-1962395daf45 | -13.22243 | -47.2393 | 2025-08-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b67fb14c-d88b-3761-96e6-9848ae4360e5 | -12.4614 | -57.87588 | 2025-08-01 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db87e294-9954-3e54-83f0-0465185be7bd | -11.77806 | -45.00759 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ee5105d-ba31-36eb-9476-45a3b7144c3d | -10.34556 | -56.49041 | 2025-08-01 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b8f8a6e-d329-367b-a8f8-6411f865e526 | -11.188 | -55.01601 | 2025-08-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 607b35fd-ef60-3e2a-bfcc-29a2cff17c1c | -7.3229 | -59.62543 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a01364d-669e-33dc-9bc4-849c5380f0ad | -10.43365 | -47.25358 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39adce94-9448-315a-afc8-18b156c4b075 | -10.58094 | -59.09746 | 2025-08-01 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5c06079e-a30d-3254-b03e-0dc7dc12a19a | -10.08186 | -46.75008 | 2025-08-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d6da9ea5-14d6-38ae-9179-65901d97ab85 | -12.43927 | -60.5652 | 2025-08-01 05:06:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b0af271-becf-3c29-b37d-a7304730443f | -9.45936 | -57.84118 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 831454c4-bc16-3785-8691-35974929ba7d | -10.44786 | -47.27351 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 654a82e6-a467-367c-a518-5d8af6afb399 | -9.63307 | -61.45622 | 2025-08-01 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 388db7d6-76ff-391c-8660-cd03b6e46b85 | -10.32818 | -58.72719 | 2025-08-01 05:06:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff4895d2-55be-3d01-b053-2f5552c9f9b4 | -10.08752 | -46.7507 | 2025-08-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1711000e-e4c6-3ea4-b949-9379c8d60d6b | -7.32656 | -59.62603 | 2025-08-01 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0160d3e7-8089-3acf-aeb2-2694ceb6f693 | -14.32901 | -48.65502 | 2025-08-01 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24fc98d4-77a2-3a94-ba50-0277c2508a4f | -9.31755 | -62.05572 | 2025-08-01 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f226b766-8bf6-320a-a35d-be35b4f8954e | -11.16741 | -45.75692 | 2025-08-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61c28dd5-17a5-33f2-8457-8a6c636503ce | -11.76636 | -44.99565 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de4294c2-cd19-3ef0-a9d8-8bf163b05667 | -11.16797 | -45.75223 | 2025-08-01 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76566945-1da2-36fb-9d4e-0f5448f73f19 | -9.28627 | -57.79814 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad13be85-1b46-34ee-a344-94d8546496ee | -9.01521 | -47.97726 | 2025-08-01 05:06:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5ab3ac3-0c3d-323e-8b68-a7c1f8a84a75 | -10.34972 | -57.50512 | 2025-08-01 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db311a3a-4e5b-3529-95a4-9760606150ba | -12.26715 | -45.06415 | 2025-08-01 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fd34435-2ae0-3088-80bd-3e86e569c4e3 | -10.43778 | -47.26513 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a99df3f-5fe0-3ab9-bfc0-57ca14977592 | -13.08909 | -52.14414 | 2025-08-01 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ff351a5-99cf-34f0-8e34-2acf46771db2 | -9.60716 | -57.92004 | 2025-08-01 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36b9640a-ecbf-3be6-b0af-a07b793ea914 | -11.77753 | -45.01218 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed6be232-3d17-3d18-a805-6f46a8d19bd1 | -12.65697 | -48.087 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b99c791a-0805-303a-a178-ba2ff38820c9 | -10.60187 | -45.27531 | 2025-08-01 05:06:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6f7542b-3c66-31ac-b36a-7c78d361d340 | -11.76118 | -44.9837 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22b1054e-b2ab-325e-8249-00cec3ce9788 | -9.45658 | -57.83707 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e89ebf05-2947-38bf-929f-9ebe4f3e642e | -12.65559 | -48.09849 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 14b1b657-8509-3e82-83d5-10b3778e1c23 | -9.47781 | -57.83317 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 828636ba-cb20-390b-a922-716880547cb3 | -11.7711 | -45.01133 | 2025-08-01 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec1e7cb1-7d63-32b3-a4cd-a963390b6b55 | -12.66131 | -48.09605 | 2025-08-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 958d28c3-f125-3489-9456-1dfb68b4ef9e | -13.21119 | -47.23653 | 2025-08-01 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6430c6a-4066-3605-b716-6248b7195004 | -9.45993 | -57.8376 | 2025-08-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d13efa0-f33d-39e9-91e6-c972f55c43d0 | -10.08286 | -46.74218 | 2025-08-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 04c9a4e4-82e5-38cc-b9cd-ceea8b916833 | -12.27507 | -63.79628 | 2025-08-01 05:06:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 552033e4-e92d-3f7b-8741-bf239fa0feef | -10.43823 | -47.26154 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6963f07-9d1c-3ff8-b5a7-315347f6f6fe | -10.60812 | -45.27605 | 2025-08-01 05:06:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6da8393-55ed-395b-925f-c5df7d76a6e5 | -9.01476 | -59.53374 | 2025-08-01 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1a1df3d-efa2-30bd-bc3d-5046689e17c9 | -10.13616 | -57.77913 | 2025-08-01 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a89ab6a5-5a5d-35cb-b86c-230eef1275a7 | -10.43732 | -47.26871 | 2025-08-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7c1b5bf-cca8-3247-a628-5366afc249ee | -18.14237 | -49.96497 | 2025-08-01 05:08:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93412f42-36f8-3fd0-833c-74fc2312e55f | -18.44547 | -46.92415 | 2025-08-01 05:08:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d9cb65d-c1ae-32b8-96d0-9d740fcffb09 | -19.46045 | -56.88655 | 2025-08-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e781f40d-efa4-3b02-87b5-f50f61b8e6d3 | -21.44869 | -57.14499 | 2025-08-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 158989cd-d5c3-3c7d-945c-e962a7c35b1c | -18.95128 | -54.32177 | 2025-08-01 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
