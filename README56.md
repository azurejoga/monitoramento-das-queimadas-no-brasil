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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fed15815-95a2-3c5e-8946-8e3b70f9e1eb | -12.16616 | -47.7622 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db118551-23bb-387b-be92-c2c9626be815 | -12.16561 | -47.76588 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86262a47-a872-3e82-a32b-b786ae28e8c3 | -12.1628 | -47.76167 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5765715a-6373-3f4f-a2ff-e3bbcffa4643 | -12.16225 | -47.76536 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 38b5abdb-97c7-316a-9f34-a6cb4fa9a3eb | -12.03892 | -46.85814 | 2024-10-08 04:34:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1106dd93-53f7-390a-a359-b3b0b5fd1206 | -11.73512 | -46.96572 | 2024-10-08 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 722d74ef-16f5-326c-8cd7-44fb1ce35125 | -11.73456 | -46.96951 | 2024-10-08 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1581fde0-6dcc-305f-bfbb-c668ece59253 | -11.69486 | -47.67065 | 2024-10-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e900db3f-8517-3c68-8355-c0bf84ce30ba | -11.28384 | -47.58156 | 2024-10-08 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e84848f9-4209-3523-9ce2-10f11182f7ec | -11.20023 | -46.58548 | 2024-10-08 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10f13e40-55d9-3816-b4d7-5bbad226484f | -11.19965 | -46.58935 | 2024-10-08 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c45dee35-6e7a-33c8-8243-5de484f7d77a | -13.1793 | -47.98713 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8f2ba420-c284-3f2f-a770-b690e27efd43 | -13.17874 | -47.99078 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e4a9c4e-2536-3137-92d2-88f64410e9b8 | -13.17818 | -47.99444 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ffc9c46-f00d-30f1-b198-428f8b98d6e3 | -13.17482 | -47.99389 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 691c4f38-3f25-39b4-a7c2-be198fef77b8 | -12.54348 | -47.65131 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 396534f6-2322-309b-af4b-b22b9c1d5d29 | -12.53954 | -47.65449 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1192976f-2e24-3134-b7d8-92e5942f8119 | -12.46853 | -47.31196 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78336a8d-172a-36e3-8cb5-5d47b2fc2d50 | -12.46511 | -47.31142 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 309ab172-c795-39d8-9fb7-4c5bc6d6acc6 | -12.46455 | -47.31519 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4e5c7d8-fb26-37a9-9f03-4af565ec5cb0 | -12.4617 | -47.31088 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30c20b8c-c535-3ada-b520-9bbe0e6e24c7 | -12.46114 | -47.31465 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93154d74-861d-364f-a4f6-5cf7304d9671 | -12.39632 | -47.1848 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e462d0cc-16aa-35b0-9f3c-a97088f0596c | -12.39392 | -47.05952 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dc9660b-8368-34fe-9a73-8f005b490a0e | -12.39335 | -47.06335 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6709897-b37a-3f23-acba-cad00e6f062e | -12.3929 | -47.18427 | 2024-10-08 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edb665b3-995e-3809-a440-8d3f07ab54f3 | -12.36361 | -47.09784 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a519ffc-b696-3598-89e7-0577f573b00e | -12.36305 | -47.10166 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e2be710-5959-3bd5-82fd-7ada4f65b10c | -12.36074 | -47.09349 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa95a668-61f6-3fb4-b8ff-76e57c586902 | -12.36017 | -47.09731 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77352fe0-1fda-3176-9771-b3b62a745bca | -12.35961 | -47.10113 | 2024-10-08 04:34:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a662cc8b-8f5a-3dad-bfc0-445358e5fca5 | -12.3573 | -47.09295 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 530d50a8-fd07-327f-8c4b-ac8ee209b8b0 | -12.35674 | -47.09677 | 2024-10-08 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94e293ea-a305-3273-b45b-f9e6695c77d0 | -12.28267 | -47.64126 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09e21dc7-c1fc-3bc1-b84a-fe14bc3a2383 | -12.28211 | -47.64493 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3337ae19-b2d0-3c81-8961-3459886ccbdb | -12.27984 | -47.63705 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67c07ea8-eb2d-3b52-a82f-e352a22c0ed2 | -12.27929 | -47.64074 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e142419d-c83d-369a-b8d3-cc4415f6a3ba | -12.27874 | -47.64441 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8a38f2b-e243-382b-865a-6c13952bc288 | -6.13464 | -47.21225 | 2024-10-08 04:34:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29077b34-7cd4-33b9-977c-46a66bc1fb44 | -6.1341 | -47.21572 | 2024-10-08 04:34:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf6566c4-0744-3105-ad0e-d8d20d930771 | -6.13133 | -47.21173 | 2024-10-08 04:34:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd5cf98a-8b7b-3c32-afb2-a3080d3bd2dc | -6.13079 | -47.2152 | 2024-10-08 04:34:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 740a4c7f-0457-3561-869a-dd0638ee859e | -6.05305 | -46.5974 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a72240db-f00b-3a00-87e1-97082e171d99 | -6.0525 | -46.60094 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dbae1f9-2d26-3d0a-acc9-f33fcd6721c0 | -6.05196 | -46.60447 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdb20a17-57f3-3ebb-83d3-3a20c07bdefb | -6.04193 | -46.60294 | 2024-10-08 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 779ff895-df10-3020-8b23-b2d4ceea2d4e | -7.89586 | -47.72087 | 2024-10-08 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7949abd4-90da-3fd9-8fe5-a787e5b5c09e | -7.89215 | -47.72022 | 2024-10-08 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eee2e46c-7a68-3a00-b500-556bf6922439 | -7.89161 | -47.72369 | 2024-10-08 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a360d6b-3512-39ab-83fe-3622aa6748ff | -7.63309 | -47.74654 | 2024-10-08 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 975df268-b8e8-387f-a5a7-0ef39765c589 | -7.63254 | -47.75 | 2024-10-08 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e9fafbf-2723-3cda-9d36-19be53609c17 | -7.62924 | -47.74949 | 2024-10-08 04:34:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 692fba76-1440-39db-8296-1f365e195b83 | -7.43472 | -48.35987 | 2024-10-08 04:34:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b753ea81-037c-3ef5-8188-d239ff9b63cc | -7.2491 | -48.00445 | 2024-10-08 04:34:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3808908-7307-3d68-a7c8-3a0fd71bf250 | -7.10118 | -47.83911 | 2024-10-08 04:34:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fb16f40-3ad9-3a62-b37b-1078b77ad801 | -7.09358 | -47.86613 | 2024-10-08 04:34:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc6dbe13-4f44-355a-8baf-3025c1ff0ac7 | -7.09303 | -47.86959 | 2024-10-08 04:34:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70633361-e579-3e80-9760-517a953163db | -7.09028 | -47.86562 | 2024-10-08 04:34:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95c415bf-5fcc-3dcb-bc20-ea41835c0625 | -6.91572 | -47.65441 | 2024-10-08 04:34:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63342383-c5c1-30e4-87d1-e93f689947ee | -6.85673 | -48.00918 | 2024-10-08 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3d76e08-d8e8-3824-9d50-d0777fdd425f | -6.85224 | -47.97314 | 2024-10-08 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d4b9a44-9876-3902-9d75-274f07633180 | -6.76042 | -47.99391 | 2024-10-08 04:34:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c964304-292a-3486-8532-6fddaaad10f8 | -6.648 | -48.10698 | 2024-10-08 04:34:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e471b91-6a25-3c3d-b7cf-61cab20ea1e1 | -6.66737 | -47.11026 | 2024-10-08 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a4792c53-d1db-3f5e-b30f-bf300be25ee1 | -6.66405 | -47.10974 | 2024-10-08 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebaf71de-e271-3d94-a31e-06d6275754a3 | -6.66351 | -47.11323 | 2024-10-08 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0228397b-3f0e-366a-b623-a97c8e1bbc15 | -6.66073 | -47.10922 | 2024-10-08 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f8e7fc1-d5ea-3099-b8d2-1ccbb4102048 | -6.66019 | -47.11271 | 2024-10-08 04:34:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f3962df-14e0-34cf-ac1f-c2f3deda48ef | -8.32649 | -48.01288 | 2024-10-08 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73cff09d-e9e9-3f08-aba0-b327849a981a | -10.72343 | -49.02146 | 2024-10-08 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81b069cb-ea08-3d1f-8904-c2e93dfafc70 | -10.55504 | -47.78754 | 2024-10-08 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55d5bc50-e2dd-3c93-97df-837a298d30b5 | -9.53939 | -47.8914 | 2024-10-08 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b156cae4-870c-3bfe-ac49-d02096708341 | -12.1867 | -47.98806 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b2ef59c-039b-33d1-ac34-fbb2f051019d | -11.7943 | -47.88229 | 2024-10-08 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df9870a7-29e5-3b51-abfa-54a06d9a79c1 | -12.99675 | -48.60011 | 2024-10-08 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e67ea9f1-bc43-3ff7-9f86-18f541156e36 | -12.78076 | -48.21382 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19786b78-18ea-32f5-aa83-0929e8a21d6d | -12.77742 | -48.21329 | 2024-10-08 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dab3b090-e284-3737-8bb3-a72ce0885be6 | -12.53567 | -49.48642 | 2024-10-08 04:34:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aebf2396-ebc4-32aa-931a-158f56a9060b | -5.7548 | -49.25158 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0746de15-1877-3f24-b027-8c5276dc1a03 | -5.75422 | -49.25518 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87c1e852-01d5-36f0-bab0-3c4cb0bf44c0 | -5.75142 | -49.25105 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb1c97ce-bbfd-3ee2-8213-95ab1784259a | -5.75085 | -49.25466 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baef6849-a29a-3f64-8c32-8a95228f4c5a | -5.74805 | -49.25053 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1235b7e-c776-36d4-a744-93394667d6da | -5.74747 | -49.25413 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71457ada-d5d7-3d77-ba38-aa2a882ba042 | -5.71084 | -49.26688 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a1a9e44-3631-35bd-8f96-e6196985c770 | -5.71063 | -49.31132 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f2e36c3-4261-31cf-880c-67cddb6c8c1b | -5.71005 | -49.31494 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43f57dff-8adb-32e3-b15e-64cd2ee3664d | -5.7083 | -49.32579 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c1352d3-9d44-3b0a-8113-527a695dfc7e | -5.70747 | -49.26635 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e93e48c3-ca3d-3a40-ad25-6c8d0a706bc3 | -5.70492 | -49.32528 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fe0315b-ced7-369c-9661-f7317f5647fb | -5.58764 | -49.46408 | 2024-10-08 04:34:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a975d81-c3ff-3bd4-937d-5d3275ba08c6 | -6.23096 | -48.16035 | 2024-10-08 04:34:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e0cac75-17cb-3829-8f06-813890b89b80 | -6.23042 | -48.16381 | 2024-10-08 04:34:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d3904b3-c92b-37db-ad8f-2d7dd2571eb5 | -6.22327 | -48.16622 | 2024-10-08 04:34:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdadb4cf-46e1-3515-95df-429fe2d898c2 | -7.39867 | -49.65426 | 2024-10-08 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e08436f7-da9a-3235-b48b-2b8016ac0954 | -7.39808 | -49.65789 | 2024-10-08 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d021d50-9465-375c-9a32-66250a44c190 | -7.27001 | -49.48584 | 2024-10-08 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3780ce6-f410-3689-8a01-79737fd97bbd | -7.26664 | -49.48531 | 2024-10-08 04:34:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c36d1393-fb18-3262-8721-8d580815b2fd | -9.12676 | -49.66415 | 2024-10-08 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 087cc131-cf13-3c77-8ccf-ad7f20e9b0d8 | -9.05165 | -49.71008 | 2024-10-08 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README57.md)
