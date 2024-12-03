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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd3327f0-3d52-3ce1-9d6f-ad0699b71f32 | -5.1181 | -43.1964 | 2024-12-03 04:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 931ed9b9-541a-33da-9b14-4da8727d83f6 | 2.7267 | -60.3916 | 2024-12-03 04:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b5b2cef5-ffed-31b4-924e-a1b2d7d0ea57 | -1.0736 | -53.436 | 2024-12-03 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| cc883665-ceec-33f1-bd45-3e9d259725ed | -3.076 | -53.3808 | 2024-12-03 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e011715c-2fe3-3ca8-979d-4bce26be62b7 | -5.8197 | -46.4706 | 2024-12-03 04:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| a221e809-edd9-32d5-8158-d396a42aaf4f | -5.118 | -43.2198 | 2024-12-03 04:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 1adc8448-668a-3932-9da1-591bc44e41a4 | -3.3141 | -53.6575 | 2024-12-03 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 42e02f08-cf11-3af7-8ca8-3aa8d4155a3c | -3.347 | -46.0486 | 2024-12-03 04:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 8caf09c0-d691-32d9-b3d3-dc04721feb56 | -3.259 | -53.659 | 2024-12-03 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 25556f58-2107-357d-bb64-c03443e309c3 | -4.1914 | -51.1914 | 2024-12-03 04:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e0ff667f-5bd5-3d60-a4ea-e8efedbd7f6f | -1.0735 | -53.4562 | 2024-12-03 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 934668eb-0af0-388e-9485-d0c406e73d6f | -5.8195 | -46.4929 | 2024-12-03 04:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e7e13530-15cd-325c-82a5-05c90220f2cc | -3.2591 | -53.6186 | 2024-12-03 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fb462c76-714e-3b41-a570-83369f7a2b7e | -3.2957 | -53.6782 | 2024-12-03 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 19ca00e4-5c41-3873-a3cb-cd7c293a56c3 | -5.801 | -46.4719 | 2024-12-03 04:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 6c7f02f1-a95f-3ae2-b0fd-e0e67fd2f778 | -3.259 | -53.6388 | 2024-12-03 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5bac20a5-7690-3fda-92a4-ab64d051201d | -1.0919 | -53.4561 | 2024-12-03 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 1d9fb072-4d2c-31a3-9a9d-7e74f0007ee5 | -5.8009 | -46.4941 | 2024-12-03 04:40:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| a90b72d9-eaae-389f-8152-a0f80680293d | -2.8196 | -53.0629 | 2024-12-03 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3851987f-e493-3d6c-8aca-185c4abac811 | -2.8197 | -53.0425 | 2024-12-03 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 278075f9-c67b-36ec-b150-6d529dcad2d6 | -5.8009 | -46.4941 | 2024-12-03 04:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 7f1c2373-4953-3988-b335-c9b9a8b089cd | -3.347 | -46.0486 | 2024-12-03 04:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 40f58f60-fca1-3bc8-a9ec-186006dcf971 | -5.1181 | -43.1964 | 2024-12-03 04:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| f4bbae71-6520-3fb5-ab08-fe00c63505f8 | -3.2958 | -53.658 | 2024-12-03 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ae5898b3-12d3-36eb-82be-f9350da36518 | -5.8197 | -46.4706 | 2024-12-03 04:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 66e9fe1a-f249-334d-bfe9-f97ec06176e7 | -5.801 | -46.4719 | 2024-12-03 04:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 142842f3-53bc-3e4f-a1df-ed5706ca18dd | -1.0735 | -53.4562 | 2024-12-03 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| de0979a7-b9bb-3441-9c82-954796b830e1 | -3.259 | -53.659 | 2024-12-03 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ae9d6daa-7e63-3a21-badd-69a3ef665ff3 | -6.9723 | -43.5133 | 2024-12-03 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 2d1df1d3-362d-3638-855d-6264134182b5 | -5.8195 | -46.4929 | 2024-12-03 04:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 2612817a-8680-3329-b1c3-f9c7eab68ebb | -3.259 | -53.6388 | 2024-12-03 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 76d5e9a7-7746-3c63-849e-774ecc9b197e | -3.0944 | -53.3804 | 2024-12-03 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 86a826a5-6044-389e-9006-05bdb2c387e9 | 2.7267 | -60.3916 | 2024-12-03 04:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a7ae922d-5a80-3bc5-a0d9-bec5313732d3 | -3.076 | -53.3808 | 2024-12-03 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ffc2c3e0-3b29-3bcb-a693-94371932ff1e | -6.9911 | -43.5116 | 2024-12-03 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 52c6d168-2643-3458-8c29-f965e9e0c2f7 | -3.2957 | -53.6782 | 2024-12-03 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 60e1fd38-14cb-3c38-a7d5-f0d9f21a7ddc | -1.0919 | -53.4561 | 2024-12-03 04:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 469b0847-7135-398b-a2da-7be7f673c716 | -5.118 | -43.2198 | 2024-12-03 04:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| dd74c5f2-4797-3c20-9e20-73757d02decf | -3.2591 | -53.6186 | 2024-12-03 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a51f499f-de7a-37c0-a288-0321e2fa5f14 | -3.076 | -53.3808 | 2024-12-03 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0193825b-1819-3847-ae05-9d4b9ed76aa2 | -5.8195 | -46.4929 | 2024-12-03 05:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bd47d015-80e2-3a85-8fa9-00433ce4d473 | -5.7824 | -46.4732 | 2024-12-03 05:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ce2becfd-0738-3c98-b153-5bdd9d1a30a3 | -3.0944 | -53.3804 | 2024-12-03 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e3a99da0-3159-36cc-aa8d-54151a858e61 | -1.0735 | -53.4562 | 2024-12-03 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8fafd1f5-5478-386f-a706-f0e6cbdde07a | -5.118 | -43.2198 | 2024-12-03 05:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 957e8198-c27c-38fe-a346-647b288e231b | 2.7267 | -60.3916 | 2024-12-03 05:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 7c40e65d-4316-353b-9b54-458f65c42431 | -6.9911 | -43.5116 | 2024-12-03 05:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 87579447-9c46-399d-a394-f199b8293b14 | -6.9723 | -43.5133 | 2024-12-03 05:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5658264e-2983-3525-a9da-0f981e342cd5 | -1.0919 | -53.4561 | 2024-12-03 05:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 11f75951-02ba-313d-96d7-beebde91d0d8 | -5.1181 | -43.1964 | 2024-12-03 05:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2286af5a-34c6-39d3-a2d6-8ae34b3008f9 | -5.8197 | -46.4706 | 2024-12-03 05:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| e0d114e9-5fe0-3fee-b318-000f555b3bda | -5.801 | -46.4719 | 2024-12-03 05:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 213c5e06-4aa1-3fdc-aa8c-d633deb54395 | -5.8009 | -46.4941 | 2024-12-03 05:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| dc93ce0b-dc57-3a10-9980-ae5dd7ee0480 | -6.1229 | -43.9578 | 2024-12-03 05:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0cd2382c-3d24-364c-8bc0-47d939fd01b9 | -3.347 | -46.0486 | 2024-12-03 05:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4fed6b75-e2c0-3798-a321-b29891c91bd8 | -1.7972 | -46.6449 | 2024-12-03 05:05:00 | AQUA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 36406eb3-39ae-3eb8-8cc8-d44e32835fdf | -3.34132 | -46.0518 | 2024-12-03 05:05:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 063ac042-9ef6-32fc-8994-675352ae54b6 | -4.21205 | -44.36546 | 2024-12-03 05:05:00 | AQUA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c3d5a8a5-2fea-36af-b3a8-12eacf7077e9 | -3.32985 | -46.04955 | 2024-12-03 05:05:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 50d8ff85-0307-339e-831b-dc00bb1c958f | -3.3414 | -46.04193 | 2024-12-03 05:05:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b5a0c51f-4cf6-3e01-9a82-9702e85e2ce5 | -2.20539 | -45.73487 | 2024-12-03 05:05:00 | AQUA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6c55c4ff-7c51-3be3-8c25-4650f6030c40 | -2.84359 | -45.39124 | 2024-12-03 05:05:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f182e0c0-0a72-3cbb-87d7-08af927b851d | -4.21029 | -44.37693 | 2024-12-03 05:05:00 | AQUA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 86aa4f4a-f850-30e1-9ed4-3ab45f09d253 | -3.34364 | -46.0365 | 2024-12-03 05:05:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 238f18ab-7884-3795-951a-0cbffeeb2c4c | -3.34386 | -46.0265 | 2024-12-03 05:05:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f3b13696-acf6-340b-b588-5cdac6b8fa16 | -2.72175 | -45.20297 | 2024-12-03 05:05:00 | AQUA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9e2bd4a3-722d-3500-aa9a-821a665f019e | -2.20403 | -45.72585 | 2024-12-03 05:05:00 | AQUA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 65f58819-3b2b-3668-9338-112c0ba216b3 | -2.95638 | -39.96079 | 2024-12-03 05:05:00 | AQUA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8dc32a76-59a1-3e95-abc7-d668622a4662 | -2.84578 | -45.37703 | 2024-12-03 05:05:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 28ef00f8-c120-33e0-8772-0a34b7edf6c4 | -3.33899 | -46.05704 | 2024-12-03 05:05:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 022ccfd1-b7a9-3d72-b71c-b39381d1b6d5 | -3.46426 | -41.99936 | 2024-12-03 05:05:00 | AQUA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| c2691288-4800-3096-a201-8727cfa39182 | -3.33213 | -46.03462 | 2024-12-03 05:05:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9465204f-be80-3b3c-b648-b2e9cb7b286c | -2.67956 | -46.61267 | 2024-12-03 05:05:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e32a58dc-7718-3658-bc1a-742dc2056f89 | -4.20205 | -44.36394 | 2024-12-03 05:05:00 | AQUA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fa6b4ab3-6ce5-39ec-bc1b-dcc3f487c84c | -6.11168 | -43.95568 | 2024-12-03 05:08:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 659d2de7-281b-3b16-9304-b29088aedb4d | -6.12117 | -43.95722 | 2024-12-03 05:08:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| d65083ba-9356-3083-8e11-fda599fb3d79 | -4.56213 | -46.62767 | 2024-12-03 05:08:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 252c718a-a8f3-31ae-82a0-5558edb85088 | -5.45473 | -44.82011 | 2024-12-03 05:08:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a448c99d-06b4-3c1e-b114-4334c1148402 | -6.17829 | -42.6158 | 2024-12-03 05:08:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 414bedb3-e8b6-302b-9fc2-135e31a2880a | -4.92932 | -43.77068 | 2024-12-03 05:08:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2db10e29-39c7-386d-b2af-897ca4ed3854 | -6.98081 | -43.52313 | 2024-12-03 05:08:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3f610217-156a-3c6c-b01d-d7c7b9b25427 | -6.99001 | -43.52455 | 2024-12-03 05:08:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6682a64c-e42b-311c-a94e-b7bde4cded62 | -5.10892 | -43.20879 | 2024-12-03 05:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c6219755-7933-35fb-a278-5b3bcb6d54ab | -10.65637 | -44.49492 | 2024-12-03 05:08:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae8eecbe-5a1d-30dd-ab2d-20b7c2a8db91 | -5.10743 | -43.21851 | 2024-12-03 05:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 990afdb0-f1ec-37d4-b2f1-56b0518c59e1 | -4.1698 | -48.17925 | 2024-12-03 05:08:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1dfad43d-9188-3ab5-8f3c-8f22f7d24ac3 | -5.11042 | -43.19907 | 2024-12-03 05:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 15939c1e-76ed-3420-8a0e-e4a4b8345c13 | -5.56657 | -44.88588 | 2024-12-03 05:08:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2c6a60a6-d78d-3e75-a5fa-3fbc97ed6253 | -6.18707 | -43.40549 | 2024-12-03 05:08:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 99183639-060f-346b-a8c2-2eb5f0be2d24 | -6.03657 | -42.51445 | 2024-12-03 05:08:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cfeab7ec-053a-321a-8f7b-30b4ef0617f9 | -7.56546 | -45.73069 | 2024-12-03 05:08:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a09e0940-5c16-3f28-bbf6-31419b43acba | -5.11966 | -43.20044 | 2024-12-03 05:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 6e45d168-e3ba-3fd7-8c79-40afd1a3bfba | -5.80906 | -46.46582 | 2024-12-03 05:08:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| fe55ffda-8524-302f-a736-8066e9ccbaa2 | -6.11959 | -43.96745 | 2024-12-03 05:08:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6c3d4b41-2ed3-330f-ae08-df4502f2c3c9 | -6.98231 | -43.51351 | 2024-12-03 05:08:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f2dd9837-fbd3-3d23-a5a9-381577b7c316 | -4.16634 | -48.2011 | 2024-12-03 05:08:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 62dea618-58ef-3fac-a8de-27bcfa2dd997 | -10.64711 | -44.49346 | 2024-12-03 05:08:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9cc9fa13-a63a-38e3-a892-dc81d761b2b5 | -5.14443 | -43.22405 | 2024-12-03 05:08:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 981e166f-6ff6-396e-b4f1-d60c4990fa88 | -5.79765 | -46.46405 | 2024-12-03 05:08:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 81e1c3ce-3c68-3995-8dc1-b280ee4c3d92 | -4.93885 | -43.77218 | 2024-12-03 05:08:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |


[Clique aqui para ver as próximas entradas](README55.md)
