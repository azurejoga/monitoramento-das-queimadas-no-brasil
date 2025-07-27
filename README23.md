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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f503e4c5-83bf-3ea3-bfaa-7c023db23981 | -6.63297 | -58.85593 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f43a8c49-e24c-31d1-ad30-cf0133fdbb1f | -6.6358 | -58.83762 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fa48c3a-b2d6-350e-811a-21dfcc78b8c5 | -8.60765 | -64.03361 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26cb6dd0-153c-38a3-a9db-e2013b8efffc | -2.90537 | -48.24866 | 2025-07-27 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5deefafc-5fef-37d8-9615-75e7d4ba6759 | -6.66762 | -58.835 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56275b9e-9364-3afc-a820-394c79a13284 | -6.54857 | -56.19444 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d06bc0-a6ce-3125-8b25-59833c2be2db | -7.49164 | -63.8237 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e03170c-3641-3fc5-8b48-97e3c4b7a7fc | -6.67103 | -58.83552 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e90f7de-9cc8-38f6-914a-460ef8adc87c | -6.62954 | -58.83289 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3dd4434-7f80-3507-bf5b-d0c88871b20a | -6.64887 | -58.84336 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85531e11-2830-3407-b840-b0057477cf33 | -3.06542 | -49.4969 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 800718fd-3525-34fc-bbe6-d4dbf7996159 | -10.03671 | -59.1046 | 2025-07-27 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca113d92-068f-396d-8086-16016733483d | -9.43338 | -51.7486 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 008569f0-1142-388f-83d5-dd6bb176b6a3 | -6.63012 | -58.85176 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ff7b2e6-4a1d-3630-955d-c11bbd57c042 | -6.62613 | -58.83237 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4046fd55-ee29-3479-9c6c-16f98f2cea23 | -6.62844 | -58.86271 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4ed63ea9-ed4e-361d-a800-817f2dbb89ba | -6.66421 | -58.83447 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b258916-c206-37b8-b2e9-da02b9c7a0a5 | -6.63751 | -58.84915 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d2778345-2a87-318f-8289-24369db23fd6 | -6.66875 | -58.8502 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dff1717a-1d54-39ed-8df1-6e42194bae61 | -6.63352 | -58.82972 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| facc4300-4066-3097-926b-3b592c3212eb | -7.28909 | -60.18188 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12cfd0a1-157f-3dec-82cd-25de57f4d1dc | -6.63241 | -58.85958 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3e39ef04-b4b1-3d12-8c48-589f3a19de14 | -9.02564 | -59.76687 | 2025-07-27 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c4c2b151-21a2-33bd-b689-a74214711c85 | -6.65398 | -58.85541 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e0d8b270-0cde-3bfc-8359-09616d429ebe | -7.56651 | -61.40639 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b91be0a7-b86d-3bc7-b73f-ae350628de37 | -3.07002 | -49.50578 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b64ca83d-0ec9-3245-99fb-b2192afb8b88 | -6.54513 | -56.18631 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23375709-4564-3459-8236-bd74b2eec20a | -3.1236 | -48.96303 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be9255be-a021-389d-9bf6-25fd5862fb8d | -6.55175 | -56.19978 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7904dc43-a7f7-3ecf-a96b-ad18512e8ae1 | -6.64717 | -58.85436 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 294f0f4d-5ef2-3a5a-b24d-ae672d63aae4 | -11.30504 | -55.13877 | 2025-07-27 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d54f3f82-4e81-31a6-a479-75931bc23fa2 | -6.62728 | -58.84758 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50a0fd63-13b8-3786-ba9a-fcaeb50b48e2 | -6.66818 | -58.85386 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdc01265-748c-3e1d-999c-ac1c494bb233 | -6.6733 | -58.84339 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 102796f8-0dd3-339e-90af-414dc4971ddf | -6.63921 | -58.83813 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ff843b0-f261-32fc-beba-50ad07e37ff7 | -6.62672 | -58.85124 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f41afa56-0604-3d6a-ba0a-caed46737d00 | -6.891 | -52.87038 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1b0a167-a46f-3d4e-8434-1449de3966f2 | -6.67273 | -58.84705 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e7fd99-9a27-318b-b414-839ed3805a5a | -6.65909 | -58.84496 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e8a06cd-a60f-396f-837a-c6964c89ce60 | -6.5514 | -56.19712 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56ddb3c4-f989-39ec-8066-cf31307b9751 | -10.04307 | -59.1095 | 2025-07-27 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d6198ef-c9c4-3624-a015-1888c90327ee | -9.43696 | -51.75336 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a5ea1f9-0daa-32e2-be62-38971db915a0 | -6.64944 | -58.83969 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36ddb4a1-c61a-37cc-9ee0-782049b5f47e | -6.65796 | -58.82973 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aff1762c-8748-3e9f-90d5-77a5a159d3bd | -6.6466 | -58.83548 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f68f4a75-4acd-38fd-a3ae-cd1f8c1586f0 | -6.63523 | -58.8413 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a76a49c-4fde-39a1-aa85-290f044f22a6 | -6.66819 | -58.83132 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1ea3de-be53-330d-8f6f-89b0a281abd0 | -6.54125 | -56.18578 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82074805-338f-3cf9-8484-407068eda7a4 | -10.88033 | -56.09737 | 2025-07-27 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 288c83c9-22c8-318b-a2e2-9c1a6ff5bd48 | -6.6483 | -58.84704 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33518a00-acec-3dbf-ad67-5d953afb5548 | -3.11827 | -48.95783 | 2025-07-27 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ad9c605-c750-3a99-bff2-1dfa5700200b | -7.75861 | -51.12413 | 2025-07-27 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aac4a90-021e-3bab-933d-2a4d8c6d3571 | -6.63069 | -58.84812 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c8c2001-2b51-3fc4-b782-3135bee11818 | -6.68637 | -58.84915 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3033772-a5c6-3451-b2e7-8656b1edff0b | -6.64489 | -58.82393 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aee74d1-aff0-3ca1-ba88-0e4c6d41e0ca | -6.62956 | -58.85541 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f0437c38-2c58-3593-af18-8592a40e9fc2 | -6.62615 | -58.85489 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ef53896-0c1a-36d7-9dc9-3dafea3e8b59 | -2.90607 | -48.24379 | 2025-07-27 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c3ec388-77ab-37a7-961b-22d9185c6149 | -8.97196 | -61.50986 | 2025-07-27 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae6c902f-e4da-3920-a845-c39b368a506f | -9.85634 | -65.2374 | 2025-07-27 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de4441d5-ca84-35c7-98d1-ad1cd86ba309 | -10.34858 | -57.50891 | 2025-07-27 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1f79d22-a26c-3b5f-9e67-c820ad20f906 | -6.6608 | -58.83393 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82def20e-c2a1-36df-a26d-bc8c91ea6637 | -6.66194 | -58.82658 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39dd1072-54da-327c-9c16-604d33c05cde | -6.64432 | -58.8276 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6133308c-a295-34e7-821f-7ec4ba8a32ba | -6.63638 | -58.85645 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e0243d5b-4784-3fc9-98c2-c3921d60168c | -6.65171 | -58.82499 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e48fe231-3488-39b8-97e2-709868627651 | -2.9116 | -48.24966 | 2025-07-27 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9834c2d7-7f0c-3fc4-9002-d13406221756 | -6.54998 | -56.18471 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb755f4a-8146-379d-8cd6-e3fd3ce80b29 | -8.66323 | -63.85344 | 2025-07-27 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 371db162-d0fc-31fa-b3d5-07d0860942d0 | -6.67955 | -58.8481 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45fbdb5c-4be7-3410-981c-d7a138a1643b | -6.54753 | -56.19658 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a533bc5d-319b-322b-8b0c-b236b081abdc | -7.55874 | -61.41233 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67d4759c-5c1e-381d-938f-c54663eac2a9 | -9.02901 | -59.76739 | 2025-07-27 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1cd5557e-6a8d-364d-90fe-6758b22e3935 | -10.04365 | -59.10566 | 2025-07-27 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d65d91c4-8005-3170-b544-062350339f93 | -6.61931 | -58.83131 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3957dc9-5cb1-32b4-ba9a-cdcc3655da6d | -8.07618 | -63.86215 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 548e4682-99eb-39ee-a514-ed256d57a1cd | -6.64148 | -58.84601 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 567fa7e0-be0d-3fa4-ba59-7d3b4787aa73 | -6.64603 | -58.83916 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7cc3cc3-36de-3da7-801c-5d8dba10f9a0 | -6.65114 | -58.85123 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| caf095ab-be2e-3e1c-8e35-3ee32cb7c047 | -6.65966 | -58.84129 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f7f9df3-e157-3b24-a11f-380937520606 | -6.68978 | -58.84967 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88473043-32f2-3ad4-96eb-fba75a27e4d7 | -10.0463 | -64.98667 | 2025-07-27 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fcf7633-2f89-3d30-ac5c-03d9713dee3c | -6.54827 | -56.19173 | 2025-07-27 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cbf134d-e259-33c7-8ec7-0e0e081e87ca | -6.6824 | -58.82977 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b9ffd45-f258-3935-85c6-4829534dde4c | -6.63694 | -58.85279 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 85dd5df9-f52b-3b97-ae4a-d9c3b34fbdfe | -8.61055 | -64.03836 | 2025-07-27 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f019f234-6954-3452-9528-ab3ca414694b | -10.0396 | -59.10896 | 2025-07-27 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f6396bc-80a7-384d-8aab-6a4e6a4e3e77 | -7.29241 | -60.18241 | 2025-07-27 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42631330-3f0e-3ce7-a450-a16e6a31dcce | -6.69054 | -58.84565 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 461dba8a-041a-3535-b77c-6972abaca91b | -6.625 | -58.83972 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dda478e6-9759-3da1-bb4d-5cdbea0585b6 | -5.91688 | -61.30604 | 2025-07-27 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec110126-d27e-3236-93bf-4e5a6294b040 | -10.03729 | -59.10075 | 2025-07-27 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8325be3-3bea-3fe0-9fc0-b4ab36bc4d6b | -9.43653 | -51.75657 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1025d95-bd06-3097-8ec2-06b33e9779bd | -9.43155 | -51.75233 | 2025-07-27 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 335d28a2-f2a3-32ff-93b9-1d242c0233c0 | -6.65455 | -58.85176 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fce5e7d-b36a-3f05-8cfc-8374b2e7a8f2 | -11.93954 | -63.8476 | 2025-07-27 05:25:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79184b22-a1e7-32a1-bd91-8a518a442b59 | -2.82955 | -52.36066 | 2025-07-27 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b784b179-15ba-31f6-bcaf-1250325f1260 | -2.74179 | -48.68355 | 2025-07-27 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 118662f0-8027-3325-8d51-3f067ec95993 | -6.68069 | -58.84078 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7e2f4e0-5ac3-3712-a431-672f75a7fff6 | -6.62275 | -58.85435 | 2025-07-27 05:25:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README24.md)
