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

## Dados Diários - Página 184

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b784347-89b9-37ac-b0df-f752ee542d91 | -16.32791 | -45.64523 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 39.1 |
| c4534de2-d010-3fc0-8a1b-38018cd29d31 | -16.3247 | -45.67841 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 176.4 |
| a2708aef-2e7b-322a-8f9e-28fad069fb0e | -16.31519 | -45.67206 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| c539e6df-9fe9-3f48-90f5-c5d0433f42bf | -13.30153 | -46.32301 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 979f2128-0cd6-35f5-8873-f8c1e6593780 | -13.23767 | -45.68007 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 921b59f6-24b7-31f9-bcfa-61a5cd5ae564 | -13.23538 | -45.68554 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 6d938d44-db4d-3558-9252-525ba384b10b | -13.23431 | -45.70965 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 8e062391-9581-3903-adfd-db10c10873cd | -13.23224 | -45.71511 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 246.0 |
| ce6a41f4-e9b2-3d31-9a01-1b2f4ab5c75b | -13.2233 | -45.65402 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6e7a5bf1-07af-3927-b1e8-c640756f49e3 | -13.22245 | -45.67842 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 6706dcec-6db5-3fe9-b66b-efd4b860a7f9 | -13.22018 | -45.68382 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 3146e7e8-3557-300b-95b3-a177724de413 | -13.21914 | -45.70793 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 594.9 |
| a1ee3814-e427-3e31-adf8-c5e05f6ddca8 | -13.21708 | -45.71338 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 306.6 |
| 0440bd94-299c-322f-9958-345502237e53 | -13.21056 | -45.64692 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| 8591593c-586a-303c-a2da-f73e19331428 | -13.19532 | -45.6452 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e996fff0-c661-32bd-9128-09ebcc4758d9 | -13.18477 | -45.4847 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| cf9b1fa0-10f3-3231-821e-3c95ad8ba851 | -13.181 | -45.49068 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 448.2 |
| 3447bc70-0666-30e9-a9e2-cdc98373adc7 | -13.16936 | -45.48288 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 350.0 |
| f5c8a0e8-6f11-3474-8200-0ccd69f9af56 | -13.1656 | -45.48876 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 293f6459-a0be-3ce9-874b-073eeb446e44 | -13.15738 | -45.45034 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| b4d8f115-0991-3563-8dfc-a1bce10e15f2 | -12.96258 | -45.29074 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d5817e85-6e13-33bd-8ee7-e432f6dcc369 | -14.57824 | -45.70339 | 2024-09-26 13:10:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 25f4f310-966b-330f-8ba4-046c2e9f3c01 | -14.57407 | -45.70967 | 2024-09-26 13:10:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 371071f1-47eb-313a-8a99-2dd447c80e17 | -14.56608 | -45.6707 | 2024-09-26 13:10:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ba4219b1-55dc-3592-abaa-e3e83d4e672e | -14.5628 | -45.70145 | 2024-09-26 13:10:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 25f15285-d2ea-34fe-9835-3b5c5f544111 | -12.79296 | -47.23499 | 2024-09-26 13:10:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 680c41ed-4839-3fab-8d32-6e3cb7a8dfc1 | -14.19207 | -48.19163 | 2024-09-26 13:10:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| fe19e814-3405-3a36-98fd-b6ce8e6fc961 | -14.17943 | -48.18994 | 2024-09-26 13:10:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| a4444ec3-16f7-3b46-b993-3d8dd9c89c85 | -14.15802 | -47.81829 | 2024-09-26 13:10:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 13a9db99-dfa9-35c7-bf80-7c7be7d12d2e | -13.79728 | -48.12119 | 2024-09-26 13:10:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 802bc8ed-9c2e-39c0-8ba1-e8ca9aea7dd0 | -13.79124 | -48.06193 | 2024-09-26 13:10:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 7a23f271-e27c-3ec0-a35d-04d148f56f54 | -13.78921 | -48.07961 | 2024-09-26 13:10:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 091f9d0e-b305-39ed-b9bd-62b880866ae0 | -13.78906 | -48.07331 | 2024-09-26 13:10:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fcbe1bd7-10f7-3cab-8b22-7cec6d2eac6c | -15.17105 | -48.81586 | 2024-09-26 13:10:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 85c9fb93-929c-3b47-b2cb-54c8bc151eb7 | -13.14823 | -48.52702 | 2024-09-26 13:10:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6a7beb02-b84a-3068-8b32-e57433d69234 | -13.14627 | -48.54306 | 2024-09-26 13:10:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5396fba3-f35f-332e-8a56-25849ecd4a63 | -12.51603 | -48.91991 | 2024-09-26 13:10:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 570cb84b-7f22-3fb6-8739-46a47af22b20 | -12.51408 | -48.93589 | 2024-09-26 13:10:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 05de810e-3fc6-3fe1-a100-dbcfde8bc2d3 | -12.50441 | -48.91838 | 2024-09-26 13:10:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| ac1d130c-62e9-3ec6-bf8c-8330a6e04a4e | -12.50247 | -48.9344 | 2024-09-26 13:10:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 19aab6d4-2428-3de1-a4de-23bc96f50e58 | -12.49279 | -48.91687 | 2024-09-26 13:10:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| b7872ff7-a41d-3094-a7b5-e3b4a917e2b8 | -12.49086 | -48.93294 | 2024-09-26 13:10:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| cd4a5f5b-a3a4-374e-b3e2-581bc10530c1 | -14.82938 | -48.86674 | 2024-09-26 13:10:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 41c94a86-6a8b-3a2e-af14-e624fc701815 | -16.36905 | -49.4748 | 2024-09-26 13:10:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 28ca747f-a703-3b33-ae2b-68c7cda66b00 | -16.36559 | -49.46354 | 2024-09-26 13:10:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eb20bae2-e2ed-3832-b998-32d7a789085a | -16.36365 | -49.48049 | 2024-09-26 13:10:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| edfa62e6-86df-30a6-80c4-57d8f8f7e943 | -20.78724 | -51.28222 | 2024-09-26 13:12:00 | TERRA_M-T | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 621f001d-806f-3bda-acd6-6fcf1b46d39d | -20.78549 | -51.29703 | 2024-09-26 13:12:00 | TERRA_M-T | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 31799125-b4d6-383a-ae3b-b661e71d2204 | -20.77621 | -51.28099 | 2024-09-26 13:12:00 | TERRA_M-T | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 0200289c-6546-36ef-bf7e-6049e368cd5b | -20.77447 | -51.2958 | 2024-09-26 13:12:00 | TERRA_M-T | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| 7d707010-4784-3bfd-a07f-97bc0598adf4 | -20.76346 | -51.29444 | 2024-09-26 13:12:00 | TERRA_M-T | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| d3396eb2-d44e-350b-8626-651ca144e799 | -21.30154 | -50.97851 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 1581fdc1-9ffb-32fa-9ded-15747be71f4c | -21.30134 | -50.98809 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 370.7 |
| fa2f0a94-7c07-3d0b-a922-46141bfd4ad1 | -21.29978 | -50.99443 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 765.3 |
| d1b7cb63-baf6-3c70-8e10-694ed3f704eb | -21.29946 | -51.00409 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 311.4 |
| b48fa83a-6deb-35b8-af08-68f592e7e541 | -21.29802 | -51.01041 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| ea437a70-7db5-3520-ab88-f44f97c3b90c | -21.29018 | -50.97711 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 6c7279d8-b1a7-3a35-b363-d1b12bf25303 | -21.29 | -50.98667 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 450.0 |
| 8338672f-918d-3a5b-b17d-f6483e67a11a | -21.28845 | -50.99296 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 443.9 |
| 2df03450-32d3-3adc-b50a-4ef5a1f5165e | -21.28814 | -51.00268 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 490.5 |
| bb73f4af-8951-3285-992e-d8b166952bbf | -21.28669 | -51.00904 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.7 |
| d70973e4-3db2-35c5-b9ed-df8f0d4c4034 | -21.27866 | -50.9853 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 171.0 |
| ae7d045f-a5de-3353-abd6-3dd283287497 | -21.2768 | -51.00129 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 273.6 |
| 173082a1-a6ef-310e-b448-c01f0b8094b3 | -21.27496 | -51.01723 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.2 |
| 01b61c9a-cc89-38a1-9cd6-79e431f35a2a | -21.26546 | -51.00001 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| d42e1a4a-4675-3dd4-a10b-975b2913a460 | -21.26364 | -51.01589 | 2024-09-26 13:12:00 | TERRA_M-T | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |
| 9429d49c-4b5c-3c6b-8bd4-870a92f15330 | -21.39344 | -50.12245 | 2024-09-26 13:12:00 | TERRA_M-T | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 408.0 |
| 90225104-6e8a-346e-a3b9-a2ff78794a6e | -21.38928 | -50.11541 | 2024-09-26 13:12:00 | TERRA_M-T | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 549.5 |
| b41f68a8-ada9-32cd-8291-de2f1fc8f9d0 | -21.38726 | -50.1336 | 2024-09-26 13:12:00 | TERRA_M-T | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 373.5 |
| d14111fe-486b-3d6b-8200-488a1776e423 | -21.38131 | -50.12098 | 2024-09-26 13:12:00 | TERRA_M-T | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 386.5 |
| 7e106a98-52db-37ca-859e-4a5b8d906eeb | -21.37942 | -50.13913 | 2024-09-26 13:12:00 | TERRA_M-T | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 5d6a3eea-fe0c-3ebf-b32c-736156537c4a | -21.37716 | -50.11386 | 2024-09-26 13:12:00 | TERRA_M-T | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.4 |
| 3a3b2de8-bd16-3f93-9a41-cddd1c1330a4 | -21.37513 | -50.13222 | 2024-09-26 13:12:00 | TERRA_M-T | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 394064e7-6c27-323c-bc1d-0602b43acb8f | -19.78354 | -51.48603 | 2024-09-26 13:12:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4b14700a-e4c6-3b61-a821-dd19df420b46 | -16.12032 | -51.98246 | 2024-09-26 13:12:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5cf10415-1f50-35be-a4ad-305823ffb529 | -16.11883 | -51.99374 | 2024-09-26 13:12:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 4e089c0c-d975-38ac-99cc-144b2830c385 | -16.11586 | -52.01621 | 2024-09-26 13:12:00 | TERRA_M-T | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 273ca8e4-e032-32a0-bb38-a7f04eb3745d | -17.02066 | -53.27785 | 2024-09-26 13:12:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9cd4e671-e78d-3e05-8de5-8df08cda53e7 | -21.04361 | -54.17902 | 2024-09-26 13:12:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5913ab15-06f8-3b95-bcda-8ecfead65573 | -16.62497 | -54.08324 | 2024-09-26 13:12:00 | TERRA_M-T | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5674e914-3c9f-33ca-8ff6-d500c7ca2bf5 | -20.51307 | -54.90243 | 2024-09-26 13:12:00 | TERRA_M-T | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c26157ae-70a4-39a6-a25b-bb574f05e7b0 | -21.34736 | -54.65267 | 2024-09-26 13:12:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 53938286-be8b-305e-b6ba-223a824dda83 | -21.33823 | -54.65132 | 2024-09-26 13:12:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d4cc2de8-4cb8-36c8-b569-e8b8f6fd5eeb | -16.12867 | -55.4268 | 2024-09-26 13:12:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4ca67ff4-c999-3e79-8ef7-4eff55de8a4c | -16.11832 | -55.42825 | 2024-09-26 13:12:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7f635d63-0003-3b54-93b3-1ad5a4fa2d91 | -15.90286 | -55.39178 | 2024-09-26 13:12:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82ad3c2f-2a7f-3182-a226-cac9b82988b8 | -15.56519 | -56.17196 | 2024-09-26 13:12:00 | TERRA_M-T | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22ec3a48-9d64-3833-a165-71a809e951ba | -17.11577 | -56.16612 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 08bfc868-9e21-387f-b094-c89ccc0d84ef | -17.11436 | -56.17559 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| e747441b-ed1a-3b2a-a59d-e9a39d10c4d0 | -17.11295 | -56.18508 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 38870121-3d83-3fad-aa6e-5596ecbae612 | -17.10678 | -56.1647 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.9 |
| 732a2d97-e00f-31c9-860e-84652fa3d1a6 | -17.10537 | -56.17417 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| ea17827d-5b93-303d-9080-b791b1ea2427 | -17.10396 | -56.18365 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 144.5 |
| 0dbd5316-c10a-3bf9-9be9-ae1dc21b54de | -17.0992 | -56.1538 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| cd34010a-0fa2-3064-8e97-43bb047e47e6 | -17.09779 | -56.16327 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 1010c2b2-c3ee-3278-99de-6a99b21283db | -17.09637 | -56.17274 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| f4a5832d-2499-39e1-9480-c97dbe8fd47e | -17.09354 | -56.19172 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 300fbab0-d3cb-3b5f-a7d9-ab6d0a7f8957 | -17.09021 | -56.15237 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 141.2 |
| e3707e3e-3ebc-355d-9a56-6219e9ef6ba0 | -17.08879 | -56.16184 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 172.1 |
| 35c36682-9053-3387-abc3-30b47ef2f221 | -17.0798 | -56.16042 | 2024-09-26 13:12:00 | TERRA_M-T | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |


[Clique aqui para ver as próximas entradas](README185.md)
