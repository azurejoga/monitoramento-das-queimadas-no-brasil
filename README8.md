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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43095a6b-f6de-3ca9-b639-4159e04abff8 | -11.8269 | -47.596001 | 2025-11-17 01:12:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7973fb1-1cef-3960-965a-06fe01d4d0c1 | -11.8127 | -47.581001 | 2025-11-17 01:12:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6cb073d-352c-3869-8769-d3f32043803a | -12.7022 | -46.7939 | 2025-11-17 01:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6f3fec0-0726-31c9-b044-2a45dde62796 | -10.6677 | -49.368099 | 2025-11-17 01:15:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58f31f3e-3977-3156-8ee0-3787c733edd9 | -9.3328 | -46.5709 | 2025-11-17 01:15:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60cd53b2-0639-38fd-ac59-e528c3714d6b | -2.6889 | -52.067501 | 2025-11-17 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a51c7dd-5ec5-3f48-b0dc-3f5f2969dfed | -3.7686 | -51.0714 | 2025-11-17 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24c9fe22-3ed9-3f46-b83e-d7bf2a7747e8 | -20.315201 | -57.768398 | 2025-11-17 01:15:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7d333740-e8ba-3448-9375-00802114c1b5 | -2.4829 | -50.243698 | 2025-11-17 01:15:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a99224a-fd37-35b7-ba13-3b322b5abb6e | -7.9704 | -50.016499 | 2025-11-17 01:15:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbe7b252-0aa9-38f3-97fe-6df2849b8d48 | -7.2266 | -47.984001 | 2025-11-17 01:15:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89f21991-5450-397e-a066-773b2f308360 | -2.5097 | -47.836899 | 2025-11-17 01:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950aff6d-6a9b-39d1-8c0a-ce7cdb285713 | -3.7764 | -49.267799 | 2025-11-17 01:15:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08bf0d4d-09f7-3f89-be60-1e84f5ac3675 | -2.529 | -47.832298 | 2025-11-17 01:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac690ba-c02e-32bc-98d4-8179190a7c18 | -3.1858 | -50.653099 | 2025-11-17 01:15:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 162cad4a-86e9-35bb-b4a4-5f27527d1edb | -10.6712 | -49.382 | 2025-11-17 01:15:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c39893e-5195-37b4-99ab-a85bd380201e | -9.5806 | -49.109699 | 2025-11-17 01:15:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 240415e2-d4c2-3b55-8e20-5958b736d922 | -2.248 | -53.6105 | 2025-11-17 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c6c34ea-7baa-3da9-becc-c7f86e6fc8fd | -2.8951 | -53.2952 | 2025-11-17 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1809d465-834d-3f8f-bd09-c86de547a8c2 | -3.7861 | -49.265499 | 2025-11-17 01:15:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa87c7e-939e-307a-9f40-c2a3492bd9ea | -10.658 | -49.370602 | 2025-11-17 01:15:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88b2af01-b96b-3abf-8088-878bee20b6fd | -2.5193 | -47.834599 | 2025-11-17 01:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c612b373-9fd7-3bb3-ad2c-5e5694ef6024 | -2.2503 | -53.6203 | 2025-11-17 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22c25e73-197e-3747-84d0-8f4a6e046bb2 | -5.8385 | -48.845402 | 2025-11-17 01:15:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c2b5d57-7e36-3a1d-aaa9-4c327abb3de0 | -9.5843 | -49.124599 | 2025-11-17 01:15:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2dc567f0-9b21-3f40-abaf-fbfa19e71879 | -2.5039 | -47.813 | 2025-11-17 01:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7ad2c2e-ac4d-344f-b7a0-7f651d2d69dd | -9.3231 | -46.573502 | 2025-11-17 01:15:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b62fb1a-0084-3c2e-b858-8a74752455cd | -8.5344 | -46.0709 | 2025-11-17 01:15:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c0136d9-9405-3861-89ea-07a799fba3fb | -3.7589 | -51.0737 | 2025-11-17 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c8154f-b590-367f-9874-055530e8d6b0 | -3.7712 | -47.733398 | 2025-11-17 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95c503bf-dfe6-37e6-ae3e-a9274c7fb66c | -11.8552 | -56.897301 | 2025-11-17 01:15:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c46d955c-93c6-39de-819f-9f31672e2076 | -4.7282 | -46.400501 | 2025-11-17 01:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40153a2d-2afb-353c-811f-019e748cc247 | -5.1228 | -56.038601 | 2025-11-17 01:15:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7a2faac-f77d-3cde-8154-9ec8aee03c39 | -3.7654 | -51.0578 | 2025-11-17 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b43b6a0-e6a7-3cd8-b69d-05bd478c7bd5 | -10.9614 | -48.690899 | 2025-11-17 01:15:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51a0822e-cf05-3f3e-8b59-6cc7cd0047b9 | -2.686 | -52.055302 | 2025-11-17 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 451e86fe-b401-380a-bca6-00bca9b805ea | -2.2405 | -53.622501 | 2025-11-17 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de00124d-d7f5-339e-a48a-b5c750ad0a11 | -4.6977 | -46.3195 | 2025-11-17 01:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff6895b9-f317-364f-bc59-6f1712c15139 | -10.8563 | -46.763599 | 2025-11-17 01:15:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b76f8238-5937-3609-be67-ef40c8564ded | -2.6791 | -52.069698 | 2025-11-17 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d2ae10-ccbe-3b09-83ff-9dc12fa0952e | -2.2526 | -53.6301 | 2025-11-17 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71bf36c9-a353-3a42-a643-86d481b5c403 | -7.2169 | -47.986401 | 2025-11-17 01:15:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1ef475c-683d-32da-a6e2-3af3ea766082 | -4.1655 | -50.198299 | 2025-11-17 01:15:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fda7207-d2a5-3e27-b91d-666af6dfaa80 | -3.235 | -50.5149 | 2025-11-17 01:15:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af3ed66f-f415-3574-8b14-0996fa0f0e44 | -3.2447 | -50.5126 | 2025-11-17 01:15:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d09f37-dfff-3595-b1a3-66aaef9891bc | -3.8325 | -55.812599 | 2025-11-17 01:15:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe279751-1313-34d1-bf28-79794fa05271 | -11.3469 | -48.906898 | 2025-11-17 01:15:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc47b9b0-b903-3446-b8cd-c975d9f6c096 | -3.2411 | -50.497398 | 2025-11-17 01:15:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 650732f8-8ae9-3621-bd63-12f9265f376c | -20.316999 | -57.777599 | 2025-11-17 01:15:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 22ecc172-ec9f-37d7-ba77-f8330deeec2f | -10.8509 | -46.743 | 2025-11-17 01:15:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcdfc973-0f22-31b7-bd55-930a99602ec7 | -3.7817 | -49.247398 | 2025-11-17 01:15:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f1338a5-bdac-324e-a726-59888ec4dd43 | -3.2314 | -50.499699 | 2025-11-17 01:15:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d3fb44-54ae-308a-8b2d-b5eddb47c488 | -3.3065 | -50.084702 | 2025-11-17 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed6cee97-3062-3989-b088-c4410c102def | -3.7769 | -47.7565 | 2025-11-17 01:15:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9b21f05-ca7a-36a9-94e1-e15ea8b4c30b | -2.5136 | -47.810699 | 2025-11-17 01:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ae04b5b-a138-3c95-9044-10a858b897f6 | -7.967 | -50.002701 | 2025-11-17 01:15:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41671142-a058-3a52-b2d7-1ca04c968f84 | -3.7557 | -51.060101 | 2025-11-17 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed9e7b3-bc0b-3ade-b586-4451b7e4d1c9 | -2.8904 | -53.275101 | 2025-11-17 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f44c58e-00b1-30fb-9da8-b2798c813bcf | -12.1959 | -54.2714 | 2025-11-17 01:15:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec9fb51-a5e4-309f-a6bd-8a0e0af3fd3c | -4.7212 | -46.372799 | 2025-11-17 01:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eaa64d1a-d839-3fad-892c-9733487634a6 | -20.326799 | -57.775501 | 2025-11-17 01:15:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c2666d0-f877-3033-b791-986cc00a33eb | -5.1244 | -56.0457 | 2025-11-17 01:15:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf095bca-dcf6-39fa-a33a-cc33386f02ca | -4.7378 | -46.398102 | 2025-11-17 01:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 480e6d0b-0af5-3e27-973c-dceb1ede6b81 | -4.1692 | -50.213699 | 2025-11-17 01:15:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ee7b8f4-4677-3b83-859b-431323475ca7 | -3.4094 | -50.128502 | 2025-11-17 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c2519f-d2e9-3cd2-be89-5e0ed8392cfd | -12.1942 | -54.264 | 2025-11-17 01:15:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37b20382-6e6c-33df-9324-300da77c9e29 | -7.9767 | -50.000301 | 2025-11-17 01:15:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c597bee2-feb7-3400-88b1-ef6d820d5ac9 | -10.9517 | -48.693401 | 2025-11-17 01:15:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8d83b6c-cab0-3dc0-8e20-6bd80fe967c6 | -2.4732 | -50.245899 | 2025-11-17 01:15:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb54f41a-ef5d-3563-85a9-6b3c5e04e243 | -10.9556 | -48.708599 | 2025-11-17 01:15:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea2e2232-d8f9-336a-b183-c5e665660531 | -3.4789 | -49.692299 | 2025-11-17 01:15:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c256cee3-8c2d-3ad8-9a43-a83c708dfcd5 | -10.6615 | -49.384499 | 2025-11-17 01:15:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee30109b-44f5-3689-ad0e-8f8eb22b9e0b | -2.6917 | -52.079601 | 2025-11-17 01:15:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f27c75-0ffc-3d58-b480-92b6d1dbc3c7 | -3.151 | -50.2062 | 2025-11-17 01:15:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 884ee78f-3dbe-3cc6-9111-12da7b9814a2 | -4.7308 | -46.370399 | 2025-11-17 01:15:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed10544a-ead1-3dcc-8f85-b69c62247ac1 | -2.8928 | -53.285198 | 2025-11-17 01:15:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16f167b-a61a-379a-b970-a8678f1d44b8 | -3.8308 | -55.805199 | 2025-11-17 01:15:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65e48a61-f8fa-3d72-8d6b-8f813bf0d648 | -6.6875 | -42.0296 | 2025-11-17 01:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 6e077c6a-7279-3f39-a47f-752f3250ad22 | -11.8295 | -49.2242 | 2025-11-17 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| dae51701-cb97-3590-be53-8718f703ded0 | -11.8987 | -46.1934 | 2025-11-17 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| d4abae0b-9a29-3f08-9763-6ad6959ef250 | -11.8486 | -49.2218 | 2025-11-17 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 73975144-19f5-3215-946f-d82c4c7ac44d | -2.5238 | -47.8332 | 2025-11-17 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 56653f07-4e8e-3119-b1c5-fef03f86a71d | -2.5238 | -47.8115 | 2025-11-17 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 06440c0a-0d6a-37e4-91ae-527eba3b15b6 | -11.7021 | -48.8474 | 2025-11-17 01:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e6fcc1bd-d842-3f03-9d5e-53978e602356 | -3.2344 | -50.4952 | 2025-11-17 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1b4eaef4-41f9-33db-8c66-5bfd5165a8dc | -11.7017 | -48.8692 | 2025-11-17 01:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 8eacc103-a986-31c0-9b16-dc46be8edb58 | -2.5053 | -47.8337 | 2025-11-17 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 43bb6f5b-1d03-3199-8e8a-9e42ea90c661 | -3.776 | -49.2517 | 2025-11-17 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 20b19e62-da36-383c-9134-aaa51a7094ca | -2.5053 | -47.812 | 2025-11-17 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 517e31b0-7453-3fed-952b-6530287879ac | -4.7211 | -46.361 | 2025-11-17 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 943b8b7d-c98c-3f7a-b03a-ea51e4e721f2 | -11.8991 | -46.1707 | 2025-11-17 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 6b3d098f-e3d5-3764-8510-5a07443ed3d6 | -10.6687 | -49.3813 | 2025-11-17 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a07be2a3-12f1-31ef-ba00-d13bd9a6a6e0 | -4.7395 | -46.3821 | 2025-11-17 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 585ddd3c-da06-33fb-8c9e-8489ec0f5ecb | -9.5152 | -40.331 | 2025-11-17 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 155.2 |
| 3a31048e-3f1d-3ebf-9651-1974ea08674d | -4.7209 | -46.3832 | 2025-11-17 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 7340ad01-b013-3b85-8b75-7fb35c76a76b | -11.849 | -49.2 | 2025-11-17 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 12327ad6-6473-3df7-8e9f-c43950f835c0 | -6.6687 | -42.0314 | 2025-11-17 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 43.3 |
| eadfb047-377d-3e17-be1e-2b6f54efb786 | -2.5053 | -47.812 | 2025-11-17 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 43c16020-f4d5-3c1c-834a-b3472016170d | -6.6873 | -42.0535 | 2025-11-17 01:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| cef8d04e-bb1b-386d-a5c2-8bc4a99fba82 | -4.7395 | -46.3821 | 2025-11-17 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.9 |


[Clique aqui para ver as próximas entradas](README9.md)
