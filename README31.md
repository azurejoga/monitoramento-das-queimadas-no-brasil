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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45803796-1d2d-3a33-9988-92d98168992e | -24.57813 | -53.78813 | 2026-08-16 04:44:00 | NOAA-21 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8932d753-122b-3993-ae84-c8bd1a1bf7c7 | -20.81283 | -48.9577 | 2026-08-16 04:44:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 757aa6f8-0b12-345c-8ba6-7c39312aad82 | -20.33121 | -46.72551 | 2026-08-16 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46619997-05dd-3a4c-9a3c-a35e9bc51278 | -20.32651 | -46.72883 | 2026-08-16 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e52cf21a-2937-3dfb-80b4-834fb291f287 | -20.5086 | -50.12315 | 2026-08-16 04:44:00 | NOAA-21 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 157a6f38-a8c9-3d54-912b-09b5c7f3e5be | -21.79362 | -57.33881 | 2026-08-16 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71b502a2-2a48-3837-a28d-06f8edad829c | -22.21603 | -48.62379 | 2026-08-16 04:44:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e88a9b31-e00f-3489-8f37-c9c64a75b2c8 | -18.99936 | -50.56063 | 2026-08-16 04:44:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cce5a836-8365-3ae3-8573-36456705738a | -22.87205 | -47.10158 | 2026-08-16 04:44:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 038dba6c-a414-3f8d-9203-4383a5dec525 | -22.78739 | -51.09044 | 2026-08-16 04:44:00 | NOAA-21 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3481e6a2-1270-3d09-bfe6-3b70413a26f8 | -20.33595 | -46.72195 | 2026-08-16 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5268636-c930-3a38-9baa-bc6b4662d8eb | -22.796 | -51.39689 | 2026-08-16 04:44:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 8770d663-8d34-30e1-8d01-777cf76355e0 | -20.89496 | -50.50787 | 2026-08-16 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e85b17eb-ff04-3196-b9f8-2c09d8a6f49d | -19.23066 | -46.79453 | 2026-08-16 04:44:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd54f8cb-1c5f-34bd-bccb-46f967c1f2b8 | -20.34505 | -46.75309 | 2026-08-16 04:44:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db3d6d3e-138c-3703-b054-0a50bf159f57 | -21.53009 | -46.76113 | 2026-08-16 04:44:00 | NOAA-21 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4c4819e9-0efe-36ba-a022-30ec48677ef1 | -21.69066 | -46.77567 | 2026-08-16 04:44:00 | NOAA-21 | DIVINOLÂNDIA | SÃO PAULO | Brasil | 3513900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61f99d81-3809-36af-bcf5-98e6e9108bf1 | -22.79999 | -51.39343 | 2026-08-16 04:44:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 20838cf5-8bac-3340-a3fb-268903e20ddf | -18.72783 | -51.007 | 2026-08-16 04:44:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f45735c1-062c-35cb-942f-854196a030d7 | -20.80909 | -48.95719 | 2026-08-16 04:44:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 75a50345-2fea-3cd5-9539-705d776dcd97 | -22.611 | -54.95057 | 2026-08-16 04:44:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4e189927-0372-397d-a845-967e167056db | -18.92235 | -51.38999 | 2026-08-16 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c187af3b-a5e7-32ec-8b4e-266e96e61afb | -20.87259 | -47.01545 | 2026-08-16 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 358dacc8-5153-3ffb-802e-f09afd74da2e | -21.45387 | -48.68449 | 2026-08-16 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2911919b-94a2-358d-b540-2ce4514fdb4b | -20.4115 | -51.36474 | 2026-08-16 04:44:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 90195c70-77b1-338b-98a7-4708cbdcc28f | -21.43491 | -45.18238 | 2026-08-16 04:44:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 814422e6-11a7-3647-935d-7465dc75d0eb | -22.86828 | -47.09662 | 2026-08-16 04:44:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9214b7a4-2b48-3a21-8a81-75b4d87b481d | -8.9415 | -60.5174 | 2026-08-16 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| de69ff34-1aeb-3654-ac41-9b956d6aa9b6 | -6.8387 | -56.4344 | 2026-08-16 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 01ca9d88-33db-3491-901a-67307961f863 | -8.9785 | -60.5349 | 2026-08-16 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e7234244-35aa-3eee-935d-0a8a03b3e6e4 | -8.9787 | -60.5156 | 2026-08-16 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| bcd736c1-84a3-3f2e-9430-afdc139d9508 | -6.6377 | -59.0795 | 2026-08-16 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9c2aae43-2ca3-3ad4-9d5e-062a1e3002dd | -8.96 | -60.5358 | 2026-08-16 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 77494814-cb91-32a1-a928-428eb4f67f96 | -6.6194 | -59.0609 | 2026-08-16 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a438fb3a-799f-3872-88d2-fa48cb1c7983 | -6.82 | -56.4551 | 2026-08-16 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 23dcd1f4-3d7b-3526-b21b-bcf25371928f | -6.7123 | -58.9412 | 2026-08-16 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e20106c4-8f1e-3331-9fa5-487d9075cd79 | -8.9601 | -60.5165 | 2026-08-16 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 30a0be1a-ee53-3ac0-8507-960eae40012f | -6.3137 | -43.6178 | 2026-08-16 04:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 3ea84089-c4f7-3899-9aeb-a77df516ddd1 | -8.9787 | -60.5156 | 2026-08-16 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 41650cb8-f215-3096-b78d-e0b70c1dcdea | -8.9601 | -60.5165 | 2026-08-16 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 8849b36b-8cde-3082-88d6-62a8abb01e66 | -6.6194 | -59.0609 | 2026-08-16 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d1f8a2c5-d6f2-325e-868f-e794f4c182ab | -6.82 | -56.4551 | 2026-08-16 05:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b203b20f-3d65-38ac-a53e-ca963fd4ca2e | -6.6193 | -59.0802 | 2026-08-16 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 37383800-3311-35c8-b98d-3578a58b69ec | -8.96 | -60.5358 | 2026-08-16 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 9d57ec85-f5f5-3af9-901e-0af419cdb4bb | -6.3137 | -43.6178 | 2026-08-16 05:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 654d60bb-6894-34a1-8669-79ab7283e556 | -8.4275 | -62.676 | 2026-08-16 05:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 2f1169e7-1ea1-312d-a34f-b8668e79b615 | -6.7123 | -58.9412 | 2026-08-16 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 1da4a077-91f0-3def-be25-53a2821a385e | -6.8597 | -58.9738 | 2026-08-16 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 1cb8c6f3-42ea-3843-a13e-89478ae364d8 | -8.9785 | -60.5349 | 2026-08-16 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9a576670-01f2-33a9-af5b-1b6a0bd498c1 | -12.7017 | -48.4753 | 2026-08-16 05:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 74855bfa-dd49-35ec-bc2f-045af160ad78 | -8.446 | -62.6752 | 2026-08-16 05:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 358b817d-06f6-3d4b-ab04-a9a58188272f | -8.4276 | -62.657 | 2026-08-16 05:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2dff0d3f-01cd-37be-9c31-48b6881591c2 | -6.6194 | -59.0609 | 2026-08-16 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| f8c71137-b10c-34fb-8fa0-309b18cab7a0 | -12.7017 | -48.4753 | 2026-08-16 05:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b638b031-e814-35b9-93b2-39567f0d371b | -6.7123 | -58.9412 | 2026-08-16 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c02b5d68-9b8f-3150-8a9e-5df9d1038a48 | -12.0095 | -46.4271 | 2026-08-16 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| ddc41590-5f58-3b2d-aa1e-a37cc7fa83a0 | -8.9785 | -60.5349 | 2026-08-16 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a2c6291c-5ef7-390f-8d9c-060e0601e911 | -8.9787 | -60.5156 | 2026-08-16 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 9decc991-a0e0-35ea-b440-1b2ea05638d3 | -8.96 | -60.5358 | 2026-08-16 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| fe9bfc6b-7447-36fc-87d3-a025e2d1688d | -8.4275 | -62.676 | 2026-08-16 05:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 169.8 |
| 11e4b237-5571-3f96-9e90-8527a649ef4b | -6.3137 | -43.6178 | 2026-08-16 05:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 3beca12f-9442-3a12-96c1-9f109d291fa4 | -8.4273 | -62.6949 | 2026-08-16 05:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 38b44885-e495-3723-9a05-1c6f98799e58 | -6.6193 | -59.0802 | 2026-08-16 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ec387f97-0d47-3e7a-9e09-7a0cb1b32a38 | -8.9601 | -60.5165 | 2026-08-16 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| cb300a5e-169c-37db-ba40-003a44dde051 | 3.86586 | -51.79878 | 2026-08-16 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d80df79e-2f71-30fb-a5ea-c4f3bbb3363e | -3.26022 | -49.52546 | 2026-08-16 05:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3c39cff-1d88-3757-818d-20dd0416afba | 0.49018 | -60.598 | 2026-08-16 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de89090e-d194-3273-ad08-7e5587f83839 | -4.09441 | -42.49847 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 23fc4536-d720-367d-9872-57f0e52fa7c6 | -2.95835 | -49.27223 | 2026-08-16 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24b54fe4-a2c7-3eec-ab3c-ae0af1f4da77 | -2.95897 | -49.26821 | 2026-08-16 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 416e2a4e-435d-3861-91df-a98929a0e286 | -2.76704 | -48.56773 | 2026-08-16 05:14:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5ecacb4-4423-37c7-bb44-3bf37c3c3bce | -1.80231 | -48.06417 | 2026-08-16 05:14:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f990cfa8-0ab5-3abd-9c36-0956660dbdfa | 0.48951 | -60.59383 | 2026-08-16 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 771d7997-2f53-335f-b3fc-89e50a5168bd | -1.59074 | -50.44107 | 2026-08-16 05:14:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec0cec18-e0f6-39fe-9cea-2dd6a81c5b0c | -2.9602 | -49.26017 | 2026-08-16 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f243086-e95c-3f54-9a7d-5e31ccb4121b | -3.50013 | -48.03669 | 2026-08-16 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c0516123-3bdf-3f8d-ac09-1b63e3e3676a | -4.01471 | -49.46228 | 2026-08-16 05:14:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc81d571-f0f7-3958-9166-7d304393ef66 | -2.95468 | -49.26756 | 2026-08-16 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c756db79-789d-331b-a0c7-4da70a6e383d | -2.82594 | -46.73415 | 2026-08-16 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 82e4be18-55fc-3992-8e75-67a56b3137be | 1.58004 | -55.78307 | 2026-08-16 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81fae9b8-f451-37f4-9855-cea94c256874 | 1.57888 | -55.77578 | 2026-08-16 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bbadaba-8e82-309c-a558-253be3028660 | -2.9553 | -49.26353 | 2026-08-16 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66a2cc75-e8c5-30f9-b623-586122415f03 | -2.95958 | -49.26418 | 2026-08-16 05:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7df2e47c-a3a7-37a1-9523-c268ff6a6fdc | 0.7113 | -52.02173 | 2026-08-16 05:14:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d032c3ab-4b54-3144-bb1b-ed3d22622540 | -4.09356 | -42.50456 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| ed20f636-f70f-3655-8625-a3d8f3faa1e4 | -4.10123 | -42.4995 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fe7ad545-633c-320a-86bb-081336e7770a | -4.27255 | -48.5666 | 2026-08-16 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d35431-1eff-3184-a70c-7e811475fcf4 | -3.49846 | -48.04002 | 2026-08-16 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5db59b4e-41e3-304d-b729-cdd7ac403434 | -3.50482 | -48.03753 | 2026-08-16 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 590de8f7-641e-31af-8c92-6f59804fbc4e | -4.09379 | -42.49947 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4197e2b5-39ff-3a55-8cae-164d00933f13 | -1.83157 | -54.66262 | 2026-08-16 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 042f602d-c152-3235-996a-42643252e493 | -4.10632 | -42.51277 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1e9826ba-a98b-3393-920b-e807d2d926aa | -4.10061 | -42.50048 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0b696946-3c87-3661-ac1c-0ac8ea288123 | -1.81097 | -54.87443 | 2026-08-16 05:14:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 355a6d93-98d7-3902-9149-58920d794ef0 | -1.80302 | -48.05948 | 2026-08-16 05:14:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0535d92-cc10-3495-bd9b-48763327d77d | -1.58686 | -50.44048 | 2026-08-16 05:14:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6634dc67-bcc6-384e-8298-6d99a71b61cc | -3.28979 | -56.99205 | 2026-08-16 05:14:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b251f24a-2b9b-3961-a327-533a7c014ed8 | -4.10742 | -42.5015 | 2026-08-16 05:14:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| abf76c97-8aef-3a69-a022-25fdffbf6bd5 | -0.00323 | -60.57152 | 2026-08-16 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9886542c-8d79-39cb-a4d0-a7f8f1d3782a | 1.57946 | -55.77942 | 2026-08-16 05:14:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README32.md)
