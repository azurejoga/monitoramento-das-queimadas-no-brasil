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
| 7a493511-dad4-39ee-a269-07a487226a0b | -12.42675 | -54.47507 | 2026-05-05 04:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 735679d7-1836-3784-b4a2-95b4be95c805 | -12.27354 | -43.50956 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4ed1539e-16ab-3d49-a697-7e4013e83370 | -13.91193 | -47.52904 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 404eac0e-f8f4-388e-882e-a501e025e898 | -11.78855 | -43.61378 | 2026-05-05 04:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44f1f4f7-5d88-3f1d-ba15-c97faab1c14d | -12.26774 | -43.50063 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bebe5405-0e3d-3a13-8ac2-e84b41fdbeb5 | -12.33397 | -50.00742 | 2026-05-05 04:23:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c527fac2-5121-380c-8998-feecfb2d4870 | -13.97606 | -47.52791 | 2026-05-05 04:23:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d25b0c2-d7c0-3d91-9faa-2d6f0deb37f4 | -9.47135 | -47.79903 | 2026-05-05 04:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0775c9e2-33cb-30bb-8118-bdd65d3191e4 | -13.86283 | -49.89513 | 2026-05-05 04:23:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1b51db5-7530-3257-a379-a06db1ccc178 | -12.27413 | -43.50563 | 2026-05-05 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 86860ba5-b401-3818-b0cd-fc2c6a488acf | -12.45257 | -43.73566 | 2026-05-05 04:23:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 691d3e1e-9995-32b6-8cde-4136f66f767c | -12.33773 | -50.00809 | 2026-05-05 04:23:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3a61788d-a8a4-3f95-90a7-c03d2d2bab84 | -13.69003 | -55.67479 | 2026-05-05 04:23:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c30c7165-dc5c-3099-924e-461cc18e405c | -11.79864 | -40.08176 | 2026-05-05 04:23:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3d2502c7-0222-386d-b133-36f303847f25 | -18.49172 | -51.6942 | 2026-05-05 04:25:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d4aa407-a071-3e9b-8865-844522227ebb | -23.36245 | -46.17013 | 2026-05-05 04:25:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bd0da72b-0d29-3de2-9664-270f717f43f4 | -22.34151 | -41.78441 | 2026-05-05 04:25:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 791e2872-4597-3766-9619-b5d1b3f111d4 | -23.49292 | -46.76126 | 2026-05-05 04:25:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| aaccb438-de29-3393-9f6d-944e6f8bfee7 | -16.59108 | -58.24091 | 2026-05-05 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 89df45da-b682-35e6-b218-ca78c5002418 | -22.29285 | -48.78437 | 2026-05-05 04:25:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 03e47520-1457-3a9b-8cdc-e92b1b93dc2d | -22.67722 | -47.47414 | 2026-05-05 04:25:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ef3f3ea-2208-312e-b4e0-168903bc6e93 | -17.79822 | -46.71256 | 2026-05-05 04:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c70df3e-ff74-357c-82e6-cbd3e5d28ce0 | -14.40567 | -56.31785 | 2026-05-05 04:25:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f845522-1634-3b9f-a8ba-d8e93cf9e328 | -14.32132 | -57.73338 | 2026-05-05 04:25:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 062f8ade-7d8e-307b-8025-7c1101dd6173 | -14.31801 | -57.73613 | 2026-05-05 04:25:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8392153-d383-36f6-ba29-cd3b8f855b1a | -21.23201 | -56.92545 | 2026-05-05 04:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cd458f4-f4d8-3047-9112-b26c21ff252e | -18.43313 | -54.70614 | 2026-05-05 04:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7303f534-aa24-3e57-8bb9-76823346517d | -21.53498 | -47.1386 | 2026-05-05 04:25:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f109fdc9-1a58-3170-9cac-4bb983cc0646 | -14.40498 | -56.31707 | 2026-05-05 04:25:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b49c37e6-a1ce-39c7-8217-41d45de106a3 | -22.67779 | -47.47036 | 2026-05-05 04:25:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2913531a-7232-3ad7-ac33-287399d03a68 | -23.364 | -46.16857 | 2026-05-05 04:25:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e87b089d-7973-3c0c-90bc-e545dc9ab7ef | -20.22513 | -50.75683 | 2026-05-05 04:25:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc19a835-d895-31d4-8d66-c75349d0a574 | -17.79878 | -46.70892 | 2026-05-05 04:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 672261d1-70f1-3c8e-8f7d-c67a2b2458b9 | -22.03463 | -48.35961 | 2026-05-05 04:25:00 | NOAA-20 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7d1110e-a5e3-38ec-8c4f-7a22b8271d45 | -22.48515 | -41.96415 | 2026-05-05 04:25:00 | NOAA-20 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 530d861a-8f6f-3c04-a653-22c66661cffe | -18.75571 | -48.06516 | 2026-05-05 04:25:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3dda6f65-3f3f-3953-ac45-e1ae95234811 | -23.03947 | -47.7427 | 2026-05-05 04:25:00 | NOAA-20 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 38cc1dda-6497-3bf4-a301-ea58af244849 | -21.85643 | -48.06827 | 2026-05-05 04:25:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f63b2c7-9154-341e-8d91-173fad088eec | -18.66834 | -50.22584 | 2026-05-05 04:25:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 51f6c4a8-a539-3a8b-8f65-18a58d2f2ad6 | -18.66905 | -50.22171 | 2026-05-05 04:25:00 | NOAA-20 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5391c208-488b-3fa2-8427-a6e5f9a7984c | -22.80109 | -49.33674 | 2026-05-05 04:25:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05cd114f-82ff-31a8-b807-57ffbeef90f8 | -22.03404 | -48.36333 | 2026-05-05 04:25:00 | NOAA-20 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7776af99-4cc5-3dff-9b38-7f31bfa90d29 | -16.59309 | -58.24225 | 2026-05-05 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d822971d-2da9-3c52-a369-415a48f54e2b | -23.40622 | -46.42087 | 2026-05-05 04:25:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b9df3f3-9bba-3499-97e6-18558ef32046 | -22.03736 | -48.36393 | 2026-05-05 04:25:00 | NOAA-20 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18c2ff82-0820-3512-ad1b-945cf5568280 | -21.23226 | -56.92386 | 2026-05-05 04:25:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f33edb76-bfef-3773-8f73-f40c66d46497 | -16.59406 | -58.23766 | 2026-05-05 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e0e64af1-4d87-3e39-994f-0f72801111c5 | -17.80154 | -46.71313 | 2026-05-05 04:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 707ade45-fb21-3ecb-8152-d30c59d47dce | -16.15163 | -58.49504 | 2026-05-05 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9a4360a2-1e9d-3ab6-9596-f5289226233b | -20.71488 | -55.17625 | 2026-05-05 04:25:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33bbd58d-0b1c-3909-babe-cb7e9e68fcbb | -19.834 | -49.7972 | 2026-05-05 04:25:00 | NOAA-20 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43621235-166f-3b63-bccc-6bfd5a5f97d8 | -22.03794 | -48.36021 | 2026-05-05 04:25:00 | NOAA-20 | TRABIJU | SÃO PAULO | Brasil | 3554755 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d2a7d0c-0a02-3474-aa1b-c40a750c5010 | -22.6733 | -47.47733 | 2026-05-05 04:25:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1997efc3-8d5e-3267-aa09-c373a2e36799 | -21.52829 | -47.13742 | 2026-05-05 04:25:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e2f7803-5e41-36f0-abe8-257127427e31 | -18.23309 | -54.59193 | 2026-05-05 04:25:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea469fed-428f-3dcf-a45c-555a2674bb89 | -14.40569 | -56.31346 | 2026-05-05 04:25:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4d4541c-4ea5-3cd5-82e6-dd8adc5c96aa | -22.49 | -41.96035 | 2026-05-05 04:25:00 | NOAA-20 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 28094c22-8e0a-3dcd-abcf-2826974f40a9 | -14.32033 | -57.73806 | 2026-05-05 04:25:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66bb2820-b91c-3d90-81be-e44a655e060d | -21.53164 | -47.13801 | 2026-05-05 04:25:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f459e4e7-974c-3eab-a154-32121cc43f01 | -20.7157 | -55.17941 | 2026-05-05 04:25:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af4fd441-c0e8-3075-9eb3-a447cb1d7b00 | -22.29013 | -48.78003 | 2026-05-05 04:25:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| f221948e-d0c1-399c-92ce-e270d9e22c0c | -21.19354 | -48.81596 | 2026-05-05 04:25:00 | NOAA-20 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 88123de4-b902-32ef-9e6f-ef2f81436045 | -16.59695 | -58.24224 | 2026-05-05 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8cb2ba63-8826-3947-87c6-44eda7872051 | -14.40641 | -56.31426 | 2026-05-05 04:25:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b68cea8e-ada6-3c9b-b81c-0d62c47e8f6a | -22.28954 | -48.78376 | 2026-05-05 04:25:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 973673b4-3b20-3b8f-96bc-3cf370b5520e | -22.80442 | -49.33738 | 2026-05-05 04:25:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 269d31b9-7a51-3f21-bc8c-fe0c33dc3cd2 | -16.75637 | -51.87056 | 2026-05-05 04:25:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a742a100-6517-3bd8-9322-6e2bd5f3715d | -21.31939 | -48.68969 | 2026-05-05 04:25:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32fe5be5-9a5a-345b-8773-b8d1bf2efc18 | -20.94211 | -45.42062 | 2026-05-05 04:25:00 | NOAA-20 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac276fdb-c02a-33f6-8db1-a782aa710166 | -22.67664 | -47.47792 | 2026-05-05 04:25:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32016ad4-5e7a-3e01-a40a-2aefe78d6dcd | -18.32044 | -54.53086 | 2026-05-05 04:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cc39ead-8577-3a09-b19a-7347df7cb3f4 | -21.85748 | -46.97386 | 2026-05-05 04:25:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f8f13a8-5ce0-3eb3-9894-d83ab8916f2a | -21.09407 | -47.79768 | 2026-05-05 04:25:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b3e5b41-1ed2-3b6f-a1b3-2c6ecfbd8fc4 | -18.43217 | -54.71091 | 2026-05-05 04:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a928cbfa-a1ae-3443-bb29-21fa184ee507 | -17.52326 | -46.71511 | 2026-05-05 04:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7182343c-8cc1-3d2d-9dcd-5d2a3beb328d | -22.80048 | -49.34051 | 2026-05-05 04:25:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad622a32-6897-3b56-a0dc-99be025f1a3b | -18.49259 | -51.6894 | 2026-05-05 04:25:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cca5d754-cc29-3bb2-b2d7-8eb25154634c | -22.70172 | -43.36195 | 2026-05-05 04:25:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32484fb0-3651-32a1-b0e8-91fc472caf6e | -18.43408 | -54.70138 | 2026-05-05 04:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b0c777a-ed58-3be1-bb20-3e07f4b15925 | -22.48567 | -41.95973 | 2026-05-05 04:25:00 | NOAA-20 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 629ad743-0801-3d73-96b6-aae27c0cf0dd | -21.49785 | -48.65617 | 2026-05-05 04:25:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfa89043-2368-374b-92a3-02123e7f049c | -18.2329 | -54.59032 | 2026-05-05 04:25:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a9a2a15-3b40-36d5-8e4b-1e2e16ed7b7e | -18.43576 | -54.71669 | 2026-05-05 04:25:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c2c9d9d-78c9-39c8-9e4c-787aa152894f | -21.52886 | -47.13364 | 2026-05-05 04:25:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ce56f55-075e-3ff0-a077-cd15a9c5d127 | -23.08416 | -48.61558 | 2026-05-05 04:25:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66f40890-66a9-3f9a-8d89-335229685b19 | -23.77261 | -49.15454 | 2026-05-05 04:27:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 051707a3-14d7-3afc-8d55-ebe7c58ae3d4 | -21.95286 | -57.59408 | 2026-05-05 04:27:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9102c952-c3fe-37c0-93f7-5909f6aa05e9 | -24.0666 | -48.9285 | 2026-05-05 04:27:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee3202b0-8d96-3322-9b3f-f02974b189b7 | -23.55883 | -47.51831 | 2026-05-05 04:27:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6de48504-6b0c-323c-8322-06dc0051a6dd | -18.6643 | -50.2255 | 2026-05-05 05:10:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 140.5 |
| 02dc8355-fa9f-30d2-91bc-fd0358798977 | 2.73367 | -61.36148 | 2026-05-05 05:10:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8ace671-34d5-3b58-8612-707bf4662267 | 2.35939 | -61.06125 | 2026-05-05 05:10:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4317f216-d960-3ee3-bad6-3fb97c02401e | 2.73304 | -61.35732 | 2026-05-05 05:10:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 920bcc64-728b-38ba-9af4-55e48d37830b | 2.35882 | -61.05749 | 2026-05-05 05:10:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae01ec23-6996-3868-8610-d57010d61eee | -11.12893 | -45.12262 | 2026-05-05 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 075899c6-4268-3a64-99cd-80d8ebe74172 | -10.59257 | -46.67104 | 2026-05-05 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09bf63ac-3465-3889-afc4-88f7e187e523 | -11.61362 | -47.10098 | 2026-05-05 05:12:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77525349-54f2-375d-aa68-c87631dc6f7b | -11.60952 | -48.05867 | 2026-05-05 05:12:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58298630-2bec-3ddc-831d-b37eb143f28a | -12.34026 | -50.00452 | 2026-05-05 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e8105f92-a311-3e12-8cb8-2f74e600077c | -7.52631 | -47.17276 | 2026-05-05 05:12:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)
