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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6cbc511-2207-3b6c-bb8c-7832cc6d6062 | -7.0799 | -59.1964 | 2025-08-11 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| bd4edb34-221f-3cf6-84f5-0551bfc7ab33 | -7.0614 | -59.1972 | 2025-08-11 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5114b503-6d23-3a38-a9aa-19bea33bec49 | -6.5856 | -44.564 | 2025-08-11 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| faa85436-e6ac-3986-9ccf-24efb2170bd5 | -5.5013 | -44.3726 | 2025-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| dfe75087-dc08-3fb8-b3af-b92a285fe73b | -8.9401 | -60.7288 | 2025-08-11 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f73e24d7-5995-37a7-980d-f9479a5e97ee | -5.4825 | -44.374 | 2025-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 990fce59-1d1c-3562-9a18-f99cf4b1f539 | -7.0613 | -59.2165 | 2025-08-11 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 91622e29-c52a-35f6-bd4c-1dcd2bcf9782 | -5.5011 | -44.3956 | 2025-08-11 03:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 5f32dec7-b7a3-3ed1-af32-7a5a621c9974 | -8.9399 | -60.7481 | 2025-08-11 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 4ff27577-4d9b-320a-a35d-4911c0dcd463 | -5.4822 | -44.4198 | 2025-08-11 03:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 614e1870-4120-306a-a298-c6a364a8c7df | -5.5011 | -44.3956 | 2025-08-11 03:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 53b35453-5633-36da-8e15-10539db6dc60 | -5.5013 | -44.3726 | 2025-08-11 03:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 5bfac88b-80e0-3912-94fd-d30e265055f1 | -7.0614 | -59.1972 | 2025-08-11 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 3b574140-8fc9-362f-9911-6a288d9c6e95 | -15.4216 | -53.9073 | 2025-08-11 03:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0dc5e5e0-6ac1-3a7b-aba4-1708d7f204ab | -8.9399 | -60.7481 | 2025-08-11 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c47e3c68-c6f5-3d41-8ddc-812fd00d8979 | -8.9401 | -60.7288 | 2025-08-11 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1966f4aa-f3b8-3ba3-9176-dcce750cdcfc | -5.4824 | -44.3969 | 2025-08-11 03:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 342.3 |
| 86de6f99-b08e-37b0-8798-24367ae82702 | -5.4636 | -44.3982 | 2025-08-11 03:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 1a1cc482-f0a9-32f1-b02a-7b2713de38e0 | -7.0799 | -59.1964 | 2025-08-11 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 578d61da-9741-314d-a2b9-9fd09f2228e9 | -7.0613 | -59.2165 | 2025-08-11 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c8ccb4eb-9b37-3822-a47d-0472724638dd | -6.5856 | -44.564 | 2025-08-11 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e36357a7-24d0-3f03-b21f-ef5e045a69ea | -15.4407 | -53.9258 | 2025-08-11 03:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 3ed82a79-a046-3018-83df-224ce0174e7a | -5.4825 | -44.374 | 2025-08-11 03:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| e8f29c4e-63db-374c-bf96-57f611d4c9ec | -15.4212 | -53.9283 | 2025-08-11 03:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| eca646f0-f019-324b-9251-a30a5c0b9107 | -5.47933 | -44.40054 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c039bd34-7e5e-3c24-aff4-93aca60a6c18 | -6.57206 | -44.57679 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 00b21435-8e09-3bca-bdba-7ab5c605c000 | -7.16902 | -44.27551 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e7d31030-64dd-38f5-940a-565906e353ca | -6.92821 | -42.96405 | 2025-08-11 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 89bffd47-695c-386a-b615-f5af1c784843 | -7.1761 | -44.27722 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 153e64c3-7f06-3a7a-9719-412a8bc65358 | -5.48161 | -44.38757 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 8e10c9f7-51bb-38ce-852e-e63ffb0e6c13 | -7.16949 | -44.281 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a30f18c1-8cb1-36bc-b934-e48738a50634 | -7.62049 | -45.19127 | 2025-08-11 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26c69933-348c-399a-9a32-a003168eae67 | -6.65902 | -40.92017 | 2025-08-11 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4c533942-036a-3535-a94d-df109d87f6b3 | -7.36551 | -44.85159 | 2025-08-11 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a944c125-65f0-391a-88c5-f0c4f5fa8aad | -5.4801 | -44.39619 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6e219f38-a898-357d-8131-51534ff3ff43 | -6.57867 | -44.5633 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 481089c0-49fd-3421-9cd1-73be7c202fd7 | -6.57506 | -44.55972 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 562d00ea-1a16-32e6-8ec3-f83730f2043d | -7.36803 | -44.85772 | 2025-08-11 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 784f234f-9a8c-3dc7-b104-364a24182923 | -7.17044 | -42.93852 | 2025-08-11 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b97fdb24-24f3-38b0-9ac1-7527b1e4509d | -6.92761 | -42.96748 | 2025-08-11 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bd72d876-96b5-3e67-a514-becfab831c0d | -6.58022 | -44.55486 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 08fa8ca7-ff90-3272-b9e2-49d24266536d | -7.17028 | -44.27671 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b5470f2b-d1b1-34f8-baba-32eac87408cc | -6.59191 | -44.55735 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3eed2ae9-d2cf-33cc-84d2-77ac3a801404 | -5.27607 | -37.67965 | 2025-08-11 03:36:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6be3baa6-69da-3ebe-9aeb-85d4a465e273 | -5.49272 | -44.39391 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 95b3dd9c-42a8-3a6f-9bb1-f083d7bb7f55 | -6.58167 | -44.55662 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2af5ed91-0157-3a24-926a-af9f6027cb23 | -6.57792 | -44.578 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4c6af2e4-45cc-3475-a603-c5e2b06f7112 | -7.35961 | -44.85042 | 2025-08-11 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b08143db-21a9-3901-b86f-fa2e4f497f41 | -5.47857 | -44.40489 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0986173b-92c3-3ec1-bfa7-d7e46e34cad4 | -7.61626 | -45.19088 | 2025-08-11 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d9772c7b-402a-31d1-816a-fda12971374d | -6.14384 | -38.94556 | 2025-08-11 03:36:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9bc48051-d62b-3da7-97d0-89d505c376c2 | -7.36473 | -44.85597 | 2025-08-11 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52549646-54ad-3fa8-9694-6999cc914fcc | -7.17102 | -42.93523 | 2025-08-11 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c366418-932d-3416-935a-3ebe905a56fb | -6.58373 | -44.56891 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 87160969-a634-3289-9be2-df61d5563f2d | -7.16825 | -44.27987 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ae7b98f3-6309-3052-8f01-6b6de468ef84 | -6.58018 | -44.56516 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a1ab6ff3-9a1d-3643-aafb-1ed74f52f6e2 | -7.17674 | -42.93355 | 2025-08-11 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a568c245-3b2d-35a2-9a44-f46b1a8161ab | -6.5927 | -44.55302 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4c330474-841a-3a1f-b8e9-966cd2cd2dc7 | -5.48452 | -44.40582 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8b49906-eeab-38e1-ba4f-9aa6373c52a8 | -6.58451 | -44.56462 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 665ecfb8-4a9a-39dd-b0dc-b065cc0de3cf | -7.87591 | -44.96994 | 2025-08-11 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce289a15-daa7-3a10-aecc-bfe2577fe467 | -7.16297 | -44.28425 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38270945-f593-3cd8-a447-94db5d348009 | -7.87514 | -44.97419 | 2025-08-11 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b5c86f38-591c-3b3d-900e-628e158eda3b | -6.5771 | -44.57188 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 278d099b-38f2-315d-b279-11232ae30a54 | -6.57579 | -44.55552 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b4d0488d-214b-37b9-b650-d71d8aa3ac9f | -7.17108 | -44.27235 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6bb28d85-fc5d-3d9c-86c4-7aa9209fe202 | -5.48604 | -44.39717 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 90f110c1-ba9e-38bf-b3b6-873b54b2a1b2 | -6.57867 | -44.57373 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 12d45eb8-4916-3fcf-b65e-0dfa1a50f04b | -7.1637 | -44.28032 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30b858ac-2395-3cfe-ab94-82bd7261e95e | -6.66399 | -40.92352 | 2025-08-11 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3266a010-33a5-33a3-99ca-6e1d62c1bf36 | -5.48755 | -44.38853 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 3b5d1720-bb79-3673-81a7-5e42d5c69297 | -6.57632 | -44.57615 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 41c2afac-facb-3f1e-9503-67ab15491cdb | -6.5853 | -44.56028 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5be85265-e103-3482-9668-5fb1f9b35659 | -7.36295 | -44.85217 | 2025-08-11 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f40a355-0558-3d1b-b137-177a6189be67 | -7.16176 | -44.28316 | 2025-08-11 03:36:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77edfaf7-04a5-349d-9775-0c3f072da778 | -6.57431 | -44.56396 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 55233065-7848-3a1b-8997-8da6658b5134 | -6.57945 | -44.55907 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 6e00b87c-729b-3c0a-ad0c-a9709ccccbaf | -6.58093 | -44.56087 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e60b5dc3-a41a-3a8b-9c08-15b0427b0729 | -6.5861 | -44.55591 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 889d53df-e6d2-3d12-82a9-4c56224450d8 | -5.48085 | -44.39188 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 751a552d-b165-35e9-b72d-2e208244de1d | -6.65937 | -40.92272 | 2025-08-11 03:36:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1d8cc0a-0abf-38d5-b26e-a2560d820938 | -5.48528 | -44.40149 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 63a6927f-d5c0-3fbc-b0cb-1253727eee49 | -7.17089 | -42.93594 | 2025-08-11 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 515ccf6c-239c-34e6-8499-242803a1b60a | -6.57942 | -44.56946 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a6929a9e-c828-3d14-adde-7235d5a2818c | -7.62234 | -45.19166 | 2025-08-11 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 18380741-4cb0-3d2a-b637-54899c3a2e96 | -6.57356 | -44.56824 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8f6fb73f-b94a-3367-90db-c09c4e0d1482 | -7.18198 | -42.93446 | 2025-08-11 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d5ecbe7-251c-3de8-92bd-b6a84d9a84fb | -5.4883 | -44.38424 | 2025-08-11 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ef31f8e3-bff6-3c90-9eab-c88e280d3486 | -6.57789 | -44.5676 | 2025-08-11 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5aa2b5a3-76c7-337c-a6f9-52faf56dd51f | -10.42207 | -46.25293 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebf19813-09f6-37a7-8567-5dfe130b2446 | -9.63192 | -40.58782 | 2025-08-11 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 924df234-4cf7-30ea-b0bb-ee285c455a09 | -7.87407 | -44.968 | 2025-08-11 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3694fae6-95de-3099-a523-514ccbaa5b57 | -15.09779 | -46.53848 | 2025-08-11 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f4b6497-103e-3e86-afa4-c97f0b9e6897 | -8.30191 | -44.98709 | 2025-08-11 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0fc13c6-2950-35e3-acbc-9b39a963ae95 | -8.30276 | -44.99086 | 2025-08-11 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e4d51e4-e1c6-35d4-afcf-46f9169b867d | -11.94943 | -43.39217 | 2025-08-11 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 379c4e20-128f-380d-9c9d-011ea8bcacab | -9.21019 | -44.52502 | 2025-08-11 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2befbc99-884e-3994-8850-6df29a9e2244 | -11.94391 | -43.39419 | 2025-08-11 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2e220f3-76f5-3a43-a707-10de0968f34d | -14.48418 | -47.07373 | 2025-08-11 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7324cdda-36e3-3398-9462-5b9edf1a4b30 | -13.33864 | -43.37719 | 2025-08-11 03:38:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |


[Clique aqui para ver as próximas entradas](README8.md)
