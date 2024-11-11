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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 309e5c9b-c177-3145-a47b-0be05755814b | -2.10648 | -46.53407 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8705899-abcf-3147-a32d-affbbb61612c | -2.24543 | -53.67118 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ad3fb35-68f8-3f17-b9f1-707377c5f9ee | -2.99332 | -46.9416 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6417163a-873a-3343-80a3-394976b148fd | -2.06584 | -46.28511 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0eb3f0c6-2d38-38c1-8812-f073c51c519b | -2.68037 | -48.66451 | 2024-11-11 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dca2846-941f-3282-af85-208f637a1ecb | -2.30774 | -49.11934 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ece5d9a-73e5-3292-87bd-81537ae78f07 | -2.8809 | -45.36504 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee75cd58-e288-3496-842a-92217a772737 | -2.37119 | -46.79583 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a813fc40-14c5-36c2-b1e5-77da11129c66 | -2.91734 | -49.48859 | 2024-11-11 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd6f2ec3-ed67-3bb1-9dae-9148e3632e1e | -3.25053 | -46.48278 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f57f7e72-9fba-3e11-8aa6-c1c8c4ad31aa | -2.60267 | -51.72089 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc6921f2-721c-3772-9ab8-b825bce4c928 | -2.24609 | -53.73928 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 15c84ab6-ae8a-3ac2-bc23-1f36165a0976 | -2.75132 | -49.36762 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a403b67-ff80-3026-8303-5f1f652f39dc | -2.60905 | -46.1586 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 489e3ea9-71ee-3acd-8885-4cc6571c9067 | -2.13583 | -46.39405 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ca0282a-264e-39d9-8628-60e553acb1dd | -1.7574 | -53.75276 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5af082f6-3d2c-347c-8211-37ad6f052287 | -3.0253 | -50.98106 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b5764d6-cea4-3960-abc6-fcac9f946a23 | -3.53134 | -54.08527 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b7388b-91c7-39c3-9c47-e4ba569773a1 | -3.12326 | -45.97012 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30031813-f14a-3fd7-b126-8c459986cbfc | -2.17395 | -46.69906 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d07d28f6-face-30f2-a15d-34d48f2303b6 | -0.84106 | -52.53415 | 2024-11-11 04:18:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6157e279-29d9-3c46-b242-bde36fd5dead | -2.61635 | -49.24057 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 822c0466-56c1-341d-b7d4-a25fa2ff9351 | -2.78831 | -45.96576 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ed137c2-b94b-3254-b363-b3e085de5b54 | -2.19332 | -46.81189 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a19272f7-1a97-38f0-b4e3-aa9041b346b0 | -3.02474 | -48.07295 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26a9de9d-436d-3d7a-a2c0-f38b478b96ad | -0.84224 | -52.53711 | 2024-11-11 04:18:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0016c9b4-e662-38bd-b0e8-189d000bee3c | -2.36621 | -46.85062 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0809f8f-be3d-34c3-8b13-d767d1a362a3 | -2.37355 | -48.63369 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c356ec-29ba-33eb-a411-61f6323fb436 | -2.61696 | -49.23677 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df2f569a-49d5-34c5-ba70-6021974e4104 | -3.9582 | -49.00808 | 2024-11-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e45aa11-1eb9-324b-b579-11f0d5ffef33 | -3.13018 | -45.97122 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8746a819-d1d1-38b1-b1b5-fb550f1aad23 | -3.09124 | -51.07792 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7f1b8ba-6abc-3760-8edb-c54cc8c10d30 | -3.02062 | -50.98029 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d683246-af81-3734-b35d-29f3985e10c8 | -4.70601 | -46.38337 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58d3208e-dee3-30be-888e-52911307d3f0 | -2.06914 | -53.29821 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a57920ef-c05b-369b-95c7-2f848882e8ca | -3.59651 | -44.55176 | 2024-11-11 04:18:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 105dcc56-9420-3922-9323-84a5ff10882b | -2.37333 | -50.34084 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2a8d481-edb0-3353-b000-b1c11bf3e656 | -3.52309 | -53.4992 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a74a9e7-6d73-378d-a50a-828ec196c721 | -2.99761 | -46.93795 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4246eb57-438d-31a6-80cc-3b32964f1fc1 | -2.25116 | -53.74419 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 115c36de-ef2f-3691-ab3b-70ce6fbe101e | -2.56714 | -47.33918 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5dac4b7-67c2-3d4c-ad3a-453fae242060 | -4.08857 | -43.94172 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 817345db-1640-39ee-91bb-b3023920702e | -0.90694 | -51.64916 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4782c8f-3261-3e6c-a909-5817a78368f6 | -3.16203 | -49.73395 | 2024-11-11 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 703b998c-9d4f-3746-bd37-43cf3705ffcd | -4.8386 | -45.84 | 2024-11-11 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d837efc-8234-37f5-a925-8c7d536a39f2 | -5.26847 | -45.72614 | 2024-11-11 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7c9c656-0a6d-3203-8c59-d3b77e5841c2 | -2.34358 | -48.58937 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b86b83d-928b-3493-9802-24983df2046d | 0.84624 | -50.20952 | 2024-11-11 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 510cccce-1ff1-3eed-8779-820a809f67b3 | -6.28159 | -43.39574 | 2024-11-11 04:18:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 11820d0e-70cf-36e6-9c2a-32d28d1c4deb | -1.65724 | -52.64356 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9651e82a-9d56-30fd-8fd2-b11127ed3613 | -4.54314 | -43.56894 | 2024-11-11 04:18:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a11ae28-0a7b-3d24-b6c2-2ae0726f6159 | -5.81939 | -44.12413 | 2024-11-11 04:18:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3a4208f-bd1b-3907-9864-fe85798f2b27 | -3.28095 | -53.6654 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff00b57e-6dcc-3edb-8975-9b46c2688780 | -3.24214 | -46.44507 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 274d55bb-7042-360a-a073-632ddcb30692 | -4.69928 | -46.4254 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e38b5fe-0e29-39bb-847d-5efb037c266f | -1.71723 | -52.47323 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d83aecb-f47c-3ea3-9beb-66cc3efb0bf1 | -2.65373 | -46.80295 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2063c4d-a2f3-366b-beaf-4de450096174 | -2.35788 | -46.57917 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 310437fb-32c4-38bd-af96-c5250adec1b2 | -3.02397 | -50.97932 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3fd3a8c5-bd43-392d-b18e-2e48c48d8163 | -3.21399 | -46.48558 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf3e89d8-5ebc-3efc-ad13-07e3804356fb | -2.59609 | -46.17243 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4a84da4-08ee-351b-8113-8866faac2fbc | -2.24708 | -53.74242 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5292e0f6-3e93-3055-b0e4-e6ce90e3b944 | -3.02553 | -50.96965 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3203f4ec-5417-30fe-8329-eddcbf183dda | -1.8456 | -46.58372 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b2e9e189-02e3-35de-82b5-f047a19b34a1 | -4.71172 | -46.39216 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b5d96db-1dd4-34f3-b353-30488bbdae86 | -2.89236 | -46.82538 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fa72a46-990c-3396-8179-c146234d35ee | -2.79916 | -45.98697 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ddcfd5f-6f9e-3619-91e2-cacc7ea90683 | -1.11521 | -48.37522 | 2024-11-11 04:18:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf2947b2-376c-304d-a15a-cba0c2a6d214 | -4.70887 | -46.38777 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9a4d49c4-2585-3284-9926-82fd13272b6a | -5.42987 | -45.53094 | 2024-11-11 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12b28723-c4a9-38de-818e-01d488c6221a | -4.69867 | -46.42926 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cf3e06d-b0f0-3252-9419-e6a879a13937 | -2.17756 | -46.69962 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a88329a4-22dd-392a-9d7a-421b1932b03e | -4.08525 | -43.9412 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6569ff1-1b09-3b4b-a457-e0578ae490d9 | -2.46635 | -50.39805 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b9b753a-4214-31e5-9ba1-b3e60fdb05ea | -2.06853 | -53.30198 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18dfb6e1-a388-32c2-b793-cc78a13a482c | -3.0189 | -53.24714 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a7b90174-cf34-318d-ad73-fa53cfbfa804 | -3.01772 | -53.25415 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 830161b3-9822-3f8f-b4f8-91ede93979e3 | -2.40748 | -48.91041 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f16a56e-ef8e-3909-8cf9-50b974c9f13f | -2.289 | -46.51548 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b76508d3-d59b-3c2a-8cf5-076991d6017a | -2.23301 | -46.44141 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d41d00ab-9547-393d-a777-6df2c521f55e | -2.37337 | -50.33374 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ed4dae8-5d01-3417-8cee-83801a8ffb66 | -2.64879 | -46.81063 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5325c27-8d1e-33dd-9b21-af1949525fc8 | -5.27071 | -45.73387 | 2024-11-11 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cbea6ad9-192d-3bd0-8f15-65a3023449b6 | -3.13364 | -45.97176 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcf1a275-4603-3c98-bf2d-c74d77077669 | -2.92219 | -45.63409 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dba7123-5fee-33ba-a4b9-9614ff486a21 | -2.22268 | -53.66737 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f49855e3-2409-34f8-a4cc-8d5b53644b8b | -0.15001 | -51.40186 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df5ff0ac-7255-3d23-9416-e3532fdb7111 | -5.2679 | -45.72974 | 2024-11-11 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2490816-c09b-35a1-a874-34d5e497cb20 | -2.23411 | -48.38649 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4a2ed45-311a-3447-ad8c-172be00abfba | -2.31689 | -48.44358 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f893bf89-2a67-31bc-99eb-09a89c6b4dc8 | -2.67232 | -48.66323 | 2024-11-11 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 026eb81a-a27c-3351-be29-7d14f3bdc504 | -2.73538 | -45.97711 | 2024-11-11 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2378fb2-b530-3f65-a31f-bee5cce252b2 | -3.12489 | -45.23634 | 2024-11-11 04:18:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c381439d-e65d-33e2-9d4a-3bcd33b44514 | -2.10584 | -46.53813 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b094e1-3dc4-306f-8296-bdd41008df91 | -3.87984 | -52.39049 | 2024-11-11 04:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0df877c2-6f91-3e15-8a84-59eb72923df6 | -2.01032 | -48.41034 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20d9c2b1-daa9-3474-b0ea-9744db8b27b5 | -2.18856 | -46.58358 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67e8991b-5aeb-3caf-9f76-ab861cba28cc | -2.15661 | -48.90064 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a510d1c1-88f8-3b67-a2da-b933dd60b5db | -4.90542 | -45.85822 | 2024-11-11 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1dccf88-1d2d-395d-8e41-0c1350765912 | -4.842 | -45.84055 | 2024-11-11 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README36.md)
