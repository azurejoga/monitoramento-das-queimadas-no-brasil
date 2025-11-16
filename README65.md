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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af7d7675-2d52-3f7d-b21c-84aa79d20d8c | -10.92968 | -48.69796 | 2025-11-16 05:27:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d3d8a076-1221-3e7c-9d6f-5d7b58fca2e5 | -11.70677 | -48.86211 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 836fde1f-ddb3-37b1-bb8d-bc1ecff35c2f | -9.83053 | -47.08745 | 2025-11-16 05:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 041a94c4-2f3a-3b66-ba89-462024c72e95 | -12.21766 | -49.54736 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c81519e6-4c54-3959-a6f2-b36fb6614d49 | -11.71131 | -48.39698 | 2025-11-16 05:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e82d806-b7b6-356a-86d5-02f06c860441 | -10.93026 | -48.69289 | 2025-11-16 05:27:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5752801d-7996-3ee0-85a7-fc28f892be17 | -12.19651 | -49.61659 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33933848-94cb-3c32-8598-348b88112b91 | -12.06004 | -48.19954 | 2025-11-16 05:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aee225cd-9fb6-3f0d-9c2d-af5be5edb063 | -9.82323 | -47.08633 | 2025-11-16 05:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb178197-15c4-3815-b0e8-01765ae6b2b4 | -12.21023 | -49.61308 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 23188331-0c60-33f3-8e86-df5875b3fdc7 | -12.40572 | -47.55231 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff90419a-7f02-3abe-b18d-7b9817d25216 | -9.72007 | -48.8978 | 2025-11-16 05:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aa9a611-bb88-34a4-a291-498e9b4a7553 | -12.00465 | -49.27773 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9b8125c9-de83-36aa-9077-b96231ca221c | -11.15851 | -49.44576 | 2025-11-16 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7da348f0-661c-395e-ae06-2a3c21303fd1 | -11.71586 | -48.85614 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6e8c1c5-3fb3-3acb-998f-7d8f167d6c3d | -12.40493 | -47.55422 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa00b4af-af19-3950-9ba9-60ea3b878aa4 | -12.01064 | -49.28423 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a72ce563-6b7c-3728-a33d-08da84f4f1e7 | -11.66248 | -54.58015 | 2025-11-16 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea0e86d3-c7a4-3e56-befb-e95b90d132f9 | -11.70709 | -48.87379 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb554b67-e8ed-3f3a-8ba4-e302906fd649 | -8.32285 | -54.75584 | 2025-11-16 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b2a846-439d-36dd-89b9-02379b0bb90c | -9.71864 | -48.89831 | 2025-11-16 05:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87b7c7a2-b61d-3acb-81df-1b383fa71b2b | -13.05399 | -53.95033 | 2025-11-16 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef7bbfec-12ae-3112-a816-fe6dc7081b00 | -12.40657 | -48.09484 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80474ea7-4e2e-397f-89c5-060520142903 | -12.20461 | -49.54577 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d421439-ef73-3268-b76d-d00b77a3a14b | -8.86587 | -50.18927 | 2025-11-16 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdad0c3d-c624-3f12-a10a-a1290f8de8e0 | -11.70843 | -48.86148 | 2025-11-16 05:27:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 428c684c-2506-356b-ac6b-ac99fea87a2a | -11.66446 | -54.58189 | 2025-11-16 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb851f0f-2db4-3016-bccb-adc48f9bca44 | -11.99968 | -49.2801 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b98ff9ec-7da9-3705-a766-811428b5a518 | -13.05469 | -53.94475 | 2025-11-16 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 155210ba-475d-3fa3-93ab-24fbfe8f6976 | -9.71136 | -48.90337 | 2025-11-16 05:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e720721-2565-34d4-850a-afc4df345403 | -12.40491 | -47.56007 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1be7136b-8925-37bb-b53d-efbf7181f8dc | -12.00403 | -49.28331 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 08da6d67-cc06-3556-8766-912e961ba8e6 | -12.19658 | -49.61728 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 208aa970-866b-3491-9465-b1f0a85981f3 | -10.8012 | -47.98737 | 2025-11-16 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25c0d79b-813d-3c67-8ea1-b1c0e0ec919a | -9.71793 | -48.90428 | 2025-11-16 05:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1ca18bd-2bcf-38fd-a5bc-a1cea50cc58a | -12.0129 | -49.28175 | 2025-11-16 05:27:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b174a36a-674c-3f26-81bb-1c8b828656ea | -12.41308 | -47.54775 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 929a93c9-5ca5-3b14-a4f9-16447f690e6b | -12.38523 | -48.09219 | 2025-11-16 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e9a88d5-e61e-39be-b8a4-bfd99832c4c2 | -11.16499 | -49.44655 | 2025-11-16 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26b428f7-ed55-3742-8403-b0feed2e1a91 | -11.99868 | -49.27105 | 2025-11-16 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0668067-c361-32ca-a720-a1e94785e53b | -10.66144 | -49.36853 | 2025-11-16 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ac226ca-2fc4-3c28-9a3f-04b5def87831 | -12.05929 | -48.20632 | 2025-11-16 05:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db27625f-3ce1-331a-933d-19ab049451a7 | -11.85015 | -47.60171 | 2025-11-16 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de24cad1-080b-3e6e-9077-9a9a0380e666 | -14.50043 | -58.42691 | 2025-11-16 05:29:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dd391f0-5f96-3118-b6d8-2a15527f65e3 | -6.3121 | -43.7804 | 2025-11-16 05:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5e93e048-8778-3bae-8365-7a3ea1ceed86 | -3.1093 | -45.2518 | 2025-11-16 05:30:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| de2bc779-2715-3b2a-92c3-b90da612155d | -2.5238 | -47.8115 | 2025-11-16 05:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4f0c72e5-63f2-30cd-9a71-44bbb6eee683 | -6.3119 | -43.8036 | 2025-11-16 05:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f8e60a44-262d-3145-ae28-65996950ac1f | -2.5238 | -47.8115 | 2025-11-16 05:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ed4b7c72-f6c8-38b4-8a97-fa0e15792c34 | -6.3121 | -43.7804 | 2025-11-16 05:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| aebeb9bf-e47a-373e-be95-dc4a359e1524 | 1.61709 | -55.81467 | 2025-11-16 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 589d998d-2833-36ca-b97e-7cef8dce699e | -2.89458 | -53.28878 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 222fdf2f-ba60-3457-9c36-a51f04af577e | -2.9691 | -53.21999 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be489b32-113c-3d72-bc98-86a3bf732eef | -2.88783 | -53.28776 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3bd8459e-2225-3d28-ad27-2ffc79ddfacb | 1.61765 | -55.8181 | 2025-11-16 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db295f97-5ca9-3482-9e17-6a4a2b4925f8 | -2.96141 | -53.22509 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdf99442-1a90-3f38-9e11-7d6d7729a354 | -2.89075 | -53.28255 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c0381055-5158-3983-b33e-e9205eb9c9b1 | -2.88989 | -53.28855 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 40494fd1-30a1-3aaf-b21a-ff8e232b23b5 | -1.84361 | -56.372 | 2025-11-16 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c607eb2-e565-341c-a0d4-03200fdd3d83 | 2.75285 | -60.36982 | 2025-11-16 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aef25d5d-3b2e-3d9d-bf72-ce0f0f2c557f | -3.08315 | -52.92664 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 099ce008-d744-37f2-82a6-90b9b3d8e426 | -1.34461 | -54.61054 | 2025-11-16 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc8365e8-92f7-3fdc-bd90-a10848b245c9 | -2.13463 | -56.68406 | 2025-11-16 05:46:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98d5e7c9-62bb-3f2a-89ce-10ec44b4f1e3 | -1.34492 | -54.61404 | 2025-11-16 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b6ccda1-586f-3412-b21b-f776c1e926b7 | -1.34566 | -54.60916 | 2025-11-16 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d133bf30-df56-353c-808f-8beb2ce00e32 | -2.1341 | -56.6875 | 2025-11-16 05:46:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e45e2d4-0861-37cf-a87b-f529054fb60d | -1.84854 | -56.37644 | 2025-11-16 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b00f5ff0-985d-3fd6-b3ee-0f8c21f7deec | 4.02395 | -59.6375 | 2025-11-16 05:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eed3bc48-90ea-31c4-8032-47704d1b9885 | -3.07626 | -52.92542 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9794a4e4-ea81-3c6c-8b0a-c24b6252d67a | -2.9682 | -53.22607 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d43f98d9-da62-3a10-82bb-e886b084d8ff | -2.96231 | -53.21898 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05382291-16b8-3624-aff2-a55417978daf | -2.80182 | -52.96735 | 2025-11-16 05:46:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 182dcd74-a212-3eac-b0c7-f7c126007f97 | -1.34386 | -54.61523 | 2025-11-16 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e262af2-004d-3e03-8657-5f0da7b6fb25 | -5.12231 | -55.96668 | 2025-11-16 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ce558ca-bae9-3fa3-922e-21bbb1eb8d15 | -3.49013 | -54.04812 | 2025-11-16 05:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3f7c834-46ba-3d88-b64e-03bda5e07216 | -5.1282 | -55.96766 | 2025-11-16 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d4ae327-f860-37a9-b0c0-7ffb861579ff | -5.12111 | -55.97519 | 2025-11-16 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3dd110-b47e-310a-b3ad-7fdbb3b9785e | -5.1217 | -55.97104 | 2025-11-16 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d9a7de8-a46d-3ca1-83e2-04a01947e981 | -5.12698 | -55.97618 | 2025-11-16 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d5e25b1-7e2f-355a-afee-5a961ae3213f | -2.5238 | -47.8115 | 2025-11-16 05:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 7f8daf1b-f734-3e76-b865-5fc7a9bd8c28 | -6.3121 | -43.7804 | 2025-11-16 05:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| f5f614d0-ee46-3703-9f07-27a4ed46a0af | -9.44467 | -59.20752 | 2025-11-16 05:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30084d7c-7c8d-30a4-9277-a607f7b676d5 | -2.5238 | -47.8115 | 2025-11-16 06:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3cdcf5d8-f621-342c-913f-ff047cacfdc1 | -3.9103 | -45.059 | 2025-11-16 06:00:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 286edc7a-b769-3f06-8429-be94056d714d | -6.3121 | -43.7804 | 2025-11-16 06:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 3fa45078-30c7-3255-9f34-03e3b5ff903a | -6.3119 | -43.8036 | 2025-11-16 06:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 62a487a4-9548-36c9-9490-bd2727efda61 | -2.5238 | -47.8115 | 2025-11-16 06:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 571017ba-daa3-3868-bd9b-b84d03682bc8 | -6.3121 | -43.7804 | 2025-11-16 06:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 78c9bbfb-0988-3e7c-9c73-e9a79472a5cb | -2.5238 | -47.8115 | 2025-11-16 06:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 098dae5e-3233-30b2-8634-68c04df2689b | -3.9103 | -45.059 | 2025-11-16 06:20:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ec623265-689f-338f-a1b4-28e8357e7800 | -6.5631 | -51.1126 | 2025-11-16 06:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 4c631d87-7d37-3acf-a9aa-cb2d21138413 | -2.5238 | -47.8115 | 2025-11-16 06:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| dc3a0946-11cf-3511-bd64-0c4637bf6d49 | -2.5238 | -47.8115 | 2025-11-16 06:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 125f0f09-6209-3c72-89af-c13e335aff6d | -2.5238 | -47.8115 | 2025-11-16 06:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5029cc2d-5176-3d12-8eb5-007ef7e102a3 | -3.4971 | -45.7748 | 2025-11-16 07:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a39a8167-c141-3e6a-a8b9-1ef5a38549b7 | -3.4785 | -45.7756 | 2025-11-16 07:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 954dc2a5-4cfa-3785-b2c5-d0d620878d48 | -3.4786 | -45.7532 | 2025-11-16 07:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7c6eb8ad-6fa2-3b71-bae9-be78def1ece9 | -2.5238 | -47.8115 | 2025-11-16 07:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b0e34816-179c-393b-b16f-8c2c210f96bd | -3.4972 | -45.7524 | 2025-11-16 07:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1d64c79f-5ddb-3290-a0bd-6944e69685df | -3.4971 | -45.7748 | 2025-11-16 07:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |


[Clique aqui para ver as próximas entradas](README66.md)
