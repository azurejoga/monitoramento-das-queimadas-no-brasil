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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76e2a0a3-aebe-3813-958b-95ee622c8843 | -11.33187 | -45.03012 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 946fab0e-99be-3869-8f9e-ea6d78fc62bb | -11.33132 | -45.03473 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca7ba808-d670-3d6b-b2a8-1d006d53f68d | -13.69708 | -46.11852 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ffba80d-3f47-3058-8ee5-b09cce545fc9 | -13.69656 | -46.1232 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ae7e6a5-e4be-3129-befc-ae51948067d1 | -13.691 | -46.11767 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 338178c9-71f1-3f03-924d-84b09e99fd38 | -13.69048 | -46.12243 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 393ae714-640f-3d6a-9694-423564bca3b9 | -13.68995 | -46.12722 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8a9209f-3ff6-347a-a21d-f730af5024cd | -13.68942 | -46.13203 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37b279c8-bed3-3fd5-beec-1cd7cd563f52 | -13.68889 | -46.13683 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d079e25e-1377-3938-9147-00aed3040ba8 | -13.68491 | -46.11703 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38320a47-8510-36be-84dc-b83a5dad2636 | -13.68488 | -46.116 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d55d495-a9a7-3743-8d6c-4c534720c777 | -13.68433 | -46.12077 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 748f886b-ba31-3cd7-94d0-1c42b7278f19 | -13.60912 | -45.58359 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c1b4d06-f4fb-337b-a483-70384611601c | -13.60692 | -45.57887 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10302300-3d4b-30d3-9ede-4132e69f9918 | -13.60638 | -45.58398 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a43bfe9b-b1e6-3448-a698-00ab7c458ef8 | -13.6053 | -45.59416 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff7da3dc-69d8-3dad-b80d-05c97ae2c094 | -13.59902 | -45.59335 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d670b89-9252-3f98-adc1-896da5f71127 | -13.36776 | -45.10598 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ee94a11-10c2-35bf-88d3-121f1c64860b | -13.36765 | -45.10634 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70784c3d-af9e-39d7-881f-f81679c3d8ed | -13.36715 | -45.11138 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 792d1d05-57c0-3859-a4b2-505e9317bca0 | -13.36707 | -45.11175 | 2024-10-29 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7c98bce-33f7-3e69-be2c-3f76fec453ea | -7.57266 | -46.44593 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fbd912c-a4a4-3c9f-aba4-5d9d5183a242 | -7.25921 | -46.076 | 2024-10-29 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a7ceb0b-8ce9-3ca1-8bbf-087692ae1ac8 | -7.25359 | -46.07528 | 2024-10-29 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05556ed7-3092-3bd3-b34f-302bdd9f21b0 | -7.2531 | -46.07893 | 2024-10-29 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1203643c-a9c0-304c-88ac-8b8748cf53f3 | -7.18024 | -46.32679 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 75419b7a-0f52-3419-a390-078af766c41c | -7.18001 | -46.32756 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1670194e-db51-3da1-b579-4a8c19fd647e | -7.17481 | -46.3254 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a2e9e8f-6f59-3b0a-ad03-d77c22da453f | -7.17458 | -46.32619 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f9c5f85-a8d5-3a5c-939c-237fdbd59f55 | -7.17434 | -46.329 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c993837b-a877-3668-91a9-066736ec710f | -7.17408 | -46.32977 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fc2f3cf-a344-3a58-99e2-7582448b110d | -6.94739 | -46.10444 | 2024-10-29 05:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 079e48e8-fad1-3ee8-9c9f-f5bd04365c58 | -6.94688 | -46.10811 | 2024-10-29 05:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc733c9c-d357-3327-8ebc-af50d29d46e7 | -6.87393 | -45.91017 | 2024-10-29 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 653fb2e8-fb64-3806-b337-bb40e0974eb4 | -6.86823 | -45.9098 | 2024-10-29 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ce968de-478c-3cb8-8b03-166a2736f9ac | -6.6628 | -46.38295 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e81a72e4-f4b0-3fac-950d-48859b0e0710 | -6.65737 | -46.38209 | 2024-10-29 05:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9d40713-321d-3cac-b664-e8159ccc29f1 | -7.60964 | -46.87133 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94bf8d88-76fb-3a43-a41d-d040f4e9150f | -7.60918 | -46.87466 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4877b4c8-ef3c-36f9-93cd-985f663e052c | -7.60384 | -46.87394 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 640a8c51-e042-3568-a66e-15abb6f573e3 | -7.60337 | -46.8773 | 2024-10-29 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbe66cd0-e15a-3c56-b1ee-6747b0bdff16 | -9.70208 | -46.23966 | 2024-10-29 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc818169-564c-3d52-b894-c9446a072ce3 | -9.70155 | -46.24378 | 2024-10-29 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2657b296-d258-3cae-b639-71695f8da532 | -9.70103 | -46.24782 | 2024-10-29 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad4160b4-2747-3e23-8841-4c753dcf65e5 | -9.70052 | -46.25181 | 2024-10-29 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fa0a98c-bea1-3d1d-a58c-763c8b2494c9 | -11.9964 | -47.16551 | 2024-10-29 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdc3b65d-30f2-3988-8deb-d7045e8f6ab3 | -11.99594 | -47.16929 | 2024-10-29 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30a903cf-251b-3222-8418-3a8e9ecbdef6 | -11.69013 | -47.11299 | 2024-10-29 05:04:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec5043e1-d533-37b0-97b9-cc8feeb462ad | -12.64199 | -47.54785 | 2024-10-29 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bbf4392-0e4b-367d-9a55-9bfb8e4e6bbc | -12.63651 | -47.5472 | 2024-10-29 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 913f3371-2c4c-3fda-b064-2e9cf0954ae2 | -12.63059 | -47.55013 | 2024-10-29 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dd5d197-3150-3b81-865d-ebb6b4e0a5f8 | -6.51384 | -47.04147 | 2024-10-29 05:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81bb9d6b-c95e-3194-a9a1-28bd73434be5 | -6.51341 | -47.04454 | 2024-10-29 05:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5912bb2a-4f9d-3eca-b8c3-7c8e563a47d2 | -6.51298 | -47.0476 | 2024-10-29 05:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ae44bbae-e7f6-3970-a890-9592fa1c7010 | -6.50865 | -47.04069 | 2024-10-29 05:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ece0e18a-cecd-335b-8b71-a0793421abfd | -6.50822 | -47.04374 | 2024-10-29 05:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dd37457b-9828-3ba9-9e9d-3f0abe5538be | -6.50779 | -47.0468 | 2024-10-29 05:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b8f583c4-f705-31b4-a688-1d5a52cf7917 | -6.42189 | -47.2856 | 2024-10-29 05:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9aa3b009-0e01-3404-86ba-87a35b120920 | -6.42147 | -47.28862 | 2024-10-29 05:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffc67bbe-0369-33b1-b5ef-6c3cac71df3b | -6.29367 | -47.34206 | 2024-10-29 05:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c89830e8-0cfe-3f8a-9f3f-b9f30c59627a | -6.29323 | -47.34504 | 2024-10-29 05:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6552f8e7-438d-319b-b9b8-9a020123be2a | -6.98808 | -47.08173 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 707bbea6-79fa-37a1-adb5-af95fbcf7c11 | -6.98765 | -47.08489 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a3d0582-6924-35c9-9c93-ccda7aaa2c6c | -6.98722 | -47.08805 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80658b80-9c2d-3c54-9a2e-a344b2d1bb1f | -6.98286 | -47.081 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0d3121c-d7d0-3282-aba7-0c7677fb3497 | -6.98243 | -47.08415 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4699938-f601-388c-a2b1-1e02ef5d9add | -6.63133 | -47.35249 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 78033a6d-8bb9-3b73-a041-21d411f9e4f7 | -6.63093 | -47.35541 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40f55eb8-79b6-387e-9e7e-09abb462f3e1 | -6.60727 | -47.38903 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7827d16c-1a90-3d5e-be1f-7c1436ace711 | -6.60684 | -47.39202 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 04b4cf64-4f11-3655-9414-97519ce97c5f | -6.60641 | -47.395 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0902d06e-e7ba-3a93-bb87-e0460bee73cc | -6.60572 | -47.38778 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 63e6729e-a199-376d-b67c-94f03bc6adf5 | -6.60531 | -47.39077 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 32404c04-7f55-3b39-b675-4ffac0ae5084 | -6.6049 | -47.39378 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2ba20245-6881-34be-b0c1-7d672e374c1e | -6.60449 | -47.39675 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ba1ba5a3-2d82-3d23-8291-b6a406c7ec86 | -6.6022 | -47.38827 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e0f45e1-0b78-3806-b2e6-d56ccba9228c | -6.60176 | -47.3913 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7b8b4347-5435-3cb6-982e-5f3bdd7d1aeb | -6.60132 | -47.39434 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0aaa6096-afaa-3a48-bf7c-2ad64d0392fa | -6.60022 | -47.39009 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f5092681-9b81-3e77-acc4-5eb0d51ba34f | -6.5998 | -47.39315 | 2024-10-29 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| afff409f-77c5-3616-a2bc-99c4e4493566 | -9.10634 | -47.65413 | 2024-10-29 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 067ce445-0f1a-3867-9b1c-c2c96ebcc982 | -9.10593 | -47.6572 | 2024-10-29 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b68f12d-fc17-3794-9b46-6e44f02fb978 | -8.66625 | -47.86502 | 2024-10-29 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2629270-e901-3002-8997-c6b7ea15b2ee | -8.66584 | -47.868 | 2024-10-29 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74a489f6-0cd8-3930-9d69-a9d9542b9f68 | -8.47088 | -47.80817 | 2024-10-29 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50ce79f4-1d38-3e91-9d58-eb04928040a1 | -8.47045 | -47.8112 | 2024-10-29 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0704986e-2c27-3f8e-8dc0-a6d62841f9f3 | -8.46912 | -47.80991 | 2024-10-29 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c2841e7-6901-3b7f-a43d-b7e0fc3e1fe8 | -8.46872 | -47.81294 | 2024-10-29 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36a31f79-06dc-3ded-bd36-db839f99a653 | -8.46539 | -47.81042 | 2024-10-29 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b636e660-3800-3110-b7c0-86fd05e8aa43 | -10.44667 | -49.04393 | 2024-10-29 05:04:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5ce5fee-8309-31b8-8803-8b5701032b44 | -10.44645 | -49.04788 | 2024-10-29 05:04:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 999fbd8d-3092-3a55-b4d5-88b1e21361dd | -10.44597 | -49.04931 | 2024-10-29 05:04:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 27cd1552-6d46-31de-897d-c138fc39731c | -10.44165 | -49.04721 | 2024-10-29 05:04:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ae18f80-6a24-3007-a84e-af7cb741568d | -11.96705 | -48.09139 | 2024-10-29 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f9787d4-305d-397a-b0a7-d01309bf5de7 | -11.96665 | -48.09465 | 2024-10-29 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f33b9210-1654-38e3-baf6-c212c45e6969 | -11.8239 | -48.7554 | 2024-10-29 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7725d0da-451a-3927-a738-a7011c3b05c8 | -11.82316 | -48.76119 | 2024-10-29 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 116eee4b-de6b-3913-b4c7-f7c7dd59a073 | -11.72651 | -48.35767 | 2024-10-29 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1dcffee4-7bab-3366-b027-bcbf07facb89 | -11.72613 | -48.36069 | 2024-10-29 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75e71b13-e7a2-35e7-8ed2-a9b24316fab0 | -11.72139 | -48.35696 | 2024-10-29 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README92.md)
