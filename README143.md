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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2fa6e4f-055b-3506-8069-0c654f9be133 | -11.9276 | -47.8719 | 2025-10-02 11:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 030b6239-419a-3553-b0b0-333f6f9d699e | -11.9085 | -47.8745 | 2025-10-02 11:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 264.1 |
| 457eafe6-cce5-3120-9b98-f9474eee0781 | -13.0114 | -45.222 | 2025-10-02 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 23821da6-9f4c-3015-8e40-6e87637f8dc3 | -12.4182 | -45.0385 | 2025-10-02 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3ef4add7-3023-3e43-aac5-3e809d759c1d | -11.2799 | -47.8445 | 2025-10-02 11:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 9e5dffab-6dcd-3ec7-b7f8-db9617ce4532 | -13.0119 | -45.1988 | 2025-10-02 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 857921de-c482-39f1-9273-3c65fed2497e | -14.4255 | -46.115 | 2025-10-02 11:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 7fa5760e-ff0e-35f1-9cc5-4647b12d4a3d | -9.9369 | -43.7422 | 2025-10-02 11:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 0216c6ba-16bd-330a-ae05-ffcaf8090ec1 | -14.425 | -46.1381 | 2025-10-02 11:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 593a3f83-393f-30dc-a67f-0f79d2bc0b4a | -11.9085 | -47.8745 | 2025-10-02 11:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| a7723da1-e1d7-37ad-94ea-aa276643ce6c | -12.9507 | -46.3789 | 2025-10-02 11:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f5a243c2-a182-3589-bb7c-e5e1116c1ed8 | -9.9369 | -43.7422 | 2025-10-02 11:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| ba04601b-cdb1-3f51-8e2e-8eb3ef299ae4 | -11.8238 | -45.0132 | 2025-10-02 11:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 55bebf03-b987-303a-b716-c9e4d31e2804 | -13.1735 | -47.854 | 2025-10-02 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 94109900-53b3-32a5-a911-93e3b3eb8345 | -12.4182 | -45.0385 | 2025-10-02 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 585d8f84-d81c-3487-a600-8c14d59a3374 | -13.0119 | -45.1988 | 2025-10-02 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 68ed9e98-6409-3be4-a741-5f849c3e023c | -14.1921 | -46.1321 | 2025-10-02 11:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 799a64e9-c561-3196-8e10-283530c168af | -13.0114 | -45.222 | 2025-10-02 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 9962501a-244e-3e7c-a6e8-f096f0e49063 | -13.1542 | -47.8568 | 2025-10-02 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| a0665f8e-4ec4-3b5a-ada0-622de2e4de2e | -9.4086 | -47.5521 | 2025-10-02 11:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 4666a22e-d011-34f3-b25d-63bfacc409fd | -14.4757 | -48.4137 | 2025-10-02 11:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 473f2962-e7dd-3cf4-8b2d-2e5f9444b918 | -11.0897 | -47.846 | 2025-10-02 11:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1f89e720-edca-3c4d-9ee8-204fe8c6cca0 | -14.9275 | -47.2159 | 2025-10-02 11:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 76c8174f-e537-38a6-8b3f-09bd6d48f1dd | -9.4083 | -47.5742 | 2025-10-02 11:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| e4c01278-5b19-3ad7-a40c-8b0f8efe5e81 | -14.927 | -47.2387 | 2025-10-02 11:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 0a49fb80-7404-347f-a34d-beee7fe1da1a | -14.4255 | -46.115 | 2025-10-02 11:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 14366c34-a19e-3f01-99e4-85a130df9765 | -12.9507 | -46.3789 | 2025-10-02 11:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d3381f1b-4c88-3d8a-8e95-24d513abe408 | -9.9178 | -43.7447 | 2025-10-02 11:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 811604ec-62ac-327b-983c-b5940531f630 | -13.1542 | -47.8568 | 2025-10-02 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 459ff74e-08b4-300e-ac58-db2cd4cb7393 | -14.2924 | -45.977 | 2025-10-02 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 37b3d6aa-d94d-3e6b-a1e2-db6c2993f3c9 | -14.4255 | -46.115 | 2025-10-02 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ea06b0cf-561a-3693-9f6f-9090678d2f9e | -9.4272 | -47.5722 | 2025-10-02 11:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 41bce0ac-9766-3b6a-bb39-a4a2844345dc | -11.8234 | -45.0364 | 2025-10-02 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| e2a731b2-61c3-3587-97f6-f97055735faf | -11.9085 | -47.8745 | 2025-10-02 11:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 244a8622-db0b-357f-a25e-9051066bb36b | -14.4757 | -48.4137 | 2025-10-02 11:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 11b3e4f0-09af-3086-b174-061254f2b47b | -13.0119 | -45.1988 | 2025-10-02 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f44d4dce-11f1-3909-9051-9557726fe503 | -14.3709 | -45.9403 | 2025-10-02 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9aaa5c48-9059-32dc-8e9e-763206cd1d91 | -14.4951 | -48.4106 | 2025-10-02 11:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 55572b30-6148-3d74-b4e3-186de449b55a | -14.927 | -47.2387 | 2025-10-02 11:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 62042c07-7352-3ec5-b150-6b069a31d590 | -14.1921 | -46.1321 | 2025-10-02 11:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 3f4b59aa-c8ea-32d4-93b4-4bb662a19e54 | -11.2799 | -47.8445 | 2025-10-02 11:20:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b50ace23-5306-3a6a-823c-9a7a56400e7b | -14.4947 | -48.4329 | 2025-10-02 11:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a5127f80-4365-31ea-9911-330855e4cb17 | -9.4086 | -47.5521 | 2025-10-02 11:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| b97be6d3-5d90-3802-8892-973677ec25a6 | -9.4083 | -47.5742 | 2025-10-02 11:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| fa92c492-7d08-3053-b5f9-3ea31a912b5e | -9.9369 | -43.7422 | 2025-10-02 11:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 6b0d26ce-ce08-3d75-af0a-6a46a1cb9848 | -12.2773 | -45.3834 | 2025-10-02 11:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1656cf42-11ed-37ee-b7a1-f66c479c45f1 | -14.9275 | -47.2159 | 2025-10-02 11:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1883f5f9-c782-30cf-9a4c-ddd826a5b46e | -14.425 | -46.1381 | 2025-10-02 11:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 0ab0b4fc-f253-3832-8c25-03bb8d27f1d6 | -14.9924 | -46.9091 | 2025-10-02 11:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4f22d622-e57d-358c-a505-eebd293c3b73 | -11.8238 | -45.0132 | 2025-10-02 11:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 8c15ac9d-9c4f-3ef0-852c-3a79b289fe7a | -13.0114 | -45.222 | 2025-10-02 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 25f1edd6-deb4-31f9-9de9-fa7013e50d8f | -10.9751 | -46.6569 | 2025-10-02 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 7382e0fb-aad9-3021-b547-a37844e467c2 | -9.4083 | -47.5742 | 2025-10-02 11:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 214.9 |
| c1e94886-8ecc-318a-b15a-88400b0b925d | -14.425 | -46.1381 | 2025-10-02 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7b9c5419-438f-3127-87d6-77959761dda2 | -11.8238 | -45.0132 | 2025-10-02 11:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| cda11eff-c6c4-3f6a-afb8-e72736f6dfdd | -14.3119 | -45.9736 | 2025-10-02 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c9374acf-dba3-3deb-8e61-c0bf13ea68c6 | -9.3894 | -47.5762 | 2025-10-02 11:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| be735d7c-6030-32b1-b7b9-ec97f1c1cdd7 | -11.9085 | -47.8745 | 2025-10-02 11:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 45897802-5dc0-3c59-91c4-e181eca43914 | -14.1921 | -46.1321 | 2025-10-02 11:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fa8d1816-8460-3cc5-bf60-594e99088d8a | -14.3709 | -45.9403 | 2025-10-02 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 84cd4e54-905f-361d-abce-3c8b5f00cf33 | -9.0803 | -46.6992 | 2025-10-02 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1a723518-aca3-38bc-a16a-e7a71c599241 | -13.1542 | -47.8568 | 2025-10-02 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f360374c-be89-34bf-bdeb-2f840a760a64 | -9.4272 | -47.5722 | 2025-10-02 11:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 69fcc8dc-3042-3191-b770-de2d31cc189d | -14.4757 | -48.4137 | 2025-10-02 11:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a9e045ef-6bd0-3e87-84d7-458b72071173 | -14.9074 | -47.242 | 2025-10-02 11:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b6f6178a-1c9e-3e12-9306-db262826087d | -9.4086 | -47.5521 | 2025-10-02 11:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 296775c7-7732-3474-9d33-3428b6715666 | -13.0114 | -45.222 | 2025-10-02 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 79fdb19d-109f-347c-8951-8a2f4dbdc619 | -9.9178 | -43.7447 | 2025-10-02 11:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| db2bb972-ad0f-34c9-bb48-bad315943322 | -14.3704 | -45.9634 | 2025-10-02 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 234.4 |
| bf325d5c-046a-3b2b-8270-0889d55f5e3b | -14.4255 | -46.115 | 2025-10-02 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 71d65999-83cd-3802-b8d0-99cfb560a6ff | -9.08 | -46.7215 | 2025-10-02 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ea9dcb63-9577-387e-8393-ddca2b6d9e13 | -14.927 | -47.2387 | 2025-10-02 11:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| cc89105a-329d-3404-a637-a8877509e52e | -13.0119 | -45.1988 | 2025-10-02 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 24e0733d-cbe7-336c-9609-c03acc7d0c0c | -14.2924 | -45.977 | 2025-10-02 11:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 31eeceac-24d6-3ae7-b647-8fd03440cffe | -9.9369 | -43.7422 | 2025-10-02 11:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| df8f5cbd-3a23-32ad-9e8f-765cc48a94db | -11.2799 | -47.8445 | 2025-10-02 11:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5a722168-0acb-305f-aa25-a4ec8aa4ca78 | -11.0897 | -47.846 | 2025-10-02 11:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9a7913ef-37f0-3cab-b2bc-127dc5886880 | -14.3709 | -45.9403 | 2025-10-02 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 3e6b059a-1125-3c04-8702-e60c11eeff4b | -14.2924 | -45.977 | 2025-10-02 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1eb6a604-91c5-31fa-8311-a96bade4f9bc | -13.1542 | -47.8568 | 2025-10-02 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| a0ff1d78-a774-345e-9fc5-b9216d4cb14a | -8.6911 | -47.6906 | 2025-10-02 11:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| bae68118-ff15-3ec2-965e-66d1a22ccd3e | -14.4947 | -48.4329 | 2025-10-02 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 87ef9f6c-aae8-3149-8d6a-3694037fc242 | -14.1921 | -46.1321 | 2025-10-02 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 787db8fc-de40-3ff4-91c7-201bd1fc5f95 | -14.2116 | -46.1288 | 2025-10-02 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 38b0bcf5-44d0-31f6-8cf0-b192ea4115a2 | -9.08 | -46.7215 | 2025-10-02 11:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 455e220c-4200-339c-9d27-edd5efd057b7 | -9.4086 | -47.5521 | 2025-10-02 11:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| fd66a3a9-8606-3e7c-8780-5c29c56dab23 | -11.8234 | -45.0364 | 2025-10-02 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 67f12511-38ea-3ae7-8880-366aead861ff | -11.8238 | -45.0132 | 2025-10-02 11:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| cce31464-8b3f-3a66-b0ac-9539cbd293a0 | -14.9275 | -47.2159 | 2025-10-02 11:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 35873973-78d6-38e0-bd44-998f50b09558 | -13.0119 | -45.1988 | 2025-10-02 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| e1d45e4f-66b3-3d13-815c-fbd91d5f03b4 | -14.4757 | -48.4137 | 2025-10-02 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 38954773-5874-3823-98b2-485637847247 | -14.1917 | -46.1552 | 2025-10-02 11:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 917c1253-6430-3aba-aa35-4610d352021a | -14.3704 | -45.9634 | 2025-10-02 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 181.6 |
| a412e01f-2484-36cf-b682-e8bf857f9757 | -14.425 | -46.1381 | 2025-10-02 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1b5e13cd-8acd-3ec3-8d0b-0229518943af | -14.9074 | -47.242 | 2025-10-02 11:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 1380412e-4219-32d9-acf7-10aaf4805622 | -9.9178 | -43.7447 | 2025-10-02 11:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| cacd35ba-f428-3053-997f-02cb92fa6d3f | -9.4083 | -47.5742 | 2025-10-02 11:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 570d4646-f7f0-33c1-b471-a5aa429cefb8 | -7.8882 | -47.281 | 2025-10-02 11:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9397c2e6-bf68-3d9d-ac5f-3755f22babbc | -14.927 | -47.2387 | 2025-10-02 11:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 278.8 |
| 50e7d72d-aaab-3397-8925-604d43677049 | -13.0114 | -45.222 | 2025-10-02 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |


[Clique aqui para ver as próximas entradas](README144.md)
