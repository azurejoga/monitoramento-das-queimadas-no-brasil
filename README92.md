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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43abe3c2-94ab-3320-8705-37fc1a92c9c2 | -16.07291 | -59.70687 | 2024-11-28 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 434f4ec7-35d5-3027-9fd3-bd1d9a040eb6 | -16.12835 | -59.63815 | 2024-11-28 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fe83687-f20b-390a-a37a-b464a68bee54 | -21.60538 | -57.49937 | 2024-11-28 05:22:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc114065-8dd6-393a-aa6e-13a267c5890f | -17.63799 | -57.57647 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 55cb15a6-b7ab-3aa5-b2e6-6bdb838db728 | -19.88344 | -54.812 | 2024-11-28 05:22:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b315118-dee0-38e1-aa35-e36b0ca528fd | -18.67631 | -54.99091 | 2024-11-28 05:22:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 877cecb9-b324-33d6-a41e-b7b2feec6e47 | -18.77463 | -55.83842 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3290e319-558e-3d6b-8514-106f0191c8ed | -17.57657 | -57.60498 | 2024-11-28 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2eed367e-d69c-3a43-81d0-f909a0eb771e | -18.77788 | -55.84751 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 388884b2-848f-3ef1-9711-015082cbc973 | -16.16413 | -59.61172 | 2024-11-28 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d6e77b1-a479-387c-a55c-1d0d6356d209 | -17.56686 | -57.47481 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 700b8bd5-654c-37ba-9c11-7b713e13eacd | -21.29505 | -50.58423 | 2024-11-28 05:22:00 | NOAA-21 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d27f5ec8-4ed5-3839-913f-e1a0c954b99b | -18.7784 | -55.84327 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e24c2f9d-0c70-3c62-8230-f4f74d8d40f7 | -20.12681 | -53.3203 | 2024-11-28 05:22:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9110cf13-5986-31a2-8831-5de02cbcd18d | -18.77085 | -55.83358 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bdb49d74-8a0b-3e57-bb18-ddafc1a73f56 | -17.23205 | -54.43994 | 2024-11-28 05:22:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e89d2e28-7040-3411-ab52-b8421bc9a749 | -17.56304 | -57.47425 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2586988f-049b-34ee-a3ed-ccf180d73d4e | -18.78323 | -55.83961 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e45b74f0-9788-34b9-b0cb-a1e8adacf70c | -19.7231 | -53.63237 | 2024-11-28 05:22:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 332edf13-4b98-3386-9d18-40327ac5b719 | -16.08098 | -60.10529 | 2024-11-28 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a9e336a-b5aa-3cef-ba3c-982805ea5ddd | -20.72013 | -54.43418 | 2024-11-28 05:22:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ec3746d4-4a5b-38fc-b350-8e3046029610 | -20.6304 | -56.58714 | 2024-11-28 05:22:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9aad2930-918c-3c56-bf0c-f20b595d8c3d | -17.54463 | -57.43649 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e25a281e-9a59-3c41-b5fa-2355ef039138 | -18.7827 | -55.84386 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 07acbf99-f29f-3e73-bb17-9f550d837e03 | -17.57636 | -57.49117 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d710784f-21ba-34d2-b6f8-8c11b0c0c64f | -15.53084 | -59.08424 | 2024-11-28 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 454cecc0-f4a7-32e2-bd37-14cf33b847b1 | -16.07989 | -60.11269 | 2024-11-28 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 996b8d78-f307-3032-a0cc-69bbb50802b6 | -17.64303 | -57.59695 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 11d50fa7-e35c-3c10-a95c-f992f9b36d47 | -18.77359 | -55.84692 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3acc43ae-7e2f-3543-bd84-1fbf77bc9dbc | -17.6418 | -57.57703 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e98b0254-a08b-31df-b3d9-f73747a591f2 | -21.60584 | -57.49577 | 2024-11-28 05:22:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6300a699-c8cf-3810-99aa-1e794c07d459 | -18.77033 | -55.83783 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 63f81d88-5c70-30c0-897a-d30dfdb11caf | -17.63356 | -57.58074 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| de356a78-4bc9-3dd5-be8f-fb311c99ba17 | -18.77516 | -55.83417 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9bfe3edc-a7d4-3f4b-a61b-88e0c519f09a | -19.97381 | -55.09249 | 2024-11-28 05:22:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1c57617a-8561-3c05-8b67-71865a2b7c6b | -19.55548 | -56.71354 | 2024-11-28 05:22:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3d7ed4fe-0079-32a0-9956-b73394d5e1a7 | -17.63736 | -57.58131 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 40cf987e-de04-3561-968e-6c83c396ee78 | -17.57722 | -57.60017 | 2024-11-28 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| af467fa0-87a0-31a0-89b8-7d503bbfa377 | -16.07762 | -60.10475 | 2024-11-28 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 547d373a-ed1d-3bb0-ba57-5979422a7606 | -16.12495 | -59.63761 | 2024-11-28 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac0f8ed9-1941-3d5d-b354-47d2a01df379 | -16.07927 | -60.09365 | 2024-11-28 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 689f7f4f-a7a1-38fc-a04b-45146fc88305 | -16.08043 | -60.10899 | 2024-11-28 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e79ce9b-c38e-36ad-a091-3562ba4d051c | -20.13196 | -53.32111 | 2024-11-28 05:22:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9223c848-53d6-3b26-bfdf-68819ab89afc | -17.6456 | -57.57759 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5bc87c7d-4c69-3123-bdbd-9f0de6e61b26 | -19.55597 | -56.70968 | 2024-11-28 05:22:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a536038c-974e-3f8c-8f76-3196d4ada498 | -16.16072 | -59.61119 | 2024-11-28 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec5a2bc8-4134-3982-8242-be607af2d0c2 | -18.77893 | -55.83902 | 2024-11-28 05:22:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 140274a4-f588-3fcf-bd8c-2e401ba45b25 | -21.29549 | -50.57888 | 2024-11-28 05:22:00 | NOAA-21 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6ae7300f-74a7-3a4f-8646-2f096d088674 | -16.07707 | -60.10845 | 2024-11-28 05:22:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c28a749-e6e9-3f63-96e9-600abc6713c0 | -17.58101 | -57.60073 | 2024-11-28 05:22:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d718a7e0-0d2d-35cb-9e4b-8e0ab6c8c986 | -17.5572 | -57.51817 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 163895ec-012d-3ac6-b054-59d0f04924b8 | -17.63419 | -57.57589 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6c4c6bd3-13df-3c5c-9e66-76e1e3ee16d7 | -17.62976 | -57.58017 | 2024-11-28 05:22:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 73500637-672d-34ea-9659-e76492ec6e77 | -15.69265 | -59.14774 | 2024-11-28 05:22:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ef07b85-a768-3829-ab16-c20c818bccfe | -19.88558 | -54.81126 | 2024-11-28 05:22:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2483292d-6844-3ef8-a73e-aaec7bcd517b | -16.07631 | -59.70741 | 2024-11-28 05:22:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09d288a8-c312-338c-8bd6-ab4ec261eec7 | -5.979 | -45.3395 | 2024-11-28 05:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| fc27cc26-c46d-320f-868b-327838a403e5 | -3.3852 | -45.8465 | 2024-11-28 05:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 19ff3712-5aca-3c06-b75e-5a1e316e3738 | -5.9788 | -45.3621 | 2024-11-28 05:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 170.6 |
| c09aabef-e9b8-32c1-a40c-6a87b2ca8489 | -3.3853 | -45.8241 | 2024-11-28 05:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 9e637c52-91a5-3606-af39-dee6e6ad103b | -3.3837 | -50.1125 | 2024-11-28 05:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 725be15c-0a52-3696-80ad-99b92700d277 | -6.1735 | -42.6221 | 2024-11-28 05:30:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 18c6d899-9a82-35ca-bca8-143a9bdff199 | 0.97697 | -50.12706 | 2024-11-28 05:37:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 39083b48-0d31-3c39-9274-5c95d3898a3b | 4.37588 | -60.81923 | 2024-11-28 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bb338c1-1136-35ec-ba92-24a1449a4e57 | 0.98397 | -50.12578 | 2024-11-28 05:37:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f8fc3d7-6f24-3ed7-9aff-d321e0b0708b | 2.09086 | -50.62336 | 2024-11-28 05:37:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b82f3ce3-226d-3f3b-bf1c-8b38e7af00eb | 2.17334 | -56.02777 | 2024-11-28 05:37:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd7fe415-410d-33a0-845d-065cc1e17c9c | 0.98472 | -50.2608 | 2024-11-28 05:37:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8834980d-e6f9-3988-be27-ec9a4b589e8b | 2.09185 | -50.62917 | 2024-11-28 05:37:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b25236c-8a7c-3d79-aef6-7dfacc0b588f | 4.65227 | -60.51599 | 2024-11-28 05:37:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3b77d6d-166b-3f7f-baa3-15a90086e7ff | 4.37242 | -60.81959 | 2024-11-28 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65acbdff-31e8-36c7-9600-0777b77a7829 | 1.72175 | -55.80386 | 2024-11-28 05:37:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 679efe38-4e92-32ea-90d8-82e285cbb127 | 2.08929 | -50.62656 | 2024-11-28 05:37:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76e08a59-ec72-34dc-a326-6b44cd2bbf7b | -1.5897 | -52.271 | 2024-11-28 05:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6783136b-d620-3232-8e78-cf760000e0b5 | -5.979 | -45.3395 | 2024-11-28 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 90fc470a-a35b-3dff-a9a6-dfda4b917da4 | -5.9975 | -45.3607 | 2024-11-28 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ac5eddc2-d006-3ff6-9a4f-e75b1ab8ba95 | -5.9788 | -45.3621 | 2024-11-28 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| c55539bf-dd22-3724-8951-51a5f4295c85 | -3.3853 | -45.8241 | 2024-11-28 05:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 2577eec9-1c1a-311b-bfed-17c238e3ecf8 | -3.3852 | -45.8465 | 2024-11-28 05:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 180.8 |
| d333bfff-0621-32b7-8fc5-bd63627f69be | -3.1113 | -53.8242 | 2024-11-28 05:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 3e6e8c63-63ec-3d4a-b68b-d3e00b26bf75 | -3.3837 | -50.1125 | 2024-11-28 05:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 904b8359-30b8-36a1-974e-924a7baefaea | -6.1735 | -42.6221 | 2024-11-28 05:40:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| ff8d8b70-756c-3bb6-86de-5bfc059d21f8 | -3.3666 | -45.8472 | 2024-11-28 05:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| eb05c99a-f6e8-3984-8a53-8ccf222a3ba9 | -3.40227 | -54.28151 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45732ad6-105d-3e6d-aeb8-22edac19bbaf | -2.98876 | -51.44909 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 55b0941e-9775-31e1-85d7-76c6e08687c1 | 1.25563 | -55.91773 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c952571-0df3-364b-bd32-6ea87f62497c | -1.65918 | -55.23481 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab39f571-0541-34b8-8ce3-6e6da5c866ab | -1.60403 | -55.38115 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fce60581-a15d-32a5-81e8-82d4cbd23e2d | -3.09877 | -53.73306 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a4c6aba-b7c4-31f1-a5a9-eb5febb70feb | -1.64831 | -52.73435 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5650ec98-0beb-3cf5-b8a2-b10cd1508c78 | 1.44567 | -55.90715 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 462ee528-ee08-390e-8b57-9b4860f23239 | -1.70138 | -52.76234 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d345523-151c-323f-b48e-2dbc2b07d4e7 | -1.10254 | -54.14761 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d280019-fc3d-3980-8c66-35a816525e24 | -1.66499 | -55.23236 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24b407e2-7f3a-3564-a14e-22f39e5ed266 | -2.60283 | -53.96831 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91bd0648-86e4-32d5-9c2b-09f7b76375bf | 1.25425 | -55.96205 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 326992d6-be7d-37cf-8897-661ab14a0c1d | -3.11942 | -53.75841 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a5e1cba-9480-34fd-b64d-e34d1875a703 | -3.06065 | -51.05685 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13247dc6-2270-3a95-b976-ce6caf0950a3 | -3.50131 | -50.49421 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bcc7c61-b381-3e73-8b3a-a92955d8ec9a | -2.26325 | -53.4692 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README93.md)
