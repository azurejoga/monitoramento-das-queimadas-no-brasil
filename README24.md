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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4821496f-2040-30a9-afc7-03379cfc07aa | -2.94753 | -50.47381 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e9ec0a03-f4e0-37b4-a1f3-3192c26ad534 | -2.94016 | -50.48172 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5acbdaf4-3e49-3cde-a1c9-73f211dc4bbb | -2.94685 | -50.47834 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e96a280b-5412-3158-ab28-7502c9a0fd89 | -2.9361 | -50.46754 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23879246-f274-34cc-8d8c-9a3d0e9dff6b | -2.94821 | -50.48132 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a56a9f4-4d93-36a2-9af5-428d890f6f06 | -3.55062 | -48.17596 | 2026-09-09 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73bb3dc2-5d7f-3d12-97a6-0ba840124c60 | 4.13559 | -60.9382 | 2026-09-09 05:27:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fab69e3b-de3c-3b95-8712-eb2aa537369b | -1.19127 | -55.71802 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6f7bca36-d4a7-3ecf-8899-3dbf7b56128d | -2.94148 | -50.47287 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 583a8673-3f47-3041-a963-a6a44d8ae317 | -1.60921 | -54.90954 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e914373d-cb20-3cf5-9460-d49e5ca11ed8 | -2.4851 | -58.00581 | 2026-09-09 05:27:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77194c3e-92eb-30ed-a8ab-4431237b7eb5 | -2.93265 | -50.46044 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f15425b3-b682-3b10-9d26-35f4024ecc0b | 0.30253 | -60.44233 | 2026-09-09 05:27:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab5bf2b2-496f-357b-a2d6-93fe006d6537 | -1.1954 | -55.71864 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cfbda099-7028-3e0d-b815-58994e5b556f | -2.93677 | -50.46302 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f907cc4-93bd-310f-a2b4-f2f24bfddb90 | -1.31847 | -54.66245 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9055efe2-7ed9-394e-ba68-a8a7f2fb6321 | -2.11796 | -54.3832 | 2026-09-09 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e14451bb-dc14-3913-a426-3c12f31c195a | -2.94885 | -50.47686 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26ac2508-1db8-3467-8fdf-0230fae253f9 | -1.97047 | -56.77973 | 2026-09-09 05:27:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6436f0fd-f94e-3ebb-afec-12a57386bb28 | -3.54363 | -48.17474 | 2026-09-09 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eb52f17a-0930-352a-941e-f0047cc03128 | -1.03975 | -53.73379 | 2026-09-09 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 576ef279-d5fa-316f-94a9-a9710b6a2366 | -2.94821 | -50.4693 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d8481a9e-a9db-32ae-be70-d927735b72b9 | -3.54966 | -48.18264 | 2026-09-09 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 987189c7-f651-3243-afa0-cc6822dc401b | -2.94282 | -50.47583 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 019b77c6-0fcf-3493-b025-30f0a5540764 | -1.20747 | -55.75052 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09a79ae9-06c7-3f89-972f-d0bf2ada39e5 | 3.2107 | -60.28537 | 2026-09-09 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cae73988-023d-3401-8168-3bb301d53483 | -3.26932 | -50.08043 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db9eef72-98be-3d46-9b18-a7623e1a9914 | -2.76775 | -48.57363 | 2026-09-09 05:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff9917cd-3aeb-3b34-b267-78f09cca1895 | -1.60855 | -54.9138 | 2026-09-09 05:27:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f56de20b-bdda-312f-888f-811dc9083754 | -3.54876 | -48.18895 | 2026-09-09 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f5f3705-f360-3e72-8974-bdb575f578f8 | -1.18861 | -55.71857 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8409fa40-7e05-3dea-a76a-fbd2332240fd | -2.932 | -50.46499 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61288825-3a6c-34f6-adf9-f9be29bd9ded | -1.19072 | -55.72166 | 2026-09-09 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f970a84-b215-379b-8efe-f35932eb4525 | -2.94081 | -50.47737 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 06dbc9bb-556e-37cd-9ae9-0fffdc9d47c0 | 2.51117 | -50.85616 | 2026-09-09 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a41d1e8-74ac-3b44-b48a-953c60cdb35b | 2.66433 | -60.18087 | 2026-09-09 05:27:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32186df8-1c22-3720-a089-85087bf18afe | 2.51059 | -50.85265 | 2026-09-09 05:27:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ff0db88-4ea4-31b3-8c55-87b420531a48 | -2.93135 | -50.46955 | 2026-09-09 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76df3c88-e59e-306d-bb9e-1a0ddc7f359f | -1.62051 | -55.13635 | 2026-09-09 05:27:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5abcccd2-bb46-3997-a303-f0fbe44581bd | -1.03424 | -53.73814 | 2026-09-09 05:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd85d984-22cf-344a-9ac7-1f05dd5a9706 | -3.38846 | -61.31106 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eca9be1-8949-3618-a13a-6a1625baa98e | -6.9514 | -59.75858 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64640e70-23a5-3d1e-83de-836666703e63 | -3.67845 | -58.52395 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 499ebfde-f558-3771-b0f5-6cc660597513 | -4.28989 | -59.96742 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5071750d-6116-3da4-a831-3c4adcfbb859 | -3.96213 | -59.36228 | 2026-09-09 05:29:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cb2e915-1eab-3c7f-803c-fecf4d372974 | -5.38336 | -54.44723 | 2026-09-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 24ec0c71-4336-3741-bb8c-69c65c9acbe6 | -2.7377 | -58.18845 | 2026-09-09 05:29:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10226c71-db18-3013-86c1-72a3e9de1259 | -3.55729 | -58.55767 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af80a870-7f44-34d6-a5ef-c4293e9c2376 | -5.21726 | -55.99223 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7dcc1c13-bb83-39f6-95f7-07f760bd5770 | -5.44554 | -60.23103 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f25a129-61ce-3f94-9392-6062be929b0e | -3.79828 | -52.40552 | 2026-09-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcf48231-c4c4-3cb1-bd3f-5a4828357ca6 | -6.79635 | -58.95024 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6972d069-9e5c-38c9-bed2-5787c65a3e3d | -5.36707 | -56.02416 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbfa34a2-5ed8-3f25-9408-82d8013bc0da | -7.12458 | -56.51061 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b678c9fa-79ad-37fd-8792-0d3101e639df | -3.37047 | -59.42272 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f086b65f-3f28-3649-b8fe-92b3d8064e86 | -3.06602 | -59.85403 | 2026-09-09 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8476e7c-ec41-337b-9c52-7fc3919e297b | -4.19442 | -59.94955 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4305f7dd-68dd-3142-8360-c5998647b3b5 | -3.4544 | -59.99097 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d008b078-dea6-3d0c-b7fa-343dbf0d2b02 | -3.37968 | -59.40868 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e542f572-54f5-3018-af69-76a057313312 | -3.44121 | -59.2623 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77893548-fa6f-3da3-ae7f-229ce1850c09 | -3.35896 | -59.42868 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e770e2e-261e-37e8-9175-f0cd459f0b2c | -5.44782 | -60.23892 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dc17e06-d2dc-3460-9d36-1044ea03b1aa | -5.45009 | -60.24681 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18dc1eb2-42b8-3b2d-9743-128f00e96dd4 | -5.38302 | -54.44796 | 2026-09-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9553c71-be4e-3245-954f-4704442ebcf6 | -7.12193 | -56.50777 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38dcab91-7138-3f68-ac52-7c3889c99b5b | -6.63751 | -59.43967 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3d13c0b-80b1-3a80-b071-c10f4bf3d9a7 | -3.38132 | -61.31348 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c34a4779-dc04-3f58-b20d-7fe8f52a29ad | -3.55792 | -58.55359 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7af0f228-4247-3abf-8caa-e8a063f4d013 | -3.389 | -61.30762 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2771fd7c-4810-39a7-b48f-ee70bd7a1f93 | -3.39561 | -61.30864 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bb5268c-baec-3fab-ab49-c0a9c2213d38 | -3.8292 | -59.40485 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3b7983b-95c5-364e-9967-1b59cd7a290c | -4.24148 | -62.23077 | 2026-09-09 05:29:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8d1eabf5-00bc-3ffd-9f9f-93dd5749d547 | -6.55589 | -62.89474 | 2026-09-09 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9248e324-fa45-33af-a4c8-b20e1cc602c2 | -3.1532 | -60.65757 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c4c37a26-e6ad-3ea6-bae5-46f97fdf74c5 | -3.06017 | -59.27251 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd4d3294-8d76-3fc1-b270-93ee9adac633 | -3.36126 | -59.43676 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4f4d853-0918-353f-8bd5-0eea06bc15ba | -7.11975 | -56.51401 | 2026-09-09 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 975ba977-3432-319a-8aac-4776b4d98394 | -6.24321 | -51.67296 | 2026-09-09 05:29:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb5ce381-c0fe-3975-94dd-074056475e27 | -3.35822 | -61.28515 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03061024-bd8f-3f29-9c48-a9420356e0dd | -3.06363 | -59.27304 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f555f34-c105-3126-920b-3e62723b4941 | -4.44451 | -54.83063 | 2026-09-09 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c4e81ae-1e48-3d81-b2d4-9271e76da89d | -3.37277 | -59.40762 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8df282ae-0710-3343-858b-79d637c226a6 | -3.15653 | -60.65808 | 2026-09-09 05:29:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ba1f24e2-fc13-3c1e-a65b-1ca5dbd45b91 | -3.66392 | -58.89915 | 2026-09-09 05:29:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0c2a554-09ff-32f1-ac92-01a0f025e10d | -7.08716 | -59.82159 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98a2e409-7a1e-3338-9cd4-2066a9446263 | -5.37197 | -56.02069 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3dc43752-c4a6-37e9-ba32-357cf530a64f | -6.63395 | -59.43911 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d2c961d-b481-3995-865a-4af53d52e734 | -3.35838 | -59.43245 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65a54fc8-89e3-3af3-8f2d-dccd90c65d51 | -5.21295 | -55.99161 | 2026-09-09 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 33047e96-bcc0-3bc1-9436-20ebdf6cc9c6 | -3.39231 | -61.30812 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdfc4da1-0f86-320a-9a75-750f061ae33e | -3.15905 | -58.64673 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cfe6daf-b259-3d66-aa16-1f337149e2b6 | -5.44441 | -60.2384 | 2026-09-09 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d61884be-3b4a-3312-952e-e4eb7c023026 | -6.55534 | -62.89822 | 2026-09-09 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24c77c1a-bfe4-3fe9-917d-229c87e7ed86 | -7.05665 | -59.78135 | 2026-09-09 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 414fb83b-0573-344a-92db-71c65909ef70 | -3.39892 | -61.30915 | 2026-09-09 05:29:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e20e1d6-bb4f-3db5-bb1b-81b6f52abd2b | -4.49801 | -55.49566 | 2026-09-09 05:29:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51c54e9b-fc43-306a-85cf-b15817fbe72f | -3.47773 | -60.00578 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e75d7dea-7981-3247-b7ba-28805da15fbd | -3.56088 | -58.55822 | 2026-09-09 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41a01bfe-9cbd-39bd-b70a-9c3d39d5841c | -3.79095 | -59.72248 | 2026-09-09 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 301c2b07-a713-359c-9620-cc94198dc25a | -3.36456 | -59.84727 | 2026-09-09 05:29:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
