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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4ecd52a-1605-3c54-9f5b-01d1e864adc0 | -17.8631 | -57.5201 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| df526411-d794-3d73-bf74-d6661b277771 | -17.8828 | -57.5177 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 68124f29-b790-3df2-a257-a37c6733ef59 | -17.9217 | -57.554 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 9480969a-6f74-395b-82d3-a4bf8e526018 | -17.922 | -57.5334 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 2836c6c3-e7b5-3262-8ee2-2898fc23f033 | -17.9411 | -57.5722 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 7eb6a188-6ef5-38b9-b662-65abfa900577 | -17.9415 | -57.5516 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.4 |
| 1d109142-9243-3b54-970c-47b25e31c81d | -17.9418 | -57.531 | 2024-10-26 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.8 |
| 9f99d601-8d6c-3922-83b9-1f3a96a5bc9e | -18.0629 | -57.3721 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 6640ef70-1607-34b0-b214-8ca55e2ff007 | -18.0653 | -57.2274 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| cb33a8d2-c328-3597-a712-b460317dd795 | -18.0827 | -57.3696 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| 01901105-7ca4-326e-8c73-0a160246ca4e | -18.083 | -57.3489 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 1e421938-9b22-3fa1-b4e0-2dd48af6abbd | -18.0847 | -57.2456 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 84b6e22f-4f52-31f0-90ea-1e94443846f9 | -18.0851 | -57.2249 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 3193fbc0-f409-3551-b0cd-e326583aa7a2 | -18.1025 | -57.3671 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.0 |
| 52ff60dc-ca18-3b88-8ee8-b5b477d99e44 | -18.1028 | -57.3465 | 2024-10-26 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 5ffcb178-fe19-3041-83e2-c4b90cc2ef9a | -18.2649 | -55.9975 | 2024-10-26 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| cddd29c0-0cbe-3940-a9e8-a37d9330f4ad | -2.1929 | -53.7234 | 2024-10-26 02:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d39506c7-3f21-3e0d-a946-5c98cd84ef7f | -2.8923 | -53.3247 | 2024-10-26 02:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| f5bbafa8-5580-3a1a-9762-c35da897d859 | -2.9501 | -52.5708 | 2024-10-26 02:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 133f5040-bf9c-376a-916d-a5e5fc189e58 | -2.9944 | -50.5025 | 2024-10-26 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6c15174a-71a8-3796-b7e4-9911ff8f1f83 | -2.9945 | -50.4816 | 2024-10-26 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| b58c4b39-54fa-392b-84c4-ef32d83a13b0 | -3.0129 | -50.502 | 2024-10-26 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| afcb6398-8ba1-3d75-b476-c5b075b5fd81 | -3.013 | -50.481 | 2024-10-26 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 7ebdd366-6360-3414-907e-405486fc1f6c | -3.4729 | -43.3377 | 2024-10-26 02:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 43acf7d0-9cad-32cd-978a-9ad2a72d80ae | -3.473 | -43.3144 | 2024-10-26 02:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 73d471fc-ea0b-3e3a-b439-49a1c540e504 | -3.4915 | -43.3368 | 2024-10-26 02:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 527e1535-8f30-37ba-9726-9d6c994e8ec3 | -3.4917 | -43.3136 | 2024-10-26 02:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b1318e26-b0f6-3c0c-a2c7-ab194ac32a51 | -3.6084 | -45.8147 | 2024-10-26 02:45:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 95b8b9ba-56f8-36dd-ae0f-c0858567c14b | -4.5613 | -48.0358 | 2024-10-26 02:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| bb6c84c4-0196-3840-936f-6bc5e0b65b2a | -4.5799 | -48.0349 | 2024-10-26 02:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 290.3 |
| 96e55467-fadd-3689-a170-7a18364f74e8 | -4.58 | -48.0132 | 2024-10-26 02:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 185.1 |
| fb87f80a-c76e-3970-92fb-a53a8a68263a | -7.6474 | -63.4584 | 2024-10-26 02:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 59d7cb47-c50e-3bff-b02f-76c2114143bf | -16.9012 | -57.5108 | 2024-10-26 02:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 8d6419e8-dbc5-356f-a084-a9bf4dc28927 | -16.9204 | -57.5291 | 2024-10-26 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| b62a4540-8f25-3807-97cd-666ea0cf53c3 | -16.9207 | -57.5086 | 2024-10-26 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| f2e2bdcb-e59f-3ddd-9708-c31e46618f51 | -17.0499 | -53.452 | 2024-10-26 02:46:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 89bb3c3b-c1b9-3bec-9215-01dcff54e8e7 | -17.2537 | -57.5108 | 2024-10-26 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| e266933a-628d-3db5-925e-37b3b5888b06 | -17.254 | -57.4903 | 2024-10-26 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 3cb1b265-c094-35dd-bb97-3948785debbe | -17.6861 | -57.5004 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 2cccde6e-e1ec-3c26-a743-d260db76fbf0 | -17.6865 | -57.4798 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.6 |
| 5f07688e-bd71-38a3-b9c0-1c29fdac2107 | -17.7446 | -57.5344 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| e4d8e7cf-f8b6-3995-a024-262e32235216 | -17.745 | -57.5138 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| d04a5853-9526-3cc3-8c66-0ef38098fad5 | -17.7644 | -57.532 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 8fa21e1b-8161-303e-94cf-fa9494cfb19f | -17.7647 | -57.5115 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| cac33af2-5db7-3fa2-bbc4-1a6ac68d931a | -17.7674 | -57.3467 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 98e7d9ae-1a9c-3b5e-9ac1-c327b456309f | -17.7868 | -57.3649 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 451f9a06-014e-3493-88ce-d4f92eb59eb3 | -17.7872 | -57.3443 | 2024-10-26 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.8 |
| e9cfd3e5-5428-3d60-a06b-5b7222e937d0 | -17.8628 | -57.5407 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| f56964c6-f680-3172-a9ae-0dca17bdbd51 | -17.8631 | -57.5201 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 6a07bf97-c24a-362a-8374-52c18e79266f | -17.8828 | -57.5177 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 7df3988f-ee51-3b66-85e5-f0d9e43e662e | -17.9217 | -57.554 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| bfe6c7e7-9d58-3983-828b-3241c5e4288b | -17.922 | -57.5334 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| aea70602-415b-3c0a-a1c9-e94601704f9a | -17.9411 | -57.5722 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 788e3b0c-2d63-3f6d-866f-906dfd3c971c | -17.9415 | -57.5516 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.2 |
| a3c11d1a-e810-33ff-a0af-88b63ada2ac8 | -17.9418 | -57.531 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.4 |
| d81a2cb6-aa85-3857-b9e4-39df8379622b | -17.9612 | -57.5492 | 2024-10-26 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| ace738f3-0fac-3792-b377-34dc60583b94 | -18.0431 | -57.3745 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| c77f246d-a18f-364c-afea-601fcd5f72ed | -18.0629 | -57.3721 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 0ec3375c-e0df-3c13-b91c-895909c407ed | -18.0653 | -57.2274 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.7 |
| d8a875b0-86a7-3d4f-aeb0-ce6cd7276349 | -18.0827 | -57.3696 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.1 |
| 3ff3d231-58fa-31db-881c-955edd16433e | -18.083 | -57.3489 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| aa51222d-0d17-3a6f-aa74-82a9f8929a8d | -18.0847 | -57.2456 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| bda94769-abb8-33f5-9a38-8bd4ab4a5209 | -18.0851 | -57.2249 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 225f482c-6d73-3c86-af9c-70c12f885d3f | -18.1025 | -57.3671 | 2024-10-26 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| c592eb30-321e-3a46-8673-04fd9d7a033a | -18.2649 | -55.9975 | 2024-10-26 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 2d33dfac-cc42-34dd-bfa3-96283bafd547 | -7.82477 | -72.77802 | 2024-10-26 02:47:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 68bf3412-3f4b-360b-a977-f2faf897d96d | -7.82642 | -72.78924 | 2024-10-26 02:47:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| edf5a39e-c41d-36ab-8fcf-ffb8f4090d00 | -7.33687 | -72.80177 | 2024-10-26 02:47:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a4fd74c8-e88c-328c-a871-00465c9a9e3d | -2.1929 | -53.7234 | 2024-10-26 02:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 319110c0-30ee-38a7-95b4-ca33b076ba72 | -3.013 | -50.481 | 2024-10-26 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 4b6c0e5b-da27-304a-a86e-7e92a4aa580f | -3.0129 | -50.502 | 2024-10-26 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 02bfc5e2-99de-3033-b67b-dddebadf51c5 | -2.9945 | -50.4816 | 2024-10-26 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| c9a82c6b-f42b-3882-bb9b-240f7cba6f42 | -2.9944 | -50.5025 | 2024-10-26 02:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dc7155c0-f91d-3d0b-986a-c261028c4f72 | -2.8923 | -53.3247 | 2024-10-26 02:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 762ce008-db92-3fd1-9df3-008ad5b43ca6 | -3.4917 | -43.3136 | 2024-10-26 02:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5e3d0290-0fa8-3a23-97ec-a461265736d5 | -3.4915 | -43.3368 | 2024-10-26 02:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 5d530113-6f58-35cc-a611-ec815cc005d8 | -3.4729 | -43.3377 | 2024-10-26 02:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 69488bdd-f000-3bd3-bba4-7b473ab1728b | -3.473 | -43.3144 | 2024-10-26 02:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| ef7212fd-8f1a-32bd-a730-b6ff53027113 | -3.6084 | -45.8147 | 2024-10-26 02:55:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 8def8d9f-414a-38d5-8b8e-3173e9dbc298 | -4.58 | -48.0132 | 2024-10-26 02:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 234.1 |
| 3b993562-a949-3833-8c40-b40de2009649 | -4.5799 | -48.0349 | 2024-10-26 02:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 260.1 |
| 16c00915-a7d1-3f01-bfb3-518012954ff5 | -4.5613 | -48.0358 | 2024-10-26 02:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c980b6fc-e440-3dbd-8a58-1e617696fbd1 | -7.6474 | -63.4584 | 2024-10-26 02:55:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 19151d23-fcd6-3099-8ae9-3d9340505325 | -17.0499 | -53.452 | 2024-10-26 02:56:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f1541245-2114-390e-b3cd-a2c3b56bc52d | -16.9207 | -57.5086 | 2024-10-26 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| d24039f0-b0c2-38a3-9cde-df2389a22458 | -17.254 | -57.4903 | 2024-10-26 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 9fc88f64-c2bf-381b-bfd1-98e59c0252f1 | -17.2537 | -57.5108 | 2024-10-26 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 844eeec4-03ce-3518-bc72-07af8214085e | -17.7875 | -57.3237 | 2024-10-26 02:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| bb4e2eb0-8ee8-3b3c-80e7-48d95bd9b053 | -17.7872 | -57.3443 | 2024-10-26 02:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.1 |
| 7cfda761-a84b-3d72-8558-8fd0c07c024d | -17.7647 | -57.5115 | 2024-10-26 02:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| bfff379e-7611-3350-8c7b-c3036f233474 | -17.745 | -57.5138 | 2024-10-26 02:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| 79a416c4-5ec2-347e-8763-c221ec2b8f16 | -17.7446 | -57.5344 | 2024-10-26 02:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 36b87a79-f760-3769-91f9-d494a7bcef33 | -17.6865 | -57.4798 | 2024-10-26 02:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 471d0c48-6cd4-32d5-9ca0-c8fc4986e5f7 | -17.9612 | -57.5492 | 2024-10-26 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 8314e90b-8aa0-39bb-9afe-3a67838404d4 | -17.9418 | -57.531 | 2024-10-26 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 4dc44fac-ecef-3650-8336-b583c0e1df19 | -17.9415 | -57.5516 | 2024-10-26 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 206.4 |
| c5076555-8579-3aaa-b848-a4d0ee66e532 | -17.9411 | -57.5722 | 2024-10-26 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.9 |
| 02b0ae2d-80d1-3585-b407-0af69eff34e7 | -17.922 | -57.5334 | 2024-10-26 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| cc491407-25e9-395d-a833-7bc9a7be8a69 | -17.9217 | -57.554 | 2024-10-26 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| f3c33d59-e6ce-37cf-a406-cbf6b93b9d6c | -17.8631 | -57.5201 | 2024-10-26 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |


[Clique aqui para ver as próximas entradas](README24.md)
