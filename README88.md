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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09a81d9f-6653-3060-8169-dc15290242f1 | -7.02132 | -43.43828 | 2026-10-05 16:37:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e48e5401-6b58-322c-947f-08bb5f2aff95 | -8.53163 | -54.58925 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3a6618b9-2160-377a-ba60-1f78d458bb65 | -7.19129 | -44.30434 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18f5a9e6-925a-34ef-b92b-7cc31442b57f | -9.62767 | -47.69912 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8847a7a5-f530-39f3-b11f-23a0a36bb406 | -7.92192 | -41.10284 | 2026-10-05 16:37:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| a340c8d2-1ec4-3b59-95c7-c83d859496a9 | -9.16455 | -45.1287 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f24618af-1534-3f97-be1f-2a66945b29c5 | -6.90096 | -43.68267 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| a64abb7a-7aa5-3615-b1f0-b116fbe2eafb | -6.63392 | -41.78255 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 88256f44-e831-3dba-a581-df896db5fe15 | -6.69822 | -45.22303 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 97ec7956-c8ee-3c85-b14c-20b39682d46d | -6.62972 | -41.7833 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| eb91156b-3686-3aa6-bf9e-c61580216e65 | -9.03015 | -45.1652 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 68f9244e-c84d-346a-bdf9-161fbf345a8a | -6.69837 | -45.24665 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d977d0b1-2564-3b72-944d-417addb8aeb2 | -11.16307 | -43.49648 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 08cc9f4c-88fb-352b-9770-bde2eda3ac72 | -9.03296 | -45.16092 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9d4d294f-986c-3f0c-b636-4b3448929b7e | -11.71967 | -43.50376 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| dd5615a7-95ab-3309-a721-559f37e04ff7 | -8.14721 | -47.09665 | 2026-10-05 16:37:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 92def0d5-21b3-3d60-aa07-bf49f016c948 | -7.67606 | -45.46107 | 2026-10-05 16:37:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8bb3ff1e-bfbe-3d2f-87c7-4f0aa35c54ac | -8.54419 | -54.58026 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 37a29d6d-b6d6-371f-a4c4-c5dced5e2b60 | -11.07759 | -41.25745 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de6ce335-a931-3fcb-b5e5-307d8186aa1d | -11.18972 | -50.807 | 2026-10-05 16:37:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2682390f-a8ce-3099-b877-5b6b7d15abde | -11.82572 | -47.16137 | 2026-10-05 16:37:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e1575c74-68fd-3099-9223-c24a4b391a99 | -17.92602 | -39.4242 | 2026-10-05 16:37:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 37173d0b-ca30-31e9-a63d-0c6692556467 | -8.52762 | -39.55088 | 2026-10-05 16:37:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 820629b4-3c20-3f28-a572-1e5eae42d1c7 | -8.58817 | -45.65987 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d95ba3cd-6384-3bf5-814e-df4d9d6f6280 | -8.54015 | -54.58604 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 18814bd8-b318-3fa6-8598-2d5ed4431725 | -6.73473 | -44.92319 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 32bfa32a-f8e6-3b3c-a2b5-2dd079bd013b | -6.85869 | -38.68604 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| b15d503d-32b0-314b-bfd7-d9eaae201e01 | -11.81609 | -47.36792 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c9a5dd25-c426-3da5-a712-26a47850cb12 | -12.82432 | -41.83112 | 2026-10-05 16:37:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ca4c7c93-617f-30fe-a3e6-98aecb21dcf2 | -9.41277 | -47.30897 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4da80454-b411-32bd-90e7-6da510c0ea27 | -11.21733 | -47.1342 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d6133e73-d02a-337a-b172-6c170692d452 | -11.72321 | -43.50317 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 07c9c7fd-c99c-328c-87da-fa26958a600b | -7.54062 | -45.40273 | 2026-10-05 16:37:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0edd7a6f-fb05-3fa9-b514-91a64a36566a | -19.5555 | -40.39099 | 2026-10-05 16:37:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d3ab95ae-4be9-39e6-b6e5-03b0cd1aaaa6 | -8.66103 | -54.57768 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6b5be904-5836-367b-8945-de0b0a6e27ac | -7.15936 | -42.42234 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8c182b7d-d939-35b7-8ce4-4df24baa8714 | -10.117 | -45.89228 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 9fc59450-00d5-37cb-b889-029874acbfbb | -14.08081 | -43.76496 | 2026-10-05 16:37:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 50a40805-5d2c-3625-b1a6-9b29ad3441ca | -12.4853 | -44.72644 | 2026-10-05 16:37:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 88e57761-2c3a-394a-9863-53c4719aab5c | -10.74062 | -40.25831 | 2026-10-05 16:37:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d708dde-24ea-3bd3-89af-9122e83030e6 | -7.65541 | -44.37162 | 2026-10-05 16:37:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8567bce4-099f-3f18-86c5-8990d0936a5a | -9.02276 | -45.16259 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 23f997c0-5e59-3320-8fc0-f8561dd31e44 | -19.32559 | -40.87643 | 2026-10-05 16:37:00 | NOAA-21 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9a13c860-83bc-368c-be12-b6ed34562def | -3.21501 | -57.88253 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 42043f7b-2c77-3d3e-9004-d91051365c62 | -5.48587 | -39.55857 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d91d69ec-4d78-3ef7-91a4-890e46c745b4 | -1.61225 | -55.91979 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4f1b47f6-ed28-33d8-818b-69810a95ca0e | -3.38558 | -59.42907 | 2026-10-05 16:39:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5cce5b3b-0503-3076-899b-175704e8dc7e | -4.29528 | -42.18677 | 2026-10-05 16:39:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 390588c6-b646-34d1-9efd-8ad19c9d7c2c | -4.9583 | -40.56419 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 9303317a-4660-3525-a123-3428578e5a6d | -3.28871 | -53.83539 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 45e1335e-9f93-3443-a6da-cd277b174b7b | -1.94087 | -54.71766 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 330e9d97-f22b-3ea8-81ff-d706d44e9fd2 | -5.09547 | -42.91213 | 2026-10-05 16:39:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 98c68aea-09dd-3b4e-9a49-f3ae62a7caee | -3.0808 | -54.18323 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 57eb48d8-6eca-324e-8e1f-dbc0e9dbdac5 | -5.95117 | -41.35525 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 204.7 |
| 4693ad67-eea5-3a92-a3a7-fc4a8bfc53da | -4.18471 | -44.30045 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 294ef3a1-694c-327c-98e5-cc4fee2d3a3e | -4.491 | -39.36875 | 2026-10-05 16:39:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ba8d4132-faa1-334e-8253-defde0096f54 | -3.21476 | -57.87938 | 2026-10-05 16:39:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 578099a8-80e0-36b1-b3fd-c44067e2034e | -4.37719 | -43.92016 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e8485b31-010c-3474-8e4b-f09573f07e10 | -3.74169 | -39.54664 | 2026-10-05 16:39:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 91350753-2aab-3f6f-beae-f0afcc35627d | -3.1127 | -44.28934 | 2026-10-05 16:39:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a67ded34-b98a-3944-a7ba-d93dd784cef9 | -3.05394 | -54.20745 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| b6139432-f954-33e2-8d50-eee71ad82022 | -4.79772 | -43.23478 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 45868d30-3f88-3b6f-9814-9f42d7dfb39e | -5.48092 | -39.5574 | 2026-10-05 16:39:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 236da115-8a65-337e-8a70-c13472c92646 | -3.53208 | -59.39857 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 053475b7-2a71-34e6-ab59-3a0454ac8875 | -5.83891 | -45.01263 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 13025518-db94-32d4-b798-0f7e3b046699 | -2.5782 | -57.14922 | 2026-10-05 16:39:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f65bcc3-9c8d-3b58-b679-d0360e0e5672 | -1.2929 | -52.87581 | 2026-10-05 16:39:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a4d50670-5f34-3a29-884f-d3fa93ed3a88 | -2.97201 | -53.26614 | 2026-10-05 16:39:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 95d2ad75-58db-33cb-a1c8-93167602e03b | -1.63193 | -56.0067 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 69de6f15-27cf-3081-962b-bcf03bf995ec | -3.09934 | -53.73182 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a7d20e4d-da28-36be-a6a1-d358a37e3ea2 | -6.04762 | -43.68625 | 2026-10-05 16:39:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9b14235d-573b-350c-88bd-dd4713cbc196 | -0.38548 | -52.07561 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e739f7f8-c2d5-3b5c-852f-c2b0d1965d69 | -5.84017 | -45.02052 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| d6e83160-d148-3a99-ae53-893822607586 | -3.74674 | -59.62749 | 2026-10-05 16:39:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8e1258f3-efa3-31d3-b46f-05e537cec1d1 | -3.09666 | -43.91777 | 2026-10-05 16:39:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 100db063-9630-3861-bb88-a51f2ee460a3 | -4.78965 | -42.57555 | 2026-10-05 16:39:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| f65df9ed-f6c5-3f5e-961e-f61df3089f25 | -3.13963 | -53.72915 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| c533ce49-5d9b-36fb-9b52-02e138ec3029 | -1.89219 | -48.51802 | 2026-10-05 16:39:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| d805bc72-3ae1-3fa2-988f-9e8817a93734 | -4.57442 | -39.5838 | 2026-10-05 16:39:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2e1723dc-2f91-396a-979f-46da384a92e7 | -2.76612 | -57.66492 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f2796915-95fa-31dd-af60-d8a7ea77959d | -4.35066 | -43.82829 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 83f0c0bb-315e-33ff-8d3d-36e7c3e4cfbc | -2.7522 | -51.55184 | 2026-10-05 16:39:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 536b6b6b-b9dc-38d6-a35c-445be8296056 | -5.84427 | -53.82078 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dcce6967-a7ae-34ac-abb5-fe03b42bf689 | -3.84449 | -50.31031 | 2026-10-05 16:39:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d6cc71b0-05f7-36fd-8030-c44a62eff381 | -6.1877 | -55.35547 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 52593823-57a3-3674-9a5c-2fe056edeaa3 | -2.77492 | -57.6498 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e48f4bff-8097-38a6-8152-985fca59ace5 | -1.55912 | -55.17184 | 2026-10-05 16:39:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9f36612a-0aca-3ba7-a58c-00ecaf2cfbea | -4.0534 | -59.36288 | 2026-10-05 16:39:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 59977874-6bf6-3dd6-9e74-08d2895a8f11 | -2.98513 | -44.31737 | 2026-10-05 16:39:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f8248e4e-b2b9-3dc2-8903-78d3cd3d2f5a | -4.55721 | -43.71256 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e4585b86-381c-34ad-8330-da931862b99d | -3.18725 | -57.23895 | 2026-10-05 16:39:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c978c85-fbe7-3cb9-ae2c-27145f2c30bf | -6.27295 | -43.25126 | 2026-10-05 16:39:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f152497b-b47e-3d5a-a743-60a28f2b5b39 | -6.10387 | -55.67521 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ee9133b6-201c-32f7-b762-b10e118adcca | -1.46879 | -54.77931 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 438cce53-0e64-3dac-96bc-89a3840374c6 | -3.35308 | -42.90529 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3921f0cc-8f3c-3774-be40-a59b9904289b | -1.10861 | -46.64265 | 2026-10-05 16:39:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26860f8c-46b7-3c74-ab94-0b64395a52cb | -5.83539 | -45.01317 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fafa5001-56c2-39b0-bd43-a0b29e331da1 | -5.85298 | -53.81974 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 73833b73-5f66-32c7-8f93-9eb30e0dee7e | -1.66529 | -47.62919 | 2026-10-05 16:39:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6e0ad1b8-9ae3-370f-8a9c-413e0f64ba7b | -3.37649 | -58.20462 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |


[Clique aqui para ver as próximas entradas](README89.md)
