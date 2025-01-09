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
| c5a58b85-8a64-38d7-ab46-ec968d8c92ad | -8.4276 | -35.30998 | 2025-01-09 03:49:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 832618eb-4d94-3b5d-98cb-15702c26c1d3 | -10.46086 | -36.87506 | 2025-01-09 03:49:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fdbca693-d0e5-3fc1-a20b-eddd4009924c | -10.63386 | -37.05381 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 943fae39-df34-3caa-bd64-1403182634a0 | -7.1381 | -39.9075 | 2025-01-09 03:49:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| aa16726a-d896-3540-bb7e-4ee5df359092 | -10.31148 | -36.7169 | 2025-01-09 03:49:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85c75410-9c57-37bc-9939-8985d3fda93e | -9.56717 | -38.28693 | 2025-01-09 03:49:00 | NOAA-21 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2c784a7-1060-304f-91b8-a8e2f0af4b72 | -10.66012 | -37.01495 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6ab4e8e1-8d9e-3944-8e34-304d1562c57a | -10.9018 | -37.95736 | 2025-01-09 03:49:00 | NOAA-21 | RIACHÃO DO DANTAS | SERGIPE | Brasil | 2805802 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c053496-84cf-3139-86c3-fa927cd652c9 | -9.87335 | -36.27207 | 2025-01-09 03:49:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f789cb25-17d2-3df5-9f18-fb0815a768ea | -9.40112 | -35.68782 | 2025-01-09 03:49:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3af9c94e-f605-3987-aafe-3e212aa971a7 | -11.9692 | -37.87531 | 2025-01-09 03:49:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca2a6f57-ce85-39ac-88dd-b7b7f5df307d | -8.15483 | -35.32731 | 2025-01-09 03:49:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9ea8699-4e6d-3538-af24-d58a65fdbb1e | -10.23851 | -36.6619 | 2025-01-09 03:49:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0bc6d0ff-c67a-33c3-885f-ccad59f2f2d8 | -7.56981 | -39.00873 | 2025-01-09 03:49:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 541d9657-d65a-30ba-9b79-d840ba4b0e1b | -10.63495 | -37.04673 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9294cae-15e6-3c76-8f70-37c593c48e85 | -7.39705 | -42.77713 | 2025-01-09 03:49:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c99d10c-490e-3660-abbb-0463ef331bd1 | -11.61314 | -37.67027 | 2025-01-09 03:49:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b735ca1a-9897-3585-840e-3b7bc1e19529 | -7.82399 | -35.22052 | 2025-01-09 03:49:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9eeb932a-c1f8-3a2f-9f85-b2bea963e81e | -9.36419 | -35.49148 | 2025-01-09 03:49:00 | NOAA-21 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 242e6470-c6ac-3df7-82e4-037749347862 | -8.71119 | -36.16018 | 2025-01-09 03:49:00 | NOAA-21 | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3fd2473e-12fc-3ebd-a2ce-b62f8fc576b1 | -11.12698 | -38.16937 | 2025-01-09 03:49:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5bb3063d-be32-3b1f-92f4-d130e6848b6b | -8.52811 | -35.52688 | 2025-01-09 03:49:00 | NOAA-21 | JOAQUIM NABUCO | PERNAMBUCO | Brasil | 2608206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9e9be923-35c4-34df-8427-09202cc995e7 | -11.97305 | -37.87233 | 2025-01-09 03:49:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 51394964-0528-38f6-8af0-8af4629d4475 | -12.45961 | -38.4799 | 2025-01-09 03:49:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c148f409-626e-3025-8ed0-a6f1daaaee4a | -7.82455 | -35.21678 | 2025-01-09 03:49:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3722db70-2f31-3334-a88d-af4246580829 | -10.63109 | -37.04974 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 315094c7-8b00-307e-bb12-c3e31498f5b7 | -13.35869 | -39.3559 | 2025-01-09 03:49:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 658b1a85-a5ee-3d38-8ee2-bff16696aa6f | -11.31104 | -37.62192 | 2025-01-09 03:49:00 | NOAA-21 | ARAUÁ | SERGIPE | Brasil | 2800407 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5d53647-ed81-33df-b992-be2c873afb5a | -7.8274 | -35.22105 | 2025-01-09 03:49:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 36e34cc9-0f67-3e13-b72e-7cb795f5d8da | -10.08535 | -36.28551 | 2025-01-09 03:49:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d7b63c6-05ab-33ba-888d-bc48e7abae3e | -7.13692 | -38.86079 | 2025-01-09 03:49:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a825ae2-fc49-37f1-93e4-e84b41e2afc0 | -10.23517 | -36.66138 | 2025-01-09 03:49:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 00d918f0-ff10-32b3-8653-de283ba38998 | -10.66066 | -37.01141 | 2025-01-09 03:49:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f5c5f883-d6bd-30a4-9b4f-a112f5906769 | -11.6126 | -37.67377 | 2025-01-09 03:49:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 12735ac9-76d5-3630-be2b-31ca3c66eb92 | -7.64732 | -35.13669 | 2025-01-09 03:49:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7aa6a071-f200-35fb-8c44-5adde958a1cf | -14.99384 | -40.13178 | 2025-01-09 03:51:00 | NOAA-21 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 47b1997f-e79c-3c4b-a4d2-846687363980 | -15.35508 | -39.12886 | 2025-01-09 03:51:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9eb6d880-babc-3c15-9cdf-7efa6fe104fc | -15.35452 | -39.13242 | 2025-01-09 03:51:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08b08ae9-7b6f-304d-954d-898b1b6d9470 | -15.43972 | -39.79712 | 2025-01-09 03:51:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f6de33b4-4e69-344e-8d93-3dc639a37c7a | -19.83366 | -53.92057 | 2025-01-09 03:53:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1196d36e-4c2a-391f-929c-a2b5ff74ea44 | -22.01837 | -49.11671 | 2025-01-09 03:53:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f129971f-3a77-3f94-a601-eb467b6a7831 | -19.56538 | -54.12542 | 2025-01-09 03:53:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 20f5814b-0d6b-3537-9ac5-602c7e35f841 | -19.84028 | -53.9226 | 2025-01-09 03:53:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f301139-9aee-32a3-b927-9bb203f851ad | -22.84991 | -49.38409 | 2025-01-09 03:53:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1a8e668-88a8-3982-a3c1-7a56ba0b0df9 | -22.95421 | -47.08377 | 2025-01-09 03:53:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 529eaf19-7284-3174-b388-a2b8963b3e12 | -22.53873 | -48.81354 | 2025-01-09 03:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1c12965-3c97-3993-9e03-6993794e655a | -29.81096 | -51.2262 | 2025-01-09 03:55:00 | NOAA-21 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| be8b0f88-05e2-3bc1-b0b3-09fcaf07382d | -29.49889 | -51.97977 | 2025-01-09 03:55:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f6e3a4cc-7eb9-3c34-bdcd-1b566fc97d63 | -29.49778 | -51.98456 | 2025-01-09 03:55:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6e90be5b-9532-376d-887c-01ac56a70e4b | -7.56511 | -39.00971 | 2025-01-09 04:14:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a28b36d3-80f1-3d51-beb9-fc0ae5c6288d | -7.68379 | -35.42302 | 2025-01-09 04:14:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d3c805b0-a3d4-3ef5-ab68-2fde260acf1f | -7.64812 | -35.13456 | 2025-01-09 04:14:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4a32d99e-b867-3fb0-8805-3ef3bddd74d8 | -7.39195 | -42.77514 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 20f2b61e-bb0f-3925-bf4a-2e3deadaaf4c | -5.00593 | -37.59921 | 2025-01-09 04:14:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 333c55a5-9f58-3e53-a282-d68fac099ee8 | -4.39852 | -37.8459 | 2025-01-09 04:14:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c454adbd-e2ec-3256-8ed9-33a899130899 | -7.67958 | -35.41644 | 2025-01-09 04:14:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 688084ec-8e4a-36b6-92a5-0cbb5b343c6c | -9.87291 | -36.27004 | 2025-01-09 04:14:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 17003401-0659-3b30-9ee8-46697083c66b | -7.39808 | -42.77972 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 83939ab1-64a8-388f-b421-a6646f7fd2a0 | -5.42442 | -40.6798 | 2025-01-09 04:14:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 77f2e896-00bd-3e1f-b27b-cd6cba465e37 | -4.84363 | -40.04868 | 2025-01-09 04:14:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c157d13-9013-35aa-93c6-17fff6e081db | -8.70994 | -36.16178 | 2025-01-09 04:14:00 | NPP-375D | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f630e9a3-b213-329b-aaba-7194eaddd36f | -10.65916 | -37.01268 | 2025-01-09 04:14:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0105bc70-e20a-38ae-a6ba-1a67a11a0284 | -7.57005 | -39.00877 | 2025-01-09 04:14:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6813fd28-744b-3d91-8248-fce53330a965 | -7.56904 | -39.01027 | 2025-01-09 04:14:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ff112027-c29e-3462-8e4c-16cc7acf13b5 | -4.05434 | -38.79415 | 2025-01-09 04:14:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f20b2d32-99a5-3a19-8d18-826ed8dd0651 | -7.39584 | -42.77216 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6d7cb11-c64d-3fbe-b668-a116d083b56b | -7.56613 | -39.00822 | 2025-01-09 04:14:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5965e489-a336-3d29-882b-c49dae703a7c | -7.39474 | -42.77919 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c90fbd24-155a-33ab-bb12-c70e3ab8d38e | -2.90439 | -40.38248 | 2025-01-09 04:14:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30208afa-70e7-3128-8493-672384aa6875 | -8.70926 | -36.1589 | 2025-01-09 04:14:00 | NPP-375D | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c1f8f31-f75d-355d-9797-60f16a269a0f | -8.52706 | -40.57495 | 2025-01-09 04:14:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 278aa7c2-423f-38bf-ab3b-f61c938f59de | -7.39419 | -42.7827 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5e2e2917-6f8b-3c98-a923-b1e0fe3bddcb | -5.47656 | -37.23347 | 2025-01-09 04:14:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed2cb8b6-ecf2-3024-8516-cae67157317a | -8.65092 | -36.90959 | 2025-01-09 04:14:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 414306df-c25d-308f-89b9-f7de0cffeb2a | -2.88187 | -40.39056 | 2025-01-09 04:14:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d59017e-7f0e-3a4d-a675-2a4b3d178ba8 | -4.39788 | -37.84611 | 2025-01-09 04:14:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff038ee3-b896-3123-b65e-cd98fc81f1ff | -9.39597 | -35.68858 | 2025-01-09 04:14:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 95894a87-cddb-3fb5-95d8-664953cc7d53 | -7.39863 | -42.7762 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 44306083-a868-3153-8aed-a27efc5f535f | -4.33359 | -39.36266 | 2025-01-09 04:14:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00e3a91b-24eb-3207-b2db-061d14571f14 | -10.63615 | -37.11514 | 2025-01-09 04:14:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 260ea810-1325-3597-845c-ee8fe32148f4 | -5.97434 | -37.50764 | 2025-01-09 04:14:00 | NPP-375D | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00f26d06-6b01-3040-b571-b2960494326b | -5.4316 | -40.81848 | 2025-01-09 04:14:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b31645c3-7bf3-3670-a9d2-2eb671080e1d | -7.6788 | -35.4222 | 2025-01-09 04:14:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3a7ab115-40b9-3395-8371-f7313817a8d7 | -7.39529 | -42.77567 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 55789ae5-7c19-3217-9df7-c0189f71a940 | -5.6637 | -35.75755 | 2025-01-09 04:14:00 | NPP-375D | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b8fd312-0d8d-3172-a9fa-f8b53985d9cd | -7.3914 | -42.77866 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 809cce10-f18d-33d3-8c19-1730b8073268 | -10.30953 | -36.71684 | 2025-01-09 04:14:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c4c52d4e-7cc5-35a0-83eb-cab60a49e56e | -2.90381 | -40.38624 | 2025-01-09 04:14:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f8879a0-36db-3c1a-9446-3e802332fd2e | -4.79319 | -40.54472 | 2025-01-09 04:14:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f357597a-8f9a-34ef-aa7f-af6b89e416d4 | -4.39801 | -37.84943 | 2025-01-09 04:14:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 152c565e-8028-3e30-a719-264da841822e | -4.59944 | -37.88308 | 2025-01-09 04:14:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f486c75a-ff5b-33ef-a7f5-6cb98a024e83 | -4.16205 | -42.02171 | 2025-01-09 04:14:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4160f45b-16e9-392d-af40-d151d52abef0 | -4.39734 | -37.84963 | 2025-01-09 04:14:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48358714-2855-345f-866e-726c79047748 | -3.85029 | -41.116 | 2025-01-09 04:14:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 43e0397a-1aeb-371a-a365-b65c1a5753e0 | -4.33726 | -39.3633 | 2025-01-09 04:14:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ffd7614d-2c42-3d85-acdb-435f8e01c9a6 | -10.66385 | -37.01334 | 2025-01-09 04:14:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e1e628f6-0a11-362e-929f-3ebda751e1b9 | -7.3925 | -42.77162 | 2025-01-09 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 97dd226a-79f0-31ad-8cb2-f5cc05f05c76 | -7.68459 | -35.41717 | 2025-01-09 04:14:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c4e5c116-7480-3b46-99f6-f8d129faec3a | -4.84721 | -40.04922 | 2025-01-09 04:14:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9a735c1f-2978-3924-a46d-e88f0e20f38e | -4.1626 | -42.01822 | 2025-01-09 04:14:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README4.md)
