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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a973846-effc-3f15-8831-112a3ec1e6e2 | -10.81429 | -57.75001 | 2025-06-28 04:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5b4615f8-b75c-38d1-87c5-981b0f141275 | -12.6553 | -54.10279 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be506e28-14ac-3874-bde6-2d688fa0f549 | -11.0345 | -55.3784 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f2f8a107-2e7f-3837-b8c4-f420ec6a87fe | -11.05203 | -55.07631 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 537ef526-e816-3c58-99e6-cc78e1ce95fa | -12.50519 | -58.35929 | 2025-06-28 04:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e81bde-4f29-366b-8bc8-ebb31cca69b6 | -11.0518 | -55.07256 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b293331-865f-3fa3-a413-05208d7fa5c0 | -10.28327 | -57.01301 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 550c1058-dbaf-3065-9856-4696fe5d0200 | -15.07737 | -48.94426 | 2025-06-28 04:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81d48321-8f69-3bd8-b73c-17c7288474a5 | -13.57632 | -45.26117 | 2025-06-28 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee87f7dd-3eab-36a3-a8d3-fafdc4ec88f5 | -10.52821 | -53.621 | 2025-06-28 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75a6715e-07e8-34f7-9319-ecdfe3f042be | -14.89386 | -48.4025 | 2025-06-28 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57630c0f-e50b-3aa8-997b-d910ce4e6e33 | -11.05025 | -55.37553 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 0463258f-0b02-388b-b9fb-06e246b2c681 | -13.29074 | -47.52008 | 2025-06-28 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ca5f28b-0531-3581-aa37-0a084edc3f27 | -11.65853 | -46.73098 | 2025-06-28 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d9cee7e-ac05-32e6-b488-ed4ca3c6953e | -14.83708 | -59.80107 | 2025-06-28 04:29:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 797254e3-5e14-3c76-bfdb-f88c6c5f92b5 | -13.94609 | -54.49374 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25f1a107-04b9-3508-8812-8a5114f296df | -11.44255 | -54.47169 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 780e503f-46a4-300b-8873-0ce9e0ca16f9 | -11.60796 | -47.61282 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee9ccecf-8019-3718-a447-1ffaaf60b15e | -9.70804 | -56.18047 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d2f9401e-793e-3200-bd42-92be4b5b3158 | -10.04163 | -59.36172 | 2025-06-28 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbe21091-f12d-37bc-8ca1-aa419e78cc8f | -11.18514 | -55.9208 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1412fab1-a26a-318b-abfb-1b0f4d15e4f9 | -10.82932 | -53.75159 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 602b91bb-3b52-3586-8275-865f5e49c721 | -11.27255 | -52.74559 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c8bec87-dcd0-3493-b828-79947d1ca40b | -11.27055 | -52.75674 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2a1c29ec-f0c0-3afb-901f-4842c3d78916 | -11.88402 | -58.74213 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96071079-ec4b-3417-9e0c-b099caf1f586 | -11.26924 | -52.74924 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 753d60e5-201a-34e1-9640-0f8eae4f0248 | -10.03005 | -54.32604 | 2025-06-28 04:29:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 165afd4b-6e10-393f-8787-4ab1d4ab14c8 | -11.43996 | -54.48589 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f6c9b3c-def2-34a0-af58-0d41bc4b38b5 | -10.83659 | -53.76194 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d86b11a-deb8-391d-b2fb-4bf0b1c82e39 | -11.57704 | -52.11979 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07ad8943-cee7-3fa0-8048-1d84ad55d1fc | -11.18569 | -55.91787 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1814da0-d618-3c4d-bcf6-a3545c6bd87c | -10.03666 | -54.34248 | 2025-06-28 04:29:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b6f9e14-0aaa-3087-9460-9acb331e9e82 | -10.28715 | -57.01711 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9921d610-c68d-3acf-b546-74acf04e92ee | -11.88497 | -58.73742 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 491bd062-35bd-3505-bc6f-8a46b79c1eee | -12.10641 | -54.66966 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1320c72b-a7d1-3968-a82e-5884998bdf8b | -10.95161 | -49.2524 | 2025-06-28 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c03b1a6-7045-3f89-a889-6eb8f80b7aab | -12.65513 | -54.10067 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 567e5a14-9873-3945-90fb-6a40a5535431 | -11.56623 | -47.62448 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 591272d1-e265-3267-8bd3-8b3aaa8c7365 | -10.84618 | -53.75925 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 489865c9-282e-3e3e-8fab-550114ac1cb6 | -11.57486 | -52.10894 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7283df09-3505-370c-bde9-c2c4fb3f5909 | -14.68937 | -53.38481 | 2025-06-28 04:29:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db0eb2d1-645e-3433-b3be-7b2cc98667f9 | -9.71801 | -56.18574 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 37ded540-9724-3bc8-97b0-37fbcbc0f29b | -14.53318 | -53.83974 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5286facc-0c5b-3059-b77b-51eb92e5c493 | -12.26034 | -46.77061 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 519c8f26-fa99-3f7f-ae12-08b052a20a8d | -11.84171 | -43.79523 | 2025-06-28 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72ec740c-e0a6-34ab-a820-d1d6d242d761 | -11.88273 | -58.73952 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebd3973d-58bb-3bdf-b874-fd2d9fe775c1 | -11.04723 | -55.0754 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f818771c-b9d9-35ad-9666-192581190d7e | -10.29883 | -57.1366 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 605f0ff2-8d04-3d97-aadf-fc073a08ee42 | -10.95595 | -48.15585 | 2025-06-28 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27dd12b7-0358-3970-86d0-e5993c4e9b8e | -10.87028 | -53.77761 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aed849ce-6048-33d3-bcd8-c2af2cec882d | -14.69613 | -53.39364 | 2025-06-28 04:29:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9551c12a-7913-3069-aa12-0b6892c05731 | -9.71739 | -56.18904 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 978e3162-ccdd-397c-8a7c-cb57fe92ce31 | -11.44083 | -54.48112 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43874637-e91c-3a14-bab8-b3104c712c61 | -10.82207 | -53.74123 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79a00378-e168-3430-84f3-5d1798fb65a2 | -17.04438 | -43.7715 | 2025-06-28 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0ae0ab9-50d4-32d3-9ef8-3025641c643f | -11.67355 | -46.72239 | 2025-06-28 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cfffd2b-ccdf-3027-b8fe-cb519f7d95d4 | -10.8696 | -53.77563 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e57d77c3-bb83-3e8f-b98f-848b5d2469e9 | -11.83798 | -43.79466 | 2025-06-28 04:29:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7a14e62-ee69-3f88-b943-cf4a6ab5ef1e | -14.38232 | -50.32913 | 2025-06-28 04:29:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24a23751-cfc3-3ad4-bd9c-9aa26a4e6590 | -11.57399 | -52.11401 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| caa2d0c6-719e-3adf-9863-d371c71433e1 | -14.88778 | -48.39781 | 2025-06-28 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4bc843c-2bef-3654-bc2b-4e7d48c1b022 | -12.10417 | -54.58374 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41e4b043-bdc5-3631-889b-27630d298137 | -12.02521 | -57.09124 | 2025-06-28 04:29:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e2d926a-e54b-3fb4-b0db-3e8081d81ade | -12.25865 | -46.75933 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c27efbd3-b44d-3384-a624-23d44a3fc03e | -12.107 | -54.59417 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7604619c-46bb-3083-8787-53e29f1abcbf | -14.6921 | -53.39279 | 2025-06-28 04:29:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc40cb81-cf21-3484-91e7-063dca247cbd | -13.63965 | -47.68605 | 2025-06-28 04:29:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac126500-6265-3dbc-bbf6-2266e056518a | -11.77941 | -59.31961 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6801d578-67ec-36b0-beba-326d9106214c | -11.87988 | -58.73177 | 2025-06-28 04:29:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1c4094-18ee-3a77-9148-6a70cfcaa09b | -10.87561 | -53.76771 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2310815-7381-308f-b13e-79edd58adc0b | -12.02575 | -47.77481 | 2025-06-28 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76e8db0d-40f6-3533-b75d-89c77754c4be | -12.11328 | -54.58551 | 2025-06-28 04:29:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b8db5bf-5444-3808-8951-7108ef7c8894 | -11.57878 | -52.10962 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83498d2b-fc09-3c96-89ca-d06844c49cce | -10.1589 | -53.92516 | 2025-06-28 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 476c0137-955e-31de-b7ab-e96085c59212 | -17.04366 | -43.77695 | 2025-06-28 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16d8d413-e933-30c3-a99a-8c4f540f3cb5 | -14.68873 | -53.38837 | 2025-06-28 04:29:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a58b2e45-3e0f-355c-a88e-5cf98109ef73 | -10.83813 | -53.75327 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 818ea108-9950-312a-8685-d4075784315e | -11.54043 | -47.87335 | 2025-06-28 04:29:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c61647c-d7c1-322b-bb07-398bf909261b | -9.71272 | -56.1847 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d7619fa9-4385-3ee3-b1bf-1053124bc17f | -13.07407 | -48.83953 | 2025-06-28 04:29:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f21f0f6-9873-31d6-8cf6-84b848fa51d8 | -9.71861 | -56.18249 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f137fedb-cb44-3fd7-b0e9-21eaa3a205d0 | -15.68222 | -47.74563 | 2025-06-28 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8031f488-23fb-392e-bdcd-ccccd476ede8 | -10.83581 | -53.76636 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d630f8a-b6dd-36bc-83ea-017e9a037bfe | -11.43883 | -54.46616 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b98a6ae7-2a07-3179-96c3-56eec60d0f6b | -12.20167 | -49.64466 | 2025-06-28 04:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 783015b2-fd2a-3c5e-bbfa-b5e651dadaea | -10.50729 | -53.58585 | 2025-06-28 04:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34fffdb1-5bb9-3c14-86ec-c4dd5cd4eadd | -11.57038 | -54.51871 | 2025-06-28 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e759b04-fb0f-36f1-b635-8b492a2c7b5a | -11.03553 | -55.37287 | 2025-06-28 04:29:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1daff6b7-a754-3699-9d49-a40b4b5887d3 | -9.70617 | -56.19044 | 2025-06-28 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9dc02465-df02-3692-b9a5-5f234e129f7b | -10.82764 | -54.02993 | 2025-06-28 04:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b32667-b8d6-3529-bfef-26c1d71ebffa | -11.27598 | -52.75008 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a401c28b-f21c-326c-b74e-80ac371ccaec | -13.94172 | -54.49281 | 2025-06-28 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e3bf90c-ad31-3a18-bd8e-0893a846084e | -10.28855 | -57.00984 | 2025-06-28 04:29:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08c0abde-ea09-3ade-bb60-ed9e09e3bf7e | -14.69275 | -53.38921 | 2025-06-28 04:29:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2762d0ed-cc29-3ea5-ba24-6bb1dc430769 | -12.25611 | -46.76284 | 2025-06-28 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e5b8aaf-f145-33a6-a643-3c98d80200f2 | -11.80113 | -56.96208 | 2025-06-28 04:29:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 248ebaf9-52fe-3ed8-a8bb-0feee1c8bf51 | -11.58183 | -52.11539 | 2025-06-28 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3dbfd245-16b9-3afe-8d48-448423777249 | -10.05436 | -59.36276 | 2025-06-28 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a010cff-1f26-3075-a85c-495e6ef978c8 | -11.58972 | -44.66523 | 2025-06-28 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d129c628-811a-3555-a82f-76b3e1d388e2 | -13.29307 | -57.09083 | 2025-06-28 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README19.md)
