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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a324e643-6930-3d16-84f6-7831ea94530a | -7.4541 | -49.4018 | 2025-07-24 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 76a39308-cd34-338d-80a4-993e75fa6b91 | -13.7169 | -45.6833 | 2025-07-24 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a489c751-17eb-31f2-a2f7-877c48ef51df | -11.2383 | -46.8699 | 2025-07-24 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 3a4a6630-aa2a-31eb-b8c4-563ac327dd2a | -7.2408 | -43.0664 | 2025-07-24 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| eec2edda-e0fc-3a6c-a195-08ebda9ab442 | -7.2405 | -43.0899 | 2025-07-24 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 00941667-751a-3ccf-b95f-f5acc7fb5242 | -7.4728 | -49.4004 | 2025-07-24 00:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 07c2e333-7141-3968-8a16-6c8154e401a0 | -3.1648 | -49.4648 | 2025-07-24 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 203.3 |
| 58a1256a-e7d1-31ea-84f7-a0a2b5b44eb9 | -7.2597 | -43.0645 | 2025-07-24 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 436.4 |
| 11033d1b-6cda-318b-a0f5-9d7ea0bc81dd | -3.2321 | -46.7836 | 2025-07-24 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1092eb7d-4ce0-36ff-91c8-786f7c79baad | -3.1649 | -49.4435 | 2025-07-24 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 239.9 |
| d95d7c53-bd40-3ef7-addf-6505bf89248d | -11.257 | -46.8899 | 2025-07-24 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| adb8392f-5e61-3545-82e1-c56e9af74fde | -12.4309 | -45.383 | 2025-07-24 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| ea3dcec4-403e-3c01-be26-4f8d1c59351e | -11.7317 | -48.1849 | 2025-07-24 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 52f9ada4-74a3-38c8-82ca-7dc39c49c6d5 | -7.2594 | -43.0881 | 2025-07-24 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 298.6 |
| edb81746-4b53-3966-82c8-601e36c7b41e | -4.7842 | -45.3282 | 2025-07-24 00:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 3181773e-237e-3f98-9ba9-12984b196805 | -13.7169 | -45.6833 | 2025-07-24 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| fd20327e-98d2-33ca-a6a8-9a9af2d7ce22 | -7.4541 | -49.4018 | 2025-07-24 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| eded9a7d-6de3-3af6-ad36-84f45ae10d7b | -4.0569 | -42.5118 | 2025-07-24 00:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 153.6 |
| 608a193e-31b0-3f40-8952-7f05e25f31e0 | -11.7317 | -48.1849 | 2025-07-24 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 7f96914f-2f2f-3181-b493-720324b638d4 | -11.2574 | -46.8674 | 2025-07-24 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9473214b-54f9-34b6-a282-65b3cf76e8ad | -4.0567 | -42.5354 | 2025-07-24 00:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| e6646b81-2515-39d9-9c2a-b08aaeb7a5bc | -3.1832 | -49.4642 | 2025-07-24 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 236.1 |
| b3b95cf2-1450-3837-a644-fbb5a05ff2c6 | -7.2408 | -43.0664 | 2025-07-24 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.3 |
| 194d93d3-fdfe-3184-9add-b87328035f46 | -3.1833 | -49.4429 | 2025-07-24 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 264.2 |
| 85a53d32-2b8f-31ac-b15f-61c1b6c6187d | -7.4728 | -49.4004 | 2025-07-24 00:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 31808fd9-9a4d-3bab-ad2f-99ddbf776dd4 | -7.2405 | -43.0899 | 2025-07-24 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 37c500f4-22c0-3c52-88a9-eb3fc08ba888 | -3.1648 | -49.4648 | 2025-07-24 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 189.5 |
| 23b4f474-d77d-3049-97ed-735748d46e84 | -7.2597 | -43.0645 | 2025-07-24 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 498.2 |
| 781d11df-1c09-3377-89a9-23888ace0908 | -3.1649 | -49.4435 | 2025-07-24 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 199.0 |
| 3f39dc04-f717-315e-b0ed-1c30a5d927aa | -7.4728 | -49.4004 | 2025-07-24 00:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 84b23a3f-8108-3466-8c78-5aa646af0e5f | -7.2594 | -43.0881 | 2025-07-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 320.9 |
| 0ac92d9e-b84b-31eb-af9a-94feba194e38 | -13.6975 | -45.6865 | 2025-07-24 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| dbd35989-b865-3477-acda-eedde1d02afe | -4.0567 | -42.5354 | 2025-07-24 00:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| be3d04fa-a0b1-30f7-bc21-07bba7191588 | -3.1832 | -49.4642 | 2025-07-24 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 225.4 |
| f8ba0285-b76a-3e53-896b-987432a79708 | -3.1648 | -49.4648 | 2025-07-24 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 207.1 |
| d9cdf67d-31fc-3dc8-a592-8affe4c7335a | -3.1833 | -49.4429 | 2025-07-24 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 240.8 |
| 42eb1502-c2eb-3b9c-855d-2f49688a9385 | -7.4541 | -49.4018 | 2025-07-24 00:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| baae1224-3ea4-3d1f-9b9e-2114bbf4f962 | -4.0569 | -42.5118 | 2025-07-24 00:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 127.0 |
| 06145272-9ea5-3580-8b8d-d3918683b8bb | -3.1649 | -49.4435 | 2025-07-24 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 215.4 |
| 72c73e22-e5eb-35ad-8457-f75eae25aada | -11.2574 | -46.8674 | 2025-07-24 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 9c2afb20-4ce9-3c29-b3df-fd571231ed6c | -4.0382 | -42.5129 | 2025-07-24 00:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 0fc9787d-3e0e-316f-b7f4-03ff764a0552 | -7.2785 | -43.0627 | 2025-07-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 3e9c24f0-e4fc-34d6-bda4-cfc69b0222f6 | -7.2405 | -43.0899 | 2025-07-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 8775b4d1-62eb-37b2-8678-4903e2eeed1b | -13.698 | -45.6634 | 2025-07-24 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 6ba77d19-64c5-3476-b03a-3cb884bbd710 | -7.2408 | -43.0664 | 2025-07-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 1f8894f1-72dc-30b6-bdcd-f0f69f3233b6 | -7.2597 | -43.0645 | 2025-07-24 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 494.9 |
| 4bfbf95f-7b4a-3eaa-aed4-a2335cce0708 | -3.1649 | -49.4435 | 2025-07-24 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 4de8103b-17b2-355e-bcd9-f583fd356d8c | -3.1648 | -49.4648 | 2025-07-24 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 7de01d33-64e4-3f7b-81b1-e6ce962092f4 | -7.4541 | -49.4018 | 2025-07-24 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f59534c3-00f1-3e86-a5e4-c6749c4eb2aa | -7.2597 | -43.0645 | 2025-07-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 393.2 |
| 2ada38d6-09ed-36f2-a76d-15f41a406582 | -7.2782 | -43.0862 | 2025-07-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 3c322dae-3317-3ae8-8e7f-2e5c5688c0de | -7.4728 | -49.4004 | 2025-07-24 00:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| ce245538-f259-3157-b1c7-003d013e2e46 | -4.0569 | -42.5118 | 2025-07-24 00:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 81ad454e-f3eb-3cbc-aef5-b302ebb0066c | -4.0567 | -42.5354 | 2025-07-24 00:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 3745bdba-aaad-331b-8a3d-2bf40a121de0 | -13.6975 | -45.6865 | 2025-07-24 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 2180e0a9-e27b-3a88-b5ad-1c62fc4d58d1 | -7.2408 | -43.0664 | 2025-07-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 51940e84-66c7-3c8a-829b-2026586f444b | -7.2405 | -43.0899 | 2025-07-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 505f53bd-ba70-3c78-8547-25aeba95e798 | -7.2594 | -43.0881 | 2025-07-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 358.5 |
| 4dbfdf29-7b14-39c8-85fd-8c9bf4bc8eb0 | -7.2785 | -43.0627 | 2025-07-24 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 88de6e0b-aeaa-3ff7-8207-df34d6adb15c | -3.1833 | -49.4429 | 2025-07-24 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 250.2 |
| 0cfe92d5-43ab-3f8a-b4d5-7719d6caa96a | -3.1832 | -49.4642 | 2025-07-24 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 264.6 |
| 92ed0d0b-a505-3c62-9627-0119afd9f439 | -3.1649 | -49.4435 | 2025-07-24 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| cda21e33-0354-3d4c-a935-4614d4b91b97 | -4.0569 | -42.5118 | 2025-07-24 01:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| a2bcd5d6-e703-301a-a419-1186b026b722 | -13.6975 | -45.6865 | 2025-07-24 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e3aefd9f-c9b5-310b-b631-b419ee7946e2 | -7.2408 | -43.0664 | 2025-07-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.7 |
| a812b9e5-5bc9-3063-859c-ea4bf1497e37 | -3.1648 | -49.4648 | 2025-07-24 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| a95acf7a-63ab-3692-b537-85a5cc0cb303 | -7.4541 | -49.4018 | 2025-07-24 01:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9eebf13f-7e05-38b6-bde3-99c01ba3c25d | -3.1833 | -49.4429 | 2025-07-24 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 24adb68a-a7ca-39f0-8e44-d7f4f0578be2 | -13.698 | -45.6634 | 2025-07-24 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 46d4d063-c3f1-3377-abef-8d5c8a0f29e9 | -7.4728 | -49.4004 | 2025-07-24 01:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| da85cbad-8052-3bc9-bc0b-2586c53dce31 | -3.1832 | -49.4642 | 2025-07-24 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 6ae01401-6d37-3149-8b19-931152835382 | -7.2782 | -43.0862 | 2025-07-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| f5b57e79-7a4f-3d29-a92f-2c22cf8776dd | -7.2597 | -43.0645 | 2025-07-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 371.9 |
| a7e2b104-6315-3acd-935a-4c4f116f3a7d | -7.2785 | -43.0627 | 2025-07-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 36bfa70c-1785-3e5f-b9da-6ad85af3223b | -7.2405 | -43.0899 | 2025-07-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| b9d141f5-e5e1-3c3e-a83a-829ce2a4ca65 | -7.2594 | -43.0881 | 2025-07-24 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 297.2 |
| c9697ba5-0ccc-3d4b-8808-bc9ead45b5d0 | -3.1649 | -49.4435 | 2025-07-24 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 57edc3fb-4574-3c25-9730-e680de39a266 | -7.2594 | -43.0881 | 2025-07-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 250.4 |
| 479b2521-a3a5-3e37-b22a-4dcb75a01c6f | -7.2785 | -43.0627 | 2025-07-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 8af23d47-6de6-39ea-9a7c-750b31cd83cb | -7.2597 | -43.0645 | 2025-07-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 317.2 |
| f1cef817-e44b-3db1-be76-8a65c2030e2d | -3.1832 | -49.4642 | 2025-07-24 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 240.5 |
| cc689c93-18ee-3230-8fbc-c9531d1b628b | -7.4728 | -49.4004 | 2025-07-24 01:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3ed333df-f513-33ff-9130-75a45059aabf | -3.1648 | -49.4648 | 2025-07-24 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 6ff520e0-1a68-319e-9bff-faadcc622ca2 | -3.1833 | -49.4429 | 2025-07-24 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 36e27914-16d1-36c7-b420-eed2616a69e1 | -4.0569 | -42.5118 | 2025-07-24 01:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 62430b71-3af8-3ff2-a438-baadc687fa2c | -7.2405 | -43.0899 | 2025-07-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| d6a287bd-2a0a-37a8-95f2-f2072bf724d9 | -7.2782 | -43.0862 | 2025-07-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 19ec0abc-0abe-31d7-84ee-c5a3d133b753 | -7.2408 | -43.0664 | 2025-07-24 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.6 |
| 40bd965f-ff63-340a-8984-70c6e69bcd52 | -7.2597 | -43.0645 | 2025-07-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 326.5 |
| 2d7324ca-5a43-3027-aed0-e8c8e0b6bc6a | -3.1832 | -49.4642 | 2025-07-24 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 224.0 |
| 9d304d21-8f44-3bf7-b2bd-c18a3303797f | -7.4728 | -49.4004 | 2025-07-24 01:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 73ea1296-e541-3adf-800f-546bceffca66 | -7.2785 | -43.0627 | 2025-07-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 0ef9d8a7-6b83-3533-9c33-f241e039eb44 | -7.2405 | -43.0899 | 2025-07-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| b5d9469f-d074-3993-a7b5-a34206bc60f5 | -7.2594 | -43.0881 | 2025-07-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 209.0 |
| 2657e2ef-a861-3043-aa7e-6e50ade51d6c | -4.0569 | -42.5118 | 2025-07-24 01:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| c5aa20ed-4ccd-300a-bdef-cda424611ec0 | -3.1648 | -49.4648 | 2025-07-24 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| b22c2eca-1cb1-363c-9a1e-71a1ad8288b0 | -3.1649 | -49.4435 | 2025-07-24 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 43293b63-1a04-3964-9e7b-102c3ff07b82 | -7.2408 | -43.0664 | 2025-07-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.4 |
| f213a9a6-1919-304d-8dd4-0d2845288563 | -3.1833 | -49.4429 | 2025-07-24 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 226.1 |
| d42783c6-3354-34c3-b4bf-a39d8dd7f9e0 | -7.2782 | -43.0862 | 2025-07-24 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |


[Clique aqui para ver as próximas entradas](README4.md)
