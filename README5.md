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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87d223f2-125a-39c2-8241-075363e28e2c | -4.1109 | -43.9202 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f17b6f9f-3a57-3601-aacf-917974a732cc | -4.0547 | -46.804001 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e825b36e-4c24-3167-a623-b99fb9991cfb | -2.9235 | -46.768902 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77fd6c92-8156-3671-bd4f-44a0d1811782 | -3.7055 | -51.3321 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69f99133-cb5a-3c45-ae66-77938827b29d | -5.9716 | -45.3437 | 2024-12-04 00:17:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e6c51f3-56c8-3805-9e6d-3f899a3dee3b | -3.2818 | -53.687698 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ba3599-a91a-39fb-b683-8b3fe5309322 | -3.3748 | -51.043598 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2641c045-fee0-3d64-81f5-7de16305a677 | -2.507 | -45.3839 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5807c56a-62eb-375d-9029-e772029d0845 | -9.8613 | -36.611 | 2024-12-04 00:17:00 | METOP-B | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6c9b762-5719-3ae9-a12f-b9d9bab9345a | -3.4058 | -50.256802 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51efa112-f9f1-38c5-a534-22b65fa36ebe | -2.6697 | -46.6031 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4fdd3a4-2e37-3cb6-a657-1a1802a96e27 | -2.0656 | -45.482498 | 2024-12-04 00:17:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef597e8-0e56-3712-97e1-1d4142ec4cbe | -3.8564 | -46.5187 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18b2f533-6957-31d8-adc7-f62a00cba953 | -3.9305 | -46.7099 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d290c5a-901e-3f9d-a944-42197f744026 | -1.8287 | -46.211399 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2e4249-b559-3e8d-b041-f7436865602c | -10.06 | -44.687801 | 2024-12-04 00:17:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2791560-4366-3aac-ae9a-9128edb1a548 | -3.8032 | -51.636002 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 071ab024-eed5-3f86-93fb-389b7eda223c | -5.9708 | -46.298801 | 2024-12-04 00:17:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7c92c4e-e6a6-3553-b47d-7626da212573 | -3.8985 | -46.659698 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f48df41f-3383-33f7-97f3-574e4b2a5616 | -4.3743 | -43.362202 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bee99c8a-961e-3cbf-9b6d-62d6ec0cae97 | -3.813 | -51.6339 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 767586c1-5027-39bb-ab7c-8907aefb3a9f | -2.1925 | -48.327702 | 2024-12-04 00:17:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c94f8da-8885-3071-bced-4a552b0a6a85 | -3.8004 | -46.681499 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 294cf7b8-f6b5-344d-8f9a-04f57e1e12ce | -3.2446 | -46.2738 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c230433d-b6a0-3147-bd67-8902b6215917 | -2.4683 | -46.532799 | 2024-12-04 00:17:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a30ca5f6-2a0c-3065-8275-c1a788950d1f | -6.0898 | -48.030998 | 2024-12-04 00:17:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26a98276-060a-359e-8251-b209f2ac0393 | -2.8839 | -51.792301 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 758f1231-e7b1-3340-8d0b-e9f9c2d2aea1 | -3.6607 | -47.1134 | 2024-12-04 00:17:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0299111d-e18c-3254-a116-73bf6881fc9c | -2.1206 | -46.4081 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f90402ae-1cc8-37bc-a72a-dd274452f4ba | -2.688 | -45.6367 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f89d6d6-0539-3581-83b8-7937fa1315b3 | -4.309 | -48.075802 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1f73487-7371-3598-bbc5-a91084787c33 | -2.8435 | -46.779499 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eef6a2f-e6c5-3ab9-b005-a866da723ce5 | -2.8062 | -45.4757 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1e5673b-1576-33df-b24d-74c50ecea02e | -3.8169 | -46.663502 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8d009ae-734d-3d12-8c0d-5a438d88d3ce | -3.257 | -53.621399 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2e3426-e8bc-36da-b99c-c68768009083 | -12.0407 | -40.461498 | 2024-12-04 00:17:00 | METOP-B | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1cb2dd79-9fa1-3773-91de-da55620a8bc1 | -4.1073 | -43.904301 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 772d962e-538d-3741-83d4-e87dcc24d904 | -4.3705 | -43.345402 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 624fa1df-6f81-3b16-910b-98a039d0c4cb | -3.3142 | -45.4893 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 171ce06c-b50b-3762-bae1-65a751c14f8b | -4.0366 | -46.815201 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c25a174e-ad4b-3732-8513-bc7f855e0364 | -2.458 | -45.895302 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a35fa35a-4a91-3543-9923-e2d9634646d8 | -3.8327 | -50.885799 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53fe9820-7779-3ad5-a040-0c5b8a911637 | -9.7208 | -36.381901 | 2024-12-04 00:17:00 | METOP-B | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fe405e70-e684-3330-a441-b9affb923d36 | -3.7376 | -52.409599 | 2024-12-04 00:17:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f982e418-e1e1-363c-8839-633662f1b2cd | -6.08 | -48.0331 | 2024-12-04 00:17:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08e59de9-4862-36de-9d83-d4449753cded | -1.7032 | -46.202801 | 2024-12-04 00:17:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91189615-a774-396a-b0d4-cdc799b2338b | -4.066 | -46.808701 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7ac7f20-06e8-3e57-8c64-376b08fe3be2 | -3.9708 | -50.349098 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4ecf630-64dd-3ee6-9dc9-3fc47550eafc | -4.2937 | -45.1273 | 2024-12-04 00:17:00 | METOP-B | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 827fab83-55a3-302b-bce2-fc33f40c1f4c | -3.7961 | -50.952099 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 623cbe18-822b-3af9-8bf8-e131ce6e66ea | -3.4742 | -49.962799 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5fc6a42-7c48-31a9-b7ab-e6b2662ef0df | -2.6485 | -46.600601 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba55f86-4ca8-3662-ae7d-decc982b29a5 | -3.118 | -54.568501 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e3e7b9f-7ded-34ef-bbba-ba626977d3a7 | -3.0607 | -54.029701 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 396e6644-13e3-3767-8684-105b6f3c2c6d | -3.787 | -45.665001 | 2024-12-04 00:17:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68e4905a-1b3c-3f7b-a880-2dd6e96e87b5 | -5.5662 | -45.1474 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41857045-6ea8-3f63-bfd1-fe559ce7da41 | -3.1145 | -54.552799 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e814c906-fd8e-3abd-906a-b6dbdd326189 | -1.8303 | -46.2183 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8690a13c-ee4a-3f77-b3c9-349145240067 | -3.4945 | -49.9156 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e9ee7be-2428-3a89-8d9b-1ff1fce967ea | -2.5992 | -46.200298 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37c28b72-f33e-3d95-989b-6e9cef88c8bc | -2.9687 | -46.923401 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec3a1a0f-8998-36ee-be6a-7ffd061c65c9 | -2.5576 | -46.563301 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb36969-cc6a-3fa9-96f6-0b21847abc5d | -3.4927 | -49.907398 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9093e84a-5615-3196-a800-3014f817f8ed | -2.4729 | -46.553398 | 2024-12-04 00:17:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f02422c-7324-3ca6-bced-318cf38476a0 | -2.6035 | -45.400299 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c210ff96-7455-35f4-b7c1-b5b3feabbb27 | -1.7394 | -52.595901 | 2024-12-04 00:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2052122d-b9fc-3343-a507-f74e0a0ae4a8 | -2.7162 | -45.533298 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd49d515-76f2-33b3-8085-795e2d2df6de | -2.6636 | -46.120499 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 412c8ce7-ae96-37a7-a00d-12cf7f3f84ad | -3.5496 | -50.163601 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5f6fb31-1723-30b0-b6f6-3af0d74c95ac | -3.4462 | -45.8438 | 2024-12-04 00:17:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 175bcf7e-692e-31bc-8eb5-1bfb9b01282a | -4.1029 | -43.930401 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18cb1086-734a-3287-b378-812e9616bb2b | -0.959 | -46.831799 | 2024-12-04 00:17:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d573816-675c-3e96-9a40-89466da0cc3a | -5.2426 | -45.856701 | 2024-12-04 00:17:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4c58835-c553-3e8f-8e7e-13afa518b384 | -4.6405 | -49.2883 | 2024-12-04 00:17:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10575e30-6a0a-34ac-abbb-b13b1a5991a7 | -3.9522 | -52.174099 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba1e2db-b821-35c1-8f38-92d7581124f4 | -3.6798 | -50.241402 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f15f8ddc-1286-33ad-869b-835bebdbba2f | -3.2742 | -50.312 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08af4595-45b2-3fcc-8170-7328efff0554 | -3.5221 | -49.901001 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 038e69f1-dbaf-3775-9228-d9f0ce28106f | -1.1721 | -46.999802 | 2024-12-04 00:17:00 | METOP-B | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a2c7c0e-8d2b-360e-bde6-8b9f794ac798 | -3.0964 | -53.727501 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7badd2e0-d6ef-3b0c-bd0a-c751453cd3bf | -3.2461 | -46.280602 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0499d04f-ccfa-397b-b59e-b0ea366102be | -4.0975 | -43.906601 | 2024-12-04 00:17:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e13e864b-ef7d-32e9-930b-41c68273887f | -10.0584 | -44.680901 | 2024-12-04 00:17:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b7ef86a-88c1-358c-ae69-c83cabc5a816 | -13.7996 | -41.559799 | 2024-12-04 00:17:00 | METOP-B | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 81ee7d26-6e21-3412-9842-61dd887848bf | -4.036 | -46.858299 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 583a3211-b3d8-372b-9b82-894fbfedc720 | -1.4694 | -53.7719 | 2024-12-04 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dea67e27-a0bc-3d08-b054-879a1b6d78d4 | -2.0623 | -45.468102 | 2024-12-04 00:17:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6aa5961-7f4c-396c-9a6b-df8b1c5f7de9 | -3.7921 | -46.690498 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 473127f0-836a-3170-8e3c-5a494646ff62 | -2.8123 | -53.042999 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3b0e5d0-817a-38b3-b5ef-98246551b77c | -3.8066 | -46.937801 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45cbfb55-1eda-3cc8-9c95-ab33fbdd3930 | -3.7372 | -50.175701 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efb93cbb-38d1-3889-87e0-80bc453947f1 | -2.6605 | -46.106602 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e906a405-9061-36f9-96ed-55054663a92c | -1.8538 | -46.322399 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a811ab3f-8d73-3236-81ac-cd72335f40f8 | -2.6764 | -46.5872 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b15b7051-7acb-3ed9-ac32-caa65dc5bedf | -6.2523 | -43.548599 | 2024-12-04 00:17:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6df38583-c445-3e36-8591-c3a9310a1e46 | -4.1111 | -48.526299 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37576653-9205-352b-9026-1ba1b0c4c3bb | -2.845 | -46.786301 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb5192cb-62a4-3db6-91ea-a27e2f007241 | -4.576 | -50.439201 | 2024-12-04 00:17:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e75711b3-df59-3464-9176-482499346d56 | -4.4354 | -47.4897 | 2024-12-04 00:17:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3be1bc3d-c7e6-3cb2-bfd8-ade8898e6456 | -3.5123 | -52.130501 | 2024-12-04 00:17:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
