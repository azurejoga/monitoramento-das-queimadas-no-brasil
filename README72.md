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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9758bf0-adec-31b9-b5d3-28f803e41f9e | -6.9884 | -59.0457 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 207.6 |
| 620806ff-7dfb-3cdc-b67e-d82afa026662 | -9.7908 | -47.223 | 2026-08-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 701af9c3-b968-320c-b83a-c2da55046994 | -7.6053 | -45.7238 | 2026-08-17 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| ed1b6ced-2c4d-329c-b78f-c47d85e3c5f6 | -6.2378 | -47.7406 | 2026-08-17 14:20:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8ad353d5-6a3c-3f4f-aa40-ce2234c56058 | -9.1998 | -60.793 | 2026-08-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 178.0 |
| dfeec19a-8c2a-3b42-b77f-6d2a9658e6e6 | -14.2758 | -53.0866 | 2026-08-17 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 53044938-a59e-3501-ae30-3eabfec8148e | -6.7832 | -59.4401 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 43cc2e69-49cd-3b78-aa9f-0d366e017932 | -14.4871 | -51.9806 | 2026-08-17 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 90540b35-824c-3f90-bcb0-5ca3df23411e | -5.5074 | -43.6576 | 2026-08-17 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| a926feea-aae2-34fa-b8b1-baf1970d8909 | -5.5072 | -43.6808 | 2026-08-17 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 8fb8277c-2074-3324-9dee-342a2c4035d4 | -13.4123 | -54.3324 | 2026-08-17 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 523.0 |
| 849ee6cc-fd8a-335c-8d74-6f20672ff351 | -9.7553 | -45.7237 | 2026-08-17 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7975dc1c-4516-3067-b6f0-25c22cd685e2 | -8.9601 | -60.5165 | 2026-08-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5bfff0f5-beed-3fbc-9972-d909bd6b38ab | -12.5392 | -47.9 | 2026-08-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 259e304e-e347-3c1f-9133-54f983e40430 | -7.4074 | -60.0108 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 90361332-3522-3890-80ad-b2ea45674b98 | -11.1299 | -46.5019 | 2026-08-17 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7d36edc0-9634-3060-b7e9-7fa70f4cf339 | -11.4907 | -46.5892 | 2026-08-17 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 64cc75df-5059-38d4-b9df-83b6cb7e3341 | -6.2376 | -47.7624 | 2026-08-17 14:20:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a6680011-eed9-3185-9cd9-006bc79a2eb8 | -17.3369 | -54.9315 | 2026-08-17 14:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 509e7cdf-a88a-3e3f-b233-8ef36895acd7 | -8.5212 | -54.9016 | 2026-08-17 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| e3f144ed-71e7-3923-b798-b7d93a58934f | -13.5128 | -46.2219 | 2026-08-17 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e99b16c5-841a-388a-899d-dac3c67ab4f9 | -11.5099 | -46.5866 | 2026-08-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5cc07f61-3d63-3bad-a9ee-6631f6993c8b | -13.5124 | -46.2449 | 2026-08-17 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8999688d-10ac-3884-a39d-1c378752610d | -13.2805 | -51.6886 | 2026-08-17 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 225.7 |
| fa7d5ad1-5fbe-39f8-b694-37779da46db7 | -11.4907 | -46.5892 | 2026-08-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 704f2ab2-c65f-3050-913e-1dd7cb39f146 | -7.3824 | -55.4924 | 2026-08-17 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ac9ac71c-7ae5-3a8a-877a-04eeb7d393c2 | -14.4871 | -51.9806 | 2026-08-17 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| d0359579-6563-3e7f-852d-74d594c6373c | -6.6015 | -58.9651 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 60f410a6-ded6-3416-b0c3-fac065c40f38 | -10.9322 | -57.1511 | 2026-08-17 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 3c04958c-bfe8-3eb7-9737-aa9bdf479067 | -6.9886 | -59.0264 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 18abeafc-981e-35b4-80c1-9639adfad2fa | -6.2565 | -47.7393 | 2026-08-17 14:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 547c2bb6-881d-302f-ae5d-3e2a8054e0c3 | -15.2839 | -52.8934 | 2026-08-17 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 368ddb55-cf07-349a-afc6-0c29c1e899a7 | -7.8071 | -47.8372 | 2026-08-17 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 9934b55e-2e29-3aee-b00c-5c85cf3a8a31 | -6.7123 | -58.9412 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7be8cf20-5ca9-32d5-87e7-5e18dda65e6f | -6.97 | -59.0465 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c84e70c7-5d79-38d5-af1c-f59390b85262 | -9.3382 | -62.3344 | 2026-08-17 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 271fc5c4-9ce8-320a-b1cc-12737cd2cd1f | -6.6384 | -58.9636 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 44779c80-a2f3-3bbd-ab34-5891cb2fd7ee | -11.4716 | -46.5918 | 2026-08-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 96e55375-64b8-3100-ad77-c70a45ba6559 | -14.4101 | -51.9696 | 2026-08-17 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 65947483-17e2-3ccb-a796-bacea6e51214 | -6.7647 | -59.4601 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 359.0 |
| db6e751e-bde4-394b-a789-ff941332bfc2 | -15.4384 | -52.9361 | 2026-08-17 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8cde8ab5-2929-3487-9f28-c42a92ef4150 | -7.6053 | -45.7238 | 2026-08-17 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 0bb11870-4252-3420-8fbc-e19842294bc5 | -11.5095 | -46.6092 | 2026-08-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 295.1 |
| e30b713a-f3c5-3415-b5b8-c08434865833 | -6.2378 | -47.7406 | 2026-08-17 14:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 3df8a47d-485b-3353-bbfb-f0bbc120f90b | -9.1996 | -60.8122 | 2026-08-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 1d64d0a4-cdb0-3321-9b77-092170ac24e9 | -8.9601 | -60.5165 | 2026-08-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| bbb2351a-7a60-348a-a97f-cc34ffe6af66 | -11.472 | -46.5692 | 2026-08-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 1fa08ad7-c893-3002-a307-140ad8f37a65 | -6.9701 | -59.0272 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 27ed335e-aec1-3c96-acb5-3303d9c0d0b1 | -6.6199 | -58.9643 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 3c51322b-09b4-30e3-b96b-8e3ee0e38d99 | -6.2376 | -47.7624 | 2026-08-17 14:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| aaa03a4d-6107-3cf4-9d46-8439a830d337 | -12.1392 | -50.1388 | 2026-08-17 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 819dda7d-1f4e-371e-af5b-c654cbef3014 | -6.6568 | -58.9628 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0f5ba9c6-3b34-397f-8069-ba430016c3be | -6.2192 | -47.7419 | 2026-08-17 14:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c54ca5b9-e710-3c66-8302-d8b153b6578f | -10.951 | -57.1497 | 2026-08-17 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 173.5 |
| 8d2a3f63-79f3-3318-99ca-b289a6f3e989 | -7.7881 | -47.8607 | 2026-08-17 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 7b3a4136-0724-32f6-93e0-303405bd7762 | -6.2563 | -47.7611 | 2026-08-17 14:30:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 103e40a8-ea70-30c4-90cc-60475a2efc7b | -9.127 | -46.0214 | 2026-08-17 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ee421eeb-4a62-303b-8692-c6812fd969c1 | -12.5396 | -47.8777 | 2026-08-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| acafb4ff-4b02-3812-8664-23d51bcceb43 | -22.0767 | -55.9708 | 2026-08-17 14:30:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 5a9b26b4-a02a-3246-9b94-c52ed3e2db62 | -7.3639 | -55.4935 | 2026-08-17 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| dd30a86b-1ed0-3f26-b20c-ccdef972660f | -9.3196 | -62.3353 | 2026-08-17 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 14c952e3-accb-3cff-a908-81736bb4d9d4 | -12.5392 | -47.9 | 2026-08-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 0e03af30-ac28-3483-8040-6dcca483839c | -11.4904 | -46.6118 | 2026-08-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 197.5 |
| cfb24220-a1ef-3404-b028-51266dd5dc51 | -14.2947 | -53.1052 | 2026-08-17 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e44dfef8-594a-39b0-88d8-a4a4cf00e675 | -11.7351 | -54.5636 | 2026-08-17 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4dfdb29a-1968-3d94-a88b-2d9dc0768143 | -6.6198 | -58.9836 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ff733417-159c-3622-ab4c-f2ed00e7394f | -10.9508 | -57.1696 | 2026-08-17 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d99f7b0f-09c8-3c3d-8987-1cbf7a957ecb | -9.7908 | -47.223 | 2026-08-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b6f707c1-2b6a-31a6-a257-11743b87c4bd | -11.3239 | -46.2955 | 2026-08-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 22dad479-afc8-3f30-959d-fdf6b1a53481 | -9.1998 | -60.793 | 2026-08-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 290.0 |
| 9bf9686e-7377-37d9-b9fc-f3dce89b1a14 | -12.5588 | -47.875 | 2026-08-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| be78ac26-0c48-3181-a8d8-7d313166783e | -8.0834 | -61.3603 | 2026-08-17 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6b4f6905-0fbe-3047-b5e1-abd95dae02a8 | -8.5211 | -54.9217 | 2026-08-17 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 50ad57b2-af03-38f7-bb44-8b1313bc676d | -11.3235 | -46.3182 | 2026-08-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 678.1 |
| 681b2ae3-5bbb-3398-8ddd-54bba95fc8f9 | -11.1159 | -49.9138 | 2026-08-17 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 1444240f-e75c-3194-8b42-02b81b875eda | -12.7009 | -48.5195 | 2026-08-17 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| d0a9192f-a884-385f-ac27-cd2ff2dbf88f | -11.7159 | -54.5858 | 2026-08-17 14:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| b5cd8ea0-20be-3222-9d1f-40e74dff75e1 | -14.5247 | -52.0395 | 2026-08-17 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a9d7e6db-b312-30fc-868a-079377b34d8f | -13.7836 | -53.835 | 2026-08-17 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d89db509-eac3-33c6-9513-88e06fbe405e | -8.5212 | -54.9016 | 2026-08-17 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| ec0be0c5-8f2f-39db-8e9b-43b68e6ec86f | -7.8068 | -47.8591 | 2026-08-17 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| e4921c74-61b9-336c-85e4-29543d315d2d | -6.6014 | -58.9844 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 211051e0-aa23-3edd-894a-692f98d77730 | -11.7349 | -54.5841 | 2026-08-17 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 75755e5a-ebda-3276-92b5-3d49c971f61f | -14.3878 | -53.3037 | 2026-08-17 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4c365419-d9ef-3685-b110-68536933b5f0 | -5.5074 | -43.6576 | 2026-08-17 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e11bcbd5-8e2c-343b-b5da-e40eda269141 | -10.5085 | -50.0228 | 2026-08-17 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 237.7 |
| c555c95e-01c6-35c1-9014-9e6ddef9ccc2 | -6.7831 | -59.4594 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 172.3 |
| aadab6a1-b6ae-380b-b5b6-a3adeab840de | -9.1706 | -59.6762 | 2026-08-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c1f7f982-ac03-3161-a6c9-0b3c7d9faa5e | -9.2184 | -60.7921 | 2026-08-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 154adb2c-9ac0-3b25-a5aa-eb2625bf0522 | -15.2645 | -52.896 | 2026-08-17 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7c21b546-3643-359e-bd8c-6c33684dece0 | -9.7905 | -47.2452 | 2026-08-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| a0c0f4ec-2f26-34a4-844e-6cc7e036203a | -2.1729 | -54.4265 | 2026-08-17 14:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 201.3 |
| 7ed82a09-2afc-3bc3-8af9-4615c48f02ea | -9.7719 | -47.2251 | 2026-08-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 711dda2c-9e8f-33b9-b32e-bd233430316d | -10.5275 | -50.0208 | 2026-08-17 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 2489a230-25ed-3642-8cd4-98c791e9fe83 | -14.2758 | -53.0866 | 2026-08-17 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 658afea4-32e8-3022-a9f8-087ee6cff028 | -6.9884 | -59.0457 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 317.3 |
| 23f3ceb5-2d6d-3572-ab8e-0fb1a776f1bc | -15.4579 | -52.9334 | 2026-08-17 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a10db464-0f7d-3bf6-9fc0-ed3f6e962752 | -13.4123 | -54.3324 | 2026-08-17 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 674.8 |
| 986e00b4-158c-36f3-af49-ea583d6743ea | -8.96 | -60.5358 | 2026-08-17 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 84d9a9a8-8896-3bc9-a183-3576b0fbcaea | -6.8573 | -56.4137 | 2026-08-17 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |


[Clique aqui para ver as próximas entradas](README73.md)
