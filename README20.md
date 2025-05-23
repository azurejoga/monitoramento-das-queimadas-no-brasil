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
| 584467a1-fce5-34d2-8f1c-de46cfaa5419 | -9.29356 | -57.54995 | 2025-05-23 05:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c936dc-86e2-37d6-a301-699231e3006c | -12.299 | -52.50902 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 641f504c-acde-3a41-b892-093c7fb56568 | -11.29801 | -53.9874 | 2025-05-23 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef0f5406-e8cd-3709-8f3b-e7c6db0b3f42 | -11.09124 | -57.27149 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ef1f0c0-2319-3dee-a531-6f67ff9b7d56 | -11.29433 | -53.97792 | 2025-05-23 05:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9be52f-72f7-3fdf-b492-f5b1dcbdad77 | -11.08589 | -57.27079 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa7f6998-3bdb-3b11-a708-13e5e924dc17 | -12.28606 | -52.49253 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 132da2b7-847a-3d40-972a-4c3c43b4abeb | -9.49142 | -63.33074 | 2025-05-23 05:44:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ed09906-8be2-3270-a55d-9bfdf4a44209 | -12.2948 | -52.49179 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 378d0e03-de36-342c-a1ab-79bad00c1476 | -12.27766 | -57.26809 | 2025-05-23 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fd761ec-d0c6-30bc-a7f5-158f4b96b2d4 | -10.36947 | -57.50407 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1354caf-d357-365a-9aa4-574aa17713b6 | -8.17021 | -61.47419 | 2025-05-23 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67ddf173-3a83-3f8b-929b-a19cfb604585 | -10.98776 | -59.1521 | 2025-05-23 05:44:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 750711c9-e807-32c5-be96-5dc06b5ae925 | -10.37028 | -57.49774 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6383ebbc-64e3-3722-91f2-249aba58dca2 | -9.29316 | -57.55298 | 2025-05-23 05:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5909bcdf-6c73-3d2e-9d5a-06e368f57916 | -12.30131 | -52.50008 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57a5d6f1-45f3-3ab8-808c-b9a8df5d43fe | -10.98708 | -59.15701 | 2025-05-23 05:44:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 504cee73-a285-3bb9-8419-ec7e254d7bbc | -11.81327 | -57.35911 | 2025-05-23 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7c5f3d55-32ee-34ac-964b-696f1ec7a30e | -11.65668 | -58.26297 | 2025-05-23 05:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e48e653-7011-35d3-be5c-fbd80f6e3e09 | -12.29403 | -52.49923 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65b32b3b-daae-366a-b5e3-0116edcada1b | -11.80211 | -57.3611 | 2025-05-23 05:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3612d95c-c4e5-31bf-81d1-a85c083e0085 | -8.16563 | -61.4784 | 2025-05-23 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61e6a9b3-011c-3f7d-bcdc-5a0580558a5a | -12.28752 | -52.49089 | 2025-05-23 05:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83045b16-19f4-3474-9dd5-eb924e4b9231 | -10.68145 | -57.60535 | 2025-05-23 05:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b59229c4-a8af-3b37-90b8-b956951abcd6 | -20.84985 | -53.74379 | 2025-05-23 05:46:00 | AQUA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 82a94afe-ea11-39fe-9218-30c24b468990 | -21.71891 | -55.37003 | 2025-05-23 05:46:00 | AQUA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 319e525b-4eca-3f2c-b6d5-ae4564510068 | -13.78445 | -54.30635 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f1e8e055-c1e3-3ff0-a667-d24e95590a71 | -13.9792 | -56.01126 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 812fc210-0e64-3275-a683-961ca52afcd9 | -13.79049 | -54.31323 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ce0cce5-025a-3375-8967-0c941ba2c690 | -13.9913 | -56.01228 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3506e9cf-00fb-3ec6-93bf-ff258c2de831 | -14.02952 | -55.13931 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2b3be3a-8add-3943-bdf1-d5925fd8a978 | -13.94347 | -54.48827 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73c154e7-ee31-392d-953a-f9a969c02c2a | -13.77996 | -54.31184 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| caf82bfe-7251-3f7c-bbe6-4b6dcaaa1668 | -19.79918 | -53.83884 | 2025-05-23 05:46:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dce1ccbb-33ee-3cee-a077-b94e739c088e | -14.03172 | -55.13222 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7c316a0-089c-3a20-b106-5dcd3662d484 | -13.24909 | -56.54444 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c753c3-4a6b-3d1c-b332-058649d78578 | -14.01844 | -55.13588 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7138a9dc-9012-300c-bd76-c324947af7bb | -14.03012 | -55.13399 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe4c74e0-5ab1-33de-95b1-6e7e8add28c3 | -13.78384 | -54.31226 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa6b68f7-9fce-3c5a-b62f-273ae364bbc9 | -14.03649 | -55.13469 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4240d261-c2cb-3d50-9024-0fd83f0a1658 | -19.79188 | -53.83863 | 2025-05-23 05:46:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b241d2b2-264b-3a0c-843b-6b61fe8a6214 | -13.7866 | -54.31284 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 258b2b40-6930-3933-9b5d-85c48dbf8a63 | -14.03945 | -53.37436 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 724c9283-0a1e-313f-91d5-cce4f2c8004f | -14.07021 | -57.10719 | 2025-05-23 05:46:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12a3187c-b774-3055-a17b-6ba17266f4f5 | -14.019 | -55.13055 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 267148c4-b4f8-3a74-9aee-1bccedc357ac | -19.79991 | -53.83578 | 2025-05-23 05:46:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf8dc000-0668-377d-98a7-3edf5b0d37a0 | -13.78597 | -54.31857 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc607653-f07f-38fd-be7d-83dcff65be39 | -13.15803 | -56.8176 | 2025-05-23 05:46:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bbd04008-097b-33e6-8bb5-8b96ddfe5112 | -14.02256 | -55.14384 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a915941-55e2-3bf4-ac6b-66b693cd0235 | -13.98474 | -56.01624 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 66d6e99c-1e99-358c-8bec-4f3306f2af94 | -13.72425 | -58.67072 | 2025-05-23 05:46:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 659b2cc5-fcce-32a4-ad15-76ca074e9a71 | -14.07066 | -57.10337 | 2025-05-23 05:46:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6b6aaac-bd5d-39cd-86df-323d2ce1a0b1 | -13.86042 | -59.72372 | 2025-05-23 05:46:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36fe688b-821e-3fe9-8824-ccc57a33d2ab | -13.98525 | -56.01177 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d99f8c59-a396-3251-953c-9d7990345c02 | -13.1632 | -56.82235 | 2025-05-23 05:46:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 108d44bb-9cb9-3bb1-a4d8-fbb39d3095e5 | -14.04581 | -53.382 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d29d7ce-10ff-3912-a302-4f499c7870f8 | -14.04651 | -53.37518 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38d48b1e-6b58-3334-adb4-65e453b49067 | -13.98578 | -56.00706 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f49fb73-7d33-3053-bd12-041ef0a63234 | -14.01741 | -55.13237 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0677144e-00f5-389e-9084-b256841b77bd | -13.98424 | -56.02064 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 19f2ea1a-3490-32c2-9e97-f2c62e6a4146 | -13.16274 | -56.82617 | 2025-05-23 05:46:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 430d08f1-004e-36b3-aa99-20bbb74aac22 | -19.79261 | -53.83547 | 2025-05-23 05:46:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5077bfc-38ae-3862-b9a4-bf78a60d4ea6 | -14.02423 | -55.14207 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ec203c5-eecd-3de2-89a3-353524ec0f5e | -14.05357 | -53.37598 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc126872-25fb-332b-8f5d-68dfa72af3ae | -13.72005 | -58.66992 | 2025-05-23 05:46:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b320af79-714c-3922-bb01-f3b9f49dc8f6 | -13.72509 | -58.67062 | 2025-05-23 05:46:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f758b67-8015-3644-b278-ae9ce225b577 | -14.03876 | -53.38116 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53d9b230-7ce1-3a57-9d3e-3a6a515d1fd3 | -14.03752 | -55.13824 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 538510d5-4837-3b6f-b343-bc78ac066e83 | -14.62674 | -59.99983 | 2025-05-23 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca417f16-93db-3fc1-a84f-b51ff1b0fd24 | -14.02479 | -55.13673 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02cb6658-c6f7-3a44-af9f-df5dcb472f3d | -14.06501 | -57.10286 | 2025-05-23 05:46:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5ac6f3d-0169-39f5-ad53-64e9a00162de | -14.02317 | -55.13848 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26301787-bebe-3ce0-a186-75591508e499 | -13.71921 | -58.67 | 2025-05-23 05:46:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa9dd183-a092-3f2f-9d39-a4bd74dd0172 | -13.78726 | -54.30689 | 2025-05-23 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f48cf2bf-acf8-36f3-9ba0-a690228c5453 | -14.03115 | -55.13756 | 2025-05-23 05:46:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b65b7281-2ca6-398b-b0ee-7fb11cdec748 | -13.99079 | -56.01675 | 2025-05-23 05:46:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 693b9aff-3d35-3b1c-8ebc-2f7fc99e165e | -13.15755 | -56.82154 | 2025-05-23 05:46:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 052e9318-f8a6-30a0-9724-3d0b7b93bf72 | -21.72513 | -55.37086 | 2025-05-23 05:48:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d52109-7649-3890-9270-9d045eb21250 | -21.71749 | -55.37149 | 2025-05-23 05:48:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0913e50-61e9-3915-aa5b-bdae563b4e7c | -21.71801 | -55.36489 | 2025-05-23 05:48:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfac0384-0095-3d28-8ca7-0421b29a6084 | -20.85451 | -53.75651 | 2025-05-23 05:48:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| afbdfe88-6320-3af6-a308-d3acd2709c67 | -21.72429 | -55.37209 | 2025-05-23 05:48:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ff75d12-f4f8-34d1-89b9-e63400fc435f | -20.85505 | -53.74884 | 2025-05-23 05:48:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24a9852e-fdc7-30ec-97de-c2764aaa2982 | -20.8477 | -53.74776 | 2025-05-23 05:48:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc79da20-f512-3ce0-9f78-a8d3f04418a7 | -21.71832 | -55.37025 | 2025-05-23 05:48:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a942579c-b1ce-3094-ad8a-433be351aea4 | -21.71881 | -55.3636 | 2025-05-23 05:48:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4bb6f7e-6dde-32d7-bce6-74eed8881143 | -6.2224 | -43.3693 | 2025-05-23 05:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d5334a71-8394-33c8-aa03-0330effc767e | -13.9818 | -56.0151 | 2025-05-23 05:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 53d7a255-481e-331c-a805-4bb3591eab25 | -6.2224 | -43.3693 | 2025-05-23 06:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b666e225-3093-3797-a04f-7a5e243f1d43 | -13.9818 | -56.0151 | 2025-05-23 06:00:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 01274a80-3e02-3739-b044-1e4e10a39430 | -9.54498 | -63.33257 | 2025-05-23 06:05:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0e3c2af-79fc-3d9a-83fb-416145a20071 | -9.55025 | -63.33331 | 2025-05-23 06:05:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8170ecd-8089-3cc1-9cab-ff31d713a30b | -13.85761 | -59.72089 | 2025-05-23 06:08:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94193d50-9980-3a00-9444-72f5607be737 | -13.85693 | -59.72744 | 2025-05-23 06:08:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 366fb809-3d45-3f71-8cfd-56d802370731 | -6.2224 | -43.3693 | 2025-05-23 06:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0b32c488-da9c-33a3-9d1b-d6e7a8250c33 | -13.9818 | -56.0151 | 2025-05-23 06:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 4dd35781-46c7-353a-af02-589525bb1cf8 | -13.9818 | -56.0151 | 2025-05-23 06:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d8b9b765-6bd9-39a4-82cd-365191e59552 | -6.2224 | -43.3693 | 2025-05-23 06:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 51640830-affc-3aa7-83d0-a47f9b59ce6b | -6.2224 | -43.3693 | 2025-05-23 06:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e02a756c-7b0b-354c-a49f-1605f68d6b66 | -13.9818 | -56.0151 | 2025-05-23 06:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |


[Clique aqui para ver as próximas entradas](README21.md)
