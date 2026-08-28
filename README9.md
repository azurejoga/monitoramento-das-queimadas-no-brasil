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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f92a6330-ac49-3b49-a651-57e28625c2f8 | -4.8397 | -45.3926 | 2026-08-28 01:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d572c93a-117a-3071-9027-f5d5c8fcdbd8 | -12.4305 | -43.3944 | 2026-08-28 01:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| fb9aa934-5026-3d5c-9ba5-92e74724214d | -10.5168 | -64.4997 | 2026-08-28 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ebf405a0-54a2-3e56-8c88-d2b0805e2752 | -11.2693 | -54.0129 | 2026-08-28 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 286.0 |
| 95597a7a-9e91-3176-964b-93049be139a9 | -10.3895 | -61.231 | 2026-08-28 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 215.1 |
| aaca544e-9399-37b0-b6ec-656c76964a78 | -21.5511 | -48.382 | 2026-08-28 01:40:00 | GOES-19 | DOBRADA | SÃO PAULO | Brasil | 3514007 | 35 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 6d4c6cc8-08cd-36e4-bfa2-5e452e6b9692 | -4.8583 | -45.3915 | 2026-08-28 01:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b3773516-a4cb-3d2c-9e92-2aab824ff166 | -11.2879 | -54.0317 | 2026-08-28 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 174.2 |
| 5feae171-8711-313c-b2fa-cbe39768c421 | -11.2317 | -53.9958 | 2026-08-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6e3e6121-a09c-38dc-9965-732b44245e0d | -15.5403 | -41.9175 | 2026-08-28 01:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.4 |
| c5f4fb10-c99c-343e-8b04-9d45387b3aaa | -14.1645 | -52.8269 | 2026-08-28 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 55779482-c54b-348b-bf3f-528d017cb726 | -11.269 | -54.0334 | 2026-08-28 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 219.8 |
| 93268fee-3470-387e-8559-c8145b453f00 | -16.1638 | -58.6053 | 2026-08-28 01:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| fec37188-f77f-3075-9986-dc34c7e839e0 | -6.1657 | -57.7793 | 2026-08-28 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| c268b974-9ff6-3a48-853a-530625d4c1f1 | -6.1656 | -57.7988 | 2026-08-28 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 21307bc8-30e3-3084-b827-92a608416019 | -12.43 | -43.4182 | 2026-08-28 01:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 281.6 |
| d16fee05-c47a-339d-81a4-ded6feb9069a | -11.2314 | -54.0164 | 2026-08-28 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 767560aa-61f5-3f13-a3b8-f91b5f642bb8 | -14.8631 | -52.5893 | 2026-08-28 01:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 33d3a154-f9b7-3c88-a7a6-91098b849ec8 | -11.5663 | -45.5108 | 2026-08-28 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| ed415ddf-d467-3904-af05-a13fdc973c87 | -11.7357 | -54.5227 | 2026-08-28 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e98dd6ab-8d85-33c5-ad76-32e239bef531 | -11.585 | -45.5311 | 2026-08-28 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 7243f840-207c-32ab-a3e6-8d001a876f02 | -14.8627 | -52.6106 | 2026-08-28 01:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 518b1133-c545-3e55-b1d1-cde2922aa937 | -10.4981 | -64.5005 | 2026-08-28 01:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 319c1c95-d383-34eb-bda2-54dabaea6bf8 | -8.5968 | -54.7957 | 2026-08-28 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| f43bebdf-cf63-3b59-a9b4-daf38afadcd3 | -14.1838 | -52.8245 | 2026-08-28 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 2d3267bb-4e1b-359e-9730-5f78380b4f26 | -16.1444 | -58.6073 | 2026-08-28 01:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 32ed46b3-a5ee-31af-9a07-3363ac654b7b | -7.2474 | -45.846 | 2026-08-28 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 270.8 |
| a075a360-ae2e-3f25-abfd-2cbdd78f5f51 | -12.4305 | -43.3944 | 2026-08-28 01:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 2aa2e1e8-3483-379d-879e-c8ec568bc2a7 | -7.2471 | -45.8685 | 2026-08-28 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 392.0 |
| b5ec2a17-bc05-3aa2-80f3-f7fd1e6f8404 | -10.4081 | -61.2492 | 2026-08-28 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0748388b-2e81-3030-97d5-0fd06cf48cbd | -6.1472 | -57.7995 | 2026-08-28 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 665ff726-1e47-31f3-8472-a3120356e624 | -14.8627 | -52.6106 | 2026-08-28 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 925ba1f5-0e0b-3a3e-9524-7952c5ac325f | -10.7596 | -54.0384 | 2026-08-28 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 7274a8c2-1bd6-3f59-b3fe-bbc921155fdb | -14.8825 | -52.5868 | 2026-08-28 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| edb36bb1-5831-3e1d-ac22-61bba3a341ae | -4.8583 | -45.3915 | 2026-08-28 01:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| de4f6b9f-3232-3086-a497-a2f1c307a8ac | -11.2317 | -53.9958 | 2026-08-28 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d181921e-26aa-3235-821e-155211d3d7cd | -14.8631 | -52.5893 | 2026-08-28 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 454.1 |
| 1020fe96-baaf-3a3c-a106-e8f3f432ed24 | -7.2661 | -45.8443 | 2026-08-28 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 184.3 |
| f2f674ba-30fc-3af0-8aec-c323cb03dff6 | -10.3895 | -61.231 | 2026-08-28 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| 7c0d9993-05ad-3bed-ac71-8815d96f2f01 | -16.1444 | -58.6073 | 2026-08-28 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| cf5aec58-ae10-37bd-9dae-0e7d75497912 | -6.1657 | -57.7793 | 2026-08-28 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ae90357c-675f-3efd-bfc3-e8027c055909 | -10.9367 | -50.5332 | 2026-08-28 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 12f5bc3a-9f5d-3b8e-beaa-6b442ac4650c | -8.5969 | -54.7755 | 2026-08-28 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 25738e0a-8c58-3cb2-8d91-3fcf92e6b874 | -8.5968 | -54.7957 | 2026-08-28 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 56764f98-bbc1-3244-871d-b3eb7439edb6 | -14.1645 | -52.8269 | 2026-08-28 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 28a54848-3359-3eb9-83bf-d18e160ab8e6 | -14.8635 | -52.5681 | 2026-08-28 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| bf3b1791-e29f-319b-a2b2-110ec0efb53d | -10.3894 | -61.2502 | 2026-08-28 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 209.0 |
| 04a41d94-050b-3e12-ab42-9d93d209cea9 | -10.4082 | -61.23 | 2026-08-28 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6fa51224-4966-3f04-80b2-69121a708dc5 | -4.8397 | -45.3926 | 2026-08-28 01:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 444cd3c7-3674-3f15-acb8-bda431e76051 | -16.1641 | -58.5851 | 2026-08-28 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| d8114107-952c-3e12-ab79-d091ec929310 | -11.2314 | -54.0164 | 2026-08-28 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f412fedd-a70e-376f-a15e-ce43e39d69b7 | -10.9177 | -50.5352 | 2026-08-28 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 49e8d4ed-b8bc-32cb-8730-2cbfb0d2c3da | -16.1638 | -58.6053 | 2026-08-28 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 7f966b01-53d4-3c7d-af2b-0909cf866920 | -6.1656 | -57.7988 | 2026-08-28 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| f1c44b9c-16a2-33ba-b67c-1444e79afb7b | -14.1838 | -52.8245 | 2026-08-28 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b374a8fc-00c2-3dc4-8aa7-8b58afe20776 | -10.4981 | -64.5005 | 2026-08-28 01:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 56a5d81b-11a3-3a95-b753-bc6a8cb0474c | -7.2659 | -45.8668 | 2026-08-28 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 335.8 |
| e8a4342b-f4cb-35bc-9a03-c7403924228a | -16.1447 | -58.5871 | 2026-08-28 01:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| b6fc0500-bf91-39a2-9ff2-ab1ab0dc2107 | -14.1649 | -52.8058 | 2026-08-28 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 49d9c7a5-fcbe-304d-9a4b-b0137faced57 | -14.8437 | -52.5919 | 2026-08-28 01:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| a1daef36-a7a9-33a9-8492-70f444056328 | -7.2474 | -45.846 | 2026-08-28 01:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 712c59e7-bb8d-309c-8985-fee830dbc438 | -15.5403 | -41.9175 | 2026-08-28 01:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| d03beebb-60a7-348f-add3-f1f85ebb1953 | -12.43 | -43.4182 | 2026-08-28 01:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 3c7cf031-3351-3093-a0da-f1474e2e74e3 | -8.5968 | -54.7957 | 2026-08-28 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| af8b6930-410f-3406-86de-c4eb57f2df1e | -7.2659 | -45.8668 | 2026-08-28 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 395.1 |
| c515e99e-8797-348c-b43b-6333161b9adb | -7.2661 | -45.8443 | 2026-08-28 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| a20267f6-db6c-35f6-9d1f-9735984d1354 | -7.2474 | -45.846 | 2026-08-28 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 12abf005-3b6b-369c-a16a-8c5186b0d0a0 | -4.8583 | -45.3915 | 2026-08-28 02:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b3ba8ca3-24ba-3cac-8c6f-4db960312a6e | -14.1645 | -52.8269 | 2026-08-28 02:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 82f11d3b-cab8-337c-bf56-a04a58e4fee9 | -10.7596 | -54.0384 | 2026-08-28 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 12f8c1e4-16ee-3211-b8fd-09adf475c1a4 | -16.1641 | -58.5851 | 2026-08-28 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.6 |
| 898d0bfa-ff01-3772-a6c5-444419733165 | -12.4494 | -43.415 | 2026-08-28 02:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ef6f9923-6c69-354f-a68d-e378ab43ecf3 | -15.5403 | -41.9175 | 2026-08-28 02:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| e8aca3d8-4b54-3795-9cbe-1579063446ba | -10.3707 | -61.2513 | 2026-08-28 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 87ccde62-e8aa-3993-87e7-b9fa15b487a2 | -10.4981 | -64.5005 | 2026-08-28 02:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| dff4f33c-1a69-3ca0-921e-8621b65dcbba | -6.1657 | -57.7793 | 2026-08-28 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cae9b3ec-7e30-3306-a083-ffc14e62efa7 | -12.43 | -43.4182 | 2026-08-28 02:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 20c182e7-818b-3fca-8845-a83159853674 | -10.3894 | -61.2502 | 2026-08-28 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 203.7 |
| c176a9f0-d937-3d63-adbf-d0a7b63a2ce7 | -10.3895 | -61.231 | 2026-08-28 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 160.5 |
| d957c006-6f2c-30d6-9893-a0140178d79a | -11.2314 | -54.0164 | 2026-08-28 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ddf5f474-d132-385a-8540-b5e494d9558c | -16.1638 | -58.6053 | 2026-08-28 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 144.5 |
| 710cf37c-6991-34e4-b5a8-094bc3216669 | -10.4082 | -61.23 | 2026-08-28 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 5aa79918-52b2-301e-8b6c-2436c0cf40be | -12.4305 | -43.3944 | 2026-08-28 02:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 5f1c64d3-61fa-3cf2-85c6-0b77a3657209 | -6.1656 | -57.7988 | 2026-08-28 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| dd93b8fa-e66b-391d-882f-cfefbf790a0f | -4.8397 | -45.3926 | 2026-08-28 02:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1f96e32b-be3c-3fbf-8e58-026fd67df47a | -6.1472 | -57.7995 | 2026-08-28 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 54291412-d3d3-3b34-9465-3314683264ed | -8.5969 | -54.7755 | 2026-08-28 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 40b935c3-9b31-3605-87d9-9e223147d346 | -11.2317 | -53.9958 | 2026-08-28 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 21e979d4-63b1-3c33-967b-abc83fdbc2af | -16.1444 | -58.6073 | 2026-08-28 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 33fbc5b7-3e14-3f97-a72f-cf2484b5744c | -6.5323 | -55.2378 | 2026-08-28 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2430f526-09c5-3c2d-91e3-5157421f7e0d | -7.2471 | -45.8685 | 2026-08-28 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 277.9 |
| 130bb30a-4e9a-30f5-ac96-eebd70c7a6b0 | -16.1447 | -58.5871 | 2026-08-28 02:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 01eff906-264f-3abf-95df-6a37d1e8c68b | -10.3708 | -61.232 | 2026-08-28 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d61cb602-ec30-3799-85cf-6c982204672b | -10.4081 | -61.2492 | 2026-08-28 02:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| d204baff-b514-3f85-9c6b-6cf3a571f51e | -7.2659 | -45.8668 | 2026-08-28 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 303.3 |
| 3db32f56-ec02-3c54-a6b3-788fb464cdd9 | -12.43 | -43.4182 | 2026-08-28 02:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| d4d9b1d5-5b23-3b43-81a2-c8f2725a8f2f | -10.5168 | -64.4997 | 2026-08-28 02:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 80f60b44-fdf8-31c0-98b4-0d947d7cd375 | -6.1473 | -57.78 | 2026-08-28 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 31599b3d-d339-3c66-bd73-5439b64d5cfe | -16.1447 | -58.5871 | 2026-08-28 02:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 2cead6e0-769d-3a4b-9b31-2c55161765a6 | -11.2693 | -54.0129 | 2026-08-28 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |


[Clique aqui para ver as próximas entradas](README10.md)
