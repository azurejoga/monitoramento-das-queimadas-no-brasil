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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1716d34b-7e8e-3e94-ae41-b8d2cbf88280 | -10.97595 | -45.09875 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 9fdf0552-ccb5-3ea2-89e3-c6585c20af63 | -9.70989 | -46.82506 | 2025-09-09 05:50:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 3b6143c5-33c0-3ea2-ab16-723c86da4dce | -9.7085 | -46.8341 | 2025-09-09 05:50:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6bba9c32-7e97-3188-b62c-29ec254faa34 | -11.83774 | -46.75209 | 2025-09-09 05:50:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 40cb0c44-3c8d-399d-9a89-3869602090c2 | -9.7071 | -46.8432 | 2025-09-09 05:50:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e4df3711-f09c-3118-b2e6-fac301b49f44 | -11.30893 | -46.52368 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bc397ba6-6044-3235-a988-9bba4478bff7 | -9.82224 | -46.02839 | 2025-09-09 05:50:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e27f95ea-ae56-3860-a69e-9c3e6eb0f270 | -9.71737 | -46.83554 | 2025-09-09 05:50:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 5f5453d5-f7de-32fe-89cb-c206ec7f081a | -10.96437 | -45.11569 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9af4babf-e3b3-31c4-8ccf-764ecd023f0a | -11.30419 | -46.49562 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e50ddc8c-7a6e-378f-a9ce-9177aee112b9 | -10.73824 | -48.18166 | 2025-09-09 05:50:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 437393cc-5936-36d2-b74c-9820fd51c375 | -9.72434 | -46.7901 | 2025-09-09 05:50:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| adc7c363-4793-3294-ad28-e442ca1cedf0 | -8.47703 | -48.26422 | 2025-09-09 05:50:00 | AQUA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a8f9be67-5a4e-3255-9f75-85018916954b | -11.29587 | -46.47856 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 519ebd5d-f4e8-344f-b0e7-4c915c651460 | -11.126 | -48.41771 | 2025-09-09 05:50:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9681b38f-817b-3729-88db-17fb35a44bcf | -9.84677 | -47.78669 | 2025-09-09 05:50:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0862e823-833e-3be2-a625-7d768c51ff27 | -9.71598 | -46.8446 | 2025-09-09 05:50:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 82785dc8-de94-31e1-8530-d2d33508f138 | -10.1677 | -48.34407 | 2025-09-09 05:50:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fdb850c3-e707-3e0d-bb0c-b9fa6b27801b | -11.29453 | -46.48747 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 994e1d7b-1e18-3092-9b65-97434e6d9afd | -8.40645 | -49.09971 | 2025-09-09 05:50:00 | AQUA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fa4a200d-f97f-35b5-bc1f-ef6de8669875 | -10.28817 | -48.81896 | 2025-09-09 05:50:00 | AQUA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6a8c9188-ae1e-3d54-bf33-064d6da268b8 | -10.98486 | -45.10008 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8a8bbeff-b93c-3ce0-84c4-8747cc04204d | -10.97328 | -45.11702 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| b79614c1-8582-30ea-a711-be797ad79f38 | -11.33869 | -46.56469 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e7b296d5-3d39-34f2-850a-215ab59607f1 | -11.43317 | -43.59941 | 2025-09-09 05:50:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 749dbd96-46bd-3219-ad30-6c2fb96ab96a | -11.30554 | -46.48671 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dd3461a9-071d-3460-810b-f2c69a3abd7d | -10.97462 | -45.10788 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3017393f-1f4c-377d-8521-a3edd81d2603 | -9.0905 | -45.71831 | 2025-09-09 05:50:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d0d904de-d0f2-3039-8595-14511b645ab3 | -10.96571 | -45.10654 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 239c1a8e-1b28-333d-9b5a-b9f8b95ac525 | -10.97729 | -45.08959 | 2025-09-09 05:50:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| dab6a24d-6491-367d-9c51-acd8038e9f34 | -14.17253 | -48.97972 | 2025-09-09 05:53:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bae2f3d9-11b9-3448-94cb-4a7ebc77cb04 | -14.35893 | -47.30955 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4081b28c-2794-3872-865d-fac1599ca8e6 | -13.04797 | -48.0202 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f94c8814-9043-3820-8244-00f9737868e4 | -17.27191 | -46.73547 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f16ee69b-e4d7-32b7-afe2-09d082722385 | -14.80775 | -47.57824 | 2025-09-09 05:53:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 78e687f2-fc3f-3653-93a1-145bc52ed8dd | -19.82983 | -48.16711 | 2025-09-09 05:53:00 | AQUA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 62c9024a-7b09-3146-9e50-145cc890036c | -13.79564 | -46.25932 | 2025-09-09 05:53:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 25fb2110-6722-33d4-b9f8-99d7b2ccecbe | -17.72263 | -44.496 | 2025-09-09 05:53:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1560cf25-21b2-3b89-98cd-0fa61f474bff | -18.82332 | -49.69739 | 2025-09-09 05:53:00 | AQUA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f89d6010-71bd-3482-b039-7c581b7cce5f | -14.35482 | -47.3365 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3a16b796-9f4b-3048-92fe-baee01af4007 | -18.00844 | -47.11942 | 2025-09-09 05:53:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5772ced5-3875-33fd-86eb-5ae337ee784b | -14.54199 | -48.75314 | 2025-09-09 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 70f99c86-faec-3fea-b0a6-dc0006767b0c | -13.93776 | -48.24431 | 2025-09-09 05:53:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| acbe85d7-3851-3df4-be9a-a3a0b60c17b3 | -18.66546 | -47.54869 | 2025-09-09 05:53:00 | AQUA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3c4d383f-d6bf-3d0f-9c56-653ec8e24178 | -16.95732 | -49.67513 | 2025-09-09 05:53:00 | AQUA_M-M | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0b08ca92-446d-3f3f-a638-7875a25f933e | -18.03492 | -47.12377 | 2025-09-09 05:53:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| f4468150-8f39-3896-bec4-f0c1f985bb10 | -14.33253 | -47.30532 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 19066821-0391-3610-a960-673a8f9a7116 | -16.96483 | -45.84943 | 2025-09-09 05:53:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 446c7b36-c0d9-33ec-a22d-fadc36580f93 | -15.771 | -53.52949 | 2025-09-09 05:53:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4576a34b-ac9a-3153-a30c-6f5edc8913ac | -14.79806 | -48.17881 | 2025-09-09 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c06472c9-ed5f-3c83-ac4f-103d36e8cbc4 | -12.19183 | -53.89405 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6e722d22-1d82-397c-9e01-7c8de8c49975 | -13.01947 | -48.02523 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 05f1162e-7a9a-3a6d-8708-9efcfd76166a | -13.74875 | -46.89315 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b38df3f0-3188-3c04-9d9b-1823cc9062a8 | -17.30126 | -46.72095 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 825c97d4-99ab-337e-8a9b-3d9c46bdeb30 | -12.86202 | -47.96739 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3688be0e-40eb-357c-a76f-f63f13859ff6 | -12.83201 | -47.98215 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 19e0edc0-e429-325c-a251-a131655b3e5f | -16.28887 | -45.67836 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9b0ac021-8409-3ef4-aaa8-8d04d1df22c1 | -13.74739 | -46.90213 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dec508f7-250e-389b-84bd-2aa4f68bdf3a | -19.41426 | -46.52056 | 2025-09-09 05:53:00 | AQUA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3e711927-a9b7-355c-badf-c27e92cb57e8 | -15.54681 | -48.36594 | 2025-09-09 05:53:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ca4de07e-f3c6-3fa9-af97-ecfa01605ef5 | -12.83939 | -52.94031 | 2025-09-09 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 7f1405e0-2c53-3278-b9bd-25c37963e475 | -17.57218 | -44.54477 | 2025-09-09 05:53:00 | AQUA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7a7f1a04-75ef-354f-a06f-0bee27001d33 | -13.92877 | -48.24269 | 2025-09-09 05:53:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 70f7f305-6afc-396b-b48f-70de4c7e2058 | -16.07388 | -50.48959 | 2025-09-09 05:53:00 | AQUA_M-M | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 28f32d6b-f0dc-3301-90ea-622dd98c27b9 | -17.57543 | -44.53941 | 2025-09-09 05:53:00 | AQUA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7f8f1dee-1afc-3bf2-82ee-b91173551d11 | -13.81731 | -46.23484 | 2025-09-09 05:53:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 36c52dd5-d0ee-3214-8762-fa1da6b67dc7 | -13.79295 | -46.2774 | 2025-09-09 05:53:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b7603d0a-7eaa-39f6-af7b-c0bad44dc212 | -12.19817 | -53.89032 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 962ab4d7-c02a-3163-95f7-7ea9ff8c5186 | -20.16472 | -44.79208 | 2025-09-09 05:53:00 | AQUA_M-M | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 53b503d8-9af1-3c70-b0b8-3b69e06ade37 | -13.03751 | -48.02803 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f47f43de-80c4-3b46-872d-dba728d92f98 | -13.65256 | -46.97369 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 95bb7709-cff7-3a20-9242-ef666ed5b2ef | -14.90737 | -55.82786 | 2025-09-09 05:53:00 | AQUA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 607e366f-3b8b-32a6-b1d7-63bcf3733b46 | -19.99686 | -46.9543 | 2025-09-09 05:53:00 | AQUA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 72a4de65-043e-3654-9a83-673754baffbe | -18.0098 | -47.11018 | 2025-09-09 05:53:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1cc8c242-03ce-35ea-93df-00da47ec11c8 | -15.8261 | -48.93827 | 2025-09-09 05:53:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0f0c3134-60dc-3d81-a82f-c250e42ed1cf | -17.72407 | -44.48523 | 2025-09-09 05:53:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f6dd933e-f8fd-398a-b7bc-871c78b22776 | -11.97446 | -51.01157 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b91861fc-207b-3f04-8f32-b776e7fab25d | -12.19613 | -53.8706 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 200ea9b0-d3dd-340e-83c7-06d8257970fc | -12.82684 | -52.93805 | 2025-09-09 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 9a0fe4da-46cb-3c18-91c9-33a6f218d579 | -18.81739 | -49.67578 | 2025-09-09 05:53:00 | AQUA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| c7820c62-7f1c-3c3a-8cfa-7d69ccff9631 | -12.8876 | -47.98076 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 16af91d1-e80f-3b48-8231-c36ed14562ee | -15.524 | -48.38558 | 2025-09-09 05:53:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fa60425e-b0c8-3172-ae43-c61a5a1756dd | -13.82747 | -46.22712 | 2025-09-09 05:53:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7ac5b95c-af00-3117-8fba-193740d996e1 | -12.02211 | -51.06419 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cdd0db71-3de6-3d27-90b9-fde22eabefd6 | -18.8158 | -49.68577 | 2025-09-09 05:53:00 | AQUA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 9f3df46b-9a34-3703-9996-b35ceb1cb164 | -14.52522 | -48.74054 | 2025-09-09 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 369c7444-a454-302f-8ff3-53f85109c3bf | -15.78347 | -53.53138 | 2025-09-09 05:53:00 | AQUA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| c2748ba4-363e-31e6-b5bc-94be06fd8285 | -18.77138 | -48.19324 | 2025-09-09 05:53:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c809abfe-4149-3200-8fda-8151c2aa426c | -12.20551 | -53.89671 | 2025-09-09 05:53:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 216dd4c9-e56c-3cd8-9986-1b80da7b6736 | -15.53296 | -48.38692 | 2025-09-09 05:53:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 17cfa3ae-684c-3620-9ad2-b5e0b5a468cc | -17.73396 | -44.4864 | 2025-09-09 05:53:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| da8f5389-dfa1-3ba7-b998-d92b67b0b65e | -17.29583 | -46.7582 | 2025-09-09 05:53:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| acbb32f2-99a3-3628-aaa0-b66a30702897 | -12.83988 | -52.93304 | 2025-09-09 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 9a942edf-651b-35f3-9f32-f33e56548612 | -13.8381 | -46.23458 | 2025-09-09 05:53:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 277666a3-260b-394d-adbe-2e3475b7f904 | -16.43599 | -49.28769 | 2025-09-09 05:53:00 | AQUA_M-M | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e1e78bc8-8661-3365-a8ca-2c7137a27796 | -12.90408 | -47.99358 | 2025-09-09 05:53:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b267390f-8d74-3be3-85c1-5f5cf1ae8905 | -14.3562 | -47.32747 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 31568e9c-44f3-3013-a61f-2ff4f2b8e623 | -15.83114 | -52.25622 | 2025-09-09 05:53:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3cf4047c-66af-3f81-8d08-0269b337ce4f | -14.35014 | -47.30809 | 2025-09-09 05:53:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 29d8f28c-693d-3f5f-b3df-174069360a6b | -14.17089 | -48.9899 | 2025-09-09 05:53:00 | AQUA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |


[Clique aqui para ver as próximas entradas](README70.md)
