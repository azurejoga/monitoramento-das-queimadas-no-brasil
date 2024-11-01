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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e595fee9-c2ba-3223-99df-92845b4427fe | -3.05362 | -49.48442 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 91ae1dc3-5fad-30ee-bf96-57cb56018a50 | -3.05352 | -49.47865 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 449d3e8f-d6cb-3e8e-a4c4-b10d034c73a8 | -3.05305 | -49.48848 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2b4b7403-0376-34ad-9a0c-f09410eda20a | -3.05292 | -49.48271 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 46e99ada-eec7-3841-9f77-08a9a519bfd3 | -3.05231 | -49.48676 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e687b554-c864-3864-9ab6-9c79fec6380c | -3.05171 | -49.49082 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b2e14467-09dc-3cd8-9d7c-c942578bc679 | -3.04897 | -49.46963 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 23c1c733-84f8-32ff-bb64-8388cdeecdcd | -3.04836 | -49.47374 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ba07df11-5ffb-39bf-a90d-58a2aa328a22 | -3.04775 | -49.47786 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ae9b5888-d74f-3448-b376-b595e115eac4 | -3.04715 | -49.48191 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b2ed0fdf-c6b7-360a-bc16-8110dcbb8ef2 | -3.04655 | -49.48594 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fb59edb1-b5f7-3bc3-a0ab-5fe3cf2daefe | -3.04595 | -49.48998 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a3fb4e34-532e-3b14-bc92-fc60f0c6a51e | -3.0426 | -49.4729 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8b78e5d5-829a-3a08-be75-280bf2dfa50a | -3.04199 | -49.477 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e2690064-a2ac-3748-ac13-bfae50b92ddc | -3.04139 | -49.48104 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c3ee39b2-1218-3806-b0c0-4bb264b7f377 | -3.0408 | -49.48506 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 278b43fb-bb34-326c-8bd0-00d47760c433 | -3.0402 | -49.48906 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9f680a5d-de3d-3ba9-9392-9cf943a4ea7f | -3.03961 | -49.49308 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0e77c180-845c-31b4-bcb0-bafba509e3b8 | -3.03624 | -49.47605 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d5686c40-87c3-3bbe-98a4-4ce00d915646 | -3.03564 | -49.48013 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b4c8f805-73d1-3ee5-a906-73219f366151 | -3.03505 | -49.48415 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| be857ac8-13ba-3d54-a7c1-898f5a612bf9 | -2.81904 | -49.76861 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52431a83-769b-3953-a803-f41342f95225 | -2.81845 | -49.77253 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b20089d-ad3c-3077-9c6f-1610bc0dae88 | -2.81717 | -49.76453 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3e2c2cb2-adcd-3adc-a201-e2ad7136d5cc | -2.8166 | -49.7685 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41a89ed7-7d32-34e9-a0ee-3c3b6e9b6d48 | -2.81603 | -49.77247 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f68153d7-42bc-3ede-ba76-411650af16de | -2.81341 | -49.76775 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd3b8e3d-0d98-38d2-bfee-f5e62638d7d5 | -2.81281 | -49.77172 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43cbd68d-b588-3f6a-9a93-6612b901755d | -2.81096 | -49.76767 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9973856e-9881-33ba-894e-caf6c361f731 | -2.79324 | -49.4737 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f746cd6-67c1-3f8e-aaf4-5947bf1fc52c | -2.79266 | -49.47767 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12a0826a-6423-3928-8aa4-9d7b00bc8be5 | -2.75311 | -49.6286 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 452fe1e5-7a6e-3b8d-9854-773b9feb7e59 | -2.75254 | -49.63248 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d86840d-a1d1-39be-acfc-5a31d703d031 | -2.74688 | -49.63152 | 2024-11-01 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b36cd1d-729b-3647-8dc1-01a7cfda3365 | -2.82379 | -49.22436 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63ac1738-19a1-3380-821e-54fe2cdf2043 | -2.82317 | -49.22857 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf8a47a0-94b3-3609-ae06-9c9739e54726 | -2.80152 | -49.21568 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7457a301-d444-35a8-9896-ab483eb2692a | -2.80106 | -49.21653 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17de15c8-e799-381d-a274-324238194331 | -2.80088 | -49.21989 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bcc66f14-035d-3960-80ba-75619e15188b | -2.80045 | -49.22073 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35c0b70c-9336-382d-8f89-f061617b16b5 | -2.79522 | -49.21565 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c5cc67be-13b8-3e29-b3d8-06dfcd04e043 | -2.79505 | -49.21901 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 979fde7b-863c-36fe-8680-ca09e2341fb0 | -2.79462 | -49.21982 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a7aa0ea-4154-3004-bfac-3ab7a29d2fd1 | -2.6044 | -49.09788 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc1c99b4-da2e-33cd-a67c-b7ae5a8fa5d0 | -2.5998 | -49.09426 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2816725a-b9af-3d50-8856-9e148187c705 | -2.59918 | -49.09834 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04908136-1c45-30e6-a92a-45373fca10d4 | -2.59853 | -49.09696 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 801e9dfc-00d8-3965-bbd3-46fda5479c33 | -2.48983 | -49.07534 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4cb3ccd-f7b1-3c69-b2b6-403126e59a70 | -2.48906 | -49.07249 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e03c5d92-38db-3b9c-bdc8-85c91f245db9 | -2.48844 | -49.07677 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1cddc1e-a280-3da0-a828-987bb7cb7ec1 | -2.34262 | -49.10255 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b0f65d5-b562-35a3-a1df-51777316cc54 | 1.08475 | -50.96433 | 2024-11-01 05:23:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 781f8b5b-3efd-31de-83ee-683af6c90e06 | 0.36574 | -51.13247 | 2024-11-01 05:23:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 158908bb-6254-387f-b247-58f25c6b9a58 | 0.32636 | -50.81334 | 2024-11-01 05:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd58b68d-e2ae-329d-930a-0987ee5af7d2 | -2.24354 | -50.43917 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b18c40ae-6494-33bf-8d3a-b7c1dec9d6a3 | -2.24304 | -50.44252 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a4ce39b-7815-306b-9625-5434fd0ee268 | -2.24064 | -50.53059 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 236f6275-4540-3687-a871-cbaa123c7721 | -2.23822 | -50.43825 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8b31031-9159-3f5d-9709-4317b12fbe16 | -2.12039 | -50.83391 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bd25a59-ef7a-3cb4-b6b1-3f60d99b23fc | -2.1188 | -50.83421 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fd04be8-151d-3040-97fb-6cddd5b53325 | -2.4247 | -51.96543 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 670c745a-1ede-3d71-8b33-7f767e3ec79e | -3.18517 | -51.33324 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 226d5cf1-862d-3368-b245-dbc4c98c50d7 | -3.18472 | -51.33628 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a400c1bd-6e5d-3928-8b8a-dcee6ce8a112 | -3.13876 | -51.02775 | 2024-11-01 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ecfbd758-190f-3d6f-8944-56a24d12a015 | -3.13829 | -51.03094 | 2024-11-01 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 89770c1b-26ab-3047-82e3-1fb91e918c9b | -3.08518 | -51.28148 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9795b6-e33d-3fc4-9c86-72d40b82e146 | -3.04722 | -51.3976 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aab3c85-d79a-3bc8-a6b1-13cb0b609cb7 | -3.04682 | -51.40037 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf6650f-4639-318d-9706-ddaedb7bac64 | -3.0464 | -51.4032 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4e41713-9ced-3f79-a92d-13489b70004e | -3.02624 | -51.09695 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccf37f81-f8cf-3fac-ad64-6a87c9c1487f | -3.02431 | -51.44816 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f789300-24cb-3950-b4f6-83a1776da01e | -3.02387 | -51.45119 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b06b9a7-4c40-3720-a83f-13fac812b10c | -2.95325 | -51.05405 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c65c4754-b34d-3112-8bca-d14e6aceb11d | -2.9528 | -51.05721 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58f384be-0144-33c7-a2ba-c3c087117829 | -2.9516 | -51.05307 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cce4369a-6bdc-376a-9bbc-26cb402e3fc3 | -2.95112 | -51.0562 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07a7d918-b4a0-3174-b2c7-3318dd8f63c0 | -2.90149 | -51.4827 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10b07a96-d6b6-3ce4-abf0-d07ee429c683 | -2.90106 | -51.48563 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5353982-d2c3-3e21-8a89-b07cc6df64d6 | -2.88615 | -51.65748 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 318e7d87-85b2-353f-8ea7-e04d3fd3c6c4 | -2.88128 | -51.31001 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8ae7916-943a-3ce8-80f5-4de02f68301e | -2.8812 | -51.65662 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b7fa5b-b441-3619-bbad-50e0067ead76 | -2.88084 | -51.31298 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51805d36-812d-3d23-8940-ac8de25b5028 | -2.87621 | -51.30922 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a6b39ca-35ba-3a85-a977-81f6fbba6b87 | -2.87576 | -51.31219 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c032982-45ea-3d1f-9c0e-d65701658016 | -2.85585 | -51.76102 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cf206de-b23d-35ec-a578-ca462a35fb31 | -2.84446 | -51.80474 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f844415-47c6-3dc7-8e40-d55df7bd1ec6 | -2.84226 | -51.80289 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb654244-073f-3abb-b0c9-c80f25b96a21 | -2.84142 | -51.80838 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8092a462-23ee-3484-8732-b4526da0967a | -2.83876 | -51.80947 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2230debd-99fe-3c65-8fd9-9f2c51836661 | -2.83652 | -51.80763 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4bdb2de-8e4b-3370-8683-86db2453fa42 | -2.83466 | -51.80316 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c50ecf23-b8a1-3ac6-b18f-7b35ce8cb834 | -2.83386 | -51.80869 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 529ec5bf-a8cb-351b-b399-319c3be9a153 | -2.83162 | -51.80683 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 415a583e-c093-3a92-8407-21e7829b582f | -2.83078 | -51.81234 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c43d2e58-2ddc-305c-bb03-ea62a6441056 | -2.82896 | -51.80788 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 87955b3f-2f5e-3607-afb1-6affb99a43f9 | -2.82672 | -51.80606 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acf74efc-ce1d-3311-8200-48fed22c81ad | -2.82588 | -51.81158 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5dd00c8b-8495-3337-a02c-9f0a548f0d81 | -2.81688 | -51.60299 | 2024-11-01 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 064ddb9c-9c77-3277-9671-fd8843b67601 | -2.74556 | -51.73072 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34ce60e2-3538-36fe-ac6d-31830c859fed | -2.7447 | -51.73631 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
