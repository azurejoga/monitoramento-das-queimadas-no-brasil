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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d0e2bc3-d554-3190-b921-ada332ff03ed | -3.39874 | -42.27927 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| df9573f3-457d-31a2-aee1-e7fe0767ca12 | -3.39822 | -42.28288 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8a60efb-fdd6-3cac-8b8f-0d16282752ce | -3.3977 | -42.28645 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e0253bb-e27f-3493-b4f6-911654a3eb90 | -3.39718 | -42.29004 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b6ce538-6c54-3950-9f29-438bab8838eb | -3.39604 | -42.26276 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b6387ad-43f7-3af6-9716-af77c80650b1 | -3.39547 | -42.26653 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f081c3d-e3ce-3b6b-8ad0-98efa2224e80 | -3.39489 | -42.27028 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3f0dd43-d512-3b7a-997b-8c18650099da | -3.39481 | -42.26733 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 52aab34a-4919-3045-8e83-548fe1f3b26e | -3.39433 | -42.27399 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afe94da1-9005-36ca-9a8c-faaacc99884a | -3.39427 | -42.27109 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 764b9a2a-3567-3911-89c6-1af601544a43 | -3.39377 | -42.27768 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 141e8415-3341-3351-97f6-06ba3e194ab6 | -3.39373 | -42.27481 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| fa537c6a-46e8-362b-affa-da37a5e16654 | -3.39321 | -42.2813 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b36b156b-06e0-3b63-b4b5-50448a10aa6c | -3.3932 | -42.27851 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4c61b4f1-65a1-3c9c-bff3-34f3f2050900 | -3.39268 | -42.2821 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f2dc3d02-cf7f-3c69-9bfb-15af1fdcfd04 | -3.38381 | -42.26873 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5045ca7c-e03d-323b-aa45-ad32b289cc2e | -3.38324 | -42.27246 | 2024-10-03 04:49:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 469bfa4c-0cf9-3862-9cf3-d8ee7587e866 | -3.38268 | -42.27615 | 2024-10-03 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| cf2bc4bd-8d05-3323-a88f-d6db8e56ca72 | -4.81632 | -42.75528 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8158ce89-f808-32bf-aecc-1b963d561ef3 | -4.81583 | -42.75874 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c347083-caa4-3930-932e-50c4a8945b2f | -4.81548 | -42.75575 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c87983fb-4e0e-30b0-a8b1-d6bdf87c362f | -4.81534 | -42.76221 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e490bab2-d5d9-32b7-bb2f-a72a3cc1f61f | -4.81496 | -42.7592 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29fc48cd-ee16-368a-81c1-b3b068ddb38c | -4.81445 | -42.76268 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ceae61f-9d41-325d-b08c-16e9b607413f | -4.81036 | -42.75791 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a3f5f21-46be-3b3b-be3f-f7eb9f145927 | -4.80949 | -42.75839 | 2024-10-03 04:49:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebf0f795-75ea-3625-92af-14203cc82cbb | -4.4907 | -42.87348 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0c446437-9f88-3423-80ef-24f00d46ea03 | -4.49021 | -42.87694 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ccdfbf9-c9c5-35bc-af49-20b80e0ae0f3 | -4.48972 | -42.8804 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8e0b3b4-8c85-3265-a4fd-348a92f2aa44 | -4.48579 | -42.86922 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3737f800-68e7-31a2-b151-eed15cb9aa44 | -4.4853 | -42.87265 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 46a8f901-0f69-3324-9912-6f0c7790efac | -4.48481 | -42.87609 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 1bc00ca0-a56a-3f2d-bd94-5525b037218c | -4.48432 | -42.87954 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6c41dd6e-7bea-350d-be6f-5cc88b6d1830 | -4.47941 | -42.87527 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b800c11a-dc17-30f8-96b6-ba08ed205c70 | -4.47893 | -42.8787 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 67725b6b-ef9c-3aef-85c1-5de5c607df04 | -4.47743 | -42.87902 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b505f02f-af3a-3945-8098-f2be2c569534 | -4.471 | -42.88514 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6135e6e7-7d96-39ea-947c-46393cb9a4ac | -4.46715 | -42.88399 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74317f89-dda0-3101-8c5f-26c31bd26c14 | -4.46666 | -42.88746 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2f1eeac-e4b2-340d-a323-7e7619bc142b | -4.46561 | -42.8843 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbfc6b55-a2b3-358f-8722-34a217019822 | -3.94751 | -41.50863 | 2024-10-03 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9a30aae4-f231-3fa1-a163-83e6e62094d1 | -3.94691 | -41.51279 | 2024-10-03 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1c0c6e7-e5d1-3cfe-a106-a3c7cf432550 | -3.94632 | -41.5169 | 2024-10-03 04:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 45ba0772-cf07-3e94-94c5-fc94d68cef2f | -6.26792 | -42.75418 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 02e7e382-119b-339e-a21d-c8488b213e68 | -6.2674 | -42.75788 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 855aec9d-67d8-3cf1-8fc4-7a2b24bf925f | -6.17259 | -42.91764 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5be77059-ebf3-3f5b-b8d5-39bc824b04ce | -6.1721 | -42.92104 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0bed4c7f-0069-3aa4-9a85-a15331890688 | -6.17127 | -42.91991 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ba56ab65-3279-3109-8cea-5e938e39ffea | -6.1611 | -42.91921 | 2024-10-03 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0dbfdd24-1d1c-301f-b96b-11219a756a2a | -6.15541 | -42.47133 | 2024-10-03 04:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5363f9a6-9f7e-361e-b75e-3f0367bc98b7 | -6.02193 | -43.19634 | 2024-10-03 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e6623014-e5c0-3609-ab7b-9c746c279637 | -5.92525 | -42.8421 | 2024-10-03 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5a20f320-2321-304d-9e9e-4abd5dabf4b4 | -5.92475 | -42.84562 | 2024-10-03 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5fc3729b-3b85-3df4-87fd-803ec0ebdd9d | -5.92426 | -42.84911 | 2024-10-03 04:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7da591da-4156-32c8-9ace-549a449d98df | -5.57267 | -43.10969 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b07c0280-5ce4-32c0-83d1-1588ac6cacb4 | -5.56726 | -43.10897 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7025c285-5b83-3e1e-92b3-03d27095082f | -5.56677 | -43.11243 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f88f72c2-662f-3f8b-a15f-ab7a66c59da9 | -5.56135 | -43.11176 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bf545ccd-b86f-3acb-9551-bd92c9deb3f7 | -5.53658 | -42.77762 | 2024-10-03 04:49:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1facbeeb-2ece-3683-bd83-798d864d666b | -5.53107 | -42.77674 | 2024-10-03 04:49:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25574837-b3f0-3b4e-bc10-8b1a672c8586 | -5.52557 | -42.77578 | 2024-10-03 04:49:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| afbe27b1-c3f7-3fa6-b74f-1158e774f9d7 | -5.52506 | -42.77938 | 2024-10-03 04:49:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 072eef24-db3f-3c19-ad40-479191376618 | -5.40996 | -42.92022 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2d56b06e-2b86-37e1-8f05-5c7dec9e13aa | -5.40948 | -42.92372 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e712bf9-824d-31b6-9139-daa48416eec8 | -5.4088 | -42.92079 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4475126-b750-3028-8c9e-e13b6dfdfb3b | -5.40829 | -42.92429 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a9784649-8b1d-3b1f-a05b-bc4a9d6d0e66 | -5.40334 | -42.92001 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7eed6554-d464-3e1a-aecb-0e5f6b85b735 | -5.31889 | -42.96634 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 44334cad-7b67-3f33-80b1-7673bdd94eec | -5.3184 | -42.96988 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a0763a14-fbe2-36c7-87c3-29cc9f3b43ab | -5.31801 | -42.96693 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e959c5bd-23a0-386f-8493-65ad94ef73de | -5.31749 | -42.97047 | 2024-10-03 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4441c070-fdf2-3e8d-8e78-d6423b2ee1a0 | -5.88308 | -43.42909 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0fc1497f-c86f-3465-a346-34a70351edeb | -5.88033 | -43.42563 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2589e061-a0f3-38af-b08f-957ab1e0fa63 | -5.87985 | -43.42894 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9014722e-8310-385b-892c-3d65cb49e750 | -5.87938 | -43.4322 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da7c447c-f049-3d78-8c66-7bad867c483d | -5.8782 | -43.42516 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24118795-0677-3c6f-85e1-e2c593086b4b | -5.87774 | -43.42847 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b004001-19be-3bfd-a3e4-b776c5b005f0 | -5.87729 | -43.43174 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b02d258-ce67-37b2-8d36-968e310b65d9 | -5.87406 | -43.4315 | 2024-10-03 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa2e5f47-cab1-3c7a-96a5-834c925bc44b | -5.39866 | -43.10418 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0c5ef3b-ec17-37a2-8ed5-73d5f58a660e | -5.39815 | -43.10765 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2faa7a3b-2b0e-332f-bd61-2aa5f8a007f7 | -5.39765 | -43.11108 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13525529-249d-3fc4-8fe4-f5d9d0d50cb0 | -5.39574 | -43.1033 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f680f48a-ae27-38de-bdc3-37cbe8b9fcc1 | -5.39526 | -43.10675 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0123f73-4de3-3f21-9e36-bead701f0b59 | -5.39479 | -43.11018 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3528f224-221d-3869-bc44-5b8fd94e6bc5 | -5.39328 | -43.10336 | 2024-10-03 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6b8ee9a-8446-3fe8-b4f4-4d2dd051477c | -7.86481 | -43.09745 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f4395161-f689-32fd-9ac1-d24b15175f9e | -7.86108 | -43.08259 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e9a0827c-396b-3b58-963b-26bd3c3e849d | -7.86059 | -43.08626 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 36eadc3b-65b2-31c6-af4e-daab69028e65 | -7.85919 | -43.09695 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 85c3accd-5a63-3858-a9bb-6b900ecc99cc | -7.85871 | -43.10054 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 350c2b10-7e27-3902-a5ea-679b6c18f5c7 | -7.85823 | -43.07994 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9b36dfd-47fa-3a67-81fe-2fff6a222657 | -7.85772 | -43.0836 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eb768f21-5703-32aa-a18a-b7d1c724d580 | -7.85593 | -43.07841 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 99755015-88f7-3b92-862b-29f46f975fdc | -7.81757 | -43.08549 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34e4f471-9b51-3735-98cd-2b491aa39099 | -7.81709 | -43.08903 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e24ce98-87e1-3d7e-a24a-180813b85b62 | -7.81196 | -43.08487 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ead858d9-c715-3ede-926a-022a8738c46d | -7.81147 | -43.08843 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d5b8def8-27bb-3b99-9060-60cd2566aa13 | -7.80636 | -43.08414 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1cb07c1a-0b36-3747-a3ae-8e97989c91de | -7.80587 | -43.08775 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README112.md)
