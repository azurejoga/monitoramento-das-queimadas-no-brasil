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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1544c54a-cc93-36ea-8db6-436fa45186a1 | -6.90179 | -43.71383 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76db4529-a85f-3f06-a005-967694a347b1 | -7.90439 | -48.25315 | 2026-07-06 05:01:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ee2fd31-0dec-3258-b89e-627f6cb4d717 | -9.2731 | -48.21378 | 2026-07-06 05:01:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2b6464d-af6c-384c-9f63-a6e80a3adae3 | -8.73305 | -54.56444 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3bb2607-de1b-3889-a029-f52aa9f88bba | -6.8894 | -43.71626 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 208b42b0-8187-37d7-929f-4d5ddf71ac7b | -5.67491 | -48.09819 | 2026-07-06 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a25f1daf-ac20-3959-ab4c-c852afab5314 | -6.94204 | -43.72816 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f156723f-1054-3b33-8844-0b6b353535cc | -8.73084 | -54.55696 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcfdcf16-6872-36b4-ab49-2bfb064388dc | -8.72021 | -54.53743 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77db91a1-e472-326f-a627-f848a88894f2 | -8.12007 | -47.12011 | 2026-07-06 05:01:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e6ffbbc0-2c8c-37f3-b86d-f8923301753e | -5.28358 | -49.33326 | 2026-07-06 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c5350a7-0ce6-38aa-b266-a325626ffefa | -8.7336 | -54.56096 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32646aff-aa55-3c32-b20b-767571ff6eeb | -8.73636 | -54.56497 | 2026-07-06 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00837fdf-6a71-38f6-bc7b-aef9df3f1478 | -4.34495 | -47.76624 | 2026-07-06 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53a94ca4-918d-33e9-8b61-1318badeb19c | -6.94264 | -43.72386 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb5cd723-807d-3d40-91c3-080c7f457430 | -6.42688 | -55.79362 | 2026-07-06 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7123d44c-8d0a-34ae-97e7-bdaca3f3cf53 | -6.94142 | -43.71837 | 2026-07-06 05:01:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1c88eb9-8fe0-3896-a3f9-896d05ee4285 | -3.5889 | -52.47621 | 2026-07-06 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e1ee9b7-8c45-3403-9147-11ca2532ed2a | -9.74878 | -48.18682 | 2026-07-06 05:01:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d6c9600-3b5c-3c26-8c2a-0531b10b4abf | -4.34556 | -47.76207 | 2026-07-06 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 942c3992-3152-32f4-8687-c9689e1f8951 | -13.24925 | -54.31121 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2318c768-226c-34c0-b193-f77d5238889f | -10.39167 | -56.77224 | 2026-07-06 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16f8f441-f820-3e9f-b1f4-6734a1382ef1 | -11.92744 | -55.91172 | 2026-07-06 05:04:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2e9c084-a23b-3cfb-bd33-fa1050c6bf9d | -9.25175 | -60.33099 | 2026-07-06 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f718879d-a8f6-34b6-a42f-cdafb112ea01 | -13.20405 | -54.3041 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74b96f1f-be94-3dc7-9684-5ae6fcfda0d8 | -11.46647 | -46.54743 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82d56bbb-5737-3ef9-a4bd-70775fd79fae | -14.02224 | -53.94274 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1517473-e9c0-3025-be3b-f84bb884b312 | -13.22848 | -54.37978 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05ee4606-4521-3e83-bef9-eea63f8d4d70 | -13.2943 | -54.37893 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16ac71f0-bc46-3a8e-99aa-b4da4d8d22dd | -13.31064 | -54.36265 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 055fcff5-a60b-34ea-b3c8-e71595629f51 | -10.77635 | -54.11033 | 2026-07-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c54d283d-726c-383e-8e73-cc3480f7d521 | -13.20462 | -54.3004 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e380728e-2ab9-341f-a96a-c5cb46182806 | -12.43967 | -47.00519 | 2026-07-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a24cda3b-919b-39a0-9075-7c4f68982ac9 | -13.28474 | -54.37362 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 35542654-d12a-3584-99fc-c16259db9d4f | -13.24868 | -54.31492 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5edfd1a-cf7d-38bf-beda-d2d805ac33e9 | -13.28418 | -54.3773 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee261b39-f9e4-30c6-85f9-7c6df9251021 | -9.25111 | -60.33467 | 2026-07-06 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3519e67-d50a-3f48-a15d-9c0a70a82866 | -13.29993 | -54.38735 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71dd1405-33dc-3402-b37b-c3d6b259e3e3 | -10.92832 | -43.05735 | 2026-07-06 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b1287a03-539f-36db-bfe5-1bbab1929b07 | -13.2239 | -54.31854 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d997012-4405-303a-9172-65ad1edfffac | -13.25545 | -54.316 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29d0fd02-9e15-354a-ac21-5b1369d79fa5 | -13.2515 | -54.31917 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7adc4bb5-3a00-3724-b3c1-9ad2a3f5f4f8 | -13.31007 | -54.36633 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3677c23-7c8d-37e9-b26e-76bcb0ccf82e | -11.45552 | -46.63173 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24bcbe88-3e1d-3a38-8858-1b4b6e7440d0 | -11.92681 | -43.37445 | 2026-07-06 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 411ff8fe-fda5-362b-b2ed-9a5076a5acb2 | -13.208 | -54.30094 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eac846b6-2a09-38e0-b278-f1997dec87bc | -11.45074 | -46.62786 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4e40410-3425-34c3-8ab1-0eb36054ef9d | -9.21 | -67.40042 | 2026-07-06 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c97d6029-00b2-3c0c-a46d-be898ba043b9 | -13.29825 | -54.37578 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e530c382-f035-37bd-a53e-d5562dd9c797 | -13.25207 | -54.31546 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ce06814-599d-3b6e-8245-6a5df58fb3fd | -10.20907 | -61.48579 | 2026-07-06 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b892e191-f913-3ffe-9dd2-d1350a8355a8 | -11.31138 | -54.47292 | 2026-07-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38ec4198-24b9-3df9-a841-dfc4d4b932c8 | -11.44122 | -46.61966 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5f2c2df-16bd-367b-b56d-f69a35ed01f6 | -13.22895 | -54.30799 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca64d121-ff0a-3ee7-8f92-ede655500a51 | -13.20743 | -54.30465 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f773bd59-b060-328e-a919-c8d7959e6ed4 | -10.20473 | -61.48494 | 2026-07-06 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e94b55a-d5a7-3900-a566-0a7ff385cc6c | -13.29712 | -54.36051 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dcd41af-20e9-36af-81f7-a436204f5f40 | -12.15473 | -57.21793 | 2026-07-06 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dece4fae-6ba1-3c4a-be58-a27975f45856 | -11.9203 | -43.37412 | 2026-07-06 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e4a63868-56d8-385d-b82a-4ee101adf2ad | -13.30331 | -54.36528 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b97a375-555f-387b-bb10-a357ba98bbeb | -13.24474 | -54.31809 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1487b586-01c2-323a-9d6f-47306b9d55d5 | -13.22114 | -54.35979 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be6598e-b6de-344c-ab34-6c30a8455d3c | -13.29937 | -54.36842 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 063b752a-ce1f-3ddd-8ea1-5f8b65ce3b2f | -13.24192 | -54.31384 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a36d97ea-d2be-371c-83d9-3f9f2a27c71b | -10.62326 | -53.89486 | 2026-07-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17abeb0a-b2f3-3a6a-902e-077913cccf1b | -12.15751 | -57.22218 | 2026-07-06 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdfade76-8e77-3913-9e64-be3fcf9aaab9 | -11.62929 | -48.44723 | 2026-07-06 05:04:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f779e231-bd59-350b-aa72-2c66ec1cc66c | -11.41061 | -57.81311 | 2026-07-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e301bb48-d71f-3459-8937-4217b70b90d5 | -13.2105 | -54.38445 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf2ccac7-1523-36c9-875d-32c3bf728a70 | -11.44556 | -46.62696 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62e0a597-ba34-3481-b3af-0b504f0cf559 | -11.43639 | -46.61609 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0255fe6-8ea5-3fd4-a124-54e9cae11416 | -10.39226 | -56.76858 | 2026-07-06 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d059666-a717-33ae-ab0e-ad621aeb066e | -9.21109 | -67.39487 | 2026-07-06 05:04:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d400c85-89a8-3f98-abcc-8bc0e5bf66b3 | -10.45301 | -49.97609 | 2026-07-06 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff1e61f1-931b-3e0c-b32e-aaea3ffb7c22 | -11.46607 | -46.5505 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cf3e553-97b6-3f2f-98c2-2958d1ea0f1c | -13.24136 | -54.31755 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8d38429-4419-364b-9670-e07453524774 | -13.2453 | -54.31437 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a8c951e-5241-3554-9412-357a205c56a9 | -10.93493 | -54.09849 | 2026-07-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3568516-387b-38e7-927e-ff4548f4b79c | -13.23798 | -54.31701 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7635853c-e00d-3921-b5ad-c35528c9ccdb | -13.20123 | -54.29986 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fb78d9a-0aae-3242-b993-0b83037aeac9 | -11.9132 | -43.379 | 2026-07-06 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b635bc75-da2f-3a43-87d6-cd8807dec4f3 | -13.30106 | -54.38 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 468e46fc-1b8e-33f6-ab60-c7ca071c5ee7 | -13.29375 | -54.35997 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 460e69ad-6cb6-33d9-8828-888ac85f4328 | -10.92766 | -43.06285 | 2026-07-06 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 33d00e2d-bd06-393f-a1de-44ce25b1d932 | -13.24812 | -54.31863 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 891150b8-9dbf-3b7b-8d94-c4bb957f64a8 | -10.90192 | -56.85215 | 2026-07-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 226e44e8-4671-36cd-8dbd-ff0e4089e9a9 | -11.45592 | -46.62864 | 2026-07-06 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 772af169-34b0-3f23-b308-308953fbeb3f | -10.39505 | -56.77279 | 2026-07-06 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc48a05-21dc-3c2b-aef8-bd07b3f7610a | -11.9197 | -43.37931 | 2026-07-06 05:04:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fb252c4d-2caf-3c5a-a6c0-f791ff0c7e0e | -13.29768 | -54.37947 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2780fb4-7007-366d-8c04-b74acff924ac | -10.45709 | -49.97668 | 2026-07-06 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 467cf149-fff4-32ac-9b03-296dec4752a2 | -13.29543 | -54.37156 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7118c5e5-b5fc-35e3-b773-df05facd0d44 | -13.2808 | -54.37677 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2dcca2ab-9b62-3751-b1fa-964f38c16828 | -13.24418 | -54.3218 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16ed5329-b47a-361f-895b-ce3ec9000cbe | -13.29881 | -54.3721 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 267f8881-40e2-3266-a06d-9e0b4aee38c0 | -13.29655 | -54.38683 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cbd39d5-a583-3618-9668-c41974190523 | -13.29994 | -54.36474 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c326475-1d13-3b59-b693-72b6af9427b2 | -12.43929 | -47.0082 | 2026-07-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9c641e0-a8da-3b77-98fd-d4c1497ff07e | -13.30275 | -54.36896 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f5b7cb7-91c2-370e-b50b-ea2ab64173e1 | -13.29318 | -54.36366 | 2026-07-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README6.md)
