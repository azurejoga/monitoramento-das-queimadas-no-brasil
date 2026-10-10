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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 269e4573-113a-32c5-bb69-f510b80c832c | -7.10099 | -41.75157 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9485f42c-037d-3b2f-95cd-652a6a499dab | -7.19144 | -41.99905 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f0901090-70b3-305f-a503-c5baf257ce46 | -6.58355 | -41.55669 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 898f27b4-ea69-33c7-8978-94b8dc022268 | -3.32064 | -53.84149 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb52fb4f-a78f-3278-87cc-dda30113aebd | -3.26364 | -54.68651 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 174341f1-4de2-320b-8727-2e78b1dd3310 | -8.92703 | -45.41677 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afd37831-fb9a-3333-95b3-0f6104d5bed7 | -5.88101 | -43.4062 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c94f476-c956-3c8a-8025-1e70751a6318 | -2.20806 | -50.82343 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e8aaae1-2032-322f-8d38-19fb7574741e | -7.52902 | -45.30958 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 89908363-f33c-363a-9df3-ed5a7ad7e354 | -8.26034 | -46.41976 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e41d443b-f999-3fcc-88d9-195249202f51 | -4.81593 | -42.75339 | 2026-10-10 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3be570e-c05a-3906-9186-4df1dcb852b7 | -3.56899 | -53.00728 | 2026-10-10 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3787c15-0345-30bf-b313-584fce417a17 | -4.11698 | -50.98148 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6fa2596a-8881-3f24-8442-4fbd1b73f44a | -5.69938 | -53.46794 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 195cc6b7-7dd0-3855-927f-2ee89ec81f7a | -6.34197 | -46.03114 | 2026-10-10 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebc1f53e-c81b-3e8c-a267-12ec69151f8b | -4.40803 | -49.77748 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1457c835-03fe-3463-8ccc-073721342467 | -7.10176 | -46.71824 | 2026-10-10 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 571f6042-cf5c-36bc-b493-835dd47f8c57 | -9.48054 | -47.70535 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb4c0f1-5019-384a-9fd4-c454d38b0815 | -3.89181 | -52.1937 | 2026-10-10 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71b24d12-38e1-3503-97d8-bfdbfeec0eb9 | -4.05816 | -50.96233 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd7d8d3-bbae-356c-a65d-b5aafb94c394 | -3.38821 | -44.48143 | 2026-10-10 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 650593dc-c6d1-3fbd-af36-c20de99369fb | -3.18022 | -50.58477 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c586265-a369-3400-87f3-02dc5eec7632 | -3.75504 | -50.00917 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c37d972f-759c-361b-8548-93de31147fb0 | -3.74925 | -50.01162 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98968553-037d-3dfb-8d6b-291477489acd | -3.57114 | -54.70019 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| effadcde-1d30-3a38-8715-f77644e6d8e4 | -9.92528 | -44.78239 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc1747b1-2602-33ea-a25e-f25dc292d240 | -1.62538 | -54.43158 | 2026-10-10 04:08:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ef223b79-5d48-3b5a-901e-a24e54eb48d7 | -4.09886 | -54.01885 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0b450ba1-2ef9-3f38-86e0-7a2184ae2887 | -1.9564 | -54.40287 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e45ce8d0-6fb2-308b-8121-c7bead44a45c | -6.81975 | -39.54361 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7da0a1f0-76f8-3d42-95a7-05c349647eb3 | -3.20915 | -50.54549 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8aa3f851-d41f-3b95-a17f-f7b73877b477 | -3.59041 | -54.59897 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d1ce93f7-0344-3a3a-8eda-49a128971bb4 | -6.43786 | -55.205 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6707946c-58fe-3bbe-8551-4d7fa6cf562f | -5.2338 | -50.68188 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 01682744-bbbf-365a-a341-42cad7a0fe2e | -4.11734 | -50.98346 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a0336a6-5d10-3924-9b58-4dcdd19889b3 | -3.25256 | -50.42801 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a6d8abc-0373-3d9c-bc51-5bccdb0a0a40 | -5.89062 | -43.41148 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 69643fae-31c9-32ac-a5af-d36661067943 | -4.31449 | -50.78848 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d4894ef-438a-32c2-99dd-dded740876b0 | -4.98626 | -42.60493 | 2026-10-10 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68681508-f7a8-3eae-8019-5a65cc36b59c | -2.73173 | -54.13935 | 2026-10-10 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c506c82c-a036-34b9-998d-25bf76b265d3 | -3.03826 | -50.34113 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01b6748c-a6e2-389c-afdc-224cc4d7d45c | -5.88499 | -43.40304 | 2026-10-10 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38913679-a576-3f94-8f3b-9458bb3f1c1f | -7.00586 | -47.72683 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13c838a7-4ec4-3866-b9de-a5de39fdb7d7 | -7.24281 | -44.18431 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9ade1ff-71e1-3f57-be6f-b847cb6dc21d | -6.24028 | -44.10163 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bec6836-684e-3dab-8175-14f948334350 | -6.32203 | -55.33484 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8645256c-41f2-3fe4-90f2-60c98d7a3ce3 | -3.85946 | -42.99688 | 2026-10-10 04:08:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 038bba2e-3e0b-3868-be55-9d3685620596 | -3.17844 | -50.59555 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c555f2a5-5a6a-3e44-b4dc-9847b6265e41 | -9.9013 | -44.78299 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f49907f5-d002-326e-800e-5d2e2f721ca6 | -9.27137 | -47.40628 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a61cb6-7acb-363b-95fe-9059bcea7d3a | -3.19989 | -53.86033 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c4646cb2-5092-3045-bbde-05a01ab87c2a | -3.23504 | -50.18465 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a29c2712-49df-3bbb-b338-f985f0ba7fca | -6.40793 | -43.73904 | 2026-10-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec61e55a-73af-3329-951f-1d70d4aa65ed | -6.20033 | -45.4268 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 211ba869-37dd-3706-93ff-0b420107f0e5 | -3.28768 | -53.87316 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1f18deb8-9d76-3e53-a086-42ea8e556b19 | -6.43831 | -55.20472 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 13e7b65a-2494-362d-99df-85f57624620a | -3.00703 | -51.01937 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f844106a-f62a-3f58-b4d3-0353eb224bc3 | -2.83766 | -49.8802 | 2026-10-10 04:08:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5680dcfa-dd35-32e0-91b0-4c92b59ec6ed | -7.02972 | -47.66209 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d252c6bd-58d9-3d37-b500-e7df03887a92 | -8.99346 | -45.88091 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07906b5a-00d3-36b5-8bb4-cf9fd8558f65 | -7.10394 | -52.66942 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87c5e42d-4c88-32af-9e49-f93bd4758588 | -5.75177 | -45.13566 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7c48c311-c0c2-349f-9b2d-33325597b8f9 | -8.9425 | -45.121 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8c0e621-d04a-319b-8e1f-2f61d525cb88 | -2.93984 | -54.08281 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c077779b-9b1f-3353-8ef5-610421225ce9 | -5.79181 | -53.80093 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb51b1a1-f2f9-3950-98bb-d40b2ec571bf | -3.34332 | -50.41758 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7ebb25b-b41a-34e5-9499-4b47754f74ef | -7.11008 | -42.5181 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 74c6ef67-93fb-39f0-9fd3-4e0975f85dc4 | -8.9863 | -47.53656 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bc44290-55f8-393f-a877-c8b2608aab46 | -5.68884 | -53.47404 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b54ce417-bc87-3017-83ea-4365d1af28f7 | -8.95101 | -47.37933 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 658d100b-654b-385f-9e28-000d05bafcd8 | -7.05103 | -40.95491 | 2026-10-10 04:08:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 80965060-98ac-3707-9b4a-1517f946b3f1 | -6.54485 | -46.55208 | 2026-10-10 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01db0964-2ed6-3c5a-82f1-debc575832ce | -9.91767 | -43.57478 | 2026-10-10 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c999b530-af70-3400-8009-527206c53588 | -6.06447 | -44.66848 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ffcff5-4e7f-3bd1-a1e6-ff9267336a0f | -5.8421 | -44.92575 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dad43817-8f27-3cfe-980c-690ee0181583 | -6.58301 | -41.56013 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6121b5e1-9dd5-3305-b6ea-f4232bba6a1f | -7.10108 | -46.71571 | 2026-10-10 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e55d4ea0-bffe-3c23-9d9c-258c2dae8eab | -6.72986 | -46.45623 | 2026-10-10 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f2cc51d-9bdb-3902-b633-0e014643590c | -8.24033 | -46.42879 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 497d6f3c-d25c-31d4-8e27-0cdc06ae1dba | -5.65874 | -44.34998 | 2026-10-10 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b57f35a5-3684-34e2-8c99-0cb4d6e20d98 | -7.22556 | -40.3522 | 2026-10-10 04:08:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9ecd3872-df68-364f-bfc7-a8a8aa09c3e8 | -3.25316 | -50.42448 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a0a45270-436b-346d-b736-dbeed74ced83 | -3.49593 | -54.61386 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5eafa891-b90d-3a79-ae16-67458445879b | -9.27816 | -47.40037 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe47f6b8-8bbd-36c6-bf15-d1a661a1633e | -4.99734 | -45.77464 | 2026-10-10 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9035995b-52df-3f73-a57c-3fceaf13dce0 | -4.11796 | -50.97971 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19c605c8-33bf-32c4-8096-39617c59741c | -9.9129 | -44.777 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0c991a1-da39-37e2-8cd2-c031ab40d8c7 | -5.23877 | -40.57677 | 2026-10-10 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca2fd7cd-0352-3034-876a-624cb4298101 | -7.91092 | -54.73323 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 54022ed1-411d-3e58-87f0-0fc696512e34 | -8.7951 | -47.57908 | 2026-10-10 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cfac60c-70ef-3f45-84f9-31cb1a409574 | -6.37259 | -55.17336 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59d26c29-ddf9-3a0f-8098-9ac24d48dea7 | -6.20775 | -45.42807 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5217ba64-8070-39b6-8aac-a5a4ba9ca7f0 | -5.70378 | -41.76347 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 042f19d6-f04e-30dd-b182-33b1635824d8 | -5.98657 | -47.06943 | 2026-10-10 04:08:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f7e3ff3-733a-3f17-bf2f-bb149612f645 | -6.49862 | -44.36166 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cf60262-f2ab-3235-9e28-be64fdc897a6 | -4.30903 | -50.78756 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 09669aee-466c-363f-bf3b-83d7129d742d | -6.53812 | -44.27954 | 2026-10-10 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b693e324-bc00-3514-b549-299232058a25 | -3.31074 | -53.83745 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8f034e1-080a-3acd-8055-9934be95fbd5 | -3.22389 | -49.43922 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 6c5dc646-62b8-309a-8e18-cf1d53c5f3c4 | -3.55713 | -54.69758 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README42.md)
