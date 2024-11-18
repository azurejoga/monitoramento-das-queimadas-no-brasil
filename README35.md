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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11c22eee-d8ae-30d9-8a9c-61684a7c90e5 | -2.19803 | -53.66388 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcde44b1-b7c1-32be-b6f1-7ed532959b2e | -2.45311 | -53.92477 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1b0fa6c-87f7-3fda-8095-07b28438d282 | -2.17596 | -50.61085 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 825f5287-e826-3f67-91c2-923cf4875dc6 | -1.76279 | -45.69121 | 2024-11-18 05:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04140047-d2d4-31a1-9fdb-44cc03c4c4db | -2.86865 | -51.7911 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e90feb2d-ed92-3264-8e11-32b64615d4cf | -2.85961 | -51.84835 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d4cbe55-675f-3078-b4eb-19e07bc2ca4f | -3.30914 | -45.69247 | 2024-11-18 05:03:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a4a9a76-1c3b-3889-a08a-4406dbb3aecb | -2.93985 | -54.10065 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff936e8b-b45d-3ab3-a468-fb8ca6f249fc | -0.93619 | -51.63492 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae59e49-bc11-3b44-9ab4-dcaea4d2488f | -2.1974 | -53.62347 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3de9d66-467b-3026-be3f-ec265af58235 | -2.15777 | -50.7021 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7ca9367-7e87-3706-af66-673fba82bcfd | -2.42626 | -54.62326 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6b5aa963-d2ff-3f9e-91b3-cc273a85bb26 | -2.57967 | -51.72134 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a962e408-2d50-36a2-a51a-f35afbde0c29 | -3.66401 | -50.43841 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 284ff9ae-671a-3c81-aafc-7f25790cceb9 | -1.3196 | -51.86934 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d99ccb17-c29d-39b8-9bea-1e8e3fb48ad6 | -1.9531 | -53.33932 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c61374-912d-36ce-b4b4-5a4f8545d050 | -1.80397 | -54.03315 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1724e5fa-e9bd-3fc7-8305-e01355785dd0 | -3.57906 | -50.25519 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c49be2e-9179-31d0-9c7c-832fab15f623 | -1.2162 | -55.81725 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b27b6d21-cd18-3ceb-a894-f989a97b2d65 | -2.17208 | -50.61026 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69f8e54f-cff3-3da0-9d16-7e0d9f19dfed | -2.84293 | -54.00281 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa2acf77-5cdf-3919-bd24-1a0e3d8a1f94 | -1.33495 | -51.85757 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14540036-6e49-39a8-96a0-f287e030753c | -1.11161 | -51.92149 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ab73f0f-5372-33ed-b512-5db9bdecd85a | -1.77464 | -55.53104 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ee89f08-56e6-30c9-8f4b-b3d58344ba20 | -3.08441 | -54.6586 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 33aca930-0816-31d4-a681-e2d0469c42b0 | -2.62729 | -46.83812 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a05c7198-3ca8-3b54-bd4f-e6515dfb2ee0 | -3.33471 | -50.49463 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f26603d6-dce1-37d8-84b9-0dce8c8f868f | -1.62971 | -53.29777 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e9d68be-a8b7-3a6a-8181-54f304c046f4 | -2.83788 | -46.66152 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37203b1b-942a-3b7e-ab6b-9675c3c6d2af | -3.16477 | -46.59631 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 936d614f-4775-37a5-b1ec-94a53b9b26ec | -3.69264 | -51.56266 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 320a5671-4a8f-3715-bba3-b4d400fcf325 | -2.34006 | -49.1339 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f8af63f-2020-3741-bbb6-501fef7768c2 | -3.5304 | -50.24795 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf832307-b3c8-3e23-a5d4-f4548d44c659 | -1.64758 | -52.77554 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6951ebd5-e358-352a-9542-de43e1dde872 | -2.76328 | -52.61051 | 2024-11-18 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b43a68a-a463-322b-80e2-b5530917af64 | 0.17132 | -51.26804 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 828bfb6f-ed30-3dca-8572-7463df870bea | -3.32304 | -54.61079 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a60de33-4ec0-3b05-8be2-5d6e9bb5fb8d | -2.67835 | -52.98696 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3299e7ff-e126-3458-b74a-3044a7a1bfed | -4.79536 | -46.49625 | 2024-11-18 05:03:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ebd9fa5-bcb0-3d60-8fb3-1eed92fcfe86 | -1.20325 | -53.69674 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6873ffb6-c25c-3c22-ac6f-f399c6b19f05 | -1.62858 | -53.30499 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b00faa36-a828-3f39-bd13-8959fadcdc19 | -2.7662 | -52.61496 | 2024-11-18 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5448355a-1f2f-31a7-99a4-0135f4a749c2 | -4.0385 | -50.88551 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aae3a3f-9fcc-3178-b301-410599840074 | -3.37796 | -53.31697 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87a2137b-1959-3e87-b8ab-f5f83828611f | -3.57147 | -50.2505 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c6b64acc-b009-3b9d-b1d7-72389fa91ac1 | -3.33398 | -53.35197 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d85db529-e249-330a-b382-8036161bdaca | -1.62275 | -52.50703 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 488d7cc2-4251-3850-bba6-ddc1f90be634 | -1.05865 | -53.66326 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2913cf7-a34e-326e-88ab-c19db4913039 | 0.61159 | -51.77262 | 2024-11-18 05:03:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9954e5e2-3020-35bf-a2d6-1e01932ce969 | -2.1357 | -52.07285 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d95bd670-b2ba-348d-9506-b846660d2b75 | -1.1708 | -49.1366 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97dd9f83-e961-3ad2-8731-7c19caabba1d | -3.1872 | -53.23499 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0417750a-0bb9-3f91-9a4b-5c71698bbfa8 | -3.17512 | -46.59792 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9981f3a1-e5a2-3926-9262-3beff03e095a | -1.4144 | -52.05179 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6415bf63-dcb5-3781-aab6-e2b282eacf69 | -4.03941 | -49.27884 | 2024-11-18 05:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bd6e328-1942-355e-b316-23eb1884b7e5 | -3.23709 | -49.12885 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f3c1cde-fb3b-3b5f-a614-7a7739274414 | -0.69583 | -52.73692 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fa9dda6-4487-3f57-b233-8437c653cd11 | -3.6675 | -50.44246 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6b9a14f-6239-368e-9be7-7c2045ed254b | -3.33074 | -50.49399 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af2fdbbd-0e4c-3430-b788-173b9de90fab | -2.34587 | -51.97635 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de4d7b37-ab5e-36e0-99c4-4c943b772054 | -1.62169 | -52.62836 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91dc2fc6-99d5-379e-b5e0-eadc4a355405 | -1.42353 | -52.81864 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea13a5c3-235b-3029-8c8b-018a0c60f685 | 0.68696 | -52.15375 | 2024-11-18 05:03:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 541480d9-f227-3eb7-a9ff-5db5280f44a8 | -1.62738 | -55.14544 | 2024-11-18 05:03:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b8cfcb-0a1f-3bf5-ba3d-dab1da178322 | -3.39587 | -54.27198 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da0d7d65-47e3-31b5-bc41-a94339afce2a | -4.11114 | -51.04481 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf5f04d1-0f1e-37a4-b54b-bfddfe0de6ea | -3.90347 | -50.08756 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddd1a5ba-5c08-3c98-a52c-5e7f3384f616 | -1.29271 | -51.73509 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 128f72cb-70e9-31a3-a78f-4285a9389eb5 | -3.42123 | -50.25394 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| baf6cc11-3b77-32d7-b9cb-2148a1ce5410 | -4.95067 | -44.84248 | 2024-11-18 05:03:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c97d8e3-75f7-3e7f-86e6-763f58fb90fe | -2.45601 | -48.81366 | 2024-11-18 05:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f3070f8-e165-3138-8423-97d2334bf61b | -3.47496 | -49.97252 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3e53b98-f440-3997-9f0e-da971a42cbf8 | -1.77468 | -50.7438 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29128b33-03b4-3f38-a0ee-0ba642a5d63b | -2.75508 | -54.06156 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8c78a2d-a708-3b86-a597-65db199c2597 | -3.69211 | -50.11015 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f763d2b1-3799-3ef0-9e91-3cc8d250fd6b | -2.65616 | -51.71115 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8336386-5808-3ff4-90b9-7544e47403bf | -1.51266 | -51.18523 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdd239b6-6ff2-3c90-8899-efd5900c734d | -3.40294 | -50.28802 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a98f4b1-7728-3f9e-8233-a5dc27a22ff4 | -2.93912 | -48.33276 | 2024-11-18 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac92131b-2446-3a73-ad58-9e2e1f5b0595 | -3.02728 | -54.10665 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 352d46ef-17e3-388e-a372-75a0410f89e5 | -1.15355 | -53.79697 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 714cc1cb-c086-34c6-8559-a28418a14464 | -2.68377 | -52.44226 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87b56a90-a5e6-3e61-9fb8-e7dda8fdfbfe | -3.06692 | -53.28582 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6b85214d-f38b-3974-833d-d174a44489c9 | -3.22819 | -45.55404 | 2024-11-18 05:03:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 877943bb-9a50-3d4d-9c39-9a79e75543bb | -1.70477 | -45.82397 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4ba478e-d0f6-371f-a4be-50d113174482 | -3.06161 | -54.41006 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eae9e5fe-ca8f-36ac-89c3-caa5b91ebe34 | -1.1402 | -51.69708 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa02a36c-46bc-369a-bd74-8abd1718839d | -3.57447 | -50.25819 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a57d2271-9bfb-37da-b584-c72b40234369 | -3.32677 | -50.49334 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 18649335-661b-34c2-9964-b4be186a55d6 | -1.81256 | -46.53261 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 13b83e7e-68eb-37c5-a896-1ae5e0444340 | -0.16683 | -50.14206 | 2024-11-18 05:03:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eed97484-c1f4-3f08-85fd-18bc1925f6c8 | -1.48632 | -51.15847 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6ee685a-25a6-3964-a331-119d259abae0 | -2.2868 | -53.63698 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d07c5ea-7778-3686-ad7c-1da9b367089c | -4.10512 | -51.05852 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6f6a36a-ad44-3786-891e-8ef5eb9e13d4 | -3.02783 | -54.10313 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 842c0923-272f-32a9-9736-64476348c172 | -2.20084 | -53.66797 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c1a34957-cc84-326d-8421-ecce0089540c | -1.57789 | -53.80082 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7afbb750-cd56-3f7c-8270-cc564916bf8d | -3.05883 | -54.40606 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 74680fb0-718b-3dce-a01b-b18760dd8379 | -3.60226 | -54.7389 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e636e13-f3f6-3f99-9a4c-1285f5bdf851 | -3.37353 | -54.80983 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
