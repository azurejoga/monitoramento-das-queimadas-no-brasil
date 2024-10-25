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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd3a62a5-8a1a-3613-9009-f6c8457dfa78 | -4.59579 | -56.09357 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d9a6dd77-2282-3952-b3e0-aae37b81019c | -4.58165 | -55.96804 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92647d46-2d26-35f3-ae7c-c18128889861 | -4.56109 | -55.82716 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 65768d6e-2c1b-3ebe-8938-cd3b3dbacf68 | -4.52778 | -55.91909 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 08e5b09e-eda7-3ef9-a80c-1eaec35052e9 | -4.5161 | -55.81426 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3d931a34-2444-37fd-9926-e11bab3105d3 | -4.48991 | -55.58758 | 2024-10-25 16:52:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9430dd0d-e93d-36e0-b585-67ea54cd518b | -4.46064 | -56.02242 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6e3f0e2-355a-3506-bf10-d6c89154afb2 | -4.42575 | -55.69775 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 233.0 |
| f993ba6a-0791-3b00-8369-33e0bf4578f0 | -5.25509 | -55.96355 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 98f37fb2-a1d3-32e0-b748-34a735b48434 | -5.25154 | -55.96775 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4337e84e-4a3f-3ede-8eaf-82b04c5c6d36 | -5.25101 | -55.96412 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e19b3502-bdd9-3192-a75e-490dcf8d77b3 | -5.24746 | -55.96833 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bc19302f-ca78-3abf-9160-15b7b7c57549 | -5.24694 | -55.96471 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc506f91-798a-3d8a-8d92-8ca0191b84f6 | -5.24339 | -55.96891 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cc26508d-a125-33f6-83b3-84b86b499722 | -5.24286 | -55.96527 | 2024-10-25 16:52:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ed1c182-1702-3ca7-b6ff-0e961b57c9ee | -7.79096 | -56.34675 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5b7ef4d9-d2ab-34ec-8991-db9e57a58a6d | -7.79038 | -56.34255 | 2024-10-25 16:52:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 68bfb8dd-d21b-31b9-94e1-dc0a0abd3549 | -9.34001 | -57.32587 | 2024-10-25 16:52:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 425bbe94-221d-37d2-aa1e-0f8910df620a | -10.5412 | -58.0954 | 2024-10-25 16:52:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04939db2-8e13-37b8-a7db-c380d59d41ec | -10.54081 | -58.09246 | 2024-10-25 16:52:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e14cf9f-aab1-366e-9681-2f6fd9be2dcf | -10.50702 | -57.79839 | 2024-10-25 16:52:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9db1eb68-e362-378b-89d0-dd68e0504e9f | -10.39104 | -58.00463 | 2024-10-25 16:52:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 673e01fb-ee4a-3b29-b1eb-313d275df887 | -10.23652 | -57.68113 | 2024-10-25 16:52:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9b833040-1883-378e-afe4-d0aa567fd77e | -9.97279 | -57.85416 | 2024-10-25 16:52:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 45837450-8e83-3297-b782-fe746755530f | -9.90071 | -57.80549 | 2024-10-25 16:52:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ad4d660f-30c7-335f-a532-34105ea0aac1 | -9.89612 | -57.88744 | 2024-10-25 16:52:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5596f6aa-59fb-3703-b282-063478d83052 | -9.7408 | -57.36375 | 2024-10-25 16:52:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| eac70485-1447-33ab-8b7f-688ee136e336 | -9.74011 | -57.35854 | 2024-10-25 16:52:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7347a827-cfbb-37a2-9e2e-ed542865b187 | -9.7367 | -57.3697 | 2024-10-25 16:52:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 63590c53-aac5-3374-bb9d-aa4346652d60 | -9.736 | -57.3644 | 2024-10-25 16:52:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e9c468ef-b2e3-30d3-ac90-80dcaaf0ca92 | -9.62938 | -57.69492 | 2024-10-25 16:52:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9dc6b852-db5a-31cc-b500-835406677b98 | -10.88004 | -58.39292 | 2024-10-25 16:52:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 03ae722d-79b1-3bd2-86b3-5a2e40628b4f | -10.94022 | -57.79163 | 2024-10-25 16:52:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c74bdb06-2d4b-370a-80a1-dffdab08f3e8 | -3.67498 | -57.07489 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 929d6328-7416-3601-adba-f928027f38ae | -3.50496 | -58.38188 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 367af9bb-8ef2-30b0-a19f-2ce8e1dac377 | -3.50426 | -58.37699 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 73635476-7e3c-3404-809a-3cfcf27e9815 | -3.50219 | -58.38026 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5c763060-6873-3a67-a5ab-5abb5be976ce | -3.49816 | -58.36781 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 81075d3f-1b5c-3c6d-adb1-a4d87e687993 | -3.39717 | -57.512 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 42b67cb1-6d1b-3238-a639-b90d4731188a | -3.39276 | -57.5126 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 321a1d66-fbe7-3844-8001-ec30d6ea1194 | -3.39174 | -58.33329 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1ca17bfb-fab0-35b5-ae1e-ddf4f850311a | -3.38996 | -58.33108 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 20bce00a-189c-3d92-83b8-18b968dbefa6 | -3.36559 | -56.97196 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 9a43a084-87f2-34ce-a276-e8ac7259e5f4 | -3.34074 | -58.24693 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9fcb8897-4a83-3011-b0e5-bb523eed6898 | -3.24477 | -57.09027 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6d5b0c5d-6ab6-32b1-9cc7-70bda58e9183 | -3.2405 | -57.09085 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1b93087c-871b-319a-a679-e6ca54170431 | -3.24045 | -57.23936 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 04c29065-4fd9-3cbe-8113-de9ff4e5ad78 | -3.22079 | -57.68942 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f438c788-172f-387d-838c-9493d14ac3a6 | -3.22013 | -57.68499 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7d9c27fa-e1ff-302c-99a2-e90877916aa9 | -3.20781 | -56.81234 | 2024-10-25 16:52:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d72d7c3c-e529-3ece-8a6a-b2f28e5a0ec9 | -3.20534 | -56.8245 | 2024-10-25 16:52:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7c66457f-c5fd-31da-9b8d-d0081a4d4f9b | -3.19289 | -57.06023 | 2024-10-25 16:52:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ac00314e-7ea1-39b2-9165-fb9f6d1fbf25 | -3.81406 | -58.24922 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 119a8b2f-14bf-3742-b39e-dbdea2d8ba38 | -3.81063 | -58.2482 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| eadc3344-5268-3e5c-995f-9ac68d38b392 | -3.79897 | -57.95023 | 2024-10-25 16:52:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e5af906c-10ef-3350-9092-0b99ba547ce1 | -3.66696 | -58.23096 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| f16afa37-e38c-37b5-aa8c-6643b2815368 | -3.66162 | -58.22692 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 79cfde13-59da-3d6a-9baf-4b2002b2b373 | -3.65768 | -58.23236 | 2024-10-25 16:52:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 13369708-dedb-3a71-baff-21fd8a9b4fb1 | -5.93755 | -57.69584 | 2024-10-25 16:52:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80ecd08d-30ff-3380-b02a-e91ad3c756f9 | -5.88015 | -57.65354 | 2024-10-25 16:52:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 89a91299-294b-3c58-b88c-55675f68fa48 | -5.87922 | -57.65018 | 2024-10-25 16:52:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 46ec4371-472b-3a8b-9ff1-48136c308eea | -6.93067 | -59.01611 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 18f24794-546b-35a2-8e71-b64980e6e885 | -6.93026 | -59.01306 | 2024-10-25 16:52:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 60adc953-b8a0-3aab-a3dc-29169152a638 | -9.33652 | -59.03168 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33e355ec-5bd6-3d55-b128-42e3d46061f4 | -9.23785 | -59.0126 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 2ee069c3-5ea7-378d-a273-55a0f77dbda5 | -9.23741 | -59.00925 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 83522a4b-8f71-39aa-99f4-0d9f72842761 | -9.23336 | -59.06118 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3cb1cad4-4072-3b3f-b88b-1c65ebdf9f1c | -9.23253 | -59.01333 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6e4cc204-7ecd-3308-8594-ae26ca17f267 | -9.23209 | -59.00999 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c2883e6c-fe69-3115-89be-75679eea842e | -9.17011 | -58.98159 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2c2a86f3-1a2d-335e-ab3d-2c969394ddf7 | -9.16964 | -58.9781 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cc895aa4-6154-3ef9-9ce4-ebf9dbe78323 | -9.16873 | -58.98 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b6d44ce1-f720-3809-a47e-34921e089bdc | -9.1683 | -58.97659 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c8b5833d-2b19-33db-b74e-06d8299eb578 | -9.1643 | -58.97859 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9eeb9ab5-3796-36c9-8874-ce668307092e | -9.0572 | -58.9398 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa8f6f40-1a02-3ef5-908d-a48468171f6f | -9.05679 | -58.93954 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6fa2803d-563e-3dfe-910e-0ad06bf0f1e8 | -9.05188 | -58.94026 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d9e2ef37-dd84-3b0f-ae8e-7de36e5c09b9 | -9.04132 | -58.90176 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 9df9a156-af95-3391-81b9-95ced8bc41de | -9.04088 | -58.8985 | 2024-10-25 16:52:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| c127caec-b56a-30d8-8191-dcd6f23fc7f2 | -10.85081 | -58.91423 | 2024-10-25 16:52:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e28e1a4-e3e1-3859-a46a-4a7e6cd62e8e | -10.76098 | -58.59141 | 2024-10-25 16:52:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 525ab230-1149-3d8e-9d28-be70260e5b30 | -10.4469 | -58.80308 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ededb161-7ab5-32ae-9455-bf43027edeab | -10.44106 | -58.84129 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9109c793-1e5a-34a6-b187-952c461ce0a7 | -10.43911 | -58.84193 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e26efbc8-8a72-34be-aed0-144dd5e0843e | -10.39171 | -58.41799 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| badbaed8-9cd9-3fff-8e84-6345cbc773cd | -10.39054 | -58.41836 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c2c0b76-dc8d-3203-a107-57c449579b11 | -10.29448 | -58.49512 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ebc6a46-3ca4-346b-a47c-03e5c1a9ba09 | -10.29349 | -58.4944 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f980bdda-3465-3fb1-ac39-c92c97c9a43c | -10.25 | -58.48653 | 2024-10-25 16:52:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2fef07dd-655d-31a7-84d6-0fb11a86fdbd | -10.24313 | -59.13059 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87f85af1-47eb-35b1-9334-e644c4d13fff | -10.22311 | -59.14709 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c3189ff-5541-3b85-8b81-96a6989e1b05 | -10.21766 | -59.14779 | 2024-10-25 16:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e6c23cfa-9675-32f9-a2fe-701592647ef7 | -9.55974 | -59.0609 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eda6e16e-b58a-3cb0-9e50-dd979c419365 | -9.40201 | -59.04853 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a52ce77-3fa2-32c0-b0e8-2ff4e74dc994 | -9.39861 | -59.04875 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b3c5fc2c-8981-3f80-823b-00ab17a4114b | -9.55557 | -59.15586 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d345c49f-8e1d-3524-ada4-a10d61e6b8b8 | -9.55513 | -59.15241 | 2024-10-25 16:52:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e17661b6-ac74-3f45-9f3c-22ab8b58cddb | -3.70433 | -58.51364 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1284c99f-a175-3a71-81ba-c827736479bc | -3.69958 | -58.51424 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| bf286b44-a7f1-3852-900c-5ee00df1fc06 | -3.68289 | -58.43427 | 2024-10-25 16:52:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |


[Clique aqui para ver as próximas entradas](README181.md)
