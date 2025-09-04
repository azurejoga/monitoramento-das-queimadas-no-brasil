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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e7c0908-37f3-3b01-8c40-7c6328f6e48f | -6.84265 | -46.39698 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ace2f848-2236-3e30-b0dd-b8a82fc229b5 | -6.02729 | -46.6596 | 2025-09-04 05:53:00 | AQUA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 418089f7-b451-3989-a9a3-f0ecc6e78bd1 | -5.8844 | -51.93833 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| eb3ffc8c-3939-3ba4-89f3-e8c4abdfeee7 | -6.33037 | -45.67699 | 2025-09-04 05:53:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| de6a2371-cbbd-360d-a1f0-1a9267c7c6f9 | -5.69672 | -45.17032 | 2025-09-04 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| cb8b690f-2c32-397c-92da-687fdd547ad6 | -6.32159 | -45.67569 | 2025-09-04 05:53:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 71a45ef5-1ab1-33c3-96e6-3365d9cb6b54 | -4.98695 | -49.90283 | 2025-09-04 05:53:00 | AQUA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 55708541-0d12-3949-be48-53d428b86cde | -5.68632 | -45.60133 | 2025-09-04 05:53:00 | AQUA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4d6acb15-4463-39ff-91e8-33b2fa72c81c | -6.2968 | -43.58915 | 2025-09-04 05:53:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 41b822dd-aadd-3ebe-8593-264ac488dccf | -4.88813 | -43.05472 | 2025-09-04 05:53:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7f8bf80d-b94b-3902-9f55-5913f959e959 | -5.60572 | -45.02634 | 2025-09-04 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| daac8bc0-36e4-397a-a5b2-66d48f5cab87 | -6.16018 | -43.32324 | 2025-09-04 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9a882ceb-20e8-3ae8-902c-1571d116564f | -6.77777 | -44.09285 | 2025-09-04 05:53:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a61c3c62-b0a6-3da2-b5d9-1a8f2189eeb2 | -4.88426 | -43.04853 | 2025-09-04 05:53:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7c9eacaf-f345-374f-8f83-1a560e303a3d | -6.2634 | -43.57866 | 2025-09-04 05:53:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1200dc98-0903-362c-babd-7e202cea29e6 | -8.52507 | -51.30268 | 2025-09-04 05:53:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 4373130b-c955-3322-9407-b1e0aca32528 | -6.69109 | -48.4078 | 2025-09-04 05:53:00 | AQUA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c0c28c7f-9118-33dd-8001-8cdb04ed94c3 | -6.54565 | -43.91145 | 2025-09-04 05:53:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f7830303-d438-3a34-9863-e31df45a4585 | -7.7143 | -50.31529 | 2025-09-04 05:53:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 1465a18f-9aa8-3514-a617-3808e3f76098 | -2.95885 | -49.35635 | 2025-09-04 05:53:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 73b9e407-722c-3354-b686-3d877a4cfbaf | -6.22508 | -42.43402 | 2025-09-04 05:53:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| cd2a896b-9824-328a-ad9e-8ae8dac42b1b | -6.77919 | -44.08298 | 2025-09-04 05:53:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 6be66678-d8a7-35a1-8f9c-e07c05ded895 | -4.88963 | -43.04422 | 2025-09-04 05:53:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| dcc7a55e-9c25-35e3-a91b-6f2bcf319710 | -7.70796 | -50.28764 | 2025-09-04 05:53:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 23163926-0512-3859-b182-d0f072f5fd3b | -6.48948 | -44.10387 | 2025-09-04 05:53:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 99bc2043-b543-3700-9ee6-2839df5a4b8b | -6.1617 | -43.31261 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 22.5 |
| abfcea18-4029-3d65-a2ed-31a23a84928f | -7.71221 | -50.3284 | 2025-09-04 05:53:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a9c02a42-c60a-3181-8d84-211fc600df48 | -7.93623 | -44.95071 | 2025-09-04 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6c62d9cf-cd9b-384f-a080-f5f800e0e40a | -6.7807 | -44.45744 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b39a39f3-aa34-349b-a771-59d5090e866e | -6.22542 | -43.3717 | 2025-09-04 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9b8970e7-ffd3-3174-b5fb-d8cec6b97ee2 | -8.02715 | -45.39199 | 2025-09-04 05:53:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 55fa5174-8f84-32df-8e60-7717fce99beb | -7.55486 | -45.71833 | 2025-09-04 05:53:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f3eab9c-f3c6-355b-96e5-6c8cdbce7120 | -5.69804 | -45.16144 | 2025-09-04 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c7e1b82e-af8f-3146-a119-166ab2729fae | -6.78845 | -44.08433 | 2025-09-04 05:53:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f5f7115e-0baa-3252-ae40-2da91a9d5778 | -6.23499 | -43.37301 | 2025-09-04 05:53:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c7d0a31-e84a-3a1c-adfe-e159aa5a4236 | -5.69935 | -45.15256 | 2025-09-04 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8748f928-805f-37bf-9006-85f4dfb0c7e8 | -6.2792 | -43.84389 | 2025-09-04 05:53:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4450f085-32fa-3d9a-8f4c-0a193afa94c7 | -7.03759 | -43.26295 | 2025-09-04 05:53:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 23cbffc1-6cfd-3ba0-897d-e73db13cbb06 | -8.07947 | -45.35899 | 2025-09-04 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 540254f0-40ad-3548-bb42-4204e07c3832 | -8.02983 | -45.37389 | 2025-09-04 05:53:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 41b6f9ad-f495-36b4-a36c-fa5f97515966 | -5.70687 | -45.16275 | 2025-09-04 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 00d38f51-063c-37c2-a32e-6608841acfc8 | -4.95613 | -42.06982 | 2025-09-04 05:53:00 | AQUA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 60cf8313-72d1-32eb-b4b6-f29be41ad3e7 | -7.74383 | -48.77092 | 2025-09-04 05:53:00 | AQUA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ee644dd-5275-35a3-bbf2-170149720c0d | -7.69484 | -48.73621 | 2025-09-04 05:53:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 06ce0146-3a32-3c33-b34c-87dd6bc75b0b | -6.26189 | -43.58892 | 2025-09-04 05:53:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| de324d6c-48b6-3375-a966-848580c64a91 | -6.79259 | -44.43986 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 280c6a31-f529-3741-9676-17b594d658a1 | -7.07628 | -46.19263 | 2025-09-04 05:53:00 | AQUA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b3bc6d1e-cc72-3654-8408-ef57df0a0ab2 | -7.67753 | -48.72311 | 2025-09-04 05:53:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 638dc84b-cbfb-3dde-818a-03095ccd209d | -6.00091 | -46.57737 | 2025-09-04 05:53:00 | AQUA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1d378b4c-0f94-39e1-a4af-37011703da8c | -8.0808 | -45.34995 | 2025-09-04 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0678d289-c593-373e-a7a5-64c5da79511a | -9.43577 | -46.79397 | 2025-09-04 05:53:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ed79ee9d-e10f-32be-b8e3-6dee75d520a9 | -6.87402 | -45.5688 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eeb8f68e-0f47-30eb-8724-0852afaa33c1 | -6.67393 | -48.39462 | 2025-09-04 05:53:00 | AQUA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 00cb1aab-b645-3ba2-a285-3119274c0a1f | -7.97788 | -46.34364 | 2025-09-04 05:53:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 07c3bd9a-e969-349a-b201-7daeef36db12 | -5.98003 | -44.12137 | 2025-09-04 05:53:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 57bd3d9e-615e-38a6-a9e3-1064bc4539ed | -5.89246 | -44.34408 | 2025-09-04 05:53:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c20292a4-5319-3a78-ae4e-5a6608186553 | -8.02665 | -44.14091 | 2025-09-04 05:53:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3ef43311-654c-3d9d-8645-4b1f29654bcc | -6.25672 | -43.28944 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5ef71b61-ff58-347a-bdf2-3644759cdde1 | -7.68699 | -48.72453 | 2025-09-04 05:53:00 | AQUA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 35.5 |
| e6d02c4f-738f-3913-8e14-fd1698ca560e | -8.07188 | -45.34875 | 2025-09-04 05:53:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3a51ae0d-5a37-31bb-8c38-d6781f558089 | -5.69139 | -45.93993 | 2025-09-04 05:53:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5d3bb545-5223-3333-8e23-6aae3bf6f0c0 | -8.03605 | -45.39325 | 2025-09-04 05:53:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1ac24e71-e78b-3614-b3a1-cbe868a19b85 | -7.93757 | -44.9415 | 2025-09-04 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 62080611-5386-3d82-bb0a-04215a77b7a7 | -8.53257 | -51.32534 | 2025-09-04 05:53:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a35583e6-b5d5-3461-ae24-ec79290a601b | -6.68173 | -48.40615 | 2025-09-04 05:53:00 | AQUA_M-M | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 990c795f-6100-3476-847f-888647ae43a3 | -8.01653 | -44.78025 | 2025-09-04 05:53:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1aad1e00-1273-3bbc-92b9-95d637e32b74 | -6.77515 | -44.49503 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 68b71d5b-46c0-3399-ae47-fe1112e4a947 | -6.78979 | -44.45877 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1dfebfaf-8a37-3334-9e4c-063b306969b3 | -5.90099 | -44.16152 | 2025-09-04 05:53:00 | AQUA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f644d1a-d3f3-3fdc-926c-82540b1f46e2 | -6.33916 | -45.67831 | 2025-09-04 05:53:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5da5f97d-d48a-3d72-9e26-2793a1e28f87 | -6.41224 | -43.2632 | 2025-09-04 05:53:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c306cc94-55f6-3e86-b283-cb554ac8371e | -7.70384 | -50.31336 | 2025-09-04 05:53:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 40ff45b4-41f7-3b1f-98bb-a6bcb06f0f2d | -8.0374 | -45.38416 | 2025-09-04 05:53:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 41977510-2f8b-3af1-a094-650fbc3f8478 | -5.24881 | -44.45039 | 2025-09-04 05:53:00 | AQUA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99219403-638b-3419-81cf-fb25b398edbe | -5.70555 | -45.17162 | 2025-09-04 05:53:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6df5e068-f42d-3199-a331-a9b396e11fff | -7.93891 | -44.93223 | 2025-09-04 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| efd1019d-5516-3c77-8ff0-252bff450b40 | -8.07321 | -45.33972 | 2025-09-04 05:53:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5a8f4ed5-e29d-3280-99ab-229568659d38 | -6.8727 | -45.57764 | 2025-09-04 05:53:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8e3f47ea-5f1f-3fd7-94c6-ef31042fb348 | -8.02849 | -45.38294 | 2025-09-04 05:53:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f21bc02d-fdd5-3fa3-8780-cd6b5496a358 | -8.89621 | -45.82056 | 2025-09-04 05:53:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1f24ad74-1be3-3b39-a01f-3449bc34a647 | -2.96085 | -49.34337 | 2025-09-04 05:53:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d1ce75b0-9799-3c1e-96f1-93ae7f23ae00 | -11.73123 | -47.74242 | 2025-09-04 05:55:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f907a939-33eb-3222-be23-31ba9929cb52 | -14.78698 | -48.13486 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 423000dd-0f0c-36fc-a827-0802bdc7ec29 | -13.56862 | -48.13081 | 2025-09-04 05:55:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5829728a-0bfd-35ad-abec-c6176b88bf68 | -16.29644 | -45.68538 | 2025-09-04 05:55:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b1e47599-8e89-36b8-a26c-9bb8a1c57750 | -9.61296 | -47.02329 | 2025-09-04 05:55:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ab63cfe4-6d57-3f05-903c-334e58994a99 | -13.57 | -48.12176 | 2025-09-04 05:55:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d94e30e2-7d42-33e9-91e3-9a399a1a3e75 | -13.46133 | -46.93526 | 2025-09-04 05:55:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| def188c9-1d98-30a8-9dcd-3328b8cdd00f | -9.60148 | -47.0397 | 2025-09-04 05:55:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 47b7cdbb-4034-3da7-8946-a4a4305bacfa | -11.67723 | -57.32141 | 2025-09-04 05:55:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 0656d168-85d5-39ca-bfb7-9825e8fce498 | -14.53715 | -48.07655 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 64d5c135-9b42-3852-8bad-7a31d8839d74 | -10.42659 | -50.37109 | 2025-09-04 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 00ce6e4b-6358-3992-95f5-0a1b490f3958 | -15.15425 | -52.37135 | 2025-09-04 05:55:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f799f98a-3760-3178-b93e-67af5b383005 | -11.85361 | -51.43943 | 2025-09-04 05:55:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f6a323f2-14b4-3353-88a9-15a357152b63 | -12.8734 | -48.01813 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf4a73bd-9c88-316f-bbe1-6849d774fe06 | -13.44188 | -46.93483 | 2025-09-04 05:55:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 85128295-d8f1-3690-9866-3482c00d1a2c | -15.54996 | -48.41327 | 2025-09-04 05:55:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| bca37fd3-5130-394a-8972-45ed0d1c5075 | -15.02196 | -48.10097 | 2025-09-04 05:55:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 93f6be32-e7a3-3385-9a50-b2ac7e6b70bb | -12.48491 | -48.08132 | 2025-09-04 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 028244ad-24fe-3a42-8825-927ad25567d8 | -14.56021 | -48.04309 | 2025-09-04 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README93.md)
