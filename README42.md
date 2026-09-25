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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f056d54b-447d-3768-af92-0c33c922432e | -14.3689 | -52.1239 | 2026-09-25 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 332e71aa-f278-314d-a3fc-a0884fea63ae | -13.3439 | -51.3187 | 2026-09-25 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 9993a5d0-54da-3c51-abee-ddb86fdbc475 | -10.8189 | -57.1993 | 2026-09-25 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| f8295fcd-ad63-3ff2-8c37-b3ebd94b43f8 | -12.6071 | -51.9595 | 2026-09-25 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 4b9489b4-ea8b-337a-84a3-1863fbe4a17a | -10.8567 | -57.1767 | 2026-09-25 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| d2d0ba92-77d9-361d-8095-2a655b572f4a | -14.3693 | -52.1026 | 2026-09-25 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| db14e559-0fbb-37f8-8a9e-e0eed9049187 | -11.2002 | -55.0398 | 2026-09-25 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a17fa9e9-0368-3bbb-8c0d-7b48d39a7e70 | -16.3645 | -47.7094 | 2026-09-25 14:50:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b3513124-164c-3cfd-8000-e891c2f5a684 | -13.3824 | -51.3138 | 2026-09-25 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.8 |
| c2cbae05-3e00-37d5-a3e4-a0d91857e522 | -12.7865 | -54.0482 | 2026-09-25 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 6e342665-41d8-3d22-a10f-b28b042fe1b6 | 1.5649 | -56.0223 | 2026-09-25 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 8ebc2d98-a4fb-3c59-a5f9-84f5329695d0 | 1.6199 | -55.9429 | 2026-09-25 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| fe89ce4a-db1a-3903-b483-7ff857eb89bd | 1.6199 | -55.9626 | 2026-09-25 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 76f445be-37e5-3cb8-8d95-85aa2785ba17 | 1.5832 | -56.0221 | 2026-09-25 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| d0a25a4b-4f94-352f-a776-fc82aa3653cf | -12.8059 | -54.0255 | 2026-09-25 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c8c5187f-ad76-362a-b78d-a2768cc7ece2 | -10.8569 | -57.1568 | 2026-09-25 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 02f70916-e730-32dc-a837-7f629385da95 | -5.8276 | -47.768 | 2026-09-25 14:50:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 889e05ee-9adb-3496-ae8a-739fd0e2bbab | -12.8053 | -54.0669 | 2026-09-25 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| b6430204-a896-3e06-bccf-e778438e855d | -18.8915 | -47.5482 | 2026-09-25 14:50:00 | GOES-19 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 009a3f8f-06d9-3b95-a9d8-880a5db16b46 | 1.565 | -55.9238 | 2026-09-25 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 3f53697c-b50c-3de0-ad1b-aeb460838ec2 | 1.62 | -55.9232 | 2026-09-25 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| bef03ed2-7ada-38dc-95bb-5ab937d46e37 | 4.0595 | -60.8985 | 2026-09-25 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 7a812ea5-77b6-37b7-b176-a3dc44d75d79 | -12.8056 | -54.0462 | 2026-09-25 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 1f3eb702-9075-3a49-8a8e-0ce2b3c5acc7 | -7.5467 | -61.496 | 2026-09-25 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| ecfb5f23-8920-32d1-ab57-4e9b7af72917 | -7.5284 | -61.4776 | 2026-09-25 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.5 |
| b5c3607e-9565-3866-aed8-17165ace1f57 | -13.3824 | -51.3138 | 2026-09-25 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.3 |
| c82c56c2-3ffc-376d-8e7d-699e078e37bb | 4.0412 | -60.8989 | 2026-09-25 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 89.7 |
| f5a3a911-b7a1-3543-8d15-def33ff4b203 | -16.3645 | -47.7094 | 2026-09-25 15:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 13134052-4323-3481-b504-b4cacebea821 | 1.5649 | -56.0223 | 2026-09-25 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 357562da-4021-3746-a90d-703f6399740a | -9.043 | -65.4175 | 2026-09-25 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ecc9ce64-b094-3620-9dc1-9f70f1fe5938 | -12.8056 | -54.0462 | 2026-09-25 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 8eae6d03-e817-332a-a96f-d7690624fc76 | -8.9428 | -63.2797 | 2026-09-25 15:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 7eb9f7c9-c34e-3a3f-b927-c0c02aab1569 | -12.6071 | -51.9595 | 2026-09-25 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| e9e502d5-05d3-3465-bb81-39be39dd4381 | 1.6199 | -55.9626 | 2026-09-25 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| d31e59d4-9bb6-3d97-a1a9-57b77701ab06 | 1.6383 | -55.9427 | 2026-09-25 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| dcbb9aaa-eea2-38fc-a6a2-54b0b713b559 | -10.8189 | -57.1993 | 2026-09-25 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 140195fc-e1eb-35ca-89a7-adde121a6826 | -13.3827 | -51.2924 | 2026-09-25 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7ccc9a64-6c80-3f4e-a9d5-03707fe87dd8 | 1.6199 | -55.9429 | 2026-09-25 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 1c120dfc-45b1-36eb-8c75-e1dff1a32e22 | -13.3439 | -51.3187 | 2026-09-25 15:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| eb6fe0ee-25ae-34e9-bdc0-061b73096038 | 1.565 | -55.9238 | 2026-09-25 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ab13471f-9f5f-329b-bb2d-c38ced39a52a | -10.8569 | -57.1568 | 2026-09-25 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 15a79f92-e338-3443-ab69-b790914f7977 | 1.5834 | -55.8842 | 2026-09-25 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 435593f1-68fd-3355-b51b-676eccc8bbf4 | -13.203 | -51.7406 | 2026-09-25 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3836c6aa-bc9b-3140-8b67-596771082a54 | -12.8053 | -54.0669 | 2026-09-25 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7915660b-ce46-334b-8b67-7da84b3eb33c | 4.0777 | -60.9171 | 2026-09-25 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a0216616-39c4-34ea-9ad8-7db2d24af99a | -13.3632 | -51.3163 | 2026-09-25 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e1b6b7b4-6808-3373-b542-6c2f77428909 | -10.8567 | -57.1767 | 2026-09-25 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 39ce11b3-c230-398f-8f19-754a85f81151 | -13.3247 | -51.3211 | 2026-09-25 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c95f3ca9-cbb0-3e18-a862-884086e1fc92 | -7.5283 | -61.4967 | 2026-09-25 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| f502609e-d2cf-35a3-950f-1d546bf41069 | -12.7865 | -54.0482 | 2026-09-25 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ced468ea-7ba0-3a5b-939c-371312ab5e0d | 1.5649 | -56.0223 | 2026-09-25 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 162d36e6-679e-3705-8c20-6aae677e501b | 1.5834 | -55.8645 | 2026-09-25 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| b9c0e929-13f7-385d-8ea6-63649fce143d | -7.566 | -61.343 | 2026-09-25 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 5f16e523-ec85-36a4-ae67-ab1d54a19b7b | -12.8249 | -54.0235 | 2026-09-25 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5ac64d51-eb5e-35df-8149-ff3b92047935 | -13.8347 | -51.8316 | 2026-09-25 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 396b223e-457b-3e66-a799-2b30effa626c | -8.8736 | -62.4115 | 2026-09-25 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 97c6ca29-40a8-3d1a-9e9c-76dfb8b8af32 | -13.2033 | -51.7193 | 2026-09-25 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2c566acd-d497-3e9e-94d3-fadc26836917 | -11.983 | -57.6066 | 2026-09-25 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9c4e8cd8-23d0-3392-97ac-0183eb0e8194 | -10.8567 | -57.1767 | 2026-09-25 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 52d1eee2-bdd9-3aaa-a887-74837d4bfd2d | -7.9426 | -63.4861 | 2026-09-25 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 72a46254-0727-3f42-b6a9-a931c5b03a2d | -12.8059 | -54.0255 | 2026-09-25 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 02ebd4b1-7f44-3c42-bbfc-d7b9b6baa693 | -12.7865 | -54.0482 | 2026-09-25 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 48b69f15-3f76-3d11-b0c8-3f09ba68df1a | -12.6071 | -51.9595 | 2026-09-25 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| e1f3658c-4230-33d3-ad9e-8d18ef4150a2 | -14.0425 | -52.06 | 2026-09-25 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 492d373e-e8b0-32b0-ae32-60411b240337 | -11.9832 | -57.5867 | 2026-09-25 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ef385903-006f-3c04-9167-662bb2547827 | -10.8569 | -57.1568 | 2026-09-25 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 342e1271-d103-3f05-b0c4-ed45bb5adbb8 | 1.6199 | -55.9429 | 2026-09-25 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| e06e58c6-25df-39d6-8261-50c09b64b737 | -7.9425 | -63.5049 | 2026-09-25 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| cc4d0ff3-cd3a-38eb-a447-ed9bf73b8527 | -10.8189 | -57.1993 | 2026-09-25 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 1b47036f-0a12-3b1e-83b7-b0d5246085b4 | -13.2225 | -51.717 | 2026-09-25 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 51142be3-8469-33c0-bfd6-97d6375ecb47 | 1.6018 | -55.8643 | 2026-09-25 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d4082dd2-7ddf-346c-9a44-7add279a703f | -12.8056 | -54.0462 | 2026-09-25 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 81c972d5-6bad-3143-83f7-4948ec8cd0ba | -9.043 | -65.4175 | 2026-09-25 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c60fc88f-e485-3882-8007-f67bb4a8930f | 1.62 | -55.9035 | 2026-09-25 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| cfcdd582-684f-3dbd-95f8-3a55b70ce00f | -7.9241 | -63.4867 | 2026-09-25 15:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 04e15437-649f-37cf-95c4-be69abf371a4 | -8.9428 | -63.2797 | 2026-09-25 15:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d25260b1-c91f-3d39-89f9-817b0eb297ea | 1.5832 | -56.0024 | 2026-09-25 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 7fd1be83-bdf6-36b6-be2b-bfd49dfab4d6 | -12.8059 | -54.0255 | 2026-09-25 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 9e944aa4-bf2d-31a9-b5b4-a67604d5bef9 | -8.9428 | -63.2797 | 2026-09-25 15:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7ad4c74f-44b1-3924-8173-f671e57cef12 | -11.983 | -57.6066 | 2026-09-25 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 655e4b11-63ee-3bad-afec-c11e8fc73bbb | -8.8922 | -62.4107 | 2026-09-25 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0c977581-f941-340e-b455-f6cd0e673352 | -8.8551 | -62.4123 | 2026-09-25 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| efd8b488-63e3-3318-96ba-0e8268a5dc3d | 1.5834 | -55.8842 | 2026-09-25 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 3ddd53c6-c7ba-35fe-a586-a57a6b1fe545 | -7.9241 | -63.4867 | 2026-09-25 15:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5be60a39-d9d1-3386-9376-a38b3856bce1 | -11.9832 | -57.5867 | 2026-09-25 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 043a84f8-5b7e-3b6f-8f39-7fd49285a5f1 | -12.8249 | -54.0235 | 2026-09-25 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f07ee91d-b7e8-3d90-ab81-a48f9e137c3f | -13.204 | -51.6768 | 2026-09-25 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f03a9453-b4c2-3aa6-8318-443e09aea06a | 1.6017 | -55.9234 | 2026-09-25 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| eabb04e2-1604-37c1-999d-c775dc1cb6a3 | -7.5477 | -61.3247 | 2026-09-25 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 1cbe7aa9-3c48-3914-99c1-9c2a7fc5c7b6 | -7.5476 | -61.3437 | 2026-09-25 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a5c12535-3141-3dd9-99e7-a60479f260ba | -14.3496 | -52.1264 | 2026-09-25 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 6ba6e170-581e-3fe6-aac2-6872ed4c4b11 | 1.62 | -55.9035 | 2026-09-25 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1b34eda0-f1e0-33b5-a667-d2841dcc8f25 | -7.5284 | -61.4776 | 2026-09-25 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 71a37fd7-bf6d-3571-9fd5-8415052d854f | -11.3257 | -54.0282 | 2026-09-25 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 76022ded-6cee-385e-adff-7f2dd7459000 | -12.6071 | -51.9595 | 2026-09-25 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 7ba0ead6-6480-368b-8b70-f0d7d2cb6bba | -10.8569 | -57.1568 | 2026-09-25 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 404d2406-01fb-30e0-9da1-22dfc558c9f1 | 1.5651 | -55.8844 | 2026-09-25 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 6733980a-188c-3eb6-989c-6468743de1f5 | -12.0021 | -57.5852 | 2026-09-25 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 241f43f6-00fb-37d1-937e-e199d1bf2d1d | -13.7993 | -54.0617 | 2026-09-25 15:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7ca4d408-f7a9-3391-bb34-e9694e3b827a | -10.6827 | -54.1679 | 2026-09-25 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |


[Clique aqui para ver as próximas entradas](README43.md)
