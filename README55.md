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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5376a649-3951-3ef2-b991-7c164cfce274 | -14.54266 | -47.35818 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bfb44c64-d9c2-3778-b9c4-bd1484f28b1c | -18.56032 | -49.25502 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.0 |
| 47f8ed6c-4cfd-3b0e-8a82-212927847d85 | -16.01801 | -59.25279 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 047123e7-6e07-3234-a131-a5fe0639e347 | -16.66416 | -49.75932 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ea6bbdf-230a-3cdf-a5c1-9d83cd0ddc03 | -14.53488 | -47.35375 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5b261f7-a133-3be9-9489-8a2ccc0cbe49 | -16.88412 | -45.78046 | 2025-09-16 04:32:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c6b484d-3960-384e-bbad-29cfde3cc136 | -16.01524 | -59.45818 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 181cf0d3-c99d-39ad-815b-c5d5fdcddd1c | -16.93133 | -44.0689 | 2025-09-16 04:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 325d86eb-0e33-371b-b693-62647c2f3f39 | -20.09222 | -47.7322 | 2025-09-16 04:32:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c7757a0-f0d4-3738-836c-234b796b5352 | -16.51953 | -43.5463 | 2025-09-16 04:32:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f5610b1c-1645-3d39-8420-dfaa6c5aaa4e | -14.84696 | -45.50544 | 2025-09-16 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b3b2a67-795f-3820-9fbc-8c293f8078ab | -18.90409 | -49.5807 | 2025-09-16 04:32:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f5253d35-d828-3875-afbe-e994c8fbb843 | -16.75228 | -49.19616 | 2025-09-16 04:32:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6029c67-ed51-3595-9bb3-05e9f7b2a9bc | -16.02261 | -59.4329 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1069679-f615-3cf1-8b35-e8b0dbe7fa70 | -15.99608 | -59.41451 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec861cbf-7d71-37d3-b2c5-f1623bb31b28 | -15.40771 | -47.3476 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52fe29cb-64fd-326e-a712-129158cef573 | -13.61431 | -47.64185 | 2025-09-16 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e460ce1-14bf-3012-8553-d38b7980e004 | -16.66475 | -49.75576 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9da9229-7b4e-3f05-a8f8-49fef490a5b5 | -14.60609 | -46.38731 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50ef76a0-c71b-3559-80b9-7859c9c85a97 | -16.03168 | -59.44774 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beedd5a8-5f2c-3a5d-a5c3-405a1bfdc848 | -16.70917 | -54.97595 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 878e47e0-e5e6-3d15-bdbc-4cdb893c8bb3 | -14.5125 | -47.38735 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1fd35f0-49f0-3fb4-9e6f-d679951881d8 | -14.42468 | -47.36535 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b15abf4-9ce4-3133-8716-6c7c35b820aa | -15.72457 | -39.32248 | 2025-09-16 04:32:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7689b1dc-80a0-3244-b713-a25bb27543e5 | -16.47319 | -55.10557 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8df91876-b339-31da-aad6-18b877b4b6c2 | -14.45681 | -47.28148 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d82c394c-d67f-3481-af96-d198c2713af8 | -15.82125 | -53.46501 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a0cab95-be18-3b4d-afc9-8b0a40d16119 | -15.15763 | -52.46486 | 2025-09-16 04:32:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ed0e056-6e83-3b43-8dec-baba3f2eb362 | -19.07739 | -43.12855 | 2025-09-16 04:32:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 343807df-b602-3888-a207-dff13ec4ccb4 | -14.48131 | -44.87036 | 2025-09-16 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 267189d9-7eb8-3b7c-bf79-425d6af9dd33 | -14.80688 | -51.67217 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7f45b351-fff4-3311-8d51-c54fda433e2b | -16.43095 | -45.68143 | 2025-09-16 04:32:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd2b7464-8940-3d88-aa7a-e22ada858854 | -20.01818 | -43.78627 | 2025-09-16 04:32:00 | NPP-375D | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1dd54c6e-1cfc-3b05-b21a-23322d414003 | -13.99472 | -49.64587 | 2025-09-16 04:32:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bfc0a681-4dd2-3248-b2b3-fd1915dcf916 | -18.5876 | -48.1424 | 2025-09-16 04:32:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3737f37-d1c6-373a-8acb-c680a077134d | -16.05271 | -59.42544 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f453439-7ad2-3ef4-b4d6-391005446d05 | -15.62603 | -44.37641 | 2025-09-16 04:32:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 827b4be7-49b8-379b-98c3-ed5e6eb01fcb | -19.00984 | -49.9274 | 2025-09-16 04:32:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d878856-92aa-315b-9040-804eb31379c0 | -13.78152 | -54.95182 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c01f575-e65d-33ac-b42f-beb2f2630dfb | -14.51869 | -47.34748 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49a02500-f111-38f3-bafb-295635ead0b7 | -21.15972 | -47.75931 | 2025-09-16 04:32:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31f21cba-bc5f-3c86-b53e-f84b82119c6d | -14.52154 | -47.32918 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bf3dd6d-e811-3e19-a1e2-c15cfb404889 | -18.77895 | -47.63971 | 2025-09-16 04:32:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df4bb60d-effe-3270-96c8-f3d77e2b57eb | -18.55916 | -49.26232 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18f3208f-c670-3285-95bc-a16ee64de6a0 | -18.55308 | -49.25751 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| ed650c3b-a98a-35d6-9e90-f46ed4324c19 | -21.22321 | -46.94538 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4d728347-cac4-3c0b-9783-1695deee0490 | -15.79738 | -53.45993 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aafa175d-eb65-3dac-9f79-24df0058ad4a | -15.572 | -46.7514 | 2025-09-16 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9c9f4d3-5656-3e63-b935-475b608842af | -16.02173 | -59.42813 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15e2193f-9ba7-3886-bea5-2b3db4aa297f | -15.83227 | -53.4726 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f4016135-0633-35a1-b8b9-bae7924a925e | -17.86261 | -44.4402 | 2025-09-16 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 296ef8c3-8a8b-3cb1-842f-abdd01941c28 | -20.12671 | -49.11176 | 2025-09-16 04:32:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 128825bb-dd9c-30f3-91ad-e13abe8ce023 | -16.8126 | -47.78341 | 2025-09-16 04:32:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d47cc287-342d-3614-8be5-1f95307f6972 | -18.15772 | -49.20442 | 2025-09-16 04:32:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c85d84c-ad48-3988-afb6-1145516a9913 | -16.69869 | -49.78087 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6518581-d33b-3338-be2e-dda37a2cb6e7 | -14.53201 | -47.3942 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f682f5aa-c649-33ad-9090-76ce9bfafc25 | -15.79835 | -53.45466 | 2025-09-16 04:32:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5395f3f-4a0b-339c-b8aa-07c52f0e761f | -15.59943 | -42.38288 | 2025-09-16 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82f16b99-af1e-3cfe-aacb-c838cbc5082a | -16.01136 | -59.25581 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a487e446-2181-3c0e-99ca-455c42b98d20 | -14.51541 | -47.32444 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2187429b-db2d-3c6c-8226-3c28f62cb638 | -14.52309 | -47.3854 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 182e8ded-fd66-365a-97b2-2e5ef2934097 | -15.99766 | -59.4359 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2fc1cda-d993-3db7-bb0e-137bdef089ca | -13.78064 | -54.95646 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 83d83ed5-9676-31fd-948a-09606b5d4ec8 | -15.87475 | -59.41953 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f36b107b-8b2c-3b68-8fc5-66a95b5878fb | -18.55641 | -49.25809 | 2025-09-16 04:32:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| ed6771f6-8363-3597-8adb-5dfb7596d736 | -14.81204 | -51.66403 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ce606e4-7f73-36ef-bb6c-9b81c7dd9aaf | -20.8656 | -49.40243 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e1d5e03-1d20-3a15-bd65-2d2499eeba2e | -20.60582 | -50.14003 | 2025-09-16 04:32:00 | NPP-375D | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e90c1cf9-4bab-38e1-bc8e-028dc403cacd | -14.5471 | -47.37397 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63822712-9c1f-364f-82a8-eb9c0126f07c | -21.19719 | -44.37227 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2788f217-efb3-3500-b216-12eee226d4cd | -21.05923 | -46.28126 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea03f711-2426-3a83-97bb-7f52d2817a45 | -16.0244 | -59.25102 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db0fd5b5-baa0-3e8b-a117-fcffb431e05a | -16.69198 | -49.77958 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd50d6d8-7011-319f-beaf-a903ac500aff | -15.99072 | -59.26802 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8180f591-f362-3ea5-a378-3fabb306902e | -14.47536 | -46.35589 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e51afccd-d21d-3355-a963-788b926d4964 | -21.21668 | -46.94018 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbc30598-62fb-3c66-9608-64abcc79a7fb | -15.99393 | -59.25289 | 2025-09-16 04:32:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc9a2827-cd00-312f-a62c-b5d1bebfd68c | -13.76453 | -48.76025 | 2025-09-16 04:32:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a12fe38-5d7c-349e-8923-b50e595c0682 | -15.41557 | -47.34891 | 2025-09-16 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 690a7aa7-583e-3907-a2db-f6bda0eaf8fe | -18.62089 | -43.89988 | 2025-09-16 04:32:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a09ae1a-b853-34ec-b07f-0b1636a4ed1b | -16.05864 | -59.42613 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 569985cd-386f-3b27-8d1e-fe16ff204c64 | -21.27218 | -47.00911 | 2025-09-16 04:32:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdda3d3c-7668-3d9f-a123-b96fb30408a2 | -19.8707 | -46.74132 | 2025-09-16 04:32:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0942ded4-879f-339d-a5fa-54348ba61626 | -17.60446 | -46.68571 | 2025-09-16 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f19ea686-8996-364b-8176-2acd308296b9 | -21.23209 | -45.01634 | 2025-09-16 04:32:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5bb891d3-fd62-3072-8ed1-21c2cbdbe0c2 | -13.28399 | -54.24064 | 2025-09-16 04:32:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 458861e0-dfd8-3278-a05f-e282066fcbbc | -15.77784 | -47.72798 | 2025-09-16 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78ad933f-5194-34c8-945e-ad152e249029 | -16.48476 | -55.11122 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bb684f44-052e-37bc-a619-dbdfc3f712b3 | -16.48125 | -55.10585 | 2025-09-16 04:32:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 29.4 |
| 73b83a65-fd6b-3a85-9c4b-23d7c5bf1c2e | -14.97392 | -46.55937 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a2d8b65-bafa-37af-be1a-e932b2500fd3 | -17.72363 | -47.93815 | 2025-09-16 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adafafc7-3dea-33b2-88bb-a8d62c33266b | -14.54488 | -47.36607 | 2025-09-16 04:32:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 659b6ac4-bef3-30dd-8dc3-fd9ada9233ed | -19.58835 | -44.06656 | 2025-09-16 04:32:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0bd49d9-9329-3ddc-b6f3-aafbd358d27c | -14.97049 | -46.55893 | 2025-09-16 04:32:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41ef3fc1-5126-3daa-84fa-b49283f2729b | -15.71932 | -39.32164 | 2025-09-16 04:32:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 052c32af-c9c9-3180-8208-2ee00626b039 | -15.86419 | -59.38314 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c3e971a-83f6-35b6-877e-1679f11aa997 | -16.66138 | -49.7552 | 2025-09-16 04:32:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38ee4aa1-2d80-39ed-8fb9-a081351bf963 | -18.86568 | -43.34888 | 2025-09-16 04:32:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 48cde7b0-504f-3fe6-8b91-977c0c5884cb | -16.02109 | -59.45935 | 2025-09-16 04:32:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb49e06f-1566-3b5e-8d60-12c9588911bd | -14.92282 | -51.65092 | 2025-09-16 04:32:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README56.md)
