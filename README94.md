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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a7828ae-f387-3811-ba2f-5591bf6f7c3f | -2.73187 | -51.73227 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bb7d640-60a6-3e56-99c6-e4bf970054cf | -2.73175 | -51.73121 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c9761d2-62dd-36ae-8f89-c0e3286396e8 | -2.72461 | -51.70434 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5905da21-4dd6-3466-89c3-1524ec2353e0 | -2.72406 | -51.70795 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d4ba9ff-370b-3544-b7ed-13f8f8297d17 | -2.4207 | -50.50664 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 643a6b3b-3703-34a0-b106-bb02ecab8c1e | -2.41604 | -50.49717 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d58db59-2a46-37a1-9005-40f0f0665683 | -2.41541 | -50.50148 | 2024-11-02 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e757da05-b5aa-3c3f-a4df-f33862e9a450 | -4.12802 | -51.07517 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36006142-9722-321f-a288-b5020304d403 | -4.12738 | -51.07946 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70ddc3b4-4538-3c30-8496-11c82c8e0bf8 | -4.12737 | -51.07298 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b694901-36c0-35c0-9f74-473df3bb63d0 | -4.12676 | -51.07729 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09c99c53-839a-3e2a-848c-b8e5e1b959f1 | -4.12615 | -51.08153 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2b53dd9-26f9-31c3-a954-7911456b7a63 | -4.12206 | -51.07504 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fe35ff2-4bb9-3acb-92d3-b8c124686a1c | -4.12143 | -51.07272 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34be52eb-a033-31b1-bb08-1d2ba36b9c28 | -4.12081 | -51.07706 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91abcdf2-0eb6-3d56-b352-404c93fe5193 | -3.61559 | -52.20637 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c68f3c08-80a5-304f-bcb9-4f56ee733ab9 | -3.61507 | -52.20982 | 2024-11-02 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0e5f11e-9d1c-3ddf-9bc2-b1adb3bf356b | -3.89276 | -50.98437 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cb79bbdc-3fe7-3d42-9881-c8ba587813c1 | -3.89217 | -50.98836 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| db0eee6b-5c68-3212-80a7-785393e44226 | -3.89158 | -50.99231 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3117b3e3-944d-3c89-b317-b1f886169100 | -3.88629 | -50.98757 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cbf116f5-5f11-30b2-ac1f-58b5d2b3a17c | -3.88545 | -51.03374 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e5d0283-bf64-32e6-be86-80c4cca0dbb6 | -3.83941 | -50.98011 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8ce2a57-376f-3c01-8736-686b05d71118 | -3.69337 | -51.17558 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fa79b55-12cc-398a-a650-80a40bc68c26 | -3.68761 | -51.17457 | 2024-11-02 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d699d3e-8791-3c5d-a079-4cfa4d8e83ef | -1.92886 | -52.67194 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b21679bc-6990-38d1-8b38-0a39f3119a02 | -1.92842 | -52.67482 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8260ce3d-9eab-3930-b83c-f7d0fee09202 | -1.92797 | -52.67772 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05d2b779-88f9-3544-88da-ec8787169966 | -1.88966 | -52.13087 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91c1c06e-a5f7-3e3c-b086-5fa399828a81 | -1.88916 | -52.13412 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df1e8902-4225-3d7b-9c4a-dfbf2b0ce894 | -1.88439 | -52.13002 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74860ef4-e40b-30c1-bb95-ebee3ff0ca86 | -1.88389 | -52.13327 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e38cb7a-b50d-3e9f-954f-a17560421f3e | -1.86467 | -52.32816 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f341376f-f4a2-3804-8603-547b6bd2d6ae | -1.86418 | -52.33135 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b601abb-7972-3835-b67b-69f809c78e5d | -1.60133 | -52.37147 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55a5d526-5584-3ac2-bd50-e83441936bd9 | -1.60086 | -52.37454 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fe5f9cd-5b7f-39a2-bc41-5db63371918a | -1.59546 | -53.14655 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33b9cf31-f70f-3314-966e-807f5b698083 | -1.59223 | -52.14879 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e12ed252-8a50-375a-8f27-53d270ddf981 | -1.59049 | -53.14619 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28f5df91-7ff4-3c85-8219-d3959ee40495 | -1.58974 | -52.16473 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1d93f00-9bbc-3772-9789-60bf3e63d9a4 | -1.58924 | -52.1679 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9515b2d5-a430-3631-ab40-5d7bbf14ec9b | -1.58875 | -52.17108 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f44a5648-ba7d-34a1-9e52-4d3b113c2e2f | -1.58698 | -52.14803 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bfc054e-3ffa-31a1-bd9a-d19be3420541 | -1.58449 | -52.16393 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 491f42f3-da80-3235-8e42-bc7f2a2ca5a6 | -1.584 | -52.1671 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb34ec0e-bda1-3c3a-9ace-e27a50c1b150 | -1.58074 | -52.15359 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61bdf338-c420-3163-a6c0-ab8385af635b | -1.58024 | -52.15677 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57e9eb2e-897e-3dd2-b8eb-eaf1a6c52c08 | -1.57975 | -52.15995 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40a19258-f089-32b8-8ae6-675b51856424 | -1.57925 | -52.16313 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e079314-3857-3cbc-bb87-1624993ee845 | -1.57846 | -52.13364 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72004260-f0de-3a98-adb7-965e5b53f1af | -1.57697 | -52.14323 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e15b6f7e-2b83-35ae-b646-3c6cfcb2ddc8 | -1.57648 | -52.14642 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d53fb0bd-ca7f-32b6-9411-1f241eac4a62 | -1.57549 | -52.15276 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c9d6b80-5010-3277-bcd9-2baf5a679d83 | -1.575 | -52.15594 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581eb42c-48c9-38a4-954e-4fde82abd868 | -1.57321 | -52.13282 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0e2803e-bf86-31fa-9d7d-f08f6f6c121f | -1.56239 | -52.20269 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 992e7359-9b8b-321f-a509-19af9d7dc5d7 | -1.56211 | -52.27327 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0122c05d-7a94-3bef-bc80-165967223e16 | -1.56113 | -52.2795 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f81f92c-eafa-3c31-a06c-5c32fd0ba617 | -1.55863 | -52.1924 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 792ea937-0f6c-3666-abdb-54d49f9d1f96 | -1.55814 | -52.19556 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b434a8e-bbea-3cb6-8633-a01e889ecaf6 | -1.55807 | -52.09127 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc7d8717-20f6-3d23-abe3-7ef82fc3b5b6 | -1.55765 | -52.19872 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ffb971a-155c-3d06-9335-7db0bc16f495 | -1.55758 | -52.09449 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f01a036b-2648-36a6-b81f-ebb8eccb70c6 | -1.55716 | -52.20187 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f19acd1b-1a66-36cd-9724-8bb0d229d708 | -1.55388 | -52.18844 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47a34d4f-6478-38af-90d4-fc15c431fe72 | -1.55 | -52.07352 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73a0b0e1-dd1f-35dd-8e92-367ba532d981 | -1.54522 | -52.06946 | 2024-11-02 05:27:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83cc5c4f-818f-3390-9af4-ff3068551408 | -1.5149 | -53.13777 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 107eea81-d074-3765-8b69-b91ff1031c7a | -1.51406 | -53.14321 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dee70ea-f710-37b0-9287-bcf2d66b3b75 | -1.51002 | -53.13691 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 886f0745-f228-32fd-b5ea-b7fd084d61c6 | -1.50917 | -53.14241 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee23de37-6274-3a8b-aaab-df66bef480b4 | -1.45612 | -52.37716 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b7deb7f-d156-3483-a632-6fbf053b0593 | -1.45508 | -52.37674 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 281c621d-7bd1-3094-a8a6-3fbae1964234 | -1.4504 | -52.3729 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97dbd957-c89e-38b3-a01a-f7c399919779 | -1.44992 | -52.37595 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98034477-c10e-38a4-b751-84dd661ec457 | -1.41685 | -52.21233 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b5a5cab-6f76-3da5-91a4-e154907ee08c | -1.41355 | -52.19897 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445f4456-4212-3651-a545-9fbb0a8bf50c | -1.41211 | -52.20838 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1311003e-c3b8-38d5-b370-ab251279432c | -1.41163 | -52.21152 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e490eb1-3821-30c8-8fe1-b0d5b37c01c8 | -1.40833 | -52.19816 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b4fcf0e-3316-3e7f-b091-26b424b43260 | -1.3465 | -52.53645 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef363edf-77ed-3872-9a87-6a088b3c8c47 | -1.32627 | -52.80514 | 2024-11-02 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75c7b675-3417-3848-87e0-9faca400767c | -2.04333 | -53.25307 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dd502b3-0a4e-385c-90f8-578382a50f23 | -2.03843 | -53.25232 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc6a4fc0-2557-35b3-b129-c185ed2a39d5 | -2.01713 | -53.29332 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6c51913-30a6-340e-bfde-d15e0648249e | -2.01631 | -53.29871 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bbd1fca-61fd-31f2-889a-55b6ebbbab88 | -3.27034 | -53.41072 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d41173a-812f-3c67-a79d-9e0149c65366 | -3.26952 | -53.41624 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ed111b4-9b5f-34fa-ab29-c54b4a4770f4 | -3.2687 | -53.42178 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 59dcf1da-c8e3-34a8-bc87-59daa932043b | -3.2662 | -53.40452 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d048fc4e-f46f-3f37-9f8e-5dc39a5b5988 | -3.2654 | -53.40992 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 333f5eba-de49-3fbb-bf56-2560ed3089d3 | -3.26459 | -53.4154 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b8f1f74d-72fc-31e6-9cda-19d589d2b8f3 | -3.26377 | -53.42095 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 77558629-c9a8-3f0c-aea9-7c9d443a8e04 | -3.26364 | -53.35325 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| bf95f999-4fb7-3c09-803a-924df9413a76 | -3.26126 | -53.40377 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cdc5a4b2-2fec-3a3d-9e3d-b04c78b50076 | -3.26046 | -53.40918 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7e47ba9e-45d1-3bfd-b6d4-db59e5e87d22 | -3.25966 | -53.41462 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3b5b7d2e-0b59-35fa-8441-2f2c7b6acea5 | -3.25885 | -53.42009 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 33a664fb-4ada-3946-8cbd-64702694bc58 | -3.25869 | -53.35249 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| a64cac00-5b57-3e5a-8b61-99a361f6a6da | -3.25856 | -53.35168 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |


[Clique aqui para ver as próximas entradas](README95.md)
