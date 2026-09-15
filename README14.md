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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 946e901c-a922-3365-b60e-0e13c2ca3714 | -5.1255 | -55.955 | 2026-09-15 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c2779d3e-545b-372f-9e2a-66e334c1b7a7 | -6.7195 | -48.1201 | 2026-09-15 01:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 439af6ec-ff41-322a-9c2f-570c73275dbf | -3.4272 | -58.2138 | 2026-09-15 01:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| afa990d2-10c3-3417-a460-26a040a92ac4 | -2.9025 | -50.4214 | 2026-09-15 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 35ad1ffd-f4de-31b2-adfe-0f5f6c9ea789 | -2.6966 | -57.5889 | 2026-09-15 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8c072d27-7f52-3bb8-b592-6085bb3f2d19 | -4.6776 | -42.0713 | 2026-09-15 01:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 500f7141-8d9c-3b17-9da3-89644f31938e | -6.8448 | -55.5411 | 2026-09-15 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 160ac97b-ad76-379c-b035-de07a2e0afe1 | -3.5336 | -53.9939 | 2026-09-15 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1e2151ea-b357-3ab5-9f95-e29d0d0ef681 | -6.8446 | -55.5611 | 2026-09-15 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| f2afccb1-02e7-3c2b-8b97-9b2cc63e3d95 | -11.8836 | -43.8378 | 2026-09-15 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ec32445e-2cc5-38a1-b289-befde9cde44a | -2.9025 | -50.4214 | 2026-09-15 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| c6e64e83-f655-31d0-8cec-143941b350fa | -18.1709 | -51.7685 | 2026-09-15 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 76ae181e-1d8c-333d-af3b-93e84e0d79d6 | -11.884 | -43.8142 | 2026-09-15 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 330d07c7-e874-3ab8-8708-7d1e58352486 | -18.1714 | -51.7466 | 2026-09-15 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 200.3 |
| e5d836b3-a6a1-3dc3-9f16-54b316a0a0a1 | -4.6776 | -42.0713 | 2026-09-15 01:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 06101b36-65ae-3bb6-9373-98110d0ba09a | -4.6774 | -42.0951 | 2026-09-15 01:20:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 1aa699e3-d87b-3b40-8a38-7deca5e9741d | -3.552 | -53.9934 | 2026-09-15 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 87a5a6d1-146c-3ecc-b6c9-778e721664bc | -6.9612 | -44.5316 | 2026-09-15 01:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 8339c754-ce4b-3e7d-b97b-d01f6bd123b9 | -3.3637 | -61.3282 | 2026-09-15 01:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| fd732d7b-dd91-3ec3-b8e9-0aac43d2eb2c | -3.382 | -61.3279 | 2026-09-15 01:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| a3670039-30db-3432-bf99-0ac41bf3a908 | -2.9209 | -50.4208 | 2026-09-15 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e7fef74e-c94b-3d36-ab4c-1d36ce018914 | -10.1755 | -36.5659 | 2026-09-15 01:20:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 74.4 |
| b6238221-d19d-3bd9-8963-66a850e940fd | -10.7572 | -44.8184 | 2026-09-15 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ec704cd5-caff-3f47-9ebb-77124259f446 | -14.37224 | -58.35699 | 2026-09-15 01:20:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 7ed4bed7-af55-3495-9f73-639d6feb01a5 | -9.53603 | -62.36285 | 2026-09-15 01:22:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d4133080-8956-3153-a55e-82fc695c614c | -9.85242 | -65.19023 | 2026-09-15 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 38bbabaa-9a68-378d-824e-9ea92f8cacca | -9.85055 | -65.17767 | 2026-09-15 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 60fa8172-c714-3109-8133-c901e07ac806 | -9.40556 | -62.70604 | 2026-09-15 01:22:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3a493d29-ed14-39e5-b631-78f2aa9818d1 | -9.71912 | -64.91557 | 2026-09-15 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7ea20c82-8b0a-3906-af71-fbf90753556f | -7.55936 | -62.32582 | 2026-09-15 01:22:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| bd1f5389-e35d-35b5-aff8-08b82bd862a5 | -9.70855 | -64.91723 | 2026-09-15 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4f80e41-6279-3ba7-beda-8be9ebdea6f3 | -9.40876 | -62.71888 | 2026-09-15 01:22:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 31.1 |
| e2dc3080-1b07-3b0c-9c2e-134f8d9fc9cf | -9.40857 | -62.72544 | 2026-09-15 01:22:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0a08ac61-215a-3442-b2e2-c72b9b741bb5 | -9.67635 | -65.80023 | 2026-09-15 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c88ec90b-74fc-3bca-8098-970906056098 | -9.53926 | -62.38356 | 2026-09-15 01:22:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1c55c18b-44d8-3ee5-9451-c4b5b993d8fd | -9.53727 | -62.37716 | 2026-09-15 01:22:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 0b926c7b-d1b3-3c0c-b465-c8bc603ca925 | -3.7462 | -61.7552 | 2026-09-15 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| db14985f-cbc3-3839-8b0f-6a76523400c5 | -4.6774 | -42.0951 | 2026-09-15 01:30:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 4b790472-f39a-37cc-80a4-b8aa29f3baeb | -3.552 | -53.9934 | 2026-09-15 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 40ac4675-a946-32ff-848a-f2b5b0439572 | -13.3059 | -51.3022 | 2026-09-15 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5cbe424a-0da7-3bfb-b43e-511869e4aeae | -18.1709 | -51.7685 | 2026-09-15 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 863cd4a9-fc91-3ec6-a895-3da01c202cdb | -2.9025 | -50.4214 | 2026-09-15 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 5d8f9087-fa27-3499-83dd-08bf9b048690 | -11.1207 | -50.9179 | 2026-09-15 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| b169d876-2823-330e-b41d-bfba0980253d | -3.4272 | -58.2138 | 2026-09-15 01:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e0e37b90-287b-38cc-8cdd-0fea9d0dc86b | -2.9209 | -50.4208 | 2026-09-15 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 08fe8e42-0f6e-3912-b761-0fab7a8ab870 | -11.1017 | -50.9199 | 2026-09-15 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| fe3623fb-3603-3669-8bcc-a211edaabbad | -4.6776 | -42.0713 | 2026-09-15 01:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 619a684b-df2c-3cb0-9dda-993104868143 | -13.2867 | -51.3046 | 2026-09-15 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| dc8eb907-8249-3a47-9054-7bbf29bdc0eb | -11.9033 | -43.8112 | 2026-09-15 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d2eaac75-5445-3e20-a191-b44263faabf4 | -11.884 | -43.8142 | 2026-09-15 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 64cfd93d-2747-3676-88c1-df08ea3a11a0 | -6.8446 | -55.5611 | 2026-09-15 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 25ec38d5-bbc5-3b52-96e3-c40efcc9303b | -13.2678 | -51.2856 | 2026-09-15 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3ec139ce-b4d5-3f5a-ba09-2e8fd9cf44d7 | -10.7572 | -44.8184 | 2026-09-15 01:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| eee6fbbc-3725-39ee-afb2-3a9e3e9dfa82 | -13.287 | -51.2832 | 2026-09-15 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 688a2cf9-708e-3eae-af15-30f128a4b265 | -11.1204 | -50.9392 | 2026-09-15 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ae65375f-575b-3ed1-b4bb-d71bda09ba8a | -3.5336 | -53.9939 | 2026-09-15 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 869b02ee-17b3-394a-a6bc-f05b95b381e7 | -13.3062 | -51.2808 | 2026-09-15 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2536810e-9e5a-3e4b-a506-24d844c48aef | -9.5152 | -40.331 | 2026-09-15 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 73f69482-6cd0-3aeb-9e7d-6fa0c7e6eda7 | -18.1714 | -51.7466 | 2026-09-15 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 54b618c1-939f-35dd-b1e2-3d030c867597 | -13.2678 | -51.2856 | 2026-09-15 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 159.5 |
| d358d66b-0af3-3773-a552-7f519ffc88a3 | -2.9209 | -50.4208 | 2026-09-15 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5734905a-f525-3873-bfa6-195604ec32bd | -11.8836 | -43.8378 | 2026-09-15 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b2609bba-f2a5-30e3-8f82-fcf2ddf2b1f1 | -3.552 | -53.9934 | 2026-09-15 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 10273d6a-df56-3096-ad7a-aa3e70fa22a1 | -10.7916 | -46.2298 | 2026-09-15 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c4857ccd-5735-3703-a24e-258a3ed041e2 | -18.1709 | -51.7685 | 2026-09-15 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 94461630-4aa9-339c-97ee-a87b74093621 | -18.1714 | -51.7466 | 2026-09-15 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 88f01305-85ec-36ea-930b-a8ef8b9336be | -11.884 | -43.8142 | 2026-09-15 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| f75bbbff-f9c0-35e8-9762-484570a20519 | -15.2827 | -42.783 | 2026-09-15 01:40:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 64.6 |
| e523b924-f1b6-3f7a-b104-e979f2173dae | -18.1514 | -51.75 | 2026-09-15 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 84dff660-7934-36ef-aafc-e66e76632aa3 | -13.2867 | -51.3046 | 2026-09-15 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 38a8951b-eb29-3c12-807b-7aa77d582164 | -10.7572 | -44.8184 | 2026-09-15 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| fda58cc4-4d43-3689-ad0a-c85864ffcdf5 | -3.7462 | -61.7552 | 2026-09-15 01:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 0ad16f43-df86-3e5a-a8d8-50b52275565e | -13.287 | -51.2832 | 2026-09-15 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.4 |
| d9119d55-70e4-3fce-b875-318538b02d2f | -13.3059 | -51.3022 | 2026-09-15 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 7e4c2be3-770d-3bdb-9467-c8042070835d | -11.1207 | -50.9179 | 2026-09-15 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 3710d6ba-f831-3f7b-8db8-888321599cff | -13.3062 | -51.2808 | 2026-09-15 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| d919cfbb-c829-3bf8-943e-adcf3bc0fc0a | -2.9025 | -50.4214 | 2026-09-15 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ab6a97f6-4598-33b6-b8e4-eab84cacc26d | -3.4272 | -58.2138 | 2026-09-15 01:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 11e6937d-2ba1-3ed5-8611-cd00c706a590 | -11.1017 | -50.9199 | 2026-09-15 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 16836a85-700c-3f99-9cf7-6e5822428bc1 | -13.2486 | -51.288 | 2026-09-15 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 737714a3-021a-3a24-ab33-b999de8242b3 | -3.5336 | -53.9939 | 2026-09-15 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a0cacbc3-b6fe-307e-b02f-a398afa0931e | -6.8446 | -55.5611 | 2026-09-15 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 31113251-e90d-32ec-80b8-cf747188bc87 | -4.6774 | -42.0951 | 2026-09-15 01:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 84872c36-d42f-3076-aa04-6cc8a6bc9da8 | -3.728 | -61.7555 | 2026-09-15 01:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0743d5ae-4a96-3511-88d8-d52c1b732334 | -4.6774 | -42.0951 | 2026-09-15 01:50:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 1295f8b0-b34b-32c8-a511-62ed1e8192b9 | -10.7916 | -46.2298 | 2026-09-15 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| d0bbefbf-fd20-3fab-bada-a0a5cf5d664b | -17.6204 | -47.2607 | 2026-09-15 01:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 53a202cd-8ae2-38b2-93c3-79debe35faca | -6.8446 | -55.5611 | 2026-09-15 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ccf701f4-958f-3607-9c7c-37bf0cc57cae | -6.6952 | -58.7097 | 2026-09-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| c9c0577c-f9ad-3a7b-a246-1d1383360982 | -3.7462 | -61.7552 | 2026-09-15 01:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 7ef114bf-6157-3cca-995f-93d585860f48 | -11.884 | -43.8142 | 2026-09-15 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 134758c2-dce8-3fe7-be70-69958c9725ef | -18.1714 | -51.7466 | 2026-09-15 01:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 2b8e0f66-7130-3641-958f-233015208b6b | -18.1709 | -51.7685 | 2026-09-15 01:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 91f5ebf9-4f76-3aa6-bc1d-8d97a4498794 | -11.1017 | -50.9199 | 2026-09-15 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| ab549334-8405-30e9-ac82-e95e53e926b1 | -6.6953 | -58.6903 | 2026-09-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9d69ffb3-519e-397f-9cf3-f2f324fe8c83 | -3.5336 | -53.9939 | 2026-09-15 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 4fd6c02b-a06c-35c2-97b6-866c5794da71 | -18.1514 | -51.75 | 2026-09-15 01:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| dfa3c2ef-9645-3c9e-a8fc-7192e8298e37 | -11.8836 | -43.8378 | 2026-09-15 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 520e2bcd-2a4b-3d35-af0f-8d9be09b3b0f | -2.9025 | -50.4214 | 2026-09-15 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1c3bd277-f21c-362b-94eb-d675fe5f37d0 | -3.552 | -53.9934 | 2026-09-15 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |


[Clique aqui para ver as próximas entradas](README15.md)
