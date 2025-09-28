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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6785a938-fe87-3622-b9d8-b8abfc5d0e45 | -15.9076 | -46.2139 | 2025-09-28 12:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 26f8d2a5-8f8f-30e2-8e10-f5b558e2468f | -12.9547 | -45.1618 | 2025-09-28 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8785826a-bf60-3b58-86bc-b3c76ab077ea | -11.9986 | -47.0596 | 2025-09-28 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 22b83f3a-9562-3300-bbcb-0adb2c9d7d90 | -7.7555 | -45.7324 | 2025-09-28 12:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| d4cd9500-4822-372e-a5ee-aa639e860b4d | -12.2825 | -44.0804 | 2025-09-28 12:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 19d10e25-661c-300a-be1b-eaa70fcc97e7 | -12.0214 | -47.9703 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 47c84716-a80e-3bae-884c-b8a009e9b5eb | -7.7972 | -47.0241 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 50f27330-6ec9-3952-8305-f92ba7035f1b | -11.9456 | -47.936 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 45d9ed55-a3ac-3fed-918b-df47c0d05bd5 | -12.0019 | -47.995 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 4bdf7861-cb43-39f5-a790-4af239ef33d8 | -15.8879 | -46.2177 | 2025-09-28 12:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 7b072103-1178-3994-be56-9d734dc834ea | -14.7655 | -45.6854 | 2025-09-28 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8f1797b2-0805-36d2-963a-d55b5f9cf779 | -8.1611 | -46.4122 | 2025-09-28 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| fbb871f2-d9ea-3a72-a8a9-00be65a4b015 | -11.979 | -47.0847 | 2025-09-28 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 65844d75-d90d-3991-b84c-ccef63bff193 | -12.9156 | -45.1912 | 2025-09-28 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5251f3f2-dcfd-365f-a494-f61d12891221 | -11.4409 | -45.0229 | 2025-09-28 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d6284066-49c0-3313-8504-5eaf60a995b4 | -11.4413 | -44.9998 | 2025-09-28 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 9e0d3979-7891-3157-acb0-a26c8a8e15bb | -11.9794 | -47.0622 | 2025-09-28 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a7d3c7cb-a4ad-33ee-bf60-c34c26e37e55 | -7.7785 | -47.0258 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 127.8 |
| ee6f1e71-415c-35d4-ba4d-bbc749471972 | -11.3892 | -46.9622 | 2025-09-28 12:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| d929d43a-338c-3f72-911b-548b31522dd7 | -7.3847 | -47.0378 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 278.1 |
| 8b1c1b7d-7fba-369d-98ac-21a922576104 | -18.1977 | -53.3208 | 2025-09-28 12:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 147.0 |
| fd30d856-a493-31ea-b862-6d1fda50c87a | -7.7412 | -47.007 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 81f53fb6-568c-3e45-848b-d569c679d0ff | -7.3659 | -47.0394 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 81b64908-aa1a-3f54-910e-e797b04019c4 | -9.0913 | -45.8673 | 2025-09-28 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c53d8bc9-7482-356a-b99d-455da5795b46 | -11.9633 | -48.0223 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 82de2293-acee-3dc8-948d-a925c2e5d3c6 | -11.3889 | -46.9847 | 2025-09-28 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| b7e967ba-7c29-3062-b0cb-dc7fdb3ef25f | -11.9982 | -47.0821 | 2025-09-28 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 47553a7e-cce9-39ac-a78d-a10f2209e86a | -7.7782 | -47.0479 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 4afe96e0-7907-3e3c-8e86-2df216edf45c | -7.3849 | -47.0157 | 2025-09-28 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| a3b646d6-fe36-3af9-8a97-a1f09f3c4d32 | -11.4045 | -44.9127 | 2025-09-28 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 82c55212-7160-3e38-b28e-c1f39feba520 | -11.9828 | -47.9976 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0235cc0b-60aa-3c9b-a6e7-578dd638fc83 | -8.2856 | -45.4545 | 2025-09-28 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 456259ca-dbac-3036-88a6-c12014e813d3 | -7.3661 | -47.0173 | 2025-09-28 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 93305333-b195-3b4b-9991-c94a0b364ecd | -11.4083 | -46.9597 | 2025-09-28 12:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| b123522a-499d-340d-867b-17ab0445878d | -7.7414 | -46.9848 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 18eb62cf-7d79-34a0-9c8c-209710be3c1b | -7.7604 | -46.961 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a29ceffd-26ea-3cfe-87bb-9f003b09c2a1 | -7.7602 | -46.9831 | 2025-09-28 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 641744fb-3a0d-3155-835b-a77c05968595 | -11.4417 | -44.9767 | 2025-09-28 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 7d5e014d-43dc-3bc2-a4d3-a632516d850e | -11.946 | -47.9138 | 2025-09-28 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6bd1ee41-97be-341f-8f42-4f869a368643 | -13.6122 | -48.0787 | 2025-09-28 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 62b6307e-de95-35d2-9732-92035da4508b | -7.8823 | -44.5594 | 2025-09-28 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 444f4b34-969d-336e-8b84-5e4f79c090b9 | -8.2668 | -45.4564 | 2025-09-28 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9c01744e-d5a7-3544-a5d0-f74a9a05329c | -11.4413 | -44.9998 | 2025-09-28 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 16d66ee1-265b-3ef9-94f2-d122a01d4167 | -7.3847 | -47.0378 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 298.3 |
| 08491537-74cf-36f2-ac31-3f9354aa8cdb | -12.4167 | -44.1057 | 2025-09-28 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e226ab3c-00cf-35b7-bea5-5e38e6c6bb55 | -7.7602 | -46.9831 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6baad87c-6a7c-3cbc-a977-8a4e69cabe6e | -12.2825 | -44.0804 | 2025-09-28 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 0e3763b4-48f1-3108-9213-ae4bd9c26b4f | -7.816 | -47.0224 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| b02fb596-94bf-3270-9acd-a470301a97d4 | -14.7846 | -45.7051 | 2025-09-28 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 291.1 |
| b28c71f7-9bda-3629-a60d-ae7af4a317b9 | -12.9156 | -45.1912 | 2025-09-28 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 025a5307-ff62-321a-a23d-3e55b36ebd45 | -11.4409 | -45.0229 | 2025-09-28 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b5ff7b23-3961-3fb1-982f-a42a11237e10 | -7.3661 | -47.0173 | 2025-09-28 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 17c65c6e-1cc6-3605-bff8-e94d63668ae4 | -13.2777 | -50.6846 | 2025-09-28 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 5b3e9516-fd3e-3df8-a76d-85f9939f9201 | -15.8879 | -46.2177 | 2025-09-28 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 0cdba12e-cd6f-372e-bdc6-de343b883b71 | -7.882 | -44.5824 | 2025-09-28 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f0ad256d-a260-3c06-8282-b0a85146b5a7 | -7.8634 | -44.5612 | 2025-09-28 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 056eb7f5-8179-3d15-aaf8-a770653f3d09 | -11.4083 | -46.9597 | 2025-09-28 12:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 6d312d2f-8a91-3d44-b5c6-da81b9ac511c | -12.0214 | -47.9703 | 2025-09-28 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 26930bd7-ae3c-327b-a328-698c7f0c79e0 | -11.979 | -47.0847 | 2025-09-28 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 57a8a47f-1f92-3758-8c49-ac849d835afa | -7.3659 | -47.0394 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 244a34c9-23e6-3da2-8e5c-9940ecd9afe8 | -8.2856 | -45.4545 | 2025-09-28 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1736ea7c-17cb-38c6-840c-705c3d375252 | -12.3018 | -44.0773 | 2025-09-28 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0751628c-957e-3fee-ac1b-5492cf22edf9 | -13.011 | -49.4423 | 2025-09-28 12:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| bb1a8a0d-baf9-3330-af89-36b8e2243bdd | -11.3834 | -45.0312 | 2025-09-28 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 244160c3-5e40-3935-a357-0c8d65f97028 | -5.9004 | -43.6976 | 2025-09-28 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5a691bf5-ba6c-3690-81dc-b1b178f428fa | -18.1977 | -53.3208 | 2025-09-28 12:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 97564932-0318-33a8-a741-12e1ac001610 | -11.9986 | -47.0596 | 2025-09-28 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 1d3488c9-c414-3159-bab8-e0caa08bc53f | -7.7414 | -46.9848 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a262a360-6ca9-3587-8a6d-d69f02061001 | -13.2966 | -50.7036 | 2025-09-28 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 48b2a3ad-613d-39c5-86b2-0c1325164676 | -13.2773 | -50.7061 | 2025-09-28 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0d913b4b-323a-395b-930c-725120b03d0e | -8.8759 | -45.0274 | 2025-09-28 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 223.9 |
| 46dbd8e5-b982-391e-a16e-38868f5f3dc2 | -13.2969 | -50.6821 | 2025-09-28 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 4627479c-2fe4-3d5c-8f79-91a5934f61f5 | -13.6122 | -48.0787 | 2025-09-28 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 668684e7-1b2a-3d98-9de6-fe59a4100ad9 | -7.3849 | -47.0157 | 2025-09-28 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| a2473e45-6eb5-3227-a8cb-56cb905dc00e | -15.9076 | -46.2139 | 2025-09-28 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 04ef839f-cacf-3dbc-bd58-cdf01d5cdc9d | -11.9824 | -48.0197 | 2025-09-28 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 1c1ee0f6-0180-374b-b4a1-f43148851fe7 | -7.7604 | -46.961 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a2f04b10-37e4-34b6-903f-be818862ccec | -7.7785 | -47.0258 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 79345269-a6c8-330c-abec-496d722f1e0c | -15.8873 | -46.2409 | 2025-09-28 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 441fc772-1611-3eda-b2a9-b82545705692 | -12.2335 | -46.7568 | 2025-09-28 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3c011480-47fd-3f0c-b242-a813fe0255fe | -12.9547 | -45.1618 | 2025-09-28 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a4a2a8cc-c5fa-35c4-98c0-1859ba926a32 | -7.7972 | -47.0241 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 6701d7f6-5a86-3a29-b075-04353864cc73 | -7.7782 | -47.0479 | 2025-09-28 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| c2071875-f4d3-3e44-b954-4630c1ebc03c | -12.4162 | -44.1293 | 2025-09-28 12:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9a1ec564-cf03-3a23-9be5-119c59ba4dc9 | -13.6267 | -47.3152 | 2025-09-28 12:50:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ba170824-049c-3bca-b2ce-6aa9f96e3cae | -7.1571 | -45.5158 | 2025-09-28 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 17a8fe79-ddfc-373e-bf20-7cccb2a375db | -13.7893 | -47.8957 | 2025-09-28 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d8158fc2-4e17-36c7-a251-fde5dfbf4597 | -9.3013 | -45.7082 | 2025-09-28 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| cb90109a-9144-3156-aa7e-2a1165d9349a | -11.9633 | -48.0223 | 2025-09-28 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| cca771e8-51e6-3e47-9ff2-83655370d75f | -11.9828 | -47.9976 | 2025-09-28 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7ffa3f42-9bb8-3815-be9c-f16804014217 | -8.8226 | -46.2115 | 2025-09-28 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| eb7e5008-4043-399c-be2c-75304d6c84eb | -15.159 | -46.422 | 2025-09-28 12:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5e7624fb-ed52-337f-9800-80d25dec7b38 | -7.7555 | -45.7324 | 2025-09-28 12:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ec14af10-51a5-3301-a843-6ed4d510dfd5 | -14.7851 | -45.6818 | 2025-09-28 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 2dd29cc8-506e-3c72-9ca2-2f2fdac554d9 | -11.4604 | -44.997 | 2025-09-28 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ae85959e-3630-3766-aa59-81c690c5eb37 | -13.2773 | -50.7061 | 2025-09-28 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e3371a7e-17f3-3026-a1c3-d4e675e452af | -12.9547 | -45.1618 | 2025-09-28 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f3759ddf-b48d-3bb1-af18-ba57f15f6db9 | -8.8415 | -46.2095 | 2025-09-28 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fdf0b54f-34d6-3a90-9eea-939dd665379f | -12.0214 | -47.9703 | 2025-09-28 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| fc8edf44-dfa0-3d60-8b8b-2f17022a827e | -7.8634 | -44.5612 | 2025-09-28 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |


[Clique aqui para ver as próximas entradas](README98.md)
