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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56a394ab-deb6-3cd0-9fb0-5244f9ba6122 | -7.01384 | -59.40466 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 872f5a32-8ca5-3494-91d3-6253dec09ebc | -7.01383 | -59.36073 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a5f25fe-6834-38a8-8ae4-94bee823ec1d | -7.01228 | -59.39804 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ace90ed-9c31-3897-b582-5a0f39ea98a4 | -7.01172 | -59.40228 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2338bcc-767d-3f8d-bef5-cd440eb60597 | -7.00492 | -59.38161 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 459205db-c454-3512-a800-81142d8a64df | -7.00433 | -59.38594 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac3d3b04-a01f-3e54-8703-d8f0787bd0cd | -6.999 | -59.38071 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f06344a-1cc3-3c4a-8227-8639fd0cae81 | -6.99842 | -59.38499 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28799224-ee34-3a16-8395-342daf28b947 | -6.99783 | -59.38931 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c01d976-3843-3206-8191-12a171598fcc | -6.99249 | -59.38416 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c6c2ae4-50fa-3241-b35f-a127eadb3ab4 | -6.78134 | -60.10368 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0346dc1-f31f-32e3-8d5c-293e3febbaa0 | -6.77568 | -60.10302 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d48d214d-eee1-3020-835d-22ee36524d40 | -7.15312 | -59.29745 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbfa5c3b-587c-3b9c-b10c-61f30e621593 | -7.15251 | -59.30183 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 742072bb-475e-365f-afac-b86ad2c03036 | -7.15024 | -59.29601 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d996f80-a725-3033-a22f-357be8afeea1 | -7.14967 | -59.30041 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| edee66c2-bffc-3efc-a02d-faf288924a81 | -7.14714 | -59.2966 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8af99534-0cf0-3fa7-988e-2591ef318de4 | -7.14654 | -59.301 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b676688-e717-36dc-9adb-a63ae2b5d424 | -7.14427 | -59.29515 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b451d028-e40e-374d-8f03-2d5673a2423a | -7.14369 | -59.29956 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc193c01-efc7-3a83-b814-d46a2e6c60b2 | -7.14117 | -59.29578 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 682e56a2-3864-3899-90d7-397454aebb67 | -7.14056 | -59.30019 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b46dde2f-0f79-39c4-b949-df5d262f97f3 | -7.13771 | -59.29874 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2434f950-eb5f-3ba3-9e74-e6754c786289 | -7.13714 | -59.30318 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c99c646f-1db3-30d9-92ea-2ca85783722e | -7.13458 | -59.29937 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 822448c6-8d7c-3a59-a8d5-e87f0793ab87 | -6.7264 | -59.08306 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c4638bb-7d46-38a1-862a-bf27910c2a25 | -6.72039 | -59.08211 | 2024-10-06 05:59:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dabb538e-a531-3980-bd06-d4628863e6a3 | -9.27299 | -60.82568 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1272ab63-d116-3c1c-8474-406a827efe64 | -9.27249 | -60.82944 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6442581f-4a07-378b-a2de-fcea985c230a | -9.27199 | -60.83316 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aea993c-ccde-32b7-b115-6f5ca1ef10c9 | -9.15397 | -60.66116 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40efd260-e7ab-3053-b3bd-55d6d88c2f94 | -9.14836 | -60.66038 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a46e1a43-5319-3acb-8645-8b56a813277e | -9.14786 | -60.66422 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acfb80a9-d2f3-305f-bace-f957cab43ece | -9.14273 | -60.65962 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0038b8d9-c7e7-3312-b952-0ebecacaf704 | -9.14223 | -60.66347 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 042474ba-5956-300f-ae0f-f0c139afefab | -9.13711 | -60.65884 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af28c80c-81c2-365f-bf75-5261df20d5c3 | -9.13661 | -60.66269 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3474f25-a2f1-33d7-bd8b-76b2f3bb2236 | -9.13149 | -60.65806 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdb2c4bf-9ac9-3a1b-b772-0bb116dc44bc | -9.131 | -60.66191 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d9d82d0-76be-30c7-86ef-c7c76a109455 | -9.12587 | -60.6573 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe72ddc2-8a46-351e-9ddb-1e0c787cec75 | -9.12538 | -60.66113 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b808c85-83ff-37a8-86ce-9643f4a5a616 | -9.11976 | -60.66034 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf58d924-cf56-32d9-bebe-5a470424ec1a | -9.12195 | -60.39997 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 849d16e0-a92f-3bca-a036-81a0ca38d1f6 | -9.12143 | -60.40397 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa2989ca-b3fb-34a4-93d8-a7f03336fbbe | -9.11817 | -60.39912 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e57cecbb-0391-3f83-ae51-060ab4541536 | -9.11767 | -60.40315 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea680863-f3be-3c1f-a86e-d093b9350441 | -9.11571 | -60.40318 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6915781-1010-39c7-b6da-b23806311291 | -9.48406 | -61.0134 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c657e529-4a1c-316a-8913-a73cd8c046b7 | -9.48359 | -61.01705 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64a1b9dc-b0ae-3c07-83e1-120f878639ee | -9.48351 | -61.0165 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f0b7606-e9c2-3497-95c5-2cca1ef03826 | -9.47854 | -61.01258 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 543760ba-ede9-30dd-aae4-495cfeac7262 | -9.47808 | -61.01627 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bf40a8f-3b4b-399d-97b1-dee5ff524dd3 | -9.478 | -61.01572 | 2024-10-06 05:59:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c64e4e02-5141-3464-8d41-db7b7f6098c8 | -9.87795 | -60.31939 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8017c1ff-38f9-3ff6-a99c-db9a45f6b5b3 | -9.87779 | -60.31979 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26cdfa84-15d6-3a5a-9877-634125b92a37 | -9.87742 | -60.32348 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9bd8bb7-d58f-3d7b-aa40-9c7ed302bcc8 | -9.87161 | -60.32272 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49adadcb-34a0-362e-9a3c-8d341e8097bd | -9.87149 | -60.32309 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71f9ebf2-3c38-31f9-86a6-363dff8ea56e | -9.86792 | -60.30559 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b6bbd4b-6d78-3a3f-85d5-a9eedd06930f | -9.86264 | -60.30065 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c784213-3244-37cf-9031-3b4bc53b44b7 | -9.86212 | -60.30474 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2d7e636-f690-34c8-9ddd-6025f6552b54 | -9.85682 | -60.29994 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbdabfe2-3a9c-3d60-b16e-3614502a6064 | -9.8563 | -60.30401 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a2cfa6b-6120-3840-964c-4dff67bd6ef5 | -9.85577 | -60.30813 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 345588be-b1d4-301d-9acf-3bab0815120f | -9.85525 | -60.31226 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86f978be-f30a-35c3-a1d7-d64679619861 | -9.85205 | -60.29104 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 811d6f16-da67-3e3e-8f09-a259881be5c3 | -9.85153 | -60.29515 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc4b4869-5a65-347f-a99b-1e6df62303a0 | -9.85101 | -60.29924 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcf752ae-2098-32aa-aebc-06aac94743f3 | -9.85048 | -60.30331 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dacda7c-1973-3318-9372-f531a8690836 | -9.84996 | -60.30739 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7546c42a-1daa-31d6-b3cd-134d3c314388 | -9.84624 | -60.29026 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cfff51d-a861-3c7c-ab1c-175ec000bd35 | -9.84571 | -60.29441 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 270706bb-b696-3282-bfae-767a98910264 | -9.84519 | -60.29852 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38345558-477a-3490-872a-ac79657b7813 | -9.84467 | -60.3026 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ba0891a-bac7-3c73-9228-0901e2c89cd3 | -9.84415 | -60.30666 | 2024-10-06 05:59:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2483b1ec-31fb-35ad-943d-a72f7869b4bb | -7.98263 | -61.39896 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d535edb6-417c-34eb-967d-f76142633402 | -7.97782 | -61.39492 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e22056f4-09f3-33db-b14f-69533ee8a166 | -7.97737 | -61.39821 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c550c425-88c2-30f7-b514-1825a6c633ef | -7.97693 | -61.40149 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67618d73-1a4e-3486-9169-a4cd7c3fa229 | -7.97649 | -61.40475 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a3ff7e3-9c67-30ac-845f-bf632c1247db | -7.92986 | -61.27706 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1aa781b-15e5-3f17-84af-730d7eae3385 | -7.92941 | -61.28035 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb9d84a-8f0c-350a-aec4-ff6ac1f82609 | -7.92502 | -61.27297 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b532e8d-5c80-34f8-83f6-2e12fe667003 | -7.92456 | -61.27628 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7227599d-2e29-3aa4-bedd-cffb1f1a9b0f | -7.92411 | -61.27958 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b40428bf-73a0-398e-af2c-a2456972336c | -7.27575 | -61.09026 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5597aa68-0357-3f29-ac5e-6834bac2a930 | -7.27529 | -61.09357 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed06f952-9d0a-3d82-a7ec-caf95b3cccf6 | -7.27484 | -61.09689 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 539ed532-7ba0-304f-be6c-fb61768d104b | -7.26951 | -61.09617 | 2024-10-06 05:59:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c67bef6-90ad-33f6-92ae-ab6ac2c78c79 | -9.1767 | -62.29911 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 050637ac-17dd-3f9c-85f7-f868c434de59 | -9.17249 | -61.57753 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8623ea02-6146-3d56-bcd5-78aa0188e6e0 | -9.16807 | -61.57034 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6302df6c-9027-3372-a140-49121104d60d | -9.16763 | -61.57361 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1a5cf187-d8bb-3e8e-ac6e-63daed2741a7 | -9.16719 | -61.57688 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| da8bebcd-4b70-3d50-a4d9-604841259292 | -9.16277 | -61.56965 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 99852028-c043-3511-a51c-a48ab966fb19 | -9.16233 | -61.57294 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f4ddb9c-46c7-349e-9520-98e25fdb7aab | -9.16189 | -61.57622 | 2024-10-06 05:59:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a2d3a40e-533e-3b2b-a5c6-db320675ea44 | -8.37422 | -61.5492 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 187664c0-f2ae-300c-97c4-d858ccd331df | -8.36942 | -61.54519 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 516a2227-3212-3e0c-9ef6-0492508a4967 | -8.22569 | -61.22294 | 2024-10-06 05:59:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README153.md)
