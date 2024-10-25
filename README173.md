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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdd3ac0d-a9a6-36cd-ac78-c409a8ffdaa9 | -2.87747 | -44.69573 | 2024-10-25 16:52:00 | NOAA-21 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 108d3a70-7fe2-31d4-87e2-2907b895ae06 | -2.65058 | -44.77417 | 2024-10-25 16:52:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5921a5bf-1b2d-3f3f-9631-d8d00a61435f | -2.6308 | -44.98739 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 22fa54e2-1e7e-3566-9da5-62b8765a0d49 | -2.61262 | -45.15582 | 2024-10-25 16:52:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7da227ac-fd73-3eb7-8128-58f4d1f4c4a6 | -5.11691 | -45.05796 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 84dd727b-d44c-3658-b080-061335705a3b | -4.81955 | -45.09784 | 2024-10-25 16:52:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d2c0c0ea-907d-3d4f-a21f-ebcdf323a4dc | -4.78221 | -45.18752 | 2024-10-25 16:52:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 67fc332d-fd40-3c1c-868d-be05d2205879 | -2.00816 | -48.52689 | 2024-10-25 16:52:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1d28d67e-53cb-3f18-8bbd-ea74b200383d | -4.77078 | -45.11775 | 2024-10-25 16:52:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 680c5ca8-b20d-3698-98e9-be3cf91ece16 | -4.53138 | -44.95415 | 2024-10-25 16:52:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdd45af6-606a-3711-9be7-a36f2719b4e1 | -4.52143 | -45.63616 | 2024-10-25 16:52:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 1c3ca755-1714-3a2a-a465-203d48eb640a | -4.52083 | -45.63251 | 2024-10-25 16:52:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c9b57a94-4560-34f0-86a8-41381fd103e7 | -4.50744 | -45.55045 | 2024-10-25 16:52:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a710aad4-01b4-366b-ab60-61996f95d51e | -4.49464 | -45.96233 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 46811940-a418-3c4a-b1e1-080a5373a236 | -4.45397 | -45.7352 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a20c3d4c-8507-320c-99b1-2b13610207d2 | -4.3846 | -45.66491 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 3f917b41-7bdc-35b1-be4c-dcab920dcada | -4.38384 | -45.66488 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| a25dc5d7-c657-32dc-b106-314bef98d0b9 | -4.38141 | -46.03502 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0ad9de95-991c-36e6-a74e-1c816a4a324e | -4.28591 | -45.83297 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 34d21143-997f-3afc-89c0-27bd85e7c9c0 | -4.26063 | -45.67353 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7a21a95c-6888-3f76-91d8-1c70002b0e5d | -4.26005 | -45.66983 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| baa939bc-f817-375b-9b40-71614f6ed9e4 | -4.24073 | -45.68056 | 2024-10-25 16:52:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 0725c289-1815-3a74-98c7-ea10ef38b6cd | -4.21423 | -45.9288 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d00c1c02-fb5e-3421-bea5-8b1086566475 | -4.21365 | -45.92529 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 94ef2da5-3be3-30ec-b7ee-de26bd669c2a | -4.01312 | -46.02737 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 946dea6f-73b5-3ed2-ba9c-230d0f98d787 | -3.84388 | -45.57973 | 2024-10-25 16:52:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 12782b17-cf53-3cae-8460-e029df7d26c5 | -3.83974 | -45.58043 | 2024-10-25 16:52:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 3d3ef119-e687-3c18-b05d-0bc8464afe29 | -3.7971 | -45.51268 | 2024-10-25 16:52:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36cf78f2-5939-3ae9-8999-9f804b3d21dc | -3.76311 | -45.80195 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 8b82f8d9-0a84-3609-be7d-cc47c4f4195e | -3.75901 | -45.80259 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 657f4104-dc4c-39a9-9661-7fa1483717a0 | -3.75841 | -45.79892 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2453a6c9-4d85-3ae7-b22e-93dccd3fed74 | -3.75519 | -45.79972 | 2024-10-25 16:52:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ff8f608c-0f34-3d90-9c9b-dae89b756276 | -3.67462 | -45.92442 | 2024-10-25 16:52:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9018bcc-9624-359c-adc1-eb6c8afc9d5a | -5.00649 | -45.81992 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a8ef8df2-c22f-39cc-ab3a-4f1aedd2c9fc | -5.00534 | -45.81281 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 797ad9f3-27d6-3ef5-9bb6-1104abae40eb | -5.00451 | -45.29741 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a641ebe-3f6d-3942-8dba-89228c2543f4 | -5.00132 | -45.81341 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 53cf0021-7f80-3385-9596-6e192699ed1f | -4.91938 | -45.28336 | 2024-10-25 16:52:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9a40999-0487-3836-b0d0-014ee2d35b98 | -4.91658 | -45.67875 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f318b2f2-21a4-381f-a86e-1e9c18d22abc | -4.89416 | -45.49118 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9afa2a42-bfec-3e65-8828-bd0335d3038f | -4.89351 | -45.48731 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| edc49540-e4e9-36ff-a3c3-09676f737009 | -4.89108 | -45.49219 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| eaff5e42-0049-3e26-9a54-2b3cb89be7dd | -4.89047 | -45.48834 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 94f66aa2-d61a-3d0e-a625-fb017a1b0b4d | -4.85976 | -45.45478 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70423c61-5e5b-38cd-9638-afb4684fb0d7 | -4.82786 | -45.82905 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2abf20d0-7c80-3e52-841c-d2b6e5709e05 | -4.80718 | -45.98158 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 947dac8e-93af-3ced-8fdf-54ecfc7d0a8b | -4.8066 | -45.97803 | 2024-10-25 16:52:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a87b58bb-60e9-3e65-9ee8-656e189df0ca | -4.79709 | -45.33062 | 2024-10-25 16:52:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 598cf95d-2a9b-32fb-a013-c20d8d074294 | -4.76091 | -45.40895 | 2024-10-25 16:52:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4406ced7-3af7-3254-b113-d8f110d3dd3b | -4.75654 | -45.77161 | 2024-10-25 16:52:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ee7f17e-88e3-3621-b117-cf951b15e2b2 | -4.74529 | -45.67724 | 2024-10-25 16:52:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5b72fd45-6fd4-398a-8942-467c7681d118 | -4.74123 | -45.67797 | 2024-10-25 16:52:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 770d7fc1-682b-3575-a02c-e5cca7f14192 | -4.738 | -45.78496 | 2024-10-25 16:52:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a8c919e1-6a71-3777-b43d-ad9e5dd75d09 | -4.69188 | -45.2723 | 2024-10-25 16:52:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c496b87a-c4cc-3288-9d2f-82f79b9311bc | -4.66219 | -46.03452 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8c10dd8a-10b5-3236-b61a-9ec4448d867f | -4.65999 | -46.03567 | 2024-10-25 16:52:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6f3492ba-f9ed-37ac-ab17-93b7da25b2e7 | -4.25297 | -45.02623 | 2024-10-25 16:52:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d71c1eed-748a-3089-9c2a-c01e67c1c42c | -4.19348 | -44.79499 | 2024-10-25 16:52:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 10919da1-ccad-383d-be70-7f30bdcf1de3 | -4.1067 | -44.73472 | 2024-10-25 16:52:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9b8c0f95-da72-38c3-a411-54c30d024b87 | -3.98978 | -44.62406 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| daab9483-5e45-3966-b794-fdb62ef7a246 | -3.98909 | -44.61973 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f4836cbd-86f5-35c4-b7d2-f18aa995dd2a | -5.76541 | -44.9894 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 16696866-6715-3164-828f-b27dfece8e1c | -3.98885 | -44.62175 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c48ce24e-8455-34db-9103-2db02061e1cc | -3.98537 | -44.62479 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 220e2c9e-9f10-39f4-89d9-c04112ed1dd9 | -3.93008 | -44.75732 | 2024-10-25 16:52:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 59027e9a-253b-35da-a01d-a9ecafece069 | -3.92711 | -44.76659 | 2024-10-25 16:52:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 61ff09c9-962d-385b-9d46-03db76233c29 | -3.91835 | -44.76805 | 2024-10-25 16:52:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 15fbe095-9c04-327e-832f-4fc4b3774d97 | -3.91778 | -44.76741 | 2024-10-25 16:52:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 87403b81-3570-3c30-960a-f2533b56f583 | -3.84195 | -44.97247 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 955d754d-3772-3cd5-91b8-4ee549ed6cb3 | -3.84016 | -44.97774 | 2024-10-25 16:52:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e45edd18-6793-32e3-b61f-6f56898c54f9 | -3.83947 | -44.97362 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6cd9df72-1409-37a4-be63-499844251214 | -3.82083 | -44.86121 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aac28ae1-b0e8-391b-a6c0-61493e1d682a | -3.81981 | -44.8605 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ec676b5b-1172-39b1-ba75-fd6b6cf162be | -3.81647 | -44.8619 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c02bc0ee-b1b5-3aeb-bae0-2acb4c592408 | -3.81577 | -44.85772 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6edf687a-9219-3801-a426-3f37e9f33e38 | -3.81545 | -44.8612 | 2024-10-25 16:52:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 66330564-ea17-35bc-b14e-206f8ae7d71a | -3.80845 | -44.59458 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 38bc655b-2f55-30f8-bc56-c6a19e38c34c | -3.78118 | -44.56762 | 2024-10-25 16:52:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 5fda02d6-7955-3d28-a26c-a5273990197f | -3.75679 | -44.69118 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f5274372-3a72-3e12-b80f-52dcffee4f98 | -3.75027 | -44.67887 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ab482b9c-0b04-34c8-a24b-105fee39eadd | -3.7349 | -44.66801 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 46a91d3a-8aa0-338f-85d8-bb1fb9cf7684 | -3.73469 | -45.04905 | 2024-10-25 16:52:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b74c1e4a-820d-3572-b838-66125a09fe6a | -3.73401 | -45.04495 | 2024-10-25 16:52:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 76c845d2-df1e-3213-8b48-86dcbc7447c9 | -3.73284 | -45.05224 | 2024-10-25 16:52:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 7e5af95b-4d80-346e-9115-d0807a606282 | -3.73219 | -45.04814 | 2024-10-25 16:52:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 827bafc3-ffb6-33a7-8fe2-8301a3897c72 | -3.72605 | -44.66945 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4aaa4740-2c98-3f6e-8ddb-b4b0e6b3fd9f | -3.7172 | -44.67089 | 2024-10-25 16:52:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1ee9ef81-9bfc-3486-94f3-f7bd5a660aea | -3.70572 | -44.9932 | 2024-10-25 16:52:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8004167a-01ee-33bd-b901-29706757c893 | -3.68974 | -45.05925 | 2024-10-25 16:52:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9af3b04a-7efd-3925-b89c-a35da768ef2b | -5.70932 | -45.01444 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 2b205dab-3f14-3a3c-b9c6-1f6874193ea6 | -5.70867 | -45.01056 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9c4525a8-d02c-3308-a8f3-a26bda7b2189 | -5.70385 | -45.00745 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e6ea0add-277d-32a9-99bc-790be0711d80 | -5.64463 | -45.09871 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b3923c4-e7c3-38d3-a16a-e2eec78e6ba0 | -5.45232 | -45.03975 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 57588fb4-0c51-30e7-b6bc-3de0f9d1c8ad | -5.4517 | -45.03588 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8c7a8b73-e084-34c3-9fe0-6d2ac1be1c63 | -5.19288 | -45.20037 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b588a49d-d548-3f9e-96c4-5da568df2b34 | -5.18871 | -45.20105 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e6a9d6d6-8f00-362e-a43c-86777350b127 | -5.13521 | -45.09092 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7d8a6537-9fbb-3ec9-b9cb-99745f4888d4 | -5.13458 | -45.08704 | 2024-10-25 16:52:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 845b92ec-4e04-38f0-ad40-08582acfa3f6 | -5.1306 | -45.11581 | 2024-10-25 16:52:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README174.md)
