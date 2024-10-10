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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5253328d-59b3-37c7-940e-ab443d748bd4 | -11.5282 | -53.846802 | 2024-10-10 01:05:14 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47c925d9-4515-36bf-bd09-577f7c8e495b | -12.2886 | -57.7187 | 2024-10-10 01:05:15 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85090bfb-7e0c-3214-9b8c-f48a42afe361 | -12.2903 | -57.7267 | 2024-10-10 01:05:15 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4e5f4a17-c889-3e25-9555-8bb3c7a9373f | -11.6017 | -54.672699 | 2024-10-10 01:05:16 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf3058b-ecda-37de-a2f3-1a69cf71d93f | -11.6033 | -54.679699 | 2024-10-10 01:05:16 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc7bf52c-b094-30e6-b1fc-34418c7bae80 | -11.5935 | -54.6819 | 2024-10-10 01:05:16 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1c4b588-cc03-3d42-8570-f59789c1ea02 | -11.2469 | -53.293999 | 2024-10-10 01:05:16 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cae96df-15b1-3667-a734-3270a9361d4f | -11.2302 | -53.2663 | 2024-10-10 01:05:16 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b363ccaf-4f41-3cf6-ad61-64129c5a06c4 | -11.8868 | -56.189899 | 2024-10-10 01:05:16 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 016873f2-2055-3013-85a2-0246b8f8034c | -11.8883 | -56.196999 | 2024-10-10 01:05:16 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a49b4c92-7de1-3576-868e-f1e63ad460d1 | -11.8899 | -56.204102 | 2024-10-10 01:05:16 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6be344dc-b22d-398b-89c1-b66c2bfadb94 | -10.6683 | -51.0877 | 2024-10-10 01:05:17 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 525787ce-dae8-3693-b7f6-593345e8b66d | -10.6706 | -51.097198 | 2024-10-10 01:05:17 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dd34dd5f-f622-35a3-a02b-5a270cad6c05 | -10.6585 | -51.090099 | 2024-10-10 01:05:17 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4d8ddf0-376f-3903-a76f-1012ab3707ad | -11.921 | -56.913502 | 2024-10-10 01:05:18 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0f054b7-5909-3bed-a7df-8b94cffa46e3 | -11.9226 | -56.920898 | 2024-10-10 01:05:18 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3b47eb-be91-33d5-b5b9-677fe27515e6 | -11.929 | -56.950699 | 2024-10-10 01:05:18 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4e8a6f7-2adf-3523-b8b0-b78cbc0b9829 | -11.9306 | -56.958099 | 2024-10-10 01:05:18 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3997272e-6921-3224-b0f5-cdbb1f0582d0 | -11.9096 | -56.908298 | 2024-10-10 01:05:19 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd06f95-6137-3c09-b563-48fbcd7cde6f | -9.9947 | -48.817799 | 2024-10-10 01:05:19 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc4f1419-6bf1-36ce-a515-4a275644b264 | -9.998 | -48.831402 | 2024-10-10 01:05:19 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e771227a-8869-3446-8c73-149ed893757f | -10.0014 | -48.844898 | 2024-10-10 01:05:19 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08930a26-f336-32b3-a44f-6abff3805fc0 | -11.231 | -54.172298 | 2024-10-10 01:05:20 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bb6c594-5344-3d93-bd89-561cb26f0e56 | -10.4087 | -50.692402 | 2024-10-10 01:05:20 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f6953f85-c063-3c94-8b23-db72f792adda | -10.4111 | -50.702599 | 2024-10-10 01:05:20 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83c45b5f-81d2-31c0-a032-dc1ee8bd7899 | -12.3048 | -59.160198 | 2024-10-10 01:05:20 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce9bfd1a-4225-3405-817f-1a730263946e | -11.2895 | -54.5676 | 2024-10-10 01:05:20 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20edf9e6-ccb2-3d5c-a29f-bb1635c1da34 | -11.2797 | -54.569801 | 2024-10-10 01:05:20 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b815950-4c24-3dc2-90a8-ce01b4751e4f | -11.1284 | -53.993 | 2024-10-10 01:05:21 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f93ae13b-ff90-3836-9475-60af7106abee | -11.13 | -54.000198 | 2024-10-10 01:05:21 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b0f10ff8-40d8-363c-a577-143f4286a757 | -11.1317 | -54.007401 | 2024-10-10 01:05:21 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e73c5cb-ff4e-3ee7-a3ee-4ffa04c770b0 | -11.1333 | -54.0145 | 2024-10-10 01:05:21 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23ae746d-ab01-30f1-9f87-19029ebd8aea | -10.0571 | -49.535999 | 2024-10-10 01:05:21 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b01413c-3140-3eac-be39-cb6c91a63877 | -11.2246 | -54.737202 | 2024-10-10 01:05:22 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f8e2770-27cc-3def-8924-45cd64498b99 | -11.11 | -54.2752 | 2024-10-10 01:05:22 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f27060c0-ac98-3039-86e6-637b6e8b300d | -11.1116 | -54.2822 | 2024-10-10 01:05:22 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0deabf5d-33f6-3f6e-9733-c29161b2c8ed | -11.3546 | -55.410198 | 2024-10-10 01:05:22 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 926d3108-a256-3a0a-bfe7-15a79151b04b | -11.3561 | -55.417099 | 2024-10-10 01:05:22 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de5aaa14-4f5c-3b41-a29c-c3cd3f6164f1 | -11.1756 | -54.748501 | 2024-10-10 01:05:23 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb697ed1-e3d6-3e7a-9945-db7f8f368238 | -11.1772 | -54.755501 | 2024-10-10 01:05:23 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac9eeb82-7983-30bf-b913-7987b2f486a1 | -11.169 | -54.764702 | 2024-10-10 01:05:23 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc3a2e8a-ba4f-39d7-811d-c8a2e53aec14 | -11.1706 | -54.771702 | 2024-10-10 01:05:23 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96a66e65-4c71-3b51-af75-ec919eb11c78 | -11.1925 | -54.8694 | 2024-10-10 01:05:23 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e337916-7f0c-3ed8-b41a-a0d7252c527a | -11.1576 | -54.759998 | 2024-10-10 01:05:23 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 270aa3c5-b48d-373d-b2f3-3d999c19c114 | -11.1592 | -54.766998 | 2024-10-10 01:05:23 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95e83133-4e69-3055-ab94-7fb262e0713b | -10.6993 | -53.0224 | 2024-10-10 01:05:24 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84c8db5e-1144-3290-be50-1ccabf7b4637 | -10.6877 | -53.016998 | 2024-10-10 01:05:24 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46840b24-418d-30d3-b70d-070d8c6c45bc | -10.6895 | -53.0247 | 2024-10-10 01:05:24 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 752de4ba-b57f-3559-9110-a4af7773c556 | -10.6913 | -53.032398 | 2024-10-10 01:05:24 | METOP-B | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91696f6f-2785-3745-90da-354aa2a3bfa3 | -3.3341 | -53.232 | 2024-10-10 01:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 77d2affa-8ec0-3020-9557-5c57f9ebb626 | -3.3342 | -53.2117 | 2024-10-10 01:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| aa562545-849c-3347-bb4f-dac8bc0b7ce7 | -9.9492 | -50.070099 | 2024-10-10 01:05:25 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12203123-e249-323b-ae82-64978f47f99d | -11.4826 | -56.7868 | 2024-10-10 01:05:25 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b38cf74-beda-346a-99eb-25b6513e6e70 | -9.6193 | -48.9692 | 2024-10-10 01:05:26 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23d757f2-c834-3b5b-8ec7-a4ea4f88f1af | -9.6226 | -48.982601 | 2024-10-10 01:05:26 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bfffd026-9159-3867-b872-ee6ee5a7fa1b | -9.6096 | -48.9716 | 2024-10-10 01:05:26 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a25a527a-4b71-39eb-8822-2046a795dce2 | -9.6129 | -48.985001 | 2024-10-10 01:05:26 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc65e517-2166-31ce-b700-35d47c8d5c25 | -3.7061 | -44.9555 | 2024-10-10 01:05:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 309fe685-ed91-35d6-b5ef-f39d5c7d6e7c | -3.7247 | -44.9547 | 2024-10-10 01:05:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9ac5205c-8a22-3dc7-9581-ed32a70f4e55 | -9.5575 | -48.927399 | 2024-10-10 01:05:27 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56417f0b-0232-3ce8-952b-e0aa6bac6d03 | -9.5608 | -48.940899 | 2024-10-10 01:05:27 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4287993d-b15d-39da-8fc2-275cc840a58c | -11.8155 | -58.824501 | 2024-10-10 01:05:27 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 328a8f24-bf24-3f83-a029-910d243a9781 | -11.8174 | -58.833401 | 2024-10-10 01:05:27 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba983ee5-4408-363e-bd96-b9eba7790d74 | -11.8057 | -58.826599 | 2024-10-10 01:05:27 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f566682-b447-334a-b984-05ce2a50c418 | -11.8076 | -58.835499 | 2024-10-10 01:05:27 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8b02fd30-ffb1-3eab-91b5-66a66c398b02 | -10.6388 | -53.655602 | 2024-10-10 01:05:27 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0dd82050-0bda-3d10-99c7-50e755c409d4 | -10.6405 | -53.662899 | 2024-10-10 01:05:27 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8fff02d-2987-3e99-9c67-abc6f76ad68e | -3.7961 | -45.4927 | 2024-10-10 01:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 84db6a3e-22a2-3058-8872-08e26a389dd6 | -3.8146 | -45.5143 | 2024-10-10 01:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3d3c0ef7-fea3-361d-a633-7558f9e25f2d | -3.8147 | -45.4918 | 2024-10-10 01:05:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 16f48982-bf9b-36f6-a021-94c1ea708edc | -10.629 | -53.657902 | 2024-10-10 01:05:28 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdc9cd98-b494-3fcc-a4ca-18ffe0fe282e | -10.6307 | -53.665199 | 2024-10-10 01:05:28 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7fda50-4744-3424-b97e-71dd82ab0c7a | -11.8921 | -59.4366 | 2024-10-10 01:05:28 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d8f724e2-8e0b-30b7-a511-2d9a5d9fbf9c | -10.6209 | -53.6675 | 2024-10-10 01:05:28 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa5af58-25ad-3c21-9264-31d380dbb452 | -10.6226 | -53.6749 | 2024-10-10 01:05:28 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e72b2f84-24c7-3d0a-b8d8-7e6ed33e8b82 | -10.6111 | -53.6698 | 2024-10-10 01:05:28 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 227a3e61-2594-30cb-812a-f0363d0d02b6 | -10.6128 | -53.6772 | 2024-10-10 01:05:28 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74bdc3ec-879b-31d8-941b-9aaa6484be55 | -9.7614 | -50.104301 | 2024-10-10 01:05:28 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bec6b503-8287-32f8-a4be-52f9aa9576b2 | -4.0814 | -51.0292 | 2024-10-10 01:05:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 7881674b-6477-37a0-a691-e69a321337df | -4.0961 | -48.2739 | 2024-10-10 01:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 9eab4396-1387-38d6-bf00-f0982b3d496e | -4.0962 | -48.2523 | 2024-10-10 01:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| ca84d7c9-68f2-3387-9b1a-c51e94cfeb6a | -4.0998 | -51.0285 | 2024-10-10 01:05:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 020eccdc-e0a6-308d-94f2-ff7ff54dd9ba | -4.1146 | -48.2731 | 2024-10-10 01:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 217.8 |
| cef4ce7c-5cd0-3074-a7e8-a196a7b107c1 | -4.1148 | -48.2515 | 2024-10-10 01:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 66ae221c-f2b0-3204-be64-a6c8b2f3359b | -11.3585 | -57.256901 | 2024-10-10 01:05:29 | METOP-B | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2b81549-587d-3557-9858-6afbb25a159d | -9.3548 | -48.773899 | 2024-10-10 01:05:29 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63e12619-98f1-3745-8415-260c9314523d | -9.3582 | -48.787899 | 2024-10-10 01:05:29 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b03c4706-8db4-3340-9c68-d12ae32fd6d2 | -9.3616 | -48.8018 | 2024-10-10 01:05:29 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cfca703-5447-3331-9c79-f05503128062 | -11.6625 | -58.8759 | 2024-10-10 01:05:29 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ae5c8c4-a1cf-3c0c-a5c9-e1db38af6802 | -9.3485 | -48.790298 | 2024-10-10 01:05:30 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e16904f-2de0-3c04-939b-164397b186a2 | -10.6239 | -54.223 | 2024-10-10 01:05:30 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef19355b-9143-38ea-845b-63098597ff30 | -10.6141 | -54.2253 | 2024-10-10 01:05:30 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2791d1bc-f2e2-3acf-b887-6947f6483c39 | -10.449 | -53.637699 | 2024-10-10 01:05:30 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4d768d-7704-3d39-b5a0-d7c3285a93c2 | -10.4507 | -53.6451 | 2024-10-10 01:05:30 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c845605-54cc-34c1-9565-6e31c82c169f | -8.9807 | -47.720001 | 2024-10-10 01:05:31 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b09c998-0b5b-3339-847a-3155fc2f5548 | -4.4776 | -46.5956 | 2024-10-10 01:05:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 6c6052b3-e041-3b7d-bacd-8ee27d481455 | -11.1545 | -57.1684 | 2024-10-10 01:05:32 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af7fc09c-2799-3586-8436-c6dffd09f976 | -11.1561 | -57.1759 | 2024-10-10 01:05:32 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be213eef-cf79-3658-a675-617926527654 | -10.3321 | -53.757999 | 2024-10-10 01:05:33 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d298d59-6dec-3c13-8fc4-4981c24e7e9d | -10.3071 | -53.694099 | 2024-10-10 01:05:33 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README21.md)
