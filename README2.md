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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d53e4b4-300f-34a7-a4c1-8756e91d9251 | -10.36467 | -44.83933 | 2025-04-03 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 15e08f74-94a1-3291-92ad-faf09f103403 | -9.06572 | -38.22669 | 2025-04-03 04:14:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4c0bd135-0b5f-3411-8f27-6539e06cebc6 | -8.72861 | -44.02116 | 2025-04-03 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8672af03-bbe3-373a-9e5c-03359833f2c9 | -9.16467 | -40.97075 | 2025-04-03 04:14:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9b9a7c9c-835a-3525-adb8-870746e5f5f8 | -7.23209 | -35.59383 | 2025-04-03 04:14:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a4c22438-d11a-3d18-bfb3-e078ce2031f4 | -8.72916 | -44.01768 | 2025-04-03 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebb8321d-c99c-31eb-96a7-2da3a8468cf6 | -8.11035 | -43.12569 | 2025-04-03 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 111d412d-fad2-3282-9768-cda60f27a5e4 | -6.96443 | -43.01538 | 2025-04-03 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb95d97b-db4e-34b8-8550-1021d16e1c5c | -11.5297 | -40.42005 | 2025-04-03 04:14:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 635f0c2c-2dea-3cb9-b559-fcb4695a1b8a | -7.23281 | -35.59336 | 2025-04-03 04:14:00 | NOAA-21 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d2053b96-d34e-3af5-88ef-b96548fc3b7e | -6.23156 | -48.05594 | 2025-04-03 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 55340590-5824-3c88-aa93-d38f27b3e79c | -6.96774 | -43.0159 | 2025-04-03 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b43e514b-0c19-359c-916a-fa9b639c24bb | -6.23555 | -48.05672 | 2025-04-03 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b5e7d73-c6e0-3f07-b391-7c6f1156b645 | -6.23614 | -48.05317 | 2025-04-03 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b64377c-86cc-3606-a4c4-9bb2cf8e80f6 | -6.23956 | -48.05742 | 2025-04-03 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ba7dda8-e45c-3034-8b51-0ec247d06ea5 | -10.22534 | -42.1823 | 2025-04-03 04:14:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 17f412ef-878e-34c6-91b3-945c24997688 | -9.82721 | -40.57395 | 2025-04-03 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1cb119a1-69dd-3ca1-ae56-e20f9743bf44 | -6.95459 | -43.03509 | 2025-04-03 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 60a7fd66-718f-3098-8c2c-347a542c82ed | -10.33429 | -38.48124 | 2025-04-03 04:14:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3764387-4eee-3e54-b361-fb40268405f0 | -10.22193 | -42.18178 | 2025-04-03 04:14:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5bfe933-037f-3b2c-8da0-f3cb2655c3ee | -9.91987 | -37.08852 | 2025-04-03 04:14:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 78e99d94-8824-3380-8efd-c9c37093b8fe | -8.17588 | -42.92189 | 2025-04-03 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 79a08820-b6fd-350a-9e7a-eab7f5cf682a | -17.67836 | -42.74504 | 2025-04-03 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fee77278-1350-38c7-86c5-f4f47b6af640 | -12.78697 | -45.88119 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53c96a0d-4145-3b1f-99d1-cb0400c5f08b | -13.48345 | -44.0302 | 2025-04-03 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23ef9468-87ae-3da8-a4db-0f0d11ee551f | -13.36536 | -43.08724 | 2025-04-03 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d298245-12e5-3f9b-9c40-12e13a7345b7 | -19.36638 | -45.50111 | 2025-04-03 04:17:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2495d81-f073-3dd2-a415-c02c831ce3a4 | -13.03707 | -45.08489 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3cc1c23-a129-305f-9259-efaa30b12cc7 | -13.03871 | -45.09605 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb19554a-eb32-394c-84ef-b54a817720ec | -19.71066 | -44.76886 | 2025-04-03 04:17:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e446b0f-c57f-342e-ac89-f037aa215ed5 | -13.26616 | -43.53976 | 2025-04-03 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ede80ecd-491c-3b21-9f58-efde97b1f955 | -14.12171 | -41.67921 | 2025-04-03 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aac9fc12-0561-3b58-bb64-fdcdbc7a8676 | -15.14516 | -43.98011 | 2025-04-03 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cc3d254-8d56-3437-b044-1437932da573 | -21.48719 | -57.08358 | 2025-04-03 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccb22bf1-3140-3539-b400-7b619ed928f6 | -13.73685 | -48.27204 | 2025-04-03 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d962863-5075-3438-8acb-dd68715c1147 | -12.12038 | -45.62946 | 2025-04-03 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e39a184a-6d3e-3bc3-8a47-2dc5b2651146 | -14.13245 | -47.67104 | 2025-04-03 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 361eb6e7-a99c-38ae-b07f-3a5b0c1f891f | -13.29305 | -39.82187 | 2025-04-03 04:17:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 983a9dd4-95c8-3150-b6dc-c336cba66ef6 | -13.03152 | -45.0985 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aa15f11-717e-31ba-ad13-3b9acba66f95 | -15.07871 | -48.94334 | 2025-04-03 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e649bbb-0c60-3307-a10b-845be316862b | -15.76458 | -43.22774 | 2025-04-03 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54cef178-7520-3a0c-88fb-f669f2c3d56b | -12.29449 | -43.54165 | 2025-04-03 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f277d670-1d14-343c-a1d5-6cabd8e58923 | -13.03651 | -45.08842 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0c8f431-749a-3e6f-b969-e5d280537eb2 | -21.23301 | -56.25296 | 2025-04-03 04:17:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19502444-a389-3130-9aad-bdb4b2b16710 | -18.55722 | -44.58728 | 2025-04-03 04:17:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20b5cf75-70c7-30bf-ad0b-e30b045f3053 | -12.69904 | -44.94236 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 760e542e-8c40-30ee-8baa-19aac780013b | -14.13481 | -41.69046 | 2025-04-03 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9a13a0b-c5e6-3805-a847-cc0c7fb2abb2 | -13.03539 | -45.0955 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15a8bb11-1099-3b0a-9d36-e0b2406994d2 | -13.03483 | -45.09904 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9075f9af-ec63-3382-b3bd-4984561b284c | -15.80501 | -43.5682 | 2025-04-03 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f5ea09f-5e2f-387e-9470-f5560ed3c69a | -17.67896 | -42.74084 | 2025-04-03 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c178660-2643-36cd-bdee-6651a2c9b7b8 | -13.03815 | -45.09959 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2711087-6c61-3347-9e3a-d828eb406349 | -15.80784 | -43.57252 | 2025-04-03 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb22a44c-9e9f-32be-97bd-6b5690d10303 | -13.42628 | -41.7905 | 2025-04-03 04:17:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 07be2f44-8b90-3d23-82bf-594dbacba1e7 | -15.52809 | -48.50268 | 2025-04-03 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e4440eb-c04c-3d03-8b8e-bf6ec8022937 | -16.61759 | -44.0821 | 2025-04-03 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95313d0b-9757-3232-8aaa-8e0f44948115 | -13.03595 | -45.09196 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 424e69fb-4869-33ed-8287-e9db1cb3b24a | -12.29116 | -43.54112 | 2025-04-03 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da223604-1104-3a3d-b7b9-533650ff7493 | -12.30382 | -43.50289 | 2025-04-03 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eebe30b1-a9a9-3810-a9fb-da221acb6444 | -12.29715 | -43.50183 | 2025-04-03 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a4937e7-d62c-3061-a8f6-5d717df2ea29 | -12.30049 | -43.50236 | 2025-04-03 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 952d42b2-a87a-3e6a-bd34-e8bbc6ea1227 | -22.90214 | -43.75415 | 2025-04-03 04:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8dd1653c-abe8-324d-87af-2e69291f17ac | -12.29395 | -43.54522 | 2025-04-03 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2500ef1d-bb66-3a92-aedd-27e2d47854c7 | -15.54388 | -42.67051 | 2025-04-03 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 280768e5-3a11-363a-948c-7f5ac13fc589 | -15.54446 | -42.66643 | 2025-04-03 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cf5d1390-0dfc-3ff9-b219-0c45196976bb | -14.04062 | -43.8098 | 2025-04-03 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6467221b-1cc2-32d8-99df-2a60dcf45f62 | -13.40614 | -41.88021 | 2025-04-03 04:17:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5d849279-f0e9-39af-b431-846c9e9b616e | -16.61479 | -44.07782 | 2025-04-03 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d614034f-e393-3f0e-ba38-fe90b427e2ef | -19.53866 | -44.07851 | 2025-04-03 04:17:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d33fb875-5ea4-3992-9b81-37420a3e2914 | -15.60428 | -42.32088 | 2025-04-03 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6a4b26c-9487-3307-9c1e-71ed57963e10 | -17.77796 | -42.80671 | 2025-04-03 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda7883c-06c8-3b77-bc46-511ae0cfc5d8 | -13.03983 | -45.08897 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a397fbc5-45c8-3f99-b74f-4d644e46ae62 | -14.10707 | -47.69208 | 2025-04-03 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aec6b9e9-fb96-3dba-b2aa-b2b7d086245b | -14.10354 | -47.69145 | 2025-04-03 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9471989-ee77-3d54-a086-608609635a49 | -13.56832 | -45.25243 | 2025-04-03 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d71c4a8-549d-314f-8783-a911d95ab8fb | -12.6996 | -44.93883 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b01fa19-f074-348e-8121-a5f6f6b386c3 | -19.45371 | -45.30831 | 2025-04-03 04:17:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b269124a-ed1a-3680-8e11-d0e2e2ce4a43 | -19.71347 | -44.77314 | 2025-04-03 04:17:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59e493c6-8a4c-33c4-a669-8f7301ce5ce4 | -14.13315 | -47.66692 | 2025-04-03 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfab7a26-6f6d-39bf-9aa7-a7034a46c1eb | -25.1909 | -49.32803 | 2025-04-03 04:17:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a446c04-2f8a-3c72-b152-a341b7b46e29 | -12.1198 | -45.63308 | 2025-04-03 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcf237bd-c893-3581-8112-64edb8000d32 | -14.10493 | -47.66201 | 2025-04-03 04:17:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62067600-a1aa-3ccc-8f62-00da208c877b | -13.4829 | -44.03376 | 2025-04-03 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fbcd7b1-7101-3cdd-a0ef-03bfd6ecf645 | -15.54097 | -42.66586 | 2025-04-03 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 97e69c7d-8267-3769-ae08-3f9ee4bd597e | -15.0806 | -48.94485 | 2025-04-03 04:17:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de6db302-b4fd-3a53-a2a7-ae756b4f6e7d | -15.80445 | -43.57198 | 2025-04-03 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ad4606e-0ead-32f2-9ce3-2e9ad4f3ed05 | -19.85157 | -43.84473 | 2025-04-03 04:17:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9aa5a58d-7867-37dd-8acd-b1dc9314313a | -12.69629 | -44.93829 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06345b2a-f918-3690-ba09-1eb1436b94f7 | -18.56066 | -46.54534 | 2025-04-03 04:17:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 130a6815-aa31-3804-be14-a5d9f187c424 | -17.78151 | -42.80727 | 2025-04-03 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e30fbc6f-e26b-3f19-971e-3d267409e153 | -21.48636 | -57.08732 | 2025-04-03 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 748f5dfc-cc3e-335a-b4ee-0052fb0b1ec6 | -13.03208 | -45.09496 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fde5840-3556-388f-a24c-31cde8f7a139 | -13.03927 | -45.09251 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87bb343b-94dd-3c64-8df3-8278e751c081 | -13.56888 | -45.24887 | 2025-04-03 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d27300a1-89d0-3a29-a135-60b240b759a1 | -12.84798 | -43.83334 | 2025-04-03 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0bb37c4-1b5d-3d2a-935a-6d65b6ac1fbc | -13.0332 | -45.08788 | 2025-04-03 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d2a32b0-f6b2-3258-b9e1-07235681a7f4 | -13.56775 | -45.25598 | 2025-04-03 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6591ff86-9c64-3b1c-bfe6-8f629477b49d | -12.11922 | -45.63671 | 2025-04-03 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cb44022-0c37-3e5b-b8a6-60aedeb6fd4f | -18.13771 | -52.35749 | 2025-04-03 04:17:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc9f45ef-aea9-32de-b7dd-dc71de0eae3d | -16.34993 | -43.69486 | 2025-04-03 04:17:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
