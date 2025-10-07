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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90248dbb-0952-3dba-83ee-74d8c688d71d | -9.1786 | -47.84 | 2025-10-07 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 7999b538-d38d-3935-8b67-daa5b9c6fcb2 | -7.6648 | -45.4471 | 2025-10-07 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 50cadf62-5932-329f-9665-57c9b23ceea8 | -7.0046 | -42.3091 | 2025-10-07 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 60ff85ad-e03c-37e6-a28c-6961a7253ea7 | -9.921 | -50.2109 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7689f09a-b169-3004-95ca-a01ce3626ccc | -8.9207 | -47.3816 | 2025-10-07 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1db04498-180f-3fd8-a963-ec813496cd59 | -11.0262 | -50.9067 | 2025-10-07 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| d3dc1ecd-f3f7-370e-94c1-fa79c9537224 | -10.3854 | -47.9956 | 2025-10-07 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e5c1fe98-ddda-3929-b1cf-cc906499d5da | -11.9963 | -47.1944 | 2025-10-07 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 34b95d2f-3d36-3c4d-8f42-d5c6f064891c | -8.8794 | -47.6722 | 2025-10-07 13:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 8a944e42-8dad-3faa-a22b-3e2f89c9fc8c | -8.1324 | -47.2589 | 2025-10-07 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d08325a6-221a-33bf-8aaa-4437aed1bf86 | -11.2436 | -50.2645 | 2025-10-07 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 202e1381-7361-3770-acd9-28b1ca4fbbaa | -8.5395 | -46.2406 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b0bbc206-f12a-3b8b-850b-b8faa242786b | -7.7182 | -42.5688 | 2025-10-07 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 0ef55be5-9ea6-3087-9777-6e6a474cecf1 | -10.0868 | -50.5141 | 2025-10-07 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 750c6a45-ab9b-3dfe-a894-c356cab55fc6 | -13.0747 | -48.002 | 2025-10-07 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8a43c967-c823-3dfe-84d8-f576110a5d7c | -12.9106 | -54.7147 | 2025-10-07 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1261efed-c5cc-34a4-af97-b23b1da5db2c | -10.4054 | -45.3931 | 2025-10-07 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b141c78d-8bf3-33e1-b401-aae7e6575f8f | -10.4283 | -50.3732 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 52c77a4e-149e-34c7-ac8b-29283274e8dc | -10.4655 | -50.412 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 0358a231-b726-3911-a54a-3f1380d36733 | -8.1804 | -43.3445 | 2025-10-07 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 282.5 |
| 57d44b71-1fdd-31a1-a3a9-c20246d62ed8 | -14.8645 | -51.4158 | 2025-10-07 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| de6c40a8-12e7-3f8a-8576-e25bb29104ff | -8.5584 | -46.2387 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3bcf79b0-ec78-3051-b9ab-f0888361a1ba | -8.6521 | -46.274 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2e592f6b-4107-36a8-82cd-fcb6333ca06c | -8.5207 | -46.2425 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 67faa589-9bb8-3cf4-8d87-bf88b231c725 | -8.1801 | -43.3679 | 2025-10-07 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.1 |
| bb20ba23-ad0f-3895-ac08-cb863526a301 | -12.7637 | -50.4921 | 2025-10-07 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 157ae7c0-b178-32df-8ccc-ed12003af46c | -10.428 | -50.3946 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| f06733e4-d06f-3de6-87b8-57680a664233 | -13.0939 | -47.9992 | 2025-10-07 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ea2a5ef2-91ae-30ad-a16a-1cbea540141a | -10.2129 | -54.1262 | 2025-10-07 13:50:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 8ac1847e-a9ce-3fcb-b8ef-705e440401b0 | -13.7927 | -45.7627 | 2025-10-07 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 252.3 |
| a80c50e9-76a1-32d6-99f9-743dba02f2dc | -8.2159 | -49.875 | 2025-10-07 13:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 88364842-99a5-3f9c-aa7c-ca6fba4f5e82 | -8.4821 | -46.3136 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| bce7ac33-9ff0-333f-97e9-4aa5e8cadfde | -8.501 | -46.3117 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 22eaf668-98dc-3d5d-9a54-717bf01c7825 | -12.1655 | -50.9073 | 2025-10-07 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| cff9c9ca-f5e1-3e90-9287-c16f8b82fe12 | -19.0295 | -44.7327 | 2025-10-07 13:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 78a5ecf3-5b15-32ce-92ba-39aa15761a55 | -8.6397 | -47.2769 | 2025-10-07 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| c77fcea8-3090-3f80-9aaf-c749b8789ad6 | -18.2856 | -45.4587 | 2025-10-07 13:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f65fee3f-ba96-3e97-a8fa-65d11b85f43a | -8.8717 | -46.7878 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 14fa9bf1-670b-372e-be13-5f9315ebcc20 | -7.0043 | -42.3329 | 2025-10-07 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 811422a0-b3c2-33f5-abc2-b4888b97e028 | -8.6519 | -46.2964 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2200d588-6294-3ffb-a70f-46003bca30c0 | -11.7217 | -45.3738 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 6a734570-07c5-37c5-a211-ec1492b496ee | -11.6859 | -46.3366 | 2025-10-07 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| b6e5af56-38ea-30c3-a4ee-86e8d899e627 | -8.613 | -44.9189 | 2025-10-07 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| d1698113-b74a-379c-8a25-064574f0d6d5 | -12.6159 | -44.7519 | 2025-10-07 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5a2e8372-2281-320b-8839-ec463068420c | -10.3913 | -50.313 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d2f08129-ee05-3b59-ba83-8a75798669df | -9.1528 | -49.9425 | 2025-10-07 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 67672687-d54a-365c-b1aa-a97dbf996fb8 | -13.2426 | -47.2391 | 2025-10-07 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| bd33d41c-e6bb-3463-af44-0d3e6579bf29 | -9.6804 | -45.6645 | 2025-10-07 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 3df96ea4-acec-3e66-a507-357060e2803d | -12.4919 | -54.7158 | 2025-10-07 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 80a7efb1-4eed-39d5-bc99-9554df55b015 | -8.6211 | -47.2567 | 2025-10-07 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c3e101f7-9e24-3ab3-bb66-a9416e016615 | -8.0866 | -44.791 | 2025-10-07 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3e77add1-c2b4-3e55-ad31-8edeabcc011a | -7.8119 | -44.1516 | 2025-10-07 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6371f6e5-ce32-31ec-9b17-46906ec6bbf7 | -10.7468 | -46.6634 | 2025-10-07 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f2dbd409-ca8b-3eb7-9751-7307347e0f2f | -10.4245 | -45.3907 | 2025-10-07 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| aa453721-e529-3383-a4e6-4521e77afdb3 | -8.8986 | -47.6483 | 2025-10-07 13:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fe8949fc-99cc-3240-88b0-bd1228b36d08 | -11.8029 | -45.1087 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 17ee2c97-415a-3234-9907-01c5aec33c39 | -8.921 | -47.3595 | 2025-10-07 13:50:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| d316a29b-ba57-3a22-b60f-5dc4a73fa813 | -15.6202 | -52.5501 | 2025-10-07 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5e771062-b2b2-310a-81af-a66c814fcadf | -11.8025 | -45.1318 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5b9d5460-de19-30fd-900a-c2d6d5ce3502 | -12.1652 | -50.9287 | 2025-10-07 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| f8193798-e0b8-3605-9b77-711b62d66fdb | -12.4669 | -45.5155 | 2025-10-07 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7a00fff6-ed33-38b4-8c0d-0d408b2fe90c | -11.0454 | -50.8834 | 2025-10-07 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 0d6bea7a-6db4-32a0-be3d-1271d7e8b818 | -6.9704 | -42.0023 | 2025-10-07 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 114a1a22-0eba-380f-8217-a3093d054db0 | -12.9816 | -46.7824 | 2025-10-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6fca7df9-f44c-301e-a5a5-29b048cf004d | -15.6003 | -52.5742 | 2025-10-07 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| af38ef60-fd86-3d09-9591-47f71bdf66cc | -11.8221 | -45.1059 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| fddb0bdb-784a-302c-bc0e-79046db063e6 | -12.9619 | -46.808 | 2025-10-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a6aa80a0-1a3c-38ff-851f-87365f8a717f | -11.2433 | -50.2859 | 2025-10-07 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| db14882e-2775-3640-900c-7840e02a7043 | -11.8447 | -44.9176 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 917a6790-7d27-33b9-ad72-35c23054e413 | -9.1978 | -47.8161 | 2025-10-07 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 37b272a0-9eed-32d3-95f8-9fa7993cf1d6 | -18.9852 | -47.805 | 2025-10-07 13:50:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 138.1 |
| e299d989-4542-3e00-ada0-8efca1710c9c | -11.8823 | -44.9583 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f4ebce88-3312-3189-a934-7c2812e5b6df | -15.1548 | -45.73 | 2025-10-07 13:50:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7e824fde-669f-33a4-ad0a-6c564f9bc9d2 | -10.4291 | -50.3091 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c1caf371-df7a-3aae-907c-ce1d8c8ba745 | -7.4669 | -43.0674 | 2025-10-07 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 942df8f3-cfb7-3aae-9429-fbb69b93a228 | -7.1815 | -41.6931 | 2025-10-07 13:50:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 10f1b256-456a-39b7-96c5-6c0fdf587cb2 | -18.9846 | -47.8282 | 2025-10-07 13:50:00 | GOES-19 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 129.1 |
| bd89490c-651f-32ae-8db6-c5a2f04a56c1 | -11.8635 | -44.938 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 650ced3e-94a9-351c-93c2-6970d11c152b | -15.3737 | -47.3201 | 2025-10-07 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 90cfe390-a36f-3cc0-ad26-593d15a65a39 | -9.1789 | -47.818 | 2025-10-07 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| fb3cbb6f-9664-34c2-9285-51a6943e4f00 | -15.5808 | -52.5769 | 2025-10-07 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 4f9642b6-1fef-3848-a5a7-54ecfb475673 | -7.4666 | -43.0909 | 2025-10-07 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 9473f698-09aa-3756-9109-913a6e01b95e | -10.4102 | -50.311 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0f6cd0e3-0302-36b5-80ef-d30a7506e5e0 | -10.4288 | -50.3305 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 6ab013b1-00b5-3a01-99e0-af2eea16232c | -7.0235 | -42.3073 | 2025-10-07 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| e2e09450-d0b6-3278-8d38-ecd7015c4621 | -13.7923 | -45.7859 | 2025-10-07 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 8c11e60a-f646-33a4-971e-cdbf50646aca | -8.6208 | -47.2788 | 2025-10-07 13:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4a8d26f4-83a9-3fa2-879a-5a76a2d51a68 | -7.6932 | -46.2548 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b5bcb87f-7f86-388f-a27e-4ff753116805 | -9.1975 | -47.8381 | 2025-10-07 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f11a559a-cbea-39b1-ba5f-66d722b26bd7 | -8.4824 | -46.2912 | 2025-10-07 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0be5500b-dc0f-3ef6-848f-95b3dd78f9d4 | -11.8422 | -45.0567 | 2025-10-07 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 303668a6-85c0-3ed2-af8c-727bb4c4e58f | -12.9103 | -54.7352 | 2025-10-07 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 987bfecf-1d1c-321b-b8ff-712be58ccc52 | -9.9207 | -50.2323 | 2025-10-07 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 45bb9317-e32f-325c-810f-4916b4bbf0de | -10.1573 | -45.4701 | 2025-10-07 13:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 61233989-1cbe-3792-b400-fcdb720a1155 | -14.7088 | -48.399 | 2025-10-07 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 399794f1-70e3-3bad-b9e4-6926dd839bd3 | -11.0451 | -50.9047 | 2025-10-07 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 8248dd88-8cee-3f91-8bb1-456081282466 | -9.6098 | -46.6416 | 2025-10-07 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b70e0da4-2cf8-30fd-b4ce-1824525c80b3 | -7.4672 | -43.0438 | 2025-10-07 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 4513bd1f-a866-3f9d-84e7-8492aef7d1cd | -12.1843 | -50.9265 | 2025-10-07 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 61ce3af9-a842-3f7d-85de-b373bd4d8cf6 | -9.1525 | -49.9639 | 2025-10-07 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |


[Clique aqui para ver as próximas entradas](README125.md)
