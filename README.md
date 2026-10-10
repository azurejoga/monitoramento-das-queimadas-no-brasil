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
| b11050b7-76ec-3be0-8736-afe1c0ae4978 | -6.441 | -55.0624 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7b90cf4b-bd9d-34c7-8e4d-80b8e7ae6e34 | -7.5162 | -54.9844 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 680ec0af-1218-333d-8c6d-65aba3186554 | -11.0745 | -44.1003 | 2026-10-10 00:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 7c4483cd-c944-3165-b410-a641216284a3 | -3.1284 | -54.1857 | 2026-10-10 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 710d33b6-f867-35f2-a682-b2dadd2998f5 | -14.4726 | -43.956 | 2026-10-10 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 437.0 |
| 46124561-54e8-3f24-bc7b-6f6cfc2a7e48 | -12.2876 | -63.3903 | 2026-10-10 00:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 2ed349d3-ed31-3898-8e65-a5d58f531afc | -3.5491 | -54.7351 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 932be41b-9c11-30b1-b5bb-19f60956a7f4 | -3.8574 | -55.7794 | 2026-10-10 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 12a0564f-0c7e-34ff-8904-9ab3041627c5 | -2.618 | -59.9747 | 2026-10-10 00:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 095c86a8-6bcd-368c-9a1e-c77a206b2166 | -4.3767 | -54.7493 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 734cc164-7d95-32d2-9baf-ccd0ed48ed73 | -6.9319 | -59.2412 | 2026-10-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| dd984e23-fe57-3c35-af36-bc16acdbfcbc | -11.0741 | -44.1237 | 2026-10-10 00:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e4c76bf4-f9bf-3cd1-b85f-6b33593eae91 | -3.1101 | -54.1661 | 2026-10-10 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a8da282d-cdbc-3fe3-9f8a-cb378cd82029 | -14.4731 | -43.9322 | 2026-10-10 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 8452602e-79b9-3768-be19-7c028254d598 | -3.8573 | -55.7992 | 2026-10-10 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2d440d9f-48e0-3018-b68c-39e379bc0691 | -4.3582 | -54.77 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 186.4 |
| 32013c95-f5be-3c26-8e44-ce1e185f2b01 | -3.1285 | -54.1657 | 2026-10-10 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 884fbb2d-3ae5-38f7-b34e-784bb72f803f | -5.6873 | -49.0511 | 2026-10-10 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0b20cc6e-7d1b-3f9d-ad4e-f60eff3857a2 | -12.3066 | -63.3701 | 2026-10-10 00:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 9167b815-a901-3133-8442-76ca4962608e | -9.3165 | -47.3851 | 2026-10-10 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 8bcf5dcf-cc04-3e7e-ac9a-f059062ffc23 | -9.362 | -64.6573 | 2026-10-10 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 5dd5762e-19c4-348e-9ce5-ced4e57cf119 | -4.6096 | -49.2156 | 2026-10-10 00:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 8b7622c7-a857-3805-8dd4-0856326beb79 | -4.4507 | -47.9112 | 2026-10-10 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 5cd8caa1-219a-3707-bec6-94bb861335a1 | -12.2156 | -57.1087 | 2026-10-10 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 360f2d97-c6a2-3d0a-aed1-ee89f8e96c51 | -9.6367 | -48.8628 | 2026-10-10 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| f44d5075-e8c4-352b-91df-2bc85d02b040 | -4.5929 | -55.7366 | 2026-10-10 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 597a47b5-8fea-350c-9a4e-4edf0cb831cd | -7.0225 | -47.6829 | 2026-10-10 00:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| d8846bb2-75d1-3637-bc12-c60d48a255dd | -3.2393 | -54.0222 | 2026-10-10 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 538f530d-154a-377e-b1b2-0bd573aa2452 | -3.9729 | -59.3564 | 2026-10-10 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 80b3ecca-acf3-391e-8d07-f02f126159cd | -7.4975 | -55.0055 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 4b531f52-09d5-337f-b9e1-705e8ba45f5d | -7.1823 | -52.6489 | 2026-10-10 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| d0bf777d-60bb-3477-a9d7-8646823e1f33 | -12.1015 | -57.1583 | 2026-10-10 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d47c7e80-f8c1-3576-82fb-a20b4778828a | -12.3064 | -63.3893 | 2026-10-10 00:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 24b30403-f29c-3178-a09e-a62e77feda1e | -3.7494 | -60.6014 | 2026-10-10 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 207.2 |
| fb22856a-fa51-351a-8c81-b25bec8aac4e | -7.9086 | -54.7194 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 487e92db-7975-3286-8b65-a5cb40c1afa2 | -12.2152 | -57.1488 | 2026-10-10 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 73a2f39d-ecf2-354a-bf99-5065cb2531db | -6.4751 | -55.4999 | 2026-10-10 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 69e63efd-189c-3cfe-a2d3-b36d21e38e6a | -4.4506 | -47.9329 | 2026-10-10 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a9851a8c-a97b-3294-9401-65324a65e514 | -13.3666 | -43.8979 | 2026-10-10 00:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 2992c340-cfd9-3b96-9caf-01019fdd795d | -12.0825 | -57.1598 | 2026-10-10 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e625dec3-01a7-3690-b035-1342fedb9b9f | -4.3766 | -54.7693 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| bf9f1c4c-0ad5-3f93-be41-58995de96e27 | -3.3129 | -54.0001 | 2026-10-10 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 80980175-09c9-378d-aa14-2633748d5d63 | -3.9912 | -59.356 | 2026-10-10 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| be11ba98-ebe6-300d-966a-b7cbc9009a9f | -6.9318 | -59.2605 | 2026-10-10 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e6bbeb20-f66e-3ee4-9e15-8337a5c355b9 | -3.0375 | -53.8865 | 2026-10-10 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| dd4c7b7f-87ce-3d2d-8411-6615c16998e1 | -9.2973 | -47.4092 | 2026-10-10 00:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 8f934e25-1a82-3129-aa9e-93b3ed101e9d | -7.927 | -54.7384 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| b8817ce8-5325-35d1-8a9f-cdf2798cd011 | -7.5347 | -45.3233 | 2026-10-10 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 00cd550a-efa1-303e-9ce2-a0caa3286084 | -3.5807 | -51.5039 | 2026-10-10 00:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ba49a9c2-a17f-333e-a807-8b274eee3ce5 | -11.0937 | -44.0975 | 2026-10-10 00:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 279.9 |
| 1c64f519-97ef-355e-aef2-8a8e04adb752 | -7.9272 | -54.7182 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| b2e86ee8-bfb4-3964-b129-0ee0fd01f70d | -7.2009 | -52.6477 | 2026-10-10 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 9f745f67-0233-3399-b3b2-979a0e52dc04 | -4.812 | -56.0849 | 2026-10-10 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 93011919-21f1-37cc-a7b5-37d71046758a | -3.7311 | -60.6018 | 2026-10-10 00:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| c952361f-e053-3253-8950-554c22dd3e5d | -9.3805 | -64.6567 | 2026-10-10 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0f58fd14-aaeb-311d-986a-f6a979bf6b58 | -7.5159 | -45.3251 | 2026-10-10 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 3d9c1206-dbf3-3ab3-8528-6b0d9aef1a56 | -3.2577 | -54.0217 | 2026-10-10 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d1d3b0ff-df5b-3784-b7fb-e2d4cf79ae62 | -5.2303 | -50.6856 | 2026-10-10 00:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f782e6e3-00ad-3470-9c49-82fb0106319f | -4.421 | -49.7766 | 2026-10-10 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f7cbcfa1-b1e5-3e4c-ad9a-92462a646665 | -6.4566 | -55.5008 | 2026-10-10 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 1f1fed90-911d-3bb6-9b11-a8eb2678fb2f | -14.453 | -43.9598 | 2026-10-10 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 345.9 |
| 7de21025-0416-38bb-a778-42c2b2338d4d | -3.8391 | -55.7799 | 2026-10-10 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 0bc0c02b-bbec-35c3-8899-7fd87605a5fc | -12.2877 | -63.3711 | 2026-10-10 00:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 121.2 |
| cabadb5d-694b-3a92-9c8a-8ee01fa24d98 | -13.386 | -43.8945 | 2026-10-10 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e7e63c61-65d7-34d3-8632-522979633648 | -3.839 | -55.7997 | 2026-10-10 00:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| 358dff52-cffd-3027-9b7f-ab30485bf2ac | -3.6907 | -47.815 | 2026-10-10 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| e63099f8-fd0f-31d2-963e-385e12d31461 | -12.2343 | -57.1271 | 2026-10-10 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4bb070d8-5248-3f33-a0b1-39c5bb5fec17 | -4.7848 | -42.7502 | 2026-10-10 00:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 140.9 |
| cd663c20-a205-321c-b3ff-bff3cbd67f8a | -7.1825 | -52.6283 | 2026-10-10 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 165cdf7a-9685-3a16-92c0-682b38b8421b | -3.875 | -55.9764 | 2026-10-10 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a973580c-b51f-3ab9-bf1f-c8adc1a73465 | -4.4344 | -47.5421 | 2026-10-10 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5efdf409-ee2b-3014-8d70-702107391186 | -4.9113 | -43.327 | 2026-10-10 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a2b9dcd0-724d-31bc-9471-ba9b3e13fa06 | -10.8905 | -44.8232 | 2026-10-10 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 40edcce1-c0fe-3ab0-b65e-651f787ca632 | -11.0933 | -44.1209 | 2026-10-10 00:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 0977cd8c-9065-32f8-92f0-a39b78708b11 | -3.549 | -54.7551 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 67035e7c-d989-331a-acb3-4e4dc4003e56 | -6.6145 | -59.9464 | 2026-10-10 00:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 80889104-e626-367c-b953-e46211613561 | -12.2154 | -57.1287 | 2026-10-10 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f682ecc7-50c0-322f-aec4-aad380ff7701 | -1.6225 | -54.4348 | 2026-10-10 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e07041aa-a8dd-350a-b3c1-e6b934604c87 | -5.0876 | -60.2263 | 2026-10-10 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2238cb2b-fa1c-3a1e-b2a5-2d9fdf8190d9 | -1.2906 | -55.7493 | 2026-10-10 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| c49f6097-f2e9-33c2-b289-d6770950a6d3 | -7.2011 | -52.6272 | 2026-10-10 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 5ecdba55-580e-3ae8-be8d-a4e47c7fd088 | -11.0332 | -45.4246 | 2026-10-10 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 16c7cdf8-b850-380c-9ffc-a7f0f282181f | -6.4596 | -55.0415 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9c90b689-a2b6-3492-95fd-fa8271c18c8d | -1.2723 | -55.7494 | 2026-10-10 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c76adb61-102e-3c88-9d45-0b97f566e3c5 | -14.472 | -43.9799 | 2026-10-10 00:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6f1f538c-3937-35a8-a2ad-bdd9ddfc55d2 | -7.5161 | -55.0044 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 748c938b-88e9-3781-a817-a7b23b1eaa4c | -5.7378 | -45.1307 | 2026-10-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 9bcb64a4-d6c8-33dc-819e-5b2cc8043a4d | -3.1114 | -53.7839 | 2026-10-10 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 12d587be-5c3c-30f2-acdb-dc59bd67222b | -9.6364 | -48.8845 | 2026-10-10 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| be57ec8c-9fec-3709-a0e2-a0413151200b | -4.5929 | -55.7168 | 2026-10-10 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 20b4654b-136b-3f9d-b6bb-b5580e08de3b | -6.4411 | -55.0424 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| fdfb0cff-6798-3de3-9a91-3324af6bc146 | -12.3067 | -63.351 | 2026-10-10 00:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e3b14cac-91e3-3ff1-9bae-5a15493343ca | -3.5676 | -54.6946 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| df752c3e-5d68-37d3-8864-8e5d5e660499 | -2.618 | -59.9938 | 2026-10-10 00:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 57531b42-755f-328b-87a1-341dc63f6f92 | -3.5307 | -54.7356 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 95927c42-1c16-322d-8640-41e3a6c651af | -3.2736 | -54.7025 | 2026-10-10 00:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9870197a-53fa-3549-8cf7-1cf0ad6bbb77 | -3.6048 | -54.5936 | 2026-10-10 00:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 81ba5bb1-a00a-33a1-b507-92f5ced92200 | -5.7565 | -45.1293 | 2026-10-10 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a508a1a1-aeed-36da-a7c1-5ac6894f238d | -7.535 | -45.3006 | 2026-10-10 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 599b6768-fb14-3ed4-b5c0-236ad0edb2c5 | -6.4595 | -55.0615 | 2026-10-10 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |


[Clique aqui para ver as próximas entradas](README2.md)
