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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4423345-81af-3f45-84bc-bb7b2e1adb7e | -1.69217 | -52.437 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 71d8ceeb-63dc-3f32-9fd9-f2a689883122 | -2.29598 | -50.58727 | 2024-11-29 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 904ff130-58db-368e-acf2-c87f8f69d33d | -1.26898 | -52.18913 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6b4e94f5-d10a-3c0c-8394-55304abc73c4 | -1.04431 | -51.73253 | 2024-11-29 05:42:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f204b731-3fce-3989-bca5-94e65b2088b9 | -2.01955 | -51.19836 | 2024-11-29 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76630a38-1fd0-3187-83d9-333b8bd68efd | -1.1578 | -53.58094 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| fadc5809-bf81-3815-ab2c-6afce7a33f77 | -1.53269 | -51.60923 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c10406e-ba6b-3260-a108-c7d756ed6e6a | -1.21431 | -53.55339 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 00d3af9a-2cd3-38ce-bd02-b35e4c4e230e | -0.95353 | -51.65497 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 380b5791-71fe-38d0-9b82-161589e41e17 | -2.0209 | -51.18933 | 2024-11-29 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 65241bf3-3b6d-35ce-ae0c-d61ef6d860c6 | -1.69372 | -52.42686 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd0a094c-a336-39b7-8731-4ab8a1024f2b | -1.19583 | -53.87014 | 2024-11-29 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| a05ab6a5-02a3-3fb3-929c-8d56089834c3 | 0.97855 | -50.13055 | 2024-11-29 05:42:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7e7b8858-9c8d-37b8-94ca-d289e0dcabca | -1.70008 | -52.44854 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 5ad66cd0-c8e1-399e-8a60-70ed059dd62d | -0.27429 | -51.62907 | 2024-11-29 05:42:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d189c116-34cb-3817-9f50-97a27a4d7bf1 | 0.98609 | -50.12043 | 2024-11-29 05:42:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 93c54379-4447-312e-899b-df341d6d573b | -1.14595 | -48.33677 | 2024-11-29 05:42:00 | AQUA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0bf8401d-c340-390c-83c0-a26b2d5d1d38 | -1.09643 | -53.38401 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| b438f65c-ab4c-3e9a-ad97-7ac6ab337ed3 | -2.65707 | -48.78582 | 2024-11-29 05:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 177.8 |
| d7d30d4a-5cbe-3fa3-bcb0-3011c1c7c9bc | -1.72386 | -52.48323 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c8308ad4-36d0-37b1-a248-e9852b343df6 | -2.66756 | -48.77778 | 2024-11-29 05:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 49c292f1-3031-3de9-81c8-898434c9ec70 | -1.59764 | -52.28705 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 3027c922-561f-3bf6-b422-5777f00186b1 | -1.68906 | -52.45732 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5033d5b9-8f1b-3532-8894-95c0def2609f | 0.9411 | -50.73859 | 2024-11-29 05:42:00 | AQUA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f1d31e05-e80b-3bb7-bffd-76f06d815956 | 0.97938 | -50.25735 | 2024-11-29 05:42:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 564267b6-c221-3f8c-ad23-471a3fb0f2cd | 0.93974 | -50.72946 | 2024-11-29 05:42:00 | AQUA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ba8ede3f-7704-3351-b537-043218fff7b2 | -1.36181 | -54.654 | 2024-11-29 05:42:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f4bc3ed2-ce35-3dbd-833f-c1c767703a8c | -1.67811 | -52.52879 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6a30edfd-4438-33b2-a54c-b1fbb79eef18 | -1.67922 | -52.42831 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eed8c2d7-7146-3e2b-85b9-ccf33eb2302d | -1.58825 | -52.28567 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c689ffbe-5b17-337f-a95f-bd3e533d2fa9 | 0.33489 | -49.7135 | 2024-11-29 05:42:00 | AQUA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3517a5f3-156e-3dfe-ab5b-f713ad8c06af | -1.60703 | -52.28843 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| be88e4d2-562d-3d61-983b-adfb73467961 | -1.0863 | -53.38255 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 04f7f41a-0fa4-3f37-80c6-feea5734efe3 | -1.71048 | -52.76781 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 54812246-1832-3dae-9acd-d6ff1802fdb5 | -0.56807 | -51.70093 | 2024-11-29 05:42:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| baadd791-0e40-3702-983b-2b0b5e5f8adf | -1.66709 | -52.72906 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ebc9d7ab-69b3-3691-a693-0d3d1c6017b4 | -1.68427 | -52.42548 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c0a4ba4e-6078-3231-9304-0040d70bf6ad | -0.95494 | -51.64548 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 94ac6521-c379-39b6-bb32-d0760c0c5de6 | -2.69498 | -48.65671 | 2024-11-29 05:42:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 35988b6b-15fc-341b-a798-e2c5ddd07ae4 | -1.58036 | -52.27429 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f27a416-118d-3fe4-8b11-957652c9d400 | -1.15965 | -53.5689 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 02bbbf08-9ff7-3d64-81f4-c045fca59468 | -1.09467 | -53.39555 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a98e3a83-aae9-3946-ba4d-4dc59df1d464 | -1.72231 | -52.49345 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a96e0572-f5f9-361c-b12f-bfa018bbb713 | -1.71283 | -52.49206 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 23220920-a90e-3666-960a-c57f01abd286 | -1.31118 | -51.73217 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 12bc7d63-b056-30db-9ef0-26cf7b798348 | 0.94246 | -50.74772 | 2024-11-29 05:42:00 | AQUA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db0988ac-b4de-35cc-ab52-45d99c6a7a1a | -2.10183 | -50.34908 | 2024-11-29 05:42:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 011691b1-97b9-3fcc-b7d9-e03e1d9e43ff | 0.0352 | -51.10709 | 2024-11-29 05:42:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 552e7d18-825e-3ab5-9a25-a8fb400d06e7 | -1.94893 | -52.96288 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1871ee1d-e4ce-314c-93cc-ef95396d0e11 | -1.70162 | -52.43839 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 14de9bba-c795-390e-a8b7-74c97fcbb135 | -1.26746 | -52.19909 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cce8d421-103b-38c0-bdbf-97cab4121cac | -0.96411 | -51.64682 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 289dddaa-fd2f-3ac7-ae5e-e9e0f021e1db | -1.08908 | -53.639 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ae107c13-96ca-3c81-a69a-e432cc531d65 | -1.06842 | -53.6362 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 45534cb0-bf7f-329a-a925-f136136bd38a | -1.95954 | -46.43913 | 2024-11-29 05:42:00 | AQUA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| df12e96c-0a94-3f6e-bdc1-fe18b4a9eded | -1.31752 | -51.75253 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9e9b9086-01b8-34a6-8573-861efacf0e6a | -1.58042 | -53.83791 | 2024-11-29 05:42:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8778034e-2691-3edb-8337-e48bb5f0ed52 | -1.68072 | -52.41816 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d12e9ad-fdcb-3163-a8e0-7d56b14810fb | -1.49773 | -52.43751 | 2024-11-29 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2054a2bf-70e7-35d3-a579-7960a705b46a | -1.59913 | -52.27705 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4e225ef5-82d2-3394-b142-f53741134f22 | -1.63016 | -52.3694 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fd64d63a-7683-35d9-98ed-880ddf5f30b7 | -2.37978 | -50.39975 | 2024-11-29 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7442f9a9-5f65-31ac-8429-bc788d60f92a | -2.01195 | -51.18802 | 2024-11-29 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 5686914f-5a52-3b59-ae6a-c920a5fe054d | -1.61785 | -52.45046 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5116fc78-cd6e-34af-935a-40e45240fa60 | -1.53126 | -51.6186 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 9ee15f59-acc3-33fc-a136-7d6ce4736fe0 | 1.67818 | -50.66608 | 2024-11-29 05:42:00 | AQUA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6eae53dc-5278-3487-97e7-482975909de4 | -1.20905 | -51.73978 | 2024-11-29 05:42:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9b79a86f-dc30-39b8-a085-1fbf244db2b0 | -1.93921 | -52.96143 | 2024-11-29 05:42:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8a9826c2-6ffb-367b-8e37-e08bf7a573b6 | -4.78836 | -46.11584 | 2024-11-29 05:44:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| c51a8bbf-433d-3c35-b0c4-ba6c8f1e38ce | -3.24793 | -50.76804 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06ff266b-b0f0-3ee0-b498-d3de86b645da | -4.16327 | -48.71238 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a277a37d-9265-3a4c-87e2-d7dbe241bc57 | -3.49725 | -50.45778 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efc6aa16-b860-3c89-b28b-d50df823e5f9 | -3.2879 | -48.76565 | 2024-11-29 05:44:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c9e297ee-af65-3df9-bb7a-266f8a59465c | -2.63887 | -49.9025 | 2024-11-29 05:44:00 | AQUA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e05136a-0726-3fa5-9174-68ded6ce08cd | -2.30652 | -51.98194 | 2024-11-29 05:44:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ca90b88-c252-35c6-bd19-16965028cc7e | -4.26673 | -47.6055 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 19816554-2aaa-3bcb-859c-c6fa128870fc | -3.25273 | -50.61597 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d0d0607-839c-3032-8acc-099a0957ed02 | -3.101 | -53.8188 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 819400de-8ceb-30ef-b30f-c9a506c51c90 | -4.16848 | -48.6134 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5181599-793d-3667-8694-12d0cee3ae98 | -2.83083 | -54.03573 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9b182821-cb22-364b-915f-0011321a47cc | -3.19683 | -46.57479 | 2024-11-29 05:44:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5d175f14-b630-31da-9af2-d1fa3b8bdfdc | -4.34257 | -47.57037 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 169eac1e-cadd-33ee-b455-7ca8ff1c95a4 | -4.79043 | -46.10133 | 2024-11-29 05:44:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bcdb43c4-d7d1-3075-bbfd-5d9fe11e3afe | -3.85692 | -50.15076 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 087ef9c5-b9d8-3172-a16b-3293ca6ceb10 | -3.5943 | -50.36998 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8949816c-7b06-31a8-a002-488d3bdcb50e | -1.88625 | -54.53653 | 2024-11-29 05:44:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 893f2a6d-01d1-32e6-af61-a43deedae1df | -2.73381 | -54.12945 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a27274c8-289f-3bdf-afe7-79a06ccc6197 | -4.31138 | -48.20856 | 2024-11-29 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2a07f439-a967-3508-b617-98e352e1625e | -4.04529 | -48.32947 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 01985012-7abb-37d8-96a8-46062bd70575 | -3.21962 | -54.18194 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| be6707f1-d417-30cf-ad34-998bf5bd7f8a | -4.07889 | -50.03035 | 2024-11-29 05:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 69ef7386-8292-3877-a2c2-514d4490c146 | -3.5821 | -50.51175 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 699b8248-53ac-3d38-bd73-40eec2077db9 | -3.96137 | -48.08052 | 2024-11-29 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a1fbca24-10e3-33ae-bcdf-38f288c90f82 | -2.03379 | -53.49008 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 03213318-29cc-3232-982c-fb4642e151f0 | -3.28399 | -50.15633 | 2024-11-29 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7f8a738a-0ff0-3a85-aca7-df890c26619d | -3.24939 | -53.64583 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e309afd3-5ff6-337d-99ff-48f29d85a2de | -3.22151 | -54.16959 | 2024-11-29 05:44:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 528a7ce0-3b02-3543-becc-92cbc0532612 | -3.96685 | -48.91282 | 2024-11-29 05:44:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| df4cbc9f-5554-3dfe-89c3-e2c89334397a | -3.59299 | -50.37877 | 2024-11-29 05:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 525f9ed6-803f-3f83-9787-100c5d13d184 | -2.22998 | -53.68705 | 2024-11-29 05:44:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |


[Clique aqui para ver as próximas entradas](README102.md)
