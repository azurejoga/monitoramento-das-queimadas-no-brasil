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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25ec370a-f6e3-325c-ba0d-5d599125b34e | -11.7561 | -44.513 | 2024-10-07 03:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 49865f44-0984-389f-ad9b-00e19bbb96eb | -11.7566 | -44.4897 | 2024-10-07 03:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ff85304d-21fa-3551-8337-38c6e8a21355 | -12.1277 | -50.8904 | 2024-10-07 03:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| f438cf78-f2a0-38f3-a6b2-0deff7ed53e2 | -13.7342 | -60.6471 | 2024-10-07 03:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 41e2c629-6356-34b6-8b2b-bba3dfb89093 | -16.4161 | -57.3211 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |
| 47916b57-156d-3d5a-8616-c78d5402d124 | -16.4164 | -57.3006 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| d05c365b-deb7-3eb7-974f-22ad2b441cb5 | -16.4362 | -57.278 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 38751184-4411-31c1-8047-0c65eca1945c | -16.4365 | -57.2575 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 3c7a15f6-ef55-37b2-b4d1-5be7e3351d30 | -16.5072 | -57.7387 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| a9a3d732-e727-3e2f-ac7d-02a970688321 | -16.5075 | -57.7183 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 6e5fadd4-9c9b-3831-852c-0530d5956ec8 | -16.5267 | -57.7365 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 4ef8edf3-60e4-33c4-b6a5-586a7ad0b783 | -16.527 | -57.7161 | 2024-10-07 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 4a7e3de1-8072-3e81-83e5-e3da8ed0e426 | -17.0881 | -56.8328 | 2024-10-07 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| cfe9ed7a-e791-3ca1-8852-11792f033ff7 | -17.1078 | -56.8304 | 2024-10-07 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| be58b3f0-1f8a-3c3f-a4b9-e790a21d37ce | -17.1274 | -56.828 | 2024-10-07 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.4 |
| 83c8da89-a77e-3ad8-b4d7-340601941faf | -17.1278 | -56.8074 | 2024-10-07 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.6 |
| 0838eb75-6da3-3a01-80ad-110a5ca5c258 | -17.1581 | -57.3582 | 2024-10-07 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 998eb3eb-8c71-369b-bb8c-a119740ca830 | -17.1584 | -57.3377 | 2024-10-07 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| caa7f1cf-2ceb-31e7-a2c1-a59707b36c8a | -17.1777 | -57.3559 | 2024-10-07 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 70b0505f-1552-3c71-85f4-273a75b81225 | -18.718 | -57.289 | 2024-10-07 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 47658bb0-fc00-3bc9-9a9d-1c179db0c2b6 | -18.6391 | -57.2578 | 2024-10-07 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 904308f7-95b1-3724-b0f8-0c916556fe79 | -18.659 | -57.2552 | 2024-10-07 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.6 |
| ba881ea0-cf6f-3af8-a43b-d9c197bcbeb5 | -18.7176 | -57.3097 | 2024-10-07 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 8c0f2a73-6978-325e-b75b-99444bc31e68 | -20.5848 | -48.5137 | 2024-10-07 03:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a0d120b1-12c6-3678-a49a-e7138ef473ab | -20.5855 | -48.4904 | 2024-10-07 03:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 31c87bdc-8ee5-33de-9977-ec4f967b3000 | -20.606 | -48.4858 | 2024-10-07 03:27:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 76504a5c-5a5f-352a-81bb-c0b826c697a6 | -21.5691 | -47.7696 | 2024-10-07 03:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6060d782-e62e-3108-932f-44de53e73cec | -21.5698 | -47.746 | 2024-10-07 03:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 5626e6e3-ef86-3e48-befb-b403014daf91 | -21.5705 | -47.7223 | 2024-10-07 03:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a845593e-e649-31d4-9a90-701195493a15 | -21.5906 | -47.7409 | 2024-10-07 03:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 517b1d99-e17e-3162-ac24-8de15ceca7ff | -21.5913 | -47.7172 | 2024-10-07 03:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 187.0 |
| c3e65989-ec53-33fa-beee-811f28de77f9 | -21.605 | -47.9485 | 2024-10-07 03:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 866268d2-545c-3b52-9278-7dfaa0c4ae2f | -21.6121 | -47.7121 | 2024-10-07 03:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e1a45b37-21f3-3736-b653-194dfc9fc020 | -7.71025 | -35.24904 | 2024-10-07 03:34:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6504648-55ee-349b-a6da-7bd8a2df5a66 | -7.47527 | -34.84303 | 2024-10-07 03:34:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 741ce6d4-d6cc-3a8a-a93f-3eec5568637a | -7.37725 | -34.88545 | 2024-10-07 03:34:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 09c50ea2-ace4-31c7-854a-fdceee29f0a7 | -7.10754 | -35.19479 | 2024-10-07 03:34:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 222bab28-8141-3e6a-a79d-9ae1b2901db0 | -6.90767 | -34.91738 | 2024-10-07 03:34:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c11e563a-531b-341e-abcd-58d20986813d | -8.49737 | -35.04985 | 2024-10-07 03:34:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1b588f7d-2b41-3575-ba88-c3f54f3a6f61 | -5.95717 | -38.63113 | 2024-10-07 03:34:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e20219c-4df9-378c-ad5d-85f09828d50c | -5.95573 | -38.63057 | 2024-10-07 03:34:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a466f3e5-dea3-3c6f-8644-ae406a49a830 | -5.95305 | -38.63049 | 2024-10-07 03:34:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1d3f0d9-e068-36e4-96aa-909d75f8f268 | -6.64449 | -38.71773 | 2024-10-07 03:34:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d29ec74-90df-3b69-be14-44dfc8a97ee4 | -7.26928 | -39.18866 | 2024-10-07 03:34:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9deecf0f-0c87-31ca-9c90-a0ff8100ca6d | -7.26924 | -39.19145 | 2024-10-07 03:34:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e945363-a83b-3b9d-84aa-95b101b98b0b | -6.87749 | -39.20682 | 2024-10-07 03:34:00 | NPP-375D | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 52964495-0bda-3672-b87e-f31c241d83bf | -6.87328 | -39.20613 | 2024-10-07 03:34:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 67e4697c-540f-3430-9c9a-22d42b49ce29 | -6.28249 | -41.85646 | 2024-10-07 03:34:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be59c53c-bddd-3086-8689-d44948fa98df | -6.28196 | -41.85945 | 2024-10-07 03:34:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d6cf9ee-988f-36f4-85d2-5f3225cdaa71 | -6.90568 | -41.98294 | 2024-10-07 03:34:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ca2e0de8-9e38-3fd5-b724-3d12f70550a2 | -6.854 | -41.69602 | 2024-10-07 03:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ac4ce202-7ec7-3f98-9212-6a2a801c3da6 | -6.85299 | -41.70174 | 2024-10-07 03:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b0b95df8-7069-33e6-bd95-873fd3ada655 | -6.85197 | -41.70747 | 2024-10-07 03:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a97e4a50-c086-3827-a918-f1d8a6bc38e4 | -6.85059 | -41.68882 | 2024-10-07 03:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 160d9b19-7e0b-3f71-8d2b-adadd2d9b7d5 | -6.85007 | -41.68927 | 2024-10-07 03:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 41ec23bf-4ce0-3a0f-830b-32276b28705f | -6.84564 | -41.68775 | 2024-10-07 03:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6671be87-c9a6-3fb2-b3fe-0339b9d7ee40 | -6.83106 | -41.80389 | 2024-10-07 03:34:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47793a04-c7bd-3a18-ba48-67f63a502d12 | -6.69821 | -40.88482 | 2024-10-07 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 428a56c8-c0dd-3d1f-9359-98ef69b7a747 | -6.69736 | -40.88972 | 2024-10-07 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c22c0a5b-01a8-31c3-b709-3f2a67ff36a8 | -6.65737 | -40.89062 | 2024-10-07 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 799d428d-d7a9-303b-836b-2ea09b558d72 | -6.48119 | -41.95013 | 2024-10-07 03:34:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9b3218a-ae5b-381c-b37e-d5ee80a9c94b | -6.48067 | -41.95305 | 2024-10-07 03:34:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a95a3903-99fb-329f-9f32-0f60a5042460 | -6.47711 | -41.94354 | 2024-10-07 03:34:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aeb8645a-01a6-31fd-840f-cae5ebfa7818 | -3.95158 | -41.49487 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7e6406a-6672-334c-99fe-68bbe2b7539a | -3.95107 | -41.49795 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5eeb2be2-a385-3edc-9312-be7cacecb273 | -3.95056 | -41.50103 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b581d68-b4b6-3123-874c-00edbbd4d89a | -3.94642 | -41.49402 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bfb6973f-ebdd-3805-b8de-85e38b1326ba | -3.9459 | -41.49711 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83da425d-95a9-3296-ba55-42a281a39cef | -3.94539 | -41.50019 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a13c98d-69f4-3507-b52b-9a4480f5c65d | -3.94126 | -41.49312 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a02079d8-d1a2-314e-8a65-49edaa496267 | -3.94075 | -41.4962 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 514d97de-f958-3f5b-9f50-7100fade545c | -3.93611 | -41.49223 | 2024-10-07 03:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 61018b0f-6cfa-31c1-84a8-d007b4ba77dd | -4.80146 | -42.75443 | 2024-10-07 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 720d3d1b-2ad7-3326-a698-290bd64e5507 | -4.79654 | -42.74985 | 2024-10-07 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ea2f0e8b-cf60-3ab2-b7c5-6a103b19c647 | -4.79593 | -42.75342 | 2024-10-07 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c89fa304-b380-38fc-a506-b4c6472e9087 | -4.79529 | -42.75716 | 2024-10-07 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e9fccc17-d698-3963-b876-69e22885361d | -4.79038 | -42.75259 | 2024-10-07 03:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27836bfc-e011-38e1-8593-64f48eec3bb4 | -4.37944 | -43.0401 | 2024-10-07 03:34:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef07a22e-829f-37d4-9c88-3b7f5087ce76 | -6.25969 | -42.52738 | 2024-10-07 03:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a2f675b1-0fdd-3f33-b2a7-8da756a02878 | -7.1447 | -42.63101 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eba45ad1-c17b-3408-a99c-b8d5e8b70639 | -7.14412 | -42.63427 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e15a4287-c2a1-3f25-ad94-c0201e959634 | -7.14354 | -42.63753 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ab13e33b-67db-3f63-b2ce-3acb1dda3908 | -7.14177 | -42.61688 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 67e63dc7-58ee-3a5a-855e-35ba48481db0 | -7.14119 | -42.62014 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5423239d-61b5-30ef-97dd-26698bc94554 | -7.13827 | -42.63652 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc3cea45-0166-3161-aaa9-b3ae78cc7e2f | -7.13769 | -42.63977 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e214f366-b6f5-39e3-b406-5e3f5b423b77 | -7.13766 | -42.60947 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fd0fe770-6bd0-3c1f-bca3-75709368cc7e | -7.13708 | -42.61271 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d687a1f-4e5c-3dea-8024-ad9e99bd0ff4 | -7.13298 | -42.63563 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e57db83-923c-3b61-aba5-cb49c638797d | -7.13239 | -42.63892 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e73bf13a-a956-33fa-bab1-279859bcad2e | -7.12711 | -42.638 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5eb98ad4-6f58-3a04-b6e0-08ef3c6f9242 | -7.12125 | -42.64022 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 00e34739-acad-3e3c-b63c-32de75c9c877 | -7.1154 | -42.64244 | 2024-10-07 03:34:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 20df7058-4c67-3b7d-ba34-c0ec3cb09fe8 | -6.47008 | -43.22009 | 2024-10-07 03:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd720fbe-6b03-3e78-bc53-d8a25efe04e8 | -6.46944 | -43.2238 | 2024-10-07 03:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44324213-e156-3003-9fa9-0438c037bc10 | -6.46858 | -43.22118 | 2024-10-07 03:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b6062a3-f5f1-328c-afe7-887bcc20c878 | -6.46791 | -43.22491 | 2024-10-07 03:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 856ce0ba-86c9-315a-ac46-ff18bed9048c | -6.46452 | -43.21919 | 2024-10-07 03:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfd1849e-6af8-313a-80be-8124697d5ff9 | -6.46389 | -43.22282 | 2024-10-07 03:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06236844-7142-3e22-85c7-96cd15c95605 | -6.46301 | -43.2203 | 2024-10-07 03:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README42.md)
