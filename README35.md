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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc94d3da-750b-31f4-bcc8-2db2b64afe1d | -5.73185 | -43.28748 | 2026-10-03 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93a498cf-8610-32dc-a4e6-b52e2b074451 | -6.25124 | -52.68293 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8b112ce-ff4d-352a-98d3-70d33574ba0d | -1.26844 | -54.56517 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3df71fa7-5bf3-3738-8b89-63360308a708 | -3.29318 | -53.85462 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b7ab3cb-ba6e-3cc9-969c-1f968fd0671b | -4.56911 | -46.57986 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a94af63-2fe3-3ecb-9322-c006b107c1e6 | -2.93927 | -54.18856 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1864ad1b-e5d8-3d76-af92-7aadd0a9fa3e | -5.8717 | -50.15828 | 2026-10-03 05:16:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75e92bdd-361c-3871-a048-7aaf8978aae8 | -5.85418 | -53.47967 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2cd98fd-1ade-3a09-b3f0-de0c11d6da45 | -6.01464 | -53.54187 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e391651a-e7f1-3161-9903-ab0ca067e37e | -5.94417 | -43.65251 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f446dfa6-8fdb-36dc-8024-12b73a903ebd | -3.28476 | -53.84239 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bf6f8f6-3846-31d6-b9ad-d2306ed977f1 | -5.88911 | -55.48576 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 33674b0a-fb58-3c2d-ad91-92c6ed8293c9 | -3.28252 | -53.83475 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 58d7e4bf-215d-35c6-9588-08378214b14d | -2.86898 | -50.31656 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c664fc8-bed2-39df-84fb-1871383048c3 | -6.74237 | -44.13727 | 2026-10-03 05:16:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bcf57927-7bad-3c8f-a976-a60867e3a68d | -7.4678 | -55.0134 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c23e311f-1bb1-36fd-9066-9ba3b11d470b | -1.99417 | -49.65368 | 2026-10-03 05:16:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abf60979-2865-3e24-8632-47d883d446e3 | -3.88183 | -49.68424 | 2026-10-03 05:16:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ddc4db89-a057-376d-9633-342360c41cc7 | -2.97349 | -53.27106 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 673d6138-8c71-3396-a671-c54fab0f00db | -3.12167 | -53.75094 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29710be4-7409-3d54-9fd7-f97f2852a81c | -3.01975 | -53.88802 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c1bf763-af67-3818-9d51-42c496626e0c | -3.29929 | -50.32328 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33db1c83-f9c1-3acb-abd9-44fdf759d83f | -4.29882 | -50.78114 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8c9c0da4-ea79-33d0-a3ae-8cefba2a0ccc | -3.71903 | -54.64606 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a79c1de4-21bb-34ff-9083-161ec19fcdb1 | -3.51289 | -54.60265 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e0bb48b-3166-3310-87b7-a1257ecd1447 | -3.11846 | -53.7435 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6abf3076-605a-3e48-8970-d2f935f8b7ad | -2.97748 | -53.26794 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3e4f02d-5d7f-3237-9aa2-1e8311d628c8 | -2.97495 | -54.17261 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5221e864-da8d-3852-8b01-158716fa2d01 | -1.62019 | -55.14137 | 2026-10-03 05:16:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e096f3f-077e-3d4b-8be0-89babac842f9 | -3.56072 | -53.06009 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9694fe7a-0e7d-3cbb-8864-4de8f904c7fc | -2.33552 | -51.94247 | 2026-10-03 05:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3e763f8-a63c-397f-869b-5fc597c49d33 | -4.81071 | -46.82147 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b56f9c69-2a95-3b37-9b2a-f6570590b5a5 | -1.26512 | -54.56465 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49d4a4ca-192d-33b7-8b4c-599401d764a5 | -2.89132 | -54.14527 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 619ce9cc-daf1-33a9-8082-14302c243a4e | -7.46776 | -54.99154 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 974cd5b4-ed3b-3fc9-bd7d-f1d54014d5f4 | -2.90746 | -54.12989 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 555d393b-01c0-3d4e-a70a-1fa2d62705b4 | -4.26343 | -50.7505 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3faa8975-3ae9-398f-93f9-479af5eb711f | -5.95131 | -43.6483 | 2026-10-03 05:16:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c041b486-91ff-3187-84c3-e272463c32d7 | -3.09778 | -51.09851 | 2026-10-03 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc378c3f-ffaa-3e8f-a089-c0d773530f19 | -2.92065 | -53.9377 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4caf731-03bd-372f-bdaa-84d2b044afdc | -3.00342 | -54.2308 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 221d7217-a441-3d7b-8669-8704d39c0ad4 | -3.15951 | -54.07917 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb2e65ff-c2a4-3c6d-85f9-e55eed57755d | -5.25611 | -55.9185 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c938c408-9d9b-3a5c-8426-dac63fc75f57 | -3.64037 | -55.50256 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4227a85-c535-319f-bd81-86c4d59ce2af | -2.97007 | -53.27055 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc5e1586-e30e-3e4b-99aa-83f07342834e | -3.17424 | -54.08557 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 806d8c16-4112-37c9-b07d-8816ef7662f6 | -5.55912 | -43.96308 | 2026-10-03 05:16:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61c7c47d-4826-3d20-a11a-32f52d470e93 | -3.50442 | -53.20078 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 09f20357-2599-3111-b044-e1d1930a7985 | -6.50056 | -41.74261 | 2026-10-03 05:16:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e4ff1c16-c9dc-3a1d-b0cd-42c534d07ff7 | -3.24881 | -54.51527 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| decd1425-7432-34c0-97dc-dd1a38cdba0f | -6.20543 | -53.21701 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f644f961-cfd2-3b1c-87a6-2b89d4b5652b | -2.9576 | -54.07313 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95e184a1-b929-3310-ba7f-61b31b5b41a2 | -3.7793 | -52.14172 | 2026-10-03 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9590c2a3-2d47-3fac-a2fa-dd548d249587 | -2.92527 | -54.10398 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec12db48-7700-3156-b8ab-a2d7559ab527 | -5.71721 | -46.20305 | 2026-10-03 05:16:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecd30039-84bf-3da5-81d6-775f3fb7c992 | -3.13065 | -53.73774 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 14e15ead-6f21-391f-a2c0-f4eff057c0b2 | -3.07467 | -51.27264 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 783be51e-5287-30d2-9be4-bd15f5d43e20 | -6.09673 | -47.65974 | 2026-10-03 05:16:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d92d8e7c-4360-3371-a590-6d06b7a04fb7 | -2.15472 | -47.75144 | 2026-10-03 05:16:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 486edaad-1d4a-3a4c-9e62-522610c7a7da | -3.81842 | -52.20454 | 2026-10-03 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2168b23-8c0e-3c40-bfa8-6f88f2343872 | -3.28532 | -53.83884 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be6ede8c-fef8-3f41-a401-645a8bd5cef7 | -3.76352 | -55.53614 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b54b86a-0328-361d-911f-e35668a7744b | -2.95705 | -54.07664 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfb73fee-9547-35b7-92f2-48af77f8eaa6 | -3.01842 | -54.20095 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f0f0af3-378e-3992-9668-12190fdcddfb | -2.89074 | -54.12727 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bf853e4-6b43-3bee-8638-029d8ee14612 | -3.28196 | -53.83831 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f7810f9-7325-3929-ad2c-718755d11439 | -5.59442 | -44.90934 | 2026-10-03 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 858a8647-5b7c-31d4-b089-dfe6d6065177 | -2.88964 | -54.13427 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5244feb8-17d3-3a39-b1c8-422e37e959ad | -4.79026 | -55.71677 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd1dd0a9-b9c7-3b42-be60-cf6ef71a31c7 | -4.98931 | -56.14811 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bee9568a-7282-3407-91ad-5a1211ce93d6 | -3.29543 | -53.84042 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f6c4eb1-3aff-32d2-a350-538e48389356 | -4.78582 | -55.72319 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef34c38-8afb-3b09-81e6-13f85c4da509 | -3.07689 | -51.27909 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9503180-dda9-375b-bd72-a02275fbfd25 | -3.13123 | -53.75608 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 113a0400-b1ca-3d31-ad5a-8f9c937e24e9 | -5.85878 | -53.47292 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa60a7ae-af67-3414-ad7b-701bde56e8ad | -4.14781 | -53.94601 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 562bfe52-d667-3f1e-8556-e7e8c60ba5a1 | -1.28039 | -55.40884 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da951d09-ed08-3c81-be7f-cf88908b3a92 | -3.51205 | -51.16255 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2ba2a33-3417-30d1-9b44-2f537b429c5f | -4.41154 | -49.96255 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa6dd8fa-35e5-353e-9630-cd4f7c39d0ca | -6.31598 | -43.34789 | 2026-10-03 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ed5c4a80-4a75-30b1-8805-17368be6fad4 | -1.37219 | -54.63813 | 2026-10-03 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0337457-51dd-3877-9fbf-c8603821a436 | -3.12419 | -48.67468 | 2026-10-03 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40fd0ba9-c510-3080-a9cf-80cb1cdcfdd3 | -6.33418 | -43.36229 | 2026-10-03 05:16:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 681c478d-d660-37b0-99a0-9a6cee454f71 | -4.12357 | -55.01519 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fff23f6b-7d73-346a-8f87-36986cfca69c | -3.00967 | -53.88645 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cb80b5c-be8a-3f9e-8156-1d2d7138733d | -2.88343 | -54.08667 | 2026-10-03 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb1e7730-bfc6-356b-9478-31e34c26e2b1 | -2.95919 | -54.09849 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 195c14b5-11a4-30fa-a451-98bf552244d9 | -1.59909 | -55.14517 | 2026-10-03 05:16:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17ea8a9b-2f43-3db0-a1c4-4389be7c0e6c | -3.12839 | -53.73008 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 087ce9ed-9381-30b2-a2fb-adf0de1c0d43 | -3.1273 | -53.75911 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14b558b0-e0e2-37a7-89de-b65a4b23687f | -3.31925 | -51.67575 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20a24853-573b-351f-b46c-82cac09be55e | -2.93144 | -54.15155 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21cfafa8-c56d-3976-8d9b-a2bda0a7ae06 | -3.17204 | -54.09963 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 586b9024-b241-3e80-ab51-c74416f4930b | -2.46396 | -56.06854 | 2026-10-03 05:16:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b40200c-11b3-39fd-bb60-993c2a3c1b24 | -3.1815 | -54.08307 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd24776f-29e7-37f6-9d0c-1c96a1816409 | -3.29655 | -53.85515 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c084278-da7d-37a2-a2ea-1beb551c747e | -6.20773 | -53.22538 | 2026-10-03 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3c59d3f-3635-307c-9054-91c9d38f01bc | -3.00373 | -54.73911 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c53f2c04-c8f7-3d79-9b1e-c75b52b93a1f | -6.39923 | -55.23492 | 2026-10-03 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 212903a7-6085-38ba-ac45-ab7cc3b68023 | -3.16676 | -54.07671 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README36.md)
