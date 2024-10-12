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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e27f9bd-4f48-3221-8f58-417f0a100ff0 | -15.6228 | -59.9585 | 2024-10-12 08:26:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 85cbb883-3a9c-37ac-81dc-654ca2a368fc | -17.826 | -57.3807 | 2024-10-12 08:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.3 |
| d9d06e33-1f40-331e-9163-1b86efdee823 | -17.8461 | -57.3576 | 2024-10-12 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 624f888e-4cc6-3d57-a27e-9954ca577554 | -17.8457 | -57.3783 | 2024-10-12 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.2 |
| 74b7ddda-6e51-3bf1-89bd-4563ed6cfab7 | -17.9643 | -57.3637 | 2024-10-12 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.1 |
| ae48d0bf-c740-3421-b07b-9c2786b739b8 | -17.964 | -57.3843 | 2024-10-12 08:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 5ec3e3c6-f486-34e1-b368-977af49f5174 | -12.4367 | -54.5778 | 2024-10-12 08:36:16 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b40d3c5a-aed9-38db-90a3-9bfaa469b4bd | -12.437 | -54.5573 | 2024-10-12 08:36:16 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 42988b49-0918-35ac-b59e-a1f7dbd6e81f | -12.4558 | -54.576 | 2024-10-12 08:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 260b9403-f076-3b6c-96b4-860544f591a8 | -12.456 | -54.5554 | 2024-10-12 08:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 862c7deb-c5cc-3b78-bc9a-e3c0bad1018c | -16.9805 | -57.4404 | 2024-10-12 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 4cf953bb-aa8b-3e07-a987-0441ff563fd8 | -17.9643 | -57.3637 | 2024-10-12 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 8a3a876d-8141-34b3-9336-410034eb9eba | -17.964 | -57.3843 | 2024-10-12 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 11447e76-601e-32f7-b188-64a28d06d758 | -17.9841 | -57.3612 | 2024-10-12 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| c6ace5b4-9cc7-3729-89fc-47648d18a26a | -17.9837 | -57.3819 | 2024-10-12 08:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| c7970745-46ff-35bd-81a1-3be6fb142b1b | -18.1956 | -56.5483 | 2024-10-12 08:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 7b74120f-5a47-3173-bbfe-94a0bd119b4f | -13.7348 | -60.5883 | 2024-10-12 08:46:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 23c071e4-b289-3ba3-802c-111499258da4 | -13.7346 | -60.6079 | 2024-10-12 08:46:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5bfdf866-cf01-3649-9529-99bb219f43c8 | -15.6225 | -59.9784 | 2024-10-12 08:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 6cd53529-ed7c-39a8-96be-01efe3eab34e | -15.6228 | -59.9585 | 2024-10-12 08:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 52ad6b33-1245-3c97-900e-f2643256df6a | -17.9643 | -57.3637 | 2024-10-12 08:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.9 |
| 18c6d77e-5df6-3e10-b380-c89d343c5c98 | -17.964 | -57.3843 | 2024-10-12 08:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.1 |
| 0902da41-3739-342d-b9d9-54e977cd0a42 | -17.8457 | -57.3783 | 2024-10-12 08:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 392e3224-d80f-394d-b00e-73f72d20c41f | -17.9841 | -57.3612 | 2024-10-12 08:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 7a00eefc-395d-3830-8ef8-10720c6bd5b1 | -17.9837 | -57.3819 | 2024-10-12 08:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 52af1035-f49e-307d-a7eb-a70381b3d267 | -13.7346 | -60.6079 | 2024-10-12 08:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3820fce4-02f3-392e-8326-3fc2924eb43c | -13.7153 | -60.6289 | 2024-10-12 08:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 128942f0-58b1-3acf-9308-fd89d7ba62b3 | -17.964 | -57.3843 | 2024-10-12 10:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 45a8bad0-8a23-372c-ae2b-76139a1bb08b | -17.9643 | -57.3637 | 2024-10-12 10:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 411180c9-d3c7-3edf-99b3-1d9df3c5b06b | -17.964 | -57.3843 | 2024-10-12 10:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| c8172866-3f52-33f2-9145-5890256a3031 | -17.9643 | -57.3637 | 2024-10-12 10:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 01f1fb7a-ea5b-3aa2-bc48-49d780612d1f | -17.9643 | -57.3637 | 2024-10-12 10:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| b62aa70e-7a3a-342b-9650-2bd1f35dacf6 | -15.6225 | -59.9784 | 2024-10-12 11:26:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 8c8231a3-6199-37ba-a242-b21eea5f39c7 | -15.6228 | -59.9585 | 2024-10-12 11:26:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 745af51a-a4c4-353d-bb42-60322c9e2cf9 | -15.6228 | -59.9585 | 2024-10-12 11:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 9ca09e70-5e61-3e44-b811-9e33121b7faa | -15.6225 | -59.9784 | 2024-10-12 11:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 32bc9950-9e84-3b74-a470-df26b81ca0ac | -11.2912 | -50.9208 | 2024-10-12 11:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 217.3 |
| 503b049e-61ff-371a-8388-d39031083bcb | 2.8262 | -51.1119 | 2024-10-12 12:04:50 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2bd3fbbb-084d-37cf-bef8-7bb4676e57d9 | -3.39274 | -44.76203 | 2024-10-12 12:21:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b1c0e259-9699-30f7-8ecf-71bcedc6f93e | -3.41651 | -44.463 | 2024-10-12 12:21:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 37d6fd22-4166-3c96-b5f5-41468595a6af | -5.03541 | -39.83917 | 2024-10-12 12:21:00 | TERRA_M-T | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 29c86608-3079-37fb-a270-ca0c06b62e8e | -5.97813 | -36.92959 | 2024-10-12 12:21:00 | TERRA_M-T | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 23.2 |
| fb87a164-3e24-37f0-9589-805023e8ff14 | -5.42121 | -35.78661 | 2024-10-12 12:21:00 | TERRA_M-T | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 139.8 |
| a4b051aa-c5e0-363c-a0ea-6926566f9817 | -5.36316 | -37.79071 | 2024-10-12 12:21:00 | TERRA_M-T | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 15.1 |
| db2c9413-ca40-3859-afd4-ea17b3af6249 | -6.44828 | -38.81046 | 2024-10-12 12:21:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| c317b468-b627-34d4-849c-cd85b97e029c | -6.44679 | -38.82131 | 2024-10-12 12:21:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 28.7 |
| c4096137-dd9f-3fff-adb6-8d0de5065c6a | -5.00882 | -39.17289 | 2024-10-12 12:21:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 33.3 |
| d89a050c-8d5b-32e9-8046-ec4fa7b6f228 | -5.0035 | -39.16621 | 2024-10-12 12:21:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 5cccd5cd-f4e8-3401-8c6d-34e48c97fc26 | -5.00208 | -39.17616 | 2024-10-12 12:21:00 | TERRA_M-T | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 455aab2c-e96b-306e-8981-498740d4bd2b | -5.11829 | -39.90445 | 2024-10-12 12:21:00 | TERRA_M-T | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 8a541dd5-109b-3fdd-b7b6-21e29f03c7c7 | -5.03408 | -39.84851 | 2024-10-12 12:21:00 | TERRA_M-T | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 3f32e939-6a4e-381c-9335-10c7819361e3 | -9.04007 | -40.57066 | 2024-10-12 12:21:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 67.3 |
| af90eac2-53ff-30d8-98df-d42d81bd6d58 | -9.03872 | -40.58017 | 2024-10-12 12:21:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 58f8d202-457b-3726-b575-0ecee6d61732 | -8.50941 | -39.94581 | 2024-10-12 12:21:00 | TERRA_M-T | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 81cd8f71-30f0-3b31-a49f-e80379653a51 | -8.49969 | -40.80819 | 2024-10-12 12:21:00 | TERRA_M-T | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a044aefc-73ff-3d1a-95a5-f0ccfbb1e6f8 | -8.26779 | -39.62651 | 2024-10-12 12:21:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| ec4846dc-d2d0-3cb7-b7fa-8971fed839a7 | -8.04063 | -39.4829 | 2024-10-12 12:21:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 8c803832-3dc5-3708-9e99-b2cff72d1071 | -9.97435 | -40.79795 | 2024-10-12 12:21:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| ccec0a37-21ba-3e4c-8039-6c61a2e80de6 | -4.76288 | -41.54697 | 2024-10-12 12:21:00 | TERRA_M-T | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 546354f0-eddf-36aa-8d61-355e0586f5b1 | -3.78346 | -40.34484 | 2024-10-12 12:21:00 | TERRA_M-T | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 7eb489fe-15d1-3d31-aa83-fe7cf1f2b236 | -3.71328 | -40.70596 | 2024-10-12 12:21:00 | TERRA_M-T | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| bb578bde-7706-3272-aeaf-17b61eefac65 | -3.712 | -40.71479 | 2024-10-12 12:21:00 | TERRA_M-T | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 6bb0e0bf-11aa-3f22-b706-0941bdcffb14 | -3.70425 | -40.19098 | 2024-10-12 12:21:00 | TERRA_M-T | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 26.5 |
| ced1d3ee-7052-3ee5-8312-53b00f1491d4 | -3.70314 | -40.71354 | 2024-10-12 12:21:00 | TERRA_M-T | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| caa9f2f7-4b71-3486-9aa0-d29a03e5fea8 | -5.41373 | -40.35384 | 2024-10-12 12:21:00 | TERRA_M-T | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6125c070-c71f-3eb0-9430-c0123958b7c3 | -8.92448 | -41.18882 | 2024-10-12 12:21:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| b36733a7-797b-37f4-ad90-f488649c7dd8 | -2.73326 | -42.18053 | 2024-10-12 12:21:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ce40997d-5a26-3f39-ab0f-491629a27dae | -3.81205 | -42.37009 | 2024-10-12 12:21:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| be41b099-9007-3514-96ed-0a0922b7e821 | -4.47275 | -42.89016 | 2024-10-12 12:21:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ddb4d18b-a160-34b5-9d94-7bf4e5a57333 | -4.42439 | -42.84785 | 2024-10-12 12:21:00 | TERRA_M-T | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a56f3bc6-e319-384f-bdc5-c7b9dbe35521 | -3.67414 | -42.62578 | 2024-10-12 12:21:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9cf577ad-39f8-3a1c-8442-44471a1803f7 | -3.66495 | -42.62451 | 2024-10-12 12:21:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cd05ab25-b0de-3a86-8846-8333ade22f7c | -5.95768 | -43.2722 | 2024-10-12 12:21:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 617f2af2-f3ba-348f-baca-18f77ed5f5a6 | -9.26486 | -43.53824 | 2024-10-12 12:21:00 | TERRA_M-T | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 7a74a382-ac0b-35e1-b925-73aa14b5406f | -9.02386 | -42.9869 | 2024-10-12 12:21:00 | TERRA_M-T | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| fe126a97-09fd-3a4c-abc6-040ef9fd350c | -8.13637 | -43.00138 | 2024-10-12 12:21:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0ac269a4-20a1-34ec-8208-efb5cbca6810 | -8.13504 | -43.01052 | 2024-10-12 12:21:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 7e9d07db-7267-385f-8142-2e3bc55f2f6a | -8.12737 | -43.00008 | 2024-10-12 12:21:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| c2bdf203-6eb4-38b1-b5f2-fceb3bc8272f | -8.12603 | -43.00921 | 2024-10-12 12:21:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| fa4e6492-5690-3ec3-aac0-42426d6535f0 | -3.41213 | -43.32857 | 2024-10-12 12:21:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3d688634-b91f-3f0f-a674-b8bbdd569c4a | -3.4106 | -43.33881 | 2024-10-12 12:21:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9b17c05c-328c-34b3-8f7d-9634b9b98a84 | -4.53321 | -43.295 | 2024-10-12 12:21:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1ea0707f-e61a-3a0c-8ac2-73e8a1bfd60f | -7.38155 | -44.79206 | 2024-10-12 12:21:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 2ca8622f-d55a-35ba-90d4-bef15185cf24 | -7.37987 | -44.80325 | 2024-10-12 12:21:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8bd370ab-bad4-354f-b89d-22e5c54682e8 | -7.08492 | -43.81985 | 2024-10-12 12:21:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 921b75a7-15ee-3ce7-8ae3-eeeaa3fc7a3f | -7.00958 | -45.21652 | 2024-10-12 12:21:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f4081565-4f83-30ed-91b9-27d6148d2d39 | -9.25244 | -44.54763 | 2024-10-12 12:21:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 01bd16a9-1708-3a4b-b7d1-fed7a697131b | -9.25087 | -44.55806 | 2024-10-12 12:21:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 729d341c-79ab-3022-b959-f13a2cb18f6e | -9.14012 | -45.28666 | 2024-10-12 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| cec05526-a6e3-356d-91ca-a328133a0ae5 | -9.13836 | -45.29815 | 2024-10-12 12:21:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 339458a1-b7a7-364d-b33f-9683ba226c93 | -8.13856 | -44.4659 | 2024-10-12 12:21:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4fd5b1b4-bfd0-3219-94b3-9ffd6fa83c5f | -10.9365 | -44.64347 | 2024-10-12 12:23:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b9d3736f-8efe-3cf3-9197-bf541ad101ec | -12.34252 | -45.32642 | 2024-10-12 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| dd60fe56-5f40-339f-9dca-e77cf5ca565c | -12.09958 | -38.37606 | 2024-10-12 12:23:00 | TERRA_M-T | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| c4dafddf-b313-37ac-985f-90198a18c47d | -10.42502 | -39.59938 | 2024-10-12 12:23:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| af7688a1-6d2d-3be8-aa40-c6fea2cd40e4 | -10.50542 | -40.55902 | 2024-10-12 12:23:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 2c1377b8-8d2b-3ed5-a234-38810ae0cb9c | -10.448 | -40.10449 | 2024-10-12 12:23:00 | TERRA_M-T | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 64d26297-ebb4-379b-a5fd-3c5e159ce04c | -11.5834 | -41.53448 | 2024-10-12 12:23:00 | TERRA_M-T | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 1f0ed82d-3c67-3cdc-8825-6a1e5b11e058 | -13.61573 | -41.54319 | 2024-10-12 12:23:00 | TERRA_M-T | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8e63635d-3486-3a91-aff4-034fa2304e7d | -12.78993 | -41.59513 | 2024-10-12 12:23:00 | TERRA_M-T | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 23.7 |


[Clique aqui para ver as próximas entradas](README152.md)
