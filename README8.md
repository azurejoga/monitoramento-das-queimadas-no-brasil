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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16e1ee9e-8d9a-3c33-9a7c-753162a030c8 | -12.39729 | -46.64401 | 2025-11-03 04:31:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bc62f10-b75c-37e8-9ec0-98db1a6ef44b | -10.42505 | -44.35216 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4cf7bb1-6492-33c3-8897-517c2f96548b | -14.50335 | -43.85507 | 2025-11-03 04:31:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2ebe56d-14d9-3f32-82ae-665c2e30df36 | -10.5097 | -44.48376 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0651e26-5ab9-36a8-8c62-23a65ac6d025 | -10.8508 | -44.73442 | 2025-11-03 04:31:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4733558d-0771-3505-b876-78ce9366677d | -12.01767 | -44.79681 | 2025-11-03 04:31:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7638bdfc-2355-3668-a95b-d17d3def8e9a | -10.65643 | -51.89199 | 2025-11-03 04:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f0c104f-a424-30fc-8fd3-b443ee38da03 | -13.50097 | -47.09119 | 2025-11-03 04:31:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1955574-01ae-399e-8955-2f00ea9c14dd | -10.96533 | -44.4691 | 2025-11-03 04:31:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c104a8e-37c0-343e-8455-8cb9ae22ade3 | -10.623 | -44.66925 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c85aa596-d740-3383-9fd4-3125cfa295ce | -11.0073 | -42.73902 | 2025-11-03 04:31:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 40deecd7-cbb2-3c7b-815d-c6c50a8b2cd0 | -10.77087 | -46.31628 | 2025-11-03 04:31:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef63504a-8365-3a44-9cfc-122868680c4f | -11.61888 | -58.27829 | 2025-11-03 04:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d86090fb-9f2f-3b71-b3b1-7f55d4e550e9 | -12.01412 | -44.79625 | 2025-11-03 04:31:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ef13237-9116-3b8b-a6e7-06cd283d823e | -11.51639 | -44.99946 | 2025-11-03 04:31:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36db2ed2-b5d4-32da-9890-98a37370bcde | -10.42803 | -44.35667 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ab1286-bec2-3ba5-91c5-686e741ff33b | -10.54871 | -44.90316 | 2025-11-03 04:31:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 604ad2e8-2f12-36b7-a841-6ff2703e7aa8 | -11.11518 | -41.09088 | 2025-11-03 04:31:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 248acc8d-9fbf-31da-a5c5-8808f6d1f302 | -11.17817 | -40.95842 | 2025-11-03 04:31:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c2cae1c-a649-393a-9ac5-94966f62e46a | -12.42207 | -54.48589 | 2025-11-03 04:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cfe190b-b9d1-3a43-be94-6592a063ff1e | -10.30216 | -53.77606 | 2025-11-03 04:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 940c3abb-7efb-37f9-bc80-a23b445a89fd | -11.17756 | -40.96286 | 2025-11-03 04:31:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9f235e8-0e84-3f4e-ac8a-fb16358b9fd6 | -11.06029 | -45.32896 | 2025-11-03 04:31:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f49b8e6-df39-39aa-b14c-1ea66694bea2 | -11.9496 | -44.79963 | 2025-11-03 04:31:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e280f33a-86b9-3ce9-9d42-f65e6eb64d41 | -11.05626 | -45.33224 | 2025-11-03 04:31:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 248f3a62-ec43-34cf-abb2-e407a49ea3e4 | -10.4054 | -44.3617 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62d3cfe1-51b4-3071-8f75-757246170828 | -11.61804 | -58.28252 | 2025-11-03 04:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 141a6591-ce8e-3b63-966a-a187ee00f342 | -10.62653 | -44.66981 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8a4b7b4-07b2-3b85-b858-25255ac8f763 | -10.97271 | -54.25347 | 2025-11-03 04:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40ff69fe-ad2c-3393-b43c-cc706e0b9edb | -10.40348 | -44.35863 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dceef33e-1a62-3a73-bf1b-768d3a5a917c | -11.39211 | -46.71681 | 2025-11-03 04:31:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8d4932b-f22a-3cba-9bba-923c796f6a91 | -10.42725 | -44.94437 | 2025-11-03 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a1a5fd11-90df-3aa6-a69b-6626c103172e | -12.68896 | -41.56706 | 2025-11-03 04:31:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9917a238-28ff-3c2f-ab43-18e12093cf1e | -11.11957 | -41.09156 | 2025-11-03 04:31:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85a89a35-7580-3c36-8b7d-c7abf2f28a48 | -11.05683 | -45.32843 | 2025-11-03 04:31:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32395fcb-2727-352f-bc90-6793ac19ac25 | -13.61768 | -45.30941 | 2025-11-03 04:31:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d141d1c1-42c8-3083-afab-d07768ef6273 | -10.85072 | -56.95853 | 2025-11-03 04:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc901179-d09c-35f6-b0a9-b4e21d57d591 | -13.94348 | -43.55455 | 2025-11-03 04:31:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 257c4daf-e988-322f-9919-28faf845eb3f | -10.42909 | -44.94963 | 2025-11-03 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bd0c4c86-8584-3c4a-ac5a-c74fffb4064b | -12.39393 | -46.64347 | 2025-11-03 04:31:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d01c488d-894a-35cb-9014-10097f600999 | -11.21386 | -43.74062 | 2025-11-03 04:31:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91c4eb74-a47b-3423-a64c-95d8f4a5a266 | -11.14201 | -45.38761 | 2025-11-03 04:31:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30d72df0-2f96-30db-b1ba-d3717f3fb220 | -14.50403 | -43.85018 | 2025-11-03 04:31:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9514f348-04fa-3f74-b9fe-df5e6a5b9a71 | -12.40287 | -46.63013 | 2025-11-03 04:31:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db2e94a2-f991-3e15-a017-b434311c12b5 | -14.27039 | -47.99192 | 2025-11-03 04:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1e78ea0-0513-3f85-8ec9-e4e24cfb706f | -10.5408 | -46.66888 | 2025-11-03 04:31:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a98c21c3-d1ea-372e-a745-c13ad1d53b0a | -13.30168 | -41.92249 | 2025-11-03 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| cbbe735e-65eb-3d55-b55a-f4fa9a8ceb25 | -10.42667 | -44.94823 | 2025-11-03 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c3dbeb32-076e-3d9f-9205-9e8d89b9ad47 | -10.4262 | -44.94526 | 2025-11-03 04:31:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3bc4556f-809b-30c2-929e-c8d9ad77af46 | -12.40176 | -46.63734 | 2025-11-03 04:31:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c7d348f-ada8-3f34-aaf0-fe1c2f809e90 | -11.56971 | -47.07497 | 2025-11-03 04:31:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83d3994d-cdd2-3a36-83c8-579edd63a55a | -11.01124 | -42.73959 | 2025-11-03 04:31:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2c4125ac-0e18-3e83-8cf1-e74f64cea98a | -12.39785 | -46.6404 | 2025-11-03 04:31:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3bd5f276-90c3-3eac-b9fb-a193945ea048 | -12.33426 | -43.6559 | 2025-11-03 04:31:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 761a648c-3eda-330e-a787-aa48fcbd22ea | -10.61948 | -44.66868 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3cbe1bd-580c-3c32-8025-0508376746e1 | -13.30591 | -41.92343 | 2025-11-03 04:31:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| a0302caa-9d60-33d0-86f4-ab3bc4ac9509 | -11.1146 | -41.09518 | 2025-11-03 04:31:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5c6a58f-cd14-3b46-8ef9-c89c53977d9b | -12.40232 | -46.63374 | 2025-11-03 04:31:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e58bed53-85f9-39ef-818f-02ea4775f8dc | -13.61415 | -45.30885 | 2025-11-03 04:31:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a6eead6-586e-3920-96f3-883188bfbf81 | -10.64178 | -44.68838 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 84d63a71-7ad9-3dec-b7b2-74b7a90706c1 | -10.84528 | -56.95743 | 2025-11-03 04:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 895b84a4-ca9b-35b1-90b4-efc7714e1509 | -11.61217 | -58.28146 | 2025-11-03 04:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c86c4dc-2ce4-382f-a87a-a922e1055834 | -12.76766 | -43.47583 | 2025-11-03 04:31:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 785177a4-cc14-3ac7-83ff-78b036b9c249 | -9.75892 | -55.6194 | 2025-11-03 04:31:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b361febb-35cf-377d-a330-9518500781ed | -12.42293 | -54.4813 | 2025-11-03 04:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08829436-9abb-374a-9ebc-eb1576e8e7b2 | -10.6183 | -44.67655 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58b886cb-ee59-339c-93b0-df01938fc109 | -10.62183 | -44.6771 | 2025-11-03 04:31:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7af924-d89a-3250-9700-ac04101b10b1 | -11.95021 | -44.79556 | 2025-11-03 04:31:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4703243c-7b69-3f42-8c16-adb069cd0f8a | -18.83887 | -40.17708 | 2025-11-03 04:33:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df1b111c-dce1-3339-a295-c4467333b71f | -18.83851 | -40.18037 | 2025-11-03 04:33:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b4f7291f-12eb-328c-b09e-3aeb1340c1f7 | -5.0399 | -43.6205 | 2025-11-03 04:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 50d30d67-1714-396c-a62d-70592f0b997d | 2.13475 | -50.99338 | 2025-11-03 04:48:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4519532c-5a90-3fa5-8058-dd99ad66aaff | 1.70398 | -50.93436 | 2025-11-03 04:48:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bac0db3-7d77-3099-9690-c336ca424342 | 2.13144 | -50.99389 | 2025-11-03 04:48:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baa96995-f166-3929-9e4a-9da1c45be5cc | 3.23173 | -60.75791 | 2025-11-03 04:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b758a670-e9da-34f8-ab12-b7323e37083d | -5.0399 | -43.6205 | 2025-11-03 04:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 615f4995-bc68-3509-89bb-a8b02f876484 | -0.8915 | -52.0328 | 2025-11-03 04:50:00 | GOES-19 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3e170eca-4b8b-33ce-a4b1-1514e1a71eab | -3.43811 | -51.47131 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d50e7aa-b51e-32c1-a5c8-8ae7bc1e46f1 | -2.49133 | -48.15448 | 2025-11-03 04:50:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05313d6b-1506-39bf-93a8-de00c434a7ea | -2.31635 | -48.58516 | 2025-11-03 04:50:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9595a74-6cc2-32c8-a640-083cdf31df67 | -5.26702 | -50.96806 | 2025-11-03 04:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4207cc2-bdbf-330f-ab6d-4da860be4e34 | -2.72312 | -48.34859 | 2025-11-03 04:50:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2fc39d7-b9fa-368d-ae83-5f434ec8e78d | -5.43154 | -46.36488 | 2025-11-03 04:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71162cb5-b45c-31a6-a381-25894edf1f5b | -2.90417 | -53.96152 | 2025-11-03 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4db5b4c3-3c58-34cd-a716-d018d90adeb3 | -3.22412 | -50.58462 | 2025-11-03 04:50:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca52d6d-f715-30b9-913e-49d5835da07f | -3.42863 | -45.90253 | 2025-11-03 04:50:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98f9d241-1baf-333f-b52d-93c5139ecdcc | -3.77069 | -51.79851 | 2025-11-03 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b39b93-d609-3e4c-800c-dc5f0fac9668 | -6.68609 | -46.67165 | 2025-11-03 04:50:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ffacaf-4631-39c6-8497-002d20102b43 | -3.02007 | -49.44216 | 2025-11-03 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9ed1058-d13b-33b3-833d-d52cf5985f59 | -1.96852 | -52.10629 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 767e2c3c-31bb-3d5b-ac67-0098eec6ed06 | 0.45856 | -50.88408 | 2025-11-03 04:50:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cf5fcfb-7600-3be2-a132-c31562877aa9 | -1.96411 | -52.11268 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83c8f263-419d-3590-9dd9-eaa9185fa3f6 | -1.24062 | -46.02859 | 2025-11-03 04:50:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f267a6d-681a-37b2-9548-f8705897394b | -3.1734 | -46.58252 | 2025-11-03 04:50:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d4f513b3-2e5e-32fc-b6ad-22bb67f9cbcb | -2.90453 | -51.58147 | 2025-11-03 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d5db775-dbfb-3dd7-ae8c-b817167c8562 | -5.42785 | -46.36005 | 2025-11-03 04:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9258cd03-b691-32f0-adca-7a9351cc323f | -6.68123 | -46.67513 | 2025-11-03 04:50:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5f61f11-e12f-3e9a-a205-9141f75baf1f | -1.9386 | -52.70504 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fb1af96-2b01-3b2e-949f-a0f7113d7833 | -1.96466 | -52.10922 | 2025-11-03 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22f76ba6-9528-3902-89d3-aa3c3f6b5395 | -2.81949 | -54.03433 | 2025-11-03 04:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
