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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cbb1347-0cb1-3726-8db3-93ccd000b047 | -13.8371 | -54.0989 | 2026-08-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 237.0 |
| 9cdbddee-e642-3b22-847b-1004e6ec1005 | -9.9281 | -60.5242 | 2026-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f15dc76a-89ca-30a6-80cc-eb7b807b1f48 | -3.6399 | -60.5466 | 2026-08-30 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d954217d-a4d3-3fcc-9aed-46d8fee8e8bc | -9.874 | -60.2762 | 2026-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a41724c2-5e8f-3841-bdcc-38805efd2e14 | -9.0615 | -65.4169 | 2026-08-30 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5b905343-f1e7-3458-b4a5-53ad9e5d7f23 | -3.7715 | -59.3419 | 2026-08-30 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e1541477-da30-34e3-b25b-fc364edc04d8 | -13.856 | -54.1175 | 2026-08-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 377.3 |
| 184dbeee-ccbd-3766-baef-96b7a921767b | -11.2879 | -54.0317 | 2026-08-30 00:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 49329215-e125-31fb-8df1-480d62585020 | -5.871 | -57.7715 | 2026-08-30 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9f1532ce-131a-3ce1-a9a8-31eaf9ef145f | -4.9603 | -55.8622 | 2026-08-30 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8d46eb20-7903-3586-a632-9d1bfcad94bb | -7.3117 | -60.6089 | 2026-08-30 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8db8adb2-db26-3514-8293-a4ddc0afd69a | -10.8058 | -45.3407 | 2026-08-30 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 4858df0f-afdf-3b80-aa83-77912d540244 | -10.9597 | -43.0088 | 2026-08-30 00:50:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b567f000-24ab-35df-ade9-6d6eb33b2687 | -9.8927 | -60.2752 | 2026-08-30 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 64c78dbc-459c-31ab-a100-230f77fcabc9 | -13.8752 | -54.1153 | 2026-08-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f56df291-8c35-3565-bdae-18c639435675 | 0.14474 | -60.40132 | 2026-08-30 00:50:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 42ed6936-6cc0-3c09-a4de-0fc327fa5d51 | 0.1357 | -60.40005 | 2026-08-30 00:50:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c500fe34-cc21-35a0-bd8d-99561574c716 | -4.9591 | -55.865101 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21ec545-b18a-3b88-ac28-ab501b8ec8c5 | -4.6876 | -55.663601 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e216194a-d132-3c09-be98-0e24aefb67f5 | -14.9166 | -52.631302 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 819b382f-037c-3f8a-94da-1eca62837c8a | -10.4848 | -59.596199 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf99e22c-436f-3aac-b481-757c527bc895 | -14.4289 | -52.561798 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecf0bae5-2ffe-3006-8b40-4ced3a0f72a1 | -6.7434 | -55.659199 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f551e040-c23d-3d41-bcf0-aaa15e30b48e | -8.5097 | -55.283199 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3e7ae8-c47a-3b64-ad64-ee3818a0095a | -7.5295 | -55.59 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1c305e5-1159-3391-80bf-33b133411173 | -11.6939 | -47.614498 | 2026-08-30 00:55:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3a32cce-8b36-3ea6-abbc-f7753c6c33ce | -6.9592 | -55.705502 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4d712d-eb2e-31ec-b6b5-b294d05a5438 | -10.9422 | -43.031601 | 2026-08-30 00:55:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86844aaa-f66d-3602-93e1-cb9bf1c772d8 | -9.7583 | -48.162201 | 2026-08-30 00:55:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79849294-e27b-312c-ad64-282f8b8d4da4 | -8.624 | -54.729 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 271d149f-4a34-33b4-95dc-db01a8c3ebed | -16.358 | -50.990101 | 2026-08-30 00:55:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6922c3a3-bdd6-3efd-b48a-1691a500e108 | -11.3494 | -45.1591 | 2026-08-30 00:55:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31202033-8fa1-3cb8-9700-1d64c28059c7 | -19.0835 | -57.382599 | 2026-08-30 00:55:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a61e8f43-bf40-3205-a57a-dac5ea3f8160 | -7.5137 | -55.3321 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 919429ff-3ded-31a6-8c0b-4ec6c69b6e13 | -7.089 | -51.577202 | 2026-08-30 00:55:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4a87ab5-7a15-34ba-850d-1a93bd2e4c72 | -6.687 | -60.102798 | 2026-08-30 00:55:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de1d211a-5dbc-3efb-b590-c9b44038644a | -6.6416 | -53.185501 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10802dee-55d7-3c8e-8401-ee2a90b582ae | -8.6147 | -54.779598 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20874597-d518-33bf-abc8-2aa95c566e0e | -4.9637 | -55.839401 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52cc1279-2dec-3c7d-942a-c6fbc15152af | -3.6226 | -60.5522 | 2026-08-30 00:55:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 481c0d47-7a6a-3f86-8850-ac11258ce280 | -9.1602 | -58.307701 | 2026-08-30 00:55:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6676e5a0-72b3-3d20-9a0e-8c78bbfe0265 | -8.9398 | -62.3568 | 2026-08-30 00:55:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| adc2b653-7ceb-3641-b4fa-d271ba8852dc | -14.7537 | -48.744598 | 2026-08-30 00:55:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd3e8e38-9763-3ede-800f-0df0d3524770 | -4.4341 | -58.6721 | 2026-08-30 00:55:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0298da-775e-3ae2-b850-871d3d0e7b9e | -7.5651 | -61.3237 | 2026-08-30 00:55:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d653cf9-cbcd-3111-b341-f12d0164dff0 | -11.1633 | -51.306499 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2857e21a-23ee-3197-aadc-aa7f6e298a29 | -8.61 | -54.805 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175b93b6-a11b-3c9b-bad5-e5d6deefe0c5 | -6.1273 | -53.553299 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7a0c2f-c18f-3f89-98f7-2ae90dd8854d | -7.3055 | -49.534 | 2026-08-30 00:55:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e06f23db-c7f5-35ad-bd23-f836686ce892 | -9.9522 | -53.992699 | 2026-08-30 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34d1e74a-f1fd-3795-afda-fd34b04846e2 | -10.9957 | -50.529499 | 2026-08-30 00:55:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| def3d4ea-7695-3e5e-98ff-c1e394c59f23 | 0.217 | -51.465 | 2026-08-30 00:55:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8057dad0-f206-3ecc-8a2d-79a28705ec2b | -11.8331 | -51.122799 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06d33465-c754-30af-abcf-5eb0b0a6ab07 | -1.3739 | -49.295502 | 2026-08-30 00:55:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aedb5a2-0c5f-3130-a5dc-e7076a1c008c | 2.1894 | -50.7132 | 2026-08-30 00:55:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 42c94f9a-cce3-3c9b-9fb6-25e00be5a0e2 | -6.4264 | -55.527802 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03f1e7fa-5082-3087-8f1a-9d11d04b4a25 | -10.3906 | -49.612801 | 2026-08-30 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0168a72-9060-36c8-ab41-81b7c5ef84b3 | -5.9885 | -55.731499 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2218fb89-c571-30d2-8ca9-a2bffde7c353 | -8.6181 | -54.795101 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b06d4e12-64f5-33af-b1bd-b87e79254858 | -20.5012 | -47.457001 | 2026-08-30 00:55:00 | METOP-C | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b3f99a23-77ed-3c9c-b0d4-560e1921f3f2 | -14.2509 | -54.6614 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bfd356a-25c6-3233-be25-7a922fab7878 | -7.5553 | -61.3256 | 2026-08-30 00:55:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27bb8656-0919-365d-8363-5f46438c3424 | -14.4207 | -52.5714 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eece02e0-c624-3e3a-bcf2-2dfb845354fd | -13.8701 | -54.117298 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a1e25f8-4877-3a01-a75a-019262d90179 | -4.9574 | -55.8573 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5b03582-17d3-31e3-b0f5-3a30802fef62 | -5.8869 | -57.7789 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2979aa8-8cb8-3b26-91c7-a33fcbcd3a1d | -10.3525 | -49.980598 | 2026-08-30 00:55:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8b97285-0011-30df-94c0-8ea21a3eccae | -7.4888 | -55.3125 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac1f42f-720a-3796-be7f-61f4a26cacad | -11.4467 | -61.487099 | 2026-08-30 00:55:00 | METOP-C | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed64c9f-f24e-38ae-9398-49cb99d45819 | -7.5182 | -55.306099 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0556ac4-1a93-325c-9b62-6cab063ce81e | -8.59 | -54.7607 | 2026-08-30 00:55:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed39ca9c-d57a-39dc-abbe-e2493333e110 | -9.9538 | -54.000198 | 2026-08-30 00:55:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17063751-6081-31b1-8f40-d21316d14749 | -14.4191 | -52.563999 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b4456a6-f81b-392a-82e1-5865d3fed03e | -10.7542 | -50.6908 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f741fdc2-a142-32c6-910e-9e477fdb872e | -9.1763 | -59.6035 | 2026-08-30 00:55:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb71f3c5-17b6-3ce5-81de-03f8307fa097 | 2.1642 | -50.6884 | 2026-08-30 00:55:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0c2b50cd-450b-30da-afb7-b029b38084b4 | -4.0888 | -54.1078 | 2026-08-30 00:55:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59e745fb-82c2-3ee7-9f10-fa423f9f0e5f | -10.1306 | -45.7005 | 2026-08-30 00:55:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a01f0f2-d542-31f9-ab1a-0d5e27dd4c32 | -5.8802 | -57.748199 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed5a75cc-bb0e-3be6-9087-451f9fdc702b | -2.9155 | -54.1157 | 2026-08-30 00:55:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7115f950-1e46-319c-9190-a5d9f6f92da9 | -16.3498 | -50.9995 | 2026-08-30 00:55:00 | METOP-C | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6a39537f-d4c4-33cf-b5fc-d534271de37e | -12.5628 | -55.735699 | 2026-08-30 00:55:00 | METOP-C | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92591416-c227-3555-9d76-a3b4c3c89288 | -10.7551 | -54.044899 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae8ad12a-7692-310c-8e77-31bdd458f853 | -9.7703 | -48.1689 | 2026-08-30 00:55:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6177474f-9fa5-3867-949a-aef8cd6b4214 | -10.7558 | -50.876999 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7076f55d-be12-3082-9456-98a1a772abac | -13.8718 | -54.125599 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 059dad43-0864-3ccc-b941-5a90942bb262 | -2.93 | -51.479599 | 2026-08-30 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f595d6d-a48e-3caf-a789-f2a7dfb0c9d0 | -9.6725 | -55.107399 | 2026-08-30 00:55:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31fed68e-b71a-310d-b6e8-27ab7424605a | -14.398 | -52.5611 | 2026-08-30 00:55:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8c8dbae-f98c-32d6-8b7d-9b790dd54d5d | -9.6651 | -50.8456 | 2026-08-30 00:55:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2751bc18-96f3-322d-b54c-e4126c149c41 | -6.8745 | -41.652401 | 2026-08-30 00:55:00 | METOP-C | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c89c2255-ef87-3bfa-89e6-f70aede1a601 | -11.2947 | -54.022499 | 2026-08-30 00:55:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9572dd48-ed88-37ac-9f5b-eb5e9ed8dd05 | -5.7625 | -51.685398 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f04232e-ae6c-3a6f-b389-ee6943ade373 | -6.8569 | -59.468399 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a915f89f-254d-38bc-b5e3-a97fda3552f6 | 1.1208 | -50.889099 | 2026-08-30 00:55:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 92bffe89-e850-3a53-863f-83a93a5a6912 | -6.7728 | -55.652802 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bf15dd1-5db2-373a-b76f-912921f69e95 | -10.7559 | -50.698002 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de784b96-a597-3b07-abe4-727b8caf8f87 | -9.7681 | -48.159901 | 2026-08-30 00:55:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16fcd893-c494-3256-8bad-c4c72c790a4a | -3.6356 | -60.564499 | 2026-08-30 00:55:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b1923ac-3b7c-3120-9a89-6dc5096360ac | -4.1525 | -60.6856 | 2026-08-30 00:55:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
