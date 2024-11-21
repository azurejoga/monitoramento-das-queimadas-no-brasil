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
| 129255a6-9f6c-3261-b464-0b5ccfb64a31 | -6.214 | -46.2202 | 2024-11-21 01:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d1865dce-f54f-3eb9-b074-54eb8c6deec5 | -3.3739 | -52.4773 | 2024-11-21 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 6695109a-d491-315f-a042-83f8160fe0df | -3.3924 | -52.4563 | 2024-11-21 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 689069c9-543d-363f-b41a-7da044708096 | -1.7556 | -52.0636 | 2024-11-21 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a6cdd4ec-ca2c-3fe6-bd87-b732f5cb6144 | -2.7676 | -52.1045 | 2024-11-21 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 6cf15238-b1a9-3405-a89c-5b8ffa88d6db | -3.1831 | -54.3247 | 2024-11-21 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b5f58265-7fa5-3e69-a3b9-2140417c212d | -3.2768 | -53.8199 | 2024-11-21 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| bed2a079-ab1a-3329-a143-008c33e17476 | -5.1 | -43.16 | 2024-11-21 01:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee9d311d-17b0-373b-b2e7-16328654d969 | -4.58 | -48.0132 | 2024-11-21 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 182.7 |
| 09e1b129-0073-369b-abba-8e237d8ada52 | -5.1183 | -43.1731 | 2024-11-21 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 9f8d2d4a-02fd-3d2f-9b03-6907266fb5c3 | -3.3924 | -52.4563 | 2024-11-21 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 55032814-d4c9-3821-9b56-025f1810ccd0 | -1.7557 | -52.043 | 2024-11-21 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d5f5456f-75c4-3637-afb3-d7a9c4cf280f | -3.8167 | -52.3403 | 2024-11-21 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7a0bd4bd-781d-3b58-8b44-de65a962e6f6 | -4.16 | -43.8818 | 2024-11-21 01:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2d7ae208-fa42-35ab-810b-e7d88250c44c | -6.8258 | -46.7737 | 2024-11-21 01:10:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 2d5b2488-cca5-39ee-b9ff-4a6448c22c50 | -2.7676 | -52.1045 | 2024-11-21 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| f3881b73-3190-382b-8794-d8f4a5bbf50f | -3.2951 | -53.8395 | 2024-11-21 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| ad239bbb-4ea9-3c7d-be51-f7b5440afb1b | -2.6076 | -45.2469 | 2024-11-21 01:10:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 4a28e0ea-a49d-31b8-91f4-2a8ecb9db68a | -2.7491 | -52.105 | 2024-11-21 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| aaa0b9da-5d72-30bb-971c-d6987795d26e | -4.5799 | -48.0349 | 2024-11-21 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 82f535aa-04e0-3a2c-aa43-356d969c3464 | -1.7556 | -52.0636 | 2024-11-21 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| b9e04ee0-a770-3108-affe-7e2f6a07100f | -3.374 | -52.4568 | 2024-11-21 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| e90680d0-33fa-34b6-b6f0-744601646997 | -5.0996 | -43.1744 | 2024-11-21 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 2c0dc6f6-5891-39ef-b067-519c7d858590 | -4.3911 | -45.5977 | 2024-11-21 01:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2c6971bc-4253-377c-84fe-dd49f29497b5 | -2.0075 | -54.5292 | 2024-11-21 01:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 8ef3a4e2-96a7-306d-a534-4d5060d18c78 | -5.0998 | -43.151 | 2024-11-21 01:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3769f1e9-84fa-3fbb-933e-7d96f9494e58 | -3.2768 | -53.8199 | 2024-11-21 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ec0c9396-43d4-3ff0-8de6-ea4dd8b7227d | -1.7372 | -52.0639 | 2024-11-21 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1b5bbc68-5314-3f2e-9613-6525564adad6 | -3.3923 | -52.4767 | 2024-11-21 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 73cb799e-955e-3875-93d3-9fbc3c22f5f2 | -3.2767 | -53.84 | 2024-11-21 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| d29314c5-c508-3b00-96b9-57fd39c681dd | -10.1223 | -65.0237 | 2024-11-21 01:10:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a4e1fc34-5921-368a-a4f9-af791b91edf7 | -3.2952 | -53.8194 | 2024-11-21 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0a427d59-0c5a-3e40-9cff-14781b9128b3 | -3.0354 | -49.4688 | 2024-11-21 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| decf0b57-bc28-3174-ba05-a1a2a80c78f4 | -3.6018 | -43.6331 | 2024-11-21 01:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| eee838c7-ac20-3530-a00a-9deb61e4d025 | -4.5986 | -48.0123 | 2024-11-21 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 79cabccc-90b6-3df7-994b-97a92b54d221 | -2.0259 | -54.5289 | 2024-11-21 01:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| cacd9023-810c-33fc-ab07-8b13d22828ae | -4.1413 | -43.8828 | 2024-11-21 01:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| fa9ca4bc-3a7c-31c9-b070-689929d755d4 | -4.5614 | -48.0141 | 2024-11-21 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| d3047da7-f17c-3582-86c8-44876a41af01 | -3.3739 | -52.4773 | 2024-11-21 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d7b106c2-0a16-3d1e-96c3-41d7fd4386fc | -3.2014 | -54.3243 | 2024-11-21 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 86d73c2c-2c9b-3a03-8a30-ac0454c74c73 | -2.7675 | -52.1251 | 2024-11-21 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| e935dd34-073e-3d0f-a3f8-499b8c7384f9 | -5.1183 | -43.1731 | 2024-11-21 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a444ecc6-9fbe-3c7a-9f65-f96c189400e7 | -4.5986 | -48.0123 | 2024-11-21 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 45faf591-0cee-3b0c-a4b7-21a6736772b1 | -4.5799 | -48.0349 | 2024-11-21 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 458015f4-5333-350f-9e83-cd7cedc773ce | -3.6018 | -43.6331 | 2024-11-21 01:20:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b0bc0748-8685-39b8-ac43-ba9705e5b683 | -3.8167 | -52.3403 | 2024-11-21 01:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 04c23f42-d330-307d-bcd8-0a3d37627dd0 | -4.5614 | -48.0141 | 2024-11-21 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0c36984d-daae-3da1-b85c-8a59562ab872 | -2.0075 | -54.5292 | 2024-11-21 01:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 02fa4340-7da8-3511-9e1d-739781cdd26e | -4.1413 | -43.8828 | 2024-11-21 01:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 881a6544-584d-389b-aa30-f2df31449bec | -10.1223 | -65.0237 | 2024-11-21 01:20:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| bf6f99c5-da22-312b-82e8-98aa2905dc74 | -2.7675 | -52.1251 | 2024-11-21 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 86bb5c79-ffe1-3d09-93a9-dbc159806146 | -6.8258 | -46.7737 | 2024-11-21 01:20:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5164b8f2-b6f2-3663-aee3-887e24bc8518 | -3.2951 | -53.8395 | 2024-11-21 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 3cf274ed-668e-35ed-b9f2-885da52fb9b2 | -5.0996 | -43.1744 | 2024-11-21 01:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 26ace4e3-64dd-3063-a0ca-a750bad5fbaf | -1.7556 | -52.0636 | 2024-11-21 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2c6f56fb-937a-30fe-b7c2-a324fbb2dc88 | -3.2767 | -53.84 | 2024-11-21 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 6d8c4040-ed91-372e-9289-fbc119fbbaf1 | -2.7676 | -52.1045 | 2024-11-21 01:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ad698c9a-3e48-3321-8a15-ee0eab1e9acc | -9.9324 | -36.1788 | 2024-11-21 01:20:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 0f8a54b3-4d31-37c9-b57b-4857b53558ad | -3.374 | -52.4568 | 2024-11-21 01:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 166.0 |
| c6130392-b9ca-328c-8db9-c76293cd3bca | -6.214 | -46.2202 | 2024-11-21 01:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 93ef8e96-c8f3-30c0-8fa1-01a4b04130cc | -4.16 | -43.8818 | 2024-11-21 01:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 81b5176d-3554-3f9b-95a4-f25e6bba5262 | -3.2014 | -54.3243 | 2024-11-21 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 09b22e7d-cbfc-3d6b-91af-bc8940d60f27 | -3.3924 | -52.4563 | 2024-11-21 01:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 8e199505-ef4a-316a-bb45-1efcda7665d8 | -3.2952 | -53.8194 | 2024-11-21 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 28a1c64e-b799-3200-a58a-4192c651272c | -3.295 | -53.8597 | 2024-11-21 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 984fe8d0-aac8-3c38-a29b-266708855cb0 | -2.0259 | -54.5289 | 2024-11-21 01:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4d84317d-1177-3987-b0cb-32f1cdd1c441 | -9.9329 | -36.1517 | 2024-11-21 01:20:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| 1f4fa5d5-12c2-3574-b66c-ecffcf53ff11 | -4.58 | -48.0132 | 2024-11-21 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 6a4f6eaa-eecd-3050-ba7e-5142b747a674 | -4.5799 | -48.0349 | 2024-11-21 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 07e226d4-7f09-35a3-863c-38dbf4d58b0e | -4.7717 | -44.4891 | 2024-11-21 01:30:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b06b2759-fec8-3b98-8315-7a4fc8811251 | -3.295 | -53.8597 | 2024-11-21 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 49d6c665-30f7-3c38-b0b2-795a48576c62 | -6.8258 | -46.7737 | 2024-11-21 01:30:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e96c742f-1acb-3402-b1e5-254f1617a933 | -2.7676 | -52.1045 | 2024-11-21 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| fd0e6c47-08a3-33b7-a1a4-32d4ef8a06ab | -3.8167 | -52.3403 | 2024-11-21 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 233c1b52-33a2-3d3a-aeb0-9e80f9ed87ec | -3.0354 | -49.4688 | 2024-11-21 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 302ef61e-0c2c-3eda-bfed-ef07b610d01d | -2.0075 | -54.5292 | 2024-11-21 01:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 321201a5-d533-3bd7-ad9a-9829729b78b6 | -3.2767 | -53.84 | 2024-11-21 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| b12bf224-0d56-3ab6-8173-3fd40dddd06e | -3.2951 | -53.8395 | 2024-11-21 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| bfabe9c1-86b2-3a88-a6ca-470b276ca07d | -6.214 | -46.2202 | 2024-11-21 01:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d836068b-7da3-3376-8e58-e5c9e30fc65e | -4.5614 | -48.0141 | 2024-11-21 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4e115947-f135-3b03-a5eb-acf97b0ee48b | -3.2768 | -53.8199 | 2024-11-21 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 57087ed9-0712-3310-8844-989667ef8efb | -3.2014 | -54.3243 | 2024-11-21 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 384fbae2-aa80-36f9-a12d-adbfd66fa967 | -2.0259 | -54.5289 | 2024-11-21 01:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 00c4ab0d-20e2-3b40-b27e-8e81dc434bd1 | -3.374 | -52.4568 | 2024-11-21 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 2bc173ef-7061-3ca9-b974-eec86a354ae4 | -4.58 | -48.0132 | 2024-11-21 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 191.1 |
| f9e323bf-559f-35f6-b189-db92f30c77b7 | -2.7675 | -52.1251 | 2024-11-21 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d4de3c2f-61bb-35b3-87c5-cdc601d443da | -3.2952 | -53.8194 | 2024-11-21 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 84dc6c13-fc1d-30c6-99e6-46bb66ef8bff | -4.2388 | -46.1197 | 2024-11-21 01:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 20808472-5bc2-34b5-8fd8-d6ce5f07b5ca | -4.1413 | -43.8828 | 2024-11-21 01:30:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a153a441-4bd6-3285-ac0b-5f14cd6474b6 | -10.1223 | -65.0237 | 2024-11-21 01:30:00 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a00ef3b5-cb4d-3efc-bfae-5681eb03c65f | -4.2575 | -46.1188 | 2024-11-21 01:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 1e1488fb-a7c7-3316-aa53-a255aac3e1d0 | -3.8166 | -52.3608 | 2024-11-21 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c0a2d17a-4b4b-3846-ac48-e9919f0a1cbf | -3.3924 | -52.4563 | 2024-11-21 01:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e44810a0-807d-3273-a4c3-8fc9304738f8 | -2.0075 | -54.5292 | 2024-11-21 01:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ff489d05-4794-3380-b316-983fa381f19b | -4.5986 | -48.0123 | 2024-11-21 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3b250832-6820-3d02-8b45-751d5444ec3d | -1.601 | -46.8729 | 2024-11-21 01:40:00 | GOES-16 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 2378db02-9914-35a8-8036-eb949fa5084c | -3.3924 | -52.4563 | 2024-11-21 01:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 5a4381e2-96ab-3690-9d49-48af165dc695 | -3.2767 | -53.84 | 2024-11-21 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 337022c6-3d36-3a12-972e-c239f55d9fb6 | -4.58 | -48.0132 | 2024-11-21 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 178.3 |
| d3c72ba7-e8a8-35ce-a411-3f005cd06a9a | -4.2575 | -46.1188 | 2024-11-21 01:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README8.md)
