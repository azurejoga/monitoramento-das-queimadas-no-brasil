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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95919057-39c3-36f5-9a63-e0b8ba07836c | -2.92702 | -52.69292 | 2026-01-30 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbe3d30a-2416-3337-9ee2-33baa2ff546c | -14.04059 | -50.52861 | 2026-01-30 04:53:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df084386-7534-3745-bdf4-48b585656dfa | -3.05535 | -52.83011 | 2026-01-30 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aaa1770-2e3c-38ac-9b71-6ae004873108 | -1.84487 | -54.10139 | 2026-01-30 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b71099fa-a6e6-3423-b578-1011ce935082 | -12.5444 | -54.59956 | 2026-01-30 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd1cb2dd-e726-3b2a-ad37-41ff351bc1ed | -2.81737 | -52.95731 | 2026-01-30 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c25faa14-fb9c-3669-b9b8-4900d3d98109 | -3.5359 | -53.27869 | 2026-01-30 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1662c3b4-96aa-311c-a038-b9493f95578c | -2.42684 | -49.0302 | 2026-01-30 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d7a05e7-ae3b-3355-b5fa-78f04e1e2e38 | -5.53631 | -45.9577 | 2026-01-30 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a951c8d9-7f5b-3996-8e95-c3eebd41cffd | -1.84253 | -54.1017 | 2026-01-30 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 882390ea-a48b-3686-8cbb-40065b4f1897 | -3.9195 | -40.72872 | 2026-01-30 04:53:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7c853295-1e46-3a71-a745-fa18328fae62 | -12.30695 | -57.3641 | 2026-01-30 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b88ed48d-8809-3116-998c-f3e483f48ba2 | -1.19887 | -53.65891 | 2026-01-30 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4344caca-83ae-3582-af42-1b74bd0e808f | -8.15784 | -43.19103 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 479cd503-650d-3463-b081-0c786c2735b6 | -13.78861 | -52.72985 | 2026-01-30 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0c8e208-5c86-30ef-8d0f-48325fe16bd6 | -1.68929 | -54.77898 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee17256b-2b4e-35fd-a5a4-bcb5169b47ad | -1.84601 | -54.10219 | 2026-01-30 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6be7c84-77df-305f-9cbc-778234bdd29d | -3.16438 | -52.85128 | 2026-01-30 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60d04bee-22c9-3cd1-a295-1906b21950c8 | -2.50036 | -56.08095 | 2026-01-30 04:53:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b5c67ad-c009-3772-8ac0-8c3a690dfe52 | -1.81465 | -54.49175 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 925c38aa-88ac-3853-9a1f-0b9c960c30cf | -12.55351 | -54.58721 | 2026-01-30 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c54c7531-af13-3180-8c3c-1a2bbcd8346f | -1.95317 | -47.90494 | 2026-01-30 04:53:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae6ea452-7a14-3cda-bdad-90fa90c419bd | -12.31218 | -57.36375 | 2026-01-30 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70cb7e7d-5adc-35b4-ad64-bcf1439c6e4f | -3.42492 | -53.42105 | 2026-01-30 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff4a36be-5646-3a04-b1c1-20f19b24980d | -1.81528 | -54.48778 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17973d9b-7ea2-30e4-b206-479dc1707a56 | -1.80695 | -54.49465 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9086470c-939c-38e4-bdb4-379f4878b705 | -1.81111 | -54.4912 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 68f40287-b5a3-3ca3-b246-386e6805fbf9 | -8.12899 | -43.14801 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 78e8a5c1-61de-39f7-aa24-cc6ddce2a81d | -1.84549 | -54.09754 | 2026-01-30 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4411c8b-e0be-306e-aa2a-bf4431bd1add | -5.93583 | -44.45729 | 2026-01-30 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b8a97f6-a001-3e4f-b72d-4f72d1d2b6f3 | -11.18708 | -55.92203 | 2026-01-30 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae29e8fa-ef7b-3abd-ba36-f419541f93d2 | -3.82127 | -54.37706 | 2026-01-30 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3add1551-5b08-3c4f-a7bb-d8138adee874 | -1.81818 | -54.49231 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e83768b8-69bb-3b61-a3ce-cae498619e6c | -8.1285 | -43.15186 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d31921f-6fdd-35a0-a763-31dd3e773aec | -4.97087 | -50.91126 | 2026-01-30 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0bade0e-034c-3325-b3b4-6debe43da22c | -1.41602 | -45.65484 | 2026-01-30 04:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3d0eebf-bbf8-3c72-8b3d-a18f405e319c | -3.76665 | -52.0504 | 2026-01-30 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0e470c9-99be-3fb7-838c-558af8107eca | -3.29308 | -52.72579 | 2026-01-30 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e992de4-697a-36b8-80b8-e312fdafe2dc | -12.54881 | -54.59305 | 2026-01-30 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d830795-ab58-322c-b478-0b4a5284a375 | -11.1768 | -55.92033 | 2026-01-30 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15513b11-fe25-33df-9efb-38971e82267e | -1.81175 | -54.48723 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f48ddf8b-fa01-3c9f-983e-d031015de2a6 | -3.20281 | -51.97896 | 2026-01-30 04:53:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eb17e27-201a-3aa4-bf51-7ceb2b3af253 | -3.26738 | -42.55088 | 2026-01-30 04:53:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02447000-707a-32af-a74a-35ca1001ec52 | -1.84313 | -54.09785 | 2026-01-30 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2474cdd-9236-319d-99e7-8e0879a641d8 | -12.34785 | -54.76651 | 2026-01-30 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 645d243f-4b81-3c45-8a6c-03ba29c41865 | -2.9019 | -49.37865 | 2026-01-30 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e80a156d-e4c0-34a3-b4c8-635dec44a28d | -4.98022 | -47.91635 | 2026-01-30 04:53:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 586f0786-16bb-3b9b-a3ee-637b062a9803 | -3.74044 | -52.43275 | 2026-01-30 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a48b0cb-347d-356f-987e-8de6390dfc84 | -12.54826 | -54.59658 | 2026-01-30 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab75b770-d72f-3d93-a6c6-44409de94186 | -8.15223 | -43.19011 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 687940ac-1cb2-320c-9d48-f48d361af21f | -8.12544 | -43.14955 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 58d5ae1d-9c8c-3d35-9482-1d2610a8d98e | -11.18146 | -55.91336 | 2026-01-30 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28336c65-2ce2-3768-8fd2-718bfd6df65d | -1.81048 | -54.49519 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7d08fb77-662a-3593-8577-9320441bd06a | -13.69081 | -52.58836 | 2026-01-30 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22e0a255-2bce-3f07-bf15-14accc5cb528 | -1.45239 | -54.05396 | 2026-01-30 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ff997d7-fe52-34fc-9481-12fe922955ca | -2.24972 | -48.1721 | 2026-01-30 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb0f7cb-87df-33ee-9371-5fdbb34d2432 | -13.78522 | -52.72932 | 2026-01-30 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b84890b6-31e9-38ec-a0a6-e9a0f6204f91 | -2.53714 | -54.73838 | 2026-01-30 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67566d6d-7b98-3f21-80b3-a910666767bd | -12.54495 | -54.59604 | 2026-01-30 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e44fd692-7441-31dc-9846-3cacc4c4f158 | -1.80953 | -47.70075 | 2026-01-30 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fd7e4c0-79b9-3159-846e-55d542ac6ac6 | -8.13107 | -43.15034 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a6d307d0-f227-33b7-92af-a44a5d77b1f1 | -2.98937 | -52.36002 | 2026-01-30 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b56f1e20-698b-312f-bb5c-55c2d47d482e | -2.15573 | -53.6517 | 2026-01-30 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0984fe1b-b422-339b-85cb-978e7dfddbd1 | -13.78805 | -52.73357 | 2026-01-30 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7057d24-4d73-3509-aa09-2a8899975625 | -12.5477 | -54.6001 | 2026-01-30 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48afff9b-9efd-39b4-b95d-e653989ca57d | -1.80758 | -54.49067 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 74d12f07-3b6b-3151-a239-fb5e7873ebe4 | -8.13463 | -43.1488 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 28b6c367-6a72-324a-8e9b-b0995c3026b7 | -1.81401 | -54.49573 | 2026-01-30 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d393922a-ac19-38c0-b475-7567bb1c4caa | -3.54517 | -53.56752 | 2026-01-30 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b8ed3d8-fbe1-32dc-add8-7cd83058dbed | -12.56077 | -54.75483 | 2026-01-30 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18780f2-a13f-3379-a87c-fa3600e3685b | -8.12287 | -43.15104 | 2026-01-30 04:53:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52e98ccd-4757-3f64-a878-dd8a230ffd73 | -20.29379 | -57.35073 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d79125da-3e7e-3873-aee3-e86cae6a3898 | -20.31451 | -57.35065 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3b5e6057-cfc3-3cc6-9924-d5d55749e499 | -16.08174 | -57.09629 | 2026-01-30 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4267e090-e0c9-31a1-81f9-b1b25644bce4 | -20.26656 | -58.14078 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5a141208-1704-3629-9b7f-67f68b432adc | -20.31116 | -57.35003 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| eb5ee349-f0dc-3b4d-80b2-af7e3e3b374e | -20.26381 | -58.13618 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8e009c72-cad4-36ca-8863-510798797a54 | -20.27188 | -57.32403 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed57ad79-bdce-38f7-880f-70ef5a2d68c4 | -20.26314 | -58.14014 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 50da07f9-55e0-3ac9-8ce8-5d264a3b6c1c | -20.31514 | -57.34687 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 65e1afe7-6d5a-3f2a-8425-de52c718d4d4 | -20.26588 | -58.14474 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bc6848d4-b705-3fe6-8431-701abe7fffa6 | -20.28772 | -57.34572 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84e7f762-49c1-3ca4-b01e-98dfd4ba35be | -19.14575 | -57.79568 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 79ed0d16-4901-3ebf-8a78-68924ef6d3c9 | -16.58608 | -57.80672 | 2026-01-30 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 8732af04-6536-312e-8385-36805f580663 | -19.14916 | -57.79632 | 2026-01-30 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cecca4e2-43de-30e2-b4ec-ff746bea6e8c | -16.43995 | -57.27026 | 2026-01-30 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e734e2a3-c6a2-374e-b7ef-f09ce8329507 | -16.58539 | -57.81084 | 2026-01-30 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f150ae10-d9a1-3d73-b3df-1c39c7ab2096 | -16.44338 | -57.27087 | 2026-01-30 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0a2c55c7-97d1-384c-8510-64aabbc95a2d | -16.58889 | -57.81147 | 2026-01-30 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5a44ce3e-913e-3adf-a079-1ccb84a002c4 | -16.58958 | -57.80737 | 2026-01-30 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6b41f51a-2615-3e77-975f-69742caff612 | -17.06982 | -52.69086 | 2026-01-30 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5f96490-82d9-38b1-848d-901563e41dec | -15.42791 | -56.32286 | 2026-01-30 04:55:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91ee9830-8061-3308-a3f9-cc811a85c7b5 | -21.40387 | -56.05519 | 2026-01-30 04:57:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c08e1ef7-2f92-3d13-8f2d-3f9feba7bb85 | -21.30458 | -55.90548 | 2026-01-30 04:57:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf5c9b36-6e01-3273-9569-e6b665ad14d4 | 4.01384 | -60.88421 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19305683-11df-3b55-9b54-c4f45ea36ad0 | 2.74532 | -60.21431 | 2026-01-30 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d83a7cd-d689-32e1-94f2-5e67c9c0caf3 | 3.55232 | -60.5382 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11222ac1-1d68-3ba8-bfed-5428be4be221 | 2.5148 | -60.98678 | 2026-01-30 05:20:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1bd9011-7dca-383c-aca2-c31b2db02f94 | 4.19431 | -60.70351 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ef4a22b-1ea9-3a73-bd2a-37acc1fac92b | 4.19881 | -60.70753 | 2026-01-30 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README4.md)
