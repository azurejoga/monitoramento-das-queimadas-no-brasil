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
| 44a629bd-712a-3160-8429-77f2e166e4ec | -3.5559 | -53.0021 | 2024-11-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 67953e84-4259-3216-8350-10ed196d27bc | -21.2181 | -47.1261 | 2024-11-13 00:30:00 | GOES-16 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 441bab78-9323-33d7-afd4-75a44e8880f7 | 1.0663 | -60.5985 | 2024-11-13 00:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 23c2a3d7-d6cb-3dac-a3d5-507ed09ecb7d | -10.7425 | -49.5244 | 2024-11-13 00:30:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 88de526d-96a1-3bb3-9434-3df6c46fdf58 | -3.0504 | -50.3332 | 2024-11-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 0ff235fc-eb10-34cd-b6f1-45df0e4ab292 | -3.1501 | -53.2574 | 2024-11-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| b0d840b9-33ab-34c3-b196-ca478068e2c6 | -3.2495 | -43.2547 | 2024-11-13 00:30:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| fc75bcb5-efa1-3825-8776-b4214df2a1d9 | -2.2479 | -53.7627 | 2024-11-13 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| c6f14158-5023-3a50-b99c-54c2d1191740 | -3.4914 | -50.8213 | 2024-11-13 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| f57376be-63db-3c5c-aa84-d5b1e30c0995 | -2.248 | -53.7426 | 2024-11-13 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 293.9 |
| 352c1e2b-a4fe-39aa-8b58-15ed05f6deb2 | -2.7033 | -49.3513 | 2024-11-13 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 691fd9d0-0586-3f00-b9cf-0acecb3f0bfe | -4.408 | -48.8403 | 2024-11-13 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| eacf9cd7-480f-3531-890d-5bf0aec1d49b | -3.5928 | -53.0009 | 2024-11-13 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5826d7f8-7726-3df4-8e4e-6d5e883bfe1e | -3.0689 | -50.3326 | 2024-11-13 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 9183d5eb-3e42-3113-b0a6-4e14b4afd723 | -2.2112 | -53.7432 | 2024-11-13 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c54ad995-e024-363d-b655-862750f27caa | -10.0448 | -36.3475 | 2024-11-13 00:30:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 88.9 |
| f3322d2c-0bf4-3682-995d-d14d06e25b33 | 1.0663 | -60.5985 | 2024-11-13 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 7b19f45a-897c-3579-b403-09da259273b4 | -3.5743 | -53.0015 | 2024-11-13 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| ae749746-d63d-33f1-b12a-f3e7ea88e1eb | -3.5743 | -53.0218 | 2024-11-13 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 1925944e-3c29-3912-b6c7-86c0a5229d64 | -3.5098 | -50.8415 | 2024-11-13 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 26d4cdb9-71de-3db6-8204-ab760c0ae451 | 1.048 | -60.5986 | 2024-11-13 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 145.4 |
| ffaa100d-3b3a-30c6-9ba5-81f4d4283cb6 | -2.9924 | -51.045 | 2024-11-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6b38fb4b-77a7-3ca6-8031-d13868413c44 | -2.7189 | -45.2883 | 2024-11-13 00:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 7490ca69-07a8-381f-9b56-8c8644d069b5 | -5.3587 | -43.529 | 2024-11-13 00:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b5e6c2b8-4e8f-35f5-ba8a-88c4c801fdad | -3.0689 | -50.3326 | 2024-11-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 9abb2739-5de7-3828-826c-91af046b293a | -4.4265 | -48.8395 | 2024-11-13 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e32158fd-038f-3728-acc4-171d7fe8cae0 | -3.0504 | -50.3332 | 2024-11-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 51fe5c13-a59f-335d-ad12-ce304495da9c | -10.7425 | -49.5244 | 2024-11-13 00:40:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| cbb21229-7281-30aa-87b6-f8a368e58e00 | -1.8798 | -54.211 | 2024-11-13 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8e5e6258-a925-3bb3-b53c-e3cc7faf0609 | -2.9925 | -51.0242 | 2024-11-13 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f02008a8-b6b7-3fa5-9346-79b25e8ca883 | -2.7033 | -49.33 | 2024-11-13 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d9cc6fb6-2b5b-33cf-9794-a27ec98334c7 | -3.1096 | -54.3066 | 2024-11-13 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6f4f01a2-5a03-33a7-b958-ce3a13770e8a | -2.7033 | -49.3513 | 2024-11-13 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 064b962f-d1e7-3aa0-b048-0548643e73ba | -2.6848 | -49.3518 | 2024-11-13 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 8cd55d27-9a0a-397a-9d66-bff41874813b | -3.1501 | -53.2371 | 2024-11-13 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 8f295e53-efea-3317-b21d-b5cd60d58fb3 | -21.2181 | -47.1261 | 2024-11-13 00:40:00 | GOES-16 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |
| ef9ec1d6-06b0-3922-aee3-419f9016b78a | -2.7374 | -45.2877 | 2024-11-13 00:40:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1429de1a-a40e-3d8e-bed1-2f3b931299f8 | -10.5576 | -36.7374 | 2024-11-13 00:40:00 | GOES-16 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 75829242-28ab-3aba-85e6-066fd2ee5327 | -3.5099 | -50.8207 | 2024-11-13 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b306c6a6-7e4f-320e-a084-0f3d00a65cff | -2.7189 | -45.2883 | 2024-11-13 00:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 992ede56-792b-3b14-9fde-4fe1f6956bcb | -5.3587 | -43.529 | 2024-11-13 00:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2bb13fce-b71b-3c12-bd0a-b258f9035345 | -2.9924 | -51.045 | 2024-11-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5ed3cebb-6b4c-3813-aa55-22a3b2f49d55 | -3.0689 | -50.3326 | 2024-11-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 72eba7ca-cf2a-304e-9682-b7b86a60e16e | -2.7374 | -45.2877 | 2024-11-13 00:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0f4b830e-8f3f-3958-8126-db89a9d51601 | 1.0663 | -60.5985 | 2024-11-13 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 38da3a9c-6416-354e-926c-dba8837b9ddd | -2.9925 | -51.0242 | 2024-11-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ce6f36e0-d99b-3ca2-a8f7-6b2ed0285d1b | -3.5743 | -53.0218 | 2024-11-13 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 09daf274-d71a-3fac-b435-e10bfe647cac | -3.1096 | -54.3066 | 2024-11-13 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 674e2ed7-24d6-3df9-9250-53d6eb1b9ba2 | -2.7033 | -49.3513 | 2024-11-13 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b2d2ec5e-de4e-375e-8308-67ec3dc310e6 | 1.048 | -60.5986 | 2024-11-13 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.4 |
| ccbe8e1f-1214-3842-ae6a-ba4cac2fe6c7 | -3.1501 | -53.2371 | 2024-11-13 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| bc9e7819-db50-33a7-9857-e8109872963b | -4.3434 | -50.4123 | 2024-11-13 00:50:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1e183142-13a4-3376-ad2b-8893686bf8bf | -3.0504 | -50.3332 | 2024-11-13 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 6d77c779-149c-3a20-9520-57c13172db6e | -3.5743 | -53.0015 | 2024-11-13 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 8ec46022-2916-38bb-b0a4-d66a1a6cd299 | -3.4913 | -50.8421 | 2024-11-13 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 14a0b318-a401-3538-b847-51a5b0a276fb | -2.7033 | -49.33 | 2024-11-13 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| e605828d-c966-353e-99d4-939311364093 | -1.8798 | -54.211 | 2024-11-13 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 807f7439-9ef1-3230-9173-5e89e7a732f6 | -2.6875 | -49.349499 | 2024-11-13 00:50:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e16bc1-6b97-3422-a8b1-c46d2dd5da21 | -4.4047 | -48.833599 | 2024-11-13 00:50:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7336ed2c-aaad-3a6d-8522-8d04984f18a9 | -3.2501 | -50.398102 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b4a721e-4aae-3f64-b055-7d750674e124 | -3.4127 | -51.054901 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c4f5ca4-c146-3aaa-a6b6-cda0689a7107 | -4.3251 | -50.420399 | 2024-11-13 00:50:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58af4af2-7ef2-3e50-aba4-779820bbf502 | -3.7613 | -54.6437 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9daab012-2eb4-35f4-907b-663385c7c0ea | -2.9354 | -54.456001 | 2024-11-13 00:50:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7836e7d6-7f5d-3555-9150-15b709b8b13d | -3.5031 | -54.6866 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0236ff2f-f41b-300c-8d0b-228689c15060 | -4.3226 | -50.409401 | 2024-11-13 00:50:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0443beb-5d0c-34f6-ae1b-a18356f9d430 | -3.5734 | -53.005402 | 2024-11-13 00:50:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf28f839-592e-3bee-84c1-3d928a8b56a5 | -4.3982 | -49.634102 | 2024-11-13 00:50:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21bbcdcc-60bd-3268-9e37-475ccd27e59c | -2.5658 | -48.126598 | 2024-11-13 00:50:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e55df3c-8c09-330a-9be5-95d9c30b3bd1 | -3.8028 | -52.3438 | 2024-11-13 00:50:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4dbb226-08f9-35dc-979b-6edffe32b7c3 | -4.1629 | -59.893002 | 2024-11-13 00:50:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89891bab-870c-311e-bddb-11d932b1d76b | -2.8794 | -54.164299 | 2024-11-13 00:50:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aac957f4-8946-3cca-ac26-bde18a65d1fd | -16.128799 | -43.552399 | 2024-11-13 00:50:00 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 151d2e0e-0b11-3953-8909-1110141e7d29 | -4.109 | -54.223099 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8ac1bba-dd45-3f9a-a097-0f6d0dfa9ab3 | -3.157 | -50.573399 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76424b7c-ba78-315d-a1ef-1269e1a46a3c | -3.1596 | -50.584499 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0841d86-f840-3109-9ffc-9232d7660e66 | -2.9442 | -51.9692 | 2024-11-13 00:50:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfef5d3-4899-3749-8e9d-d24c29ace928 | -3.1577 | -50.443199 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0693633c-1fc9-3448-a568-4c5b85e37212 | -2.8342 | -53.965302 | 2024-11-13 00:50:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26264439-30cd-353d-bbf9-1c308c5f0064 | -4.408 | -48.8475 | 2024-11-13 00:50:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0e593ca-0427-3e09-a720-2eeb162b35d6 | -2.9978 | -51.040798 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d715eaee-9b1f-33c1-bff2-7fca4a6c62d3 | -2.9896 | -53.969398 | 2024-11-13 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2dc7f94-d914-3abd-bf45-43d8de810d94 | -3.7621 | -47.466301 | 2024-11-13 00:50:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ade92bb7-dc94-3174-9ee8-6cc169207b74 | -20.9828 | -47.402 | 2024-11-13 00:50:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 14168bab-847c-3f94-8270-389163d08678 | -3.7328 | -54.427399 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab10c65e-cf62-3854-b779-8d9b322ad9b9 | -2.9798 | -53.9716 | 2024-11-13 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6868f83-8c7f-3132-a5aa-71408be8cdda | -2.9735 | -51.3368 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac4e5bc-6021-3d83-9f82-159aa44edbdf | -3.4841 | -54.013401 | 2024-11-13 00:50:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f39f4e03-4996-3122-87f6-61a51bea11ec | -3.53 | -54.487701 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f205d1a-fa4c-3d7c-a658-adebcf350494 | -29.5277 | -49.878799 | 2024-11-13 00:50:00 | METOP-B | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | nan |
| a182df12-fc4d-38df-95fe-e8eb184ac130 | -3.5751 | -54.640999 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf099f72-894f-3105-add6-9a1e15fd99d2 | -2.9337 | -54.448799 | 2024-11-13 00:50:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2136bc1b-eb2e-3405-ac79-8f47174a1cdf | -2.7795 | -48.076801 | 2024-11-13 00:50:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee8768a-2d14-3d6d-8878-910c5769c1b7 | -2.1156 | -50.693401 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ac750f-d7a0-3b8c-8d71-96ae1d237f1e | -3.0504 | -50.3353 | 2024-11-13 00:50:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf00f6ab-d0f7-31ea-8ac5-fc6072e6ec5f | -3.5735 | -54.633999 | 2024-11-13 00:50:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9162d72-ffc5-3248-a59e-2ab907e43438 | -3.4937 | -50.827499 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12dea120-4c39-3344-b22d-877d830219ee | -29.5261 | -49.870899 | 2024-11-13 00:50:00 | METOP-B | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 7485d789-9d31-3fde-918e-633a4c0d40fc | -3.484 | -50.8298 | 2024-11-13 00:50:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1481384c-f0c9-33c5-8e44-192cc3d154fb | -2.9758 | -51.346802 | 2024-11-13 00:50:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
