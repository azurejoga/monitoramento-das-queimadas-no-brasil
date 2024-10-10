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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee9cb9e1-4bbf-33a1-b9c5-0432e85ea7d3 | -7.66031 | -42.41325 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 55bedd30-6810-33a3-b945-1b3035762a87 | -7.65798 | -42.54733 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2f9002dc-dbf1-3c7e-9373-606cf497f339 | -7.65508 | -42.54297 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 734c3cbe-3b17-369a-a717-0a222d4739ef | -7.65448 | -42.4044 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f1792db-467e-3cc8-89f9-bbfaa863a86d | -7.65217 | -42.53862 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ae75d2c-155e-3a82-a67f-64ff0e2b1ba8 | -7.65098 | -42.40385 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 03bd7019-99fc-3b07-9e80-f860b12d51b5 | -7.64748 | -42.40331 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 20e3c959-ad9d-3019-a900-14aa47ebeeb8 | -7.64661 | -42.40409 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d58b64c5-c474-334f-9b01-0155fc132f26 | -7.64397 | -42.40275 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f86de6bc-c144-390c-9a2b-3433179819e4 | -7.64311 | -42.40354 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6090e2d8-bf14-38f0-bff5-1ef7fe2b2eb5 | -7.64251 | -42.40744 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a16108f0-4183-3cf5-8d2e-e395f756670d | -7.64115 | -42.54085 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6e2a611-9082-3a6f-9dfe-3bc30eebd246 | -7.63901 | -42.4069 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 143e808d-6b9e-3388-8ed3-47fee3dd8ff0 | -7.63766 | -42.54031 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e988a3b3-5602-3f8b-b158-e58c10b00c87 | -7.63551 | -42.40635 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9871a0e5-0de1-3ee8-ad22-8e3f67ba9a15 | -7.63201 | -42.40581 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 532980d2-cd12-36e4-ac43-5f966a6c9039 | -7.62851 | -42.40526 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 97093db5-8c77-30a3-ba4a-1d4a8e6ddc89 | -7.62791 | -42.40919 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b8057e8e-8204-3c14-ad22-c3c432aee174 | -7.62442 | -42.40862 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4fa7f195-c91b-3307-bd46-3689b2a43f83 | -7.62092 | -42.40804 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 93df9d88-b42d-3e87-87ea-c5dea2844483 | -7.62032 | -42.41196 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1456ea3-149f-347d-9c12-c1bf7c3e253f | -7.61743 | -42.40748 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8bf7a9ab-ab91-3e1d-adde-3d662da8607d | -7.61683 | -42.41139 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d861a54b-9fea-3b54-833d-b710d5913394 | -7.61623 | -42.4153 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f561d375-eefa-3ef0-bf68-6e648b5cf2f0 | -7.61563 | -42.4192 | 2024-10-10 04:19:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c16b1357-0c61-32e8-84cc-3640aa3348ba | -7.51285 | -42.76733 | 2024-10-10 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63873d0d-ff7d-3351-b2c9-07d2246b2ab0 | -7.29084 | -42.23671 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b4676b05-b195-3375-9bb4-1fc4c54f767a | -7.73345 | -43.8049 | 2024-10-10 04:19:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a9fc7bb-d475-320f-a5c9-1e94bccf1e1a | -7.73009 | -43.80438 | 2024-10-10 04:19:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6566558-b79b-36b4-bfd8-76091a8b56cc | -7.72618 | -43.80743 | 2024-10-10 04:19:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6f9419dc-ffa8-3c8c-9748-20cae66703ae | -7.67559 | -43.71202 | 2024-10-10 04:19:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9cb345b-3058-3202-bfb2-1b5824e5d957 | -8.15265 | -42.96233 | 2024-10-10 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 74fcd8df-f40b-3425-af5b-3fe8bee6cf49 | -8.15207 | -42.96609 | 2024-10-10 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 6301447b-1fb2-37a1-a9bb-7a50eb1fa765 | -8.14978 | -42.95803 | 2024-10-10 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 1e4dca58-5608-35e9-a900-711426d7e739 | -8.1492 | -42.96179 | 2024-10-10 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 88b7b1a4-2841-3cb9-830a-9bbc0d821a9c | -8.14863 | -42.96556 | 2024-10-10 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 7667ce88-f1f4-33f2-b03a-e63e2c3bbeb6 | -8.14576 | -42.96126 | 2024-10-10 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| b3608c87-de50-3b47-a1ed-41c5950b957d | -8.14519 | -42.96502 | 2024-10-10 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c43d533c-acaa-3364-84b3-f388a83c61d7 | -8.13634 | -43.79747 | 2024-10-10 04:19:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc6f774a-8eea-3135-a18d-addac21b2e4e | -8.06634 | -43.83799 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c6051b2-9d3c-3498-8ae2-231a3d07a2e7 | -8.06578 | -43.84156 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4aba141c-f63f-317c-bfef-9398a7b7f7da | -8.06242 | -43.84105 | 2024-10-10 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 37a37d71-6627-3d0f-9e5c-8483ff6661e6 | -9.30408 | -43.3485 | 2024-10-10 04:19:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 053079d7-0c9c-3cad-a135-9e4a95028f7b | -10.82919 | -43.79332 | 2024-10-10 04:19:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29f93047-a263-37c0-b2ad-fd94112544d5 | -9.75685 | -43.168 | 2024-10-10 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0cea72a5-37ab-33b3-9dd0-5e2275732464 | -12.29495 | -43.73774 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a383d2f9-e204-347f-810c-d6fd3b58fb62 | -12.29207 | -43.73339 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e77e4785-e7d1-30b8-8a6b-d33ee88a3b9e | -12.29149 | -43.73723 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2d1a9e8e-d91f-3f67-94df-d10635aea10d | -12.29091 | -43.74104 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 336f1b36-1f9e-399f-9a0c-b226ffdc67de | -12.28861 | -43.73282 | 2024-10-10 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 826b079e-0ccd-35be-87ec-ebca3e8b34f3 | -12.28802 | -43.73671 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 79858328-a31b-3d38-ab5e-2a22029c42e6 | -12.28744 | -43.74055 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ca1b9c66-1f3e-3047-9e85-b5ab77635f33 | -12.28458 | -43.73608 | 2024-10-10 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6867e516-4ae3-3342-a07d-c64d561b5143 | -12.28399 | -43.73998 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5b784170-fc0b-318e-a243-248e97b9cd13 | -12.2834 | -43.74385 | 2024-10-10 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 35cfc050-f303-32e9-b2c8-da290ce1869a | -12.27995 | -43.7433 | 2024-10-10 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ea96872c-fa7c-381f-9e0e-e2a8f5be2b5f | -12.27936 | -43.74721 | 2024-10-10 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03a1756b-965d-32c4-a6d8-8615fb4e85f5 | -12.22941 | -44.00814 | 2024-10-10 04:19:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1533d77-0239-3122-a36b-bd9607b5b596 | -12.22599 | -44.00759 | 2024-10-10 04:19:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc6013d9-d096-3397-83d6-4a47081a8340 | -12.13787 | -43.70937 | 2024-10-10 04:19:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ebb910d-6031-33c6-88f6-8c2835bc2445 | -11.89575 | -43.8842 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59e6cbb1-0edf-3612-9b77-3ce202c88dca | -11.89518 | -43.88797 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f1641e7-3cc5-32db-a744-de3d1ba4ed8d | -11.89231 | -43.88366 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb303db0-a197-3e18-a255-edbe49ad2b9c | -11.89175 | -43.88744 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6654d3f5-9ab3-34df-971a-08dbdb2f1db6 | -11.87561 | -43.83071 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aa45d59-5f5b-3d5a-ab4f-c7ce0d3446ae | -11.84249 | -43.8258 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7994691-4842-3934-883e-ceea0db74111 | -11.84192 | -43.82959 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b798d6f-dd68-3120-9f42-8cf4b1c010a7 | -11.84134 | -43.83338 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| add446ca-48d1-3bfc-a1ed-767f60779f23 | -11.83905 | -43.82527 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c63116f0-11dc-3e82-9c65-90b88e606068 | -11.52976 | -44.02448 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c17a0979-c60b-3232-b868-0bd45102a279 | -11.5292 | -44.02819 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b08a7b87-751c-382f-85db-26a98bc12e20 | -11.52742 | -43.99365 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aea674ac-cf5e-3c1b-9b6e-ca34942b092c | -11.52635 | -44.02394 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 49abe137-310d-3ee6-b100-85dad13abe75 | -11.52579 | -44.02766 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 338297c7-be0d-34e1-9f9b-9d0ee92618cc | -11.52344 | -43.99683 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cabac5c6-ec89-3383-a4ff-c97124f46de1 | -11.52003 | -43.9963 | 2024-10-10 04:19:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93b511b3-4cb9-30ef-b26a-856c34b3eae1 | -12.36246 | -44.73458 | 2024-10-10 04:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58a4ea0d-371e-3753-b000-66c634e71a4e | -12.29037 | -44.5967 | 2024-10-10 04:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2fc22d9-f25c-3ecf-920c-e97cf9178b37 | -12.26608 | -44.58955 | 2024-10-10 04:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 923c24a0-9d51-327c-8856-b915276356d1 | -12.26551 | -44.5932 | 2024-10-10 04:19:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5de81bf-c643-3a7b-a104-504e78c2b1bd | -13.6653 | -43.67088 | 2024-10-10 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df1e5361-a46c-37da-8071-78d5646d2461 | -13.57497 | -43.67479 | 2024-10-10 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2881996-0ec9-3e1f-9164-a1f63a4cf708 | -13.42401 | -43.55035 | 2024-10-10 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 042985b8-ed16-3e00-92b6-fb2febbd30e3 | -14.08708 | -44.13415 | 2024-10-10 04:19:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9e702d2-606a-31bc-a555-36b8bf99466a | -14.08651 | -44.13803 | 2024-10-10 04:19:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 81b9d674-dd3d-3174-8169-574ecd6ffdea | -14.08464 | -44.09095 | 2024-10-10 04:19:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94576480-ba6f-39af-8636-4f807650b8fe | -14.08405 | -44.09484 | 2024-10-10 04:19:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7efa11c9-0382-3f51-b80d-c9aa74df3f92 | -14.03776 | -44.02377 | 2024-10-10 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b82fb98c-31bb-3322-b546-f815672c062a | -14.03428 | -44.02322 | 2024-10-10 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f954964f-56e0-3563-8321-c23c0ff7f330 | -13.96747 | -44.51981 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f255cdb-86e2-3f0b-873a-d2523c89db19 | -13.9624 | -44.55361 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed761116-9ada-3a43-8848-478f937a8a7a | -13.95955 | -44.54932 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 762a4b31-32e4-37f2-b39b-df6f9cdce77e | -13.88307 | -44.48036 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34026577-6e5f-334d-abba-d8263cb7a7cc | -13.85863 | -44.52664 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d6b1411-61c9-3380-adf7-08d9b88417ef | -13.85806 | -44.5304 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fcfd73f-9168-39ff-b738-f00f3db0a333 | -13.85578 | -44.52233 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e07872c-de9f-3942-a09e-18acc98873d8 | -13.85525 | -44.54912 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4faf4f5f-2cac-3f54-8513-949722d5d4c0 | -13.85522 | -44.5261 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ee99424-2ceb-3ee5-a1e6-97f3d1091175 | -13.85519 | -44.50296 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 482b4317-8220-37bd-8518-2447d8215b0c | -13.8518 | -44.52555 | 2024-10-10 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README72.md)
