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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b679bb9b-976b-33d4-ad61-d9b4dee090d2 | -7.95408 | -44.12853 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6c0391a-d065-3048-ad76-cf759e99dd94 | -7.38675 | -44.00884 | 2025-10-14 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bfd024e3-3682-30e8-b929-0202af9094aa | -5.31532 | -42.90754 | 2025-10-14 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93954498-7829-3f6a-93cd-2a5ef0faa3bd | -7.93987 | -44.12811 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a8dddfa-307b-30fe-b600-dd08469c2f88 | -5.10509 | -43.20197 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 626b0bef-ae18-37e1-9738-0fc6981ba329 | -6.57855 | -43.91394 | 2025-10-14 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a9942627-b022-331c-9f89-87a3d7842e83 | -5.3278 | -45.19347 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995025b2-893c-3824-ac1c-360ae85f1db2 | -6.00016 | -42.8661 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 62062e75-c9c9-3797-82dc-a93b83e8ae27 | -4.80131 | -45.33432 | 2025-10-14 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce6c9a2e-45c1-3906-9146-5fc2b346a363 | -7.15132 | -39.42603 | 2025-10-14 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53456eb4-fd39-310e-aa33-aee8b2b21bbc | -6.33716 | -41.60796 | 2025-10-14 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a4ac3e4-a3de-32a2-9c74-fc700a379845 | -7.8797 | -47.27334 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30f0d499-8023-3081-b6a1-95352cecd503 | -4.75779 | -40.86104 | 2025-10-14 03:36:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 27c025db-e35c-3c01-8deb-8471a05a250d | -7.91428 | -47.19916 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fe7b8e63-b4ed-3fdf-bdb0-fd0821783e8e | -4.84755 | -45.21224 | 2025-10-14 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66ed75c4-d6a1-38ee-9a2c-e5e7025b6d1a | -7.39867 | -39.78875 | 2025-10-14 03:36:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 1d388b98-58cc-3d20-8341-462e2ee5179d | -6.30091 | -42.99786 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 42e60414-4c9c-31bb-848c-f3e757735a66 | -4.65889 | -43.13425 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8dd31434-a893-3e01-89af-2fd079506287 | -5.40374 | -40.88485 | 2025-10-14 03:36:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4993060c-e51e-328d-bae0-f39ed7e699f1 | -5.6381 | -42.68787 | 2025-10-14 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45314564-b04d-3c6a-9821-f409afd62174 | -7.68187 | -42.3773 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ec7a98cd-b224-322c-96d2-6f8f8103181d | -4.84832 | -43.2059 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a6657bd-2c91-3004-887e-50010f42f494 | -5.49053 | -45.40996 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a8fb8e20-eed8-317a-8fca-9dd4b418dd82 | -7.67629 | -42.37935 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8c798aeb-6087-35fa-9d52-b23a42b76b85 | -7.92858 | -44.15849 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16560a68-84ce-3dc0-9ee7-4f4002ae8c23 | -7.20701 | -45.48766 | 2025-10-14 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f55a0d1e-b667-35eb-b032-b7aceffe5719 | -7.68795 | -42.3724 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37d495c6-991e-3b54-89ad-07e37eb98591 | -7.67576 | -42.38234 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73440b42-616e-341f-82e2-3c7650c46bb6 | -6.63669 | -41.72379 | 2025-10-14 03:36:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0c79846c-4635-3239-b67d-b7f70a0649ca | -5.74362 | -40.76994 | 2025-10-14 03:36:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e61013c3-ec25-34eb-921a-d2d19f8a7f46 | -7.95337 | -44.13236 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4a54407-79a8-3685-9314-984ec7dc8e59 | -4.66945 | -43.14004 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9845d0cb-50bf-33f4-9e6f-a31d84a4d7d2 | -4.66577 | -43.12758 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15880792-65ad-3bc2-b812-2d94df2c6f27 | -4.83983 | -42.77218 | 2025-10-14 03:36:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f7cf3158-de3a-3ee3-8c0c-0360b67f4ebc | -5.38523 | -43.22701 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f527b56b-24b6-3a25-be9d-0b52da83bb09 | -5.90277 | -42.8375 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e49f461e-dcee-36cc-b5c2-78adf02737af | -6.16207 | -41.72061 | 2025-10-14 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cf0a8b43-94a1-3bdd-a29f-17b9c10ca0e2 | -7.89857 | -45.00465 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6251be8d-74ce-3abe-9b0c-44086ebee84a | -7.94483 | -44.13303 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da808116-fb3c-3a47-9cd7-46fb70245fcf | -5.88189 | -42.87891 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1365fb6e-119c-3105-afeb-2f38e78ba80d | -10.16765 | -36.39172 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| d8115639-bbd3-3b96-b492-a0de93139ec8 | -5.88909 | -42.91423 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c432ba2-cbb9-3c0a-bb9d-14ab0f14fb0a | -7.64189 | -42.57473 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7c23838e-3877-36cf-a905-b57e99677971 | -4.66329 | -43.13079 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 228f7711-bb31-3634-b941-bc4ab28ebec8 | -6.14874 | -41.76832 | 2025-10-14 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3b8c0800-a0c7-343a-a156-e68fd137a827 | -6.16375 | -43.75667 | 2025-10-14 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c7d13265-323b-34ee-aa4e-9007e2d7dfc5 | -6.25858 | -42.90922 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dca4a67b-8459-3d2c-a796-ff0cda17ae5d | -5.25445 | -45.23846 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04b48b3e-a64d-3c37-be7e-cca676e5092a | -6.29817 | -43.00094 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 406bf3dd-810e-3a96-882c-daefd42b52ca | -5.73891 | -40.76926 | 2025-10-14 03:36:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 3ec0277f-e18e-3d73-80e1-b04024bb4500 | -4.66822 | -43.13558 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a91c3779-d95e-3e48-8d7b-54a793db0a80 | -7.20173 | -45.48135 | 2025-10-14 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1c93340-49d6-3766-b3a9-6bb30a9004a0 | -4.74368 | -45.65708 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 990054b0-29f0-3da6-b5f9-d5eed79688e7 | -6.15321 | -41.77219 | 2025-10-14 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f66dcc0f-23e9-306d-931b-a2e1274c8370 | -5.88247 | -42.87556 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| df1a3be7-07cf-3980-b0ff-7f528620dafe | -10.17168 | -36.38853 | 2025-10-14 03:36:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3eec3809-bf7f-3ff3-8dd5-4c418a4804d2 | -8.22117 | -43.32723 | 2025-10-14 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c9210fb3-42ff-3c0c-bf1a-9ed186ce894c | -5.49834 | -43.06403 | 2025-10-14 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a2ad174-dc57-3a6f-89d8-b7dcb3fa5cae | -7.48917 | -42.15333 | 2025-10-14 03:36:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99feab00-673f-363a-9700-ee24b3472a92 | -4.66687 | -43.14325 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| df9ea81e-875c-323d-a01b-0bdb4ecb0bd2 | -7.75957 | -44.72553 | 2025-10-14 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96b482f3-a7a2-3f79-9012-245ccd044c55 | -7.92854 | -44.12608 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 961aa86d-a63e-365b-b58b-c0bc67dbc500 | -7.16829 | -39.23768 | 2025-10-14 03:36:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f8eb784-3b02-36d5-bbd0-71f3a6e09a12 | -9.93238 | -36.45405 | 2025-10-14 03:36:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0e21811c-98a7-3ca7-84c4-ee0f0fc8ffa3 | -6.22689 | -41.56082 | 2025-10-14 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b757ba21-4e6f-3b60-b6f2-28d8435cd7f0 | -7.68695 | -42.37813 | 2025-10-14 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 57682f02-3e52-3b34-a62a-557a0dd26612 | -7.64244 | -42.57159 | 2025-10-14 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4080b868-28e7-3764-9b74-50ff150da28a | -5.10999 | -43.20686 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0b6589f5-5043-35a4-b244-10802af66fde | -8.50466 | -37.94056 | 2025-10-14 03:36:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0ad9499e-6f2c-314c-beb4-d26e606fc66b | -4.62713 | -45.77832 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b209bd01-9f92-3d2e-a8bc-46ed12be1a1e | -6.29671 | -42.99021 | 2025-10-14 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73a4eef0-50ed-36f1-ae4f-4508365f9229 | -5.87852 | -42.87984 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 62180089-b048-375c-ab1d-ca0c6c35b0ca | -5.977 | -43.56378 | 2025-10-14 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44e89744-4d23-3d97-b147-26b86ddf1f82 | -9.99036 | -36.37867 | 2025-10-14 03:36:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc808a5e-5c2b-3588-b574-30c159d7c557 | -5.11921 | -45.50097 | 2025-10-14 03:36:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cdeb56f-6a2c-3af1-a5f0-ee2bf6702ac0 | -5.64936 | -43.60465 | 2025-10-14 03:36:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c16cf29-afb1-35d8-868c-0b80d82b251f | -7.94353 | -44.12238 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31f4e931-4c80-37c4-ba08-5f550428da7a | -5.9172 | -42.81871 | 2025-10-14 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5a9fbd93-bf93-3666-ba64-5dbd5cdc1c58 | -5.85071 | -46.45124 | 2025-10-14 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 006ef82c-d7bb-3cf2-8f7e-27df9d802a71 | -7.91791 | -44.12019 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e34ed775-5a4a-3894-aeba-50173c870195 | -6.16447 | -43.75268 | 2025-10-14 03:36:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e3e1995a-a574-3525-a106-07ad392f3ed5 | -7.91318 | -47.20498 | 2025-10-14 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 455d72a1-7a16-3823-a38a-db3b411dfc5c | -7.20081 | -45.48634 | 2025-10-14 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e60fc627-c512-34b3-a2b1-515bc61477da | -6.5766 | -43.91442 | 2025-10-14 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a74889d8-ecb8-359c-b0b2-8c435c202e0b | -7.94774 | -44.1312 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bcb44252-1c30-3015-9ed7-6fb4ef44975f | -5.24804 | -45.2377 | 2025-10-14 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc0ae6a8-aa65-3abb-ba74-f13b2a559417 | -7.40172 | -39.78957 | 2025-10-14 03:36:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 24.1 |
| a5be3978-4a1d-3ad8-b8ef-9935adc28ad9 | -4.65824 | -43.13808 | 2025-10-14 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7435ced1-9f5c-32f0-b83e-d39399fd08cb | -8.39114 | -45.05507 | 2025-10-14 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01981532-4571-37c1-ae41-495e2f13f6bc | -7.91943 | -44.12615 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5571f901-faee-3587-b99c-cbee90330285 | -7.94209 | -44.13014 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2b0c7d5-541e-3a41-af8a-b9e6b9e7f3db | -4.80542 | -45.34132 | 2025-10-14 03:36:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d940a57-5d86-36ec-9b84-d1d89a5339b0 | -4.80035 | -45.33962 | 2025-10-14 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a601289-e56d-3f38-a775-67ab976fde32 | -4.62385 | -45.77088 | 2025-10-14 03:36:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42bface5-31aa-3742-af6e-5e4617c85d7d | -4.79983 | -45.33539 | 2025-10-14 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2b75b795-a7a9-308a-9718-e65b25036171 | -7.14675 | -41.71988 | 2025-10-14 03:36:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d74e569f-42db-3e8e-b6ee-aa5d2045f2e5 | -8.45515 | -40.55148 | 2025-10-14 03:36:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb0a88cf-f6c2-3177-989f-2455ac293429 | -5.30985 | -42.90663 | 2025-10-14 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d2c3caa2-b985-3512-b2d7-fcc1c413b6bf | -7.75878 | -44.7298 | 2025-10-14 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3899941a-40d4-37c1-989e-0df16da8d60a | -7.93859 | -44.1175 | 2025-10-14 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
