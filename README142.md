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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e889fdf-801b-3365-82d4-0cd2895d2e2f | -1.64132 | -54.39684 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9c5147f-d356-3ded-9c6f-785b3b137e33 | -4.10027 | -54.015 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a4ed38ee-e52d-3256-8963-14ccc505ca6f | -1.64506 | -54.39788 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e91cf2c4-f9e7-3263-b5f0-bce60fa44e9b | -3.27675 | -54.69775 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fbe2387-3c33-35a8-a26a-ea226cd31c0d | -4.82321 | -56.08175 | 2026-10-10 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4ee71ab-6e40-3f32-809e-d6b1e9eb15eb | -3.2828 | -53.87474 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c1a3568c-912a-3cbb-a16c-f78b2c356f14 | -5.97678 | -55.35374 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 724fa55a-f304-3b12-8cb2-f9ba638af718 | -3.19871 | -53.86171 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a1867a8-d62a-3b77-890e-82e9e7a24860 | 0.22358 | -60.38511 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63ccaa52-3a4c-3950-8ca1-9292526f5d59 | -2.93596 | -54.07875 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c525b75-02d1-3fd2-8fe8-51ee65413c6a | -3.30634 | -54.00233 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 76a9c33e-8700-3513-ac03-1c463531ff92 | -6.44286 | -55.05884 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd42a646-d15f-3adb-abe1-4615b3a63afa | -3.72587 | -59.46374 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5afc3c9b-fd65-3a43-90a2-0716656621b4 | -3.78981 | -59.37655 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 021dac1f-aebc-3b66-822f-af91d3384890 | -1.27553 | -55.75499 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 642e58dc-a7e0-397a-82a0-12d25a69d1c8 | -6.45629 | -55.50119 | 2026-10-10 05:48:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8cdd3a35-e9f1-3836-90cf-6e54004d085c | -5.48283 | -60.2654 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abd4f2bb-4265-39a1-bef0-543eaef7af54 | -1.62734 | -54.431 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74c28512-32ef-3402-9de1-5c0d3b0f213b | -4.18966 | -59.40734 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0c39d21-fda9-3849-9b15-10112078307e | -1.95625 | -54.38843 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c298d959-eab9-3d2f-aa37-c45a2860bfb4 | -5.16845 | -60.32959 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80b61113-0c84-34b5-a2a7-6fadba5a5453 | -1.32785 | -55.45245 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3699a03-6412-3005-bd17-7aef9c227821 | -3.08182 | -57.66964 | 2026-10-10 05:48:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67fbcd59-1df7-3453-bb4b-b0b5e720dbd7 | -4.19433 | -59.40804 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe83078e-ed14-3c45-8d37-2406652fda40 | -2.72675 | -54.14655 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a88e12ee-4397-3bfa-8c8f-a913ba109fc1 | -3.18852 | -58.65646 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55de7ca5-48d6-31e2-abfd-2f1c46399efc | -1.63584 | -54.41683 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c56059e-2afc-31d2-8e43-56ac9b2b1d47 | -3.57232 | -54.68459 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 737f11ec-d404-3abd-afd4-8857fc664f49 | -2.39305 | -57.89772 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e79bc7e-dbeb-3eba-8055-e2f531955819 | -6.46406 | -55.05647 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4983217e-4afb-329e-a70c-4047e463edf8 | -5.18491 | -60.30963 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5920256f-3307-3e14-bba2-1fb8ad97e19f | -3.28044 | -54.69602 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53794672-7489-3332-94be-98df2406f719 | -4.12442 | -54.03555 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79bac152-d1d6-32ff-baa3-49dfcd90aa4d | -2.57037 | -57.4132 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e7b24f99-2d7f-3794-93dd-0394355c23a8 | -2.53034 | -56.2692 | 2026-10-10 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51e196a9-24de-3d1c-ad9a-7495e77ab046 | -3.79117 | -59.37536 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11350914-6193-3954-b29f-ab1b00c7cb4d | -5.30939 | -60.085 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14cef7c8-720c-3554-a696-85ef83cdf16b | -1.3358 | -56.39614 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edfac178-80c1-3419-97c0-becaafa7ef13 | -3.63986 | -59.56874 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1084ffe6-cbd1-382a-aeca-17a5c04a74aa | -5.19062 | -60.30147 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 969d4f95-f9b6-3c17-8763-e471e2093370 | -2.89456 | -59.21501 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a27f6249-503a-3d2e-9ff1-c084fec1e28a | -3.95381 | -55.34525 | 2026-10-10 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e20eb81-2563-3c07-9d49-d34d474f6e05 | -3.12752 | -54.17743 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 16116c49-c7ec-3621-8b2f-8b22b625d878 | -3.11626 | -53.79106 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc09ff7e-a4d6-36b1-8666-72bbbc2a9676 | -3.03016 | -59.15815 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 439ad385-c361-37df-8ada-5ed25572f1e6 | -3.16901 | -58.62075 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f1188a0e-bb48-351c-b30d-6e00c74906a5 | -4.51824 | -54.8593 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b1e6d95-7fe8-3f63-8e31-de8f99b230ac | -3.92515 | -59.67066 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 371c08dd-7620-394d-81df-b075b5d9bfa0 | -3.2247 | -54.29004 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce108a65-b6dc-3752-9376-2dd3aebe5973 | -3.04229 | -53.895 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63203b77-9cb5-3749-85f2-59b56c84aba6 | -2.83172 | -54.81225 | 2026-10-10 05:48:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cfd94d20-ff03-3fac-8760-dbd11e1eb690 | -3.78289 | -58.5854 | 2026-10-10 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 639feb3b-dcdc-3e41-b2d3-3be33e97a3a0 | -2.80544 | -58.26506 | 2026-10-10 05:48:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3d2184a7-bc26-37cf-81ea-25061934c947 | -3.00032 | -58.89644 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 045011c8-e848-3472-94eb-299e0197dddf | 0.22764 | -60.38444 | 2026-10-10 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8403af63-8236-33d6-8ba7-95930c68d12a | -3.16339 | -58.62532 | 2026-10-10 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cca3178-28c1-3610-b148-aa4682b655e1 | -2.3887 | -57.89689 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5d6ffc6-999e-350c-9fc8-c0820e164f6f | -3.59129 | -54.59843 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f8314e3d-047f-323d-a056-2ad7aa53e93f | -3.65605 | -59.71612 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ace7294-a3e9-3624-a549-69503316ed3d | -1.95548 | -54.39345 | 2026-10-10 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b406c4f-88cc-300e-832b-180f2c6a3f98 | -3.30807 | -53.69367 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0223a6b-21ec-36a2-9130-550740736814 | -5.95094 | -55.35566 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e805256b-b0df-3e02-9969-e7770d49564b | -3.99403 | -59.35614 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03bd6fa9-ae54-311c-bedd-893db40064ca | -3.59055 | -54.71521 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4254b509-f0e8-310e-b60b-2806bb8307bd | -4.1136 | -54.01662 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 902bedaf-5436-3d82-acf0-ada5bc3d68c4 | -6.12847 | -55.7033 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53e99bc8-3825-30c4-bd6a-c32ebae88aaa | -2.56418 | -57.41877 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beeb3ed3-c0a4-3748-99ce-09436ff1f332 | -3.25887 | -54.18662 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 646170cf-1d9e-3b67-9d8e-d555f62e7731 | -3.59764 | -54.59947 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 44e3810f-5be1-394b-a5b2-d9882bc4a7b3 | -3.59689 | -54.60463 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3be5dc50-5b8d-3d7b-afde-f1c5b7ab3055 | -1.87971 | -56.31186 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04443495-7338-3dcc-8c29-b7493860ea5e | -5.97184 | -55.34329 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0faea24-565f-3111-b873-e8f5d706bea9 | -1.63041 | -54.42584 | 2026-10-10 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0d0b3de-26d1-3e5c-801e-66fb2cf9ba5f | -3.78447 | -59.38071 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e6c3f75-9c53-3423-a8d3-b244428f247b | -3.58277 | -54.70159 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5ed10ed-9a86-3bbd-8c55-5178b9dde7a0 | -2.45615 | -57.88936 | 2026-10-10 05:48:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41a6f4b2-783d-344f-9066-bd51f33c25ce | -6.47048 | -55.05744 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d742bb28-f590-3b6a-a91a-20317a1df295 | -2.39809 | -57.89849 | 2026-10-10 05:48:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ccfaaae-6c2b-39d2-a794-d8122c6f9dbc | -3.30728 | -53.69934 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b605b6df-40d3-3cee-b033-5398f99a15b6 | -5.30676 | -60.08159 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 900fb719-b766-393c-ac6b-19470e326ba6 | -3.20159 | -53.85657 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a81b2f7-7046-3335-8d1e-f90be29cf035 | -3.86932 | -55.98926 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d13345f8-4249-3e51-91bb-1afe951b9c14 | -2.22091 | -53.6988 | 2026-10-10 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17ac2e75-0082-39c9-bc26-eed12b40eaf5 | -5.79697 | -53.79966 | 2026-10-10 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e4c7dd70-4109-394e-91c1-ea0976b29ff0 | -3.74819 | -59.47215 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f084e38-4c61-391a-a46e-5f99623b8cdc | -3.78653 | -59.37464 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90e671eb-c494-3a5d-9d5a-62e40a0c00dc | -3.12821 | -54.17187 | 2026-10-10 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d67387df-1305-3133-b8e3-d896899041c5 | -6.32081 | -55.33809 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52e5e446-09ef-3efb-803a-919af77a2458 | -5.96369 | -55.33736 | 2026-10-10 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 839f0273-afc1-3b93-b314-735df1397a0f | -2.7288 | -57.47092 | 2026-10-10 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d8f379c-4faa-34a0-8ccb-db5413de20c5 | -1.21873 | -55.65752 | 2026-10-10 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a31b75db-145a-3d77-9d06-aa013f13b40b | -3.11547 | -53.79659 | 2026-10-10 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69b8c336-1be6-3e12-b890-829e083c7139 | -3.43229 | -54.54124 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae2e3636-5ff4-3000-8dbb-12683bc8ca9f | -5.24311 | -60.19101 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf56694a-222a-3947-8a8c-ea1a6d0c4158 | -3.57679 | -54.38021 | 2026-10-10 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64ee5a71-7d9d-3a6f-9c04-f3beaae5f73d | -3.89341 | -58.96061 | 2026-10-10 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 587937a1-e577-37ec-befd-daaf4e0c8d9f | -5.31129 | -60.08228 | 2026-10-10 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18a6fcc7-d56c-3c06-9450-c999edc89433 | -1.3169 | -56.40561 | 2026-10-10 05:48:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdd57070-1fd0-37cf-b4ee-9836fb468fba | -3.81941 | -59.3362 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf1229d2-f48c-3505-8dfc-f18c9ee0d747 | -3.78578 | -59.37955 | 2026-10-10 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README143.md)
