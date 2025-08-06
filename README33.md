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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 076fe768-df8e-3dc8-92ef-df85d307dfda | -6.2792 | -45.249 | 2025-08-06 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| a4bc7207-8403-34ef-9edf-97576ad85d58 | -6.914 | -43.6816 | 2025-08-06 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 829fe5a6-695c-3454-a06d-183cce1ab77a | -6.2789 | -45.2716 | 2025-08-06 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 9c0008de-c3a5-345d-8e3f-7751b396c280 | -13.0731 | -56.8527 | 2025-08-06 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 0eb4af0e-c14d-33e3-ab20-11de64994c36 | -6.2602 | -45.2731 | 2025-08-06 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 48f8294c-370d-390a-8bf2-3a681eb0b91d | -13.2472 | -46.9905 | 2025-08-06 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 891d4004-534b-3693-8fe5-9d88f88a4f19 | -8.9213 | -60.7489 | 2025-08-06 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5115c718-ea6f-33be-9934-9ddd26bc1b1a | -8.9213 | -60.7489 | 2025-08-06 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e4a1c55e-7581-3d80-97a7-ab8a6fbd3a78 | -13.0728 | -56.8729 | 2025-08-06 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 32a795ad-7e54-3af2-8e34-f9febb3f88db | -6.2602 | -45.2731 | 2025-08-06 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| aa2fb8b5-cc88-38ce-9d16-f4754d1e5e21 | -13.0731 | -56.8527 | 2025-08-06 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c65fac8c-83b2-3fce-9a74-a52a8f6a2446 | -13.2472 | -46.9905 | 2025-08-06 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| afd93af9-a3d6-3543-8678-85a9b092f3d2 | -6.914 | -43.6816 | 2025-08-06 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 6145f710-e4ad-3b11-a7f2-dfa59cc15e47 | -6.2792 | -45.249 | 2025-08-06 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| f5fea01d-32aa-3a01-a80b-8422ef57772d | -6.2604 | -45.2504 | 2025-08-06 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2ee037e4-0171-3c63-b35a-08375425b876 | -6.2789 | -45.2716 | 2025-08-06 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 0ac09fe9-eb71-3557-b52f-ef8ce8268830 | -6.2792 | -45.249 | 2025-08-06 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| bbd7819b-39c4-3327-97e9-02f50b0551f6 | -6.2789 | -45.2716 | 2025-08-06 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 189.8 |
| a133fc9b-6c99-36d5-b4ec-ff73df83c743 | -6.914 | -43.6816 | 2025-08-06 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| baf4241a-0399-3b2c-a70b-70fe7e531a2b | -6.2604 | -45.2504 | 2025-08-06 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 73866c19-e9cb-36d0-9462-e781252ce46f | -13.0731 | -56.8527 | 2025-08-06 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 4cc775a0-39ea-3f61-89ba-f08b3893579f | -6.2602 | -45.2731 | 2025-08-06 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| c9305849-6383-3809-9fa6-9d576c241da2 | -8.9213 | -60.7489 | 2025-08-06 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e31bca14-09ac-3281-b419-6992d64ea7d8 | -6.5007 | -45.5705 | 2025-08-06 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1694138e-e25f-3557-944a-6ea45b88265d | -10.6166 | -50.4177 | 2025-08-06 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2185b075-cc91-32f3-8c6b-4935a7d644da | -7.5214 | -44.8465 | 2025-08-06 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 58b3b991-a173-3880-b3c0-d5d5d048789f | -8.9213 | -60.7489 | 2025-08-06 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| bf5fe5ca-1665-3043-9886-56c132b71418 | -13.0731 | -56.8527 | 2025-08-06 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2726e715-2b47-354b-9c5d-ee8c0f13c0cb | -7.5143 | -47.1814 | 2025-08-06 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0ac14bbd-0099-321a-b7e0-8159fe32a7ba | -6.5009 | -45.5479 | 2025-08-06 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 0daa3282-3363-3845-acc2-67be01aece3b | -6.2789 | -45.2716 | 2025-08-06 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 183.4 |
| ed2adf20-70bf-3032-b539-11c9fae7bcf4 | -11.7804 | -47.536 | 2025-08-06 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 37520f5c-8d44-3fde-bbca-81d0c660e1b2 | -6.2604 | -45.2504 | 2025-08-06 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| c6e2cb9e-8a24-3046-8e1e-78e32f87ed60 | -6.914 | -43.6816 | 2025-08-06 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 1d256b40-17d2-37c3-ac4e-babec7e2a15e | -6.4822 | -45.5494 | 2025-08-06 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ad1440a5-f641-330d-9420-d803ef2d013b | -13.0728 | -56.8729 | 2025-08-06 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5fde3ad5-793d-336b-a6f2-90348a48349f | -11.7613 | -47.5385 | 2025-08-06 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 4c575802-2ad0-3370-8712-4cf6662ebb5e | -7.4955 | -47.183 | 2025-08-06 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b1380158-c4b2-3e2c-ab89-d491ec4ea9b7 | -6.2792 | -45.249 | 2025-08-06 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| b4f62d42-dd9f-39c9-b799-2234cee189a2 | -10.6166 | -50.4177 | 2025-08-06 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 4640c799-50c3-307f-a3cf-9b3902152de5 | -6.5007 | -45.5705 | 2025-08-06 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f9a73f6e-e694-36bf-aaaa-691e8fef8862 | -6.2602 | -45.2731 | 2025-08-06 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 184002c2-0017-3181-8058-ba44c73725a9 | -10.6353 | -50.4371 | 2025-08-06 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 33a84bd0-18bb-3abf-a2b7-08739b3f0783 | -6.2602 | -45.2731 | 2025-08-06 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 964982c7-4e3c-3ac1-ada2-1186396a329f | -6.2932 | -45.7441 | 2025-08-06 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8c711c01-a1b9-325b-b700-65eafceaae48 | -11.7613 | -47.5385 | 2025-08-06 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 486381a3-c63f-3129-adb8-ef450817c48b | -11.644 | -47.7095 | 2025-08-06 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 00098a0e-8b39-3bf0-86a1-cca21a519fc2 | -10.6166 | -50.4177 | 2025-08-06 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| c0690bff-17ab-308c-a996-0ff0c4422bc6 | -6.2792 | -45.249 | 2025-08-06 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| a0e07eff-797d-30fe-97f9-80cb8b6d692c | -11.7804 | -47.536 | 2025-08-06 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| c451ddd4-b9ca-320f-a913-2f6735c16942 | -6.4822 | -45.5494 | 2025-08-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 891385dc-0068-3c93-b34c-e2cb43612149 | -13.0731 | -56.8527 | 2025-08-06 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 4ac40bc1-9439-3541-bd16-6b340c47a922 | -6.2604 | -45.2504 | 2025-08-06 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 910da880-5e9f-3664-bf7d-b2df0c386d02 | -6.914 | -43.6816 | 2025-08-06 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 451d13c9-b4d1-3887-86f6-95d721ae1ba6 | -6.5007 | -45.5705 | 2025-08-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| d24ddaf6-1c0a-3dd6-8252-b3053d3a8847 | -6.2789 | -45.2716 | 2025-08-06 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 200.9 |
| a6654557-7019-312e-8d79-5c1ced3957db | -13.0728 | -56.8729 | 2025-08-06 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| bc7c9021-88ae-34ab-9a35-d9028d8c308d | -6.5009 | -45.5479 | 2025-08-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8f58784e-d87e-3b99-9166-5cf570775217 | -8.9213 | -60.7489 | 2025-08-06 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2497bf80-2746-3bea-b4ef-2f4899340111 | -13.0731 | -56.8527 | 2025-08-06 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 86d4eeaa-2759-304d-94b3-80c9a2b0442a | -6.2792 | -45.249 | 2025-08-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 23645ffd-e375-3f8b-b25b-6a77fff4d41d | -13.0728 | -56.8729 | 2025-08-06 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 88520bf2-9d89-346b-a649-d344de861582 | -6.2602 | -45.2731 | 2025-08-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 9aaca9ff-c797-3544-8d4d-7724ce132e55 | -6.2789 | -45.2716 | 2025-08-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 172.8 |
| b8bc9534-ab75-39ab-8381-b1764908ebe1 | -6.2604 | -45.2504 | 2025-08-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1d055065-ebff-3da8-8b07-33815e02bf6c | -11.644 | -47.7095 | 2025-08-06 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2a62acf2-9814-3005-b0d8-4b8184cb42f8 | -10.6353 | -50.4371 | 2025-08-06 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 6c353f3c-7c5f-3bc0-91c9-1f7cfd7b4418 | -6.4822 | -45.5494 | 2025-08-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9fda56e4-a2c8-37c3-b15f-6b01bfd6a7cd | -8.9215 | -60.7297 | 2025-08-06 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f9ea8278-4f01-3d54-bae6-5098cc3cb99f | -8.9213 | -60.7489 | 2025-08-06 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 58369cc2-c01d-381b-a4d6-317042dc74c0 | -6.2932 | -45.7441 | 2025-08-06 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 59c8164c-19b9-3033-b7f7-4cad0699ed46 | -6.914 | -43.6816 | 2025-08-06 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4418730b-a83d-3f1e-9309-058f9f15fcbe | -6.9593 | -50.4571 | 2025-08-06 14:20:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 5adf63d4-8f10-3cc8-b8b4-1c2e35eb116a | -6.5009 | -45.5479 | 2025-08-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f60b76f9-b103-36d0-a73f-287d4da53f9f | -6.2792 | -45.249 | 2025-08-06 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a7aabda9-ee6a-3a04-9926-7f7b90f37f3b | -6.914 | -43.6816 | 2025-08-06 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 42d01004-12f3-3e84-be68-c20866821a0b | -6.5966 | -45.337 | 2025-08-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e1241747-55ab-38f6-8602-e5dce27bc003 | -13.0731 | -56.8527 | 2025-08-06 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 25d1eda6-fec5-3a19-8a32-b07da99bdf0b | -6.5007 | -45.5705 | 2025-08-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 157.6 |
| d2163619-8a82-37f2-a284-eb8fd3d55a3c | -8.9213 | -60.7489 | 2025-08-06 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 8a2d1563-e8b2-3dfc-bf61-5122fd12e65e | -13.054 | -56.8545 | 2025-08-06 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 55a7a05f-9aa0-351b-a8da-97398f94cb73 | -11.6249 | -47.7119 | 2025-08-06 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 08fbebbc-647f-3203-8852-04370c23e5d4 | -6.5009 | -45.5479 | 2025-08-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b5334ed3-2694-337d-bb0b-a8a4e4762f5b | -6.9593 | -50.4571 | 2025-08-06 14:30:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| ac729b7d-c4af-3159-ab76-b6fc23f0e427 | -8.9215 | -60.7297 | 2025-08-06 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fd7d032f-4aa9-3191-8973-d424547a7315 | -6.2932 | -45.7441 | 2025-08-06 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 6ef943b3-3ade-3a8f-8217-3b0b3e415c90 | -13.0728 | -56.8729 | 2025-08-06 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 843146df-e60e-35c1-95c1-28f2eb37b69c | -10.6353 | -50.4371 | 2025-08-06 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 34072902-467d-3bc1-ae22-9dcf8fbeec7c | -13.0538 | -56.8746 | 2025-08-06 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 598dcda5-e0cf-3f15-94bb-d8caeea516bc | -11.644 | -47.7095 | 2025-08-06 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 38272637-40d4-3c4e-98c3-51556faa97b4 | -6.2604 | -45.2504 | 2025-08-06 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| eb80c75a-95c8-3717-b8ac-cee362917184 | -13.054 | -56.8545 | 2025-08-06 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 3a5ead45-2cec-3710-8669-e3ce86d1453c | -13.0538 | -56.8746 | 2025-08-06 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 197466b5-7ddf-3a51-b2d1-cb1d0c8b1c28 | -13.0731 | -56.8527 | 2025-08-06 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 119.3 |
| c9f4e697-cf1c-3635-b33a-7f3cb565157f | -6.2602 | -45.2731 | 2025-08-06 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 77a331b3-4ba6-34de-a059-ef6724e417c6 | -9.9284 | -60.4856 | 2025-08-06 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 15b77d1b-8c80-33ee-abe4-d391cf801f6d | -13.0728 | -56.8729 | 2025-08-06 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| b1897506-59d9-387a-9c68-8029cfb08802 | -9.9285 | -60.4663 | 2025-08-06 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 4f5c93e3-d1b2-314c-8822-a76fbe700c78 | -6.6158 | -45.2901 | 2025-08-06 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b3fbf50e-7072-3c5f-9eb6-7ae78bf6d0dc | -6.9593 | -50.4571 | 2025-08-06 14:40:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |


[Clique aqui para ver as próximas entradas](README34.md)
