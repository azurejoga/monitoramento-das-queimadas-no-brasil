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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e7685b6-cc6f-34fb-a7ba-f7f7397f5e98 | -4.09567 | -48.24198 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0fe2b54d-db96-3fef-ba3c-52640a19ecba | -4.08846 | -48.24442 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3f15ddb-6994-3d5d-8da9-0e54d69623c0 | -4.07416 | -48.29201 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d60bde-efde-3859-99ed-7aae792b4422 | -4.07236 | -48.23836 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b7096ae-82bb-3627-b69a-9adc3f56e123 | -4.07127 | -48.24532 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e690a91-b194-3f1c-9449-5a6fba055d61 | -4.07083 | -48.29149 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84d0d51d-834d-3a2f-a5f3-c643392f9d4e | -4.07029 | -48.29496 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81493d49-6971-3e93-8291-e6d363c68c0e | -4.0686 | -48.28402 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 705571b3-99cf-36df-a0a0-c7d95de88a57 | -4.06805 | -48.2875 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad64b5a2-8337-3372-89bd-e616679f33f5 | -4.06794 | -48.2448 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97ec29ff-560d-33c7-9238-b20746def28a | -4.06751 | -48.29096 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00f46ca7-0450-3d36-a8b2-9bacf539d0dd | -4.05426 | -48.11434 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f40126c-e686-3015-a18e-8171679d4452 | -4.05038 | -48.11733 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61397fdd-8626-3b2f-b41c-b683ab5a4537 | -4.01909 | -48.87465 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf3629ba-7250-3024-b66c-413d0abbf15a | -3.98903 | -49.0221 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c404632-29d5-3932-b476-4716a0540bb6 | -3.98849 | -49.02555 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 746cfb77-8604-33c9-a541-af75453db00f | -3.98571 | -49.02158 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21e45bfc-d400-3279-a895-c62ccc5a34a5 | -3.93472 | -48.35905 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83e863a7-57f0-3125-b1b1-e161b72619fc | -3.93133 | -48.33725 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e2c3dda-2c9c-32a9-95ed-a3690cb4e36b | -3.928 | -48.33673 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51c93265-93bd-3f92-b69c-2ac181cd0b71 | -3.92746 | -48.3402 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 89618e39-090d-3c91-a276-9dba3fd0a029 | -3.92522 | -48.33274 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93b41b14-56cb-31d5-a768-22930e0e3127 | -3.92468 | -48.33621 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b82b72c-5f02-38d8-b485-0584ac33d1f4 | -3.92413 | -48.33967 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0df25e97-78cf-3ac0-a35a-cb90dfdf37b5 | -3.9219 | -48.33222 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8c30dda-a3b7-3eea-ba97-74d511bf10fd | -3.92081 | -48.33916 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bded135a-b57e-3126-9f55-719d4a0c2bea | -3.91925 | -48.37082 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0c5fb6f-869d-3ec8-bcae-05bda26bd5cc | -3.91592 | -48.37031 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2eeaa47f-2008-31bf-809a-5d703bfe1e39 | -3.91314 | -48.36633 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13205a87-00c8-3299-a173-2ef01d60458f | -3.9126 | -48.36979 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fd1c703-2eb2-3baa-b6f2-6fa219d91a43 | -3.91036 | -48.36236 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e99f6aa5-9409-3bd7-a864-e1b0b74023be | -3.90981 | -48.36582 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c577df8-3d07-3cae-81fc-9cc74b872d15 | -3.90927 | -48.36928 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e36cd2b-b9c3-300b-8a88-2ae8d12ebc3a | -3.9086 | -48.33015 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1405cbf-fe67-37a2-9648-746a01b664a8 | -3.90703 | -48.36184 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63f73024-45e1-33db-91bc-a7f9428d6629 | -3.90649 | -48.3653 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32ca26d0-7eaf-3a26-a82e-2643cf15747a | -3.90527 | -48.32963 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f10b533-863a-3e34-ad1c-60bcf6325221 | -3.8993 | -48.36773 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eddb6de-fe1a-3f99-816c-347ae755bc12 | -3.89584 | -48.32461 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3083e5dc-f92a-35e1-9aa5-fcadf5d5a6b4 | -3.89251 | -48.32409 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38528a2a-71e0-34ae-b096-e71da9b874b4 | -3.88864 | -48.32705 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9886e728-2f99-36fc-8488-371a9498e193 | -3.88478 | -48.32999 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a867f38e-157a-3b0f-a848-81a0ec71cbe6 | -3.87108 | -48.37398 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ec28fac-0c46-3d0c-b890-b90f60344367 | -3.86884 | -48.36653 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9a9d16d-d10d-3814-ae3a-ff37a6a6de1f | -4.19727 | -48.04334 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1352789a-cf7f-3ca8-b039-472e25d021e7 | -4.19436 | -47.77652 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cdd0ebf-abdd-3027-a42d-b6d254e96bc9 | -4.191 | -47.77598 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d806cd2-9853-3153-b78a-084841113ca5 | -4.19045 | -47.77952 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0191c94-4f56-3f15-b597-60bb916b0ee5 | -4.1882 | -47.77188 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efd13499-aa00-376c-aa36-4e32a8ca36f4 | -4.18765 | -47.77543 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ef9d544-923c-37ef-8aff-3ec9563b4d3b | -4.09621 | -48.2385 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 108313f0-0edd-3e39-ac1e-ad9b2a3155fd | -4.07624 | -48.2354 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22b31a6b-1b6f-32a9-ab83-c3fcbbe06ba9 | -4.07291 | -48.23487 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9708be4-1b8e-38d0-a7fd-7709b9990d51 | -4.07182 | -48.24184 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcf19652-caf3-3d39-a0c7-6ff041ce11b1 | -4.05093 | -48.11383 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 972210a9-ec09-3a57-bf31-fee0206f64d3 | -4.04759 | -48.11332 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8105dc3f-ec95-3a87-85fb-c6190c6bd911 | -4.04535 | -48.10581 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b1a168c4-4aff-3150-b3f2-50abc4ebe92d | -4.04154 | -47.95482 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13e94cf9-3b37-3875-9cb5-b3a6788d5ff7 | -4.0382 | -47.95431 | 2024-10-25 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33cdc776-d6b4-31e5-8c6e-5df0c3f028d5 | -3.7623 | -47.72794 | 2024-10-25 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7dca49f-163a-34ce-adb4-a9f97f800085 | -3.83444 | -48.8884 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dbea886-9f6a-3777-a521-b5419f747f51 | -3.8339 | -48.89185 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e35e951-be3b-3ac7-aeb3-0dac0c972199 | -3.82998 | -48.87357 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a0513a3-6eb3-3188-96b9-c133b93381c2 | -3.82944 | -48.87701 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebfe72b8-1139-3d32-a62f-cae101cb0378 | -3.82889 | -48.88046 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e05d21e-e6ec-3b89-a807-d55e1469a9fb | -3.82781 | -48.88737 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c4cdf5e-9024-3b06-8a2f-1d262272eeea | -3.82612 | -48.8765 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78a0b5c6-1e65-3950-9207-7f7fc9e6a15e | -3.82557 | -48.87994 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5182534-23bc-30b2-8de8-dff23690bc97 | -3.82449 | -48.88685 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 053f6d79-0488-3814-8b6c-c368a4658476 | -3.82002 | -48.87201 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7e1abcd-cec5-3f76-aac5-66e42f4a0ce6 | -3.81948 | -48.87546 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9d860a5-8b4c-32ca-b164-ead58c0a4a43 | -3.81616 | -48.87494 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a62f309-f851-39bf-b714-bacd371a8122 | -3.69124 | -49.04666 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e0d5b24-33bc-30ad-8222-07c917d33834 | -4.38456 | -48.61722 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d9aa681-b129-3ce0-8658-f268a13e1e2b | -4.3708 | -48.63982 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ffd39fd-1cfe-3801-ae8e-74cd48f80df4 | -4.36748 | -48.6393 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b799fa63-5eb7-3e94-ab94-c5c98c4780f6 | -4.36694 | -48.64276 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dbaeb258-d55a-3428-9da8-34dd955254b1 | -4.36572 | -48.60719 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b015644f-145f-3576-b127-66e1b5ab9a13 | -4.36445 | -48.59631 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 191d73fe-38e6-3493-93d0-6e0b4afff222 | -4.36336 | -48.60323 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 115edaf9-dc04-3be5-94e3-ae66ef73f5e3 | -4.36282 | -48.60669 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b90b1d1d-3168-358f-bac4-12b513687ad5 | -4.36058 | -48.59925 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d4b2589-1ce7-399d-919e-a6fe8035d3cd | -4.36004 | -48.60271 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6749885-8eab-3265-94f7-74ea2fd56506 | -4.34458 | -48.61448 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 176f482d-d65a-316e-a73d-00000b9c5901 | -4.34403 | -48.61794 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bd12fdf-cc70-3bf0-be2e-0a1ed6c7a65b | -4.34349 | -48.6214 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14cf61bc-2960-3292-bcfc-78289b2d1358 | -4.34296 | -48.6248 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ee4f2cf-cb95-396e-8337-c61e499f93ea | -4.34242 | -48.62825 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebd60ad2-1cc9-3c55-99a8-8b9905960ef0 | -4.34126 | -48.61396 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 768dbeb4-dce5-3397-9c7c-4fe66877b7a0 | -4.34071 | -48.61742 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b845a42-91e5-3b79-9f14-c586177ba329 | -4.34017 | -48.62088 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33080cfd-09f2-32a3-bdcf-93a9237f68cc | -4.33964 | -48.62428 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7780c6f0-2460-335f-9608-e80a52433a1d | -4.33801 | -48.63465 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 89a78b4b-33d8-34bd-a342-88b214d7b5a3 | -4.33747 | -48.63811 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| eaecf3c3-3468-36aa-9c86-0c30ed106ea9 | -4.33632 | -48.62376 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e27cc23-c12c-3dec-9062-e4b1cd6154b9 | -4.33523 | -48.63068 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| df15cb75-cf65-3791-b184-891b12c435f0 | -4.33469 | -48.63414 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 661f9243-5fea-3f4e-b394-fcc7cb6a3a1a | -4.33414 | -48.63759 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b17a2d67-9938-3a75-b8de-9b7305464670 | -4.3336 | -48.64105 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9d6e8f6d-667d-3bfc-8d23-b7b831e265b9 | -4.33191 | -48.63016 | 2024-10-25 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README58.md)
