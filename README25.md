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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5194c6ea-fd57-3897-94ed-2e48748e24c8 | -4.86793 | -45.05798 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9134b096-823e-3e26-ac94-c76a95aa2975 | -11.51175 | -43.54447 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50b121fd-c789-3cc1-94f2-53c24004977d | -4.50666 | -40.726 | 2025-09-30 03:47:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30d2b267-4458-3b19-9165-8c0b6be94c0a | -5.40782 | -37.7048 | 2025-09-30 03:47:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b8e70a4a-956e-3584-917f-5086674959ad | -11.42658 | -43.50881 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8076d8e4-8ec1-3dab-b82e-20bcd24ed3b9 | -8.00719 | -47.05811 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 71379926-0326-383f-8c67-31b0a474d853 | -10.18293 | -44.90426 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 6be50931-c861-3c75-8b4f-e01176e4b31b | -10.95756 | -46.49609 | 2025-09-30 03:47:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44e008e3-d335-34a5-9914-1bfcb6b629c0 | -8.32869 | -46.21671 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 587639a9-4ea9-3802-9460-921a506988c7 | -9.44098 | -50.9043 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9474c4bc-3788-3853-ada3-8f84e29d7e5c | -9.32066 | -45.696 | 2025-09-30 03:47:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9a7d6a3-d8c4-3efb-88c9-d28d804fb8e3 | -10.54751 | -43.63394 | 2025-09-30 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c54bafad-cc35-33f7-8e76-4abfbf2fc179 | -8.26662 | -45.5133 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35ee9c56-2c70-3892-8986-d06d3c44037c | -3.42422 | -39.342 | 2025-09-30 03:47:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0b20264b-67f0-3a7b-a9f7-c2a5c4301834 | -10.20036 | -44.89993 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f3d49888-4dd2-3ca9-8f67-01866248ce61 | -8.25292 | -45.53136 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25e7b978-165e-3e26-940f-6b0c70328438 | -8.25598 | -45.5145 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40b6d6f5-7aed-335c-b037-a6f0848fdfa7 | -10.19751 | -44.88913 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cc043909-c118-33b7-9ed3-4e3114b94486 | -4.89579 | -43.46997 | 2025-09-30 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 15af049e-f22a-3308-8a9a-7d04540e5781 | -10.8101 | -45.36399 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c23b531-a20c-3cfe-867c-0acc8216177a | -3.09845 | -47.01317 | 2025-09-30 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 82699ba5-38c0-3a04-9530-8a7a916f06d0 | -9.9396 | -43.63773 | 2025-09-30 03:47:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6325cdbd-b77f-38ae-87ab-35f966b0f676 | -5.96387 | -35.58051 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 416b50bd-d8da-3556-88ce-c9ee0e1e43c3 | -9.31619 | -50.63266 | 2025-09-30 03:47:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9a92960-bada-3cf9-8c9e-4a45f8eeb98f | -9.93601 | -47.45901 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abcb32c8-83eb-3c22-a206-553a0e5051ba | -7.82931 | -47.01065 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ad2dbbf-fa60-3e0b-89e0-d7ea2bf436e1 | -4.3287 | -38.86385 | 2025-09-30 03:47:00 | NOAA-20 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 128ccd6b-5bb8-39b3-8377-cbc4330485b9 | -5.32898 | -43.73627 | 2025-09-30 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0320c353-2ed8-3cf8-ad66-802b65372c89 | -4.40767 | -40.69291 | 2025-09-30 03:47:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ec51725-bb04-3392-97ef-6f3b01b2b598 | -10.19491 | -44.89114 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7894d2c0-adfb-3c27-a016-6e704da30b25 | -11.48845 | -43.52451 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6b84f68-ee18-372b-9e4c-cdf1150657a9 | -10.19194 | -44.89313 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 51.3 |
| dd7d64df-4c1f-35d5-88b3-32669e90be64 | -4.67658 | -43.2597 | 2025-09-30 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6857c9da-0ec1-3192-bf3e-9f3dfa7891f8 | -11.45956 | -44.98574 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d626976-fcdf-3e01-b956-5646e2c70f18 | -7.77098 | -45.74436 | 2025-09-30 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b9ee214-4450-396c-950f-d6d2097f86c4 | -7.91306 | -44.60502 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fa1d065b-b1fe-33c5-bba0-26e40deb17f3 | -4.86328 | -45.05389 | 2025-09-30 03:47:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06fc4694-5555-30d4-a97c-1f476ac0ccc4 | -11.51245 | -43.54058 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ed22a1b-eb44-39ac-a886-3d3ac87dcf1e | -10.75924 | -45.37321 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b1a7602-dcbe-3af9-a710-745daafc8b30 | -5.24989 | -42.90452 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3878e948-1889-3888-91a5-dd1d51552c47 | -4.89114 | -43.46918 | 2025-09-30 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 946ec2c8-3f8d-3e7a-a77e-19477c7f9e3b | -8.82977 | -46.1901 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04629ece-1631-3df1-857b-5860fc4d710a | -9.57406 | -40.35495 | 2025-09-30 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| bd6739de-f639-3a1c-a3e1-7927807b8f6f | -10.39402 | -49.04375 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 191ffc5b-9da6-3df6-950f-9dea68db0c57 | -9.12952 | -47.63027 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7eb591b-2596-3903-831f-0f417f29e8dd | -8.87694 | -46.6163 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 45fc4d00-0e71-332d-89bf-08d63a05194b | -11.45746 | -45.01799 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69d6be8e-6b2b-3234-9ddd-f81797f2c999 | -10.19958 | -44.89205 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4baa04df-330c-32e2-97fc-bbd7e86d6697 | -4.35149 | -45.5847 | 2025-09-30 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54bf03ff-5fe3-3b39-a315-b109031fa526 | -3.80851 | -47.57219 | 2025-09-30 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f1a0ad3-7ae1-34ed-b086-4213ee49f293 | -11.37349 | -45.06493 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5e4213c-0e90-355d-9b84-f9c14a948948 | -10.0833 | -46.06871 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90166fe4-d9c6-3d08-8bc0-5b2bf222d38a | -7.91219 | -44.60992 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 40a06a64-3482-329a-86c4-60bce28fea80 | -8.07082 | -42.94855 | 2025-09-30 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a8ecc8c-a33b-31a0-8e6d-ae636112fa9d | -8.67197 | -47.70384 | 2025-09-30 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8815c6b4-8709-3983-8494-20c81ed7d271 | -4.40318 | -44.39327 | 2025-09-30 03:47:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6db891f7-8788-3aaa-8bf7-3c77c494a8ec | -7.90871 | -44.62968 | 2025-09-30 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6e266a07-6eb4-3ab1-b109-53fee9d08daa | -8.82403 | -46.19199 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25b6f157-4470-335b-8090-12e279158c08 | -9.98498 | -45.4099 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e4e3063-cd98-3c37-91b5-e0faa6907722 | -10.18919 | -44.90803 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 630ccafd-d16d-3092-88f2-04e0452f41e8 | -9.93755 | -47.45905 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cd5a007-c0e7-325e-b805-dd7e36c2d397 | -9.12801 | -47.6314 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 42941ce1-5b51-344f-b877-c8b2cd38a18a | -7.75847 | -46.64916 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a5ff4d9-6983-3714-970a-a5baf8d57973 | -3.68087 | -38.9301 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f50994f6-75ef-3432-800c-d36a2d01806d | -10.82801 | -47.9645 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1644ccf-f887-3b49-ac0f-35ac218238a3 | -7.83142 | -46.99894 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 128701ec-9955-38f3-a97b-aef8d3f8e8e0 | -10.39081 | -48.14514 | 2025-09-30 03:47:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db965bdd-7ff4-3992-825b-ff4b15548d2c | -10.10676 | -47.78509 | 2025-09-30 03:47:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc063b2d-e12a-3565-b671-fff97dd81e45 | -3.81103 | -40.95525 | 2025-09-30 03:47:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e8c9683-9978-3862-88ae-573fd0354a53 | -8.24148 | -45.51601 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fb58e91-eb35-3848-9153-5fa7ae8bd838 | -7.86273 | -47.25883 | 2025-09-30 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8af8f62d-f4d2-3aee-b83d-d672598d4497 | -9.12722 | -47.64222 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbae2f26-6b8d-3d33-9472-2c1cac508c1b | -7.36723 | -47.05476 | 2025-09-30 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1775f19-ffb2-3ede-bc5c-b2c76563f62a | -4.50649 | -40.72402 | 2025-09-30 03:47:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b35cd155-c0d7-35cf-8fe2-c27ce7897617 | -4.81266 | -42.76645 | 2025-09-30 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc12118e-3e86-33ec-b12d-974ed89b8384 | -8.14433 | -46.36712 | 2025-09-30 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a29af68f-4a00-353f-80ac-c70c3c60c2b9 | -10.1966 | -44.89408 | 2025-09-30 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2fc77ca2-ed4a-3880-bd87-a9b6b8aa358a | -4.81341 | -42.7621 | 2025-09-30 03:47:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58b8f94f-20a2-32a0-9bbb-796feeba860e | -10.83469 | -47.96033 | 2025-09-30 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2124aa1e-142c-385a-8c27-cef8b7387e25 | -11.34688 | -45.06321 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1a32ca7-ec0e-30f4-b96f-89b1aa05d385 | -3.67601 | -38.93763 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f046558-9ae3-3096-be01-a2fb6b8c7f3a | -5.30986 | -43.16141 | 2025-09-30 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6797ca94-d71c-37fc-a554-fc6f2192bb86 | -11.40363 | -44.90174 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83d034de-c471-3e8e-afbe-88550c65494c | -7.80215 | -48.03503 | 2025-09-30 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e3364f-9482-392b-9a8b-59161d36533f | -9.88201 | -45.9564 | 2025-09-30 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9040e1a6-4e96-3800-91c4-87fe85992ed4 | -8.24323 | -45.52729 | 2025-09-30 03:47:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85711d4e-0631-3a75-8b74-d3d9a232e94a | -9.12506 | -47.64736 | 2025-09-30 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b69d58e-bc10-3d62-911c-5beaa89eae94 | -10.06374 | -50.22464 | 2025-09-30 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb3d8f9c-822b-35a8-886f-08919c93731d | -9.99084 | -45.40516 | 2025-09-30 03:47:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66a6d002-02bb-3bbe-b99b-0ddca37797da | -11.44156 | -44.9538 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c5ae1eb-7eea-346a-9205-79873a893a1e | -11.4224 | -43.50809 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d6159ee-a101-345a-97eb-cd81a72ceb4f | -10.75832 | -45.37837 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 667786f6-e839-3ac5-9b6f-6a3c5b941805 | -10.75956 | -45.37003 | 2025-09-30 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0664b78-b5af-3545-be25-bbb64262412c | -4.48332 | -47.67801 | 2025-09-30 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e9000c3-2d45-3212-9c12-ae460a5a3286 | -9.75855 | -47.19787 | 2025-09-30 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5a4fe0b-4f74-38db-9c52-f892e64a9e89 | -11.45895 | -45.01568 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47fc5acb-89a0-3b2d-bf1b-7a960d358d51 | -11.42727 | -43.50497 | 2025-09-30 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 663c67a5-5216-3a8b-ac38-67874a8a629a | -11.46068 | -45.00602 | 2025-09-30 03:47:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b7eb4a8-4da2-354c-b22a-bf3acdac511f | -10.64568 | -48.59576 | 2025-09-30 03:47:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37a23b72-48e5-3ddb-b604-c92b1bf12fc1 | -9.57475 | -40.35085 | 2025-09-30 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |


[Clique aqui para ver as próximas entradas](README26.md)
