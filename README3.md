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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 371d26bf-6f19-3a5d-8be8-691c844e73db | 2.6902 | -60.3731 | 2026-03-11 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 131.3 |
| d4e44735-70c0-3885-80c6-83486926cf97 | 2.7085 | -60.3539 | 2026-03-11 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 57307ffe-02fe-377e-bc04-7c4a2e4c707c | 2.7085 | -60.3729 | 2026-03-11 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 451efaac-c3db-37c9-b7ac-73593fd884f6 | 2.6903 | -60.3541 | 2026-03-11 04:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| d81fde26-d682-3e42-897d-9b12e3b74217 | 2.7084 | -60.3919 | 2026-03-11 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 1793a70b-8002-30fe-b018-17e79c9bdb82 | -29.3579 | -56.28067 | 2026-03-11 04:10:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| cd26f70f-861d-31dc-b9d4-282e0f3a1801 | -30.307 | -53.9754 | 2026-03-11 04:10:00 | NOAA-21 | VILA NOVA DO SUL | RIO GRANDE DO SUL | Brasil | 4323457 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| e7c1b531-41c8-30a6-948e-ccb0352c92a0 | -29.74188 | -53.08447 | 2026-03-11 04:10:00 | NOAA-21 | PARAÍSO DO SUL | RIO GRANDE DO SUL | Brasil | 4314027 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cebf8b7c-74c8-31bd-9a3b-5a9e17559531 | 3.2211 | -59.9075 | 2026-03-11 04:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f64fc91b-8182-3725-b1a8-9602723b505f | 2.6902 | -60.3731 | 2026-03-11 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 77289de8-1dd6-3843-b666-f71fdc7f1348 | 2.7084 | -60.3919 | 2026-03-11 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5581a107-a01c-35d8-86ff-01e2e7131ae7 | 2.6903 | -60.3541 | 2026-03-11 04:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 764256a8-4895-3216-951e-e644d95ab4ad | 2.7085 | -60.3539 | 2026-03-11 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 168.1 |
| ff2f557d-2f43-312d-a633-4c83400fd011 | 2.6902 | -60.3921 | 2026-03-11 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fb00eb9d-6bca-307c-a81f-2c795455e6b7 | 2.7085 | -60.3729 | 2026-03-11 04:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 225.2 |
| bd711ce8-4aa0-381a-ab35-1fd5b97e7963 | -11.55571 | -38.26002 | 2026-03-11 04:34:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 26fac350-98c8-34f8-88f7-2a71143fe2cc | -15.13933 | -41.83231 | 2026-03-11 04:34:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a561480f-5a1d-3307-858e-f7aa15d7f350 | -13.55567 | -44.68733 | 2026-03-11 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4830b2cd-e207-35c2-84a3-ed935512cc16 | -13.42187 | -41.32005 | 2026-03-11 04:34:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b8f8d80-feb0-3c5d-8e3d-e5710c689fd7 | -11.55038 | -38.25923 | 2026-03-11 04:34:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 43ca10a3-2847-3fe5-a93e-d08d58442b27 | -9.15617 | -40.07944 | 2026-03-11 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74740b90-6f4d-366f-91e7-65ac30002863 | -11.54994 | -38.26264 | 2026-03-11 04:34:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d8af3348-fb83-3c32-81df-203882b53472 | -11.56061 | -38.26417 | 2026-03-11 04:34:00 | NPP-375D | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| db031255-5249-353b-aacf-4a3f26f65aff | -15.75501 | -41.41586 | 2026-03-11 04:34:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 121b3178-ca69-39db-96d5-b0f2e7532d9a | -13.42298 | -41.32261 | 2026-03-11 04:34:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97da4a4e-c603-3ae8-bdc7-c70024fa9e99 | -12.01214 | -45.35218 | 2026-03-11 04:34:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f997ed80-7024-3a66-b318-49b0d65ef40a | -17.09559 | -46.46902 | 2026-03-11 04:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1102763-a19e-3090-b18c-9bd1b2c51334 | -17.09505 | -46.44862 | 2026-03-11 04:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95b2c618-0819-331a-a7d7-a578ec1a53fa | -21.92216 | -51.85348 | 2026-03-11 04:38:00 | NPP-375D | PRESIDENTE VENCESLAU | SÃO PAULO | Brasil | 3541505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e353bac3-3fef-34bd-896e-8a0b6e8b392c | 2.7086 | -60.3349 | 2026-03-11 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a7f32c92-cf78-3889-a844-d0d254ce0fe7 | 2.7084 | -60.3919 | 2026-03-11 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| dbcc1a2e-4666-3199-bf29-2c5cd276cb69 | 2.6902 | -60.3731 | 2026-03-11 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.6 |
| fab91ad4-7d6b-384f-b04b-746268e6b602 | 2.7085 | -60.3729 | 2026-03-11 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 02cd689d-4ed8-362e-abe4-db4db18ec345 | 2.7085 | -60.3539 | 2026-03-11 04:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 276.1 |
| 0932c3da-45af-3dd2-82ab-f040fa394b31 | 2.6903 | -60.3541 | 2026-03-11 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 8a139d60-1476-30d8-b8cf-6d2065db4ef7 | 2.6903 | -60.3541 | 2026-03-11 04:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 583aed4e-d9cd-3335-af6c-5c74b88667aa | 2.7084 | -60.3919 | 2026-03-11 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b60278c3-a6c4-3458-93c8-c871979765c5 | 2.7085 | -60.3539 | 2026-03-11 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 4f1dd3f0-c888-367c-83e1-40c1d1607129 | 2.6902 | -60.3731 | 2026-03-11 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 2a65da0a-0f1d-3a37-b2e0-bc591a59c761 | 2.7085 | -60.3729 | 2026-03-11 04:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 171.1 |
| 9228ce3a-2f2a-34c8-a73e-f481d1a14057 | 3.23292 | -59.8946 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8d63704-80be-359d-b2b3-52606c3700c1 | 2.70523 | -60.36232 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 2d20b831-9adc-3572-970d-9e8df2bb28b6 | 2.70583 | -60.40332 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 444c7904-d583-37ce-b663-59b46287aae4 | 2.69527 | -60.37133 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a81d6e4d-6bcb-3f64-8a6d-bab289b97133 | 2.69306 | -60.3568 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 328b076c-f418-398b-b40c-75e86c7a5598 | 2.70585 | -60.3693 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e519aa1e-c4fc-3979-8458-849c3004d1c9 | 2.71404 | -60.38666 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 35500be5-d82c-3ac9-a963-bbdfae99e3fd | 2.70957 | -60.39486 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ecf13b0-0bb0-31a9-8d40-eedf1d30d3a8 | -3.85804 | -54.08265 | 2026-03-11 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 507e0a76-b602-30e3-b503-b822fa0f9c5e | 2.71744 | -60.37113 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 401f9890-fe94-3198-a4b4-323dc9f4d619 | 2.70478 | -60.362 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ca3c46ee-b54c-354f-9a24-eb19cf91cf27 | 2.25807 | -60.28051 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bab35a91-02aa-3e31-ac0f-88559d6e9ed1 | 2.7069 | -60.3732 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2709804c-c626-3fc1-9b96-621745ba6927 | 2.69859 | -60.35595 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f355dc0d-3064-3417-9ca5-7dd27ca0480e | 3.22312 | -59.90313 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc88124-fc24-3210-8aea-8f85dc788684 | 2.71032 | -60.36111 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 262c5351-ac92-3c4f-a636-b8e81c14ea70 | 2.70745 | -60.37681 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 31b68dbd-e895-33a6-88ec-7d3bb96666db | 2.70634 | -60.36958 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d7887235-07fb-38e8-b602-dd9275c550cd | -1.86329 | -54.68495 | 2026-03-11 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc55869b-258b-3cbd-88de-9677357617ae | 2.71081 | -60.39875 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c120fcbd-a65d-34f4-984a-95df3198ebd3 | 2.70136 | -60.37408 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4572c03c-2443-391d-b2dd-9d3419a9fed4 | 3.22751 | -59.89542 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 640c664f-0183-39f3-948f-de82a3d35038 | 2.70415 | -60.3923 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ff2085b-e85b-3c1b-88c5-d18eb8d08c5a | 2.7119 | -60.37199 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c65a9ecd-1556-340b-8e1d-d29459d99bd4 | 2.71137 | -60.36836 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4878a3d-17a0-3566-8b46-c9e95c186be0 | 2.70303 | -60.38501 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bf53bdd5-3078-38de-8985-94a8645a9481 | 2.7032 | -60.35109 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b88ab9-48e8-3e34-85cb-5e60c6d5b6ea | 2.71298 | -60.37591 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1d6572c-0263-3a8f-a610-4e0740a57955 | 2.70797 | -60.38388 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2eff72df-4604-34d0-b636-ebfc42535fc9 | -1.63753 | -54.49042 | 2026-03-11 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b278132f-6f6e-32c0-95ee-3ca8a5503a7c | 2.71354 | -60.37954 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 786bdec4-effd-3089-b3df-bd8f120daeee | 2.70578 | -60.36595 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 843d3eed-b7d9-3dbf-aad9-633585111478 | 2.70979 | -60.35748 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a25d334-080e-3795-88f0-6b13bbec2deb | 2.71131 | -60.36506 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a29eaf0-856f-3026-a736-887b55129e34 | 2.70247 | -60.38134 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e93314c1-0839-3db3-9955-10c5673dbc39 | 2.70743 | -60.3802 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cc78921-5338-3306-bf69-4ee1f9b0cd9d | 2.7069 | -60.37656 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94394d67-c926-3158-b13f-581b11f5e9fd | 2.69472 | -60.36773 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e4f1ad0-f614-305b-bd26-1849ea374422 | 3.22261 | -59.89968 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf2f20a-5bae-3cb5-92a2-fa45c1d85ef1 | 2.70913 | -60.38777 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 85d22dbc-75b8-323c-8282-996a7714da1b | 2.71411 | -60.38322 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d034c3a7-ccfb-37b2-baa1-4ed48c9c81ef | 2.70412 | -60.35506 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b4fede9d-28e3-3a4b-925f-2676fea74b27 | 2.69804 | -60.38945 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51701c65-6fb7-3f83-9e20-71db3bafc540 | 2.69803 | -60.35231 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df78961d-d81f-38f8-8380-634f448abf2d | 2.26342 | -60.2789 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 638c7965-1436-324e-b750-169b8e823926 | 2.69362 | -60.36047 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9921c16-bbbd-3e62-8b04-afff49c5fe37 | 2.71085 | -60.36474 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8e37bfe4-7ccc-31c8-a84f-20179486ff45 | 2.70467 | -60.35868 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 286fdade-60ae-345a-9d90-d3059fa76f0e | 2.7102 | -60.35781 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6508a160-e967-3c14-836b-53b679b91477 | 2.70532 | -60.36565 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4579ad5f-85c4-3281-ad56-0380c9de7770 | 2.70904 | -60.39121 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a130db9-07fe-3a63-a781-d8ce65b98584 | 2.71467 | -60.38689 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6741142a-c9cc-388e-97b6-d29f04299f17 | 2.70025 | -60.36683 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 75a10a7b-5244-3495-9bc8-26b8d02a9b64 | 2.70637 | -60.37292 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ee8c86f-2ff4-3f8d-bb68-582e0a347b79 | 2.71076 | -60.36145 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77dcac9a-5560-3b79-b9e9-1518fb545c2e | 2.7101 | -60.39854 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 420bd172-2d93-305e-8aeb-655401722cdb | 3.22802 | -59.89887 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31db28ba-6787-3f79-bb34-ff84ad93533b | 3.23935 | -59.90064 | 2026-03-11 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0ab5523-d619-3e05-befd-dcafeca399a8 | 2.69637 | -60.37854 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3724edf6-4fa7-3efe-bd49-0da71ff62d6f | 2.71242 | -60.37227 | 2026-03-11 04:51:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README4.md)
