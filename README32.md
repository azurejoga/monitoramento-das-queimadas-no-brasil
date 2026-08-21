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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cae7f88f-443d-3132-8493-50fc5913973b | -13.3926 | -54.3758 | 2026-08-21 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 403.9 |
| 9ca50ac5-15ea-3001-922f-3e16b1befdf3 | -6.1177 | -59.9069 | 2026-08-21 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 749362c4-fcb7-3ece-8062-fb743f2e4e7d | -13.39 | -54.38 | 2026-08-21 04:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0df3e406-7d47-38e3-9757-ff76e251c0a6 | -7.3603 | -45.8136 | 2026-08-21 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| b60572ea-c143-3e47-9da3-41eb900e284c | -5.5978 | -44.0209 | 2026-08-21 04:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| cb83496e-9bce-3cd6-82b5-5f188e7e5d9a | -6.8756 | -59.4171 | 2026-08-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 5d488eb6-c21a-3345-892c-60a2eec0e3a2 | -14.3149 | -51.8969 | 2026-08-21 04:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 64c42680-ccc5-3071-bda5-58b33615b318 | -11.3263 | -45.0162 | 2026-08-21 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 10bc8ff4-ebe0-329d-892c-5782a649a309 | -6.1361 | -59.9063 | 2026-08-21 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 967f8c2c-106b-30b3-b22f-8cbd88c0109d | -6.8203 | -59.4001 | 2026-08-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| bccf2070-d85b-35db-baae-f2171ac01233 | -12.9237 | -56.6248 | 2026-08-21 04:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 4769f688-3dd2-3537-b871-beea8e6e3b10 | -7.3605 | -45.791 | 2026-08-21 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1b5e8d7b-c013-3171-adef-05037509cdca | -5.6168 | -43.9965 | 2026-08-21 04:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 9234b911-b400-3b96-8373-55bc1b944b91 | -6.8388 | -59.3993 | 2026-08-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| a4223236-ea7f-37db-8b67-8b112f456399 | -9.4069 | -60.4362 | 2026-08-21 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 04df3aba-940d-3e44-ad22-6dfc6ea27e2c | -7.3791 | -45.8119 | 2026-08-21 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b351be04-1703-31ba-9d2a-8461e41b4271 | -11.1747 | -54.0216 | 2026-08-21 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| f8d2e1de-ef8d-36a0-840a-df8bde27282d | -6.2341 | -55.6109 | 2026-08-21 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 92938542-1dc2-31ce-a958-1f475161c7b9 | -9.4257 | -60.416 | 2026-08-21 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f75b7130-d328-37a0-a3bf-132b4d9993a9 | -5.598 | -43.9978 | 2026-08-21 04:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 181.4 |
| b5ac6a3c-5ab4-3a45-b05b-fba8157fd5b3 | -6.2156 | -55.6118 | 2026-08-21 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5cd167d6-6dc9-3f78-a7e6-f84a203e7390 | -8.3717 | -62.716 | 2026-08-21 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a2080da7-fdbf-383a-b370-c2ecf8798868 | -6.1177 | -59.9069 | 2026-08-21 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 8702addb-9f79-3dbc-a6d1-f07b5673d9d8 | -8.3903 | -62.6963 | 2026-08-21 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 45e3b673-4d03-3706-940a-dfaf08e9c41e | -5.6166 | -44.0196 | 2026-08-21 04:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 26a10332-1a46-3b24-bfdb-85a239e0bf4d | -3.5406 | -48.1889 | 2026-08-21 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4fbfd21d-9757-3da8-817b-54bb72e06677 | -9.4071 | -60.417 | 2026-08-21 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 241.3 |
| 7cd964b4-402d-3b00-b8ef-e391c21dd259 | -9.4072 | -60.3977 | 2026-08-21 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 3f9f18df-aae5-360d-8e29-26332e1865ab | -6.8755 | -59.4364 | 2026-08-21 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 4f04a9b5-1cac-3b26-b66e-bc29bf1e26c6 | -11.175 | -54.001 | 2026-08-21 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| cb723bc7-9a3a-3280-a814-656c5d66625b | -8.3718 | -62.697 | 2026-08-21 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.8 |
| d8560d35-47c4-3f6e-ae4d-887e4ad8ec3a | -8.3903 | -62.6963 | 2026-08-21 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c10040e7-228c-36d8-a58a-880239169108 | -3.5407 | -48.1673 | 2026-08-21 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c987f06c-efde-35ce-a646-b91cb04a546a | -8.3718 | -62.697 | 2026-08-21 04:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 266584f0-3bd5-3cf9-8aaf-0bda16654bfb | -6.1361 | -59.9063 | 2026-08-21 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| f11296f2-b002-3207-aefd-2a29798e3e01 | -5.5978 | -44.0209 | 2026-08-21 04:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9448404d-66f6-3cd7-9fa9-260c7003dfef | -11.175 | -54.001 | 2026-08-21 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e64e1fb6-6379-3eb8-be5a-a9191db8d0eb | -12.9237 | -56.6248 | 2026-08-21 04:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d9ecb724-4166-3a54-b22e-e3854390335b | -9.4257 | -60.416 | 2026-08-21 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f1cf2105-0309-37b6-953f-8b95a5a1351a | -11.1747 | -54.0216 | 2026-08-21 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7c776f18-bfcd-3338-baff-49b10965ce46 | -9.4072 | -60.3977 | 2026-08-21 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 7ab2f769-fe55-3e30-bfc4-0c041a6bd85a | -13.3929 | -54.3551 | 2026-08-21 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 742b44b2-dc7c-3906-bf00-50f7d356048c | -7.3791 | -45.8119 | 2026-08-21 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 0adf33df-64a8-3fd6-8872-f63b80afbed4 | -6.1177 | -59.9069 | 2026-08-21 04:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5a7c2a3e-43f2-3064-9c95-cd1258152876 | -9.4259 | -60.3967 | 2026-08-21 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 90f46987-7cc8-37ca-a0f2-ced198653176 | -3.5406 | -48.1889 | 2026-08-21 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0b29c41a-88d9-3fd1-aa62-aac383541c9d | -6.2156 | -55.6118 | 2026-08-21 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 73904692-b92a-3da5-b080-fa1a63868ace | -13.3926 | -54.3758 | 2026-08-21 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 265.7 |
| 6dd4efe2-e7f3-3fe2-9258-537b2e9db870 | -6.2341 | -55.6109 | 2026-08-21 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2176572c-1b2d-38ec-9fb0-d0ec4ae515e0 | -7.3605 | -45.791 | 2026-08-21 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7d24ffc3-db73-33c6-b800-2e69bdb5baec | -13.3923 | -54.3965 | 2026-08-21 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 440391ed-5678-3a97-9060-ceb8298f4c63 | -9.4071 | -60.417 | 2026-08-21 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 196.1 |
| 47aa25fd-fe58-3b5c-8d68-bec62f3eb615 | -9.3885 | -60.4179 | 2026-08-21 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| cc2c68ee-3597-3120-bc0e-39fee5bdd315 | -13.3734 | -54.3779 | 2026-08-21 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 274.8 |
| 1233d8c6-311a-3fe0-b910-21afe77a4348 | -5.6168 | -43.9965 | 2026-08-21 04:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| faebf4a0-b02a-3991-b1d3-c89ff5a5c74f | -13.3737 | -54.3572 | 2026-08-21 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 4f321dcb-a5c9-316e-ba75-1c88a02a8e66 | -5.6166 | -44.0196 | 2026-08-21 04:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 322a2fff-955b-3423-804f-33f3cb2cb8e9 | -9.4069 | -60.4362 | 2026-08-21 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 04555b23-c78f-3ff4-b534-fac112b949b7 | -5.598 | -43.9978 | 2026-08-21 04:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 7e9365aa-236d-3b60-be95-e8deedd950d0 | -7.3603 | -45.8136 | 2026-08-21 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 6d3672fc-654c-3dac-996c-31d459895c14 | -6.8756 | -59.4171 | 2026-08-21 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 760068e2-31d2-36c8-9c80-4427e702c659 | -6.2341 | -55.6109 | 2026-08-21 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| b74215e3-dc21-3964-ba8a-9aa39328b656 | -11.1747 | -54.0216 | 2026-08-21 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| caa8a1ba-b241-37b3-a638-8193582ec1a8 | -13.3923 | -54.3965 | 2026-08-21 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4563e8b3-5fa1-3b35-9437-e788e59c960e | -7.3791 | -45.8119 | 2026-08-21 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f37812e2-f088-3502-86fc-3af9d8a9bc87 | -5.598 | -43.9978 | 2026-08-21 04:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9cc2033c-27d9-3cf7-80f7-29f463c1802e | -3.5406 | -48.1889 | 2026-08-21 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 22a3db0f-d15e-367c-8866-bf3728e573e4 | -6.8755 | -59.4364 | 2026-08-21 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| e28b45bb-3997-3dd3-8e1a-a51c7cabc76c | -7.3603 | -45.8136 | 2026-08-21 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 37547a6b-b1b6-38f7-a939-90892121d788 | -13.3737 | -54.3572 | 2026-08-21 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 9af63807-a9d5-3dbb-8ba3-a2d60bf4033e | -6.2156 | -55.6118 | 2026-08-21 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| f5274246-9f59-3aef-9997-c5fa55fcb63e | -13.3929 | -54.3551 | 2026-08-21 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 04a91bd8-4403-3af2-b4ac-4bcb107f3b32 | -13.3734 | -54.3779 | 2026-08-21 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 215.6 |
| 4e079ab6-0ec6-3ec0-9353-8350a4539e84 | -9.4072 | -60.3977 | 2026-08-21 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| eb04ec4b-c009-3a3e-b63a-2a6b33f4abcb | -8.3903 | -62.6963 | 2026-08-21 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ddff7a5a-557f-316d-b8fc-7a70d1e6306c | -8.3718 | -62.697 | 2026-08-21 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 85426818-7335-333d-af10-9e83119f40f9 | -8.3717 | -62.716 | 2026-08-21 04:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 1f077175-1dfb-3cac-8556-58d9a245c284 | -6.1177 | -59.9069 | 2026-08-21 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7964ebef-4fc0-3773-be26-080e4b0826a0 | -13.3926 | -54.3758 | 2026-08-21 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 238.3 |
| b907e9c2-9011-3e0d-bd5e-ff36c286b789 | -9.4257 | -60.416 | 2026-08-21 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 8e3a6b03-01b5-3350-9a66-f91c12f97599 | -9.4259 | -60.3967 | 2026-08-21 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 1f4a9500-cea5-3629-9699-96aa0024aac2 | -7.3605 | -45.791 | 2026-08-21 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6431bb87-e210-35ea-8033-b2f5c6055950 | -9.4069 | -60.4362 | 2026-08-21 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5b464b64-041b-3a09-9a65-5878a66e023f | -9.4071 | -60.417 | 2026-08-21 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 60b7e876-1f6a-3832-8e3b-970e7d8a3add | -4.09315 | -42.50341 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0fd6952b-87f1-39c9-974f-24a54c28a3e6 | -4.09235 | -42.50908 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5dc9c128-7b4e-321d-8940-f1cd244c0575 | -3.20796 | -50.92208 | 2026-08-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b98bab28-e463-30b3-8894-8215b4731f68 | -4.09913 | -42.49712 | 2026-08-21 04:44:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| d9e1fca1-2127-3730-b70f-c4e9fb6e895e | -2.80479 | -48.59307 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a2f15a2-b6b8-34aa-8b15-298a42e7aaeb | 0.29942 | -60.44824 | 2026-08-21 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f855781-3ce8-3226-b7ee-473999777ae9 | -3.21181 | -50.91913 | 2026-08-21 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9e9078e-b406-315d-875f-4352994e767a | -0.86899 | -47.92954 | 2026-08-21 04:44:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1221045f-18d8-3335-bf20-9d373f4418b0 | -2.47739 | -49.41311 | 2026-08-21 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f94c38e5-a556-348c-9db5-f94e2b400c40 | -2.8777 | -48.6901 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 464824bf-56fb-35c2-9d78-a6c18c94ea6c | -2.7902 | -49.52223 | 2026-08-21 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ce30c6d-55dc-331c-bb17-757db688da44 | -3.46347 | -48.82298 | 2026-08-21 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5a62543-1744-316d-8144-d9f3a9d75938 | -3.53476 | -48.17985 | 2026-08-21 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 28d0758c-5c8b-35e3-92f2-9bcda28330a1 | -1.09783 | -48.05893 | 2026-08-21 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64a69941-181a-3809-9960-80a6e2f68b29 | -3.03934 | -48.4139 | 2026-08-21 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecdc82a0-76e7-367d-a86f-16255d45e26f | -2.76965 | -48.57273 | 2026-08-21 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README33.md)
