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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adaa7861-4bd9-3e5b-96a7-a1eedfa777dc | -12.97247 | -62.80063 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1141ccbc-47a5-37a8-afa0-fd10b3dc4a15 | -12.97223 | -62.78277 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3c14af5-3dc1-33f4-99f3-dbaad90a5cbb | -12.97214 | -62.67282 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7781a2be-cf2f-3b1a-8dec-b2aa30df6333 | -12.97167 | -62.78633 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bce79541-901d-35b1-b5b5-6f15ac5e79d5 | -12.97057 | -62.79347 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29001353-624a-3d46-9843-4272e8d15c3e | -12.97046 | -62.66154 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9871b69b-45f5-360a-8df3-76b8740be27c | -12.96993 | -62.68716 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0e4d712-b0d1-3a6b-9059-fa66af6927ff | -12.96724 | -62.79294 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa8a5559-ed60-3539-9b6a-46d1adca715f | -12.96717 | -62.70506 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb3ee377-842b-37e6-84bb-d0b5a853286b | -12.96669 | -62.79651 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 057f5e95-35c1-35ca-aa52-e6ac0f16ff06 | -12.9666 | -62.68664 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7e7d1dd-6465-3164-9417-3f591cfb49e0 | -12.96384 | -62.70453 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 451ab90e-4d47-3260-b63e-fd1d376cc3f6 | -12.96271 | -62.68968 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d4a774-6017-31ef-936f-27091461ddb8 | -12.96216 | -62.69326 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f3bfdb-9497-3399-80af-8bbdc8a3fbac | -12.95768 | -62.65583 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a303b452-4e18-38e8-80c7-a9da10b2710f | -13.01316 | -62.47293 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8fd0c94-4512-37e2-b841-9768ae15de62 | -13.00981 | -62.47241 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cc207c3-bde4-32c0-a503-112e8e150a70 | -13.00591 | -62.47549 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8a8a304-5f1f-3ddc-bc7b-accd2a8bd6c2 | -13.00256 | -62.47497 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bfecd9d-87bf-3b4d-a035-77d24a131a63 | -13.00089 | -62.48584 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da980090-7fba-38db-98f9-cbea50ed6d38 | -12.9942 | -62.48478 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16aac0ed-1cfd-3e17-86e7-577991033bef | -12.99089 | -62.50639 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 69d64f66-6202-32c2-ad9b-49330d6d5b7b | -12.99085 | -62.48425 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4973052f-c5e6-3cf6-8e0d-88bc898bdf28 | -12.98809 | -62.50225 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d231df1a-95aa-310d-8143-44c287584b85 | -12.98754 | -62.50586 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30f58951-3d76-3582-a055-865b00680c97 | -12.97864 | -62.51923 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be4c4c17-70ee-32dd-9523-805de06c45b0 | -12.94246 | -62.53193 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38bea92b-a2e5-3e8f-8078-0be6ce133017 | -12.93912 | -62.53141 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da6a5601-cab5-3589-a143-e405ee7ca8d9 | -12.93578 | -62.53087 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b809a94f-68b4-32d9-adcf-f6a0674757fe | -12.92964 | -62.52621 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18d4a1d9-363f-3b05-ba66-233d8e0c594a | -12.92909 | -62.52982 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2530249b-f78b-3e80-986a-a68f87820982 | -12.92854 | -62.53341 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cec2038-de1f-3d20-be02-399213abbba5 | -12.92016 | -62.52102 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43c99b7d-4ff8-3fb1-949e-b096c8b2c8c4 | -12.81077 | -62.45964 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9556ac3a-4641-36e3-882e-1aab862fd63b | -12.80223 | -62.45452 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff0b706f-9e99-3d7c-acdb-f6553f9d5745 | -12.77596 | -62.10793 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18eab181-6bdb-32f3-afaf-b33a9e86f43f | -12.76793 | -62.27486 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc47d2f0-a35c-3890-a689-b78f019e98da | -12.76737 | -62.27849 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17198e1a-bb11-319b-8e3e-ad5d2a97afec | -12.76622 | -62.26342 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5e471994-aca3-361e-8f48-26e7fb7b9401 | -12.76567 | -62.26706 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6cee2ff-d4b0-3e03-81cc-e201dbecaa8e | -12.76512 | -62.2707 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7fbf2aa-ba84-3b91-ba7e-c40066cf3321 | -12.76402 | -62.27797 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b62a6145-2c93-370d-b15b-86738e5bfcee | -12.76066 | -62.27743 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c52732a8-f6d1-338a-99ec-4afb0ec820bf | -12.75675 | -62.28055 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41823c31-0191-352e-b56b-e316612206cb | -12.71845 | -62.24881 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d6a190-26bf-3895-b703-0fb255a9919f | -12.7162 | -62.24101 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19b4fbaa-4619-311c-bd0e-2da624052327 | -12.74207 | -63.04097 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40aeff0-30cc-30b7-a971-f5350a90579d | -12.74153 | -63.04451 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2c4a26d-34ea-3fdb-bc76-a6acc0861bdb | -12.73876 | -63.04043 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f517ef5-76aa-3e31-9cf5-b21468e947cf | -12.73599 | -63.03636 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89e17a5d-f4ba-39b4-b50c-999efa38885a | -12.73545 | -63.0399 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32634340-6a4e-3bda-b1fc-59037f971ecf | -12.73213 | -63.03937 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2925e889-f246-3218-96f1-50a15aeab6b6 | -12.72389 | -63.07067 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5276373d-53b0-303b-9026-65d8d32b0a00 | -12.72334 | -63.07421 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ababb3ee-3985-3d23-9e02-1d103eb23314 | -12.72328 | -63.03069 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cabf4af9-3a6c-37b6-985a-6439edb38612 | -12.71996 | -63.03016 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa539509-a317-3dbe-bc93-f1984dd30952 | -12.71616 | -63.07668 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0d3e496-cce1-329c-9c32-f3f2b5b8bcb9 | -12.71557 | -63.03651 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ef11388-d0fe-34e0-b997-abf1c0fbaf41 | -12.71226 | -63.03599 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffa54c6e-019b-3819-b8c4-d5cc7f9bab6e | -12.70949 | -63.03192 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8539f1a9-7200-34e0-a01e-282d82e8736d | -12.70894 | -63.03545 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47f35a7c-7d25-34ba-b512-be6a3f03d5fd | -12.70839 | -63.03899 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a74cb15a-e4e3-315f-a66d-391c3fa5825a | -12.70618 | -63.03138 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b9229b2-220b-3799-9b2d-895afed00d5d | -12.70563 | -63.03492 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e3fc1d4-ba63-3e85-b802-37d1c9802eae | -12.70508 | -63.03845 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2c359fe-5535-3ea5-90d3-db2c73394fb6 | -12.70286 | -63.03084 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 85047812-e908-333e-afba-7fa3d11c95e5 | -12.70231 | -63.03439 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71d692ab-b5ec-3fa3-a5fb-764a5afb11b7 | -12.70176 | -63.03792 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 607f4456-5120-379a-9808-ddfbc76d6ecd | -12.70068 | -63.06673 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3943f162-0966-3900-9ee0-d9267628b3ff | -12.69955 | -63.03031 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b7bf072-c3f4-31aa-93ac-f372872d00e2 | -12.699 | -63.03386 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93cbaf74-de8f-3080-b806-733bbc364311 | -12.69845 | -63.03739 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94d2e7ec-bb20-3835-a489-8e2806fd3de3 | -12.6979 | -63.04092 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53fc0d69-72f0-3a1a-a860-0b2707dae9a0 | -12.67638 | -63.07008 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7290684b-6635-333f-8d7f-686a1e7ed0a1 | -12.67583 | -63.07362 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1bb4c8d-ae01-3b67-a57d-5acc66f74b25 | -12.66534 | -63.07555 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cabf1b87-45ca-33d1-a16c-1e8767ee8841 | -12.66479 | -63.07908 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ec199ad-7909-3a66-87e6-9c8e56f32e40 | -12.66148 | -63.07854 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 726d5da7-94d2-3195-b7b3-2185886a86e2 | -12.50991 | -63.26745 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f553f55-2d4f-39a4-b882-916759306729 | -12.50715 | -63.26339 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 350d9975-fbaf-3b61-8afe-f0b963f0e64a | -12.5066 | -63.26691 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72f79ae5-170a-3845-9dea-f36b55225af1 | -12.50605 | -63.27043 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ae2bd22-82a5-3d66-a67d-96c06e084b1f | -12.50329 | -63.26638 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55b65e71-94dc-3ff3-9519-aced16ad67fc | -12.50274 | -63.2699 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63207695-5e58-3f81-aa51-d3c638d3bc81 | -12.99897 | -62.73897 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eb3aaa0-51e9-34f3-8d69-d705c97c27b3 | -12.99673 | -62.73128 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 499ef0a0-51da-339a-b4e8-ed41772791fc | -12.99618 | -62.73486 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 797eb025-5fd9-3331-b563-a538015de218 | -12.98351 | -62.77312 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60c35396-ba2e-3f7f-b586-3ba6e430d993 | -12.98346 | -62.75115 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d29b607e-0bf3-392c-99ef-037cdaf73abf | -12.98341 | -62.72915 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43463f67-3fb0-37fd-8e94-571fc8affd3f | -12.98018 | -62.77259 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 708061e2-4a0c-3e92-bcb1-6fd40302411b | -12.97963 | -62.77617 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fef421c-1a42-301f-b91d-ee8706aa414e | -12.97829 | -62.7215 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d1217ce-b1d8-3a57-9487-ef0a4404fae7 | -12.97773 | -62.72507 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 089c2409-bd97-3fac-a5b7-c21c91031aa4 | -12.97278 | -62.7792 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb7b0182-d747-3a68-a24b-d92ce0d856c8 | -12.97269 | -62.66925 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72ee2f39-8caf-3655-93ee-c8cd05a6cab3 | -12.97112 | -62.7899 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a83287b3-e265-3e48-909f-c2f53f83037f | -12.97048 | -62.68357 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ba49dbc-9251-36fa-b2c6-ea790176a40f | -12.97002 | -62.79705 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d872ba47-79bd-3af0-82eb-a0e1eed9bec4 | -12.96947 | -62.80061 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README107.md)
