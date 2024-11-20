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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79c3d995-c6ab-39ba-8f97-18346a23fd9d | -2.208 | -46.457199 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769dc494-e001-36b7-81e6-40cd70295564 | -3.2885 | -45.397099 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c71bc7df-418d-3109-9f31-4cde96438852 | -9.1618 | -44.7309 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a2ae09c-5d67-3bdc-a780-ecfec0101c78 | -3.29 | -45.403999 | 2024-11-20 00:09:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca92fa1d-7c99-364d-9e56-075eee6cf3f8 | -2.6997 | -46.0784 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99c7045c-6974-312f-9195-f18ac4a8b36c | -1.845 | -47.822399 | 2024-11-20 00:09:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4e7a08-987e-39ec-8a17-0b20faee3aef | -2.6631 | -46.236198 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87f840b9-e9a4-37bd-86a6-fdffd8249b83 | -2.305 | -46.843601 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 028d42dc-e849-382f-a6b1-a73ad8341e36 | -6.52 | -44.189602 | 2024-11-20 00:09:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4edcfcb1-f849-3150-ae3b-8e01a5d59556 | -2.0889 | -46.385201 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df0a6f28-f4d2-3570-aeba-1f1c9b365b07 | -3.8681 | -47.070099 | 2024-11-20 00:09:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92ea45c0-c5e3-3e65-b8cd-2f85c65921ca | -14.4656 | -43.360401 | 2024-11-20 00:09:00 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 33eab388-d408-3499-8cd7-fdae400c19a7 | -2.1159 | -45.359798 | 2024-11-20 00:09:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c763c64-d156-3dae-9619-755d42aca337 | -2.4029 | -45.811401 | 2024-11-20 00:09:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cced5648-ac16-39dd-a2a8-6cb08f9eaefe | -0.8757 | -47.8591 | 2024-11-20 00:09:00 | METOP-B | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89b6670c-0931-3d9a-9aa1-85ac14a52d9e | -3.2253 | -48.433701 | 2024-11-20 00:09:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 638003f2-3478-3de0-ae86-5f1a4a47253c | -2.737 | -45.693802 | 2024-11-20 00:09:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 098050ae-10ea-34ea-beab-7d409a6579c5 | -2.6745 | -46.241299 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 434b5118-51ce-3e0e-be19-97165720af59 | -2.6729 | -46.2341 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9cbf84c-2800-3167-badc-8e67599158f4 | -4.1742 | -45.6273 | 2024-11-20 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0185ec38-80b0-3e04-a5b8-59a219a8bbc0 | -3.3697 | -44.430401 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e55ccd1e-0f03-315f-b8be-9a1d38e7dca9 | -8.1392 | -43.785198 | 2024-11-20 00:09:00 | METOP-B | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f180baf-c652-3d61-a5fa-fcd9e554f81e | -2.4374 | -46.2859 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddc1bd7-75b7-33d8-b624-dda350eb9cbc | -5.721 | -46.197201 | 2024-11-20 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 947a4539-46db-311b-8fc7-3a487c8cd916 | -0.0965 | -51.4203 | 2024-11-20 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ec39a347-58ca-3edb-93f2-f595a6e43c28 | -3.1745 | -54.285 | 2024-11-20 00:09:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e03b075c-16ab-3a3e-a100-7849d2d87d8e | -1.6793 | -46.029701 | 2024-11-20 00:09:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45214189-b107-3c56-a9f2-9c5471eb4c4a | -3.1794 | -54.307201 | 2024-11-20 00:09:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ea7bbc-ba6d-3409-a02b-5d29b81917c5 | -11.5561 | -44.825699 | 2024-11-20 00:09:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| edbbfed8-37c8-3865-8bf6-2d58910a4bc2 | -4.5575 | -48.003601 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71bb5ec9-d232-368f-93db-8eeb5a080de6 | -4.0521 | -46.834 | 2024-11-20 00:09:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad24f4e0-022a-39aa-8317-086423324be7 | -2.6746 | -46.196098 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88edbadd-8051-3b8c-966d-d8ac59fde1e7 | -4.3723 | -47.768902 | 2024-11-20 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 900d0522-6090-3447-b8ef-b4b1b708cd0f | -1.853 | -47.812302 | 2024-11-20 00:09:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbb697c4-efba-3096-9a91-6891e15b90c7 | -12.2827 | -43.533001 | 2024-11-20 00:09:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f7be37d-632a-3462-89ca-11a9b90cdbd0 | -17.850201 | -44.703602 | 2024-11-20 00:09:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb9c9e9-a421-39f4-9613-adcefc181f59 | -5.4093 | -44.703499 | 2024-11-20 00:09:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e20adad-e8cd-3337-9e88-28cbf2e03d8d | -4.4382 | -46.580898 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d08696d-93c3-3c0d-adb0-935262a489b8 | -2.9113 | -45.277699 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e27dfd84-b976-3dcb-9447-0be8e65b320a | -2.9328 | -48.3195 | 2024-11-20 00:09:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05746e6f-6dcf-3c42-bc52-338d58fdfea3 | -5.59 | -46.162701 | 2024-11-20 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c991654-66af-397d-a118-9a494c7a022c | -3.2876 | -50.3391 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a45f994-54c4-3f23-abf2-7af8f274aa86 | -7.3519 | -48.887199 | 2024-11-20 00:09:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba9743a-898e-30ba-8050-b69624f2530f | -3.0574 | -45.8363 | 2024-11-20 00:09:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e63af18e-991a-3cea-80df-967f97dc032f | -4.0582 | -50.025501 | 2024-11-20 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b254349-70f8-384c-8f12-c0ea9a90b6a3 | -7.1395 | -40.482201 | 2024-11-20 00:09:00 | METOP-B | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6eb5466d-89dc-30e9-8a00-684c2ffe8da5 | -1.1842 | -51.745499 | 2024-11-20 00:09:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc7186f6-cf5a-33e9-b4c9-66530e78bede | -0.8896 | -51.710098 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c8360166-03bd-33bf-b1f7-6c1315b0852a | -4.1408 | -43.965199 | 2024-11-20 00:09:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b7977c6-f173-311f-99b7-d121cacae97f | -1.4827 | -47.445999 | 2024-11-20 00:09:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b500000-6d1b-3076-b7c6-1237b13f52cb | -11.422 | -44.680801 | 2024-11-20 00:09:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c61b6d97-6cce-3350-9a17-6957bbd418ef | -3.8238 | -41.5742 | 2024-11-20 00:09:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c4bddcd9-6b36-36aa-8dab-3f3f91908489 | -9.1684 | -44.714298 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7fdbd409-e636-3e14-a3c0-cc5ed22eb05f | -10.4481 | -45.068699 | 2024-11-20 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a168444-a71d-3e9b-aa4e-1d2aefff2ede | -3.6879 | -43.4664 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a34b596a-9cda-3008-a2e9-8c8bece13226 | -1.2342 | -53.334499 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4607e6d0-af45-3b7b-8d48-11cf1e2d028d | -5.4756 | -46.203499 | 2024-11-20 00:09:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7ce099-4f26-3ff5-bb57-08880685f73f | -4.1279 | -47.732399 | 2024-11-20 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff107ae1-136b-33c7-ae08-a010167efa89 | -3.1304 | -49.1171 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71c19164-032f-31eb-969f-e7aa13660496 | -2.6123 | -51.775002 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01045048-dacd-399d-b246-ba727f6b1a31 | -9.4185 | -39.021599 | 2024-11-20 00:09:00 | METOP-B | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 381a852e-3a3a-3daf-a8a4-a7f32fca735b | -3.2233 | -48.424702 | 2024-11-20 00:09:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfd35a41-69f5-38b5-80be-eb378c9a19e8 | -3.7695 | -44.055099 | 2024-11-20 00:09:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81567d13-f7f3-36da-b7c9-622de72305ae | -2.7401 | -45.707699 | 2024-11-20 00:09:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d748887f-3146-3d95-b432-5169842269b2 | -2.2517 | -45.459499 | 2024-11-20 00:09:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 58f36234-5855-35f0-ae3f-917277faf33b | -1.6942 | -46.233101 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8d27bfe-2e09-320f-9b57-103cf0486096 | -14.3094 | -51.479801 | 2024-11-20 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9dddc50d-07bf-30d2-a24a-82a47cfdb7d5 | -2.6714 | -46.181801 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3626c868-72cc-3468-b7e3-ca72334f120b | -16.0739 | -41.302601 | 2024-11-20 00:09:00 | METOP-B | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8ff52f3-dc94-3649-964f-aa8e3ae220b7 | -2.743 | -45.307701 | 2024-11-20 00:09:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f283dc61-999e-36f6-b5c5-b10a98853d16 | -2.2129 | -46.478901 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43aae263-093e-398c-9bfc-7ed8ee3126c3 | -10.4044 | -44.395599 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b1f1cd3-e3e3-3941-8a32-bb3ee9ff6407 | -2.6132 | -47.116798 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae0a999-ec9f-3d6d-b86a-e8e53ca074b0 | -1.429 | -52.655399 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 427ea1c5-872c-35c6-a9ce-27702e1bf0f8 | -3.5705 | -43.630798 | 2024-11-20 00:09:00 | METOP-B | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94049889-409e-3560-a644-dd769de221a9 | -1.2943 | -52.373501 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19a4db69-109a-37e0-a2af-dc517cd1d4f5 | -1.2947 | -47.800098 | 2024-11-20 00:09:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad1b4373-63ed-3e40-8065-b27d91e970cb | -4.1261 | -47.7239 | 2024-11-20 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b5e6a19-4a62-3028-a149-2b0f89c18ffd | -10.0517 | -44.7103 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 26cf370d-939c-3492-bb94-6bdf047f7c03 | -10.7537 | -44.819901 | 2024-11-20 00:09:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5b1fda8-0625-30b2-8a1a-2ff94cdbcea9 | -16.7337 | -45.756199 | 2024-11-20 00:09:00 | METOP-B | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ccb25bbc-3611-3f53-939d-2483c3c994e2 | -3.1033 | -43.980499 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1385b7ef-69ee-3869-84b2-3ea0873a6b48 | -2.8777 | -41.762798 | 2024-11-20 00:09:00 | METOP-B | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b52d922-6269-313d-ba97-3eb08d9737af | -2.9867 | -46.946701 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5cf1f7e-c399-353b-9826-0057a5c93aa0 | -1.6926 | -46.226002 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49ef830d-18c0-3b60-bbe1-9fd1e8dfb2dd | -2.4044 | -45.818401 | 2024-11-20 00:09:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 181b684b-b699-323d-91b4-0a4161a4452f | -3.3569 | -44.4189 | 2024-11-20 00:09:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0d7fa78-8124-3562-905c-907c8f80d0a5 | -3.8458 | -44.439201 | 2024-11-20 00:09:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed84ada-cb89-3155-841f-a25c2e5ec3d7 | -4.536 | -47.998901 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0deffc76-42eb-3e24-b608-413339ef8376 | -3.0621 | -45.857498 | 2024-11-20 00:09:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2a737f3-de24-39b4-acd4-fd19a3180718 | -14.464 | -43.3531 | 2024-11-20 00:09:00 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 73244af3-8e0e-3763-9f85-3201b42836b5 | -1.6807 | -46.310398 | 2024-11-20 00:09:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8a51c09-8ee1-339a-8ce4-be57d1ed6a2e | -1.8512 | -47.804199 | 2024-11-20 00:09:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d010de97-d75c-3687-a8e4-138c82e92f55 | -3.822 | -41.566299 | 2024-11-20 00:09:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e35dcfb4-4a49-3587-9bce-1a1de45373fe | -4.525 | -43.2938 | 2024-11-20 00:09:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d37e0bf0-3aa7-3239-8f52-f9092fb35900 | -2.228 | -46.821499 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5625d49-a828-33d1-bfae-b7515b62ae65 | -2.6422 | -46.143299 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01773846-4911-35f8-b5ed-d56d35e64ac9 | -1.0384 | -51.734402 | 2024-11-20 00:09:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 24bae325-65d9-3285-9167-43534b0f4079 | -11.9054 | -43.971401 | 2024-11-20 00:09:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f36d3554-157a-3e87-bd23-2b53d55017e4 | -3.1048 | -43.9874 | 2024-11-20 00:09:00 | METOP-B | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
