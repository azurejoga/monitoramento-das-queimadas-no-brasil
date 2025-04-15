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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce0cbec6-ba59-3414-8c6f-7f8332a8a5ff | 2.3964 | -61.3048 | 2025-04-15 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 152.8 |
| d1f1308d-cba5-3f4b-bce8-5b96230b6d02 | 2.3965 | -61.2859 | 2025-04-15 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 210.1 |
| 6a2fda2d-4862-3129-bbbe-817e7a4bd290 | 2.4147 | -61.3045 | 2025-04-15 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 5a5889ba-6a5f-3be4-8013-2c7734ddc4b8 | 2.3782 | -61.2861 | 2025-04-15 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 76a4ec54-873d-3d1c-a806-6fb53d9df643 | 2.4147 | -61.2857 | 2025-04-15 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 104.5 |
| aab4a157-874a-35e8-831a-5d7ad1487bef | 2.3782 | -61.305 | 2025-04-15 00:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2dc01078-e820-34cd-abb2-2adfd0bbd088 | 2.4147 | -61.3045 | 2025-04-15 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 6a5cc830-7d55-3156-b743-8c993bbabba2 | 2.3965 | -61.2859 | 2025-04-15 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 191.5 |
| f1e31b27-50c4-38bb-a110-13a685f0c706 | 2.3964 | -61.3048 | 2025-04-15 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 35816d88-fd26-32e8-b1a6-3344e83c55d6 | 2.4147 | -61.2857 | 2025-04-15 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 8545761e-1f77-3ee3-984a-1c5d59cae5ba | 2.3782 | -61.305 | 2025-04-15 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7d547d3a-1955-324d-83fb-0e3de6146d90 | 2.3782 | -61.2861 | 2025-04-15 00:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1ea470e0-1faf-3562-9383-c45376a5889a | 2.3965 | -61.2859 | 2025-04-15 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 201.4 |
| 8432d254-1867-318e-9a55-46ebe102ea61 | 2.4147 | -61.3045 | 2025-04-15 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| cae5a484-c3ac-36ed-9d13-12e9edb9ef41 | 2.3964 | -61.3048 | 2025-04-15 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 574198df-ff9b-343d-9d42-fd8bfa00dfcf | 2.4147 | -61.2857 | 2025-04-15 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 91.5 |
| e9f8ab4e-054c-3472-a4bb-2f27a7562d12 | 2.3782 | -61.2861 | 2025-04-15 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 50b9aa70-f6a6-33f6-8b8b-c81dadc10389 | 2.4147 | -61.2857 | 2025-04-15 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 85.2 |
| ef1eeec4-9815-335c-8c3f-aa8f19b5167c | 2.4147 | -61.3045 | 2025-04-15 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 596b8fba-5d67-355b-b20f-7704bebf005d | 2.3964 | -61.3048 | 2025-04-15 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 47af3056-9cb0-3ab3-8efc-6fb863f79cba | 2.3965 | -61.2859 | 2025-04-15 00:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 202.0 |
| 43637f7f-ed87-347d-8801-794a96ee144f | 2.3965 | -61.2859 | 2025-04-15 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 44b465b8-218f-3d29-a361-c76c70744781 | 2.4147 | -61.3045 | 2025-04-15 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 95b78cbf-4f63-33f6-b900-9a8e34feed1a | 2.3782 | -61.2861 | 2025-04-15 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f212b01c-b017-3f97-80d3-f123a9b78c49 | 2.3964 | -61.3048 | 2025-04-15 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 131.6 |
| b14197a0-dac1-3269-9146-275bc7b24d60 | 2.4147 | -61.2857 | 2025-04-15 00:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 149bde7b-40d7-3df6-8bc7-5bef409fef18 | -6.3724 | -43.6586 | 2025-04-15 00:44:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31685d29-9742-30ee-8efc-506ed4e7511d | -20.098301 | -41.565399 | 2025-04-15 00:44:00 | METOP-C | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b26e846-3594-35bd-acd4-c23fbf61dfc7 | 2.4145 | -61.278999 | 2025-04-15 00:44:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dafe8da9-8d41-3e72-955b-646483724335 | -5.5837 | -44.541698 | 2025-04-15 00:44:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d344966d-cd84-3d52-9243-7614c74317a8 | 2.409 | -61.301899 | 2025-04-15 00:44:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbf3cfe-7d47-3778-9d71-ac9a94aed596 | -5.5812 | -44.5312 | 2025-04-15 00:44:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce08a40e-b556-32fc-88ed-4fd29b272a5e | -20.2498 | -46.569 | 2025-04-15 00:44:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1e094a4c-130a-3846-82b8-7edbeabff4b1 | 2.4048 | -61.276699 | 2025-04-15 00:44:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2f354593-dc8e-3371-8e95-cf4983a65c2f | -7.4574 | -45.522701 | 2025-04-15 00:44:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be8af2af-ca5d-353a-9262-ba10817f8170 | -21.3647 | -48.599602 | 2025-04-15 00:44:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7257060-8f07-301f-b812-328bafd9579f | -6.3627 | -43.6609 | 2025-04-15 00:44:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e1f3122-0cc2-3635-81a9-43b26ca40cdd | 2.3897 | -61.297401 | 2025-04-15 00:44:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4019f2b6-e9b9-34f8-9500-e4c1d6481ea7 | 2.3993 | -61.299599 | 2025-04-15 00:44:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c7654d84-801c-3395-8855-ab9432bd920d | -6.3696 | -43.646999 | 2025-04-15 00:44:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 863254cb-5547-3c11-8369-ad01f6d26a95 | -6.3599 | -43.6493 | 2025-04-15 00:44:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49a0f031-6a35-35db-9225-eeca886d0fcc | -20.246599 | -46.554401 | 2025-04-15 00:44:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8ce5a685-2e64-3ddd-b818-7e452a9e3dcf | -19.762501 | -48.1343 | 2025-04-15 00:44:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 216dbf42-8d5c-3a4a-bcbc-cfa992652c9a | -20.248199 | -46.561699 | 2025-04-15 00:44:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0f1b7ddb-18f2-3963-9d3a-532d0e59a6b1 | 2.4102 | -61.254002 | 2025-04-15 00:44:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09d3de31-22e4-3fe7-a13b-849496571eea | 2.3952 | -61.274502 | 2025-04-15 00:44:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2a903f19-ad2d-3b50-9b87-63ef79c0ffee | -21.363001 | -48.591301 | 2025-04-15 00:44:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72776db8-1a48-34aa-844b-04113ed0d9ce | 2.4147 | -61.2857 | 2025-04-15 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 51f00700-c8b4-3e51-9c8b-ed72497ad255 | 2.4147 | -61.3045 | 2025-04-15 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| eab6d6ee-01f2-3a83-a325-a5987fb88259 | 2.3965 | -61.2859 | 2025-04-15 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 182.9 |
| 57a29836-8ac0-311b-8033-458ed20c18c5 | 2.3964 | -61.3048 | 2025-04-15 00:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 0287affe-b69c-3e55-a00e-d82f536aab9f | 2.4147 | -61.3045 | 2025-04-15 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 380c1009-800a-3fe7-8465-4fdc37fc48e1 | 2.3782 | -61.305 | 2025-04-15 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1573574f-1d77-3401-9b9a-f860958805b8 | 2.4147 | -61.2857 | 2025-04-15 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6364f5b9-449f-30e2-a484-ceb5a6f31721 | 2.3782 | -61.2861 | 2025-04-15 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 383388b8-c1e9-3ab0-aae7-4b7a0fd4f213 | 2.3965 | -61.2859 | 2025-04-15 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 169.0 |
| 3b18f6d1-b7fd-3884-abbc-a9a2324187a0 | 2.3964 | -61.3048 | 2025-04-15 01:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 143.5 |
| a14520fa-6a07-3a9a-b042-38c370d345d3 | 2.3964 | -61.3048 | 2025-04-15 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 3229d542-5687-3221-874f-a2e6c91ede85 | 2.4147 | -61.3045 | 2025-04-15 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 30fb5d6d-b371-3a37-b270-2b2f4b782019 | 2.3965 | -61.2859 | 2025-04-15 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 47f3e470-ed22-32e7-91a9-f7cc0aac70d5 | 2.4147 | -61.2857 | 2025-04-15 01:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0d1e481c-aeb0-3e2b-9153-a8eb412c15b2 | -20.24058 | -46.5748 | 2025-04-15 01:24:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9dd7f6b7-b926-3456-8e5b-ec1b146559fb | -20.23357 | -46.53952 | 2025-04-15 01:24:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 319e71c3-2747-3bf8-b128-7fb6fc23641e | -20.23178 | -46.57172 | 2025-04-15 01:24:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 833166ea-43bc-313e-9b74-70f22e567f2e | 2.4147 | -61.3045 | 2025-04-15 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f905f876-0bc7-3642-9afa-f75dd783cbed | 2.3965 | -61.2859 | 2025-04-15 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 9b05d796-c9ba-3660-bfdd-98c2ce662816 | 2.3964 | -61.3048 | 2025-04-15 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 121.0 |
| cd5d862d-fa70-37d1-a2e3-5aa4df051202 | 2.4147 | -61.2857 | 2025-04-15 01:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7177b16d-74ed-3da7-bfd3-b53a028fe2d3 | 2.40329 | -61.29747 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f6522fd7-99fd-3b4b-98dd-6165cdcfc435 | 2.40572 | -61.27989 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4ac1c5f4-22b4-3c09-869d-d1ff13702456 | 2.40207 | -61.30625 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d327de12-24e0-314f-9075-eec9ad402909 | 2.39568 | -61.28744 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 363a587d-a82a-3dfb-9e97-b3fdda7edd5f | 2.40451 | -61.28868 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 75df4c45-29bf-3156-825b-8a9ed94b0bbb | 2.41211 | -61.29874 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ba90133-0d99-3abe-9e07-a16870fa11f0 | 1.64735 | -60.23462 | 2025-04-15 01:30:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 18f74ec8-1166-3602-a6fe-715e02fb34b6 | 2.41333 | -61.28993 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cb3753c-3f05-3782-a748-cb077fe7ad27 | 2.39324 | -61.305 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 5e32a968-744c-3f37-9498-c75da7b50cd7 | 2.3969 | -61.27865 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5d6f3ff7-1a03-386d-a744-45be73ee812f | 2.39446 | -61.29622 | 2025-04-15 01:30:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 120.2 |
| fd6cd950-6fa7-3dfb-b47f-a370d82a8788 | 2.3978 | -61.315899 | 2025-04-15 01:33:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fa70e269-ae63-32de-b0c1-e3748b51a45d | 2.4013 | -61.2999 | 2025-04-15 01:33:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b033327a-759d-3e14-8004-984f75775375 | 2.3881 | -61.313801 | 2025-04-15 01:33:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e6e158b5-3788-3819-9411-43be412d1706 | 2.4049 | -61.283798 | 2025-04-15 01:33:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 636eb487-bcf1-3329-8424-d92e8fb97080 | 2.3952 | -61.2817 | 2025-04-15 01:33:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b7470f13-1302-3abd-9269-1c658968e4ca | 2.3916 | -61.297699 | 2025-04-15 01:33:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a2b88045-6563-3b73-9c1d-5a81a1321ff2 | 2.3819 | -61.295601 | 2025-04-15 01:33:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2333278a-6959-3ae3-bb18-f1dbaa76cedb | 2.3965 | -61.2859 | 2025-04-15 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 137.7 |
| f3bab399-729a-3dfc-9b2e-e1663315aa3f | 2.3964 | -61.3048 | 2025-04-15 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 111.8 |
| e00ab85c-eea7-35e7-a3ce-3b4c91ccd568 | 2.4147 | -61.3045 | 2025-04-15 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 5859304e-093e-39ed-94fb-2fc0c5c98026 | 2.4147 | -61.2857 | 2025-04-15 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 86.5 |
| e8c3e478-eb80-33d7-8b25-9961f0c01e0c | 2.3964 | -61.3048 | 2025-04-15 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9e339c22-b8c3-3a24-a156-10754ac6c780 | 2.3965 | -61.2859 | 2025-04-15 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 128.0 |
| fb48a013-5acc-3aa6-9576-63ae44268cf7 | 2.4147 | -61.2857 | 2025-04-15 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d9ac7d3c-9d22-34c3-b743-e31021ff9f85 | 2.3964 | -61.3048 | 2025-04-15 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 55337320-cefc-3e7d-8a99-54ec1cd2fab1 | 2.3782 | -61.2861 | 2025-04-15 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f3b79020-040f-3c03-99f1-e645c28cd47b | 2.3965 | -61.2859 | 2025-04-15 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 51f3ed01-75c5-3bbd-a70e-70170ba2fb59 | 2.4147 | -61.3045 | 2025-04-15 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4dddc8da-3796-38b4-aef0-08967c3429cc | 2.3782 | -61.305 | 2025-04-15 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5196a8e1-6f09-37e8-854c-22a453822500 | 2.4147 | -61.2857 | 2025-04-15 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 4c3c6ccc-f6ef-3472-90d4-59d88dd92bb6 | 2.3964 | -61.3048 | 2025-04-15 02:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 105.7 |


[Clique aqui para ver as próximas entradas](README2.md)
