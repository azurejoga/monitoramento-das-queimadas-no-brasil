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
| 4ee64738-3d4d-320c-bf08-ec0b56dfc750 | -19.9396 | -49.091 | 2025-05-15 00:00:00 | GOES-19 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| cfb5c465-b3f2-33a7-918f-447c819958ca | -13.2778 | -45.4099 | 2025-05-15 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 3eb336d3-8dfb-3a82-b510-e3a8bc55390b | -11.7834 | -47.3573 | 2025-05-15 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 62acb1b9-6b56-35ca-aa0f-7cbaa1badbed | -6.1791 | -48.0712 | 2025-05-15 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 215c6d99-c9e3-36b2-9365-c2478babeb70 | -13.9521 | -56.7893 | 2025-05-15 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 25ff0076-8dce-3be5-8781-eb807a429b27 | -13.9713 | -56.7874 | 2025-05-15 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 7f556318-c325-33d3-b7a7-0076ea0d903e | -13.9521 | -56.7893 | 2025-05-15 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 97ae7a39-2890-35c4-83cd-45a5a736534a | -13.2778 | -45.4099 | 2025-05-15 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 3d005749-1be6-371c-b85e-d01c0ecf43cf | -13.9713 | -56.7874 | 2025-05-15 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 1ad43c83-b07a-37f3-851d-0760e76e41f6 | -6.1791 | -48.0712 | 2025-05-15 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| a569c30c-dbf1-38a2-94af-85b561b28391 | -13.2774 | -45.4331 | 2025-05-15 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| f85ab45a-2b2c-3706-ad34-b82fa0fec47b | -13.2774 | -45.4331 | 2025-05-15 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| ca6d02d0-6e85-3979-bc2c-ac9cc85dc29f | -13.9713 | -56.7874 | 2025-05-15 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 255ba469-55c5-3816-b332-ac21c96403ce | -13.2778 | -45.4099 | 2025-05-15 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 80e2499f-2786-32c3-9e2f-c22915086cd9 | -13.9521 | -56.7893 | 2025-05-15 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 39820ff8-d887-3323-bff8-526d92b850cb | -6.6503 | -41.9853 | 2025-05-15 00:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 402fb6c5-c8da-3c5d-852b-82127dcc3688 | -8.8041 | -49.825199 | 2025-05-15 00:20:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59568026-164f-3b63-a096-b6b07435c9c0 | -5.7932 | -43.618 | 2025-05-15 00:20:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43cb9f11-89a0-3689-8b2c-f315ac226240 | -6.5619 | -44.497898 | 2025-05-15 00:20:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd754bbe-eafe-3a78-8940-2f47cc4c1d0e | -6.665 | -41.992401 | 2025-05-15 00:20:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2f1e59b-cbc4-3bd5-a995-23e9a8ac2f37 | -11.2383 | -49.4799 | 2025-05-15 00:20:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae0c6cd-0b8d-35df-b466-acb88264872a | -8.8015 | -49.812599 | 2025-05-15 00:20:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 512692d3-4ec5-3656-9471-40eb3ae7bfdd | -10.3396 | -47.678398 | 2025-05-15 00:20:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 725227f6-69b3-3b73-9f45-2479d80bf22a | -6.1725 | -48.076099 | 2025-05-15 00:20:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55cb16bc-196d-36b8-8c2a-d8f259faf6c6 | -12.1479 | -48.0144 | 2025-05-15 00:20:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c82de1d-8b3b-3da5-8b86-818ae5967fef | -6.6633 | -41.985001 | 2025-05-15 00:20:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e0009b3-8b69-3289-b768-45b9e06851ab | -11.5691 | -47.446899 | 2025-05-15 00:20:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 008bf48e-31e5-3348-a250-be473aa5ef0d | -7.9432 | -49.760502 | 2025-05-15 00:20:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30a05fdc-8b40-3cc4-875d-ec7fa7d110fe | -8.584 | -45.8862 | 2025-05-15 00:20:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3cfcb16-fa6e-3d60-b7e5-2eb92c02dad0 | -6.1823 | -48.074001 | 2025-05-15 00:20:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d7a3135-ead3-3b2d-a035-3e888336f15e | -8.5955 | -45.891602 | 2025-05-15 00:20:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df6821cd-9d0e-39e6-8e7f-9423a33d1a78 | -8.724 | -47.973701 | 2025-05-15 00:20:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c87b5c64-e533-3399-9287-5f2a2e4eb025 | -7.075 | -44.396999 | 2025-05-15 00:20:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ea4bca8-934e-3b91-b54a-e41f1c9f670f | -10.3327 | -47.981602 | 2025-05-15 00:20:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd6f0fc8-f0a6-3586-97cd-c80522d4de02 | -8.7261 | -47.983299 | 2025-05-15 00:20:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75e063e9-3b3c-3886-ad8c-8a5e2564b279 | -6.6569 | -42.002102 | 2025-05-15 00:20:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5d9f81e8-0811-3a4f-bee6-10ed805efb3c | -6.7857 | -47.600101 | 2025-05-15 00:20:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebba4668-8fb9-3f65-aa15-6cec2a4e6ad1 | -6.6667 | -41.999901 | 2025-05-15 00:20:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4dc6a5d3-f2fd-3e3a-8d04-ab67d32e7c71 | -11.7839 | -47.349899 | 2025-05-15 00:20:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99573057-e374-3ccb-8952-0ab11ae0dc00 | -5.7432 | -47.992001 | 2025-05-15 00:20:00 | METOP-C | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5517863e-3932-3f32-8c32-251b70bf9818 | -6.1705 | -48.067101 | 2025-05-15 00:20:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4d49d7c-b832-32c1-9fdb-44dbe6f002e1 | -6.6552 | -41.994598 | 2025-05-15 00:20:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0bf2709c-b892-370e-83e3-8e3895959b1f | -11.6306 | -48.470798 | 2025-05-15 00:20:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f68496a6-e234-3ad2-9c6e-dec94ecdea0e | -6.1803 | -48.064899 | 2025-05-15 00:20:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b160ccb0-ae00-3cd7-bfcf-11bbae82055a | -9.6598 | -47.5639 | 2025-05-15 00:20:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f97b158-083d-3b72-8965-4da7112db074 | -7.953 | -49.758499 | 2025-05-15 00:20:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d611965-3fcd-3c6b-b119-df3a15816258 | -10.4654 | -49.142502 | 2025-05-15 00:20:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ef52597-7e1b-3bb5-b555-b97b7f2d4d70 | -11.1635 | -48.6763 | 2025-05-15 00:20:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d46da74-3a8f-34c5-b3aa-9e5a8caa2701 | -9.6577 | -47.554501 | 2025-05-15 00:20:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da95fbb0-4082-3aa9-a604-2206ec3bc7cd | -6.6668 | -43.201 | 2025-05-15 00:20:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| f2bb9aae-4cd1-3f7a-a261-74b821a92022 | -11.241 | -49.493 | 2025-05-15 00:20:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 576ca024-14a9-30f0-b25c-b30dfb312057 | -8.5857 | -45.893799 | 2025-05-15 00:20:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59f7ca7f-bcea-3538-812e-69e0715ef5db | -6.6535 | -41.987202 | 2025-05-15 00:20:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0063bb09-c02e-34f3-9f70-13d2f40d9f26 | -10.3425 | -47.9795 | 2025-05-15 00:20:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 211e8858-7f88-3821-ae02-1fa120b46c51 | -11.7859 | -47.359699 | 2025-05-15 00:20:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e23c7a9b-1caf-30dc-a932-6030ddafdf2d | -8.5938 | -45.883999 | 2025-05-15 00:20:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc5cfa9-c55c-3f9a-ab17-08c9dca75389 | -10.4752 | -49.1404 | 2025-05-15 00:20:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bb337c2-a6eb-3961-9ca4-bfa49ce824d4 | -12.1457 | -48.003601 | 2025-05-15 00:20:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86ce61a5-e814-3785-aa98-5d4d9e9f170d | -8.5921 | -45.8764 | 2025-05-15 00:20:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f1102d8-2c71-3698-a126-06949a300258 | -7.0734 | -44.390202 | 2025-05-15 00:20:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0537d2f-2458-3172-a597-b78ad7e8790b | -11.5538 | -47.616501 | 2025-05-15 00:20:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc0baa25-01c0-32f9-9ebd-69f6a65230ce | -11.788 | -47.369499 | 2025-05-15 00:20:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 165a6132-d395-3827-acb9-9461f8453390 | -11.567 | -47.437099 | 2025-05-15 00:20:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0228d02-f1a2-3d5e-a644-3a335f76c2a0 | -13.0388 | -53.7206 | 2025-05-15 00:20:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04b8330c-28c6-367c-86bb-98af1b1586d2 | -19.9648 | -45.164902 | 2025-05-15 00:24:00 | METOP-C | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee3601d4-9cc7-3a80-b1fb-c71f919b7a90 | -13.2801 | -45.4296 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 173ac368-154c-3519-ad06-2251edbd48f8 | -13.2668 | -45.415501 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d4183e4-8944-31a4-a8ca-316bb9995507 | -13.272 | -45.439899 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 058ec9bb-c3a4-3ea3-b2b7-6d4bc39f421d | -13.2836 | -45.4459 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14bf7056-80dd-3dbb-91cd-d8c99587afb5 | -19.9667 | -45.174599 | 2025-05-15 00:24:00 | METOP-C | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fcd644f2-dfb3-334a-920b-74780f82ce59 | -13.2934 | -45.443802 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09dedbc4-32bd-335b-8deb-00797278cdd9 | -13.2766 | -45.4133 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b75041cf-8733-3f42-8870-2905af549122 | -13.2685 | -45.423599 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d4292c2-2c3a-35b9-bc78-a8628714d2cf | -13.2703 | -45.431801 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ebd70468-4815-3bd9-bca9-054048036e82 | -13.2783 | -45.421398 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6e36b7a-39e7-3ea9-ae22-5f1b94e3c772 | -13.2818 | -45.437801 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65109ffa-8582-38d4-965e-b9410abd9596 | -13.2738 | -45.448101 | 2025-05-15 00:24:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd70ee43-e26a-33dc-9162-41aa3a8f3663 | -13.2778 | -45.4099 | 2025-05-15 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| fbd30bc4-d1f3-3961-901e-e39f4144fef7 | -13.9713 | -56.7874 | 2025-05-15 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 439dc72d-cf7e-37fd-805e-2aa791125e89 | -6.6503 | -41.9853 | 2025-05-15 00:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| 50d3c8ce-7a05-36c2-bf68-8e6a241704d3 | -13.9521 | -56.7893 | 2025-05-15 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 43c2161a-d461-3198-b394-440c7d82ce56 | -13.2585 | -45.4131 | 2025-05-15 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 47fb3920-6c6d-3612-b993-4376dbaed697 | -13.2774 | -45.4331 | 2025-05-15 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 08042d89-1d1b-365f-8265-3c6a30726c79 | -13.9521 | -56.7893 | 2025-05-15 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 346da5ef-0ec5-3798-a883-f84f52380f36 | -13.2778 | -45.4099 | 2025-05-15 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| a1f81b83-9061-3384-8f82-815b1dfde5a2 | -13.9713 | -56.7874 | 2025-05-15 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 98ef5326-95f0-312e-af57-635fadb6092d | -13.2774 | -45.4331 | 2025-05-15 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c2b60532-0e75-366b-a208-f67352e15d6a | -13.9713 | -56.7874 | 2025-05-15 00:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| b42e2894-459d-3385-905c-9ab491e1b809 | -13.9521 | -56.7893 | 2025-05-15 00:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 7b2bc3f7-6100-369c-b2c2-e78fe6b236a8 | -13.2778 | -45.4099 | 2025-05-15 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 139189b8-d171-336b-8b77-e2367ac3e523 | -13.9521 | -56.7893 | 2025-05-15 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e673091f-e2f5-346a-9e6a-ae45e8aa3fd4 | -13.9713 | -56.7874 | 2025-05-15 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c9efa7f1-0f24-33ae-b15e-0244d925a3f7 | -13.2778 | -45.4099 | 2025-05-15 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 254.4 |
| 63444ade-f7c7-3bea-94a6-d63f20a972aa | -13.2972 | -45.4067 | 2025-05-15 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6540f50f-953d-3b0f-8947-54c7ba068c7a | -13.2774 | -45.4331 | 2025-05-15 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 6d2d0ca7-9559-3db4-8ab8-0296b2865550 | -13.2967 | -45.4299 | 2025-05-15 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 924f2f5c-3c38-3bb7-8f48-1e943ed26ee9 | -13.2585 | -45.4131 | 2025-05-15 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 975dba9c-9a4c-3f4a-b9d6-fb0cb5d54b2e | -13.258 | -45.4362 | 2025-05-15 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 1280a0d7-7242-34d5-874f-75627474cbcd | -6.6503 | -41.9853 | 2025-05-15 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 22226365-4911-3e86-80d8-e0a12a2ae587 | -6.1791 | -48.0712 | 2025-05-15 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |


[Clique aqui para ver as próximas entradas](README2.md)
