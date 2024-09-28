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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bf3d59b-c643-336c-9d7b-ab579b091b4b | -10.64894 | -46.04924 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffe45b68-0965-397f-a775-57a5f79899da | -10.64839 | -46.05273 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12d8ee1a-699d-36c1-a6d1-9883486e238f | -10.6462 | -46.0452 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 459d2256-169e-3cb9-a917-c15c3cc14c8d | -10.64564 | -46.0487 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e49b4c2-6d01-3029-85af-3037f30c7647 | -10.64509 | -46.0522 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8e71055-5a85-315b-a9b8-5f2ec41e9e49 | -10.64345 | -46.04117 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84e0aa5a-5fd6-3c97-9d7b-f360819661ad | -10.64289 | -46.04467 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47e349a1-c043-3b8d-9ab8-20d17bf6d5d1 | -10.64234 | -46.04817 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a56ed8dc-93ec-3c61-8ad7-7b4e58fe52c7 | -10.64178 | -46.05167 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb191eb0-9844-3fa1-a2fb-7aa2480d7bd0 | -10.6407 | -46.03714 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67530ef2-4248-3199-8980-2fb5bd79e47a | -10.63959 | -46.04414 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 031afe33-571c-382a-885c-9d615a7ce19e | -10.63904 | -46.04764 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9e6c14f-b3bf-39bb-8d03-475ad128f6a4 | -10.63848 | -46.05114 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27705422-6761-3e39-98ff-7d838d905809 | -10.59494 | -46.04422 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93f31b6a-a385-3641-9075-73ced3a8a48f | -10.59439 | -46.04771 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b44473e-35d7-3025-a86f-8f5b6b3d522e | -10.59109 | -46.04718 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83a223e4-10f7-3d7c-a050-c350c30f6424 | -10.58944 | -46.03616 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 226d4982-46ea-3148-8960-22809aa08783 | -10.58889 | -46.03965 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d4c3df3-5c6d-3890-a5a6-70b4129d43d2 | -10.58614 | -46.03563 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68807c80-3c66-3808-b704-41be0b433495 | -10.57403 | -46.02651 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9ff82e8-f90a-3cba-a853-4e5c06a370c2 | -10.57402 | -46.04802 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31a3c56f-5990-38fc-8349-9ff88880bb26 | -10.57071 | -46.04748 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96557dab-0adf-3a37-a2c2-feb193216664 | -10.57018 | -46.02947 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee425659-81fa-329c-96db-3d00e2f80428 | -10.57016 | -46.05098 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d1d0c190-0c8c-3c33-806a-214acb31c325 | -10.56741 | -46.04696 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c745c92f-1f71-3a0a-b219-5f869d6bdc5c | -10.56686 | -46.05045 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2e5a04e1-0f1a-33c6-b6a4-d60d99ba6aed | -10.56411 | -46.04643 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 02febcb9-795c-3b6b-9671-f87fad5cb02c | -10.56355 | -46.04993 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 11702936-faa1-3444-85bd-e8728fbdec5a | -10.56191 | -46.0389 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 874c55c8-01d9-388d-8c03-5633adfe993d | -10.65389 | -46.0608 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 246b0a98-a688-3e65-9ab5-6c47e50d7713 | -10.65333 | -46.0643 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 58e9fc32-da7f-3b14-a873-20caaa8dc589 | -10.65278 | -46.0678 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d55ab838-4929-31ab-aa0e-1fd1289be74c | -10.65114 | -46.05677 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 03da5b07-4fb8-3a95-9f71-6ee091b34391 | -10.65058 | -46.06026 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1e8c4ce4-4778-3aa3-aacc-48b58269f74c | -10.65003 | -46.06377 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8285e397-16d3-38fa-b4ab-cfa0a1490902 | -10.64783 | -46.05624 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d815241e-2134-3da4-94d0-5162de75a8f4 | -10.64728 | -46.05973 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ac7b387-7fb9-3332-8d24-5ebf1ca26310 | -10.64453 | -46.0557 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c613dfa9-86f3-39c6-b7d0-c1a1c36de4af | -10.64231 | -46.06971 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba1a011c-9c1b-3d50-af62-a2d3597ea051 | -10.64123 | -46.05517 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aabae1fd-b823-333c-94a1-ecc87411bf97 | -10.6412 | -46.07671 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b2abf4c-7d57-37b5-ae79-48d2f5c75a87 | -10.64067 | -46.05867 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12628f46-d7c5-35b0-8347-05260137fd8a | -10.64064 | -46.08021 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a36c8580-e27c-3741-b777-8e2c2e0954a5 | -10.64012 | -46.06218 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0122fb5d-212f-3edf-b295-f0de73055ef9 | -10.639 | -46.06918 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 888aded7-35a2-3264-8529-a6a244075113 | -10.63845 | -46.07267 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f81eaf10-224d-308e-8489-9be7d4731633 | -10.63681 | -46.06164 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 486ce548-01a4-37b8-ba2f-bb76c20fdf15 | -10.6357 | -46.06865 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39ff8252-243e-3f9a-ac4b-ce6bc9d26388 | -10.63459 | -46.07564 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84d2b503-e694-3635-bb17-7328cded7e12 | -10.63403 | -46.07914 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd69ede8-1908-33a3-a5a0-8ccae09997aa | -10.63348 | -46.08264 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81380975-7758-3d67-a16e-5dbc14213399 | -10.63184 | -46.07161 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae3e07dd-5b41-32f4-86fc-395cab16263b | -10.63129 | -46.0751 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5600ee9-9d36-3e67-b4dd-d1f6f1535aed | -10.63018 | -46.0821 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 218e137c-654f-390f-8df6-26a75940e06f | -10.62249 | -46.06651 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e796ab4c-76f3-3f3e-a6db-9f6719eda590 | -10.62193 | -46.07 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58bebabc-be8e-375f-aacd-53b7f163cf48 | -10.62138 | -46.0735 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc0a4db6-cd95-302b-a7cb-980f77216857 | -10.62082 | -46.07699 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94bf83cf-aaa6-340e-9ebf-8e0e7576aafa | -10.61974 | -46.06247 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71301a4c-2713-3626-a89a-6969e6915ce0 | -10.61919 | -46.06596 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9cab5a6a-6292-35c1-b9f2-7fc4987e7955 | -10.617 | -46.05843 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de97e10e-3300-3609-87c9-0015cbaf939a | -10.61644 | -46.06193 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1a6158d-314f-3a2f-9f51-1e524018db67 | -10.6153 | -46.09045 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 075340fa-89e4-3452-b8a1-74f093286ada | -10.60648 | -46.07838 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7190c18a-cffa-3fd8-ba55-e886c7f63ef1 | -10.59934 | -46.05927 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fc3f680-5718-3c0a-ada5-d868ab59c2a4 | -10.59659 | -46.05524 | 2024-09-28 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2e8af3a-4bd8-352f-9551-3b04f7f2d24b | -10.59879 | -46.06277 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8358db1-4b40-3acc-bc40-6534cc07fe4c | -10.59823 | -46.06627 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 643021de-dd39-38ac-b205-c3d88194d853 | -10.59604 | -46.05874 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ce8ecdf-6cef-32ff-afb9-680dc34bd689 | -10.58446 | -46.06765 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e0f8c72-a0b7-3b56-a7eb-8dcc8326fc29 | -10.58227 | -46.06011 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f99dd4b-6f84-3a2d-a8a6-cd075365e37d | -10.58171 | -46.06361 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0df68b7-2cda-365b-b267-e07dedb3bf66 | -10.57896 | -46.05958 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2504af7-cf62-3ab6-aa2c-da5c6559eb4a | -10.57786 | -46.06658 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87842bcc-b6ab-3e4f-a16e-329935e9c45d | -10.5773 | -46.07009 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66b5c149-43d1-3607-a44a-ae6451192266 | -10.57675 | -46.07359 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02ee0626-0ba7-30dd-a4cf-0d109dec8fed | -10.57619 | -46.0771 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da0fde8c-bd4e-3a57-aa82-3c924a5542ce | -10.57564 | -46.0806 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fd25d07-dd74-3615-a7fc-8fde8ed948b1 | -10.57562 | -46.10215 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efde54ed-9e05-38c0-ba53-90902215f40e | -10.57511 | -46.06255 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6b3113f2-1655-3fc8-8848-9207cbbc217b | -10.57508 | -46.0841 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33a91648-237e-3895-a5dd-51e27cfa5808 | -10.57455 | -46.06605 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2f2e61f4-f179-37ca-b04c-c5761d1eaae0 | -10.57453 | -46.0876 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 073562f7-d092-3159-8829-c5e3b5c156bf | -10.57397 | -46.09111 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f03c5130-07b0-34db-b27f-74a38f5a2fe7 | -10.57342 | -46.09461 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08a1375b-c5ca-3918-96f4-b56d67520c81 | -10.57286 | -46.09811 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9581c850-1e67-3f25-b45e-c9b997d32304 | -10.57236 | -46.05851 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 486bb051-2542-38ae-8b0c-758db578d8a3 | -10.5718 | -46.06202 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cf880206-d1bf-347d-be9e-11b790f4f360 | -10.56961 | -46.05448 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 2f2c8580-09cb-3dc3-b5a8-8976b130c455 | -10.56905 | -46.05798 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5d1dc8e3-478b-316c-ae4c-1518be2baef9 | -10.5685 | -46.06149 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cd52bfe9-a2af-3148-9dd7-0eadfac41731 | -10.5663 | -46.05396 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3831c4a5-c4ac-39fa-beff-f6ea092110bb | -10.56575 | -46.05745 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 747825aa-735a-3a74-a9d1-1de2815aa07f | -10.563 | -46.05343 | 2024-09-28 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7f16b9a4-72ea-30b6-9150-35c19173acb7 | -10.00781 | -46.07782 | 2024-09-28 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae226467-aa46-36fe-929e-32c1c0e351d0 | -11.7879 | -47.62033 | 2024-09-28 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3421864f-8960-31e2-89bd-019a310d9966 | -11.78451 | -47.61977 | 2024-09-28 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a66b270c-e4ee-32c7-b624-b05666fd02ae | -11.7839 | -47.62347 | 2024-09-28 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4729f739-34ff-3c95-b72c-c9c0792cc46d | -11.7799 | -47.62661 | 2024-09-28 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3363ca1b-d1ad-3be4-9769-42d5b7a0b327 | -11.69434 | -46.34655 | 2024-09-28 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README52.md)
