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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 417e1635-d277-3b6b-9368-8d8d46e3a473 | -8.51294 | -43.30999 | 2025-07-14 05:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 4c9c038c-0ae3-3d3c-879d-426d3e62168b | -8.51752 | -43.28254 | 2025-07-14 05:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| d5ce942f-b642-3918-8b7b-fa2f83ea52e4 | -8.51855 | -43.28764 | 2025-07-14 05:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 9f21b762-4b19-3cb5-822f-8ae8d9360683 | -8.51376 | -43.31513 | 2025-07-14 05:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 9bfd6f9a-eeec-3786-96a8-72c46592d688 | -8.50381 | -43.28495 | 2025-07-14 05:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| d801f508-7afe-34e0-9d22-f9390b94e89d | -22.67704 | -42.84847 | 2025-07-14 05:04:00 | AQUA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 53a23c60-9fab-3197-a2d9-677307a23105 | -22.67443 | -42.86301 | 2025-07-14 05:04:00 | AQUA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 85bbd60f-a565-3f53-81b5-5e9875667e50 | -8.5211 | -43.3063 | 2025-07-14 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 17543151-2e96-3634-acfb-834963b4b9b3 | -8.5211 | -43.3063 | 2025-07-14 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 077de2f7-5795-3785-8936-a001e8b0287a | -8.5022 | -43.3085 | 2025-07-14 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| ca984115-c7d6-3163-b8f8-c03e4b28a41a | -8.5211 | -43.3063 | 2025-07-14 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e6d65c63-d619-3a91-ab6e-45bfb9cd0d89 | -8.5211 | -43.3063 | 2025-07-14 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ae9e1a2b-3539-3a00-af50-5cfca4084f95 | -7.6324 | -56.76285 | 2025-07-14 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbf2007f-798d-3490-bad3-4519b7f42535 | -7.62715 | -56.76198 | 2025-07-14 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a6a9682-9dfd-39ad-89a9-54c43a524721 | -6.63223 | -56.28397 | 2025-07-14 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7768485f-377c-3ac9-923c-c4aee7266389 | -7.62671 | -56.76521 | 2025-07-14 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6beee4d-872c-3a2c-b09f-0f85176d3462 | -6.63177 | -56.28734 | 2025-07-14 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4861c00e-e905-394e-a387-c01470bf3efe | -6.62689 | -56.28305 | 2025-07-14 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a21135d8-8b3d-39bd-8672-e8bb711fd91c | -9.78708 | -62.48713 | 2025-07-14 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08873178-8607-3ee6-8df6-d84a14cb3243 | -9.01994 | -59.54558 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93adb0c7-ce26-34c9-81fd-41fbfca24146 | -9.20557 | -60.82626 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e688b69-57d9-31b1-bd05-20d6e137537f | -9.02472 | -61.22679 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d0b29d1-1078-3720-83f2-a154d895d751 | -9.78918 | -62.48597 | 2025-07-14 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91d045f6-625c-32db-acb3-a58883d331f9 | -10.27659 | -60.54655 | 2025-07-14 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a877485-ec27-38ff-b63d-686a1b7d12be | -9.82948 | -60.7572 | 2025-07-14 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a5d736d-c245-3ed3-89bc-fe4015f2783d | -11.82586 | -63.03259 | 2025-07-14 05:44:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5809ab4e-1c5f-3795-9ebe-f87a4fc74905 | -9.01932 | -59.54997 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c89d9a31-065f-3a2f-be16-e7d20609e521 | -9.46884 | -57.32833 | 2025-07-14 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcb3fea6-ce47-3b32-92d4-4f3262839f11 | -9.28939 | -63.46906 | 2025-07-14 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 354b03a4-7cf6-340d-a28f-fd8cec1b45c4 | -9.46926 | -57.32512 | 2025-07-14 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5223e642-36cd-3bd8-a941-43c78da0d539 | -9.46968 | -57.32194 | 2025-07-14 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 257a0fc4-fb4a-3bb2-8ee3-89f4f26b562e | -9.02336 | -59.54773 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ee79b21-eef4-34cd-89cc-061941c86fb9 | -8.73099 | -64.17357 | 2025-07-14 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb498cb8-f087-3e70-9d1e-2c6636309442 | -10.05406 | -59.11186 | 2025-07-14 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00cc3247-df71-3001-8ecc-6736ce5cc07f | -9.86745 | -60.29374 | 2025-07-14 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32d50a8c-f7d9-300a-87ca-34bd6a8d2d27 | -11.86755 | -58.7072 | 2025-07-14 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 440d2fd1-603f-3f52-882f-6b115ebf8764 | -14.50194 | -58.59639 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac00c5dc-492d-3bef-bdd0-eba42f00630e | -14.53392 | -58.91779 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f71ec1d3-b70c-3f8c-b3a5-9b59aa246966 | -10.27238 | -60.54591 | 2025-07-14 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b8898b7-7502-3637-85c8-eb6034c13696 | -8.7182 | -60.63019 | 2025-07-14 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67ff05a0-8b84-32de-9664-a74d37d0da86 | -9.99867 | -65.3077 | 2025-07-14 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac3b01dd-7f33-3aec-ac1b-79c81c58f463 | -9.20608 | -60.82257 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01f87380-2ad9-3adf-a610-b61832b72f2b | -10.01638 | -67.74845 | 2025-07-14 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1548739e-6a2c-3f90-a80b-0acf38d3a7bc | -9.24614 | -64.40607 | 2025-07-14 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcbc765a-1d99-344f-88dd-3c620c8191e0 | -14.53427 | -58.91492 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 529e437c-0658-327a-a51a-fdd4d2ddcd99 | -9.0623 | -60.39874 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fa9dc63-a5fb-3473-ae79-9ca3995da21f | -9.46843 | -57.33151 | 2025-07-14 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e847d592-d548-3813-8a3f-44c7dc599174 | -14.49981 | -58.59533 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bee2538e-a580-3572-97a9-c8f7412347c8 | -9.01678 | -61.22558 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b66e314e-f4b5-322f-93bf-efcf824a38e6 | -9.01892 | -59.54706 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e5f79fde-46ca-3532-8d14-ce802c39a34c | -10.27632 | -60.54904 | 2025-07-14 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4d47e21-b9b0-3528-b90d-6cc77cf3180b | -10.2721 | -60.54836 | 2025-07-14 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 143177eb-ae08-31d6-83ce-5a21ce0e8fcb | -8.92968 | -63.90041 | 2025-07-14 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82f6b823-ee24-3c81-91b3-73065b4e864b | -9.6465 | -65.73943 | 2025-07-14 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb269600-9382-3b7c-bd88-8a6e6efb868d | -14.53357 | -58.92066 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b646d42-27ac-3deb-af5d-be543b8c282a | -14.49681 | -58.59582 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc5d73ec-0ce0-3a79-831f-d11d6eba18f9 | -14.49431 | -58.59793 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ccfbeea-8c72-3fc0-8df0-9cc718df360a | -9.202 | -60.82195 | 2025-07-14 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9287000-c2de-314d-97f5-d75103222048 | -9.24986 | -58.76268 | 2025-07-14 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8306d5a5-eca0-3312-bbba-19cf2997e4d7 | -14.49944 | -58.59852 | 2025-07-14 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28398f23-cdd2-3e0c-80ba-a22e735413f4 | -21.49068 | -54.27036 | 2025-07-14 05:46:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fbc3034f-b202-31a2-a182-65011b72d43f | -8.5211 | -43.3063 | 2025-07-14 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c97fc6ed-ebf9-3bfb-adee-bbf740662b46 | -8.5211 | -43.3063 | 2025-07-14 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e4080bb3-dcc1-3349-86cf-f48e877408a9 | -8.5211 | -43.3063 | 2025-07-14 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 72cc71be-23fb-3e4c-88e0-4b1446808767 | -6.4467 | -45.349 | 2025-07-14 06:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9c47b8fd-69f0-36ce-99f8-7cd6ebe9b4e3 | -9.28634 | -63.47045 | 2025-07-14 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 867ddf81-b98f-3858-95b6-254a779ca2ea | -10.05702 | -59.10781 | 2025-07-14 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cee0faed-6d3b-3a0b-88f4-a4d4ac037c46 | -9.64653 | -65.73849 | 2025-07-14 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d926fe45-f0f1-32de-af9a-d9217ef0af32 | -9.2019 | -60.82113 | 2025-07-14 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99c908b7-af1a-3506-821a-2b583dff8d69 | -8.25787 | -72.8045 | 2025-07-14 06:10:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53a18da2-b2dd-3cc0-8954-96c76cfae6e6 | -9.29156 | -63.47123 | 2025-07-14 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44b92e35-4a3a-3efe-aef4-d8d55e0d3f59 | -9.28678 | -63.46919 | 2025-07-14 06:10:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b6be28d-40da-36d3-b2ac-75bcaa34f56d | -8.5211 | -43.3063 | 2025-07-14 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 39ce62df-38e5-386f-b0b1-b627fd014137 | -8.5211 | -43.3063 | 2025-07-14 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 51aaf999-0233-337e-bf30-e3dc298ac6a4 | -8.2582 | -72.80368 | 2025-07-14 06:31:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72bfcc98-26b9-30ed-8905-33200fc3ebc5 | -6.2783 | -43.4113 | 2025-07-14 06:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| fc269a22-612c-30ca-a7c0-5ec8180cb47e | -8.5211 | -43.3063 | 2025-07-14 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 732edb84-e0ac-3131-bca6-5f4e839ea7c6 | -7.62209 | -56.75982 | 2025-07-14 06:40:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 071b511c-07e0-3e61-99c3-d15a766b840a | -8.5211 | -43.3063 | 2025-07-14 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 2daa57af-cbb4-3d3e-8409-62e288b32f04 | -8.5211 | -43.3063 | 2025-07-14 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 88c49e21-68a2-35da-95ce-203a4065983c | -8.5211 | -43.3063 | 2025-07-14 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| ed6724d1-8328-3ee1-a414-3442c4bbcf88 | -6.36658 | -43.64801 | 2025-07-14 12:29:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0e76d997-1be6-3bb9-bd7a-964ec5eb04cd | -6.48361 | -45.29159 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 34322a21-0761-320a-aba2-d349d7c35ac7 | -3.58369 | -47.52836 | 2025-07-14 12:29:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4bb7e989-0cae-304b-a841-89f1a50d8b4a | -5.69842 | -43.65474 | 2025-07-14 12:29:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 6ec9bee0-59c6-3205-9583-de5efd345d1c | -12.10654 | -44.73891 | 2025-07-14 12:29:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 527cb600-3daa-3cce-b67b-a11783c6bd04 | -10.57053 | -49.12411 | 2025-07-14 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b1014b8b-5564-3aa4-a936-c6c99379a4ff | -9.80646 | -47.75628 | 2025-07-14 12:29:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 56c62351-d4c7-3561-9a7e-87b4f0cf6b40 | -10.39233 | -46.71037 | 2025-07-14 12:29:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 96c9b75b-5e4e-38f5-bdf2-79023a53a37f | -11.71766 | -47.04652 | 2025-07-14 12:29:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ec828b07-1031-3d4a-95b6-99f2c636d239 | -4.86593 | -45.3106 | 2025-07-14 12:29:00 | TERRA_M-T | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 83e58e52-0fd0-3ae6-b10c-fe8fd4e4b3e1 | -8.91496 | -47.34175 | 2025-07-14 12:29:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f259955c-10e7-3d78-8871-a4c15282ca55 | -8.59672 | -47.3114 | 2025-07-14 12:29:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| f53fe29b-bbb8-353c-ac3b-15ee2395b199 | -12.20185 | -50.292 | 2025-07-14 12:29:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3abe2d50-34db-3515-aaf7-8e897ed25779 | -4.60784 | -43.31953 | 2025-07-14 12:29:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c9d2264e-7eff-36e7-b835-163db2309a94 | -6.3841 | -44.75752 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 63eddf3d-62c3-39a7-85ca-9ad5f4b9fe3d | -11.71488 | -47.06725 | 2025-07-14 12:29:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6437c77-91e1-39c4-bd71-42d5fbd1e5cd | -2.91835 | -48.2395 | 2025-07-14 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 14d07bc2-1223-3fb2-b3b9-f1c8b8b0f207 | -3.69105 | -47.4241 | 2025-07-14 12:29:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 418b7d63-4ebd-3aa2-ad64-c7fac3c5fece | -6.45997 | -45.38969 | 2025-07-14 12:29:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |


[Clique aqui para ver as próximas entradas](README15.md)
