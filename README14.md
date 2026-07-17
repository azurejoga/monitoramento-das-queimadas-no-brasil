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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a1c7e82-ff9d-30b5-a7a8-810758c3b81a | -9.45201 | -64.03898 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d4809979-fd31-3ea3-990e-677b9fef1a1b | -11.78358 | -47.09055 | 2026-07-17 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40926c24-835e-3cb3-898a-d02cca1cff37 | -12.50314 | -46.34782 | 2026-07-17 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95f69837-818e-3c07-83d8-e85623f154d3 | -9.45195 | -64.03931 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bf0055ff-cd02-3a55-ac20-5af96fec7263 | -10.81594 | -45.13522 | 2026-07-17 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2cffc171-b1ef-33cf-be20-93dd29160c2f | -14.88643 | -48.47203 | 2026-07-17 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5a2ee96-a762-34fd-bd51-1df0bb293b36 | -11.7676 | -49.07868 | 2026-07-17 04:57:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddfe24bf-c3a1-3e73-a755-c56276dbf512 | -9.45774 | -64.04039 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 341190ee-fd74-3f56-ac01-81e13a4f1925 | -13.44141 | -43.86241 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a2deedc2-1ce7-3fe9-9559-d6f6f94aa212 | -13.44242 | -43.85382 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6fc90214-6346-3a29-89fc-324d126f9d27 | -13.43519 | -43.86541 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3221f70e-3a6f-320f-ad19-f1fda1cc3630 | -9.91029 | -53.36852 | 2026-07-17 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33fd51fb-e97d-3e96-9b21-3f881e584a53 | -12.11764 | -49.93787 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5699bdff-c7a5-3638-8566-44f37dfd725c | -13.24749 | -45.11488 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 9851a355-a8d7-3d78-a60b-8f58e19e8ceb | -12.68389 | -48.21061 | 2026-07-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcb7b7f2-9331-3b80-85fc-dcd34ecb6c92 | -13.25399 | -45.10564 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| bad0d305-ca0e-37ae-bbff-ec84fd242a5f | -10.81673 | -45.12916 | 2026-07-17 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aacf5c4e-b284-3553-8c07-4786ece21dd6 | -9.45689 | -64.04498 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72836b71-5fa5-30f8-a833-74e90496c664 | -10.82032 | -47.37724 | 2026-07-17 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b4d5bd7-e6f0-3641-bc3e-faf26213d0a5 | -13.43668 | -43.85273 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29c94867-9aa2-3e0c-a0ce-841a2f939712 | -10.04344 | -51.66314 | 2026-07-17 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 874a3b94-624e-318d-9303-a4a95f7766f2 | -13.55111 | -47.79168 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8aa49ef0-679a-3d6d-a969-ce5978822a9b | -13.51894 | -47.79543 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fe67506-14cb-376b-bf57-923d5cf32844 | -13.55053 | -47.79615 | 2026-07-17 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ccea5d2-a1d6-37a5-b230-0b61fc8bf483 | -11.40438 | -47.5325 | 2026-07-17 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eecdcd1-d4cb-35dd-8224-9d6d5aa00085 | -12.69623 | -46.51064 | 2026-07-17 04:57:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0d6d8787-ec5b-30e0-91d7-67da12f0465a | -12.43807 | -49.57426 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e605031a-9899-30ea-b47f-e0e4ae939c8a | -12.66406 | -48.22847 | 2026-07-17 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d03a5681-507d-3cc2-a890-561031ae9d67 | -10.8349 | -46.57634 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5a6cef87-4167-3c79-bec7-fead36e04c7d | -11.18556 | -49.89498 | 2026-07-17 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c0a533e-b567-315c-9a4e-26090d11ced2 | -13.43715 | -43.84864 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1f8b4ce-d12c-3836-a086-9e021b287300 | -11.64409 | -48.50348 | 2026-07-17 04:57:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2594f9d6-6313-3294-aa86-97ee71967c09 | -12.19771 | -46.4861 | 2026-07-17 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 808c7dfe-240d-315a-b605-4d4eec680210 | -11.78814 | -47.09113 | 2026-07-17 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c844334-bcd4-3cef-b037-05dd7e0164c7 | -12.45225 | -49.58667 | 2026-07-17 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42378d9c-c48a-3e64-8624-73c22a4b63fa | -11.40505 | -47.5277 | 2026-07-17 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 042914b2-5d62-3d43-8274-6c1a02e8b6da | -13.28053 | -45.19725 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84eda55c-769e-3ce4-b131-936183309b6b | -10.83555 | -46.57146 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 74ef24c7-0ebe-353c-9f71-fa4ad8e6b875 | -12.41354 | -58.40329 | 2026-07-17 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa131bab-62da-3f7b-a050-07c42ab9af40 | -13.25359 | -45.10898 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| b4ba276a-a1db-3366-bd6a-c03461846624 | -15.37885 | -59.54097 | 2026-07-17 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c1eeef7-f598-31f8-9672-d7d1767a2c26 | -10.82145 | -45.13305 | 2026-07-17 04:57:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2f0aaee0-f3e6-3ec8-abad-6a2ca706a815 | -10.84087 | -46.56715 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f263d84-f6d4-3dc6-bafa-a63575aeaa3e | -10.82285 | -46.52443 | 2026-07-17 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf2684cf-13b3-392b-86af-b5ea32034e3b | -13.25319 | -45.1123 | 2026-07-17 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 74ad034f-0c02-3b29-976e-60b98e6dbd8b | -13.43619 | -43.85686 | 2026-07-17 04:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0cc71ae0-6bf7-36bc-936b-5f4fef8c5c92 | -9.45863 | -64.03577 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da9766b3-5637-35d3-a307-cd09f32151af | -12.4522 | -46.51387 | 2026-07-17 04:57:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55e32542-5616-3fa6-8a91-a369a3310c4c | -9.4594 | -64.03179 | 2026-07-17 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5915d29e-17e1-3265-9a85-5c9e8adf424c | -19.83174 | -57.97456 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a0762638-d728-3c4c-8ea5-73f4aa9e186f | -21.66147 | -56.32532 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a6a7041-be6c-3329-8fb9-5326f2f3ac77 | -19.82146 | -57.9726 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9102ce6d-e5bd-362e-a5c3-049d88c6b721 | -19.83779 | -57.93918 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c20efd6d-5faf-361e-9771-074cddfbf506 | -19.85778 | -57.98765 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7f0ed10a-54bf-3e78-8529-31770f6209da | -21.76705 | -56.30233 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a565c080-f8c8-34ab-b52d-7c806a3d55a6 | -19.82214 | -57.96867 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 1097c845-4d49-31bc-a3f2-237b6a95aca7 | -22.46908 | -43.1012 | 2026-07-17 04:59:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f8413d1a-fb5a-30b3-afa9-72d301e57eb5 | -19.81732 | -57.95557 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dc39e22d-ea0e-3eba-9350-099f0dc2e864 | -19.83095 | -57.93789 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 199d8c29-a6de-336e-a1d3-33b8090cc42c | -22.97771 | -48.92147 | 2026-07-17 04:59:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea22ba2f-9171-3049-b083-7c98c382f203 | -19.81845 | -57.95269 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fa5cd4eb-0431-3014-baf4-2a275869c2a4 | -21.76978 | -56.30664 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8664d03-49cc-3506-a307-1bb5e9e4d5aa | -21.76316 | -56.30544 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f74e6214-6b4e-3e8e-8758-1942eb9cf1ce | -18.95746 | -49.57217 | 2026-07-17 04:59:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f07a4ac-caa3-3198-8269-c7809db12035 | -22.24398 | -56.05375 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89ca3c9c-5413-3b5a-bd70-b9f302713aae | -18.55693 | -56.81703 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7ed024a9-b2b0-371b-97e8-f4c2e7f7d8f4 | -23.14052 | -48.66924 | 2026-07-17 04:59:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dd5f62c-763d-3f48-9890-6bbc16f39042 | -19.86805 | -57.98961 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 065fc6df-4936-38db-8408-7f35aa6f89ea | -19.13871 | -51.73801 | 2026-07-17 04:59:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8127b51-208a-3c39-bcdf-03d39735c294 | -19.81977 | -57.94482 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b368a084-59c7-36ed-a175-f7ae68e1ed06 | -22.24667 | -52.87214 | 2026-07-17 04:59:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6be1409a-d763-33d8-bf85-b47c4a4c788a | -19.1374 | -51.74003 | 2026-07-17 04:59:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 477d745e-f5e7-39a9-bb85-108a0431aa38 | -21.76647 | -56.30604 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 713b059c-a22e-3d81-9b7f-8fd36d92bd23 | -19.17793 | -47.35439 | 2026-07-17 04:59:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fbb54511-2398-3276-adda-7ba24683ca90 | -19.86463 | -57.98896 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 9818fe04-e8fe-38fb-97ab-bceb604d2dc5 | -23.19985 | -48.25565 | 2026-07-17 04:59:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 53c41823-d596-385d-9db9-d9cba181f3bf | -19.82489 | -57.97326 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a93518ff-28de-302e-a741-bc143396f058 | -21.77036 | -56.30294 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33d4f355-5da0-3a9b-96e2-3e914456d206 | -22.91867 | -49.20398 | 2026-07-17 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f751897b-e480-3fc2-912e-f424577d1487 | -21.76374 | -56.30174 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0e23672-0701-33d7-a569-d3cb8b5b5468 | -22.23792 | -56.04885 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 879239c9-0539-3f69-a058-fd9acddbafaa | -19.84476 | -57.98111 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a0cd144f-c7ee-3445-a176-20e0f80252e8 | -23.13633 | -48.66322 | 2026-07-17 04:59:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7813c77a-e91f-34da-b072-df59d4d3b78a | -22.25308 | -56.01708 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8581a6f6-8ee7-37a0-8a54-6cca196387d8 | -21.77095 | -56.29923 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e26ea5b-9429-3b02-819d-2f1c65ab2ba8 | -19.83028 | -57.94181 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ce9cd15e-5bbc-33ea-a618-851836dff90d | -18.5542 | -56.8127 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ec1b6912-5884-3a36-ae60-225fdef8c52b | -22.46943 | -43.09657 | 2026-07-17 04:59:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| cd7af357-e93c-37c1-8b0c-416b7040cceb | -19.83449 | -57.97915 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cb2616df-a95e-36b1-9920-e8ceb628ebf6 | -22.23996 | -52.86639 | 2026-07-17 04:59:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8feb4483-5576-3e6d-8d01-fea8a4db99b2 | -22.22235 | -55.97332 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 240e22b1-a5f8-3b6c-8be4-9a2076d3d4d0 | -22.4698 | -43.09166 | 2026-07-17 04:59:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 03816350-a888-3eb5-88ca-bd63d0018163 | -18.81244 | -47.55642 | 2026-07-17 04:59:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9c52cef-0de6-39ac-b07d-b01676fa428b | -19.85435 | -57.987 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| f7f557d3-e250-38a8-b6b3-f4a15a0efd4c | -22.24301 | -52.87159 | 2026-07-17 04:59:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 842c2a8b-52ca-30ff-b7c9-13ff1ed602df | -22.21928 | -56.103 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30133c5f-42dd-33ed-88d0-aa4bce91acd0 | -19.84751 | -57.9857 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e3f05f71-b008-32a1-914e-cbccfafd06fc | -16.17425 | -59.1543 | 2026-07-17 04:59:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7f1f462-5794-3ffa-adef-7f0faa3eb332 | -20.33469 | -46.63602 | 2026-07-17 04:59:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19871a9f-2ba5-3e15-a52b-c2e3960d9736 | -19.84133 | -57.98045 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |


[Clique aqui para ver as próximas entradas](README15.md)
