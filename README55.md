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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b915ce2-c4cb-3694-b743-d01ea3eb2436 | -8.97176 | -60.49308 | 2025-08-19 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| faefe504-14f8-38fd-8c52-59939745008d | -7.78099 | -66.95226 | 2025-08-19 06:59:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ee936816-9487-3d53-a22f-addaeb05bf9d | -9.17932 | -59.64458 | 2025-08-19 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 69c06fa5-86d0-3997-b422-9eec521b491e | -9.17636 | -59.63865 | 2025-08-19 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b99c8133-2d6e-3b26-b428-94a4e0bc6da3 | -7.79088 | -66.9538 | 2025-08-19 06:59:00 | AQUA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4ff7b701-c915-3169-ad38-b59821681d85 | -9.19207 | -59.63221 | 2025-08-19 06:59:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2d8e8135-83b8-37d2-8fd1-abddd5a0e549 | -6.9715 | -43.5833 | 2025-08-19 07:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| cdcc738c-9c00-343b-89b9-926909946555 | -6.9339 | -43.5868 | 2025-08-19 07:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 58811522-ec2d-3aa0-a69f-1c26674765dd | -6.9527 | -43.585 | 2025-08-19 07:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1185eba8-7dbc-3117-8953-b0e761cb867c | -6.1932 | -42.5259 | 2025-08-19 07:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 143.1 |
| 901d195e-c911-3135-bba6-895c079a85ff | -13.1555 | -54.9357 | 2025-08-19 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e7168754-4ef7-37f9-bf9f-ebbcfe476059 | -12.98324 | -56.84626 | 2025-08-19 07:01:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| fe5ae064-5d76-3ff3-966b-5a82dc464936 | -13.1548 | -54.93181 | 2025-08-19 07:01:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| cad8221e-2648-3ca8-a414-59298aebfca0 | -13.15106 | -54.92357 | 2025-08-19 07:01:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 12647bd3-25c4-38c1-acb2-2849fa12f978 | -6.9339 | -43.5868 | 2025-08-19 07:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d9b35711-17a8-36b3-9753-4ef2ad392573 | -6.1932 | -42.5259 | 2025-08-19 07:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 54b28f2f-cb35-3c26-8768-167203f72d14 | -6.9715 | -43.5833 | 2025-08-19 07:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d7c44f03-3258-3009-91c5-be93af8921b1 | -13.1555 | -54.9357 | 2025-08-19 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 60901b10-6a53-3a74-b3d1-2f1b035e577d | -6.9527 | -43.585 | 2025-08-19 07:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4b5ae85e-2d2d-3a99-a477-917d6f190919 | -6.212 | -42.5243 | 2025-08-19 07:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| ffbf39a5-3558-38e3-8973-469ea6897e61 | -6.212 | -42.5243 | 2025-08-19 07:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| b91276b9-d893-3e15-bc0b-c8f50401ab1a | -13.3537 | -54.4213 | 2025-08-19 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 664b7272-3477-33e1-ab71-44b771ac9c4f | -6.9339 | -43.5868 | 2025-08-19 07:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b78ad1e6-f45b-34e4-859a-aa776798b3a2 | -6.9527 | -43.585 | 2025-08-19 07:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 08f4f202-4bc0-3fd8-a206-3d82b5217c60 | -13.1555 | -54.9357 | 2025-08-19 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| bce61531-d039-3179-82c4-f7e54650d1a8 | -6.9715 | -43.5833 | 2025-08-19 07:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 372c29ec-ba67-31cf-93c1-e0f6b9e2e56a | -13.3346 | -54.4233 | 2025-08-19 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| ae4decd5-eee8-33c3-84c5-261b094e0c9c | -6.1932 | -42.5259 | 2025-08-19 07:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 71ff5e5d-0c2f-302b-a828-ca4fe9643c1c | -6.9339 | -43.5868 | 2025-08-19 07:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 173b657d-66df-35f0-b225-beca482a650d | -6.9715 | -43.5833 | 2025-08-19 07:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b820caf7-1d91-309f-8c17-a7c1813f99b0 | -13.1555 | -54.9357 | 2025-08-19 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fc505238-f650-3449-bf15-0ba79ba18dd4 | -6.1935 | -42.5022 | 2025-08-19 07:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 5486c262-d2b7-3456-8931-e849e32bf60f | -6.1932 | -42.5259 | 2025-08-19 07:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 87a561c9-81fe-3906-b6d4-2ba7a137c0b6 | -13.1555 | -54.9357 | 2025-08-19 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 62f66b51-6d02-3458-945d-88338fa7ab9b | -6.1935 | -42.5022 | 2025-08-19 07:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| ddcc6eb4-ef39-3741-b1cd-e48ebd3fbed9 | -6.9339 | -43.5868 | 2025-08-19 07:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| a1d7dce6-7db2-3b74-b044-32789899c32c | -6.9715 | -43.5833 | 2025-08-19 07:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d56a54ff-92fe-3ab7-8456-a546fac6b8be | -6.1932 | -42.5259 | 2025-08-19 07:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| f547b81a-f268-3597-acc4-631b6d4e9777 | -6.9339 | -43.5868 | 2025-08-19 07:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fbc1a69f-e7d3-3a5e-8f03-ce06bea037a9 | -13.1555 | -54.9357 | 2025-08-19 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4f393118-c869-3d01-bc0e-94ae3d61e003 | -6.9715 | -43.5833 | 2025-08-19 07:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4d82d722-3369-3e2b-8ccd-66c2a9a91f1a | -6.1932 | -42.5259 | 2025-08-19 07:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| b579be8f-71a6-3e25-ab36-696f84cd542f | -6.1935 | -42.5022 | 2025-08-19 07:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 567cb89a-e36b-343e-b2a2-aa9fed9d8eb1 | -6.9339 | -43.5868 | 2025-08-19 08:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b8233e8e-1638-35a8-aeda-2b25d578bab7 | -13.1555 | -54.9357 | 2025-08-19 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| bc6d7e15-bc89-393f-82c9-8d50f3951b24 | -6.9715 | -43.5833 | 2025-08-19 08:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d185cdd1-a79a-3426-b3c9-6f56b8a1c45d | -6.1932 | -42.5259 | 2025-08-19 08:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 123.3 |
| b3fe0e14-ee15-3674-9384-7989169ee911 | -18.3852 | -51.9718 | 2025-08-19 08:00:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 37ee342c-0777-3bde-aba6-16b85e471580 | -6.1935 | -42.5022 | 2025-08-19 08:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 202a863e-428d-300c-8584-a652f91f3181 | -6.9715 | -43.5833 | 2025-08-19 08:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1046a3fd-ae54-31d0-a0ab-903e02ffc685 | -13.1555 | -54.9357 | 2025-08-19 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| bcd11db3-ddd4-3981-ba97-6947b251d48f | -6.1932 | -42.5259 | 2025-08-19 08:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 4c6b7428-cc62-3e21-9bcf-6112ece0a250 | -6.9339 | -43.5868 | 2025-08-19 08:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6acb53fd-cec9-3b66-9ed0-208d5793f304 | -13.1555 | -54.9357 | 2025-08-19 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| a39b47c8-f03b-3138-82c0-dbdf378a1c97 | -6.9715 | -43.5833 | 2025-08-19 08:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b329f632-4bf6-3c92-86e9-03882aad5596 | -6.9339 | -43.5868 | 2025-08-19 08:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b16798b7-728f-3f8e-8285-cd03ea413ea9 | -13.1555 | -54.9357 | 2025-08-19 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 363e772f-c531-32d7-9bfb-ff3a0ae79e30 | -13.1555 | -54.9357 | 2025-08-19 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1b495b7e-32dd-32a9-8502-eb9ca9b3aa10 | -13.1555 | -54.9357 | 2025-08-19 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| efcf4601-2cc4-3836-8943-a89cc0ac9447 | -13.1555 | -54.9357 | 2025-08-19 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 383acef3-0ead-3dfd-8035-8d147cc0a3cb | -13.3537 | -54.4213 | 2025-08-19 09:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b77e3beb-724b-3b01-9fdf-6bfc4377bee7 | -13.3346 | -54.4233 | 2025-08-19 09:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9aec3471-2bbd-3969-a4c2-65366132bf9c | -13.3349 | -54.4027 | 2025-08-19 09:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 26c96d79-c43b-34a7-b0af-e491c0bdaf4f | -13.1555 | -54.9357 | 2025-08-19 09:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| e095fc44-9681-3c1f-90bb-22fdc000b6ab | -11.586 | -46.5988 | 2025-08-19 10:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| bb83ff18-b919-383c-9939-ef7156f41623 | -11.586 | -46.5988 | 2025-08-19 10:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 44284a0f-03fe-3010-8bed-a929475bd3bb | -6.9339 | -43.5868 | 2025-08-19 10:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 2696908a-f108-3d61-9b00-25492264b69e | -11.5856 | -46.6214 | 2025-08-19 10:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 7f70838c-96b5-37be-a8a8-3ff1035ec88c | -11.5856 | -46.6214 | 2025-08-19 10:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 80f2386a-2b70-3087-923c-2761865623f5 | -11.586 | -46.5988 | 2025-08-19 10:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 220.4 |
| c05cade7-8922-363b-b783-ec5febbbf194 | -6.5201 | -45.5013 | 2025-08-19 10:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 3857e54f-0b70-3ee0-ae2a-e3b195fd502f | -6.9339 | -43.5868 | 2025-08-19 10:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| c2ba679a-10f4-3f98-af66-8befb82822d1 | -11.6048 | -46.6188 | 2025-08-19 10:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 363.0 |
| 1ebd2efa-3cb6-3473-a756-c146d1880834 | -11.6051 | -46.5962 | 2025-08-19 10:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 316.5 |
| 6bf3b5ed-466d-3f41-ba10-0dc6d8cb86d6 | -11.586 | -46.5988 | 2025-08-19 10:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 308.0 |
| ca9bc318-c504-3818-b150-4995883b5275 | -11.6051 | -46.5962 | 2025-08-19 10:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 2f691a35-0473-33f0-bf42-95ac8cb0e6a8 | -11.6048 | -46.6188 | 2025-08-19 10:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 224.3 |
| d6c6ebe5-6675-3f61-9d8b-2991b4be0700 | -6.9339 | -43.5868 | 2025-08-19 10:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 67b9e8a1-5a29-3234-881c-8929c7b4cb61 | -11.5856 | -46.6214 | 2025-08-19 10:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 280.4 |
| bfd9a06b-62d2-3cd3-af3e-d4c0ee575c86 | -6.5201 | -45.5013 | 2025-08-19 10:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b428047c-b96e-36a3-8398-b9269b2c8301 | -11.6051 | -46.5962 | 2025-08-19 10:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 329.3 |
| 73320f41-b39c-385d-ad88-87a4b2eca69e | -11.6048 | -46.6188 | 2025-08-19 10:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 2b2f1660-21eb-390f-98cb-0a5a96c4a769 | -11.586 | -46.5988 | 2025-08-19 10:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 98883b8c-3d95-3781-b386-1788c89e31e2 | -6.9339 | -43.5868 | 2025-08-19 10:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 27da0f4a-f549-3e65-93aa-9a4bf9351d4a | -13.8752 | -45.5179 | 2025-08-19 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 67ac6534-07a6-32a4-b73d-d0deba2d6504 | -12.993 | -45.1787 | 2025-08-19 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 41274f51-4b6f-3b39-a507-f706f489d6a6 | -11.5856 | -46.6214 | 2025-08-19 10:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 021f5a85-828c-3194-94b7-4d97358a3b3b | -12.993 | -45.1787 | 2025-08-19 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| f8c71e7d-99f1-3ee0-95e3-53377aec50a1 | -11.6048 | -46.6188 | 2025-08-19 10:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| a9b93c5a-d6ac-3e2e-9c33-1c49255661a0 | -11.586 | -46.5988 | 2025-08-19 10:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b047d2f9-3a96-3482-a251-6821489a6538 | -11.5856 | -46.6214 | 2025-08-19 10:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 3b15746c-3cd8-3c19-b829-9dbf58cebddd | -6.5201 | -45.5013 | 2025-08-19 10:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| bd5fd709-d7ac-3b03-8ae1-290422cebb33 | -13.8752 | -45.5179 | 2025-08-19 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 4cdc5c0a-c13f-3d74-9681-1fea34e0d307 | -6.9339 | -43.5868 | 2025-08-19 10:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 71e546bb-0c42-3f1c-9fa3-5ecd7d5e5cb8 | -13.0123 | -45.1756 | 2025-08-19 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| b8b36efa-efba-3e91-a99f-6f6476532b86 | -11.6048 | -46.6188 | 2025-08-19 11:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 306e3922-c7c5-33ae-b590-5fac3c4a356b | -6.9339 | -43.5868 | 2025-08-19 11:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| dd4f0a3b-4506-392d-8198-1085b0b67f24 | -12.993 | -45.1787 | 2025-08-19 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 7c5ffd3a-1f1c-35f7-9375-2f9ad95d836d | -12.993 | -45.1787 | 2025-08-19 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 8c2cfc34-ed21-357e-bf32-93360597aaf8 | -13.8752 | -45.5179 | 2025-08-19 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |


[Clique aqui para ver as próximas entradas](README56.md)
