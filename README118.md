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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81036b41-c471-3fb5-be0b-9f5fd0c58bf0 | -11.8843 | -50.6197 | 2025-09-03 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b6423ad4-5436-3974-a32c-78ef0cd917db | -11.3901 | -43.5602 | 2025-09-03 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| dca67d55-1ff4-36ba-8551-3bbe36545da4 | -12.7926 | -47.6638 | 2025-09-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| a6d28fee-3860-3e64-9105-54582b8d31b1 | -9.7427 | -49.414 | 2025-09-03 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a870e8d3-d4e8-3739-a880-37498143340c | -6.7595 | -45.9095 | 2025-09-03 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 03de2033-a54e-39f8-afc0-9b25cc296c1c | -8.0608 | -45.3636 | 2025-09-03 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 9d675b22-31e7-3376-916e-0eddb872a741 | -8.0605 | -45.3863 | 2025-09-03 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 85a944cd-caac-35f4-970c-bcacdd48e673 | -6.35 | -45.6723 | 2025-09-03 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| b800ce86-bf4b-3e19-9478-764917daf463 | -7.302 | -44.2936 | 2025-09-03 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 18a3a238-b6cd-3d61-82b1-28fa51a64ebf | -7.988 | -48.4318 | 2025-09-03 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 18bf7b57-c784-3e17-8ec6-e13b485cf19b | -5.7181 | -45.2453 | 2025-09-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 260.7 |
| eb97f381-b64f-3a97-820b-b408679009f9 | -12.4793 | -48.0414 | 2025-09-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9785fe86-835d-36c7-9689-90049dd28827 | -8.0203 | -44.0608 | 2025-09-03 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 147.0 |
| e4fddd18-67bb-31f8-9e09-ab1defa75e7a | -7.4654 | -44.8061 | 2025-09-03 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 406e26a3-f212-3faa-9e35-752e83086927 | -11.5779 | -52.115 | 2025-09-03 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| d3534e9d-4bbb-3e15-9b55-dfa4ae6893a0 | -8.3646 | -48.2899 | 2025-09-03 13:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 55f266f9-7377-3aae-90ed-bc6ca3e42db8 | -8.8842 | -45.822 | 2025-09-03 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 788a09ad-f880-3cdc-b46e-097fce23cf0e | -11.3893 | -43.6075 | 2025-09-03 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 6d7e0167-ae36-3f27-8571-6a8cb734a34e | -11.5963 | -52.155 | 2025-09-03 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| d55ba309-3af8-31a7-b3ad-c4ea868f5446 | -15.1771 | -52.356 | 2025-09-03 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 04cba77f-23b3-3c42-9cb3-faf71b1c2ec1 | -13.5167 | -47.0167 | 2025-09-03 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 5733995d-8383-3021-a3ee-84728f068f41 | -6.797 | -44.0859 | 2025-09-03 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 99008409-4fcc-34aa-bcd0-e675b673f27c | -6.3502 | -45.6498 | 2025-09-03 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| c62574fa-0010-3993-8079-6b386fa59a0f | -13.536 | -47.0136 | 2025-09-03 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f5e38a92-0f24-310c-b62a-c5c01aae40af | -8.3644 | -48.3116 | 2025-09-03 13:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 04e697b8-cf11-3d47-a9f7-3957daa5c379 | -11.5966 | -52.134 | 2025-09-03 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| b4b37cc3-0e18-393e-9ecb-e5bf1ff30699 | -9.1375 | -49.6444 | 2025-09-03 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1fb4987e-76d7-3382-9e03-98127ac2f657 | -7.5157 | -45.3478 | 2025-09-03 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| cefded1e-323f-34a9-b56c-a020c426f0f1 | -9.5454 | -45.8389 | 2025-09-03 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ab867753-0de0-3724-8f3f-a32d9e44722a | -5.8109 | -43.239 | 2025-09-03 13:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 9d6318fc-bc0e-3379-9caf-f6670109c909 | -9.7613 | -49.4337 | 2025-09-03 13:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1473f15d-c5fa-3f1f-b2a2-5ab18f16eadf | -5.7549 | -45.3105 | 2025-09-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a5795dc1-3639-3df1-a575-8d81b0872e47 | -6.8279 | -52.8348 | 2025-09-03 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5edd23ae-9185-37a1-baa2-2feafef7055f | -13.536 | -47.0136 | 2025-09-03 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f332fda6-1711-3f73-aafd-d211b6bd7594 | -5.7181 | -45.2453 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 277.4 |
| 87309ae7-c4b9-3f9c-b73c-1d860c3bef20 | -7.302 | -44.2936 | 2025-09-03 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| ca69727e-d702-3b6c-85b5-29e918512c12 | -12.7926 | -47.6638 | 2025-09-03 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 2f3e9a9d-67dd-30f4-82e2-2e98ebcb54db | -11.8533 | -51.4318 | 2025-09-03 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| b402a83c-1d35-3e95-854e-cae3d67be5dd | -5.7154 | -45.5613 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 5e1008f5-c7b9-300c-a1a6-bdcab5b885be | -9.7427 | -49.414 | 2025-09-03 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b6a8f8f3-e23c-3f87-b9d7-fea49bb0554a | -6.7595 | -45.9095 | 2025-09-03 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 60d90f8a-5ae5-35c0-9964-a0b58aad245d | -8.2006 | -49.5559 | 2025-09-03 14:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 06bf5574-e364-3592-900c-26a7955d4e6c | -11.6156 | -52.132 | 2025-09-03 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 76d8b06e-188b-327c-b129-cc19c53d8571 | -8.3646 | -48.2899 | 2025-09-03 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0c0f010c-08f3-3acb-80ab-f1c37af4a5eb | -13.5167 | -47.0167 | 2025-09-03 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 460404bc-a229-347b-af29-0b5551574875 | -8.8278 | -45.8054 | 2025-09-03 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8e2f5fe4-ab22-3dd1-a3e5-e2010e75a099 | -10.4632 | -53.6132 | 2025-09-03 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8122d7b8-eae0-33ad-8ea7-680089148129 | -11.5969 | -52.113 | 2025-09-03 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 73ff5d76-791b-3571-9861-de3b3ad32500 | -16.5305 | -55.0807 | 2025-09-03 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 768a47f1-1e1c-3e5d-9b7d-fb2b660ac274 | -5.7736 | -45.3091 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 7eb43c8c-af2d-384c-88de-bb6fc3e7f992 | -11.6647 | -57.3533 | 2025-09-03 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| bdfd001f-8d8b-30b4-89f3-aac91fb367e6 | -12.967 | -54.7705 | 2025-09-03 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5ebaff82-3f8d-3b3d-846c-bfbb7629931e | -6.7928 | -44.4776 | 2025-09-03 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 900a3a2f-b99d-328d-9046-8e6e35b474c7 | -7.4842 | -44.8043 | 2025-09-03 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2cee827d-c26a-39a4-aa8b-c94ff5c6c106 | -6.797 | -44.0859 | 2025-09-03 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 4f6c256e-fed6-346b-a316-1c12f6985eec | -8.02 | -44.084 | 2025-09-03 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 464e0027-b8a6-3b89-8d1c-b89c3b844aa7 | -11.672 | -52.168 | 2025-09-03 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| bfa9614d-1ba9-310a-a5f1-ccc05a84d22c | -9.6232 | -47.0416 | 2025-09-03 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9d45c14a-84df-3f7e-af40-ef1ed56e7fc4 | -5.7343 | -45.5375 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 61d65e85-bb1e-39d3-99fd-27db2272bee5 | -6.0699 | -45.6259 | 2025-09-03 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 42404830-bfd3-3956-aefd-e9f337c34ee7 | -8.8845 | -45.7994 | 2025-09-03 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b601c446-1c30-3c51-a0a4-b470094abc23 | -5.7183 | -45.2226 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5e0dba23-6fc5-3161-85dd-8e0e69b9297f | -9.6229 | -47.0638 | 2025-09-03 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 71acc90d-4b1f-3672-a462-6c92fc723325 | -10.4816 | -53.6527 | 2025-09-03 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f799738a-0911-3a1b-9c67-dff1474b17de | -7.53 | -47.4662 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 6a351c66-5012-39b6-a0e1-abd3a7ae2bfe | -16.5501 | -55.0782 | 2025-09-03 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 2ceea4e9-9abf-3d8e-b6e9-312596e51d07 | -7.4966 | -45.3722 | 2025-09-03 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 40cace6f-e776-3dd8-8a23-3a4e6efd71e0 | -9.6226 | -47.0861 | 2025-09-03 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 6e300000-b5ff-3596-bb37-27e94eee317f | -9.1373 | -49.6659 | 2025-09-03 14:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 682cebb5-2627-3fae-a771-1003f4ff97a8 | -6.3692 | -45.6258 | 2025-09-03 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 25944950-13d9-3881-a003-47baa417ddd5 | -7.4969 | -45.3495 | 2025-09-03 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 81966594-fc65-37e2-8c6c-eb3eadccbe43 | -11.5972 | -52.092 | 2025-09-03 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 70a1c9af-75ee-3244-b3e8-2ed5acf8a198 | -7.5302 | -47.4443 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 23cd6546-6701-3e77-a8bf-d2e932930133 | -8.0203 | -44.0608 | 2025-09-03 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 2bd733a3-faed-30c0-ae0b-88c3b916d08b | -16.3145 | -52.9628 | 2025-09-03 14:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 80d04ae6-04de-3013-80d5-ab59f48d62de | -10.5045 | -50.3226 | 2025-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 941d475e-9497-350b-8722-9060acf7fc7d | -11.9635 | -45.7741 | 2025-09-03 14:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 80fa6757-b51b-3360-98bc-b6f3637f4b7f | -15.1771 | -52.356 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7f46e40d-0d64-33d3-93c3-d60dc7769d3c | -9.636 | -46.1221 | 2025-09-03 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 43f05a01-b6ff-3f05-be81-e4cfe91a8752 | -9.7613 | -49.4337 | 2025-09-03 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3a0f7d74-f4b7-3975-a41d-92d9505ccc25 | -5.7004 | -45.1333 | 2025-09-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5eb8df7d-63b3-3471-9de9-2b6d80427d2d | -11.3897 | -43.5839 | 2025-09-03 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 213.4 |
| e055fc78-a7a9-3064-9dbb-c6f6e5bc5289 | -8.8839 | -45.8446 | 2025-09-03 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 78d386ce-e9ba-3889-baad-9025ad8031b6 | -5.8884 | -42.9753 | 2025-09-03 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 159.2 |
| 80964bea-119e-32e3-a462-7c90c18004f1 | -8.0197 | -44.1072 | 2025-09-03 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b5a8e0dc-e868-3dff-8072-d3b341b81d4a | -11.5966 | -52.134 | 2025-09-03 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 5dc2e1e9-d702-3c41-9abd-67b9a8ed3f4f | -8.8842 | -45.822 | 2025-09-03 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 26396fae-4982-39f3-9244-3f82d6a0c98f | -5.2575 | -44.4581 | 2025-09-03 14:00:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 14ca7a09-e72a-3154-ab7e-137c88c69ce9 | -11.3901 | -43.5602 | 2025-09-03 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| a7c44a3f-ab6e-3de2-bb3e-0df4a87b8fe2 | -11.6836 | -57.3518 | 2025-09-03 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| a68e764b-daaf-33f2-a25e-f9c02db31faa | -11.8708 | -51.5357 | 2025-09-03 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b7df0288-744b-3cc3-91d5-3b0f0491d783 | -6.1234 | -45.9139 | 2025-09-03 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| b163e638-bf05-3344-aca5-8746966e59f8 | -5.7152 | -45.5838 | 2025-09-03 14:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 572af1eb-1458-3c55-8d0f-40f95b180724 | -10.0932 | -54.7667 | 2025-09-03 14:00:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 6a4ccaa1-b9c2-373e-b67e-8adb16bc21f2 | -8.3644 | -48.3116 | 2025-09-03 14:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 8591a37c-028a-3971-a57b-7ad6befdee81 | -6.3689 | -45.6483 | 2025-09-03 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 4d0914f5-09e2-3e88-b981-9b17c205cccf | -5.8455 | -45.6421 | 2025-09-03 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 69b16c9e-1abc-3149-a970-737663d63964 | -7.5157 | -45.3478 | 2025-09-03 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 269cdd27-575f-3e9c-b33e-d22fc07687a4 | -7.4332 | -46.0093 | 2025-09-03 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7cac07c6-7fd6-3833-b47c-0df0308d2dcb | -6.3502 | -45.6498 | 2025-09-03 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 177.4 |


[Clique aqui para ver as próximas entradas](README119.md)
