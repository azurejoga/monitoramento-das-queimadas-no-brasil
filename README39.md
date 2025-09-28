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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 277eb440-680d-3c1d-a457-9cc8e9067015 | -13.76606 | -47.87131 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54e029bf-53bb-3579-bdf5-d3359c841798 | -13.60011 | -47.32288 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd1f21ce-bf85-3b4d-8bb4-343b2d55e94a | -10.86167 | -47.76699 | 2025-09-28 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b26651f-225d-3ce1-ad22-63c5ae52fc01 | -12.10514 | -44.19899 | 2025-09-28 04:06:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c85e809f-2af6-3454-ba14-796445e67abe | -14.07086 | -48.83096 | 2025-09-28 04:06:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87dfd520-ff5b-39c7-b50e-83d962d5391a | -11.43177 | -43.51591 | 2025-09-28 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d131bea-3411-343a-8562-559ef6a0ed1a | -12.00434 | -47.04467 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc1a8878-2284-3684-8ce3-8ada7e8c8800 | -10.90219 | -45.75962 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb8eda92-e825-35f8-b482-f9e800462ccd | -13.60452 | -48.09287 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 767d069c-8899-3129-ab61-7073e8596df3 | -10.85233 | -47.79499 | 2025-09-28 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 083f36e6-a134-34cf-b03b-8bbc93c3c44f | -13.51402 | -47.39384 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9126f130-7e9f-3757-982b-21975f4af4bf | -13.60373 | -48.09719 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16983db4-122c-3339-a622-9bfcf2fd7996 | -10.41429 | -46.15165 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e200f94f-8eb0-32bd-9657-f8a94d8469b1 | -11.37633 | -46.97334 | 2025-09-28 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e730bd6-1d26-378e-8e2c-edf8b217adb6 | -15.44125 | -48.24217 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adf26392-7146-3a01-992a-18478c1245b4 | -11.62152 | -52.84992 | 2025-09-28 04:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b95a05d5-3a7e-3392-8712-8cad4c330f3b | -11.35131 | -44.9997 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 461e8cd8-1d91-3145-851b-6a74f256e999 | -11.36811 | -44.96761 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81be0de1-964b-38ce-840e-12d5eae98311 | -15.43419 | -48.23239 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40deb951-5ce8-3bab-8b94-a0285363348f | -9.89521 | -49.12005 | 2025-09-28 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0555a1ec-ae70-3d0c-bb03-f444befe6f1c | -12.95148 | -45.14857 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1659101b-2c52-3a3b-b1ee-9553afdc2ea8 | -12.89164 | -45.17617 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2495cd9-8171-3c95-8f43-da553ed2579a | -13.77241 | -47.89147 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9882926e-8f75-3120-8039-47373eb60e33 | -11.43123 | -44.96019 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d578ac8f-188b-30a6-ad0c-29decaf4695f | -12.059 | -44.8652 | 2025-09-28 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0950c67a-c631-3ac2-b56f-d34830d261df | -11.37155 | -45.01479 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 542336f0-65e9-3e63-9e07-25283682151b | -12.25647 | -44.0938 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a442f47-ba66-3b75-a6ae-471983e421a1 | -11.95061 | -47.93356 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6481412-d81b-3664-9b21-e336c0a9769e | -15.5366 | -47.92176 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c41e692-52c5-3d22-80cc-2bdd7ee3986e | -14.87917 | -47.98317 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e3c7e15-4fa6-3f23-a4d1-6b364d7bd29d | -12.43745 | -45.2064 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96e8daa6-487e-3df6-9cee-bc4e36fd2b24 | -14.58049 | -48.25323 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e84a6cef-388c-3314-8041-cff62f5e7eed | -11.40324 | -46.96989 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac7b1b4c-320c-328e-a6f5-450ef2d8951a | -13.39624 | -48.14929 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd69c10e-9165-3c78-b0b5-48f79984c86f | -11.95722 | -47.89754 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 719d8f74-2e30-328f-a962-b67c4bf1415e | -11.94249 | -47.92732 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae4b8b68-1d30-3d45-86be-3a17334b9fd9 | -14.93128 | -47.70086 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 866803fc-2713-3d50-a16e-52aa9e2bc23a | -10.91055 | -45.73434 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b2bb509-0d41-374f-becd-24a9a2a2d637 | -11.94613 | -47.93274 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4babbe6c-372b-3588-8e2a-78304595fa32 | -15.2924 | -46.43676 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd8a661f-0990-3b4b-a714-365403293380 | -11.40152 | -44.90836 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12d09a1a-be21-3340-8301-b323af76006c | -12.73392 | -46.81484 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a6b8f2-c4bc-3b41-bced-f87f0b1899e3 | -11.98746 | -47.04154 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d132aab-53e3-3d20-a935-343444884fd1 | -15.08981 | -48.33192 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d0fae31-c67e-3389-9ade-0a2b2980e945 | -12.00683 | -47.99004 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a4c54f5-d269-38bc-82a0-c9182d8b0265 | -14.88074 | -47.9747 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47e7e0ea-ac50-324f-beb9-cc3976077b76 | -12.87685 | -46.80003 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bbd1127-3ac7-38ab-a15e-09be635ad7af | -10.29356 | -45.42474 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 317da80c-075c-3041-aece-3b6fe23de554 | -15.25284 | -43.08828 | 2025-09-28 04:06:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 18.4 |
| dc9552c9-d6a8-3161-b291-201b5f61f2b2 | -12.68925 | -46.87441 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7b797ee-956b-34d9-98c6-65a15812ef86 | -15.62265 | -48.35821 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c8fd0af-2e30-33b3-9870-21e97b46fe39 | -15.0237 | -46.96723 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 431adf11-7395-3fe6-a3b6-784d17c3c1df | -10.91247 | -45.73774 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8dced9a3-2d12-32f1-8cdd-df32da3ad517 | -15.33153 | -47.88293 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f808367e-fef1-389f-a3f2-2caa0a594b15 | -14.46846 | -46.35294 | 2025-09-28 04:06:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb9a0a94-64de-3564-aeb0-bc464ec65c1a | -11.44919 | -44.99096 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0148f5ff-b00c-39d6-8648-2cd3989344c6 | -14.76742 | -45.67669 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204cca22-8d89-3de7-a8a5-ac305a39a110 | -15.20313 | -44.00534 | 2025-09-28 04:06:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de72eaf9-9780-34a7-b6b1-a8691df7a734 | -12.90589 | -45.16016 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 46a6b910-4e32-31d9-a521-1f41b7563652 | -12.94103 | -45.11106 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7454aa42-d1cc-327f-8f1f-18820f2e574d | -14.59237 | -48.2382 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be8ac9b4-e2b6-361e-859c-f0bf2303f210 | -14.44549 | -46.36791 | 2025-09-28 04:06:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbd5d949-136f-39e5-8c12-987858b6afa9 | -15.44094 | -48.2203 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82ae4a4e-f296-304a-ba81-b23a2e8a4e58 | -10.30109 | -45.40249 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ef5c9bc-8c6e-347d-9293-cd7172f4e6d1 | -12.68864 | -46.87779 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5414123b-884f-34dd-bc9c-ee6329921909 | -13.39568 | -48.16557 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 771054cf-edc7-3933-8893-a416aa15118d | -12.25579 | -44.09788 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64fd00ec-b8ab-3b36-a61a-60eb09f48bda | -15.22524 | -48.06118 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93a24c4c-4706-36d4-b2a2-386c648aaf99 | -13.34641 | -47.28831 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 693e207b-64f9-30b0-806f-7ad82594f9f7 | -12.90434 | -45.16916 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 971b33cb-f367-3dbb-b663-68ed90b592f2 | -15.05629 | -42.33745 | 2025-09-28 04:06:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 29.7 |
| fe497f36-418c-3614-b9bc-4101664a8d90 | -13.77554 | -47.87468 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50638fae-7159-3185-856d-9dbef1029b56 | -11.79526 | -44.91087 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bf3ca15-cd0f-35b7-a98b-aeb5a76ee77d | -11.98097 | -47.07729 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1c592c63-75a2-3610-871e-a55690a1c1e8 | -15.2568 | -43.0852 | 2025-09-28 04:06:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b0b2f2a-54a8-3cc4-a513-d73778d551dc | -12.94398 | -45.1162 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5b668804-ea86-38e3-94ae-8e8c4710086e | -11.99929 | -47.89482 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1b20995-cb28-3e7a-9682-4060f363f86b | -12.97732 | -46.85392 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 812f5ef7-31eb-376a-87c8-ff921b1e9917 | -11.99461 | -47.94638 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 516207e5-7923-3672-bc58-9c9b7bddd084 | -11.36082 | -44.94291 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21dac7bb-afb3-34b2-a6cf-44006d19d3de | -12.02027 | -47.93242 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3e8cb30-53c0-341d-9a84-70d62d803ce3 | -11.72076 | -44.41864 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ab911fe-22e4-3dc8-8601-660af54e1f5d | -12.0052 | -47.99067 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e4a4805-f22e-30fe-a5f1-61b24042424a | -10.58624 | -46.26998 | 2025-09-28 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 175804f8-1680-3cb5-b844-e431f4c82404 | -12.89075 | -47.10141 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2811c46f-b5ac-3cb0-ae2e-3bf49d0dcbf2 | -12.84902 | -46.89413 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17368d04-4e18-3ec1-9582-623c5fa43f50 | -12.9096 | -45.16082 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 36ad72ea-ba73-3639-98d3-246523fcadbd | -13.6307 | -48.06821 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc1014d0-20c9-34ec-824a-6e6196ee2a54 | -14.71388 | -43.95737 | 2025-09-28 04:06:00 | NPP-375D | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16353fcb-689a-32ef-baae-b63a2a1be6a6 | -14.58762 | -48.26343 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db8c01f8-63c1-33c2-98ee-5e114526428b | -12.0001 | -47.8903 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c6113ea-a639-3472-bc41-f453680b9628 | -15.21317 | -48.05471 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d54dd37a-d0b8-341a-baaa-b7ef1c379b8f | -11.3876 | -46.93477 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ebd7516-b687-332a-b63a-5e42486dfe70 | -13.84172 | -47.95358 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a2487d6-819c-3992-80a4-e26fb726b516 | -10.29675 | -45.42712 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f825978c-729a-31e5-af58-0c441103e6e1 | -13.63591 | -48.06464 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2188b38b-b544-3a87-b31d-a1cae4e6e119 | -11.97045 | -48.0029 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc319213-37d9-34e2-8f48-f9387d5b8ec7 | -15.89914 | -46.2035 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffe803ed-ef54-3afd-be86-c9a07ee5f025 | -11.60685 | -45.43124 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ce40b4e-0543-3ecc-b60b-65396c7da1f1 | -15.08465 | -48.33529 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README40.md)
