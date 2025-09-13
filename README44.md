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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b70e7332-8d43-364c-a6dd-d0fcebab0fda | -3.22483 | -47.13028 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7b62d1ca-8624-3c19-8d94-07324ee1bbb7 | -5.38736 | -42.81222 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b47293ad-b58a-3ad9-b4cb-45562483d463 | -6.43829 | -42.61896 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b08ff143-3e9b-3a3e-a972-7d3f7d809c9e | -5.40415 | -42.83717 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78572fd2-da96-3f13-be34-6b1e487823a4 | -6.28179 | -44.23921 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e7d63fe-1f5c-3fa8-aa24-1699112e9b50 | -6.31708 | -43.5701 | 2025-09-13 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4560868e-3e5d-3184-9be4-1a00ee4c4953 | -7.41559 | -44.35083 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 971970ec-56e7-35a6-8256-03c2af482cbe | -5.92508 | -42.75299 | 2025-09-13 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ed603ac4-0434-39bc-adde-d5ac704f2a32 | -7.44891 | -44.39188 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9371ef62-6ab0-38d2-853f-1382d9393925 | -7.15082 | -44.35365 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6b6a90a-61e1-372b-afda-995151609c3c | -6.19934 | -43.45164 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5de6570-4cce-331b-8b5c-b6ca1530d6f4 | -7.43091 | -44.41339 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 278a1553-7871-3d9a-9b36-914d51e7c67c | -4.48294 | -48.11514 | 2025-09-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63aa2529-eac6-30a6-bce2-794ce78e7876 | -6.25767 | -43.47972 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b6a217a-b3bd-3782-adf0-841923708716 | -3.81087 | -52.09119 | 2025-09-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ce70303-b5e4-3d15-af7b-a3865d1ae07f | -7.25693 | -44.59304 | 2025-09-13 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee65d803-7f57-31b3-8af5-e0ad90e4ce6b | -6.53299 | -44.76377 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc47f604-481f-327a-b1d2-b6f92e959159 | -3.43222 | -42.46905 | 2025-09-13 04:06:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb6ced60-05e6-34be-9d84-d70af4ed4576 | -6.83418 | -47.86359 | 2025-09-13 04:06:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0ed17da-6303-3225-9d46-3051d3115869 | -5.65498 | -42.60802 | 2025-09-13 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4628ce68-7124-353c-8c09-e4d03c0acf88 | -6.41193 | -44.37567 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f1756aa-458e-3f4e-b606-4f7815d75ded | -5.54477 | -46.42495 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dcf19f8-a5d2-3b04-88b8-8a63b3090640 | -7.06317 | -44.68771 | 2025-09-13 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 519bd5f9-40af-3786-99a6-f256a02e7eca | -3.22043 | -47.12957 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| db6a65b9-cb30-30a0-9e77-4a63701c3c04 | -6.56047 | -50.87413 | 2025-09-13 04:06:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b86b2e10-5a0b-3c1e-b209-6531d3a7dbb1 | -6.372 | -44.41898 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 178aa480-c1be-3de1-a1fe-4abca4c4e3e5 | -3.51702 | -47.21723 | 2025-09-13 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fce03912-87a5-3886-b5e4-2f23fa28f524 | -5.66333 | -42.62035 | 2025-09-13 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bae5bfdf-1b53-3897-9f0e-7e531be42581 | -6.38992 | -44.37626 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edaef736-c5d6-3f72-bf83-acfbe2ad8e10 | -5.95077 | -42.77527 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ceed6247-408a-3e0e-b17e-31b7256749e8 | -7.5571 | -42.63477 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78e0db13-842c-3d6a-9b31-1a0bb2ebbbe5 | -6.50433 | -43.80172 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83c12d5f-b394-3477-8f4e-828c77f832d4 | -6.69375 | -44.13661 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f615fcb-9e99-3d8d-a744-6474dcfc9172 | -8.02957 | -39.58915 | 2025-09-13 04:06:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b677fbec-f752-38d4-a6d9-90a0cd520c29 | -5.95299 | -42.78296 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 03a2d21c-f8d0-3341-be4a-a6364e87311e | -7.43354 | -44.39745 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cf19583-6e99-3244-b609-3183bade5616 | -6.6966 | -44.14117 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cd9986d-3347-3cc5-bb6e-40b559b001dc | -7.55875 | -42.64585 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e12e2e43-595c-3f43-9dd7-42ae536867f7 | -6.13996 | -43.36284 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cbd87348-8b8a-3b61-9a93-be0e0fcaca1f | -6.2139 | -43.33965 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c0e930ef-104a-3436-95fc-7da2899eacd0 | -5.5312 | -43.04766 | 2025-09-13 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c5e3b81-d020-3296-89a8-66f588abcf06 | -7.23416 | -44.41967 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ccf8d51-b1ac-3e20-a788-25353c547d02 | -3.23239 | -46.78561 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e23fefb-7186-3ee5-ba81-2d9c44d22589 | -5.65025 | -43.8912 | 2025-09-13 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89f90c79-2af8-3b93-9fc6-ba89104ff74f | -5.96884 | -45.84866 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c78e2b84-786b-36e8-ae4e-7e1f5f58ea39 | -6.18634 | -41.07872 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0f3de1f3-8938-343b-8482-e7197d1b1774 | -7.39449 | -44.34746 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ebe4c56-31da-3b3e-9cde-261cb3740bc3 | -7.31279 | -46.586 | 2025-09-13 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a279d93a-0b53-34ba-a0f1-e33915783632 | -6.17675 | -43.48247 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2733cde2-c8c2-390d-823b-fd2ff82d9a40 | -6.5653 | -50.87811 | 2025-09-13 04:06:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eac38d0-59fb-3594-b5e2-cdc181b49259 | -7.4076 | -44.33326 | 2025-09-13 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 041b42bd-b719-31df-8150-c000df1c4235 | -5.99639 | -43.34007 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d534caef-1c5c-3f4f-aa2e-7bcf9eac47d4 | -7.44953 | -34.8615 | 2025-09-13 04:06:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1efb5054-86aa-30de-a822-68b1d648faab | -6.0711 | -43.26822 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 908ea87b-6fc3-3f83-bd92-cce52adad3bc | -3.6639 | -52.17861 | 2025-09-13 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e12100d7-3736-3332-93b5-c4c32e90618e | -6.28244 | -44.23522 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c1e3d8e-ae14-3976-a631-2339dbac697d | -6.43886 | -42.61544 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 721d7a62-96fb-3e86-93c4-32437198bc76 | -6.17324 | -41.14047 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f1460f6-6e4f-3d3c-80f8-2d239cf6292c | -6.18421 | -41.11383 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d169ebbd-63e8-3821-bed3-ac2d232b08ef | -7.0596 | -44.68706 | 2025-09-13 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a7d2408-041a-3cf6-b079-4f30029a8522 | -6.16869 | -43.35895 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9185b3f2-04cb-3012-83aa-1c779738e945 | -5.24961 | -45.57948 | 2025-09-13 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f578ca9a-79c1-32ae-a5d5-7964e3424aca | -6.78898 | -43.40414 | 2025-09-13 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cac61321-632f-307d-8a0d-0943512082c6 | -3.51631 | -47.22155 | 2025-09-13 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79405e1f-9ee7-38e5-af0d-6ba8f289300a | -5.94741 | -42.77472 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e9980f7c-8cfc-351e-9cda-67d6ee02fe7b | -6.77391 | -41.59696 | 2025-09-13 04:06:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2348fb4b-3202-33d7-9bed-178c9d029b71 | -6.26735 | -43.48515 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbc96245-e117-353a-8317-028002305372 | -6.1727 | -41.14393 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a59ba74-71f5-324b-87c5-e6b03005d66f | -5.40532 | -42.82991 | 2025-09-13 04:06:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab506145-4ed6-366e-810c-41dcc3a084d0 | -7.51494 | -44.67432 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 875b4df0-3582-3d54-a505-93db63368111 | -6.08475 | -43.2704 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 12b0a4cd-2322-34a0-9108-dca5f2090db6 | -7.2164 | -43.97208 | 2025-09-13 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 359bd8f0-cd69-3cbb-b999-205ab2e7e2da | -6.17928 | -43.2509 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2513130-bcdf-3662-a43d-180ea8f1e7ea | -5.94405 | -42.77418 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1554dddc-6c6a-3a0c-8a9d-89a39397c830 | -7.55985 | -42.66046 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d30e4a5-9a51-397e-891c-3284822bef15 | -5.72287 | -43.18671 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97cb60d2-b117-3828-b6c3-9f2eb919c900 | -5.7251 | -43.19461 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef2036a8-7839-3baa-951b-cf3e31ecf4a5 | -3.2268 | -47.63702 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a72f514f-e731-3a92-8335-85dfb1a1a6e1 | -6.16939 | -41.14341 | 2025-09-13 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b17b90a5-1842-3986-b36c-2e090c4ca718 | -6.29238 | -44.2411 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe67abbb-3bf5-3758-af07-1872d0d607b3 | -6.28053 | -42.39507 | 2025-09-13 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 03235b53-1f0d-3669-a4f5-6696cc75afb0 | -6.50717 | -43.8062 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fcd0f1c-7fdb-3a7a-9948-04f0cb0738fb | -6.7918 | -43.40838 | 2025-09-13 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7290240f-fbaf-3152-b8cf-45af28123630 | -5.71663 | -43.18195 | 2025-09-13 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a2aaf73-880f-3fb0-af68-4c47831470a8 | -3.22924 | -47.13099 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9ac5cc7b-6809-3060-b781-371753b2965d | -5.19882 | -43.0441 | 2025-09-13 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1349979d-fb2d-3210-a3ca-b454fc83a1b1 | -2.87434 | -41.74554 | 2025-09-13 04:06:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6860dcfa-2a06-3e8f-a8b5-28c7cf756e34 | -6.29782 | -42.22191 | 2025-09-13 04:06:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ac758a9f-3312-3ea5-979a-f38695b29531 | -6.10449 | -45.94873 | 2025-09-13 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8f6826cb-7153-3e6f-9256-e95a92016bd3 | -6.06282 | -43.55754 | 2025-09-13 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51460ab0-9ccb-3b2a-a692-84173066f116 | -4.15145 | -43.88306 | 2025-09-13 04:06:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5d25368-8500-325c-bc84-4107cf304b13 | -7.69703 | -44.6892 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63cf7406-54af-3f65-be5b-41bdd10089e1 | -12.10456 | -47.57813 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e7fdf67-5b01-31f4-b5bc-ae9e1532e101 | -11.86443 | -46.75376 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 63472c51-d59c-3aaf-a1fe-1f7d9111b59b | -9.00921 | -45.76937 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbb5f247-9f30-3408-9b10-53360c6d6743 | -14.26007 | -45.04966 | 2025-09-13 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 213b8914-42c0-3ed0-8446-bdb184377435 | -12.93142 | -54.74429 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 768e3baa-f9b9-372e-a430-acffa5578276 | -14.19894 | -46.24635 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| d2d7e0d5-a76f-30e9-992c-fc1fbbf62498 | -13.91236 | -48.27688 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8a27a724-e754-3d51-bf87-d0ce94e90802 | -14.20326 | -46.26395 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README45.md)
