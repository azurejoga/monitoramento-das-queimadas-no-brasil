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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f90abde-1f54-32b1-b276-0b67e24da2de | -6.9658 | -34.943901 | 2024-12-09 00:13:00 | METOP-B | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4c87a8c-896c-3350-a070-64491eb452f8 | -15.8419 | -45.1628 | 2024-12-09 00:13:00 | METOP-B | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fdf7f3c1-ec37-341b-9ca1-3d56a732b015 | -3.2323 | -42.428799 | 2024-12-09 00:13:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a5b172a-34f8-3dff-93b9-01020b86aa31 | -13.2774 | -51.055 | 2024-12-09 00:13:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3932900-47a7-3751-b82e-2bd2a358806e | -7.8084 | -46.210999 | 2024-12-09 00:13:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23abcbfd-7c47-3169-977a-a31ed14917a8 | -4.3937 | -46.134701 | 2024-12-09 00:13:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9863f19d-eabe-38c9-823f-6a9e6b6ab53e | -10.9221 | -48.907001 | 2024-12-09 00:13:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fbea36e-d53e-319d-8566-832065a36457 | -12.3729 | -45.931301 | 2024-12-09 00:13:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5722a991-755d-3ba9-b9e5-4e8a39a5d3ff | -11.752 | -54.7255 | 2024-12-09 00:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 122ba93a-1c9b-3019-978e-7a3fe847829e | -17.4765 | -40.1274 | 2024-12-09 00:20:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 171.1 |
| 28784cac-fb74-313b-8b56-eb83d7b236ce | -17.4773 | -40.1013 | 2024-12-09 00:20:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 146.5 |
| a19e0e95-cd10-393e-b147-44056332476e | -2.7823 | -53.2463 | 2024-12-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.8 |
| c0bc2e48-7b65-353c-aab8-9d4eac32aa96 | -2.8007 | -53.2459 | 2024-12-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 9b488e0f-8584-3ffc-bcdd-23b32503d563 | -4.0885 | -46.3715 | 2024-12-09 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5e61f77b-a80b-38ba-b23e-b87571ee9720 | -3.2351 | -42.4353 | 2024-12-09 00:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 768b90e1-605b-3cbd-aac9-2bd976006384 | -2.7823 | -53.2261 | 2024-12-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 22009c77-fd03-333f-a164-8e766b4b9ad8 | -2.7822 | -53.2666 | 2024-12-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 70b96bf2-8218-34bd-8142-5a8d4324598e | -2.8007 | -53.2256 | 2024-12-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c7263397-7c2f-3444-b2be-6e8aacdd2f41 | -9.5331 | -35.9238 | 2024-12-09 00:20:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.8 |
| 05d2aec8-c908-3d36-92a0-213b386930d0 | -2.57 | -45.3382 | 2024-12-09 00:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8fd6f1e3-ee2f-34ed-8f84-a34a731cddfc | -6.9633 | -34.9466 | 2024-12-09 00:30:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 8416debc-1070-38b0-a227-40c51539079b | -6.9825 | -34.9441 | 2024-12-09 00:30:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| f87e371a-00e9-34c8-8d49-df8ef625a7ec | -3.2351 | -42.4353 | 2024-12-09 00:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1912aeb7-af5e-35e1-9572-b2b6aa093406 | -6.9637 | -34.919 | 2024-12-09 00:30:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| 14cd8220-a2f9-34b1-afb6-051e890f4471 | -11.752 | -54.7255 | 2024-12-09 00:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 3a162227-4465-326c-910f-a14129817850 | -12.5495 | -57.7395 | 2024-12-09 00:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| fe6eb1ce-3ad8-3430-99c1-18ecade2cbe6 | -6.9828 | -34.9165 | 2024-12-09 00:30:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 07dff845-59dc-3244-948a-16966f0896b5 | -3.2351 | -42.4353 | 2024-12-09 00:40:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 03395c54-1074-39a3-ab3c-dc149a5fb969 | -6.9633 | -34.9466 | 2024-12-09 00:40:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 116.8 |
| 1c4a0e36-ea1d-38f5-9dff-f484ee8089c6 | -12.5495 | -57.7395 | 2024-12-09 00:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b51172be-a1ac-3329-b04d-1de2faeb5bff | -11.752 | -54.7255 | 2024-12-09 00:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| e4fa3264-7e1c-32b5-a771-0f34633cfb59 | -6.9825 | -34.9441 | 2024-12-09 00:40:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| f4e52760-da70-394a-98f0-de728deac1c6 | -6.9637 | -34.919 | 2024-12-09 00:40:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 116.2 |
| aa6436eb-6bb0-3245-9698-0c210086ddd7 | -6.9828 | -34.9165 | 2024-12-09 00:40:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 133.8 |
| 14b3860d-a07b-30df-9da0-44092a278c9c | -3.2351 | -42.4353 | 2024-12-09 00:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 7929c6a0-97b2-3471-8f43-843a48eb18ba | -2.7823 | -53.2463 | 2024-12-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 128b2d6c-7228-39c8-bab1-0949b720b090 | -13.2713 | -51.0715 | 2024-12-09 00:50:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| affd1233-8d6c-36b1-bfae-581a699ae00c | -11.752 | -54.7255 | 2024-12-09 00:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| c23e243f-a7c4-3614-a6e6-e8ceec8d9ade | -11.771 | -54.7237 | 2024-12-09 00:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| aa651716-a92d-3561-b0a5-e8f5e31dcfbd | -21.33765 | -44.74611 | 2024-12-09 00:52:00 | TERRA_M-M | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 7a35c7e3-ccdd-3a5f-9238-9735e03ebd83 | -19.2986 | -45.54768 | 2024-12-09 00:52:00 | TERRA_M-M | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 65e4782f-8f87-3a27-8d6f-ce05a3a0929b | -21.3362 | -44.73626 | 2024-12-09 00:52:00 | TERRA_M-M | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c1eccb9b-c605-316f-818e-68e8df560b98 | -13.26095 | -51.07519 | 2024-12-09 00:54:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1738ae2b-4181-3208-afb9-89ca47fd655f | -11.75128 | -54.72653 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| f5d3f531-0ecb-3a15-83e2-2b062138ec0a | -12.28696 | -45.50164 | 2024-12-09 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 2a0531e3-b4d2-383b-ba8e-2335c35b2609 | -12.40737 | -49.67907 | 2024-12-09 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ca9c8932-393c-3f20-a9b6-08f71f654136 | -10.4326 | -51.82829 | 2024-12-09 00:54:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8866b42f-2863-3a7a-814c-c9080a315685 | -10.91866 | -48.93655 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 01d04e6c-52ec-3a61-8efd-232f7ee72c8a | -11.7499 | -54.72006 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7b88c8b1-4100-38f5-bbb4-64511a825aa9 | -16.21042 | -48.21684 | 2024-12-09 00:54:00 | TERRA_M-M | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53ed1812-0d10-37d0-ba3a-332511523599 | -11.75229 | -54.74064 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 86d07b9e-220a-3af3-b376-dfd9f0198fc0 | -10.92633 | -48.92622 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f46dfec-a867-3428-84d4-86387f1988de | -11.76285 | -54.71861 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 2571ba16-1bc4-3c10-8b5b-97d93349d498 | -11.76524 | -54.73907 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 755a7ba9-bcf3-3dd7-9265-b296092b272c | -10.45297 | -44.88532 | 2024-12-09 00:54:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a2d133c9-e48b-32e5-aaf7-674f2f8627f7 | -13.26244 | -51.08685 | 2024-12-09 00:54:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| baad9f87-439a-3d9f-8cc4-8e0b9e5f006a | -12.53499 | -57.74521 | 2024-12-09 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 69e1767d-5389-37d6-8844-5a1d4955a769 | -12.28536 | -45.49098 | 2024-12-09 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d5684ea-9811-399a-896f-8380ccdac00a | -13.27395 | -51.09719 | 2024-12-09 00:54:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3af5fb35-3975-3dbd-9a1e-895c530967ed | -10.44461 | -44.89915 | 2024-12-09 00:54:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 79262901-6faf-33e3-8947-c1573470458c | -12.54586 | -57.749 | 2024-12-09 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6b67cc54-2e62-3b05-bd63-f0c2fdaa6dba | -10.91742 | -48.9275 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 43755a95-3463-35fb-a9bd-b8d85b98f89d | -12.53322 | -57.78653 | 2024-12-09 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 1a1bfaf9-99c0-3cdf-b06c-077e342bf2ec | -10.44275 | -44.88698 | 2024-12-09 00:54:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c2a36ba3-e421-389a-b50f-7d3fd91b6a4c | -10.92757 | -48.93527 | 2024-12-09 00:54:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 890f26f2-90cb-38e6-a816-97bece8b55a5 | -13.26393 | -51.09854 | 2024-12-09 00:54:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cda46902-994b-3fc1-83a1-7bca1ee7a5da | -13.27095 | -51.07384 | 2024-12-09 00:54:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 9e9ce9be-e03f-3b94-ac2a-704db7e54b23 | -14.97956 | -44.41208 | 2024-12-09 00:54:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 966da6c5-44d0-3459-80f0-2cfca7d9255a | -10.41999 | -51.88992 | 2024-12-09 00:54:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 576f7862-ffaa-325d-803e-345f32b82804 | -12.53872 | -57.78134 | 2024-12-09 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3707c32a-4069-3d5d-a220-1503cefbdd9e | -12.90702 | -55.05041 | 2024-12-09 00:54:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 472332a6-7262-3dfd-b11f-2926d6e1d389 | -12.52209 | -57.78283 | 2024-12-09 00:54:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| b05d5f0a-ba40-36bb-8190-a93cbecb8dda | -10.45483 | -44.89757 | 2024-12-09 00:54:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d6cf0fef-65f6-3472-8005-61e4650cb605 | -12.68376 | -46.75729 | 2024-12-09 00:54:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aaf084ef-0a20-336c-a513-50c13220a63e | -15.84231 | -45.17056 | 2024-12-09 00:54:00 | TERRA_M-M | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5e852557-34aa-3064-bdfc-ae68629db969 | -12.68511 | -46.7667 | 2024-12-09 00:54:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a7644e6-1d96-3f1b-9af7-505d831f4628 | -12.27739 | -45.50321 | 2024-12-09 00:54:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 791654c4-b73d-3d5c-a4cc-96b4c4b410e3 | -6.44418 | -47.06017 | 2024-12-09 00:56:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bbaf30c1-f69a-32e6-933d-c6547e59fb12 | -8.15759 | -49.1464 | 2024-12-09 00:56:00 | TERRA_M-M | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 628216b7-e372-3656-91be-5b5aea050175 | -4.54614 | -48.02346 | 2024-12-09 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 3b32ace0-b9fd-3518-a40c-378164836a03 | -7.18156 | -45.44389 | 2024-12-09 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 74bceaf1-738e-31a7-b240-4081142acfeb | -6.45733 | -47.85896 | 2024-12-09 00:56:00 | TERRA_M-M | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 27e003fe-61ec-3581-8290-9a4e70a62fdf | -8.78521 | -48.75292 | 2024-12-09 00:56:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24f7a464-ffb2-3c1a-8557-e6d4be1cc117 | -4.08311 | -46.72253 | 2024-12-09 00:56:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f14e5184-b664-3c1b-a56d-904c904268bd | -8.09582 | -46.03873 | 2024-12-09 00:56:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3e4fb6b5-0e9a-3408-95c2-05d15a784393 | -3.46541 | -53.96389 | 2024-12-09 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 24c3785b-92f6-3f18-b484-b0088e3c48c9 | -4.54479 | -48.01392 | 2024-12-09 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 002fe98e-5f60-3479-861a-7a66feddd4c1 | -3.42575 | -42.99125 | 2024-12-09 00:56:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f21b69da-eda3-304f-8390-2713a6131fe4 | -2.87458 | -54.26293 | 2024-12-09 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f94b0925-d7aa-3bcf-aec4-8062d0a22643 | -4.52477 | -47.02456 | 2024-12-09 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| df8b5fd7-7b46-3594-bc99-29277a744eda | -4.08696 | -54.39704 | 2024-12-09 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 3e804583-cb1a-3e7f-9c46-9102c000fe71 | -2.57158 | -45.34421 | 2024-12-09 00:56:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 2f912f78-1a97-3a9b-847c-640dc1c7e7d4 | -2.44366 | -48.91921 | 2024-12-09 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 446a0599-1e6a-358e-8e89-5687ba143818 | -4.68 | -44.44537 | 2024-12-09 00:56:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 77c024d6-4714-37f9-9856-005e72b54224 | -4.08148 | -46.71131 | 2024-12-09 00:56:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f7f4eedb-b6f9-33da-8919-ef2ad7db27b9 | -2.50292 | -49.01357 | 2024-12-09 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cd032f56-08ee-32ca-92ef-7f68bc5ade36 | -8.08603 | -46.04033 | 2024-12-09 00:56:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f8e278fc-0f50-37a6-bb41-1cf59ea47138 | -4.52327 | -47.01402 | 2024-12-09 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| be856955-cc5b-3908-b876-a346df672304 | -7.99027 | -45.80145 | 2024-12-09 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6c9ae368-4bb0-3ad5-9ae3-a2dab7a12689 | -8.01025 | -45.79862 | 2024-12-09 00:56:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |


[Clique aqui para ver as próximas entradas](README3.md)
