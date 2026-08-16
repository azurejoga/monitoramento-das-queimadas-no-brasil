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
| cb82f5cd-ae3b-3dae-a579-61d7cf91cf3e | -8.9787 | -60.5156 | 2026-08-16 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 147.0 |
| f8e52a84-370d-3d33-be77-66fbd90d4db5 | -6.6938 | -58.942 | 2026-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 54b64c94-12f0-31fb-a782-2d0879bfbab2 | -14.3923 | -51.8867 | 2026-08-16 03:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ba567725-65dc-3dc4-aa0b-b08a35539a49 | -14.3919 | -51.9081 | 2026-08-16 03:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b796fbd5-6c93-304a-9f12-b49518f7c71b | -6.6194 | -59.0609 | 2026-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b664ea2b-69fa-3eef-a597-8c6857d2b67a | -6.7123 | -58.9412 | 2026-08-16 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| b6b5f967-0674-3368-a9cc-942627e25a1c | -6.6377 | -59.0795 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 5d939bff-b05b-3982-8223-cc68ac18afff | -6.6937 | -58.9613 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 60f2f066-4640-339b-88f8-0ac2de3a81cd | -8.4275 | -62.676 | 2026-08-16 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 3024b98d-caa4-3d6e-84f7-fc426eaad844 | -6.8387 | -56.4344 | 2026-08-16 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5edd9965-3d56-3c26-877c-84587d0f6866 | -8.96 | -60.5358 | 2026-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 3f14521c-9ed1-394c-994a-860ae730e6b1 | -8.9601 | -60.5165 | 2026-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 199.2 |
| 4274554c-5148-30f8-ba2c-6b935597a919 | -6.6378 | -59.0602 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8f6b2dd1-aa7a-3d51-857c-79b4bb2e1898 | -6.82 | -56.4551 | 2026-08-16 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 736f8ea7-f8d4-3f28-844a-402937431523 | -6.6193 | -59.0802 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 78b5a69c-7e9c-38f7-95fd-67c70d0889ff | -8.446 | -62.6752 | 2026-08-16 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| aecda5ca-d5c6-32fd-8db0-2d60494d8d55 | -6.8597 | -58.9738 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f516683c-9f95-3b03-8dbf-4bb61499dcd4 | -6.7124 | -58.9219 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 316b647a-64fd-3ef8-b178-beb844536c39 | -6.6938 | -58.942 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9b483d84-c3be-3d10-9a65-ce447e00cf1a | -6.7123 | -58.9412 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 1f104bb6-9d8f-3516-8d87-a7650c348b59 | -8.9415 | -60.5174 | 2026-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 432078d4-4773-398e-af74-39e5c9fe8322 | -6.6194 | -59.0609 | 2026-08-16 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 4fec0623-d4cb-332d-937e-0b9d09c4ebfc | -8.9414 | -60.5367 | 2026-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| fbaf40a5-0e0e-3b92-85dc-052165dcf5f6 | -8.9787 | -60.5156 | 2026-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 38011dc3-c07c-3c0d-a631-5a15f02de0ee | -8.9785 | -60.5349 | 2026-08-16 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 9ba213dc-ab92-31d7-a715-ff68ba29e820 | -8.4275 | -62.676 | 2026-08-16 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 221bc860-2407-3764-bb67-8af2fee859c1 | -8.9601 | -60.5165 | 2026-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 3d9decfb-e702-396d-b5ec-f62666136f02 | -8.9414 | -60.5367 | 2026-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 68d91a21-e65a-31a0-a7e7-cd0bf2a2982f | -6.6938 | -58.942 | 2026-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d1b45863-1ea7-3e81-840e-c0dae190ef88 | -6.7122 | -58.9606 | 2026-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b6e7bf25-f0b8-31ea-b667-c3585dd3d761 | -8.4273 | -62.6949 | 2026-08-16 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b43bd187-8141-3d40-9cf7-895c3cc924eb | -6.7123 | -58.9412 | 2026-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 10d1b2a3-e20e-3cc9-b430-3a2e83e03288 | -8.9787 | -60.5156 | 2026-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 912256ed-c807-3d22-aade-62d9a69a1165 | -8.446 | -62.6752 | 2026-08-16 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 10a4a291-0c5c-3eb5-a652-9506ee8289fb | -6.8387 | -56.4344 | 2026-08-16 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 7eb37cff-24f9-30c1-a161-309356937cf7 | -6.6377 | -59.0795 | 2026-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 39cd72cd-8861-3a27-9ca2-ad07f3927daa | -8.9785 | -60.5349 | 2026-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| d42888ad-7605-3178-b4ac-c9c0ae42b83d | -6.6194 | -59.0609 | 2026-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 68f9c486-9559-3536-b3b9-5d282d7312de | -6.8385 | -56.4542 | 2026-08-16 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 2a983972-7db6-3d84-b83e-617f34c1f78d | -6.8597 | -58.9738 | 2026-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 81ec11d5-85da-3fb2-a606-ba5c8db5e389 | -8.96 | -60.5358 | 2026-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 9e252da6-6048-3b36-84c3-4db5c8265bad | -8.9415 | -60.5174 | 2026-08-16 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| dd891ce1-52e8-39b8-90ca-79d6c5969275 | -6.82 | -56.4551 | 2026-08-16 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 445c259d-95ff-34cc-b1a3-3ea13d7fb742 | -6.6193 | -59.0802 | 2026-08-16 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 83406f4b-b271-300b-a9d3-37e488548dce | -6.99959 | -41.43166 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 80de9829-9bb8-3122-bd12-ff4e1b515b94 | -4.10675 | -42.50157 | 2026-08-16 03:34:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4dbdf66d-3a82-3627-aafe-48139671563b | -6.93013 | -43.63601 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d706b9e-b9dc-3553-8179-617724880cea | -7.0062 | -41.42899 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b809093-746f-38df-94a0-b18a729e065f | -7.99469 | -38.32972 | 2026-08-16 03:34:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 82db40ef-1396-3e5f-9a16-1a1f7a95996c | -7.01217 | -41.4297 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| deae3cf5-21f2-33e2-af45-08b3b58662af | -6.92336 | -43.63482 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b012fc47-762f-3d4e-b9d8-6c7c456a0311 | -4.10475 | -42.51299 | 2026-08-16 03:34:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c328ec0c-081c-356b-b98a-ea45c8e1c7eb | -6.9289 | -43.64241 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8129db3c-7265-3497-be6b-f8dd90ecc698 | -4.11336 | -42.50272 | 2026-08-16 03:34:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7844caca-6737-3299-97b9-81061901b5d1 | -7.99478 | -38.33089 | 2026-08-16 03:34:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 70399eb1-4bb1-32f2-9616-afe64ab3f1dd | -7.00548 | -41.43282 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ecbcf7f5-6f5f-333c-818a-1ec794468a80 | -4.10015 | -42.50039 | 2026-08-16 03:34:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ec33484c-b841-3f42-bc6d-bef091bded82 | -6.99629 | -41.43308 | 2026-08-16 03:34:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9240830-8127-3dd8-929c-7179146e4fbd | -6.92852 | -43.63469 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a99c16a-fb87-34f1-87d8-0b8183fc8779 | -6.92175 | -43.63347 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a09691d-1990-337e-89fc-47237ed9e313 | -7.01799 | -41.4312 | 2026-08-16 03:34:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6aefdc12-2718-3bbd-b3b9-e25e85e8160c | -7.00875 | -41.43169 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb18d565-c3b5-3045-86d2-02321bd055df | -6.67641 | -43.99931 | 2026-08-16 03:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1d6c2f83-2d87-3025-acfc-c1565b477ff0 | -4.09255 | -42.50492 | 2026-08-16 03:34:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 9bc2c51a-f3a7-32af-a265-b7d06f476385 | -4.09355 | -42.49919 | 2026-08-16 03:34:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 370f1216-48ba-396f-992d-051450e6aedb | -7.00214 | -41.4345 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fceb4e68-d700-3ab0-9769-8dee94489757 | -6.93409 | -43.64242 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eeb6a4ee-0d38-380a-a3d4-ce9346b52a99 | -7.21936 | -41.53426 | 2026-08-16 03:34:00 | NPP-375D | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a4d15694-3ef0-3195-8db7-eeb35d8c827b | -6.99895 | -41.43509 | 2026-08-16 03:34:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a1cdda05-3fc8-32ad-be3c-6068db2194fe | -7.22525 | -41.53551 | 2026-08-16 03:34:00 | NPP-375D | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e583023c-fbb7-3b39-9f7d-2994b8e26f5d | -6.92735 | -43.64107 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07ccc936-43bd-3895-9c51-199d4b87cfbd | -7.00148 | -41.43816 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2d6b7492-1f42-38a9-9de9-1cc7c66d47c2 | -6.93565 | -43.64375 | 2026-08-16 03:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 304afa59-2032-36cf-b71f-b79cb5d5285f | -6.67773 | -43.99237 | 2026-08-16 03:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7078920e-8c3a-3cbb-a8c8-1975fa89260f | -7.0028 | -41.43086 | 2026-08-16 03:34:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 08c9fbc7-7306-3c95-ba9b-434c85997ebf | -10.52172 | -44.85573 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b41f62a-5ba0-3a0e-ba77-2ede813afd02 | -12.64323 | -43.90488 | 2026-08-16 03:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1acbbdc5-4106-3c45-a387-aeb046d37f74 | -12.23733 | -43.14482 | 2026-08-16 03:36:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 202d1e8b-991e-34ce-8069-86bb7edcb798 | -7.2614 | -44.69967 | 2026-08-16 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62595f87-5a41-3e30-b6b6-e92371311d6c | -12.23666 | -43.14336 | 2026-08-16 03:36:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9b3dc863-7072-3cca-b346-71a8360a04f2 | -10.52038 | -44.86216 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 792f70f0-4cc1-3f9b-b443-77fe2857a767 | -11.90653 | -45.97812 | 2026-08-16 03:36:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d24162c-aa26-359f-8195-e3decc36570b | -10.53648 | -44.8514 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e08e634e-d194-3ecc-b772-3c270f3fd01a | -13.38178 | -41.34586 | 2026-08-16 03:36:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a82b7ca9-4fdd-3bf6-8565-daa159b3e4c9 | -12.23809 | -43.14114 | 2026-08-16 03:36:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 968ce868-d971-3c63-882d-a226f018fc1c | -12.65048 | -43.90136 | 2026-08-16 03:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8779e20-a1f6-37ee-91ab-6dd8d2f6c358 | -12.6473 | -43.89887 | 2026-08-16 03:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca186d0-15b4-3758-86c9-3e67851b9453 | -10.52836 | -44.85643 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c83eb5f1-2247-32fd-aa28-5828bed45276 | -10.51469 | -44.85368 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c21c4a9-ad7d-3475-afc6-0adac7f8ce80 | -12.23739 | -43.13972 | 2026-08-16 03:36:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 353b8c3b-8f99-354c-90dd-90b833daa865 | -10.52856 | -44.85709 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3258cf9b-09db-3cc8-8cc4-b395f1d0aef1 | -13.37679 | -41.34792 | 2026-08-16 03:36:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec688d8c-3297-3598-8dbe-e8f7f720c93b | -12.6463 | -43.9038 | 2026-08-16 03:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a6db665-e1ce-3cde-869e-0ee66511ee01 | -10.51487 | -44.8544 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b7f049e-fbe2-3775-8a40-d67ba6e97c94 | -10.53521 | -44.85775 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab1b42fa-4221-3c7d-8fb2-a8e8567d5296 | -7.27534 | -44.71574 | 2026-08-16 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 313e109e-f02c-36bf-a2d9-55387d822971 | -10.52153 | -44.85504 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| face9cf8-4506-340f-bfc2-eee1c0b15c46 | -10.52988 | -44.85068 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3a4978f-e03e-370d-bb7a-10268f4c74b2 | -10.52283 | -44.84856 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e06b605-bc0d-371a-a4c4-e9b565b36320 | -10.53541 | -44.85838 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README8.md)
