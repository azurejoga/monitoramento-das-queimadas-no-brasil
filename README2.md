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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a73bfd02-315f-3f4b-b84f-6608d595e9ea | -10.81824 | -54.02017 | 2025-05-27 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b3404fa5-0e4b-3b0e-b9ec-4445b828c70f | -10.82466 | -56.95518 | 2025-05-27 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| dbb1ee30-e0de-3b76-8ea0-ded37a648b3e | -8.42664 | -46.658 | 2025-05-27 01:17:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f68a2312-728e-3d00-9634-fe7d06b3f3e8 | -10.82589 | -56.96412 | 2025-05-27 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 479b0f20-d92d-30e1-8eb9-e3d12c99dfa0 | -8.75248 | -49.77225 | 2025-05-27 01:17:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2a8fdf95-e6da-3e5f-91d8-481abcc43852 | -11.13882 | -53.91927 | 2025-05-27 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 28bb8a13-e62b-336f-ad35-b7b0d4f17ffe | -10.83471 | -56.96284 | 2025-05-27 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 15ad6233-37bf-3913-912a-9b96ec40a14b | -13.1498 | -56.8054 | 2025-05-27 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| cdf1d9d2-aa86-3d46-b8f6-cfaad82cc16e | -7.2025 | -43.1171 | 2025-05-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 8d10781e-4eb4-3332-acea-e72b495ceb55 | -18.8479 | -53.6251 | 2025-05-27 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 48.8 |
| d5819c0f-bdb3-32e3-8898-2de136f934e1 | -18.8484 | -53.6035 | 2025-05-27 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 51a0913a-448a-3cb4-9f6b-50f03b63a63e | -7.2214 | -43.1153 | 2025-05-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| a9e0017b-a597-32e1-982a-2fe35a79874f | -22.2257 | -48.6155 | 2025-05-27 01:30:00 | GOES-19 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.5 |
| 0ba0c6ad-1532-3785-956c-1f25d7048315 | -7.2214 | -43.1153 | 2025-05-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 7a485f02-8280-3d5b-aff9-5c8a2b124817 | -19.4239 | -54.774 | 2025-05-27 01:30:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 72adb1d2-3035-32d0-9809-4eee06dd70b3 | -18.8484 | -53.6035 | 2025-05-27 01:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1108172b-cc84-3bfb-a9b3-58bd7604ec7e | -13.1498 | -56.8054 | 2025-05-27 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 462a2cb9-2a41-36aa-9c31-51142bddb03a | -7.2403 | -43.1134 | 2025-05-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| 8d0cc336-5717-3cfe-b63a-2e86fec1cfdc | -7.2025 | -43.1171 | 2025-05-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.0 |
| 17b1621a-bc05-31d0-ac65-7d879b352c41 | -7.2028 | -43.0936 | 2025-05-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| e9d76fe0-452f-30f8-b26b-24cd00e1d798 | -19.444 | -54.7708 | 2025-05-27 01:30:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9c9f3d0f-82a3-3304-b47a-f28f5d588cb7 | -7.2214 | -43.1153 | 2025-05-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.6 |
| 128fc1e9-0e30-34eb-837c-1bb34ac5e280 | -7.2025 | -43.1171 | 2025-05-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 146.6 |
| 251a5156-61f9-3ac8-bb18-2736794e00e3 | -7.2403 | -43.1134 | 2025-05-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 7cb8439e-37fb-3448-b9fc-d5984687d9d7 | -18.8479 | -53.6251 | 2025-05-27 01:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0eac8aa5-94c2-3f7c-a666-0c3eaa4f7ef7 | -18.8484 | -53.6035 | 2025-05-27 01:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 31ae0023-889d-3946-bbd5-f613ab2cdaec | -7.2028 | -43.0936 | 2025-05-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 74c28471-bb82-3344-8a81-04342332a064 | -7.2025 | -43.1171 | 2025-05-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 192.9 |
| 3900613b-c610-32c6-b875-7426820aa896 | -7.2217 | -43.0917 | 2025-05-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 8a00be72-29c6-3d87-8f77-d21e100f5846 | -7.2214 | -43.1153 | 2025-05-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.8 |
| 21160b8a-f1ea-34d2-b467-8f4a4c60344c | -18.8479 | -53.6251 | 2025-05-27 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 54.5 |
| c49e10a2-dcfc-3e0e-b231-00cd2079fc05 | -18.8484 | -53.6035 | 2025-05-27 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.7 |
| decdca96-9945-3da7-9db3-20cc4e897a82 | -7.9051 | -63.6001 | 2025-05-27 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8f5e3805-a6c8-3e5b-a5e7-543909345c17 | -7.2403 | -43.1134 | 2025-05-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 3438e5d1-8650-31d4-8cfe-8dd549166982 | -9.4956 | -40.3586 | 2025-05-27 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 60805d7e-92f9-3bf5-978c-4a38591c885c | -18.8479 | -53.6251 | 2025-05-27 02:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cf7e98f0-1b82-3c3b-8088-b8c5f59a2e5d | -7.2217 | -43.0917 | 2025-05-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 70c82d0b-8e8f-3144-9041-c0fa7918f577 | -18.8484 | -53.6035 | 2025-05-27 02:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 100.8 |
| b3e1b807-4b4e-3364-9aa6-98817aab5104 | -9.5147 | -40.3558 | 2025-05-27 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 1cd9809e-68a1-31f8-ae88-c088a3283012 | -7.2028 | -43.0936 | 2025-05-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 8ed4edb9-32eb-3b69-b397-65f494c1d22b | -7.2025 | -43.1171 | 2025-05-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 182.1 |
| 804569fa-22a8-32e5-84a8-738625e769d8 | -7.2214 | -43.1153 | 2025-05-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| ac6e6328-5d4e-3a42-9dc3-5ab3278349d4 | -7.2214 | -43.1153 | 2025-05-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 120.1 |
| aa02ca5a-1e61-3114-82ba-7a7899e80f6e | -7.2403 | -43.1134 | 2025-05-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| ec2d7eb8-bf14-311f-806d-185166df4036 | -9.4964 | -40.3088 | 2025-05-27 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 54b7b0b7-1875-31ee-b5e2-a50d06af2318 | -7.2028 | -43.0936 | 2025-05-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 60ce4301-435d-337c-9dd4-350cfb2160b8 | -7.2025 | -43.1171 | 2025-05-27 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.7 |
| 5aff256c-4753-3ffc-84dc-a8b820054371 | -7.2214 | -43.1153 | 2025-05-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 9b3651a6-a65a-38c6-8cc4-581804e9d78f | -7.2403 | -43.1134 | 2025-05-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 49708341-2601-33fe-94b1-524b9313fb5f | -7.2025 | -43.1171 | 2025-05-27 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.4 |
| fc2c188c-0607-3674-a8ad-eb655348cbe9 | -19.444 | -54.7708 | 2025-05-27 02:20:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 52.8 |
| e06afd26-3e6e-3144-8b89-6736318e2c92 | -18.8479 | -53.6251 | 2025-05-27 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 122.4 |
| fbd6aa54-8e7a-3b0b-a6be-c5cc3fa6ca3e | -7.1591 | -47.1228 | 2025-05-27 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 17c6275d-559a-301a-aa4d-2bea1e1eafcf | -7.1589 | -47.1448 | 2025-05-27 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d25e16d6-4df3-373c-92bb-7b335f894979 | -7.2025 | -43.1171 | 2025-05-27 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.2 |
| 73db2a60-4706-393e-bdb0-c3bca919edc3 | -18.8284 | -53.6067 | 2025-05-27 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 55.4 |
| b38d2d84-8cb5-3503-8ce9-5d493d0676dc | -7.2214 | -43.1153 | 2025-05-27 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 5f07c588-72d1-3768-9763-43f159471d34 | -18.8484 | -53.6035 | 2025-05-27 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 2bc557f7-af36-3b66-8198-b2b0c565fa25 | -7.1778 | -47.1212 | 2025-05-27 02:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b902b310-61ef-3722-81ea-e482d18bb719 | -18.8679 | -53.6218 | 2025-05-27 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 01e6af67-af18-300a-aaab-5ea8b3d11869 | -18.8488 | -53.582 | 2025-05-27 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 13ec48f6-9276-3618-accd-96e9de21640f | -18.8479 | -53.6251 | 2025-05-27 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 23947def-729d-31d6-bdf8-998af62f876e | -18.8284 | -53.6067 | 2025-05-27 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 724882d7-bc98-3379-9ace-3becdbb1836c | -19.4239 | -54.774 | 2025-05-27 02:40:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 117fd425-4b24-3d3b-ace4-1e7528940f99 | -18.8679 | -53.6218 | 2025-05-27 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 1dc5e085-729f-39da-b481-8d59405836bb | -7.2214 | -43.1153 | 2025-05-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| e4051ed2-1413-3c14-b1b6-2b834bf4f19b | -18.8484 | -53.6035 | 2025-05-27 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 5e8ef010-00cc-309a-84ed-7b8a1e0da0df | -7.1589 | -47.1448 | 2025-05-27 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b7467137-87bb-3074-bfec-94b966fdc327 | -7.2025 | -43.1171 | 2025-05-27 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 6c3b784e-d9fd-3981-9a96-d1bf0ca2e020 | -7.1776 | -47.1433 | 2025-05-27 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 0ba9d74e-c4a9-32a4-a919-baa1eddb7f38 | -19.444 | -54.7708 | 2025-05-27 02:40:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 56.0 |
| afde6294-bf75-346d-87e3-487f817d1e8f | -7.1778 | -47.1212 | 2025-05-27 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 902f12d9-942a-3529-b205-dd092577b321 | -7.1591 | -47.1228 | 2025-05-27 02:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 5c667c78-77ea-3037-af53-29322e67a97e | -7.2214 | -43.1153 | 2025-05-27 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 3461be35-7a2b-3293-a644-1f3e14b55d4e | -18.8484 | -53.6035 | 2025-05-27 02:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e0d17c50-26e9-330a-97ce-a5c6d7f24174 | -7.1591 | -47.1228 | 2025-05-27 02:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 53d77c21-37d5-349f-b394-5e3282ca50c7 | -18.8479 | -53.6251 | 2025-05-27 02:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 8e762e1a-0e35-3890-8ff1-60172aeae308 | -7.2025 | -43.1171 | 2025-05-27 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| 7a4307d7-0624-3b07-a038-4e42c2848ca4 | -7.2025 | -43.1171 | 2025-05-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.8 |
| e91ed83d-b914-34ae-9008-4fb8ccebb54d | -7.2214 | -43.1153 | 2025-05-27 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 8fe39141-6493-310e-b284-f0f46e5c2d67 | -5.95963 | -36.09731 | 2025-05-27 03:08:00 | NOAA-20 | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1e7cd83c-627d-3e7e-b5bf-44a479d1cb63 | -5.95998 | -36.0989 | 2025-05-27 03:08:00 | NOAA-20 | SÃO TOMÉ | RIO GRANDE DO NORTE | Brasil | 2412906 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b47203af-d0b8-30d2-a6cd-722c4252b302 | -7.2025 | -43.1171 | 2025-05-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 3f588e1d-03c4-3055-8d62-44673c110208 | -7.2214 | -43.1153 | 2025-05-27 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 19f0e7bd-9207-3065-b327-2ef705a33f8a | -9.49763 | -40.35089 | 2025-05-27 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5932330e-351b-35a1-9c1b-932e942f6453 | -9.49871 | -40.34747 | 2025-05-27 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 96ffa3f3-21e0-3388-80f2-4e003ddc4f5a | -9.49766 | -40.35299 | 2025-05-27 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 30804234-05bd-3e3d-bba9-072dec462f0b | -15.80283 | -43.57101 | 2025-05-27 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff35aaa7-53bd-368d-b312-99a662054f15 | -15.88409 | -43.46207 | 2025-05-27 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 98086c88-5ef9-3ca3-9bfc-d1f48e616e74 | -15.89129 | -43.45637 | 2025-05-27 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9a24de-d67a-3bd8-8d3a-2af861053992 | -15.88969 | -43.46326 | 2025-05-27 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ca9c6b1-2163-30b3-b3e7-0d3e89c423be | -15.7959 | -43.56924 | 2025-05-27 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 89fb6aa2-6d86-3d25-8b2b-1b55fc63231d | -15.80054 | -43.57204 | 2025-05-27 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5f4e8d08-f2ef-39ae-bb78-18f3f5312a09 | -15.88565 | -43.45522 | 2025-05-27 03:13:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 60bb7d2d-c73f-3959-9987-1ca35311377c | -18.8684 | -53.6003 | 2025-05-27 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 2816601f-d7d8-3f49-b077-099673bec7c5 | -7.2214 | -43.1153 | 2025-05-27 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| d13db978-9212-3183-8903-3733708cb317 | -18.8679 | -53.6218 | 2025-05-27 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 04044a0b-55f3-3241-a589-4e17ff7014d2 | -18.8484 | -53.6035 | 2025-05-27 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 862f74fc-db10-3b14-aac2-a9c82aea7f19 | -18.8284 | -53.6067 | 2025-05-27 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8f6e4abf-2841-37fe-ac0c-6c4f39a4aa6d | -18.8479 | -53.6251 | 2025-05-27 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 190.7 |


[Clique aqui para ver as próximas entradas](README3.md)
