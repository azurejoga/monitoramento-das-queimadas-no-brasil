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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 669bdfc0-1fd7-3a4a-96d3-620dafc3bc89 | -5.54027 | -51.44115 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99413feb-a4ee-3434-93bc-d070bf9b7513 | -12.28011 | -49.20825 | 2025-10-05 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 445a7ae6-c622-3407-894f-ac140b8df23f | -10.35567 | -48.15808 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 38c011eb-a371-3669-a2d9-42b6c64f8500 | -13.27397 | -47.61921 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| baf7f8b1-a1d7-3e8c-b058-92d5bcee4d27 | -7.25318 | -45.32559 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6ff2a36-4ae0-343b-9d53-2dcb62f1d5f5 | -13.30104 | -48.09771 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6cba267f-44b0-3a90-bd87-bebd66eb6299 | -7.0358 | -42.80388 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c357ba25-1005-33fa-803e-3cefb6f881ad | -13.26623 | -47.82502 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d578d587-bcf2-3df8-a7b9-3013a7f97b9b | -7.78365 | -49.83478 | 2025-10-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8b5092c-4b06-3e0a-8521-8a2f16378899 | -13.2695 | -47.62207 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4f91ea2-bb12-3f1e-9cca-89cbf8c0334b | -13.08441 | -47.89476 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 196d99c0-5faa-3a60-9577-d6a01b0b8ab3 | -11.79701 | -46.84354 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47cea7b8-b6de-3a0b-89a2-69bc7d595656 | -7.45875 | -47.1756 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b678717-57c5-3bd0-a9d5-2acffe855385 | -8.86967 | -49.29137 | 2025-10-05 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49ac809d-a442-35e2-b38f-3d965d24cada | -13.14272 | -47.96527 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf1fed3f-3a07-3feb-b869-28f36b782a8e | -11.67995 | -47.48131 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c3a0d656-5da3-3c63-ae5c-8fe2712ddd90 | -10.57028 | -48.71862 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 148080f5-f7bd-31e2-8ff0-2a1a45e7b398 | -13.44948 | -47.27088 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db5b38e7-1b3b-350a-abfc-0a7a1abdea16 | -9.15424 | -59.53866 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ece47205-697b-3ecf-8142-99196831012e | -10.2085 | -48.93789 | 2025-10-05 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11edd1b2-ccc9-3155-a6b3-90f7c5d13abc | -13.09455 | -47.85122 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a9761a75-5d1e-3292-ac22-219c5a074df5 | -12.8242 | -46.85257 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c10a8949-b770-3f36-9b0c-08581bb9fcfb | -12.39038 | -51.09737 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdd09e24-befa-3734-aa16-7cc6549c09f0 | -6.98971 | -47.47415 | 2025-10-05 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2067f091-9dbd-3511-8f35-1b38eb915169 | -12.40715 | -51.10001 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1d30f5a-38d0-3465-921e-f9fdc333ca56 | -12.19622 | -47.77255 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e55502f7-162d-3369-8a61-b26f3faf208a | -11.67132 | -43.90236 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1de5b662-62e9-3cc7-a14a-d2879dbac3f6 | -11.5433 | -47.6864 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef2807b1-cb76-35e2-9ff5-629baac962d1 | -13.30239 | -48.08772 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a82f288-d352-3eeb-af0c-21c66cf77961 | -9.29618 | -46.00236 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65ba8cd6-8e5d-36e3-9803-39b1ef0c07ad | -11.91314 | -46.24012 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4741337-51f4-37a3-abae-5918fc0b6a0a | -13.3169 | -47.17365 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a034a3df-9cb0-3993-abbb-75d6f66cc7ca | -10.50638 | -51.8479 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0e424b6-3046-3c17-89ac-f44968d43e6b | -12.27408 | -55.12796 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5d5814-2735-3f80-99ee-f97f80c1eac3 | -9.06083 | -47.01706 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ddc6fd8-47fc-39d9-b0d9-2f2691ae25ac | -13.14922 | -47.97581 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2d4363c-d922-35b0-80b8-a58a5462e538 | -11.11612 | -47.13479 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20bde76d-fc61-3bc0-b0a9-34016e778339 | -13.64948 | -47.29519 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4118cc0-eb85-3f5d-b29c-a06ed5c6b72c | -12.31785 | -55.13028 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5965e25f-e6c4-3195-bfb3-5abab0e21145 | -13.2518 | -47.81274 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b64683db-9305-362b-9fbf-f2b11dd6d2fa | -13.08864 | -47.92324 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a32d3b41-baf3-316e-bc6b-0cbe8fa1ee9f | -12.61571 | -48.11965 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3fdc5cd1-6f92-398e-a02d-8a6933423720 | -11.46584 | -51.5169 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fcaad78-340f-396b-bbae-0e0e527b2364 | -11.76224 | -44.73774 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1e703fd8-31e5-3237-b033-881c6223c809 | -11.23454 | -47.7419 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88864ad5-71ac-37b0-a22e-b59c161c293d | -12.41879 | -51.10579 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ada38cbc-1f10-3f63-b065-4743dc243f6c | -12.24735 | -47.83943 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6e0aa06-acd5-3605-b95e-cec67361c09f | -12.26989 | -55.13141 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7fd872a-7531-3f08-96ed-75ea6cd9f0b1 | -9.46952 | -45.5318 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94b97118-a895-374e-bc7c-850915ea27f6 | -9.57 | -46.11795 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4f8249c-a14f-3c7e-8be9-a7e314aee3c1 | -12.31581 | -55.14234 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c4f3aa-b09d-3622-ba03-abbbb646183a | -11.87452 | -56.87358 | 2025-10-05 04:46:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ffb9c410-ef35-3f47-9c6c-c97794aa185e | -12.3123 | -55.14173 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 570f51f9-519a-3152-9bf3-49afeecea267 | -12.86536 | -46.86323 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 731c83d8-8b8f-38f4-81ed-61f65dba71fe | -9.63287 | -54.31729 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 836954d6-769c-3f59-b668-fe2c1905820f | -10.85029 | -47.96841 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f27c87a-305f-396b-8651-89996efe164a | -8.50704 | -54.59958 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a0b73de-9325-3b04-85ab-1522d940da7e | -8.62525 | -54.99371 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb2540af-12bf-3a22-904a-ea15ce42f204 | -6.84679 | -44.73953 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45fd1a8d-8f1b-3173-952a-eaebe2325038 | -9.25684 | -51.81126 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78bac1a7-8a66-3d94-a099-01b0f7ce984f | -10.84522 | -47.97688 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9f2efb1-16e8-320e-a5e1-ac58db018143 | -13.5504 | -47.23006 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d68bc043-a70a-395d-a729-d7cbc584ff1f | -8.12478 | -44.09694 | 2025-10-05 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eaf6b50c-0766-3e1d-8be2-c1be89388d6f | -11.81971 | -46.8615 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 533e1974-186d-3156-8bdf-2c421f8e3fdd | -12.23112 | -47.83525 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 798c8cf2-56ed-365c-88d1-0054cecafff8 | -10.59328 | -54.35648 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7a22f37-d190-3eec-bfa8-9b16d68b890e | -5.60121 | -51.13971 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 404dcf63-dbbd-3e15-8438-cb757de10356 | -13.12562 | -47.97373 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1cfce8d3-d78f-30d8-975a-3579cad658be | -12.31728 | -55.15507 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec56d8a6-5441-3710-80d0-b85dc053dc33 | -12.9037 | -47.31535 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bd1f30f-39cd-3382-abb8-e3a92afbcc6f | -13.46903 | -47.28088 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36f3755a-c3b8-3cd2-ac97-139605cb4d74 | -11.5291 | -47.67434 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0923737c-2288-38fe-bad8-00fc21305209 | -13.35762 | -47.24512 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0611d068-7e08-367e-9f9e-a0229a239ad4 | -11.04998 | -47.78194 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f3a571f-4f1b-3fb8-97bd-c761b9ae0a7a | -13.29052 | -47.61743 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a505d4ad-dbca-3729-a451-5d2363cd4efd | -7.05975 | -42.78027 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c356e145-7d9f-3cdf-9bff-cc2e4d5333f0 | -11.59558 | -46.7075 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73a7366b-9e2e-38af-acd9-cd0fd5f848fc | -13.08035 | -47.8957 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 505a0aa1-ecdf-3a97-aa42-1f7164907558 | -9.39698 | -45.83641 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c85c62d5-40fa-3492-89f7-4e6626e82b1e | -12.23474 | -43.77089 | 2025-10-05 04:46:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 265eb446-d270-3bea-baa4-98db77aa5bfc | -13.32354 | -47.78238 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ac7e664-8532-33d9-a234-047c7c0a690e | -12.39429 | -51.09427 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 657dafa5-60ef-3f09-8cc9-c557f7042979 | -9.64111 | -54.31069 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0cba1b6-d896-3a09-b856-4c06350f28c0 | -13.12068 | -47.80393 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b8775f4-41d3-35fa-aae3-6ce8b08c2c3e | -6.29929 | -45.93279 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 082c57f5-b883-3202-9aec-87b05bc2072f | -12.59462 | -54.76003 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d4f2cd4-6247-33c2-b7f6-fdcb000a1443 | -13.57498 | -48.16768 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 37634b3a-ff6b-3cac-8e9d-2428c1a3efe7 | -12.87921 | -47.282 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af596b7d-625f-3859-b8f5-748d85cfe88d | -12.46824 | -45.52063 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9a66342-92a4-3063-95d3-f7209ac409d9 | -8.70406 | -49.36425 | 2025-10-05 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6241482f-a2f4-3829-87ff-14df9ccee9fd | -10.59955 | -54.36157 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 542ea03a-ef52-3d5e-950e-ca11de426606 | -11.07312 | -47.86852 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adcfd129-dcd4-3dc6-9820-4267378dbffc | -11.9508 | -55.32607 | 2025-10-05 04:46:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 479f2361-b0c5-373d-8d47-4d030d7dd21e | -7.00188 | -46.02724 | 2025-10-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34dc341a-de18-3954-aa84-79fa907e2c27 | -10.39735 | -45.41757 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78dd2a4c-3ac2-31bb-b3ab-2e1be463e3ee | -8.60278 | -46.29271 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b01ff34-f25c-3664-9611-0793e84b0cc7 | -11.21159 | -54.98392 | 2025-10-05 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10f80d62-97ee-30e8-8fb9-8f94336facfd | -13.30676 | -48.11384 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba2261fd-36f0-3de9-8981-7c4520cb2a3b | -12.88586 | -47.29421 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cc98fdf-b0a4-388f-95e4-a2488b7d9115 | -12.60418 | -48.11792 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README101.md)
