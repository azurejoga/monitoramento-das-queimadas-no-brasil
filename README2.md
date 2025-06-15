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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d9a0fa3-0778-3d4f-b6e9-898639a3bd25 | -10.09219 | -52.73642 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| c85f0440-f630-3af7-87d9-1eae3a618bf1 | -10.92217 | -56.85319 | 2025-06-15 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 2cf6a5eb-3d23-37b2-8be1-a6087a9fd64f | -11.72605 | -48.87579 | 2025-06-15 00:39:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 31a48155-29e4-3abe-8080-67756874851f | -10.74622 | -48.57496 | 2025-06-15 00:39:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e9d41b7d-83fb-30ed-85e6-202a0a059e1c | -10.09399 | -52.75094 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 47a59adc-e716-3699-aa5d-ea07214b24e3 | -9.40734 | -48.43004 | 2025-06-15 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 98a52e3e-3f2b-3a09-b699-b46741a24631 | -12.69396 | -52.39582 | 2025-06-15 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 73dc9a68-e86c-3547-b42d-4ca62a81ce6f | -11.89089 | -54.68726 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0baad83f-69a6-336c-b96b-d77ecc6a742d | -10.85489 | -53.78399 | 2025-06-15 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f0495768-7a52-3d3f-bdaf-ba60ad792dcf | -12.76802 | -44.41289 | 2025-06-15 00:39:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9c3c5329-041d-3bdf-9033-4a519cac49b1 | -9.4224 | -48.45825 | 2025-06-15 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ab69a499-3b35-3c90-b995-cac4d6013b52 | -12.69584 | -52.41066 | 2025-06-15 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 7d90d2d0-0606-3e2b-967b-5d1a9e28a37b | -8.07569 | -43.11959 | 2025-06-15 00:39:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| d1447f60-1bda-3c12-8d10-6df3806d985a | -7.23311 | -44.15711 | 2025-06-15 00:39:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f2f3ee2b-c317-38a4-b0a5-c65e5e6404c1 | -12.98303 | -48.63956 | 2025-06-15 00:39:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8db36725-3329-3dac-ad99-21baf9c89456 | -10.93776 | -56.85163 | 2025-06-15 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| dabe0a39-9dd3-3342-bb87-f339e6cefc70 | -7.23421 | -44.15041 | 2025-06-15 00:39:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6df7195a-0136-3222-83e2-9746ca427932 | -14.38162 | -47.82241 | 2025-06-15 00:39:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26bd3f90-2365-3e46-a6d0-4a5482605108 | -11.00052 | -55.06141 | 2025-06-15 00:39:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| fd5ccaa3-a908-3ca4-ab66-ce0ccb926b43 | -14.83265 | -48.43341 | 2025-06-15 00:39:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1c0d202e-dcb4-3c30-bc67-fdc42e0bd01b | -10.91297 | -54.78356 | 2025-06-15 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a279b985-4c3b-37e6-87a5-7cac004e11df | -12.09388 | -49.49146 | 2025-06-15 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| da640d99-3160-3d1b-9219-52c8b2341df1 | -9.05086 | -47.91973 | 2025-06-15 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5d2249c8-fd5d-301f-aa99-4e21b41682f9 | -10.24628 | -52.24134 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 44660df9-f2cc-3d6e-b964-be79b11fd58e | -11.18166 | -44.49489 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 99e69683-f2bb-313f-839d-9adff8010157 | -10.9267 | -56.85957 | 2025-06-15 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ecfed8b4-4958-375e-a4e1-e5cb6e62f2af | -14.6678 | -53.12709 | 2025-06-15 00:39:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| eb8af928-376b-35ce-a7f3-ddebc04a8252 | -10.92306 | -56.82822 | 2025-06-15 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| df3663ff-3346-3a4d-8bc3-f4cef9762dd8 | -9.11236 | -49.63488 | 2025-06-15 00:39:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ae05eda5-e2cb-305c-bd8b-9b39944446cf | -13.92635 | -54.6097 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 252.7 |
| 5f7960e8-a6fe-3bc7-b2b1-a409c3e21c26 | -11.01381 | -55.10053 | 2025-06-15 00:39:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 424275a4-65b3-3774-89e2-2423939400b4 | -13.94035 | -54.49157 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 45933c80-5244-3589-83c9-424c5bbbcd9a | -13.92895 | -54.63279 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 3981d198-9d14-3978-91c3-dbce30a25321 | -10.84698 | -53.77916 | 2025-06-15 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 929c498b-1767-3248-946a-34237aca4b78 | -13.23281 | -49.8343 | 2025-06-15 00:39:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5dc81bc8-98c4-3014-a79d-840330e447eb | -12.97407 | -48.64083 | 2025-06-15 00:39:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b37081d-eb96-3cf3-95ba-180cf0dd7574 | -8.5898 | -45.86637 | 2025-06-15 00:39:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ad2ac094-1dc8-3cd5-8a59-e15e07a47a2a | -11.74439 | -46.75072 | 2025-06-15 00:39:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44315b74-d9ed-3bcf-ba71-7c5e94093252 | -8.07305 | -43.10295 | 2025-06-15 00:39:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b42ea798-a23c-3929-be37-504b8c1824dd | -15.40845 | -47.8579 | 2025-06-15 00:39:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 07887576-ef63-34f1-9278-eacf6de005c4 | -8.31925 | -46.20701 | 2025-06-15 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91776e72-5cde-3e51-bcac-c511a5743592 | -9.04431 | -47.01891 | 2025-06-15 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 14acd17c-d14b-335e-b08e-1b1b5d130b6d | -8.58497 | -45.86271 | 2025-06-15 00:39:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2b4270a-be2b-3247-b7e2-2545ed7627b1 | -11.01116 | -55.07743 | 2025-06-15 00:39:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 198.8 |
| a6c39cd0-053a-38eb-b922-06c44f882b32 | -15.41097 | -47.87649 | 2025-06-15 00:39:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb975dc1-3e49-3bbc-b953-45a3ec01f2a6 | -11.01681 | -55.08236 | 2025-06-15 00:39:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 3273e8c0-a019-3494-a93e-3fe08d930a52 | -9.42117 | -48.44936 | 2025-06-15 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| aba0bba7-cda1-388b-b8ef-6f1ca8fe2734 | -10.63196 | -49.43245 | 2025-06-15 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f5f33b83-3ef5-3176-8a76-53db7d50c5d7 | -13.89908 | -54.61303 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| ea48c0cd-e589-317a-a6d0-41a416ac6169 | -13.91271 | -54.61134 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1010.7 |
| 8daebf15-1373-322c-9e8a-a5911acc042e | -16.28812 | -52.93533 | 2025-06-15 00:39:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c98df9ee-d1be-33bf-bc18-d3f186b07ee6 | -13.91531 | -54.63452 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 8f62916a-0d82-3333-9d35-27c2bc54015a | -13.07288 | -48.89834 | 2025-06-15 00:39:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9c49809b-365d-37be-9abd-5f10056b2f68 | -11.88146 | -54.69373 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d4c5af97-5de9-3659-b622-4b09993beb67 | -11.57985 | -47.87223 | 2025-06-15 00:39:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3ba1f74b-c3e4-3da6-a5c8-e7b78248dbb9 | -11.57104 | -47.87352 | 2025-06-15 00:39:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 138b3afb-6341-3e1c-be0b-a6c7221542c3 | -8.07847 | -43.10769 | 2025-06-15 00:39:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 3a3ac01d-0a76-346f-b162-5060fff6a187 | -11.19172 | -44.49326 | 2025-06-15 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 424db13a-35ef-3391-bdad-3538b8cafda2 | -10.99762 | -55.07904 | 2025-06-15 00:39:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f60a1569-434e-3857-931d-f55bac4c22f5 | -12.69387 | -52.39023 | 2025-06-15 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 066b4446-b87f-371d-804f-4d52adbdb29b | -10.63069 | -49.42307 | 2025-06-15 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 078e9f84-cd0f-3699-9dbd-02cee32c18aa | -12.42299 | -43.82085 | 2025-06-15 00:39:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e43fb37e-6c93-3308-b2da-5cc9695e65bc | -9.68141 | -48.60867 | 2025-06-15 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e2b32f6c-7c7c-3509-bf38-1c9177eb5b82 | -10.71293 | -46.56402 | 2025-06-15 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 257618c9-73e5-324d-8472-b91033f82c8d | -13.91013 | -54.58824 | 2025-06-15 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 5315b9cb-4813-3324-bb01-2221e1b39043 | -9.04962 | -47.91081 | 2025-06-15 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cff80774-6f5a-359f-aa7a-9f0616f885b2 | -10.3014 | -60.5421 | 2025-06-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f1307ad1-8c2b-3d6e-8986-82371e38fd6e | -10.2827 | -60.5432 | 2025-06-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| f70e5ff6-9962-31a7-b7c7-24a8e04e54e1 | -12.696 | -52.3917 | 2025-06-15 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d4ffaff4-1671-35fc-9392-ce76de8dfd8e | -10.9924 | -55.078 | 2025-06-15 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ee075fdf-f90b-3d99-bced-90521a7e3869 | -10.9207 | -54.7592 | 2025-06-15 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3ca687d2-2f16-3f35-96ec-d378ad7c1c63 | -7.2028 | -43.0936 | 2025-06-15 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.0 |
| df320f95-3745-3060-a56c-1f680926a4c8 | -9.4158 | -48.4504 | 2025-06-15 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| c0f09a78-fd72-38a1-b853-721fae25fe82 | -7.2025 | -43.1171 | 2025-06-15 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.9 |
| 5c556e5f-fbf1-34d6-8053-9afac412ffdb | -11.0113 | -55.0764 | 2025-06-15 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 96a60642-9b5a-3266-9472-3719ef5e6140 | -10.9355 | -56.8322 | 2025-06-15 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 86ac8a63-1028-31ef-8bb3-37bd50799e39 | -7.2214 | -43.1153 | 2025-06-15 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 7676e2a2-e944-3ffc-8bf2-59887b1d4f72 | -10.9167 | -56.8336 | 2025-06-15 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d1327ff6-7336-3948-a4ea-8fa28131d6b0 | -10.2826 | -60.5625 | 2025-06-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e444b936-cbf0-3c3e-8475-a54e7708f385 | -7.08045 | -49.59814 | 2025-06-15 00:41:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bfb4775c-e7ae-33af-8ba1-7e94923eb85c | -5.62368 | -44.00366 | 2025-06-15 00:41:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 2c8e6e1b-ff02-3728-8bed-c6ec1a88501d | -6.21133 | -43.33109 | 2025-06-15 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 806230ef-fc54-363b-8e0f-40e2f984f95d | -10.2826 | -60.5625 | 2025-06-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d0b7dab8-4962-334d-bb48-0df54ec0ac85 | -11.885 | -54.6926 | 2025-06-15 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8f702f5d-02ba-384c-bbcd-5baacec883db | -11.0113 | -55.0764 | 2025-06-15 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 86060c4e-2531-3445-810c-2fa629b716bd | -9.4347 | -48.4485 | 2025-06-15 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 0bf81653-6ef3-3ca6-8228-d3bb3cab7894 | -10.3014 | -60.5421 | 2025-06-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d1611518-69e6-3f28-bff8-d011782fb7d6 | -7.2217 | -43.0917 | 2025-06-15 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 46da92f4-7e75-3d93-8836-93f8ca114ebe | -7.2028 | -43.0936 | 2025-06-15 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| ed59fd9a-707f-38df-bd76-08cec63aee35 | -7.2025 | -43.1171 | 2025-06-15 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.3 |
| f8cab039-5948-3cb0-8cde-167b0f6eb076 | -10.2827 | -60.5432 | 2025-06-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 3111b3d2-ee28-3ed6-84b4-cfd3b1f6a7c2 | -10.9207 | -54.7592 | 2025-06-15 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| d2ece2ef-70a2-3690-8b05-f7a12a6d5578 | -9.4158 | -48.4504 | 2025-06-15 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 974ef363-897e-3a83-be96-a7fd56c9edd0 | -7.2214 | -43.1153 | 2025-06-15 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| bc85de6c-0241-3799-9f89-1becd26bde22 | -11.011 | -55.0967 | 2025-06-15 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 136cd26d-fa06-3058-bd7a-bf98ea8c1792 | -10.9355 | -56.8322 | 2025-06-15 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5fd1edda-7a02-38ac-83ac-753c2cc5d5b5 | -12.696 | -52.3917 | 2025-06-15 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a3634359-9668-3b47-8e9a-f401aab18001 | -13.9059 | -54.6291 | 2025-06-15 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 50b610ee-eecf-3ad6-96af-f3e274642e8a | -10.9207 | -54.7592 | 2025-06-15 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 002b7699-2934-36e0-9ba0-f8b54f33c993 | -13.9065 | -54.5878 | 2025-06-15 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |


[Clique aqui para ver as próximas entradas](README3.md)
