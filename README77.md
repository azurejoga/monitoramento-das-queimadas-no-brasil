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
| a4641162-008e-36c8-b199-7760df4cfbda | -17.33232 | -46.68453 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94317a50-9896-3956-b012-dc17f9b33df9 | -15.79961 | -52.25035 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a68b33d6-521e-34ef-be6f-77fee699c8b9 | -15.12647 | -50.13523 | 2025-09-11 04:25:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5085fdbe-5a7e-3762-9587-e974f286a285 | -16.88816 | -45.76113 | 2025-09-11 04:25:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 582f9f25-6cd9-3be0-95cb-07ba80e44bce | -15.12384 | -52.41713 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 153065b2-dec7-322b-a6dc-6fa1f0af4ea9 | -19.95152 | -49.27229 | 2025-09-11 04:25:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 48c13672-dc3e-3997-ac9f-a1391991d736 | -18.34622 | -44.36228 | 2025-09-11 04:25:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77c5c511-2e49-34ab-b54d-f88cea0bb22e | -15.07958 | -50.06442 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f41916d7-106f-340a-ad0d-792cb9b2cb2d | -20.23494 | -43.58055 | 2025-09-11 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| beb1c2ea-cff9-38d6-872b-d9422d152348 | -15.62801 | -47.54096 | 2025-09-11 04:25:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fea32c27-2466-32e9-8723-de321bbabdc4 | -20.53794 | -47.62554 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2baa35c6-3323-3f69-b072-8f1d8029262f | -17.9381 | -44.48365 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d00d4890-faeb-3bfa-9d10-7450bc42bbe7 | -19.18828 | -48.793 | 2025-09-11 04:25:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a73754e-8235-302e-8cac-4c3b50321191 | -20.11393 | -44.34737 | 2025-09-11 04:25:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 72d54493-418a-36e8-86e1-ee56343ab34f | -15.6056 | -47.10389 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59d1ab8a-67e7-3783-bcca-f25f97a260e1 | -19.23851 | -48.00264 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 06315196-ebb2-3bb4-add0-fdc64aae7fcc | -15.11304 | -50.08258 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 241fb52f-003c-307c-b5d5-1489864f255e | -17.94372 | -44.48289 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4cbba603-b4d5-31bf-a8b7-a47a5a64d47d | -16.65687 | -47.72682 | 2025-09-11 04:25:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbb37b3e-1f7d-3452-94da-ddfc5c6b28be | -17.55109 | -44.54561 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72c92011-2f9b-307f-8d8c-4a490086f087 | -15.14655 | -48.60373 | 2025-09-11 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13627b43-8276-3725-96c4-14d22497cd6e | -17.50098 | -43.75175 | 2025-09-11 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7ddeed5-1365-388d-a1cc-940c240e5f22 | -17.5558 | -44.53802 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4f1d5cf-6da8-33c0-b2ce-5c82a71e3374 | -18.76482 | -48.19235 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9020c39-f54a-349f-aa3c-b672f68a6207 | -16.60681 | -49.77293 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6607cef-0507-396a-ad04-f1b4d1c98a49 | -15.80136 | -52.23062 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e26c4d40-61f9-37e6-9c65-6c510739d952 | -19.20363 | -47.98515 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2337b1e8-46a0-38c1-a6d3-4a167ea68dfb | -16.2976 | -50.05021 | 2025-09-11 04:25:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ec5c9133-247c-3928-9005-4345446369c4 | -17.72627 | -44.4325 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51a86c43-b4d6-3b0a-aa9d-c054efbcce00 | -16.56281 | -49.73663 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9e7ff6e-4b33-311c-9172-a74a8efb41ce | -18.35172 | -49.3268 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd9e40bb-e6d5-326a-b690-9ac7cb911e65 | -17.55228 | -44.53735 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72bf68bc-9be3-3c4c-b5bc-f19ad6a8721c | -17.34007 | -46.70074 | 2025-09-11 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5413737-72ed-3304-973a-8e3343ea026f | -19.32847 | -47.28064 | 2025-09-11 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6561000-f22d-3744-a419-edbf5c9a07b7 | -16.42563 | -45.68458 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fb65fa5-3873-3fd1-a8f0-664b42debf2b | -15.15492 | -52.41303 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0f27a102-d4c8-3d47-8ae0-904e8915ca85 | -22.32028 | -48.82466 | 2025-09-11 04:25:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c857a4f-8135-3b70-b344-7f755a4f1055 | -17.24292 | -46.0844 | 2025-09-11 04:25:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1a4e291-ba65-384c-9e88-d0a6f5e3bca8 | -20.22603 | -41.01283 | 2025-09-11 04:25:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1d492ca-b104-342a-89b9-4eca8d0beeb6 | -19.9893 | -47.63424 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2fe6a28-80f5-34df-a04a-9455956fbfdb | -16.7102 | -43.93194 | 2025-09-11 04:25:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cca4ddee-2708-38e9-b30d-2730f0da8cca | -14.31179 | -54.75613 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 237263b7-45f5-327e-abe3-2f4b4a82a2df | -14.50644 | -53.9403 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c21224e0-7e52-3d00-b18d-6acf957e56c2 | -15.55439 | -54.7724 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff2842f4-0509-393e-a010-87d4889477dc | -21.91376 | -47.90826 | 2025-09-11 04:25:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8689e27-a87c-3496-844a-caddd31b530a | -15.10008 | -50.07055 | 2025-09-11 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d161c7b8-5967-3eb8-9ff3-59477638305d | -20.48336 | -49.72879 | 2025-09-11 04:25:00 | NPP-375D | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27ee3df3-abe1-36fd-bd9e-16efa95ed411 | -16.6132 | -49.77822 | 2025-09-11 04:25:00 | NPP-375D | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02931a33-12bc-30a1-b8c1-04d2fa99e49d | -14.88728 | -55.87899 | 2025-09-11 04:25:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15c261b7-396e-38de-9188-9356048d3771 | -17.57693 | -47.49605 | 2025-09-11 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1aa6ad5a-6c6c-3449-8077-5a8e898132d7 | -19.23793 | -48.00629 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cae7fa49-b5a9-3dab-b348-22d21b5a8985 | -16.54303 | -55.17724 | 2025-09-11 04:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| adce6a0d-1a90-3bde-87dd-7eb7b3b7af15 | -20.40121 | -46.27907 | 2025-09-11 04:25:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f79d1ef-48e0-3c2a-9d61-a255db45e2b5 | -15.56114 | -54.77596 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f71eb6ac-0cc9-3a0c-a0d7-6eb358491ac8 | -17.82593 | -46.74349 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5da397ef-2408-3df3-be20-ad688bcccac6 | -19.3279 | -47.28432 | 2025-09-11 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c9df44d-5f10-355e-904a-d6c7c5772725 | -19.23185 | -48.00146 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 97efe948-ca71-349a-81f8-9274d5399fbc | -19.98379 | -47.62571 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d8002aa3-372c-3c87-b4f3-54e8f078105c | -20.00217 | -47.61759 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c928d8e6-e4cc-3353-b3c2-f58e659b8b66 | -19.3506 | -56.71178 | 2025-09-11 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d714594d-ac80-3e2e-9a8e-a98b14b81087 | -18.60501 | -43.97309 | 2025-09-11 04:25:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa0354c4-1432-3af2-85cf-2f4686adc163 | -19.37887 | -41.81707 | 2025-09-11 04:25:00 | NPP-375D | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c69f2ecc-368c-3ab4-a6e4-12f7b271d282 | -15.81514 | -48.96022 | 2025-09-11 04:25:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| beb50d18-33a9-3e98-bb51-088f6534acac | -17.84317 | -44.2151 | 2025-09-11 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f91ea394-7567-390d-9ae6-1818c2909fee | -15.79613 | -52.24615 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2659ac36-6e8e-3288-8a9a-4e4d531fd724 | -16.26274 | -46.7823 | 2025-09-11 04:25:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c474812-2fb7-3d28-9414-651bc0deb33c | -16.56862 | -49.74055 | 2025-09-11 04:25:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b93c9bb6-2728-3bf7-8e59-609d59ba5efb | -15.6681 | -47.0334 | 2025-09-11 04:25:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18c62833-aa01-3d63-b767-8b179af1cf81 | -15.59813 | -49.39412 | 2025-09-11 04:25:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed50cd1c-9839-323a-bcfd-9da90c59fdbb | -18.05798 | -50.72081 | 2025-09-11 04:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eba39e1c-383e-3670-9d99-1a3f51ccde69 | -17.30696 | -49.31546 | 2025-09-11 04:25:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d8a09d0-bb9e-399a-8b57-c8c1edf57581 | -19.34994 | -56.71494 | 2025-09-11 04:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ff044a7d-4527-3bef-9a19-c2807e3618dc | -19.23518 | -48.00205 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 8c653b29-83c5-3387-bd73-f24cd58bd6e4 | -17.57751 | -47.49243 | 2025-09-11 04:25:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5a4db14-a811-3d06-8a38-4e24988ec080 | -18.91578 | -41.11839 | 2025-09-11 04:25:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8cd37afe-8e6d-3427-bb9b-01a96676bbbc | -14.51863 | -53.92678 | 2025-09-11 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e85b96b-251a-389d-87dc-209f9e256e1a | -16.42845 | -45.68883 | 2025-09-11 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a6f8a3c-160b-3c4a-bf45-98edae23aec0 | -19.00936 | -46.24955 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e77b93a1-f49b-3e9d-bd0a-4572a176b965 | -20.57102 | -47.67696 | 2025-09-11 04:25:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5eb89e4b-908f-32f1-9ab3-f235ab13fb03 | -20.08572 | -44.47793 | 2025-09-11 04:25:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 36573437-2790-38bd-b29a-75e259db268f | -17.15547 | -44.45068 | 2025-09-11 04:25:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93ea8bba-fc55-3267-b8ec-6d12ca68635d | -18.45165 | -49.57831 | 2025-09-11 04:25:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0b59bd3-2403-34c0-9619-1650176eae5d | -18.76423 | -48.19603 | 2025-09-11 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16d93e7c-fef1-3abc-b57e-089eabf34311 | -22.29472 | -43.02903 | 2025-09-11 04:25:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6692e2fe-5405-3e1d-bf01-455148407a1a | -20.23944 | -43.576 | 2025-09-11 04:25:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 28357098-dba0-34ef-91ff-4cc431261190 | -19.98264 | -47.63308 | 2025-09-11 04:25:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d08d0209-086b-3268-acd9-1f39773cc1ef | -15.12105 | -52.40958 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6414b869-6bf7-3a24-9e93-9328132fa6bb | -20.16883 | -44.62401 | 2025-09-11 04:25:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49d9e73e-fbbb-3ebf-87df-5b551f5a54a5 | -17.90835 | -44.58847 | 2025-09-11 04:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec8b557d-bd65-32ee-a133-8ac8363532aa | -17.99898 | -47.10907 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e08b5d34-5215-3d04-a6a6-9d83e0fcbf9b | -17.06806 | -49.67624 | 2025-09-11 04:25:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5034daf-821c-36cd-999b-43a4ca2906c3 | -16.62258 | -51.82058 | 2025-09-11 04:25:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff3adce6-9fb0-3990-87b1-f2c47430b6bc | -17.5564 | -44.53387 | 2025-09-11 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcae35e3-5cb2-3717-a1f8-65daf51dda08 | -17.84596 | -46.74687 | 2025-09-11 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0927f49-593a-361d-8f63-b07114614a81 | -21.29718 | -45.95321 | 2025-09-11 04:25:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 68432ce1-729a-3f2d-9b2d-3aa67da5e04b | -18.05643 | -50.72955 | 2025-09-11 04:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9999f0be-7977-3fde-9ba0-4d7d57b11fe1 | -15.80094 | -52.27826 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa1bae62-1853-3ca5-9ef5-19a55cab617f | -18.35515 | -49.3274 | 2025-09-11 04:25:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 019be472-0f29-3078-bda7-ca9a00eb9c5e | -15.79944 | -52.27495 | 2025-09-11 04:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c23e77a2-434a-3018-a2ab-a1f986c6793a | -15.86999 | -54.93519 | 2025-09-11 04:25:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |


[Clique aqui para ver as próximas entradas](README78.md)
