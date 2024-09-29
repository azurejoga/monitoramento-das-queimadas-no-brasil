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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2599886e-b31b-3351-af20-5f2c9e476575 | -16.86857 | -57.69758 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9fef52d6-a2b5-38ba-b474-8fb71ef39913 | -16.86434 | -57.70105 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7cf0277b-a8dd-3583-bca9-30ae5d194924 | -16.86081 | -57.70039 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 79cc58f7-3254-305a-83cb-44a5b650b83e | -16.86011 | -57.70452 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9e94690f-b6ba-397f-be5d-e6fd0501021e | -16.85729 | -57.69974 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f145f3e7-ff4d-3302-a15e-a739b949d5f6 | -16.85377 | -57.69908 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 34e0fb2f-31fd-31c5-bb8f-2fdc8edae06f | -16.78623 | -57.79873 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4b91f84c-5614-336d-afe2-79d324059cb0 | -16.78553 | -57.80289 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2ddad08b-36d9-394f-b11d-330c92d6a38d | -16.78502 | -57.80175 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| face151e-b793-3b59-a149-3ca0e03fe722 | -16.78482 | -57.80707 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bf0618a3-ecb1-35d5-aafa-20266c7878bd | -16.7843 | -57.80591 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c1e91e44-5271-3a08-8705-79d25a993f00 | -16.78268 | -57.79807 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e4277c67-8f55-381b-8935-568ec92a8465 | -16.78198 | -57.80224 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 94da29dc-f72e-3c97-afa4-b10d0366017d | -16.78148 | -57.80109 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1eb20dd1-d1e5-33a4-93ff-dfab2df2ab69 | -16.78128 | -57.80641 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dbfae13e-707b-33a3-a823-1b589546e3d1 | -16.78076 | -57.80526 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b0143692-eb90-3031-94f3-36a69b0fba36 | -16.78057 | -57.81058 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3643bad8-01e2-3dca-8f48-896b0935b417 | -16.78003 | -57.80942 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7c71bb70-81d1-3042-bec8-507c1e12ed4a | -16.77773 | -57.80575 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e1151d72-3659-33ae-ade2-5c776083a3a3 | -16.96506 | -57.94181 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a7a7e3cb-ae51-3e71-973a-50e53e597ff9 | -16.96221 | -57.93694 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2ebfcaca-408e-3327-93c8-10e89b4e330a | -16.9615 | -57.94115 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 30b7e387-b876-35ac-82be-031e9757bef8 | -16.95865 | -57.93629 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f0577d1d-398d-35a5-b92c-c2229462885b | -16.95794 | -57.94049 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 50385652-eb98-3c05-bef5-3e95522493f5 | -16.95581 | -57.93142 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 269ed1fa-cbb8-377a-b115-1d331129f769 | -16.95509 | -57.93562 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ba4e7ce5-dd6a-3eb9-bc58-a86d286be163 | -16.95438 | -57.93983 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 39870112-ca7c-34b0-9e53-358426700b2a | -16.95226 | -57.93075 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| addd99d8-3527-33b7-a801-bf30b3d658e0 | -16.95154 | -57.93496 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5df8f272-31d8-3a14-91b3-6acfa54af960 | -16.95082 | -57.93916 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b6b0344e-9246-3ee7-92b4-bf96314f4c2b | -16.9501 | -57.94337 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2fdbf256-f6b3-3f15-a76d-9857c1a25877 | -16.94798 | -57.93429 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 503484e0-1b15-3220-893e-abc1ed76b4f1 | -16.94726 | -57.9385 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fccd57a5-d0ba-3d9f-b3ed-d89ff6978484 | -16.94654 | -57.94271 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| f32c62ae-54f6-3aec-a2ea-e070048e31ab | -16.94582 | -57.94692 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e1009737-0ea6-306f-b10a-714455491eb4 | -16.94514 | -57.92942 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7b13cdd8-66af-3d8c-aeac-baac467c714e | -16.9437 | -57.93784 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 0909b752-5d8c-32cd-8c32-33dd6625676b | -16.94298 | -57.94204 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| f1401a45-9091-3617-97a6-de4f5c3bc6e3 | -16.94226 | -57.94626 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| dbc42b59-e566-30a0-a188-0f3b999b3cdb | -16.94086 | -57.93296 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| f91c5793-27b6-3de2-9d6b-4c00ff275248 | -16.94014 | -57.93717 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 2434105b-851c-3c78-9a48-21fead4dd0a0 | -16.93788 | -57.99341 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4f4fa2ff-6168-3d19-9e8b-cf039968c261 | -16.93731 | -57.93229 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b3cfd5fb-0569-3f21-922d-36db9fcf0698 | -16.93658 | -57.9365 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fece2628-160a-38de-aa4f-9ddf8ec30b5c | -16.93504 | -57.9885 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c30154b5-d7f8-319d-b87d-ee69071467b9 | -16.93375 | -57.93163 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 51423977-8aff-319f-8a70-0da7277ab923 | -16.93303 | -57.93584 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 67559408-5add-303a-94d8-07a22db2b844 | -16.93292 | -57.97937 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 01087d55-113c-3cf2-9b72-bb8381105cb8 | -16.9322 | -57.98361 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 96596d5a-b588-3166-9032-6702c175da72 | -16.93147 | -57.98783 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b750fef9-0578-363a-b7a4-e46f8b716864 | -16.93019 | -57.93097 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ee9b8a91-273a-39f1-9627-107c0e031287 | -16.92936 | -57.97871 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a792fdb3-a30a-357c-8044-b4c9d8437b7f | -16.92863 | -57.98294 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 2412cbcd-f791-3ec8-9e54-96f798ea93ad | -16.92663 | -57.9303 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1d00fb45-0b57-32cf-8245-9232c94d8bf8 | -16.92307 | -57.92963 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ffc5895a-6a80-3c0e-a071-7e9253d1e3a1 | -16.92222 | -57.97736 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0bad69d7-85e2-3064-bf62-05b60a50069b | -16.91951 | -57.92897 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| de63e80e-33be-3648-8be4-de40f2e2c209 | -16.91879 | -57.93318 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f8ba5f6d-09ed-356a-92b3-f0365b325363 | -16.91866 | -57.9767 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| addb6531-d9ee-392e-a60a-7cd6f2ed1a12 | -11.72765 | -57.44403 | 2024-09-29 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d8713f4-014c-3fc8-acfd-5ff3b867f0ec | -11.72628 | -57.4413 | 2024-09-29 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8811572-3488-33b5-8795-a6147ccb07f2 | -11.72553 | -57.4458 | 2024-09-29 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44956c2c-30c2-318b-80f0-e733c22ef0a6 | -11.72472 | -57.43892 | 2024-09-29 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a5d1b24-47a7-3b5e-a022-0c2b7d600adb | -11.72394 | -57.44341 | 2024-09-29 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72b2fcc0-4187-3c9b-a4be-31cd1529974c | -11.72332 | -57.43617 | 2024-09-29 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62cf20bf-bb36-37ab-a225-029f9f731d16 | -11.72257 | -57.44067 | 2024-09-29 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5097b79d-d828-331a-a247-a8ee64083b4d | -12.61481 | -57.307 | 2024-09-29 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e54294e-cea7-32e8-9ef1-28d512724809 | -14.94047 | -57.95071 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 941da48e-4f81-3c34-86eb-64b1ba2f1608 | -14.89936 | -57.97041 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6c69f4f-769d-3889-b748-52157320c083 | -14.89367 | -57.98481 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd399f63-a475-3e49-9692-7dc8f2a72bc3 | -14.89294 | -57.98911 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b29c0149-8577-359d-9b69-5c5b488aacbe | -14.89222 | -57.99333 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da2a1783-c796-3aa1-96f3-dd50523bc2e8 | -14.8915 | -57.99756 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37945cd7-31ad-307c-9735-dda25bd0d4bd | -14.89078 | -58.0018 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c07db118-4659-3b43-8b91-27f52b0ed8c7 | -14.88927 | -57.98853 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86f5fac6-1ba4-327b-b1c9-ac5de5162cd5 | -15.36796 | -58.17163 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88c2421b-1075-3d60-baae-aa6694424ec8 | -15.32035 | -58.14075 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eebb6bbf-6661-3837-9461-def2dd5667a0 | -15.31959 | -58.14507 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b735e5c-965d-36d9-84e2-4965c9bfe8a9 | -15.31514 | -58.14883 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 524647ea-2f20-3785-83ce-8b00a344a32d | -15.30828 | -58.15042 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a373f08-b7ff-3c90-8cf8-04df3d2a2ab4 | -15.30461 | -58.14977 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f07446d7-2661-3442-95e1-2d09aa53eb5e | -15.30386 | -58.15416 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22601580-6a29-3654-ab3b-af91b867b6b1 | -15.30335 | -58.15128 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cbcfb4e-bce7-38f1-aaf3-3037b1756811 | -15.30312 | -58.15852 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c641d3fd-b021-3b49-b1c6-a670a5240ce9 | -15.30258 | -58.15566 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c92995bb-e2dd-3946-97b0-b0907a48c216 | -15.30181 | -58.16001 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e252c861-4a53-3f6d-a362-1c8373258a06 | -15.29944 | -58.15789 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aff3631e-3855-3728-8641-e9a046775ed5 | -15.29576 | -58.15725 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e65b7e6c-08d7-3805-9aba-3fe0a15b992b | -15.29501 | -58.16168 | 2024-09-29 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3067939f-6680-3450-ad01-db9f16c045e4 | -10.69534 | -58.53088 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1bde5104-3220-3d29-947b-7f1e91a01426 | -10.69472 | -58.53446 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d65129b1-2751-3a6d-bc4a-7108458756be | -10.69133 | -58.53015 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af6756d7-5626-3db2-8a70-b69fbc72ead5 | -10.69071 | -58.53374 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e137ed93-07cf-3c15-8ca6-89fbd2dbf6a6 | -10.69008 | -58.5373 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 665345d5-a8b1-3bed-a7d9-ccc7cf3ffe7f | -10.68796 | -58.52579 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26b60280-9d79-3b0f-9d25-06b0f9510981 | -10.68733 | -58.5294 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67cd699d-f089-362b-881a-23fcdef32ae8 | -10.6867 | -58.53299 | 2024-09-29 04:51:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab56fc83-c0ba-3ca0-b00e-718a75442f01 | -14.52082 | -59.77105 | 2024-09-29 04:51:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1aebe393-c790-322d-adde-31dcdf70d694 | -11.57503 | -63.88193 | 2024-09-29 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8ccd5a3-64f3-375a-b0d4-d20e31eb26e4 | -14.45112 | -60.10704 | 2024-09-29 04:51:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README61.md)
