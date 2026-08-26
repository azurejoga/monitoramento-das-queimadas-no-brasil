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
| 8929f101-4425-3346-832c-b2055d1121cc | -13.24464 | -51.37173 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 1ef9b520-9799-3d03-930b-10e1689b3b7d | -10.74954 | -54.00553 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74f00dc8-eb75-3426-bd71-066c4275dd7e | -12.04025 | -46.04374 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 472e5dec-f95d-30ef-b2e8-03fd30e413eb | -11.76 | -54.53444 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6649365f-78a2-3850-b564-78db07128ec6 | -13.85802 | -54.07554 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cde26da5-c78e-3d4a-94d7-b6bfb4618852 | -13.30578 | -51.4687 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06a3b1b1-0ab4-3c5d-a934-f34534e4c511 | -9.56563 | -49.26239 | 2026-08-26 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80d5de96-edee-3368-89bc-025e5ffa4ae3 | -12.65339 | -48.42624 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a206457b-dd0b-3d94-838c-30f9fb26089a | -8.80932 | -62.31421 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f192c6c-b469-3c5f-a19d-f023b55c4efd | -13.86026 | -54.07843 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ddab235-5926-304a-af6e-1ce9dc279861 | -13.25201 | -51.37548 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2fec863b-1229-355b-ac5a-cf407266a14c | -13.24129 | -51.37407 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15ed173a-4209-301d-ac27-e914637362f2 | -13.23564 | -51.35669 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35f003cb-3615-3acb-9cfb-c0a34a416536 | -12.03461 | -46.02763 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a92c2007-1b95-3703-b97b-399eedc49bf3 | -12.0256 | -46.04207 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 9cea1e40-8c92-3948-a69d-cbc745300c8e | -9.56515 | -49.27327 | 2026-08-26 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3935ee2-43f3-3f13-a6ba-f333ad531421 | -12.675 | -48.42009 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1686e65b-b12e-3743-b7aa-0a9270e7744d | -13.23972 | -51.36763 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 6a645157-7b14-3dd5-bf5e-637e2543073c | -10.99012 | -60.78967 | 2026-08-26 05:29:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb80764b-2462-3ebf-8c0e-f6fd0a50a826 | -8.26145 | -63.99523 | 2026-08-26 05:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29a8d8e-25b6-39d2-b7a7-d1e98dde5138 | -13.23674 | -51.36653 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| fcadac39-91c8-30cc-a180-33c312a2b2e5 | -13.26971 | -51.45378 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62e5af0c-7b96-3d80-8631-c4f418dc0368 | -10.75263 | -54.00676 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddcbb2f3-f786-31f3-bf03-78e37858f0f2 | -9.59392 | -60.52203 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac4f1ea4-41a0-3607-885c-eb63913f29ca | -12.68999 | -48.40291 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08d2b92a-01f6-3d02-ba0f-2dcd62a1d4d9 | -9.48878 | -56.91847 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f02b93b-797a-3ec1-88fb-d7398e5b64ba | -13.25119 | -51.3823 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e4bea746-d0fe-3eb9-a038-c9f30e30cb7d | -9.13589 | -57.56276 | 2026-08-26 05:29:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81b2e250-e3d1-3893-af2d-69b433ee442a | -9.46653 | -56.90837 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d10a8f6-8ad0-32c7-9f39-866a94681703 | -12.02752 | -46.03157 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 1d2e9bca-e2bc-34a3-b638-2df1a7c87302 | -13.23178 | -51.38741 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5b69398-06e8-3ea1-a5a7-1ad52a68e1ec | -11.16884 | -54.00476 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6f415e0-395b-3a27-bca1-e09b6a00b0a0 | -13.24088 | -51.37749 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62593120-812a-300e-be1b-637321d2b730 | -13.24058 | -51.36079 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| bddb4bf3-8bc8-3f47-8edb-cb53d49cbf12 | -13.65198 | -51.846 | 2026-08-26 05:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a85130e2-097d-3d66-8afd-ddb886ac034d | -10.43435 | -61.22672 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 167b0f84-6973-32df-b625-d849f5a5d86f | -13.26108 | -51.39054 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 5cfdc5ba-09a6-33cc-86f2-05f1cb2557a0 | -13.33563 | -48.20529 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d26904e2-d243-3ecf-94ba-433002c77341 | -13.24706 | -51.37135 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2ac34133-3ead-3c01-8217-f1c827ba23b6 | -11.7636 | -54.53342 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21e351c7-93a3-36e6-a0de-0511b85b370c | -13.29721 | -51.45042 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 05df2348-ee08-3fec-86ee-6140fe5c82bf | -13.23458 | -51.52083 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63015d1e-baf6-3d85-abc3-2cb9eb188b66 | -13.23756 | -51.38469 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| e6e89541-cc3e-3b39-b2dc-2ef837b3f8d2 | -11.79748 | -47.64355 | 2026-08-26 05:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b2b32ad-de06-3eed-af56-55484b3fb9ae | -10.76081 | -54.01992 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 688523ac-afcd-3fdc-9ccf-40591ca318e0 | -9.59613 | -61.00842 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58c6f60a-024e-33b3-b6f7-0ba17a2b9451 | -7.65062 | -62.54927 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c0b6a45-7b61-3b9d-94b0-cee1134ef363 | -13.24543 | -51.38502 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6da11c73-bf8e-3c3e-81c2-50ea1bcfcad5 | -13.24421 | -51.37515 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 78d385ff-1e9e-36f7-9d12-92fc7b56e4b8 | -12.0841 | -64.24454 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3f0b41b-fac0-3c36-9997-420470f8207c | -11.19178 | -54.00277 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60dfa6dd-6bd2-3aac-b108-00bdf8b1cd5c | -7.78045 | -61.56939 | 2026-08-26 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 188f32dd-93fe-3f4f-858d-b215f8b346d9 | -13.2516 | -51.37889 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 87fb2e38-1ff7-3550-9187-d48787c493b0 | -10.42099 | -57.23241 | 2026-08-26 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bf0d1f2-c886-3b14-acd0-4ea37a7fa427 | -9.09438 | -59.40762 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc53fd81-507b-3312-ac3f-6a827ca00f85 | -9.29292 | -60.91521 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77925e8c-bf7e-3e5a-af6c-b2500ec3aa5c | -8.93359 | -60.71368 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3171d427-e8b9-3b72-ad42-0ad0cf70e90f | -9.46279 | -60.53714 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c970b1e7-d15e-36f2-91c2-28c346fb696e | -9.17056 | -58.33434 | 2026-08-26 05:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa9cb0ab-cf04-35d9-ad29-3c668945a5de | -13.28447 | -51.46592 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ebe4ceb8-2b2f-305c-9911-2cfac6ed4553 | -13.26067 | -51.39394 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ad7028b9-6327-3e72-9b9a-edd253929ddc | -13.24507 | -51.36832 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 216a4021-16d2-3b32-b12a-aeb907c1821e | -13.23221 | -51.38401 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85ccb1d1-2b0f-30a4-826b-5a7e118b7e2f | -9.48164 | -56.91747 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a18f0596-368a-36c8-b9cd-ff8138fae84b | -13.22856 | -51.36968 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 27887941-e4b9-3ac4-8af4-86fc2e24dbd9 | -12.02672 | -46.03926 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| a0a94143-fc89-372a-9401-e5736edad8b5 | -10.42406 | -61.21775 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c00268fe-c2e2-39e0-b947-2d8ecd17e8cc | -9.09383 | -59.41112 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02093f1c-aa3c-35b8-b3aa-765cf8daeb1f | -13.28488 | -51.46255 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1787f444-0bbc-3752-bc4b-a1e0e7a17f6f | -9.56989 | -49.28254 | 2026-08-26 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce3e348f-d94d-3f0f-9020-449ac6afc8c3 | -7.60288 | -67.42329 | 2026-08-26 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36f3d6f4-7521-3057-9568-29aee1c11210 | -9.67552 | -55.08448 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd9912cc-9165-3f90-869c-a9c8a3485198 | -14.36517 | -51.75345 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c21f9f5e-57d0-3bf9-8373-0ff4547280d5 | -9.66687 | -55.08831 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 35ba96f2-cf7c-3159-95d9-7273a3125a82 | -10.76482 | -53.98316 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c4c0033-c9d5-3221-a32c-2b55408a1947 | -13.87423 | -54.09196 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c91e2449-5a86-3681-aca7-98a71d6f0784 | -9.46548 | -56.89128 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c7cd731-3e07-37f3-9a37-b9da389be2cf | -11.15579 | -54.00291 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7af9cc4-0b19-3147-9995-c0e01cc7c97f | -9.11078 | -60.39323 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1e681ce-79e3-3c1e-a726-6ad20c642eeb | -12.68369 | -48.40091 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 786d0e21-dd02-3e65-9946-bd95719f75db | -10.1695 | -55.30522 | 2026-08-26 05:29:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34875607-bfbe-3aab-bc0f-b761ad65d410 | -10.76776 | -54.03357 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 5e409e69-924a-3a52-a52c-a937d05efa1e | -11.75098 | -54.53716 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3907f4b4-d16e-3889-914b-136be522ead0 | -10.75163 | -54.02275 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9897599-e7a6-305a-bc75-6eb90069981d | -13.24624 | -51.37819 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4dab0091-15a1-333b-9c9c-f9187b7945d6 | -9.38909 | -60.57608 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a45ad49a-7418-3f24-a45e-32d6ab77496b | -11.82224 | -47.66336 | 2026-08-26 05:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0df04d70-4de6-3cba-a661-94906fb665d2 | -13.33454 | -48.21522 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ef1b611-de50-38f0-825a-e47475977c5b | -13.85928 | -54.02956 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7079b765-d8a9-3b39-84ba-0c754fbe5aad | -9.71863 | -49.35665 | 2026-08-26 05:29:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77b1b6b4-a6e2-3f38-9493-388be191e923 | -9.29014 | -60.91105 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0251e970-2357-3977-859e-18eafde89fd8 | -8.8202 | -62.33661 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5976eca8-88bb-31b2-97a1-2ff4c94f6b13 | -13.61142 | -49.01446 | 2026-08-26 05:29:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3c74324-2c0e-333c-98a2-4e888eb047a8 | -9.39407 | -60.58779 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b7dccc0-c58e-3fdd-9586-537e030cbabe | -13.23885 | -51.37446 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b1559b5-8c2b-3c7b-a57d-f321278efd3a | -13.23522 | -51.3601 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 81290cfa-e321-3687-8db8-b0c08c11e108 | -13.98598 | -54.01562 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af4e08d1-eaa4-30de-9fb2-b6329e6b7fd0 | -13.23842 | -51.37788 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b5727aef-646b-3560-bb3e-e230fe5aa403 | -9.40018 | -60.59243 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afbbd58f-f306-33ac-ba6c-1f6b42ed8f29 | -13.25614 | -51.38642 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |


[Clique aqui para ver as próximas entradas](README64.md)
