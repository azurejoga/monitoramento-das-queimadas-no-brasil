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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 293693b5-6be3-3873-84f7-eb2d47d0d046 | -3.11903 | -54.16109 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60483401-be40-3370-8049-e74a09629ffa | -3.91326 | -55.89858 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d18f0df-2ea1-3b22-95b9-91433cef2328 | -2.93808 | -53.92072 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dfc1b23-14d4-31ed-8b12-90e7501f0bef | -3.8404 | -44.14021 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0daf0c96-ac43-3b69-80f3-834d50e8f236 | -2.8479 | -54.12453 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23707e3a-1aaa-3fdc-8d21-4d05530a81e5 | -2.81687 | -58.29462 | 2026-10-09 04:25:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 7b558b33-7225-3841-81cf-f125c55901ad | -2.94037 | -54.15567 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c184bcd-c3ac-38a7-b537-a5ffff7839ad | -4.75392 | -55.66098 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc040576-6f9c-3777-89e1-b8ad3242c5f7 | -5.99474 | -40.97813 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9e90e93e-d43b-3742-b221-d0322a6b4327 | -3.5693 | -54.68791 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f8bf7f3f-a102-300c-84e3-794ffb47ee5d | -5.71588 | -53.48855 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2197cbc7-8282-3d7e-9b1e-852e799cec47 | -3.35871 | -50.4135 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 605baf7f-7024-3377-ad0d-c2d3ad6a95ad | -3.11111 | -53.93061 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef67e96f-cb9b-3ff9-8221-e0aceea5b515 | -3.60119 | -54.56656 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e73da139-fa49-3c60-87f8-f99abd126008 | -3.25314 | -50.39383 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aadec984-b280-356d-9148-0710046cd3d3 | -3.27004 | -54.0592 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0313a15-5b21-3a8e-8a94-30a812ca246b | -3.73583 | -59.44804 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8261f681-c820-3970-b38c-fe6a6fc92ba5 | -1.12985 | -57.2826 | 2026-10-09 04:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e50d2244-318e-3e1e-b78c-c9f4901406dd | -3.354 | -50.41784 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9e4919d0-3f91-3500-bbe1-3bd82532dc1d | -5.71051 | -53.46343 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67c6e5ab-8fe5-3ce9-becd-1394cb7fcd6d | -3.5484 | -54.68465 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5b35d50-9e2d-3f14-a2ba-5caa3e69472e | -4.07426 | -59.84661 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8c6169ba-892a-3c30-a239-8eb1995557c5 | -3.1098 | -53.78335 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ae59d9e2-6478-3c07-ad4a-6c140bf0fd25 | -4.15732 | -55.13782 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 382e2b1e-fd8f-3f07-9e9d-e3bb8a9b8896 | -3.09594 | -53.96055 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd66df66-a86a-39be-bd6c-cf7a7e576cf8 | -3.54528 | -54.67097 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a218bb2-ec27-3d49-a12a-6af60cbde76b | -3.30305 | -53.70958 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95332a09-9258-3c0b-aac0-eceb239dd43f | -2.84741 | -54.12751 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2408cc10-e505-3e4e-bdd3-4fedaaff20d9 | -3.50218 | -59.27136 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1704688c-c674-3f41-a4d4-9efd60bf7d75 | -5.00041 | -45.2696 | 2026-10-09 04:25:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7d9883e-48d1-3590-9405-bed77bf42351 | -4.65888 | -55.94841 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99fdcad3-ede7-33fa-914d-050c0b3c5e64 | -3.11348 | -54.16311 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8f66144d-e575-3b3b-899d-18b0955b88b5 | -3.30014 | -53.71296 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 251fd632-f58e-3258-bad5-e1c136adf543 | -6.00265 | -40.95272 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e1acbdae-d298-335d-b11e-a10566d5cb70 | -1.10672 | -54.15317 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f10facd-3934-3517-a466-6e05f78ba6b1 | -5.83804 | -43.80885 | 2026-10-09 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d67cfcfe-850e-3a75-8f88-7544daa9a703 | -3.77904 | -58.58972 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c59cd0a5-2182-3c34-97f7-066e9c85d204 | -5.83847 | -44.92851 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43297349-c3b0-3e5c-b029-268d910fbf3f | -5.70826 | -53.44825 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4bd0621-c830-3bcf-95db-331be95b8df2 | -3.74076 | -59.37016 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2ba0fe7e-0d60-349e-a969-8c3b4213fc8c | -3.89304 | -58.95558 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ef96a60-e623-3c75-9ab3-6667506aff0e | -1.41804 | -54.62071 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33e6eed6-ad89-3bf2-b577-2961424b962f | -3.89841 | -58.95533 | 2026-10-09 04:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05502343-6311-3a79-a496-01607ae566cf | -3.35225 | -50.47918 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f62e7e37-7796-3931-9a7d-07e634c42d05 | -6.16731 | -39.45176 | 2026-10-09 04:25:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3cb5729f-954e-375a-8eae-3577006e58b2 | -4.32657 | -44.65332 | 2026-10-09 04:25:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1faf38a3-01e3-3373-9151-e88a439315a2 | -3.01322 | -54.05459 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3775942a-69f6-36c1-af4f-d7a045a76b11 | -3.54372 | -54.68047 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4feb8650-fc32-3ad9-8d73-df1c6723077c | -5.10218 | -46.21227 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 013a37dc-327d-335a-a01a-4e2b41e34b99 | -1.15361 | -54.23057 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb72374e-260d-3160-9c7c-6db9fb79b9a0 | -3.79728 | -50.04796 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 563dfa28-91ed-330f-887d-4fc27250053c | -2.88138 | -54.19568 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5325a973-9877-3a03-a36d-b04764276594 | -2.99913 | -54.08271 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0a3f5be-d5e7-3563-b58a-ee9cf580c495 | -5.68426 | -49.04487 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f1191c-b1d0-31b2-bbd6-cd941a496e2f | -3.11259 | -53.76643 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce51a802-183a-3964-bcb1-5309b5844244 | -3.67239 | -49.52525 | 2026-10-09 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b3ea4ae-39ce-366c-8f02-57b4a91dbc3c | -3.17023 | -50.45785 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e1a41a9-b0da-33e1-8081-be9a18049f57 | -6.19317 | -45.40793 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f75c394-1286-304e-8b47-76519e69183c | -3.00323 | -54.08942 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8107219-ed9d-38f5-b8cc-c9b170c7ae17 | -3.174 | -58.62353 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78013202-8c60-3701-826b-5cba0b974951 | -4.40414 | -43.11703 | 2026-10-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50a3c2a1-73df-3ecf-b734-e5bd961ea57f | -2.46514 | -56.08395 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a777b84-5ee7-346a-8d16-6341b3ac1c43 | -7.38375 | -39.97297 | 2026-10-09 04:25:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39107009-867a-368a-95bb-1b3ed1cc9cf0 | -7.40477 | -35.19445 | 2026-10-09 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 249e6bb9-4c16-3017-ab0b-b05cf4220985 | -3.48301 | -50.49182 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 332b3f86-61f6-3f77-86d6-c47dda4c5873 | -2.81032 | -58.29302 | 2026-10-09 04:25:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 55ebf987-16fd-3448-bfb3-9966d8b4ad84 | -3.113 | -54.16597 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c90e7420-cb60-3d38-bac0-d81686fea57a | -3.42372 | -54.06376 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57e3c3f3-a144-3f30-9b3f-a077ffa36c4f | -5.70435 | -53.46475 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f1a57f3-61e2-3422-902b-fccd59b2c60f | -3.50417 | -59.26498 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed06ee64-0dac-3296-b503-f6725f6f7d8c | -3.30774 | -53.69692 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b71797a-953b-3855-a8e6-0ec936245d2d | -3.09642 | -53.95764 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f19eeb6-0135-390c-b6cd-2c4ef5ca2cc7 | -3.20593 | -50.56222 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb816ae1-42e6-3c3b-a816-df11f2ca64f5 | -5.97867 | -44.26375 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 068e0f92-7c5c-3509-bd04-343a179a532e | -3.62783 | -54.23096 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11425370-378d-33b5-a06f-513e74629d2f | -5.74556 | -43.27237 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a14513e7-7de7-37c6-93a8-7c9f25758307 | -4.32926 | -55.01775 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 542fe010-16ca-32ab-ab5c-abd704cc2b70 | -5.70684 | -53.45043 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| faba84d9-e3b1-3ad3-a38f-3b48075bd4da | -3.5669 | -54.67419 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aaa313aa-0eba-39d6-a413-11f1fc8fdf4b | -2.41094 | -56.53165 | 2026-10-09 04:25:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 54c03b24-c71a-33eb-886a-51d0c2cbff6b | -5.34519 | -45.76797 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d56ccf8-89ea-38b2-baf9-64296fc20e2c | -7.40632 | -35.19359 | 2026-10-09 04:25:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 62265113-169f-3b85-80dc-c13daaef9cfe | -3.02073 | -54.04077 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d79db580-428b-36fd-aa06-f605737f7e06 | -3.85616 | -51.93474 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2578316d-4ce6-3330-8893-9ee1e2e365f0 | -2.97553 | -54.03676 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93d5eb8a-b987-389f-b763-9689cbd64763 | -3.31905 | -54.04324 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2ebf7eb-33ef-3924-ab80-4ed3b2edfaf1 | -4.93343 | -45.72423 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 901a28aa-d815-3d4e-812c-9f09d010aa16 | -7.11606 | -42.54364 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5f2d4f1a-89f9-3256-9812-336e35532794 | -3.02688 | -54.06575 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb7efa0d-aefe-35c8-a378-ee5ec4effd18 | -3.4777 | -59.50234 | 2026-10-09 04:25:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d87a1297-ce12-39b8-98e0-0ab0c8d0d68e | -3.18181 | -50.58557 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd75ce74-001d-33fd-94ed-9889d25bb5a4 | -3.62733 | -54.23407 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1604761e-cc87-3f63-b3a2-51fa51643b75 | -3.73353 | -59.46154 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 35c702ad-44d5-30fd-943d-3eb9f0f21127 | -3.72122 | -54.22456 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bcd6778a-0fea-3256-87c4-fd745348878d | -6.8959 | -39.53656 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e2329d9-cadf-36ff-a30e-46c11e477643 | -2.88541 | -54.18298 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26ae1ec8-6d82-3261-960d-2e54b379c2c4 | -4.32981 | -55.0145 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ce49cd7-9260-3d29-a756-32a25a1de95f | -5.70184 | -53.47923 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| da6248d2-1ffb-34dd-b774-1d0e94021aca | -1.15467 | -54.2241 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 536f5357-ed8f-3847-8bdb-5bac4c772cc2 | -4.20297 | -55.63254 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README97.md)
