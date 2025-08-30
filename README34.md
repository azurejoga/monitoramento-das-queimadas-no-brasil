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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e740bd68-8432-3ea7-a754-8456ee1acc5a | -9.57445 | -54.49578 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 273676bb-013d-3301-a14b-3f292aa83eae | -11.07103 | -52.04805 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18e2c7a8-4062-3245-8d73-19abfa394828 | -11.33556 | -43.6016 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33e9cd12-a128-34fb-9d2c-59cda6c22f5f | -13.3887 | -47.03523 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed27185d-4c5f-3c1b-bbec-35e1886ec683 | -14.34375 | -51.89286 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8710dd61-ceba-3382-8723-654b4e673e2a | -11.2289 | -45.00892 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad4cb25d-d253-3422-bd16-5dfad62635a0 | -11.06384 | -52.03859 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 636d170b-9923-37a2-a59e-ceefb9866cbe | -13.39162 | -46.99559 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7df4a270-45b6-3ee2-bc51-abf6476520b1 | -13.19577 | -45.28052 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d4eac28-50c3-3025-ac41-fad00f6ee53c | -12.83697 | -48.09715 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2245ea3-595c-3be2-9e1a-bcc57b32e018 | -10.99816 | -46.95891 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0695a63b-126f-39f6-b67c-61adafe208a9 | -13.43375 | -46.94427 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7901a96f-2248-33c6-ad8c-28052d1ccf80 | -11.31252 | -43.66147 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 45f2cb2e-0d96-37ac-992c-b362c03ad3e0 | -13.36879 | -46.98832 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 033fb168-a20a-3615-bd50-532e9d30a17d | -10.96345 | -49.5715 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16c7606c-62a2-3357-a561-c991adc2b174 | -9.69215 | -48.30363 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fe7f6f2-ed62-3f1b-9c3f-6c61dd346ec4 | -15.11916 | -48.56585 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c18407b2-a97e-3430-8180-d75f23a1bfb9 | -10.443 | -51.3569 | 2025-08-30 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd584979-0456-3c45-ab78-c56f7585ef2f | -13.57135 | -46.91242 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9719d6e7-2378-3e11-988a-cb9f974ba85a | -16.38271 | -46.28107 | 2025-08-30 04:21:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 737a95f0-80ee-3a8a-bfc6-0d0b41a3b4dc | -16.40854 | -45.65172 | 2025-08-30 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 615ebb9d-0fb9-3992-a5c1-03ca483eedac | -13.3845 | -46.97623 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2799438-f043-3ad4-8151-865ee5f0c404 | -11.82981 | -46.45979 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 33fbec80-5524-311d-b050-85ac87f85b41 | -13.19467 | -45.28773 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18b27a8c-9447-3a27-9eda-65678b797ce7 | -11.07102 | -44.77548 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52354c4f-3f0a-3d52-8c43-20835bbbac71 | -13.45688 | -46.96978 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b274f51-5026-356d-a676-9cd652cfdc44 | -11.33556 | -43.57759 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6972327-0f78-344a-aee6-5ecf6cdb84fd | -14.00534 | -44.58641 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ffb493d-f452-3536-88a6-406765168559 | -9.94485 | -44.0232 | 2025-08-30 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f05a3287-1429-351a-970d-dac2992ed678 | -10.49144 | -51.63108 | 2025-08-30 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d922f786-9cca-3cf2-acf0-39d377cd9b73 | -11.41243 | -46.92432 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9da107ce-cf5b-3bbb-87cc-59cb9b62ec9c | -15.16746 | -52.3259 | 2025-08-30 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c0cec21-48c5-30a3-ac9a-3e925c6d5be9 | -10.66741 | -48.72961 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0332d251-4c67-3e96-a1be-f0db4f947e92 | -13.50623 | -46.93783 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a6a5470-2bf9-3911-9928-013a498d7131 | -12.82344 | -48.18031 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb9d633-4b17-3a11-8b8d-1a904920c287 | -10.48721 | -57.95503 | 2025-08-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 10b6a3e0-2d31-3b72-b041-4cb8ebf5ecbd | -11.31713 | -43.65428 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8cbf45c-4626-3b63-aa0c-fdbc7e8f0119 | -9.58016 | -54.47029 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7da40ddf-922c-3871-b30d-9153f580eda8 | -10.0256 | -48.05867 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7747c06f-c88e-3e26-a831-360f6d655f33 | -14.62711 | -48.07403 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9e5ba92b-af1d-31ff-9b2d-34f192efc1c1 | -10.80529 | -46.35412 | 2025-08-30 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8979f230-b030-3f62-ae54-b634ee678368 | -10.02952 | -46.03058 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c03c62a3-84bb-3200-9f80-53ce5af38f82 | -11.83311 | -46.46033 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 9ab37941-9090-3968-8e25-74c2c04de805 | -15.31113 | -46.08933 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86afb6d8-f7f0-325b-8d77-5e68e88f3388 | -13.42271 | -46.94963 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28cfaace-f83a-39f8-95be-d2f035ebffee | -11.83524 | -46.78974 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06a8f343-9c7f-3e96-9e13-65c91e1ff8c5 | -15.24064 | -48.25764 | 2025-08-30 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 018babc6-f2cd-32a1-9ea6-31b0a0939e25 | -10.93905 | -47.4314 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8eb928-2b9a-3724-9af4-a0f0d47b4699 | -11.87283 | -46.42355 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d3c858-f928-33a9-8f77-14210eec0ef2 | -12.83759 | -48.13635 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83256afc-1c2b-3d33-8d42-a1f2fcf558d9 | -13.50786 | -46.94895 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f19e8760-69ab-3dbb-9717-e3bc0006441b | -13.4089 | -46.95105 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4adfbec0-34c7-39b2-9bfd-261d2b433cee | -11.35702 | -43.5528 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 124b5a29-13e0-384d-b16d-b1d16ea031fd | -11.30831 | -43.56938 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11bc6c97-3804-3c99-b49f-0bf5122e2898 | -11.35876 | -43.54105 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea615e3f-96fb-3a1a-af9a-7ede17afd388 | -15.16125 | -52.33695 | 2025-08-30 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec2281f9-e532-31ca-bbeb-1b0a3bf10e59 | -13.67539 | -46.87893 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae902927-5c25-31dc-84d1-0edbaa219482 | -14.04237 | -44.50211 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c09155b6-05d7-36d7-89d5-3b97976e7e69 | -8.55097 | -51.30884 | 2025-08-30 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32afb7df-3fdf-38e9-b054-276eef3c52c8 | -13.19633 | -45.27691 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7e832fd-25c6-346b-aee3-178a3fb1df33 | -12.63109 | -57.00745 | 2025-08-30 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e420cded-a156-3bbb-ab03-dac25b7c8ed1 | -14.31819 | -51.87322 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5156979d-67e7-3732-97fc-2d29dc3a96b5 | -11.88606 | -46.40409 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b462259-e30e-38a1-a2dd-f24c99356039 | -16.30804 | -42.04343 | 2025-08-30 04:21:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3d1909de-3caf-3ff2-af55-dc34236fc86a | -13.39868 | -46.8441 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7b62131-a645-3b5e-83c4-ddd90b0cebc7 | -11.36223 | -43.56563 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed9f73a5-5769-3ff3-b242-062261dc61ff | -11.87507 | -46.38786 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fa11bf15-9501-384d-9e78-041babe18535 | -12.83944 | -48.12496 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c27da63-3419-3b42-816b-8344d5c9002a | -11.90012 | -46.72462 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b17a1e63-3c01-3317-88f4-bdfc77da2d3b | -11.32577 | -43.64375 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c32f6b5-fa58-3682-9a4d-fd5a4c8330b4 | -11.35644 | -43.55671 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9124189f-54cb-3082-bf3d-252c91b50b6c | -13.50237 | -46.94078 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e1d1cf2-e13d-3719-8466-3bc2eb4c0206 | -10.02346 | -48.09386 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 999977f0-553e-39e8-94b8-942c8c39c278 | -15.08013 | -48.15909 | 2025-08-30 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c331980b-4424-3ab4-8bc1-1c44363f3351 | -16.40799 | -45.65545 | 2025-08-30 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 211171ab-6544-37a9-8194-d1c11e79838d | -13.65271 | -46.91512 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef96a45d-2b82-3b84-9941-6a11a9d7aeac | -11.0624 | -52.04671 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc0a8d5a-ddb6-36d6-834e-e89dd1d37c10 | -11.07491 | -44.77243 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae8dfb35-b390-3c9f-9cdf-49d20b3780f5 | -14.84614 | -46.74525 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aebf6d22-4054-3624-ab59-f1550f62f8a2 | -8.83004 | -47.7804 | 2025-08-30 04:21:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7c0967d-5c17-3788-bc53-f58bde0dfa26 | -11.84589 | -46.40105 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcd2b11a-9569-3529-9ecb-5284275a7922 | -13.35467 | -54.38691 | 2025-08-30 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92735738-7893-3755-be12-e4c76beac3ff | -12.69579 | -48.20894 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cd6258c-c2a5-3286-9cf4-7aed935fe7fc | -14.02069 | -44.55371 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b6826a60-f04c-3ceb-8795-8da59a7511e3 | -10.93965 | -47.42773 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52047283-c1c1-345c-9332-98ef306c089f | -11.83451 | -46.85867 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b791755-4a1a-3064-92c6-17df2138d3e8 | -15.08619 | -47.16454 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf814b74-1b42-3922-b28c-b68e45c4d4ef | -11.91774 | -44.8592 | 2025-08-30 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 298c9bd6-c7f0-31a6-8e09-5550e4d2d02c | -12.9398 | -46.1469 | 2025-08-30 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 160b196e-b36a-3af5-98e4-ef16cfe42fb3 | -11.40861 | -46.9054 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ec251da-2ba6-30b1-ad64-76323fb75016 | -13.98065 | -46.31971 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49973072-8bd1-38d6-82b0-ed50888fd940 | -11.30668 | -43.62889 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3d60bae-4549-3a2d-8ab4-42b4b75c813c | -11.35818 | -43.54496 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0530786c-5680-3166-8c45-38f808235c42 | -11.83478 | -46.44978 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e268943d-a73b-3c38-925b-b2d1f5b844a7 | -10.3666 | -59.20052 | 2025-08-30 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d2eb6ab-3e88-331d-a9d9-e90f784ac532 | -11.8662 | -46.44407 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3b770498-d0e3-3bf3-aa5a-c040a0dfd0e3 | -9.58534 | -54.47125 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32078fb0-455e-3b5d-8325-94a20da230e1 | -13.3744 | -47.01829 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8904250a-8f7a-37a7-8256-1d5bf00359f0 | -13.58462 | -46.89285 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41b0a1b2-0551-3795-9bd5-1c6b21b4c657 | -9.58368 | -54.48014 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README35.md)
