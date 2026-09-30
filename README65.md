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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a99d3f94-84f5-3204-a0f6-3577e55de4f7 | -12.495 | -49.10794 | 2026-09-30 12:04:00 | TERRA_M-T | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6bb5da77-7729-3788-b1fa-5e337969a6b2 | -11.1933 | -45.11284 | 2026-09-30 12:04:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 61af1883-c663-3307-ac58-b8efd157de39 | -12.78816 | -53.9986 | 2026-09-30 12:04:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| f8713f6e-ee43-34bf-85f8-41646dc72afe | -12.89156 | -44.80111 | 2026-09-30 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c30f48f8-53f8-3d9f-9fc8-50299e46184e | -17.12493 | -52.11956 | 2026-09-30 12:04:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6ffa5e10-fad8-3cfa-a973-5245cd512935 | -18.26924 | -53.04918 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| af03ac11-b411-3992-8dc3-b48cbca21c6c | -18.25248 | -53.03684 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| bc943d52-66a6-36f2-be49-812ff813cd5e | -18.28998 | -53.03233 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 39e7aaba-9e4b-334b-8242-edf5ac8bc833 | -18.28093 | -53.03102 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d9c73bfa-a312-303d-b2f9-efb7e16dfa79 | -17.12356 | -52.12977 | 2026-09-30 12:04:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9898aa91-0d3c-3758-ad38-54388ce39282 | -18.28865 | -53.04206 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c3c05573-ce7b-3da6-a9b6-411201b8ffb4 | -17.13083 | -52.12633 | 2026-09-30 12:04:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| e33888c3-248a-3cd2-8ee9-e74daf8595ab | -18.29808 | -53.03956 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 927247cb-e39e-34de-9f19-1110868d4813 | -18.25888 | -53.05761 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 289.1 |
| 129c8036-4bff-398c-8ce4-758889bce91d | -17.91722 | -44.39795 | 2026-09-30 12:04:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 30ad3654-e18e-3b47-aef6-e8396587a643 | -18.2602 | -53.04787 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 260.9 |
| ead3af8e-43af-3341-b970-13eaae0a105c | -18.2357 | -53.02451 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 0ac47baf-4427-30d8-bd6a-117b659a032d | -17.92809 | -44.39315 | 2026-09-30 12:04:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 80579d16-d888-3803-966a-31db6aa74be1 | -18.27961 | -53.04075 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d03c6c8e-f66c-35b4-96e4-b6aebfb29caa | -18.23701 | -53.01479 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| bdaf955f-2316-3b47-9f2b-825cdfb94b54 | -16.78832 | -51.3664 | 2026-09-30 12:04:00 | TERRA_M-T | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9d53d28d-79ae-3288-b651-4f4b746eacdb | -18.29938 | -53.02982 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 201.8 |
| d01e8051-b03c-34d0-9501-648d9887fc7d | -18.27188 | -53.02972 | 2026-09-30 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c891df4a-a26a-379b-9368-17f7ce6d7a44 | -11.4119 | -43.415 | 2026-09-30 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 64c9194c-21c4-30d2-b04f-ef2fabc2f8ae | -11.2095 | -45.1478 | 2026-09-30 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 15259a8d-04c3-319b-809c-bac2d2d0313c | -7.8297 | -45.8156 | 2026-09-30 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 43fbcd22-165c-3fa1-978f-9d6757f6e79f | -9.8613 | -44.9577 | 2026-09-30 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 54b95c34-0b03-3bed-9dea-4e4246c708be | -11.1903 | -45.1505 | 2026-09-30 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| eabd0ebe-c7e8-3693-bd2b-c3f2cad864b4 | -13.3662 | -46.8139 | 2026-09-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0338863b-e12d-370d-99f6-048a79c5c5d5 | -17.9144 | -44.3976 | 2026-09-30 12:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 73a8a2ab-520f-3151-a669-ae5bf162e736 | -10.5197 | -45.3784 | 2026-09-30 12:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 7302c2a5-1f58-38f3-ab71-8636f755eb66 | -12.6166 | -42.7649 | 2026-09-30 12:20:00 | GOES-19 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 138.9 |
| ced6034e-d100-3db7-9576-96ef9c77e2d0 | -11.2095 | -45.1478 | 2026-09-30 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 3c2afa5e-cbc2-38ae-8aa6-2c8eaa28add2 | -8.0169 | -42.8444 | 2026-09-30 12:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| ce1598ae-b088-3b6d-a45a-82da24b52bf6 | -7.8297 | -45.8156 | 2026-09-30 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e32c4eac-d5f1-3f93-939e-19d41f9164d0 | -11.4119 | -43.415 | 2026-09-30 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| c507f884-d98f-3a6c-a1f6-f0fdf69a3ba6 | -18.1144 | -44.3988 | 2026-09-30 12:20:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 58ca5e5a-d620-380d-b0a0-4790a9afbbef | -18.0943 | -44.4035 | 2026-09-30 12:20:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 116.4 |
| e049340d-3991-3679-a53d-a0cd1a3c7570 | -9.8613 | -44.9577 | 2026-09-30 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 563c4296-6ef1-38d0-8ffc-9e303b605e06 | -8.0169 | -42.8444 | 2026-09-30 12:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| d8be40ee-c9b8-31fc-98b7-62f5cb61be31 | -7.5248 | -44.5485 | 2026-09-30 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 8fe1e443-48db-3ffb-884e-bfcdd19770ec | -11.4119 | -43.415 | 2026-09-30 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| a8b86f5d-3074-3344-bd50-d9e795d2b9e9 | -11.4307 | -43.4358 | 2026-09-30 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| cf07ee4d-52a5-3621-9bbd-1d96b2eb2be9 | -6.9138 | -43.7049 | 2026-09-30 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2fb47f1d-f953-3bc0-9cc2-74ed7b130ead | -7.8297 | -45.8156 | 2026-09-30 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 11326086-24a7-3bb3-a376-6de473e232cb | -17.9144 | -44.3976 | 2026-09-30 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 09dabc36-1e13-32e3-b2bb-09f9b4fbb43c | -6.895 | -43.7066 | 2026-09-30 12:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| da7298cd-3d7f-34d6-9436-70c1e76787c1 | -9.8613 | -44.9577 | 2026-09-30 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| edcfd35f-01b9-38f9-ad40-bdf2e717f989 | -11.4499 | -43.4329 | 2026-09-30 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9cf9b4d4-eab4-302e-9e1f-bb262b32627c | -12.4346 | -44.1733 | 2026-09-30 12:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| cdc9b0de-ef3b-3fd0-8693-2a48c72c251c | -7.0281 | -45.3008 | 2026-09-30 12:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b1510e2e-c179-30cf-b87b-2dcdac2d40c0 | -11.4119 | -43.415 | 2026-09-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 4c1f1af1-bc77-32ce-b155-45aa399ed109 | -12.4346 | -44.1733 | 2026-09-30 12:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b2bc0936-d37a-33b6-8655-a4f3baedc09d | -8.0166 | -42.8681 | 2026-09-30 12:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 42fffef4-5c86-37c8-afc8-91c01d0ea643 | -7.8297 | -45.8156 | 2026-09-30 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 53dc3afe-2ba2-37f9-ae12-e272ddff6687 | -14.3153 | -44.9052 | 2026-09-30 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 7a1d2e40-8a1c-3f4e-ba9f-e4d26fc25abc | -11.4307 | -43.4358 | 2026-09-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 87640038-c8db-398e-8576-89cec207613a | -8.0169 | -42.8444 | 2026-09-30 12:40:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 7dfebc28-7d04-33dd-8b28-7ebb74e00dd1 | -7.5248 | -44.5485 | 2026-09-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| a792a412-7849-357e-93a4-8d45cd501173 | -6.9138 | -43.7049 | 2026-09-30 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6b12a45b-5f47-3bc9-9d1d-cd960e4e1c4e | -9.8613 | -44.9577 | 2026-09-30 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 0b27991b-959e-3731-940c-50328ad3287d | -7.506 | -44.5503 | 2026-09-30 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 58a98c72-8cc4-3e7a-aa31-5e337782b6f4 | -6.914 | -43.6816 | 2026-09-30 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 681f6feb-1fe4-38e7-9050-03be2734c562 | -6.8952 | -43.6833 | 2026-09-30 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6dba1a29-a7fa-3f59-a870-f51eabf1c894 | -6.895 | -43.7066 | 2026-09-30 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c5c3770a-907d-3ffa-bbf2-cee3441c5c69 | -11.4499 | -43.4329 | 2026-09-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| d9e5c0ac-fe1f-387b-b642-0da386ce77fa | -11.2095 | -45.1478 | 2026-09-30 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 809a1f28-69aa-32d1-b4c9-8207695c7797 | -11.4311 | -43.4121 | 2026-09-30 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| d970778e-d788-3e2f-9730-830d7935bd41 | -7.0281 | -45.3008 | 2026-09-30 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| ed1e8a31-162c-37c9-be93-e6c1393d6610 | -11.2095 | -45.1478 | 2026-09-30 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 9e8c3eec-0990-3075-9142-595dcf0cfaca | -9.9215 | -50.1682 | 2026-09-30 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3b4f8a58-d3b1-3a62-935b-d160abc4fdf4 | -6.914 | -43.6816 | 2026-09-30 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 21cf0ece-1437-340e-810c-8bac66bceacc | -9.8613 | -44.9577 | 2026-09-30 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 543ebba5-3326-3da2-bf85-120238dd9e9b | -10.207 | -49.9684 | 2026-09-30 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| bfa7012f-0de9-3dd7-aa5b-2a5d3131d42d | -11.4499 | -43.4329 | 2026-09-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 0be06d42-fbf3-3364-bda9-5cdffdfa7c89 | -7.0612 | -42.3035 | 2026-09-30 12:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 3f731652-8aff-3ce9-a4a2-fc43d6170d91 | -6.895 | -43.7066 | 2026-09-30 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 2224630c-5e57-3592-9973-3c8e3abe7599 | -13.8784 | -44.4442 | 2026-09-30 12:50:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| fba9b14d-1e08-314f-a0c3-a91ad645baff | -8.0166 | -42.8681 | 2026-09-30 12:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 280b7ad2-731b-3e7a-9ee6-6d289ca102d4 | -6.9138 | -43.7049 | 2026-09-30 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 04f23622-8240-3b82-bed0-8a5985b32b82 | -11.64 | -43.5218 | 2026-09-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 0fbbdc30-bfb8-3baf-9a4f-24cecf9d00a2 | -11.4311 | -43.4121 | 2026-09-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 7b201444-e1f0-3392-84ff-cad6cd1c07dc | -11.4119 | -43.415 | 2026-09-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 8e4b0619-98fc-3578-bff0-73c7ad47d75b | -12.6086 | -47.2204 | 2026-09-30 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 27085cf9-8793-30be-91f4-e68f38115484 | -11.4307 | -43.4358 | 2026-09-30 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| 78fc9bc2-2986-364f-81eb-78bdf46ce297 | -7.8297 | -45.8156 | 2026-09-30 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 065ad220-f76a-3f92-8d4d-5ce9dbd823d2 | -17.5137 | -43.7183 | 2026-09-30 12:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 5cc50f86-0bff-3dda-82b7-1ea8f1e8741f | -6.8952 | -43.6833 | 2026-09-30 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0fed4aad-fe3c-3116-8c3b-4878145cd434 | -12.4346 | -44.1733 | 2026-09-30 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| b7efad54-b0cc-36d5-a3ac-3463df83998d | -11.1903 | -45.1505 | 2026-09-30 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 5c26981e-ddfd-3e73-ade2-e8ba17a7a23a | -8.0169 | -42.8444 | 2026-09-30 12:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 160.9 |
| 661fb4b1-51ed-3553-9088-684ad56311ef | -12.6082 | -47.2429 | 2026-09-30 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 4c9c5f1e-0c53-3870-8b0b-6da1abd1e600 | -12.8842 | -44.8249 | 2026-09-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| df2216a6-b5dc-3d94-9ea8-e61c3ddf445b | -9.9784 | -50.1412 | 2026-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f8b8364e-b295-374a-9852-06e152820c7f | -7.8297 | -45.8156 | 2026-09-30 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5de33c3d-c46b-3523-b9f4-4d3a938a4aed | -12.4539 | -44.1702 | 2026-09-30 13:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| cf4b6082-7631-3db4-b7f2-f252c55ae754 | -9.8613 | -44.9577 | 2026-09-30 13:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d7a22ed8-66a7-3658-ad86-ed89633926cb | -9.9773 | -50.2267 | 2026-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 36cd49aa-79db-39d5-bebb-15d6858cd4a7 | -9.9207 | -50.2323 | 2026-09-30 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7a336ca0-47f7-30d3-8650-1e4d610acfce | -10.5197 | -45.3784 | 2026-09-30 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |


[Clique aqui para ver as próximas entradas](README66.md)
