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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e79232a0-3130-32c6-8ebf-7d640d95dc7c | -12.69765 | -48.19677 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3f76f44d-8d36-3bad-8879-ff399c0a9391 | -11.58217 | -46.26621 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65415e65-3a7d-3bdc-866c-dce74e65c5a7 | -9.12129 | -65.76434 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94df5bf1-5136-327b-b6da-e7b3129c7054 | -9.11836 | -65.78401 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9295a5a-241b-3f87-989a-f787c2361743 | -9.41519 | -60.57142 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72275507-8284-31da-ad7f-e2dff3981b25 | -9.12593 | -65.80353 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 837b19f2-5ea4-3bcb-bfe5-d5c1200bf188 | -9.80501 | -61.20163 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cbdeae8-23bb-3002-a084-d6c2369353a4 | -13.52726 | -46.94683 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2b7dda9-eb69-339f-9fd5-8f8d3f1dc49c | -9.15446 | -59.57481 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 341d0006-6f21-3254-815e-b6275418dc23 | -13.19567 | -45.2872 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 430cc9a9-b5b3-3677-a33c-4da443ed1ef6 | -12.91366 | -48.12523 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 61c7f259-c1fd-3506-8ae0-5f92a5fd7d8b | -11.26081 | -45.49887 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e99db393-64c1-3fc0-8719-ec93600be65a | -12.66668 | -48.18849 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d16ce658-0973-37b8-97b8-53e4db1d035d | -11.87721 | -46.40181 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d345e542-b569-3729-9ae5-9aacc5dd2c89 | -10.36922 | -57.82207 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 746732da-6b40-3784-8158-61952f0a4e2d | -10.02266 | -51.11293 | 2025-08-29 05:08:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e612ce8-7983-3a76-8f0f-129205bbaac3 | -12.83855 | -48.16959 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3838214b-338c-3985-8a10-74a5d5d81363 | -12.0668 | -46.62727 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97916ec8-e29e-3489-af74-4b977c82df20 | -16.28522 | -53.62064 | 2025-08-29 05:08:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7eaba252-090c-3877-846f-e2848f8e752a | -10.84555 | -47.49838 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 567187db-ba13-39ca-8571-a7f78fd2066e | -9.67686 | -48.33236 | 2025-08-29 05:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b822b0f-ebf1-353a-a51c-e2788dc21264 | -13.45508 | -46.96277 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 424b32ed-6935-33e6-8e1f-e9c802d7f972 | -12.70255 | -48.20022 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8d810324-9f98-35e2-8371-f4d0e282ba5a | -9.11466 | -65.77008 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c0779866-9a52-36c6-b447-f985782f75cf | -9.76639 | -64.25615 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| edfacc51-307a-3824-ae99-03e44a6d4ada | -13.39736 | -46.99599 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f36f8fd6-643e-3414-8654-0db8404d854d | -8.18956 | -61.37957 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fe95b96-1960-341c-9ae9-70018890322b | -9.12181 | -65.79555 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec7bb886-5a62-3313-95a0-4c7c39f88ccf | -12.42992 | -63.92096 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 25285038-5284-38c2-a605-c2c5337d1d92 | -14.33164 | -53.30119 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea2c8654-fd86-3ec1-9adf-fc3eed313420 | -12.90106 | -48.14022 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9b496dc-d0f3-3a75-8ec6-7357b5001703 | -10.46653 | -57.93455 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1e577b8a-c9a7-30c8-bf7c-bd39013e0ee1 | -11.61269 | -46.20021 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aaf03c9c-96fb-3af2-b138-0b7d39c58e06 | -12.99216 | -56.92298 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c3c32b8-bd22-3c71-ad7b-158ff36c938c | -11.56247 | -46.37662 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f7d1f7d-e629-3965-b54c-fb0f60396ecf | -13.60443 | -48.15744 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d3cea0b-98a1-3459-8218-0a15ef6eb458 | -11.32018 | -55.21865 | 2025-08-29 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea322ade-3845-3770-b8b5-642a68bdb9f9 | -9.77801 | -64.24724 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 81267889-a7d9-3bb4-9e32-172fc45611a9 | -9.78866 | -64.24365 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93b5d4df-ecab-3c08-96ed-2c81d6ed1562 | -10.45055 | -57.96918 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0b05880-95ff-3c2e-9e00-e90cbc10f7a9 | -13.02977 | -56.91418 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f8d2ac5-15f8-37c3-87e3-b2f8c85f80e0 | -14.78074 | -59.73565 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a97686aa-1f0b-3be7-9a55-02e547a29016 | -13.53567 | -46.87531 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cde6e97f-93a2-3d1a-89f2-e9802cea7679 | -13.35264 | -54.3913 | 2025-08-29 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caf6e724-f2b0-317a-b389-647fc81c7c9a | -12.3994 | -46.49586 | 2025-08-29 05:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d16c0be-1073-311a-9bf5-1715c291e24b | -9.24548 | -59.7918 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce800dcf-1831-3f02-9aeb-690913311391 | -11.03297 | -45.06636 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7303ac79-9c2c-3728-a46c-4d1b04285d4e | -10.4732 | -57.96114 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad392425-0107-3630-8456-4d7401546ca9 | -13.17928 | -45.28074 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4acabed4-5311-3bbe-bb15-4fc513668ffe | -10.36527 | -57.82513 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cef026b0-2991-3e8a-9057-919fdc6d1ee2 | -12.09186 | -44.72121 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6563101f-f6b9-3432-8046-ccf94b5559f1 | -9.31305 | -57.69868 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f942dfb0-d249-38d4-86e8-deefa57faecb | -11.58615 | -46.3766 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69dcd91e-4eff-3450-aaba-b04b35c9d6bc | -14.78622 | -59.72414 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e55b5b93-cc72-34ac-82c2-994c4cc41246 | -11.35465 | -43.56591 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efe80c56-586f-3491-b8fb-0cb1259f1cb5 | -10.47397 | -57.93519 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d828b3ea-8fcc-38f2-bf8b-9f9d933b6d70 | -15.04604 | -48.13371 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d7ed0a-acc8-3d24-85aa-6fa9cc4a1f79 | -13.56655 | -46.91033 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8ef15ab-aaf9-3fc8-a8b0-d3a175886ff1 | -12.83376 | -48.16874 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 724b7bbc-a7ce-3be0-b64c-a7d84ea5f190 | -13.41255 | -46.96658 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 620d18b0-ed94-3b45-93b8-fd5bd97c42d7 | -10.47119 | -57.93101 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7736cbe-282b-36be-bba4-5824cbb947b2 | -12.84655 | -48.10269 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a8aa277-9799-35bc-a742-126f7eda2ab8 | -13.53598 | -46.86985 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ce5a59dc-2de2-3eee-bcba-3cbf45301997 | -9.64945 | -64.95607 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed44933e-317f-385c-b5a6-fd330bef81b7 | -8.69296 | -62.47096 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ad73d41-735b-3b08-80f0-e270e527c83a | -12.91171 | -48.14089 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ee39603-ff30-36aa-98a6-faf8f8743056 | -17.0498 | -45.88365 | 2025-08-29 05:08:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bce3cbc-4afb-3808-9990-980524407cf5 | -10.32413 | -62.61875 | 2025-08-29 05:08:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 679f0e4a-a0bf-3f91-879f-0f5d966af8bf | -13.53476 | -46.88063 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ebeb95b0-34bb-31a4-be31-9309cac46cfa | -9.52306 | -60.52918 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b81d09ad-ba77-3e7d-a408-0b2d3d692753 | -13.41596 | -46.98661 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b59c6473-7e3f-3862-8fc5-cc65823ad4d0 | -9.11404 | -65.77351 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4e48fcdc-0d03-3d7e-b1b0-b8b963c4279b | -9.54156 | -65.69511 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62334d59-0f84-3795-9a54-401e4b36f6fa | -10.31483 | -62.62123 | 2025-08-29 05:08:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30701f9a-db8e-3804-8729-7ca690e1fcf0 | -8.24529 | -61.44981 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 592c80df-f7f7-3ca7-9a54-2a3b93918f84 | -9.47414 | -62.38132 | 2025-08-29 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00a8b60c-1f85-3410-ab65-03bcb4b88e21 | -15.19408 | -52.33436 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e3ac157-f2c6-35fc-9f96-f45d47cee3b0 | -13.4057 | -46.98676 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5ad51a9-8812-373e-9195-e0959a7b239b | -12.83375 | -48.16491 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6879829-05df-31e1-909d-9497c067349c | -9.16749 | -59.56403 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a132528-5351-3634-8129-3d1605922dd2 | -15.63301 | -56.31328 | 2025-08-29 05:08:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4cfef46-23bb-3dea-9f49-e792baf2d51b | -9.46061 | -60.30526 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1935d7d-bb25-35a3-b77a-c229fe3f7afd | -8.18892 | -61.38325 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 902f5417-477c-31a9-b232-452c5fecabf6 | -9.13063 | -65.28989 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0874cd4f-9602-322c-ba3d-fe4d56d0c288 | -13.18293 | -45.28568 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4753474e-8c56-34be-a645-9a2f64d83056 | -11.06242 | -44.76274 | 2025-08-29 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95d5a60e-1576-3b9f-a016-16be43d71f92 | -9.66685 | -65.03458 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b92cf499-0a7e-317d-a3ef-4e4bff5920ad | -9.6674 | -65.03153 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4274808f-4c56-33d6-94de-ff03fb351f27 | -14.59979 | -54.50893 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f9520c2-0d60-3b18-9653-9acd0cd085d5 | -13.41719 | -46.97644 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8d40507e-ce06-36b9-97dd-742a2b6e5abd | -9.47114 | -60.31178 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43e6f849-7574-34aa-b12e-ef0080affde0 | -9.15655 | -60.93435 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0d0ebdb2-f4d4-325a-acad-83fabd5e4dbf | -13.4036 | -46.84596 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa08765f-f594-3a93-9678-4abe8aab5b8a | -8.12738 | -61.21142 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c494d788-cb08-3073-bb73-113b7f94c068 | -15.04098 | -48.12982 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2aacbfd3-7d48-3892-b329-038eb28fd7c5 | -9.18272 | -65.80002 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfaa195a-c09e-3a67-a4d9-07c58ae02128 | -13.5415 | -46.87564 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b3366e15-63c3-390c-9f95-d8ddc5117e29 | -11.55084 | -46.37495 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4e1be80-3854-3059-bb15-40546cf2f75c | -15.174 | -52.32791 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad5de749-74e2-39f3-82d2-67ef398f1d64 | -11.56829 | -47.61948 | 2025-08-29 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README67.md)
