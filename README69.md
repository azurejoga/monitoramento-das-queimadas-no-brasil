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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddf30d6a-68b4-3a36-b191-0406c4f4289c | -13.6606 | -53.95013 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 955ae211-564c-3cb4-9306-9ab3aa02cc76 | -14.39032 | -51.29036 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 001b8495-e950-3459-afc9-36d6efebea2c | -17.22056 | -46.84348 | 2026-10-01 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a2fa054-471a-3757-97ca-8ef2146f33e6 | -14.41421 | -51.25039 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fc2afab-3940-38cc-9017-c3f3f4baf520 | -14.40496 | -51.26154 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b78c7c81-87fa-3cfa-97da-a5c7aba54e19 | -14.39712 | -51.26439 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 9317e787-df52-36c0-a70c-80aa5a68394c | -13.65641 | -53.94931 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c674416e-0416-312f-96cb-e516d038e8e7 | -14.40068 | -51.26504 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 73ceb949-1d98-3a15-99bc-c43dbb00b354 | -14.14069 | -51.13315 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dcc3ab0f-593c-3ba2-a02b-f65ee912f803 | -17.87951 | -44.31384 | 2026-10-01 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bda8031-1128-3d58-9759-4d7902ab36d6 | -14.88291 | -51.88165 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b267c382-a5db-3bcc-bedb-46bdffeb54e6 | -18.87849 | -43.82772 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e0d7358-df79-3a24-af3c-eae0dbcae867 | -14.43554 | -51.25424 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc308e99-c624-3e3a-91ed-e1ec63956d25 | -15.16291 | -46.12761 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9c1bf95-9fc6-32f1-9427-fb157693e619 | -15.23932 | -46.15067 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c89d5ec9-8be6-3ddb-8f00-0fb71a336217 | -17.10508 | -46.47041 | 2026-10-01 04:36:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b078518-9f95-3ae7-9641-1210b15ebace | -14.39213 | -51.27206 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0e9e9dc8-fe11-378b-a6e5-fd942040884c | -13.65296 | -53.94446 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a8e25be-d4bc-3c5b-b0d6-9a3f8e48c142 | -20.2784 | -50.39335 | 2026-10-01 04:36:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 04d00102-5f9e-3c82-bbd0-b79da7e32e38 | -14.40017 | -51.25359 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| dd77b8db-ec37-3b03-b242-e5efcef348f2 | -15.63977 | -40.9875 | 2026-10-01 04:36:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 822a4414-d9df-328c-93e2-3b613b09a1e8 | -14.38179 | -51.2974 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4d276e29-e959-3532-8c5e-50cc3784efa5 | -14.15632 | -51.14871 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f10e6aa-ef0f-3c10-a1fc-8134c5fbc2c5 | -19.11144 | -41.49966 | 2026-10-01 04:36:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 09d10451-832e-3d1f-9b57-3bbca43757a0 | -14.42132 | -51.25167 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 065621e2-a9aa-3547-b74a-87a351e1fb51 | -14.38249 | -51.29323 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d511d31d-6706-30d3-84fc-79f065ec5410 | -14.87503 | -51.86214 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e73261e-fd7d-3989-a369-caca999e1903 | -20.53926 | -45.76316 | 2026-10-01 04:36:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72e2dd62-f570-37b2-bfe8-8c4f58b172d5 | -14.15277 | -51.14807 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54ed8200-6047-3f2a-a0cb-6a63be58b376 | -14.40639 | -51.25325 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d58d2370-3dd2-3ac6-b4f5-0f6e2d685d97 | -14.41698 | -51.31945 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41c270be-1e84-3334-a422-961955db05d6 | -17.91703 | -45.04177 | 2026-10-01 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8995fd9b-6989-37c6-a9e8-fe9a88399936 | -15.85298 | -41.70746 | 2026-10-01 04:36:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4fe69cb3-9d31-3545-a422-29f4da30bb23 | -18.22554 | -42.75339 | 2026-10-01 04:36:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 588997a5-bde3-380d-91e0-e197901ece96 | -18.89202 | -43.81045 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32fb369c-bc2a-3b04-86ff-5c07709d90d3 | -17.88344 | -44.31445 | 2026-10-01 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 316b2f15-2afd-3c3e-84f5-00f8087ba6b3 | -14.40212 | -51.25675 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 54721318-2567-32ee-aea5-e01245407431 | -13.64876 | -53.9437 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ce3203a-cc9a-39b1-a84f-b95f21a9bc2d | -13.65513 | -53.93254 | 2026-10-01 04:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62053fc7-430d-3be2-8df7-abd2ebf98bb7 | -14.39947 | -51.25774 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| d80f6c34-89f0-3a8e-96bd-a6508d58efe7 | -15.22779 | -46.15659 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7135bd9-ba20-32eb-882a-8dc7556cf3f3 | -14.48637 | -48.30833 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29d974f6-680e-3430-9ae9-3b369bfc74f5 | -18.88147 | -43.82781 | 2026-10-01 04:36:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2efaac3c-f70b-3430-bc4d-ec9e91aa5873 | -14.49687 | -48.30643 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 809cdffa-1516-3ffd-b77e-bc2f794b565d | -14.39592 | -51.25709 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| ffd02952-862a-3a9d-be85-a265941dc335 | -14.39382 | -51.26956 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 95be76aa-62c4-3ffa-a5d9-fbf9b5b46d3d | -15.22713 | -46.1368 | 2026-10-01 04:36:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b78b4834-6f00-3459-b990-190626f93c7f | -14.90525 | -47.73741 | 2026-10-01 04:36:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93e7e8d4-edec-3a47-8b24-0ab274f5245a | -15.3048 | -42.77038 | 2026-10-01 04:36:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 969b0fd9-c702-3fcd-91c0-aee6ca02ae93 | -17.91767 | -45.03713 | 2026-10-01 04:36:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f46126b-9e53-36fc-b63d-05f726a5ba11 | -14.4177 | -51.31528 | 2026-10-01 04:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cdc7f40-1665-37e2-b93f-f02b7174845c | -14.49911 | -48.29222 | 2026-10-01 04:36:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9fff640-816d-395e-b2a2-995db01b8a45 | -14.86928 | -51.85206 | 2026-10-01 04:36:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0df40dc3-7483-3beb-8e46-54ca05820a16 | -15.62883 | -44.7224 | 2026-10-01 04:36:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5216df3-6f9c-3fb8-a5d4-b919b8dc0f98 | -16.14058 | -43.7408 | 2026-10-01 04:36:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1532ea55-b0a6-3b87-a30b-0b2e80c48046 | -22.18907 | -46.92637 | 2026-10-01 04:38:00 | NOAA-20 | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1295c249-888a-397b-851a-bb922e536fa2 | -20.89876 | -47.41468 | 2026-10-01 04:38:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b3292c97-bcf5-3825-9ebe-6fa816c1cda5 | -20.47605 | -50.90803 | 2026-10-01 04:38:00 | NOAA-20 | APARECIDA D'OESTE | SÃO PAULO | Brasil | 3502606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eccc76f0-038e-3d96-a094-1007aabb6873 | -21.71343 | -47.13373 | 2026-10-01 04:38:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91eaf1a0-9bb9-3a9d-8345-785d6497fc70 | -21.49457 | -46.61312 | 2026-10-01 04:38:00 | NOAA-20 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fe941d29-8d92-3774-a44e-63021ca8a1d3 | -22.08467 | -46.9789 | 2026-10-01 04:38:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27e26a81-d15b-3cee-8691-dbb0b195f187 | -20.89934 | -47.41061 | 2026-10-01 04:38:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3ac17ba7-21d6-3c9a-8730-bedaca1ce8db | -21.17516 | -47.01373 | 2026-10-01 04:38:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba24891b-b9f9-3bfd-b4fd-4d5717883d2e | -20.89528 | -47.41409 | 2026-10-01 04:38:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05ea1e91-c1cb-3861-80bc-eb7484416bb3 | -21.71579 | -47.14284 | 2026-10-01 04:38:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb98ec8f-3fcf-3850-8631-795df1a862e1 | -22.1416 | -46.67441 | 2026-10-01 04:38:00 | NOAA-20 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b1201180-87a4-3454-97dd-0422fb66d77c | -20.89818 | -47.4187 | 2026-10-01 04:38:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a6fe7f74-8d66-32b2-87c7-0981dcafc876 | -21.45864 | -48.67885 | 2026-10-01 04:38:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09655726-6148-3f91-82d4-cbffb178f704 | -20.47543 | -50.91177 | 2026-10-01 04:38:00 | NOAA-20 | APARECIDA D'OESTE | SÃO PAULO | Brasil | 3502606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f44c1660-72f6-3d25-8c14-446fb75ffc8e | -21.1787 | -47.0143 | 2026-10-01 04:38:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e71879-1404-3709-a29b-3dc7ebc14b64 | -21.71638 | -47.13858 | 2026-10-01 04:38:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28311cc1-b61d-3415-9304-6270cbc9d82c | -6.6758 | -58.8654 | 2026-10-01 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 2c6e8f99-f8a4-3c0b-8810-a24be6fb725d | 1.9772 | -50.82899 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6669a95b-b6d3-377d-b4a1-13dea9fca5fd | 1.98232 | -50.83262 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fe807e2-ed82-391e-a1fb-2b5229e02e95 | 1.97348 | -50.83406 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1558e67c-0f06-331c-8135-639fb26f8658 | 1.98163 | -50.82827 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 821b1206-ea36-3be4-87c4-e561ae746e5c | 1.9807 | -50.85072 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 211ccbed-d47b-378f-8282-c9abae2a96f0 | 2.4861 | -50.79134 | 2026-10-01 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7c43438-136b-3069-89a0-10b217ad3924 | 1.96445 | -50.86228 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e479b71-dad7-387c-9ea0-54682740aa1a | 2.16322 | -50.91945 | 2026-10-01 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 117cc99d-2bb7-3cf2-b078-bbf24e380037 | 1.9779 | -50.83334 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 931c5fa6-4a1d-3587-aa6e-c7340e9ca750 | 1.96746 | -50.85289 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50eb604e-32b6-3c03-892d-fc7b7921ca4e | 1.9814 | -50.85506 | 2026-10-01 05:14:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4076660-d8bc-3dc3-ad76-acee7c4ee316 | 2.48623 | -50.79321 | 2026-10-01 05:14:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd4e3b97-3cb3-3f37-b37f-d08fa4b2d785 | -4.26 | -50.81 | 2026-10-01 05:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1631eda-ce06-3fe2-8537-ee288fd2f97f | -4.29 | -50.76 | 2026-10-01 05:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c492460-454a-3796-9c5f-7def6d3e1213 | -4.29 | -50.81 | 2026-10-01 05:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23feb5e0-03b6-320e-8d47-6213e921fd9a | -4.32 | -50.81 | 2026-10-01 05:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 437d0626-12c7-33aa-9234-03d6337575f2 | -4.26 | -50.75 | 2026-10-01 05:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f254ee6e-e040-3ef5-82f4-1fb4d80c0608 | -4.32 | -50.76 | 2026-10-01 05:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1423d2-45ef-358e-a530-ac4fd4201ba8 | -3.17968 | -60.07145 | 2026-10-01 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bb75ccf-4ad8-3016-8f40-b8ba828098b6 | -2.90376 | -54.0896 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01c45fef-9732-3fa2-84b4-fdde978e03d2 | -2.90304 | -54.09436 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1fb87e6-2459-35d4-b214-d7141c41a936 | -2.89971 | -54.14235 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 654d8d9b-35d7-3756-a8fb-c24f14f1363c | -3.18106 | -54.10715 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 66b49218-f0f4-33c5-8bb0-577c93407818 | -4.12743 | -46.87197 | 2026-10-01 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 294d97cd-6e18-3ef4-887c-c37abae3c7ed | -3.01885 | -53.88659 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03d920ff-5f02-3cb1-9933-f2378cad60bd | -3.16529 | -51.35556 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95521875-6e00-34a9-bff1-4dcfc1bd7d0a | -2.90042 | -54.13764 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 380c38df-3e6c-3038-a51e-650fbbf28942 | -4.27592 | -50.78767 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |


[Clique aqui para ver as próximas entradas](README70.md)
