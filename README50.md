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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05a53e2e-90b3-3430-b396-b6b013edfe00 | -16.8491 | -55.892 | 2024-10-02 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| fc2aacdb-bb43-30ae-8241-b960c8f4f4b3 | -16.8295 | -55.8945 | 2024-10-02 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 17a3d418-62a8-335d-81af-708180572ee1 | -16.8292 | -55.9152 | 2024-10-02 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| b8e7d31e-9d88-3559-91c0-ce61c60177ed | -16.8891 | -55.8455 | 2024-10-02 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 30eb78b8-b56b-341d-8278-a27fcd251fd0 | -17.1581 | -56.1637 | 2024-10-02 03:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 6581a614-ff65-33ff-981c-ed5f15a35e08 | -17.1577 | -56.1844 | 2024-10-02 03:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 61cba880-59e2-38e2-bda7-9e0daf459b92 | -17.2364 | -56.1745 | 2024-10-02 03:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| f5de588b-a648-3920-b66e-076ad9a11aaa | -17.2361 | -56.1952 | 2024-10-02 03:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| e4c8583a-47a8-3bed-ae99-b1ac47d90225 | -17.2167 | -56.177 | 2024-10-02 03:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| ce475e57-ffb7-389b-aec8-70d65085e41e | -17.2164 | -56.1977 | 2024-10-02 03:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 29cace27-56e8-3228-ba99-fa3b2f596cb6 | -17.1971 | -56.1795 | 2024-10-02 03:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.6 |
| f9a3b4b5-1053-39b3-bae2-feaf8108ac56 | -21.3661 | -55.6807 | 2024-10-02 03:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e6fbbd1d-0633-33a3-8d50-ec1af59b0b1b | -21.3656 | -55.7022 | 2024-10-02 03:27:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0e75383e-2f2f-3c9b-a347-b231a6ad48db | -21.3456 | -55.6841 | 2024-10-02 03:27:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d2fa9b28-2e7d-31a1-9ec9-ae1ae11f6e60 | -22.3929 | -49.2727 | 2024-10-02 03:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.0 |
| 59038ddc-874b-3732-a0eb-b0388e496bea | -22.3922 | -49.2961 | 2024-10-02 03:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 265.8 |
| 25d9360e-fae0-3902-b073-35938592fcd6 | -22.3916 | -49.3194 | 2024-10-02 03:27:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.8 |
| a5c19f3b-fa81-3de4-8290-080f713b39a1 | -22.372 | -49.2777 | 2024-10-02 03:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 214.8 |
| e40330b3-766b-35e1-8c09-6038a616290e | -22.3713 | -49.3011 | 2024-10-02 03:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 270.5 |
| df33c7e4-471e-39a3-b491-78a2ef8f6ac0 | -22.3505 | -49.306 | 2024-10-02 03:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.0 |
| 370d0d7e-aecc-324b-a443-684460a53656 | -22.9014 | -45.0779 | 2024-10-02 03:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| bcf99ee1-4dd6-352a-b137-c404a5585333 | -22.9006 | -45.1029 | 2024-10-02 03:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 88eb9718-f352-3123-be5d-a5bb5e21dcba | -6.87951 | -44.29382 | 2024-10-02 03:28:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff112429-973f-375f-98b8-33cff531e33b | -6.60062 | -44.18356 | 2024-10-02 03:28:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b053960b-1b4d-3bac-b871-44bba964787f | -6.59993 | -44.18365 | 2024-10-02 03:28:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58b92418-4e6e-3ef3-9eac-057cad1e8f61 | -6.59419 | -44.18209 | 2024-10-02 03:28:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4db7dc34-d3df-33bc-b0e1-5d6cf43141d4 | -6.40434 | -44.75361 | 2024-10-02 03:28:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee16fd57-f57e-314a-be5b-36f9fab6be57 | -6.40116 | -44.74825 | 2024-10-02 03:28:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 278aeea9-4414-3e76-9bdd-6d41093566d7 | -6.40004 | -44.75423 | 2024-10-02 03:28:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76b880fc-e2d1-3fef-888f-5c4a1c9b0e6b | -6.39867 | -44.74657 | 2024-10-02 03:28:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e331a3b4-9fc1-3449-af85-5616826e5e6f | -6.39761 | -44.75245 | 2024-10-02 03:28:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de09b83c-205a-3699-b086-0f5621fc79a0 | -5.98507 | -45.36852 | 2024-10-02 03:28:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14e41bed-87ab-3040-a998-0ed19af172f4 | -5.98 | -45.36845 | 2024-10-02 03:28:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e8b7e12-7739-3f26-a6ef-6fc69fbcc77b | -5.97804 | -45.36737 | 2024-10-02 03:28:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ae8ba142-cf8b-3012-a9f2-cfb7c5393d27 | -5.97679 | -45.37405 | 2024-10-02 03:28:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e8669668-5aa3-34c9-b44b-0f7b47387fd7 | -5.97174 | -45.37412 | 2024-10-02 03:28:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 437939cc-39ac-3500-a87d-7f288afab13e | -5.96973 | -45.37312 | 2024-10-02 03:28:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3fa000e9-286e-3f71-b509-28c6be9a9c14 | -5.44666 | -45.18726 | 2024-10-02 03:28:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d54c2e13-7b7d-3085-a12b-b84e2f1176fa | -5.44549 | -45.17871 | 2024-10-02 03:28:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 288194d3-db35-3904-920d-40c0f0bbe61d | -5.44418 | -45.1857 | 2024-10-02 03:28:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce0d1b5b-a685-366b-aa4b-60c531b2dcd9 | -5.44084 | -45.17951 | 2024-10-02 03:28:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ce77dbd-2bd8-311a-9052-f27aed9c202f | -5.43955 | -45.18665 | 2024-10-02 03:28:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0eb7f428-6b66-37bf-9e85-20f06bf7e12f | -3.58957 | -44.54563 | 2024-10-02 03:28:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52ce384a-49c7-362e-8e2e-dea8f85b2f61 | -8.6915 | -36.23928 | 2024-10-02 03:28:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9434b39e-94c4-3dd6-bae2-45e88f1b646e | -8.68851 | -36.23414 | 2024-10-02 03:28:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f74c1d6c-0ed8-3f3d-a797-267952c7c7a8 | -8.68775 | -36.23867 | 2024-10-02 03:28:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 498fe781-836d-355f-907e-b9873ecdab76 | -8.16685 | -35.40311 | 2024-10-02 03:28:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8698229d-a3ed-3f6d-aa3e-bc48343a7d49 | -8.07502 | -34.97763 | 2024-10-02 03:28:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48ad5890-9334-3006-a9b5-b9d7a4628ebf | -8.07149 | -34.97704 | 2024-10-02 03:28:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c3fbd61e-3947-3587-8172-0574fc73adb6 | -7.49396 | -34.83694 | 2024-10-02 03:28:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1cce631d-156b-392a-bb41-b25858e9ac3a | -7.49331 | -34.84091 | 2024-10-02 03:28:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 8a9fc23a-22b9-38e9-abbb-49700ee5d767 | -7.49042 | -34.83636 | 2024-10-02 03:28:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 536632fd-417a-3096-9cd9-a7101d159838 | -7.48977 | -34.84034 | 2024-10-02 03:28:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6ea02bdc-f0c6-31d7-96ac-aac41385da8b | -7.47495 | -34.84204 | 2024-10-02 03:28:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26cd2695-341d-38ee-af1c-af1f2ed60321 | -7.45241 | -42.51155 | 2024-10-02 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4d9a8c8a-f193-331a-be7c-99bf1327c4b1 | -7.45167 | -42.51571 | 2024-10-02 03:28:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c469eb4-ee9d-3de5-8802-a01618def000 | -7.29182 | -42.25353 | 2024-10-02 03:28:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62ca7b53-9a6c-39e7-a8c3-0fbfef5e9f85 | -7.2911 | -42.25743 | 2024-10-02 03:28:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b3f5c99-2f2f-3fe0-981e-67c80de2a433 | -7.2899 | -42.25427 | 2024-10-02 03:28:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f2fe9681-693d-32ce-801e-f3b5aeb91feb | -7.2892 | -42.25822 | 2024-10-02 03:28:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cf354032-cb2b-3c01-9b17-e41e553e4b90 | -7.1846 | -38.92276 | 2024-10-02 03:28:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac5655a8-8235-3e94-85b1-457892467286 | -7.1838 | -38.92744 | 2024-10-02 03:28:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cee4b7de-585d-30d5-a745-02ef44780132 | -7.18006 | -38.92194 | 2024-10-02 03:28:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 42094773-6b56-3d9e-adb6-90d2927d37ae | -7.17925 | -38.92664 | 2024-10-02 03:28:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5d302f17-258b-3b09-9d3a-516f7cd3be79 | -7.15898 | -44.22298 | 2024-10-02 03:28:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fb2acf7-b31e-3a68-838d-055a245b3172 | -7.1581 | -44.22766 | 2024-10-02 03:28:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d91c9409-093d-3b55-bf65-f1fee083f8f3 | -7.07604 | -39.14864 | 2024-10-02 03:28:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| cfc0cddd-74a2-3fdc-8b1f-3bf4f0390956 | -7.07521 | -39.15358 | 2024-10-02 03:28:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 315276f7-1030-3875-b7df-0b6172b1a5ab | -7.07418 | -39.15037 | 2024-10-02 03:28:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| eaf767d4-01c0-3618-a735-3eab88996783 | -7.07139 | -39.14793 | 2024-10-02 03:28:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b487564c-b946-3b40-9b1d-3991ef5d71a5 | -6.95429 | -42.50403 | 2024-10-02 03:28:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f404a5f3-68b9-351c-afdf-8c81ccccd633 | -6.95353 | -42.50824 | 2024-10-02 03:28:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e9a29b6-adcb-39a5-bb8d-e1f687f876f4 | -6.87708 | -44.08996 | 2024-10-02 03:28:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d9b57be-582d-3071-b1e3-9f36925e36d5 | -6.87612 | -44.09511 | 2024-10-02 03:28:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 31ec06a9-b647-3105-84bb-f98d74f7e2f0 | -6.63678 | -42.10575 | 2024-10-02 03:28:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 387bdbce-2cb7-3042-a69f-dc62e41105a6 | -6.49843 | -43.8291 | 2024-10-02 03:28:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d00750e4-0fbf-393c-ac1a-e65bb7a0ae54 | -6.45913 | -35.11275 | 2024-10-02 03:28:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 25b03512-8ec5-3dc9-a745-1167ba8a5c7c | -6.44461 | -43.97295 | 2024-10-02 03:28:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68b1e0f0-540d-3805-930d-0ac182d82727 | -6.44364 | -43.97842 | 2024-10-02 03:28:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d9e2109-4ade-3f98-a9c2-fd9a85c2ec71 | -6.25153 | -41.85272 | 2024-10-02 03:28:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a2a9e4f7-b684-3c68-9914-78dec9c13e58 | -6.25086 | -41.85658 | 2024-10-02 03:28:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad56a65c-e7b6-37fd-b69f-c04c56b6bb51 | -6.24521 | -41.85564 | 2024-10-02 03:28:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cfe7cb34-a183-3f84-a908-3c4ade03b2fc | -6.24025 | -41.85083 | 2024-10-02 03:28:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e93ac593-5e24-3a0b-adcf-bc3f9348ef73 | -6.23957 | -41.85474 | 2024-10-02 03:28:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a24b00a5-a7c6-355f-b074-851d7c655bd3 | -6.16237 | -42.90195 | 2024-10-02 03:28:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0103731e-79bc-3cc4-aa81-49252e9d5216 | -6.15705 | -42.89691 | 2024-10-02 03:28:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fc039330-804a-367f-a796-d21c92e0500c | -6.15624 | -42.90146 | 2024-10-02 03:28:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 03ca82a6-6246-3201-8fc1-66261d8d1938 | -6.15533 | -42.90656 | 2024-10-02 03:28:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 402ef687-aba1-3e10-a42f-28d7eb1c48c2 | -6.1491 | -42.90664 | 2024-10-02 03:28:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| db251614-6c0f-3584-8ef2-1f1a5b2aca8a | -6.137 | -37.22652 | 2024-10-02 03:28:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d83852f-c5c1-3eb6-a52f-8bf92ebc918d | -6.08915 | -37.63904 | 2024-10-02 03:28:00 | NPP-375D | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 924c2a26-d0ff-3720-bd17-44d41d3f80f0 | -5.96033 | -43.42878 | 2024-10-02 03:28:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfffcac5-0e40-3868-91b7-8e6c48ecf699 | -5.95102 | -43.26645 | 2024-10-02 03:28:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5b593bf8-c1c8-3314-96b2-0389e83bc949 | -5.94482 | -43.26542 | 2024-10-02 03:28:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 061bb199-9e83-329a-b265-d44b6f50c016 | -5.92235 | -41.97732 | 2024-10-02 03:28:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fca48224-df91-3969-94aa-de1fdf7e5537 | -5.92143 | -41.97956 | 2024-10-02 03:28:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e81cbc8-6c7f-36b1-a12f-279a1b76743f | -5.91594 | -41.98021 | 2024-10-02 03:28:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b2a38694-bd61-3415-90f5-5b5432d601c8 | -5.88237 | -43.71729 | 2024-10-02 03:28:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a4dfe91-1de3-3a05-abf2-0b73500cb940 | -5.8814 | -43.72264 | 2024-10-02 03:28:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f58d3af-ae1e-320c-828c-61752482ce8c | -5.7099 | -43.93664 | 2024-10-02 03:28:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README51.md)
