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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7ebdbb8-6de2-3ae7-aae3-32dff1c66de0 | -15.40465 | -55.91697 | 2026-07-29 04:17:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4f7a4097-e576-37e7-a662-6cb086bebe54 | -19.6901 | -42.02857 | 2026-07-29 04:17:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70d0e4e2-75d3-3002-9ab4-07d352cb1a7a | -20.60518 | -57.25784 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d103876c-338d-38b7-bdbd-78902dcfd470 | -16.15222 | -48.61522 | 2026-07-29 04:17:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ce8bd32-13b6-3c5f-895b-1c9b2f452f48 | -21.02324 | -44.57726 | 2026-07-29 04:17:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60bfda6d-7e65-3863-bd0f-6c03da95ebbd | -18.025 | -41.82984 | 2026-07-29 04:17:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3722f604-c1fb-3de0-9330-7469d9240563 | -15.86782 | -49.61214 | 2026-07-29 04:17:00 | NPP-375D | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08ce22be-01b5-3c0e-aa75-e4b38a94b1bb | -21.44813 | -43.79151 | 2026-07-29 04:17:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d4bc9d6a-2f94-3854-acd2-6a1c9d82539d | -20.67235 | -40.51404 | 2026-07-29 04:17:00 | NPP-375D | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6ca011ba-27ac-3a81-8cef-922148f90062 | -21.08094 | -44.01159 | 2026-07-29 04:17:00 | NPP-375D | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7673b4a6-979f-3a5b-8da5-f9714bcb618b | -23.45679 | -46.43705 | 2026-07-29 04:17:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cab9f4d2-c4f6-30f9-8582-48e7a089120a | -21.45145 | -43.79211 | 2026-07-29 04:17:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f076e221-42d2-3805-a2e7-1909b8beea35 | -25.9394 | -49.11987 | 2026-07-29 04:19:00 | NPP-375D | TIJUCAS DO SUL | PARANÁ | Brasil | 4127601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6406a3bb-01ba-3feb-8413-6ba7ac9bddb8 | -23.24642 | -52.33127 | 2026-07-29 04:19:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fc8bb3e4-98ab-3e8e-81a7-7832a20eebfa | -23.84451 | -52.86479 | 2026-07-29 04:19:00 | NPP-375D | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2f722d00-8e7c-320e-92df-b6b8f7b79769 | -21.98081 | -57.59678 | 2026-07-29 04:19:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1247b1c-d228-3b70-a96d-8dc61a522eb3 | -23.84744 | -52.86477 | 2026-07-29 04:19:00 | NPP-375D | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 807b52aa-f875-3976-bea4-546998eccd22 | -23.84866 | -52.85901 | 2026-07-29 04:19:00 | NPP-375D | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cc66365-94fa-36e1-9394-549cdb7ea666 | -24.48742 | -50.12091 | 2026-07-29 04:19:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04897ca7-5eb5-3eb0-a7a7-254689b9a45f | -23.09928 | -52.6847 | 2026-07-29 04:19:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 2235f3f4-5310-38be-b0a6-0d94bf044fa5 | -23.0985 | -52.68254 | 2026-07-29 04:19:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| f7ef36f9-2674-31ff-b946-2c18f3b45879 | -23.10056 | -52.67887 | 2026-07-29 04:19:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ac4b64dd-2287-3eea-8812-ba23c9d567af | -23.84576 | -52.85906 | 2026-07-29 04:19:00 | NPP-375D | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b1a6dc9-8b57-33ce-94bd-c7de8bb20ccf | -20.3058 | -50.5981 | 2026-07-29 04:20:00 | GOES-19 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| 018e8cec-0289-35c0-8f28-ae864e966e98 | -10.9397 | -43.0593 | 2026-07-29 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| c5857565-4c70-3884-aa27-5799a3106809 | -10.9401 | -43.0355 | 2026-07-29 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 52b935af-02c1-30f0-8de2-7e08ccb3f5d6 | -10.9205 | -43.0622 | 2026-07-29 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| aecfce59-3eba-3abc-9c78-bba735778315 | -7.3413 | -45.8377 | 2026-07-29 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 43d78bb8-d50d-3856-a379-d89ff30bd65f | -7.341 | -45.8602 | 2026-07-29 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 69e465be-3e25-3d4a-b920-31f67dbba645 | -7.36 | -45.8361 | 2026-07-29 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 97e6defa-9775-3bdf-8003-5b67d32d8059 | -3.78368 | -49.71498 | 2026-07-29 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe079052-9f48-3744-a523-8f0ecc5d5548 | -3.16674 | -48.12565 | 2026-07-29 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 305b5ba5-5cf4-3cbd-b607-cb0a369bf0e1 | -3.03354 | -48.41732 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35c181f5-37e7-3007-9c24-17bebac48ee7 | -3.68161 | -47.64225 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7284e5fd-12b1-3450-b9de-6695479243f9 | -4.54708 | -47.80315 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83339f6a-444b-34e1-b4eb-f0a0f4355b0b | -0.99343 | -48.08497 | 2026-07-29 04:29:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30ae26ad-6967-3bbe-81dc-84f7bdf9ad2d | -3.17563 | -48.02461 | 2026-07-29 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0b3b325-fe37-3a15-9cea-86b37875ce83 | -3.06498 | -48.35737 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69c13750-0dd2-31ad-a511-8fbf6e0fad3f | -3.94413 | -40.96922 | 2026-07-29 04:29:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecddc226-4a61-3c9e-a95d-6cb25c3bd0d1 | -3.9582 | -48.12475 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42fe0241-bef9-31af-85b6-aaaa3de315eb | -3.16961 | -48.13005 | 2026-07-29 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f348ac7-b974-346f-b91f-4e3b6537874b | -3.03483 | -48.4094 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| debd15a0-0ab8-340c-9754-e978bcb7e0ae | -4.86979 | -45.30962 | 2026-07-29 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1c18425-1587-3a29-aa5e-704222d6622f | -3.16613 | -48.12949 | 2026-07-29 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d59597da-052f-371d-bf20-18d92fa29743 | -4.87311 | -45.31015 | 2026-07-29 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e0c1af0-ea43-3573-9df7-1050a0ad1566 | -3.68502 | -47.6428 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 122e18b9-2b10-351e-a0f9-5891ffbe6406 | -3.71916 | -48.87919 | 2026-07-29 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75724dfa-1ddc-390e-bc6b-ff90850cfe79 | -3.03419 | -48.41336 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8363b40a-4601-3a4e-827b-46e2b077d0ef | -3.6856 | -47.63911 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a257cdd-c5fa-3dec-bafb-0279f04107a6 | -5.7288 | -39.03688 | 2026-07-29 04:29:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d956d88-6d09-31d4-aa28-df75b007634f | -3.68843 | -47.64335 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b3eb49a-0257-30b4-9ff9-62061429c3c4 | -4.75374 | -45.63581 | 2026-07-29 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3b71194-3360-3ff6-9662-19c5e5654c30 | -4.27926 | -48.24387 | 2026-07-29 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38c774cb-76ab-33af-a1db-a3e8fb64a281 | -3.06851 | -48.35794 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50b3150d-e20c-362f-92bd-8289f8dfb195 | -3.06434 | -48.36133 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa6c5498-f74e-3e9b-b8d2-468925f043a2 | -4.87034 | -45.30613 | 2026-07-29 04:29:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37720ebf-00ea-35ea-a08b-26753470b6f9 | -4.36957 | -47.77146 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b8d87e6-d6fa-3dca-a160-ffd4d7ee4aa0 | -4.27864 | -48.2477 | 2026-07-29 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a277c216-b000-3b44-b25b-887949b29f9e | -3.68784 | -47.64704 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec2c18e3-1333-3edd-a7cf-edf2bda51db6 | -3.06082 | -48.36077 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ae1f3f0-5b04-385e-8fd3-56ae0bc2a065 | -4.38953 | -47.75578 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf11e54-3583-355d-a256-61051aa8de73 | -3.95881 | -48.12094 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59e4741a-3576-3084-832a-d325a59e30fb | -3.67879 | -47.63803 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63462612-c407-3cb6-bb64-e47c3ccd1c69 | -3.0313 | -48.40883 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c181983-e039-3cc4-81f9-73d35e9084c8 | -4.36676 | -47.76725 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 62e00237-5dc0-3042-bf94-792a343ee470 | -3.68824 | -47.64671 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bdc7c935-18fd-353c-be00-a3fac635ce09 | 1.02105 | -51.3012 | 2026-07-29 04:29:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeeedbb4-10e9-3879-bfa0-9b6e512b69a9 | -3.67821 | -47.64172 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 39292ebc-e0ce-37dd-8a44-c0d42ee59707 | -4.54368 | -47.80259 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41872045-cbba-3394-a2a0-0679f4e0fbbb | -3.06146 | -48.3568 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a98f002-3512-30c7-b854-d29eca06a84a | -3.96166 | -48.12527 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 493d54d7-ed8d-3f70-9ba7-35e13b6d28e5 | -4.47055 | -38.64532 | 2026-07-29 04:29:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| be7f0d73-6e10-3ca4-8035-69a7570aa9ac | -3.68901 | -47.63966 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cc47b1c-cc91-33b2-85fd-7059f20cd77d | -4.36735 | -47.76357 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 694b3a40-3e59-372d-b76d-4ee757565859 | -3.67762 | -47.64541 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 07f976b8-7ae7-3a4d-bce6-cdf23a1a5a5a | -4.37016 | -47.76778 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c770f241-18e0-3d99-a9b3-c8425eddaffd | -4.1164 | -49.08623 | 2026-07-29 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 01122d29-0ac3-3f7e-b1ba-376e281a17c4 | -3.67344 | -50.94755 | 2026-07-29 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ed714f7-4a2b-34de-aca3-0dcd7da1a65b | -3.72982 | -49.27226 | 2026-07-29 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be99fb76-d8cf-36f0-b6eb-ffce2b3d3aa3 | -3.68103 | -47.64594 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6ae9576a-2ec5-3cda-bc77-67e94fe8f63b | -3.68943 | -47.63934 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5426219d-5d4b-3978-a7d3-01095c567481 | -3.68444 | -47.64648 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8036318c-6ed0-37da-b0e3-2d92f4c577b0 | -3.03066 | -48.41279 | 2026-07-29 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eaa96036-babb-38c0-ba84-bd36a12cf2eb | -3.6822 | -47.63857 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1012300-63ed-31be-8722-646b2f45e2c7 | -3.69164 | -47.64728 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67a47717-3072-3760-83d9-0559abff5c75 | -3.96512 | -48.1258 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9883c7d0-97a0-379d-9b17-fb3fa1200aa2 | -3.1731 | -48.13063 | 2026-07-29 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5534d039-a3cf-30fc-a12a-082f07be58fe | -3.47923 | -43.31036 | 2026-07-29 04:29:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5db911e5-f492-3ec6-ae79-edb901714af3 | -3.96104 | -48.12909 | 2026-07-29 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39613071-9f63-35de-880d-c7bcc0289a77 | -4.4698 | -38.65038 | 2026-07-29 04:29:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0c2e8455-8086-3f6c-967c-760244003bf4 | -3.48182 | -47.68613 | 2026-07-29 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fb77bd8-4306-3259-85c7-17f6385ef9b5 | -3.68883 | -47.64303 | 2026-07-29 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a4fb59e-335e-3754-b547-ad7cba0e169a | -3.78258 | -49.71696 | 2026-07-29 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c07eb62c-ac41-3755-aeec-3b2e1afeb22c | -7.36 | -45.8361 | 2026-07-29 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c4a72bdc-932b-34b8-94f0-eaf2d14ad07a | -10.9205 | -43.0622 | 2026-07-29 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| cd7b6650-e7b8-3eb9-a785-b89af30a619b | -7.3413 | -45.8377 | 2026-07-29 04:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| cb21641e-7da1-3a20-ac80-fdd823888beb | -10.9397 | -43.0593 | 2026-07-29 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 6d8e629d-8010-386a-bb97-0bf6b86a83b9 | -11.71653 | -50.1821 | 2026-07-29 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fec289a5-5315-378e-b36c-46d2df674cc2 | -9.61151 | -47.76588 | 2026-07-29 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bcc72990-608b-33ea-9c23-e45ec1aae1b8 | -6.87492 | -46.01627 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README10.md)
