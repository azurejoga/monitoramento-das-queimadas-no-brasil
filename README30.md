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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51667712-b1f8-329d-88d5-5f57e7e5f249 | -17.12933 | -51.68509 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 719f40dd-06c8-3bee-b977-d58a04b9b2a9 | -17.1383 | -51.6584 | 2026-08-11 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57ea4351-1b6e-3b8d-a635-84571f58608b | -16.28274 | -56.59814 | 2026-08-11 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 783900c6-65d7-3f15-abd2-93702231df91 | -4.2634 | -48.2016 | 2026-08-11 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7b876ec0-f559-3115-beec-21eb72f50a5f | -8.96 | -60.5358 | 2026-08-11 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 332cd452-46f6-3f3b-a2c0-d54a32dc8303 | -4.2635 | -48.1799 | 2026-08-11 05:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6dda7939-6e03-375e-b9fb-16ffcc7d04cf | -9.3714 | -47.5119 | 2026-08-11 05:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 4fdaaa7c-cfb0-30e1-ba4d-5b04a282ca04 | -4.2634 | -48.2016 | 2026-08-11 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4cd17a73-a626-3038-a938-6488076ccd3e | -4.2635 | -48.1799 | 2026-08-11 05:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d7210fd6-e476-3203-92e3-4fd3e3fb272d | -14.6268 | -47.6506 | 2026-08-11 06:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| caad7173-b400-346e-aeeb-a7fb31d25058 | -8.9601 | -60.5165 | 2026-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 3db27689-2c84-3a93-8a10-2cd3f17ec19e | -4.2635 | -48.1799 | 2026-08-11 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6671c0dd-b359-3063-a13e-00d68b0f0f13 | -9.3909 | -47.4656 | 2026-08-11 06:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 9a2aadb2-6146-3d9d-9b34-f7198dee6829 | -14.6268 | -47.6506 | 2026-08-11 06:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 21a1f341-434d-3b13-8780-dfbc9b2f33a5 | -8.9598 | -60.555 | 2026-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 1d352ad9-f280-3a16-9b53-fec445775e8f | -8.9414 | -60.5367 | 2026-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 56f36fea-6216-3b5f-98e4-2de591ddfc12 | -8.96 | -60.5358 | 2026-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 000c5985-e784-369d-9a15-9cff60ca0677 | -8.9415 | -60.5174 | 2026-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 9b46081f-2348-39e0-b8f4-5e13562f38fe | -8.9412 | -60.5559 | 2026-08-11 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| ee618284-9e59-3f83-9b53-9f1434cee6cf | -2.36128 | -67.218 | 2026-08-11 06:14:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10874c1d-5e9c-3d80-8c6c-0360961b01e4 | -8.95711 | -60.54517 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 91940051-d928-3694-b85a-7c1db769d14e | -9.47345 | -60.51559 | 2026-08-11 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02255efa-fd3d-38c0-a258-a9c408a34983 | -8.94784 | -60.50657 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 196fdeef-5ba4-3af3-85a8-887c80c34721 | -8.68139 | -62.87505 | 2026-08-11 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12a1e7bd-31fc-37bd-808c-d1e1d0a6de09 | -8.95477 | -60.56507 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3609331-fc85-336e-bb03-db3c05272924 | -8.95156 | -60.53361 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| abae229f-e969-3018-aa2d-2e9c66c6f3fc | -8.95076 | -60.54002 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ceb3d5d2-8e4e-3472-b111-991a91fd3d37 | -8.94859 | -60.49753 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bc4f408-b960-382d-940f-e419beb6bc80 | -8.95521 | -60.56086 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 70e457f4-81f4-332c-8eb8-62bc09bad8ea | -9.47184 | -60.52893 | 2026-08-11 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 78e981e5-fe2d-3751-9d5a-b22695ed4941 | -8.95552 | -60.49858 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 90b61a71-e52f-3a39-9803-ab3ec5bb0bd8 | -8.96247 | -60.49947 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4e8d310e-a904-3fc5-9b03-32d690b920d9 | -8.95632 | -60.55185 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 743183fa-9125-3a0e-ae97-10d4ec5a357e | -8.95094 | -60.5378 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 923da32f-bbe6-35af-bce4-aa9d11a78f66 | -9.47027 | -60.54187 | 2026-08-11 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c72c1615-871e-3ec1-b5f7-a2d7c513412b | -8.95605 | -60.55413 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cdd18c56-4d3d-3c93-a583-ee7b543278ee | -8.95553 | -60.55858 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4745e8e3-2142-31b5-ad1f-2d48e3cae9cf | -8.95019 | -60.54418 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1d626ff4-722d-39de-8846-db4cb9f9ef5a | -8.95688 | -60.54741 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3c379234-8374-33fc-99e5-b6bb05887e84 | -8.95477 | -60.50761 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7cd9dc53-b48d-35ab-9749-adf5f42dd041 | -9.47803 | -60.53627 | 2026-08-11 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43a440c3-58b2-30b2-82e4-9cace5c9b642 | -8.94476 | -60.53039 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4de53858-1184-3164-b45d-b4b2fd798006 | -8.95404 | -60.57123 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0dad141-d6e9-30b7-a135-186431122484 | -7.41429 | -60.00717 | 2026-08-11 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b29cf5b-c8b8-3fb4-a422-024314c89fa3 | -8.94543 | -60.52615 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e67dc58a-4eb5-3990-b5ec-bcb3b743c4c0 | -8.95559 | -60.50098 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 86a914d5-2c11-3715-abe0-da109af7d04f | -8.95474 | -60.50526 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 73ecc1ac-b913-3529-aae3-8ed124067c36 | -9.47883 | -60.5297 | 2026-08-11 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d1369aff-c8b5-34ae-bf54-00430c9e2ec1 | -8.94782 | -60.50417 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 080654c1-23bc-3e7e-90fa-4840fd2cb889 | -8.95847 | -60.53462 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| cc185c1e-6058-3db0-ad59-418c11b399b5 | -9.47264 | -60.52228 | 2026-08-11 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ea3a6956-9b91-3670-aada-dc63ba535165 | -8.68195 | -62.87059 | 2026-08-11 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d0b0dcc-934c-328c-ab69-1d9dd23a0637 | -5.69016 | -60.23219 | 2026-08-11 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 564fb8a6-e406-3021-99af-8a3905eb14bd | -9.47106 | -60.5354 | 2026-08-11 06:14:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b834e753-f80e-32a7-9fb7-4618b7e55eda | -8.94866 | -60.49994 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4381821a-3c01-39da-aaff-78affb614fe6 | -8.95768 | -60.54098 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 56d629e2-609e-3c4d-9aa3-7e11587d5a86 | -8.95786 | -60.5388 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8c49ef92-681f-3246-9841-df0cc2d1d688 | -8.944 | -60.53688 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 362def08-c3c6-3b28-a46b-5d83b9a09b50 | -8.95169 | -60.53135 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 1a829c00-0851-36e3-999f-03a707a69d6a | -8.95641 | -60.49431 | 2026-08-11 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3188ac38-a0bb-3587-bc93-2ce112d02600 | -9.47198 | -60.51696 | 2026-08-11 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94ae0068-038f-3f90-a3f5-eb4c4ace06c9 | -9.47745 | -60.5311 | 2026-08-11 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f5d9efc-fa12-38ea-8b79-9b92c348ab04 | -9.4782 | -60.52451 | 2026-08-11 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce01bd4d-1a81-3e39-b5f9-81be4be63f83 | -9.47122 | -60.52365 | 2026-08-11 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b24e5f04-4e94-32e4-8950-a0d6559d66fc | -9.46972 | -60.53674 | 2026-08-11 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b408330a-1b67-3984-ad5b-6105625ff3e7 | -9.47046 | -60.5303 | 2026-08-11 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c6054dd4-ada6-3c70-91f3-7183ea7aa430 | -10.1523 | -67.72495 | 2026-08-11 06:16:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b60d9919-736b-3f91-a0ab-adb321a035ab | -9.4767 | -60.53766 | 2026-08-11 06:16:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff93f8f7-4909-3a36-a633-e0bc1da0acb3 | -4.2635 | -48.1799 | 2026-08-11 06:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ab33cd09-bf4c-3f45-87e2-0b4e3f458f6d | -8.96 | -60.5358 | 2026-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c939846b-4a4c-3a55-a984-97c7e525e97f | -8.9601 | -60.5165 | 2026-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| fe9c39e9-f1fb-3b55-a5e0-7ac406ac2119 | -8.9602 | -60.4973 | 2026-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 12315819-8d8b-36e1-873e-c0dd661db9fa | -8.9598 | -60.555 | 2026-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9edf1208-7dcf-32ad-a93a-9150f714474b | -8.9415 | -60.5174 | 2026-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d3da9ec1-07d7-36f3-91da-c852a0976c53 | -8.9414 | -60.5367 | 2026-08-11 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8e6b35a9-cbce-30d2-84c2-e6d8810138aa | -8.96 | -60.5358 | 2026-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a5cb33d9-8521-3b38-b4f4-32409113171b | -13.5502 | -46.2844 | 2026-08-11 06:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c898be43-25df-3d60-abb6-0a2a718928db | -13.5701 | -46.2584 | 2026-08-11 06:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 273.6 |
| de5ad060-3a33-3dcb-8908-2435ad39655e | -13.5705 | -46.2355 | 2026-08-11 06:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 79f0e1b2-fba4-3e7c-9285-9fe8cce1a893 | -8.9414 | -60.5367 | 2026-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d51f49ef-5122-3b21-a9ae-fe54571a7c38 | -13.5507 | -46.2615 | 2026-08-11 06:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 40835752-633a-3941-afb5-e820ab2010f1 | -8.9601 | -60.5165 | 2026-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 84eb4f02-9a25-377c-a5b6-ee151f71fd1d | -13.5696 | -46.2813 | 2026-08-11 06:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 8846616f-388b-3b6a-b80a-57125551fac6 | -8.9412 | -60.5559 | 2026-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 05c741bc-d144-3f7b-984c-46f14af78088 | -8.9598 | -60.555 | 2026-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 44f9baba-7445-3ca8-aa22-140be7d64af9 | -8.9602 | -60.4973 | 2026-08-11 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 65a272ff-50aa-364e-a81d-c6b6bb69d380 | -8.9598 | -60.555 | 2026-08-11 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5073b42d-6755-3805-bf07-1274f00a82f8 | -8.9602 | -60.4973 | 2026-08-11 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 595c7b2a-b108-309d-912b-b3f25ab87a5c | -8.9414 | -60.5367 | 2026-08-11 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 4e9e28f9-215b-359c-9e11-f3d5f60cefbd | -8.9601 | -60.5165 | 2026-08-11 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| e1386646-e08f-3243-a03b-1a9d3ba3792a | -13.5701 | -46.2584 | 2026-08-11 06:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 408.5 |
| 229cf82b-ab05-3c04-a669-b877c6d53739 | -13.5507 | -46.2615 | 2026-08-11 06:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 1bea2439-ddb8-3c00-839d-d484a5bcc1fd | -13.5502 | -46.2844 | 2026-08-11 06:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9f2d40d9-0287-3620-ac1d-86317f107045 | -13.5696 | -46.2813 | 2026-08-11 06:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 226.1 |
| fdcba9af-3f75-327e-8f4a-9cfa335cd955 | -8.96 | -60.5358 | 2026-08-11 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ea83671f-281b-351b-9296-629208dca65a | -8.9415 | -60.5174 | 2026-08-11 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 795395d3-ef70-3e1c-8def-fbf4460f95f8 | -13.5701 | -46.2584 | 2026-08-11 07:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 264.2 |
| 9ee05217-6167-30a8-acfb-e99cd6573b6a | -13.5507 | -46.2615 | 2026-08-11 07:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 2488e4bb-3512-3e5a-b305-77ed858bfc67 | -13.5696 | -46.2813 | 2026-08-11 07:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 306.4 |
| 66eb3210-8c3d-3cda-b936-504a5860f0de | -13.5502 | -46.2844 | 2026-08-11 07:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 119.6 |


[Clique aqui para ver as próximas entradas](README31.md)
