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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87795b2f-a7d2-321f-862f-cd8b213d0d3e | -15.03795 | -46.9723 | 2025-09-29 12:19:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1713750c-4872-34fa-8750-6359baaa330f | -10.39313 | -48.16222 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9b3a765f-43ee-3e68-8054-2e3bb2144b2c | -12.48887 | -48.02312 | 2025-09-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 15d70fd5-615a-35ac-9a2d-95d6152631c5 | -11.40895 | -47.31836 | 2025-09-29 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 80faf5fe-ce83-3aa2-894c-125245c6835b | -20.34987 | -44.85248 | 2025-09-29 12:19:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4f12fb0d-1720-3615-af86-063a7b7f6efe | -14.70444 | -45.22142 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 4582b8d6-a854-3477-84ec-4123a244cec3 | -13.60675 | -48.06651 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 98cd704e-b221-3619-99b0-b534599ef840 | -14.7858 | -46.17418 | 2025-09-29 12:19:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2f2e7ed7-f55a-3886-be60-cec981f20c51 | -13.8367 | -47.93612 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ade56b4f-7e04-3db9-a650-6323374c8b79 | -15.7605 | -48.14127 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 2a624761-b351-3389-9e37-11ddfbf9baa1 | -12.67773 | -46.8728 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4b6898c5-1466-3a7a-ad5d-def8ac7f0ff5 | -13.23247 | -50.97488 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 647.7 |
| ac5db01e-d99c-3598-a357-ab31613dea41 | -11.92907 | -48.06968 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1326a3b5-95e2-348b-9d3b-29117fcc13f8 | -10.39574 | -48.14417 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c5552773-edbb-3bfe-8833-6371a6672be6 | -10.19446 | -46.91172 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c0d1280-e561-394d-a28a-70b6566e408d | -14.54791 | -48.44899 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c5956a8d-3ab9-3dcf-a904-0e30411812d5 | -10.31238 | -48.20829 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 48bd5bce-1457-3c94-a344-c3f9cba136ac | -15.07385 | -47.25512 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b15daf0c-d025-3ab1-b19b-d59a0043f95a | -15.28556 | -46.41933 | 2025-09-29 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ac88deb7-6508-32a9-801e-dc7ea7e82e20 | -13.60803 | -48.05749 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 71b6f98c-4897-3a88-a670-7c8186734b34 | -14.68134 | -48.15846 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 65006165-a732-323b-8bb0-0ac0c2ff994b | -12.84625 | -46.98571 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41009473-1c55-3125-859b-9a271a14cf24 | -15.16998 | -46.41289 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 743b1d22-cc7b-35bd-aea3-5e5b15ba1125 | -14.61679 | -48.28272 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a730c0f8-17b5-36a9-9699-67de31b460b6 | -10.40979 | -48.10959 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 54ea48fd-71f1-3129-8688-504595e9693a | -18.15612 | -51.47255 | 2025-09-29 12:19:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 89557381-1de3-38d4-983c-4e21fd370a1c | -13.72542 | -48.65043 | 2025-09-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1237f2aa-e166-3046-a3ba-8446b08c665f | -18.47424 | -43.99488 | 2025-09-29 12:19:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 38.1 |
| e00ee579-4320-3094-8300-be154eca5165 | -10.38544 | -49.03413 | 2025-09-29 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 12f15136-b7c3-38b0-bfda-06b0a1d1e99f | -15.27922 | -49.25559 | 2025-09-29 12:19:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e38ba25c-187f-34b7-925a-68b16332f296 | -12.42256 | -44.10611 | 2025-09-29 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 47193028-9c96-3fa8-bd74-f2ebc52c07d2 | -12.96588 | -45.17687 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8666afec-9962-3a6a-8185-851537aac137 | -15.25131 | -48.03518 | 2025-09-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7a07f8b9-5835-3d79-abcc-0eb642e9af25 | -11.47917 | -43.51392 | 2025-09-29 12:19:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3e9adf19-ff00-3f81-ae08-0fc73eb68b6e | -11.36725 | -45.07525 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 2964f40d-a59d-3b0f-8593-506dc4677848 | -12.84754 | -46.97635 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3748d3c4-d10e-3cfb-9ae4-edb1c12b2536 | -9.64286 | -48.12293 | 2025-09-29 12:19:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 716f7253-3b64-3699-8b19-a08a40e47b97 | -11.97783 | -47.13869 | 2025-09-29 12:19:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f05e0a0a-1063-38e6-8641-1c9e61c0b370 | -11.26818 | -47.20287 | 2025-09-29 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 6f56c6e7-69e8-3b21-939f-c3b7bbce1be5 | -10.39444 | -48.15313 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| b35b516b-d976-3a74-b725-0d15899ade5b | -12.70999 | -46.90612 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| ece11242-4123-3b38-be29-f1f03170eb00 | -13.02941 | -49.43539 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6794d6b-1500-399c-a321-5fce3281c56c | -13.275 | -48.45166 | 2025-09-29 12:19:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ca772c18-bb90-3e54-92b1-3eecb5d74cee | -9.78684 | -46.93102 | 2025-09-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d50db77e-dc3c-3ba4-b010-caa0657fadc5 | -10.68566 | -46.76043 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f00c6e52-658c-3d68-aba4-99ed44efb090 | -11.98935 | -46.5914 | 2025-09-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4e5e20de-01ef-326a-be1c-9440358c8284 | -9.42578 | -48.34607 | 2025-09-29 12:19:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 371b0ccc-f685-3831-8c52-c29f84a71364 | -14.58264 | -48.26848 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a086999f-8d72-3d0a-a19b-11d399f0b9ba | -12.90336 | -47.10513 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 28de4ebb-a6e3-3f99-94e1-223cd7973bcb | -12.02633 | -48.347 | 2025-09-29 12:19:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 40436a68-d84e-3d48-b13b-5eef97e16efd | -15.55039 | -47.87026 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 28.2 |
| aebf5bce-7ab3-3063-b139-0f4d15cfb8dd | -10.81753 | -46.67253 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ae3b63d9-e035-3a1d-8243-ada512fbcb0d | -10.63204 | -48.54703 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fac701c7-a0e6-3746-90ca-639f3dcca74d | -13.18482 | -50.74422 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| d0b9cf2d-0881-39a0-9f51-5bb5d6205b82 | -13.17534 | -50.74273 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| aa577e7c-ce39-39b2-b65a-019055202ca0 | -10.38825 | -47.80821 | 2025-09-29 12:19:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8029297e-2583-396d-ae7c-e5d3c6e593fa | -11.44459 | -45.03528 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 33942451-9f1d-3d71-8539-c9a3731248a9 | -15.25981 | -48.75286 | 2025-09-29 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| af4535c6-82c3-313d-84bb-912c3ffc5c01 | -16.09894 | -46.03727 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 21686666-6042-31aa-b3b0-41daea55994a | -16.85288 | -45.80021 | 2025-09-29 12:19:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| cb16cc79-9eeb-30d4-b616-0750c2bd8004 | -15.87193 | -46.22123 | 2025-09-29 12:19:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4bf033a4-86e5-3db5-b2fe-6e2c06234681 | -19.56199 | -44.46677 | 2025-09-29 12:19:00 | TERRA_M-T | FORTUNA DE MINAS | MINAS GERAIS | Brasil | 3126406 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ad4bd4ca-0612-349e-8f1a-ec21b389d7b6 | -9.63399 | -48.12166 | 2025-09-29 12:19:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9c73c55e-a097-392a-830c-d190275bcf2c | -13.57707 | -47.29173 | 2025-09-29 12:19:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 77ea36ae-dd8d-3b67-af8a-0b0fae50d8b4 | -13.79858 | -47.94954 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a42b37c6-fad6-31c7-9a75-74eab9fd6981 | -13.22452 | -50.96263 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 5e2cacda-634f-38a0-8a37-8ea9c0b1ce9c | -15.90079 | -46.22532 | 2025-09-29 12:19:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| b6bbf8bb-cef7-36b1-af8b-83222f7cb92b | -10.45382 | -50.84935 | 2025-09-29 12:19:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a575ff8d-188a-3acb-88e7-ccd35c889038 | -11.429 | -44.91265 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 319dd62d-5e62-3ec4-b994-7147b95bae4d | -15.43869 | -48.20683 | 2025-09-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b68e1059-f8f1-391f-994c-6c44d3d9c8cf | -13.00156 | -49.43448 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| f8373048-898a-37c0-8480-13bcde1e6017 | -20.34812 | -44.86818 | 2025-09-29 12:19:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2d0feb41-7a78-360b-96c1-d18259a900bc | -10.82145 | -47.93837 | 2025-09-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e9e5ed0a-7a65-3efa-8545-645c0c77e84d | -11.90644 | -44.85539 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 2c89a8f2-4695-3d64-b368-143f8a610def | -17.09196 | -48.56249 | 2025-09-29 12:19:00 | TERRA_M-T | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 26e5b93d-58b9-35ca-a736-18248b4a68f3 | -10.91406 | -47.74787 | 2025-09-29 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fd3fedb6-eff4-3e9c-b955-e8f959104e4b | -11.91543 | -48.02508 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d9da76d6-3d65-3424-8aea-c120a40feffe | -9.77124 | -46.18625 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 649b1740-2c0d-393d-9dbe-fcc31aca8b91 | -15.46861 | -47.92801 | 2025-09-29 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cc4c7fb9-b703-35fc-a28d-beedb3fd99c4 | -12.86824 | -46.95991 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 69c94863-e708-3675-b211-2732bb22668c | -17.09193 | -50.34451 | 2025-09-29 12:19:00 | TERRA_M-T | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ebea23cc-4be3-3ee1-b1c7-b507a6a47ac8 | -14.51817 | -48.3918 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b4321472-426c-398d-995c-f67d428fb122 | -18.8671 | -47.34792 | 2025-09-29 12:19:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6ec6c9a9-3771-312c-8b07-2c61e067a3bb | -12.98275 | -46.26464 | 2025-09-29 12:19:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4a56cdc8-af84-3560-ba4c-1164b7ce2664 | -11.66733 | -45.36116 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ee4f1b79-b1c6-30e4-9d48-981b288c5475 | -15.29753 | -49.5026 | 2025-09-29 12:19:00 | TERRA_M-T | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| e3b583c1-c64f-3a6f-8944-c6fff3b5c469 | -9.88241 | -45.9168 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c424b060-84d0-35eb-afc0-911012250b34 | -10.68694 | -46.75127 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 4f1d03c1-0448-327f-b62b-0fb65f4bc727 | -9.72124 | -47.76925 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 60427b99-23b3-30dd-93c3-f8ee9798a0ed | -17.09065 | -48.57179 | 2025-09-29 12:19:00 | TERRA_M-T | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| e3ac83d1-f742-338b-8a7e-3707bc72eca8 | -9.99698 | -45.40568 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 51f53900-7e6e-346e-848b-1506212cd57a | -15.18928 | -48.4755 | 2025-09-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f8539f95-d97c-34a7-8cab-d644a02afa52 | -13.02043 | -49.434 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 3973e1b1-2b95-3ba3-aeb9-30a2e992f29c | -15.22886 | -50.09213 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e7698120-a6a3-339d-84e6-d34465b8dbdd | -11.92427 | -48.02636 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f0b87498-c805-37e3-8a5a-7afa9c79e9a3 | -15.28121 | -46.4123 | 2025-09-29 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b946bc1a-2ca7-364a-96e5-06fa406cb667 | -18.5476 | -44.93105 | 2025-09-29 12:19:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 457df4d1-de6d-35e1-8d5c-70a1c290c62d | -19.85099 | -44.30872 | 2025-09-29 12:19:00 | TERRA_M-T | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b0ec5632-91a8-316c-ba97-fd0ca2f99183 | -16.41939 | -47.02487 | 2025-09-29 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| efc0a643-b0c3-3fb8-ad7f-9755f3e4e795 | -11.55747 | -46.85101 | 2025-09-29 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |


[Clique aqui para ver as próximas entradas](README88.md)
