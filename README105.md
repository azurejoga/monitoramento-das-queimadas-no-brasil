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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61357a56-ebf0-32c2-91be-4b2c850b793d | -10.844 | -45.3356 | 2026-08-31 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 6776544b-d441-34a8-aff6-82782b67b7df | -6.6542 | -59.426 | 2026-08-31 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 225f3915-b13a-3ecb-a096-bb1071a2b121 | -19.0948 | -57.3641 | 2026-08-31 16:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 239.5 |
| e54165de-8a7b-3f26-8d61-fc5c8acf9ece | -6.77 | -55.6445 | 2026-08-31 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 27095812-4628-3d80-8313-d2442a40b945 | -10.1528 | -45.7665 | 2026-08-31 16:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 923ab551-3762-34a9-86a4-6bc498c6fad6 | -9.4339 | -45.6931 | 2026-08-31 16:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| ae509cbd-5850-3bcb-8a81-1faa73910d48 | -8.9253 | -66.9477 | 2026-08-31 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 9dee50c3-2046-3bb0-a7a2-f31c0affb463 | -7.0242 | -59.2374 | 2026-08-31 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 20335b9a-4fca-308c-bf56-48087d34ceda | -6.1295 | -57.6637 | 2026-08-31 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6eade885-b546-3e96-939c-4b797a068655 | -19.0944 | -57.3849 | 2026-08-31 16:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 466.8 |
| b11866bf-172b-3678-994c-a7bf81cedb0c | -3.8114 | -65.0747 | 2026-08-31 16:10:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8961e0e0-df57-3008-87e9-adcb3943d9df | -8.5555 | -66.9574 | 2026-08-31 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 0fa94ab3-890f-381a-8d1e-71adfe668585 | -7.1823 | -60.6522 | 2026-08-31 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| ae29b0aa-5dac-31bc-8e69-fcb26abd87e7 | -5.5647 | -60.2312 | 2026-08-31 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a74a033b-4f9e-3171-b0d3-e6c9a635029f | -7.529 | -61.3635 | 2026-08-31 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 76912bbd-edbd-3e67-9bb3-67ac3973a767 | -9.7126 | -65.0951 | 2026-08-31 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7b290afe-3c5f-3dd1-aef7-d58aa514e894 | -13.4901 | -57.0355 | 2026-08-31 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 166.9 |
| f8a8e0a2-4f0d-3215-a728-3fcc75505d96 | -12.9221 | -45.8582 | 2026-08-31 16:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 4eeb7a7a-c6ec-3b0a-be57-9bdd04fc4ac6 | -10.8215 | -50.6519 | 2026-08-31 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.5 |
| b0f4c870-64cc-3441-9f73-dde91d43ff81 | -8.87 | -66.8935 | 2026-08-31 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 02cd6666-d9f8-3b75-a774-22174ba80eff | -11.6786 | -54.5484 | 2026-08-31 16:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 95928ba0-9903-32a3-8b34-8079b6b0b1cc | -7.3478 | -55.1744 | 2026-08-31 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 9ed71d8f-4ac8-3229-8c69-b31896c7e261 | -7.9239 | -44.2327 | 2026-08-31 16:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| d80e9c02-6580-3452-b4a9-e95cafd533dd | -7.685 | -63.3255 | 2026-08-31 16:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8639f559-56ee-3f3c-abe9-41beb237a25f | -10.7268 | -50.6618 | 2026-08-31 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2b8be687-2ee7-38b5-af94-e4e35f1e0b74 | -12.1711 | -50.5432 | 2026-08-31 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 94d4f965-aee4-3e38-ac63-c4becd8593d5 | -6.861 | -41.6772 | 2026-08-31 16:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| cea06336-6bea-3372-8dc8-43c56f68411e | -19.0744 | -57.3876 | 2026-08-31 16:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 5d8c1b17-4cf2-3855-8e6e-f229cbcc0764 | -11.3427 | -45.1751 | 2026-08-31 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 81ad961a-6c98-318a-b31e-0cfe4f8676f9 | -10.1531 | -45.7438 | 2026-08-31 16:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 37fb9261-5285-3a90-aa27-338d8aed8cd4 | -9.6676 | -47.9429 | 2026-08-31 16:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 182.1 |
| a4107c4c-103e-321b-85df-75490f417be9 | -14.9858 | -48.1529 | 2026-08-31 16:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b404dcf7-ffe2-3755-b9b4-f8d134019ece | -13.4516 | -57.0592 | 2026-08-31 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7a87aabd-e715-37da-bd7c-96047faf242c | -9.7873 | -59.4479 | 2026-08-31 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a95e6aa9-0a3a-3604-a9d5-91712746996b | -8.8207 | -71.243 | 2026-08-31 16:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e5200707-b200-30c9-b4b3-574ee5a7c339 | -8.2043 | -54.9423 | 2026-08-31 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 389a02d8-ee10-3ec8-9e51-a3da42d2968b | -2.6741 | -59.382 | 2026-08-31 16:10:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8cefb9d4-de70-3eb0-83dc-35f0e8b950f4 | -10.5607 | -50.3595 | 2026-08-31 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 3b3e12da-1756-35e8-89a5-580613dc9f50 | -3.6216 | -60.547 | 2026-08-31 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 54c6940a-e8fc-3726-b243-fd041d826817 | -3.1839 | -60.1559 | 2026-08-31 16:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 902e4a61-f36e-3821-b6fa-d383a159ef5b | -11.2125 | -54.0181 | 2026-08-31 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| c8a5f874-0bf3-3753-a595-8cbe2a5b9f6e | -10.8614 | -50.4985 | 2026-08-31 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| cca981e9-a913-35c0-a564-19da79072d14 | -3.4002 | -61.3465 | 2026-08-31 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 97a37c5a-ffa2-345d-a2be-d3ac68dfc8ca | -11.1824 | -50.5706 | 2026-08-31 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| b88402c5-6888-34e4-a69a-106a02d8c89f | -3.6399 | -60.5466 | 2026-08-31 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d8629a87-1b93-337e-99e1-f428149f76e5 | -8.7631 | -46.4418 | 2026-08-31 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 319.2 |
| 998cfd88-dc1c-3481-9d98-7b5260888a5f | -19.1536 | -57.4186 | 2026-08-31 16:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 218.8 |
| 33351b09-2670-3308-902e-9f403627f6b6 | -10.7081 | -50.6425 | 2026-08-31 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c0de9fba-ca9a-34cb-bb79-f0c434220020 | -10.7856 | -50.5066 | 2026-08-31 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| bba0275d-343f-3900-b332-1056bad39a55 | -10.1538 | -45.6982 | 2026-08-31 16:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 210c0d85-98cc-3e0e-9956-3fb76b331091 | -9.173 | -59.3659 | 2026-08-31 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6c61a8f9-ac66-3f86-9b00-47a302293e03 | -8.1671 | -54.9447 | 2026-08-31 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c24025ea-1fae-3623-b566-678034aa9cd1 | -8.7442 | -46.4437 | 2026-08-31 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.8 |
| eb255986-5f16-3b98-bdf9-90be5aea5b5e | -5.4876 | -57.1416 | 2026-08-31 16:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 624ed96f-f2a8-33e2-bf57-6abef8a6b8ee | -10.3202 | -49.9782 | 2026-08-31 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| aeb9c9dd-58dc-3aa3-9bb3-a8a63387b195 | -8.7579 | -45.3823 | 2026-08-31 16:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 622e5b61-b1a9-3521-9a45-b9e1c4064233 | -9.694 | -65.0958 | 2026-08-31 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a1667d88-c96d-3db5-89c9-eef3f60a4dbf | -3.4185 | -61.3273 | 2026-08-31 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 17ea7a38-4831-35ae-abc6-68bf20212308 | -7.3476 | -55.1945 | 2026-08-31 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 94dc7dc6-e82e-336e-8e1c-4786f1443376 | -8.2229 | -54.9412 | 2026-08-31 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1693cb45-acd2-361a-9357-37b6dfabc27c | -8.7213 | -67.1014 | 2026-08-31 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| f3b60a07-9228-31d0-9e33-707eaa05c1c2 | -7.3087 | -72.8449 | 2026-08-31 16:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| eb5ba23b-1e9e-3aee-ad87-9e79cdf6a41f | -10.1535 | -45.721 | 2026-08-31 16:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 45e95852-e924-3ef2-830a-d68086ce2e10 | -12.209 | -50.5601 | 2026-08-31 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a4f991f4-e70c-3001-8658-82b65900689a | -3.6215 | -60.566 | 2026-08-31 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 195.5 |
| aa020f9b-1ba4-3fd0-b287-ac9dad3051af | -19.074 | -57.4084 | 2026-08-31 16:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 190.3 |
| 2559825e-40c5-3507-95b0-25721403a175 | -14.4641 | -52.1964 | 2026-08-31 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 193.2 |
| dbb003ea-a403-3dc5-b1bf-aad588149e9e | -12.3997 | -50.5585 | 2026-08-31 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| fbaa1abd-6cee-32c6-8331-ce7db0ce6a8f | -9.1544 | -59.3669 | 2026-08-31 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 8d85bdcf-6342-351f-aa4c-97098ffcd358 | -6.1109 | -57.684 | 2026-08-31 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 194.0 |
| 0038df1c-8827-3c6f-bb67-60321f25f168 | -9.4342 | -45.6704 | 2026-08-31 16:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 4441c5c9-6c26-337c-8e3f-1ba3ab77c1f6 | -9.1523 | -59.6384 | 2026-08-31 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| ac4eac42-88e0-36da-b5dc-db737050e697 | -11.1807 | -55.1024 | 2026-08-31 16:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 9b002567-d9cb-31a3-a7b1-d871dc9d0832 | -7.0057 | -59.2575 | 2026-08-31 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9efb5ded-fa8f-3ded-a4a8-0f38ec9f77b1 | -3.4002 | -61.3276 | 2026-08-31 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7689d342-3e95-3776-9eb2-0a2821669394 | -10.8025 | -50.6539 | 2026-08-31 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 73d374d4-f082-37e1-bd2a-e63d847656e0 | -9.4156 | -45.6499 | 2026-08-31 16:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| bd0a624d-12fa-367f-a3fc-0031061e9b76 | -5.9636 | -57.6704 | 2026-08-31 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c35ea11e-b719-3ead-a65d-90fce0f13b54 | -7.566 | -61.343 | 2026-08-31 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f8084b95-cfaf-3479-aa5a-44ae6a763eb1 | -11.3431 | -45.1521 | 2026-08-31 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| bf33079b-04d0-36ee-9148-e58ba831e9eb | -19.17 | -57.38 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c6aacdd0-181d-3221-9f68-f6e29a4fdf21 | -19.2 | -57.4 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ecf7fe68-f3a8-32ac-8741-c3c3d68e7083 | -11.25 | -45.15 | 2026-08-31 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7bccde3d-bce4-3535-bbdb-3b7288af4c63 | -7.98 | -44.32 | 2026-08-31 16:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ef21d2d-a011-3701-bd20-240272f41b7a | -17.85 | -52.07 | 2026-08-31 16:15:00 | MSG-03 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 74ec0d6a-13a9-374d-a09c-76f0db39f19b | -11.22 | -46.15 | 2026-08-31 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| babca752-66c0-3b08-95ac-3112ccf62f47 | -19.17 | -57.3 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ffd92c07-d45d-3506-a204-fdc3bb3cdbc4 | -17.86 | -52.13 | 2026-08-31 16:15:00 | MSG-03 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d475f58-9f1d-396c-944b-9b040daca1a7 | -19.2 | -57.33 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7561e254-58c0-3004-b1f4-0eb66f39d933 | -11.19 | -46.14 | 2026-08-31 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8ddec3d-551a-3501-8907-9a8c29dc2b13 | -19.11 | -57.41 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7b34b0e9-d346-3fd0-ba04-3e333a31c2e4 | -11.22 | -45.14 | 2026-08-31 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| deb27f09-b302-39d2-a3c9-70930ff6397f | -19.14 | -57.35 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ce9d92fe-7c46-3dd4-b587-ab93eab14b7a | -19.1 | -57.33 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ce8a78f5-3bdf-34a9-bbc1-5c1de0e5b284 | -19.14 | -57.43 | 2026-08-31 16:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c32bd091-87da-3133-9c90-38a4ddca4ffe | -3.1998 | -61.161 | 2026-08-31 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 56f689b7-9795-3653-88c8-ce477fe53984 | -3.3504 | -59.4274 | 2026-08-31 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 80e3388e-cf0c-3c2b-a42f-f5bb6d9ecdc8 | -19.074 | -57.4084 | 2026-08-31 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.3 |
| 430ed538-da79-3bc2-9433-c02e7ab45a08 | -10.8215 | -50.6519 | 2026-08-31 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 995eb016-6234-3010-bf47-0d5fbb1c66cc | -11.1809 | -55.0821 | 2026-08-31 16:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |


[Clique aqui para ver as próximas entradas](README106.md)
