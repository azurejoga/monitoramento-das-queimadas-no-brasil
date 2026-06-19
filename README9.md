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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a31ef982-7320-3883-8753-9f371d994d8f | -17.32159 | -43.64212 | 2026-06-19 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d5b60ab-2b0d-3965-a97c-b82780b2f68f | -11.47872 | -57.10983 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9c9d621-8775-3d3c-b782-2c701b9c492a | -16.02884 | -43.42774 | 2026-06-19 05:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c721e4b6-9768-3f4f-9256-812dc5983777 | -14.21722 | -54.70403 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bd0f796-48c8-37da-9ed6-05524e4d3096 | -16.986 | -53.20826 | 2026-06-19 05:04:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 897be7bf-9d8d-3d69-bc97-68af6ece5cf3 | -11.78538 | -57.00117 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9ee0017-b07d-3af8-b056-7e1b94718f94 | -14.22055 | -54.70459 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce186c2b-23ae-3e55-9814-f1be067eff45 | -12.86306 | -44.37008 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf3e03c0-3ab5-3865-96ec-fc3348238c26 | -12.87522 | -44.36381 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00670620-8d95-3afc-bbd1-5e62b6519a48 | -10.90663 | -56.85388 | 2026-06-19 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1be3f44-1a2c-35cf-9bc3-9bd74149c24c | -12.78428 | -44.5083 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14a8067f-1983-3b41-a844-6496e89bb4a7 | -14.21389 | -54.70348 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4e8859e-b296-3067-9a87-055ae4842a5b | -15.0692 | -55.80975 | 2026-06-19 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7fedf78-12d4-35d8-81c7-c81f1220fac7 | -10.57349 | -57.32224 | 2026-06-19 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebf975d7-87fb-3450-9ce2-213ae8b79409 | -13.94159 | -53.56814 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04c4855c-7b74-3c2a-a6fb-a59092f40d3d | -13.93598 | -53.55978 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3b60aa61-5816-33ba-9329-edb561828276 | -12.77935 | -44.51644 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3618005-29c9-3dfc-a6ca-b43e6757496d | -12.87005 | -44.35938 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 132726e8-56c2-3a7e-afb6-8ac2ea4983cd | -11.3566 | -55.82201 | 2026-06-19 05:04:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7d97fbc-c03b-36db-b075-211793e12895 | -12.54762 | -54.58962 | 2026-06-19 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb21d6ec-deed-3a22-92ac-ca2430c92776 | -11.66513 | -56.76705 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a8b5125-cf5c-3bbf-a43b-a99156ef69dc | -12.78983 | -44.50903 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c91f3111-3deb-3a94-9b3d-0c0e3a4a6db0 | -12.54706 | -54.59317 | 2026-06-19 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10cad393-63c5-3c98-85ab-f45916d0edc0 | -17.32323 | -43.64691 | 2026-06-19 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37274c7f-3a55-3e74-b51f-9bb73676a645 | -12.13651 | -48.26307 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58a85e18-2d25-38d3-9858-f08badd2c8c5 | -12.55151 | -54.58663 | 2026-06-19 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a70a422e-4c32-3a89-85bf-84a5a7664bd3 | -12.20838 | -52.77386 | 2026-06-19 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbacbae7-3029-3b69-aa92-fde370d9c34f | -12.87476 | -44.36762 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 10e2d4c1-60ef-3a0a-9219-587057481f1a | -10.57717 | -57.32291 | 2026-06-19 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b90ab00-544a-3708-bdb3-e3c12be4b2bd | -17.95272 | -54.46292 | 2026-06-19 05:04:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c01569f5-7f88-300c-84be-ab845d0d106e | -18.49112 | -51.66633 | 2026-06-19 05:04:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4909211d-6212-3e66-bf0a-680a8911d6f6 | -12.84061 | -44.36715 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6df2d4a9-81e4-30cd-8ecb-f0d2b876a580 | -16.02314 | -43.42217 | 2026-06-19 05:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b6ec48f2-dde5-323f-b269-35003adb4a74 | -13.31409 | -45.15934 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd412919-dd3b-3401-a136-654d2b7885e3 | -16.26805 | -60.00395 | 2026-06-19 05:04:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ccbbe07-81a9-3633-b595-ee67792289a4 | -12.91905 | -49.48093 | 2026-06-19 05:04:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7384733-4480-3f57-bb80-25d3d7097139 | -11.52088 | -54.26144 | 2026-06-19 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2df2fb2-1521-39e3-a543-1f0f7717cefb | -12.4945 | -43.76737 | 2026-06-19 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8dc12765-af0a-337c-9b7a-9399e856cab6 | -13.93879 | -53.56396 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1c963b8d-8717-3258-ae55-c3190c37efe8 | -10.91021 | -56.85452 | 2026-06-19 05:04:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e7fae80-98f9-3ba4-9cf1-6348614d388e | -11.91449 | -55.91423 | 2026-06-19 05:04:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f0d55e5-4552-3a01-92b0-9bb17a833757 | -16.02984 | -43.41813 | 2026-06-19 05:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d96537e4-238f-3a20-ae48-76309b17ba6f | -12.14908 | -48.45506 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83042d3a-7063-3b65-9595-4ad42c23cf6d | -12.14963 | -48.45114 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4580e515-73e1-3800-96f9-b06e846feca2 | -11.79239 | -57.35521 | 2026-06-19 05:04:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fc918fe-228e-39b7-9a0a-dd8bce9db901 | -15.06861 | -55.81341 | 2026-06-19 05:04:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 099d0bb6-3470-33ef-8c4f-685d458389ca | -13.32355 | -45.17086 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfedcd08-3f30-3a7b-8e68-07cbc592ec95 | -14.20554 | -54.71306 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc94c784-4b61-325b-b019-e36f1c3f17b9 | -17.10682 | -49.75508 | 2026-06-19 05:04:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cb771f7-c543-3e9f-b6fb-41d8c24789cf | -17.31758 | -43.64088 | 2026-06-19 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1667993-225b-37ed-852b-aac259b8d5de | -18.82848 | -51.47203 | 2026-06-19 05:04:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43723630-afa1-30c2-b157-2ec148688d70 | -13.49329 | -47.50692 | 2026-06-19 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 488f9faa-d9b9-3d5c-88f3-f5581c728d87 | -11.48492 | -52.91842 | 2026-06-19 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c73a710a-d28c-341d-88ba-3c9f282ce694 | -12.78026 | -44.50907 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c37399e9-dc0d-362d-9586-462de05d1216 | -12.86822 | -44.37456 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 5445bf4c-8ee9-3ea2-80af-6d507f43332c | -12.91833 | -49.48616 | 2026-06-19 05:04:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e9faf54-6e9d-3020-83ab-d8d3b36b451d | -13.49287 | -47.50473 | 2026-06-19 05:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcd4979d-0fcf-36ec-a1b8-7cb6778fdf44 | -12.87947 | -44.37584 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ff9fff0-a858-3f54-8aa0-0ab6d230d36b | -11.47802 | -57.11405 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d76ec538-57a2-3894-8f95-5aed1293a740 | -18.97379 | -52.45463 | 2026-06-19 05:04:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dcbb654-6d71-34b4-a91b-aeba14d321f6 | -15.64838 | -58.01983 | 2026-06-19 05:04:00 | NPP-375D | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fb616da-35ab-30ad-a30a-ffa35a899c50 | -11.90228 | -54.83309 | 2026-06-19 05:04:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9873efd1-b9ca-3ee4-8409-b026b2f0885d | -12.77981 | -44.51275 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70874512-2552-325c-87a6-81a5a171f3ad | -13.3227 | -45.17775 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c0221a0-cadf-3d2f-9d23-41c112761d29 | -12.49983 | -43.7722 | 2026-06-19 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3e38329a-26c7-351b-9d62-4d8fe2510f49 | -18.97441 | -52.45016 | 2026-06-19 05:04:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7289da8-330a-365b-bb80-9a4c0ee6d477 | -12.835 | -44.36637 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbc307f6-3a99-38c9-a393-d6a484918ace | -13.94215 | -53.56451 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2e34204-3b7d-3f5a-ac21-54ef1989d340 | -12.13169 | -48.26645 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 98df6e4e-dff9-3311-af9a-6b3f7a0c17d4 | -16.02933 | -43.42295 | 2026-06-19 05:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d4765e00-0e9c-323a-9d1d-a6680fbba4f8 | -14.20887 | -54.71361 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6b34351-3954-3ba9-961a-f237b4781e4b | -12.13223 | -48.26247 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 14de832d-f936-3582-a52d-440665021344 | -11.7818 | -57.00057 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a92efc40-b0b8-32bc-9c1c-449197ef451e | -11.66686 | -56.76393 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fac35ed-3d05-32f5-b7a4-2b9a48442413 | -12.68995 | -54.58362 | 2026-06-19 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 945b0daa-5c9b-3070-a715-e7a11f6bd7fa | -11.91411 | -55.91352 | 2026-06-19 05:04:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 220bfddc-ae73-37b6-ac6d-a6ef60f3dc70 | -12.87384 | -44.37521 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 169dc0e1-3276-3bbe-b2fc-075b4cf0249d | -18.82465 | -51.47148 | 2026-06-19 05:04:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56dd35b4-d8fc-36b2-a9dc-47af546adbb0 | -13.33537 | -45.20702 | 2026-06-19 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e5bb23c-e62c-36be-88bf-77d73a6283dc | -12.79184 | -44.50681 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75e5ff24-30c3-33b8-9d15-2c7adf5d681a | -17.32378 | -43.64164 | 2026-06-19 05:04:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5efd9709-9d00-3770-90ec-435499633648 | -12.83456 | -44.37014 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6f04198c-2f1e-3a6a-a36b-bc77694f6fb6 | -12.77754 | -44.53101 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4b04446-345e-3f60-b926-50ae548358d9 | -16.26409 | -60.00321 | 2026-06-19 05:04:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e4e96bb-c0d0-3399-b44c-c8cf176c632d | -17.35087 | -53.8144 | 2026-06-19 05:04:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 884b226d-5e9d-399c-90a9-18b737776ec1 | -13.93543 | -53.56341 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2ed7da26-ad15-3fce-b382-c8a4976f4976 | -12.49934 | -43.77633 | 2026-06-19 05:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c07bfeb6-dbb0-3fba-86ba-06f076cfbcf8 | -12.15439 | -48.44783 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fa9b33c-93af-3680-8686-e105920b571d | -12.13597 | -48.26704 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 449f5dd8-399a-3b44-9a7c-3c72fdfca246 | -11.7825 | -56.99643 | 2026-06-19 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55b8cb0d-5934-33f7-94d4-e262b3573f34 | -12.87568 | -44.36 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62b523fa-b483-34a0-a4dd-32ae15c7278b | -12.78385 | -44.51199 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97d91b8d-93f3-3ecd-912c-b5fc242202e3 | -13.9455 | -53.56505 | 2026-06-19 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 427ffd99-bed9-3a40-bd09-0235594f7335 | -11.50992 | -56.1201 | 2026-06-19 05:04:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bdefd9d-4029-3ca2-9d28-25b031246191 | -12.89041 | -50.16463 | 2026-06-19 05:04:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac5615a8-0f8a-3668-9711-cece55dcbd32 | -12.86776 | -44.37834 | 2026-06-19 05:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 9e920267-a429-3208-9a9e-acf9b197e723 | -12.15017 | -48.44723 | 2026-06-19 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a61230b-08fd-3e04-8e50-3d8464591155 | -16.02365 | -43.41731 | 2026-06-19 05:04:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a01a29df-bc76-3964-b80b-978c9b993936 | -11.26041 | -53.95905 | 2026-06-19 05:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f47cf506-2453-349a-92ba-4a10870aad5d | -10.72409 | -60.74903 | 2026-06-19 05:04:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README10.md)
