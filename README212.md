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

## Dados Diários - Página 212

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca996b3e-6fe0-3fdd-891e-2f6303c0dc14 | -12.0128 | -47.3486 | 2024-10-03 13:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| bcc0a6e7-5352-3c6b-a7bd-28901ab16a33 | -11.9737 | -47.3986 | 2024-10-03 13:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 235.1 |
| db9e4e1a-649e-3001-bc9f-e89a92555eb5 | -11.9741 | -47.3762 | 2024-10-03 13:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1d5fe754-d72d-3d17-8102-0abe085fb6d0 | -11.9671 | -50.181 | 2024-10-03 13:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 83410ccd-393e-32c5-8af2-152c45ad2b8b | -12.7815 | -50.5758 | 2024-10-03 13:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| fc921693-d791-30e1-a5aa-c0f6c598e531 | -13.1976 | -48.6489 | 2024-10-03 13:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 18dd24d2-7901-3d6d-82c0-2a1f4c7e1832 | -13.0402 | -51.1432 | 2024-10-03 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| abfac2eb-9ae4-33e4-9fd9-d24fade20d54 | -13.0783 | -51.1599 | 2024-10-03 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 67cdd6b7-01fb-3d82-a83c-a686e42ca1fe | -13.0406 | -51.1218 | 2024-10-03 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a7fab512-b8b6-3ae1-a954-e9a5d60e8a24 | -13.0591 | -51.1623 | 2024-10-03 13:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a2f44cee-187b-3a00-b4a3-dfd18fe7366a | -13.0835 | -50.8382 | 2024-10-03 13:06:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| eab39ee7-5824-3e22-8e64-df438af7e0ba | -13.198 | -48.6267 | 2024-10-03 13:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cb0ea832-349d-3223-bd2e-7e04cbfde001 | -13.6339 | -51.1961 | 2024-10-03 13:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| fc5ed1c5-fbc0-3a37-80db-bc6005628fca | -13.6342 | -51.1746 | 2024-10-03 13:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e67a521b-4627-3262-b013-b07e519c508c | -14.7017 | -48.7559 | 2024-10-03 13:06:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e46c1b17-a116-3492-8e53-0e036a70ce35 | -18.8927 | -41.2248 | 2024-10-03 13:06:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 134.8 |
| dfd625b5-38e5-372c-a67e-8fd57f825ab0 | -18.8731 | -41.2048 | 2024-10-03 13:06:50 | GOES-16 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.1 |
| c729b4d4-342c-3be8-a777-8282229dd26e | -19.0148 | -43.1749 | 2024-10-03 13:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| 66308d85-2238-380c-ba6b-bcff3a2f1a34 | -19.0344 | -43.1944 | 2024-10-03 13:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.8 |
| 419197de-2260-3461-8953-845fde55ab8e | -19.0141 | -43.1998 | 2024-10-03 13:06:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.0 |
| 40f8a7e7-671f-3da4-9b13-e57643eb329a | -19.0932 | -48.2876 | 2024-10-03 13:06:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 7c32ddcf-e8e1-3157-a1b8-f2ab6f1a6037 | -19.2954 | -42.6032 | 2024-10-03 13:06:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 142.7 |
| 2958a820-1987-3acf-b0f2-72b3f5e7fb3b | -19.2962 | -42.5779 | 2024-10-03 13:06:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 132.9 |
| 3b6f100b-0299-33ad-9745-611978c88e09 | -6.9075 | -44.2836 | 2024-10-03 13:15:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0c38e7da-5bd0-3ed3-9253-bdfebbd97cd0 | -7.2199 | -46.6751 | 2024-10-03 13:15:47 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 32fc2963-f1d1-3a1c-ad8f-13c6777803b2 | -7.6441 | -42.458 | 2024-10-03 13:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 94aab568-c254-3052-ad40-1224b0821d9d | -7.7213 | -45.4418 | 2024-10-03 13:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 16d7c9b9-d7f6-30cf-88f9-6601220baf6b | -7.7025 | -45.4436 | 2024-10-03 13:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 77f2f181-8443-30e2-9d4f-e9e884977fa5 | -7.8149 | -45.4782 | 2024-10-03 13:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a9434564-2b57-3c2d-a568-52a4435429c6 | -7.8626 | -43.0969 | 2024-10-03 13:15:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 5f260d4f-90ed-311d-932f-82be783ebf08 | -7.8629 | -43.0733 | 2024-10-03 13:15:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 9307778d-0a32-30bd-bddd-e5f65b9ea8ec | -7.7216 | -45.4191 | 2024-10-03 13:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f3e18253-d78f-3b4c-a308-eff743f62073 | -7.8245 | -61.3709 | 2024-10-03 13:15:51 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| aa0c18ae-cd5a-35f1-96ce-8bcb431807d6 | -8.157 | -43.6977 | 2024-10-03 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| f5f8ba8e-e3fe-351e-a428-49456e1b2849 | -8.1567 | -43.7211 | 2024-10-03 13:15:52 | GOES-16 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 2a958a61-e5d3-3603-b387-715ccc2fa38e | -8.1759 | -43.6957 | 2024-10-03 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8ed08151-d24a-307e-87b5-8ad90e985d5b | -8.1937 | -46.8324 | 2024-10-03 13:15:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4b2cc286-f487-3612-bb27-f042fc1f7ff7 | -8.1756 | -43.719 | 2024-10-03 13:15:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 2d99b810-5dbb-33c2-bdc9-159d17eaa567 | -8.3194 | -42.8343 | 2024-10-03 13:15:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 9d60ce30-9628-3831-975d-849bf9190481 | -8.7225 | -45.204 | 2024-10-03 13:15:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 257df195-7cbe-3932-9074-a58abe85fcd9 | -8.9244 | -45.6367 | 2024-10-03 13:15:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a7e47b97-96bf-37b0-9fba-5b4558612a1c | -8.8362 | -45.1688 | 2024-10-03 13:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 2c2f6646-c0a1-3bf3-a04b-7b161caeb1b4 | -8.8356 | -45.2145 | 2024-10-03 13:15:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1d9988c4-6d55-3110-b6bf-b4abea49ddbb | -8.8885 | -44.1045 | 2024-10-03 13:15:56 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b37062b2-1394-3c37-b0e3-3cc9d17e2f54 | -8.9074 | -44.1024 | 2024-10-03 13:15:56 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6f5f6e5a-8aeb-3ef4-bb4b-4c2a1294318e | -9.0227 | -49.8262 | 2024-10-03 13:15:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 6d335eb1-a245-3005-9a01-922f00e116c3 | -9.0415 | -49.8245 | 2024-10-03 13:15:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c92c38c9-3ad2-30a0-a1b9-f3455819a916 | -9.0229 | -49.8048 | 2024-10-03 13:15:57 | GOES-16 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 684cad6f-0a6a-3b70-a026-dc527bc2a2ff | -8.9791 | -67.4099 | 2024-10-03 13:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ad53d2ed-d550-3bdf-a9b8-fc4b35ae48bd | -9.0515 | -67.871 | 2024-10-03 13:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fbaec983-ec2b-3214-9e37-0b2592db5c49 | -9.0149 | -67.7423 | 2024-10-03 13:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1f4f0a95-ae64-3331-bbc7-3dccc556ec40 | -9.3833 | -68.3256 | 2024-10-03 13:16:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a6a091ab-a149-3440-a3bb-d68ef9a1e75c | -10.2381 | -47.7038 | 2024-10-03 13:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3fb1f0fd-9c4f-3593-899d-fb433fc95019 | -10.5926 | -48.0817 | 2024-10-03 13:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 25999979-c7a7-32f3-8489-407905327116 | -10.7161 | -46.1942 | 2024-10-03 13:16:06 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 2242f482-8bec-3037-852f-44ae181008c1 | -10.6981 | -46.1287 | 2024-10-03 13:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| bbbbf2c3-f254-345c-9313-25b467a88b6a | -10.7309 | -47.7126 | 2024-10-03 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| e2e66a35-76e8-3213-a06e-de81ab2a5ee6 | -10.7122 | -47.6927 | 2024-10-03 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7629c78a-ab7f-3d0e-bd94-b7f71b066e40 | -10.7312 | -47.6904 | 2024-10-03 13:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 7307e000-5011-39ce-bc2a-03d00f446305 | -10.7459 | -47.9757 | 2024-10-03 13:16:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a396fc03-9602-339d-bed9-d3c3ed14aae5 | -10.7352 | -46.1918 | 2024-10-03 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 9650c340-78db-393e-9ffa-c390a043cb2a | -11.0345 | -46.5143 | 2024-10-03 13:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| f1aa88e9-867a-33b0-9d7c-1cffe5882973 | -10.876 | -48.1584 | 2024-10-03 13:16:08 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| d49b70fc-e650-3675-8d1b-ab0c7fa38583 | -11.1575 | -45.9779 | 2024-10-03 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 2ca6ddbb-6b21-3ef1-8c40-8fdce55ded38 | -11.2783 | -43.388 | 2024-10-03 13:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 672e6d28-294b-3f4b-b988-de9170fd56fa | -11.2779 | -43.4118 | 2024-10-03 13:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 61393380-2c77-39a8-a998-e7c74ed625ad | -11.1579 | -45.9551 | 2024-10-03 13:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 321.1 |
| fab4b17c-07cb-349a-a153-ec2c32c8c511 | -11.2563 | -46.9348 | 2024-10-03 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a601b284-4f81-347f-a684-4a9e173cecac | -11.2758 | -46.9098 | 2024-10-03 13:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| b0e26472-f97f-31f5-a319-beddb8d352e4 | -11.9737 | -47.3986 | 2024-10-03 13:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 210.1 |
| a18326be-0d2d-38a6-bbaf-556dc83979e9 | -11.9671 | -50.181 | 2024-10-03 13:16:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| ac9f2eeb-9522-3958-b790-ebafc8338f56 | -12.217 | -45.5305 | 2024-10-03 13:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 9bd9ba56-3f8d-3d35-b3b9-c022a856eb27 | -12.7815 | -50.5758 | 2024-10-03 13:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 6890d399-f439-3e0c-ac5b-0b6720496218 | -12.7812 | -50.5973 | 2024-10-03 13:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 5b2a0f04-c393-3ec8-8182-a09bafbbf565 | -12.762 | -50.5997 | 2024-10-03 13:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 84f778b1-ecf0-37aa-a320-a47f25932937 | -13.0017 | -44.7357 | 2024-10-03 13:16:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 92b4b07c-6450-3f79-84d2-07d1ac7b7269 | -13.1976 | -48.6489 | 2024-10-03 13:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0f84b8dd-9f4a-3d7f-8d2b-cfd55dd2efa6 | -13.0022 | -51.1266 | 2024-10-03 13:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 5dafc1b9-6e11-3096-8a55-695f1067c811 | -13.198 | -48.6267 | 2024-10-03 13:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 378b5d1b-d712-3344-8676-8bc6da301461 | -13.1927 | -51.1883 | 2024-10-03 13:16:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 4b289695-941a-3d5f-b968-d89e612c56f9 | -13.1924 | -51.2097 | 2024-10-03 13:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 4291c338-b1ca-3006-9462-1172fd92024a | -14.0392 | -45.0947 | 2024-10-03 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 6e9e9d82-011d-372b-94c6-3bbfa7471b32 | -14.7017 | -48.7559 | 2024-10-03 13:16:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ea31e778-eaf0-36de-9238-abea96cf54a3 | -16.1286 | -53.5189 | 2024-10-03 13:16:37 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 241fc673-a353-37d1-a0e2-5e43f5487a64 | -18.8406 | -42.9235 | 2024-10-03 13:16:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.3 |
| d86e2ca7-43b8-307b-b750-bcf61ca09edc | -19.0344 | -43.1944 | 2024-10-03 13:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 169.5 |
| 99ab2363-0b2c-34fd-88d4-68cc8cd8786a | -19.0141 | -43.1998 | 2024-10-03 13:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.4 |
| 93605a44-4cec-3976-8226-b128102a3afd | -19.0932 | -48.2876 | 2024-10-03 13:16:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| f934a3cf-035d-3278-bd79-8faba7a6b99b | -19.2954 | -42.6032 | 2024-10-03 13:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 139.5 |
| 2f4a2b5d-b04b-342f-80c3-48b529786d2f | -19.2962 | -42.5779 | 2024-10-03 13:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 150.8 |
| febda6b2-9566-3b8f-8e10-339089b139c9 | -19.744 | -40.6685 | 2024-10-03 13:16:54 | GOES-16 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 111.6 |
| a74ef527-3f42-3c4f-a50c-bd05bb42f383 | -6.8887 | -44.2853 | 2024-10-03 13:25:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 298.2 |
| c61b521b-196a-313e-b415-80f9885e77b1 | -6.9075 | -44.2836 | 2024-10-03 13:25:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 2e170ab1-8c06-3b99-b551-0314ae5d0ab3 | -7.0367 | -42.8036 | 2024-10-03 13:25:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 91ec0702-f305-313a-9b6e-a000b793cc7d | -7.0175 | -42.829 | 2024-10-03 13:25:46 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| e97f82aa-4c3f-3e8c-9fb4-e3451d96c8bb | -7.2199 | -46.6751 | 2024-10-03 13:25:47 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 33019a53-5f22-3c30-a871-a4af886dea43 | -7.6444 | -42.4342 | 2024-10-03 13:25:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 2fec5612-6410-3473-b4bc-c1165aac6be9 | -7.6441 | -42.458 | 2024-10-03 13:25:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| abd2e1b0-b9c0-3458-9066-ffbe7310ef14 | -7.8629 | -43.0733 | 2024-10-03 13:25:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 8aefe6d6-a315-39fb-aa0c-2ab36506912e | -7.8149 | -45.4782 | 2024-10-03 13:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |


[Clique aqui para ver as próximas entradas](README213.md)
