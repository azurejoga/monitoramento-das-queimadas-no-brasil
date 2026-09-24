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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d1f035d-2195-3d31-8fa3-72d9b7e08236 | -11.2284 | -51.3515 | 2026-09-24 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 098e9113-d4d2-38e4-86d8-41769a32d77a | -6.6146 | -59.9272 | 2026-09-24 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| d301fc05-778a-3876-8bce-08a684ed5744 | -10.0921 | -46.0232 | 2026-09-24 02:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.1 |
| de1ef8a1-7892-3122-902f-37e0fcb59700 | -5.0062 | -45.5626 | 2026-09-24 02:50:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 400.9 |
| 246a1e4c-17bc-344d-a2be-f9624c2161dd | -10.0917 | -46.0458 | 2026-09-24 02:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 03b8b233-174f-34ea-b0eb-ec210256e7f0 | -12.0099 | -52.4465 | 2026-09-24 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 96162ab7-1516-3ddc-b6e0-d34a7720e302 | -6.6145 | -59.9464 | 2026-09-24 02:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 08a3cc79-4c09-33ba-b70e-0c4b19f4eec3 | -5.7754 | -45.1053 | 2026-09-24 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 48169095-f238-3369-afe3-67af71d8956a | -11.9906 | -52.4695 | 2026-09-24 02:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d89e317e-8e34-3902-9e3e-1d20b6f91fd2 | -4.9876 | -45.5637 | 2026-09-24 02:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 606.9 |
| c0fe3127-f784-3a1b-9c9b-d23cae5605ce | -3.4578 | -50.0679 | 2026-09-24 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2d89408e-e713-3eab-8cfa-3401217af841 | -3.4578 | -50.0679 | 2026-09-24 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 28afca3c-00f7-3608-b396-3819e2dcd2f6 | -3.6947 | -60.5455 | 2026-09-24 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 0af8d78d-4541-32fa-ae75-182128fe63bf | -3.4393 | -50.0685 | 2026-09-24 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0e85a790-6994-3377-9bd9-aa192b4c4272 | -5.7754 | -45.1053 | 2026-09-24 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 3933a4f8-1236-3494-8da6-1c21b24b83fd | -10.1098 | -50.1921 | 2026-09-24 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| dbc2a904-237a-3edd-ab6f-81e78036e0dd | -3.6763 | -60.5839 | 2026-09-24 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| a7d286eb-8fd6-3c8d-bf4f-c4dbda0ec08a | -3.4392 | -50.0896 | 2026-09-24 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d8b0c32f-0d8e-375c-920b-72ec65c437e6 | -11.2281 | -51.3727 | 2026-09-24 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 55620ee0-96d2-39bc-be4c-b1246111ec46 | -6.4487 | -59.9526 | 2026-09-24 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c30dc7f0-05ab-3ac9-b3fd-9f909576fe3f | -10.0731 | -46.0254 | 2026-09-24 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 193181d5-5503-3e9a-834f-5c8eb0d4bc40 | -10.0734 | -46.0028 | 2026-09-24 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 8c61a0da-ac89-3f28-95ba-5d02d9787eab | -3.4577 | -50.089 | 2026-09-24 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 089c77ce-092d-386b-b863-20a2742aaa82 | -4.9877 | -45.5412 | 2026-09-24 03:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 428.4 |
| 53cf3367-8a97-3fe1-a6ac-2f9b5bbdbcdb | -3.6947 | -60.5645 | 2026-09-24 03:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 326492d2-3e73-30e7-a635-0cf1cc5a1dfd | -10.0921 | -46.0232 | 2026-09-24 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| b658dca5-4bbd-340a-802e-54315ba6fe9c | -4.9876 | -45.5637 | 2026-09-24 03:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 368.2 |
| df0c5100-30e5-3e67-b294-9ac263c12067 | -1.8421 | -54.7113 | 2026-09-24 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| ea1505c1-6f25-36b9-a3b9-5219a2c6587c | -1.842 | -54.7313 | 2026-09-24 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f13a07d9-0f0f-364e-bf5d-b36a3a0da20d | -5.0062 | -45.5626 | 2026-09-24 03:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 0673c8da-ba1c-3d5a-adfc-dafdff5ba1bf | -6.6146 | -59.9272 | 2026-09-24 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| f4ac52cb-314d-3ec1-aa3c-f74fc2f072c8 | -10.1286 | -50.1902 | 2026-09-24 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 9607bb71-e70f-3849-90f9-2c30d24f2454 | -10.0924 | -46.0005 | 2026-09-24 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 0b4a532e-f8cb-352b-95e1-a628a12dcc66 | -6.6331 | -59.9265 | 2026-09-24 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 35c1f59b-e266-3f4e-ba34-95d7b78cd911 | -10.1095 | -50.2135 | 2026-09-24 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 87b9b86d-431f-3c22-9808-865c131669e0 | -2.6493 | -54.6971 | 2026-09-24 03:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 550bf41c-f624-39b4-b60b-d5eb018a3c91 | -5.0064 | -45.5401 | 2026-09-24 03:00:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 4ea8f785-5dc6-3de3-b3fc-e88d124f09c6 | -11.93685 | -38.295 | 2026-09-24 03:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ddc57b67-24d5-3880-99c3-19b80863f506 | -11.9437 | -38.29874 | 2026-09-24 03:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9a1066f6-7bfb-3570-a9b8-b2a2d171b3fe | -11.92934 | -38.29486 | 2026-09-24 03:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 214f98ba-6169-35d5-9807-43830e63d157 | -11.93656 | -38.2966 | 2026-09-24 03:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| db86731c-958f-31ba-8ed9-cab593f94e1c | -11.92963 | -38.29325 | 2026-09-24 03:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3a1d0316-84ac-3d7f-aa70-904fccad027b | -3.4578 | -50.0679 | 2026-09-24 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 17338a74-ef9f-3ee9-9192-4b16127191b7 | -10.0917 | -46.0458 | 2026-09-24 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| a6f33d0b-6904-304e-bda6-f92245036594 | -1.8421 | -54.7113 | 2026-09-24 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 2667f7ca-da0a-3455-9af7-50eca71db9c8 | -6.3501 | -57.7717 | 2026-09-24 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 49852afd-c006-3f3e-99fe-a01345142fc8 | -1.842 | -54.7313 | 2026-09-24 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| baafaaa2-8a39-3156-9994-8dceb5730106 | -4.9877 | -45.5412 | 2026-09-24 03:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 280.6 |
| fae1da15-811d-3b9d-b16b-0ffe7fd00747 | -3.4577 | -50.089 | 2026-09-24 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| e40e6b9f-b708-34ac-856d-29fe6a69537a | -10.0734 | -46.0028 | 2026-09-24 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| db146503-d0b7-3c7f-849f-05006d79a0c8 | -5.0062 | -45.5626 | 2026-09-24 03:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 792ed086-7fc2-3406-9987-dacb57c7a865 | -5.7754 | -45.1053 | 2026-09-24 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 7b110a17-515c-3f08-82b7-e6d68cbfda1e | -6.6775 | -58.5748 | 2026-09-24 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| a10b05e8-1798-3330-85d6-b6abb95c8560 | -10.0921 | -46.0232 | 2026-09-24 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| a826e06f-d3ac-3fe5-acb8-2a3f9090386b | -6.6331 | -59.9265 | 2026-09-24 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 3298fefb-eaf3-3bb2-9697-1a6b50c887ae | -10.1095 | -50.2135 | 2026-09-24 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 7a77cfc4-cbc4-3d39-93ab-e8c48b695325 | -6.4487 | -59.9526 | 2026-09-24 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 67222c27-22a4-3dfb-9043-cbbeea038ac2 | -3.6947 | -60.5455 | 2026-09-24 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 2ca160ea-19ce-3fb7-ab47-533b28afd704 | -12.1491 | -50.7384 | 2026-09-24 03:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 58955436-935c-3ebd-bc4b-c771955d3f51 | -6.6145 | -59.9464 | 2026-09-24 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d93f4985-5181-35d8-a969-f39a6a6b9f23 | -12.1487 | -50.7598 | 2026-09-24 03:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d2cc5e0b-649f-31b8-9166-29cc527d42de | -10.1098 | -50.1921 | 2026-09-24 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2c5d235b-fd53-3af6-90bb-92ec0a5a8389 | -3.6947 | -60.5645 | 2026-09-24 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| a02d63f2-13bd-33c3-a314-31806d8b3ca7 | -3.4392 | -50.0896 | 2026-09-24 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ea8f3ea7-2de7-3ecf-b5dc-4d853bd60175 | -10.0731 | -46.0254 | 2026-09-24 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| bf841e14-8a52-349a-b000-1600f846c2ca | -3.6764 | -60.5649 | 2026-09-24 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 66ed8919-e389-3150-825f-87b502ec8898 | -10.0924 | -46.0005 | 2026-09-24 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 4515e9d3-35d8-32c2-ad37-bb2f400c1c2a | -12.0096 | -52.4675 | 2026-09-24 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 32d2aee8-c889-3c13-b811-cec64d9eff19 | -4.9876 | -45.5637 | 2026-09-24 03:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 176.0 |
| b845bdae-f1d7-310d-a438-6faae8a1c042 | -3.6763 | -60.5839 | 2026-09-24 03:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 3a1d47af-2e30-3c0f-b0b9-b38d6c8189e1 | -2.6493 | -54.6971 | 2026-09-24 03:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cd6b3882-378a-3516-b056-be3c01f806b7 | -5.0064 | -45.5401 | 2026-09-24 03:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 9515586e-badc-3e7d-b0fb-d5acd0ef78d9 | -9.8677 | -48.5126 | 2026-09-24 03:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7176b733-24a9-365e-a053-c5a6c8a9e3dc | -6.6146 | -59.9272 | 2026-09-24 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| be094ff8-b0f4-3123-8de4-246ed161aed0 | -11.9906 | -52.4695 | 2026-09-24 03:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 03e011b7-54bf-31f9-9a5d-fe8ca8254cf6 | -2.7151 | -57.5109 | 2026-09-24 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6f2d1818-3a54-31ec-b10f-d42711d8d0b7 | -5.01 | -45.57 | 2026-09-24 03:15:00 | MSG-03 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a470aa5-cd6a-3ddb-8420-f549e05e2851 | -4.98 | -45.52 | 2026-09-24 03:15:00 | MSG-03 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7740921-ac61-32c8-bc07-1b70b0ab15d8 | -4.98 | -45.56 | 2026-09-24 03:15:00 | MSG-03 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a255b36c-a00c-3eed-b7fd-8d1d809bd401 | -10.0917 | -46.0458 | 2026-09-24 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 1b5bcede-c04f-369a-9a49-d5d280484604 | -5.7754 | -45.1053 | 2026-09-24 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2ef23217-ed11-3565-bb28-610f6630f915 | -10.0731 | -46.0254 | 2026-09-24 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 2cdf3ba4-6936-30c7-8189-4b86622c32e5 | -10.1098 | -50.1921 | 2026-09-24 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 289929c6-5464-3f75-92b4-919459b48fe8 | -2.6493 | -54.6971 | 2026-09-24 03:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 85c8398f-ee27-3e25-843c-129840a699fa | -10.0909 | -50.194 | 2026-09-24 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2d5318af-5f29-3722-91ec-e760974fcf70 | -11.4015 | -47.3851 | 2026-09-24 03:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e1cddd77-9af4-3458-8b04-0876c9b3b6ef | -3.4577 | -50.089 | 2026-09-24 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 272ae62e-ef94-3cf8-8fe1-3fd904d6f8f5 | -10.0921 | -46.0232 | 2026-09-24 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 308023d6-7bf0-3250-868a-f9e26c35f1a0 | -1.8421 | -54.7113 | 2026-09-24 03:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ec0cecd0-2961-317d-ba44-f680fcd2435c | -10.1286 | -50.1902 | 2026-09-24 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d8fb7257-d093-3e8a-8da7-f159f0e232b7 | -4.9876 | -45.5637 | 2026-09-24 03:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 1f57b259-b0f1-300f-a947-ba9ec3f19b56 | -10.0924 | -46.0005 | 2026-09-24 03:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| e8c26674-c9fb-39d8-b033-cca41d5eca35 | -6.6145 | -59.9464 | 2026-09-24 03:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 2a3ae042-b4e0-3346-b603-a7d651acae86 | -10.0906 | -50.2154 | 2026-09-24 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 3c9eddbb-7365-3722-a450-c373b11c5617 | -6.4487 | -59.9526 | 2026-09-24 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 47991dbb-1123-3dc3-b133-645c9ecd671c | -10.1095 | -50.2135 | 2026-09-24 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7fc33289-daa5-37f1-85c0-98b1ff9c98dd | -12.0099 | -52.4465 | 2026-09-24 03:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 2fd76df9-53ec-3354-b1d7-3afbed156f77 | -1.842 | -54.7313 | 2026-09-24 03:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 320f6643-7e50-386b-aba5-6abca6971cbe | -6.6146 | -59.9272 | 2026-09-24 03:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| f52e9518-297d-372d-a08b-be962ec597a6 | -5.0062 | -45.5626 | 2026-09-24 03:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |


[Clique aqui para ver as próximas entradas](README27.md)
