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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7eb918b-39bf-31cb-aad0-10b51ee44566 | -12.9226 | -51.1413 | 2024-10-10 01:04:41 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c01482ad-b526-3d8e-8ad5-b2115741f92f | -11.7782 | -47.363098 | 2024-10-10 01:04:45 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 480eed79-d83e-326b-8f03-b742b4ad8029 | -11.7822 | -47.378899 | 2024-10-10 01:04:45 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5afe04-4243-37b2-92a8-0e7789155a1a | -13.2873 | -53.737499 | 2024-10-10 01:04:45 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce359bff-2115-304e-b694-93b3b9cc5042 | -13.2759 | -53.7327 | 2024-10-10 01:04:45 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf4b854e-1a39-3d7f-9b4b-523724f524d9 | -13.4346 | -54.669899 | 2024-10-10 01:04:46 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5bb76d2-9a1d-38cb-b3d4-cbc7ccd3d22d | -13.4362 | -54.676899 | 2024-10-10 01:04:46 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 997bc8d4-d92b-3589-a5ed-01a214d67d6e | -13.4233 | -54.6651 | 2024-10-10 01:04:46 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 354d9348-2586-3c99-bc31-916982b06f3d | -13.4248 | -54.6721 | 2024-10-10 01:04:46 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a0f31de-5a70-38c4-89db-e09076f86ac5 | -13.4264 | -54.6791 | 2024-10-10 01:04:46 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a80abc1-5629-36fa-a9fb-fea06fec89a7 | -13.428 | -54.6861 | 2024-10-10 01:04:46 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a851932-6f2e-3075-b54a-1191eb0513ca | -13.4151 | -54.6744 | 2024-10-10 01:04:46 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6479f62d-e74a-3f4a-891c-6400c9c5f1e7 | -12.1562 | -49.674099 | 2024-10-10 01:04:48 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87a64263-3679-3d5d-954c-e3e324efb618 | -12.8469 | -52.803299 | 2024-10-10 01:04:49 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f33fec51-e4be-39cf-b428-e0b3aa12c94a | -12.8486 | -52.810902 | 2024-10-10 01:04:49 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6ef3be7-b00d-30af-bdb9-8c6e3af834ad | -12.8504 | -52.818501 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf3973c-632d-3beb-a71f-df8e51b562c6 | -12.982 | -53.482899 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be249498-ec51-39ca-82cf-3a9e458249ba | -12.9836 | -53.490101 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e35bf07-e236-329d-a5ca-845170445a5d | -12.9722 | -53.485199 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a74e4eb-1194-3a8c-b44e-b36c5640fe44 | -12.9739 | -53.492401 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f41af74-0f2d-3161-94d1-7080c76e1daa | -13.01 | -53.651501 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bffb613-318b-31eb-87b6-5a895bc7890e | -12.9986 | -53.646599 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abb3a42d-1d38-33a6-abd5-120d757f349d | -13.0003 | -53.653801 | 2024-10-10 01:04:49 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac496dba-4754-3292-98c5-c2b4f57ec23f | -12.8857 | -53.4673 | 2024-10-10 01:04:50 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c136c937-69dd-354f-bfb4-b6bda3b58ea4 | -12.8725 | -53.455101 | 2024-10-10 01:04:51 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bedf290-d6c1-32eb-9b64-6a922a7dcba6 | -12.8742 | -53.462399 | 2024-10-10 01:04:51 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcaa2ec-b3c7-3f1c-be86-b3622a7d1aac | -12.8759 | -53.469601 | 2024-10-10 01:04:51 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd70b2f-17f3-3147-9a5e-bb7f5983deeb | -12.1821 | -50.592999 | 2024-10-10 01:04:51 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2141de17-5734-30e7-a48e-a46e569988d1 | -11.5777 | -48.415798 | 2024-10-10 01:04:52 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53172fd1-3ca3-3fc2-82d9-67e2461d48b0 | -10.5792 | -44.752701 | 2024-10-10 01:04:53 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1440d2d-acfc-3d4b-adce-8542ef84842c | -10.5888 | -44.750099 | 2024-10-10 01:04:53 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df748ade-a922-33ab-94ba-901fdf39c938 | -12.6364 | -53.099499 | 2024-10-10 01:04:53 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a14b36e-1cf1-347c-8245-4cf87a9610cc | -12.606 | -53.0121 | 2024-10-10 01:04:53 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9652f8-d008-3c5f-9911-0505a61f3101 | -12.6077 | -53.0196 | 2024-10-10 01:04:53 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f61d5c2b-19b6-39a4-af84-1dff645ab678 | -12.6202 | -53.119099 | 2024-10-10 01:04:53 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bb818d4-e4c0-337f-93a1-fe6d5bf1879e | -12.6219 | -53.126598 | 2024-10-10 01:04:53 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e68df83-f401-3435-a756-fcfdff737f3b | -12.6236 | -53.133999 | 2024-10-10 01:04:53 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9557af5-8921-3a32-bccd-d260c3ac778b | -12.6105 | -53.121399 | 2024-10-10 01:04:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03b55b8b-b99a-3b08-b901-5d23c51ab11b | -12.6122 | -53.128899 | 2024-10-10 01:04:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36eb6dbe-6d89-376c-a359-356bd08b34c2 | -12.572 | -53.0439 | 2024-10-10 01:04:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77ca5311-2cfc-3f8c-aefb-2b0718b2376c | -12.5738 | -53.051399 | 2024-10-10 01:04:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68e3ca68-34f2-33d4-bcfb-9cb93a280fc2 | -12.5755 | -53.0588 | 2024-10-10 01:04:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 945e496b-6e93-3980-9118-aee99a389a4a | -12.5772 | -53.066299 | 2024-10-10 01:04:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c33ce0a6-a456-320c-b69e-0e69410d9690 | -12.564 | -53.053699 | 2024-10-10 01:04:54 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2eb5a9ab-e198-3da8-914a-14525a50ae59 | -13.345 | -56.660599 | 2024-10-10 01:04:54 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4fbee390-d04a-3609-b1f2-a7e4c4508b09 | -12.4815 | -53.144199 | 2024-10-10 01:04:56 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57f71202-24f5-3e8d-9cf3-6d6bed1e86dd | -12.7008 | -54.107201 | 2024-10-10 01:04:56 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3639fc6-a163-305a-82cc-32170ca627fe | -12.4701 | -53.139 | 2024-10-10 01:04:56 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31d28c36-12c5-32ca-a8c7-17e2efab5d9f | -12.6894 | -54.102402 | 2024-10-10 01:04:56 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d9ec587-7704-3237-9da7-89d43b727074 | -12.691 | -54.109501 | 2024-10-10 01:04:56 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b758fc17-c811-3578-a110-71b25e7e02b5 | -11.549 | -49.896702 | 2024-10-10 01:04:58 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb693505-8fdb-336c-8f9c-aa124a53a90b | -12.6672 | -54.6922 | 2024-10-10 01:04:58 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8c8f9be-0e5e-3248-b60d-50f2d29f02ca | -12.6688 | -54.6991 | 2024-10-10 01:04:58 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abe41cfd-c409-369a-8072-9955b711954e | -12.6703 | -54.7061 | 2024-10-10 01:04:58 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0653eaa-82ff-343c-be8a-ed6961d2802f | -12.6719 | -54.7131 | 2024-10-10 01:04:58 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f80056a-4172-397d-b59c-71b3542cc43a | -12.659 | -54.701401 | 2024-10-10 01:04:59 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11c4f6e8-48d3-38cf-8bc8-1fa0590def6b | -12.6605 | -54.708401 | 2024-10-10 01:04:59 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5abbadb-7cd6-312b-87ed-0706462a1320 | -11.9883 | -51.909302 | 2024-10-10 01:04:59 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db074e2d-ac21-3c18-82f0-9a12c36d3faa | -11.9785 | -51.911701 | 2024-10-10 01:04:59 | METOP-B | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc5b4658-8ea1-340f-8950-4fe39cad48a6 | -13.7536 | -60.570599 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38a2c729-e6a8-3112-917f-2349d84d89e3 | -13.0593 | -57.244202 | 2024-10-10 01:05:01 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 730a84c7-adce-34b5-9485-33cee9d2b980 | -13.061 | -57.252102 | 2024-10-10 01:05:01 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ea977ba-6182-3ca0-af84-aa60e220a8b3 | -13.7438 | -60.572601 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a7d2e2f-29e5-326e-9c57-717c333b12cd | -13.7462 | -60.584702 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb785b7-a00d-30e7-a57a-812673b70889 | -13.734 | -60.5746 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69593a9a-3226-3b80-be10-44e0de9d15a8 | -13.7364 | -60.5867 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a67b2e06-b319-39a6-8a13-07b6b72f6587 | -13.7388 | -60.598701 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bfaacb8-d5eb-3dab-94f3-67816be79412 | -13.7266 | -60.588699 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88a948dd-a976-36df-9415-ec69d8e8fada | -13.729 | -60.6007 | 2024-10-10 01:05:01 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78f6980b-910d-38ac-a566-5eb9443dce07 | -12.5868 | -55.2104 | 2024-10-10 01:05:02 | METOP-B | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a961c052-3ee5-35ec-b415-7b9ac599f6a3 | -12.4208 | -54.557499 | 2024-10-10 01:05:02 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64259684-3e84-3126-8133-e9dcb0fdcff8 | -12.4223 | -54.564499 | 2024-10-10 01:05:02 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78ce7df2-82b7-3ed4-8886-30a3f91cd2bd | -12.4094 | -54.552799 | 2024-10-10 01:05:02 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0475e29e-973e-399e-8aed-8cbda41cdc7f | -12.411 | -54.559799 | 2024-10-10 01:05:02 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00c6f631-9c3b-304f-b1cb-6117ed0fda95 | -12.4125 | -54.566799 | 2024-10-10 01:05:02 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8cf366-587c-32e8-9304-e9e203b28286 | -12.4011 | -54.562 | 2024-10-10 01:05:02 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37de7a72-59ae-366b-8c29-ea6e2f9a1d91 | -12.4027 | -54.569 | 2024-10-10 01:05:02 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d6be268-69d1-310b-9388-a00ee2f2e9b2 | -11.2019 | -49.9133 | 2024-10-10 01:05:04 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 224ab410-bfa2-3910-8910-d112853f3dee | -11.1922 | -49.915798 | 2024-10-10 01:05:04 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65fb623e-289f-3621-81c0-e76975927835 | -10.5869 | -47.6726 | 2024-10-10 01:05:05 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 351e90b0-9124-3543-b909-750cfa72d63b | -10.5909 | -47.6884 | 2024-10-10 01:05:05 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d950032a-7f97-3939-941c-474f0650367d | -10.5634 | -47.990799 | 2024-10-10 01:05:07 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70b4db9e-b133-3cc4-8b62-dc7a64e87c11 | -10.5672 | -48.005901 | 2024-10-10 01:05:07 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c969b3a0-ae78-351b-8987-d6ebd4d83df4 | -10.5709 | -48.020901 | 2024-10-10 01:05:07 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de26b30f-cd93-3ccd-b99a-085b68146d41 | -10.5537 | -47.993198 | 2024-10-10 01:05:07 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0441ae7c-0b9e-3b93-97a5-86350b251e70 | -10.5575 | -48.008301 | 2024-10-10 01:05:07 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f3ba641-91f6-392d-b428-771440d64221 | -10.5612 | -48.0233 | 2024-10-10 01:05:07 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94f48a80-05d7-373b-af2e-c61683acbc29 | -11.2864 | -51.037498 | 2024-10-10 01:05:07 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bdf5b695-c06f-3522-b99b-0498e9d39dbf | -11.2886 | -51.046902 | 2024-10-10 01:05:07 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43bfceb0-142c-3a99-a9c4-f27f9faa5e11 | -11.4775 | -51.845001 | 2024-10-10 01:05:07 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 081e2399-82bf-3f3f-981b-a07e94cd91f3 | -11.4795 | -51.8535 | 2024-10-10 01:05:07 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a86ad7b-99ec-3ed1-b2a2-2cf67b72462f | -10.6686 | -48.7052 | 2024-10-10 01:05:08 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf2920b9-41ab-341c-8fce-9b06df7d3f7a | -10.8468 | -49.7272 | 2024-10-10 01:05:09 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87d31a99-7c07-320f-a09d-0b8411b80294 | -10.8496 | -49.738701 | 2024-10-10 01:05:09 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59341cfa-878f-33e4-b769-42f283f00a67 | -10.8524 | -49.750099 | 2024-10-10 01:05:09 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7454f5cd-ba54-395c-9974-df71d3d0cd72 | -11.2017 | -51.333401 | 2024-10-10 01:05:10 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4f03c78-4a13-30c1-becb-48f57e2acda0 | -10.7305 | -49.546101 | 2024-10-10 01:05:10 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3c57f3e-5a97-377b-abf1-b0a13c6d16bb | -10.7334 | -49.557899 | 2024-10-10 01:05:10 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3676511e-0899-320b-beaf-f69df31d21ca | -2.67 | -53.35 | 2024-10-10 01:05:12 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75741b36-4f31-3e58-be27-64047312d012 | -10.516 | -49.0914 | 2024-10-10 01:05:12 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
