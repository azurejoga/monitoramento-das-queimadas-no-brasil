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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7235140-c8d1-3206-b222-39f6edcdce3c | -2.5019 | -49.01675 | 2024-12-09 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8faf58bd-c7ec-34b4-b9c3-6ab9ef1fb875 | -3.46565 | -53.96302 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7a1cfe78-0322-340b-b3c0-472b4d7dd77e | -3.09243 | -53.21413 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5d9a6f8d-8a81-3fa1-8cca-9e560d30954c | -3.08681 | -53.21337 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b215a2e3-db2f-314d-99ac-7e664a5785da | -3.46518 | -53.96627 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25fdfbdd-1945-3c72-8341-0a55317e0e3c | -2.98925 | -53.03862 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 326e6444-a31c-354f-87c4-31ddb7df4193 | -3.67513 | -54.32394 | 2024-12-09 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c6a5619-62dc-3196-84dc-7c41686db2be | -2.9949 | -53.0395 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b8cc30a-2283-3164-8f07-40ba83ab6528 | -3.47056 | -53.96693 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13f4f1ff-38ac-3071-b066-4f42ddbc060e | -2.99435 | -53.0432 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0d4722c-7960-35ab-9794-911cbb666f29 | -2.50294 | -49.00968 | 2024-12-09 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5904c09-a7f8-3a88-a853-55fa5a25cb5d | 0.94088 | -59.91787 | 2024-12-09 05:33:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60104c5a-6d67-3dcf-8e97-0de263cc4bcf | -3.46725 | -53.9682 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 63f36b92-2b29-3f59-a64c-c1faecb05cd6 | -3.46236 | -53.96434 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f79f614a-545d-3909-bac9-2f9d9602f392 | 1.48621 | -56.04101 | 2024-12-09 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b84a6c65-d1bd-309d-ab37-f8a3ac0747c5 | -3.68037 | -54.32474 | 2024-12-09 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52a0341c-b17f-3af9-89a5-52ffb7f5e570 | -3.08628 | -53.21696 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 321d864b-b8bb-3bfc-9d09-9c98d7c260f6 | -3.46825 | -53.96166 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 627334ed-8e8e-3909-9d65-d3433d5a35b0 | -1.51578 | -60.33428 | 2024-12-09 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8037fb84-ccd7-31d1-9692-8ad783139086 | -3.09189 | -53.21774 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39caf38a-8df4-35d0-9cf0-82b6912a01f0 | -3.00002 | -53.04399 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03ab3f6f-dfff-3a69-aba1-31fb91506395 | -3.47103 | -53.96365 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 411b1fd4-3b43-3963-87af-fbfa15e86c93 | -3.46286 | -53.96104 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cba1561c-6b61-3621-8e98-addd0c555485 | 1.48404 | -56.03966 | 2024-12-09 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 793195d1-3c22-319c-87a8-bf278564f5dd | -11.75267 | -54.71892 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfe49efb-b184-3c8e-9f03-b333f098d35c | -11.75843 | -54.7253 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb7ba5fb-d96a-3fc9-a69c-d607e5c41bd3 | -11.88006 | -54.68423 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df6799d9-5bf4-3dd4-bc68-5b00893e9ee2 | -11.75169 | -54.72675 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9908c03-cac6-3501-978f-ce2073d2e800 | -10.83689 | -56.62585 | 2024-12-09 05:35:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 327c1659-743a-39cb-a0ba-a3edb1ce72cf | -11.20582 | -53.81811 | 2024-12-09 05:35:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c08d294-6058-34f9-b97a-6a6c283d1834 | -11.75269 | -54.72465 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6961e37d-9974-3900-9ad8-b70ddf298dcb | -11.75792 | -54.72348 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b86cfbd5-b183-38a7-a031-41871b083b8d | -11.20525 | -53.82273 | 2024-12-09 05:35:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b52153d-76be-304e-8b66-0d2b9350a094 | -11.75742 | -54.72739 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55001fed-a9c5-357f-bcb3-bb4707285f1f | -9.38839 | -58.22554 | 2024-12-09 05:35:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 950adf18-22ea-3afa-9c11-ff7647ca7334 | -11.88057 | -54.68018 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03a51bcd-22bb-3111-984c-1343167a522d | -10.83192 | -56.62512 | 2024-12-09 05:35:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02114093-042c-32ff-a58a-44307ac3f0f4 | -9.73168 | -61.91366 | 2024-12-09 05:35:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36be3ef8-6275-3f57-994c-c2ca905ea00b | -11.75223 | -54.72855 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d9e0522-70a5-3bb0-aaa6-caaa35e262d5 | -11.74595 | -54.72606 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 8e614c82-dc60-3bb2-828b-4f569e6f6851 | -10.83614 | -56.63152 | 2024-12-09 05:35:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1ab272e5-31b5-3f09-8560-378e52ef1448 | -11.75315 | -54.72074 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c26fbb9-a064-31c4-ba2c-8c12f981ea5c | -11.75217 | -54.72285 | 2024-12-09 05:35:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07d915cb-28be-3967-9b35-a6c26f53a9b7 | -11.88109 | -54.68451 | 2024-12-09 05:37:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50101c2a-a2dd-3b9e-9cd4-686383906af5 | -12.53628 | -57.72957 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 38b60571-d024-3d9a-b6c1-1bd333701903 | -12.53873 | -57.73886 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5749ab73-29f4-3aa8-b48d-351fcaa11693 | -13.48096 | -56.5572 | 2024-12-09 05:37:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66aac70e-8fe9-3e7d-bb90-acdcc0136e70 | -12.79158 | -54.22622 | 2024-12-09 05:37:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92c16c96-813b-30d1-bfe3-4ee0c5a78a38 | -12.53563 | -57.73476 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 16fb8014-4d3f-3293-9c4f-6b7525a55957 | -15.07937 | -59.65187 | 2024-12-09 05:37:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51f44969-e0f8-3a88-9787-8a70efd30fe7 | -12.53806 | -57.7439 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 40278d8e-21d5-30db-a043-50be8ec7fb15 | -15.07685 | -59.654 | 2024-12-09 05:37:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f042249-d7cf-3e31-bf5b-e49ff2d167b4 | -12.53399 | -57.7383 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b5a0cf5-9093-33fd-a348-6633b4e0ad50 | -12.56551 | -57.76471 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bce4fa92-e357-3f11-abb0-ae05f78af37a | -12.56014 | -57.76918 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd4b25d2-89f7-319f-a04d-402938ef4a35 | -12.53973 | -57.74044 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a9592a43-0552-3acc-8fe4-56747614a4e3 | -12.56079 | -57.76406 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d3b2d0-b2ec-31f5-baa9-d19f26117795 | -12.54279 | -57.74446 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5df16091-86ff-387f-8d72-a220f1c5c3c6 | -12.53332 | -57.74331 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dfb1eb01-6cd6-30d0-b4dd-5b1feccca052 | -12.54037 | -57.73532 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e6f47fa5-bd45-3381-9fbb-f83c76b5074e | -12.78559 | -54.2254 | 2024-12-09 05:37:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 435799ae-23e4-3289-abbd-4d1e407dbf2f | -12.53467 | -57.73316 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a027b9e8-6f10-3839-97d8-534378baddf4 | -13.0254 | -57.21856 | 2024-12-09 05:37:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89d9c241-662a-33a5-b53b-ad77a0eebe55 | -12.53909 | -57.74549 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 07f8c796-7a20-3024-ae4c-d4561792e26c | -12.53436 | -57.74489 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8764bdab-1e2d-3d4c-8cc6-2ca795a2b851 | -11.88157 | -54.68045 | 2024-12-09 05:37:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c7d0cd8-7d45-3f85-9719-53b2a536fc34 | -12.56485 | -57.76986 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80592c72-9221-3335-aa32-117452b4745e | -12.53941 | -57.73372 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bd7e8b55-d24d-3f09-9d9a-1edee0751edf | -12.53499 | -57.73987 | 2024-12-09 05:37:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4200f205-e17c-3094-bc71-459b0ee0e76a | -3.09163 | -53.21571 | 2024-12-09 05:46:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50eef72d-40c2-3d19-afff-afbd1474218d | -2.78265 | -53.24159 | 2024-12-09 05:46:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| b916d38d-ef1c-31bf-9fe1-30559bafd50d | -3.22911 | -42.4327 | 2024-12-09 05:46:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| fbf3ff4f-a3f1-310c-acfe-d0a7be068fa4 | -2.90182 | -48.02021 | 2024-12-09 05:46:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 381f7297-3aaa-3cd0-bd08-e58e4160d68e | -2.99752 | -53.04591 | 2024-12-09 05:46:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| de7531b5-978c-31eb-9673-987ad66c7b47 | -3.45868 | -53.96752 | 2024-12-09 05:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 99474716-78b7-3c66-9925-0de20cba6b86 | -2.77509 | -53.24493 | 2024-12-09 05:46:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8626ebba-68f1-3568-8fea-ea3f30429804 | -2.78418 | -53.23168 | 2024-12-09 05:46:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f6256045-60bf-38c8-90c5-29d35cd641d6 | -2.77657 | -53.23498 | 2024-12-09 05:46:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f03c3120-591c-38bb-8993-4468b6f75b73 | -3.21754 | -42.42591 | 2024-12-09 05:46:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 475a09e7-3611-343a-977f-2cac68b33060 | -5.57178 | -45.20123 | 2024-12-09 05:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 58b676ff-e39e-3a0a-8605-abeab19e4f46 | -3.4603 | -53.95686 | 2024-12-09 05:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 50a7dfe6-ffc8-3406-8c7f-0a5eb4254e8d | -11.75683 | -54.71951 | 2024-12-09 05:48:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| aecce2ac-5823-30bd-8f76-239d8f091099 | -11.74771 | -54.71804 | 2024-12-09 05:48:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c149a3b7-176a-34dc-bf1a-94cf1e889413 | -10.9217 | -48.93077 | 2024-12-09 05:48:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e5789157-7354-3f7a-a9e7-17a622fc4b2f | -12.90683 | -55.05268 | 2024-12-09 05:50:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e205eba7-7b4c-3e36-924d-eccf5f4df16c | -15.97842 | -57.1691 | 2024-12-09 05:52:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5ffcf42f-6e9b-315b-ac22-89287b92f0a0 | 0.80851 | -60.27581 | 2024-12-09 05:57:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6733642-6e1d-30da-921a-7a7f737e9a24 | -12.52872 | -57.77647 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 249245ff-8a8d-317f-a2f8-5ef9f1287354 | -12.54009 | -57.73652 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 87acb742-b7cc-3862-a758-e24ee1bca4e0 | -12.53938 | -57.74317 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 305923f5-1eb5-3cd2-82e1-ba5c18466d49 | -12.53308 | -57.73599 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f389aa2-5f9e-3245-8fbe-d931cb7dce4b | -12.56346 | -57.76946 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd4e2eb8-f001-31e8-8efc-e6cd6d53ceb4 | -12.53866 | -57.74984 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2ad53d33-0f80-39b8-95b5-8306021de049 | -12.53237 | -57.74257 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e61f41cc-845c-3430-883f-ca65e86b19ac | -12.56436 | -57.77337 | 2024-12-09 05:59:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 110ca65a-0d55-3219-a4ca-8c80c4ef5e46 | -3.2351 | -42.4353 | 2024-12-09 06:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| ab18c657-b338-3873-96b8-283f2a069b10 | -3.2351 | -42.4353 | 2024-12-09 07:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 5044b65e-fcdb-3077-a7f1-8571a31fefb5 | -17.37 | -44.92 | 2024-12-09 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4531d414-ecf4-3b9c-b52d-cb46829739dd | -17.43 | -44.89 | 2024-12-09 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3b9fef1f-51c1-38b8-8037-b9cde81059f9 | -17.4 | -44.88 | 2024-12-09 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
