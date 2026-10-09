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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83b7f7d4-3ae6-39fe-af50-671027b929dc | 3.52995 | -51.25582 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93b2981a-442d-35a9-b4dd-7d601014068a | 4.4371 | -60.96872 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d82e245-2942-34f9-8350-7cae66cc7579 | 3.5245 | -51.24881 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23c7aa8a-7cde-3dae-8189-4365d355b9fa | 3.73201 | -51.64696 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77c3b619-e646-32fb-b87c-6e662a7cd110 | 2.42115 | -50.8232 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e7e12771-d8de-3eb2-b260-652d1a85d7c8 | 2.42044 | -50.81894 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6eaa94b0-4b2d-36da-9d6c-9642df0baf93 | 3.55465 | -51.27544 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6983204e-9135-3e0a-9233-42eb3721e38c | 3.73955 | -51.61604 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95d31e87-a3b4-3b37-bbc5-d5a7be958477 | 3.52932 | -51.25197 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 150baa50-20cd-3272-94b7-62d5ba726aab | 4.43804 | -60.9492 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9db09c91-2de3-3ca7-8afa-a253e2686164 | 2.4208 | -50.82219 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 04f7ab9a-683b-3258-8bd7-9b6af02c1cad | 4.44093 | -60.96803 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 589efe5a-5912-32c9-b930-aca0b9e04317 | 2.45628 | -50.81755 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28321dbc-b809-3b80-a650-83ae0c146610 | 2.4208 | -50.8222 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5dd1a9d4-8803-3a97-999e-fccc83ff00b5 | 2.41572 | -50.81863 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e35a635c-4b2a-3a29-a7c6-6acbeefa53c8 | 4.43925 | -60.9827 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ffca818d-37a8-3b3b-bb56-b9a45ea7f7f1 | 4.22771 | -60.83915 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7add1cad-c9c0-34a2-a3ef-1b99ae953bcf | 2.45118 | -50.81399 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 098c3b78-35e5-3635-b88d-531253d4733d | 4.43846 | -60.90095 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5dd783d-eeda-3380-a401-bb182fc390e3 | 3.55403 | -51.27161 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19cfe07b-6a00-3ca4-88b8-ba0c22d4c0b0 | 2.42011 | -50.81792 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e7f0f2fb-272e-3dce-ad47-d0369697807b | 4.88966 | -60.31086 | 2026-10-09 05:21:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1066775-5b47-36c9-88c8-cae0a44a14e0 | 4.25682 | -60.92567 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21cc0f62-1cb1-3bc9-af5d-9fd0e6df9f52 | 4.43875 | -60.95387 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7170f780-ba41-3e2e-8b38-a7a1c89bb58e | 4.25598 | -60.92796 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 465f9e9a-63fe-3a97-9a5a-f8534827cc8a | 3.85786 | -51.78049 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccded3d4-0442-308c-a3be-199ad4da449d | 4.25682 | -60.92568 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e859333-4200-3f61-8895-e94dac255ed2 | 2.41709 | -50.82719 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 29d0a7af-1ed2-3405-a12c-a88f66f5cf63 | 3.52031 | -51.2495 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d69a9e2-b7ee-3287-867f-51b3999c104f | 3.55527 | -51.27927 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6f3984c-537e-3788-ad50-8fd1a0a688ef | 2.4164 | -50.82291 | 2026-10-09 05:21:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 389feda0-bd68-32b9-8266-0e1991d33134 | 4.23151 | -60.83855 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53477074-9a87-311c-8446-1ae451811ee7 | 3.74304 | -51.61175 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549a94e7-3881-3f05-beb4-6ae3df6d009b | 4.23506 | -60.84006 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a374a84-806f-3766-b702-79128a042848 | 4.43536 | -60.90625 | 2026-10-09 05:21:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22eb85e7-8fa8-37bc-862b-32ac9b49fc5c | 3.55403 | -51.2716 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 50ebe8e7-3741-3cf7-871b-4486526e6eff | 3.52932 | -51.25198 | 2026-10-09 05:21:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e57b772-b2c2-3467-b558-7f82c6aec226 | -11.11482 | -47.79116 | 2026-10-09 05:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f770c0a1-2669-38bd-91b0-b8c4246fba12 | -2.5752 | -56.17776 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35dc43f8-cc0c-30f5-95bb-f271e39dc9cf | -2.56705 | -57.40615 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fb11935-39d5-3fb5-bd60-33e323b20f30 | -10.24232 | -59.02666 | 2026-10-09 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 728965fd-cce2-3bab-9f24-22ecd40f560f | -3.73692 | -59.45694 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3d288a9-58a7-3bfa-b98f-558844cab9f0 | -2.52041 | -56.61765 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae73aad2-ed08-325d-bc9e-8f71af84a20a | -9.4945 | -57.25338 | 2026-10-09 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 146e2403-4edb-393c-b2d5-a452da26b53f | -2.73826 | -54.11929 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 064f91a1-94a2-3527-9971-a6e7d836f588 | -3.00384 | -54.05829 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62816885-c3cc-36b7-ba62-01061bb9bbac | -7.57843 | -61.54547 | 2026-10-09 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aec3660-8617-3602-981f-e6b0577f2a5a | -3.40918 | -59.59599 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86be8d8a-d907-3d5b-b6bd-f957173cba5c | -3.28956 | -49.51081 | 2026-10-09 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edf3aced-0915-37bc-a860-2af5b05cf87a | -1.10914 | -54.16013 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70343013-4b36-34c4-9614-347cc1a1cccf | -1.18604 | -55.67265 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3193dc75-c4d6-3693-ba8f-99c7bee608b0 | -3.73247 | -59.46342 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cab72d98-680d-3760-95a8-6e885ed66f72 | -3.71052 | -59.64371 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd9dbf9-0588-380d-9026-b9af40adbc3d | -2.74737 | -54.11106 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6aec75a8-f9b4-314e-96cc-cf714deeda6d | -3.46717 | -59.25303 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e1e299d-24a1-33b5-b04b-6c6cf9696b26 | 0.53103 | -50.8986 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fce47043-7a00-3dd5-85e9-a0b3a1bd960d | -1.37389 | -54.6423 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44d20a61-6d93-3e69-87c5-9238a7bb931a | -3.9255 | -56.02561 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7adf896-0138-3c44-a2e7-6badd83ccb00 | -3.0138 | -54.04512 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7046e5ce-3829-3f86-9b71-e786b96cf033 | -2.49569 | -58.07133 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db4b3f87-bb8c-3ada-b514-16eec8c80b7e | -3.54028 | -54.68893 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 74503d50-c94e-3d9d-adef-8dd4b68abc99 | -3.24959 | -54.03313 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e5f1aee8-faa1-37ce-96ca-159208a00ea2 | -7.00085 | -59.10205 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b7ee647-b53c-3a20-ad90-aa991e461d93 | -8.76936 | -61.38417 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ce1300a-8542-3aa6-99f0-48f34422a2cd | -2.5047 | -56.15535 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d050db3a-152f-3654-abc3-6309b5fe2a99 | -2.57923 | -56.17456 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a159d6a-68bd-3f8d-8c7a-ee40dca30c75 | -7.42877 | -63.55146 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95333a35-4354-380a-aee8-a039fa3f930e | -3.28827 | -51.54198 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67bd07bc-8352-346f-9e69-450709f5675b | -3.02033 | -54.76341 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc9d19b4-45c0-3006-84ce-0db1a81bec89 | -3.10408 | -53.77615 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32767265-30b4-3542-9201-53bb5b64697c | -3.57204 | -54.48471 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b70e20-4043-3981-bcd6-bab6e57ce101 | -3.05835 | -59.0887 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db8b40a8-0f8c-3ec8-8495-404fdc8166b7 | -2.56903 | -56.14992 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e0cc23d-fccc-3c47-a9a5-e840a2c1019d | -3.71484 | -59.33887 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fced8a17-9fd3-3acf-b506-a4f33ad47fba | -3.00479 | -54.0899 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24694d98-d4d2-3e46-b6a6-45bfa2418fb3 | -3.59692 | -54.67633 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8eebeaac-8ba0-3df3-9992-cdcb2d9ffa7a | -3.29383 | -51.56945 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3625f44f-8477-3164-a424-6b7cd110cb95 | -1.12555 | -57.28371 | 2026-10-09 05:23:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1f1bf35-427f-3ac4-9e64-caddf9fb089c | -4.17579 | -55.5079 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 417a5405-867f-3795-8ac4-7d0e68a9f315 | -1.53805 | -54.54871 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f08aacd-cf63-34be-8d74-31b14abfd09e | -3.08896 | -58.01637 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca76b504-4f8d-33b8-b000-234b1fbc815d | -3.8705 | -55.6524 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e870fa6-ef7f-3bb7-8b1d-5aeb1135a898 | -3.51888 | -59.22551 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9828493c-4ec4-3a3c-91fa-3c382fabf853 | -8.84064 | -61.46368 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d9e0edd-636f-362f-9e03-4c6642035c2f | -3.7819 | -59.19618 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6979a48f-604d-3d27-ad1e-e661be9d6876 | -8.33285 | -49.1293 | 2026-10-09 05:23:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3112c61-e2e9-3c40-a1b2-1e700766699d | -3.07675 | -54.28384 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16820c8b-194d-3eab-9ac3-88278e091360 | -2.49776 | -56.17725 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e5965bb7-90ba-364b-8f2e-93ce143ef970 | -3.74024 | -59.479 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b33284c0-5ff4-387a-ae77-62d15f4073a4 | -3.6677 | -60.61169 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0dadc11-61e1-3bb5-b0ee-20251c87568b | -3.44769 | -59.54786 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee278f90-244c-3d79-9897-10ca55d38c39 | -3.27224 | -54.06635 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba007774-970b-369c-aa1e-3b9b887775cd | -2.57641 | -56.18922 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8c925f0-fe57-3478-8654-6ef8acca30b9 | -3.64239 | -60.61533 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02c27f7a-4229-3f10-8519-0182ef238596 | -3.54604 | -55.52726 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b3b45a8-a393-3229-881f-581b7e760d75 | -3.40865 | -59.57781 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f61a5b6-35d7-38c8-aa26-26a089b2851d | -3.64992 | -59.1718 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 038ef651-de20-3b35-99b4-7eca9744d49a | -3.57158 | -54.68455 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ab1c5126-6032-3b1e-8e08-dd2c22402ea9 | -4.12183 | -55.03667 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 468a7633-a876-337c-8dbe-e8ab6e78c141 | -2.77181 | -54.10512 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README178.md)
