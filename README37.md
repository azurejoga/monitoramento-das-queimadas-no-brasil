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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6293cfe1-40b5-3f20-adc0-7687d2e63e89 | -3.44142 | -49.25754 | 2026-10-07 04:00:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8525b154-3b18-3fd8-b2a0-fd97b182b873 | -3.30222 | -42.27451 | 2026-10-07 04:00:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9045c8a3-4a5f-3a2f-a8bc-c765deb769ec | -5.74834 | -43.28251 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6031c75c-3277-30ba-9ae1-e5d96c7f7b80 | -5.71978 | -45.15777 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 386e4a63-52df-338e-8950-bf32200cb1a3 | -5.72847 | -45.16906 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d8f4ec8b-26a5-3dc4-b0b1-71ff5b8612cc | -8.44248 | -46.41016 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 76835bc4-89f3-352c-97f4-712eeaf77658 | -8.38709 | -46.2904 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00921601-f242-37be-b9af-1ae0192160c4 | -11.6381 | -43.67231 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36128672-1388-32e2-ba77-4c9f3583ba54 | -11.75051 | -44.93574 | 2026-10-07 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e0ff3b6-fad1-3ea5-821b-119f83d04cd8 | -11.22647 | -45.26146 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e3b1382-3bdd-3f89-8a9c-01125317dd85 | -7.27502 | -45.57341 | 2026-10-07 04:02:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d80181e-0ea9-3150-986a-2bcd175f829e | -11.7758 | -46.69572 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbb41fb8-5ff9-3693-be6d-59447dd5f2cf | -11.06174 | -45.82667 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5712342c-8a68-35c5-9744-364ac88976d3 | -11.00218 | -45.43744 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb59eacd-a36d-3369-94db-aac1d3152bfa | -12.95425 | -42.43062 | 2026-10-07 04:02:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 931cf6ca-e3d2-36b7-acd3-4963b59cd3de | -11.36905 | -46.65075 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b9f0615-c9b6-3242-b360-2a932780d535 | -11.78299 | -46.57533 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2a427a5-e460-36ce-a5a7-08bd0cc6b117 | -8.6921 | -45.22046 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50351b18-98e4-3011-9713-6374359bfe90 | -11.67684 | -43.62175 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 06a18a65-9973-3fad-9774-0270cbbb2242 | -9.26888 | -50.66811 | 2026-10-07 04:02:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e39ab92e-94f3-333a-9292-b411ace9268e | -9.34732 | -45.42741 | 2026-10-07 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aec2a167-9179-364b-ba53-c2a325ea1186 | -11.78954 | -46.70765 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d489bea-2ff2-343d-b254-9fdaafea60aa | -12.16823 | -44.70938 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b80a4a48-b37c-35d3-8873-d53665419058 | -8.4472 | -46.41464 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32c92703-3d03-314c-905a-c3adcbbea8e1 | -11.00737 | -45.44199 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 386e8670-d661-3e91-9958-254387635f5e | -11.73186 | -43.50839 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15bdb526-4179-30c6-9043-6ce47bf4c886 | -8.28148 | -50.27203 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9a1838f8-192f-320e-8025-4d6e1cf3ee8c | -11.73633 | -43.65369 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 971e3a26-aa06-33cc-8e15-07d452957f0f | -8.71192 | -45.1954 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 142143a9-9719-3e9d-a54b-2391f56c5144 | -6.99042 | -43.21283 | 2026-10-07 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eca55ca6-3574-386d-9980-e212f7f8f6ec | -13.00476 | -45.9987 | 2026-10-07 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6110a01f-e384-31f5-9afa-4574b6f9f309 | -11.36829 | -46.71146 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0bfb810-10bf-392e-b436-2afe1ecbb837 | -11.37425 | -46.65162 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43abc330-1cce-313f-89b8-43b8bdc46b2d | -7.82221 | -46.86172 | 2026-10-07 04:02:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a8b75f4-efac-31c7-a456-6741d79d6fa2 | -7.8778 | -44.20825 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 04f949ac-8a7e-3536-b1e1-daf6987e007a | -10.371 | -45.02854 | 2026-10-07 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c48b6ae-ab5e-3957-a971-938fd873b00f | -8.77842 | -47.57835 | 2026-10-07 04:02:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 726d54fb-abad-3916-9572-77b03c9fc271 | -8.33769 | -44.74221 | 2026-10-07 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3cf0580-d606-3c87-9f46-8466afde7648 | -13.75612 | -43.6262 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 477cdd49-31d2-3219-b231-0261569691f8 | -8.5837 | -45.66832 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca547f9a-6c05-3e78-8c2d-52045b6fd4b9 | -12.21687 | -44.70732 | 2026-10-07 04:02:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc091106-c972-3ad1-bfef-f40a77d463f4 | -12.18283 | -44.731 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcfde42c-5cd6-3a25-ad43-74a8c6c3701a | -8.71293 | -45.18983 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ef0ea66f-c295-3455-aacd-190cbe6eaa1a | -13.44796 | -41.31981 | 2026-10-07 04:02:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f83d2d37-bd7a-375f-bafe-affded826fc4 | -10.99967 | -45.42965 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6362a114-e1cb-3585-8cb7-023dca6ce7bf | -11.78438 | -46.70668 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6aa4abe1-6543-367b-99d9-1629652ddbec | -11.33305 | -46.6707 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a50df7e-612c-3948-a982-d7b4ede795ca | -8.71783 | -45.19085 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ce92671b-0c52-3c6b-8b0a-65b79e225eec | -11.73211 | -43.6529 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f86f3ee5-a9c6-3520-8fb8-379495e9ac0f | -7.87564 | -44.19289 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ad149294-5382-36af-94ce-cd251eb57c94 | -7.87377 | -44.21372 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f916ccf2-de64-30ca-9f7c-cda0602af2d9 | -8.28271 | -50.26579 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fd8460c2-b2d4-3c86-8e0a-a8eff4442342 | -11.62315 | -43.65832 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec9467cb-316b-3632-80d6-083c3af23e0c | -11.37818 | -46.68758 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e1dbcfb-b13a-3a9c-adf3-bbcf139b1a0c | -11.23581 | -44.8697 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fd03e15-c4e3-39de-a24a-43af6f1b032d | -13.0278 | -42.67205 | 2026-10-07 04:02:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 71a25c78-2523-3842-b586-173c041cb9cc | -10.85121 | -50.66341 | 2026-10-07 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aa1019c-c465-38ef-91e5-64ec88598fbe | -10.48273 | -50.42551 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fa80874-709e-3255-beae-e80487be25bd | -10.06664 | -36.43042 | 2026-10-07 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3195119f-3fce-3269-88aa-29b2c3c46e90 | -7.98962 | -45.49773 | 2026-10-07 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 787c6d80-7485-37d6-bf4c-27ca6dbd9d29 | -9.81082 | -44.78519 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc6ab962-ce5a-3538-94ab-ba15dc60cccc | -11.3273 | -46.67268 | 2026-10-07 04:02:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d757acd-94bd-387e-95fc-a52a7f1733e3 | -11.61267 | -44.14647 | 2026-10-07 04:02:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 313ebeba-8c23-350a-8d70-c84cec9288a1 | -6.9889 | -43.22152 | 2026-10-07 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8dd462a4-6067-38f6-8ff0-a908b6d043ef | -11.22844 | -44.86689 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f39a83dc-c1db-3f95-98da-a85a445125eb | -6.72933 | -45.80741 | 2026-10-07 04:02:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 335cd6e8-c8c7-3141-9f47-4d53ac334e17 | -12.66987 | -47.49516 | 2026-10-07 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 686c80ad-dfd1-3ad1-9711-6fc1606e55e9 | -8.74551 | -47.87659 | 2026-10-07 04:02:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0fab075d-f6e1-3c72-93bb-204777c63ec2 | -11.77521 | -46.69878 | 2026-10-07 04:02:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5cda62f-2ba7-34ba-98e2-07b61e7ad93c | -11.62245 | -43.66226 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da9e1225-5cf4-3d6e-ad79-38701626e560 | -11.57355 | -48.43927 | 2026-10-07 04:02:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa3493a3-ef92-31c9-b8d8-e6a5469c092a | -7.24966 | -45.25849 | 2026-10-07 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c9d840a-82c9-3354-be54-5e2bea8d3ba6 | -7.87463 | -44.20895 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3e0701e2-0b8a-3c1d-a3a7-6b42f700b065 | -6.93644 | -43.06029 | 2026-10-07 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad8c0a93-c5b7-3565-95f6-622b1b8f5d85 | -11.71234 | -43.42566 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 000464bd-4942-3ab7-af70-3ef230e82e69 | -9.26669 | -45.6431 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5c17f7fa-52ce-3794-9b9e-15d1e4d3fa67 | -8.45249 | -46.41605 | 2026-10-07 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acf86473-4a3c-37ac-bc86-136c7bb37e89 | -13.57921 | -44.42361 | 2026-10-07 04:02:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84e3594c-99ae-3432-804c-7ca85039e0b0 | -10.98327 | -45.4107 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d66e7556-80b0-3f0e-aec5-d69f81062697 | -7.87341 | -44.189 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6008282b-7e27-32ff-85d4-db3515cc639f | -7.60805 | -42.37098 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0cbaa8c6-2789-3b76-9ab9-eb4c1d9f032a | -8.60735 | -45.65416 | 2026-10-07 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 322c92ce-ee11-3266-bb42-dfc19d827971 | -8.03632 | -47.81913 | 2026-10-07 04:02:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 667327ea-4df9-36a9-baaf-ab4edbc12858 | -11.73255 | -43.50455 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 553153f7-aa76-325c-824e-07889ad68066 | -13.6323 | -43.68707 | 2026-10-07 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7c852cf-9420-338a-8fc2-e9ecd791705b | -10.06945 | -36.43453 | 2026-10-07 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6917f504-8fec-3260-9374-70be40454518 | -9.8166 | -44.78827 | 2026-10-07 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea2f4339-4ede-3d20-a160-d69e5912a511 | -11.23306 | -45.25212 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e457d59d-6249-3cd0-ba6f-801d619b7462 | -11.73494 | -43.66153 | 2026-10-07 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 51742a17-c495-31e3-8662-e93c5ed211f3 | -10.99091 | -45.42321 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ac7a786d-b1b4-37ac-93d2-ca7f2dd53aba | -7.87155 | -44.21655 | 2026-10-07 04:02:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 54bfdd53-e38b-39a2-a1c4-f654557ab6b4 | -7.61155 | -42.3755 | 2026-10-07 04:02:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ade55720-c818-3343-a6ce-503ce30a8476 | -12.17834 | -44.73016 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bea4ecf7-d0f2-36ab-9686-7b876bb3e03d | -8.70296 | -45.21674 | 2026-10-07 04:02:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 36022063-66c7-3bde-9cdf-89d2ebb5c5fa | -10.47957 | -50.42531 | 2026-10-07 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bca76e7c-4332-3a8e-bc93-f907f456cec0 | -9.35226 | -45.42835 | 2026-10-07 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe6c36e3-3b23-3cb6-b6a5-2e921a0676ae | -11.10599 | -45.72609 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dad982d9-5aa8-33b0-b2d0-b4b829656d89 | -11.01218 | -45.44285 | 2026-10-07 04:02:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dca6471d-95fe-3f71-a44e-771031e343fa | -12.1674 | -44.71392 | 2026-10-07 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51dd79c0-67c3-35e3-976f-daa8d213f287 | -11.22757 | -44.87178 | 2026-10-07 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README38.md)
