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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 010ff0a2-abcd-33d4-b80a-e173acaaf896 | -11.17838 | -55.91858 | 2026-05-23 07:20:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 8200f9bd-8aa8-3644-a11b-5bfee306f930 | -12.89391 | -58.18394 | 2026-05-23 07:20:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ac1ce7b2-bf83-3c35-9b74-3bcebffc3c2b | -12.89542 | -58.17303 | 2026-05-23 07:20:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a6f96b94-09aa-3cc9-a003-2a61fa26df00 | -15.21502 | -57.65635 | 2026-05-23 07:22:00 | AQUA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0a9f22d1-2063-37e7-94ce-0dcd48bb21b6 | -15.22712 | -57.64499 | 2026-05-23 07:22:00 | AQUA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6ec98770-c018-368c-b29a-7a3ae08b54a5 | -15.22538 | -57.65782 | 2026-05-23 07:22:00 | AQUA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5e955a2d-4e1c-3615-acd3-0691bdea768b | -15.21674 | -57.64356 | 2026-05-23 07:22:00 | AQUA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f35e38a1-4dda-3eb0-94a0-f17c67456072 | -12.8859 | -58.1891 | 2026-05-23 07:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 97aa2047-2403-3812-86df-85a47a123b6f | -12.8859 | -58.1891 | 2026-05-23 07:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 28e2e53a-2d11-3738-a0a7-38c2c1e76453 | -12.8859 | -58.1891 | 2026-05-23 08:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e7ef58ef-7c5b-3f45-b950-76d97e5e988c | -12.8859 | -58.1891 | 2026-05-23 08:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 98e76963-3c42-3077-a48c-2766a4408aaf | -12.8859 | -58.1891 | 2026-05-23 09:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| fa4cc838-73ba-3d57-9286-83d4a5aeccb0 | -12.8859 | -58.1891 | 2026-05-23 09:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| bb3b9271-b998-35a8-b0e7-f7a21414d2b9 | -11.4534 | -52.9212 | 2026-05-23 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 61d91ee8-5d1b-351e-b645-9bcd6e6c4e59 | -9.4698 | -50.88558 | 2026-05-23 12:34:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 64035d07-2d60-3105-9e97-4c5ff01e18a8 | -11.27276 | -53.95544 | 2026-05-23 12:36:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6a4c8a66-5ea7-30fc-a2ce-832774f58d52 | -12.89309 | -58.17747 | 2026-05-23 12:36:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 02216ab8-459b-339d-b877-cc1b8d892651 | -11.44881 | -52.91785 | 2026-05-23 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 84991b31-7c7d-3430-825f-954d4242c08d | -14.02628 | -53.35528 | 2026-05-23 12:36:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 4cd36e08-13ed-3ca4-bf1f-8c2225103af4 | -12.5436 | -57.18502 | 2026-05-23 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 345d2166-7385-3d38-8467-77c9d14ec959 | -11.46014 | -52.9193 | 2026-05-23 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 16ab7579-9623-3a02-b507-4371ff3884f7 | -11.18058 | -55.91279 | 2026-05-23 12:36:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 4e15b94d-1329-32d5-a510-ec75c07b1ab9 | -12.54231 | -57.19421 | 2026-05-23 12:36:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 71a5d33b-79d8-37fa-8613-09f2a939aa2c | -12.89438 | -58.16849 | 2026-05-23 12:36:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d389849f-a450-3ec6-81e1-d7b950a847b7 | -14.0244 | -53.37088 | 2026-05-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1a57b9c3-ef35-3777-9d0f-731a821509f5 | -14.04717 | -53.37374 | 2026-05-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 44bcecca-9fc0-3308-bdeb-b0ef7d67a801 | -11.44687 | -52.93312 | 2026-05-23 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5cbdcfb8-a5f3-3d18-976a-57e8a96c9974 | -10.65287 | -49.73309 | 2026-05-23 12:36:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5e82b499-eaf0-3ff0-a781-3677724e675a | -10.60035 | -53.47337 | 2026-05-23 12:36:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 120653a1-b079-3918-8166-10df4a0d8c14 | -11.17926 | -55.92267 | 2026-05-23 12:36:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ef89946d-d0e3-3485-9b43-1162b741b245 | -14.01489 | -53.35383 | 2026-05-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 35.5 |
| b5d07b28-a2d1-31a4-895c-c93c70976664 | -14.01301 | -53.36948 | 2026-05-23 12:36:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6a61195a-c4d9-353a-8b8e-58fc13661e95 | -11.73496 | -54.80022 | 2026-05-23 12:36:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bfe26c1d-8efa-3dc7-ab23-1360f5068a94 | -11.4582 | -52.93451 | 2026-05-23 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 494bb3d9-0c44-3846-972e-6de6c2ca6357 | -11.4534 | -52.9212 | 2026-05-23 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 167.2 |
| b8c6155a-f2c8-34c5-9277-46f03985ce58 | -11.4531 | -52.9421 | 2026-05-23 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 361741ad-74fd-367d-9e08-e34a13b6596a | -11.4534 | -52.9212 | 2026-05-23 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 195.5 |
| b20debd5-362b-3ab7-bdee-16119432e8dc | -11.4531 | -52.9421 | 2026-05-23 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 4ecefa6e-b63b-36e8-b332-3616725a0edc | -11.4534 | -52.9212 | 2026-05-23 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 208.8 |
| 6c5602cd-0a5b-37ee-8c20-e53b58d3cbe9 | -14.0404 | -53.3669 | 2026-05-23 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| f0e23ed0-8c03-384e-bd93-72d4d6c1cfe4 | -11.4344 | -52.9231 | 2026-05-23 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| cc222342-9587-30c3-99b8-e0562b9ab591 | -11.4531 | -52.9421 | 2026-05-23 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 2517099e-2fd5-352d-ba9e-4dadd2d2e8d2 | -11.4534 | -52.9212 | 2026-05-23 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 238.8 |
| c31e1731-63d3-33ff-9896-82976a20b3e6 | -11.4531 | -52.9421 | 2026-05-23 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 144.4 |
| a22c4e3c-afd1-39de-9074-e24215b20d7d | -11.4531 | -52.9421 | 2026-05-23 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| e14cb86d-ac32-388e-8841-0eb334adc543 | -11.4534 | -52.9212 | 2026-05-23 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 261.1 |
| a0dd0202-9444-3556-8b29-d5aaa573bd1e | -11.4534 | -52.9212 | 2026-05-23 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 242.9 |
| 82d0f59d-17c0-3bf2-96e5-f4b001bc5ed3 | -11.4531 | -52.9421 | 2026-05-23 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 6c61c05c-c747-30a4-8cbe-4dc8dcb281e8 | -14.0404 | -53.3669 | 2026-05-23 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 1fd9d805-7213-30ac-862b-64b61fbb8792 | -11.4531 | -52.9421 | 2026-05-23 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 65498a1d-6f35-3bc0-96e0-6dd415827c14 | -11.4534 | -52.9212 | 2026-05-23 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 275.4 |
| 8aa5311e-8a7c-3338-b828-087cc80d4e97 | -11.4344 | -52.9231 | 2026-05-23 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 7d234b1c-a74d-3c8c-bb6b-dbac55bf492b | -11.4531 | -52.9421 | 2026-05-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 84a67ec2-180e-3af1-adb5-eec84be8c412 | -11.4344 | -52.9231 | 2026-05-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 5ff5fc0c-1a0a-36fb-b274-36452868b00e | -11.4534 | -52.9212 | 2026-05-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 264.2 |
| cf1f867b-3a0a-3973-bb40-3f887f2a9ca6 | -10.4346 | -49.9019 | 2026-05-23 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 0b28ee9f-40ff-349a-bdf4-924c365264d4 | -11.4342 | -52.9439 | 2026-05-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| f35d681c-403e-3072-81ca-4aa5bc5580f0 | -11.4344 | -52.9231 | 2026-05-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 1c61f80b-3c11-3372-b73a-a26f2f9e6975 | -11.4534 | -52.9212 | 2026-05-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 268.0 |
| fec5f020-3e96-32c8-819d-96515bccb2f4 | -11.4531 | -52.9421 | 2026-05-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 165.4 |
| a06b475e-38e9-3cfb-bb78-9fa255543f76 | -11.4344 | -52.9231 | 2026-05-23 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 85f1cb8a-ee7f-3e8a-9fca-899de4f1d437 | -12.8859 | -58.1891 | 2026-05-23 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| dc3fde04-b33f-3b0d-9571-2afb8e346440 | -11.4534 | -52.9212 | 2026-05-23 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 329.8 |
| 11dbff3c-8248-3255-9e39-cc5e2a5d0204 | -11.4531 | -52.9421 | 2026-05-23 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| af11345c-8917-364b-b9d3-8d6f54c41d2e | -10.6639 | -49.727 | 2026-05-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| ae8ca89b-3b76-3ff3-bbc8-adee297ccdae | -11.4534 | -52.9212 | 2026-05-23 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 309.5 |
| 9b10e6d5-ac2d-35fe-8d63-0fb64e2353e7 | -12.8859 | -58.1891 | 2026-05-23 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| d5e0d831-c236-3b36-87da-7edfbc4cf659 | -11.4344 | -52.9231 | 2026-05-23 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| a97e663d-5c49-3f1d-958b-e5771da1be76 | -12.8861 | -58.1692 | 2026-05-23 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 00b0ddd9-ff3a-35ff-b9b8-991188249e6b | -11.4531 | -52.9421 | 2026-05-23 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| b8a63dfd-9171-3672-80a0-2056345545a1 | -10.645 | -49.729 | 2026-05-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 2e92317c-0906-388b-9286-062a0c128b7f | -11.4531 | -52.9421 | 2026-05-23 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| b3951eaa-c894-3d90-85ef-de762257ccf3 | -12.8859 | -58.1891 | 2026-05-23 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 3e3897f2-6583-3101-8ac0-25fe6bee317f | -12.8861 | -58.1692 | 2026-05-23 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 70540251-fe3d-3ed6-a887-867bee01ce42 | -11.4344 | -52.9231 | 2026-05-23 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 63f98b7a-f7a1-3f8f-ab15-4564fa2239d2 | -11.4342 | -52.9439 | 2026-05-23 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| f3cad392-9b7b-3c42-bde0-a40606b1783b | -10.6639 | -49.727 | 2026-05-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 64f8d8d6-9dc4-368b-b285-8724d7dbd5e2 | -11.4534 | -52.9212 | 2026-05-23 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 256.5 |
| 369743a9-0f03-33c5-ba52-03b9e70c01b2 | -12.9049 | -58.1875 | 2026-05-23 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 12f7d01c-d000-38cb-b87a-6f3a4fbcc7af | -12.9052 | -58.1676 | 2026-05-23 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5e15ab3f-935b-3636-a2f1-1b69ddcfcdaa | -11.4531 | -52.9421 | 2026-05-23 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 136.9 |
| b67d1b44-a13c-341e-8bf5-a3fdeb313783 | -12.8861 | -58.1692 | 2026-05-23 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 87c2d8c8-dfd7-3b16-ad28-4481a18ad6b9 | -11.4342 | -52.9439 | 2026-05-23 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 6dc0e374-589a-33cb-9970-10d11cd01e6d | -12.8859 | -58.1891 | 2026-05-23 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3d776c5c-af21-363b-9aea-b612c351a859 | -11.4534 | -52.9212 | 2026-05-23 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 246.9 |
| e2df4301-0f7d-35c0-8ca7-853803d708ca | -11.4344 | -52.9231 | 2026-05-23 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 167.7 |


