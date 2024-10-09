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
| 2af302de-3598-32d6-ab89-990ce486e77e | -9.47478 | -57.92249 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 047d073c-e3da-3a5d-b6da-afb0a3a3c150 | -9.43439 | -57.8302 | 2024-10-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b35eefcb-9945-3359-976e-8e09e8b98b6e | -9.43381 | -57.83381 | 2024-10-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87882c71-4158-3f11-8120-6a2ed0fe4b09 | -10.00983 | -57.91209 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb46187c-d530-35a1-afff-d7ec139f62ae | -10.25773 | -56.76344 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b473c46-8cdc-3a30-9157-76664ed27d23 | -10.25498 | -56.75941 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51415830-8f67-32b0-9864-f75812818582 | -10.25443 | -56.7629 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91982712-5c02-3ed0-a741-645aea13c5ab | -10.1317 | -56.76438 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 778f8950-a290-3c96-90f1-43e82ab0826f | -10.1306 | -56.77136 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3013a319-5363-3956-a05e-c7ba36e98711 | -10.12729 | -56.77082 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d48c764-6cfc-3889-8e3c-7fb25d306297 | -10.12674 | -56.77432 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98f04c32-2c93-3d0b-822e-c1cc6764f590 | -10.12619 | -56.77781 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b617c5f9-5817-357c-8f50-4ced3d9270dc | -10.12344 | -56.77378 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dae81827-b973-3148-aa61-e0c8597fbbb4 | -10.12068 | -56.76977 | 2024-10-09 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1fe5415-23f5-3314-bd00-15f3959985a6 | -10.3341 | -57.50259 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d86211a-63ac-33ec-9552-2048c22e057d | -10.33353 | -57.50613 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4602d70b-0602-32b2-872f-fc26bc431cf7 | -10.33297 | -57.50968 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 574bb0d6-877c-35cd-bc7d-2bde27e81613 | -10.33077 | -57.50204 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cea88e5-dcb5-320d-bf2e-aaeb7e4258c7 | -10.3302 | -57.5056 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aec1fcd9-b01a-36f7-aba6-22e31564262e | -10.30672 | -58.03078 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdd24fc-4bbc-32b3-bd41-08ce6112173f | -10.30267 | -57.97056 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 185e273b-e460-33d1-94b5-dd25bcb1754a | -10.28247 | -57.91222 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4ad990b-8824-3d79-a989-981c981c601a | -10.28232 | -58.20271 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 271cc249-fb34-3b0b-8b7d-6c72283e4ee7 | -10.25144 | -57.95534 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bbbf2df-9757-3ba7-a884-ccc4b97edbd5 | -10.23149 | -57.82253 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36f306a3-2eb3-35f8-b3a1-1bc5a696056f | -10.23091 | -57.82612 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3945683-985d-3b65-9e93-e3b2b0ab780e | -10.2293 | -57.81479 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18cc3b5c-3ffd-3d5d-8b12-522676c5d9ab | -10.22872 | -57.81837 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b652ac12-a54e-3665-8b7d-b521d44e9f21 | -10.22814 | -57.82196 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59228204-4b52-3079-adb1-19c3ca8439bd | -10.22756 | -57.82556 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f4a7ebb-3ef9-303d-acc2-f19469e82d74 | -10.22653 | -57.81066 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2330f0f-d655-3350-b670-312d1afcc1a3 | -10.22595 | -57.81425 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5caf57c3-95ed-3bd0-812a-06951b816e51 | -10.22537 | -57.81783 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d8fc59c-2499-36b5-bdae-c46807fef93b | -10.22479 | -57.82142 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3368261f-e065-3b56-9436-464a4ebcc9a2 | -10.19928 | -57.95792 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cedfad4-944c-3a97-87d5-6c8f94539a8f | -10.10024 | -58.00499 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8f4325-03bd-3cb4-bf7f-67fb6aa63621 | -11.81042 | -58.5126 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afe83c74-6147-32fa-bdf5-8dffd549db10 | -12.29544 | -57.88158 | 2024-10-09 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cbf8019-76b7-3c65-8245-05a0d06060f5 | -12.29487 | -57.88514 | 2024-10-09 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7719765-c245-32e5-93c9-c9615af9339b | -12.29211 | -57.88103 | 2024-10-09 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc2a9dc4-54ac-3745-835f-58c79dd8c9da | -12.29154 | -57.8846 | 2024-10-09 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 827df3ac-aeb2-3654-8534-c4a75fd3fa04 | -12.00306 | -57.81839 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6637f5ec-df40-3c00-8ce0-b807475b37e0 | -11.99974 | -57.81783 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 202e40a2-07de-3b12-8d94-d3bddc246e88 | -11.99641 | -57.81727 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9319894-ecdf-3c9c-8acc-af6f73a0fca5 | -11.9664 | -57.6015 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c842d9-74fb-357b-8776-239b87691a0b | -11.96584 | -57.60503 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5b47a96-ede4-37ec-b1e6-c9a06dd5f767 | -11.96309 | -57.60096 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d71a49-c749-3ab3-8929-abe6274fd027 | -11.96253 | -57.60449 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f83b4e2c-73cc-3cc2-bfc5-333a101c932c | -11.96033 | -57.59688 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b99222f0-eccf-3faf-b1e5-ee1cca03fbfe | -11.95977 | -57.60042 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e2f61bc-d82a-3568-9be5-3258de3ab518 | -11.95701 | -57.59634 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dc2480f-23a9-32a5-a30b-d65a80ebd94b | -11.8993 | -57.4674 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de1119bc-b56b-3ecc-9fb5-41d7eb3073ef | -11.89598 | -57.46686 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ef1b7be-c08e-3175-90ba-00426c196db4 | -11.89267 | -57.46632 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9364108-0ec5-388c-94b8-93d796080de1 | -11.88936 | -57.46577 | 2024-10-09 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d14d99d-5c5a-383f-bc60-b863a4072ffd | -11.54119 | -57.32621 | 2024-10-09 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 270de691-5567-3faf-b63b-aef6d58aa16e | -11.36343 | -57.2688 | 2024-10-09 05:04:00 | NOAA-20 | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d77528d-2666-3e05-ba6b-37d46c9dbdab | -11.36287 | -57.2723 | 2024-10-09 05:04:00 | NOAA-20 | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99684854-c36d-3339-92a4-85b9c8fcafd5 | -11.36012 | -57.26826 | 2024-10-09 05:04:00 | NOAA-20 | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cea594a-6dd8-310d-984f-171345432178 | -11.35956 | -57.27176 | 2024-10-09 05:04:00 | NOAA-20 | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5db391e-5747-371e-abda-bebe6c4453c8 | -15.10377 | -58.36216 | 2024-10-09 05:04:00 | NOAA-20 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b0cad911-60ac-323a-96c1-243f5eb69fd3 | -14.92827 | -57.9266 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d76f0a4-78ee-3b98-8dcf-2b19d3dddca2 | -14.92771 | -57.93015 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99990dfe-0a3e-342b-a24e-7c0bdd8ed171 | -14.92496 | -57.92605 | 2024-10-09 05:04:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549a46e6-bd1d-3459-9955-a22d86c12005 | -15.12542 | -59.02447 | 2024-10-09 05:04:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d97624b3-33b3-3a8e-b889-f64749798315 | -9.20866 | -59.37385 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d476983-7ba7-3079-8865-f6257a92421f | -9.13651 | -58.90889 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2976d6f-5be6-3317-9c91-1896bd9bacbf | -9.13301 | -58.90833 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ea7f88d-c031-32aa-9669-93ef08e02062 | -9.12886 | -58.9117 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf4d50f-7fcc-30e7-b823-ed38db3dd168 | -9.11188 | -58.99404 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aede6a2f-1570-3676-ac43-932c606f05ea | -9.10837 | -58.99341 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2cb572b-d109-3655-82de-e76f4af509bd | -9.10104 | -58.97203 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2279d882-1f93-3593-a543-420949a77092 | -9.09644 | -58.89009 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bf72292-83e2-3311-b150-bc0bcc91b34a | -9.09579 | -58.89404 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cb74cd1-060c-3c2c-b75f-4cd3e3e09ade | -9.87761 | -58.33801 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cc9b701-d573-3711-89fa-23bca0ad574f | -9.87701 | -58.34172 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bc30ebe-81b2-3962-add3-b67a42825079 | -9.68963 | -58.19796 | 2024-10-09 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0708931b-2a64-3204-ba96-7b252c9c9809 | -10.04507 | -58.38809 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6552d3b-a30d-33d4-9be7-19bd667e0bae | -9.9945 | -59.53587 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdd06e15-4128-3b39-a9cf-57c7520a5710 | -9.505 | -59.0078 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69b8cb88-5996-3876-93af-2a5bb9d8ec2b | -10.40037 | -59.13862 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76b17854-eac2-3080-ab8c-a3b22cc4a4bb | -10.39688 | -59.13806 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c332a7c-1ad3-39da-b6fc-aca4f775a18d | -10.39403 | -59.13354 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61e76c58-ec6a-3cdd-8902-9bf05e28d8eb | -10.36005 | -58.88462 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fd89499-0b6f-32c7-bf0c-f2a4dd2101b5 | -10.24024 | -59.14485 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8398b563-c25c-3977-a930-d6dbdd0561f2 | -10.21928 | -59.4031 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4cc67cb-e69b-3341-8837-ca7ab1278618 | -10.20026 | -58.79203 | 2024-10-09 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7146ce7-83ca-33c6-b837-d43691e4a7c7 | -10.19964 | -58.79584 | 2024-10-09 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75849568-f999-3bdc-b5b2-8bb8dcd4feb4 | -10.19901 | -58.79969 | 2024-10-09 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b383ffc1-35cd-33aa-899b-e6609e738755 | -10.19838 | -58.80354 | 2024-10-09 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91baa727-81b5-34af-9e91-9c7c4434f103 | -10.19492 | -58.803 | 2024-10-09 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35867e3c-0e76-33c5-9d0e-9929c49b8641 | -10.06004 | -59.35718 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e62066a4-a029-3702-a488-4a4184bfd908 | -10.02146 | -58.77185 | 2024-10-09 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d32def50-6222-3cad-bece-dc143f39a585 | -12.31729 | -59.17224 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f268b20-b9a6-31bb-a917-6eb1dd10c49c | -12.31666 | -59.17605 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea3d33b5-7ac8-3654-89ab-b781b968ce37 | -12.31385 | -59.17167 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8707ad5-c9f7-31b9-a43c-165ca8a9e09f | -12.31322 | -59.17548 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95bcdde1-b269-38f1-b925-8de885ef68b0 | -12.3126 | -59.1793 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38d70667-e142-3284-9305-7f3e1b7e9843 | -12.30979 | -59.17492 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 92ebc4ad-220f-3ef4-8ae5-8e5623e4814d | -12.30916 | -59.17873 | 2024-10-09 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README178.md)
