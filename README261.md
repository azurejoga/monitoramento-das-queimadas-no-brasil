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

## Dados Diários - Página 261

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41c0c488-085f-3798-a743-53a346567e8f | -8.59484 | -44.86348 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 603de4d5-a1e8-303e-b1bc-6b90e57b4b9c | -11.41021 | -47.56699 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f887aaf1-0c20-3fb8-992c-690fbcc1122f | -13.55164 | -49.15138 | 2026-10-08 16:18:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7f6435d-a7c1-3e8c-b44e-d832d73c5687 | -11.68957 | -43.68788 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6f8632d9-2a37-30a2-85aa-890e7783cc6c | -12.83737 | -44.62762 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 90433a9a-5209-3606-8917-3f68cd1c5630 | -12.22962 | -44.71087 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e6330b3e-1f6d-3725-9d62-9bd0205ea21e | -6.66599 | -35.11764 | 2026-10-08 16:18:00 | NPP-375 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 36a36a81-9de0-31a0-8bd8-1e85f5ba354c | -8.9518 | -45.17515 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.9 |
| d15258eb-a9f4-31f1-af6b-50d127a47b69 | -9.13344 | -45.84073 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 176edd14-6d07-3fba-9929-776bb9a0ffb0 | -9.89863 | -44.85492 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 41e87517-4b1b-3987-959d-8751237d1a0f | -9.73783 | -46.95488 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ccd648f5-d7e0-3d7a-a5c6-485f250af72b | -8.93783 | -45.17239 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 27ef0b32-08a0-3220-8ae4-8eb1b247c519 | -8.63776 | -41.04884 | 2026-10-08 16:18:00 | NPP-375 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 2e10eaee-919d-3044-9ad1-ee64a69b76a5 | -10.44185 | -47.28094 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bbf15a88-a586-3f88-8137-ae3e3f25cf2a | -13.55784 | -49.15081 | 2026-10-08 16:18:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c25b303d-4b8a-32ab-ba22-381293a8b94a | -8.78456 | -47.59466 | 2026-10-08 16:18:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 59d075b2-4d80-359d-a8d8-1831746b52f3 | -11.76684 | -44.94387 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 940c4b85-7afb-3753-accd-81e596a9bdad | -13.12418 | -46.35484 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7bb6be71-6a81-3384-a134-912ddd47bd83 | -11.01455 | -45.43985 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dd6223b2-1c82-3210-b83d-b7e97e08f2d9 | -11.73867 | -43.64213 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| f682392b-9880-33c2-8009-04ae851484f1 | -12.13452 | -43.31517 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 771b015a-2ab0-3eb6-bf70-b4f79d50e99d | -9.88982 | -44.85622 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f8536b10-d43e-3aa9-9db1-5c80a3d33035 | -9.82367 | -45.69006 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c0dd6aee-ec34-32b1-bfdf-d80115bf4978 | -11.40659 | -46.69659 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 920f5717-6e6e-33b9-b24f-c7b67fdfeb03 | -12.28088 | -45.31457 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 09c8aa99-d20c-30eb-8bdc-8e9d8cce613a | -11.18413 | -47.72129 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| aac32794-84ac-388d-af92-98fc380b9b82 | -10.45196 | -47.27655 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 6a4ed694-bc23-35e4-8991-ed895cb89e57 | -8.60108 | -45.63121 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8a6aaddd-7f6b-389e-8bd3-7a412be5a398 | -9.81968 | -45.69568 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 5541c052-a6e0-32d7-b58c-405141c302ab | -10.68449 | -47.83503 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1df7ac7c-edcc-3a3a-bce9-859bb591fce5 | -11.07101 | -44.03471 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| b1abf43b-259a-3678-a581-7a1d0525a0cb | -9.50573 | -46.07281 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b01f477-24d8-36d8-b4e9-dae843106f06 | -9.53125 | -45.61948 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 26851597-d315-3bb8-b9c2-a6cfc43fcf42 | -11.60175 | -43.67237 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 602cf388-1b95-375b-863a-5afb53e43a6d | -13.38589 | -43.47868 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d5ea23aa-1b5f-3f32-af8d-b7e46bf0d00d | -11.30563 | -44.83047 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d0f730ee-9eed-3b30-857f-a83a1cb1416d | -11.92297 | -46.79514 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 214c3828-2d68-3434-9f32-1874a2585564 | -9.70807 | -45.6937 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f78538fc-ec72-3198-8bae-ea750e7e0c8b | -10.6718 | -47.82263 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2da4d2a5-898a-31bd-83df-495fb062a59a | -8.4488 | -46.82718 | 2026-10-08 16:18:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a5546f9-0235-383f-aee1-effa50ef07e3 | -10.76206 | -46.59816 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e8047a66-cbc1-3c21-8be8-14e16e8f510b | -13.95993 | -44.84504 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| e16d3c46-99c1-38a2-921d-1482aac802b6 | -13.43743 | -40.4451 | 2026-10-08 16:18:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| cc975be9-75a0-3f32-9e41-faf650e02bb7 | -10.86771 | -43.64691 | 2026-10-08 16:18:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| e6542391-a479-34e3-a5bb-b40a2e7b6b87 | -11.85326 | -47.38787 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4de949ca-cee2-3ca9-9220-29704a847dd6 | -12.22863 | -44.73918 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 45348e09-4107-3055-a1b8-693b5ef437e0 | -11.31072 | -44.8344 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ac645309-7bff-31da-b2d6-e65e5048d3ea | -8.2549 | -35.67548 | 2026-10-08 16:18:00 | NPP-375 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 18532423-50dc-3556-8ff2-e9fff59c83b6 | -9.36202 | -45.94638 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a92c0051-ca39-3d93-b983-389b6580964b | -11.20644 | -45.21492 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 63bacf41-4664-3b07-99da-15df4593678a | -9.10067 | -45.12614 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 9b73b58a-68a9-3b36-9894-9a0d4ada7081 | -13.71004 | -49.12592 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| afd7777f-4fcc-35da-8d57-ca2f61bfacbf | -11.24867 | -46.27821 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 400d704c-2376-3888-b86f-d6bd0fe29b54 | -11.84652 | -47.3329 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f33b96c6-170b-3848-8e68-e0a8ab4ff079 | -8.96388 | -45.1388 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d5d457cf-0629-3f87-91df-6a2c8ea5e635 | -10.76365 | -46.61004 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 06be616b-5be9-3307-afcc-cba3722b5ff3 | -13.20084 | -47.87575 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8b366fa2-9c07-349c-bc1e-492c1e6bd740 | -13.45476 | -41.92426 | 2026-10-08 16:18:00 | NPP-375 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2513eda0-1d91-3dba-a5cd-ee2046a520f9 | -11.84898 | -43.56905 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 62ea192a-8e77-36c3-8c95-4551919e9fe1 | -8.78802 | -47.26438 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5d6a356a-d3d6-3773-b8d3-bc084d25f723 | -12.71823 | -45.81747 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8eee4067-a11c-3540-9b5e-f7c8f1554593 | -11.21249 | -47.71747 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3741c5af-ebf6-313c-9ad6-9f39f02b45f1 | -9.73156 | -46.94675 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1259748a-f2f9-3401-9177-05501030f44a | -6.79727 | -35.40675 | 2026-10-08 16:18:00 | NPP-375 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9e7ff215-1bea-3e8e-b0e3-8cabed5970f2 | -9.98111 | -39.53226 | 2026-10-08 16:18:00 | NPP-375 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 2bfccf47-1a54-341c-8f73-6e9d67bdaf04 | -8.78185 | -47.37421 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 60c560f2-8dc6-3f75-9201-e79f02e324c3 | -10.76433 | -46.58521 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8202c549-41ce-3e20-aa97-633cbe9551da | -13.11717 | -46.3401 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fae11766-1ace-3ef8-883c-fec375190779 | -8.55371 | -46.92018 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b723fe05-64cb-3fa2-91ff-12fead4a01fb | -12.94753 | -44.87318 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c11e827-2fc1-398c-912b-0f038f3a9dbd | -8.945 | -45.13263 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7ea0cd4d-8fc9-3280-a2cc-28bd838806fc | -8.29311 | -45.72514 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| bd40b52d-dd03-3160-a129-36bcc784116a | -10.3322 | -46.61421 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7ea4a9e9-2b08-3de4-ab6f-4fa759c4f6f6 | -12.19508 | -38.19283 | 2026-10-08 16:18:00 | NPP-375 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d070ac69-c59f-3eac-8382-0bcff558e370 | -8.96448 | -45.14324 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 980f8104-a901-3f8d-a341-78b2e28cfa6d | -8.96261 | -45.15558 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 20aa41f1-6049-37c0-8a2a-9e451eaaf750 | -9.79916 | -47.82119 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c799322-a473-3dad-ae6f-1d62996b856b | -11.40586 | -46.69065 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a1a5ac28-c364-3721-b326-82a33a9d416f | -7.02774 | -35.20926 | 2026-10-08 16:18:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| db506434-494f-3065-ada4-05c86f32cf94 | -9.33528 | -48.34574 | 2026-10-08 16:18:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7444fd2a-28da-34d9-9ed6-6d895db644d8 | -12.19531 | -48.42164 | 2026-10-08 16:18:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2e258db3-177e-3308-be96-a2b0f2a64359 | -11.7599 | -45.49233 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| bc0535ca-f376-33f9-9cf2-bbb33cdd9c23 | -12.22081 | -43.93313 | 2026-10-08 16:18:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3280bba8-f7d3-372a-a2d0-1601975fd0dd | -13.34302 | -43.96929 | 2026-10-08 16:18:00 | NPP-375 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b1a2e861-354e-30f3-be1c-38fdfe3d0256 | -8.55845 | -46.92173 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b846f998-9740-37bc-9370-04af5e16d409 | -10.90159 | -45.53957 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 179f2cfb-95cf-3586-923f-6d1a72a5c01c | -11.73766 | -43.66567 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 404511e4-01af-3c6e-85d0-856538ee3fde | -8.60681 | -47.98787 | 2026-10-08 16:18:00 | NPP-375 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1b0dc7b-c852-37d2-8895-4b09a40269a9 | -12.2236 | -43.93321 | 2026-10-08 16:18:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 2d22b90b-1a8c-38af-adb1-5cf31391388c | -12.55657 | -38.3014 | 2026-10-08 16:18:00 | NPP-375 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d5e8beca-c63c-346f-bb04-bfe6321898a9 | -13.64911 | -47.67399 | 2026-10-08 16:18:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18b91b71-3ace-3984-934c-291f6c7815ac | -10.41578 | -47.28075 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e19e01b-2871-3d54-a739-5f307010b9a9 | -9.08069 | -45.11218 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5d2a7ead-fc47-3974-bdeb-a5d0fbf87c43 | -8.29115 | -45.71141 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| d51f74e0-13ac-3a39-8e16-6f48a04c9542 | -13.19724 | -47.89407 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b5fff389-01e7-3af1-bd74-921c0a4fc745 | -8.69349 | -36.78703 | 2026-10-08 16:18:00 | NPP-375 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 22b41c22-28d7-35a9-9a75-ad849033b899 | -11.80392 | -43.51801 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| dca00706-deaf-35c5-b5f6-5a3f732de94f | -11.74702 | -43.64101 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 4ff9fe14-018c-350b-8251-3ebc4cfb9096 | -11.86146 | -43.55867 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2d909bab-7d43-3b96-b323-5d618ead0a27 | -10.83983 | -48.13319 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |


[Clique aqui para ver as próximas entradas](README262.md)
