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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 468efbe0-33f0-3284-b933-d65ce6c343e8 | -16.54186 | -55.09339 | 2025-09-04 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 27d49ebf-c190-3f51-9aa3-664abd2e30e9 | -15.6093 | -52.88911 | 2025-09-04 01:26:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 30.9 |
| c67dd1f2-7fd0-3ffe-b79c-ddadc7510757 | -22.23023 | -55.98033 | 2025-09-04 01:26:00 | TERRA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d0fa4512-2cda-332c-b518-6ba849897a9e | -12.88919 | -56.94788 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2b793e8c-b6a2-3c97-8265-285d1e61158c | -12.96989 | -54.79385 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| b5828b16-34e2-3e10-a29b-7166bc7d7116 | -11.65775 | -54.51785 | 2025-09-04 01:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 5f7aac6a-38a3-31ea-9888-90cb2e3a66b6 | -12.97937 | -54.77023 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 2cb9c3ef-b594-3e96-98ba-bb3997ad3135 | -10.6103 | -55.40724 | 2025-09-04 01:28:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8b64f1b0-9348-3aed-a898-27ea28e8b51d | -11.87974 | -51.54726 | 2025-09-04 01:28:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 36d072ce-5812-3eff-969d-ec74adeae04c | -12.98041 | -54.7861 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b993161a-985b-3831-8746-b8c44acca2a6 | -12.97677 | -54.76495 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 2f09eab8-5117-3ce7-b040-c8b68e9294c7 | -11.67409 | -57.34602 | 2025-09-04 01:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 57ebe55b-cc17-3f14-96fd-88618a2c4066 | -9.4988 | -57.82266 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 17822bad-d8ae-3e01-a496-d31b5e119281 | -11.58724 | -52.12235 | 2025-09-04 01:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 2ad65c5e-4aed-36d8-af76-d2afd0581728 | -14.98654 | -59.38854 | 2025-09-04 01:28:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5f843317-c4b4-3e39-908d-6b7d1df4b7ec | -11.67633 | -57.36017 | 2025-09-04 01:28:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| b14c5876-c083-3fa4-9a19-c5b9153b240f | -11.5747 | -52.09288 | 2025-09-04 01:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 8fdd019f-7186-35a3-88ae-4a607cece19a | -11.88264 | -51.54137 | 2025-09-04 01:28:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| bd2c3930-c739-369a-a69c-7c6e63521948 | -12.89258 | -56.95558 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 36182fd5-c676-3c92-8ebc-aa33e8ddd0d1 | -13.10218 | -57.11164 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 7eb57075-d334-3925-a152-04916d423922 | -12.9664 | -54.77274 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| fa119190-a5a4-35c8-b726-1890be49c29a | -11.65102 | -54.525 | 2025-09-04 01:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1db1d77f-8b7c-3e88-9775-98040db26b36 | -11.66172 | -54.54111 | 2025-09-04 01:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 81233fcd-193a-375b-af03-96bd3a5f5b55 | -13.1044 | -57.12549 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fb03f9d4-7ef1-3acf-a989-27a5fb6e328e | -11.58101 | -52.12874 | 2025-09-04 01:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| f299b309-7446-3897-b306-b800a56d0f49 | -11.65481 | -54.54817 | 2025-09-04 01:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 1ce27aee-8a3a-314e-ade5-793c4bcbdb6a | -13.09965 | -57.11853 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e1e8bb46-d0cd-3d19-bc32-0be70dce7e5e | -12.88698 | -56.9335 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3b5a8918-c84f-32e3-b9c5-30225add8c59 | -12.91226 | -56.93767 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 9c2853e6-57c5-36f0-b626-f0227f7c942c | -12.90127 | -56.93948 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| d518e4f7-4f37-320b-987a-f371665b2025 | -12.64542 | -57.00091 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d8b3f52f-2e7e-32fa-8652-1eb943fb33f1 | -12.91269 | -57.01092 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 2fb7c662-71e6-3611-9c6b-2a12c6bf56d3 | -12.90357 | -56.95382 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 319eec7c-17d1-3631-a1f7-0825dbc713a5 | -12.89027 | -56.94119 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5e222f27-adda-338a-baed-29429cd26657 | -10.61226 | -55.41356 | 2025-09-04 01:28:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e71b3f4f-bdcb-3fc2-81fe-68667af18945 | -12.98285 | -54.79139 | 2025-09-04 01:28:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 088484db-1c04-3bdd-ba09-52e106eb778a | -20.0979 | -50.0105 | 2025-09-04 01:30:00 | GOES-19 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| 1cbafeb4-c49e-30bc-a853-1598265f4e36 | -12.9006 | -56.9488 | 2025-09-04 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 5d397831-890a-3efb-a6c4-a5da737b3881 | -11.0572 | -45.123 | 2025-09-04 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0044cb4a-1c4c-3d74-8739-241bbe638423 | -5.6081 | -45.0038 | 2025-09-04 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d9f47fc3-5232-3542-8980-21e3ac30a0ec | -10.4283 | -50.3732 | 2025-09-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 331fa901-c86a-3638-ac83-c0e417a989d2 | -11.0377 | -45.1487 | 2025-09-04 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| ec16061d-843e-303a-aa41-9ed2e1ed4cc6 | -6.7649 | -63.1292 | 2025-09-04 01:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 222.9 |
| 06529785-79b9-396c-aa49-c281cd6eba39 | -11.6647 | -57.3533 | 2025-09-04 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| aafe7132-0e65-3cb6-a1e2-881755d1a21b | -11.6836 | -57.3518 | 2025-09-04 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 45f17478-9c32-31cd-a25d-0b8b3e9124f9 | -6.7833 | -63.1286 | 2025-09-04 01:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 9bac2616-be42-350c-828f-91d9a94ee6e6 | -11.6599 | -54.5297 | 2025-09-04 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| face4e4b-5750-3aa0-887a-e241395c95ee | -6.7782 | -44.0876 | 2025-09-04 01:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6aa735f9-60fd-347e-88ad-79714f99246a | -5.6079 | -45.0265 | 2025-09-04 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 1399a450-e445-3c2a-bbcf-9f447eb524eb | -10.4472 | -50.3713 | 2025-09-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 2499a5ef-dfed-3e2b-91bf-2a5d578eac7a | -10.4469 | -50.3926 | 2025-09-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 1b211651-3af3-3df6-8b77-fc562c910757 | -4.9951 | -56.256 | 2025-09-04 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2091daa4-b9a6-3afc-bf85-cec6bc76a692 | -10.428 | -50.3946 | 2025-09-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |
| aea92fd3-48b7-343c-af60-d20e2f45475e | -6.7465 | -63.1297 | 2025-09-04 01:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 37738ce8-9f3c-3316-a103-2133dd01f622 | -6.797 | -44.0859 | 2025-09-04 01:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| e424d1e8-522d-348f-be85-a00df598bf1b | -6.7648 | -63.1479 | 2025-09-04 01:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 842b38fb-c0cb-3ad6-a19e-7872e1275c2b | -12.8818 | -56.9304 | 2025-09-04 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 420b0680-3a1a-31d5-ae1a-ff008643e894 | -11.5969 | -52.113 | 2025-09-04 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| a2df4ebf-d2b2-38fe-867a-964703263a1f | -5.5892 | -45.0278 | 2025-09-04 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 142f677b-f3c0-32ea-8fdc-f216c1b8d320 | -2.9619 | -49.365 | 2025-09-04 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| c661e4c7-9d98-3347-ac84-b9fbc30193f2 | -11.0568 | -45.146 | 2025-09-04 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 95de8aa8-e606-3d54-aac8-0cc732bc4af9 | -2.962 | -49.3437 | 2025-09-04 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4b312efb-b521-3e9d-8965-ff6f06292793 | -11.5779 | -52.115 | 2025-09-04 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| fa637df5-1316-30de-be07-e75570423fcf | -12.8816 | -56.9505 | 2025-09-04 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 501a68b3-27e0-366a-9ebb-5ffe0975c6f8 | -12.9009 | -56.9287 | 2025-09-04 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| bde56a8b-817e-3da7-bddd-0e7eb2489c7d | -8.6619 | -68.74633 | 2025-09-04 01:30:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 1bc6196a-18c2-3b5b-9da2-4e9910009512 | -10.1504 | -68.53784 | 2025-09-04 01:30:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 21f60069-3398-32c8-947e-92b7ef26bf1b | -6.7568 | -63.12704 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 9180df4c-de21-37c1-857e-9badfa5fdf0d | -6.76685 | -63.13463 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 21982fe3-47a8-31f9-b937-c72db0f2e73d | -6.77689 | -63.14222 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 58eab495-5b60-35f7-9aa3-ce429dcdefa4 | -6.78709 | -63.13437 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 828297bd-f78b-354d-bb93-57f57aa9ab8e | -8.66428 | -68.76557 | 2025-09-04 01:30:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 6f7631d7-0f18-37e6-b200-7797f1c86858 | -7.4536 | -63.16016 | 2025-09-04 01:30:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a8e6574c-30af-3eeb-aee3-00191115c663 | -6.76562 | -63.1258 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a6f6ebee-bf8f-31b9-9abd-ef80f6802ba4 | -6.75803 | -63.13588 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 8dde98b9-3e92-31d8-b0ef-a7e420760aa9 | -6.77567 | -63.13338 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| a396138e-169b-3ad9-94e1-3e2f7ac1564b | -6.78831 | -63.1432 | 2025-09-04 01:30:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a6a209a8-f6cd-32f7-a2a0-fe652ab8a15f | -3.4292 | -59.57487 | 2025-09-04 01:32:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 38a94347-2082-3478-87c3-7ddc0d895cf8 | -4.99514 | -56.26955 | 2025-09-04 01:32:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d698bbb9-4618-3408-831e-f72cddd01a1c | -4.99186 | -56.24795 | 2025-09-04 01:32:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 0d60b228-0209-306b-b7f4-7299d800d7ca | -11.0572 | -45.123 | 2025-09-04 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c519f8bf-f46d-3a25-9a83-7ec31a518b8a | -11.0377 | -45.1487 | 2025-09-04 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b4ba447e-3783-3845-805c-bd539d5c6b31 | -2.962 | -49.3437 | 2025-09-04 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 466a760a-67ed-30da-b0ba-e81158dac9cf | -5.6079 | -45.0265 | 2025-09-04 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 39248880-47dd-3dbb-aa89-a1a502603989 | -10.6122 | -55.413 | 2025-09-04 01:40:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| dd329662-92bc-3e58-b771-b662aed725d6 | -5.871 | -57.7715 | 2025-09-04 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| b8510939-20c2-3e26-815a-d0d05b512769 | -10.428 | -50.3946 | 2025-09-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 610032e9-3cfc-3ae9-ac3d-a8063ef72cfd | -12.9197 | -56.9471 | 2025-09-04 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e5a7e34d-9752-3b70-903b-5fd0611305d7 | -11.5779 | -52.115 | 2025-09-04 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 37ee36bb-0de8-3daf-aab2-164a6411aeca | -8.0796 | -45.3617 | 2025-09-04 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1434f01c-1acb-3b8f-a1ad-c0f1a8a78722 | -5.5892 | -45.0278 | 2025-09-04 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 0ecf70a7-0426-3e13-af88-a1a31e22860d | -10.4472 | -50.3713 | 2025-09-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 624babe2-b5af-3a3c-8971-d879a03d3fd4 | -10.4469 | -50.3926 | 2025-09-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 7efe1559-25bb-35dc-b2ca-4fe375ff7c1d | -6.7649 | -63.1292 | 2025-09-04 01:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 05ebb106-e01f-3446-ad7b-4a39f86c380c | -11.6599 | -54.5297 | 2025-09-04 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 560e890e-3993-36d4-8a9b-dd58079fc5b8 | -6.7833 | -63.1286 | 2025-09-04 01:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 8b8f96d1-7513-3008-a4bb-ffc8a6bd12a2 | -6.7782 | -44.0876 | 2025-09-04 01:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ad51a712-c2e5-32d4-adec-e74037d7bcbf | -6.7648 | -63.1479 | 2025-09-04 01:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 2b002d7d-0cc6-3067-bafb-95cfe279b859 | -5.7189 | -45.1547 | 2025-09-04 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 3356fd8c-1f0f-3385-9e9d-c254b26c434c | -12.9006 | -56.9488 | 2025-09-04 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |


[Clique aqui para ver as próximas entradas](README11.md)
