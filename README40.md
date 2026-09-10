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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bce6d5b-4dda-3a90-a807-f60723ee6240 | -8.08658 | -54.85008 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09d8688f-120b-398f-b8dd-4d7a82168d57 | -9.15442 | -58.3078 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f135cd78-2c08-3f9d-a70b-a8424ed3586f | -8.0895 | -54.85429 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e366f320-0c6b-3430-a83e-1b948e656142 | -9.16309 | -58.30909 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e49ff7fe-686d-3164-bcdf-1b9adef9790c | -6.8621 | -56.57248 | 2026-09-10 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd625aba-6cad-30d2-b368-1bef78e0dbff | -6.19038 | -55.2686 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69358379-2ca3-37d8-8c4d-913409d51a48 | -7.28448 | -70.01484 | 2026-09-10 05:48:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0371bf5-4c89-3b28-abdf-671cff7fb505 | -9.68183 | -63.43383 | 2026-09-10 05:48:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b7ceeb6-d1fd-3e36-b665-08d50693c022 | -6.55134 | -62.89199 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8e540617-b4bb-3a6e-8f0a-266612364205 | -5.28011 | -55.96333 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf8f6a4d-8255-3eaf-b63f-82e410d64eb1 | -6.79074 | -58.90055 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82a45cb9-aa18-3c3c-9896-3ccd75303a3c | -6.78824 | -58.88945 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a06c9450-96c2-3495-90f1-dc53a573c82e | -9.15816 | -58.31264 | 2026-09-10 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4caffe99-0b80-3778-8287-b83272da39d9 | -6.77128 | -58.61586 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a891abc-11f0-3d53-9807-1936af4844a5 | -5.28086 | -55.95814 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b1dd8a9-d17e-3994-acfc-28488fa90f08 | -6.79177 | -58.89353 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df155345-3a68-32f2-aa21-1fac2e19963b | -6.79581 | -58.89409 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18a9f566-3bda-319f-b913-c9495b13041c | -6.82322 | -58.98642 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96c6fd8f-834c-380f-ad77-e02af36793a2 | -8.99845 | -65.40459 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd25475f-dd39-31e6-9643-ce101acac0c0 | -6.50904 | -58.37848 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1964428c-5356-3d60-b3b0-27c587c9e120 | -6.7862 | -58.90346 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 023b5407-c475-3fb6-8d4a-f8665507932c | -6.81585 | -60.13546 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56ab93da-abe1-3aa4-b748-a6f6d21cdfc9 | -9.74397 | -58.4098 | 2026-09-10 05:48:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d638142e-0df4-3891-b14f-ac8969276df1 | -7.80288 | -67.14445 | 2026-09-10 05:48:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73e95b72-70fb-34f5-9c61-af6fee59713d | -6.82244 | -58.99163 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0adad938-90e0-3329-8b3b-e91e5ec56531 | -4.82817 | -55.76637 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| add3ef94-ece0-33af-9f8f-9957385d8ced | -6.79529 | -58.89761 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa24d5fe-3fce-3e63-ba74-af243bd64a14 | -8.82387 | -63.81392 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37cc971a-106e-36aa-a0f1-eb70f7db0ec3 | -8.89069 | -61.44078 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e3c8a9b-aaa1-329e-ab8a-1fa2789c4d74 | -9.00034 | -65.40088 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38c2004e-a8be-3a2b-a1e8-6dd40fedb439 | -9.08301 | -67.86514 | 2026-09-10 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9543f44f-5175-35b3-84a6-357e38ca88f0 | -9.01145 | -65.41734 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0969e920-7c76-33ab-b2fb-2a5a80410c12 | -8.66437 | -66.55959 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36341384-995c-358b-95bb-56053f89a7af | -8.08996 | -54.85098 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7eb00b17-96fd-3285-b10f-7f3ea487a097 | -6.7602 | -58.96418 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b27ae89f-a7df-38d0-be71-882dd1d5024f | -8.06323 | -61.27441 | 2026-09-10 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a250fdc2-02b3-391f-a16f-8fc8d0770ddd | -6.78268 | -58.89935 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d54c9fdd-fdbc-3f16-bbfd-23c064b6f758 | -6.54522 | -62.9091 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2bd8cc4-5a61-3fbc-b5f7-fc27d2732a66 | -5.9213 | -63.47611 | 2026-09-10 05:48:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feb2be4b-ca81-3554-b513-c2bb47fc14f5 | -8.89549 | -61.43313 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be3e7da3-6796-3d71-bcca-85f5a828bd99 | -9.02997 | -65.40938 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab8fb4b7-c559-3819-b91c-df7c6209cfd4 | -7.24575 | -59.52364 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ca8d4fa-5b6a-3367-8c49-a4c11304d403 | -5.36937 | -56.02403 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11157992-9cb5-3db3-a8c3-03d3874d89d7 | -6.4611 | -62.86355 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15af2347-000c-394d-ba09-d701df8c42d6 | -5.37015 | -56.01884 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 842df632-222b-3a75-a799-cd5634ceb28e | -8.36762 | -62.92862 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ed86f15-bfa6-34d4-b1d9-f1b0d454d31b | -6.46445 | -62.86408 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56cccda5-9a81-3333-aacc-04620fff0c3c | -5.37334 | -56.02736 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f006d88-a1df-3fdd-9c04-c40ab6161187 | -8.15579 | -62.89996 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35fbfb17-ea00-3e77-8c1f-ed44d1e9222f | -9.1401 | -64.4096 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9746b6cc-eff2-3e11-909a-7c2ae33da239 | -8.99976 | -65.40444 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1c72395-4fd5-3f4f-8c53-d604efe47449 | -6.76664 | -58.61883 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ecaa9f-2135-370a-86a2-6c434fee4b83 | -4.85998 | -56.00837 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 195c592b-17d2-3489-b091-35ed32550710 | -6.80419 | -58.94885 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00d692c1-d001-3cee-a359-66f559ff7081 | -8.71199 | -62.43737 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da9f277c-700f-300a-91f0-f37e0f4eb6a0 | -6.77236 | -58.60858 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e86c53-6cac-3d11-a9ee-56dbd31660fb | -9.03889 | -65.41817 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6cf814f-15b2-349f-92f0-7d1f616ba2f6 | -8.82666 | -62.48492 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8895bb7b-e809-3061-b173-9657116b957c | -8.21816 | -62.81703 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 274beee2-b191-3646-8d40-34a84b361c8e | -6.80017 | -58.94828 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1355a23-3d65-3b13-aef7-78abc8c80fce | -6.78876 | -58.88593 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3fa0b31-2842-3a16-9338-5b341a2945ff | -8.98396 | -65.38755 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f50cb3d-8e16-3f9f-a6cd-1d71d27ae69f | -8.99338 | -65.41475 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a081fc61-ef96-3ea2-a7b2-bc93a00b7f6c | -8.90204 | -61.4383 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8995416f-c681-3f4d-a5e0-1f7b93c6ebfd | -5.91852 | -63.47211 | 2026-09-10 05:48:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67beed9a-9a0a-3c8a-a69c-2e9f2f8685fc | -8.89365 | -61.4454 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 108ce43e-0d19-3e92-b389-32c78923b48d | -9.20082 | -65.77699 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f869b7c-c341-30d4-bc09-788ee65596df | -6.50017 | -58.38102 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1faa6c2-8b9a-31df-ad8b-2d377a319894 | -6.95712 | -59.76355 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d45a925c-a5d2-3958-bc9f-0aa45478554a | -8.73025 | -62.38657 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4416494-ddb6-3138-979e-858038864867 | -8.88955 | -61.42386 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 443f4825-3b27-3015-a604-379fbe8f62a6 | -8.62613 | -66.50974 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65a96a2-4dcb-3720-9091-78d9fc99ac3c | -9.21617 | -63.64518 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e6675aa-5c46-38d3-bc32-583a04073dbb | -6.77074 | -58.61943 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8029d450-7f27-391a-a03e-36967074a892 | -9.21562 | -63.64872 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46c5b469-a488-3bc4-a2c7-120b8562bb2d | -8.0857 | -54.85671 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b965940a-0e3e-30cf-b352-f134076d1d66 | -9.04282 | -65.41515 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 671b3f13-08d3-38e5-9839-93c007edef8c | -6.62538 | -58.37937 | 2026-09-10 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a7719de-bb91-31b2-b831-0e76c0847183 | -4.83302 | -55.76706 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37e4f648-a3fa-3414-8225-7af8e44b88f7 | -8.98674 | -65.39168 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b3f165f-f1da-30e4-a55b-e53bf667086f | -6.79125 | -58.89704 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2944a38a-8585-3714-a82b-5df2b731144e | -6.77718 | -58.88054 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c3ce015-82ab-396c-b58b-03717c80b3c3 | -6.50319 | -58.38914 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd23029a-d975-3e5e-a1ba-57d5b1b5fbf1 | -8.08527 | -54.86002 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7eb10a40-0091-34cc-8d7a-96c17e342822 | -9.12488 | -67.84094 | 2026-09-10 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d2daf4c-e9fe-3e06-a02a-cb5c3cb86af7 | -9.04225 | -65.41872 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38a1c473-d6bb-36b9-a744-50da4ebad843 | -8.98254 | -60.60695 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244e2e04-9362-36a2-9c87-989cc6c31b7b | -4.86323 | -56.01947 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fcfe7feb-f996-3dd4-89b5-369dfaea8a43 | -8.98339 | -65.39112 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ff35bd9-dc83-3745-8d68-606fbc00356e | -9.21896 | -63.64924 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 956890ac-9363-3238-a716-54b4facfacd6 | -6.55302 | -62.9031 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35134ab9-275d-3124-9b6d-220de8bca675 | -6.7837 | -58.89236 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75973a66-05ce-36b0-8dcc-8dbe340de856 | -8.90265 | -61.43422 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47121a2d-e345-3419-a63c-eb9d8ea24df0 | -4.19094 | -59.95478 | 2026-09-10 05:48:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67a64a88-42b6-3023-93c2-a67f44ace2b6 | -7.24258 | -59.5181 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 57eeef20-aed4-3ed2-aeeb-42c83737aa84 | -8.08362 | -54.85687 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6fd29760-6f71-3753-9a10-879a95d69218 | -8.98666 | -65.41366 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef4e91d-5cd1-38bf-8bd4-9e25045d9ead | -6.77564 | -58.89111 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39320f8c-5630-3555-bc26-a3894c3a2bfa | -9.21951 | -63.6457 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ad4605-3032-3efb-95db-17d246333e95 | -6.77181 | -58.61227 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README41.md)
