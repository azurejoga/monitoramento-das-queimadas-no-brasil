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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdb9b0b7-d523-3ce7-a10d-a32b0edcfb4c | -11.83311 | -47.6921 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a38d1c5f-ddfc-358a-89d0-7b4fb9475346 | -12.59807 | -49.88837 | 2025-10-03 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20a00dbb-39c5-3232-be21-3077a4845f13 | -13.16425 | -47.89847 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a5dba4d-8821-37df-a706-fa94d0418b97 | -11.91452 | -46.75343 | 2025-10-03 04:12:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9bd5a80-5433-36b7-a05e-5b51cbf95ff6 | -10.76469 | -45.33614 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 652ef77f-9b4a-32c9-87f7-5d93aa411421 | -11.91167 | -46.26243 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26caf862-a0a9-32f3-9441-0ad2192e46a2 | -15.17008 | -43.6233 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c5de6bd-84a2-3455-8ace-3c5fb15acd09 | -11.0527 | -47.79934 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3879984-be8a-3e9a-9347-5b1318ef445e | -11.55679 | -47.65172 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 133564f7-33a9-390e-9501-1f33b7585f74 | -13.47823 | -47.2409 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a413f2f8-d4a9-3d4e-82a5-66839f6bffa1 | -14.19526 | -46.12019 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afed963e-2bdb-3e37-aaac-b5053f9b5aa1 | -12.86614 | -47.00043 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 866c9edb-150d-3597-b089-f457b9fa75c4 | -11.4688 | -45.01804 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63f1b5cd-cbd8-30be-8c45-5cf84692161b | -13.5578 | -47.30021 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0b80913-c4be-3b8a-b90c-db0fde6ad2b9 | -10.25266 | -44.94378 | 2025-10-03 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cea78e98-b5b2-312b-af00-05d127e32c55 | -12.74818 | -44.91761 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9eb34a0-6208-35b5-90b7-67a0b16abc14 | -13.7354 | -47.91624 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44cf1457-857b-3b9a-ba1d-3b411b359e7b | -11.61679 | -45.05834 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffcfbe32-918a-3167-9a83-3b2692f033e1 | -14.4066 | -46.17329 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e96b0a8-890a-3cfa-84c4-2a66a0596636 | -13.3126 | -47.80992 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b873ba1-6a08-345c-b191-f5010a8052f4 | -10.28859 | -45.18211 | 2025-10-03 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66be41fb-63ab-37db-8e35-86c8c3740c26 | -9.89475 | -43.7081 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 26151ed5-23b8-3f56-bab0-9c88948b8ef0 | -12.54009 | -43.18717 | 2025-10-03 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b97d13c6-d50c-3f1e-ba6d-50acedd6c2dc | -13.31086 | -47.59333 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 143041e8-19d7-3da9-b819-9e199eb68529 | -13.57486 | -47.28444 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0312efb7-2268-3aed-8b5e-16a29b73989d | -14.46532 | -48.40452 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4873c6bb-6d07-35f8-85d6-878dabde856e | -9.94744 | -43.73189 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee0a315f-49b7-3460-bff6-321a56aa602f | -14.01221 | -44.96583 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51d866b9-391e-32a1-9488-49288bd01073 | -10.91844 | -47.04813 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5978d9a1-d2e9-3057-a2a0-723a669a5eac | -8.52495 | -47.83323 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb1b61f1-c320-3b97-8486-5d3d37195ed7 | -14.29677 | -45.98639 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d1aa5f1-e5ee-3a48-8f90-da4bad2f9a8e | -13.19847 | -47.88947 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f29bc8ad-a562-3ca0-8130-926dcb275294 | -11.90219 | -46.29651 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55684814-4b91-3c50-8817-211bb0342fa8 | -13.12258 | -47.88943 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0c0b1ee-290d-335d-bbfb-60a8c023bc30 | -11.45149 | -44.96427 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e77b3931-fd7b-3baf-aba0-5bf6748ea473 | -13.35381 | -47.32967 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 762fbc31-68aa-30dc-9785-d8ce55eb1d7f | -13.13052 | -47.89069 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7fc891f0-bce5-34c0-93cc-80fd93f16fcc | -11.90574 | -46.26903 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0adf2bd-79c8-3807-af26-5a1baede8d48 | -10.00331 | -50.25728 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e46a660-d30d-39a3-9e14-90e8c0a80fd9 | -13.13555 | -47.83831 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82aca94f-65c1-37f8-bbc2-912fc6b39fd3 | -14.01623 | -44.9627 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dee365d-b399-3557-87ac-35117fcf3906 | -12.66121 | -46.95562 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14950700-d1a7-3d27-9a49-8b36128f6162 | -9.93152 | -43.58777 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddc55dbe-176a-3704-bf3f-0d7785f92536 | -9.9121 | -43.72962 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ca9d6809-cf65-34e6-abcf-c7408941cd4a | -12.93987 | -48.44796 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e4b21d7-8b28-399d-aaab-e6104f06ff8e | -13.27214 | -47.26803 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fc804fa-c1da-36f5-a4e1-eed42c25f9a5 | -13.12498 | -47.85231 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61e42007-9b69-3178-8255-3c86138f8cc8 | -12.61584 | -46.97089 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af86eef9-890f-39e5-8b9d-248ce17dcbca | -10.28281 | -48.06586 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca3a05e0-dc3e-375c-b2fc-e1b3c8c1651f | -10.75702 | -45.34452 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 162a3a2c-2a6d-3825-856f-dd64e8c8b78a | -11.12962 | -43.37857 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| f79ee95b-2256-3a97-bf8d-171b3f83385b | -13.75442 | -48.07556 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 47ccfde6-42f0-3dd0-9e92-bda5680f4e3a | -12.90737 | -46.89777 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a3fe6d0-2165-3d3f-b86b-0126345022d4 | -11.14565 | -43.40695 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1437a91c-c195-3432-ab37-0c9d1024a748 | -13.35516 | -47.3329 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0aecf4c-38dc-32f1-9e02-8c8cfbc62eef | -12.60822 | -46.96999 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 25073a44-352f-3c88-84bb-4faff1e863df | -10.29261 | -47.9346 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a10abfbb-c739-3243-a091-95b79edacfe7 | -11.12339 | -47.86858 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 260a726f-467f-308a-8fbe-53da16427622 | -13.1836 | -47.3784 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a8ed0c0-f57b-31a4-bc9c-918ba6d8d95a | -13.68056 | -48.64204 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a903c570-361b-3620-973d-e5ef1a6bffa4 | -14.19174 | -46.11936 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16820576-2790-3de1-aa5b-262e1c623161 | -10.33694 | -48.1791 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aff4d240-3da0-3d25-8299-17cc572b1bf1 | -12.11776 | -43.44162 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0054fa2f-7d18-3604-8d42-442772a14fba | -10.24497 | -44.9466 | 2025-10-03 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a664322-ffb8-3f12-ae2b-ece17fef21f6 | -13.78002 | -47.52815 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cfd209d9-c4ea-3697-9bdf-e70470853b81 | -9.92563 | -43.73187 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ff5d7278-766d-3f1e-b580-fc82a6558074 | -9.44502 | -47.36869 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a01af150-26d4-38a4-bf27-3f75303780e9 | -12.80581 | -47.03564 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56a9363f-1dad-36fe-a47c-c6e2615f25f5 | -9.92093 | -43.76105 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 228fc361-eb32-30e0-9110-e9b79dbb24b0 | -14.38152 | -45.95546 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2edec1ca-fff5-3ecd-96c2-9f05cd9de98e | -9.92284 | -43.72766 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d97f7175-b2d2-3d6d-a310-6a086cd80e0f | -12.72042 | -48.58066 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e641b148-05ec-3f8c-b322-34ffd11f9505 | -13.1504 | -47.89357 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7561e94a-5a18-33e5-823a-bb5263a68c4c | -13.33099 | -47.79738 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43bcdde4-e0f0-38ef-aff9-58c753b2addd | -10.86768 | -46.68157 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3766140-6587-38c0-9f2e-0039e29daddd | -13.5397 | -47.29172 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fea52d17-8cae-32ca-a77b-c76b8f59db37 | -13.14064 | -47.89359 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b28ea632-3287-3dda-a5f2-0cc43fd0a873 | -10.92692 | -46.73813 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c07b493-49b5-38bf-828c-e4c2f1c33a71 | -10.90765 | -47.04116 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c52a99-0f86-357f-a5df-8aceae54a076 | -10.10416 | -50.35109 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 27f739f0-93fc-36fa-adc3-50eeea739b8b | -11.63011 | -45.06439 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf1b7ab1-5b2a-39ae-9445-06da373aa78b | -8.80764 | -46.66765 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e38b3fcb-1b22-31f7-9344-88336c4d0ed6 | -10.10314 | -50.35659 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 71f27ccd-28b2-34b1-a408-19888a9bce52 | -11.07519 | -48.36028 | 2025-10-03 04:12:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 528d482c-5836-3763-b4d7-081c9db5da20 | -12.29446 | -45.37102 | 2025-10-03 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9662dd05-f08a-3021-b592-9b291a5c6f86 | -8.81084 | -46.66599 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30ec7d34-412f-346b-8c43-4bbbef6cfb0c | -14.19428 | -46.0608 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5527b6b5-3100-3c19-9f35-1514bb0fe296 | -12.90105 | -46.934 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24a08d62-2f77-351c-931b-96f22733e764 | -13.19685 | -47.82961 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf0e04b2-2f6d-324e-a00d-14d0f7801036 | -12.90675 | -46.36093 | 2025-10-03 04:12:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea10d252-8b31-3acf-b223-eb6c0e0a73a0 | -10.92008 | -46.73211 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b91c8b5-89f5-39f1-8eac-ac379f6e2e4f | -11.07759 | -47.70444 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f0de478-db82-3d60-9dd0-90a2b3db960f | -14.4129 | -46.15742 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241be91a-86e2-3d19-80f3-ee21ef3a524d | -14.58825 | -46.71267 | 2025-10-03 04:12:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea4ec184-d8b0-3c93-b4fd-9fe272058710 | -14.41285 | -47.87577 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52194178-39a9-3670-b1ef-bbef69ce4bd4 | -12.84386 | -46.86003 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f191611a-eab9-382e-93da-1f771e53b9ba | -13.39937 | -42.64978 | 2025-10-03 04:12:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2f29097a-815a-31e6-8877-f93be01192b5 | -13.57566 | -47.27993 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 951ca077-201b-3f62-aeb5-0f20cc788bba | -10.9686 | -51.08615 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1c72be0-8e29-341a-9765-9a2bc039094d | -11.79672 | -47.9239 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README55.md)
