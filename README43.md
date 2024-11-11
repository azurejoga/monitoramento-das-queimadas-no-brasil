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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94bf281f-5a64-330b-9983-872de08c8fb9 | -1.23934 | -55.91168 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc054ced-3a2a-3ebb-aaf0-c48a2b6dd892 | -2.73076 | -54.14492 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35f65ae9-2fb5-3faa-8f5b-6efeaa0aabf1 | -3.0207 | -53.25067 | 2024-11-11 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7a8beeea-ec33-3c82-809c-519cb56b5768 | -2.23656 | -53.66994 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef720c09-2fb3-36f0-b0ec-d455e06c9e1b | -1.22609 | -54.17579 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b0cd9ce-783a-324c-a9d7-b144dce23f34 | -1.30383 | -54.67453 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d61aead1-591d-3132-856c-ad587444e8f2 | -2.59777 | -54.24701 | 2024-11-11 05:35:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8596ea35-e053-3ff9-8d04-8ef07fcfc224 | -2.06582 | -53.40968 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bd49e2b-960e-3f05-bb69-180038364926 | -2.06974 | -53.30409 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db913410-b7bc-359a-b82e-14f5a7eded0f | -1.6607 | -52.64279 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd1e274f-7076-3fc4-972b-1184b9a4d8f1 | -1.58278 | -53.73599 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c25015d-8962-3ebc-9182-33864bff81a1 | -3.65974 | -54.6579 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25f1f77f-4566-3776-aa67-a0d28c59f7f1 | -1.39856 | -52.36804 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b9af4f4-f5a3-33ed-8b93-e926036f7f34 | -1.38031 | -55.84644 | 2024-11-11 05:35:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18afbeef-5a75-365e-9d3d-7f904e6abe96 | -1.9767 | -53.13787 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02437725-4d01-3d34-8eb5-8eafd3244204 | -2.24835 | -53.66473 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678d1055-6197-38e3-9e92-9dccd5759f3f | -3.65499 | -54.65442 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6304afbc-b63d-36f5-9bf3-0079ac59f337 | -1.39338 | -52.36302 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc7988b6-9a5b-3b24-b18c-822e07936923 | -2.22189 | -53.67595 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f9a818c-4a81-301f-b32e-450f2ed5369a | -2.84359 | -53.99739 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 016bd14c-61e2-3488-b504-fb1acf191c3c | -1.52199 | -55.00082 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37a66535-c957-3e0a-9e7d-f41a25ea0d4c | -3.70312 | -54.61446 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5575291-c6b2-3737-a4b8-759ecf2221d8 | -1.25626 | -55.76646 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19c87f71-3cad-38ad-a59b-8c10790e8838 | -2.82142 | -54.00857 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcbcfe2b-d367-33ef-b7f5-178104ad9c8a | -3.10118 | -54.2932 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c975649-d854-3a13-baf4-f28f0601985a | -2.05983 | -53.4124 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c42f8b24-bfb4-387f-b6fd-73f44a73273b | -1.75873 | -53.74973 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07e95498-5b5e-3cad-bfd4-690d15d43ba2 | 0.83494 | -59.73886 | 2024-11-11 05:35:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c258fa0-ed59-344c-b8b4-0086d242a622 | -1.18344 | -53.92476 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 260468eb-0e62-3779-9b0e-739a2c53409b | -1.67156 | -55.17786 | 2024-11-11 05:35:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61d17c2a-b6f5-38cc-bb7b-007c45fd652c | -3.15305 | -54.48367 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad3668f7-e8ca-31bd-bc17-9348801c15bd | -2.81993 | -54.01064 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7971bcde-0988-37fe-84fc-890457854e36 | -3.69801 | -54.61328 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e077fe05-12e1-3a18-8707-3c906d021fef | -4.28506 | -50.67538 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6467b858-922d-33f1-a5c3-e4395d713793 | -1.48762 | -51.73817 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10a44eeb-409b-3731-832e-c1f999bab238 | -3.34477 | -51.65649 | 2024-11-11 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 516408e4-51fd-366e-bf62-a2f46f61af7b | -4.28816 | -50.67518 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56e3cd30-6c6e-3d4f-b671-1ee14fef0743 | -4.27922 | -50.66842 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e79ec7e-640f-397b-890b-31da58c2ea26 | -2.25338 | -53.74239 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 116a67e5-fada-3477-9206-73a9f0ca3f87 | -3.70222 | -54.62045 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b570e2d0-dce5-3d6b-8e32-344a81d8b739 | -3.1169 | -54.47792 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98b74e67-1804-3370-89d2-c4b6da7781d7 | -2.22675 | -53.68019 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6223093f-ed25-37bd-9eb4-bcbd46c7468b | -1.49366 | -51.73915 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30d7a18a-54c4-3b70-9108-64ec31eea3d4 | -1.40009 | -55.44588 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5b20e24-3e84-30d3-bc51-c2c15a75a1eb | -2.81711 | -54.00113 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cbaa856-7470-3391-a779-3519d9715996 | -1.6116 | -54.40474 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5d27677-0097-3a74-b5ef-72ee589d5ab1 | -1.51629 | -55.00561 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40db07c9-5781-3759-ae0d-f3b81687acd0 | 0.61116 | -60.08516 | 2024-11-11 05:35:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0d90fcb-b63a-3c7c-bdb0-2bb6ca234f7d | -2.73123 | -54.14169 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdcfa310-9231-3961-9375-30f08c61ddb7 | -2.27465 | -56.17076 | 2024-11-11 05:35:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc381253-8a12-3925-bddd-cdedfdc9543f | -1.56692 | -53.41775 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 514b2f17-c60e-3866-bc46-86709b5267eb | -2.24751 | -53.74498 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2964473b-f501-35bd-8a9b-7249c5b677c3 | -3.66448 | -54.66146 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 107730d3-f438-3ce3-a499-45ce7c56131f | -1.22379 | -55.79429 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1e8fd01-e596-36bf-ad4a-bdcaf4803053 | -1.60651 | -54.40402 | 2024-11-11 05:35:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15cabf8d-91ee-31f8-998c-e6acd8d36b57 | -2.22628 | -53.66487 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c77c205-14d3-3b18-a1c5-1cc4f7c4b7ed | -1.20699 | -53.70113 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e113219-eacd-3142-aa16-1119afb25561 | -2.31329 | -53.81708 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95735446-b8fc-360a-901a-de45a8becc70 | -3.10595 | -54.2972 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92b92aea-b4bc-321c-a986-1c8a866f30c2 | -1.40279 | -54.49876 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25efdee2-633f-337d-aacf-3f461e749eb4 | -1.51204 | -52.20496 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3349684-d16a-36bb-9de7-d307ba2d557a | -1.2565 | -55.76518 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76e408c8-8f1c-3485-a89b-94fc4fc09e49 | -3.69923 | -54.61654 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75f2c112-81ab-3567-a54d-c106cf5c608a | -2.22935 | -53.66326 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9094e2b-c896-3d44-b24d-70c502a6b2d0 | -3.18792 | -54.32169 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66f86cf8-c1c6-33a7-aef3-57a5df2d46d2 | -2.24194 | -53.67083 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2af238ef-1264-316a-9282-0c5d51a6d47b | -1.23232 | -51.7531 | 2024-11-11 05:35:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d29eb28-77c9-3218-b3f0-821ecd4f662c | -1.67315 | -55.17196 | 2024-11-11 05:35:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48612690-3c8f-38e9-b258-cb9be91c38a7 | -2.25388 | -53.739 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d2deb96c-e531-3e1c-b7c5-98776a5bb4d6 | -2.11847 | -56.18235 | 2024-11-11 05:35:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 066a3e5c-f8c6-3234-889a-63655e3c17b9 | -3.53477 | -54.08535 | 2024-11-11 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cf2508e-213c-34e9-9279-48ba222dd427 | -2.81606 | -53.99985 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3607f85c-2ce2-3bd1-8af1-3cb7c2b53a6f | -3.7047 | -54.65219 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63b2e593-8ff9-373e-963f-b361e95b2547 | -3.43656 | -54.53373 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7478d0ec-5172-3786-9f3e-eadd74fa0008 | -2.73171 | -54.13845 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f45fa8ae-fdea-3c47-b563-2bda54a5b68d | -4.28593 | -50.66938 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2320dc31-c373-3119-9be7-f4cea0cffc53 | -1.21224 | -53.63123 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d310d4b6-254d-3430-ab92-c5dd8b9aa49e | -1.61454 | -52.39478 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cfa194a-ca6d-37b1-b571-c006ef866cc6 | -1.34264 | -54.62609 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ee405e-61e6-3ddb-9048-29c9d3d30c23 | -3.02529 | -50.97594 | 2024-11-11 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f03e9d24-f6b5-369b-a06c-7edbf5cc73b3 | -1.34763 | -54.62675 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff7289a5-7fe4-372d-98ff-897f62536352 | -2.22779 | -53.67347 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bf0eda55-9711-3886-a08b-3a8fd30eb050 | -1.67234 | -55.17716 | 2024-11-11 05:35:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454b61b1-59fa-3a2a-8245-9fe872d23929 | -1.25576 | -55.76993 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bfe2f62-734d-3b03-ba19-c1013ba7ac2b | -1.38531 | -52.41642 | 2024-11-11 05:35:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5d45b37-a9d8-3d79-ab61-c44687288c9c | -1.39854 | -55.45589 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48e9525d-8feb-3cb3-8283-5e1019ffcbbd | -4.28148 | -50.67401 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a483925-6d3f-3f95-bb0d-af59deb59112 | -1.62955 | -52.53577 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cded3e7c-ceaf-3e55-bc28-7aaf8dfe564e | -3.35766 | -53.40763 | 2024-11-11 05:35:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f13af2a8-e85c-36a3-8a0d-c8fa46f5af4d | -1.63014 | -52.53176 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e57b3125-c5b1-33b5-b2bd-bec19a22b9d4 | -1.32489 | -54.60454 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 009a9335-ac4b-3c8f-bf82-66cb783d7855 | -2.23067 | -53.67256 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7964e3af-7da7-303f-a47c-7cd1dd82b600 | -1.32562 | -54.63785 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2f76c03-b757-3cd6-a156-0f2f39b3a9b5 | -2.22345 | -53.66581 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4008ced0-fbc9-30ef-9888-c9a869dc3efe | -1.62615 | -53.44338 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33973aa4-9ed6-3198-b90a-033bc08e8315 | -3.46239 | -51.58146 | 2024-11-11 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25415ffe-5c46-3937-9e8d-b8e2f3c14da8 | -3.51955 | -53.49976 | 2024-11-11 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1406f9ce-f4fd-3f1f-a0be-0fe16b4ff427 | -1.64185 | -55.2152 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0b4c38a-4d6a-3e53-a4a6-3cfe40f5cd03 | -2.24801 | -53.74158 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1762e676-4437-3307-9abb-618fae88517f | -2.22988 | -53.65985 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README44.md)
