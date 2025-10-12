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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b1ab546-0dec-3db0-9405-423447e7f4f6 | -15.64239 | -44.4735 | 2025-10-12 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a6d42db9-d718-309c-892d-6cb97f9240e6 | -18.02077 | -45.01343 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 83d8647f-1345-37a7-bb05-83966e11bae3 | -14.77561 | -48.65662 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0944ae5-98d8-3e4b-b20d-cafd4df243ae | -14.91052 | -48.52871 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c17e1021-2161-3065-b572-4d33d408fdba | -14.90327 | -48.5273 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4fc8df0-208a-387b-ba4d-4f71b872eb8e | -12.24039 | -45.3396 | 2025-10-12 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8db3dd0-e431-3a37-b0a9-0eed89d29887 | -14.98533 | -44.94049 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9430017-7115-3f30-b39d-13094cf33c4d | -14.92085 | -46.77326 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7073c7f5-9c95-3898-b59d-bda03d8886c3 | -18.56311 | -50.59818 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5b64dea4-0570-3680-b423-aa7854d147b9 | -17.18251 | -46.94023 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fbb57b9-c08a-3128-bd05-f58f6ab98887 | -18.58705 | -50.57644 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d6d808be-7a7c-38ab-8438-64bc709ab1a6 | -14.94513 | -46.7308 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a15143fd-13ba-3aa3-82c2-81e2739a8ba6 | -14.94728 | -46.73889 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50e56f85-a83a-3e88-bb62-5d8d0e8962a5 | -14.96508 | -46.72306 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2c55fbec-2499-3395-b89b-dc6e1581f969 | -14.9642 | -45.11889 | 2025-10-12 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c3cbde8-0f7a-3168-b620-8603adabcccb | -17.40302 | -46.86123 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87182cc9-9066-3b61-9eeb-e821d1627448 | -14.97272 | -46.73989 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a6b5f76-1c94-3a5c-aa59-cf3622fce414 | -14.02023 | -47.07341 | 2025-10-12 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| feca7935-bd11-3dd7-80de-937716b30c2a | -14.34904 | -41.31664 | 2025-10-12 04:17:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 98844268-1bd4-3d04-b85f-f1a84776a03a | -14.39886 | -48.01681 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 49517151-dfac-3f23-b6df-c2f02b126fb4 | -14.75926 | -46.1294 | 2025-10-12 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61e95a88-b988-3e62-8906-61e1f7534598 | -22.04176 | -55.16817 | 2025-10-12 04:17:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12fe8ea7-c6b0-3844-afbd-f000f2a95589 | -19.52462 | -43.04761 | 2025-10-12 04:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| cd08022a-869d-3609-972b-c6a7f262d41b | -18.4013 | -46.39237 | 2025-10-12 04:17:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d355062-a0d5-3565-a4f6-b10e39fa55c7 | -15.2852 | -46.14019 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 008c4c5e-1fb0-36de-9c90-e150678a1312 | -14.58698 | -42.77871 | 2025-10-12 04:17:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2a87bd1f-f21e-3cc5-8b16-cb3f90d37e1c | -12.22176 | -43.78892 | 2025-10-12 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88d2dd7e-897f-3a11-9678-d06ae2f31252 | -18.07301 | -42.99271 | 2025-10-12 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 69cfa8ce-a69c-37f8-a5bb-d5d44c9eb0ef | -14.94451 | -46.73461 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 30a04041-12de-3901-b591-17a7edf0340d | -14.40585 | -48.01305 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0a409b4a-682d-30f9-89e2-2c9c7d5b68a8 | -19.10239 | -46.4134 | 2025-10-12 04:17:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3803ac9a-4ab0-3b0b-9498-c44ef16fbeca | -18.34095 | -45.93245 | 2025-10-12 04:17:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ef82ee3-646e-3e16-aaf3-9258d327af8a | -14.40431 | -48.02189 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7f360a7-9dbd-30a0-b37e-49ad48271336 | -15.20421 | -44.49417 | 2025-10-12 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea3921fb-3a31-3e6b-8e03-da7d613de5e4 | -15.67978 | -46.62807 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c53788b2-8e6c-3513-8734-a3650f99517f | -19.52818 | -43.04819 | 2025-10-12 04:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7a04c477-4e5e-34a6-ad5d-eb96226538cc | -17.18191 | -46.94394 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adec35e0-909a-357a-adfc-079750acbce0 | -18.56697 | -50.59891 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 048cf60b-fd8f-374d-8487-f8f106cbb90a | -13.17636 | -47.9581 | 2025-10-12 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c420ef2-94d4-3d3b-8c5e-c85abd3c33d5 | -18.05399 | -44.97422 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b243434e-a843-368b-b017-a9b18451f0d8 | -14.40594 | -48.01836 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4a7c5716-8b9e-36bf-808e-8c6ee2af82ba | -14.94573 | -46.72709 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c586f5a-f656-30b3-b656-82e0b4726b7e | -17.18953 | -46.96064 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f698fc5-d323-3b50-bd4b-e4d31cc0f350 | -18.57654 | -50.59025 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3d78e4bd-9c7c-3ef0-ba27-512ea0240e2c | -15.67524 | -46.63479 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36854b7b-2976-3c26-bb48-96eae9cd75ae | -13.29787 | -43.31221 | 2025-10-12 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9b26671e-6392-3fab-82c7-491855ec9b1d | -18.45547 | -47.15562 | 2025-10-12 04:17:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8e441c1-7032-3158-a639-76827aa36e63 | -13.98422 | -54.89461 | 2025-10-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ddad66a-624f-3241-9a10-099d849f2c50 | -14.89649 | -48.48016 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2223ed04-8c40-34f1-a6be-fb6d73f448d0 | -18.96023 | -45.7145 | 2025-10-12 04:17:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e0818df-67ee-3579-aac4-ea7a520b3e94 | -15.50275 | -48.00247 | 2025-10-12 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04baab6e-dddf-3567-8575-3a1a74376752 | -11.77773 | -46.34269 | 2025-10-12 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07bbb90d-322b-38f7-8458-02f5b72de631 | -14.89835 | -48.5125 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8b6a71c-941a-3715-aca5-96bf5514378c | -14.40591 | -47.97466 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3eb9d566-4e20-376b-97ee-8235095a07b9 | -14.95153 | -46.72097 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9d33683-9d93-3b11-87ab-a74c9c2007a5 | -14.99971 | -53.88319 | 2025-10-12 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d968122e-3acd-3987-ba5e-307d5854426a | -18.08698 | -45.02423 | 2025-10-12 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1f952a4-948d-36cd-9362-7902abc740cf | -15.28854 | -46.14073 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67789d47-4aa8-3cfe-a719-5b88c1ea3820 | -14.68452 | -44.75285 | 2025-10-12 04:17:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a45aee12-c1d2-3f0e-a721-a3019b82ab63 | -18.91079 | -47.01473 | 2025-10-12 04:17:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b783a406-55e4-3f5d-b830-91f7f78da20d | -14.83682 | -42.39256 | 2025-10-12 04:17:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e83cc1a-9465-3f29-ab5c-3231d1b64c3d | -13.72343 | -41.94292 | 2025-10-12 04:17:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 10f27c05-e672-393d-88f3-3d7615d3649c | -18.04623 | -44.98043 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00f29da8-1145-3fdf-8341-559cad5b23e0 | -14.93989 | -46.74166 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3c3c7f65-f39a-3073-a135-727a2c59bd3b | -18.56599 | -50.60426 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f5709c40-9b49-30e4-aae0-47f0c5649ee5 | -20.56744 | -54.63165 | 2025-10-12 04:17:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd2c27e7-fcde-347e-9db1-f015123058a0 | -19.52758 | -43.05246 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c58776b8-1b6c-3753-a3cd-427a93fb5f10 | -19.50202 | -43.05269 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3a59f52-7a06-38d8-a7e7-7cfb9c7e5fed | -17.18404 | -46.95199 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b894e54d-7d94-34ba-ba5e-615514ffc0e0 | -13.6507 | -47.64448 | 2025-10-12 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 309b1435-acb9-3791-b0ee-c8648c5b7585 | -14.94389 | -46.7384 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1c7a1270-497e-3767-8d93-d047b0324004 | -19.52878 | -43.04395 | 2025-10-12 04:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b8be10a7-39c6-3c59-84b8-12f8baf699ff | -13.64895 | -42.44656 | 2025-10-12 04:17:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7f0491f4-a83a-3c9c-9a7d-24bfa42a3d3d | -14.91685 | -46.77643 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9d66691-30ab-3d56-8982-a47ab13932cb | -18.08753 | -45.02061 | 2025-10-12 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba95db68-20bf-3eb9-b23e-70fd923b88a1 | -14.95492 | -46.72151 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c50b78e-11d6-3ae0-a0b4-c62fd681f01f | -18.05123 | -44.97004 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c63e737-eda1-3213-b793-c62531cbcdcc | -12.22013 | -43.79954 | 2025-10-12 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 209d0006-e55a-3e37-bd45-a0aacb8a2fab | -14.93589 | -46.74496 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c37bd7f2-4733-34b0-9a6b-19ab1abf28d1 | -17.25102 | -52.26884 | 2025-10-12 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 233ada29-103c-364d-a44e-9e3ebe2a7845 | -14.02576 | -43.48522 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 88bb2002-c29c-3626-95dd-2176446cce16 | -14.6674 | -42.26793 | 2025-10-12 04:17:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72a8249b-11a3-300b-a996-a05f435b864e | -13.41349 | -43.68936 | 2025-10-12 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57498632-f974-3b3f-b2c4-f9148e09e22c | -14.01674 | -47.07727 | 2025-10-12 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56488068-e2d1-3a2a-a37d-86a7a66c86a0 | -15.28912 | -46.13708 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7d3ebbd-12e1-3ce9-b932-26869db3f850 | -17.19288 | -46.96119 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ceda297-37e1-33eb-a3c6-b2836b795c7e | -22.29071 | -49.88922 | 2025-10-12 04:17:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 965b1f38-404d-3cb4-9765-b728b0f93b8b | -17.18892 | -46.96441 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2610754e-dc0f-3ec7-8029-45be3720a4e4 | -14.90296 | -48.48592 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a5ca29c-54b2-3799-8dd5-de5761422323 | -15.68136 | -46.63955 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19a77b45-72fa-3021-ad75-4537a6fd41d0 | -16.34167 | -42.38693 | 2025-10-12 04:17:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f91ed1a-3013-3de9-ae8b-e7b74ba5696f | -15.6877 | -46.6218 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70ddac98-6fed-367c-9779-0d30e4db9213 | -14.94911 | -46.72765 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfb0b4a3-c169-30ae-83a1-8d4018ddb216 | -19.53333 | -43.05608 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 521b0258-aa68-348f-9935-02b01c77e8b4 | -19.01965 | -43.1702 | 2025-10-12 04:17:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0952f7f2-87a9-3dd7-8e4f-094e60d5b35e | -11.85782 | -56.87013 | 2025-10-12 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f50e091e-253c-3b17-b272-75ec8afac245 | -15.49914 | -45.93267 | 2025-10-12 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dc1bb2b-f6b1-3f37-aa6c-4ddba823ecb3 | -12.13557 | -45.58968 | 2025-10-12 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1c72a78-4eff-31cc-b382-2e93cc956235 | -14.92912 | -46.74385 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7828559e-45a7-37d7-83b3-ebde24f2317b | -15.22617 | -56.8734 | 2025-10-12 04:17:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README24.md)
