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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0858610b-02e7-30a2-9f00-0d66e0ed4b08 | -5.86343 | -45.28154 | 2025-09-25 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fba7847-2e2f-354c-9dd3-80e8d6eb300e | -5.53459 | -43.87519 | 2025-09-25 04:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cc7f0cf-8ea7-3c6a-a631-762dc4289f48 | -5.63407 | -45.7271 | 2025-09-25 04:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a51b168e-5ff5-38e1-99cc-922ff89c2f90 | -6.25625 | -46.1107 | 2025-09-25 04:59:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 732b4f00-4d4b-37c8-be77-7d8c284a460b | -2.44655 | -57.9464 | 2025-09-25 04:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e6354c8-be29-39c2-a067-960e092ce937 | -7.32084 | -45.76244 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e8cd4f5-d994-3cc2-b62f-89b381d3131f | -4.5707 | -48.02273 | 2025-09-25 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c33dc0a6-2a0e-39ce-a0ca-3428e0043c9b | -4.34889 | -50.50454 | 2025-09-25 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f0cc381-c244-390e-9745-654491b81962 | -5.96167 | -42.90303 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6cb4dab6-bb4f-3523-a113-4afea65c5991 | -6.07906 | -44.08007 | 2025-09-25 04:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcf30f50-3fa6-3b21-b907-10b70f7a21bc | -6.59063 | -44.62463 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e660eefa-9f1e-3548-b40c-26241ecae057 | -6.94742 | -44.63871 | 2025-09-25 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| accdb0e2-595e-3f8e-b3e4-8600424d61c5 | -3.80309 | -47.58575 | 2025-09-25 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9d395b6-65a2-3352-ae97-e1dadec31dcd | -6.69347 | -44.61822 | 2025-09-25 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d026fd13-5932-3cf9-98eb-b1a892d9f317 | -5.93316 | -42.92775 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 925f9418-abfa-32c8-964c-0006d5aeb670 | -6.54903 | -43.83802 | 2025-09-25 04:59:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b3603ca-c44f-3b8d-b3fb-1da7034775fc | -1.15194 | -54.22109 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67376152-1e02-3d44-bf7c-f9a1b1db23d5 | -4.73624 | -44.42934 | 2025-09-25 04:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47701e29-f445-37ca-8216-14ca78323fa2 | -5.06069 | -44.32072 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ef9d5f7-fb7a-32bf-aa45-286815fca573 | -2.69157 | -48.47382 | 2025-09-25 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8988d96-a02c-3e9e-a673-d852e66c17e0 | -1.94783 | -52.08466 | 2025-09-25 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a08c9147-727c-3916-a7fb-ab84b50ef053 | -7.10302 | -44.09567 | 2025-09-25 04:59:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1eefa5d-a73b-384e-b300-7ce5d83c9b31 | -5.5186 | -43.8641 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f75bec0a-ed3a-3674-92ea-227f6b3013af | -1.79852 | -55.59003 | 2025-09-25 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cc3d990-1669-3363-b7c4-785dae5b545d | -3.43858 | -44.4795 | 2025-09-25 04:59:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c6960c4-868c-35d7-ae08-ea95f28b84c4 | -6.82531 | -43.1841 | 2025-09-25 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51d52ee9-d660-35ac-8915-96eab6459a50 | -4.21446 | -53.52422 | 2025-09-25 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16df5690-8598-32dd-9305-b26879361ecb | -4.7973 | -43.54506 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1def2078-6bbe-307d-9b07-95a0250dc5d9 | -2.35838 | -48.89307 | 2025-09-25 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e18e549-486c-3384-b252-bd4384e418d2 | -2.06558 | -47.8227 | 2025-09-25 04:59:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e13f026-e76b-3d07-97e8-cb254941f87d | -3.83194 | -50.97405 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69a651da-0eed-390c-b68b-01de07514908 | -6.13559 | -43.45115 | 2025-09-25 04:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ea3c019-58d6-3422-b248-145bfd67e817 | -5.52887 | -43.87418 | 2025-09-25 04:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 41483d28-54db-377f-8425-178a718f6257 | -2.30304 | -48.14699 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be422584-39b5-309f-b73d-d8d12fb987fb | -5.06023 | -44.3197 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7149f96f-6dd7-3dfa-9292-f5712fdd2a80 | -5.63491 | -45.72117 | 2025-09-25 04:59:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6107429a-86ca-3846-894e-b0166c8ebabb | -3.61852 | -51.79628 | 2025-09-25 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02753194-d568-3cfb-886d-3fc8db5c35cc | -3.01507 | -51.35588 | 2025-09-25 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bbe74a0-59bd-35bb-9004-24e8cc74f536 | -4.4283 | -47.26525 | 2025-09-25 04:59:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80bcb063-305d-32a1-9304-a6490e1880fa | -3.21042 | -54.95931 | 2025-09-25 04:59:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9f73c7b-3477-349b-92a5-c189bd3a9249 | -6.565 | -42.06852 | 2025-09-25 04:59:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7fb4ce03-cdd2-35ea-bb25-d6764e6a0131 | -7.25836 | -44.90134 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4be68e0f-fef4-3996-8737-9021465bd4b9 | -5.78803 | -42.81035 | 2025-09-25 04:59:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 34b3dd77-47c5-3962-b3ca-71ccc57eea2d | -3.15595 | -49.47421 | 2025-09-25 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7b5bbaf-38eb-39e7-98cd-a3a257ccaa0a | -6.11939 | -44.00046 | 2025-09-25 04:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 226385ae-9051-3fa9-8f58-806282bdb41f | -7.26335 | -44.90579 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 268eb1e5-743e-3c43-a54d-e89586a9cb91 | -3.84323 | -50.99168 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb96b549-a666-373b-bef7-43fcca68001a | -5.22987 | -43.69506 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89c7fbcc-aefc-3465-90af-d06bf0583b1d | -6.0734 | -44.07883 | 2025-09-25 04:59:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c080c58f-4669-329d-82ab-1e269d3998bd | -1.08692 | -54.10934 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4df5f26e-8799-3250-9f91-5a9bd9f37589 | -5.53024 | -43.873 | 2025-09-25 04:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 91958110-a811-3eb1-bc37-9ce0f3804965 | -7.26321 | -43.02152 | 2025-09-25 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 845e6d83-ece7-35b0-8258-d3e376c6e925 | -1.08748 | -54.10582 | 2025-09-25 04:59:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 781013df-cc51-38b6-bfda-ad3079e709c3 | -7.04854 | -46.40794 | 2025-09-25 04:59:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc48ab74-936b-3743-a39b-b9c7226c5877 | -4.67085 | -48.15649 | 2025-09-25 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 908f04f3-e098-3eb3-a346-f54f37e23337 | -2.92131 | -48.30268 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8babc0e4-289c-3b93-accd-e1df7936dfc1 | -7.13462 | -44.33822 | 2025-09-25 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41cd763e-bf4a-34e6-9474-1b37280ca133 | -5.59998 | -52.15829 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4481ce57-d092-360a-b5d8-55187b840144 | -4.74171 | -44.43019 | 2025-09-25 04:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5f7d03f-6a8e-353c-881d-978bf50bd618 | -3.79393 | -41.73516 | 2025-09-25 04:59:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51566f4c-1eef-3e84-b34a-e7e9d6f5d7c6 | -2.26345 | -47.19468 | 2025-09-25 04:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4296bd6b-e931-3e8e-bbbe-f0717c66ea2c | -5.09202 | -47.47274 | 2025-09-25 04:59:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72c17609-6d89-3d68-bb2e-67a1230c6d47 | -3.69986 | -49.57441 | 2025-09-25 04:59:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eea118dd-b66b-3def-862f-a0df6037f6b6 | -5.06076 | -44.31595 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf85ba69-9481-3988-aa41-48b09701d403 | -3.08565 | -52.92137 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c610b194-1e7a-34b5-bc7e-0b71b0616c9a | -3.49605 | -59.05462 | 2025-09-25 04:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0f2276e-da28-3741-b7c0-8438718aa3b4 | -5.86782 | -45.28207 | 2025-09-25 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23beaf1f-a166-34b0-bacb-4d19b335554a | -4.03047 | -47.77497 | 2025-09-25 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 03731ef3-355b-32ff-b99f-7a993c988ca6 | -4.45523 | -55.43198 | 2025-09-25 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99787623-4e80-38e7-92e7-2ee8d3a88547 | -2.3837 | -57.2398 | 2025-09-25 04:59:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e403199-c64c-38ca-a5d3-8485f990d829 | -4.7995 | -47.2721 | 2025-09-25 04:59:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17df013a-78a6-3e6e-90cf-001b8681fde3 | -4.44279 | -50.7422 | 2025-09-25 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02601b7b-b187-3183-8c08-48f69714532a | -2.64132 | -54.5479 | 2025-09-25 04:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df8ae12a-381d-3f32-9aff-f0e705c0644c | -7.25701 | -43.0205 | 2025-09-25 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d9fa0366-22e4-3ce4-a65d-216c05465889 | -2.68808 | -48.46978 | 2025-09-25 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa2670d0-d82d-3678-a7d9-ffef4caeb968 | -5.39813 | -48.84849 | 2025-09-25 04:59:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05c29936-5330-3acc-b75b-ee89b9a4a682 | -2.44736 | -57.94139 | 2025-09-25 04:59:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42c19e54-6261-3aed-bbfb-0946014b7baf | -1.53578 | -51.61526 | 2025-09-25 04:59:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdc857f2-898a-32cc-aa17-c4de06f9df44 | -4.34524 | -50.50399 | 2025-09-25 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb409e8c-e2d6-37fd-872c-6f2dbcf88970 | -4.76276 | -43.25411 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c9db37c-b5d7-339c-81f4-0389031621c1 | -4.08383 | -54.30598 | 2025-09-25 04:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 967a650f-99f8-3ae3-925f-e95cde34b433 | -6.69296 | -44.6218 | 2025-09-25 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2859966f-d85f-3f2b-8095-e15e52543594 | -7.26287 | -44.90931 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5d479a6-1fcb-36a5-b1ee-658e29df8a1d | -4.20258 | -55.15491 | 2025-09-25 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c921912-474a-3651-bd98-e2388e7be20b | -2.9202 | -48.30985 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d8daa95b-ebe3-3864-a43f-da6b063199c7 | -3.83319 | -50.96612 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fa06643-11e1-3f26-b554-936b0852317d | -5.51287 | -43.86314 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41f366cb-cbe8-3e01-9084-f29b8ddaf386 | -3.61739 | -51.80363 | 2025-09-25 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c5a6189-430a-3d63-ab80-f633be0bbcac | -5.22997 | -43.6974 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b18271f0-290c-314c-8bb1-83800f78f93d | -3.61453 | -51.79942 | 2025-09-25 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d9f5223-51ff-3967-a43b-2cb3769796d6 | -7.31692 | -45.75239 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7225f5bd-2647-3f9e-bf2a-f9aa588fdb84 | -6.68366 | -43.12777 | 2025-09-25 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daa94ca1-b7e4-38db-8bb9-a4f4d26cc89c | -5.52507 | -43.86794 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 287526dc-3700-3ff1-aa58-7f16d00fea84 | -1.82298 | -55.27713 | 2025-09-25 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf85adb9-e398-3659-89c7-088bbd2c1205 | -1.72684 | -55.74654 | 2025-09-25 04:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5b08806-8945-32f5-bb87-f71428fbe586 | -3.4915 | -53.28397 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63efa519-e7d3-3174-a2b7-d7dd54ef743d | -3.78105 | -41.73352 | 2025-09-25 04:59:00 | NPP-375D | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 811b8831-e20f-39ef-9f53-404f6522890e | -6.34664 | -43.36688 | 2025-09-25 04:59:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0afe17d-e611-3f22-84a8-4b0590fdab90 | -4.01007 | -43.27435 | 2025-09-25 04:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 256025ea-17c4-33c7-a37d-9314f1f9ae4f | -6.75242 | -44.63532 | 2025-09-25 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README28.md)
