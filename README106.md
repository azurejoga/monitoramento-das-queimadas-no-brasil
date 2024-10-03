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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a25cddf-8597-385f-9b1b-0614b24dd200 | -16.10011 | -50.40204 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d919cd3-0968-3960-af10-29e4e3695998 | -16.09843 | -50.37027 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc9a44e4-0a06-31f5-8cd4-ce1333192c87 | -16.09792 | -50.43622 | 2024-10-03 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b32240bf-51ce-338c-8d9c-29c430dd0674 | -16.09779 | -50.37413 | 2024-10-03 04:29:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aabb7f7f-985a-3172-b004-8115e0646797 | -16.09737 | -50.39754 | 2024-10-03 04:29:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31d17fd3-d4b2-3918-97c0-e9879f138278 | -17.83966 | -50.81222 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f4e7e876-000b-3f89-b6f5-724324e0a01e | -17.57831 | -51.56844 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccdf73d5-31e8-3e0a-acb9-19a394871792 | -17.23585 | -50.72207 | 2024-10-03 04:29:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fdef5c4-875f-33ed-992a-ad029437874a | -18.25994 | -50.82398 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cfc8b56-c1e7-36e8-a8a8-45ead16d61d3 | -18.25719 | -50.81955 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8a7f68b-b7de-3c7f-991d-4787f96576e7 | -18.25656 | -50.82333 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd54c6b2-909b-3ef3-8ec3-894f13b70098 | -18.25594 | -50.82705 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d598c6b-7fd3-3522-9bba-e750df53560a | -18.25445 | -50.81504 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d572bf67-791d-362e-acef-5a4ead6f14fc | -18.25381 | -50.81888 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4b98723-17c9-3e76-829e-d31429015494 | -18.25172 | -50.81046 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11e3fd2a-1cce-3b5b-899d-6dfb61b9fec1 | -15.67704 | -52.5071 | 2024-10-03 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a0b62008-6a22-3f61-99a2-5518fb8d78bb | -15.67328 | -52.50645 | 2024-10-03 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7aed8409-243d-349d-8e40-d496f0b375c9 | -17.7309 | -53.10291 | 2024-10-03 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9566833a-57f8-35d8-9632-1367b601e87e | -17.72972 | -53.08783 | 2024-10-03 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63d67396-34c2-306a-a7b2-9ed97855ad75 | -17.72714 | -53.10214 | 2024-10-03 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8e00e10-8299-34d6-b050-f3aae2680528 | -17.72656 | -53.06218 | 2024-10-03 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ea336b1-659e-39b0-8459-415bed8853a8 | -17.72393 | -53.07677 | 2024-10-03 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 637751c2-ede4-3af3-bfd2-c88447b35aaa | -17.72306 | -53.08158 | 2024-10-03 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bca32ec6-1bb4-3a8a-92a4-b5a088ef9e3f | -19.01743 | -54.76448 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f313e768-ff85-309e-97b9-214d56687735 | -18.89414 | -54.52411 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bf9910c-7587-35ed-a4ce-0ebab3ed0bcb | -18.89213 | -54.51261 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2b756dbe-3997-3f33-86a5-474b6a773d8a | -18.89077 | -54.51989 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9302aee-2c13-3523-b642-baa5694f611f | -18.89009 | -54.52351 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2b44a50-b1d5-3e45-a6b7-58a10194f8d0 | -18.87267 | -54.52742 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 03ec372d-97c8-39a5-bf7e-c0ec97777718 | -20.00642 | -55.45938 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bad972db-8de2-3d2b-b866-5af09781dc6a | -20.003 | -55.45465 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 708cd2f4-04c6-345d-84d5-725440b21123 | -19.99884 | -55.45372 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 77339f92-1c5e-3070-8e7f-b7b15fb10cbe | -19.99468 | -55.45278 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1bc0dde0-de24-37a6-8cc6-347543d10ad9 | -19.99312 | -55.46079 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24a89e0e-22ff-36c8-b891-fdc9465216af | -19.99245 | -55.46044 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb33a65a-7703-3f15-b943-9f11cea6fd13 | -19.96278 | -55.47958 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d35899d-693d-3ddb-b047-ae7cc80de6f2 | -19.96199 | -55.48372 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 58cd92a2-d3cf-3d08-87a9-30e51a0d3fd7 | -19.65793 | -56.47039 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a87bad1c-84fd-3fc4-9102-f8d03b9c9ff7 | -19.65347 | -56.46941 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 18893e3a-928e-3714-a627-277a8ff879d9 | -19.65253 | -56.47417 | 2024-10-03 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0efe49ab-9713-3e11-a79b-ed4321d5130b | -16.83164 | -57.46972 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 1542138f-a22b-3de3-802c-f548d5071bfa | -16.83103 | -57.47277 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| d58546d4-cb26-3c6e-b8c9-1bb961a4c2d7 | -16.82158 | -57.46757 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 99acfb05-9fcd-36a4-9e5d-d5a14ea49923 | -16.81532 | -57.47263 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c709e4e0-6521-3a4a-994c-a4a9f005f5c4 | -16.8147 | -57.47569 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 184551dc-f13c-312b-af99-34a6af94af75 | -16.81408 | -57.47876 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1125ee02-b8c9-3f8a-8d80-a8a8e0ac72c4 | -16.81346 | -57.48183 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 39b56de3-8d42-3c69-9d29-f8ab6bfbf81a | -16.80525 | -57.47047 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 067ad019-cf13-3d5e-9bf7-34f0ad54adb2 | -16.80463 | -57.47353 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c8754b7e-4a06-3e43-ad9d-fe99c246574c | -16.80277 | -57.48273 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e9bb5dc5-ea68-31a3-95fa-3b101977adb3 | -16.80216 | -57.48579 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1de996ed-63c6-3cd8-a49c-bc06282ffc56 | -16.80022 | -57.46939 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 857485da-1a31-3f00-a643-4c1d630dcd79 | -16.7996 | -57.47246 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 7a3516ea-17d7-35bc-b4e6-fae5f651efa7 | -16.79898 | -57.47552 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0ed89fe5-4dbc-3227-b621-3dca2ab1cfa2 | -16.79836 | -57.47858 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 72ae72d8-70f5-30b6-bfb2-3c35876798a7 | -16.79774 | -57.48165 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9a5aff6b-781e-3e9a-bd8b-ca939410310f | -16.79712 | -57.48472 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 37063b2f-5d8c-3114-b547-929e7a517f41 | -16.78642 | -57.48562 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1e15d086-eaca-365f-b7bf-068ae3fb78fd | -16.7858 | -57.48869 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eca0fef0-f3dd-3a8e-ad68-72727cbd33b7 | -16.78518 | -57.49176 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1f924653-b195-3d53-9fcc-366c6fac58ce | -16.78455 | -57.49484 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f4bfb670-5e9e-31b0-9320-838f6beb1cb4 | -16.78393 | -57.49791 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 98587ed6-3fda-3498-bfaf-8a2d3d4cd421 | -16.78138 | -57.48454 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 16488999-a7d1-38cb-b526-f4b3024fe077 | -16.76752 | -57.47517 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| af71bf70-d199-321f-bb07-43a288244561 | -16.7669 | -57.47823 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| af49c63f-c502-3094-a3cf-a5b129fb65c7 | -16.76311 | -57.47104 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 65bfe09c-78e7-3620-b20b-8e293d0502e2 | -16.76249 | -57.4741 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 779c1e7b-f135-32d3-8fd2-dc29aa4152b2 | -16.76186 | -57.47716 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| aadeb93a-9386-3dc9-9a63-430277541b24 | -16.76123 | -57.48023 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 397d6aa4-889c-39b0-ac1f-8a34f6ea55db | -16.7606 | -57.4833 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 05a70198-fa4e-3427-beb3-a293769a0676 | -16.75998 | -57.48636 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 4d4db6bd-6849-3463-9c72-0e809cf3ce14 | -16.7597 | -57.46908 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 4e7c4450-ed5c-332c-b3a9-67f9ec822ca2 | -16.75909 | -57.47216 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 96fd11d8-f461-35b6-93d3-aefa7568f586 | -16.75871 | -57.4669 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 24e7eb81-4be3-3461-b6dd-fe1cf0b34a69 | -16.75849 | -57.47522 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 67e9415b-b2b7-3659-be83-063a0fd438fd | -16.75808 | -57.46996 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| ec917af4-ca4c-36b8-80f3-a5e217a281da | -16.75745 | -57.47303 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 068cfa74-1a35-342d-8ea4-d66498a184c3 | -16.75682 | -57.47609 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0c0926fa-6cab-3160-8fed-7f4d0e7de8b7 | -16.75667 | -57.48444 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| c9aca3e9-9ee2-3832-b348-ede78d64c95b | -16.75619 | -57.47915 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 39bd11e5-65c6-32a2-80c5-19f6a000e9fc | -16.75606 | -57.48752 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| d4d3249c-4662-3654-8b92-890634763085 | -16.75556 | -57.48221 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2d39cc4b-d3c2-3065-9cf7-7857fa723cb6 | -16.75494 | -57.48528 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| bdd2c894-3817-3205-bf68-a2db9dd3ce16 | -16.75467 | -57.46799 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 2f8efd3c-723b-3009-94cb-1157980f691f | -16.75406 | -57.47107 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| db4a7e39-ec03-3f01-a862-c4f5af0a5fa2 | -16.75345 | -57.47414 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| cf13f163-f03d-3030-a39a-536345860542 | -16.75304 | -57.46889 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| eaa21b0a-6330-37cc-a44a-0f093f288505 | -16.75241 | -57.47195 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 388289fb-9c5c-3120-9655-8b7fe4b43707 | -16.75178 | -57.47501 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 46742067-033d-39c9-95f4-e13dd7304417 | -16.75115 | -57.47808 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7bd8d18a-01cc-3ec2-a5d6-ff06326e2f1c | -16.75052 | -57.48114 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| eac2aa62-d837-3d00-b10f-704daf1a8d28 | -16.74989 | -57.48421 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 63ba4570-9532-3944-a4f3-bf1b3c4e4119 | -16.74963 | -57.4669 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 7d6caf0a-dff8-3816-9342-7f25d774c760 | -16.74926 | -57.48728 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fc2ab409-54b6-38d4-9e0d-a4cced5ab89a | -16.74903 | -57.46997 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 8b2dbc29-59b4-3578-8c02-87d5f35e3324 | -16.74863 | -57.49035 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e34877b4-c428-37a1-9837-744dcde4f710 | -16.74842 | -57.47304 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ce574ca7-8d15-35b3-90ea-77b27f1315c2 | -16.74801 | -57.4678 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| e332af25-ded3-3849-9a45-5d5b987b91b5 | -16.74781 | -57.47612 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1e84899a-6106-35b1-9b30-1a3392beccf6 | -16.74738 | -57.47087 | 2024-10-03 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |


[Clique aqui para ver as próximas entradas](README107.md)
