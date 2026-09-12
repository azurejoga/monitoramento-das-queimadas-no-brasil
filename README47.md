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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57044eae-af2d-320c-b2b7-e64840393fb9 | -4.52233 | -54.95853 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e31ded1-6c6c-38a3-86ac-c751ac8f176e | -2.72799 | -57.64532 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 91d9e016-5af1-3bd4-8549-95a8b1403c85 | -0.42763 | -52.07479 | 2026-09-12 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 242a0700-611e-38b5-915e-8fb2dc9ad7ee | -2.73958 | -57.63932 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b5bb4f2-2850-3272-a9a6-1255450b7f72 | -5.85105 | -53.87434 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5fbbb95-8275-3764-a9e6-df54e422c172 | -2.94678 | -50.41719 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| ade40be1-aaf0-3d59-89d1-9e8b39d13121 | -3.3539 | -59.43653 | 2026-09-12 05:27:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e34812f-e4ef-363c-b7e5-736280768913 | -3.36818 | -50.76423 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5967ccaf-6a69-35a7-9914-d00ddc21035e | -2.90069 | -51.93583 | 2026-09-12 05:27:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04d3025a-830a-3739-8acb-cd158b271708 | -2.9544 | -50.40371 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| cf94d48b-25a2-3d7b-86e8-7189f45ec8f5 | -2.94497 | -50.39133 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa3599ae-5e2e-3eb2-839e-55f7b4d517bd | -3.38002 | -50.75896 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3de9e9d7-e5fc-3aa4-a0e8-8685ff965c1e | -2.8197 | -51.34541 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3c0a770-9c21-3583-9d3b-9b71da393373 | -2.7257 | -57.63718 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89e319a6-1827-3301-af98-d7ffa76453d9 | -3.85633 | -49.22232 | 2026-09-12 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a946fa40-4f53-377f-8792-d65e612ea592 | -2.9693 | -50.41695 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 4515f560-342f-3469-a9ef-b029e85457aa | -3.35113 | -59.43255 | 2026-09-12 05:27:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61ddd5d5-15c3-3bbd-9b95-8a56e11869ae | -4.36269 | -54.77874 | 2026-09-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f85fdce4-0609-31a6-9592-74a4f97d9871 | -3.40349 | -59.23054 | 2026-09-12 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b1a1072-cdea-309e-a2c4-aa574d224a24 | -3.38492 | -50.76314 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3c87fe2-afe4-3910-b32e-abaff1951795 | -4.82235 | -55.77041 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff7c2408-e28b-345c-b610-b53615840743 | -3.15988 | -58.64426 | 2026-09-12 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b345e0d3-9c41-3a81-b4f7-568f90aeec3e | -4.36034 | -47.78225 | 2026-09-12 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d06455d9-06b8-36fd-88cf-d3472702fc17 | -2.9638 | -50.41614 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 7114988c-63c6-371f-91a5-e104284948d4 | -4.81874 | -55.76633 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b83cbb9-a01e-35c9-9464-0700c0c2abaf | -2.73898 | -57.64312 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00631725-12d2-3b35-b694-badc0c8ed505 | -2.96434 | -50.41255 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 8029aceb-f8a2-3039-bd40-a542b1136c9e | -2.95547 | -50.39649 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 05282175-6938-3210-929c-d12581ffadc9 | -2.967 | -50.39467 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e808ecef-719d-3b90-9d18-7994802302a3 | -3.97224 | -53.43936 | 2026-09-12 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e16389c0-cf9c-3aa6-aa4c-55912321a431 | -5.79556 | -53.81038 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a159f704-9131-3ff0-b84d-51f9b357d2d0 | -4.82267 | -55.76693 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29880e92-b483-3620-8f45-e35234ae6971 | 1.23145 | -50.72504 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97e86e0e-9017-302f-8e2f-fae8a6a6603a | -4.4679 | -55.43534 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16baec00-5ba2-3a4c-af38-54d754849144 | -2.72113 | -57.62088 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 58e99094-8c8e-3e44-a292-2c04390784bd | -3.89663 | -55.81876 | 2026-09-12 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 668a3b18-cd79-3bf0-84cb-8479f872dbbe | -5.78899 | -53.82364 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f19cb515-7ed6-37ba-a297-020365720f7c | -6.50786 | -47.60005 | 2026-09-12 05:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9f632c2-1536-3598-8e25-e2d7dddddbb9 | -2.72164 | -57.64045 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e0084577-b885-3967-b81f-48926d0d91d7 | -4.30417 | -49.11038 | 2026-09-12 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 025a78b3-0848-3a61-ba98-9ab465c5b845 | -1.1908 | -55.72091 | 2026-09-12 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5c35a15-1254-3c03-856e-2f4dd90afae4 | -4.35813 | -47.77982 | 2026-09-12 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 44b52964-887a-3562-bbf2-e94c1b90b94a | -3.16269 | -58.64835 | 2026-09-12 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f37a5e6-b254-3323-9bd4-f95d529f0370 | -3.75441 | -61.19849 | 2026-09-12 05:27:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 175751b0-a427-35ed-a073-5279e5f98389 | -3.20994 | -53.94516 | 2026-09-12 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bd920e7-8988-3d19-b8b8-db711699157d | -1.02814 | -53.7374 | 2026-09-12 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ae747cf-92cc-3d9b-8654-c6041026d4ff | -2.96754 | -50.39101 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 76a75b2d-cddf-3bd9-b8ca-58ac9843a341 | -2.94444 | -50.39494 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 915499fb-56a8-38d1-a34d-09c1dbf760ca | -4.86657 | -56.00516 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa7dc488-d7ff-3645-aea0-b45dbd44a5fe | -4.53114 | -54.956 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d7bc764-311c-3bef-8689-3fc40e08c45d | -2.91132 | -54.11922 | 2026-09-12 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4114a61-44c8-31f4-af38-a28f24c66fd3 | -2.94521 | -50.38985 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d31c24e-2412-35cc-9232-897d37a31879 | -5.3727 | -56.02628 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78217f6f-8b5d-3a3a-bb49-5961a5a350ab | -0.42494 | -52.07204 | 2026-09-12 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9989e37-aa50-3acd-a6ad-87c5fb781ff7 | 1.03942 | -51.05574 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8b42054-514b-32a3-8755-961160a92805 | -4.36861 | -55.77371 | 2026-09-12 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c4349dd-29e9-380d-bdf7-e07206796dd0 | -3.379 | -50.76574 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e91e2a2-e4bd-34ce-9958-5fb0e4474e2a | -5.85248 | -53.8722 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6740493d-370f-3e13-9b7f-12f9c31ac220 | -2.93787 | -50.47754 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bace670a-81b1-37d4-8792-2af00e48cdc6 | -4.36698 | -47.78318 | 2026-09-12 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1875c3aa-9d89-3058-b087-5b66ba2da2f0 | -3.59761 | -59.0745 | 2026-09-12 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1836ebb5-3ed0-329f-9d3d-08dc077916e2 | -4.52286 | -54.95495 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6782527f-20a9-3a8a-98da-96aae6022ba6 | -4.86969 | -56.01066 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a2b0053-93ad-3e99-b07d-30a956c52db0 | -3.69611 | -57.07162 | 2026-09-12 05:27:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ed2e560-bae3-3568-a5a5-638d694511cf | -4.5306 | -54.95963 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74bf742f-0ab9-30f3-91d7-3d82eeb0a28b | -3.36972 | -50.75392 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17fee4b3-4636-3248-8769-31f97709e445 | -3.23377 | -46.94871 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7e36ab43-bfdb-3420-b2f9-5177d975ef43 | -6.22745 | -51.68572 | 2026-09-12 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca183c00-5f35-39a5-bc9c-2e8191757ab7 | -5.85701 | -53.87287 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b08383-1a72-3fe1-9836-21b2bd011ccc | -5.85183 | -53.87675 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57ba764d-49d7-38d4-9706-106f8e01c678 | -2.9389 | -50.47057 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bdc9417-29f3-3150-b59a-54e1c9942587 | 1.325 | -60.71097 | 2026-09-12 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1fa6d70-fc59-35dd-9d1e-875c1bb25411 | -5.80922 | -53.81225 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5721a89-7ef4-37b1-bc11-b0e0b1e71072 | -2.94466 | -50.39345 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec50efe-9bf6-3450-9f2f-a4284f130180 | -2.97197 | -50.39907 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 125790fd-a388-327d-9269-30bdca878755 | -2.9583 | -50.41533 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 6b65d775-5607-3977-924a-57b528be87ab | -5.8308 | -53.79192 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a9732f4-b01d-3066-b31f-5b3b47e56191 | -2.94996 | -50.3957 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9128be38-66d1-3719-bf7a-eb62c19f2336 | -3.22557 | -46.9539 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 078d861b-5a14-3ab8-9263-c4232b5d1361 | -5.85558 | -53.87501 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 313af572-677b-3790-a376-43aa90a08ed3 | -4.82312 | -55.76545 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe6f144d-99bc-360c-9470-7b8406cc233b | -2.94731 | -50.41361 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| dc83c0d0-bca5-3b54-89a9-3778ca8bb519 | -5.79421 | -53.81967 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47181655-2475-30ef-98ec-588e8fd6ac2b | -2.95386 | -50.40733 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| c999ebb1-a2ea-310c-bb74-89dc8d767424 | -2.73621 | -57.61539 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a87fe77f-7911-3091-bb56-cf5b1d1a5766 | -4.475 | -54.97406 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f538ed31-c5dd-32ee-a4f7-eec2a5cb724b | -4.87046 | -56.00561 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87e32e95-a6cf-38cf-a38c-5cb6077b1081 | -2.97038 | -50.40976 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bfbf154a-69b3-3a0c-9bae-8effb4e9c838 | -3.30367 | -57.88209 | 2026-09-12 05:27:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| deb40cb2-6173-3fa1-a993-113465259957 | -1.72591 | -57.15493 | 2026-09-12 05:27:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4c32df9a-1223-343d-97cb-39362ac487f0 | -4.86735 | -56.00008 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c88e4009-b1d0-32bc-85e6-8901bd3a7e75 | -4.08237 | -56.30002 | 2026-09-12 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb11a97-23d6-36e8-be87-a0ea13c598fb | -2.956 | -50.3929 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6c59407c-4956-39a7-a135-c05d7a6b3730 | -3.5392 | -48.17952 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1372446-f591-32f5-9ef2-f61f629248a1 | 1.23621 | -50.75411 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86620deb-8c71-32dc-9cb7-17f49ec719da | -2.95653 | -50.3893 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b460a8f7-29a3-3ba8-bcc0-a909bbcb10a5 | -4.70382 | -55.99831 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01438fe9-b9ca-3670-9078-08c9cbcac76b | -3.3359 | -53.2709 | 2026-09-12 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381a911d-ad3b-30b7-84ca-b4cea1ad1e46 | -12.1288 | -48.9687 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ddf87ea0-229c-301b-9179-53a8cab2a641 | -7.11369 | -55.12807 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README48.md)
