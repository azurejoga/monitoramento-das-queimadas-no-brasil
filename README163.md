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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| add6d274-06c5-3d02-9b06-db12fd023ad9 | -6.4279 | -43.4686 | 2026-10-05 18:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 4a77d508-6cc9-3b93-be76-660a5bfdd7ae | -4.8081 | -42.1577 | 2026-10-05 18:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| d129a9d6-c950-3785-bcc4-64f6c6e9d6d1 | -7.364 | -72.6079 | 2026-10-05 18:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8ec7f523-7f22-3f80-b080-003b6d879916 | -7.997 | -42.9175 | 2026-10-05 18:20:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 1c67de1b-9fa7-3753-9059-0d4a2a57fd3b | -8.593 | -66.8081 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 221.6 |
| f03078a0-e899-3297-9a66-e9f49b114517 | -8.5929 | -66.8266 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.9 |
| c6862d45-d7ba-3251-88d4-7db077486296 | -9.0988 | -65.3596 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 8c57b1d4-6927-344a-b31d-8637a83d6786 | -9.7126 | -65.0951 | 2026-10-05 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.1 |
| be1bb406-f518-3ea5-a088-7e1cd3aeaa4e | -9.1168 | -65.4711 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4e38afa1-c3ec-3070-86d1-f375b2a5055b | -5.9606 | -41.3507 | 2026-10-05 18:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 468.9 |
| f8735c23-e4b3-3f58-842c-c8c2409f2d04 | -9.363 | -68.8619 | 2026-10-05 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 67.4 |
| effaf4e2-a7d8-384b-a34b-99079aa1f967 | -9.1243 | -68.2206 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 3aa2de92-211d-30e6-80b8-d75b5870b3a4 | -9.393 | -65.8918 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| e96c20fb-8cab-3500-80db-f0afbc3a9564 | -1.21179 | -46.41068 | 2026-10-05 18:21:00 | AQUA_M-T | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 93a50a45-bc9c-3872-8d87-5bb848434936 | -7.842 | -72.4589 | 2026-10-05 18:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 21c25695-7b25-36fb-9aa0-c3da000627f3 | -9.4819 | -66.7836 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e1cbedb2-a38d-34ef-a605-028c5c80a944 | -8.8705 | -66.7822 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 72b5c5d1-a0df-3cfa-899c-f489b7df60ad | -4.8083 | -42.134 | 2026-10-05 18:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 205.8 |
| 7880aa58-50c1-3922-8515-148a2fcf4e89 | -12.8181 | -43.3047 | 2026-10-05 18:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 03576b62-9193-30e7-a017-2ad3271c43ca | -9.4751 | -64.3336 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 8ef1b48b-6bb1-3283-8cb9-5ec83be4208c | -9.3631 | -68.8434 | 2026-10-05 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 36b12182-73ee-3062-a251-90ca6d18bff2 | -9.0584 | -66.1073 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| a9f09294-6482-3468-bc98-2f2ceaa92847 | -8.537 | -66.9764 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| a7b38a7e-7e80-3cbb-9ffe-f8e45286983d | -9.4565 | -64.3344 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 96.3 |
| dbdf222a-2247-3628-aae9-c2089f03c96b | -9.1222 | -64.3843 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 3f8a5f56-9f51-30b5-bc91-540390981ed3 | -5.9417 | -41.3524 | 2026-10-05 18:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 204.6 |
| 7212e28d-0351-3c5d-9de6-75c5f3a95415 | -9.1072 | -67.8141 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 163.7 |
| bb3ab24e-8d0d-3acf-a1a6-f1bf9f74fc07 | -9.1076 | -67.703 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 123.7 |
| cd72d765-e585-3ca1-8934-c1a7c2cb999e | -8.7521 | -68.985 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2501dfdc-49b8-37b1-b1da-fb3a98432d62 | -9.2251 | -66.1209 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 0a4d56b3-b86a-32b5-8d42-bdfd68329148 | -9.1613 | -68.2568 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| b35371d4-9aff-3989-8a29-f99553ffed7a | -2.5353 | -65.8819 | 2026-10-05 18:30:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 113.7 |
| effd58e3-f984-30d4-a667-cc43956eae73 | -10.9536 | -60.9102 | 2026-10-05 18:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 7280cb72-0079-340b-8f9d-3a340a8be77a | -8.3526 | -62.8302 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 1e7d8435-eabc-3a53-bd71-e92aa23e041b | -8.5929 | -66.8266 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 8d67dc40-e8dd-300b-b960-cb8bb4c6e1f7 | -3.292 | -42.2673 | 2026-10-05 18:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 801a9a1e-0610-3df8-8a3a-411a334d1a2c | -9.3629 | -68.8988 | 2026-10-05 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 88.3 |
| f1a602f8-1222-3346-ad27-1f25b145256a | -9.0046 | -65.6988 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 05d1953f-e634-3835-a580-94dd9220e472 | -9.1427 | -68.2757 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1e9d9147-696b-3351-a92b-516dda935f8c | -9.077 | -66.0881 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 5334e703-e00e-3b1d-bf3f-ac6513204fef | -9.0982 | -65.4904 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 8d98b798-bed9-399d-ab81-df1ce1056c83 | -9.0769 | -66.1068 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 907c3673-96e4-3b05-8707-824697173ecf | -9.1535 | -65.5634 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| affcb02e-ab9f-3855-978c-6fc68153916d | -9.4783 | -67.6752 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| cf1e608e-ef67-3b25-8793-e32ae7114e0a | -8.8895 | -66.6516 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0469d890-032c-3f1e-bb14-fca975a0b820 | -9.0585 | -66.0887 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d9b1873a-a7d1-3c74-838d-6757a16c4014 | -8.871 | -66.6521 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e2d0bd63-50a5-3b69-9d25-f344b14b8b82 | -9.1244 | -68.2021 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 336899dc-c9c8-344e-ba7e-9d5d92db9080 | -7.4889 | -42.8059 | 2026-10-05 18:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 960dac8b-f9e8-3309-9e76-c0392e0a773f | -9.0286 | -69.2559 | 2026-10-05 18:30:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0786852a-cee3-33a5-a938-5dce883571a4 | -10.6087 | -68.6852 | 2026-10-05 18:30:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ebaeb022-fbb0-3fc0-990a-dbd9b61054c8 | -8.5183 | -67.0139 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9f700a37-caea-3c32-89ad-0542aafa076e | -9.1427 | -68.2572 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 0f867deb-79a5-3c4d-8dbe-f667ddcde13e | -9.2934 | -67.5501 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b5697fbe-fefc-332a-9959-7fb8970ce6a1 | -9.7312 | -65.0944 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 18b7c84a-6827-32ea-bac9-dde2bb0a4b17 | -8.852 | -66.7827 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 1085d41c-a3ed-3eab-930e-568f2a22022d | -9.1257 | -67.8137 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 45e23b46-0730-346b-ba09-d1311ba3849a | -9.3431 | -64.7143 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| d9c10f67-00b0-308e-a9a5-bf0a76d5daf9 | -9.4958 | -63.9562 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| e5b28305-12e8-3009-815c-cb931d7f3b8b | -9.9175 | -65.0313 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| ce3d1c6b-faad-3e4b-aae4-caf201361ffd | -8.882 | -68.8166 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 148abd91-f563-3daa-8f19-c0bfa6bfebbd | -8.3341 | -62.8309 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 51b92449-2b7d-310f-91bc-7b6d73b40398 | -8.8519 | -66.8012 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 23212f0e-4c83-357b-a62e-95e35141b196 | -9.3816 | -68.8615 | 2026-10-05 18:30:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 55b2f898-9a8d-39cc-83f5-511d9947eb15 | -9.393 | -65.8918 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 8a1221c7-3b95-3762-a7f1-4b80f537129c | -9.4772 | -63.9569 | 2026-10-05 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 8b2d7eed-8ee1-3497-8cf4-1e998e415d1d | -9.2935 | -67.5316 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6266cdf3-bfbf-38e6-b231-2ccd82d6970b | -8.6493 | -66.5839 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| df85e48b-fdbc-3991-af05-fce81363a0c4 | -7.3272 | -72.6446 | 2026-10-05 18:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 050dfb6d-3699-3950-8f79-70d9003ce028 | -9.1259 | -67.7581 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a3b6ab57-ab56-3d42-bdc8-7aaae56f67a1 | -2.5353 | -65.8635 | 2026-10-05 18:30:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| ba3bb7d6-384b-33c9-b3b7-f68a6bc3b1fe | -8.593 | -66.8081 | 2026-10-05 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 193.5 |
| a831ad27-655c-3668-9337-7b047f313263 | -9.1075 | -67.7401 | 2026-10-05 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e049e6c8-364d-3ecf-ab4f-65cc9952ae44 | -5.9606 | -41.3507 | 2026-10-05 18:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 376.9 |
| 9d904bb6-731a-3148-858f-bb268e536d5b | -9.1438 | -67.9428 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 075f4357-f2dc-3937-8a15-dfded10539a1 | -8.5183 | -67.0139 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 0a08afcc-fba6-308f-826e-e4ade7d2a60c | -8.9239 | -67.3372 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1686df10-dace-307d-b87d-6bad04c55b90 | -8.7521 | -68.985 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 76ece7f2-e44b-3bfb-aa18-537214b620e7 | -7.4889 | -42.8059 | 2026-10-05 18:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 52f0cc41-ded5-3a07-a616-7e05fd87a40d | -9.1076 | -67.703 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| a44ff30c-5cc5-3291-8352-04fefe098bd6 | -9.4751 | -64.3336 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.4 |
| f86d1286-af6b-3fd1-875a-4fe25a70914e | -9.0982 | -65.4904 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 8a8e2b07-9886-3004-ae61-29248c965fe5 | -2.5353 | -65.8819 | 2026-10-05 18:40:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 0cd9298a-aefa-3dc7-9fdf-7e9dcefbcf25 | -7.8968 | -72.8778 | 2026-10-05 18:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 54.1 |
| eb45d250-7e26-39ea-bedd-4bdc6b98d647 | -9.1613 | -68.2568 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 7257d9dd-2b11-302f-a978-ba739591ebad | -6.6147 | -41.797 | 2026-10-05 18:40:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| c9090fee-2eea-346e-8271-76ddf3a54c50 | -8.882 | -68.8166 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 3ff346a6-80aa-30dd-965f-64c3248152c4 | -9.1259 | -67.7581 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9aa3f066-4ea5-37b6-bd93-66165723dcd2 | -9.7499 | -65.075 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 114e178c-f8b7-3b2a-8535-7caf7a427930 | -8.6493 | -66.5839 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 159effe4-8d3d-3c6d-b08a-d8e7b15d8f5a | -9.6672 | -66.834 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| e504dd54-2112-3929-85ef-00d420d8bf71 | -8.6214 | -69.5026 | 2026-10-05 18:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 91d4995a-e32a-3593-8c0a-4af02105780a | -9.7313 | -65.0757 | 2026-10-05 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 81f4f95e-0e5e-329b-a025-21e35b200055 | -8.537 | -66.9764 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| f32edfee-c6d1-3489-b2ca-eba2a4c3c7b7 | -8.5368 | -67.0135 | 2026-10-05 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5328208c-59ec-3f41-87d0-0fe05d58541a | -9.1257 | -67.8137 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| fd2dc8dc-0734-3b5f-8394-33c87ef94779 | -8.2674 | -71.1215 | 2026-10-05 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c088fa3e-8c10-37ea-8211-c920ba813298 | -5.9606 | -41.3507 | 2026-10-05 18:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 354.9 |
| a5639ba0-b950-3611-8633-7c56881b1499 | -9.1427 | -68.2572 | 2026-10-05 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 0f3a3ae1-8547-3a61-a70a-53f2b9a641f6 | -4.8083 | -42.134 | 2026-10-05 18:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 157.0 |


[Clique aqui para ver as próximas entradas](README164.md)
