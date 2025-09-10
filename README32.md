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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38c1f90d-0a72-3686-b583-f0c4c0925e59 | -9.07222 | -46.97718 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49b6d54d-27e5-3d5a-a26e-9d6f1297084f | -5.42606 | -45.87961 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6a08843-1e57-3085-bed9-237515b9ce4b | -7.86322 | -46.24894 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 591c94f1-e1c5-3a21-ad37-9f6768dd79f8 | -6.26413 | -43.39562 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0a4fa77-c971-3e2b-8825-59044d5afb78 | -4.49039 | -42.92428 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da7bada2-be46-3990-b1f0-f9786dd88804 | -6.53462 | -44.78278 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 419e4bfe-e462-36d3-a65f-462850a142ee | -6.35054 | -44.85379 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4be47a0-8210-3579-8221-b11ebb2dd7e7 | -6.25374 | -43.41872 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 136b9035-5f37-369c-962a-ba6e9ae370ab | -9.34889 | -46.7562 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 11008d77-e419-3ebd-bd15-f84b7c0407de | -5.58348 | -45.04221 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 04d8a2e5-c659-30eb-876d-375b57ca5161 | -9.70418 | -46.8043 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5a21183-66d6-3e54-befa-4155ee07ec90 | -7.79908 | -46.06857 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39c83ec0-d00e-3f27-bb43-bf785fd47d83 | -9.05266 | -50.47828 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3876dff3-e1be-38bd-9d74-a7f246d3185b | -6.19998 | -43.49802 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29fea088-d8fc-3685-8fd3-fb364ec58a37 | -5.66813 | -43.91517 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e5d57f2-ce55-335f-a47c-b29e928cbdcc | -7.79558 | -46.06805 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a4855a2-801d-3a89-96b1-5661cb878524 | -7.61482 | -42.53799 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20d512ee-8bef-3595-895b-bf12d004ce83 | -6.95623 | -44.80566 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 773409d5-7154-3f14-a027-8a0a25e001b4 | -7.85736 | -46.01838 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5526d97-3981-313e-8f39-19b9126fab73 | -9.31816 | -46.72288 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 57192a22-ba72-3844-8f1f-c43c25969267 | -6.4316 | -44.40057 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b51cd55e-27dc-3027-bde0-6a8db8eaec24 | -7.54763 | -48.2196 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a9b330c-04c0-3f6c-87e5-6e32a38597fa | -7.58084 | -44.7075 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 749e6f4a-369d-31a4-a151-ca53b30a6cb2 | -4.94123 | -37.9632 | 2025-09-10 04:14:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0459a7e7-ee74-33a9-8293-d61f54c2c781 | -6.40843 | -44.44354 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97425c7e-c319-3624-accc-64ce62913936 | -6.19614 | -43.50097 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 62b5f083-6867-33a4-8f16-da379334737a | -7.78611 | -46.05072 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3cec127-fc0e-36cc-a486-0c3cdfe3d3af | -6.45603 | -43.03726 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 812007e1-9406-3fba-8d99-dd5ffd117ada | -5.66398 | -44.91067 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed2ab2e0-4147-31da-a1b5-7c73c8d2dcc6 | -6.41187 | -44.48104 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f621466-0cd5-3eba-ac01-0b8522f35f96 | -8.20857 | -47.15382 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f810a618-932c-3609-857a-b1a3471538af | -5.72672 | -45.41631 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9004366-b864-3135-8dc7-0963928240e3 | -5.4103 | -43.45786 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b686f625-2b41-3dae-952f-d48d77c93d40 | -7.79093 | -47.94015 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e8d51ed-3fc2-3f8c-8ebf-1b2aacb80fcf | -5.74539 | -47.4749 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa4fd31b-a33a-3655-9110-ffa13a69bda2 | -6.52699 | -42.42645 | 2025-09-10 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 886931ef-12c8-3839-bd73-32cbb3026af1 | -6.20415 | -43.4068 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e9a62b8-5bf3-3e79-a04f-2af2954df726 | -5.96565 | -45.79601 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7190dc17-e44e-309c-9d6f-53b2e3d24932 | -9.00584 | -46.06201 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e81c51f-dc53-3eeb-86b6-c38b219b76e7 | -7.54542 | -44.65459 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d49f8526-670b-310f-94f2-0e18d29b1d86 | -6.08463 | -43.34566 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ab0cd0f-e8da-3edf-8202-99ca6d6a0264 | -6.19229 | -43.50393 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 595e41f6-828e-3bc0-8390-7b01bd3a93ed | -5.63862 | -42.62893 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4bd666d-94d8-342f-ba28-dfccd074496f | -5.66757 | -43.89718 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5da7b538-b1a3-3cc8-b62c-475ba5d5c7a4 | -9.21635 | -50.53063 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4002393b-51a7-36d3-9add-0ac5a5dc30ee | -5.71682 | -45.41935 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 846e1bec-62d6-37bb-ad9d-c3b2be3e3d7f | -5.94194 | -45.71947 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ec199aa-02d7-3dab-90c6-a54532c9f7cc | -6.8492 | -47.91397 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c3f652e-afdc-3481-b8cf-6311f155818d | -6.82133 | -52.79934 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95887ca1-d933-3391-a3ff-6ba203747b47 | -6.88537 | -47.88919 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 8586c5c8-9a78-39f4-a77a-c47b5fa307be | -7.5547 | -48.22305 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 252295d8-5384-3f08-a653-15632d929ebd | -8.86373 | -45.8569 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebc21dc2-0720-395a-8fa5-63ae42c44c7d | -9.14752 | -46.0571 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ad32c95-f2de-3ca0-a599-f1f1ea27fa02 | -9.69355 | -46.80267 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 960fa0e0-3515-318f-9cbd-3e21ba9a9ebe | -5.96665 | -45.81232 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb9a8f1b-92e1-3c42-85c2-b91891104911 | -8.05343 | -48.68283 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 15f77893-43c1-318c-8769-72d5200bf5fb | -9.15328 | -45.56354 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8956a2a-d167-3cfb-bea6-b2739b733147 | -4.895 | -42.68507 | 2025-09-10 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d579f5fb-4a8c-3b34-accb-840b554e14f0 | -8.5225 | -51.38384 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 106dd36c-d84f-36e0-87c9-ef4d40cd5e96 | -9.21562 | -50.55168 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bc7c6fb-1749-3a8d-979a-bf231dd74ddc | -8.05038 | -48.70075 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6402dd0f-f4c5-3893-af93-68db5ec00aac | -1.96785 | -48.43422 | 2025-09-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ada5ce7-4c72-3ee8-b10c-8be38d16c209 | -6.88149 | -47.88852 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ceb29456-9a25-3674-af5e-3eaed9f2f539 | -5.2039 | -43.70898 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f39028d-6e5f-3abe-987a-1c3dbdebb9df | -6.87846 | -47.88274 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 61f7c5bf-2c53-37c8-8a9c-4e5be5aad2f8 | -5.8061 | -44.85437 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 756d08be-d80e-3bdb-b29e-c323dbb132f1 | -7.08217 | -43.88337 | 2025-09-10 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a6d9ed-ce66-3f28-86b2-2eec114fcf8c | -5.74698 | -47.46524 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 95ff28a2-2db3-3c98-bb20-5a710bf906be | -9.78866 | -46.00492 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2072f0f1-c719-361f-89cc-6e267f73464f | -8.50145 | -44.7206 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4214526-b226-3a03-ac3c-9c1f57fc6b38 | -7.76361 | -46.07928 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22dcda12-f8fb-3adf-b113-4f7cc5590545 | -5.97354 | -44.71256 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 503c6f2a-8bd7-36fc-9636-187b3b08c778 | -6.16064 | -43.38238 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3dd83c34-218b-3e79-8d7e-8a6a4f0f2049 | -9.0765 | -46.97364 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0385edf-ea98-3310-b849-ba2020f4c142 | -9.38827 | -49.22174 | 2025-09-10 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a50efd33-d8d7-30f3-9b5b-66b2fdedbb73 | -6.31861 | -43.41473 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c2e500c-146c-3c19-aa7e-59b02443e642 | -6.95566 | -44.80925 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5852958-7ec9-3480-911b-345af598889d | -5.0407 | -43.12402 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 710d231e-4758-38f7-a050-63fe6d585707 | -6.21053 | -45.6254 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 114b9303-ecb7-331d-a67a-e77fd9bab725 | -9.78928 | -46.00117 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d77ac464-790d-35ef-b801-6dd7045634b2 | -6.19709 | -42.47149 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 899827a9-8510-3a28-932c-cfe746570cda | -5.77005 | -40.94827 | 2025-09-10 04:14:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 62c38b78-152f-3b30-ba9a-153f705eca1d | -8.20054 | -47.15693 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e9ec0b9-ac87-314d-a8f2-818ddd9862f3 | -6.33821 | -43.54858 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cb1aa1a-d308-389a-8262-cf1a11475a4e | -9.15947 | -45.56832 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10160be4-516e-339c-9584-179a08d143d9 | -7.54764 | -44.66217 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 762dc94a-cce9-395d-a3b6-54f9784a7d25 | -5.044 | -43.12454 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d4b6632-10d8-34b0-b7b0-294e3f2985dc | -5.66813 | -43.89369 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e44cf10-abca-3362-8bb5-aecddd0d66cb | -6.2089 | -43.54897 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df07a7a7-2995-39ee-bdd2-5d1812644a7d | -9.09613 | -45.70213 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dc1a576-9396-3110-8c79-3beb6de52b17 | -6.35705 | -43.0394 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 609f68b4-4895-3c4a-b5bc-9e10943d87ff | -5.73445 | -45.28556 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05f9d336-5a77-3bcd-926a-0834745ab929 | -9.10075 | -46.98296 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 223de737-ddfd-3d9e-af9e-7823ec87e918 | -6.8489 | -47.93957 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 61e4097d-8738-3099-992a-fa16ad5f3405 | -7.70043 | -47.29317 | 2025-09-10 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 69351cfd-2f18-392e-a005-660418b7cdf8 | -5.64407 | -42.61561 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f8369051-a794-3725-9a92-2e4d65d4a6dd | -5.99365 | -43.31733 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6eca8146-885d-3937-aaff-f8e2919b7612 | -8.86495 | -45.84935 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97969dc9-16d8-3c04-bf48-18401726fc8b | -9.45969 | -46.43167 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49453033-c51c-3b8b-951e-a637486f8a58 | -8.07569 | -50.18485 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README33.md)
