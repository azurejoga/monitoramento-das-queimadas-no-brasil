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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90eb0254-e6b0-3160-976c-1a331ed5e5cd | -18.04826 | -57.32423 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1725bc8d-9c16-39d1-b9b8-d11f03c3dc83 | -18.04785 | -57.30541 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b904319f-d1ab-31e5-837b-9089561f35cd | -18.04177 | -57.3006 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1727deec-161e-354d-86cf-5b899ebe0a7c | -18.04118 | -57.30425 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 200259d7-c60e-3073-a413-37250809b207 | -18.04024 | -57.35283 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0a28dafd-db9e-365b-bfc7-9a012db837c4 | -18.03925 | -57.33765 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 20f99bb7-dea6-38ce-95b4-262683f26ed6 | -18.03867 | -57.3413 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5911a387-bcf3-3e5a-9b58-2d702f3f1f12 | -18.03808 | -57.34495 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c48d8e78-c2be-3194-858a-4aaccecff727 | -18.03785 | -57.30366 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ab052d32-e18d-3665-a370-e1fb47e371cc | -18.03691 | -57.35225 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0a148c9e-9366-38be-9fe0-054a9e22a19b | -18.03592 | -57.33707 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fc2ed1ce-0c70-32e9-933d-d553095522eb | -18.03534 | -57.34072 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b321d527-44e0-314c-a2b0-237870250f26 | -18.03393 | -57.30673 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ea2abf33-f2ae-396a-8edc-fa68ebbcd6e0 | -19.02324 | -57.62053 | 2024-10-24 04:59:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fe6a26a4-d8b6-35bc-9acf-2bb6046a43a7 | -18.66894 | -57.35626 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 94e65a97-3ee0-3753-bb4c-656d2ad2e799 | -18.6662 | -57.35203 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| db09e485-2655-3bc7-be74-759d94a51a65 | -18.66561 | -57.35568 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fe6e7a62-0527-3912-a63f-d473785847a3 | -18.66345 | -57.34779 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a98328c6-a33f-3a6d-96e8-e5e0d4614462 | -18.66286 | -57.35144 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ef852bfc-ce87-3d23-8baa-8bc0d1bd5df0 | -18.66228 | -57.35509 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d3464b4c-6755-3568-ac5d-30a7e0105268 | -18.66012 | -57.3472 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3e1e9beb-dfbf-39a8-aa40-0a6aa9f3aaed | -18.65682 | -57.33141 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f72ca3b-e388-3668-b122-e1e181d67580 | -18.65679 | -57.34661 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| aa0e799b-e0d2-3ef3-a8ab-a52d65abc3f2 | -18.6535 | -57.33083 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 24783e39-896b-338d-a0da-506940ef1c30 | -18.65233 | -57.33813 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| eca34176-3ab2-3b2f-a76c-e4528cd5c3ec | -18.649 | -57.33755 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 087aa64b-d52f-3141-983f-f1d7b5762bfd | -18.11608 | -57.32861 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 54825252-449a-3751-bb98-52c3179724c0 | -18.11549 | -57.33225 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 77d010c6-6377-319c-844e-5b30c7664b79 | -16.20671 | -59.1646 | 2024-10-24 04:59:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a8e558c5-e3f0-3298-8f65-acacb57ca43b | -14.92245 | -59.88176 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e31b5eb-642b-35b1-8f5c-dab57355f722 | -14.88177 | -60.07008 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f972ff3-83d6-365d-a817-329adc677b1a | -14.87479 | -59.86529 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c914fbad-4460-37ba-a5fc-f24d78021b77 | -14.8711 | -59.8675 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 031aa54f-0ccc-3c22-a029-11e10ea120d7 | -14.87029 | -59.86916 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8dc2cdf-e2e9-3461-9b59-55e88e5e9ee7 | -14.86737 | -59.86681 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e47f56c-328e-3ac1-ab17-e3177fd5d08b | -14.86656 | -59.86846 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 344d82af-739f-3ba0-8d8e-85e9989d8788 | -14.56217 | -59.99405 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f181a49-cf62-3a36-a0d0-e32edae1752e | -14.56134 | -59.99873 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f62a82c-f80d-3238-9722-b3b097ab1b11 | -14.54162 | -59.9563 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 335a5668-ebd6-32cd-92fc-6c5d08c43809 | -16.08759 | -60.13155 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04422bae-2f77-3982-8cbb-3eadff44583a | -15.92016 | -59.6301 | 2024-10-24 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 894bb20f-c935-330b-80c2-19ae080000aa | -15.91653 | -59.62942 | 2024-10-24 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8269ed19-77ef-3cc9-86c9-bb1564679bf7 | -15.80278 | -59.55112 | 2024-10-24 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cb6a652-92c7-3052-a58c-43c0fc19b33c | -15.67087 | -59.75014 | 2024-10-24 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| feb0c224-555a-3722-b709-ac08e5a54052 | -15.67009 | -59.75457 | 2024-10-24 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aaf9292c-3736-31f4-a125-d5281449861c | -15.66931 | -59.75901 | 2024-10-24 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ea2caf-156b-37b8-8187-e3b26587048f | -15.28887 | -60.40159 | 2024-10-24 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23aeec88-c5d8-3f40-8137-6224bf7e07ad | -16.00824 | -43.39264 | 2024-10-24 04:59:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 22c993a9-8e5a-3ffd-bef5-adf7e1d71ace | -16.00766 | -43.39854 | 2024-10-24 04:59:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44a8275b-e97e-3e16-b320-a7123ae23d6a | -21.14675 | -53.63339 | 2024-10-24 05:01:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3525755-8aa4-361b-9066-1a6acc33b9af | -20.52197 | -55.35512 | 2024-10-24 05:01:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7c34265-466d-3088-96a8-15210ee5f011 | -20.3881 | -54.86037 | 2024-10-24 05:01:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12b1b992-285b-3bd5-ac56-a20dea217f9a | -20.26442 | -55.42365 | 2024-10-24 05:01:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48266c8b-e97c-3579-8396-51ccd9f11d9a | -21.90173 | -56.10689 | 2024-10-24 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1e086c6-bb18-3e9c-beb2-82b6706054e1 | -23.83094 | -55.29045 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| eb79e998-9d7a-37fa-841e-5ac62b7adf46 | -23.83035 | -55.29482 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| dec26635-d02c-3311-9dd3-42a7e11e5f84 | -23.82738 | -55.28989 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ac19988b-7fd9-3470-b852-0e6158991b1b | -23.82679 | -55.29427 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 6edfac5d-f07f-3693-af15-e99c17535a29 | -23.82587 | -55.28741 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7b141cea-c8bb-34d7-8037-c7f321e4903d | -23.82526 | -55.29178 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e279a77a-1c2c-319d-bb09-bc8f79e9a711 | -23.82382 | -55.28934 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3a8ac06c-2093-3a2c-ae81-e4f45da08fdf | -23.82292 | -55.28247 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bd2a0076-f1fe-361a-929b-18019b891336 | -23.82231 | -55.28686 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5de16a4a-449c-3a10-9ca4-161550a99f33 | -23.82144 | -55.28 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8aed5831-0ae1-328e-8202-07edb14baaff | -23.82084 | -55.2844 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8bd4ecd4-2e14-3609-8290-dc3c33e19c66 | -23.81936 | -55.28191 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04848a4b-6814-329f-9c73-402f91c6017b | -23.79679 | -55.28708 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4c557277-f68e-3cd2-8606-78482af01a0b | -23.79505 | -55.27343 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c30d3918-2d7a-3f61-921a-45d851e361d6 | -23.79324 | -55.28648 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7bb72cf8-c11d-3a10-b430-46888735fa68 | -23.79209 | -55.26853 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| bf13c558-72a3-321d-9e57-f01965deb62c | -23.79149 | -55.27287 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| a644966e-65b9-3996-90e3-9b6b944d3ae9 | -23.79089 | -55.27722 | 2024-10-24 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b6a9e3b9-63df-302b-910c-de725f81ca8e | -23.26583 | -55.20524 | 2024-10-24 05:01:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 997f5d99-2278-36f6-9ec0-fd71d178d81d | -23.26227 | -55.20468 | 2024-10-24 05:01:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 97d8fb63-1baa-37a8-a3cb-05535675b97d | -23.26167 | -55.20899 | 2024-10-24 05:01:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4d2ab7ac-92ed-3c80-8872-7a66d30e7ab4 | -22.18895 | -56.91663 | 2024-10-24 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d8a9281-2f67-33ae-b837-321cd31cc7ea | -22.13863 | -56.57647 | 2024-10-24 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16bdde92-589f-397c-8b62-1e992ee5f58b | -1.5878 | -53.3089 | 2024-10-24 05:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 89133673-4d3e-33d6-8f78-978b79c2565b | -2.9763 | -50.4193 | 2024-10-24 05:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| b2ba2264-469b-3496-8a9e-5dcb5d8621f0 | -3.1607 | -50.4556 | 2024-10-24 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 43234490-07fa-3ec5-ae34-f95ba2214851 | -3.9396 | -46.4229 | 2024-10-24 05:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 65f42335-4c6f-3ef9-8e5d-e207755ecfe0 | -1.5878 | -53.3089 | 2024-10-24 05:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 37020bd5-092b-38aa-accc-d5f0f318157a | -2.9763 | -50.4193 | 2024-10-24 05:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 7e2848e8-5845-38ef-871c-e4f9c76d9937 | -3.1607 | -50.4556 | 2024-10-24 05:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 268a7292-0d14-361e-bae6-fffb52b16bcf | -3.9396 | -46.4229 | 2024-10-24 05:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 84453d4b-e72d-3e98-af08-0f367855dda3 | 2.63694 | -50.88271 | 2024-10-24 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc7507de-dcb8-387c-833d-4a2ef9031ddb | 2.63314 | -50.88504 | 2024-10-24 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a88aa2ab-7e58-325b-9159-9ca574dce1b8 | 2.6323 | -50.87978 | 2024-10-24 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44fc9a63-4d46-3ed6-87a8-d721d1eca5c1 | 2.63213 | -50.88347 | 2024-10-24 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67a4fad5-9378-3a2f-b1b5-37b8a126846c | 3.48185 | -51.26045 | 2024-10-24 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38cf8cbe-f068-3c0d-8b95-7a9a8f8cebe3 | 3.47883 | -51.2708 | 2024-10-24 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74b26eee-f6d7-3917-8d71-d736b97b006e | 3.47803 | -51.266 | 2024-10-24 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f89570b-f15c-395d-80ad-28dfceb3ac2e | 2.80372 | -50.93885 | 2024-10-24 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0607cb5f-cdf7-3b45-ba13-e91963712749 | 4.83048 | -60.1432 | 2024-10-24 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fbb1bed-35bc-3b63-af92-55ececca1909 | 4.82707 | -60.1439 | 2024-10-24 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4673a4ee-c3de-34ad-8294-bd60820fd028 | 4.82367 | -60.14463 | 2024-10-24 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ef8ff48-d3b5-3e6d-89e8-5b5c91ad6965 | 4.82026 | -60.14536 | 2024-10-24 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c20ff263-2540-3377-8a4d-c6e2d336b578 | 4.81684 | -60.14598 | 2024-10-24 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8af8c56e-c36a-3475-bd79-1de4f9cbc672 | -4.76881 | -46.40433 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dce8ed8d-6bab-31d5-91b4-52faec99a249 | -4.76788 | -46.41116 | 2024-10-24 05:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README93.md)
