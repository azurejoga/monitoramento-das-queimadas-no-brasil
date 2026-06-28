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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ee355c7-dcb0-3ed9-9910-e7d9cd49e523 | -12.99268 | -57.7749 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0ecede3-b5d1-3caa-80bc-b8560e99129b | -12.98878 | -57.7743 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eee8428-d8fe-32e4-8841-28d896ec9cb0 | -11.90479 | -63.81297 | 2026-06-28 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86103f4d-cc5d-380c-8653-5dd70d085310 | -12.62092 | -57.89364 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1bbfdb7c-b8ac-3c5c-9f3b-73694bc736aa | -12.54519 | -57.1879 | 2026-06-28 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68cc3757-8d7a-3e1c-91ea-56ca8c42a50e | -12.60166 | -57.89072 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 932e47b4-3678-3a91-9c1c-6179874b73f1 | -15.92932 | -52.28149 | 2026-06-28 05:36:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40d50d0f-ebde-3d9a-a5dc-4724ec83e6fa | -15.44211 | -59.23503 | 2026-06-28 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7111f96-9cd1-3a16-80cb-f89e9707aab5 | -12.4507 | -58.48722 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8371e1c1-f866-390b-b1fa-9ee112170949 | -12.45506 | -58.4833 | 2026-06-28 05:36:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7a4b27b-8737-3b95-8499-fabe9c70c4ae | -16.19431 | -59.32832 | 2026-06-28 05:36:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67d69a60-10c9-3d9f-8195-152f6451b82a | -12.61531 | -57.87794 | 2026-06-28 05:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aefac7ce-ba47-315e-a76e-3e3e9b561c31 | -12.77409 | -59.00436 | 2026-06-28 05:36:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f94d3543-52a5-3b6b-b04b-e13bb51dae72 | -16.2167 | -59.65856 | 2026-06-28 05:36:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56d8205e-ae9d-3280-b45f-8444e827ad20 | -18.47036 | -54.10065 | 2026-06-28 05:36:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8afdf19-84dc-35a6-a41c-ecf625e93f06 | -12.16965 | -59.75514 | 2026-06-28 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8070287f-6995-387a-8c23-e43bb5399fb9 | -12.79199 | -54.88885 | 2026-06-28 05:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0106eff1-930a-3cff-8c38-a2a00f43f8a7 | -17.3504 | -42.62494 | 2026-06-28 05:38:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 30cda047-40e3-3d76-a773-57af1f870c55 | -17.34205 | -42.628 | 2026-06-28 05:38:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 2d299c65-58fc-3b99-aab3-d9772c3289c0 | -21.77398 | -56.28854 | 2026-06-28 05:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75030257-4765-35d8-b4e8-3b23277404d7 | -21.2713 | -56.03405 | 2026-06-28 05:38:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7268abb8-3729-37ec-a328-193effc897b9 | -11.209 | -54.3053 | 2026-06-28 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 4f302667-c260-39b2-af99-2ed6981eb736 | -12.1937 | -52.8866 | 2026-06-28 05:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 59761ccb-6b51-37b6-9565-9f3c9cee39bf | -12.194 | -52.8657 | 2026-06-28 05:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 20beecf9-f1a1-32c2-832d-a8cf3fd31618 | -11.209 | -54.3053 | 2026-06-28 05:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 31a53b4b-2960-3346-9126-444c410e308d | -12.194 | -52.8657 | 2026-06-28 05:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e657fbc5-708d-3f54-973e-28c0f8340e28 | -12.1937 | -52.8866 | 2026-06-28 05:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ca1b50d0-6986-30df-8ee9-482ac5b281b0 | -12.59653 | -57.87854 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 07e6a802-f4cf-3dda-b29b-d6042d982a15 | -11.94243 | -58.615 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75483754-7145-361b-9e32-6953f036afbb | -11.87175 | -57.81927 | 2026-06-28 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96c2cd12-4108-38cc-a95d-caaa921f9fda | -11.90932 | -57.13549 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e87a6973-788b-3b31-9158-5fb5a53e1bf4 | -11.91928 | -58.66061 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46eaf7b7-32f2-3d50-8acb-c7d39b536d3d | -12.4549 | -58.50281 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 719029b1-7617-3788-bd84-3d039d34a69f | -12.60086 | -57.89161 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59a5f8b1-fe57-314d-9ad2-624d2e9c9e7d | -12.16598 | -57.13493 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01193ff6-f277-39a5-bfd8-9a694d145555 | -12.62402 | -57.89465 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dbd8bb6-d06f-3504-9fcb-5ec68e51a292 | -11.66365 | -57.2588 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 35bbe514-f109-3229-a294-dfe962cf4c6e | -12.17147 | -57.14032 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc59f391-0e3e-3438-95ae-18b743a1cf37 | -11.92076 | -58.65654 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91580018-b73b-36e3-a7bb-46a68cff1a92 | -12.46135 | -58.49632 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 95c5ec19-e70a-338a-849e-79902feac68a | -12.23392 | -56.55443 | 2026-06-28 05:53:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d0de1c1-b49f-3519-8ed7-6e2fef57f7dc | -12.16544 | -57.13946 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75ff02c-15c6-35d6-bd1f-1643b929d718 | -12.60232 | -57.8793 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 952000aa-31ce-3d9b-b9ca-248a5136d0a0 | -11.92478 | -58.66106 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f046e7f-c56d-3050-bbbe-0671d802b0b4 | -12.17696 | -57.14579 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 054c7d57-d420-3f40-9d81-0e6f5cc29c44 | -12.17642 | -57.15033 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9ced679-e444-3256-bad0-e35fbd192663 | -12.18191 | -57.15568 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc1e64e9-b255-3d8f-82df-279a1d7962f2 | -12.22766 | -56.55353 | 2026-06-28 05:53:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baa44cc7-0657-37bc-870f-b37085051942 | -12.17039 | -57.14942 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1b0645e-bb5f-3eb7-ae31-443f1119f959 | -12.79261 | -54.88209 | 2026-06-28 05:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3fadc969-c0b5-3b5b-849b-55a854b8a61a | -11.87804 | -57.8157 | 2026-06-28 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e89422ba-c8e7-3740-8e46-d3648dbb6a3c | -12.17308 | -57.12674 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 995d11b1-810b-3cd0-aaaa-bd710730fa5e | -11.92495 | -58.66785 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 946fc4b8-4482-3794-9c1c-1add2f75c8f4 | -11.94173 | -58.61542 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b27bcf24-9e0e-3dbd-9878-a0f8048bb699 | -12.59604 | -57.88265 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fc8d4b01-0a17-326d-85a7-9985df7ff68c | -12.77511 | -59.00344 | 2026-06-28 05:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 111dbf27-2095-3eca-9d4e-2f6c2deaa1e6 | -12.44557 | -58.4869 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2e0b2dd-5c2c-3ffa-aef5-0d8cb2f94e76 | -12.76972 | -59.00271 | 2026-06-28 05:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95501472-6424-33af-9835-d41cb3c4b9c3 | -12.18137 | -57.16018 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acc608ef-22d1-353e-854b-db69e24ff8ec | -12.16985 | -57.15398 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd21493a-d441-3dbd-834b-057dc18fe953 | -12.45535 | -58.4992 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d039801-0c79-3315-b01d-4ffdd5b704a1 | -12.17588 | -57.15486 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ec8d770-7f59-3223-967a-859921342fac | -11.87327 | -57.80681 | 2026-06-28 05:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3788e147-6452-3450-9d96-1a7eccd97b98 | -12.79347 | -54.88561 | 2026-06-28 05:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0e0fc854-0a30-38ea-8c94-338239e0266b | -12.4558 | -58.49559 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0cb5430c-b17e-3f02-833d-8e5103c3a099 | -11.92032 | -58.66018 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d9992ba-1b1f-3fa4-bb3b-544633b026d5 | -11.9234 | -58.67184 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d773cc5c-1652-3da9-a193-8222f45fe6d5 | -12.79193 | -54.88851 | 2026-06-28 05:53:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d04dd624-8f33-3383-a979-22a9ec5a52f6 | -11.66041 | -57.26052 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e7b0749-ca2e-33cd-b81f-81e26366f4b9 | -12.98498 | -57.77928 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6453824e-0314-3822-8e16-a4233a5fa578 | -11.66311 | -57.26321 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e249a58d-5b72-31c8-91de-f9d061f32329 | -11.9212 | -58.65287 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 442b225c-3fbb-3903-9d3d-ac1686d539e0 | -11.90147 | -57.11353 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a83b67b0-53fa-3aad-b4c6-3496797f66dc | -11.93739 | -58.61058 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 370e8039-af17-35ce-a22d-7e52518a1b76 | -12.98547 | -57.77493 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2d54541-6685-3fcf-9f78-175192a58cd6 | -11.91975 | -58.65698 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff136f44-d8a5-3ff8-8d25-de4406b7cd4c | -12.17254 | -57.13131 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97c303c2-850b-3828-aff6-f2c50dc181be | -12.16705 | -57.12587 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99179f1f-7ade-3c07-b1b5-659ef3a76ed4 | -12.59556 | -57.88673 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eccf098d-dcce-3f31-8610-d03a133ea434 | -12.98646 | -57.77393 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b95ad472-f2e6-3c2b-8afa-5010977ba5d0 | -12.44603 | -58.48312 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b2cf39d-a5e2-3c0b-9a44-9bdd2f89d36d | -11.92524 | -58.65744 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ed05bce-6595-3ba7-a99a-cec6d8e99298 | -12.61341 | -57.885 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e873dc3-a121-328c-9ec2-7f9a62aac99f | -12.4669 | -58.49709 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9389bdf8-4428-328a-8b31-5af954952e2d | -11.92669 | -58.65337 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf2f8b9d-2d83-3ac6-8898-aea4cbe286af | -12.16651 | -57.13044 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2538e528-39fe-3297-b1d2-b794512e2eff | -11.91518 | -57.40989 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cae02f0d-b85f-315c-92a7-eba97aefa2f1 | -11.66092 | -57.25609 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0960687f-671a-3e70-9dc3-17c212b89486 | -12.76929 | -59.00623 | 2026-06-28 05:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c0a37c-98d9-31ed-85bb-a4ee42c5d960 | -12.46225 | -58.48905 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d83a958-a1c8-3ab5-9d81-19cd02d0f701 | -12.46045 | -58.50357 | 2026-06-28 05:53:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dda742e3-6a93-328e-b33e-15d643791444 | -12.77469 | -59.00694 | 2026-06-28 05:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5319f6b-9e6c-3160-b510-2f2139a66077 | -12.17201 | -57.13578 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6072bc66-7bf5-3f6b-8083-65dce39f7787 | -12.6187 | -57.88992 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90349147-e046-307a-835d-4dd76eed0633 | -12.18244 | -57.15117 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 273087a7-544c-3e8c-abb7-3c6ecd37199d | -12.99133 | -57.77575 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ad968b9-42a4-39aa-9c8b-f347f1428f06 | -11.90987 | -57.13098 | 2026-06-28 05:53:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b54ee77-579b-30d3-89e5-9e5216d03a53 | -12.61243 | -57.8932 | 2026-06-28 05:53:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 555fb54b-6915-3172-9670-aeba1420ddea | -11.92386 | -58.66824 | 2026-06-28 05:53:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76fe70d7-faac-32f5-84e4-ed2b717a3e9a | -11.9157 | -57.40557 | 2026-06-28 05:53:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
