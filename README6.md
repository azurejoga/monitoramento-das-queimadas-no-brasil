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
| 52e33ce6-493d-3b91-aad6-8bcea338bc03 | -13.6671 | -53.9314 | 2026-06-27 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f257b9e3-3694-35b0-a0b4-34c62f62b9b8 | -5.7756 | -45.0826 | 2026-06-27 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 905960bf-6345-3652-997e-45d30399d7db | -12.6236 | -57.8926 | 2026-06-27 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 130.9 |
| f248a5b0-0344-3ebe-8552-56ca15641a70 | -5.7945 | -45.0586 | 2026-06-27 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 2e879cc2-6caf-3c58-a4fc-55c4f90354cc | -7.7361 | -44.1823 | 2026-06-27 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 57117883-d2ff-35f7-b4a0-c75903b0e4a7 | -10.5634 | -46.2362 | 2026-06-27 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2c6d120e-1084-3909-bd4c-1a1f04b131d0 | -10.6571 | -50.2212 | 2026-06-27 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| adfdf677-cf68-3549-b180-82f65d88a59e | -12.4654 | -58.481 | 2026-06-27 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| eaf243b5-335c-3f59-9beb-67731aedf339 | -10.6385 | -50.2018 | 2026-06-27 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 10e4e348-5312-38b1-ab0e-4c54b278610c | -12.8363 | -44.3186 | 2026-06-27 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ef88e463-5c22-34d2-b05d-8d2495d78bb0 | -12.8165 | -44.3454 | 2026-06-27 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| ad1ac2b6-8649-3bc5-a5c7-4f2a76f9075b | -12.8354 | -44.3657 | 2026-06-27 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 59279c46-bab4-3d6f-a4ca-d77b4cd82ab4 | -12.4462 | -58.5023 | 2026-06-27 01:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 91cb4486-7f68-3175-ac4a-8e7f5ddd0e2e | -12.6238 | -57.8727 | 2026-06-27 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 52c1f880-0708-30d8-849c-c8c03b223739 | -7.7361 | -44.1823 | 2026-06-27 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| eb09975c-faee-3419-a7c1-bd5edf21e537 | -7.755 | -44.1805 | 2026-06-27 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 97fd361e-70c7-3919-8072-07c1dcedaa61 | -5.7758 | -45.0599 | 2026-06-27 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 52d3429a-a249-3e97-9d47-e013aaf210f9 | -12.4651 | -58.5009 | 2026-06-27 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 69b8cef2-a758-398c-9b32-d2e2db4792ad | -12.4462 | -58.5023 | 2026-06-27 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| bc4849f8-8bbc-341b-aa47-ecb044f14a13 | -10.6195 | -50.2038 | 2026-06-27 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 01a2a484-7559-3ca1-aa42-e5df1a66bdc0 | -10.6385 | -50.2018 | 2026-06-27 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1cc9b800-7e98-3244-aaed-82f1882b5ad7 | -12.6236 | -57.8926 | 2026-06-27 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 5e6fcbbf-aea7-3d34-a6b4-094805fa1968 | -10.6192 | -50.2252 | 2026-06-27 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| d50cfb52-3427-3f46-af45-56eca4033d2c | -12.8165 | -44.3454 | 2026-06-27 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 236fbf87-f123-3fd9-927e-3110c3edd65f | -10.6382 | -50.2232 | 2026-06-27 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2885df45-54ba-398c-81fb-876a5fd06351 | -12.6238 | -57.8727 | 2026-06-27 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| fb16fc0a-8233-32f8-9084-bd646a47973d | -10.5634 | -46.2362 | 2026-06-27 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 355939ef-ef09-3852-b04a-fb5be2e20142 | -5.7945 | -45.0586 | 2026-06-27 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 4854aa78-6523-3232-8453-f4cfcc83840c | -12.8359 | -44.3422 | 2026-06-27 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 225.6 |
| 01802568-82d5-3b4e-8caa-c0f6bf05a0d7 | -13.6671 | -53.9314 | 2026-06-27 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 128215ab-80b8-3856-919b-d44715146144 | -12.4654 | -58.481 | 2026-06-27 01:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| b18a4b2d-3f63-3625-8af6-e6ee403d770f | -10.6571 | -50.2212 | 2026-06-27 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 1b08b89d-6e18-3ffc-8b0d-3af0c4fb22f0 | -12.6046 | -57.8942 | 2026-06-27 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6da61898-4353-312c-9114-76a43a034f52 | -5.7756 | -45.0826 | 2026-06-27 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e32cf90a-cbd0-35d9-aa68-de45e13b7b08 | -12.8354 | -44.3657 | 2026-06-27 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 34acce72-8672-36f0-9b43-cba1d2d3b567 | -12.4654 | -58.481 | 2026-06-27 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 454db502-2ba7-3856-8af7-335e7a9fd96a | -10.6382 | -50.2232 | 2026-06-27 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e21dc63b-af10-3419-8f90-bf185816fa6f | -12.4651 | -58.5009 | 2026-06-27 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| adf2af55-d2d9-3c61-a717-8968b1893739 | -12.8359 | -44.3422 | 2026-06-27 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 18455c8c-f3ba-3cdf-b30a-d9aa0546df21 | -12.6236 | -57.8926 | 2026-06-27 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| c8b9dc42-5f60-3a48-9593-9506fd1ee5fc | -7.7361 | -44.1823 | 2026-06-27 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 484ad68f-53fa-3fe3-9cf8-190484bee3c3 | -12.8165 | -44.3454 | 2026-06-27 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 5d5c4373-6f87-3a47-baba-0aa0a19f12dd | -10.6385 | -50.2018 | 2026-06-27 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 025ab6c7-19e4-3c5f-8355-bd9d480be157 | -5.7758 | -45.0599 | 2026-06-27 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 21395bd2-e373-3f0d-ab64-9d232cd6ad3e | -12.6046 | -57.8942 | 2026-06-27 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 4dd5d252-d580-3584-84c0-d835b071373b | -12.4462 | -58.5023 | 2026-06-27 01:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| fdd2d69e-7f89-3d84-81a6-205fcd6ee208 | -12.6238 | -57.8727 | 2026-06-27 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 596642b3-6750-3bbb-a45b-181d8987d258 | -10.6195 | -50.2038 | 2026-06-27 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| ae13023a-8d86-3807-8bfb-a85adb7693fe | -12.8354 | -44.3657 | 2026-06-27 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6f9712eb-cae5-3e37-b692-c0b0304ef3ee | -7.755 | -44.1805 | 2026-06-27 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 748e2d27-a72f-387a-b1b2-da970addc344 | -5.7756 | -45.0826 | 2026-06-27 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a4161f8f-442b-3dd2-ac60-f4881a1bb993 | -12.4651 | -58.5009 | 2026-06-27 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| eee4c326-2890-346c-95e5-ce5fd0393cfb | -12.4654 | -58.481 | 2026-06-27 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 49af25f8-ad12-33ca-878b-34e388e93a09 | -13.6671 | -53.9314 | 2026-06-27 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| bad23261-c066-3a83-bfe7-4e4e3b86b429 | -12.8359 | -44.3422 | 2026-06-27 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 27ac45dc-b468-3cae-9455-b611c55fc58b | -12.6236 | -57.8926 | 2026-06-27 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 8c0977cd-5fda-3cf0-8ba2-60081207aa4f | -12.6046 | -57.8942 | 2026-06-27 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9b0e421c-7d44-3fa7-81a7-803a3002e331 | -21.7626 | -56.2581 | 2026-06-27 02:00:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 32cd2c7f-c8cd-344b-bc66-ec1f7e4725f0 | -12.8165 | -44.3454 | 2026-06-27 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| a13da255-97d7-3ddd-b66e-5a15b1163bbd | -10.5634 | -46.2362 | 2026-06-27 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9c776a44-4072-3517-ade8-7b6e325b2283 | -10.6385 | -50.2018 | 2026-06-27 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 5a8c0a26-7ec8-3a93-bd67-cac375a3a75d | -10.6382 | -50.2232 | 2026-06-27 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1cf7b653-2b0a-3c2a-b10e-5f71433c23e0 | -7.755 | -44.1805 | 2026-06-27 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c4385e54-243c-33be-b0a2-fbc624f0f757 | -12.8354 | -44.3657 | 2026-06-27 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f7a6216e-2fb7-31ff-9869-e20420761008 | -7.7361 | -44.1823 | 2026-06-27 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e0e972ad-77e8-36ad-a6fe-90e4dac2b127 | -12.8165 | -44.3454 | 2026-06-27 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 5fa9f262-fb17-3a74-ad89-86f71e650ea7 | -10.6385 | -50.2018 | 2026-06-27 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 47f5a4c1-a2dd-38f8-9a9a-14fc011ed79e | -11.9095 | -57.4134 | 2026-06-27 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 6a9e472a-ba2a-3dcd-a189-7aa7b9b3fd92 | -10.6382 | -50.2232 | 2026-06-27 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1258185c-3850-38a4-9357-9827b30eb380 | -10.5634 | -46.2362 | 2026-06-27 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 4d513820-ddd3-36e5-94dc-b7ad5717c86b | -12.6046 | -57.8942 | 2026-06-27 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 58728ce7-4d5c-3504-8b4a-be0bf7f6f532 | -12.4654 | -58.481 | 2026-06-27 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 24064d47-41ed-3491-868c-f7021d4d4407 | -5.7758 | -45.0599 | 2026-06-27 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| f652f339-570e-3f02-99a7-74d7ae778481 | -12.8354 | -44.3657 | 2026-06-27 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| e2eea811-fd98-37c9-9c33-1fe0f6239666 | -12.6236 | -57.8926 | 2026-06-27 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ed69da0b-b04a-31f9-81b9-efbd5522ba42 | -7.7361 | -44.1823 | 2026-06-27 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| fdea10e1-e9d7-313d-8869-e954eb4ed90d | -12.6238 | -57.8727 | 2026-06-27 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 03ad8d7a-a460-33a9-a86d-6e77cc0191d7 | -12.4651 | -58.5009 | 2026-06-27 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| e32f67a3-f935-383e-afbc-6e51d59801ec | -12.8359 | -44.3422 | 2026-06-27 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 437c0401-9077-3271-b04b-0ae1bd94ef2c | -5.7756 | -45.0826 | 2026-06-27 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7934cb9e-cc77-3bb2-a12d-3ffc4054c6a3 | -12.8359 | -44.3422 | 2026-06-27 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 61ef4b0b-bdc0-361d-a698-c4bd3d7b48bd | -12.8165 | -44.3454 | 2026-06-27 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 42e92093-69d4-3ff6-9c8b-41f45b25b229 | -12.6236 | -57.8926 | 2026-06-27 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2756b83c-00f1-3d7c-8650-0b3f170da319 | -12.4654 | -58.481 | 2026-06-27 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e336d68a-41fd-36c9-b607-acc312506980 | -12.4651 | -58.5009 | 2026-06-27 02:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f9aeb94f-f26e-32b6-a4a1-7a93b480f9f1 | -7.7361 | -44.1823 | 2026-06-27 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9a2e0004-dd83-3011-8948-4a8f4c73d161 | -5.7945 | -45.0586 | 2026-06-27 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f974c754-be22-3322-bc57-505bc583e50e | -12.8354 | -44.3657 | 2026-06-27 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 59620f3e-faf5-3064-9e5c-0a990dbfd11c | -21.7626 | -56.2581 | 2026-06-27 02:20:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 4feab17c-f149-381d-b4a0-42c456439847 | -5.7758 | -45.0599 | 2026-06-27 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| eb9bb5cb-6d36-3588-98d1-95802748dd13 | -12.6046 | -57.8942 | 2026-06-27 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 68b4ef57-c9f3-31fe-b5bb-38e6001f1d6c | -10.6382 | -50.2232 | 2026-06-27 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| d2acd6a3-d2b9-3ed6-ac47-ed07e4a057d5 | -12.4654 | -58.481 | 2026-06-27 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8c9cb6bc-415b-30e6-a445-4ba84d7d2c1d | -12.4651 | -58.5009 | 2026-06-27 02:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 744b95e6-968f-3439-b0e8-5393c63bb4f9 | -12.6236 | -57.8926 | 2026-06-27 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| d9007cf9-4da4-304b-ae5b-35c22904fb4e | -5.7758 | -45.0599 | 2026-06-27 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 95f84f3b-ee6c-3d23-ad48-8980b5c01f08 | -12.8354 | -44.3657 | 2026-06-27 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ca465f5b-f624-3d1f-ad5a-570c8020dbe1 | -12.8165 | -44.3454 | 2026-06-27 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ad56a465-8eb2-3c2b-b6b2-696ef1b23e48 | -12.8359 | -44.3422 | 2026-06-27 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| c922d440-a74f-34a6-9886-a35f56f9898b | -7.7361 | -44.1823 | 2026-06-27 02:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |


[Clique aqui para ver as próximas entradas](README7.md)
