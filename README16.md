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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 586bc771-7b3c-34aa-80d1-d828997f97d3 | -6.3481 | -57.765099 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f692efe-3097-3bab-8074-b2b81bba13d8 | -3.2931 | -57.8517 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eca6195e-d07a-3f14-b491-37d9e483b969 | -8.2453 | -55.285801 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd336a1-6703-3841-8d46-6cf4204368c6 | -6.6457 | -59.919399 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 574fafbc-2b8f-3c6a-9623-c6f297d0fa53 | -18.733 | -46.940102 | 2026-09-22 01:19:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63d3de82-25ea-353d-94be-5a8d38143cf1 | -10.4643 | -51.290798 | 2026-09-22 01:19:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66638632-e0b4-361e-bfd9-fffef4d2c17e | -3.1197 | -60.683601 | 2026-09-22 01:19:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0c3a31-6e25-3917-bb94-41ec6d297eac | -9.6593 | -54.3274 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd97232d-c084-3c9f-a62b-da2c0ad9656a | -5.1304 | -60.279499 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66acf38f-8afb-3a3f-85e5-4ed1bcd1f4a4 | -10.6216 | -53.9884 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08b43073-e9a3-3dbb-ab16-d3d94eba2c2b | -2.5742 | -57.509602 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6cce913-a62b-3db1-9273-669cf5a233a8 | -6.3861 | -55.282799 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5903b6-e3d9-3941-9760-35640f21df0a | -12.1519 | -47.368099 | 2026-09-22 01:19:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99e3985c-4bb1-38df-a1eb-ef6b12d09fba | -3.4023 | -59.532101 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a84db47-c133-3722-9e44-ebbb5b332b53 | -10.8742 | -57.166599 | 2026-09-22 01:19:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2668562e-1015-320f-95bf-58978f51d7e1 | -9.3028 | -58.912498 | 2026-09-22 01:19:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9334c7de-c958-3365-8a07-73aee527dc6b | -6.5533 | -56.034801 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aac4f380-dd4a-385d-acb7-0917c6df6b3a | -3.3901 | -56.937 | 2026-09-22 01:19:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a73543c-c59b-3d14-9319-98dc2ba8966f | -7.7288 | -61.257702 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f55ff2d9-f911-30b8-b06b-f818d5640a8a | -3.2253 | -53.953499 | 2026-09-22 01:19:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee17ce0-6a36-3ed7-80ce-c2edeff5158d | -6.7145 | -59.451099 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd70fad-d47a-31b0-9347-901306d20c27 | -2.8689 | -57.8022 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75f6353d-c8bf-3d4d-9e9a-2a3a1e450047 | -4.4855 | -55.492298 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd0bac5-7ca8-3220-b7c0-a1236e540472 | -12.8945 | -52.074501 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f9643bf-bdf2-3ad7-9bbf-c0e868cb922e | -6.1411 | -59.9659 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e89f4d8-c3d2-3182-97d8-a969eed649a7 | -6.285 | -59.919102 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53528684-00d1-3562-90ca-b87e2f991120 | -4.4149 | -55.4991 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 291619c6-e0be-3d2c-904c-ddd6d47e3897 | -3.3909 | -59.5275 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21274d6c-c556-3102-ae3b-9849cdac6a72 | -6.7263 | -55.063702 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8caf7bb-da6e-3371-9523-6bd57a118b78 | -4.2178 | -48.6092 | 2026-09-22 01:19:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a71f629a-b52b-3616-b567-d81fa18da614 | -7.7173 | -61.251999 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b17e3d5-2ef2-358d-b170-ddc03e228f3f | -6.3468 | -59.9641 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03b47b27-5fe3-360a-963b-98e0b54178b3 | -4.5562 | -54.918598 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07e62501-c4c2-3a15-bc72-a718c2e69dcf | -3.7063 | -60.633598 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c03770a3-11ee-3463-8770-8f7d1d243b00 | -6.6945 | -56.1525 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83b3c796-b45d-362b-b7d3-7488ebd1daa1 | -6.6163 | -59.925999 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1ea591-18bb-394b-aca4-bafad26ffeb9 | -12.8236 | -54.0284 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28d67560-af51-33ab-91ee-f88a5a0ab677 | -6.456 | -59.991199 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 878aeda4-e040-3346-a472-2b4e926d9430 | 1.0793 | -60.677799 | 2026-09-22 01:19:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b888f7c9-8775-32ca-9b8e-c8e197f6a322 | -12.9359 | -51.0429 | 2026-09-22 01:19:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b97dd6b-f6a6-399b-9f13-49a53b16da4a | -6.6261 | -59.923801 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 120a02ae-ec43-3e9d-a305-515feafe9c54 | -6.2563 | -55.4319 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 834799f6-c835-3d80-aeed-023ce70d13bd | -2.6696 | -54.9589 | 2026-09-22 01:19:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d978a74-a2f6-3bd4-8b37-54ee0cc54b70 | -3.187 | -57.883301 | 2026-09-22 01:19:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c297bdc4-02e9-30a2-98af-f83640e9d25e | -3.405 | -59.588799 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe199c7e-631a-3049-915f-e3a02cf29a24 | -3.6071 | -60.560398 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eae1156a-9779-3cce-8720-244fc7595c55 | -11.0316 | -54.145199 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee09fdcf-f1bc-3359-8047-81290e066a41 | -3.7809 | -60.734798 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d44e34f-8173-37e6-a9aa-ebf9e1481b7c | -12.1423 | -47.3708 | 2026-09-22 01:19:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08acccbd-3e32-3e50-8f3a-d5875f8015a0 | -6.7758 | -55.490002 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e68ee5b-38e9-31d5-ab3a-c158b71dd7a7 | -6.7475 | -59.4147 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0fa705-0266-321b-b9ff-02aee5349243 | -9.293 | -58.9147 | 2026-09-22 01:19:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd1ead0-5bf1-3f65-9b38-6847895d17b4 | -3.3468 | -59.8741 | 2026-09-22 01:19:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c011a70d-5a69-33be-ad24-65507432ab04 | -3.6935 | -60.577702 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87d3c655-cb0f-3b37-b271-db3c6b481f5e | -13.2905 | -51.794399 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0854caf7-71eb-3dbd-ac4b-58c3a2462a3a | -6.5301 | -55.367901 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50b9ea6-5ef7-3d52-851c-0131841268c4 | -7.3396 | -55.603699 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd859fd3-a290-3e31-b315-27197b3975f8 | -8.2609 | -55.2645 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a103fe4a-63ef-32d2-8ba1-2653850631a9 | -3.2948 | -57.858898 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 975bc33b-a989-3621-ba41-c58ddcbdaa7d | -2.9409 | -57.801201 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| abf18f08-bc3c-3fdf-a195-b0da874cfc82 | 0.167 | -60.6525 | 2026-09-22 01:19:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ba9686cc-9ed7-3f07-ae05-35369cd454f9 | -3.4608 | -58.397999 | 2026-09-22 01:19:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc6c784-d582-3a1c-b6ff-210a6c411312 | -5.9386 | -59.9818 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4513abb-273d-37e3-8812-f35844aab7e8 | -3.4851 | -59.577999 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8a9526-0391-3177-8949-1754ed523ae0 | -6.4355 | -55.6227 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ab01cf7-e5a8-3777-9e28-4a6a268867df | 0.7919 | -59.1903 | 2026-09-22 01:19:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2f9d049e-1116-34ea-ab0e-cd877cb6fc21 | -3.7825 | -60.741901 | 2026-09-22 01:19:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2cda6ecd-9d75-3fd8-bdba-f0de225e4026 | -7.6094 | -55.3475 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d461046-86a3-332f-a673-189aa458c709 | -9.9493 | -53.986401 | 2026-09-22 01:19:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6462b78f-8702-32d1-97a6-d998e0ff486e | -3.419 | -61.317101 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 848333c5-3f64-3d32-805a-0dec8d098de1 | -10.6043 | -54.0023 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 128e4705-0216-3a9f-bc56-1643b7cfd09f | -3.4969 | -59.181099 | 2026-09-22 01:19:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5b3b762-89ab-3b83-929f-424c8d66c617 | -12.7845 | -54.037998 | 2026-09-22 01:19:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0082692-7e3c-3f4a-8bd0-0ea327259c52 | -5.9149 | -55.690899 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5868f10d-b71d-3f53-90bf-962513cd6431 | -4.4178 | -55.249001 | 2026-09-22 01:19:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7bd913f-46f0-38a1-a220-7fb6f2096b19 | -3.48 | -59.600601 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae338768-643d-3cc9-957e-8abda134acc7 | -5.9821 | -57.7001 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3650a89-f650-3522-b144-10335b0a1ada | -6.7376 | -59.416901 | 2026-09-22 01:19:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed2a20f-57b8-3e71-9eda-d9a98078cf49 | -4.6816 | -55.6241 | 2026-09-22 01:19:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef14b2e-41d5-3539-9534-365954699dd1 | -6.8366 | -55.528999 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982c943e-bbf9-3fd4-aa49-e2d8124a7a60 | -6.3641 | -58.281399 | 2026-09-22 01:19:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab4a7447-a8f8-308a-b7ac-2c09d196650d | -6.7284 | -55.072601 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69cc0cab-0ab4-3d92-b759-1c4215f637c8 | -6.1433 | -59.8848 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2b0be6-4b46-3ba8-8096-56dc6af24589 | -6.7305 | -55.081402 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86004f22-0f0f-3d3e-8fd9-b276336a651a | -2.4116 | -58.277802 | 2026-09-22 01:19:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b93887c-6c19-3fa9-8d4f-2bfb7ca4fb17 | -8.2492 | -55.2584 | 2026-09-22 01:19:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab400292-9fdf-3cf8-b55a-37b9f4e0d2cd | -8.617 | -54.634399 | 2026-09-22 01:19:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a723064-4250-3782-8431-5f1e3285a566 | -13.3031 | -51.8032 | 2026-09-22 01:19:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14e1aa37-a3fc-3089-8ee7-c9f074116d13 | -9.6886 | -54.3204 | 2026-09-22 01:19:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe15f316-cdac-3286-a79e-90f69762c417 | -10.6141 | -53.999901 | 2026-09-22 01:19:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f129149-3368-3c10-9640-af31ec047ed9 | -6.1585 | -57.704498 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8cafa17-5940-3a5b-99bd-1e10a5de633e | -3.4034 | -59.582001 | 2026-09-22 01:19:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a31efba6-c4c1-3652-9eef-752899bd015e | -6.4544 | -59.9842 | 2026-09-22 01:19:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73a4676c-71e6-3cac-b071-0956d23eb921 | -3.4174 | -61.309898 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21685c60-0188-3a58-8121-0e48437bed29 | 1.5361 | -55.899502 | 2026-09-22 01:19:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcc97616-9b06-3f72-a67e-e078c266c710 | -2.9311 | -57.803501 | 2026-09-22 01:19:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13950aa7-b724-380d-8b9d-c899c61bdfe1 | -3.3634 | -61.299099 | 2026-09-22 01:19:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14fcb724-b693-3126-a970-5755557bd25a | -6.2026 | -57.7612 | 2026-09-22 01:19:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a17c433d-6f44-3ec9-be83-38938ec20ba5 | -6.6359 | -59.9216 | 2026-09-22 01:19:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37c897c9-86a5-3d68-9afc-13cd7575ae49 | -1.9311 | -56.605301 | 2026-09-22 01:19:00 | METOP-C | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
