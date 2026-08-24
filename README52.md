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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c96a9b-0347-3643-af92-67d930c0ddd2 | -6.3507 | -54.7464 | 2026-08-24 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ba21a6ba-9629-3113-a1c1-69a78f0ca55f | -10.6305 | -52.2518 | 2026-08-24 13:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 12f7006a-019c-30e7-b885-4cf27815bef4 | -7.0193 | -48.0106 | 2026-08-24 13:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 2d5de43b-5ff4-37f2-bcdf-5ab3fa054a13 | -6.8491 | -52.505 | 2026-08-24 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f5422d14-7691-33b8-93a5-bfdc376d73f0 | -14.9582 | -52.6827 | 2026-08-24 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 250.0 |
| 9af47cc7-df88-3838-a565-2ce6b0fab77a | -15.3241 | -53.9407 | 2026-08-24 13:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ef0f69f2-b695-320a-b191-17ed925c26ba | -14.3316 | -53.2057 | 2026-08-24 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 76d1b207-367b-3308-b63e-9c78a3d22b00 | -11.4494 | -44.5353 | 2026-08-24 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f6b0721f-5e52-3df1-be68-dd044760f801 | -7.507 | -44.4583 | 2026-08-24 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 0c4ce187-a6c2-35fe-8730-5e9932729110 | -15.6951 | -53.8088 | 2026-08-24 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 6c4ec29b-a25d-340e-bab8-9347d45d7ee5 | -7.2713 | -45.37 | 2026-08-24 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| b72f09ba-756d-35be-890d-752bc34db91e | -15.3237 | -53.9617 | 2026-08-24 13:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8d325631-b1e7-389b-ae91-942e5a211744 | -15.2469 | -52.7924 | 2026-08-24 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d4f2457f-16e0-36e4-a80f-4f552bca2d3e | -14.3316 | -53.2057 | 2026-08-24 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 130802a9-6bdc-3574-9534-928fae2e9916 | -14.9396 | -52.6428 | 2026-08-24 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 70cf11ff-71e9-3b50-869b-76f5b29cf72f | -6.3507 | -54.7464 | 2026-08-24 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 9404b9de-9fad-3281-866a-5ca6769b7a1d | -15.2648 | -52.8747 | 2026-08-24 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3cf61637-5de7-3a8d-8624-4cedb96394e4 | -14.2781 | -51.7953 | 2026-08-24 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| bc99b118-a245-3a8f-a567-c5e7fb7aae78 | -7.2901 | -45.3683 | 2026-08-24 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 202.1 |
| b5fcacaf-6d91-330c-91ff-e67d7f2f3b0b | -7.507 | -44.4583 | 2026-08-24 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| c3898bdc-e6b7-360d-ba2f-88cd75a63e89 | -14.9392 | -52.664 | 2026-08-24 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 408.3 |
| c0f924d1-d005-3e59-a2d7-3529eac4c2a5 | -6.5596 | -45.2947 | 2026-08-24 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 2a2ddbf8-3646-311e-a1a6-1a4c6fb78bf8 | -9.7131 | -46.0229 | 2026-08-24 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2b1723bc-0118-35c9-8e9c-efbb06fae169 | -10.7985 | -50.9518 | 2026-08-24 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f1411a80-0c6a-342f-8c9b-5300bb7183e8 | -10.8174 | -50.9498 | 2026-08-24 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 415a14e9-aedd-3e63-bac9-f3e7e366a274 | -4.9535 | -45.1374 | 2026-08-24 13:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5006026d-260c-38fe-a77e-337ded0e3b6a | -14.9773 | -52.7013 | 2026-08-24 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| dd79b147-7239-3332-aa4e-e9e114a84d03 | -6.8491 | -52.505 | 2026-08-24 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 67d5c0d6-d492-34f5-ba9e-74189876491d | -10.6305 | -52.2518 | 2026-08-24 13:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 7b2b29d3-2da2-3ebc-bded-579b7c80c4a3 | -12.0566 | -50.5567 | 2026-08-24 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f6b6d62d-d892-399a-9357-eb6579728052 | -6.8305 | -52.5061 | 2026-08-24 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 20df5fa2-7233-3ede-a14d-8248a48dd133 | -7.0193 | -48.0106 | 2026-08-24 13:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 032837fb-976c-3b68-9db7-6c2692a4618c | -13.8954 | -54.0508 | 2026-08-24 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 3469be6f-6be9-393f-989c-c8f1bee583f1 | -6.3505 | -54.7665 | 2026-08-24 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 313.3 |
| ff55a82c-014e-3cd1-a747-10a89035eaa5 | -13.8957 | -54.03 | 2026-08-24 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3724c7f4-95e1-3260-98cc-71c8599a578e | -14.9388 | -52.6853 | 2026-08-24 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 449.4 |
| f457617d-b3a3-35b5-9131-351b4e9c83ce | -10.7988 | -50.9305 | 2026-08-24 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 73487250-6041-34a3-ba08-9e0dc118abea | -16.434 | -49.9125 | 2026-08-24 13:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 9baba1c1-faed-3d9a-8ac8-ede950ae4aeb | -9.7324 | -45.9981 | 2026-08-24 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a8c5b625-6321-3e32-aaf5-87be7da7816d | -7.507 | -44.4583 | 2026-08-24 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 260.1 |
| 8b7eaa80-3d89-3144-8fbe-9670efb85cca | -6.3505 | -54.7665 | 2026-08-24 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 311.2 |
| a3a2f77c-9eec-339c-892f-4d39aa49627d | -13.1512 | -51.3854 | 2026-08-24 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.8 |
| b0c7d3b0-9353-3330-ba52-eb3efddeaa34 | -7.2713 | -45.37 | 2026-08-24 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 52da4d6b-8721-32ed-91b0-b1c98d7e4f1b | -7.2901 | -45.3683 | 2026-08-24 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 200.7 |
| d6caacb0-b22c-30c0-8daa-daa00c70fd9c | -10.7988 | -50.9305 | 2026-08-24 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a0709fdc-1942-3d41-afb4-aabe01312681 | -14.312 | -53.2291 | 2026-08-24 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1cd40e1d-4a4b-3e67-9996-e9f6a6feca70 | -11.4201 | -45.1181 | 2026-08-24 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 01d28da2-2a62-311a-9566-a61029debede | -6.332 | -54.7674 | 2026-08-24 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3072566e-cb88-3b8d-8392-e211384ca608 | -16.4143 | -49.9158 | 2026-08-24 13:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| eee45f5d-caa6-31e0-8777-28ae16844300 | -14.9388 | -52.6853 | 2026-08-24 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 401.7 |
| f8492139-080b-3edb-84d3-aef6f81be20b | -6.5408 | -45.2962 | 2026-08-24 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 00f35871-11d5-37a3-bbb5-bf07b0ac48e6 | -14.2978 | -51.7713 | 2026-08-24 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c7186238-4e15-3d4c-9400-251a3cbb1c8d | -9.0494 | -50.7589 | 2026-08-24 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e8d6ca55-1c54-3e0e-9ee3-f0e88c27919f | -6.3507 | -54.7464 | 2026-08-24 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| d5714df6-d2e3-3aeb-a087-e53d437bc9eb | -10.7985 | -50.9518 | 2026-08-24 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 76d8f28b-9bbb-30a5-b32d-7a3c076a5b79 | -6.5596 | -45.2947 | 2026-08-24 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ed2f1ef5-2f26-38a4-ad9e-53baecec7ac8 | -10.8174 | -50.9498 | 2026-08-24 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7bcf9fa3-4a05-3617-82cf-1269bbb61485 | -14.2781 | -51.7953 | 2026-08-24 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| fcc613ff-8c15-3157-a0cb-af72d0308d98 | -14.9773 | -52.7013 | 2026-08-24 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 68d3658d-2d13-3ac1-905e-cbdbecae4b0c | -16.434 | -49.9125 | 2026-08-24 13:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 0486406e-6869-305b-984d-38e05d2407bf | -6.8305 | -52.5061 | 2026-08-24 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cbdfa3f9-cae8-392a-9f3b-abab65316656 | -12.6556 | -47.817 | 2026-08-24 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 892e98fe-f52f-3060-b2e1-7ddb95068fa5 | -14.3316 | -53.2057 | 2026-08-24 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 075d8550-f10a-392f-92c9-6af83b43eb22 | -10.0046 | -46.8201 | 2026-08-24 13:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 478704c5-030d-3c20-8f7a-bedfcc1db9df | -14.9582 | -52.6827 | 2026-08-24 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 451.8 |
| 56898b9e-d1f8-3f49-8d99-66ff165e3c0e | -9.068 | -50.7784 | 2026-08-24 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 10547b4f-585a-3e3a-a3d5-ffe6c9649278 | -6.8491 | -52.505 | 2026-08-24 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 7cfdacbb-ef96-310c-9e96-2da8d4d20708 | -6.8491 | -52.505 | 2026-08-24 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 5476c22c-1251-3d3f-8910-66f0e78dc889 | -14.2785 | -51.7739 | 2026-08-24 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| cb3e6099-c821-3c8e-909a-f219fc36784e | -7.2901 | -45.3683 | 2026-08-24 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 207.0 |
| bb6739c9-2ee5-35dd-95d2-832fcc728045 | -7.507 | -44.4583 | 2026-08-24 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 6ac35890-05e1-3a03-921d-a5d2d3ec5dc9 | -10.7988 | -50.9305 | 2026-08-24 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ca99f203-44dc-3c05-b7b2-039db50b410a | -14.9776 | -52.6801 | 2026-08-24 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 34fdc9cf-1991-3f23-9bc7-d2a30b59cdc3 | -6.3507 | -54.7464 | 2026-08-24 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 210.9 |
| 8cfc24be-12d2-38a0-af24-a37db2d92405 | -13.1512 | -51.3854 | 2026-08-24 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 7b02008d-00f1-3816-8e14-316e6ac50582 | -17.4412 | -44.936 | 2026-08-24 13:50:00 | GOES-19 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| bb87c514-e380-36dd-bfe8-378d9f3e682c | -11.4494 | -44.5353 | 2026-08-24 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0f72bc05-d8c6-3620-960c-db67467a7773 | -7.2713 | -45.37 | 2026-08-24 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 45883b11-7bb2-3451-bba4-a0362a76e7bc | -16.4143 | -49.9158 | 2026-08-24 13:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 86155a42-d256-341c-8712-e4258afbaf11 | -14.2398 | -51.779 | 2026-08-24 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 92aeaec8-d687-3153-956e-d65a6f79d9a8 | -7.8277 | -47.6602 | 2026-08-24 13:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 1f613288-d001-3a04-a695-f25fb5ab16e0 | -14.3316 | -53.2057 | 2026-08-24 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 6497add0-93d2-346b-91a0-7640c8d91219 | -7.2193 | -60.6316 | 2026-08-24 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6f444498-0c0e-318c-8c9b-fdf0f898fed4 | -7.7845 | -56.2858 | 2026-08-24 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 44549eca-8fc8-37c6-81ca-bec5766b8653 | -14.2402 | -51.7576 | 2026-08-24 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 77fdd22e-49c1-3636-b982-e1ae1980a398 | -14.9388 | -52.6853 | 2026-08-24 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 50b5c7bb-9b49-379d-bbb8-20f2f261289e | -9.7324 | -45.9981 | 2026-08-24 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b9ee9f08-d03f-3dc3-9e10-2bc9e8d5bd70 | -10.0046 | -46.8201 | 2026-08-24 13:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 6166b270-72d5-3c55-9c3d-3d532538d4bc | -6.332 | -54.7674 | 2026-08-24 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| a8135ae9-4ee4-3701-b92f-31c92079dd36 | -14.9582 | -52.6827 | 2026-08-24 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 6fb5e776-7bdd-393b-998d-3c4a707a3535 | -15.2854 | -52.8084 | 2026-08-24 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 1a8cc66f-40c8-3b2a-8ed1-71adbb0a04d2 | -13.8954 | -54.0508 | 2026-08-24 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1e5758c7-0b7a-365d-b08d-2c7e540d62e2 | -4.9535 | -45.1374 | 2026-08-24 13:50:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 65923d74-cf90-3657-bc3e-abc18ae2d4db | -6.8305 | -52.5061 | 2026-08-24 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 08fd8486-7979-37fd-a5f4-f259f3d2d62f | -14.2781 | -51.7953 | 2026-08-24 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9143ef63-ea39-3f0d-945d-ea487495af84 | -14.3554 | -52.9294 | 2026-08-24 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| abd30efb-5c50-3b65-a370-615be040f79d | -6.3322 | -54.7473 | 2026-08-24 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 734c96b2-63ad-3dc2-a739-f23ad698ab69 | -10.8174 | -50.9498 | 2026-08-24 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ea1794ae-5546-336d-b7c2-f4bdd74a955c | -16.434 | -49.9125 | 2026-08-24 13:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e9b9550f-97c1-3980-965d-a1b9b8a72635 | -10.7985 | -50.9518 | 2026-08-24 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |


[Clique aqui para ver as próximas entradas](README53.md)
