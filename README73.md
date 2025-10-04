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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50eb7199-7303-3d90-995f-d3506ebb24a9 | -13.51084 | -47.26972 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcd2e87d-a867-36ae-8c89-4624425e449c | -7.77283 | -46.25947 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb6c3687-7eee-384f-988e-385d1a802e5f | -14.22025 | -46.06425 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84c6a618-e4db-3c87-827a-b64e91210753 | -14.24419 | -46.09837 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d9b83337-7474-3ff7-82bc-69c704d5ec6f | -11.90773 | -46.38438 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06f332d4-f9e4-311e-87c5-cf4d8fc736dd | -11.49444 | -44.98915 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1f2e90f-baad-3d97-8208-bf3b96655306 | -14.04334 | -53.9289 | 2025-10-04 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b73d119b-ebaa-3b45-b748-b96c666496be | -12.86477 | -43.33517 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 040a7069-3480-35bc-808e-88510d652143 | -8.01983 | -55.42295 | 2025-10-04 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31727191-4f55-3113-bf67-1250f9375241 | -13.32837 | -48.09241 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23eb0bf5-59da-3c72-9d04-315f945a8d5f | -13.74716 | -48.057 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd22346e-bac4-3a72-bf2b-15fdea51eb63 | -13.70418 | -47.34832 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33e7f613-9b59-32f8-b529-a4d7dc9148e3 | -14.23807 | -46.09362 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 44d15ca3-f5b8-3219-898b-d6c5c00df1bd | -14.93235 | -46.85887 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a72ef8d0-83d1-3cd4-b660-af1fae7d1c05 | -9.76602 | -48.57967 | 2025-10-04 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09e13fa6-74bc-3587-97d0-02a8d731e4d5 | -13.21698 | -47.82193 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d8d0b1fd-50b0-3008-a6ba-16e971c6348e | -11.47878 | -43.5006 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c3fa136-c331-395c-aa94-838b3f657b15 | -12.36407 | -54.16736 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dee68b76-7734-31c2-99c8-ac2f2c1f8c5c | -12.93885 | -50.98298 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c7c2511-569f-3c25-a4b8-921683f6d101 | -8.61996 | -54.96436 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 209f9f6d-343e-348e-b907-a558b69614ae | -10.99781 | -46.68159 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6e82f90-83f4-3763-b2e6-d8d50e764664 | -14.63099 | -48.24255 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b82ceab7-348a-3066-baa1-94469a479271 | -8.61951 | -54.99945 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca14828e-4166-3bbf-94cb-1398882176cd | -8.50602 | -54.60191 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84d4c64c-e990-39f5-af83-671e5ae76528 | -10.83189 | -57.17612 | 2025-10-04 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb5c38c1-c67a-33b2-9aa3-d96417f8e29d | -11.09854 | -49.84706 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38b05959-b790-3f32-908f-21ffe725f669 | -15.20494 | -47.63678 | 2025-10-04 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a194b9d2-f02e-3a6f-ba69-a0bafe6c9acf | -11.80457 | -45.02619 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea2a9d73-25d8-3bd6-84ff-7077ba71dd56 | -10.5339 | -44.51675 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3d2b38a-3da2-336f-b4c9-59b779c90735 | -15.91884 | -43.33887 | 2025-10-04 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f41ecf27-4f45-375d-b9e1-b494bf163f17 | -12.91251 | -46.92481 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0490a13d-840b-31eb-a393-036e9d3f93fb | -12.7184 | -48.56929 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46d5b364-b7dc-3d27-8157-8c1623f453d1 | -14.89097 | -48.34664 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59de99d3-c3ef-3fd0-bd2b-c0cadfcfe2a9 | -14.70022 | -45.19191 | 2025-10-04 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be6f38f8-93ae-352c-980f-c8b59f216c64 | -14.74204 | -48.1412 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c72015b0-9436-314c-b84b-b69797ae571f | -7.76797 | -46.26675 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 886eadf9-1814-365c-a763-dbe4b6992307 | -13.13347 | -47.93659 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd6bc8da-2fa6-3a17-baa8-5434eedbf4ee | -10.12474 | -52.35101 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e552f2cf-dbca-364f-9b32-72ecae525d56 | -9.6586 | -46.80338 | 2025-10-04 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a12dd02-fcb6-364e-a695-9ef5cf4bc070 | -8.61389 | -40.50148 | 2025-10-04 04:14:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6aff4651-b7bb-3ae9-840a-01928cb7d0bb | -11.85431 | -44.95044 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a950e78-f22d-39c3-8055-a6d06366391d | -13.28936 | -47.83398 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 969be8c4-4879-3fe9-ad2a-62a190890a5f | -11.92034 | -46.35128 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50b9a8ec-2631-3659-9038-127475e80eb9 | -11.91145 | -46.25972 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c708faf-48c6-3fc6-864b-3366c6421ed7 | -9.63332 | -54.31313 | 2025-10-04 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81492e77-816c-3550-84db-3c39b9422adc | -12.04134 | -45.20369 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f99d7b3a-5e03-3c93-9db4-726a0c9c5b8d | -11.91653 | -46.37407 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 850d7131-5890-3248-9e5e-ea994bbfec87 | -13.33095 | -50.94396 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0defa67e-ccd5-3e75-9659-2a243572074c | -12.41732 | -44.07773 | 2025-10-04 04:14:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 76a7d696-deb5-3296-80f0-e49769039635 | -12.99534 | -44.59086 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2221027-de2c-3e56-8600-5b3fb86f7d68 | -9.90012 | -43.73697 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e182876-99f7-3e49-8f5a-ebebef187614 | -9.34866 | -45.79697 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e2432cd-29cb-366d-a50f-eafd9f147665 | -11.28138 | -47.79568 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f6c86f0-91f5-3d31-8b25-69312c4b4092 | -14.43861 | -46.10158 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9f7dbb8-1f31-3e49-ac8a-cef1b56cb8ac | -13.137 | -47.80615 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77eb2eb7-65ef-372c-86e2-17727ecc63d3 | -10.5831 | -48.71855 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd07595f-2a5b-38a7-a20a-40a664bc0588 | -9.91338 | -43.80346 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab853a12-8123-3c33-b130-f0a3b4eca956 | -13.30082 | -47.81669 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3894eab-9ea3-3444-b85e-c2955d3f1f88 | -14.88483 | -48.29562 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29932c0a-c97b-3450-a577-dad36dd7222b | -13.78034 | -47.58334 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be1e2b91-df32-3421-ad12-ea0ef70428fc | -14.63174 | -48.26015 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8fdab44-8fc2-3e44-9a39-84ba5e343020 | -11.42288 | -43.48806 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31144a57-0227-38f6-93bb-47d33b1e9039 | -10.18569 | -45.50213 | 2025-10-04 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03a6380b-0b6c-32e3-8265-435facb21637 | -11.5082 | -45.00979 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d161d52-ad74-367a-9667-741e515b5024 | -14.58425 | -46.71504 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38961473-b764-3bcc-a6a8-0b47be77e0f3 | -13.74859 | -48.07057 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f08ca780-91a5-3e02-94e1-8d8610b86c61 | -13.10025 | -47.0112 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d318c0ca-bd21-3531-bed0-d15a5216cee5 | -9.93071 | -50.19578 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 263a2778-7a89-3789-bd7b-eba72ea021c3 | -12.30379 | -45.36493 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6e00218-d09a-3c20-96a7-8ffb1f435cde | -13.32527 | -47.57582 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6fdd3c6b-f27e-36e6-aa6e-c50c8ef5f256 | -12.59481 | -47.00069 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6966560b-8345-3a1f-a732-0fc22977e231 | -11.8845 | -45.0176 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54260e7e-9994-3127-b858-51b31bd73b87 | -8.62072 | -54.99787 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ae258c9-5386-3769-a59b-08c6b77a5439 | -10.56606 | -48.69962 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 86e151c2-ffba-3803-afb5-1a5d95ee9c29 | -9.11612 | -44.39556 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77e43bf0-5804-3cad-b66d-4eae1a39e961 | -13.17546 | -50.92561 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ef69370-d990-31f7-b7b4-06c95c2baaaa | -9.31625 | -54.5322 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 662e1cac-70b6-3ac3-ba96-5a5be616c0a6 | -11.99358 | -49.85207 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b538241-4e4b-3034-93ea-96a8c74bb33e | -8.17238 | -46.99854 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 799ec195-b818-31df-9a69-007ee5dce3bc | -14.65774 | -48.28436 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0d48f7e-717c-3601-9479-8d556a8b49b0 | -14.9317 | -46.8628 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22c5247a-4cf3-33ec-9b67-3f892a68ef00 | -12.95562 | -50.99078 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24cab7d4-fe9b-381c-82f6-7dda34e05e89 | -12.36653 | -46.5198 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e39b945d-4ca1-3267-9178-bdc093803639 | -14.67867 | -48.27162 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d52203f-06d1-3ad0-b6d7-d4e0bb4b35a2 | -13.84838 | -47.9274 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b222392-b213-39dd-baf7-b3b9b92b88f9 | -9.93967 | -43.57173 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aac409b-8afa-3396-8ffa-ab837bd517e8 | -13.10952 | -47.92323 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04ddeaea-f591-3ee1-9bf5-71085eb285ee | -13.11455 | -47.87197 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f83a05e-2c63-3c41-afda-c9bf824b2933 | -12.71768 | -48.55072 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2f70dd7-b072-37ad-899b-0461609dd36e | -13.68083 | -48.62072 | 2025-10-04 04:14:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c180af84-c75b-30b5-a417-6151963c6291 | -8.17563 | -44.13561 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6de8dc10-cc0e-3729-aeb1-2f381959f65c | -14.63247 | -48.25584 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2df814f6-e4c2-3e1e-9488-edc590241651 | -11.90456 | -46.34517 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1e2da7b-8ca6-37cc-a15b-26748f3f8dd6 | -10.33738 | -50.32592 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a92b5232-9812-35df-9c85-12fc59707879 | -9.8166 | -48.7267 | 2025-10-04 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 964fac87-6c8d-3784-a365-0958d7b63971 | -14.92995 | -46.89457 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44f9ceaf-7c64-3ed5-ae37-d58cd96225d5 | -13.26411 | -47.20427 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9927c43f-c38e-301e-b4ac-4754d90fedd8 | -11.47653 | -45.01542 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87e563bd-e033-38b7-8eab-63d795e24d93 | -11.16825 | -47.75463 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 878b0c66-f5d0-35b8-8688-b380cf7a904b | -7.7661 | -46.23324 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README74.md)
