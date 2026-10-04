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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e75bc10-b94e-3a6a-8d53-cbe9acd1a20f | 2.36044 | -50.76061 | 2026-10-04 04:55:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20fcc972-64de-3f4c-a971-09c12f32a3ae | -3.47445 | -50.0934 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 173cd260-1248-3402-aa1d-aabfc7c22d75 | -3.18135 | -50.53278 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 742e3363-c933-3b24-a17e-f28fc4aba45a | -2.80223 | -54.09352 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 603b6677-2699-3312-821b-af8d0487a527 | -4.46104 | -50.9729 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 623578ce-8da4-3380-a44d-f29efbda2cf4 | -3.18244 | -54.0812 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2837884a-56f3-3ac8-b64b-c70d09b68cd3 | -2.95911 | -54.09995 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af6033b0-51a6-31cd-bd78-41ee7ce528a5 | -2.87175 | -54.11641 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e0422c9-59bb-3263-9a86-b9714d896dd8 | -4.98232 | -46.03769 | 2026-10-04 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 462097ba-43f3-31b4-887f-d64324bedeec | -3.11122 | -53.73142 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 4e552ac5-8beb-3e97-8d0a-43de764e8f70 | -2.88999 | -54.14772 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 936e3b78-1dc6-37de-9fbf-a622a4fa3909 | -3.583 | -55.55375 | 2026-10-04 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6f72a01-a9b4-315f-876e-14523129cf04 | -4.46492 | -50.96996 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52ac48c2-308e-31d1-a9a5-b571431de14c | -3.12186 | -53.75993 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c64b521f-acdd-30fa-be05-b13743d5959b | -1.61972 | -55.01343 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4daf6db8-874b-33a4-b18c-b6bf08134bbc | -3.14 | -53.73066 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 022c5f76-8098-3458-9fcc-0b9128b3e31b | -0.35778 | -52.00377 | 2026-10-04 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7afbdc89-6421-3b7f-b2d5-54cd876812eb | -3.9303 | -52.20694 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51f39862-9f5f-3c62-90bd-593ad0b447d2 | -4.46326 | -50.98037 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a13cbfff-4c23-30ec-926e-81c8cf0c4dbb | -2.97328 | -53.26499 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ffeec1d-6432-3910-8078-5b055b373429 | -3.12902 | -53.73875 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad5c6af6-fbb5-335c-9154-d09ce021542c | -3.34956 | -54.17159 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59c24e18-7348-386c-b465-d2b1ac689267 | -2.9265 | -54.16299 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a600e656-3583-3e41-9992-440cd5a099e5 | -3.04513 | -54.21752 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d92dbf3e-ae18-364a-9fba-ed7e50ed9946 | -2.75688 | -51.55718 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b877f578-18bf-307d-9860-5e22d21bc4a6 | -3.07894 | -49.5335 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e99212e9-1e05-3834-9439-0dc49018f816 | -2.75631 | -51.56076 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8c0b39b-7877-3a7c-955f-944c40b59948 | -2.5834 | -51.877 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aeea29a1-a9c7-3adc-a974-fc229299eb83 | -3.89094 | -49.70003 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b48b4b5-ee03-346b-bf16-37aa6d2ca5b2 | 2.51598 | -60.99421 | 2026-10-04 04:55:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd0b972d-531c-376f-95ed-67ae59b17bea | -3.1757 | -54.09847 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f121f9a2-8e55-33f0-976d-035ef09bfb57 | -2.10844 | -48.99836 | 2026-10-04 04:55:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a62d7190-cd91-31bd-90eb-2d1030ce1086 | -1.16493 | -49.27297 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2ab3e5e-989d-3b37-860f-c86cce13cec2 | 1.90737 | -55.76684 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13106032-94ac-3c0c-a9a7-70e71f946197 | -3.52612 | -54.61349 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19c6d397-dae5-344e-8544-953ce748c154 | -2.88231 | -51.03119 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 249e8165-5d93-355c-bd80-60cc7bd6fab2 | -2.80462 | -54.12689 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e31c66fc-3f91-3ea4-9de5-974401c08a7d | -2.69694 | -49.03522 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 37db9d54-fe0c-357d-a3c3-a8642437cf35 | 2.87316 | -60.54192 | 2026-10-04 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 073ddcee-b54d-314f-becc-69235c4b1a4a | -3.117 | -53.71896 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 3b1d8493-1996-3ada-a2ac-de2849acbe0d | -4.28558 | -50.26744 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 597daf9b-bbed-329b-acce-9cb04840f350 | -4.28891 | -50.26797 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7f32d3d0-6544-37a6-9e97-0bec7cc33c87 | -4.45832 | -47.92405 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b420284-b6b0-3390-9942-0148d79b09e0 | -3.70961 | -50.659 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f172dce8-2b99-3889-bb0c-6ceaf455544e | -3.29962 | -50.32108 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 646e1ca3-3430-3560-b6b9-7f8491e6bc5e | -1.62596 | -55.02153 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab862374-0d55-3ed8-ba45-0266372d8a06 | -3.28544 | -53.85052 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4902ed0a-db14-307b-99ca-374bec7976e0 | -2.81286 | -54.09994 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a5220e5c-7c55-3f1f-8ffc-8c618b7a3e6a | -3.1237 | -53.7245 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4f89e337-71ac-3039-93c3-799c15c640eb | -4.15866 | -47.53302 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe330cb-b347-37aa-a2e3-7046ade13106 | -2.89146 | -54.11485 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8053b893-2b4f-357c-9547-029b4df63273 | -1.0826 | -54.11162 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c649aaca-7b22-3e44-a5cc-2bff42263219 | 1.93266 | -55.72108 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8b5736-8011-34fa-aeba-3bfc4e274137 | -3.00352 | -53.87388 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384e2d28-b29d-3c2f-b3ac-5c72a2cfd847 | -3.13117 | -53.73815 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59767f08-2192-3d52-8ee8-3944a8a9a3df | -2.82044 | -54.10115 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9768aeb-b023-33cf-8ff5-7e651ebc5206 | -2.9697 | -54.10636 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84420f60-365f-3f3d-abee-9882882b78e8 | -2.8061 | -54.11769 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f17d659b-30ef-3287-a00d-62f0a85a6bb3 | -2.92694 | -50.4286 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 327bb60e-3bfb-36c9-8604-33aa44838e3f | 0.16322 | -50.07386 | 2026-10-04 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae2be78a-b781-38db-be50-57ba803ef74b | -0.36082 | -51.98448 | 2026-10-04 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b11a350-a841-3ae5-b9ba-dcd45232287c | 1.93719 | -55.7204 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe888a5b-edf8-3150-a006-e99159db2db1 | -3.56465 | -51.98447 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8476191a-ad29-347e-97ec-0db383140086 | -2.80156 | -54.12167 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3099262-46d0-3a9f-a29e-62bd22daf08e | -2.22362 | -53.70845 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 29dd9d13-6d88-3d1b-b3d4-7828630de956 | -3.295 | -53.83854 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cddc05a5-ca4e-3a92-a4a3-ae91d02d3640 | -3.11792 | -53.73695 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64c895d1-fdda-39df-9a39-93eff98b9bff | -2.90669 | -54.1409 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a5a49c9e-184b-3a6d-94f9-34ff50ab7045 | 2.09488 | -50.73351 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c350833a-13a2-37b2-83ed-c3e41b56e109 | 0.44013 | -51.06524 | 2026-10-04 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d46edae-ee14-38ee-ade1-0e007f844f92 | 1.91192 | -55.76617 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aef4ceb9-39a6-30ba-8f32-87f832ae5df3 | -4.28726 | -48.56668 | 2026-10-04 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a438ba-5d6d-3159-b508-2a0a8744361e | -2.57655 | -51.87592 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58d78bba-8e63-380e-9abd-8be3efde2503 | -3.01354 | -53.887 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba8db0f-5ec2-3030-9e47-7d8a3e406f1b | -3.08173 | -49.53751 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cd8fa29-a772-3fba-8180-560c4e847ae8 | -4.28226 | -50.26692 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 8aa46009-c817-358f-8789-c3b7d98911d2 | -3.17794 | -54.085 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62ce4736-efe8-37be-8a7c-6398f3834378 | -2.1313 | -56.69185 | 2026-10-04 04:55:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 957e4075-842e-3548-bd61-2334c5e8f604 | -2.59439 | -51.85241 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b0382155-4604-3123-9e74-5e837c309039 | -2.97346 | -54.08355 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 096dc20b-b13a-3589-91d6-3cc84ccdbeb1 | -3.00306 | -53.88078 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fe62006-3684-38a4-8169-ab8576989c5a | -2.89455 | -54.14367 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54216d53-2db0-371e-b07a-bd5bda6adf1d | -0.35382 | -51.98333 | 2026-10-04 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 742062a5-3b1e-376c-8dc6-af068a27bc4e | -2.36428 | -50.60637 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f63ac922-37d0-3d35-9a5c-9c0acfbf0241 | -2.81147 | -54.13275 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 035418b4-aeda-3bc7-a4c2-883a21d0c641 | -4.29169 | -50.27195 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2c4b8f6-bc0e-3539-bd7b-8eab3d7d33e7 | -4.01855 | -44.82655 | 2026-10-04 04:55:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f4f47da-7e44-3045-a712-01f76dabb9b4 | -3.65987 | -54.51249 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07b080de-13f3-3cfb-a96c-6edc4c11ad0d | -2.95208 | -54.12478 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90933048-fcbb-3677-9a61-2240babd04a9 | -2.22433 | -53.70403 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 58cf6ed1-4bc0-3991-bc75-d7918878b278 | -2.9995 | -54.23398 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d32627e8-dd3f-375c-bffe-77f05df84733 | -1.40339 | -49.2638 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ca2294-ed89-32e4-9055-c60fb59ba8da | -2.89984 | -54.13507 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 304aeecd-aab5-3802-8626-dbec53490f80 | -2.82814 | -54.12598 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34745d12-aca0-3619-9c51-fe833f70034f | -1.09036 | -54.11294 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bcabc882-95c3-3fc9-8d87-502135bb66a7 | -3.00838 | -50.46969 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 58fd6c8e-ab97-31c3-846f-56deb4899ce3 | -2.75126 | -51.54891 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cfb3a79-cf9c-30e7-a322-7f95a2d68b3b | -2.3615 | -50.60236 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62e50347-c7b3-3c00-aeb6-6bf87b920b2e | -3.18996 | -54.08251 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8ae6dbf-35d9-3b7c-863d-eb492a2428fe | -1.69557 | -55.11054 | 2026-10-04 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)
