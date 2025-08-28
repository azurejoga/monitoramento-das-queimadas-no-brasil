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
| 5b2d2428-bf33-3b91-a78e-75bf04b05abb | -3.2285 | -43.424 | 2025-08-28 00:51:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d3bb627-235b-3ea1-8ada-116a92e5ac98 | -17.553699 | -46.607601 | 2025-08-28 00:51:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 184ae2f6-b57f-3b02-88a5-907bcac9fa2a | -15.6763 | -52.725101 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e7bd966c-8740-374f-8cef-7baffc6e5861 | -12.4426 | -48.713402 | 2025-08-28 00:51:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50578853-cb8c-3753-b370-7a4e481ab846 | -10.1294 | -47.431999 | 2025-08-28 00:51:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af5b42f2-ac55-34cc-bdb7-f7a7a099d5c4 | -18.473101 | -49.699699 | 2025-08-28 00:51:00 | METOP-C | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 807fb4c8-c583-3346-86c1-7e130390d2da | -12.9267 | -46.3284 | 2025-08-28 00:51:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 089113b5-c863-3d8e-a8e5-317b5618f37f | -15.6568 | -49.753799 | 2025-08-28 00:51:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb12ab0-a2f3-3500-8329-dd53a0693234 | -14.5633 | -52.009399 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dff0f980-0b3b-3456-89bb-40cb935e6341 | -3.2369 | -43.459202 | 2025-08-28 00:51:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94b701d6-ead3-3290-8569-f0a120b2814d | -8.2332 | -55.555401 | 2025-08-28 00:51:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f300982-bf5c-36ba-ab99-83495c51c4d6 | -9.4834 | -51.942799 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f31c914-b351-3c97-b93a-c88f054c7987 | -6.8652 | -43.629501 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db0bb70f-ded9-3612-aa14-fcf1b5539c99 | -12.4131 | -47.7845 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebba0bd0-b1d7-3b58-aaba-df40a987a194 | -9.485 | -51.950001 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94d6c7b7-b28f-341e-af28-5ca365f95e4a | -13.4644 | -46.980301 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a95d8c23-752b-3f69-90d0-4dbe2e6fe20e | -3.979 | -47.879799 | 2025-08-28 00:51:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c79e94ac-d8f4-321b-87ef-ac3bf1d00381 | -9.4074 | -48.226501 | 2025-08-28 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d44a82f-ba93-3d67-b495-30fe2e415487 | -10.4671 | -57.937099 | 2025-08-28 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3c8399c-34fc-3813-b936-3d40312e5152 | -9.6006 | -40.327999 | 2025-08-28 00:51:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f15620d-1493-3720-b274-258ebfcc97d6 | -13.4294 | -46.963902 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d96ea892-898c-31e0-b320-a5e875974058 | -13.622 | -48.2309 | 2025-08-28 00:51:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 447dc7a7-3d46-34f5-85a0-e7b3221b30aa | -3.9888 | -47.877602 | 2025-08-28 00:51:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ffb0be2-d2d3-3e0d-a275-f068938484a0 | -6.4478 | -44.575001 | 2025-08-28 00:51:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ec28d48-b3c3-3545-8588-647a9a204b64 | -11.2366 | -55.060902 | 2025-08-28 00:51:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa155c7-78fe-3854-9625-fff6567325c6 | -4.7847 | -47.272301 | 2025-08-28 00:51:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f73c55e6-127c-3f05-a22d-10999a739d2a | -6.5766 | -47.388599 | 2025-08-28 00:51:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20a6d839-750e-3c91-ac6e-0011b8858bfb | -10.6124 | -55.395599 | 2025-08-28 00:51:00 | METOP-C | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c385c962-b318-301a-8ee7-ccc2f1fb8c31 | -3.7408 | -48.935101 | 2025-08-28 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f634dfef-967e-3cba-9be7-f181149ac9bc | -9.4025 | -60.5205 | 2025-08-28 00:51:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92e959ef-c4be-38d6-b24b-1fb90d523aa0 | -11.3325 | -43.540199 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f804970f-c2ff-300a-99b6-40360bec59a3 | -12.7968 | -48.190498 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 485cab74-7f3a-3f43-9d95-212988788425 | -4.2948 | -40.917099 | 2025-08-28 00:51:00 | METOP-C | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b7877f4b-87a6-3909-a3ee-1301978f93cc | -13.7427 | -51.913898 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7738a10-020a-3146-a821-bcbd0a68fd41 | -10.1816 | -51.658199 | 2025-08-28 00:51:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aedaddeb-c15b-33e9-9ed5-fc00cf2b92ce | -9.0524 | -54.9394 | 2025-08-28 00:51:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0c59345-4c0b-3139-b72f-03e4bf48e41f | -19.1187 | -44.014801 | 2025-08-28 00:51:00 | METOP-C | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| abf180f3-294b-33c0-9a91-e78a52ff1790 | -21.0329 | -46.2313 | 2025-08-28 00:51:00 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ff31ea6-f6b5-3e97-9a64-1eb2e8d93be1 | -9.4189 | -48.2318 | 2025-08-28 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff89ab55-23df-3bc4-a400-b8badd912de5 | -18.4715 | -49.6922 | 2025-08-28 00:51:00 | METOP-C | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e1062a6-83c9-3649-9189-5e84f6809c0f | -13.5472 | -46.893501 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 08508c88-b6dd-395d-917c-51aaeb0213c0 | -6.8675 | -43.597198 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fbaf867-e88b-3130-aaf1-7c93efec5013 | -7.2538 | -45.346001 | 2025-08-28 00:51:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32450c25-0b75-3b88-9a48-d73dac0aca7a | -8.442 | -43.669899 | 2025-08-28 00:51:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 132dea6c-4751-3aab-b0b4-4a36cf2f38db | -13.7508 | -51.903801 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bcd4185e-8865-3c84-98d8-da5a7c82f363 | -9.0622 | -54.937302 | 2025-08-28 00:51:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 927a7d37-ea26-3ec3-b81c-f3ef3d923f24 | -13.672 | -46.8964 | 2025-08-28 00:51:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 745e4049-d24f-3de3-9fbc-8c2c274aa09d | -20.155001 | -47.369598 | 2025-08-28 00:51:00 | METOP-C | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ecf4060c-bbda-31d6-947f-2bebb3e36f35 | -5.3189 | -55.866001 | 2025-08-28 00:51:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3627dab-fc0d-34a5-839a-e74b758330e5 | -13.421 | -46.8405 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 48a63206-e84a-32d5-9410-2dd87f22d831 | -3.7875 | -45.026199 | 2025-08-28 00:51:00 | METOP-C | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c58d5e49-f83d-3351-8987-29287d5c65db | -11.3487 | -43.522301 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd13f528-b964-3a08-8650-72c6862c26a6 | -13.3894 | -46.881802 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b2b0ef88-7023-3019-9844-76d764694cd9 | -11.2344 | -55.050301 | 2025-08-28 00:51:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d038cec3-29f4-3810-bf0a-d3bb006893fe | -8.9039 | -47.317799 | 2025-08-28 00:51:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7652c31-6e5b-370a-9198-dea7f33fd2d5 | -9.1842 | -60.7869 | 2025-08-28 00:51:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c92d98c8-0ee9-3eb8-8e93-c393fcb10510 | -9.1793 | -60.762699 | 2025-08-28 00:51:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| beb07924-93e4-3d21-865f-92578782adec | -14.5731 | -52.007301 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5092135-999a-3e1b-88f7-b589431ecc84 | -3.7668 | -54.808102 | 2025-08-28 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a14bcbbb-fd4e-3c89-997b-c73987166aa2 | -11.3422 | -43.537701 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4514020f-139e-3817-98e4-70b4197d3e3f | -6.1781 | -44.060501 | 2025-08-28 00:51:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9c63509-f5cb-3a68-b229-597f18d578a8 | -12.9365 | -46.326 | 2025-08-28 00:51:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0db5e889-3b62-3a91-939b-2699dc25deaf | -11.5781 | -47.6161 | 2025-08-28 00:51:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed131285-5f23-3252-9b75-16c75d562d6f | -10.4802 | -57.951199 | 2025-08-28 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce23a6dd-4f84-3384-bb4a-c4f3d8f4b8e9 | -3.2442 | -50.799999 | 2025-08-28 00:51:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc61098b-ff4c-3237-a02b-4184d378c464 | -21.010099 | -47.365501 | 2025-08-28 00:51:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 08f7f1a2-666c-377d-9590-03d954284939 | -13.6203 | -48.223598 | 2025-08-28 00:51:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eb186803-d698-3511-a4f6-ef3d2a0325aa | -9.1745 | -60.788799 | 2025-08-28 00:51:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2c57ca-e59a-33bb-a31c-31be604dc2aa | -3.9811 | -47.888699 | 2025-08-28 00:51:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91b2ad9e-2e46-3b48-a93e-1ccf465d7524 | -8.058 | -48.021702 | 2025-08-28 00:51:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44037407-8c30-3a8c-aebf-daece05fc4f2 | -9.1043 | -46.038898 | 2025-08-28 00:51:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36614cce-9f89-3972-b7e4-306311e094bf | -13.0891 | -46.315201 | 2025-08-28 00:51:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be6acb16-9398-354e-ac6a-6889af6b7d58 | -7.2565 | -45.357399 | 2025-08-28 00:51:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5964964-d445-3b09-8a7e-9ffab41723ff | -13.4755 | -46.852402 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10ae25be-9858-3136-a021-0ba133068171 | -10.4736 | -57.918999 | 2025-08-28 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 961e5d6f-cec4-3d3d-8589-4608f538a215 | -13.4233 | -46.982101 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2aa14cc6-c903-3555-be0b-1ddbaca34b04 | -7.3518 | -59.644402 | 2025-08-28 00:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05d8c6f2-2e4a-3764-848f-31e30da28f30 | -13.5221 | -46.8745 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 27d7f756-bc52-3154-805f-c87a54cfa586 | -11.2268 | -55.062901 | 2025-08-28 00:51:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 675d7d97-bce4-330c-9d93-8bb30c3730bc | -9.4075 | -60.495201 | 2025-08-28 00:51:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48d6c702-f250-3b6b-b849-014d9d2d3170 | -13.5453 | -46.885601 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 59f84a53-78df-35e0-9189-48d39a99c5ea | -10.3262 | -46.781601 | 2025-08-28 00:51:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61cc7b89-30aa-35b8-bafc-49477354e8ea | -0.7548 | -47.7495 | 2025-08-28 00:51:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5248d425-3d93-3914-b799-6d1dd7c5409d | -9.4572 | -51.963699 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60243ea7-9815-390e-ba76-4de07de0e17f | -9.4638 | -51.947102 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eea9b64e-2cc4-365e-be63-5bd9447bf746 | -13.7312 | -51.9081 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f408aea2-58b2-389b-9cb2-50eb37f10d5c | -8.5602 | -51.316799 | 2025-08-28 00:51:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e905262-b852-3655-b79e-1a0e9cdd2f12 | -12.8127 | -48.125301 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2936bd90-750b-3532-9ce9-329558b306de | -10.5331 | -46.695499 | 2025-08-28 00:51:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20ff5ebd-71f0-37f4-a978-ad895814cfca | -4.0169 | -49.501499 | 2025-08-28 00:51:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 515a9873-cd18-3c53-96fe-49a9341fbd5c | -13.4331 | -46.979698 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38f84584-ba2c-3bfa-b04a-ace4521cc7d9 | -19.069901 | -42.126301 | 2025-08-28 00:51:00 | METOP-C | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db3a9814-79fa-3645-b486-beebb3304077 | -7.3421 | -59.6464 | 2025-08-28 00:51:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6965c9fe-e860-32b1-b53a-479a8a216e57 | -13.7393 | -51.898102 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da859234-5f6e-3a6b-b17a-9f54116f3c72 | -13.4392 | -46.961498 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6109c606-cf8b-30db-a4cd-bec2f46acd7b | -12.9573 | -44.5811 | 2025-08-28 00:51:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f355bff2-bb6f-34b4-9be0-80ef2cfad28d | -17.761801 | -44.486599 | 2025-08-28 00:51:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5383a5f8-7e5d-3c13-8353-84adcaf0960f | -6.1869 | -44.0126 | 2025-08-28 00:51:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94cd49e4-e710-32bd-82cd-d873c9688b12 | -15.6156 | -52.728699 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb55fea5-95a3-3300-97bf-373d779bf989 | -12.7833 | -48.983601 | 2025-08-28 00:51:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
