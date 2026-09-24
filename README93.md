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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d36b3687-244b-3303-b94e-a9c84229a18e | -9.5735 | -46.5337 | 2026-09-24 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7a7f3312-2289-384d-8de7-f104fe8f155f | -6.6816 | -55.0502 | 2026-09-24 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 48d62ed6-7ed6-3f8d-b6fc-025df1482964 | -9.6111 | -43.9243 | 2026-09-24 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 145.6 |
| 7bda396e-2f84-3528-afee-a2eef928e7b3 | -11.3054 | -44.0198 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 7c2257f9-b6fd-3614-9151-dbd798e6a501 | -11.3246 | -44.0169 | 2026-09-24 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 12e1e07f-69fe-3df6-9843-be7b2faef63e | -8.9019 | -45.9104 | 2026-09-24 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 20f9f1c0-fdac-37dc-ad30-c6bebca41ae6 | -11.1545 | -42.8124 | 2026-09-24 13:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 93.4 |
| efd95e63-0801-3fef-853f-5949ba143cf5 | -8.0921 | -44.3538 | 2026-09-24 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 654cd0c5-ec7b-322e-ba62-668ce57f1158 | -10.0917 | -46.0458 | 2026-09-24 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 33f54dc2-78b4-3333-805e-cdf29b2897d6 | -13.7993 | -54.0617 | 2026-09-24 13:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ab0fd0b0-2b15-38dd-ad36-c803cf12ffa4 | -11.1733 | -42.8335 | 2026-09-24 13:30:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 44cc8219-e2cc-35da-a738-f20e0a9cf8b9 | -9.6302 | -43.9219 | 2026-09-24 13:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 275.9 |
| e417ff86-e01c-347d-bb22-b891ce093ced | -6.6815 | -55.0703 | 2026-09-24 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 449edf1c-6ead-36fc-a195-348c8f903f9a | -6.6816 | -55.0502 | 2026-09-24 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f57c003b-5ea6-3440-a4ad-c71a00c04bd6 | -3.9169 | -59.6641 | 2026-09-24 13:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9fb39acd-9281-384f-b0e5-b7bfaa143b83 | -8.4307 | -47.4515 | 2026-09-24 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 65091248-d817-3aa8-a920-a761f15ee8b9 | -9.5735 | -46.5337 | 2026-09-24 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 7500240b-50ca-349a-889a-bff28d111d6c | -11.9906 | -52.4695 | 2026-09-24 13:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5bcad312-0a08-3f21-bba4-96f50fd0d4e7 | -12.929 | -50.9219 | 2026-09-24 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| bc5df7d3-dd09-34d4-b567-5d1a983ec016 | -11.1733 | -42.8335 | 2026-09-24 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 76fbdc48-82b0-3737-a62c-4a62104c379e | -9.2793 | -45.9369 | 2026-09-24 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 59649017-a425-3e9c-abf7-b871f2f501bf | -11.1358 | -42.7914 | 2026-09-24 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 8bd6f3ae-ff55-3f0d-955d-c7ffb03ac200 | -8.3573 | -47.3041 | 2026-09-24 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b4feac2b-1ffc-3978-afe1-b1f00c6f03d3 | -5.5756 | -42.3157 | 2026-09-24 13:40:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 88879092-eaae-3358-a7e4-c840c8c7de08 | -5.6016 | -60.1919 | 2026-09-24 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| eb0d9c4d-17ea-3228-ad6b-e755dde2abb9 | -8.3761 | -47.3023 | 2026-09-24 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 173.0 |
| aec2296d-bd2f-3ef5-b74c-275ecf192b3a | -9.6111 | -43.9243 | 2026-09-24 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 05abdbcb-46da-3422-9791-8dbb2938cbc1 | -13.168 | -51.5324 | 2026-09-24 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| fc9e49e6-e938-32fa-a84c-21d28f54ad04 | -9.6302 | -43.9219 | 2026-09-24 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 185.9 |
| b4df4b24-0c51-3af7-ba09-cb7064738947 | -13.1677 | -51.5537 | 2026-09-24 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 24db25a1-ecc9-3961-97e7-61bb11415df2 | -8.9019 | -45.9104 | 2026-09-24 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4e854fbe-4981-3357-bf21-2eee787f42c8 | -6.185 | -43.3491 | 2026-09-24 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| db07b346-4b54-3291-b506-235cf6a0d2e7 | -8.3764 | -47.2802 | 2026-09-24 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 67456ed6-d031-3be7-84be-58dc4dd03f95 | -6.6631 | -55.0512 | 2026-09-24 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 85a18a97-7a1c-34c9-86df-dcc82da728e1 | -11.1545 | -42.8124 | 2026-09-24 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 5083064f-0c3b-32a4-bd83-78a1090a093b | -13.1872 | -51.53 | 2026-09-24 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 3ea5f5de-a0ae-385e-a6f1-e9df9014ef07 | -11.155 | -42.7885 | 2026-09-24 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 6255ead3-69dc-356e-9bb8-b7d6546327e2 | -8.0921 | -44.3538 | 2026-09-24 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 5490c922-eca7-3352-8660-7dbdf2f86736 | -8.5989 | -44.5531 | 2026-09-24 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| fa34ff8a-b4b0-3e7f-979b-82b7a14fc1ea | -11.2783 | -43.388 | 2026-09-24 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8c80966e-fcc4-3f33-bba2-0f982b499929 | -6.6631 | -55.0512 | 2026-09-24 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 74512484-32ea-3242-942d-490cb4a71294 | -11.325 | -43.9934 | 2026-09-24 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| d315e1d2-7305-382f-a4f0-f828e881a74c | -5.5756 | -42.3157 | 2026-09-24 13:50:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| c26ec4ce-9aee-3d4e-80b1-9de7809f6757 | -9.6111 | -43.9243 | 2026-09-24 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 26109b76-cf5b-3f6a-89c5-7294ea44b08c | -5.6016 | -60.1919 | 2026-09-24 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c5c16e1c-0373-3ca3-8304-97e544db4e1a | -8.0921 | -44.3538 | 2026-09-24 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8a41b708-fe6d-3359-9a5e-88dd6db451a9 | -11.3813 | -44.0554 | 2026-09-24 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| b3a379bc-9df0-3894-bfa5-0aba5f982ec0 | -11.1733 | -42.8335 | 2026-09-24 13:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 13b596ec-e2a3-3437-be44-ed1d7d1fec58 | -11.3246 | -44.0169 | 2026-09-24 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 6741cbdf-4e6e-3bf6-8963-b5aa172cfe29 | -11.2858 | -44.0461 | 2026-09-24 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| b404f170-ee19-37fe-95bd-2170b8ff8494 | -8.2529 | -48.2128 | 2026-09-24 13:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 979ac6e2-b123-3301-b2cb-020a6ba03f07 | -9.2793 | -45.9369 | 2026-09-24 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| bab7e6a2-7bc2-36f5-929b-74f377de05db | -6.1653 | -47.5052 | 2026-09-24 13:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| ac0012f1-8114-3b85-bed7-ced14fbebe6d | -8.7919 | -44.2546 | 2026-09-24 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| fc9acbf3-92ee-3b17-806a-0151f3e3c0b4 | -11.9906 | -52.4695 | 2026-09-24 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 80a55d11-9f7e-3a19-98ce-bdce678fadb2 | -8.7916 | -44.2778 | 2026-09-24 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7872c6b0-2936-3395-a143-e76849599f78 | -11.2862 | -44.0226 | 2026-09-24 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| e4b80b2a-be65-3efa-9b54-65e96ab317fe | -11.6404 | -43.4981 | 2026-09-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 287.7 |
| 0615a500-cff7-3a1d-992a-5a188f8b1a01 | -6.9686 | -47.468 | 2026-09-24 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d6b0859e-7703-39b8-9971-4fa91953ecfb | -13.7993 | -54.0617 | 2026-09-24 13:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 80a858f7-f0ec-31a1-b904-5bd7e23d76ef | -5.195 | -42.9571 | 2026-09-24 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 78.9 |
| cbee60e1-81a7-33ae-90a7-115667bce1b2 | -8.3022 | -44.1467 | 2026-09-24 13:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 5b299251-e670-3d00-84e3-20217b83eb41 | -12.9098 | -50.9243 | 2026-09-24 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4d50e18d-be50-3e04-ac7a-47e817633557 | -5.1948 | -42.9805 | 2026-09-24 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 73.8 |
| db9e6db8-9fa2-37fc-8e56-10e6b3921a3e | -13.1872 | -51.53 | 2026-09-24 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| d9a25b22-c1d1-35c1-aab9-7ee83a42eb70 | -4.5323 | -44.0219 | 2026-09-24 13:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| dcb00696-fcb8-38ae-a2e7-746324b5d829 | -13.168 | -51.5324 | 2026-09-24 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 7580bcbf-c5f6-3193-bd35-e6675eafb0f1 | -13.2057 | -51.5703 | 2026-09-24 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b7cd5d3d-1773-367d-b897-70762de55c83 | -11.6408 | -43.4744 | 2026-09-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| fadfb1ce-bea1-3933-baf7-356ed391684b | -8.7003 | -45.4567 | 2026-09-24 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 7aa54415-e756-3133-967d-c25e232c77b9 | -3.9169 | -59.6641 | 2026-09-24 13:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| d3d81cfe-7b54-343e-8e0d-b040b5857b06 | -8.4307 | -47.4515 | 2026-09-24 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 25dc2bdb-fc5f-3b2d-a083-c8c3d9c30a3f | -8.5989 | -44.5531 | 2026-09-24 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| a94fae44-6dd8-3653-97cc-8413415c9f40 | -6.6816 | -55.0502 | 2026-09-24 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 119dc74b-eb38-31fe-aa0c-7aee3630f337 | -11.305 | -44.0432 | 2026-09-24 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 313.5 |
| bc094a1d-c731-348e-b37f-779bd987dcea | -12.0096 | -52.4675 | 2026-09-24 13:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 18be3bb4-5770-3926-9eb2-82714d82de51 | -13.2249 | -51.5679 | 2026-09-24 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 3619b67f-88db-321a-806c-1f9a8ca4530b | -9.2796 | -45.9143 | 2026-09-24 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f21a614e-41dc-3ecb-92a2-5ffabbee6283 | -8.7898 | -45.8321 | 2026-09-24 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 486325c3-26b9-335e-9df6-f5417faf0c1a | -12.929 | -50.9219 | 2026-09-24 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d17f15a6-8921-3dbe-a95c-93a05bbc8204 | -6.9683 | -47.4899 | 2026-09-24 13:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1181bcce-49ea-3c2b-b1b0-c5378b83e7eb | -6.6815 | -55.0703 | 2026-09-24 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 94107fb9-e0d1-3c8e-a578-a8f7b02c5519 | -8.7729 | -44.2568 | 2026-09-24 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f4968c08-9a2c-3daa-a484-e80efed3f9a6 | -8.7709 | -45.8341 | 2026-09-24 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| a88410ff-2852-3b01-aa67-78bf084a64f2 | -8.3761 | -47.3023 | 2026-09-24 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 95e8f2e6-2c80-3961-9ad6-3c11322f5597 | -8.754 | -44.2589 | 2026-09-24 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 884a7a5f-9680-33fd-850e-9c498cebd672 | -12.0096 | -52.4675 | 2026-09-24 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f12dd4a0-0810-38d6-b9d8-6eee9a977d39 | -9.5735 | -46.5337 | 2026-09-24 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| ada6ce1c-e739-3195-81f0-a2b1ac5951a5 | -11.3976 | -44.2167 | 2026-09-24 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 23e7d7ab-dc8d-3855-aeb4-9d30a3c9c2c1 | -9.0087 | -44.9897 | 2026-09-24 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8f0c9b5d-8eb6-3876-9239-4f68a0393115 | -7.6765 | -46.0771 | 2026-09-24 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| de3557cc-2c4e-3ceb-909b-4dce38181cd8 | -11.9906 | -52.4695 | 2026-09-24 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 24ff88b5-6dd6-3678-9a6d-f418577688f8 | -6.6631 | -55.0512 | 2026-09-24 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c66c96cf-3d1f-376b-b7c3-7bae373f2704 | -7.1014 | -42.0849 | 2026-09-24 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 998a3765-dc5b-3cd3-a94f-4c068d0b7e9b | -8.8914 | -62.5436 | 2026-09-24 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4ba88db4-3e40-36e5-95f0-c383c9d17c25 | -6.6816 | -55.0502 | 2026-09-24 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| bf21a1e1-e94b-3679-a667-25068e06b146 | -6.9683 | -47.4899 | 2026-09-24 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 02c6065c-7197-3acd-a149-5614d274d109 | -7.1088 | -43.0792 | 2026-09-24 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| 4baef926-2ed1-3341-8cf9-0117481391b4 | -11.3547 | -43.4001 | 2026-09-24 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1e26f66c-64a2-3b58-89bd-c7ea85b9ba49 | -9.6111 | -43.9243 | 2026-09-24 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 175.9 |


[Clique aqui para ver as próximas entradas](README94.md)
