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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d360423-cfe8-3be8-b00c-ee32a24ad18c | -5.70336 | -45.52105 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e05b89bf-a71d-3d1a-88bf-674ab35a5d3e | -6.77328 | -44.30877 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c2a3c2a-c393-3403-9e86-5437db8fd53f | -6.88467 | -45.65546 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69052454-536d-38fe-980c-21fd4219425a | -3.43455 | -49.04808 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26cd1f5d-8066-3d78-8bdf-f9a0cd25431e | -5.74253 | -57.58669 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a26d2f8-3597-3f3a-ad55-27b92e950c12 | -8.02655 | -44.99847 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf8c339e-50f9-39ee-8538-4b7751a33699 | -7.28681 | -44.47359 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3d178e0-a103-3ff1-a3fd-7011e7ce9e23 | -3.82599 | -54.11637 | 2025-08-25 04:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73c13083-eea0-356b-b125-0b7cd095630a | -6.43316 | -44.56092 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e56f4738-7b80-36b6-b855-ad5a9381b03a | -5.79828 | -45.40091 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3056c2df-8831-30d8-a6dc-caad9e3ebb8a | -6.67865 | -44.41444 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 452a486b-0612-3498-a8c4-0a2da48503c7 | -5.79454 | -45.40031 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32b23134-38d6-33ed-84e9-77fbc5387c9d | -5.79895 | -45.39638 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebe79e44-52f2-357b-b1c0-08451f08eae9 | -3.434 | -49.05154 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7f907f6c-0674-3292-b49a-dded11888af3 | -7.32335 | -44.53385 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44051b17-4142-3239-adea-4f0132d07d16 | -6.14422 | -51.7534 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40a154f-5bbb-3ae0-bac1-72cdea84f5ce | -6.9185 | -44.41927 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e71f24ab-9020-304a-82e3-ba2ac7338a78 | -3.83889 | -55.9708 | 2025-08-25 04:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 76cb0482-c966-3419-bb81-e5973295e02a | -6.44185 | -44.55721 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 978f1799-d5f8-3bd3-8dbe-1a9963ca0dc4 | -6.90227 | -44.41425 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 808552b7-9c78-3c3f-8703-777a0a936b2e | -7.54141 | -46.02207 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 839908aa-e9fc-3e63-828b-faf53009723c | -6.89529 | -45.66128 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09af96aa-f67a-3914-a429-000053757636 | -6.16701 | -43.0024 | 2025-08-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a64c5e75-c111-3c83-b721-55deb31e1c75 | -7.59305 | -46.24521 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ff8604c-8dec-3fbc-937f-4f1e8988e501 | -7.32806 | -44.53421 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c93d170c-a69d-3680-9b2b-5f2cd0d741b4 | -6.20541 | -44.14202 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c58d997e-4550-387c-a23e-5d8ce2e66dd5 | -6.79672 | -44.31878 | 2025-08-25 04:40:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c8f174d-005d-3dc5-88af-440108ec2f09 | -3.79585 | -51.18997 | 2025-08-25 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2bdce1f8-f94f-32ad-9541-a22df773a4f5 | -6.49887 | -44.78946 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78d52049-e44d-36cd-8570-9c8db2afd2e4 | -7.29565 | -44.52584 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b339395-6716-39e3-ad0a-23e847cea3b5 | -3.20008 | -43.90159 | 2025-08-25 04:40:00 | NPP-375D | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f3066c4-7e0f-3533-a242-5dce5f94a5ce | -5.79576 | -59.22018 | 2025-08-25 04:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b20b1a7d-c83b-3708-90c7-908b371566a0 | -6.39701 | -44.72143 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40349e91-a91e-38da-802d-2a699a6b8f28 | -6.67709 | -44.42489 | 2025-08-25 04:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f6de9ab-c7c1-3034-bbcb-e1fed3a7d21a | -7.58262 | -45.22854 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04a56ba8-0266-346f-8faa-fb012d78a997 | -5.52171 | -52.00452 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3e51b8b-7ac9-3365-b727-0c79d3a51f2e | -5.73834 | -45.38987 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 648cbe9f-08e2-3cc1-a557-073c5daec8cb | -6.1912 | -44.13186 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c70ca4f2-0404-3ff5-81f7-d68d0cdc87b2 | -7.81114 | -46.6255 | 2025-08-25 04:40:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e4b6fec-5eb7-313a-b383-daf905163e88 | -7.65942 | -42.66892 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6995f3a7-4c54-36d6-a597-e4c217275b43 | -7.2911 | -44.52877 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b209e08-9cdb-3a0b-9357-abb315541f5f | -6.20646 | -44.13474 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d219a4a-9aa3-3c10-9341-87a752dfc5a8 | -6.91501 | -43.77924 | 2025-08-25 04:40:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 249f2666-3f3c-3d4e-b6c3-4b2d0f3dc05a | -7.20896 | -49.61337 | 2025-08-25 04:40:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3283c602-2089-371e-9294-d532a475ae63 | -7.31932 | -44.53321 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ca95810-5bf3-356c-862c-7ab0718f0feb | -7.14738 | -44.15795 | 2025-08-25 04:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa850f6c-fa0a-3ce0-b756-77498cbc0226 | -4.96584 | -55.81366 | 2025-08-25 04:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f29d7c13-e6d8-3a8f-a0b7-9c4955b2b422 | -4.81637 | -43.54221 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c86ebda3-a4f6-302b-bdef-fc6eec250c87 | -3.70061 | -49.54657 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58ea9c98-51b6-3714-8333-55bcd985859c | -7.33159 | -44.53836 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 184ac02b-b363-3e48-b8a3-caee3123df9f | -7.54007 | -46.01993 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c997c2a-f6fa-3785-bb38-d7e9fe392dc1 | -6.91394 | -44.41918 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bef4f9c2-d141-3128-843e-e66f4f67506d | -7.62136 | -45.23468 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9ca9122-5fe5-3652-9219-255a92b5e9e9 | -5.75222 | -57.59132 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99ddf550-4f8a-33d0-a747-dc2fecfb81dd | -3.43122 | -49.04756 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ee0b5f9-f5df-38f4-b71b-efef383a4a47 | -3.45113 | -43.34474 | 2025-08-25 04:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 827392d5-de9e-3b4d-9954-736b7f54ad76 | -5.75323 | -57.58539 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d3ec10d-d041-3d70-8914-6cd4c2e31ce7 | -3.58785 | -49.42515 | 2025-08-25 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f500b273-006b-3f48-85b3-80068891f33d | -5.48396 | -41.40917 | 2025-08-25 04:40:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e364c610-2e8b-3400-89b1-ed8224238349 | -6.03734 | -43.99043 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c222984a-8290-3ef9-8ed5-ac73dcb0924f | -7.30562 | -43.66828 | 2025-08-25 04:40:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da1dbf0a-3d20-390a-a876-1926ffceaffd | -7.58192 | -45.23339 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd883ae5-7347-3774-9a81-6e39365a91d9 | -5.64307 | -45.14917 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc56479c-b439-3fab-a26c-7bef8d26beb3 | -6.43865 | -44.55141 | 2025-08-25 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d63300-9681-33fc-85f1-c575eee25c94 | -7.72975 | -47.44716 | 2025-08-25 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aa1ebd1-3c22-3a79-abf9-ff63ad34494e | -8.05997 | -45.01895 | 2025-08-25 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bee0da65-aab7-3c80-9bb9-3e1a7f63c73f | -5.10681 | -43.20919 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 846312d8-92d9-3ec5-be2e-1e6873306e32 | -7.92049 | -45.88973 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a308128-f310-3c93-a9d0-68d7e3baf16c | -7.46959 | -45.02198 | 2025-08-25 04:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f622d1c3-376b-3eba-90e3-e6b32fbb093d | -2.78266 | -41.87553 | 2025-08-25 04:40:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 123c23a9-c9a5-30cc-b6f9-a7428f375a74 | -5.68382 | -45.13654 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 279ca3d0-60fc-3ff9-b902-f370cf992856 | -6.50573 | -42.95021 | 2025-08-25 04:40:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53b8bc15-ef17-3196-8ee9-c92c30570c57 | -7.09201 | -44.62339 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f341c5f-01fd-3451-b714-a46e4d3a8ce6 | -5.73393 | -45.39373 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 300e0750-6538-3601-8cb1-14b08ce855db | -5.74355 | -57.58071 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a97484a-c7d5-3ac6-924c-857406409e51 | -7.9383 | -45.92444 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dad848e-dbca-36d3-bc5e-c91aab6bb444 | -5.79834 | -45.39892 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 119fbb59-9601-38e6-ad47-ac2da79b0161 | -7.85588 | -46.27535 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0b703b5-6426-30cf-b7b1-c042241afdd1 | -5.75473 | -57.57657 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de1384be-e4bf-30c8-8181-7050597029f1 | -6.20285 | -44.13752 | 2025-08-25 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b175648-a694-35d0-b027-081823ef7031 | -7.59369 | -46.24097 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1771ddb1-d2cc-339d-b69f-5e50d269d54e | -7.66864 | -42.67013 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67903690-5928-3a40-bb39-2b75f8bd761a | -5.65584 | -45.14165 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf90738c-118c-33f9-9d29-775c32307e08 | -7.86318 | -46.27663 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 171b48d4-479d-372a-8781-4cf96c3954f0 | -6.919 | -44.41579 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b5c9482-6db3-31a4-a304-9c19e99acc66 | -7.66619 | -45.39525 | 2025-08-25 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d02b98f-ac63-3168-aab3-4a743ef87335 | -6.75072 | -50.96433 | 2025-08-25 04:40:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04f8889c-8fbb-3c82-82a0-65efcf945d3d | -7.81532 | -46.88827 | 2025-08-25 04:40:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa1ff7b7-4c74-3329-af94-4a52be1005c5 | -7.31529 | -44.53256 | 2025-08-25 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cedeb84-9870-34a4-a877-b87f0fa55f4b | -5.55533 | -45.55942 | 2025-08-25 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5916ea3-ada2-3fb2-bd1b-2bf249077eba | -5.29836 | -45.26754 | 2025-08-25 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03b58a6d-e9ac-35bf-9cd7-dde9f700fc6a | -2.78196 | -41.88003 | 2025-08-25 04:40:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28f15ac7-44ff-3012-9b09-fe43da14f599 | -7.14684 | -44.1616 | 2025-08-25 04:40:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1dda5139-606d-3544-b2bb-dbd59ab81d72 | -5.73762 | -46.15559 | 2025-08-25 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfb2eb4e-b64a-3ba1-ab4e-44ecdea41565 | -5.74814 | -57.58452 | 2025-08-25 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ab9bb6-688e-37dd-b9e1-64ee27ffdb2f | -6.91798 | -44.41975 | 2025-08-25 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 921b6f64-97b7-32fd-855a-1657706165cb | -5.11168 | -43.20577 | 2025-08-25 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| dc8cf54f-5ac0-3ee7-9106-0826b3f2ff07 | -5.42041 | -60.16768 | 2025-08-25 04:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33d4479f-09d1-32cc-aa3e-c0dd13366ec8 | -6.87278 | -45.65816 | 2025-08-25 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 876852d1-ac68-3364-bbf8-93e6f8e9a9bb | -7.55649 | -46.23946 | 2025-08-25 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README39.md)
