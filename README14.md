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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 448c893e-e4a9-3ee7-a22e-ea5c63525272 | -20.26747 | -41.64819 | 2026-08-09 04:27:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3f2dbd9c-d434-3830-af84-2b41e69a3ba9 | -12.32802 | -53.15145 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae1b9b35-dc2f-3634-bd83-466c4262aedd | -12.34892 | -53.1652 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4c68b3b-6d26-31af-9095-662bdd23ceaa | -13.84193 | -53.75452 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9decace6-bd43-365f-90fc-b3d690022d8d | -18.64012 | -49.85712 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c7a7bbb1-b1f7-3528-9b43-2e1cee400097 | -16.08758 | -47.8557 | 2026-08-09 04:27:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1acbcb41-45f7-3aae-9d17-b358e1ac5278 | -14.07432 | -53.99849 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d36b16c4-8549-36b0-944f-6a780c87cd40 | -18.64832 | -49.85054 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e225475-d6c8-3f38-ba67-152ba52b1291 | -15.60688 | -48.07449 | 2026-08-09 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98eb2b05-6493-33ad-8076-614a0d45ad08 | -12.3467 | -53.15805 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48a95149-a6fb-375b-a86d-f5d45f88aa00 | -16.3158 | -49.4347 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f660b5ca-c0d8-30aa-8cae-6a10c0fabf88 | -17.70243 | -44.19516 | 2026-08-09 04:27:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fdd5c19-cedc-3ba1-b8bc-8faf4d3490e1 | -13.86319 | -53.69078 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec60064d-85fc-3541-ac47-b13cd42a4256 | -14.08082 | -53.9896 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a706724-9cc5-30c1-b504-a699ac13b1c6 | -15.09212 | -52.75031 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c981ffd7-9a63-3833-8a7b-666d1ebc4b50 | -15.13641 | -52.72141 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9e16757-84fe-3a3c-9a05-7a08562a606b | -14.02626 | -53.82965 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97d73c08-a0df-3511-b775-8f4155df1380 | -14.35553 | -54.87613 | 2026-08-09 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e8c22d4-6979-3e45-972a-7341fc2c317a | -13.93283 | -58.12574 | 2026-08-09 04:27:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33d44fb2-54a0-3bc4-8e36-38b3a7d73045 | -20.37976 | -41.99871 | 2026-08-09 04:27:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 063b907c-b1ff-3340-81d8-4071d047a53b | -10.91884 | -57.11952 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1b74a7df-6858-340a-90ff-85237198f4b3 | -14.06843 | -53.83285 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d967107a-7b40-3225-a2db-fa4bafaa1d53 | -11.17215 | -54.81374 | 2026-08-09 04:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 406a94ef-2b61-30a0-a7ee-9f0e9f49d1e3 | -13.92586 | -58.12897 | 2026-08-09 04:27:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 564f67a7-7ba0-340b-b8cf-ad4fd66e3f3d | -12.34157 | -53.15409 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d336a076-ede7-3cdc-af18-259aff145135 | -13.97284 | -47.37528 | 2026-08-09 04:27:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff567369-6d7f-3703-9c1d-0b7fc69867c2 | -15.14129 | -52.72112 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 573e94ce-d40d-39f6-9220-5a7d1f1dc82a | -13.96895 | -47.37827 | 2026-08-09 04:27:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c9f5746-fd4d-35ba-b82c-49ba62dc8350 | -20.21532 | -42.57978 | 2026-08-09 04:27:00 | NOAA-20 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 711c68fc-4c94-3ef7-80bb-34e05b75796c | -12.34608 | -53.15497 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25e77fcc-375d-3b0c-a0a2-a409266ee9a0 | -19.79715 | -43.94905 | 2026-08-09 04:27:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf2cfa58-e0a0-3e83-bc4e-fde455dbbb4d | -14.90738 | -48.23473 | 2026-08-09 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1080441a-f29b-3e2d-9465-c10cbf4acb43 | -15.37042 | -53.78031 | 2026-08-09 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b130600d-ed68-3be0-84cb-1f59bcaf146a | -20.55739 | -41.24116 | 2026-08-09 04:27:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9976ab09-f9ca-3cb6-8bc4-ef2847236671 | -20.21437 | -42.57876 | 2026-08-09 04:27:00 | NOAA-20 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ae0dae6c-8c7c-3582-a3a2-fd1e35300113 | -15.07761 | -52.73479 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 473bab8c-f84e-3aae-a3f5-119a45746233 | -14.91014 | -48.23899 | 2026-08-09 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eca13a90-4492-31a7-aaaf-1bab7aba7908 | -20.38346 | -42.00372 | 2026-08-09 04:27:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 2b7a3afe-3549-332c-aaa2-c84b0d469b3b | -14.04918 | -53.83418 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8171c07c-de88-324d-8d5e-f552cc90dae8 | -16.73912 | -43.83902 | 2026-08-09 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6ed9fff-4021-362c-8921-f9a9ae193062 | -14.06567 | -53.82207 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 615f776c-c921-3372-8347-09e923d40eac | -11.19508 | -54.84208 | 2026-08-09 04:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 607066c6-0ce0-3696-a237-cc624d2c3b52 | -15.836 | -42.23351 | 2026-08-09 04:27:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b60c456c-fd3a-3c8c-b07f-bcc9a3546883 | -13.86619 | -53.67448 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 872f058d-3941-37c4-83df-77e3aaf41278 | -13.83737 | -53.7535 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b99b4ed-61ff-3f88-b1ed-239b1734e262 | -18.64421 | -49.85383 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| c1db8098-1abc-37f8-b3a3-a2c69abbb18f | -15.14548 | -52.7219 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48e01624-61b6-3cce-a8ca-fedac3a30862 | -19.14881 | -43.49886 | 2026-08-09 04:27:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23e6c0a0-2c3f-34a7-842a-d9aaf8914410 | -16.31302 | -49.43012 | 2026-08-09 04:27:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7633bc86-ae93-3cd8-ad4f-53a1caf3262f | -20.55069 | -41.02431 | 2026-08-09 04:27:00 | NOAA-20 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 28767949-3e42-32b2-a2a1-380bfbe57ad4 | -15.07689 | -52.73872 | 2026-08-09 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 058829a8-6899-36a9-ac4b-9aa3280fc82f | -10.92176 | -57.12583 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f33aae8c-110c-386d-8c15-cb535058a4f6 | -14.06835 | -53.82979 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 097e507c-13ff-3429-a230-556309666561 | -11.28587 | -53.94484 | 2026-08-09 04:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d09d19d-3a0e-3d5c-800a-d012ba3c7bbb | -13.85989 | -53.68305 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 057f5772-b7a3-311a-9053-b47c15971b77 | -12.3566 | -53.15514 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3912c5-c77c-335d-acf0-a8d1a0c09789 | -12.35034 | -53.16359 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69657e55-f470-3954-a7bd-81ae40801692 | -14.16491 | -54.01864 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fa587ef-9d94-3cd6-b2d8-ca8e869a174d | -14.02349 | -53.8445 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cbff423-e321-3072-9be2-ce3857f56d1b | -14.04734 | -53.8441 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 008fa0ab-efb5-304f-baf7-d4ca9a2e7abe | -16.37187 | -48.9554 | 2026-08-09 04:27:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 928bb31f-d83b-39b8-ba1e-d28291b82b31 | -20.57854 | -41.91609 | 2026-08-09 04:27:00 | NOAA-20 | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8b77e475-03aa-3acd-b28e-7db2cf2352a6 | -13.85005 | -53.73627 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d98f27b6-90a5-3799-a254-888564854b33 | -19.84928 | -43.17576 | 2026-08-09 04:27:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e5439da6-bd97-3ce9-9b09-5f6ac54e5201 | -11.19567 | -54.83898 | 2026-08-09 04:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 524b5d4a-a270-343e-b1a6-09f10566a182 | -18.93616 | -43.47666 | 2026-08-09 04:27:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5ea94845-0698-3411-8bef-e8c5e1999eca | -14.01889 | -53.8183 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8430f322-5b28-3b9d-a4f0-9c69142f4c95 | -14.1603 | -54.01762 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c2d4420-e81e-312e-8f61-294a059547f7 | -14.02901 | -53.84037 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 543b5755-236f-3a69-9fdf-a4b030a9dacb | -14.01889 | -53.84364 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3f38967-8f0a-31e9-a100-3399c051265f | -10.92392 | -57.12525 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0f428ae-e30b-3f50-8d80-f04661cf90a2 | -12.34757 | -53.1534 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1532b36c-18ca-3d26-8f47-8c2c13bba8da | -20.12937 | -43.6838 | 2026-08-09 04:27:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a5a7c637-bc04-3ea8-9c89-e597ccd60fe9 | -14.15568 | -54.01669 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbfac5cb-f30a-3075-a9ff-243eb465a8f4 | -15.87308 | -43.61014 | 2026-08-09 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc0ad961-0346-3736-9aa9-8fbd066dbf46 | -20.27183 | -41.64869 | 2026-08-09 04:27:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be8246b8-8240-3ff4-9e2f-1b6d1431f71c | -14.04092 | -53.80202 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3976edc8-f2a2-30d8-9ffc-0da6c8fedbdb | -14.92083 | -48.23709 | 2026-08-09 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e43c1b05-c7fb-3a3a-80fd-bd0ee7b5f1ed | -14.06658 | -53.81711 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3082744-00a6-3793-92f3-bd592368c04d | -20.21173 | -42.57524 | 2026-08-09 04:27:00 | NOAA-20 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b5a851a8-2822-35c2-893c-ead9097d5cf6 | -18.62847 | -49.8631 | 2026-08-09 04:27:00 | NOAA-20 | IPIAÇU | MINAS GERAIS | Brasil | 3131406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 31177d0b-7fe5-376b-81fe-f338877c8678 | -15.37309 | -53.77846 | 2026-08-09 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25c2ac5a-a2b1-3a14-8e11-af511e297a57 | -14.84651 | -60.06582 | 2026-08-09 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 461512da-1f37-3bce-ba01-6b4f0a6d2b04 | -14.92993 | -42.81427 | 2026-08-09 04:27:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3c0f4bb-b288-3857-a9da-c46dbc3ec74f | -11.16895 | -54.81106 | 2026-08-09 04:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7cb0714-4f2a-35c4-87c1-88bf0664c8b0 | -14.32022 | -54.92706 | 2026-08-09 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e89effb3-8c74-3e9a-81a4-889034507179 | -12.35573 | -53.15981 | 2026-08-09 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ff81fd9-c3df-3f96-b62d-2af5b8a4b0b7 | -15.76214 | -47.76638 | 2026-08-09 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de7dbd13-110e-30fc-b7a7-62cc39631883 | -13.53191 | -44.03616 | 2026-08-09 04:27:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b89d191-8ef1-31c1-a2b2-1445bae25b4a | -14.02166 | -53.82884 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42fcb089-62b0-3e6b-a0e1-187107d85cd5 | -19.58843 | -42.59443 | 2026-08-09 04:27:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| b95016d4-4a36-3ef3-b53c-ee635c043c34 | -19.33962 | -44.53589 | 2026-08-09 04:27:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c43e2a78-4655-312f-b5f7-0c78c3465828 | -16.77024 | -41.48629 | 2026-08-09 04:27:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 38ad88bc-613d-3fe3-9006-2e93db87d32b | -14.02074 | -53.83375 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 693994e2-eebd-3896-b533-db477d215786 | -13.83713 | -53.70389 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da5b374f-25bd-318a-b470-6278d3ee1986 | -13.81068 | -53.69361 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d67ab66-73cd-3a2d-9f86-71b933518089 | -11.1939 | -54.84828 | 2026-08-09 04:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aba0b71a-0e08-383b-a9eb-bb96e5129d6b | -14.03908 | -53.83741 | 2026-08-09 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d0ca88d-9d83-3b7a-a46c-e625c38ece0d | -10.91579 | -57.12448 | 2026-08-09 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bdddbf4-c21f-34b4-9b41-be1023fc0b25 | -15.87276 | -43.61164 | 2026-08-09 04:27:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
