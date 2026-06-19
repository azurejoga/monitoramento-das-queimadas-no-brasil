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
| 50693c3d-0abd-302f-acb0-7d0c1fa435d6 | -22.7859 | -49.3406 | 2026-06-19 00:00:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c634e9da-6939-35fa-b996-2d12e500f4d0 | -4.3588 | -47.7636 | 2026-06-19 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| bb0ab9cc-dd0c-37e2-a6ee-b811937c4f39 | -12.8548 | -44.3625 | 2026-06-19 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 03221f72-8901-3ebe-b1e0-c215e3a04db6 | -12.8741 | -44.3593 | 2026-06-19 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.7 |
| d45b0115-366e-3d8e-b756-a69ac7d1f991 | -4.3402 | -47.7645 | 2026-06-19 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8fa36f2d-b659-3b5e-ac36-836b35f0209f | -7.8037 | -46.4458 | 2026-06-19 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f90ab1e9-4ba4-337a-9c31-542e8089de67 | -12.8935 | -44.356 | 2026-06-19 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5573c398-16a4-3a1f-bc31-35b968dc0143 | -12.8736 | -44.3828 | 2026-06-19 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 57001380-a39a-350b-bb4f-34fcd92a8705 | -4.3588 | -47.7636 | 2026-06-19 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| f8a21826-56b8-3e41-afa3-696b268d320b | -12.8736 | -44.3828 | 2026-06-19 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| ceee43cb-9ab9-35ad-b453-a6e70843adbc | -12.8741 | -44.3593 | 2026-06-19 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 7051366d-64d6-3298-bb06-3fd46e34a964 | -22.7859 | -49.3406 | 2026-06-19 00:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8b0f0101-1334-38d6-bced-2dded9198b14 | -12.8935 | -44.356 | 2026-06-19 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 55c803bd-5fcf-33a4-86c6-41720a2c8430 | -12.8548 | -44.3625 | 2026-06-19 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fc8efed8-64cf-3922-ac75-85bb8057e1af | -4.3589 | -47.7418 | 2026-06-19 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 10ab51fe-4062-3178-8c2e-18e306813035 | -4.3402 | -47.7645 | 2026-06-19 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ee711767-c1c9-3d68-bd47-67820485d816 | -12.8741 | -44.3593 | 2026-06-19 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 6bffc876-728d-3bdd-8129-7473191207fe | -12.8736 | -44.3828 | 2026-06-19 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 75fb7430-83d7-3033-b557-c85472e0e2fa | -4.3588 | -47.7636 | 2026-06-19 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 2ab046cc-fb77-3396-8362-f86d56d14dac | -12.8935 | -44.356 | 2026-06-19 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 197a2f5a-d2ce-365b-8504-17e862c2ec47 | -4.3402 | -47.7645 | 2026-06-19 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| cf8587a2-7276-3874-8b45-790274a37f12 | -12.8548 | -44.3625 | 2026-06-19 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 332e3fac-9251-3b2a-84d0-e8976a448129 | -12.8741 | -44.3593 | 2026-06-19 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 5aa898cf-a744-30d2-a6ff-9f939e2582b8 | -12.8935 | -44.356 | 2026-06-19 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 12149612-8c09-3efd-8add-29a1c630657c | -12.8548 | -44.3625 | 2026-06-19 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 059a4f42-d91f-3c05-82e6-08f45cdd1915 | -12.8736 | -44.3828 | 2026-06-19 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 96a642fc-30c2-375c-999b-40ef9055220f | -4.3402 | -47.7645 | 2026-06-19 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 926950b4-bbf7-317f-8319-6348e3ac96a5 | -12.5003 | -43.7621 | 2026-06-19 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| fb6ac0b0-c45b-3b1c-8335-25ca572a1bf6 | -4.3588 | -47.7636 | 2026-06-19 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d382c375-0f64-3832-b56b-a90bba8a4a1f | -4.3588 | -47.7636 | 2026-06-19 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a1952c18-dbee-3135-968d-18dabd49841b | -16.1974 | -49.9737 | 2026-06-19 00:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 5df4a0db-a836-33a0-af21-6a2857c44fd3 | -16.2171 | -49.9705 | 2026-06-19 00:40:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 8a86093d-cf61-3f56-ad17-f1ec48c94c95 | -4.3402 | -47.7645 | 2026-06-19 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4fbc9cc7-9108-3b5d-a32c-603ea2fab1a1 | -12.8548 | -44.3625 | 2026-06-19 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 6fd6fdaa-0baf-3bb1-bc73-0d2cffb454d4 | -12.8736 | -44.3828 | 2026-06-19 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8b277aa9-22eb-3da5-bdac-44458887bdef | -12.8741 | -44.3593 | 2026-06-19 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| b3a916e1-0321-3c64-b70a-e365851aa5af | -12.8741 | -44.3593 | 2026-06-19 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 18e6347b-d5bd-3814-9507-8d8978049f5a | -12.8548 | -44.3625 | 2026-06-19 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| f6b5041c-1847-35ea-b76b-adcf2a6fdb05 | -4.3402 | -47.7645 | 2026-06-19 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 908d1b89-7901-3ba2-af3b-303b8d36782c | -4.3588 | -47.7636 | 2026-06-19 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 39c4ca1d-a035-312a-82f7-e37e3ab7a470 | -12.8736 | -44.3828 | 2026-06-19 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| e129277c-68c8-3cf5-aeab-45b52b7f4737 | -12.8548 | -44.3625 | 2026-06-19 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 43cf0ec4-6fcd-33dc-bd4a-50750a7ab2df | -4.3588 | -47.7636 | 2026-06-19 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e6532429-6780-3294-8172-ecf574b18291 | -12.8741 | -44.3593 | 2026-06-19 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 7d06f336-f318-3902-92a4-51fbfe00d566 | -4.3402 | -47.7645 | 2026-06-19 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8e14333e-408e-3a11-b372-8ef30b939631 | -12.8736 | -44.3828 | 2026-06-19 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 722a643f-b83e-3a67-bbcf-a4216ce07f35 | -12.8736 | -44.3828 | 2026-06-19 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 7ae38390-8ea3-3f44-9cd6-01b11fc8818d | -12.8548 | -44.3625 | 2026-06-19 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 68dfb52e-25d6-31e3-819b-b564217a2755 | -12.8741 | -44.3593 | 2026-06-19 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 15a999dc-b7cf-3c27-b60e-4b49856cc701 | -4.3588 | -47.7636 | 2026-06-19 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0a08480d-b560-31d7-826a-3ec034eddb55 | -4.3588 | -47.7636 | 2026-06-19 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| ef8b4e8f-d4d3-3afb-8ef4-e07ef52dac17 | -12.8548 | -44.3625 | 2026-06-19 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2bd37faf-e6cb-3f91-ac14-fa036cf402f3 | -12.8741 | -44.3593 | 2026-06-19 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 2d485dfa-c855-3485-9258-dd6aaac1e9b7 | -12.8736 | -44.3828 | 2026-06-19 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 9455218c-f5d1-3834-a827-2ebdf90144c5 | -9.01431 | -63.54884 | 2026-06-19 01:24:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 21b523d9-864f-3520-a53c-536ff5e6ce01 | -9.01873 | -63.54238 | 2026-06-19 01:24:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| affaab2a-3125-3c91-9539-922d58b7a8cf | -4.3588 | -47.7636 | 2026-06-19 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8ee6e9f3-db14-357d-b3cc-19883b930364 | -12.8935 | -44.356 | 2026-06-19 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 2574a0d7-f760-3320-82a7-3433032b0b22 | -12.8548 | -44.3625 | 2026-06-19 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 626ed2f8-e65f-3aaa-9aed-93ac5e5cdf73 | -12.8741 | -44.3593 | 2026-06-19 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 99dd5cf1-12bf-3a59-bc3d-4036086872a2 | -12.8736 | -44.3828 | 2026-06-19 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 539bb370-83ff-34ab-9dfa-65264152ddf0 | -12.8736 | -44.3828 | 2026-06-19 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| a5d1b488-3ecb-33bc-9149-a43f166ae5fe | -12.8741 | -44.3593 | 2026-06-19 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 94d93030-fb67-3f89-a83c-f2ae6db30307 | -12.8548 | -44.3625 | 2026-06-19 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ce093d1e-add6-3928-8d24-aab272a89cd0 | -12.8548 | -44.3625 | 2026-06-19 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 069c6b7b-7855-34a4-9ade-aea2f3af3453 | -12.8741 | -44.3593 | 2026-06-19 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 167.2 |
| a5a8465f-d9ee-3b55-bcac-e02825e716d0 | -12.8736 | -44.3828 | 2026-06-19 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| a0dc0ba7-3025-3262-b637-274cee56e991 | -12.8548 | -44.3625 | 2026-06-19 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 820653f6-8f2e-3a81-87af-eded6bff88a0 | -12.8736 | -44.3828 | 2026-06-19 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| c28112b5-cd5c-3743-8488-23f53029f31a | -12.8741 | -44.3593 | 2026-06-19 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| a803ccf6-5377-380d-bb54-f7a46d28309b | -12.8741 | -44.3593 | 2026-06-19 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 0c5fe0d1-3e35-39ee-9cbc-8c558124bd44 | -12.8548 | -44.3625 | 2026-06-19 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 926de9a0-5d47-3f1c-a224-c297607dcb50 | -12.8736 | -44.3828 | 2026-06-19 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 084c2a8b-189f-3bf2-82b2-fa797df5909b | -12.8741 | -44.3593 | 2026-06-19 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 57d5e835-5714-3977-9a1e-bf42239fbffa | -12.8736 | -44.3828 | 2026-06-19 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| d5ecbb41-3b76-30a2-b00a-9a2fbefa1618 | -12.8548 | -44.3625 | 2026-06-19 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ac6a9de5-4090-34dc-a389-ff3c64c4bd5c | -12.8741 | -44.3593 | 2026-06-19 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| f9647945-7144-3e6c-ae75-f2fb711914bd | -16.0342 | -43.4224 | 2026-06-19 02:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 155569e6-da69-3a4b-b22a-8eb327ded4f8 | -12.8736 | -44.3828 | 2026-06-19 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 4ba98fda-b22c-316a-87e4-1387fcd6edf0 | -12.8741 | -44.3593 | 2026-06-19 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 3439be6f-a6d6-3cc2-97d0-35211668d381 | -12.8548 | -44.3625 | 2026-06-19 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| d83d9f7b-7b91-36f4-9048-fb69bd013657 | -12.8736 | -44.3828 | 2026-06-19 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2d79e147-400c-3c0d-a501-62980a59b227 | -12.8736 | -44.3828 | 2026-06-19 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| dbacdfa2-62a7-39b3-9e5f-2bfc929810b7 | -12.8741 | -44.3593 | 2026-06-19 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 9a326e7d-f67e-3e57-8832-72192b7345a7 | -16.0342 | -43.4224 | 2026-06-19 03:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b6e82c86-b7f0-3327-a72a-fcfbf861f094 | -12.8741 | -44.3593 | 2026-06-19 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 6d826d9d-65b7-3d7c-bcdd-e3246d061b5e | -12.8548 | -44.3625 | 2026-06-19 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c2f83a83-1a7a-35dc-b55e-6119f4b7a21b | -12.8736 | -44.3828 | 2026-06-19 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 05bd0b98-9de6-3164-aa9d-6fbea8b1af80 | -12.8736 | -44.3828 | 2026-06-19 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 1e15acd7-54a4-3f5e-bf6b-714154bbd5c3 | -12.8548 | -44.3625 | 2026-06-19 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d43e8ed4-f06d-3be2-9dad-33ac90a7e6c5 | -12.8741 | -44.3593 | 2026-06-19 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| d37d5a20-0c2e-3041-a467-b004e96e6367 | -16.0342 | -43.4224 | 2026-06-19 03:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d708431d-a389-38b9-94ff-3c797a59360a | -5.51898 | -37.48445 | 2026-06-19 03:19:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 352815ca-b8f5-3e55-9888-0bbc76bf7e5d | -5.51827 | -37.48838 | 2026-06-19 03:19:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d854ad88-5716-3cb5-9b3e-1db574429c4d | -12.8741 | -44.3593 | 2026-06-19 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 59aa3372-fa5c-388a-8a0c-03c8e6cfb928 | -12.8736 | -44.3828 | 2026-06-19 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 009a7f4d-c263-339f-931b-ceccc2bc5ef2 | -7.47227 | -38.95911 | 2026-06-19 03:21:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c34f626b-bef3-305a-98fb-9c42c844b038 | -7.47838 | -38.96012 | 2026-06-19 03:21:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1fdaefa7-d1d3-3105-b493-0d39509f5451 | -7.47871 | -38.95794 | 2026-06-19 03:21:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ddf5ce39-31ba-3fc2-ba22-ef6e5b48190e | -7.47261 | -38.95689 | 2026-06-19 03:21:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README2.md)
