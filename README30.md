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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3e083a1-3454-360b-a75f-8de44533adee | -13.25093 | -47.88276 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| badb7880-549d-3ecf-858a-00caeac705db | -12.82083 | -48.6332 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 842c79e0-3465-3ff0-9ea1-943ee78c8b9b | -12.41716 | -54.36116 | 2025-10-24 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 301bf37e-f948-3403-859a-fabf1a9d8985 | -13.34714 | -47.97759 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ed33abd-5325-3cd3-9cb5-cc25eb061576 | -17.0967 | -46.1848 | 2025-10-24 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb095379-3f7a-3b43-bbbe-ae8eefd0705b | -13.33114 | -47.96203 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39ff356b-e4c1-3aaa-a550-2d0eeb3a9840 | -17.37718 | -52.01898 | 2025-10-24 04:19:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5497199-a23e-337a-9e39-96e512f06799 | -8.66237 | -44.77896 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c926e23e-318d-3dea-978a-8ee81fd7ade2 | -13.1548 | -47.09687 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f78484f-2584-3565-9b77-21b0134ee70e | -14.48279 | -47.91828 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e27cfe65-6a30-3d62-a30b-504c476f2f26 | -12.81807 | -48.63107 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f86d88b8-364b-3466-a899-24741b185551 | -7.399 | -43.91697 | 2025-10-24 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96cb8e89-ebcc-3c10-a278-82c2f58ba0b5 | -6.81602 | -45.46254 | 2025-10-24 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83273bc5-ef82-341c-81ab-4780cc0d053c | -6.8556 | -46.92968 | 2025-10-24 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e43d6d5a-3ebc-3b00-9517-6dfb3b3fabf7 | -13.90452 | -48.39009 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7feff69a-c153-34cf-a15a-57bde2cf272d | -6.44736 | -47.27378 | 2025-10-24 04:19:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a79aa1a9-b552-344c-b090-e9a8aac66f37 | -8.33019 | -46.24899 | 2025-10-24 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8267548-15ba-3d43-99f6-566fabbe548a | -8.61178 | -44.81462 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e3a6658-da13-331e-aa35-a1932e564203 | -8.11269 | -47.04609 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c21c4ef9-c92e-384e-83a3-5494b8090bbc | -6.92005 | -47.16961 | 2025-10-24 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9afdef2b-24ad-34d2-b292-38871119c327 | -16.32961 | -49.08517 | 2025-10-24 04:19:00 | NPP-375D | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ad04062-9843-3693-96aa-c71d67681e09 | -12.80672 | -48.62922 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 373271fd-9a74-3c8d-aa77-026cbfdf205a | -19.4619 | -50.44731 | 2025-10-24 04:19:00 | NPP-375D | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 237ad1fb-00d5-32a4-abc4-953297ae965d | -8.61573 | -44.81158 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78e35add-cc36-36b6-a45f-127e2e300e3f | -14.46482 | -47.91601 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 829055a7-6c54-3926-af2f-045d3510f2c1 | -13.66802 | -47.95628 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d20f6762-d265-3de1-a173-e252e9d4c512 | -8.56795 | -44.86316 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4eed604-d28e-332b-9284-48e5cde86f30 | -13.35507 | -47.97485 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 886bba1c-4a9b-3459-8291-829f1bd07b0f | -13.7311 | -48.37033 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26ddef08-50eb-3261-9268-39790b089a6a | -12.81779 | -48.62836 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67a498ae-28e5-3ff2-bcc6-bfc76c418e26 | -8.73996 | -45.83794 | 2025-10-24 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46f1a0a5-1382-3362-9a1c-56bc9c048d1f | -17.60031 | -46.63152 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1ded8477-6252-39e4-9613-5a1a6b3de7d5 | -12.827 | -48.6645 | 2025-10-24 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b77126f-b145-3867-b321-c794b17551a7 | -7.00647 | -45.21006 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d51968a-a315-33c4-8aa7-930593a2764c | -15.83447 | -49.09625 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 87ecc9de-9e56-3790-9a65-119535612aab | -15.60296 | -48.0516 | 2025-10-24 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38d04ffa-f716-3b71-9bbd-892732d9c29e | -14.27382 | -48.13152 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c58e6fb9-bb22-37c2-bb7f-857c20ceacf2 | -14.9195 | -48.13742 | 2025-10-24 04:19:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7526bc28-5dc5-35bf-ade1-d57dc554f0d1 | -8.65336 | -44.79216 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 434959ab-8947-36e0-a9c7-cccf2207be10 | -13.90819 | -48.39077 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a896ffe-6c16-3eec-9a06-a7476971f264 | -12.73157 | -46.94918 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dec1e391-75b6-3c70-bcc0-2d33ac880bd4 | -17.78414 | -53.31222 | 2025-10-24 04:19:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| edb863b1-8821-39b5-a220-0d767c1ef715 | -7.42839 | -40.72469 | 2025-10-24 04:19:00 | NPP-375D | MARCOLÂNDIA | PIAUÍ | Brasil | 2205953 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b83ca7bb-086d-34a7-bded-9a19832cb5e2 | -13.19526 | -47.75269 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34960b11-bee1-3007-8f89-15372a4c0405 | -13.19039 | -47.75346 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2beab37-9789-3379-aff8-4c0a4808080a | -18.91619 | -47.18079 | 2025-10-24 04:19:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f4f85ee-6c54-3c3d-be18-92ffe986cd66 | -13.35292 | -47.96547 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 724563a3-a1a0-3aef-b016-cf8106073a5d | -12.82737 | -47.24263 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0ae35aa-8e25-378d-95f9-ec185dfbd2de | -7.55204 | -47.36631 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f3a0d8f7-2ec3-30b9-acd8-289cd354e4d2 | -8.65278 | -44.79574 | 2025-10-24 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51134400-e5ed-3927-8dad-8e6b9c0a88e6 | -12.95245 | -48.49917 | 2025-10-24 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52223625-8ffe-3a10-9537-ec0f62f38e8c | -6.99438 | -42.79341 | 2025-10-24 04:19:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9f6f106-bf21-3957-bf5d-6257804b8498 | -7.27426 | -50.00417 | 2025-10-24 04:19:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ea0657d-1f9c-372d-a44d-1b4ebb7abecd | -8.11638 | -47.04665 | 2025-10-24 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83eb68d7-2adf-3c48-807d-b2ac304c874e | -7.78264 | -45.40165 | 2025-10-24 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3ce3f3e-b7f0-3164-966d-4b390881e8da | -18.34974 | -51.69599 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a74fb0f-938c-360c-a460-f55dfe966ca5 | -14.34733 | -46.88319 | 2025-10-24 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c8d73a3-f29b-30ca-8f6f-7b26d428ba9b | -12.39528 | -57.53008 | 2025-10-24 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4a41ddd-1aa0-3119-93bf-60da26b19678 | -6.7747 | -45.47544 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5328fec0-0aa4-3562-8ab7-7d7278b5d9a8 | -12.95659 | -48.50225 | 2025-10-24 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13f1adcb-cffe-376f-a19d-ab5c377aaf86 | -9.15641 | -43.15855 | 2025-10-24 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 054ebad5-7b85-3d16-9d2a-db1bc29f809a | -8.196 | -44.43765 | 2025-10-24 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69a0752e-536f-391b-b936-bd3d43e96303 | -13.77385 | -48.34227 | 2025-10-24 04:19:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bce5247-07dd-39ea-8f37-0b13423b5ccc | -19.67077 | -44.77753 | 2025-10-24 04:19:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 117abeb2-560a-3410-9e5b-5cbf4f2bed61 | -8.20151 | -46.98972 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| dfc79623-3ab1-3f83-96b1-9066ac4d10f9 | -6.92082 | -47.16505 | 2025-10-24 04:19:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7f20fe0-8e83-353d-ab57-1609cf444db6 | -14.77536 | -44.97244 | 2025-10-24 04:19:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6369dc0d-3d83-30e0-8a7d-b7f5c4166ee8 | -12.95285 | -48.50161 | 2025-10-24 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 740ab7e6-165c-3170-945e-219849efdc7c | -13.40399 | -47.35845 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 551cc0d5-8311-301f-9c9e-4112608f6758 | -18.60476 | -51.79236 | 2025-10-24 04:19:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3fa13a2-40a9-3acb-a4df-76916e28db30 | -15.20957 | -47.96069 | 2025-10-24 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9614afb-aef3-3412-bdce-80d534f00854 | -17.31271 | -43.60135 | 2025-10-24 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 331607c7-043d-355e-b05d-ecdfbf84d9a9 | -7.54903 | -47.3611 | 2025-10-24 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96d6371a-ed4a-3004-9ddb-43854537524b | -14.92355 | -43.44544 | 2025-10-24 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 819741b5-4e50-3fdc-8ae5-768e72feb9a7 | -13.90161 | -48.385 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4ee1ca0-159a-3a31-b08b-5b8fd3616162 | -7.25074 | -43.97602 | 2025-10-24 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94cc8154-4eef-3c64-826c-50db75e82803 | -15.57325 | -47.71487 | 2025-10-24 04:19:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6d08e75-ffea-3aa4-b56e-63198853d8a1 | -7.00303 | -45.2095 | 2025-10-24 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e73e9bc-e920-3bca-b93c-c458f8a056fc | -17.6015 | -46.62417 | 2025-10-24 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8251187d-02db-3b23-8745-11cf5fa40323 | -13.02717 | -47.23526 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2f5da13-ddd9-340d-a6da-b0f5c7ac715e | -8.20291 | -46.98119 | 2025-10-24 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c416dde6-747d-3c98-bb1a-d4307588f706 | -12.72809 | -46.94856 | 2025-10-24 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca7d9e4d-6151-3d82-8e7a-cf58a21c8950 | -7.27076 | -50.00608 | 2025-10-24 04:19:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff15f286-3e75-3315-8637-b3614c67a3e6 | -15.83616 | -49.08658 | 2025-10-24 04:19:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddcab1fd-278a-37fb-ba9f-8f88b2ae9f86 | -18.35315 | -51.70074 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b89900a-2cf8-3ee8-a3c3-c53ec3f489c5 | -19.94022 | -45.75822 | 2025-10-24 04:19:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5745bd6e-0266-3699-92aa-bddae34f71b5 | -14.02642 | -48.00665 | 2025-10-24 04:19:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67a68bb2-cfe4-35ea-b1fa-764932ce2beb | -6.78004 | -45.46458 | 2025-10-24 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe8103ce-35b2-3eb5-95f4-7e320e7710c1 | -14.47346 | -47.90851 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b573902a-9ca3-387d-a7be-a2b1cea66ea3 | -18.36142 | -51.70256 | 2025-10-24 04:19:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcc2f7c9-3437-36c2-98d3-af288db75e74 | -13.28517 | -47.48379 | 2025-10-24 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c648db0-14ac-3e20-b045-012a0bcf1184 | -7.29282 | -46.27718 | 2025-10-24 04:19:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b9b4f279-88a6-309c-8d3f-d9d55ede4738 | -13.26108 | -47.88866 | 2025-10-24 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bf5354e-de82-3731-af36-c63266ac5ac4 | -19.98636 | -44.22138 | 2025-10-24 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77bf5b1a-7369-3cee-872e-28c7b2617e7b | -7.61947 | -41.84811 | 2025-10-24 04:19:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b784bce-8feb-357d-9337-9a0929e48ad7 | -7.62319 | -42.20756 | 2025-10-24 04:19:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 147cd517-a48f-3da7-bff6-2a3b45045a2a | -19.64763 | -43.63295 | 2025-10-24 04:19:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e4543de0-fb6b-37a1-8307-b9d7f1fe4c51 | -14.26817 | -48.07766 | 2025-10-24 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82babfd2-0a69-3a91-b87a-e1b42ffca702 | -14.43527 | -50.95111 | 2025-10-24 04:19:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7194f338-07d4-3a51-a2da-44fa15c44779 | -15.4979 | -50.44739 | 2025-10-24 04:19:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README31.md)
