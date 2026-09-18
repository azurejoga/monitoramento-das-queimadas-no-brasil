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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 210e5981-ae6d-366d-a0a8-0b01aef66d6e | -10.67752 | -50.26549 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cc0cb7b-abb3-37df-99a8-1fdd2cd8582c | -8.46132 | -44.51037 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96c48fc3-dd0b-3b2f-92ef-8f28ee60e235 | -9.18919 | -45.69277 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94f4b5f8-7ac6-33b1-a0a3-ce3f1cf85bf9 | -9.91189 | -46.56369 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fe328e3-8a53-3c00-827e-fa035ee9f43c | -9.54978 | -45.48438 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f16861aa-6a0e-3fa1-a9bb-b412abb8830d | -10.66725 | -50.26389 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| a1c7bb11-9dce-3591-ac93-355d2ead9b3c | -12.31589 | -50.7655 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 948eb0b2-bcd0-339d-bfad-c028ce445bd7 | -8.9321 | -51.46381 | 2026-09-18 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82fe96e3-b30a-3f96-b1b0-bb452daef999 | -12.43073 | -50.67645 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1471fb92-853b-3be2-b5c9-b5c0d62551b9 | -8.51523 | -48.49572 | 2026-09-18 04:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff4c2acb-8c0d-392b-996a-ec7174b09425 | -7.19568 | -41.81156 | 2026-09-18 04:57:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29858122-6399-3e0d-831d-23243a177618 | -12.36601 | -50.68929 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfce13ef-269a-323e-a52d-474b183f9f85 | -8.46066 | -44.51516 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87b21f87-031f-3912-8bc0-080c7e46c95a | -4.87634 | -56.0692 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f4e5342-d697-3c48-83a1-eb24c025d19d | -9.46152 | -45.44347 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2331d96-d5c8-3a45-bbc6-44d4f7d0ae8a | -10.95234 | -54.09391 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf409881-8607-377e-9bc8-43099757ce9f | -11.33513 | -43.39771 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79193e6d-9bce-3e5f-8e07-33765b756700 | -9.91598 | -48.38395 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d24c4e37-bfe2-32e3-a96e-6802a9b1b492 | -10.63585 | -50.23988 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7274132-b70e-3c78-bfbd-4db148478d51 | -12.43815 | -50.67377 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d555212-afa9-39e0-b3b4-006461609e43 | -10.71659 | -54.01591 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4dc1b74c-ec3b-3820-a5e2-8c1dcab190f6 | -10.67067 | -50.28732 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06b97a65-beae-367a-9234-2c373a4e8707 | -7.46175 | -46.83789 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ee5a612-368d-3ed8-91ba-9861539ae9dc | -12.26586 | -50.74997 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fb4381b7-57fa-3579-b9ed-abf076d0d5e7 | -7.20021 | -44.10239 | 2026-09-18 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cb01d29-4eba-3b85-b653-3d928ef51296 | -12.1673 | -46.98364 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 305807a8-3d74-39b4-a4f3-cc26ef23c321 | -12.3095 | -54.1275 | 2026-09-18 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 101feba1-8365-325a-9d6e-f8d0bc87975c | -13.25135 | -46.90479 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3219c3ef-fcbe-30e1-bedf-9f7be371324e | -12.40623 | -50.69945 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74a9b6a6-be43-367b-bc3d-4598e9e39dd4 | -7.34409 | -44.64246 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fb8e53e-391f-3df3-8fdb-d859ee9f3591 | -7.34917 | -44.639 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2565b85c-9695-3d14-a63f-b59151b0a0f4 | -11.52069 | -46.87912 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14aa8377-6a96-3813-b179-23af590bb3b7 | -11.27677 | -54.11959 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48db9e2c-6d64-38d9-8c22-07cff073c4ca | -8.55671 | -44.8956 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ecaecda-8b09-3447-82bf-7843856ac81b | -12.51379 | -47.09443 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70e24b4a-b56e-333c-a9e5-c3435da3fa03 | -9.90741 | -46.50623 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87336d06-0053-3729-a60b-c9ef5ef652c3 | -10.66322 | -50.47192 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8230a4c9-078b-3e0a-936f-c8b939175751 | -10.62617 | -50.25747 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fc98dff-5674-3150-bb12-0b7cf6b605b2 | -10.49651 | -46.288 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a18f67a-e25a-340f-9980-dd2991b3f212 | -10.80379 | -46.66105 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7507396-9831-3d41-85c9-394f9c3b807a | -4.51146 | -56.08167 | 2026-09-18 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16fb4217-4eaf-3520-8f17-8b55ba32ce97 | -7.80895 | -44.9061 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17b44325-d3a1-35a7-b930-a428ecd7e8da | -5.88691 | -52.08722 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25273db2-dc7a-3951-b7a7-d6ae405fc4a3 | -6.99704 | -42.15791 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b4cc537-152b-3591-a086-c2afe70d4f03 | -12.29769 | -50.74737 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e815cc8a-ed48-3d01-a656-bca0d484ea4e | -10.1192 | -45.56747 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9173ce58-a633-3752-835a-958550413387 | -6.44286 | -44.95111 | 2026-09-18 04:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f3b9d2f-86f2-379c-b1b8-2255d90d1474 | -7.62936 | -46.1662 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 683bd4d8-38c3-3dc5-a15c-530d59d01c98 | -5.86676 | -52.06214 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2caefb62-6918-3a7c-8716-32689d98e8f0 | -5.97874 | -53.58259 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c41482fd-8838-3473-9c54-4dccbde7c11a | -6.65788 | -50.91629 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0155cba7-3aa0-3e6f-9380-650401fd0f3c | -5.85946 | -52.06467 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaf38d0a-0570-3d54-b5d7-3336523c283c | -5.86404 | -52.03605 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2d47d74-82f2-381a-bafc-a7760e2b3c9b | -9.92629 | -46.58035 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daf6bee8-c385-3821-8dd3-972ddafdfb44 | -9.70942 | -54.81787 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c1a39182-a7a9-3388-aee2-06e89dfaf748 | -7.96165 | -54.90479 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57173de5-b462-3d41-9e6d-55aad3594562 | -10.94952 | -54.0895 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07fdff08-b4f4-3821-8fa0-7613d31679bd | -5.88778 | -52.09081 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ad28d22-bbf1-3a32-b662-433c9d3aacaf | -11.2991 | -43.38955 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20ccfb0a-de8a-363f-812c-1101e907bdaf | -10.49763 | -46.28003 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92a4bdd1-bc71-35ed-a8a0-08e1ccfd9a17 | -12.17259 | -46.97617 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40e8da31-6b8c-3318-97a6-5fb002fb7b20 | -6.93316 | -43.1198 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 293e2447-6cd3-3e27-a811-115f559f1d39 | -11.47796 | -45.72147 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71d6c260-b7b4-37ad-8e38-30bc4217ca28 | -10.86824 | -53.99032 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ce65ce4-10c5-33e8-9ed2-9108a5ed0ce8 | -8.68137 | -45.4322 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41915b1e-7545-349b-ae31-9b066da5e34b | -7.34912 | -44.63216 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5c600a40-cef0-3dd6-aebf-dd3c6a4f0650 | -6.94749 | -42.55088 | 2026-09-18 04:57:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 282e6aed-ecd4-3983-b9b8-94cd6f19e66e | -6.33509 | -45.67338 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8dcc666e-e817-3646-b47a-d99f23697c03 | -11.89802 | -47.57282 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6421b3af-ef77-3a92-9dd0-d4aab0ef07c0 | -11.2987 | -43.39268 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd4bd596-8cae-367f-a279-7970b72de178 | -6.34504 | -57.88302 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| febd84b7-a079-3bb9-bd87-d8c7d4406c2a | -7.00349 | -43.86956 | 2026-09-18 04:57:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00a7f91b-4374-31ba-a326-b899895fa5b8 | -7.94836 | -54.89363 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa214d7b-8fd6-3dbb-9831-c126e75900bd | -12.27103 | -50.78506 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87c02670-76d9-3a7b-bcf9-82dda095f68e | -10.65469 | -50.25429 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 068ad0a3-717b-3c7b-b4b7-e652f904ada3 | -7.20487 | -44.10312 | 2026-09-18 04:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f40efb5-caca-3e17-ab95-5d1d4ef41704 | -8.88416 | -50.78304 | 2026-09-18 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeedf0b8-0f11-38ef-9968-a5aaf3a1cb3c | -11.31274 | -46.77151 | 2026-09-18 04:57:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecc6b05e-9711-3f76-94e0-dac477df3a31 | -9.59871 | -45.86305 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2d56c943-3e3b-32b7-aafe-828ca823f456 | -10.87952 | -54.00779 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6237bc07-257a-3ccf-a7b0-3009531c6a00 | -12.1702 | -46.97479 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69b9fe69-66f3-3326-b3bb-e822e3db4e02 | -6.67228 | -50.91145 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c67234fd-331e-3d53-a6a6-58e98005114b | -10.12341 | -45.56625 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e2c9a73-12d6-3fd8-ad02-666a0165c223 | -9.04286 | -47.75905 | 2026-09-18 04:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb101d86-1d2d-326b-991d-d1b8807552d3 | -7.79177 | -44.89893 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6521e571-3c54-3b82-b475-ded23ed237f6 | -12.18084 | -48.97883 | 2026-09-18 04:57:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fdddb42e-47e2-3b22-8a10-57019de227e3 | -9.94316 | -46.60869 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f06cd8a9-bf63-3f0b-b5e5-3116867b64d4 | -5.8648 | -51.94529 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5c9fc1d-aa39-33c2-b49f-ed3d2b65d99d | -10.50609 | -46.28114 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ad756da-1af3-3be2-a30c-bf14590250d9 | -9.91658 | -46.53068 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24b8419b-15dc-3d8e-9010-68a53e5bd0a3 | -7.49932 | -55.01083 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d5ef0d87-52e5-3101-957d-f75ef2b8458c | -7.8103 | -45.11406 | 2026-09-18 04:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8afe82ee-38e7-30ce-b70d-be412f0e8a5d | -12.43016 | -50.6802 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43f38160-2fb8-3343-847f-a843692034ac | -9.83389 | -49.23333 | 2026-09-18 04:57:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d84963d-f483-396c-894f-6b53243a616b | -8.95887 | -50.8455 | 2026-09-18 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 616a9941-104a-3c7f-b9ea-2158f30fc97e | -10.12781 | -43.95487 | 2026-09-18 04:57:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14efad29-5376-3d90-af9b-393261ccfb39 | -7.68002 | -46.09882 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edc7d3eb-dbac-3bc5-b8ec-dbb02bb47dbe | -9.56286 | -45.45549 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f88a780-cab4-34c1-8082-9764a6f42233 | -8.35328 | -45.98582 | 2026-09-18 04:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1120e280-eec1-3e52-830f-6cdeb823a5f5 | -12.78762 | -47.56101 | 2026-09-18 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README65.md)
