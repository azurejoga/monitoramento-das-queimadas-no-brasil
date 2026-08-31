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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18acb7d1-a1fd-30d2-bdf9-89838845272a | -12.39777 | -46.45335 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f84a6389-61ee-3573-826d-ccd72cb1cd2c | -11.68952 | -47.60379 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 497e10be-0caa-335a-856c-d72f70fc4ec9 | -8.18271 | -48.80863 | 2026-08-31 04:14:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 146c5032-9740-3859-be0b-361fc05a92bb | -6.86058 | -41.65844 | 2026-08-31 04:14:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f661cde9-8292-36bd-8373-5b1517a68c52 | -10.75675 | -44.86557 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3b51b8d-795a-3a60-9aa4-e12996d635e9 | -11.20966 | -43.38523 | 2026-08-31 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| db770190-f14a-3f29-ae2b-79b1a7b6d87e | -6.91538 | -55.72242 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d134fe60-b255-318c-8986-3a66e0857ae9 | -11.49654 | -46.9339 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98d4bd76-b8b8-3390-98ce-acad5019bfeb | -10.79971 | -50.65637 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d8202ed6-c1f5-317a-8ad9-8d497b442d58 | -10.83891 | -45.32604 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ed91f33-ef86-34ea-af0e-4343ddfc9a27 | -11.21453 | -45.115 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff40c7c5-a15b-39d6-962d-b64a2e90f398 | -11.37064 | -45.16343 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ca3f346-4b5e-3afb-8ede-509225cd7cf0 | -9.00387 | -39.88427 | 2026-08-31 04:14:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4e9e15eb-2ee4-3110-b928-e9e0f17d3874 | -5.45201 | -42.65093 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b3f5ad15-9c70-3c0b-9b72-e65a7e54e3e9 | -7.9117 | -44.28543 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3434feb5-f7f2-336c-83e3-81c86be887f5 | -11.19768 | -45.04474 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bb890d1-df47-3932-89ba-95b3ec3d8789 | -9.58313 | -47.61038 | 2026-08-31 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35798317-2935-345b-9c88-34a4c4904e6d | -10.05242 | -48.68533 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ca0d7e2-7b01-3a55-961a-ff814bd72171 | -7.14651 | -46.17188 | 2026-08-31 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7c449ab-dcad-3b88-8307-809f0552c570 | -10.74152 | -50.64513 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e56a473f-92eb-35c2-b43c-f74cd716375c | -7.2112 | -42.74414 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c7581e44-3564-3ca1-b5dc-49eb43f6eb7d | -7.04958 | -42.20301 | 2026-08-31 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c17d5e6d-1049-389b-a360-124078e055e7 | -10.73667 | -50.64419 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc4d64ed-5c94-353f-b932-563895fed81d | -10.07104 | -48.70602 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87d1f305-63f8-3514-936b-cc2d01e60c34 | -7.40941 | -44.24961 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d139b7af-dd05-3619-8914-c0ecba9b3216 | -8.23076 | -49.0472 | 2026-08-31 04:14:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7d028f7-72a3-3ea9-aebf-12febaaa1912 | -11.19732 | -45.06842 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e9fb34c-633e-36b2-a90e-2e5cc9db3434 | -11.35053 | -45.21959 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f62a1e37-36f0-393b-9ba7-513f8e6c327b | -12.09459 | -45.05463 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef133da3-9bb6-3d47-96c4-a2d28975323b | -7.97574 | -44.28459 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1272940d-f80a-30a2-a8b1-92500de72f45 | -7.52426 | -55.32418 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 702faac2-ba26-35a9-97f0-2d26d65cda17 | -12.13601 | -47.25848 | 2026-08-31 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7b00904c-2b43-3bca-8a84-704e1bd405a2 | -6.86378 | -43.87563 | 2026-08-31 04:14:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b30106cd-d077-3e7b-a11e-47aaa0fa60b1 | -11.34681 | -45.19917 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dcf9202-46d0-355a-aad2-d29e5a09fcdb | -11.27218 | -45.31553 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bacb2d2-fbac-3e7a-b3df-d4138260ec68 | -11.47791 | -45.06583 | 2026-08-31 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1588969-7e5f-3de4-a699-42fa20824e5d | -11.22276 | -45.10829 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1857bf0d-af25-3d41-8087-6accf017a83d | -12.10051 | -45.0401 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13ac6875-7216-36ac-a870-2fa4a43104a3 | -11.32954 | -45.18486 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 098039c0-435f-3a99-914c-f7c3bbc96b01 | -7.28481 | -49.84526 | 2026-08-31 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61257823-0435-338a-8210-5a416e565b31 | -7.12774 | -42.82059 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4d2e1d2-0d05-3063-8fe5-acd0815317fb | -6.39475 | -45.50312 | 2026-08-31 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01a8e842-4324-3e65-9afb-7508e8885279 | -8.15289 | -45.4702 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cce49476-7fe7-3a8c-ad97-da8308c5689b | -11.62583 | -46.72739 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72997d8b-627d-3d73-ac57-f09c81ee0e40 | -11.91772 | -45.06017 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d983c7cb-d050-3fa6-a783-ebc32f3af102 | -9.96427 | -46.31074 | 2026-08-31 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae117211-ed71-37f3-af48-5aab0cf5c233 | -7.22227 | -42.76032 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5edcb0bc-0da9-3564-87f0-a82abe666ed5 | -8.12953 | -45.49759 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb1fbd89-501e-3ff0-9d3d-ad0e57009260 | -10.82242 | -45.36017 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3119ffa6-bd3c-3ba9-82e6-c6fdf3594803 | -9.43422 | -45.67887 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5e31f7a-26f3-322b-8c74-083ecc79af18 | -10.83322 | -45.3169 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8dfb1456-8990-3955-924d-2d5f2de04ea4 | -11.22119 | -45.0962 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 203e693e-4aa6-3d61-9579-50bf43108478 | -10.75138 | -44.87653 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f137a23-9d1d-37a2-a5ab-5b364c55e3a0 | -11.37679 | -45.21204 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 171917a8-8461-3abf-a8b9-7f273f981d21 | -6.33675 | -38.93232 | 2026-08-31 04:14:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28f83164-dae7-3ced-a664-b7ee18c1c464 | -11.33358 | -45.19297 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 929c4a4d-b399-34c4-a6fc-06465247da95 | -11.34642 | -45.22282 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56052bbe-e7de-36df-9ffe-d1a883d0279d | -11.87553 | -45.82987 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0142006-cd2c-3a98-b7e4-d58d02211415 | -11.3741 | -45.16401 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92f124f5-d7b5-3a65-9d78-79bd9e4ffeb4 | -10.05891 | -48.69904 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cbbbadf-b3dd-31e6-a4b2-a3c6260d88da | -9.43712 | -45.68376 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a1e52ba3-97fc-3e64-a2d7-04646b8ccdad | -11.33459 | -45.19757 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78fac65d-4c24-3432-8daf-92e019888e96 | -12.43107 | -42.88144 | 2026-08-31 04:14:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 355a058e-d834-3773-b6d6-709fa4c769b5 | -10.79486 | -50.65543 | 2026-08-31 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 71e0694e-81d4-34c3-bbd8-c8285cbbc5ac | -7.28646 | -52.54152 | 2026-08-31 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a97e74e-c684-3b9c-b980-6954d61e0f29 | -7.14508 | -46.16887 | 2026-08-31 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2951f4a7-2aec-3258-aecb-d3360666bd27 | -7.97636 | -44.28074 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fb8fea9-1d20-3605-a589-3cd691fd6ff3 | -8.23531 | -49.04803 | 2026-08-31 04:14:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 319e19f9-7db9-318b-ac9e-2de50cf097ba | -11.49276 | -46.93328 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9cd467e-1c76-3b30-8c2e-fc296cc641b6 | -11.8811 | -45.81828 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3a0cdfa7-6370-3836-86bc-1b59bfbb6426 | -7.79097 | -43.95316 | 2026-08-31 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77a23700-7b4c-3642-98ad-353504f3e45c | -6.92123 | -55.73033 | 2026-08-31 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 03d4c530-3649-32ba-bfd1-471a2e0c5d6c | -7.63052 | -44.84497 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb89fa78-704b-38e1-8fb0-6291dd1bb2b6 | -10.74577 | -44.86768 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a386e792-091d-3bcb-af3b-b618154b33b9 | -11.68866 | -47.60881 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37c3bc07-0868-3828-8c78-28b7b48827a7 | -9.43784 | -45.67953 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 39982ec6-bb53-31a2-90fa-dbf72602cf7c | -7.97858 | -44.28896 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e58829e-7eb2-3129-a352-f1493df6173e | -11.33947 | -45.15798 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a36f97d9-07bb-32bf-ad12-e50e121a0225 | -10.07322 | -48.7045 | 2026-08-31 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14d26a09-33e9-3049-8d6c-81235ecc9342 | -11.68478 | -47.60791 | 2026-08-31 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e09aa1a4-7291-36cd-ac9d-6397cc7e3b37 | -11.22339 | -45.10444 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36276581-7690-3989-845d-8c394be2148f | -7.61673 | -44.88412 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 083cfe9a-e863-3e19-9f7a-8289b9ec24b0 | -7.08493 | -43.61358 | 2026-08-31 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c3131ce-ccaa-3f8c-aaad-c652466e8cb2 | -11.33749 | -45.1581 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c099674e-1c06-399e-85a8-0afa014ac066 | -10.83104 | -45.30839 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a093110b-4a73-33b6-ae3f-ff8119f04874 | -12.39268 | -46.46131 | 2026-08-31 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc4cb373-ba71-3153-981b-eb37392c928f | -11.34835 | -45.21131 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| efd3814d-01eb-344c-b328-63557f9ea3d5 | -7.1028 | -42.7841 | 2026-08-31 04:14:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 930aa19a-8c57-3743-885f-3839f0300212 | -9.43926 | -45.67107 | 2026-08-31 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ced26c7f-4fc3-357a-83bb-11c321819df3 | -11.21982 | -45.1479 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6ec3bad-7099-30c9-b346-09624e7fe944 | -11.61005 | -46.72213 | 2026-08-31 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c253f65-b641-3b6f-9fcd-d18b4a9e2d38 | -10.85205 | -45.37753 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03769058-a289-3823-a2f2-a87fc3c31a2e | -10.1478 | -45.69087 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f0715bc-daaa-39c9-8b72-53ba14ddf0bf | -8.13005 | -45.49496 | 2026-08-31 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6add30a2-8307-3cee-99c9-a199ddc43d05 | -5.45985 | -42.64492 | 2026-08-31 04:14:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ed0b96e-cb60-3972-a807-f83209ee7858 | -11.93274 | -45.05487 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e4a45d6-7d69-3955-83ec-76df46b97edc | -7.78364 | -44.06322 | 2026-08-31 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1de75847-7314-322f-a2dd-1f0f7fe6112b | -11.92274 | -45.07245 | 2026-08-31 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf9817e7-bff1-3ed7-a2a7-598067ca50ba | -11.23822 | -45.1335 | 2026-08-31 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 470edbe3-7a9d-30d1-b337-ad85100d15da | -7.93056 | -44.30032 | 2026-08-31 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
