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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08b932fc-c333-3622-b6ac-751609958894 | -8.1264 | -43.139 | 2025-02-17 00:00:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| f12cfaf5-c84e-3ad5-9062-2925070350ad | -8.1264 | -43.139 | 2025-02-17 00:10:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 543e2d2a-78fd-3407-8ae9-187521e56997 | -8.1264 | -43.139 | 2025-02-17 00:20:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| f1e7c553-e23d-31eb-be0f-f0f6440a4a65 | 2.9092 | -60.4268 | 2025-02-17 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c1b43f41-458e-3383-aa7d-60ed8bb54b26 | -8.1264 | -43.139 | 2025-02-17 00:30:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 10a9a0a9-b7d4-329d-a256-13aca19c6a5d | -8.1264 | -43.139 | 2025-02-17 00:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| df2c504d-15ff-3070-94dc-fe3d5c0a2147 | -8.1264 | -43.139 | 2025-02-17 01:10:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 5d64875e-58b2-3ef8-a75a-c3e1790e8d2f | -10.77805 | -54.26926 | 2025-02-17 01:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1ca5e56c-08e1-321a-9375-3e1c2a465df9 | -9.12554 | -61.46225 | 2025-02-17 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 82a96574-f64a-39c3-a000-99378cef1e76 | -9.12705 | -61.47362 | 2025-02-17 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ca70544-2ae2-360e-aeb0-df25a446a5f4 | 2.6522 | -61.14825 | 2025-02-17 01:32:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00713a73-3442-3a6c-b8c8-48fde9f404f9 | -5.24174 | -36.20219 | 2025-02-17 03:17:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b64df924-b5e3-3813-87c7-ee624e926deb | -6.82592 | -34.94017 | 2025-02-17 03:17:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 20872af6-7a7b-38de-92f7-d61dc53c4d85 | -11.01268 | -40.33649 | 2025-02-17 03:17:00 | NOAA-21 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e2338816-dd4b-3287-9271-aee6b9695dc9 | -7.37809 | -34.8854 | 2025-02-17 03:17:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b91277bd-d523-3bca-9d6c-35d0a999f64b | -5.24264 | -36.19692 | 2025-02-17 03:17:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ec92c742-9bf6-335f-bf2d-b5861fcdb834 | -5.23693 | -36.20142 | 2025-02-17 03:17:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86b37aae-40e5-3110-8ffe-70f003a089f8 | -6.82163 | -34.93947 | 2025-02-17 03:17:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 73f16281-2585-387b-81c4-69d2b9b2c650 | -11.91781 | -43.12088 | 2025-02-17 03:17:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fb9c7c0f-9146-3bf6-9c20-6e014102c1fd | -5.24744 | -36.19768 | 2025-02-17 03:17:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 417fab9b-842c-3282-85de-b29922205943 | -13.00176 | -42.67176 | 2025-02-17 03:19:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b0066506-dc25-32e2-be3f-a7a4b17bf1f1 | -20.38273 | -40.84201 | 2025-02-17 03:19:00 | NOAA-21 | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f859f8c5-e1c4-3d62-b3c5-31532dc3c202 | -20.31985 | -41.68378 | 2025-02-17 03:19:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 38dbe74f-3e04-3be3-96c0-38aa10656ffe | -20.31911 | -41.68726 | 2025-02-17 03:19:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 47c7d4f6-a24b-3b9c-92a4-a16ba63b89b8 | -22.90847 | -43.5196 | 2025-02-17 03:21:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7e7cc70a-82ee-3f3f-b404-7b03d29d7d3c | -22.90756 | -43.52361 | 2025-02-17 03:21:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f582222c-b8ec-3b3f-9f83-b473c777f6da | -22.67616 | -42.86033 | 2025-02-17 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 39921523-4f2e-3b14-9d20-a44d6cc8bb60 | -22.67698 | -42.85665 | 2025-02-17 03:21:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 45885b22-ff0f-3d91-839b-9aa49b9b73f7 | -20.98509 | -43.03482 | 2025-02-17 03:21:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| daf09091-f2b5-33df-862a-084495f5d32f | -22.90621 | -43.52195 | 2025-02-17 03:21:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| acc8f851-1041-32ae-91a6-3569b1467671 | -7.19219 | -40.14021 | 2025-02-17 03:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50f440ca-234a-31b0-b122-2f65e358206b | -5.24161 | -36.19761 | 2025-02-17 03:42:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 122770ca-414b-37c9-a839-8b0345c4c514 | -5.23768 | -36.20063 | 2025-02-17 03:42:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 197e9c06-4037-3cb6-91fe-ffb515339c2d | -5.24498 | -36.19813 | 2025-02-17 03:42:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3125854f-6510-39be-a0d4-7b3107e0d261 | -5.24104 | -36.20116 | 2025-02-17 03:42:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0cf8525e-7acb-36d6-8f1b-bdf237ac05dc | -7.47629 | -34.84445 | 2025-02-17 03:42:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 03bae69b-3a71-3e3c-9dc4-d952cc882198 | -14.11901 | -41.67871 | 2025-02-17 03:44:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| add690e8-ac82-39a5-bd67-68e8028d4a7e | -11.01276 | -40.33329 | 2025-02-17 03:44:00 | NPP-375D | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26fb01b9-9374-3e2f-83cf-4fcfc8e466e3 | -9.56308 | -38.28844 | 2025-02-17 03:44:00 | NPP-375D | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a0c834e-1964-3737-92fa-00223f432b67 | -11.78925 | -40.92982 | 2025-02-17 03:44:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 10f4c847-dd9c-3ff4-a917-e4fbd14eaaa9 | -11.01199 | -40.33785 | 2025-02-17 03:44:00 | NPP-375D | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 699cb088-2ec5-38b3-93ff-3f504cd2cb9c | -13.00539 | -42.6726 | 2025-02-17 03:44:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b0e55d0f-44a3-311b-a350-9a767d564e2b | -19.74318 | -40.11694 | 2025-02-17 03:46:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5059097f-e683-3c1f-bb0f-5bd5009983c0 | -18.89418 | -39.9012 | 2025-02-17 03:46:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f20fb3a-6e45-3368-8085-d8bd4337824d | -18.52096 | -39.93369 | 2025-02-17 03:46:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7466af17-68fa-36f6-862b-d4f71b3915d4 | -20.31824 | -41.68595 | 2025-02-17 03:46:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a480fafe-b0c8-3d67-82e2-04aa2eaaf9a5 | -17.55558 | -46.5447 | 2025-02-17 03:46:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bea75ebb-47bf-3fe4-859f-10896a292fe8 | -19.71796 | -40.35292 | 2025-02-17 03:46:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b617d0f8-5fbf-37f9-906a-4dedc06392f2 | -20.984 | -43.0331 | 2025-02-17 03:46:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e1534553-7d47-35d6-b423-ca99c37512b3 | -20.3617 | -40.88877 | 2025-02-17 03:46:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 60f5db12-3c36-3958-8acd-9bdbefad9292 | -17.67691 | -42.74406 | 2025-02-17 03:46:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abc8c370-483a-308f-a09e-8f63d227f0c6 | -19.83965 | -40.08212 | 2025-02-17 03:46:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 75bad057-aad3-3de9-819b-a2018f0951ad | -20.319 | -41.6816 | 2025-02-17 03:46:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3bfa151a-51f2-3dde-ab0e-892f0e223ca9 | -15.46171 | -42.14719 | 2025-02-17 03:46:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64cc66be-ccd7-33d6-89dd-91dafb3e2a3d | -21.6589 | -41.32269 | 2025-02-17 03:46:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b688cd3b-a10f-396e-b97a-8ee4f3f366e8 | -20.98596 | -43.03185 | 2025-02-17 03:46:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 638002bc-31a3-32b7-a291-7a663347cf78 | -15.60573 | -42.39422 | 2025-02-17 03:46:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e5eb01c-c0ea-3dee-9416-9a5756299af0 | -15.0769 | -48.94403 | 2025-02-17 03:46:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96a31aff-6e76-3b35-a00d-ef529935f691 | -17.67565 | -42.74567 | 2025-02-17 03:46:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fac3559-5b92-3566-8274-bf6edf0d3b4c | -20.32259 | -41.68228 | 2025-02-17 03:46:00 | NPP-375D | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cccbdd38-f834-399a-89ec-49b929123415 | -20.3803 | -40.84241 | 2025-02-17 03:46:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8df8776c-1b58-3c51-a6cb-85b069020b52 | -20.36239 | -40.8847 | 2025-02-17 03:46:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 99e62903-f1e3-33a7-b5d1-c1614e4df9f3 | -20.98217 | -43.03107 | 2025-02-17 03:46:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c0a63fd5-89e4-3729-a785-9ecf3abb9618 | -20.32183 | -41.68661 | 2025-02-17 03:46:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 678e8085-cabd-3c48-9a89-cb9591d61a02 | -22.67529 | -42.8565 | 2025-02-17 03:49:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c010e638-eecc-3c57-ab52-1746d70eed12 | -22.81586 | -42.28328 | 2025-02-17 03:49:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae9fd55e-bb06-3dc8-b052-0642feef8663 | -25.18915 | -49.32729 | 2025-02-17 03:49:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 695e78ce-b7ce-31b7-85f5-38bfd5747044 | -22.90605 | -43.52066 | 2025-02-17 03:49:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 88045839-57e1-3331-9ff3-a2d369230500 | -22.54178 | -48.81161 | 2025-02-17 03:49:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9abefe94-1391-352e-9d97-d7b53d0cab65 | -23.98436 | -48.91525 | 2025-02-17 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e08d5e96-55dd-33f0-9431-d14d01d5636b | -22.90231 | -43.51958 | 2025-02-17 03:49:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6dd177e1-aa4f-3a3a-9bb0-891e38ee355a | -22.54399 | -48.80657 | 2025-02-17 03:49:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40b6b297-a7d7-3fc4-a0c5-d8541200c76d | -23.41438 | -46.54578 | 2025-02-17 03:49:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17d8a361-4605-3bc6-9d8e-e31cc53acd6f | -23.98364 | -48.91846 | 2025-02-17 03:49:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70a5e883-c244-3236-8fe2-e3b1eebd4554 | -4.43773 | -40.63412 | 2025-02-17 04:04:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cc81c917-3b7f-3a51-8a27-3e15da5d00c8 | -10.6161 | -44.56033 | 2025-02-17 04:06:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e050f73-a9f1-3ca8-82f6-c5ebaf7ee07a | -7.79519 | -41.88169 | 2025-02-17 04:06:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2f50c533-2644-3754-8f72-50473d754da9 | -10.53459 | -44.67355 | 2025-02-17 04:06:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9be8a889-ffa5-328c-b00c-723b7387904b | -10.61673 | -44.55653 | 2025-02-17 04:06:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dca8c66-94b3-371a-b3b6-ef31dd261d87 | -9.56237 | -35.69304 | 2025-02-17 04:06:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1da4f227-db07-382b-ab8f-a3e1534f37c9 | -7.7985 | -41.88221 | 2025-02-17 04:06:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e6924187-38a3-3c6f-a6ee-44142215b1a3 | -15.56804 | -47.85744 | 2025-02-17 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d365e189-b380-3e68-a9a0-9a45353bc502 | -14.13392 | -41.69067 | 2025-02-17 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 38e26660-8931-3bc5-b52a-61daf2d5df9e | -13.2705 | -43.60769 | 2025-02-17 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e83b7df-08ec-3735-829e-efba8638d606 | -11.99632 | -41.23987 | 2025-02-17 04:08:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14e3fc3e-dc22-37b7-87d5-f7298f128656 | -12.27734 | -44.83342 | 2025-02-17 04:08:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 526c8d76-16c6-378e-83cd-1425b57739d7 | -16.28643 | -46.27339 | 2025-02-17 04:08:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5b2dcbba-a230-3886-9f64-9c913b236109 | -16.28709 | -46.26946 | 2025-02-17 04:08:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f0339add-f891-3040-a287-a8cdd399e896 | -17.67455 | -42.74225 | 2025-02-17 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55442906-6c65-382d-8fef-3ef91643ecf4 | -13.54454 | -44.39906 | 2025-02-17 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12ed4221-bb0f-3286-98b0-bfc487920a12 | -17.09474 | -43.8045 | 2025-02-17 04:08:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9871237-1106-377f-b488-6ba392d7ac32 | -14.11869 | -41.67653 | 2025-02-17 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aec45888-69a4-38be-bc47-1e29c312588d | -16.34801 | -43.6947 | 2025-02-17 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a81d6659-4509-391b-ae00-1322bb9f3964 | -15.60493 | -42.39674 | 2025-02-17 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 092f18be-e01c-3c2c-9bb0-cced3dbcfd0a | -11.91789 | -43.11789 | 2025-02-17 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0f6a6de4-cb29-3e4c-ba23-57c1a737d00b | -16.0724 | -46.12375 | 2025-02-17 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae33688a-6af7-3da2-b018-1939694d8749 | -17.67736 | -42.74654 | 2025-02-17 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65764657-f730-3613-b216-fe702bc83eb3 | -15.46185 | -42.14718 | 2025-02-17 04:08:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d57e7e25-d2b4-31bc-8c5b-7e3606e5fae0 | -12.27795 | -44.82964 | 2025-02-17 04:08:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 28de1aac-1e21-365c-acf7-258027619214 | -13.00401 | -42.66959 | 2025-02-17 04:08:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |


[Clique aqui para ver as próximas entradas](README2.md)
