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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c590c787-92ea-3845-8d12-4c1bbeeee2d9 | -3.05728 | -51.06247 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d138f0-ba38-3401-b999-7c89a4f4cefe | -2.31623 | -51.96124 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb4496a9-6cf1-3902-843d-cdb2fafc4440 | -2.36511 | -54.35535 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e2092fd-761d-347f-9425-705b4929c0ca | -2.52367 | -54.26746 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e32f162c-3141-321d-bca3-461fbf1b58ff | -2.66521 | -48.7777 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a14dcea8-09bf-30fe-bb6d-1bf1654ab528 | -1.78721 | -52.74286 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d20f531-4e3a-3b4c-bd54-2cc05f549933 | -4.12398 | -60.93213 | 2024-11-29 05:22:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99c0d874-3c6e-368a-837e-fe745a56ac29 | -3.52997 | -50.54174 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6faf8a57-bc18-37cc-8e54-c69efa3de49a | -2.59795 | -53.97691 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 653f9ad4-8927-335c-92d6-c7fc88b70af4 | -2.86451 | -53.97932 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd1f139f-f1bc-33b2-a14e-13a1039cde5c | -2.65043 | -48.78536 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 3daae1d0-28b5-3d69-8656-92ef5cfaae68 | -1.60237 | -55.43139 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1ca19eb-4184-3457-bfaf-e2378e971a5b | -4.48077 | -48.19555 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37464a97-0dae-3941-8843-d33f5a24554f | -2.77166 | -54.08008 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13da04cb-7153-3101-83f7-f571c093ac7a | -1.68598 | -52.43173 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ff92ddaf-5c9b-39a2-a07a-fd1e1dd8ee01 | -3.19799 | -54.7411 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1733eb9-b337-3de6-ad04-c50fbfa3f141 | -4.11723 | -54.23583 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a972845b-ee43-3a4d-ab59-7d2de178a7fa | -1.93907 | -52.96085 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15d6106f-b3a6-33ec-bd3e-2a7c047f3db0 | -1.71288 | -52.49221 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b144d7e3-d9e5-3c74-8903-f03cbf967765 | -2.04024 | -54.69115 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f021f1be-0b0c-3b70-84d4-8c1f8ed5a9fe | -2.57455 | -54.29406 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7456848e-3465-357f-93cd-f727cf8e884f | -1.58901 | -53.83944 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| af236bf6-1361-34b2-870c-e44cb190908a | -3.10243 | -53.81027 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a95aca49-2d9a-3a5d-a40f-129679f13532 | -2.54971 | -55.22493 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fac4095-399b-31bc-b407-595e914fdc32 | -3.40687 | -49.52943 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae7f043b-9ba6-31d3-8668-839a42ce634e | -1.5842 | -53.84266 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f2e47be7-45bb-3f4a-84a0-f7cb8e0b4aec | -3.23792 | -53.93036 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aac040fd-e2ee-355a-ac7b-f50e293cb659 | -1.72281 | -52.48893 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9a5c3b1-5a09-355b-a48f-f1711520de8d | -2.80486 | -54.14355 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50868451-ad03-35b6-9810-8ebbf0d46da7 | -3.08488 | -50.25169 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6ddddf6-815e-30c5-8044-3f442e547b31 | -1.70381 | -52.76503 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 67251829-92d0-3e17-8cac-d19d265d20e6 | -2.85813 | -54.0221 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b54090b7-7460-3e9e-a670-dd7bc49adcb4 | -2.78608 | -52.86967 | 2024-11-29 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 780e1fa7-46f5-3513-9e04-9b3ffca261c6 | -2.62593 | -54.30501 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 975f770f-b822-3c87-82a3-dd0cb771ae91 | -3.38698 | -54.28288 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c4080b1-c857-3a8a-8819-66ea44c0dd56 | -3.19853 | -54.73751 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d219bcb-6b27-3e5e-8100-13205499808a | -3.11696 | -53.75797 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d166b9d-273e-3bc6-9edd-7b7a792c898a | -2.59313 | -53.98014 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28998448-a8fa-3e74-bad1-68a23baffbfe | -3.10743 | -53.82206 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b5f9d93-c415-309d-b917-4929cbbe33e8 | -2.90385 | -54.17437 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a2fcd95-90f2-3043-bedf-7c3a24b478a6 | -11.47009 | -56.8697 | 2024-11-29 05:22:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08dc1fc1-a81e-3f48-8954-3b240f759f80 | -3.72319 | -50.18861 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22691646-c671-3f39-a01f-563ebade5746 | -8.13328 | -47.98628 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c39e572-6230-3a3d-b43e-9cccb1087ee9 | -2.78471 | -51.71941 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ad10e3-2e7a-3f28-b648-850ec1e17fab | -3.29111 | -53.27463 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65cb3457-a1ee-376e-8814-06a4220a2be4 | -3.34475 | -50.23701 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0158f62f-0f3e-3330-86a3-91845a1eda44 | -2.60681 | -54.2067 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed198a09-065b-3671-9170-665567f55707 | -1.64637 | -52.74693 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c2066add-45fc-39ce-bdca-f9843d951cab | -11.36236 | -56.20671 | 2024-11-29 05:22:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90bae3ac-da73-3531-955f-757491b32a26 | -1.82489 | -52.07448 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3e5c2b9-8bce-35ea-9f51-7fee8965a67b | -3.46527 | -50.52267 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc952a5-15ba-3bf7-9204-78a6dac160e8 | -4.48148 | -48.19613 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b57ff8ff-b8fb-3ea2-9cd9-615620e46e8e | -3.35369 | -50.51535 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1345ecf9-99aa-3823-a411-08394b04562b | -2.82623 | -54.03316 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1da7eff-eb62-394d-8a13-7ff411a3221b | -3.03989 | -54.04466 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c512b799-3fe1-3d78-a3e9-77d95344731f | -3.05394 | -52.76435 | 2024-11-29 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e482460-c69f-3990-80b4-faf6fc488361 | -3.07731 | -50.96574 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dba36a3-b910-3e05-a7aa-d1c398f97ebe | -2.23362 | -53.68732 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0ceedaf-7bc3-31fa-8907-09e889ee8889 | -3.33754 | -53.20917 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7d98c6ca-2716-3187-adb4-8d8ae51fc9f9 | -7.97842 | -55.3022 | 2024-11-29 05:22:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abb1e58c-832c-3e22-b83d-8bb6ef85c0e7 | -4.10579 | -50.98164 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce17fed-0c8b-3a1b-8193-2977a28f1604 | -3.07594 | -53.91636 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0b786bb-2222-3659-b3b7-f95512ed0908 | -3.50242 | -53.80866 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b31692e9-5f1a-3da2-9ff2-7b78a5f9c9f2 | -1.68687 | -52.45617 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46a1c34b-0c2c-3f47-8d9f-8daf9afb2d13 | -1.94427 | -52.97284 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47fc2b82-9174-3020-80d3-e7d62e1c721f | -3.39173 | -54.27971 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18da87e4-dc71-3e04-b349-2da35affda8e | -2.96043 | -53.72045 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3046edc1-4646-3127-97fc-cf6e39262179 | -4.05866 | -49.07014 | 2024-11-29 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a19cec0a-bf4f-3e30-9928-d4bb9d502b49 | -2.95923 | -51.00606 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b64d32db-3fb5-32b3-84d4-71b9e5eb6086 | -2.96844 | -53.72582 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e7a5fad-f09f-3af9-8b6c-0a0770783e9e | -2.9771 | -53.28252 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0ad184db-04c1-3b35-8398-c8bf34b2fdf2 | -2.36456 | -54.35898 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbfe1395-6070-3668-b721-943e9825c721 | -2.75636 | -54.12451 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe8fef2f-ce54-39dd-ba93-8d7b711b0ff1 | -2.76656 | -55.32273 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44d8f2e4-6984-3c81-9ad9-a74c86db78bd | -1.49948 | -54.46245 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e3319a5-e1f7-342c-be7e-4e3091b6d245 | -3.67077 | -54.28418 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1cbfd2c7-8901-39eb-b221-467348c0b9be | -3.06869 | -50.98728 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d54bd8d3-8238-3e41-9163-bfc8209461e9 | -3.0969 | -53.25858 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcdeb91f-45ef-3073-a5f7-17da1032e7f5 | -3.38626 | -50.10931 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99f73021-5933-349e-aea3-91e8e1423506 | -3.35898 | -50.40607 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1974567b-c68e-3e3f-9d66-83b0dccd6bd8 | -1.69942 | -52.45621 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 31c18195-969c-3218-9c96-bf2cd75e4ff0 | -3.61057 | -50.18767 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1531d547-c170-3215-8ee8-fe9f1c1c2807 | -5.1809 | -60.26084 | 2024-11-29 05:22:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48ab6a7e-239b-36d7-8b51-26bd0dd7d791 | -1.88943 | -53.30754 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f19a3de7-e0ef-36e8-8484-6b2a4198f060 | -1.99257 | -54.89611 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b4b752fe-d6b8-3bd6-b9bc-c4c792697147 | -2.65729 | -48.78996 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 06402393-b2fc-3a03-82f4-b5fea8e8cb14 | -2.36759 | -56.11922 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1de51f5-0b80-3427-8dfb-a3ec02542160 | -3.86359 | -50.15131 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b376a481-ba6a-3391-bc6e-530938f8f08b | -2.88829 | -54.16422 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ea0a42a-550c-3bf7-a7f9-874f7f23caf5 | -3.32566 | -50.22044 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b7c6ffd-a8c3-3c1d-92c1-b821c0b55b5e | -2.89135 | -51.586 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11dca73b-9101-380b-ae1e-bffda6690214 | -2.46109 | -55.28351 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bab79a5c-fb46-3029-a0bb-332d76001a9c | -2.98561 | -51.32828 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0e6e2de-2f8a-343e-a4a8-15f906b372a9 | -1.36365 | -55.18401 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe31569e-b83b-3105-89e4-714c6686a79b | -2.83471 | -54.11703 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dc5adeb-a32c-36d0-81bb-ed0e3ac3f10b | -2.82985 | -54.03766 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5eefeab2-e10c-372a-97b1-c850c12e2aaf | -2.46164 | -53.96847 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5bc6bdc-74c7-3c07-8f94-92c6fe66e7a7 | -2.88028 | -53.98973 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e165c5c8-8d7e-331c-a9f2-40ddfe784b28 | -4.43409 | -46.58672 | 2024-11-29 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| e2f709c9-8337-3a6e-ba77-8a4f21b9d580 | -3.96781 | -48.91886 | 2024-11-29 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README97.md)
