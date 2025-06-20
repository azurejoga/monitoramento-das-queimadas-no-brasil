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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3371299-e712-3ba2-8b45-5b564ea639a1 | -9.465 | -57.8252 | 2025-06-20 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 963cfc7b-3f4d-3630-b863-caa0e07daf53 | -8.7204 | -47.99339 | 2025-06-20 00:41:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10c16638-91aa-3dbf-af4f-d58b8b772231 | -10.08387 | -52.74586 | 2025-06-20 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 9f256588-c7a5-3c09-a253-0f1713b8d63b | -7.22466 | -43.06783 | 2025-06-20 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 191.6 |
| 1017e7a7-838c-3586-8b1b-a3088759827a | -9.29917 | -47.78936 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d721d427-334b-307d-815f-4e3577f7793e | -9.48274 | -56.07788 | 2025-06-20 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 68c93afb-c0ca-386f-aed0-3582e25139f3 | -9.97471 | -48.60299 | 2025-06-20 00:41:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| efd43976-c4f4-339b-a300-86763e73dcd5 | -3.03889 | -49.42443 | 2025-06-20 00:41:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f3e82bff-16bc-3fb5-886e-3518944d4745 | -9.30044 | -47.79837 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 856e582e-79cf-3eb0-b277-8b661bc41e78 | -7.22743 | -43.08609 | 2025-06-20 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 9945318b-0841-3f73-85db-359d4bad6dc3 | -9.45835 | -57.86243 | 2025-06-20 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d3cb10cb-5207-3608-a58d-690654fbb7d9 | -5.48125 | -42.14531 | 2025-06-20 00:41:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 1efee325-31a1-3d1c-babb-5fc7b7083bc0 | -9.30463 | -44.72034 | 2025-06-20 00:41:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d815f39e-f607-3cbc-a4f8-ec7891e1df80 | -7.52049 | -49.51408 | 2025-06-20 00:41:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6449cac4-bc15-3988-8746-8e7a9737e5d3 | -3.6126 | -47.542 | 2025-06-20 00:41:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e6473bcb-f34f-35fe-aca3-3a5e5d11ba98 | -6.66496 | -44.24027 | 2025-06-20 00:41:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d08ebac9-0f00-39fe-a239-bb212a6b2823 | -10.26306 | -54.02773 | 2025-06-20 00:41:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 19945a6f-b7fd-353f-9e36-ddeb06c12066 | -8.89615 | -47.48144 | 2025-06-20 00:41:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5aa80fc7-cb73-3d5b-96c4-85f55d646387 | -6.14526 | -47.26753 | 2025-06-20 00:41:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 87a1cb04-db0c-39e7-8488-b34c17844941 | -7.02052 | -44.60667 | 2025-06-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7200941c-da87-3f6d-b488-c75939d1a6aa | -9.49061 | -56.09628 | 2025-06-20 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 5a7d7c62-decf-3787-9fdd-5c6764fcdcd6 | -8.27347 | -44.95982 | 2025-06-20 00:41:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dee4e1ca-52d0-38b7-86e7-d0a4585126a8 | -7.01472 | -44.58444 | 2025-06-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a1817618-bd09-3c5d-8c92-8d01666eddd9 | -5.124 | -45.02745 | 2025-06-20 00:41:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1647a127-ff97-348d-b1e1-49daeb85b65a | -8.12778 | -43.12099 | 2025-06-20 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| aa4ca1eb-402e-3e0b-944f-e0cf05ac9497 | -10.09152 | -52.75116 | 2025-06-20 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 967dac1f-c3d3-3200-9ea1-55837302c06c | -9.46689 | -57.85476 | 2025-06-20 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 1e343442-4f27-3df8-869f-f0c40612fc7a | -7.39226 | -44.57318 | 2025-06-20 00:41:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d55c0706-adaf-3fcb-965b-535f722d2336 | -8.26564 | -44.9544 | 2025-06-20 00:41:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| c5710558-5b27-3819-8464-cf7ec20ddee3 | -6.6939 | -43.20639 | 2025-06-20 00:41:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 928f63af-f753-319b-bf73-31613d1d8796 | -9.33344 | -47.83959 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7118d89d-d333-33f6-b7a1-7f9c2ebc89dc | -3.41917 | -47.61287 | 2025-06-20 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fdff741b-3121-36cb-8eb9-314b17dc6cf7 | -9.33217 | -47.83055 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 0eefac01-9f2d-3222-bc93-8edd09b42fb5 | -8.25523 | -44.95612 | 2025-06-20 00:41:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a3a44a4b-7ace-3aa7-9f64-4c253708fece | -7.01839 | -44.59277 | 2025-06-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 2a96331c-d718-3fa3-b9fb-278284ab8570 | -5.49494 | -42.14309 | 2025-06-20 00:41:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 843d5752-8750-3411-b6af-a8cc2658c76e | -7.39025 | -44.5594 | 2025-06-20 00:41:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d675e2c6-12b2-3e08-a0f6-8aaabae4ef98 | -9.98495 | -48.54702 | 2025-06-20 00:41:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8c2a437f-83af-3d57-8519-97ad763561c6 | -7.70623 | -49.39396 | 2025-06-20 00:41:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| debb759e-6929-32f6-84a1-7613c90f3874 | -9.31133 | -44.83549 | 2025-06-20 00:41:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 209be2d5-c049-33ac-afd6-0b5024a88384 | -8.26751 | -44.96721 | 2025-06-20 00:41:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 93688efc-762a-3529-b173-f04667c2a946 | -7.71937 | -46.60864 | 2025-06-20 00:41:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9448a820-31ff-3fb2-b4bc-d98f31240baa | -9.45082 | -57.85669 | 2025-06-20 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| ce9b991b-85e5-34e9-b53c-cd24f28a3fc8 | -4.28512 | -48.18834 | 2025-06-20 00:41:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 873c1530-e7d7-303d-87d7-43d64eaeda2a | -2.29336 | -48.57765 | 2025-06-20 00:41:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fb961df5-d1ab-39f9-aecd-67a9addbace5 | -2.96064 | -49.07008 | 2025-06-20 00:41:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 417d7a15-81f4-3a17-be16-c7c81b40cbe3 | -10.07894 | -52.7388 | 2025-06-20 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 665a9382-1426-3710-befc-095e596d2438 | -6.14385 | -47.25771 | 2025-06-20 00:41:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 796c79d2-9b53-31f3-9ae2-476bc1b53c7e | -8.72928 | -47.9921 | 2025-06-20 00:41:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 03482f69-662c-316c-ac48-6d6cf3ad128f | -7.39434 | -44.56728 | 2025-06-20 00:41:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 816355bf-1953-3b7a-8469-54461d57df10 | -6.24492 | -44.66382 | 2025-06-20 00:41:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f4bc8e7b-ffb3-3468-810d-5f4dd5617817 | -9.97348 | -48.59408 | 2025-06-20 00:41:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 26d865e9-febb-35ad-8b91-551468c2f2b7 | -2.54904 | -47.70562 | 2025-06-20 00:41:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 47b4395a-ac6a-313b-83ec-f67e56128f69 | -9.301 | -44.8371 | 2025-06-20 00:41:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 321d0b01-c8b4-3cdf-96eb-e4eaca9991aa | -7.01681 | -44.5988 | 2025-06-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 21ee77a0-42b4-3e61-a8a0-8f02c12542df | -9.46301 | -57.82108 | 2025-06-20 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 7cfe876b-59a5-31dd-aec8-55f5fea177da | -9.30806 | -47.78802 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6af27455-bb31-3907-8af5-d11aedfa1b3e | -6.67847 | -44.25339 | 2025-06-20 00:41:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 624962b4-35d0-3f9d-b3ed-a245a4a6ae14 | -8.95772 | -47.98332 | 2025-06-20 00:41:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f49858e-8b8b-35d2-8fa5-8e6c1937eb8e | -9.30654 | -44.73305 | 2025-06-20 00:41:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 10328e27-9b46-3879-8aa6-b556e3990818 | -7.39223 | -44.55349 | 2025-06-20 00:41:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9bdd74f6-95af-3db3-8284-cad573a0b47a | -3.03006 | -49.42567 | 2025-06-20 00:41:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c41c117-4878-3e98-a5aa-7598bc540c5a | -7.06589 | -43.39622 | 2025-06-20 00:41:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e590b027-5fe9-3e38-a710-2ef3ef98980c | -7.87646 | -47.89453 | 2025-06-20 00:41:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b22af0c7-a4fa-3e62-8ac5-0b311379215c | -3.41774 | -47.60289 | 2025-06-20 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e378230f-c471-309a-9997-33828ad28044 | -7.75405 | -47.61829 | 2025-06-20 00:41:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 722ed99d-afdf-3e8d-a594-37d0a92ca135 | -8.37365 | -48.42109 | 2025-06-20 00:41:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e6ebd20a-f336-3f5e-9a36-c2ef3d255883 | -9.31695 | -47.78667 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 251ad629-308a-37e8-9022-356ecb9bd809 | -8.9122 | -49.85374 | 2025-06-20 00:41:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b1075508-3955-3764-bd14-ca081ed0cd0d | -9.13288 | -47.58791 | 2025-06-20 00:41:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c561f6ab-c52c-3df7-96bd-d205ca071703 | -9.45428 | -57.829 | 2025-06-20 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 9cc26774-5875-3eb1-a4be-d029d04ccf82 | -9.30933 | -47.79704 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7f821414-9cdd-3f43-96fb-5f8d2a8c2116 | -10.15732 | -48.98381 | 2025-06-20 00:41:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5f02b594-ad31-3516-a14e-ed301b7ba2c9 | -10.08073 | -52.75256 | 2025-06-20 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| bf63bf74-5d17-314b-b06d-930e13de53f4 | -9.48777 | -56.07173 | 2025-06-20 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 6d11b049-02cd-384f-b94a-bed024e87de8 | -10.36043 | -57.51459 | 2025-06-20 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| b44b64fd-af67-3ef4-99ef-cc366798e15e | -9.87287 | -49.33407 | 2025-06-20 00:41:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d5bcbdc7-9442-3865-a058-a6df14ee4746 | -8.25711 | -44.96886 | 2025-06-20 00:41:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e57b2e50-3168-3435-8745-dd798966c394 | -6.66718 | -44.25518 | 2025-06-20 00:41:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| c430b2b2-bae1-37dd-bc68-b60ff3dbfe1c | -6.84326 | -42.79973 | 2025-06-20 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 9a315c9b-7e55-3e31-be82-cf68e2627240 | -9.31821 | -47.7957 | 2025-06-20 00:41:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 50d7ab16-be50-3213-a02d-7db67c5dc142 | -9.30945 | -44.823 | 2025-06-20 00:41:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4c486536-4710-3924-a163-e90f28f4fb14 | -7.01886 | -44.61279 | 2025-06-20 00:41:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 828fc043-3b4c-357b-acdc-784a49f5ea8b | -6.24282 | -44.64978 | 2025-06-20 00:41:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 60419bba-8cb2-3fac-b09b-fb3570fa9edd | -10.36701 | -57.51924 | 2025-06-20 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 8328875c-fece-3e1e-a0f9-8e572858c266 | -4.38107 | -48.08231 | 2025-06-20 00:41:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c36f11b9-be43-3929-9d82-2b3c70a33767 | -7.1195 | -43.14576 | 2025-06-20 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| eceda645-8853-3b8f-9acd-569b853b6c7a | -8.13052 | -43.13866 | 2025-06-20 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5034f5ca-1bbd-3831-bd63-005c11447d8e | -2.44402 | -47.47453 | 2025-06-20 00:41:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 086587df-41e1-3c0d-b5e7-598f23478484 | -4.77939 | -47.25303 | 2025-06-20 00:41:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 34.3 |
| f4323b24-68de-3f89-93a1-37fb47d49985 | -7.21233 | -43.06969 | 2025-06-20 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 212.8 |
| 04595924-2b18-3a00-9edf-ae534821ce14 | -3.03129 | -49.43451 | 2025-06-20 00:41:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f945d590-5538-38f7-b477-4509211f4ee5 | -7.21514 | -43.08805 | 2025-06-20 00:41:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 6bafab3d-6a7d-30b3-8264-53a994f76921 | -8.95646 | -47.97432 | 2025-06-20 00:41:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3b67e018-d02e-3ced-ad22-facc72a9cf6a | -6.16521 | -47.27463 | 2025-06-20 00:41:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 20ba0c71-1f34-30c5-802e-bc26b1f866a5 | -8.36482 | -48.42237 | 2025-06-20 00:41:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 825cd59e-eefc-329b-ac43-74cdde286e3e | -8.18224 | -46.48818 | 2025-06-20 00:41:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e038480b-88b1-31ae-9732-14f343839d7b | -3.04013 | -49.43326 | 2025-06-20 00:41:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| d1a02ca6-623d-340f-9ea9-40af1c279e80 | -4.37976 | -48.07293 | 2025-06-20 00:41:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4243afc9-dd67-363b-b980-8e626a049c3a | -7.2031 | -43.0701 | 2025-06-20 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |


[Clique aqui para ver as próximas entradas](README4.md)
