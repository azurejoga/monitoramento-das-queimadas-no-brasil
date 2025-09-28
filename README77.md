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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac2f2039-b275-3151-a065-6260a806f7ae | -15.03091 | -46.9649 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d10d87e4-9e0b-3bb2-8c71-ce3009a4490e | -15.43118 | -48.21363 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b31aad8-4de6-3727-8941-92ca5ad2793e | -15.44434 | -48.23776 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7865b282-8b2d-389d-9446-1719ff0a8138 | -13.64754 | -48.06849 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 622d2a93-c07f-3140-8532-326c759c7b4d | -15.81179 | -56.4211 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7879f4fd-6b5d-3209-add7-eab5b5b9e689 | -14.78843 | -45.64273 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc805998-cb03-3896-9f0f-afcae6ce6774 | -15.08376 | -48.32816 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a6c8e24-d976-32ee-9d2e-5b0db01e0444 | -19.32328 | -43.80548 | 2025-09-28 04:27:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9d60458-e44a-3485-88f8-e29157518558 | -15.19883 | -50.09688 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c04e2a8d-36da-387f-b8c0-15948fca70a6 | -19.31733 | -43.81987 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf647d9e-a95a-3e7d-9a88-8a79e5e0516e | -13.58785 | -47.30325 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16736d60-e5fb-302f-9e7a-7695c1256a20 | -14.49989 | -48.55972 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fddda9af-ffef-3949-a80f-cf8c525e5cb8 | -19.75363 | -50.09966 | 2025-09-28 04:27:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 891b073f-ed8d-3495-a11e-554a580b9ee1 | -13.7743 | -47.88914 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30349b71-c096-3200-8821-8ddf61f3b96d | -19.86963 | -43.80088 | 2025-09-28 04:27:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 5b7d1b00-390a-3600-9927-28fec5cd897a | -19.9889 | -42.33924 | 2025-09-28 04:27:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d886b352-7615-374c-b680-cc245cb2100e | -15.27669 | -46.45176 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea618474-27f4-3fc2-a928-0c3b79092136 | -13.60493 | -48.10144 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df9bd55d-a6d4-333f-ae86-887fbedfa416 | -13.57125 | -44.44094 | 2025-09-28 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5510aa5-4edc-35f8-a65a-7c10e63e3692 | -16.9653 | -53.69374 | 2025-09-28 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0b83f576-6030-3b52-82b0-a910b013ff9d | -13.37854 | -47.92203 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da8fbf76-e6bc-309b-9ab1-fdb945cdcc8b | -15.21085 | -48.06067 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f90e1f9-a6ed-363e-93ee-2094222be3fc | -16.40081 | -43.72261 | 2025-09-28 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 60ad4301-c65c-33c0-bea3-8a99bc19f416 | -21.39672 | -41.00074 | 2025-09-28 04:27:00 | NOAA-20 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8ed7cdc1-a3fd-3753-be74-3cd762e2b926 | -13.60331 | -48.09027 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed7d5f8b-5c44-3091-b3f0-45f42e5bfa3a | -15.70547 | -47.80453 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 185620ed-ab9a-3838-9b3b-acce82829099 | -14.77042 | -45.66819 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94d10f2a-cfeb-3dc0-be33-5a358b2ee80f | -13.26019 | -48.45179 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d019561-8c18-3c03-84f3-876e4bf146f6 | -13.59395 | -47.32962 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd55564b-8675-3095-b9af-3ba747029e0f | -14.31945 | -52.92966 | 2025-09-28 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39f6bfb0-441d-381c-944c-1af71e46df5c | -14.77448 | -45.68907 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2377d9e4-9e93-3b74-b36c-09dcc4758f0a | -13.79294 | -48.32869 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f09237e-a846-3ce3-9dcd-6c8f7575e978 | -19.24233 | -44.0784 | 2025-09-28 04:27:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d8ce777-e72f-3340-9b38-896acf7a1aee | -15.26679 | -56.80497 | 2025-09-28 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e5c24a8-022c-3a1d-9381-ee6ebf937b63 | -14.48021 | -48.57859 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3bc3a77-673b-3f66-be20-72ddc5dee70b | -19.20367 | -44.06241 | 2025-09-28 04:27:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0842261b-7990-3859-a32a-45c13ac3a72c | -18.87036 | -47.13629 | 2025-09-28 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5871ed87-e336-307e-a329-dd8a67d9393c | -17.18832 | -43.38996 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96bef73f-3217-3e07-bd3e-e71b5aa4fbe4 | -15.54607 | -47.89212 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afa7ebaf-eaad-3f41-b3e5-1aa2f72547d0 | -15.96651 | -50.87321 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6e733c4-7343-3ef3-9299-17ad2a358daf | -13.62624 | -47.31674 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1793fe1f-f82f-382e-a2e7-c204db5d2618 | -18.17694 | -53.33503 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2f00182d-5c00-3fea-9294-7cb196c2325d | -13.39836 | -48.1616 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 719c36ff-eea0-365a-b0b4-a5fe7f79fcee | -15.44547 | -48.23062 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cb5e7e67-8258-3900-b9d4-77292df59aac | -20.12583 | -41.71912 | 2025-09-28 04:27:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1044039e-2825-346e-9ebd-658fb8ed62af | -13.61493 | -48.08127 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3e2e3c3-b5b2-35af-afcb-4252afb402c0 | -15.89104 | -46.22334 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ed5842-f09a-3ee6-b31f-636fa43485a5 | -15.54328 | -47.91 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36c2ce85-5c42-3225-94df-5fcbd3c2ddc6 | -15.778 | -50.16102 | 2025-09-28 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9b49df7-0e6c-3784-aba3-d4370debab73 | -15.28862 | -46.44183 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ec30939-51b1-368a-ab1b-800d9a120a35 | -17.72781 | -46.70585 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a08f5296-742a-3587-a37b-20df74fec87c | -13.78041 | -47.87199 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24ae2463-448b-34f7-bdf6-cab0f0c372c2 | -16.95543 | -53.70279 | 2025-09-28 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 27fe88cf-cecc-39eb-b7f5-a27042c90952 | -20.12111 | -41.71854 | 2025-09-28 04:27:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5833a647-6f91-3455-ac03-64110f5de8ef | -13.4028 | -48.15507 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d1f9569-eea7-3aba-8aab-366bc81d27d2 | -12.9956 | -49.45447 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 791f9af8-5965-37a2-918f-0a0bd38d8101 | -15.44603 | -48.22705 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 811f77bf-cfb8-3885-9e40-1fec80d543d4 | -14.56356 | -46.93566 | 2025-09-28 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7edd8991-65a2-320a-b845-e7cbb0a3b997 | -14.46615 | -46.3512 | 2025-09-28 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf2b3950-638c-3b93-bf23-a4ef1f0ed4c5 | -13.64947 | -42.38653 | 2025-09-28 04:27:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 30d07088-52c0-3d0f-b044-b9481c3ff39a | -15.78943 | -45.3853 | 2025-09-28 04:27:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33a11028-5a27-3c10-b547-252f0d7e591e | -14.87938 | -47.98725 | 2025-09-28 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18e307d0-ecc0-33c6-8468-fc7fe366d98c | -18.2914 | -47.68803 | 2025-09-28 04:27:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d43eb86-8ae2-3122-9e8b-a2c2bdfd4e5f | -16.96134 | -53.69289 | 2025-09-28 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d1e98e57-62d7-3731-8a25-e2c38f92d7c9 | -13.74835 | -48.31 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6eb63b8-9d68-333d-a98d-a1404b6b9a2b | -13.00519 | -49.45992 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 81ff225b-80b0-386e-b8bd-526472665486 | -13.59781 | -47.32664 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3de28cd1-5ca9-3453-aec1-17d08dc58b78 | -15.61301 | -50.3093 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7e5f6e7-e08b-361d-8311-37798b9667fb | -17.71692 | -46.70805 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61f11bd3-6124-3c7a-b8c9-d8b4baaf694b | -13.26626 | -48.45649 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72b8024d-d1f4-3d0d-a6a3-571c23b32466 | -13.28996 | -50.68921 | 2025-09-28 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ec6d7be-0142-39e2-9010-0b74314f71b7 | -14.76924 | -45.65187 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcdb62a2-7809-3265-90b9-a2cb0e2b227f | -13.60387 | -48.08674 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3c248e6-31db-3b63-b29e-718db3385a89 | -15.77863 | -50.15722 | 2025-09-28 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2976c63f-dc50-38d0-9f88-35ad200813e6 | -13.62324 | -48.07176 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5f420bd-28d2-3dd4-8b3e-23c8d7ca23a6 | -13.51213 | -47.3964 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50d16fad-fae3-3629-a390-04bf2b9d85e7 | -13.60436 | -48.105 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fddac0df-77b9-3f84-b715-067a07150428 | -17.18166 | -43.37793 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0abfe238-44f3-3079-9817-434eb5edfb33 | -15.46553 | -50.2246 | 2025-09-28 04:27:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d540dce-7806-38ea-9895-248b6ee67909 | -13.00646 | -49.45218 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0f0092a8-89f9-3ed4-9afc-66a545241e24 | -13.34226 | -47.28879 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88c04bca-998d-323d-83c0-6eb59d06d0e7 | -14.43703 | -44.88071 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cce15b17-c1bc-318e-ad9c-382b1b9c8356 | -13.80132 | -47.91177 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eeeb6968-8102-3f20-9beb-29d328239bd4 | -15.62604 | -48.35606 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac1da5d2-b58e-34ef-a2e3-af5f7799d793 | -15.21691 | -48.06534 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d9aba57-1cb9-3ca3-86cc-301346b9b825 | -14.0687 | -48.83329 | 2025-09-28 04:27:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e63f222-6f11-3d44-828f-408c60584533 | -13.72525 | -48.66505 | 2025-09-28 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00115a66-5335-3c4e-86d0-1a741de7c0a7 | -15.88815 | -46.24292 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2fd0f83-aa7d-38e5-8c37-4ff8362ec271 | -13.39673 | -48.15046 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5049f2d1-9766-3549-be36-f1d8a62dafaa | -19.31421 | -43.81178 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3de9094-f47c-36bb-a3f1-36fdae359d89 | -13.0037 | -49.44765 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c472f2b2-286d-32f2-a0b0-86b95ebc9be9 | -19.32281 | -43.80923 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6011db07-7472-3436-948f-0b798c3471d6 | -14.53319 | -48.41529 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efad8124-02cb-386a-8c28-9f9f1a78aee0 | -13.61661 | -48.07069 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78344ddb-f55d-323f-8db9-6be461026301 | -15.81469 | -56.42385 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae810372-3923-326e-b62b-5d0b0909560a | -15.26995 | -51.46465 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a093f435-89e2-38d4-8140-4ed1be0df295 | -14.59011 | -48.24969 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7f3c957-b1aa-302b-9642-2552fc02bf13 | -13.75168 | -47.88177 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b5eb41d-d144-3c3c-a902-84f279415645 | -12.98664 | -49.44521 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d726ac09-212b-3ad4-bb1d-afa48f8efa58 | -13.34835 | -47.29339 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README78.md)
