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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a512819-d3f5-3788-9298-97cbaea7534f | -19.06512 | -49.37218 | 2025-01-18 04:23:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05dc54ca-1359-354d-a1e9-67abc7dedc07 | -11.74816 | -38.52372 | 2025-01-18 04:23:00 | NOAA-21 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 224267cc-fa7e-3d2d-a77c-126f4f93dc21 | -16.68251 | -43.88364 | 2025-01-18 04:23:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 685558cb-6887-3094-a8b1-bfb0e51b1e89 | -22.85474 | -43.52354 | 2025-01-18 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3c533142-ca87-3024-b70f-b17844e9ca13 | -17.31783 | -39.58156 | 2025-01-18 04:23:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ad67e6e7-ed9d-39f8-9894-df1e28230710 | -20.45893 | -47.5452 | 2025-01-18 04:23:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dec3f0b6-b968-3d15-ad4c-c79f7f53bf08 | -20.76346 | -46.76871 | 2025-01-18 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 79fca910-39f8-3765-a722-d025883e28fb | -10.28609 | -48.32829 | 2025-01-18 04:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6c111ac-b356-3939-8b40-170b9c482414 | -19.96925 | -44.21655 | 2025-01-18 04:23:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 912c3f6d-c1a1-393f-a79f-300235dbbe49 | -20.4188 | -43.55103 | 2025-01-18 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2c185bed-3e72-356d-acdd-59583cda9626 | -22.8539 | -43.52423 | 2025-01-18 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6f80a0e3-ffc9-3beb-98f9-427f1ee9b12c | -16.35054 | -43.69706 | 2025-01-18 04:23:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0fba290-3704-3ca7-83a3-9cb88d379956 | -20.45562 | -47.54462 | 2025-01-18 04:23:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f711a541-0246-3273-9cc4-6e7d25378a3a | -18.14682 | -47.80256 | 2025-01-18 04:25:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1536abda-d5fa-3e5b-b56e-7d3fb832c414 | -29.87437 | -51.15704 | 2025-01-18 04:25:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 1213d8fb-a187-371d-839f-7e8b603a1695 | -22.8398 | -53.47944 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 67d6dc35-d5f7-329a-b1b3-81f0287cbffc | -29.31117 | -56.0159 | 2025-01-18 04:25:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| a91bb63f-3e6e-3959-bf9c-0ffe7e1d0a38 | -22.86006 | -53.50039 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 2de4785a-81bc-3ef3-a8a9-bf77e3a19d8f | -22.85906 | -53.50569 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| e7bb7ddd-5913-32ed-8313-ec3b333e82e7 | -22.85518 | -53.50484 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 832312d6-9589-30b6-b411-0db6edd215de | -29.10693 | -55.93858 | 2025-01-18 04:25:00 | NOAA-21 | MAÇAMBARÁ | RIO GRANDE DO SUL | Brasil | 4311718 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 74ead00a-fa50-331f-abd3-8b1c9a0feaff | -22.8523 | -53.49869 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 7441232e-eef3-3398-b441-9246561352fc | -22.84855 | -53.47585 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 878986d3-e5ee-3006-b502-34cccf10f4f2 | -29.95191 | -51.61664 | 2025-01-18 04:25:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 0dc32360-8619-3008-a2cb-10d45206b80e | -22.85417 | -53.51015 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c2fc2127-0656-3eb4-abea-8dbab574dca4 | -27.08233 | -50.51207 | 2025-01-18 04:25:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6d7821a7-7068-33e6-819c-c02d7082fc8b | -22.85618 | -53.49953 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 7ac3540d-1ab9-3cfc-9788-c4a6606d1d60 | -19.71786 | -40.35506 | 2025-01-18 04:25:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1ae60f2d-8a3e-3164-be36-57847ed03fc9 | -17.00949 | -49.78241 | 2025-01-18 04:25:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4353edfa-3727-3429-9b9f-d38573bd73f3 | -19.17125 | -45.545 | 2025-01-18 04:25:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e875a55f-5a4d-3aee-a4a7-b1ae26c53e8c | -26.46287 | -52.22826 | 2025-01-18 04:25:00 | NOAA-21 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61eda9e2-721f-3495-9a91-7fdf8284a2db | -22.86194 | -53.51183 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| 80aa31ab-d6ad-3914-b396-5e32bb58d0ee | -22.86294 | -53.50653 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 3e8369db-529d-36c9-99cc-adc204a98dd5 | -22.85805 | -53.511 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| 7afbd666-8762-38a2-8a06-3c0bd1ed6e83 | -22.8408 | -53.47415 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c15ee630-a7ba-37c8-82f8-eab7a769bdbc | -22.84367 | -53.48029 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 74f4356b-aef1-3389-acef-9716387126a5 | -22.84468 | -53.475 | 2025-01-18 04:25:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 6a24e5a7-7951-3746-b514-7604f9856986 | -22.8585 | -53.4947 | 2025-01-18 04:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 7b951172-e7f4-35cb-94d4-187691731f6f | 4.3708 | -60.8156 | 2025-01-18 04:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f26b3e9f-9f0c-38b3-942f-9a5a4a29a94d | -22.8579 | -53.5169 | 2025-01-18 04:30:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| ce3c65ea-c87f-303e-bcb4-3069f5cf8146 | 4.36732 | -60.82539 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 620dcde4-458a-3526-91f7-57c6809043f0 | 4.91894 | -60.29417 | 2025-01-18 04:44:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b2351b1-dec1-38f0-ba04-90c987e7b758 | 1.8851 | -60.4843 | 2025-01-18 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fa6d866-701c-345f-8b55-628b49c35207 | 4.36018 | -60.82273 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 73f81d8f-525e-3ad8-be0d-075f3e8054e4 | 3.61446 | -60.11179 | 2025-01-18 04:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74ad316d-1cf6-3c64-9890-d54921203336 | 3.28093 | -59.9653 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cf694cc-61b8-39ba-a6ac-260b744e23ef | 4.29479 | -60.11892 | 2025-01-18 04:44:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6d1c8c3-cbdb-3579-bd3e-7310d19e53ee | 3.28631 | -59.9599 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0ace39d-7b4d-33f8-be7c-c9f29c3a81f2 | 3.61515 | -60.11646 | 2025-01-18 04:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d16aba5-d01b-3d11-a522-338fe6e07097 | 4.36016 | -60.82139 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c2bbc224-d805-39f3-a72e-9281d1fc4f43 | 0.86825 | -59.69242 | 2025-01-18 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b23a20aa-34cd-3230-a0f9-823ad8f081db | 2.94188 | -60.16427 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bd58a71-4a50-3504-ae0e-0e9737207d0d | 2.61545 | -61.31503 | 2025-01-18 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e26690a-c522-312f-91c2-c9b2fa2e33d3 | 3.27554 | -59.97068 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c817ee5c-c545-3aa6-a895-267486157b96 | 1.13007 | -59.43137 | 2025-01-18 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9ffb8a-bf95-3184-975e-1688e3279794 | 4.3729 | -60.81914 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b13b304-bce6-313a-b6a8-465d17ba32c1 | 4.29546 | -60.12366 | 2025-01-18 04:44:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aaed4b5-fc8b-3523-8766-65c88e59c912 | 3.28742 | -59.96309 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4048d453-f81d-3217-a45a-282788761fa6 | 4.53301 | -60.69117 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de87c3c9-3554-3de0-8517-361275f8b1ce | 1.89125 | -60.48347 | 2025-01-18 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdfbeea3-6431-3456-bc8a-e25858a81b0d | 0.86763 | -59.68841 | 2025-01-18 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f02d482-28d1-3fdc-b49e-9367fab84da5 | 4.53238 | -60.68676 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e732d69f-3bcd-3063-95ec-022a034d87af | 2.60892 | -61.31595 | 2025-01-18 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 487a4bb1-1368-3d52-b136-7b22e2e5072e | 2.94798 | -60.16335 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9e77621-6024-3d46-8c06-b242ce883f20 | 4.29702 | -60.12534 | 2025-01-18 04:44:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 481f5e16-4b36-3bfd-99a4-1726b65fd3c9 | 3.29283 | -59.95766 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e399a38-6904-3680-addd-3f73d8cbff86 | 3.28698 | -59.96437 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63dc25c5-03cb-3a06-9736-b15b8c8a0278 | 4.36576 | -60.81557 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d2aa826f-c53b-3f36-8e50-332cc5a03654 | 1.1295 | -59.42764 | 2025-01-18 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e03ea0c9-7443-3d76-ab10-92931e73e311 | 2.37504 | -61.25671 | 2025-01-18 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 759e86a4-ff1d-30bf-9a0c-79709215b6a1 | 4.36658 | -60.82122 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6f9e272d-bfe3-32ab-82e3-1282df83a7a6 | 4.36655 | -60.81981 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a05e2a00-5d78-3a6b-b218-05f74cca71c3 | 3.29236 | -59.95899 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9722372-e1db-37ed-bf6d-d54b558c0316 | 2.37584 | -61.26202 | 2025-01-18 04:44:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6060de3c-75d2-3af3-a470-5810e48a71a6 | 4.29633 | -60.12066 | 2025-01-18 04:44:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aa8ef71-ed63-3f7d-b32c-e6f9480fa844 | 4.37288 | -60.8177 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bea80bc9-5429-34fb-b60c-3db2ab973fdd | 3.28679 | -59.9586 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d2a134b-91d9-38bb-b990-fa5b6d815a66 | 4.37211 | -60.81372 | 2025-01-18 04:44:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 227ebf0a-9d6e-3d60-bf6c-6a2a9eaa120e | 4.30227 | -60.1271 | 2025-01-18 04:44:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 529c1d7a-3783-3940-988b-34d820dca739 | 3.27016 | -59.97607 | 2025-01-18 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba8d9c0c-3aae-38bf-ba3c-805023f029da | -10.28417 | -48.32871 | 2025-01-18 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d60ec526-73c5-31d1-af9d-fd0ecbd2aea9 | -15.4925 | -59.40834 | 2025-01-18 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cda7df1e-77e7-3043-94fe-eda1bce321d2 | -15.56671 | -59.41413 | 2025-01-18 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 636c3600-f54a-3d48-82a2-55294e7550d5 | -15.57099 | -59.41491 | 2025-01-18 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 342c03d1-e238-3b7c-b10c-ca7af65a0f2f | -22.8579 | -53.5169 | 2025-01-18 04:50:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| c858a197-0856-3ccb-a702-4a4007a9aff4 | -22.8585 | -53.4947 | 2025-01-18 04:50:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| 1cc45af5-2b6f-3906-865b-f07546dbf2ed | -22.85483 | -53.51244 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b5d35cc9-9026-3d25-a9f8-0b668399a0bc | -22.85317 | -53.50009 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0d6489fd-a51d-3747-b357-3f612a6ff812 | -21.87877 | -56.11557 | 2025-01-18 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98a3dc97-4276-33f9-ba14-efe754566bb4 | -21.88213 | -56.11623 | 2025-01-18 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfc49b89-be61-3909-b65b-082492755983 | -23.77094 | -54.57678 | 2025-01-18 04:50:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6de1a6ec-f3c7-3bbc-8174-9a33f6d29e10 | -22.84587 | -53.47871 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62ca6cb5-35ac-30fb-a140-faa064583fcb | -22.84246 | -53.47813 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7105a9bf-49bf-3240-aa8a-aad54ef7a085 | -21.8794 | -56.11172 | 2025-01-18 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b74029c5-8fff-36fe-8a1e-412187a72b79 | -21.8834 | -56.10856 | 2025-01-18 04:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f529164e-d0f9-3249-bb70-6e499fd63c1b | -22.85824 | -53.51302 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c0b5f33f-2fba-3725-980b-b411dfc7cce5 | -22.84304 | -53.47421 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 15079b91-f7d4-39bf-b6bd-5ea9523f7a9b | -22.85998 | -53.50126 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 080ae5db-3051-3b2c-9a2e-feb197fde2a6 | -22.84977 | -53.4995 | 2025-01-18 04:50:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1a8d52d6-2201-3bc4-959d-c574c1600cde | -22.67382 | -42.85303 | 2025-01-18 04:50:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README4.md)
