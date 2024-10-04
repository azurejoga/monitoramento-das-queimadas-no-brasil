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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcad829a-7455-3a6b-9210-895083e34bcd | -17.36883 | -42.62276 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f639849-5297-3ffc-af71-9d5969680b37 | -17.36827 | -42.62649 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70dd6a84-bad4-3666-a419-bd81b77db505 | -17.36491 | -42.62594 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66f91636-81c7-3f45-87b9-f8e4e5987588 | -17.35314 | -42.61257 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d3750c2-708c-34ae-8d1c-1deac35fbbef | -17.35258 | -42.61629 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65d25d94-6d1b-33b3-9601-9097e53f8998 | -17.33369 | -42.37108 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7593d74-58c3-37f3-af3f-2bbf7ba3462c | -17.31941 | -42.36509 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fc58e3e-0d20-3abe-88f2-3340d3da7153 | -17.31884 | -42.3689 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1cfe9e1-0d07-39ef-a40e-b23a02912398 | -17.31433 | -42.37592 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3fa2a2e-efa5-31f1-8a60-735d967356c2 | -17.33237 | -42.37111 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6a46b26-5767-3d8c-b889-48fdbe744767 | -17.37946 | -42.48255 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44f68eab-46f8-34d0-b052-c0c29e4de045 | -17.32955 | -42.36676 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e7ea0cb-07ba-37a8-b44e-259e6b3f7da5 | -17.3149 | -42.37214 | 2024-10-04 04:10:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20d07422-af96-3b6b-a0f4-f1239bc5b9f1 | -17.96172 | -42.21631 | 2024-10-04 04:10:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bfc130ac-6631-35db-98b7-dd25b971f146 | -17.93549 | -42.20435 | 2024-10-04 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b0b999a8-1536-332d-b233-b5a308115a87 | -17.93206 | -42.20388 | 2024-10-04 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f45daff6-d076-3563-827f-b6a7ecfcd321 | -17.93149 | -42.20782 | 2024-10-04 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c2f1c194-2a6b-362d-a76c-70bda78019d5 | -17.92864 | -42.20338 | 2024-10-04 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a691719-8a50-3427-bff0-3fdab746bd44 | -17.90982 | -42.18843 | 2024-10-04 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| cd91ed74-35a5-3c79-8e41-f0d6e7f8a5b4 | -17.9064 | -42.18788 | 2024-10-04 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 81c7e5cd-b678-38fe-93ff-b96dfae39937 | -17.85099 | -42.2554 | 2024-10-04 04:10:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4773ccaa-c92c-3784-943b-2c8d755c445e | -17.62648 | -42.01902 | 2024-10-04 04:10:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9fa9e4c1-fa8a-340d-a3c8-39bf210fe72e | -17.62305 | -42.01846 | 2024-10-04 04:10:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e0ff5509-f975-3d16-8221-ef59ac0635da | -16.66643 | -41.73864 | 2024-10-04 04:10:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36534bf7-e64d-3982-b920-85cf4df3353f | -16.66587 | -41.74246 | 2024-10-04 04:10:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 702f9e27-7631-35fb-8ac0-2e99c213167d | -16.66549 | -41.74148 | 2024-10-04 04:10:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a4d6d301-efe1-3da3-b865-727df2973020 | -18.69623 | -43.05246 | 2024-10-04 04:10:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 173373ba-4508-32db-bc9a-f20e392eb1a8 | -18.63615 | -42.77333 | 2024-10-04 04:10:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f7e0959-c521-32bd-9560-8eac2870468d | -18.57843 | -43.04504 | 2024-10-04 04:10:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5434c646-3277-3292-9cf8-3c644ee98e01 | -18.57452 | -43.04822 | 2024-10-04 04:10:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 129ddda8-ff35-3a70-bdf5-9c7b9d0125be | -18.51203 | -42.96912 | 2024-10-04 04:10:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a5493fb6-cc23-34a4-96b9-2bf023382501 | -18.5042 | -42.95254 | 2024-10-04 04:10:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f557b1c-c056-3b88-bfb2-38bc83e70fe4 | -11.26971 | -43.41944 | 2024-10-04 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41c6a638-ea1a-39af-9b72-da6bb986c674 | -18.28948 | -42.5624 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8935d95e-b4fc-3a5c-b87e-46f8c081af5a | -18.61959 | -41.84964 | 2024-10-04 04:10:00 | NOAA-21 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5b7015b7-8b20-327f-ab80-8585e9bbed94 | -18.61669 | -41.84501 | 2024-10-04 04:10:00 | NOAA-21 | MATHIAS LOBATO | MINAS GERAIS | Brasil | 3171501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 29820707-294e-32a3-be0f-0d3fcd502319 | -18.58937 | -42.47245 | 2024-10-04 04:10:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 95e3f7db-60f4-3c10-919b-dba69352a59b | -18.55793 | -42.25664 | 2024-10-04 04:10:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 82d9bf91-4762-3e06-8ba1-14d63885ce16 | -18.55737 | -42.26054 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9f5d3187-111d-38e8-9008-3601c99df382 | -18.55507 | -42.25217 | 2024-10-04 04:10:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c5f87ce-5def-35a8-a0e6-9ce73f822009 | -18.55395 | -42.25996 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b986bd12-8a45-32a9-933c-dd9ec4851314 | -18.54667 | -42.23978 | 2024-10-04 04:10:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fd6fdd56-3860-3331-95e7-dcf703af5ff4 | -18.54649 | -42.23868 | 2024-10-04 04:10:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2ec01ac0-92d8-3972-bda7-78d647f0fd7f | -18.54379 | -42.25934 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2a53ea6a-cebe-321e-833e-b22002a9272c | -18.54367 | -42.25827 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5dcf0b7c-70d5-3a58-8617-713e5886fe54 | -18.54324 | -42.23925 | 2024-10-04 04:10:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cbe07775-0ff1-3b92-99ac-b8c4f8c7dc3c | -18.54321 | -42.26321 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 38571f46-2375-3eb8-9966-4030f033acb2 | -18.54312 | -42.26215 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5f241e1e-85f3-3665-932b-c8227005175b | -18.54037 | -42.25872 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ef334f25-7990-3f17-9783-437ada6672d5 | -18.5398 | -42.26261 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3abbd703-ccac-3294-9acd-95c957624094 | -18.53696 | -42.25807 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bab101ff-38ae-36d8-91a6-3486d88933d3 | -18.53638 | -42.262 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 27a7ef6e-7927-33ee-9d2b-2e026f1c583e | -11.94723 | -44.73342 | 2024-10-04 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9637601b-cb8c-398a-a76a-82071cd25204 | -18.5313 | -42.24892 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f8704849-1ad0-342e-83ab-f7d8eb9fed7c | -18.53072 | -42.25282 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ab3edc1e-73d5-39ed-a279-a0ae5e53770c | -18.52731 | -42.25217 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ad7af248-322c-3d4b-a7ae-3d9ebc72c647 | -18.52674 | -42.25608 | 2024-10-04 04:10:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6743e5a4-e1b0-3459-8b24-f8233345908e | -18.52163 | -42.21909 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc07c6b0-aefa-36d6-857f-cca4298b738d | -18.52105 | -42.22309 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0d2d4d7d-a91b-30ba-9e26-40a4e1392115 | -18.51193 | -42.21339 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dc756a16-0b26-3f24-a1f5-8a4ade1fbca3 | -18.49361 | -42.19448 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d11bec7b-aa45-3ce0-a947-3ace5f8208bd | -18.43254 | -42.20547 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f0b9eec3-da8b-34d4-a902-3c84d4c3b105 | -18.43197 | -42.2093 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dcbfd7d1-1978-31b7-8d17-72fccba009dd | -18.42966 | -42.20118 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 2be2349e-083c-31bb-8b24-444c993b38d6 | -18.42854 | -42.20877 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 0a40694f-8876-348b-a49b-3285c650c513 | -18.42798 | -42.21259 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4ec414b6-6987-367f-b9e6-3b31d8fd51b8 | -18.42455 | -42.21204 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 70c3c2aa-1288-3fc8-95a7-621a80fd941e | -18.42397 | -42.21595 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| faacf8d5-001f-34ba-b2a5-c49ac313ecc7 | -18.41253 | -42.22224 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cc7e3626-cc6f-31cb-b8b7-c00604f8b483 | -18.4091 | -42.22165 | 2024-10-04 04:10:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f7e2c389-7ded-3b60-8c6e-d63dc907cbc8 | -18.30128 | -42.16932 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 79a0805e-1b2e-32b6-b95b-f028f5c82ee9 | -18.29783 | -42.16887 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c4362a30-3f16-38a6-a20c-70b3dc99f081 | -18.29676 | -42.15209 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c000a6bd-1658-3c81-a4a9-640db1e83957 | -18.29388 | -42.14775 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a71f81f3-d8b0-3739-b866-2fc1964362c1 | -18.29331 | -42.15167 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| dfec9e1a-bfff-306b-b262-2221366e4997 | -18.29043 | -42.14734 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b493889d-81a4-3002-ae1a-81f5eaf1f52d | -18.34847 | -43.03811 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f1573a2c-ccc1-3c58-855b-ca532fd28d41 | -18.33057 | -42.99713 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 25ce727e-ec26-3f8e-834a-ab6273dd85d1 | -18.32539 | -42.99318 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81d7c34e-f20e-3757-9b79-8797dcba1150 | -13.89592 | -44.28049 | 2024-10-04 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fb64a39-a3db-34d1-b35c-110c809a782d | -18.26119 | -43.03215 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dacac7f2-8b50-3cdf-b87b-7ff58a529aa8 | -18.26063 | -43.0359 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a42696ef-657e-3d56-86be-a98df6e5b405 | -18.2584 | -42.93609 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6830fea8-43ac-34cb-b12a-738dcb35d43c | -18.25785 | -42.9398 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32a78b13-9355-35b2-a0a6-f053e3acd47d | -18.24833 | -42.93454 | 2024-10-04 04:10:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| da70d947-5465-37e5-a8c9-86587a134d0d | -18.08809 | -42.66697 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4093a45-9809-34f2-8e93-a4946be6cfe4 | -18.08807 | -42.59692 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e12b2133-2e8d-385e-8535-5e173b27814b | -18.08525 | -42.59256 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9d91b12e-e5a4-3d04-af4c-0df4ae5f919d | -18.08469 | -42.59638 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| c24777cb-0442-3682-911a-58e8c206c638 | -18.08412 | -42.6002 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 90270e58-ec4f-3158-9e07-6d95ecd587d7 | -18.0813 | -42.59583 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 549071ae-a4ad-3a25-907a-167e0285ad19 | -18.08074 | -42.59965 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 685eafc2-a9b9-3914-89c6-2494aea6ab4d | -18.0768 | -42.60292 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7c49b8c0-cf5a-36a0-af32-b25bd027a806 | -18.07454 | -42.59473 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0132f403-9063-3e05-9250-dc3690f180a2 | -18.07117 | -42.59418 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fd9c64e1-5d18-3828-8bd2-75a623848b03 | -18.07061 | -42.598 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8beec84d-15b1-3a61-9726-443d50cdd639 | -18.06724 | -42.62093 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 67211627-f60a-3698-b217-c326d54c60fa | -18.06668 | -42.62472 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 53a9927c-ab44-3ad0-bbd4-f2eb52870d43 | -18.0633 | -42.62421 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b26793c0-3514-3cda-83c3-afe1d4861e88 | -18.06163 | -42.63554 | 2024-10-04 04:10:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README77.md)
