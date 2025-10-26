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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8395bc9-a14a-34bf-92c4-bef99fba06eb | -11.39558 | -46.06184 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c399e49-ed3f-3a80-8d75-7a09af7570e4 | -15.29213 | -50.76289 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed2002aa-4590-3630-9ced-d269e0d2f384 | -13.3217 | -47.92934 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77543ed4-b3cf-3757-ab5a-befcc19e6f9c | -9.57368 | -46.92289 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ffd88c4-11bb-3e3a-b793-a4e11bfdaa63 | -13.9044 | -48.44574 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6cf81d7-d45f-38e4-a75d-dff8c1a1f990 | -14.77218 | -44.97357 | 2025-10-26 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb0c72fa-dc8c-3e23-a69e-dfc5c62acaa5 | -10.80251 | -47.86948 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9f9e8b8-5061-32bd-9ef5-20a610606d0b | -10.41302 | -45.32635 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 477992c9-53f5-3604-81ba-ce0548785f44 | -14.83532 | -52.45343 | 2025-10-26 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 903eb9ae-fcf4-3787-91b5-1accd0ccdbd9 | -10.99164 | -44.86664 | 2025-10-26 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d723dd8-cc23-30fa-bd3d-a96147d9c755 | -10.87018 | -50.14099 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21d1d3d5-1a21-3b9a-8f68-37ab597130eb | -13.8795 | -48.47841 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a214a46d-773e-309b-bee9-fb1a97b7fa87 | -13.32698 | -47.92523 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65cad7c2-7525-3476-ae50-7d93bbf17b84 | -13.89648 | -42.8206 | 2025-10-26 04:02:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9ee385a9-a9a4-355a-82b1-7bcd629283e3 | -10.62787 | -52.18522 | 2025-10-26 04:02:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83cc1675-820f-3494-91a3-533d65d6e9f5 | -10.8859 | -47.95551 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27bafc59-27d0-377a-8e7f-d45912e72865 | -9.43404 | -46.32739 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65cadc06-ef5d-3c40-9b26-9e7b60e3d42f | -14.77504 | -44.9785 | 2025-10-26 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71853008-1248-3328-8754-62bbecbde811 | -9.7395 | -45.50216 | 2025-10-26 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fd37b13-6985-3d79-bf70-87bc24036abb | -9.26021 | -45.59578 | 2025-10-26 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed5a53f3-daea-3c15-befb-bc0571d4ec58 | -13.89155 | -48.41533 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cecf4b0-dc84-3a6d-a019-837ab036854e | -10.98878 | -47.88335 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0351076b-ffc5-3fff-9f4b-5de692dec712 | -14.48108 | -45.26523 | 2025-10-26 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7edb7c86-4f14-3214-87ce-56ee3604f298 | -13.25228 | -47.98485 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 716caa58-ffcd-3510-8cfc-f2cff7dc6733 | -14.22358 | -49.51021 | 2025-10-26 04:02:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fad78cc2-6b19-3ca1-b7bc-b0e3cf4185d3 | -13.53538 | -43.01307 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| e5c3b85e-c359-3fbc-ab17-51ee6a377d51 | -14.91136 | -46.24501 | 2025-10-26 04:02:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d890650-6244-3621-969c-19d4dffa9791 | -10.39501 | -45.31433 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3efe7e02-2ea9-3d8e-939e-1d4e5bb4fdc6 | -8.72143 | -48.01485 | 2025-10-26 04:02:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6b7e438-8193-3d0c-91bd-5d5c49fa868f | -9.24849 | -45.61568 | 2025-10-26 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78069c6a-fbb3-3158-8fe0-dafdbc428756 | -10.20975 | -52.66799 | 2025-10-26 04:02:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3876fa2-ad62-34fe-abb1-d567ddd0c874 | -10.61003 | -47.99863 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 831c021f-1a4c-3fa8-b893-d7a47dc4b885 | -9.15717 | -51.30564 | 2025-10-26 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e32ccf4-011a-3189-8e88-9a8668db5a64 | -10.41643 | -44.50171 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4021d027-192f-3d3d-8901-6e7d4aaa93b6 | -12.22386 | -47.04409 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d8b9a67-bd1f-37e7-a527-a35d63dd6f1a | -11.65676 | -43.3144 | 2025-10-26 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d889275a-9e33-34f5-a7b3-818ce94d38eb | -14.21899 | -49.51348 | 2025-10-26 04:02:00 | NOAA-20 | ALTO HORIZONTE | GOIÁS | Brasil | 5200555 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 651279ba-48fa-3359-97d3-b57969c63cb1 | -13.75276 | -48.41773 | 2025-10-26 04:02:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e5c5ffb-3be8-34df-b3ce-f8cac93bb819 | -13.47486 | -42.50339 | 2025-10-26 04:02:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a061b029-30a2-359c-95c3-26f09ea2d896 | -12.58363 | -43.90874 | 2025-10-26 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28093b60-9cc0-30d1-9eba-4865f111678f | -9.57957 | -46.91504 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc137d07-7099-3d12-bd3b-90beab08d588 | -10.75277 | -47.90864 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c99d9ed1-b971-3d18-a1ad-1f89553e470f | -9.3068 | -45.22697 | 2025-10-26 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 23a79bc3-10a4-328e-a5be-39c47411d4a2 | -10.20128 | -46.56284 | 2025-10-26 04:02:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c421cfc2-a196-3c32-8035-6f0bdc157bc8 | -10.86384 | -47.94637 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28facc31-2478-3556-9faa-74cbd0a9f0e5 | -12.25242 | -47.75902 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84ab93a3-b463-3f63-bbd6-79ccc1f00522 | -10.53416 | -46.37199 | 2025-10-26 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 669cd5e7-28af-3f2c-a12f-2de9cecdf7e8 | -10.85764 | -47.95426 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 025df621-dbcb-34de-affd-f2b1bbd92c35 | -14.6536 | -50.18908 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77fbd5ae-aa53-3d33-8f12-e8ca15396c9f | -12.56511 | -43.97599 | 2025-10-26 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d7fa12a-b617-33eb-8535-2f0cece5ca5a | -12.30299 | -47.45283 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2aee9fd-af3f-3e95-8397-18d96714a79a | -10.87185 | -50.14316 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9033f158-9901-3d4d-b092-ba428b06b76f | -9.43264 | -46.33538 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 582121e0-700d-3bf5-970b-80d025795796 | -11.53502 | -47.09809 | 2025-10-26 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce1041eb-73c4-387c-a13a-d749e304c5a7 | -8.95878 | -47.17899 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0da932ce-864d-3115-b5fe-d353ef0883c5 | -9.98241 | -47.09335 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4b8bb0c-5a15-3e06-97c7-2c544d74a812 | -15.539 | -44.02105 | 2025-10-26 04:02:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4b9b5a2-ac14-37d6-9986-f425c2722900 | -12.12986 | -47.01016 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72f213bf-cf25-357a-b8b6-ff0d33de7e71 | -11.84474 | -49.85882 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190b061a-dcbc-3e88-bf60-12b7262cc301 | -9.0932 | -49.64535 | 2025-10-26 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75ddb2d1-7c3d-32de-a803-fc8e2b569e43 | -15.5081 | -46.79296 | 2025-10-26 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8dfb15b6-b356-33b0-87a4-887a08fb508f | -13.86142 | -42.48622 | 2025-10-26 04:02:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a0b9d052-3bdc-3ffb-a5d2-3ca3f9e0475d | -12.18881 | -47.75624 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 342b587f-79d8-312e-80f3-b84ad631ac61 | -13.3286 | -47.91626 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f208a70-50bf-3adc-a726-780429413fec | -12.17644 | -47.01788 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ba93465-f1ce-3ab6-a74a-f9ae33f21d73 | -10.88677 | -47.95071 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5202fb7f-3684-3788-9a60-fa0ba86f3fcc | -10.188 | -44.90701 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4fdb48f-e5bd-355f-ba0e-3e26f86daec2 | -12.09493 | -47.25258 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c08e46eb-f469-3428-9213-042bfebe50fb | -11.0285 | -47.87223 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b69dc587-7c07-3a50-be0a-f96793f6c9b9 | -9.96143 | -43.86244 | 2025-10-26 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75f73dbf-63c2-3c69-b5f2-d576519b7a6b | -13.88942 | -48.41689 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14baf754-7cce-351d-ba72-d7bc036a4b1b | -15.60582 | -46.78734 | 2025-10-26 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12883ab5-19af-3f34-ba39-43f1fd056bd9 | -10.87083 | -50.13761 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85f643db-8d95-3ff3-b74f-103a2e9a41fe | -11.03825 | -47.8704 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f1216d6-3544-320c-9f78-1b24ef3dc7a3 | -15.45993 | -50.48267 | 2025-10-26 04:02:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad36e857-e18f-33ee-b184-61bdc6d81e64 | -14.76457 | -46.6208 | 2025-10-26 04:02:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6420ab1-13cf-34c5-bf13-0909126ea344 | -13.87441 | -48.44795 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 738b756c-13a2-3bb0-9d4a-1e39e1070a72 | -12.17722 | -47.01348 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e349207c-67fc-34d9-a781-cd32861e0e0f | -12.02071 | -43.30362 | 2025-10-26 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faaab938-97ad-3399-bb91-ad6430fe4d60 | -10.77462 | -40.31637 | 2025-10-26 04:02:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| c124e028-ad3a-3136-84cc-f8aa65b9229f | -17.16263 | -43.34724 | 2025-10-26 04:02:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a14ccef-1a2f-3e5a-8134-f9680a497594 | -15.2495 | -50.76344 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87c06aad-6773-3a46-9036-8b9a1a548e21 | -13.82165 | -42.3761 | 2025-10-26 04:02:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd1fb41b-4382-318f-b64a-949942fa3b55 | -15.42074 | -43.76059 | 2025-10-26 04:02:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15e750fe-66d5-3f3c-a38b-d1f921af308e | -11.5368 | -47.09933 | 2025-10-26 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26b19699-eecb-3e4d-8960-a2444a1fa944 | -14.925 | -43.44679 | 2025-10-26 04:02:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6d011f7a-e44a-36cb-926e-3f06fba323df | -15.58465 | -43.19704 | 2025-10-26 04:02:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67ad7ee1-6094-3bad-bfe8-6c75b7704070 | -13.43546 | -47.39179 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eda3b5a6-fdb0-3173-928b-80e7c6e52f77 | -11.50979 | -48.23721 | 2025-10-26 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db36f6ca-7a55-3113-99c6-ec2141d76434 | -10.7884 | -47.61249 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e148cb6c-d462-3dd5-ae8d-3752ae483ec7 | -14.83621 | -52.44902 | 2025-10-26 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7706aa7-482a-3a49-a997-46a6d792e550 | -12.13571 | -47.00188 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf9b744c-0c30-39bc-9adb-e94f160fd84e | -12.36917 | -48.1072 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18e456cc-0eea-31a2-b560-a57ee5f79abb | -10.22255 | -49.85054 | 2025-10-26 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 023ae2ae-ebc1-3fd0-957c-fb9413dd0d9b | -11.53427 | -47.10221 | 2025-10-26 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71efb4c7-a1c9-3f12-9eeb-18fa0c071f32 | -12.17298 | -47.01281 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a89bfe62-ecc5-3c1d-a533-f6e6347169d4 | -12.02805 | -43.63238 | 2025-10-26 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2d1fea1-f2b4-3739-b196-b43b71003aa1 | -11.99949 | -47.15503 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 847cb58b-3904-3537-a8d1-ec676d24aa68 | -13.28844 | -47.51147 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebfdc2a1-2f9d-324a-b02f-2a9b6331bba3 | -10.76145 | -45.07788 | 2025-10-26 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README25.md)
