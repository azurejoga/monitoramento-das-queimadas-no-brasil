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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91def279-6b44-3691-9ce6-0b9fe76eceba | -3.86904 | -54.2311 | 2024-10-05 05:29:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c532e00-cc51-3e4a-8d1a-7fd04edaddd8 | -7.9449 | -54.76483 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b75feb3-76a3-3425-bccb-f8dc9b1da79e | -7.90153 | -54.7634 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04250b48-f3e3-3c7f-8ae8-6449c52cc04f | -7.90147 | -54.75865 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7fdd907e-9670-339c-9c7e-f4fd5f5d365f | -7.89898 | -54.74668 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ae87543-d55a-305f-8fcc-5c7b73b45def | -7.89808 | -54.74725 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f75bd6e9-57fe-3109-90ce-16a7ca5e9850 | -7.87978 | -54.88398 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 931cc084-ab61-3837-a2db-e56ab22c5f3a | -7.8764 | -54.8728 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 96b1f8fe-7993-3ee4-9490-fdaa436b03c8 | -7.87633 | -54.87199 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a73b56ba-26a7-3c34-98ba-1c840edef928 | -7.8757 | -54.87802 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a325a53-36d7-3d9b-bc05-bb77c3a89978 | -7.8756 | -54.8772 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e8ddae32-16cf-3409-aa1f-5594a6e809be | -6.87093 | -55.12112 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d778fbfd-4e3a-3790-800f-90d8a1ab000d | -6.67532 | -55.37496 | 2024-10-05 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4762536-1789-3c4c-b8b2-b4fcfce9057e | -6.58349 | -55.39142 | 2024-10-05 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef096fdc-caa3-36a1-a94e-b85537f70575 | -8.51296 | -55.15245 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6212e16d-92a8-32c1-b907-af19a91e6a15 | -8.51226 | -55.15763 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cf5d1efe-7417-32a8-b829-6c4c73acd1e7 | -8.4487 | -55.45301 | 2024-10-05 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffcc56a2-a317-3e25-821c-e760c12b77a4 | -8.27835 | -55.10883 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d73d4e5-8376-3101-8db8-3d4a218fb786 | -8.27528 | -55.10536 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f53801e-0c60-3cfe-96d2-e6be06863391 | -8.27459 | -55.1105 | 2024-10-05 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4837658-c3ed-35c0-996c-9b450a4f64de | -8.18211 | -55.21368 | 2024-10-05 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e550235f-ce36-3467-a3e0-41f498002b35 | -4.70719 | -55.98757 | 2024-10-05 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6fb9c151-7c38-3aee-bbb1-c08e30b8b5d5 | -4.70677 | -55.98899 | 2024-10-05 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 209042ec-424a-30e1-a1c9-51a3bf63c9fb | -4.05729 | -56.2817 | 2024-10-05 05:29:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faae31fb-24f5-3faa-8957-d9a4f294e33d | -5.23707 | -56.06166 | 2024-10-05 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a300248-f9d0-39c7-96bd-b34f8caef876 | -5.23689 | -56.06229 | 2024-10-05 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9fd01a1-0460-3b51-b7b9-cea32e68c09b | -9.44315 | -57.83112 | 2024-10-05 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52e68b86-37e5-3f55-b902-1bc9a48de255 | -3.47969 | -57.85408 | 2024-10-05 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfa98d84-5c9a-3a89-9f44-31bb3ff3f51a | -5.79432 | -57.52932 | 2024-10-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aa48242-bf58-3df9-930e-537a6c3a5bc8 | -5.73539 | -57.54367 | 2024-10-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f500e09-3a0a-358f-ae53-208c2dcee113 | -5.73152 | -57.54311 | 2024-10-05 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67081b46-9f19-3f58-a56c-a25b1a841413 | -6.96999 | -59.07124 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7cc5dbff-edc8-3615-8b94-162667c8944f | -6.967 | -59.06653 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cb51287-6b62-3ddd-a992-f076c59ed77d | -6.96639 | -59.07069 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a38cf117-3e6c-3525-8830-25662aadc814 | -6.96577 | -59.07483 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 24609a13-fb7c-3d34-a58d-e773b036fe65 | -6.9634 | -59.06598 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a0d79d8-f3be-3cfc-95b0-1553fde03217 | -6.96278 | -59.07013 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1cd6525d-f892-3893-b3de-9861505f98f5 | -6.96217 | -59.07429 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e1d80db-d83c-3f01-8ff2-a4b86b10cbd4 | -6.95979 | -59.06543 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5151cae2-e8d5-3333-a2e9-7588709c4b39 | -6.95918 | -59.06959 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f487ad68-9cb5-38a9-aeb5-474b9080eaa1 | -6.95848 | -59.06279 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4ba6ed64-afa5-3138-93c4-c74696e62af0 | -6.95785 | -59.06694 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9d46c9e-1420-3132-b10e-438869b7d8ee | -6.9568 | -59.06072 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d0e0c98d-ea72-3c89-819e-a9518140ca18 | -6.95618 | -59.06488 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 28b4cd92-10eb-3774-adbb-4d9ae5adb59d | -6.95557 | -59.06904 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfc1916b-9ec9-372c-93af-b1277147930e | -6.95488 | -59.06225 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1912412e-977e-3c2b-99ce-3326e31dcf08 | -6.95446 | -59.04082 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbc7894d-4730-3786-9ba9-1452a2c9721b | -6.95424 | -59.0664 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 86b47f32-05f9-3be3-89ae-3602cc62bca4 | -6.95361 | -59.07055 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c15f556a-5bda-3515-a050-b284e804efd6 | -6.95319 | -59.06017 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2fa28ea0-f3f9-3ff7-9d58-7d0d363eb1b2 | -6.95258 | -59.06433 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 606eaa15-d363-3e1b-b61e-2d1c3dec0ab7 | -6.95197 | -59.06849 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8a95dc2-b47c-39b4-abdb-d95a664efa0a | -6.95191 | -59.05753 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1789dd4f-ee8f-3308-af46-ada9bb8eaecd | -6.95128 | -59.06169 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 016f178f-6217-3726-ae69-7a28c2bb3e37 | -6.95064 | -59.06585 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1b63b332-2c59-3975-8726-b9beb94b5c27 | -6.95001 | -59.07 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f80c2098-f6cc-3b27-8a10-343bc2e06281 | -6.94768 | -59.06112 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fae04051-c6fe-3799-bea3-f00b0404a8b2 | -6.94704 | -59.06529 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 921bf814-fe62-3e68-9dbf-5c8c6a270aed | -6.94641 | -59.06945 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7218520f-7c0d-34ac-ac10-5d39563730f3 | -6.94407 | -59.06056 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61a70552-2036-3d39-950a-68aee1d75bb7 | -6.94344 | -59.06472 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d3e5f46-d695-3be7-96e0-6be142ad0eef | -6.94281 | -59.06888 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8b01863-df99-3257-b057-000dc042241e | -6.76434 | -59.06873 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22e8f5d-b58a-3409-8099-3a7c38a2b17b | -6.74697 | -59.06183 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c27c82c7-cd35-3589-9f4c-6afa3f4d8312 | -6.59856 | -58.62138 | 2024-10-05 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d860c7b8-e8d7-301e-8985-155a2b3d1f1f | -3.53148 | -59.39962 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 050f6721-4665-34bb-9dbb-7fdebf7c70e5 | -3.10711 | -58.56456 | 2024-10-05 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e085e01d-b743-32a1-b4a6-b5d8dc4c5543 | -3.10137 | -59.36582 | 2024-10-05 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95535b1c-c3d1-378d-b454-c02fd44df275 | -3.10079 | -59.36953 | 2024-10-05 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 348f26b7-6c89-3718-ab70-a484a579ea1f | -3.09795 | -59.36531 | 2024-10-05 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef724430-1fb9-31aa-bd23-cc410ebff2de | -3.09452 | -59.36479 | 2024-10-05 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9cd9d33-946d-326e-8aac-853081baca7d | -3.09394 | -59.36849 | 2024-10-05 05:29:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32b42ffe-2c82-3f49-a034-ad6d5ad11cc7 | -3.02265 | -59.39925 | 2024-10-05 05:29:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 717d4c96-6231-3343-b935-15d68451ea16 | -4.29187 | -60.0176 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7eb67f9-0f7f-3c44-b824-3f49817ad7ab | -4.2885 | -60.01708 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95bd04cd-8968-3700-a17e-316fa37cbc05 | -4.28793 | -60.0207 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76ba502f-8835-3a97-9b18-f02c274453b6 | -4.28512 | -60.01656 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 980541c4-1845-39fa-bebc-41fab2e1c012 | -4.28455 | -60.02018 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08590120-169b-3c87-b32a-e00be538fb37 | -3.8722 | -59.73798 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7c05ef7-6dbe-39d7-a2f3-36cd96d95d83 | -3.87163 | -59.74164 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f3f464a-7086-3c6f-9801-5254c48329ec | -3.86823 | -59.74112 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27589318-fb6e-3d9d-a6e1-23853bf987eb | -3.86483 | -59.7406 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21109b51-675b-38a5-8aa3-6d879d522b91 | -3.76285 | -59.33453 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42086ab9-918f-3cfe-9c2a-d334b183fc33 | -3.76233 | -59.33376 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa492150-daa7-3a9c-992c-de475d4df2d3 | -3.7594 | -59.334 | 2024-10-05 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2625e44b-2be6-38ba-ad80-46250dbd110e | -7.37508 | -59.79762 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b297a121-cb5c-3ad5-82ad-05f0c7fb0d6a | -7.37449 | -59.80151 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdc07769-8b6f-37c5-ba11-994bf4bf4df7 | -7.20711 | -59.61934 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90eeebb3-d639-3c3f-a269-6b802ab4dc51 | -7.20419 | -59.61477 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee0eae4-8ed1-366f-b9d8-ea71ecee761c | -7.2036 | -59.61877 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aa6eadf-976f-3968-9250-e43f614356e1 | -7.15326 | -59.29976 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30308cd3-2d33-3515-b989-3b59be2186ee | -7.15265 | -59.30385 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3fe65e1-3015-346e-89a7-afca281807aa | -7.15072 | -59.36597 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 799baf4c-93bf-30a0-8427-4c1d0a1088c7 | -7.14969 | -59.2992 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 534c32c1-d60a-3a85-8dcc-151c8e232704 | -7.14908 | -59.3033 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9817d13c-f98d-3843-8df2-1c5f9b83b705 | -7.14716 | -59.36544 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bc50fdfe-12e4-3a18-b02d-5003d56478d8 | -7.13959 | -59.2993 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b973f397-25bd-339a-a4fb-d76eb7406090 | -7.13954 | -59.31853 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6be21942-cdd6-3868-8c89-fad510901e12 | -7.13898 | -59.29757 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85140cb7-8b24-3a8f-af5a-0da5926298ec | -7.13897 | -59.30339 | 2024-10-05 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README134.md)
