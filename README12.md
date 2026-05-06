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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a5e4e6c-791c-3428-b4b9-9ae9bbc99013 | -12.50817 | -58.46946 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| e9f37a9c-763a-311f-a1e9-fabc608abf4d | -9.25091 | -60.33375 | 2026-05-06 12:59:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ad21b6e3-d4d5-3992-863e-032eb4a0180d | -12.49837 | -58.46183 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3931a3f7-2014-300e-9d7d-71e2de805c55 | -11.80123 | -56.95544 | 2026-05-06 12:59:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 435100ad-583a-33be-b14a-4b13a47ba348 | -12.49494 | -58.48363 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 301.3 |
| fdea45e0-2ec7-3f99-a7b3-8e353bdd7822 | -13.98156 | -56.6594 | 2026-05-06 12:59:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| c8907ee6-3791-3b2a-853b-b0e63f4de095 | -12.50628 | -58.48503 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 199.7 |
| 93ebcc67-859b-3aad-8ece-ca078afdecaa | -12.46409 | -58.55051 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5a8783dd-c72e-30ba-959d-c3428b5ec4d7 | -12.49637 | -58.47742 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 3adc572d-2044-3041-8620-899b6335f8e5 | -12.49442 | -58.49269 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| a4b83b99-ffe1-3c20-a575-11785a60fa2d | -13.98676 | -56.65334 | 2026-05-06 12:59:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2266b127-2735-3725-9f61-620134164c3f | -12.49681 | -58.46809 | 2026-05-06 12:59:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 7eb9dc44-b708-3f31-b871-da85cc9ec8e6 | -12.5033 | -58.4781 | 2026-05-06 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 256.6 |
| d943c27c-ecbd-356e-afa9-507e437f6e5e | -12.4843 | -58.4795 | 2026-05-06 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 6a027472-82fd-3f6e-bbdf-2115573c203d | -18.7849 | -51.9247 | 2026-05-06 13:00:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 80d3e83a-8383-3744-afd4-dc80aeaef6ec | -12.5031 | -58.4979 | 2026-05-06 13:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| b8e72e39-2dfe-3727-900c-5eea9e21d8cc | -18.7844 | -51.9467 | 2026-05-06 13:00:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 32eb528c-eba4-3693-b403-47aeaeff19e0 | -21.66617 | -56.31569 | 2026-05-06 13:01:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 26.7 |
| ff1a63cd-c0aa-3411-b1bd-ef3051b78bba | -12.4843 | -58.4795 | 2026-05-06 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 251.9 |
| 15202ce1-9e01-3992-9e36-5eeef7c8b9b9 | -18.7844 | -51.9467 | 2026-05-06 13:10:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 366b8f9a-dfe6-3d7e-bd6f-fddc91970703 | -12.5033 | -58.4781 | 2026-05-06 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 392.1 |
| f72c7e97-ef2b-38c2-a375-e7c233cd1849 | -18.7849 | -51.9247 | 2026-05-06 13:10:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9790e408-59c4-3406-b950-edd047cf6520 | -12.5035 | -58.4582 | 2026-05-06 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 97386067-418a-3397-a938-49bcc36bfab2 | -12.5031 | -58.4979 | 2026-05-06 13:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 4a856229-d8ff-30d8-b147-8d4a188792ff | -18.7849 | -51.9247 | 2026-05-06 13:20:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 969e7b88-7d3b-389e-b85c-d27880a738e3 | -12.5033 | -58.4781 | 2026-05-06 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 569.7 |
| 1b10cd2b-8b28-3765-9704-94136d147a77 | -12.5031 | -58.4979 | 2026-05-06 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 231.9 |
| a778e93f-fa0a-31b2-a584-dc35a8ab4753 | -12.4843 | -58.4795 | 2026-05-06 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 328.0 |
| f01b50a0-117e-34de-af0d-008ca7cacc8f | -18.7844 | -51.9467 | 2026-05-06 13:20:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 150.7 |
| fa01067d-63e2-3910-9bf8-41f27e777069 | -18.7844 | -51.9467 | 2026-05-06 13:30:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 8205ff5b-5854-3382-863a-dc31bcf5b7f3 | -18.7849 | -51.9247 | 2026-05-06 13:30:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 247f9054-ec8a-3d77-ac63-c50167e35474 | -23.7759 | -49.164 | 2026-05-06 13:30:00 | GOES-19 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c6b6e009-cbd4-386c-92b9-b1eec599d18d | -18.7849 | -51.9247 | 2026-05-06 13:40:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 6549843e-235c-3aeb-b7db-cc128e6fe391 | -18.7844 | -51.9467 | 2026-05-06 13:40:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 699273e6-9c10-394a-b9f3-9a232401d694 | -11.8214 | -49.7457 | 2026-05-06 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| f11b3186-a1ae-3414-b5fc-6a448d99c1e1 | -14.1502 | -45.3543 | 2026-05-06 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8271d39c-f9be-3a2b-bfd2-c4ce948a1723 | -12.4843 | -58.4795 | 2026-05-06 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 596.1 |
| 6023c002-340c-396c-920a-e82a753ee6bb | -12.5222 | -58.4765 | 2026-05-06 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| cd8b8961-0350-3244-9a53-ec1435f6d3c7 | -18.7849 | -51.9247 | 2026-05-06 13:50:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5501b980-6ed6-3a96-ab68-89136e7b0650 | -9.4259 | -50.683 | 2026-05-06 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 80ed98e1-175c-30b1-a9c2-86157430562d | -18.7844 | -51.9467 | 2026-05-06 13:50:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 3f81d929-eb75-3345-9320-683916d53822 | -12.5035 | -58.4582 | 2026-05-06 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 8e09bde9-3800-3834-b33a-aa5f4a9970ff | -14.1502 | -45.3543 | 2026-05-06 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 3254eba8-743f-32d6-8d91-fc266f00dcd7 | -18.7849 | -51.9247 | 2026-05-06 14:00:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 757a8ff6-cb2f-3a51-a8e5-5a62d64bb4b8 | -18.7844 | -51.9467 | 2026-05-06 14:00:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 00d8fb36-c7e2-3fa9-b44e-df9066bf02be | -12.5035 | -58.4582 | 2026-05-06 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 7f2593ef-2dc1-30b1-9b01-42f9a6f11ba5 | -9.4259 | -50.683 | 2026-05-06 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 71cc22ef-91cc-3f20-b5f7-d1cbe9597fbb | -14.1307 | -45.3577 | 2026-05-06 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6811325a-e6b2-3af7-8dc0-84337b534c33 | -12.5033 | -58.4781 | 2026-05-06 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 876.4 |
| b27a4a9e-1469-3458-8f59-b67fd103bb34 | -12.5222 | -58.4765 | 2026-05-06 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| eb846d5e-83b9-3318-99bc-91306b7f19f4 | -12.4843 | -58.4795 | 2026-05-06 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 753.2 |
| ff5d6512-f492-3591-9cc3-04f0cb7a6c53 | -18.7844 | -51.9467 | 2026-05-06 14:10:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 161.6 |
| f7d09b86-f09b-380f-9d9c-2532906265ff | -18.7849 | -51.9247 | 2026-05-06 14:10:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 93917874-a24f-3d0f-b0b3-4d08b23b0108 | -14.1502 | -45.3543 | 2026-05-06 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 856dbfb0-6839-3175-9647-c57b90057988 | -9.4259 | -50.683 | 2026-05-06 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| f9d9e783-33d8-338e-ba6f-3cd7943b01fe | -12.4843 | -58.4795 | 2026-05-06 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 595.1 |
| 432d4efb-695f-38ef-80d1-5027959b2457 | -9.4256 | -50.7042 | 2026-05-06 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 32acc1b0-68f1-3efe-940f-a55a33efb5f9 | -14.1307 | -45.3577 | 2026-05-06 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f3bf5364-a4e7-3a50-9e75-0ba2052cf26c | -12.5035 | -58.4582 | 2026-05-06 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 4f93d25b-9962-3d5f-be98-1891a5a57a44 | -12.5222 | -58.4765 | 2026-05-06 14:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1f5d07f7-892b-3e8e-baa9-8379fb1c540f | -10.8927 | -49.6157 | 2026-05-06 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2e9060b5-3a36-3138-b810-8ec3d14363c7 | -10.8927 | -49.6157 | 2026-05-06 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 45dcc7a6-5e97-38aa-86eb-0e8dd055fd83 | -14.1307 | -45.3577 | 2026-05-06 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 05aaae02-4169-3951-9ec9-b6f3d4eb415a | -9.4259 | -50.683 | 2026-05-06 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| e1e6c802-b3dd-311a-ba9c-172528fb4f3e | -18.4478 | -54.7099 | 2026-05-06 14:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2942ab5d-51ac-3037-95b7-578f7fcb8193 | -12.4843 | -58.4795 | 2026-05-06 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 838.6 |
| 94ee6efa-a7d6-3ad6-aa35-f5b391239fdc | -9.4256 | -50.7042 | 2026-05-06 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 581e11e2-758b-3e86-93ba-662bbf6bfeef | -18.7844 | -51.9467 | 2026-05-06 14:20:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 159.0 |
| c0019a20-04de-3b11-bd0e-ff839e5a6038 | -12.5222 | -58.4765 | 2026-05-06 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 152.6 |
| d6e4f660-c064-3db7-92fb-78b7855cf92c | -12.5035 | -58.4582 | 2026-05-06 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 1057c996-d7a1-3674-b24c-56126b1dde9e | -18.7849 | -51.9247 | 2026-05-06 14:20:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| dd4dcc83-7bfc-3652-9f25-d3f0f2c844e5 | -14.1502 | -45.3543 | 2026-05-06 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 91831263-1f97-31a2-ae01-069b587519e0 | -14.1307 | -45.3577 | 2026-05-06 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 72cc173d-43de-3b5f-94f5-3027f43ee676 | -9.4259 | -50.683 | 2026-05-06 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2205c2e9-7ad0-382d-baac-34b775e843b3 | -18.7849 | -51.9247 | 2026-05-06 14:30:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ad936ba9-4633-3788-a635-cccb1bb9536b | -12.5035 | -58.4582 | 2026-05-06 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| b30c0009-4095-38bf-8c1d-588a967a040a | -14.1502 | -45.3543 | 2026-05-06 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 67d1dba4-19df-3e8a-b11d-6c77bc5c2a98 | -18.7844 | -51.9467 | 2026-05-06 14:30:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 163.8 |
| cc759d09-8cbd-3fe7-8627-5e87e0e1b814 | -18.4478 | -54.7099 | 2026-05-06 14:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d9ed0de2-5df8-3664-bab8-94303e6fadff | -14.1307 | -45.3577 | 2026-05-06 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e57bccec-091c-3373-b2a6-a3d24dddf02f | -18.7844 | -51.9467 | 2026-05-06 14:40:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 201.3 |
| d2aa5b6f-f931-37f7-ab19-fe8cd6df199c | -10.874 | -49.5962 | 2026-05-06 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d3d9075a-63c8-3b8d-a9ca-e88c795f337c | -12.5035 | -58.4582 | 2026-05-06 14:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 4a1c5860-ce0b-334c-b11d-76da45cfea19 | -9.4259 | -50.683 | 2026-05-06 14:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3232552c-77a4-315b-bed6-11167a9358f2 | -18.4478 | -54.7099 | 2026-05-06 14:40:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 28adebf6-a925-3376-b0e9-233a42ae41d0 | -14.1307 | -45.3577 | 2026-05-06 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7f1e95f2-d49b-3ca2-8134-4ff301331e86 | -10.6458 | -47.0564 | 2026-05-06 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 3d79dc74-15e4-37f6-a127-dab0520dac0e | -10.6455 | -47.0788 | 2026-05-06 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d8eeb261-9820-30ae-97cc-f08d467db246 | -12.4191 | -54.477 | 2026-05-06 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 727b54ab-58d9-356a-943f-796adeb44eb7 | -18.4478 | -54.7099 | 2026-05-06 14:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9dbe9491-3e66-3f2a-8954-ac4c9f96a95d | -12.5035 | -58.4582 | 2026-05-06 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 401036ad-2948-3296-ae85-1bf329ca77d8 | -12.4381 | -54.4751 | 2026-05-06 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 20526c52-bda2-371c-89ca-795661010cda | -10.4162 | -49.8609 | 2026-05-06 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 893110a2-78f8-32d2-bc29-83bb700fe18b | -18.4478 | -54.7099 | 2026-05-06 15:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 98a6c8cc-9670-354f-aab1-c4037db816a4 | -18.7844 | -51.9467 | 2026-05-06 15:00:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| b473cac5-c2b5-30f8-a039-4153ca34b028 | -12.4191 | -54.477 | 2026-05-06 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7e55501b-b992-3c53-a10e-891b7c791813 | -9.4259 | -50.683 | 2026-05-06 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e33ce126-1fbf-3ad5-89d7-c8a48795d875 | -10.4162 | -49.8609 | 2026-05-06 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 4b7a9e70-4967-363f-a497-945767289055 | -13.9924 | -56.6437 | 2026-05-06 15:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a478bee3-acd1-3140-81e3-f58b16a2ac46 | -14.1307 | -45.3577 | 2026-05-06 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |


[Clique aqui para ver as próximas entradas](README13.md)
