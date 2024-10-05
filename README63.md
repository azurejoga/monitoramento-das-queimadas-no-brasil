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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cea47a62-cd15-38ba-b2ee-568b9a61e6bc | -7.75361 | -43.04868 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 55f36e57-b37e-312d-89ae-60909ea2f0ae | -7.75257 | -43.07704 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 043f99f9-4788-30fe-8ba0-2e0a89d45125 | -7.75028 | -43.04815 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b2f6ad74-be7e-3151-92c7-a74bd57339d0 | -7.74974 | -43.05164 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1c7d146a-f5bf-32eb-85f0-f769f94a36f6 | -7.74735 | -43.05143 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c6a38733-6a16-395e-abda-868917b8611c | -7.74681 | -43.05491 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7b73ea8-cdb1-3dd8-9e73-cd191c84e824 | -7.74408 | -43.0723 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5dbf4459-4367-3c12-bcaf-359c6607d497 | -7.74354 | -43.07578 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 04766632-4014-3ef0-b40f-0a2213de81e1 | -7.74294 | -43.05787 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dcc69667-e4e2-356d-9beb-e59c8daf76c3 | -7.74239 | -43.06134 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8fb01127-aea1-36ef-a1ea-b56dbd049e37 | -7.74185 | -43.06482 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b0b732e-509e-3f54-a7a6-a50eeb4937de | -7.7413 | -43.0683 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 68d84a39-58fa-3486-9f0e-f8af1cbee624 | -7.74076 | -43.07177 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2298b616-199a-3e6b-aa78-5d18eca2d568 | -7.6968 | -42.98278 | 2024-10-05 04:14:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5f1145ee-5acf-3d82-adeb-63cb9a8ac7c8 | -7.69735 | -42.9793 | 2024-10-05 04:14:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f9620bc7-f3a3-31b1-aac7-9695b864dd9c | -8.77375 | -44.8224 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 6933219d-6d45-3dfc-bd16-006e599375d0 | -8.77317 | -44.82601 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f8969916-3cb3-3dad-a6fa-43ba44bb37a9 | -8.77258 | -44.82962 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d9f68dd-b656-3d94-b9cf-2aae9e7ca0cb | -8.77155 | -44.81463 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d16698d2-3bfc-3eb3-923d-e4ccbd54acd3 | -8.77097 | -44.81824 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0d0f83c-ba89-3bed-9266-b784c4ca24c5 | -8.77038 | -44.82185 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ab1bd47f-1879-34fa-9824-c34d5eb17f9b | -8.7698 | -44.82545 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 7f72492d-d794-39ff-b16a-0143778e6f18 | -8.76921 | -44.82907 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 74c1ece3-cee3-3c6a-b1b2-9ab56dc55afa | -9.95194 | -44.08535 | 2024-10-05 04:14:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 73859267-3c34-3705-a72c-af24f51df028 | -9.95138 | -44.08885 | 2024-10-05 04:14:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ca4e29c-daff-34f9-b223-2d7e004cc4e3 | -9.95083 | -44.09235 | 2024-10-05 04:14:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67dca06e-d532-3883-a2f8-a99bc0375e81 | -9.94917 | -44.08131 | 2024-10-05 04:14:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f1c7b4a4-ac00-3ed0-80c5-3e8526f41f50 | -9.94861 | -44.08481 | 2024-10-05 04:14:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e38bc520-f81f-3461-baeb-34b3a6a7d6dc | -8.57124 | -44.08377 | 2024-10-05 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51c4b80e-fbb0-3aed-9a56-db650fff1974 | -8.37201 | -43.65722 | 2024-10-05 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b75ccc28-5f09-3264-935a-f56d94a5742b | -8.36869 | -43.65669 | 2024-10-05 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e347fe99-676a-36be-8e6c-0288d8645fa3 | -8.36814 | -43.66018 | 2024-10-05 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ae7eb12-101b-3dc2-b661-f7cdde0d54e9 | -8.36592 | -43.65266 | 2024-10-05 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50a964d8-741b-36b4-8806-b7927cedcf72 | -8.36537 | -43.65615 | 2024-10-05 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d07cc57-cbb5-35b9-b6c3-36e64d547137 | -8.3637 | -43.64516 | 2024-10-05 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e28d821f-c02e-3449-a001-4790f7b5cdaa | -8.36259 | -43.65213 | 2024-10-05 04:14:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6be888fa-e119-322c-a295-ac1c719d779c | -7.47081 | -43.98695 | 2024-10-05 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f3f63b4-3cda-34e2-9c89-2e9da6c7c142 | -7.43573 | -43.99224 | 2024-10-05 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1ffe6532-48e2-3dc2-be19-dc62d821d14d | -10.17351 | -43.90215 | 2024-10-05 04:14:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3a20c44-2d04-327f-9517-e45e2164263a | -10.13856 | -43.84265 | 2024-10-05 04:14:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75cd6cba-e356-394c-92e8-2bdc9f43bf90 | -14.01048 | -45.07153 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97f7759f-e6c3-3270-a486-b7929f289be7 | -14.04613 | -45.14307 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d9f06c0-4abc-3c5c-bfa5-6df76d75a6a0 | -14.0432 | -45.18287 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31a65dd4-0532-377b-9e4e-38f0fd87ce8d | -14.0138 | -45.07209 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a43861b9-5287-3172-9ca1-581adbba5b4c | -13.99366 | -44.03086 | 2024-10-05 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd787e52-2137-3431-b2c8-67441499b09a | -13.9931 | -44.03444 | 2024-10-05 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8e53743-027d-3032-aef8-3d9a282c64bb | -13.99031 | -44.03031 | 2024-10-05 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c128d031-83ba-33b8-a54b-145668ec3895 | -13.89225 | -43.96321 | 2024-10-05 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 884335cb-cbc2-3a03-8337-cac3550b4bca | -13.87324 | -43.78643 | 2024-10-05 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7830759-9781-3837-909a-3ceb3c5acbbd | -13.78637 | -43.6467 | 2024-10-05 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8738e9c6-8411-3fd5-99d7-d27f072e3922 | -13.16392 | -44.06681 | 2024-10-05 04:14:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71deee4a-a7fa-3944-84b9-848f482e768f | -13.01386 | -44.76225 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da29e8a6-533a-32af-bb4f-81b5e4ceb3ad | -13.0133 | -44.76579 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91920a16-3c74-3326-bed2-c37ceb25d89b | -13.00997 | -44.76524 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 74493076-5c11-38fa-94ec-96443820e2ed | -12.8839 | -44.62524 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f207d7b8-c019-3ba1-9330-b076895802e8 | -12.88058 | -44.6247 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e14ffbd-6ed9-3f70-94ae-15e218d3685b | -12.87726 | -44.62415 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5dd8ccf-328e-3e4d-9a9d-e4acdf1a2bb4 | -12.86452 | -44.61843 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12a16dc9-1446-3f39-a10a-8c1183733bb5 | -12.8612 | -44.61789 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1ae0cf9-1257-3cce-81d9-e814d6bc9713 | -12.8252 | -44.60836 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be0a0db5-2870-3fc5-876c-319d6e2aacc5 | -12.82188 | -44.60781 | 2024-10-05 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ade37745-1e5f-3bef-9a17-89b7f72db58a | -12.73417 | -43.48169 | 2024-10-05 04:14:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c65628a3-66d9-3767-89be-99bea125fe13 | -12.73137 | -43.47755 | 2024-10-05 04:14:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e865e33-0bbc-33e2-adac-43c2948b4e8a | -12.73081 | -43.48114 | 2024-10-05 04:14:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af099806-215e-3a8c-a5b9-9f6c1b6155c8 | -12.43939 | -44.46191 | 2024-10-05 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d07bb169-bb07-3018-bd12-cbc69ddbbfff | -12.34959 | -44.62434 | 2024-10-05 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f937b98-99ff-38bb-adcf-4926ecfa0716 | -11.76375 | -44.64899 | 2024-10-05 04:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d9619d9-1018-3fd9-8fe9-c620ccc2ce33 | -11.76043 | -44.64845 | 2024-10-05 04:14:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d343547d-2758-397b-8aa7-33f2b212bb9e | -11.73069 | -44.96369 | 2024-10-05 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d32d6d1-b285-3566-809d-2ce7f2600039 | -11.69761 | -45.25587 | 2024-10-05 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5d1abb6-ed50-3d04-ac5a-d455a9730d01 | -11.67414 | -45.25187 | 2024-10-05 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee2e3608-0465-3944-9d6e-337c5cfb9e8b | -11.67356 | -45.25546 | 2024-10-05 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77e7954f-e4e6-3173-8c33-823656fa517d | -11.67298 | -45.25908 | 2024-10-05 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed2a5125-50b2-35b9-bb62-970089b09716 | -11.44253 | -43.83104 | 2024-10-05 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3a2c636-ae96-3d31-baec-63e7bc8641e6 | -11.32875 | -45.52684 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 622e527c-32ff-3a0c-85f6-d0cdf1cadef1 | -11.32537 | -45.52626 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79c1f7de-4b73-39c5-a03c-7cfc79af03b9 | -11.31802 | -45.52872 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 297079d2-719d-376c-a18e-515914d07a3a | -11.31464 | -45.52816 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 459f5d53-c74b-3568-a296-0fb9b139195e | -11.30837 | -43.38953 | 2024-10-05 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98015672-3316-3165-9b8a-a4699705a2d3 | -11.14954 | -45.03736 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3929b8b0-b1c6-36fe-b6a0-6a22b7c1716c | -11.14676 | -45.03324 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e3df7c4-0019-3135-b823-aacbfe4a8c42 | -10.98583 | -44.43638 | 2024-10-05 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 510ebd67-7b38-3b5c-9c65-c3541f43312b | -10.8405 | -42.84734 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12f26a07-88c5-3026-a485-c26860127a49 | -10.83994 | -42.85095 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0bccc3c7-5a68-32a0-bffe-745a29fc8d5e | -10.83939 | -42.85456 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cebc3ef8-2a8d-3b5f-8602-2635cbef50ff | -10.83768 | -42.84321 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76add002-6292-30e2-b637-0d021c89c2fa | -10.83713 | -42.84681 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c05ac8a0-1388-386b-a97a-d9a3a2185339 | -10.83658 | -42.85042 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f84d38b3-ef90-37fd-8d35-c3b96569883a | -10.83603 | -42.85403 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 51f5f19f-b591-30ea-93fb-771932acb340 | -10.83547 | -42.85764 | 2024-10-05 04:14:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 54bbb087-af14-36ef-a7d4-348b61b2fd93 | -10.82292 | -45.52297 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b517d560-75d3-3cd8-8dc2-45612e11f4a2 | -10.77327 | -45.54926 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3ff6514-5168-3848-9741-4bf50faa4843 | -10.76987 | -45.54868 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 927f61a8-21d8-32c5-99cd-abb6559bc4e6 | -10.74449 | -44.61396 | 2024-10-05 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b2ca0b3-de4e-3348-a6d4-89a6e6ff5c9b | -10.74116 | -44.61341 | 2024-10-05 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f830dc17-893f-301b-87a0-7facd7049709 | -10.73932 | -45.60783 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc4060bc-9889-3f74-ab52-95806be02f41 | -10.73873 | -45.61145 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57694bd3-0254-398e-8944-c196d753b53a | -10.73813 | -45.6151 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d7e3dde-2bf8-3dd3-8452-ca947c3090da | -10.63643 | -45.20493 | 2024-10-05 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 559b70a4-12dd-3a10-8e52-ff4fef9943e0 | -10.63585 | -45.20853 | 2024-10-05 04:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
