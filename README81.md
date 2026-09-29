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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d119066b-1af6-38c6-ae31-ccc218ad6d60 | -11.8678 | -50.4504 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 47a3da73-dd99-380c-93de-5cb6145c73e5 | -11.0101 | -50.6958 | 2026-09-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ba01c1db-af94-3cb5-be5a-9b85f8e11ade | -6.6709 | -45.3988 | 2026-09-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 29f10d6e-f598-340c-a04f-30972327340d | -11.8672 | -50.4933 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a2eeeee9-659d-33f6-94c8-b44cb662b150 | -12.0369 | -50.6019 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 23cb8c74-8675-3fe8-8153-0d0794b5635a | -11.1327 | -50.0624 | 2026-09-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d6d29784-ea76-3122-9e06-740e3f16d59d | -11.9842 | -50.3079 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| bd30f826-961b-39f8-8a4f-cfd86285cd50 | -12.6078 | -47.2653 | 2026-09-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 281.3 |
| cf2184eb-3f79-3e11-939b-82ac33e571bb | -6.7254 | -45.5749 | 2026-09-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| dd5029e1-aa19-3005-9280-8146594b98c8 | -8.3614 | -45.424 | 2026-09-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 241fb6af-2ae3-36a5-9abb-dd7fea6cf745 | -12.2911 | -50.1849 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| a280e001-6844-387e-ae71-ba032c895528 | 1.8403 | -55.6442 | 2026-09-29 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 5763aae9-3ea8-336a-a55e-5520a5e23c36 | -11.9936 | -50.9486 | 2026-09-29 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b5b45dd8-a861-3042-9ded-a4a6f0ffb114 | -8.0358 | -42.8423 | 2026-09-29 14:30:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 16057654-23a2-3690-9921-cf6f44050028 | -11.1962 | -44.8037 | 2026-09-29 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1fa7116b-6611-389f-bb08-bb619462595a | -4.2981 | -48.6094 | 2026-09-29 14:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| fb3c2ae4-1df9-32b8-8207-8a27e9f81561 | -14.5362 | -48.2927 | 2026-09-29 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 72686f89-2639-30b4-a7e9-614694fbb23e | -10.9156 | -50.6845 | 2026-09-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 5d814aae-8b81-37b0-b983-f815aa5e8ba9 | 1.4453 | -50.7863 | 2026-09-29 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a2a859cc-8338-367b-9a57-8c7e66ecd43c | -6.5593 | -45.3173 | 2026-09-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 37b15d44-cc9d-3c36-a748-8ede03964f85 | -10.7913 | -48.7596 | 2026-09-29 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2e455c9d-7ccf-35ec-87ee-5b1478381598 | -7.4156 | -42.6241 | 2026-09-29 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| bfa2ea8f-e433-332d-b341-4283bac0d912 | -15.3998 | -47.9261 | 2026-09-29 14:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c67e7267-3254-32db-a303-cbac7fff886d | -12.4355 | -44.1262 | 2026-09-29 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 712cced0-c847-3d4c-8d39-54b827b35efe | -10.2843 | -44.6274 | 2026-09-29 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 169.0 |
| ee9cf33b-c2d6-3148-9704-46bc3fb89376 | -12.1925 | -50.3904 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| b5fa02f7-c4ee-39ed-9ff7-f6e0e49284b2 | -12.0175 | -50.6256 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d07a8081-3c9c-3a5f-a28e-c53766de571f | -12.2901 | -50.2496 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 12e05801-bd74-331e-96c1-880634505266 | -10.7916 | -48.7377 | 2026-09-29 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| d4bff389-829f-314b-b908-9faa1cf196e5 | -9.8064 | -44.8265 | 2026-09-29 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e63ab0ec-3f86-3f8c-9832-0eb2d40a0c63 | -10.2656 | -44.6067 | 2026-09-29 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9f0e5432-1939-36d1-be14-a69846f68488 | -10.8967 | -50.6866 | 2026-09-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 939ca044-e80b-3d37-95af-29c3d7e1a5ac | -12.6271 | -47.2626 | 2026-09-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 423.7 |
| 3de4de93-a7aa-3178-a44d-a1fb1530517d | -8.9823 | -44.1633 | 2026-09-29 14:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 7fd87015-ae17-36a3-a6b2-b4960f78fddf | -12.8847 | -44.8015 | 2026-09-29 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 226.8 |
| a3560a22-c487-313f-9660-0aac00c0f160 | -12.1731 | -50.4142 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 195d23a4-660c-3411-a0c4-2b79eb80fd33 | -11.64 | -43.5218 | 2026-09-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 80233eb4-fdf4-314e-b450-dce4e030c0e6 | -11.5727 | -47.4074 | 2026-09-29 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f4f26ee9-0e68-337b-b0f4-aa7d63f7adeb | -12.0642 | -50.0617 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 7924d4b9-0566-344c-b959-cfd5f840e9ee | -12.7801 | -50.6619 | 2026-09-29 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 6f0a52c4-a434-384a-95eb-f29ada3ad848 | -11.0983 | -46.0992 | 2026-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 796ad468-9ee4-378f-891d-8a36de34cce3 | -14.3693 | -52.1026 | 2026-09-29 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 5e6228ce-05d5-39da-b40a-7bd08352a1d2 | -11.9428 | -50.5273 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 2fa36419-7964-3fc2-b0db-ecfe1f6c4cd3 | -8.2102 | -45.4621 | 2026-09-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 98cbaca6-8259-300b-aba6-f13f61cdc8c5 | -7.2718 | -45.3246 | 2026-09-29 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 0c197364-b8cc-3f27-9eca-3bd6b5e0b6a7 | -13.6762 | -45.7822 | 2026-09-29 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 321.1 |
| d1c02068-0326-31b0-9468-dbb177cc9d63 | -11.6797 | -44.5012 | 2026-09-29 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| bd1cc9d6-0ae2-37a3-911e-b7db1d802ab0 | -11.3927 | -43.418 | 2026-09-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 88a40558-b8a9-3800-a17e-a8e354a2e439 | -12.2254 | -50.7294 | 2026-09-29 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 5f6ab6f4-9aad-30aa-b5f7-9a6d7dfd612b | -9.1337 | -49.9656 | 2026-09-29 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| fc381daf-1ccd-385b-885a-1c72235fd568 | -14.1309 | -46.2801 | 2026-09-29 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 156.8 |
| c4408e0a-141a-3750-90d4-058869e6ff26 | -11.9609 | -50.5894 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| c67d392b-233c-37f4-979c-d885b09e4794 | -12.4351 | -44.1497 | 2026-09-29 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| cd9259f5-fcca-3997-8041-fb76e822f512 | -8.3611 | -45.4468 | 2026-09-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e0525900-f4df-3bbf-84e6-0b5b3a57f0c6 | -10.8964 | -50.7079 | 2026-09-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1b76ef83-eb32-38c7-b402-da335e79b976 | -20.9159 | -57.8246 | 2026-09-29 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 154.1 |
| 42f95758-5515-39cd-b8d8-b145bd57f980 | -20.6905 | -57.9607 | 2026-09-29 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.5 |
| c480c68d-ea20-3d5f-bb03-3f3f834d4a46 | -12.2633 | -50.7463 | 2026-09-29 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e7f4779e-6807-3d45-bdfd-c6fdf6fabb02 | -15.7547 | -46.0347 | 2026-09-29 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 178.2 |
| a0e10410-3004-3137-8fcb-6761e3f8f577 | -10.7064 | -44.4317 | 2026-09-29 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4242ae96-c81b-39c1-a7af-a904712ddad8 | -12.6267 | -47.2851 | 2026-09-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| b6cd4b89-531a-3cda-8fce-090f9a51f5df | -11.6596 | -43.4951 | 2026-09-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| db7ac2fd-2914-308d-97c8-6a81d6002bba | -11.6784 | -43.5158 | 2026-09-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 774c16d2-0460-35a6-a46a-b2d2f1862110 | -6.1598 | -52.9134 | 2026-09-29 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 73bec1d4-1399-30ff-8569-e40d8cd1e56e | -12.6463 | -47.2598 | 2026-09-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 91738ca4-3bae-356b-91f2-a822208c7d25 | -12.6074 | -47.2878 | 2026-09-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| af56e5a9-6949-3e45-8575-ae22b3e8a42a | -8.7264 | -44.9066 | 2026-09-29 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 55ee5bbc-c9d1-3d65-b8f0-604c474be6b2 | -5.641 | -45.5214 | 2026-09-29 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d2afb46b-0845-31d6-bbf4-748a9062cb19 | -7.064 | -42.0648 | 2026-09-29 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| 1bf1ee51-3da2-3963-aec9-e3c45482b3f8 | -10.9912 | -50.6978 | 2026-09-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 0509de70-f17d-3d4a-b7e6-8aadfb5b82a7 | -11.8862 | -50.4911 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 53e19af8-e1b7-3a05-8fed-f7b6fa75a224 | -10.9154 | -50.7059 | 2026-09-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5a7fa208-f6fc-3ee3-af3e-c51eb949b386 | -12.2723 | -50.1657 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 94f9190e-abf1-3863-ac8a-9d79468fd435 | -11.6989 | -44.4984 | 2026-09-29 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| c7ded9fc-4d7f-35b1-98b1-c494972f654b | -10.7255 | -44.4291 | 2026-09-29 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 25edcdd8-c458-347c-974c-58eb7831ea9e | -11.6592 | -43.5188 | 2026-09-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| f10987de-6f5b-3e51-90cf-cc92612165b0 | -12.2897 | -50.2712 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b3a6955a-28f7-39bb-861f-a2928a8b9872 | -14.0915 | -46.3096 | 2026-09-29 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 2bb8aeda-1bdf-3caf-bea0-6322eab7a51f | -10.9343 | -50.7039 | 2026-09-29 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 96dac1a1-d233-3823-977e-e5afe14ecf0f | -20.8373 | -57.6891 | 2026-09-29 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 129.1 |
| b0978e92-0101-31d4-83bc-5a84e42d8c91 | -12.1734 | -50.3927 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3dddd736-49cf-3450-ada9-9ab1d80e1675 | -10.2257 | -49.9879 | 2026-09-29 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 513c2bed-c0c2-3889-9cc7-051ffd0193f8 | -10.207 | -49.9684 | 2026-09-29 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 33a2da11-efcd-3791-ba7d-d820327882b0 | -11.3743 | -43.3734 | 2026-09-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 75c4db26-18cd-36b0-9660-dd46fd925319 | -6.7251 | -45.5975 | 2026-09-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2cd60ee8-2310-3432-81d8-4687c9b782e4 | -12.0559 | -50.5996 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a87270f1-92ad-361c-b7bf-78ef19f35f2c | -8.6451 | -45.3489 | 2026-09-29 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| b058db7a-ab45-3654-a471-568b8ac92203 | -11.1324 | -50.0839 | 2026-09-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1bb30d37-cad5-33b5-ba39-69dee584a07b | -15.735 | -46.0384 | 2026-09-29 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 194.6 |
| c2a32847-ccba-3b5d-9a1c-3986d36dff79 | -11.9138 | -49.9289 | 2026-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 15407f56-59f0-36dd-b184-8f516aa74e2f | 3.6391 | -60.8313 | 2026-09-29 14:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 84b2a4ec-0f53-336a-883d-8c85f7121214 | -11.6404 | -43.4981 | 2026-09-29 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| d7eef903-62d0-38d0-bd4e-9280fd1517a8 | 1.8403 | -55.6244 | 2026-09-29 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 4ece4271-705e-3e3b-8e96-8d43685a8975 | -9.4328 | -50.1086 | 2026-09-29 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 4762ae67-2cbf-3ab2-ace6-2ec105602ac1 | -10.3895 | -61.231 | 2026-09-29 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b71e2966-6c13-33f8-8046-8f8d9b454e99 | 1.822 | -55.6247 | 2026-09-29 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| b0389cc6-c0e2-36cd-a559-2a4a5fa599db | -9.2048 | -45.8548 | 2026-09-29 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9121809f-b686-3c2a-a7bd-b68e9f6d0fa2 | -10.2067 | -49.9898 | 2026-09-29 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| f943e80e-7cb7-33b8-af37-35bb512e3730 | -10.3894 | -61.2502 | 2026-09-29 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 870d92df-5093-3843-8005-edcf65ef17af | -20.9155 | -57.8456 | 2026-09-29 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 155.2 |


[Clique aqui para ver as próximas entradas](README82.md)
