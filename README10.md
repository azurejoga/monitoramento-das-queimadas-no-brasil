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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ddaaa33-d2ea-3d0b-a0f4-6e72d3ef4281 | -5.87653 | -42.87775 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2c357e2b-4042-3b43-864f-0153c38d3319 | -4.91622 | -41.53513 | 2025-10-14 03:36:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c1f705f8-d389-3742-917a-788358623f48 | -7.94056 | -44.12422 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f61b9475-3da8-3b58-97e3-afdcb4295a44 | -5.65166 | -43.60443 | 2025-10-14 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 118aded7-4d7a-32a5-9904-10f4d5f7ef68 | -5.87913 | -42.87646 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7a344d48-578d-3ec8-b914-44769b026da9 | -4.67248 | -43.14421 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| babadec7-b1bf-3466-8e39-002485193fb0 | -4.67137 | -43.12858 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2787928-04e0-3df9-81a3-83d1c5e4ce55 | -5.42501 | -41.33325 | 2025-10-14 03:36:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1ed47ea1-0c01-304b-a904-66b8e72d3f9e | -5.63271 | -42.68718 | 2025-10-14 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a6c6615-6408-33e6-9613-b49f7e284b4a | -11.51422 | -43.51714 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f26f809-cc19-396a-bbbc-c58fc8b556ef | -14.08666 | -44.14064 | 2025-10-14 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c1cfc55-4be6-3910-97b3-3a70233c2d88 | -11.52562 | -43.51289 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40face20-4be6-3e32-a98d-73feec947161 | -13.97877 | -42.50659 | 2025-10-14 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 076e0abb-c93c-3c88-a6f9-2bf4f63e3475 | -11.51481 | -43.51403 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16275eea-7e83-30e9-8f28-7ed92284d15f | -10.82058 | -43.99633 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fb7c3ec-43bf-338c-851a-c863e8372da6 | -12.26803 | -46.7701 | 2025-10-14 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 317d6b95-8290-334d-9deb-38e70dd13d74 | -11.29637 | -44.02741 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 85956728-869d-3631-9fca-a41401d0bc7e | -16.14768 | -43.28303 | 2025-10-14 03:38:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1354968-097e-3bcf-b84d-a6d1c6b05a93 | -15.0511 | -40.84115 | 2025-10-14 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e92976d-d9f4-3c55-a930-ad10af83af35 | -15.49449 | -41.96051 | 2025-10-14 03:38:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f2e13cae-cf51-357a-a93f-807dc3d22334 | -12.85865 | -43.81678 | 2025-10-14 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3332c5b7-0a87-346c-b55c-ea6336e19b83 | -11.29806 | -44.02567 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a7b0f8d-8aaf-3c3c-8c5d-1a0b8158d2d2 | -11.50229 | -43.48191 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78b947fe-fec8-3ab6-9e0f-0bcb2ca466d4 | -12.6358 | -43.44472 | 2025-10-14 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d65a471-40f9-3567-8bee-45e8bc99676e | -14.48306 | -41.45688 | 2025-10-14 03:38:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c8943e3c-fa17-3516-9136-81dc4ff95d06 | -10.81126 | -43.95807 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca2ccaab-3f20-3b3d-aebe-4413af747372 | -15.60973 | -41.37173 | 2025-10-14 03:38:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ec3253d2-6ed7-39c0-8da4-ab135c230424 | -14.0239 | -44.00429 | 2025-10-14 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e282ea08-293e-3b3e-8c30-d9376db35ffc | -13.3872 | -42.71364 | 2025-10-14 03:38:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d8c4795b-a8e6-3306-8bea-665873941ec7 | -13.39338 | -42.7173 | 2025-10-14 03:38:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e1ea226-f06e-3f28-b63d-adc13a549b63 | -12.40331 | -39.24653 | 2025-10-14 03:38:00 | NOAA-21 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4f50d17e-a5ba-3d04-a912-911a46e8ee03 | -10.82658 | -43.99385 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26edbb68-5313-3b28-b02f-18dfccc335c8 | -13.39186 | -42.71467 | 2025-10-14 03:38:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 03e56c3e-8c4a-3c18-8954-ec130f149142 | -16.04853 | -42.45403 | 2025-10-14 03:38:00 | NOAA-21 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09569957-8324-36fd-97bc-f48035ec58f3 | -10.81593 | -43.96255 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5fbdf95-e763-32f8-bce3-774725a3d493 | -11.75053 | -43.28497 | 2025-10-14 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 014218a7-920f-38cd-998a-0489bb3e8d76 | -10.81525 | -43.96612 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba39ff7d-7506-30a4-b8f9-d8b76fab0526 | -13.84484 | -42.38741 | 2025-10-14 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2165ddca-4bb7-3c5c-9520-f073f508085a | -15.03037 | -42.26057 | 2025-10-14 03:38:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25b20fff-39de-33c8-9d30-439a3cd98ca0 | -12.68892 | -38.55535 | 2025-10-14 03:38:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cc8c251d-a6f6-3189-abd5-f83e5a2bc372 | -11.5217 | -43.50572 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c77ecb16-e24a-386b-bdbf-6977f73ed5e2 | -12.26906 | -46.76517 | 2025-10-14 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d85593a4-d8a7-344a-9eca-1788323a2b83 | -11.56291 | -44.05535 | 2025-10-14 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afeaa20c-e28c-32de-b4d0-d65f2c75cbbe | -11.51704 | -43.51651 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72200386-4a66-3842-8fb5-edc19b2332e5 | -10.82449 | -43.97562 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d63207d-f782-3164-bad1-25eb5f1888bd | -12.68526 | -38.5547 | 2025-10-14 03:38:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0bd0f947-77ce-3d15-8d80-d044f09ec836 | -16.08086 | -41.45117 | 2025-10-14 03:38:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 005d7f5c-3e17-36dc-aec6-a49b93fc2bd6 | -13.97844 | -42.50889 | 2025-10-14 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2b1f7979-f187-3cd8-888b-941d15aff64c | -14.47885 | -41.45599 | 2025-10-14 03:38:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 29adcb49-b306-34bf-a9bb-f4dc22717824 | -11.51875 | -43.50721 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0b49a6b-c53d-33fc-8753-6ecc1e35744c | -10.82917 | -43.9801 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce503ef6-6831-3e15-b031-1ff7b8e9ea51 | -13.38872 | -42.71626 | 2025-10-14 03:38:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6085a383-0a1a-33df-8ad2-55b25e97a7f9 | -16.08016 | -41.45494 | 2025-10-14 03:38:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b4d5c304-304e-3a99-b657-48fe806f48a8 | -14.31038 | -44.58567 | 2025-10-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5916983e-cf02-3aac-8e84-268d1d495b60 | -10.8119 | -43.9547 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 712ce84e-c33d-3368-9ff9-508fd5106071 | -16.24355 | -44.05683 | 2025-10-14 03:38:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ad50dd95-b360-37b8-9c00-03ca6e8c72d1 | -14.30519 | -44.58452 | 2025-10-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07cf3b5e-b902-3438-b38e-16903a5ab88a | -12.85577 | -43.81514 | 2025-10-14 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd47ad7b-8dd0-3901-93ce-da68eef2a01d | -15.42206 | -39.13135 | 2025-10-14 03:38:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 80370f62-8a25-3fa6-8a07-599eaa68c5d5 | -11.29743 | -44.02905 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c9be0df-3ff0-31d2-97c9-f5cb65c1b108 | -11.74943 | -43.29092 | 2025-10-14 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 89262959-fc7b-39f2-8965-fda3ca872428 | -10.81986 | -43.97092 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b42a4444-15f0-3f31-a452-8e6365c7be5b | -13.54088 | -43.00499 | 2025-10-14 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 205871fe-9b11-3255-add7-dd89d616b4aa | -11.51934 | -43.51805 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a68c3fe7-280a-3c84-ba51-540dffee2adc | -12.85519 | -43.81822 | 2025-10-14 03:38:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d51fa35-3a21-3ecc-9ca9-24e9047b4a87 | -13.41209 | -43.68999 | 2025-10-14 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbb3a683-43a1-3d9a-9d24-aa70c2b37405 | -10.81657 | -43.95918 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6afb5518-1050-3e5a-98ae-e554e10c761f | -11.74552 | -43.284 | 2025-10-14 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| bbf65068-5f1e-3533-b676-8f293a7107c1 | -13.67305 | -42.85308 | 2025-10-14 03:38:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 044d73b2-07f4-36b4-b79b-19d80b253e62 | -17.28838 | -41.46016 | 2025-10-14 03:38:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ae7c121-39bf-3597-ba5a-affbdf8f755b | -11.74998 | -43.28794 | 2025-10-14 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| dc78b9c6-976f-3651-8a91-7fd17909f8d8 | -11.52327 | -43.52517 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3cef026-7b00-390d-8a2f-da86c5463284 | -10.81992 | -43.99979 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 960c80e3-f0bf-33f1-916b-2d255c9adada | -16.33554 | -41.68227 | 2025-10-14 03:38:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0e3af9a5-1a68-3ae4-af92-8ca7ef1fd82c | -15.05034 | -40.84105 | 2025-10-14 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dd93c0cb-7f89-3e47-97c0-8897382a3b6c | -13.36583 | -43.7149 | 2025-10-14 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6e61a0d-a9be-3ace-a624-f975c532848d | -12.26982 | -46.76831 | 2025-10-14 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb54a21a-5774-3c3a-8c67-1d86e46f9f9a | -14.09174 | -44.14168 | 2025-10-14 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34486442-6f2e-3ac0-9de5-38b5a57d7f4a | -16.89874 | -41.45584 | 2025-10-14 03:38:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 67d087eb-6a9d-3700-a73d-f7b399976970 | -10.82592 | -43.99733 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5595e148-9559-3040-9a94-da5d792555fa | -10.82854 | -43.98346 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5daea14c-abd3-3b92-8577-94257c97dafe | -11.52111 | -43.5088 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b70e4e4-d3c0-3468-ab00-ca3fe83d4b8c | -11.52444 | -43.51902 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5890d45-09e9-3987-978b-500f319e66c9 | -16.91959 | -41.68383 | 2025-10-14 03:38:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e67f6566-331d-365c-b420-b8e479a73410 | -12.63523 | -43.44765 | 2025-10-14 03:38:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f464674-f5f6-3556-ac8b-ba41b51bb00d | -14.14455 | -44.1854 | 2025-10-14 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddd11ef1-da50-3508-9d77-711382f857b1 | -14.09513 | -44.30157 | 2025-10-14 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0ea23c4-e681-3b76-bd62-ff61bb101378 | -10.81918 | -43.97452 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e124593-fc35-3b62-a3cb-387efb8aad0e | -13.97389 | -42.50791 | 2025-10-14 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0f833d12-16d7-3072-8ce0-5a5265062a24 | -11.29212 | -44.02805 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a884b105-f795-3c5a-9f2d-0948544138be | -11.52386 | -43.5221 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56e9f565-2de2-3807-8e05-3a0853fd1bf8 | -14.30973 | -44.58899 | 2025-10-14 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8abde7e5-3e91-3f17-bc27-54da0f547f0c | -15.37517 | -43.03896 | 2025-10-14 03:38:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 20f291ce-3f91-3788-888b-5415ea79bd58 | -14.10026 | -44.30259 | 2025-10-14 03:38:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 013bb689-e59f-3bce-9e04-a6ddb55af242 | -10.82463 | -44.00419 | 2025-10-14 03:38:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4bac477-3368-39af-8af0-463098bd9415 | -11.51659 | -43.50477 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5d35fd1-ecbe-3cf3-87a5-51dda88698af | -16.35255 | -42.38375 | 2025-10-14 03:38:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e249ef6-b1df-3397-a626-2120be81ef9d | -10.73273 | -42.72303 | 2025-10-14 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e5ed08b-2797-363e-b05c-dbc317cc7718 | -15.61206 | -41.37167 | 2025-10-14 03:38:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4d5faf1b-f994-3c9c-b01c-14564ced58ce | -15.31644 | -43.09492 | 2025-10-14 03:38:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README11.md)
