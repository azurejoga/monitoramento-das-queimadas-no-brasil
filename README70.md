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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 729db833-a37d-3093-924c-a3e12842dacb | -13.10716 | -48.00689 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38588a94-2fbc-3b6d-bfb0-65a6c9c53fc2 | -12.89981 | -47.29607 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ddcf8ad-98c9-3a02-9bd0-f9e790050b68 | -17.67435 | -52.24936 | 2025-10-06 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2e7b8c4-158b-33db-b670-f4a425edb071 | -13.62974 | -48.71318 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1448d5f5-d82c-3c52-b7f7-acfc6272a352 | -14.6299 | -52.54432 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a14d9bc2-1635-3c20-b9c6-55f79f27c913 | -14.92543 | -46.82155 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 429bac88-8c96-3f23-8bae-cc85cb91a172 | -16.94908 | -52.67336 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6964a1fa-8f98-38a6-a291-59d4ed9436bd | -14.54945 | -46.96249 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 149c77e3-b466-314c-93cd-0beba336a5dd | -11.92306 | -55.90529 | 2025-10-06 05:18:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04beaf46-f266-3caf-a22e-a5d84f8982ef | -12.38103 | -63.70879 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d312af26-370b-36c0-9c59-a780622885d7 | -12.29171 | -55.10832 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7198cd93-6ac6-3fe8-9cbb-3d01aac44b27 | -15.20968 | -56.81035 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd5d64c1-1765-32a4-8d66-51c77c2f754e | -13.23516 | -48.46235 | 2025-10-06 05:18:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 514e0e85-6412-3c1b-ac3e-5401c6a907c5 | -15.99877 | -50.85265 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ef83729-1c18-3b53-97df-d70fb7c3fe31 | -13.08629 | -47.83565 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2499ac2b-4938-368e-a568-76f23fc630f1 | -13.32556 | -48.05654 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e6ce004b-4ef9-3d4d-8d3d-6772af585d27 | -12.27916 | -55.1101 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a1468b8-4ccd-32f3-a0bf-d4f67885d2a3 | -15.74663 | -47.69726 | 2025-10-06 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e78d4286-2203-39d0-acb3-30cf74b0b277 | -16.9571 | -52.69229 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65a669db-5b72-3197-9be5-8156ce185bea | -11.8716 | -56.869 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 757f3398-8a3a-3b85-8cda-ad7de42b6c35 | -15.93236 | -48.6049 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f183a819-f164-3717-9d4a-70819135e40c | -14.55985 | -46.69518 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e45b9d88-acd4-3205-9f49-9347f22e253b | -15.60052 | -52.55603 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fd0c547b-2eed-3ead-a91e-2d0d82bbe3b9 | -16.02593 | -51.05401 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4c5a77c-7e97-38cb-ab70-90a5340a4bcb | -13.26627 | -47.18575 | 2025-10-06 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09e2c868-8fa4-3280-8af3-50dc9a451cdc | -15.99919 | -50.84889 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddd4f2cb-e059-3652-9365-fefd743500df | -14.36232 | -47.7312 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e64bf27b-444f-35ab-a6ed-6b7018fc51cb | -15.59552 | -52.55536 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e8f54120-7292-3dc3-bb05-a7a6727a852b | -16.94367 | -52.67576 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dff88a3c-a35a-3b7d-a493-c79ce95b6594 | -14.67958 | -48.38029 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52f724a8-224e-3d1c-91ee-91206f4cfdd0 | -13.0509 | -47.91843 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dff3b2cb-3eb1-3fdf-9f9d-16014a96bde9 | -18.28175 | -53.3274 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fff9571-d42a-3ce3-ac9a-393f131e6fd1 | -12.89918 | -47.30205 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66ca53a4-c056-38cf-9243-36e2fbab49b1 | -12.37803 | -63.72632 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9486d807-c95a-395a-8db4-2f373aad797c | -14.69299 | -48.38127 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 93bfd9e3-1ba6-38ff-b2e0-1355ee2a9ec4 | -15.35802 | -47.99749 | 2025-10-06 05:18:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8801a649-3325-32de-a091-da3562b84d0a | -13.08066 | -47.82631 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c36d8299-66dd-361e-befb-f65e6561db14 | -14.84564 | -51.48087 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f48d35f-b3e9-3077-8d5c-622f4d916b37 | -12.8973 | -47.29847 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67f7525b-1634-3120-a644-75c80b498866 | -12.90475 | -47.29299 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8049e39-f1d6-3d8a-b8bf-3683f1d9ac2d | -12.38319 | -63.7182 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d92a828-4d4a-341f-937e-ba28d86387f5 | -14.87692 | -51.47863 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23f42134-d685-3dd4-b692-26222d5308f2 | -18.14429 | -53.4038 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2fc2206e-dc63-3776-a773-b305cbdc7a91 | -18.26876 | -53.33633 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fda564c6-506f-360b-82c2-990d801dac55 | -11.48426 | -59.09313 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91c90dc9-0a0a-3807-8da0-6c69f230b857 | -12.38244 | -63.72258 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 540a95ca-afe3-31ee-a730-9cec2a46cd64 | -13.0349 | -58.77436 | 2025-10-06 05:18:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b83505c3-7f65-33d0-bcd3-27a4afba88b8 | -14.9324 | -46.82353 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ece20333-d28b-3938-89f4-de403607c6bb | -16.15068 | -57.56604 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fc9dad28-ecea-3b9c-b299-73d9335ea0b5 | -14.6726 | -48.38433 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20dbef4b-f0ff-32c1-8caa-60669b594909 | -14.89627 | -51.49832 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 707e4b66-f267-3c94-8862-abc3ea633a2a | -13.32616 | -48.05111 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ec0e68d-5687-3686-9513-b4a6748d9bca | -15.82627 | -57.43801 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c8e82e7-110a-31a9-b55a-1d74666c32cc | -17.95858 | -48.55576 | 2025-10-06 05:18:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f5cfba9-3be7-381c-92a6-5f48eb6e8cae | -18.27122 | -53.33231 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98a6c075-1aa4-32ef-b263-7db322d00161 | -17.95192 | -48.5555 | 2025-10-06 05:18:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8e4556-5047-3541-9455-9a3dcf89bf48 | -15.61827 | -52.53575 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 537449d3-4c10-3428-8079-47bf13705b6d | -13.05739 | -47.91955 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f179bac-6fb7-3169-a657-882375e5c402 | -14.62003 | -52.5026 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3960c7df-3755-343b-b299-f26cca6ba816 | -12.37953 | -63.71755 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec87a3cb-92a8-3142-9a68-ba1415b8e4e7 | -13.25296 | -47.80927 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9586771d-42e9-3ba3-b9dc-80cde026c431 | -14.68591 | -48.38655 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50619ee7-5f0f-3c3e-8b6e-a09838aeacaa | -13.25962 | -48.47291 | 2025-10-06 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 413ca979-bbca-3827-a629-7d504b911410 | -15.21957 | -49.29318 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7b8a978a-cd0c-3643-b423-5c3963786a14 | -15.93182 | -48.61009 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 429600e4-859b-3e61-a455-de2dde9d8fda | -18.1797 | -53.37467 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5d00d0f8-4422-3ab0-83c2-757ee0b302f6 | -15.5681 | -52.445 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 653f8779-76a9-3150-b1d5-b6995ce6f7f4 | -13.05103 | -47.92219 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e12c03da-d6d4-3623-a174-143cde219941 | -15.99582 | -59.53305 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19efaa19-f3ad-3cea-8949-70df0f370bbc | -16.03388 | -51.03305 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99826a2e-5eab-33a6-bb50-da01b4f10cb9 | -15.21941 | -49.29033 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 173da7b3-06d7-3001-951b-aedf8a1962c3 | -15.18692 | -56.8358 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6beae37-4e1a-3904-9390-f4848645163d | -13.12126 | -47.99849 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6400dd2e-e7ca-3689-8372-372af2405249 | -15.98951 | -50.93425 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a670ede8-1882-3255-ab7f-93d713ea363a | -15.57924 | -52.4375 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64ed3838-9056-3196-bd6c-d26539cb49de | -15.31729 | -56.92385 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2832c2a3-a6f3-38aa-a018-a22053dc50f8 | -14.35942 | -47.72575 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e6e0003-38f5-3e7b-bacd-aa1691fe8982 | -15.20902 | -56.81506 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e1e756a-8fe1-3ee3-91f7-09f85365b185 | -14.87159 | -51.47795 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 12bb18f9-eb31-3dbc-bd44-80fc6f1ff2a5 | -13.05247 | -47.90384 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8f16ab7-6c73-3bcd-ac43-a0a92c037384 | -13.27827 | -47.63052 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2311a4a8-8178-39c8-8035-92983ba3bfa0 | -15.62829 | -52.53798 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e233633-8885-3bbb-972a-ed59d0bb6e6e | -14.54823 | -46.96034 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6da9a64d-e717-3a26-ad47-1674a96509fb | -16.15004 | -57.57064 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2891acf0-e2a3-3ddd-aef0-138abccfbd20 | -14.92952 | -46.82407 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 60a6a6e5-cc0b-332c-90b9-c69835e22999 | -14.61008 | -52.50162 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fd66b9b3-47cb-37c3-bff8-a5a9674b8b97 | -12.91551 | -54.73003 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d02a2d5-b2fc-3f0d-b418-725bcefddd2f | -13.68367 | -47.35411 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 959485f7-3048-3e23-bb79-96dde878c43d | -13.12016 | -48.00826 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d6ff062-cb9b-3bb2-be88-9c6328c0ba27 | -15.18751 | -56.8316 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73fc0c35-dc08-3244-b1b7-e7966094c9ff | -12.89524 | -54.75449 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 239b0534-e485-36dc-9a9f-617b276fbe57 | -14.63705 | -52.5274 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0e2259b-0638-3931-aac3-43c8ef229ac2 | -13.12666 | -48.009 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecb69188-4c73-3bd5-84d0-b1bdc13dd1f7 | -15.3367 | -47.31708 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56a076cb-ca02-3206-b338-e69883a5dd0b | -13.27928 | -47.62084 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4a74178-7bd5-303a-9941-6a94ef624547 | -11.87648 | -57.81667 | 2025-10-06 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9444b357-df4e-3c69-8c93-6a29d200cd70 | -18.13263 | -53.41874 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3d046226-76dc-369b-a9be-54c951db7d37 | -14.86627 | -51.47728 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 79666f25-2257-3e42-b206-c7503a7f48d1 | -13.08102 | -47.83369 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c25be59f-39c2-3145-a3e7-96e5d00f4b08 | -14.5619 | -46.67394 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README71.md)
