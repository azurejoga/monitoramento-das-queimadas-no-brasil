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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0691a795-9c5e-3fb2-9adf-1130eaf95243 | -7.73605 | -42.49553 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| acb58ff5-a721-3177-b3dd-93c5c90cbd76 | -4.51987 | -54.94511 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e22ec4e5-b53a-3b47-a2b3-f7b701f2bcfb | -8.48675 | -57.64107 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0a9528b2-b2e5-3258-991a-890c48259b1c | -11.32413 | -47.25295 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6df8e15-f353-3736-8e8a-d3e2b0e64262 | -11.53387 | -46.86254 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2da84f09-efdd-3a8a-8dcd-4b94ecccf58c | -10.78681 | -46.19861 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 24f53531-a608-3e10-8dcc-df69c314d215 | -7.13748 | -42.09388 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e08344b2-ab80-3a36-9fb4-78e78a62ebb0 | -8.39265 | -42.20473 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 42ab5385-aaf5-3894-b4a1-ecd084e5b089 | -9.72105 | -47.09502 | 2026-09-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ebcd5aad-1fe5-3004-9b6c-9f0656e29e3f | -7.13069 | -42.17426 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| eda00d28-19cf-3073-b290-c214fe10b602 | -7.13662 | -42.16878 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| eb038951-da9e-3afa-b0fe-995482c3ea88 | -11.11171 | -47.5044 | 2026-09-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 852003c9-5f9a-370e-a760-bfdf37c769e2 | -12.1437 | -48.25866 | 2026-09-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4c219b7-dbfe-3950-a951-23e771119c62 | -8.61354 | -44.47733 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72494fa4-6fad-3ae2-8bb6-64e2ef210655 | -5.97677 | -46.63677 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d69cb4c4-03a8-3058-9b3a-004b0996a554 | -7.36139 | -44.47961 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e0a50a8-8b97-34a0-be13-a0f2f9849f9d | -9.84075 | -48.37231 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1880918-6b66-317f-8756-9962c1eb8b00 | -8.4744 | -44.89917 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e25d4e7f-37af-3f82-b561-76ddaef28bae | -6.51777 | -44.05029 | 2026-09-17 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9b845bf-0258-30ee-bb65-dd60aecd5d95 | -11.89001 | -47.58211 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0d6164d-4894-32b6-ba2a-08b17dfbccb1 | -8.44803 | -46.02552 | 2026-09-17 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4787356b-519a-378f-8427-c91627231ed2 | -7.97287 | -44.83035 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b28e8a8f-db96-3c4b-b784-1960e152027c | -8.46336 | -44.91701 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf987ea0-f0b5-3746-9d19-994437f7c5ab | -9.10081 | -60.97712 | 2026-09-17 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a2b8b04-e7ff-37ae-b94c-e3292ec67f9e | -9.84066 | -48.34932 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d530147-8502-3676-8387-c8f108ccd816 | -8.50589 | -44.71053 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f7752e4-648a-3c33-b6e9-64a04c495328 | -9.10775 | -45.72977 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 8f5110c6-8406-3e82-b158-39808d52f18d | -7.08294 | -42.09681 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bc732d5c-0be6-37f8-bf60-e56d1ef6c548 | -9.83268 | -48.35577 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d58661ed-65eb-3b33-9036-0a07ce37a3b3 | -10.57643 | -57.69706 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b68b890-ad24-3bcf-95e5-568f17919383 | -8.42698 | -47.75193 | 2026-09-17 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deea75d6-5a54-33eb-8644-2360cda3d33b | -7.14713 | -42.09527 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4414b45b-6231-3138-8134-d94b0459e929 | -9.039 | -47.75338 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93517feb-78d9-3fb0-b39b-93e9a897dd66 | -10.37819 | -46.89106 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ae0d5cc-7dd9-3808-bb8e-dc56239d7ee5 | -11.32046 | -47.25246 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 232684ac-9809-3ac9-a5c6-bda49bd964f4 | -8.91918 | -62.39613 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c5419a5-8f6f-3bcb-acfa-b9c94ee3e96f | -7.14241 | -42.16002 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2a4b47cd-2095-3f66-ae8c-548629ccd87a | -4.57262 | -54.91411 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76fbb64f-20d4-3fc8-91b7-3515f8f68fb3 | -8.49149 | -57.64194 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3baed66b-61d8-3ec9-816b-0f9c6023650e | -4.88026 | -56.06554 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a345107-30ee-3ce2-bf0e-af1d3f00f1f0 | -9.87392 | -48.38509 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| dd946f9e-fa2f-313b-b7b5-c87a745099ad | -7.27639 | -46.80351 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfe25efd-3d61-3395-9015-e44ac95b56b8 | -6.43692 | -55.61188 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81322d5c-7287-3ca5-8b5b-0fa7ca8cce45 | -7.36602 | -44.47654 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ee227a-41ce-38bf-94fa-0aaad8671aa2 | -6.78414 | -48.66423 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a8c08d-aa0d-3295-9905-7a521c9dd9c6 | -11.33576 | -47.2501 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d0c8fe6-d2dd-35f3-b8e8-4b21d27e75f4 | -9.75318 | -46.11975 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 562aaf53-9f61-396c-82a4-87e23bc9d20e | -7.14686 | -42.09075 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ddf4f66-c611-31b1-93fe-6b76b755dbf2 | -10.81697 | -46.16507 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 41e142e0-adb4-3d01-b3d7-f0c6f64cab25 | -7.81178 | -44.84853 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80cf89a6-ca44-3b7b-b59e-800ebf4790b5 | -11.26927 | -43.49239 | 2026-09-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92296554-8849-3a4a-97cb-fab59e851e35 | -9.98777 | -45.45473 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ae9594f-2570-32f0-af28-87b3197aaa0a | -7.8466 | -44.81197 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c26ef276-354c-3bfe-ad85-5d2d8ae124cc | -4.52821 | -54.91901 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48346a3c-a93a-3ce0-baf8-be7c16bb4e13 | -6.75984 | -55.84045 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6866703-76cc-3a0a-9b2e-16834622cb22 | -5.19467 | -49.32943 | 2026-09-17 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73f19e8b-de5b-37b8-9bec-620169635911 | -10.38981 | -58.30782 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93a0db1b-7458-3bd4-8e67-d88504c61098 | -5.86456 | -52.05948 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95e81121-2256-372a-9a80-f8078e9427c5 | -5.83318 | -52.09863 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 714c8e94-d2f8-35fe-8658-939509bed38f | -8.29268 | -45.65283 | 2026-09-17 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a748fe78-4507-3b9e-82f1-fe9d121a8f0a | -6.15902 | -55.70993 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8196dad5-e846-37e8-801d-ac1881a02e55 | -9.84184 | -48.36498 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65566d86-9706-3b6c-942e-1e90744be399 | -8.46486 | -44.55475 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8850cd0-85cc-3afc-810b-db67012004fe | -9.88706 | -48.39102 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce46d369-2a73-33b4-8acd-f088c590e0af | -8.55807 | -44.47696 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d574c8a-0223-303b-8adf-1614fdf74605 | -7.7229 | -42.49475 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9b17e674-c8e5-3100-9ea2-dc346158e61d | -10.24395 | -54.26192 | 2026-09-17 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92793eb9-cde9-323f-98bc-b8b812c45038 | -11.35257 | -43.96638 | 2026-09-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1605fed0-5ca9-3c9c-9f4d-a20f71f535af | -10.8272 | -46.17664 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21410f40-7dfa-3b6f-b2f4-2353154fdcbc | -11.57531 | -46.87532 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60baefc3-08e8-3aec-9d4b-84324535535b | -11.25742 | -47.6653 | 2026-09-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9a9c500-b43d-34d1-b16f-65c15cc93fa0 | -8.84937 | -46.92111 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe520633-40b2-3548-8df6-6c9afec92db1 | -7.94806 | -44.83022 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 37df3452-5ad4-326b-a1c2-be70601506a2 | -7.83646 | -44.855 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2193b7e4-2d3b-38aa-ae0c-2cfac3c3867e | -9.40809 | -62.71077 | 2026-09-17 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ed3eb63-6766-3244-9403-452b176c649a | -8.47415 | -44.89987 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ffd7d47-9164-3d07-96ee-8a385e742ed7 | -8.60607 | -44.49977 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c47f2be7-a98b-3139-a23c-9dd1662ff1b2 | -9.83444 | -48.36755 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f57b73c7-47c5-3372-986a-2f2105b525cd | -7.02826 | -44.62973 | 2026-09-17 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 070f1206-6398-33a1-88c5-584aab204e80 | -7.08312 | -47.48627 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24de507a-ebb1-340b-bd8f-90b72d309d3c | -6.78469 | -48.6607 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 716e824b-4557-3684-8c6e-b67cafd549bf | -9.56281 | -46.58615 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfbda952-c16e-3363-be8c-fe7856cf235b | -9.49067 | -56.75685 | 2026-09-17 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0902e39-bfe4-3e7f-984d-87874876e635 | -9.99725 | -45.44561 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ebeeff3-25a6-3277-b055-1c4d534aa700 | -8.10378 | -45.62535 | 2026-09-17 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5b2f9ab-cc56-32ca-aac1-50b058d023cd | -7.43891 | -44.58094 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a0953da-49f7-3357-b278-64fde552a6f1 | -9.69281 | -58.18159 | 2026-09-17 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28ca7918-3f1b-3973-b417-5b28daa4c95f | -5.49602 | -43.67398 | 2026-09-17 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ff89764-6740-3651-a9ce-9d692931354e | -8.85591 | -46.97777 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0a8e8325-c8da-3c15-a88f-06b9b1f8a22f | -6.58056 | -49.86674 | 2026-09-17 04:40:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78c8f096-c2e1-3012-b83e-6dde6d711390 | -5.76537 | -47.17968 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88b481f6-1f3f-353d-8dd4-ef1fdbd49813 | -10.58073 | -57.69666 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b094f6c-9aee-3056-b83c-fcf8917bfc54 | -8.85902 | -45.86106 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2637a98d-9bb3-34d1-a1de-1ec2834b35bc | -8.50181 | -44.91077 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b6a65b9-af62-386a-9f7c-c6037bc6c687 | -11.91744 | -44.19786 | 2026-09-17 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a9c2b4b-ddad-39fd-98d2-1232aea14405 | -8.37088 | -54.73298 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de39a9e0-63f5-3eb3-8943-f0e31179b6b9 | -6.9483 | -41.69814 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5893da88-ebb9-3d44-9acc-baf16c3ec6b9 | -8.1165 | -54.81026 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 91ad0cc1-dc6d-3698-8be8-459b595156ac | -5.8378 | -52.0471 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ce6ee32-9af2-3f0f-b147-0bb646a59cc5 | -9.71684 | -48.1488 | 2026-09-17 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README41.md)
