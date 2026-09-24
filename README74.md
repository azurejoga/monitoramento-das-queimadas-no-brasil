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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fac22c62-aba8-3050-9280-9d199db6c6a1 | -5.83961 | -53.85502 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdc8cfff-9d25-3965-a48e-7d69a5603621 | -7.97448 | -45.22571 | 2026-09-24 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2235e17c-2cef-38ef-b18e-417e32880fea | -1.62781 | -54.9145 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d8dd7d9-8f41-394e-9c06-5d40f4ca6d31 | -6.67947 | -55.04969 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93ced003-d5b1-3b7f-8b0e-8c194f36bb95 | -6.88048 | -59.85798 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b7f3ae7-368a-3739-8674-7c3d8c31ce09 | -2.64587 | -54.68945 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3d3350fb-73aa-3795-9e64-df3b08d32262 | -3.07533 | -54.38355 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fe04976-5b20-3bb3-a25f-56ede0e9f1ec | -8.26575 | -54.7737 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0081f065-c37a-32b2-a744-c82cc171e7a0 | -6.46658 | -59.96241 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3235f04d-372c-3b8d-94a8-ca3019bbf7fd | -1.8322 | -55.7185 | 2026-09-24 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e7399848-c468-3efc-9d93-9422992dca50 | -1.33122 | -54.66521 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89d36906-52de-31bc-8ba7-232e895470c1 | -4.56678 | -54.93808 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aefaf769-7a28-3f9f-85f8-6b355bccd4ee | -1.2789 | -57.03642 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e52da3cb-14fc-3f43-9a35-6d2a87997161 | -3.15799 | -57.69015 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ecc8900-c873-3b5d-9028-94b4c046dcff | -6.91742 | -59.91407 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44d73d0c-55d8-3fc5-bcf0-5a2fce007299 | -5.32956 | -48.98745 | 2026-09-24 05:04:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cc2784c4-0b72-35d6-a7ed-afbcfd312fc1 | -6.07242 | -57.80287 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8889b9ba-fc14-3b30-ae1b-cb7f5bba9345 | -1.21504 | -54.54884 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac879860-891b-3d32-8667-1aed522260a8 | -3.2337 | -54.32692 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 256f53a6-c562-3f45-a776-125e687dd0eb | -3.96445 | -49.68739 | 2026-09-24 05:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71a58376-c980-3c8a-aabb-907df981f26a | -4.33554 | -55.21731 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb5c93f2-c2b3-3161-8f5f-0282c3435f6c | -6.44516 | -59.96241 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e3e53ce2-d329-34b5-85f9-857238c21701 | -1.2184 | -54.54936 | 2026-09-24 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd5d2b00-1ca6-31e0-8ae0-43d212070766 | -6.72536 | -50.94902 | 2026-09-24 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 759b0b86-e82f-3784-85dd-a7d94267c127 | -5.79806 | -57.53404 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78b1945a-9435-314d-9d94-85032372f87c | -1.92064 | -58.26505 | 2026-09-24 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6a9c315-fd42-3621-be49-a4b813729798 | -3.80517 | -55.66109 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee5d51eb-16bb-3a9b-8d58-86b87ff9d556 | -9.23515 | -47.37682 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d09267b-6610-3e99-86c6-14febffec043 | -5.87787 | -51.93866 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cc52170-43bc-39ef-83d7-8a5e0b24ef98 | -7.51397 | -61.48885 | 2026-09-24 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ceaf347-1919-3e57-84fc-8579f5473d7b | -2.97295 | -54.15124 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bc43ba5-ff90-361c-a657-75103401f15f | -6.72106 | -44.15873 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 711baea2-2d2d-340c-80ea-d824fcaf7edc | -6.62102 | -59.91837 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afe6bb02-b10c-34b1-8c73-bf7f9756a24c | -6.71326 | -59.00491 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afdddadb-d3a2-3737-9cb4-b3cb75f57d6b | -3.71918 | -54.20146 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ac64b50-b6df-3b77-94fb-d59b638625da | -6.44034 | -59.96553 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2c8daba6-c255-32ab-8bd0-66b5553d18cb | -8.38525 | -46.29164 | 2026-09-24 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 61a8d520-e680-31ab-9273-235a7fa904ee | -3.70262 | -54.19888 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c366713-a982-3836-bd65-768ce341f929 | -6.20083 | -47.50013 | 2026-09-24 05:04:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d90b5ea-16ef-3be7-aeaf-76263384b9e0 | -2.79872 | -51.36619 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60be6c3f-6c48-3b0d-b76a-2b63211b5cd1 | -5.25587 | -49.22918 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf7bb34b-b8e1-3ece-91ac-fb248330ef03 | -6.44408 | -57.77559 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 866aefd8-714e-3376-ae00-aef14bd08479 | -3.71061 | -58.85471 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 947ad990-d46c-3fa1-b1b4-1bdad0d11264 | -5.8594 | -60.16385 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 347f0939-6abe-35f8-8142-e4adf986bbdc | -3.88287 | -57.17062 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2686a336-b759-30b2-b820-dc5990da6aff | -2.82362 | -46.70905 | 2026-09-24 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c39806fc-46eb-373f-af9c-9515b068f4ca | -5.72192 | -49.83233 | 2026-09-24 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b33c0ef-430e-319f-9aea-1986a3084317 | -8.38483 | -46.2947 | 2026-09-24 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 615c34a8-34c4-3dfd-87eb-a34ab63511ca | -6.46693 | -54.99764 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dd9e681-03f6-3866-a355-2f79c412417a | -7.43663 | -49.8314 | 2026-09-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 440152df-e70f-31c2-a754-162e6ef7240e | -6.31399 | -57.74698 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b8dd050-a629-37cf-8d6d-72635522fe1e | -8.08633 | -54.76966 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8de2fdc1-5b07-3e47-91ef-34e3216068ee | -6.60955 | -59.93594 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e4d74496-20aa-3259-b13b-ed9c9efa77cf | -3.2128 | -53.40879 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ff7be99-cc73-3b63-80fd-bdf5af435ad6 | -6.57518 | -51.49022 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c46e530f-c4fd-35f0-a53d-0bbf38b4a7d4 | -6.05094 | -53.28728 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02ddcb98-5d08-30cf-818b-9eb5219a2138 | -3.90449 | -60.59564 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbbcd7e0-9212-33a2-9ecd-30c0f09b576a | -5.57788 | -42.73784 | 2026-09-24 05:04:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a1172e8f-98d9-3fe5-937a-c459d282c2d9 | -6.94888 | -59.82809 | 2026-09-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48cc5859-967e-360d-999a-d608a1854072 | -3.21335 | -53.40535 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87be6d60-8ee6-3600-be94-168162578d69 | -9.03995 | -66.05604 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06f0b964-6708-3dfc-9906-f41f7cd6944e | -10.10526 | -50.19256 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c2cf350-0e33-31e1-8da7-50e1f8bfab82 | -9.86884 | -48.31895 | 2026-09-24 05:06:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f451e963-e858-3573-848a-27a73d48d2cc | -9.13039 | -57.54763 | 2026-09-24 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e658a381-1a71-373b-8b30-756bd2b12fc2 | -12.41522 | -46.96009 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6eb38cd-d165-34df-a71a-4ad308762bef | -11.52319 | -58.65928 | 2026-09-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98a91d61-f191-3865-afaa-9f0a04ac38e9 | -10.4095 | -49.35607 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| badc4f41-97e4-3e28-b2fa-43e16aa6a174 | -11.39087 | -47.37796 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fbdbb2e-53c8-3b31-b7e8-57120d8876b6 | -9.75126 | -64.30418 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f131cb82-d57f-3333-8696-61f27aab6f14 | -10.90769 | -53.93531 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4042b21-40c8-3fd9-844a-26ce7dcc84cb | -11.39252 | -47.36488 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22f996c4-93b6-3241-82f0-f4564cce9113 | -11.00702 | -49.70776 | 2026-09-24 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00b499d2-1730-3362-8950-8290f8f2f4df | -10.56107 | -46.70839 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45114133-6a11-378f-a1c7-2dd3f55a7194 | -9.96319 | -50.25807 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb2be3b7-0999-3c8b-8c64-b7bad20cad14 | -9.85768 | -48.51029 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6644282f-9629-33a9-8466-cba7d33734d5 | -12.13599 | -50.74706 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 55226836-6bb4-391a-80e3-3d57552f31fc | -9.47793 | -56.76289 | 2026-09-24 05:06:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9c418cf-bfd1-32ab-a9a8-43a806f1e0f9 | -12.13644 | -47.36354 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d48e1b2-17e1-312b-a658-50d645cb787c | -12.152 | -50.74938 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef3aff7-3d57-3039-9aa0-a71e1ac3d92d | -10.43118 | -46.27176 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bccb5322-1d7b-3e2a-b8f9-de0ffd048ea5 | -10.91051 | -53.93951 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe988e9b-ef44-3d33-94a2-27d5a4b4846b | -11.39864 | -47.39624 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 285280b0-f216-3633-90b4-6e4f0bcd9dbb | -8.49694 | -57.60592 | 2026-09-24 05:06:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cafd77f9-d9f2-30ac-ba59-78251edce2a5 | -9.55796 | -65.98471 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9538b858-f9a3-3ac4-9899-cc5ac254228d | -11.6503 | -43.48912 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 859ce08b-39bd-3bb8-8882-005a5a559dff | -12.14096 | -50.74059 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e49a2f2a-2b46-36ba-b018-7f45067f99ec | -9.75063 | -64.30758 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77728497-e1e0-3ed0-a3c5-86490ad77155 | -14.63324 | -50.59664 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e74303e2-5e2c-3fd3-988b-0b3c87ddb935 | -11.91401 | -50.73355 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fb0b2ecf-9658-3cc4-9b6d-0b20f763359c | -9.84993 | -48.49985 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e024917e-e849-35a3-9b33-aeec0eeab1e3 | -11.65709 | -43.49675 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 40bbde5c-1c43-34fc-ad73-45f8c32670a1 | -13.17616 | -51.53855 | 2026-09-24 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4345326b-a0ab-3739-9887-88fe9e0608e7 | -10.73855 | -46.28796 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdd65e9a-e4e8-3245-986d-d2ce611ed6fd | -12.15705 | -50.77165 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9026c48c-0cc0-348e-8091-edbb60cc034e | -11.12437 | -48.3306 | 2026-09-24 05:06:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fbe655f-e3e0-3cd0-b91c-1b8d4106300f | -13.78479 | -54.06785 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22dcfaf1-d229-35d0-bd50-2826f4e7f5b8 | -13.79879 | -54.06509 | 2026-09-24 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2538bc44-a41b-3e16-b594-fa09f61604c1 | -12.70758 | -47.00451 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46009059-b853-3e54-9a58-27ac2766ba72 | -12.11108 | -50.73685 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| feb22f10-836a-3697-85d9-79ea1adfb4e8 | -12.42041 | -46.96079 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README75.md)
