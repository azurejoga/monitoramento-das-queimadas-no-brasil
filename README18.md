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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a856ea5-92e7-3995-8315-61225e5300fa | -4.71487 | -45.96981 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee4ea3bc-e300-3e4d-8b7d-0f9aa3e0fe7e | -4.71173 | -45.8464 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc9c4dda-081e-32d8-a895-ecb6fc25b5f8 | -4.71159 | -45.84344 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 314c2e53-516e-30a9-91c4-6fe25699e464 | -4.71092 | -45.85149 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abae8ff5-c147-3875-87b2-af165cfeb423 | -4.71075 | -45.84847 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8515674-8763-3a18-9303-b4ca4f4b300b | -4.70858 | -45.84083 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7a608561-e162-36f3-8bcd-4de5cec80b42 | -4.70778 | -45.84584 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 51948250-188e-3ce5-8654-1521ff66c168 | -4.70763 | -45.84288 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ecb96633-e6cf-3b4e-8dbc-0dcb85fdf117 | -4.7075 | -45.96504 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca4056d0-dc61-3fc2-bad9-ec90da4843dd | -4.70696 | -45.85092 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a482654f-f440-3625-b12e-4cba0a21bde4 | -4.70693 | -45.96848 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cbf776f-4f52-39aa-bb6f-7530ef700b07 | -4.70679 | -45.84792 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a5cd317d-e44f-3411-aff5-b32cfcd1f84f | -4.70463 | -45.84026 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 71d6f432-bd62-3e94-94b7-0a4569ab8abd | -4.70382 | -45.84529 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f390389d-91c6-3d13-9604-9dcce2571ce7 | -4.70368 | -45.84232 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b5ac40a9-18d7-32e4-a16f-6d0d86b73298 | -4.70283 | -45.84737 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1fe41e6e-4242-3062-8756-7da5dd8ca550 | -4.70068 | -45.83966 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c1c024c-ebee-39e0-8014-4e8497b9b537 | -4.69986 | -45.84475 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 998f0f74-2e5d-36d8-beb7-42bc8acfaffa | -4.46571 | -45.89865 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecd5623a-6006-35d0-b6ea-bf8d6e51a0fa | -4.46227 | -45.89469 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 824abc59-3a62-3e08-a579-0401d0a41116 | -4.46171 | -45.89814 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67f63d0a-8e55-3a7a-a21f-820d7662165f | -4.44059 | -45.70506 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 54ff5256-cc3c-31c7-ad1b-fe1c540e1a72 | -4.42544 | -45.97051 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a901e33b-81c6-3861-9721-3a8dfc90ef92 | -4.42147 | -45.96975 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1144aa8d-94e5-3fa6-9650-de6f12babcb6 | -4.42091 | -45.97319 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d1bbcfd-2c95-3b48-bed5-9a280f0bd269 | -4.42034 | -45.97663 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efd9a933-760d-37d2-941a-554f2bb92a1d | -4.41693 | -45.97245 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5e81934-2dfd-3b84-8e4d-24def111a55b | -4.41636 | -45.97594 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 842af647-5e86-3c92-beff-068970e08ef3 | -4.39341 | -46.16645 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f33638d1-b530-3c44-8582-1395a7c0d850 | -4.39142 | -45.80639 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 86915935-8dcb-399d-8da6-75743f53f844 | -4.38933 | -46.166 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1248f51-e5dc-3351-bf8e-1ce115500cba | -4.38848 | -45.80378 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f93e0781-6e7b-3c7d-b0aa-7aa08d55e7c9 | -4.38836 | -45.80044 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c1d938d8-2b6b-3447-b6f9-d9111dbcfcbc | -4.38748 | -45.80568 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 9154a28b-3d2e-36f0-95ea-394da5752384 | -4.38678 | -45.83978 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ef3a78d3-2e2a-3ab2-9321-862a8531b39b | -4.38639 | -45.83649 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ad29d5f-ad1c-301a-944a-0e3b26200fa6 | -4.38555 | -45.8415 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59afd00a-72c1-3815-bbd6-01b554afd7a9 | -4.3844 | -45.82922 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc6ab58a-7d58-3ebc-a74b-2e7fcafbd7ff | -4.3836 | -45.83423 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3478d25-648c-312c-af04-ce2ab34b8ba0 | -4.38324 | -45.83099 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fcf10f99-db4e-381e-b0d6-39f670b42c9b | -4.3828 | -45.8392 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d54013e9-f73d-3578-8b7d-f27170eef88f | -4.38241 | -45.83596 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35338fa8-1b87-3845-8eb8-abff0b4fbf3b | -4.38158 | -45.84091 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee95d79b-8a3a-3abd-936a-71ee6ccfa2b7 | -4.37883 | -45.83866 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67572c0a-5182-37a2-8b82-b0b62ca21b5c | -4.37804 | -45.8436 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fd8726c-7450-30f1-acc0-0d4146b63309 | -4.3776 | -45.84039 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 949707a8-c56d-3175-9909-553ab2568a06 | -4.37677 | -45.84534 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10286617-93a8-371c-acc7-f0f67d02157c | -4.37484 | -45.83817 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a43ff62d-7c58-3503-9818-9db7b003d674 | -4.37404 | -45.84314 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cec70f72-3080-3b15-bd7f-9a78b9cbf72a | -4.30463 | -45.9688 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 840fc0d6-77c5-3268-af53-3437e11fcef6 | -4.30119 | -45.96476 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edae7040-c606-3e1c-970f-8b884fa8bad0 | -4.30063 | -45.96819 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5522d955-430f-3aab-87a3-2b86a3c40f92 | -4.1933 | -45.74178 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa4672a0-8496-323c-b2d8-fa9b43f2be69 | -4.19321 | -45.73857 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f72e4be6-0dd2-359d-8508-1f6299f917a4 | -4.19249 | -45.74684 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 987e1fc9-c93a-3e47-b184-6b581b9c0968 | -4.19237 | -45.74363 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73de0a6e-7359-3a9f-baf5-c8d9b173b731 | -4.19152 | -45.74871 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01e9a2b7-80c2-3cc0-9836-72cf61ea4803 | -4.19097 | -45.73098 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eef6b91-ea44-3e64-8201-960694237b28 | -4.19016 | -45.73606 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 139e453d-ad83-384e-a52e-b05eb832f1c5 | -4.19011 | -45.73286 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c801827d-75db-38d4-91a2-485ec9517233 | -4.18935 | -45.74112 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a40fd9b-75b6-3d9e-8b2d-88db9257c284 | -4.18926 | -45.73793 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ab9f1c1-7082-3aeb-8643-ca3c28995524 | -4.18855 | -45.74619 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0067f05e-2c78-3d05-a249-1c2797b7f585 | -4.18842 | -45.74299 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a36e8ca9-0399-3408-99d6-324f8291364f | -4.18758 | -45.74807 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0e00a26-b7e7-384d-b4ac-80a1a478e162 | -4.1854 | -45.7405 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 747b0971-2fa4-3d6c-8776-aba3c24cdf9c | -4.18447 | -45.74239 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab54222c-926f-3371-ad3a-5bcf3c9b7904 | -4.17499 | -45.8236 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae373f4-3d04-3877-93e9-af3c7fe2e3ca | -4.17442 | -45.827 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4569a1e-7211-34ff-a153-b5afe2b8181b | -4.0441 | -46.03025 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cbeb9a8-eeec-3c86-80ff-ebeb48d6cfe1 | -4.01547 | -46.02163 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04537f4f-96ea-336d-81e2-0eb73f7d6cea | -4.01493 | -46.02499 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3e4c415c-7751-31cb-8f14-d9ed4ab2b6c6 | -5.62864 | -44.96103 | 2024-10-20 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9fe95ec-c29f-38df-812f-18b83892f923 | -5.38053 | -45.12076 | 2024-10-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7c82b63-37ea-3ce2-98ad-6d1bc9df5ed9 | -5.37888 | -45.12177 | 2024-10-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89ec1f6a-b8ba-3723-88a1-cfba10ee928a | -5.24333 | -45.86798 | 2024-10-20 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55c3eafc-4fea-3435-838d-4981cd3e3f05 | -5.24307 | -45.87095 | 2024-10-20 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe26ced-92e8-3612-a7b1-9a29f278783f | -5.21742 | -46.09536 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4714a3e6-c6b9-34a2-a0a3-552dc547531b | -5.21685 | -46.09875 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b7a65240-c79a-32ee-b141-e19086398ead | -5.21628 | -46.10215 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0472c06f-0bdc-3220-93f5-7beb1dfa82fd | -5.2157 | -46.10559 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d02d36ff-08aa-3500-8c62-ae79a5a83cd6 | -5.21444 | -46.09723 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9dbe5427-7b09-314a-a740-74e3c3afb688 | -5.2139 | -46.1006 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b77ecca8-3d3d-367f-858c-0e9a3b313d23 | -5.21335 | -46.10396 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 094ba134-8f27-3df1-acc0-451edc97578a | -5.21291 | -46.09791 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4e0bbf68-2a7a-3aba-972c-83ad0bd828ba | -5.21278 | -46.10753 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15dc71df-86b6-3f6c-b075-eb3f1fbf6198 | -5.21235 | -46.10126 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf759012-0847-310c-93a8-05bbbeccf172 | -5.21177 | -46.10468 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9c935bd-ace1-3339-af5b-539009922cea | -5.21117 | -46.10825 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 396ef245-7617-348d-823d-0dd4df7c6842 | -5.20938 | -46.10327 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a21eac1-2434-3479-9415-dec4216adb4c | -5.20882 | -46.10677 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44873602-fcb0-3110-94de-c290910674d4 | -5.19254 | -45.73768 | 2024-10-20 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 752edf75-e3a3-369b-91dd-e1c275cba17a | -5.17585 | -46.18384 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a4231c6-66ec-3353-a5f9-e630fd3a03e6 | -5.17529 | -46.18724 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bffdafd-55ed-31bc-8319-0eef8d39ef0f | -5.17451 | -45.57206 | 2024-10-20 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a2d9299-ddde-3d2d-a421-4800ceff3fc6 | -5.17183 | -46.18328 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 306552bf-121d-3005-be4e-a5b872037531 | -5.17128 | -46.18666 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eb5e1af-b9a0-3319-b72c-6c6c6bbc8cb8 | -5.17067 | -45.57139 | 2024-10-20 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f433cb6-63b7-3403-a741-7a014039db3b | -5.13762 | -46.11715 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4609d7a-90b7-3a43-88b4-c9e264f50937 | -5.13131 | -46.1551 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README19.md)
