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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31a1bd55-f4d8-30fc-9188-3ffc1083c665 | -5.2464 | -48.0387 | 2024-10-12 00:24:46 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf8ef44-7dd1-3ce0-9a79-819e5a5bd4b7 | -4.7226 | -45.8843 | 2024-10-12 00:24:47 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 537eb4ba-2568-3208-a7f3-34b0cc2f21eb | -4.7242 | -45.891201 | 2024-10-12 00:24:47 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32c30523-9d66-3daf-87ac-4c5f962adad1 | -5.2024 | -48.164501 | 2024-10-12 00:24:47 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 56397530-060b-3e81-a0d3-81d4993c2b9e | -5.204 | -48.172001 | 2024-10-12 00:24:47 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9f050a90-2e56-3e9d-ba60-807ce4939921 | -5.2057 | -48.179401 | 2024-10-12 00:24:47 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6d1b69f-c686-332b-9720-c4794399bda3 | -4.6001 | -45.615898 | 2024-10-12 00:24:48 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67f5bd3d-ea29-3fd3-8ed9-499b81327395 | -4.6016 | -45.622799 | 2024-10-12 00:24:48 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a57e355c-1e48-33c5-924c-0e3232b21b06 | -4.6032 | -45.6297 | 2024-10-12 00:24:48 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92699367-0942-3301-b933-f9d1568f6d7b | -4.5918 | -45.624901 | 2024-10-12 00:24:48 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb30ad8c-42a6-3c80-a5cd-4a01546267ce | -4.8666 | -46.844398 | 2024-10-12 00:24:48 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9498fafa-428d-3058-956c-af0a3a4a90f6 | -4.8681 | -46.851299 | 2024-10-12 00:24:48 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2c40a0-71e8-3bfd-afa4-b7e5ddbfa9fd | -5.0962 | -47.918201 | 2024-10-12 00:24:48 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d9729bb7-223b-3f57-9981-85c528092798 | -5.0978 | -47.925499 | 2024-10-12 00:24:48 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c05b3a90-099a-3950-9876-46027ee1eab3 | -5.078 | -48.067902 | 2024-10-12 00:24:49 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e47210e2-3a7a-3d6f-a6b4-218de92734b4 | -5.0797 | -48.075199 | 2024-10-12 00:24:49 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9440b76-4244-397d-af1a-b8d84cbc183e | -4.4748 | -45.882 | 2024-10-12 00:24:51 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 918576d0-a676-3c1d-9029-e54ef9eb64ea | -4.6196 | -47.350498 | 2024-10-12 00:24:54 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9efaf66-fdc5-3fec-8b9a-465ca6a8d0d3 | -4.6211 | -47.357498 | 2024-10-12 00:24:54 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| efc3cf5a-a184-39c9-a816-abd0b61c18d8 | -5.2083 | -50.148102 | 2024-10-12 00:24:54 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 003d15ae-6b14-3796-8b6b-da52996b6e64 | -5.2103 | -50.157299 | 2024-10-12 00:24:54 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5802c6d6-b806-3bbe-bd3a-1778dc509b46 | -4.199 | -45.7561 | 2024-10-12 00:24:55 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e84100bd-c756-3305-9033-0bc9e685c39a | -4.2005 | -45.763 | 2024-10-12 00:24:55 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6358fa61-f4e0-3c6c-8075-64457d5ee8d5 | -5.0165 | -49.741699 | 2024-10-12 00:24:56 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 244bb966-323f-314f-ad94-25c604c1b24d | -5.0184 | -49.750401 | 2024-10-12 00:24:56 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 765aef91-f3ef-3a14-abfc-5d249b3c58ac | -5.0067 | -49.743801 | 2024-10-12 00:24:56 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d098f292-e843-3860-b01e-6c109fa1afc9 | -4.4763 | -47.722599 | 2024-10-12 00:24:57 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 334e9ba6-fae7-32e6-be18-01bd246fe68b | -4.4779 | -47.729698 | 2024-10-12 00:24:57 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c324ec35-b084-3020-919f-2bb6e92fd07f | -4.2923 | -47.452099 | 2024-10-12 00:24:59 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b49f8e-2f5c-349e-8372-324a38c3e84d | -3.9477 | -46.422901 | 2024-10-12 00:25:01 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10b34588-1bfc-3987-823b-2311b444968f | -3.9493 | -46.429699 | 2024-10-12 00:25:01 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5c1467d-0766-3f92-94cd-282511d03c18 | -3.9508 | -46.436501 | 2024-10-12 00:25:01 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97951dfd-8d9f-3ae1-b343-07c5c03b60c2 | -3.9379 | -46.425098 | 2024-10-12 00:25:01 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b636a68-2436-3e83-8cb7-e0680ebb2d5c | -3.9395 | -46.4319 | 2024-10-12 00:25:01 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30f46c45-e0df-3f88-8ede-2a1c877e8b8e | -3.941 | -46.438702 | 2024-10-12 00:25:01 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f53802b8-5784-3cd3-869d-0cf0a10e7aa0 | -4.3844 | -48.6031 | 2024-10-12 00:25:02 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22d53a8f-dc53-37b2-af38-8fb79f9c7774 | -4.3861 | -48.6106 | 2024-10-12 00:25:02 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3b48936-7ae8-37f1-a007-b940953cdc09 | -4.2786 | -48.220299 | 2024-10-12 00:25:02 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc09d28f-9b84-321e-bc2b-0bf9497398f1 | -4.2802 | -48.2276 | 2024-10-12 00:25:02 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc099b2d-8146-362d-9eb6-29d4ee17a362 | -4.8353 | -50.785999 | 2024-10-12 00:25:02 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca9358a9-f56c-3034-9669-18e6bd93cdf2 | -4.0321 | -47.210201 | 2024-10-12 00:25:03 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8070b93f-3479-3774-8149-97f190af9db5 | -3.9968 | -47.649899 | 2024-10-12 00:25:05 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee2ef00-2fa0-3af7-92e8-24236edfc26b | -3.9984 | -47.657001 | 2024-10-12 00:25:05 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3c78ae6-488d-35cf-b4e2-7cfaa2205d63 | -4.1151 | -48.225399 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a8fb1ea-3f8e-35db-80c1-1a2fac77306e | -4.1167 | -48.2328 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 763b2708-e605-33b8-9543-d1231c66a05a | -4.1184 | -48.240101 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15fed452-0625-3905-8615-046e8e77803d | -4.12 | -48.247398 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e49cfb06-b7d0-3b4f-a51e-eea08b4bdeb0 | -4.1216 | -48.2547 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f95f12eb-73c0-3875-9276-2833a9703e3b | -4.1233 | -48.262001 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c694573a-b392-3f71-98f8-5991f7ca4b4a | -4.1249 | -48.269402 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1bfc578-fcd2-3eca-bcb6-025e0abc0151 | -4.1053 | -48.227501 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6a5b993-bd8f-3520-8df6-2f891b4c5de0 | -4.1069 | -48.234901 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21130d74-8c91-32da-aaaa-fcb99bc7918c | -4.1086 | -48.242199 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78df28a-531e-3fbb-ba04-b619d79d6024 | -4.1102 | -48.2495 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0fe438c-3e3e-3aa2-aabc-153988730af5 | -4.1118 | -48.256802 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a1e111-da0b-3dca-a6c4-e32f54e61205 | -4.1135 | -48.264099 | 2024-10-12 00:25:05 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f92fc3-1e94-3753-8710-59bffaf31195 | -4.6635 | -50.937698 | 2024-10-12 00:25:06 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26fdeda-7551-3bf1-b027-352c0f66a2d6 | -4.0547 | -48.230999 | 2024-10-12 00:25:06 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2193aae6-5d1b-3c44-97b7-dab28244f91d | -4.5275 | -50.411301 | 2024-10-12 00:25:06 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5155008c-f3b1-37a0-9345-17d8871f86cb | -3.9606 | -47.948399 | 2024-10-12 00:25:06 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6f98f69-fc83-373b-a0be-ee4900571737 | -3.9622 | -47.955601 | 2024-10-12 00:25:06 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5132c9c1-47b0-3cf9-a18d-38ac9629c879 | -3.9508 | -47.9505 | 2024-10-12 00:25:07 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7c0c4a5-a9b9-3604-a7a7-e1e9f7a4f386 | -3.9524 | -47.957699 | 2024-10-12 00:25:07 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db040eca-71e5-320c-967b-ef9fb39b73d7 | -3.9222 | -48.3293 | 2024-10-12 00:25:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60d66ce9-3f31-3196-8738-bd9fe93af6b9 | -3.9238 | -48.336601 | 2024-10-12 00:25:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b864f66a-2eda-3e5b-8a90-cc794b407a73 | -3.9254 | -48.344002 | 2024-10-12 00:25:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e20ec449-61bd-39a2-b4fc-2e5550901098 | -3.9156 | -48.3461 | 2024-10-12 00:25:09 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c91c0a6-da57-3d2c-9e45-5bf3e5fa0c67 | -4.2144 | -49.736401 | 2024-10-12 00:25:09 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e77bce8-a9dc-3c62-9cf8-0f9f2c6f1f8d | -4.2162 | -49.744801 | 2024-10-12 00:25:09 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47faeeac-90b0-351a-b70d-d4ba19488b0b | -3.9849 | -48.9799 | 2024-10-12 00:25:10 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ad207b-7e15-34e7-a0bc-bd680fdb548b | -4.3831 | -50.780998 | 2024-10-12 00:25:10 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09da13d3-60a5-35aa-8cb5-417fab3992a1 | -4.3852 | -50.790699 | 2024-10-12 00:25:10 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 032ed81a-6011-3a1e-a305-f5cc94023488 | -4.3874 | -50.8004 | 2024-10-12 00:25:10 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6ca6162-b432-3a8b-b393-43d627db0210 | -4.3754 | -50.792801 | 2024-10-12 00:25:10 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eba1e077-7f88-392c-b183-07783e78a99a | -4.3776 | -50.802502 | 2024-10-12 00:25:10 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef3570c-4330-36ef-87b9-762cf5be35f9 | -3.7159 | -47.912399 | 2024-10-12 00:25:10 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae3540f-1c78-3f31-98c8-ac5ee8217b94 | -3.7174 | -47.919498 | 2024-10-12 00:25:10 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9241be0d-268f-3f3e-9d82-ef4a3bfd83a4 | -3.7075 | -47.9217 | 2024-10-12 00:25:10 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e252e10d-b602-331f-be72-5f8cf4c362bb | -4.2838 | -50.936001 | 2024-10-12 00:25:12 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a8fc2f6-b769-3d66-bd61-d60a183a8624 | -4.286 | -50.9459 | 2024-10-12 00:25:12 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49fb3ef6-84af-3daa-9693-9bf9b0866dd9 | -4.2882 | -50.955898 | 2024-10-12 00:25:12 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47895680-fbaf-3ef6-92a2-fe8fbb9938ce | -4.274 | -50.938099 | 2024-10-12 00:25:12 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 659bb713-517d-31db-8bef-702d60ee2870 | -4.2762 | -50.948002 | 2024-10-12 00:25:12 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9345550c-27a2-3bd3-afb0-a187dd0659cc | -4.2784 | -50.958 | 2024-10-12 00:25:12 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2731c728-37fe-35db-a49c-c3fda87ab4eb | -3.3154 | -47.000599 | 2024-10-12 00:25:13 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9fa070-357f-38da-89a9-2e6c135ae15a | -3.317 | -47.007401 | 2024-10-12 00:25:13 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eba76ba9-c238-3321-bb7d-d6e0419d1dfd | -3.3185 | -47.014198 | 2024-10-12 00:25:13 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffe3d5b7-ad17-332d-8cb0-e68b9e552a16 | -3.2224 | -46.770199 | 2024-10-12 00:25:14 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e7ae794-5008-35c7-8878-ce6c7cc984d0 | -3.2239 | -46.777 | 2024-10-12 00:25:14 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cbd9c86e-a413-34a3-a647-d17c4dadb37a | -3.2255 | -46.783798 | 2024-10-12 00:25:14 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e213cf6e-45f6-3bcd-b0d0-f981a669a47f | -3.0009 | -45.835098 | 2024-10-12 00:25:14 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b81d115-02b1-329a-8053-0e82ee2b40bc | -1.5877 | -53.3494 | 2024-10-12 00:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f344ec81-d4ad-36a7-9862-76fcc81c6a46 | -1.6169 | -48.0269 | 2024-10-12 00:25:15 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 08715ac6-09f0-38f3-8bff-fcbc29870bf3 | -4.0272 | -50.981098 | 2024-10-12 00:25:16 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b45e7d-113c-3397-8bc4-eb09ea16a8c8 | -4.0293 | -50.991001 | 2024-10-12 00:25:16 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d3ccce-4e23-36cb-a9f2-b012d28cfccc | -4.0315 | -51.0009 | 2024-10-12 00:25:16 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbfe85f7-1912-3a59-b40a-badf4c9b58b8 | -3.6626 | -49.6115 | 2024-10-12 00:25:17 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a092da85-9cad-3a93-ae3b-dd65fabdd794 | -3.6644 | -49.619801 | 2024-10-12 00:25:17 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 863e9dfa-5b7f-3298-9c47-1188504627f9 | -3.64 | -49.556301 | 2024-10-12 00:25:17 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 878f6901-cb8e-31cf-bba5-ed10d1fdc4b7 | -3.6528 | -49.613701 | 2024-10-12 00:25:17 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
