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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87ca3672-f1c9-389d-ba32-6b386a882068 | -17.50992 | -44.32459 | 2025-10-27 04:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd8f76d3-2620-381c-a040-12a7f4d79fec | -17.23891 | -46.79295 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db4d9e80-4dbb-3148-96c4-39a58d4edee4 | -12.3032 | -47.47326 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38b32c5f-f037-32f8-88e8-f013b906a270 | -11.42528 | -46.11171 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8699dbd4-ac0c-3de0-93fa-1965ef3e8bc4 | -10.42374 | -47.64962 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac9f8087-6516-3a32-9cea-03451b3f606c | -10.6088 | -46.62229 | 2025-10-27 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59b6c8d9-9e2a-31ad-8355-8440c806e870 | -11.43829 | -44.67834 | 2025-10-27 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f6a7e3b-32bf-3b21-9f18-eed6114c9df0 | -12.78797 | -48.56799 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a086b0c-d28d-3b07-99d3-9ca77cc641fe | -13.5486 | -49.55969 | 2025-10-27 04:34:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21bbe967-8f03-3ebc-8202-069a836a2806 | -14.25927 | -48.1262 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48562494-783d-35dc-a3f7-c65b34aafa0a | -16.3782 | -47.41493 | 2025-10-27 04:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6d5ba4b9-0519-384c-92f7-a5cdea519cf7 | -15.11377 | -43.26113 | 2025-10-27 04:34:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fe4659e2-926a-38a7-9e81-f00495a04539 | -12.59293 | -52.85411 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb7649ba-dd0c-3092-b0f1-b6d2ddee06f7 | -14.62224 | -48.39657 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c6a13b1-abd7-33c9-a82f-60851c783404 | -14.37964 | -51.53106 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa3537fb-c60b-36d8-9ae2-875aa0f55fe8 | -15.51278 | -50.00895 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2f0d14da-d48a-32ee-8564-545aaf463cd0 | -10.93756 | -47.60139 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9ceb6f5-a124-3a81-a75d-2bf4397d4da3 | -10.35242 | -47.1822 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e441551-af30-3a7e-a531-c2031477f75d | -15.50893 | -50.01196 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 30ade534-ba48-3156-bb38-0fa4a572a68d | -12.3254 | -47.4957 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cfa89d45-5b65-3280-8161-6cecdcd37f73 | -11.01853 | -47.80488 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 370403af-e795-36e6-b634-8cb0e2d161d2 | -11.04696 | -47.86383 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 104a23c0-6807-3c89-ba89-9499d59d996d | -17.40961 | -46.88222 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fba84da1-f476-3ba2-8b8a-5c10b24c5fe4 | -13.44473 | -47.3902 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf632f73-c3e9-3f60-8bfd-3f99546f111e | -17.4193 | -46.86567 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e30f2b8c-8894-3190-a59a-16aac4306313 | -12.8626 | -48.65674 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2719e91d-3860-3dff-89c5-1c32ac0c9495 | -10.85964 | -48.95848 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c62f0fe0-e8c5-3b3c-8213-5590c5fc46e5 | -15.15316 | -47.93994 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ab7d22e-3562-3b01-aa1f-ee095c571b0d | -13.24305 | -47.99048 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f7454cf-ede3-3124-ad1c-6f313fa2c4d8 | -14.83048 | -52.43303 | 2025-10-27 04:34:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d1909620-2a28-390f-b00f-446736f4e5cf | -12.24015 | -46.50346 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea85a850-4c7a-3486-8b30-a057d9094fd4 | -13.36931 | -47.42587 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd7b159b-69d5-3b4c-9abc-d35a5217e4f5 | -15.32823 | -43.80416 | 2025-10-27 04:34:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6524f17-f7fd-34ee-954a-6e08eaf11f2a | -14.56647 | -47.99944 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8deec845-c321-343c-859c-ce45f2bc708e | -11.43449 | -46.12407 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a566b1f-97b2-31bb-adac-163fc70c2f2a | -14.37219 | -51.53368 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfb9c28d-516a-318e-afc7-740cce40ba28 | -13.28928 | -54.40133 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d122f237-d4c4-3381-819a-2f6b21d5f0af | -16.1925 | -45.09706 | 2025-10-27 04:34:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c66c0fe-8ab7-3b7c-9c52-2fb0ed4561b4 | -15.12312 | -43.25795 | 2025-10-27 04:34:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0fe6f378-1d97-3425-ba6d-5746a47e633a | -13.55685 | -49.55022 | 2025-10-27 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09392ad4-4cbe-37bf-9a6b-10bba2c5c407 | -12.5298 | -49.59074 | 2025-10-27 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a11ab957-6d09-39b2-a9ac-c3c33475feb1 | -12.31397 | -47.45646 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d45fbee2-2692-395c-8850-71bbc21ebde5 | -17.03694 | -47.05474 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64412c93-8672-3520-ba93-4460a442c084 | -12.07078 | -47.99141 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab116664-95a6-31ff-a324-bc9efa9d8447 | -13.23689 | -47.98583 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21c2e8ce-9699-3541-bf2d-dddf8d031f91 | -11.01943 | -45.15821 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2ac2899-5095-33ca-9b44-5b07e9cc8ef2 | -15.54201 | -44.0192 | 2025-10-27 04:34:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fed39d0-2c79-3fe6-8661-e145b495d535 | -12.90252 | -48.59766 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba8168f0-3456-374b-95e5-79a133fdb16e | -11.90864 | -43.82687 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4794c637-e1e0-389e-8643-d32c9ae991c9 | -10.73212 | -44.19107 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5b07b05-8879-3dd3-9d1f-557e74b2ed1d | -12.78465 | -48.56746 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d175da4c-dc98-38cc-a44e-a8853666c073 | -10.75636 | -44.19586 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1741c322-3bbc-3ee5-9932-b32f4e51531f | -14.44615 | -47.77395 | 2025-10-27 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d2e9533-e6fc-369f-9aa6-66317aab8eac | -12.90692 | -48.59119 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15c3782c-e6b3-3b91-aad5-7750e0162dc0 | -15.51995 | -50.00649 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7c61610-3f21-3692-8893-75feb0bbdb41 | -10.76484 | -44.19202 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4ecff66-dd88-3856-9488-a45bb8502e96 | -11.09361 | -55.55893 | 2025-10-27 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1bea296f-6eb4-356a-a750-57f277f7e799 | -10.90354 | -48.0222 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99215bb4-d261-3ab0-88f1-f053dbf0f5fb | -11.00516 | -47.78081 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a295b134-fbf2-31e3-8620-372c693b6ddc | -10.69058 | -48.05747 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e88292b5-a911-352c-81b5-c399a0b4c233 | -13.27445 | -54.36909 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea67c448-0519-3fa1-9268-ab19570448bc | -17.51711 | -44.99736 | 2025-10-27 04:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcb67ebd-a267-35d9-819b-72d50ee2db7c | -12.33208 | -47.47422 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31454aa1-c933-3c21-835e-f63217a27456 | -18.15518 | -44.26186 | 2025-10-27 04:34:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4fcd6d0-c620-33b9-91cd-54fd81490920 | -13.26646 | -47.97195 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00f1d8c1-87ca-3680-a752-dbb1ba7b1871 | -12.22953 | -46.49501 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92f683db-7f0c-38bf-8026-005c663ebf84 | -11.42418 | -46.09487 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 755a7073-e3fa-3610-9524-0b18efa73f2a | -14.53995 | -47.99166 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb6c7c7a-bd9d-304f-88cf-941ba2af3646 | -15.30347 | -48.06288 | 2025-10-27 04:34:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9f5a954-3d6f-37dd-99ee-8abf02bb8519 | -10.68727 | -48.05697 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f5bbea4d-583d-3eec-af77-57c47b552d14 | -10.87819 | -50.14874 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a15d9ea3-84af-3ba8-9399-e3c8afb57534 | -11.71096 | -44.44397 | 2025-10-27 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f1d63a47-935c-31cd-995f-b8d09d7daae5 | -12.33373 | -47.46322 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60365cbf-f67f-3149-94dd-293bb3ede28d | -11.02518 | -47.80597 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0b8c98c-7e58-3578-9872-d36438fec59e | -13.431 | -47.38854 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29b279ad-35e6-3587-bb36-3417ed26a375 | -12.3265 | -47.48839 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa5027fa-046f-34f9-b6f8-ad7da4a8c333 | -10.95612 | -49.81139 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60f98465-3b50-353f-8283-e2baf278400d | -13.59945 | -43.11489 | 2025-10-27 04:34:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8582b41f-f3e5-3c88-9b8a-e91f7b431816 | -12.96526 | -48.49886 | 2025-10-27 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60b872b6-0bae-33a5-9739-5d1c0bf60f22 | -11.42269 | -46.10582 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e815589a-8b20-3969-abf8-a899a41a1f42 | -15.51167 | -50.01606 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e4e681b-4966-3c38-82dc-d82849369c11 | -10.31719 | -47.21005 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e41901e-5548-3a83-a072-60b38848bf77 | -12.65361 | -52.62927 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e436bc8-1eaf-3681-b594-8af964c5070d | -10.34663 | -47.10674 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05c74ea5-ff00-33f7-a5cf-ad8bbe5391d7 | -13.5519 | -49.56023 | 2025-10-27 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98a68a60-fa4e-3a1f-acee-c764a5518b4e | -10.42042 | -47.64909 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c06fe68-56b5-3433-8d4d-4aba7dcaf050 | -13.00325 | -48.67158 | 2025-10-27 04:34:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bf2e689-c885-31e4-b515-3cb84c5e2c6d | -10.57438 | -48.01709 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61de1218-79fe-337c-a7bf-b8174ac65c80 | -10.9111 | -49.81502 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 351aad74-310a-34af-aee4-967d254d929d | -15.30246 | -42.38241 | 2025-10-27 04:34:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eb03d004-42c3-345d-b3af-f7720201c617 | -12.27985 | -43.7547 | 2025-10-27 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a023a9ec-c035-33c5-ada3-a38e6643665a | -10.6094 | -46.64189 | 2025-10-27 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adf63345-808f-39f7-a1dc-0aab3de10a53 | -11.28967 | -45.15338 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 754e8add-7492-31cf-8788-a2cf123dfe63 | -11.90914 | -43.82325 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5a04753-7d31-3add-a3ce-cea288a81a96 | -13.23299 | -47.98893 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d45c93b-630a-3060-9327-efc92aceb0e5 | -15.50563 | -50.00802 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50eff16f-6969-33c4-8797-6baa9c32fb32 | -12.32751 | -47.45846 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6eb806d-ca5b-311f-9288-cdb6383b865e | -10.53639 | -49.79398 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 570356f0-3fb4-3dc4-814b-824ca220e889 | -10.92672 | -48.02634 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ffb53f1-7bf1-3636-bb25-568b1f6155ee | -10.85653 | -47.44168 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README48.md)
