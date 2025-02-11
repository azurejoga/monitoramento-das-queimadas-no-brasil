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
| 15252fec-6114-3810-891b-9bf0603f4e20 | -8.35922 | -45.18596 | 2025-02-11 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c70573ee-e98d-3cf2-8ff3-5351d8056144 | -10.59221 | -44.7836 | 2025-02-11 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e9f78b2-f531-3475-8742-518675a05c51 | -6.97382 | -42.82155 | 2025-02-11 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a80ff6f8-5ffa-3aff-975f-7cac9268d347 | -6.53146 | -43.10151 | 2025-02-11 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86d66e7d-a6bf-3456-8b10-92bd870a37ce | -12.13873 | -38.31144 | 2025-02-11 03:55:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed5825bc-50ea-388b-9be0-33bb04c29046 | -7.24288 | -44.71513 | 2025-02-11 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92c2850e-e867-339d-bf85-756ee9054cf9 | -7.92171 | -44.88243 | 2025-02-11 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 984779c6-583a-33ed-83f7-ac5ec43ed717 | -6.98223 | -42.9939 | 2025-02-11 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f21a085e-bca8-3b6f-9c78-d8426d0134be | -9.8784 | -41.80069 | 2025-02-11 03:55:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cc9e8ca8-8284-314f-aaf3-24f0eb6dfee4 | -7.23425 | -44.71364 | 2025-02-11 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d083384-b06b-3c47-af40-302080e1c7ad | -8.35484 | -45.18522 | 2025-02-11 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05b480f9-e75b-327d-aa6c-5db88d6ee2b4 | -11.54111 | -40.41701 | 2025-02-11 03:55:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39702a6c-941b-36d2-ac9b-33a24e2be7a5 | -8.51425 | -36.64812 | 2025-02-11 03:55:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cd2c598f-7eb5-30f7-be57-627912255aa5 | -6.97511 | -42.82488 | 2025-02-11 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e340c094-2282-3bca-9f68-a6ce3f6cf5ab | -6.97895 | -42.82553 | 2025-02-11 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7078bdf-8b7a-3dbc-9304-c90534430c5c | -7.9199 | -44.8833 | 2025-02-11 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 553b8883-4bad-364e-ab2d-ab084a0ae758 | -7.72734 | -37.48792 | 2025-02-11 03:55:00 | NPP-375D | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 219202aa-7344-3880-bb3a-d34a313c5122 | -6.97687 | -42.827 | 2025-02-11 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89983697-3186-3f7f-a144-08b24c9def5b | -7.24651 | -44.7199 | 2025-02-11 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 284c4a09-ed43-36c0-b3cb-95803e554ee0 | -5.60714 | -37.89521 | 2025-02-11 03:55:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9baa3765-0c8b-345e-9a4d-ee3ecda0629e | -7.24219 | -44.71918 | 2025-02-11 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ac330ec-7bd8-3749-88ba-ad40d0872a0e | -6.73512 | -39.99507 | 2025-02-11 03:55:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9da35d3d-d011-3601-8c78-d91d93ed7f19 | -10.59286 | -44.77986 | 2025-02-11 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17ec7c18-5f5c-3af2-b986-520e5e3b28f5 | -8.70934 | -36.16193 | 2025-02-11 03:55:00 | NPP-375D | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f19fe50a-206d-3d8f-ad4c-6b99c56bc3de | -13.48002 | -44.01847 | 2025-02-11 03:57:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f7c33e7-56a9-3dac-b31a-b47f308be100 | -18.53197 | -39.93654 | 2025-02-11 03:57:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4d595eb2-7b31-3380-80c2-8efe38fd6b99 | -19.6362 | -40.96299 | 2025-02-11 03:57:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7cf473b-858a-36de-8933-7824d7b8f1b0 | -18.53648 | -39.92955 | 2025-02-11 03:57:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 430e3278-7cc6-36cf-aabc-757718bdb004 | -12.85135 | -43.82419 | 2025-02-11 03:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ade3b8b4-f90c-3591-a89d-73c526b7e7b2 | -18.76953 | -39.86477 | 2025-02-11 03:57:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ebef28f9-39b5-3655-a8c2-87a97a2f7177 | -18.76613 | -39.86421 | 2025-02-11 03:57:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 70f94c67-b025-3e4b-a32f-d29982576bca | -12.89382 | -45.05371 | 2025-02-11 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10fcf30d-23e0-3aa6-a7ac-b72311726d98 | -12.84386 | -43.82285 | 2025-02-11 03:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc3015d0-8095-3361-918a-d4835ac6a8a3 | -14.13398 | -41.69096 | 2025-02-11 03:57:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85818006-efed-31e2-ba9f-c41efff91dc0 | -14.11884 | -41.67722 | 2025-02-11 03:57:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9bb7d7b0-715a-33e9-96e7-3d7ef90a99f4 | -18.53592 | -39.93333 | 2025-02-11 03:57:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5b5d63d5-0355-3e8e-8d29-9c9c19c59339 | -16.34922 | -43.69447 | 2025-02-11 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d89bc525-6dcd-30fc-ba23-945eed1a60c8 | -13.48378 | -44.01905 | 2025-02-11 03:57:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c47c1c6-2987-322b-80b3-7231b73dc189 | -18.62647 | -40.34598 | 2025-02-11 03:57:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e48ef761-ba5a-3346-8ada-bb9e4863cfbf | -18.6259 | -40.3497 | 2025-02-11 03:57:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 74273723-9d5a-30e1-8253-f7a21978eadf | -16.11049 | -46.20083 | 2025-02-11 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94d8c245-9d26-3404-b5a8-9af107cce32d | -19.22611 | -42.54857 | 2025-02-11 03:57:00 | NPP-375D | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5cb0f5ae-253f-365d-a270-86fe0fd9f4a0 | -18.53253 | -39.93277 | 2025-02-11 03:57:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eeb65c13-6a66-39d7-a1e9-9fc930f3271c | -18.5331 | -39.92899 | 2025-02-11 03:57:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ccbbafce-ca35-39d1-aa25-a6b824c04c89 | -12.64783 | -43.81623 | 2025-02-11 03:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2451a1a-ea6c-3cc5-b2b5-923c1bec638d | -12.84761 | -43.82352 | 2025-02-11 03:57:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3f4b3c3-82c9-3dcb-9792-2c2c77356a6a | -20.27747 | -54.99608 | 2025-02-11 03:59:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 995bfe6c-9954-3682-a31d-154f20a1c79a | -21.35492 | -48.6154 | 2025-02-11 03:59:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 020c98ad-90d3-3685-a81c-53ca8e1a16a9 | -21.47157 | -48.57478 | 2025-02-11 03:59:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 991abba6-1da8-3c32-9a1c-a56d4e33808f | -23.23524 | -51.28623 | 2025-02-11 03:59:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d1bb617-ae09-385f-83c9-4347dd466bd8 | -23.63711 | -47.07161 | 2025-02-11 03:59:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c344f493-0c7b-3e79-a2d6-0e4f3a7a9b3b | -20.28173 | -54.99738 | 2025-02-11 03:59:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38f60c4a-27a8-348b-a2e0-b25aacb4c5a9 | -23.98239 | -48.9174 | 2025-02-11 03:59:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41be071b-11f8-3f2b-8f11-22b15a5d411f | -21.43973 | -48.68874 | 2025-02-11 03:59:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7df625e9-4f4d-3a0e-8412-99fc4ed8223e | -20.28678 | -55.005 | 2025-02-11 03:59:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ab49264-93fc-3a28-90fc-6a151441446f | -21.89427 | -53.71725 | 2025-02-11 03:59:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bda5d0e1-3503-379d-905c-e24b44d5625a | -23.33938 | -46.77037 | 2025-02-11 03:59:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ea3e2d5c-a99d-3733-a176-79d6783d4d84 | -21.88733 | -53.72044 | 2025-02-11 03:59:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f499e03-058e-3020-a496-79892e936ad1 | -21.62446 | -43.46561 | 2025-02-11 03:59:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58de358c-6716-35f6-afad-f1bbe29aa454 | -20.48232 | -47.53585 | 2025-02-11 03:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1d42f19d-c13a-3624-886e-a508951bf337 | -20.28389 | -54.99802 | 2025-02-11 03:59:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2feb28a5-65b5-3785-aeae-3630b6611017 | -20.76112 | -46.76998 | 2025-02-11 03:59:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| add0f9ed-ef5e-3cbf-8c88-fa1fc3d557a3 | -22.52733 | -45.54959 | 2025-02-11 03:59:00 | NPP-375D | PIRANGUÇU | MINAS GERAIS | Brasil | 3150901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eb0517da-70a4-3472-ba16-e48ee5930599 | -20.28815 | -54.99929 | 2025-02-11 03:59:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0609bb27-f2ca-3155-8056-4ad7a35b7237 | -21.60454 | -48.45345 | 2025-02-11 03:59:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ae2c035-ae9f-3f43-ba4f-74b9ab226ad9 | -21.05153 | -48.47652 | 2025-02-11 03:59:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e6ef2198-e8d7-3915-b588-4afcb8fefd57 | -21.60537 | -48.44925 | 2025-02-11 03:59:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90bb808f-3600-340f-8361-d1df39707f37 | -21.06194 | -48.46955 | 2025-02-11 03:59:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30c2668a-f917-31b3-9bc3-8a9b5883e62d | -23.33847 | -46.77524 | 2025-02-11 03:59:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 264444bb-472e-340b-8425-d3e3748ef9b8 | -21.60025 | -48.45257 | 2025-02-11 03:59:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43628dfe-4fa5-3660-9cce-86fe9a3298c3 | -23.40624 | -46.55654 | 2025-02-11 03:59:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 84f5ab39-eca1-3feb-9498-7744dd67a418 | -20.48309 | -47.53188 | 2025-02-11 03:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e770bb5c-3608-3609-8454-5b7ff9c6163f | -23.9866 | -48.91835 | 2025-02-11 03:59:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5d7401-0bd6-3b98-bcda-b05bc46d8441 | -21.44409 | -48.68966 | 2025-02-11 03:59:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2746b7b-a06b-3b5e-b81c-948a28773e51 | -21.89533 | -53.71269 | 2025-02-11 03:59:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8242a3ff-d0bd-3a4f-a25c-86a12d7d9dd0 | -20.28256 | -55.00371 | 2025-02-11 03:59:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 592b6d54-997e-34b4-94f2-143bb47af9a6 | -24.24244 | -50.74233 | 2025-02-11 03:59:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| df6b783f-9a8d-363a-a89e-c0cba1409dca | -20.479 | -47.53084 | 2025-02-11 03:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5694e469-bcb1-350b-8f29-35bf2c82ec34 | -20.47822 | -47.53484 | 2025-02-11 03:59:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba68479e-423d-3550-946f-0bad36633df0 | -30.19188 | -56.6857 | 2025-02-11 04:01:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 176a651c-e2bc-3b19-a122-21b5ecfaebf2 | -30.30896 | -51.8988 | 2025-02-11 04:01:00 | NPP-375D | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 57207f1a-fd54-33b3-a7a7-2247fd8c5142 | -32.20283 | -52.26624 | 2025-02-11 04:01:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| aa27b8e5-2d7e-3b05-a4a8-d24e9ba1a582 | -30.19065 | -56.69036 | 2025-02-11 04:01:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 518c550e-9959-3800-9b1a-a13bd50530ef | -30.19634 | -56.69242 | 2025-02-11 04:01:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| b86a41b8-9d91-3d9c-81c9-cafbce37ecdb | -32.20176 | -52.27111 | 2025-02-11 04:01:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 811af8fb-cd55-3858-a629-870e85dd5513 | -30.1871 | -56.68628 | 2025-02-11 04:01:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.4 |
| b1f38ba6-6429-3ce0-9288-13f6c14d88f3 | -32.1942 | -52.26361 | 2025-02-11 04:01:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| b5703e36-2fb6-353f-9249-116f3a199c88 | -26.57359 | -51.02198 | 2025-02-11 04:01:00 | NPP-375D | CALMON | SANTA CATARINA | Brasil | 4203154 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4750c820-a9ac-3d4b-a58f-5ca902406e57 | -28.86256 | -50.87484 | 2025-02-11 04:01:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0d5e84d4-1c95-3e9f-8d2e-398a03db4e6c | -25.4764 | -49.8483 | 2025-02-11 04:01:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d29eb7b7-c7dc-30a9-bc74-962af230fb4c | -31.67163 | -52.07954 | 2025-02-11 04:01:00 | NPP-375D | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 1c8d913e-a4d8-3f6b-bfd3-bc4ba2039135 | -32.19526 | -52.25875 | 2025-02-11 04:01:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 51ba4283-7b71-3a03-a332-89d32ea3b15a | -30.19278 | -56.68841 | 2025-02-11 04:01:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 7.3 |
| 61a24d31-bdf5-37a5-8cd1-0ad6c835b3ae | -25.48069 | -49.84947 | 2025-02-11 04:01:00 | NPP-375D | PORTO AMAZONAS | PARANÁ | Brasil | 4120101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11438283-9593-3c85-9f3d-81a6a66ae3ef | -30.4103 | -50.65702 | 2025-02-11 04:01:00 | NPP-375D | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| f0c461a6-0503-368f-acb6-815bad7b96a9 | -28.58627 | -49.44264 | 2025-02-11 04:01:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4122d1fa-9be1-338c-85f7-f7a776f53df2 | -8.70711 | -36.16046 | 2025-02-11 04:18:00 | NOAA-20 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 470d748f-b74c-3a49-8b60-c68d23302d45 | -8.3555 | -45.18419 | 2025-02-11 04:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb51df76-6376-3bf1-93c9-6f4b74ebd71c | -7.24414 | -44.71314 | 2025-02-11 04:18:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a49cc8b-35b5-3be2-a6c6-60bb60d99173 | -8.35881 | -45.18471 | 2025-02-11 04:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
