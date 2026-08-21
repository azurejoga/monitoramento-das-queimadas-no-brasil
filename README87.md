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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac0d6329-cb97-355a-b932-fea69c96518a | -6.2341 | -55.6109 | 2026-08-21 07:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 76be8e95-573a-36a5-82d8-005d42952973 | -13.3926 | -54.3758 | 2026-08-21 07:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a1e6f180-a4fa-3373-80a8-25afdcd443a1 | -9.4072 | -60.3977 | 2026-08-21 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| e58eb3e3-8cf5-36bb-ad6d-38032e53a0f7 | -11.1747 | -54.0216 | 2026-08-21 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 95080943-935f-3679-a659-cfbe200dfc68 | -9.4072 | -60.3977 | 2026-08-21 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 4dca7d30-f22f-32c9-9cd4-45a1d803e266 | -13.3926 | -54.3758 | 2026-08-21 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9cbb52f0-872e-3807-aab7-1cbc64512952 | -7.3603 | -45.8136 | 2026-08-21 07:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 6c045b4f-6d1c-3699-8a44-e93d8b8ca4ee | -9.4071 | -60.417 | 2026-08-21 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.5 |
| 78891052-1847-30da-b2bb-28b575330a26 | -10.8078 | -50.2693 | 2026-08-21 07:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 0edabc03-dfeb-3e78-b1ae-1804e1d46319 | -9.4257 | -60.416 | 2026-08-21 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 715f99f8-0b46-3856-b9e0-10b1b0878e2a | -6.8755 | -59.4364 | 2026-08-21 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8c4d7436-3e4d-396e-a400-33169e2913df | -6.1177 | -59.9069 | 2026-08-21 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e8d7c5ac-5dc6-33e0-b213-3b6e1173544f | -6.2341 | -55.6109 | 2026-08-21 07:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9bcf8e74-0379-3329-b674-1286e799dc42 | -9.4069 | -60.4362 | 2026-08-21 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 9e446cb1-7d1f-3626-805d-a306f4c61b65 | -14.3149 | -51.8969 | 2026-08-21 07:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e2a829ef-7fda-3ff3-b393-65fcc8bd9265 | -11.1747 | -54.0216 | 2026-08-21 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f36d6a3b-8a6f-3ee6-ae06-4dae5fa9ed9b | -6.8755 | -59.4364 | 2026-08-21 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 629786d6-8738-317c-8f7a-d7452781f0dc | -9.4072 | -60.3977 | 2026-08-21 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3394f689-101b-3764-9390-1ab44c815d9b | -6.2341 | -55.6109 | 2026-08-21 07:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e31a333d-8e26-3750-84a6-1b3a257057a6 | -13.3926 | -54.3758 | 2026-08-21 07:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| da7db4b1-db74-32ab-922c-2e6edb772e7c | -9.4257 | -60.416 | 2026-08-21 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 92553adb-7198-3b73-9089-cbbebf0f4b6e | -9.4069 | -60.4362 | 2026-08-21 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 775acd35-395a-3c62-98ff-8cd120faad88 | -9.4071 | -60.417 | 2026-08-21 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 5591c498-8a1d-3103-b0a7-3ee6f6262344 | -7.3603 | -45.8136 | 2026-08-21 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ec04e1aa-6364-3e4a-bdc0-685f7b70409b | -13.3926 | -54.3758 | 2026-08-21 07:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| d09266fb-4484-3e95-9e89-2918369c55ff | -9.4072 | -60.3977 | 2026-08-21 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 48cd5df4-f452-35cb-baaf-fe3909a7806d | -9.4069 | -60.4362 | 2026-08-21 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a7772126-82e4-398b-a093-b47e5e11cc04 | -9.4071 | -60.417 | 2026-08-21 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 89dd1969-7423-3fb6-9694-bdf312b341e9 | -6.2341 | -55.6109 | 2026-08-21 07:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a9955a2b-cec2-3c9f-af09-23f77df47892 | -13.4324 | -51.776 | 2026-08-21 07:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 78d0c4f4-6d92-3081-93f4-6cbbb1e89676 | -6.8755 | -59.4364 | 2026-08-21 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f370467c-d092-3314-af42-d5a5bb74d8e8 | -13.432 | -51.7973 | 2026-08-21 07:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 7e16c473-e1ff-31bd-a98c-56cca47584c9 | -14.3149 | -51.8969 | 2026-08-21 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| b351c9f5-da7c-388c-8e93-43f74196e1f3 | -14.3153 | -51.8756 | 2026-08-21 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 48c56c31-519e-3c53-b924-02f8822cabad | -7.3603 | -45.8136 | 2026-08-21 07:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| ae104327-ebcf-3bff-8b56-b15b9558a001 | -6.2341 | -55.6109 | 2026-08-21 07:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f397cc5e-723d-3c92-b59f-42fe60028fe4 | -13.6624 | -51.7897 | 2026-08-21 07:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9d23e1f0-da69-30f5-8263-6bd347048ca1 | -6.8755 | -59.4364 | 2026-08-21 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6ecf238a-d034-39ee-8b3d-020b76951732 | -9.4071 | -60.417 | 2026-08-21 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 178af15f-7162-32fc-92e0-f0c2df915bac | -9.4069 | -60.4362 | 2026-08-21 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 48b9de34-72b5-340b-8e6e-c632ab86a16f | -9.4072 | -60.3977 | 2026-08-21 07:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3801d944-0b16-3b68-84f0-88c217c5fa9d | -14.3149 | -51.8969 | 2026-08-21 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b2de3dc1-07ab-385c-9702-08c8827d450c | -13.3926 | -54.3758 | 2026-08-21 07:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c86cffd9-d808-35ed-b2e8-a7f5fccc68b1 | -9.4072 | -60.3977 | 2026-08-21 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| fe16de6d-010f-3a0f-9ea2-1c104b39fbcc | -14.3343 | -51.8944 | 2026-08-21 08:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| a2e77ab0-2571-31c8-938c-5f08ca8b2948 | -6.8755 | -59.4364 | 2026-08-21 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b056e09f-e8c9-3db0-9223-72aec6ef268e | -6.2341 | -55.6109 | 2026-08-21 08:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ed0d274e-38cc-314d-9a1a-0f335301c2ba | -13.3926 | -54.3758 | 2026-08-21 08:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a2c7c817-4407-349c-92dc-acb91eabd9e1 | -9.4071 | -60.417 | 2026-08-21 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| ba70e343-ebc6-371a-8265-64afb889c9fa | -14.3149 | -51.8969 | 2026-08-21 08:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 3b60032d-237d-3c97-9ea6-46c1607fdb36 | -7.3603 | -45.8136 | 2026-08-21 08:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 33560a4e-b35c-3c60-8338-d6070444244e | -11.1747 | -54.0216 | 2026-08-21 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8f565cd3-9713-3c0e-8e7c-f739ee166846 | -9.4257 | -60.416 | 2026-08-21 08:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 15b4874a-fd2a-3e62-9ca6-bada3713a72f | -9.4257 | -60.416 | 2026-08-21 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7c6a4e1e-cea4-39a6-bf59-cc0e4a7cf74d | -6.2341 | -55.6109 | 2026-08-21 08:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c784c50a-b7b7-3383-9e72-07fc48dcd97f | -13.3926 | -54.3758 | 2026-08-21 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 41cba739-1808-3cd8-84c5-0232b636c94e | -6.8755 | -59.4364 | 2026-08-21 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 4690f52c-d64c-3a90-ba01-e87479d3b630 | -11.1747 | -54.0216 | 2026-08-21 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b7e5a874-b485-3f5b-a154-ca7f6305e93f | -9.4072 | -60.3977 | 2026-08-21 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| db50b40b-7b67-3644-87c0-6cd1897346e1 | -9.4071 | -60.417 | 2026-08-21 08:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 0403e246-78e9-3a13-aee8-6a18543e2ffb | -9.4071 | -60.417 | 2026-08-21 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 18b050fc-38d4-3b48-819f-59d0e93e175b | -11.1747 | -54.0216 | 2026-08-21 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 20a2edc1-22d3-3b07-b885-1a09a66aca9b | -13.2431 | -51.6295 | 2026-08-21 08:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| a35326d4-899c-3f93-893f-fa60750b2fc5 | -9.4257 | -60.416 | 2026-08-21 08:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3f083753-74b1-3f5d-bf30-4e8d4a6cfec2 | -6.8755 | -59.4364 | 2026-08-21 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 36554ac3-1fb3-3ccd-b10a-60e943b54962 | -6.2341 | -55.6109 | 2026-08-21 08:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0fc05111-00ca-3d99-a244-01438f5d013d | -9.4071 | -60.417 | 2026-08-21 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| a6c1f632-f5cb-3d98-abb1-d3cf97e3333c | -13.3926 | -54.3758 | 2026-08-21 08:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0708b3f8-34f3-31de-b3fe-60af89ec224a | -9.4257 | -60.416 | 2026-08-21 08:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c19be62c-85cb-3c89-8935-74753203aaed | -6.2156 | -55.6118 | 2026-08-21 08:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 05c07d5a-ee37-3354-b177-5fa23bcbab96 | -6.8755 | -59.4364 | 2026-08-21 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 0d82cb19-abab-362a-afdd-375c2d8b3a89 | -6.2341 | -55.6109 | 2026-08-21 08:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 373227d5-16e2-3963-ad85-1778cc66e30b | -14.3343 | -51.8944 | 2026-08-21 08:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 6b1eba62-a764-3749-ad2d-51bffd2cb29e | -14.3149 | -51.8969 | 2026-08-21 08:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 120b3d33-d614-326f-afca-a042d0577396 | -14.3149 | -51.8969 | 2026-08-21 08:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 31d30ba1-f7c3-3dd2-a4d0-adf478ed12ae | -6.8755 | -59.4364 | 2026-08-21 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3a8eab22-fd29-306e-9932-a40670ce16bb | -9.4071 | -60.417 | 2026-08-21 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| a7f0fc11-b8f9-3353-927f-c31830f09824 | -6.2341 | -55.6109 | 2026-08-21 08:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| de86ba8c-81c6-378b-b443-f95c133909ca | -13.3926 | -54.3758 | 2026-08-21 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 29b40d29-255c-3c41-a92d-48dc2ce8ea2f | -9.4257 | -60.416 | 2026-08-21 08:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 24282796-9338-3d52-a8a5-d36b424fc33d | -6.2341 | -55.6109 | 2026-08-21 08:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a606ba57-625d-3cd9-968e-548ccf24b663 | -13.3926 | -54.3758 | 2026-08-21 08:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 02216b60-9ce6-34b9-a641-fe7fc817eb24 | -9.4071 | -60.417 | 2026-08-21 08:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 9702e01e-a06d-3cab-b488-8d6775b1cd04 | -6.2156 | -55.6118 | 2026-08-21 08:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 84cc827d-0462-39f6-94a3-011c0c6835d5 | -6.2341 | -55.6109 | 2026-08-21 09:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| afae6eed-171c-3f77-afdd-f7e94408bde7 | -6.2156 | -55.6118 | 2026-08-21 09:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 1fd97c56-4640-387b-8c5e-9b3a1630eda0 | -9.4071 | -60.417 | 2026-08-21 09:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| e51efd1c-d18e-35ee-8a36-f4c9d972248b | -6.2341 | -55.6109 | 2026-08-21 09:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f489edfd-f269-3e56-a901-940e87457435 | -6.2156 | -55.6118 | 2026-08-21 09:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 167258d8-cea5-38ea-8c8d-10e9fc77bbce | -9.4071 | -60.417 | 2026-08-21 09:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 653606c6-6c55-3168-93eb-95cacbea49fe | -9.4071 | -60.417 | 2026-08-21 09:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 8302fde6-b891-3b92-8201-fc97ef04c91f | -9.4071 | -60.417 | 2026-08-21 09:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 2603e65e-6588-33b0-8e8f-e0cba95cad99 | -9.4072 | -60.3977 | 2026-08-21 09:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9fda474b-1d2c-3052-ace3-6f47a0bfa250 | -14.3343 | -51.8944 | 2026-08-21 11:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 397a7b65-c387-3c73-9e65-a128fe122773 | -14.3149 | -51.8969 | 2026-08-21 11:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 177d1af3-3578-388b-b3c3-3c6b640bfd85 | -17.9546 | -44.3882 | 2026-08-21 11:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| aba6091d-c7b8-3bfc-a7ab-d954333f8640 | -17.9546 | -44.3882 | 2026-08-21 11:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4d445d59-6f9b-32f8-b193-e1c3cc556c94 | -14.3149 | -51.8969 | 2026-08-21 11:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e40e4f85-004d-367d-9a46-dfd8e4a98564 | -14.3343 | -51.8944 | 2026-08-21 11:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a40fab53-fd5d-32af-8ab2-386441091ddb | -14.3343 | -51.8944 | 2026-08-21 11:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |


[Clique aqui para ver as próximas entradas](README88.md)
