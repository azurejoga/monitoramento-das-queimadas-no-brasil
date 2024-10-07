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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 210151f8-29fb-306e-bbd6-9fff549426c5 | -20.19543 | -41.83184 | 2024-10-07 03:17:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4fb070dd-7f1a-39e5-91a6-74a14329b348 | -20.1325 | -43.86205 | 2024-10-07 03:17:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 901536f0-3aff-3d5d-9bd0-6bedba791cb3 | -19.97899 | -42.45932 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2613f515-89e0-30ca-a83e-99c51dbcb1e0 | -19.97298 | -42.45776 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de904d5b-35af-3e93-adbc-230fa76f1e58 | -19.96699 | -42.45613 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e5e3b9c2-da64-3369-a47d-b7e31d50c6e1 | -19.96583 | -42.45872 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8a186381-ed75-33c9-bfc5-08eff00a1f3d | -19.96467 | -42.46387 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 25a5796f-d339-39fb-9c0a-4db6f0348413 | -19.95871 | -42.46207 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| dbff3f4c-320a-3df4-af3b-7108199e1a88 | -19.95864 | -42.46463 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| afb6125f-a856-3292-8001-fd11dfb74134 | -19.95756 | -42.46715 | 2024-10-07 03:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1dc13dc4-7850-3bb6-ba6d-0c77c87ad85f | -19.94163 | -44.08915 | 2024-10-07 03:17:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| aa3edebc-14d4-3449-9bb7-a10074c9293b | -19.89686 | -42.65021 | 2024-10-07 03:17:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 981cea17-0fed-3d58-b5be-8e05302cca65 | -19.89679 | -42.64698 | 2024-10-07 03:17:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cf33887d-c440-34a7-824f-6fe401b42cab | -19.89555 | -42.65228 | 2024-10-07 03:17:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 73506e63-5370-3d66-8bb2-9ff5b2005f4e | -19.89307 | -42.63857 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| f4c0ca25-89d0-3717-bd63-bd6546e96cdc | -19.89296 | -42.63579 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 633c0474-cd13-372b-b7b5-f68d14b28cef | -19.89195 | -42.64347 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4a47212d-380f-396a-9c57-4bdb6eaa36a7 | -19.89183 | -42.64059 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 9e6810bd-4d13-3891-957a-2f4e7fdf5a44 | -19.89082 | -42.64842 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 35645fe4-5c26-370c-80c4-dc5e133fdd9b | -19.89067 | -42.64555 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 904e9ada-016c-3a22-93cf-0fe1eed6366e | -19.88975 | -42.65314 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ff10ed52-eb18-3f60-9da1-8b5d907354ea | -19.88955 | -42.65033 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| a8296ee0-ae90-3a8f-a76e-9cf639daac4c | -19.88866 | -42.6579 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 12ef6724-4337-3092-b785-941af0c6f237 | -19.88846 | -42.65495 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 9f237bcd-8f90-3a02-a0be-36b987a93a32 | -19.88731 | -42.65982 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 5206e15a-2778-3d32-8ace-0e191e8e30b8 | -19.88696 | -42.63707 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 05b27cb1-182a-3c19-b4a3-2e702460f02f | -19.88365 | -42.65158 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| c742d930-0938-3947-9b5f-203036fdae24 | -19.88343 | -42.64887 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 5ff4d366-e4e9-3ec7-aa3c-6d1762ac6524 | -19.88255 | -42.65637 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| db6f05aa-628c-3875-9912-0157649b399e | -19.88233 | -42.65352 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 75606db3-fff5-3b55-976f-5e0307486fc7 | -19.8812 | -42.65835 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 45ec6d82-931c-3698-a8d3-98a365566ddb | -19.87861 | -42.64541 | 2024-10-07 03:17:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 706a6340-5a49-3072-a765-5d7b23d3f90b | -19.8614 | -44.10182 | 2024-10-07 03:17:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d786aa47-53ab-3380-afe3-b03a7bd867ed | -19.8492 | -42.38436 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dd6dac82-77c7-3f1a-be61-79a9133722bd | -19.84893 | -42.38094 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9af28992-25a5-3de9-b2aa-2b2184325762 | -19.84528 | -42.40117 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85602daf-39ce-343c-83ee-c548b06bdcd7 | -19.84406 | -42.4064 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 51901849-5158-31a6-b298-e5d31b89167f | -19.8433 | -42.38237 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3f54507e-164b-33f2-9894-56645d574ba0 | -19.84135 | -42.38636 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5ab962ba-4391-3622-8b01-aaf2b2db9b74 | -19.83131 | -42.37457 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2a074be0-1500-3f5c-8194-9faaf6ac2f17 | -19.82979 | -42.38129 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3e5b7c08-b8f0-35c5-8eeb-9a0676409300 | -19.8265 | -42.3678 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e35b65a6-9511-3306-870d-b4aa4da4d0eb | -19.82507 | -42.3741 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 34a5c21a-65d2-3e88-8490-084074a592ae | -19.8237 | -42.38008 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 22f881a8-ec99-394d-848d-a57d76c89480 | -19.82012 | -42.36792 | 2024-10-07 03:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 33fcd1f1-1dd5-301d-af27-e2522273bac9 | -19.77674 | -41.99638 | 2024-10-07 03:17:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4bffa30a-b0d9-3627-9de6-5990bef9aa5f | -19.77562 | -42.00132 | 2024-10-07 03:17:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b60f1a89-a349-3a1e-af87-4d290f5a35a1 | -19.77452 | -42.00618 | 2024-10-07 03:17:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8ccfed0b-691d-3719-a07c-b52433af0119 | -19.77412 | -42.65385 | 2024-10-07 03:17:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 122e4d60-fcca-3da2-aa4a-8543f9c8e7af | -19.7728 | -42.6557 | 2024-10-07 03:17:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 51d5de3d-e5ae-3544-b6ad-0b60b8da3e2b | -19.76795 | -42.65257 | 2024-10-07 03:17:00 | NOAA-21 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1e41af67-3807-3e10-85b2-d5b7d07e8fde | -19.66386 | -43.1913 | 2024-10-07 03:17:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8254efc9-5d69-31f9-ac8d-f798fb58f72e | -19.64917 | -41.48607 | 2024-10-07 03:17:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 66861d00-e812-386f-a11e-b3855ab3e143 | -19.56631 | -42.7531 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9f2ee58b-e980-3ad6-9c61-cbaa000a6a2c | -19.56531 | -42.74885 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 024846f3-5ded-3226-9a13-74a3d946af2e | -19.56422 | -42.7535 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 0a6ae3cb-2425-3ed6-ab43-8c2e6f327cd4 | -19.56146 | -42.74569 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 069785ec-2458-33da-bac7-ae1d3fa8a9b4 | -19.56033 | -42.75065 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 9cd3422d-68e2-365c-bf6e-1990ad4f9257 | -19.56019 | -42.74278 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| b93e746b-3810-3726-bb12-8fccd55e84d9 | -19.55908 | -42.75616 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 025ba554-d53e-374a-afc1-e13784e3fc55 | -19.55908 | -42.74751 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 47d310bf-2441-31f6-9036-562f45bb6930 | -19.55787 | -42.75269 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 25b6be45-d75c-3eb3-94f2-c401d4c89686 | -19.55592 | -42.74137 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 09a2e815-aa22-3901-ae40-aa8490feb9b1 | -19.55488 | -42.74594 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 8f3df2c4-aa61-3e2a-ad5f-46bf6249c89c | -19.55376 | -42.75087 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| a2367c53-477d-33eb-b9e0-a35858901e46 | -19.55366 | -42.74278 | 2024-10-07 03:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 56238970-0a1b-31f7-839d-0acc49cb1ec5 | -21.9505 | -45.36775 | 2024-10-07 03:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 26bca180-04b5-32db-8163-c30a8c829699 | -19.86297 | -44.0954 | 2024-10-07 03:17:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af178eec-b633-3d03-ba29-dcafe6e4f9cf | -23.16232 | -45.555 | 2024-10-07 03:17:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 9ed9e4a4-f113-3102-afc0-f6f0b8329228 | -22.9037 | -43.75595 | 2024-10-07 03:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 27691837-2a6d-3285-8cc7-12cda2952e56 | -22.03212 | -42.88763 | 2024-10-07 03:17:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9e4bbca9-1161-3d73-9f4a-763c675f04a6 | -22.03001 | -42.88654 | 2024-10-07 03:17:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2789a629-5018-3620-ba7c-38d623f27b05 | -22.02877 | -42.89191 | 2024-10-07 03:17:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f1b90b4d-f52c-355d-bd8b-c463f8942555 | -21.95559 | -45.37617 | 2024-10-07 03:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| cc5512a6-d7b5-3d08-8230-71752e0345ba | -21.95528 | -45.37589 | 2024-10-07 03:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 4c83aa21-519c-30ae-b55c-68a32882356a | -21.95416 | -45.38173 | 2024-10-07 03:17:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 8c811cc5-b60e-3f1b-9231-7906f5db5e2b | -21.95387 | -45.38155 | 2024-10-07 03:17:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 91b4d739-d118-3283-9b8a-67e9c03face9 | -21.95016 | -45.36744 | 2024-10-07 03:17:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 2860ce8a-a4f1-3fe5-9090-a8f3af9b58ff | -21.94423 | -45.36394 | 2024-10-07 03:17:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| feb6a1cc-5b90-3fd9-8df2-f203533c1b32 | -21.81035 | -42.5169 | 2024-10-07 03:17:00 | NOAA-21 | CARMO | RIO DE JANEIRO | Brasil | 3301207 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 60739481-b8db-3063-a8ed-f0fd6cfa2ab3 | -21.80634 | -42.51526 | 2024-10-07 03:17:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 66e1b22c-8046-3c75-85aa-4e85f6472f70 | -21.80567 | -42.51052 | 2024-10-07 03:17:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 37e207db-ea7c-37af-a158-75f374b9ac22 | -21.80533 | -42.51972 | 2024-10-07 03:17:00 | NOAA-21 | VOLTA GRANDE | MINAS GERAIS | Brasil | 3172103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c788d84f-b4bb-3a8a-8ac8-786856b52f6b | -21.5906 | -47.7409 | 2024-10-07 03:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 389c2ea0-1402-3891-acd7-2f2e71dfdc6d | -21.5913 | -47.7172 | 2024-10-07 03:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 193.5 |
| d81d53bf-5919-39c6-b349-8a9ff6755502 | -21.5691 | -47.7696 | 2024-10-07 03:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 130.9 |
| fa7903b4-78d6-349a-bc47-77b83b29174e | -21.5698 | -47.746 | 2024-10-07 03:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 260.6 |
| 856e00f5-de05-3ef6-9c8e-861e90f54988 | -21.5705 | -47.7223 | 2024-10-07 03:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 0a6ebc94-07c9-3e8c-9ab4-2f3a3b8a4f6f | -21.605 | -47.9485 | 2024-10-07 03:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 27a19ff5-7e8e-3a0c-ba7f-2039610c3df2 | -21.6121 | -47.7121 | 2024-10-07 03:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 3ad45ee2-ad8e-3001-86dd-ed87fc66e298 | -1.0365 | -53.7389 | 2024-10-07 03:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2ad913d1-8719-35e1-af11-2913b462c60a | -2.857 | -52.8993 | 2024-10-07 03:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b20f48b2-4f6b-330e-9882-538762ff4d2c | -2.8753 | -52.9192 | 2024-10-07 03:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 51fded73-3c3a-38a0-a245-eae8ede9af2f | -2.8754 | -52.8989 | 2024-10-07 03:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 60365ea3-6222-34f7-bff9-26f71b7311aa | -4.2728 | -43.7601 | 2024-10-07 03:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| e21dedb5-a157-3262-a3ee-027be5effb30 | -4.2729 | -43.737 | 2024-10-07 03:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5f9da789-8388-3f15-9010-78059c607765 | -10.8754 | -63.9169 | 2024-10-07 03:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 3a6f3f80-0e63-3a53-a804-9ca58e272f44 | -10.8755 | -63.8979 | 2024-10-07 03:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 27c5606e-6c5f-36bf-a96f-d117fc37bd0b | -11.2847 | -51.3878 | 2024-10-07 03:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 02cb776c-ac38-35fc-a09f-fe640cdbe022 | -11.285 | -51.3666 | 2024-10-07 03:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |


[Clique aqui para ver as próximas entradas](README41.md)
