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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 680f0f51-363f-32c9-a863-265fe3a825bc | -9.25776 | -43.52023 | 2024-10-09 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 04d8f2ed-1996-3bfd-a803-414079af6e67 | -9.25714 | -43.52453 | 2024-10-09 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fae438b3-9877-3afb-ac17-363b6499ea4f | -9.2489 | -43.51889 | 2024-10-09 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 23ad6b84-cdad-382c-88a7-fb52bbcfc38d | -9.24766 | -43.52753 | 2024-10-09 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c83ded60-4509-37ca-adf1-b8f5f3a288f0 | -8.49565 | -43.9124 | 2024-10-09 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b82f13f7-546e-3799-8ec9-f7a4dbce1aa6 | -8.49509 | -43.91634 | 2024-10-09 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8fc422b5-bcb3-37eb-a6e8-a29ae2fe627f | -9.52848 | -42.99181 | 2024-10-09 04:38:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc6beb87-fa01-3d95-a842-5c9b4824d7bb | -4.24629 | -41.92844 | 2024-10-09 04:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45345a60-428e-33fa-a357-942cf87b6ab6 | -4.24561 | -41.9331 | 2024-10-09 04:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b5de7bf-1131-3d11-9f58-c8cbf052dec9 | -5.97161 | -43.35613 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7840bd92-ae77-3982-8d39-8392235c4132 | -5.97104 | -43.36009 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5985d632-ec56-39a8-b22a-a0de2e973386 | -5.97046 | -43.36413 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91809d1b-a359-310a-bc6b-79e2d01dc9dd | -5.96619 | -43.36348 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5064edd2-d29d-3a15-9ec5-31db10fe2337 | -5.96598 | -43.19913 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2f3b4d4c-5388-37b5-a36b-9df69d38ce59 | -5.96537 | -43.20324 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6040c19b-f68e-3cd5-a6e7-8615b6501996 | -5.96165 | -43.19856 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e7db6dc6-8e28-35d4-9bbb-b45b65fbd45f | -5.96043 | -43.20678 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e5a2175-7c9a-3976-80cc-c1cbe1ea374e | -5.73159 | -43.12148 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7a5c3e04-b142-3fd4-9859-9871317383fc | -5.73097 | -43.12562 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eaf9ab7f-9ccd-3f0a-9168-4178bb6c658f | -5.54917 | -42.93192 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e79860c1-84b9-3698-ae46-6b2826e66f90 | -5.49942 | -42.78828 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 246d61a7-f646-3dc0-b8be-fb97422e355a | -5.49878 | -42.7925 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cadf54ed-a050-3aae-80c5-7ea8fab64bc6 | -5.49797 | -42.79027 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 08a87884-e2cf-3de3-ba75-baafc17a4530 | -5.49629 | -42.77909 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e79cf003-f959-353d-becc-6565a00f482f | -5.49565 | -42.78334 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0c5c61c-6371-32f6-9009-38b76e0bffa9 | -5.49477 | -42.78107 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82ebdd23-6420-3534-93c7-1732243d7d32 | -5.49417 | -42.78532 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 48a1bf1a-cf40-3f0d-9e45-c882f153c48f | -5.49124 | -42.78266 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e75f1f2a-3224-3a07-b494-734ebc21fe6c | -5.48976 | -42.78461 | 2024-10-09 04:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f7ad9c45-8a4b-39c4-af84-9ef8a11c3181 | -9.93613 | -44.07207 | 2024-10-09 04:38:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 378f9897-9699-3104-8e22-26f58ad7d4b9 | -9.83272 | -45.48649 | 2024-10-09 04:38:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bcfeef4-8b69-3406-8a5a-fc776b2a216b | -9.67605 | -44.49876 | 2024-10-09 04:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a17b9a2-6abf-3058-a4d5-7e24b7495e66 | -9.67186 | -44.49819 | 2024-10-09 04:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e67a3f5-d95f-30da-b81c-a6e17b44758a | -9.5328 | -44.44493 | 2024-10-09 04:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9924cfca-841e-3e1a-ac12-bee92e307c95 | -9.52806 | -44.44818 | 2024-10-09 04:38:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56e43021-355a-399c-88c0-3999a79bca74 | -9.43108 | -44.12847 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a252cd0c-bd26-3fb7-b0ec-a9807ac7e3f1 | -9.42802 | -44.11921 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f9fc74a-8e77-3fd6-abbf-0fa33798a3a9 | -9.42376 | -44.11846 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ad93d25-d82b-37bf-896b-598ba5f8f11a | -9.41352 | -44.12944 | 2024-10-09 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cc0be7d-afc2-3029-8dfd-159285bc2a62 | -9.32909 | -45.73956 | 2024-10-09 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b499c80-db64-3d39-95a9-8422f9c910dc | -7.47151 | -43.98239 | 2024-10-09 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a44a09f9-c5e3-3375-8332-d09dee9e6227 | -7.47131 | -43.98263 | 2024-10-09 04:38:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a405e2d-0bfe-37a8-ba12-a28716a914ef | -7.63682 | -44.81952 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e4ea1ff-7982-3b51-a066-2f99b535d712 | -6.90058 | -43.82724 | 2024-10-09 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e75c109d-4db8-3b2d-9ca2-42a93312d137 | -6.89638 | -43.82664 | 2024-10-09 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40d262c0-1ec2-3c78-99b9-8edd5931b91d | -6.78276 | -43.81122 | 2024-10-09 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 482138a2-73c1-3e92-a86c-7d3a8b8e21f9 | -5.3841 | -43.64118 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f59930cd-7631-3b34-8e44-ed0c5ab0feb4 | -5.37994 | -43.6406 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73ef535c-68b4-31c4-8f0b-16cc5069f4ba | -5.31915 | -43.72768 | 2024-10-09 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b705bef0-f2fb-35e7-a5c4-ad40626e4ffb | -5.29039 | -43.39979 | 2024-10-09 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec7582f1-0d48-3059-875f-27637b5bafde | -5.28617 | -43.39914 | 2024-10-09 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef41d130-f667-305e-b3c1-bac91755d258 | -5.23514 | -43.81251 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cbccfed-a65c-37aa-be17-53e98a542087 | -5.23461 | -43.81613 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2dd95a8-9017-3a8f-ac70-1471054aecfd | -5.232 | -43.81273 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fee9862c-2556-355f-add1-40f9c94ec397 | -5.23145 | -43.81635 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f320a6f-34de-36e2-9499-4315701a0be0 | -5.22736 | -43.81569 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bd22d26-f771-3e7d-8bcd-3d28597f4ab7 | -5.22327 | -43.81503 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e037563-2805-3897-bd04-598dcb44cd37 | -5.21918 | -43.81436 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23b02570-baa1-3c92-a02f-2a3f1cf0333b | -4.94508 | -43.67276 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1bdf585-56aa-38d2-9f7d-7164af0614cc | -8.12645 | -44.41551 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10ed987c-2d96-3f99-a76e-244c50345640 | -8.12592 | -44.41916 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f1c0e6a-7360-3cff-839f-cdd8c0d22590 | -8.12539 | -44.4228 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 716e4626-9218-352a-9349-68b3380f4812 | -8.12129 | -44.42217 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d998aa56-5224-3277-b6f6-a9c0173e3851 | -8.12077 | -44.42575 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d16ac0e1-c2c2-39fd-b72b-e7a3c78f1bf2 | -8.10198 | -43.99393 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4b2dc92-9d3a-386a-ac2a-383fb14965f0 | -8.1014 | -43.99786 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4c53754-bca1-319c-9a4e-2c9cf821695b | -8.00499 | -44.36892 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df6836f5-8a20-3db0-8aec-cbef622cf956 | -8.00446 | -44.37259 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b21ddcf2-bdf0-3e8b-b745-2db9e4f9d301 | -8.00394 | -44.37626 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b6d0d75-5338-345c-a888-6e9cfb0529b1 | -8.00341 | -44.37993 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0f14928-5033-3f87-8097-60a31b571053 | -8.00288 | -44.3836 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9572cfc4-e42d-3722-aedd-4ece2df3a5c2 | -8.00247 | -44.35724 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d7e47f3-e2a1-35c2-8880-a870a0ef5f1a | -8.00194 | -44.36093 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b88b22e-2900-3ed1-8564-0eb255b258b8 | -8.00141 | -44.36461 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42f2c8ba-def9-33c6-b8f4-2f616c579327 | -8.00088 | -44.36829 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b49e5a2-7037-38a5-8e73-269ec03a42e8 | -7.6336 | -44.81381 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ae2d9bc-4a6a-3041-9bbe-c81d50853e61 | -7.63283 | -44.81904 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88fa8e54-bc16-319f-80a6-7c3618db93e4 | -7.62884 | -44.81851 | 2024-10-09 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 756a118b-a514-3ec4-a600-fe47645d0237 | -11.14027 | -45.37615 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2699e91-2095-3681-92dc-1243a51cc562 | -11.13989 | -45.3767 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c53feb68-b87c-3d51-b09a-3266846bcc9a | -11.13978 | -45.3797 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 764d4087-defe-32be-a2d0-b18b040e6ea8 | -11.13938 | -45.38025 | 2024-10-09 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16213458-ce77-3982-906f-0c3927f0b26d | -11.12906 | -44.95034 | 2024-10-09 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e908b5dd-365d-3dc7-877e-8d8c53b9e2b8 | -11.12853 | -44.95418 | 2024-10-09 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f04a7ce-8872-3642-a45b-bae2d3e9928b | -11.12492 | -44.94972 | 2024-10-09 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac4af890-c19d-34bb-8a0b-8bfda163f157 | -11.1244 | -44.95356 | 2024-10-09 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65d7199d-f0ad-34c5-a460-9462de7faf2c | -10.8044 | -45.14628 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 731e3e5a-efb0-3443-88bb-1c9d338fd6ce | -10.80388 | -45.14994 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40347db1-0ee3-38fc-b698-7955296f6aae | -10.80033 | -45.14566 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc7cf3f4-3dfe-33d1-a573-4a94e3736de3 | -10.79982 | -45.1493 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96932b99-9738-3598-b285-68221ea5c573 | -10.71888 | -45.02216 | 2024-10-09 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12c4f371-35dd-3e14-a444-14b1fb131a28 | -10.45716 | -45.11809 | 2024-10-09 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a4f0e84-beb3-3d3e-8bca-a92c239b6b5e | -10.45666 | -45.1217 | 2024-10-09 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d6a0ac1-ba9d-3cb5-9d8e-f159e515b41c | -10.44752 | -45.12791 | 2024-10-09 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a597b213-caae-30cb-b676-9e29c82727db | -10.44296 | -45.13099 | 2024-10-09 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3672821-fd2d-3d4e-a748-1a80779bd432 | -4.47953 | -43.77552 | 2024-10-09 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18869406-1db4-3895-bb3a-20f441e640ee | -4.17547 | -42.99329 | 2024-10-09 04:38:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac4a752c-0a70-334d-a209-a89f10ef8e75 | -4.17342 | -42.99023 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f063121-be4c-3715-80ec-51e7c68993b1 | -4.17281 | -42.99423 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1ae754c-2a68-398a-a5f0-249d82b6ac6a | -4.17179 | -42.98862 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README115.md)
