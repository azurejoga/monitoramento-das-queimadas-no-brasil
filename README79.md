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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e063a788-dabc-3a1f-be44-8b65f827b8ad | -5.5634 | -46.28983 | 2024-10-08 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1b080dc-e37f-3bf9-b8cc-9a58329df723 | -5.56288 | -46.28704 | 2024-10-08 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5667272-d07c-3f3f-8533-0831437faa30 | -5.56214 | -46.2923 | 2024-10-08 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a029675-d7e9-3a87-b72b-54b10cf09e0c | -5.50566 | -46.38148 | 2024-10-08 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc47f6f7-b39c-3a84-b5a9-4d2bd6fdb567 | -5.50086 | -46.38084 | 2024-10-08 04:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2968774a-76bb-394b-a9e3-770f120d9e2d | -6.33508 | -45.72096 | 2024-10-08 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0495d2ec-f25d-3600-aee5-fcdf1b4f6b83 | -6.33466 | -45.72392 | 2024-10-08 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e89a3eb-ae11-37f3-9e01-d7e3678de8a4 | -6.33424 | -45.72686 | 2024-10-08 04:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c3a893a-e72d-3e3d-9e72-9418aace8e72 | -5.91779 | -45.39245 | 2024-10-08 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0baf8478-d408-3ccf-8e5b-295831d9ee5b | -5.91734 | -45.39565 | 2024-10-08 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d002974-1777-36e0-8f31-2fe47e3b915d | -5.91689 | -45.39887 | 2024-10-08 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c82265d7-b630-3052-802b-df9c373aea46 | -5.91216 | -45.39506 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 259be65c-39e9-32bd-b484-33c697ad2401 | -5.91171 | -45.39828 | 2024-10-08 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3a8c7b2-9363-3657-b855-236e1f0e21b5 | -5.5204 | -45.25647 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83b511a8-2a19-36db-9d29-3fb3a1487a02 | -5.51996 | -45.25962 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a42d27f-ba21-3cf3-9dff-76188c42cf70 | -5.51347 | -45.48862 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b884c95-b53c-3fa1-ad32-2ad7a512daf6 | -5.51305 | -45.49148 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07fc038d-2864-36f5-8eec-7a7073e44fb1 | -5.39849 | -44.95248 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95d421d2-8896-3de6-b7b7-2aac71f9a9e7 | -5.3937 | -44.94842 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4561884c-bea9-3d03-99c2-ab8931cf0707 | -5.39322 | -44.95172 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cff91093-7d13-37c1-bba9-50f7a05d9144 | -5.28374 | -45.38208 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28dea072-043d-3cbb-ad34-25849f851793 | -5.27717 | -45.12305 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 772b3d5a-3a43-3d2c-b54b-360b87c1bf49 | -5.27244 | -45.11898 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10db7a5a-2b4c-30bf-9c42-38519cd13478 | -5.27198 | -45.12218 | 2024-10-08 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1579eb52-a9ca-38c5-b3f3-5c758808715d | -7.52686 | -46.59259 | 2024-10-08 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54bd233a-6956-364f-9529-8255b89c5934 | -7.52472 | -46.5912 | 2024-10-08 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d4972633-fc2a-30a0-854d-85ae24a6163b | -7.46134 | -46.6902 | 2024-10-08 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96576490-b9f5-3861-8691-266f52b8d8ef | -7.01342 | -45.3754 | 2024-10-08 04:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f20bec67-4276-3ac9-b356-72af8132e6c2 | -1.17453 | -46.73001 | 2024-10-08 04:55:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e4a5af7-a6c2-3b3c-af82-d6bcf6f203e6 | -3.30618 | -47.00866 | 2024-10-08 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e613dea-7a94-3709-b788-6889ac8948d2 | -3.28837 | -47.1225 | 2024-10-08 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33d4b562-9dfe-32db-b259-f2d65161a46e | -3.28822 | -47.12435 | 2024-10-08 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 031dbd97-affc-3e8f-9377-1a2ce54e4aeb | -3.28776 | -47.12663 | 2024-10-08 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 985fdb2d-54ff-36ae-b43d-9e5378920bcb | -3.28757 | -47.12849 | 2024-10-08 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dea64876-99aa-34e3-a839-821062ef2ffa | -4.95145 | -47.40551 | 2024-10-08 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b36d8bc-0b9f-3d11-9af8-1c5e95d21244 | -4.58764 | -47.17298 | 2024-10-08 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bec8484-36c4-32c1-bfbb-27c96c89171c | -4.58316 | -47.17231 | 2024-10-08 04:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f07b8ce-35bb-36fc-a2ae-1ed616918050 | -4.47672 | -47.73416 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11abebbd-40a1-3520-84fa-25ae47c68deb | -4.47494 | -47.73265 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8441030-b3a5-3ad2-90ee-a2d559f1bf85 | -4.47437 | -47.73653 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 940343ea-5389-3cb0-abfc-d3245278eb17 | -4.47243 | -47.7335 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 940ead0f-739f-37e1-9caa-087c54497f6f | -4.35431 | -47.30086 | 2024-10-08 04:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a734bc76-4cf8-3cce-afb6-0f4e428d0faf | -4.31661 | -47.70646 | 2024-10-08 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0748a02f-15b2-3bed-bd1f-47b056edbbf0 | -4.274 | -46.28169 | 2024-10-08 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92c5779e-62ed-3a42-bdc1-1e3a064bb611 | -4.27331 | -46.28649 | 2024-10-08 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 940bf502-3000-3b56-96df-cfdf1e42f06e | -4.27233 | -46.28485 | 2024-10-08 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f6121ea-c2a9-3e35-9bc4-11686d320cd3 | -4.26925 | -46.28109 | 2024-10-08 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f78e3331-82c0-315f-9c21-c28ab789a3a6 | -3.93831 | -46.44244 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a9953e81-7d0b-3ca3-bba0-a09d7dfda00a | -3.9376 | -46.44727 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cbbb562c-95bc-3a00-82f4-6e486d9b9b08 | -3.9369 | -46.45209 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 281003e5-4079-3c80-afa6-097f22f4e5b0 | -3.93365 | -46.44171 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8c3a97ae-a0b3-33dd-a5a1-0e8271d01db2 | -3.93295 | -46.44658 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c6720010-2024-3d0b-982f-e0def8104809 | -3.93178 | -46.43951 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25efe02e-fd02-3187-b9ed-a28d8b01d6bd | -3.93103 | -46.44439 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 785dd874-bfbe-3304-aca7-05f90e62b07a | -3.929 | -46.44099 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 08a6007b-69cd-31e9-bd8f-1024e56f50b1 | -3.92082 | -46.41768 | 2024-10-08 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d871118b-9fb0-3a2a-a031-ca5908c3a790 | -3.70019 | -47.60078 | 2024-10-08 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b109f4ac-6435-318b-a28c-1f9d2929d792 | -3.69958 | -47.60478 | 2024-10-08 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeee4b3a-3038-3264-8e62-113f6f287cd1 | -6.1347 | -47.21468 | 2024-10-08 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88c33ecb-243b-34f8-a68d-3ab2460d18e0 | -6.13014 | -47.21399 | 2024-10-08 04:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59421c9f-aad7-3a5d-8f6e-8a8a28b8d724 | -6.05353 | -46.59917 | 2024-10-08 04:55:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496f4146-1d4b-35e5-afb5-6a601c374bce | -6.05309 | -46.60292 | 2024-10-08 04:55:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57af0af9-46a2-34cb-9e21-769c9c802eca | -6.05282 | -46.6042 | 2024-10-08 04:55:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4e35796-3fa7-3d2a-91ad-69cecd9b7376 | -7.89353 | -47.72298 | 2024-10-08 04:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a79ccde7-587a-35da-aa64-5d96073be426 | -7.889 | -47.72239 | 2024-10-08 04:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b366161b-ddf7-334e-a309-2bd30489ecc7 | -7.62937 | -47.74887 | 2024-10-08 04:55:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1c3d641-54d2-307b-aeeb-93913ae5f9b7 | -7.60329 | -47.10384 | 2024-10-08 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db954010-22b8-3102-8bd8-17ca7b37de89 | -7.6026 | -47.10882 | 2024-10-08 04:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d57eb4b-d4ee-3941-a29f-641401999e42 | -7.09043 | -47.86705 | 2024-10-08 04:55:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 649ae9ee-af81-37eb-90bd-53c1d85fda6a | -6.75888 | -47.99346 | 2024-10-08 04:55:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e510b9b-b521-31b5-85a3-7e9ad990ec56 | -6.66673 | -47.11081 | 2024-10-08 04:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2440db48-d060-3412-a01f-02f8d076d268 | -6.66211 | -47.11004 | 2024-10-08 04:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ff2d2e1-5959-3750-9f51-4907703c30cf | -6.64821 | -48.1087 | 2024-10-08 04:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 762fdb0c-cf5e-3249-ace1-f82c37ff0506 | -6.59771 | -47.7787 | 2024-10-08 04:55:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8007b1f7-c857-361e-94da-f7f4dc3c61d5 | -1.61481 | -47.46559 | 2024-10-08 04:55:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fdd8619-8390-35b3-9868-42d4f1be61f2 | -1.61466 | -47.46836 | 2024-10-08 04:55:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b524bdef-738f-38aa-9903-d934b4ef232e | -1.61421 | -47.46937 | 2024-10-08 04:55:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5398c60b-dbe8-3c75-a852-f0bafd071315 | -1.59146 | -48.03191 | 2024-10-08 04:55:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb8dda1-6d92-30ea-8cca-e5cecf27bfc6 | -1.34803 | -47.21286 | 2024-10-08 04:55:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cc1c9f1-c6bc-3c8d-b739-6e84940ae9f1 | -1.34743 | -47.2168 | 2024-10-08 04:55:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96c9ea38-106f-39f6-a7b7-eecb865ab373 | -3.49566 | -48.89465 | 2024-10-08 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80e37741-363f-38fa-abe1-7147b25f3a56 | -3.49173 | -48.89407 | 2024-10-08 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5f845d5-fbd4-3f75-9369-457679e476ae | -3.48706 | -48.89843 | 2024-10-08 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 356e58b4-2569-3e40-84df-431c2e41f8ce | -3.48631 | -48.90336 | 2024-10-08 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0678a0fe-0424-332e-8ed7-3ce2eaa94160 | -3.46285 | -47.66063 | 2024-10-08 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c383496a-1770-34f4-b5a2-a007b256bdae | -3.46225 | -47.66465 | 2024-10-08 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f4ebf8a7-d99b-3f68-9f21-f32a21e82327 | -3.45918 | -48.82118 | 2024-10-08 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcc1dffd-f956-3230-abbe-ea5fa5a9458a | -3.45897 | -48.81788 | 2024-10-08 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eb96e42-9723-35ad-a6a6-2779638c8b5d | -3.22346 | -48.92497 | 2024-10-08 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76b8294a-e0f1-32fd-9b9d-5cc229247cea | -3.22281 | -48.92706 | 2024-10-08 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d686da24-a4f8-334d-938f-f849becc9770 | -3.21956 | -48.92439 | 2024-10-08 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f6907e8-7042-3942-b68c-a4f99b087636 | -3.21891 | -48.92646 | 2024-10-08 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c832644c-4d37-385d-bc5d-4e3b09f58be5 | -2.79345 | -48.57468 | 2024-10-08 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0ad3a29-78bb-36e1-a451-551ab21d906d | -2.79026 | -48.56902 | 2024-10-08 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5c078532-b092-3359-980b-712251f235d5 | -2.78949 | -48.57408 | 2024-10-08 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 387a53b5-7b11-36db-99e6-0fcac34f9a50 | -2.40788 | -48.59089 | 2024-10-08 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bbb7dfd-6637-35ad-85a3-7d20f020d9b7 | -2.4071 | -48.59584 | 2024-10-08 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34bbd93d-d15a-3829-9631-0e1194d6b513 | -2.40695 | -48.59262 | 2024-10-08 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2324a86b-7198-35db-9ad0-53d5afccc2f6 | -2.4062 | -48.59758 | 2024-10-08 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a3a0a2a-1397-3b4a-8f21-36571d72e5f6 | -2.38988 | -48.62869 | 2024-10-08 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README80.md)
