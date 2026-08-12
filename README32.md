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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f84c173-698a-38bb-936d-2c2064569f55 | -13.54471 | -46.2727 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d332b012-7459-3170-a0bf-67b5c347381e | -14.52595 | -49.30008 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9292c05e-e7b7-3a35-b3ec-819384b4b913 | -15.30513 | -48.87922 | 2026-08-12 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db18809e-1c94-3cec-ab6d-19d4093cef9e | -13.88437 | -53.82376 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb939ba8-e6e7-35ab-9d78-d44228393ac1 | -13.9002 | -53.79331 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c09c5eac-63bd-3379-b623-e27c3b27b4ec | -14.52117 | -49.29705 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b666911f-1cec-30c0-8e5d-aacfd7cb7e2e | -13.86752 | -53.83487 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f8df72c-ef32-3965-b37e-902bb4afeed9 | -12.72957 | -48.44201 | 2026-08-12 05:12:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d50b14c9-0bb8-328e-a7c9-b79fdb754819 | -13.83204 | -53.8159 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ad2ed70-371d-31d1-874e-4f89f1acd349 | -13.60506 | -46.23734 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c46b958-675f-3d7e-b015-09f0f10495c3 | -11.10756 | -62.89254 | 2026-08-12 05:12:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db62615-e422-367a-bca2-ab1491ff4816 | -13.90754 | -53.82204 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8f84a81-1944-3e65-ac4d-ba174d277b0e | -14.27983 | -45.28297 | 2026-08-12 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9c1dd8c-6f41-303b-aff9-f5244e900aff | -14.25722 | -49.66276 | 2026-08-12 05:12:00 | NOAA-20 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 064571b0-258d-3b13-a151-6dd5db19e4d9 | -14.9756 | -46.60783 | 2026-08-12 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a41e4369-7cd2-3823-b1b7-06ac7a3ba3fc | -14.51677 | -49.2907 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cff2bc2-8903-3cac-8f9a-553c8899a7c3 | -14.51602 | -49.29706 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a52115b-eaec-3d60-b259-2ea4d0c10dd7 | -16.33972 | -49.46829 | 2026-08-12 05:12:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8a82133-2993-3ccf-91cd-ad75b30a958f | -13.8308 | -53.82471 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2236c38e-cf04-356d-a015-df900e6d2aa0 | -13.43588 | -57.04836 | 2026-08-12 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fdb87c2-70dd-3f8b-99f1-d06f2d56d246 | -13.53097 | -46.28501 | 2026-08-12 05:12:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da9faf1a-74a8-3200-a3cb-a92669bb9172 | -16.34519 | -49.46601 | 2026-08-12 05:12:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae4884fa-4945-3673-ba70-fbc659e22c12 | -12.14589 | -57.19748 | 2026-08-12 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085131a5-5c36-3910-8deb-1a0609e234d9 | -13.8607 | -53.82915 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fa815ad-0df3-3f56-b702-1be51b7597eb | -14.52083 | -49.29994 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2646a992-f684-3d66-9b8d-113a736d6750 | -13.83768 | -53.80286 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50ae2000-4cd3-3d38-8740-25cfe0b9fd14 | -13.8903 | -53.78225 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf3a0d41-e688-3fe2-863e-7972d0fe802f | -14.35358 | -54.86704 | 2026-08-12 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5de3d07-d2c2-3555-a850-0bff6246bcbf | -12.32335 | -53.18554 | 2026-08-12 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 285fb001-2e24-324a-b602-ee801ed34e2e | -13.81931 | -53.90677 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 031d3569-ddca-3fcf-9428-80e5f9233d2f | -16.34483 | -49.46914 | 2026-08-12 05:12:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8bc54759-298b-3f67-a042-39c330ba49e7 | -12.85219 | -52.03975 | 2026-08-12 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d51b1bb9-2f5c-3f71-9093-ec23115f8032 | -14.51982 | -49.30849 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b2b3b6a-273b-35e7-9574-49f62769e2b2 | -14.54743 | -50.40405 | 2026-08-12 05:12:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 384fc00e-8eba-304f-a5bf-592cf6e673f7 | -13.88064 | -53.8232 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fafacff4-ea02-3f5f-b657-bea218f030c2 | -15.1601 | -52.71056 | 2026-08-12 05:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1d4b8ab-9479-3b2b-bdf3-246ffd6da504 | -13.86443 | -53.82979 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7932d8cc-1d7b-3e3a-8413-401274a3326b | -14.30198 | -51.99631 | 2026-08-12 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1b37f43-35f7-312b-9e12-e480b83ceadc | -14.33971 | -54.04911 | 2026-08-12 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bbb8b459-30eb-3879-b4a5-af796cbedff9 | -14.51638 | -49.29398 | 2026-08-12 05:12:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7611bfb1-64b7-3133-923a-9dbc34d7a712 | -16.10858 | -49.88485 | 2026-08-12 05:12:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d52e79e9-3f9a-3590-bbea-41237a6579e6 | -13.27772 | -49.67223 | 2026-08-12 05:12:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f0744a78-facb-3818-8860-31311bc0279e | -18.48145 | -51.69577 | 2026-08-12 05:14:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f158fce3-1342-3656-ab3a-90c3c9c7e590 | -18.48087 | -51.70059 | 2026-08-12 05:14:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7679470-5f0e-3063-a452-0e3cba33418a | -20.96205 | -47.41425 | 2026-08-12 05:14:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 779227d3-5844-356e-9fb0-4c88af2e69bc | -18.96461 | -49.50422 | 2026-08-12 05:14:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc9e153f-2a2a-3966-a4e4-e44e6e95a9ef | -21.31065 | -46.7352 | 2026-08-12 05:14:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0f11de74-e9e8-3b0a-b991-e498e7ad9ca9 | -21.30418 | -46.73468 | 2026-08-12 05:14:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3cab2b51-077d-3953-af0b-7187a288d835 | -18.96379 | -49.503 | 2026-08-12 05:14:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc5ae07b-439d-35c2-a878-a4443eb93134 | -20.96703 | -47.4165 | 2026-08-12 05:14:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5c4ea9a-b89f-32d9-b0e6-42cbf6b15f07 | -21.49811 | -48.64048 | 2026-08-12 05:14:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0c67d8c-9520-3c35-80b2-4d646fe0d452 | -18.48543 | -51.7011 | 2026-08-12 05:14:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d98bfe3-b819-3061-8031-645766b5bfb8 | -18.96909 | -49.50367 | 2026-08-12 05:14:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c82372c-7b9c-3307-8004-af21682b8e65 | -21.49878 | -48.63859 | 2026-08-12 05:14:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 539d9946-c960-3e30-8783-6ac5aaf5e521 | -20.96822 | -47.41499 | 2026-08-12 05:14:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 591424a0-29df-3288-8c13-2774dcdd9ae5 | -21.49301 | -48.63795 | 2026-08-12 05:14:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db627801-de61-34d0-931a-efd46c31a82a | -18.96945 | -49.50017 | 2026-08-12 05:14:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9d7e56d-0596-3bc4-989a-acfafcd46646 | -18.96499 | -49.50082 | 2026-08-12 05:14:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eef56cb8-a7ce-3a92-9500-fa2f1a8387a5 | -22.26475 | -48.6609 | 2026-08-12 05:14:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6abb9bdd-fad3-3436-9940-f92778d4c238 | -20.65387 | -55.40774 | 2026-08-12 05:14:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65f6bc33-3674-3eb4-a3e6-5f233dae4e5a | -11.9539 | -46.3217 | 2026-08-12 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| d47e042b-fad7-37cc-bd8f-a3a3d751c4e8 | -11.9527 | -46.3899 | 2026-08-12 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a4c36f35-2b46-3bc1-bc0f-6473571ac68b | -11.9535 | -46.3444 | 2026-08-12 05:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| be4b296b-db08-3ddf-a98c-13d2273abd0a | -8.96 | -60.5358 | 2026-08-12 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d2578e13-3009-3897-9718-f0fbee7e30df | -11.9911 | -46.3844 | 2026-08-12 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d5b00e55-2b3d-3190-9348-668ac7499bed | -11.9535 | -46.3444 | 2026-08-12 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3673edb6-712e-3293-ae33-882c151612be | -11.9535 | -46.3444 | 2026-08-12 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c81d7d73-e53f-3b5e-8632-cf416cb1b1c9 | -11.9911 | -46.3844 | 2026-08-12 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6760f8b3-cec9-3bf6-82e1-2e0971805d7a | -11.9539 | -46.3217 | 2026-08-12 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ef37fe8e-d99f-319e-921f-ce550f66a703 | -11.9911 | -46.3844 | 2026-08-12 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c522c70c-842f-3b57-9ba7-a9215f5656c9 | -3.14853 | -54.60675 | 2026-08-12 05:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e21e267-412f-3b76-9b64-70345b6e70bf | 2.64742 | -60.08894 | 2026-08-12 05:53:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0affbb35-3468-3781-83a3-a8174fd0f984 | 4.18202 | -60.02639 | 2026-08-12 05:53:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09b9350c-17f9-36fd-be00-904fb7bf019b | 1.68856 | -61.07917 | 2026-08-12 05:53:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e19de0b-c4e1-30e9-9f05-1d7bc635bf1c | 2.64701 | -60.09008 | 2026-08-12 05:53:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74e689af-ad2c-3c96-a520-d536ae857135 | -2.947 | -60.92698 | 2026-08-12 05:53:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1260a239-1f93-3f65-9052-71110560f1cd | -8.95791 | -60.53519 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93c1279a-88a3-37d0-bc7a-9b7e6d60a8b6 | -9.764 | -60.76541 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8f4c375-28ef-3a48-90a9-2c457017d7f4 | -7.40662 | -59.99638 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc840495-7a25-3ca8-8af6-8e76536254a3 | 1.09943 | -60.51438 | 2026-08-12 05:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25af12ab-8c95-34a7-a89b-5d7998e80467 | -8.95864 | -60.5695 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa7214a4-ef40-39c6-8e40-dacab5fe52b5 | -6.60301 | -59.00802 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 783e8c12-623e-34d4-be53-ffd7fa77de92 | -6.60898 | -59.00529 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afa6678f-6de8-3692-b5c3-af4ad7c88dba | -7.4005 | -59.99301 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3624244c-157a-3e12-a0ca-d8d2f3ffdda9 | -8.89751 | -60.57618 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88e28167-cd03-3fc9-9ab9-65fe516581ca | -8.95903 | -60.56652 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ff547db-a669-320d-86f1-cbc111addb91 | -8.95164 | -60.50299 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 360af8d3-a2a4-3da7-b97b-996af1f14aaf | 0.18928 | -60.48805 | 2026-08-12 05:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 164a8aa0-eefe-3728-810b-20bd751594e7 | -8.8924 | -60.57547 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d62d31a2-b677-32f8-bd94-76f633b33be3 | -8.94691 | -60.4991 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 359d4544-32f6-3ebe-a282-324777ace13e | -9.7565 | -60.7599 | 2026-08-12 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9a2e518-dc4a-3647-926d-a6d6eda5ed2e | -8.9488 | -60.56508 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 151cb922-2103-3032-9798-d972747bf4cb | -8.95758 | -60.49751 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36338a05-fa30-382e-9d1b-5a163812e85f | -8.95551 | -60.55354 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fa4aecb-1438-30df-92f5-dc5bb2a7053a | -6.61496 | -59.00257 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e60f0c79-ee19-38ca-bc9a-76d690f2c714 | -8.95712 | -60.54123 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 013dbf73-d574-3112-9f6b-6b4169ab726f | -8.95084 | -60.50918 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31a3e31a-aa8a-3e50-a31e-65679ef19a86 | -9.47163 | -60.52538 | 2026-08-12 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af35fa2d-7f3d-35bf-bb11-40bcd32ec0f0 | -8.98646 | -60.5954 | 2026-08-12 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd0fcbff-0a89-3b44-8bc8-274862cb0acf | -7.40576 | -60.00283 | 2026-08-12 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README33.md)
