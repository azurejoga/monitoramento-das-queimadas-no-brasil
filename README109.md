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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd63e97-30d2-380a-b922-b3da7dd6102c | -19.38194 | -42.57252 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.9 |
| 013a427f-288a-30a1-a540-9d8abc4c68d6 | -19.37249 | -42.5703 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| f99914a9-433a-360c-8fdc-493984ccd3c0 | -19.37078 | -42.58058 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| c228401d-e3a7-3ebc-9341-251f7620ddf9 | -19.37017 | -42.56371 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 51921d4c-2b57-3d8e-ab37-79b3d8f48a4d | -19.36851 | -42.57388 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 2867fa99-d613-3adb-9e78-97a7cc735270 | -19.36677 | -42.58456 | 2024-09-27 04:46:00 | AQUA_M-M | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 3bab36d5-cb75-3954-9def-b3b9a6c0200e | -19.15941 | -41.38728 | 2024-09-27 04:46:00 | AQUA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| cf07b1a2-24d3-3aaa-b400-c3e0487e8a78 | -19.15187 | -41.37588 | 2024-09-27 04:46:00 | AQUA_M-M | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 77f17047-0b05-3567-b2c5-0019677c7cf4 | -19.10081 | -43.44904 | 2024-09-27 04:46:00 | AQUA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 299c470f-6eab-3444-a867-3c1c96f2f531 | -18.70585 | -42.09661 | 2024-09-27 04:46:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| e70bea1c-63ed-3b32-b165-b1391d94e244 | -18.70414 | -42.10738 | 2024-09-27 04:46:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| b0d487ed-9515-3a10-8242-d339fe08754f | -18.69817 | -42.08423 | 2024-09-27 04:46:00 | AQUA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| cc2253f3-1bbd-3e4f-9794-42382ccf6cae | -18.48532 | -42.19773 | 2024-09-27 04:46:00 | AQUA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 1deadb26-5156-32c3-b5ee-71edbaefa827 | -18.48358 | -42.20852 | 2024-09-27 04:46:00 | AQUA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| b7118663-f4cd-393e-aa1b-21af10a3da05 | -17.498 | -47.82947 | 2024-09-27 04:46:00 | AQUA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4bf6e743-00e5-300e-b634-d8139bf9715c | -22.95818 | -45.95602 | 2024-09-27 04:46:00 | AQUA_M-M | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 76ec6a59-da01-3052-8974-8d05e8b2b9d2 | -22.95802 | -45.95129 | 2024-09-27 04:46:00 | AQUA_M-M | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 26f57f31-2820-39de-9513-2dd7cc7e7548 | -22.9007 | -44.73468 | 2024-09-27 04:46:00 | AQUA_M-M | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 47f2574b-ff89-3cdf-8429-6d72949a1f40 | -22.749 | -44.78577 | 2024-09-27 04:46:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| ef218f74-d8ea-3e33-920e-d655560d1897 | -22.74648 | -44.80025 | 2024-09-27 04:46:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| c76348b1-b255-3797-8289-998c3b02b213 | -22.74394 | -44.8148 | 2024-09-27 04:46:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 58920e0f-05ea-312a-af29-6e3fc14f4621 | -22.73847 | -44.78494 | 2024-09-27 04:46:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 15299226-72c0-3a1f-aeec-b4060fc03d39 | -22.7359 | -44.7996 | 2024-09-27 04:46:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 05876edb-ab0e-3e79-bf12-98276ccf69fd | -22.73336 | -44.81406 | 2024-09-27 04:46:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 43a40fd2-508d-3927-a438-1f00e2208f44 | -22.64407 | -44.86071 | 2024-09-27 04:46:00 | AQUA_M-M | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| b1a38d82-29ba-3625-a93c-a2c6ed62dfed | -22.59156 | -45.22096 | 2024-09-27 04:46:00 | AQUA_M-M | PIQUETE | SÃO PAULO | Brasil | 3538501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| cb765088-b598-328c-a152-2c6d87fbb2a4 | -28.01428 | -52.40548 | 2024-09-27 04:46:00 | NOAA-21 | SERTÃO | RIO GRANDE DO SUL | Brasil | 4320503 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 127fbae1-e20d-3460-8683-4d763f9f152e | -2.41923 | -48.41042 | 2024-09-27 05:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36199a16-8e9f-30f4-965e-a22dc6bc8086 | -2.35591 | -47.60312 | 2024-09-27 05:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 84e592c3-74e2-3b22-9c13-0023c1c13d9f | -2.35493 | -47.60963 | 2024-09-27 05:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| af264371-6860-33b3-a6a7-012f7860fe01 | -2.35395 | -47.6162 | 2024-09-27 05:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 66416541-8c18-398a-b6d0-05abddf3ce45 | -4.75334 | -48.90136 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e7f2b6e-2dbf-322e-95fd-9b68c6fc7c5a | -4.7466 | -48.90065 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67227277-dacb-3f46-abef-9692f0bdbe46 | -4.56241 | -48.00616 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0fa6b51-a1b3-38ba-832e-5f17ebba9ed6 | -4.56149 | -48.01288 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4509735-0982-3b5a-91e8-cbb931c86ff1 | -4.55687 | -48.01069 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1a9872a7-04cb-32a5-8440-d251104f4282 | -4.19514 | -48.62157 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 581cd2c6-5916-3910-9e00-86432d8e1d11 | -4.19431 | -48.62743 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2207b93-021c-3d5e-bf07-fa3c90dc9c08 | -4.1935 | -48.63312 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c02d9837-0436-3275-ad30-879484ecc6fe | -4.18752 | -48.62659 | 2024-09-27 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1ccf97d5-aa7c-37fa-a48c-bdc341f9f131 | -5.87113 | -48.10137 | 2024-09-27 05:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f78f081b-85cf-32ee-8608-890bb8c31e06 | -5.87015 | -48.10862 | 2024-09-27 05:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15000e34-bb98-36a8-916c-04edcfe5875e | -5.68529 | -49.3189 | 2024-09-27 05:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a701afb-5f14-30b6-bc88-fca22b358294 | -5.62208 | -49.15482 | 2024-09-27 05:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cf2269b-8caf-37b4-880f-789d21cf6b93 | -5.62126 | -49.16076 | 2024-09-27 05:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7f4168eb-b4e1-3be4-b641-7e3ea4fb9f63 | -1.47609 | -49.48393 | 2024-09-27 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67ab45c8-8ec7-3607-ab4b-e52cbc827c79 | -1.4715 | -49.48137 | 2024-09-27 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7589cbc7-9952-300b-a20d-61ab4e385007 | -1.46989 | -49.48303 | 2024-09-27 05:25:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5a99409-8228-311e-92ae-d99a51d0efa9 | -3.32173 | -50.30931 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b366f6a9-ffb3-3ebf-8c35-9ce4d0d04c7d | -3.3211 | -50.31364 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f18d9a61-34d3-345d-8185-a3980e2a11d8 | -3.31507 | -50.31273 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aecb9f21-281b-3e62-a14f-68096d2aaf1f | -3.31441 | -50.31723 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf353c8b-e73f-3ff0-a7fb-c2a5a19f25ba | -3.22561 | -50.32304 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2116e0c3-144f-39b9-a1b3-c5fd40835356 | -3.22495 | -50.32752 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46d6ade8-3b96-3eca-a30a-e147cfb24a12 | -3.14298 | -50.28455 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6a0ad01-9936-3e74-bc82-8858051c2792 | -3.14231 | -50.28904 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a34eeaa-bbc1-3485-8407-0ab72e29f1b1 | -2.80528 | -50.28087 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25ea8a64-9029-322e-a7e4-6eb07d8e572e | -2.79994 | -50.27553 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2631d233-16be-336c-86de-ff3bed62f195 | -2.79928 | -50.27999 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f485e0e2-e330-3c94-a58d-9456f68d163f | -2.80159 | -49.5891 | 2024-09-27 05:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 174dca2e-8713-326d-819f-9bdecf1ba2d7 | -3.57399 | -50.39299 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25644cd8-5150-3904-b3e3-6e6f9ab4c8c5 | -3.57336 | -50.39744 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 23abddf1-7277-3f35-aa25-44383f7b4567 | -3.57177 | -50.39373 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b40f48e7-7665-38f5-bdc3-a900779b5afb | -3.5711 | -50.39825 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cd133c51-094f-3438-b52d-09744df2db9d | -3.56862 | -50.57812 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4177252-b57b-37f7-a682-98a6131fd210 | -3.56836 | -50.37526 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a596c4d-0f29-3741-8f9c-b1b11c58dc02 | -3.56795 | -50.58255 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b41a18bb-fb9c-35e9-9a52-3796fc95dd97 | -3.56768 | -50.37982 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65714eb3-f1a0-3f83-8d55-41b1a289fc53 | -3.56612 | -50.57704 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7b7d0ba4-7ee2-371a-baba-83cb11d697db | -3.56548 | -50.58149 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d192d00a-f72b-35b8-a5a3-6e9c464a51d3 | -3.56264 | -50.57742 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b9e5e72-caff-3185-9b29-8fa56ee965a7 | -3.56198 | -50.58181 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 710e97aa-ffc5-3907-be2c-5ccbd7fa66d0 | -3.56167 | -50.37879 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e5a9c0d-f1d5-315e-9128-58b157db7d3e | -3.56102 | -50.38317 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63c9a6f2-b5ad-3252-ab19-c9fc201d7af6 | -3.56038 | -50.38755 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1401fef-9591-3c8c-9fe8-3eeef55786cb | -3.55565 | -50.37786 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f05e4110-efb5-3502-b432-0a803c840011 | -3.555 | -50.38229 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0151217f-3e4e-3a0f-91e9-47a47331a4c6 | -3.19898 | -51.14523 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cebfe0e3-0436-346a-98a2-5979af17f932 | -3.1984 | -51.14916 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dc7f961-4441-3037-a5c8-855c12852721 | -3.19782 | -51.15308 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3072308-f8de-3f8b-a24c-d09b402f6850 | -3.19724 | -51.15701 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 686e8b34-a2fb-37c6-9380-28b47ba15329 | -3.19666 | -51.16092 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b383dbf-d04c-3c87-9279-999b405e71a8 | -3.19326 | -51.14441 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 515c33d3-9e6c-3b01-ab93-d3d170320e5f | -3.19268 | -51.14836 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a3e59e2-e989-3656-a4c4-6c278faaba91 | -3.1921 | -51.15234 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11c3b476-7c0c-3122-a586-384e1bd214fe | -3.19152 | -51.15626 | 2024-09-27 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 882e568f-4a11-30b0-9e8c-0faec79fbc7a | -3.09375 | -51.29123 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87f62727-680b-3aa4-ad52-9d5f5ac8fe97 | -3.02088 | -51.06201 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e632f522-80d3-3ec2-a33a-e444a50de2d1 | -3.0203 | -51.06594 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ee32ee8-7a84-3f38-acc2-84a8ede3aee0 | -3.01634 | -51.05325 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b929a734-b0b3-3f49-8e0e-0764e66cee1f | -3.01575 | -51.05722 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d8cb2d6c-d434-37a1-9a7e-ae2a96ea1d71 | -3.01516 | -51.06116 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| faf9662e-c1f9-3835-ba6b-88b3b8ba123e | -3.01457 | -51.0651 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c7d55753-d3bd-3800-9831-24ef736518f9 | -3.01399 | -51.06902 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1a38eeae-8918-3096-8285-3930245ba4a4 | -3.01167 | -51.08455 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63e7d03-bc00-3698-ab43-18f36c531b1b | -3.01112 | -51.08827 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8e116ac-e0f6-3245-93dd-01cd197b8ac9 | -3.01003 | -51.05634 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cce03f1d-f29c-3b52-aa99-a2c6a3bf4359 | -3.00944 | -51.06029 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 47760615-b32b-3f5c-a4fe-238f623444d1 | -3.00544 | -51.08719 | 2024-09-27 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b51c9c6-db72-3f34-b39e-8e275fe2a6b8 | -2.87827 | -51.67697 | 2024-09-27 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README110.md)
