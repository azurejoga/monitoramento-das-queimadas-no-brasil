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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cb78f5e-eab7-33fb-9c21-f191151cb240 | -1.89474 | -54.42282 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5368e59-a9e6-3463-8f32-7d607ea9e25a | -1.89466 | -54.63385 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 027b5366-273f-348d-b2ff-eaee69e9b50d | -1.89418 | -54.42635 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92efe73c-7c9c-3d79-9c7d-02cbfe4692aa | -1.89363 | -54.42989 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cc7e814-2ed3-38b8-b8c3-56128b403e7f | -1.89186 | -54.62974 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 326cb90d-bddf-3164-8447-72aa7309b13b | -1.89139 | -54.42231 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbf8fb3f-5bb0-395f-8a7b-ad7e55bb00fe | -1.89084 | -54.42584 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3ca841fd-ec5b-3136-9a7e-6f2eed54f91a | -1.89028 | -54.42937 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 70f0da9d-7dae-328c-b9fb-4cdc35e188d9 | -1.8886 | -54.41826 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 224f2e85-8b11-3165-919b-f98ac39b707c | -1.88805 | -54.42179 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f26ca072-f5d6-39a9-a1e2-e0ad2f466fe5 | -1.88749 | -54.42532 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 67e1ee41-ff65-3326-a226-c85369db74c4 | -1.88694 | -54.42886 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4a3cbf11-082c-33de-88ab-62df77a540d7 | -1.8847 | -54.42128 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd234db2-72d9-3433-a981-a46161039cfb | -1.88415 | -54.42481 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8aece113-d023-368c-b7b6-4a3601dd1e36 | -1.88359 | -54.42834 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1882b53-6a97-3294-a07f-69f41aabaac4 | -1.88303 | -54.43188 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e138880-ce6e-391e-9f1a-d02f067845c9 | -1.88248 | -54.43542 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86388f42-1bd5-3e23-bdc9-bb034679bab5 | -1.88024 | -54.42783 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 101f18b2-7f35-333b-8f84-ab2ec0da456c | -1.87969 | -54.43136 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 687f13c5-d4d2-3e40-ae60-b5e3a43e15b3 | -1.87913 | -54.4349 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ac6edf9-4d3d-3a8f-b084-d37d3edeca0b | -1.87858 | -54.43843 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6686e65-1de3-3611-9f88-abf403906c59 | -1.8769 | -54.42731 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e34bbe4b-7cfb-3583-87ee-985f93e5b5ee | -1.87634 | -54.43085 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2e7d330-a1f7-35f2-8a3f-254d6a1e4d98 | -1.87578 | -54.43438 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff7ce2ec-108b-3225-a5d5-27fab00221f7 | -1.77178 | -53.51701 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75444001-2bf0-3637-addc-76e734c1c1f6 | -1.59723 | -53.34928 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7553641f-d419-388c-8662-9f1a6134a72d | -1.59393 | -53.34877 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df03fc51-e4ad-3ce6-bfeb-de5de712adb0 | -1.59063 | -53.34826 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abae223a-2754-352f-b30b-965439331426 | -1.39101 | -53.57669 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7cc4c7f-0566-39d8-a0d3-ddfdec297a20 | -1.27862 | -54.12013 | 2024-10-12 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49b93a81-0ce2-3a7c-941c-431efb09daee | -1.26852 | -54.67924 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 68a21c7b-2efa-3071-ac11-fead4dd6bea3 | -1.26795 | -54.68287 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b588de04-361a-366f-9490-6cbd723d7148 | -1.26514 | -54.6787 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40a8ce63-84f6-3dda-8101-e015bc72e004 | -1.26457 | -54.68233 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b48212e3-eaf4-356d-b831-7a5ba8b24914 | -1.26399 | -54.68598 | 2024-10-12 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 669fdf8c-8b62-3aa8-a064-18b0c7eca50f | -1.22911 | -53.37563 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2146da65-afa6-3bd1-8e94-92a194c03f6c | -1.22581 | -53.37512 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90bfa5c8-dd08-3aef-8a7f-6dfcfd1c7ca2 | -1.17416 | -53.39799 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83b86462-775b-34b2-b0c1-3e2a61c50a29 | -1.17086 | -53.39748 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0481162-e06e-3f0e-a06a-edd2bf8b173e | -1.16372 | -53.39989 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8ab4b2f-9667-3a2f-932f-fdcc62538090 | -1.16318 | -53.40332 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4064808e-a795-35aa-ba70-7b9ad27f83e5 | -1.16264 | -53.40675 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34871a56-9c6f-37c0-b94e-2ebda00070e4 | -1.15988 | -53.40281 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 454ff12d-bf2c-349e-a609-1fa34f985cba | -1.15934 | -53.40624 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca4a58b5-8033-3e22-9630-317ee138ec62 | -1.15847 | -53.78082 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6aad50d-ca63-3d9a-bcc0-2ba9f6f44bf9 | -1.13787 | -54.2138 | 2024-10-12 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b7e680-6a34-3082-ba54-1e238d129863 | -1.11723 | -54.06315 | 2024-10-12 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36c9ceaa-d892-37b0-9942-e5e74ac7d7dc | -1.11541 | -53.62123 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| babcc0a7-ecdb-3650-8a89-60eb02f273c0 | -1.11501 | -54.05564 | 2024-10-12 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92589db7-69e2-354b-bac0-a86dff32e143 | -1.11265 | -53.61727 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9bfa315-b33a-3609-a4b9-0a0b6b6a10cd | -1.10934 | -53.61678 | 2024-10-12 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d6299ce-621c-3312-a22a-9e6c5c08ded3 | -1.0961 | -54.2182 | 2024-10-12 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5fca382-8f03-33bd-93e9-46492cda3968 | -1.02925 | -53.735 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78448827-3165-38d3-9b2d-79acba2c9726 | -1.02647 | -53.73107 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 672a3c63-a26c-3b34-baa8-0a9276a61040 | -1.02371 | -53.72709 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce576157-cbf7-3931-bdff-21c9ef87d7eb | -1.02317 | -53.73053 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829b2a32-7782-3049-9f7f-92843cff32b5 | -1.0204 | -53.72655 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3c6db68-219a-313a-b057-a892b8e32723 | -1.01986 | -53.73 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3783295e-8abe-3dfd-a3ff-2a0c95b7d4cd | -3.6724 | -54.07076 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73d9e6e3-a1db-3012-a7ab-a64fbbf1021a | -3.67185 | -54.07421 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 762f241e-05eb-3ba6-a230-4e0785e7e0e3 | -3.66909 | -54.07024 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eab48028-610e-3e59-90d8-1f5a6697388d | -3.66855 | -54.07368 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 498034e2-86a0-340d-b9b4-b6f73a6d992f | -3.61383 | -54.02988 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41db77a-d7a4-35a7-a268-7656072b180e | -3.61052 | -54.02937 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bbac524-ad15-3d6e-bd69-f38b9c9b668d | -3.59985 | -53.94663 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 293795d7-a49f-3924-a49e-7bbad3aa547b | -3.59931 | -53.95008 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24a467b5-1bb1-395e-9fc2-4365ec10b41b | -3.59876 | -53.95352 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6648e2d-fea9-3cbf-997f-58fe968cb248 | -3.59601 | -53.94955 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a30a4eb1-42f6-3aa5-a7bf-d08a41281c4f | -3.51917 | -54.02931 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b08daa-4495-39f8-8be9-b51f0493fe07 | -3.51862 | -54.03276 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cc33f71-c7d1-3d73-b3c2-e60c9d253cd1 | -3.51586 | -54.02881 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c282b9a-b378-3742-9037-7f98cd4fe399 | -3.38776 | -54.08226 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ba03906-1f0f-394c-8b27-7da8a6d3b799 | -3.27823 | -54.17504 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f1128c9-e1ee-34e8-8324-645e206e880f | -3.27492 | -54.17451 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3fde6b1-8079-3e7f-a939-02c99e669454 | -3.27438 | -54.17797 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 749bd192-cdf3-360e-a86a-29ac55c2810c | -3.27383 | -54.18142 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b11270a2-c9fb-380a-b79b-84670d873d58 | -3.26906 | -54.14507 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6842a87e-1505-3e73-9861-866e88066b72 | -3.26852 | -54.14853 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 751f8403-ec5d-3b27-9b65-0cc9fb3c848b | -3.26309 | -54.18311 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c91da2b4-0c78-3e09-87ed-fc19311f19cc | -3.26093 | -54.19691 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1406787d-f9c6-31bb-a5fc-2a54fa6f7d41 | -3.25978 | -54.18259 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11f92e2a-a538-3bf3-aaaf-032a4c5e3f58 | -3.25816 | -54.19294 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b34dd310-6ff7-3c95-8ab1-f187a5d21155 | -3.25761 | -54.19639 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 657f608c-e330-39df-802f-b75e3b14ebdb | -3.25647 | -54.18206 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3da65752-1aa8-3f98-a920-5b2fa056cb83 | -3.25593 | -54.18551 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aa9767c-924b-3e24-8c05-9ec2801a071e | -3.25539 | -54.18896 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab357af6-c8f0-3039-95b0-e8e5cbe1c976 | -3.25485 | -54.19241 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0be9a6b2-2303-39e5-96f6-aa6ff5622dbe | -3.2543 | -54.19587 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16da122c-324c-3e12-9aa7-64a8f9548cde | -3.25316 | -54.18154 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b3adcc6-2885-3abc-ab55-5b24eee43e6d | -3.25262 | -54.18499 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14a28413-5c01-399e-8bf8-c1e294b97da2 | -3.25208 | -54.18844 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cad0f6c2-450c-3f08-970a-0e2848c657c3 | -3.25153 | -54.1919 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 34b2a29c-a266-3f3a-9235-9a5205edf3c7 | -3.24589 | -54.14149 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 595f0941-1081-3f19-baed-8b2bf6b1e8cf | -2.18729 | -54.48681 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65b479ce-bf45-32bb-8dc6-d7580d0473d7 | -2.1845 | -54.48275 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1853f9bd-0575-35a1-9ef0-ef619b59c613 | -2.18394 | -54.48629 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a9bc8b5-c297-345d-8d12-4ebbd27b623b | -2.18116 | -54.48223 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f6c675a-a3c3-36e6-84da-c5ac1991d22f | -2.1806 | -54.48576 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 024ab0da-f103-3e8a-b201-28562b422bc5 | -2.17837 | -54.47817 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad5e3c5b-c7c7-3adc-b36e-25b10c5f2e54 | -2.17725 | -54.48524 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README60.md)
