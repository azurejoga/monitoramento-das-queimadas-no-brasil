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
| 70feeaef-c439-3788-95a1-d3a677a9f5cc | -12.91663 | -56.93089 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9b1e588-29ff-3ae4-8907-a28f07b33aa7 | -11.85407 | -51.42138 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa6fb692-78c5-3d8e-82af-2b62ec5900eb | -18.06498 | -45.98827 | 2025-09-03 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8336aaf0-314d-3415-b4ae-93c80e7fbfc2 | -15.9957 | -49.14835 | 2025-09-03 04:49:00 | NOAA-21 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82a60a6a-106d-328b-a8d1-4b216ab2ac7c | -12.48617 | -48.04861 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adf4e04c-822a-3053-a2ce-cc2d1a755f4c | -11.66465 | -57.35698 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5e97770-f5fc-3887-8958-c1682ff42075 | -12.91935 | -56.9992 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae47a9ca-4425-3e22-b160-389ae4117494 | -17.62215 | -46.70782 | 2025-09-03 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 938c2561-3bd3-3a16-a13d-ee620ad7985e | -15.60649 | -52.67994 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d4c123c-3963-3427-be34-4e21a8b79b81 | -12.84497 | -48.05661 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a478b60-446f-3cdb-b480-1f4ea2b393cf | -17.36626 | -49.17677 | 2025-09-03 04:49:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afd99aa7-8a5e-33a3-90a3-d63738a79a14 | -13.49078 | -46.82319 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6967071-f2cc-30d2-8f05-95966fb19c46 | -12.93081 | -57.00122 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a67ae2-184f-3a23-ac10-d361d6a949c5 | -17.95266 | -47.23957 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b808d76c-2208-3a09-91b6-46a6586bed72 | -14.47992 | -48.45371 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f9fee11-4605-3a0b-a41b-f5baf59c7dab | -15.08382 | -51.34894 | 2025-09-03 04:49:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 089e6123-e708-3ea2-a445-38163b1661b3 | -13.28259 | -46.83206 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d470beec-74f4-36c5-8d0e-2ac46d18aa73 | -15.55056 | -48.36606 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f6acdffc-0ce2-3bc2-9aa5-addc2865c7e7 | -12.92403 | -56.99503 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 050f5966-f353-36a3-b610-320ed3fdf6da | -12.9776 | -54.77504 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ee46855-e483-3bff-bbf8-6b66be6a9da5 | -14.40304 | -51.70476 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae72d5c9-0067-3d6b-8a6e-e279f102ca97 | -14.54981 | -51.94466 | 2025-09-03 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0019393d-7c9f-314b-a758-38251c3c9874 | -16.37957 | -45.24454 | 2025-09-03 04:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9900b24d-c788-3bbc-9b90-20363a9cc345 | -12.48886 | -53.83242 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dd388d4-fb9c-3b45-b9b0-49eaaa7e953f | -15.0233 | -50.04268 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9648931d-85c3-318b-8ca0-19531ffc03b3 | -14.05991 | -44.56926 | 2025-09-03 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b640581c-5445-3529-bc48-a8e350188345 | -12.92888 | -56.99744 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7adf9dc-ebd9-3897-acfd-9ab548ae4360 | -12.92257 | -57.01143 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 827d9d7a-9ef2-306b-a876-55775cf15011 | -12.49497 | -53.83715 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea1a74fc-3fbf-337a-91cb-b33e990f142a | -12.88406 | -48.03342 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbe3c45c-f259-309f-a04c-cb6ecc800c1d | -15.55718 | -48.38651 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61e843e8-1e4b-397c-921f-f1bb0bba6fe2 | -17.53539 | -47.57724 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5a5b68c-4f1b-3bd6-9298-6909858bd346 | -11.96115 | -51.34243 | 2025-09-03 04:49:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1245efd8-1b8f-3604-ba22-6b28b0878891 | -13.73436 | -46.93439 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ed676a78-102a-3f84-a120-a74cb98063cd | -12.93048 | -48.07677 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07c6e4bc-fe4a-3fde-8c09-17b7a68e64cc | -11.86502 | -51.5472 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b2aaa08-be29-3404-8da8-2778ccc02ffe | -12.84357 | -48.06676 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a76897cd-ee60-3ad6-a86d-f308cb076c18 | -18.06374 | -45.99902 | 2025-09-03 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 7c2929ec-3b5a-3430-a672-064bd0511e15 | -12.63551 | -57.00053 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b8288c6f-d5b6-3d93-a24f-607703c622c2 | -14.05955 | -44.57224 | 2025-09-03 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1291404-70ba-3bf7-b8e5-52b14b9330e0 | -14.56344 | -53.04983 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60ef38b9-6549-3d3b-a373-953835f8484c | -12.6043 | -48.20475 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e667ae2-a323-3f8f-925c-bd79a3049790 | -14.51946 | -53.15486 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba813242-a15a-38fd-8f84-89408774faf1 | -15.03049 | -50.04372 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c82fd34f-df2a-3dd9-a798-b0eca20b3c4c | -13.08908 | -57.12667 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f2f20c73-3cf3-39b5-8fa1-4564d0eeb790 | -12.93634 | -56.94755 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11eaad06-fc2b-3071-acd4-6aa08fba135b | -15.02454 | -50.05995 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f9492ba-33d8-3662-9a35-33da5071b677 | -16.30437 | -52.95977 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aad1ea6-8f71-36e0-9d71-f48199da9f64 | -14.55933 | -49.14637 | 2025-09-03 04:49:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20fa9e01-6bae-3c4d-ab12-5ffc89b703ae | -12.87239 | -48.03135 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 03fd259c-70af-38df-8957-609679f51046 | -11.86093 | -51.48443 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4885573d-4366-3546-9949-50cf8f80b907 | -16.3005 | -52.9628 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45959001-fccf-3e12-8524-d13000d26c55 | -11.87595 | -52.42235 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67224579-4a66-351d-8231-aa494c1879e4 | -17.9455 | -47.225 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83044f35-b6c9-3a74-8c42-44d2579834d1 | -12.29966 | -50.0053 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60f93180-95d2-3340-abe1-c0753ad75b86 | -13.00585 | -48.10693 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe1369ad-5665-3896-bf7b-9c93140985a0 | -15.24801 | -53.79897 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83b11f61-ded4-392b-8de7-cf1ceb8a2404 | -12.92722 | -57.00721 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 21d87a43-94f9-33a8-a224-84033a103cb0 | -12.94355 | -56.97356 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 840b4544-74fe-3ca3-b5b0-cf1f2bf011f4 | -12.444 | -48.71314 | 2025-09-03 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d70133c-cb71-30a8-ac86-a9b311a5135a | -15.01076 | -50.05375 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7618b20a-26af-3701-897e-397f0b1b9445 | -12.91202 | -56.93496 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1117971-1f49-3d6d-b6d9-101f57ebef77 | -11.67321 | -57.35493 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 56136a14-3c31-3901-b028-ce34fc4b5ceb | -18.39247 | -49.2188 | 2025-09-03 04:49:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30e52041-449c-3d15-9230-59117fd85322 | -12.9823 | -54.76801 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ca8016b-ed67-3979-87b6-66d1519f4d82 | -12.85746 | -48.02404 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b695682-c139-39ae-a268-55f664b78272 | -12.91959 | -57.0058 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65e16d6d-fc5e-380c-8b77-c730fba99fd7 | -13.69635 | -46.96142 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a200044-d2a9-31be-8b90-2c966f68a562 | -13.73535 | -46.92684 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 661d555a-4535-34c5-8be1-deeb7193aa43 | -12.9112 | -56.93975 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 28b43df9-bcfe-3b67-89fc-4a062bac4303 | -15.90298 | -48.16493 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ab334823-8750-3536-99a3-07255967c553 | -13.21028 | -51.81829 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45a831e4-cb5d-32e7-8d50-7d69317bb3f8 | -15.55768 | -48.40456 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 844a2ee9-9006-3062-9421-a9efabd87e6e | -12.90657 | -56.9439 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e18aa31b-b670-38f1-b952-2f104af65e9b | -14.60308 | -48.0766 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 700a2107-8caa-3b82-8e61-9a9cddb7615b | -16.54292 | -55.07412 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7000b190-cb38-3c95-8a86-95d5036d4444 | -15.7381 | -53.69027 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19348d66-cca0-3243-bbce-110fab2cac3d | -17.29623 | -47.70146 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec2a510b-6d76-3b75-8bfe-e8db6a8cfb58 | -13.51078 | -47.02937 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c523df5-f9ce-375b-a3ce-d29158142016 | -14.98183 | -50.21231 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bd2eb72-5c4c-3429-a61d-573bd1d6f551 | -13.31148 | -51.77881 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb46dcb8-7f23-33a2-b22b-bc10fddbf96d | -11.66237 | -57.35649 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1fac5c5-c01a-3387-8248-4a6dd863627a | -12.97398 | -48.10727 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4faec3b0-75bd-3ecf-9c01-f537a3948356 | -13.45547 | -46.92507 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20e487c3-f85a-3d5e-b2b5-e138814fc55b | -14.96179 | -50.07336 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f135a21-b185-3c4c-95d2-23770bbf8710 | -12.92232 | -57.00469 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f65f6f1c-46bc-3a4b-9202-b696c6409cc2 | -16.29719 | -52.96224 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cefc8dcd-79b3-3dd5-a6ab-b27edbf5efd1 | -15.70744 | -47.66523 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 452c54af-e964-37d8-aca3-2ad43dc2e5b7 | -14.79209 | -47.5073 | 2025-09-03 04:49:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e20eb00-11da-3c2c-b3a0-e7367313c4eb | -15.72284 | -53.63642 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f73dfb3-04d6-34ba-abca-11156580def0 | -14.76948 | -48.14269 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12d9c66d-80d6-3733-aff9-2ec782a6d187 | -13.01072 | -48.10493 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0354632-86ba-3df7-a183-112d79804b93 | -15.0 | -50.05212 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e612d1fc-578a-3ed9-9892-9328f9bc2031 | -14.0632 | -54.01636 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bb094cd-4f72-3db8-97c6-b5df1d70f5d7 | -15.00425 | -50.05816 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bdd7790-3958-325f-9137-fdb40d07f66e | -13.31261 | -51.79374 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21a75b02-8c78-3a26-9140-236f7fe0c235 | -12.9185 | -57.00401 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac37c9b3-c2bf-3200-8a1b-7a3c3e3a46df | -13.70078 | -46.96015 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f804cb92-808b-3e40-96fa-2adefbe17cab | -14.35261 | -52.80803 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d179889-9902-337d-abfb-d1ab859babf1 | -13.27838 | -46.83118 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README70.md)
