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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f70bc46-2588-39fa-aa9e-b5f5712bbd9b | -10.75658 | -44.82084 | 2026-09-24 04:10:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbf61031-863c-3fb7-92ba-bf5e5ced4424 | -10.08222 | -46.01234 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7e93daca-8fec-3144-8b69-cc97216d9a31 | -13.46318 | -46.26632 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a54705d-e4ba-3245-a5bc-ac7b6253c884 | -10.42301 | -49.3642 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c345db5-46f8-30ca-bc35-0e320d2273ce | -10.41772 | -49.36799 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4f9d4d93-57f3-3719-90de-de7d1b5e7391 | -10.27343 | -49.95615 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ee44484-9f2e-3e56-ba5a-985e6ed940e9 | -10.62118 | -54.00158 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f6dfd02-9311-321a-a776-ed9f68870c8d | -13.07833 | -47.40258 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aeaa4583-e345-3570-8400-3ac7b7615fec | -11.48977 | -47.3553 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2655e4cd-0b4b-3b28-a78b-bad016878ae0 | -10.27435 | -49.95117 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3c3a98a-4e07-3236-900d-8cb55d4ccbd7 | -14.96414 | -47.53407 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82bfdae8-402d-34ab-afb4-5e3c02220e48 | -10.07898 | -46.00905 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0ffd57e-cc6d-3ff9-acbc-061a2bcd52fd | -11.23896 | -51.35624 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af86a8b3-2906-3cae-9e1a-b88672dbfc1f | -11.45504 | -46.72014 | 2026-09-24 04:10:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22c02b1f-44d0-3af9-a257-f444c6afba80 | -11.25464 | -51.3561 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a01d2bb-f759-3886-b6c1-ff09e137f239 | -12.41007 | -46.9608 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abb80e00-1627-344d-b0cb-8a48a5136b38 | -10.08333 | -46.00541 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 64b55460-e25f-36ba-9eac-2e3384cfbda3 | -11.69753 | -43.43625 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 55e93880-4818-3e1a-9146-8886b5d41bdd | -13.45748 | -46.25679 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d148d35-dacd-36a9-a205-97cc0062164b | -14.72709 | -45.60385 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ecf3af1-9705-343f-b5c6-4b686759d3d7 | -14.96338 | -47.53843 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6ef9b18-6e89-3468-9324-22f1a3edf78d | -11.63018 | -50.60881 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bd8d9141-9f91-339f-811d-df121dc10313 | -10.09021 | -46.05387 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 053af68b-28f4-3007-a9cd-d972aedcd1d0 | -14.70352 | -45.57624 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3bcbdb0-8c26-3c02-8d9f-89d66c5c00df | -11.49529 | -42.33643 | 2026-09-24 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 39ce4f35-054f-3836-812c-47081e1c11e8 | -12.10363 | -51.86377 | 2026-09-24 04:10:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5397f1b-ff3e-3813-8618-0d60545cb3aa | -14.72151 | -45.59495 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e07cd5b-8f1f-349f-be39-789a88fc4257 | -11.98183 | -50.00046 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 580cf939-3c39-357e-b0ff-9521d1e49a68 | -10.39115 | -46.56989 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2802c49f-6187-36cd-b346-02f55fde5b71 | -12.05896 | -50.30053 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5a2ea94-1db3-3bba-9633-8251cf338c48 | -11.12589 | -42.78661 | 2026-09-24 04:10:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2bd0f0d-7f1c-3be5-a20b-4df61c08cacb | -10.88747 | -45.07846 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4c59e5f-fdf4-3a58-a3b6-3bd7ac5936fd | -19.00281 | -43.75529 | 2026-09-24 04:12:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e0a639d-1d7d-3d11-b5c6-4ef3c91a3c22 | -18.51947 | -46.04111 | 2026-09-24 04:12:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 17f40908-3670-30a2-bcf5-10fc98a83fcd | -18.62973 | -44.23936 | 2026-09-24 04:12:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b655eda0-4e3a-38b8-aab0-4c1e7442bb01 | -19.67668 | -44.59202 | 2026-09-24 04:12:00 | NOAA-21 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52456104-9c3a-3188-bb29-777ffb20b9d2 | -21.21247 | -45.40807 | 2026-09-24 04:12:00 | NOAA-21 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13ed33ec-9277-326a-a750-7f1b14e06c8a | -17.97211 | -47.84996 | 2026-09-24 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e051e05d-ff8b-386b-9eab-cdd908cc50a2 | -18.88617 | -47.57566 | 2026-09-24 04:12:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caad8cba-044d-348f-8821-4befdfe3d4b4 | -19.46105 | -45.65528 | 2026-09-24 04:12:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28f58b35-721f-3db9-ad29-0dca8200b43b | -17.97287 | -47.84561 | 2026-09-24 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bd1f04c-c153-38c6-8f6c-2d7673600d5f | -19.18801 | -47.36421 | 2026-09-24 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| baeae61f-a369-3395-8ee3-0c52ada17a20 | -17.85088 | -52.38729 | 2026-09-24 04:12:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73b80e97-0e18-3c4c-9b65-d35eb2772285 | -18.34908 | -46.41134 | 2026-09-24 04:12:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5884ab53-19f2-3c3c-b26f-f30eee7abc70 | -18.76105 | -44.98753 | 2026-09-24 04:12:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb941cfc-9c14-36a3-b7b7-7e40456b0b83 | -18.88634 | -47.17111 | 2026-09-24 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58c72763-fd01-3a03-bcd9-f04dbda5e46b | -20.01571 | -45.40127 | 2026-09-24 04:12:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83857658-8c2f-3820-87d2-853f10d89b77 | -17.85058 | -52.39075 | 2026-09-24 04:12:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ab9ab65-536e-3b7a-bf75-3630a325a02f | -19.18521 | -47.35948 | 2026-09-24 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3483c70-a84a-3651-b889-276ff0727faa | -19.67337 | -44.59145 | 2026-09-24 04:12:00 | NOAA-21 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59dde7b0-bc92-3117-867d-a7e0e35f30d5 | -18.72018 | -47.07545 | 2026-09-24 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9a639f4-430e-3890-98b1-55652e068b4f | -19.77711 | -48.28963 | 2026-09-24 04:12:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b7126c7-4163-3678-ad3c-4e9f13e97997 | -17.58863 | -54.0469 | 2026-09-24 04:12:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f223ca47-0515-3670-ae9d-29b651a01fa3 | -16.7812 | -52.63328 | 2026-09-24 04:12:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b8a5661-9697-3428-a93a-3db8b56ca4a6 | -19.18451 | -47.36355 | 2026-09-24 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 597c500e-33f0-32e7-a0c5-301b7f694750 | -18.34843 | -46.4152 | 2026-09-24 04:12:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f037c59b-fe77-3a08-8891-0cde03f1723e | -18.88565 | -47.17514 | 2026-09-24 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7de8947b-5d25-3c1e-8232-7b85c82c97b1 | -18.88497 | -47.17918 | 2026-09-24 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d51eed54-67e2-36b6-aeee-0ec48b29d574 | -17.96924 | -47.84496 | 2026-09-24 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29b8ff4f-f9a8-33d4-bf45-d0a10cf73b8d | -19.1887 | -47.36013 | 2026-09-24 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0adabf2-a024-33c5-88bb-ed2a6ca6d3b0 | -17.97573 | -47.85063 | 2026-09-24 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 775b6615-26c3-3f9d-91bc-f6c71598d5cd | -18.61851 | -45.13496 | 2026-09-24 04:12:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa619a46-0b9c-38d8-b5dd-0dd0d0fcdecb | -6.6146 | -59.9272 | 2026-09-24 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9159e9c2-0992-3430-a7f2-e0aaa8e2036f | -6.6331 | -59.9265 | 2026-09-24 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 22b8337d-413e-3682-86d1-0444ebac028a | -6.4487 | -59.9526 | 2026-09-24 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8cbcfd76-487a-3a3b-8c49-4e318c78e319 | -6.6145 | -59.9464 | 2026-09-24 04:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 43a40c0c-cd86-3c43-aada-a9dc5ff13cfe | -6.6146 | -59.9272 | 2026-09-24 04:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| cc1a3a55-ddb9-3015-9146-304d706d9961 | 1.29729 | -50.85991 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df528295-e2ed-3c6d-9148-514375a5500f | 2.13007 | -50.72817 | 2026-09-24 04:42:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac2c521a-f3d5-319b-afae-ef2ce5e01464 | 1.29458 | -50.85221 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f041df-2598-3fb9-9125-485376d43294 | 2.1599 | -50.89034 | 2026-09-24 04:42:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25d10860-3a1f-3417-bcf3-7f0deff5b593 | 1.27621 | -50.83945 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11e58cc3-dd21-3d55-b22a-8e454ce54429 | 3.83359 | -51.79985 | 2026-09-24 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10f0e7e6-0b0b-3c26-8190-5554fef1dccc | 1.29539 | -50.8573 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee2ac802-00f6-3047-89aa-e49264aa5f71 | 1.29807 | -50.86502 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af1379a9-37e9-3201-b643-d1706066d0ec | 2.4548 | -50.94627 | 2026-09-24 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f21a28a5-7a28-3ee6-9dbc-f0adb7ee05e6 | 2.15937 | -50.88682 | 2026-09-24 04:42:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0362acef-b6a2-3531-9df7-79216f779a78 | 2.13095 | -50.72659 | 2026-09-24 04:42:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0a60439-5b0f-335d-b8ac-9136fffd1961 | 1.8727 | -50.67203 | 2026-09-24 04:42:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 109e6752-243c-3d5e-98fd-5938a8504c13 | 1.9958 | -50.87582 | 2026-09-24 04:42:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09c3731c-e5dc-3528-a77b-4834b1d2756e | 2.45424 | -50.94268 | 2026-09-24 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5249a13-8633-372c-a72f-7081e1513164 | 1.28019 | -50.83883 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e90f931b-40d3-3c26-af55-a94d095ce763 | 1.29651 | -50.8548 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a15eaf0-4ca9-3a3b-9a00-82df26faaeea | 1.27746 | -50.83693 | 2026-09-24 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0371673-a0d3-3ac4-8f59-2c2727370088 | -5.96029 | -49.97411 | 2026-09-24 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bad7ab43-beda-338d-882b-c220d1a5d6ca | -5.51849 | -50.02854 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a98de214-8ee3-3b9b-b5d3-e2cd734c560b | -6.72191 | -43.94096 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b82e85d-3fb7-368a-8d37-a38ae7ed7fa0 | -6.61971 | -43.73082 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1319d0d-5b4a-3414-ad86-8832aad9ca38 | -1.19237 | -54.138 | 2026-09-24 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b59f380f-5ef5-30fd-ac7a-41689cf2a0cc | -5.7862 | -49.18882 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45bbbfef-78d2-3532-97e2-ec0c254ce74a | -3.69036 | -60.55304 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60882213-6c6d-38ea-900b-3ea08452f2c3 | -1.60606 | -49.81657 | 2026-09-24 04:44:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b189921a-706e-3f81-a736-8102f2f531f5 | -3.68457 | -60.54531 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 02061d90-e520-31f6-997e-d0629d94cd5b | -6.32912 | -42.94692 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17e1288d-b5b8-3829-83d7-f1d5294f160a | -3.71456 | -54.20398 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ca782f1-9f9c-3205-94f5-88d72f44c2cc | -2.9741 | -54.15006 | 2026-09-24 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d83a62-fc68-3caa-aaf7-b995238de202 | -6.4391 | -48.46915 | 2026-09-24 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc6a0e7d-ef1f-3082-aebb-247d6d00e7ab | -6.2003 | -47.49692 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73441048-f6de-34c3-bbcf-1a60e2503b5d | -5.95684 | -49.9733 | 2026-09-24 04:44:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 012a329c-54a6-3f96-b6f3-caa159b2d649 | -2.71598 | -57.51128 | 2026-09-24 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README42.md)
