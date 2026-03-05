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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da378086-7433-3c5b-a654-dd98b7bcc73b | 2.69642 | -60.68911 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb5699e9-3bfa-393a-892c-c283d785a964 | 2.7205 | -60.67706 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07267073-2a11-3107-a979-ff62f220523c | 3.02669 | -60.8283 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9db6a44f-8ce0-32c0-841d-b341a3cc973a | 0.30325 | -60.45459 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56eb6d92-49c0-30e7-aa30-820a4f5280d3 | 2.77821 | -60.3403 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1ef58593-655f-358f-b46b-ce32230840f8 | 2.09511 | -60.19837 | 2026-03-05 05:54:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d067a6c3-5147-3314-bbec-3afa1bbd1be3 | 3.1849 | -60.5686 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8cacd7fc-959c-3a3a-82f9-6f981c9f850d | 3.05935 | -60.62499 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54009f0f-e4b9-32f5-a3f8-7f76d400e86f | 2.69378 | -60.70012 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90a454f3-8b64-3e2a-bf88-49275b5bb0db | 0.76956 | -59.89682 | 2026-03-05 05:54:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e675ee4e-53a5-3830-b38b-436fd241d253 | 2.69738 | -60.69549 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 84559979-20c1-3292-a0a4-3b843f379966 | 3.18426 | -60.56461 | 2026-03-05 05:54:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e73c76fe-6c41-36ca-9c2b-367cc7f51943 | 0.46906 | -60.32408 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea3f5626-d6b9-3690-977f-2caae5b7087e | 1.00701 | -59.51317 | 2026-03-05 05:54:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c7f867c-1446-35c1-8649-cba627c2c6d5 | 1.51009 | -59.90533 | 2026-03-05 05:54:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a7ef8e3b-5f66-388c-a1c4-696e73f81bb5 | 2.9589 | -61.08469 | 2026-03-05 05:54:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ee6274ca-579f-3ce4-960d-c715ebfa69b4 | 2.69976 | -60.68297 | 2026-03-05 05:54:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f6c5b21-6ef2-3a4b-8cf6-853f3cc859f8 | 3.51183 | -61.90323 | 2026-03-05 05:54:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d49844c-0d7f-3447-b74f-695e94c5b470 | 0.49577 | -60.49767 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b62e934-5d8f-385e-81f7-04b88e600ae5 | 0.04342 | -60.97773 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec076f95-a0d6-34c7-ad1c-e441604e9e94 | 0.45774 | -60.39951 | 2026-03-05 05:54:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad32534f-8af0-3981-9be0-d0a02f99a76f | 2.7816 | -60.3528 | 2026-03-05 06:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7a91ac67-ad62-3bdf-99a3-3a57c5e1e5e6 | 2.7816 | -60.3338 | 2026-03-05 06:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 134.6 |
| a22e20ed-d6bd-3fff-bb66-1da17f3c5c55 | 2.7816 | -60.3528 | 2026-03-05 06:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 48692def-352a-3e51-a8e7-77fb04ae8f45 | 2.7999 | -60.3335 | 2026-03-05 06:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 63303cf1-db92-35b0-925a-5c2821fedf6b | 2.7816 | -60.3338 | 2026-03-05 06:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 718a3309-0581-359b-9c3d-708270b32c61 | 1.5047 | -59.9116 | 2026-03-05 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b5639ba9-035b-3255-9fab-86aeb6d163c6 | 2.7816 | -60.3338 | 2026-03-05 06:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 102.3 |
| d3ae0af7-8d1c-3f15-98d9-470add247f77 | 2.7816 | -60.3528 | 2026-03-05 06:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e0e34a03-4c75-3999-bf22-4ea2d7a62980 | 4.9623 | -60.26259 | 2026-03-05 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 225a8ef0-e565-3824-a91f-1b062df8b15b | 4.9603 | -60.25874 | 2026-03-05 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 553a7003-9e29-37db-bdc9-7d2ed41274d5 | 4.96125 | -60.26406 | 2026-03-05 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a00e82f-c60a-3949-b9bd-b341b4d14d79 | 4.96981 | -60.26752 | 2026-03-05 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebe5157e-8d06-309d-966e-9ba0dd850a91 | 4.96771 | -60.2633 | 2026-03-05 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da980e22-407c-3785-a2c3-155bc1d1b2b0 | 4.96336 | -60.26837 | 2026-03-05 06:22:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09356c6a-51b9-32f1-95c4-d9af3f8394df | 3.03335 | -60.80997 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3a51fc5-5f9a-31b7-9553-6ed4291e4ff5 | 3.06929 | -60.63237 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 416ad1c2-743d-34ca-8159-12fcca7072bf | 2.72346 | -60.66994 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d4801aa-9142-36b2-bccd-cb0616e334c8 | 1.51138 | -59.917 | 2026-03-05 06:24:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73604acf-b2ef-3236-bc98-2e2438076d9f | 2.96676 | -61.04826 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98b9d0c6-6fdb-34f1-a584-3a2dd3824d67 | 2.96097 | -61.09052 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde0cd9f-ee85-3af1-ae07-16e1a8bf668b | 2.96266 | -61.10048 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d693c4a2-48ac-3579-995e-8617229b9762 | 0.04279 | -60.98837 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 856b312a-b0b5-39b7-8cfc-b66f4a3bd803 | 3.50799 | -61.90574 | 2026-03-05 06:24:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed55397f-83c1-3768-a819-b4ac52260ed4 | 3.03448 | -60.81153 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5e25095-fd1b-344e-b636-9eb754a27e0c | 2.70054 | -60.68986 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 395533a4-b3d3-3a8f-aa33-8c936401a9b5 | 2.78976 | -60.34669 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 70181a87-fedd-3d3f-b772-6cc8127e6975 | 3.50873 | -61.91005 | 2026-03-05 06:24:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b50629b7-96a8-3d61-8fdf-dba27b77f818 | 0.03706 | -60.99483 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6c21f5e-75bc-301b-a913-635e89a55e6e | 2.78516 | -60.33581 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 47527aea-e1cb-3a3a-aac3-43bf987e5eb9 | 1.51167 | -59.9197 | 2026-03-05 06:24:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7544affc-fd70-39b9-9011-cedf89424cfa | 0.04189 | -60.9828 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a44b643-09b9-318d-908e-cb66c260f948 | 2.95385 | -61.08664 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c868cf05-733b-3c3e-90d9-4b916d959e11 | 2.69474 | -60.69701 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9094a958-6dbf-3304-98b3-f1e9f1bddd87 | 0.47882 | -60.32883 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e7179fc-afec-331c-ac45-caa9a99c84f4 | 0.47782 | -60.32267 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c616bca2-c4a2-3aba-9b25-e89872cf8bdd | 2.72435 | -60.6753 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 254dee77-5ea0-39c6-9f41-beaa5134278a | 2.78883 | -60.34114 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 86b08027-70b2-33dc-b3cc-b31ddf87532a | 2.6994 | -60.68523 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a2cd591-6c4f-3615-bf91-26ac69708ead | 2.72359 | -60.66936 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d76b952-e287-3b38-9faf-e0161acb38ac | 3.28203 | -60.74554 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c853efa4-0d21-3a34-b824-6c5c4d73bc56 | 2.77942 | -60.32532 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 741b4f44-cefe-33df-b531-8002804bdd67 | 3.28751 | -60.73922 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0df9b115-f036-3668-8824-547765c7d3a4 | 2.7871 | -60.34698 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0718c1eb-c1c6-3cf7-8e5a-59b179161683 | 2.77856 | -60.33688 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1c27d604-83ff-31d4-9b08-9eace99cabb5 | 3.04087 | -60.81044 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e3dab8a-80ba-39d0-9f20-0dffc24ca95b | 2.78319 | -60.32444 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8bcb2071-1343-3731-aa2d-4a5b45254720 | 3.28137 | -60.74635 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc004f24-ed9d-3ead-9535-662fd0ca69af | 0.47099 | -60.3238 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93638b1a-8f9d-3ee8-af3e-93db598ab2bf | 3.036 | -60.82561 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f5ec68d-7f8d-300d-8f09-83c1b950bab8 | 2.69594 | -60.70157 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d031733-1aac-3491-875c-737339c71862 | 0.66505 | -60.30418 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db474717-b5ae-3add-9657-7b84a354319e | 1.51069 | -59.91381 | 2026-03-05 06:24:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abc4246d-4c9b-3b8e-b84e-15f3d8a7ef4d | 0.04759 | -60.97612 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3065ff9-4095-3204-acbe-7dc0957419ce | 2.78051 | -60.34812 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 403fdf4f-2a16-38a2-a2f3-a415521b7e9f | 0.04943 | -60.98755 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d104c908-a640-311a-823c-ea2f63d85004 | 3.2805 | -60.74113 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab37007b-cadf-30af-b41c-b304e85c7197 | 2.77954 | -60.34251 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c1129c1b-fe9a-367f-953d-feed9680c0e4 | 2.77758 | -60.33125 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1ed928b4-6e59-3d3b-ae3d-4a8cc9866dd5 | 1.50969 | -59.90769 | 2026-03-05 06:24:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 636906b2-47a3-3fce-9a42-6d8fbb1e93de | 3.03973 | -60.80887 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bc2f16a-63e8-35ea-bc83-7248b6084b76 | 2.78224 | -60.34228 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0be3193b-4459-3a10-a707-faba3f59f808 | 2.22864 | -60.22531 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67c6e603-15f0-3b75-affc-e3e3a011c472 | 0.47199 | -60.32991 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4ff6e22-1395-3887-8b27-fce0a5f9b564 | 2.78417 | -60.3301 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 85f3ecec-01a5-35a3-b0df-0d926b41b4f6 | 0.05691 | -60.99193 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d614e9f0-6584-3e3a-9e9b-2d18efcf7a02 | 0.05607 | -60.98669 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09edc8f9-6cc1-39ed-8903-78739d9dd07a | 0.04366 | -60.99377 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e337736-38c9-3f71-8abd-c29d62aa559a | 3.06192 | -60.62816 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e7bbe74-a8db-35bb-ad2f-663b0745fe41 | 2.78317 | -60.34787 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 620f9d1a-fad4-3014-b3a2-96e45ccc2e8d | 2.96012 | -61.08553 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23f0b065-d45b-352f-86a5-a4ea53ac74a7 | 2.7003 | -60.69056 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8979aef9-cc6f-3511-9282-3cfa5933f33d | 2.78036 | -60.33098 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bc76f556-8611-3361-965a-b0e7bdfef324 | 2.7813 | -60.33665 | 2026-03-05 06:24:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 193ffa0a-aca3-3d92-8114-3e2ea6a6ebdc | 0.04098 | -60.9772 | 2026-03-05 06:24:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 12743957-1450-3675-9fd7-970e55da7904 | 2.69501 | -60.69628 | 2026-03-05 06:24:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 348d596e-bd8a-3da9-8049-0a087dc3a1d8 | 1.50335 | -59.91147 | 2026-03-05 06:24:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc334fac-4bd5-3fe5-b8fa-60c3ba145216 | 2.96809 | -61.09439 | 2026-03-05 06:24:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df2e2943-d7d0-391b-bead-d6800f63875c | 3.02962 | -60.82671 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40a59729-59a5-37f0-a7b9-6b57148ad3ad | 3.28112 | -60.74033 | 2026-03-05 06:24:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
