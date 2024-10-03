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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abfe4c45-be9d-3068-bd50-12703e0c567e | -11.5187 | -63.7038 | 2024-10-03 01:50:26 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc425eb6-af03-3ede-b607-e2e6d001d269 | -11.3317 | -63.039001 | 2024-10-03 01:50:27 | METOP-B | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a208abb6-5d07-397a-87ba-631e98f0b64a | -11.5434 | -63.942902 | 2024-10-03 01:50:27 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 183e4e05-c366-33bb-84c0-dd429277a766 | -11.596 | -64.1698 | 2024-10-03 01:50:27 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4813b0f-a98a-3d03-8f59-5b846644ad67 | -11.5978 | -64.177498 | 2024-10-03 01:50:27 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f5de81f6-f682-38ed-b358-0decb8ee9857 | -11.5996 | -64.185303 | 2024-10-03 01:50:27 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 31415796-0321-3c22-aca6-bfefd01af8b5 | -11.588 | -64.179802 | 2024-10-03 01:50:27 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9deb9cbc-2a51-3857-816b-1516c79ab038 | -11.5898 | -64.187599 | 2024-10-03 01:50:27 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1cc9778a-bb19-39bb-9831-36a4516b7748 | -11.6776 | -64.973099 | 2024-10-03 01:50:28 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c17f1069-9cc8-3da3-9ceb-aee8f8bfd1be | -11.6793 | -64.9804 | 2024-10-03 01:50:28 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b1123fb7-0681-3625-8e8d-d0995fb1d723 | -11.681 | -64.987701 | 2024-10-03 01:50:28 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 27559277-e730-356a-a466-2078cf48f5ca | -11.6843 | -65.002197 | 2024-10-03 01:50:28 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c653d67-7f7c-3f7c-b8a0-6b882b8038f8 | -11.686 | -65.009499 | 2024-10-03 01:50:28 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3eeb8801-4bc1-343f-bf5f-14493d0c112b | -11.6876 | -65.0168 | 2024-10-03 01:50:28 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05b1eb08-d018-3a69-8402-8e41782d4aa5 | -11.6678 | -64.975403 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a43ef137-75d2-3385-8516-00cb76117b2e | -11.6695 | -64.982697 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eadd3ca2-2031-3292-af23-b804755f9f9e | -11.6712 | -64.989998 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e30d61e2-0871-32cb-af22-63b59755667a | -11.6728 | -64.997299 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad67aac6-f6ac-33bf-96f9-36056f06569c | -11.6745 | -65.004501 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4cff9f-7edb-3c62-a5e2-58415d48daad | -11.6762 | -65.011803 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a28fe7a0-5d53-3a99-a6cd-5151234821fe | -11.6778 | -65.019096 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3c26e8-f2ea-3574-ba89-7ae30593bf95 | -11.6564 | -64.970398 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cffea54b-0f15-3465-baec-44fe8ead0fe1 | -11.6581 | -64.977699 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afffe3f3-3070-39a0-9ee3-f412ea7a749a | -11.663 | -64.999603 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba8eced-d417-39b0-b7f1-854ab0f6a3b4 | -11.6647 | -65.006798 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8a37a64-a9f8-3de4-abd7-f8499bdde4ed | -11.6664 | -65.014099 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8708f52d-3a72-39f3-8862-d6eee6ee7730 | -11.668 | -65.0214 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf77f02-4adb-3add-9032-636289ed11c6 | -11.6466 | -64.972603 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 55a43b00-3907-3143-ac2e-e84552e996f9 | -11.6483 | -64.979897 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f654f2b-dd98-3cb5-a4ee-2beafa9f7687 | -11.6549 | -65.009102 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a053d646-6c88-379e-8f5a-586f764de5c7 | -11.6566 | -65.016296 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 809a42d8-92d0-34f6-8d82-3e3aa247762c | -11.6582 | -65.023598 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6c4d71-8e11-37f5-882e-814f79fe909d | -11.6369 | -64.974899 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 662edbe0-e721-38ea-9a93-5618d97d82fb | -11.6385 | -64.982201 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87dc0b4b-b28a-3cc0-949e-afeb2261973c | -11.6452 | -65.011398 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6fa261c7-9cf5-32b4-aeeb-f1037f584f8b | -11.6469 | -65.0186 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 719bd3af-cac9-3292-8f07-1ed588375e66 | -11.6271 | -64.977203 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7a55d3f-1f0d-319e-a384-86b46d719e32 | -11.6287 | -64.984497 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7f1e448-6b74-36b7-8877-3112f43ce126 | -11.6173 | -64.9795 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fbe68726-638a-3d9b-849f-ecd30a3cc019 | -11.6189 | -64.986801 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc96bfb8-5662-3171-afb5-2253efa87de0 | -11.6206 | -64.994102 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9bba2b86-0d4d-3eee-be56-786857888738 | -11.6636 | -65.182602 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c0d2f8f9-4839-34b8-948b-4bfe825e140e | -11.6653 | -65.189903 | 2024-10-03 01:50:29 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f77990b2-d1a1-3f0a-ba8a-912b71a8fcc4 | -11.5929 | -65.008301 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba3b3591-b27e-3c07-a534-51cdf968d107 | -11.6091 | -64.989098 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba85189-148c-3ea0-8330-f979d4a848c6 | -11.6108 | -64.996399 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5187736f-9f19-3446-9881-dedd4231a636 | -11.6538 | -65.184898 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4282048f-9f53-3244-8556-ca57672a8fd0 | -11.6555 | -65.1922 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1279ab63-b4e4-3154-9d8e-c6c9becad7d2 | -11.6571 | -65.199402 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54225afe-fa87-3f79-a168-fe46d7194b47 | -11.601 | -64.998703 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f082331f-3116-3524-b1e8-9cd37cff9eee | -11.6027 | -65.005997 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 097d6711-c21e-31e6-a0d0-2d450e9fa416 | -11.5912 | -65.000999 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d1f3640-6313-39be-88e2-ca538c3e0c72 | -11.5945 | -65.015602 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63606f32-da02-3e9a-bdd0-26804611e565 | -11.5847 | -65.017899 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8554516d-012b-3858-bc77-273147113168 | -11.5864 | -65.0252 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 445c271e-57e6-3a9a-86bd-25af9f259acf | -11.5749 | -65.020203 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b33fc672-0746-3441-a9f8-4292dde64217 | -11.5766 | -65.027496 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4c4f398-eae6-362f-a0a3-79e7970f54d9 | -11.6015 | -65.136299 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8d9ac49e-c0bf-3ab7-baf6-85087799e52c | -11.6031 | -65.143501 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63a3114b-d8f6-3ecf-a909-f9e7f4781cf7 | -11.6047 | -65.150803 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee87ee01-bbec-3beb-9fbe-9c35baeebc97 | -11.6113 | -65.179703 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 541a84ca-bb68-350c-88aa-c8e027b854ea | -11.613 | -65.186897 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 13f94df0-c3f0-35f9-a988-6a3df487cb6d | -11.5668 | -65.0298 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19c69596-46c9-3d35-8c5f-c7c39d82e5e3 | -11.5685 | -65.037003 | 2024-10-03 01:50:30 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65e77cd5-e9e2-380a-a921-9f1dfcf286cb | -11.5819 | -65.1409 | 2024-10-03 01:50:31 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e94a004b-9ae1-30da-bdd5-88a8c27a8823 | -11.5327 | -65.060699 | 2024-10-03 01:50:31 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87ad9885-a10f-361f-9672-9bc577e7b0db | -11.5181 | -65.087097 | 2024-10-03 01:50:31 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51b077d0-14a0-3656-993a-c7939b65e9bc | -11.5086 | -65.271896 | 2024-10-03 01:50:32 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e0ec1efe-ffe7-30ca-bc1e-f1813568309c | -11.2822 | -64.957802 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f4f3e45f-01dc-3101-b026-8be21fba7b30 | -11.289 | -64.987099 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f36a4730-d1f1-3fe6-9c47-eabe42684b99 | -11.2906 | -64.994499 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 404dc2eb-42dd-30cc-a5be-5fd519a80dcd | -11.2607 | -64.908699 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5d650a-04b4-369f-a0e4-0bdd2d237262 | -11.2623 | -64.9161 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8b8e5a5-6e92-32f2-bc04-a0678727cff4 | -11.2808 | -64.996803 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9430d5ac-8d0e-3f4f-ac1e-5e7a683332c1 | -10.376 | -61.203499 | 2024-10-03 01:50:35 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 189814f2-a0a0-33e3-9e1e-c2c99d6bd9d1 | -11.2629 | -65.008598 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee9628f-4691-396d-b952-406e71b2de50 | -11.2397 | -64.952301 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e11b5764-75db-3009-9ddb-5d9144eae5c1 | -11.2414 | -64.959602 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 135a4a87-3081-3f24-973b-5f2688e18463 | -11.2531 | -65.010902 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86b5cdf2-f60c-3d74-9a1a-69c6c5b65ec7 | -11.2548 | -65.018204 | 2024-10-03 01:50:35 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee34aec-f32a-31d1-b0c1-0f17be44e90e | -10.9758 | -63.943802 | 2024-10-03 01:50:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcde9a36-bd8d-3721-8ffb-a223c5a403a5 | -10.9777 | -63.951801 | 2024-10-03 01:50:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e760ef99-80c7-3e60-b510-91df7d1a92dd | -10.9796 | -63.959702 | 2024-10-03 01:50:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37635231-4c6a-37b6-8f0f-2e82c0c8e491 | -11.28 | -65.264503 | 2024-10-03 01:50:36 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d768090-b8c7-3260-b814-3e0d94a70406 | -10.9064 | -63.8671 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e36aa7e-2689-3cd0-800f-c605cba45d39 | -10.9082 | -63.875198 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c8cf7450-d8ac-33b9-92ba-8cad91f1dd55 | -10.8985 | -63.877499 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 59361abf-aa8d-341d-9719-abf2b756c1fd | -10.6353 | -62.8013 | 2024-10-03 01:50:37 | METOP-B | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 898f24b9-cbb8-3bfe-94ad-1bdb5cda0a0f | -10.8869 | -63.8717 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 497798de-fe63-3c06-bfcc-55e2dfccfe2e | -10.8887 | -63.879799 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a2338f5d-f7b8-3499-bce5-40c3bf015eff | -10.8906 | -63.887901 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d03d8771-1295-35e8-a15a-3f2c50e80f00 | -10.8925 | -63.895901 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e74cc987-6c8d-3f1e-8a78-785035e3b69b | -10.8789 | -63.882099 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 55c50504-1f6b-3bcb-a489-f9d3cc3e48d7 | -10.8808 | -63.890202 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 684c97d3-7736-38a1-8581-9be77838277a | -10.8827 | -63.898201 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca529dcc-80da-3480-8b44-b254e79f7966 | -10.8673 | -63.8764 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a0d7f7b-84f8-37dd-b9a0-d92d91396377 | -10.8691 | -63.884499 | 2024-10-03 01:50:37 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f21bf4a-d994-3d1d-a457-d504ea90b05c | -10.8537 | -63.862598 | 2024-10-03 01:50:38 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c8fa695a-d0b0-39af-9407-ce4271834b9b | -10.8556 | -63.870701 | 2024-10-03 01:50:38 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b514aab-005d-3b49-8b1a-b4313a781653 | -10.8575 | -63.878799 | 2024-10-03 01:50:38 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README41.md)
