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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b9f4d1e-658b-3b3b-ba62-81ffb64ce536 | -11.9635 | -45.7741 | 2025-09-03 14:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 991aa198-8ee9-3ad3-a56e-ec21940f1343 | -11.8537 | -51.4106 | 2025-09-03 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 29b45c3b-e9f3-3721-a96b-fb51b986ba9e | -10.913 | -50.8762 | 2025-09-03 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 82fb9f48-273e-3189-851b-508dc4874813 | -11.5966 | -52.134 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| bdf07c94-8cc2-3a5f-a6db-460fdc94ddf2 | -6.2036 | -43.3709 | 2025-09-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 8599a620-fe2e-387f-b3d6-4ecc582d5165 | -5.7738 | -45.2865 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 188.7 |
| f2cf7cf3-6b74-36e1-b9bf-25cae7eb8c53 | -10.9509 | -50.8722 | 2025-09-03 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c7a31885-56cd-3de6-937b-f3c645d97631 | -6.2038 | -43.3475 | 2025-09-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 1a437bd8-ac7f-3259-9452-661b06d83649 | -11.8141 | -51.5208 | 2025-09-03 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 3a0ce783-de5e-307e-a7ba-be1a3f160930 | -7.7224 | -48.7572 | 2025-09-03 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 008e6ae1-a22f-3b45-8db9-697917379dbe | -11.6717 | -52.189 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 44b282e7-28ad-38cf-898f-8a0ab0f90904 | -15.7175 | -53.6376 | 2025-09-03 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ebfca5ee-a475-399e-ae92-8c0de271d76b | -13.0156 | -56.8781 | 2025-09-03 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| ac35425b-7b04-34e9-9c1d-f4b8177f0c6d | -7.4969 | -45.3495 | 2025-09-03 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 907f46e1-2cc8-31f7-8f6d-c26896b6640d | -11.6647 | -57.3533 | 2025-09-03 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 6608b3a4-ac12-3176-8d52-34b7402652ea | -12.9382 | -56.9856 | 2025-09-03 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5770a1e6-0e73-3f29-a22b-d17c0f05a16e | -10.5045 | -50.3226 | 2025-09-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 1d17a7e0-87f1-3812-91fe-0ec7264521f3 | -12.967 | -54.7705 | 2025-09-03 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6f49d03f-8129-35ad-b37a-82cacbbf071a | -12.6339 | -57.0127 | 2025-09-03 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| c9a45363-bea5-379c-a55a-00f2d24bc7b1 | -10.0932 | -54.7667 | 2025-09-03 14:40:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 426eae0e-6aa6-30ef-b516-a5458315db67 | -11.5963 | -52.155 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| daf18425-545c-39b8-bcb7-a84bfeee57d5 | -11.3901 | -43.5602 | 2025-09-03 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 269.2 |
| f90f4408-c457-319c-8677-7319a632f199 | -8.8278 | -45.8054 | 2025-09-03 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 7921bfc6-8021-32f0-841c-768ca65263b4 | -7.7039 | -48.7371 | 2025-09-03 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 970d41cc-1f4b-3671-b83e-f6429449bd70 | -5.8986 | -45.9748 | 2025-09-03 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ddca6d28-372b-3bdc-bc68-36d8d09d33ff | -7.5302 | -47.4443 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a797ab6d-c672-3559-b6b6-079109c65f71 | -6.35 | -45.6723 | 2025-09-03 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 9b16c567-8b39-3a4c-8ba3-2ca253280835 | -11.0249 | -47.121 | 2025-09-03 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f2f81e97-f348-336f-97ed-550e0ddcd673 | -9.7615 | -49.4121 | 2025-09-03 14:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 416d1ed5-5993-353a-87d8-8b9b945f0701 | -11.3709 | -43.5631 | 2025-09-03 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.8 |
| e8a05bcf-5118-3d4f-a111-20fc378321de | -10.4632 | -53.6132 | 2025-09-03 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6fb1b6ed-6126-3d99-b402-51e6860b7ed5 | -6.8281 | -52.8143 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5c9aff74-8139-301f-894a-93cf64012b97 | -9.6226 | -47.0861 | 2025-09-03 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 810b1988-efdd-32bb-86b1-18d706f140d3 | -8.0206 | -44.0376 | 2025-09-03 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d40b5595-32d2-3b91-b693-fcabd163e472 | -6.7595 | -45.9095 | 2025-09-03 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 1e277bd5-24c8-3f33-bf1c-3084aafc1e88 | -13.5167 | -47.0167 | 2025-09-03 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e0725d48-fecf-3740-97c3-53b7dc0ad287 | -8.3644 | -48.3116 | 2025-09-03 14:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| d9f46715-cd7f-30ff-ba82-a7958e27379b | -8.8839 | -45.8446 | 2025-09-03 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9ec6efc2-1411-32e3-971a-ab2f7b5480cb | -8.0203 | -44.0608 | 2025-09-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 648fe8c2-8e18-3de0-bc46-0721ed9dbe82 | -11.2005 | -55.0195 | 2025-09-03 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| ca46a688-84c4-3b31-8743-a4a2c181d8c7 | -8.2006 | -49.5559 | 2025-09-03 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 45770685-fa73-35b1-8a6b-e0518b828070 | -8.0608 | -45.3636 | 2025-09-03 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 2a2d777b-785b-392a-8a9d-750a32b7f406 | -12.9189 | -57.0074 | 2025-09-03 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 52dbcf44-bebc-32bb-8062-6998bf5da59b | -7.3793 | -49.4075 | 2025-09-03 14:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 1c7dc0cd-b598-3d5c-98df-a44d851c47b1 | -5.7343 | -45.5375 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2bbd9d60-c789-3c22-b1bb-f38bd87728ff | -6.2221 | -43.3927 | 2025-09-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 258.5 |
| d8f3b12a-83b6-337d-b533-0a759744a788 | -5.7154 | -45.5613 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 3e0a9cc5-fc3c-3ffd-92c7-22a2d0c0038c | -9.1373 | -49.6659 | 2025-09-03 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 6995e367-8e64-3792-859a-594f6b5ebd0d | -6.7928 | -44.4776 | 2025-09-03 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| df3c5224-05f5-3e0b-bfa2-b0d843cfa086 | -6.6535 | -45.2644 | 2025-09-03 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 37f55900-a3a3-37d3-9334-c43d3b902640 | -6.0966 | -46.8281 | 2025-09-03 14:40:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 4c9ae5ca-0845-3153-82a9-73c0c4779786 | -15.1771 | -52.356 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 150.2 |
| c0efd845-02c2-354f-b856-26fdd47e3404 | -10.9136 | -50.8336 | 2025-09-03 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 00f7164e-673b-36e6-82f0-de768da8b8d5 | -8.4604 | -45.0495 | 2025-09-03 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9ddb6386-d8ce-3282-ad20-b82dac023145 | -5.7922 | -43.2405 | 2025-09-03 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d7bc59c6-0d1d-3373-beaa-3a467e33b6d5 | -5.7925 | -45.2852 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d0869a53-33a3-30f0-a70f-b611d01d8504 | -6.2411 | -43.3677 | 2025-09-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| b414fadc-0227-3842-9ff9-7e08d365ae07 | -6.7967 | -44.1091 | 2025-09-03 14:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9aae8d88-a273-30ea-a7e1-06bbbbc70cc9 | -6.9632 | -44.3477 | 2025-09-03 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| aad2db37-b087-396a-a130-7bb2434c2c95 | -8.9031 | -45.82 | 2025-09-03 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4d840dcf-b22f-3675-b9c1-645e67e2dce1 | -6.8465 | -52.8337 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6be6632d-d933-3c97-9e48-0be746e5be5c | -6.7407 | -45.911 | 2025-09-03 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d7504f01-87e9-3e96-a80f-eb6135fa796a | -15.737 | -53.635 | 2025-09-03 14:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| fa964259-8d48-3cf2-adca-377ca883b5ac | -10.45 | -54.7785 | 2025-09-03 14:40:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 5856a509-4ac5-331d-a311-994011838535 | -16.5305 | -55.0807 | 2025-09-03 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 790dd868-3fda-3af8-818b-ef959d03c900 | -9.1949 | -45.1972 | 2025-09-03 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 0acf35c7-4a36-333d-b9c3-a9148fc2bf0f | -6.4648 | -49.5151 | 2025-09-03 14:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6613de19-46e8-365d-9c29-4cf6533ab0e5 | -7.53 | -47.4662 | 2025-09-03 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9cc85d89-2fb0-32ab-9b26-74c446eb4503 | -9.402 | -48.0585 | 2025-09-03 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e9757f7a-6482-3240-aa85-88d21f9a7c4c | -6.2409 | -43.3911 | 2025-09-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 53873056-976e-3889-8309-0b7d3000936b | -6.8466 | -52.8132 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8fac20a7-0a36-327e-8152-8454ae941c74 | -11.5969 | -52.113 | 2025-09-03 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| ab2c5b13-3a3b-3c53-ba83-41d232f5ec40 | -9.6229 | -47.0638 | 2025-09-03 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 1f16f675-66de-3021-9fc4-b5442c9d2f35 | -7.5157 | -45.3478 | 2025-09-03 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 4e301c86-2627-3278-a293-a912720dd00c | -5.8895 | -57.7513 | 2025-09-03 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 8a2b54b5-1c9b-3f85-8e96-ada25f96fc40 | -9.6232 | -47.0416 | 2025-09-03 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 0a4025cb-102c-3950-b022-4c6fc45077ed | -12.9861 | -54.7685 | 2025-09-03 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 49abb060-2720-3bc9-b61f-2f00ee4751ec | -14.0685 | -54.0308 | 2025-09-03 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 822ce310-eac6-3cf8-bda0-c7eba9171cd4 | -8.5376 | -51.3069 | 2025-09-03 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 06c1d9b2-75d8-3f14-bcaa-daf1cee2a488 | -11.795 | -51.5229 | 2025-09-03 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8ae9cf88-39be-3da8-8208-546a822416b9 | -7.7226 | -48.7355 | 2025-09-03 14:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 141.3 |


