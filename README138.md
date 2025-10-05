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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1683657-d1e2-3751-b4f9-2b66983e9ff1 | -17.96583 | -57.5782 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8eaf19b3-6e70-39da-b6e0-99a870db74ba | -15.35412 | -47.98318 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9986bba5-c594-3644-a66e-2e1c8d3f3a22 | -17.88043 | -57.59571 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 58831a14-0608-3209-b000-b0cbf1066ea4 | -12.98589 | -46.83981 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8300590-8584-38c2-b2e2-3d09bc808ad3 | -17.92948 | -57.60588 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a4b25767-212a-3348-8599-53843a2041f3 | -14.27621 | -45.86264 | 2025-10-05 05:16:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3a4425e-33cb-3177-8623-4146c193a86e | -10.6568 | -58.75574 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5600cdba-0165-3a4b-b488-b6ce3753196d | -12.91662 | -54.72889 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b3dd692-5f74-3c34-abb4-0c1911f0ca12 | -9.90671 | -63.58386 | 2025-10-05 05:16:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9d1031-ebf6-3bf6-aee0-7d62d44a0f9e | -15.60041 | -52.45972 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc0147d9-6f1d-3504-bfc7-30d5ee460445 | -11.51429 | -54.47906 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7eb894ac-a465-3fe0-87a0-3869bc04f2d7 | -15.23183 | -56.85594 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1172e4f3-337d-3532-9d04-feb4f284abd0 | -16.34066 | -51.47139 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b209861c-b50b-3777-a453-8cddf6787ebd | -15.34793 | -56.94634 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60a0fedd-1bc4-3fd0-99dc-051851496117 | -17.91194 | -57.62806 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 32abd273-bbef-3002-bd4d-684d0bd94595 | -11.51422 | -61.93137 | 2025-10-05 05:16:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97b56ff1-5408-3a7f-8b07-3207ebdb0538 | -14.33602 | -47.68872 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cea1ef51-9b9e-3b1a-a51c-5f07978621ed | -12.91516 | -47.31195 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 926dcc29-b2fa-33e1-a219-e5c8b44ed409 | -16.00545 | -50.8511 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d3e4b6d-a3c6-33a4-9893-19e972e0c3e6 | -15.59291 | -52.51579 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88002edd-1e20-3bb3-be01-342498d8b7d5 | -11.83059 | -60.48318 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b00779f0-e436-3c8f-afe5-57cca17c3ae3 | -14.95113 | -46.85094 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 297e5dc2-9616-3258-9c10-edcb7550cab7 | -14.98843 | -49.98283 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 883c16cf-33fe-3996-bf40-ac3865949f68 | -17.86803 | -57.63142 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| d778fa2c-2e1d-32fe-a013-1f30ddf2127d | -12.46168 | -45.50525 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17185657-1960-3658-b790-b3bc9de7d9c4 | -16.12278 | -53.98276 | 2025-10-05 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3fa33e17-2f06-397d-bf8d-6be05cc0ac10 | -13.6865 | -48.05399 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db471679-2b2b-3328-a455-bf53e581ccae | -15.21312 | -56.81306 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c186f1a0-54de-302b-a7c2-c39868fe873f | -12.30909 | -55.1278 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80eb2704-4c68-3ab5-a8fc-9a082ec1bbef | -16.05605 | -50.92569 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d219278a-d74e-3c2c-9086-758147fc24e1 | -18.24954 | -53.35244 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 231caee1-2919-3399-9512-e17186b875b5 | -14.3342 | -47.68671 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3958c50e-0cbc-3ec0-9ac6-e106a8aa58dc | -11.22065 | -54.8631 | 2025-10-05 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35b801c2-5f8b-3493-80b4-08e0f88b499e | -13.734 | -51.27525 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d980b8dd-627b-33c3-9add-544f82c2f4c4 | -18.17133 | -53.35664 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 86cc14e8-d356-3f7c-9dcf-8997e990c358 | -13.09268 | -47.83155 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 57a3539a-a864-3e65-a775-e2ce4e4e8ac1 | -13.08224 | -47.92364 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16472c2b-3b2a-3350-96e5-4601f1860065 | -12.98052 | -51.04161 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf0dcf64-c0be-3829-8cd9-d9234f822913 | -13.34219 | -47.19703 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cac7435-8e63-3869-b060-527e08feeffd | -14.2693 | -45.86188 | 2025-10-05 05:16:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 170bb98e-7dd9-3066-a12c-68f0a384a990 | -12.59336 | -48.13722 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c29c984d-5b7d-36f3-85d6-b100a51753c4 | -18.15911 | -53.33401 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7607161-89e0-30b1-a8b2-2d676613d6bc | -17.88274 | -57.57987 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dc991571-ad91-3913-b5ab-353ceaeb318d | -13.33868 | -48.05797 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb9e8140-1788-3443-ad00-1b1aa8b76d3f | -14.32671 | -47.69819 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf83cb5a-4323-3a98-9489-7f2547598940 | -18.15971 | -53.32922 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c51899dc-be52-379a-a175-3bc53ae44253 | -13.18094 | -50.86744 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f98cf141-38aa-32d1-90a6-ff01956a6af4 | -16.39243 | -52.14942 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0ea132f-380b-3816-9d27-d220c45976de | -11.51032 | -60.45346 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4a40ba3-5cf7-335b-a9d7-3feb4940b27e | -13.17031 | -50.8718 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9b1bf41-2495-32ce-8fa0-c31335f0f4fb | -18.24952 | -53.32985 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5cf64126-6d25-3b7b-944b-4f7fe6436676 | -10.83326 | -57.17941 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0685f93e-e2c0-3b5b-a2bb-f08850616daf | -10.83495 | -57.16853 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c878aead-def0-3f49-89a9-740835a69410 | -15.77667 | -49.09194 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b520227-60c5-388b-9931-1f69600f640c | -11.98725 | -64.11075 | 2025-10-05 05:16:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f2e9a89-d701-3e17-9b4a-257bb5ab7122 | -12.31958 | -55.13395 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3407a8-6a03-383e-8659-585f6e843d86 | -15.20008 | -56.82787 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb4bd54d-1324-35b1-9e98-70216264d547 | -9.90193 | -63.58688 | 2025-10-05 05:16:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbab7a24-2294-3a9e-a6df-7df46df897ee | -16.12331 | -53.97882 | 2025-10-05 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 42484dfb-382d-3abd-ba38-cb53b000adec | -14.92524 | -46.85603 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b349ae9-3bd0-3229-9c27-457557627e93 | -13.25274 | -48.48549 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e4b2d80-6f3d-39cb-93d0-ea73b3ba6590 | -15.23643 | -56.77416 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 729b074f-a897-3b0b-8fb5-1bced0a51127 | -15.78301 | -49.09407 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5086a360-9c65-3524-89fa-da36e0ab007d | -17.70219 | -56.77053 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e3a1b6c7-610a-3e27-977a-d184d1e946dc | -15.13632 | -45.7468 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b2bc4c0-7dd2-3d06-924a-2298d6438b7a | -16.03617 | -51.05017 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed06f66e-9298-3c13-adc7-b066f8f19a2a | -16.06868 | -50.90718 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f4fd8d1-c339-3d65-a314-3d0fd32db2a1 | -15.98468 | -50.91153 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59702266-3c51-39fc-b911-53a45a3ae50e | -18.32478 | -45.88882 | 2025-10-05 05:16:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 0758e88b-8057-3b34-b8f3-76cda44cdbba | -15.72527 | -46.25799 | 2025-10-05 05:16:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68e05f48-c33e-3f11-b9f9-6e2441ce0125 | -12.32506 | -55.14836 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9d23351-4ea2-3ab5-a7ef-826519b82fab | -14.3183 | -47.67873 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb343f2c-4d69-3acd-89a9-ede6b06b5779 | -13.14622 | -47.97156 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f22e1c8-8530-30f4-8809-538245d03624 | -17.95511 | -57.55282 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9e83d28b-363b-37f1-beb2-7bb7fbe861dc | -15.59978 | -52.4978 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12b2617c-b5f3-3521-acba-02c6662c7bb0 | -12.82475 | -46.8702 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3293a464-ab35-3faa-a4e9-da79e0cc1238 | -13.43231 | -47.28047 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 082d5075-62b7-3928-b5f6-448666a01f51 | -12.60936 | -48.12514 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17390b0c-78cc-3959-a88c-038bd218795d | -14.74444 | -54.64726 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb75081b-ada2-3c14-8a77-82ea1ebaa351 | -13.27575 | -47.58947 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a8d2601-2811-37a8-ad1d-07f8331536c4 | -17.96231 | -57.57766 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3f3fb923-c4e0-3298-9c19-5a3ecf90330a | -13.35344 | -48.05904 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 523a52c5-ec47-3936-9da0-9513ba9a6434 | -13.29975 | -47.8113 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e225301-37b2-32d9-92cd-ee5f2df9d5c4 | -12.32135 | -55.1478 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282160f5-2494-3238-9e80-b9aeac0869c5 | -12.26984 | -49.19827 | 2025-10-05 05:16:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82d6585b-2e4d-3099-a735-d3496e0cdbf4 | -15.25893 | -56.76881 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 757218e4-eda3-350f-8757-e414c80b420a | -15.68239 | -46.27155 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82119e0f-c7cd-31ce-87d7-b5d662bb3670 | -14.95235 | -46.85093 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0f3d5c07-1e91-32cb-98ae-ae4664c03745 | -13.25331 | -48.48061 | 2025-10-05 05:16:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| baba23f2-ffc8-3790-8990-29533ca560fd | -15.58558 | -52.50192 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e26ab389-6267-3be5-b6d4-c697f41b9668 | -16.11964 | -53.97427 | 2025-10-05 05:16:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1b5b21ff-49ae-3d8d-bb15-6dabfecac02b | -10.79884 | -69.03922 | 2025-10-05 05:16:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b1a6a8f-b824-31b7-93cf-bca7522b9b57 | -12.30778 | -55.13675 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12a8120b-a3ec-3351-a8ba-872a0b78ffe7 | -14.93904 | -46.83896 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 880b47c0-1945-32b5-8cf3-b45f4947eee5 | -15.91405 | -59.51171 | 2025-10-05 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c47364b-4e9c-301c-8e95-1b8c102220d7 | -13.14235 | -47.98298 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3be0e113-7113-3260-a283-370d4b51dd9c | -14.70016 | -48.35584 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2a2cf46f-275d-31d7-8aa5-30df3ca7257a | -11.76841 | -64.87016 | 2025-10-05 05:16:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e129a925-2e94-3962-bade-47a609acfce4 | -13.75272 | -47.96674 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d8c129f4-bbb5-3d64-ad14-2bff9ea25e62 | -13.1859 | -50.8681 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README139.md)
