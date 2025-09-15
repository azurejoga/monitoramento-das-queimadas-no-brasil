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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d477908-0915-399e-8c6f-3dc12d38b2c3 | -7.8756 | -43.5643 | 2025-09-15 12:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 40f8e71f-0958-3efc-a11d-19783dcdf1bd | -6.1502 | -41.2131 | 2025-09-15 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 4b283c54-c35c-33bc-9d20-ed5279a4be4a | -6.9798 | -44.5529 | 2025-09-15 12:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 789d5722-0b7b-3c1d-a1fe-5cafb55f6618 | -8.651 | -46.3637 | 2025-09-15 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 3bd29aa4-56e9-38fc-bd28-550f3fdf5383 | -11.6622 | -46.611 | 2025-09-15 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c37d54d6-fca5-3d23-bec2-823e3876aba2 | -8.9784 | -45.8344 | 2025-09-15 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 16b59652-fd21-3860-b649-2d409db737e5 | -11.81 | -50.4999 | 2025-09-15 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 521ab91c-ff09-381a-9c51-1b5ce3e8d2b5 | -12.5607 | -45.639 | 2025-09-15 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ed0fa26d-ba72-35bb-91cc-8792368eabab | -6.1504 | -41.1889 | 2025-09-15 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 9a7989a5-1451-31d9-942c-8af68e70898f | -8.9734 | -46.218 | 2025-09-15 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 405.0 |
| 2088a0c4-0e0c-332a-a924-bb780b3ff7b0 | -7.8945 | -43.5623 | 2025-09-15 12:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 6cb4b15c-a8b3-315b-9f7a-251208fb6a22 | -12.8404 | -47.1417 | 2025-09-15 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 33dfc2cf-50d8-3d1d-aee3-2e9a6b11d4ab | -6.1693 | -41.1872 | 2025-09-15 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 210.6 |
| b85961e6-ddf7-3665-a1d4-7a7f16f02d04 | -12.7875 | -47.9541 | 2025-09-15 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b46ee6ad-6163-34d9-a44b-b2f15b614347 | -6.1881 | -41.1855 | 2025-09-15 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 2132d11f-1abc-3053-b40d-2f1241453d78 | -8.9601 | -45.7912 | 2025-09-15 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 693e70f9-dad5-300d-a40a-da55d03a3559 | -12.6533 | -47.9507 | 2025-09-15 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 214.9 |
| d4ca92ca-cc36-33cc-8d02-26b429899e6f | -12.6537 | -47.9285 | 2025-09-15 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| ea2950a2-9547-3132-9f4f-5c12b9730d51 | -8.9787 | -45.8118 | 2025-09-15 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c64c7a5e-0474-32ed-8f0a-4e331e6fe333 | -17.7354 | -49.0801 | 2025-09-15 12:30:00 | GOES-19 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5effa9b1-2671-34d8-9d77-7923e7899ff6 | -7.8753 | -43.5876 | 2025-09-15 12:30:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 31caa331-2e17-36f5-a790-3e69b592ac42 | -10.8944 | -48.2002 | 2025-09-15 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6066d1ec-5b04-3343-93c0-8f533808f749 | -16.673 | -49.7615 | 2025-09-15 12:30:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9a7b9c36-f486-323c-b573-b6d587cf52d5 | -9.1365 | -45.3178 | 2025-09-15 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 661fdc2c-cd2f-34cc-83bb-098e47a63b8f | -6.1695 | -41.1629 | 2025-09-15 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 8c6320b4-1111-3e5d-9b42-286122374dfa | -8.9604 | -45.7686 | 2025-09-15 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b9aa5f3a-7ed3-36b1-babc-21a5411bb5b0 | -8.4329 | -45.7337 | 2025-09-15 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 95ea1011-ec1e-3ec2-aeeb-e3160e6f581c | -8.9545 | -46.22 | 2025-09-15 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 5c433bb0-e885-3ad9-b5af-5a81e3704e01 | -12.7879 | -47.9318 | 2025-09-15 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 25a54772-8173-3a08-8297-4356aff00bd8 | -10.948 | -47.1753 | 2025-09-15 12:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 6af2b034-bc11-3baf-a255-a2becb64777c | -20.9096 | -46.4681 | 2025-09-15 12:30:00 | GOES-19 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.1 |
| 2e25e896-8853-345f-a610-25a0693646d7 | -11.791 | -50.5021 | 2025-09-15 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 6ce2ec6f-1289-3585-98a4-cd7291558a9f | -6.169 | -41.2114 | 2025-09-15 12:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 239.3 |
| e67151b9-1854-338e-832b-1dd4d297cbdd | -12.1668 | -44.0988 | 2025-09-15 12:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 5ab80785-c529-3ec5-90c0-2bb75922c44c | -7.7025 | -48.8667 | 2025-09-15 12:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 985afab8-bb45-3971-9d79-08fa386b8eda | -10.6586 | -46.2242 | 2025-09-15 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6524ead9-6bd6-3e25-aed0-a49d173c72ef | -7.8756 | -43.5643 | 2025-09-15 12:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| daa1b891-bf36-3375-a7d9-3354fa374d43 | -11.791 | -50.5021 | 2025-09-15 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| de15e794-2c41-380b-b0c9-588f6b7263e1 | -8.9545 | -46.22 | 2025-09-15 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 347.3 |
| 316181b5-7988-346e-a6b8-875e9043f1f1 | -10.075 | -47.1908 | 2025-09-15 12:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2243aa9c-8f15-3d66-85aa-860b670d930a | -8.651 | -46.3637 | 2025-09-15 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| cd749e18-da09-3c86-be69-33fecdc2a055 | -12.1668 | -44.0988 | 2025-09-15 12:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| b53eed4c-62cb-3682-8cfb-2dc487bd9364 | -12.6533 | -47.9507 | 2025-09-15 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 57ddbde3-b545-3adc-9292-dc4f538dedb2 | -8.4329 | -45.7337 | 2025-09-15 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1d110aa9-1641-3d91-81f6-cbf8c7ca5ae5 | -12.5607 | -45.639 | 2025-09-15 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 245.9 |
| c5961dd2-d0a3-3a10-a536-1d0e53a4ad84 | -20.9096 | -46.4681 | 2025-09-15 12:40:00 | GOES-19 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.2 |
| 9f5946b4-1de8-3f4a-822d-4f15c512eab8 | -10.935 | -45.5978 | 2025-09-15 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 1319ab8b-3041-3bd5-a368-b9b11300acee | -11.81 | -50.4999 | 2025-09-15 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| ecbaeb5b-21d8-3f5b-ba45-ac6ca4cf8f43 | -12.7879 | -47.9318 | 2025-09-15 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| e04098f7-0ffb-384d-9bcd-caae2851591f | -8.9412 | -45.7933 | 2025-09-15 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a4471b82-7b41-30b6-af47-eafa51877785 | -7.676 | -44.4879 | 2025-09-15 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f2664496-d9be-35aa-a356-070ac09ecc81 | -12.7875 | -47.9541 | 2025-09-15 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9ba2c08c-1012-3ad4-b15d-00fa76f28614 | -6.3372 | -43.1492 | 2025-09-15 12:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e6c162c4-1cf2-3acf-b361-95d15bda3460 | -11.6622 | -46.611 | 2025-09-15 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 824fc66c-8f3f-3246-87b5-6f3d5983535b | -6.1502 | -41.2131 | 2025-09-15 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| ef4efc2e-bb56-35e9-b539-0ce2e48b6646 | -10.8944 | -48.2002 | 2025-09-15 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| dd2ac795-19a0-3480-aae5-113715226510 | -12.5603 | -45.662 | 2025-09-15 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 01d9735a-f653-399c-8d7b-2cf7148424f3 | -6.1881 | -41.1855 | 2025-09-15 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 800.7 |
| 952d91ae-e202-3c0d-94d8-21aac64872e0 | -6.1504 | -41.1889 | 2025-09-15 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| cf3c284d-74aa-31ee-988d-269f4c941960 | -14.8218 | -51.6362 | 2025-09-15 12:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b3d1f0a3-7216-34d4-ae95-67980f04a1b1 | -6.169 | -41.2114 | 2025-09-15 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 539.2 |
| b4e60447-965a-346f-86d9-ff19bf16e829 | -8.9734 | -46.218 | 2025-09-15 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 730.4 |
| a5545dec-6e7a-3c7c-a046-58f9c08d6801 | -6.1693 | -41.1872 | 2025-09-15 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 758.8 |
| 8a84cd7c-50b9-382f-b61c-6920dd5ad27f | -7.8753 | -43.5876 | 2025-09-15 12:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3fefb6fb-8024-3ccd-8c9e-7c7d3f2791da | -13.9288 | -44.8106 | 2025-09-15 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 6419f194-e20f-36ff-8cd7-44e660d538c0 | -8.6507 | -46.3862 | 2025-09-15 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d75ff402-627f-337f-aba5-9a0c1849bcd0 | -11.8097 | -50.5214 | 2025-09-15 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ad7a6c8a-7805-335d-acf9-a92f15ee1f0b | -6.1884 | -41.1612 | 2025-09-15 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 229.7 |
| d0104f25-3d11-3bbc-aaef-f2665a28d4a5 | -6.9798 | -44.5529 | 2025-09-15 12:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c3ce2755-0ed5-394c-baae-904959428e9c | -8.5944 | -46.3695 | 2025-09-15 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 28878b65-6a81-3eef-8f4a-327329ee7837 | -8.5947 | -46.3471 | 2025-09-15 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 30e205e6-4f09-3e29-922e-dc5f9298aec5 | -8.9784 | -45.8344 | 2025-09-15 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 514f4588-a20f-3690-a1b0-42f2f8515cb8 | -8.9601 | -45.7912 | 2025-09-15 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e88a9e18-0ca8-3cd3-a5db-1ed2ec52218b | -6.1695 | -41.1629 | 2025-09-15 12:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 169.3 |
| e5ff21a2-fa15-35ad-bc5a-a1a3a12fc4fa | -7.6838 | -48.8682 | 2025-09-15 12:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4cd921b9-9170-3bc1-b8db-24faaec8039c | -10.8944 | -48.2002 | 2025-09-15 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| edf093c5-6a7f-3656-83f0-d92902c6ddf8 | -7.7025 | -48.8667 | 2025-09-15 12:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 252d5ae7-066e-3b31-83bc-48ce2840d39c | -8.9604 | -45.7686 | 2025-09-15 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 80a15c44-6bdc-3534-970a-8bcd94a84330 | -8.9545 | -46.22 | 2025-09-15 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 562.8 |
| 0ec7e896-295a-3bb6-b938-96ce9ccba02a | -11.791 | -50.5021 | 2025-09-15 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fc77bb1a-9e85-30a4-acfe-2f9d2a43dd59 | -5.7363 | -43.1981 | 2025-09-15 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 117acb40-3b3f-393c-85e6-69045e9d73b8 | -14.5168 | -47.3304 | 2025-09-15 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 39533693-7972-38d2-a1af-0d9114c2ab6f | -18.7551 | -44.462 | 2025-09-15 12:50:00 | GOES-19 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b3607d83-a047-3f09-ac15-a2fe357b7e6d | -20.9096 | -46.4681 | 2025-09-15 12:50:00 | GOES-19 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| abba6c04-5c34-3994-954d-40f927552990 | -6.1504 | -41.1889 | 2025-09-15 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| a604c1cc-31f3-3a75-b1f4-2b7b77bbe8ee | -7.8076 | -46.1099 | 2025-09-15 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 1d5239f9-1681-37a9-a781-932257887ff4 | -6.9798 | -44.5529 | 2025-09-15 12:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 1414daca-0b3b-36e7-ae2f-c525f1103b50 | -8.4145 | -47.2324 | 2025-09-15 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 73156233-9b09-3115-8b56-46b615c23073 | -6.1881 | -41.1855 | 2025-09-15 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 464.6 |
| 8cf4f49a-424e-30ce-932e-8870b1eab9bf | -10.0937 | -47.2109 | 2025-09-15 12:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 9d6b06d9-deff-3802-a83c-b594a6ba21e0 | -10.9159 | -45.6004 | 2025-09-15 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9c6887a4-eb60-3f3b-8b33-3eed1d1e056e | -10.935 | -45.5978 | 2025-09-15 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 623335c8-d13d-358c-afb1-062763d1e838 | -14.5163 | -47.3531 | 2025-09-15 12:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6f7cff62-e773-3010-8e87-484f4d6d645e | -7.8073 | -46.1323 | 2025-09-15 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 13adc649-cb2e-3080-ab7f-967523fc8742 | -12.5607 | -45.639 | 2025-09-15 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 560ad496-d417-329e-8afb-fdf965b06f57 | -8.4329 | -45.7337 | 2025-09-15 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d32c804f-d4a1-3d35-9a9b-fd4573e01a44 | -13.9488 | -44.7837 | 2025-09-15 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ed5e1554-281c-3af8-a976-159a7bc30da4 | -13.9483 | -44.8072 | 2025-09-15 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 160e6efe-0f70-30dd-8044-dc67187fe07e | -13.9293 | -44.7871 | 2025-09-15 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 9344dada-b207-3f42-8d05-c921b7b46469 | -12.0051 | -46.6763 | 2025-09-15 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |


[Clique aqui para ver as próximas entradas](README70.md)
