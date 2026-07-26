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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c143f95-20a9-30b1-a645-94a690ba1de0 | -3.12616 | -59.00212 | 2026-07-26 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cea1f422-0c17-391d-8c10-29f708ca9d5b | -5.67961 | -49.81834 | 2026-07-26 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c4e017a-a740-3a09-b058-8806ca3b0d1b | -3.12891 | -59.00249 | 2026-07-26 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a26937-e25b-359b-a592-589636a5601a | -3.72621 | -48.87413 | 2026-07-26 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f604be03-35e2-30f4-84f5-ee0495044545 | -8.33108 | -64.02145 | 2026-07-26 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cc7ed2b-5039-3624-a121-afb48dc49498 | -12.77524 | -59.79363 | 2026-07-26 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c92baa1-7983-3e82-9ba0-f4c2a4adf4aa | -12.66736 | -48.217 | 2026-07-26 05:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef739285-cf28-36a5-942e-a0d71075e14c | -11.58602 | -50.14838 | 2026-07-26 05:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffedced1-4081-33c3-94dc-1b2725c93f2f | -9.29734 | -64.36224 | 2026-07-26 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9963667-780d-39f2-b1e2-f97f1e1cfc56 | -9.73143 | -63.43024 | 2026-07-26 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66db6f2f-6445-3cb6-9991-2ff83efa92d9 | -13.80314 | -53.85645 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f7e9a0c-1cc8-3d2e-9d80-90d361b92035 | -13.80104 | -53.86002 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0e00657-02f7-3c05-b07c-a27325734a04 | -12.66025 | -48.21602 | 2026-07-26 05:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be23a155-aea9-32bb-81ef-661a2da8d67d | -13.93145 | -53.87904 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7daea1dd-af28-3200-8af1-863b700ac2c9 | -12.67193 | -48.21132 | 2026-07-26 05:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39a9dc34-66e3-3389-9745-e8a39ceacb43 | -13.80575 | -53.86377 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f316aa4-abce-3478-b711-a5d666e27d9e | -11.01933 | -54.32181 | 2026-07-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c9b4161-5ee8-3c6b-8012-fba3ac1dbd9a | -11.30636 | -54.47666 | 2026-07-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3574e11-1e01-3b34-a0bc-e7748be5beab | -12.77235 | -59.7892 | 2026-07-26 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d51c411-4953-33aa-92b5-1e5803a4a786 | -12.43857 | -56.54325 | 2026-07-26 05:29:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b73fdab-8fb0-3223-b5ce-999ef4293f97 | -12.67117 | -48.21851 | 2026-07-26 05:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab72584f-d57e-3615-87a5-4c04c6bced25 | -10.01605 | -67.66934 | 2026-07-26 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75a1c608-864b-3559-8d1b-38905392b615 | -11.0146 | -54.32113 | 2026-07-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d871aad-7d86-3634-a83f-0c2a9d7bfb3b | -12.54029 | -57.21777 | 2026-07-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a85adf7-00de-3404-869f-fcc859e4895d | -9.84043 | -62.21849 | 2026-07-26 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7122de61-39eb-3ed0-91f5-7e859450e948 | -12.77176 | -59.79309 | 2026-07-26 05:29:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21a9e076-2d6a-36c6-bf76-013f9761490d | -15.81499 | -56.72103 | 2026-07-26 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4918b904-0b39-30a3-8258-8a770a77389e | -13.80611 | -53.86076 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcc61a03-7c55-3ee6-b2ca-44eb52c15f0e | -9.89091 | -67.02406 | 2026-07-26 05:29:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fd49737-9838-34e6-98f8-899533dabfda | -11.58339 | -50.1508 | 2026-07-26 05:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41c214e7-cfc3-36e9-abeb-35b306317153 | -11.02475 | -54.31731 | 2026-07-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 431bd976-668e-3048-ac8b-8a4fd7f728bb | -13.80141 | -53.85699 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fddc7da1-ada1-3c3d-8a16-586ef56fbb02 | -11.58397 | -50.14576 | 2026-07-26 05:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43e18a99-2fef-33da-91f1-1cfd4e841244 | -9.83711 | -62.21796 | 2026-07-26 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce2635ef-9c71-32ea-95c2-f4574f488d1a | -13.92638 | -53.8783 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36bda4a4-1b39-33c4-ae84-48a09e1cdddd | -13.93109 | -53.88206 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e33b6c6b-4c47-31af-9338-b9bd7ab183cf | -13.80237 | -53.86251 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b99e4d3-0334-3809-a4cc-d0ddc2a2317c | -15.81445 | -56.72528 | 2026-07-26 05:29:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3d7d11d-56ca-351c-87f9-4ca98e90c8d5 | -13.80275 | -53.85949 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87855106-5922-3dc0-8ac5-e08de239a9c6 | -11.73273 | -62.32977 | 2026-07-26 05:29:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efa73cf5-6e47-3e3f-87eb-d0fe1384d60d | -13.92602 | -53.88132 | 2026-07-26 05:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84a36ec6-5d19-3c97-b3e3-2ffcb5545851 | -21.28052 | -56.03148 | 2026-07-26 05:31:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd04d705-bf68-39b4-aa7f-f9968e7e224d | -18.49701 | -54.10188 | 2026-07-26 05:31:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 75d95a1b-3586-328d-a5ee-6aa48403834d | -18.49167 | -54.10144 | 2026-07-26 05:31:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fedfe47a-66d8-310e-a36c-328a89c01299 | -21.27991 | -56.03712 | 2026-07-26 05:31:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 577835a7-3840-3d19-8065-a4bd62f97b08 | -10.2713 | -46.7216 | 2026-07-26 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 16a0a45f-5283-3a7c-9b19-04c8c2b0881d | -10.271 | -46.7441 | 2026-07-26 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 10d1d237-775c-3965-9de0-5a72fb022a08 | -10.2903 | -46.7194 | 2026-07-26 05:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 7b5de830-be71-319a-a5c9-d3c09e5698a9 | -10.2713 | -46.7216 | 2026-07-26 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| be37404a-d836-3b80-ae77-d677aa2cf722 | -10.2713 | -46.7216 | 2026-07-26 06:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 9b5ef740-14d1-375f-bdaa-988e1c82a512 | -9.83923 | -62.21838 | 2026-07-26 06:16:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af5fc2df-1739-3902-9b05-19c95b679257 | -9.89323 | -67.02557 | 2026-07-26 06:16:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 620583d4-142f-367e-b80d-20cdb008e512 | -3.7211 | -48.87446 | 2026-07-26 06:57:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 61654195-a62e-392c-baa3-dfc00d2d34bd | -14.27911 | -53.38121 | 2026-07-26 06:59:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| afb5d860-db0b-3492-b30c-e2e7f0f11837 | -2.93686 | -40.87366 | 2026-07-26 11:38:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d50f7e37-3992-3e9b-b2ef-d54fcc25866f | -6.27032 | -42.52918 | 2026-07-26 11:40:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 797bea43-087b-3bf8-8b2c-7f4740cd5b4d | -6.27172 | -42.5189 | 2026-07-26 11:40:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 5a89c4b6-6f7a-3485-84f8-471e1b354852 | -4.91358 | -43.46998 | 2026-07-26 11:40:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4c7ba69d-e341-3fd0-8afb-322fbf4a9d55 | -5.93912 | -43.65771 | 2026-07-26 11:40:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f1e03f27-d3a7-373c-a165-37439fa6847d | -13.29018 | -54.27839 | 2026-07-26 11:42:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a6062fb9-dd89-34f9-b838-3e9044d96eb5 | -11.85862 | -50.22022 | 2026-07-26 11:42:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bc84b9b4-9528-3621-9c31-5998be61fad4 | -12.32594 | -47.1733 | 2026-07-26 11:42:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e28c003f-3205-3fbc-9171-f2e26a74b041 | -11.42905 | -47.50032 | 2026-07-26 11:42:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 69cec9aa-5632-3b81-a16f-34d4d21f59a9 | -10.26876 | -46.72587 | 2026-07-26 11:42:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c03f3053-97d6-36fb-b1a4-0ccf1e4e58cd | -11.49873 | -47.52703 | 2026-07-26 11:42:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e241b5bc-29f4-3464-b5ad-f8719cbbe6fb | -8.0827 | -47.27644 | 2026-07-26 11:42:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7ccd9c47-3938-3e2a-bfb8-df540513df8d | -11.42764 | -47.50985 | 2026-07-26 11:42:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e8604b9-e0a5-38bb-87c4-0fe0f9d0bf26 | -12.32729 | -47.16407 | 2026-07-26 11:42:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 20980f9b-cb94-3fdf-b828-f534402d8e77 | -13.26359 | -43.57059 | 2026-07-26 11:42:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f2e9a854-2347-39d5-8e3f-d97d024f38ee | -11.85654 | -50.23367 | 2026-07-26 11:42:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5d39724b-1c7b-304d-9d7f-0e9da9dcf74b | -11.4792 | -47.53331 | 2026-07-26 11:42:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 201a469a-1cd6-365a-8ccb-cb92eeec712d | -12.66991 | -48.21211 | 2026-07-26 11:42:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 07076d22-c042-3670-8ab8-ced530fc20e2 | -11.48057 | -47.52409 | 2026-07-26 11:42:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5733d9eb-7365-33f9-be29-fba717436ae1 | -11.43814 | -47.50164 | 2026-07-26 11:42:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 0a492a65-dbbd-3c8f-9f06-b1fb383afd7b | -11.15148 | -44.48181 | 2026-07-26 11:42:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 81ea64df-3067-3ee8-a272-5a6892a2e28d | -11.50782 | -47.52845 | 2026-07-26 11:42:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e26d272b-2ac3-35a0-9a4b-e83ae8d89f30 | -13.76264 | -42.6427 | 2026-07-26 11:42:00 | TERRA_M-M | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 547c161b-01b8-3a2c-afcb-768f851c8271 | -10.26352 | -40.61355 | 2026-07-26 11:42:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 1dc4aeca-f578-3293-8bad-ae974ee813a0 | -11.75816 | -47.26956 | 2026-07-26 11:42:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5fc1f78c-82fb-3307-a923-bfe15243fd4f | -10.2655 | -40.59818 | 2026-07-26 11:42:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 96ac4f1d-b3a0-306b-86dd-b51cf367abb2 | -17.81272 | -51.03231 | 2026-07-26 11:45:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b7ae0054-0169-39b5-9e32-0f0502d7a613 | -15.22333 | -50.85029 | 2026-07-26 11:45:00 | TERRA_M-M | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cabc5406-1578-3439-b81d-196566614a12 | -16.83866 | -44.18707 | 2026-07-26 11:45:00 | TERRA_M-M | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a23094e3-648c-35ca-ab88-269c74ce56a2 | -11.4944 | -47.5289 | 2026-07-26 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 7795f823-9542-3514-8690-702bf46ed07c | -11.852 | -50.2377 | 2026-07-26 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0fa71024-4b6f-300c-8b95-b7046d6c2205 | -11.4375 | -47.514 | 2026-07-26 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 90710a7a-f1c3-303e-a52f-5130f89156b7 | -11.852 | -50.2377 | 2026-07-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b62c58ff-2638-3c44-93db-2ca1b9103c3c | -11.8523 | -50.2161 | 2026-07-26 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 86b47b9f-b673-3bf6-9e3e-bba53c016b61 | -11.4375 | -47.514 | 2026-07-26 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c414a2c6-9dc0-38d0-bccf-744ef71129d2 | -11.4375 | -47.514 | 2026-07-26 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 22c037b8-88b8-3d2f-ad30-734781704853 | -11.852 | -50.2377 | 2026-07-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 8bca4dfc-4d28-3db8-b07e-857b6117123c | -11.8523 | -50.2161 | 2026-07-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 9a699eb9-a224-36da-a4b4-aa72f15b7dd3 | -11.4375 | -47.514 | 2026-07-26 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 46b4fe3d-a552-3777-b4e4-e93553421124 | -11.852 | -50.2377 | 2026-07-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 03ee07e6-45d2-39ea-87a7-c2e00fb9ba7a | -11.852 | -50.2377 | 2026-07-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| a606c430-6e46-3549-ae12-118928f8956c | -11.4753 | -47.5314 | 2026-07-26 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 20251d78-0b21-3c8f-90b2-e0dab59da38f | -11.8523 | -50.2161 | 2026-07-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 39eb2899-1b38-312c-9580-3de42da00857 | -11.4753 | -47.5314 | 2026-07-26 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| f191ffa9-65e3-342e-8eda-8fb656983956 | -11.852 | -50.2377 | 2026-07-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 33eb1a26-8522-3e20-8d4d-6bfda12b4ca4 | -12.6679 | -48.2148 | 2026-07-26 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |


[Clique aqui para ver as próximas entradas](README8.md)
