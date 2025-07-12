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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75e7b9b7-4853-3293-9805-8f590b6b71cc | -10.8432 | -49.1018 | 2025-07-12 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3a6bf921-fa78-3736-8f58-de5e79119621 | -10.8432 | -49.1018 | 2025-07-12 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b4e9baa4-c6a5-367e-9439-1cb7b5f7c0cf | -10.8986 | -49.204 | 2025-07-12 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6994e98a-2aad-3c11-827f-0204a7ef698c | -11.7245 | -47.4543 | 2025-07-12 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7991b8e5-7476-33cd-928d-db3fe1fbc959 | -7.4733 | -47.5149 | 2025-07-12 00:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 165.9 |
| d04e097f-5fce-308c-8a56-b7b53607fecd | -10.8429 | -49.1236 | 2025-07-12 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| e01b1eca-bf81-3878-9930-aa416022dbbb | -11.7241 | -47.4766 | 2025-07-12 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 0bc00c45-ef82-3c90-b08e-2f1adf55371a | -10.8622 | -49.0997 | 2025-07-12 00:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e9bdf402-7f2a-3dae-b912-f7b2eccd4c83 | -8.4809 | -49.6177 | 2025-07-12 00:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 605d309d-d8bb-36ca-b0e4-c7e4fade5185 | -8.4622 | -49.6193 | 2025-07-12 00:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7cd90464-8853-3aa0-8671-cf65d26aa98b | -7.492 | -47.5134 | 2025-07-12 00:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 182cd9d2-c51e-324e-bfdf-e3ec089ff652 | -11.7245 | -47.4543 | 2025-07-12 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d3dc197d-dfd2-3114-a8cf-406d45db134e | -10.8619 | -49.1214 | 2025-07-12 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 7e0dd93e-12ae-325d-9cb9-bb6e8dd8682e | -3.75 | -47.1144 | 2025-07-12 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c90a5b4e-04e1-3e3c-bd13-5e129d3ce989 | -8.4622 | -49.6193 | 2025-07-12 01:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 0aba8657-be07-3f02-89cf-f374527d2baa | -10.8986 | -49.204 | 2025-07-12 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| dbde08b0-bc8c-36b9-8669-c66ed7523334 | -8.4809 | -49.6177 | 2025-07-12 01:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 97e48a7d-8f98-370e-87e2-9b4599b608d6 | -11.7433 | -47.4741 | 2025-07-12 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 84ba1ef5-a4db-3ded-9b3f-69d47a576549 | -7.492 | -47.5134 | 2025-07-12 01:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9b8ac263-a1dd-3178-82e6-0040bb8f508f | -10.8429 | -49.1236 | 2025-07-12 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 25afd8a4-f5f3-30c3-83cf-50061729cecb | -10.8432 | -49.1018 | 2025-07-12 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 569c8d5e-6b01-3e8a-b1dd-14dc903d22bd | -11.7436 | -47.4518 | 2025-07-12 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 9b875133-6f70-3f47-9fe7-31870150f99b | -10.8622 | -49.0997 | 2025-07-12 01:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 22f387db-be0e-3182-874c-c69bf50e686c | -7.4733 | -47.5149 | 2025-07-12 01:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 3b63a91f-05e1-35b3-9388-e16e16c92df6 | -11.7241 | -47.4766 | 2025-07-12 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b6a7f41c-2616-3c99-ab6b-f2507b07399f | -7.4731 | -47.5369 | 2025-07-12 01:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d5937e06-f0af-3438-86e7-daf267ab3b88 | -8.4622 | -49.6193 | 2025-07-12 01:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f59b7e10-4ac2-3990-89fb-fabfe55b3553 | -11.7241 | -47.4766 | 2025-07-12 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 77277784-2a0b-3acd-9f46-db527788c5c0 | -10.8432 | -49.1018 | 2025-07-12 01:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 30f62d41-b1e5-357c-8407-f885554a40c8 | -10.8986 | -49.204 | 2025-07-12 01:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b93c368f-dd36-326f-9ac7-d94e00934b2a | -10.8429 | -49.1236 | 2025-07-12 01:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5e548c60-3183-3e81-8c6d-028155ae53a4 | -11.7245 | -47.4543 | 2025-07-12 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 627a16e3-7c58-3ecb-859f-b95091183bad | -8.4809 | -49.6177 | 2025-07-12 01:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0d8bf6fa-586b-3328-a5be-94a68b245c41 | -10.8619 | -49.1214 | 2025-07-12 01:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d10b63f8-3ab0-39ff-a678-7d8a2b3b3587 | -7.4733 | -47.5149 | 2025-07-12 01:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| defb808d-da82-3d2e-84eb-eb5b32de6bef | -11.8802 | -58.709801 | 2025-07-12 01:12:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a40f17e-197b-3852-8ad7-66a362ffebbd | -14.3497 | -58.715 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9b5de5c-dca1-3915-935c-3144e97c9742 | -9.6615 | -62.909302 | 2025-07-12 01:12:00 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8863a7b8-4c64-3856-bd8e-c6fd4f7d64ad | -11.8684 | -58.703602 | 2025-07-12 01:12:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1be74f-cd9a-3de1-8af7-3ea088977c70 | -7.934 | -61.549 | 2025-07-12 01:12:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b262f61-6b59-3cce-bf25-cb3116bdf9dc | -9.025 | -61.224098 | 2025-07-12 01:12:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8317fc71-234c-3a08-9c20-0c787d305dd2 | -13.6469 | -53.931702 | 2025-07-12 01:12:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9576b988-4966-3051-9a28-3f583e4c168e | -14.3516 | -58.723099 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74721585-3fe3-3f21-89e7-02eba3e115c9 | -9.66 | -62.902302 | 2025-07-12 01:12:00 | METOP-B | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50d4eeaa-9d4a-3c83-bce6-537559822ea3 | -9.9727 | -64.942101 | 2025-07-12 01:12:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1b8f366-6faf-34b0-8a93-e5f97d55a232 | -9.971 | -64.934402 | 2025-07-12 01:12:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e7dc094-6466-3bfd-9893-c1f4bc985239 | -11.8822 | -58.7183 | 2025-07-12 01:12:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f00bf45c-b94d-3bfd-8be4-2154eab9b1bd | -14.4966 | -58.636101 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 859b1efb-cf97-3a01-922d-01f14427579d | -14.4947 | -58.627899 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1df23aa8-c849-32ab-a023-604cd622f37b | -14.4849 | -58.630299 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12d15bb0-8fcb-3498-9936-ea669d6cae4f | -10.2286 | -56.763302 | 2025-07-12 01:12:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ece89bd8-0194-3682-aeb4-1500aa8cfdf4 | -10.0522 | -59.102699 | 2025-07-12 01:12:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96d6782f-cba8-3d87-abfa-cc421082b73e | -11.1036 | -60.8433 | 2025-07-12 01:12:00 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 66130fe8-3314-38cc-87a8-80f5df34174d | -19.0928 | -56.039001 | 2025-07-12 01:12:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fbe6ae7d-7bca-3eec-94cd-150a959b47f5 | -13.6565 | -53.9291 | 2025-07-12 01:12:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 38c8f282-4b64-3099-981a-925634a79124 | -10.0542 | -59.111301 | 2025-07-12 01:12:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 575a07bf-824b-3d8c-aac5-9bb411888331 | -14.4928 | -58.619801 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6cdc0583-50c0-3d15-b4c3-879af26c53c9 | -14.4868 | -58.6385 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 16418e4c-4631-352c-b5eb-ef5861a7dac3 | -9.9744 | -64.949898 | 2025-07-12 01:12:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ff32a25-f644-34a8-b25f-e806c54fb6b8 | -9.0267 | -61.2314 | 2025-07-12 01:12:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebf9d41-7792-3d00-b6dc-eb9675b5ac1e | -14.3418 | -58.725498 | 2025-07-12 01:12:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71abb194-1a4a-3769-8d2e-c431fcf29b69 | -11.8862 | -58.735401 | 2025-07-12 01:12:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 553a32ef-9c01-3228-8745-45abf12c137c | -11.8782 | -58.701302 | 2025-07-12 01:12:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 27bb6ae9-e203-3364-b85e-0978e085d00e | -9.0234 | -61.2169 | 2025-07-12 01:12:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdbaa8e-98ac-320b-b207-5c0341f1f154 | -10.8432 | -49.1018 | 2025-07-12 01:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ffbfa972-c00c-3176-aa7a-3d5ac90c3973 | -11.7436 | -47.4518 | 2025-07-12 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| c90aceb4-ea08-362e-81cc-25083ffc5fe2 | -11.7245 | -47.4543 | 2025-07-12 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 424e78b3-ce4f-3983-905a-7e3e64495a5e | -7.4733 | -47.5149 | 2025-07-12 01:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 1dbd02f6-b2da-3325-bec8-baac362f0f82 | -11.7241 | -47.4766 | 2025-07-12 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 97fb8013-dc45-3fec-b4a2-d6798cd09ab2 | -10.8986 | -49.204 | 2025-07-12 01:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 295649a7-dfa5-3b54-abb6-4eaa0d334b44 | -11.7433 | -47.4741 | 2025-07-12 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| d0bca286-f3ce-388c-b9a5-434381795751 | -10.8622 | -49.0997 | 2025-07-12 01:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| b60456bf-3afd-313e-bff2-d44ab2a685d4 | -3.75 | -47.1144 | 2025-07-12 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e4f76420-9841-34c6-abcd-60fdb3c9b83a | -8.4809 | -49.6177 | 2025-07-12 01:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8a6f7d27-6e99-377c-8913-3cce96972f6c | -10.8432 | -49.1018 | 2025-07-12 01:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 286d82b6-a578-3b91-a841-8c325cd2316a | -5.8412 | -48.3964 | 2025-07-12 01:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| fb46d2d3-8e11-36d8-8315-956265a49b69 | -10.8622 | -49.0997 | 2025-07-12 01:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 4d861527-a1a1-3e80-b6db-cdcec16a99f7 | -11.7433 | -47.4741 | 2025-07-12 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8eb58603-1888-37d4-a668-8ce6500f6e9a | -11.7241 | -47.4766 | 2025-07-12 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 56bbb696-0f72-3d6a-9c70-673ce1282f05 | -8.4809 | -49.6177 | 2025-07-12 01:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7dff9a24-8627-3286-afce-6900e8642dd5 | -11.7245 | -47.4543 | 2025-07-12 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| e7032a84-eb90-3630-bd84-7f0c11f0f89b | -3.75 | -47.1144 | 2025-07-12 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 214b903a-6f02-3195-beb5-138b5b174983 | -11.7436 | -47.4518 | 2025-07-12 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 02ad3a42-5abb-34a2-9c6c-a2982b5907d2 | -10.8986 | -49.204 | 2025-07-12 01:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 243de02c-f579-3326-8705-c1d7c1cc365b | -10.8986 | -49.204 | 2025-07-12 01:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5d5d64fd-be23-34d9-ae5d-bfc23d33f20a | -10.8432 | -49.1018 | 2025-07-12 01:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| a11d951c-ba79-335e-a938-a5759036a200 | -11.7436 | -47.4518 | 2025-07-12 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| be82e4a9-6161-31f4-93ae-fc1891bde361 | -3.75 | -47.1144 | 2025-07-12 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 4683c8da-d6ad-36fd-ae09-d428fbb6826a | -8.4809 | -49.6177 | 2025-07-12 01:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 17b491c0-8bb8-37d7-b5c1-608525403690 | -11.7245 | -47.4543 | 2025-07-12 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e53356be-8c20-3838-a9b1-aaf7dbdbc7f9 | -11.7241 | -47.4766 | 2025-07-12 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 0f460a72-38f3-3895-a9d6-1ac2ab90c857 | -10.8986 | -49.204 | 2025-07-12 01:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b9fae4f4-c55d-3ef7-9f0e-2ac61b0a0352 | -11.7241 | -47.4766 | 2025-07-12 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 3c0c838e-99f0-3390-b71b-424413d63565 | -10.8432 | -49.1018 | 2025-07-12 01:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 57257ff9-9b98-3d91-bda0-0cf861c58ca4 | -8.4809 | -49.6177 | 2025-07-12 01:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d61981a4-37a5-3c93-b747-18164dd05958 | -11.7241 | -47.4766 | 2025-07-12 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0ab03647-1672-35ef-85b6-81f20f9adf48 | -10.8986 | -49.204 | 2025-07-12 02:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a479b0ca-8586-37d8-a2c5-aaab7740ce22 | -10.8432 | -49.1018 | 2025-07-12 02:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 305b72bf-7a1f-3510-99f6-58453a70f27d | -11.7245 | -47.4543 | 2025-07-12 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 37c536bc-09a7-3d77-bb4b-e80b65e527b9 | -9.96907 | -64.9647 | 2025-07-12 02:02:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |


[Clique aqui para ver as próximas entradas](README5.md)
