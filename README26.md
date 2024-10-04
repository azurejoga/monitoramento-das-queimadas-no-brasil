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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48af50df-ce9b-3432-9038-6fc88504a435 | -9.32455 | -51.13588 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1840598b-8313-352b-aba9-1ee1f1f7097e | -9.32376 | -50.80819 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8054381c-dbc1-3e34-a3c8-950b69b79e16 | -9.3233 | -51.12698 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6c43db9b-e06a-3326-aa0b-8151013718e4 | -9.3225 | -50.79924 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 999a1b10-4af5-39b8-94b6-83cb0f748cb0 | -9.32125 | -50.79027 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 28a0cb8b-02f9-33df-b4c3-7542287fc944 | -9.31616 | -50.81842 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 5e0c5024-c42b-3b77-abf5-ec7d1d83b273 | -9.31491 | -50.80951 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 244.5 |
| a4284507-a878-3e10-9daf-bf61ae4651a8 | -9.31365 | -50.80056 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4cae56b8-d8bb-3eb3-8cd0-fa52b7648064 | -9.31239 | -50.79157 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 5b158cbc-2531-38d4-a967-6ee38c5cdb9f | -9.31198 | -51.11045 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5e3ba6b0-e134-323c-898f-4de6e5ae68f0 | -9.3073 | -50.81972 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3da2ef42-fad2-3e3c-bc6f-f4c1b1b56240 | -9.30605 | -50.81078 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 973c884e-e82d-3479-b46e-87d8a0a32942 | -9.30479 | -50.80183 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 4032c91c-1378-38ce-a6eb-666993f2ea4e | -9.29815 | -51.0761 | 2024-10-04 01:09:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9b42758a-33f8-3642-babe-1e7d18ffe271 | -9.2969 | -51.06719 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a8d1179d-a1d8-369b-bd8d-5ad7afd9f17a | -9.8055 | -51.81754 | 2024-10-04 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f07a692-655b-3943-a6e9-083f40079bb6 | -9.77298 | -51.92031 | 2024-10-04 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c99ecde0-49e6-3556-8b4c-c914d0fd6047 | -9.73692 | -50.66204 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a5b536cc-1b6f-3e30-82bb-445913b26ae3 | -9.72932 | -50.6723 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 563325b1-e3b5-3abc-b17a-25a17a0a0081 | -9.72805 | -50.66334 | 2024-10-04 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9438a6d9-4094-3059-99e0-352518e52091 | -9.68947 | -51.38264 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c2f92c7-2ada-344a-8486-f96ebc4ecddc | -9.59979 | -51.46561 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ce23604f-5e58-3a66-a5d1-17cef4b0273e | -9.59855 | -51.45665 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f8188384-0101-3b06-acc2-24e1018517ac | -10.54555 | -50.97879 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3dad8171-b659-37e9-96e7-fba951c59a3d | -10.49242 | -51.12967 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ed1bde09-dd19-3e23-a602-8b4069649c6e | -10.49117 | -51.12073 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0d7bafb9-81aa-35b5-b3be-6a9900bd1c2c | -10.44989 | -50.74641 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 09788808-9413-368b-832c-d5bdd3533ebc | -10.44863 | -50.73745 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 344c46d2-13ee-3bbe-a653-e56f204a3804 | -10.44737 | -50.72849 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 87259b57-6da8-33f0-884f-2de5d8e2e1eb | -10.44378 | -50.781 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f6ca5a4e-7108-3da5-a0ee-56c0480a72ba | -11.22283 | -51.21278 | 2024-10-04 01:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 400ddd65-bfe4-3eb2-aeeb-6551f19f89bb | -13.1463 | -51.20362 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d3cef569-cea3-3990-9494-6c8230ebac0c | -12.73442 | -51.9699 | 2024-10-04 01:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f61fdef3-7fbb-3654-9790-17f54918bae1 | -9.02629 | -52.11222 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 757e8a5b-6723-3ebe-92b9-fd86abd3e4b6 | -9.84159 | -52.08101 | 2024-10-04 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a6c4b4f8-00af-3801-854e-9d834104a202 | -9.84034 | -52.07187 | 2024-10-04 01:09:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 50df1066-a5c5-3f61-813a-a19a964598a6 | -9.75937 | -53.16466 | 2024-10-04 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d850a958-eb43-3c73-9048-449cbbd4f291 | -9.68622 | -53.18494 | 2024-10-04 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1e656b83-41ff-3dac-8e89-aee77bea0e88 | -9.68491 | -53.17502 | 2024-10-04 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b7b1f864-c6f7-35f3-9f0d-5d77133db0aa | -10.91887 | -52.4222 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6a70b74b-367e-3153-abd3-c8e552e29f93 | -10.91759 | -52.4127 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| da65ce6e-2654-3ca6-90cd-1db6ec007bdb | -10.9163 | -52.40319 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c0a1919a-c9c8-35da-bb7f-4aefec1efae8 | -10.91105 | -52.43303 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 9c54c293-24e0-318c-97fa-3082ee6e2c80 | -10.90719 | -52.40444 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| aec436b1-8cd1-3fb9-82d7-3b71ac8f3c8c | -10.90193 | -52.43435 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4539d0cc-2bfc-304a-9084-e5661f088809 | -10.89808 | -52.40571 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 806df2bd-b0cb-3160-b271-f3963225ce08 | -10.88898 | -52.40699 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c9ff6fc-9d78-392b-b737-4cd6e2994d54 | -10.64063 | -53.70692 | 2024-10-04 01:09:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3c1e3c43-4a12-3979-8354-9725d545f53e | -10.2446 | -52.74156 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8c2acb15-6f93-30de-9b58-34229349215b | -10.23542 | -52.74282 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3056b8f7-05ba-39fe-961e-6b3169d3f82b | -10.06668 | -53.35447 | 2024-10-04 01:09:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1a435cf-15a7-3198-bd89-db0f73b89d0e | -11.72462 | -52.94354 | 2024-10-04 01:09:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 238e94fa-aeb1-38f8-9c94-54a024acc1fc | -11.08067 | -52.53403 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e0ca612b-8e51-3ab1-bb1b-69dbf52ac5e1 | -11.0715 | -52.53534 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ff15d2cd-cbe7-3df8-817f-950580e032f2 | -11.07021 | -52.52563 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fffd828a-72c4-3fd7-a878-a3393d55ab31 | -16.58216 | -57.27454 | 2024-10-04 01:09:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 96089b41-5e7d-3edd-877f-904fdf4b6503 | -11.05004 | -52.50527 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ed1a07ee-eb12-37ce-9774-0b4240ee1674 | -11.04089 | -52.50658 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5d59f650-cd78-3b46-9aad-2f4390d9616b | -11.03958 | -52.49695 | 2024-10-04 01:09:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 858c4a44-d44a-3b10-ba50-818a0c18cd6e | -12.6657 | -54.05859 | 2024-10-04 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| cb161246-4282-37b7-a0af-b59f01de3248 | -12.6142 | -53.49582 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7488eb2d-4977-32e6-b754-d381610e35b3 | -12.61282 | -53.15465 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ca51823c-195a-3bf9-8a8b-4c6502f1d884 | -12.60846 | -53.15058 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e5a83e2a-b08e-34ec-8820-3172c230d974 | -12.59603 | -53.13059 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 669233a1-f4bf-37b4-8429-5753b01f7a2e | -12.59462 | -53.11991 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 241.7 |
| c2d9cf07-74eb-3bc5-9182-eb6db1544a85 | -12.58644 | -53.13191 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| a1692f03-4d0b-3e11-b932-fcc93ca04d97 | -12.58503 | -53.12125 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7517129d-29a9-3919-b400-ad72a06270e6 | -12.57684 | -53.13322 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d3e342d2-a50e-3cf3-adaf-7ad0050d0333 | -12.57544 | -53.12257 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 45fc3003-1840-3f81-828b-07082726e543 | -12.57404 | -53.11186 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f712f2bc-b436-3317-b1ad-ed2e47891765 | -12.51474 | -53.1368 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 83b5e812-3c4a-3bae-a577-b377aead2ba2 | -12.48597 | -53.14077 | 2024-10-04 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 71dc0981-f72d-3752-87c2-bd874aeef928 | -12.3237 | -54.09198 | 2024-10-04 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 38fe4fed-37f4-3434-bb16-ee3c0bf1c2af | -11.58987 | -54.48114 | 2024-10-04 01:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7afb4dee-ff11-3574-8000-1f8ce9d17a7f | -11.5878 | -54.48833 | 2024-10-04 01:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2e8021ce-824d-33ee-bc67-665c34fbb70e | -17.15466 | -56.16726 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 9e873938-2f34-301d-b83f-127297de1023 | -17.06688 | -56.07972 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| d0109a7a-726a-3c54-8e0c-9fdafa866322 | -17.06683 | -56.07436 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| ed82b470-74e7-3220-aa85-dd27a912341d | -17.05411 | -56.08121 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| a266405b-9e1d-38a4-856d-453def004216 | -17.04379 | -56.69329 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| c2347b3a-2400-3622-ad0b-1a22ef5a6db0 | -16.95194 | -56.59111 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 8d93dae7-7546-3245-9b31-8854ed79497a | -16.94238 | -56.59767 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 2c68d435-cdbf-3d2b-9777-e2a3a634db03 | -16.93867 | -56.59264 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 4eea76cb-4c31-321c-9e8d-41eeb94f281c | -16.92375 | -55.84326 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 2aabf7a9-dcba-3bf3-a572-7510410734f1 | -16.9216 | -55.82398 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.8 |
| b40f04e3-712d-3e73-b23c-0801d57cc2b2 | -16.67063 | -55.91052 | 2024-10-04 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 6dfcb4ae-0a7c-36e3-85e4-45548fdcaaa5 | -11.89226 | -56.94909 | 2024-10-04 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 8e5e15de-2c15-3230-8d99-c307c14a1075 | -11.89192 | -56.21024 | 2024-10-04 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3a28d2f1-fac2-3eea-a55a-625e03e54f66 | -11.88621 | -56.20459 | 2024-10-04 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3cb6d525-7bba-39da-a0b5-729a43f5de03 | -11.82603 | -56.61493 | 2024-10-04 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 9f826640-8f65-3dda-a962-782212879afe | -11.82382 | -56.59683 | 2024-10-04 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 3429c8ac-bb81-3852-b794-366ec6aa7ff5 | -11.81377 | -56.6165 | 2024-10-04 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| b295a88b-2d79-332f-979b-7575851de2fd | -11.81158 | -56.59838 | 2024-10-04 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9cf81ab7-687e-33a1-aa70-d89a870ce21c | -12.60941 | -56.50182 | 2024-10-04 01:09:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 7637e932-c450-31c3-a28c-6726811cc0d6 | -12.60723 | -56.48345 | 2024-10-04 01:09:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 5e4146a5-7b80-3fd8-8cbe-29a9d3f3f935 | -16.61618 | -57.1966 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| e8443252-6b41-39a9-8f23-e60732cb11c4 | -16.61361 | -57.17241 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| bad98461-9e6b-39a8-a09d-8e2678ed25eb | -16.60233 | -57.19817 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 68a0f75c-92ef-3842-a6c0-2bb5abfa0ae1 | -16.59979 | -57.17398 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| b1cacb49-5f71-3c7e-871c-d4d6b336e961 | -16.58789 | -57.25577 | 2024-10-04 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |


[Clique aqui para ver as próximas entradas](README27.md)
