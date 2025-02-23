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
| 9eadba5d-3f8b-3beb-97a9-bd502661cef3 | -16.65173 | -49.36775 | 2025-02-23 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff610e99-8c2c-3f20-9f37-28d81c9fc898 | -17.34819 | -43.86022 | 2025-02-23 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 080e7345-e9d2-3683-8f39-5d5a6d35dd21 | -17.34866 | -43.86258 | 2025-02-23 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86505dca-8b9a-3a82-8c8e-6a046139e26e | -16.68034 | -43.88634 | 2025-02-23 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bb882c5-9c49-3579-b0cd-05c63006dab1 | -15.55546 | -46.27698 | 2025-02-23 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f91b0aec-1f72-322b-838e-8f6e747b37c2 | -13.62408 | -44.43196 | 2025-02-23 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f4f3f8a-8bde-3901-8dac-fc0115df7ca0 | -20.58338 | -46.38191 | 2025-02-23 03:55:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a08dd46-cb23-33ff-a3e2-191c7d3505ce | -15.04762 | -45.61687 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 343ed6d6-990b-3c38-ae53-56f7d305571a | -7.89212 | -44.19268 | 2025-02-23 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 135c1df1-300d-300c-9752-7e7e6f79b5ab | -15.03953 | -45.61545 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 228569ab-5b08-3185-9772-f12b5e50f219 | -17.67697 | -42.74245 | 2025-02-23 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76d97fee-ed41-396a-b3c4-63c86fcfbb56 | -7.26822 | -44.91125 | 2025-02-23 03:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71168f71-34c0-341e-82d7-38c53bd4ef40 | -16.68105 | -43.88222 | 2025-02-23 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4c48dd3-d7f2-3e11-9b5f-6b50232e75e6 | -15.04357 | -45.61616 | 2025-02-23 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b11e48c-d592-3869-9fad-c7649bdd6c9b | -16.64621 | -49.36941 | 2025-02-23 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0cc2b9c6-6508-30f9-adf6-71985cf18902 | -20.31717 | -46.48966 | 2025-02-23 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27cb7ed5-4e88-304d-af23-d70366d1b276 | -20.31348 | -46.48777 | 2025-02-23 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a586fc1a-c829-3687-8ae3-eb555d6b58ab | -17.34512 | -43.8619 | 2025-02-23 03:55:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56fbab5b-bd26-33f6-a012-858ade0f1f2c | -15.92572 | -47.45577 | 2025-02-23 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 649d2dbd-d6ca-3176-a881-6b2580d94332 | -17.08157 | -39.43256 | 2025-02-23 03:55:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 020c514e-9ce5-3fde-8092-a77e1aa0eb9f | -7.90402 | -39.72646 | 2025-02-23 03:55:00 | NOAA-20 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c24e4907-7c13-3f94-9e47-2a8bcdf0005a | -20.30286 | -46.47964 | 2025-02-23 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a348c370-fd43-325a-a671-762ea1ab2151 | -17.77907 | -42.80342 | 2025-02-23 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b57bee47-66e7-3a86-9382-90531007184c | -20.31251 | -46.493 | 2025-02-23 03:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fbe2881e-5522-3896-9b16-014f9df8af08 | -20.45204 | -40.36778 | 2025-02-23 03:55:00 | NOAA-20 | VILA VELHA | ESPÍRITO SANTO | Brasil | 3205200 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 34f49f8e-b037-37e0-8ea2-4cbad3ddae2f | -17.68036 | -42.74306 | 2025-02-23 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99212602-205f-31d4-8467-a25f1b96e44c | -8.74651 | -38.97759 | 2025-02-23 03:55:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ffa7d974-4ac0-334d-b55a-920ade73f6ee | -17.78182 | -42.80787 | 2025-02-23 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19418eff-cd82-3d06-ad49-4698bb891528 | -20.76292 | -46.76951 | 2025-02-23 03:57:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cf84b6a7-9cb2-3814-a553-4e3d0e112f9d | -22.67559 | -42.85698 | 2025-02-23 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a128f50b-9541-3d93-8251-760f8214a786 | -20.88842 | -46.1585 | 2025-02-23 03:57:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74ecd473-d1fa-3ef9-a9d7-450abdc6bc62 | -22.8359 | -42.5353 | 2025-02-23 03:57:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ba96d2a-ba88-3151-93e0-a9276a35907c | -25.56631 | -49.3665 | 2025-02-23 03:57:00 | NOAA-20 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85e28af2-bb1c-3186-bab9-441f5a24b608 | -20.89885 | -46.1659 | 2025-02-23 03:57:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c568140-3b61-3a33-a07d-640683a2fb0a | -23.98379 | -48.91827 | 2025-02-23 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ccdda42-5757-31e7-b0f9-e301f5e9c635 | -20.76146 | -46.77073 | 2025-02-23 03:57:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| df78718b-8a12-383b-a2c3-543985e63ecd | -20.89228 | -46.15886 | 2025-02-23 03:57:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2175d938-036f-3d3c-a0a3-82975b8e154d | -20.88745 | -46.16369 | 2025-02-23 03:57:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94b96c64-1058-390d-a875-81a83624304e | -20.89408 | -46.17041 | 2025-02-23 03:57:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d718fa01-36ae-3d6b-a93c-d357c138e021 | -21.18186 | -44.27317 | 2025-02-23 03:57:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b540de2-2d96-3fe8-8aba-1afd15e75938 | -23.59298 | -47.43907 | 2025-02-23 03:57:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0f6c52f3-2bbd-39e5-b5fd-0b102038e75e | -29.80962 | -51.34384 | 2025-02-23 03:59:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 72204393-c023-3469-9280-08abad881f19 | -3.02048 | -54.58822 | 2025-02-23 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73511e85-10dc-3fd9-b5ac-63129ef33462 | -3.01123 | -54.57213 | 2025-02-23 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f6f496c-d142-38a3-aedb-7781aa80fd09 | -3.01046 | -54.5769 | 2025-02-23 04:44:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4f8349ba-2c91-3e2f-90a2-ea81646bb3e2 | -1.60013 | -54.5879 | 2025-02-23 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e518b68-0dae-3ab8-97bf-cbae38e8b88b | -13.62056 | -44.43481 | 2025-02-23 04:46:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8f073ff-ac38-3d8f-a487-0d585e183449 | -12.84932 | -43.82819 | 2025-02-23 04:46:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14e84929-a14e-3fe0-bf1d-280aac244ce0 | -12.09669 | -51.22759 | 2025-02-23 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10be3632-383a-3cd0-8d9f-99ac9e1a1dea | -7.86885 | -44.18468 | 2025-02-23 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90938d3c-0633-3819-a9e6-61066808eaf7 | -8.94301 | -50.33939 | 2025-02-23 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b1fb3b4-ab20-34b4-8b5d-5cadd9225750 | -6.95286 | -43.00532 | 2025-02-23 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ed698ff-7827-3e31-b7dc-0a84a566e102 | -10.61198 | -45.10913 | 2025-02-23 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25d6e996-c5da-3843-a867-4d94a9ca08f7 | -12.8442 | -43.82747 | 2025-02-23 04:46:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b43e99ff-2a42-3cfd-8ee6-9d50fa3f120a | -12.10003 | -51.22811 | 2025-02-23 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d643556-935a-337d-ae2b-dd0775eec9a5 | -12.10337 | -51.22863 | 2025-02-23 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab2b8abd-ca63-3ac4-a9dd-45ee4827c92a | -10.48359 | -42.41899 | 2025-02-23 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 21c61a7a-aec4-36e5-8981-eb7c2d0a9e8e | -10.60743 | -45.10854 | 2025-02-23 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8cf5c06e-a43b-3aac-9995-11059a77b900 | -12.32876 | -52.48114 | 2025-02-23 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83f35294-298a-3148-be4e-cc4e3856e046 | -10.4826 | -42.41655 | 2025-02-23 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| db9d048a-455d-3e3e-a63f-b03c6f66f3db | -6.95246 | -43.00819 | 2025-02-23 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3e711b8-9e4b-373a-b062-103b585736fd | -6.95783 | -43.00611 | 2025-02-23 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 80197b4b-3e23-3642-85d5-ab2588239e80 | -10.60805 | -45.10379 | 2025-02-23 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 16d24bb3-8d4b-3042-a2bb-519980c7172a | -13.62552 | -44.43552 | 2025-02-23 04:46:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9685a02c-63c6-3616-a3a3-3397b0e8af4f | -10.48214 | -42.42012 | 2025-02-23 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 889952bf-3f60-387f-af56-763203eaaa1a | -12.10392 | -51.22503 | 2025-02-23 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8fa8023-a44c-3b32-b471-7072972f18bd | -12.09615 | -51.23119 | 2025-02-23 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de0ba24a-c2c6-3dde-be6e-0a912ab259ee | -15.04022 | -45.61626 | 2025-02-23 04:48:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fc29e0e-c724-3b4f-9bcb-b02e0f359da4 | -15.04488 | -45.61701 | 2025-02-23 04:48:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fab7c46-3aa2-3210-b59e-4f7a24f7a0ce | -14.86126 | -52.75032 | 2025-02-23 04:48:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c50198bd-a35c-3b9c-bed8-92ea5116f613 | -15.29012 | -53.20705 | 2025-02-23 04:48:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22380aa7-1e88-3013-9d7c-50de4c478b56 | -15.0455 | -45.61192 | 2025-02-23 04:48:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f610a32d-6cea-38f2-be0d-32b610367468 | -16.02987 | -60.08178 | 2025-02-23 04:48:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4acdcae4-2154-3200-a989-acf1f8465741 | -15.561 | -46.27678 | 2025-02-23 04:48:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f0de3e8-4074-33d8-9083-6355969a8d47 | -19.3013 | -44.50764 | 2025-02-23 04:48:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90a1599e-baf8-3192-b10f-55cf1d7b51f8 | -19.30166 | -44.50419 | 2025-02-23 04:48:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6688f56-3d24-3834-a929-53032761fc17 | -15.29287 | -53.21115 | 2025-02-23 04:48:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dada30f3-ac8e-3109-ad9e-fe5f756729cb | -17.77905 | -42.80925 | 2025-02-23 04:48:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 808e34c3-44ee-39f0-8dc3-1486b4895116 | -16.34878 | -43.69349 | 2025-02-23 04:48:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8792c69-8378-35d1-9ab7-b6e22bfea04b | -13.41882 | -53.37759 | 2025-02-23 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad4b465a-47dc-32c9-bebe-1552c80e9b89 | -16.68017 | -43.88493 | 2025-02-23 04:48:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dcd1cc9-d838-3435-8119-26a70b95b028 | -15.19613 | -47.59168 | 2025-02-23 04:48:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecc8ee75-5ca1-3972-9d4c-d41351b9435e | -15.29068 | -53.20349 | 2025-02-23 04:48:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0523f8e-7e2d-35b4-8596-11e9c3edd23d | -18.41283 | -55.58986 | 2025-02-23 04:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8238e72e-80c7-3062-b286-5ebedf302871 | -18.42025 | -55.58726 | 2025-02-23 04:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 25c6b8d5-981e-303f-897b-dc4e00bc21c3 | -15.19564 | -47.59531 | 2025-02-23 04:48:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa795165-4ea9-3188-a2e0-ede45977f75e | -15.04427 | -45.62212 | 2025-02-23 04:48:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b188561a-4073-34b5-a67f-a3aa2bcc0f65 | -16.34839 | -43.69702 | 2025-02-23 04:48:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 702f588d-16e9-3f5c-b39a-072fad6b123f | -18.48121 | -48.37386 | 2025-02-23 04:48:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4771e4e-a245-36b2-a5ec-a8ead36f2013 | -18.41686 | -55.58665 | 2025-02-23 04:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9700a637-1f4b-33fb-8652-9f4e79548d9c | -18.41623 | -55.59048 | 2025-02-23 04:48:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 01b9ad00-ebd4-357e-bbc0-2a5d48680f71 | -15.53069 | -60.10656 | 2025-02-23 04:48:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eea4b377-3dc4-3c1d-b2da-3424df3c5a29 | -16.65185 | -49.36798 | 2025-02-23 04:48:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a2bc34ec-9b6e-374f-9647-39f02faae56f | -15.5565 | -46.27614 | 2025-02-23 04:48:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bb26cec-c099-3e7a-b258-6218b1c321c3 | -15.08017 | -48.94285 | 2025-02-23 04:48:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cd5b276-1994-3ba2-8e09-147dcd3d382a | -21.37817 | -52.05003 | 2025-02-23 04:50:00 | NOAA-21 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 775ebf3d-4965-3541-86e8-f825dc0c19aa | -20.90153 | -46.16204 | 2025-02-23 04:50:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a706dfa7-6dac-3f94-aa04-ec61139fca78 | -20.76646 | -46.76821 | 2025-02-23 04:50:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 32ad5b5b-712f-3e1a-9e8c-8459377316ae | -20.58578 | -46.38676 | 2025-02-23 04:50:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 31a1d151-1924-3c91-b414-52fdaf71b1cc | -23.5947 | -47.43903 | 2025-02-23 04:50:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
