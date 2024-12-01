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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9376906e-0267-3b03-b0de-8fb3edffa4b9 | -3.59315 | -50.37928 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd9bb84c-382e-3fb6-9911-b72838c1efba | -3.4699 | -53.87965 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3cdf1de-4399-38ed-a6be-ce5188364f96 | -3.99644 | -46.65084 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2132b99f-0191-3b1f-b53a-962eb640bea7 | -0.20119 | -51.40387 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b840b689-a302-380f-932f-2bb8096a05c4 | -1.26066 | -47.5074 | 2024-12-01 04:44:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c5864e-0761-3725-906e-d6b0b7ff1936 | -2.7258 | -52.97467 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 59552824-35c8-3cd7-a0a7-e7ee4ccda5cb | -2.28969 | -45.60201 | 2024-12-01 04:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f60712e0-152c-3f79-a662-9fd7c21dacfc | -1.10139 | -53.60335 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ed785e3-8fb0-3e21-8796-904912e9df35 | -3.08903 | -51.40633 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d954ff5e-1f68-31a8-b6d8-bbb346f98e77 | -3.11094 | -53.81001 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66698a9a-fcf7-3555-b3f5-e43d53828fa7 | -3.06944 | -53.80801 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da92bd60-15af-39ae-956e-36ff94886d82 | -3.58815 | -50.36789 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35570068-844a-3638-ba98-76cc520d8cc4 | -2.57362 | -51.88397 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b07d0b2a-19dd-37b2-bc2d-104c4991fc3a | -2.92959 | -51.44727 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3ec6211-3e35-37f8-b3e1-3030f376a962 | -3.10844 | -54.04126 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 676e6317-b4e4-3aed-b72c-0c96192b8f4c | -4.55102 | -45.72041 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5877fc21-6f61-3f61-8d05-c2187ea576fa | -3.09441 | -54.29465 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ba01974-d3a9-3f90-8589-360ba83506df | -1.40492 | -54.09299 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad67d0d1-990d-39bd-b3d2-9fa69645b8fe | -2.68905 | -51.72975 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71c89576-9ba3-354b-bd8e-8b31bde7de7d | -1.19454 | -51.75243 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5caaabd-2acd-3639-b865-1bb8f5fa1c7f | -3.02581 | -53.41232 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a913612-0572-3529-bba1-16761a2d6417 | -1.96918 | -51.95044 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fec19e0-5984-3bff-824c-1a07d6bf297a | -4.09434 | -46.13344 | 2024-12-01 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f7950c6-95e3-3796-a964-3e2997d48a78 | -4.00175 | -54.61416 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeceb6f5-0320-3c05-beaa-3446e9a409ac | -1.16656 | -53.77516 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 748afe3f-b518-3851-b8d5-06a9fa0608dc | -3.11699 | -53.98741 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86764187-1302-314e-9c92-92d282a7d321 | -4.20589 | -50.69446 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b998d07e-51d3-3943-b91d-0e09973cb9d9 | -3.21676 | -54.08955 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 839a85bf-1e7f-3c2d-92ce-995fdd659377 | -3.30066 | -53.69395 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c03e6687-9264-3a28-a6c6-a354ad66b31c | -1.67791 | -52.5088 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bbe3a7d-b7ec-3af8-b242-832408963056 | -3.38344 | -50.33549 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0bab32b-17bf-3485-abe7-d965c5fce522 | -2.46976 | -46.56473 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11d54d28-18b8-342e-b2de-3a237f6376e5 | -3.33744 | -53.37384 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27370563-17b8-3a44-83f8-1e1d6d605d5e | -3.73308 | -51.31152 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2494ede6-2d0d-390d-a49c-1afcfe011ab8 | -1.64278 | -52.75196 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ad5f15c-c3d9-34ce-bb33-184d2cddf4f6 | -4.47202 | -50.76846 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1e50bc9-92ea-3890-97ee-e7d630bbf81d | -1.01292 | -51.72449 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57ee8507-3c8e-378a-b09c-4452fc9764b8 | -3.74599 | -52.26104 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 859eb883-42ad-3918-ade0-32352d4540e6 | -2.72517 | -52.97864 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df8b2524-f15c-392b-99d8-fac3e839a9a4 | -3.24333 | -50.14751 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a42b0b91-da61-35b9-8664-a8973b332393 | -2.84756 | -54.03109 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3c6dcc7-728d-395f-97a6-d02d39850fc0 | -2.59305 | -46.94187 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b706fbf-8d4a-384b-89d2-e61eb1bdabd7 | -3.33383 | -53.37328 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f56198f1-b571-39cf-9847-d3ad25319a4f | -0.18236 | -51.41668 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25e270a4-847d-3a0b-994b-41c1f5297435 | -4.1841 | -43.98131 | 2024-12-01 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b1f924b-04d2-3f3a-a074-be8af9e4ee8f | -1.10209 | -53.59892 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ff1badf-407b-3073-99b0-3ae60736e1fb | -3.32672 | -50.22064 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 93eb81be-9666-33ff-9c9e-e662991ccfc3 | -3.2591 | -53.63218 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a49ebaca-1e73-3c93-9e86-60b10d195d1c | -4.1966 | -50.67192 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15fa1ab2-e5fd-3ee6-89d3-a0113f21e7c3 | -3.9185 | -50.11494 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 294a69d5-a235-3404-893a-49e830bcd515 | -2.62371 | -46.95948 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86a0e6c7-4f91-3a8c-a63f-5b09bc845c28 | -2.0278 | -53.50074 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04296074-e303-3e72-985b-22a65877cb68 | -2.84532 | -52.5407 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 790facd6-07ae-34c8-ba32-490b8e9fa37d | -2.63167 | -51.76171 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80117435-512e-36eb-915e-0aca2220e444 | -2.12164 | -45.95935 | 2024-12-01 04:44:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49f3fb68-2795-37fb-8bba-c9663860202c | -3.52814 | -62.77439 | 2024-12-01 04:44:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34c1fecc-edf8-3382-9561-03b6fc9290b2 | -3.02511 | -54.03251 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe6d0afa-3790-3e66-b3b5-c30703e8bcbc | -6.59885 | -44.18645 | 2024-12-01 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 875cbfdb-b94a-3f39-9ecf-2671ad29b3e3 | -4.29442 | -48.21624 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d53d45a2-7d37-3eb1-afe4-a72e562004ab | -2.97797 | -53.89442 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e09df46b-632e-349b-8fef-0a3ba19806a5 | -1.51504 | -48.36207 | 2024-12-01 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 556c18be-5756-3b62-92a3-4adc8a993fc6 | -3.48246 | -53.81291 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5a261ba-60d7-3532-82c3-56f18d9359f3 | -2.831 | -48.47538 | 2024-12-01 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c68f6ec-affe-3963-bd86-3af4746a4843 | -4.68594 | -46.80314 | 2024-12-01 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16436046-2e3d-3263-8172-3cdca540005d | -3.14467 | -45.36884 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f35eb763-4c5d-3ad6-b58a-3d6e19918f84 | -1.70577 | -52.77016 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ae12ee0-44bf-3059-83c2-6a4d65a12f8b | -3.30091 | -50.49226 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66deb7c7-ab88-326d-a1ad-4f4af07625cb | -3.98456 | -49.97632 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f6a836c-ee4d-3f4f-a4cd-e4fb874e204e | -2.90324 | -54.1648 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ca92095-05fe-3d3f-bca2-18eab4257aa7 | -1.27782 | -52.69385 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93079aa2-c533-3e65-8c07-3cf11f79bc6e | -3.33707 | -53.30599 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 600e2ff9-0cb8-3450-bc08-100db5a25d19 | -3.41716 | -50.18157 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c55274b5-91fc-30b9-af93-8ff694878620 | -2.63163 | -54.22334 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33057229-fc6d-3e97-99e4-e27018b4017f | -2.43808 | -53.62793 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76576e49-d6c9-33a3-9ca3-e514701d4f23 | -1.48169 | -52.6796 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bbb6ab1-de0d-3b36-b162-f41ad8260fd8 | -2.84109 | -54.09526 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f3e904d-d262-3735-abb9-848a13668197 | -2.77608 | -55.34982 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2095dec5-bbb9-3ac7-be1a-a61a141676ba | -2.43764 | -50.49475 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e1f477-9ae7-388e-80e5-427ab1b78921 | -1.82141 | -50.90117 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 85d32973-3212-3300-bfbb-37dd94f181b1 | -2.95461 | -49.44582 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee9b6eb5-18ff-33cb-ab9b-709664f4d51d | -3.09405 | -54.132 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c04b8b3f-97b1-3705-9077-ebc1e2aa892e | -2.58492 | -49.21676 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 137157ae-a9e6-3d0f-8178-e1cb13119ad3 | -3.25221 | -50.75747 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 904f7b2e-983d-3d29-9e39-65069e0a9b41 | -2.66804 | -49.86974 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9851b9d-e908-3cce-a726-fe770969eb25 | -3.21453 | -54.17701 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10490a99-0fc8-35b2-9a47-eee420728af4 | -3.25544 | -53.63162 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ac24219c-cc47-3cf7-bf31-23bb934bcae4 | -3.6693 | -49.89567 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18ef325b-7e90-397e-b6ae-6950dc080f09 | -2.86466 | -53.99676 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4788bb0b-aada-3d74-9a7e-50a4336d7e03 | -3.13894 | -53.16806 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 285596ed-97bd-3d94-9c3a-52ce2e115fa4 | -4.20311 | -50.69048 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c83296ae-d73a-36fd-bb5f-a4125398a5df | -2.01774 | -53.30132 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a4f7002-d79b-38f5-9497-722d6a2c47de | -3.11784 | -53.27795 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f968870a-4531-3ea9-97e5-5f8b36804afd | -2.03014 | -52.07888 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c938994-d2c4-3055-9f30-1a797b12afbf | -2.63543 | -46.88298 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9025a222-2552-3855-a93e-677d6550e9d6 | -3.26872 | -53.64254 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d7ed6de7-2d97-34e7-9a53-c7c6b3e63753 | -2.3043 | -53.90467 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 328b65ba-d462-34f4-bb2f-e43205510682 | -3.67776 | -50.2474 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37b9446b-51a1-394c-b4d5-36efdab350a1 | -1.77814 | -55.27758 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db574aef-2453-306e-b166-e404ca5fd7f4 | -2.80983 | -53.05649 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fb7120f-3830-385a-b9ec-88607f478276 | -2.99024 | -51.45672 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README57.md)
