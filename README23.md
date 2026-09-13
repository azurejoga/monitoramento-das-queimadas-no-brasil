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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d61f46e-9a1c-308c-a1fe-c2dac52b319a | -2.64344 | -48.56839 | 2026-09-13 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efbc414f-d114-34b3-8929-34cbfd403dd2 | -6.8306 | -43.50721 | 2026-09-13 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3c68a31-9c58-3735-bbaf-13ecfcbd9dc6 | -7.38372 | -45.35622 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 749df65e-a085-3d13-96ac-fbd19faceda8 | -3.40846 | -48.88943 | 2026-09-13 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f95656d-75c4-313e-85a2-2df56fb5a3c5 | -5.12838 | -55.96456 | 2026-09-13 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 640ae5f6-2ab8-32e9-a9f2-ccdff8df4e5e | -7.01511 | -44.62487 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19a90f5e-cbd0-3fa7-9288-3e4412501bd5 | -2.96007 | -50.39528 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edfdb280-f4be-3bc6-b24a-5bf01f5bb10d | -6.68196 | -45.4832 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4890e7d1-9732-3513-a2c4-48e5cbcf8dc6 | -2.9641 | -50.40153 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a39c186-3e01-35b8-a773-df444f2d5282 | -6.72306 | -50.47358 | 2026-09-13 04:14:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| edd3c6d4-6234-34bb-b4f3-01055ba97a66 | -5.81601 | -53.80619 | 2026-09-13 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d768d52d-b536-3887-b516-8c938f72fd41 | -6.85988 | -43.88426 | 2026-09-13 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7443e0d6-29f7-36f7-a420-9674dc4f801c | -3.3356 | -42.2973 | 2026-09-13 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6ca7ebea-b799-3722-8847-da0e0e499881 | -6.08149 | -51.75479 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d79fc5c2-748a-3718-ac87-3bca55cd2736 | -1.94516 | -44.77774 | 2026-09-13 04:14:00 | NOAA-21 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d86e894e-490c-304a-a0c8-50bc5a6a2380 | -6.698 | -45.90788 | 2026-09-13 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a1e97d0-6e06-36a5-8143-edf7e7cc1d63 | -7.46498 | -46.14511 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed1db1f4-abbd-3751-b9be-d1678dc4d558 | -8.74629 | -46.43795 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34238855-85f9-3862-8868-949f46f134cd | -3.04333 | -51.25866 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff250385-93bd-3b88-bdc7-2c00dcbac8b5 | -7.76815 | -46.69344 | 2026-09-13 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e8cb0bf1-a661-31bb-ab71-e276094e3d69 | -20.84748 | -45.71381 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 077135fa-3b69-3a7b-b2a0-c18679182fa1 | -20.69127 | -47.52171 | 2026-09-13 04:17:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3fc8814-7ebe-32fb-8712-46ce8f1b1c3c | -19.20795 | -46.79746 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe567363-3330-386a-b04b-e564277ce305 | -20.84467 | -45.73257 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72ef1355-6ffa-35d9-a4e5-52d3cf42ad3a | -20.848 | -45.73312 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce509066-714b-36f5-b824-1db9004d9ee8 | -18.33474 | -51.9557 | 2026-09-13 04:17:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26307082-8424-3da6-91d9-1fe20bfac6cd | -20.85189 | -45.72996 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c4e1c46-e236-355d-930d-48b76e31387d | -20.83192 | -45.72649 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4144e43c-8abc-3939-b193-2e348cf9e613 | -18.99255 | -46.95137 | 2026-09-13 04:17:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf317dee-fe45-38d4-b790-63471854dfed | -18.33855 | -51.95318 | 2026-09-13 04:17:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5d4aca3-c587-3d56-9410-1396467e4cd2 | -22.36006 | -46.97554 | 2026-09-13 04:17:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 549b8f0c-9f7d-3fb1-bd36-555426c30212 | -20.84416 | -45.71318 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3265cf32-1126-373a-b774-fddb04eee8d5 | -18.33963 | -51.95276 | 2026-09-13 04:17:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1f6be06-6642-3cd3-a515-6bdd6cdee518 | -20.82747 | -45.73337 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9364bc50-6caa-3a9a-9a90-70390c33fc4d | -19.20522 | -46.79321 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fb7e441-6cb9-3245-b318-a29ef389092a | -20.37739 | -40.59631 | 2026-09-13 04:17:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 801c506c-63fa-3de2-a93b-7fe5cf780bd9 | -19.20853 | -46.7938 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84a881b9-44b5-36ee-a50d-e80ff4e0dae5 | -21.09887 | -49.21925 | 2026-09-13 04:17:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 91cb5a09-6f48-3117-be56-1be37e5c69bc | -20.04533 | -45.19754 | 2026-09-13 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b17d41ae-7d05-3a21-a389-137bd48d33c9 | -20.8247 | -45.72902 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f48e4e8d-8123-3b7e-8de3-ab7b902cdec7 | -20.82414 | -45.73276 | 2026-09-13 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c9c4756-c55f-383d-a403-15951ef28415 | -20.04588 | -45.19379 | 2026-09-13 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a295ba2d-fb27-34b9-83e8-d00e8a1e843b | -19.87833 | -44.05309 | 2026-09-13 04:17:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7a47de14-78b0-36f3-aa7f-afd5fffe738d | -18.33548 | -51.95181 | 2026-09-13 04:17:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5db9e76e-6b45-3130-adc1-e08910185aec | -12.12162 | -48.97989 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53704304-10a4-3f1c-be2c-746b5ddaffbc | -10.30936 | -45.28588 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2d9c678-e37b-38e6-a2a6-f797b0402c93 | -11.19746 | -42.78184 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d2fa5993-6a9a-3738-8bfa-446afd66d13e | -10.69514 | -54.16036 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5bf5779f-839d-3713-8f7a-ae983e8da05a | -10.30715 | -45.2782 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7bfa47c-c118-3abb-a633-98a27d227317 | -8.5337 | -54.71507 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0d46a4de-59ca-32ab-8909-32cf48b8e01c | -13.32168 | -51.3174 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 967f0e6e-7bf1-3028-b483-8e5e2ea3aa39 | -9.5509 | -45.44761 | 2026-09-13 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4b97a357-c067-3a0e-98ec-2a82275d99eb | -13.29764 | -51.64319 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e6e4601-991f-3d6b-b653-4485e21cf92d | -8.54641 | -54.71277 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 839b5f31-5cee-31b5-bf8a-dad48493066e | -11.81225 | -46.38678 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e65b496-b6bf-3702-8158-0445dfcf1ff1 | -13.99037 | -54.07507 | 2026-09-13 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f7878ab-164c-3dc7-a4df-de6868f430ed | -8.03342 | -54.85397 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6689eceb-970b-30cb-b896-a9cc06169da2 | -13.34756 | -51.77597 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 223f61b2-aad4-3b10-b676-36371cbaaf53 | -11.04364 | -47.16987 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d09fb27-8ecc-3e24-b53c-454f441817f7 | -8.11847 | -54.79845 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19deecc8-c1ea-3bf9-b985-1dc51d1cb566 | -10.35862 | -46.67882 | 2026-09-13 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c50a4d8-be0e-3d64-a2eb-6ae3b37fca29 | -12.85783 | -44.39172 | 2026-09-13 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f2d595b0-c98d-370f-a15c-52fea0931731 | -10.54018 | -45.22504 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24565093-3f8c-3eaa-98fb-91ee67c73c60 | -13.61937 | -47.88239 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39ee97c3-3921-355f-94ad-82719385e797 | -13.61586 | -47.88157 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0086fcb4-b8cf-30fe-9bb4-6fe51d620aa2 | -14.91524 | -44.67328 | 2026-09-13 04:17:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59fcb7fd-be6e-31ae-bb64-9ca7885fb4d8 | -10.35927 | -46.67488 | 2026-09-13 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d75ebc3-d9de-309e-9a9c-8f925c07f32c | -10.68127 | -54.17318 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b9a0c946-aa2f-37cc-9916-b4d224031317 | -11.36689 | -46.90967 | 2026-09-13 04:17:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 505099d9-5118-3495-8391-19027899ce36 | -9.71056 | -48.1147 | 2026-09-13 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 317fd7b2-6d82-3414-bd99-ef765c45932f | -10.69032 | -54.1556 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e4f0c4dd-388d-3b4e-8b11-532017a8c138 | -11.83152 | -46.39745 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b39fdc01-a1d8-3d4c-9b27-7197f70ca725 | -11.80883 | -46.38627 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 142f0d63-1ed3-34f6-95cc-3374da7684f5 | -10.46067 | -48.64244 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32663d1e-4c85-3315-99c9-88cd729aa337 | -8.54722 | -54.70842 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b56a55d-7750-3379-a2be-e56695bf485d | -9.59225 | -55.14602 | 2026-09-13 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 934065c0-8221-3d47-bebe-b44c89fab545 | -12.85729 | -44.39524 | 2026-09-13 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5acce256-5c7c-3d2c-9ac6-875a2b34c4a9 | -8.31765 | -49.68676 | 2026-09-13 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea7443e3-d27d-3b8a-97d7-b81a615ab7ab | -10.68963 | -54.15927 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4a10ae64-cd04-3216-8852-b10b513ada45 | -13.15049 | -48.5841 | 2026-09-13 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4108dfa-3d8c-39a2-bd8b-9a8e98e376f2 | -9.41317 | -50.13505 | 2026-09-13 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2fff7b4-3132-34cb-915b-8cc7b17ca4aa | -13.39094 | -48.00835 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3dca086-0b73-3f81-a763-967ea94bd459 | -12.1588 | -48.97104 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 905a5178-bd8b-398e-ab3d-c85fc1d40d46 | -10.51426 | -51.34538 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cffa7e46-520c-3013-800c-b91bdd10041a | -10.63574 | -46.1027 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e1e1924-6b4a-3333-8c58-51dcbef05e22 | -11.24811 | -54.15688 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6304d919-81d5-3cdb-8d4f-ad63acf40136 | -13.61512 | -47.88588 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 872127e3-fedb-3d45-a0ed-aec128b14c2f | -15.91841 | -42.55547 | 2026-09-13 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be3fbad7-37d3-3261-a6ba-7f02e8fff536 | -11.43067 | -45.14423 | 2026-09-13 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3449e255-6df3-3a10-a7af-760c3511ac66 | -13.30651 | -51.72054 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3aaa92a-d1a3-3726-8fc0-f8a3b25f8d1d | -14.10817 | -46.35847 | 2026-09-13 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c49331d7-bfb8-3dcf-94b8-7327829a9212 | -9.55227 | -51.36417 | 2026-09-13 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 276e84f6-302e-3679-a56d-f08feeae0072 | -16.78524 | -43.86372 | 2026-09-13 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f373d06c-9f44-3d21-9798-c768337541d8 | -13.40261 | -57.03271 | 2026-09-13 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 298770d9-08d7-39ae-82dc-2692720bb196 | -11.04719 | -47.17046 | 2026-09-13 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb9d4e54-591d-35e9-93c3-185ee24f33a7 | -9.54477 | -45.44279 | 2026-09-13 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a87d4bcc-6f71-31d7-bd48-ff00933b666a | -11.83895 | -46.39481 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 006c9b64-808f-3e73-9a73-3ae569c88aa8 | -13.61789 | -47.89108 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91562016-52dc-33a7-8c84-30cbcf528677 | -9.69801 | -54.3517 | 2026-09-13 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6015a343-a3e9-32cd-86ee-71568fa11509 | -10.30879 | -45.28946 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README24.md)
