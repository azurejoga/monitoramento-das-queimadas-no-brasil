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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07efaeba-8a7d-33e4-8c4e-637fc209fd91 | -22.09043 | -46.9806 | 2026-09-30 04:00:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| adf44ca6-e0a4-36ed-b797-171878f6dfcb | -20.80713 | -47.16909 | 2026-09-30 04:00:00 | NOAA-21 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e78aa627-c32e-3372-aab9-6660a29dce5a | -20.08197 | -45.35691 | 2026-09-30 04:00:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db9fb163-4cd0-35a2-bb77-1279bed5102f | -18.26926 | -53.05342 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 55f7a95b-cbf6-3b60-b146-506c54408126 | -21.0593 | -47.03604 | 2026-09-30 04:00:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0996b5d9-fd08-3617-bc4a-3f40b012c5e0 | -20.45266 | -45.19781 | 2026-09-30 04:00:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 937a28f6-1a17-350b-a408-2e7f7d5d1666 | -21.10713 | -45.79865 | 2026-09-30 04:00:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9a1283a0-a50f-3851-b161-11d16dafae5b | -18.28126 | -53.05614 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae17515f-d233-3579-9c3f-797ca6de8595 | -20.4048 | -42.42965 | 2026-09-30 04:00:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ac5267a-a439-347f-8156-3fad88cce2d6 | -18.26134 | -53.05361 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 967502fe-ca7f-35aa-89c2-8bd85a798eff | -21.79767 | -48.10905 | 2026-09-30 04:00:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec9cae9c-cb42-38fd-b2f8-cb8783f6be6d | -20.07834 | -45.35616 | 2026-09-30 04:00:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8289335-08cb-3e5f-a552-f34ea176d07a | -19.58071 | -46.91202 | 2026-09-30 04:00:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10586474-bd86-3cff-98e4-c8a4b89b147e | -18.27351 | -53.03462 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8409582-2daa-3df0-bcf0-04a7ef19a28e | -20.50739 | -49.62825 | 2026-09-30 04:00:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 099e4bb6-363d-3a4a-a661-ef109252527f | -18.28032 | -53.05322 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e6dd7ef-d9ff-3d80-b087-7601046e77e8 | -18.27526 | -53.05481 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9c5b9479-3a24-34eb-90bb-109b34c19baf | -18.27245 | -53.03933 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 827852ab-6a3c-3193-a332-0b4a44d6e4ff | -20.79549 | -45.35097 | 2026-09-30 04:00:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e8edf29a-eb61-3774-81de-f04ba0820bfb | -18.27144 | -53.03625 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afe3c909-1178-3039-938f-90474867649e | -20.74369 | -46.38291 | 2026-09-30 04:00:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 664aaea8-8c0a-3a1f-80c0-35d66630eedb | -18.27639 | -53.0424 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31e225b2-abcb-3564-9f13-98b29b2f407c | -21.38537 | -45.31483 | 2026-09-30 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 7eca0130-e408-318f-b584-f21d1f590fc1 | -20.7941 | -45.35263 | 2026-09-30 04:00:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c8f03820-d741-3585-b580-157c1080cdeb | -18.28335 | -53.04684 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d474e17f-fa2f-3557-953d-683778ee000c | -18.2564 | -53.04743 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 27978f26-08ff-33df-91ea-b4b2d83b96a1 | -18.28935 | -53.04819 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a181a6c5-c7be-3cb5-ab06-07677371e0f7 | -20.37967 | -42.56574 | 2026-09-30 04:00:00 | NOAA-21 | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f18eaa70-bbdd-3e4e-9d19-dee226285d66 | -21.38179 | -45.31418 | 2026-09-30 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| ad089493-bb30-3507-b5bf-962c741916d0 | -21.38459 | -45.31925 | 2026-09-30 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 68db67de-ea07-3141-b6c8-e5afc4e10770 | -20.50276 | -49.62712 | 2026-09-30 04:00:00 | NOAA-21 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa3554c9-7cc5-3f0e-ba5b-ebb958cee136 | -20.85054 | -44.58429 | 2026-09-30 04:00:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 603de2aa-6508-3697-b808-ba7782720ef9 | -18.28633 | -53.05453 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8461754-04d6-3b9f-885e-d8a767783220 | -18.33412 | -53.07339 | 2026-09-30 04:00:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10939d59-8726-3805-bef9-0dade4815929 | -20.85402 | -44.58494 | 2026-09-30 04:00:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1760af0e-225d-3831-b5c2-39b1ce3c6d7d | -19.63007 | -46.91411 | 2026-09-30 04:00:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fb6f3de-f80e-390b-814d-9b626761ca0a | -7.8297 | -45.8156 | 2026-09-30 04:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5a8c1de7-0654-3563-9dc6-74c4725c27f5 | -2.9082 | -54.1108 | 2026-09-30 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 20a68019-9bd9-30fa-87bf-2bf6347cd2ad | -2.9924 | -51.045 | 2026-09-30 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8b0bfc74-071d-36d7-bd0d-75fcb92e9d98 | -2.9739 | -51.0455 | 2026-09-30 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| c5361d60-6d6c-390c-ab79-f65e3e3333b3 | -7.8109 | -45.8173 | 2026-09-30 04:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 525f741c-1b43-337e-9de0-304b44b5c37e | -20.5138 | -49.6289 | 2026-09-30 04:10:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f674eae0-cec8-3b35-97a6-418c3691fdb5 | -12.3085 | -47.9539 | 2026-09-30 04:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 054d82b9-71c7-3cc5-bb51-01ae3df7e545 | -2.9082 | -54.0907 | 2026-09-30 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 365536f8-78ae-3c57-a4eb-54ced3e1e508 | -7.8486 | -45.8138 | 2026-09-30 04:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4d09a5e3-26bd-3b96-b6b4-d9787b1ff0db | -2.8899 | -54.0912 | 2026-09-30 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fced42a0-5c3e-3354-a4be-5f88ecfea200 | -2.974 | -51.0247 | 2026-09-30 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8308c247-19b3-37ca-a1d2-b551a84e27dd | -14.1314 | -46.2571 | 2026-09-30 04:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e7c85e27-20f3-37ce-8880-0ae4e114b3f0 | -18.2627 | -53.0528 | 2026-09-30 04:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2a82e901-8a9f-396c-be07-e8f4cc6eb0bd | -20.5138 | -49.6289 | 2026-09-30 04:20:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 97a142d6-fef5-3a9d-886c-1fca8453e765 | -2.8899 | -54.0912 | 2026-09-30 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 55714855-df4d-3233-b868-d7970a8d6163 | -11.811 | -50.4356 | 2026-09-30 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| bc082cf6-3cd4-3020-a895-7cb4402175a5 | -2.9082 | -54.0907 | 2026-09-30 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 93ba7b35-2d68-342b-b58c-9c19151d689d | 1.70491 | -55.92828 | 2026-09-30 04:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f88d7234-04a7-35a2-95d6-b64fe4556178 | -1.5971 | -45.81307 | 2026-09-30 04:29:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65a8e9ff-0707-3d75-8940-c03234c0ef64 | 1.70554 | -55.927 | 2026-09-30 04:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b1572e6-7fdb-37a5-8bb7-5a4ae183d7f8 | -1.12836 | -46.94212 | 2026-09-30 04:29:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 725a974e-a030-3eec-837c-d379432bf2fc | -0.482 | -49.13012 | 2026-09-30 04:29:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45201c28-5c9b-3b2b-a791-d8676aaf44a1 | -0.48628 | -49.1308 | 2026-09-30 04:29:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecad75e6-d439-3d67-9675-49439574dcd3 | -0.66988 | -49.24892 | 2026-09-30 04:29:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 388f05d8-75ae-35a1-8c3c-2c02a9b4e5d2 | -0.92964 | -47.12426 | 2026-09-30 04:29:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2926aa7f-5e76-36e8-914a-a3e51b312712 | 1.70653 | -55.93337 | 2026-09-30 04:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d33cbfa-885f-356e-918e-2da1dfcf49f4 | -0.84438 | -48.72147 | 2026-09-30 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ab6ca32-d474-32ab-bceb-ab3dc03e319b | -0.50451 | -49.11642 | 2026-09-30 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc027ef-5740-39ee-be02-5c4f96d8d510 | 1.86072 | -55.56438 | 2026-09-30 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc957a09-ae85-3b3d-b9bb-2ae88e93d309 | -0.67052 | -49.24488 | 2026-09-30 04:29:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08d41001-9b92-34d3-a172-57f2929b1532 | -0.67418 | -49.24962 | 2026-09-30 04:29:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39675707-693f-3a2a-a261-36bcef752590 | 0.70195 | -51.43343 | 2026-09-30 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7846902b-0693-3931-b461-b0a8c6aabcdd | -0.50879 | -49.1171 | 2026-09-30 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bce5dfa5-fba2-31b9-9b94-a2fe1f65cea9 | -0.48565 | -49.1348 | 2026-09-30 04:29:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 854774fd-adb6-3ede-aaab-63dcac0e4877 | -0.50587 | -49.11762 | 2026-09-30 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cc03135-b9a6-3582-ae7b-0c312ab45aa6 | -2.88492 | -54.87434 | 2026-09-30 04:32:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bf67792-62ad-3908-a2a7-17d46737355e | -5.72845 | -43.50502 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81bfcf97-1ca0-3f98-95d4-4b0a4f91f19c | -7.83979 | -45.8252 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| afd44762-598d-3b1b-b838-f322fda3a201 | -2.99114 | -51.04316 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| daeac90f-5eec-3d1c-8057-1521277faadb | -7.17061 | -55.40806 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f117040-4151-382e-a9e1-a773278c9820 | -7.45536 | -45.78863 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32f38655-b19b-3d59-a01f-55c4ad384efe | -5.73125 | -43.50909 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa50f744-2729-3d4f-a00b-7d6d060fbd9f | -8.83954 | -49.71168 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d01b7fb7-7f53-3638-9986-7358c7a16ec7 | -4.29705 | -48.61136 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 493ac326-3194-3199-a667-57d9105cbf3f | -7.81912 | -45.82552 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 98f067cc-cabe-30e6-a243-3329f3f7af78 | -3.24085 | -46.93422 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a73d76f-eb12-3205-b59f-4c89d332bd5c | -7.07779 | -44.35997 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bfcce8d-5cbd-33d4-9e4f-ec6538598c00 | -5.86953 | -50.16327 | 2026-09-30 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59644114-b41b-3bf6-ada7-c70168c17ce8 | -3.26864 | -50.70413 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e65f313-5948-395e-b135-b83722f1189a | -8.00937 | -44.50045 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abc83ee7-cae6-3bf6-aaac-395a733e115c | -8.60551 | -48.91359 | 2026-09-30 04:32:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed9cef30-4773-3f5b-b705-dd65ab48a9a2 | -6.37955 | -55.1401 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1dec639-ae68-37f7-bb13-b65bd396d56d | -3.25135 | -50.80615 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0157ba95-6cfa-3d26-8dff-46cd4037e3c3 | -5.75501 | -45.17064 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 307d6a32-c58f-3d4a-b5c0-8c74af0c247e | -5.72773 | -45.16986 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc41cd7a-9e70-348f-b405-f292cbfe61f7 | -3.22861 | -46.93339 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86d3d141-f84b-32d8-95c2-309d27ff0b69 | -5.75723 | -45.17819 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2f9bb8b9-49c2-34b3-bcd7-9970355f5cd8 | -5.76057 | -45.17872 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| abf7a7f1-5588-321d-87a5-bcf9dabae939 | -6.21092 | -42.51252 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 52e1615e-4e66-3261-85a8-9268af600d33 | -2.96701 | -51.03201 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5bf8e7b3-e4b8-3a63-92aa-3f30d16933c4 | -5.09871 | -46.0406 | 2026-09-30 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adaab2ac-4fff-3c86-acc9-1ea969803a37 | -5.12565 | -56.02452 | 2026-09-30 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1164f8e7-3a16-3f18-88f5-d569c1c611e0 | -2.73417 | -49.41423 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3c960bd-a34f-3a7f-a4a9-54032b0d296d | -7.82247 | -45.82606 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |


[Clique aqui para ver as próximas entradas](README22.md)
