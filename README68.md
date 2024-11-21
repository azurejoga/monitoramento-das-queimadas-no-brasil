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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 652a7459-cc8d-3bf0-a893-5cfd3201e1d3 | -2.80178 | -51.76875 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6e07c1b-0807-3805-9706-620bef63aff7 | -2.76766 | -53.21675 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edda0ca1-c4c5-39d5-b45c-98e75a13e4d2 | -2.61311 | -54.26382 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7046368-005c-3404-907b-bca502a9e976 | -3.53822 | -50.53022 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b4e09af4-6f16-3dd5-bd93-045ea6f53287 | -2.26848 | -53.75474 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b00daed-dd0e-3129-ad69-29089d48d1eb | -2.90508 | -53.05518 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d4f2f46-85cb-3c99-b41e-e1cc56267118 | -2.8214 | -52.96103 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d92ca783-329c-3807-9255-c582c62578df | -2.82279 | -54.09702 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9c2df75-dfdf-3e54-a419-b7f9e664f416 | -3.28078 | -53.82193 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 54552b31-3bf0-3aa5-9d20-4d718c2beda5 | -3.26923 | -53.83072 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc495906-773e-3d38-abbe-f6e2f81b8cab | -2.62256 | -54.26889 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f7407d0-6d00-36e2-8157-5b07573dd437 | -3.76071 | -52.40856 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8f72075e-e0e1-3f12-b2bd-346b71b820d6 | -3.73042 | -52.31691 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c1a4ee0-5e07-3375-b5a7-a085f67dbce0 | -3.90654 | -52.40538 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 397f7c61-3bcb-3cd3-852d-d2875760a491 | -3.10106 | -53.99131 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bb7f504-42c7-34d2-a031-edc9b6a37595 | -2.89516 | -53.05364 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3619b4ec-b624-3e88-afe2-6b63bd78f331 | -2.59288 | -54.04656 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8f67410-98ad-35e8-9be2-46f20c823ecf | -3.98808 | -49.92601 | 2024-11-21 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b713a8f-9d48-3b82-a465-27e09e4b25c0 | -3.55727 | -51.53344 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11a5f973-6983-33db-8d16-afcbfa198c18 | -3.81701 | -52.34781 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3ba3933-347d-32fd-9176-e157d8bf7fac | -3.18477 | -54.32141 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25c4cbfe-789b-3897-a209-87590c5b8d6e | -2.62977 | -54.28431 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a80f87ae-5c7a-39ab-8ca7-ca0bdda8ecfe | -2.62311 | -54.26539 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d067e6-90ef-3c48-8d43-cfc924988ccc | -4.093 | -51.08721 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d24b670-c159-3986-b1fc-29f2929e18c8 | -3.10167 | -53.20944 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa29278a-3390-3b3f-b2d2-6dbc7346fef9 | -2.57631 | -54.08675 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68a2f63a-f2ae-389b-95a7-6ae4763e9e58 | -3.42236 | -53.28783 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79d373f2-39cc-3c99-80f6-f25fe1de0163 | -2.82652 | -54.00881 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86dc7058-02a1-388e-8ba0-91170be38f46 | -3.46976 | -51.64536 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5de4d466-ab44-3f81-b1df-81b5b4a86ff7 | -3.96858 | -54.13518 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 715bbcc7-4345-31c3-9d7e-b5b104f06c5e | -2.74538 | -54.07035 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bbc57a3-c4ee-354c-b7f6-fab3ceba966b | -3.66291 | -49.49228 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9f37a2e-9101-3921-aa0c-2da0776d135f | -3.12175 | -54.18272 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a97b785c-0ca5-36e7-af87-3f2b3ec5e545 | -3.10134 | -53.10377 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 731040ad-b684-3197-8bff-6d0b483120f9 | -3.6416 | -50.21458 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c918c4f9-d18a-321c-9f21-5d4614db303d | -3.31608 | -52.86133 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134cddc9-2ed4-33cd-bd7d-d677bc6803b2 | -2.76361 | -54.06253 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5594f031-8fa1-3651-a193-f1f6ceba696c | -4.24457 | -46.10586 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf633826-d973-3a33-b449-673178b9a461 | -3.72337 | -52.66884 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5227e15-0af0-386b-b5b6-9438ef1803ac | -2.78774 | -52.54801 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62990a94-c02d-365c-97b8-b663d1bff7c6 | -3.13792 | -49.12723 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e40bc57-b06a-3736-a197-b75c5d50e188 | -3.10101 | -53.17059 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f573f657-7fd7-3675-bc61-cd124fa68adc | -2.89901 | -53.05071 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6befe804-d0b8-3e77-9689-df44bb811a27 | -2.37308 | -53.65107 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 763beeda-5c3a-3146-80cd-99cdbb156a0b | -3.29465 | -53.86289 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73eb0f40-bb69-3a4c-a515-ac3ea67fdbea | -3.96804 | -54.13863 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd4fc22a-8843-30d3-bcdf-c968ebbf5fa9 | -5.94929 | -44.24264 | 2024-11-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e39963a6-9e68-34a4-8ef4-4a04f91a290c | -3.09749 | -54.29301 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b9a793d-4983-334e-8a59-e3615ca5d7bd | -5.71792 | -44.80938 | 2024-11-21 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ae79c07-d9d6-38d8-b211-d41fb00bcdef | -3.10707 | -53.17506 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 64bbbb1f-a8ba-3719-931b-5fe46ab6d9d4 | -4.5846 | -48.01542 | 2024-11-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16f40037-b63e-3ec6-94f5-4d6c0cb1af03 | -3.82615 | -52.19968 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2302445b-a759-3df1-815b-f92edf72aeda | -2.74377 | -51.82986 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f1ccd66-1b03-30de-afce-8bde2db0a099 | -2.82929 | -54.01279 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5864d7b1-35f5-3ad0-a8c7-589581ee8741 | -2.83261 | -54.01331 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1100f6a-ddd8-3f96-a59b-b9711c85c4f3 | -3.29933 | -50.22713 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16db5eba-da37-3c4a-ad8d-ba6b60123c60 | -4.00087 | -54.33915 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84e39d25-6c3f-3679-b6e4-ce64cf7c7846 | -3.76533 | -52.13626 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 322744aa-ee43-352a-bfbc-95dbaf2fb56b | -2.62922 | -54.28782 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9de9b946-9e4f-3c8e-b2a9-f2396800e6da | -3.53768 | -54.08814 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7988114-72dc-3cb6-a204-3e982e496b8a | -2.58783 | -51.7249 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07528e34-2dc2-30d1-b53d-c83c3030c76c | -2.79122 | -51.61477 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44e18dd9-e2f1-3ab8-b9b9-6fc8e4ec9b80 | -2.59837 | -54.01183 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d96618b-97ba-3861-a2de-3e9315af67fe | -3.25785 | -50.82615 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b3244f6-17e5-3a47-8800-9033a0d9caa4 | -3.80527 | -51.26609 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 333f1baf-557c-31b3-9a6a-05f341c83800 | -2.7647 | -54.0556 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37f67dde-8297-3fa8-99d6-53d38c4c2ecd | -4.3904 | -45.59442 | 2024-11-21 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 239a7877-d569-3c7f-93ad-8f565f05791b | -2.58562 | -53.98499 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a17a04d0-178e-3db2-b840-7848f4306ab3 | -3.77481 | -54.22148 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97ddbc65-0840-38c9-987a-b8b2220eb461 | -3.7197 | -53.75342 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0968d4e7-c90e-39b6-aa88-dc7627ae7805 | -2.80998 | -54.02751 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c3f9ba-a008-3e32-8a28-444e4f1fafef | -2.87524 | -51.79393 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da712d4e-496b-3c62-be02-124c9ee4f1d9 | -2.67072 | -51.88829 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7684ccd7-d911-385c-a1b6-7c96a3992ef7 | -3.78253 | -49.36869 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45cc86ed-e1d6-3bde-878c-45335ed9ee2b | -3.53579 | -54.48719 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae0ad988-f92a-370d-8c16-90c2ba6e05e3 | -3.09398 | -53.21528 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c145a6c-530d-37ab-8b64-e05e21b514fb | -2.89847 | -53.05415 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a508e250-0650-362a-8c7e-4b83f02c423f | -2.80115 | -53.00369 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03669196-7efb-378c-ab43-b9f0a29a39ce | -3.32479 | -53.19477 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45dc92a8-2608-3270-bca4-5b3cc61af53a | -2.55535 | -54.04748 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8937b724-13d4-3838-8ecd-0a26d76430ad | -3.25559 | -50.6311 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e60fb06d-5b86-3c60-ba5b-33037dea0aba | -2.76012 | -52.11281 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8e62574f-0bab-3707-a452-6c68b2335008 | -4.4856 | -50.14506 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ad7a766-e7e4-32d4-b448-3450ca4867de | -2.75622 | -52.11583 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e3c1f57-5690-36c8-9f71-6bc05b3f4b0a | -2.84274 | -53.02085 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 383321ca-8869-390f-b1c6-fb21be72f8d9 | -2.85627 | -53.97092 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe05018a-77f6-31a5-a969-a3539c4fa317 | -4.12098 | -53.81645 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 767f8b53-6c84-3265-a2ad-a04788934795 | -2.60059 | -54.01927 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2460bdef-9b0f-3cb4-accf-a423a76c0bda | -3.18255 | -54.31393 | 2024-11-21 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8fe5ab8-b079-325e-a2e1-04511934a5bb | -2.81162 | -54.01712 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41c78e62-0b08-35c3-8b45-394d73570e57 | -3.30055 | -50.36356 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10353307-2957-35b3-ae3c-3ee886596893 | -2.85147 | -51.58941 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d1cb74ce-da10-394d-ab5b-0cb4296ed782 | -2.50697 | -54.24694 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10c7d84b-1532-3efe-b7bf-6bad2eaff62e | -3.39577 | -50.25799 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f12cf642-315f-3cdc-af15-dc68d1755efa | -2.582 | -54.22312 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49cec08b-9802-35a6-a9ab-9ce9a183a18c | -4.07604 | -50.03674 | 2024-11-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5db08c3-8c43-3844-a559-f438895c329e | -2.62239 | -51.80004 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 424d0746-c00f-38cb-8326-2c0fa3231168 | -2.52011 | -54.14178 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5763636e-e25e-382f-81af-a73ca756cab4 | -2.36915 | -53.82706 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f79cc25f-ca37-3ed9-a4c2-f66b7297e5f6 | -2.77354 | -54.06444 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README69.md)
