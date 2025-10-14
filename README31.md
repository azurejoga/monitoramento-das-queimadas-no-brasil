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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8d26e33-27ab-37ec-9c24-b4225e642e6c | -7.15722 | -42.50029 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a49836b3-a710-3327-9ca6-8578fc28d2b0 | -13.00306 | -48.77055 | 2025-10-14 04:25:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b5ab2b3-b2fb-311a-8dd3-c641a76499ce | -7.427 | -45.41853 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02a5db8c-84aa-33ad-b604-15bc8b5e4b8a | -7.9305 | -44.11369 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee93edba-113b-3e33-8761-0722c687d8fb | -11.29705 | -44.02505 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed76008-dd9d-3b59-8f78-9c8e5b1cbbdd | -9.49025 | -43.0609 | 2025-10-14 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1f808f5b-41bf-3c39-bb0b-9a4baf227d72 | -9.99097 | -36.3847 | 2025-10-14 04:25:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53435ee9-c51a-3740-a674-65a08dcdf25c | -12.83832 | -50.64169 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e838dfed-f104-373f-9ab4-98c9060b969d | -7.90811 | -45.00948 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 777161cd-171b-3469-b0d1-7fbc863f7fd4 | -12.82471 | -50.63496 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b876fcd0-c508-3e88-ad6a-1367ddbfe7c2 | -12.8369 | -50.65007 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f438f119-7691-3875-bf9a-ac986a8de472 | -7.90194 | -45.00483 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf5f26da-8b25-31cd-afad-780379a9363d | -7.93803 | -44.1109 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b6d156c-10f8-3a59-8179-f7019df465fb | -6.70419 | -45.97911 | 2025-10-14 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4291730b-c09d-3f8c-bf92-24cc890f1670 | -11.74885 | -43.28477 | 2025-10-14 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| be5facee-738b-368d-a571-d4d097dc9b3c | -12.85123 | -50.65261 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 558ef9f5-c7f5-3672-a30a-976d971b7e16 | -7.16068 | -46.52977 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c9458c6-9726-3b1e-b554-153057eb71e5 | -7.30758 | -46.67442 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2bf61ac5-7ef5-3052-b5bd-30fea1df9e18 | -10.82371 | -43.99849 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25eac6ae-2abb-332c-a7e5-a011568cdb55 | -7.1643 | -42.1921 | 2025-10-14 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ca548ff-d90c-3029-bdb9-d282fea280d7 | -7.15658 | -46.53323 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aee64e06-dfe5-3c9e-851e-094590a93096 | -7.35473 | -44.07551 | 2025-10-14 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98186001-222a-3c2f-a43a-38ee2861863b | -8.45158 | -46.20633 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40baa7fb-cd3b-3f19-9b5f-eac3eaf99203 | -7.5326 | -42.69585 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e7e9e45-19b4-3002-8633-00182a141360 | -8.53329 | -44.59013 | 2025-10-14 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fc51bc7-2cf8-3a01-b360-311d2dddbad7 | -7.94896 | -44.13222 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9cbd50c9-bb0c-3742-8d03-1a29ce731009 | -12.81467 | -50.65045 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d81e31c-81ee-306a-9f4f-e1b2093189b6 | -7.9432 | -44.1235 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6d591776-1ff6-36af-8595-2131fd28eb67 | -12.79131 | -50.64784 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b74a11b6-2638-329f-acfe-ad0f09a34e11 | -7.75558 | -44.72611 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 589141b6-e69a-34ec-84fb-8d050d6e4f79 | -12.73538 | -50.6509 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 63c4a626-0329-38a8-bfed-4bf606c9b88e | -12.67825 | -43.39939 | 2025-10-14 04:25:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae90a989-24a8-3f0b-a6b0-daad9306db7f | -11.52521 | -43.51705 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d76c47d2-1333-3daf-b1d4-39446a5f3670 | -7.89969 | -44.99706 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 63e6bc4c-89b0-36a0-8fba-17a6b6918cb2 | -7.624 | -47.8368 | 2025-10-14 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 405a9e8d-6ca9-3a06-aa2c-75c007fdaca3 | -12.81969 | -50.6427 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7d6d10ac-be3c-3ec5-819b-1edd1b529785 | -7.93338 | -44.11806 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 584f9e8f-595c-39e8-9db7-5c1607712cc5 | -8.45887 | -40.55038 | 2025-10-14 04:25:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d72e5aff-4244-3f84-af98-84453eef0ae7 | -7.89913 | -45.00069 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 3b4623a4-ca95-3191-8096-0dd73cb035b3 | -12.82113 | -50.65592 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2a30dfc-2038-3329-9c94-78f12a0c73bb | -7.53563 | -42.70076 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1c48c6bf-896d-33d6-891b-18e45392e140 | -12.81611 | -50.64207 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 76a3e30d-2f3b-382c-819c-628d63b43400 | -12.80392 | -50.64855 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a213a5bd-51af-306b-9811-c0a41b5b4927 | -7.94844 | -44.11248 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 636bd50d-6da8-3d07-91cb-a1a0848215c2 | -7.48739 | -42.15154 | 2025-10-14 04:25:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cbf923c9-38d4-3b79-b3df-65ef2edc0613 | -7.92816 | -44.12905 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8a620ad-7556-3f47-9fb8-b33362e06f83 | -7.92992 | -44.11753 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2569d2c4-686e-3790-b76b-4f05155f4fc5 | -6.53173 | -55.03516 | 2025-10-14 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 144361d2-91ce-331d-b376-2ae67b800548 | -12.26867 | -46.76683 | 2025-10-14 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 137aecc0-d8ef-3b69-8fff-ce48c6cd4bf5 | -12.85981 | -50.6455 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0db3060c-3c27-3391-bbf8-684136d59939 | -7.95361 | -44.12504 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 98705d9f-ed64-36c1-989f-04822d32fc1c | -13.84305 | -42.38983 | 2025-10-14 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c8a534d6-9827-31a5-81e7-e1676a5c4aef | -7.43143 | -45.41202 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9305ea33-b418-31bb-8866-b2f14e2b820f | -8.44986 | -46.174 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3ce1ce3-16bd-3f2c-aa00-ba269741d46f | -11.51951 | -43.52996 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1654ada4-f280-3c1a-92a7-64310a384367 | -11.51408 | -43.51539 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b514b856-c262-3477-ad9d-38cf4bba5edb | -12.81683 | -50.63789 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7bd200f6-2bee-355d-a2ed-eeb8a71b4537 | -7.49121 | -42.15208 | 2025-10-14 04:25:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1de80479-beb2-3fb1-b587-01f990705269 | -8.44153 | -46.14062 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59eb354c-378a-3756-8af1-3154c4285bcf | -6.85149 | -47.63966 | 2025-10-14 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 172e0ec6-ed8e-3033-87a4-89149423b70c | -8.46361 | -46.1512 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc2072e3-b0e7-3f3f-a615-b2be22a2a537 | -10.14217 | -44.55008 | 2025-10-14 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74733560-7b44-395b-b7f1-817098a5e269 | -12.23377 | -49.39097 | 2025-10-14 04:25:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28c1411e-d17a-3e74-bca9-e073399df857 | -7.54406 | -44.28084 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4684f87-7c1f-384f-8972-73ab733994ea | -13.54091 | -43.01123 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 637078d5-fc91-3ae2-969d-463b7df376a5 | -7.69386 | -42.37253 | 2025-10-14 04:25:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| eed22c6c-d36e-338e-abb3-652dac84723a | -13.84451 | -42.38685 | 2025-10-14 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 07750000-1ddf-3f9c-9e94-939cb5d6ed99 | -8.43767 | -46.14358 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6205c95-b9f2-3a34-8d2b-1cf67615eea9 | -8.4339 | -46.18932 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 725e869f-8b92-3f45-8f3d-991117a53913 | -8.08349 | -55.18105 | 2025-10-14 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3c6e66d-e132-39a8-b483-0ffed81bda7f | -10.14159 | -44.55392 | 2025-10-14 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a9936d0-a80b-33d3-8c24-2a88f358272a | -7.6077 | -43.97876 | 2025-10-14 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 187447c1-848a-37ea-a1d0-780f9555bacc | -12.77844 | -50.65854 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2f7d46c-4091-364a-b7d2-19c9b00ab766 | -7.29207 | -41.95825 | 2025-10-14 04:25:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73697198-a1be-31cd-be1f-41f6a25e2dd6 | -12.81396 | -50.63307 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb7a222b-cfdd-312c-b061-e1cc4c113976 | -12.79244 | -50.65084 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2db9b971-0bb8-3a11-b02e-0d716ec30465 | -10.82431 | -43.99434 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f92cdaa-ce33-34c2-b413-e841520b1848 | -7.38542 | -44.01345 | 2025-10-14 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b31a6ac-fb6b-3f76-acfd-4322e4d78f87 | -7.95242 | -44.13274 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f211ebf5-4cbb-3048-b7d2-45e009f02e26 | -12.80966 | -50.63662 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| dd0a2555-27cd-35f7-81d2-22372e720aa2 | -8.45103 | -46.20982 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bd85152-403b-3fb7-89d9-0d728b6af414 | -7.91209 | -47.2115 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d54fea74-ecea-3bcf-9d2a-fce006977a15 | -8.44772 | -46.20929 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ee3a508-7d23-318b-8d48-ff8df45ded26 | -7.93914 | -44.12681 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 150ca6d7-ffb2-3f66-9213-c687a108623b | -12.85481 | -50.65325 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 854d091d-ba88-37b1-ae35-db6093b89098 | -8.4471 | -46.17002 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2658bf79-485c-373b-ae78-f6709f697cab | -11.74441 | -43.28885 | 2025-10-14 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| ed222abd-fc72-31a6-9ca7-dfa89aa52f48 | -7.74901 | -42.44471 | 2025-10-14 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c42f3b73-7fcb-30cd-b369-e728286aad8d | -7.52123 | -46.61285 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47eb52e8-d37d-305b-afd2-864380e2107c | -7.30979 | -46.68187 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6de06b1d-3dd6-32d8-946d-22d03fd2d040 | -8.43674 | -46.23607 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d2bacba-60cc-3673-b086-5143a2152d55 | -7.0862 | -43.70058 | 2025-10-14 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0a274621-316f-358c-91d4-ecd42332ed36 | -7.91044 | -47.20045 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6b23b7b-494f-3f40-9489-0f5787ca1863 | -7.80788 | -46.62628 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d0c3d2f-f094-3d28-9d89-9cf163370a5b | -7.76236 | -44.72717 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71bc27f7-86e7-3d9d-9011-60a1193a5deb | -7.9025 | -45.0012 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec2e81b9-fe64-3096-a590-7e09f0f4812d | -8.11737 | -55.28778 | 2025-10-14 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee26b793-9c16-38c3-9cda-2c862171adc1 | -8.45091 | -46.14565 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd17c3dd-05ab-3853-a5aa-e18db9c6afde | -12.82757 | -50.63979 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c141e7-1ecb-30a2-8b26-39bd551ee680 | -7.16122 | -46.52631 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
